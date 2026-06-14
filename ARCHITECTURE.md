# Architecture

This is a **research-ops catalogue**: structured knowledge + a RAG pipeline +
validation, not an application. The architecture optimizes for (a) integrity
(nothing fabricated, everything validated), (b) retrievability (clean RAG), and
(c) growth (new problems and enriched citations land without breaking anything).

## Data flow

```
problems/<NN-slug>/problem.json   ← source of truth (human-authored, schema-bound)
        │
        ├── validate.py ──────────→ CI gate (schema + structural + integrity rules)
        │
        └── build_rag.py ─────────→ rag/INDEX.jsonl  (problem / paper / physicist records)
                                          │
                                          └──→ embedded by any RAG client
problems/<NN-slug>/README.md      ← human narrative, kept consistent with problem.json
```

`problem.json` is canonical. `README.md` is the readable face of the same facts.
`rag/INDEX.jsonl` is **generated** — never hand-edited — and CI fails if it drifts
from the source `problem.json` files (so the corpus is always reproducible).

## Layers

1. **Source layer** — `problems/*/problem.json`, governed by
   `schema/problem.schema.json`. One file per problem; the single point of truth.
2. **Narrative layer** — `problems/*/README.md`, `papers.md`, `physicists.md`.
   Human-facing; mirrors the source layer.
3. **Validation layer** — `scripts/validate.py` + `.github/workflows/ci.yml`.
   Enforces schema, rank contiguity, slug/folder agreement, README/disk
   consistency, and the no-unverifiable-citation rule.
4. **RAG layer** — `scripts/build_rag.py` → `rag/INDEX.jsonl`. Deterministic,
   diff-clean, three record types (problem, paper, physicist) each with a `text`
   field for embedding and `metadata` for filtered retrieval.
5. **Governance layer** — `PHILOSOPHY.md` (epistemics + truth tiers),
   `KANBAN.md` (workflow), `CHANGELOG.md`, `docs/audits/`, `docs/logs/`.

## Entity model

See [schema/ERD.md](schema/ERD.md). In brief: a **Problem** has many **Papers**
and many **Physicists**; a Physicist may relate to many Problems (originator /
active / historical); Problems reference related Problems by rank.

## Truth-tier propagation

Every node (problem statement, resolution, paper, approach) carries a truth tier
from `PHILOSOPHY.md`. The RAG records preserve the tier in `metadata` so a
downstream model can weight `established_theory` and `observational_constraint`
above `open_conjecture` and `speculative_extension`.

## Toolchain note (Eshkol / Tsotchke)

The companion `black-hole-simulation-lab` evaluated the Eshkol language and the
Tsotchke ecosystem (see its `docs/integrations/`). The honest finding: those are
LOW-relevance for a classical-GR renderer, and likewise this catalogue does not
take a runtime dependency on them. Their genuine, bounded uses (a metric-based
verification *oracle*; `libirrep` for future spin-weighted-harmonic / QNM work)
are tracked in that repo. This catalogue's `#11` (no-hair tests) is the natural
place where representation-theory tooling could later earn its keep.
