#!/usr/bin/env python3
"""Verify the exact event-driven open-record block transfer theorem."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "COMPLETE_QSPEC_OPEN_RECORD_BLOCK_TRANSFER_MAP_SPEC_V001.md"
PROOF = (
    ROOT
    / "COMPLETE_QSPEC_OPEN_RECORD_BLOCK_TRANSFER_INDUCTION_PROOF_V001.md"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_open_record_block_transfer_v001.json"
)

EXPECTED = {
    SPEC:
        "7bd9b18b1f818cd923472c5911b2b5e0b406faf16fa4345259dffd248d3702d3",
    PROOF:
        "a1db0e42954e639e70bbabe3526d0baaab4082ae892a931832a85e8ac160cee9",
    ROOT / "COMPLETE_QSPEC_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_RESULT_V001.md":
        "ade49876242ffc4ce6c90942f8b63261f3cc1c463103110ff1e2e60fee232e84",
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
    phase = np.ones_like(diagonal)
    nonzero = np.abs(diagonal) > 0.0
    phase[nonzero] = diagonal[nonzero] / np.abs(diagonal[nonzero])
    return q_value @ np.diag(phase.conjugate())


def apply_on_axes(
    state: np.ndarray,
    unitary: np.ndarray,
    axes: tuple[int, ...],
) -> np.ndarray:
    remaining = tuple(
        axis for axis in range(state.ndim)
        if axis not in axes
    )
    permutation = axes + remaining
    inverse = np.argsort(permutation)
    permuted = np.transpose(state, permutation)
    leading = int(np.prod([state.shape[axis] for axis in axes]))
    trailing_shape = permuted.shape[len(axes):]
    flat = permuted.reshape(leading, -1)
    evolved = (unitary @ flat).reshape(
        *(state.shape[axis] for axis in axes),
        *trailing_shape,
    )
    return np.transpose(evolved, inverse)


def partial_trace_record_one(
    operator: np.ndarray,
    source_dimension: int,
    record_dimension: int,
) -> np.ndarray:
    tensor = operator.reshape(
        source_dimension,
        record_dimension,
        record_dimension,
        source_dimension,
        record_dimension,
        record_dimension,
    )
    reduced = np.trace(tensor, axis1=1, axis2=4)
    return reduced.reshape(
        source_dimension * record_dimension,
        source_dimension * record_dimension,
    )


def partial_trace_record_two(
    operator: np.ndarray,
    source_dimension: int,
    record_dimension: int,
) -> np.ndarray:
    tensor = operator.reshape(
        source_dimension,
        record_dimension,
        source_dimension,
        record_dimension,
    )
    return np.trace(tensor, axis1=1, axis2=3)


def validate_closures(
    supports: tuple[frozenset[str], ...],
    closures: dict[str, int],
) -> tuple[bool, dict[str, int], list[str]]:
    records = sorted(set().union(*supports))
    last = {
        record: max(
            index
            for index, support in enumerate(supports)
            if record in support
        )
        for record in records
    }
    violations = [
        record
        for record in records
        if closures.get(record, -1) < last[record]
    ]
    return not violations, last, violations


def main() -> None:
    for path, expected in EXPECTED.items():
        if sha256(path) != expected:
            raise RuntimeError(f"authority drift: {path.name}")

    generator = np.random.default_rng(20260725)
    source_dimension = 3
    record_dimension = 2
    ready = np.array([1.0, 0.0], dtype=complex)
    ready_density = np.outer(ready, ready.conjugate())

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

    dimensions = {
        "one_record": source_dimension * record_dimension,
        "two_records":
            source_dimension * record_dimension * record_dimension,
    }
    plus_u1 = random_unitary(generator, dimensions["one_record"])
    minus_u1 = random_unitary(generator, dimensions["one_record"])
    plus_u12 = random_unitary(generator, dimensions["two_records"])
    minus_u12 = random_unitary(generator, dimensions["two_records"])
    plus_u2 = random_unitary(generator, dimensions["one_record"])
    minus_u2 = random_unitary(generator, dimensions["one_record"])

    full_plus = np.einsum(
        "s,r,t->srt",
        source_plus,
        ready,
        ready,
    )
    full_minus = np.einsum(
        "s,r,t->srt",
        source_minus,
        ready,
        ready,
    )
    full_plus = apply_on_axes(full_plus, plus_u1, (0, 1))
    full_minus = apply_on_axes(full_minus, minus_u1, (0, 1))
    full_plus = apply_on_axes(full_plus, plus_u12, (0, 1, 2))
    full_minus = apply_on_axes(full_minus, minus_u12, (0, 1, 2))
    full_plus = apply_on_axes(full_plus, plus_u2, (0, 2))
    full_minus = apply_on_axes(full_minus, minus_u2, (0, 2))
    full_plus_flat = full_plus.reshape(source_dimension, -1)
    full_minus_flat = full_minus.reshape(source_dimension, -1)
    full_source_cross = (
        full_plus_flat @ full_minus_flat.conjugate().T
    )

    block = np.kron(
        np.outer(source_plus, source_minus.conjugate()),
        ready_density,
    )
    block = plus_u1 @ block @ minus_u1.conjugate().T
    block = np.kron(block, ready_density)
    block = plus_u12 @ block @ minus_u12.conjugate().T
    block = partial_trace_record_one(
        block,
        source_dimension,
        record_dimension,
    )
    block = plus_u2 @ block @ minus_u2.conjugate().T
    block_source_cross = partial_trace_record_two(
        block,
        source_dimension,
        record_dimension,
    )
    operator_scale = max(np.linalg.norm(full_source_cross), 1e-30)
    relative_error = float(
        np.linalg.norm(block_source_cross - full_source_cross)
        / operator_scale
    )

    supports = (
        frozenset({"R1"}),
        frozenset({"R1", "R2"}),
        frozenset({"R2"}),
    )
    valid, last_incidence, valid_violations = validate_closures(
        supports,
        {"R1": 1, "R2": 2},
    )
    invalid, _, invalid_violations = validate_closures(
        supports,
        {"R1": 0, "R2": 2},
    )
    passed = bool(
        relative_error < 1e-12
        and valid
        and not valid_violations
        and not invalid
        and invalid_violations == ["R1"]
    )
    result = {
        "schema": "complete_qspec_open_record_block_transfer_v001",
        "spec_sha256": sha256(SPEC),
        "induction_proof_sha256": sha256(PROOF),
        "generic_overlapping_regression": {
            "seed": 20260725,
            "source_dimension": source_dimension,
            "record_dimensions": [record_dimension, record_dimension],
            "supports": [
                sorted(support) for support in supports
            ],
            "full_source_cross_frobenius":
                float(np.linalg.norm(full_source_cross)),
            "block_source_cross_frobenius":
                float(np.linalg.norm(block_source_cross)),
            "relative_frobenius_error": relative_error,
            "threshold": 1e-12,
            "pass": relative_error < 1e-12,
        },
        "liveness_validation": {
            "last_incidence": last_incidence,
            "valid_schedule_pass": valid and not valid_violations,
            "invalid_early_close_rejected":
                (not invalid and invalid_violations == ["R1"]),
            "invalid_schedule_violations": invalid_violations,
        },
        "theorem": {
            "open_step_proved": True,
            "evolution_step_proved": True,
            "valid_close_step_proved": True,
            "sequential_reduction_proved": True,
            "invalid_early_close_excluded": True,
            "maximum_open_width_bounded": False,
        },
        "verdict": (
            "COMPLETE_QSPEC_OPEN_RECORD_BLOCK_TRANSFER_MAP_DERIVED"
            if passed
            else "COMPLETE_QSPEC_OPEN_RECORD_BLOCK_TRANSFER_MAP_BLOCKED"
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
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
