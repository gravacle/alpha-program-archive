# BID Full Dirac/CAR Source Typing Derivation v001

Date: 2026-07-23

## Purpose

Put the local Dirac source, boundary Hilbert space, particle/antiparticle
carrier, vector charge action, and the earlier two-state chirality quotient
in one type-correct construction. No alpha value or electromagnetic response
target is used.

## Disclosed ordinary-branch inputs

This construction uses:

```text
an oriented, time-oriented, globally hyperbolic 3+1 spacetime;
a spin structure and complex Dirac bundle S;
the standard vector-U(1) charged Dirac equation;
standard CAR quantization;
and an ordinary exterior-vacuum polarization.
```

The exterior-vacuum polarization is the usual positive/negative-frequency
split in the stationary asymptotic branch. It is a disclosed state choice,
not a polarization derived by BID and not a canonical construction on every
nonstationary spacetime.

## Local source and chirality

The local Dirac fiber is

```text
S=S_L direct-sum S_R,
P_L=(I-gamma^5)/2,
P_R=(I+gamma^5)/2.
```

Both `S_L` and `S_R` have complex dimension two. The vector charge action is
scalar on the local Dirac factor, so its generator commutes with `gamma^5`.
Charge conjugation is different: its antiunitary spin action obeys

```text
C_spin gamma^(5*) C_spin^(-1)=-gamma^5,
```

and therefore exchanges left and right chirality while also reversing
charge. Thus chirality and vector charge are commuting observables, but
particle/antiparticle exchange does not preserve a fixed chirality label.

The two-state carrier used
in the earlier finite incidence model is the multiplicity-free chirality
quotient obtained after suppressing the unchanged two-component spin
multiplicity:

```text
S_L direct-sum S_R
  -> span{|L>,|R>}.
```

It is not a particle/antiparticle quotient. For a massive Dirac source, the
local equation couples left and right chiral components, and `gamma^5` does
not preserve the positive/negative-frequency subspaces.

## Positive Cauchy-data Hilbert space

For a spacelike Cauchy surface `Sigma` with future unit normal `n`, compactly
supported Cauchy data carry

```text
<psi,phi>_Sigma
  =integral_Sigma bar(psi) slash(n) phi dSigma.
```

The integrand is the positive hypersurface form

```text
h_n(psi,phi)=psi^dagger gamma^0 slash(n) phi.
```

Writing a future unit normal as `n=(n^0,vector(n))`, the eigenvalues of
`gamma^0 slash(n)` are

```text
n^0+|vector(n)|,
n^0-|vector(n)|,
```

each twice. Both are positive because `n^0>|vector(n)|`. This proves local
positivity for every future timelike normal rather than for one sampled
normal.

Current conservation and standard well-posedness of the Dirac equation make
the evolution map between Cauchy surfaces isometric. Completion gives the
one-solution Hilbert space `H_q` for charge `q`. Surface independence,
completion, and well-posedness are standard globally hyperbolic Dirac
results disclosed here; the finite executable checks their local algebraic
typing, not the continuum theorem.

## Particle and antiparticle carrier

In the disclosed stationary exterior-vacuum branch, let `H_D(q,A)` be the
self-adjoint stationary Dirac Hamiltonian and let

```text
Pi_+=1_((0,infinity))(H_D),
Pi_-=1_((-infinity,0))(H_D)
```

be its orthogonal spectral projectors, with zero modes treated separately if
present. Define

```text
K_particle=Pi_+ H_q,
K_antiparticle=conjugate(Pi_- H_q),
K=K_particle direct-sum K_antiparticle.
```

In the source-free stationary exterior used by the executable, the Weyl-basis
antiunitary `C_spin=i gamma^2 K` satisfies

```text
C_spin H_D(p) C_spin^(-1)=-H_D(-p),
C_spin Pi_+(p) C_spin^(-1)=Pi_-(-p).
```

For a charged background the corresponding statement relates
`H_D(q,A)` to `H_D(-q,A)` (equivalently to the charge-conjugated background);
it is not assumed for a charge-asymmetric background without that
transformation.

The conjugate Hilbert space uses

```text
<conjugate(u),conjugate(v)>_conjugate(K)
  =<v,u>_K,
```

and carries the opposite vector character. Standard CAR quantization then
gives the fermionic carrier

```text
F_a(K).
```

On its finite-particle core,

```text
Q=dGamma(I_particle direct-sum -I_antiparticle)
 =N_particle-N_antiparticle,
U(theta)=exp(i theta Q).
```

Thus `Q` has integer spectrum and generates the compact vector action.
The continuum Fock construction and the self-adjoint second-quantized
generator are standard CAR consequences of the disclosed polarized
one-particle Hilbert space. The executable builds a finite spectral cohort
with the same ranks, conjugation, and charge action as a type check.

## Relation to the finite boundary map

The boundary-normal Riesz map derived in the local source file is

```text
M_(n,rho,delta)=rho slash(n) exp(i delta gamma^5).
```

In the rest frame, after suppressing the unchanged two-component spin
multiplicity, its unit representative is the earlier two-state map

```text
C_delta=
  [[0,exp(i delta)],
   [exp(-i delta),0]].
```

This establishes the precise relation:

```text
finite two-state label = chirality quotient;
global CAR sign label = particle versus antiparticle;
Q sign = charge orientation.
```

The labels must not be identified. Vector charge commutes with chirality,
whereas charge conjugation exchanges both charge orientation and chirality.

## Boundary

This construction does not derive:

```text
the existence of charged Dirac matter;
the 3+1 spin branch;
the exterior-vacuum polarization on a general spacetime;
the source mass or interacting pole;
the complete charged source-record coupling;
or alpha.
```

## Status

```text
three_plus_one_spin_Dirac_branch_disclosed = true
local_Dirac_chiral_fiber_typed = true
positive_Cauchy_data_Hilbert_space_constructed = true
Dirac_evolution_isometric_given_standard_current_conservation = true
ordinary_exterior_vacuum_polarization_disclosed = true
stationary_Dirac_spectral_projectors_constructed_given_disclosed_branch = true
charge_conjugation_intertwines_positive_and_negative_spectral_subspaces = true
particle_antiparticle_one_particle_carrier_constructed_given_polarization = true
fermionic_Fock_CAR_carrier_constructed_given_standard_CAR = true
compact_vector_U1_action_constructed = true
integer_charge_spectrum_on_finite_particle_core_derived = true
chirality_commutes_with_vector_charge = true
charge_conjugation_exchanges_chirality = true
chirality_particle_antiparticle_conflation_rejected = true
two_state_chirality_quotient_relation_derived = true
existence_of_charged_Dirac_matter_derived_by_BID = false
vacuum_polarization_derived_by_BID = false
continuum_CAR_theorem_derived_by_finite_audit = false
physical_source_mass_computed = false
complete_connected_source_record_action_derived = false
alpha_computed = false
proof_authorized = false
```
