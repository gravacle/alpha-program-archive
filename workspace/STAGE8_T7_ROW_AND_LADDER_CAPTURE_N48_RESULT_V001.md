# Stage-8 T7 Row-and-Ladder Capture at Unchanged N_t = 48 — Result V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY RESULT. Discharges O-1, O-2 and O-4 of
STAGE8_T7_PRIMARY_RESOLUTION_SUCCESSOR_SPEC_V001 (0b7b7ea340cf1e22…) and
step (ii) of the principal's revised order of work.
PRIMARY RESOLUTION UNCHANGED AT N_t = 48. NO BYTE-FREEZE SPENT. NO
GENERATION CREATED. NO BUDGET, TOLERANCE, THRESHOLD, QUADRATURE OR BASIS
PIN TOUCHED. CANONICAL WORKSPACE READ ONLY.
PRODUCTION REMAINS PROHIBITED.
```

## Artifacts

```text
STAGE8_T7_ROW_AND_LADDER_CAPTURE_N48_DATA_V001.json      — full capture,
  all 157 comparison rows with difference/tolerance/passed, plus every
  ladder rung. THIS IS THE PROVENANCE THAT WAS MISSING.
STAGE8_T7_ROW_AND_LADDER_CAPTURE_INSTRUMENT_V001.py      — the instrument,
  sealed so the numbers can be re-obtained and the method audited.
```

METHOD, and why it does not disturb anything: the instrument copies the
canonical workspace, sets the copy's fence to 0555, VERIFIES CLOSURE BY
ATTEMPTING A WRITE, runs all three real lanes through the real launcher
v007 and controller v007, and then obtains the row values by calling
**comparator v006's own** `compare_scalar_categories` and
`compare_matrix_categories` on the produced bundles. No comparison is
re-implemented and no tolerance is re-declared; the numbers are the
comparator's own. Lane exits: independent 0, primary 0, comparison 1
(BLOCKED, as at cycle 7).

DISCLOSED DEVIATION from `test_..._real_chain_rehearsal_v001.py`: that
harness OPENS by building manifest v006, and its builder is fail-closed
against overwriting. Because manifest v006 was sealed canonically to close
the cycle-7 verdict's item 2, the copy inherits it and the build step
correctly refuses — the harness cannot now run its first step. This
instrument therefore SKIPS the build and runs against the manifest as it
stands canonically, which is the real production state. Recorded because
closing one item made a sealed test unrunnable, and that is a fact about
the harness, not a weakening of this run.

## PART 1 — V-2's PROVENANCE GAP IS CLOSED, AND EVERY REPORTED NUMBER REPRODUCES

```text
                                    REPORTED (no pedigree)   CAPTURED NOW
rows total                                            157            157
failures                                               34             34
  propagators                                          10             10
  cross_operators                                      24             24
  by oscillator length  ell0                           28             28
                        ell1                            6              6
worst failing difference                        8.411e-4   8.4114758e-4
typical (median) failing difference             4.206e-4   4.2062716e-4
transported rows                                        —            138
passing transported rows                              104            104
worst PASSING transported margin                2.941e-4   2.9411438e-4
transported budget (read from comparator)               —         3.0e-4
EVERY FIGURE THE DERIVATION CONSUMES IS CONFIRMED. Bohm's 4.20627e-4
matches the captured median to six significant figures.
```

### One structural fact the reported breakdown did not contain

```text
THE 34 FAILURES ARE NOT A SPREAD — THEY ARE THREE DISCRETE TIERS:
   8.4114758e-4   x6    2.804x budget
   4.2062716e-4   x22   1.402x budget
   3.2805210e-4   x6    1.094x budget
  tier ratios  t1/t2 = 1.99975   t2/t3 = 1.28220   t1/t3 = 2.56407
