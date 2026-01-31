"""
Test Harness Entry Point (tests/run.py)

Purpose:
This script orchestrates the testing workflow for the GoDarda site.
It validates the runtime environment, executes verification tests,
performs code compilation, and generates a summary report.

Key Features:
1. Orchestration: Coordinates title verification and code compilation steps.
2. Validation: Checks Python version and directory structure before running.
3. Reporting: Calculates execution time and displays final results.
"""

import os
import sys
import time
import shutil
from compile import compile_snippets
from unittesting import TitleVerificationTest
from report import print_report
from utilities import CONFIG, STATS


def main() -> None:
    """
    Executes the test suite, including environment checks, verification, and reporting.
    """
    # Ensure the Python runtime meets the minimum version requirement.
    if sys.version_info < (3, 7):
        print("Python 3.7 or later is needed for execution.")
        return

    try:
        start = time.time()
        cwd = os.getcwd()
        source = os.path.join(cwd, "pages")
        destination = os.path.join(cwd, ".codes")

        # Verify that the source directory exists.
        if not os.path.exists(source):
            print(f"Source path not found: {source}")
            return

        print(f"Starting test suite on {CONFIG.OS_NAME}.")
        print("Please wait, execution in progress...")

        # Execute title verification.
        TitleVerificationTest("test_site_titles").test_site_titles()

        # Execute snippet compilation if supported.
        if CONFIG.OS_NAME != "Windows":
            compile_snippets(source, destination)
            if os.path.exists(destination):
                shutil.rmtree(destination)

        print_report(
            STATS.matched,
            STATS.unmatched,
            STATS.compiled,
            STATS.uncompiled,
        )

        # Calculate and display execution time.
        end = time.time()
        total_seconds = round(end - start)
        m, s = divmod(total_seconds, 60)
        h, m = divmod(m, 60)

        print("-" * 100)
        if h >= 1:
            time_str = f"\033[91m{h:02d}:{m:02d}:{s:02d}\033[0m"
        else:
            time_str = f"\033[92m{h:02d}:{m:02d}:{s:02d}\033[0m"

        print(f"{'Total Execution Time':<25}: {time_str}")

    except Exception as e:
        print("\n\033[91mExecution failed.\033[0m")
        print(f"Error details: {e}")
        print("\nPossible causes:")
        print(f"1. Local server not running at {CONFIG.BASE_URL}")
        print("2. Network connectivity issues.")
        print("3. Environment or configuration errors.")


if __name__ == "__main__":
    main()
