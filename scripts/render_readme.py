#!/usr/bin/env python3
"""Generate a thorough README.md for each problem from its problem.json.

problem.json is the source of truth; this renders a consistent narrative page
from it. By default it only writes a README where one does NOT already exist, so
hand-authored narrative READMEs (e.g. the deepest problems #01-#04) are
preserved. Pass --force to regenerate all.

Usage:
  python scripts/render_readme.py            # fill in missing READMEs
  python scripts/render_readme.py --force    # regenerate every README
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROBLEMS = ROOT / "problems"


def fmt_paper(p: dict) -> str:
    ident = p.get("identifier") or {}
    ref = ""
    if ident.get("arxiv"):
        ref = f"`arXiv:{ident['arxiv']}`"
    elif ident.get("doi"):
        ref = f"doi:{ident['doi']}"
    elif ident.get("url"):
        ref = ident["url"]
    note = p.get("note", "")
    tail = " — ".join(x for x in [ref, note] if x)
    tier = p.get("tier", "")
    authors = ", ".join(p.get("authors", []))
    line = (f"- **{p.get('title')}** ({p.get('year')}) — {authors}. "
            f"_{p.get('kind')}_" + (f", `{tier}`" if tier else ""))
    if tail:
        line += f". {tail}"
    return line


def render(d: dict) -> str:
    out: list[str] = []
    out.append(f"# #{d['rank']:02d} — {d['title']}\n")
    aliases = d.get("aliases") or []
    if aliases:
        out.append(f"*Also known as: {', '.join(aliases)}.*\n")
    out.append(
        f"> **Status: {d['status'].replace('-', ' ').upper()}** · "
        f"Statement tier: `{d['statement_tier']}` · "
        f"Resolution tier: `{d['resolution_tier']}` · "
        f"First posed: {d['first_posed']}.\n"
    )
    out.append("## The problem\n")
    out.append(d["statement"] + "\n")

    out.append("## History & originators\n")
    for o in d.get("originators", []):
        note = f" — {o['note']}" if o.get("note") else ""
        out.append(f"- **{o['name']}**{note}")
    out.append("")

    r = d["ranking"]
    out.append(f"## Why it ranks #{d['rank']:02d}\n")
    out.append(
        f"{r['rationale']}\n\n"
        f"*(depth {r['depth']}/10 · age {r['age']}/10 · "
        f"tractability {r['tractability']}/10 — higher tractability pushes the "
        f"rank toward the bottom of the list.)*\n"
    )

    out.append("## Key ideas\n")
    for k in d.get("key_ideas", []):
        out.append(f"- {k}")
    out.append("")

    approaches = d.get("approaches") or []
    if approaches:
        out.append("## Live approaches\n")
        for a in approaches:
            props = a.get("proponents") or []
            ptail = f" _Proponents: {', '.join(props)}._" if props else ""
            out.append(f"- **{a['name']}** (`{a['tier']}`) — {a['summary']}{ptail}")
        out.append("")

    out.append("## Key papers\n")
    out.append("*Real, verifiable references (see PHILOSOPHY.md: no fabricated "
               "citations). This is a curated seed; coverage is noted below.*\n")
    for p in d.get("papers", []):
        out.append(fmt_paper(p))
    out.append("")

    out.append("## Key physicists\n")
    for ph in d.get("physicists", []):
        bits = [ph.get("role"), ph.get("era"), ph.get("affiliation")]
        meta = ", ".join(x for x in bits if x)
        contrib = f" — {ph['contribution']}" if ph.get("contribution") else ""
        out.append(f"- **{ph['name']}** ({meta}){contrib}")
    out.append("")

    if d.get("simulator_angle"):
        out.append("## Connection to the simulator\n")
        out.append(d["simulator_angle"] + "\n")

    rel = d.get("related_problems") or []
    if rel:
        out.append("## Related problems\n")
        out.append(", ".join(f"#{x:02d}" for x in sorted(rel)) + "\n")

    out.append("---\n")
    out.append(
        f"*Coverage: {d['metadata'].get('coverage_note', '')}*\n\n"
        f"*This page is generated from `problem.json` by "
        f"`scripts/render_readme.py` (the structured file is the source of "
        f"truth). Last updated {d['metadata'].get('updated', '')}.*"
    )
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    force = "--force" in argv
    written = 0
    for d in sorted(p for p in PROBLEMS.iterdir() if p.is_dir()):
        pj = d / "problem.json"
        if not pj.is_file():
            continue
        readme = d / "README.md"
        if readme.exists() and not force:
            continue
        data = json.loads(pj.read_text(encoding="utf-8"))
        readme.write_text(render(data), encoding="utf-8", newline="\n")
        written += 1
        print(f"rendered {readme.relative_to(ROOT)}")
    print(f"Wrote {written} README(s){' (forced)' if force else ' (missing only)'}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
