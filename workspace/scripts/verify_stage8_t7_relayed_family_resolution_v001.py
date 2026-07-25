#!/usr/bin/env python3
"""Independent exact verifier for the relayed-family resolution result."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_RELAYED_FAMILY_RESOLUTION_SPEC_V001.md"
REPORT = ROOT / "stage8_execution/work/T07_relayed_family_resolution.json"
OUT = (
    ROOT
    / "stage8_execution/work/"
    "T07_relayed_family_resolution_verification.json"
)
SPEC_SHA256 = "b99c41a1744f3b252c32b484ec0ce49832fc5f95dc64a6dab2c855afd078892e"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


Matrix = list[list[Fraction]]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(
                (
                    left[row][pivot] * right[pivot][column]
                    for pivot in range(len(right))
                ),
                Fraction(0),
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return [
        [a - b for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def frobenius_square(matrix: Matrix) -> Fraction:
    return sum(
        (entry * entry for row in matrix for entry in row),
        Fraction(0),
    )


def projector(vector: tuple[int, ...]) -> Matrix:
    denominator = sum(value * value for value in vector)
    return [
        [
            Fraction(vector[row] * vector[column], denominator)
            for column in range(len(vector))
        ]
        for row in range(len(vector))
    ]


def exact_transport_invariants() -> dict[str, object]:
    vectors = ((-1, 1, 0, 0), (0, -1, 1, 0), (0, 0, -1, 1))
    projectors = [projector(vector) for vector in vectors]
    overlaps = [
        [
            sum(
                (
                    projectors[i][row][column]
                    * projectors[j][column][row]
                    for row in range(4)
                    for column in range(4)
                ),
                Fraction(0),
            )
            for j in range(3)
        ]
        for i in range(3)
    ]
    source_commutator_squares = {}
    for left, right in ((0, 1), (1, 2), (0, 2)):
        commutator = subtract(
            matmul(projectors[left], projectors[right]),
            matmul(projectors[right], projectors[left]),
        )
        source_commutator_squares[f"{left}_{right}"] = (
            frobenius_square(commutator)
        )

    # ||gamma5^2||_F^2=4.  On three qutrit factors,
    # ||C_left C_right||_F^2=4*4*3=48 and
    # ||Delta_left Delta_right||_F^2=8*8*3=192.
    generator_norm_squares = {
        key: value * 4 * 48
        for key, value in source_commutator_squares.items()
    }
    unitary_norm_squares = {
        key: value * 4 * 192
        for key, value in source_commutator_squares.items()
    }
    return {
        "overlaps": [[str(value) for value in row] for row in overlaps],
        "source_commutator_norm_squares": {
            key: str(value)
            for key, value in source_commutator_squares.items()
        },
        "generator_commutator_norm_squares": {
            key: str(value) for key, value in generator_norm_squares.items()
        },
        "unitary_order_norm_squares": {
            key: str(value) for key, value in unitary_norm_squares.items()
        },
    }


def main() -> None:
    report = json.loads(REPORT.read_text())
    exact = exact_transport_invariants()
    f1 = report["F1_transport_assignment"]
    f4 = report["F4_conditioning"]
    f5 = report["F5_interval"]

    checks = {
        "sealed_spec_verified": sha256(SPEC) == SPEC_SHA256,
        "reported_spec_verified": report["spec_sha256"] == SPEC_SHA256,
        "projector_overlaps_exact":
            exact["overlaps"]
            == [
                ["1", "1/4", "0"],
                ["1/4", "1", "1/4"],
                ["0", "1/4", "1"],
            ],
        "generator_commutators_exact":
            exact["generator_commutator_norm_squares"]
            == {"0_1": "72", "1_2": "72", "0_2": "0"}
            and abs(f1["generator_commutator_norms"]["0_1"] ** 2 - 72.0)
            < 2e-12,
        "unitary_order_exact":
            exact["unitary_order_norm_squares"]
            == {"0_1": "288", "1_2": "288", "0_2": "0"}
            and abs(
                f1["unitary_order_difference_norms"]["0_1"] ** 2 - 288.0
            )
            < 2e-11,
        "prior_record_factors_preserved":
            max(f1["prior_pointer_commutator_norms"].values()) == 0.0,
        "active_handle_retraction_unique":
            report["F2_active_handle"]["algebraic_retraction_condition"]
            == "(lambda-1)P=0 => lambda=1"
            and report["F2_active_handle"]["sector_coefficients"]
            == [0, 1, 1],
        "minimal_endpoint_scope_explicit":
            report["F3_endpoint"]["minimal_graph"]
            == {
                "root_count": 1,
                "active_public_endpoint_count": 1,
                "primitive_arrow_count": 1,
            }
            and report["universal_enlarged_branch_exhaustion_claimed"]
            is False,
        "closure_curvature_exact":
            f4["FS_curvature"] == 0.25
            and f4["linear_amplitude_attenuation"] == 0.25
            and f4["endpoint_probability_attenuation"] == 0.5
            and f4["inclusive_sandwich_attenuation"] == 0.0,
        "mixed_intervals_excluded_by_global_bounds":
            f5["mixed_star_bounds"]["2"]["max_designated_transfer"]
            == 2.0 / 3.0
            and f5["mixed_star_bounds"]["2"]["max_symmetric_transfer"]
            < 1.0
            and f5["mixed_star_bounds"]["3"]["max_designated_transfer"]
            == 0.5
            and f5["mixed_star_bounds"]["3"]["max_symmetric_transfer"]
            < 1.0,
        "family_resolution_is_branch_scoped":
            f1["scope"]
            == "causally sequential pure-charge primitive branch"
            and report["branch_conditioning_is_not_physical_in_state_selection"]
            is True
            and report["physical_connected_preparation_derived"] is False,
        "verdict_matches_coordinate_checks":
            report["overall_verdict"]
            == "RELAYED_FAMILY_RESOLVED_IN_DECLARED_BRANCH"
            and report["relayed_family_resolved"] is True,
        "amplitude_not_claimed":
            report["connected_primitive_amplitude_derived"] is False
            and report["connected_linked_cluster_density_proved"] is False,
        "protected_flags_false":
            report["kappa_record_computed"] is False
            and report["coupling_evaluation_authorized"] is False
            and report["alpha_computed"] is False
            and report["proof_authorized"] is False,
        "no_target_access": report["no_target_access_attestation"] is True,
    }
    output = {
        "schema": "stage8_t7_relayed_family_resolution_verification_v001",
        "pass": all(checks.values()),
        "checks": checks,
        "independent_exact_transport_invariants": exact,
        "construction_script_imported": False,
    }
    OUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))
    if not output["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
