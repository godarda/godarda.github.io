#!/usr/bin/env python3
"""
Setup Entry Point (setups/run.py)

Purpose:
This script serves as the central entry point for provisioning and running the
GoDarda website environment. It detects the host operating system and orchestrates
the setup process by invoking platform-specific logic and shared utilities.

Key Features:
1. OS Detection: Automatically identifies Windows, Linux (Ubuntu), or macOS.
2. Setup Orchestration: Delegates system package installation to platform-specific functions.
3. Repository Management: Clones the repository if missing during interactive runs.
4. Unified Execution: Provides a single command to start the environment on all platforms.
5. Environment Validation: Checks Python version and disk space.
6. Dependency Management: Installs Python and Ruby dependencies.
7. Artifact Cleanup: Removes git-ignored files and build artifacts.
8. Server Management: Handles Jekyll server lifecycle and port management.
"""

import os
import subprocess
import sys
import socket
import shutil
from pathlib import Path
from config import CONFIG


REPO_NAME = "godarda.github.io"
PERFORM_FULL_SETUP = any(arg.lower() in ("full", "-full", "--full") for arg in sys.argv[1:])


def is_internet_available():
    """
    Verify internet connectivity by connecting to public DNS endpoints.

    Returns:
        bool: True if reachable, False otherwise.
    """
    test_hosts = [("8.8.8.8", 53), ("1.1.1.1", 53)]  # Google DNS, Cloudflare DNS

    for host, port in test_hosts:
        try:
            socket.create_connection((host, port), timeout=3)
            return True
        except OSError:
            continue
    return False


def cleanup_artifacts():
    """
    Remove git-ignored files and generated site artifacts (_site).
    """
    if Path.cwd().name == REPO_NAME:
        ignore_path = Path.cwd() / ".gitignore"
        if ignore_path.exists():
            with ignore_path.open("r", encoding="utf-8") as ignore_file:
                for line in ignore_file:
                    target = line.strip()
                    if not target or target.startswith("#"):
                        continue
                    abs_path = Path.cwd() / target
                    if abs_path.is_dir():
                        shutil.rmtree(abs_path, ignore_errors=True)
                    elif abs_path.is_file():
                        try:
                            abs_path.unlink()
                        except Exception:
                            # Silently ignore removal errors to avoid interrupting setup flow.
                            pass

        site_path = Path.cwd().parent / "_site"
        if site_path.is_dir():
            shutil.rmtree(site_path, ignore_errors=True)


