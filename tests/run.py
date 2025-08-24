"""
Author: Shubham Darda
Description: Entry point for automated browser-based testing and code compilation.
"""

import os
import sys
import time
import platform
import shutil
from compile import compile_codes
from unittesting import TitleVerificationTest
from report import print_report
from utilities import config, stats, start_tests, clean_pycache


def main() -> None:
    """
    Main procedure:
      - Validate Python version
      - Branch behavior for Ubuntu vs Windows
      - Run compilation or tests
      - Print summary report and execution time
    """
    start = time.time()

    # Python version guard (maintain original project's minimum)
    if sys.version_info < (3, 7):
        print("Python 3.7 or later is needed for execution.")
        return

    try:
        print("Starting automated tests on:", platform.platform())
        cwd = os.getcwd()
        source = os.path.join(cwd, "pages")
        destination = os.path.join(cwd, "gdfied")
        if not os.path.exists(source):
            print(f"Source path not found: {source}")
            return
        
        # macOS-specific flow
        if config.is_macos:
            # browser = "safari"
            print("Running tests on macOS. Please wait...")
            TitleVerificationTest().runTest()
            browser = None
            # start_tests(browser)
            compile_codes(source, destination)

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
            compile_codes(source, destination)

            print_report(
                stats.matched,
                stats.unmatched,
                stats.compiled,
                stats.uncompiled,
                browser,
            )

        # Windows-specific flow
        elif config.is_windows:
            # browser = "chrome"
            # print("Running tests on Windows. Please wait...")
            # start_tests(browser)

            TitleVerificationTest().runTest()
            browser = None
            print_report(stats.matched, stats.unmatched, 0, 0, browser)

        else:
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
        time_str = f"\033[91m{h:02d}:{m:02d}:{s:02d}\033[0m"  # Red for long runs
    else:
        time_str = f"\033[92m{h:02d}:{m:02d}:{s:02d}\033[0m"  # Green for short runs

    print(f"{'Total Execution Time':<25}: {time_str}")

    # Attempt to remove any leftover bytecode cache
    clean_pycache()


if __name__ == "__main__":
    main()
