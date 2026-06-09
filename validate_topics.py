import json
import re
import sys
from collections import Counter

path = "config/topics.json"
errors = []
warnings = []

with open(path, encoding="utf-8") as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        sys.exit(1)

if not isinstance(data, list):
    errors.append("Root must be a JSON array")

names = []
topic_pattern = re.compile(r"^[a-z0-9][a-z0-9-]*$")

for i, entry in enumerate(data):
    if not isinstance(entry, dict):
        errors.append(f"Entry {i}: must be an object")
        continue
    if "repositoryName" not in entry:
        errors.append(f"Entry {i}: missing repositoryName")
        continue
    name = entry["repositoryName"]
    if not isinstance(name, str) or not name.strip():
        errors.append(f"Entry {i}: invalid repositoryName")
    elif "," in name:
        errors.append(f"Entry {i}: repositoryName contains comma: {name!r}")
    names.append(name)

    topics = entry.get("repositoryTopics")
    if topics is None:
        errors.append(f"Entry {i} ({name}): missing repositoryTopics")
        continue
    if not isinstance(topics, list) or len(topics) == 0:
        warnings.append(f"{name}: empty or invalid repositoryTopics")
        continue
    for j, t in enumerate(topics):
        if not isinstance(t, dict) or "name" not in t:
            errors.append(f"{name}: topic {j} missing name field")
            continue
        tname = t["name"]
        if not isinstance(tname, str) or not tname.strip():
            errors.append(f"{name}: topic {j} has empty name")
        elif not topic_pattern.match(tname):
            errors.append(
                f"{name}: invalid topic name {tname!r} (GitHub: lowercase alphanumeric + hyphens)"
            )

counts = Counter(names)
dups = [n for n, c in counts.items() if c > 1]
for n in sorted(dups):
    errors.append(f"Duplicate repositoryName: {n!r} ({counts[n]} times)")

topic_names = {
    t["name"]
    for e in data
    if isinstance(e, dict) and isinstance(e.get("repositoryTopics"), list)
    for t in e["repositoryTopics"]
    if isinstance(t, dict) and "name" in t
}

print(f"Entries: {len(data)}")
print(f"Unique repositories: {len(set(names))}")
print(f"Distinct topic names: {len(topic_names)}")

if warnings:
    print(f"\nWarnings ({len(warnings)}):")
    for w in warnings:
        print(f"  - {w}")

if errors:
    print(f"\nErrors ({len(errors)}):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print("\nValidation passed: valid JSON and all checks OK")
if warnings:
    print(f"({len(warnings)} warning(s))")
