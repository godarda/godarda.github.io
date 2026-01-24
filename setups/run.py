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
"""

import os
import subprocess
import sys

from utilities import CONFIG, orchestrate_setup


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
        "git-all", "lsof", "maxima", "mysql-server", "nasm",
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


def main():
    """
    Identify the OS and execute the matching setup logic.
    """

    # On interactive/local runs ensure the repository exists; clone it if absent.
    if CONFIG.REPO_NAME not in os.getcwd():
        subprocess.run("git clone https://github.com/godarda/godarda.github.io.git", shell=True, check=True)
        if os.path.isdir(CONFIG.REPO_NAME):
            os.chdir(CONFIG.REPO_NAME)

    system_installer = None

    if CONFIG.OS_NAME == "Linux":
        system_installer = install_ubuntu_packages
    elif CONFIG.OS_NAME == "Darwin":
        system_installer = install_macos_packages
    elif CONFIG.OS_NAME == "Windows":
        pass
    else:
        print(f"Error: Unsupported operating system '{CONFIG.OS_NAME}'.")
        sys.exit(1)

    orchestrate_setup(system_installer)

if __name__ == "__main__":
    main()