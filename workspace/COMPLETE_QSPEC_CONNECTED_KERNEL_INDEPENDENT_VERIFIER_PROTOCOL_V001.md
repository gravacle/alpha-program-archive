# Complete-Qspec Connected-Kernel Independent Verifier Protocol v001

Date: 2026-07-25

## Purpose

Independently verify the period-two connected-kernel locality diagnostic by
differentiating the transfer map rather than finite-differencing
multi-perturbation logarithms.

No response target, alpha value, or measured constant may enter.

## Independent construction

Use step counts `{48,96}`, distinct from the primary `{32,64}` family.
For each step count, construct the one-supercell map `T_theta` at:

```text
theta in {0, +/-h, +/-2h}
h in {1/160, 1/320}.
```

Use five-point centered derivatives:

```text
T'(X)
 = [T(-2h)X - 8T(-h)X + 8T(h)X - T(2h)X] / (12h),

T''(X)
 = [-T(2h)X + 16T(h)X - 30T(0)X
    +16T(-h)X - T(-2h)X] / (12h^2).
```

Generate the zero-field bulk density by 64 applications of `T_0` from the
frozen source density. Do not insert an eigenvector.

Let:

```text
z_1 = Tr T'(rho_bulk)

K(0) = -Re[Tr T''(rho_bulk) - z_1^2],

K(r) = -Re[
          Tr T' T_0^(r-1) T'(rho_bulk) - z_1^2
        ],  r>0.
```

Apply fourth-order `h` Richardson extrapolation and second-order time-step
Richardson extrapolation.

## Frozen gates

1. The bulk density must retain trace one within `1e-10`, and one additional
   `T_0` application must change it by Frobenius norm below `1e-10`.
2. For `r=0,...,8`, require:

```text
|K_independent(r)-K_primary(r)|
/ max(|K_primary(r)|, 1e-7) < 0.02.
```

3. On rows `r=3,...,10`, fit `log|K(r)|=a+r log q`; require at least six
   rows, `q<0.8`, and `R^2>0.90`.
4. Recompute:

```text
C_R = -sum_(r=1)^R r^2 K(r)
```

and require `|C_10-C_8|/max(|C_10|,1e-10)<0.05`.
5. Require the `R=8` and `R=10` Fourier responses to remain positive at
   `k in {0,pi/16,pi/8}`.

No threshold may be changed after execution.

## Verdict

Return:

```text
INDEPENDENT_PERIODIC_CONNECTED_KERNEL_LOCALITY_CONFIRMED
```

only if every gate passes. Otherwise return:

```text
INDEPENDENT_PERIODIC_CONNECTED_KERNEL_LOCALITY_BLOCKED
```

## Scope ceiling

A pass independently confirms regulator-level connected-kernel decay and
low-frequency stability. It does not prove all-cellulation locality, a
volume-uniform zero-free theorem, the Maxwell tensor, kappa_record, alpha,
or proof authorization.

## Fixed status

```text
periodic_connected_kernel_locality_diagnostic_passed = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
local_Maxwell_response_derived = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
