# Kanban — research-ops board

Workflow for growing and maintaining the catalogue. Cards move
**Backlog → Researching → Drafted → Validated → Done**; integrity review is a
required gate before Done.

## Done

- [x] Repo scaffold: README master list, PHILOSOPHY, ARCHITECTURE, ERD, schema,
      validate.py, build_rag.py, CI, LICENSE.
- [x] 16 problems seeded with statements, originators, history, key ideas,
      status, and ranking rationale (from established domain knowledge).
- [x] All 16 `problem.json` pass schema + structural validation; `rag/INDEX.jsonl`
      built and drift-checked in CI.
- [x] Enrichment pass complete: every problem has 24–30 verified, sourced papers
      (foundational + recent) and 10–11 physicists with contributions; all
      `metadata.confidence: "researched"`. Integrity gate enforced on apply
      (identifier-or-note required, else dropped). RAG rebuilt to 584 records.

## Researching

- (none — enrichment pass complete; reopen per problem as new results land)

## Backlog

- [ ] Cross-link `simulator_angle` fields to concrete `black-hole-simulation-lab`
      features (e.g. #11 no-hair tests ↔ QNM spectroscopy module).
- [ ] Daily research feed (mirror the simulator's scheduled pull) appending new
      arXiv items to a per-problem `recent` list.
- [ ] Consider additional problems if genuinely distinct (e.g. holographic
      complexity growth; islands in cosmology) — only if not a duplicate.

## Ranking disputes log

Ranking is editorial (see PHILOSOPHY.md §4). Record any reorder here with reason.

- 2026-06-14 — initial ordering: fundamental/quantum-gravity problems (#01–#10)
  above observational/astrophysical ones (#11–#16). #03 (entropy microstates)
  placed below #02 because special (SUSY/extremal) cases are solved.
