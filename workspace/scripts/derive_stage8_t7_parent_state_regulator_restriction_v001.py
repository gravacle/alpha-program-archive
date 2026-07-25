#!/usr/bin/env python3
"""Derive finite parent states as restrictions of the continuum covariance."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_SPEC_V001.md"
SPEC_SHA256 = "3d598a19588ff79aea830f0c906f1ed3478d852efe94b0da278fe7921a4838c6"
OUT = ROOT / "stage8_execution/work/T07_parent_state_regulator_restriction.json"

AUTHORITIES = {
    "PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md":
        "532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb",
    "BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md":
        "6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546",
    "STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md":
        "5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    "STAGE8_T7_ACTUAL_PARENT_RECORD_AMPLITUDE_ADJUDICATION_RESULT_V001.md":
        "7aafba8667ac01f1c4326b0d714e838bf068eec7c8f4ce28ef03c8bef9d62098",
    "stage8_execution/t7_actual_parent_record_amplitude/"
    "T07_ACTUAL_PARENT_RECORD_AMPLITUDE_V001.seal.sha256":
        "322510075e1f8f6616eb47b1325f47963d90e8adaf20e83f7209c8be5f048b40",
    "BID_FULL_DIRAC_CAR_SOURCE_TYPING_DERIVATION_V001.md":
        "0fe3905aa14ed744bda883dd68aa799dc9bb90f4f5647b477be3f6de65330f57",
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


def alpha_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sx, sy, sz = pauli_matrices()
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma0 = np.block([[identity, zero], [zero, -identity]])
    spatial = tuple(
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    )
    return tuple(gamma0 @ gamma for gamma in spatial)


def cohort_covariance(
    momenta: tuple[tuple[float, float, float], ...],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    alphas = alpha_matrices()
    blocks = []
    occupied = []
    for momentum in momenta:
        h_block = sum(
            (
                momentum[index] * alphas[index]
                for index in range(3)
            ),
            np.zeros((4, 4), dtype=complex),
        )
        values, vectors = np.linalg.eigh(h_block)
        require(np.min(np.abs(values)) > 1e-12, "Zero momentum entered cohort")
        blocks.append(h_block)
        occupied.append(vectors[:, values < 0.0])

    dimension = 4 * len(momenta)
    h_total = np.zeros((dimension, dimension), dtype=complex)
    covariance = np.zeros_like(h_total)
    occupied_total = np.zeros((dimension, dimension // 2), dtype=complex)
    occupied_column = 0
    for index, (h_block, occupied_block) in enumerate(zip(blocks, occupied)):
        row = slice(4 * index, 4 * index + 4)
        h_total[row, row] = h_block
        covariance[row, row] = occupied_block @ occupied_block.conjugate().T
        width = occupied_block.shape[1]
        occupied_total[row, occupied_column:occupied_column + width] = (
            occupied_block
        )
        occupied_column += width
    return h_total, covariance, occupied_total


def slater_vector(occupied: np.ndarray) -> np.ndarray:
    dimension, particle_count = occupied.shape
    state = np.zeros(2**dimension, dtype=complex)
    for subset in itertools.combinations(range(dimension), particle_count):
        minor = occupied[np.array(subset), :]
        bitmask = sum(1 << index for index in subset)
        state[bitmask] = np.linalg.det(minor)
    state /= np.linalg.norm(state)
    return state


def annihilate(state: np.ndarray, mode: int, dimension: int) -> np.ndarray:
    result = np.zeros_like(state)
    lower_mask = (1 << mode) - 1
    for basis, amplitude in enumerate(state):
        if not (basis & (1 << mode)):
            continue
        sign = -1 if bin(basis & lower_mask).count("1") % 2 else 1
        result[basis ^ (1 << mode)] += sign * amplitude
    return result


def fock_covariance(state: np.ndarray, dimension: int) -> np.ndarray:
    annihilated = [annihilate(state, mode, dimension) for mode in range(dimension)]
    return np.array(
        [
            [
                np.vdot(annihilated[column], annihilated[row])
                for column in range(dimension)
            ]
            for row in range(dimension)
        ],
        dtype=complex,
    )


def cohort_report(
    momenta: tuple[tuple[float, float, float], ...],
) -> tuple[dict[str, object], np.ndarray, np.ndarray]:
    h_total, covariance, occupied = cohort_covariance(momenta)
    dimension = h_total.shape[0]
    dispersion_error = float(
        max(
            np.linalg.norm(
                h_total[4 * index:4 * index + 4, 4 * index:4 * index + 4]
                @ h_total[4 * index:4 * index + 4, 4 * index:4 * index + 4]
                - sum(value * value for value in momentum)
                * np.eye(4, dtype=complex)
            )
            for index, momentum in enumerate(momenta)
        )
    )
    state = slater_vector(occupied) if dimension <= 8 else None
    covariance_from_fock = (
        fock_covariance(state, dimension) if state is not None else None
    )
    report = {
        "momenta": [list(momentum) for momentum in momenta],
        "dimension": dimension,
        "zero_eigenvalue_count": int(
            np.count_nonzero(np.abs(np.linalg.eigvalsh(h_total)) <= 1e-12)
        ),
        "dispersion_error": dispersion_error,
        "covariance_idempotence_error": float(
            np.linalg.norm(covariance @ covariance - covariance)
        ),
        "covariance_hermiticity_error": float(
            np.linalg.norm(covariance - covariance.conjugate().T)
        ),
        "covariance_rank": int(np.linalg.matrix_rank(covariance, tol=1e-10)),
        "expected_half_dimension_rank": dimension // 2,
        "fock_density_trace": (
            float(np.vdot(state, state).real) if state is not None else None
        ),
        "fock_covariance_error": (
            float(np.linalg.norm(covariance_from_fock - covariance))
            if covariance_from_fock is not None
            else None
        ),
    }
    return report, covariance, h_total


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "Sealed specification drift")
    for relative, expected in AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"Authority drift: {relative}")

    small_momenta = ((1.0, 0.0, 0.0), (-1.0, 0.0, 0.0))
    large_momenta = (
        *small_momenta,
        (0.0, 1.0, 0.0),
        (0.0, -1.0, 0.0),
    )
    small, c_small, _ = cohort_report(small_momenta)
    large, c_large, _ = cohort_report(large_momenta)
    restriction_error = float(
        np.linalg.norm(c_large[:c_small.shape[0], :c_small.shape[1]] - c_small)
    )

    for report in (small, large):
        require(report["zero_eigenvalue_count"] == 0, "Finite cohort has zero mode")
        require(report["dispersion_error"] < 1e-12, "Dirac dispersion failed")
        require(
            report["covariance_idempotence_error"] < 1e-12,
            "Restricted covariance is not a projection",
        )
        require(
            report["covariance_hermiticity_error"] < 1e-12,
            "Restricted covariance is not Hermitian",
        )
        require(
            report["covariance_rank"] == report["expected_half_dimension_rank"],
            "Restricted covariance has the wrong rank",
        )
    require(restriction_error < 1e-12, "Nested state restriction failed")
    require(small["fock_density_trace"] is not None, "Fock regression missing")
    require(abs(small["fock_density_trace"] - 1.0) < 1e-12,
            "Finite Fock state is not normalized")
    require(small["fock_covariance_error"] < 1e-12,
            "Finite Fock covariance mismatch")

    result = {
        "schema": "stage8_t7_parent_state_regulator_restriction_v001",
        "spec_sha256": SPEC_SHA256,
        "authorities_verified": len(AUTHORITIES),
        "continuum_zero_set_measure_zero": True,
        "continuum_covariance_representative_independent": True,
        "finite_restriction_rule": "C_n=Q_n C Q_n",
        "small_cohort": small,
        "large_cohort": large,
        "nested_covariance_restriction_error": restriction_error,
        "momentum_inversion_pairs_retained": True,
        "new_zero_mode_filling_adopted": False,
        "thermal_parameter_introduced": False,
        "old_three_site_regression_used_as_state_regulator": False,
        "parent_state_regulator_restriction_derived": True,
        "overall_verdict": "PARENT_STATE_REGULATOR_RESTRICTION_DERIVED",
        "finite_actual_parent_record_amplitude_derived": False,
        "connected_primitive_amplitude_derived": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
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
