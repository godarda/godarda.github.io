#!/usr/bin/env python3
"""
Test Reporting Utilities (tests/report.py)

Purpose:
This module handles the generation of console reports for the test suite.
It summarizes test execution statistics, details failures, and lists
installed development tool versions.

Key Features:
1. Statistics: Displays pass/fail counts for title verification and compilation.
2. Diagnostics: Lists specific unmatched titles or uncompiled files.
3. Environment: Reports versions of installed compilers and tools.
"""

import subprocess
import platform
from utilities import STATS, CONFIG


def get_version(cmd: str) -> str:
    """
    Retrieves the version string of a tool by executing a shell command.

    Returns:
        The version string if successful, otherwise a default error message.
    """
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout.strip() or result.stderr.strip()
        return (
            output.splitlines()[0]
            if result.returncode == 0 and output
            else "Not installed"
        )
    except Exception:
        return "Not installed or retrieval failed"


def get_all_versions(os_name: str) -> dict:
    """
    Collects version information for common development tools.
    """
    versions = {"OS": platform.platform()}
    tools = {
        "gcc/g++": "g++ --version",
        "Rust": "rustc --version",
        "NASM": "nasm --version",
        "Java": "javac --version",
        "Python": "python3 --version",
        "Ruby": "ruby -v",
        "Gem": "gem -v",
        "Bundler": "bundler -v",
        "Jekyll": "bundle exec jekyll -v",
    }

    for tool, cmd in tools.items():
        versions[tool] = get_version(cmd)
    return versions


def print_report(
    matched: int, unmatched: int, passed: int, failed: int
) -> None:
    """
    Generates and prints the final test execution report.
    """
    total_urls = matched + unmatched
    total_files = passed + failed

    # --------------------------------------------------------------------------
    # Title Verification Report
    # --------------------------------------------------------------------------
    if total_urls:
        print("\nTitle Verification Report")
        print("-" * 100)

        if STATS.unmatched:
            print(f"{'Status':<10} {'URL':<32} {'Expected Title'}")
            print("-" * 100)
            for url, title in STATS.unmatched_entries:
                print(f"\033[91m{'Unmatched':<10}\033[0m {url:<32} {title}")
            print("-" * 100)
        else:
            print("All page titles matched expected values.")

        print(f"{'Total URLs Checked':<25}: {total_urls}")
        print(f"{'Titles Matched':<25}: \033[92m{STATS.matched}\033[0m")
        print(f"{'Titles Unmatched':<25}: \033[91m{STATS.unmatched}\033[0m")

    # --------------------------------------------------------------------------
    # Code Compilation Report
    # --------------------------------------------------------------------------
    if total_files:
        print("\nCode Compilation Report")
        print("-" * 100)

        if STATS.uncompiled:
            print(f"{'Status':<10} {'File':<10}")
            print("-" * 100)
            for src in STATS.uncompiled_entries:
                print(f"\033[91m{'Uncompiled':<10}\033[0m {src:<10}")
            print("-" * 100)
        else:
            print("All source files compiled successfully.")

        print(f"{'Total Files Processed':<25}: {total_files}")
        print(f"{'Compilation Passed':<25}: \033[92m{passed}\033[0m")
        print(f"{'Compilation Failed':<25}: \033[91m{failed}\033[0m")

    # --------------------------------------------------------------------------
    # Toolchain Version Report
    # --------------------------------------------------------------------------
    print("\nResource Versions Report")
    print("-" * 100)

    versions = get_all_versions(CONFIG.OS_NAME)
    for tool, ver in versions.items():
        if "Not installed" not in ver:
            print(f"{tool:<25}: {ver}")
