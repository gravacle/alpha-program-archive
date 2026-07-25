#!/usr/bin/env python3
"""Independent unequal-dimension verifier for the open-record block map."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = (
    ROOT
    / "COMPLETE_QSPEC_OPEN_RECORD_BLOCK_TRANSFER_INDEPENDENT_VERIFIER_PROTOCOL_V001.md"
)
PRIMARY = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_open_record_block_transfer_v001.json"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_open_record_block_transfer_verification_v001.json"
)

EXPECTED = {
    PROTOCOL:
        "241fee2f9ece23523eea45f2f2026212b52e7de6d4947bd69c3301338870d67f",
    ROOT / "COMPLETE_QSPEC_OPEN_RECORD_BLOCK_TRANSFER_MAP_SPEC_V001.md":
        "7bd9b18b1f818cd923472c5911b2b5e0b406faf16fa4345259dffd248d3702d3",
    ROOT / "COMPLETE_QSPEC_OPEN_RECORD_BLOCK_TRANSFER_INDUCTION_PROOF_V001.md":
        "a1db0e42954e639e70bbabe3526d0baaab4082ae892a931832a85e8ac160cee9",
    ROOT / "scripts/derive_complete_qspec_open_record_block_transfer_v001.py":
        "80b437a237dc37b75d0a6ac5bb24bb87a6620ec55f71ca80bae7774f32520fcb",
    PRIMARY:
        "663b6d6b0adbaff98a04a51d49337de07d4b6afe348f6416cd7468a0e0731988",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def unitary(generator: np.random.Generator, dimension: int) -> np.ndarray:
    raw = (
        generator.standard_normal((dimension, dimension))
        + 1j * generator.standard_normal((dimension, dimension))
    )
    q_value, r_value = np.linalg.qr(raw)
    diagonal = np.diag(r_value)
    correction = np.ones(dimension, dtype=complex)
    selected = np.abs(diagonal) > 0.0
    correction[selected] = (
        diagonal[selected].conjugate() / np.abs(diagonal[selected])
    )
    return q_value @ np.diag(correction)


def act(
    state: np.ndarray,
    operation: np.ndarray,
    axes: tuple[int, ...],
) -> np.ndarray:
    other = tuple(
        index for index in range(state.ndim)
        if index not in axes
    )
    order = axes + other
    inverse = np.argsort(order)
    arranged = np.transpose(state, order)
    acted_dimension = int(np.prod([state.shape[index] for index in axes]))
    tail = arranged.shape[len(axes):]
    result = (operation @ arranged.reshape(acted_dimension, -1)).reshape(
        *(state.shape[index] for index in axes),
        *tail,
    )
    return np.transpose(result, inverse)


def embed(
    operation: np.ndarray,
    dimensions: tuple[int, ...],
    axes: tuple[int, ...],
) -> np.ndarray:
    total = int(np.prod(dimensions))
    embedded = np.zeros((total, total), dtype=complex)
    for column in range(total):
        basis = np.zeros(total, dtype=complex)
        basis[column] = 1.0
        evolved = act(basis.reshape(dimensions), operation, axes)
        embedded[:, column] = evolved.reshape(-1)
    return embedded


def trace_axis(
    operator: np.ndarray,
    dimensions: tuple[int, ...],
    axis: int,
) -> tuple[np.ndarray, tuple[int, ...]]:
    tensor = operator.reshape(*dimensions, *dimensions)
    reduced = np.trace(
        tensor,
        axis1=axis,
        axis2=axis + len(dimensions),
    )
    new_dimensions = dimensions[:axis] + dimensions[axis + 1:]
    new_total = int(np.prod(new_dimensions))
    return reduced.reshape(new_total, new_total), new_dimensions


def main() -> None:
    for path, expected in EXPECTED.items():
        if sha256(path) != expected:
            raise RuntimeError(f"authority drift: {path.name}")
    primary = json.loads(PRIMARY.read_text())

    generator = np.random.default_rng(17012027)
    source_dimension = 2
    record_one_dimension = 2
    record_two_dimension = 3
    dimensions = (
        source_dimension,
        record_one_dimension,
        record_two_dimension,
    )
    ready_one = np.zeros(record_one_dimension, dtype=complex)
    ready_two = np.zeros(record_two_dimension, dtype=complex)
    ready_one[0] = 1.0
    ready_two[0] = 1.0
    sigma_one = np.outer(ready_one, ready_one.conjugate())
    sigma_two = np.outer(ready_two, ready_two.conjugate())

    initial = (
        generator.standard_normal((source_dimension, source_dimension))
        + 1j * generator.standard_normal((source_dimension, source_dimension))
    )
    initial /= np.linalg.norm(initial)

    plus_one = unitary(
        generator,
        source_dimension * record_one_dimension,
    )
    minus_one = unitary(
        generator,
        source_dimension * record_one_dimension,
    )
    plus_joint = unitary(generator, int(np.prod(dimensions)))
    minus_joint = unitary(generator, int(np.prod(dimensions)))
    plus_two = unitary(
        generator,
        source_dimension * record_two_dimension,
    )
    minus_two = unitary(
        generator,
        source_dimension * record_two_dimension,
    )

    global_plus_one = embed(plus_one, dimensions, (0, 1))
    global_minus_one = embed(minus_one, dimensions, (0, 1))
    global_plus_two = embed(plus_two, dimensions, (0, 2))
    global_minus_two = embed(minus_two, dimensions, (0, 2))
    full = np.kron(np.kron(initial, sigma_one), sigma_two)
    full = global_plus_one @ full @ global_minus_one.conjugate().T
    full = plus_joint @ full @ minus_joint.conjugate().T
    full = global_plus_two @ full @ global_minus_two.conjugate().T
    full, after_one = trace_axis(full, dimensions, 1)
    full, after_two = trace_axis(full, after_one, 1)

    block = np.kron(initial, sigma_one)
    block = plus_one @ block @ minus_one.conjugate().T
    block = np.kron(block, sigma_two)
    block = plus_joint @ block @ minus_joint.conjugate().T
    block, block_dimensions = trace_axis(block, dimensions, 1)
    block = plus_two @ block @ minus_two.conjugate().T
    block, final_dimensions = trace_axis(block, block_dimensions, 1)

    relative_error = float(
        np.linalg.norm(block - full)
        / max(np.linalg.norm(full), 1e-30)
    )
    last_incidence = {"R1": 1, "R2": 2}
    valid_closures = {"R1": 1, "R2": 2}
    invalid_closures = {"R1": 0, "R2": 2}
    valid = all(
        valid_closures[name] >= event
        for name, event in last_incidence.items()
    )
    invalid_violations = [
        name for name, event in last_incidence.items()
        if invalid_closures[name] < event
    ]
    passed = bool(
        primary["pass"]
        and primary["concurrent_open_record_block_map_derived"]
        and relative_error < 1e-12
        and valid
        and invalid_violations == ["R1"]
        and after_two == (source_dimension,)
        and final_dimensions == (source_dimension,)
    )
    result = {
        "schema":
            "complete_qspec_open_record_block_transfer_verification_v001",
        "protocol_sha256": sha256(PROTOCOL),
        "independent_regression": {
            "seed": 17012027,
            "source_dimension": source_dimension,
            "record_dimensions": [
                record_one_dimension,
                record_two_dimension,
            ],
            "initial_cross_operator_rank":
                int(np.linalg.matrix_rank(initial)),
            "initial_cross_operator_Hermitian":
                bool(np.allclose(initial, initial.conjugate().T)),
            "relative_frobenius_error": relative_error,
            "threshold": 1e-12,
            "pass": relative_error < 1e-12,
        },
        "liveness_validation": {
            "last_incidence": last_incidence,
            "valid_schedule_pass": valid,
            "invalid_early_close_violations": invalid_violations,
            "invalid_early_close_rejected":
                invalid_violations == ["R1"],
        },
        "verdict": (
            "INDEPENDENT_OPEN_RECORD_BLOCK_TRANSFER_MAP_CONFIRMED"
            if passed
            else "INDEPENDENT_OPEN_RECORD_BLOCK_TRANSFER_MAP_BLOCKED"
        ),
        "pass": passed,
        "sequential_relative_history_transfer_map_derived": True,
        "concurrent_open_record_block_map_derived": passed,
        "connected_K_cell_amplitude_constructed": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "local_Maxwell_response_derived": False,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
