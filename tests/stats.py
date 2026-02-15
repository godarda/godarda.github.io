#!/usr/bin/env python3
"""
Test Statistics (tests/stats.py)

Purpose:
This module defines the data structure for tracking test execution statistics.
It provides a global STATS object used across different test modules to accumulate results.
"""

from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class TestStats:
    """Tracks statistics for the test run."""
    matched: int = 0
    unmatched: int = 0
    unmatched_entries: List[Tuple[str, str]] = field(default_factory=list)
    compiled: int = 0
    uncompiled: int = 0
    uncompiled_entries: List[str] = field(default_factory=list)

# Initialize global statistics.
STATS = TestStats()
