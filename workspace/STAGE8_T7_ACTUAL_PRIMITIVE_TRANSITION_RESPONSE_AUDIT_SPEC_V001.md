# Stage-8 T7 Actual Primitive Transition Response Audit Spec v001

Date: 2026-07-24

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

This hostile, target-free audit tests whether the newly derived finite
transition map carries a nonzero primitive record susceptibility or merely a
unit-modulus open-line holonomy.

## Hash-pinned candidate

```text
c4dcbf5bc1e98e3dd3e4503bcc2739e8795be11b7e96873598a181eedf00d654  STAGE8_T7_ACTUAL_PRIMITIVE_CAUSAL_TRANSITION_MAP_SPEC_V001.md
f04a54f4b52489e5e67eba3445b54a2028a947828204674ad1fbcb17d19be091  scripts/derive_stage8_t7_actual_primitive_causal_transition_map_v001.py
3f7191c817435104f16c9e48fc43b4cd6f734417d0dcdc99add5acffc46b829d  stage8_execution/work/T07_actual_primitive_causal_transition_map.json
0ece7cdb1b2a947dc50a0f9a961a568dd708ff60cf828767ba1bf3cd81964e8f  scripts/verify_stage8_t7_actual_primitive_causal_transition_map_v001.py
3a722c3867d90b664ba32420b75f2ff213f7f7bbce53e247e4fc94297a59c776  stage8_execution/work/T07_actual_primitive_causal_transition_map_verification.json
```

Any mismatch aborts execution.

## A1 - Covariant incidence overlaps

On an oriented path, use the unit-character covariant incidence vectors:

```text
d_j(A_j) = -|v_j> + exp(i A_j)|v_(j+1)>,
u_j(A_j) = d_j(A_j)/sqrt(2).
```

For adjacent cells, compute exactly:

```text
<u_j(A_j),u_(j-1)(A_(j-1))>.
```

Determine separately its phase and modulus. The calculation must also cover
arbitrary orientations and a closed causal sequence, where the product
phase is the Wilson-loop holonomy.

## A2 - Normalized connected amplitude

Insert the exact overlaps into the transition theorem:

```text
a_N(A)=product_(j=1)^(N-1)<u_j(A_j),u_(j-1)(A_(j-1))>,
Z_N(A)=a_N(A)/a_N(0).
```

No branch sum or inclusive probability may be introduced.

Compute:

```text
Gamma_N(A)=-log|Z_N(A)|;
its first and second connection derivatives;
the intensive Hessian.
```

## A3 - Mandatory verdict

`NONZERO_PRIMITIVE_RESPONSE_SURVIVES` requires a nonzero target-independent
Hessian.

`OPEN_LINE_HOLONOMY_ZERO_STIFFNESS` is mandatory if every connection
perturbation changes only the phase and:

```text
|Z_N(A)|=1,
Gamma_N(A)=0,
kappa_record=0.
```

The Stage-8 battery requires exact-zero `kappa_record` to route to `BLOCKED`.
No branch sum, probability, source state, determinant, envelope change, or
residual term may repair a zero result.

## No-target attestation and fixed status

```text
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
