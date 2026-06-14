# Project Log

Dated operational log. Human-readable narrative of what happened and why
(CHANGELOG.md is the terse, release-style summary).

## 2026-06-14

- **Created** the `unsolved-black-hole-problems` catalogue as a **private**
  GitHub repo (per the standing "don't publish without OK" rule) with branch
  `main`. Cloned and built it; established the scaffold (README master ranked
  list, PHILOSOPHY, ARCHITECTURE, ERD, JSON schema, `validate.py`,
  `build_rag.py`, GitHub Actions CI, KANBAN, proprietary LICENSE/NOTICE).
- **Authored all 16 problems** from established domain knowledge. Decision:
  hand-author rather than rely on the multi-agent research workflow, which hit a
  transient server rate-limit on two attempts (a fleet-wide throttle, not a
  usage cap). Hand-authoring is the reliable, integrity-controlled path; the
  workflow remains the route for citation *enrichment* later. #01–#04 got
  hand-written narrative READMEs; #05–#16 are rendered from `problem.json` by
  `scripts/render_readme.py` (single source of truth → narrative).
- **RAG** `rag/INDEX.jsonl` built: 198 records (16 problems + ~90 papers +
  ~90 physicists), truth-tier-tagged. Validation + CI green throughout.
- **Relocation to the Z: dev drive.** The repo was initially built in a
  temporary `C:\bhwork` workspace (a workaround while Z: project locations were
  churning mid-session). On user instruction this was corrected: the repo was
  moved to `Z:\[Vibe Coded (AI)]\CLAUDECODE\Unsolved Black Hole Problems` (a
  sibling of "Black Hole Simulation Lab" and "Unresolved Math Problems"), the
  C: junctions were removed link-only (Z: targets verified unharmed), and
  `C:\bhwork` was deleted. Standing rule recorded: **all dev work on the Z: ReFS
  dev drive, never C:.**

- **Enrichment pass — completed to spec.** Ran the multi-agent paper-search
  workflow (Consensus → arXiv/Semantic Scholar) in small waves to dodge the
  fleet-wide throttle. 15/16 problems landed on the first pass; #15 (primordial-BH
  dark matter) dropped on a transient socket error and was re-run via workflow
  resume (the other 15 returned from cache). Result: **all 16 problems now hold
  24–30 verified papers and 10–11 physicists**, `metadata.confidence: "researched"`.
  `scripts/apply_enrichment.py` enforces the integrity gate on merge — any paper
  lacking both an identifier (arXiv/DOI/URL) and a note is dropped, so nothing
  fabricated survives. All READMEs regenerated; `rag/INDEX.jsonl` rebuilt to
  **584 records**; validate + CI green. Commits `cc1cf7d` (15) and `f5232fd` (#15).
- **Fixed** the simulator's daily-research scheduled task: its "preferred local
  clone" path was missing the `CLAUDECODE` segment, forcing a slow clone-fallback
  each run. Corrected to `Z:\[Vibe Coded (AI)]\CLAUDECODE\Black Hole Simulation Lab`.

### Open follow-ups

- Cross-link `simulator_angle` fields to concrete features in
  `black-hole-simulation-lab` (notably #11 no-hair tests ↔ a QNM module) once a
  quasinormal-mode module exists in the simulator.
- Optional: extend the daily arXiv pull to append recent items per problem in
  this catalogue (mirroring the simulator project's research feed).
