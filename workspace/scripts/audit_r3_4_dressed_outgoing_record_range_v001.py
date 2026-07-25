#!/usr/bin/env python3
"""Audit the range of the stabilized shared-source record map."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_DRESSED_OUTGOING_RECORD_RANGE_SPEC_V001.md"
SEAL = ROOT / "R3_4_DRESSED_OUTGOING_RECORD_RANGE_SPEC_V001.seal.sha256"
OUTPUT = ROOT / "results" / "r3_4_dressed_outgoing_record_range_v001.json"

PINNED = {
    "R3_4_SHARED_SOURCE_CAUSAL_PARENT_V001.seal.sha256":
        "1f710cb0e865e359988ba4fe1800f1c8e025f5eee9185ce5521371ef5a8d42ef",
    "R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_V001.seal.sha256":
        "56d257cd0d9218a37277850a9dff987a54757153d49ade4a232d0a4684cd276d",
    "R3_4_SHARED_SOURCE_CAUSAL_PARENT_RESULT_V001.md":
        "781608f2fe4c8753a0c06b1d87407b2a6c88caa0ab45329e1200160e56292a24",
    "R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_RESULT_V001.md":
        "1d114e71c29c3a39b7afd1b7a80b47afb52fe77e8ee1e4e19b604defe3c69305",
    "CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md":
        "b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30",
    "PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md":
        "532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evolve(operator: np.ndarray, interval: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return (
        vectors
        @ np.diag(np.exp(-1.0j * interval * values))
        @ vectors.conjugate().T
    )


def embed_record(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    value = np.array([[1.0]], dtype=complex)
    for index in range(count):
        value = np.kron(
            value,
            operator if index == site else np.eye(3, dtype=complex),
        )
    return value


def record_conditional_expectation(
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
    record_operator = np.einsum("aiaj->ij", tensor) / source_dimension
    return np.kron(np.eye(source_dimension, dtype=complex), record_operator)


def reduced_first_record(
    state: np.ndarray,
    source_dimension: int,
) -> np.ndarray:
    tensor = state.reshape(source_dimension, 3, 3)
    matrix = np.transpose(tensor, (1, 0, 2)).reshape(3, -1)
    return matrix @ matrix.conjugate().T


def main() -> None:
    require(
        SEAL.read_text(encoding="ascii").strip().split()
        == [sha256(SPEC), SPEC.name],
        "Specification seal failed",
    )
    for name, digest in PINNED.items():
        require(sha256(ROOT / name) == digest, f"Historical drift: {name}")

    incidence = np.zeros((3, 2), dtype=complex)
    incidence[0, 0] = -1.0
    incidence[1, 0] = 1.0
    incidence[1, 1] = -1.0
    incidence[2, 1] = 1.0
    source_projectors = tuple(
        np.outer(incidence[:, j], incidence[:, j].conjugate()) / 2.0
        for j in range(2)
    )
    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    source_dimension = 3
    record_dimension = 9
    generators = tuple(
        np.kron(
            source_projectors[j],
            embed_record(c_partial, j, 2),
        )
        for j in range(2)
    )
    tau = math.pi / math.sqrt(2.0)
    first = evolve(generators[0], tau)
    second = evolve(generators[1], tau)
    histories = (first, second @ first)

    matrix_units = {}
    for row in range(3):
        for column in range(3):
            value = np.zeros((3, 3), dtype=complex)
            value[row, column] = 1.0
            matrix_units[(row, column)] = value

    images = {}
    stabilization_errors = {}
    range_distances = {}
    for key, matrix_unit in matrix_units.items():
        bare = np.kron(
            np.eye(source_dimension, dtype=complex),
            embed_record(matrix_unit, 0, 2),
        )
        first_image = histories[0].conjugate().T @ bare @ histories[0]
        second_image = histories[1].conjugate().T @ bare @ histories[1]
        images[key] = first_image
        stabilization_errors[str(key)] = float(
            np.linalg.norm(second_image - first_image)
        )
        record_projection = record_conditional_expectation(
            first_image, source_dimension, record_dimension
        )
        range_distances[str(key)] = float(
            np.linalg.norm(first_image - record_projection)
        )

    star_errors = []
    product_errors = []
    norm_errors = []
    for (row, column), image in images.items():
        star_errors.append(
            float(np.linalg.norm(image.conjugate().T - images[(column, row)]))
        )
        norm_errors.append(abs(np.linalg.norm(image, 2) - 1.0))
        for (left, right), other_image in images.items():
            expected = (
                images[(row, right)]
                if column == left
                else np.zeros_like(image)
            )
            product_errors.append(
                float(np.linalg.norm(image @ other_image - expected))
            )
    identity_image = sum(images[(index, index)] for index in range(3))
    unitality_error = float(
        np.linalg.norm(
            identity_image
            - np.eye(source_dimension * record_dimension, dtype=complex)
        )
    )

    pointer_image = images[(1, 1)]
    source_probe = np.kron(
        np.diag([1.0, 0.0, 0.0]),
        np.eye(record_dimension, dtype=complex),
    )
    source_commutator = float(
        np.linalg.norm(
            pointer_image @ source_probe - source_probe @ pointer_image
        )
    )

    source_root = incidence[:, 0] / np.linalg.norm(incidence[:, 0])
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    initial = np.kron(source_root, np.kron(ready, ready))
    after_first = first @ initial
    after_second = second @ after_first
    record_state_restriction_error = float(
        np.linalg.norm(
            reduced_first_record(after_second, source_dimension)
            - reduced_first_record(after_first, source_dimension)
        )
    )

    maximum_stabilization_error = max(stabilization_errors.values())
    maximum_range_distance = max(range_distances.values())
    maximum_star_error = max(star_errors)
    maximum_product_error = max(product_errors)
    maximum_norm_error = max(norm_errors)

    require(maximum_stabilization_error < 1e-11,
            "Dressed record images did not stabilize")
    require(maximum_range_distance > 1e-3,
            "All images unexpectedly remained record-only")
    require(range_distances["(1, 1)"] > 1e-3,
            "Pointer image unexpectedly remained record-only")
    require(source_commutator > 1e-3,
            "Pointer image carries no source dependence")
    require(maximum_star_error < 1e-11, "Star preservation failed")
    require(maximum_product_error < 1e-11, "Multiplication failed")
    require(unitality_error < 1e-11, "Unitality failed")
    require(maximum_norm_error < 1e-11, "Injective norm preservation failed")
    require(record_state_restriction_error < 1e-11,
            "Bare output-record state restriction failed")

    result = {
        "schema": "r3.4-dressed-outgoing-record-range-v001",
        "spec_sha256": sha256(SPEC),
        "spec_seal_verified": True,
        "upstream_hashes_verified": len(PINNED),
        "target_values_used": False,
        "matrix_units_tested": len(matrix_units),
        "maximum_image_stabilization_error": maximum_stabilization_error,
        "record_only_range_distances": range_distances,
        "maximum_record_only_range_distance": maximum_range_distance,
        "pointer_image_source_commutator_norm": source_commutator,
        "maximum_star_preservation_error": maximum_star_error,
        "maximum_multiplication_error": maximum_product_error,
        "unitality_error": unitality_error,
        "maximum_norm_preservation_error": maximum_norm_error,
        "bare_output_record_state_restriction_error":
            record_state_restriction_error,
        "prior_bare_record_endomorphism_claim_superseded": True,
        "bare_record_endomorphism_derived": False,
        "stable_dressed_record_monomorphism_derived": True,
        "dressed_output_record_algebra_embedded_in_full_parent": True,
        "bare_output_record_state_family_restriction_compatible": True,
        "same_GNS_unitary_Moller_implementer_derived": False,
        "complete_parent_to_outgoing_GNS_map_derived": False,
        "generated_descendant_action_derived": False,
        "complete_physical_durability_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": "STABLE_DRESSED_RECORD_MONOMORPHISM_DERIVED",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
