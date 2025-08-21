# Module: Title verification unit test
# Purpose: Fetch pages from the site and verify their <title> matches expected values.
# This test is intended to be run as part of the test suite; it uses a thread pool and a
# requests.Session for efficiency.

import os
import yaml
import requests
import unittest
import concurrent.futures
import urllib.parse
from pathlib import Path
from bs4 import BeautifulSoup
from utilities import config, stats, load_expected_data


# Helper that performs the HTTP GET for a single relative URL using a shared session.
def _fetch_title_session(
    session: requests.Session, base_url: str, relative_url: str, timeout: int = 5
):
    """
    Helper to fetch title using a provided session. Returns (relative_url, title_or_None).

    - session: a prepared requests.Session (keeps connections pooled)
    - base_url: site base to join with the relative path
    - relative_url: page path to fetch (may start with '/')
    - timeout: per-request timeout in seconds

    Returns:
        (relative_url, title_string_or_None)
    """
    # Build full absolute URL from base and relative path
    full_url = urllib.parse.urljoin(base_url, relative_url.lstrip("/"))
    try:
        # Use the shared session to GET the page
        resp = session.get(full_url, timeout=timeout)
        resp.raise_for_status()
        # Parse HTML and extract <title>
        soup = BeautifulSoup(resp.text, "html.parser")
        return relative_url, (soup.title.string.strip() if soup.title else None)
    except requests.RequestException:
        # Any network or HTTP error -> treat as missing title
        return relative_url, None


class TitleVerificationTest(unittest.TestCase):
    """
    Unit test for verifying webpage titles against expected values.

    The test:
    - loads expected data (list of dicts with "url" and "title")
    - concurrently fetches each page's title
    - increments stats.matched / stats.unmatched and records mismatches
    """

    def runTest(self):
        # Load expected results from the configured data path
        expected_data = load_expected_data(config.datapath)

        # Reset global stats counters used by the test runner/reporting
        stats.matched = 0
        stats.unmatched = 0
        stats.unmatched_entries = []

        # Prepare a single Session for connection pooling and a mounted adapter
        session = requests.Session()
        session.headers.update({"User-Agent": "GoDarda-TitleChecker/1.0"})
        adapter = requests.adapters.HTTPAdapter(pool_maxsize=20, max_retries=1)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        # Determine threadpool size: bounded to avoid oversubscription
        max_workers = min(20, (os.cpu_count() or 4) * 5)

        futures = {}
        print(
            "Please wait. It may take some time for the Title Verification Test to complete..."
        )

        # Use a ThreadPoolExecutor to fetch many pages concurrently
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as ex:
            for item in expected_data:
                # Schedule the fetch for each expected entry
                fut = ex.submit(
                    _fetch_title_session, session, config.base_url, item["url"], 5
                )
                futures[fut] = item

            # Process results as they complete
            for fut in concurrent.futures.as_completed(futures):
                item = futures[fut]
                rel_url, actual_title = fut.result()
                # Compare the fetched title to the expected title
                if actual_title == item["title"]:
                    stats.matched += 1
                else:
                    stats.unmatched += 1
                    # Record the relative URL and expected title
                    stats.unmatched_entries.append((rel_url, item["title"]))
