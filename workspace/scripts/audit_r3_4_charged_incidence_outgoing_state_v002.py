#!/usr/bin/env python3
"""Audit the charged-incidence endpoint map and quasi-local state lift."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import re

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_SPEC_V002.md"
SEAL = ROOT / "R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_SPEC_V002.seal.sha256"
OUTPUT = ROOT / "results" / "r3_4_charged_incidence_outgoing_state_v002.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_status(path: Path, key: str) -> bool:
    pattern = re.compile(rf"^{re.escape(key)}\s*=\s*(true|false)\s*$", re.MULTILINE)
    matches = pattern.findall(path.read_text(encoding="utf-8"))
    require(len(matches) == 1, f"Expected one {key} in {path.name}")
    return matches[0] == "true"


def evolve(operator: np.ndarray, interval: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return (
        vectors
        @ np.diag(np.exp(-1.0j * interval * values))
        @ vectors.conjugate().T
    )


def record_embedding(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    result = np.array([[1.0]], dtype=complex)
    identity = np.eye(3, dtype=complex)
    for index in range(count):
        result = np.kron(result, operator if index == site else identity)
    return result


def source_state() -> np.ndarray:
    weights = (0.2, 0.3, 0.5)
    chiral_states = (
        np.array([[0.65, 0.10j], [-0.10j, 0.35]], dtype=complex),
        np.array([[0.55, 0.15], [0.15, 0.45]], dtype=complex),
        np.array([[0.60, -0.12j], [0.12j, 0.40]], dtype=complex),
    )
    result = np.zeros((6, 6), dtype=complex)
    for index, (weight, state) in enumerate(zip(weights, chiral_states)):
        eigenvalues = np.linalg.eigvalsh(state)
        require(np.min(eigenvalues) > 0.0, "Source test state is not positive")
        block = slice(2 * index, 2 * index + 2)
        result[block, block] = weight * state
    require(abs(np.trace(result) - 1.0) < 1e-14, "Source state is not normalized")
    return result


def ready_projector(count: int) -> np.ndarray:
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    vector = np.array([1.0], dtype=complex)
    for _ in range(count):
        vector = np.kron(vector, ready)
    return np.outer(vector, vector.conjugate())


def partial_trace_last_record(
    density: np.ndarray, source_dimension: int, record_count: int
) -> np.ndarray:
    kept_dimension = source_dimension * 3 ** (record_count - 1)
    reshaped = density.reshape(kept_dimension, 3, kept_dimension, 3)
    return np.trace(reshaped, axis1=1, axis2=3)


def build_finite_write(count: int) -> tuple[np.ndarray, tuple[np.ndarray, ...]]:
    q = np.diag([-1.0, 0.0, 1.0]).astype(complex)
    p_ch = np.diag([1.0, 0.0, 1.0]).astype(complex)
    gamma5 = np.diag([-1.0, 1.0]).astype(complex)
    c_partial = np.array(
        [
            [0.0, 0.0, -1.0j],
            [0.0, 0.0, +1.0j],
            [+1.0j, -1.0j, 0.0],
        ],
        dtype=complex,
    )
    source_identity = np.eye(6, dtype=complex)
    tau = math.pi / math.sqrt(2.0)
    generators = []
    unitaries = []
    for site in range(count):
        record_operator = record_embedding(c_partial, site, count)
        generator = np.kron(np.kron(p_ch, gamma5), record_operator)
        generators.append(generator)
        unitaries.append(evolve(generator, tau))

    total = np.eye(source_identity.shape[0] * 3**count, dtype=complex)
    for unitary in unitaries:
        total = unitary @ total
    return total, tuple(generators)


def main() -> None:
    seal_fields = SEAL.read_text(encoding="ascii").strip().split()
    require(seal_fields == [sha256(SPEC), SPEC.name], "Specification seal failed")

    c_partial = np.array(
        [
            [0.0, 0.0, -1.0j],
            [0.0, 0.0, +1.0j],
            [+1.0j, -1.0j, 0.0],
        ],
        dtype=complex,
    )
    gamma5 = np.diag([-1.0, 1.0]).astype(complex)
    tau = math.pi / math.sqrt(2.0)
    active_unitary = evolve(np.kron(gamma5, c_partial), tau)
    swap = np.array(
        [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]],
        dtype=complex,
    )
    expected_active = np.kron(np.eye(2, dtype=complex), swap)
    active_error = np.linalg.norm(active_unitary - expected_active)

    q = np.diag([-1.0, 0.0, 1.0]).astype(complex)
    p_ch = np.diag([1.0, 0.0, 1.0]).astype(complex)
    controlled_generator = np.kron(np.kron(p_ch, gamma5), c_partial)
    controlled_unitary = evolve(controlled_generator, tau)
    expected_controlled = (
        np.kron(
            np.kron(np.eye(3, dtype=complex) - p_ch, np.eye(2, dtype=complex)),
            np.eye(3, dtype=complex),
        )
        + np.kron(np.kron(p_ch, np.eye(2, dtype=complex)), swap)
    )
    controlled_error = np.linalg.norm(controlled_unitary - expected_controlled)
    charge_commutator = np.linalg.norm(
        controlled_unitary @ np.kron(np.kron(q, np.eye(2)), np.eye(3))
        - np.kron(np.kron(q, np.eye(2)), np.eye(3)) @ controlled_unitary
    )

    finite_states: dict[int, np.ndarray] = {}
    finite_generators: dict[int, tuple[np.ndarray, ...]] = {}
    for count in (1, 2, 3):
        unitary, generators = build_finite_write(count)
        initial = np.kron(source_state(), ready_projector(count))
        finite_states[count] = unitary @ initial @ unitary.conjugate().T
        finite_generators[count] = generators

    restriction_errors = {
        f"{count + 1}_to_{count}": float(
            np.linalg.norm(
                partial_trace_last_record(finite_states[count + 1], 6, count + 1)
                - finite_states[count]
            )
        )
        for count in (1, 2)
    }

    earlier_pointer = np.diag([-1.0, 1.0, 0.0]).astype(complex)
    earlier_observable = np.kron(
        np.eye(6, dtype=complex),
        record_embedding(earlier_pointer, 0, 2),
    )
    later_generator = finite_generators[2][1]
    later_record_commutator = np.linalg.norm(
        later_generator @ earlier_observable
        - earlier_observable @ later_generator
    )

    later_endpoint_unitary = evolve(later_generator, tau)
    source_probe = np.array(
        [
            [0.2, 0.3 + 0.1j],
            [0.3 - 0.1j, -0.4],
        ],
        dtype=complex,
    )
    source_probe_full = np.kron(
        np.kron(np.eye(3, dtype=complex), source_probe),
        np.eye(9, dtype=complex),
    )
    endpoint_source_commutator = np.linalg.norm(
        later_endpoint_unitary @ source_probe_full
        - source_probe_full @ later_endpoint_unitary
    )

    t_probe = math.pi / (2.0 * math.sqrt(2.0))
    one_cell_stationary_overlap = (
        1.0 + math.cos(math.sqrt(2.0) * t_probe)
    ) / 2.0
    stationary_overlaps = {
        str(count): one_cell_stationary_overlap**count
        for count in (1, 2, 4, 8, 16, 32)
    }

    global_parent = ROOT / "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md"
    support_derived = exact_status(
        global_parent, "time_dependent_continuum_ordering_derived"
    )
    preparation_derived = exact_status(
        global_parent, "connected_preparation_derived"
    )

    require(active_error < 1e-12, "Active incidence unitary is not the swap")
    require(controlled_error < 1e-12, "Controlled incidence unitary mismatch")
    require(charge_commutator < 1e-13, "Completed write demolishes charge")
    require(max(restriction_errors.values()) < 1e-12, "State lift is incompatible")
    require(
        later_record_commutator < 1e-13,
        "Later pulse changes an earlier record observable",
    )
    require(
        endpoint_source_commutator < 1e-12,
        "Completed later map is not source-spin identity",
    )

    verdict = (
        "CHARGED_INCIDENCE_OUTGOING_PUBLIC_STATE_DERIVED"
        if support_derived and preparation_derived
        else "CHARGED_INCIDENCE_OUTGOING_STATE_CONDITIONAL_ON_CAUSAL_SUPPORT"
    )
    result = {
        "schema": "r3.4-charged-incidence-outgoing-state-v002",
        "spec_sha256": sha256(SPEC),
        "spec_seal_verified": True,
        "target_values_used": False,
        "active_endpoint_unitary_swap_error": float(active_error),
        "controlled_endpoint_unitary_error": float(controlled_error),
        "completed_unitary_charge_commutator_error": float(charge_commutator),
        "completed_endpoint_map_spin_independent": bool(
            endpoint_source_commutator < 1e-12
        ),
        "finite_state_restriction_errors": restriction_errors,
        "later_pulse_earlier_record_commutator_error": float(
            later_record_commutator
        ),
        "completed_later_map_source_spin_commutator_error": float(
            endpoint_source_commutator
        ),
        "charge_superselected_quasilocal_state_lift_derived": True,
        "macroscopic_pointer_central_sequence_imported_from_same_state_family": True,
        "stationary_parent_one_cell_endpoint_overlap_at_probe_time": (
            one_cell_stationary_overlap
        ),
        "stationary_parent_N_cell_overlap_at_probe_time": stationary_overlaps,
        "stationary_infinite_endpoint_product_GNS_implementation_fails": True,
        "one_use_causal_support_derived_by_live_parent": support_derived,
        "connected_preparation_derived_by_live_parent": preparation_derived,
        "complete_continuous_parent_covariance_derived": False,
        "complete_parent_action_derived": False,
        "physical_response_spectral_measure_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": verdict,
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
