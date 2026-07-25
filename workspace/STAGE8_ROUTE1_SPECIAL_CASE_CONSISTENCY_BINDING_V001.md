# Stage-8 Route-1 Special-Case Consistency Binding v001

## Binding

Route 1 remains a mandatory consistency falsifier for Route 2.

Its frozen definition is O6 of
`STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md`, SHA-256
`2f2aa7f7397b70616fa5c9e8ed628ca1d1e819bb698133a169c6d544086b3cde`.

Its sealed execution is reported in
`STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_RESULT_V001.md`, SHA-256
`76f5505e3aa1fdc11102f782ed8ee40e49787bb38e3a2524e17b92fd8de46740`.

The same generic operator-compression implementation reproduced:

```text
maximum completed-component error   4.45e-16
maximum exhaustive-kernel error     3.34e-16
```

## Interpretation

This passes the one-dimensional special-case architecture check. It does
not show that the actual finite Lorentzian parent has a derived
one-dimensional Route-1 restriction. It cannot select the complete
`Q_spec` state, scalar functional, response coefficient, coupling, or
alpha.

The falsifier remains active: any downstream Route-2 construction that
fails this exact special case is blocked.

## Protected status

```text
route1_special_case_consistency_falsifier_frozen = true
route1_special_case_consistency_falsifier_passed = true
actual_parent_route1_line_restriction_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
