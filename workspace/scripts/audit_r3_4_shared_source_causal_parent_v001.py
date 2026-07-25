#!/usr/bin/env python3
"""Audit the shared-source causal incidence parent and local Moller map."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_SHARED_SOURCE_CAUSAL_PARENT_SPEC_V001.md"
SPEC_SEAL = ROOT / "R3_4_SHARED_SOURCE_CAUSAL_PARENT_SPEC_V001.seal.sha256"
OUTPUT = ROOT / "results" / "r3_4_shared_source_causal_parent_v001.json"

PINNED = {
    "CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md":
        "b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30",
    "PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md":
        "532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb",
    "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md":
        "949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd",
    "scripts/audit_bid_global_boundary_descent_quasi_free_v001.py":
        "f19892d5b87149f0627e17a118021670a1e54ab4c003f76641c364154b326097",
    "BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md":
        "b786db3adec8cc335967d49ec13b59923d67f424644f72c535b27b579dd1489f",
    "scripts/audit_bid_unique_charged_controlled_coupling_v001.py":
        "c0ee054d73e93cdcf3f909f65a989dff4a1377e892f71d5e657441640c48db58",
    "BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md":
        "7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476",
    "scripts/audit_bid_first_opening_interval_v001.py":
        "c5de96772a85f128df0a51a68d364a61c73b8c94c7e8e13e26b95964048651d5",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_seal(target: Path, seal: Path) -> None:
    fields = seal.read_text(encoding="ascii").strip().split()
    require(fields == [sha256(target), target.name], f"Seal failed: {target.name}")


def projector(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conjugate()) / np.vdot(vector, vector)


def evolve(operator: np.ndarray, angle: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return vectors @ np.diag(np.exp(-1.0j * angle * values)) @ vectors.conjugate().T


def embed_record(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    result = np.array([[1.0]], dtype=complex)
    identity = np.eye(3, dtype=complex)
    for index in range(count):
        result = np.kron(result, operator if index == site else identity)
    return result


def reduced_records(state: np.ndarray, source_dim: int, count: int, keep: int) -> np.ndarray:
    tensor = state.reshape((source_dim,) + (3,) * count)
    kept_axes = tuple(range(1, keep + 1))
    traced_axes = (0,) + tuple(range(keep + 1, count + 1))
    permuted = np.transpose(tensor, kept_axes + traced_axes)
    matrix = permuted.reshape(3**keep, -1)
    return matrix @ matrix.conjugate().T


def reduced_source_and_first_record(
    state: np.ndarray, source_dim: int, count: int
) -> np.ndarray:
    tensor = state.reshape((source_dim,) + (3,) * count)
    axes = (0, 1) + tuple(range(2, count + 1))
    matrix = np.transpose(tensor, axes).reshape(source_dim * 3, -1)
    return matrix @ matrix.conjugate().T


def main() -> None:
    verify_seal(SPEC, SPEC_SEAL)
    for name, digest in PINNED.items():
        require(sha256(ROOT / name) == digest, f"Upstream drift: {name}")

    cell_count = 3
    vertex_count = cell_count + 1
    incidence = np.zeros((vertex_count, cell_count), dtype=complex)
    for cell in range(cell_count):
        incidence[cell, cell] = -1.0
        incidence[cell + 1, cell] = 1.0
    source_vectors = tuple(incidence[:, cell] for cell in range(cell_count))
    source_projectors = tuple(projector(vector) for vector in source_vectors)

    adjacent_overlaps = {
        f"{cell}_{cell + 1}": float(
            np.trace(source_projectors[cell] @ source_projectors[cell + 1]).real
        )
        for cell in range(cell_count - 1)
    }
    disjoint_overlap = float(np.trace(source_projectors[0] @ source_projectors[2]).real)

    gamma5 = np.diag([1.0, 1.0, -1.0, -1.0]).astype(complex)
    c_partial = np.array(
        [
            [0.0, 0.0, -1.0j],
            [0.0, 0.0, +1.0j],
            [+1.0j, -1.0j, 0.0],
        ],
        dtype=complex,
    )
    source_dim = vertex_count * gamma5.shape[0]
    record_dim = 3**cell_count
    generators = []
    for cell in range(cell_count):
        source_spin = np.kron(source_projectors[cell], gamma5)
        record = embed_record(c_partial, cell, cell_count)
        generators.append(np.kron(source_spin, record))

    commutators = {}
    for left in range(cell_count):
        for right in range(left + 1, cell_count):
            commutators[f"{left}_{right}"] = float(
                np.linalg.norm(
                    generators[left] @ generators[right]
                    - generators[right] @ generators[left]
                )
            )

    tau = math.pi / math.sqrt(2.0)
    unitaries = tuple(evolve(generator, tau) for generator in generators)

    profile_segments = (
        (tau,),
        (tau / 7.0, 2.0 * tau / 7.0, 4.0 * tau / 7.0),
        (1.5 * tau, -0.5 * tau),
    )
    profile_errors = []
    for segments in profile_segments:
        unitary = np.eye(generators[0].shape[0], dtype=complex)
        for segment in segments:
            unitary = evolve(generators[0], segment) @ unitary
        profile_errors.append(float(np.linalg.norm(unitary - unitaries[0])))

    adjacent_order_error = float(
        np.linalg.norm(unitaries[1] @ unitaries[0] - unitaries[0] @ unitaries[1])
    )
    disjoint_order_error = float(
        np.linalg.norm(unitaries[2] @ unitaries[0] - unitaries[0] @ unitaries[2])
    )

    p_record = np.diag([0.0, 1.0, 0.0]).astype(complex)
    x_record = np.array(
        [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
        dtype=complex,
    )
    source_identity = np.eye(source_dim, dtype=complex)
    old_pointer = np.kron(
        source_identity, embed_record(p_record, 0, cell_count)
    )
    old_coherence = np.kron(
        source_identity, embed_record(x_record, 0, cell_count)
    )
    later_pointer_commutators = {
        str(cell): float(
            np.linalg.norm(
                generators[cell] @ old_pointer - old_pointer @ generators[cell]
            )
        )
        for cell in (1, 2)
    }

    source_initial = source_vectors[0] / np.linalg.norm(source_vectors[0])
    spin_initial = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
    source_spin_initial = np.kron(source_initial, spin_initial)
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    record_initial = ready
    for _ in range(cell_count - 1):
        record_initial = np.kron(record_initial, ready)
    state = np.kron(source_spin_initial, record_initial)

    states = []
    record_restrictions_at_write = []
    for index, unitary in enumerate(unitaries):
        state = unitary @ state
        states.append(state.copy())
        record_restrictions_at_write.append(
            reduced_records(state, source_dim, cell_count, index + 1)
        )

    first_pointer_probability_after_each_pulse = [
        float(np.real(np.vdot(value, old_pointer @ value))) for value in states
    ]
    record_restriction_errors = {}
    for keep in (1, 2):
        final_reduction = reduced_records(states[-1], source_dim, cell_count, keep)
        reference = record_restrictions_at_write[keep - 1]
        record_restriction_errors[str(keep)] = float(
            np.linalg.norm(final_reduction - reference)
        )

    source_record_before = reduced_source_and_first_record(
        states[0], source_dim, cell_count
    )
    source_record_after = reduced_source_and_first_record(
        states[-1], source_dim, cell_count
    )
    source_inclusive_restriction_change = float(
        np.linalg.norm(source_record_after - source_record_before)
    )

    partial_products = []
    product = np.eye(source_dim * record_dim, dtype=complex)
    for unitary in unitaries:
        product = unitary @ product
        partial_products.append(product.copy())

    record_moller_images = [
        value.conjugate().T @ old_coherence @ value for value in partial_products
    ]
    record_moller_stabilization_errors = [
        float(np.linalg.norm(record_moller_images[index] - record_moller_images[0]))
        for index in range(1, cell_count)
    ]

    source_local = np.kron(
        np.kron(source_projectors[0], np.eye(4, dtype=complex)),
        np.eye(record_dim, dtype=complex),
    )
    source_moller_images = [
        value.conjugate().T @ source_local @ value for value in partial_products
    ]
    source_buffer_error = float(
        np.linalg.norm(source_moller_images[2] - source_moller_images[1])
    )
    source_first_neighbor_change = float(
        np.linalg.norm(source_moller_images[1] - source_moller_images[0])
    )

    inverse_images = [
        value @ source_local @ value.conjugate().T for value in partial_products
    ]
    inverse_successive_changes = [
        float(np.linalg.norm(inverse_images[index] - inverse_images[index - 1]))
        for index in range(1, cell_count)
    ]

    one_cell_record = evolve(c_partial, tau)
    two_cell_record = evolve(c_partial, 2.0 * tau)
    r = ready
    p = np.array([0.0, 1.0, 0.0], dtype=complex)
    first_write_error = float(np.linalg.norm(one_cell_record @ r - p))
    stationary_recurrence_error = float(np.linalg.norm(two_cell_record @ r - r))

    require(all(abs(value - 0.25) < 1e-13 for value in adjacent_overlaps.values()),
            "Adjacent incidence overlap changed")
    require(abs(disjoint_overlap) < 1e-13, "Disjoint source supports overlap")
    require(commutators["0_1"] > 1e-6 and commutators["1_2"] > 1e-6,
            "Adjacent causal order is not load-bearing")
    require(commutators["0_2"] < 1e-12, "Disjoint generators do not commute")
    require(max(profile_errors) < 1e-11, "Pulse profile changed isolated endpoint")
    require(adjacent_order_error > 1e-6, "Adjacent order unexpectedly commutes")
    require(disjoint_order_error < 1e-11, "Disjoint order changed the parent")
    require(max(later_pointer_commutators.values()) < 1e-12,
            "Later primitive cell acts on an earlier record")
    require(abs(first_pointer_probability_after_each_pulse[0] - 1.0) < 1e-12,
            "First pulse did not write the first record")
    require(
        max(abs(value - 1.0) for value in first_pointer_probability_after_each_pulse)
        < 1e-12,
        "Later pulse erased the first record",
    )
    require(max(record_restriction_errors.values()) < 1e-11,
            "Public-record state restrictions are incompatible")
    require(max(record_moller_stabilization_errors) < 1e-11,
            "Local public Moller image did not stabilize")
    require(source_first_neighbor_change > 1e-6,
            "Shared source support produced no neighbor effect")
    require(source_buffer_error < 1e-11,
            "Source-local Moller image failed finite-buffer stabilization")
    require(source_inclusive_restriction_change > 1e-6,
            "Source-inclusive state was incorrectly reported as compatible")
    require(first_write_error < 1e-12 and stationary_recurrence_error < 1e-12,
            "Mandatory recurrence control failed")

    result = {
        "schema": "r3.4-shared-source-causal-parent-v001",
        "spec_sha256": sha256(SPEC),
        "spec_seal_verified": True,
        "upstream_hashes_verified": len(PINNED),
        "target_values_used": False,
        "source_vertex_count": vertex_count,
        "record_cell_count": cell_count,
        "adjacent_projector_overlaps": adjacent_overlaps,
        "disjoint_projector_overlap": disjoint_overlap,
        "generator_commutator_norms": commutators,
        "profile_endpoint_errors": profile_errors,
        "adjacent_order_error": adjacent_order_error,
        "disjoint_order_error": disjoint_order_error,
        "later_cell_earlier_pointer_commutators": later_pointer_commutators,
        "first_pointer_probability_after_each_pulse":
            first_pointer_probability_after_each_pulse,
        "public_record_restriction_errors": record_restriction_errors,
        "public_record_moller_stabilization_errors":
            record_moller_stabilization_errors,
        "source_first_neighbor_change": source_first_neighbor_change,
        "source_finite_buffer_stabilization_error": source_buffer_error,
        "source_inclusive_state_restriction_change":
            source_inclusive_restriction_change,
        "inverse_candidate_successive_changes": inverse_successive_changes,
        "first_write_error": first_write_error,
        "stationary_recurrence_error": stationary_recurrence_error,
        "shared_source_causal_order_derived": True,
        "primitive_pointer_persistence_derived": True,
        "public_record_state_family_restriction_compatible": True,
        "outgoing_public_record_Moller_endomorphism_derived": True,
        "source_local_Moller_images_stabilize_after_causal_buffer": True,
        "same_GNS_unitary_Moller_implementer_derived": False,
        "parent_selected_outgoing_state_given_in_sector_derived": True,
        "parent_selected_physical_in_state_derived": False,
        "complete_parameter_free_Q_spec_frozen": False,
        "generated_descendant_durability_closed": False,
        "complete_physical_durability_derived": False,
        "nontrivial_outgoing_tail_generator_derived": False,
        "complete_write_plus_tail_spectrum_derived": False,
        "physical_spectral_measure_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": "SHARED_SOURCE_CAUSAL_PARENT_PUBLIC_MOLLER_DERIVED",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
