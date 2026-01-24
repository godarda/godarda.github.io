#!/usr/bin/env python3
"""
Ubuntu Setup Script (setups/ubuntu.py)

Purpose:
This script handles the provisioning and execution of the GoDarda website
environment on Ubuntu. It manages APT/Snap package installations and delegates
core setup tasks to shared utilities.

Key Features:
1. Package Management: Installs system packages via APT and Snap.
2. Environment Setup: Validates environment and installs dependencies.
3. Server Lifecycle: Starts the Jekyll server for local development.
4. Automation: Supports full provisioning via CLI flags.
"""

from utilities import *


def install_packages():
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

    # Define package sets depending on environment (CI vs local)
    if IS_GITHUB_ACTIONS:
        packages = "ruby-full clisp rustc freeglut3-dev nasm shc"
    else:
        packages = (
            "python3-pip git-all openjdk-21-jre openjdk-21-jdk ruby-full "
            "build-essential zlib1g-dev dotnet-sdk-8.0 r-base octave clisp maxima "
            "rustc freeglut3-dev mysql-server nasm nmap shc finger lsof"
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
    subprocess.run(f"sudo apt-get -y --ignore-missing install {packages}", shell=True, check=True)

    # On interactive/local runs ensure the repo exists; clone it if absent.
    if not IS_GITHUB_ACTIONS:
        if REPO_NAME not in os.getcwd():
            subprocess.run("git clone https://github.com/godarda/godarda.github.io.git", shell=True, check=True)
            os.chdir(str(REPO_ROOT))


def main():
    """
    Execute the Ubuntu setup orchestration.

    Delegates to `orchestrate_setup` with the Ubuntu-specific package installer.
    """
    orchestrate_setup(install_packages)


if __name__ == "__main__":
    main()