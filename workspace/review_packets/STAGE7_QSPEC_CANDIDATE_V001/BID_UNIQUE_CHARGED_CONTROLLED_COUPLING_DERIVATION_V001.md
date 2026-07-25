# BID Unique Charged Controlled Coupling Derivation v001

Date: 2026-07-23

## Purpose

Derive the source-controlled record operator in the declared primitive
vacuum-plus-one-charged-source branch. No response, mass, coupling, endpoint,
or alpha value is used.

## General charge-nondemolition family

Let `Q` be the conserved compact vector-`U(1)` generator on the primitive
source sector, with spectral projectors

```text
P_0, P_+, P_-,
spec(Q)={0,+1,-1}.
```

The source carrier is typed before imposing naturality:

```text
H_source
 =direct-sum_(q in {0,+1,-1}) (M_q tensor S_Dirac).
```

`S_Dirac` carries the disclosed Lorentz/Clifford representation and is
therefore structural source data. `M_q` contains labels not resolved by the
pure charge-only public handle. Every self-adjoint source-record operator
that commutes with `Q tensor I_R` is block diagonal in charge, but may
initially act nontrivially on both factors:

```text
B
 =direct-sum_(q in {0,+1,-1}) B_q^(M,Dirac,R).
```

Charge conservation alone does not reduce this family further.

The pure charge-only public endpoint does not resolve a label in `M_q`.
Consequently every unitary change of basis on `M_q` that acts trivially on
the Dirac factor is an admissible source equivalence. Naturality requires
invariance under

```text
product_q (U(M_q) tensor I_Dirac).
```

This is an active symmetry of unresolved multiplicities, not a passive
spinor-basis change. Passive changes transform the gamma matrices and the
Dirac operator covariantly; they are not elements of this multiplicity
group.

The commutant of the full unitary group on each `M_q` is the scalar identity
on `M_q`. The remaining operator on `S_Dirac tensor H_R` is then restricted
by the already-derived single incidence line. Therefore the source-blind
charge-only family on that line is exactly

```text
B
 =P_0 tensor a_0 B_Q
  +P_+ tensor a_+ B_Q
  +P_- tensor a_- B_Q.
```

The executable verifies this with rank-greater-than-one `M_q` sectors,
computes their commutant rather than replacing them by rank-one charge
labels, and verifies that those multiplicity actions commute with the
structural Dirac-record operator. If an additional label is publicly
resolved, that is an enlarged multi-handle branch and this reduction does
not apply.

## Pure charged-access support

The pure charged handle is active exactly on the nonzero spectral support of
`Q`:

```text
P_ch=1_(R\{0})(Q)=P_++P_-.
```

This is the operational content of selecting the pure charged-access branch.
On `ker(Q)` no charged handle opens. Therefore its record-odd transition
generator vanishes:

```text
B_0=0.
```

This is not inferred from CPT and is not a claim that a neutral source has no
gravity or other record dynamics. It concerns only the primitive charged
handle.

## One normalized incidence line

The upstream incidence, Hilbert, exact-transfer, superconnection, and
single-operator gates leave one normalized primitive record-odd line. Standard
Dirac CPT fixes its physical quadrature, up to incidence orientation, as

```text
B_Q=gamma^5 tensor c_partial,
c_partial=i Gamma_cell b_partial.
```

The opposite incidence orientation is a basis convention on the same
one-cell, not a second source-sector coefficient. The selected orientation is
fixed once for the charged record endpoint. Thus, inside this declared
primitive line,

```text
B_+=a_+ B_Q,
B_-=a_- B_Q
```

with real coefficients.

## Spectral restriction of the normalized parent

Before source control, symmetric-monoidal identity extension sends the
normalized record incidence operator to

```text
B_parent=I_source tensor B_Q.
```

This is the source-independent lift: it acts as `B_Q` after restriction to
every one-dimensional source ray and contains no source observable. A
nonconstant spectral function of `Q` is already a source control and is not
part of this identity extension.

The charged-handle support is the exact spectral projector

```text
Pi_ch=P_ch tensor I_(Dirac,R).
```

The action of a boundary control is fixed by the following target-free
projection-module axioms. For every orthogonal projector `P`, the map
`C_P:End(H)->End(H)` is:

```text
linear;
supported: C_P(B)=P C_P(B) P;
a retraction: C_P(A)=A for every A=PAP;
a P-End(H)-P bimodule map:
  C_P(A B D)=A C_P(B) D for A=PAP and D=PDP.
```

