# BID Charged Cellular CPT Intertwiner Derivation v001

Date: 2026-07-23

## Purpose

Construct the standard Dirac CPT antiunitary, its action on future-oriented
boundary Hilbert spaces, charge sectors, and a transported record edge. Then
classify the CPT-compatible cellular quadrature without using alpha.

## Disclosed standard input

Use the ordinary `3+1` charged Dirac field, standard CPT, and the Weyl gamma
representation used throughout the source-parent audits. CPT itself is
standard Dirac/CAR input rather than a Gravacle derivation.

Let

```text
U_X=gamma^5 gamma^2=i gamma^0 gamma^1 gamma^3
```

up to a constant phase, and define the antiunitary spin action

```text
Theta_D psi(x)=U_X psi^*(-x).
```

It obeys

```text
U_X^dagger U_X=I,
U_X U_X^*=-I,
U_X gamma^(mu*) U_X^dagger=gamma^mu
```

for all four gamma matrices. The last identity, together with coordinate
inversion, intertwines the conjugated kinetic and mass Dirac equation. It
also implies

```text
U_X gamma^(5*) U_X^dagger=-gamma^5.
```

The audit verifies these equations in the Weyl representation and after a
nontrivial unitary change of spin basis.

## Future-normal convention

Spacetime inversion sends a future normal `n` to the past-directed geometric
pushforward `I_*n=-n`. The target boundary is reoriented to retain the
future-normal convention:

```text
n_Theta=-I_*n.
```

If `e_a` is the source orthonormal tetrad, define the reoriented target tetrad
and its dual coframe by

```text
e_a^Theta=-I_*e_a,
theta_Theta^a=(e^Theta)^(-1).
```

Then

```text
n=n^a e_a
implies
n_Theta=n^a e_a^Theta.
```

Thus the target components equal the original future-normal components. The
geometric pushforward, which is past-directed, is kept distinct from the
future reorientation. The three boundary-tangent legs inherit the transformed
hypersurface orientation, while reversing the source and public endpoint
order supplies the separate minus sign on the oriented one-cell used below.
With

```text
h_n=gamma^0 slash(n),
```

the antiunitary is an isometry:

```text
U_X^dagger h_(n_Theta) U_X=h_n^*.
```

This distinguishes geometric pushforward from the reorientation needed for
the positive boundary Hilbert space. The audit verifies the construction for
a cohort of explicit proper-Lorentz tetrads, their dual coframes, geometric
pushforwards, and reoriented future normals.

## Charge line and projectors

Complex conjugation maps the compact character of `L^q` to that of `L^-q`:

```text
conjugate(exp(i q theta))=exp(-i q theta).
```

On the direct sum of positive, negative, and neutral charge sectors, let
`X_Q` exchange the first two sectors and fix the neutral sector. The
antiunitary `X_Q K` obeys

```text
Theta_Q Q Theta_Q^(-1)=-Q,
Theta_Q P_+ Theta_Q^(-1)=P_-,
Theta_Q P_- Theta_Q^(-1)=P_+,
Theta_Q P_0 Theta_Q^(-1)=P_0.
```

The projectors are spectral projectors of `Q`, not inserted labels.

## Transported edge and causal-role reversal

Let `e:r -> p` be a future-directed record edge with admissible spin/charge
transport

```text
U_e:H_r^q -> H_p^q
```

and local-coefficient boundary

```text
d_e xi=(-xi,U_e xi).
```

Under time reversal, the future-directed target edge runs from `p_Theta` to
`r_Theta`; root and public causal roles exchange. If `theta_r` and `theta_p`
are the antiunitary source maps at the two vertices, define the reversed
transport by

```text
U_(Theta e) theta_p U_e=theta_r.
```

On degree zero, CPT swaps the vertex roles. On degree one its antiunitary is

```text
Theta_1=-theta_p U_e.
```

The minus sign is the induced orientation sign of the reversed one-cell.
These maps satisfy the typed chain equation

```text
Theta_0 d_e=d_(Theta e) Theta_1
```

for the CPT-induced target transport of any source transport satisfying the
standard connection transformation law. Because the maps are isometries, the
same equation carries the `h_n`-weighted adjoint dilation to the target
dilation. The audit tests a cohort of spin boosts between different future
normals, with independent `U(1)` phases; it does not infer the transformation
law of an unrelated external connection. The old scalar equation
`J_0 d=d J_1` is only the common-frame special case.

## CPT parity of the cellular quadratures

