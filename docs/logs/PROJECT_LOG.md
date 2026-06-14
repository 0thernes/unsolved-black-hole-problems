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

### Open follow-ups

- Sourced citation enrichment (toward the ~25-papers / ~10-physicists aspiration)
  when the research workflow / paper APIs are not throttled.
- Optional: a scheduled daily arXiv pull appending recent items per problem
  (mirroring the simulator project's research feed).
- Cross-link `simulator_angle` fields to concrete features in
  `black-hole-simulation-lab` (notably #11 no-hair tests ↔ a QNM module).
