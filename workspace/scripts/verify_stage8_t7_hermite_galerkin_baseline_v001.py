#!/usr/bin/env python3
"""Independent verification of the Hermite-Galerkin baseline diagnostic."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_HERMITE_GALERKIN_BASELINE_SPEC_V001.md"
SPEC_SHA256 = "80aa4e1722c117e8195ce0fb2ae3fc37262bc8fc2ba5d79a6dd38cd1029bc26d"
PRIMARY = ROOT / "stage8_execution/work/T07_hermite_galerkin_baseline.json"
OUT = ROOT / "stage8_execution/work/T07_hermite_galerkin_baseline_verification.json"

MIDPOINT_TO_STRANG_TOLERANCE = 5e-5
NESTING_TOLERANCE = 2e-12


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def midpoint_histories(
    n: int,
    ell: float,
    steps: int,
    alpha: tuple[np.ndarray, ...],
    incidence: np.ndarray,
) -> tuple[np.ndarray, ...]:
    h0 = h0_matrix(n, ell, alpha)
    dt = 1 / steps
    output = []
    for lam in (-math.sqrt(2), 0.0, math.sqrt(2)):
        u = np.eye(h0.shape[0], dtype=complex)
        for index in range(steps):
            s = (index + 0.5) / steps
            r = min(s, 1 - s)
            m = ball_matrix(r, n, ell, 14, 14, 28)
            h = h0 + lam * (math.pi / math.sqrt(2)) * 32 * r**3 * np.kron(
                m, incidence
            )
            u = exp_h(h, dt) @ u
        output.append(u)
    return tuple(output)


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


def read_complex(value: dict[str, float]) -> complex:
    return complex(value["real"], value["imag"])


def main() -> None:
    if sha256(SPEC) != SPEC_SHA256:
        raise RuntimeError("Sealed specification drift")
    primary = json.loads(PRIMARY.read_text())
    alpha, incidence = gamma_data()

    # Nested-subspace checks use explicit index injection, not a leading block.
    h2 = h0_matrix(2, 1.0, alpha)
    h4 = h0_matrix(4, 1.0, alpha)
    spatial_index = [
        (a * 4 + b) * 4 + c
        for a in range(2) for b in range(2) for c in range(2)
    ]
    spin_index = [4 * spatial + spin for spatial in spatial_index for spin in range(4)]
    h_nesting = np.linalg.norm(h4[np.ix_(spin_index, spin_index)] - h2)
    m2 = ball_matrix(0.37, 2, 1.0, 14, 14, 28)
    m4 = ball_matrix(0.37, 4, 1.0, 14, 14, 28)
    m_nesting = np.linalg.norm(m4[np.ix_(spatial_index, spatial_index)] - m2)

    c = mixed_c(2, alpha)
    h0 = h2
    values, vectors = np.linalg.eigh(h0)
    occupied = vectors[:, values < 0]
    histories_48 = midpoint_histories(2, 1.0, 48, alpha, incidence)
    histories_96 = midpoint_histories(2, 1.0, 96, alpha, incidence)
    midpoint_48 = amplitude(histories_48, c, occupied)
    midpoint_96 = amplitude(histories_96, c, occupied)

    primary_case = next(
        case for case in primary["cases"]
        if case["n"] == 2 and abs(case["ell"] - 1.0) < 1e-15
    )
    strang = (
        read_complex(primary_case["amplitudes"]["48"]["mixed"]),
        read_complex(primary_case["amplitudes"]["48"]["pure"]),
    )
    midpoint_tail = tuple(
        abs(left - right) for left, right in zip(midpoint_48, midpoint_96)
    )
    midpoint_to_strang = tuple(
        abs(left - right) for left, right in zip(midpoint_96, strang)
    )
    c_values = np.linalg.eigvalsh(c)
    reported_min = primary_case["mixed_covariance_minimum_eigenvalue"]
    reported_max = primary_case["mixed_covariance_maximum_eigenvalue"]

    checks = {
        "h0_nested_subspace_error": float(h_nesting),
        "cell_multiplier_nested_subspace_error": float(m_nesting),
        "mixed_covariance_min_q24": float(c_values[0]),
        "mixed_covariance_max_q24": float(c_values[-1]),
        "mixed_covariance_min_difference_from_q20": float(abs(c_values[0] - reported_min)),
        "mixed_covariance_max_difference_from_q20": float(abs(c_values[-1] - reported_max)),
        "midpoint_48_to_96_mixed": float(midpoint_tail[0]),
        "midpoint_48_to_96_pure": float(midpoint_tail[1]),
        "midpoint_96_to_strang_48_mixed": float(midpoint_to_strang[0]),
        "midpoint_96_to_strang_48_pure": float(midpoint_to_strang[1]),
    }
    passed = (
        h_nesting < NESTING_TOLERANCE
        and m_nesting < NESTING_TOLERANCE
        and abs(c_values[0] - reported_min) < 2e-4
        and abs(c_values[-1] - reported_max) < 2e-4
        and midpoint_tail[0] < MIDPOINT_TO_STRANG_TOLERANCE
        and midpoint_tail[1] < MIDPOINT_TO_STRANG_TOLERANCE
        and midpoint_to_strang[0] < MIDPOINT_TO_STRANG_TOLERANCE
        and midpoint_to_strang[1] < MIDPOINT_TO_STRANG_TOLERANCE
    )
    result = {
        "schema": "stage8_t7_hermite_galerkin_baseline_verification_v001",
        "spec_sha256": SPEC_SHA256,
        "checks": checks,
        "independent_integrator": "full-Hamiltonian midpoint exponential",
        "independent_ball_quadrature": "14x14x28 direct Hermite evaluation",
        "independent_covariance_quadrature_order": 24,
        "pass": passed,
        "physical_regulator_completed_record_baseline_derived": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise RuntimeError("Independent Hermite-Galerkin verification failed")


if __name__ == "__main__":
    main()
