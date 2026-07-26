#!/usr/bin/env python3
"""Run the sealed Stage-8 T7 production lanes and issue local execution receipts."""

from __future__ import annotations

import hashlib
import json
import os
import stat
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
RUNTIME_MARKER = "_stage8_t7_content_addressed_runtime_v001"
RUNTIME_MANIFEST_SHA256 = (
    "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b"
)
PINNED_PYTHON = Path(
    "/Users/bgm/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/python/bin/python3"
).resolve()
RUNTIME_LAUNCHER = (
    ROOT / "scripts/launch_stage8_t7_content_addressed_runtime_v001.py"
)
IMPLEMENTATION_MANIFEST = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_regulated_car_operator_response_implementation_v001.json"
)
IMPLEMENTATION_SEAL = Path(f"{IMPLEMENTATION_MANIFEST}.seal.sha256")
IMPLEMENTATION_SIGNATURE = Path(f"{IMPLEMENTATION_MANIFEST}.asc")
SIGNING_FINGERPRINT = "18488605D44F65A9B57B610AA5F3A86512A04D61"
GPG = Path("/opt/homebrew/bin/gpg")

WORK = ROOT / "stage8_execution/work"
INDEPENDENT_JSON = (
    WORK
    / "T07_actual_parent_regulated_car_operator_response_"
    "independent_precomparison_v001.json"
)
INDEPENDENT_NPZ = INDEPENDENT_JSON.with_suffix(".npz")
PRIMARY_JSON = (
    WORK / "T07_actual_parent_regulated_car_operator_response_primary_v001.json"
)
PRIMARY_NPZ = PRIMARY_JSON.with_suffix(".npz")
COMPARISON_JSON = (
    WORK / "T07_actual_parent_regulated_car_operator_response_comparison_v001.json"
)
INDEPENDENT_RECEIPT = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_car_independent_execution_receipt_v001.json"
)
PRIMARY_RECEIPT = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_car_primary_execution_receipt_v001.json"
)
COMPARISON_RECEIPT = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_car_comparison_execution_receipt_v001.json"
)

TARGETS = {
    "independent": (
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "independent_v001.py"
    ),
    "primary": (
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v001.py"
    ),
    "comparison": (
        "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
        "v001.py"
    ),
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def strict_json(path: Path) -> dict[str, Any]:
    def object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            require(key not in result, f"duplicate JSON key in {path}: {key}")
            result[key] = value
        return result

    value = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=object_pairs,
        parse_constant=lambda value: (_ for _ in ()).throw(
            RuntimeError(f"non-finite JSON constant in {path}: {value}")
        ),
    )
    require(isinstance(value, dict), f"JSON document is not an object: {path}")
    return value


def atomic_sealed_json(path: Path, payload: dict[str, Any]) -> str:
    seal = Path(f"{path}.seal.sha256")
    require(not path.exists(), f"immutable receipt already exists: {path}")
    require(not seal.exists(), f"immutable receipt seal already exists: {seal}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)
    digest = sha256(path)
    seal_temporary = seal.with_suffix(seal.suffix + ".tmp")
    seal_temporary.write_text(f"{digest}  {path.name}\n", encoding="ascii")
    os.replace(seal_temporary, seal)
    for artifact in (path, seal):
        artifact.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    return digest


def verify_adjacent_seal(path: Path) -> str:
    seal = Path(f"{path}.seal.sha256")
    require(path.is_file(), f"expected output is absent: {path}")
    require(seal.is_file(), f"expected output seal is absent: {seal}")
    fields = seal.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, f"malformed output seal: {seal}")
    digest = sha256(path)
    require(fields[0] == digest, f"output seal digest mismatch: {path}")
    require(fields[1] == path.name, f"output seal filename mismatch: {path}")
    return digest


