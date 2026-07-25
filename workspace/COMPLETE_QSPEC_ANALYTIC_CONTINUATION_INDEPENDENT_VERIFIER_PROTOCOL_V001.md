# Complete-Qspec Analytic-Continuation Independent Verifier Protocol v001

Date: 2026-07-25

## Purpose

Independently reconstruct the repaired analytic continuation and test the
full transfer spectrum on the target-independent source support. The
verifier may not import the v003/v004 producer or its matrix-exponential
implementation.

## Frozen authorities

```text
5065836ae6162cdcc609b3a0058777a54322c90fb551ab7d037855646a53cdd0  COMPLETE_QSPEC_ANALYTIC_CONTINUATION_DERIVATIVE_REPAIR_SPEC_V001.md
4f9ca24625f8cb96027ba8863d6910892250e1c709b1a1d57c0c66534bff2a99  scripts/derive_complete_qspec_periodic_analytic_continuation_v004.py
e7fefe80f447e464a320f16840f2fdf2a32b70ce93bda6f0a25d02c379f97a54  stage8_execution/work/QSPEC_periodic_analytic_continuation_v004.json
f706a4ab85f5863b87f6f5591a6907b25164cc6bebc6484e87b67a04bfc107b4  COMPLETE_QSPEC_COMPLEX_CONTINUATION_CONJUGATION_ERRATUM_V001.md
```

Any mismatch aborts execution.

## Independent implementation

The verifier must separately implement:

```text
Dirac matrices;
the directed analytic three-site connection;
number-conserving dGamma;
the diamond envelope;
a Taylor-series scaling-and-squaring exponential;
cell Kraus operators;
the zero-history reachable-support closure;
and the reduced relative-history transfer operator.
```

It may use NumPy linear algebra but may not import any construction helper
from the producer lineage.

## V1 - Real and analytic checks

At the five frozen real-axis points, reconstruct the Hermitian directed-edge
operator and require a Hermiticity error below `1e-12`.

At the three frozen complex points, compare centered derivatives to the
independently written exact analytic derivative and require every relative
residual below `1e-8`.

The conjugate-based negative control must exceed `1e-3`.

## V2 - Zero-history support

At 96 steps, close the source Hilbert-space orbit generated from the incoming
pure source state by all nine two-cell zero-history Kraus products.

Require:

```text
reachable support dimension = 5;
maximum invariance residual < 1e-11.
```

Use this support only on the zero-history side. The analytic branch remains
on the complete 70-dimensional source carrier, giving a `70 x 5` relative
operator space and a `350 x 350` dense transfer matrix.

## V3 - Frozen complex points

Use:

```text
0;
+1/100;
-1/100;
+i/100;
-i/100;
(1+i)/(100 sqrt(2));
(-1+i)/(100 sqrt(2));
(-1-i)/(100 sqrt(2));
(1-i)/(100 sqrt(2)).
```

At every nonzero point:

```text
1. compare reduced and direct amplitudes for N={1,2,8,64};
2. require maximum relative disagreement < 1e-10;
3. compare N=64 with the sealed producer output and require < 1e-9;
4. diagonalize the complete 350-dimensional reduced transfer matrix;
5. require one isolated dominant eigenvalue with relative modulus gap > 0.25;
6. construct its left/right rank-one spectral projector;
7. require projector idempotence and eigen-relations below 1e-10;
8. require dominant scalar coefficient magnitude > 0.95;
9. require ||R||_2/|lambda| < 0.85 for R=T-lambda P.
```

For the final two requirements, verify the all-power sampled-point
dominance inequality:

```text
sqrt(5) [||R||_2/|lambda|]^5 / |a| < 1.
```

This proves nonvanishing for every `N>=5` at each frozen point. Directly
require `|Z_N|>0.95` for `N=1,...,4`.

At zero, require direct and reduced amplitudes equal one below `1e-11` for
the same volumes. No nondegenerate spectral claim is made at zero.

## Verdict

Return:

```text
INDEPENDENT_PERIODIC_ANALYTIC_CONTINUATION_CONFIRMED
```

only if V1-V3 all pass. Otherwise return:

```text
INDEPENDENT_PERIODIC_ANALYTIC_CONTINUATION_BLOCKED
```

## Scope

The sampled-point all-volume dominance result does not fill the continuum
between points and does not prove arbitrary-cellulation zero-freeness.
`volume_uniform_zero_free_neighborhood_proved` remains false.

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
