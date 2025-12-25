#!/usr/bin/env python
"""
Author: Shubham Darda
Description:
    Windows convenience entrypoint for provisioning and running the GoDarda website locally.

    This module exposes a minimal, Windows-focused startup flow. It delegates core
    responsibilities to the shared utilities module (utilities.py) and intentionally
    keeps logic small: validate environment / perform optional full provisioning,
    then start or build the Jekyll site.

Operational notes:
    - The "full" CLI flag (see utilities.py) enables a more comprehensive flow:
        * ensure_setup_with_cleanup()   - environment validation and optional cleanup
        * install_dependencies()        - language/package dependency installation
        * start_server()                - start or build the Jekyll site
      When "full" is not provided, the script only attempts to start the server.
    - Many dependency installation steps may require elevated privileges or additional
      Windows tooling (e.g. Chocolatey, Ruby, Bundler). Review utilities.install_dependencies()
      for platform-specific behavior.
    - This file is intentionally small and defers heavy lifting to utilities to keep
      platform differences consolidated and maintainable.

Usage:
    - Run from the repository root (or let utilities.py change into the repo root).
    - To perform a full provisioning flow: python setups/windows.py full
    - To only attempt to start the server: python setups/windows.py

Safety:
    - The "full" flow may remove files or alter the system environment. Run only on
      trusted machines and review commands before execution.
"""
from utilities import *


def main():
    """
    Windows setup entrypoint.

    Behavior:
    - If the 'full' CLI flag is present and basic internet connectivity is available:
        perform environment validation, install dependencies, then start/build the site.
    - Otherwise, only attempt to start the Jekyll server.

    The function intentionally performs minimal control flow and relies on utilities
    for platform-specific operations and safety checks.
    """
    if full and is_internet_available():
        ensure_setup_with_cleanup()
        install_dependencies()
        start_server()
    else:
        start_server()


if __name__ == "__main__":
    main()