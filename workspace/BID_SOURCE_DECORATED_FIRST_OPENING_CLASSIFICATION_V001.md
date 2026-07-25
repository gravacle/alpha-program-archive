# BID Source-Decorated First-Opening Classification v001

Date: 2026-07-23

## Scope

This classification asks whether the local source-record incidence family was
complete inside the declared ordinary pure-charged first-opening branch. It
does not classify enlarged branches with additional public alternatives.

Its inputs are:

```text
the disclosed 3+1 Lorentz/spin/vector-U(1) structure;
the ordinary first-opening topology premise;
the positive Dirac current inner product on a boundary;
the minimal isotropic boundary data, consisting only of the unit normal;
and the Elementary Record Hilbertization gate when that gate passes.
```

No mass, coupling, endpoint, or alpha value is used.

## Source-decorated objects

Extend a pure-charged `DecRec_2` object by:

```text
the Dirac bundle E_q=S tensor L^q on its vertices;
the spin/U(1) connection along each edge;
a future unit timelike normal on each spacelike record boundary;
and the positive hypersurface form h_n.
```

Morphisms preserve the cellular data, root, first-opening status, `Q` label,
spin/U(1) transport, normal, and hypersurface form. In particular, an
admissible edge transport must obey

```text
h_(n_p)(U_e psi,U_e phi)=h_(n_r)(psi,phi).
```

`BID_BOUNDARY_METRIC_TRANSPORT_DERIVATION_V001.md` proves this compatibility
from spin pseudounitarity and Clifford covariance when the endpoint normal is
the Lorentz transport of the root normal. It does not follow from preserving
the indefinite Dirac pairing while allowing two unrelated normals. The
source decoration is not a second record label.

## Stipulated minimal graph representative

The first-opening premise permits one unresolved root, one charged public
endpoint, and one primitive arrow between them in the pure charged branch.
The following are not alternate presentations of that same object:

```text
two parallel primitive arrows:
  add an independent path/one-cell distinction;

an intermediate vertex:
  adds another public first-order alternative;

separate L and R endpoints or edges:
  make chirality a public record label;

a loop or face:
  is a composition or higher-order cell.
```

They are legitimate enlarged-branch objects, but they do not belong to the
stipulated minimal pure-charged first-opening object.
`BID_FIRST_OPENING_GRAPH_REFINEMENT_QUOTIENT_V001.md` now defines invisible
bivalent subdivision and proves that every finite unlabeled linear path
reduces to the one-arrow representative, while parallel paths, branches,
public intermediates, and loops remain enlarged objects.

## Incidence boundary and the open zero-form class

`BID_ROOT_INCIDENCE_IDENTITY_DERIVATION_V001.md` derives the root component
as `-I` from the covariant cellular boundary. Normal-dependent source
zero-forms remain competitors in the complete parent action, but they are not
alternate coefficients of the incidence boundary.

At the endpoint, the full normal-dependent little-group zero-form family is
classified
in `BID_COMPLETE_NORMAL_DEPENDENT_ENDPOINT_MAP_CLASSIFICATION_V001.md`:

```text
E(n)=a I+b gamma^5+c slash(n)+d slash(n) gamma^5.
```

The previously studied chiral-odd family is a proper subfamily, not the
exhaustive endpoint zero-form class. But `E` is not an incidence coefficient.
The covariant cellular boundary itself fixes the complete bare incidence
column:

```text
D_partial psi
  =-i_r(psi)
   +i_p(U_e psi).
```

A separate root dressing `R(n_r)` and endpoint dressing `E(n_p)` are
comparably typed degree-zero parent terms. Neither is an alternate
coefficient of `D_partial`; both remain in the complete parent-action
enumeration under SP17. This removes the earlier endpoint/root asymmetry.

## Metrics and transfer

The source metric is the vector-current hypersurface metric. A chiral
imbalance would replace the declared vector charge by a vector-plus-axial
current and is therefore not the same source branch.

The record labels are orthogonal public alternatives. The Public Record
Hilbertization derivation obtains their counting metric from disclosed
quantum-record axioms QR1--QR7, including pointer-projection orthogonality and
probability-preserving singleton inclusions. Conditional on those axioms, the
local product metric is

```text
h_n tensor I_record.
```

This does not derive the Born rule from deeper boundary dynamics.

The bare boundary already has unit endpoint magnitudes. For comparison, a
restricted endpoint-dressed pure off-diagonal model may be written

```text
D_(a,b,U)=[-a I;b U],
B=[[0,D],[D^sharp,0]].
```

If one additionally imposes source-independent scaled normalization, excludes
all parent zero-form detuning, and defines completion as exact transfer, then

```text
P_endpoint,max
  =4|a|^2|b|^2/(|a|^2+|b|^2)^2,
```

and completion forces

```text
|a|=|b|=1.
```

This last statement is conditional on that pure off-diagonal dynamics. It
does not survive arbitrary zero-form detuning without a new derivation.

## Earned result

Inside the stipulated minimal one-arrow graph, the covariant local-system
boundary fixes the bare source incidence to `[-I;U_e]`. Conditional on
QR1--QR7, the associated record metric is the counting metric. The complete
normal-dependent endpoint zero-form family is separately classified, but its
physical element and the full parent dynamics remain unresolved.

This does not derive:

```text
the first-opening topology premise itself;
the Born rule or record axioms from deeper boundary dynamics;
the source-independent scaled-normalization premise;
the endpoint `U(2)` element or its CPT/CP reduction;
the exclusion or coefficient of root/endpoint zero-form detuning;
the global connected source-record action;
the active-handle current projector;
a physical mass;
or alpha.
```

## Status

```text
source_decorated_object_and_morphism_type_defined = true
minimal_pure_charged_first_opening_graph_stipulated = true
linear_path_graph_presentation_equivalence_derived = true
universal_graph_exhaustion_across_enlarged_branches = false
parallel_edge_same_branch_equivalence = false
intermediate_vertex_same_branch_equivalence = false
chirality_labeled_endpoint_same_branch_equivalence = false
metric_compatible_edge_transport_required = true
metric_compatible_edge_transport_derived_from_spin_transport_alone = false
metric_compatible_edge_transport_derived_given_transported_normal = true
root_incidence_identity_derived = true
normal_dependent_root_zero_forms_forbidden_in_parent = false
chiral_even_and_chiral_odd_endpoint_competitors_admitted = true
singular_and_nonunitary_endpoint_competitors_admitted = true
endpoint_zero_form_is_incidence_coefficient = false
normal_dependent_endpoint_zero_form_family_exhausted_given_one_normal = true
all_spinor_scaled_normalization_derived = false
conditional_endpoint_scaled_unitary_lemma_derived = true
endpoint_U2_element_selected = false
axial_source_frame_quotient_used = false
bare_covariant_incidence_column_is_minusI_plus_Ue = true
root_and_endpoint_zero_forms_retained_as_parent_competitors = true
conditional_pure_offdiagonal_equal_transfer_derived = true
parent_zero_form_detuning_excluded = false
record_Hilbertization_derived_given_QR1_through_QR7 = true
record_Hilbertization_derived_from_deeper_boundary_action = false
local_source_record_family_closed_unconditionally = false
complete_source_record_parent_closed = false
global_connected_source_record_action_derived = false
physical_source_mass_computed = false
complete_Q_spec_sealed = false
alpha_computed = false
proof_authorized = false
```
