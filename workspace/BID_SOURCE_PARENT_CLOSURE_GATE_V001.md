# BID Source-Parent Closure Gate v001

Date: 2026-07-23

## Purpose

This gate records every source-parent obligation found before any V011
response, coupling, or alpha evaluation. A later revision may close an item,
but it may not omit, rename, or silently pass one.

The restricted pure off-diagonal transfer model has earned one conditional
lemma:

```text
given source-independent scaled normalization, no parent zero-form detuning,
and exact completed transfer, D_(a,b,U)=[-a I;b U] forces |a|=|b|=1.
```

The unconditional incidence result is instead the covariant cellular boundary
`[-I;U_e]`. Neither result establishes the complete physical Lorentzian
source-record parent.

## Blocking obligations

| ID | Obligation | Current state | Closure condition |
|---|---|---|---|
| SP01 | Full source typing | PASS WITH DISCLOSED ORDINARY STATIONARY EXTERIOR-VACUUM DIRAC/CAR INPUT | The positive Cauchy-data Hilbert space, stationary spectral polarization, particle/antiparticle CAR carrier, vector-`U(1)` generator, charge-conjugation action, and exact relation of the two-state quotient to Dirac chirality are constructed. Charged Dirac matter, the polarization, and continuum CAR quantization are disclosed standard inputs. |
| SP02 | Lorentz covariance | PASS FOR BARE INCIDENCE | Spin/U(1) transport with the transported future normal gives a Lorentz-covariant local-system boundary and preserves the positive hypersurface metric. Lorentz/CPT restrictions on parent zero-forms remain SP03 and SP17. |
| SP03 | CPT covariance | PASS WITH DISCLOSED STANDARD DIRAC CPT IN THE SELECTED INCIDENCE LINE | The standard Dirac CPT antiunitary, charge-sector exchange, geometric normal pushforward and future reorientation, different-normal transported-edge chain equation, weighted-adjoint dilation, and nonzero neutral/charged controls are explicit. The computed phase constraint selects the imaginary cellular quadrature up to incidence orientation on the preselected normalized incidence line. CP/anomaly/axial reduction remains SP04. |
| SP04 | Axial phase | PASS IN THE DISCLOSED ORDINARY CP-EVEN ZERO-INDEX CLOSED-DOUBLE REGULATOR BRANCH | Combined C/P reduces the complete scalar/pseudoscalar family to `delta=0,pi`. A closed doubled-cell Fredholm regulator makes the Dirac domain `gamma5` invariant and removes boundary eta phases; chiral anticommutation derives spectral pairing. The zero-index Fujikawa Jacobian and determinant ratio identify the two signs, while an explicit index-one rectangular control fails both tests. Non-axially-invariant boundary domains remain separate branches. |
| SP05 | Complete incidence family | PASS IN DECLARED ONE-ARROW LOCAL-SYSTEM CLASS | The source-decorated category, positive source metric, covariant boundary, and invisible bivalent refinements are explicit. Parallel paths, public intermediates, loops, and faces are enlarged branches rather than alternate presentations. Parent zero-forms remain SP17. |
| SP06 | Charged-handle provenance | PASS WITH DISCLOSED STANDARD DIRAC/CAR INPUT | The conserved Dirac current gives `Q_Sigma`; CAR second quantization gives the integer-spectrum generator; functional calculus gives the exact nonzero-charge projector `P_ch`. The existence of charged Dirac matter is an input, and the unique signed record coupling remains SP16. |
| SP07 | Global composition | PASS IN THE ADOPTED FINITE STATIONARY ORIENTED ONE-COMPLEX PRIMITIVE QUASI-FREE BRANCH | One global Dirac CAR source carrier is coupled to distinct even record factors. Explicit cell pushouts are associative, relabeling and full cellular orientation reversal are covariant, each isolated cell recovers the SP17 incidence zero-form, and shared-support structure occurs in the primitive operator. The operator-valued CAR lift is exact on the one-source sector; an otherwise invisible quartic competitor is rejected by the openly adopted quasi-free completeness premise. Continuum/time-dependent ordering and preparation remain downstream. |
| SP08 | Physical pole | BLOCKED AFTER PASSING THE PRIMITIVE QUASIFREE LORENTZIAN SCHUR-POLE SUBGATE | Lorentzian Dirac reality forces `i gamma5 tensor c_partial`; the exact edge compression has a proper-Lorentz timelike shell `p^2=2 mu^2`, no edge massless pole, and strictly positive free residue. The internal source is a degenerate opposite-pseudoscalar pair, and `m_* T_R=pi` remains relational. Full SP08 still requires the complete CTP state/contour, durability and absolute `T_R`, gauge/edge dressing, infrared/infraparticle analysis, regulator-independent interacting spectrum, and exclusion of mass-shifting freedom before any physical numerical mass claim. |
| SP09 | Exhaustive independent audit | BLOCKED | Independently enumerate the admissible family and verify SP01-SP08. Representative phase samples and a hard-coded matrix identity do not close uniqueness. |
| SP10 | Complete normal-dependent incidence-map family | PASS FOR BARE INCIDENCE | The covariant cellular boundary fixes the bare column to `[-I;U_e]`. Additional normal-dependent root or endpoint maps are degree-zero parent competitors, not incidence coefficients, and remain open under SP17. |
| SP11 | Boundary-metric-compatible edge transport | PASS | With `n_p=Lambda_e n_r`, spin pseudounitarity and Clifford covariance derive `h_(n_p)(U_e psi,U_e phi)=h_(n_r)(psi,phi)`; the unit `U(1)` phase cancels. |
| SP12 | Graph presentation equivalence | PASS IN DECLARED CLASS | Invisible bivalent subdivisions with composed transport reduce uniquely to one arrow; parallel paths, branches, public intermediates, loops, and faces remain enlarged objects. No universal exclusion of enlarged branches is claimed. |
| SP13 | Physical record Hilbertization | PASS WITH DISCLOSED QUANTUM-RECORD AXIOMS | Disclosed axioms QR1-QR7 derive the counting metric and tensor coherence from orthogonal pointer projections, probability-preserving singleton inclusions, and independent-register product structure. Without QR3 one common scale survives, which the audit reproduces. Born kinematics is not derived from deeper boundary dynamics. |
| SP14 | Optimization-safe executable audits | BLOCKED | Load-bearing Python `assert` statements have been removed, exact subordinate verdicts are checked, and all critical audits dual-run under normal and `-O` interpreters. Closure still requires a content-addressed isolated runtime manifest and terminal seal. |
| SP15 | Physical charge/current construction | PASS WITH DISCLOSED DIRAC/CAR INPUT | The conserved current, finite-particle CAR generator, compact action, integer spectrum, full spectral projectors, and charge-conjugation sector action are constructed. The existence of charged Dirac matter remains a disclosed input. |
| SP16 | Unique charged controlled coupling | PASS IN THE DECLARED PRIMITIVE PURE-CHARGE SINGLE-INCIDENCE BRANCH | The source carrier separates unresolved multiplicity from structural Dirac data; the actual multiplicity commutant is computed. Symmetric-monoidal identity extension gives the source-independent parent, and target-free projection-module support, retraction, and bimodule axioms uniquely force control to be `C_P(B)=PBP`. The complete finite superoperator cohort has affine nullity zero; a rescaled competitor fails retraction. CPT and neutral inactivity then give `(a_0,a_+,a_-)=(0,1,1)`. The record interval is only a crosscheck. |
| SP17 | Complete graded superconnection typing | PASS IN DECLARED ONE-NORMAL LOCAL AMBIENT-3+1 DIRAC CLASS | On `S tensor (C_0 direct-sum C_1)`, the complete one-normal self-adjoint zero-form inventory is `36=20 even+16 odd`; the full ambient Clifford constraint has rank 12 and nullity four, exactly `gamma5 tensor record-odd`; the intrinsic tangential competitor is separately retained with nullity eight; and the `3 x 3` raw incidence, CPT-selected quadrature, and `12 x 12` spin lift are type-distinct. Primitive-line selection remains conditional on the adopted branch principles; local CPT selects `c_partial=i Gamma_cell b_partial`, while CP/anomaly/axial reduction remains SP04. |
| SP18 | Primitive-filtration provenance | PASS AS DISCLOSED ADOPTED BRANCH PREMISE | The augmentation-ideal filtration independently types incidence as degree at least one and curvature as degree at least two. Excluding an independent primitive Pauli/curvature coefficient is explicitly the adopted Single-Operator Completeness premise, not a derived theorem; generated Pauli and Maxwell descendants remain allowed. |

