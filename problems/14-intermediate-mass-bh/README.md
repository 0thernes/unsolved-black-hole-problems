# #14 — Intermediate-mass black holes: existence & formation

*Also known as: IMBHs, missing-link black holes, 100-100000 solar mass black holes.*

> **Status: OPEN OBSERVATIONAL** · Statement tier: `observational_constraint` · Resolution tier: `open_conjecture` · First posed: 1970s-present.

## The problem

Black holes are well established in two regimes: stellar-mass (~3-100 M_sun, from stellar collapse) and supermassive (~10^6-10^10 M_sun, in galactic nuclei). Intermediate-mass black holes (IMBHs, ~100-10^5 M_sun) are the expected bridge, but observational confirmation is sparse and their formation channels uncertain. The open problem: do IMBHs exist as a genuine population, where (globular clusters, dwarf-galaxy nuclei, ultraluminous X-ray sources?), and how do they form (runaway stellar collisions, repeated mergers, leftover SMBH seeds)? Gravitational-wave events like GW190521 (a ~150 M_sun remnant) and dynamical/X-ray candidates are narrowing the gap.

## History & originators

- **(community)** — no single originator; the 'missing link' framing emerged from cluster dynamics and ULX observations.

## Why it ranks #14

Existence/formation is an observational and astrophysical-dynamics question, actively narrowed by gravitational waves (GW190521), dynamics, and X-ray surveys; shallow fundamentally and progressing, so near the bottom.

*(depth 3/10 · age 5/10 · tractability 7/10 — higher tractability pushes the rank toward the bottom of the list.)*

## Key ideas

- Candidate sites: cores of globular and nuclear star clusters; nuclei of dwarf galaxies; some ultraluminous X-ray sources (ULXs).
- Formation channels: runaway collisions of massive stars in dense clusters; hierarchical (repeated) mergers of stellar-mass black holes; surviving direct-collapse SMBH seeds.
- GW190521 produced a ~150 M_sun remnant — the first fairly secure IMBH-scale object — and its components fall in/near the pair-instability gap (#16).
- Dynamical mass measurements in clusters are contentious (alternatives: a dense subcluster of stellar remnants can mimic an IMBH).
- An IMBH population would test SMBH seed scenarios (#12) and hierarchical-merger predictions.
- Future facilities (LISA, ngVLA, next-gen X-ray) target the IMBH regime directly.

## Live approaches

- **Gravitational-wave detection** (`observational_constraint`) — Identify IMBH-scale remnants and hierarchical mergers in LIGO/Virgo/KAGRA (and future LISA) data. _Proponents: LIGO/Virgo/KAGRA Collaboration._
- **Dynamical / X-ray candidate searches** (`observational_constraint`) — Measure central masses in clusters and characterize ULXs and tidal-disruption events. _Proponents: Jenny Greene, M. Coleman Miller._
- **Cluster N-body formation models** (`numerical_approximation`) — Simulate runaway collisions and repeated mergers to predict IMBH masses and rates. _Proponents: (community)._

## Key papers

*Real, verifiable references (see PHILOSOPHY.md: no fabricated citations). This is a curated seed; coverage is noted below.*

- **Intermediate-Mass Black Holes (review)** (2020) — Jenny E. Greene, Jay Strader, Luis C. Ho. _review_, `observational_constraint`. `arXiv:1911.09678`
- **GW190521: A Binary Black Hole Merger with a Total Mass of 150 Msun** (2020) — LIGO Scientific Collaboration, Virgo Collaboration. _foundational_, `observational_constraint`. `arXiv:2009.01075`
- **Intermediate-Mass Black Holes (earlier review)** (2004) — M. Coleman Miller, E. J. M. Colbert. _review_, `observational_constraint`. `arXiv:astro-ph/0308402`

## Key physicists

- **Jenny Greene** (active, 2000s-present, Princeton) — Low-mass / intermediate-mass black-hole searches and demographics.
- **M. Coleman Miller** (active, 2000s-present, Maryland) — IMBH formation theory; ULX interpretation.
- **Jay Strader** (active, 2010s-present, Michigan State) — IMBH candidate searches in clusters.
- **Luis Ho** (active, 1990s-present, Peking University (KIAA)) — AGN/black-hole demographics across the mass range.

## Connection to the simulator

Mass-agnostic for the GR renderer (an IMBH renders like any Kerr/Schwarzschild hole at the right mass); relevant mainly as the demographic bridge, not a new geometry.

## Related problems

#12, #16

---

*Coverage: Seed: 3 key references with arXiv ids + 4 physicists. Aspiration up to 25 papers, to be expanded.*

*This page is generated from `problem.json` by `scripts/render_readme.py` (the structured file is the source of truth). Last updated 2026-06-14.*
