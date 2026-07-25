#!/usr/bin/env python3
"""Fail-closed authority and seal audit for CURRENT_AUTHORITY_LEDGER_V010."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "CURRENT_AUTHORITY_LEDGER_V010.json"

SEALED_INPUTS = {
    "PRIMITIVE_VECTORLIKE_CHARGED_SOURCE_BRANCH_V003.md":
        "PRIMITIVE_VECTORLIKE_CHARGED_SOURCE_BRANCH_V003.seal.sha256",
    "PRIMITIVE_SOURCE_RECORD_PAIRED_RETURN_IDENTIFICATION_PRINCIPLE_V002.md":
        "PRIMITIVE_SOURCE_RECORD_PAIRED_RETURN_IDENTIFICATION_PRINCIPLE_V002.seal.sha256",
    "PRIMITIVE_SOURCE_RECORD_CHIRAL_OPERATOR_GATE_V002.md":
        "PRIMITIVE_SOURCE_RECORD_CHIRAL_OPERATOR_GATE_V002.seal.sha256",
    "scripts/audit_primitive_source_record_chiral_operator_v002.py":
        "scripts/audit_primitive_source_record_chiral_operator_v002.seal.sha256",
    "tests/test_primitive_source_record_chiral_operator_v002.py":
        "tests/test_primitive_source_record_chiral_operator_v002.seal.sha256",
    "results/primitive_source_record_chiral_operator_v002.json":
        "results/primitive_source_record_chiral_operator_v002.seal.sha256",
    "SOURCE_RECORD_CLOSURE_MAGNITUDE_NONDERIVATION_GATE_V003.md":
        "SOURCE_RECORD_CLOSURE_MAGNITUDE_NONDERIVATION_GATE_V003.seal.sha256",
    "scripts/audit_source_record_closure_magnitude_nonderivation_v003.py":
        "scripts/audit_source_record_closure_magnitude_nonderivation_v003.seal.sha256",
    "tests/test_source_record_closure_magnitude_nonderivation_v003.py":
        "tests/test_source_record_closure_magnitude_nonderivation_v003.seal.sha256",
    "results/source_record_closure_magnitude_nonderivation_v003.json":
        "results/source_record_closure_magnitude_nonderivation_v003.seal.sha256",
    "CURRENT_AUTHORITY_LEDGER_V010.json":
        "CURRENT_AUTHORITY_LEDGER_V010.seal.sha256",
    "scripts/audit_current_authority_v010.py":
        "scripts/audit_current_authority_v010.seal.sha256",
    "tests/test_current_authority_v010.py":
        "tests/test_current_authority_v010.seal.sha256"
}

EXPECTED_EXECUTION_STATE = {
    "alpha_computed": False,
    "auxiliary_compact_connection_adopted_Level_1": True,
    "binary_gap_interval_relation_is_conditional": True,
    "closure_magnitude_presently_derived": False,
    "closure_phase_presently_derived": False,
    "complete_dynamical_parent_kernel_frozen": False,
    "complete_parameter_free_Q_spec_frozen": False,
    "complete_parent_action_uniquely_derived": False,
    "complete_source_record_closure_action_uniquely_derived": False,
    "controlled_x_write_candidate_unique": False,
    "coupled_record_bundle_charge_radius_derived": False,
    "coupled_record_bundle_tree_relation_derived": True,
    "coupling_evaluation_authorized": False,
    "current_premises_admit_response_inequivalent_parent_actions": True,
    "declared_trial_potential_algebra_verified": True,
    "declared_trial_potentials_have_distinct_radial_stationary_points": True,
    "displayed_fixed_time_block_algebra_verified": True,
    "durable_record_dynamics_derived": False,
    "durable_record_generator_derived": False,
    "finite_c_F2_deformation_excluded_as_universal_theorem": False,
    "finite_c_F2_deformation_excluded_inside_adopted_primitive_branch": True,
    "finite_cell_flux_protocol_frozen": True,
    "finite_flux_response_evaluated": False,
    "free_mass_shell_relation_for_supplied_background_derived": True,
    "full_Q_spec_nonuniqueness_proved": False,
    "historical_target_blindness_established_for_trial_potentials": False,
    "interacting_source_pole_and_residue_derived": False,
    "operator_tensor_structure_derived_from_record_principles": False,
    "physical_binary_record_generator_derived": False,
    "physical_closure_stability_derived": False,
    "physical_public_EM_connection_derived": False,
    "pointwise_active_relative_U1_derived": True,
    "positive_trial_radial_second_derivatives_verified": True,
    "proof_authorized": False,
    "record_generated_free_mass_parameter_derived": False,
    "record_generated_source_mass_derived": False,
    "response_inequivalence_evaluated": False,
    "scalar_pseudoscalar_bilinear_class_declared": True,
    "smooth_principal_relative_U1_bundle_adopted_Level_1": True,
    "source_block_identified_with_complete_closure_map": False,
    "source_branch_charge_basis_corrected": True,
    "source_record_odd_component_authority_active": True,
    "source_record_odd_component_identity_adopted_Level_1": True,
    "source_record_odd_component_identity_derived": False,
    "source_record_odd_component_principle_forward_sealed": True,
    "source_record_odd_component_principle_target_blind": False,
    "source_record_odd_component_principle_target_value_free": True,
    "spectral_evaluation_authorized": False,
    "transport_only_phase_complete_principle_adopted": True,
    "transport_only_phase_complete_principle_is_derived_theorem": False,
    "two_complete_admissible_closure_actions_exhibited": False,
    "unique_causal_record_cell_derived": False,
    "unique_finite_coincident_extension_derived": False,
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def verify_seal(target_name: str, seal_name: str) -> None:
    target = ROOT / target_name
    seal = ROOT / seal_name
    require(target.exists(), f"Missing sealed target: {target_name}")
    require(seal.exists(), f"Missing seal: {seal_name}")
    fields = seal.read_text(encoding="utf-8").strip().split()
    require(len(fields) == 2, f"Malformed seal: {seal_name}")
    expected_hash = fields[0]
    actual_hash = hashlib.sha256(target.read_bytes()).hexdigest()
    require(actual_hash == expected_hash, f"Seal mismatch: {target_name}")


def validate_execution_state(state: dict[str, object]) -> None:
    expected_keys = set(EXPECTED_EXECUTION_STATE)
    actual_keys = set(state)
    missing_keys = sorted(expected_keys - actual_keys)
    unknown_keys = sorted(actual_keys - expected_keys)
    mismatches = {
        key: {
            "expected": EXPECTED_EXECUTION_STATE[key],
            "actual": state.get(key),
        }
        for key in sorted(expected_keys & actual_keys)
        if state[key] != EXPECTED_EXECUTION_STATE[key]
    }
    require(not missing_keys, f"Missing execution-state keys: {missing_keys}")
    require(not unknown_keys, f"Unknown execution-state keys: {unknown_keys}")
    require(not mismatches, f"Execution-state mismatches: {mismatches}")


def main() -> None:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    state = data["execution_state"]

    required_files = [
        *data["sealed_pre_alpha_authority"].values(),
        *data["current_derived_results"].values(),
        *data["current_level_1_postulates"].values(),
        *data["external_target_independent_route_audits"].keys(),
        *data["conditional_or_diagnostic_only"].keys(),
    ]
    missing = [name for name in required_files if not (ROOT / name).resolve().exists()]
    require(not missing, f"Missing authority inputs: {missing}")

    for target_name, seal_name in SEALED_INPUTS.items():
        verify_seal(target_name, seal_name)

    require(data["schema_version"] == 10, "Unexpected authority schema version")
    validate_execution_state(state)

    out = {
        "status": "PASS_AUTHORITY_V010_IDENTITY_SEALED_MAGNITUDE_BLOCKED",
        "missing_files": missing,
        "verified_new_seals": len(SEALED_INPUTS),
        "verified_execution_state_keys": len(EXPECTED_EXECUTION_STATE),
        "source_record_odd_component_identity_adopted_Level_1": state[
            "source_record_odd_component_identity_adopted_Level_1"
        ],
        "free_mass_shell_relation_for_supplied_background_derived": state[
            "free_mass_shell_relation_for_supplied_background_derived"
        ],
        "closure_magnitude_presently_derived": state[
            "closure_magnitude_presently_derived"
        ],
        "record_generated_source_mass_derived": state[
            "record_generated_source_mass_derived"
        ],
        "alpha_computed": state["alpha_computed"],
        "proof_authorized": state["proof_authorized"],
        "scope": "authority_and_seal_consistency_only",
    }
    result_path = ROOT / "results" / "current_authority_v010.json"
    result_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
