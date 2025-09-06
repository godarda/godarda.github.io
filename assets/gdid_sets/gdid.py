import re
import yaml
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict

# ------------------------------------------------------------
# Resolve repo root dynamically
# ------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
def find_repo_root(start_path):
    current = start_path
    while current != current.parent:
        if (current / ".git").exists() or (current / "index.html").exists():
            return current
        current = current.parent
    raise RuntimeError("Repo root not found")

REPO_PATH = find_repo_root(SCRIPT_PATH)
SETS_DIR = REPO_PATH / "assets" / "gdid_sets"
GITIGNORE_PATH = REPO_PATH / ".gitignore"
INVALID_PATH = SETS_DIR / "invalid.txt"
URL_YML_PATH = REPO_PATH / "_data" / "url.yml"

# ------------------------------------------------------------
# Load .gitignore entries
# ------------------------------------------------------------
def load_gitignore():
    ignored = set()
    if GITIGNORE_PATH.exists():
        for line in GITIGNORE_PATH.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                ignored.add(line.rstrip("/"))
    return ignored

# ------------------------------------------------------------
# Load GDIDs from gdid_set*.txt files
# ------------------------------------------------------------
def load_gdids_by_file():
    gdid_map = defaultdict(list)
    for txt_file in sorted(SETS_DIR.glob("gdid_set*.txt")):
        for line in txt_file.read_text(encoding='utf-8').splitlines():
            token = line.strip().split(" -")[0]
            if token.startswith("gd") and len(token) == 7 and token.isalpha():
                gdid_map[txt_file].append(token)
    return gdid_map

# ------------------------------------------------------------
# Scan markdown files for GDID usage
# ------------------------------------------------------------
def scan_markdown_files(all_gdids):
    usage = defaultdict(list)
    md_files = list(REPO_PATH.rglob("*.md"))

    def process_md(file):
        rel_path = file.relative_to(REPO_PATH).as_posix()
        found = []
        try:
            lines = file.read_text(encoding='utf-8', errors='ignore').splitlines()
            for i, line in enumerate(lines, 1):
                bracketed = re.findall(r'\[([^\]]+)\]', line)
                for token in bracketed:
                    if token.startswith("gd") and len(token) == 7 and token in all_gdids:
                        found.append((token, f"{rel_path} (line {i})"))
        except:
            pass
        return found

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_md, file) for file in md_files]
        for future in as_completed(futures):
            for gid, ref in future.result():
                usage[gid].append(ref)

    return usage

# ------------------------------------------------------------
# Scan url.yml for GDID usage
# ------------------------------------------------------------
def scan_url_yml(all_gdids):
    usage = defaultdict(list)
    if not URL_YML_PATH.exists():
        return usage

    rel_path = URL_YML_PATH.relative_to(REPO_PATH).as_posix()
    try:
        lines = URL_YML_PATH.read_text(encoding='utf-8').splitlines()
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if not line or ":" not in line:
                continue
            key = line.split(":", 1)[0].strip()
            if key.startswith("gd") and len(key) == 7 and key.isalpha() and key in all_gdids:
                usage[key].append(f"{rel_path} (line {i})")
    except Exception as e:
        print(f"Failed to read {rel_path}: {e}")

    return usage

# ------------------------------------------------------------
# Scan all other repo files for GDID usage and nonstandard filenames
# ------------------------------------------------------------
def scan_repo_files(all_gdids, ignored):
    usage = defaultdict(list)
    nonstandard_ids = []

    files = [f for f in REPO_PATH.rglob("*") if f.is_file() and not f.name.endswith(".md") and f.name != "url.yml"]

    def process_file(file):
        rel_path = file.relative_to(REPO_PATH).as_posix()
        if ".git" in rel_path or any(part in ignored for part in Path(rel_path).parts):
            return [], None

        found = []
        local_nonstandard = None
        name = Path(rel_path).name
        stem = Path(rel_path).stem.strip()

        # Check filenames
        candidates = [word for word in re.findall(r'\b[a-z]{7}\b', name) if word.startswith('gd')]
        for word in candidates:
            if word in all_gdids:
                found.append((word, rel_path))

        # Detect nonstandard filenames in pages/
        if "pages" in rel_path and name != "index.html":
            if not stem.startswith("gd") or len(stem) != 7:
                local_nonstandard = f"{stem},{rel_path}"

        return found, local_nonstandard

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_file, file) for file in files]
        for future in as_completed(futures):
            found, nonstandard = future.result()
            for gid, ref in found:
                usage[gid].append(ref)
            if nonstandard:
                nonstandard_ids.append(nonstandard)

    INVALID_PATH.write_text(
        '\n'.join(nonstandard_ids) if nonstandard_ids else "No non-standard IDs found during scan.",
        encoding='utf-8'
    )

    return usage

# ------------------------------------------------------------
# Update gdid_set*.txt files with usage info
# ------------------------------------------------------------
def update_set_files(gdid_map, usage):
    def process_file(txt_file, gdids):
        original_lines = txt_file.read_text(encoding='utf-8').splitlines()
        comments, unused, used_entries = [], [], []
        seen = set()

        for line in original_lines:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                comments.append(line)
                continue

            token = stripped.split(" -")[0].strip()
            seen.add(token)

            if token in gdids:
                refs = usage.get(token, [])
                if refs:
                    usage_str = '; '.join(sorted(refs))
                    used_entries.append((token, usage_str))
                else:
                    unused.append(token)
            else:
                comments.append(line)

        # Include GDIDs not originally listed
        for token in gdids:
            if token not in seen:
                refs = usage.get(token, [])
                if refs:
                    usage_str = '; '.join(sorted(refs))
                    used_entries.append((token, usage_str))
                else:
                    unused.append(token)

        # Sort used GDIDs by first usage path and line number
        def sort_key(item):
            first_usage = item[1].split(';')[0].strip()
            match = re.match(r'(.+?) \(line (\d+)\)', first_usage)
            if match:
                path, line = match.groups()
                return (path.lower(), int(line))
            return (first_usage.lower(), 0)

        sorted_used = sorted(used_entries, key=sort_key)
        used_lines = [f"{gid} - {refs}" for gid, refs in sorted_used]
        updated_lines = comments + unused + used_lines

        txt_file.write_text('\n'.join(updated_lines), encoding='utf-8')

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(process_file, txt_file, gdids)
            for txt_file, gdids in gdid_map.items()
        ]
        for future in as_completed(futures):
            future.result()

# ------------------------------------------------------------
# Main execution flow
# ------------------------------------------------------------
def main():
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