# BID Graded Boundary-Superconnection Repair v001

Date: 2026-07-23

## Purpose

Type the boundary superconnection on the actual cellular carrier and derive
the compatible Cliffordized square without conflating:

```text
spin chirality;
cellular grading;
differential order;
and BID incidence degree.
```

No alpha or target response is used.

## Cellular grading

For one record edge, use

```text
E_cell=C_0 direct-sum C_1,
C_0=span{root,public},
C_1=span{edge},
Gamma_cell=+1 on C_0 and -1 on C_1.
```

The source-cellular carrier is `S tensor E_cell`, with complex dimension
twelve. After transporting the endpoint source fiber into the root frame,
the covariant boundary and its self-adjoint dilation are

```text
d_partial z=(-z,+z),

b_partial=
  [[0,d_partial],
   [d_partial^sharp,0]].
```

Thus

```text
Gamma_cell b_partial+b_partial Gamma_cell=0.
```

Here `b_partial` acts only on `E_cell` and is `3 x 3`. Its spin lift is

```text
B_hat_partial=I_S tensor b_partial,
```

a square `12 x 12` self-adjoint operator on the consistently ordered carrier
`S tensor E_cell`. The bare rectangular boundary is embedded in this lift;
no edge sector is omitted.

The raw incidence dilation is CPT even. The charged-cellular CPT
classification independently selects the Hermitian record-odd quadrature

```text
c_partial=i Gamma_cell b_partial,
C_hat_partial=I_S tensor c_partial,
c_partial^2=b_partial^2.
```

The sign pair is the primitive incidence-orientation convention, not a new
coefficient.

## Abstract superconnection

On `S tensor E_cell`, distinguish the raw chain-complex superconnection from
the CPT-selected physical branch:

```text
A_raw=nabla_(spin+U1+cell)+B_hat_partial,
A_BR=nabla_(spin+U1+cell)+C_hat_partial.
```

The connection is a one-form and is even in `Gamma_cell`;
both zero forms are record odd. The physical graded curvature identity is

```text
A_BR^2=F_nabla+nabla C_hat_partial+C_hat_partial^2.
```

This identity is valid independently of Cliffordization.

## Cliffordized Laplace branch

The complete one-normal zero-form inventory is derived in
`BID_COMPLETE_ONE_NORMAL_ZERO_FORM_ENUMERATION_V001.md`. A general odd
zero-form may carry spin structure and need not yield a Laplace-type square.

Requiring the square to contain no additional first-order derivative term
for the ambient `3+1` Dirac principal symbol forces the spin factor to
anticommute with all four `gamma^mu`. On the disclosed irreducible complex
Dirac carrier this fixes the spin factor to `gamma^5`, up to one real scalar.
The compatible operator is

```text
D_BR
  =i gamma^mu nabla_mu tensor I_3
   +gamma^5 tensor c_partial.
```

Both terms act on the same `12`-complex-dimensional carrier. Its square is

```text
D_BR^2
  =(i gamma^mu nabla_mu)^2 tensor I_3
   +I_4 tensor b_partial^2
   +i gamma^mu gamma^5 tensor nabla_mu(c_partial).
```

For constant local incidence, the last term vanishes. The covariant Dirac
square supplies its usual fixed Clifford contraction of spin/gauge
curvature. No omitted first-order wavefunction derivative is hidden.

The ambient qualification is essential. Using only an intrinsic
three-dimensional tangential principal symbol leaves an eight-dimensional
compatible odd kernel. The four-dimensional kernel and unique `gamma^5`
spin direction are claims about the ambient `3+1` operator written above.

## Complete zero-form boundary

Inside the one-normal local class, the complete self-adjoint zero-form space
has real dimension `36`, split into `20` record-even and `16` record-odd
directions. The Laplace-compatible record-odd subspace has dimension four.

The adopted Boundary Superconnection Principle selects record-odd primitive
terms. The adopted Single-Operator Completeness premise then excludes an
independent second primitive odd map after the incidence line is fixed.
Standard Dirac CPT then selects `c_partial` on that line. The first two are
visible branch premises, not universal theorems of Dirac geometry; the CPT
quadrature is derived only inside their selected line.

Even detuning, curvature-dependent Pauli terms, and enlarged geometric terms
remain valid competitors outside those adopted primitive rules. Generated
effective terms remain allowed.

## Differential order versus incidence degree

The two orderings remain independent:

| Term | Differential order | BID incidence degree |
|---|---:|---:|
| `B_hat_partial` | 0 | 1 |
| covariant derivative | 1 | 1 |
| Pauli `sigma.F` endomorphism | 0 | at least 2 |
| `F^2` endomorphism | 0 | at least 4 |

The augmentation-ideal filtration derives the incidence-degree lower bounds.
Excluding an independent primitive degree-two coefficient remains the
disclosed Single-Operator Completeness premise.

## Earned result and boundary

The cellular carrier, grading, incidence embedding, complete one-normal
zero-form inventory, Clifford-compatible odd subspace, and corrected square
are now mutually type-compatible.

The local standard-CPT incidence quadrature is applied. The remaining
anomaly/topology/CP axial reduction, global connected action, causal/CTP
state, physical pole, response normalization, and alpha remain open.

## Status

```text
spin_chirality_and_cellular_grading_separated = true
cellular_carrier_C0_direct_sum_C1_typed = true
source_cellular_carrier_complex_dimension_twelve = true
bare_rectangular_incidence_embedded_in_square_dilation = true
cellular_b_partial_odd_under_cellular_grading = true
CPT_selected_c_partial_odd_under_cellular_grading = true
CPT_selected_c_partial_square_equals_b_partial_square = true
graded_superconnection_curvature_identity_corrected = true
complete_one_normal_zero_form_inventory_imported = true
Laplace_compatible_odd_subspace_derived = true
Cliffordized_operator_terms_same_dimension = true
Cliffordized_square_first_order_cross_term_cancelled = true
differential_order_and_BID_incidence_degree_distinguished = true
primitive_Pauli_exclusion_conditional_on_adopted_single_operator_premise = true
primitive_BID_filtration_derived_independently = false
local_standard_CPT_incidence_quadrature_applied = true
complete_CP_axial_reduction_applied = false
complete_connected_source_record_action_derived = false
complete_Q_spec_sealed = false
alpha_computed = false
proof_authorized = false
```
