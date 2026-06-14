# #05 — Weak cosmic censorship

*Also known as: no naked singularities, WCC, cosmic censorship hypothesis.*

> **Status: OPEN WITH RECENT PROGRESS** · Statement tier: `analytic_classical` · Resolution tier: `open_conjecture` · First posed: 1969.

## The problem

Weak cosmic censorship (Penrose 1969) conjectures that the singularities produced by realistic gravitational collapse are always hidden behind event horizons, so no 'naked' singularity is visible to a distant observer and predictability at infinity is preserved. There is no general proof. Spherically-symmetric counterexamples exist (Christodoulou) but appear non-generic; gedanken experiments that try to over-spin or over-charge a black hole into a naked singularity are generically thwarted, though with subtle near-extremal cases; and clean violations are known in asymptotically anti-de Sitter spacetimes.

## History & originators

- **Roger Penrose** — 1969 cosmic-censorship hypothesis; weak version protects observers at infinity.

## Why it ranks #05

Foundational and old, but attacked with rigorous PDE methods and explicit examples; the genericity question (do violations survive perturbation?) is the crux and remains open in 4D asymptotically-flat GR.

*(depth 7/10 · age 8/10 · tractability 5/10 — higher tractability pushes the rank toward the bottom of the list.)*

## Key ideas

- A naked singularity would emit unpredictable signals to infinity, breaking the predictive power of GR for outside observers.
- Christodoulou proved naked singularities CAN form in spherical scalar-field collapse, then proved they are non-generic (perturbations remove them).
- Critical collapse (Choptuik): at the precise threshold between dispersal and black-hole formation sits a self-similar, marginally-naked solution.
- Overspinning/overcharging gedanken experiments: attempts to push a black hole past extremality (a>M) by throwing in matter are generically prevented, with delicate near-extremal exceptions.
- In asymptotically anti-de Sitter space, explicit WCC violations are known (Horowitz, Santos and collaborators).
- Closely tied to whether the final state of collapse is always a Kerr black hole.

## Live approaches

- **Rigorous spherical-collapse analysis** (`analytic_classical`) — Prove formation/non-genericity of naked singularities in symmetric models. _Proponents: Demetrios Christodoulou._
- **Critical-collapse / numerical relativity** (`numerical_approximation`) — Study the threshold of black-hole formation and its self-similar, marginally-naked critical solution. _Proponents: Matthew Choptuik._
- **Overspinning/overcharging gedanken tests** (`analytic_classical`) — Test destructibility of horizons by infalling matter; backreaction and self-force generically protect censorship. _Proponents: Robert Wald, Veronika Hubeny._
- **AdS violations** (`numerical_approximation`) — Construct explicit naked-singularity-forming solutions with anti-de Sitter boundary conditions. _Proponents: Gary Horowitz, Jorge Santos, Toby Crisford._

## Key papers

*Real, verifiable references (see PHILOSOPHY.md: no fabricated citations). This is a curated seed; coverage is noted below.*

- **Gravitational Collapse: The Role of General Relativity** (1969) — Roger Penrose. _foundational_, `analytic_classical`. Riv. Nuovo Cimento 1, 252.
- **Universality and Scaling in Gravitational Collapse of a Massless Scalar Field** (1993) — Matthew W. Choptuik. _foundational_, `numerical_approximation`. Phys. Rev. Lett. 70, 9 — critical collapse.
- **The instability of naked singularities in the gravitational collapse of a scalar field** (1999) — Demetrios Christodoulou. _foundational_, `analytic_classical`. Ann. of Math. 149, 183 — naked singularities are non-generic.
- **Gedanken Experiments to Destroy a Black Hole** (1974) — Robert M. Wald. _foundational_, `analytic_classical`. Ann. Phys. 82, 548 — cannot overcharge/overspin by dropping particles.
- **Violating the Weak Cosmic Censorship Conjecture in Four-Dimensional Anti-de Sitter Space** (2017) — Toby Crisford, Jorge E. Santos. _recent_, `numerical_approximation`. `arXiv:1702.05490`

## Key physicists

- **Roger Penrose** (originator, 1969-present, Oxford) — Cosmic-censorship hypothesis; Nobel Prize 2020.
- **Demetrios Christodoulou** (foundational, 1980s-present, ETH Zurich) — Formation and non-genericity of naked singularities in scalar collapse.
- **Matthew Choptuik** (active, 1990s-present, UBC) — Discovered critical phenomena in gravitational collapse.
- **Robert Wald** (foundational, 1970s-present, Chicago) — Gedanken tests of horizon destructibility.
- **Jorge Santos** (active, 2010s-present, Cambridge) — Explicit WCC violations in anti-de Sitter space.
- **Gary Horowitz** (active, 1980s-present, UC Santa Barbara) — Holography; AdS instabilities and censorship violations.

## Connection to the simulator

The event-horizon vs naked-singularity distinction is exactly the shadow-formation condition the simulator encodes (b_critical, the photon region); a hypothetical naked singularity would cast no shadow — a renderable contrast.

## Related problems

#01, #04, #11

---

*Coverage: Seed: 5 key references (Crisford-Santos with arXiv id; others as bibliographic notes) + 6 physicists. Aspiration up to 25 papers, to be expanded.*

*This page is generated from `problem.json` by `scripts/render_readme.py` (the structured file is the source of truth). Last updated 2026-06-14.*
