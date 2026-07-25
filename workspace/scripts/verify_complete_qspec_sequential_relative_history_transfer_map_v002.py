#!/usr/bin/env python3
"""Independent verifier for the strictly sequential transfer theorem."""

from __future__ import annotations

import hashlib
import json
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
PRIMARY_SCRIPT = (
    ROOT
    / "scripts/"
    "derive_complete_qspec_sequential_relative_history_transfer_map_v002.py"
)
PRIMARY = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_sequential_relative_history_transfer_map_v002.json"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_sequential_relative_history_transfer_map_verification_v002.json"
)

EXPECTED = {
    SPEC:
        "b6337e4697e3487f927b9bc324d00a5c5a3f245d98bd8cde1833cdf62ee49357",
    INDUCTION:
        "5fc923b9ecca5ee6e63fe8faa50047d72747ebaf09646b14b03affc48a6e84a3",
    PRIMARY_SCRIPT:
        "954f9ca6d6f70cf893748216ceb8b489eba28618e1637afd6c02be3f79be7aa5",
    PRIMARY:
        "ce84fb8244751d8f2cc8495a64ee219bd2dd4d9ffc5d3593a34b7265da589cca",
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
    source_plus = (
        generator.normal(size=source_dimension)
        + 1j * generator.normal(size=source_dimension)
    )
    source_minus = (
        generator.normal(size=source_dimension)
        + 1j * generator.normal(size=source_dimension)
    )
    source_plus /= np.linalg.norm(source_plus)
    source_minus /= np.linalg.norm(source_minus)
    full_shape = (source_dimension,) + (record_dimension,) * cell_count
    plus_state = np.zeros(full_shape, dtype=complex)
    minus_state = np.zeros(full_shape, dtype=complex)
    ready_index = (slice(None),) + (0,) * cell_count
    plus_state[ready_index] = source_plus
    minus_state[ready_index] = source_minus

    cross_density = np.outer(
        source_plus,
        source_minus.conjugate(),
    )
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
    stage_operator_relative_errors = []
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
        cross_density = transfer(
            cross_density,
            plus_kraus[cell],
            minus_kraus[cell],
        )
        plus_flat = plus_state.reshape(source_dimension, -1)
        minus_flat = minus_state.reshape(source_dimension, -1)
        full_cross = plus_flat @ minus_flat.conjugate().T
        stage_scale = max(np.linalg.norm(full_cross), 1e-30)
        stage_operator_relative_errors.append(
            float(np.linalg.norm(cross_density - full_cross) / stage_scale)
        )
    full_overlap = complex(np.trace(full_cross))
    transfer_overlap = complex(np.trace(cross_density))
    general_identity_error = max(stage_operator_relative_errors)

    reversed_density = np.outer(
        source_plus,
        source_minus.conjugate(),
    )
    for cell in reversed(range(cell_count)):
        reversed_density = transfer(
            reversed_density,
            plus_kraus[cell],
            minus_kraus[cell],
        )
    reversed_operator_relative_difference = float(
        np.linalg.norm(reversed_density - full_cross)
        / max(np.linalg.norm(full_cross), 1e-30)
    )

    diagonal_density = np.outer(source_plus, source_plus.conjugate())
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
    physical_operator_error = primary[
        "order_sensitive_operator_regression"
    ]["ordered_operator_relative_error"]
    physical_reversed_difference = primary[
        "order_sensitive_operator_regression"
    ]["reversed_operator_relative_difference"]
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
        == "COMPLETE_QSPEC_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_DERIVED"
        and general_identity_error < 1e-12
        and reversed_operator_relative_difference > 1e-6
        and diagonal_trace_error < 1e-12
        and max(completeness_errors) < 1e-12
        and physical_error < 1e-10
        and physical_diagonal_error < 1e-10
        and physical_operator_error < 1e-10
        and physical_reversed_difference > 1e-6
        and primary["theorem"]["base_case_stated"]
        and primary["theorem"]["induction_hypothesis_stated"]
        and primary["theorem"]["partial_trace_commutation_step_stated"]
        and primary["theorem"]["sequential_history_factorization_stated"]
        and primary["theorem"]["concurrent_open_record_scope_excluded"]
        and primary["theorem"]["concurrent_open_records_require_block_map"]
        and primary["theorem"]["complete_final_identity_retained"]
        and not primary["theorem"]["final_source_ray_inserted"]
        and not primary["theorem"]["record_outcome_postselected"]
        and not primary["theorem"]["determinant_used"]
        and protected
        and primary["no_target_access_attestation"]
    )
    result = {
        "schema":
            "complete_qspec_sequential_relative_history_transfer_map_verification_v002",
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
            "maximum_stage_operator_relative_error":
                general_identity_error,
            "stage_operator_relative_errors":
                stage_operator_relative_errors,
            "reversed_operator_relative_difference":
                reversed_operator_relative_difference,
            "diagonal_trace_error": diagonal_trace_error,
            "maximum_kraus_completeness_error":
                max(completeness_errors),
        },
        "physical_regression_rechecked": {
            "transfer_full_error": physical_error,
            "diagonal_trace_error": physical_diagonal_error,
            "ordered_operator_relative_error": physical_operator_error,
            "reversed_operator_relative_difference":
                physical_reversed_difference,
        },
        "protected_statuses_verified": protected,
        "verdict": (
            "INDEPENDENT_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_CONFIRMED"
            if passed
            else "INDEPENDENT_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_BLOCKED"
        ),
        "pass": passed,
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
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
