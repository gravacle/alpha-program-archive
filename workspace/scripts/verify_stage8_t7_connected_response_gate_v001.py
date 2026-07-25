#!/usr/bin/env python3
"""Independent verifier for the Stage-8 T7 connected-response gate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(
    "/Users/bgm/Documents/New project/gravity_emergence_evidence_program/"
    "alpha_fundamental_record_action_cleanroom_v003"
)
REPORT = ROOT / "stage8_execution/t_reports/T07.json"
SEAL = (
    ROOT
    / "stage8_execution/t7_connected_response/"
    "T07_CONNECTED_RESPONSE_GATE_V001.seal.sha256"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def verify_content_address(path: Path) -> bool:
    obj = json.loads(path.read_text())
    claimed = obj["sha256_of_body"]
    obj["sha256_of_body"] = ""
    actual = sha256_bytes(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    )
    return actual == claimed


def verify_seal() -> bool:
    rows = []
    for line in SEAL.read_text().splitlines():
        expected, relative = line.split("  ", 1)
        rows.append(sha256_file(ROOT / relative) == expected)
    return bool(rows) and all(rows)


def independent_counterfamily() -> dict[str, object]:
    b0 = [
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
    ]
    b1 = [
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
    ]
    restriction_equal = all(
        b0[i][j] == b1[i][j] for i in range(3) for j in range(3)
    )
    return {
        "vacuum_and_one_record_restrictions_equal": restriction_equal,
        "connected_two_record_dynamics_differ": b0[3][3] != b1[3][3],
    }


def run() -> None:
    report = json.loads(REPORT.read_text())
    counter = independent_counterfamily()
    reported_counter = report["evidence"]["connected_counterfamily"]
    checks = {
        "content_address_verified": verify_content_address(REPORT),
        "seal_verified": verify_seal(),
        "T7_is_blocked": report["pass"] is False,
        "mandatory_failure_class": report["failure_class"]
        == "MANDATORY_ZERO_FREE_AND_CONNECTED_DENSITY_NOT_DERIVED",
        "authority_statements_verified": report["evidence"]["authority_audit"][
            "all_required_statements_verified"
        ],
        "no_successor_closure_found": report["evidence"]["corpus_closure_scan"][
            "no_successor_closure_found"
        ]
        and report["evidence"]["corpus_closure_scan"]["true_hit_count"] == 0,
        "counterfamily_recomputed": all(
            counter[key] == reported_counter[key] for key in counter
        ),
        "downstream_CTP_not_misused": report["evidence"][
            "downstream_Qspec_CTP_issue_used_as_T7_blocker"
        ]
        is False,
        "no_new_principle": report["evidence"]["new_principle_adopted"] is False,
        "no_target_value": report["evidence"]["target_value_used"] is False,
        "protected_flags_false": all(
            value is False for value in report["protected_flags"].values()
        ),
    }
    output = {
        "schema": "stage8-t7-connected-response-independent-verification-v001",
        "pass": all(checks.values()),
        "checks": checks,
        "independent_counterfamily": counter,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    if not output["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
