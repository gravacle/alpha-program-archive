# BID Charged-Handle Restricted-Sector Algebra v002

Date: 2026-07-23

## Why v002 exists

Version 001 inherited a `{0,1}` flux matrix and then called its spectral
projector derived. That did not derive the flux operator from the physical
current and hid the CPT-conjugate negative-charge branch. Version 001 is
historical and is not authority for source-projector provenance.

## Current and charge operator

For the declared vectorlike unit-character Dirac source, the normal-ordered
vector current is

```text
j^mu=:bar(psi) gamma^mu psi:.
```

On a Cauchy surface,

```text
Q_Sigma=integral_Sigma j^mu dSigma_mu.
```

`Q_Sigma` is the self-adjoint generator of the compact vector-`U(1)` action
on the CAR algebra. The primitive character normalization makes its spectrum
integer-valued.

The ordinary primitive first-source sector contains the vacuum plus one
particle or one antiparticle crossing. On that explicitly declared sector,

```text
spec(Q_Sigma)={-1,0,+1}.
```

This sector restriction follows from the one-primitive-source branch. It is
not a statement about the full many-particle charge spectrum.

## Forced access and orientation projectors

Charged boundary access depends on nonzero unit flux, not its orientation.
Functional calculus therefore gives the unique projector onto the nonzero
unit-flux subspace:

```text
P_ch=1_(R\{0})(Q_Sigma)=Q_Sigma^2.
```

The orientation projectors are

```text
P_+=(Q_Sigma^2+Q_Sigma)/2,
P_-=(Q_Sigma^2-Q_Sigma)/2,
P_0=I-Q_Sigma^2.
```

They are mutually orthogonal and sum to the identity on the primitive sector.
CPT exchanges `P_+` and `P_-` and leaves `P_ch` invariant.

The earlier orientation-fixed `{0,1}` branch is the restriction to
`P_0+P_+`, where `Q_Sigma^2=Q_Sigma`. Thus its formula is recovered rather
than assumed.

## Controlled charged generator

Let `B_Q` be the derived unit-incidence first-opening operator on the charged
record carrier. The source-controlled generator is

```text
B_charged
  =P_0 tensor 0_R
   +P_ch tensor B_Q.
```

The charge sign enters the compact connection/holonomy orientation, not the
primitive incidence magnitude. Because `B_charged` is a spectral function of
`Q_Sigma`,

```text
[B_charged,Q_Sigma tensor I_R]=0.
```

At the first completed-transfer interval:

```text
Q_Sigma=0:
  |0,r> -> |0,r>;

Q_Sigma=+1:
  |+,r> -> |+,p_Q>;

Q_Sigma=-1:
  |-,r> -> |-,p_Q>.
```

No coherent superposition of different total-charge sectors is required for
this statement. It is an operator identity on the direct sum of sectors and
is compatible with charge superselection.

## Boundary

This derivation fixes the active pure-charged source projector from the
physical vector current on the declared primitive one-source sector. It does
not derive:

```text
the existence or multiplicity of all charged source species;
the many-particle charge spectrum;
a simultaneous gravity-plus-charge source projector;
the connected source-record action;
the Thomson response;
or alpha.
```

## Status

```text
vector_current_operator_declared_from_Dirac_source = true
physical_current_and_charge_operator_constructed = false
compact_U1_integer_charge_spectrum_inherited_given_representation = true
primitive_vacuum_plus_one_excitation_sector_disclosed = true
primitive_minus_one_zero_plus_one_sector_declared = true
full_integer_spectrum_access_projector_equals_Q_squared = false
restricted_primitive_sector_access_projector_equals_Q_squared = true
charge_orientation_projectors_derived = true
antiunitary_CPT_operator_constructed = false
CPT_exchange_rule_inherited_conditionally = true
old_zero_one_branch_recovered_as_positive_orientation_restriction = true
coherent_cross_charge_superposition_required = false
controlled_charged_generator_flux_nondemolition = true
unique_charge_controlled_record_coupling_derived = false
pure_charged_branch_tau_R_authorized = false
composite_gravity_charge_branch_derived = false
complete_connected_source_record_action_derived = false
physical_Thomson_stiffness_computed = false
alpha_computed = false
proof_authorized = false
```
