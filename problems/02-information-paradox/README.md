# #02 — The black-hole information paradox

> **Status: OPEN (with recent progress)** · Statement tier: `established_theory`
> · Resolution tier: `open_conjecture` · First posed: 1975–1976 (Hawking).

## The problem

In 1975 Hawking showed that a black hole is not truly black: quantum fields near
the horizon produce **thermal radiation**, and the hole slowly **evaporates**.
Taken at face value, the radiation is exactly thermal — it carries no imprint of
what fell in. If the hole then evaporates *completely*, a **pure** initial
quantum state has become a **mixed** (thermal) final state. That is forbidden by
quantum mechanics, whose evolution is **unitary** (information-preserving). So
either quantum mechanics, general relativity, or our picture of the horizon must
give. Reconciling evaporation with unitarity is the defining problem of the
quantum/gravity interface — hence #2, just below the singularity itself.

## History & originator

**Stephen Hawking (1942–2018)**, building on Bekenstein's entropy proposal
(#03) and Zel'dovich/Starobinsky's rotating-body radiance, computed in 1975 that
a Schwarzschild hole radiates at temperature `T = ℏc³/8πGMk_B`. In 1976 he argued
this implied a genuine **breakdown of predictability** — information loss. He
famously bet against information preservation, and in 2004 conceded (
controversially) that information is likely preserved, though the mechanism was
unclear. The paradox drove decades of work on holography and quantum gravity.

## Why it is hard

The two horns are each compelling. The semiclassical Hawking calculation is
trustworthy where it is done (low curvature at the horizon), yet it predicts
thermality. Unitarity is the bedrock of quantum mechanics. The information, if
preserved, must escape from behind a horizon that classically lets nothing out —
without violating locality or the equivalence principle (the **firewall**
tension, #06).

## Live approaches (truth tiers)

- **Islands / quantum extremal surfaces** (`open_conjecture`) — including
  "island" regions of the interior in the radiation's entropy reproduces the
  **Page curve** in semiclassical gravity (Penington; Almheiri–Engelhardt–
  Marolf–Maxfield, 2019).
- **Replica wormholes** (`open_conjecture`) — new gravitational path-integral
  saddles that supply the entropy turnover (Almheiri–Hartman–Maldacena–
  Shaghoulian–Tajdini, 2019–2020).
- **Complementarity / holography** (`open_conjecture`) — interior and exterior
  are complementary descriptions (#07); AdS/CFT is manifestly unitary.
- **Soft hair** (`speculative_extension`) — information in zero-energy horizon
  modes (Hawking–Perry–Strominger, 2016).

## Status & what would count as a solution

The island program shows the **radiation entropy** follows a unitary Page curve —
strong evidence for unitarity. **What remains open:** the explicit mechanism by
which information is transferred from the interior to the radiation, the physical
interpretation of replica wormholes, and the fate of the interior. A solution
would give a complete, mechanism-level account consistent with both unitarity
and a smooth horizon (no firewall).

## Key references

See [`problem.json`](problem.json). Landmarks: Hawking 1975 (*Commun. Math.
Phys.* **43**, 199); Hawking 1976 (*Phys. Rev. D* **14**, 2460); Page 1993
(`arXiv:hep-th/9306083`); the islands review (`arXiv:2006.06872`).

Related: [#06 firewall](../06-firewall-paradox/),
[#07 complementarity](../07-complementarity/), [#08 ER=EPR](../08-er-epr/),
[#03 entropy microstates](../03-bekenstein-hawking-entropy/),
[#09 evaporation endpoint](../09-evaporation-endpoint/).
