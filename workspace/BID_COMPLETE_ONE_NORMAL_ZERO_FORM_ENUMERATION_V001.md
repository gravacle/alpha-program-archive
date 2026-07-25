# BID Complete One-Normal Zero-Form Enumeration v001

Date: 2026-07-23

## Purpose

Enumerate, without using alpha, every local complex-linear zero-order
endomorphism on the correctly graded cellular source-record carrier. Then
identify the subspace compatible with a Laplace-type Cliffordized parent.

This is an inventory and compatibility result. Coefficient selection is
separate.

## Cellular carrier and common frame

For one oriented record edge,

```text
C_0=span{root,public},
C_1=span{edge},
E_cell=C_0 direct-sum C_1,
Gamma_cell=diag(+1,+1,-1).
```

The source bundle is the disclosed Dirac bundle `S`. The complete local
carrier is

```text
H_local=S tensor E_cell,
dim_C(H_local)=12.
```

The physical root and endpoint spin fibers carry normals `n_r` and `n_p`.
Metric-compatible edge transport `U_e` identifies the endpoint fiber with
the root frame:

```text
psi_p -> U_e^(-1) psi_p.
```

In that common frame, both vertex fibers use `H_(n_r)` and the covariant
cellular boundary is

```text
d_partial:C_1 -> C_0,
d_partial z=(-z,+z).
```

Its self-adjoint cellular dilation on `E_cell` is

```text
b_partial=
  [[0,d_partial],
   [d_partial^sharp,0]]
```

and is `3 x 3`. The corresponding spin-lifted incidence is

```text
B_hat_partial=I_S tensor b_partial
```

on the consistently ordered carrier `S tensor E_cell`. It is `12 x 12` and
odd in `Gamma_cell`.

## Complete local zero-form inventory

At a reference normal, the Hermitian part of the `Spin(3)` commutant has real
basis

```text
S_0=I,
S_1=gamma^5,
S_2=gamma^0,
S_3=i gamma^0 gamma^5.
```

Transport by `Spin^+(1,3)` gives the corresponding `H_n`-self-adjoint basis
at every future unit normal.

The Hermitian algebra on `E_cell=C^3` has real dimension nine. Therefore
every local `H_n`-self-adjoint zero form constructed from the declared
one-normal data lies in a real space of dimension

```text
4 x 9=36.
```

The record-even Hermitian algebra is block diagonal on `C_0 direct-sum C_1`:

```text
Herm(C_0) direct-sum Herm(C_1),
dimension 4+1=5.
```

The record-odd Hermitian algebra consists of a complex two-vector
`C_1 -> C_0` plus its adjoint and has real dimension four. Thus the complete
spin-record inventory splits as

```text
record even: 4 x 5=20 real dimensions,
record odd:  4 x 4=16 real dimensions.
```

Root/public diagonal detuning and root-public mixing occupy the even sector.
Cellular transitions between the edge and either vertex occupy the odd
sector. The bare cellular incidence dilation `b_partial` is literally one
member of the odd sector.

## Clifford compatibility

A general Dirac-type operator with the ambient `3+1` Dirac principal symbol
is

```text
D=i gamma^mu nabla_mu tensor I_3+Psi.
```

For its square to have no additional first-order derivative term, the
spin part of `Psi` must anticommute with every `gamma^mu`. On one irreducible
complex Dirac carrier in `3+1` dimensions, that real self-adjoint
anticommutant is
one-dimensional:

```text
M=lambda gamma^5.
```

Consequently the Laplace-compatible record-odd zero forms are exactly

```text
Psi_odd=gamma^5 tensor phi_odd,
{Gamma_cell,phi_odd}=0,
phi_odd^dagger=phi_odd.
```

Their real dimension is four. For a constant `phi_odd`,

```text
D^2
  =(i gamma^mu nabla_mu)^2 tensor I_3
   +I tensor phi_odd^2;
```

for a varying field, the additional term is
`i gamma^mu gamma^5 tensor nabla_mu(phi_odd)`.

The other twelve record-odd zero forms remain legitimate first-order
operator competitors, but their squares contain first-order cross terms.
They are not members of the declared Laplace-type branch.

The ambient qualification is load-bearing. If only the three intrinsic
spatial/tangential gamma matrices are imposed, the compatible odd kernel has
real dimension eight. The four-dimensional result therefore applies to the
ambient `3+1` Dirac operator used here, not to an intrinsic three-dimensional
boundary Dirac operator.

## Relation to adopted principles

The Boundary Superconnection Principle selects the record-odd sector. The
Single-Operator Completeness premise excludes an independent additional odd
primitive after the cellular boundary has been fixed. These two premises
select the one-complex-dimensional incidence line, not its physical
quadrature. Standard Dirac CPT then fixes that quadrature, up to incidence
orientation, as

```text
c_partial=i Gamma_cell b_partial,
c_partial^2=b_partial^2.
```

The primitive local Cliffordized odd operator is therefore
`gamma^5 tensor c_partial`.

This conclusion is branch-conditional. The inventory itself is independent
of those principles.

## Boundary

This closes the carrier typing, common-frame reduction, one-normal zero-form
inventory, incidence embedding, and Laplace-compatible odd subspace. It does
not:

```text
derive the adopted Boundary Superconnection or Single-Operator principles;
derive the remaining anomaly/topology/CP axial reduction;
include curvature, extrinsic-curvature, flavor, or enlarged-record data;
derive connected many-record composition;
derive a physical pole, stiffness, or alpha.
```

## Status

```text
cellular_carrier_C0_direct_sum_C1_typed = true
cellular_carrier_complex_dimension_three = true
source_cellular_carrier_complex_dimension_twelve = true
two_normal_fibers_reduced_to_common_frame_by_metric_transport = true
bare_incidence_dilation_embedded_in_cellular_endomorphisms = true
spin_Hn_self_adjoint_commutant_real_dimension_four = true
record_Hermitian_algebra_real_dimension_nine = true
full_Hn_self_adjoint_zero_form_real_dimension_thirty_six = true
record_even_zero_form_real_dimension_twenty = true
record_odd_zero_form_real_dimension_sixteen = true
Laplace_compatible_record_odd_zero_form_real_dimension_four = true
complete_one_normal_zero_form_inventory_derived = true
Clifford_compatible_odd_subspace_derived = true
primitive_incidence_selected_given_two_adopted_principles = true
primitive_incidence_selected_without_adopted_principles = false
local_standard_CPT_incidence_quadrature_applied = true
complete_CP_axial_reduction_applied = false
enlarged_geometric_zero_form_branches_exhausted = false
complete_connected_source_record_action_derived = false
alpha_computed = false
proof_authorized = false
```
