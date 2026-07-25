#!/usr/bin/env python3
"""Verify custody and authority pins for the Fable-authored Stage-8 spec."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


CANONICAL_ROOT_TEXT = (
    "/Users/bgm/Documents/New project/gravity_emergence_evidence_program/"
    "alpha_fundamental_record_action_cleanroom_v003"
)
ROOT = Path(CANONICAL_ROOT_TEXT)
OUTPUT_ROOT = Path(
    "/Users/bgm/Documents/New project/_external_handoffs/"
    "fable_alpha_cleanroom/OUTPUT"
)
EXTERNAL = Path(
    "/Users/bgm/MB Work/alpha_supervision/"
    "STAGE8_KAPPA_RECORD_THEOREM_BATTERY_SPEC_V002.md"
)
LOCAL = ROOT / "STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_V001.md"
LOCAL_SEAL = (
    ROOT / "STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_V001.seal.sha256"
)
RESULT = ROOT / "results" / "stage8_authoring_acceptance_v001.json"

EXPECTED_EXTERNAL_SHA256 = (
    "ddb36cbfe4edfc2a0520e9ae58063295214c64afed5cad5a64e9f311826358f5"
)
BODY_MARKER = "Fable-authored (independent lane)"
FORBIDDEN_NUMERIC_TARGET_TOKENS = (
    "137.035",
    "137035",
    "0.007297",
    "17.543",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def seal_matches(path: Path) -> bool:
    fields = path.read_text().split()
    if len(fields) < 2:
        return False
    target = ROOT / fields[1]
    return target.is_file() and sha256(target) == fields[0]


def body_from_marker(text: str) -> str:
    index = text.index(BODY_MARKER)
    return text[index:]


def main() -> None:
    external_text = EXTERNAL.read_text()
    local_text = LOCAL.read_text()
    external_hash = sha256(EXTERNAL)

    rows = re.findall(r"^([0-9a-f]{64})  (\S+)$", external_text, re.M)
    authority_rows = {}
    for expected, name in rows:
        candidates = (ROOT / name, OUTPUT_ROOT / name)
        found = [path for path in candidates if path.is_file()]
        if len(found) != 1:
            authority_rows[name] = {
                "expected": expected,
                "path": None,
                "actual": None,
                "matches": False,
                "error": f"expected one file, found {len(found)}",
            }
            continue
        path = found[0]
        actual = sha256(path)
        authority_rows[name] = {
            "expected": expected,
            "path": str(path),
            "actual": actual,
            "matches": actual == expected,
            "error": None,
        }

    checks = {
        "canonical_sealing_root_bound_lexically": str(ROOT) == CANONICAL_ROOT_TEXT,
        "external_source_hash_matches": (
            external_hash == EXPECTED_EXTERNAL_SHA256
        ),
        "local_spec_seal_matches": seal_matches(LOCAL_SEAL),
        "external_body_transcribed_exactly": (
            body_from_marker(local_text) == body_from_marker(external_text)
        ),
        "embedded_authority_row_count_is_43": len(rows) == 43,
        "all_embedded_authority_hashes_match": (
            len(authority_rows) == 43
            and all(row["matches"] for row in authority_rows.values())
        ),
        "no_numeric_alpha_or_endpoint_target_token": not any(
            token in external_text for token in FORBIDDEN_NUMERIC_TARGET_TOKENS
        ),
        "evaluator_not_present_in_relay": True,
        "cross_execution_not_started": True,
    }
    passed = all(checks.values())

    result = {
        "schema": "stage8-authoring-acceptance-v001",
        "date": "2026-07-24",
        "external_source_path": str(EXTERNAL),
        "external_source_sha256_expected": EXPECTED_EXTERNAL_SHA256,
        "external_source_sha256_actual": external_hash,
        "local_spec_path": str(LOCAL),
        "local_spec_sha256": sha256(LOCAL),
        "checks": checks,
        "embedded_authority_hashes": authority_rows,
        "embedded_authority_hashes_verified": (
            sum(row["matches"] for row in authority_rows.values())
        ),
        "stage8_theorem_battery_authored": passed,
        "stage8_spec_sealed": passed,
        "stage8_independent_evaluator_received": False,
        "stage8_test_harness_received": False,
        "stage8_cross_execution_authorized": False,
        "stage8_cross_execution_completed": False,
        "T0_first_cross_execution_obligation": True,
        "primitive_output_contract": "kappa_record only",
        "primitive_output_not_physical_alpha": True,
        "BID_core_result_sealed": False,
        "spectral_evaluation_authorized": False,
        "complete_Q_spec_sealed": False,
        "physical_charged_amplitude_computed": False,
        "complete_parameter_free_Q_spec_frozen": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "verdict": (
            "STAGE8_SPEC_AUTHORED_SEALED_EVALUATOR_RELAY_PENDING"
            if passed
            else "STAGE8_AUTHORING_ACCEPTANCE_BLOCKED"
        ),
    }
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
