#!/usr/bin/env python3
"""Execute the sealed relayed connected-preparation retest."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_RELAYED_CONNECTED_PREPARATION_RETEST_SPEC_V001.md"
SPEC_SHA256 = "47fe0d5f6b97899ae17a5ea682222fd0ca48f81c16d4e581219af64f6135f111"
OUT = ROOT / "stage8_execution/work/T07_relayed_connected_preparation_retest.json"

AUTHORITIES = {
    "STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md":
        "52401eefc3ff84e22f04bbc329a619b830058661db7f969d2d43d167d97d893d",
    "stage8_execution/t7_relayed_family_resolution/"
    "T07_RELAYED_FAMILY_RESOLUTION_V001.seal.sha256":
        "53c499da21ba2387d1cb235e573bc67c2974331b873d9b93ad2baece467107e4",
    "STAGE8_T7_CONNECTED_ANALYTIC_CLOSURE_SPEC_V001.md":
        "dced9d9ed95601d8524bfbe68ec870a620bfe1cbee5b7c07230a5a9658de945c",
    "STAGE8_T7_CONNECTED_ANALYTIC_CLOSURE_RESULT_V001.md":
        "f891d3afc58e695529d8d569b5d2ba4b853e30c9cfa4296817cb17b60f38b054",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md":
        "345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb",
    "PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md":
        "532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb",
    "STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.md":
        "202f8d8db60046a8069b1cd8fcc38f505eb95fa29578e094e005f56e967c3a35",
    "R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_RESULT_V001.md":
        "1d114e71c29c3a39b7afd1b7a80b47afb52fe77e8ee1e4e19b604defe3c69305",
}

Matrix = list[list[Fraction]]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


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


def trace(matrix: Matrix) -> Fraction:
    return sum((matrix[index][index] for index in range(len(matrix))), Fraction(0))


def projector(vector: tuple[int, ...]) -> Matrix:
    denominator = sum(value * value for value in vector)
    return [
        [
            Fraction(vector[row] * vector[column], denominator)
            for column in range(len(vector))
        ]
        for row in range(len(vector))
    ]


def identity(size: int) -> Matrix:
    return [
        [Fraction(int(row == column)) for column in range(size)]
        for row in range(size)
    ]


def scaled(matrix: Matrix, value: Fraction) -> Matrix:
    return [[value * entry for entry in row] for row in matrix]


def expectation(density: Matrix, operator: Matrix) -> Fraction:
    return trace(matmul(density, operator))


def apply(matrix: Matrix, vector: list[Fraction]) -> list[Fraction]:
    return [
        sum(
            (
                matrix[row][column] * vector[column]
                for column in range(len(vector))
            ),
            Fraction(0),
        )
        for row in range(len(matrix))
    ]


def inner(left: list[Fraction], right: list[Fraction]) -> Fraction:
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def normalized_incidence(vector: tuple[int, ...]) -> list[Fraction]:
    # Keep sqrt(2) outside: vectors below represent sqrt(2)*e_j.
    return [Fraction(value) for value in vector]


def baseline_table() -> dict[str, object]:
    vectors = ((-1, 1, 0, 0), (0, -1, 1, 0), (0, 0, -1, 1))
    projectors = [projector(vector) for vector in vectors]
    densities = {
        "P0": projectors[0],
        "P1": projectors[1],
        "P2": projectors[2],
        "I_over_4": scaled(identity(4), Fraction(1, 4)),
    }

    operators: list[Matrix] = []
    product = identity(4)
    for projector_matrix in projectors:
        product = matmul(projector_matrix, product)
        operators.append(product)

    amplitudes = {
        f"N{index + 1}": {
            label: str(expectation(density, operators[index]))
            for label, density in densities.items()
        }
        for index in range(3)
    }

    # Evaluate <e_(N-1)|K_N|e_0> without irrational coordinates:
    # e_j=v_j/sqrt(2), so the final inner product is
    # (v_final^T K v_0)/2.
    raw_vectors = [normalized_incidence(vector) for vector in vectors]
    in_out = {}
    for index, operator in enumerate(operators):
        evolved = apply(operator, raw_vectors[0])
        in_out[f"N{index + 1}"] = str(
            inner(raw_vectors[index], evolved) / 2
        )

    all_values = [
        Fraction(value)
        for row in amplitudes.values()
        for value in row.values()
    ]
    return {
        "compressed_source_operators": {
            "N1": "P0",
            "N2": "P1 P0",
            "N3": "P2 P1 P0",
        },
        "state_expectation_amplitudes": amplitudes,
        "off_diagonal_in_out_amplitudes": in_out,
        "at_least_one_zero_baseline": any(value == 0 for value in all_values),
        "state_expectations_not_unique": len(set(all_values)) > 1,
        "in_out_functional_is_not_a_state_expectation": True,
    }


def state_selection_audit() -> dict[str, object]:
    return {
        "parent_state_covariance_requires_parent_selected_state": True,
        "ordinary_branch_quasifree_state_status": "DISCLOSED_BRANCH_STATE",
        "finite_energy_charged_excitation_status": "INCOMING_BOUNDARY_DATA",
        "unique_physical_charged_in_state_derived": False,
        "minimal_nonuniqueness_theorem": (
            "On a charged sector of dimension greater than one, distinct "
            "normalized spectral functions of h0 commute with h0 and Q; "
            "stationarity plus charge superselection therefore does not "
            "select one density operator."
        ),
        "relay_selects_source_functional": False,
    }


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "sealed spec hash mismatch")
    for relative, expected in AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"authority drift: {relative}")

    baselines = baseline_table()
    state_audit = state_selection_audit()
    blocked = (
        baselines["at_least_one_zero_baseline"]
        and baselines["state_expectations_not_unique"]
        and not state_audit["unique_physical_charged_in_state_derived"]
        and not state_audit["relay_selects_source_functional"]
    )
    require(blocked, "preparation no-go did not fire")
    result = {
        "schema": "stage8_t7_relayed_connected_preparation_retest_v001",
        "spec_sha256": SPEC_SHA256,
        "P1_P2_exact_baseline_table": baselines,
        "P3_state_selection_audit": state_audit,
        "overall_verdict": "T7_CONNECTED_PREPARATION_BLOCKED_AFTER_RELAY",
        "relay_dependency_resolved": True,
        "relayed_family_resolved": True,
        "connected_preparation_derived": False,
        "all_finite_connected_baselines_nonzero_proved": False,
        "connected_primitive_amplitude_derived": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
