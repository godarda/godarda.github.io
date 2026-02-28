#!/usr/bin/env python3
"""
Test Statistics (tests/stats.py)

Purpose:
This module defines the data structure for tracking test execution statistics.
It provides a global STATS object used across different test modules to accumulate results.
"""

from dataclasses import dataclass, field
from typing import List, Tuple
from threading import Lock

@dataclass
class TestStats:
    """Tracks statistics for the test run."""
    total_urls: int = 0
    matched: int = 0
    unmatched: int = 0
    unmatched_entries: List[Tuple[str, str]] = field(default_factory=list)
    total_files: int = 0

    compiled: int = 0
    uncompiled: int = 0
    uncompiled_entries: List[str] = field(default_factory=list)
    aborted: bool = False

    _lock: Lock = field(default_factory=Lock, repr=False, init=False, compare=False)

    def add_title_result(self, matched: bool, entry: Tuple[str, str], is_error: bool = False) -> int:
        """Thread-safely add a title verification result. Returns new unmatched count."""
        with self._lock:
            if matched:
                self.matched += 1
            else:
                self.unmatched += 1
                if not is_error:
                    self.unmatched_entries.append(entry)
            return self.unmatched

# Initialize global statistics.
STATS = TestStats()
