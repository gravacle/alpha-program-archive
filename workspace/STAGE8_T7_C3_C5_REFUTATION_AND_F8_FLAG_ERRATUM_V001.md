# Stage-8 T7 Errata — C3/C5 Refuted; F-8 Flag Over-Promotion Corrected V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY_ERRATA — TWO DEFECTS IN THIS CONSTRUCTION LANE'S OWN SEALED
ARTIFACTS, ONE OF WHICH WAS ALSO REPORTED TO THE PRINCIPAL AS FACT
```

Issued on two hostile reviews returning NOT_READY and
F8_GATE_NOT_DISCHARGED (transcripts sealed at
/Users/bgm/MB Work/alpha_supervision/E1_SPEC_HOSTILE_REVIEW_SEALED_
TRANSCRIPT_V001.md, d95c7a16…, and .../F8_SECOND_HALF_REVIEW_SEALED_
TRANSCRIPT_V001.md, 3cacd4b7…). No sealed artifact is altered; these
errata govern how the named artifacts are read.

## ERRATUM 1 — C3 and C5 are REFUTED by exact witness

```text
REFUTED CLAIM (sealed as correction C5, and asserted in C3):
  "the lowest connected two-cell cumulant is a TWO-LINE object; hence
   the pair activity carries R^-6, not R^-3; the long-distance direction
   has margin; clustering was never the missing ingredient."
```

WHY IT IS FALSE. The claim rested on writing V - 1 = X_1 + X_2 with each
X_i diamond-supported. That decomposition is NOT exact for relay-ordered
cell evolutions: V^(12) = V_2 V_1, so

```text
V^(12) - 1 = Y_1 + Y_2 + Y_2 Y_1,      Y_i = V_i - 1,
```

and the Moebius difference of the LINEAR (trace) term leaves
tr[C Y_2 Y_1 C] != 0. The reviewer's exact computation (exact Fractions,
rank-3 rational projector, n = 6) gives at order eps^2:

```text
Phi_12(eps^2)                        = -346463176730651/17428667193612
  -tr[C Y_2 Y_1 C]   (ONE sea line)  = -1337849531/65078154
  +tr[C Y_1 C Y_2]   (TWO sea lines) = 35484269897501/52286001580836
eps^2 == oneline + twoline : TRUE
eps^2 == twoline alone    : FALSE
one-line term identically zero : FALSE
```

So the lowest connected two-cell cumulant is
Phi_12 = -tr[C Y_2 Y_1] + tr[C Y_1 C Y_2] + O(Y^3) — TWO terms at the
SAME order, only one of which is two-line. The one-line term carries a
SINGLE sea-kernel factor (R^-3) plus free propagation between cells.
Y_2 Y_1 = 0 holds only in the strict equal-time multiplication-operator
idealization with disjoint supports; the actual V_i - 1 are Dyson-dressed
by free h_0 propagation across the whole interval.

CONSEQUENCES, recorded without softening:

```text
1. C5's "the long-distance direction has margin" and "clustering was
   never the missing ingredient" are UNPROVEN.
2. C3's dismissal of NC3 ("a one-line counting artifact; says nothing
   about E1") is NOT ESTABLISHED. NC3 may be precisely the control that
   detects the one-line term. Its exact 24 H_K divergence is back in
   play.
3. IR-A's n >= 2 leg would certify a bound on the WRONG OBJECT, making
   the E1 spec's own predicted verdict
   E1S_N_GE_2_CERTIFIED_BLOCK_ISOLATED_TO_N1 FALSE-POSITIVE-CAPABLE.
4. The E1 spec froze C3/C5 as non-re-litigable inputs and fenced
   executors away from the correct algebra. That freeze should never
   have been placed.
