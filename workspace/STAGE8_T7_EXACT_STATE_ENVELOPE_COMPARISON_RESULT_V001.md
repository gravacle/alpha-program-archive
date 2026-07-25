# Stage-8 T7 Exact-State Envelope Comparison Result v001

Date: 2026-07-24

## Verdict

```text
EXACT_STATE_ENVELOPE_DIAGNOSTICS_VERIFIED
```

The genuine nested Hermite-Galerkin parent was evaluated with:

```text
n in {2,4};
ell in {1,sqrt(2)};
ER-A and ER-B;
exact inherited mixed covariance and finite pure vacuum;
all three completed-record histories;
N_t in {24,48,96}.
```

Every primary time sequence converged at the expected second-order rate and
the secondary spatial quadrature checks passed. ER-A and ER-B yield
materially different raw completed amplitudes; neither was selected.

The independent verifier rebuilt all eight cases with a separately coded
Hamiltonian assembly. It compared:

```text
every N_t=96 history unitary;
every mixed and pure history determinant;
every completed signed sum;
and the worst-cancelled row with 90-digit complex arithmetic.
```

The largest double-precision determinant discrepancies remained below
`2.4e-12`, against the sealed `3e-10` tolerance. In the strongest
cancellation row, whose cancellation factor is `1177.47`, the independent
90-digit evaluation reproduced the completed amplitude to `1.87e-16`.

## Scope

This closes the finite numerical reconstruction and its hostile
cross-verification. It does not turn numerical convergence into a
thermodynamic determinant theorem and it does not choose between ER-A and
ER-B.

```text
exact_state_envelope_diagnostics_verified = true
ER_A_selected = false
ER_B_selected = false
envelope_realization_derived = false
global_determinant_convergence_derived = false
sharp_cell_implementability_proved = false
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```

## Artifacts

```text
4f38691b6f49b01e9d3dc62c4c8d6ed45c6d0f87ddf4cb216ad255f54b604a76  STAGE8_T7_EXACT_STATE_ENVELOPE_COMPARISON_SPEC_V001.md
02bec04a0dc3ec0141a5625cea1ca073de742ee3cb139741b1b3ad52fcfd0019  scripts/derive_stage8_t7_exact_state_envelope_comparison_v001.py
30b311eb97c4553f40f8038b6773b9b082fabf3fb1c037cdef4aacc116130a29  stage8_execution/work/T07_exact_state_envelope_comparison.json
efeea723fd545498b0d19a75de43d97d9e4b84ac29d146ad199ccb8feecff56d  stage8_execution/work/T07_exact_state_envelope_histories.npz
7421c634c5e1733d3a26d8ca8a9b84272152031a2ffcf91f0388366b8a1a6640  scripts/verify_stage8_t7_exact_state_envelope_comparison_v001.py
db0b2f4a8204043ecc61e6cb594d35c1ace883581baea6cf9a7ee25863af802f  stage8_execution/work/T07_exact_state_envelope_comparison_verification.json
```
