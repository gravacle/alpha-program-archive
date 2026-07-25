#!/usr/bin/env python3
"""Independent verifier for the Stage-8 T7 response-closure derivation."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(
    "/Users/bgm/Documents/New project/gravity_emergence_evidence_program/"
    "alpha_fundamental_record_action_cleanroom_v003"
)
REPORT = ROOT / "stage8_execution/work/T07_response_closure_selection.json"
SEAL = (
    ROOT
    / "stage8_execution/t7_response_closure_selection/"
    "T07_RESPONSE_CLOSURE_SELECTION_V001.seal.sha256"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def verify_content_address() -> bool:
    obj = json.loads(REPORT.read_text())
    claimed = obj["sha256_of_body"]
    obj["sha256_of_body"] = ""
    actual = sha256_bytes(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    )
    return claimed == actual


def verify_seal() -> bool:
    rows = []
    for line in SEAL.read_text().splitlines():
        expected, relative = line.split("  ", 1)
        rows.append(sha256_file(ROOT / relative) == expected)
    return bool(rows) and all(rows)


def independent_geometry() -> dict[str, str]:
    dpsi_norm = Fraction(1, 2)
    berry_norm = Fraction(1, 4)
    fs = dpsi_norm - berry_norm

    # z(0)=1, z'(0)=i/2, z''(0)=-1/2.
    # Re(z''-(z')^2)=-1/4, so -d2 log|z|=1/4.
    linear = Fraction(1, 4)
    probability = 2 * linear
    inclusive = Fraction(0)
    return {
        "FS_metric": str(fs.numerator) + "/" + str(fs.denominator),
        "linear_Gamma_hessian": str(linear.numerator)
        + "/"
        + str(linear.denominator),
        "probability_Gamma_hessian": str(probability.numerator)
        + "/"
        + str(probability.denominator),
        "inclusive_sandwich_Gamma_hessian": str(inclusive.numerator),
    }


def run() -> None:
    report = json.loads(REPORT.read_text())
    derived = independent_geometry()
    witness = report["D2_exclusion_witness"]
    reported = {key: witness[key] for key in derived}
    candidates = report["D1_admissible_closure_class"]["candidates"]
    survivors = [item["id"] for item in candidates if item["admissible"]]

    checks = {
        "content_address_verified": verify_content_address(),
        "seal_verified": verify_seal(),
        "verdict_derived": report["verdict"]
        == "RESPONSE_CLOSURE_SELECTION_DERIVED",
        "exact_geometry_recomputed": derived == reported,
        "one_admissible_survivor": survivors
        == ["complex_linear_connection_return"],
        "linear_dual_dimension_one": report["D3_linear_uniqueness"][
            "dual_complex_dimension"
        ]
        == 1,
        "normalization_unique": report["D3_linear_uniqueness"][
            "normalized_solution_count"
        ]
        == 1,
        "finite_stage_pass": report["D4_finite_stage"]["pass"] is True,
        "no_new_principle": report["new_principle_adopted"] is False,
        "CTP_not_closed": report["source_inclusive_CTP_closed"] is False,
        "action_multiplier_not_fixed": report["action_multiplier_c_fixed"] is False,
        "analytic_T7_items_false": all(
            report[key] is False
            for key in (
                "volume_uniform_zero_free_neighborhood_proved",
                "connected_linked_cluster_density_proved",
                "Duhamel_intensive_Hessian_equality_proved",
            )
        ),
        "protected_flags_false": all(
            report[key] is False
            for key in (
                "kappa_record_computed",
                "physical_charged_amplitude_computed",
                "coupling_evaluation_authorized",
                "alpha_computed",
                "proof_authorized",
            )
        ),
        "no_target_value": report["target_value_used"] is False,
    }
    output = {
        "schema": "stage8-t7-response-closure-independent-verification-v001",
        "pass": all(checks.values()),
        "checks": checks,
        "independent_geometry": derived,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    if not output["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
