import re
import csv
from pathlib import Path


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
    usage = {gid: [] for gid in valid_ids}
    return valid_ids, usage

# Scan repository for GDID usage and nonstandard IDs
def scan_repository(valid_ids, usage, ignored):
    nonstandard_ids = []

    for file in REPO_PATH.rglob("*"):
        rel_path = file.relative_to(REPO_PATH)

        # Skip excluded files and folders
        if rel_path == Path("assets/gdid.csv") or ".git" in rel_path.parts:
            continue
        if not file.is_file() or any(part in ignored for part in rel_path.parts):
            continue

        name = file.name
        stem = file.stem.strip()

        # Track valid GDIDs in filenames
        candidates = [word for word in re.findall(r'\b[a-z]{7}\b', name) if word.startswith('gd')]
        for word in candidates:
            if word in usage:
                usage[word].append(str(rel_path))

        # Detect nonstandard IDs in pages/ directory
        if "pages" in rel_path.parts and name != "index.html":
            if not stem.startswith("gd") or len(stem) != 7:
                nonstandard_ids.append(f"{stem},{rel_path}")

        # Scan Markdown content for bracketed GDID references
        if file.suffix == ".md":
            try:
                lines = file.read_text(encoding='utf-8', errors='ignore').splitlines()
                for i, line in enumerate(lines, 1):
                    bracketed = re.findall(r'\[([^\]]+)\]', line)
                    for token in bracketed:
                        if token.startswith("gd") and len(token) == 7 and token in usage:
                            usage[token].append(f"{rel_path} (line {i})")
            except:
                continue  # Gracefully skip unreadable files

    return nonstandard_ids

# Write updated GDID usage and nonstandard entries to CSV
def write_csv(unused, used, nonstandard_ids):
    with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for gid in unused:
            writer.writerow([gid])
        for gid in used:
            writer.writerow([gid, '; '.join(used[gid])])
        if nonstandard_ids:
            f.write("\n" + "-"*100 + "\n")
            f.write("# Nonstandard IDs found in pages (which are not in gdid.csv):")
            f.write("\n" + "-"*100 + "\n")
            for bad in nonstandard_ids:
                f.write(bad + "\n")


def main():
    ignored = load_gitignore()
    original_ids, usage = load_gdids_and_init_usage()
    nonstandard_ids = scan_repository(original_ids, usage, ignored)

    unused = [gid for gid in original_ids if not usage[gid]]
    used = {gid: usage[gid] for gid in original_ids if usage[gid]}

    write_csv(unused, used, nonstandard_ids)

if __name__ == "__main__":
    main()