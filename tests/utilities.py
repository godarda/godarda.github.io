#!/usr/bin/env python3
"""
Shared utilities and configuration for the test suite.

This module provides:
- Environment detection (OS, paths, base URLs).
- Configuration data structures.
- Helper functions for loading expected test data from YAML files.
- Cleanup routines.
"""

# --- Standard library imports ---
import os
import platform
import sys
import shutil

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple, Union
from concurrent.futures import ThreadPoolExecutor

# --- Third-party imports ---
import yaml


@dataclass(frozen=True)
class EnvironmentConfig:
    """Configuration object holding environment-specific settings."""
    BASE_URL: str
    DATAPATH: Path
    OS_NAME: str


@dataclass
class TestStats:
    """Tracks statistics for the test run."""
    matched: int = 0
    unmatched: int = 0
    unmatched_entries: List[Tuple[str, str]] = field(default_factory=list)
    compiled: int = 0
    uncompiled: int = 0
    uncompiled_entries: List[str] = field(default_factory=list)


def get_environment_config() -> EnvironmentConfig:
    """
    Detects the host operating system and validates environment requirements.

    Returns:
        An EnvironmentConfig object containing the base URL, data path, and OS name.
        Exits the process if the OS or version is unsupported.
    """
    system_name = platform.system()
    base_url = "http://localhost:4000/"
    datapath = os.path.join(os.path.dirname(__file__), "..", "_data/")

    if system_name == "Darwin":
        os_name = "macOS"
    elif system_name == "Linux":
        # Verify that the Linux distribution is Ubuntu.
        distro_id = platform.freedesktop_os_release().get("ID", "").lower()
        if distro_id != "ubuntu":
            print(f"Unsupported Linux distribution: {distro_id}. Only Ubuntu is supported.")
            sys.exit(1)
        os_name = "Ubuntu"
    elif system_name == "Windows":
        # Verify minimum Windows build version.
        _, ver, _, _ = platform.win32_ver()
        try:
            build_number = int(ver.split(".")[2])
        except (IndexError, ValueError):
            print(f"Failed to parse Windows build from version string: {ver}")
            sys.exit(1)
        if build_number < 20348:
            print(f"Unsupported Windows build {build_number}. Requires Server 2022 (20348+) or Windows 11 (22000+).")
            sys.exit(1)
        os_name = "Windows"
    else:
        print(f"Unsupported OS: {system_name}. Only macOS, Ubuntu, and Windows are supported.")
        sys.exit(1)

    return EnvironmentConfig(
        BASE_URL=base_url,
        DATAPATH=Path(datapath),
        OS_NAME=os_name,
    )


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

    files = []
    for root, _, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith((".yml", ".yaml")):
                files.append(Path(root) / filename)
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
        # Extract entries from 'sidenav' and 'grandparent' sections.
        for section_name in ("sidenav", "grandparent"):
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


# Initialize global configuration and statistics.
CONFIG = get_environment_config()
STATS = TestStats()


def clean_pycache(cache_path: Optional[str] = None) -> None:
    """
    Removes the __pycache__ directory.

    Args:
        cache_path: Optional path to the cache directory or its parent.
                    Defaults to the directory of this module.
    """
    try:
        p = (
            Path(cache_path)
            if cache_path
            else Path(__file__).resolve().parent / "__pycache__"
        )
        # Adjust path if a parent directory was provided.
        if p.name != "__pycache__":
            p = p / "__pycache__"
        if p.exists():
            shutil.rmtree(p)
    except Exception as e:
        print(f"Cleanup warning (could not remove {cache_path or 'default'}): {e}")
