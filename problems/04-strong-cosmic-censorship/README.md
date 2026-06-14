# #04 — Strong cosmic censorship & the Cauchy horizon

> **Status: OPEN (with recent progress)** · Statement tier: `analytic_classical`
> · Resolution tier: `open_conjecture` · First posed: 1969 (Penrose).

## The problem

Charged and rotating black holes have, inside them, an **inner (Cauchy)
horizon**. Initial data on a spacelike slice determines the spacetime only up to
that horizon; beyond it, Einstein's equations admit *infinitely many*
continuations — determinism fails. **Strong cosmic censorship (SCC)** is the
conjecture that nature forbids this: for *generic* initial data the Cauchy
horizon is unstable and turns into a genuine singular boundary, so no observer
ever reaches the unpredictable region. Whether SCC holds — and in which precise
formulation — is open.

## History & originator

**Roger Penrose** posed cosmic censorship in 1969. The *weak* version (#05)
hides singularities behind event horizons; the *strong* version concerns
determinism in the interior. Penrose and Simpson (1973) found the key mechanism:
infalling radiation is **infinitely blueshifted** at the Cauchy horizon,
hinting it becomes singular. Poisson and Israel (1990) sharpened this into **mass
inflation**.

## Why it is hard

It is a global statement about *generic* solutions of a nonlinear PDE system —
exactly the regime where rigorous theorems are hardest. The competition is
quantitative: the **blueshift** amplifies perturbations while **quasinormal
ringing** damps them; which wins (and how smooth the surviving metric is) decides
SCC. Christodoulou reframed the question as the *regularity* of the metric
extension, not mere continuity.

## Live approaches (truth tiers)

- **Rigorous PDE relativity** (`analytic_classical`) — Dafermos & Luk's program
  on the C⁰-stability / nonlinear instability of the Kerr Cauchy horizon.
- **QNM vs blueshift analysis** (`numerical_approximation`) — Cardoso, Costa,
  Destounis, Hintz, Jansen (2018) showed **near-extremal Reissner–Nordström–de
  Sitter** black holes can *violate* SCC in the Christodoulou sense — a striking
  apparent counterexample.
- **Mass-inflation modeling** (`analytic_classical`) — Poisson–Israel.

## Status & what would count as a solution

There is genuine, rigorous progress (and explicit counterexamples in de Sitter
backgrounds), which is why this ranks more tractable than #01–#03. A resolution
would be a theorem settling, for the astrophysically relevant **Kerr** case with
generic data, whether the Cauchy horizon is generically singular at the required
regularity — preserving determinism — or not.

## Key references

See [`problem.json`](problem.json). Penrose 1969 (*Riv. Nuovo Cimento* **1**,
252); Simpson–Penrose 1973; Poisson–Israel 1990; Cardoso et al. 2018
(`arXiv:1711.10502`).

Related: [#05 weak cosmic censorship](../05-weak-cosmic-censorship/),
[#01 singularities](../01-spacetime-singularities/),
[#11 no-hair tests](../11-no-hair-tests/).
