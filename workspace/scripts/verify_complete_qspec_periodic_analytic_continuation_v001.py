#!/usr/bin/env python3
"""Independent analytic-continuation and reduced-transfer verifier."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = (
    ROOT
    / "COMPLETE_QSPEC_ANALYTIC_CONTINUATION_INDEPENDENT_VERIFIER_PROTOCOL_V001.md"
)
PRIMARY = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_periodic_analytic_continuation_v004.json"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_periodic_analytic_continuation_verification_v001.json"
)

EXPECTED = {
    PROTOCOL:
        "e5630cbc9d5d92607773ebb5fc8f8a90075f437d8131311e7d1ec6f5bb84ce0e",
    ROOT / "COMPLETE_QSPEC_ANALYTIC_CONTINUATION_DERIVATIVE_REPAIR_SPEC_V001.md":
        "5065836ae6162cdcc609b3a0058777a54322c90fb551ab7d037855646a53cdd0",
    ROOT / "scripts/derive_complete_qspec_periodic_analytic_continuation_v004.py":
        "4f9ca24625f8cb96027ba8863d6910892250e1c709b1a1d57c0c66534bff2a99",
    PRIMARY:
        "e7fefe80f447e464a320f16840f2fdf2a32b70ce93bda6f0a25d02c379f97a54",
    ROOT / "COMPLETE_QSPEC_COMPLEX_CONTINUATION_CONJUGATION_ERRATUM_V001.md":
        "f706a4ab85f5863b87f6f5591a6907b25164cc6bebc6484e87b67a04bfc107b4",
}

STEPS = 96
RADIUS = 1.0 / 100.0
BOUNDARY_ANGLES = 64
SELECTED_BOUNDARY_INDICES = (0, 8, 16, 24, 32, 40, 48, 56)
VOLUMES = (1, 2, 8, 64)
REAL_AXIS_POINTS = (
    -1.0 / 100.0,
    -1.0 / 200.0,
    0.0,
    1.0 / 200.0,
    1.0 / 100.0,
)
CR_POINTS = (
    0.0 + 1j / 200.0,
    (1.0 + 1.0j) / (200.0 * math.sqrt(2.0)),
    (-1.0 + 2.0j) / 1000.0,
)
CR_STEPS = (1e-5, 5e-6)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dirac_operators() -> tuple[np.ndarray, np.ndarray]:
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma_0 = np.block([[identity, zero], [zero, -identity]])
    spatial = tuple(
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sigma_x, sigma_y, sigma_z)
    )
    gamma_5 = 1j * gamma_0 @ spatial[0] @ spatial[1] @ spatial[2]
    return gamma_0 @ spatial[0], -1j * gamma_0 @ gamma_5


def directed_difference(theta: complex) -> np.ndarray:
    matrix = np.zeros((3, 3), dtype=complex)
    forward = np.exp(1j * theta / 3.0)
    backward = np.exp(-1j * theta / 3.0)
    for site in range(3):
        matrix[site, (site + 1) % 3] += forward / 2.0
        matrix[site, (site - 1) % 3] -= backward / 2.0
    return matrix


def directed_difference_derivative(theta: complex) -> np.ndarray:
    matrix = np.zeros((3, 3), dtype=complex)
    forward = np.exp(1j * theta / 3.0)
    backward = np.exp(-1j * theta / 3.0)
    for site in range(3):
        matrix[site, (site + 1) % 3] += (1j / 6.0) * forward
        matrix[site, (site - 1) % 3] += (1j / 6.0) * backward
    return matrix


def conjugate_based_difference(theta: complex) -> np.ndarray:
    matrix = np.zeros((3, 3), dtype=complex)
    phase = np.exp(1j * theta / 3.0)
    for site in range(3):
        matrix[site, (site + 1) % 3] += phase / 2.0
        matrix[site, (site - 1) % 3] -= phase.conjugate() / 2.0
    return matrix


def dgamma(
    one_body: np.ndarray,
    particles: int,
) -> tuple[np.ndarray, tuple[tuple[int, ...], ...]]:
    dimension = one_body.shape[0]
    basis = tuple(itertools.combinations(range(dimension), particles))
    lookup = {occupation: row for row, occupation in enumerate(basis)}
    lifted = np.zeros((len(basis), len(basis)), dtype=complex)
    for column, occupation in enumerate(basis):
        for q_position, q_mode in enumerate(occupation):
            reduced = list(occupation)
            reduced.pop(q_position)
            q_sign = -1 if q_position % 2 else 1
            for p_mode in range(dimension):
                if p_mode in reduced:
                    continue
                p_position = sum(mode < p_mode for mode in reduced)
                p_sign = -1 if p_position % 2 else 1
                output = tuple(sorted((*reduced, p_mode)))
                lifted[lookup[output], column] += (
                    q_sign
                    * p_sign
                    * one_body[p_mode, q_mode]
                )
    return lifted, basis


def expm_taylor(matrix: np.ndarray) -> np.ndarray:
    """Taylor scaling-and-squaring, independent of the producer's Pade path."""
    norm_one = float(np.linalg.norm(matrix, 1))
    scaling = (
        max(0, int(math.ceil(math.log2(norm_one / 0.25))))
        if norm_one > 0.25
        else 0
    )
    value = matrix / (2 ** scaling)
    identity = np.eye(value.shape[0], dtype=complex)
    result = identity.copy()
    term = identity.copy()
    for order in range(1, 81):
        term = term @ value / order
        result += term
        if np.linalg.norm(term, 1) < 1e-17 * max(
            np.linalg.norm(result, 1),
            1.0,
        ):
            break
    for _ in range(scaling):
        result = result @ result
    return result


