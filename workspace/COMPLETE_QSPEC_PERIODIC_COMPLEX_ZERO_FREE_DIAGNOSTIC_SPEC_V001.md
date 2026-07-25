# Complete-Qspec Periodic Complex Zero-Free Diagnostic Specification v001

Date: 2026-07-25

## Purpose

Search for complex-field zeros of the frozen period-two sequential
relative-history amplitude before any logarithmic effective-action or
coupling identification.

This is a preregistered numerical diagnostic, not a certified analytic
zero-free theorem. No response target, alpha value, or measured constant
may enter.

## Analytic continuation

Continue the cell holonomy `theta` to complex values using the same
finite-dimensional Qspec generator and the matrix exponential:

```text
exp[-i dt H(theta)].
```

No Hermitian eigensolver may be used for complex `theta`.

For uniform complex `theta`, define:

```text
Z_N(theta)
 = Tr_S [T_theta^N(rho_source,in)].
```

## Frozen domain

```text
disk radius delta          1/100
boundary angles            64 equally spaced values
interior radii             {1/400, 1/200, 3/400}
interior angles            16 equally spaced values
time steps per cell        {48, 96}
volumes N                  {1,2,...,64}
```

## Frozen gates

1. Every sampled `|Z_N(theta)|` must exceed `0.95`.
2. The maximum relative disagreement between the 48-step and 96-step
   amplitudes must be below `1e-4`.
3. For every `N=1,...,64`, the unwrapped phase of `Z_N` around the boundary
   must have winding number zero and maximum adjacent phase increment below
   `pi/2`.
4. On every boundary point, define:

```text
lambda_48 = Z_48/Z_47
lambda_64 = Z_64/Z_63.
```

Require:

```text
|lambda_64-lambda_48| / max(|lambda_64|,1e-30) < 1e-6.
```

No threshold may be changed after execution.

## Verdict

Return:

```text
PERIODIC_COMPLEX_ZERO_FREE_DIAGNOSTIC_PASS
```

only if every gate passes. Otherwise return:

```text
PERIODIC_COMPLEX_ZERO_FREE_DIAGNOSTIC_BLOCKED
```

## Scope ceiling

A pass finds no zero in the sampled complex disk and confirms zero winding
through volume 64 with converged large-volume ratios. Sampling does not
certify the continuum between points and does not prove the all-volume or
all-cellulation zero-free theorem. Therefore
`volume_uniform_zero_free_neighborhood_proved` remains false.

## Fixed status

```text
periodic_complex_zero_free_diagnostic_passed = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
local_Maxwell_response_derived = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
