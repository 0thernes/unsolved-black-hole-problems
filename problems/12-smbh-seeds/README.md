# #12 — Origin & seeds of supermassive black holes

*Also known as: SMBH seeds, high-redshift quasar problem, early black hole growth.*

> **Status: OPEN OBSERVATIONAL** · Statement tier: `observational_constraint` · Resolution tier: `open_conjecture` · First posed: 2001-present (sharpened by high-z discoveries).

## The problem

Quasars powered by billion-solar-mass black holes are observed at redshift z > 7, less than ~700 million years after the Big Bang. Growing such masses so quickly from ordinary stellar-mass seeds via Eddington-limited accretion is difficult. The open problem is the formation channel: light seeds (~100 M_sun remnants of Population III stars) with episodes of super-Eddington accretion, heavy seeds (~10^4-10^6 M_sun) from direct collapse of pristine gas clouds, or runaway collapse in dense nuclear star clusters — and which dominates. It is an astrophysical problem (no new fundamental physics required), now sharply constrained by JWST and high-z quasar surveys.

## History & originators

- **Martin Rees** — early frameworks for SMBH formation and accretion.
- **Marta Volonteri** — modern seed/growth scenarios and reviews.

## Why it ranks #12

An astrophysical formation problem (no new fundamental physics), strongly observationally driven (JWST, high-z quasars) and modeled with simulations; tractable and progressing, hence low on the difficulty list.

*(depth 4/10 · age 4/10 · tractability 7/10 — higher tractability pushes the rank toward the bottom of the list.)*

## Key ideas

- e-folding (Salpeter) time for Eddington-limited growth is ~45 Myr; reaching 10^9 M_sun by z~7 from a 100 M_sun seed requires near-continuous accretion or super-Eddington phases.
- Light seeds: Population III stellar remnants (~10-1000 M_sun).
- Heavy seeds: direct collapse of atomically-cooling, metal-free gas to ~10^4-10^6 M_sun, avoiding fragmentation (needs Lyman-Werner radiation to suppress H2 cooling).
- Runaway stellar collisions in dense nuclear clusters as an intermediate channel.
- JWST is finding abundant faint AGN / overmassive black holes at high z, reshaping the seed debate.
- Connects to intermediate-mass black holes (#14) as possible leftover seeds.

## Live approaches

- **Direct-collapse heavy seeds** (`numerical_approximation`) — Form ~10^5 M_sun seeds from pristine gas without fragmentation; explains rapid early growth. _Proponents: Mitchell Begelman, Zoltan Haiman, Priyamvada Natarajan._
- **Light seeds + super-Eddington accretion** (`numerical_approximation`) — Pop III remnants grow via episodic super-Eddington (slim-disk) accretion. _Proponents: Marta Volonteri, Kohei Inayoshi._
- **Nuclear-cluster runaway** (`numerical_approximation`) — Stellar collisions in dense clusters build a very massive star then a seed. _Proponents: Marta Volonteri, Hagai Perets._

## Key papers

*Real, verifiable references (see PHILOSOPHY.md: no fabricated citations). This is a curated seed; coverage is noted below.*

- **Formation of Supermassive Black Holes (review)** (2010) — Marta Volonteri. _review_, `numerical_approximation`. `arXiv:1003.4404`
- **The Assembly of the First Massive Black Holes (review)** (2020) — Kohei Inayoshi, Eli Visbal, Zoltan Haiman. _review_, `numerical_approximation`. `arXiv:1911.05791`
- **An 800-million-solar-mass black hole in a significantly neutral Universe at a redshift of 7.5** (2018) — Eduardo Banados, et al.. _foundational_, `observational_constraint`. `arXiv:1712.01860` — quasar ULAS J1342+0928 at z=7.54.
- **A luminous quasar at redshift 7.642 (J0313-1806)** (2021) — Feige Wang, et al.. _recent_, `observational_constraint`. `arXiv:2101.03179`
- **Massive black hole seeds (review)** (2006) — Mitchell C. Begelman, Marta Volonteri, Martin J. Rees. _review_, `numerical_approximation`. MNRAS 370, 289 — direct-collapse 'quasistar' seeds.

## Key physicists

- **Martin Rees** (foundational, 1970s-present, Cambridge) — Foundational AGN/SMBH theory; seed scenarios.
- **Marta Volonteri** (active, 2000s-present, IAP Paris) — Leading theorist of SMBH seed formation and growth.
- **Zoltan Haiman** (active, 2000s-present, Columbia) — Direct-collapse seeds; high-z quasar growth.
- **Priyamvada Natarajan** (active, 2000s-present, Yale) — Heavy-seed models and their observational signatures.
- **Mitchell Begelman** (active, 1980s-present, Colorado) — Quasistar / direct-collapse seed theory.
- **Kohei Inayoshi** (active, 2010s-present, Peking University) — Super-Eddington growth and seed assembly.

## Connection to the simulator

Out of the GR-ray-tracer's scope (this is formation astrophysics), but the resulting Kerr black holes are exactly what the simulator renders; spin distributions of early SMBHs connect to #11.

## Related problems

#13, #14

---

*Coverage: Seed: 5 key references (Volonteri/Inayoshi/Banados/Wang with arXiv ids; Begelman-Volonteri-Rees as note) + 6 physicists. Aspiration up to 25 papers, to be expanded.*

*This page is generated from `problem.json` by `scripts/render_readme.py` (the structured file is the source of truth). Last updated 2026-06-14.*
