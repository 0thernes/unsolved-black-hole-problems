#!/usr/bin/env python3
"""Merge an enrichment payload into the problem.json files.

The enrichment workflow returns, per problem, an expanded {slug, papers,
physicists, coverage_note}. This script reads that payload (a JSON array) and,
for each entry, REPLACES the papers[] and physicists[] of the matching
problems/<slug>/problem.json, refreshes metadata (coverage_note, confidence ->
'researched', updated date), and writes it back. It validates that the new
lists are non-empty and that every paper is verifiable (has an identifier or a
note) BEFORE writing — an unverifiable citation is dropped with a warning, never
silently kept (PHILOSOPHY.md: no fabricated citations).

Usage:  python scripts/apply_enrichment.py <payload.json> [--updated YYYY-MM-DD]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROBLEMS = ROOT / "problems"


def verifiable(paper: dict) -> bool:
    ident = paper.get("identifier") or {}
    return bool(ident.get("arxiv") or ident.get("doi") or ident.get("url")
                or paper.get("note"))


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: apply_enrichment.py <payload.json> [--updated DATE]")
        return 2
    payload_path = Path(argv[0])
    updated = "2026-06-14"
    if "--updated" in argv:
        updated = argv[argv.index("--updated") + 1]

    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    if isinstance(payload, dict) and "results" in payload:
        payload = payload["results"]

    applied = 0
    for entry in payload:
        slug = entry.get("slug")
        if not slug:
            continue
        pj = PROBLEMS / slug / "problem.json"
        if not pj.is_file():
            print(f"  SKIP {slug}: no problem.json")
            continue
        data = json.loads(pj.read_text(encoding="utf-8"))

        papers = entry.get("papers") or []
        kept = [p for p in papers if verifiable(p)]
        dropped = len(papers) - len(kept)
        physicists = entry.get("physicists") or []

        if not kept:
            print(f"  SKIP {slug}: no verifiable papers in payload (keeping seed)")
            continue

        data["papers"] = kept
        if physicists:
            data["physicists"] = physicists
        md = data.setdefault("metadata", {})
        md["coverage_note"] = entry.get("coverage_note") or md.get("coverage_note", "")
        md["confidence"] = "researched"
        md["updated"] = updated
        # keep created as-is
        pj.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8", newline="\n")
        note = f" ({dropped} unverifiable dropped)" if dropped else ""
        print(f"  {slug}: {len(kept)} papers, {len(physicists) or len(data.get('physicists', []))} physicists{note}")
        applied += 1

    print(f"Applied enrichment to {applied} problem(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
