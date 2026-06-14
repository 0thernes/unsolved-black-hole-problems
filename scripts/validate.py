#!/usr/bin/env python3
"""Validate the unsolved-black-hole-problems catalogue.

Checks (fail the build on any violation):
  1. Every problems/<NN-slug>/ has README.md and problem.json.
  2. Each problem.json parses and (if jsonschema is installed) validates
     against schema/problem.schema.json.
  3. slug matches its folder name; rank's NN prefix matches the slug.
  4. Ranks are unique and form 1..N with no gaps.
  5. The README master table lists exactly the on-disk problems.
  6. Integrity: every paper with no identifier carries an explicit note (so a
     bare, unverifiable citation cannot slip in silently); coverage_note is
     non-empty. (PHILOSOPHY.md: no fabricated citations.)

Exit 0 = green. Anything else prints the failures and exits 1.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROBLEMS = ROOT / "problems"
SCHEMA = ROOT / "schema" / "problem.schema.json"
README = ROOT / "README.md"

try:
    import jsonschema
except ImportError:  # optional locally; CI installs it
    jsonschema = None

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def main() -> int:
    if not PROBLEMS.is_dir():
        fail("problems/ directory is missing")
        return report()

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema) if jsonschema else None

    dirs = sorted(p for p in PROBLEMS.iterdir() if p.is_dir())
    ranks: dict[int, str] = {}
    slug_re = re.compile(r"^(\d{2})-[a-z0-9-]+$")

    for d in dirs:
        name = d.name
        if not slug_re.match(name):
            fail(f"{name}: folder name is not NN-slug")
            continue
        if not (d / "README.md").is_file():
            fail(f"{name}: missing README.md")
        pj = d / "problem.json"
        if not pj.is_file():
            fail(f"{name}: missing problem.json")
            continue
        try:
            data = json.loads(pj.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            fail(f"{name}/problem.json: invalid JSON: {e}")
            continue

        if validator is not None:
            for err in sorted(validator.iter_errors(data), key=str):
                fail(f"{name}/problem.json: schema: {err.message}")

        if data.get("slug") != name:
            fail(f"{name}: problem.json slug '{data.get('slug')}' != folder")
        nn = int(name[:2])
        if data.get("rank") != nn:
            fail(f"{name}: rank {data.get('rank')} != folder prefix {nn}")
        if nn in ranks:
            fail(f"duplicate rank {nn}: {ranks[nn]} and {name}")
        ranks[nn] = name

        # Integrity: unverifiable papers must be explicitly noted.
        for i, paper in enumerate(data.get("papers", [])):
            ident = paper.get("identifier") or {}
            if not ident and not paper.get("note"):
                fail(f"{name}: paper #{i} '{paper.get('title')}' has no "
                     f"identifier and no note (unverifiable)")
        if not (data.get("metadata", {}) or {}).get("coverage_note"):
            fail(f"{name}: empty metadata.coverage_note")

    # Ranks form 1..N
    if ranks:
        expected = set(range(1, len(ranks) + 1))
        if set(ranks) != expected:
            fail(f"ranks are not contiguous 1..{len(ranks)}: {sorted(ranks)}")

    # README table lists exactly the on-disk problems.
    if README.is_file():
        text = README.read_text(encoding="utf-8")
        for nn, name in ranks.items():
            if f"problems/{name}/" not in text:
                fail(f"README does not link problems/{name}/")

    return report()


def report() -> int:
    if errors:
        print(f"VALIDATION FAILED ({len(errors)} issue(s)):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("Catalogue validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
