# Stage-8 T7 Intrinsic-Measure Parent-Normalization Scope Correction v001

Date: 2026-07-24

## Correction

The executed v001 normalization audit correctly evaluates the scalar-density
integral

```text
integral dt integral_(B_t) d^3x w(t)=2 pi/21
```

for a unit-duration diamond. It does **not** establish that the sealed parent
counts the slice volume twice.

That inference treated the constant function `1` as the source probability
density. The parent is a one-particle operator on `L2(R3;C4)`. Its spatial
factor

```text
M(t)=multiplication by 1_(B_t)
```

is an orthogonal support projector, and its matrix element is evaluated
against a normalized source state:

```text
<psi(t),M(t)psi(t)> in [0,1].
```

There is no additional unweighted spatial-volume integral in that matrix
element. The v001 full-cell scalar test is therefore not the parent action on
an admissible normalized state.

## Consequence

The v001 verdict

```text
PARENT_NORMALIZATION_DOUBLE_COUNTS_SLICE_VOLUME
```

is withdrawn as a physical verdict. Its arithmetic is retained as a negative
control against confusing a normalized time marginal with a four-density
acting on an unnormalized constant function.

The actual normalization question is now:

```text
Does the pushforward time marginal, combined with the unit support
projector, give total action tau_R on full support and no more than tau_R on
partial support?
```

That question is answered by the successor projection-normalization theorem.

## Fixed status

```text
v001_scalar_density_arithmetic_valid = true
v001_physical_double_count_verdict_withdrawn = true
corrected_parent_normalization_frozen = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
