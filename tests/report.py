#!/usr/bin/env python3
"""
Author: Shubham Darda

Purpose:
    Reporting helpers used by the automated test suite for the GoDarda website.

Description:
    This module centralizes functionality that prints consolidated, human-readable
    reports for CI and local runs. Reports include:
      - Title verification results (matched / unmatched)
      - Code compilation outcomes (passed / failed)
      - Installed toolchain and browser versions

    Reports are intentionally concise and formatted for readability in CI logs.
    Keep output deterministic and avoid side-effects beyond printing.

Guidelines:
    - Keep functions focused and easy to read.
    - Use the utilities.stats object for shared test counters.
    - Prefer stable, minimal external calls when probing the environment (used
      by get_all_versions).
"""

import subprocess
import platform
from utilities import stats


def get_version(cmd: str) -> str:
    """
    Execute a shell command to retrieve a tool's version.
    Returns the trimmed stdout on success or a standardized error message on failure.
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
    Retrieve versions of common development tools and browsers across Ubuntu and macOS.
    """
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
        "Chrome": (
            "google-chrome --version"
            if os_name == "Linux"
            else "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --version"
        ),
        "Safari": (
            "defaults read /Applications/Safari.app/Contents/Info CFBundleShortVersionString"
            if os_name == "Darwin"
            else None
        ),
    }

    return {tool: get_version(cmd) for tool, cmd in tools.items()}


def print_report(
    matched: int, unmatched: int, passed: int, failed: int, browser: str
) -> None:
    """
    Generate and print a consolidated report including:
      1. Title verification results
      2. Compilation outcomes
      3. Installed toolchain and browser versions
    """
    total_urls = matched + unmatched
    total_files = passed + failed
    os_name = platform.system()

    # --------------------------------------------------------------------------
    # Title Verification Report
    # --------------------------------------------------------------------------
    if total_urls:
        print("\nTitle Verification Report")
        print("-" * 100)

        if stats.unmatched:
            print(f"{'Status':<10} {'URL':<32} {'Expected Title'}")
            print("-" * 100)
            for url, title in stats.unmatched_entries:
                print(f"\033[91m{'Unmatched':<10}\033[0m {url:<32} {title}")
            print("-" * 100)
        else:
            print("All page titles matched expected values.")

        print(f"{'Total URLs Checked':<25}: {total_urls}")
        print(f"{'Titles Matched':<25}: \033[92m{stats.matched}\033[0m")
        print(f"{'Titles Unmatched':<25}: \033[91m{stats.unmatched}\033[0m")

    # --------------------------------------------------------------------------
    # Code Compilation Report
    # --------------------------------------------------------------------------
    if total_files:
        print("\nCode Compilation Report")
        print("-" * 100)

        if stats.uncompiled:
            print(f"{'Status':<10} {'File':<10}")
            print("-" * 100)
            for src in stats.uncompiled_entries:
                print(f"\033[91m{'Uncompiled':<10}\033[0m {src:<10}")
            print("-" * 100)
        else:
            print("All source files compiled successfully.")

        print(f"{'Total Files Processed':<25}: {total_files}")
        print(f"{'Compilation Passed':<25}: \033[92m{passed}\033[0m")
        print(f"{'Compilation Failed':<25}: \033[91m{failed}\033[0m")

    # --------------------------------------------------------------------------
    # Toolchain & Browser Version Report
    # --------------------------------------------------------------------------
    print("\nResource Versions Report")
    print("-" * 100)

    versions = get_all_versions(os_name)
    for tool, ver in versions.items():
        if "Not installed" not in ver:
            print(f"{tool:<25}: {ver}")
