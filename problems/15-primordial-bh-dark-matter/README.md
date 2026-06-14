# #15 — Primordial black holes as dark matter

*Also known as: PBH dark matter, primordial black holes, asteroid-mass window.*

> **Status: OPEN OBSERVATIONAL** · Statement tier: `observational_constraint` · Resolution tier: `open_conjecture` · First posed: 1971-1974.

## The problem

Black holes could have formed in the very early universe from the collapse of large density fluctuations, before stars existed (Hawking 1971; Carr-Hawking 1974). Such primordial black holes (PBHs) are a candidate for some or all of the dark matter, requiring no new particle. Observational limits (Hawking-evaporation constraints, microlensing, dynamical and accretion bounds, gravitational waves) exclude PBHs as the dominant dark matter across most mass ranges, but an 'asteroid-mass' window (~10^17-10^23 g) remains largely open, and PBHs could still be a sub-component or seed SMBHs. Whether PBHs exist at all, and their cosmological role, is unresolved.

## History & originators

- **Stephen Hawking** — 1971 proposal that gravitationally-collapsed objects could form in the early universe.
- **Bernard Carr** — with Hawking, 1974, developed PBH formation from density perturbations.

## Why it ranks #15

Cosmology/observation-driven and old (1971), but progressing fast with microlensing, GW, and CMB constraints; needs no new fundamental physics, so it ranks below the quantum-gravity problems despite its age.

*(depth 4/10 · age 7/10 · tractability 6/10 — higher tractability pushes the rank toward the bottom of the list.)*

## Key ideas

- PBHs form when a sufficiently large primordial overdensity re-enters the horizon and collapses; the mass is set by the horizon mass at that epoch.
- Mass spectrum is broad in principle (from sub-gram to supermassive), so constraints are window-by-window.
- Hawking evaporation: PBHs below ~5e14 g would have evaporated by now; their final bursts are searched for (gamma rays).
- Microlensing (MACHO/EROS/OGLE/Subaru-HSC), dynamical heating of star clusters, CMB accretion, and the LIGO/Virgo merger population all set bounds.
- The asteroid-mass window (~10^17-10^23 g) is hard to constrain (lensing wave-optics + finite-source effects) and remains viable for 100% dark matter.
- PBHs could also be sub-dominant yet seed supermassive black holes (#12) or contribute to GW mergers.

## Live approaches

- **Microlensing surveys** (`observational_constraint`) — Search for brightening of background stars by PBH lenses to constrain the mass function. _Proponents: Subaru HSC team, OGLE, Hiroko Niikura._
- **Evaporation / gamma-ray constraints** (`observational_constraint`) — Bound low-mass PBHs via Hawking emission and final-burst signatures. _Proponents: Bernard Carr, Don Page._
- **GW and accretion constraints** (`observational_constraint`) — Use the LIGO/Virgo merger population and CMB accretion bounds to limit PBH abundance. _Proponents: Juan Garcia-Bellido, Misao Sasaki._

## Key papers

*Real, verifiable references (see PHILOSOPHY.md: no fabricated citations). This is a curated seed; coverage is noted below.*

- **Gravitationally Collapsed Objects of Very Low Mass** (1971) — Stephen Hawking. _foundational_, `established_theory`. MNRAS 152, 75 — the first PBH proposal.
- **Black Holes in the Early Universe** (1974) — Bernard J. Carr, Stephen W. Hawking. _foundational_, `established_theory`. MNRAS 168, 399 — PBH formation from perturbations.
- **Primordial Black Holes as Dark Matter (constraints)** (2016) — Bernard Carr, Florian Kuhnel, Marit Sandstad. _foundational_, `observational_constraint`. `arXiv:1607.06077`
- **Primordial Black Holes as Dark Matter: Recent Developments (review)** (2020) — Bernard Carr, Florian Kuhnel. _review_, `observational_constraint`. `arXiv:2006.02838`
- **Microlensing constraints on primordial black holes with Subaru/HSC Andromeda observations** (2019) — Hiroko Niikura, et al.. _recent_, `observational_constraint`. `arXiv:1701.02151`

## Key physicists

- **Bernard Carr** (originator, 1974-present, Queen Mary University of London) — Co-founder of PBH theory; leading constraints and reviews.
- **Stephen Hawking** (originator, 1971-2018, Cambridge) — First proposed primordial black holes.
- **Florian Kuhnel** (active, 2010s-present, Munich (MPP)) — Modern PBH-dark-matter constraints and reviews.
- **Juan Garcia-Bellido** (active, 1990s-present, UAM Madrid) — PBH formation from inflation; GW/PBH connection.
- **Misao Sasaki** (active, 1980s-present, Kavli IPMU) — Inflationary perturbations; PBH and GW signatures.
- **Anne Green** (active, 2000s-present, Nottingham) — PBH dark-matter constraints and mass functions.

## Connection to the simulator

Asteroid-mass PBHs are far too small to image, but the simulator's Hawking-evaporation module (thermo) directly gives the evaporation lifetime that sets the low-mass PBH constraint boundary (~5e14 g evaporating now).

## Related problems

#02, #12, #16

---

*Coverage: Seed: 5 key references (Carr et al / Niikura with arXiv ids; Hawking 1971 & Carr-Hawking 1974 as notes) + 6 physicists. Aspiration up to 25 papers, to be expanded.*

*This page is generated from `problem.json` by `scripts/render_readme.py` (the structured file is the source of truth). Last updated 2026-06-14.*
