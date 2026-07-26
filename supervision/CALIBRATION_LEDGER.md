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
| 07-26 | Control-4 v3 S3(b) unbroken ≤1e-18 (ceiling 1e-12) | HIT (certified ≤1.11e-13; exact ≤3.6e-23) | magnitude: HIT |
| 07-26 | Control-4 v3 S3(c) structural (5 predictions) | 4 of 5 HELD; same-slot occupancy failed (the support mismatch) | outcome-class: mostly HIT |
| 07-26 | Control-4 v3 S3(a) broken magnitude, central 1e-6, window 1e-8..1e-4 | **MISS** — null (≤2.27e-11 certified; exact ~1e-21). Cause: the pinned DIRECTION was trace-orthogonal to the detector (L5), not a magnitude-model error. POST HOC and NOT CREDITED: the same model on the supported direction gives 4.57e-6, inside the window. | magnitude: MISS (3rd consecutive) |

## Independent-system prediction set (Codex; tracked SEPARATELY from this lane's)

Re-frozen 2026-07-26 after Codex withdrew its contaminated echo and
restated on the corrected algebra. Recorded before any E1 execution.

| id | prediction | status |
|---|---|---|
| P-C1 | Most likely outcome E1S_BLOCKED, with the one-line cross-term obligation AND Q6 as live blockers | open |
| P-C2 | IR-A's n≥2 leg DOWNGRADED from likely-survivor to open-block candidate | open |
| P-C3 | Route-Q / O7 independence unchanged (now triple-confirmed) | HELD so far |
| P-C4 | SCAD right for the n=1 side but does NOT repair the n≥2 cross term | open |
| P-C5 | Cross-term lemma: honest split (no universal zero identity; certification only via a propagation-bridge bound) | **LANDED** |
| P-C6 | Q6: no uniform raw adjacency-degree bound exists on full D3 | **LANDED** (with an explicit star-refinement construction) |

| P-C7 | Arm-2 C(ii): decay morally present from the free kernel after smooth time integration, but object-level uniform certification over D3 open absent a sealed profile/transversality/projection-tail lemma | **LANDED VERBATIM** |

Running assessment of the independent-system family: P-C3 held, P-C5, P-C6
and P-C7 landed with constructions — THREE CONSECUTIVE CYCLES. Two consecutive cycles in which its
predictions held while this lane's magnitude and route-survival
predictions did not. Weight it accordingly when the two disagree.

Note for later scoring: P-C2 is a prediction AGAINST this lane's earlier
IR-A optimism, and P-C1 predicts a block where this lane's spec predicted
a certified n≥2 sector. If P-C1/P-C2 land, that is a second independent
data point that this lane's route-survival predictions run optimistic —
the same direction as the inherited Fable-era calibration note.

## This lane's own defect ledger (added 2026-07-26; not predictions but errors)

| date | defect | caught by |
|---|---|---|
| 07-25 | theta_kappa arithmetic (1000x, plus a misderivation) | hostile review |
| 07-26 | R2 fabrication-economics claim false as written | external audit |
| 07-26 | C3/C5 two-line R^-6 claim REFUTED by exact witness — and reported to the principal as a headline | hostile review |
| 07-26 | F-8 flag over-promotion ("first half discharged" vs two narrow reproductions) | hostile review |
| 07-26 | three false prose claims (manifest-pins-both; "sole change"; stale disarm docstring) | production-gate audit |
| 07-26 | A-L0 sealed with a first arm my own erratum's witness had already killed | Codex reconciliation |
| 07-26 | fix-(B) F1 probe covered only the controller route, leaving a live write route | production-gate audit |

Pattern of record: the arithmetic/prose defects are caught by review every
time; the structural ones (C3/C5, the live write route) were caught only
by lanes that re-derived from scratch or probed a route I had not. That is
the argument for keeping the no-stubs rehearsal and the independent
re-derivation permanent rather than per-cycle.

## Earlier inherited calibration (prior supervision lane, for continuity)

~12 exact hits / 4 optimism-misses at handoff; all four misses were
"predicted DERIVED where the corpus found an underived step" — errors
pointing toward honesty. The present lane's misses are of a different
character: magnitude scaling, not optimism about derivability.
