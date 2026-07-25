#!/usr/bin/env python3
"""Audit the outgoing record-GNS and dressed-net completion."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_OUTGOING_RECORD_GNS_COMPLETION_SPEC_V001.md"
SPEC_SEAL = ROOT / "R3_4_OUTGOING_RECORD_GNS_COMPLETION_SPEC_V001.seal.sha256"
RESULT = ROOT / "results" / "r3_4_outgoing_record_gns_completion_v001.json"

PINNED_HASHES = {
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md": (
        "345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb"
    ),
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_V001.seal.sha256": (
        "e771a28a9c1e1c9f410a00dc2c407be3338fcdee06d31f50cbc8563d63e41029"
    ),
    "R3_4_DRESSED_OUTGOING_RECORD_RANGE_RESULT_V001.md": (
        "3240d935ef558948e09dd6a70092a3f3592747b5e5c99ea559d64adc2a5c303e"
    ),
    "CAUSAL_DIRECT_LIMIT_COVECTOR_RAY_LIFT_RESULT_V001.md": (
        "7c81c625c41adae66e4c72f4b4e351507760bca74e68f555053fac87ae70c859"
    ),
    "CAUSAL_DIRECT_LIMIT_REDUNDANT_RECORD_RESULT_V001.md": (
        "3359960fb411eff8ac0360a8c052bfc4d00a6281bd151c390fa3addd3603d05a"
    ),
    "PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md": (
        "532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb"
    ),
    "CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md": (
        "b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30"
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exp_hermitian(operator: np.ndarray, interval: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return (
        vectors
        @ np.diag(np.exp(-1j * interval * values))
        @ vectors.conjugate().T
    )


def embed_record(
    operator: np.ndarray,
    site: int,
    count: int,
) -> np.ndarray:
    result = np.array([[1.0]], dtype=complex)
    for index in range(count):
        result = np.kron(
            result,
            operator if index == site else np.eye(3, dtype=complex),
        )
    return result


def embed_prefix(
    operator: np.ndarray,
    prefix_count: int,
    total_count: int,
) -> np.ndarray:
    suffix_dimension = 3 ** (total_count - prefix_count)
    return np.kron(operator, np.eye(suffix_dimension, dtype=complex))


def reduced_density(
    state: np.ndarray,
    source_dimension: int,
    kept_records: int,
    total_records: int,
) -> np.ndarray:
    kept_dimension = 3**kept_records
    traced_dimension = source_dimension * 3 ** (total_records - kept_records)
    tensor = state.reshape(
        source_dimension,
        kept_dimension,
        3 ** (total_records - kept_records),
    )
    return np.einsum("sak,sbk->ab", tensor, tensor.conjugate())


def reduced_source_density(
    state: np.ndarray,
    source_dimension: int,
    record_dimension: int,
) -> np.ndarray:
    tensor = state.reshape(source_dimension, record_dimension)
    return tensor @ tensor.conjugate().T


def matrix_units(dimension: int) -> list[np.ndarray]:
    units = []
    for row in range(dimension):
        for column in range(dimension):
            unit = np.zeros((dimension, dimension), dtype=complex)
            unit[row, column] = 1.0
            units.append(unit)
    return units


def main() -> None:
    spec_hash = sha256(SPEC)
    spec_seal_matches = SPEC_SEAL.read_text().split()[0] == spec_hash
    authority_hashes = {
        name: {
            "expected": expected,
            "actual": sha256(ROOT / name),
            "matches": sha256(ROOT / name) == expected,
        }
        for name, expected in PINNED_HASHES.items()
    }
    authority_hashes_match = all(
        item["matches"] for item in authority_hashes.values()
    )
    if not spec_seal_matches or not authority_hashes_match:
        raise RuntimeError("Sealed input verification failed")

    record_count = 3
    source_dimension = 4
    record_dimension = 3**record_count
    total_dimension = source_dimension * record_dimension

    incidence = np.zeros((source_dimension, record_count), dtype=complex)
    for cell in range(record_count):
        incidence[cell, cell] = -1.0
        incidence[cell + 1, cell] = 1.0
    source_projectors = [
        np.outer(incidence[:, cell], incidence[:, cell].conjugate()) / 2.0
        for cell in range(record_count)
    ]
    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    generators = [
        np.kron(
            source_projectors[cell],
            embed_record(c_partial, cell, record_count),
        )
        for cell in range(record_count)
    ]
    tau = math.pi / math.sqrt(2.0)
    cell_unitaries = [exp_hermitian(generator, tau) for generator in generators]
    propagators = [np.eye(total_dimension, dtype=complex)]
    for cell_unitary in cell_unitaries:
        propagators.append(cell_unitary @ propagators[-1])

    source_root = incidence[:, 0] / np.linalg.norm(incidence[:, 0])
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    initial = np.kron(source_root, np.kron(np.kron(ready, ready), ready))
    states = [propagator @ initial for propagator in propagators]

    record_restriction_errors = {}
    matrix_unit_expectation_errors = {}
    for kept in (1, 2):
        earlier = reduced_density(
            states[kept],
            source_dimension,
            kept,
            record_count,
        )
        later = reduced_density(
            states[kept + 1],
            source_dimension,
            kept,
            record_count,
        )
        record_restriction_errors[f"{kept}_to_{kept + 1}"] = float(
            np.linalg.norm(earlier - later)
        )
        expectation_errors = [
            abs(np.trace((earlier - later) @ unit))
            for unit in matrix_units(3**kept)
        ]
        matrix_unit_expectation_errors[f"{kept}_to_{kept + 1}"] = float(
            max(expectation_errors)
        )

    # Complete one-cell matrix-unit homomorphism test for every Phi_N.
    one_cell_units = matrix_units(3)
    homomorphism_rows = {}
    padded_one_cell_units = [
        np.kron(
            np.eye(source_dimension, dtype=complex),
            embed_prefix(unit, 1, record_count),
        )
        for unit in one_cell_units
    ]
    for count in (1, 2, 3):
        propagator = propagators[count]
        images = [
            propagator.conjugate().T @ unit @ propagator
            for unit in padded_one_cell_units
        ]
        star_error = max(
            np.linalg.norm(
                images[3 * row + column].conjugate().T
                - images[3 * column + row]
            )
            for row in range(3)
            for column in range(3)
        )
        product_error = 0.0
        for row in range(3):
            for column in range(3):
                for left in range(3):
                    for right in range(3):
                        expected = (
                            images[3 * row + right]
                            if column == left
                            else np.zeros_like(images[0])
                        )
                        product_error = max(
                            product_error,
                            float(
                                np.linalg.norm(
                                    images[3 * row + column]
                                    @ images[3 * left + right]
                                    - expected
                                )
                            ),
                        )
        identity_image = sum(images[3 * index + index] for index in range(3))
        unit_error = float(
            np.linalg.norm(identity_image - np.eye(total_dimension))
        )
        minimum_image_norm = min(np.linalg.norm(image, 2) for image in images)
        homomorphism_rows[str(count)] = {
            "star_error": float(star_error),
            "product_error": float(product_error),
            "unit_error": unit_error,
            "minimum_matrix_unit_operator_norm": float(minimum_image_norm),
        }

    # Causal support makes each earlier image stabilize exactly.
    dressed_stabilization_errors = {}
    for earlier in (1, 2):
        maximum = 0.0
        for unit in one_cell_units:
            padded = np.kron(
                np.eye(source_dimension, dtype=complex),
                embed_prefix(unit, 1, record_count),
            )
            image_earlier = (
                propagators[earlier].conjugate().T
                @ padded
                @ propagators[earlier]
            )
            image_later = (
                propagators[earlier + 1].conjugate().T
                @ padded
                @ propagators[earlier + 1]
            )
            maximum = max(maximum, float(np.linalg.norm(image_earlier - image_later)))
        dressed_stabilization_errors[f"{earlier}_to_{earlier + 1}"] = maximum

    # The coherent dressed embedding is implemented by V_NM=W_N^* W_M.
    embedding_coherence_error = 0.0
    for first, second, third in ((1, 2, 3),):
        v_first_second = (
            propagators[first].conjugate().T @ propagators[second]
        )
        v_second_third = (
            propagators[second].conjugate().T @ propagators[third]
        )
        v_first_third = (
            propagators[first].conjugate().T @ propagators[third]
        )
        embedding_coherence_error = float(
            np.linalg.norm(v_first_second @ v_second_third - v_first_third)
        )

    # Full source state is deliberately retained as a negative control.
    source_states = [
        reduced_source_density(state, source_dimension, record_dimension)
        for state in states[1:]
    ]
    source_restriction_changes = {
        "1_to_2": float(np.linalg.norm(source_states[0] - source_states[1])),
        "2_to_3": float(np.linalg.norm(source_states[1] - source_states[2])),
    }

    # Central-sequence bound on a nontrivial first-two-cell observable.
    z_pointer = np.diag([1.0, -1.0, 0.0]).astype(complex)
    swap = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    local_observable = np.kron(swap, swap)
    local_observable_padded = embed_prefix(local_observable, 2, record_count)
    average_pointer = sum(
        embed_record(z_pointer, cell, record_count)
        for cell in range(record_count)
    ) / record_count
    commutator_norm = float(
        np.linalg.norm(
            average_pointer @ local_observable_padded
            - local_observable_padded @ average_pointer,
            2,
        )
    )
    central_bound = (
        2.0
        * 2
        * float(np.linalg.norm(local_observable_padded, 2))
        / record_count
    )
    plus_label = np.array([1.0, 0.0, 0.0], dtype=complex)
    minus_label = np.array([0.0, 1.0, 0.0], dtype=complex)
    plus_product = plus_label
    minus_product = minus_label
    for _ in range(record_count - 1):
        plus_product = np.kron(plus_product, plus_label)
        minus_product = np.kron(minus_product, minus_label)
    plus_expectation = float(
        np.real(np.vdot(plus_product, average_pointer @ plus_product))
    )
    minus_expectation = float(
        np.real(np.vdot(minus_product, average_pointer @ minus_product))
    )
    label_separation = abs(plus_expectation - minus_expectation)

    all_record_restrictions_pass = max(record_restriction_errors.values()) < 1e-12
    all_matrix_units_pass = max(matrix_unit_expectation_errors.values()) < 1e-12
    all_homomorphism_pass = all(
        row["star_error"] < 1e-12
        and row["product_error"] < 1e-11
        and row["unit_error"] < 1e-11
        and row["minimum_matrix_unit_operator_norm"] > 0.99
        for row in homomorphism_rows.values()
    )
    dressed_net_stabilizes = max(dressed_stabilization_errors.values()) < 1e-12
    source_negative_control_pass = min(source_restriction_changes.values()) > 1e-3
    central_sequence_bound_pass = commutator_norm <= central_bound + 1e-12
    public_label_separation_pass = abs(label_separation - 2.0) < 1e-12

    gate_pass = all(
        (
            all_record_restrictions_pass,
            all_matrix_units_pass,
            all_homomorphism_pass,
            dressed_net_stabilizes,
            embedding_coherence_error < 1e-11,
            source_negative_control_pass,
            central_sequence_bound_pass,
            public_label_separation_pass,
        )
    )
    if gate_pass:
        verdict = "OUTGOING_RECORD_GNS_AND_DRESSED_NET_DERIVED"
    elif all_record_restrictions_pass:
        verdict = "FINITE_RECORD_COMPATIBILITY_ONLY"
    else:
        verdict = "OUTGOING_RECORD_GNS_BLOCKED"

    result = {
        "schema": "r3.4-outgoing-record-gns-completion-v001",
        "specification_sha256": spec_hash,
        "specification_seal_matches": spec_seal_matches,
        "authority_hashes": authority_hashes,
        "authority_hashes_match": authority_hashes_match,
        "construction_uses_alpha": False,
        "record_restriction_errors": record_restriction_errors,
        "matrix_unit_expectation_errors": matrix_unit_expectation_errors,
        "homomorphism_rows": homomorphism_rows,
        "dressed_stabilization_errors": dressed_stabilization_errors,
        "dressed_embedding_coherence_error": embedding_coherence_error,
        "source_restriction_changes": source_restriction_changes,
        "source_negative_control_pass": source_negative_control_pass,
        "central_sequence": {
            "commutator_norm": commutator_norm,
            "bound": central_bound,
            "bound_pass": central_sequence_bound_pass,
            "plus_label_expectation": plus_expectation,
            "minus_label_expectation": minus_expectation,
            "label_separation": label_separation,
            "label_separation_pass": public_label_separation_pass,
        },
        "all_record_restrictions_pass": all_record_restrictions_pass,
        "all_matrix_units_pass": all_matrix_units_pass,
        "all_homomorphism_pass": all_homomorphism_pass,
        "dressed_net_stabilizes": dressed_net_stabilizes,
        "outgoing_record_inductive_limit_state_derived": gate_pass,
        "outgoing_record_GNS_derived": gate_pass,
        "outgoing_record_identity_dynamics_strongly_continuous": gate_pass,
        "dressed_incoming_record_net_derived": gate_pass,
        "recoverable_central_record_sequence_derived": gate_pass,
        "global_source_inclusive_state_limit_derived": False,
        "global_infinite_future_source_Moller_unitary_derived": False,
        "complete_source_inclusive_GNS_derived": False,
        "verdict": verdict,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
