#!/usr/bin/env python3
"""Re-execute the five pinned Gate 1-4 cores for Stage-8 T0."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(
    "/Users/bgm/Documents/New project/gravity_emergence_evidence_program/"
    "alpha_fundamental_record_action_cleanroom_v003"
)
AUTHORITY_SPEC = (
    ROOT / "STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_AUTHORITY_FABLE_V002.md"
)
OUTPUT_ROOT = Path(
    "/Users/bgm/Documents/New project/_external_handoffs/"
    "fable_alpha_cleanroom/OUTPUT"
)
COPIED_SCRIPT_ROOT = ROOT / "stage8_execution/t0_lineage/core_scripts"
RESULT_PATH = ROOT / "stage8_execution/t0_lineage/raw_execution.json"
FIRST_ATTEMPT_PATH = (
    ROOT / "stage8_execution/t0_lineage/raw_execution_attempt1_runtime_blocked.json"
)
REPORT_PATH = ROOT / "stage8_execution/t_reports/T00.json"
PYTHON = Path(
    "/Users/bgm/.cache/codex-runtimes/codex-primary-runtime/dependencies/"
    "python/bin/python3"
)

AUTHORITY_SPEC_SHA256 = (
    "ddb36cbfe4edfc2a0520e9ae58063295214c64afed5cad5a64e9f311826358f5"
)
SCRIPT_ORDER = [
    "34_gate1_comparison_group_v001.py",
    "40_gate2_first_opening_v001.py",
    "37_gate3_hilbert_functor_v001.py",
    "31_gate4_differential_uniqueness_v001.py",
    "43_gate4_covector_ray_v001.py",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def write_content_addressed(path: Path, body: dict[str, object]) -> None:
    body = dict(body)
    body["sha256_of_body"] = ""
    canonical = json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    body["sha256_of_body"] = sha256_bytes(canonical)
    path.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")


def authority_rows() -> dict[str, str]:
    text = AUTHORITY_SPEC.read_text()
    rows = dict(re.findall(r"^([0-9a-f]{64})  (.+)$", text, flags=re.MULTILINE))
    return {
        filename: digest
        for digest, filename in rows.items()
        if re.match(r"^(?:3[0-9]|4[0-4])_", filename)
    }


def verify_seal(path: Path) -> dict[str, object]:
    lines = path.read_text().splitlines()
    match = re.fullmatch(r"([0-9a-f]{64})  (.+)", lines[0]) if lines else None
    if not match:
        return {"pass": False, "reason": "malformed first line"}
    expected, filename = match.groups()
    target = path.parent / filename
    actual = sha256_file(target) if target.is_file() else None
    return {
        "pass": actual == expected,
        "target": filename,
        "expected": expected,
        "actual": actual,
    }


def main() -> int:
    failures: list[str] = []
    if not PYTHON.is_file():
        failures.append("pinned workspace Python runtime is missing")
    if sha256_file(AUTHORITY_SPEC) != AUTHORITY_SPEC_SHA256:
        failures.append("authority specification hash mismatch")

    expected = authority_rows()
    if len(expected) != 30:
        failures.append(f"expected 30 lineage pins, found {len(expected)}")

    authority_checks: dict[str, object] = {}
    for filename, digest in sorted(expected.items()):
        path = OUTPUT_ROOT / filename
        actual = sha256_file(path) if path.is_file() else None
        matches = actual == digest
        authority_checks[filename] = {
            "expected": digest,
            "actual": actual,
            "matches": matches,
        }
        if not matches:
            failures.append(f"authority mismatch: {filename}")

    seal_checks: dict[str, object] = {}
    for filename in sorted(expected):
        if not filename.endswith(".seal.sha256"):
            continue
        check = verify_seal(OUTPUT_ROOT / filename)
        seal_checks[filename] = check
        if not check["pass"]:
            failures.append(f"seal verification failed: {filename}")

    executions: dict[str, object] = {}
    for filename in SCRIPT_ORDER:
        copied = COPIED_SCRIPT_ROOT / filename
        source = OUTPUT_ROOT / filename
        copied_hash = sha256_file(copied) if copied.is_file() else None
        source_hash = sha256_file(source) if source.is_file() else None
        expected_hash = expected.get(filename)
        if copied_hash != expected_hash or source_hash != expected_hash:
            failures.append(f"copied script is not authority-identical: {filename}")
            continue
        completed = subprocess.run(
            [str(PYTHON), "-I", str(copied)],
            cwd=ROOT,
            text=False,
            capture_output=True,
            check=False,
        )
        stdout = completed.stdout
        stderr = completed.stderr
        fail_marker = b"FAIL:" in stdout or b"FAIL:" in stderr
        pass_count = stdout.count(b"PASS")
        executions[filename] = {
            "authority_sha256": expected_hash,
            "copied_sha256": copied_hash,
            "exit_code": completed.returncode,
            "stdout_sha256": sha256_bytes(stdout),
            "stderr_sha256": sha256_bytes(stderr),
            "stdout_line_count": len(stdout.splitlines()),
            "stderr_line_count": len(stderr.splitlines()),
            "pass_marker_count": pass_count,
            "fail_marker_present": fail_marker,
        }
        if completed.returncode != 0 or fail_marker or pass_count == 0:
            failures.append(f"core re-execution failed: {filename}")

    result = {
        "schema": "stage8-t0-lineage-raw-v001",
        "authority_spec_sha256": AUTHORITY_SPEC_SHA256,
        "canonical_workspace": str(ROOT),
        "external_lineage_root": str(OUTPUT_ROOT),
        "isolated_python_runtime": str(PYTHON),
        "authority_pin_count": len(expected),
        "authority_checks": authority_checks,
        "seal_checks": seal_checks,
        "executions": executions,
        "all_authority_pins_match": all(
            item["matches"] for item in authority_checks.values()
        ),
        "all_lineage_seals_match": all(
            item["pass"] for item in seal_checks.values()
        ),
        "all_five_cores_reexecuted": len(executions) == len(SCRIPT_ORDER),
        "M0_M1_M2_identity_requirement_addressed": (
            "37_gate3_hilbert_functor_v001.py" in executions
        ),
        "failures": failures,
        "pass": not failures,
        "protected_flags": {
            "alpha_computed": False,
            "proof_authorized": False,
        },
    }
    RESULT_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    write_content_addressed(
        REPORT_PATH,
        {
            "schema": "stage8-obligation-report-v001",
            "obligation": "T00",
            "pass": not failures,
            "authority_spec_sha256": AUTHORITY_SPEC_SHA256,
            "authority_pin_count": len(expected),
            "lineage_seal_count": len(seal_checks),
            "reexecuted_core_count": len(executions),
            "M0_M1_M2_identity_requirement": (
                "addressed by authority-identical Gate-3 core re-execution"
            ),
            "raw_execution_sha256": sha256_file(RESULT_PATH),
            "runtime_blocked_attempt_sha256": (
                sha256_file(FIRST_ATTEMPT_PATH)
                if FIRST_ATTEMPT_PATH.is_file()
                else None
            ),
            "runtime_blocked_attempt_classification": (
                "environment-only: system isolated Python lacked NumPy"
            ),
            "isolated_python_runtime": str(PYTHON),
            "protected_flags": {
                "alpha_computed": False,
                "proof_authorized": False,
            },
        },
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
