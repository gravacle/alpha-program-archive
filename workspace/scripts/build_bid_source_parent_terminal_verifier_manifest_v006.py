#!/usr/bin/env python3
"""Freeze the independent verifier after parent validation of both producers."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
RUNTIME = PROJECT_ROOT / "provenance" / "primitive_step6_runtime_snapshot_v014.json"
TARGET = ROOT / "scripts" / "verify_bid_source_parent_terminal_children_v006.py"
OUTPUT = PROJECT_ROOT / "results" / "bid_source_parent_terminal_children_verifier_v006.json"
RECEIPT = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_children_verifier_v006_execution_receipt.json"
)
MANIFEST = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_children_verifier_v006_execution_manifest.json"
)
NORMAL_MANIFEST = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_producer_normal_v006_execution_manifest.json"
)
NORMAL_OUTPUT = (
    PROJECT_ROOT / "results" / "bid_source_parent_terminal_producer_normal_v006.json"
)
NORMAL_RECEIPT = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_producer_normal_v006_execution_receipt.json"
)
OPTIMIZED_MANIFEST = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_producer_optimized_v006_execution_manifest.json"
)
OPTIMIZED_OUTPUT = (
    PROJECT_ROOT / "results" / "bid_source_parent_terminal_producer_optimized_v006.json"
)
OPTIMIZED_RECEIPT = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_producer_optimized_v006_execution_receipt.json"
)
V003_FAILURE_RECORD = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_sp14_terminal_v003_failure_record.json"
)
V003_FAILURE_SEAL = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_sp14_terminal_v003_failure_record.seal.sha256"
)
V003_FAILURE_RECORD_SHA256 = (
    "4195917299558acd17b5c94c64d8e1b33a440d7c32db578a143b9319c07407c6"
)
V003_FAILURE_SEAL_SHA256 = (
    "1465596364b659f6bfaf86f1501441669cdf03ab1de2c78e628d961a8557f627"
)
V005_FAILURE_RECORD = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_sp14_terminal_v005_failure_record.json"
)
V005_FAILURE_SEAL = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_sp14_terminal_v005_failure_record.seal.sha256"
)
V005_FAILURE_RECORD_SHA256 = (
    "16b92ed10af821a5a740cbaf9b8280a97066fe93e59ec4b54166e989e5dcda42"
)
V005_FAILURE_SEAL_SHA256 = (
    "262b208893c07caaa6d65a383364b3b1b435c962c78420024dfda50654b79008"
)
VERIFIER_CHECKS = (
    "normal_artifact_chain_independently_validated",
    "optimized_artifact_chain_independently_validated",
    "process_optimize_levels_distinct_and_exact",
    "producer_outputs_equal_excluding_process_level",
    "module_rows_rederived",
    "native_rows_rederived",
    "open_events_rederived",
    "originless_alias_negative_controls",
    "preserved_failure_lineage_validated",
    "runtime_scope_retained",
    "known_blockers_retained",
    "authority_firewall_retained",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(PROJECT_ROOT.resolve()))


def preserved_failure_lineage() -> dict[str, dict[str, str]]:
    return {
        "v003": {
            "record": relative(V003_FAILURE_RECORD),
            "record_sha256": V003_FAILURE_RECORD_SHA256,
            "seal": relative(V003_FAILURE_SEAL),
            "seal_sha256": V003_FAILURE_SEAL_SHA256,
        },
        "v005": {
            "record": relative(V005_FAILURE_RECORD),
            "record_sha256": V005_FAILURE_RECORD_SHA256,
            "seal": relative(V005_FAILURE_SEAL),
            "seal_sha256": V005_FAILURE_SEAL_SHA256,
        },
    }


def build_manifest_payload(
    files: dict[str, str],
    exact: dict[str, object],
    checks: list[str],
) -> dict[str, object]:
    return {
        "schema": "gravacle.sealed-target-execution.v002",
        "stage": "bid-source-parent-terminal-independent-verifier-v006",
        "python_optimize": 0,
        "alpha_computed": False,
        "runtime_snapshot": relative(RUNTIME),
        "runtime_snapshot_sha256": sha256(RUNTIME),
        "target_script": relative(TARGET),
        "expected_output": relative(OUTPUT),
        "execution_receipt": relative(RECEIPT),
        "files": files,
        "preserved_failure_lineage": preserved_failure_lineage(),
        "producer_semantics_parent_validated_before_manifest": True,
        "output_contract": {
            "required_fields": list(exact) + ["checks"],
            "exact_values": exact,
            "required_check_keys": checks,
        },
    }


def build_exact_output_contract(
    normal_hashes: dict[str, str],
    optimized_hashes: dict[str, str],
) -> dict[str, object]:
    return {
        "schema": "gravacle.bid-source-parent-terminal-child-verifier.v006",
        "status": "PASS_INDEPENDENT_NORMAL_OPTIMIZED_CHILD_VALIDATION_ALPHA_FALSE",
        **normal_hashes,
        **optimized_hashes,
        "preserved_v003_failure_record_sha256": V003_FAILURE_RECORD_SHA256,
        "preserved_v003_failure_seal_sha256": V003_FAILURE_SEAL_SHA256,
        "preserved_v005_failure_record_sha256": V005_FAILURE_RECORD_SHA256,
        "preserved_v005_failure_seal_sha256": V005_FAILURE_SEAL_SHA256,
        "source_parent_closure": False,
        "proof_authorized": False,
        "alpha_computed": False,
    }


def main() -> None:
    builder = Path(__file__).resolve()
    producer_builder = (
        ROOT / "scripts" / "build_bid_source_parent_terminal_producer_manifests_v006.py"
    )
    supervisor = ROOT / "scripts" / "run_bid_source_parent_terminal_supervisor_v006.py"
    generic_validation = (
        PROJECT_ROOT
        / "scripts"
        / "validate_content_addressed_runtime_evidence_v014.py"
    )
    launcher = PROJECT_ROOT / "scripts" / "launch_content_addressed_runtime_script_v014.py"
    runtime_builder = (
        PROJECT_ROOT / "scripts" / "build_primitive_step6_runtime_snapshot_v014.py"
    )
    runtime_gate = PROJECT_ROOT / "primitive_step6_content_addressed_runtime_gate_v012.md"
    producer_manifests = (
        json.loads(NORMAL_MANIFEST.read_text(encoding="utf-8")),
        json.loads(OPTIMIZED_MANIFEST.read_text(encoding="utf-8")),
    )
    producer_inputs = tuple(
        sorted(
            {
                (PROJECT_ROOT / name).resolve()
                for manifest in producer_manifests
                for name in manifest.get("files", {})
            },
            key=str,
        )
    )
    dependencies = (
        TARGET,
        builder,
        producer_builder,
        supervisor,
        generic_validation,
        launcher,
        runtime_builder,
        runtime_gate,
        V003_FAILURE_RECORD,
        V003_FAILURE_SEAL,
        V005_FAILURE_RECORD,
        V005_FAILURE_SEAL,
        NORMAL_MANIFEST,
        NORMAL_OUTPUT,
        NORMAL_RECEIPT,
        OPTIMIZED_MANIFEST,
        OPTIMIZED_OUTPUT,
        OPTIMIZED_RECEIPT,
    ) + producer_inputs
    for path in dependencies:
        if not path.is_file():
            raise FileNotFoundError(path)
    for record, record_hash, seal, seal_hash in (
        (
            V003_FAILURE_RECORD,
            V003_FAILURE_RECORD_SHA256,
            V003_FAILURE_SEAL,
            V003_FAILURE_SEAL_SHA256,
        ),
        (
            V005_FAILURE_RECORD,
            V005_FAILURE_RECORD_SHA256,
            V005_FAILURE_SEAL,
            V005_FAILURE_SEAL_SHA256,
        ),
    ):
        if (
            sha256(record) != record_hash
            or sha256(seal) != seal_hash
            or seal.read_text(encoding="utf-8").strip()
            != f"{record_hash}  {record.name}"
        ):
            raise RuntimeError(
                f"preserved failure lineage does not match its trust anchor: {record.name}"
            )
    for path in (MANIFEST, OUTPUT, RECEIPT):
        if path.exists():
            raise FileExistsError(f"refusing to overwrite {path}")

    normal_hashes = {
        "normal_manifest_sha256": sha256(NORMAL_MANIFEST),
        "normal_output_sha256": sha256(NORMAL_OUTPUT),
        "normal_receipt_sha256": sha256(NORMAL_RECEIPT),
    }
    optimized_hashes = {
        "optimized_manifest_sha256": sha256(OPTIMIZED_MANIFEST),
        "optimized_output_sha256": sha256(OPTIMIZED_OUTPUT),
        "optimized_receipt_sha256": sha256(OPTIMIZED_RECEIPT),
    }
    exact = build_exact_output_contract(normal_hashes, optimized_hashes)
    checks = list(VERIFIER_CHECKS)
    payload = build_manifest_payload(
        {relative(path): sha256(path) for path in dependencies},
        exact,
        checks,
    )
    with MANIFEST.open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")
    print(MANIFEST)
    print("verifier_manifest_binds_parent_validated_artifacts=true")
    print("alpha_computed=false")


if __name__ == "__main__":
    main()
