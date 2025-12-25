"""
Author: Shubham Darda
Purpose:
    Entry point for the automated test harness used to validate the generated
    GoDarda static site and optionally compile code snippets.

Description:
    This module orchestrates:
      - Environment validation (minimum Python version).
      - Platform-specific test flows (macOS, Ubuntu, Windows).
      - Browser-driven title verification and optional snippet compilation.
      - Summary reporting and lightweight cleanup.

Guidelines:
    - Keep orchestration logic here; delegate browser and file helpers to utilities.py.
    - Fail fast on obvious preconditions (missing pages folder, unsupported OS).
    - Maintain concise, CI-friendly logging to ease debugging in GitHub Actions.
"""

import os
import sys
import time
import platform
from compile import compile_snippets
from unittesting import TitleVerificationTest
from report import print_report
from utilities import config, stats, start_tests, clean_pycache


def main() -> None:
    """
    Main procedure for running the test harness and compilation steps.

    Responsibilities:
      - Validate Python runtime compatibility (project minimum: 3.7).
      - Determine the repository 'pages' -> 'codes' paths.
      - Branch into OS-specific behaviors:
          * macOS: Safari (local) or run bare title verification in GH Actions.
          * Ubuntu: Chrome (local/CI) with full verification and snippet compilation.
          * Windows: Chrome for local runs; limited behavior in CI.
      - Emit a concise report and execution time.
      - Attempt non-destructive cleanup (remove __pycache__).
    """
    start = time.time()

    # Python version guard (maintain original project's minimum)
    if sys.version_info < (3, 7):
        print("Python 3.7 or later is needed for execution.")
        return

    try:
        # High-level run info to help CI logs correlate results with environment
        print("Starting automated tests on:", platform.platform())
        cwd = os.getcwd()
        source = os.path.join(cwd, "pages")
        destination = os.path.join(cwd, "codes")

        # Sanity check: ensure site pages exist before attempting browser work
        if not os.path.exists(source):
            print(f"Source path not found: {source}")
            return

        # macOS-specific flow
        if config.is_macos:
            print("Running tests on macOS. Please wait...")
            if config.is_github_actions:
                # In CI we only run the minimal TitleVerificationTest to avoid GUI dependencies
                TitleVerificationTest().runTest()
                browser = ""
            else:
                # Local macOS: prefer Safari for verification to match user environment
                browser = "safari"
                start_tests(browser)
            # Compile snippets for macOS flows when snippet sources are present
            compile_snippets(source, destination)

            print_report(
                stats.matched,
                stats.unmatched,
                stats.compiled,
                stats.uncompiled,
                browser,
            )

        # Ubuntu-specific flow
        elif config.is_ubuntu:
            browser = "chrome"
            print("Running tests on Ubuntu. Please wait...")
            start_tests(browser)
            compile_snippets(source, destination)

            print_report(
                stats.matched,
                stats.unmatched,
                stats.compiled,
                stats.uncompiled,
                browser,
            )

        # Windows-specific flow
        elif config.is_windows:
            print("Running tests on Windows. Please wait...")
            if config.is_github_actions:
                # CI on Windows may run a reduced verification set
                TitleVerificationTest().runTest()
                browser = ""
            else:
                browser = "chrome"
                start_tests(browser)
            # Windows path historically did not attempt compilation in this harness
            print_report(stats.matched, stats.unmatched, 0, 0, browser)

        else:
            # Guard for unsupported OS; utilities.get_environment_config should already catch this
            print("Script works on macOS, Ubuntu, and Windows only.")
            return

    except Exception as e:
        # Provide helpful diagnostics for common runtime issues.
        print("The script execution aborted due to the following possible reason(s):")
        print("1. The local server isn't up and running.")
        print("2. The required driver isn't found at the given location.")
        print("3. Unsupported OS, browser or driver versions.")
        print("4. Manual interruption during execution.")
        print("5. Local code changes or misconfiguration.")
        print("Exception details:", e)

    # Compute and print total execution time in HH:MM:SS format
    end = time.time()
    total_seconds = round(end - start)
    m, s = divmod(total_seconds, 60)
    h, m = divmod(m, 60)

    print("-" * 100)
    if h >= 1:
        # Long runs highlighted in CI-friendly red
        time_str = f"\033[91m{h:02d}:{m:02d}:{s:02d}\033[0m"
    else:
        # Short runs highlighted in green
        time_str = f"\033[92m{h:02d}:{m:02d}:{s:02d}\033[0m"

    print(f"{'Total Execution Time':<25}: {time_str}")

    # Best-effort cleanup of bytecode caches to avoid stale artifacts across runs
    clean_pycache()


if __name__ == "__main__":
    main()
