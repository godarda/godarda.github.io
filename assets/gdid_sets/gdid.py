#!/usr/bin/env python3
"""
Author:  GoDarda Site Automation
Purpose:
    Maintain and reconcile GDID sets used across the repository.

Description:
    This module provides utilities to:
      - Locate the repository root dynamically from the script location.
      - Load GDID identifiers from gdid_set*.txt files.
      - Scan markdown, yaml, and other repository files for usages of GDIDs.
      - Detect non-standard page filenames and write them to an invalid.txt file.
      - Extract title and permalink metadata from generated HTML and update
        the corresponding YAML navigation data.
      - Update gdid_set*.txt files with usage references and trigger YAML updates.

Guidelines:
    - Keep functions small and focused; prefer explicit error messages to aid CI/debugging.
    - Concurrency is used for IO-bound scans to improve performance on large repos.
    - Avoid destructive operations; updates are limited to known metadata and set files.
"""
import re
import yaml
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict


# ------------------------------------------------------------
# Resolve repo root dynamically
# ------------------------------------------------------------
def find_repo_root(start_path: Path) -> Path:
    """
    Ascend the filesystem from start_path until a repository sentinel is found.

    Behavior:
      - Recognizes repository root by presence of a .git folder or an index.html file.
      - Raises RuntimeError if no repo root is found up to filesystem root.

    Notes:
      - Using Path.resolve() upstream is recommended so symlinks are handled.
    """
    current = start_path
    while current != current.parent:
        if (current / ".git").exists() or (current / "index.html").exists():
            return current
        current = current.parent
    raise RuntimeError("Repo root not found")


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = find_repo_root(SCRIPT_PATH)
SETS_DIR = REPO_ROOT / "assets" / "gdid_sets"
GITIGNORE_FILE = REPO_ROOT / ".gitignore"
INVALID_FILE = SETS_DIR / "invalid.txt"
URL_YML_FILE = REPO_ROOT / "_data" / "url.yml"


def load_gitignore() -> set:
    """
    Read the repository .gitignore and return a set of top-level ignored paths.

    Behavior:
      - Strips comments and trailing slashes.
      - Returns an empty set if .gitignore is missing.
    """
    ignored = set()
    if GITIGNORE_FILE.exists():
        for line in GITIGNORE_FILE.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                ignored.add(line.rstrip("/"))
    return ignored


def load_gdids_by_file() -> dict:
    """
    Parse gdid_set*.txt files in the assets/gdid_sets directory.

    Returns:
      dict mapping Path -> list of GDID tokens found in the file.

    Notes:
      - Tokens are validated to match the expected 'gd' prefix and length.
      - Non-matching lines are ignored (comments/blank lines preserved elsewhere).
    """
    gdid_map = defaultdict(list)
    for txt_file in sorted(SETS_DIR.glob("gdid_set*.txt")):
        for line in txt_file.read_text(encoding="utf-8").splitlines():
            token = line.strip().split(" -")[0]
            if token.startswith("gd") and len(token) == 7 and token.isalpha():
                gdid_map[txt_file].append(token)
    return gdid_map


def scan_markdown_files(all_gdids: set) -> dict:
    """
    Concurrently scan all markdown (.md) files in the repo for referenced GDIDs.

    Returns:
      defaultdict(list) mapping gdid -> list of "relative_path (line N)" references.

    Implementation notes:
      - Uses a regex to locate bracketed tokens like [gdxxxxx].
      - Skips binary/unreadable files by ignoring read errors.
      - ThreadPoolExecutor is used to parallelize IO-bound scanning.
    """
    usage = defaultdict(list)
    md_files = list(REPO_ROOT.rglob("*.md"))

    def process_md(file: Path):
        rel_path = file.relative_to(REPO_ROOT).as_posix()
        found = []
        try:
            for i, line in enumerate(
                file.read_text(encoding="utf-8", errors="ignore").splitlines(), 1
            ):
                for token in re.findall(r"\[([^\]]+)\]", line):
                    if (
                        token.startswith("gd")
                        and len(token) == 7
                        and token in all_gdids
                    ):
                        found.append((token, f"{rel_path} (line {i})"))
        except Exception:
            pass
        return found

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_md, file) for file in md_files]
        for future in as_completed(futures):
            for gid, ref in future.result():
                usage[gid].append(ref)

    return usage


