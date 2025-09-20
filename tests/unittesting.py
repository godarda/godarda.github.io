#!/usr/bin/env python3
"""
Author: Shubham Darda
Purpose:
    Title verification unit test for the GoDarda static site.

Description:
    This module performs concurrent HTTP fetches of site pages and validates that
    each page's <title> element matches the expected value loaded from the
    repository _data YAML files. It is optimized for CI-friendly output and
    efficient network use by reusing a single requests.Session and a bounded
    ThreadPoolExecutor.

Guidelines:
    - Reuse a single requests.Session to leverage connection pooling and reduce
      test runtime.
    - Bound the thread pool size to avoid oversubscribing small CI runners.
    - Fail-fast on excessive mismatches to surface server-wide problems early.
    - Keep printed output concise for readability in CI logs.
"""

import os
import requests
import unittest
import concurrent.futures
import urllib.parse
from requests.adapters import HTTPAdapter
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
        title_text = (
            soup.title.string.strip() if soup.title and soup.title.string else None
        )
        return relative_url, title_text
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
        if not expected_data:
            self.skipTest("No expected data loaded; skipping title verification test.")
        # Prepare a single Session for connection pooling and a mounted adapter
        session = requests.Session()
        session.headers.update({"User-Agent": "GoDarda-TitleChecker/1.0"})
        adapter = HTTPAdapter(pool_maxsize=20, max_retries=1)
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
                    # Fail-fast: abort if too many mismatches
                    if stats.unmatched > 10:
                        print("\n\033[91mToo many unmatched titles.\033[0m")
                        print(
                            "This likely indicates a server down, broken selectors, or bad input."
                        )
                        os._exit(1)

            # Explicitly close session to release connections
            session.close()
