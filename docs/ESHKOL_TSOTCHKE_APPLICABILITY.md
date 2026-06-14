# Eshkol & Tsotchke: where they genuinely help (and where they don't)

The directive asks to "start using ESHKOL and Tsotchke" and to think hard about
how they are useful "in various new angles." This document does that honestly,
problem by problem. The conclusion up front, because honesty beats hype:

> **For a research *catalogue* of open problems, neither Eshkol nor the Tsotchke
> ecosystem is on the critical path.** They are tools for *computation*, and the
> catalogue is *curated knowledge + a RAG*. Their genuine, bounded uses live in
> the companion `black-hole-simulation-lab` (the GR computation engine), where a
> source-grounded study already mapped them. This file records the few angles
> that survive scrutiny and the many that do not — applying deductive (what
> follows from what each tool actually is), inductive (what their code/tests
> show), and abductive (best explanation of where value lies) reasoning.

## What these tools actually are (from source, not READMEs)

- **Eshkol** — a real but prototype Scheme dialect that compiles to native code
  via LLVM, with genuine automatic differentiation (forward/reverse/symbolic),
  an AVX2 BLAS kernel, and RK4/RK45 ODE solvers. *Never built on Windows*;
  README over-claims ("consciousness engine", "quantum RNG"). MIT-licensed.
- **Tsotchke / quantum_geometric_tensor** — a *quantum-computing* library; its
  "geometric tensor" is the Fubini–Study/Bures metric on quantum state space
  CP^n, **not** spacetime curvature. One file, `differential_geometry.c`, is a
  generic (finite-difference, complex-Hermitian) metric→Christoffel→Riemann→
  geodesic engine usable as a *reference oracle*.
- **Tsotchke / libirrep** — a real C11 library for SO(3)/SU(2)/O(3)/SE(3)
  representations: Wigner-D matrices, Clebsch–Gordan coefficients, spherical
  harmonics. MIT. The genuinely most relevant piece for black-hole physics.
- **tensorcore / PINN / PIMC / spin-NN** — GEMM kernels and ML/condensed-matter
  demos; off-domain for classical GR. (The "PINN" trains on one hardcoded point
  and cannot solve a PDE as shipped.)

## Per-problem applicability

| # | Problem | Eshkol | Tsotchke | Verdict |
|---|---|---|---|---|
| 01 | Singularities | AD could differentiate regular-BH metric families | — | weak; conceptual only |
| 02 | Information paradox | — | — | none (pure quantum gravity) |
| 03 | BH entropy microstates | — | tensor/linear-algebra for state counts (generic, not GR-specific) | weak |
| 04 | Strong cosmic censorship | ODE/QNM solving | — | weak (own C++ suffices) |
| 05 | Weak cosmic censorship | — | — | none |
| 06–10 | Firewall / complementarity / ER=EPR / endpoint / trans-Planckian | — | — | none (QG/foundations) |
| **11** | **No-hair tests** | — | **libirrep: spin-weighted spherical harmonics for QNM angular eigenfunctions** | **GENUINE** — the one clear win |
| 12–16 | SMBH seeds / final parsec / IMBH / PBH-DM / mass gaps | — | — | none (astrophysics/population) |

## The genuine angles (survive scrutiny)

1. **`libirrep` ↔ #11 (no-hair tests / QNM spectroscopy).** Quasinormal-mode and
   perturbation analysis needs spin-weighted spherical harmonics ₛYₗₘ and
   angular-momentum coupling — exactly libirrep's domain (Wigner-D,
   Clebsch–Gordan). This is the right first integration *if and when* the
   simulator grows a QNM module; tracked via ADR-0005 (opt-in, SHA-pinned,
   adapter-only) in `black-hole-simulation-lab`. Premature before a QNM consumer
   exists — do not add scaffolding with no caller.
2. **`differential_geometry.c` as a verification oracle.** Its metric→Christoffel
   →geodesic pipeline is a useful *independent cross-check* of analytic GR
   computations. Already realized in the simulator as
   `tests/kerr_metric_cross_check_tests.cpp` (a from-scratch Kerr metric that
   verifies the kernel's geodesics are null and recover E, L_z). This is the
   honest "use Tsotchke to build the black hole" — as a checker, not a runtime
   dependency.
3. **Eshkol autodiff ↔ inverse/differentiable rendering (speculative).** *If* the
   simulator ever fits black-hole parameters to an image by gradient descent
   through the integrator, AD is the relevant feature — but mature C++ AD
   (Enzyme/Clad) or JAX is preferable to an unbuilt-on-Windows prototype.

## What to AVOID (cargo-culting)

- Do **not** wire `quantum_geometric_tensor` as a GR Christoffel/Riemann backend
  — its tensors live on quantum state space, a category error for Lorentzian
  spacetime.
- Do **not** treat `tensorcore`/`PINN`/`PIMC` as relevant to classical GR.
- Do **not** port a working C++ engine onto Eshkol for "speed" — its RK4 is
  interpreted Scheme; you would trade tooling and a green build for a feature the
  forward problem does not use.

*Cross-reference: `black-hole-simulation-lab/docs/integrations/` carries the full
source-grounded study and the corrected ADR-0005 integration plan.*
