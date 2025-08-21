"""
Author: Shubham Darda
Description: A standard script file contains the functionalities needed for automated testing.
"""

# --- Standard library imports ---
import os
import platform
import re
import shutil
import subprocess
import sys
import time
import unittest
import requests

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
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# It holds the base URL of the website and the environment information.
@dataclass(frozen=True)
class EnvironmentConfig:
    os_platform: str
    distribution: Optional[str]
    is_windows: bool
    is_ubuntu: bool
    is_github_actions: bool
    base_url: str
    datapath: Path


# It tracks match/unmatch counts for automated tests.
@dataclass
class TestStats:
    matched: int = 0
    unmatched: int = 0
    unmatched_entries = []


def get_environment_config() -> EnvironmentConfig:
    """
    Detects the host operating system, enforces Windows 11 builds,
    and sets up flags for Windows, Ubuntu, and GitHub Actions,
    along with the appropriate base URL.
    Returns an EnvironmentConfig.
    """
    os_platform = sys.platform
    is_windows = False
    is_ubuntu = False
    is_github_actions = False
    distribution = None
    base_url = "http://localhost:4000/"
    datapath = os.path.join(os.path.dirname(__file__), "..", "_data")

    if os_platform == "linux":
        distro_id = platform.freedesktop_os_release().get("ID", "").lower()
        distribution = distro_id

        if distro_id == "ubuntu":
            is_ubuntu = True
        else:
            print(
                f"Unsupported Linux distribution: {distro_id}. Only Ubuntu is supported."
            )
            sys.exit(1)

    elif os_platform == "win32":
        is_windows = True
        distribution = platform.system().lower()
        _, ver, _, _ = platform.win32_ver()

        try:
            build_number = int(ver.split(".")[2])
        except (IndexError, ValueError):
            print(f"Failed to parse Windows build from version string: {ver}")
            sys.exit(1)

        if build_number < 22000:
            print(
                f"Unsupported Windows build {build_number}. Only Windows 11 (22000+) is supported."
            )
            sys.exit(1)

    else:
        print(
            f"Unsupported OS: {os_platform}. Only Ubuntu Linux and Windows are supported."
        )
        sys.exit(1)

    # Common override for GitHub Actions on any OS
    if os.getenv("GITHUB_ACTIONS", "").lower() == "true":
        is_github_actions = True
        base_url = "https://godarda.github.io/"

    return EnvironmentConfig(
        os_platform=os_platform,
        distribution=distribution,
        is_windows=is_windows,
        is_ubuntu=is_ubuntu,
        is_github_actions=is_github_actions,
        base_url=base_url,
        datapath=datapath,
    )


def open_browser(browser_name: str, cfg: EnvironmentConfig) -> WebDriver:
    """
    Launches a Selenium WebDriver for the specified browser.

    Args:
        browser_name: The browser to launch ('chrome', 'firefox', 'msedge').
        cfg: EnvironmentConfig for toggling headless and other options.

    Returns:
        An instance of Selenium WebDriver.

    Raises:
        ValueError: If browser_name is not recognized.
        WebDriverException: If browser fails to launch.
    """
    browser = browser_name.strip().lower()
    driver = None

    try:
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if cfg.is_github_actions:
                options.add_argument("--headless")
                print("Running Chrome in headless mode for GitHub Actions.")
            else:
                options.add_experimental_option(
                    "excludeSwitches", ["enable-automation", "enable-logging"]
                )
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(options=options, service=service)

        elif browser == "msedge":
            options = webdriver.EdgeOptions()
            options.add_experimental_option(
                "excludeSwitches", ["enable-automation", "enable-logging"]
            )
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(options=options, service=service)

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if cfg.is_github_actions:
                options.headless = True
                print("Running Firefox in headless mode for GitHub Actions.")
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(options=options, service=service)

        else:
            message = f"Unsupported browser: {browser_name}. Choose 'chrome', 'firefox', or 'msedge'."
            print(message)
            raise ValueError(message)
        return driver

    except WebDriverException as e:
        print(f"Failed to launch browser '{browser_name}': {e}")
        raise

    except Exception as e:
        print(f"Unexpected error during browser launch: {e}")
        raise


