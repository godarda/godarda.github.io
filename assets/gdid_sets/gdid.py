#!/usr/bin/env python3
"""
GDID Maintenance Utility (assets/gdid_sets/gdid.py)

Purpose:
This script maintains the integrity of GoDarda IDs (GDIDs) across
the repository. GDIDs are unique identifiers for webpages within the project.
It reconciles usage, updates set files, and ensures consistency in navigation data.

Key Features:
1. Usage Scanning: Scans Markdown, YAML, and other files for GDID references.
2. Reconciliation: Updates `gdid_set*.txt` files to reflect current usage.
3. Metadata Sync: Updates YAML navigation data from generated HTML metadata.
4. Validation: Reports non-standard filenames or invalid IDs.
"""

import re
import yaml
import os
import logging
import functools
from pathlib import Path
from threading import Lock
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict
from typing import Set, Dict, List, Tuple, Optional, Callable

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

# Use C-based YAML loader/dumper if available for performance
try:
    from yaml import CSafeLoader as Loader, CSafeDumper as Dumper
except ImportError:
    from yaml import SafeLoader as Loader, SafeDumper as Dumper

# Compiled Regex Patterns
GDID_PATTERN = re.compile(r"\b(gd[a-z]{5})\b")
MARKDOWN_LINK_PATTERN = re.compile(r"\[(gd[a-z]{5})\]")

SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH
while REPO_ROOT != REPO_ROOT.parent:
    if (REPO_ROOT / ".git").exists() or (REPO_ROOT / "index.html").exists():
        break
    REPO_ROOT = REPO_ROOT.parent
else:
    raise RuntimeError("Repo root not found")

SETS_DIR = REPO_ROOT / "assets" / "gdid_sets"
GITIGNORE_FILE = REPO_ROOT / ".gitignore"
INVALID_FILE = SETS_DIR / "invalid.txt"
URL_YML_FILE = REPO_ROOT / "_data" / "url.yml"


def load_gitignore() -> Set[str]:
    """
    Loads ignored paths from the repository's .gitignore file.
    Comments and empty lines are skipped. Trailing slashes are removed.

    Returns:
        A set of top-level ignored path strings.
    """
    ignored = set()
    if GITIGNORE_FILE.exists():
        for line in GITIGNORE_FILE.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                ignored.add(line.rstrip("/"))
    return ignored


def collect_all_files(ignored: Set[str]) -> Tuple[List[Path], List[Path]]:
    """
    Collects all relevant files in a single pass.
    Returns (md_files, other_files).
    """
    md_files = []
    other_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        # Prune ignored directories
        dirs[:] = [d for d in dirs if d not in ignored and d != ".git" and d != "_site"]
        for filename in files:
            if filename in ignored:
                continue
            path = Path(root) / filename
            if filename.endswith(".md"):
                md_files.append(path)
            elif filename != "url.yml":
                other_files.append(path)
    return md_files, other_files


def load_gdids_by_file() -> Dict[Path, List[str]]:
    """
    Parses `gdid_set*.txt` files to load GDIDs.

    Returns:
        A dictionary mapping each set file path to a list of GDIDs found within it.
    """
    gdid_map = defaultdict(list)
    for txt_file in sorted(SETS_DIR.glob("gdid_set*.txt")):
        for line in txt_file.read_text(encoding="utf-8").splitlines():
            token = line.strip().split(" -")[0]
            if GDID_PATTERN.fullmatch(token):
                gdid_map[txt_file].append(token)
    return gdid_map


def scan_markdown_files(all_gdids: Set[str], md_files: List[Path]) -> Dict[str, List[str]]:
    """
    Scans all Markdown files for GDID references.
    This function concurrently searches for `[gdid]` patterns in `.md` files.

    Args:
        all_gdids: A set of all known GDIDs to validate against.
        md_files: List of markdown files to scan.

    Returns:
        A dictionary mapping each found GDID to a list of its locations.
    """
    usage = defaultdict(list)

    def process_md(file: Path):
        rel_path = file.relative_to(REPO_ROOT).as_posix()
        found = []
        try:
            text = file.read_text(encoding="utf-8", errors="ignore")
            if not GDID_PATTERN.search(text):
                return found

            for match in MARKDOWN_LINK_PATTERN.finditer(text):
                token = match.group(1)
                if token in all_gdids:
                    line_num = text.count('\n', 0, match.start()) + 1
                    found.append((token, f"{rel_path} (line {line_num})"))
        except Exception:
            pass
        return found

    def process_batch(files: List[Path]) -> List[Tuple[str, str]]:
        results = []
        for file in files:
            results.extend(process_md(file))
        return results

    chunk_size = 50
    chunks = [md_files[i : i + chunk_size] for i in range(0, len(md_files), chunk_size)]

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_batch, chunk) for chunk in chunks]
        for future in as_completed(futures):
            for gid, ref in future.result():
                usage[gid].append(ref)

    return usage


