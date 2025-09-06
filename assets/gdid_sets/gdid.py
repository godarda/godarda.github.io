import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict

# ------------------------------------------------------------
# Resolve repo root dynamically, regardless of execution path
# ------------------------------------------------------------
def find_repo_root(start_path):
    current = start_path
    while current != current.parent:
        if (current / ".git").exists() or (current / "index.html").exists():
            return current
        current = current.parent
    raise RuntimeError("Repo root not found")

SCRIPT_PATH = Path(__file__).resolve()
REPO_PATH = find_repo_root(SCRIPT_PATH)
SETS_DIR = REPO_PATH / "assets" / "gdid_sets"
GITIGNORE_PATH = REPO_PATH / ".gitignore"
INVALID_PATH = SETS_DIR / "invalid.txt"

# ------------------------------------------------------------
# Load .gitignore entries to exclude ignored paths
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
# Load GDIDs from all gdid_set*.txt files
# Returns: {Path: [gdids]}
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
# Concurrently scan repo for GDID usage and nonstandard filenames
# Writes invalid.txt directly from here
# Returns: {gdid: [usage paths]}
# ------------------------------------------------------------
def scan_repository(all_gdids, ignored):
    usage = defaultdict(list)
    nonstandard_ids = []
    files = [f for f in REPO_PATH.rglob("*") if f.is_file()]

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

        # Check markdown content
        if rel_path.endswith(".md"):
            try:
                lines = file.read_text(encoding='utf-8', errors='ignore').splitlines()
                for i, line in enumerate(lines, 1):
                    bracketed = re.findall(r'\[([^\]]+)\]', line)
                    for token in bracketed:
                        if token.startswith("gd") and len(token) == 7 and token in all_gdids:
                            found.append((token, f"{rel_path} (line {i})"))
            except:
                pass

        return found, local_nonstandard

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_file, file) for file in files]
        for future in as_completed(futures):
            found, nonstandard = future.result()
            for gid, ref in found:
                usage[gid].append(ref)
            if nonstandard:
                nonstandard_ids.append(nonstandard)

    # Write invalid.txt directly from here
    if nonstandard_ids:
        INVALID_PATH.write_text('\n'.join(nonstandard_ids), encoding='utf-8')
    else:
        INVALID_PATH.write_text("No non-standard IDs found during scan.", encoding='utf-8')

    return usage

# ------------------------------------------------------------
# Concurrently update each gdid_setX.txt file with usage info
# Format: unused GDIDs at top, used GDIDs at bottom (sorted by first usage path)
# ------------------------------------------------------------
def update_set_files(gdid_map, usage):
    def process_file(txt_file, gdids):
        original_lines = txt_file.read_text(encoding='utf-8').splitlines()
        comments, unused, used_entries = [], [], []

        for line in original_lines:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                comments.append(line)
                continue

            token = stripped.split(" -")[0]
            if token in gdids:
                refs = usage.get(token, [])
                if refs:
                    usage_str = '; '.join(sorted(refs))
                    used_entries.append((token, usage_str))
                else:
                    unused.append(token)
            else:
                comments.append(line)

        sorted_used = sorted(used_entries, key=lambda item: item[1].split(';')[0])
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
    usage = scan_repository(all_gdids, ignored)
    update_set_files(gdid_map, usage)

if __name__ == "__main__":
    main()