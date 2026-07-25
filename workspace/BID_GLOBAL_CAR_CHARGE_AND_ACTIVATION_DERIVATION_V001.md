# BID Global CAR Charge and Activation Derivation v001

Date: 2026-07-23

## Purpose

Construct the charged-handle generator and access projectors on a fermionic
particle/antiparticle carrier rather than inserting the quotient matrix
`diag(0,+1,-1)`.

No alpha or response target is used.

## Disclosed field input

Use the ordinary charged Dirac field in the disclosed `3+1` spin branch:

```text
j^mu=:bar(psi) gamma^mu psi:,
partial_mu j^mu=0.
```

For Cauchy surfaces with vanishing flux at spatial infinity,

```text
Q_Sigma=integral_Sigma j^mu dSigma_mu
```

is independent of `Sigma`. On the finite-particle domain it is the
second-quantized generator of the compact vector-`U(1)` action.

This imports standard Dirac/CAR kinematics. It does not derive the existence
of electric charge from BID.

## CAR construction

Let the one-particle carrier be

```text
K=K_particle direct-sum conjugate(K_particle).
```

On fermionic Fock space define

```text
Q=dGamma(I_particle direct-sum -I_antiparticle)
 =N_particle-N_antiparticle.
```

Then

```text
U(theta)=exp(i theta Q)
```

implements the vector character:

```text
U(theta) a_particle U(theta)^dagger
  =exp(-i theta) a_particle,

U(theta) a_antiparticle U(theta)^dagger
  =exp(+i theta) a_antiparticle.
```

The spectrum is integer on the finite-particle core. The finite-mode
executable constructs the CAR matrices, number operator, compact action, and
charge-conjugating antiunitary explicitly.

## Exact access projectors

On the full integer spectrum the charged-access projector is the spectral
projector

```text
P_ch=1_(R\{0})(Q),
```

not `Q^2`. The orientation projectors are

```text
P_+=1_((0,infinity))(Q),
P_-=1_((-infinity,0))(Q),
P_0=1_{\{0\}}(Q).
```

They are orthogonal and complete. Only on the primitive
vacuum-plus-one-excitation quotient does

```text
P_ch=Q_prim^2
```

hold.

## Charge conjugation and CPT

The finite CAR core carries an antiunitary charge-conjugation map

```text
Theta_C=U_swap K
```

that exchanges particle and antiparticle modes and satisfies

```text
Theta_C Q Theta_C^-1=-Q,
Theta_C P_+ Theta_C^-1=P_-,
Theta_C P_ch Theta_C^-1=P_ch.
```

The full spacetime CPT operator additionally reverses the standard spin and
momentum labels. That extension is inherited from the disclosed Dirac/CPT
input; the finite audit tests the load-bearing charge-sector action.

## Controlled charged-record coupling

Every source-charge-nondemolition coupling has spectral block form

```text
B=P_0 tensor B_0+P_+ tensor B_++P_- tensor B_-.
```

For the pure charged-access branch, two declared record conditions reduce
this family:

```text
neutral charged-handle inactivity: B_0=0;
CPT-even orientation-insensitive incidence:
  B_+=B_-=B_Q.
```

Then

```text
B_ch=P_ch tensor B_Q.
```

The algebraic reduction is exact given those two conditions. Their physical
content remains visible: this file does not claim that vector `U(1)` alone
forces them, nor does it cover charged record/environment factors that can
exchange source charge.

## Earned result and boundary

The physical compact charge generator, integer spectrum on the finite
particle core, exact full-spectrum access projectors, and charge-conjugation
action are constructed. The old `Q^2` formula is retained only on its proper
primitive quotient.

The existence of electric charge, the pure-branch activation conditions,
the complete connected action, the continuum interacting domain, and alpha
remain open.

## Status

```text
standard_Dirac_current_and_continuity_disclosed = true
global_CAR_particle_antiparticle_Fock_core_constructed = true
compact_vector_U1_generator_constructed = true
integer_charge_spectrum_on_finite_particle_core_derived = true
full_spectrum_charged_access_projector_derived = true
full_spectrum_P_ch_equals_Q_squared = false
primitive_one_excitation_P_ch_equals_Q_squared = true
antiunitary_charge_conjugation_constructed = true
charge_orientation_exchange_verified = true
full_spacetime_CPT_inherited_from_disclosed_input = true
general_charge_nondemolition_block_family_derived = true
pure_charged_controlled_coupling_derived_given_two_record_conditions = true
two_record_conditions_derived_from_vector_U1_alone = false
complete_connected_source_record_action_derived = false
alpha_computed = false
proof_authorized = false
```
