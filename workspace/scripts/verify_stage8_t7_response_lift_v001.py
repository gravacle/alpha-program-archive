#!/usr/bin/env python3
"""Independent verification of the Stage-8 T7 response-lift audit."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(
    "/Users/bgm/Documents/New project/gravity_emergence_evidence_program/"
    "alpha_fundamental_record_action_cleanroom_v003"
)
REPORT = ROOT / "stage8_execution/work/T07_response_lift_underdetermination.json"
SEAL = (
    ROOT
    / "stage8_execution/t7_response_lift/"
    "T07_RESPONSE_LIFT_AUDIT_V001.seal.sha256"
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
    return claimed == actual


def verify_seal(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for line in path.read_text().splitlines():
        expected, relative = line.split("  ", 1)
        artifact = ROOT / relative
        actual = sha256_file(artifact)
        rows.append(
            {
                "path": relative,
                "expected": expected,
                "actual": actual,
                "verified": expected == actual,
            }
        )
    return rows


def independent_hessians() -> dict[str, str]:
    # For z(theta)=cos(theta), z(0)=1, z'(0)=0, z''(0)=-1.
    # Gamma=-log(z) locally, so Gamma''(0)=-(z''z-z'^2)/z^2=1.
    z0 = Fraction(1)
    z1 = Fraction(0)
    z2 = Fraction(-1)
    loschmidt = -(z2 * z0 - z1 * z1) / (z0 * z0)

    # For the inclusive equal-branch CTP closure z(theta)=1 identically.
    ctp = Fraction(0)
    return {"in_out_loschmidt": str(loschmidt), "inclusive_equal_branch_ctp": str(ctp)}


def run() -> None:
    report = json.loads(REPORT.read_text())
    seal_rows = verify_seal(SEAL)
    hessians = independent_hessians()
    reported = {
        row["name"]: row["gamma_hessian_at_zero"]
        for row in report["scalar_closure_counterexample"]["closures"]
    }

    checks = {
        "content_address_verified": verify_content_address(REPORT),
        "seal_verified": bool(seal_rows) and all(row["verified"] for row in seal_rows),
        "authority_disclosures_verified": report["authority_audit"][
            "all_disclosures_verified"
        ],
        "independent_hessians_match": hessians == reported,
        "closures_disagree": len(set(hessians.values())) == 2,
        "t7_not_promoted": report["t7_pass"] is False,
        "no_new_principle": report["new_principle_adopted"] is False,
        "no_target_value": report["target_value_used"] is False,
        "protected_flags_false": all(
            value is False for value in report["protected_flags"].values()
        ),
    }
    output = {
        "schema": "stage8-t7-response-lift-independent-verification-v001",
        "pass": all(checks.values()),
        "checks": checks,
        "independent_hessians": hessians,
        "seal_rows": seal_rows,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    if not output["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
