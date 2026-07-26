# Stage-8 T7 Step-3 Blocker, the Convergence-Ladder Discovery, and Review Completion V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY. Two items: (1) a STRUCTURAL BLOCKER on step 3 of the
principal's order of work, escalated rather than resolved by this lane;
(2) the completion of the E1 v002 hostile review's refutation pass.
NO SEALED ARTIFACT EDITED. NO FREEZE BROKEN. PRODUCTION PROHIBITED.
```

## PART 1 — N_t = 96 IS NOT A PARAMETER FLIP

The decision authorizes raising the primary lane's resolution and says the
successor "supersedes the frozen-numerics resolution row and nothing else."
Ending a byte-freeze is more than that row, so this is escalated.

```text
WHAT THE PRIMARY LANE ACTUALLY CONTAINS
  derive_..._primary_v002.py:103   RESOLUTIONS = (12, 24, 48)
  :1468-1470  by_resolution[12], by_resolution[24], by_resolution[48]
              — the three rungs are HARD-CODED, not indexed generically
  :1486       production = by_resolution[48]
  :1454-1456  secondary = execute_resolution(..., 48, ...)   — the
              quadrature cross-check, also hard-coded at 48
  :1591-1600  emitted array names embed the rung: diag_primary__{tag}__
              n{steps}__p{pair}__{kernel}, and
              diag_primary_secondary_quadrature__{tag}__n48__...
FREEZE STATUS, VERIFIED: sha256 402d3e988037fa47… IS a row of SEALED
implementation manifest v001, which BOTH derive lanes verify row-by-row at
canonical paths and which the v001-path BRIDGE pins.

THEREFORE N_t = 96 REQUIRES: a new derive-primary v003; a new
implementation manifest; a new generation (G8) with launcher/controller/
comparator allowlist and pin updates; and IT ENDS THE PRIMARY LANE'S
BYTE-FREEZE, on which the bridge and the independent lane's verification
both rest. It also forces two SPEC-LEVEL choices this lane may not make:
  (i) does the ladder become (24, 48, 96), and if so the convergence gate
      is evaluated on different rungs than the one that has been passing;
  (ii) does `secondary` — the same-resolution quadrature cross-check —
      move to 96, or stay at 48 and change meaning?
ESCALATED. This lane will not break a byte-freeze or re-point a
convergence gate on its own authority.
```

## PART 2 — WHAT THE FROZEN LANE ALREADY DOES, discovered while checking the above

This is the useful half, and it was already in the sealed corpus.

```text
THE PRIMARY LANE ALREADY RUNS A TWO-DOUBLING CONVERGENCE LADDER AND GATES
ON SECOND-ORDER SCALING:
  ratio = ||u_24 - u_12|| / ||u_48 - u_24||
  require(ratio >= CONVERGENCE_RATIO_MIN)   with CONVERGENCE_RATIO_MIN = 3.2
  (exact second order would give 4.0; 3.2 is the frozen floor)
  require(d_24_48 > 1.0e-15, "Unresolved primary convergence tail")
  every rung is EMITTED into the bundle as diag_primary__…__n12/n24/n48…,
  and the ratios are recorded in a `convergence` dict.
CONSEQUENCE 1 — P-R2 HAS PROVENANCED SUPPORT THAT PREDATES THIS
DISCUSSION. In the N_t = 48 rehearsal the primary lane SUCCEEDED, so this
gate PASSED, so the lane's own measured doubling ratio was >= 3.2 across
12 -> 24 -> 48. That is second-order Strang behaviour measured by
BYTE-FROZEN CODE on its own sealed output path, produced before the
diagnosis was formed and by an instrument with no stake in it.
CONSEQUENCE 2 — P-R2 CAN BE TESTED WITHOUT N_t = 96 AT ALL. The ladder
already spans two doublings. The factor-4 prediction is checkable on the
existing frozen lane, with no new lane version and no freeze spent.
CONSEQUENCE 3 — THE §6 PROVENANCE GAP IS CLOSABLE THE SAME WAY. Capturing
the comparator's full `rows` plus the emitted ladder in ONE rehearsal at
the UNCHANGED N_t = 48 gives provenance to 8.411e-4 / 4.20627e-4, hence to
C_worst and C_typical, hence to §2's derivation of N — and discharges O-1,
O-2 and O-4 of the successor spec without touching anything frozen.
NOTE, so it is not mistaken for available data: NO primary CAR bundle
exists canonically. Production outputs are ZERO; the only two .npz in
stage8_execution/work are unrelated T07 artifacts. The ladder arrays
existed only inside the disposable rehearsal copy and are gone. Obtaining
them requires re-running the rehearsal (A2, disposable copy, byte-frozen
lane unchanged) — NOT a production run.

RECOMMENDED RE-ORDERING, and the reason: run the A2 rehearsal at the
UNCHANGED N_t = 48 with full row-and-ladder capture FIRST. It costs one
rehearsal, breaks no freeze, needs no new artifact version, and returns
(a) provenance for the derivation's input constants, (b) a measured test
of P-R2 from frozen code, (c) the O-4 re-derivation check. ONLY IF P-R2
HOLDS is it worth spending the primary byte-freeze on a v003 to test P-R1.
If P-R2 fails at 12->24->48, the refutation condition fires BEFORE any
freeze is spent — which is the cheaper place to find out.
```

## PART 3 — E1 v002 HOSTILE REVIEW: refutation pass complete

```text
The capped first pass tested 6 of 55. The completion pass tested the
remaining 30 in topic clusters, same refute-by-default instruction.
  TOTAL TESTED NOW: 36 of 55.  SURVIVED: 5.  KILLED: 25 (this pass).
  19 MINOR findings remain untested and are recorded as such.
