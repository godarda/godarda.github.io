import subprocess
import platform
import shutil
from utilities import stats


def get_version(cmd: str) -> str:
    """
    Execute a shell command to retrieve a tool’s version.
    Returns the trimmed stdout on success or a standardized error message on failure.
    """
    try:
        raw_output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        return raw_output.decode("utf-8").strip().splitlines()[0]
    except Exception:
        return "Not installed or retrieval failed"


def get_browser_version(browser: str, os_name: str) -> str:
    """
    Determine the installed browser version using platform-aware probing.
    Supports Firefox, Chrome, Edge, and Safari (macOS only).
    """
    browser_cmds = {
        "firefox": ["firefox --version"],
        "chrome": [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --version",
        "chrome --version",
        r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --version'
        ],
        "msedge": [
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge --version",
            "msedge --version",
            "microsoft-edge --version",
            "microsoft-edge-stable --version",
            r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --version'
        ],
        "safari": [
            "defaults read /Applications/Safari.app/Contents/Info CFBundleShortVersionString"
        ] if os_name == "Darwin" else []
    }

    for cmd in browser_cmds.get(browser, []):
        if shutil.which(cmd.split()[0].strip('"')) or os_name == "Darwin":
            version = get_version(cmd)
            if "Not installed" not in version:
                return version

    return "Not installed or retrieval failed"


def get_all_versions(browser: str, os_name: str) -> dict:
    """
    Retrieve versions of common development tools and browsers across platforms.
    """
    tools = {
        "gcc/g++": "g++ --version",
        "Rust": "rustc --version",
        "NASM": "nasm --version",
        "Java": "javac --version",
        "Python": "python --version" if os_name == "Windows" else "python3 --version",
    }

    versions = {tool: get_version(cmd) for tool, cmd in tools.items()}

    if browser:
        versions[browser.capitalize()] = get_browser_version(browser, os_name)

    return versions


def print_report(
    matched: int,
    unmatched: int,
    passed: int,
    failed: int,
    browser: str
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

    versions = get_all_versions(browser, os_name)

    for tool, ver in versions.items():
        if "Not installed" not in ver:
            print(f"{tool:<25}: {ver}")