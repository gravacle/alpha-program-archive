# Stage-8 T7 Control-4 v3 Specification V001

Date: 2026-07-26

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

Authorized by STAGE8_T7_GAMMA_GATE_CONTROL4_V3_CONDITIONAL_AUTHORIZATION_
V001 (principal), Condition 1 having returned SAME APPARATUS
(STAGE8_T7_CONTROL4_CONDITION1_SAME_APPARATUS_RESULT_V001). This spec is
Condition 2: every prediction below is frozen BEFORE any execution.

## S0 - Selection history and its compensation (Condition 2(d), stated up front)

```text
This falsifier was SELECTED AFTER THREE DEFEATS. Control 4 v1
(broken-P_x) and v2 (double-symmetry-broken) were both defeated, and
the third defeat produced Lemma L4, which explains why: a-parity is
protected by an antiunitary REALITY CLASS. The class-leaving direction
used here was WITNESSED EFFECTIVE before it was chosen.
THE PRINCIPAL AUTHORIZED IT KNOWING THIS, on the recorded ground that
the foreknowledge objection is dissolvable by commitment rather than a
reason to abandon the question. THE FROZEN PREDICTIONS OF S3 ARE WHAT
RESTORE ITS EVIDENTIAL VALUE. A future reader must weigh the selection
history and this compensation together; neither may be cited alone.
```

## S1 - Scope (binding; the control may not be read as more than this)

```text
CERTIFIES: the teeth proposition — that the Z'(0) reading path on the
  completed-record object is LIVE, hence Lemma 2's Z'(0) = 0 is a fact
  about the object and not a dead instrument.
DOES NOT CERTIFY: A3's original intent, that breaking P_x or Theta
  CAUSES the zero. That intent is known FALSE by L4 and is unachievable
  by any design.
```

## S2 - The frozen falsifier (pinned exactly; no executor discretion)

Sealed carrier and machinery unchanged: Hermite n = 2, ell in {1, sqrt2},
Strang N_t = 48 with scaling-and-squaring exponentials (apparatus note),
sealed quadratures, both pinned finite states, sealed record data
w = (-1/4, 1/2, -1/4) on lambda = (-sqrt2, 0, +sqrt2).

```text
CLASS-LEAVING CONNECTION (the v3 falsifier):
  J'(t) = -( B_D(t) + i * ||B_D(t)||_2 * A_0 ) (x) alpha_x
where A_0 is the FIXED real antisymmetric 8x8 matrix in the sealed
lexicographic spatial basis order (a,b,c):
  A_0[m][n] = +1 if n = m+1 ; -1 if m = n+1 ; 0 otherwise,
  then normalized to ||A_0||_2 = 1.
AMPLITUDE PIN (mandatory): the class-leaving component is at 100% of
  the sealed connection strength, i.e. || i ||B_D(t)||_2 A_0 ||_2 =
  ||B_D(t)||_2 at every t. It may NOT be reduced. Reason of record: the
  reading is exactly linear in this amplitude, so an unpinned amplitude
  makes the prediction vacuous; and the sealed floor 1e-9 sits only
  ~1.9 decades below the expected reading, so a reduced amplitude could
  fall under the floor for reasons unrelated to teeth.
UNBROKEN COUNTERPART: the sealed J(t) = -B_D(t) (x) alpha_x, unchanged.
```

## S3 - FROZEN PREDICTIONS (not revisable after any execution)

```text
(a) BROKEN (class-leaving) reading:
      CENTRAL   |Z'(0)| ~ 1e-6
      WINDOW    1e-8 <= |Z'(0)| <= 1e-4      [+-2 decades, EXPLICITLY WIDENED]
    Derivation: the measured transfer coefficient |Z'(0)|/|dD| is
    0.0091-0.0177 (two normalizations), applied to the witnessed
    positive control |dD| ~ 1e-4.
    THE WINDOW IS WIDENED DELIBERATELY, for three recorded reasons:
      (i)   an 11x envelope spread measured directly (envelope B gives
            8.5e-7 where envelope A gives 7.5e-8 at equal amplitude) —
            the suppression is not a constant of the apparatus;
      (ii)  the witnessed |dD| ~ 1e-4 carries NO recorded normalization
            in any artifact on disk; independent normalizations span
            four decades for the same apparatus;
      (iii) STANDING CALIBRATION: this lane's magnitude predictions
            have MISSED TWICE CONSECUTIVELY while its sign/outcome-class
            predictions have been reliable (CALIBRATION_LEDGER.md). A
            third narrow-window miss would be uninformative.
(b) UNBROKEN counterpart:
      PREDICTED |Z'(0)| <= 1e-18 ; CEILING (pinned) 1e-12.
      Grounds: measured 1.3e-37 (sealed J) and 2.9e-21 (v2 variant).
(c) STRUCTURAL predictions (sign/class — the reliable family):
      per-slot vanishing for the in-class input (no +-lambda
      cancellation); the class-leaving reading occupying the SAME
      (lambda, k) slots; exact linearity in the class-leaving
      amplitude; Lemma 1 (D_{+lambda} = D_{-lambda}) surviving the
      falsifier; a mixed connection giving the same Z'(0) as the pure
      class-leaving part.
```

## S4 - WHAT WOULD REFUTE TEETH (Condition 2(c))

```text
|Z'(0)| < 1e-9 for the pinned class-leaving falsifier at 100% amplitude,
WHILE max_k ||J'(t_k)||_2 > 1e-6 (non-vacuity gate clears) AND
||antisym(Psi)||_F is O(1e-2) (the detector is loaded).
That combination would mean the alpha_x channel is annihilated in BOTH
tau gradings — a FIFTH protection — and the control would have no
teeth. It is not what this lane predicts, and it would be a structural
discovery outranking the control's own purpose.
```

## S5 - Execution protocol (two lanes; commitment-first ENFORCED MECHANICALLY)

```text
1. A fresh-context BLIND lane implements from this sealed text alone
   and writes its commitment DIRECTLY to
   stage8_execution/work/T07_control4_v3_blind_commit_v001.json.
   Standing rule (adopted 2026-07-26): a commitment in a scratchpad is
   NOT a commitment; it seals in the workspace at commitment time.
2. A fresh-context PRIMARY lane implements independently and writes its
   output ONLY to its own scratch directory. It may not write to the
   workspace.
3. The construction lane seals the blind commitment FIRST, verifies no
   primary output exists in the workspace at that moment, and only then
   imports and seals the primary output. Ordering is thereby mechanical,
   not asserted.
4. Neither lane reads the other's outputs; neither runs any production
   lane; no measured constants.
```

## S6 - Consequence rules (from the authorization's Condition 3; not re-decided here)

```text
v3 BITES (within or outside the window, provided the floors are met):
  control-4 is SATISFIED; the gate's control obligation is discharged;
  the gate may be re-run to a verdict under its existing sealed rules.
  GAMMA_REFUTED_NONZERO would then fire from B1 — but the reviewer's
  standing position on the blind-commitment chain still governs whether
  it may be CITED as established refutation evidence.
v3 DOES NOT BITE: recorded as a FOURTH defeated falsifier; the gate
  stays BLOCKED, finally; L4's significance grows.
EITHER WAY: gamma's refutation rests on the STRUCTURAL argument. Beta is
  not contingent on any of this and is already in force.
```

## Protected status

```text
control4_v3_condition2_spec_sealed = true
control4_v3_executed = false
control4_satisfied = false
gamma_refutation_computed = false
alpha_computed = false
proof_authorized = false
```
