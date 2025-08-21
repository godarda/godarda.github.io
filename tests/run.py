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
    if sys.version_info < (3, 4):
        print("Python 3.4 or later is needed for execution.")
        return

    try:
        print("Starting automated tests on:", platform.platform())

        # OS-specific flows
        if config.is_ubuntu:
            # Build source/destination paths from current working directory
            cwd = os.getcwd()
            source = os.path.join(cwd, "pages")  # pages/ folder containing source files
            destination = os.path.join(cwd, "gdfied")  # output folder for compiled pages
            browser = "chrome"  # or "firefox" if preferred

            # Ensure source exists before invoking compilation
            if not os.path.exists(source):
                print(f"Source path not found: {source}")
                return

            print(
                "Please wait. It may take some time to complete the tests."
            )
            # Start the automated tests
            start_tests(browser, config.datapath)

            # Run the compilation pipeline (module: compile)
            compile_codes(source, destination, config.datapath)

            # Print consolidated report using values collected in utilities.stats
            print_report(stats.matched, stats.unmatched, stats.compiled, stats.uncompiled, browser)

        elif config.is_windows:
            # Run the Windows-specific unit/test entrypoint
            TitleVerificationTest().runTest()
            browser = None  # No browser in this path
            # On Windows the passed/failed counters are not used here, so pass zeros
            print_report(stats.matched, stats.unmatched, 0, 0, browser)

        else:
            print("Script works on Windows and Ubuntu only.")
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

    if h or m or s:
        print("-" * 100)
        print("Total Execution Time:", f"{h:02d}:{m:02d}:{s:02d}")

    # Attempt to remove any leftover bytecode cache
    clean_pycache("tests/__pycache__")


if __name__ == "__main__":
    main()
