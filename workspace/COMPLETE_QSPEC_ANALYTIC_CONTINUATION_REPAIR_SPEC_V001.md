# Complete-Qspec Analytic-Continuation Repair Specification v001

Date: 2026-07-25

## Purpose

Rebuild the complex holonomy continuation after the conjugation erratum and
rerun the frozen finite-volume zero search. This is a diagnostic repair, not
an all-volume zero-free theorem.

No electromagnetic target value may enter.

## Frozen authorities

```text
ade49876242ffc4ce6c90942f8b63261f3cc1c463103110ff1e2e60fee232e84  COMPLETE_QSPEC_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_RESULT_V001.md
b7f5f0f29c69c14b3cfd6afba285c437ff0c2cb285c2f29f4ce3fb576bdfff48  COMPLETE_QSPEC_PERIODIC_TRANSFER_SPECTRAL_DIAGNOSTIC_RESULT_V001.md
880ce005c7672857b927b12c24b3f07a16da9aeb1c89ed6430b4992fddfec47e  COMPLETE_QSPEC_CONNECTED_KERNEL_LOCALITY_DIAGNOSTIC_RESULT_V001.md
01501e04a9935c6714599076c0503353350245ce094e6ad18e3e146d7ff9d53b  COMPLETE_QSPEC_COMPLEX_ZERO_FREE_RUNTIME_PORTABILITY_ADDENDUM_V001.md
f706a4ab85f5863b87f6f5591a6907b25164cc6bebc6484e87b67a04bfc107b4  COMPLETE_QSPEC_COMPLEX_CONTINUATION_CONJUGATION_ERRATUM_V001.md
```

Any mismatch aborts execution.

## A1 - Holomorphic directed-edge continuation

For complex `theta`, define:

```text
p_forward(theta)  = exp(+i theta/3)
p_backward(theta) = exp(-i theta/3).
```

The backward factor must not use complex conjugation. Every entry of the
one-body covariant difference, its fixed active-basis compression, and its
number-conserving second quantization is then entire in `theta`.

## A2 - Real-axis identity

At:

```text
theta in {-1/100, -1/200, 0, 1/200, 1/100}
```

the repaired free generator must agree with the sealed Hermitian real-axis
generator below relative Frobenius error `1e-12`. The repaired half-step
matrix exponential must be unitary below `1e-11`.

## A3 - Independent Cauchy-Riemann check

At:

```text
theta = i/200;
theta = (1+i)/(200 sqrt(2));
theta = (-1+2i)/1000
```

use centered finite differences with:

```text
h in {1e-5, 5e-6}.
```

For a holomorphic matrix function `F`,

```text
dF/dy = i dF/dx.
```

Require the maximum relative Cauchy-Riemann residual at the finer step to be
below `1e-8`, and require it to decrease from the coarse step.

As a negative control, apply the same check to the superseded
conjugate-based construction and require a residual above `1e-3` at at least
one frozen complex point.

## A4 - Frozen complex-disk diagnostic

Retain the prior domain:

```text
disk radius                         1/100
boundary points                     64
interior radii                      {1/400, 1/200, 3/400}
interior angles per radius          16
time steps per cell                 {48, 96}
volumes                             {1,...,64}
```

Require:

```text
minimum |Z_N(theta)| > 0.95;
maximum 48/96 relative disagreement < 1e-4;
zero boundary winding for every N;
maximum adjacent boundary phase increment < pi/2;
maximum relative difference between Z_48/Z_47 and Z_64/Z_63 < 1e-6.
```

No threshold may change after execution.

## Verdict

Return:

```text
PERIODIC_ANALYTIC_CONTINUATION_DIAGNOSTIC_PASS
```

only if A1-A4 all pass. Otherwise return:

```text
PERIODIC_ANALYTIC_CONTINUATION_DIAGNOSTIC_BLOCKED
```

## Scope ceiling

A pass repairs the holomorphic continuation and supplies finite-volume
evidence on the frozen period-two regulator. It does not prove continuity
between sampled points, all-volume zero-freeness, arbitrary-cellulation
zero-freeness, or the physical continuum response.

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
