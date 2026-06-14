# #03 — Microscopic origin of Bekenstein–Hawking entropy

> **Status: PARTIALLY SOLVED** (string theory counts special cases) · Statement
> tier: `established_theory` · Resolution tier: `open_conjecture` · First posed:
> 1972–1973.

## The problem

A black hole has entropy `S = k_B c³ A / (4 G ℏ)` — exactly one quarter of its
horizon **area** in Planck units. In ordinary thermodynamics entropy counts
microstates (`S = k_B ln Ω`). So: **what are a black hole's microstates, and why
is the count universally `A/4`?** That an *area* (not a volume) measures the
information content is the seed of the **holographic principle**. A microscopic
derivation exists for special black holes; the general astrophysical case does
not.

## History & originators

**Jacob Bekenstein (1947–2015)**, then a Princeton graduate student, argued in
1972–73 — against Wheeler's intuition and Hawking's initial skepticism — that a
black hole must carry entropy proportional to its area, or else dropping matter
in would violate the second law. **Stephen Hawking**, by computing the radiation
temperature in 1975, fixed the proportionality constant to exactly `1/4`. The
result has been a Rosetta Stone for quantum gravity ever since.

## Why it is hard

A microstate count needs a microscopic theory of the horizon's degrees of
freedom — i.e. quantum gravity. The answer must come out to `A/4` *universally*,
across charges, spins, and dimensions, which is a stringent constraint that most
naive countings miss.

## Live approaches (truth tiers)

- **String theory / D-brane counting** (`established_theory` *for SUSY cases*) —
  Strominger–Vafa (1996) counted BPS brane microstates and reproduced `A/4`
  exactly for extremal charged black holes; later extended to near-extremal and
  rotating cases. The generic non-extremal case is not covered.
- **Loop quantum gravity** (`speculative_extension`) — counts spin-network
  punctures of the horizon; fixes `A/4` via the Barbero–Immirzi parameter.
- **Wald / Noether-charge entropy** (`analytic_classical`) — defines horizon
  entropy as a Noether charge, generalizing `A/4` to higher-curvature gravity.
- **Near-horizon conformal symmetry (Cardy)** (`open_conjecture`) — a symmetry
  argument for universality, independent of microscopic details (Carlip).

## Status & what would count as a solution

Solved for supersymmetric/extremal black holes (a genuine triumph of string
theory). **Open:** a microstate account for a *generic, non-extremal, rotating
(astrophysical)* black hole, and a framework-independent explanation of why the
answer is always `A/4`.

## Key references

See [`problem.json`](problem.json). Landmarks: Bekenstein 1973 (*Phys. Rev. D*
**7**, 2333); Hawking 1975; Strominger–Vafa 1996 (`arXiv:hep-th/9601029`); Wald
1993 (`arXiv:gr-qc/9307038`).

Related: [#02 information paradox](../02-information-paradox/),
[#01 singularities](../01-spacetime-singularities/), [#08 ER=EPR](../08-er-epr/).