In the common frame write the `3 x 3` cellular incidence dilation as
`b_partial`, cellular grading as `Gamma_cell`, and causal-role reversal as
`J_cell`. Then

```text
J_cell b_partial^* J_cell^dagger=+b_partial,
J_cell Gamma_cell J_cell^dagger=Gamma_cell.
```

The real incidence quadrature is CPT even. Standard Dirac CPT makes
`gamma^5` odd, so

```text
gamma^5 tensor b_partial
```

is CPT odd and is not the CPT-invariant primitive.

For the already fixed complex incidence column `d_partial`, every Hermitian
lift on its one-complex-dimensional boundary line is

```text
b_partial(zeta)=
  [[0,zeta d_partial],
   [conjugate(zeta) d_partial^dagger,0]].
```

CPT maps `b_partial(zeta)` to `b_partial(conjugate(zeta))`. Since the spin
factor is CPT odd, invariance of
`gamma^5 tensor b_partial(zeta)` requires

```text
conjugate(zeta)=-zeta.
```

The executable does not insert this equation as a constraint row. It computes
the real-linear CPT residual on the basis lifts `b_partial(1)` and
`b_partial(i)`, forms the resulting constraint matrix, and obtains rank one
with the imaginary axis as its one-dimensional nullspace.

Thus the phase is purely imaginary. After the already fixed unit magnitude,
the only possibilities are the overall-sign pair `zeta=+i` and `zeta=-i`.
They are related by reversing the primitive incidence orientation.

The selected Hermitian quadrature can therefore be written

```text
c_partial=i Gamma_cell b_partial.
```

It is record-odd and satisfies

```text
c_partial^dagger=c_partial,
c_partial^2=b_partial^2,
Theta_cell c_partial Theta_cell^(-1)=-c_partial.
```

Therefore

```text
Phi_CPT=gamma^5 tensor c_partial
```

is CPT even. This selects, up to the incidence-orientation sign, one phase on
the fixed boundary line within the already enumerated four-dimensional
record-odd space. It does not add a new coefficient or change the Laplace
square.

## General controlled coupling

For

```text
B=P_0 tensor B_0+P_+ tensor B_++P_- tensor B_-,
```

full CPT covariance is equivalent to

```text
Theta_cell B_0 Theta_cell^(-1)=B_0,
B_-=Theta_cell B_+ Theta_cell^(-1).
```

The audit constructs the full block operator with a nonzero CPT-even neutral
block, verifies both conditions, and separately perturbs `B_-` and `B_0` so
that each incorrect operator fails. This is a necessary-and-sufficient
classification, not evidence that orientation blindness `B_-=B_+` holds.

## Boundary

This derivation closes the local standard-CPT typing and selects the
CPT-even incidence quadrature in the declared cellular branch. It does not:

```text
derive CPT itself;
force orientation-blind B_+=B_-;
select the remaining scalar/pseudoscalar axial phase;
derive anomaly, topology, or CP data;
derive connected many-record dynamics;
compute a pole, stiffness, or alpha.
```

Scalar and pseudoscalar fermion-bilinear CPT parities remain standard input;
they are not counted as a new result here.

## Status

```text
standard_Dirac_CPT_disclosed_input = true
explicit_Weyl_basis_CPT_antiunitary_constructed = true
all_four_gamma_CPT_intertwiners_verified = true
Dirac_kinetic_and_mass_CPT_covariance_verified = true
future_normal_pushforward_tetrad_and_reorientation_typed = true
positive_boundary_Hilbert_CPT_isometry_verified = true
charge_line_conjugation_typed = true
positive_negative_neutral_charge_projector_CPT_actions_verified = true
induced_target_transport_CPT_chain_equation_derived = true
different_normal_transport_cohort_verified = true
weighted_adjoint_incidence_dilation_CPT_covariance_derived = true
real_incidence_quadrature_CPT_even = true
gamma5_real_incidence_product_CPT_even = false
CPT_odd_Hermitian_cellular_quadrature_derived = true
CPT_even_Cliffordized_incidence_phase_unique_up_to_orientation_sign = true
phase_constraint_derived_from_computed_antiunitary_action = true
gamma5_CPT_odd_cellular_quadrature_product_CPT_even = true
general_controlled_coupling_CPT_conditions_derived = true
nonzero_neutral_control_block_verified = true
neutral_and_charged_negative_controls_rejected = true
orientation_blind_B_plus_equals_B_minus_derived = false
CPT_selects_axial_phase_delta_zero = false
complete_connected_source_record_action_derived = false
alpha_computed = false
proof_authorized = false
```
