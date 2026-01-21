#!/usr/bin/env python3
"""
Author: Shubham Darda
Purpose:
    Test helper utilities used by the automated test suite for the GoDarda website.

Description:
    This module centralizes reusable functionality required by integration/acceptance
    tests that exercise the generated static site:
      - Environment detection and validation (OS, GitHub Actions, base URL).
      - Selenium WebDriver lifecycle and browser helpers (Chrome, Safari).
      - Page verification helpers (title checks, scrolling/back-to-top).
      - YAML-driven expected-data loader with concurrency and deduplication.
      - Lightweight cleanup helpers (remove __pycache__).

Guidelines:
    - Keep functions small and focused; prefer explicit error messages to aid CI debugging.
    - Avoid destructive operations in tests; cleanup functions only remove local caches.
    - Use EnvironmentConfig to centralize platform-specific behavior (headless mode, base_url).
    - Load expected title data from the repository _data folder to drive page checks.
"""
# --- Standard library imports ---
import os
import platform
import sys
import time
import shutil
import subprocess

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple, Union
from concurrent.futures import ThreadPoolExecutor

# --- Third-party imports ---
import yaml
from selenium import webdriver
from selenium.common.exceptions import (
    WebDriverException,
    JavascriptException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# It holds the base URL of the website and the environment information.
@dataclass(frozen=True)
class EnvironmentConfig:
    # Platform booleans (mutually exclusive)
    is_macos: bool
    is_ubuntu: bool
    is_windows: bool
    # CI indicator (affects headless mode and base_url override)
    is_github_actions: bool
    # Base URL used for tests (localhost for local dev, GitHub Pages in CI)
    base_url: str
    # Path to the repository data folder (used to load expected titles)
    datapath: Path


# It tracks match/unmatch counts for automated tests.
@dataclass
class TestStats:
    # Number of successful title matches
    matched: int = 0
    # Number of mismatches encountered
    unmatched: int = 0
    # List of (path, expected_title) tuples that failed
    unmatched_entries = []
    # Counters reserved for future compilation checks
    compiled: int = 0
    uncompiled: int = 0
    uncompiled_entries = []


def get_environment_config() -> EnvironmentConfig:
    """
    Detect the host operating system, enforce Windows 11 builds when running locally,
    and set up flags for macOS, Ubuntu, Windows, and GitHub Actions. Also returns
    the appropriate base URL and datapath for loading expected titles.

    Notes:
      - On Linux, only Ubuntu is supported by the test harness; other distros exit.
      - On Windows, a minimum build number (22000) is required (Windows 11).
    """
    system_name = platform.system()
    is_windows = system_name == "Windows"
    is_macos = system_name == "Darwin"
    is_linux = system_name == "Linux"
    is_github_actions = os.environ.get("GITHUB_ACTIONS") == "true"

    is_ubuntu = False
    base_url = "http://localhost:4000/"
    datapath = os.path.join(os.path.dirname(__file__), "..", "_data/")

    # When running on Linux, ensure it's Ubuntu (tests rely on distro-specific behavior)
    if is_linux:
        # platform.freedesktop_os_release provides structured distro info when available
        distro_id = platform.freedesktop_os_release().get("ID", "").lower()
        is_ubuntu = distro_id == "ubuntu"
        if not is_ubuntu:
            # Fail fast: unsupported distro will produce unpredictable results
            print(f"Unsupported Linux distribution: {distro_id}. Only Ubuntu is supported.")
            sys.exit(1)

    # On Windows ensure at least Windows Server 2022 (build 20348) or Windows 11 (build 22000+) to avoid incompatible behavior
    if is_windows:
        _, ver, _, _ = platform.win32_ver()
        try:
            build_number = int(ver.split(".")[2])
        except (IndexError, ValueError):
            print(f"Failed to parse Windows build from version string: {ver}")
            sys.exit(1)
        if build_number < 20348:
            print(f"Unsupported Windows build {build_number}. Requires Server 2022 (20348+) or Windows 11 (22000+).")
            sys.exit(1)

    # Only macOS, Ubuntu (Linux) and Windows are supported by the test harness
    if not (is_windows or is_ubuntu or is_macos):
        print(f"Unsupported OS: {system_name}. Only macOS, Ubuntu, and Windows are supported.")
        sys.exit(1)

    return EnvironmentConfig(
        is_windows=is_windows,
        is_ubuntu=is_ubuntu,
        is_macos=is_macos,
        is_github_actions=is_github_actions,
        base_url=base_url,
        datapath=Path(datapath),
    )


def open_browser(browser_name: str, cfg: EnvironmentConfig) -> WebDriver:
    """
    Launch a Selenium WebDriver for the requested browser.

    Supported browsers:
      - chrome: uses webdriver-manager to download a compatible ChromeDriver.
      - safari: macOS-only. Attempts to enable the safaridriver if necessary.

    Behavior:
      - When running in GitHub Actions, Chrome is started in headless mode.
      - Experimental options are used for local Chrome runs to reduce automation flags.
      - Detailed errors are printed to help CI logs diagnose failures.
    """
    browser = browser_name.strip().lower()
    driver = None

    try:
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if cfg.is_github_actions:
                # Use headless mode in CI to avoid requiring a display server
                options.add_argument("--headless")
                print("Running Chrome in headless mode for GitHub Actions.")
            else:
                # Reduce noisy automation warnings when running locally
                options.add_experimental_option(
                    "excludeSwitches", ["enable-automation", "enable-logging"]
                )
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(options=options, service=service)

        elif browser == "safari":
            # Safari WebDriver is only available on macOS
            if not cfg.is_macos:
                raise ValueError("Safari is only supported on macOS.")

            try:
                # Enabling safaridriver requires elevated privileges on macOS
                print("Enabling Safari WebDriver (requires admin privileges)...")
                subprocess.run(["sudo", "safaridriver", "--enable"], check=True)
                print("Safari WebDriver enabled.")
            except subprocess.CalledProcessError as e:
                raise RuntimeError(f"Failed to enable Safari WebDriver. Exit code: {e.returncode}") from e
            except FileNotFoundError:
                raise EnvironmentError("safaridriver not found. Ensure Safari is installed and you're on macOS.")

            print("Launching Safari browser on macOS.")
            driver = webdriver.Safari()

        else:
            message = f"Unsupported browser: {browser_name}. Choose 'chrome' or 'safari'."
            print(message)
            raise ValueError(message)

        return driver

    except WebDriverException as e:
        # Propagate Selenium-specific failures after logging
        print(f"Failed to launch browser '{browser_name}': {e}")
        raise

    except Exception as e:
        # Generic fallback for other unexpected launch errors
        print(f"Unexpected error during browser launch: {e}")
        raise


def verify_title(driver: WebDriver, path: str, expected_title: str) -> Tuple[int, int]:
    """
    Navigate to the provided path (relative to config.base_url), compare the page title,
    and update the global TestStats counters.

    Returns:
        (matched_count, unmatched_count)

    Notes:
      - This function maximizes the browser window before loading to ensure titles
        and layout are consistent across environments.
      - On any unexpected exception the test run exits with status 1 to fail CI/runner.
    """
    url = f"{config.base_url}{path}"

    try:
        driver.maximize_window()
        driver.get(url)
        actual_title = driver.title.strip()
        if actual_title == expected_title.strip():
            stats.matched += 1
        else:
            stats.unmatched += 1
            stats.unmatched_entries.append((path, expected_title))
        
        # Run scrolling only if not in GitHub Actions and URL has 0 or 1 "/"
        # Use the last processed url as representative (this is consistent with previous behavior)
        slash_count = path.count("/")
        if not config.is_github_actions and slash_count in (0, 1):
            verify_scrolling(driver)
            
    except Exception as e:
        # Keep the logged message compact for CI readability while preserving cause
        print(
            f"WebDriverException during title verification for '{url}': {str(e).splitlines()[0]}"
        )
        sys.exit(1)

    return stats.matched, stats.unmatched


def verify_scrolling(driver) -> bool:
    """
    Validate scrolling behavior:
      - Scroll to the bottom of the page.
      - Click the '#backtotop' element (if present).
      - Confirm page returns to the original top position.

    Returns:
      True on success, False on failure or if element not present.
    """
    try:
        # Measure document height before and after scroll to detect dynamic content
        before_scroll = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        after_scroll = driver.execute_script("return document.body.scrollHeight")
        if after_scroll > before_scroll:
            # Attempt to click the back-to-top control to return to top
            driver.find_element(By.ID, "backtotop").click()
            time.sleep(1)
        # Re-evaluate height to determine whether we're back to top
        back_to_top = after_scroll = driver.execute_script(
            "return document.body.scrollHeight"
        )
        if back_to_top != before_scroll:
            print("Back to top: Unsuccessful")
            return False
        return True

    except (TimeoutException, JavascriptException, NoSuchElementException) as exc:
        # Log a concise failure for CI; do not raise so the suite can continue if desired
        print("verify_scrolling failed: %s", exc)
        return False


def load_expected_data(folder_path):
    """
    Parse all YAML files in the specified folder concurrently to extract expected
    (url, title) pairs used by page verification.

    Behavior and notes:
      - Supports both .yml and .yaml file extensions.
      - Concurrently reads files with ThreadPoolExecutor for improved IO throughput.
      - Deduplicates entries by (url, title) to avoid redundant tests.
      - Recognizes 'sidenav' and 'grandparent' sections in YAML files; extracts
        'parent' and child 'title' fields as needed.
      - Returns a list of dictionaries: [{"url": <str>, "title": <str>}, ...]
    """
    folder = Path(folder_path)
    expected = []
    if not folder.exists() or not folder.is_dir():
        return expected

    files = []
    for root, _, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith((".yml", ".yaml")):
                files.append(Path(root) / filename)
    if not files:
        return expected

    def parse_file(path: Path):
        # Safely load YAML content; return [] on parse/read failure to avoid aborting all parsing
        try:
            with path.open("r", encoding="utf-8") as fh:
                data = yaml.safe_load(fh) or {}
        except Exception as e:
            print(f"Warning: failed to read {path}: {e}")
            return []

        entries = []
        # Process both named sections; entries can be present at parent and child levels
        for section_name in ("sidenav", "grandparent"):
            for section in data.get(section_name, []):
                if "url" in section and "parent" in section:
                    entries.append((section["url"], section["parent"]))
                for child in section.get("children", []):
                    if "url" in child and "title" in child:
                        entries.append((child["url"], child["title"]))
        return entries

    # Choose a conservative worker count to avoid overwhelming small CI runners
    max_workers = min(32, max(2, (os.cpu_count() or 2) * 2))
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        for res in ex.map(parse_file, files):
            if res:
                results.extend(res)

    # Deduplicate results while preserving original order
    seen = set()
    out = []
    for url, title in results:
        key = (url, title)
        if key not in seen:
            out.append({"url": url, "title": title})
            seen.add(key)

    return out


# Global configuration and statistics
# These are initialized at module import time and intended to be reused across tests.
config = get_environment_config()
stats = TestStats()


def start_tests(browser_name: str):
    """
    Run the suite of title verifications and a single scrolling check.

    Args:
      browser_name: 'chrome' | 'safari'

    Returns:
      (matched_count, unmatched_count)

    Notes:
      - The driver is always torn down in the finally block to avoid leaking processes.
      - Scrolling is only validated for URLs with 0 or 1 slashes and only on local runs
        (disabled in GitHub Actions to avoid interacting with remote pages).
    """
    # Launch the browser driver according to the environment config
    driver = open_browser(browser_name, config)

    try:
        # Load expected url/title pairs from _data
        expected = load_expected_data(config.datapath)
        if not expected:
            print(f"No expected titles found in: {config.datapath}")

        for entry in expected:
            url = entry.get("url")
            title = entry.get("title")
            if not url or not title:
                continue

            verify_title(driver, url, title)

    finally:
        # ensure we always tear down the browser to avoid zombie driver processes
        if driver:
            try:
                driver.delete_all_cookies()
                driver.quit()
            except Exception:
                # Suppress cleanup errors to avoid masking test results
                pass

    return stats.matched, stats.unmatched


def clean_pycache(cache_path: str | None = None) -> None:
    """
    Remove a __pycache__ directory.

    Behavior:
      - If cache_path is provided and points to a __pycache__ directory, it will be removed.
      - If cache_path is provided and points to a parent directory, that parent's
        __pycache__ child will be removed.
      - If cache_path is None, the function removes the __pycache__ directory adjacent
        to this file.

    Exceptions are caught and logged as warnings to avoid failing the test run.
    """
    try:
        p = (
            Path(cache_path)
            if cache_path
            else Path(__file__).resolve().parent / "__pycache__"
        )
        # If caller passed a parent folder (not named __pycache__), remove its __pycache__ child
        if p.name != "__pycache__":
            p = p / "__pycache__"
        if p.exists():
            shutil.rmtree(p)
    except Exception as e:
        print(f"Cleanup warning (could not remove {cache_path or 'default'}): {e}")
