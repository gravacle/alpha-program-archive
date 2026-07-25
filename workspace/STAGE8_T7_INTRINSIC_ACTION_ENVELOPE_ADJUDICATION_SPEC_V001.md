# Stage-8 T7 Intrinsic-Action Envelope Adjudication Spec v001

Date: 2026-07-24

## Status

```text
SPECIFICATION_FROZEN_BEFORE_EXECUTION
```

This gate decides how the already-classified uniform intrinsic four-volume
measure enters the already-declared local source action. It compares no
response value and may not select a realization by its completed amplitude.

The two finite ER-A/ER-B output tables have already been evaluated. That
historical fact is disclosed. The present adjudication is therefore not
called output-blind. Its admissibility tests are exact operator-measure
identities fixed entirely by the upstream action and measure authorities.

## Pinned authorities

```text
e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2  R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md
a27a2d571273494a0787e2283734ef1405d74dadfe16d64d3450bb4536e50732  FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md
b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30  CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md
7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476  BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md
40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md
202f8d8db60046a8069b1cd8fcc38f505eb95fa29578e094e005f56e967c3a35  STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.md
cb88ef62a36597b67bf8a2415ed335741a8f5f4c1f86646e7e95d3581b45b312  STAGE8_T7_INTRINSIC_MEASURE_SUPPORT_PROJECTION_NORMALIZATION_SPEC_V001.md
ef190c0b4bf4f1ddbabbe228a4dfce55bf8b27d612306d74cc1b9ba9d3ad44df  stage8_execution/work/T07_support_projection_normalization.json
dcb6b36e129edf633f4f4279d959a11526acdc7267bca4055865c32d8ab9318e  STAGE8_T7_INTRINSIC_MEASURE_PARENT_NORMALIZATION_SCOPE_CORRECTION_V001.md
```

Any authority drift blocks execution.

## A1 - Uniform cell measure

Use unit-duration coordinates:

```text
r(t)=min(t,1-t);
B_t={x in R^3: |x|<=r(t)};
V3(t)=Vol_3(B_t)=(4 pi/3) r(t)^3;
V4=integral_0^1 V3(t)dt=pi/24;
rho=1/V4=24/pi.
```

The unique intrinsic probability measure is:

```text
dmu_D=rho 1_(B_t)(x) d^3x dt.
```

Its time marginal is:

```text
w(t)=rho V3(t)=32 r(t)^3.
```

## A2 - Operator-valued disintegration

Let `E(dx)` be the position projection-valued measure on
`L2(R^3;C^4)` and:

```text
M(t)=E(B_t).
```

The conditional spatial probability measure is:

```text
dnu_t(x)=1_(B_t)(x)d^3x/V3(t)
```

away from the measure-zero tips. Its operator-valued average is:

```text
A(t)=integral dnu_t(x) E(dx)=M(t)/V3(t).
```

The action density obtained either directly or by disintegration must agree:

```text
rho M(t)=w(t) A(t).
```

Although `A(t)` alone is unbounded as `t` approaches a tip, the physical
product is exactly the bounded operator `rho M(t)`. No standalone
`M(t)/V3(t)` generator is introduced.

## A3 - Candidate adjudication

In the dimensionless unit-cell conventions already used by the finite
calculation, compare:

```text
ER-B:
  V_B(t)=tau_R rho M(t);

correctly typed time-marginal form:
  V_push(t)=tau_R w(t) A(t);

previously implemented ER-A:
  V_A,old(t)=tau_R w(t) M(t).
```

Require:

```text
V_push(t)=V_B(t)
```

as an exact operator identity for every interior slice.

The old ER-A expression is admissible only if its local spacetime density
equals the classified constant density `rho`. Since its density relative to
`d^3x dt` is `w(t)=rho V3(t)`, test that no constant rescaling can make it
equal to `rho` at both `t=1/4` and `t=1/2`.

## A4 - Support-gate scope

`M(t)` remains the binary causal-support projector. The earlier support
fraction theorem:

```text
integral w(t)<psi(t),M(t)psi(t)>dt in [0,1]
```

is retained as a theorem about an event-schedule functional. It does not
derive the local spacetime action measure, because it postulates `w(t)M(t)`
instead of constructing the operator-valued disintegration of `mu_D`.

If A1-A3 pass, its label `SUPPORT_PROJECTION_NORMALIZATION_DERIVED` must not
be used as authority for the parent envelope.

## Predeclared verdicts

```text
INTRINSIC_ACTION_ENVELOPE_DERIVED_ER_B
```

iff A1-A4 pass exactly. This verdict means the apparent ER-A/ER-B fork
collapses: the correctly typed time-marginal representation and the uniform
spacetime-density representation are the same operator.

```text
INTRINSIC_ACTION_ENVELOPE_FORK_SURVIVES
```

iff both expressions represent the same uniform operator-valued measure.

```text
INTRINSIC_ACTION_ENVELOPE_GATE_BLOCKED
```

iff an authority drifts or any exact identity fails.

No result of the finite completed-amplitude comparison enters any verdict.

## Fixed status

```text
envelope_realization_derived = false
ER_A_selected = false
ER_B_selected = false
sharp_cell_implementability_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
