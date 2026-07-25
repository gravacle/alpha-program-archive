#!/usr/bin/env python3
"""Independent algebraic verifier for the relative-history transfer theorem."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "COMPLETE_QSPEC_RELATIVE_HISTORY_TRANSFER_MAP_SPEC_V001.md"
PRIMARY_SCRIPT = (
    ROOT / "scripts/derive_complete_qspec_relative_history_transfer_map_v001.py"
)
PRIMARY = (
    ROOT / "stage8_execution/work/QSPEC_relative_history_transfer_map_v001.json"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_relative_history_transfer_map_verification_v001.json"
)

EXPECTED = {
    SPEC:
        "7e79583981dd97b2fb5e0ebb6a3498b7bdc03a29cb46f8e2c654f62bc52315ef",
    PRIMARY_SCRIPT:
        "3800b661ea0dacb052aeb0a843f331a13eddc9c838949e5e224c2a5c288271d1",
    PRIMARY:
        "b202278190c5e440713abbea247fcfcb92c1dc4fba1a1b08d8db648f3579caaf",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def random_unitary(
    generator: np.random.Generator,
    dimension: int,
) -> np.ndarray:
    matrix = (
        generator.normal(size=(dimension, dimension))
        + 1j * generator.normal(size=(dimension, dimension))
    )
    q_value, r_value = np.linalg.qr(matrix)
    diagonal = np.diag(r_value)
    phases = np.ones_like(diagonal)
    nonzero = np.abs(diagonal) > 0
    phases[nonzero] = diagonal[nonzero] / np.abs(diagonal[nonzero])
    return q_value @ np.diag(phases.conjugate())


def apply_cell(
    state: np.ndarray,
    unitary: np.ndarray,
    cell: int,
) -> np.ndarray:
    """Apply U on source axis 0 and record axis cell+1."""
    record_axis = cell + 1
    axes = [0, record_axis] + [
        axis for axis in range(state.ndim)
        if axis not in (0, record_axis)
    ]
    inverse = np.argsort(axes)
    permuted = np.transpose(state, axes)
    leading_shape = permuted.shape[:2]
    trailing_shape = permuted.shape[2:]
    flat = permuted.reshape(
        leading_shape[0] * leading_shape[1],
        -1,
    )
    evolved = (unitary @ flat).reshape(
        *leading_shape,
        *trailing_shape,
    )
    return np.transpose(evolved, inverse)


def kraus_from_ready(
    unitary: np.ndarray,
    source_dimension: int,
    record_dimension: int,
) -> tuple[np.ndarray, ...]:
    tensor = unitary.reshape(
        source_dimension,
        record_dimension,
        source_dimension,
        record_dimension,
    )
    return tuple(
        tensor[:, outcome, :, 0]
        for outcome in range(record_dimension)
    )


def transfer(
    cross_density: np.ndarray,
    plus: tuple[np.ndarray, ...],
    minus: tuple[np.ndarray, ...],
) -> np.ndarray:
    return sum(
        left @ cross_density @ right.conjugate().T
        for left, right in zip(plus, minus)
    )


def main() -> None:
    hash_checks = {
        str(path.relative_to(ROOT)): sha256(path) == expected
        for path, expected in EXPECTED.items()
    }
    if not all(hash_checks.values()):
        raise RuntimeError("authority hash mismatch")
    primary = json.loads(PRIMARY.read_text())

    generator = np.random.default_rng(20260725)
    source_dimension = 3
    record_dimension = 2
    cell_count = 3
    plus_unitaries = tuple(
        random_unitary(generator, source_dimension * record_dimension)
        for _ in range(cell_count)
    )
    minus_unitaries = tuple(
        random_unitary(generator, source_dimension * record_dimension)
        for _ in range(cell_count)
    )
    source = (
        generator.normal(size=source_dimension)
        + 1j * generator.normal(size=source_dimension)
    )
    source /= np.linalg.norm(source)
    full_shape = (source_dimension,) + (record_dimension,) * cell_count
    plus_state = np.zeros(full_shape, dtype=complex)
    minus_state = np.zeros(full_shape, dtype=complex)
    ready_index = (slice(None),) + (0,) * cell_count
    plus_state[ready_index] = source
    minus_state[ready_index] = source
    for cell in range(cell_count):
        plus_state = apply_cell(
            plus_state,
            plus_unitaries[cell],
            cell,
        )
        minus_state = apply_cell(
            minus_state,
            minus_unitaries[cell],
            cell,
        )
    full_overlap = complex(np.vdot(minus_state, plus_state))

    cross_density = np.outer(source, source.conjugate())
    plus_kraus = tuple(
        kraus_from_ready(
            unitary,
            source_dimension,
            record_dimension,
        )
        for unitary in plus_unitaries
    )
    minus_kraus = tuple(
        kraus_from_ready(
            unitary,
            source_dimension,
            record_dimension,
        )
        for unitary in minus_unitaries
    )
    for cell in range(cell_count):
        cross_density = transfer(
            cross_density,
            plus_kraus[cell],
            minus_kraus[cell],
        )
    transfer_overlap = complex(np.trace(cross_density))
    general_identity_error = abs(full_overlap - transfer_overlap)

    diagonal_density = np.outer(source, source.conjugate())
    for cell in range(cell_count):
        diagonal_density = transfer(
            diagonal_density,
            plus_kraus[cell],
            plus_kraus[cell],
        )
    diagonal_trace_error = abs(complex(np.trace(diagonal_density)) - 1.0)
    completeness_errors = [
        float(
            np.linalg.norm(
                sum(
                    operator.conjugate().T @ operator
                    for operator in cell_kraus
                )
                - np.eye(source_dimension)
            )
        )
        for cell_kraus in plus_kraus + minus_kraus
    ]

    physical_error = primary["physical_regression"]["transfer_full_error"]
    physical_diagonal_error = (
        primary["physical_regression"]["diagonal_trace_error"]
    )
    protected = all(
        not primary[name]
        for name in (
            "connected_K_cell_amplitude_constructed",
            "volume_uniform_zero_free_neighborhood_proved",
            "connected_linked_cluster_density_proved",
            "local_Maxwell_response_derived",
            "kappa_record_computed",
            "physical_Thomson_stiffness_computed",
            "coupling_evaluation_authorized",
            "alpha_computed",
            "proof_authorized",
        )
    )
    passed = bool(
        primary["pass"]
        and primary["verdict"]
        == "COMPLETE_QSPEC_RELATIVE_HISTORY_TRANSFER_MAP_DERIVED"
        and general_identity_error < 1e-12
        and diagonal_trace_error < 1e-12
        and max(completeness_errors) < 1e-12
        and physical_error < 1e-10
        and physical_diagonal_error < 1e-10
        and primary["theorem"]["complete_final_identity_retained"]
        and not primary["theorem"]["final_source_ray_inserted"]
        and not primary["theorem"]["record_outcome_postselected"]
        and not primary["theorem"]["determinant_used"]
        and protected
        and primary["no_target_access_attestation"]
    )
    result = {
        "schema": "complete_qspec_relative_history_transfer_map_verification_v001",
        "hash_checks": hash_checks,
        "independent_general_test": {
            "seed": 20260725,
            "source_dimension": source_dimension,
            "record_dimension": record_dimension,
            "cell_count": cell_count,
            "full_overlap_real": full_overlap.real,
            "full_overlap_imag": full_overlap.imag,
            "transfer_overlap_real": transfer_overlap.real,
            "transfer_overlap_imag": transfer_overlap.imag,
            "identity_error": general_identity_error,
            "diagonal_trace_error": diagonal_trace_error,
            "maximum_kraus_completeness_error":
                max(completeness_errors),
        },
        "physical_regression_rechecked": {
            "transfer_full_error": physical_error,
            "diagonal_trace_error": physical_diagonal_error,
        },
        "protected_statuses_verified": protected,
        "verdict": (
            "INDEPENDENT_RELATIVE_HISTORY_TRANSFER_MAP_CONFIRMED"
            if passed
            else "INDEPENDENT_RELATIVE_HISTORY_TRANSFER_MAP_BLOCKED"
        ),
        "pass": passed,
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
