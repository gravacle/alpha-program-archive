# Stage-8 T7 Intrinsic-Measure Parent-Normalization Audit Spec v001

Date: 2026-07-24

## Purpose

Check whether the one-particle causal-cell interaction in the sealed parent
implements the already-derived intrinsic measure

```text
d mu_D(x)=d^4x/Vol_4(D)
```

without counting the spatial slice volume twice.

This is an upstream normalization audit. It uses no response value, coupling,
alpha, endpoint, or measured constant.

## Pinned authorities

```text
e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2  R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md
40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md
80aa4e1722c117e8195ce0fb2ae3fc37262bc8fc2ba5d79a6dd38cd1029bc26d  STAGE8_T7_HERMITE_GALERKIN_BASELINE_SPEC_V001.md
950e957ec2aa1022509b57df48f4f701e717e5dcbb18731332abbf55bf57dadd  STAGE8_T7_HERMITE_GALERKIN_NUMERICS_PROTOCOL_V001.md
```

## Geometry

In unit-duration flat coordinates let

```text
r(t)=min(t,1-t),                     0<=t<=1,
B_t={x in R^3: |x|<=r(t)},
V_3(t)=Vol_3(B_t),
V_4(D)=integral_0^1 V_3(t) dt,
M(t)=multiplication by 1_(B_t).
```

The normalized time marginal of the uniform four-volume measure is

```text
w(t)=V_3(t)/V_4(D).
```

The audit must distinguish the marginal `w(t)` from the four-density
`1/V_4(D)`.

## Competing Hamiltonian forms

The uniform intrinsic action with total record interval `tau_R` gives

```text
H_uniform(t)=[tau_R/V_4(D)] M(t).
```

An exactly equivalent conditional-slice form is

```text
H_slice(t)=tau_R w(t) [M(t)/V_3(t)]
```

away from the measure-zero tips, with the bounded product understood by its
continuous operator-valued extension.

The sealed parent instead states

```text
H_parent(t)=tau_R w(t) M(t).
```

The audit must determine whether `H_parent=H_uniform`. It may not reinterpret
the sealed unnormalized multiplication operator `M(t)` after the fact.

## Exact checks

The primary derivation must compute:

```text
V_3(t);
V_4(D);
w(t);
integral_0^1 w(t) dt;
integral_D d^4x/V_4(D);
integral_0^1 dt integral_(B_t) d^3x w(t);
and the pointwise ratio H_parent/H_uniform.
```

The independent verifier must recompute the decisive integrals through a
different symbolic route.

## Predeclared verdicts

```text
PARENT_NORMALIZATION_CONSISTENT
  iff H_parent=H_uniform almost everywhere.

PARENT_NORMALIZATION_DOUBLE_COUNTS_SLICE_VOLUME
  iff H_parent/H_uniform=V_3(t) is nonconstant and the full uniform-test
  integral differs from one.
```

On the second verdict:

```text
the old parent normalization is retained as a negative result;
the old Hermite-Galerkin amplitudes remain numerical regression data only;
a successor parent must use H_uniform or its exactly equivalent
slice-normalized form before response evaluation;
and no downstream status advances.
```

## Fixed status

```text
parent_normalization_audited = false
corrected_parent_normalization_frozen = false
physical_regulator_completed_record_baseline_derived = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
