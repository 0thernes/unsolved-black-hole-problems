# Unsolved Black-Hole Problems

A ranked, research-grade catalogue of the major **open problems** about black
holes — from the deepest, oldest foundational mysteries to the more tractable,
observationally-progressing questions. Each problem gets its own subfolder with
a narrative writeup, the originator's biography and core idea, a curated list of
key papers (foundational and recent), the physicists working on it, and
RAG-ready structured data.

> **Epistemic charter — read this first.** This repository **catalogues and
> structures** open problems. It does **not** claim to solve them, and it never
> presents a conjecture, speculation, or preprint as settled fact. Every entry
> carries a status and a truth tier. Where a problem is genuinely open, it says
> so. Citations are real and verifiable; nothing here is fabricated. See
> [PHILOSOPHY.md](PHILOSOPHY.md). This is the discipline that makes a catalogue
> like this worth anything — rigor over bravado.

License: **Proprietary — All Rights Reserved** (see [LICENSE](LICENSE)).
Branch: `main`. CI: GitHub Actions (schema + structural validation).

---

## How the ranking works

Problems are numbered **#1 (hardest / oldest / most fundamental) → #N (more
tractable / closer to resolution / observationally progressing)**. The ordering
blends three axes — *depth* (how fundamental: does it need new physics?), *age*
(how long it has resisted), and *tractability* (is there a credible path or
recent progress?). The methodology is spelled out in [PHILOSOPHY.md](PHILOSOPHY.md).
Ranking open problems is inherently a judgment call; the rationale per problem is
in its folder, and reordering is a normal, logged activity (see [KANBAN.md](KANBAN.md)).

## The catalogue

| # | Problem | First posed | Originator(s) | Status |
|---|---|---|---|---|
| 01 | [Spacetime singularities & their quantum-gravity resolution](problems/01-spacetime-singularities/) | 1916 / 1965 | Schwarzschild; Penrose, Hawking | Open — needs quantum gravity |
| 02 | [The black-hole information paradox](problems/02-information-paradox/) | 1975–76 | Hawking | Open — leading edge (islands/replica) |
| 03 | [Microscopic origin of Bekenstein–Hawking entropy](problems/03-bekenstein-hawking-entropy/) | 1972–73 | Bekenstein; Hawking | Open in general; solved for SUSY extremal |
| 04 | [Strong cosmic censorship & the Cauchy horizon](problems/04-strong-cosmic-censorship/) | 1969 | Penrose | Open — recent (near-extremal) counterexamples |
| 05 | [Weak cosmic censorship](problems/05-weak-cosmic-censorship/) | 1969 | Penrose | Open — known fragile cases |
| 06 | [The firewall paradox (AMPS)](problems/06-firewall-paradox/) | 2012 | Almheiri, Marolf, Polchinski, Sully | Open — sharpens #02 |
| 07 | [Black-hole complementarity & its consistency](problems/07-complementarity/) | 1993 | Susskind, Thorlacius, Uglum; ’t Hooft | Open — partially superseded |
| 08 | [ER=EPR and the entanglement–geometry connection](problems/08-er-epr/) | 2013 | Maldacena, Susskind | Open — active conjecture |
| 09 | [The endpoint of evaporation: remnants vs information release](problems/09-evaporation-endpoint/) | post-1975 | (Hawking and successors) | Open |
| 10 | [The trans-Planckian problem of Hawking radiation](problems/10-trans-planckian-problem/) | 1990s | Unruh; Jacobson | Open — robustness arguments exist |
| 11 | [Testing the no-hair theorem & exotic compact objects](problems/11-no-hair-tests/) | 1970s / 2015– | Israel, Carter, Hawking, Robinson | Open — observationally progressing |
| 12 | [Origin & seeds of supermassive black holes](problems/12-smbh-seeds/) | 2000s | (community; high-z quasar discoveries) | Open — astrophysical |
| 13 | [The final-parsec problem](problems/13-final-parsec/) | 1980 | Begelman, Blandford, Rees | Open — PTA-relevant |
| 14 | [Intermediate-mass black holes: existence & formation](problems/14-intermediate-mass-bh/) | 1970s– | (community) | Open — observationally narrowing |
| 15 | [Primordial black holes as dark matter](problems/15-primordial-bh-dark-matter/) | 1971 | Hawking; Carr | Open — heavily constrained |
| 16 | [The compact-object mass gaps](problems/16-mass-gaps/) | 1990s– | (community) | Open — narrowing with GW data |

Counts, coverage, and per-problem rationale live in each folder and in
[`rag/INDEX.jsonl`](rag/) (the machine-readable corpus).

## Repository layout

```text
README.md                     This file — the ranked master list.
PHILOSOPHY.md                 Epistemic stance, truth tiers, ranking method.
ARCHITECTURE.md               Repo + data + RAG architecture.
KANBAN.md                     Project board (research-ops workflow).
CHANGELOG.md                  Dated change log.
LICENSE / NOTICE              Proprietary, All Rights Reserved.
schema/
  problem.schema.json         JSON Schema each problem.json must satisfy.
  ERD.md                      Entity-relationship model (problem/physicist/paper).
scripts/
  validate.py                 Validate structure + every problem.json vs schema.
  build_rag.py                Assemble rag/INDEX.jsonl from per-problem data.
rag/
  INDEX.jsonl                 Generated RAG corpus (problems, papers, physicists).
problems/<NN-slug>/
  README.md                   Narrative: statement, history, originator bio, ideas.
  problem.json                Structured source-of-truth (validated, RAG input).
  papers.md                   Curated key papers (foundational + recent).
  physicists.md               Key researchers, past and present.
docs/
  audits/  logs/              Audit reports and project logs.
.github/workflows/ci.yml      Schema + structural validation on every push.
```

## Relationship to the simulator

This catalogue is the research backbone for the
[`black-hole-simulation-lab`](https://github.com/0thernes/black-hole-simulation-lab)
project (the GR ray tracer + observables). Problems here that have a concrete,
computable angle feed candidate features there; the simulator's research feed
and this catalogue share the same truth-tier discipline.
