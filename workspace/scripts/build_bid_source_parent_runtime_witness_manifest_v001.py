#!/usr/bin/env python3
"""Build the sealed manifest for the independent source-parent runtime witness."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
RUNTIME = PROJECT_ROOT / "provenance" / "primitive_step6_runtime_snapshot_v008.json"
RUNTIME_BUILDER = (
    PROJECT_ROOT / "scripts" / "build_primitive_step6_runtime_snapshot_v008.py"
)
RUNTIME_GATE = PROJECT_ROOT / "primitive_step6_content_addressed_runtime_gate_v006.md"
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
TARGET = ROOT / "scripts" / "verify_bid_source_parent_runtime_witness_v001.py"
MANIFEST = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_runtime_witness_verification_v001_execution_manifest.json"
)
OUTPUT = (
    PROJECT_ROOT
    / "results"
    / "bid_source_parent_runtime_witness_verification_v001.json"
)
RECEIPT = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_runtime_witness_verification_v001_execution_receipt.json"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"duplicate JSON key: {key}")
        output[key] = value
    return output


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(
        path.read_text(encoding="utf-8"),
        parse_constant=lambda value: (_ for _ in ()).throw(
            ValueError(f"non-finite JSON constant: {value}")
        ),
        object_pairs_hook=reject_duplicate_keys,
    )
    if not isinstance(value, dict):
        raise RuntimeError(f"{path} is not a JSON object")
    return value


def project_relative(path: Path) -> str:
    return str(path.resolve().relative_to(PROJECT_ROOT.resolve()))


def main() -> None:
    for path in (
        RUNTIME,
        RUNTIME_BUILDER,
        RUNTIME_GATE,
        WITNESS_MANIFEST,
        WITNESS_OUTPUT,
        WITNESS_RECEIPT,
        TARGET,
    ):
        if not path.is_file():
            raise FileNotFoundError(path)
    for path in (MANIFEST, OUTPUT, RECEIPT):
        if path.exists():
            raise FileExistsError(f"refusing to overwrite {path}")

    witness_manifest = read_json(WITNESS_MANIFEST)
    witness_receipt = read_json(WITNESS_RECEIPT)
    witness_files = witness_manifest.get("files")
    if not isinstance(witness_files, dict) or not witness_files:
        raise RuntimeError("witness manifest has no sealed file inventory")

    files = dict(witness_files)
    for path in (
        RUNTIME_BUILDER,
        RUNTIME_GATE,
        WITNESS_MANIFEST,
        WITNESS_OUTPUT,
        WITNESS_RECEIPT,
        TARGET,
    ):
        files[project_relative(path)] = sha256(path)
    for relative, expected in files.items():
        path = (PROJECT_ROOT / relative).resolve()
        path.relative_to(PROJECT_ROOT.resolve())
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(f"witness dependency changed before sealing: {relative}")

    checks = [
        "manifest_file_inventory_recomputed",
        "target_source_buffer_bound",
        "runtime_snapshot_bound",
        "output_contract_bound",
        "receipt_assurance_flags_exact",
        "module_and_native_ledgers_classified",
        "environment_and_write_policy_verified",
        "known_blockers_and_alpha_firewall_retained",
    ]
    exact = {
        "schema": "gravacle.bid-source-parent-runtime-witness-verification.v001",
        "status": "PASS_CONTENT_ADDRESSED_SOURCE_PARENT_RUNTIME_WITNESS_ALPHA_FALSE",
        "witness_manifest_sha256": sha256(WITNESS_MANIFEST),
        "witness_output_sha256": sha256(WITNESS_OUTPUT),
        "witness_receipt_sha256": sha256(WITNESS_RECEIPT),
        "witness_loaded_module_count": len(witness_receipt.get("loaded_modules", [])),
        "witness_loaded_native_image_count": len(
            witness_receipt.get("loaded_native_images", [])
        ),
        "source_parent_closure": False,
        "content_addressed_runtime_sealed": True,
        "proof_authorized": False,
        "alpha_computed": False,
    }
    payload = {
        "schema": "gravacle.sealed-target-execution.v002",
        "stage": "bid-source-parent-runtime-witness-verification-v001",
        "alpha_computed": False,
        "runtime_snapshot": project_relative(RUNTIME),
        "runtime_snapshot_sha256": sha256(RUNTIME),
        "target_script": project_relative(TARGET),
        "expected_output": project_relative(OUTPUT),
        "execution_receipt": project_relative(RECEIPT),
        "files": files,
        "output_contract": {
            "required_fields": list(exact) + ["checks"],
            "exact_values": exact,
            "required_check_keys": checks,
        },
    }
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST.open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")
    print(MANIFEST)
    print(f"sealed_dependency_files={len(files)}")
    print("alpha_computed=false")


if __name__ == "__main__":
    main()
