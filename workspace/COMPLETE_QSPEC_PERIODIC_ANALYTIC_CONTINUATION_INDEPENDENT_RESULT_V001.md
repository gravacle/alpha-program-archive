# Complete-Qspec Periodic Analytic-Continuation Independent Result v001

Date: 2026-07-25

## Frozen inputs

```text
85d5a138a1c11dbcfcd85428536afd65bad1f9f6603c7a79c9ad489cd3070e37  COMPLETE_QSPEC_ANALYTIC_CONTINUATION_INDEPENDENT_ISOMETRY_STABILIZATION_ADDENDUM_V001.md
1cd9528bc6872a3a28df828a452a165f8672cccc455a64323edab9e0905bf69d  scripts/verify_complete_qspec_periodic_analytic_continuation_v003.py
f39103452e214c8e0ef29ebeddd884074140a35316c486fadabb12c4b160bf65  stage8_execution/work/QSPEC_periodic_analytic_continuation_verification_v003.json
```

## Verdict

```text
INDEPENDENT_PERIODIC_ANALYTIC_CONTINUATION_CONFIRMED
```

The independent verifier:

- rebuilds the parent, analytic directed factors, derivatives, Kraus maps,
  reachable support, reduced transfer, and spectral decomposition without
  importing the producer;
- uses Taylor scaling-and-squaring for every nonzero complex branch;
- uses Hermitian spectral evaluation and a canonical nearest-isometry
  retraction only for the exactly Hermitian zero-history normalization lane;
- retains every inherited point, volume, and pass threshold.

## Decisive results

```text
complex test points                                  8
zero-history reachable support dimension             5
maximum support-invariance residual                  1.556582229217841e-14
minimum selected-point amplitude, N=1..4             > 0.95
maximum repaired derivative residual                 1.666904213796268e-10
maximum bad-conjugation negative-control residual    about 1.154701
maximum selected-point remainder ratio               < 0.85
maximum all-N sampled-point dominance bound, N>=5     < 1
maximum zero-history error, N=1,2,8,64                1.914909862451447e-14
maximum selected-row change from sealed v002          7.677365821065874e-12
```

The raw zero-history Stinespring defects were about `1.9e-12`. Their canonical
polar corrections were about `1.1e-13`, producing repaired Gram defects below
`2.6e-14`. No complex branch was retracted or normalized.

## Scope

This result independently confirms analyticity, zero-freeness at the sealed
finite sample, and all-volume dominance at the eight sealed boundary points
for the frozen period-two regulator. It does **not** prove:

- a zero-free theorem on every point of the continuous complex disk;
- a connected linked-cluster density for the full disk;
- extension to every pinned Stage-8 regulator or cellulation;
- `kappa_record`, a Thomson stiffness, or `alpha`.

## Fixed status

```text
independent_analytic_continuation_confirmed = true
sampled_point_all_volume_dominance_confirmed = true
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