def release_port():
    """
    Identify and terminate processes using TCP port 4000.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        port_in_use = sock.connect_ex(('localhost', 4000)) == 0

    if port_in_use:
        system = CONFIG.SYSTEM_NAME.lower()

        if system in ("linux", "darwin"):
            cmd = "pid=$(sudo lsof -t -i:4000 2>/dev/null); if [ -n \"$pid\" ]; then sudo kill -9 $pid; fi"
        elif system == "windows":
            cmd = 'for /f "tokens=5" %a in (\'netstat -aon ^| find ":4000"\') do taskkill /f /pid %a'
        else:
            print(f"Unsupported platform: {system}. Skipping port cleanup.")
            cmd = None

        if cmd:
            exit_code = os.system(cmd)
            if exit_code != 0:
                print(f"Failed to free port 4000. Exit code: {exit_code}")


def run_command(cmd, shell=True, check=True, sudo=False):
    """
    Execute a shell command with optional sudo elevation.

    Args:
        cmd (str): Command to be executed.
        shell (bool): Whether to execute the command through the shell.
        check (bool): If True, exit the process on non-zero return codes.
        sudo (bool): If True and not on Windows, prefix the command with "sudo".
    """
    if sudo and CONFIG.SYSTEM_NAME != "Windows":
        cmd = f"sudo {cmd}"
    result = subprocess.run(cmd, shell=shell)
    if check and result.returncode != 0:
        print(f"Command failed: {cmd}")
        sys.exit(result.returncode)
    return result.returncode


def install_python_dependencies():
    """
    Install Python dependencies from requirements.txt into a virtual environment.
    """
    venv_dir = Path.cwd() / ".venv"
    python_exe = sys.executable

    if CONFIG.SYSTEM_NAME == "Darwin":
        # On macOS, ensure we use the Homebrew-installed Python for the venv
        try:
            brew_prefix = subprocess.check_output(["brew", "--prefix"], text=True, encoding="utf-8").strip()
            homebrew_python = Path(brew_prefix) / "bin" / "python3"
            if homebrew_python.exists():
                python_exe = str(homebrew_python)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Warning: Homebrew not found or 'brew --prefix' failed. Using current python for venv.")

    if not venv_dir.exists():
        print(f"Creating virtual environment in {venv_dir} using {python_exe}...")
        subprocess.run([python_exe, "-m", "venv", str(venv_dir)], check=True)

    if CONFIG.SYSTEM_NAME == "Windows":
        venv_python = venv_dir / "Scripts" / "python.exe"
        venv_playwright = venv_dir / "Scripts" / "playwright.exe"
    else:
        venv_python = venv_dir / "bin" / "python"
        venv_playwright = venv_dir / "bin" / "playwright"

    run_command(f'"{venv_python}" -m pip install --upgrade pip')
    pip_cmd = f'"{venv_python}" -m pip install --upgrade -r tests/requirements.txt'
    run_command(pip_cmd)
    print("Installing Playwright browsers...")
    playwright_cmd = f'"{venv_playwright}" install'
    if CONFIG.SYSTEM_NAME == "Linux":
        # Try installing with dependencies first; fallback to browsers-only on failure.
        if run_command(playwright_cmd + " --with-deps", check=False) != 0:
            print("Warning: Failed to install Playwright system dependencies. Attempting to install browsers only...")
            run_command(playwright_cmd)
    else:
        run_command(playwright_cmd)


def install_ruby_dependencies():
    """
    Install Ruby dependencies (Gems, Bundler) and configure the bundle.
    """
    # On macOS, Homebrew manages Ruby, and `sudo` should not be used for `gem`.
    # On Linux, we may need `sudo` if using the system Ruby.
    use_sudo = CONFIG.SYSTEM_NAME == "Linux"

    run_command("gem install bundler", sudo=use_sudo)

    if subprocess.run("bundle config set --local path .vendor/bundle", shell=True).returncode == 0:
        run_command("bundle install")
    else:
        print("Failed to set bundle config.")
        sys.exit(1)


def start_jekyll_server():
    """
    Start the Jekyll development server.
    """
    try:
        subprocess.run("bundle exec jekyll serve", shell=True, check=True)

    except KeyboardInterrupt:
        pass
    except subprocess.CalledProcessError as e:
        print(f"\nCommand failed: {e.cmd}\nExit code: {e.returncode}")
    except Exception as e:
        print(f"\nUnable to start the Jekyll server: {e}")
        print("Run this script with 'full' to install all resources - make sure you're connected to the internet.")


def orchestrate_setup(system_installer=None):
    """
    Execute the full setup workflow: checks, cleanup, installations, and server start.

    Args:
        system_installer (callable, optional): Platform-specific function to install system packages.
    """
    if PERFORM_FULL_SETUP and is_internet_available():
        if CONFIG.AVAILABLE_DISK_GB < 2.0:
            print(f"Insufficient disk space: only {CONFIG.AVAILABLE_DISK_GB:.2f} GB free. Minimum 2 GB required.")
            sys.exit(1)
        else:
            cleanup_artifacts()
            release_port()

        if system_installer:
            system_installer()

        install_python_dependencies()
        install_ruby_dependencies()

    start_jekyll_server()


def install_ubuntu_packages():
    """
    Install required system packages via APT and Snap.

    Actions:
        - Updates and upgrades APT packages.
        - Installs defined package sets (CI vs Local).
        - Installs Snap packages (VS Code, Julia) if available.
        - Clones the repository if running interactively and not present.
    """
    # Update package metadata and upgrade installed packages
    subprocess.run("sudo apt-get update -y", shell=True, check=True)
    subprocess.run("sudo apt-get full-upgrade -y", shell=True, check=True)

    # Define package sets depending on environment (local)
    packages = (
        "build-essential", "clisp", "dotnet-sdk-8.0", "finger", "freeglut3-dev",
        "git-all", "libasound2-dev", "lsof", "maxima", "mysql-server", "nasm",
        "nmap", "octave", "openjdk-21-jdk", "openjdk-21-jre", "python3-pip",
        "python3-venv", "r-base", "ruby-full", "rustc", "shc", "zlib1g-dev",
    )

    # Conditionally install snap packages only when snap is present
    has_snap = subprocess.run("snap --version", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    has_vscode = subprocess.run("code --version", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    has_julia = subprocess.run("julia --version", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0

    if has_snap and not has_vscode:
        # Install VS Code via snap if not present
        subprocess.run("sudo snap install --classic code", shell=True, check=True)
    if has_snap and not has_julia:
        # Install Julia via snap if not present
        subprocess.run("sudo snap install julia --classic", shell=True, check=True)

    # Install apt packages (best-effort). Use --ignore-missing to reduce failures.
    subprocess.run(f"sudo apt-get -y --ignore-missing install {' '.join(packages)}", shell=True, check=True)


def install_macos_packages():
    """
    Install required system packages via Homebrew.

    Actions:
        - Bootstraps Homebrew if missing.
        - Installs defined package sets (CI vs Local).
        - Installs GUI tools (VS Code, Julia) if missing.
        - Clones the repository if running interactively and not present.
    """
    # Ensure Homebrew is installed; if not, bootstrap it using the official installer.
    # The check uses subprocess.call so a non-zero return value indicates Homebrew is missing.
    if subprocess.run("brew --version", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
        subprocess.run(
            '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
            shell=True,
            check=True,
        )

    # Define package sets: broader for local development.
    packages = (
        "clisp", "dotnet-sdk", "finger", "freeglut", "git",
        "maxima", "mysql", "nasm", "nmap", "octave",
        "openjdk", "python3", "r", "ruby", "rust",
        "shc", "zlib",
    )

    # GUI tools installed via Homebrew Cask when not already present.
    # Using `brew list --cask` and `brew list` checks avoids reinstall attempts.
    if subprocess.run("brew list --cask visual-studio-code", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
        subprocess.run("brew install --cask visual-studio-code", shell=True, check=True)
    if subprocess.run("brew list julia", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
        subprocess.run("brew install julia", shell=True, check=True)

    # Install each CLI package via Homebrew. Use subprocess.run in a loop to keep behavior simple.
    subprocess.run(f"brew install {' '.join(packages)}", shell=True, check=True)

    # Add Homebrew's Ruby to the PATH for this script's execution to ensure
    # the correct `gem` and `bundle` commands are used.
    brew_prefix = subprocess.check_output(["brew", "--prefix"]).strip().decode("utf-8")
    ruby_bin_path = Path(brew_prefix) / "opt" / "ruby" / "bin"
    os.environ["PATH"] = str(ruby_bin_path) + os.pathsep + os.environ["PATH"]


def main():
    """
    Identify the OS and execute the matching setup logic.
    """

    # On interactive/local runs ensure the repository exists and we are inside it.
    cwd = Path.cwd()
    if cwd.name != REPO_NAME:
        repo_dir = cwd / REPO_NAME
        if repo_dir.is_dir():
            os.chdir(repo_dir)
        else:
            print(f"Cloning repository '{REPO_NAME}'...")
            subprocess.run(f"git clone https://github.com/godarda/{REPO_NAME}.git", shell=True, check=True)
            if repo_dir.is_dir():
                os.chdir(repo_dir)
            else:
                print(f"Error: Failed to clone and change to repository directory '{REPO_NAME}'.")
                sys.exit(1)

    system_installer = None

    if CONFIG.SYSTEM_NAME == "Linux":
        system_installer = install_ubuntu_packages
    elif CONFIG.SYSTEM_NAME == "Darwin":
        system_installer = install_macos_packages
    elif CONFIG.SYSTEM_NAME == "Windows":
        pass
    else:
        print(f"Error: Unsupported operating system '{CONFIG.SYSTEM_NAME}'.")
        sys.exit(1)

    orchestrate_setup(system_installer)

if __name__ == "__main__":
    main()
