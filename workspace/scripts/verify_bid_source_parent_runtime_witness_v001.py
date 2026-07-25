#!/usr/bin/env python3
"""Independently verify the sealed source-parent runtime witness."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
WITNESS_MANIFEST = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_closure_v001_execution_manifest.json"
)
WITNESS_OUTPUT = (
    PROJECT_ROOT / "results" / "bid_source_parent_closure_v001_sealed.json"
)
WITNESS_RECEIPT = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_closure_v001_execution_receipt.json"
)
RUNTIME_SNAPSHOT = (
    PROJECT_ROOT / "provenance" / "primitive_step6_runtime_snapshot_v008.json"
)
SOURCE_PARENT_TARGET = ROOT / "scripts" / "audit_bid_source_parent_closure_gate_v001.py"
EXPECTED_RECEIPT_KEYS = {
    "alpha_computed",
    "blocked_audit_events",
    "child_local_output_contract_validated",
    "child_local_validators_mutable_by_target",
    "conditional_environment_mutation_policy",
    "declared_python_audit_process_network_and_mutation_policy_enforced",
    "environment_after_clear",
    "environment_cleared_before_target_imports",
    "environment_keys_before_clear",
    "exact_executed_source_buffer_sha256",
    "import_time_origin_allowlist_enforced",
    "inherited_file_descriptors_closed_before_target",
    "loaded_module_history_complete_claimed",
    "loaded_module_origins_all_sealed",
    "loaded_modules",
    "loaded_native_images",
    "local_record_is_not_remote_attestation",
    "native_environment_after_target",
    "native_environment_empty_before_target_imports",
    "native_environment_keys_before_clear",
    "native_process_network_and_mutation_resistance_claimed",
    "native_transient_environment_mutation_resistance_claimed",
    "observed_transient_environment_events",
    "open_events",
    "output_contract_sha256",
    "prelaunch_python_execution_resistance_claimed",
    "python_audit_transient_environment_sequence_enforced",
    "python_state_invocation_contract_passed",
    "record_authoritative_for_terminal_pass",
    "runtime_manifest_sha256_after",
    "runtime_manifest_sha256_before",
    "runtime_snapshot_path",
    "runtime_snapshot_sha256",
    "schema",
    "source_and_runtime_bytes_unchanged",
    "source_only_cache_prefix_enforced",
    "stage",
    "status",
    "surviving_loaded_module_identity_ledger_enforced",
    "target_manifest_files_sha256_after",
    "target_manifest_files_sha256_before",
    "target_manifest_path",
    "target_manifest_sha256_after",
    "target_manifest_sha256_before",
    "target_output",
    "target_output_sha256",
    "target_script",
    "target_source_sha256",
}
EXPECTED_OUTPUT_KEYS = {
    "alpha_computed",
    "checks",
    "content_addressed_runtime_sealed",
    "content_root_sha256",
    "currently_blocking_obligations",
    "known_source_parent_obligations",
    "proof_authorized",
    "schema",
    "source_parent_closure",
}
ALLOWED_MODULE_CLASSIFICATIONS = {
    "sealed_file",
    "sealed_originless_source",
    "sealed_interpreter_builtin",
    "sealed_interpreter_frozen",
    "sealed_parent_export_alias",
    "sealed_native_empty_runtime_module",
    "sealed_native_generated_runtime_module",
}
ALLOWED_NATIVE_CLASSIFICATIONS = {
    "sealed_file",
    "system_trust_root",
    "SIP_dyld_shared_cache_trust_root",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha(value: Any) -> str:
    data = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"duplicate JSON key: {key}")
        output[key] = value
    return output


def reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON constant: {value}")


def validate_finite(value: Any, label: str) -> None:
    if isinstance(value, float) and not math.isfinite(value):
        raise RuntimeError(f"non-finite value in {label}")
    if isinstance(value, dict):
        for key, item in value.items():
            validate_finite(item, f"{label}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            validate_finite(item, f"{label}[{index}]")


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(
        path.read_text(encoding="utf-8"),
        parse_constant=reject_constant,
        object_pairs_hook=reject_duplicate_keys,
    )
    if not isinstance(value, dict):
        raise RuntimeError(f"{path} is not a JSON object")
    validate_finite(value, str(path))
    return value


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    manifest = read_json(WITNESS_MANIFEST)
    output = read_json(WITNESS_OUTPUT)
    receipt = read_json(WITNESS_RECEIPT)

    require(
        manifest.get("schema") == "gravacle.sealed-target-execution.v002",
        "witness manifest schema mismatch",
    )
    require(
        manifest.get("stage") == "bid-source-parent-regression-gate-v001",
        "witness manifest stage mismatch",
    )
    require(manifest.get("alpha_computed") is False, "manifest lost alpha firewall")
    require(set(receipt) == EXPECTED_RECEIPT_KEYS, "receipt field inventory changed")
    require(set(output) == EXPECTED_OUTPUT_KEYS, "output field inventory changed")

    manifest_relative = str(WITNESS_MANIFEST.resolve().relative_to(PROJECT_ROOT.resolve()))
    output_relative = str(WITNESS_OUTPUT.resolve().relative_to(PROJECT_ROOT.resolve()))
    receipt_relative = str(WITNESS_RECEIPT.resolve().relative_to(PROJECT_ROOT.resolve()))
    target_relative = str(SOURCE_PARENT_TARGET.resolve().relative_to(PROJECT_ROOT.resolve()))
    runtime_relative = str(RUNTIME_SNAPSHOT.resolve().relative_to(PROJECT_ROOT.resolve()))
    manifest_sha = sha256(WITNESS_MANIFEST)
    output_sha = sha256(WITNESS_OUTPUT)
    target_sha = sha256(SOURCE_PARENT_TARGET)
    runtime_sha = sha256(RUNTIME_SNAPSHOT)

    require(manifest.get("target_script") == target_relative, "target path mismatch")
    require(manifest.get("expected_output") == output_relative, "output path mismatch")
    require(manifest.get("execution_receipt") == receipt_relative, "receipt path mismatch")
    require(manifest.get("runtime_snapshot") == runtime_relative, "runtime path mismatch")
    require(
        manifest.get("runtime_snapshot_sha256") == runtime_sha,
        "manifest runtime hash mismatch",
    )

    files = manifest.get("files")
    require(isinstance(files, dict) and bool(files), "manifest file inventory is empty")
    actual_files: dict[str, str] = {}
    for relative, expected in files.items():
        require(isinstance(relative, str), "non-string manifest path")
        require(isinstance(expected, str), "non-string manifest digest")
        path = (PROJECT_ROOT / relative).resolve()
        path.relative_to(PROJECT_ROOT.resolve())
        require(path.is_file(), f"witness input is absent: {relative}")
        actual = sha256(path)
        require(actual == expected, f"witness input changed: {relative}")
        actual_files[str(path)] = actual
    require(files.get(target_relative) == target_sha, "target is not manifest-bound")

    require(
        receipt.get("schema") == "gravacle.sealed-target-child-execution-record.v008",
        "receipt schema mismatch",
    )
    require(
        receipt.get("status") == "CHILD_LOCAL_OUTPUT_CONTRACT_VALIDATED_ALPHA_FALSE",
        "receipt status mismatch",
    )
    require(receipt.get("stage") == manifest["stage"], "receipt stage mismatch")
    require(receipt.get("runtime_snapshot_path") == runtime_relative, "receipt runtime path mismatch")
    require(receipt.get("runtime_snapshot_sha256") == runtime_sha, "receipt runtime hash mismatch")
    require(receipt.get("target_manifest_path") == manifest_relative, "receipt manifest path mismatch")
    require(
        receipt.get("target_manifest_sha256_before")
        == receipt.get("target_manifest_sha256_after")
        == manifest_sha,
        "manifest changed during witness execution",
    )
    require(receipt.get("target_script") == target_relative, "receipt target path mismatch")
    require(
        receipt.get("target_source_sha256")
        == receipt.get("exact_executed_source_buffer_sha256")
        == target_sha,
        "executed target bytes are not the manifest target bytes",
    )
    require(receipt.get("target_output") == output_relative, "receipt output path mismatch")
    require(receipt.get("target_output_sha256") == output_sha, "receipt output hash mismatch")
    require(
        receipt.get("target_manifest_files_sha256_before")
        == receipt.get("target_manifest_files_sha256_after")
        == canonical_sha(actual_files),
        "sealed input inventory changed during witness execution",
    )
    require(
        receipt.get("runtime_manifest_sha256_before")
        == receipt.get("runtime_manifest_sha256_after"),
        "runtime inventory changed during witness execution",
    )
    require(
        receipt.get("output_contract_sha256")
        == canonical_sha(manifest.get("output_contract")),
        "output-contract digest mismatch",
    )

    required_true = {
        "source_and_runtime_bytes_unchanged",
        "loaded_module_origins_all_sealed",
        "surviving_loaded_module_identity_ledger_enforced",
        "import_time_origin_allowlist_enforced",
        "source_only_cache_prefix_enforced",
        "python_state_invocation_contract_passed",
        "declared_python_audit_process_network_and_mutation_policy_enforced",
        "python_audit_transient_environment_sequence_enforced",
        "native_environment_empty_before_target_imports",
        "child_local_output_contract_validated",
        "environment_cleared_before_target_imports",
        "local_record_is_not_remote_attestation",
        "child_local_validators_mutable_by_target",
    }
    require(
        all(receipt.get(key) is True for key in required_true),
        "a required witness assurance flag is not true",
    )
    required_false = {
        "alpha_computed",
        "record_authoritative_for_terminal_pass",
        "prelaunch_python_execution_resistance_claimed",
        "loaded_module_history_complete_claimed",
        "native_process_network_and_mutation_resistance_claimed",
        "native_transient_environment_mutation_resistance_claimed",
    }
    require(
        all(receipt.get(key) is False for key in required_false),
        "a required witness limitation/firewall flag changed",
    )
    require(receipt.get("environment_after_clear") == {}, "Python environment was not empty")
    require(
        receipt.get("native_environment_after_target") == {},
        "native environment was not empty after target",
    )
    require(
        receipt.get("observed_transient_environment_events")
        == receipt.get("conditional_environment_mutation_policy"),
        "transient environment event sequence mismatch",
    )
    require(
        all(
            isinstance(descriptor, int) and descriptor > 2
            for descriptor in receipt.get("inherited_file_descriptors_closed_before_target", [])
        ),
        "invalid inherited-descriptor ledger",
    )

    modules = receipt.get("loaded_modules")
    require(isinstance(modules, list) and bool(modules), "empty loaded-module ledger")
    require(
        all(
            isinstance(row, dict)
            and row.get("classification") in ALLOWED_MODULE_CLASSIFICATIONS
            and isinstance(row.get("causal_provenance"), dict)
            for row in modules
        ),
        "unsealed or causally untracked module row",
    )
    native_images = receipt.get("loaded_native_images")
    require(isinstance(native_images, list) and bool(native_images), "empty native-image ledger")
    require(
        all(
            isinstance(row, dict)
            and row.get("classification") in ALLOWED_NATIVE_CLASSIFICATIONS
            for row in native_images
        ),
        "unsealed native-image row",
    )
    runtime_probe = np.asarray([len(modules), len(native_images)], dtype=np.int64)
    require(
        runtime_probe.shape == (2,)
        and bool(np.all(runtime_probe > 0)),
        "sealed numerical runtime probe failed",
    )
    allowed_write_paths = {str(WITNESS_OUTPUT.resolve()), str(WITNESS_RECEIPT.resolve())}
    require(
        all(
            not row.get("write_mode") or row.get("path") in allowed_write_paths
            for row in receipt.get("open_events", [])
            if isinstance(row, dict)
        ),
        "witness opened an undeclared write target",
    )

    require(output.get("schema") == "gravacle.bid-source-parent-regression.v001", "output schema mismatch")
    require(output.get("known_source_parent_obligations") == 18, "obligation count mismatch")
    require(output.get("currently_blocking_obligations") == 3, "witness blocker count mismatch")
    require(output.get("content_addressed_runtime_sealed") is True, "witness did not run sealed")
    require(output.get("source_parent_closure") is False, "witness falsely closed source parent")
    require(output.get("proof_authorized") is False, "witness authorized proof")
    require(output.get("alpha_computed") is False, "witness computed alpha")
    checks = output.get("checks")
    require(
        isinstance(checks, dict)
        and bool(checks)
        and all(value is True for value in checks.values()),
        "witness regression checks did not all pass",
    )

    result = {
        "schema": "gravacle.bid-source-parent-runtime-witness-verification.v001",
        "status": "PASS_CONTENT_ADDRESSED_SOURCE_PARENT_RUNTIME_WITNESS_ALPHA_FALSE",
        "witness_manifest_sha256": manifest_sha,
        "witness_output_sha256": output_sha,
        "witness_receipt_sha256": sha256(WITNESS_RECEIPT),
        "witness_loaded_module_count": len(modules),
        "witness_loaded_native_image_count": len(native_images),
        "source_parent_closure": False,
        "content_addressed_runtime_sealed": True,
        "proof_authorized": False,
        "alpha_computed": False,
        "checks": {
            "manifest_file_inventory_recomputed": True,
            "target_source_buffer_bound": True,
            "runtime_snapshot_bound": True,
            "output_contract_bound": True,
            "receipt_assurance_flags_exact": True,
            "module_and_native_ledgers_classified": True,
            "environment_and_write_policy_verified": True,
            "known_blockers_and_alpha_firewall_retained": True,
        },
    }
    context = globals().get("__sealed_execution_context__")
    if not isinstance(context, dict):
        raise RuntimeError("runtime witness verifier requires sealed execution")
    output_path = (
        PROJECT_ROOT
        / "results"
        / "bid_source_parent_runtime_witness_verification_v001.json"
    )
    with output_path.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")
    print(output_path)
    print("SOURCE_PARENT_RUNTIME_WITNESS=PASS")
    print("alpha_computed=false")


if __name__ == "__main__":
    main()
