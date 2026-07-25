# BID Monoidal Extensivity Derivation v001

Date: 2026-07-23

## Purpose

This derivation replaces the terminated V010 normalized direct-sum response.
It contains no coupling target and computes no alpha.

## Premise

Independent record-forming regions compose symmetrically monoidally:

```text
K=disjoint_union_i K_i,
H(K)=tensor_i H(K_i),
r(K)=tensor_i r(K_i),
U_K(A)=tensor_i U_(K_i)(A_i).
```

This is the quantum composition law for independent systems. It is a
physical premise of V011 and is tested against the direct-sum competitor.

## Theorem 1: Exact disjoint additivity

For each completed branch, let `p(K_i)` be the public endpoint state derived
by `BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md`. Define the
normalized record-transition amplitude and attenuation:

```text
A_K(A)
  =<p(K)|U_K(A)|r(K)>
   /<p(K)|U_K(0)|r(K)>,
Gamma_K(A)=-log|A_K(A)|.
```

For disjoint independent components,

```text
A_K(A)
 =product_i [
    <p(K_i)|U_(K_i)(A_i)|r(K_i)>
    /<p(K_i)|U_(K_i)(0)|r(K_i)>
  ]
 =product_i A_(K_i)(A_i).
```

On any connected logarithm branch containing the unperturbed point,

```text
Gamma_K(A)=sum_i Gamma_(K_i)(A_i).
```

Differentiating twice gives a block-direct-sum Hessian. If `N` identical
cells receive the same perturbation `s a`,

```text
Gamma_N(s a)=N Gamma_1(s a),
Gamma_N''(0)/N=Gamma_1''(0).
```

The response density is therefore intensive and is produced by composition,
not by multiplying a diluted result after the calculation.

## Theorem 2: V010 direct-sum obstruction

The V010 normalized global ray gives, for its declared canonical mode,

```text
R_L(a,a)=L^-4,
||b_L||^2=4 sin^2(pi/L),
kappa_L=1/[4 L^4 sin^2(pi/L)]
       ~1/[4 pi^2 L^2]
       ->0.
```

This is incompatible with a nonzero extensive local stiffness. The route is
rejected. No factor of `L^2`, `L^4`, cell count, or volume may be supplied
afterward.

## Theorem 3: Connected-cellulation obligation

Disjoint additivity alone does not prove a thermodynamic response on a
connected cellulation. Let

```text
B_K(A)=sum_(X subset K) b_X(A)
```

be the local finite-range generator on the tensor-product record carrier.
For a product or uniformly exponentially clustering preparation, the
normalized amplitude has the cumulant expansion

```text
Log A_K(A)
 =sum_(n>=1) (-i tau_R)^n/n! <B_K(A)^n>_connected.
```

Every connected cumulant is a sum over connected clusters. A volume-density
limit follows only if V011 proves:

```text
uniform finite-range/bounded local terms;
uniform preparation clustering;
a volume-independent open neighborhood of A=0 in which A_K(A) is nonzero;
uniform absolute convergence of the differentiated connected-cluster sum;
and subextensive boundary corrections across the sealed refinement class.
```

Under those conditions,

```text
gamma(A)=lim_(K exhausts R^4) -Log|A_K(A)|/N_4(K)
```

exists and its Hessian is the connected local record susceptibility. If a
zero of `A_K` approaches the origin, the cumulant series fails uniformly, or
the limit depends on cellulation, the connected response gate fails.

## Status

```text
exact_disjoint_monoidal_additivity_proved = true
root_survival_amplitude_used = false
derived_public_transition_amplitude_used = true
V010_direct_sum_zero_stiffness_reproduced = true
posthoc_extensive_factor_forbidden = true
connected_linked_cluster_density_proved = false
primitive_record_stiffness_computed = false
alpha_computed = false
```

The open connected-cell condition is carried into the record-interval and
locality gates. It cannot be silently counted as a pass.
