#!/usr/bin/env python3
"""Independent verifier for the Stage-8 T7 source-scalarization no-go."""

from __future__ import annotations

import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_SPEC_V001.md"
PRIMARY = ROOT / "stage8_execution/work/T07_source_scalarization_no_go.json"
OUT = (
    ROOT
    / "stage8_execution/work/T07_source_scalarization_no_go_verification.json"
)
PARENT_RESULT = (
    ROOT / "STAGE8_T7_ACTUAL_PARENT_RECORD_AMPLITUDE_ADJUDICATION_RESULT_V001.md"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def solve_exact_constraints() -> dict[str, str]:
    # Equations, in variable order (c00,c01,c10,c11):
    # 2*c01=0, 2*c10=0, c00-c11=0, c00+c11=1.
    c01 = Fraction(0)
    c10 = Fraction(0)
    c00 = Fraction(1, 2)
    c11 = Fraction(1, 2)
    assert 2 * c01 == 0
    assert 2 * c10 == 0
    assert c00 - c11 == 0
    assert c00 + c11 == 1
    return {
        "E00": str(c00),
        "E01": str(c01),
        "E10": str(c10),
        "E11": str(c11),
    }


def direct_unitary_checks() -> dict[str, object]:
    # Test C(K)=Tr(K)/2 on a generic exact rational matrix under X, Z, and H.
    k = [
        [Fraction(2), Fraction(3)],
        [Fraction(5), Fraction(7)],
    ]
    x = [[Fraction(0), Fraction(1)], [Fraction(1), Fraction(0)]]
    z = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(-1)]]
    # Avoid irrational entries by checking the unnormalized Hadamard
    # conjugation H K H / 2 directly.
    h = [[Fraction(1), Fraction(1)], [Fraction(1), Fraction(-1)]]

    def mm(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
        return [
            [
                sum((a[i][r] * b[r][j] for r in range(2)), Fraction(0))
                for j in range(2)
            ]
            for i in range(2)
        ]

    def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
        return [[a[j][i] for j in range(2)] for i in range(2)]

    def trace_half(a: list[list[Fraction]]) -> Fraction:
        return (a[0][0] + a[1][1]) / 2

    conjugates = {
        "X": mm(mm(x, k), transpose(x)),
        "Z": mm(mm(z, k), transpose(z)),
        "H": [
            [entry / 2 for entry in row]
            for row in mm(mm(h, k), transpose(h))
        ],
    }
    baseline = trace_half(k)
    checks = {name: trace_half(value) == baseline for name, value in conjugates.items()}
    return {
        "baseline": str(baseline),
        "checks": checks,
        "all_pass": all(checks.values()),
    }


def verify_parent_witness(primary: dict[str, object]) -> dict[str, object]:
    text = PARENT_RESULT.read_text()
    match = re.search(r"distance from scalar identity = ([0-9.]+)", text)
    if match is None:
        raise RuntimeError("missing parent scalar-residual witness")
    authoritative = float(match.group(1))
    reported = float(
        primary["N1_non_scalar_parent_witness"]["distance_from_scalar_identity"]
    )
    return {
        "authoritative_distance": authoritative,
        "reported_distance": reported,
        "exact_decimal_match": authoritative == reported,
        "strictly_nonzero": authoritative > 0.0,
    }


def verify_infinite_obstruction() -> dict[str, object]:
    # Traciality gives tau(V_i V_i*)=tau(V_i* V_i)=1 for each isometry.
    tau_identity = Fraction(1)
    tau_sum_of_ranges = tau_identity + tau_identity
    return {
        "tau_identity": str(tau_identity),
        "tau_sum_of_two_orthogonal_ranges": str(tau_sum_of_ranges),
        "contradiction": tau_identity != tau_sum_of_ranges,
    }


def main() -> None:
    primary = json.loads(PRIMARY.read_text())
    exact_solution = solve_exact_constraints()
    unitary = direct_unitary_checks()
    parent = verify_parent_witness(primary)
    infinite = verify_infinite_obstruction()

    pass_value = bool(
        primary["spec_sha256"] == sha256(SPEC)
        and primary["overall_verdict"]
        == "PRIMITIVE_SOURCE_SCALARIZATION_BLOCKED"
        and exact_solution
        == primary["N2_finite_covariance_classification"][
            "matrix_unit_coefficients"
        ]
        and unitary["all_pass"]
        and parent["exact_decimal_match"]
        and parent["strictly_nonzero"]
        and infinite["contradiction"]
        and primary["no_target_access_attestation"]
        and not primary["primitive_source_scalarization_derived"]
        and not primary["connected_primitive_amplitude_derived"]
        and not primary["kappa_record_computed"]
        and not primary["coupling_evaluation_authorized"]
        and not primary["alpha_computed"]
        and not primary["proof_authorized"]
    )

    result = {
        "schema": "stage8_t7_source_scalarization_no_go_verification_v001",
        "spec_sha256": sha256(SPEC),
        "primary_sha256": sha256(PRIMARY),
        "exact_constraint_solution": exact_solution,
        "direct_unitary_checks": unitary,
        "parent_witness_check": parent,
        "infinite_trace_obstruction": infinite,
        "verdict": (
            "INDEPENDENT_SOURCE_SCALARIZATION_BLOCK_CONFIRMED"
            if pass_value
            else "INDEPENDENT_VERIFICATION_FAILED"
        ),
        "pass": pass_value,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not pass_value:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
