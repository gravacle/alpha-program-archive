# Stage-8 T7 Gamma-Refutation Gate Result V001

Date: 2026-07-26

## Verdict (per the sealed frozen rule; any control failure blocks)

```text
GATE_BLOCKED
witness: CONTROL4_V2_DESIGN_DEFECT_REALITY_CLASS_PROTECTION
```

The gate's computation completed in full and its deciding quantity is
certified; the gate nevertheless BLOCKS because negative control 4 (v2)
cannot be satisfied by any conforming implementation. Per the sealed
control-4 amendment's own clause — "if yet another symmetry protects the
broken variant, the gate blocks again with a new named witness; every
such block is itself a structural discovery and is preserved" — this is
the anticipated branch, and the discovery is Lemma L4 (sealed separately
in STAGE8_T7_RECORD_PARITY_LEMMAS_RESULT_V001).

## What the control failure means (and does not)

The doubly-broken falsifier (b_D displaced to x_0 = 1/10 AND J scaled by
the time-asymmetry factor 1 + t/3) DOES break both targeted symmetries —
P_x-conjugation residual 1.82e-6, Theta residual 2.25e-8, against
unbroken counterparts ~3e-15 — yet |Z'(0)| remains at noise (3.02e-13
pure / 3.12e-14 mixed) against the required >= 1e-9 floor. Both lanes
independently established WHY: a-parity is protected by the antiunitary
REALITY CLASS of L4, which no perturbation keeping J in the class can
break. Verified not-an-apparatus-artifact by finite differences (<= 2e-13)
and by a positive control (a complex-Hermitian spatial connection factor,
outside the class, yields |dD| ~ 1e-4 under the same apparatus).

A falsifier that actually has teeth must leave the reality class. That is
a control-DESIGN question, and per the sealed amendment its resolution
belongs to the principal.

## Preserved computation (complete; not a verdict)

Both lanes computed the deciding quantity in exact/certified arithmetic
with entirely independent implementations (primary: certified Van Loan
triple for v_B + record-Dyson partial sums with pi^(N+1)/(N+1)! tails for
v_A; blind: exact 6-dim multiplicity reduction + 208-bit ball arithmetic):

```text
B1 deciding state (pure sea, kernel excluded), fixture, R4 cluster:
  primary  Re[Delta_Xi] = -0.002195149493896592  (+- 5.75e-11 certified)
  blind    Re[Delta_Xi] = -0.002195149493896619  (+- 1.83e-12 certified)
  inter-lane agreement                          = 2.69e-17
  both certified enclosures EXCLUDE ZERO; Im also excludes zero
  (primary +4.7846338846e-4, blind +4.7846338846e-4).
  No ZERO_DENOMINATOR (|F_v - F(0)| ~ 1). No RE_IM_CORNER.
B2: exact symbolic proof of the pinned identically-zero expectation
  (log D affine in a => H == 0 => Xi == 0, both envelopes). Delta_Xi = 0.
B3 (corrected assembly): kappa_A = 0.7070882 +- 3.6e-11 (certified),
  kappa_B = 0.5340003 (exact closed form), difference 0.1730879 certified
  nonzero — control 5 PASS, and the amendment's corrected toy values
  (0.707 / 0.534 / 0.173) confirmed symbolically by both lanes.
Exact reductions established: F(0) = e^{2i sqrt3}; H(0)_pure = 0;
  H(0)_mixed = -1/9 (sympy-verified).
```

Had the control behaved, GAMMA_REFUTED_NONZERO would have fired from B1
alone. It did not fire, and this artifact does not claim it.

## Standing position on gamma (honored of record)

The external reviewer's position stands: until the blind-commitment chain
is accepted, gamma is NOT established as refuted by computation. With the
gate additionally BLOCKED on control design, the position is unchanged
and unambiguous:

```text
gamma's refutation is carried by the route memo's STRUCTURAL argument
(exact counterexample; the chiral anticommutation transmitting the
envelope's cumulative profile into the lambda-even Hessian), NOT by this
gate. No artifact may cite this gate as established refutation evidence.
```

## Calibration record (frozen predictions)

```text
P1 (NONZERO): consistent with the certified B1 enclosures — but the gate
   verdict is BLOCKED, so P1 is recorded as CONSISTENT, not CONFIRMED.
P2 (magnitude ~ ||J||^2 with an O(1e-1)-O(1) coefficient): MISSED.
   Measured |Delta_Xi| / ||J||^2 = 0.0202 (primary) / 0.0198 (blind) —
   below the predicted window. Recorded honestly; this is the second
   consecutive magnitude-scaling miss by this lane's prediction family.
```

## Escalation to the principal

```text
1. CONTROL-4 DESIGN (third falsifier design defeated): a teeth-bearing
   falsifier must break the L4 reality class itself (e.g. a
   complex-Hermitian spatial connection factor, witnessed effective at
   |dD| ~ 1e-4). Whether to author control-4 v3 on that basis, or to
   accept the gate's BLOCKED verdict with L4 as the explanation, is the
   principal's decision.
2. BETA (disposition item 3) was made contingent on "the kill-test
   returning nonzero". The COMPUTATION returned certified nonzero; the
   GATE returned BLOCKED. This lane does not resolve that gap and does
   NOT seal the beta adoption artifact on its own authority.
```

## Protected status

```text
gamma_refutation_computed = false
ER_A_selected = false
ER_B_selected = false
envelope_realization_derived = false
record_parity_lemmas_sealed = true
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```