def scan_url_yml(all_gdids: set) -> dict:
    """
    Scan the _data/url.yml file for GDID keys.

    Returns:
      defaultdict(list) mapping gdid -> list of "url.yml (line N)" references.

    Notes:
      - Only checks top-level YAML keys in "key: value" lines for GDID-like keys.
      - Returns empty mapping if file doesn't exist.
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
                if (
                    key.startswith("gd")
                    and len(key) == 7
                    and key.isalpha()
                    and key in all_gdids
                ):
                    usage[key].append(f"{rel_path} (line {i})")
    except Exception as e:
        print(f"Failed to read {rel_path}: {e}")

    return usage


def scan_repo_files(all_gdids: set, ignored: set) -> dict:
    """
    Scan non-markdown repo files for GDID usage and collect non-standard page IDs.

    Returns:
      defaultdict(list) mapping gdid -> list of relative path references.

    Side-effects:
      - Writes a list of non-standard IDs and their paths to assets/gdid_sets/invalid.txt.

    Behavior:
      - Skips files under .git and paths matching .gitignore entries.
      - Looks for gd-prefixed 7-letter tokens in filenames.
      - Flags pages/* files whose stem does not match the expected gdxxxxxx pattern.
    """
    usage = defaultdict(list)
    nonstandard_ids = []

    files = [
        f
        for f in REPO_ROOT.rglob("*")
        if f.is_file() and not f.name.endswith(".md") and f.name != "url.yml"
    ]

    def process_file(file: Path):
        rel_path = file.relative_to(REPO_ROOT).as_posix()
        if ".git" in rel_path or any(part in Path(rel_path).parts for part in ignored):
            return [], None

        found = []
        name = file.name
        stem = file.stem.strip()

        # Match GDID-style filenames
        for word in re.findall(r"\b[a-z]{7}\b", name):
            if word.startswith("gd") and word in all_gdids:
                found.append((word, rel_path))

        # Detect nonstandard filenames in pages/
        if "pages" in rel_path and name != "index.html":
            if not stem.startswith("gd") or len(stem) != 7:
                return found, f"{stem},{rel_path}"

        return found, None

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_file, file) for file in files]
        for future in as_completed(futures):
            found, nonstandard = future.result()
            for gid, ref in found:
                usage[gid].append(ref)
            if nonstandard:
                nonstandard_ids.append(nonstandard)

    INVALID_FILE.write_text(
        (
            "\n".join(nonstandard_ids)
            if nonstandard_ids
            else "No non-standard IDs found during scan."
        ),
        encoding="utf-8",
    )

    return usage


def extract_metadata_from_html(html_path: Path) -> tuple:
    """
    Extract permalink and title metadata lines from a generated HTML file.

    Returns:
      (permalink, title)

    Raises:
      ValueError if either permalink or title cannot be found.

    Notes:
      - Assumes YAML front-matter style lines like "permalink: /path" and "title: My Title".
      - Stops early once both values are discovered.
    """
    permalink, title = None, None
    for line in html_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("permalink:"):
            permalink = line.split("permalink:")[1].strip()
        elif line.startswith("title:"):
            title = line.split("title:")[1].strip()
        if permalink and title:
            break
    if not permalink or not title:
        raise ValueError(f"Missing permalink or title in {html_path}")
    return permalink, title


def update_yaml(html_path: Path):
    """
    Given a path to a generated HTML page under pages/, insert its title/permalink
    into the appropriate section YAML file under _data.

    Behavior:
      - Normalizes permalink (removes trailing .html for matching).
      - Locates a YAML file named <section_key>.yml under _data.
      - Searches 'grandparent' sections for a matching parent URL and appends a child.
      - Writes back the YAML preserving key order (sort_keys=False).

    Raises:
      FileNotFoundError if the expected YAML file is missing.
      ValueError if the permalink format is unexpected or the matching section isn't found.
    """
    permalink, title = extract_metadata_from_html(html_path)
    normalized_permalink = permalink.rstrip('.html')
    parts = normalized_permalink.split('/')

    if len(parts) < 2:
        raise ValueError(f"Invalid permalink format: {permalink}")

    section_key, subsection_key = parts[0], parts[1]
    yml_path = REPO_ROOT / "_data" / f"{section_key}.yml"

    if not yml_path.exists():
        raise FileNotFoundError(f"YAML file not found: {yml_path}")

    data = yaml.safe_load(yml_path.read_text(encoding='utf-8')) or {}

    # Traverse grandparent sections safely
    for section in data.get('grandparent', []):
        if not isinstance(section, dict):
            continue  # skip malformed entries

        if section.get('url', '').strip('/') == f"{section_key}/{subsection_key}":
            children = section.get('children')
            if not isinstance(children, list):
                children = []
                section['children'] = children  # initialize if missing

            # Skip if permalink already exists (normalized)
            if any(child.get('url', '').rstrip('.html') == normalized_permalink for child in children):
                return  # silently skip

            children.append({'title': title, 'url': permalink})
            yml_path.write_text(yaml.dump(data, sort_keys=False, allow_unicode=True, width=float("inf")), encoding='utf-8')
            print(f"Updated {yml_path.name} \nTitle: {title}  \nPermalink: {permalink}")
            return

    raise ValueError(f"No matching section found for path: {section_key}/{subsection_key} in {yml_path}")


def update_set_files(gdid_map: dict, usage: dict):
    """
    Reconcile each gdid_set*.txt file with discovered usage information.

    Behavior:
      - Preserves comment lines and originally unrelated lines.
      - Collects unused GDIDs and used GDIDs with reference lists.
      - For used GDIDs that reference pages/*.html entries, attempts to update YAML navigation.
      - Writes back the file with unused entries first then used entries sorted by first usage.

    Concurrency:
      - Processes each set file concurrently using ThreadPoolExecutor.
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
    Orchestrate the full GDID reconciliation run.

    Steps:
      1. Load .gitignore patterns to exclude irrelevant paths.
      2. Load GDIDs from set files.
      3. Scan markdown, url.yml, and other repo files concurrently for usage.
      4. Merge usage maps and update set files (and YAML nav files as needed).

    Notes:
      - This function is intentionally simple: most work is delegated to helpers.
    """
    ignored = load_gitignore()
    gdid_map = load_gdids_by_file()
    all_gdids = {gid for gid_list in gdid_map.values() for gid in gid_list}

    with ThreadPoolExecutor() as executor:
        future_md = executor.submit(scan_markdown_files, all_gdids)
        future_yml = executor.submit(scan_url_yml, all_gdids)
        future_repo = executor.submit(scan_repo_files, all_gdids, ignored)

        usage_md = future_md.result()
        usage_yml = future_yml.result()
        usage_repo = future_repo.result()

    # Merge all usage maps
    usage = defaultdict(list)
    for source in [usage_md, usage_yml, usage_repo]:
        for gid, refs in source.items():
            usage[gid].extend(refs)

    update_set_files(gdid_map, usage)


if __name__ == "__main__":
    main()
