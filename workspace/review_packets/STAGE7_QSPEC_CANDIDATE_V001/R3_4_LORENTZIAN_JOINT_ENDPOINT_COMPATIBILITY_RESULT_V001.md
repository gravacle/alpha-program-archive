# R3.4 Lorentzian Joint-Endpoint Compatibility Result v001

## Verdict

```text
EXACT_ENDPOINT_REST_NORMAL_ONLY_THRESHOLD_ROUTE_REQUIRED
```

The local Lorentzian parent preserves the exact primitive opening endpoint
only on the rest-normal momentum ray. A generic finite momentum packet does
not undergo exact `ready -> pointer` transfer at the same finite interval.
This is a negative compatibility result, not a repair license.

## Exact decomposition

The record carrier separates into

```text
z=(ready+pointer)/sqrt(2),  c_partial z=0,
m=(ready-pointer)/sqrt(2),  c_partial^2 m=2m.
```

For tangential momentum `p`, the two frequencies are therefore

```text
omega_0=|p|,
omega_m=sqrt(p^2+2 mu^2).
```

At the first-opening interval `T_R=1` and
`mu=pi/sqrt(2)`, `p=0` gives `omega_m T_R=pi`; the record endpoint is exact.
For nonzero `p`, exact transfer additionally requires commensurate kinetic
and massive phases with opposite parity. Generic momenta do not satisfy
those simultaneous conditions.

## Executable result

The pointer probabilities at `T_R` are

```text
p=0.00: 0.9999999999999996
p=0.25: 0.9845052711696443
p=0.50: 0.9395566924273323
p=1.00: 0.7812082943003530
p=2.00: 0.4067339219700168
p=4.00: 0.2596535767624385
```

A normalized one-dimensional Gaussian packet with width `0.7` gives

```text
P_pointer(T_R)=0.9442917391998132.
```

The producer obtains these values by Hermitian diagonalization. The
independent verifier instead evaluates the exact functional calculus

```text
exp(-iHt)=cos(sqrt(H^2)t)
          -i H sin(sqrt(H^2)t)/sqrt(H^2)
```

on the zero and massive record projectors. The two calculations agree
within `2e-12`.

## Consequence

The primitive internal action interval, the exact rest-normal endpoint, and
physical durability are distinct statements. The first two are derived in
their stated scope. Physical durability must be tested through the already
declared thresholded outgoing/direct-limit criterion; it cannot be inferred
from exact finite-time orthogonality.

The previously examined comoving transported interaction is not promoted
as a repair. Its covariance law remains underived from the adopted
principles.

## Scope

```text
rest_normal_exact_endpoint_derived = true
universal_exact_finite_wavepacket_write_derived = false
thresholded_direct_limit_route_required = true
physical_thresholded_durability_derived = false
physical_in_state_selected = false
complete_root_spectral_measure_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
