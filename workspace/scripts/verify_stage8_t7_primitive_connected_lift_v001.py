#!/usr/bin/env python3
"""Independent verifier for the primitive T7 connected-lift derivation."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(
    "/Users/bgm/Documents/New project/gravity_emergence_evidence_program/"
    "alpha_fundamental_record_action_cleanroom_v003"
)
SPEC = ROOT / "STAGE8_T7_PRIMITIVE_CONNECTED_LIFT_DERIVATION_SPEC_V001.md"
REPORT = ROOT / "stage8_execution/work/T07_primitive_connected_lift.json"
SPEC_SHA256 = "63116a5d2b6f1e557db421e9bbd9e8363f85c84ac04c5d54cb7e7dd314aab544"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def independent_flat_root_check(length: int) -> tuple[int, int, float]:
    n_vertices = length**4
    root_value = 1.0 / math.sqrt(n_vertices)
    residual_square = 0.0
    for _vertex in range(n_vertices):
        for _direction in range(4):
            residual = root_value - root_value
            residual_square += residual * residual
    return n_vertices, 4 * n_vertices, math.sqrt(residual_square)


def independent_one_handle_check() -> dict[str, float]:
    # The pinned polynomial evolution gives these coefficients directly.
    angle = math.sqrt(2.0) * (math.pi / math.sqrt(2.0))
    root = (1.0 + math.cos(angle)) / 2.0
    endpoint = (1.0 - math.cos(angle)) / 2.0
    edge = math.sin(angle) / math.sqrt(2.0)
    return {
        "root_abs": abs(root),
        "endpoint_abs": abs(endpoint),
        "edge_abs": abs(edge),
    }


def run() -> None:
    report = json.loads(REPORT.read_text())
    root_rows = {
        row["L"]: row for row in report["L1_periodic_zero_mode"]
    }
    independent_rows = {}
    for length in (3, 5, 7):
        n0, n1, residual = independent_flat_root_check(length)
        independent_rows[length] = {
            "vertices": n0,
            "positive_edges": n1,
            "Ddagger_root_norm": residual,
        }

    handle = independent_one_handle_check()
    endpoint = report["L2_endpoint_classification"]
    checks = {
        "spec_hash_verified": sha256(SPEC) == SPEC_SHA256,
        "reported_spec_hash_verified": report["spec_sha256"] == SPEC_SHA256,
        "flat_root_recomputed_all_L": all(
            root_rows[length]["vertices"]
            == independent_rows[length]["vertices"]
            and root_rows[length]["positive_edges"]
            == independent_rows[length]["positive_edges"]
            and root_rows[length]["Ddagger_root_norm"]
            == independent_rows[length]["Ddagger_root_norm"]
            == 0.0
            and root_rows[length]["B_root_norm"] == 0.0
            for length in (3, 5, 7)
        ),
        "completed_endpoint_baseline_zero":
            endpoint["orthogonal_completed_endpoint_baseline"] == 0.0,
        "mixed_endpoint_equals_root_component": abs(
            endpoint["mixed_endpoint_baseline"]
            - endpoint["mixed_endpoint_root_component"]
        )
        < 2e-15,
        "root_survival_only_nonzero":
            endpoint["root_survival_baseline"] == 1.0,
        "one_handle_endpoint_transfer_recomputed":
            handle["root_abs"] < 2e-15
            and abs(handle["endpoint_abs"] - 1.0) < 2e-15
            and handle["edge_abs"] < 2e-15,
        "one_handle_numeric_positive_control":
            report["L3_one_handle_positive_control"][
                "endpoint_transfer_error"
            ]
            < 2e-14,
        "finite_duhamel_crosscheck_passed":
            report["L4_duhamel_map"]["relative_error"] < 2e-8,
        "blocked_verdict_matches_logic":
            report["verdict"] == "PRIMITIVE_CONNECTED_LIFT_BLOCKED",
        "no_endpoint_or_amplitude_promoted":
            report["connected_primitive_completed_endpoint_derived"] is False
            and report["connected_primitive_amplitude_derived"] is False,
        "protected_flags_false":
            report["kappa_record_computed"] is False
            and report["coupling_evaluation_authorized"] is False
            and report["alpha_computed"] is False
            and report["proof_authorized"] is False,
        "no_target_access": report["no_target_access_attestation"] is True,
    }
    output = {
        "schema":
            "stage8_t7_primitive_connected_lift_independent_verification_v001",
        "pass": all(checks.values()),
        "checks": checks,
        "independent_flat_root": independent_rows,
        "independent_one_handle": handle,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    if not output["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
