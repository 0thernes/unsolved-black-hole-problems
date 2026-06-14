# Changelog

## 2026-06-14 — All 16 problems populated + RAG + moved to Z: dev drive

- Completed all 16 problem entries: each `problems/NN-slug/` now has a full
  `problem.json` (schema-validated) and a `README.md`. #01-#04 have hand-authored
  narrative articles; #05-#16 are rendered from `problem.json` by the new
  `scripts/render_readme.py` (source-of-truth → narrative, like the RAG build).
- Added `scripts/render_readme.py` (`--force` regenerates all; default fills
  only missing READMEs, preserving hand-authored ones).
- Rebuilt `rag/INDEX.jsonl`: **198 records** (16 problems + ~90 papers +
  ~90 physicists), each truth-tier-tagged. Validation green.
- Citations are real (arXiv/DOI/bibliographic notes); paper/physicist lists are
  honestly marked as curated seeds (the "25 papers / 10 physicists each"
  aspiration is recorded per problem, slated for sourced enrichment).
- Repository relocated from a temporary C: workspace to the Z: ReFS dev drive
  (`Z:\[Vibe Coded (AI)]\CLAUDECODE\Unsolved Black Hole Problems`), a sibling of
  the simulator and the math-problems catalogue.

## 2026-06-14 — Repository created

- Scaffolded the unsolved-black-hole-problems catalogue: README master ranked
  list, PHILOSOPHY (epistemic charter + truth tiers), ARCHITECTURE, schema/ERD,
  `validate.py`, `build_rag.py`, GitHub Actions CI, KANBAN, proprietary LICENSE.
- Seeded 16 major open problems (#01 spacetime singularities → #16 mass gaps),
  each with a precise statement, originator(s), first-posed date, history, key
  ideas, ranking rationale, status, and an honest `seed` coverage note.
- Generated the initial RAG corpus `rag/INDEX.jsonl` (problem / paper /
  physicist records, truth-tier-tagged).
- Honesty stance fixed from the start: catalogue-only, no fabricated citations,
  no claims of solving open problems. Private repo (not published).
