# Stage-8 T7 Primitive Connected-Lift Derivation Spec v001

Date: 2026-07-24

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

This specification tests whether the sealed primitive BID response complex
itself supplies the connected completed-record amplitude required by T7.
It introduces no source-inclusive parent, new principle, coupling target, or
measured constant.

## Hash-pinned authorities

```text
aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a  BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md
7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476  BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md
6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb  BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md
e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6  STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md
85d24996987278b285d63b8fe15a8732e55664e7c1b09063617b66cb4bc926b4  STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_V001.md
```

Any mismatch aborts execution.

## Primitive objects

For every odd periodic response complex `K_L`, use only the sealed objects

```text
H_L=C_0(K_L;L) direct-sum C_1(K_L;L),
B_L(A)=[[0,D_L(A)],[D_L(A)^dagger,0]],
r_L=J_r,L z/norm(J_r,L z),
U_L(A;tau)=exp(-i tau B_L(A)),
tau_R=pi/sqrt(2).
```

The baseline connection `U_0` is flat with trivial plaquette and fundamental
Wilson-loop holonomy. No source Fock/CTP carrier is admissible in this test.

## L1 - Connected operator and preparation

Verify that `B_L(A)` and `r_L` are fixed by the pinned F1 incidence and root
embedding. Explicitly construct the finite matrices for `L=3,5,7`.

For the flat baseline, prove symbolically and verify numerically that

```text
D_L(0)^dagger J_r,L=0,
B_L(0) r_L=0,
U_L(0;tau) r_L=r_L
```

for every real `tau`.

## L2 - Completed-endpoint classification

Classify every fixed final ray `p_L` by its root component:

```text
p_L orthogonal to r_L;
0<|<p_L,r_L>|<1;
p_L equal to r_L up to phase.
```

Use the pinned record semantics:

```text
a completed public alternative is orthogonal to the unresolved root;
the root ray is the unresolved/survival boundary and is not a completed
record endpoint.
```

Show the baseline transition consequences:

```text
<p_L|U_L(0;tau_R)|r_L>=<p_L|r_L>.
```

An `A`-dependent final ray, or a ray defined by applying the same evolution
being tested, is inadmissible because the public final boundary must be fixed
before response evaluation.

## L3 - One-handle regression

Construct the pinned one-edge first-opening operator

```text
B_h=[[0,0,-1],[0,0,1],[-1,1,0]]
```

and verify exactly/numerically that

```text
exp(-i tau_R B_h)|r>=|p_h>,
<p_h|exp(-i tau_R B_h)|r>=1.
```

The test must identify the structural difference between the open one-handle
cell and the closed periodic response complex: the former has a distinguished
public endpoint and the latter has a covariantly constant root zero mode.

## L4 - Duhamel map

For a differentiable tangent

```text
V_L(a)=d B_L(sa)/ds at s=0,
G_L(a;tau_R)=integral_0^tau_R
  exp(iB_L(0)t)V_L(a)exp(-iB_L(0)t) dt,
```

verify the finite-dimensional identity

```text
d U_L(sa;tau_R)/ds at s=0
  =-i U_L(0;tau_R) G_L(a;tau_R).
```

Consequently, for a fixed endpoint,

```text
a_L'(0)=-i <p_L|U_L(0;tau_R)G_L(a;tau_R)|r_L>.
```

This establishes the exact tangent map but must not form `Z_L=a_L/a_L(0)`
when the completed-record baseline denominator is zero.

## L5 - Verdict

```text
PRIMITIVE_CONNECTED_LIFT_DERIVED
```

requires a fixed, derived completed-record endpoint with nonzero baseline,
one-handle reduction, and a normalized scalar amplitude on every declared
response complex.

```text
PRIMITIVE_CONNECTED_LIFT_BLOCKED
```

is required if the sealed root is stationary while every admissible
completed-record endpoint has zero baseline transition, or if only the
excluded root-survival boundary has nonzero baseline.

No `CONDITIONAL` promotion and no post-failure principle are available in
this execution.

## Downstream consequences

If blocked, T7(ii)-(iv) are not executable: a volume-uniform zero-free
neighborhood, linked-cluster density, and Duhamel/intensive-Hessian equality
cannot be asserted before the connected normalized amplitude exists.

## No-target attestation

No alpha, CODATA value, cosmological endpoint, measured coupling, or
response-selected coefficient may be read or used.

## Fixed flags

```text
connected_primitive_operator_derived = false
connected_primitive_preparation_derived = false
connected_primitive_completed_endpoint_derived = false
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
