# Primitive Reversible Record-Write Candidate v002

## Authority correction

This file supersedes v001. The finite controlled-`X` matrix identity is valid,
but v001 incorrectly described its Hermitian logarithm as principal and
suggested more physical uniqueness and durability than the construction
earns.

This candidate is not an active Level-1 postulate and is not part of the
alpha proof path unless an upstream record-dynamics principle independently
selects it.

## Ready-subspace task

The endpoint write task

```text
|0_S 0_R> -> |0_S 0_R>,
|1_S 0_R> -> |1_S 1_R>
```

creates orthogonal conditional record states for arbitrary source amplitudes.
It does not uniquely determine the unitary on the unused input subspace.

Even under global source nondemolition, the family

```text
U_(a,b)
  = P_0 tensor [|0><0| + exp(i a)|1><1|]
    + P_1 tensor [|1><0| + exp(i b)|0><1|]
```

implements the ready-state task. Controlled `X` is the selected
`a=b=0` representative, not a theorem.

## Selected matrix representative

The candidate matrix is

```text
U_write
  = P_0^S tensor I_R
    + P_1^S tensor X_R.
```

One positive-semidefinite Hermitian logarithm is

```text
K_selected
  = (pi/2) P_1^S tensor (I_R-X_R),

exp(-i K_selected) = U_write.
```

Because `U_write` has eigenvalue `-1`, the standard analytic principal matrix
logarithm is unavailable. `-K_selected` is equally short, and infinitely many
time profiles integrate to either branch. A constant profile over an assumed
`tau_R` is only a selected implementation:

```text
H_selected = hbar K_selected/tau_R.
```

It does not derive `tau_R`.

## Durability boundary

The matrix establishes conditional endpoint distinguishability at the write
endpoint. It does not establish persistence. Controlled `X` is self-inverse;
a second application erases the record. A durable record additionally
requires a derived closure map, post-write invariant record sectors, or
redundant environmental amplification.

## Status

```text
conditional_record_orthogonality_at_write_endpoint = true
controlled_x_extension_unique = false
standard_principal_matrix_log_exists = false
selected_PSD_logarithm_adopted = false
shortest_logarithm_unique = false
constant_interaction_profile_adopted = false
tau_R_derived = false
persistence_rule_specified = false
durable_record_established = false
phase_complete_microscopic_action_derived = false
candidate_is_active_Level_1_postulate = false
finite_response_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
