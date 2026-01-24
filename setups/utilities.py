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

# Determine OS name once for reuse (used by run_command/install logic)
OS_NAME = platform.system()

# Detect GitHub Actions environment to alter behavior (e.g. build instead of serve)
IS_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS", "").lower() == "true"

# GitHub repository name
REPO_NAME = "godarda.github.io"

# If script not already executed from repo root, attempt to change into that directory.
# This is a convenience for running the script from other locations in CI or local shells.
CWD = Path.cwd()
if CWD.name == REPO_NAME:
    REPO_ROOT = CWD
else:
    REPO_ROOT = CWD / REPO_NAME
    if REPO_ROOT.exists():
        os.chdir(REPO_ROOT)

# "full" CLI flag enables additional install/cleanup behavior (e.g. remove ignored files,
# perform dependency installs). Case-insensitive. Recognizes "full", "-full", "--full".
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
            # Try the next host; a single host being unreachable does not imply no internet.
            continue
    return False


def check_system_requirements():
    """
    Validate system requirements (Python version >= 3.7, Disk space >= 2GB).

    Returns:
        bool: True if requirements are met, False otherwise.
    """
    # Validate minimum Python version
    if sys.version_info < (3, 7):
        print("Python 3.7 or later is required for setup.")
        return False

    # Ensure at least 2 GB of free disk space in current working directory
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
    # If we are at repository root, perform .gitignore-based cleanup and remove _site
    if Path.cwd().name == REPO_NAME:
        ignore_path = Path.cwd() / ".gitignore"
        if ignore_path.exists():
            # Read each non-empty line and attempt to remove the referenced path.
            # This is a best-effort cleanup; failures are tolerated.
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

        # Remove _site directory one level up if present (common Jekyll output location)
        site_path = Path.cwd().parent / "_site"
        if site_path.is_dir():
            shutil.rmtree(site_path, ignore_errors=True)


def release_port():
    """
    Identify and terminate processes using TCP port 4000.
    """
    # Check if port 4000 is currently in use (Jekyll default). If in use, attempt to free it.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        port_in_use = sock.connect_ex(('localhost', 4000)) == 0

    if port_in_use:
        system = OS_NAME.lower()

        # Build platform-specific command to kill the process using port 4000.
        # These commands are executed via the shell and may require elevated privileges.
        if system in ("linux", "darwin"):
            cmd = "pid=$(sudo lsof -t -i:4000 2>/dev/null); if [ -n \"$pid\" ]; then sudo kill -9 $pid; fi"
        elif system == "windows":
            cmd = 'for /f "tokens=5" %a in (\'netstat -aon ^| find ":4000"\') do taskkill /f /pid %a'
        else:
            print(f"Unsupported platform: {system}. Skipping port cleanup.")
            cmd = None

        # Execute cleanup command if applicable and report non-zero exit codes.
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
    if sudo and OS_NAME != "Windows":
        cmd = f"sudo {cmd}"
    result = subprocess.run(cmd, shell=shell)
    if check and result.returncode != 0:
        print(f"Command failed: {cmd}")
        sys.exit(result.returncode)


def install_python_dependencies():
    """
    Install Python dependencies from requirements.txt.
    """
    # Python dependencies
    pip_cmd = "pip install --user --upgrade -r setups/requirements.txt"
    if OS_NAME != "Windows":
        pip_cmd += " --break-system-packages --no-warn-script-location"
    run_command(pip_cmd)


def install_ruby_dependencies():
    """
    Install Ruby dependencies (Gems, Bundler) and configure the bundle.
    """
    # RubyGems and bundler installation/update
    run_command("gem install rubygems-update", sudo=True)
    run_command("update_rubygems", sudo=True)
    run_command("gem install bundler", sudo=True)

    # Configure bundler to use vendor/bundle and run bundle install
    if subprocess.run("bundle config set --local path vendor/bundle", shell=True).returncode == 0:
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
    if PERFORM_FULL_SETUP and is_internet_available():
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
        # If caller passed a parent folder (not named __pycache__), remove its __pycache__ child
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
        # Allow clean exit on Ctrl-C during local serve
        pass
    except subprocess.CalledProcessError as e:
        # Report failing external command and its exit code
        print(f"\nCommand failed: {e.cmd}\nExit code: {e.returncode}")
    except Exception as e:
        # Generic catch-all with guidance for remediation
        print(f"\nUnable to start the Jekyll server: {e}")
        print("Run this script with 'full' to install all resources - make sure you're connected to the internet.")
