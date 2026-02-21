#!/usr/bin/env python3
"""
GoDarda Test Configuration (tests/config.py)

Purpose:
This module defines environment-specific configuration for the Playwright test suite.
It enforces strict OS validation, selects the appropriate browser engine per platform,
and provides immutable settings for consistent test execution.

Key Features:
1. Environment Detection:
   - Identifies OS, distribution, and version.
   - Validates supported platforms (macOS, Ubuntu, Windows).
2. Browser Selection:
   - macOS → Safari (WebKit)
   - Ubuntu → Firefox
   - Windows → Edge/Chrome (Chromium)
3. Configuration:
   - Defines constants for base URL, data paths, and timeouts.
   - Provides a frozen dataclass (`EnvironmentConfig`) for structured access.
"""

import os
import sys
import platform
import psutil
from pathlib import Path
from dataclasses import dataclass

SYSTEM_NAME = platform.system()

if SYSTEM_NAME == "Darwin":
    OS_NAME = "macOS"
    DISTRO_ID = None
    OS_VERSION = platform.mac_ver()[0]
    BROWSER = "webkit"

elif SYSTEM_NAME == "Linux":
    DISTRO_ID = platform.freedesktop_os_release().get("ID", "").lower()
    if DISTRO_ID != "ubuntu":
        print(f"Unsupported Linux distribution: {DISTRO_ID}. Only Ubuntu is supported.")
        sys.exit(1)
    OS_NAME = "Ubuntu"
    OS_VERSION = platform.freedesktop_os_release().get("VERSION_ID", "")
    BROWSER = "firefox"

elif SYSTEM_NAME == "Windows":
    _, VER, _, _ = platform.win32_ver()
    try:
        BUILD_NUMBER = int(VER.split(".")[2])
    except (IndexError, ValueError):
        print(f"Failed to parse Windows build from version string: {VER}")
        sys.exit(1)
    if BUILD_NUMBER < 20348:
        print(f"Unsupported Windows build {BUILD_NUMBER}. Requires Server 2022 (20348+) or Windows 11 (22000+).")
        sys.exit(1)
    OS_NAME = "Windows"
    DISTRO_ID = None
    OS_VERSION = VER
    BROWSER = "chromium"

else:
    print(f"Unsupported OS: {SYSTEM_NAME}. Only macOS, Ubuntu, and Windows are supported.")
    sys.exit(1)

# --- System Resource Analysis ---
CPU_COUNT = os.cpu_count() or 1
MEM_STATS = psutil.virtual_memory()
AVAILABLE_RAM_GB = MEM_STATS.available / (1024 ** 3)

# Default assumptions for worker calculation
ESTIMATED_GB_PER_WORKER = 1.0
MAX_WORKERS = 8
MEM_CAPACITY = int(AVAILABLE_RAM_GB / ESTIMATED_GB_PER_WORKER)
OPTIMAL_WORKERS = max(1, min(CPU_COUNT, MEM_CAPACITY, MAX_WORKERS))

BASE_URL = "http://localhost:4000/"
DATAPATH = Path(os.path.join(os.path.dirname(__file__), "..", "_data/"))
DEFAULT_TIMEOUT = 30000
NAVIGATION_TIMEOUT = 60000
IS_GITHUB_ACTIONS = os.environ.get("GITHUB_ACTIONS") == "true"

@dataclass(frozen=True)
class EnvironmentConfig:
    """
    Immutable configuration object for the test environment.
    """
    SYSTEM_NAME: str
    OS_NAME: str
    DISTRO_ID: str | None
    OS_VERSION: str
    BASE_URL: str
    DATAPATH: Path
    BROWSER: str
    DEFAULT_TIMEOUT: int
    NAVIGATION_TIMEOUT: int
    IS_GITHUB_ACTIONS: bool
    CPU_COUNT: int
    AVAILABLE_RAM_GB: float
    OPTIMAL_WORKERS: int

CONFIG = EnvironmentConfig(
    SYSTEM_NAME=SYSTEM_NAME,
    OS_NAME=OS_NAME,
    DISTRO_ID=DISTRO_ID,
    OS_VERSION=OS_VERSION,
    BASE_URL=BASE_URL,
    DATAPATH=DATAPATH,
    BROWSER=BROWSER,
    DEFAULT_TIMEOUT=DEFAULT_TIMEOUT,
    NAVIGATION_TIMEOUT=NAVIGATION_TIMEOUT,
    IS_GITHUB_ACTIONS=IS_GITHUB_ACTIONS,
    CPU_COUNT=CPU_COUNT,
    AVAILABLE_RAM_GB=AVAILABLE_RAM_GB,
    OPTIMAL_WORKERS=OPTIMAL_WORKERS
)
