# AI-Reviewed Meta-Analysis — what that means here

This catalogue is an **AI-reviewed meta-analysis** of the published black-hole
literature, **directed and reviewed by a human, Alexander Donahue** (the
Human-in-the-Loop). This document states honestly what that label does and does
**not** claim — because an integrity charter that overclaims is worthless (see
[PHILOSOPHY.md](../PHILOSOPHY.md)).

## What was actually done

- **Assembly.** The 16 problems, rankings, statements, originator biographies,
  key-paper lists (~25 per problem), and key-physicist lists (~10 per problem)
  were drafted by Anthropic **Claude / Claude Code** and a **multi-agent
  research-and-verification system** that searched the literature
  (Consensus → arXiv / Semantic Scholar) in waves, under Alexander Donahue's
  direction.
- **Citation integrity (enforced mechanically).** Every paper entry must carry a
  real identifier (arXiv / DOI / resolver URL) **or** an explicit bibliographic
  note. `scripts/validate.py` and `scripts/apply_enrichment.py` **drop any entry
  that has neither**, so a fabricated or unverifiable citation cannot survive
  into the catalogue or its RAG index. CI enforces this on every push.
- **Truth tiers.** Every problem and paper is tagged with one of six truth tiers
  (established_theory … speculative_extension). No tier = no claim.
- **Single-model review.** The content has been internally cross-checked by
  Claude during assembly and curated by the human author.

## What has NOT (yet) been done — stated plainly

- **It has not been independently verified by Grok, Gemini, or GPT.** The
  "multi-model" review below is an *open invitation and a reproducible method*,
  not a completed result.
- **It has not been peer-reviewed by human academics.** See
  [ACADEMIC_REVIEW_REQUEST.md](ACADEMIC_REVIEW_REQUEST.md).
- **It solves no open problem.** It is a catalogue/meta-analysis. Conjectures are
  labeled as conjectures.
- Citation *identifiers* are checked for presence and format; this is not a
  guarantee that every bibliographic detail (year, page) is transcribed
  perfectly. Corrections are welcome (open an issue).

## The multi-model verification framework (reproducible)

The goal is a catalogue whose every factual claim can be independently checked by
several frontier models **and** by human experts. Anyone can run the check
below; results (agreements and disagreements) are welcome as issues or PRs.

**Per-problem verification prompt** (run against Grok, Gemini, GPT, and Claude
independently, then compare):

> You are verifying one entry of a black-hole research catalogue. For the
> problem described in `problems/NN-slug/problem.json`:
> 1. Is the problem statement an accurate description of a genuinely *open*
>    question (or is any part of it actually resolved)? Cite sources.
> 2. For each listed paper: does it exist, do the authors/year match, and is it
>    correctly characterized (foundational / recent / review)? Flag any you
>    cannot verify.
> 3. For each listed physicist: is the attributed contribution accurate?
> 4. Is the truth-tier label defensible?
> 5. List anything important that is **missing** or **miscategorized**.
> Return a structured verdict with per-item confidence and citations.

**Aggregation.** A claim is "multi-model confirmed" when ≥3 of the 4 models
independently confirm it with citations; disagreements are logged per problem and
escalated to human review. This file will record the status as that review
happens — it currently stands at **single-model (Claude) + mechanical integrity
checks**.

## Attribution

Human-in-the-Loop and author of record: **Alexander Donahue** (0thernes). Cite
via [CITATION.cff](../CITATION.cff). AI involvement is disclosed deliberately;
the human author is responsible for the catalogue's scope, decisions, and the
acceptance of every entry.
