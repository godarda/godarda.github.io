#!/usr/bin/env python3
"""
Smoke Tests (tests/smoke.py)

Purpose:
This script performs smoke testing using Playwright to verify that all pages
load correctly and display the expected titles. It serves as a high-level
validation of the deployed site or local development server.

Key Features:
1. Playwright Integration: Uses the Playwright engine for reliable browser automation.
2. Concurrency: Runs verification in parallel using thread pools.
3. Data Validation: Compares actual page titles against expected values.
"""

import urllib.parse
import math
from concurrent.futures import ThreadPoolExecutor
from playwright.sync_api import sync_playwright
from config import CONFIG
from utilities import load_expected_data
from stats import STATS

def verify_chunk(urls):
    """
    Worker function to verify a chunk of URLs in a separate browser instance.
    """
    local_matched = 0
    local_unmatched = 0
    local_unmatched_entries = []

    with sync_playwright() as p:
        browser_type = getattr(p, CONFIG.BROWSER)
        try:
            # Note: --start-maximized is a Chromium-specific flag.
            launch_args = ["--start-maximized"] if CONFIG.BROWSER == "chromium" else []
            browser = browser_type.launch(headless=CONFIG.IS_GITHUB_ACTIONS, args=launch_args)
            page = browser.new_page(no_viewport=True)
        except Exception:
            # Mark all as failed if browser fails to launch
            for entry in urls:
                local_unmatched += 1
                local_unmatched_entries.append((entry["url"], "Browser Launch Failed"))
            return local_matched, local_unmatched, local_unmatched_entries

        for entry in urls:
            relative_url = entry["url"]
            expected_title = entry["title"]
            # Ensure clean URL construction
            full_url = urllib.parse.urljoin(CONFIG.BASE_URL, relative_url.lstrip("/"))

            try:
                page.goto(full_url, timeout=CONFIG.NAVIGATION_TIMEOUT)
                actual_title = page.title()

                if actual_title == expected_title:
                    local_matched += 1
                else:
                    local_unmatched += 1
                    local_unmatched_entries.append((relative_url, expected_title))

            except Exception as e:
                local_unmatched += 1
                local_unmatched_entries.append((relative_url, f"Error: {str(e)}"))

        browser.close()

    return local_matched, local_unmatched, local_unmatched_entries

def verify_page_titles():
    """
    Verifies that the title of each page matches the expected value defined in the data files.
    Runs in parallel using multiple browser instances.
    """
    # Load expected data.
    expected_data = load_expected_data(CONFIG.DATAPATH)

    if not expected_data:
        return

    total_urls = len(expected_data)

    num_instances = 5
    # Calculate chunk size
    chunk_size = math.ceil(total_urls / num_instances)

    # Create chunks
    chunks = [expected_data[i:i + chunk_size] for i in range(0, total_urls, chunk_size)]

    with ThreadPoolExecutor(max_workers=num_instances) as executor:
        futures = []
        for chunk in chunks:
            futures.append(executor.submit(verify_chunk, chunk))

        for future in futures:
            matched, unmatched, unmatched_entries = future.result()
            STATS.matched += matched
            STATS.unmatched += unmatched
            STATS.unmatched_entries.extend(unmatched_entries)
