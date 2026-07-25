# BID Global Boundary Descent and Quasi-Free Completeness v001

Date: 2026-07-23

## Purpose

Derive the primitive connected source-record action from one globally glued
boundary construction while keeping fermionic source modes and even record
degrees of freedom type-distinct. No coupling, mass, endpoint, or alpha target
is used.

## Adopted primitive principle

**Global Boundary Descent and Quasi-Free Completeness Principle.** The
primitive connected source-record action is exactly the operator-valued
functorial CAR lift of the globally assembled one-particle boundary
superconnection. No independent primitive higher-CAR, record-only, contact,
or overlap kernel is allowed. Terms of those forms may arise only as
effective descendants after shared gauge, gravitational, record, or
environmental fields are eliminated from the one complete action.

This is an additional microscopic Gravacle premise. It does not follow from
CAR, locality, or disjoint monoidality alone. It is target-value-free but
historically target-aware, and is forward-adopted before further evaluation
under this branch.

## Typed global carrier

On the disclosed stationary Cauchy surface, use one global source
one-particle space

```text
K_Sigma = K_orb tensor S_Dirac
```

and its single global CAR algebra `CAR(K_Sigma)`. For each labeled record cell
`c`, retain the even record carrier

```text
R_c=span_C{|r_c>,|p_c>,|e_c>}.
```

For a finite cell complex `K`,

```text
R(K)=tensor_(c in K) R_c,
A_SR(K)=CAR(K_Sigma) graded-tensor B(R(K)).
```

The record algebra has trivial fermion grading. No record direction receives
a fermionic annihilation operator, and the source carrier is not copied once
per record cell.

## Finite stationary global boundary descent

This version treats finite consistently labeled oriented one-complexes in the
ordinary stationary branch. Each cell has:

```text
an oriented incidence vector d_c in K_orb;
the orientation-invariant support projector
  P_c=|d_c><d_c|/<d_c,d_c>;
and the actual SP17 cellular quadrature
  c_c=i Gamma_cell b_partial,c.
```

Orientation reversal sends `d_c` to `-d_c` and leaves `P_c` unchanged. Shared
vertices are identified exactly once by the pushout of the labeled incidence
maps. Record labels are not identified: they remain separate tensor factors.

Let `iota_c(c_c)` act as `c_c` on `R_c` and as the identity on every other
record factor. The global operator-valued one-particle superconnection is

```text
h_K
 =sum_c P_c tensor gamma^5 tensor iota_c(c_c)
```

on `K_orb tensor S_Dirac tensor R(K)`. This is constructed from the global
incidence data, not by tensoring duplicated source algebras.

For an isolated one-cell complex, restriction to its normalized incidence
ray gives exactly

```text
gamma^5 tensor c_c,
```

the 12-dimensional SP17 source-record **incidence zero-form**. The kinetic
Dirac term and its physical pole are not claimed here; they remain SP08.

When two cells share source support, `P_c P_d` is nonzero. Consequently
`h_K` has source-orbital off-diagonal blocks and the local summands need not
commute. This is connected structure in the primitive operator itself. The
invariant overlap magnitude is

```text
Tr(P_c P_d)=|<d_c,d_d>|^2/(||d_c||^2 ||d_d||^2);
```

its sign cannot depend on an orientation convention. A Laplacian term in
`h_K^2` is only induced two-step propagation and is not relabeled as a
primitive overlap coefficient.

The pushout and operator assembly are associative for this declared finite
one-complex category. Relabeling vertices conjugates `h_K` by the induced
source permutation. Reversing a cell orientation sends its source incidence
vector to its negative and conjugates its record quadrature by the cellular
orientation unitary. The source-support projector is invariant, while the
complete `h_K` is covariant under the corresponding record-space
conjugation.
Higher-dimensional cells, continuum domains, and time-dependent backgrounds
are not claimed by this finite stationary theorem.

## Operator-valued quasi-free CAR lift

Choose an orthonormal basis `e_i` of `K_Sigma` and decompose

```text
h_K=sum_(i,j) |e_i><e_j| tensor b_ij,K
```

with `b_ij,K` acting on the even record carrier. The primitive generator is

```text
H_K
 =sum_(i,j) a_i^* a_j tensor b_ij,K.
```

On the one-source sector it recovers `h_K` exactly. This is the
operator-valued number-preserving quasi-free CAR lift. It is unique within
the adopted primitive class up to an additive scalar, fixed by public vacuum
normalization:

```text
<Omega|H_K|Omega>=0.
```

The family

```text
H_lambda
 =H_K + lambda n_i n_j tensor I_R
```

agrees with `H_K` on the vacuum and one-source sectors but changes a
two-source sector. The adopted principle rejects every nonzero `lambda` at
the primitive level because the added term is not the CAR lift of `h_K`.
This negative control is retained in the executable. Effective quartic or
record-only terms remain permitted when derived by eliminating fields or
coarse-graining the complete action.

## Ordering and preparation

For the finite stationary self-adjoint `H_K`, Stone evolution

```text
U_K(t)=exp(-i t H_K)
```

is unique and obeys the one-parameter group law. This version makes no
time-dependent or unbounded-operator domain claim.

The result fixes the primitive finite stationary connected action. It does
not select a continuum vacuum, CTP state, durability sector, clustering
state, physical pole, or residue. Those remain separate gates.

## Executable obligations

The companion audit must:

```text
keep one global fermionic source carrier and distinct even record factors;
identify a shared source boundary once;
recover the actual SP17 one-cell incidence zero-form;
construct the pushout from separate cell objects and compare both
  three-cell parenthesizations;
assemble the same global operator under both cell orders;
verify vertex-relabeling and orientation-reversal covariance;
compute nonzero shared-support structure in h_K itself;
separate that structure from induced h_K^2 propagation;
construct the operator-valued CAR lift on one- and two-source sectors;
recover h_K exactly on the one-source sector;
show a quartic competitor matches vacuum and one-source sectors;
show it differs on a two-source sector and reject it by the adopted premise;
verify finite stationary Stone composition;
run identically under normal and optimized Python.
```

## Status

```text
global_boundary_descent_principle_adopted = true
primitive_quasi_free_completeness_adopted = true
historically_target_blind = false
target_value_used_in_construction = false
forward_adopted_before_further_branch_evaluation = true
single_global_source_CAR_carrier_retained = true
record_factors_distinguishable_and_fermion_even = true
record_directions_fermionized = false
finite_stationary_oriented_one_complex_scope = true
shared_source_boundary_pushout_defined = true
finite_gluing_associativity_derived = true
vertex_relabeling_naturality_derived = true
orientation_reversal_covariance_derived = true
actual_SP17_one_cell_incidence_zero_form_recovered = true
complete_SP17_kinetic_operator_recovered_here = false
global_operator_valued_one_particle_superconnection_constructed = true
primitive_shared_support_structure_computed = true
two_step_Laplacian_not_mislabeled_as_primitive_overlap = true
operator_valued_quasi_free_CAR_lift_derived = true
primitive_quartic_competitor_rejected = true
effective_descendant_interactions_forbidden = false
finite_stationary_ordering_fixed_by_Stone_evolution = true
time_dependent_continuum_ordering_derived = false
connected_preparation_derived = false
physical_source_pole_and_residue_derived = false
alpha_computed = false
proof_authorized = false
```
