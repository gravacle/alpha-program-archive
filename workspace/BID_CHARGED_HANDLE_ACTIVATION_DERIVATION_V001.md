# BID Charged-Handle Activation Derivation v001

Date: 2026-07-23

## Scope

This derivation closes the active-handle question for the declared pure
charged ordinary branch only. It uses the pre-response source-flux branch and
contains no alpha or response value.

## Source-access projector

The declared local charged source-flux operator obeys

```text
spec(Q_Sigma)={0,1}.
```

Its spectral projectors are

```text
P_0=I-Q_Sigma,
P_Q=Q_Sigma.
```

The already adopted allow/require rule for this branch is:

```text
Q_Sigma=0 => no charged-record write;
Q_Sigma=1 => the charged-record channel reaches first opening.
```

Thus `P_Q` is not chosen from the three endpoint labels and is not selected by
a response. It is the spectral projector of the charged source-access
operator.

## Controlled primitive generator

Let `B_Q` be the unit-incidence operator on the closed-cell carrier of the
charged first-opening edge. The controlled charged generator is

```text
B_charged
  =P_0 tensor 0_R
   +P_Q tensor B_Q.
```

It commutes with `Q_Sigma tensor I_R`, so source flux is nondemolished in this
reduced branch. At

```text
tau_R=pi/sqrt(2),
```

it gives

```text
|0_S,r> -> |0_S,r>,
|1_S,r> -> |1_S,p_Q>.
```

The pure charged sector `P_Q H` therefore uses the handle-conditioned interval
and the public charged endpoint derived in the preceding gates. The
uncontrolled full three-handle star is not the charged branch operator.

## Boundary

This result depends on the declared `{0,1}` local flux branch and its
allow/require activation rule. It does not derive:

```text
the gravitational or mass-handle source projector;
a simultaneous gravity-plus-charge composite source sector;
the complete spinor/environment carrier;
physical durability;
or the Thomson coupling.
```

Those sectors may not be folded into `B_charged` after response evaluation.
If a composite source branch is later studied, it requires its own sealed
first-opening operator and interval.

## Status

```text
local_charged_flux_spectrum_inherited = true
charged_source_access_projector_derived_from_flux_spectrum = true
zero_flux_charged_write_absent = true
unit_flux_charged_handle_activated = true
controlled_charged_generator_derived = true
controlled_charged_generator_flux_nondemolition = true
pure_charged_branch_tau_R_authorized = true
full_three_handle_star_used_for_charged_response = false
composite_gravity_charge_branch_derived = false
complete_Q_spec_source_carrier_derived = false
primitive_record_stiffness_computed = false
alpha_computed = false
proof_authorized = false
```
