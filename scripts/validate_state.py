#!/usr/bin/env python3
"""
Lightweight state validator.

Checks:
- YAML files are parseable
- IDs are unique inside each state file
- common counters are non-negative
- known lifecycle statuses are valid

Optional dependency:
    pip install pyyaml
"""

from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install it with: pip install pyyaml")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "state"

STATUS = {
    "errors.yaml": {"candidate", "active", "improving", "mastered"},
    "vocabulary.yaml": {"new", "learning", "active", "stable", "mastered"},
    "structures.yaml": {"introduced", "practicing", "improving", "stable", "mastered"},
}

COLLECTION = {
    "errors.yaml": "errors",
    "vocabulary.yaml": "vocabulary",
    "structures.yaml": "structures",
}

def fail(message):
    print(f"ERROR: {message}")
    return 1

def validate_collection(path):
    errors = 0
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    key = COLLECTION[path.name]
    items = data.get(key, [])
    ids = set()

    for item in items:
        item_id = item.get("id")
        if not item_id:
            errors += fail(f"{path.name}: item without id")
            continue

        if item_id in ids:
            errors += fail(f"{path.name}: duplicate id '{item_id}'")
        ids.add(item_id)

        status = item.get("status")
        if status not in STATUS[path.name]:
            errors += fail(
                f"{path.name}: invalid status '{status}' for '{item_id}'"
            )

        for counter in ("occurrences", "successful_uses", "encounters", "attempts"):
            if counter in item:
                value = item[counter]
                if not isinstance(value, int) or value < 0:
                    errors += fail(
                        f"{path.name}: '{item_id}' has invalid {counter}: {value}"
                    )

    return errors

def main():
    errors = 0

    for filename in COLLECTION:
        path = STATE / filename
        if not path.exists():
            errors += fail(f"missing file: {path}")
            continue
        try:
            errors += validate_collection(path)
        except Exception as exc:
            errors += fail(f"{filename}: {exc}")

    for yaml_file in STATE.glob("*.yaml"):
        try:
            with yaml_file.open("r", encoding="utf-8") as f:
                yaml.safe_load(f)
        except Exception as exc:
            errors += fail(f"{yaml_file.name}: YAML parse error: {exc}")

    if errors:
        print(f"\nValidation failed with {errors} error(s).")
        return 1

    print("State validation passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
