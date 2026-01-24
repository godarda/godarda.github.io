#!/usr/bin/env python3
"""
Windows Setup Script (setups/windows.py)

Purpose:
This script serves as the entry point for provisioning and running the
GoDarda website on Windows. It delegates environment validation, dependency
management, and server lifecycle to shared utilities.

Key Features:
1. Entry Point: Initiates the setup process for Windows environments.
2. Delegation: Relies on shared utilities for platform-agnostic logic.
3. Automation: Supports full provisioning via CLI flags.
"""
from utilities import *


def main():
    """
    Execute the Windows setup orchestration.

    Delegates to `orchestrate_setup` (no system-level package installer required for Windows in this context).
    """
    orchestrate_setup()


if __name__ == "__main__":
    main()