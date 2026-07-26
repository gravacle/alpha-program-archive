# Stage-8 T7 v003 Authorization, Sub-Question Clearance, and Frozen Direct Predictions V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY. SEALED BEFORE derive-primary v003 IS AUTHORED AND BEFORE ANY
RUN AT N_t = 96, as condition A3 requires.
NO SEALED ARTIFACT EDITED. v002's BYTE-FREEZE STANDS AS A FACT ABOUT THAT
FILE. PRODUCTION REMAINS PROHIBITED ON BOTH GATES.
```

## §1 — The authorization and its five binding conditions, as relayed

```text
AUTHORIZED: author derive-primary v003 at N_t = 96, with a new manifest and
generation as required.
A1  v002 IS NOT EDITED. "The freeze on v002 stands; production moves to
    v003" — NOT "the freeze is ended." v002 remains verifiable against
    manifest v001 forever.
A2  v003's SOLE functional change is the resolution ladder and what
    mechanically follows from it (array names, by_resolution keys). No
    numerics, quadrature rule, ordering, convention, tolerance or
    threshold may change. Every diff v002->v003 enumerated and classified;
    any change not classifiable as ladder-mechanical IS A FINDING, NOT A
    DECISION.
A3  Frozen predictions P-D1..P-D3 sealed BEFORE running. (§4 below.)
A4  v003 GETS ITS OWN FULL AUDIT BEFORE PRODUCTION. It is a new,
    less-audited lane in the production path — "that is the actual cost
    being paid here and it must be paid, not assumed."
(a) THE LADDER MOVES TO (24, 48, 96) — the convergence gate must bracket
    the PRODUCTION rung. DISCLOSED, as required: the gate is thereby newly
    exercised at rungs that have not been the passing ones, and its >= 3.2
    threshold is UNCHANGED — not retuned for the new rungs, because
    retuning it would be the move this program has refused throughout.
(b) THE QUADRATURE CROSS-CHECK MOVES TO 96.
```

## §2 — SUB-QUESTION (b): checked before implementing, as instructed. NO COST TO REPORT.

The instruction was to stop and bring the cost if moving the cross-check
alters what it certifies. It does not, and the reason is measurable.

```text
WHAT THE CROSS-CHECK ACTUALLY IS, read from v002:
  production = execute_resolution(ell, 48, PRIMARY_QUADRATURE,   ...)
  secondary  = execute_resolution(ell, 48, SECONDARY_QUADRATURE, ...)
  PRIMARY_QUADRATURE   = (10, 10, 20)
  SECONDARY_QUADRATURE = (12, 12, 24)
It is a SAME-TIME-RESOLUTION, DIFFERENT-QUADRATURE comparison. Its meaning
is "quadrature sensitivity AT THE PRODUCTION RUNG". Moving both legs to 96
preserves that meaning exactly — it remains the same-resolution,
different-quadrature probe, now at the rung actually in production. The
principal's reasoning is correct and there is no meaning change.

AND THE MAGNITUDE, MEASURED FROM THE SEALED BUNDLE rather than assumed:
  ell0__p1__all      1.652619e-09      ell0__p1__pointer  1.759129e-14
  ell0__p2__all      8.263220e-10      ell0__p2__pointer  8.810546e-15
  ell1__p1__all      6.323877e-10      ell1__p1__pointer  1.567343e-16
  ell1__p2__all      3.162082e-10      ell1__p2__pointer  1.219236e-16
  MAX = 1.652619e-09 = 0.0000x the 3.0e-4 budget, and 1.97e-6 of the worst
  failing component.
CONSEQUENCE: quadrature error is FIVE TO SIX ORDERS too small to be a
floor under the 34 failures, so raising N_t cannot be defeated by a
quadrature-limited plateau. This was a live risk to P-D2 that no lane had
named; it is now measured and excluded rather than assumed away.
```

## §3 — A QUANTITATIVE LAW, and a PRECISE CORRECTION to the relayed signature

The relay states the decisive signature as: "the failures occur exactly
where the source eigenvalue is NONZERO (l0/l2 = +-sqrt2) and pass at
l1 ~ 0." **That is not exactly right, and the exact rule is better.**

```text
WHAT THE CAPTURED ROWS ACTUALLY SHOW. Six of the 34 failures ARE at l1
(ell0.p0.mu0.l1, ell0.p0.mu2.l1, ell0.p1.mu0.l1, ell0.p1.mu2.l1,
ell0.p2.mu0.l1, ell0.p2.mu2.l1), each at 4.206272e-4 = 1.402x budget. So
"passes at l1" is false as stated. The l1 rows are not exceptions — they
are cross operators whose OTHER slot (mu0 or mu2) is nonzero.

THE EXACT RULE, with lambda = (+sqrt2, 0, -sqrt2) on slots (0, 1, 2), and
|dlam| the difference of the two coupled slots (for a single-slot
propagator, |lambda| itself):

  |dlam|      class            n    difference range              verdict
  0           diagonal / l1   28    3.07e-13 .. 6.16e-09          ALL PASS
  sqrt2       one slot zero   44    1.640273e-4 .. 4.206272e-4    MIXED
  2 sqrt2     (+ , -) pair    12    3.280521e-4 .. 8.411476e-4    ALL FAIL

  worst at 2 sqrt2 / worst at sqrt2 = 8.4114758e-4 / 4.2062715e-4
                                    = 1.99975
  min  at 2 sqrt2 / min  at sqrt2 = 3.280521e-4 / 1.640273e-4 = 2.00000
