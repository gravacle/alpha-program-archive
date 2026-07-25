# Complete-Qspec Periodic Transfer Spectral Diagnostic Specification v001

Date: 2026-07-25

## Purpose

Resolve the blocked finite-size period-two regression by computing the
reachable dominant mode of its exact two-cell cross-history transfer
operator. The infinite-chain intensive rate must come from this spectrum,
not from extending a finite cutoff until a tolerance happens to pass.

This remains a period-two regulator diagnostic. It is not the physical
Lorentz-covariant continuum or a linked-cluster theorem.

No coupling target, alpha value, endpoint value, or measured constant may
enter.

## Frozen authorities

```text
b3800c690cf7376a13375f1fb747e94ccc1a000383f0ea48ab1a3341fcd45549  COMPLETE_QSPEC_PERIODIC_CONNECTED_AMPLITUDE_NUMERICAL_BLOCK_V001.md
7e79583981dd97b2fb5e0ebb6a3498b7bdc03a29cb46f8e2c654f62bc52315ef  COMPLETE_QSPEC_RELATIVE_HISTORY_TRANSFER_MAP_SPEC_V001.md
3800b661ea0dacb052aeb0a843f331a13eddc9c838949e5e224c2a5c288271d1  scripts/derive_complete_qspec_relative_history_transfer_map_v001.py
b202278190c5e440713abbea247fcfcb92c1dc4fba1a1b08d8db648f3579caaf  stage8_execution/work/QSPEC_relative_history_transfer_map_v001.json
```

## S1 - Exact supercell operator

For each frozen time resolution and angle, define on source cross-densities:

```text
P_(theta,0)
 = T_cell1^(theta,0) o T_cell0^(theta,0).
```

The operator is applied matrix-free using the already derived Kraus form. No
`4900 x 4900` dense matrix is built and no full record Hilbert space is
introduced.

## S2 - Frozen spectral computation

Use:

```text
Strang steps per cell = 32 and 64
theta = +1/20, -1/20, +1/40, -1/40
Arnoldi Krylov dimension = 48
starting vector = the frozen incoming source density
two-pass modified Gram-Schmidt
```

Diagonalize the resulting Hessenberg matrix. For every Ritz pair compute the
full matrix-free residual:

```text
r = ||P(X)-lambda X||_F / ||X||_F.
```

The selected reachable mode is the largest-modulus Ritz mode satisfying:

```text
r < 1e-8;
|Tr X|/||X||_F > 1e-8.
```

The relative modulus gap to the next reachable Ritz mode must exceed `1e-5`.
If no mode satisfies these conditions, the diagnostic is blocked.

## S3 - Independent power check

Starting from the frozen source density, apply the supercell map 128 times,
normalizing in Frobenius norm at every step. Require:

```text
final eigen-residual < 1e-6;
relative difference between its Rayleigh quotient and the selected
Arnoldi eigenvalue < 1e-6.
```

This check is algorithmically distinct from Hessenberg diagonalization.

## S4 - Infinite-chain intensive rate

For each angle and time resolution, let the selected eigenvalue be
`lambda(theta)`. Define per physical cell:

```text
h_inf(theta)
 = [-log|lambda(+theta)|-log|lambda(-theta)|]/(2 theta^2).
```

Extrapolate second-order Strang error and then centered-angle error using the
same frozen formulas as the blocked finite-schedule diagnostic.

Require the resulting interval to be strictly positive.

## S5 - Boundary-correction check

Using the already frozen finite results at `N=8,16,32`, compare:

```text
d_N = h_N-h_inf.
```

The spectral interpretation passes this check only if:

```text
sign(d_16)=sign(d_32);
0.35 < |d_32/d_16| < 0.65.
```

This is the predeclared `O(1/N)` boundary-correction window.

## Verdict

Return:

```text
PERIODIC_TRANSFER_SPECTRAL_DIAGNOSTIC_PASS
```

only if S1-S5 pass. Otherwise return:

```text
PERIODIC_TRANSFER_SPECTRAL_DIAGNOSTIC_BLOCKED
```

## Scope ceiling

Even a pass establishes only the asymptotic rate of the declared period-two
regression. It does not establish:

```text
a volume-uniform zero-free theorem;
an all-cellulation linked-cluster density;
Lorentz-covariant continuum convergence;
low-frequency temporal locality;
spatial plaquette response;
the Maxwell tensor;
kappa_record;
the Thomson limit;
alpha;
or proof authorization.
```

## Fixed status

```text
relative_history_transfer_map_derived = true
periodic_connected_amplitude_constructed = true
periodic_transfer_spectral_limit_computed = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
local_Maxwell_response_derived = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
