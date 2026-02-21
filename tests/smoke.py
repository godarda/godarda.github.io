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
import os
import sys
import concurrent.futures
from playwright.sync_api import sync_playwright  # type: ignore
from config import CONFIG
from utilities import load_expected_data
from stats import STATS


def verify_chunk(urls):
    """
    Worker function to verify a chunk of URLs in a separate browser instance.
    Updates global STATS object directly.
    """
    with sync_playwright() as p:
        browser_type = getattr(p, CONFIG.BROWSER)
        try:
            launch_args = []
            # Use a fixed viewport size (1280x720) to ensure the browser window
            # fits within standard screen resolutions without overflowing.
            context_args = {"viewport": {"width": 1280, "height": 720}}
            browser = browser_type.launch(headless=CONFIG.IS_GITHUB_ACTIONS, args=launch_args)
            page = browser.new_page(**context_args)
        except Exception as e:
            # Mark all as failed if browser fails to launch
            for entry in urls:
                STATS.add_title_result(False, (entry["url"], f"Browser Launch Failed: {e}"))
            return

        for entry in urls:
            relative_url = entry["url"]
            expected_title = entry["title"]
            # Ensure clean URL construction
            full_url = urllib.parse.urljoin(CONFIG.BASE_URL, relative_url.lstrip("/"))

            try:
                page.goto(full_url, timeout=CONFIG.NAVIGATION_TIMEOUT)
                actual_title = page.title()

                if actual_title == expected_title:
                    STATS.add_title_result(True, (relative_url, actual_title))
                else:
                    STATS.add_title_result(False, (relative_url, expected_title))

            except Exception as e:
                STATS.add_title_result(False, (relative_url, f"Error: {str(e)}"), is_error=True)

        browser.close()


def verify_page_titles():
    """
    Verifies that the title of each page matches the expected value defined in the data files.
    Runs in parallel using multiple browser instances.
    """
    # Load expected data.
    expected_data = load_expected_data(CONFIG.DATAPATH)
    STATS.total_urls = len(expected_data)

    if not expected_data:
        return

    total_urls = len(expected_data)

    num_instances = CONFIG.OPTIMAL_WORKERS
    print(f"Using {num_instances} browser instances (Available RAM: {CONFIG.AVAILABLE_RAM_GB:.2f} GB)")
    chunk_size = math.ceil(total_urls / num_instances)

    # Create chunks
    chunks = [expected_data[i:i + chunk_size] for i in range(0, total_urls, chunk_size)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_instances) as executor:
        # Use executor.map to run verify_chunk for each chunk.
        # This blocks until all tasks are complete. We wrap it in a list
        # to ensure execution and to catch exceptions from workers.
        try:
            # list() consumes the iterator returned by map, ensuring all tasks run.
            list(executor.map(verify_chunk, chunks))
        except Exception as exc:
            print(f'\n\033[91mA test chunk generated an exception: {exc}\033[0m')
