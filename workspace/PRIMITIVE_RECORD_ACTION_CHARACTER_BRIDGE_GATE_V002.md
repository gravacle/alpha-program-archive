# Primitive Record Action-Character Bridge Gate v002

Date: 2026-07-23

## Why v002 exists

`PRIMITIVE_RECORD_CARRIER_AND_KINEMATICS_V001.md` mixed a useful exact
two-endpoint calculation with claims that its executable audit did not test.
In particular, the audit checked a declared two-dimensional representation
but did not derive the representation, the action-period normalization, or the
balanced comparison state.

Version 002 separates imported premises from deductions and adds the exact
bridge to the sealed relative Fubini-Study onset budget. Version 001 is not
authority.

## Imported and inherited premises

The following inputs are not derived here:

1. The pre-alpha V156 single-handle result supplies one ordinary
   two-endpoint comparison face, conditional on its declared boundary
   hypotheses H1-H6. It does not uniquely derive the full primitive state
   body or exclude reducible multiple-plane representations of one
   one-parameter generator.
2. Quantum action differences act through the standard additive character

   ```text
   chi(Delta S) = exp(i Delta S/hbar).
   ```

3. The compact action coordinate has period `2 pi hbar`, and the primitive
   faithful character has winding `k=+1` up to orientation reversal.
4. Record onset requires orthogonal conditional alternatives and, under the
   separately adopted Level-1 onset rule, saturates the shortest relative
   Fubini-Study path.
5. The bridge is evaluated in the standard pure `C^2` two-path comparison
   representation with its Hermitian inner product, Born overlap, and
   Fubini-Study convention. Along a differentiable character path,

   ```text
   H_rel = hbar dot(theta) G.
   ```

The first item is branch-scoped. The affine irreducibility, Bloch-ball
geometry, and `M_2(C)` effect algebra used in older wording are not derived
here. The second item imports the ordinary quantum phase law and does not
derive `hbar`. The third fixes the primitive character after that phase
coordinate has been declared; it does not determine an electromagnetic
response strength. The fifth item is standard quantum kinematics imported for
this conditional bridge; it is not supplied by V156.

## Three representation levels

The calculation keeps three objects distinct:

```text
Delta S = S_1-S_0:
  the relative action marker;

U_H(Delta S):
  its Hilbert-space relative-phase representation;

Ad_U:
  the induced conjugation action on the orientation plane.
```

After removing the common mean-action phase, the Hilbert-space operator is

```text
U_H(Delta S)
  = exp[-i (Delta S/2hbar) sigma_z].
```

Its two eigenphases are `+/- Delta S/(2hbar)`. Its adjoint action rotates the
orientation plane by the full angle `Delta S/hbar`. The older expression
`exp(J Delta S/hbar)` belongs only to that real orientation-plane action; it
is not the same operator as the Hilbert-space lift.

## Exact two-endpoint character

Choose endpoint basis vectors `|0>` and `|1>`. Up to a common phase, the
primitive unit character acts as

```text
U(theta) = diag(1, exp(i theta)),
theta = Delta S/hbar.
```

For a normalized ready state with endpoint population `p`,

```text
|r_p> = sqrt(p)|0> + exp(i phi)sqrt(1-p)|1>,
```

the squared overlap is

```text
|<r_p|U(theta)|r_p>|^2
  = p^2 + (1-p)^2 + 2p(1-p)cos(theta).
```

For fixed `p`, its minimum is

```text
(2p-1)^2,
```

attained at `theta = pi` modulo `2 pi`. Therefore exact orthogonality under
one primitive phase character is possible if and only if

```text
p = 1/2,
theta = pi mod 2 pi.
```

The balanced state and the first half-turn are deductions from the declared
orthogonality task. This calculation contains no alpha value. Historical
target blindness is not claimed.

## Exact Fubini-Study/action-marker bridge

Use the centered Hilbert-space dimensionless generator

```text
G = diag(-1/2,+1/2).
```

On the forced balanced state,

```text
<G> = 0,
Delta G = 1/2.
```

Along the primitive half-turn `0 <= theta <= pi`, the projective budget is

```text
J_FS
  = hbar integral_0^pi Delta G d theta
  = pi hbar/2.
```

The eigenphase gap of the same relative holonomy is `pi`, so its recoverable
action-marker interval is

```text
Delta S_record = pi hbar = 2 J_FS.
```

This agrees exactly with the sealed relative-onset gate's conditional value
`J_FS,rel = pi hbar/2`. The factor of two is the difference between the
projective speed, set by the generator uncertainty, and the gap between the
two generator eigenvalues.

Equivalently, along this balanced two-level geodesic,

```text
J_FS = |Delta S|/2.
```

This equality is not asserted for an arbitrary weighted state, a reducible
multi-plane carrier, or a non-geodesic evolution.

## What this does and does not establish

Established inside the declared primitive action-character branch:

```text
orthogonality_forces_balanced_endpoint_population = true
first_orthogonalizing_character_half_turn_derived = true
relative_action_marker_interval = pi*hbar
relative_FS_budget = pi*hbar/2
relative_action_marker_equals_two_FS_budgets = true
```

Not established:

```text
the V156 boundary hypotheses are universal;
affine irreducibility or one-plane exhaustion;
the Bloch ball or M_2(C) algebra;
the standard exp(i Delta S/hbar) phase law is derived from deeper dynamics;
Delta S_record is either branch's complete microscopic Lagrangian action;
the complete source-record-environment generator;
orthogonal reduced record supports or physical durability;
the causal-cell duration or volume;
the chiral-odd source mass;
the finite electromagnetic response;
alpha.
```

In particular, this gate fixes a relative holonomy/action-marker interval. It
does not yet prove which microscopic Hamiltonian and cell realize that marker.

## Next gate

Construct the complete anomaly-balanced source-record-environment/edge
dilation. Its exact reduced record channel and its chiral-odd source
self-energy must arise from the same unretuned off-diagonal matrix elements.
The route fails if the constrained operator space retains independent
rescalings of those two outputs.

## Status

```text
ordinary_two_endpoint_comparison_face_inherited_conditionally = true
unique_primitive_carrier_derived = false
bloch_ball_derived = false
M2C_algebra_derived = false
pure_C2_comparison_representation_imported = true
Hermitian_Born_overlap_imported = true
Fubini_Study_convention_imported = true
standard_additive_action_character_imported = true
primitive_unit_winding_imported = true
primitive_unit_winding_derived_here = false
balanced_ready_state_derived_from_orthogonality = true
first_half_turn_derived_from_orthogonality = true
relative_action_marker_interval_fixed = true
relative_action_marker_interval = pi*hbar
relative_FS_budget_bridge_derived = true
relative_action_marker_equals_two_FS_budgets = true
historical_target_blindness_established = false
physical_onset_action_derived = false
complete_physical_dynamical_action_fixed = false
complete_source_record_environment_operator_derived = false
physical_durability_derived = false
unique_causal_record_interval_numerically_derived = false
record_generated_source_mass_derived = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
