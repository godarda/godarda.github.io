#!/usr/bin/env python3
"""
Author: Shubham Darda
Description:
    Ubuntu convenience helpers for provisioning and running the GoDarda website locally.

    This module provides a small wrapper around system package installation and the
    default startup flow used on Ubuntu-based development hosts or CI runners.
    It intentionally keeps behavior imperative and minimal — it invokes system package
    managers (apt/snap) and relies on the shared utilities module for environment
    validation, dependency installation, cleanup and server lifecycle.

    Safety / operational notes:
    - Many commands in this script require elevated privileges (sudo). Run only on
      trusted machines and review commands before execution.
    - This script is tailored to Ubuntu/Debian environments. Do not run on other
      distributions without adjusting package names and package manager calls.
    - The script uses a basic "full" CLI flag and a lightweight internet check to
      decide whether to perform a complete provisioning flow vs. only starting the server.

Usage:
    - Run from the repository root (or let utilities.py change into the repo root).
    - To perform a full provisioning flow: python3 setups/ubuntu.py full
    - To only attempt to start the server: python3 setups/ubuntu.py

"""

from utilities import *
import os
import subprocess


def install_packages():
    """
    Install system-level packages required to build and serve the site on Ubuntu.

    Behavior:
    - Performs an apt update and full-upgrade to ensure package metadata is current.
    - Installs a curated list of packages. The list is narrower in CI (githubactions)
      to reduce runtime and avoid interactive installs; for local development a
      broader set of developer tools is installed.
    - Uses snap to install Visual Studio Code and Julia when available on the host
      and not already installed.
    - If not running inside GitHub Actions and the repository is missing locally,
      the repository will be cloned and the working directory adjusted.
    - Delegates Ruby/Python gem and pip installs to install_dependencies() from utilities.

    Important:
    - All apt/snap commands use system calls that will require sudo. The caller of
      this function must be prepared to provide credentials or run the script with sudo.
    - The function deliberately tolerates missing packages via --ignore-missing and
      continues on best-effort.
    """
    # Update package metadata and upgrade installed packages
    os.system("sudo apt-get update -y")
    os.system("sudo apt-get full-upgrade -y")

    # Define package sets depending on environment (CI vs local)
    if githubactions:
        packages = "ruby-full clisp rustc freeglut3-dev nasm shc"
    else:
        packages = (
            "python3-pip git-all openjdk-21-jre openjdk-21-jdk ruby-full "
            "build-essential zlib1g-dev dotnet-sdk-8.0 r-base octave clisp maxima "
            "rustc freeglut3-dev mysql-server nasm nmap shc finger"
        )

        # Conditionally install snap packages only when snap is present
        snap = os.system("snap --version > /dev/null")
        vscode = os.system("code --version > /dev/null")
        julia = os.system("julia --version > /dev/null")
        if snap == 0 and vscode != 0:
            # Install VS Code via snap if not present
            os.system("sudo snap install --classic code")
        if snap == 0 and julia != 0:
            # Install Julia via snap if not present
            os.system("sudo snap install julia --classic")

    # Install apt packages (best-effort). Use --ignore-missing to reduce failures.
    cmd = "sudo apt-get -y --ignore-missing install "
    for pkg in packages.split():
        command = str(cmd) + str(pkg)
        subprocess.run(command.split())

    # On interactive/local runs ensure the repo exists; clone it if absent.
    if not githubactions:
        if repo not in os.getcwd():
            os.system("git clone https://github.com/godarda/godarda.github.io.git")
            os.chdir(target_dir + "/")

    # Install language-level dependencies (Ruby gems, pip requirements, bundler)
    install_dependencies()


def main():
    """
    Entrypoint for the Ubuntu setup flow.

    Flow:
    - If the "full" CLI flag was provided and basic internet connectivity is available:
        1) Run environment validation and destructive cleanup (ensure_setup_with_cleanup).
        2) Install required system packages (install_packages).
        3) Start or build the Jekyll site (start_server).
    - Otherwise only attempt to start the server (start_server).

    Rationale:
    - The internet check prevents long-running package installs when offline.
    - The "full" flag gates potentially destructive cleanup operations and heavy installs.
    """
    if full and is_internet_available():
        ensure_setup_with_cleanup()
        install_packages()
        start_server()
    else:
        start_server()


if __name__ == "__main__":
    main()