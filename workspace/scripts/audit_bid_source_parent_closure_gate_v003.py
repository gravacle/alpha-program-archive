#!/usr/bin/env python3
"""Fresh-process v003 regression producer for source-parent obligations."""

from __future__ import annotations

import ast
from contextlib import redirect_stderr, redirect_stdout
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
SEALED_EXECUTION = "__sealed_execution_context__" in globals()
EXPECTED_OBLIGATION_TABLE_SHA256 = (
    "64d28520dcc8e5049a2318b3e4a1456dbff255aa1c71ad2eb1a6ef853159563e"
)
STATUS_LINE = re.compile(r"^([A-Za-z][A-Za-z0-9_]*) = (true|false)$")
OBLIGATION_ROW = re.compile(
    r"^\| (SP\d{2}) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \|$"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def clean_environment() -> dict[str, str]:
    allowed = {}
    for key in ("HOME", "PATH", "TMPDIR", "LANG", "LC_ALL"):
        if key in os.environ:
            allowed[key] = os.environ[key]
    allowed["PYTHONPATH"] = ""
    allowed["PYTHONSTARTUP"] = ""
    allowed["PYTHONOPTIMIZE"] = ""
    allowed["PYTHONDONTWRITEBYTECODE"] = "1"
    allowed["PYTHONHASHSEED"] = "0"
    return allowed


def run(script: str, optimize_level: int = 0) -> str:
    require(optimize_level in (0, 1), "subordinate optimize level must be 0 or 1")
    if SEALED_EXECUTION:
        path = ROOT / "scripts" / script
        source = path.read_bytes()
        stdout = io.StringIO()
        stderr = io.StringIO()
        namespace = {
            "__name__": "__main__",
            "__file__": str(path),
            "__package__": None,
            "__cached__": None,
        }
        try:
            with redirect_stdout(stdout), redirect_stderr(stderr):
                exec(
                    compile(
                        source,
                        str(path),
                        "exec",
                        optimize=optimize_level,
                    ),
                    namespace,
                )
        except SystemExit as error:
            require(
                error.code in (None, 0),
                f"{script} failed in sealed "
                f"optimize={optimize_level} execution: "
                f"{stderr.getvalue().strip()}",
            )
        require(
            not stderr.getvalue(),
            f"{script} wrote sealed stderr: {stderr.getvalue().strip()}",
        )
        return stdout.getvalue()

    command = [sys.executable]
    if optimize_level:
        command.append("-O")
    command.extend(["-B", str(ROOT / "scripts" / script)])
    result = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        env=clean_environment(),
    )
    require(
        result.returncode == 0,
        f"{script} failed (optimize={optimize_level}): "
        f"{result.stderr.strip()}",
    )
    return result.stdout


def contains_assert(script: str) -> bool:
    tree = ast.parse((ROOT / "scripts" / script).read_text(encoding="utf-8"))
    return any(isinstance(node, ast.Assert) for node in ast.walk(tree))


def parse_status_block(text: str, heading: str = "## Status") -> dict[str, bool]:
    start = text.rfind(heading)
    require(start >= 0, f"missing status heading: {heading}")
    fence_start = text.find("```text", start)
    require(fence_start >= 0, f"missing status fence after {heading}")
    body_start = text.find("\n", fence_start) + 1
    fence_end = text.find("```", body_start)
    require(fence_end >= 0, f"unterminated status fence after {heading}")
    statuses: dict[str, bool] = {}
    for line in text[body_start:fence_end].splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        match = STATUS_LINE.fullmatch(stripped)
        require(match is not None, f"invalid machine-status line: {stripped}")
        key, value = match.groups()
        require(key not in statuses, f"duplicate machine-status key: {key}")
        statuses[key] = value == "true"
    require(bool(statuses), f"empty machine-status block after {heading}")
    return statuses


def expect(
    statuses: dict[str, bool],
    expected: dict[str, bool],
    label: str,
) -> None:
    for key, value in expected.items():
        require(key in statuses, f"{label} missing status key: {key}")
        require(
            statuses[key] is value,
            f"{label} status {key} is {statuses[key]}, expected {value}",
        )


def parse_obligations(text: str) -> dict[str, tuple[str, str, str]]:
    obligations: dict[str, tuple[str, str, str]] = {}
    for line in text.splitlines():
        match = OBLIGATION_ROW.fullmatch(line.strip())
        if not match:
            continue
        identifier, name, state, closure = match.groups()
        require(identifier not in obligations, f"duplicate obligation: {identifier}")
        obligations[identifier] = (name.strip(), state.strip(), closure.strip())
    return obligations


def obligation_table_sha256(
    obligations: dict[str, tuple[str, str, str]],
) -> str:
    payload = {
        identifier: list(values)
        for identifier, values in obligations.items()
    }
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def reject_duplicate_json_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    output: dict[str, object] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"duplicate JSON key: {key}")
        output[key] = value
    return output


def read_json_strict(path: Path) -> dict[str, object]:
    value = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicate_json_keys,
        parse_constant=lambda value: (_ for _ in ()).throw(
            ValueError(f"non-finite JSON constant: {value}")
        ),
    )
    require(isinstance(value, dict), f"{path} must contain a JSON object")
    return value


def parse_output_record(output: str, script: str) -> dict[str, str]:
    record: dict[str, str] = {}
    for line in output.splitlines():
        if line != line.strip() or not line:
            raise ValueError(f"{script} has malformed output line")
        key, separator, value = line.rpartition("=")
        if not (separator and key and value):
            raise ValueError(f"{script} has non-record output line: {line}")
        if key in record:
            raise ValueError(f"{script} has duplicate output key: {key}")
        record[key] = value
    if not record:
        raise ValueError(f"{script} produced an empty output record")
    return record


def content_root(paths: tuple[str, ...]) -> str:
    digest = hashlib.sha256()
    for relative in sorted(paths):
        payload = (ROOT / relative).read_bytes()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(payload).digest())
    return digest.hexdigest()


