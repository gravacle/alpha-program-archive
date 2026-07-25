#!/usr/bin/env python3
"""Execute the sealed genuine Hermite-Galerkin baseline diagnostic."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_HERMITE_GALERKIN_BASELINE_SPEC_V001.md"
SPEC_SHA256 = "80aa4e1722c117e8195ce0fb2ae3fc37262bc8fc2ba5d79a6dd38cd1029bc26d"
PROTOCOL = ROOT / "STAGE8_T7_HERMITE_GALERKIN_NUMERICS_PROTOCOL_V001.md"
PROTOCOL_SHA256 = "950e957ec2aa1022509b57df48f4f701e717e5dcbb18731332abbf55bf57dadd"
CORRECTION = ROOT / "STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md"
CORRECTION_SHA256 = "a1258dcf40732f0e3fce358a68ffdbd34bc347d70283550440582a1129bec510"
OUT = ROOT / "stage8_execution/work/T07_hermite_galerkin_baseline.json"

AUTHORITIES = {
    "STAGE8_T7_COMPLETED_CONTINUUM_RESPONSE_PROVENANCE_SPEC_V001.md":
        "6e24ceb6b18e6e6da5a6d21e872f90f6d79a324df9f305d226ab6edec863831b",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    "BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md":
        "6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546",
    "STAGE8_T7_GAUSSIAN_PATH_SUM_REDUCTION_RESULT_V001.md":
        "1fd82d0d42c7d7b1369adfa0e0061c80044afc847f7dae2f066bdfb89165e56f",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dirac_matrices() -> tuple[tuple[np.ndarray, ...], np.ndarray, float]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma0 = np.block([[identity, zero], [zero, -identity]])
    spatial = tuple(
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    )
    gamma5 = 1j * gamma0 @ spatial[0] @ spatial[1] @ spatial[2]
    alphas = tuple(gamma0 @ gamma for gamma in spatial)
    source_incidence = -1j * gamma0 @ gamma5
    clifford_error = max(
        np.linalg.norm(
            alphas[left] @ alphas[right]
            + alphas[right] @ alphas[left]
            - (2.0 * np.eye(4) if left == right else np.zeros((4, 4)))
        )
        for left in range(3)
        for right in range(3)
    )
    return alphas, source_incidence, float(clifford_error)


def momentum_1d(n: int, ell: float) -> np.ndarray:
    operator = np.zeros((n, n), dtype=complex)
    for column in range(n):
        if column + 1 < n:
            operator[column + 1, column] += (
                1j * math.sqrt(column + 1) / (math.sqrt(2.0) * ell)
            )
        if column - 1 >= 0:
            operator[column - 1, column] -= (
                1j * math.sqrt(column) / (math.sqrt(2.0) * ell)
            )
    return operator


def free_dirac(
    n: int,
    ell: float,
    alphas: tuple[np.ndarray, ...],
) -> np.ndarray:
    identity = np.eye(n, dtype=complex)
    p = momentum_1d(n, ell)
    momenta = (
        np.kron(np.kron(p, identity), identity),
        np.kron(np.kron(identity, p), identity),
        np.kron(np.kron(identity, identity), p),
    )
    return sum(
        (np.kron(momentum, alpha) for momentum, alpha in zip(momenta, alphas)),
        np.zeros((4 * n**3, 4 * n**3), dtype=complex),
    )


def normalized_hermite_functions(
    values: np.ndarray,
    n: int,
    ell: float,
) -> np.ndarray:
    scaled = values / ell
    polynomials = np.empty((len(values), n), dtype=float)
    polynomials[:, 0] = 1.0
    if n > 1:
        polynomials[:, 1] = 2.0 * scaled
    for order in range(2, n):
        polynomials[:, order] = (
            2.0 * scaled * polynomials[:, order - 1]
            - 2.0 * (order - 1) * polynomials[:, order - 2]
        )
    gaussian = np.exp(-0.5 * scaled**2)
    for order in range(n):
        normalization = (
            math.pi**0.25
            * math.sqrt((2**order) * math.factorial(order) * ell)
        )
        polynomials[:, order] *= gaussian / normalization
    return polynomials


def spatial_basis_values(
    x: np.ndarray,
    y: np.ndarray,
    z: np.ndarray,
    n: int,
    ell: float,
) -> np.ndarray:
    hx = normalized_hermite_functions(x, n, ell)
    hy = normalized_hermite_functions(y, n, ell)
    hz = normalized_hermite_functions(z, n, ell)
    return np.einsum("pa,pb,pc->pabc", hx, hy, hz).reshape(len(x), n**3)


def ball_multiplication(
    radius: float,
    n: int,
    ell: float,
    radial_count: int,
    polar_count: int,
    azimuth_count: int,
) -> np.ndarray:
    if radius <= 0.0:
        return np.zeros((n**3, n**3), dtype=complex)
    radial_node, radial_weight = np.polynomial.legendre.leggauss(radial_count)
    polar_node, polar_weight = np.polynomial.legendre.leggauss(polar_count)
    radial = 0.5 * radius * (radial_node + 1.0)
    radial_weight = 0.5 * radius * radial_weight
    azimuth = 2.0 * math.pi * np.arange(azimuth_count) / azimuth_count
    azimuth_weight = 2.0 * math.pi / azimuth_count

    rr, mm, pp = np.meshgrid(radial, polar_node, azimuth, indexing="ij")
    wr, wm, _ = np.meshgrid(
        radial_weight,
        polar_weight,
        np.ones(azimuth_count),
        indexing="ij",
    )
    sin_theta = np.sqrt(np.maximum(0.0, 1.0 - mm**2))
    x = (rr * sin_theta * np.cos(pp)).ravel()
    y = (rr * sin_theta * np.sin(pp)).ravel()
    z = (rr * mm).ravel()
    weights = (wr * wm * rr**2 * azimuth_weight).ravel()
    basis = spatial_basis_values(x, y, z, n, ell)
    matrix = basis.conjugate().T @ (weights[:, None] * basis)
    return 0.5 * (matrix + matrix.conjugate().T)


def mixed_covariance(
    n: int,
    alphas: tuple[np.ndarray, ...],
    quadrature_order: int = 20,
) -> np.ndarray:
    nodes, weights = np.polynomial.hermite.hermgauss(quadrature_order)
    polynomials = np.empty((quadrature_order, n), dtype=float)
    polynomials[:, 0] = 1.0 / math.pi**0.25
    if n > 1:
        polynomials[:, 1] = 2.0 * nodes / (
            math.pi**0.25 * math.sqrt(2.0)
        )
    for order in range(2, n):
        raw = (
            2.0 * nodes
            * polynomials[:, order - 1]
            * math.sqrt((2 ** (order - 1)) * math.factorial(order - 1))
            - 2.0 * (order - 1)
            * polynomials[:, order - 2]
            * math.sqrt((2 ** (order - 2)) * math.factorial(order - 2))
        )
        polynomials[:, order] = raw / math.sqrt(
            (2**order) * math.factorial(order)
        )

    px, py, pz = np.meshgrid(nodes, nodes, nodes, indexing="ij")
    wx, wy, wz = np.meshgrid(weights, weights, weights, indexing="ij")
    radius = np.sqrt(px**2 + py**2 + pz**2)
    directions = (px / radius, py / radius, pz / radius)
    basis_real = np.einsum(
        "pa,qb,rc->pqrabc", polynomials, polynomials, polynomials
    ).reshape(quadrature_order**3, n**3)
    degrees = np.array(
        [a + b + c for a in range(n) for b in range(n) for c in range(n)]
    )
    basis = basis_real * ((-1j) ** degrees)[None, :]
    volume_weights = (wx * wy * wz).ravel()

    direction_matrices = []
    for direction in directions:
        matrix = basis.conjugate().T @ (
            (volume_weights * direction.ravel())[:, None] * basis
        )
        direction_matrices.append(0.5 * (matrix + matrix.conjugate().T))
    spatial_identity = np.eye(n**3, dtype=complex)
    covariance = 0.5 * np.kron(spatial_identity, np.eye(4, dtype=complex))
    for direction_matrix, alpha in zip(direction_matrices, alphas):
        covariance -= 0.5 * np.kron(direction_matrix, alpha)
    return 0.5 * (covariance + covariance.conjugate().T)


def exp_hermitian(operator: np.ndarray, time: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return vectors @ np.diag(np.exp(-1j * time * values)) @ vectors.conjugate().T


def apply_interaction(
    value: np.ndarray,
    multiplication: np.ndarray,
    source_incidence: np.ndarray,
    theta: float,
) -> np.ndarray:
    spatial_values, spatial_vectors = np.linalg.eigh(multiplication)
    cos_matrix = (
        spatial_vectors
        @ np.diag(np.cos(theta * spatial_values))
        @ spatial_vectors.conjugate().T
    )
    sin_matrix = (
        spatial_vectors
        @ np.diag(np.sin(theta * spatial_values))
        @ spatial_vectors.conjugate().T
    )
    spatial_dimension = multiplication.shape[0]
    column_dimension = value.shape[1]
    tensor = value.reshape(spatial_dimension, 4, column_dimension)
    cosine = np.einsum("ab,bid->aid", cos_matrix, tensor, optimize=True)
    sine = np.einsum("ab,bjd->ajd", sin_matrix, tensor, optimize=True)
    sine = np.einsum("ij,ajd->aid", source_incidence, sine, optimize=True)
    return (cosine - 1j * sine).reshape(value.shape)


def cell_matrices(
    n: int,
    ell: float,
    time_steps: int,
    quadrature: tuple[int, int, int],
) -> tuple[np.ndarray, ...]:
    radial, polar, azimuth = quadrature
    return tuple(
        ball_multiplication(
            min((index + 0.5) / time_steps, 1.0 - (index + 0.5) / time_steps),
            n,
            ell,
            radial,
            polar,
            azimuth,
        )
        for index in range(time_steps)
    )


def propagate_histories(
    h0: np.ndarray,
    source_incidence: np.ndarray,
    multiplications: tuple[np.ndarray, ...],
) -> tuple[np.ndarray, ...]:
    time_steps = len(multiplications)
    dt = 1.0 / time_steps
    half_free = exp_hermitian(h0, 0.5 * dt)
    free_full = exp_hermitian(h0, 1.0)
    tau = math.pi / math.sqrt(2.0)
    histories = []
    for record_value in (-math.sqrt(2.0), 0.0, math.sqrt(2.0)):
        if record_value == 0.0:
            histories.append(free_full)
            continue
        value = np.eye(h0.shape[0], dtype=complex)
        for index, multiplication in enumerate(multiplications):
            midpoint = (index + 0.5) / time_steps
            radius = min(midpoint, 1.0 - midpoint)
            envelope = 32.0 * radius**3
            value = half_free @ value
            value = apply_interaction(
                value,
                multiplication,
                source_incidence,
                record_value * tau * envelope * dt,
            )
            value = half_free @ value
        histories.append(value)
    return tuple(histories)


def determinant_from_covariance(covariance: np.ndarray, unitary: np.ndarray) -> complex:
    matrix = np.eye(covariance.shape[0], dtype=complex) - covariance + covariance @ unitary
    sign, logarithm = np.linalg.slogdet(matrix)
    return complex(sign * np.exp(logarithm))


def determinant_from_occupied(occupied: np.ndarray, unitary: np.ndarray) -> complex:
    matrix = occupied.conjugate().T @ unitary @ occupied
    sign, logarithm = np.linalg.slogdet(matrix)
    return complex(sign * np.exp(logarithm))


def completed_amplitudes(
    histories: tuple[np.ndarray, ...],
    covariance: np.ndarray,
    occupied: np.ndarray,
) -> tuple[complex, complex, list[complex], list[complex]]:
    weights = (-0.25, 0.5, -0.25)
    mixed_terms = [
        determinant_from_covariance(covariance, unitary)
        for unitary in histories
    ]
    pure_terms = [
        determinant_from_occupied(occupied, unitary)
        for unitary in histories
    ]
    mixed = sum(weight * term for weight, term in zip(weights, mixed_terms))
    pure = sum(weight * term for weight, term in zip(weights, pure_terms))
    return mixed, pure, mixed_terms, pure_terms


def complex_json(value: complex) -> dict[str, float]:
    return {"real": float(value.real), "imag": float(value.imag)}


def execute_case(
    n: int,
    ell: float,
    alphas: tuple[np.ndarray, ...],
    source_incidence: np.ndarray,
) -> dict[str, object]:
    h0 = free_dirac(n, ell, alphas)
    h0_values, h0_vectors = np.linalg.eigh(h0)
    zero_count = int(np.count_nonzero(np.abs(h0_values) < 1e-11))
    occupied = h0_vectors[:, h0_values < 0.0]
    pure_covariance = occupied @ occupied.conjugate().T
    covariance = mixed_covariance(n, alphas)
    covariance_values = np.linalg.eigvalsh(covariance)

    amplitudes = {}
    maximum_unitarity_error = 0.0
    maximum_multiplication_hermiticity = 0.0
    for time_steps in (12, 24, 48):
        multiplications = cell_matrices(n, ell, time_steps, (10, 10, 20))
        maximum_multiplication_hermiticity = max(
            maximum_multiplication_hermiticity,
            max(
                float(np.linalg.norm(matrix - matrix.conjugate().T))
                for matrix in multiplications
            ),
        )
        histories = propagate_histories(h0, source_incidence, multiplications)
        maximum_unitarity_error = max(
            maximum_unitarity_error,
            max(
                float(
                    np.linalg.norm(
                        unitary.conjugate().T @ unitary
                        - np.eye(unitary.shape[0], dtype=complex)
                    )
                )
                for unitary in histories
            ),
        )
        mixed, pure, mixed_terms, pure_terms = completed_amplitudes(
            histories, covariance, occupied
        )
        amplitudes[str(time_steps)] = {
            "mixed": complex_json(mixed),
            "pure": complex_json(pure),
            "mixed_history_terms": [complex_json(value) for value in mixed_terms],
            "pure_history_terms": [complex_json(value) for value in pure_terms],
        }

    secondary_multiplications = cell_matrices(n, ell, 48, (12, 12, 24))
    secondary_histories = propagate_histories(
        h0, source_incidence, secondary_multiplications
    )
    secondary_mixed, secondary_pure, _, _ = completed_amplitudes(
        secondary_histories, covariance, occupied
    )

    def stored_complex(step: int, scheme: str) -> complex:
        stored = amplitudes[str(step)][scheme]
        return complex(stored["real"], stored["imag"])

    convergence = {}
    time_pass = True
    for scheme in ("mixed", "pure"):
        a12 = stored_complex(12, scheme)
        a24 = stored_complex(24, scheme)
        a48 = stored_complex(48, scheme)
        first = abs(a12 - a24)
        second = abs(a24 - a48)
        ratio = first / second if second else float("inf")
        improving = second < first
        second_order = ratio > 3.0
        time_pass = time_pass and improving
        convergence[scheme] = {
            "12_to_24": float(first),
            "24_to_48": float(second),
            "ratio": float(ratio),
            "improving": improving,
            "second_order_consistent": second_order,
            "secondary_quadrature_difference": float(
                abs(
                    a48
                    - (
                        secondary_mixed
                        if scheme == "mixed"
                        else secondary_pure
                    )
                )
            ),
        }

    covariance_violation = max(
        max(0.0, -float(covariance_values[0])),
        max(0.0, float(covariance_values[-1]) - 1.0),
    )
    report = {
        "n": n,
        "ell": ell,
        "spatial_dimension": n**3,
        "spinor_dimension": 4 * n**3,
        "h0_hermiticity_error": float(np.linalg.norm(h0 - h0.conjugate().T)),
        "h0_zero_mode_count": zero_count,
        "h0_smallest_absolute_eigenvalue": float(np.min(np.abs(h0_values))),
        "mixed_covariance_minimum_eigenvalue": float(covariance_values[0]),
        "mixed_covariance_maximum_eigenvalue": float(covariance_values[-1]),
        "mixed_covariance_bound_violation": covariance_violation,
        "mixed_covariance_hermiticity_error": float(
            np.linalg.norm(covariance - covariance.conjugate().T)
        ),
        "pure_covariance_rank": int(occupied.shape[1]),
        "pure_covariance_projector_error": float(
            np.linalg.norm(pure_covariance @ pure_covariance - pure_covariance)
        ),
        "maximum_multiplication_hermiticity_error": (
            maximum_multiplication_hermiticity
        ),
        "maximum_unitarity_error": maximum_unitarity_error,
        "amplitudes": amplitudes,
        "secondary_quadrature_48": {
            "mixed": complex_json(secondary_mixed),
            "pure": complex_json(secondary_pure),
        },
        "convergence": convergence,
        "time_convergence_pass": time_pass,
        "quadrature_pass": all(
            convergence[scheme]["secondary_quadrature_difference"] < 5e-4
            for scheme in ("mixed", "pure")
        ),
    }
    return report


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "Sealed specification drift")
    require(sha256(PROTOCOL) == PROTOCOL_SHA256, "Numerics protocol drift")
    require(sha256(CORRECTION) == CORRECTION_SHA256, "Authority correction drift")
    for relative, expected in AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"Authority drift: {relative}")

    alphas, source_incidence, clifford_error = dirac_matrices()
    cases = []
    for n in (2, 4):
        for ell in (1.0, math.sqrt(2.0)):
            cases.append(execute_case(n, ell, alphas, source_incidence))

    structural_pass = (
        clifford_error < 1e-12
        and all(case["h0_hermiticity_error"] < 1e-11 for case in cases)
        and all(
            case["maximum_multiplication_hermiticity_error"] < 1e-11
            for case in cases
        )
        and all(
            case["mixed_covariance_bound_violation"] < 5e-8
            for case in cases
        )
        and all(
            case["pure_covariance_projector_error"] < 1e-10
            for case in cases
        )
        and all(case["h0_zero_mode_count"] == 0 for case in cases)
        and all(case["maximum_unitarity_error"] < 2e-10 for case in cases)
    )
    numerics_pass = (
        structural_pass
        and all(case["time_convergence_pass"] for case in cases)
        and all(case["quadrature_pass"] for case in cases)
    )
    verdict = (
        "GENUINE_HERMITE_GALERKIN_BASELINES_COMPUTED"
        if numerics_pass
        else "HERMITE_GALERKIN_NUMERICS_BLOCKED"
    )
    result = {
        "schema": "stage8_t7_hermite_galerkin_baseline_v001",
        "spec_sha256": SPEC_SHA256,
        "numerics_protocol_sha256": PROTOCOL_SHA256,
        "authority_correction_sha256": CORRECTION_SHA256,
        "clifford_error": clifford_error,
        "cases": cases,
        "structural_pass": structural_pass,
        "numerics_pass": numerics_pass,
        "overall_verdict": verdict,
        "genuine_nested_finite_rank_subspaces_used": True,
        "old_three_site_regression_used": False,
        "two_basis_scales_reported": True,
        "both_state_schemes_reported": True,
        "physical_regulator_completed_record_baseline_derived": False,
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
