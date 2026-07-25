#!/usr/bin/env python3
"""Build the sealed Stage-8 T7 independent PRECOMPARISON bundle.

This lane is intentionally standalone.  It does not import the primary
executor or any project construction helper, and it never reads a future
primary or comparison artifact.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import stat
import sys
from pathlib import Path
from typing import Callable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SELF_RELATIVE = (
    "scripts/"
    "derive_stage8_t7_actual_parent_regulated_car_operator_response_"
    "independent_v002.py"
)
SPEC_RELATIVE = (
    "STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md"
)
SPEC_SHA256 = "789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3"
BUNDLE_SCHEMA = "stage8_t7_actual_parent_regulated_car_operator_response_bundle_v001"
GENERATOR_PIECES_SCHEMA = "stage8_t7_generator_pieces_v002"
RUNTIME_MARKER = "_stage8_t7_content_addressed_runtime_v001"
ATTESTATION_SCHEMA_V001 = "stage8_t7_content_addressed_runtime_attestation_v001"
RUNTIME_MANIFEST_SHA256 = (
    "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b"
)
IMPLEMENTATION_MANIFEST = (
    ROOT
    / "provenance"
    / "stage8_t7_actual_parent_regulated_car_operator_response_implementation_v001.json"
)
IMPLEMENTATION_SEAL = Path(f"{IMPLEMENTATION_MANIFEST}.seal.sha256")

OUTPUT_STEM = (
    "T07_actual_parent_regulated_car_operator_response_"
    "independent_precomparison_v001"
)
OUTPUT_DIRECTORY = ROOT / "stage8_execution" / "work"
OUTPUT_NPZ = OUTPUT_DIRECTORY / f"{OUTPUT_STEM}.npz"
OUTPUT_JSON = OUTPUT_DIRECTORY / f"{OUTPUT_STEM}.json"
FUTURE_OUTPUTS = (
    OUTPUT_DIRECTORY
    / "T07_actual_parent_regulated_car_operator_response_primary_v001.npz",
    OUTPUT_DIRECTORY
    / "T07_actual_parent_regulated_car_operator_response_primary_v001.json",
    OUTPUT_DIRECTORY
    / "T07_actual_parent_regulated_car_operator_response_comparison_v001.json",
)

SCHEMA = BUNDLE_SCHEMA
N = 2
SPATIAL_DIMENSION = N**3
SPIN_DIMENSION = 4
SOURCE_DIMENSION = SPATIAL_DIMENSION * SPIN_DIMENSION
RECORD_DIMENSION = 3
ELLS = (1.0, math.sqrt(2.0))
HISTORIES = (0.0, 0.07, -0.11, 0.13, 0.04)
HISTORY_PAIRS = ((0.0, 0.0), (0.07, -0.11), (0.13, 0.04))
RECORD_VALUES = (-math.sqrt(2.0), 0.0, math.sqrt(2.0))
RK4_RESOLUTIONS = (192, 384)
QUADRATURE = (12, 12, 24)
OVERLAP_QUADRATURE_ORDER = 16
READY_INDEX = 0
POINTER_INDEX = 1

AUTHORITIES = {
    SPEC_RELATIVE:
        SPEC_SHA256,
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    "STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md":
        "5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e",
    "STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md":
        "a1258dcf40732f0e3fce358a68ffdbd34bc347d70283550440582a1129bec510",
    "STAGE8_T7_HERMITE_GALERKIN_BASELINE_SPEC_V001.md":
        "80aa4e1722c117e8195ce0fb2ae3fc37262bc8fc2ba5d79a6dd38cd1029bc26d",
    "STAGE8_T7_HERMITE_GALERKIN_NUMERICS_PROTOCOL_V001.md":
        "950e957ec2aa1022509b57df48f4f701e717e5dcbb18731332abbf55bf57dadd",
    "STAGE8_T7_EXACT_HERMITE_MIXED_COVARIANCE_RESULT_V001.md":
        "235246abd1c4df69c80bda8f79494c342e30178504dadec411612c18d6f8685b",
    "STAGE8_T7_PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_RESULT_V001.md":
        "a79939adf1d7185fdf4d6ec5ccb929de2e4f5997bee2ed085c0d63164dc8e370",
    "STAGE8_T7_GAUSSIAN_PATH_SUM_REDUCTION_RESULT_V001.md":
        "1fd82d0d42c7d7b1369adfa0e0061c80044afc847f7dae2f066bdfb89165e56f",
    "stage8_execution/work/T07_hermite_galerkin_baseline.json":
        "87593740c5f35f68ea1c484c7ab304fbd12ee7b54f62f48f38417c80a2e33f7c",
    "stage8_execution/work/T07_hermite_galerkin_baseline_verification.json":
        "fc55cdedb059d31843b2490a9af2a74902c20acaed08793d64ff5c1e2a7f32f8",
    "STAGE8_ROUTE2_CAR_STATE_BRIDGE_SCOPE_CORRECTION_V001.md":
        "4e1282bc800c47441d255e9d9d576958608d955dce15f02969261cd6e601e268",
    "STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_"
    "AMENDMENT_V001.md":
        "8a7f52ffa2500d20ad834b11e3762ed114ee1a201f2fec18bcb119e3c7ead860",
    "STAGE8_ROUTE2_COMPLETE_QSPEC_STATE_BINDING_V001.md":
        "5cbcd28ee493ba43e3d36158d80c4202230f056808caf2b36420f08c38fbd0d7",
    "STAGE8_ROUTE1_SPECIAL_CASE_CONSISTENCY_BINDING_V001.md":
        "460e87522884e703968025081cceccc0153af3cda27410c397fc2a09a0b367e3",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md":
        "2f2aa7f7397b70616fa5c9e8ed628ca1d1e819bb698133a169c6d544086b3cde",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_RESULT_V001.md":
        "76f5505e3aa1fdc11102f782ed8ee40e49787bb38e3a2524e17b92fd8de46740",
    "scripts/derive_stage8_t7_primitive_operator_response_v001.py":
        "3d8aea1a4779b0bfe7a472dca1fab0642750e8e010e339b9e3b100197b75a18c",
    "provenance/stage8_t7_numpy_runtime_manifest_v001.json":
        "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b",
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md":
        "6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb",
}

READ_ALLOWLIST = frozenset({SELF_RELATIVE, *AUTHORITIES})
FORBIDDEN_FUTURE_READ_MARKERS = (
    "T07_actual_parent_regulated_car_operator_response_primary",
    "T07_actual_parent_regulated_car_operator_response_comparison",
)
SEMANTIC_READ_LEDGER: list[dict[str, str]] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def require_runtime_attestation() -> dict[str, object]:
    attestation = getattr(sys, RUNTIME_MARKER, None)
    require(
        isinstance(attestation, dict),
        "production execution requires the sealed Stage-8 runtime launcher",
    )
    require(
        attestation.get("schema") == ATTESTATION_SCHEMA_V001,
        "Stage-8 runtime-attestation schema mismatch",
    )
    require(
        attestation.get("runtime_manifest_sha256") == RUNTIME_MANIFEST_SHA256,
        "Stage-8 runtime-attestation manifest mismatch",
    )
    require(
        attestation.get("python_isolated") is True
        and attestation.get("python_no_site") is True,
        "Stage-8 isolated/no-site runtime flags are absent",
    )
    return dict(attestation)


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    with path.open("rb") as handle:
        digest = hashlib.sha256()
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def json_scalar(value: complex | float) -> float | list[float]:
    number = complex(value)
    if abs(number.imag) <= 1.0e-15:
        return float(number.real)
    return [float(number.real), float(number.imag)]


def verify_implementation_manifest() -> list[dict[str, str]]:
    require(IMPLEMENTATION_MANIFEST.is_file(), "implementation manifest missing")
    require(IMPLEMENTATION_SEAL.is_file(), "implementation manifest seal missing")
    seal_fields = IMPLEMENTATION_SEAL.read_text(encoding="ascii").strip().split()
    require(len(seal_fields) == 2, "malformed implementation-manifest seal")
    require(
        seal_fields[0] == sha256_file(IMPLEMENTATION_MANIFEST),
        "implementation-manifest seal mismatch",
    )
    manifest = json.loads(IMPLEMENTATION_MANIFEST.read_text(encoding="utf-8"))
    rows = manifest.get("files")
    require(isinstance(rows, list) and bool(rows), "empty implementation manifest")
    row_map = {str(row["path"]): str(row["sha256"]) for row in rows}
    require(
        row_map.get(SELF_RELATIVE) == sha256_file(Path(__file__).resolve()),
        "independent executor is not the presealed implementation",
    )
    verified: list[dict[str, str]] = []
    for relative, expected in sorted(row_map.items()):
        actual = sha256_file(ROOT / relative)
        require(actual == expected, f"presealed implementation drift: {relative}")
        verified.append({"path": relative, "sha256": actual})
    return verified


def assert_read_allowed(relative: str) -> None:
    require(relative in READ_ALLOWLIST, f"semantic read outside allowlist: {relative}")
    require(
        not any(marker in relative for marker in FORBIDDEN_FUTURE_READ_MARKERS),
        f"future primary/comparison read forbidden: {relative}",
    )


def tracked_read(relative: str) -> bytes:
    assert_read_allowed(relative)
    path = (ROOT / relative).resolve()
    require(ROOT.resolve() in path.parents, f"read escapes canonical root: {relative}")
    payload = path.read_bytes()
    SEMANTIC_READ_LEDGER.append(
        {"path": relative, "sha256": sha256_bytes(payload)}
    )
    return payload


def verify_authorities() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for relative, expected in AUTHORITIES.items():
        payload = tracked_read(relative)
        actual = sha256_bytes(payload)
        require(actual == expected, f"authority drift: {relative}")
        rows.append({"path": relative, "sha256": actual})
    require(
        not any(
            marker in relative
            for relative in READ_ALLOWLIST
            for marker in FORBIDDEN_FUTURE_READ_MARKERS
        ),
        "future primary/comparison path leaked into read allowlist",
    )
    return rows


def pauli_and_dirac() -> tuple[tuple[np.ndarray, ...], np.ndarray]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma0 = np.block([[identity, zero], [zero, -identity]])
    spatial_gamma = tuple(
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    )
    gamma5 = 1j * gamma0 @ spatial_gamma[0] @ spatial_gamma[1] @ spatial_gamma[2]
    alpha = tuple(gamma0 @ gamma for gamma in spatial_gamma)
    source_incidence = -1j * gamma0 @ gamma5
    return alpha, source_incidence


def primary_labels() -> tuple[tuple[int, int, int, int], ...]:
    return tuple(itertools.product(range(N), range(N), range(N), range(SPIN_DIMENSION)))


def independent_labels() -> tuple[tuple[int, int, int, int], ...]:
    # Deliberately distinct from primary (a,b,c,s): spin is slowest and the
    # spatial axes are enumerated c,b,a.
    return tuple(
        (a, b, c, spin)
        for spin in range(SPIN_DIMENSION)
        for c in reversed(range(N))
        for b in range(N)
        for a in reversed(range(N))
    )


def independent_phase(label: tuple[int, int, int, int]) -> complex:
    a, b, c, spin = label
    return (1j) ** ((a + 2 * b + 3 * c + spin) % 4)


def normalized_hermite_polynomials(nodes: np.ndarray) -> np.ndarray:
    values = np.empty((len(nodes), N), dtype=float)
    values[:, 0] = math.pi ** -0.25
    values[:, 1] = (
        2.0 * nodes
        / (math.pi**0.25 * math.sqrt(2.0))
    )
    return values


def prepropagation_overlap() -> np.ndarray:
    nodes, weights = np.polynomial.hermite.hermgauss(OVERLAP_QUADRATURE_ORDER)
    polynomials = normalized_hermite_polynomials(nodes)
    overlap_1d = polynomials.T @ (weights[:, None] * polynomials)
    prim = primary_labels()
    indep = independent_labels()
    overlap = np.zeros((SOURCE_DIMENSION, SOURCE_DIMENSION), dtype=complex)
    for row, left in enumerate(prim):
        for column, right in enumerate(indep):
            if left[3] != right[3]:
                continue
            overlap[row, column] = (
                overlap_1d[left[0], right[0]]
                * overlap_1d[left[1], right[1]]
                * overlap_1d[left[2], right[2]]
                * independent_phase(right)
            )
    return overlap


def momentum_1d(ell: float) -> np.ndarray:
    operator = np.zeros((N, N), dtype=complex)
    for column in range(N):
        if column + 1 < N:
            operator[column + 1, column] = (
                1j * math.sqrt(column + 1) / (math.sqrt(2.0) * ell)
            )
        if column - 1 >= 0:
            operator[column - 1, column] = (
                -1j * math.sqrt(column) / (math.sqrt(2.0) * ell)
            )
    return operator


def canonical_spatial_momenta(ell: float) -> tuple[np.ndarray, ...]:
    identity = np.eye(N, dtype=complex)
    momentum = momentum_1d(ell)
    return (
        np.kron(np.kron(momentum, identity), identity),
        np.kron(np.kron(identity, momentum), identity),
        np.kron(np.kron(identity, identity), momentum),
    )


def spatial_index(label: tuple[int, int, int, int]) -> int:
    return (label[0] * N + label[1]) * N + label[2]


def lift_spatial_spin(spatial: np.ndarray, spin: np.ndarray) -> np.ndarray:
    labels = independent_labels()
    phases = tuple(independent_phase(label) for label in labels)
    operator = np.empty((SOURCE_DIMENSION, SOURCE_DIMENSION), dtype=complex)
    for row, left in enumerate(labels):
        for column, right in enumerate(labels):
            operator[row, column] = (
                phases[row].conjugate()
                * spatial[spatial_index(left), spatial_index(right)]
                * spin[left[3], right[3]]
                * phases[column]
            )
    return operator


def free_dirac(ell: float, alpha: tuple[np.ndarray, ...]) -> np.ndarray:
    operator = np.zeros((SOURCE_DIMENSION, SOURCE_DIMENSION), dtype=complex)
    for momentum, alpha_axis in zip(canonical_spatial_momenta(ell), alpha):
        operator += lift_spatial_spin(momentum, alpha_axis)
    return 0.5 * (operator + operator.conjugate().T)


def normalized_hermite_functions(
    values: np.ndarray,
    ell: float,
) -> np.ndarray:
    scaled = values / ell
    result = np.empty((len(values), N), dtype=float)
    result[:, 0] = np.exp(-0.5 * scaled**2) / (
        math.pi**0.25 * math.sqrt(ell)
    )
    result[:, 1] = (
        math.sqrt(2.0)
        * scaled
        * np.exp(-0.5 * scaled**2)
        / (math.pi**0.25 * math.sqrt(ell))
    )
    return result


def spatial_basis_values(
    x: np.ndarray,
    y: np.ndarray,
    z: np.ndarray,
    ell: float,
) -> np.ndarray:
    hx = normalized_hermite_functions(x, ell)
    hy = normalized_hermite_functions(y, ell)
    hz = normalized_hermite_functions(z, ell)
    return np.einsum("pa,pb,pc->pabc", hx, hy, hz).reshape(len(x), SPATIAL_DIMENSION)


def smooth_diamond_bump(t: float, radius_squared: np.ndarray | float) -> np.ndarray:
    radius_squared_array = np.asarray(radius_squared, dtype=float)
    output = np.zeros_like(radius_squared_array)
    if not 0.0 < t < 1.0:
        return output
    minus = t * t - radius_squared_array
    plus = (1.0 - t) ** 2 - radius_squared_array
    active = (minus > 0.0) & (plus > 0.0)
    product = minus[active] * plus[active]
    output[active] = np.exp(16.0 - 1.0 / product)
    return output


def multiplication_matrices(
    t: float,
    ell: float,
    quadrature: tuple[int, int, int] = QUADRATURE,
) -> tuple[np.ndarray, np.ndarray]:
    radius = min(t, 1.0 - t)
    if radius <= 0.0:
        zero = np.zeros((SPATIAL_DIMENSION, SPATIAL_DIMENSION), dtype=complex)
        return zero.copy(), zero
    radial_count, polar_count, azimuth_count = quadrature
    radial_nodes, radial_weights = np.polynomial.legendre.leggauss(radial_count)
    polar_nodes, polar_weights = np.polynomial.legendre.leggauss(polar_count)
    radial = 0.5 * radius * (radial_nodes + 1.0)
    radial_weights = 0.5 * radius * radial_weights
    azimuth = 2.0 * math.pi * np.arange(azimuth_count) / azimuth_count
    azimuth_weight = 2.0 * math.pi / azimuth_count

    rr, mm, pp = np.meshgrid(radial, polar_nodes, azimuth, indexing="ij")
    wr, wm, _ = np.meshgrid(
        radial_weights,
        polar_weights,
        np.ones(azimuth_count),
        indexing="ij",
    )
    sin_theta = np.sqrt(np.maximum(0.0, 1.0 - mm**2))
    x = (rr * sin_theta * np.cos(pp)).ravel()
    y = (rr * sin_theta * np.sin(pp)).ravel()
    z = (rr * mm).ravel()
    base_weights = (wr * wm * rr**2 * azimuth_weight).ravel()
    basis = spatial_basis_values(x, y, z, ell)

    cell = basis.conjugate().T @ (base_weights[:, None] * basis)
    bump = smooth_diamond_bump(t, (rr**2).ravel())
    connection = basis.conjugate().T @ (
        (base_weights * bump)[:, None] * basis
    )
    cell = 0.5 * (cell + cell.conjugate().T)
    connection = 0.5 * (connection + connection.conjugate().T)
    return cell, connection


def diamond_envelope(t: float) -> float:
    if not 0.0 <= t <= 1.0:
        return 0.0
    return (math.pi / math.sqrt(2.0)) * 32.0 * min(t, 1.0 - t) ** 3


class IndependentModel:
    def __init__(self, ell: float):
        self.ell = ell
        self.alpha, self.source_incidence = pauli_and_dirac()
        self.h0 = free_dirac(ell, self.alpha)
        self.record = np.array(
            [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
            dtype=complex,
        )
        self._multiplication_cache: dict[float, tuple[np.ndarray, np.ndarray]] = {}

    def multiplication(self, t: float) -> tuple[np.ndarray, np.ndarray]:
        key = float(round(t, 15))
        if key not in self._multiplication_cache:
            self._multiplication_cache[key] = multiplication_matrices(t, self.ell)
        return self._multiplication_cache[key]

    def source_hamiltonian(self, t: float, history: float, record_value: float) -> np.ndarray:
        cell, bump = self.multiplication(t)
        incidence = lift_spatial_spin(cell, self.source_incidence)
        connection = -lift_spatial_spin(bump, self.alpha[0])
        return (
            self.h0
            + record_value * diamond_envelope(t) * incidence
            + history * connection
        )

    def direct_hamiltonian(self, t: float, history: float) -> np.ndarray:
        cell, bump = self.multiplication(t)
        incidence = lift_spatial_spin(cell, self.source_incidence)
        connection = -lift_spatial_spin(bump, self.alpha[0])
        return (
            np.kron(self.h0 + history * connection, np.eye(RECORD_DIMENSION))
            + diamond_envelope(t) * np.kron(incidence, self.record)
        )

    def maximum_connection_norm(self, resolution: int = RK4_RESOLUTIONS[-1]) -> float:
        maximum = 0.0
        for index in range(resolution + 1):
            t = index / resolution
            _, bump = self.multiplication(t)
            connection = -lift_spatial_spin(bump, self.alpha[0])
            maximum = max(maximum, float(np.linalg.norm(connection, ord=2)))
        return maximum

    def maximum_primitive_hermiticity_residual(self) -> float:
        residuals = [
            float(np.linalg.norm(self.h0 - self.h0.conjugate().T, ord=2)),
            float(np.linalg.norm(self.record - self.record.conjugate().T, ord=2)),
            float(
                np.linalg.norm(
                    self.source_incidence - self.source_incidence.conjugate().T,
                    ord=2,
                )
            ),
        ]
        residuals.extend(
            float(np.linalg.norm(matrix - matrix.conjugate().T, ord=2))
            for matrix in self.alpha
        )
        for cell, bump in self._multiplication_cache.values():
            residuals.append(
                float(np.linalg.norm(cell - cell.conjugate().T, ord=2))
            )
            residuals.append(
                float(np.linalg.norm(bump - bump.conjugate().T, ord=2))
            )
        return max(residuals)


def rk4_propagate(
    hamiltonian: Callable[[float], np.ndarray],
    dimension: int,
    steps: int,
) -> np.ndarray:
    dt = 1.0 / steps
    value = np.eye(dimension, dtype=complex)

    def derivative(t: float, state: np.ndarray) -> np.ndarray:
        return -1j * hamiltonian(t) @ state

    for index in range(steps):
        t = index * dt
        k1 = derivative(t, value)
        k2 = derivative(t + 0.5 * dt, value + 0.5 * dt * k1)
        k3 = derivative(t + 0.5 * dt, value + 0.5 * dt * k2)
        k4 = derivative(t + dt, value + dt * k3)
        value = value + dt * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
    return value


def record_spectral_data(
    record: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    eigenvalues, eigenvectors = np.linalg.eigh(record)
    order = np.argsort(eigenvalues)
    eigenvalues = eigenvalues[order]
    eigenvectors = eigenvectors[:, order]
    projectors = np.stack(
        [
            eigenvectors[:, index:index + 1]
            @ eigenvectors[:, index:index + 1].conjugate().T
            for index in range(RECORD_DIMENSION)
        ]
    )
    ready = np.eye(RECORD_DIMENSION, dtype=complex)[:, READY_INDEX]
    pointer = np.eye(RECORD_DIMENSION, dtype=complex)[:, POINTER_INDEX]
    probabilities = np.array(
        [np.vdot(ready, projector @ ready) for projector in projectors],
        dtype=complex,
    )
    pointer_weights = np.array(
        [np.vdot(pointer, projector @ ready) for projector in projectors],
        dtype=complex,
    )
    return eigenvalues, projectors, probabilities, pointer_weights


def kraus_from_direct(
    propagator: np.ndarray,
    *,
    source_dimension: int = SOURCE_DIMENSION,
    record_dimension: int = RECORD_DIMENSION,
    ready_index: int = READY_INDEX,
) -> np.ndarray:
    tensor = propagator.reshape(
        source_dimension,
        record_dimension,
        source_dimension,
        record_dimension,
    )
    return np.stack(
        [
            tensor[:, outcome, :, ready_index]
            for outcome in range(record_dimension)
        ]
    )


def kraus_from_spectral(
    propagators: np.ndarray,
    projectors: np.ndarray,
) -> np.ndarray:
    ready = np.eye(RECORD_DIMENSION, dtype=complex)[:, READY_INDEX]
    family = []
    for outcome in range(RECORD_DIMENSION):
        coefficient = np.array(
            [
                np.vdot(
                    np.eye(RECORD_DIMENSION, dtype=complex)[:, outcome],
                    projector @ ready,
                )
                for projector in projectors
            ]
        )
        family.append(
            sum(
                coefficient[index] * propagators[index]
                for index in range(RECORD_DIMENSION)
            )
        )
    return np.stack(family)


def aggregate_responses(
    left_kraus: np.ndarray,
    right_kraus: np.ndarray,
    pointer_index: int = POINTER_INDEX,
) -> tuple[np.ndarray, np.ndarray]:
    require(
        left_kraus.shape == right_kraus.shape
        and left_kraus.ndim == 3
        and left_kraus.shape[0] > pointer_index,
        "Kraus family inventory is inconsistent",
    )
    all_outcomes = sum(
        left_kraus[index].conjugate().T @ right_kraus[index]
        for index in range(left_kraus.shape[0])
    )
    pointer = (
        left_kraus[pointer_index].conjugate().T
        @ right_kraus[pointer_index]
    )
    return all_outcomes, pointer


def spectral_cross_responses(
    left: np.ndarray,
    right: np.ndarray,
    probabilities: np.ndarray,
    pointer_weights: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    cross = np.empty(
        (RECORD_DIMENSION, RECORD_DIMENSION, SOURCE_DIMENSION, SOURCE_DIMENSION),
        dtype=complex,
    )
    for mu in range(RECORD_DIMENSION):
        for lam in range(RECORD_DIMENSION):
            cross[mu, lam] = left[mu].conjugate().T @ right[lam]
    all_outcomes = sum(
        probabilities[lam] * cross[lam, lam]
        for lam in range(RECORD_DIMENSION)
    )
    pointer = sum(
        pointer_weights[mu].conjugate() * pointer_weights[lam] * cross[mu, lam]
        for mu in range(RECORD_DIMENSION)
        for lam in range(RECORD_DIMENSION)
    )
    return cross, all_outcomes, pointer


def matrix_residual(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.linalg.norm(left - right, ord=2))


def array_digest(array: np.ndarray) -> str:
    contiguous = np.ascontiguousarray(array)
    metadata = json.dumps(
        {"dtype": contiguous.dtype.str, "shape": contiguous.shape},
        separators=(",", ":"),
    ).encode("ascii")
    return sha256_bytes(metadata + b"\0" + contiguous.tobytes())


def array_manifest(arrays: dict[str, np.ndarray]) -> dict[str, dict[str, object]]:
    return {
        name: {
            "shape": list(value.shape),
            "dtype": value.dtype.str,
            "sha256": array_digest(value),
        }
        for name, value in sorted(arrays.items())
    }


def atomic_write_bundle(
    arrays: dict[str, np.ndarray],
    metadata: dict[str, object],
    npz_path: Path = OUTPUT_NPZ,
    json_path: Path = OUTPUT_JSON,
) -> None:
    npz_seal = Path(f"{npz_path}.seal.sha256")
    json_seal = Path(f"{json_path}.seal.sha256")
    require(not npz_path.exists(), f"immutable output already exists: {npz_path}")
    require(not json_path.exists(), f"immutable output already exists: {json_path}")
    require(not npz_seal.exists(), f"immutable output seal already exists: {npz_seal}")
    require(not json_seal.exists(), f"immutable output seal already exists: {json_seal}")
    require(npz_path.parent == json_path.parent, "bundle outputs must share a directory")
    npz_path.parent.mkdir(parents=True, exist_ok=True)
    npz_temporary = npz_path.with_name(f".{npz_path.name}.tmp")
    json_temporary = json_path.with_name(f".{json_path.name}.tmp")
    npz_seal_temporary = npz_seal.with_name(f".{npz_seal.name}.tmp")
    json_seal_temporary = json_seal.with_name(f".{json_seal.name}.tmp")
    require(not npz_temporary.exists(), f"stale temporary output: {npz_temporary}")
    require(not json_temporary.exists(), f"stale temporary output: {json_temporary}")
    require(
        not npz_seal_temporary.exists(),
        f"stale temporary output: {npz_seal_temporary}",
    )
    require(
        not json_seal_temporary.exists(),
        f"stale temporary output: {json_seal_temporary}",
    )
    committed: list[Path] = []
    try:
        with npz_temporary.open("wb") as handle:
            np.savez_compressed(handle, **arrays)
            handle.flush()
            os.fsync(handle.fileno())
        npz_hash = sha256_file(npz_temporary)
        payload = dict(metadata)
        try:
            payload["npz_path"] = str(npz_path.relative_to(ROOT))
        except ValueError:
            # Unit tests exercise the same transaction in an isolated
            # temporary directory; production uses the canonical work path.
            payload["npz_path"] = str(npz_path)
        payload["npz_sha256"] = npz_hash
        payload["arrays"] = array_manifest(arrays)
        encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
        with json_temporary.open("wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        json_hash = sha256_file(json_temporary)
        with npz_seal_temporary.open("x", encoding="ascii") as handle:
            handle.write(f"{npz_hash}  {npz_path.name}\n")
            handle.flush()
            os.fsync(handle.fileno())
        with json_seal_temporary.open("x", encoding="ascii") as handle:
            handle.write(f"{json_hash}  {json_path.name}\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(npz_temporary, npz_path)
        committed.append(npz_path)
        os.replace(json_temporary, json_path)
        committed.append(json_path)
        os.replace(npz_seal_temporary, npz_seal)
        committed.append(npz_seal)
        os.replace(json_seal_temporary, json_seal)
        committed.append(json_seal)
        for artifact in committed:
            artifact.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    except Exception:
        npz_temporary.unlink(missing_ok=True)
        json_temporary.unlink(missing_ok=True)
        npz_seal_temporary.unlink(missing_ok=True)
        json_seal_temporary.unlink(missing_ok=True)
        for artifact in reversed(committed):
            artifact.unlink(missing_ok=True)
        raise


def write_blocked_result(error: Exception) -> None:
    if OUTPUT_JSON.exists() or OUTPUT_NPZ.exists():
        return
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT_JSON.with_name(f".{OUTPUT_JSON.name}.blocked.tmp")
    require(not temporary.exists(), f"stale blocked-result temporary: {temporary}")
    payload = {
        "schema": SCHEMA,
        "lane": "independent",
        "spec_sha256": SPEC_SHA256,
        "overall_verdict": "ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_BLOCKED",
        "reason": str(error),
        "exception_type": type(error).__name__,
        "sealed": True,
        "immutable_bundle": True,
        "precomparison_committed": False,
        "primary_output_paths_readable_during_construction": False,
        "actual_parent_regulated_CAR_operator_response_derived": False,
        "actual_parent_same_carrier_one_source_restriction_derived": False,
        "actual_finite_parent_state_evaluation_derived": False,
        "actual_finite_parent_operator_to_scalar_bridge_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    try:
        with temporary.open("x", encoding="utf-8") as handle:
            json.dump(
                payload,
                handle,
                indent=2,
                sort_keys=True,
                ensure_ascii=True,
                allow_nan=False,
            )
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, OUTPUT_JSON)
        seal = Path(f"{OUTPUT_JSON}.seal.sha256")
        require(not seal.exists(), f"blocked-result seal already exists: {seal}")
        seal.write_text(
            f"{sha256_file(OUTPUT_JSON)}  {OUTPUT_JSON.name}\n",
            encoding="ascii",
        )
        for artifact in (OUTPUT_JSON, seal):
            artifact.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    finally:
        temporary.unlink(missing_ok=True)


def execute_case(
    ell: float,
    resolution: int,
    arrays: dict[str, np.ndarray],
) -> dict[str, object]:
    model = IndependentModel(ell)
    eigenvalues, projectors, probabilities, pointer_weights = record_spectral_data(
        model.record
    )
    spectral: dict[float, np.ndarray] = {}
    direct: dict[float, np.ndarray] = {}
    spectral_kraus: dict[float, np.ndarray] = {}
    direct_kraus: dict[float, np.ndarray] = {}
    prefix = f"ell_{ell:.16g}__rk4_{resolution}"

    arrays[f"{prefix}__h0"] = model.h0
    arrays[f"{prefix}__record_eigenvalues"] = eigenvalues
    arrays[f"{prefix}__record_projectors"] = projectors
    arrays[f"{prefix}__p_lambda"] = probabilities
    arrays[f"{prefix}__w_lambda"] = pointer_weights

    for history in HISTORIES:
        spectral[history] = np.stack(
            [
                rk4_propagate(
                    lambda t, a=history, lam=record_value: model.source_hamiltonian(
                        t, a, lam
                    ),
                    SOURCE_DIMENSION,
                    resolution,
                )
                for record_value in eigenvalues
            ]
        )
        direct[history] = rk4_propagate(
            lambda t, a=history: model.direct_hamiltonian(t, a),
            SOURCE_DIMENSION * RECORD_DIMENSION,
            resolution,
        )
        spectral_kraus[history] = kraus_from_spectral(
            spectral[history], projectors
        )
        direct_kraus[history] = kraus_from_direct(direct[history])
        history_label = f"a_{history:+.8f}"
        arrays[f"{prefix}__u_lambda__{history_label}"] = spectral[history]
        arrays[f"{prefix}__direct_W__{history_label}"] = direct[history]
        arrays[f"{prefix}__spectral_kraus__{history_label}"] = spectral_kraus[history]
        arrays[f"{prefix}__direct_kraus__{history_label}"] = direct_kraus[history]

    if resolution == RK4_RESOLUTIONS[-1]:
        ell_tag = f"ell{ELLS.index(ell)}"
        dt = 1.0 / resolution
        midpoint_times = [index * dt + 0.5 * dt for index in range(resolution)]
        arrays[f"genpiece_midpoint_times__{ell_tag}"] = np.asarray(
            midpoint_times, dtype=np.float64
        )
        arrays[f"genpiece_M_stack__{ell_tag}"] = np.stack(
            [model.multiplication(t)[0] for t in midpoint_times]
        ).astype(np.complex128)
        arrays[f"genpiece_B_stack__{ell_tag}"] = np.stack(
            [model.multiplication(t)[1] for t in midpoint_times]
        ).astype(np.complex128)
        arrays[f"genpiece_h0__{ell_tag}"] = model.h0.astype(np.complex128)
        arrays[f"genpiece_p_stack__{ell_tag}"] = np.stack(
            canonical_spatial_momenta(ell)
        ).astype(np.complex128)
        arrays["genpiece_alpha_stack"] = np.stack(model.alpha).astype(
            np.complex128
        )
        arrays["genpiece_Sn"] = model.source_incidence.astype(np.complex128)

    pair_results: dict[str, object] = {}
    maximum_kraus_residual = 0.0
    maximum_aggregate_residual = 0.0
    maximum_adjoint_residual = 0.0
    maximum_contraction_violation = 0.0
    maximum_same_history_residual = 0.0
    maximum_spectral_unitarity_residual = max(
        matrix_residual(
            value.conjugate().T @ value,
            np.eye(SOURCE_DIMENSION, dtype=complex),
        )
        for history_values in spectral.values()
        for value in history_values
    )
    maximum_direct_unitarity_residual = max(
        matrix_residual(
            value.conjugate().T @ value,
            np.eye(SOURCE_DIMENSION * RECORD_DIMENSION, dtype=complex),
        )
        for value in direct.values()
    )
    for plus, minus in HISTORY_PAIRS:
        pair_label = f"plus_{plus:+.8f}__minus_{minus:+.8f}"
        cross, gaussian_all, gaussian_pointer = spectral_cross_responses(
            spectral[minus],
            spectral[plus],
            probabilities,
            pointer_weights,
        )
        direct_all, direct_pointer = aggregate_responses(
            direct_kraus[minus], direct_kraus[plus]
        )
        spectral_all_from_kraus, spectral_pointer_from_kraus = aggregate_responses(
            spectral_kraus[minus], spectral_kraus[plus]
        )
        kraus_residuals = [
            matrix_residual(
                spectral_kraus[history][outcome],
                direct_kraus[history][outcome],
            )
            for history in (minus, plus)
            for outcome in range(RECORD_DIMENSION)
        ]
        aggregate_residuals = (
            matrix_residual(gaussian_all, direct_all),
            matrix_residual(gaussian_pointer, direct_pointer),
            matrix_residual(gaussian_all, spectral_all_from_kraus),
            matrix_residual(gaussian_pointer, spectral_pointer_from_kraus),
        )
        maximum_kraus_residual = max(maximum_kraus_residual, *kraus_residuals)
        maximum_aggregate_residual = max(
            maximum_aggregate_residual, *aggregate_residuals
        )
        maximum_contraction_violation = max(
            maximum_contraction_violation,
            max(0.0, float(np.linalg.norm(gaussian_all, ord=2)) - 1.0),
            max(0.0, float(np.linalg.norm(gaussian_pointer, ord=2)) - 1.0),
        )
        reverse_cross, reverse_all, reverse_pointer = spectral_cross_responses(
            spectral[plus],
            spectral[minus],
            probabilities,
            pointer_weights,
        )
        maximum_adjoint_residual = max(
            maximum_adjoint_residual,
            matrix_residual(gaussian_all.conjugate().T, reverse_all),
            matrix_residual(gaussian_pointer.conjugate().T, reverse_pointer),
        )
        arrays[f"{prefix}__cross__{pair_label}"] = cross
        arrays[f"{prefix}__reverse_cross__{pair_label}"] = reverse_cross
        arrays[f"{prefix}__gaussian_all__{pair_label}"] = gaussian_all
        arrays[f"{prefix}__gaussian_pointer__{pair_label}"] = gaussian_pointer
        arrays[f"{prefix}__direct_all__{pair_label}"] = direct_all
        arrays[f"{prefix}__direct_pointer__{pair_label}"] = direct_pointer
        pair_results[pair_label] = {
            "kraus_residuals": kraus_residuals,
            "aggregate_residuals": list(aggregate_residuals),
            "all_norm": float(np.linalg.norm(gaussian_all, ord=2)),
            "pointer_norm": float(np.linalg.norm(gaussian_pointer, ord=2)),
        }

    identity = np.eye(SOURCE_DIMENSION, dtype=complex)
    for history in HISTORIES:
        _, same_all, same_pointer = spectral_cross_responses(
            spectral[history],
            spectral[history],
            probabilities,
            pointer_weights,
        )
        maximum_same_history_residual = max(
            maximum_same_history_residual,
            matrix_residual(same_all, identity),
        )
        pointer_eigenvalues = np.linalg.eigvalsh(
            0.5 * (same_pointer + same_pointer.conjugate().T)
        )
        maximum_contraction_violation = max(
            maximum_contraction_violation,
            max(0.0, float(-pointer_eigenvalues[0])),
            max(0.0, float(pointer_eigenvalues[-1] - 1.0)),
        )

    return {
        "ell": ell,
        "resolution": resolution,
        "pair_results": pair_results,
        "maximum_direct_spectral_kraus_residual": maximum_kraus_residual,
        "maximum_direct_spectral_aggregate_residual": maximum_aggregate_residual,
        "maximum_adjoint_exchange_residual": maximum_adjoint_residual,
        "maximum_same_history_identity_residual": maximum_same_history_residual,
        "maximum_spectral_unitarity_residual":
            maximum_spectral_unitarity_residual,
        "maximum_direct_unitarity_residual": maximum_direct_unitarity_residual,
        "maximum_contraction_or_positivity_violation": maximum_contraction_violation,
        "maximum_connection_norm": model.maximum_connection_norm(),
        "maximum_primitive_hermiticity_residual":
            model.maximum_primitive_hermiticity_residual(),
        "spectral_completeness_residual": float(
            np.linalg.norm(projectors.sum(axis=0) - np.eye(RECORD_DIMENSION), ord=2)
        ),
        "probability_sum_residual": float(abs(probabilities.sum() - 1.0)),
        "record_eigenvalues": [float(value) for value in eigenvalues],
    }


def tail_metrics(
    arrays: dict[str, np.ndarray],
    ell: float,
) -> dict[str, float]:
    result: dict[str, float] = {}
    for plus, minus in HISTORY_PAIRS[1:]:
        pair_label = f"plus_{plus:+.8f}__minus_{minus:+.8f}"
        for kernel in ("gaussian_all", "gaussian_pointer", "direct_all", "direct_pointer"):
            left_key = f"ell_{ell:.16g}__rk4_192__{kernel}__{pair_label}"
            right_key = f"ell_{ell:.16g}__rk4_384__{kernel}__{pair_label}"
            result[f"{pair_label}__{kernel}"] = matrix_residual(
                arrays[left_key], arrays[right_key]
            )
    return result


def common_discrete_labels() -> dict[str, object]:
    return {
        "ell": [f"ell{index}" for index in range(len(ELLS))],
        "histories": [f"a{index}" for index in range(len(HISTORIES))],
        "history_pairs": [
            [f"a{HISTORIES.index(plus)}", f"a{HISTORIES.index(minus)}"]
            for plus, minus in HISTORY_PAIRS
        ],
        "pairs": [f"p{index}" for index in range(len(HISTORY_PAIRS))],
        "record_labels": [f"l{index}" for index in range(RECORD_DIMENSION)],
        "outcome_labels": [f"x{index}" for index in range(RECORD_DIMENSION)],
        "kernels": ["all", "pointer"],
    }


def add_common_component_arrays(
    arrays: dict[str, np.ndarray],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    record = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    values, projectors, probabilities, pointer_weights = record_spectral_data(record)
    for record_index, projector in enumerate(projectors):
        arrays[f"record_projector__l{record_index}"] = projector

    resolution = RK4_RESOLUTIONS[-1]
    for ell_index, ell in enumerate(ELLS):
        ell_tag = f"ell{ell_index}"
        prefix = f"ell_{ell:.16g}__rk4_{resolution}"
        arrays[f"diag_h0__{ell_tag}"] = arrays[f"{prefix}__h0"]
        diagnostic_model = IndependentModel(ell)
        _, midpoint_bump = diagnostic_model.multiplication(0.5)
        arrays[f"diag_connection_midpoint__{ell_tag}"] = -lift_spatial_spin(
            midpoint_bump,
            diagnostic_model.alpha[0],
        )
        for history_index, history in enumerate(HISTORIES):
            history_label = f"a_{history:+.8f}"
            propagators = arrays[f"{prefix}__u_lambda__{history_label}"]
            direct_kraus = arrays[f"{prefix}__direct_kraus__{history_label}"]
            for record_index in range(RECORD_DIMENSION):
                arrays[
                    f"common_u__{ell_tag}__a{history_index}__l{record_index}"
                ] = propagators[record_index]
            for outcome in range(RECORD_DIMENSION):
                arrays[
                    f"common_direct_kraus__{ell_tag}__a{history_index}__x{outcome}"
                ] = direct_kraus[outcome]
        for pair_index, (plus, minus) in enumerate(HISTORY_PAIRS):
            pair_label = f"plus_{plus:+.8f}__minus_{minus:+.8f}"
            cross = arrays[f"{prefix}__cross__{pair_label}"]
            for left in range(RECORD_DIMENSION):
                for right in range(RECORD_DIMENSION):
                    arrays[
                        f"common_cross__{ell_tag}__p{pair_index}"
                        f"__mu{left}__l{right}"
                    ] = cross[left, right]
            for kernel in ("all", "pointer"):
                arrays[
                    f"common_direct_{kernel}__{ell_tag}__p{pair_index}"
                ] = arrays[f"{prefix}__direct_{kernel}__{pair_label}"]
                arrays[
                    f"common_gaussian_{kernel}__{ell_tag}__p{pair_index}"
                ] = arrays[f"{prefix}__gaussian_{kernel}__{pair_label}"]
                if pair_index in (1, 2):
                    for diagnostic_resolution in RK4_RESOLUTIONS:
                        diagnostic_prefix = (
                            f"ell_{ell:.16g}__rk4_{diagnostic_resolution}"
                        )
                        arrays[
                            f"diag_independent__{ell_tag}"
                            f"__n{diagnostic_resolution}"
                            f"__p{pair_index}__{kernel}"
                        ] = arrays[
                            f"{diagnostic_prefix}__gaussian_{kernel}__{pair_label}"
                        ]
    return values, probabilities, pointer_weights


def common_component_manifest(
    arrays: dict[str, np.ndarray],
    record_values: np.ndarray,
    probabilities: np.ndarray,
    pointer_weights: np.ndarray,
) -> dict[str, object]:
    scalar_components: dict[str, dict[str, object]] = {
        "record_eigenvalues": {
            f"l{index}": json_scalar(value)
            for index, value in enumerate(record_values)
        },
        "coefficients": {
            **{
                f"p.l{index}": json_scalar(value)
                for index, value in enumerate(probabilities)
            },
            **{
                f"w.l{index}": json_scalar(value)
                for index, value in enumerate(pointer_weights)
            },
            **{
                f"ell.ell{index}": float(value)
                for index, value in enumerate(ELLS)
            },
            **{
                f"history.a{index}": float(value)
                for index, value in enumerate(HISTORIES)
            },
        },
    }
    matrix_components: dict[str, dict[str, str]] = {
        "record_projectors": {
            f"l{record_index}": f"record_projector__l{record_index}"
            for record_index in range(RECORD_DIMENSION)
        },
        "propagators": {},
        "cross_operators": {},
        "direct_kraus_members": {},
        "direct_responses": {},
        "aggregate_kernels": {},
    }
    for ell_index in range(len(ELLS)):
        ell_tag = f"ell{ell_index}"
        for history_index in range(len(HISTORIES)):
            for record_index in range(RECORD_DIMENSION):
                identifier = f"{ell_tag}.a{history_index}.l{record_index}"
                matrix_components["propagators"][identifier] = (
                    f"common_u__{ell_tag}__a{history_index}__l{record_index}"
                )
            for outcome in range(RECORD_DIMENSION):
                identifier = f"{ell_tag}.a{history_index}.x{outcome}"
                matrix_components["direct_kraus_members"][identifier] = (
                    f"common_direct_kraus__{ell_tag}__a{history_index}__x{outcome}"
                )
        for pair_index in range(len(HISTORY_PAIRS)):
            for left in range(RECORD_DIMENSION):
                for right in range(RECORD_DIMENSION):
                    identifier = (
                        f"{ell_tag}.p{pair_index}.mu{left}.l{right}"
                    )
                    matrix_components["cross_operators"][identifier] = (
                        f"common_cross__{ell_tag}__p{pair_index}"
                        f"__mu{left}__l{right}"
                    )
            for kernel in ("all", "pointer"):
                identifier = f"{ell_tag}.p{pair_index}.{kernel}"
                matrix_components["direct_responses"][identifier] = (
                    f"common_direct_{kernel}__{ell_tag}__p{pair_index}"
                )
                matrix_components["aggregate_kernels"][identifier] = (
                    f"common_gaussian_{kernel}__{ell_tag}__p{pair_index}"
                )
    referenced = {
        npz_key
        for category in matrix_components.values()
        for npz_key in category.values()
    }
    require(
        referenced <= set(arrays),
        "independent common component inventory is incomplete",
    )
    return {
        "dimensions": {
            "source_dimension": SOURCE_DIMENSION,
            "record_dimension": RECORD_DIMENSION,
            "spatial_dimension": SPATIAL_DIMENSION,
        },
        "discrete_labels": common_discrete_labels(),
        "scalar_components": scalar_components,
        "matrix_components": matrix_components,
        "basis_overlap_key": "basis_overlap_primary_from_independent",
        "npz_keys": sorted(arrays),
    }


def independent_comparison_diagnostics(
    arrays: dict[str, np.ndarray],
    cases: list[dict[str, object]],
    tails: dict[str, dict[str, float]],
    record_values: np.ndarray,
    probabilities: np.ndarray,
) -> dict[str, object]:
    local_fields = (
        "maximum_direct_spectral_kraus_residual",
        "maximum_direct_spectral_aggregate_residual",
        "maximum_adjoint_exchange_residual",
        "maximum_same_history_identity_residual",
        "maximum_spectral_unitarity_residual",
        "maximum_direct_unitarity_residual",
        "maximum_contraction_or_positivity_violation",
        "maximum_primitive_hermiticity_residual",
        "spectral_completeness_residual",
        "probability_sum_residual",
    )
    local_gate_maxima = {
        field: max(float(case[field]) for case in cases)
        for field in local_fields
    }
    local_gate_maxima["record_eigenvalue_error"] = float(
        np.max(np.abs(record_values - np.asarray(RECORD_VALUES)))
    )
    normalized_tails: dict[str, dict[str, float]] = {}
    connection: dict[str, dict[str, float]] = {}
    resolution = RK4_RESOLUTIONS[-1]
    for ell_index, ell in enumerate(ELLS):
        ell_tag = f"ell{ell_index}"
        raw_tail = tails[f"ell_{ell:.16g}"]
        normalized_tails[ell_tag] = {}
        for pair_index, (plus, minus) in enumerate(HISTORY_PAIRS[1:], start=1):
            pair_label = f"plus_{plus:+.8f}__minus_{minus:+.8f}"
            for kernel in ("all", "pointer"):
                normalized_tails[ell_tag][f"p{pair_index}.{kernel}"] = float(
                    raw_tail[f"{pair_label}__gaussian_{kernel}"]
                )
        production_prefix = f"ell_{ell:.16g}__rk4_{resolution}"
        plus, minus = HISTORY_PAIRS[1]
        pair_label = f"plus_{plus:+.8f}__minus_{minus:+.8f}"
        signal = matrix_residual(
            arrays[f"{production_prefix}__gaussian_all__{pair_label}"],
            np.eye(SOURCE_DIMENSION, dtype=complex),
        )
        production_case = next(
            case
            for case in cases
            if float(case["ell"]) == float(ell)
            and int(case["resolution"]) == resolution
        )
        connection[ell_tag] = {
            "signal_norm": float(signal),
            "maximum_connection_norm": float(
                production_case["maximum_connection_norm"]
            ),
        }
    return {
        "local_gate_maxima": local_gate_maxima,
        "independent_rk4_tails": normalized_tails,
        "connection": connection,
        "record_probability_sum": float(abs(np.sum(probabilities) - 1.0)),
    }


def current_route2_route1_architecture_reduction(
    arrays: dict[str, np.ndarray],
) -> dict[str, object]:
    """Independent O6 reduction of the current Stinespring/PVM architecture."""

    ready = np.ones(2, dtype=complex)
    ready /= np.linalg.norm(ready)
    completed_vector = ready.copy()
    other_vector = np.array([1.0, -1.0], dtype=complex)
    other_vector /= np.linalg.norm(other_vector)
    projectors = (
        completed_vector[:, None] @ completed_vector[None, :].conjugate(),
        other_vector[:, None] @ other_vector[None, :].conjugate(),
    )
    comparator_basis = np.column_stack((completed_vector, other_vector))
    generator = np.diag([0.0, 1.0]).astype(complex)

    def spectral_unitary(theta: float) -> np.ndarray:
        eigenvalues, eigenvectors = np.linalg.eigh(generator)
        return (
            eigenvectors
            @ np.diag(np.exp(1j * theta * eigenvalues))
            @ eigenvectors.conjugate().T
        )

    route1_histories = HISTORIES[1:]
    unitaries = {theta: spectral_unitary(theta) for theta in route1_histories}
    arrays["diag_route1_ready"] = ready
    arrays["diag_route1_projector__completed"] = projectors[0]
    arrays["diag_route1_projector__other"] = projectors[1]
    for history_index, theta in enumerate(route1_histories, start=1):
        arrays[f"diag_route1_unitary__a{history_index}"] = unitaries[theta]

    maximum_completed_error = 0.0
    maximum_all_error = 0.0
    rows: list[dict[str, object]] = []
    for route_index, (plus, minus) in enumerate(
        ((HISTORIES[1], HISTORIES[2]), (HISTORIES[3], HISTORIES[4]))
    ):
        plus_kraus = kraus_from_direct(
            comparator_basis.conjugate().T
            @ unitaries[plus]
            @ comparator_basis,
            source_dimension=1,
            record_dimension=2,
            ready_index=0,
        )
        minus_kraus = kraus_from_direct(
            comparator_basis.conjugate().T
            @ unitaries[minus]
            @ comparator_basis,
            source_dimension=1,
            record_dimension=2,
            ready_index=0,
        )
        exhaustive_matrix, completed_matrix = aggregate_responses(
            minus_kraus,
            plus_kraus,
            pointer_index=0,
        )
        completed = completed_matrix[0, 0]
        exhaustive = exhaustive_matrix[0, 0]
        expected_completed = np.conjugate(
            (1.0 + np.exp(1j * minus)) / 2.0
        ) * ((1.0 + np.exp(1j * plus)) / 2.0)
        expected_exhaustive = (
            1.0 + np.exp(1j * (plus - minus))
        ) / 2.0
        completed_error = float(np.abs(completed - expected_completed))
        all_error = float(np.abs(exhaustive - expected_exhaustive))
        maximum_completed_error = max(maximum_completed_error, completed_error)
        maximum_all_error = max(maximum_all_error, all_error)
        arrays[
            f"diag_route1_current__r{route_index}__completed"
        ] = np.asarray([[completed]], dtype=complex)
        arrays[
            f"diag_route1_current__r{route_index}__all"
        ] = np.asarray([[exhaustive]], dtype=complex)
        rows.append(
            {
                "route_pair": route_index,
                "theta_plus": plus,
                "theta_minus": minus,
                "completed_component_error": completed_error,
                "exhaustive_kernel_error": all_error,
            }
        )
    require(
        maximum_completed_error <= 1.0e-10,
        "independent Route-2 architecture failed Route-1 completed component",
    )
    require(
        maximum_all_error <= 1.0e-10,
        "independent Route-2 architecture failed Route-1 exhaustive kernel",
    )
    return {
        "construction":
            "independent_production_kraus_and_aggregate_on_declared_O6_carrier",
        "rows": rows,
        "maximum_completed_component_error": maximum_completed_error,
        "maximum_exhaustive_kernel_error": maximum_all_error,
        "passed": True,
        "actual_parent_route1_line_restriction_derived": False,
    }


def build_precomparison_bundle() -> tuple[dict[str, np.ndarray], dict[str, object]]:
    runtime_attestation = require_runtime_attestation()
    require(not OUTPUT_JSON.exists(), f"immutable output already exists: {OUTPUT_JSON}")
    require(not OUTPUT_NPZ.exists(), f"immutable output already exists: {OUTPUT_NPZ}")
    for future in FUTURE_OUTPUTS:
        require(not future.exists(), f"future output exists before precomparison: {future}")
        require(
            not Path(f"{future}.seal.sha256").exists(),
            f"future output seal exists before precomparison: {future}",
        )
    authority_rows = verify_authorities()
    implementation_rows = verify_implementation_manifest()
    arrays: dict[str, np.ndarray] = {}
    overlap = prepropagation_overlap()
    arrays["basis_overlap_primary_from_independent"] = overlap
    arrays["primary_labels"] = np.asarray(primary_labels(), dtype=np.int64)
    arrays["independent_labels"] = np.asarray(independent_labels(), dtype=np.int64)
    arrays["independent_phases"] = np.asarray(
        [independent_phase(label) for label in independent_labels()],
        dtype=complex,
    )
    overlap_residual = float(
        np.linalg.norm(overlap.conjugate().T @ overlap - np.eye(SOURCE_DIMENSION), ord=2)
    )
    require(overlap_residual <= 2.0e-11, "basis-overlap unitarity gate failed")

    cases = []
    for ell in ELLS:
        for resolution in RK4_RESOLUTIONS:
            cases.append(execute_case(ell, resolution, arrays))
    tails = {f"ell_{ell:.16g}": tail_metrics(arrays, ell) for ell in ELLS}
    record_values, probabilities, pointer_weights = add_common_component_arrays(arrays)
    route1_current = current_route2_route1_architecture_reduction(arrays)
    manifest = common_component_manifest(
        arrays,
        record_values,
        probabilities,
        pointer_weights,
    )
    diagnostics = independent_comparison_diagnostics(
        arrays,
        cases,
        tails,
        record_values,
        probabilities,
    )

    metadata: dict[str, object] = {
        "schema": SCHEMA,
        "generator_pieces_schema": GENERATOR_PIECES_SCHEMA,
        "generator_midpoint_count": {
            f"ell{index}": RK4_RESOLUTIONS[-1] for index in range(len(ELLS))
        },
        "lane": "independent",
        "verdict": "INDEPENDENT_PRECOMPARISON_BUNDLE_SEALED",
        "spec_sha256": SPEC_SHA256,
        "executor_sha256": sha256_file(Path(__file__).resolve()),
        "implementation_manifest_sha256": sha256_file(IMPLEMENTATION_MANIFEST),
        "runtime_attestation": runtime_attestation,
        "authority_hashes": authority_rows,
        "implementation_hashes": implementation_rows,
        "semantic_read_allowlist": sorted(READ_ALLOWLIST),
        "semantic_read_ledger": list(SEMANTIC_READ_LEDGER),
        "future_primary_paths_read": False,
        "configuration": {
            "n": N,
            "ell": list(ELLS),
            "source_dimension": SOURCE_DIMENSION,
            "record_dimension": RECORD_DIMENSION,
            "histories": list(HISTORIES),
            "history_pairs": [list(pair) for pair in HISTORY_PAIRS],
            "quadrature": list(QUADRATURE),
            "rk4_resolutions": list(RK4_RESOLUTIONS),
            "basis_order": "spin_slowest_then_c_descending_b_ascending_a_descending",
            "basis_overlap": "prepropagation_Gauss-Hermite_from_sealed_metadata",
            "integrator": "classical_RK4_exact_tableau_from_sealed_spec",
        },
        "basis_overlap_unitarity_residual": overlap_residual,
        "manifest": manifest,
        "manifest_sha256": canonical_sha256(manifest),
        "comparison_diagnostics": diagnostics,
        "sealed": True,
        "immutable_bundle": True,
        "precomparison_committed": True,
        "primary_output_paths_readable_during_construction": False,
        "cases": cases,
        "independent_rk4_tails": tails,
        "route1_current_route2_architecture_reduction": route1_current,
        "state_evaluated": False,
        "actual_parent_regulated_CAR_operator_response_derived": False,
        "actual_parent_same_carrier_one_source_restriction_derived": False,
        "route1_special_case_reexecution_passed": False,
        "route1_current_route2_architecture_reduction_passed": True,
        "actual_parent_route1_line_restriction_derived": False,
        "actual_finite_parent_state_evaluation_derived": False,
        "actual_finite_parent_operator_to_scalar_bridge_derived": False,
        "interacting_continuum_CTP_amplitude_derived": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "ER_fork_closed": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    return arrays, metadata


def execute() -> None:
    arrays, metadata = build_precomparison_bundle()
    atomic_write_bundle(arrays, metadata)
    print(
        json.dumps(
            {
                "schema": SCHEMA,
                "verdict": metadata["verdict"],
                "json": str(OUTPUT_JSON),
                "npz": str(OUTPUT_NPZ),
                "array_count": len(arrays),
            },
            indent=2,
            sort_keys=True,
        )
    )


def main() -> None:
    # A launcher failure is not a precomparison result and must not consume
    # the immutable output path.
    require_runtime_attestation()
    try:
        execute()
    except Exception as error:
        write_blocked_result(error)
        raise


if __name__ == "__main__":
    main()
