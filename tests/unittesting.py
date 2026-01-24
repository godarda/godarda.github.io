#!/usr/bin/env python3
"""
Unit tests for verifying the integrity of the deployed static site.

This module:
- Performs concurrent HTTP requests to validate page titles.
- Verifies that <title> tags match expected values from data files.
- Utilizes a thread pool for efficient network I/O.
"""

import os
import requests
import unittest
import sys
import concurrent.futures
import urllib.parse
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
from utilities import CONFIG, STATS, load_expected_data


def fetch_page_title(
    session: requests.Session, base_url: str, relative_url: str, timeout: int = 5
):
    """
    Fetches the page title for a given URL using a shared session.

    Returns:
        A tuple containing the relative URL and the extracted title string (or None if failed).
    """
    # Construct the absolute URL.
    full_url = urllib.parse.urljoin(base_url, relative_url.lstrip("/"))
    try:
        # Perform the GET request.
        resp = session.get(full_url, timeout=timeout)
        resp.raise_for_status()
        # Parse the response content to extract the <title> tag.
        soup = BeautifulSoup(resp.text, "html.parser")
        title_text = (
            soup.title.string.strip() if soup.title and soup.title.string else None
        )
        return relative_url, title_text
    except requests.RequestException:
        # Treat network or HTTP errors as a missing title.
        return relative_url, None


class TitleVerificationTest(unittest.TestCase):
    """
    Test case for verifying that webpage titles match expected values.
    """

    def test_site_titles(self):
        # Load expected URL/title pairs from the data directory.
        expected_data = load_expected_data(CONFIG.DATAPATH)
        if not expected_data:
            self.skipTest("No expected data loaded; skipping title verification test.")
        
        # Initialize a session with connection pooling.
        session = requests.Session()
        session.headers.update({"User-Agent": "GoDarda-TitleChecker/1.0"})
        adapter = HTTPAdapter(pool_maxsize=20, max_retries=1)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        # Calculate an appropriate thread pool size.
        max_workers = min(20, (os.cpu_count() or 4) * 5)

        futures = {}

        # Execute requests concurrently.
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            for expected_entry in expected_data:
                future = executor.submit(
                    fetch_page_title, session, CONFIG.BASE_URL, expected_entry["url"], 5
                )
                futures[future] = expected_entry

            # Process results as they become available.
            for future in concurrent.futures.as_completed(futures):
                expected_entry = futures[future]
                rel_url, actual_title = future.result()
                
                if actual_title == expected_entry["title"]:
                    STATS.matched += 1
                else:
                    STATS.unmatched += 1
                    STATS.unmatched_entries.append((rel_url, expected_entry["title"]))
                    
                    # Abort early if a significant number of mismatches occur.
                    if STATS.unmatched > 10:
                        print("\n\033[91mToo many unmatched titles.\033[0m")
                        print(
                            "This likely indicates a server down, broken selectors, or bad input."
                        )
                        sys.exit(1)

            # Clean up session resources.
            session.close()
