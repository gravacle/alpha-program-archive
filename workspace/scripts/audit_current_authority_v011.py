#!/usr/bin/env python3
"""Fail-closed delta authority audit for CURRENT_AUTHORITY_LEDGER_V011."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "CURRENT_AUTHORITY_LEDGER_V011.json"

NEW_SEALED_INPUTS = {
    "SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V002.md":
        "SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V002.seal.sha256",
    "scripts/audit_source_record_generator_structure_v002.py":
        "scripts/audit_source_record_generator_structure_v002.seal.sha256",
    "tests/test_source_record_generator_structure_v002.py":
        "tests/test_source_record_generator_structure_v002.seal.sha256",
    "results/source_record_generator_structure_v002.json":
        "results/source_record_generator_structure_v002.seal.sha256",
    "DURABLE_POINTER_CLOSURE_OPERATOR_SELECTOR_GATE_V002.md":
        "DURABLE_POINTER_CLOSURE_OPERATOR_SELECTOR_GATE_V002.seal.sha256",
    "scripts/audit_durable_pointer_closure_operator_selector_v002.py":
        "scripts/audit_durable_pointer_closure_operator_selector_v002.seal.sha256",
    "tests/test_durable_pointer_closure_operator_selector_v002.py":
        "tests/test_durable_pointer_closure_operator_selector_v002.seal.sha256",
    "results/durable_pointer_closure_operator_selector_v002.json":
        "results/durable_pointer_closure_operator_selector_v002.seal.sha256",
    "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md":
        "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.seal.sha256",
    "scripts/audit_boundary_record_onset_saturation_action_v003.py":
        "scripts/audit_boundary_record_onset_saturation_action_v003.seal.sha256",
    "tests/test_boundary_record_onset_saturation_action_v003.py":
        "tests/test_boundary_record_onset_saturation_action_v003.seal.sha256",
    "results/boundary_record_onset_saturation_action_v003.json":
        "results/boundary_record_onset_saturation_action_v003.seal.sha256",
    "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md":
        "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.seal.sha256",
    "scripts/audit_source_flux_conditioned_record_write_v003.py":
        "scripts/audit_source_flux_conditioned_record_write_v003.seal.sha256",
    "tests/test_source_flux_conditioned_record_write_v003.py":
        "tests/test_source_flux_conditioned_record_write_v003.seal.sha256",
    "results/source_flux_conditioned_record_write_v003.json":
        "results/source_flux_conditioned_record_write_v003.seal.sha256",
}

EXPECTED_ADDITIONS = {
    "coherent_flux_superposition_physically_admissible_derived": False,
    "combined_grading_conservation_derived": False,
    "common_source_term_excluded": False,
    "complete_physical_write_operator_derived": False,
    "complete_source_record_environment_operator_derived": False,
    "conditional_pointer_commutant_classified": True,
    "conditional_source_flux_holonomy_verified": True,
    "nonzero_source_record_exchange_derived": False,
    "orthogonal_reduced_record_supports_derived": False,
    "physical_contrast_normalization_derived": False,
    "physical_dynamical_action_fixed": False,
    "physical_durability_derived": False,
    "physical_pointer_operator_selected": False,
    "physical_source_flux_nondemolition_derived": False,
    "reduced_source_record_generator_structure_classified": True,
    "relative_onset_saturation_adopted_Level_1": True,
    "relative_orthogonalization_bound_derived": True,
    "source_relative_phase_observability_derived": False,
}

EXPECTED_PROTECTED = {
    "alpha_computed": False,
    "complete_parameter_free_Q_spec_frozen": False,
    "complete_source_record_closure_action_uniquely_derived": False,
    "coupling_evaluation_authorized": False,
    "proof_authorized": False,
    "record_generated_source_mass_derived": False,
    "spectral_evaluation_authorized": False,
    "unique_causal_record_cell_derived": False,
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
    require(fields[1] == target.name, f"Seal target-name mismatch: {seal_name}")
    actual_hash = hashlib.sha256(target.read_bytes()).hexdigest()
    require(actual_hash == fields[0], f"Seal mismatch: {target_name}")


def validate_exact_map(actual: dict[str, object], expected: dict[str, object], label: str) -> None:
    require(set(actual) == set(expected), f"{label} key drift")
    mismatches = {
        key: {"expected": expected[key], "actual": actual[key]}
        for key in sorted(expected)
        if actual[key] != expected[key]
    }
    require(not mismatches, f"{label} mismatches: {mismatches}")


def build_result(data: dict[str, object] | None = None) -> dict[str, object]:
    if data is None:
        data = json.loads(LEDGER.read_text(encoding="utf-8"))
    require(data["schema_version"] == 11, "Unexpected authority schema version")
    validate_exact_map(
        data["execution_state_additions"],
        EXPECTED_ADDITIONS,
        "execution-state additions",
    )
    validate_exact_map(
        data["protected_parent_flags"],
        EXPECTED_PROTECTED,
        "protected parent flags",
    )

    parent_info = data["parent_authority"]
    required_parent_keys = {
        "ledger", "ledger_seal", "audit", "audit_seal",
        "test", "test_seal", "result", "result_seal",
    }
    require(set(parent_info) == required_parent_keys, "Parent authority schema drift")
    verify_seal(parent_info["ledger"], parent_info["ledger_seal"])
    verify_seal(parent_info["audit"], parent_info["audit_seal"])
    verify_seal(parent_info["test"], parent_info["test_seal"])
    verify_seal(parent_info["result"], parent_info["result_seal"])

    parent = json.loads((ROOT / parent_info["ledger"]).read_text(encoding="utf-8"))
    require(parent["schema_version"] == 10, "Unexpected parent schema")
    parent_state = parent["execution_state"]
    for key, expected in EXPECTED_PROTECTED.items():
        require(parent_state.get(key) == expected, f"Protected parent flag changed: {key}")

    overlap = set(parent_state) & set(EXPECTED_ADDITIONS)
    require(not overlap, f"V011 additions collide with parent keys: {sorted(overlap)}")
    effective_state = {**parent_state, **EXPECTED_ADDITIONS}
    for key, expected in EXPECTED_PROTECTED.items():
        require(effective_state[key] == expected, f"Effective protected flag changed: {key}")

    for target_name, seal_name in NEW_SEALED_INPUTS.items():
        verify_seal(target_name, seal_name)

    required_files = [
        *data["new_sealed_results"].values(),
        *data["new_level_1_postulates"].values(),
        *data["superseded_or_rejected_since_v010"].keys(),
    ]
    missing = [name for name in required_files if not (ROOT / name).exists()]
    require(not missing, f"Missing V011 authority inputs: {missing}")

    return {
        "status": "PASS_AUTHORITY_V011_CONDITIONAL_OPERATOR_PROGRESS_ALPHA_BLOCKED",
        "parent_schema_version": parent["schema_version"],
        "verified_new_seals": len(NEW_SEALED_INPUTS),
        "verified_parent_seals": 4,
        "verified_effective_execution_state_keys": len(effective_state),
        "conditional_pointer_commutant_classified": effective_state[
            "conditional_pointer_commutant_classified"
        ],
        "relative_orthogonalization_bound_derived": effective_state[
            "relative_orthogonalization_bound_derived"
        ],
        "conditional_source_flux_holonomy_verified": effective_state[
            "conditional_source_flux_holonomy_verified"
        ],
        "complete_source_record_environment_operator_derived": effective_state[
            "complete_source_record_environment_operator_derived"
        ],
        "alpha_computed": effective_state["alpha_computed"],
        "proof_authorized": effective_state["proof_authorized"],
        "scope": "sealed_delta_authority_and_no_promotion_only",
    }


def main() -> None:
    out = build_result()
    result_path = ROOT / "results" / "current_authority_v011.json"
    result_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
