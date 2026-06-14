# Entity-Relationship Model

The catalogue is a small graph of three entities. `problem.json` denormalizes
Papers and Physicists *into* each Problem (one file per problem is the unit of
authorship and review); the RAG build re-expands them into separate records.

```
┌─────────────────────────────┐
│           PROBLEM           │
│  rank (PK, 1..N, unique)    │
│  slug (unique, NN-slug)     │
│  title, statement           │
│  first_posed                │
│  status                     │
│  statement_tier             │
│  resolution_tier            │
│  ranking{depth,age,tract.}  │
│  key_ideas[]                │
│  simulator_angle            │
└──────────────┬──────────────┘
               │ 1
        ┌──────┼───────────────────────┬─────────────────────────┐
        │ N    │ N                      │ N                       │ N
┌───────▼──────────┐   ┌───────────────▼────────┐   ┌────────────▼───────────┐
│      PAPER       │   │       PHYSICIST        │   │   RELATED_PROBLEM (ref) │
│  title           │   │  name                  │   │  rank (FK → PROBLEM)    │
│  authors[]       │   │  role                  │   └────────────────────────┘
│  year            │   │  era, affiliation      │
│  kind            │   │  contribution          │
│  tier            │   └────────────────────────┘
│  identifier{...} │      (a physicist may recur
│  note            │       across many problems)
└──────────────────┘
```

## Relationships

- **PROBLEM 1—N PAPER.** Each problem owns a list of real, verifiable papers
  (foundational / review / recent / textbook). A paper with no `identifier`
  must carry a `note` (integrity rule, enforced by `validate.py`).
- **PROBLEM 1—N PHYSICIST.** Originators, foundational figures, and currently
  active researchers. The same person legitimately appears under several
  problems (e.g. Penrose under #01, #04, #05; Hawking under #01, #02, #03, #15).
- **PROBLEM N—N PROBLEM** via `related_problems` (by rank) — e.g. the firewall
  (#06) sharpens the information paradox (#02).

## Keys & invariants

- `rank` is the primary key; ranks are unique and contiguous `1..N`
  (validated). The two-digit folder prefix equals `rank`.
- `slug` equals the folder name and matches `^[0-9]{2}-[a-z0-9-]+$`.
- The RAG index id space: `problem:<slug>`, `paper:<slug>:<i>`,
  `physicist:<slug>:<i>` — stable across rebuilds.