def diamond_weight(time: float) -> float:
    return 32.0 * min(time, 1.0 - time) ** 3


def apply_free(state: np.ndarray, free_step: np.ndarray) -> np.ndarray:
    source_dimension, record_dimension, input_dimension = state.shape
    flat = state.reshape(
        source_dimension,
        record_dimension * input_dimension,
    )
    return (free_step @ flat).reshape(state.shape)


def apply_interaction(
    state: np.ndarray,
    source_vectors: np.ndarray,
    source_values: np.ndarray,
    record_vectors: np.ndarray,
    record_values: np.ndarray,
    interval: float,
) -> np.ndarray:
    coordinates = np.einsum(
        "as,sri,rb->abi",
        source_vectors.conjugate().T,
        state,
        record_vectors.conjugate(),
        optimize=True,
    )
    phases = np.exp(
        -1j
        * interval
        * source_values[:, np.newaxis]
        * record_values[np.newaxis, :]
    )
    return np.einsum(
        "sa,abi,br->sri",
        source_vectors,
        phases[:, :, np.newaxis] * coordinates,
        record_vectors.T,
        optimize=True,
    )


def cell_kraus(
    free: np.ndarray,
    interaction: np.ndarray,
    record: np.ndarray,
) -> tuple[np.ndarray, ...]:
    source_dimension = free.shape[0]
    record_dimension = record.shape[0]
    source_values, source_vectors = np.linalg.eigh(interaction)
    record_values, record_vectors = np.linalg.eigh(record)
    half_free = expm_taylor(-0.5j * free / STEPS)
    state = np.zeros(
        (source_dimension, record_dimension, source_dimension),
        dtype=complex,
    )
    state[:, 0, :] = np.eye(source_dimension, dtype=complex)
    action = math.pi / math.sqrt(2.0)
    for index in range(STEPS):
        midpoint = (index + 0.5) / STEPS
        state = apply_free(state, half_free)
        state = apply_interaction(
            state,
            source_vectors,
            source_values,
            record_vectors,
            record_values,
            action * diamond_weight(midpoint) / STEPS,
        )
        state = apply_free(state, half_free)
    return tuple(
        state[:, outcome, :]
        for outcome in range(record_dimension)
    )


