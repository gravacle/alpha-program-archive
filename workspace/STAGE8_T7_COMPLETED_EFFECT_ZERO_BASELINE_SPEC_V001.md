# Stage-8 T7 Completed-Effect Zero-Baseline Spec v001

Date: 2026-07-24

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

This append-only test strengthens the sealed primitive connected-lift result
against generalized completed-record boundaries. It does not modify or
replace the ray-endpoint execution.

## Pinned inputs

```text
b8235b89ac2f7fed5ba913df5cc67f828da1c8b374ae35cd1b29a7c7040bf8d6  stage8_execution/t0_lineage/core_scripts/43_gate4_covector_ray_v001.py
63116a5d2b6f1e557db421e9bbd9e8363f85c84ac04c5d54cb7e7dd314aab544  STAGE8_T7_PRIMITIVE_CONNECTED_LIFT_DERIVATION_SPEC_V001.md
1a6c92719410e49c4abb7770abe86e403384a2b479c9e5b528ce80d26dfce0ab  stage8_execution/work/T07_primitive_connected_lift.json
```

## Theorem obligation

Let `E_L` be any positive completed-record effect on the primitive carrier,
with `0<=E_L<=I`. The sealed no-output-without-record rule requires:

```text
<r_L|E_L|r_L>=0.
```

Prove:

```text
E_L^(1/2) r_L=0,
E_L r_L=0.
```

Because the flat primitive evolution fixes the root,

```text
U_L(0;tau_R)r_L=r_L,
```

derive:

```text
E_L U_L(0;tau_R)r_L=0.
```

For every instrument/Kraus completion `K_L` subordinate to the effect,
`K_L^dagger K_L<=E_L`, prove:

```text
norm(K_L U_L(0;tau_R)r_L)^2
 <=<r_L|E_L|r_L>
 =0.
```

Thus no positive completed-record effect or subordinate instrument can
provide a nonzero primitive baseline transition.

## Verdicts

```text
COMPLETED_EFFECT_ESCAPE_EXCLUDED
```

requires the exact theorem and an independent finite-dimensional regression.
Any counterexample with positive `E_L` and the sealed no-output condition
blocks this strengthening.

## Fixed flags

```text
connected_primitive_completed_endpoint_derived = false
connected_primitive_amplitude_derived = false
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```