STILL NOT A CLEARANCE: the review gate on v002 remains OPEN.
```

### The five survivors

```text
ARM2-BINDING-RETEST  -> CONFIRMED, severity corrected to MINOR.
  The prior refutation is itself refuted: a corpus-wide search of both
  trees returns the binding and its own seal file AND NOTHING ELSE. The
  binding is ORPHANED. Two of its literal mandates are undischarged: v002
  carries no U3-attached projection-tail obligation, and no verdict
  language anywhere states uniform-in-Q vs limit-with-certified-tails.
  WHY SEVERITY DROPS, and this is a real reduction this lane did not
  find itself: U3's OPERATIVE content is already fenced in v002 with
  BLOCK force, harder than the binding asked — F'-5 forbids any constant
  or decay rate depending on carrier index, ell or truncation level;
  B-L2* demands carrier-uniformity with a named witness; D5' requires
  carrier-index-blindness; C2 already records the identical
  finite-on-a-fixed-carrier failure mode. That effectively pins v002 to
  the binding's FIRST option (uniform-in-Q) and forecloses the other.
  The reviewer also CONFIRMED U3 is live, not hypothetical: Q is the
  finite Hermite-Galerkin carrier projector and D6' freezes
  M(t) = Q 1_{|x|<=r(t)} Q inside the sealed record vertex.
  THIS LANE'S DEFECT STANDS AS A PROCESS DEFECT. Its safety consequence
  is smaller than this lane stated. Both facts recorded.

F-T1  -> MAJOR. Every clause survives, against THIS LANE's withdrawn
  claim, and the freeze is STRONGER than even the erratum said: the
  Phase-A prose spec states <=3e-4 five times at :357-361 for exactly the
  gated families, CALLS THEM "preregistered" AT LINE 466, and was sealed
  2026-07-25 — a day BEFORE first real-chain execution.

V-2  -> MAJOR. CONFIRMED, and this lane had already verified the mechanism
  independently: on the blocked path comparator v006 emits only
  {reason, exception_type, the frozen False flags, provenance_paths}. The
  34/104 magnitudes, the 10/24 category split, the 28/6 ell split and the
  2.941e-4 passing margin are obtainable from NOTHING the run sealed or
  printed. The instrument that produced them is unidentified.

L7-2  -> MAJOR, NEW AND SUBSTANTIVE. eta_1 := 2 kappa_bal sup_C g(C,eps)
  e^{X_*} requires sup_C g < infinity. R-L0's stated deliverable is only
  x = |C|_4 g <= X_*, which does NOT imply it once D3 admits |C|_4 -> 0.
  Worse, R-L0's ground (i) as worded — |C|_4 g scale-invariant, i.e.
  weight(g) = -1 — SATISFIES R-L0's letter while FORCING sup_C g = +inf,
  hence eta_1 = +inf and the n=1 leg blocked. Exact witness supplied
  (kappa=1, x == 1/4 at every depth, |C|_4 = 16^-m: g = 1/4, 4, 64, 1024,
  … 1.07e9 — x bounded at every depth while sup_C g diverges).
  PROVENANCE OF THE DEFECT: v001 had g a single cell-independent number,
  so finiteness was automatic; the B-5 per-cell repair introduced sup_C
  WITHOUT adding the corresponding finiteness obligation. A repair
  created it.

F2  -> MINOR. "four surviving constants" (:937, repeated in the author's
  own reviewer instruction at :2318) contradicts the spec's own
  enumerations of FIVE (:951, :2180). Consequence is audit coverage, not
  arithmetic: the instruction tells the auditor to check four when five
  survive, so S1/G_tr falls outside the instructed audit.
```

### What was killed, recorded so the survivors are not read as the whole story

```text
25 of 30 killed. Notably ALL FIVE of the arm-2 factor-(ii) findings
(OA0-2..OA0-6) died as NOT_A_FINDING, as did both A-L5-vs-Q6 findings
(B-A4, B-A5), all three §E1' min findings (E-1, E-2, E-3), V-1, V-3 and
V-6. So: PA-A0 is not under-called on the evidence; the spec's Q6
disclaimer was not shown false; the min composition is not inoperable;
and this lane's V-6 self-defect was judged NOT_A_FINDING by an
independent skeptic — the ERRATUM STANDS AS WRITTEN regardless, because
the precondition ordering it corrects is a fact and the erratum claims
nothing more.
```

## Protected status

```text
step3_as_ordered_executable_by_this_lane = false   (ESCALATED)
primary_lane_byte_freeze_intact = true
primary_lane_v003_authored = false
new_generation_G8_created = false
convergence_ladder_exists_in_frozen_lane = true    (12, 24, 48)
convergence_gate_floor = 3.2
P_R2_testable_without_N96 = true
provenance_of_derivation_inputs_established = false
recommended_next = A2_rehearsal_at_UNCHANGED_48_with_row_and_ladder_capture
hostile_review_tested = 36_of_55
hostile_review_survivors = 5
hostile_review_minor_untested = 19
hostile_review_cleared = false
v002_executable = false
production_authorized = false
alpha_computed = false
proof_authorized = false
```