def build_parent() -> dict[str, object]:
    alpha_x, incidence_spin = dirac_operators()
    full_zero = np.kron(-1j * directed_difference(0.0), alpha_x)
    eigenvalues, eigenvectors = np.linalg.eigh(full_zero)
    active = np.abs(eigenvalues) > 1e-12
    active_values = eigenvalues[active]
    active_vectors = eigenvectors[:, active]

    masks = (
        np.diag([1.0, 1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, 1.0]).astype(complex),
    )
    interactions = tuple(
        dgamma(
            active_vectors.conjugate().T
            @ np.kron(mask, incidence_spin)
            @ active_vectors,
            4,
        )[0]
        for mask in masks
    )
    free_zero, basis = dgamma(np.diag(active_values), 4)
    occupied = tuple(
        index for index, value in enumerate(active_values)
        if value < 0.0
    )
    source_row = basis.index(occupied)
    source_vector = np.zeros(len(basis), dtype=complex)
    source_vector[source_row] = 1.0
    density = np.outer(source_vector, source_vector.conjugate())
    record = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )

    def lift(difference) -> np.ndarray:
        full = np.kron(-1j * difference, alpha_x)
        one_body = active_vectors.conjugate().T @ full @ active_vectors
        return dgamma(one_body, 4)[0]

    return {
        "source_dimension": len(basis),
        "source_vector": source_vector,
        "density": density,
        "record": record,
        "interactions": interactions,
        "free_zero": free_zero,
        "free": lambda theta: lift(directed_difference(theta)),
        "free_derivative":
            lambda theta: lift(directed_difference_derivative(theta)),
        "bad_free": lambda theta: lift(conjugate_based_difference(theta)),
    }


def composite_kraus(
    cells: tuple[tuple[np.ndarray, ...], ...],
) -> tuple[np.ndarray, ...]:
    return tuple(
        second @ first
        for first in cells[0]
        for second in cells[1]
    )


def reachable_support(
    source_vector: np.ndarray,
    zero_composites: tuple[np.ndarray, ...],
) -> tuple[np.ndarray, float]:
    basis = source_vector[:, np.newaxis]
    for _ in range(16):
        candidates = np.column_stack(
            (basis, *(operator @ basis for operator in zero_composites))
        )
        left, singular, _ = np.linalg.svd(
            candidates,
            full_matrices=False,
        )
        next_basis = left[:, singular > 1e-11]
        if next_basis.shape[1] == basis.shape[1]:
            basis = next_basis
            break
        basis = next_basis
    projector = basis @ basis.conjugate().T
    residual = max(
        np.linalg.norm(
            (np.eye(projector.shape[0]) - projector)
            @ operator
            @ basis
        )
        for operator in zero_composites
    )
    return basis, float(residual)


def reduced_transfer(
    branch_composites: tuple[np.ndarray, ...],
    zero_composites: tuple[np.ndarray, ...],
    support: np.ndarray,
) -> np.ndarray:
    zero_reduced = tuple(
        support.conjugate().T @ operator @ support
        for operator in zero_composites
    )
    return sum(
        np.kron(left, right.conjugate())
        for left, right in zip(branch_composites, zero_reduced)
    )


def direct_amplitudes(
    density: np.ndarray,
    branch_composites: tuple[np.ndarray, ...],
    zero_composites: tuple[np.ndarray, ...],
) -> dict[int, complex]:
    value = density.copy()
    rows = {}
    for volume in range(1, max(VOLUMES) + 1):
        value = sum(
            left @ value @ right.conjugate().T
            for left, right in zip(
                branch_composites,
                zero_composites,
            )
        )
        if volume in VOLUMES or volume <= 4:
            rows[volume] = complex(np.trace(value))
    return rows


def point_key(point: complex) -> str:
    return f"{point.real:+.12f}_{point.imag:+.12f}i"


def producer_z64(primary: dict[str, object], point: complex) -> complex:
    row = primary["sample_summaries_fine_steps"][point_key(point)]["z64"]
    return complex(row["real"], row["imag"])


def derivative_rows(parent: dict[str, object]) -> tuple[dict, float, float]:
    rows = {}
    maximum_repaired = 0.0
    maximum_bad = 0.0
    for point in CR_POINTS:
        point_rows = []
        for step in CR_STEPS:
            derivative_x = (
                parent["free"](point + step)
                - parent["free"](point - step)
            ) / (2.0 * step)
            derivative_y = (
                parent["free"](point + 1j * step)
                - parent["free"](point - 1j * step)
            ) / (2.0 * step)
            exact = parent["free_derivative"](point)
            denominator = max(np.linalg.norm(exact), 1e-30)
            values = {
                "x_vs_exact": float(
                    np.linalg.norm(derivative_x - exact) / denominator
                ),
                "y_vs_i_exact": float(
                    np.linalg.norm(derivative_y - 1j * exact)
                    / denominator
                ),
                "cauchy_riemann": float(
                    np.linalg.norm(derivative_y - 1j * derivative_x)
                    / max(
                        np.linalg.norm(derivative_x),
                        np.linalg.norm(derivative_y),
                        1e-30,
                    )
                ),
            }
            maximum_repaired = max(maximum_repaired, *values.values())
            bad_x = (
                parent["bad_free"](point + step)
                - parent["bad_free"](point - step)
            ) / (2.0 * step)
            bad_y = (
                parent["bad_free"](point + 1j * step)
                - parent["bad_free"](point - 1j * step)
            ) / (2.0 * step)
            bad = float(
                np.linalg.norm(bad_y - 1j * bad_x)
                / max(
                    np.linalg.norm(bad_x),
                    np.linalg.norm(bad_y),
                    1e-30,
                )
            )
            maximum_bad = max(maximum_bad, bad)
            point_rows.append(
                {
                    "step": step,
                    "repaired": values,
                    "conjugate_negative_control": bad,
                }
            )
        rows[point_key(point)] = point_rows
    return rows, maximum_repaired, maximum_bad


