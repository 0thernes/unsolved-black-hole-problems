# Kanban — research-ops board

Workflow for growing and maintaining the catalogue. Cards move
**Backlog → Researching → Drafted → Validated → Done**; integrity review is a
required gate before Done.

## Done

- [x] Repo scaffold: README master list, PHILOSOPHY, ARCHITECTURE, ERD, schema,
      validate.py, build_rag.py, CI, LICENSE.
- [x] 16 problems seeded with statements, originators, history, key ideas,
      status, and ranking rationale (from established domain knowledge).

## Validated (schema + CI green, seed coverage)

- [ ] All 16 `problem.json` pass schema + structural validation.
- [ ] `rag/INDEX.jsonl` built and drift-checked.

## Researching (enrichment pass — real, sourced citations)

- [ ] Per-problem: gather verified key papers (target up to 25: foundational +
      recent) via arXiv / Consensus / Semantic Scholar.
- [ ] Per-problem: top ~10 active/historical physicists with contributions.
- [ ] Upgrade `metadata.confidence` from `seed` → `researched` as coverage lands.

## Backlog

- [ ] Cross-link `simulator_angle` fields to concrete `black-hole-simulation-lab`
      features (e.g. #11 no-hair tests ↔ QNM spectroscopy module).
- [ ] Add `docs/audits/` entry once enrichment completes.
- [ ] Consider additional problems if genuinely distinct (e.g. holographic
      complexity growth; islands in cosmology) — only if not a duplicate.
- [ ] Daily research feed (mirror the simulator's scheduled pull) appending new
      arXiv items to a per-problem `recent` list.

## Ranking disputes log

Ranking is editorial (see PHILOSOPHY.md §4). Record any reorder here with reason.

- 2026-06-14 — initial ordering: fundamental/quantum-gravity problems (#01–#10)
  above observational/astrophysical ones (#11–#16). #03 (entropy microstates)
  placed below #02 because special (SUSY/extremal) cases are solved.
