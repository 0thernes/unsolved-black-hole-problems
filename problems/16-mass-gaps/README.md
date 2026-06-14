# #16 — The compact-object mass gaps

*Also known as: lower mass gap, pair-instability mass gap, neutron-star-black-hole gap.*

> **Status: OPEN OBSERVATIONAL** · Statement tier: `observational_constraint` · Resolution tier: `open_conjecture` · First posed: 1990s-present.

## The problem

Two apparent gaps in the compact-object mass distribution are unexplained. The LOWER mass gap (~3-5 M_sun) lies between the heaviest neutron stars and the lightest black holes; X-ray binary data once suggested a real dearth there, but gravitational-wave events (e.g. GW190814's ~2.6 M_sun secondary, GW190425) populate or blur it. The UPPER (pair-instability) gap (~50-120 M_sun) is predicted because pair-instability supernovae leave no remnant; yet GW190521's ~85 M_sun component sits inside it. The open problem: are these gaps real features of stellar/supernova physics, or artifacts of selection and small samples — and what fills them (hierarchical mergers, accretion, exotic channels)?

## History & originators

- **(community)** — lower gap from X-ray-binary mass measurements (Bailyn et al. 1998); upper gap from pair-instability supernova theory.

## Why it ranks #16

A stellar-astrophysics and population-statistics question (shallow fundamentally), being actively resolved by the growing gravitational-wave catalogue; the most tractable entry, placed at the bottom of the list.

*(depth 3/10 · age 5/10 · tractability 7/10 — higher tractability pushes the rank toward the bottom of the list.)*

## Key ideas

- Lower gap (~3-5 M_sun): X-ray binaries showed few objects there; whether it is a true gap depends on the supernova explosion mechanism (rapid vs delayed).
- GW190814's secondary (~2.6 M_sun) is right in the lower gap — neutron star or black hole is unknown.
- Upper (pair-instability) gap (~50-120 M_sun): electron-positron pair production in very massive stellar cores triggers an instability that leaves NO remnant, forbidding direct-collapse BHs in this range.
- GW190521's ~85 M_sun component lies inside the upper gap, suggesting hierarchical (second-generation) mergers or uncertain pair-instability boundaries.
- Selection effects and small samples can mimic or hide a gap; population inference is improving with each LIGO/Virgo/KAGRA run.
- Resolving the gaps constrains supernova physics, the maximum neutron-star mass, and binary-evolution channels.

## Live approaches

- **Gravitational-wave population inference** (`observational_constraint`) — Hierarchically model the merging-binary mass distribution to test for true gaps. _Proponents: Will Farr, Maya Fishbach, LIGO/Virgo/KAGRA Collaboration._
- **Supernova / stellar-evolution modeling** (`numerical_approximation`) — Predict remnant masses (explosion mechanism, pair-instability) and the resulting gaps. _Proponents: Stan Woosley, Alexander Heger._
- **X-ray-binary mass measurements** (`observational_constraint`) — Dynamical masses of compact objects in X-ray binaries probing the lower gap. _Proponents: Charles Bailyn, Feryal Ozel._

## Key papers

*Real, verifiable references (see PHILOSOPHY.md: no fabricated citations). This is a curated seed; coverage is noted below.*

- **The Mass Distribution of Stellar Black Holes** (1998) — Charles D. Bailyn, Raj K. Jain, Paolo Coppi, Jerome A. Orosz. _foundational_, `observational_constraint`. `arXiv:astro-ph/9708032`
- **The Black Hole Mass Distribution in the Galaxy** (2010) — Feryal Ozel, Dimitrios Psaltis, Ramesh Narayan, Jeffrey E. McClintock. _foundational_, `observational_constraint`. `arXiv:1006.2834`
- **GW190814: Gravitational Waves from the Coalescence of a 23 Msun Black Hole with a 2.6 Msun Compact Object** (2020) — LIGO Scientific Collaboration, Virgo Collaboration. _foundational_, `observational_constraint`. `arXiv:2006.12611`
- **The mass distribution of stellar-mass black holes (lower-gap statistics)** (2011) — Will M. Farr, et al.. _recent_, `observational_constraint`. `arXiv:1011.1459`
- **Pulsational Pair-Instability Supernovae** (2017) — S. E. Woosley. _foundational_, `numerical_approximation`. `arXiv:1608.08939` — predicts the upper (pair-instability) mass gap.

## Key physicists

- **Feryal Ozel** (active, 2000s-present, Georgia Tech) — Compact-object mass distributions; the lower gap.
- **Charles Bailyn** (active, 1990s-present, Yale) — Early dynamical evidence for the lower mass gap.
- **Will Farr** (active, 2010s-present, Stony Brook / Flatiron) — Gravitational-wave population inference of the mass distribution.
- **Maya Fishbach** (active, 2010s-present, Toronto (CITA)) — Population analyses probing both gaps.
- **Stan Woosley** (active, 1980s-present, UC Santa Cruz) — Pair-instability supernova theory setting the upper gap.
- **Alexander Heger** (active, 2000s-present, Monash) — Massive-star evolution and remnant masses.

## Connection to the simulator

Mass-agnostic for the GR renderer; relevant as the population context (which masses of Kerr black holes actually exist) rather than a distinct geometry.

## Related problems

#12, #14

---

*Coverage: Seed: 5 key references with arXiv ids + 6 physicists. Aspiration up to 25 papers, to be expanded.*

*This page is generated from `problem.json` by `scripts/render_readme.py` (the structured file is the source of truth). Last updated 2026-06-14.*
