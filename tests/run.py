"""
Author: Shubham Darda
Description: Entry point for automated browser-based testing and code compilation.
"""

from utilities import *
from compile import *

def get_version(cmd: str) -> str:
    """
    Executes a shell command to retrieve tool version.
    Returns the version string or a fallback message if the command fails.
    """
    try:
        return subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
    except Exception:
        return "Not installed or failed"

def print_report(matched: int, unmatched: int, passed: int, failed: int, browser: str):
    """
    Prints a consolidated report including:
    - Website test results
    - Code compilation summary
    - Toolchain and browser versions
    """
    visited = matched + unmatched
    compiled = passed + failed

    if visited > 0:
        print("---------------------------------\nWebsite Report\n---------------------------------")
        print("Total Webpages Visited:", visited)
        print("Total Titles Matched:", matched)
        print("Total Titles Unmatched:", unmatched)

    if compiled > 0:
        print("---------------------------------\nCode Compilation Report\n---------------------------------")
        print("Total Files Compiled:", compiled)
        print("Total Passed:", passed)
        print("Total Failed:", failed)

        print("---------------------------------\nResources Version\n---------------------------------")
        versions = {
            "gcc/g++": get_version("g++ -dumpfullversion"),
            "Java": get_version("javac --version"),
            "Python": get_version("python3 --version"),
            "Rust": get_version("rustc --version"),
            "NASM": get_version("nasm --version")
        }

        # Browser-specific version command
        if browser == "firefox":
            versions["Firefox"] = get_version("firefox --version")
        elif browser == "msedge":
            versions["Edge"] = get_version("msedge --version")
        elif browser == "chrome":
            versions["Chrome"] = get_version("google-chrome --version")

        for label, output in versions.items():
            print(f"{label}: {output}")

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

        elif config.is_windows:
            data_path = "D:/godarda.github.io/_data/"
            browser = "chrome"  # Alternative: "msedge"

            matched, unmatched = start_tests(browser, data_path)
            passed = failed = 0

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
        matched = unmatched = passed = failed = 0
        browser = "unknown"

    # Generate consolidated report
    print_report(matched, unmatched, passed, failed, browser)

    # Print total execution time
    end = time.time()
    m, s = divmod(round(end - start), 60)
    h, m = divmod(m, 60)

    if h or m or s:
        print("---------------------------------")
        print("Total Execution Time:", f"{h:02d}:{m:02d}:{s:02d}")

    # Cleanup bytecode cache
    clean_pycache()

if __name__ == "__main__":
    main()