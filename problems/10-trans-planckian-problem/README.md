# #10 — The trans-Planckian problem of Hawking radiation

*Also known as: trans-Planckian problem, robustness of Hawking radiation, ultrashort-distance problem.*

> **Status: OPEN WITH RECENT PROGRESS** · Statement tier: `established_theory` · Resolution tier: `open_conjecture` · First posed: 1981-1991.

## The problem

In the standard derivation, the Hawking quanta seen at late times are traced back to modes that were, near the horizon at early times, blueshifted to arbitrarily high (trans-Planckian) frequencies — far beyond where the underlying field theory and the fixed-background approximation can be trusted. The trans-Planckian problem asks whether Hawking radiation is a genuine, robust prediction or an artifact of extrapolating physics into an unknown ultraviolet regime. Analogue-gravity systems and modified-dispersion models give strong evidence for robustness, but a fully satisfactory, first-principles demonstration awaits the true short-distance theory.

## History & originators

- **William Unruh** — 1981 raised the issue and proposed the sonic (analogue) horizon as a testbed.
- **Ted Jacobson** — 1991 analysis of Hawking radiation and ultrashort distances / modified dispersion.

## Why it ranks #10

Less deep than the information cluster (it questions an approximation, not unitarity) and unusually tractable: analogue-gravity experiments and dispersion models let it be probed concretely; hence ranked lower.

*(depth 6/10 · age 5/10 · tractability 6/10 — higher tractability pushes the rank toward the bottom of the list.)*

## Key ideas

- Near-horizon exponential blueshift sends the origin of late Hawking quanta to trans-Planckian frequencies in the naive calculation.
- Modified-dispersion-relation models (introducing a UV cutoff) still reproduce a thermal spectrum to good approximation — evidence of robustness.
- Analogue gravity: sonic/optical/BEC 'horizons' realize the same kinematics with KNOWN microphysics, providing experimental tests.
- Observation of stimulated and (claimed) spontaneous analogue Hawking radiation in BECs (Steinhauer) supports the effect's robustness.
- The result hints that Hawking radiation is a low-energy, horizon-kinematics phenomenon insensitive to UV details — but this is argued, not proven.
- Connects to whether the equivalence principle plus QFT alone fix the radiation, independent of quantum gravity.

## Live approaches

- **Modified dispersion relations** (`numerical_approximation`) — Impose a Lorentz-violating UV cutoff and check the spectrum survives. _Proponents: Ted Jacobson, Renaud Parentani, Stefano Liberati._
- **Analogue gravity (sonic/optical/BEC horizons)** (`observational_constraint`) — Reproduce horizon kinematics in condensed-matter systems with known microphysics; measure analogue Hawking radiation. _Proponents: William Unruh, Jeff Steinhauer, Carlos Barcelo, Matt Visser._
- **Wave-packet / mode-tracking analyses** (`analytic_classical`) — Track the relevant modes carefully to show the trans-Planckian region is not essential. _Proponents: Renaud Parentani, Ralf Schutzhold._

## Key papers

*Real, verifiable references (see PHILOSOPHY.md: no fabricated citations). This is a curated seed; coverage is noted below.*

- **Experimental Black-Hole Evaporation?** (1981) — William G. Unruh. _foundational_, `established_theory`. Phys. Rev. Lett. 46, 1351 — the sonic-horizon analogy.
- **Black-hole evaporation and ultrashort distances** (1991) — Ted Jacobson. _foundational_, `established_theory`. Phys. Rev. D 44, 1731.
- **Analogue Gravity (Living Review)** (2011) — Carlos Barcelo, Stefano Liberati, Matt Visser. _review_, `established_theory`. `arXiv:gr-qc/0505065`
- **Observation of quantum Hawking radiation and its entanglement in an analogue black hole** (2016) — Jeff Steinhauer. _recent_, `observational_constraint`. `arXiv:1510.00621`
- **Hawking radiation without trans-Planckian frequencies** (1996) — Renaud Parentani, et al.. _recent_, `numerical_approximation`. representative dispersion-model robustness analysis; details to be verified in enrichment.

## Key physicists

- **William Unruh** (originator, 1976-present, UBC) — Unruh effect; sonic analogue horizons; raised the trans-Planckian issue.
- **Ted Jacobson** (originator, 1990s-present, Maryland) — Ultrashort-distance analysis; entropic/thermodynamic gravity.
- **Matt Visser** (active, 1990s-present, Victoria University of Wellington) — Analogue gravity framework.
- **Stefano Liberati** (active, 2000s-present, SISSA) — Analogue gravity; Lorentz-violation phenomenology.
- **Renaud Parentani** (active, 1990s-2020, Paris-Saclay) — Dispersion-model robustness of Hawking radiation.
- **Jeff Steinhauer** (active, 2010s-present, Technion) — BEC analogue Hawking-radiation experiments.

## Connection to the simulator

The near-horizon blueshift is exactly the gravitational-redshift factor the simulator already computes; the simulator can visualize how the redshift diverges approaching the horizon, the kinematic root of the trans-Planckian issue.

## Related problems

#01, #02

---

*Coverage: Seed: 5 key references (Barcelo-Liberati-Visser and Steinhauer with arXiv ids; Unruh/Jacobson as notes; one dispersion-model entry flagged for verification) + 6 physicists. Aspiration up to 25 papers, to be expanded.*

*This page is generated from `problem.json` by `scripts/render_readme.py` (the structured file is the source of truth). Last updated 2026-06-14.*