def main() -> None:
    documents = {
        "gate": "BID_SOURCE_PARENT_CLOSURE_GATE_V003.md",
        "parent": "BID_CHIRAL_SOURCE_RECORD_INCIDENCE_PARENT_V001.md",
        "activation": "BID_CHARGED_HANDLE_ACTIVATION_DERIVATION_V002.md",
        "composition": "BID_DISTINGUISHABLE_RECORD_CELL_COMPOSITION_DERIVATION_V001.md",
        "lorentz": "BID_LORENTZ_COVARIANT_SOURCE_BOUNDARY_MAP_DERIVATION_V001.md",
        "global_car": "BID_GLOBAL_CAR_RECORD_COMPOSITION_DERIVATION_V001.md",
        "source_family": "BID_SOURCE_DECORATED_FIRST_OPENING_CLASSIFICATION_V001.md",
        "hilbert_old": "BID_ELEMENTARY_RECORD_HILBERT_FUNCTOR_CLASSIFICATION_V001.md",
        "superconnection_old": "BID_PRIMITIVE_BOUNDARY_SUPERCONNECTION_CLASSIFICATION_V001.md",
        "restricted_source_attempt": "BID_FULL_SOURCE_MAP_COMMUTANT_CLASSIFICATION_V001.md",
        "charge_car": "BID_GLOBAL_CAR_CHARGE_AND_ACTIVATION_DERIVATION_V001.md",
        "public_hilbert": "BID_PUBLIC_RECORD_HILBERTIZATION_DERIVATION_V001.md",
        "graded_repair": "BID_GRADED_BOUNDARY_SUPERCONNECTION_REPAIR_V001.md",
        "metric_transport": "BID_BOUNDARY_METRIC_TRANSPORT_DERIVATION_V001.md",
        "graph_refinement": "BID_FIRST_OPENING_GRAPH_REFINEMENT_QUOTIENT_V001.md",
        "root_identity": "BID_ROOT_INCIDENCE_IDENTITY_DERIVATION_V001.md",
        "endpoint_family": "BID_COMPLETE_NORMAL_DEPENDENT_ENDPOINT_MAP_CLASSIFICATION_V001.md",
        "zero_form_inventory": "BID_COMPLETE_ONE_NORMAL_ZERO_FORM_ENUMERATION_V001.md",
        "source_typing": "BID_FULL_DIRAC_CAR_SOURCE_TYPING_DERIVATION_V001.md",
        "charged_cpt": "BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md",
        "axial_phase": "BID_AXIAL_PHASE_CP_REDUCTION_DERIVATION_V001.md",
        "global_descent": "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md",
        "controlled_coupling": "BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md",
        "lorentzian_pole": "BID_LORENTZIAN_SOURCE_SCHUR_POLE_DERIVATION_V001.md",
    }
    texts = {label: read(path) for label, path in documents.items()}
    statuses = {
        label: parse_status_block(
            text,
            "## Machine status" if label == "gate" else "## Status",
        )
        for label, text in texts.items()
    }

    obligations = parse_obligations(texts["gate"])
    expected_ids = {f"SP{index:02d}" for index in range(1, 19)}
    require(set(obligations) == expected_ids, "SP01-SP18 table is not exact")
    require(
        all(name and state and closure for name, state, closure in obligations.values()),
        "an obligation row is incomplete",
    )
    require(
        obligation_table_sha256(obligations)
        == EXPECTED_OBLIGATION_TABLE_SHA256,
        "SP01-SP18 name/state/closure table changed without gate revision",
    )

    expect(
        statuses["gate"],
        {
            "complete_relativistic_source_parent_derived": False,
            "connected_many_record_parent_derived": False,
            "public_record_Hilbertization_derived_given_QR1_through_QR7": True,
            "physical_record_Hilbertization_derived_from_deeper_action": False,
            "physical_charge_operator_constructed_from_disclosed_Dirac_CAR_input": True,
            "existence_of_charged_Dirac_matter_derived_by_BID": False,
            "one_normal_ambient_3plus1_graded_superconnection_typing_derived": True,
            "local_standard_CPT_incidence_quadrature_derived": True,
            "ordinary_CP_even_zero_index_axial_phase_reduced": True,
            "unique_primitive_charged_controlled_coupling_derived": True,
            "finite_stationary_primitive_connected_action_derived": True,
            "primitive_quasifree_Lorentzian_source_edge_pole_derived": True,
            "complete_CPT_CP_reduced_graded_source_parent_derived": False,
            "physical_source_mass_computed": False,
            "complete_Q_spec_sealed": False,
            "physical_Thomson_stiffness_computed": False,
            "alpha_computed": False,
            "proof_authorized": False,
        },
        "closure gate",
    )
    expect(
        statuses["source_typing"],
        {
            "three_plus_one_spin_Dirac_branch_disclosed": True,
            "local_Dirac_chiral_fiber_typed": True,
            "positive_Cauchy_data_Hilbert_space_constructed": True,
            "stationary_Dirac_spectral_projectors_constructed_given_disclosed_branch": True,
            "charge_conjugation_intertwines_positive_and_negative_spectral_subspaces": True,
            "particle_antiparticle_one_particle_carrier_constructed_given_polarization": True,
            "fermionic_Fock_CAR_carrier_constructed_given_standard_CAR": True,
            "compact_vector_U1_action_constructed": True,
            "chirality_commutes_with_vector_charge": True,
            "charge_conjugation_exchanges_chirality": True,
            "two_state_chirality_quotient_relation_derived": True,
            "existence_of_charged_Dirac_matter_derived_by_BID": False,
            "vacuum_polarization_derived_by_BID": False,
            "continuum_CAR_theorem_derived_by_finite_audit": False,
            "complete_connected_source_record_action_derived": False,
            "alpha_computed": False,
        },
        "integrated Dirac/CAR source typing",
    )
    expect(
        statuses["charged_cpt"],
        {
            "standard_Dirac_CPT_disclosed_input": True,
            "explicit_Weyl_basis_CPT_antiunitary_constructed": True,
            "all_four_gamma_CPT_intertwiners_verified": True,
            "future_normal_pushforward_tetrad_and_reorientation_typed": True,
            "positive_boundary_Hilbert_CPT_isometry_verified": True,
            "charge_line_conjugation_typed": True,
            "positive_negative_neutral_charge_projector_CPT_actions_verified": True,
            "induced_target_transport_CPT_chain_equation_derived": True,
            "different_normal_transport_cohort_verified": True,
            "weighted_adjoint_incidence_dilation_CPT_covariance_derived": True,
            "gamma5_real_incidence_product_CPT_even": False,
            "CPT_odd_Hermitian_cellular_quadrature_derived": True,
            "CPT_even_Cliffordized_incidence_phase_unique_up_to_orientation_sign": True,
            "phase_constraint_derived_from_computed_antiunitary_action": True,
            "gamma5_CPT_odd_cellular_quadrature_product_CPT_even": True,
            "general_controlled_coupling_CPT_conditions_derived": True,
            "nonzero_neutral_control_block_verified": True,
            "neutral_and_charged_negative_controls_rejected": True,
            "orientation_blind_B_plus_equals_B_minus_derived": False,
            "CPT_selects_axial_phase_delta_zero": False,
            "complete_connected_source_record_action_derived": False,
            "alpha_computed": False,
        },
        "charged cellular CPT intertwiner",
    )
    expect(
        statuses["axial_phase"],
        {
            "charge_conjugation_and_parity_actions_both_constructed": True,
            "CP_even_coefficient_kernel_is_scalar_axis": True,
            "delta_zero_and_pi_unitarily_endpoint_rephasing_equivalent_as_incidence_maps": True,
            "closed_doubled_cell_source_determinant_regulator_disclosed": True,
            "regulated_Dirac_domain_explicit": True,
            "gamma5_preserves_regulated_Dirac_domain": True,
            "massless_Dirac_operator_anticommutes_with_gamma5": True,
            "boundary_eta_phase_absent_in_closed_regulator": True,
            "ordinary_zero_index_topological_sector_disclosed": True,
            "regulated_determinant_mass_sign_ratio_evaluated": True,
            "nonzero_index_domain_negative_control_rejected": True,
            "delta_zero_and_pi_physically_equivalent_in_zero_index_branch": True,
            "ordinary_CP_even_axial_phase_class_unique": True,
            "CP_violating_enlarged_branches_excluded_universally": False,
            "complete_connected_source_record_action_derived": False,
            "alpha_computed": False,
        },
        "axial phase and anomaly reduction",
    )
    expect(
        statuses["controlled_coupling"],
        {
            "source_carrier_factorized_as_multiplicity_tensor_Dirac": True,
            "Dirac_spinor_factor_retained_as_structural_data": True,
            "charge_only_public_naturality_acts_only_on_unresolved_multiplicity": True,
            "internal_sector_unitary_commutant_computed": True,
            "source_independent_parent_is_monoidal_identity_extension": True,
            "boundary_control_projection_module_axioms_adopted": True,
            "projection_module_control_map_uniqueness_derived": True,
            "charged_control_is_orthogonal_spectral_compression": True,
            "compression_preserves_parent_incidence_normalization": True,
            "independent_sector_rescaling_excluded_by_single_operator_incidence": True,
            "compressed_operator_first_opening_interval_crosscheck": True,
            "unique_primitive_charged_controlled_coupling_derived": True,
            "complete_connected_source_record_action_derived": False,
            "alpha_computed": False,
        },
        "unique charged controlled coupling",
    )
    expect(
        statuses["global_descent"],
        {
            "global_boundary_descent_principle_adopted": True,
            "primitive_quasi_free_completeness_adopted": True,
            "historically_target_blind": False,
            "target_value_used_in_construction": False,
            "single_global_source_CAR_carrier_retained": True,
            "record_factors_distinguishable_and_fermion_even": True,
            "record_directions_fermionized": False,
            "finite_stationary_oriented_one_complex_scope": True,
            "finite_gluing_associativity_derived": True,
            "orientation_reversal_covariance_derived": True,
            "actual_SP17_one_cell_incidence_zero_form_recovered": True,
            "complete_SP17_kinetic_operator_recovered_here": False,
            "global_operator_valued_one_particle_superconnection_constructed": True,
            "primitive_shared_support_structure_computed": True,
            "two_step_Laplacian_not_mislabeled_as_primitive_overlap": True,
            "operator_valued_quasi_free_CAR_lift_derived": True,
            "primitive_quartic_competitor_rejected": True,
            "time_dependent_continuum_ordering_derived": False,
            "connected_preparation_derived": False,
            "physical_source_pole_and_residue_derived": False,
            "alpha_computed": False,
        },
        "finite stationary global boundary descent",
    )
    expect(
        statuses["lorentzian_pole"],
        {
            "Lorentz_signature_plus_minus_minus_minus_disclosed": True,
            "Lorentzian_chiral_reality_factor_derived": True,
            "Lorentzian_inverse_kernel_constructed": True,
            "proper_orthochronous_Lorentz_covariance_derived": True,
            "full_parity_covariance_derived": False,
            "timelike_source_edge_shell_derived": True,
            "finite_Schur_resolvent_recovered_covariantly": True,
            "primitive_mass_relation_m_star_T_R_equals_pi_derived": True,
            "stationary_one_particle_Hamiltonian_Hermitian": True,
            "source_edge_massive_spectral_weight_positive": True,
            "source_edge_internal_massive_pair_degeneracy_retained": True,
            "Feynman_i0_follows_from_disclosed_state_not_Schur_algebra": True,
            "complete_CTP_propagator_derived": False,
            "physical_durability_derived": False,
            "gauge_invariant_dressed_source_spectrum_derived": False,
            "interacting_isolated_pole_proved": False,
            "physical_source_mass_computed": False,
            "alpha_computed": False,
        },
        "primitive Lorentzian source Schur pole",
    )
    expect(
        statuses["parent"],
        {
            "conditional_pure_offdiagonal_perfect_transfer_forces_equal_endpoint_magnitudes": True,
            "conditional_scaled_norm_and_perfect_transfer_force_a_b_magnitudes_one": True,
            "parent_zero_form_detuning_derived_absent": False,
            "complete_physical_source_record_parent_derived": False,
            "physical_source_mass_computed": False,
            "connected_many_record_parent_derived": False,
            "alpha_computed": False,
        },
        "restricted incidence parent",
    )
    expect(
        statuses["activation"],
        {
            "compact_U1_integer_charge_spectrum_inherited_given_representation": True,
            "primitive_minus_one_zero_plus_one_sector_declared": True,
            "full_integer_spectrum_access_projector_equals_Q_squared": False,
            "restricted_primitive_sector_access_projector_equals_Q_squared": True,
            "antiunitary_CPT_operator_constructed": False,
            "unique_charge_controlled_record_coupling_derived": False,
            "pure_charged_branch_tau_R_authorized": False,
        },
        "restricted charged activation",
    )
    expect(
        statuses["source_family"],
        {
            "linear_path_graph_presentation_equivalence_derived": True,
            "universal_graph_exhaustion_across_enlarged_branches": False,
            "metric_compatible_edge_transport_derived_given_transported_normal": True,
            "root_incidence_identity_derived": True,
            "normal_dependent_root_zero_forms_forbidden_in_parent": False,
            "chiral_even_and_chiral_odd_endpoint_competitors_admitted": True,
            "endpoint_zero_form_is_incidence_coefficient": False,
            "normal_dependent_endpoint_zero_form_family_exhausted_given_one_normal": True,
            "all_spinor_scaled_normalization_derived": False,
            "conditional_endpoint_scaled_unitary_lemma_derived": True,
            "endpoint_U2_element_selected": False,
            "axial_source_frame_quotient_used": False,
            "record_Hilbertization_derived_given_QR1_through_QR7": True,
            "record_Hilbertization_derived_from_deeper_boundary_action": False,
            "bare_covariant_incidence_column_is_minusI_plus_Ue": True,
            "root_and_endpoint_zero_forms_retained_as_parent_competitors": True,
            "parent_zero_form_detuning_excluded": False,
            "complete_source_record_parent_closed": False,
            "global_connected_source_record_action_derived": False,
        },
        "source incidence family",
    )
    expect(
        statuses["restricted_source_attempt"],
        {
            "unitary_source_frame_quotient_physically_authorized": False,
            "one_physical_relative_axial_phase_established": False,
            "normal_dependent_source_map_family_exhausted": False,
            "superseded_as_authoritative_classification": True,
        },
        "superseded source-map attempt",
    )
    expect(
        statuses["root_identity"],
        {
            "root_incidence_component_is_negative_identity": True,
            "normal_dependent_root_zero_forms_forbidden_in_complete_action": False,
            "complete_parent_zero_form_family_enumerated": False,
        },
        "root incidence",
    )
    expect(
        statuses["endpoint_family"],
        {
            "normal_dependent_little_group_commutant_dimension_four": True,
            "I_gamma5_slashn_slashn_gamma5_basis_complete": True,
            "chiral_even_endpoint_competitors_admitted": True,
            "chiral_odd_endpoint_subfamily_only": False,
            "endpoint_zero_form_is_incidence_coefficient": False,
            "endpoint_zero_form_competitor_class_complete_given_one_normal": True,
            "endpoint_rank_strata_zero_two_four_complete": True,
            "all_spinor_scaled_normalization_derived_from_QR1_through_QR7": False,
            "conditional_scaled_normalization_forces_E_sharp_E_scalar": True,
            "conditional_rank_deficient_endpoint_rejected": True,
            "conditional_anisotropic_endpoint_rescaling_rejected": True,
            "h_n_adjoint_used_away_from_reference_normal": True,
            "conditional_endpoint_family_reduces_to_U2": True,
            "endpoint_U2_element_selected": False,
            "root_source_frame_axial_quotient_used": False,
            "bare_covariant_incidence_column_is_minusI_plus_Ue": True,
            "conditional_pure_offdiagonal_equal_transfer_independent_of_U2": True,
            "parent_zero_form_detuning_excluded": False,
            "complete_parent_zero_form_family_enumerated": False,
        },
        "endpoint family",
    )
    expect(
        statuses["public_hilbert"],
        {
            "record_axioms_QR1_through_QR7_disclosed": True,
            "pointer_projection_orthogonality_forces_offdiagonal_zero": True,
            "probability_preserving_singleton_inclusions_force_unit_diagonal": True,
            "without_QR3_common_scale_freedom_reproduced": True,
            "public_record_counting_metric_derived_from_disclosed_quantum_record_axioms": True,
            "strong_symmetric_monoidal_record_functor_derived_given_QR6_QR7": True,
            "Born_kinematics_derived_from_deeper_action": False,
            "global_connected_source_record_action_derived": False,
        },
        "public record Hilbertization",
    )
    expect(
        statuses["graded_repair"],
        {
            "spin_chirality_and_cellular_grading_separated": True,
            "cellular_carrier_C0_direct_sum_C1_typed": True,
            "source_cellular_carrier_complex_dimension_twelve": True,
            "bare_rectangular_incidence_embedded_in_square_dilation": True,
            "cellular_b_partial_odd_under_cellular_grading": True,
            "CPT_selected_c_partial_odd_under_cellular_grading": True,
            "CPT_selected_c_partial_square_equals_b_partial_square": True,
            "graded_superconnection_curvature_identity_corrected": True,
            "complete_one_normal_zero_form_inventory_imported": True,
            "Laplace_compatible_odd_subspace_derived": True,
            "Cliffordized_operator_terms_same_dimension": True,
            "Cliffordized_square_first_order_cross_term_cancelled": True,
            "differential_order_and_BID_incidence_degree_distinguished": True,
            "primitive_BID_filtration_derived_independently": False,
            "local_standard_CPT_incidence_quadrature_applied": True,
            "complete_CP_axial_reduction_applied": False,
        },
        "graded superconnection repair",
    )
    expect(
        statuses["zero_form_inventory"],
        {
            "cellular_carrier_C0_direct_sum_C1_typed": True,
            "cellular_carrier_complex_dimension_three": True,
            "source_cellular_carrier_complex_dimension_twelve": True,
            "two_normal_fibers_reduced_to_common_frame_by_metric_transport": True,
            "bare_incidence_dilation_embedded_in_cellular_endomorphisms": True,
            "spin_Hn_self_adjoint_commutant_real_dimension_four": True,
            "record_Hermitian_algebra_real_dimension_nine": True,
            "full_Hn_self_adjoint_zero_form_real_dimension_thirty_six": True,
            "record_even_zero_form_real_dimension_twenty": True,
            "record_odd_zero_form_real_dimension_sixteen": True,
            "Laplace_compatible_record_odd_zero_form_real_dimension_four": True,
            "complete_one_normal_zero_form_inventory_derived": True,
            "Clifford_compatible_odd_subspace_derived": True,
            "primitive_incidence_selected_given_two_adopted_principles": True,
            "primitive_incidence_selected_without_adopted_principles": False,
            "local_standard_CPT_incidence_quadrature_applied": True,
            "complete_CP_axial_reduction_applied": False,
            "enlarged_geometric_zero_form_branches_exhausted": False,
            "complete_connected_source_record_action_derived": False,
        },
        "one-normal zero-form inventory",
    )
    expect(
        statuses["charge_car"],
        {
            "global_CAR_particle_antiparticle_Fock_core_constructed": True,
            "compact_vector_U1_generator_constructed": True,
            "full_spectrum_charged_access_projector_derived": True,
            "full_spectrum_P_ch_equals_Q_squared": False,
            "antiunitary_charge_conjugation_constructed": True,
            "two_record_conditions_derived_from_vector_U1_alone": False,
        },
        "global CAR charge",
    )
    expect(
        statuses["global_car"],
        {
            "global_source_CAR_algebra_typed": True,
            "source_factor_replicated_per_record_cell": False,
            "quadratic_number_preserving_family_complete_among_all_even_couplings": False,
            "complete_connected_source_record_action_derived": False,
        },
        "global CAR composition",
    )
    expect(
        statuses["composition"],
        {
            "connected_cross_cell_terms_derived": False,
            "connected_preparation_beyond_primitive_product_derived": False,
        },
        "record composition",
    )
    expect(
        statuses["lorentz"],
        {
            "proper_orthochronous_Lorentz_covariance_derived": True,
            "charged_boundary_CPT_intertwiner_derived": False,
            "global_particle_antiparticle_CAR_carrier_derived": False,
        },
        "Lorentz map",
    )
    expect(
        statuses["metric_transport"],
        {
            "boundary_metric_edge_transport_isometry_derived": True,
            "proper_orthochronous_scope_only": True,
            "charged_boundary_CPT_intertwiner_derived": False,
        },
        "boundary metric transport",
    )
    expect(
        statuses["graph_refinement"],
        {
            "linear_first_opening_path_unique_reduced_representative": True,
            "minimal_graph_universal_across_enlarged_branches": False,
        },
        "graph refinement",
    )
    expect(
        statuses["superconnection_old"],
        {
            "primitive_BID_filtration_derived_independently": False,
            "incidence_degree_and_differential_order_distinguished": False,
            "displayed_Laplace_type_square_verified": False,
            "minimal_versus_independent_Pauli_parent_fork_closed_given_superconnection_principle": False,
        },
        "superseded superconnection inventory",
    )

    expected_outputs = {
        "audit_bid_elementary_record_hilbert_functor_classification_v001.py": (
            "BID_ELEMENTARY_RECORD_METRIC_CONDITIONAL_AUDIT=PASS_BLOCKED",
            "deeper_physical_Hilbertization_derived=FALSE",
        ),
        "audit_bid_source_decorated_first_opening_classification_v001.py": (
            "BID_SOURCE_DECORATED_RESTRICTED_FAMILY_AUDIT=PASS_BLOCKED",
            "endpoint_U2_element_selected=FALSE",
        ),
        "audit_bid_charged_handle_activation_v002.py": (
            "BID_CHARGED_HANDLE_RESTRICTED_ALGEBRA_AUDIT=PASS_BLOCKED",
            "integer_spectrum_status=INHERITED_GIVEN_COMPACT_U1_REPRESENTATION",
            "sign_insensitive_activation=ADOPTED_PREMISE",
            "pure_charged_branch_tau_R_authorized=FALSE",
        ),
        "audit_bid_primitive_boundary_superconnection_classification_v001.py": (
            "BID_PRIMITIVE_SUPERCONNECTION_CONDITIONAL_AUDIT=PASS_BLOCKED",
            "primitive_Pauli_exclusion_theorem=FALSE",
        ),
        "audit_bid_full_source_map_commutant_classification_v001.py": (
            "BID_RESTRICTED_SOURCE_MAP_ATTEMPT_AUDIT=SUPERSEDED",
            "normal_dependent_source_map_family_exhausted=FALSE",
            "source_frame_axial_quotient_physically_authorized=FALSE",
        ),
        "audit_bid_global_car_charge_and_activation_v001.py": (
            "BID_GLOBAL_CAR_CHARGE_ACTIVATION_AUDIT=PASS_BLOCKED",
            "full_spectrum_Q_squared_access=REJECTED",
        ),
        "audit_bid_public_record_hilbertization_derivation_v001.py": (
            "BID_PUBLIC_RECORD_HILBERTIZATION_AUDIT=PASS_CONDITIONAL",
            "without_QR3_common_scale_freedom=REPRODUCED",
            "Born_kinematics_derived_from_deeper_action=FALSE",
        ),
        "audit_bid_graded_boundary_superconnection_repair_v001.py": (
            "BID_GRADED_BOUNDARY_SUPERCONNECTION_REPAIR_AUDIT=PASS_BLOCKED",
            "source_cellular_carrier_complex_dimension=12",
            "cellular_b_partial_shape=3x3",
            "spin_lifted_B_hat_partial_shape=12x12",
            "bare_rectangular_incidence_square_dilation=PASS",
            "CPT_selected_cellular_quadrature=I_GAMMA_CELL_B_PARTIAL",
            "CPT_selected_cellular_quadrature_square=BARE_INCIDENCE_SQUARE",
            "ambient_3plus1_Laplace_compatible_spin_direction=gamma5",
            "intrinsic_tangential_compatible_spin_dimension=2",
            "primitive_BID_filtration_derived_independently=FALSE",
        ),
        "audit_bid_boundary_metric_transport_derivation_v001.py": (
            "BID_BOUNDARY_METRIC_TRANSPORT_AUDIT=PASS",
            "charged_boundary_CPT_intertwiner_derived=FALSE",
        ),
        "audit_bid_first_opening_graph_refinement_quotient_v001.py": (
            "BID_FIRST_OPENING_GRAPH_REFINEMENT_AUDIT=PASS",
            "universal_graph_exhaustion_across_enlarged_branches=FALSE",
        ),
        "audit_bid_chiral_source_record_incidence_parent_v001.py": (
            "BID_CHIRAL_SOURCE_RECORD_INCIDENCE_PARENT_AUDIT=PASS_BLOCKED",
            "source_independent_scaled_normalization_derived=FALSE",
            "parent_zero_form_detuning_derived_absent=FALSE",
            "full_normal_dependent_source_map_family_exhausted=FALSE",
        ),
        "audit_bid_active_handle_control_v001.py": (
            "BID_ACTIVE_HANDLE_CONTROL_AUDIT=PASS_BLOCKED",
            "full_star_completes_at_handle_tau_R=FALSE",
        ),
        "audit_bid_physical_record_amplitude_zero_free_v001.py": (
            "BID_PHYSICAL_RECORD_AMPLITUDE_ZERO_FREE_AUDIT=PASS_BLOCKED",
            "root_survival_log_response=REJECTED",
        ),
        "audit_bid_many_record_parent_identifiability_v001.py": (
            "BID_MANY_RECORD_PARENT_IDENTIFIABILITY_AUDIT=PASS_BLOCKED",
            "connected_many_record_parent_unique=FALSE",
        ),
        "audit_bid_root_incidence_identity_derivation_v001.py": (
            "BID_ROOT_INCIDENCE_IDENTITY_AUDIT=PASS_BLOCKED",
            "complete_parent_zero_form_family_enumerated=FALSE",
        ),
        "audit_bid_complete_normal_dependent_endpoint_map_classification_v001.py": (
            "BID_COMPLETE_NORMAL_ENDPOINT_MAP_AUDIT=PASS_BLOCKED",
            "endpoint_zero_form_role=PARENT_NOT_INCIDENCE",
            "conditional_all_spinor_normalization_forces_E_sharp_E_scalar=PASS",
            "conditional_rank_deficient_nonzero_endpoint=REJECTED",
            "conditional_anisotropic_endpoint_rescaling=REJECTED",
            "endpoint_U2_element_selected=FALSE",
            "root_axial_source_frame_quotient_used=FALSE",
        ),
        "audit_bid_complete_one_normal_zero_form_enumeration_v001.py": (
            "BID_COMPLETE_ONE_NORMAL_ZERO_FORM_ENUMERATION_AUDIT=PASS_BLOCKED",
            "source_cellular_carrier_complex_dimension=12",
            "full_zero_form_real_dimension=36",
            "record_even_zero_form_real_dimension=20",
            "record_odd_zero_form_real_dimension=16",
            "ambient_3plus1_Clifford_constraint_rank=12",
            "Laplace_compatible_record_odd_real_dimension=4",
            "ambient_kernel_equals_gamma5_tensor_record_odd=PASS",
            "intrinsic_tangential_competitor_nullity=8",
            "bare_incidence_dilation_in_odd_basis=PASS",
            "CPT_selected_incidence_quadrature_in_odd_basis=PASS",
            "CPT_selected_incidence_square_equals_bare_square=PASS",
            "complete_connected_source_record_action_derived=FALSE",
        ),
        "audit_bid_full_dirac_car_source_typing_v001.py": (
            "BID_FULL_DIRAC_CAR_SOURCE_TYPING_AUDIT=PASS_CONDITIONAL",
            "stationary_Dirac_spectral_projectors=PASS",
            "charge_conjugation_spectral_exchange=PASS",
            "charge_conjugation_chirality_exchange=PASS",
            "finite_particle_antiparticle_complete_CAR=PASS",
            "four_to_two_dimensional_chirality_factorization=PASS",
            "continuum_CAR_status=DISCLOSED_STANDARD_RESULT",
        ),
        "audit_bid_charged_cellular_cpt_intertwiner_v001.py": (
            "BID_CHARGED_CELLULAR_CPT_INTERTWINER_AUDIT=PASS_BLOCKED",
            "all_four_gamma_CPT_intertwiners=PASS",
            "legacy_gamma5_only_CPT_matrix=REJECTED",
            "future_normal_pushforward_reorientation_checks=12",
            "future_normal_Hilbert_isometry_checks=12",
            "different_normal_transport_CPT_chain_checks=8",
            "different_normal_transport_CPT_chain_equation=PASS",
            "weighted_adjoint_incidence_dilation_CPT_covariance=PASS",
            "gamma5_real_incidence_product_CPT_parity=ODD",
            "CPT_even_Cliffordized_incidence_phase=PURE_IMAGINARY_UNIQUE_UP_TO_SIGN",
            "computed_phase_constraint_rank=1",
            "computed_phase_kernel_dimension=1",
            "gamma5_conjugate_quadrature_product_CPT_parity=EVEN",
            "controlled_coupling_negative_control=REJECTED",
            "nonzero_neutral_CPT_even_block=PASS",
            "neutral_block_negative_control=REJECTED",
            "orientation_blind_B_plus_equals_B_minus=FALSE",
        ),
        "audit_bid_axial_phase_cp_reduction_v001.py": (
            "BID_AXIAL_PHASE_CP_REDUCTION_AUDIT=PASS_BLOCKED",
            "combined_CP_action_constructed=PASS",
            "computed_CP_even_kernel=SCALAR_AXIS",
            "source_determinant_regulator=CLOSED_DOUBLED_CELL",
            "regulated_Dirac_domain_gamma5_invariant=PASS",
            "zero_index_spectral_pairing=DERIVED",
            "boundary_eta_phase=ABSENT_CLOSED_REGULATOR",
            "zero_index_fujikawa_jacobian=ONE",
            "nonzero_index_negative_control=REJECTED",
            "zero_index_regulated_determinant_mass_sign_equivalence=PASS",
            "nonzero_index_regulated_determinant_mass_sign_equivalence=REJECTED",
        ),
        "audit_bid_unique_charged_controlled_coupling_v001.py": (
            "BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_AUDIT=PASS_BLOCKED",
            "source_carrier_factorization=MULTIPLICITY_TENSOR_DIRAC",
            "Dirac_spinor_factor=STRUCTURAL_NOT_MULTIPLICITY",
            "internal_sector_unitary_commutant_dimension=3",
            "projection_module_control_affine_nullity=0",
            "projection_module_unique_control=PBP",
            "rescaled_control_retraction_negative_control=REJECTED",
            "charged_control=ORTHOGONAL_SPECTRAL_COMPRESSION",
            "compression_preserves_parent_incidence_normalization=PASS",
            "compressed_operator_first_opening_interval=CROSSCHECK_PASS",
            "controlled_operator=P_CH_TENSOR_B_Q",
        ),
        "audit_bid_global_boundary_descent_quasi_free_v001.py": (
            "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_AUDIT=PASS_BLOCKED",
            "single_global_source_CAR_mode_count=12",
            "duplicated_source_per_record_cell=FALSE",
            "distinguishable_even_record_factor_count=2",
            "record_directions_fermionized=FALSE",
            "three_cell_pushout_associativity=PASS",
            "actual_SP17_one_cell_incidence_zero_form_recovered=PASS",
            "complete_SP17_kinetic_operator_recovered_here=FALSE",
            "complete_operator_orientation_reversal_covariance=PASS",
            "primitive_shared_support_commutator=NONZERO",
            "h_squared_role=INDUCED_TWO_STEP_NOT_PRIMITIVE_OVERLAP",
            "operator_valued_CAR_one_source_recovery=PASS",
            "quartic_competitor_two_source_difference=DETECTED",
            "primitive_quartic_competitor=REJECTED_BY_QUASI_FREE_COMPLETENESS",
        ),
        "audit_bid_lorentzian_source_schur_pole_v001.py": (
            "BID_LORENTZIAN_SOURCE_SCHUR_POLE_AUDIT=PASS_BLOCKED",
            "Lorentzian_chiral_reality_factor=I",
            "missing_i_reality_negative_control=REJECTED",
            "Lorentzian_kernel_square=P2_MINUS_MU2_C2",
            "source_edge_Schur_propagator=SLASH_P_OVER_P2_MINUS_2MU2",
            "primitive_source_edge_shell=TIMELIKE",
            "stationary_Hamiltonian_Hermitian=PASS",
            "source_edge_zero_mode_weight=0",
            "source_edge_massive_spectral_weight=1",
            "source_edge_internal_massive_pair_degeneracy=2",
            "positive_energy_spectral_projector=PASS",
            "edge_compressed_positive_energy_residue=STRICTLY_POSITIVE",
            "Feynman_i0_source=DISCLOSED_STATIONARY_STATE",
            "proper_orthochronous_Lorentz_covariance=PASS",
            "full_parity_covariance_derived=FALSE",
            "interacting_isolated_pole_proved=FALSE",
        ),
        "audit_bid_lorentz_covariant_source_boundary_map_v001.py": (
            "BID_LOCAL_PROPER_LORENTZ_RIESZ_KINEMATICS_AUDIT=PASS",
            "Clifford_3_plus_1=PASS",
            "boundary_normal_Riesz_map=PASS",
            "proper_orthochronous_Lorentz_covariance_cases=27",
            "charged_boundary_CPT_intertwiner_derived=FALSE",
            "relative_axial_phase_unresolved=TRUE",
        ),
        "audit_bid_distinguishable_record_cell_composition_v001.py": (
            "BID_DISTINGUISHABLE_RECORD_CELL_COMPOSITION_AUDIT=PASS_BLOCKED",
            "labeled_two_cell_dimension=9",
            "cell_swap_is_unitary_not_identification=PASS",
            "connected_cross_cell_terms=PENDING_QSPEC",
        ),
        "audit_bid_global_car_record_composition_v001.py": (
            "BID_FINITE_GLOBAL_CAR_RECORD_COMPOSITION_AUDIT=PASS_BLOCKED",
            "typed_total_dimension=36",
            "toy_duplicate_same_global_modes_dimension=144",
            "CAR_relations=PASS",
            "overlap_connected_competitor_nonzero=PASS",
            "complete_connected_source_record_action_derived=FALSE",
        ),
    }
    contract_path = ROOT / "BID_SOURCE_PARENT_SUBORDINATE_OUTPUT_CONTRACT_V001.json"
    contract = read_json_strict(contract_path)
    require(
        contract.get("schema")
        == "gravacle.bid-source-parent-subordinate-output.v001",
        "wrong subordinate-output contract schema",
    )
    require(
        contract.get("alpha_computed") is False,
        "subordinate-output contract lost alpha firewall",
    )
    contract_records = contract.get("records")
    require(
        isinstance(contract_records, dict)
        and set(contract_records) == set(expected_outputs),
        "subordinate-output contract script inventory is not exact",
    )

    duplicate_output_rejected = False
    try:
        parse_output_record("synthetic=FALSE\nsynthetic=TRUE\n", "synthetic")
    except ValueError:
        duplicate_output_rejected = True
    require(duplicate_output_rejected, "duplicate subordinate output was accepted")

    # The current Python environment is not yet a content-addressed -I -S
    # snapshot because numpy resides in the user-site runtime. Until SP14 is
    # sealed, sanitize startup inputs, reject asserts, and dual-run every
    # subordinate audit under normal and optimized interpreters.
    if SEALED_EXECUTION:
        require(
            sys.flags.isolated
            and sys.flags.no_site
            and sys.flags.dont_write_bytecode
            and sys.flags.ignore_environment
            and sys.flags.no_user_site,
            "sealed gate requires CPython -I -S -B",
        )
        require(
            sys.flags.optimize in (0, 1),
            "sealed producer requires process optimize level 0 or 1",
        )
        require(
            not any(
                name in sys.modules for name in ("sitecustomize", "usercustomize")
            ),
            "custom startup module was loaded in sealed execution",
        )
    else:
        preflight = subprocess.run(
            [
                sys.executable,
                "-B",
                "-c",
                "import sys; print(int('sitecustomize' in sys.modules),"
                "int('usercustomize' in sys.modules))",
            ],
            check=False,
            capture_output=True,
            text=True,
            env=clean_environment(),
        )
        require(preflight.returncode == 0, "Python startup preflight failed")
        require(preflight.stdout.strip() == "0 0", "custom startup module was loaded")

    for script, required_lines in expected_outputs.items():
        require(not contains_assert(script), f"{script} still contains Python assert")
        if SEALED_EXECUTION:
            normal = run(script, optimize_level=sys.flags.optimize)
        else:
            normal = run(script, optimize_level=0)
            optimized = run(script, optimize_level=1)
            require(normal == optimized, f"{script} changes under python -O")
        try:
            normal_record = parse_output_record(normal, script)
        except ValueError as error:
            raise SystemExit(f"FAIL: {error}") from error
        expected_record = contract_records[script]
        require(
            isinstance(expected_record, dict)
            and all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in expected_record.items()
            ),
            f"{script} output contract is malformed",
        )
        require(
            normal_record == expected_record,
            f"{script} output record differs from its frozen exact contract",
        )
        require(
            normal_record.get("alpha_computed") == "FALSE",
            f"{script} lost alpha firewall",
        )
        for required_line in required_lines:
            key, separator, value = required_line.rpartition("=")
            require(bool(separator and key and value), "malformed required output line")
            require(
                normal_record.get(key) == value,
                f"{script} lost required output: {required_line}",
            )

    blocking_ids = {
        identifier
        for identifier, (_, state, _) in obligations.items()
        if not state.startswith("PASS")
    }
    closure = not blocking_ids
    require(not closure, "source-parent closure unexpectedly passed")
    require(
        statuses["gate"]["complete_relativistic_source_parent_derived"] is False,
        "machine status contradicts computed blocked obligations",
    )

    bound_paths = tuple(documents.values()) + tuple(
        f"scripts/{script}" for script in expected_outputs
    ) + (
        "BID_SOURCE_PARENT_SUBORDINATE_OUTPUT_CONTRACT_V001.json",
        "scripts/audit_bid_source_parent_closure_gate_v003.py",
    )
    current_root = content_root(bound_paths)

    if SEALED_EXECUTION:
        manifest_path = Path(
            globals()["__sealed_execution_context__"]["target_manifest_path"]
        ).resolve()
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        output_path = (PROJECT_ROOT / manifest["expected_output"]).resolve()
        output_path.relative_to(PROJECT_ROOT.resolve())
        payload = {
            "schema": "gravacle.bid-source-parent-regression.v003",
            "python_optimize": sys.flags.optimize,
            "known_source_parent_obligations": 18,
            "currently_blocking_obligations": len(blocking_ids),
            "content_root_sha256": current_root,
            "content_addressed_runtime_sealed": True,
            "source_parent_closure": False,
            "proof_authorized": False,
            "alpha_computed": False,
            "checks": {
                "structured_status_contradiction_rejection": True,
                "subordinate_output_contradiction_rejection": True,
                "subordinate_specific_verdict_enforcement": True,
                "subordinate_process_optimize_exact": True,
                "startup_custom_modules_absent": True,
                "all_known_obligations_retained": True,
            },
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("x", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True, allow_nan=False)
            handle.write("\n")
        print(output_path)
        print(f"python_optimize={sys.flags.optimize}")
        print("alpha_computed=FALSE")
        print("SOURCE_PARENT_CLOSURE=BLOCKED")
        print("SOURCE_PARENT_REGRESSION_GATE=PASS_SEALED")
    else:
        print("known_source_parent_obligations=18")
        print(f"currently_blocking_obligations={len(blocking_ids)}")
        print("structured_status_contradiction_rejection=PASS")
        print("subordinate_output_contradiction_rejection=PASS")
        print("subordinate_specific_verdict_enforcement=PASS")
        print(f"optimization_safe_subordinate_audits={len(expected_outputs)}")
        print("sanitized_startup_custom_modules_absent=PASS")
        print(f"unsealed_content_root_sha256={current_root}")
        print("content_addressed_isolated_runtime_manifest=NOT_YET_SEALED")
        print("complete_relativistic_source_parent_derived=FALSE")
        print("public_record_Hilbertization_given_QR1_QR7=PASS_CONDITIONAL")
        print("physical_record_Hilbertization_from_deeper_action=FALSE")
        print("physical_charge_operator_constructed_from_disclosed_Dirac_CAR_input=TRUE")
        print("one_normal_ambient_3plus1_graded_superconnection_typing_derived=TRUE")
        print("complete_CPT_CP_reduced_graded_source_parent_derived=FALSE")
        print("physical_source_mass_computed=FALSE")
        print("alpha_computed=FALSE")
        print("SOURCE_PARENT_CLOSURE=BLOCKED")
        print("SOURCE_PARENT_REGRESSION_GATE=PASS_UNSEALED")


if __name__ == "__main__":
    main()
