# Complete-Q_spec Finite-Holonomy Response Numerics Successor v001

Date: 2026-07-25

Authority:

```text
a7d5a3330bfe7ad7e696399aa8673763c97faecdeebfdc42996d9581c938c3e3  COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_NUMERICAL_BLOCK_V001.md
```

The v001 run is preserved as blocked. This successor changes only the
RK4 tangent/Duhamel resolutions:

```text
old: 200/400 steps per cell;
new: 800/1600 steps per cell.
```

The split-response grids remain:

```text
theta=1/20,1/40;
time steps=200,400.
```

All physics inputs, the `2e-10` state-norm threshold, the positive-lower-bound
requirements, and the interval-intersection rule remain unchanged.

For the new Duhamel pair:

```text
radius_D=|g_D(1600)-g_D(800)|/3+1e-8.
```

No target access or tolerance change is authorized.

```text
finite_Qspec_holonomy_response_diagnostic_passed = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