THE EXACT 2x STRUCTURE BOHM IDENTIFIED IS CONFIRMED (t1/t2 = 1.99975).
A THIRD TIER AT 1.094x BUDGET WAS NOT IN THE REPORTED BREAKDOWN. It is
recorded here as new: it is the tier that clears the budget most easily
and it does not change the derivation, which is driven by t1.
Discreteness itself supports (b): a physics disagreement would not
generically quantize into three tiers in exact 2 : 1 : 0.78 proportion.
```

## PART 2 — THE CONVERGENCE LADDER, measured by byte-frozen code

The primary lane's own 12 -> 24 -> 48 rungs, as it emits them.
`ratio = ||u_24 - u_12|| / ||u_48 - u_24||`; exact second order = 4.0; the
lane's own frozen gate floor is 3.2.

```text
series                     d_12_24        d_24_48        ratio
ell0__p1__all           4.843192e-09   7.564180e-10    6.4028
ell0__p1__pointer       3.782543e-06   1.019067e-06    3.7118
ell0__p2__all           2.421606e-09   3.782121e-10    6.4028
ell0__p2__pointer       3.782543e-06   1.019067e-06    3.7118
ell1__p1__all           8.808872e-10   1.265328e-10    6.9617
ell1__p1__pointer       7.820175e-08   2.115894e-08    3.6959
ell1__p2__all           4.404453e-10   6.327903e-11    6.9604
ell1__p2__pointer       7.820175e-08   2.115894e-08    3.6959
min 3.6959   max 6.9617   mean 5.1929   n = 8
```

```text
THE SPLIT IS BY KERNEL, NOT BY PAIR, AND IT IS CLEAN:
  every `pointer` series      3.6959 - 3.7118   (second order; inside
                                                 P-R2's band)
  every `all` series          6.4028 - 6.9617   (FASTER than second order;
                                                 above P-R2's band)
Also structural: the `pointer` diagnostics are PAIR-INDEPENDENT — p1 and
p2 give identical d values at both oscillator lengths.
NO SERIES IS SLOWER THAN SECOND ORDER. min = 3.6959 > 3.4.
NO PLATEAU. NO SERIES SCALES DIFFERENTLY IN THE DANGEROUS DIRECTION.
```

## PART 3 — SCORING THE FROZEN PREDICTIONS, honestly and by family

```text
P-R2  "doubling N_t reduces EVERY failing component by a factor 4.0
      (+-15%)", band [3.40, 4.60].
      VERDICT: DIRECTION CONFIRMED; MAGNITUDE NOT CONFIRMED AS WORDED.
      4 of 8 series inside the band; the other 4 at 6.40-6.96 exceed it.
      *** AND A LIMIT ON WHAT THIS INSTRUMENT CAN SAY, STATED RATHER THAN
      GLOSSED: the ladder measures the primary lane's OWN diagnostic
      kernels (gaussian_all / gaussian_pointer), NOT the failing
      transported comparison components (propagators ell0.a*.l*,
      cross_operators ell0.p0.mu*.l*). It is a PROXY for P-R2's object,
      not that object. P-R2 cannot be closed on a proxy, and is recorded
      as DIRECTION-CONFIRMED / MAGNITUDE-OPEN. ***
P-R1  UNTESTED. Requires N_t = 96.
P-R3  UNTESTED. Requires N_t = 96.
P-R4  NOT INVOKED.
THE REFUTATION CONDITION DOES NOT FIRE. It fires if the discrepancy
plateaus, scales differently, or new components begin failing. Nothing
plateaus; every series is at least second order; the failure set is
unchanged at 34 with the same category and ell splits. Diagnosis (b) is
SUPPORTED by provenanced measurement from code with no stake in it.
```

### What the observed rates imply for N_t = 96 — and the useful part

```text
Applying each OBSERVED rate to the worst tier 8.4114758e-4:
  slowest observed  3.6959  ->  2.2759e-4   margin 1.318x   INSIDE P-R1's
                                                            +-20% band
  P-R1's assumed    4.0     ->  2.1029e-4   margin 1.427x   INSIDE
  fastest observed  6.9617  ->  1.2083e-4   margin 2.483x   below the band
                                                            (better than
                                                            predicted)
*** EVEN AT THE SLOWEST RATE THIS INSTRUMENT MEASURED, N_t = 96 CLEARS
THE UNCHANGED 3.0e-4 BUDGET — at margin 1.32x rather than the projected
1.43x. The remedy is bracketed as sufficient from BELOW, not merely
projected. ***
Third tier at the slowest rate -> 8.876e-5. The worst PASSING transported
row is 2.9411e-4 = 0.980x budget, so it too has headroom at 96 and does
not become a new failure candidate under P-R3.
```

## PART 4 — This lane's own predictions, scored separately

```text
P-L1  "the 1/N^2 signature HOLDS and the factor-4 drop is observed"
      PARTIAL. The signature holds — every series at least second order.
      The factor-4 DROP is observed on only 4 of 8 series; the rest are
      faster. Scored PARTIAL, not a hit: the clause said "and the
      factor-4 drop is observed", and half the series exceed it.
P-L2  "at least one component NOT among the 34 moves measurably, without
      crossing tolerance" — UNTESTED at 48 by construction (it is a
      statement about the change to 96).
P-L3  worst tier in 1.6e-4..2.7e-4 at N=96 — UNTESTED, but note the
      bracketing above puts the plausible range at 1.21e-4..2.28e-4,
      whose lower half lies BELOW this lane's window. Recorded now, before
      the test, so that a low outcome counts as a miss rather than being
      reinterpreted afterwards.
Rule 6 note: P-R1..P-R4 are the PRINCIPAL's family and this lane claims no
credit for them. P-L1's partial is this lane's own and goes to the ledger.
```

## PART 5 — The fence re-opened twice more, and one hypothesis is now refuted

```text
Since the cycle-7 closure the canonical fence has been found OPEN (0700)
TWICE MORE — ctime 10:47:08 and again by 10:50:36 — i.e. it does not stay
at rest for tens of minutes. Restored each time; a write-probe confirmed
it was genuinely writable on the second occasion (the probe file was
created and then removed by this lane).
HYPOTHESIS TESTED AND REFUTED: that this lane's own archive `rsync -a`
was the cause. Set to 0555, ran the exact command, re-checked: mode 0555
and ctime UNCHANGED. rsync is not it.
NEW SUPPORTING EVIDENCE for the platform-sync hypothesis, obtained
incidentally: a traceback from inside the tree resolves the canonical root
as `/Users/bgm/Documents/Documents - Brian's MacBook Pro/New project/...`
— the corpus lives inside an iCloud-Drive-synced Documents folder. That
raises the sync hypothesis from speculation to well-supported. THE ACTOR
IS STILL NOT IDENTIFIED AND IS NOT CLAIMED.
CONSEQUENCE, now stronger than at cycle 7: the permission fence CANNOT be
adopted as a passive at-rest barrier. It is re-opened on a timescale of
minutes to tens of minutes by something outside the program. L3 pre-flight
re-assertion is the only protection that survives this, and any B3/B4
adoption must rest on it rather than on the bits.
```

## Protected status

```text
O1_row_capture_discharged = true
O2_ladder_capture_discharged = true
O4_derivation_inputs_confirmed = true
V2_provenance_gap_closed = true
derivation_inputs_reproduce = true
failure_tiers = 3          (6 / 22 / 6 at 2.804x / 1.402x / 1.094x)
third_tier_newly_recorded = true
ladder_min_ratio = 3.6959
ladder_max_ratio = 6.9617
ladder_measures_proxy_not_PR2_object = true
P_R2 = DIRECTION_CONFIRMED_MAGNITUDE_OPEN
P_R1 = UNTESTED
P_R3 = UNTESTED
P_R4 = NOT_INVOKED
refutation_condition_fired = false
diagnosis_b_supported = true
N96_clears_budget_at_slowest_observed_rate = true   (2.2759e-4, 1.318x)
primary_lane_byte_freeze_intact = true
primary_N_t = 48
v003_authored = false
generation_change = none
canonical_fence_reopenings_observed = 3
rsync_hypothesis_refuted = true
fence_viable_as_passive_barrier = false
production_authorized = false
alpha_computed = false
proof_authorized = false
```
