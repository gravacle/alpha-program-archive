# Complete-Qspec Independent Isometry-Stabilization Addendum v001

Date: 2026-07-25

## Purpose

Repair only the identified floating-point loss of zero-history Stinespring
isometry. This addendum does not change a physics operator, a sampled point, a
volume, or any pass threshold.

## Frozen authorities

```text
ef9a85a5cb8da50cd93c534e61846b2bd72944b139facfde3fb0eac355beecbc  COMPLETE_QSPEC_ANALYTIC_CONTINUATION_INDEPENDENT_ZERO_STABILIZATION_ADDENDUM_V001.md
d8cc0409bccc2f815500ec4700f9197339b245806ebf2a90948ecb1a90326370  scripts/verify_complete_qspec_periodic_analytic_continuation_v002.py
75fe2540d4a74cbbc6f7bea039810df5ac48af94e60c8dc6da7a67ed543edd70  stage8_execution/work/QSPEC_periodic_analytic_continuation_verification_v002.json
```

Any mismatch aborts execution.

## Canonical zero-history repair

For each zero-history cell only, stack its Kraus operators vertically to form
the raw Stinespring map `V`. Let `G = V^dagger V`.

The verifier shall:

1. require `G` to be positive definite;
2. require the raw Gram defect to remain below the roundoff budget
   `64 * 96 * d_source * d_record * epsilon_machine`;
3. compute the canonical nearest-isometry retraction
   `V_hat = V G^(-1/2)` using a Hermitian eigendecomposition of `G`;
4. require `||V_hat^dagger V_hat - I||_F < 1e-12`;
5. require `||V_hat - V||_F / ||V||_F < 1e-11`;
6. split `V_hat` back into the same record-indexed Kraus blocks.

The repair is forbidden on every nonzero complex analytic branch. Those
branches retain the independent Taylor implementation unchanged.

## Inherited gates

All v001-protocol and v001-zero-stabilization gates remain binding, including
the zero-history `1e-11` ceiling. The repaired execution must also report the
raw defects, roundoff budget, correction sizes, repaired defects, and the
maximum change relative to the sealed v002 selected-complex diagnostics.

## Fixed status

```text
independent_analytic_continuation_confirmed = false
sampled_point_all_volume_dominance_confirmed = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
