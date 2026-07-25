# Complete-Q_spec Finite-Holonomy Duhamel Crosscheck Protocol v001

Date: 2026-07-25

This protocol is sealed before execution and supplements, without changing,
the finite-holonomy numerics protocol.

At `theta=0`, differentiate the frozen covariant central difference
analytically to obtain:

```text
J=d H_source(theta)/dtheta at theta=0.
```

Lift `J` to the same fixed four-particle Fock sector. Along the two-cell
baseline evolution integrate:

```text
dot psi = -i H_0(t) psi;
dot eta = -i H_0(t) eta - i J psi;
psi(0)=psi_in;
eta(0)=0.
```

Use independently coded RK4 at `200` and `400` steps per cell. Compute:

```text
g_D=<eta|eta>-|<psi|eta>|^2.
```

The conservative enclosure is:

```text
radius_D=|g_D(400)-g_D(200)|/3+1e-8.
```

Pass requires:

```text
lower([g_D(400)-radius_D,g_D(400)+radius_D])>0;
the Duhamel interval intersects both frozen finite-difference intervals
I_H and I_g.
```

No response-dependent tolerance change is permitted.

```text
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
