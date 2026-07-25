# Complete-Qspec Periodic Transfer Spectral Independent Verifier Protocol v001

Date: 2026-07-25

## Purpose

Independently verify the dominant-transfer spectral diagnostic without
Arnoldi iteration, Ritz-mode selection, or the primary script's power-method
implementation.

No response target, coupling value, alpha value, or measured constant may
enter.

## Frozen method

For each frozen pair:

```text
steps in {32, 64}
theta in {+1/20, -1/20, +1/40, -1/40},
```

iterate the two-cell source-space cross-history map directly from the frozen
source density. Let:

```text
Z_N = Tr_S X_N.
```

At `N=64` and `N=96`, estimate the reachable dominant eigenvalue by:

```text
lambda_N = Z_N / Z_(N-1).
```

This is distinct from the primary Arnoldi/Rayleigh route. No eigenvector is
constructed and no spectral mode is selected.

## Gates

For every row require:

```text
|Z_(N-1)| > 1e-12;
|lambda_96 - lambda_64| / |lambda_96| < 1e-10;
||lambda_96| - |lambda_primary|| / |lambda_primary| < 1e-10.
```

Reconstruct the four raw intensive responses, the two time-extrapolated
responses, and the final theta-extrapolated infinite-chain rate from
`lambda_96`. Require:

```text
absolute difference from the primary final rate < 5e-7;
the independent rate lies inside the primary sealed interval;
the finite N=16 and N=32 differences have the same sign;
0.35 < |d_32/d_16| < 0.65.
```

No threshold may be changed after execution.

## Verdict

Return:

```text
INDEPENDENT_PERIODIC_TRANSFER_SPECTRAL_DIAGNOSTIC_CONFIRMED
```

only if every gate passes. Otherwise return:

```text
INDEPENDENT_PERIODIC_TRANSFER_SPECTRAL_DIAGNOSTIC_BLOCKED
```

## Scope ceiling

A pass independently confirms the spectral limit for the frozen strictly
sequential period-two regulator. It does not establish schedule exhaustion,
a volume-uniform zero-free neighborhood, low-frequency locality, a Maxwell
coefficient, kappa_record, alpha, or proof authorization.

## Fixed status

```text
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