def verify_implementation() -> tuple[str, dict[str, str]]:
    attestation = getattr(sys, RUNTIME_MARKER, None)
    require(isinstance(attestation, dict), "pipeline requires the sealed runtime launcher")
    require(
        attestation.get("runtime_manifest_sha256") == RUNTIME_MANIFEST_SHA256,
        "pipeline runtime manifest mismatch",
    )
    require(IMPLEMENTATION_MANIFEST.is_file(), "implementation manifest is absent")
    require(IMPLEMENTATION_SEAL.is_file(), "implementation seal is absent")
    require(IMPLEMENTATION_SIGNATURE.is_file(), "implementation signature is absent")
    manifest_digest = sha256(IMPLEMENTATION_MANIFEST)
    fields = IMPLEMENTATION_SEAL.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, "malformed implementation seal")
    require(fields[0] == manifest_digest, "implementation seal digest mismatch")
    manifest = strict_json(IMPLEMENTATION_MANIFEST)
    rows = manifest.get("files")
    require(isinstance(rows, list) and bool(rows), "implementation file inventory is empty")
    row_map = {str(row["path"]): str(row["sha256"]) for row in rows}
    require(
        row_map.get(str(SELF.relative_to(ROOT))) == sha256(SELF),
        "pipeline is not implementation-bound",
    )
    for relative, expected in row_map.items():
        path = ROOT / relative
        require(path.is_file(), f"implementation input is absent: {relative}")
        require(sha256(path) == expected, f"implementation drift: {relative}")

    verification = subprocess.run(
        [
            str(GPG),
            "--batch",
            "--status-fd",
            "1",
            "--verify",
            str(IMPLEMENTATION_SIGNATURE),
            str(IMPLEMENTATION_MANIFEST),
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    require(verification.returncode == 0, "implementation signature verification failed")
    require(
        f"[GNUPG:] VALIDSIG {SIGNING_FINGERPRINT}" in verification.stdout,
        "implementation signature fingerprint mismatch",
    )
    return manifest_digest, row_map


def lane_command(target: str, arguments: list[str]) -> list[str]:
    return [
        str(PINNED_PYTHON),
        "-I",
        "-S",
        str(RUNTIME_LAUNCHER),
        target,
        *arguments,
    ]


def run_lane(
    *,
    lane: str,
    target: str,
    arguments: list[str],
    outputs: tuple[Path, ...],
    receipt: Path,
    implementation_digest: str,
    implementation_rows: dict[str, str],
) -> dict[str, str]:
    require(target == TARGETS[lane], f"unexpected {lane} target")
    for output in outputs:
        require(not output.exists(), f"immutable output already exists: {output}")
        require(
            not Path(f"{output}.seal.sha256").exists(),
            f"immutable output seal already exists: {output}",
        )
    require(not receipt.exists(), f"immutable receipt already exists: {receipt}")
    require(
        not Path(f"{receipt}.seal.sha256").exists(),
        f"immutable receipt seal already exists: {receipt}",
    )

    command = lane_command(target, arguments)
    completed = subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    output_rows: list[dict[str, str]] = []
    if completed.returncode == 0:
        for output in outputs:
            digest = verify_adjacent_seal(output)
            output_rows.append(
                {
                    "path": str(output.relative_to(ROOT)),
                    "sha256": digest,
                    "seal_sha256": sha256(Path(f"{output}.seal.sha256")),
                }
            )
    else:
        for output in outputs:
            if output.is_file() and Path(f"{output}.seal.sha256").is_file():
                output_rows.append(
                    {
                        "path": str(output.relative_to(ROOT)),
                        "sha256": verify_adjacent_seal(output),
                        "seal_sha256": sha256(Path(f"{output}.seal.sha256")),
                    }
                )

    payload = {
        "schema": "stage8_t7_local_sealed_execution_receipt_v001",
        "lane": lane,
        "status": "SUCCEEDED" if completed.returncode == 0 else "BLOCKED",
        "returncode": completed.returncode,
        "target": target,
        "target_sha256": implementation_rows[target],
        "controller": str(SELF.relative_to(ROOT)),
        "controller_sha256": implementation_rows[str(SELF.relative_to(ROOT))],
        "runtime_launcher": str(RUNTIME_LAUNCHER.relative_to(ROOT)),
        "runtime_launcher_sha256": implementation_rows[
            str(RUNTIME_LAUNCHER.relative_to(ROOT))
        ],
        "runtime_manifest_sha256": RUNTIME_MANIFEST_SHA256,
        "implementation_manifest_sha256": implementation_digest,
        "implementation_signature_fingerprint": SIGNING_FINGERPRINT,
        "output_paths_absent_before_execution": True,
        "outputs": output_rows,
        "stdout_sha256": hashlib.sha256(completed.stdout.encode("utf-8")).hexdigest(),
        "stderr_sha256": hashlib.sha256(completed.stderr.encode("utf-8")).hexdigest(),
        "local_execution_receipt_not_remote_attestation": True,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    atomic_sealed_json(receipt, payload)
    require(
        completed.returncode == 0,
        f"{lane} lane blocked: {completed.stderr[-2000:]}",
    )
    return {row["path"]: row["sha256"] for row in output_rows}


def main() -> int:
    implementation_digest, implementation_rows = verify_implementation()
    independent_hashes = run_lane(
        lane="independent",
        target=TARGETS["independent"],
        arguments=[],
        outputs=(INDEPENDENT_JSON, INDEPENDENT_NPZ),
        receipt=INDEPENDENT_RECEIPT,
        implementation_digest=implementation_digest,
        implementation_rows=implementation_rows,
    )
    primary_hashes = run_lane(
        lane="primary",
        target=TARGETS["primary"],
        arguments=[],
        outputs=(PRIMARY_JSON, PRIMARY_NPZ),
        receipt=PRIMARY_RECEIPT,
        implementation_digest=implementation_digest,
        implementation_rows=implementation_rows,
    )
    comparison_arguments = [
        "--independent-json",
        str(INDEPENDENT_JSON),
        "--independent-npz",
        str(INDEPENDENT_NPZ),
        "--primary-json",
        str(PRIMARY_JSON),
        "--primary-npz",
        str(PRIMARY_NPZ),
        "--independent-json-sha256",
        independent_hashes[str(INDEPENDENT_JSON.relative_to(ROOT))],
        "--independent-npz-sha256",
        independent_hashes[str(INDEPENDENT_NPZ.relative_to(ROOT))],
        "--primary-json-sha256",
        primary_hashes[str(PRIMARY_JSON.relative_to(ROOT))],
        "--primary-npz-sha256",
        primary_hashes[str(PRIMARY_NPZ.relative_to(ROOT))],
        "--output",
        str(COMPARISON_JSON),
    ]
    comparison_hashes = run_lane(
        lane="comparison",
        target=TARGETS["comparison"],
        arguments=comparison_arguments,
        outputs=(COMPARISON_JSON,),
        receipt=COMPARISON_RECEIPT,
        implementation_digest=implementation_digest,
        implementation_rows=implementation_rows,
    )
    comparison = strict_json(COMPARISON_JSON)
    require(
        comparison.get("overall_verdict")
        == "ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_COMPARISON_PASSED",
        "sealed comparator did not return the Phase-A PASS verdict",
    )
    summary = {
        "schema": "stage8_t7_actual_parent_car_pipeline_summary_v001",
        "overall_verdict": comparison["overall_verdict"],
        "implementation_manifest_sha256": implementation_digest,
        "independent_receipt_sha256": sha256(INDEPENDENT_RECEIPT),
        "primary_receipt_sha256": sha256(PRIMARY_RECEIPT),
        "comparison_receipt_sha256": sha256(COMPARISON_RECEIPT),
        "comparison_output_sha256":
            comparison_hashes[str(COMPARISON_JSON.relative_to(ROOT))],
        "phase": "A",
        "alpha_computed": False,
        "proof_authorized": False,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
