# Stage-8 T7 Primitive Operator Response Authority Amendment v001

## Status

Forward-sealed, append-only preregistration amendment to
`STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md`.

The sealed specification remains unchanged. This amendment adds the exact
finite derivation and the no-site NumPy runtime manifest to the executor's
permitted authority set before any primitive operator-response number is
computed.

## Added authorities

| Role | Path | SHA-256 |
|---|---|---|
| Exact finite operator-response derivation | `STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_EXACT_DERIVATION_V001.md` | `a9875788301d8434113f77e3b5726b49d70d8609fbcfcc72c9fede76a1249e4a` |
| Content-addressed NumPy runtime manifest | `provenance/stage8_t7_numpy_runtime_manifest_v001.json` | `f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b` |
| Runtime-manifest builder provenance | `scripts/build_stage8_t7_numpy_runtime_manifest_v001.py` | `293f16de83384b4f42c6ccb1c1c9b4ac44564d1c579edc68548a9d22e767b05c` |

The exact derivation proves the finite algebraic identities. The executor
must still compute every declared numerical regression and may not replace
a failed computation with the proof text.

The runtime manifest was generated under the pinned Python executable with
both isolated and no-site flags set. Before importing NumPy, each executor
must:

1. require `sys.flags.isolated == 1` and `sys.flags.no_site == 1`;
2. hash-verify this amendment, the exact derivation, and the runtime
   manifest;
3. verify the pinned Python executable and every manifest-listed NumPy
   package file;
4. add only the manifest's `site_packages` directory to `sys.path`;
5. import NumPy; and
6. verify that every loaded site-package module is contained in the
   manifest with the recorded content hash.

## Ordered execution binding

Content hashes cannot mutually pin an amendment, an executor, and its
launcher without a hash cycle. The trust order is therefore fixed before
execution:

```text
this authority amendment
 -> executor/verifier source
 -> external -I -S launcher
 -> append-only execution-binding amendment
 -> execution result and receipt.
```

The execution-binding amendment must be sealed before either numerical
program runs. It must record the hashes of this amendment, both scripts,
the launcher, the runtime manifest, the sealed specification, and the exact
derivation. The launcher must pin the script hashes; the scripts must pin
this amendment and the runtime manifest.

## Scope

This amendment repairs authority provenance and runtime isolation only. It
does not change the frozen parent, PVM, completed sector, history pairs,
Route-1 falsifier, tolerances, or verdict rule.

## Protected status

```text
finite_primitive_operator_response_bundle_derived = false
finite_primitive_operator_Duhamel_tangent_derived = false
primitive_source_scalarization_derived = false
stage8_route2_architecture_amended = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
