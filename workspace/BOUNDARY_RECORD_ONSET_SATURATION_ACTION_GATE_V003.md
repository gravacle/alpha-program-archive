# Relative Record-Orthogonalization Budget Gate v003

Date: 2026-07-23

## Why v003 exists

Version 001 privileged one stationary branch. Version 002 corrected that
error but made two further overstatements:

```text
it said an arbitrary common additive Hamiltonian cancels;
it called an integrated energy uncertainty a physical action.
```

Only a factored common left-unitary evolution cancels automatically. The
geometric quantity is a Fubini-Study energy-uncertainty budget, not yet the
dynamical action appearing in `exp(iS/hbar)`.

Versions 001 and 002 are not authority.

## Common closed dilation

Let the source, designated record subsystem, and required environment form
one closed Hilbert space. From one common ready state `|r>`, the two
source-conditioned closed-dilation unitaries are

```text
U_0(tau), U_1(tau).
```

The conditional global states are

```text
|R_0> = U_0(tau_*) |r>,
|R_1> = U_1(tau_*) |r>.
```

Their overlap is

```text
<R_0|R_1>
  = <r|W(tau_*)|r>,

W(tau) = U_0(tau)^dagger U_1(tau).
```

If

```text
U_a(tau)=V(tau) U_tilde_a(tau)
```

with the same left-unitary factor `V`, that factor cancels from `W`. An
arbitrary additive Hamiltonian common to both branches need not cancel when
it fails to commute with the branch-dependent dynamics.

The relative generator in the common `U_0` frame is

```text
H_W
  = i hbar [partial_tau W] W^dagger
  = U_0^dagger (H_1-H_0) U_0.
```

## Proven relative geometric bound

Import the standard Fubini-Study/Mandelstam-Tamm theorem:

```text
arccos |<r|W(tau_*)|r>|
  <= integral_cell d tau Delta H_W(tau)/hbar.
```

For orthogonal conditional global states,

```text
<R_0|R_1>=0,
```

so the analytic consequence is

```text
J_FS,rel
  := integral_cell d tau Delta H_W(tau)
  >= pi hbar/2.
```

This is an energy-uncertainty/path-length budget. It is not automatically
either branch's dynamical action, the action difference, or a coefficient in
the microscopic Lagrangian.

Global orthogonality is not yet a durable public record. Perfect readout from
the designated record subsystem requires orthogonal supports of its reduced
conditional states. Durability additionally requires persistence and
recoverability or redundancy.

## Adopted Gravacle onset rule

The allow/require boundary is adopted to select first admissible record onset
through a shortest **relative** projective path on the unique physical record
cell. Conditional on this target-value-free, target-aware Level-1 rule,

```text
J_FS,rel = pi hbar/2.
```

The lower bound is derived from the imported theorem. Saturation is adopted,
not derived. Historical target blindness is not claimed.

## Exact two-state realization

On the primitive record factor, take

```text
H_W = epsilon_rel Y,
epsilon_rel tau_*/hbar = pi/2.
```

The exact symmetric branch representatives are

```text
U_0 = (I+iY)/sqrt(2) = exp(+i pi Y/4),
U_1 = (I-iY)/sqrt(2) = exp(-i pi Y/4).
```

They obey

```text
U_0^dagger U_1 = -iY,
<0|U_0^dagger U_1|0>=0.
```

Each absolute branch moves projective distance `pi/4`; the relative distance
is `pi/2`. Here `epsilon_rel` equals the relative energy uncertainty in the
ready state. It is not an absolute branch energy or expectation value.

The post-closure contrast `P_1-P_0` is Hilbert-Schmidt orthogonal to `Y`.
Accordingly, the geometric budget does not identify a source mass or pointer
coefficient.

## Status boundary

Established:

```text
conditional overlap is governed by U_0^dagger U_1;
orthogonality requires J_FS,rel >= pi hbar/2;
the declared two-state symmetric realization attains the relative endpoint.
```

Adopted:

```text
the physical allow/require onset saturates the relative bound.
```

Not established:

```text
orthogonal reduced record supports;
physical durability;
the numerical causal-cell interval;
identification of J_FS,rel with microscopic dynamical action;
the complete source-record-environment action;
a source mass, spectral response, or alpha.
```

## Exact next gate

Construct the source-flux-conditioned record-changing operator, then derive a
complete action that fixes its source-conditioned identity phase,
post-closure pointer block, causal cell, and durability map. No geometric
uncertainty budget may be substituted for physical action without a theorem.

## Status

```text
common_closed_dilation_declared = true
conditional_overlap_relative_unitary_identity_derived = true
relative_orthogonalization_bound_imported = true
orthogonality_budget_pi_over_two_derived = true
relative_onset_saturation_derived = false
relative_onset_saturation_adopted_Level_1 = true
relative_FS_budget_fixed_conditional_on_adopted_rule = true
physical_dynamical_action_fixed = false
absolute_one_branch_energy_fixed = false
arbitrary_common_additive_hamiltonian_cancels = false
orthogonal_reduced_record_supports_derived = false
physical_durability_derived = false
unique_causal_record_interval_numerically_derived = false
relative_generator_identified_with_pointer_coefficient = false
relative_generator_identified_with_source_mass = false
record_generated_source_mass_derived = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