```

CORRECTION TO THE PRINCIPAL, stated plainly: this lane reported the
two-line R^-6 result to Brian as a headline finding of the IR memo
("the connected two-cell cumulant is a TWO-LINE object decaying as
R^-6 … clustering was never the missing ingredient"). THAT REPORT WAS
WRONG. The one-line sea term survives at the same order. The memo's
one-line summary (51f655a0…) and the C1-C6 artifact (6c3e125b…) are
corrected of record by this erratum.

WHAT SURVIVES of C1-C6: C1 (the sea covariance is pinned exactly, with
closed-form kernel) and C2 (Phase-1's K_sea is divergent as defined, not
merely uncertified) are untouched by this finding. C4 (m0 = m1 = 0, the
exact second-difference structure, and its exact saturation at full
tau_R) is untouched. C6 (the block involves the sharp localizer against
the marginal sea) is untouched and is now MORE central, not less.

## ERRATUM 2 — F-8 flag over-promotion in this lane's result artifact

```text
DEFECT (drift class): STAGE8_T7_F8_FIRST_HALF_RESULT_AND_TWO_NEW_
FINDINGS_V001 asserts
    F8_rederivation_first_half_discharged = true
and the prose "The F-8 gate's first half (fresh-context re-derivation) is
discharged." THE TRANSCRIPT NEVER CLAIMED THAT. It asserted exactly two
narrow flags:
    F8_rederivation_first_half_lemma0_reproduced = true
    F8_rederivation_routeQ_independence_reproduced = true
and its own obstruction list contradicts the wider claim.
CORRECTED STATUS OF RECORD:
    F8_rederivation_first_half_discharged = FALSE
    F8_gate_discharged                    = FALSE
Two narrow reproductions were achieved; the gate was not discharged.
```

Additionally, per the review: sealed F-8 clause (3) (re-derive the O3
certificates AND the W1 enclosure without the primary's worksheets) is
UNDISCHARGEABLE BY EITHER LANE at this time — O3's half is moot under the
re-scope, but W1's half is not, and the re-scope is silent on O9/W1.
Phase A must execute first. This is a SEQUENCING FACT, not a lane
failure, and it means the F-8 gate cannot close before Phase-A
production.

## ERRATUM 3 — Q6 is worse than recorded; and one anti-conflation error

```text
Q6: real + underived, and MATERIALLY WORSE than this lane recorded —
  "refuted as stated under the natural adjacency relation". It is NOT
  derivable from sealed material. The blocker must be RE-CAST, not
  retired and not carried forward as written.
3/8 DISAMBIGUATION: the re-derivation lane's separation of the three
  distinct roles of the rational value 3/8 is WRONG on one of the three
  pairings (an anti-conflation error). It points the same direction as
  the verdict, so no verdict changes; recorded so the corpus does not
  inherit the error.
UPHELD: ROUTE_Q_INDEPENDENT survives a fourth refutation attempt the
  re-derivation lane did not run. The O1-display forcing is CONFIRMED
  (the re-derivation's coverage was incomplete; the reviewer closed it).
  Leakage check CLEAN.
```

## Consequences for live work

```text
E1 SUCCESSOR SPEC (9cfafde1…): NOT_READY. It may not be executed. Its
  repairs require demoting C3's no-cross-term clause to a numbered
  obligation (prove Y_2 Y_1 = 0 on the sealed forms, or bound
  tr[C Y_2 Y_1 C] with certified separation decay uniform over D3;
  witness E1_ONE_LINE_CONNECTED_CROSS_TERM_UNCERTIFIED), restating C5
  and the affected lemmas to the two-line SECTOR only, recasting NC8 as
  a two-sector control, plus the further blocking findings B-2/B-3/B-4
  and the conditions in the sealed transcript.
MAJORANT ARM: the re-scope (Q1/O7 retirement) is UNAFFECTED — Route-Q
  independence is upheld. But the arm's F-8 gate is NOT discharged and
  cannot be until Phase A executes.
```

## Protected status

```text
C3_no_cross_term_claim = REFUTED
C5_long_distance_margin_claim = UNPROVEN
F8_rederivation_first_half_discharged = false
F8_gate_discharged = false
route_Q_independence_reproduced = true
O1_display_nested_reading_forced = true
Q6_recast_required = true
E1_successor_spec_executable = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```
