#!/usr/bin/env python3
"""
Title Verification Tests (tests/unittesting.py)

Purpose:
This module performs unit tests to verify the integrity of the deployed
static site. It validates that webpage titles match expected values defined
in the data files.

Key Features:
1. Concurrency: Utilizes thread pools for efficient parallel HTTP requests.
2. Validation: Compares fetched HTML <title> tags against expected metadata.
3. Resilience: Implements connection pooling and retries for network stability.
"""

import os
import requests
import unittest
import concurrent.futures
import urllib.parse
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
from config import CONFIG
from utilities import load_expected_data
from stats import STATS


def fetch_and_verify_title(
    session: requests.Session, base_url: str, expected_entry: dict, timeout: int = 5
) -> None:
    """
    Fetches a page title, compares it with the expected title, and updates
    the global STATS object. This function is designed to be run in a worker thread.
    """
    if STATS.aborted:
        return

    relative_url = expected_entry["url"]
    expected_title = expected_entry["title"]
    full_url = urllib.parse.urljoin(base_url, relative_url.lstrip("/"))

    try:
        resp = session.get(full_url, timeout=timeout)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        actual_title = soup.title.string.strip() if soup.title and soup.title.string else ""

        is_match = actual_title == expected_title
        STATS.add_title_result(is_match, (relative_url, expected_title))

    except requests.RequestException as e:
        # Treat network or HTTP errors as a missing title.
        STATS.add_title_result(False, (relative_url, f"Error: {e}"), is_error=True)

    # Abort early if a significant number of mismatches occur.
    if STATS.unmatched > 10:
        with STATS._lock:
            if not STATS.aborted:
                STATS.aborted = True
                print("\n\033[91mToo many unmatched titles.\033[0m")
                print("This likely indicates a server down, broken selectors, or bad input.")
                os._exit(1)


class TitleVerificationTest(unittest.TestCase):
    """
    Test case for verifying that webpage titles match expected values.
    """

    def test_site_titles(self):
        # Load expected URL/title pairs from the data directory.
        expected_data = load_expected_data(CONFIG.DATAPATH)
        STATS.total_urls = len(expected_data)
        if not expected_data:
            self.skipTest("No expected data loaded; skipping title verification test.")

        # Initialize a session with connection pooling.
        session = requests.Session()
        session.headers.update({"User-Agent": "GoDarda-TitleChecker/1.0"})
        adapter = HTTPAdapter(pool_maxsize=20, max_retries=1)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        # Calculate an appropriate thread pool size.
        max_workers = min(20, CONFIG.CPU_COUNT * 5)

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Create a list of arguments for each task.
            tasks = [(session, CONFIG.BASE_URL, entry, 5) for entry in expected_data]

            # Use a lambda to pass arguments to the worker function via map.
            # list() consumes the iterator, ensuring all tasks complete before proceeding.
            try:
                list(executor.map(lambda p: fetch_and_verify_title(*p), tasks))
            except Exception as exc:
                # Exceptions from workers are raised here by executor.map.
                print(f"A worker thread generated an exception: {exc}")

        session.close()
