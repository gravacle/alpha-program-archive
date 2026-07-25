# R3.4 Causal-Transported Write/Tail Result v001

## Verdict

```text
CAUSAL_TRANSPORT_CONDITIONAL
```

The covariance functional equation

```text
B_tilde(t+s)=U_0(s) B_tilde(t) U_0(s)^*,
B_tilde(0)=B
```

has the unique solution

```text
B_tilde(t)=U_0(t) B U_0(t)^*.
```

Given that rule, the interaction-picture write is exact, profile
independent for fixed integrated action, preserves the primitive endpoint,
and supplies a finite-support Moller operator relative to the free tail.
Those statements are reproducible.

## Why this is not a physical derivation

The adopted upstream principles do not presently force the displayed
covariance equation as the physical write/tail joining law. In particular,
the ordinary local static interaction is not excluded by those principles.
It fails the candidate comoving covariance and the desired endpoint, but
that failure cannot itself select the candidate after the result is known.

The gate therefore records:

```text
causal_transport_rule_derived_from_pinned_principles = false
static_sum_rejected_by_adopted_principles = false
physical_write_tail_join_derived = false
```

This prevents a mathematically successful repair from being promoted into
physics by target selection.

## Reproducible candidate facts

```text
transport covariance error:                 6.69e-15
static covariance failure:                  4.65
static-sum pointer probability:             0.3062222345
transported-candidate pointer probability:  0.9999999999999982
finite-support Moller error:                1.69e-14
```

Direct midpoint time slicing converges at second order, with successive
error ratios approaching `4`.

## Scope

```text
candidate_finite_support_Moller_operator_computed = true
physical_write_tail_join_derived = false
free_outgoing_tail_generator_inherited_from_same_parent = false
physical_in_state_selected = false
finite_energy_physical_root_derived = false
generated_descendant_durability_closed = false
complete_physical_durability_derived = false
complete_write_plus_tail_root_measure_derived = false
complete_parameter_free_Q_spec_frozen = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