def scan_url_yml(all_gdids: Set[str]) -> Dict[str, List[str]]:
    """
    Scans the `_data/url.yml` file for GDID keys.

    Args:
        all_gdids: A set of all known GDIDs to validate against.

    Returns:
        A dictionary mapping each found GDID to its location in `url.yml`.
    """
    usage = defaultdict(list)
    if not URL_YML_FILE.exists():
        return usage

    rel_path = URL_YML_FILE.relative_to(REPO_ROOT).as_posix()
    try:
        for i, line in enumerate(
            URL_YML_FILE.read_text(encoding="utf-8").splitlines(), 1
        ):
            line = line.strip()
            if ":" in line:
                key = line.split(":", 1)[0].strip()
                if GDID_PATTERN.fullmatch(key) and key in all_gdids:
                    usage[key].append(f"{rel_path} (line {i})")
    except Exception as e:
        logger.error(f"Failed to read {rel_path}: {e}")

    return usage


def scan_repo_files(all_gdids: Set[str], files_to_scan: List[Path]) -> Dict[str, List[str]]:
    """
    Scans repository files for GDID usage and non-standard filenames.
    This scan looks for GDIDs in filenames and identifies page files that
    do not follow the standard `gdid.html` naming convention. Non-standard
    filenames are written to `invalid.txt`.

    Args:
        all_gdids: A set of all known GDIDs to validate against.
        files_to_scan: List of files to scan.

    Returns:
        A dictionary mapping each found GDID to a list of file paths.
    """
    usage = defaultdict(list)
    nonstandard_ids = []

    def process_batch(files: List[Path]) -> Tuple[List[Tuple[str, str]], List[str]]:
        batch_usage = []
        batch_nonstandard = []
        for file in files:
            rel_path = file.relative_to(REPO_ROOT).as_posix()
            name = file.name
            stem = file.stem.strip()

            # Match GDID-style filenames
            for word in GDID_PATTERN.findall(name):
                if word in all_gdids:
                    batch_usage.append((word, rel_path))

            # Detect nonstandard filenames in pages/
            if "pages" in rel_path and name != "index.html":
                if not stem.startswith("gd") or len(stem) != 7:
                    batch_nonstandard.append(f"{stem},{rel_path}")
        return batch_usage, batch_nonstandard

    chunk_size = 200
    chunks = [files_to_scan[i : i + chunk_size] for i in range(0, len(files_to_scan), chunk_size)]

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_batch, chunk) for chunk in chunks]
        for future in as_completed(futures):
            found, nonstandard = future.result()
            for gid, ref in found:
                usage[gid].append(ref)
            nonstandard_ids.extend(nonstandard)

    INVALID_FILE.write_text(
        (
            "\n".join(nonstandard_ids)
            if nonstandard_ids
            else "No non-standard IDs found during scan."
        ),
        encoding="utf-8",
    )

    return usage


@functools.lru_cache(maxsize=None)
def extract_metadata_from_html(html_path: Path) -> Tuple[str, str]:
    """
    Extracts permalink and title from a Jekyll-generated HTML file.

    Args:
        html_path: The path to the HTML file.

    Returns:
        A tuple containing the permalink and title.

    Raises:
        ValueError: If permalink or title metadata is missing.
    """
    permalink, title = None, None
    try:
        with html_path.open("r", encoding="utf-8") as f:
            for _ in range(50):  # Read first 50 lines only
                line = f.readline()
                if not line: break
                line = line.strip()
                if line.startswith("permalink:"):
                    permalink = line.split("permalink:", 1)[1].strip()
                elif line.startswith("title:"):
                    title = line.split("title:", 1)[1].strip()
                if permalink and title:
                    break
    except Exception:
        pass

    if not permalink or not title:
        raise ValueError(f"Missing permalink or title in {html_path}")
    return permalink, title


