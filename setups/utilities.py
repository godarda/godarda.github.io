#!/usr/bin/env python3
"""
Author: Shubham Darda
Purpose:
    Helper utilities to set up and run the GoDarda static site locally (development/CI).
    This module provides environment validation, dependency installation helpers,
    lightweight cleanup routines and a convenience function to start the Jekyll server.

Guidelines:
    - Keep logic platform-aware (Windows vs POSIX).
    - Keep CLI-friendly behavior: inspect sys.argv for a "full" flag to enable full install/cleanup flows.
    - Minimal external side-effects unless explicitly requested (e.g. deleting git-ignored files when in repo root).
"""

import os
import sys
import subprocess
import platform
import socket
import shutil
from pathlib import Path

# Determine OS name once for reuse (used by run_command/install logic)
os_name = platform.system()

# Detect GitHub Actions environment to alter behavior (e.g. build instead of serve)
githubactions = os.getenv("GITHUB_ACTIONS", "").lower() == "true"

# GitHub repository name
repo = "godarda.github.io"

# If script not already executed from repo root, attempt to change into that directory.
# This is a convenience for running the script from other locations in CI or local shells.
target_dir = os.path.join(os.getcwd(), repo)
if repo not in os.getcwd():
    os.chdir(target_dir)

# "full" CLI flag enables additional install/cleanup behavior (e.g. remove ignored files,
# perform dependency installs). Case-insensitive. Recognizes "full", "-full", "--full".
full = any(arg.lower() in ("full", "-full", "--full") for arg in sys.argv[1:])


def is_internet_available():
    """
    Quick network check to determine if the host has internet access.

    Strategy:
        Attempt to open a TCP connection to well-known public DNS endpoints (Google/Cloudflare)
        on DNS port 53. If a connection to at least one host succeeds within the timeout,
        return True. Otherwise return False.

    Returns:
        bool: True when the internet appears reachable, False otherwise.

    Note:
        This is a lightweight connectivity check and not a full HTTP probe. It is intended
        only to gate actions that require network access (e.g. package installs).
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


def ensure_setup_with_cleanup():
    """
    Validate environment and perform optional cleanup.

    Actions performed:
    - Enforce minimum Python version (>= 3.7).
    - Verify at least 2 GB free disk space in the current working directory.
    - When executed from the repository root and a ".gitignore" exists:
        - Remove each path listed in .gitignore (files or directories). This is intended
          for local development when a full reset is desired.
    - Remove the generated "_site" directory located at repo_parent/_site when present.
    - Detect if TCP port 4000 is in use and attempt to free it using a platform-appropriate command.

    Safety notes:
    - Deletions use shutil.rmtree with ignore_errors=True where applicable. Use with care:
      this function performs destructive operations when run from the repo root.
    - Port cleanup uses shell commands and may require privileges (e.g. sudo on Unix).
    """
    # Validate minimum Python version
    if sys.version_info < (3, 7):
        print("Python 3.7 or later is required for setup.")
        return

    # Ensure at least 2 GB of free disk space in current working directory
    total, used, free = shutil.disk_usage(os.getcwd())
    freedisk_gb = free // (2**30)
    if freedisk_gb < 2:
        print(f"Insufficient disk space: only {freedisk_gb} GB free. Minimum 2 GB required.")
        return

    # If we are at repository root, perform .gitignore-based cleanup and remove _site
    current_dir = os.path.basename(os.getcwd())
    if current_dir == repo:
        ignore_path = os.path.abspath(os.path.join(os.getcwd(), ".gitignore"))
        if os.path.exists(ignore_path):
            # Read each non-empty line and attempt to remove the referenced path.
            # This is a best-effort cleanup; failures are tolerated.
            with open(ignore_path, "r") as ignore_file:
                for line in ignore_file:
                    target = line.strip()
                    if not target:
                        continue
                    abs_path = os.path.abspath(os.path.join(os.getcwd(), target))
                    if os.path.isdir(abs_path):
                        shutil.rmtree(abs_path, ignore_errors=True)
                    elif os.path.isfile(abs_path):
                        try:
                            os.remove(abs_path)
                        except Exception:
                            # Silently ignore removal errors to avoid interrupting setup flow.
                            pass

        # Remove _site directory one level up if present (common Jekyll output location)
        site_path = os.path.abspath(os.path.join(os.getcwd(), "..", "_site"))
        if os.path.isdir(site_path):
            shutil.rmtree(site_path, ignore_errors=True)

    # Check if port 4000 is currently in use (Jekyll default). If in use, attempt to free it.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        port_in_use = sock.connect_ex(('localhost', 4000)) == 0

    if port_in_use:
        system = platform.system().lower()

        # Build platform-specific command to kill the process using port 4000.
        # These commands are executed via the shell and may require elevated privileges.
        if system in ("linux", "darwin"):
            cmd = "sudo kill -9 $(sudo lsof -t -i:4000) 2>/dev/null"
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
    Wrapper around subprocess.run for running short shell commands.

    Parameters:
        cmd (str): Command to be executed.
        shell (bool): Whether to execute the command through the shell.
        check (bool): If True, exit the process on non-zero return codes.
        sudo (bool): If True and not on Windows, prefix the command with "sudo".

    Behavior:
        - Prints an error and exits with the subprocess return code if check is True and the command fails.
    """
    if sudo and os_name != "Windows":
        cmd = f"sudo {cmd}"
    result = subprocess.run(cmd, shell=shell)
    if check and result.returncode != 0:
        print(f"Command failed: {cmd}")
        sys.exit(result.returncode)


