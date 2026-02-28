#!/usr/bin/env python3
"""
Test Suite Utilities (tests/utilities.py)

Purpose:
This module provides shared utilities for the test suite.
It handles data loading to ensure consistent test execution across platforms.

Key Features:
1. Data Loading: Helper functions to load expected test data from YAML files.
2. Concurrency: Utilizes thread pools for efficient file processing.
"""

import os
import yaml

from pathlib import Path
from typing import List, Union
from concurrent.futures import ThreadPoolExecutor


def load_expected_data(folder_path: Union[str, Path]) -> List[dict]:
    """
    Parses YAML files in the specified directory to extract expected URL/title pairs.
    Uses concurrency to speed up file reading and deduplicates entries.

    Returns:
        A list of dictionaries containing "url" and "title" keys.
    """
    folder = Path(folder_path)
    expected = []
    if not folder.exists() or not folder.is_dir():
        return expected

    # Use rglob for cleaner recursion and filtering
    files = list(folder.rglob("*.yml")) + list(folder.rglob("*.yaml"))
    if not files:
        return expected

    def parse_file(path: Path):
        # Attempt to load YAML content safely.
        try:
            with path.open("r", encoding="utf-8") as fh:
                data = yaml.safe_load(fh) or {}
        except Exception as e:
            print(f"Warning: failed to read {path}: {e}")
            return []

        entries = []
        # Extract entries from 'grandparent' sections.
        for section_name in ("grandparent",):
            for section in data.get(section_name, []):
                if "url" in section and "parent" in section:
                    entries.append((section["url"], section["parent"]))
                for child in section.get("children", []):
                    if "url" in child and "title" in child:
                        entries.append((child["url"], child["title"]))
        return entries

    # Use a thread pool to parse files concurrently.
    max_workers = min(32, max(2, (os.cpu_count() or 2) * 2))
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        for res in ex.map(parse_file, files):
            if res:
                results.extend(res)

    # Deduplicate results while preserving order.
    seen = set()
    unique_entries = []
    for url, title in results:
        key = (url, title)
        if key not in seen:
            unique_entries.append({"url": url, "title": title})
            seen.add(key)

    return unique_entries
