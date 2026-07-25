#!/usr/bin/env python3
"""Audit the ordinary local causal parent and its primitive Moller sector."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_SPEC_V001.md"
SEAL = (
    ROOT
    / "R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_SPEC_V001.seal.sha256"
)
OUTPUT = (
    ROOT
    / "results"
    / "r3_4_causal_shared_source_moller_durability_v001.json"
)

PINNED = {
    "LEVEL1_MICROSCOPIC_ACTION_PREMISE_LEDGER_V001.json":
        "827ba19202de2d15a551488fd175aae35325606dbbbe8a1807428d3ba7d6bcef",
    "CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md":
        "b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30",
    "R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md":
        "e60aec3c44cfc5f1ef5715d3445e53783b0185ef93e54d94e442ff1df2ae9b59",
    "R3_4_SHARED_SOURCE_CAUSAL_PARENT_RESULT_V001.md":
        "781608f2fe4c8753a0c06b1d87407b2a6c88caa0ab45329e1200160e56292a24",
    "R3_4_LORENTZIAN_JOINT_ENDPOINT_COMPATIBILITY_RESULT_V001.md":
        "1868656d1881e67c8f6263062b27806f71bcc9de03d7eec0e612085fb47de0cf",
    "R3_4_CAUSAL_TRANSPORTED_WRITE_TAIL_RESULT_V001.md":
        "321c52bc3f5cf8d66b2ca4a7f14811a41e905048ef89415f8c76e22837261c58",
    "BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md":
        "7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exp_hermitian(operator: np.ndarray, interval: float) -> np.ndarray:
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


def diamond_marginal(local_time: float) -> float:
    if not 0.0 <= local_time <= 1.0:
        return 0.0
    return 32.0 * (0.5 - abs(local_time - 0.5)) ** 3


def pulse_unitary(
    h_free: np.ndarray,
    write: np.ndarray,
    integrated_action: float,
    steps: int,
) -> np.ndarray:
    dt = 1.0 / steps
    value = np.eye(h_free.shape[0], dtype=complex)
    for index in range(steps):
        midpoint = (index + 0.5) * dt
        hamiltonian = (
            h_free
            + integrated_action * diamond_marginal(midpoint) * write
        )
        value = exp_hermitian(hamiltonian, dt) @ value
    return value


def pointer_probability(
    state: np.ndarray,
    projector: np.ndarray,
) -> float:
    return float(np.real(np.vdot(state, projector @ state)))


def main() -> None:
    require(
        SEAL.read_text(encoding="ascii").strip().split()
        == [sha256(SPEC), SPEC.name],
        "Specification seal failed",
    )
    for name, digest in PINNED.items():
        require(sha256(ROOT / name) == digest, f"Upstream drift: {name}")

    incidence = np.zeros((3, 2), dtype=complex)
    incidence[0, 0] = -1.0
    incidence[1, 0] = 1.0
    incidence[1, 1] = -1.0
    incidence[2, 1] = 1.0
    h_source = incidence @ incidence.conjugate().T
    source_projectors = tuple(
        np.outer(incidence[:, j], incidence[:, j].conjugate()) / 2.0
        for j in range(2)
    )
    source_overlap = float(
        np.trace(source_projectors[0] @ source_projectors[1]).real
    )

    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    record_count = 2
    record_dimension = 3**record_count
    h_free = np.kron(h_source, np.eye(record_dimension, dtype=complex))
    writes = tuple(
        np.kron(
            source_projectors[j],
            embed_record(c_partial, j, record_count),
        )
        for j in range(record_count)
    )

    pointer = np.diag([0.0, 1.0, 0.0]).astype(complex)
    pointer_zero = np.kron(
        np.eye(3, dtype=complex),
        embed_record(pointer, 0, record_count),
    )
    later_pointer_commutator = float(
        np.linalg.norm(writes[1] @ pointer_zero - pointer_zero @ writes[1])
    )
    free_pointer_commutator = float(
        np.linalg.norm(h_free @ pointer_zero - pointer_zero @ h_free)
    )

    integrated_action = math.pi / math.sqrt(2.0)
    resolutions = (40, 80, 160)
    unitaries = {}
    for steps in resolutions:
        first = pulse_unitary(h_free, writes[0], integrated_action, steps)
        second = pulse_unitary(h_free, writes[1], integrated_action, steps)
        unitaries[steps] = (first, second, second @ first)

    convergence_errors = {
        f"{left}_to_{right}": float(
            np.linalg.norm(unitaries[left][2] - unitaries[right][2])
        )
        for left, right in zip(resolutions[:-1], resolutions[1:])
    }
    convergence_ratio = (
        convergence_errors["40_to_80"] / convergence_errors["80_to_160"]
    )

    first, second, total = unitaries[resolutions[-1]]
    source_root = incidence[:, 0] / np.linalg.norm(incidence[:, 0])
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    initial = np.kron(source_root, np.kron(ready, ready))
    after_first = first @ initial
    after_second = second @ after_first
    after_free = exp_hermitian(h_free, 1.7) @ after_second
    pointer_probabilities = {
        "after_first_closure": pointer_probability(
            after_first, pointer_zero
        ),
        "after_second_closure": pointer_probability(
            after_second, pointer_zero
        ),
        "after_later_free_evolution": pointer_probability(
            after_free, pointer_zero
        ),
    }
    pointer_stability_error = max(pointer_probabilities.values()) - min(
        pointer_probabilities.values()
    )

    free_two_cells = exp_hermitian(h_free, 2.0)
    moller = free_two_cells.conjugate().T @ total
    moller_unitarity_error = float(
        np.linalg.norm(
            moller.conjugate().T @ moller
            - np.eye(moller.shape[0], dtype=complex)
        )
    )
    reverse_order = first @ second
    causal_order_sensitivity = float(np.linalg.norm(total - reverse_order))

    require(abs(source_overlap - 0.25) < 1e-14, "Shared-source overlap failed")
    require(later_pointer_commutator < 1e-13, "Later cell rewrites pointer")
    require(free_pointer_commutator < 1e-13, "Free tail rewrites pointer")
    require(convergence_ratio > 3.5, "Midpoint convergence is not second order")
    require(pointer_stability_error < 2e-10, "Completed pointer is not stable")
    require(moller_unitarity_error < 2e-10, "Finite Moller map is not unitary")
    require(causal_order_sensitivity > 1e-3, "Shared-source order was erased")

    result = {
        "schema": "r3.4-causal-shared-source-moller-durability-v001",
        "spec_sha256": sha256(SPEC),
        "spec_seal_verified": True,
        "upstream_hashes_verified": len(PINNED),
        "target_values_used": False,
        "intrinsic_diamond_time_marginal_used": True,
        "integrated_primitive_action": integrated_action,
        "shared_source_projector_overlap": source_overlap,
        "later_pointer_commutator_norm": later_pointer_commutator,
        "free_pointer_commutator_norm": free_pointer_commutator,
        "midpoint_resolutions": list(resolutions),
        "midpoint_convergence_errors": convergence_errors,
        "midpoint_convergence_ratio": convergence_ratio,
        "first_pointer_probabilities": pointer_probabilities,
        "pointer_stability_error": pointer_stability_error,
        "finite_Moller_unitarity_error": moller_unitarity_error,
        "shared_source_causal_order_sensitivity": causal_order_sensitivity,
        "first_pointer_probability_target_predeclared": False,
        "primitive_finite_support_Moller_derived": True,
        "primitive_public_pointer_persistence_derived": True,
        "primitive_public_outgoing_endomorphism_derived": True,
        "transported_interaction_rule_used": False,
        "generated_descendant_action_derived": False,
        "complete_physical_durability_derived": False,
        "physical_in_state_selected": False,
        "finite_energy_physical_root_derived": False,
        "complete_root_spectral_measure_derived": False,
        "thresholded_source_return_decay_derived": False,
        "complete_parameter_free_Q_spec_frozen": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": "PRIMITIVE_CAUSAL_MOLLER_AND_PUBLIC_DURABILITY_DERIVED",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
