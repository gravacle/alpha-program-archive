# Complete-Qspec Periodic Zero-Free Promotion Result v001

Date: 2026-07-25

## Sealed chain

```text
8b47ff6af29537289675dd40d8095a2dc606147a93fb524a3ff659e0aabb6bb7  COMPLETE_QSPEC_PERIODIC_ZERO_FREE_PROMOTION_SPEC_V001.md
3a5c7a7d6b3ed2ae4d9c69feab78bdb34c2222149415e9fa0e8eb5b38f4670f1  COMPLETE_QSPEC_PERIODIC_ZERO_FREE_ZERO_ALIGNMENT_ADDENDUM_V001.md
d8fb2f98290f32c23b2449c111b616ac9e0797688f9b69df0caf8fdbba288881  scripts/certify_complete_qspec_periodic_zero_free_promotion_v001.py
5f6d03dfe789a5df12db9c71665a7defe75cde86b5a588650a11ed4fd6b9550d  stage8_execution/work/QSPEC_periodic_zero_free_promotion_v001.json
```

## Result

The isolated 192-bit Arb execution returned:

```text
FROZEN_DYADIC_PERIODIC_ZERO_FREE_AND_LOG_DENSITY_PROVED
```

Before execution, hostile review found that the original composition
omitted the offset between the unretracted analytic zero and the
polar-retracted certified zero. The sealed addendum required a direct
same-support comparison. The repaired gate certified:

```text
||T_an(0)-A||_2 < 1.269517e-12 < 1e-10.
```

The resulting all-volume bounds are:

```text
graph-map radius                  < 0.0467566 < 0.05
leading coefficient modulus      > 0.764624
largest finite bound, N=6        < 0.112005 < 1
large-volume ratio q             < 0.827392 < 1
relative dominance bound at N=7  < 0.857983 < 1
```

The finite bounds prove nonzero amplitudes for `1<=N<=6`. The spectral
coefficient and decreasing geometric dominance bound prove nonzero
amplitudes for every `N>=7`. Therefore the frozen periodic regulator is
zero-free for every integer volume throughout `|z|<=1/500`.

Uniform leading-mode dominance also proves:

```text
lim_(N->infinity) N^(-1) Log Z_N(z) = Log lambda(z)
```

uniformly on the same disk.

Two separate hostile post-execution reviews checked the sealed output,
zero-alignment repair, interval arithmetic, finite and large-volume
inequalities, and scope. Both accepted the verdict with no blocker.

## Earned status

```text
frozen_dyadic_periodic_zero_free_neighborhood_proved = true
frozen_dyadic_periodic_thermodynamic_log_density_proved = true
continuous_time_parent_zero_free_proved = false
periodic_connected_linked_cluster_density_proved = false
all_stage8_regulators_zero_free_proved = false
all_connected_cellulations_linked_cluster_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

The next distinct obligation is an explicit connected-cluster expansion
with a uniformly absolutely summable majorant. The thermodynamic logarithm
proved here may not be relabeled as that expansion.
