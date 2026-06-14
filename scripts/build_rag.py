#!/usr/bin/env python3
"""Assemble the RAG corpus rag/INDEX.jsonl from every problems/*/problem.json.

Emits one retrieval record per *problem*, plus one per *paper* and per
*physicist*, each carrying a `text` field (what an embedder indexes) and
`metadata` (provenance + truth tier). Deterministic: stable ordering, no
timestamps in the output, so re-runs are diff-clean.

Run after editing any problem.json:  python scripts/build_rag.py
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROBLEMS = ROOT / "problems"
OUT = ROOT / "rag" / "INDEX.jsonl"


def records():
    for d in sorted(p for p in PROBLEMS.iterdir() if p.is_dir()):
        pj = d / "problem.json"
        if not pj.is_file():
            continue
        p = json.loads(pj.read_text(encoding="utf-8"))
        rank = p.get("rank")
        slug = p.get("slug")
        origin = ", ".join(o["name"] for o in p.get("originators", []))

        # Problem record.
        yield {
            "id": f"problem:{slug}",
            "type": "problem",
            "rank": rank,
            "title": p.get("title"),
            "text": (
                f"Unsolved black-hole problem #{rank}: {p.get('title')}. "
                f"{p.get('statement')} First posed {p.get('first_posed')} by "
                f"{origin}. Status: {p.get('status')}. "
                f"Key ideas: {'; '.join(p.get('key_ideas', []))}."
            ),
            "metadata": {
                "slug": slug,
                "status": p.get("status"),
                "statement_tier": p.get("statement_tier"),
                "resolution_tier": p.get("resolution_tier"),
                "related_problems": p.get("related_problems", []),
            },
        }

        # Paper records.
        for i, pa in enumerate(p.get("papers", [])):
            ident = pa.get("identifier") or {}
            ref = ident.get("arxiv") or ident.get("doi") or ident.get("url") or pa.get("note", "")
            yield {
                "id": f"paper:{slug}:{i}",
                "type": "paper",
                "rank": rank,
                "title": pa.get("title"),
                "text": (
                    f"{pa.get('title')} ({pa.get('year')}) by "
                    f"{', '.join(pa.get('authors', []))} — {pa.get('kind')} "
                    f"reference for black-hole problem #{rank} "
                    f"({p.get('title')}). {ref}"
                ),
                "metadata": {
                    "problem_slug": slug,
                    "year": pa.get("year"),
                    "kind": pa.get("kind"),
                    "tier": pa.get("tier"),
                    "identifier": ident,
                },
            }

        # Physicist records.
        for i, ph in enumerate(p.get("physicists", [])):
            yield {
                "id": f"physicist:{slug}:{i}",
                "type": "physicist",
                "rank": rank,
                "title": ph.get("name"),
                "text": (
                    f"{ph.get('name')} ({ph.get('role')}) — {ph.get('contribution', '')} "
                    f"Connected to black-hole problem #{rank} ({p.get('title')})."
                ),
                "metadata": {
                    "problem_slug": slug,
                    "role": ph.get("role"),
                    "era": ph.get("era"),
                    "affiliation": ph.get("affiliation"),
                },
            }


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    recs = list(records())
    with OUT.open("w", encoding="utf-8", newline="\n") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
    print(f"Wrote {len(recs)} RAG records to {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
