# Philosophy & Epistemic Charter

This catalogue is only as valuable as it is honest. A list of "unsolved
problems" that quietly smuggles in speculation, fabricated citations, or
wishful "near-solutions" is worse than no list at all. This document is the
discipline that keeps it trustworthy.

## 1. We catalogue; we do not pretend to solve

Every problem here is **open**. The repository's job is to state each problem
precisely, trace its history and originator, map the live ideas and the people
pursuing them, and assemble the literature — so that a researcher (or a
retrieval-augmented model) can stand on solid ground. Where partial results
exist (e.g. Strominger–Vafa entropy counting for supersymmetric extremal black
holes), we say exactly what was solved and what was not. Claiming to have
resolved an open problem of physics would be a lie, and lies compound.

## 2. Truth tiers

Every claim, paper, and status carries (explicitly or in `problem.json`) one of
these tiers — the same vocabulary used by the simulator project:

| Tier | Meaning |
|---|---|
| `established_theory` | Derived, widely-accepted result within a framework (e.g. the Hawking temperature within QFT-in-curved-spacetime). True *in the theory*; may be unobserved. |
| `observational_constraint` | Backed by measurement (EHT, LIGO/Virgo, X-ray, PTA). |
| `analytic_classical` | Exact GR result (e.g. the Kerr horizon area). |
| `numerical_approximation` | From simulation / numerical relativity. |
| `open_conjecture` | A precise but unproven proposal (ER=EPR, strong cosmic censorship). |
| `speculative_extension` | Beyond established frameworks; credible-but-questionable; explicitly flagged. |

A problem can mix tiers (its *statement* may be `established_theory` while its
*resolution* is `open_conjecture`). The tier is never decoration — it is the
reader's guide to how much weight a line can bear.

## 3. No fabricated citations — ever

Papers listed in `papers.md` / `problem.json` must be **real and verifiable**:
a real title, real authors, a year, and a resolvable identifier (arXiv id, DOI,
or a stable URL). When a "top 25 papers" target cannot be met with *verified*
entries, we list the verified ones and mark the set as a **seed** to be expanded
by sourced research — we do **not** invent the difference. A fabricated DOI is a
firing offense in any real lab; here it fails CI in spirit and is treated as a
defect.

## 4. How we rank (and why ranking is a judgment call)

Problems are ordered #1 (hardest) → #N. The score blends three axes, documented
per problem in its `problem.json` under `ranking`:

- **Depth** — does resolution require *new physics* (quantum gravity), or is it
  answerable within known frameworks? Deeper ⇒ higher.
- **Age / resistance** — how long has it stood? Older-and-unmoved ⇒ higher.
- **Tractability** — is there a credible path or recent traction (a theorem, a
  numerical result, an observational handle)? More tractable ⇒ lower.

Reasonable physicists would order these differently at the margins. The ranking
is a defensible editorial stance, not a theorem; disagreement is logged in
[KANBAN.md](KANBAN.md), not hidden.

## 5. Reasoning modes we apply

For each problem we try to bring more than one lens, and we name which:

- **Deductive** — what follows necessarily from the accepted axioms (GR, QFT,
  unitarity)? Paradoxes live where two deductive chains collide (information
  paradox = unitarity vs the semiclassical Hawking calculation).
- **Inductive** — what do observations (EHT, GW catalogues, quasar surveys)
  suggest, and how strongly?
- **Abductive** — what is the best explanation among rivals, and what would
  distinguish them?
- **Analogical** — controlled analogies (analogue-gravity / sonic horizons for
  Hawking radiation) and their limits.

Naming the mode keeps us from dressing a hunch as a proof.

## 6. Astrology vs astrophysics

The goal text mentions "astrology." This catalogue is **astrophysics and
cosmology** — gravity, spacetime, quantum fields. Astrology (horoscopic) has no
predictive physical content and appears here only if a specific, testable claim
is made, in which case it is filed under `speculative_extension` and assessed on
evidence like anything else. We do not blur the line.
