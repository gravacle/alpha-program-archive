#!/usr/bin/env python3
"""Expanded independent verification of every exact-state envelope case."""

from __future__ import annotations

import hashlib
import json
import math
from decimal import Decimal, getcontext
from pathlib import Path

import numpy as np

import verify_stage8_t7_hermite_galerkin_baseline_v001 as independent


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_EXACT_STATE_ENVELOPE_COMPARISON_SPEC_V001.md"
PRIMARY = ROOT / "stage8_execution/work/T07_exact_state_envelope_comparison.json"
EXACT = ROOT / "stage8_execution/work/T07_exact_hermite_mixed_covariance.npz"
HISTORIES = ROOT / "stage8_execution/work/T07_exact_state_envelope_histories.npz"
OUT = ROOT / "stage8_execution/work/T07_exact_state_envelope_comparison_verification.json"

FINITE_FOCK_AUTHORITY = (
    ROOT / "STAGE8_T7_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_RESULT_V001.md"
)
FINITE_FOCK_SHA256 = "907a274ab3a43766f8ed0250561284952dd1cd6fb3adb68330a97286dc2423f6"

UNITARY_TOLERANCE = 3e-10
DETERMINANT_TOLERANCE = 3e-10
AMPLITUDE_TOLERANCE = 3e-10
DECIMAL_PRECISION = 90


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def envelope(mode: str, midpoint: float) -> float:
    tau = math.pi / math.sqrt(2.0)
    if mode == "ER-A":
        radius = min(midpoint, 1.0 - midpoint)
        return tau * 32.0 * radius**3
    if mode == "ER-B":
        return tau * 24.0 / math.pi
    raise ValueError(mode)


def apply_spectral_interaction(
    value: np.ndarray,
    multiplication: np.ndarray,
    incidence_values: np.ndarray,
    incidence_vectors: np.ndarray,
    theta: float,
) -> np.ndarray:
    spatial_values, spatial_vectors = np.linalg.eigh(multiplication)
    spatial_dimension = multiplication.shape[0]
    column_dimension = value.shape[1]
    tensor = value.reshape(spatial_dimension, 4, column_dimension)
    tensor = np.einsum(
        "ab,bid->aid", spatial_vectors.conjugate().T, tensor, optimize=True
    )
    tensor = np.einsum(
        "ij,ajd->aid", incidence_vectors.conjugate().T, tensor, optimize=True
    )
    phases = np.exp(
        -1j * theta * spatial_values[:, None] * incidence_values[None, :]
    )
    tensor = phases[:, :, None] * tensor
    tensor = np.einsum(
        "ij,ajd->aid", incidence_vectors, tensor, optimize=True
    )
    tensor = np.einsum(
        "ab,bid->aid", spatial_vectors, tensor, optimize=True
    )
    return tensor.reshape(value.shape)


def independent_histories(
    n: int,
    ell: float,
    mode: str,
    alpha: tuple[np.ndarray, ...],
    incidence: np.ndarray,
) -> tuple[np.ndarray, ...]:
    steps = 96
    dt = 1.0 / steps
    h0 = independent.h0_matrix(n, ell, alpha)
    half_free = independent.exp_h(h0, 0.5 * dt)
    free_full = independent.exp_h(h0, 1.0)
    incidence_values, incidence_vectors = np.linalg.eigh(incidence)
    multiplications = tuple(
        independent.ball_matrix(
            min((index + 0.5) / steps, 1.0 - (index + 0.5) / steps),
            n,
            ell,
            10,
            10,
            20,
        )
        for index in range(steps)
    )
    output = []
    for record_value in (-math.sqrt(2.0), 0.0, math.sqrt(2.0)):
        if record_value == 0.0:
            output.append(free_full)
            continue
        value = np.eye(h0.shape[0], dtype=complex)
        for index, multiplication in enumerate(multiplications):
            midpoint = (index + 0.5) / steps
            value = half_free @ value
            value = apply_spectral_interaction(
                value,
                multiplication,
                incidence_values,
                incidence_vectors,
                record_value * envelope(mode, midpoint) * dt,
            )
            value = half_free @ value
        output.append(value)
    return tuple(output)


