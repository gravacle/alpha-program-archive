# Stage-8 T7 Primary-Resolution Successor Spec V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY SUCCESSOR SPEC. SEALED BEFORE ANY RECOMPUTATION.
SUPERSEDES EXACTLY ONE THING: the PRIMARY lane's frozen-numerics
time-resolution row (N_t = 48 -> N_t = 96). It supersedes NOTHING ELSE.
NO SEALED ARTIFACT IS EDITED. NO BUDGET, TOLERANCE OR THRESHOLD IS
REVISED. The independent lane is UNCHANGED.
PRODUCTION REMAINS PROHIBITED ON BOTH GATES.
```

## Authorities

```text
STAGE8_T7_PRINCIPAL_DECISION_PRIMARY_RESOLUTION_RELAY_RECORD_V001.md
  b7f3260f305c8839dfab6362…  — the principal's decision, Codex's
  diagnosis and Bohm's independent arithmetic verification, verbatim.
  THE RELAY GOVERNS OVER EVERY PARAPHRASE IN THIS TEXT.
STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md
  789338adb7d3d36da453113e…  — the sealed Phase-A spec that states the
  transported budgets IN PROSE at lines 357-361 (`<=3e-4`), including the
  two failing families, and adds "No aggregation can hide a component
  failure."
STAGE8_T7_CYCLE7_VERIFICATION_RETURN_AND_FENCE_CLOSURE_V001.md — the
  N_t = 48 rehearsal record whose numbers this derivation consumes.
STAGE8_T7_CONSTRUCTION_LANE_THREE_DEFECT_ERRATUM_AND_REVIEW_
  INCOMPLETENESS_V001.md — withdraws this lane's false claim that the
  budget was not spec-level. It IS spec-level; the freeze is stronger
  than this lane earlier reported.
```

## §1 — THE DIAGNOSIS THIS SPEC RESTS ON

```text
ACCEPTED BY THE PRINCIPAL: (b) tolerance-vs-integrator mismatch, PRIMARY
FINITE-STEP DOMINATED. Not a disagreement about physics. Not a spec
violation by either lane.
THE DECISIVE SIGNATURE, and it is a structural argument rather than a
curve fit: the failures occur exactly where the source eigenvalue is
NONZERO (l0/l2 = +-sqrt2) and PASS at l1 ~ 0. Strang splitting error is
driven by the COMMUTATOR of the split pieces, which vanishes with the
source coupling. An integrator artefact must behave this way; a physics
disagreement need not.
RK4 IS EXCLUDED QUANTITATIVELY: the independent lane's raw 192->384 tails
are 2.93e-10 / 5.70e-10, ~738,000x below the observed gap.
```

## §2 — THE DERIVATION OF N. RE-DERIVED INDEPENDENTLY BY THIS LANE, NOT ACCEPTED ON REPORT

```text
SECOND-ORDER STRANG SCALING, error ~ C / N^2.
CONSTANTS RECOVERED FROM THE N_t = 48 TIERS:
  C_worst   = 8.411e-4   * 48^2 = 1.93789     (relay: 1.938)          OK
  C_typical = 4.20627e-4 * 48^2 = 0.96912     (Bohm: 0.9691)          OK
  worst/typical = 1.99963                     (Bohm: 1.9997)          OK
     — a clean second-order constant of order unity, and an exact 2x tier
       structure. Both reproduce to the digits relayed.
THE REQUIREMENT, against the UNCHANGED frozen budget:
  C_worst / N^2 < 3.0e-4
  N^2 > 1.93789 / 3.0e-4 = 6459.6             (relay: 6460)           OK
  N   > 80.372  =>  N >= 81                   (relay: 81)             OK
  The frozen doubling scheme's next admissible resolution above 81 is
  N_t = 96.
