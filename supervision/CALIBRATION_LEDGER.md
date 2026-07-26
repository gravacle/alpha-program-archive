# Prediction Calibration Ledger — running note

Living document (not sealed; anchored with each update), maintained by
the construction/supervision lane on the principal's instruction of
2026-07-26: "Carry a running note of the prediction family's
calibration... Weight future magnitude predictions accordingly, and say
so when making them."

## Standing calibration of this lane's prediction family

```text
SIGN / DIRECTION / OUTCOME-CLASS predictions:  RELIABLE so far.
MAGNITUDE / SCALING predictions:               THREE MISSES (theta_kappa,
                                               gamma P2, control-4 S3(a)).
                                               One magnitude HIT: S3(b) —
                                               and that one predicted a
                                               NULL/bound, not a nonzero
                                               size. EVERY prediction of
                                               HOW BIG A NONZERO EFFECT
                                               WOULD BE HAS MISSED.
BLOCK-vs-DERIVE predictions:                   improving after an early
                                               optimism bias was recorded.
```

RULE IN FORCE: every future magnitude or scaling prediction must be
stated together with this calibration — the citable form is "every
prediction this lane has made about how big a nonzero effect would be has
missed; weight accordingly" — and should be widened relative to the lane's
instinct rather than narrowed. (Superseded wording, recorded because
earlier artifacts quote it: "missed twice consecutively".)

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
| 07-26 | P-L1: the 1/N^2 signature holds AND the factor-4 drop is observed | **PARTIAL** — signature held (every ladder series at least second order, min 3.6959), but the factor-4 drop appeared on only 4 of 8 series; the `all` kernels ran 6.40-6.96, faster than predicted | outcome-class: HIT / magnitude clause: MISS |
| 07-26 | P-S1: response pullback FAILS volume-naturality under slivers, because tau_R is scale-invariant and every refined cell carries a full record cycle | **GROUND REFUTED** — the completed response is the RATIO Z_comp(a)/Z_comp(0) and the record term is a-independent, so it cancels identically before any activity is formed. Conclusion OPEN (R-L2b's exponent is a symbol, not a number). NO CREDIT CLAIMABLE if the conclusion later lands | ground: MISS |
| 07-26 | P-S2: the volume weight survives slivers exactly | HIT — measure additivity; shape is not among its hypotheses. Not claimed as independent credit (agrees with landed P-C8) | outcome-class: HIT |
| 07-26 | P-X4: seal verification from the archive will SUCCEED | **MISS** — the documented procedure fails for 71 of 507 seal files (36/505 by Codex's stricter-scoped test). I had personally hit this bug earlier and misfiled it as a tooling quirk | outcome-class: MISS |
| 07-26 | P-X5: reproduction gaps concentrated almost entirely in re-run-bit-for-bit | SPLIT HIT / concentration clause MISS — the 71 failing seals are a defect in verify-the-record, the leg I predicted clean | partial |
| 07-26 | P-Y2: no control shows a PASS is reachable; the accepting branch has never executed | **HIT, and not found by the independent lane** — the principal calls it the most important sentence in the return | outcome-class: HIT |
| 07-26 | P-Y4: predicted NON-gap — fence controls are over-covered, no fence gap will be found | HIT — a prediction against my own apparatus-building bias | outcome-class: HIT |
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
| P-C8 | D3 object: the volume weight survives slivers and IS derivable from sealed authorities; the response pullback is NOT automatically proved and must remain a checkable obligation | **LANDED on both clauses** |
| P-C7 | Arm-2 C(ii): decay morally present from the free kernel after smooth time integration, but object-level uniform certification over D3 open absent a sealed profile/transversality/projection-tail lemma | **LANDED VERBATIM** |

Running assessment of the independent-system family: P-C3 held; P-C5, P-C6
P-C7 and P-C8 landed with explicit constructions. FOUR CONSECUTIVE CYCLES in
which its predictions held while this lane's magnitude and route-survival
predictions did not. Weight it accordingly when the two disagree — this is
the ledger ground for Rule 6, and Rule 6's expiry is the PRINCIPAL'S
judgment on the reviewer lane's reading of this file, never this lane's.

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
| 07-26 | sealed the arm-2 binding at 09:39, then sealed the spec it binds at 09:56 with ZERO of its markers in it — and ran a seal-time verification that never checked for them. **SECOND** instance of seal-an-obligation-then-fail-to-propagate | hostile review (and a skeptic wrongly refuted it) |
| 07-26 | asserted "3.0e-4 is not in any sealed prose spec" — false; it is in the Phase-A spec at lines 357-361 as `3e-4`. Cause: dropped the `3e-4` alternative from my own grep between two attempts, then published a negative existential from the narrowed pattern | hostile review, then verified against myself |
| 07-26 | claimed the preflight fence self-heal depended on manifest v006; PRECONDITIONS puts fence_at_rest before implementation_manifest — visible in output I had printed myself | hostile review |
| 07-26 | reused the sealed O7/tau_R obstruction ACROSS A TYPING BOUNDARY — it bites on the activity g(C,eps) where there is no normalizing ratio, not on the completed response where the Z_comp(a)/Z_comp(0) ratio deletes it. Same class as universal-vs-represented and operator-vs-scalar — the tripwire I had named ONE ARTIFACT EARLIER | my own sliver attempt, verified against myself |
| 07-26 | review apparatus: `.slice(0,6)` capped adversarial testing at 6 of 55 findings, leaving 29 non-minor untested while the return read "confirmed: 0" | self-caught reading the return |

Pattern of record: the arithmetic/prose defects are caught by review every
time; the structural ones (C3/C5, the live write route) were caught only
by lanes that re-derived from scratch or probed a route I had not. That is
the argument for keeping the no-stubs rehearsal and the independent
re-derivation permanent rather than per-cycle.

SHARPER PATTERN, after 2026-07-26: this lane's defects are no longer
mostly arithmetic. Three of the four newest are FAILURES TO CHECK MY OWN
PRIOR OUTPUT against my own current claim — a binding I had sealed 17
minutes earlier, a grep pattern I had just narrowed, a precondition order
I had just printed. In each case the refuting evidence was already in
front of me. That is not a knowledge gap and more review of the same kind
will not fix it; the fix is a mechanical seal-time check that the
obligations of every artifact this lane has sealed in the current session
appear in the artifact they govern. Recorded as the standing lesson from
the second recurrence.

## Earlier inherited calibration (prior supervision lane, for continuity)

~12 exact hits / 4 optimism-misses at handoff; all four misses were
"predicted DERIVED where the corpus found an underived step" — errors
pointing toward honesty. The present lane's misses are of a different
character: magnitude scaling, not optimism about derivability.
