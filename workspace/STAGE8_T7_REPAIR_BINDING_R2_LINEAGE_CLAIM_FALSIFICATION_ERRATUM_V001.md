# Stage-8 T7 Repair Binding R2 Lineage-Claim Falsification Erratum V001

Date: 2026-07-25 (evening)

## Status

```text
HONEST_BLOCK_APPEND_ONLY_ERRATUM
```

A sealed claim in STAGE8_T7_ACTUAL_PARENT_CAR_IMPLEMENTATION_REPAIR_
BINDING_V001 (seal dc7cdd15…) has been FALSIFIED by an independent
external audit (Fable reviewer lane, relayed by Brian, 2026-07-25;
recorded at /Users/bgm/MB Work/alpha_supervision/
EXTERNAL_AUDIT_2026-07-25_fable_v002_return.md). The sealed binding is
not altered. This erratum records the falsification and its scope.

## The falsified claim

R2's final paragraph ("Fabrication economics") asserted:

> after this gate, a passing bundle's propagators must solve the
> declared generator's ODE to the R3 budgets — which is precisely the
> lineage claim. Colluding fabrication then requires actually
> integrating the declared parent, i.e., performing the computation.

FALSE AS WRITTEN. The v002 lineage gate authenticates propagators
against BUNDLE-DECLARED generator pieces; nothing pins those pieces to
the sealed constructions (M to Q 1_ball Q, B to Q b_D Q, p to Hermite
momenta, alpha/Sn to the sealed spinor convention). The auditor
numerically reproduced a surrogate: zero M, constant diagonal B,
diagonal p/alpha — closed-form exponential "propagators" pass the
lineage gate at 2.9e-15 (48-grid) and 2.1e-14 (384-grid), pass every
internal identity, the convergence ratio, and the sensitivity gate, with
no ODE integration and no contact with the sealed Galerkin parent. This
lane independently confirmed the code facts before sealing this erratum.

The v002 test suite's own genuine-fixture test is an existence proof of
the same fact: its synthetic (non-causal-ball) pieces PASS the full
comparator. The surrogate-pair class was never negative-tested.

## Consequences recorded

1. The "in-band closure" label this binding's R0/R1 language attached to
   custody Section-6 item 2 (generator-to-propagator lineage) is NOT
   EARNED at v002. Until repaired, lineage authenticity rests on
   out-of-band execution custody (manifest, launcher, controller,
   receipts, anchoring) — as the standing-down note originally recorded.
2. R3's discrimination claim holds only against the propagator-twist
   class, not against self-consistent generator-piece substitution.
3. The two verification rounds that returned V002_READY did not detect
   this class (their fabrication fixtures held pieces honest while
   twisting u, or tampered pieces against honest u). Calibration note
   for this lane's review charters: same-model verification missed a
   class that different-family review found — future charters must
   demand surrogate-pair (self-consistent substitution) attacks
   explicitly.

## Repair path (bound separately)

The append-only successor STAGE8_T7_ACTUAL_PARENT_CAR_IMPLEMENTATION_
REPAIR_BINDING_V002 freezes the piece-authenticity mechanism (comparator
reconstructs every generator piece from the sealed spec text with its
own third implementation) and its tolerances BEFORE any repair code is
authored. Production remains prohibited until that repair is authored,
hostile-verified, externally re-audited, and Brian's recorded typed
authorization exists.

## Protected status

```text
actual_parent_regulated_CAR_operator_response_derived = false
generator_to_propagator_lineage_in_band_closed = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
