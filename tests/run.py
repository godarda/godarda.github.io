"""
Author: Shubham Darda
Description: Entry point for automated browser-based testing and code compilation.
"""

from utilities import *
from compile import compile_codes
from unittesting import TitleVerificationTest
from report import print_report


def clean_pycache():
    """
    Removes the bytecode cache directory if it exists.
    Logs a warning if cleanup fails due to permission or path issues.
    """
    cache_path = "tests/__pycache__"
    if os.path.exists(cache_path):
        try:
            shutil.rmtree(cache_path)
        except Exception as e:
            print(f"Cleanup warning: {e}")


def main():
    start = time.time()

    # Validate Python version
    if sys.version_info < (3, 4):
        print("Python 3.4 or later is needed for execution.")
        return

    try:
        print("Starting automated tests on:", platform.platform())

        # Configure paths and browser based on OS
        if config.is_ubuntu:
            root = os.getcwd() + "/"
            data_path = root + "_data/"
            source = root + "pages/"
            destination = root + "gdfied/"
            browser = "chrome"  # Alternative: "firefox"

            matched, unmatched = start_tests(browser, data_path)
            passed, failed = compile_codes(source, destination, data_path)
            os.chdir(root)  # Reset working directory

            # Generate consolidated report
            print_report(stats.matched, stats.unmatched, passed, failed, browser)

        elif config.is_windows:
            # Instantiate and run the test
            TitleVerificationTest().runTest()
            print_report(stats.matched, stats.unmatched, 0, 0, browser)

        else:
            print("Script works on Windows and Ubuntu only.")
            return

    except Exception:
        # Fail-fast diagnostics for common runtime issues
        print("The script execution aborted due to the following possible reason(s):")
        print("1. The local server isn't up and running.")
        print("2. The required driver isn't found at the given location.")
        print("3. Due to unsupported OS, browser and driver versions.")
        print("4. Manual interruption during execution.")
        print("5. Local code changes or misconfiguration.")
        stats.matched = stats.unmatched = passed = failed = 0
        browser = "unknown"

    # Print total execution time
    end = time.time()
    m, s = divmod(round(end - start), 60)
    h, m = divmod(m, 60)

    if h or m or s:
        print("-" * 100)
        print("Total Execution Time:", f"{h:02d}:{m:02d}:{s:02d}")

    # Cleanup bytecode cache
    clean_pycache()


if __name__ == "__main__":
    main()
