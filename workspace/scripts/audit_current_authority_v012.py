#!/usr/bin/env python3
"""Hardened fail-closed delta audit for CURRENT_AUTHORITY_LEDGER_V012."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_TOP_LEVEL_KEYS = {
    "schema_version",
    "parent_authority",
    "new_sealed_results",
    "new_level_1_postulates",
    "superseded_or_rejected_since_v010",
    "execution_state_additions",
    "protected_parent_flags",
}

EXPECTED_PARENT_AUTHORITY = {
    "ledger": "CURRENT_AUTHORITY_LEDGER_V010.json",
    "ledger_seal": "CURRENT_AUTHORITY_LEDGER_V010.seal.sha256",
    "audit": "scripts/audit_current_authority_v010.py",
    "audit_seal": "scripts/audit_current_authority_v010.seal.sha256",
    "test": "tests/test_current_authority_v010.py",
    "test_seal": "tests/test_current_authority_v010.seal.sha256",
    "result": "results/current_authority_v010.json",
    "result_seal": "results/current_authority_v010.seal.sha256",
}

EXPECTED_NEW_SEALED_RESULTS = {
    "reduced_source_record_generator_structure":
        "SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V002.md",
    "conditional_pointer_commutant":
        "DURABLE_POINTER_CLOSURE_OPERATOR_SELECTOR_GATE_V002.md",
    "relative_record_orthogonalization_budget":
        "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md",
    "conditional_source_flux_record_holonomy":
        "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md",
}

EXPECTED_NEW_LEVEL_1_POSTULATES = {
    "relative_record_onset_saturation":
        "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md",
    "zero_flux_no_charged_write":
        "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md",
}

EXPECTED_SUPERSEDED = {
    "SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V001.md":
        "SUPERSEDED_UNCOMPUTED_KERNEL_DIMENSIONS_AND_OVERCLAIMED_NONZERO_EXCHANGE",
    "DURABLE_POINTER_CLOSURE_OPERATOR_SELECTOR_GATE_V001.md":
        "REJECTED_IDENTITY_QUOTIENT_LEAKED_INTO_SOURCE_ACTION",
    "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V001.md":
        "REJECTED_PRIVILEGED_STATIONARY_BRANCH",
    "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V002.md":
        "REJECTED_COMMON_HAMILTONIAN_AND_PHYSICAL_ACTION_OVERCLAIMS",
    "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V001.md":
        "REJECTED_GLOBAL_PHASE_AS_PHYSICAL_RELATIVE_PHASE",
    "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V002.md":
        "SUPERSEDED_UNNORMALIZED_AND_UNQUALIFIED_PHASE_OBSERVABILITY",
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

EXPECTED_PARENT_RESULT = {
    "status": "PASS_AUTHORITY_V010_IDENTITY_SEALED_MAGNITUDE_BLOCKED",
    "missing_files": [],
    "verified_new_seals": 13,
    "verified_execution_state_keys": 53,
    "source_record_odd_component_identity_adopted_Level_1": True,
    "free_mass_shell_relation_for_supplied_background_derived": True,
    "closure_magnitude_presently_derived": False,
    "record_generated_source_mass_derived": False,
    "alpha_computed": False,
    "proof_authorized": False,
    "scope": "authority_and_seal_consistency_only",
}

RESULT_SCHEMA = {
    "status": str,
    "schema_version": int,
    "parent_schema_version": int,
    "parent_status": str,
    "verified_new_seals": int,
    "verified_parent_seals": int,
    "verified_effective_execution_state_keys": int,
    "verified_delta_addition_keys": int,
    "verified_protected_parent_flags": int,
    "verified_new_result_entries": int,
    "verified_new_level_1_postulates": int,
    "verified_superseded_entries": int,
    "conditional_pointer_commutant_classified": bool,
    "relative_orthogonalization_bound_derived": bool,
    "conditional_source_flux_holonomy_verified": bool,
    "complete_source_record_environment_operator_derived": bool,
    "alpha_computed": bool,
    "proof_authorized": bool,
    "scope": str,
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return (
            set(left) == set(right)
            and all(strict_equal(left[key], right[key]) for key in left)
        )
    if isinstance(left, list):
        return (
            len(left) == len(right)
            and all(strict_equal(a, b) for a, b in zip(left, right))
        )
    return left == right


def reject_duplicate_object_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in out, f"Duplicate JSON key: {key}")
        out[key] = value
    return out


def loads_strict(text: str) -> Any:
    return json.loads(text, object_pairs_hook=reject_duplicate_object_keys)


def load_json_file(path: Path, label: str) -> dict[str, Any]:
    try:
        value = loads_strict(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError(f"Unable to load {label}: {error}") from error
    require(type(value) is dict, f"{label} is not a JSON object")
    return value


def validate_exact_map(
    actual: dict[str, Any],
    expected: dict[str, Any],
    label: str,
) -> None:
    require(type(actual) is dict, f"{label} is not an object")
    require(set(actual) == set(expected), f"{label} key drift")
    mismatches = {
        key: {"expected": expected[key], "actual": actual[key]}
        for key in sorted(expected)
        if not strict_equal(actual[key], expected[key])
    }
    require(not mismatches, f"{label} mismatches: {mismatches}")


def confined_regular_file(name: str, label: str) -> Path:
    require(type(name) is str and bool(name), f"{label} path is not a nonempty string")
    relative = Path(name)
    require(not relative.is_absolute(), f"{label} path is absolute")
    require(".." not in relative.parts, f"{label} path escapes with '..'")
    require(relative.parts not in ((), (".",)), f"{label} path is empty")

    try:
        root_resolved = ROOT.resolve(strict=True)
    except OSError as error:
        raise RuntimeError(f"Unable to resolve authority root: {error}") from error
    require(not ROOT.is_symlink(), "Authority root is a symlink")

    cursor = ROOT
    for part in relative.parts:
        cursor = cursor / part
        require(not cursor.is_symlink(), f"{label} contains a symlink: {name}")

    try:
        resolved = cursor.resolve(strict=True)
    except OSError as error:
        raise RuntimeError(f"Missing {label}: {name}") from error
    try:
        resolved.relative_to(root_resolved)
    except ValueError as error:
        raise RuntimeError(f"{label} escapes authority root: {name}") from error
    require(resolved.is_file(), f"{label} is not a regular file: {name}")
    return resolved


def verify_seal(target_name: str, seal_name: str) -> None:
    target = confined_regular_file(target_name, "sealed target")
    seal = confined_regular_file(seal_name, "seal")
    require(target != seal, f"Seal aliases its target: {target_name}")
    try:
        fields = seal.read_text(encoding="utf-8").strip().split()
    except OSError as error:
        raise RuntimeError(f"Unable to read seal: {seal_name}") from error
    require(len(fields) == 2, f"Malformed seal: {seal_name}")
    digest, recorded_name = fields
    require(len(digest) == 64, f"Malformed SHA256 digest: {seal_name}")
    require(all(character in "0123456789abcdef" for character in digest),
            f"Non-hex SHA256 digest: {seal_name}")
    require(recorded_name == Path(target_name).name,
            f"Seal target-name mismatch: {seal_name}")
    actual_hash = hashlib.sha256(target.read_bytes()).hexdigest()
    require(actual_hash == digest, f"Seal mismatch: {target_name}")


def validate_result_schema(result: dict[str, Any]) -> None:
    require(type(result) is dict, "V012 result is not an object")
    require(set(result) == set(RESULT_SCHEMA), "V012 result schema drift")
    bad_types = {
        key: {
            "expected": RESULT_SCHEMA[key].__name__,
            "actual": type(result[key]).__name__,
        }
        for key in RESULT_SCHEMA
        if type(result[key]) is not RESULT_SCHEMA[key]
    }
    require(not bad_types, f"V012 result type drift: {bad_types}")


def validate_result_parity(
    stored: dict[str, Any],
    computed: dict[str, Any],
) -> None:
    validate_result_schema(stored)
    validate_result_schema(computed)
    require(strict_equal(stored, computed), "Stored V012 result parity failure")


def build_result(data: dict[str, Any] | None = None) -> dict[str, Any]:
    if data is None:
        ledger_path = confined_regular_file(
            "CURRENT_AUTHORITY_LEDGER_V012.json", "V012 ledger"
        )
        data = load_json_file(ledger_path, "V012 ledger")
    require(type(data) is dict, "V012 ledger is not an object")
    require(set(data) == EXPECTED_TOP_LEVEL_KEYS, "V012 top-level schema drift")
    require(type(data["schema_version"]) is int, "V012 schema version is not an integer")
    require(data["schema_version"] == 12, "Unexpected authority schema version")

    validate_exact_map(data["parent_authority"], EXPECTED_PARENT_AUTHORITY,
                       "parent authority")
    validate_exact_map(data["new_sealed_results"], EXPECTED_NEW_SEALED_RESULTS,
                       "new sealed results")
    validate_exact_map(data["new_level_1_postulates"], EXPECTED_NEW_LEVEL_1_POSTULATES,
                       "new Level-1 postulates")
    validate_exact_map(data["superseded_or_rejected_since_v010"], EXPECTED_SUPERSEDED,
                       "superseded/rejected map")
    validate_exact_map(data["execution_state_additions"], EXPECTED_ADDITIONS,
                       "execution-state additions")
    validate_exact_map(data["protected_parent_flags"], EXPECTED_PROTECTED,
                       "protected parent flags")

    require(len(set(EXPECTED_PARENT_AUTHORITY.values())) == 8,
            "Parent authority roles are not path-distinct")
    for role in ("ledger", "audit", "test", "result"):
        verify_seal(
            EXPECTED_PARENT_AUTHORITY[role],
            EXPECTED_PARENT_AUTHORITY[f"{role}_seal"],
        )

    parent_ledger_path = confined_regular_file(
        EXPECTED_PARENT_AUTHORITY["ledger"], "parent ledger"
    )
    parent_result_path = confined_regular_file(
        EXPECTED_PARENT_AUTHORITY["result"], "parent result"
    )
    parent = load_json_file(parent_ledger_path, "V010 parent ledger")
    parent_result = load_json_file(parent_result_path, "V010 parent result")
    require(type(parent.get("schema_version")) is int, "Parent schema is not an integer")
    require(parent["schema_version"] == 10, "Unexpected parent schema")
    validate_exact_map(parent_result, EXPECTED_PARENT_RESULT, "parent result")

    parent_state = parent.get("execution_state")
    require(type(parent_state) is dict, "Parent execution state is not an object")
    require(len(parent_state) == 53, "Unexpected parent execution-state size")
    require(all(type(value) is bool for value in parent_state.values()),
            "Parent execution state contains non-boolean values")
    require(parent_result["verified_execution_state_keys"] == len(parent_state),
            "Parent result/state key-count mismatch")
    for key, expected in EXPECTED_PROTECTED.items():
        require(key in parent_state, f"Missing protected parent flag: {key}")
        require(type(parent_state[key]) is bool,
                f"Protected parent flag is not boolean: {key}")
        require(parent_state[key] is expected,
                f"Protected parent flag changed: {key}")

    overlap = set(parent_state) & set(EXPECTED_ADDITIONS)
    require(not overlap, f"V012 additions collide with parent keys: {sorted(overlap)}")
    effective_state = {**parent_state, **EXPECTED_ADDITIONS}
    require(all(type(value) is bool for value in effective_state.values()),
            "Effective execution state contains non-boolean values")
    for key, expected in EXPECTED_PROTECTED.items():
        require(effective_state[key] is expected,
                f"Effective protected flag changed: {key}")

    for target_name, seal_name in NEW_SEALED_INPUTS.items():
        verify_seal(target_name, seal_name)
    for name in EXPECTED_NEW_SEALED_RESULTS.values():
        require(name in NEW_SEALED_INPUTS,
                f"New result lacks a verified seal binding: {name}")
    for name in EXPECTED_NEW_LEVEL_1_POSTULATES.values():
        require(name in NEW_SEALED_INPUTS,
                f"Level-1 postulate lacks a verified seal binding: {name}")
    for name in EXPECTED_SUPERSEDED:
        confined_regular_file(name, "superseded/rejected artifact")

    out: dict[str, Any] = {
        "status": "PASS_AUTHORITY_V012_HARDENED_DELTA_ALPHA_BLOCKED",
        "schema_version": 12,
        "parent_schema_version": parent["schema_version"],
        "parent_status": parent_result["status"],
        "verified_new_seals": len(NEW_SEALED_INPUTS),
        "verified_parent_seals": 4,
        "verified_effective_execution_state_keys": len(effective_state),
        "verified_delta_addition_keys": len(EXPECTED_ADDITIONS),
        "verified_protected_parent_flags": len(EXPECTED_PROTECTED),
        "verified_new_result_entries": len(EXPECTED_NEW_SEALED_RESULTS),
        "verified_new_level_1_postulates": len(EXPECTED_NEW_LEVEL_1_POSTULATES),
        "verified_superseded_entries": len(EXPECTED_SUPERSEDED),
        "conditional_pointer_commutant_classified":
            effective_state["conditional_pointer_commutant_classified"],
        "relative_orthogonalization_bound_derived":
            effective_state["relative_orthogonalization_bound_derived"],
        "conditional_source_flux_holonomy_verified":
            effective_state["conditional_source_flux_holonomy_verified"],
        "complete_source_record_environment_operator_derived":
            effective_state["complete_source_record_environment_operator_derived"],
        "alpha_computed": effective_state["alpha_computed"],
        "proof_authorized": effective_state["proof_authorized"],
        "scope": "hardened_sealed_delta_authority_and_no_promotion_only",
    }
    validate_result_schema(out)
    require(out["alpha_computed"] is False, "Alpha was promoted")
    require(out["proof_authorized"] is False, "Proof was authorized")
    return out


def main() -> None:
    out = build_result()
    stored_result_path = confined_regular_file(
        "results/current_authority_v012.json", "stored V012 result"
    )
    stored = load_json_file(stored_result_path, "stored V012 result")
    validate_result_parity(stored, out)
    print(out["status"])


if __name__ == "__main__":
    main()
