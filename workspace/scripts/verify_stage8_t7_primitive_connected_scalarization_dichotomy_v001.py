#!/usr/bin/env python3
"""Independent Gram-data verifier for the primitive scalarization dichotomy."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_PRIMITIVE_CONNECTED_SCALARIZATION_DICHOTOMY_SPEC_V001.md"
SPEC_SHA256 = "fdb7abb30c1db155df95bd062e3bc77ea5a1ba1462689e6004db951e347ab430"
PRIMARY = ROOT / "stage8_execution/work/T07_primitive_connected_scalarization_dichotomy.json"
OUTPUT = ROOT / "stage8_execution/work/T07_primitive_connected_scalarization_dichotomy_verification.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "spec hash mismatch")
    primary = json.loads(PRIMARY.read_text(encoding="ascii"))
    require(primary["spec_sha256"] == SPEC_SHA256, "primary used another spec")

    # Gram matrix of the normalized incidence vectors u_0,u_1,u_2.
    gram = (
        (Fraction(1), Fraction(-1, 2), Fraction(0)),
        (Fraction(-1, 2), Fraction(1), Fraction(-1, 2)),
        (Fraction(0), Fraction(-1, 2), Fraction(1)),
    )

    rows = []
    for stage in range(1, 4):
        coefficient = Fraction(1)
        for index in range(stage - 1):
            coefficient *= gram[index + 1][index]

        expectations = {}
        for state in range(3):
            value = (
                coefficient
                * gram[state][stage - 1]
                * gram[0][state]
            )
            expectations[f"P{state}"] = text(value)

        operator_trace = coefficient * gram[0][stage - 1]
        normalized_trace = operator_trace / 4
        line_return = coefficient
        rows.append(
            {
                "N": stage,
                "state_expectations": expectations,
                "normalized_trace": text(normalized_trace),
                "causal_initial_to_final_line_return": text(line_return),
            }
        )

    primary_rows = primary["D2_shared_source_compressions"]
    require(len(rows) == len(primary_rows), "row count mismatch")
    for expected, actual in zip(rows, primary_rows):
        require(expected["N"] == actual["N"], "stage mismatch")
        require(expected["state_expectations"] == actual["state_expectations"],
                f"state expectation mismatch at N={expected['N']}")
        require(expected["normalized_trace"] == actual["normalized_trace"],
                f"trace mismatch at N={expected['N']}")
        require(
            expected["causal_initial_to_final_line_return"]
            == actual["causal_initial_to_final_line_return"],
            f"line-return mismatch at N={expected['N']}",
        )

    counterfamily = primary["D1_record_line_relay"]["connected_counterfamily"]
    require(counterfamily["vacuum_and_one_record_restrictions_equal"] is True,
            "counterfamily local restriction changed")
    require(counterfamily["two_record_action_differs"] is True,
            "counterfamily connected action did not change")
    require(primary["verdict"] == "PRIMITIVE_CONNECTED_SCALARIZATION_UNDERDETERMINED",
            "primary verdict changed")
    require(primary["alpha_computed"] is False, "protected alpha flag changed")
    require(primary["proof_authorized"] is False, "proof flag changed")

    result = {
        "schema": "stage8-t7-primitive-connected-scalarization-dichotomy-verifier-v001",
        "spec_sha256": SPEC_SHA256,
        "primary_sha256": sha256(PRIMARY),
        "independent_method": "normalized-incidence Gram products",
        "reconstructed_rows": rows,
        "counterfamily_verified": True,
        "verdict_verified": True,
        "pass": True,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
