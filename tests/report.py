import subprocess
from utilities import stats


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
        """
        Prints the list of unmatched entries from the test statistics.
        """
        # Print unmatched entries only if any exist
        print("\nTitle Verification Report")
        print("-" * 100)
        if stats.unmatched > 0:
            print(f"{'Status':<10} {'URL':<32} {'Expected Title'}")
            print("-" * 100)
            for rel_url, expected_title in stats.unmatched_entries:
                print(
                    f"\033[91m{'Unmatched':<10}\033[0m {rel_url:<32} {expected_title}"
                )
            print("-" * 100)
        else:
            print("\nAll titles matched. No discrepancies found.")
        print(f"Total URLs Checked: {stats.matched + stats.unmatched}")
        print(f"Total Titles Matched: {stats.matched}")
        print(f"Total Titles Unmatched: {stats.unmatched}")

    if compiled > 0:
        print("\nCode Compilation Report")
        print("-" * 100)
        if stats.uncompiled > 0:
            print(f"{'Status':<10} {'URL':<10}")
            print("-" * 100)
            for rel_url in stats.uncompiled_entries:
                print(
                    f"\033[91m{'Uncompiled':<10}\033[0m {rel_url:<10}"
                )
            print("-" * 100)
        else:
            print("\nAll titles matched. No discrepancies found.")
        print("Total Files Compiled:", compiled)
        print("Total Passed:", passed)
        print("Total Failed:", failed)

        print("\nResources Version Report")
        print("-" * 100)
        versions = {
            "gcc/g++": get_version("g++ -dumpfullversion"),
            "Java": get_version("javac --version"),
            "Python": get_version("python3 --version"),
            "Rust": get_version("rustc --version"),
            "NASM": get_version("nasm --version"),
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
