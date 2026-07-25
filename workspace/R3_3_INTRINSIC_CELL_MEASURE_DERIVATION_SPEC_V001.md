# R3.3 Intrinsic Cell-Measure Derivation

## Status

Supervised reproduction and inherited-text adjudication.

The measure-selector result established that covariance, positivity,
normalization, and partition additivity alone permit

```text
d mu_a proportional to [1+a u_cell(x)] d^4x.
```

Supervision requires one further derivation attempt before any strict-locality
principle may be adopted. This specification fixes that attempt. Alpha and
all measured couplings are excluded.

## Authoritative inherited response clauses

The adjudication uses these existing BID V011 requirements:

1. Each disjoint causal cell supplies its own `H_c`, `r_c`, `U_c`, and `A_c`;
   the many-cell response is assembled from those cell contributions
   (`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md`, lines 1249-1257).
2. Each cell contributes its own `V_cell` times the local quadratic response
   (lines 1380-1389).
3. A residual shape-dependent scalar fails the frozen face-measure gate
   (lines 1391-1395).
4. The response map must commute with pullback to common refinement and its
   intensive coefficient must be invariant under elementary refinement
   (lines 1397-1412).
5. The final obligations explicitly require refinement naturality with no
   shape-dependent scalar (lines 1746-1747).
6. A response limit that depends on cellulation fails
   (`BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md`, lines 116-118).

Together these clauses bind response assembly to intrinsic per-cell data:
when a region is promoted to an elementary cell in a refinement, its
response is computed using that cell's own `V_cell`, state, generator, and
measure. A weight inherited from an arbitrarily chosen parent is not an
intrinsic cell datum.

## Exact nested-diamond test

Use the unit-duration parent causal diamond

```text
D[p,q], p=(-1/2,0,0,0), q=(1/2,0,0,0),
```

and its past child

```text
C=D[p,m], m=(0,0,0,0).
```

For each cell `X`,

```text
u_X(x)=[(x-p_X)^2 (q_X-x)^2]/[(q_X-p_X)^2]^2.
```

On `C`, compare:

```text
parent-restricted:
  d nu_parent,a proportional to [1+a u_D(x)] d^4x;

child-intrinsic:
  d nu_child,a proportional to [1+a u_C(x)] d^4x.
```

Both are normalized on `C`. Compute exact means for:

```text
f_1(x)=t;
f_2(x)=u_C(x).
```

The calculation must retain `a` symbolically. It must establish whether the
two means agree only at `a=0` for the predeclared family `a>=0`.

## Predeclared branch rule

```text
if BID binds intrinsic per-cell response and all a>0 fail:
  INHERITED_REFINEMENT_NATURALITY_FORCES_UNIFORM_MEASURE
  do not adopt a new strict-locality principle;

if BID demonstrably does not bind intrinsic per-cell response:
  STRICT_LOCALITY_ADOPTION_REQUIRED
  enter it as new Level-1 content with scope and falsifier;

otherwise:
  R3_3_REMAINS_OPEN.
```

## Scope

This test adjudicates the exhibited `mu_a` family and the inherited
prohibition on any residual cell-shape scalar. It does not prove the complete
connected linked-cluster limit or derive the spectral density. Those remain
downstream.

```text
alpha_used = false
alpha_computed = false
hypothesis_promoted_to_principle = false
```
