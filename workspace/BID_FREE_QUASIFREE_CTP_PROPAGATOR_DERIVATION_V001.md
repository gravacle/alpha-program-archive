# BID Free Quasifree CTP Propagator Derivation v001

Date: 2026-07-24

## Purpose

Close the free-state/contour part of SP08 for the already derived primitive
Lorentzian source-record Hamiltonian. No measured mass, coupling, endpoint,
absolute record interval, or alpha value is used.

This is a free quasifree subgate. It does not substitute a free pole for the
interacting charged spectrum or a reversible correlator for a durable record.

## Hamiltonian and state

For one nonzero spatial momentum, use

```text
H(p)
 = alpha dot p
  -i mu gamma^0 gamma^5 tensor c_partial,
```

where `c_partial` is Hermitian with spectrum
`{-sqrt(2),0,+sqrt(2)}`. The previous pole gate established

```text
H(p)^2
 = |p|^2 + mu^2 c_partial^2.
```

The disclosed stationary quasifree vacuum fills the negative-energy
spectral subspace and leaves the positive-energy subspace empty. Let

```text
P_- = 1_(-infinity,0)(H),
P_+ = 1_(0,infinity)(H).
```

For nonzero momentum, `P_-+P_+=I`.

## Complete free contour

With `U(t)=exp(-iHt)`, define

```text
G^>(t) = -i U(t) P_+,
G^<(t) = +i U(t) P_-.
```

The two real-time contour components are

```text
G^(++)(t)
 = theta(t) G^>(t)+theta(-t) G^<(t),

G^(--)(t)
 = theta(-t) G^>(t)+theta(t) G^<(t),

G^(-+)(t)=G^>(t),
G^(+-)(t)=G^<(t).
```

They satisfy the Schwinger-Keldysh identity

```text
G^(++)+G^(--)=G^(+-)+G^(-+).
```

The retarded and advanced propagators are

```text
G^R(t)=-i theta(t) U(t),
G^A(t)=+i theta(-t) U(t),
```

and obey the homogeneous equation away from `t=0` with the canonical
equal-time discontinuity. Thus the free contour is fixed once the
stationary positive-frequency state is disclosed.

## Edge projection

The source-edge vector has zero spectral weight in the
`c_partial=0` record mode and unit total weight in the two
`|c_partial|=sqrt(2)` modes. Therefore every edge-projected CTP component
has only the free massive support

```text
E_p=sqrt(|p|^2+2 mu^2).
```

This recovers the primitive relational shell without identifying it with an
interacting charged-particle pole.

## Boundary of the result

The finite free contour is unitary and reversible. Its evolution preserves
operator norm and contains no irreversible amplification, environment
redundancy, or persistence criterion. It therefore cannot establish
physical durability.

Gauge coupling introduces Gauss-law dressing and soft-photon structure. In
an interacting massless gauge theory the charged support may be an
infraparticle threshold rather than an isolated pole. Neither outcome is
decided by this free subgate.

## Status

```text
stationary_quasifree_state_disclosed = true
free_positive_negative_spectral_projectors_derived = true
free_CTP_greater_lesser_components_derived = true
free_CTP_time_and_antitime_ordered_components_derived = true
free_CTP_identity_verified = true
free_retarded_advanced_propagators_derived = true
edge_projected_free_support_is_massive_only = true
complete_free_quasifree_CTP_contour_derived = true
physical_durability_derived = false
gauge_invariant_dressed_source_spectrum_derived = false
interacting_isolated_pole_proved = false
absolute_record_duration_computed = false
physical_source_mass_computed = false
alpha_computed = false
proof_authorized = false
```