def verify_title(driver: WebDriver, path: str, expected_title: str) -> Tuple[int, int]:
    """
    Navigate to the given path, compare the actual page title to the expected title,
    update the global matched/unmatched counters, and return the updated totals.

    Args:
        driver: Active Selenium WebDriver instance.
        path: URL path segment to append to the base URL.
        expected_title: The title string expected on the loaded page.

    Returns:
        A tuple (matched_count, unmatched_count) reflecting the current totals.
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
            stats.unmatched_entries.append({path, expected_title})

    except Exception as e:
        print(
            f"WebDriverException during title verification for '{url}': {str(e).splitlines()[0]}"
        )
        sys.exit(1)

    return stats.matched, stats.unmatched


def verify_scrolling(driver, timeout: int = 10) -> bool:
    """
    Scrolls to bottom, clicks the back-to-top button, and confirms
    the page is back at the top within `timeout` seconds.

    Returns True on success, False on any failure.
    """

    try:
        before_scroll = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        after_scroll = driver.execute_script("return document.body.scrollHeight")
        if after_scroll > before_scroll:
            driver.find_element(By.ID, "backtotop").click()
            time.sleep(1)
        back_to_top = after_scroll = driver.execute_script(
            "return document.body.scrollHeight"
        )
        if back_to_top != before_scroll:
            print("Back to top: Unsuccessful")
            return False
        return True

    except (TimeoutException, JavascriptException, NoSuchElementException) as exc:
        print("verify_scrolling failed: %s", exc)
        return False


def extract_paths_from_yaml(
    data_dir: Path,
    filename: str,
    element_name: str,
    driver: Optional[WebDriver] = None,
    config: Optional[EnvironmentConfig] = None,
) -> List[str]:
    """
    Reads data_dir/filename, looks under the `element_name` key,
    extracts all child `url` values, optionally verifies titles & scroll.
    """
    config = config or get_environment_config()
    data_dir = Path(data_dir)
    file_path = data_dir / filename
    if not file_path.exists():
        print("File not found: %s", file_path)
        return []

    with file_path.open() as f:
        doc = yaml.safe_load(f) or {}

    paths: List[str] = []
    for entry in doc.get(element_name, []):
        # subtree if available, else parent, else title
        parent_title = entry.get("subtree") or entry.get("parent") or entry.get("title")
        parent_url = entry.get("url")
        if driver and parent_url:
            verify_title(driver, parent_url, parent_title)
            if not config.is_github_actions:
                verify_scrolling(driver)

        for child in entry.get("children", []):
            url = child.get("url")
            if not url:
                continue
            paths.append(url)
            if driver:
                verify_title(driver, url, child.get("title"))

    return paths


def load_expected_data(folder_path):
    """
    Parses all YAML files in the given folder to extract expected titles.
    Files are read concurrently. Deduplicates entries based on (url, title)
    pairs from both 'sidenav' and 'grandparent' sections.
    """

    folder = Path(folder_path)
    expected = []
    if not folder.exists() or not folder.is_dir():
        return expected

    files = [folder / f for f in os.listdir(folder) if f.endswith(".yml") or f.endswith(".yaml")]
    if not files:
        return expected

    def parse_file(path: Path):
        try:
            with path.open("r", encoding="utf-8") as fh:
                data = yaml.safe_load(fh) or {}
        except Exception as e:
            print(f"Warning: failed to read {path}: {e}")
            return []

        entries = []
        # process both sections; parse child and parent entries
        for section_name in ("sidenav", "grandparent"):
            for section in data.get(section_name, []):
                if "url" in section and "parent" in section:
                    entries.append((section["url"], section["parent"]))
                for child in section.get("children", []):
                    if "url" in child and "title" in child:
                        entries.append((child["url"], child["title"]))
        return entries

    # Choose a reasonable worker count
    max_workers = min(32, max(2, (os.cpu_count() or 2) * 2))
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        for res in ex.map(parse_file, files):
            if res:
                results.extend(res)

    seen = set()
    out = []
    for url, title in results:
        key = (url, title)
        if key not in seen:
            out.append({"url": url, "title": title})
            seen.add(key)

    return out


# Global configuration and statistics
config = get_environment_config()
stats = TestStats()


def start_tests(browser_name: str, data_path: str):
    """
    Launches a suite of page-title and scrolling checks using titles/URLs
    loaded from the repository's _data folder via load_expected_titles.

    Args:
        browser_name: 'chrome' | 'firefox' | 'msedge'
        data_path: (ignored) kept for compatibility; config.datapath is used.

    Returns:
        A tuple (matched_count, unmatched_count).
    """
    # driver launch
    driver = open_browser(browser_name, config)

    # reset counters
    stats.matched = 0
    stats.unmatched = 0

    try:
        # load expected url/title pairs from _data
        expected = load_expected_data(config.datapath)
        if not expected:
            print(f"No expected titles found in: {config.datapath}")

        for entry in expected:
            url = entry.get("url")
            title = entry.get("title")
            if not url or not title:
                continue

            verify_title(driver, url, title)

        # Run scrolling only if not in GitHub Actions and URL has 0 or 1 "/"
        slash_count = url.count("/")
        if not config.is_github_actions and slash_count in (0, 1):
            verify_scrolling(driver)


    finally:
        # ensure we always tear down the browser
        if driver:
            try:
                driver.delete_all_cookies()
            except Exception:
                pass
            try:
                driver.quit()
            except Exception:
                pass

    return stats.matched, stats.unmatched
