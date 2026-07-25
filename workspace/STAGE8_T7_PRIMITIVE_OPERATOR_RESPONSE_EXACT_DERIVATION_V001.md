# Stage-8 T7 Primitive Operator Response Exact Derivation v001

## Status

Forward derivation authority for the finite primitive operator-response
execution. This note proves the exact finite-dimensional identities used by
the numerical gate. It does not select a primitive source state, produce a
scalar primitive amplitude, take a continuum limit, compute a coupling, or
compute alpha.

Its notation and scope are those of the sealed
`STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md`.

## D1 - Isometric Stinespring map

Let `i_r:H_S -> H_S tensor H_R` be an isometry and let `W[A]` be unitary.
Then

```text
V[A]=W[A] i_r
```

is an isometry because

```text
V[A]^dagger V[A]
 =i_r^dagger W[A]^dagger W[A] i_r
 =i_r^dagger i_r
 =I_S.
```

No source state or scalarization enters this statement.

## D2 - PVM resolution and Kraus family

Let `{P_xi}` be an exhaustive orthogonal PVM on `H_R`, and choose an
orthonormal basis `{|xi,mu>}_mu` for the range of each `P_xi`. Then

```text
P_xi=sum_mu |xi,mu><xi,mu|;
sum_(xi,mu) |xi,mu><xi,mu|=I_R.
```

Define

```text
M_(xi,mu)[A]=(I_S tensor <xi,mu|)V[A].
```

Inserting the complete resolution of `I_R` gives

```text
sum_(xi,mu) M_(xi,mu)[A_-]^dagger M_(xi,mu)[A_+]
 =V[A_-]^dagger V[A_+]
 =i_r^dagger W[A_-]^dagger W[A_+] i_r.
```

Restricting the same sum to a predeclared completed set `C` gives

```text
sum_(xi in C,mu) M_(xi,mu)[A_-]^dagger M_(xi,mu)[A_+]
 =V[A_-]^dagger (I_S tensor Q_comp) V[A_+],
```

where `Q_comp=sum_(xi in C)P_xi`. Thus the direct-compression and Kraus-sum
forms are the same operator identity; neither is a scalar amplitude.

## D3 - Structural identities

For equal histories, D1 and D2 imply

```text
R_all[A,A]=V[A]^dagger V[A]=I_S.
```

Since `0<=Q_comp<=I_R`,

```text
0<=R_comp[A,A]
  =V[A]^dagger(I_S tensor Q_comp)V[A]
 <=V[A]^dagger V[A]
 =I_S.
```

Adjoint exchange follows directly:

```text
R_Q[A_+,A_-]^dagger=R_Q[A_-,A_+].
```

For `Q=I_R` or `Q=Q_comp`, both `I_S tensor Q` and each `V[A]` are
contractions. Submultiplicativity therefore gives

```text
||R_Q[A_+,A_-]||<=1.
```

These are finite operator identities. They do not assert a zero-free
neighborhood, an intensive limit, or a scalar logarithm.

## D4 - Passive source-basis covariance

Let `G_S` be unitary and put

```text
G=G_S tensor I_R;
W^G[A]=G W[A] G^dagger;
i_r^G=G i_r G_S^dagger.
```

The transformed Stinespring map is

```text
V^G[A]=W^G[A]i_r^G=G V[A]G_S^dagger.
```

Because `G` commutes with `I_S tensor Q`,

```text
R_Q^G[A_+,A_-]
 =G_S R_Q[A_+,A_-]G_S^dagger.
```

The numerical gate must reconstruct `W^G` from the conjugated generators
and evolve `i_r^G`; merely conjugating an already computed `V` is not an
independent implementation check.

This is passive basis covariance only. Gauge covariance remains a false
successor status until its endpoint intertwiners are separately derived.

## D5 - Finite Duhamel derivative

For a norm-`C^1` finite-dimensional Hamiltonian family `H_s(t)` with
propagator `W_s(t_2,t_1)`, differentiating the integral evolution equation
gives

```text
dW_s(T,0)/ds |_(s=0)
 =-i integral_0^T
      W_0(T,t) J(t) W_0(t,0) dt,
```

where `J(t)=dH_s(t)/ds|_(s=0)`.

With the ready injection and PVM held history-independent,

```text
R_Q[A_+,A_-]
 =i_r^dagger W[A_-]^dagger(I_S tensor Q)W[A_+]i_r,
```

the product rule yields

```text
delta_+ R_Q
 =i_r^dagger W[A_-]^dagger(I_S tensor Q)
    (delta W[A_+])i_r,
```

and

```text
delta_- R_Q[A_+,A_-]
 =[delta_+ R_Q[A_-,A_+]]^dagger.
```

The finite executor's Frechet/product-rule path and the independent
central-difference path are implementation checks of this identity. Their
agreement is not itself the proof and does not prove the continuum
Duhamel/intensive-Hessian equality.

## D6 - Exact Route-1 architecture control

On the one-dimensional source line, let

```text
V(theta)=U(theta)|+>:C -> C^2;
P_+=|+><+|;
P_-=|-><-|;
P_++P_-=I_2.
```

Applying the same compression rule as D2 gives

```text
R_comp(theta_+,theta_-)
 =V(theta_-)^dagger P_+ V(theta_+)
 =A_+(theta_-)^* A_+(theta_+),
```

and

```text
R_all(theta_+,theta_-)
 =V(theta_-)^dagger(P_++P_-)V(theta_+)
 =A_+(theta_-)^* A_+(theta_+)
  +A_-(theta_-)^* A_-(theta_+).
```

Thus the Route-1 control must be executed through the same generic
operator-compression implementation as the finite parent. A separate
closed-form recomputation is the expected value, not the implementation
under test.

This special-case identity does not derive a one-dimensional Route-1
restriction of the actual finite parent.

## Protected status

```text
finite_primitive_operator_response_exact_derivation_completed = true
primitive_source_scalarization_derived = false
actual_parent_route1_line_restriction_derived = false
finite_primitive_operator_gauge_covariance_derived = false
finite_primitive_operator_graded_monoidality_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
