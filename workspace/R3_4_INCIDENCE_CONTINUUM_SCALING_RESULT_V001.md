# R3.4 Incidence-Continuum Scaling Result v001

## Verdict

```text
FREE_FLAT_TAIL_OPERATOR_AND_ROOT_MEASURE_DERIVED_WRITE_DEFECT_OPEN
```

The free flat outgoing-tail operator, its unbounded refinement limit, and
its conditional positive-energy root measure are now computed from the
incidence operator. The complete write-plus-tail spectral measure remains
open.

## Scaled incidence and continuum limit

For lattice spacing `a`,

```text
d_a,j(k)=[exp(i a k_j)-1]/a.
```

The factor `1/a` is the coframe conversion from a dimensionless cellular
difference to a physical derivative. The resulting self-adjoint block
operator has norm

```text
||H_a||=2 sqrt(3)/a,
```

so the earlier uniformly bounded direct-limit theorem does not apply.

For every fixed momentum,

```text
d_a(k)->i k,
h_a(k)->h(k)=[[0,d(k)^dagger],[d(k),0]].
```

For nonreal `z`, self-adjointness gives

```text
||(h_a-z)^(-1)||<=1/|Im z|.
```

Pointwise resolvent convergence plus this uniform bound gives strong
resolvent convergence by dominated convergence. The same pointwise argument
with unitary norm bound one gives strong convergence of the evolution for
each fixed time.

The continuum operator is the Hermitian Fourier multiplier `h(k)` on

```text
D(H_0)={psi in L2: h(k)psi(k) is in L2}.
```

This is its self-adjoint maximal domain.

## Projector calculation

On the scalar-plus-longitudinal sector,

```text
h(k)^2=|k|^2.
```

The full truncated `0`-plus-`1`-form symbol has eigenvalues

```text
{-|k|,0,0,+|k|}.
```

For the scalar root vector:

```text
<r,P_+ r>=1/2,
<r,P_- r>=1/2,
<r,P_0 r>=0.
```

The transverse zero eigenspace is therefore retained in the operator but
does not create a point atom in this root's spectral measure.

## Root measure

The future normal selects the maximal waist ball of the unit causal diamond:

```text
R=1/2,
Vol_3(B)=pi/6,
psi_B=1_B/sqrt(Vol_3(B)).
```

Its normalized spatial Fourier form factor is

```text
F_B(E)
 =3[sin(E/2)-(E/2)cos(E/2)]/(E/2)^3.
```

This equals the full four-dimensional diamond's null-shell form factor
exactly. With the Fourier convention `(2 pi)^(-3/2)`, angular integration,
and conditioning the one-half positive projector weight, the radial
prefactor is

```text
Vol_3(B)/(2 pi^2)=1/(12 pi).
```

Thus the operator-derived conditional positive-energy root measure is

```text
rho_+(E)
 =E^2 |F_B(E)|^2/(12 pi)
 =48[sin(E/2)-(E/2)cos(E/2)]^2/(pi E^4).
```

This reproduces the R3.4 v002 scalar density without inserting its
normalization.

## Two unresolved physical issues

First, the computation constructs `P_+`; it does not yet derive that the
physical record branch must use the positive-frequency one-particle
conditioning. That spectrum condition must be inherited explicitly or
derived from the complete parent.

Second, the sharp root is in the Hilbert space but not in `D(H_0)`. Since

```text
rho_+(E)=O(E^-2),
```

its mean energy diverges logarithmically:

```text
integral E rho_+(E)dE=infinity.
```

A finite-energy preparation requires either a derived boundary profile, a
fundamental finite-cell cutoff, or a boundary-domain action that makes the
sharp cell admissible. Choosing a smoother profile after seeing the spectrum
is forbidden.

The complete compact write-region defect is also not yet attached to the
free tail. Such a defect can produce bound modes or point spectrum even when
the free root measure is absolutely continuous. Its spectrum must be
computed from the complete write operator before promotion.

## Status

```text
free_flat_continuum_scaling_derived = true
strong_resolvent_limit_derived_in_flat_cubical_branch = true
self_adjoint_free_outgoing_domain_derived = true
positive_energy_projector_derived = true
operator_derived_positive_branch_root_measure_computed = true
physical_positive_energy_record_branch_selected = false
sharp_root_in_generator_domain = false
finite_energy_physical_root_derived = false
complete_write_defect_spectrum_closed = false
complete_outgoing_root_spectral_measure_derived = false
hypothesis_promoted_to_principle = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