class YamlManager:
    """
    Manages thread-safe updates to YAML navigation files.
    Caches loaded YAML data to minimize disk I/O and writes changes in batches.
    """
    def __init__(self):
        self.cache = {}
        self.dirty = set()
        self.lock = Lock()

    def update(self, html_path: Path):
        try:
            permalink, title = extract_metadata_from_html(html_path)
        except (ValueError, FileNotFoundError):
            return

        normalized_permalink = permalink.rstrip('.html')
        parts = normalized_permalink.lstrip('/').split('/')

        if len(parts) < 2:
            return

        section_key, subsection_key = parts[0], parts[1]
        data_dir = REPO_ROOT / "_data"

        with self.lock:
            yml_path = data_dir / f"{section_key}.yml"
            if not yml_path.exists():
                candidates = list(data_dir.rglob(f"{section_key}.yml"))
                if candidates:
                    yml_path = candidates[0]
                else:
                    return

            if yml_path not in self.cache:
                try:
                    self.cache[yml_path] = yaml.load(yml_path.read_text(encoding='utf-8'), Loader=Loader) or {}
                except Exception:
                    self.cache[yml_path] = {}

            data = self.cache[yml_path]
            updated = False
            for section in data.get('grandparent', []):
                if not isinstance(section, dict):
                    continue

                if section.get('url', '').strip('/') == f"{section_key}/{subsection_key}":
                    children = section.get('children')
                    if not isinstance(children, list):
                        children = []
                        section['children'] = children

                    if any(child.get('url', '').rstrip('.html') == normalized_permalink for child in children):
                        continue

                    children.append({'title': title, 'url': permalink})
                    updated = True
                    break

            if updated:
                self.dirty.add(yml_path)

    def save(self):
        for yml_path in self.dirty:
            try:
                data = self.cache[yml_path]
                yml_path.write_text(yaml.dump(data, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=float("inf")), encoding='utf-8')
                logger.info(f"Updated {yml_path.name}")
            except Exception as e:
                logger.error(f"Failed to save {yml_path}: {e}")

YAML_MANAGER = YamlManager()

def update_yaml(html_path: Path):
    YAML_MANAGER.update(html_path)


def update_set_files(gdid_map: Dict[Path, List[str]], usage: Dict[str, List[str]]):
    """
    Reconciles `gdid_set*.txt` files with current GDID usage.
    For each set file, this function updates entries with usage references,
    separates used and unused GDIDs, and preserves comments. It also triggers
    YAML navigation updates for GDIDs linked to HTML pages.

    Args:
        gdid_map: A dictionary mapping set file paths to their GDIDs.
        usage: A dictionary mapping GDIDs to their usage locations.
    """
    def process_file(txt_file: Path, gdids: list):
        original_lines = txt_file.read_text(encoding="utf-8").splitlines()
        comments, unused, used_entries = [], [], []
        seen = set()

        for line in original_lines:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                comments.append(line)
                continue

            token = stripped.split(" -")[0].strip()
            seen.add(token)

            refs = usage.get(token, [])
            if token in gdids:
                if refs:
                    usage_str = "; ".join(sorted(refs))
                    used_entries.append((token, usage_str))
                    for ref in refs:
                        if ref.startswith("pages/") and ref.endswith(".html"):
                            update_yaml(REPO_ROOT / ref)
                else:
                    unused.append(token)
            else:
                comments.append(line)

        # Include GDIDs not originally listed
        for token in gdids:
            if token not in seen:
                refs = usage.get(token, [])
                if refs:
                    usage_str = "; ".join(sorted(refs))
                    used_entries.append((token, usage_str))
                else:
                    unused.append(token)

        # Sort used GDIDs by first usage path and line number
        def sort_key(item):
            first_usage = item[1].split(";")[0].strip()
            match = re.match(r"(.+?) \(line (\d+)\)", first_usage)
            if match:
                path, line = match.groups()
                return (path.lower(), int(line))
            return (first_usage.lower(), 0)

        sorted_used = sorted(used_entries, key=sort_key)
        used_lines = [f"{gid} - {refs}" for gid, refs in sorted_used]
        updated_lines = comments + unused + used_lines

        txt_file.write_text("\n".join(updated_lines), encoding="utf-8")

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(process_file, txt_file, gdids)
            for txt_file, gdids in gdid_map.items()
        ]
        for future in as_completed(futures):
            future.result()


def main():
    """
    Orchestrates the GDID reconciliation process.
    This involves loading GDIDs and ignore patterns, scanning all repository
    files for GDID usage, and updating the set files with the findings.
    """
    ignored = load_gitignore()
    gdid_map = load_gdids_by_file()
    all_gdids = {gid for gid_list in gdid_map.values() for gid in gid_list}
    md_files, repo_files = collect_all_files(ignored)

    with ThreadPoolExecutor() as executor:
        future_md = executor.submit(scan_markdown_files, all_gdids, md_files)
        future_yml = executor.submit(scan_url_yml, all_gdids)
        future_repo = executor.submit(scan_repo_files, all_gdids, repo_files)

        usage_md = future_md.result()
        usage_yml = future_yml.result()
        usage_repo = future_repo.result()

    # Merge all usage maps
    usage = defaultdict(list)
    for source in [usage_md, usage_yml, usage_repo]:
        for gid, refs in source.items():
            usage[gid].extend(refs)

    update_set_files(gdid_map, usage)
    YAML_MANAGER.save()


if __name__ == "__main__":
    main()