def spectral_row(
    transfer: np.ndarray,
    start: np.ndarray,
    trace_functional: np.ndarray,
) -> dict[str, object]:
    eigenvalues, right_vectors = np.linalg.eig(transfer)
    order = np.argsort(-np.abs(eigenvalues))
    leading_index = int(order[0])
    second_index = int(order[1])
    leading = complex(eigenvalues[leading_index])
    second = complex(eigenvalues[second_index])
    right = right_vectors[:, leading_index]

    left_values, left_vectors = np.linalg.eig(transfer.conjugate().T)
    left_index = int(
        np.argmin(np.abs(left_values - np.conjugate(leading)))
    )
    left = left_vectors[:, left_index]
    left /= np.conjugate(np.vdot(left, right))

    projector = np.outer(right, left.conjugate())
    remainder = transfer - leading * projector
    coefficient = (
        (trace_functional @ right)
        * (left.conjugate() @ start)
    )
    q_ratio = float(np.linalg.norm(remainder, 2) / abs(leading))
    dominance = float(
        np.linalg.norm(trace_functional)
        * np.linalg.norm(start)
        * q_ratio ** 5
        / abs(coefficient)
    )
    relative_gap = float(
        (abs(leading) - abs(second)) / abs(leading)
    )
    projector_error = float(
        max(
            np.linalg.norm(projector @ projector - projector),
            np.linalg.norm(transfer @ projector - leading * projector),
            np.linalg.norm(projector @ transfer - leading * projector),
        )
    )
    return {
        "leading_eigenvalue": {
            "real": leading.real,
            "imag": leading.imag,
            "absolute": abs(leading),
        },
        "second_modulus": abs(second),
        "relative_modulus_gap": relative_gap,
        "projector_error": projector_error,
        "leading_coefficient_absolute": abs(coefficient),
        "remainder_norm_ratio": q_ratio,
        "N_ge_5_dominance_bound": dominance,
        "pass": bool(
            relative_gap > 0.25
            and projector_error < 1e-10
            and abs(coefficient) > 0.95
            and q_ratio < 0.85
            and dominance < 1.0
        ),
    }