*** THE DIFFERENCE IS LINEAR IN |dlam|. The tier ratio t1/t2 = 1.99975 is
not a coincidence of magnitudes — it is 2sqrt2 : sqrt2 = 2 : 1, predicted
by the spectrum. ***
THIS IS STRONGER EVIDENCE FOR (b) THAN THE RELAYED SIGNATURE, because it
is quantitative: Strang splitting error is driven by the commutator of the
split pieces, the commutator is linear in the coupling difference, and the
measured differences are linear in |dlam| across the whole population.
The MIXED band at |dlam| = sqrt2 is explained by a second discrete factor
(the ell / slot constant) that scales BOTH classes identically — which is
why the minima also stand in exact 2 : 1 ratio.

AND IT SETTLES THE N-INDEPENDENT-OFFSET QUESTION, which the ladder could
not: the ladder's difference-of-successive-rungs is INSENSITIVE to a
constant offset (a constant cancels in u_24 - u_12), so no ladder ratio can
exclude one. The |dlam| = 0 rows CAN: an offset from quadrature, a
convention mismatch, a basis error, or a genuine physics disagreement would
afflict them equally, and they sit at 3.07e-13 .. 6.16e-09.
  ANY N-INDEPENDENT OFFSET IS BOUNDED BY ~6.16e-9 — five orders below the
  budget and ~7.3e-6 of the worst failure. Essentially the ENTIRE
  discrepancy is the coupling-dependent term. That is what Strang error is.
```

## §4 — FROZEN PREDICTIONS (A3). Sealed before v003 exists and before any run.

```text
P-D1  The 34 FAILING TRANSPORTED COMPONENTS THEMSELVES scale at rate
      >= 3.6959 (the slowest series rate measured on the N_t=48 ladder),
      giving worst tier <= 2.2759e-4 and typical <= 1.1381e-4, both under
      the unchanged 3.0e-4 budget.
P-D2  The failure count goes to ZERO at N_t = 96; the three-tier structure
      DISAPPEARS rather than shrinking while remaining above budget.
P-D3  The 104 currently-passing transported rows remain passing, and the
      worst passing row (2.9411438e-4 = 0.980x budget) GAINS headroom
      rather than losing it.
REFUTATION CONDITION, binding: if the failing components' own rate is
below 3.6959, OR any component remains above budget, OR a
previously-passing row fails — (b) IS REFUTED AT THE DIRECT TEST and this
becomes an implementation or specification question, not a resolution one.
*** DO NOT ESCALATE TO N_t = 192 TO CHASE A PASS. REPORT THE REFUTATION. ***
```

### This lane's own predictions on the direct test, scored separately (Rule 6)

```text
P-M1  (OUTCOME-CLASS) P-D2 holds: zero failures at 96. Confidence HIGH —
      higher than for P-D1's rate clause, because zero failures needs only
      rate >= 2.804 (8.4114758e-4 / 3.0e-4), which is well below every
      rate measured. Ground: the |dlam| law plus the ~6e-9 offset bound
      leave no N-independent term to plateau on.
P-M2  (OUTCOME-CLASS) The |dlam| linearity SURVIVES at 96: the surviving
      differences stay in 2 : 1 ratio between the 2sqrt2 and sqrt2
      classes, and the |dlam| = 0 rows stay at ~1e-9 or below, unchanged,
      because they carry no commutator term. Confidence HIGH.
P-M3  (MAGNITUDE, stated with this lane's calibration — every prediction
      it has made about how big a nonzero effect would be has missed;
      weight accordingly and credit a landing WEAKLY) the failing
      components' own measured rate lands in 3.6 .. 7.0, i.e. this lane
      predicts the direct rate is NOT below the ladder's slowest series.
      Window deliberately spans the full range of ladder rates rather than
      being narrowed to the pointer cluster.
```

## §5 — Two recorded patterns

```text
CLOSING ONE ITEM BROKE ANOTHER. Sealing manifest v006 to close the
cycle-7 verdict's item 2 made the sealed rehearsal harness UNRUNNABLE: it
opens by BUILDING v006 and its builder is fail-closed against overwriting.
Recorded as its own pattern, per the principal.
FENCE CAUSE IDENTIFIED BY THE REVIEWER: FXICloudDriveDocuments = 1, the
workspace under ~/Documents/Documents - Brian's MacBook Pro/..., i.e.
inside iCloud Desktop-and-Documents sync, which resets the mode bits.
Accepted. B3/B4 adoption rests on L3 pre-flight re-assertion, not on the
bits. No relocation ordered; no eviction markers exist; seals catch content
changes regardless.
```

## Protected status

```text
v003_authorized = true
v003_authored = false
v002_byte_freeze_stands = true          (production MOVES; freeze not ended)
subquestion_a_decided = ladder_24_48_96
subquestion_a_threshold_retuned = false            (3.2 UNCHANGED)
subquestion_b_decided = quadrature_crosscheck_at_96
subquestion_b_meaning_preserved = true
subquestion_b_cost_to_report = none
quadrature_floor_max_measured = 1.652619e-09
n_independent_offset_bound = 6.16e-09
delta_lambda_linearity_established = true          (ratio 1.99975 vs 2)
relayed_signature_corrected = true                 (6 failures ARE at l1)
P_D1_P_D2_P_D3_frozen_before_run = true
P_M1_P_M2_P_M3_frozen_before_run = true
escalation_to_192_to_chase_a_pass = FORBIDDEN
A4_v003_full_audit_before_production = required_not_yet_performed
production_authorized = false
alpha_computed = false
proof_authorized = false
```