def determinant_matrix_mixed(covariance: np.ndarray, unitary: np.ndarray) -> np.ndarray:
    return np.eye(covariance.shape[0], dtype=complex) - covariance + covariance @ unitary


def determinant_matrix_pure(occupied: np.ndarray, unitary: np.ndarray) -> np.ndarray:
    return occupied.conjugate().T @ unitary @ occupied


def determinant(matrix: np.ndarray) -> complex:
    sign, logarithm = np.linalg.slogdet(matrix)
    return complex(sign * np.exp(logarithm))


def read_complex(value: dict[str, float]) -> complex:
    return complex(value["real"], value["imag"])


def dc(value: complex) -> tuple[Decimal, Decimal]:
    return Decimal(str(float(value.real))), Decimal(str(float(value.imag)))


def cadd(
    left: tuple[Decimal, Decimal],
    right: tuple[Decimal, Decimal],
) -> tuple[Decimal, Decimal]:
    return left[0] + right[0], left[1] + right[1]


def csub(
    left: tuple[Decimal, Decimal],
    right: tuple[Decimal, Decimal],
) -> tuple[Decimal, Decimal]:
    return left[0] - right[0], left[1] - right[1]


def cmul(
    left: tuple[Decimal, Decimal],
    right: tuple[Decimal, Decimal],
) -> tuple[Decimal, Decimal]:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def cdiv(
    left: tuple[Decimal, Decimal],
    right: tuple[Decimal, Decimal],
) -> tuple[Decimal, Decimal]:
    denominator = right[0] * right[0] + right[1] * right[1]
    return (
        (left[0] * right[0] + left[1] * right[1]) / denominator,
        (left[1] * right[0] - left[0] * right[1]) / denominator,
    )


def decimal_determinant(matrix: np.ndarray) -> complex:
    getcontext().prec = DECIMAL_PRECISION
    work = [[dc(matrix[row, column]) for column in range(matrix.shape[1])]
            for row in range(matrix.shape[0])]
    sign = 1
    determinant_value = (Decimal(1), Decimal(0))
    for column in range(matrix.shape[0]):
        pivot = max(
            range(column, matrix.shape[0]),
            key=lambda row: (
                work[row][column][0] * work[row][column][0]
                + work[row][column][1] * work[row][column][1]
            ),
        )
        if work[pivot][column] == (Decimal(0), Decimal(0)):
            return 0j
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        pivot_value = work[column][column]
        determinant_value = cmul(determinant_value, pivot_value)
        for row in range(column + 1, matrix.shape[0]):
            factor = cdiv(work[row][column], pivot_value)
            for inner in range(column + 1, matrix.shape[0]):
                work[row][inner] = csub(
                    work[row][inner],
                    cmul(factor, work[column][inner]),
                )
    if sign < 0:
        determinant_value = (-determinant_value[0], -determinant_value[1])
    return complex(float(determinant_value[0]), float(determinant_value[1]))