def main() -> None:
    for path, expected in EXPECTED.items():
        if sha256(path) != expected:
            raise RuntimeError(f"authority drift: {path.name}")
    primary = json.loads(PRIMARY.read_text())
    parent = build_parent()

    hermiticity_errors = {
        f"{theta:+.8f}": float(
            np.linalg.norm(
                parent["free"](theta)
                - parent["free"](theta).conjugate().T
            )
        )
        for theta in REAL_AXIS_POINTS
    }
    derivative, maximum_derivative, maximum_bad = derivative_rows(parent)
    analytic_pass = bool(
        max(hermiticity_errors.values()) < 1e-12
        and maximum_derivative < 1e-8
        and maximum_bad > 1e-3
    )

    zero_cells = tuple(
        cell_kraus(
            parent["free_zero"],
            interaction,
            parent["record"],
        )
        for interaction in parent["interactions"]
    )
    zero_composites = composite_kraus(zero_cells)
    support, invariance = reachable_support(
        parent["source_vector"],
        zero_composites,
    )
    support_pass = bool(
        support.shape[1] == 5
        and invariance < 1e-11
    )

    start = (parent["density"] @ support).reshape(-1)
    trace_functional = support.conjugate().reshape(-1)
    selected_points = tuple(
        RADIUS * np.exp(
            2j * math.pi * index / BOUNDARY_ANGLES
        )
        for index in SELECTED_BOUNDARY_INDICES
    )
    rows = {}
    all_rows_pass = True
    for point in selected_points:
        branch_cells = tuple(
            cell_kraus(
                parent["free"](point),
                interaction,
                parent["record"],
            )
            for interaction in parent["interactions"]
        )
        branch_composites = composite_kraus(branch_cells)
        transfer = reduced_transfer(
            branch_composites,
            zero_composites,
            support,
        )
        direct = direct_amplitudes(
            parent["density"],
            branch_composites,
            zero_composites,
        )
        reduced_errors = {}
        for volume in VOLUMES:
            reduced = complex(
                trace_functional
                @ np.linalg.matrix_power(transfer, volume)
                @ start
            )
            reduced_errors[str(volume)] = float(
                abs(reduced - direct[volume])
                / max(abs(direct[volume]), 1e-30)
            )
        maximum_reduced_error = max(reduced_errors.values())
        producer = producer_z64(primary, point)
        producer_error = float(
            abs(direct[64] - producer) / max(abs(producer), 1e-30)
        )
        finite_minimum = min(abs(direct[volume]) for volume in range(1, 5))
        spectral = spectral_row(
            transfer,
            start,
            trace_functional,
        )
        row_pass = bool(
            maximum_reduced_error < 1e-10
            and producer_error < 1e-9
            and finite_minimum > 0.95
            and spectral["pass"]
        )
        all_rows_pass = all_rows_pass and row_pass
        rows[point_key(point)] = {
            "reduced_direct_relative_errors": reduced_errors,
            "maximum_reduced_direct_relative_error":
                maximum_reduced_error,
            "producer_N64_relative_error": producer_error,
            "minimum_direct_amplitude_N1_to_N4": finite_minimum,
            "spectral": spectral,
            "pass": row_pass,
        }

    zero_direct = direct_amplitudes(
        parent["density"],
        zero_composites,
        zero_composites,
    )
    zero_transfer = reduced_transfer(
        zero_composites,
        zero_composites,
        support,
    )
    zero_errors = {}
    for volume in VOLUMES:
        reduced = complex(
            trace_functional
            @ np.linalg.matrix_power(zero_transfer, volume)
            @ start
        )
        zero_errors[str(volume)] = max(
            abs(zero_direct[volume] - 1.0),
            abs(reduced - 1.0),
            abs(reduced - zero_direct[volume]),
        )
    zero_pass = max(zero_errors.values()) < 1e-11

    passed = bool(
        analytic_pass
        and support_pass
        and all_rows_pass
        and zero_pass
    )
    result = {
        "schema":
            "complete_qspec_periodic_analytic_continuation_verification_v001",
        "protocol_sha256": sha256(PROTOCOL),
        "primary_sha256": sha256(PRIMARY),
        "independent_exponential":
            "Taylor_scaling_and_squaring",
        "real_axis_hermiticity_errors": hermiticity_errors,
        "derivative_checks": derivative,
        "maximum_repaired_derivative_residual": maximum_derivative,
        "maximum_conjugate_negative_control_residual": maximum_bad,
        "analytic_pass": analytic_pass,
        "zero_history_reachable_support_dimension":
            int(support.shape[1]),
        "zero_history_maximum_invariance_residual": invariance,
        "zero_history_support_pass": support_pass,
        "relative_operator_shape": [70, 5],
        "dense_transfer_shape": [350, 350],
        "selected_complex_rows": rows,
        "selected_complex_rows_pass": all_rows_pass,
        "zero_history_volume_errors": zero_errors,
        "zero_history_pass": zero_pass,
        "verdict": (
            "INDEPENDENT_PERIODIC_ANALYTIC_CONTINUATION_CONFIRMED"
            if passed
            else "INDEPENDENT_PERIODIC_ANALYTIC_CONTINUATION_BLOCKED"
        ),
        "pass": passed,
        "independent_analytic_continuation_confirmed": passed,
        "sampled_point_all_volume_dominance_confirmed":
            passed,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "verdict": result["verdict"],
                "support_dimension":
                    result["zero_history_reachable_support_dimension"],
                "support_invariance":
                    result["zero_history_maximum_invariance_residual"],
                "maximum_derivative_residual": maximum_derivative,
                "selected_complex_rows_pass": all_rows_pass,
                "alpha_computed": False,
            },
            indent=2,
            sort_keys=True,
        )
    )
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
