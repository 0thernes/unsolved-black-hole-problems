# Requesting academic review

This catalogue is an AI-reviewed meta-analysis (see [AI_REVIEW.md](AI_REVIEW.md))
and **welcomes scrutiny from human experts**. This page is the ready-to-use
option for soliciting that review. Author of record / Human-in-the-Loop:
**Alexander Donahue** (0thernes, 0_0@0thernes.art).

> **Honesty note.** This is a *catalogue / meta-analysis*, not a claimed original
> result, and there is no single institution that "certifies AI papers." Treat
> the channels below as where domain experts actually congregate. Lead with the
> verification ask, disclose the AI assistance up front, and never present an
> open problem as solved.

## Fastest path — on this repository

- **Open a GitHub issue** using the *Academic / expert review* template
  (`.github/ISSUE_TEMPLATE/academic_review.md`). Reviewers can comment per
  problem; confirmed corrections are merged with credit.
- **Open a pull request** against a specific `problems/NN-slug/problem.json`.

## Open / community review venues (real, appropriate)

- **PREreview** (prereview.org) — community preprint review; good for structured
  expert feedback.
- **Physics Stack Exchange** / **MathOverflow** — for verifying a *specific*
  claim, paper characterization, or piece of history (one focused question at a
  time; not for "review my whole catalogue").
- **ResearchGate / Academia.edu** — share the catalogue and request comments
  from followed researchers in GR / quantum gravity.
- **Preprint servers** — note the bar honestly: **arXiv** requires endorsement
  and is for original research, not catalogues, so it is likely *not*
  appropriate; **viXra** and **Zenodo** (with a DOI) will host a meta-analysis
  for citability. Use Zenodo if you want a citable DOI.
- **Discipline forums** — e.g. the gravity / numerical-relativity mailing lists
  and Slack/Discord communities where ringdown and information-paradox work is
  discussed.

## Direct outreach to groups (use the template below)

Relevant groups that study these exact problems (information paradox, QNMs,
cosmic censorship, PBHs): Perimeter Institute, AEI (Max Planck, Potsdam),
Cardiff Gravity, MIT/Caltech LIGO groups, Cambridge DAMTP, Princeton (math
relativity), KITP (UCSB), Penn State IGC. Cold outreach is hit-or-miss; a
short, specific, honest ask works best.

### Email template

```
Subject: Request to sanity-check an AI-reviewed black-hole research catalogue

Dear Prof. <name>,

I'm Alexander Donahue. I've assembled an open, ranked catalogue of the major
OPEN problems in black-hole physics — statements, histories, ~25 key papers and
~10 key researchers per problem, with explicit truth-tier labels:
  https://github.com/0thernes/unsolved-black-hole-problems

Full disclosure: it was assembled with substantial AI assistance and is
internally citation-integrity-checked (every reference has a real identifier or
note; none fabricated), but it has NOT yet been verified by human experts. It
claims to solve nothing — it is a meta-analysis.

Would you (or a student) be willing to glance at the one or two entries closest
to your work (e.g. <problem #N: title>) and flag anything wrong, missing, or
miscategorized? Even a few lines, or pointers to what's stale, would be
valuable. Corrections are credited in the repo.

Thank you for your time.
Alexander Donahue (GitHub: 0thernes) — 0_0@0thernes.art
```

## Multi-model AI verification

In parallel, the reproducible per-problem prompt in [AI_REVIEW.md](AI_REVIEW.md)
can be run against Grok, Gemini, GPT, and Claude; disagreements are logged and
are exactly the items worth a human's attention.