def main() -> None:
    if sha256(FINITE_FOCK_AUTHORITY) != FINITE_FOCK_SHA256:
        raise RuntimeError("Small-Fock Klich authority drift")

    primary = json.loads(PRIMARY.read_text())
    stored_histories = np.load(HISTORIES)
    exact = np.load(EXACT)
    alpha, incidence = independent.gamma_data()
    weights = (-0.25, 0.5, -0.25)

    reports = []
    passed = True
    high_precision_candidates = []
    for case in primary["cases"]:
        n = case["n"]
        ell = case["ell"]
        ell_label = "1" if abs(ell - 1.0) < 1e-15 else "sqrt2"
        h0 = independent.h0_matrix(n, ell, alpha)
        values, vectors = np.linalg.eigh(h0)
        occupied = vectors[:, values < 0.0]
        covariance = exact[f"covariance_n{n}"]

        for mode in ("ER-A", "ER-B"):
            mode_label = mode.replace("-", "_")
            recomputed = independent_histories(n, ell, mode, alpha, incidence)
            stored = tuple(
                stored_histories[
                    f"n{n}_ell{ell_label}_{mode_label}_history{index}"
                ]
                for index in range(3)
            )
            unitary_errors = [
                float(np.linalg.norm(left - right, ord=2))
                for left, right in zip(recomputed, stored)
            ]

            scheme_reports = {}
            for scheme in ("mixed", "pure"):
                if scheme == "mixed":
                    matrices = [
                        determinant_matrix_mixed(covariance, unitary)
                        for unitary in recomputed
                    ]
                else:
                    matrices = [
                        determinant_matrix_pure(occupied, unitary)
                        for unitary in recomputed
                    ]
                terms = [determinant(matrix) for matrix in matrices]
                reported_terms = [
                    read_complex(value)
                    for value in case["branches"][mode]["amplitudes"]["96"][
                        f"{scheme}_history_terms"
                    ]
                ]
                term_errors = [
                    float(abs(left - right))
                    for left, right in zip(terms, reported_terms)
                ]
                completed = sum(
                    weight * term for weight, term in zip(weights, terms)
                )
                reported_completed = read_complex(
                    case["branches"][mode]["amplitudes"]["96"][scheme]
                )
                completed_error = float(abs(completed - reported_completed))
                weighted_magnitude = sum(
                    abs(weight * term) for weight, term in zip(weights, terms)
                )
                cancellation_factor = float(
                    weighted_magnitude / abs(completed)
                    if completed
                    else math.inf
                )
                condition_numbers = [
                    float(np.linalg.cond(matrix)) for matrix in matrices
                ]
                scheme_reports[scheme] = {
                    "history_determinant_errors": term_errors,
                    "completed_amplitude_error": completed_error,
                    "cancellation_factor": cancellation_factor,
                    "determinant_condition_numbers": condition_numbers,
                }
                passed = (
                    passed
                    and max(term_errors) < DETERMINANT_TOLERANCE
                    and completed_error < AMPLITUDE_TOLERANCE
                )
                if n == 2:
                    high_precision_candidates.append(
                        {
                            "n": n,
                            "ell": ell,
                            "mode": mode,
                            "scheme": scheme,
                            "cancellation_factor": cancellation_factor,
                            "matrices": matrices,
                            "double_terms": terms,
                            "double_completed": completed,
                        }
                    )

            passed = passed and max(unitary_errors) < UNITARY_TOLERANCE
            reports.append(
                {
                    "n": n,
                    "ell": ell,
                    "mode": mode,
                    "history_unitary_operator_norm_errors": unitary_errors,
                    "schemes": scheme_reports,
                }
            )

    worst = max(
        high_precision_candidates,
        key=lambda item: item["cancellation_factor"],
    )
    decimal_terms = [
        decimal_determinant(matrix) for matrix in worst["matrices"]
    ]
    decimal_completed = sum(
        weight * term for weight, term in zip(weights, decimal_terms)
    )
    decimal_term_errors = [
        float(abs(left - right))
        for left, right in zip(decimal_terms, worst["double_terms"])
    ]
    decimal_completed_error = float(
        abs(decimal_completed - worst["double_completed"])
    )
    passed = (
        passed
        and max(decimal_term_errors) < 3e-13
        and decimal_completed_error < 3e-13
    )

    result = {
        "schema": "stage8_t7_exact_state_envelope_comparison_verification_v001",
        "spec_sha256": sha256(SPEC),
        "primary_sha256": sha256(PRIMARY),
        "history_artifact_sha256": sha256(HISTORIES),
        "reports": reports,
        "high_precision_worst_cancellation": {
            "n": worst["n"],
            "ell": worst["ell"],
            "mode": worst["mode"],
            "scheme": worst["scheme"],
            "cancellation_factor": worst["cancellation_factor"],
            "decimal_precision": DECIMAL_PRECISION,
            "history_determinant_errors": decimal_term_errors,
            "completed_amplitude_error": decimal_completed_error,
        },
        "small_Fock_Klich_authority_sha256": FINITE_FOCK_SHA256,
        "tolerances": {
            "unitary_operator_norm": UNITARY_TOLERANCE,
            "history_determinant": DETERMINANT_TOLERANCE,
            "completed_amplitude": AMPLITUDE_TOLERANCE,
            "decimal_crosscheck": 3e-13,
        },
        "pass": bool(passed),
        "ER_A_selected": False,
        "ER_B_selected": False,
        "envelope_realization_derived": False,
        "global_determinant_convergence_derived": False,
        "kappa_record_computed": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
