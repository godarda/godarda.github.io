#!/usr/bin/env python3
"""
macOS Setup Script (setups/macos.py)

Purpose:
This script handles the provisioning and execution of the GoDarda website
environment on macOS. It manages Homebrew package installations and delegates
core setup tasks to shared utilities.

Key Features:
1. Package Management: Installs system packages via Homebrew.
2. Environment Setup: Validates environment and installs dependencies.
3. Server Lifecycle: Starts the Jekyll server for local development.
4. Automation: Supports full provisioning via CLI flags.
"""
from utilities import *


def install_packages():
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

    # Define package sets: minimal for CI, broader for local development.
    if IS_GITHUB_ACTIONS:
        packages = ["ruby", "clisp", "rust", "freeglut", "nasm", "shc"]
    else:
        packages = [
            "python3",
            "git",
            "openjdk",
            "ruby",
            "zlib",
            "dotnet-sdk",
            "r",
            "octave",
            "clisp",
            "maxima",
            "rust",
            "freeglut",
            "mysql",
            "nasm",
            "nmap",
            "shc",
            "finger",
        ]

        # GUI tools installed via Homebrew Cask when not already present.
        # Using `brew list --cask` and `brew list` checks avoids reinstall attempts.
        if subprocess.run("brew list --cask visual-studio-code", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
            subprocess.run("brew install --cask visual-studio-code", shell=True, check=True)
        if subprocess.run("brew list julia", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
            subprocess.run("brew install julia", shell=True, check=True)

    # Install each CLI package via Homebrew. Use subprocess.run in a loop to keep behavior simple.
    subprocess.run(f"brew install {' '.join(packages)}", shell=True, check=True)

    # On interactive/local runs ensure the repository exists; clone it if absent.
    # We avoid cloning in CI to keep the job lean and predictable.
    if not IS_GITHUB_ACTIONS:
        if REPO_NAME not in os.getcwd():
            subprocess.run("git clone https://github.com/godarda/godarda.github.io.git", shell=True, check=True)
            os.chdir(str(REPO_ROOT))


def main():
    """
    Execute the macOS setup orchestration.

    Delegates to `orchestrate_setup` with the macOS-specific package installer.
    """
    orchestrate_setup(install_packages)


if __name__ == "__main__":
    main()