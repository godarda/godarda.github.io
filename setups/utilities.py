#!/usr/bin/env python3
"""
Setup Utilities (setups/utilities.py)

Purpose:
This module provides shared utilities for setting up and managing the
GoDarda static site locally. It includes platform-aware helpers for
environment validation, dependency installation, and server management.

Key Features:
1. Environment Validation: Checks Python version and disk space.
2. Dependency Management: Installs Python and Ruby dependencies.
3. Artifact Cleanup: Removes git-ignored files and build artifacts.
4. Server Management: Handles Jekyll server lifecycle and port management.
"""

import os
import sys
import subprocess
import platform
import socket
import shutil
from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class EnvironmentConfig:
    OS_NAME: str
    REPO_NAME: str
    REPO_ROOT: Path
    PERFORM_FULL_SETUP: bool


def initialize_config() -> EnvironmentConfig:
    os_name = platform.system()
    repo_name = "godarda.github.io"

    # If script not already executed from repo root, attempt to change into that directory.
    cwd = Path.cwd()
    if cwd.name == repo_name:
        repo_root = cwd
    else:
        repo_root = cwd / repo_name
        if repo_root.exists():
            os.chdir(repo_root)

    perform_full_setup = any(arg.lower() in ("full", "-full", "--full") for arg in sys.argv[1:])

    return EnvironmentConfig(os_name, repo_name, repo_root, perform_full_setup)

CONFIG = initialize_config()


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


def check_system_requirements():
    """
    Validate system requirements (Python version >= 3.7, Disk space >= 2GB).

    Returns:
        bool: True if requirements are met, False otherwise.
    """
    if sys.version_info < (3, 7):
        print("Python 3.7 or later is required for setup.")
        return False

    total, used, free = shutil.disk_usage(os.getcwd())
    freedisk_gb = free // (2**30)
    if freedisk_gb < 2:
        print(f"Insufficient disk space: only {freedisk_gb} GB free. Minimum 2 GB required.")
        return False
    return True


def cleanup_artifacts():
    """
    Remove git-ignored files and generated site artifacts (_site).
    """
    if Path.cwd().name == CONFIG.REPO_NAME:
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
        system = CONFIG.OS_NAME.lower()

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
    if sudo and CONFIG.OS_NAME != "Windows":
        cmd = f"sudo {cmd}"
    result = subprocess.run(cmd, shell=shell)
    if check and result.returncode != 0:
        print(f"Command failed: {cmd}")
        sys.exit(result.returncode)


def install_python_dependencies():
    """
    Install Python dependencies from requirements.txt into a virtual environment.
    """
    venv_dir = Path.cwd() / ".venv"
    if not venv_dir.exists():
        print(f"Creating virtual environment in {venv_dir}...")
        subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)

    if CONFIG.OS_NAME == "Windows":
        pip_exe = venv_dir / "Scripts" / "pip.exe"
    else:
        pip_exe = venv_dir / "bin" / "pip"

    run_command(f'"{pip_exe}" install --upgrade pip')
    pip_cmd = f'"{pip_exe}" install --upgrade -r setups/requirements.txt'
    run_command(pip_cmd)


def install_ruby_dependencies():
    """
    Install Ruby dependencies (Gems, Bundler) and configure the bundle.
    """
    run_command("gem install rubygems-update", sudo=True)
    run_command("update_rubygems", sudo=True)
    run_command("gem install bundler", sudo=True)

    if subprocess.run("bundle config set --local path .vendor/bundle", shell=True).returncode == 0:
        run_command("bundle install")
    else:
        print("Failed to set bundle config.")
        sys.exit(1)


def orchestrate_setup(system_installer=None):
    """
    Execute the full setup workflow: checks, cleanup, installations, and server start.

    Args:
        system_installer (callable, optional): Platform-specific function to install system packages.
    """
    if CONFIG.PERFORM_FULL_SETUP and is_internet_available():
        if check_system_requirements():
            cleanup_artifacts()
            release_port()

        if system_installer:
            system_installer()

        install_python_dependencies()
        install_ruby_dependencies()

    start_jekyll_server()


def clean_pycache(cache_path: str | None = None) -> None:
    """
    Recursively remove __pycache__ directories.

    Args:
        cache_path (str | None): Target directory. Defaults to the script's parent.
    """
    try:
        p = (
            Path(cache_path)
            if cache_path
            else Path(__file__).resolve().parent / "__pycache__"
        )
        if p.name != "__pycache__":
            p = p / "__pycache__"
        if p.exists():
            shutil.rmtree(p)
    except Exception as e:
        print(f"Cleanup warning (could not remove {cache_path or 'default'}): {e}")


def start_jekyll_server():
    """
    Start the Jekyll development server.
    """
    clean_pycache()
    try:
        subprocess.run("bundle exec jekyll serve", shell=True, check=True)

    except KeyboardInterrupt:
        pass
    except subprocess.CalledProcessError as e:
        print(f"\nCommand failed: {e.cmd}\nExit code: {e.returncode}")
    except Exception as e:
        print(f"\nUnable to start the Jekyll server: {e}")
        print("Run this script with 'full' to install all resources - make sure you're connected to the internet.")
