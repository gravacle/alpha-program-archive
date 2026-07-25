# BID Axial-Phase CP Reduction Derivation v001

Date: 2026-07-23

## Purpose

Reduce the residual source-record axial phase in the declared ordinary
CP-even branch without using a coupling, mass, endpoint, or alpha target.

## Complete local family

The Lorentz-covariant source-boundary classification leaves

```text
L_odd(rho,delta)
 =rho cos(delta) bar(psi)psi
  +rho sin(delta) i bar(psi)gamma^5 psi,

M_(n,rho,delta)
 =rho slash(n) exp(i delta gamma^5).
```

Standard Dirac charge conjugation makes both the scalar and pseudoscalar
bilinears C-even, while parity makes the scalar even and the pseudoscalar odd.
The executable constructs both transformations and their combined CP
residual. Therefore CP invariance of this local coupling requires

```text
sin(delta)=0,
delta=0 or pi modulo 2 pi.
```

The real-linear CP constraint on the complete scalar/pseudoscalar coefficient
plane has rank one with the scalar axis as its kernel. It does not insert
`delta=0` as the constraint.

## Orientation equivalence of the two representatives

At a reference normal, the endpoint map obeys

```text
C_pi=-C_0.
```

The two incidence columns

```text
D_0 =[-I; C_0],
D_pi=[-I;-C_0]
```

are related by the unitary endpoint-line orientation change

```text
W=diag(I_root,-I_endpoint),
W D_0=D_pi.
```

This proves one endpoint-rephasing class of local incidence maps. By itself it
does not prove that the two scalar signs are equivalent in the complete
fermion action.

## Fermion measure, domain, and topological sector

The ordinary branch used here discloses:

```text
one vectorlike Dirac source;
a regulator preserving vector U(1) and CP;
a closed oriented doubled Euclidean cell C_hat for the source determinant;
the Fredholm Dirac operator D_E on Dom(D_E)=H^1(C_hat,S tensor L);
a topologically trivial charged bundle on C_hat;
vanishing gauge and gravitational Pontryagin numbers;
and no physical boundary or eta-invariant term in the determinant regulator.
```

The causal-cell record boundary is still carried by the separate record
incidence complex. Doubling is used only to define the regulated source
determinant on one closed domain; it does not erase the public record
endpoint.

On the massless closed-domain operator,

```text
gamma^5 Dom(D_E)=Dom(D_E),
{D_E,gamma^5}=0.
```

Thus the `beta=pi/2` axial map is an admissible change of variables in the
same regulated theory, and every nonzero eigenvalue is paired with its
opposite. By the standard index/anomaly relation, the disclosed topology
gives

```text
Index(D_E)=0.
```

The discrete axial transformation with angle `beta=pi/2` flips the scalar
sign. Its Fujikawa Jacobian is

```text
J_beta=exp(2 i beta Index(D_E))=1
```

in this sector. Thus the endpoint rephasing extends to a physical equivalence
of the two source-action signs in the complete regulated ordinary branch.
The executable constructs a concrete finite chiral Galerkin operator with an
invariant domain and computes its anticommutation, spectrum, index, and
determinant ratio. It also constructs a rectangular chiral negative control
with one unpaired zero mode; that control has nonzero index, a nontrivial
Jacobian, and a mass-sign determinant ratio of minus one.

Consequently the ordinary CP-even, zero-index branch has one physical
axial-phase class, represented by

```text
delta=0.
```

## Why the anomaly does not reopen this result

No axial field redefinition is used to remove an arbitrary `delta`. CP first
reduces the family to `delta=0,pi`. The single discrete transformation used
to compare those two signs is admitted only after its complete measure
Jacobian is evaluated in the disclosed zero-index sector.

Non-CP branches, boundary regulators not preserved by `gamma^5`, nontrivial
theta sectors, nonzero index, and enlarged topological data remain separate
branches. The same transformation is not declared an equivalence there.

## Scope

This closes the local axial phase in the disclosed ordinary CP-even,
zero-index, closed-double-regulated, single-incidence vectorlike Dirac
branch. It imports the standard regulated index/anomaly theorem; it does not
derive CP as a universal law, establish sign equivalence for a
non-axially-invariant boundary domain, exclude CP-violating or nonzero-index
enlarged branches, or compute a pole, stiffness, or alpha.

## Status

```text
complete_local_scalar_pseudoscalar_family_imported = true
standard_Dirac_CP_bilinear_parities_disclosed = true
charge_conjugation_and_parity_actions_both_constructed = true
CP_constraint_computed_on_complete_two_real_dimensional_family = true
CP_even_coefficient_kernel_is_scalar_axis = true
delta_zero_and_pi_survive_before_orientation_quotient = true
delta_zero_and_pi_unitarily_endpoint_rephasing_equivalent_as_incidence_maps = true
ordinary_vectorlike_CP_preserving_regulator_disclosed = true
closed_doubled_cell_source_determinant_regulator_disclosed = true
regulated_Dirac_domain_explicit = true
gamma5_preserves_regulated_Dirac_domain = true
massless_Dirac_operator_anticommutes_with_gamma5 = true
boundary_eta_phase_absent_in_closed_regulator = true
ordinary_zero_index_topological_sector_disclosed = true
standard_index_anomaly_relation_imported = true
discrete_scalar_sign_flip_Jacobian_evaluated = true
regulated_determinant_mass_sign_ratio_evaluated = true
nonzero_index_domain_negative_control_rejected = true
delta_zero_and_pi_physically_equivalent_in_zero_index_branch = true
arbitrary_delta_axial_field_redefinition_used = false
fermion_measure_anomaly_silently_ignored = false
ordinary_CP_even_axial_phase_class_unique = true
CP_violating_enlarged_branches_excluded_universally = false
complete_connected_source_record_action_derived = false
alpha_computed = false
proof_authorized = false
```
