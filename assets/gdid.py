import re
import csv
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict

# This script scans the repository for valid GDID usage in filenames and Markdown content,
# identifies nonstandard IDs in the pages/ directory, and updates gdid.csv with usage details.
# It respects .gitignore entries and is optimized for clarity and contributor onboarding.

SCRIPT_PATH = Path(__file__).resolve()
REPO_PATH = SCRIPT_PATH.parents[1]
CSV_PATH = SCRIPT_PATH.parent / "gdid.csv"
GITIGNORE_PATH = REPO_PATH / ".gitignore"

# Load .gitignore entries to exclude ignored paths
def load_gitignore():
    ignored = set()
    if GITIGNORE_PATH.exists():
        for line in GITIGNORE_PATH.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                ignored.add(line.rstrip("/"))
    return ignored

# Load GDIDs from CSV and initialize usage map
def load_gdids_and_init_usage():
    with open(CSV_PATH, newline='', encoding='utf-8') as f:
        valid_ids = [row[0].strip() for row in csv.reader(f) if row and row[0].startswith("gd") and len(row[0]) == 7]
    usage = defaultdict(list)
    return valid_ids, usage

# Concurrent file scanning for GDID usage and nonstandard IDs
def scan_repository(valid_ids, usage, ignored):
    files = [f for f in REPO_PATH.rglob("*") if f.is_file()]
    nonstandard_ids = []

    def process_file(file):
        rel_path = file.relative_to(REPO_PATH)

        if rel_path == Path("assets/gdid.csv") or ".git" in rel_path.parts:
            return [], None
        if any(part in ignored for part in rel_path.parts):
            return [], None

        local_usage = []
        local_nonstandard = None

        name = file.name
        stem = file.stem.strip()

        # Track valid GDIDs in filenames
        candidates = [word for word in re.findall(r'\b[a-z]{7}\b', name) if word.startswith('gd')]
        for word in candidates:
            if word in valid_ids:
                local_usage.append((word, str(rel_path)))

        # Detect nonstandard IDs in pages/ directory
        if "pages" in rel_path.parts and name != "index.html":
            if not stem.startswith("gd") or len(stem) != 7:
                local_nonstandard = f"{stem},{rel_path}"

        # Scan Markdown content for bracketed GDID references
        if file.suffix == ".md":
            try:
                lines = file.read_text(encoding='utf-8', errors='ignore').splitlines()
                for i, line in enumerate(lines, 1):
                    bracketed = re.findall(r'\[([^\]]+)\]', line)
                    for token in bracketed:
                        if token.startswith("gd") and len(token) == 7 and token in valid_ids:
                            local_usage.append((token, f"{rel_path} (line {i})"))
            except:
                pass

        return local_usage, local_nonstandard

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_file, file) for file in files]
        for future in as_completed(futures):
            local_usage, local_nonstandard = future.result()
            for gid, ref in local_usage:
                usage[gid].append(ref)
            if local_nonstandard:
                nonstandard_ids.append(local_nonstandard)

    return nonstandard_ids

# Write updated GDID usage and nonstandard entries to CSV
def write_csv(unused, used, nonstandard_ids):
    with open(CSV_PATH, 'w', encoding='utf-8') as f:
        for gid in unused:
            f.write(f"{gid}\n")  # Write unused GDID with trailing newline
        for gid in used:
            usage_str = '; '.join(used[gid])
            f.write(f"{gid} - {usage_str}\n")  # Write used GDID with usage string
        if nonstandard_ids:
            f.write("\n" + "-"*100 + "\n")
            f.write("# Nonstandard IDs found in pages (which are not in gdid.csv):\n")
            f.write("-"*100 + "\n")
            for bad in nonstandard_ids:
                f.write(bad + "\n")

# Main execution flow
def main():
    ignored = load_gitignore()
    original_ids, usage = load_gdids_and_init_usage()
    nonstandard_ids = scan_repository(original_ids, usage, ignored)

    # Sort usage references alphabetically for each GDID
    for gid in usage:
        usage[gid].sort()

    unused = [gid for gid in original_ids if not usage[gid]]
    used = {gid: usage[gid] for gid in original_ids if usage[gid]}

    # Sort used GDIDs by their first usage reference
    sorted_used = dict(sorted(used.items(), key=lambda item: item[1][0]))

    write_csv(unused, sorted_used, nonstandard_ids)

if __name__ == "__main__":
    main()