## Mandatory negative controls

Every future source-parent audit must continue to reproduce:

```text
full_three_handle_star_does_not_complete_at_handle_tau: true
root_survival_amplitude_at_handle_tau_is_zero: true
one_record_operator_does_not_select_connected_parent: true
primitive_quartic_competitor_rejected_only_by_adopted_quasi_free_completeness: true
endpoint_U2_element_unresolved: true
finite_source_record_frequency_is_not_a_physical_mass: true
public_record_Hilbertization_given_QR1_through_QR7: true
Born_kinematics_derived_from_deeper_action: false
physical_charge_operator_constructed_from_disclosed_Dirac_CAR_input: true
existence_of_charged_Dirac_matter_derived_by_BID: false
primitive_superconnection_completeness_not_yet_derived: true
nonzero_index_axial_sign_equivalence_rejected: true
unique_primitive_charged_controlled_coupling_derived: true
```

## Machine status

Until every blocking obligation passes on one immutable lineage:

```text
complete_relativistic_source_parent_derived = false
connected_many_record_parent_derived = false
finite_stationary_primitive_connected_action_derived = true
primitive_quasifree_Lorentzian_source_edge_pole_derived = true
public_record_Hilbertization_derived_given_QR1_through_QR7 = true
physical_record_Hilbertization_derived_from_deeper_action = false
physical_charge_operator_constructed_from_disclosed_Dirac_CAR_input = true
existence_of_charged_Dirac_matter_derived_by_BID = false
one_normal_ambient_3plus1_graded_superconnection_typing_derived = true
local_standard_CPT_incidence_quadrature_derived = true
ordinary_CP_even_zero_index_axial_phase_reduced = true
unique_primitive_charged_controlled_coupling_derived = true
complete_CPT_CP_reduced_graded_source_parent_derived = false
physical_source_mass_computed = false
complete_Q_spec_sealed = false
physical_Thomson_stiffness_computed = false
alpha_computed = false
proof_authorized = false
```

The executable companion must report `SOURCE_PARENT_CLOSURE=BLOCKED` while
also passing its regression checks. A successful regression audit is not a
source-parent closure.
