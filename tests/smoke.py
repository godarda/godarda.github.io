#!/usr/bin/env python3
"""
Smoke Tests (tests/smoke.py)

Purpose:
This script performs smoke testing using Playwright to verify that all pages
load correctly and display the expected titles. It serves as a high-level
validation of the deployed site or local development server.

Key Features:
1. Playwright Integration: Uses the Playwright engine for reliable browser automation.
2. Concurrency: Distributes work to parallel browser workers using a dynamic queue
   for resilient, efficient execution.
3. Data Validation: Compares actual page titles against expected values.
"""

import urllib.parse
import math
import concurrent.futures
from playwright.sync_api import sync_playwright  # type: ignore
import queue
from config import CONFIG
from utilities import load_expected_data
from stats import STATS


def browser_worker(work_queue: queue.Queue):
    """
    Worker that launches a browser and processes URLs from a shared queue.
    If the browser is closed, it re-queues its current task and terminates.
    """
    browser = None
    try:
        with sync_playwright() as p:
            browser_type = getattr(p, CONFIG.BROWSER)
            launch_args = ["--start-maximized"] if CONFIG.BROWSER == "chromium" else []
            context_args = {"no_viewport": True}
            browser = browser_type.launch(headless=CONFIG.IS_GITHUB_ACTIONS, args=launch_args)
            page = browser.new_page(**context_args)

            while True:
                try:
                    entry = work_queue.get_nowait()
                except queue.Empty:
                    # No more work in the queue, this worker can exit.
                    break

                relative_url = entry["url"]
                expected_title = entry["title"]
                full_url = urllib.parse.urljoin(CONFIG.BASE_URL, relative_url.lstrip("/"))

                try:
                    page.goto(full_url, timeout=CONFIG.NAVIGATION_TIMEOUT)
                    actual_title = page.title()

                    if actual_title == expected_title:
                        STATS.add_title_result(True, (relative_url, actual_title))
                    else:
                        STATS.add_title_result(False, (relative_url, expected_title))

                except Exception as e:
                    # Check if browser/page state indicates closure, even if the error message doesn't.
                    if not browser.is_connected() or page.is_closed():
                        work_queue.put(entry)
                        return

                    error_str = str(e).lower()
                    if "target closed" in error_str or "browser has been closed" in error_str:
                        work_queue.put(entry)  # Put the work back for another worker.
                        return  # Exit the function, terminating this worker.

                    error_message = f"Error: {str(e)}"
                    STATS.add_title_result(False, (relative_url, error_message), is_error=True)

    except Exception as e:
        print(f"\n\033[91mBrowser worker failed to start: {e}\033[0m")
    finally:
        if browser and browser.is_connected():
            try:
                browser.close()
            except Exception:
                pass  # Ignore errors on close, as the browser might already be gone.


def verify_page_titles():
    """
    Verifies page titles by distributing URLs to a pool of persistent browser workers
    via a shared queue. If a worker fails, its work is automatically redistributed.
    """
    expected_data = load_expected_data(CONFIG.DATAPATH)
    STATS.total_urls = len(expected_data)

    if not expected_data:
        return

    # Create a thread-safe queue and populate it with all URLs.
    work_queue = queue.Queue()
    for item in expected_data:
        work_queue.put(item)

    num_instances = CONFIG.OPTIMAL_WORKERS
    print(f"Using {num_instances} browser instances (Available RAM: {CONFIG.AVAILABLE_RAM_GB:.2f} GB)")

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_instances) as executor:
        # Each future represents one worker that will run until the queue is empty.
        futures = [executor.submit(browser_worker, work_queue) for _ in range(num_instances)]
        try:
            concurrent.futures.wait(futures)
        except Exception as exc:
            print(f'\n\033[91mA test worker generated an unhandled exception: {exc}\033[0m')
