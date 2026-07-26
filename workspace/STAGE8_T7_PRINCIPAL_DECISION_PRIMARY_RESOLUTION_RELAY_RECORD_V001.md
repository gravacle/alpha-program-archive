# Stage-8 T7 Principal Decision — Primary-Resolution Successor: Relay Record V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY RELAY RECORD. Verbatim record of the principal's decision of
2026-07-26, together with the cross-family diagnosis (Codex) and the
independent arithmetic verification (Bohm) it rests on. Sealed so the
successor spec can cite this authority BY HASH rather than paraphrase it.
The relay governs over every paraphrase of it anywhere.
```

## The diagnosis, as relayed

```text
"Codex's diagnosis is accepted: the 34 failures are (b), a
tolerance-vs-integrator mismatch, primary finite-step dominated. Bohm
verified the arithmetic independently: observed 4.20627e-4 divided by
1/48^2 = 0.9691 (a clean second-order Strang constant, C ~ 1);
worst/typical = 1.9997 (exactly the 2x tier); the independent lane's raw
192->384 tails are 2.93e-10 / 5.70e-10, i.e. ~738,000x below the observed
gap, so RK4 is definitively not the source. Decisive signature: the
failures occur exactly where the source eigenvalue is NONZERO
(l0/l2 = +-sqrt2) and pass at l1 ~ 0 — Strang splitting error is driven by
the commutator of the split pieces, which vanishes with the source
coupling. This is finite-step error, not a disagreement about physics, and
NOT a spec violation by either lane.

NO BUDGET, TOLERANCE OR THRESHOLD IS REVISED. The 3.0e-4
transported-matrix budget stands exactly as frozen. The remedy is more
computation, not a weaker standard."
```

## The decision, as relayed

```text
"Seal an APPEND-ONLY SUCCESSOR SPEC raising the PRIMARY lane's Strang
resolution. The independent lane is unchanged (its tails are six orders
inside budget). Do not edit any sealed artifact; the successor supersedes
the frozen-numerics resolution row and nothing else.

N IS DERIVED, NOT SELECTED. Record the derivation in the spec, in this
form:
  worst-tier error ~ 1.938 / N^2 (measured constant from the rehearsal,
  second-order Strang);
  require < 3.0e-4  =>  N^2 > 6460  =>  N >= 81;
  the next resolution the frozen doubling scheme admits is N_t = 96.
State explicitly that 96 is reached by this derivation from the FROZEN
budget and the scaling law — NOT by trying values until one passed. That
distinction is the whole legitimacy of this change."
```

## The frozen predictions, as relayed

```text
"P-R1: at primary N_t = 96, the typical failing tier falls to 1.05e-4
      (+-20%), and the worst tier to 2.10e-4 (+-20%). Both under the
      unchanged 3.0e-4 budget.
 P-R2: the error scales as 1/N^2 — doubling N_t reduces every failing
      component by a factor 4.0 (+-15%).
 P-R3: components that PASSED at N_t = 48 remain passing; the l1 ~ 0 rows
      remain unaffected.
 P-R4 (PRE-DECLARED FALLBACK): if the worst tier at N_t = 96 lands above
      3.0e-4 while still exhibiting ~1/N^2 scaling, the next resolution is
      N_t = 192 — declared NOW so that choosing it later is not a post-hoc
      pick. If it is invoked, predict 5.25e-5 typical / 1.05e-4 worst."
```

## The refutation condition, as relayed

```text
"if the discrepancy does NOT drop by ~4x — if it plateaus, or scales
differently, or new components begin failing — then (b) is REFUTED,
diagnosis (a) or (c) reopens, and this is no longer a resolution question
but an implementation or specification defect. Report that outcome as a
finding; do not escalate resolution further to chase a pass. A third
resolution bump without the predicted scaling would itself be evidence
against (b)."
```

## The margin disclosure, as relayed

```text
"at N_t = 96 the worst row clears the budget by only 1.43x. That is thin.
It is accepted because the budget is frozen and the scaling law is
derived, not because the margin is comfortable — and P-R4 exists precisely
so the thin margin does not become a reason to improvise later."
```

## The order of work, as relayed

```text
" 1. Seal the successor spec with the derivation, P-R1..P-R4, and the
     refutation condition — BEFORE any recomputation. Cite Codex's
     diagnosis and Bohm's verification by hash.
  2. Close your three plumbing items in parallel (fence to at-rest 0555
     and find what re-opened it; seal manifest v006; seal the cycle-7
     verification-return transcript).
  3. Re-run the A2 no-stubs rehearsal at primary N_t = 96 in a disposable
     copy. Record every failing component's difference against the frozen
     predictions.
  4. Report the outcome against P-R1..P-R4 explicitly — including any
     prediction that missed, in the calibration ledger, per Rule 6.
  5. Then the package goes to Codex for cycle 8.

Production remains prohibited on both gates. Note additionally that a GO
now requires the comparison to be CAPABLE of passing, which the N_t = 48
rehearsal says it is not — that is the condition this successor exists to
change, and the frozen predictions are how we will know whether it did."
```

## Protected status

```text
principal_decision_relayed = true
diagnosis_accepted = (b)_tolerance_vs_integrator_primary_finite_step
budget_revised = false
transported_matrix_budget = 3.0e-4   (UNCHANGED, FROZEN)
primary_resolution_target = N_t_96
independent_lane_changed = false
predictions_frozen_before_recomputation = required
production_authorized = false
alpha_computed = false
proof_authorized = false
```
