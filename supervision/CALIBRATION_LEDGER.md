# Prediction Calibration Ledger — running note

Living document (not sealed; anchored with each update), maintained by
the construction/supervision lane on the principal's instruction of
2026-07-26: "Carry a running note of the prediction family's
calibration... Weight future magnitude predictions accordingly, and say
so when making them."

## Standing calibration of this lane's prediction family

```text
SIGN / DIRECTION / OUTCOME-CLASS predictions:  RELIABLE so far.
MAGNITUDE / SCALING predictions:               MISSED TWICE CONSECUTIVELY.
BLOCK-vs-DERIVE predictions:                   improving after an early
                                               optimism bias was recorded.
```

RULE IN FORCE: every future magnitude or scaling prediction must be
stated together with this calibration ("magnitude predictions by this
lane have missed twice consecutively; weight accordingly"), and should
be widened relative to the lane's instinct rather than narrowed.

## Entries

| Date | Prediction | Outcome | Class |
|---|---|---|---|
| 07-25 | ER insensitivity gate: RESOLVABLE at 5e-5 (P1) | Superseded by the V002 refoundation (floors recomputed from witnessed moduli) | withdrawn pre-execution |
| 07-25 | ER gate V002 P3: NOT_RESOLVED_AT_FINITE_LANE_PRECISION | HELD exactly | outcome-class: HIT |
| 07-25 | ER gate V002 P1/P2 (per-state non-resolution) | HELD | outcome-class: HIT |
| 07-25 | Gamma memo: kill-test returns NONZERO (P1) | CONSISTENT with the certified computation (gate blocked, so not "confirmed") | sign: HIT (qualified) |
| 07-25 | Gamma gate P2: \|Delta_Xi\|/\|\|J\|\|^2 in O(1e-1)–O(1) | MISSED — measured 0.0202 / 0.0198 | magnitude: MISS (2nd consecutive) |
| 07-26 | Majorant P1: Route-T certifies on the pinned skeleton | NOT REACHED — blocked by ordering (Phase-A bundle absent) | untested |
| 07-26 | Majorant P2: O7 refinement-intertwiner is the honest block; overall SCOPE_RESTRICTED-class | LANDED on the predicted obligation, with an exact refuting witness | outcome-class: HIT (strongest to date) |
| 07-26 | Majorant P3/P4 (W1 inside bound; controls behave) | Controls HELD (NC3–NC7 all pass); W1 blocked by ordering | partial |
| 07-26 | Duhamel S9.1–S9.5 (identities derive cleanly; contact control bites at 2nd order; GHZ blocks; anchors hold) | ALL HELD | outcome-class: HIT |

## Earlier inherited calibration (prior supervision lane, for continuity)

~12 exact hits / 4 optimism-misses at handoff; all four misses were
"predicted DERIVED where the corpus found an underived step" — errors
pointing toward honesty. The present lane's misses are of a different
character: magnitude scaling, not optimism about derivability.
