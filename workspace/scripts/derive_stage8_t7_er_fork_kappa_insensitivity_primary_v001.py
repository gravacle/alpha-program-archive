#!/usr/bin/env python3
"""ER-fork kappa-insensitivity bound gate - PRIMARY execution lane.

Sealed authorities (verified by hash before any computation):
  STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_BOUND_SPEC_V002.md          (spec)
  STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_V002_EXECUTION_NARROWING_BINDING_V001.md
  STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md (Phase-A
      Strang order F A G A F; b_D; J = -B_D (x) alpha_x)
  Sealed finite comparison lane (carrier n=2 ell=1, envelopes, 5e-5):
      STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_SPEC_V001.md
      STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_NUMERICAL_FAILURE_V001.md
      STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_NUMERICS_SUCCESSOR_SPEC_V001.md
      scripts/derive_stage8_t7_envelope_realization_comparison_v002.py
      scripts/verify_stage8_t7_envelope_realization_comparison_v002.py
      scripts/derive_stage8_t7_hermite_galerkin_baseline_v001.py
      scripts/verify_stage8_t7_hermite_galerkin_baseline_v001.py
      stage8_execution/work/T07_envelope_realization_comparison_v002.json
      stage8_execution/work/T07_envelope_realization_comparison_verification_v002.json

Numerical machinery below is FILE-COPIED verbatim from the sealed comparison
lane scripts (module import of the sealed executors is not used, per the
execution narrowing).  New content is exactly the pinned assembly of the
sealed spec V002 section "Connection assembly" plus the exact-rational
D3/D4 layer of the spec and the narrowing binding (N1, N2, N4).

This lane writes NO .seal file.  The construction lane seals after the
blind comparison (binding N5).
"""

from __future__ import annotations

import hashlib
import json
import math
import platform
import sys
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, getcontext
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "stage8_execution/work/T07_er_fork_kappa_insensitivity_primary_v001.json"

SEALED_AUTHORITIES = {
    # path -> pinned sha256 (from verified .seal.sha256 files)
    "STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_BOUND_SPEC_V002.md":
        "1e79b0b7baf9734c5c0d91a6f37db189c270a5dd88de31da4cee13b7bb8a099d",
    "STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_V002_EXECUTION_NARROWING_BINDING_V001.md":
        "e37d39911992c91fddf4960caec9e512657922c83645bc8acd69dca34f156f78",
    "STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_BOUND_SPEC_V001.md":
        "277654eed085e0e3fce0924536f27bd2fbbf1ef54f3a0336fdb45c071be1bfb4",
    "STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md":
        "789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3",
}

RECORDED_AUTHORITIES = {
    # path -> sha256 recorded at execution time (comparison lane artifacts;
    # the result JSON's internal spec_sha256 is cross-checked below)
    "STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_SPEC_V001.md":
        "4059eff522426d06d41d2a0542ddf6be309867bd077491d84c6998b2098ede31",
    "STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_NUMERICAL_FAILURE_V001.md":
        "808bfd544e14bbe13801946379fb1c19ce622d972df66c92e4bde0a59fc292c6",
    "STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_NUMERICS_SUCCESSOR_SPEC_V001.md":
        "fa4d6aad94aee991472c52db0a03dcd495634faa6e07c998ca4dea68f1f1db8f",
    "scripts/derive_stage8_t7_envelope_realization_comparison_v002.py":
        "57f9b37a8a926eaf3e96cae44f8f4ff3bc3c419d3f71269fedc2270f7b5ce23c",
    "scripts/verify_stage8_t7_envelope_realization_comparison_v002.py":
        "8494de074b05b3a2fc3db3708f43398285c5ce4a1a863236304918b68d9337a1",
    "scripts/derive_stage8_t7_hermite_galerkin_baseline_v001.py":
        "9213371ceaef31ad798d5cc252b7c5a55f7c5ca741fce7f26e882bd1a9a050a3",
    "scripts/verify_stage8_t7_hermite_galerkin_baseline_v001.py":
        "697ea5f48e98b240cabc5a6a28f39ed674dcd0057f71efb3a11eade221f7e768",
    "stage8_execution/work/T07_envelope_realization_comparison_v002.json":
        "b5161f845e83772c7d16fc530c62f182d3e7df6c35392ae1718d4cfed65f9bd2",
    "stage8_execution/work/T07_envelope_realization_comparison_verification_v002.json":
        "987afd7b6da8e18b0985dc70287490cdff3b2c3ee03fa5635298705d15f675d6",
}

SEALED_TABLE = ROOT / "stage8_execution/work/T07_envelope_realization_comparison_v002.json"
SEALED_VERIFICATION = (
    ROOT / "stage8_execution/work/T07_envelope_realization_comparison_verification_v002.json"
)

# Frozen definitions (sealed spec V002)
H_NODE = Fraction(7, 100)
H2 = Fraction(49, 10000)
THETA_AMP = Fraction(1, 20000)
D1_TOLERANCE = 5e-5
NODES = (("-7/100", -0.07), ("0", 0.0), ("+7/100", 0.07))
NODE_ABS_COEFFICIENT = {"-7/100": 1, "0": 2, "+7/100": 1}
PRIMARY_STEPS = (24, 48, 96)
INDEPENDENT_STEPS = (96, 192)
FLOATING_ADDEND = Fraction(1, 10**12)

