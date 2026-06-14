# #13 — The final-parsec problem

*Also known as: last parsec problem, SMBH binary stalling, final-parsec problem.*

> **Status: OPEN WITH RECENT PROGRESS** · Statement tier: `numerical_approximation` · Resolution tier: `open_conjecture` · First posed: 1980.

## The problem

When two galaxies merge, their central supermassive black holes sink toward the center and form a binary. Dynamical friction and stellar scattering harden the binary efficiently down to roughly parsec separation, but there the binary may run out of stars on intersecting (loss-cone) orbits to extract its angular momentum, while gravitational-wave emission is still far too weak to drive a merger. The binary could then stall for longer than a Hubble time. Whether (and how) SMBH binaries cross this 'final parsec' to merge is open — and directly relevant to the nanohertz gravitational-wave background now detected by pulsar-timing arrays.

## History & originators

- **Mitchell Begelman**
- **Roger Blandford**
- **Martin Rees** — 1980 Nature paper describing the binary-SMBH evolution and the stalling problem.

## Why it ranks #13

A Newtonian/astrophysical dynamics problem (shallow in the fundamental sense) with active N-body/hydrodynamic simulations and a new observational handle (PTA nanohertz background); likely resolvable, so it sits near the bottom.

*(depth 3/10 · age 6/10 · tractability 7/10 — higher tractability pushes the rank toward the bottom of the list.)*

## Key ideas

- Stages: dynamical friction (kpc) -> three-body stellar scattering (parsec) -> gravitational-wave inspiral (milliparsec). The gap is between the second and third.
- Loss-cone depletion: stars on orbits that interact with the binary are ejected faster than they are replenished, stalling the hardening.
- Proposed solutions: non-spherical (triaxial) or rotating nuclei keep the loss cone full; gas-disk torques; or a third black hole inducing Kozai-Lidov oscillations.
- The detected PTA nanohertz GW background is consistent with a cosmic population of merging SMBH binaries, evidence that the final parsec IS crossed in many systems.
- Sets the event rate for future space-based (LISA) and PTA gravitational-wave observations.
- Connects to SMBH seeds (#12) and galaxy-merger demographics.

## Live approaches

- **Triaxial / rotating-nucleus N-body** (`numerical_approximation`) — Non-spherical galaxy potentials keep the loss cone refilled, avoiding stalling. _Proponents: David Merritt, Fazeel Khan, Peter Berczik._
- **Gas-driven inspiral** (`numerical_approximation`) — Circumbinary gas disks torque the binary across the gap. _Proponents: (community)._
- **PTA observational test** (`observational_constraint`) — Use the nanohertz GW background spectrum to infer whether/how binaries merge. _Proponents: NANOGrav, EPTA, PPTA, IPTA._

## Key papers

*Real, verifiable references (see PHILOSOPHY.md: no fabricated citations). This is a curated seed; coverage is noted below.*

- **Massive black hole binaries in active galactic nuclei** (1980) — Mitchell C. Begelman, Roger D. Blandford, Martin J. Rees. _foundational_, `numerical_approximation`. Nature 287, 307 — defines the binary-SMBH evolution and stalling.
- **The Final Parsec Problem** (2003) — Milos Milosavljevic, David Merritt. _foundational_, `numerical_approximation`. `arXiv:astro-ph/0212270`
- **Efficient Merger of Binary Supermassive Black Holes in Non-axisymmetric Galaxies** (2011) — Fazeel Mahmood Khan, Andreas Just, David Merritt. _recent_, `numerical_approximation`. `arXiv:1103.0272`
- **The NANOGrav 15 yr Data Set: Evidence for a Gravitational-wave Background** (2023) — NANOGrav Collaboration. _recent_, `observational_constraint`. `arXiv:2306.16213`

## Key physicists

- **Martin Rees** (originator, 1980-present, Cambridge) — Co-author of the founding binary-SMBH paper.
- **Roger Blandford** (originator, 1980-present, Stanford) — Co-author; AGN/jet theory.
- **Mitchell Begelman** (originator, 1980-present, Colorado) — Co-author of the 1980 framework.
- **David Merritt** (active, 1990s-present, RIT (emeritus)) — Named/analyzed the final-parsec problem; loss-cone dynamics.
- **Fazeel Khan** (active, 2010s-present, Pakistan/IST) — Showed triaxial galaxies avoid stalling in N-body simulations.

## Connection to the simulator

Outside the single-black-hole GR ray tracer; but a future binary/merger visualization and the resulting ringdown (a no-hair test, #11) connect back to it.

## Related problems

#12

---

*Coverage: Seed: 4 key references (Milosavljevic-Merritt/Khan/NANOGrav with arXiv ids; Begelman-Blandford-Rees 1980 as note) + 5 physicists. Aspiration up to 25 papers, to be expanded.*

*This page is generated from `problem.json` by `scripts/render_readme.py` (the structured file is the source of truth). Last updated 2026-06-14.*
