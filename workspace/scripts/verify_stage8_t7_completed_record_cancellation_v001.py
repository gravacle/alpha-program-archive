#!/usr/bin/env python3
"""Independent record-cancellation and finite determinant-history verifier."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_COMPLETED_CONTINUUM_RESPONSE_PROVENANCE_SPEC_V001.md"
SPEC_SHA256 = "6e24ceb6b18e6e6da5a6d21e872f90f6d79a324df9f305d226ab6edec863831b"
PRIMARY = ROOT / "stage8_execution/work/T07_completed_record_cancellation.json"
OUT = ROOT / "stage8_execution/work/T07_completed_record_cancellation_verification.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exp_hermitian(operator: np.ndarray, time: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return vectors @ np.diag(np.exp(-1j * time * values)) @ vectors.conjugate().T


def annihilation(mode_count: int, mode: int) -> np.ndarray:
    dimension = 1 << mode_count
    result = np.zeros((dimension, dimension), dtype=complex)
    lower = (1 << mode) - 1
    for basis in range(dimension):
        if not (basis & (1 << mode)):
            continue
        sign = -1 if bin(basis & lower).count("1") % 2 else 1
        result[basis ^ (1 << mode), basis] = sign
    return result


def fixed_sector_dgamma(one_particle: np.ndarray, particle_count: int) -> np.ndarray:
    mode_count = one_particle.shape[0]
    annihilators = [annihilation(mode_count, mode) for mode in range(mode_count)]
    creators = [operator.conjugate().T for operator in annihilators]
    full = np.zeros((1 << mode_count, 1 << mode_count), dtype=complex)
    for row in range(mode_count):
        for column in range(mode_count):
            full += one_particle[row, column] * creators[row] @ annihilators[column]
    sector = [
        basis for basis in range(1 << mode_count)
        if bin(basis).count("1") == particle_count
    ]
    return full[np.ix_(sector, sector)]


def embed_record(operator: np.ndarray, index: int, count: int) -> np.ndarray:
    result = np.array([[1.0]], dtype=complex)
    for position in range(count):
        result = np.kron(
            result,
            operator if position == index else np.eye(3, dtype=complex),
        )
    return result


def direct_fock_amplitude(
    free: np.ndarray,
    interactions: tuple[np.ndarray, ...],
    durations: tuple[float, ...],
    record: np.ndarray,
) -> complex:
    record_count = len(interactions)
    source_dimension = 6
    record_dimension = 3**record_count
    free_fock = fixed_sector_dgamma(free, 2)
    interaction_fock = tuple(
        fixed_sector_dgamma(interaction, 2) for interaction in interactions
    )
    propagator = np.eye(source_dimension * record_dimension, dtype=complex)
    for index, (interaction, duration) in enumerate(
        zip(interaction_fock, durations)
    ):
        hamiltonian = (
            np.kron(free_fock, np.eye(record_dimension, dtype=complex))
            + np.kron(interaction, embed_record(record, index, record_count))
        )
        propagator = exp_hermitian(hamiltonian, duration) @ propagator

    source_initial = np.zeros(source_dimension, dtype=complex)
    source_initial[0] = 1.0
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    pointer = np.array([0.0, 1.0, 0.0], dtype=complex)
    records_initial = ready
    records_final = pointer
    for _ in range(1, record_count):
        records_initial = np.kron(records_initial, ready)
        records_final = np.kron(records_final, pointer)
    initial = np.kron(source_initial, records_initial)
    final_source_map = np.kron(
        np.eye(source_dimension, dtype=complex),
        records_final.conjugate().reshape(1, -1),
    )
    initial_record_map = np.kron(
        np.eye(source_dimension, dtype=complex),
        records_initial.reshape(-1, 1),
    )
    compressed = final_source_map @ propagator @ initial_record_map
    return complex(np.vdot(source_initial, compressed @ source_initial))


def determinant_history_amplitude(
    free: np.ndarray,
    interactions: tuple[np.ndarray, ...],
    durations: tuple[float, ...],
    record: np.ndarray,
) -> tuple[complex, list[float], list[complex]]:
    values, vectors = np.linalg.eigh(record)
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    pointer = np.array([0.0, 1.0, 0.0], dtype=complex)
    weights = [
        np.vdot(pointer, vectors[:, index]) * np.vdot(vectors[:, index], ready)
        for index in range(3)
    ]
    occupied = np.eye(4, dtype=complex)[:, :2]
    total = 0j
    for history in itertools.product(range(3), repeat=len(interactions)):
        one_particle = np.eye(4, dtype=complex)
        weight = 1 + 0j
        for cell, label in enumerate(history):
            hamiltonian = free + values[label] * interactions[cell]
            one_particle = exp_hermitian(
                hamiltonian, durations[cell]
            ) @ one_particle
            weight *= weights[label]
        total += weight * np.linalg.det(
            occupied.conjugate().T @ one_particle @ occupied
        )
    return complex(total), [float(value) for value in values], weights


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "Sealed specification drift")
    primary = json.loads(PRIMARY.read_text(encoding="utf-8"))
    require(primary["spec_sha256"] == SPEC_SHA256, "Primary spec mismatch")

    record = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    values, vectors = np.linalg.eigh(record)
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    pointer = np.array([0.0, 1.0, 0.0], dtype=complex)
    weights = np.array(
        [
            np.vdot(pointer, vectors[:, index])
            * np.vdot(vectors[:, index], ready)
            for index in range(3)
        ]
    )
    moments = np.array(
        [sum(weights * values**order) for order in range(13)]
    )
    require(np.max(np.abs(values - np.array([-np.sqrt(2), 0, np.sqrt(2)]))) < 1e-14,
            "Independent spectrum mismatch")
    require(abs(moments[0]) < 1e-14, "Independent zeroth moment failed")
    require(abs(moments[1]) < 1e-14, "Independent first moment failed")
    require(abs(moments[2] + 1) < 1e-14, "Independent quadratic moment failed")
    require(np.max(np.abs(moments[1::2])) < 1e-13,
            "Independent odd-moment cancellation failed")

    free = np.diag([-2.0, -0.75, 1.25, 2.5]).astype(complex)
    interactions = (
        np.array(
            [
                [1.0, 0.5, 0.0, -0.25j],
                [0.5, -0.5, 0.375j, 0.0],
                [0.0, -0.375j, 0.25, 0.625],
                [0.25j, 0.0, 0.625, -0.75],
            ],
            dtype=complex,
        ),
        np.array(
            [
                [0.25, -0.2j, 0.4, 0.0],
                [0.2j, 0.75, -0.3, 0.5j],
                [0.4, -0.3, -0.25, 0.1],
                [0.0, -0.5j, 0.1, 0.5],
            ],
            dtype=complex,
        ),
    )
    durations = (0.37, 0.41)
    direct = direct_fock_amplitude(free, interactions, durations, record)
    history, history_values, history_weights = determinant_history_amplitude(
        free, interactions, durations, record
    )
    difference = abs(direct - history)
    require(difference < 2e-13, "Finite determinant-history identity failed")

    result = {
        "schema": "stage8_t7_completed_record_cancellation_verification_v001",
        "spec_sha256": SPEC_SHA256,
        "independent_record_eigenvalues": history_values,
        "independent_record_weights": [
            {"real": float(value.real), "imag": float(value.imag)}
            for value in history_weights
        ],
        "maximum_odd_moment_absolute": float(np.max(np.abs(moments[1::2]))),
        "direct_fock_amplitude": {"real": direct.real, "imag": direct.imag},
        "determinant_history_amplitude": {
            "real": history.real,
            "imag": history.imag,
        },
        "finite_identity_absolute_difference": float(difference),
        "old_three_site_regression_used": False,
        "independent_finite_parent_used": True,
        "c1_exact_record_cancellation_verified": True,
        "c2_finite_stage_identity_verified": True,
        "completed_continuum_response_provenance_derived": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "pass": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