def install_dependencies():
    """
    Install required Python and Ruby dependencies for local development.

    Steps:
        - Install Python packages from setups/requirements.txt into the user environment.
          On non-Windows platforms, include flags to avoid interfering with system packages.
        - Install/upgrade RubyGems, Bundler and perform bundler install/update steps.
        - Configure bundle to install into vendor/bundle so site-local gems are used.

    Notes:
        - Many commands here are executed with elevated privileges (sudo) on POSIX systems.
          Ensure the executing user has appropriate permissions.
        - This function assumes Ruby and the gem/bundle tools are already available on PATH.
    """
    # Python dependencies
    pip_cmd = "pip install --user --upgrade -r setups/requirements.txt"
    if os_name != "Windows":
        pip_cmd += " --break-system-packages --no-warn-script-location"
    run_command(pip_cmd)

    # RubyGems and bundler installation/update
    run_command("gem install rubygems-update", sudo=True)
    run_command("update_rubygems", sudo=True)
    run_command("gem install bundler", sudo=True)

    # Configure bundler to use vendor/bundle and run bundle install/update flows
    if subprocess.run("bundle config set --local path vendor/bundle", shell=True).returncode == 0:
        run_command("bundle install")
        run_command("bundle update --bundler")
        run_command("bundle update --all")
    else:
        print("Failed to set bundle config.")
        sys.exit(1)


def clean_pycache(cache_path: str | None = None) -> None:
    """
    Remove a __pycache__ directory.

    If cache_path is provided:
        - If cache_path points to a __pycache__ directory it will be removed.
        - If cache_path points to a parent directory, the function will remove its __pycache__ child.
    If cache_path is None, the function removes the __pycache__ directory adjacent to this file.

    Exceptions are caught and printed as warnings (non-fatal).
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


def start_server():
    """
    Start or build the Jekyll site.

    Behavior:
        - Cleans local __pycache__ directory.
        - Runs 'bundle exec jekyll serve' to start a local dev server.

    Error handling:
        - KeyboardInterrupt is swallowed to allow graceful Ctrl-C.
        - subprocess.CalledProcessError prints the failing command and exit code.
        - Any other exception prints a helpful note suggesting the 'full' flag and internet connectivity.
    """
    clean_pycache()
    try:
        def run_cmd(cmd):
            """
            Helper to run a command and return its stdout decoded to UTF-8.

            Exits the process with a helpful message if the command fails.
            """
            try:
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                return output.decode("utf-8").strip()
            except Exception:
                print("Run this script with 'full' to install all resources - make sure you're connected to the internet.")
                sys.exit(1)
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