These axioms say that control removes inaccessible support but does not
modify an action already wholly supported in the accessible subspace.
They are stated before any source coefficient is evaluated.

They have a unique solution. Taking `A=D=P` in the bimodule identity gives

```text
C_P(P B P)=P C_P(B) P=C_P(B).
```

The retraction property then gives

```text
C_P(B)=C_P(P B P)=P B P.
```

Thus the controlled operator is forced to be the orthogonal compression

```text
B_ch=Pi_ch B_parent Pi_ch
    =P_ch tensor B_Q.
```

Equivalently, if `J_ch` is the isometric inclusion of the charged subspace,
the restricted operator is `J_ch^* B_parent J_ch`. No numerical multiplier
is present in either construction. A putative

```text
lambda P_ch tensor B_Q
```

with `lambda != 1` satisfies support and bimodule covariance but fails the
retraction axiom on the active algebra. It therefore does not represent the
same action under access restriction; it introduces a second primitive
incidence normalization. The companion audit solves the complete finite
linear constraint system for `C_P` and verifies that its affine solution
space is zero-dimensional with `PBP` as the unique solution.

## CPT and interval crosscheck

The charged-cellular CPT derivation gives

```text
Theta_R B_Q Theta_R^(-1)=B_Q,
Theta_Q P_+ Theta_Q^(-1)=P_-.
```

The compression is CPT invariant because CPT exchanges `P_+` and `P_-`
while preserving `P_ch` and `B_Q`. In the coefficient classification this
requires

```text
a_-=a_+.
```

The compression has already fixed the surviving coefficient to one. The
independently derived record-only least-positive interval

```text
tau_R=pi/sqrt(2).
```

then supplies a check rather than a normalization premise. Exact evolution
under the compressed operator gives

```text
tau_first(B_ch)=pi/sqrt(2)=tau_R.
```

Rescaled competitors fail the compression identity. Odd integer rescalings
also return an endpoint at `tau_R`, but only after an earlier completed
transfer; this independent recurrence check prevents a later return from
being mislabeled as the primitive first opening. The already fixed endpoint
orientation chooses the positive incidence representative:

```text
a_+=a_-=1.
```

Together with charged-handle inactivity, the coefficient system has the
unique solution

```text
(a_0,a_+,a_-)=(0,1,1).
```

Therefore

```text
B_ch
 =P_ch tensor B_Q.
```

## Scope

The result is unique in the declared primitive, pure charge-only public,
vacuum-plus-one-source, normalized single-incidence branch. It does not
classify:

```text
multi-charge sectors with |Q|>1;
public spin, momentum, flavor, or other multiplicity-resolving handles;
charge-changing source/environment couplings;
simultaneous gravity-plus-charge source sectors;
additional primitive operators excluded by the adopted
  Single-Operator Completeness premise;
the remaining axial anomaly/topology/CP branch;
connected many-record dynamics;
a physical pole, stiffness, or alpha.
```

## Status

```text
general_charge_nondemolition_block_family_derived = true
charge_sector_internal_multiplicities_admitted_before_naturality = true
source_carrier_factorized_as_multiplicity_tensor_Dirac = true
Dirac_spinor_factor_retained_as_structural_data = true
charge_only_public_naturality_acts_only_on_unresolved_multiplicity = true
internal_sector_unitary_commutant_computed = true
source_blind_charge_projector_family_derived_on_single_incidence_line = true
pure_charged_access_support_equals_nonzero_Q_spectrum = true
neutral_charged_handle_transition_block_zero = true
one_normalized_primitive_incidence_line_imported = true
CPT_even_charged_record_operator_imported = true
positive_negative_coefficient_equality_derived_from_CPT = true
source_independent_parent_is_monoidal_identity_extension = true
boundary_control_projection_module_axioms_adopted = true
projection_module_control_map_uniqueness_derived = true
charged_control_is_orthogonal_spectral_compression = true
compression_preserves_parent_incidence_normalization = true
independent_sector_rescaling_excluded_by_single_operator_incidence = true
record_only_least_positive_interval_imported = true
compressed_operator_first_opening_interval_crosscheck = true
odd_integer_recurrence_competitors_rejected = true
unique_primitive_control_coefficients_zero_one_one = true
unique_primitive_charged_controlled_coupling_derived = true
full_many_charge_controlled_coupling_derived = false
complete_connected_source_record_action_derived = false
alpha_computed = false
proof_authorized = false
```
