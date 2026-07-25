# Finite-Parent Analytic Authority v001

Date: 2026-07-24

## Purpose

This authority replaces hard-coded analytic booleans with explicit theorem
scope. It proves three finite-parent statements under stated hypotheses and
withdraws two unproved spacelike flags.

## Hypotheses

For a finite cell set `K`, let:

```text
h_K(t)=h_0+V_K(t),
V_K(t)=sum_(c in K) v_c(t) B_c(t).
```

Assume:

1. `h_0` is self-adjoint on `D(h_0)`;
2. each `B_c(t)` is bounded and self-adjoint;
3. `t -> B_c(t)` is strongly measurable;
4. every `v_c` has compact time support and is integrable; and
5. `K` is finite.

These are the finite-regulator hypotheses used by the declared parent.

## Common-domain theorem

For almost every `t`, `V_K(t)` is bounded and self-adjoint. The
Kato-Rellich bounded-perturbation theorem therefore gives:

```text
h_K(t) is self-adjoint on D(h_0).
```

The domain is independent of `t` and of the finite cell set.

## Finite propagator theorem

In the `h_0` interaction picture:

```text
V_I(t)=exp(i h_0 t)V_K(t)exp(-i h_0 t)
```

is bounded, strongly measurable, and norm-integrable on every compact
interval. Its Dyson series converges absolutely in operator norm because the
`n`th term is bounded by:

```text
(integral ||V_I(t)|| dt)^n / n!.
```

It defines a unique unitary interaction-picture propagator. Conjugating by
the free group gives the unique finite-parent propagator. Compact time
support gives finite Moller maps before and after the interaction window.

No infinite-future source-inclusive Moller limit follows from this finite
statement.

## Smooth-to-sharp stability theorem

Let `V_epsilon` be smooth bounded finite-cell approximants and `V` the sharp
finite-cell interaction. If:

```text
integral ||V_epsilon(t)-V(t)|| dt -> 0,
```

then Duhamel's formula and unitarity give, on any interval containing the
support:

```text
sup_(t,s) ||U_epsilon(t,s)-U(t,s)||
 <= integral ||V_epsilon(r)-V(r)|| dr -> 0.
```

Thus the propagators converge in operator norm, hence strongly. The theorem
does not assert this limit for approximation families that fail the stated
`L1` operator-norm condition.

## Withdrawn spacelike flags

The boolean values:

```text
spacelike_disjoint_controlled_writes_commute = true;
causal_linear_extension_independent_under_spacelike_swaps = true;
```

in `results/causal_direct_limit_redundant_record_v001.json` were emitted as
hard-coded constants. They are reclassified:

```text
spacelike_disjoint_controlled_writes_commute = ASSERTED_NOT_DERIVED;
causal_linear_extension_independent_under_spacelike_swaps =
  ASSERTED_NOT_DERIVED.
```

They are not load-bearing for the corrected causally sequential theorem.
The concurrent-cell counterexample prevents their use as an interacting
spacelike-factorization result.

## Authority table

```text
bounded_compact_time_perturbation_common_domain = DERIVED_HERE
unique_finite_unitary_propagator                 = DERIVED_HERE
smooth_to_sharp_limit_under_L1_norm_hypothesis   = DERIVED_HERE
spacelike_disjoint_write_commutation             = NOT_DERIVED
spacelike_swap_independence                      = NOT_DERIVED
```

## Fixed boundaries

```text
intermediate_asymptotic_unitary_implementability_claimed = false
infinite_future_source_Moller_limit_derived = false
complete_parameter_free_Q_spec_frozen = false
physical_Thomson_stiffness_computed = false
alpha_computed = false
proof_authorized = false
```
