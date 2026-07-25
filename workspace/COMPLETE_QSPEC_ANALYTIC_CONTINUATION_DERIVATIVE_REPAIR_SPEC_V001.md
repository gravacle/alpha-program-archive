# Complete-Qspec Analytic-Continuation Derivative Repair Spec v001

Date: 2026-07-25

## Purpose

Replace only the roundoff-sensitive monotonicity clause in A3 of the sealed
analytic-continuation repair. Every physical domain, time discretization,
volume, and zero-search threshold remains unchanged.

## Frozen authorities

```text
1f7e78a8a71dffb6ccf80614a78344ab170381d633fa91ce7483187673512c57  COMPLETE_QSPEC_ANALYTIC_CONTINUATION_REPAIR_SPEC_V001.md
776651fd0c7732e6eb0d91a6efa16d53290a1d4bdbbb632d2d09e32069491a40  scripts/derive_complete_qspec_periodic_analytic_continuation_v003.py
02fb0d29cfb7e48422924a833379050c0a49ad57cc4182b270d963774554dc87  COMPLETE_QSPEC_ANALYTIC_CONTINUATION_PREFLIGHT_FAILURE_V001.md
f706a4ab85f5863b87f6f5591a6907b25164cc6bebc6484e87b67a04bfc107b4  COMPLETE_QSPEC_COMPLEX_CONTINUATION_CONJUGATION_ERRATUM_V001.md
```

Any mismatch aborts execution.

## Repaired A3

For:

```text
p_+(theta)=exp(+i theta/3),
p_-(theta)=exp(-i theta/3),
```

independently implement:

```text
dp_+/dtheta=(+i/3)p_+,
dp_-/dtheta=(-i/3)p_-.
```

Propagate that exact derivative linearly through the directed-edge
difference, the frozen active-basis compression, and `dGamma`.

At the three previously frozen complex points and both previously frozen
finite-difference steps:

```text
1e-5, 5e-6,
```

require:

```text
||d_x F - F'||/max(||F'||,1e-30) < 1e-8;
||d_y F - i F'||/max(||F'||,1e-30) < 1e-8;
||d_y F - i d_x F||/max(||d_x F||,||d_y F||,1e-30) < 1e-8.
```

No monotonic decrease is required once both independently oriented
derivatives satisfy the same frozen accuracy ceiling.

The conjugate-based negative control must still exceed `1e-3` at at least
one point.

## Inherited gates

A1, A2, A4, the verdict rule, the scope ceiling, and every protected status
from `COMPLETE_QSPEC_ANALYTIC_CONTINUATION_REPAIR_SPEC_V001.md` remain
binding without alteration.

## Fixed status

```text
analytic_complex_continuation_repaired = false
periodic_analytic_continuation_diagnostic_passed = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
