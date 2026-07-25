# Complete-Qspec Analytic-Continuation Independent Preflight Failure v002

Date: 2026-07-25

## Sealed execution

```text
d8cc0409bccc2f815500ec4700f9197339b245806ebf2a90948ecb1a90326370  scripts/verify_complete_qspec_periodic_analytic_continuation_v002.py
75fe2540d4a74cbbc6f7bea039810df5ac48af94e60c8dc6da7a67ed543edd70  stage8_execution/work/QSPEC_periodic_analytic_continuation_verification_v002.json
```

## Verdict

```text
INDEPENDENT_PERIODIC_ANALYTIC_CONTINUATION_BLOCKED
```

The Hermitian spectral half-step repair passed:

```text
zero-history Hermiticity error                     0
Taylor/spectral half-step relative disagreement    1.3113276888286176e-18
```

The inherited zero-history ceiling did not pass:

```text
N=1     2.7422508708241367e-13
N=2     5.2180482216205140e-13
N=8     1.9635404413577016e-12
N=64    1.5343504246163240e-11
ceiling 1.0e-11
```

Every analytic, support, selected-complex-row, and sampled spectral/dominance
gate passed. No threshold is changed and no PASS is inferred.

## Localized numerical cause

The zero-history cell map is represented by a Stinespring isometry assembled
from 96 floating-point split steps. The two raw cell-isometry Gram defects are

```text
1.880632874796716e-12
1.942168207386481e-12
```

and the two-cell composite Kraus completeness defect is

```text
2.943927509941952e-12.
```

The nearly linear volume growth in the failed zero-history check is consistent
with this accumulated floating-point loss of isometry. The v001 repair fixed
the zero-history free half-step but did not normalize the assembled
Stinespring isometry.

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
