#!/usr/bin/env python3
"""Adjudicate the scalar record amplitude of the actual finite parent."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_ACTUAL_PARENT_RECORD_AMPLITUDE_ADJUDICATION_SPEC_V001.md"
SPEC_SHA256 = "7d5041a4ed74235f7a6d5d027444e3bd0a675868ece9af383ab2e81dae713ac9"
OUT = ROOT / "stage8_execution/work/T07_actual_parent_record_amplitude.json"

AUTHORITIES = {
    "STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md":
        "5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e",
    "PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md":
        "532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md":
        "345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb",
    "BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md":
        "6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546",
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md":
        "6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb",
    "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md":
        "e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6",
    "STAGE8_T7_RELAYED_CONNECTED_PREPARATION_RETEST_RESULT_V001.md":
        "21b782b50e9b0ddf1785727ff625a2b933d370aaf539c9fea74982025279b729",
    "STAGE8_T7_CAUSAL_LINE_CONNECTION_RETURN_LIFT_RESULT_V001.md":
        "5096f4cc2421574badf392cad591787e12928d27335683b5c77d0d98cd8e5918",
    "stage8_execution/t7_causal_line_connection_return_lift/"
    "T07_CAUSAL_LINE_CONNECTION_RETURN_LIFT_V001.seal.sha256":
        "9be712d5728a6c2f78671fec4a53d3f026327c56c28b736369e3b6d05800b298",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pauli_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return sx, sy, sz


def dirac_data() -> tuple[np.ndarray, np.ndarray]:
    sx, sy, sz = pauli_matrices()
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma0 = np.block([[identity, zero], [zero, -identity]])
    spatial = [
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    ]
    gamma5 = 1j * gamma0 @ spatial[0] @ spatial[1] @ spatial[2]
    return gamma0 @ spatial[0], -1j * gamma0 @ gamma5


def c_partial_matrix() -> np.ndarray:
    return np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )


def embed_record(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    value = np.array([[1.0]], dtype=complex)
    for index in range(count):
        value = np.kron(
            value,
            operator if index == site else np.eye(3, dtype=complex),
        )
    return value


def diamond_time_marginal(local_time: float) -> float:
    if not 0.0 <= local_time <= 1.0:
        return 0.0
    return 32.0 * min(local_time, 1.0 - local_time) ** 3


def exp_hermitian(operator: np.ndarray, interval: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return (
        vectors
        @ np.diag(np.exp(-1.0j * interval * values))
        @ vectors.conjugate().T
    )


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
            + integrated_action * diamond_time_marginal(midpoint) * write
        )
        value = exp_hermitian(hamiltonian, dt) @ value
    return value


def spatial_derivative(site_count: int) -> np.ndarray:
    derivative = np.zeros((site_count, site_count), dtype=complex)
    for site in range(site_count):
        derivative[site, (site + 1) % site_count] += 0.5
        derivative[site, (site - 1) % site_count] -= 0.5
    return derivative


def record_kraus(
    unitary: np.ndarray,
    source_dimension: int,
    outcome: tuple[int, ...],
) -> np.ndarray:
    count = len(outcome)
    tensor = unitary.reshape(
        (source_dimension, *([3] * count), source_dimension, *([3] * count))
    )
    selection: list[object] = [slice(None), *outcome, slice(None)]
    selection.extend([0] * count)
    return tensor[tuple(selection)]


def scalar_residual(operator: np.ndarray) -> float:
    scalar = np.trace(operator) / operator.shape[0]
    return float(np.linalg.norm(operator - scalar * np.eye(operator.shape[0])))


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "Sealed specification drift")
    for relative, expected in AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"Authority drift: {relative}")

    site_count = 3
    record_count = 2
    source_dimension = 12
    record_dimension = 3**record_count
    alpha_x, source_incidence_spin = dirac_data()
    derivative = spatial_derivative(site_count)
    momentum = -1j * derivative
    h_source = np.kron(momentum, alpha_x)
    h_free = np.kron(h_source, np.eye(record_dimension, dtype=complex))

    eigenvalues, eigenvectors = np.linalg.eigh(h_source)
    tolerance = 1e-12
    negative = eigenvalues < -tolerance
    zero_modes = np.abs(eigenvalues) <= tolerance
    positive = eigenvalues > tolerance
    zero_projector = (
        eigenvectors[:, zero_modes] @ eigenvectors[:, zero_modes].conjugate().T
    )

    masks = (
        np.diag([1.0, 1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, 1.0]).astype(complex),
    )
    c_partial = c_partial_matrix()
    writes = tuple(
        np.kron(
            np.kron(masks[site], source_incidence_spin),
            embed_record(c_partial, site, record_count),
        )
        for site in range(record_count)
    )
    action = math.pi / math.sqrt(2.0)
    steps = 96
    first = pulse_unitary(h_free, writes[0], action, steps)
    second = pulse_unitary(h_free, writes[1], action, steps)
    total = second @ first

    outcomes = {}
    for first_label in range(3):
        for second_label in range(3):
            outcome = (first_label, second_label)
            kraus = record_kraus(total, source_dimension, outcome)
            zero_block = zero_projector @ kraus @ zero_projector
            outcomes[f"{first_label}{second_label}"] = {
                "frobenius_norm": float(np.linalg.norm(kraus)),
                "rank_at_1e-10": int(np.linalg.matrix_rank(kraus, tol=1e-10)),
                "scalar_residual": scalar_residual(kraus),
                "zero_mode_block_norm": float(np.linalg.norm(zero_block)),
            }

    one_record_dimension = 3
    first_only = first.reshape(
        source_dimension,
        one_record_dimension,
        one_record_dimension,
        source_dimension,
        one_record_dimension,
        one_record_dimension,
    )[:, :, 0, :, :, 0]
    # The second record is an untouched spectator during the first pulse.
    first_completed = first_only[:, 1, :, 0]
    source_site = np.array([1.0, 0.0, 0.0], dtype=complex)
    source_spin = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
    disclosed_regression_vector = np.kron(source_site, source_spin)
    first_completed_amplitude = np.vdot(
        disclosed_regression_vector,
        first_completed @ disclosed_regression_vector,
    )

    completed = outcomes["11"]
    finite_state_unique = False
    gaussian_shortcut_authorized = False
    one_handle_exact_reduction = bool(
        abs(first_completed_amplitude - 1.0) < 1e-10
    )
    zero_mode_ambiguity_active = bool(
        completed["zero_mode_block_norm"] > 1e-10
    )

    result = {
        "schema": "stage8_t7_actual_parent_record_amplitude_v001",
        "spec_sha256": SPEC_SHA256,
        "authorities_verified": len(AUTHORITIES),
        "actual_finite_parent_used": True,
        "ideal_projector_chain_used": False,
        "finite_source_spectrum": {
            "negative_mode_count": int(np.count_nonzero(negative)),
            "zero_mode_count": int(np.count_nonzero(zero_modes)),
            "positive_mode_count": int(np.count_nonzero(positive)),
            "minimum_eigenvalue": float(eigenvalues[0]),
            "maximum_eigenvalue": float(eigenvalues[-1]),
        },
        "finite_regulator_parent_state": {
            "negative_energy_covariance_fixed": True,
            "zero_mode_covariance_fixed_by_sealed_lineage": False,
            "same_regulator_state_unique": finite_state_unique,
            "zero_mode_ambiguity_active_in_completed_11_kraus":
                zero_mode_ambiguity_active,
        },
        "completed_record_kraus_operators": outcomes,
        "completed_11_kraus_is_scalar_on_source": bool(
            completed["scalar_residual"] < 1e-10
        ),
        "one_handle_regression": {
            "disclosed_finite_parent_vector_amplitude_real":
                float(first_completed_amplitude.real),
            "disclosed_finite_parent_vector_amplitude_imag":
                float(first_completed_amplitude.imag),
            "pinned_unit_amplitude_recovered": one_handle_exact_reduction,
        },
        "gaussian_shortcut": {
            "completed_record_kraus_proved_to_equal_second_quantization":
                False,
            "determinant_formula_authorized": gaussian_shortcut_authorized,
            "determinant_formula_used": False,
        },
        "scalarization": {
            "final_source_line_selected": False,
            "after_the_fact_source_trace_used": False,
            "existing_parent_state_defined_on_same_regulator": False,
            "unique_scalar_completed_record_amplitude_derived": False,
        },
        "overall_verdict": "ACTUAL_PARENT_RECORD_AMPLITUDE_BLOCKED",
        "finite_actual_parent_record_amplitude_derived": False,
        "connected_primitive_amplitude_derived": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }

    require(result["finite_source_spectrum"]["zero_mode_count"] > 0,
            "Expected finite-regulator zero modes were absent")
    require(zero_mode_ambiguity_active,
            "Zero-mode state ambiguity unexpectedly decoupled")
    require(completed["scalar_residual"] > 1e-6,
            "Completed source operator unexpectedly became scalar")
    require(not one_handle_exact_reduction,
            "Generic finite parent unexpectedly reproduced ideal root line")
    require(result["overall_verdict"] == "ACTUAL_PARENT_RECORD_AMPLITUDE_BLOCKED",
            "Gate did not fail closed")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
