#!/usr/bin/env python3
"""
Author: Shubham Darda
Description:
    macOS convenience helpers for provisioning and running the GoDarda website locally.

    This module provides an imperative, minimal wrapper around Homebrew package
    management and the default startup flow used on macOS development hosts or CI.
    It relies on the shared utilities module for environment validation, dependency
    installation, cleanup, and server lifecycle.

Guidelines / Operational notes:
    - Intended for macOS only. Homebrew and its casks are required for many operations.
    - Many commands will prompt for credentials or require elevated privileges
      depending on the host configuration; run on trusted machines only.
    - The "full" CLI flag (see utilities.py) enables destructive cleanup and full
      provisioning. Use with caution.
    - The script uses a lightweight internet check to gate long-running installs.

Usage:
    - Run from the repository root (or let utilities.py change into the repo root).
    - To perform a full provisioning flow: python setups/macos.py full
    - To only attempt to start the server: python setups/macos.py
"""
from utilities import *
import subprocess  # subprocess is used for shell operations invoked below


def install_packages():
    """
    Install system-level packages on macOS using Homebrew.

    Behavior:
    - Ensures Homebrew is available and installs it if absent.
    - Defines a compact package set for CI and a broader set for local development.
    - Installs GUI tools (VS Code, Julia) via Homebrew casks when appropriate.
    - Installs CLI packages via `brew install`.
    - Ensures the repository is present locally (clones if missing when running interactively).
    - Delegates language-level dependency installation to install_dependencies() from utilities.

    Safety:
    - This function performs networked installs and may change system state.
    - Review package lists before running in production-like environments.
    """
    # Ensure Homebrew is installed; if not, bootstrap it using the official installer.
    # The check uses subprocess.call so a non-zero return value indicates Homebrew is missing.
    if subprocess.call("brew --version", shell=True) != 0:
        subprocess.run(
            '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
            shell=True,
        )

    # Define package sets: minimal for CI, broader for local development.
    if githubactions:
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
        if subprocess.call("brew list --cask visual-studio-code >/dev/null 2>&1", shell=True) != 0:
            subprocess.run("brew install --cask visual-studio-code", shell=True)
        if subprocess.call("brew list julia >/dev/null 2>&1", shell=True) != 0:
            subprocess.run("brew install julia", shell=True)

    # Install each CLI package via Homebrew. Use subprocess.run in a loop to keep behavior simple.
    for pkg in packages:
        subprocess.run(f"brew install {pkg}", shell=True)

    # On interactive/local runs ensure the repository exists; clone it if absent.
    # We avoid cloning in CI to keep the job lean and predictable.
    if not githubactions:
        if repo not in os.getcwd():
            subprocess.run("git clone https://github.com/godarda/godarda.github.io.git", shell=True)
            os.chdir(target_dir + "/")

    # Install language-level dependencies (Ruby gems, pip requirements, bundler).
    # This delegates to utilities.install_dependencies(), keeping provisioning responsibilities separated.
    install_dependencies()


def main():
    """
    Entrypoint for the macOS setup flow.

    Flow:
    - If the "full" CLI flag is provided and the host has internet connectivity:
        1) Run environment validation and optional destructive cleanup (ensure_setup_with_cleanup).
        2) Install system packages via Homebrew (install_packages).
        3) Start or build the Jekyll site (start_server).
    - Otherwise, attempt only to start the site server (start_server).

    Rationale:
    - The internet connectivity check avoids wasted effort when offline.
    - The "full" flag gates potentially destructive cleanup and heavy installs.
    """
    if full and is_internet_available():
        ensure_setup_with_cleanup()
        install_packages()
        start_server()
    else:
        start_server()


if __name__ == "__main__":
    main()