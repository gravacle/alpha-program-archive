# Causal Direct-Limit Redundant-Record Result v001

Date: 2026-07-24

## Result

Under the already adopted Primitive Reversible Record-Write Principle, causal
repetition on future-ready cells derives a recoverable asymptotic pointer
sector.

For pointer label `h`, after `N` writes:

```text
|h>_source |0>^tensor_N
  -> |h>_source |h>^tensor_N.
```

The two conditional environment sectors are exactly orthogonal for every
`N>=1`. Every copied cell separately reveals `h`. Tracing any unobserved
ideal copy removes the source off-diagonal term.

For imperfect conditional records with one-cell overlap `|gamma|<1`,

```text
|<E_0^(N)|E_1^(N)>|=|gamma|^N,
```

so distinguishability and redundancy increase without a new coefficient.

The macroscopic pointer averages

```text
M_N=(1/N) sum_j Z_j
```

form a central sequence. If `O` has support on at most `m` cells,

```text
||[M_N,O]|| <= 2m ||O||/N -> 0.
```

Their distinct limiting expectations separate the two asymptotic public
record sectors.

Spacelike-disjoint controlled writes commute. Different linear extensions
of the same causal order therefore give the same circuit whenever they differ
only by interchanging spacelike-disjoint writes. Causally dependent writes
retain their causal order.

## Scope

This result does not derive the primitive controlled-write rule; that rule
was already adopted. It also inherits the ready-state boundary condition and
finite interaction-window closure. It establishes the outgoing
record-recoverability part of Fork 8 without selecting a branching number or
decay law.

It does not derive the covariant spectral measure. Consequently it does not
complete the parent action or promote the entire direct-limit hypothesis to a
principle.

## Status

```text
ideal_conditional_environment_sectors_orthogonal = true
imperfect_conditional_overlap_decays_exponentially = true
macroscopic_pointer_central_sequence_derived = true
causal_linear_extension_independence_scoped = true
outgoing_record_recoverability_derived_under_adopted_write_rule = true
primitive_write_rule_derived_here = false
ready_state_boundary_condition_derived = false
unique_covariant_spectral_measure_derived = false
fork_8_closed = false
hypothesis_promoted_to_principle = false
complete_parent_action_derived = false
alpha_computed = false
proof_authorized = false
```
