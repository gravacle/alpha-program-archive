# Complete-Qspec Periodic Uniform Zero-Free Theorem Spec v001

Date: 2026-07-25

## Purpose

Replace finite complex sampling by a volume-uniform theorem on a continuous
complex disk for the frozen period-two regulator. The theorem is a T7
sub-result. It is not an all-cellulation result and does not authorize a
coupling evaluation.

## Frozen authorities

```text
85d5a138a1c11dbcfcd85428536afd65bad1f9f6603c7a79c9ad489cd3070e37  COMPLETE_QSPEC_ANALYTIC_CONTINUATION_INDEPENDENT_ISOMETRY_STABILIZATION_ADDENDUM_V001.md
1cd9528bc6872a3a28df828a452a165f8672cccc455a64323edab9e0905bf69d  scripts/verify_complete_qspec_periodic_analytic_continuation_v003.py
f39103452e214c8e0ef29ebeddd884074140a35316c486fadabb12c4b160bf65  stage8_execution/work/QSPEC_periodic_analytic_continuation_verification_v003.json
fbe852adafe1d83e506a8f302622ed3a8234354223df029c7183a0dd4b2ea83a  COMPLETE_QSPEC_PERIODIC_ANALYTIC_CONTINUATION_INDEPENDENT_RESULT_V001.md
```

Any mismatch aborts execution.

## Frozen theorem constants

```text
disk radius R             = 1/500
zero-complement bound r0  = 813/1000
graph-ball radius X       = 1/20
finite-volume cutoff      = 6
dominance starts          = 7
source dimension          = 70
zero support dimension    = 5
two-cell record outcomes  = 9
```

The radius is smaller than the earlier sampled radius. It is selected from
the analytic perturbation inequalities below, not by comparison with alpha
or any coupling value.

## T0: zero-transfer certificate

Rebuild the stabilized zero-history composite and the `350 x 350` transfer
`T0`. Certify:

```text
|lambda0 - 1|                                  < 1e-12
||P0^2-P0||, ||P0-P0^dagger||                 < 1e-11
||T0 P0-P0||, ||P0 T0-P0||                   < 1e-11
||T0||_2                                       < 1 + 1e-11
||R0||_2 for R0=T0-P0                          < 813/1000
|trace_functional P0 start - 1|                < 1e-11
||start||_2                                    < 1 + 1e-11
||trace_functional||_2                         < sqrt(5) + 1e-11
```

The numerical singular-value certificate must include singular-vector
residuals and an independent recomputation. A failure is BLOCKED; `r0` may
not be widened after execution.

## T1: analytic generator bound

On `|z| <= R`, the active one-body derivative is the two nonzero Fourier
sectors of the three-site directed difference. From the value at zero and
the exponential remainder,

```text
L_free = (2/3) * (1 + (2R/3) exp(R/3)),
||F(z)-F(0)||_2 <= delta = L_free R.
```

The factor `2/3` is the four-particle lift of the active-sector `1/6`
one-body value. The executable must independently enumerate the active
Fourier eigenvalues and verify the bound on a denser diagnostic mesh; the
analytic inequality, not the mesh, carries the theorem.

## T2: transfer perturbation bound

There is unit total free duration per cell. Telescoping/Duhamel comparison
with the zero cell gives

```text
||V_cell(z)-V_cell(0)||_2 <= exp(delta)-1,
||V_pair(z)-V_pair(0)||_2 <= exp(2 delta)-1.
```

The composite record environment has dimension nine. The Hilbert-Schmidt
partial-trace bound therefore gives

```text
epsilon = 3 * (exp(2 delta)-1),
||T(z)-T0||_2 <= epsilon.
```

The executable shall directly sample the transfer difference only as a
negative-control check. Passing the theorem may not depend on the sampled
maximum.

## T3: invariant-graph theorem

Use the orthogonal decomposition `P0 + Q0`. Write

```text
T(z) = [[a,b],[c,D]]
```

with

```text
|a-1|, ||b||, ||c|| <= epsilon,
||D|| <= r0 + epsilon.
```

For the right and left graph maps on the closed ball of radius `X`, define

```text
separation =
  1 - epsilon - epsilon X - (r0 + epsilon).
```

The certificate must establish

```text
separation > 0,
epsilon / separation < X,
(epsilon / separation)^2 < 1.
```

Banach contraction then supplies unique analytic right and left graph
vectors of norm at most `X`, a simple nonzero analytic leading eigenvalue,
and its rank-one spectral projector.

## T4: uniform nonzero amplitude

Define

```text
lambda_min = 1 - epsilon(1+X),
D_tilde_max = r0 + epsilon + epsilon X,
projector_delta = (2X + 2X^2)/(1-X^2),
coefficient_min = 1 - sqrt(5) projector_delta,
kappa_S = (1+X)/(1-X),
q = D_tilde_max/lambda_min,
prefactor = sqrt(5) kappa_S/coefficient_min.
```

Require `lambda_min`, `coefficient_min` positive and `q < 1`.

For `1 <= N <= 6`, certify

```text
|Z_N(z)-1| <= sqrt(5) N epsilon (1+epsilon)^(N-1) < 1.
```

For every `N >= 7`, certify

```text
|remainder_N| / |leading_N|
  <= prefactor q^N
  <= prefactor q^7
  < 1.
```

These inequalities prove `Z_N(z) != 0` for every integer `N >= 1` and every
`|z| <= R`.

## T5: thermodynamic density

From the uniform analytic graph and dominance bounds, prove

```text
lim_(N->infinity) (1/N) Log Z_N(z) = Log lambda(z)
```

uniformly on the disk, with the branches fixed continuously from `z=0`.
This is the connected linked-cluster density for the frozen periodic
regulator only.

## Pass rule and scope

All T0-T5 obligations must pass. Any failed bound is BLOCKED; there is no
conditional route and no threshold widening.

Even on PASS:

```text
periodic_volume_uniform_zero_free_neighborhood_proved = true
periodic_connected_linked_cluster_density_proved = true
all_stage8_regulators_zero_free_proved = false
all_connected_cellulations_linked_cluster_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
