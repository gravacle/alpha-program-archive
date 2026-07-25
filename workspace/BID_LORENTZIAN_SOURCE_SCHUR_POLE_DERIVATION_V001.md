# BID Lorentzian Source Schur-Pole Derivation v001

Date: 2026-07-23

## Purpose

Embed the finite source-edge resolvent in the disclosed `3+1`, signature
`(+---)` Lorentzian source theory and determine whether it produces a real
timelike primitive pole. No observed mass, coupling, endpoint, or alpha value
is used.

## Euclidean and Lorentzian roles

The SP17 Laplace-compatible operator uses the self-adjoint cellular
quadrature

```text
c_partial=i Gamma_cell b_partial,
c_partial^2=b_partial^2.
```

The Lorentzian action kernel is not obtained by copying the Euclidean
self-adjoint zero-form without its reality factor. For a Hermitian
`c_partial`,

```text
gamma^0 (gamma^5 tensor c_partial)^dagger gamma^0
 =-gamma^5 tensor c_partial.
```

Thus `bar(Psi)(gamma^5 tensor c_partial)Psi` is anti-Hermitian. A real
Lorentzian action uniquely selects the Hermitian bilinear

```text
i bar(Psi)(gamma^5 tensor c_partial)Psi
```

up to the already fixed incidence orientation. This factor is forced by
Dirac reality before examining any pole.

Let

```text
mu=tau_R/T_R > 0
```

be the dimensional incidence rate. The primitive Lorentzian inverse kernel
on a locally flat stationary cell is

```text
K_L(p)
 =slash(p) tensor I_3
  +i mu gamma^5 tensor c_partial.
```

## Timelike shell

Because `gamma^5` anticommutes with every `gamma^mu` and `c_partial` acts on
the record factor,

```text
K_L(p)^2
 =p^2 tensor I_3-mu^2 I_4 tensor c_partial^2.
```

The one-cell edge projector `P_1` obeys

```text
P_1 c_partial P_1=0,
P_1 c_partial^2 P_1=2 P_1.
```

Since `P_1` commutes with `c_partial^2`, the exact meromorphic
edge-compressed inverse is

```text
P_1 K_L(p)^(-1) P_1
 =slash(p)/(p^2-2 mu^2) tensor P_1.
```

The Schur algebra fixes the pole but not a contour prescription. The
Feynman `+i0` follows only after the stationary positive-energy quasifree
state below is adopted; the full CTP matrix remains open.

The source-edge shell is therefore

```text
p^2=m_*^2,
m_*=sqrt(2) mu.
```

Using only the independently derived record interval
`tau_R=pi/sqrt(2)`,

```text
m_*=pi/T_R                    (hbar=c=1),
E_* T_R/hbar=pi              (physical units).
```

This is a relational pole scale. It is not a numerical particle mass until
the absolute record duration `T_R` is independently derived.

## Positive stationary branch

Multiplication by `gamma^0` gives the one-particle Hamiltonian

```text
H(p)
 =alpha dot p
  -i mu gamma^0 gamma^5 tensor c_partial.
```

It is Hermitian and

```text
H(p)^2=|p|^2+mu^2 c_partial^2.
```

Diagonalizing `c_partial` gives record eigenvalues
`{-sqrt(2),0,+sqrt(2)}`. The source-edge vector has weight `1/2` in each
massive eigenline and zero weight in the record-zero eigenline. Therefore its
spectral measure contains only the positive massive shell, with total
nonnegative internal record weight one. It is a degenerate pair of opposite
pseudoscalar internal branches, not one already-identified scalar-mass Dirac
species. Their odd numerators cancel in the edge compression.

The edge-compressed positive-energy residue is

```text
P_1 Pi_+(p) P_1
 =1/2 [I+alpha dot p/E] tensor P_1,
```

with eigenvalues `1/2(1+-|p|/E)>0`. The stationary ordinary vacuum is the
standard quasifree positive-energy state selected by the spectral projector
of this Hermitian Hamiltonian; this is a disclosed branch input.

## What this does and does not close

This derives a primitive quasifree proper-orthochronous-Lorentz-covariant
source-edge pole and its positive free spectral weight. It reconciles the
finite Schur resolvent with the SP17 chiral quadrature by deriving the
Lorentzian `i` from action reality. Full parity covariance additionally
requires the cellular quadrature's parity law and is not asserted here.

It does not yet establish:

```text
the complete Schwinger-Keldysh state and contour;
physical durability or the absolute value of T_R;
the gauge-invariant Gauss-law/edge dressing of a charged source;
survival of an isolated pole after massless-gauge interactions;
regulator-independent interacting pole/threshold matching;
or a numerical mass, stiffness, or alpha.
```

The full theory may replace an isolated charged pole by an infraparticle
threshold. That result must be reported if obtained; this primitive pole may
not pre-decide it.

## Status

```text
Lorentz_signature_plus_minus_minus_minus_disclosed = true
Lorentzian_chiral_reality_factor_derived = true
Lorentzian_inverse_kernel_constructed = true
proper_orthochronous_Lorentz_covariance_derived = true
full_parity_covariance_derived = false
timelike_source_edge_shell_derived = true
finite_Schur_resolvent_recovered_covariantly = true
primitive_mass_relation_m_star_T_R_equals_pi_derived = true
stationary_one_particle_Hamiltonian_Hermitian = true
source_edge_massive_spectral_weight_positive = true
source_edge_internal_massive_pair_degeneracy_retained = true
stationary_quasifree_positive_energy_state_disclosed = true
Feynman_i0_follows_from_disclosed_state_not_Schur_algebra = true
complete_CTP_propagator_derived = false
physical_durability_derived = false
absolute_record_duration_computed = false
gauge_invariant_dressed_source_spectrum_derived = false
interacting_isolated_pole_proved = false
physical_source_mass_computed = false
alpha_computed = false
proof_authorized = false
```
