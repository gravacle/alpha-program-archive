# Relative Boundary Record-Onset Saturation and Action Gate v002

Date: 2026-07-23

## Why v002 exists

Version 001 treated one conditional record branch as the unchanged ready state
and assigned the full orthogonalization action to the other branch. That is a
valid implementation but not a branch-invariant result. Two conditional
record branches can move symmetrically and become orthogonal while each
travels only half the relative projective distance.

Version 002 replaces the privileged-branch statement with the invariant
relative conditional evolution. Version 001 is not authority.

## Conditional record pair

Let one ready state `|r>` evolve under the two source-conditioned unitaries

```text
U_0(tau), U_1(tau).
```

The two conditional record states at closure are

```text
|R_0> = U_0(tau_*) |r>,
|R_1> = U_1(tau_*) |r>.
```

Their overlap depends only on the relative unitary

```text
W(tau) = U_0(tau)^dagger U_1(tau):

<R_0|R_1> = <r|W(tau_*)|r>.
```

A common branch evolution cancels from `W`. This is the comparison object
appropriate to record formation.

## Proven relative-action bound

Along the relative path `W(tau)|r>`, the Fubini-Study bound is

```text
arccos |<r|W(tau_*)|r>|
  <= integral_cell d tau Delta H_rel(tau)/hbar,
```

where

```text
H_rel(tau)
  = i hbar [partial_tau W(tau)] W(tau)^dagger
```

in the chosen sign convention. Equivalently, it is the branch-Hamiltonian
difference transported to one common frame.

Perfectly distinguishable conditional records obey

```text
<R_0|R_1> = 0,
```

and therefore

```text
integral_cell d tau Delta H_rel(tau) >= pi hbar/2.
```

This lower bound is a standard quantum-geometric result. It does not require
either absolute branch to remain fixed.

## Adopted Gravacle onset rule

The allow/require boundary is adopted to be the first admissible durable
record onset. The primitive relative path is a shortest projective geodesic
on the unique physical causal record cell required by the Fundamental
Boundary Record Action Principle. Thus the relative bound is saturated:

```text
A_rel
  := integral_cell d tau Delta H_rel(tau)
   = pi hbar/2.
```

This saturation is a target-value-free, target-aware Level-1 Gravacle
principle. Quantum mechanics supplies the bound; Gravacle identifies the
physical record threshold with equality. Historical target blindness is not
claimed, so a genuinely unused later prediction remains mandatory.

## Exact two-state realization

On the primitive record factor, choose the relative geodesic representative

```text
H_rel = E_rel Y,
E_rel tau_* / hbar = pi/2.
```

Then

```text
W(tau_*) = exp(-i pi Y/2) = -iY
```

and `W(tau_*)|0>` is orthogonal to `|0>`.

A symmetric implementation illustrates why no absolute one-branch action is
fixed:

```text
U_0 = exp(+i pi Y/4),
U_1 = exp(-i pi Y/4),
U_0^dagger U_1 = exp(-i pi Y/2).
```

Each branch travels projective distance `pi/4`; their relative separation is
`pi/2`. A common Hamiltonian may be added to both branches without changing
the record comparison.

The post-closure contrast

```text
C_contrast = P_1-P_0
```

commutes with the endpoint projectors, while `Y` does not. These remain
different operator directions:

```text
Tr(Y C_contrast)=0.
```

## What is fixed

```text
minimum integrated relative action for orthogonal conditional records
  = pi hbar/2;
under the adopted onset rule, the relative record cell saturates that value;
for a constant affine-speed relative realization,
  E_rel = pi hbar/(2 tau_*).
```

## What is not fixed

```text
the action assigned to either absolute branch separately;
any common branch Hamiltonian;
the numerical proper interval tau_* and causal support;
the complete source-record-environment action;
physical durability and cell stitching;
the mapping from E_rel to kappa_I, kappa_Z, or a source mass;
the interacting source pole and residue;
the electromagnetic response or alpha.
```

The route fails if a later step treats `A_rel` as an absolute one-branch
energy, pointer coefficient, or source mass without deriving that map from
the complete action.

## Exact next gate

Construct one complete source-conditioned cell action and determine whether
its branch difference, source-odd block, and post-closure pointer block are
fixed components of one parameter-free operator. Common-mode and
pointer-preserving deformations must remain explicit until excluded.

## Status

```text
conditional_record_overlap_reduced_to_relative_unitary = true
orthogonal_record_relative_action_lower_bound_derived = true
allow_require_relative_onset_saturation_adopted_Level_1 = true
historical_target_blindness_established = false
integrated_relative_write_action_fixed = true
constant_relative_geodesic_energy_in_terms_of_tau_derived = true
absolute_one_branch_write_action_fixed = false
common_branch_hamiltonian_fixed = false
unique_causal_record_interval_numerically_derived = false
complete_source_record_environment_action_derived = false
physical_durability_derived = false
relative_write_energy_identified_with_pointer_coefficient = false
relative_write_energy_identified_with_source_mass = false
record_generated_source_mass_derived = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
