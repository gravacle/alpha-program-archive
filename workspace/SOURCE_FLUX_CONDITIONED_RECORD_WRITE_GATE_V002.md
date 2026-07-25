# Source-Flux-Conditioned Relative Record-Holonomy Gate v002

Date: 2026-07-23

## Why v002 exists

Version 001 compared two pure active-branch vectors that differed by a global
sign. Their inequality did not demonstrate a physical source-relative phase.
Version 002 uses a coherent zero/one-source superposition: the unresolved
active-branch identity phase changes the joint source-record density matrix
while leaving the reduced record density unchanged.

Version 001 also called the conditional integrated write holonomy a complete
derived operator. Version 002 restricts the result to what the assumptions
actually fix. Version 001 is not authority.

## Declared primitive flux sector

On the declared zero-or-one unit-character source-crossing sector, inherit

```text
Q_Sigma = integral_Sigma j^mu dSigma_mu,
spec(Q_Sigma)={0,1}.
```

This is a branch input: it is the number/charge flux of one primitive
crossing, not a derivation of every local current-flux spectrum.

For the **charged handle only**, adopt:

```text
Q_Sigma=0  => no charged-record write;
Q_Sigma=1  => the charged-record channel reaches first orthogonal onset.
```

Other interactions or record handles may still evolve on the zero-flux
branch.

## Relative geodesic classification

For an affine constant-axis representative on the primitive record factor,
write the active traceless generator as

```text
h' = v_x X + v_y Y + v_z Z.
```

The ready-state survival amplitude is

```text
cos(theta)-i(v_z/|v|)sin(theta),
theta=|v| tau_*/hbar.
```

At first orthogonal onset,

```text
theta=pi/2,
v_z=0.
```

The surviving equatorial angle is changed by endpoint rephasing. Choosing
`Y_R` as representative, the **integrated record-changing holonomy** is

```text
K_write,rel = (pi/2) Q_Sigma tensor Y_R
```

up to endpoint rephasing and orientation reversal. The corresponding
ready-subspace unitary is

```text
U_write
  = (I-Q_Sigma) tensor I_R
    + Q_Sigma tensor (-iY_R).
```

This conclusion is conditional on the adopted zero-flux rule and the adopted
relative-onset saturation rule. It does not identify the Fubini-Study budget
with a complete microscopic dynamical action.

## Unresolved source-conditioned identity phase

The family

```text
U_chi
  = (I-Q_Sigma) tensor I_R
    + exp(-i chi) Q_Sigma tensor (-iY_R)
```

produces the same conditional record projectors for every `chi`.

For a coherent source superposition, different `chi` values change the joint
source-record density matrix, even though tracing out the source yields the
same reduced record density. Thus `chi` is not a global phase and cannot be
removed by the record-only comparison quotient.

Equivalently, the integrated identity term

```text
chi Q_Sigma tensor I_R
```

remains physically unresolved. It can affect later source coherence and must
be fixed or excluded by the complete action before response evaluation.

## What this gate fixes

```text
the record-changing relative holonomy class on the declared zero/one flux
ready subspace, conditional on the two adopted onset rules.
```

## What it does not fix

```text
the source-conditioned identity phase;
the operator on every unused source-record-environment subspace;
post-closure pointer stabilization;
durability, redundancy, or causal-cell stitching;
the source scalar/pseudoscalar coefficient or mass;
the physical dynamical action, response, or alpha.
```

## Exact next gate

Derive the source-conditioned identity phase and the post-closure
scalar/pseudoscalar block from one complete parameter-free boundary action,
or prove the final physical response independent of them.

## Status

```text
unit_source_flux_sector_inherited = true
zero_flux_no_charged_write_adopted = true
relative_onset_saturation_inherited_as_adopted = true
equatorial_first_onset_holonomy_class_derived_conditionally = true
integrated_record_changing_holonomy_fixed_conditionally = true
complete_physical_write_operator_derived = false
physical_dynamical_action_fixed = false
source_conditioned_identity_phase_fixed = false
complete_source_record_environment_operator_derived = false
post_closure_pointer_coefficient_derived = false
source_odd_scalar_pseudoscalar_coefficient_derived = false
physical_durability_derived = false
record_generated_source_mass_derived = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
