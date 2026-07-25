# R3.4 Causal-Diamond Spectral Pullback Result v002

## Verdict

```text
CONDITIONAL_SCALAR_DIAMOND_DENSITY_ONLY
```

The scalar causal-diamond calculation passes. The physical operator
provenance does not. This result therefore supplies a mathematically complete
candidate density and a sharper next derivation target; it does not promote
the direct-limit hypothesis.

## Conditional calculation

For the normalized unit-tip-separation diamond,

```text
Vol(D)=pi/24,

F_D(E)
 = 24/E^3 [sin(E/2)-(E/2)cos(E/2)].
```

The closed form agrees with an independent quadrature of the full
four-dimensional diamond to a maximum absolute error of `7.76e-12` over the
sealed test energies.

Under the explicitly conditional radial weight `E^2 dE`,

```text
N_D
 = integral_0^infinity E^2 |F_D(E)|^2 dE
 = 12 pi,

rho_D(E)
 = [48/pi]
   [sin(E/2)-(E/2)cos(E/2)]^2/E^4.
```

The exact normalization reduces to

```text
N_D=72 integral_0^infinity j_1(z)^2 dz=12 pi.
```

The independent numerical normalization is `0.999999994157`.

## Regularity and decay

The threshold expansion is

```text
rho_D(E)
 = E^2/(12 pi)-E^4/(240 pi)+E^6/(11200 pi)+O(E^8).
```

For large `E`,

```text
rho_D(E)
 = 6[1+cos(E)]/(pi E^2)
   -24 sin(E)/(pi E^3)
   +24[1-cos(E)]/(pi E^4).
```

This decomposition proves that `rho_D` and its first three derivatives are
integrable at infinity; the threshold series proves regularity at zero. The
first two boundary terms vanish and

```text
rho_D''(0)=1/(6 pi).
```

Three integrations by parts therefore give

```text
A_D(t)=i/(6 pi t^3)+o(t^-3),
|A_D(t)|^2=O(t^-6).
```

Riemann-Lebesgue consequently supplies thresholded local-return decay for
this conditional density.

## Regulator comparison

The result matches the probability class `t^-6` of the earlier covariant
continuum representative. It does not match the three discrete point-root
regulators, whose interval-averaged probabilities have class `t^-3`.
Compact-time regulator convergence does not prove equality of late-time
asymptotics, so this mismatch remains open.

## Physical provenance blocker

The corpus has not yet constructed an operator whose root spectral theorem
returns this density. In particular:

1. the proved direct-limit theorem is for uniformly bounded incidence
   operators, while `E=|k|` is unbounded;
2. no strong-resolvent refinement theorem to a continuum generator exists;
3. no self-adjoint outgoing-sector domain and positive-energy projector have
   been derived;
4. the finite-root/quasi-local-state map into the continuum one-particle
   Hilbert space is missing;
5. the `E^2 dE` radial weight and multiplicities have not been obtained from
   the actual operator; and
6. gapped, point-spectrum, and inequivalent preparation sectors have not
   been excluded.

The next valid move is an outgoing-record continuum-operator derivation. It
must compute `<r,P(dE)r>`; it may not adopt this density merely because the
conditional calculation is clean.

## Audit hardening

Version 002:

```text
hash-pins every authority;
requires exactly one occurrence of every expected status key;
fails closed on missing or changed negative statuses;
derives the regularity certificate instead of storing bare true values;
keeps tests side-effect-free;
and uses a separately coded midpoint-quadrature verifier.
```

## Status

```text
uniform_flat_cell_measure_derived = true
outgoing_record_algebra_subobligation_closed = true
conditional_scalar_density_computed = true
conditional_scalar_density_absolutely_continuous = true
conditional_thresholded_durability = true
operator_derived_root_spectral_measure_computed = false
unique_covariant_spectral_measure_derived = false
hypothesis_promoted_to_principle = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
