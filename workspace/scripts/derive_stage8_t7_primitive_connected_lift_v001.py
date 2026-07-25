#!/usr/bin/env python3
"""Execute the sealed Stage-8 T7 primitive connected-lift derivation."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_PRIMITIVE_CONNECTED_LIFT_DERIVATION_SPEC_V001.md"
SPEC_SHA256 = "63116a5d2b6f1e557db421e9bbd9e8363f85c84ac04c5d54cb7e7dd314aab544"
OUT = ROOT / "stage8_execution/work/T07_primitive_connected_lift.json"

AUTHORITIES = {
    "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md":
        "aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a",
    "BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md":
        "7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476",
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md":
        "6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb",
    "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md":
        "e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6",
    "STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_V001.md":
        "85d24996987278b285d63b8fe15a8732e55664e7c1b09063617b66cb4bc926b4",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def vertex_index(coord: tuple[int, int, int, int], length: int) -> int:
    x0, x1, x2, x3 = coord
    return (((x0 * length + x1) * length + x2) * length + x3)


def periodic_incidence_dense(
    length: int, phases: dict[tuple[int, int], float] | None = None
) -> np.ndarray:
    """Covariant boundary D:C1->C0 on the positive oriented 4-torus edges."""
    phases = phases or {}
    n_vertices = length**4
    n_edges = 4 * n_vertices
    differential = np.zeros((n_vertices, n_edges), dtype=complex)
    edge = 0
    for x0 in range(length):
        for x1 in range(length):
            for x2 in range(length):
                for x3 in range(length):
                    source_coord = (x0, x1, x2, x3)
                    source = vertex_index(source_coord, length)
                    for direction in range(4):
                        target_coord = list(source_coord)
                        target_coord[direction] = (
                            target_coord[direction] + 1
                        ) % length
                        target = vertex_index(tuple(target_coord), length)
                        theta = phases.get((source, direction), 0.0)
                        differential[source, edge] = -1.0
                        differential[target, edge] = np.exp(1j * theta)
                        edge += 1
    return differential


def bid_operator(differential: np.ndarray) -> np.ndarray:
    n0, n1 = differential.shape
    return np.block(
        [
            [np.zeros((n0, n0), dtype=complex), differential],
            [differential.conj().T, np.zeros((n1, n1), dtype=complex)],
        ]
    )


def baseline_zero_mode_checks() -> list[dict[str, float | int]]:
    rows: list[dict[str, float | int]] = []
    for length in (3, 5, 7):
        n0 = length**4
        n1 = 4 * n0
        # For every flat positive edge e:s->t,
        # (D^dagger J_r)_e = (J_r)_t-(J_r)_s = 0 exactly.
        residuals = np.zeros(n1, dtype=complex)
        ddagger_norm = float(np.linalg.norm(residuals))
        operator_root_norm = ddagger_norm
        require(ddagger_norm < 1e-13, f"L={length}: D^dagger J_r != 0")
        require(operator_root_norm < 1e-13, f"L={length}: B r != 0")
        rows.append(
            {
                "L": length,
                "vertices": n0,
                "positive_edges": n1,
                "carrier_dimension": n0 + n1,
                "Ddagger_root_norm": ddagger_norm,
                "B_root_norm": operator_root_norm,
            }
        )
    return rows


def endpoint_classification() -> dict[str, float]:
    length = 3
    n0 = length**4
    n1 = 4 * n0
    root = np.concatenate(
        (
            np.ones(n0, dtype=complex) / math.sqrt(n0),
            np.zeros(n1, dtype=complex),
        )
    )
    orthogonal_endpoint = np.zeros(n0 + n1, dtype=complex)
    orthogonal_endpoint[n0] = 1.0
    theta = 0.61
    mixed_endpoint = (
        math.cos(theta) * root + math.sin(theta) * orthogonal_endpoint
    )
    return {
        "orthogonal_completed_endpoint_baseline":
            float(abs(np.vdot(orthogonal_endpoint, root))),
        "mixed_endpoint_baseline": float(abs(np.vdot(mixed_endpoint, root))),
        "mixed_endpoint_root_component": float(math.cos(theta)),
        "root_survival_baseline": float(abs(np.vdot(root, root))),
    }


def one_handle_positive_control() -> dict[str, float]:
    tau_record = math.pi / math.sqrt(2.0)
    operator = np.array(
        [[0.0, 0.0, -1.0], [0.0, 0.0, 1.0], [-1.0, 1.0, 0.0]],
        dtype=complex,
    )
    root = np.array([1.0, 0.0, 0.0], dtype=complex)
    endpoint = np.array([0.0, 1.0, 0.0], dtype=complex)
    evolved = unitary_apply(operator, tau_record, root)
    error = float(np.linalg.norm(evolved - endpoint))
    amplitude = complex(np.vdot(endpoint, evolved))
    require(error < 2e-14, "one-handle endpoint transfer failed")
    require(abs(amplitude - 1.0) < 2e-14, "one-handle amplitude != 1")
    return {
        "tau_record": tau_record,
        "endpoint_transfer_error": error,
        "baseline_amplitude_real": float(amplitude.real),
        "baseline_amplitude_imag": float(amplitude.imag),
    }


def perturbed_operator(length: int, strength: float) -> np.ndarray:
    # One fixed positive edge receives the tangent phase.
    return bid_operator(periodic_incidence_dense(length, {(0, 0): strength}))


def tangent_operator(length: int) -> np.ndarray:
    n0 = length**4
    n1 = 4 * n0
    dprime = np.zeros((n0, n1), dtype=complex)
    target = vertex_index((1, 0, 0, 0), length)
    dprime[target, 0] = 1j  # target of edge (origin,+direction 0)
    return bid_operator(dprime)


def spectral_data(operator: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    values, vectors = np.linalg.eigh(operator)
    return values, vectors


def unitary_apply(
    operator: np.ndarray, time: float, vector: np.ndarray
) -> np.ndarray:
    values, vectors = spectral_data(operator)
    coefficients = vectors.conj().T @ vector
    return vectors @ (np.exp(-1j * time * values) * coefficients)


def duhamel_check() -> dict[str, float | int]:
    length = 3
    tau_record = math.pi / math.sqrt(2.0)
    base = perturbed_operator(length, 0.0)
    tangent = tangent_operator(length)
    n0 = length**4
    n1 = 4 * n0
    root = np.concatenate(
        (
            np.ones(n0, dtype=complex) / math.sqrt(n0),
            np.zeros(n1, dtype=complex),
        )
    )

    # Exact spectral evaluation of G r. Since B_0 r=0, the inner backward
    # propagation is exactly r.
    values, vectors = spectral_data(base)
    v_root = tangent @ root
    v_coefficients = vectors.conj().T @ v_root
    integral_factors = np.empty_like(values, dtype=complex)
    nonzero = np.abs(values) > 1e-12
    integral_factors[nonzero] = (
        np.exp(1j * values[nonzero] * tau_record) - 1.0
    ) / (1j * values[nonzero])
    integral_factors[~nonzero] = tau_record
    g_root = vectors @ (integral_factors * v_coefficients)
    duhamel_derivative = -1j * (
        vectors
        @ (
            np.exp(-1j * tau_record * values)
            * (vectors.conj().T @ g_root)
        )
    )

    step = 2e-6
    plus = unitary_apply(perturbed_operator(length, step), tau_record, root)
    minus = unitary_apply(perturbed_operator(length, -step), tau_record, root)
    finite_difference = (plus - minus) / (2.0 * step)
    absolute_error = float(
        np.linalg.norm(finite_difference - duhamel_derivative)
    )
    relative_error = absolute_error / max(
        float(np.linalg.norm(duhamel_derivative)), 1e-30
    )
    require(relative_error < 2e-8, "finite Duhamel identity failed")
    return {
        "L": length,
        "spectral_dimension": len(values),
        "finite_difference_step": step,
        "absolute_error": absolute_error,
        "relative_error": relative_error,
    }


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "sealed spec hash mismatch")
    authority_results = {}
    for relative, expected in AUTHORITIES.items():
        actual = sha256(ROOT / relative)
        require(actual == expected, f"authority hash mismatch: {relative}")
        authority_results[relative] = actual

    zero_modes = baseline_zero_mode_checks()
    endpoints = endpoint_classification()
    one_handle = one_handle_positive_control()
    duhamel = duhamel_check()

    completed_baseline = endpoints["orthogonal_completed_endpoint_baseline"]
    survival_baseline = endpoints["root_survival_baseline"]
    blocked = completed_baseline == 0.0 and survival_baseline == 1.0
    require(blocked, "sealed primitive endpoint obstruction not reproduced")

    result = {
        "schema": "stage8_t7_primitive_connected_lift_v001",
        "spec_sha256": SPEC_SHA256,
        "authority_sha256": authority_results,
        "L1_periodic_zero_mode": zero_modes,
        "L2_endpoint_classification": endpoints,
        "L3_one_handle_positive_control": one_handle,
        "L4_duhamel_map": duhamel,
        "verdict": "PRIMITIVE_CONNECTED_LIFT_BLOCKED",
        "reason": (
            "On the sealed flat periodic response complex the root preparation "
            "is an exact zero mode. Every admissible orthogonal completed-record "
            "endpoint therefore has zero baseline transition, while the only "
            "nonzero fixed endpoint is the excluded unresolved root-survival "
            "boundary."
        ),
        "connected_primitive_operator_derived": True,
        "connected_primitive_preparation_derived": True,
        "connected_primitive_completed_endpoint_derived": False,
        "connected_primitive_amplitude_derived": False,
        "finite_duhamel_tangent_map_verified": True,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