*** 96 IS REACHED BY THIS DERIVATION FROM THE FROZEN BUDGET AND THE
SCALING LAW. IT WAS NOT REACHED BY TRYING VALUES UNTIL ONE PASSED. NO
VALUE OTHER THAN 96 WAS EVALUATED FOR ADMISSIBILITY BEFORE THIS SEAL, AND
THE FALLBACK 192 IS DECLARED IN THIS SAME ARTIFACT RATHER THAN LATER. ***
That distinction is the whole legitimacy of this change, and it is the
reason this spec is sealed BEFORE any recomputation.
```

## §3 — FROZEN PREDICTIONS. Sealed before recomputation; they are the test, not the formality.

```text
P-R1  At primary N_t = 96: typical failing tier -> 1.05e-4 (+-20%);
      worst tier -> 2.10e-4 (+-20%). Both under the unchanged 3.0e-4.
      (This lane's independent re-derivation: 1.0516e-4 and 2.1028e-4.)
P-R2  Error scales as 1/N^2: doubling N_t reduces EVERY failing component
      by a factor 4.0 (+-15%).
P-R3  Components that PASSED at N_t = 48 remain passing; the l1 ~ 0 rows
      remain unaffected.
P-R4  PRE-DECLARED FALLBACK. If the worst tier at N_t = 96 lands above
      3.0e-4 WHILE STILL exhibiting ~1/N^2 scaling, the next resolution is
      N_t = 192 — declared NOW so that choosing it later is not a post-hoc
      pick.
```

### P-R4's magnitudes — ONE CORRECTION, RAISED BEFORE THE SEAL RATHER THAN AFTER

```text
THE RELAY STATES, VERBATIM AND PRESERVED: "If it is invoked, predict
5.25e-5 typical / 1.05e-4 worst."
APPLYING THE DECISION'S OWN 1/N^2 LAW AND ITS OWN CONSTANTS TWICE:
  at N_t = 192:  typical = 0.96912 / 192^2 = 2.6289e-5
                 worst   = 1.93789 / 192^2 = 5.2569e-5
THE RELAYED PAIR IS EXACTLY 2x EACH DERIVED VALUE (2.00x and 2.00x). The
two relayed numbers are individually recognisable: 5.25e-5 IS the derived
WORST at 192, and 1.05e-4 IS the derived TYPICAL at 96 — i.e. the labels
appear shifted by one slot rather than the law being different.
SEALED FORM OF P-R4, and the reason for this choice: a fallback prediction
that contradicts the scaling law it is conditioned on could not test
anything, and P-R4 fires only if P-R2's ~1/N^2 scaling HOLDS.
  P-R4 magnitudes AS SEALED: at N_t = 192, typical 2.63e-5, worst 5.26e-5.
  P-R4 magnitudes AS RELAYED: 5.25e-5 typical / 1.05e-4 worst — preserved
  above, not overwritten.
IF THE PRINCIPAL INTENDED THE RELAYED PAIR, HE RESTATES IT AND THIS
ARTIFACT IS SUPERSEDED. This lane does not silently adopt either version:
both are on the record, the arithmetic ground for the correction is shown,
and P-R4 is a FALLBACK not yet invoked, so correcting it now costs nothing
and correcting it after invocation would have cost the test.
```

## §4 — REFUTATION CONDITION

```text
IF the discrepancy does NOT drop by ~4x — if it PLATEAUS, or scales
DIFFERENTLY, or NEW components begin failing — THEN diagnosis (b) is
REFUTED, (a) or (c) reopens, and this is no longer a resolution question
but an IMPLEMENTATION OR SPECIFICATION DEFECT.
THAT OUTCOME IS REPORTED AS A FINDING. Resolution is NOT escalated
further to chase a pass. A THIRD resolution bump without the predicted
scaling would itself be evidence AGAINST (b), and this artifact forbids
this lane from taking it.
```

## §5 — MARGIN, disclosed here rather than discovered later

```text
At N_t = 96 the worst row clears the frozen budget by only
  3.0e-4 / 2.1028e-4 = 1.427x  (relay: 1.43x)
THAT IS THIN. It is accepted because the budget is FROZEN and the scaling
law is DERIVED — not because the margin is comfortable. P-R4 exists
precisely so the thin margin cannot become a reason to improvise later.
```

## §6 — A BOUND DEPENDENCY THIS SPEC MUST CARRY: the input constant's provenance

This section exists because the immediately preceding erratum recorded
this lane sealing an obligation into an artifact and failing to carry it
into the artifact it governed. It is carried here.

```text
THE DERIVATION IN §2 CONSUMES 8.411e-4 AND 4.20627e-4. THIS LANE HAS
VERIFIED THAT THE COMPARATOR DOES NOT EMIT THEM.
  compare_..._v006.py builds `rows` — every one of the 157 components with
  its exact `difference`, `tolerance`, `passed` — and computes ALL of them
  BEFORE any raise. So the numbers genuinely exist at runtime.
  But the block is `require(not failures, f"{len(failures)} component
  comparison(s) failed")`, which carries ONLY THE COUNT, and `rows` is
  consumed solely on the PASS path (diagnostic_gates and the returned
  dict). ON THE BLOCKED PATH `rows` IS DISCARDED — never printed, never
  sealed.
CONSEQUENCE, STATED PLAINLY: the per-tier magnitudes that C_worst and
C_typical are computed from have NO PROVENANCE IN ANY SEALED ARTIFACT
PRODUCED BY THE COMPARATOR. The arithmetic of §2 is exact given those
inputs, and three lanes have now used them consistently, but this lane
cannot establish their provenance from the sealed corpus. A derivation
from an unprovenanced constant is weaker than it looks, and the legitimacy
claim in §2 is about METHOD, not about the input's pedigree.
BOUND OBLIGATION, MANDATORY, AND ATTACHED TO STEP 3 OF THE ORDER OF WORK:
  O-1 The N_t = 96 rehearsal MUST capture and record the FULL `rows` list
      — all 157 components with difference, tolerance, passed — not just
      the failure count, so that every number P-R1/P-R2/P-R3 is tested
      against HAS provenance.
  O-2 P-R2 is a RATIO against the N_t = 48 baseline. Testing it against an
      unprovenanced baseline would not be a test. The N_t = 48 rows must
      therefore be captured in the same disposable copy and by the same
      instrument, so both sides of the ratio are provenanced and
      commensurable. THIS IS NOT A RE-RUN TO CONFIRM A READING OF THE
      DIAGNOSIS — the diagnosis is accepted and is not reopened; it is the
      establishment of provenance for numbers a frozen prediction depends
      on. If the principal reads it otherwise, O-2 is held and P-R2 is
      reported as UNTESTABLE-AS-SPECIFIED rather than tested loosely.
  O-3 Capture is READ-ONLY with respect to the numerics: no budget,
      tolerance, threshold, quadrature or basis pin is touched, and the
      capture instrument may not alter any comparison.
  O-4 If the captured N_t = 48 worst/typical differ from 8.411e-4 /
      4.20627e-4, the DERIVATION OF N IS RE-DONE from the captured values
      and the result reported — including if it no longer yields 96. The
      frozen predictions above are NOT retro-fitted to new constants;
      they stand as sealed and are scored as they stand.
```

## §7 — Prediction-family attribution, so Rule 6 is applied to the right family

```text
P-R1..P-R4 ARE NOT THIS LANE'S PREDICTIONS. They are the principal's,
frozen on Codex's diagnosis and Bohm's verification. This lane's own
magnitude record — every prediction it has made about how big a nonzero
effect would be has missed — DOES NOT ATTACH to them, and this lane will
not claim credit for them if they land.
WHAT THIS LANE PREDICTS, ON ITS OWN ACCOUNT AND SCORED SEPARATELY, stated
with its calibration as Rule 6 requires:
  P-L1 (OUTCOME-CLASS) The 1/N^2 signature HOLDS and the factor-4 drop is
       observed. Confidence: moderate-high. GROUND: the l1 ~ 0 pass /
       l0,l2 nonzero fail signature is a commutator signature, and the
       recovered constant is O(1) rather than tuned.
  P-L2 (OUTCOME-CLASS) At least one component NOT among the 34 moves
       measurably, because changing the primary time grid changes every
       transported object, not only the failing ones. This does NOT
       violate P-R3 unless such a component CROSSES its tolerance.
       Confidence: moderate. Stated because P-R3 as worded could be read
       as predicting no movement at all, and this lane reads it as
       predicting no new FAILURES.
  P-L3 (MAGNITUDE, and stated with the calibration) The worst tier lands
       in 1.6e-4..2.7e-4. WIDER than P-R1's +-20% band deliberately: every
       magnitude prediction this lane has made about the size of a nonzero
       effect has missed, so this window is widened relative to instinct
       rather than narrowed. A landing inside it should be credited WEAKLY.
```

## §8 — Order of work, with current state

```text
1. SEAL THIS SPEC BEFORE ANY RECOMPUTATION.               <- DONE by this
                                                             artifact.
2. THE THREE PLUMBING ITEMS.                              <- ALREADY
   CLOSED BEFORE THIS DECISION ARRIVED, and recorded in
   STAGE8_T7_CYCLE7_VERIFICATION_RETURN_AND_FENCE_CLOSURE_V001.md:
     fence restored to at-rest 0555, verified by attempting a write, and
       the at-rest assertion fires with three witnesses;
     WHAT RE-OPENED IT: not a program route. All three candidate causes
       are excluded on the observed mode value — every program path sets
       0o555 or 0o755 and never 0o700 — and of 279 directories in the
       tree exactly two deviated, precisely the two the fence had set,
       both at the identical second. External agency; actor not
       identified and not claimed.
     manifest v006 sealed: 642d10c0…, 12 rows, through the authorized
       raise, coherence resolving to PREFLIGHT_OK;
     cycle-7 verification return sealed with its actual numbers, plus the
       author lane's return verbatim at 027708f0….
3. RE-RUN THE A2 NO-STUBS REHEARSAL AT PRIMARY N_t = 96 in a disposable
   copy, under O-1..O-4 of §6.                            <- NEXT.
4. REPORT AGAINST P-R1..P-R4 EXPLICITLY, including any prediction that
   missed, in the calibration ledger, per Rule 6 — scoring the
   principal's family and this lane's P-L1..P-L3 SEPARATELY.
5. PACKAGE TO CODEX FOR CYCLE 8.
```

## Protected status

```text
successor_spec_sealed_before_recomputation = true
supersedes = primary_lane_time_resolution_row_only
primary_N_t = 96
independent_lane_unchanged = true
budget_revised = false
transported_matrix_budget = 3.0e-4
budget_frozen_in_sealed_prose_spec = true
budget_frozen_in_sealed_manifest = true
N_derived_not_selected = true
values_evaluated_for_admissibility_before_seal = 96_only
fallback_declared_in_advance = N_t_192
P_R4_magnitudes_corrected_at_seal = true
P_R4_relayed_magnitudes_preserved = true
input_constants_provenance_established = false      (§6, BOUND)
O1_O4_bound_to_step_3 = true
refutation_condition_sealed = true
third_resolution_bump_forbidden_without_scaling = true
worst_tier_margin_at_96 = 1.427x
predictions_frozen = P_R1..P_R4 (principal) + P_L1..P_L3 (this lane)
rehearsal_at_96_executed = false
production_gate_verdict = NO_GO
comparison_capable_of_passing = false               (the condition this
                                                     spec exists to change)
production_authorized = false
alpha_computed = false
proof_authorized = false
```
