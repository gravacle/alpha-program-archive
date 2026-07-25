#!/usr/bin/env python3
"""Independent verifier for fresh normal and optimized producer children."""

from __future__ import annotations

import hashlib
import json
import math
import os
from pathlib import Path
import sys
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
PARENT_SCRIPTS = PROJECT_ROOT / "scripts"
if str(PARENT_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(PARENT_SCRIPTS))

from validate_content_addressed_runtime_evidence_v013 import (  # noqa: E402
    allowed_runtime_files,
    validate_originless_alias_negative_controls,
    validate_loaded_modules,
    validate_loaded_native_images,
    validate_open_events,
    validate_output_against_contract,
)


RUNTIME = PROJECT_ROOT / "provenance" / "primitive_step6_runtime_snapshot_v013.json"
NORMAL_MANIFEST = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_producer_normal_v004_execution_manifest.json"
)
OPTIMIZED_MANIFEST = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_producer_optimized_v004_execution_manifest.json"
)
OUTPUT = (
    PROJECT_ROOT / "results" / "bid_source_parent_terminal_children_verifier_v004.json"
)
RECEIPT_KEYS = {
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
    "python_optimize",
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
EXPECTED_TRANSIENT_EVENTS = [
    {"event": "os.putenv", "key": "OPENBLAS_MAIN_FREE", "value": "1"},
    {"event": "os.putenv", "key": "GOTOBLAS_MAIN_FREE", "value": "1"},
    {"event": "os.unsetenv", "key": "OPENBLAS_MAIN_FREE", "value": None},
    {"event": "os.unsetenv", "key": "GOTOBLAS_MAIN_FREE", "value": None},
]


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


def validate_finite(value: Any, label: str) -> None:
    if isinstance(value, float) and not math.isfinite(value):
        raise RuntimeError(f"non-finite value at {label}")
    if isinstance(value, dict):
        for key, item in value.items():
            validate_finite(item, f"{label}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            validate_finite(item, f"{label}[{index}]")


def strict_json(path: Path) -> dict[str, Any]:
    value = json.loads(
        path.read_text(encoding="utf-8"),
        parse_constant=lambda value: (_ for _ in ()).throw(
            ValueError(f"non-finite JSON constant: {value}")
        ),
        object_pairs_hook=reject_duplicate_keys,
    )
    if not isinstance(value, dict):
        raise RuntimeError(f"{path} is not a JSON object")
    validate_finite(value, str(path))
    return value


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(PROJECT_ROOT.resolve()))


def validate_child(
    manifest_path: Path, expected_optimize: int
) -> tuple[dict[str, Any], dict[str, str]]:
    manifest = strict_json(manifest_path)
    require(
        manifest.get("schema") == "gravacle.sealed-target-execution.v002",
        "producer manifest schema mismatch",
    )
    require(
        manifest.get("python_optimize") == expected_optimize,
        "producer manifest optimization mismatch",
    )
    require(manifest.get("alpha_computed") is False, "producer manifest lost alpha firewall")
    files = manifest.get("files")
    require(isinstance(files, dict) and bool(files), "producer manifest file inventory is empty")
    current_files: dict[str, str] = {}
    for name, expected in files.items():
        require(isinstance(name, str) and isinstance(expected, str), "malformed file row")
        path = (PROJECT_ROOT / name).resolve()
        path.relative_to(PROJECT_ROOT.resolve())
        require(path.is_file(), f"producer input absent: {name}")
        actual = sha256(path)
        require(actual == expected, f"producer input changed: {name}")
        current_files[str(path)] = actual

    target = (PROJECT_ROOT / str(manifest["target_script"])).resolve()
    output_path = (PROJECT_ROOT / str(manifest["expected_output"])).resolve()
    receipt_path = (PROJECT_ROOT / str(manifest["execution_receipt"])).resolve()
    require(files.get(relative(target)) == sha256(target), "producer target is not bound")
    output = strict_json(output_path)
    validate_output_against_contract(output, manifest["output_contract"])
    require(output.get("python_optimize") == expected_optimize, "producer output optimize mismatch")
    require(
        output.get("currently_blocking_obligations") == 3
        and output.get("source_parent_closure") is False
        and output.get("proof_authorized") is False
        and output.get("alpha_computed") is False,
        "producer authority/blocker state changed",
    )

    receipt = strict_json(receipt_path)
    require(set(receipt) == RECEIPT_KEYS, "producer receipt field inventory changed")
    runtime = strict_json(RUNTIME)
    runtime_allowed = allowed_runtime_files(runtime)
    all_allowed = dict(runtime_allowed)
    all_allowed.update(current_files)
    all_allowed[str(RUNTIME.resolve())] = sha256(RUNTIME)
    all_allowed[str(manifest_path.resolve())] = sha256(manifest_path)
    expected_values = {
        "schema": "gravacle.sealed-target-child-execution-record.v013",
        "status": "CHILD_LOCAL_OUTPUT_CONTRACT_VALIDATED_ALPHA_FALSE",
        "stage": manifest["stage"],
        "python_optimize": expected_optimize,
        "runtime_snapshot_path": relative(RUNTIME),
        "runtime_snapshot_sha256": sha256(RUNTIME),
        "target_manifest_path": relative(manifest_path),
        "target_manifest_sha256_before": sha256(manifest_path),
        "target_manifest_sha256_after": sha256(manifest_path),
        "target_script": relative(target),
        "target_source_sha256": sha256(target),
        "exact_executed_source_buffer_sha256": sha256(target),
        "target_output": relative(output_path),
        "target_output_sha256": sha256(output_path),
        "target_manifest_files_sha256_before": canonical_sha(current_files),
        "target_manifest_files_sha256_after": canonical_sha(current_files),
        "source_and_runtime_bytes_unchanged": True,
        "loaded_module_origins_all_sealed": True,
        "surviving_loaded_module_identity_ledger_enforced": True,
        "loaded_module_history_complete_claimed": False,
        "import_time_origin_allowlist_enforced": True,
        "source_only_cache_prefix_enforced": True,
        "python_state_invocation_contract_passed": True,
        "prelaunch_python_execution_resistance_claimed": False,
        "declared_python_audit_process_network_and_mutation_policy_enforced": True,
        "native_process_network_and_mutation_resistance_claimed": False,
        "conditional_environment_mutation_policy": EXPECTED_TRANSIENT_EVENTS,
        "observed_transient_environment_events": EXPECTED_TRANSIENT_EVENTS,
        "python_audit_transient_environment_sequence_enforced": True,
        "native_transient_environment_mutation_resistance_claimed": False,
        "native_environment_empty_before_target_imports": True,
        "native_environment_after_target": {},
        "child_local_output_contract_validated": True,
        "output_contract_sha256": canonical_sha(manifest["output_contract"]),
        "child_local_validators_mutable_by_target": True,
        "record_authoritative_for_terminal_pass": False,
        "local_record_is_not_remote_attestation": True,
        "environment_cleared_before_target_imports": True,
        "environment_after_clear": {},
        "alpha_computed": False,
    }
    failed = [
        key for key, expected in expected_values.items() if receipt.get(key) != expected
    ]
    require(
        receipt.get("runtime_manifest_sha256_before")
        == receipt.get("runtime_manifest_sha256_after"),
        "runtime changed during producer child",
    )
    require(
        isinstance(receipt.get("environment_keys_before_clear"), list)
        and receipt["environment_keys_before_clear"]
        == sorted(set(receipt["environment_keys_before_clear"])),
        "Python environment-key ledger malformed",
    )
    require(
        isinstance(receipt.get("native_environment_keys_before_clear"), list)
        and receipt["native_environment_keys_before_clear"]
        == sorted(set(receipt["native_environment_keys_before_clear"])),
        "native environment-key ledger malformed",
    )
    descriptors = receipt.get("inherited_file_descriptors_closed_before_target")
    require(
        isinstance(descriptors, list)
        and all(type(value) is int and value > 2 for value in descriptors)
        and descriptors == sorted(set(descriptors)),
        "inherited descriptor ledger malformed",
    )
    if failed:
        raise RuntimeError(f"producer receipt binding failed: {sorted(failed)}")
    validate_loaded_modules(receipt.get("loaded_modules"), all_allowed)
    validate_originless_alias_negative_controls(
        receipt["loaded_modules"], all_allowed
    )
    validate_loaded_native_images(receipt.get("loaded_native_images"), runtime_allowed)
    validate_open_events(
        receipt.get("open_events"),
        all_allowed,
        output_path,
        receipt_path,
        Path(str(runtime["source_only_pycache_root"])),
    )
    probe = np.asarray(
        [len(receipt["loaded_modules"]), len(receipt["loaded_native_images"])],
        dtype=np.int64,
    )
    require(bool(np.all(probe > 0)), "numerical runtime provenance probe failed")
    digests = {
        "manifest": sha256(manifest_path),
        "output": sha256(output_path),
        "receipt": sha256(receipt_path),
    }
    return output, digests


def main() -> None:
    context = globals().get("__sealed_execution_context__")
    require(isinstance(context, dict), "terminal child verifier requires sealed execution")
    normal, normal_hashes = validate_child(NORMAL_MANIFEST, 0)
    optimized, optimized_hashes = validate_child(OPTIMIZED_MANIFEST, 1)
    normal_comparable = dict(normal)
    optimized_comparable = dict(optimized)
    normal_comparable.pop("python_optimize")
    optimized_comparable.pop("python_optimize")
    require(
        normal_comparable == optimized_comparable,
        "normal and optimized producer outputs differ",
    )

    result = {
        "schema": "gravacle.bid-source-parent-terminal-child-verifier.v004",
        "status": "PASS_INDEPENDENT_NORMAL_OPTIMIZED_CHILD_VALIDATION_ALPHA_FALSE",
        "normal_manifest_sha256": normal_hashes["manifest"],
        "normal_output_sha256": normal_hashes["output"],
        "normal_receipt_sha256": normal_hashes["receipt"],
        "optimized_manifest_sha256": optimized_hashes["manifest"],
        "optimized_output_sha256": optimized_hashes["output"],
        "optimized_receipt_sha256": optimized_hashes["receipt"],
        "source_parent_closure": False,
        "proof_authorized": False,
        "alpha_computed": False,
        "checks": {
            "normal_artifact_chain_independently_validated": True,
            "optimized_artifact_chain_independently_validated": True,
            "process_optimize_levels_distinct_and_exact": True,
            "producer_outputs_equal_excluding_process_level": True,
            "module_rows_rederived": True,
            "native_rows_rederived": True,
            "open_events_rederived": True,
            "originless_alias_negative_controls": True,
            "runtime_scope_retained": True,
            "known_blockers_retained": True,
            "authority_firewall_retained": True,
        },
    }
    with OUTPUT.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")
    print(OUTPUT)
    print("TERMINAL_CHILD_VERIFIER=PASS")
    print("alpha_computed=false")


if __name__ == "__main__":
    main()
