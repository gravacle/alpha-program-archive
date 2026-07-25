# Local-Covariant Cell-Measure Selector

## Status

Forward specification for Requirement R3.1.

This selector asks whether the principles already adopted by the clean-room
program uniquely determine the measure on one primitive causal record cell.
It does not introduce a measured coupling, endpoint, mass, or cosmological
quantity. Alpha is excluded from construction, adjudication, and reporting.

## Fixed inherited inputs

The selector may use only the following previously disclosed inputs:

1. the ordinary branch is 3+1-dimensional, Lorentzian, and local at the
   primitive causal cell;
2. the primitive cell is a finite causal diamond with tips `p` and `q`;
3. the measure is positive, normalized on one cell, and countably additive;
4. the construction is Lorentz covariant under simultaneous transformation
   of the cell and its fields;
5. the response is natural under admissible subdivisions and common
   refinements;
6. the primitive interaction has no target-derived coefficient.

No stronger meaning of "local" may be inserted after this specification is
sealed.

## Competing readings

### L0: strict local-density reading

The primitive density may depend only on local finite-jet field and metric
data at the event. The tips determine the support of the interaction but do
not provide an event-dependent scalar inside that support.

In a flat empty cell, Poincare invariance and positivity then leave

```text
d mu_0(x) = d^4 x / Vol(D[p,q]).
```

### L1: boundary-profile reading

The primitive density may also depend on Lorentz scalars formed from the
event and the two cell tips. In a flat causal diamond define

```text
s_+^2(x) = (x-p)^2,
s_-^2(x) = (q-x)^2,
T^2      = (q-p)^2,
u(x)     = s_+^2(x) s_-^2(x) / T^4.
```

For every fixed nonnegative integer `a`,

```text
d mu_a(x) =
  [1 + a u(x)] d^4 x
  / integral_D [1 + a u(y)] d^4 y.
```

This is a target-independent competitor family. The audit must determine
whether each member is positive, normalized, additive, Lorentz covariant,
and compatible with subdivision of the same parent cell.

## Blind adjudication rule

The existing principles uniquely force the cell measure only if every
nonuniform `mu_a` is excluded by an inherited requirement without adding a
new physical premise.

The selector must return exactly one of:

```text
MEASURE_UNIQUE_FROM_EXISTING_PRINCIPLES
MEASURE_NOT_UNIQUE_STRICT_LOCALITY_DECISION_REQUIRED
SPECIFICATION_INCONSISTENT
```

If the second result occurs, the surviving theory question is:

```text
Does primitive Gravacle record density depend only on local finite-jet
data, with the causal diamond supplying support only, or may it depend on
invariant position relative to the cell boundary?
```

## Required checks

1. Derive the flat four-volume of the unit-duration causal diamond.
2. Derive the integral of `u(x)` over that diamond.
3. Exhibit at least two distinct normalized measures if L1 is admissible.
4. Verify Lorentz-scalar construction of `u`.
5. Verify partition additivity and parent-cell refinement compatibility.
6. State whether strict locality is already derived or remains an
   additional physical assertion.

## Non-promotion rule

Passing arithmetic checks does not promote the Causal Direct-Limit Record
Hypothesis. Promotion is forbidden unless the measure is unique, its
spectral density is derived, and the thresholded durability and outgoing
record conditions follow for that derived measure.

```text
alpha_used = false
alpha_computed = false
hypothesis_promoted_to_principle = false
```
