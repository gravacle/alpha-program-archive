#!/usr/bin/env python3
"""Execute the sealed primitive connected-scalarization dichotomy."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_PRIMITIVE_CONNECTED_SCALARIZATION_DICHOTOMY_SPEC_V001.md"
SPEC_SHA256 = "fdb7abb30c1db155df95bd062e3bc77ea5a1ba1462689e6004db951e347ab430"
OUTPUT = ROOT / "stage8_execution/work/T07_primitive_connected_scalarization_dichotomy.json"

AUTHORITIES = {
    "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md":
        "aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a",
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md":
        "6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb",
    "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md":
        "e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6",
    "STAGE8_T7_RELAY_DEPENDENCY_ORDER_AMENDMENT_V001.md":
        "29c32f90e6a4f88a26e22c91504b6d92a1fc4083ad6368984a1e94858caa4365",
    "STAGE8_T7_OPEN_EXHAUSTION_ATTACHMENT_AND_RELAY_NECESSITY_RESULT_V001.md":
        "0df721a170f4f4a1ec630775a3ae47b0d793c82e100b326e681030389eaf0694",
    "STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md":
        "52401eefc3ff84e22f04bbc329a619b830058661db7f969d2d43d167d97d893d",
    "STAGE8_T7_CRITICAL_PATH_SCOPE_CORRECTION_V001.md":
        "9410ee80ff89beed4e133f75fcdb952d059f3386df12069793b5d60895d15486",
    "STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_V001.md":
        "85d24996987278b285d63b8fe15a8732e55664e7c1b09063617b66cb4bc926b4",
}

Matrix = list[list[Fraction]]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def zero_matrix(rows: int, cols: int) -> Matrix:
    return [[Fraction(0) for _ in range(cols)] for _ in range(rows)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(
                (left[i][k] * right[k][j] for k in range(len(right))),
                Fraction(0),
            )
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def trace(matrix: Matrix) -> Fraction:
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction(0))


def outer(vector: list[int]) -> Matrix:
    return [
        [Fraction(vector[i] * vector[j], 2) for j in range(len(vector))]
        for i in range(len(vector))
    ]


def is_scalar_identity(matrix: Matrix) -> bool:
    dimension = len(matrix)
    scalar = trace(matrix) / dimension
    return all(
        matrix[i][j] == (scalar if i == j else 0)
        for i in range(dimension)
        for j in range(dimension)
    )


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def record_counterfamily() -> dict[str, object]:
    base = zero_matrix(4, 4)
    base[1][2] = Fraction(1)
    base[2][1] = Fraction(1)
    alternative = [row[:] for row in base]
    alternative[3][3] = Fraction(1)

    restriction_equal = all(
        base[i][j] == alternative[i][j]
        for i in range(3)
        for j in range(3)
    )
    full_difference = any(
        base[i][j] != alternative[i][j]
        for i in range(4)
        for j in range(4)
    )
    require(restriction_equal, "counterfamily changed vacuum/one-record data")
    require(full_difference, "counterfamily failed to change connected data")
    return {
        "vacuum_and_one_record_restrictions_equal": restriction_equal,
        "two_record_action_differs": full_difference,
        "B0_two_record_diagonal": fraction_text(base[3][3]),
        "B1_two_record_diagonal": fraction_text(alternative[3][3]),
    }


def shared_source_compressions() -> list[dict[str, object]]:
    vectors = (
        [-1, 1, 0, 0],
        [0, -1, 1, 0],
        [0, 0, -1, 1],
    )
    projectors = [outer(vector) for vector in vectors]
    source_dimension = 4
    rows: list[dict[str, object]] = []
    product = projectors[0]

    for stage in range(1, 4):
        if stage > 1:
            product = matmul(projectors[stage - 1], product)
        expectations = [
            trace(matmul(state, product)) for state in projectors
        ]
        normalized_trace = trace(product) / source_dimension

        initial = vectors[0]
        final = vectors[stage - 1]
        line_numerator = sum(
            (
                Fraction(final[i])
                * product[i][j]
                * Fraction(initial[j])
                for i in range(source_dimension)
                for j in range(source_dimension)
            ),
            Fraction(0),
        )
        line_return = line_numerator / 2
        rows.append(
            {
                "N": stage,
                "operator_is_scalar_identity": is_scalar_identity(product),
                "state_expectations": {
                    f"P{index}": fraction_text(value)
                    for index, value in enumerate(expectations)
                },
                "normalized_trace": fraction_text(normalized_trace),
                "causal_initial_to_final_line_return": fraction_text(line_return),
            }
        )

    require(all(not row["operator_is_scalar_identity"] for row in rows),
            "source compression unexpectedly became scalar")
    require(rows[2]["state_expectations"]["P0"] != rows[2]["state_expectations"]["P1"],
            "pre-existing source states did not distinguish the compression")
    require(rows[2]["normalized_trace"] == "0",
            "three-cell normalized trace baseline did not vanish")
    require(rows[2]["causal_initial_to_final_line_return"] == "1/4",
            "causal-line diagnostic changed")
    return rows


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "sealed spec hash mismatch")
    verified = {}
    for relative, expected in AUTHORITIES.items():
        actual = sha256(ROOT / relative)
        require(actual == expected, f"authority hash mismatch: {relative}")
        verified[relative] = actual

    counterfamily = record_counterfamily()
    source_rows = shared_source_compressions()

    result = {
        "schema": "stage8-t7-primitive-connected-scalarization-dichotomy-v001",
        "spec_sha256": SPEC_SHA256,
        "authority_sha256": verified,
        "target_value_used": False,
        "D1_record_line_relay": {
            "line_endomorphisms_are_scalars": True,
            "relay_composition_multiplies_cell_scalars": True,
            "product_is_disconnected_completion_only": True,
            "connected_counterfamily": counterfamily,
        },
        "D2_shared_source_compressions": source_rows,
        "D3": {
            "connected_operator_uniquely_fixed_by_line_data": False,
            "shared_source_endpoint_compression_is_scalar": False,
            "source_scalar_functional_uniquely_fixed_in_primitive_scope": False,
            "normalized_trace_has_nonzero_all_stage_baseline": False,
            "causal_final_source_line_derived_as_public_endpoint": False,
        },
        "verdict": "PRIMITIVE_CONNECTED_SCALARIZATION_UNDERDETERMINED",
        "reason": (
            "The relayed line category fixes the disconnected product but "
            "does not fix connected dynamics. The connected shared-source "
            "compression is operator-valued; pre-existing source states give "
            "different scalars, the normalized trace vanishes at N=3, and "
            "the nonzero causal-line functional requires an unproved final "
            "source boundary."
        ),
        "connected_primitive_amplitude_derived": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