N3_SCOPE_NOTE = (
    "Scope: resolvable a fortiori at battery-grade precision on this same\n"
    "finite proxy and carrier. This is NOT a demonstration that kappa_record\n"
    "differs between envelopes (the proxy-to-kappa_record link is underived\n"
    "and the intensive limit could contract a fixed-regulator difference),\n"
    "and NOT an output of the sealed battery (which pins ER-A as disclosed\n"
    "premise and never computes ER-B)."
)

N4_DIGIT_CORRECTION_NOTE = (
    "N4 (binding condition C4): at minZ = 6.791e-2 the floor evaluates to "
    "0.60148 (4 s.f. 0.6015); the V002 text's '0.6016...' was the "
    "6.79e-2-rounded value. The floor is frozen as a formula; no binding "
    "constant changes."
)


class GateBlocked(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GateBlocked(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# PRIMARY-LANE machinery, file-copied verbatim from the sealed
# scripts/derive_stage8_t7_hermite_galerkin_baseline_v001.py
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# File-copied verbatim from the sealed
# scripts/derive_stage8_t7_envelope_realization_comparison_v002.py
# ---------------------------------------------------------------------------

def envelope_value(mode: str, midpoint: float) -> float:
    radius = min(midpoint, 1.0 - midpoint)
    tau = math.pi / math.sqrt(2.0)
    if mode == "ER-A":
        return tau * 32.0 * radius**3
    if mode == "ER-B":
        return tau * 24.0 / math.pi
    raise ValueError(mode)


def stored_complex(value: dict[str, float]) -> complex:
    return complex(value["real"], value["imag"])


# ---------------------------------------------------------------------------
# INDEPENDENT-LANE machinery, file-copied verbatim from the sealed
# scripts/verify_stage8_t7_hermite_galerkin_baseline_v001.py and
# scripts/verify_stage8_t7_envelope_realization_comparison_v002.py
# ---------------------------------------------------------------------------

def gamma_data() -> tuple[tuple[np.ndarray, ...], np.ndarray]:
    pauli = (
        np.array([[0, 1], [1, 0]], complex),
        np.array([[0, -1j], [1j, 0]], complex),
        np.array([[1, 0], [0, -1]], complex),
    )
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    g0 = np.block([[identity, zero], [zero, -identity]])
    gs = tuple(np.block([[zero, s], [-s, zero]]) for s in pauli)
    g5 = 1j * g0 @ gs[0] @ gs[1] @ gs[2]
    return tuple(g0 @ g for g in gs), -1j * g0 @ g5


def p_matrix(n: int, ell: float) -> np.ndarray:
    result = np.zeros((n, n), dtype=complex)
    for a in range(n - 1):
        value = math.sqrt(a + 1) / (math.sqrt(2) * ell)
        result[a + 1, a] = 1j * value
        result[a, a + 1] = -1j * value
    return result


def h0_matrix(n: int, ell: float, alpha: tuple[np.ndarray, ...]) -> np.ndarray:
    identity = np.eye(n)
    p = p_matrix(n, ell)
    p3 = (
        np.kron(np.kron(p, identity), identity),
        np.kron(np.kron(identity, p), identity),
        np.kron(np.kron(identity, identity), p),
    )
    return sum(
        (np.kron(momentum, a) for momentum, a in zip(p3, alpha)),
        np.zeros((4 * n**3, 4 * n**3), complex),
    )


def hermite_values(x: np.ndarray, n: int, ell: float) -> np.ndarray:
    output = np.empty((x.size, n), dtype=float)
    scaled = x / ell
    for order in range(n):
        coefficient = np.zeros(order + 1)
        coefficient[-1] = 1.0
        polynomial = np.polynomial.hermite.hermval(scaled, coefficient)
        output[:, order] = (
            polynomial
            * np.exp(-0.5 * scaled**2)
            / (
                math.pi**0.25
                * math.sqrt((2**order) * math.factorial(order) * ell)
            )
        )
    return output


def ball_matrix(
    radius: float,
    n: int,
    ell: float,
    nr: int,
    nm: int,
    np_: int,
) -> np.ndarray:
    rn, rw = np.polynomial.legendre.leggauss(nr)
    mn, mw = np.polynomial.legendre.leggauss(nm)
    r = radius * (rn + 1) / 2
    rw = radius * rw / 2
    phi = 2 * math.pi * np.arange(np_) / np_
    rr, mm, pp = np.meshgrid(r, mn, phi, indexing="ij")
    wr, wm, _ = np.meshgrid(rw, mw, np.ones(np_), indexing="ij")
    sint = np.sqrt(1 - mm**2)
    x = (rr * sint * np.cos(pp)).ravel()
    y = (rr * sint * np.sin(pp)).ravel()
    z = (rr * mm).ravel()
    weight = (wr * wm * rr**2 * (2 * math.pi / np_)).ravel()
    hx, hy, hz = (
        hermite_values(coordinate, n, ell) for coordinate in (x, y, z)
    )
    basis = np.einsum("pa,pb,pc->pabc", hx, hy, hz).reshape(x.size, n**3)
    result = basis.T @ (weight[:, None] * basis)
    return (result + result.T) / 2


def mixed_c(n: int, alpha: tuple[np.ndarray, ...], q: int = 24) -> np.ndarray:
    node, weight = np.polynomial.hermite.hermgauss(q)
    g = np.empty((q, n), dtype=float)
    for order in range(n):
        coefficient = np.zeros(order + 1)
        coefficient[-1] = 1
        g[:, order] = np.polynomial.hermite.hermval(node, coefficient) / (
            math.pi**0.25 * math.sqrt((2**order) * math.factorial(order))
        )
    x, y, z = np.meshgrid(node, node, node, indexing="ij")
    wx, wy, wz = np.meshgrid(weight, weight, weight, indexing="ij")
    radius = np.sqrt(x**2 + y**2 + z**2)
    real_basis = np.einsum("pa,qb,rc->pqrabc", g, g, g).reshape(q**3, n**3)
    degrees = np.array(
        [a + b + c for a in range(n) for b in range(n) for c in range(n)]
    )
    basis = real_basis * ((-1j) ** degrees)[None, :]
    w = (wx * wy * wz).ravel()
    result = 0.5 * np.eye(4 * n**3, dtype=complex)
    for coordinate, a in zip((x, y, z), alpha):
        direction = coordinate.ravel() / radius.ravel()
        rj = basis.conjugate().T @ ((w * direction)[:, None] * basis)
        rj = (rj + rj.conjugate().T) / 2
        result -= 0.5 * np.kron(rj, a)
    return (result + result.conjugate().T) / 2


def exp_h(operator: np.ndarray, time: float) -> np.ndarray:
    value, vector = np.linalg.eigh(operator)
    return vector @ np.diag(np.exp(-1j * time * value)) @ vector.conjugate().T


def det_c(c: np.ndarray, u: np.ndarray) -> complex:
    sign, logabs = np.linalg.slogdet(np.eye(c.shape[0]) - c + c @ u)
    return complex(sign * np.exp(logabs))


def det_p(v: np.ndarray, u: np.ndarray) -> complex:
    sign, logabs = np.linalg.slogdet(v.conjugate().T @ u @ v)
    return complex(sign * np.exp(logabs))


def amplitude(
    histories: tuple[np.ndarray, ...],
    c: np.ndarray,
    occupied: np.ndarray,
) -> tuple[complex, complex]:
    weights = (-0.25, 0.5, -0.25)
    return (
        sum(w * det_c(c, u) for w, u in zip(weights, histories)),
        sum(w * det_p(occupied, u) for w, u in zip(weights, histories)),
    )


def independent_envelope(mode: str, midpoint: float) -> float:
    tau = math.pi / math.sqrt(2.0)
    if mode == "ER-A":
        radius = min(midpoint, 1.0 - midpoint)
        return tau * 32.0 * radius**3
    if mode == "ER-B":
        return tau * 24.0 / math.pi
    raise ValueError(mode)


# ---------------------------------------------------------------------------
# NEW: pinned connection assembly (sealed spec V002, choices (i)-(iii);
# Phase-A spec A2 for b_D and J = -B_D (x) alpha_x)
# ---------------------------------------------------------------------------

def b_d_profile(t: float, rho: np.ndarray) -> np.ndarray:
    """Smooth causal-diamond profile b_D(t, x) of the sealed Phase-A spec A2,
    evaluated on radii rho (b_D is radial in |x|).  supp b_D(t, .) is exactly
    the ball of radius r(t) = min(t, 1-t)."""
    s_minus = t * t - rho * rho
    s_plus = (1.0 - t) * (1.0 - t) - rho * rho
    inside = (t > 0.0) & (t < 1.0) & (s_minus > 0.0) & (s_plus > 0.0)
    out = np.zeros_like(rho)
    s = np.where(inside, s_minus * s_plus, 1.0)
    out[inside] = np.exp(16.0 - 1.0 / s[inside])
    return out


def ball_bd_primary(
    t: float,
    n: int,
    ell: float,
    radial_count: int,
    polar_count: int,
    azimuth_count: int,
) -> np.ndarray:
    """B_D(t) = Q b_D(t,.) Q with the sealed comparison lane's PRIMARY ball
    quadrature realization (ball_multiplication grid at radius r(t), weights
    multiplied by b_D at each node)."""
    radius = min(t, 1.0 - t)
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
    weights = weights * b_d_profile(t, rr.ravel())
    basis = spatial_basis_values(x, y, z, n, ell)
    matrix = basis.conjugate().T @ (weights[:, None] * basis)
    return 0.5 * (matrix + matrix.conjugate().T)


def ball_bd_independent(
    t: float,
    n: int,
    ell: float,
    nr: int,
    nm: int,
    np_: int,
) -> np.ndarray:
    """B_D(t) with the sealed comparison lane's INDEPENDENT ball quadrature
    realization (ball_matrix grid at radius r(t), weights multiplied by b_D)."""
    radius = min(t, 1.0 - t)
    rn, rw = np.polynomial.legendre.leggauss(nr)
    mn, mw = np.polynomial.legendre.leggauss(nm)
    r = radius * (rn + 1) / 2
    rw = radius * rw / 2
    phi = 2 * math.pi * np.arange(np_) / np_
    rr, mm, pp = np.meshgrid(r, mn, phi, indexing="ij")
    wr, wm, _ = np.meshgrid(rw, mw, np.ones(np_), indexing="ij")
    sint = np.sqrt(1 - mm**2)
    x = (rr * sint * np.cos(pp)).ravel()
    y = (rr * sint * np.sin(pp)).ravel()
    z = (rr * mm).ravel()
    weight = (wr * wm * rr**2 * (2 * math.pi / np_)).ravel()
    weight = weight * b_d_profile(t, rr.ravel())
    hx, hy, hz = (
        hermite_values(coordinate, n, ell) for coordinate in (x, y, z)
    )
    basis = np.einsum("pa,pb,pc->pabc", hx, hy, hz).reshape(x.size, n**3)
    result = basis.T @ (weight[:, None] * basis)
    return (result + result.T) / 2


def primary_histories_with_connection(
    h0: np.ndarray,
    source_incidence: np.ndarray,
    multiplications: tuple[np.ndarray, ...],
    connection_halves: tuple[np.ndarray, ...] | None,
    mode: str,
) -> tuple[np.ndarray, ...]:
    """Chronological Strang stepping per the pinned assembly:
    Step_lambda = F A G_lambda A F (Phase-A order, sealed spec V002 (i)).
    At a = 0 (connection_halves is None) this is bit-identical to the sealed
    comparison executor's propagate_histories, including the exact
    exp(-i h0 T) shortcut for the lambda = 0 history (assembly (ii))."""
    steps = len(multiplications)
    dt = 1.0 / steps
    half_free = exp_hermitian(h0, 0.5 * dt)
    free_full = exp_hermitian(h0, 1.0)
    output = []
    for record_value in (-math.sqrt(2.0), 0.0, math.sqrt(2.0)):
        if record_value == 0.0 and connection_halves is None:
            output.append(free_full)
            continue
        value = np.eye(h0.shape[0], dtype=complex)
        for index, multiplication in enumerate(multiplications):
            midpoint = (index + 0.5) / steps
            value = half_free @ value
            if connection_halves is not None:
                value = connection_halves[index] @ value
            if record_value != 0.0:
                value = apply_interaction(
                    value,
                    multiplication,
                    source_incidence,
                    record_value * envelope_value(mode, midpoint) * dt,
                )
            if connection_halves is not None:
                value = connection_halves[index] @ value
            value = half_free @ value
        output.append(value)
    return tuple(output)


def independent_histories_with_connection(
    mode: str,
    a: float,
    steps: int,
    alpha: tuple[np.ndarray, ...],
    incidence: np.ndarray,
    cell_cache: dict,
) -> tuple[np.ndarray, ...]:
    """Full-Hamiltonian midpoint exponentials per the sealed comparison
    verification pattern, with h(t) = h0 + lambda v(t) M(t) (x) S + a J(t),
    J(t) = -B_D(t) (x) alpha_x."""
    n = 2
    ell = 1.0
    h0 = h0_matrix(n, ell, alpha)
    dt = 1.0 / steps
    output = []
    for lam in (-math.sqrt(2.0), 0.0, math.sqrt(2.0)):
        value = np.eye(h0.shape[0], dtype=complex)
        for index in range(steps):
            midpoint = (index + 0.5) / steps
            key = (steps, index)
            if key not in cell_cache:
                radius = min(midpoint, 1.0 - midpoint)
                cell_cache[key] = (
                    ball_matrix(radius, n, ell, 14, 14, 28),
                    ball_bd_independent(midpoint, n, ell, 14, 14, 28),
                )
            multiplication, bd = cell_cache[key]
            h = h0 + lam * independent_envelope(mode, midpoint) * np.kron(
                multiplication, incidence
            )
            if a != 0.0:
                h = h - a * np.kron(bd, alpha[0])
            value = exp_h(h, dt) @ value
        output.append(value)
    return tuple(output)


# ---------------------------------------------------------------------------
# Exact-rational / 50-digit outward-enclosure layer (spec D3/D4; binding N2)
# ---------------------------------------------------------------------------

getcontext().prec = 65

ULP50 = Fraction(1, 10**50)


def fraction_from_decimal(value: Decimal) -> Fraction:
    return Fraction(value)


def squared_modulus(z: complex) -> Fraction:
    return Fraction(z.real) ** 2 + Fraction(z.imag) ** 2


def sqrt_bounds(q: Fraction) -> tuple[Fraction, Fraction]:
    """Certified rational bounds lo <= sqrt(q) <= hi (verified exactly)."""
    if q == 0:
        return Fraction(0), Fraction(0)
    require(q > 0, "sqrt of negative rational")
    approx = (Decimal(q.numerator) / Decimal(q.denominator)).sqrt()
    center = fraction_from_decimal(approx)
    lo = center
    hi = center
    scale_down = 1 - ULP50
    scale_up = 1 + ULP50
    while lo * lo > q:
        lo *= scale_down
    while hi * hi < q:
        hi *= scale_up
    return lo, hi


def round_50_outward(lo: Fraction, hi: Fraction) -> tuple[Fraction, Fraction]:
    """Outward rounding of a rational interval to 50 significant decimal
    digits (binding N2)."""
    def directed(x: Fraction, rounding: str) -> Fraction:
        if x == 0:
            return x
        d = Decimal(x.numerator) / Decimal(x.denominator)
        exponent = d.adjusted() - 49
        quantum = Decimal(1).scaleb(exponent)
        quantized = d.quantize(quantum, rounding=rounding)
        # one-quantum outward guard against the 65-digit division rounding
        if rounding == ROUND_FLOOR:
            quantized -= quantum
        else:
            quantized += quantum
        return Fraction(quantized)
    return directed(lo, ROUND_FLOOR), directed(hi, ROUND_CEILING)


def log_bounds(m_lo: Fraction, m_hi: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Outward rational bounds for log over the modulus interval [m_lo, m_hi],
    carried at 65-digit decimal (>= the pinned 50 digits) with an outward
    guard of 1e-40 absolute per endpoint, then 50-digit outward rounding.
    Returns (L_lo, L_hi, enclosure_width)."""
    require(m_lo > 0, "undefined log: nonpositive certified modulus lower bound")
    guard = Fraction(1, 10**40)
    ln_lo = fraction_from_decimal(
        (Decimal(m_lo.numerator) / Decimal(m_lo.denominator)).ln()
    ) - guard
    ln_hi = fraction_from_decimal(
        (Decimal(m_hi.numerator) / Decimal(m_hi.denominator)).ln()
    ) + guard
    ln_lo, ln_hi = round_50_outward(ln_lo, ln_hi)
    return ln_lo, ln_hi, ln_hi - ln_lo


def abs_upper(z: complex) -> Fraction:
    return sqrt_bounds(squared_modulus(z))[1]


def abs_lower(z: complex) -> Fraction:
    return sqrt_bounds(squared_modulus(z))[0]


def frac_str(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def frac_float(x: Fraction) -> float:
    return x.numerator / x.denominator


# ---------------------------------------------------------------------------
# Gate execution
# ---------------------------------------------------------------------------

def main() -> None:
    blocked_trigger = None
    # --- Step 1: authority verification -----------------------------------
    for relative, expected in SEALED_AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"Authority drift: {relative}")
        seal_path = ROOT / (relative + ".seal.sha256")
        require(seal_path.exists(), f"Missing seal file: {relative}")
        sealed_line = seal_path.read_text().split()[0]
        require(sealed_line == expected, f"Seal-file drift: {relative}")
    for relative, expected in RECORDED_AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"Authority drift: {relative}")

    sealed_table = json.loads(SEALED_TABLE.read_text())
    require(
        sealed_table["spec_sha256"]
        == RECORDED_AUTHORITIES[
            "STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_NUMERICS_SUCCESSOR_SPEC_V001.md"
        ],
        "Sealed comparison result does not bind the sealed successor spec",
    )
    require(
        sealed_table["overall_verdict"]
        == "ENVELOPE_BRANCH_HIGH_RESOLUTION_BASELINES_COMPUTED",
        "Sealed comparison verdict is not the computed baseline",
    )
    sealed_verification = json.loads(SEALED_VERIFICATION.read_text())
    require(sealed_verification["pass"] is True, "Sealed comparison verification failed")

    sealed_case = next(
        case
        for case in sealed_table["cases"]
        if case["n"] == 2 and abs(case["ell"] - 1.0) < 1e-15
    )

    # --- carrier construction (primary lane) ------------------------------
    alphas, source_incidence, clifford_error = dirac_matrices()
    n, ell = 2, 1.0
    h0 = free_dirac(n, ell, alphas)
    values, vectors = np.linalg.eigh(h0)
    occupied = vectors[:, values < 0.0]
    covariance = mixed_covariance(n, alphas)

    # carrier construction (independent lane)
    alpha_ind, incidence_ind = gamma_data()
    c_ind = mixed_c(2, alpha_ind)
    h0_ind = h0_matrix(2, 1.0, alpha_ind)
    values_ind, vectors_ind = np.linalg.eigh(h0_ind)
    occupied_ind = vectors_ind[:, values_ind < 0.0]

    # cell matrices and connection factors for the primary lane
    primary_cells = {
        steps: cell_matrices(n, ell, steps, (10, 10, 20)) for steps in PRIMARY_STEPS
    }
    primary_bd = {
        steps: tuple(
            ball_bd_primary((k + 0.5) / steps, n, ell, 10, 10, 20)
            for k in range(steps)
        )
        for steps in PRIMARY_STEPS
    }
    primary_j = {
        steps: tuple(
            -np.kron(bd, alphas[0]) for bd in primary_bd[steps]
        )
        for steps in PRIMARY_STEPS
    }
    max_j_norm = max(
        float(np.linalg.norm(j, 2)) for j in primary_j[96]
    )

    def connection_halves(steps: int, a: float):
        if a == 0.0:
            return None
        dt = 1.0 / steps
        return tuple(
            exp_hermitian(a * j, 0.5 * dt) for j in primary_j[steps]
        )

    # --- D2: full grid -----------------------------------------------------
    max_unitarity_error = 0.0
    primary_z: dict = {}
    for mode in ("ER-A", "ER-B"):
        primary_z[mode] = {}
        for label, a in NODES:
            primary_z[mode][label] = {}
            for steps in PRIMARY_STEPS:
                histories = primary_histories_with_connection(
                    h0,
                    source_incidence,
                    primary_cells[steps],
                    connection_halves(steps, a),
                    mode,
                )
                max_unitarity_error = max(
                    max_unitarity_error,
                    max(
                        float(
                            np.linalg.norm(
                                u.conjugate().T @ u
                                - np.eye(u.shape[0], dtype=complex)
                            )
                        )
                        for u in histories
                    ),
                )
                mixed, pure, _, _ = completed_amplitudes(
                    histories, covariance, occupied
                )
                primary_z[mode][label][steps] = {"mixed": mixed, "pure": pure}

    independent_cache: dict = {}
    independent_z: dict = {}
    for mode in ("ER-A", "ER-B"):
        independent_z[mode] = {}
        for label, a in NODES:
            independent_z[mode][label] = {}
            for steps in INDEPENDENT_STEPS:
                histories = independent_histories_with_connection(
                    mode, a, steps, alpha_ind, incidence_ind, independent_cache
                )
                mixed, pure = amplitude(histories, c_ind, occupied_ind)
                independent_z[mode][label][steps] = {"mixed": mixed, "pure": pure}

    # --- D1: a = 0 regression against the sealed v002 tables ---------------
    d1_rows = []
    d1_max_drift = 0.0
    for mode in ("ER-A", "ER-B"):
        for steps in PRIMARY_STEPS:
            for state in ("mixed", "pure"):
                sealed_value = stored_complex(
                    sealed_case["branches"][mode]["amplitudes"][str(steps)][state]
                )
                recomputed = primary_z[mode]["0"][steps][state]
                drift = abs(recomputed - sealed_value)
                d1_max_drift = max(d1_max_drift, drift)
                d1_rows.append(
                    {
                        "envelope": mode,
                        "state": state,
                        "steps": steps,
                        "sealed": complex_json(sealed_value),
                        "recomputed": complex_json(recomputed),
                        "absolute_drift": drift,
                    }
                )
    d1_pass = d1_max_drift < D1_TOLERANCE

    # a = 0 independent-lane regression against the sealed 5e-5 discipline
    d1_independent = {}
    for mode in ("ER-A", "ER-B"):
        d1_independent[mode] = {}
        for state in ("mixed", "pure"):
            z96i = independent_z[mode]["0"][96][state]
            z192i = independent_z[mode]["0"][192][state]
            z96p = primary_z[mode]["0"][96][state]
            tail = abs(z96i - z192i)
            cross = abs(z192i - z96p)
            sealed_checks = sealed_verification["checks"][mode][state]
            d1_independent[mode][state] = {
                "midpoint_96_to_192": tail,
                "midpoint_192_to_primary_strang_96": cross,
                "sealed_midpoint_96_to_192": sealed_checks["midpoint_96_to_192"],
                "sealed_midpoint_192_to_primary_strang_96": sealed_checks[
                    "midpoint_192_to_primary_strang_96"
                ],
            }
            d1_pass = d1_pass and tail < D1_TOLERANCE and cross < D1_TOLERANCE
    require(d1_pass, f"D1 drift: max primary drift {d1_max_drift} vs 5e-5 discipline")

    # --- error budget e(node) (spec (iv) + binding N2 addend) --------------
    budget: dict = {}
    division_safety: dict = {}
    fence_ok = True
    log_nodes: dict = {}
    max_enclosure = Fraction(0)
    for mode in ("ER-A", "ER-B"):
        budget[mode] = {}
        division_safety[mode] = {}
        log_nodes[mode] = {}
        for state in ("mixed", "pure"):
            budget[mode][state] = {}
            division_safety[mode][state] = {}
            log_nodes[mode][state] = {}
            for label, _ in NODES:
                z48 = primary_z[mode][label][48][state]
                z96 = primary_z[mode][label][96][state]
                z96i = independent_z[mode][label][96][state]
                z192i = independent_z[mode][label][192][state]
                addend_strang = abs_upper(z96 - z48) / 3
                addend_cross = abs_upper(z96 - z192i)
                addend_independent = abs_upper(z192i - z96i) / 3
                e_node = (
                    addend_strang
                    + addend_cross
                    + addend_independent
                    + FLOATING_ADDEND
                )
                m_lo, m_hi = sqrt_bounds(squared_modulus(z96))
                witnessed_lower = m_lo - e_node
                witnessed_upper = m_hi + e_node
                fence_value = witnessed_lower
                if fence_value <= 2 * THETA_AMP:
                    fence_ok = False
                budget[mode][state][label] = {
                    "z96_primary": complex_json(z96),
                    "z48_primary": complex_json(z48),
                    "z96_independent": complex_json(z96i),
                    "z192_independent": complex_json(z192i),
                    "modulus_z96_primary": abs(z96),
                    "addend_strang_tail_third": frac_float(addend_strang),
                    "addend_primary_to_independent": frac_float(addend_cross),
                    "addend_independent_tail_third": frac_float(addend_independent),
                    "addend_floating": 1e-12,
                    "e_node": frac_float(e_node),
                    "e_node_rational": frac_str(e_node),
                    "witnessed_modulus_lower": frac_float(witnessed_lower),
                    "witnessed_modulus_lower_rational": frac_str(witnessed_lower),
                }
                division_safety[mode][state][label] = {
                    "witnessed_modulus_minus_e": frac_float(fence_value),
                    "two_theta_amp": frac_float(2 * THETA_AMP),
                    "fence_pass": bool(fence_value > 2 * THETA_AMP),
                }
                if witnessed_lower > 0:
                    # 50-digit outward enclosure of log|Z_96| (point value at
                    # N=96; truth distance is carried by delta_kappa, spec (iv))
                    p_lo, p_hi, p_width = log_bounds(m_lo, m_hi)
                    max_enclosure = max(max_enclosure, p_width)
                    log_nodes[mode][state][label] = {
                        "log_z96_lower_50d": str(
                            Decimal(p_lo.numerator) / Decimal(p_lo.denominator)
                        ),
                        "log_z96_upper_50d": str(
                            Decimal(p_hi.numerator) / Decimal(p_hi.denominator)
                        ),
                        "enclosure_contribution": frac_float(p_width),
                        "interval": (p_lo, p_hi),
                    }
                else:
                    log_nodes[mode][state][label] = None

    require(fence_ok, "Division-safety fence: |Z_96| - e(node) <= 2 theta_amp")
    require(
        all(
            log_nodes[mode][state][label] is not None
            for mode in ("ER-A", "ER-B")
            for state in ("mixed", "pure")
            for label, _ in NODES
        ),
        "Undefined log: certified modulus lower bound nonpositive",
    )
    require(
        max_enclosure < Fraction(1, 10**12),
        "Log-enclosure contribution exceeds 1e-12 (binding N2 blocks)",
    )

    # --- D3: kappa_proxy and certified errors ------------------------------
    inv_h2 = 1 / H2
    kappa: dict = {}
    delta_kappa_error: dict = {}
    for mode in ("ER-A", "ER-B"):
        kappa[mode] = {}
        delta_kappa_error[mode] = {}
        for state in ("mixed", "pure"):
            l_plus = log_nodes[mode][state]["+7/100"]["interval"]
            l_zero = log_nodes[mode][state]["0"]["interval"]
            l_minus = log_nodes[mode][state]["-7/100"]["interval"]
            k_lo = (-l_plus[1] + 2 * l_zero[0] - l_minus[1]) * inv_h2
            k_hi = (-l_plus[0] + 2 * l_zero[1] - l_minus[0]) * inv_h2
            kappa[mode][state] = {
                "kappa_proxy_96": (frac_float(k_lo) + frac_float(k_hi)) / 2,
                "interval": (k_lo, k_hi),
            }
            total = Fraction(0)
            for label, _ in NODES:
                e_node = Fraction(budget[mode][state][label]["e_node_rational"])
                # witnessed_modulus_lower_rational is |Z_96|_lo - e(node),
                # which is exactly the frozen denominator |Z_96| - e.
                denominator = Fraction(
                    budget[mode][state][label]["witnessed_modulus_lower_rational"]
                )
                total += NODE_ABS_COEFFICIENT[label] * (e_node / denominator)
            delta_kappa_error[mode][state] = total * inv_h2

    # --- floors (spec formula; N1 sum-floor) -------------------------------
    floors: dict = {}
    for mode in ("ER-A", "ER-B"):
        floors[mode] = {}
        for state in ("mixed", "pure"):
            min_z = min(
                Fraction(
                    budget[mode][state][label]["witnessed_modulus_lower_rational"]
                )
                for label, _ in NODES
            )
            require(min_z > THETA_AMP, "Floor undefined: minZ <= theta_amp")
            floor = Fraction(2, 49) / (min_z - THETA_AMP)
            floors[mode][state] = {"minZ": min_z, "floor": floor}

    # --- D4: per-state comparison in exact rationals ------------------------
    per_state: dict = {}
    any_resolvable = False
    for state in ("mixed", "pure"):
        ka = kappa["ER-A"][state]["interval"]
        kb = kappa["ER-B"][state]["interval"]
        d_lo = ka[0] - kb[1]
        d_hi = ka[1] - kb[0]
        if d_lo > 0:
            abs_lo = d_lo
        elif d_hi < 0:
            abs_lo = -d_hi
        else:
            abs_lo = Fraction(0)
        abs_hi = max(abs(d_lo), abs(d_hi))
        total_error = delta_kappa_error["ER-A"][state] + delta_kappa_error["ER-B"][state]
        certified_lower = abs_lo - total_error
        if certified_lower < 0:
            certified_lower = Fraction(0)
        certified_upper = abs_hi + total_error
        sum_floor = floors["ER-A"][state]["floor"] + floors["ER-B"][state]["floor"]
        resolvable = certified_lower > sum_floor
        any_resolvable = any_resolvable or resolvable
        per_state[state] = {
            "kappa_proxy_96_ER_A": kappa["ER-A"][state]["kappa_proxy_96"],
            "kappa_proxy_96_ER_B": kappa["ER-B"][state]["kappa_proxy_96"],
            "delta_kappa_point": kappa["ER-A"][state]["kappa_proxy_96"]
            - kappa["ER-B"][state]["kappa_proxy_96"],
            "delta_kappa_error_ER_A": frac_float(delta_kappa_error["ER-A"][state]),
            "delta_kappa_error_ER_B": frac_float(delta_kappa_error["ER-B"][state]),
            "abs_delta_kappa_certified_lower_bound": frac_float(certified_lower),
            "abs_delta_kappa_certified_lower_bound_rational": frac_str(certified_lower),
            "abs_delta_kappa_certified_upper_bound": frac_float(certified_upper),
            "floor_ER_A": frac_float(floors["ER-A"][state]["floor"]),
            "floor_ER_A_rational": frac_str(floors["ER-A"][state]["floor"]),
            "floor_ER_B": frac_float(floors["ER-B"][state]["floor"]),
            "floor_ER_B_rational": frac_str(floors["ER-B"][state]["floor"]),
            "sum_floor_N1": frac_float(sum_floor),
            "sum_floor_N1_rational": frac_str(sum_floor),
            "minZ_ER_A": frac_float(floors["ER-A"][state]["minZ"]),
            "minZ_ER_A_rational": frac_str(floors["ER-A"][state]["minZ"]),
            "minZ_ER_B": frac_float(floors["ER-B"][state]["minZ"]),
            "minZ_ER_B_rational": frac_str(floors["ER-B"][state]["minZ"]),
            "resolvable_exact_rational_comparison": bool(resolvable),
        }

    verdict = (
        "ER_FORK_RESOLVABLE_BY_BATTERY"
        if any_resolvable
        else "ER_FORK_NOT_RESOLVED_AT_FINITE_LANE_PRECISION"
    )

    # --- context-only amplitude-level facts (spec D5, review finding 6) ----
    context = {
        "label": "context-only; triggers no verdict (sealed spec V002 D5)",
        "sealed_amplitude_level_facts": (
            "|Delta Z| = 6.1e-2 pure / 5.7e-3 mixed at a = 0, both far above "
            "theta_amp (already sealed in the v002 comparison; amplitude-level "
            "distinguishability does not decide kappa-proxy curvature)"
        ),
        "sealed_table_ER_A_to_ER_B_absolute_difference_N96":
            sealed_case["ER_A_to_ER_B_absolute_difference_N96"],
        "recomputed_a0_difference_N96": {
            state: abs(
                primary_z["ER-A"]["0"][96][state] - primary_z["ER-B"]["0"][96][state]
            )
            for state in ("mixed", "pure")
        },
    }

    def serialize_z(table: dict) -> dict:
        out: dict = {}
        for mode, node_map in table.items():
            out[mode] = {}
            for label, step_map in node_map.items():
                out[mode][label] = {}
                for steps, states in step_map.items():
                    out[mode][label][str(steps)] = {
                        state: dict(
                            complex_json(z), modulus=abs(z)
                        )
                        for state, z in states.items()
                    }
        return out

    log_nodes_out = {
        mode: {
            state: {
                label: {
                    key: value
                    for key, value in entry.items()
                    if key != "interval"
                }
                for label, entry in state_map.items()
            }
            for state, state_map in mode_map.items()
        }
        for mode, mode_map in log_nodes.items()
    }

    result = {
        "schema": "stage8_t7_er_fork_kappa_insensitivity_primary_v001",
        "lane": "PRIMARY_EXECUTION_LANE (blind-comparison protocol N5; no seal written by this lane)",
        "date": "2026-07-25",
        "spec_sha256": SEALED_AUTHORITIES[
            "STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_BOUND_SPEC_V002.md"
        ],
        "narrowing_binding_sha256": SEALED_AUTHORITIES[
            "STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_V002_EXECUTION_NARROWING_BINDING_V001.md"
        ],
        "authorities_sealed": SEALED_AUTHORITIES,
        "authorities_recorded": RECORDED_AUTHORITIES,
        "runtime": {
            "python": sys.version,
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "carrier": {"n": 2, "ell": 1.0, "spinor_dimension": 32},
        "stencil": {
            "nodes": ["-7/100", "0", "+7/100"],
            "h": "7/100",
            "h_squared": "49/10000",
            "coefficients": [-1, 2, -1],
            "theta_amp": "1/20000",
        },
        "assembly": {
            "strang_order": "F A G_lambda A F (Phase-A order, chronological midpoints)",
            "connection": "J(t) = -B_D(t) (x) alpha_x; B_D = Q b_D(t,.) Q via sealed ball quadratures (primary 10x10x20, independent 14x14x28)",
            "lambda_zero_history": "full stepping F A A F when a != 0; exact exp(-i h0 T) shortcut only at a = 0",
            "resolutions": {
                "primary_strang": list(PRIMARY_STEPS),
                "independent_midpoint": list(INDEPENDENT_STEPS),
            },
            "max_connection_norm_J_N96": max_j_norm,
        },
        "clifford_error": clifford_error,
        "maximum_unitarity_error_primary": max_unitarity_error,
        "D1": {
            "tolerance": D1_TOLERANCE,
            "rows": d1_rows,
            "max_primary_drift": d1_max_drift,
            "independent_a0_checks": d1_independent,
            "pass": bool(d1_pass),
        },
        "D2_amplitudes_primary": serialize_z(primary_z),
        "D2_amplitudes_independent": serialize_z(independent_z),
        "error_budget": budget,
        "division_safety": {
            "fence": "block if |Z_96(node)| - e(node) <= 2 theta_amp = 1/10000",
            "per_node": division_safety,
            "fence_triggered": False,
        },
        "log_nodes_50_digit_outward": log_nodes_out,
        "max_log_enclosure_contribution": frac_float(max_enclosure),
        "D3_D4_per_state": per_state,
        "verdict": verdict,
        "predeclared_prediction_record": {
            "P1_P2_P3": "frozen prediction was NOT_RESOLVED for both states "
            "(spec V002 frozen predictions; calibration ledger notes this lane "
            "errs optimistic)",
            "prediction_held": verdict
            == "ER_FORK_NOT_RESOLVED_AT_FINITE_LANE_PRECISION",
        },
        "context_only_amplitude_facts": context,
        "notes": {
            "N4_digit_correction": N4_DIGIT_CORRECTION_NOTE,
        },
        "ER_A_selected": False,
        "ER_B_selected": False,
        "er_fork_insensitivity_bound_computed": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    if verdict == "ER_FORK_RESOLVABLE_BY_BATTERY":
        result["notes"]["N3_scope_note_verbatim"] = N3_SCOPE_NOTE

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "verdict": verdict,
                "D1_pass": bool(d1_pass),
                "D1_max_primary_drift": d1_max_drift,
                "per_state": {
                    state: {
                        "kappa_A": per_state[state]["kappa_proxy_96_ER_A"],
                        "kappa_B": per_state[state]["kappa_proxy_96_ER_B"],
                        "abs_delta_LB": per_state[state][
                            "abs_delta_kappa_certified_lower_bound"
                        ],
                        "floor_A": per_state[state]["floor_ER_A"],
                        "floor_B": per_state[state]["floor_ER_B"],
                        "sum_floor": per_state[state]["sum_floor_N1"],
                    }
                    for state in ("mixed", "pure")
                },
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    try:
        main()
    except GateBlocked as error:
        blocked = {
            "schema": "stage8_t7_er_fork_kappa_insensitivity_primary_v001",
            "verdict": "ER_FORK_INSENSITIVITY_GATE_BLOCKED",
            "block_trigger": str(error),
        }
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(blocked, indent=2, sort_keys=True) + "\n")
        print(json.dumps(blocked, indent=2))
        raise SystemExit(2)
