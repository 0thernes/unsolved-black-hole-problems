# #11 — Testing the no-hair theorem & exotic compact objects

*Also known as: no-hair theorem tests, black-hole spectroscopy, are they really Kerr?, exotic compact objects.*

> **Status: OPEN OBSERVATIONAL** · Statement tier: `analytic_classical` · Resolution tier: `observational_constraint` · First posed: 1967-1975 (theorems); 2015- (precision tests).

## The problem

The no-hair theorems (Israel, Carter, Hawking, Robinson) state that a stationary, isolated black hole in general relativity is completely characterized by mass, spin, and charge — all higher multipole moments are fixed functions of these (the Kerr metric for the astrophysical, uncharged case). The open question is observational and theoretical: are the compact objects we detect actually Kerr black holes, or could they be exotic alternatives (boson stars, gravastars, wormholes, fuzzballs) or harbor deviations from GR? Black-hole spectroscopy (quasinormal-mode ringdown with LIGO/Virgo/KAGRA) and the Event Horizon Telescope shadow are now testing this directly, with results so far consistent with Kerr but far from a decisive null.

## History & originators

- **Werner Israel** — 1967 uniqueness for static (Schwarzschild) black holes.
- **Brandon Carter** — 1971 two-parameter (Kerr) family theorem.
- **Stephen Hawking** — 1972 rigidity / horizon topology results.
- **David Robinson** — 1975 Kerr uniqueness.

## Why it ranks #11

The theorem is established GR; the open part is whether nature realizes it, which is now directly testable with gravitational-wave ringdown and EHT imaging. High tractability and active observational progress place it low on the difficulty list.

*(depth 5/10 · age 6/10 · tractability 7/10 — higher tractability pushes the rank toward the bottom of the list.)*

## Key ideas

- No-hair: (mass, spin, charge) fix all multipoles; e.g. the quadrupole is Q = -J^2/M for Kerr.
- Quasinormal modes: the ringdown after a merger is a superposition of damped tones whose frequencies depend ONLY on the remnant mass and spin if it is Kerr.
- Black-hole spectroscopy: detecting two or more QNMs over-determines (M, J) and tests the Kerr prediction; a mismatch would signal new physics or an exotic object.
- The EHT shadow size/shape tests the photon-region geometry against Kerr.
- Exotic compact objects (boson stars, gravastars, wormholes) can mimic some signatures but typically differ in ringdown 'echoes' or shadow structure.
- Charge is astrophysically negligible, so the relevant test is two-parameter Kerr.

## Live approaches

- **Gravitational-wave ringdown spectroscopy** (`observational_constraint`) — Extract multiple QNMs from merger ringdowns and check consistency with Kerr (M, J). _Proponents: Saul Teukolsky, Emanuele Berti, Vitor Cardoso, Maximiliano Isi, Will Farr._
- **EHT shadow imaging** (`observational_constraint`) — Compare the measured shadow size/asymmetry of M87* and Sgr A* with the Kerr photon region. _Proponents: Event Horizon Telescope Collaboration._
- **Exotic-compact-object modeling** (`speculative_extension`) — Predict distinguishing signatures (echoes, modified shadows, tidal-deformability) of non-Kerr alternatives. _Proponents: Vitor Cardoso, Paolo Pani._

## Key papers

*Real, verifiable references (see PHILOSOPHY.md: no fabricated citations). This is a curated seed; coverage is noted below.*

- **Event Horizon in Metrics of Rotating Masses (Kerr uniqueness, two-parameter family)** (1971) — Brandon Carter. _foundational_, `analytic_classical`. Phys. Rev. Lett. 26, 331.
- **Event Horizons in Static Vacuum Space-Times** (1967) — Werner Israel. _foundational_, `analytic_classical`. Phys. Rev. 164, 1776 — Schwarzschild uniqueness.
- **Observation of Gravitational Waves from a Binary Black Hole Merger (GW150914)** (2016) — LIGO Scientific Collaboration, Virgo Collaboration. _foundational_, `observational_constraint`. `arXiv:1602.03837`
- **Testing the no-hair theorem with GW150914** (2019) — Maximiliano Isi, Matthew Giesler, Will M. Farr, Mark A. Scheel, Saul A. Teukolsky. _recent_, `observational_constraint`. `arXiv:1905.00869`
- **Quasinormal modes of black holes and black branes (review)** (2009) — Emanuele Berti, Vitor Cardoso, Andrei O. Starinets. _review_, `numerical_approximation`. `arXiv:0905.2975`
- **First M87 Event Horizon Telescope Results. I. The Shadow of the Supermassive Black Hole** (2019) — Event Horizon Telescope Collaboration. _foundational_, `observational_constraint`. `arXiv:1906.11238`

## Key physicists

- **Brandon Carter** (originator, 1968-present, Meudon/Paris) — Kerr uniqueness; Carter constant; no-hair.
- **Werner Israel** (originator, 1960s-2010s, Alberta/Victoria) — Static black-hole uniqueness.
- **Saul Teukolsky** (active, 1970s-present, Cornell/Caltech) — Teukolsky equation; QNMs; numerical relativity; spectroscopy.
- **Emanuele Berti** (active, 2000s-present, Johns Hopkins) — QNM theory and tests of GR with ringdown.
- **Vitor Cardoso** (active, 2000s-present, IST Lisbon / NBI) — QNMs, exotic compact objects, echoes.
- **Maximiliano Isi** (active, 2010s-present, Flatiron/Columbia) — Ringdown overtone spectroscopy of GW150914.
- **Paolo Pani** (active, 2010s-present, Sapienza Rome) — Exotic-compact-object phenomenology.
- **Sheperd Doeleman** (active, 2000s-present, Harvard/EHT) — Founding director of the Event Horizon Telescope.

## Connection to the simulator

DIRECT: the simulator already computes the Kerr shadow (Bardeen boundary), photon region, and is the natural home for a quasinormal-mode module; no-hair tests are the observational counterpart of exactly what it renders. This is the catalogue entry most coupled to the simulation project (and where libirrep's spin-weighted spherical harmonics would genuinely earn their keep).

## Related problems

#01, #04, #05

---

*Coverage: Seed: 6 key references (LIGO/Isi/Berti/EHT with arXiv ids; Carter/Israel as notes) + 8 physicists. Aspiration up to 25 papers, to be expanded.*

*This page is generated from `problem.json` by `scripts/render_readme.py` (the structured file is the source of truth). Last updated 2026-06-14.*
