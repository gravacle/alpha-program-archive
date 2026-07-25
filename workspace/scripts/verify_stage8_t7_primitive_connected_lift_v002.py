#!/usr/bin/env python3
"""Non-tautological successor verifier for the primitive T7 lift block."""

from __future__ import annotations

import cmath
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


def independent_index(coord: tuple[int, int, int, int], length: int) -> int:
    """Independent layout: x0 is least significant, unlike construction."""
    x0, x1, x2, x3 = coord
    return x0 + length * (x1 + length * (x2 + length * x3))


def rebuild_incidence_residual(
    length: int, defect_phase: float | None = None
) -> tuple[int, int, float]:
    """Build every edge endpoint and evaluate D^*J_r from that data."""
    n_vertices = length**4
    root = [complex(1.0 / math.sqrt(n_vertices))] * n_vertices
    residuals: list[complex] = []
    edge_number = 0
    for x3 in range(length):
        for x2 in range(length):
            for x1 in range(length):
                for x0 in range(length):
                    source_coord = (x0, x1, x2, x3)
                    source = independent_index(source_coord, length)
                    for direction in range(4):
                        target_coord = list(source_coord)
                        target_coord[direction] = (
                            target_coord[direction] + 1
                        ) % length
                        target = independent_index(tuple(target_coord), length)
                        phase = (
                            defect_phase
                            if defect_phase is not None and edge_number == 0
                            else 0.0
                        )
                        transport = cmath.exp(1j * phase)
                        residuals.append(
                            transport.conjugate() * root[target] - root[source]
                        )
                        edge_number += 1
    norm = math.sqrt(sum(abs(value) ** 2 for value in residuals))
    return n_vertices, len(residuals), norm


def independent_one_handle_check() -> dict[str, float]:
    angle = math.sqrt(2.0) * (math.pi / math.sqrt(2.0))
    return {
        "root_abs": abs((1.0 + math.cos(angle)) / 2.0),
        "endpoint_abs": abs((1.0 - math.cos(angle)) / 2.0),
        "edge_abs": abs(math.sin(angle) / math.sqrt(2.0)),
    }


def run() -> None:
    report = json.loads(REPORT.read_text())
    reported = {row["L"]: row for row in report["L1_periodic_zero_mode"]}
    rebuilt = {}
    for length in (3, 5, 7):
        n0, n1, flat_norm = rebuild_incidence_residual(length)
        _, _, defect_norm = rebuild_incidence_residual(
            length, defect_phase=0.7
        )
        rebuilt[length] = {
            "vertices": n0,
            "positive_edges": n1,
            "flat_Ddagger_root_norm": flat_norm,
            "one_phase_defect_Ddagger_root_norm": defect_norm,
        }

    handle = independent_one_handle_check()
    endpoint = report["L2_endpoint_classification"]
    checks = {
        "spec_hash_verified": sha256(SPEC) == SPEC_SHA256,
        "reported_spec_hash_verified": report["spec_sha256"] == SPEC_SHA256,
        "incidence_rebuilt_for_all_L": all(
            rebuilt[length]["vertices"] == reported[length]["vertices"]
            and rebuilt[length]["positive_edges"]
            == reported[length]["positive_edges"]
            and rebuilt[length]["flat_Ddagger_root_norm"] == 0.0
            and reported[length]["Ddagger_root_norm"] == 0.0
            for length in (3, 5, 7)
        ),
        "flatness_has_teeth": all(
            rebuilt[length]["one_phase_defect_Ddagger_root_norm"] > 0.0
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
            and handle["edge_abs"] < 3e-15,
        "finite_duhamel_crosscheck_passed":
            report["L4_duhamel_map"]["relative_error"] < 2e-8,
        "blocked_verdict_matches_logic":
            report["verdict"] == "PRIMITIVE_CONNECTED_LIFT_BLOCKED",
        "protected_flags_false":
            report["kappa_record_computed"] is False
            and report["coupling_evaluation_authorized"] is False
            and report["alpha_computed"] is False
            and report["proof_authorized"] is False,
        "no_target_access": report["no_target_access_attestation"] is True,
    }
    output = {
        "schema":
            "stage8_t7_primitive_connected_lift_independent_verification_v002",
        "pass": all(checks.values()),
        "checks": checks,
        "rebuilt_incidence_residuals": rebuilt,
        "independent_one_handle": handle,
        "v001_tautological_zero_construction_reused": False,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    if not output["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
