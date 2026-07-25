# Stage-8 T7 Primitive Operator Response Verifier Successor v002

## Preserved failure

The sealed v001 primary result passed. The independent v001 verifier then
completed its calculations but blocked while serializing its result:

```text
TypeError: Object of type bool is not JSON serializable
```

The blocked artifact is preserved at:

| Artifact | SHA-256 |
|---|---|
| `stage8_execution/work/T07_primitive_operator_response_verification_v001.json` | `07bb8e40963a6f23a9f066e65a2257c0b35b1d81e6aac7fe2fd44bf602ff9057` |
| `scripts/verify_stage8_t7_primitive_operator_response_v001.py` | `75551faf7235166371aea9216f8bf67d1eb3aebfaf30cbd89c223f994802e6aa` |

The failure occurred because the Route-1 comparison returned a NumPy
Boolean in its result tree. No v001 file is changed or rerun.

## Frozen successor

The v002 verifier changes only:

1. its schema and output path from v001 to v002; and
2. the Route-1 `pass` value is converted explicitly to a built-in Python
   `bool` before JSON serialization.

It changes no operator, history, outcome, authority, target, tolerance,
derivative rule, primary result, or pass/fail criterion.

| Artifact | SHA-256 |
|---|---|
| `scripts/verify_stage8_t7_primitive_operator_response_v002.py` | `6eba9b307f129a6433a79ca4c32f81fc1b84bfc070adfa86f7b2a8c4ee67b23c` |
| `scripts/run_stage8_t7_primitive_operator_response_v002.sh` | `288070fc86f2d81a4b929eb7809445f8f42bd7833be26d167198b0067a1a421c` |
| sealed primary result | `6dbda44a0f21a28b57f114654a6df79fc091ccfd601c38518fd5cf5f21697dcc` |

The v002 launcher admits only `verify`. The primary may not be rerun under
this successor.

## Protected status

```text
finite_primitive_operator_response_bundle_derived = false
finite_primitive_operator_Duhamel_tangent_derived = false
primitive_source_scalarization_derived = false
stage8_route2_architecture_amended = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
