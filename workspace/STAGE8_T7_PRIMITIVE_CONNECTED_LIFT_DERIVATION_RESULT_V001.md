# Stage-8 T7 Primitive Connected-Lift Derivation Result v001

Date: 2026-07-24

## Verdict

```text
PRIMITIVE_CONNECTED_LIFT_BLOCKED
```

The response-closure functional is derived, but the sealed periodic primitive
response complex does not supply the completed-record transition to which
that functional must be applied.

## Exact zero-mode result

At the flat baseline, the root embedding is the covariantly constant vertex
section. For every oriented edge `e:s->t`,

```text
(D_L(0)^dagger J_r,L z)_e
  =U_e^dagger U_(0->t)z-U_(0->s)z
  =0.
```

Therefore

```text
B_L(0)r_L=0,
exp(-i tau B_L(0))r_L=r_L
```

for every `tau` and every declared odd periodic `L`.

The execution verified the result for:

```text
L=3: dim(H_L)=405;
L=5: dim(H_L)=3125;
L=7: dim(H_L)=12005.
```

Every residual is exactly zero.

## Endpoint consequence

For every fixed endpoint ray `p_L`,

```text
<p_L|exp(-i tau_R B_L(0))|r_L>=<p_L|r_L>.
```

A completed public record alternative is orthogonal to the unresolved root,
so its baseline transition is zero and the normalized amplitude is undefined.
The root ray has baseline one, but it is the unresolved survival boundary
explicitly excluded by the pinned record semantics. A mixed ray merely
returns its unresolved-root component and is not a completed alternative.

Defining the final ray from the perturbed evolution would choose the boundary
after seeing the response and is therefore inadmissible.

## Positive control

The same implementation reproduces the open one-handle theorem:

```text
tau_R=pi/sqrt(2),
exp(-i tau_R B_h)|r>=|p_h>,
<p_h|exp(-i tau_R B_h)|r>=1.
```

The endpoint-transfer error is `8.34e-16`. The failure on `K_L` is therefore
not an exponential/evolution failure. It is the structural difference
between:

```text
an open first-opening cell with a distinguished public endpoint; and
a closed periodic complex whose parallel root is a zero mode.
```

## Duhamel map

The finite tangent identity

```text
dU_L(sa;tau_R)/ds at s=0
  =-i U_L(0;tau_R) G_L(a;tau_R)
```

was independently compared with a central finite difference on the
`L=3`, 405-dimensional carrier. Relative error:

```text
1.58e-9.
```

Thus the local Duhamel tangent is well defined. What is absent is the
nonzero completed-record baseline needed to normalize it into the T7
connected amplitude and intensive Hessian.

## Proof implication

The current primitive data cannot satisfy T7(ii)-(iv). Before zero-free,
linked-cluster, or thermodynamic-Hessian analysis can begin, a target-free
theorem must construct a connected exhaustion with:

```text
a fixed completed public endpoint;
nonzero flat-baseline transfer from the derived preparation;
reduction to the one-handle endpoint amplitude; and
an exact natural map to the periodic F1 tangent G_L.
```

This cannot be repaired by using root survival, choosing an endpoint after
evolution, or importing the downstream source-inclusive CTP parent.

## Fixed status

```text
connected_primitive_operator_derived = true
connected_primitive_preparation_derived = true
connected_primitive_completed_endpoint_derived = false
connected_primitive_amplitude_derived = false
finite_Duhamel_tangent_map_verified = true
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
