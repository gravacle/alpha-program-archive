# Stage-8 T7 Primitive Connected-Scalarization Dichotomy Result v001

Date: 2026-07-24

## Verdict

```text
PRIMITIVE_CONNECTED_SCALARIZATION_UNDERDETERMINED
```

The relay closes the open-cell type mismatch, but the current primitive
authorities do not determine one connected scalar amplitude.

## Record-line branch

On one-dimensional root and endpoint lines, the normalized
connection-returned maps are scalars. Relay composition therefore gives:

```text
Z_K = product_c Z_c.
```

This is the unique line-only composition. It is not a uniqueness theorem for
connected dynamics. The exact family

```text
B_lambda
 = |10><01| + |01><10| + lambda |11><11|
```

has identical vacuum and one-record restrictions for every `lambda`, while
its two-record action changes. Thus the one-cell maps, relay typing, and
disjoint monoidality fix the disconnected product but do not fix the
connected completion.

## Shared-source branch

For the exact incidence projectors

```text
P_j=|d_j><d_j|/2,
K_N=P_(N-1)...P_0,
```

every `K_N`, `N=1,2,3`, is a non-scalar source operator. Exact scalar
functionals give:

```text
                  N=1    N=2    N=3
omega_(P0)(K_N)     1     1/4      0
omega_(P1)(K_N)   1/4     1/4    1/16
omega_(P2)(K_N)     0       0      0
Tr(K_N)/4          1/4    1/16      0
<d_(N-1)|K_N|d_0>/2 1    -1/2    1/4
```

Therefore:

```text
the existing incidence states do not give one common scalar;
the normalized source trace has a zero three-cell baseline;
and the nonzero causal-line functional requires a final source line that has
not been derived as the public completed endpoint.
```

No one of these functionals was selected.

## Consequence

The current primitive data support two incomplete constructions:

```text
record-line relay:
  unique scalar product, connected dynamics underdetermined;

shared-source connected parent:
  connected operator fixed in the declared branch, scalar closure
  underdetermined.
```

Neither satisfies both connectedness and scalar uniqueness. The zero-free,
linked-cluster, and Duhamel/intensive-Hessian obligations therefore remain
non-executable.

The next step is a genuine architecture decision, not more algebra on the
same inputs. An admissible successor must choose and defend one of:

```text
move connected amplitude/cluster closure downstream to complete Q_spec,
where the parent-supplied source state is available;

derive a primitive public final source line from existing record semantics,
without selecting it because its amplitude is nonzero;

or revise primitive T7 to an operator-valued response theorem and derive the
later scalar matching separately.
```

No new principle was adopted by this result.

## Independent verification

The primary calculation used exact rational matrices. The verifier rebuilt
all source values from the normalized incidence Gram matrix and imported no
primary matrix construction. It returned:

```text
pass = true
```

## Artifact hashes

```text
fdb7abb30c1db155df95bd062e3bc77ea5a1ba1462689e6004db951e347ab430  STAGE8_T7_PRIMITIVE_CONNECTED_SCALARIZATION_DICHOTOMY_SPEC_V001.md
4b86766abe07db88f34a27c002ffad0a6d36cbb6e94f24d2121dbe38ba20d55d  scripts/derive_stage8_t7_primitive_connected_scalarization_dichotomy_v001.py
0442795982753c2c62a940c827efde9c08fe1c4664a6c202d3aaaec8badf6aab  stage8_execution/work/T07_primitive_connected_scalarization_dichotomy.json
34f5eb911454d77ecd75ee006375c955e028af13a8d2ce5882570f59cd4cc073  scripts/verify_stage8_t7_primitive_connected_scalarization_dichotomy_v001.py
e0406885384464f96cbc870cf1d467570108046e02db732368f37b8737e5d5a0  stage8_execution/work/T07_primitive_connected_scalarization_dichotomy_verification.json
```

## Fixed status

```text
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
