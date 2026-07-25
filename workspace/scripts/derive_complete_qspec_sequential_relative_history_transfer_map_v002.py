#!/usr/bin/env python3
"""Derive and verify the strictly sequential Qspec relative-history map."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = (
    ROOT
    / "COMPLETE_QSPEC_RELATIVE_HISTORY_TRANSFER_MAP_REPAIR_SPEC_V001.md"
)
INDUCTION = (
    ROOT
    / "COMPLETE_QSPEC_SEQUENTIAL_TRANSFER_INDUCTION_PROOF_V001.md"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_sequential_relative_history_transfer_map_v002.json"
)

EXPECTED = {
    SPEC:
        "b6337e4697e3487f927b9bc324d00a5c5a3f245d98bd8cde1833cdf62ee49357",
    INDUCTION:
        "5fc923b9ecca5ee6e63fe8faa50047d72747ebaf09646b14b03affc48a6e84a3",
    ROOT / "COMPLETE_QSPEC_RELATIVE_HISTORY_TRANSFER_MAP_SPEC_V001.md":
        "7e79583981dd97b2fb5e0ebb6a3498b7bdc03a29cb46f8e2c654f62bc52315ef",
    ROOT / "COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_RESULT_V001.md":
        "273e1473a1a8bf0be0467634411cec1b7daeee0c9f24c330fad5d288d191dcbb",
    ROOT / "COMPLETE_QSPEC_TEMPORAL_PLAQUETTE_RESPONSE_RESULT_V001.md":
        "082a56a6cac2be75322209626a6086901cad7b5e9900cf1d1d021e99b46b7b0c",
    ROOT / "STAGE8_T7_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_RESULT_V001.md":
        "907a274ab3a43766f8ed0250561284952dd1cd6fb3adb68330a97286dc2423f6",
    ROOT / "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def dirac_operators() -> tuple[np.ndarray, np.ndarray]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma0 = np.block([[identity, zero], [zero, -identity]])
    spatial = tuple(
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    )
    gamma5 = 1j * gamma0 @ spatial[0] @ spatial[1] @ spatial[2]
    return gamma0 @ spatial[0], -1j * gamma0 @ gamma5


def covariant_difference(theta: float) -> np.ndarray:
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


def diamond_weight(time: float) -> float:
    return 32.0 * min(time, 1.0 - time) ** 3


def apply_free_tensor(
    state: np.ndarray,
    half_free: np.ndarray,
) -> np.ndarray:
    source_dimension, record_dimension, input_dimension = state.shape
    flat = state.reshape(
        source_dimension,
        record_dimension * input_dimension,
    )
    return (half_free @ flat).reshape(state.shape)


def apply_interaction_tensor(
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
    steps: int,
) -> tuple[np.ndarray, ...]:
    source_dimension = free.shape[0]
    record_dimension = record.shape[0]
    free_values, free_vectors = np.linalg.eigh(free)
    source_values, source_vectors = np.linalg.eigh(interaction)
    record_values, record_vectors = np.linalg.eigh(record)
    dt = 1.0 / steps
    half_free = (
        free_vectors
        @ np.diag(np.exp(-0.5j * dt * free_values))
        @ free_vectors.conjugate().T
    )
    state = np.zeros(
        (source_dimension, record_dimension, source_dimension),
        dtype=complex,
    )
    state[:, 0, :] = np.eye(source_dimension, dtype=complex)
    action = math.pi / math.sqrt(2.0)
    for index in range(steps):
        midpoint = (index + 0.5) * dt
        state = apply_free_tensor(state, half_free)
        state = apply_interaction_tensor(
            state,
            source_vectors,
            source_values,
            record_vectors,
            record_values,
            action * diamond_weight(midpoint) * dt,
        )
        state = apply_free_tensor(state, half_free)
    return tuple(state[:, outcome, :] for outcome in range(record_dimension))


def apply_interaction_matrix(
    state: np.ndarray,
    source_vectors: np.ndarray,
    source_values: np.ndarray,
    record_vectors: np.ndarray,
    record_values: np.ndarray,
    interval: float,
) -> np.ndarray:
    coordinates = (
        source_vectors.conjugate().T
        @ state
        @ record_vectors.conjugate()
    )
    phases = np.exp(
        -1j
        * interval
        * source_values[:, np.newaxis]
        * record_values[np.newaxis, :]
    )
    return source_vectors @ (phases * coordinates) @ record_vectors.T


def full_record_pulse(
    state: np.ndarray,
    free: np.ndarray,
    interaction: np.ndarray,
    record: np.ndarray,
    steps: int,
) -> np.ndarray:
    dt = 1.0 / steps
    free_values, free_vectors = np.linalg.eigh(free)
    source_values, source_vectors = np.linalg.eigh(interaction)
    record_values, record_vectors = np.linalg.eigh(record)
    half_free = (
        free_vectors
        @ np.diag(np.exp(-0.5j * dt * free_values))
        @ free_vectors.conjugate().T
    )
    action = math.pi / math.sqrt(2.0)
    value = state.copy()
    for index in range(steps):
        midpoint = (index + 0.5) * dt
        value = half_free @ value
        value = apply_interaction_matrix(
            value,
            source_vectors,
            source_values,
            record_vectors,
            record_values,
            action * diamond_weight(midpoint) * dt,
        )
        value = half_free @ value
    return value


def compose_cross_map(
    source_cross_density: np.ndarray,
    plus_kraus: tuple[np.ndarray, ...],
    minus_kraus: tuple[np.ndarray, ...],
) -> np.ndarray:
    return sum(
        plus
        @ source_cross_density
        @ minus.conjugate().T
        for plus, minus in zip(plus_kraus, minus_kraus)
    )


def main() -> None:
    for path, expected in EXPECTED.items():
        require(sha256(path) == expected, f"authority drift: {path.name}")

    alpha_x, incidence_spin = dirac_operators()
    full_zero = np.kron(
        -1j * covariant_difference(0.0),
        alpha_x,
    )
    eigenvalues, eigenvectors = np.linalg.eigh(full_zero)
    active = np.abs(eigenvalues) > 1e-12
    active_values = eigenvalues[active]
    active_vectors = eigenvectors[:, active]
    require(active_values.shape[0] == 8, "wrong active dimension")

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

    theta = 1.0 / 40.0
    full_plus = np.kron(
        -1j * covariant_difference(theta),
        alpha_x,
    )
    free_plus = dgamma(
        active_vectors.conjugate().T @ full_plus @ active_vectors,
        4,
    )[0]

    record_seed = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    identity_record = np.eye(3, dtype=complex)
    full_records = (
        np.kron(record_seed, identity_record),
        np.kron(identity_record, record_seed),
    )

    occupied = tuple(
        index for index, value in enumerate(active_values)
        if value < 0.0
    )
    source_row = basis.index(occupied)
    source_vector = np.zeros(len(basis), dtype=complex)
    source_vector[source_row] = 1.0
    source_density = np.outer(source_vector, source_vector.conjugate())

    steps = 64
    plus_kraus = tuple(
        cell_kraus(free_plus, interaction, record_seed, steps)
        for interaction in interactions
    )
    minus_kraus = tuple(
        cell_kraus(free_zero, interaction, record_seed, steps)
        for interaction in interactions
    )

    kraus_completeness_errors: dict[str, float] = {}
    identity_source = np.eye(len(basis), dtype=complex)
    for branch_name, branch in (
        ("plus", plus_kraus),
        ("minus", minus_kraus),
    ):
        for cell, kraus in enumerate(branch):
            gram = sum(
                operator.conjugate().T @ operator
                for operator in kraus
            )
            kraus_completeness_errors[
                f"{branch_name}_cell_{cell}"
            ] = float(np.linalg.norm(gram - identity_source))

    transferred = source_density.copy()
    for cell in range(2):
        transferred = compose_cross_map(
            transferred,
            plus_kraus[cell],
            minus_kraus[cell],
        )
    z_transfer = complex(np.trace(transferred))

    full_initial = np.zeros((len(basis), 9), dtype=complex)
    full_initial[source_row, 0] = 1.0
    full_plus_state = full_initial.copy()
    full_minus_state = full_initial.copy()
    for cell in range(2):
        full_plus_state = full_record_pulse(
            full_plus_state,
            free_plus,
            interactions[cell],
            full_records[cell],
            steps,
        )
        full_minus_state = full_record_pulse(
            full_minus_state,
            free_zero,
            interactions[cell],
            full_records[cell],
            steps,
        )
    z_full = complex(np.vdot(full_minus_state, full_plus_state))
    transfer_full_error = abs(z_transfer - z_full)

    diagonal = source_density.copy()
    for cell in range(2):
        diagonal = compose_cross_map(
            diagonal,
            plus_kraus[cell],
            plus_kraus[cell],
        )
    diagonal_trace_error = abs(complex(np.trace(diagonal)) - 1.0)

    # Frozen nonsymmetric operator probe for chronology sensitivity.
    probe_indices = np.arange(1, len(basis) + 1, dtype=float)
    probe_a = (
        probe_indices
        + 1j * ((probe_indices.astype(int) % 5) - 2)
    ).astype(complex)
    probe_b = (
        ((probe_indices.astype(int) % 7) - 3)
        + 1j * (len(basis) + 1 - probe_indices)
    ).astype(complex)
    probe_a /= np.linalg.norm(probe_a)
    probe_b /= np.linalg.norm(probe_b)
    probe_cross = np.outer(probe_a, probe_b.conjugate())

    probe_plus_state = np.zeros((len(basis), 9), dtype=complex)
    probe_minus_state = np.zeros((len(basis), 9), dtype=complex)
    probe_plus_state[:, 0] = probe_a
    probe_minus_state[:, 0] = probe_b
    for cell in range(2):
        probe_plus_state = full_record_pulse(
            probe_plus_state,
            free_plus,
            interactions[cell],
            full_records[cell],
            steps,
        )
        probe_minus_state = full_record_pulse(
            probe_minus_state,
            free_zero,
            interactions[cell],
            full_records[cell],
            steps,
        )
    probe_full_cross = (
        probe_plus_state @ probe_minus_state.conjugate().T
    )

    probe_ordered = probe_cross.copy()
    for cell in range(2):
        probe_ordered = compose_cross_map(
            probe_ordered,
            plus_kraus[cell],
            minus_kraus[cell],
        )
    probe_reversed = probe_cross.copy()
    for cell in (1, 0):
        probe_reversed = compose_cross_map(
            probe_reversed,
            plus_kraus[cell],
            minus_kraus[cell],
        )
    probe_scale = max(np.linalg.norm(probe_full_cross), 1e-30)
    ordered_operator_relative_error = float(
        np.linalg.norm(probe_ordered - probe_full_cross) / probe_scale
    )
    reversed_operator_relative_difference = float(
        np.linalg.norm(probe_reversed - probe_full_cross) / probe_scale
    )

    passed = bool(
        max(kraus_completeness_errors.values()) < 1e-10
        and transfer_full_error < 1e-10
        and diagonal_trace_error < 1e-10
        and abs(float(np.linalg.norm(full_plus_state)) - 1.0) < 1e-10
        and abs(float(np.linalg.norm(full_minus_state)) - 1.0) < 1e-10
        and ordered_operator_relative_error < 1e-10
        and reversed_operator_relative_difference > 1e-6
    )
    result = {
        "schema":
            "complete_qspec_sequential_relative_history_transfer_map_v002",
        "spec_sha256": sha256(SPEC),
        "induction_proof_sha256": sha256(INDUCTION),
        "theorem": {
            "per_cell_cross_map":
                "T_c(X)=Tr_R[U_c^+(X tensor |r><r|)U_c^-dagger]",
            "kraus_form":
                "T_c(X)=sum_q K_cq^+ X K_cq^-dagger",
            "N_cell_composition":
                "Z_N=Tr_S[(T_N o ... o T_1)(rho_source,in)]",
            "proof_method":
                "frozen_explicit_induction_over_sequential_closed_records",
            "base_case_stated": True,
            "induction_hypothesis_stated": True,
            "partial_trace_commutation_step_stated": True,
            "sequential_history_factorization_stated": True,
            "concurrent_open_record_scope_excluded": True,
            "concurrent_open_records_require_block_map": True,
            "complete_final_identity_retained": True,
            "final_source_ray_inserted": False,
            "record_outcome_postselected": False,
            "determinant_used": False,
        },
        "physical_regression": {
            "theta_plus": theta,
            "theta_minus": 0.0,
            "steps_per_cell": steps,
            "source_dimension": len(basis),
            "single_record_dimension": 3,
            "full_two_record_dimension": 9,
            "z_transfer_real": z_transfer.real,
            "z_transfer_imag": z_transfer.imag,
            "z_full_real": z_full.real,
            "z_full_imag": z_full.imag,
            "transfer_full_error": transfer_full_error,
            "diagonal_trace_error": diagonal_trace_error,
            "kraus_completeness_errors": kraus_completeness_errors,
            "full_plus_norm_error":
                abs(float(np.linalg.norm(full_plus_state)) - 1.0),
            "full_minus_norm_error":
                abs(float(np.linalg.norm(full_minus_state)) - 1.0),
        },
        "order_sensitive_operator_regression": {
            "probe_definition":
                "a_k=k+i((k mod 5)-2); "
                "b_k=((k mod 7)-3)+i(d+1-k); separately normalized",
            "ordered_operator_relative_error":
                ordered_operator_relative_error,
            "reversed_operator_relative_difference":
                reversed_operator_relative_difference,
            "ordered_threshold": 1e-10,
            "reversed_negative_control_threshold": 1e-6,
            "ordered_pass": ordered_operator_relative_error < 1e-10,
            "reversed_negative_control_pass":
                reversed_operator_relative_difference > 1e-6,
        },
        "verdict": (
            "COMPLETE_QSPEC_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_DERIVED"
            if passed
            else
            "COMPLETE_QSPEC_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_BLOCKED"
        ),
        "pass": passed,
        "complete_Qspec_CTP_scalar_closure_derived": True,
        "sequential_relative_history_transfer_map_derived": passed,
        "concurrent_open_record_block_map_derived": False,
        "connected_K_cell_amplitude_constructed": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "local_Maxwell_response_derived": False,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
