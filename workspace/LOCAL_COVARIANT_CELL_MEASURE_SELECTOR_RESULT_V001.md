# Local-Covariant Cell-Measure Selector Result

## Verdict

```text
MEASURE_NOT_UNIQUE_STRICT_LOCALITY_DECISION_REQUIRED
```

The existing requirements of positivity, normalization, Lorentz covariance,
additivity, and parent-cell refinement compatibility do not uniquely select
the uniform measure on a causal diamond.

No alpha, measured coupling, mass, endpoint, or cosmological value entered
the specification or computation.

## Exact calculation

For a unit-duration causal diamond in 3+1-dimensional Minkowski space,

```text
Vol(D)/pi                = 1/24,
integral_D u d^4x / pi   = 1/1440,
integral_D u^2 d^4x / pi = 1/50400.
```

Thus the uniform measure has

```text
E_0[u] = 1/60,
```

whereas the target-independent profile

```text
d mu_1 proportional to [1+u(x)] d^4x
```

has

```text
E_1[u] = 36/2135.
```

The two normalized measures are distinct.

The profile scalar

```text
u(x)=[(x-p)^2 (q-x)^2]/[(q-p)^2]^2
```

was independently checked under a nontrivial Lorentz boost. It is
nonnegative inside the diamond. Consequently every fixed nonnegative
integer `a` gives a positive normalized Lorentz-covariant measure

```text
d mu_a proportional to [1+a u(x)] d^4x.
```

Restricting a parent measure to a partition is additive and survives
refinement of that same parent cell.

## What the negative result means

The word "local" in the inherited action says that the primitive dynamics is
attached to one causal cell. It does not yet say that the density at an
event is forbidden from consulting invariant distances to that cell's tips.
The latter is a stronger, strict-local-density assertion.

Therefore a unique uniform measure follows only if Gravacle requires:

```text
The cell boundary determines where the primitive interaction is supported,
but not an event-dependent scalar weight inside that support. The primitive
density depends only on local finite-jet metric and field data.
```

That is now the precise theory decision. It may not be smuggled in as though
Lorentz covariance or normalization had already proved it.

## Status

```text
target_independent_competitor_family_exhibited = true
existing_measure_requirements_unique = false
strict_local_density_already_derived = false
unique_covariant_spectral_measure_derived = false
hypothesis_promoted_to_principle = false
alpha_computed = false
```
