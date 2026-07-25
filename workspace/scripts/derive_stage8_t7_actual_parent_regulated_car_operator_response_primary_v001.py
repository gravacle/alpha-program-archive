#!/usr/bin/env python3
"""Build the sealed primary Hermite-Galerkin CAR operator-response bundle."""

from __future__ import annotations

import hashlib
import json
import math
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
SPEC = ROOT / "STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md"
SPEC_SHA256 = "789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3"
BUNDLE_SCHEMA = "stage8_t7_actual_parent_regulated_car_operator_response_bundle_v001"
RUNTIME_MARKER = "_stage8_t7_content_addressed_runtime_v001"
RUNTIME_MANIFEST_SHA256 = (
    "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b"
)
IMPLEMENTATION_MANIFEST = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_regulated_car_operator_response_implementation_v001.json"
)
IMPLEMENTATION_SEAL = Path(f"{IMPLEMENTATION_MANIFEST}.seal.sha256")
OUT_JSON = (
    ROOT
    / "stage8_execution/work/"
    "T07_actual_parent_regulated_car_operator_response_primary_v001.json"
)
OUT_NPZ = (
    ROOT
    / "stage8_execution/work/"
    "T07_actual_parent_regulated_car_operator_response_primary_v001.npz"
)
INDEPENDENT_JSON = (
    ROOT
    / "stage8_execution/work/"
    "T07_actual_parent_regulated_car_operator_response_independent_precomparison_v001.json"
)
INDEPENDENT_NPZ = (
    ROOT
    / "stage8_execution/work/"
    "T07_actual_parent_regulated_car_operator_response_independent_precomparison_v001.npz"
)

AUTHORITIES = {
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
    "STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_AMENDMENT_V001.md":
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

N = 2
ELLS = (1.0, math.sqrt(2.0))
HISTORIES = (0.0, 0.07, -0.11, 0.13, 0.04)
PAIRS = ((0, 0), (1, 2), (3, 4))
RECORD_VALUES = (-math.sqrt(2.0), 0.0, math.sqrt(2.0))
RESOLUTIONS = (12, 24, 48)
PRIMARY_QUADRATURE = (10, 10, 20)
SECONDARY_QUADRATURE = (12, 12, 24)

STRUCTURAL_TOL = 2.0e-11
RECORD_TOL = 2.0e-12
INTERNAL_TOL = 3.0e-9
CONVERGENCE_RATIO_MIN = 3.2


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
        attestation.get("schema")
        == "stage8_t7_content_addressed_runtime_attestation_v001",
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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def atomic_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def atomic_write_bundle(
    arrays: dict[str, np.ndarray],
    payload: dict[str, object],
) -> dict[str, object]:
    npz_seal = Path(f"{OUT_NPZ}.seal.sha256")
    json_seal = Path(f"{OUT_JSON}.seal.sha256")
    require(not OUT_NPZ.exists(), f"Immutable output already exists: {OUT_NPZ}")
    require(not OUT_JSON.exists(), f"Immutable output already exists: {OUT_JSON}")
    require(not npz_seal.exists(), f"Immutable output seal already exists: {npz_seal}")
    require(not json_seal.exists(), f"Immutable output seal already exists: {json_seal}")
    OUT_NPZ.parent.mkdir(parents=True, exist_ok=True)
    npz_temporary = OUT_NPZ.with_name(f".{OUT_NPZ.name}.tmp")
    json_temporary = OUT_JSON.with_name(f".{OUT_JSON.name}.tmp")
    npz_seal_temporary = npz_seal.with_name(f".{npz_seal.name}.tmp")
    json_seal_temporary = json_seal.with_name(f".{json_seal.name}.tmp")
    require(not npz_temporary.exists(), f"Stale temporary output: {npz_temporary}")
    require(not json_temporary.exists(), f"Stale temporary output: {json_temporary}")
    require(
        not npz_seal_temporary.exists(),
        f"Stale temporary output: {npz_seal_temporary}",
    )
    require(
        not json_seal_temporary.exists(),
        f"Stale temporary output: {json_seal_temporary}",
    )
    committed: list[Path] = []
    try:
        with npz_temporary.open("xb") as handle:
            np.savez(handle, **arrays)
            handle.flush()
            os.fsync(handle.fileno())
        final_payload = dict(payload)
        final_payload["npz_sha256"] = sha256(npz_temporary)
        with json_temporary.open("x", encoding="utf-8") as handle:
            json.dump(
                final_payload,
                handle,
                indent=2,
                sort_keys=True,
                ensure_ascii=True,
                allow_nan=False,
            )
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        json_hash = sha256(json_temporary)
        with npz_seal_temporary.open("x", encoding="ascii") as handle:
            handle.write(f"{final_payload['npz_sha256']}  {OUT_NPZ.name}\n")
            handle.flush()
            os.fsync(handle.fileno())
        with json_seal_temporary.open("x", encoding="ascii") as handle:
            handle.write(f"{json_hash}  {OUT_JSON.name}\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(npz_temporary, OUT_NPZ)
        committed.append(OUT_NPZ)
        os.replace(json_temporary, OUT_JSON)
        committed.append(OUT_JSON)
        os.replace(npz_seal_temporary, npz_seal)
        committed.append(npz_seal)
        os.replace(json_seal_temporary, json_seal)
        committed.append(json_seal)
        for artifact in committed:
            artifact.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        return final_payload
    except Exception:
        npz_temporary.unlink(missing_ok=True)
        json_temporary.unlink(missing_ok=True)
        npz_seal_temporary.unlink(missing_ok=True)
        json_seal_temporary.unlink(missing_ok=True)
        for artifact in reversed(committed):
            artifact.unlink(missing_ok=True)
        raise


def write_blocked_result(error: Exception) -> None:
    if OUT_JSON.exists() or OUT_NPZ.exists():
        return
    payload = {
        "schema": BUNDLE_SCHEMA,
        "lane": "primary",
        "spec_sha256": SPEC_SHA256,
        "overall_verdict": "ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_BLOCKED",
        "reason": str(error),
        "exception_type": type(error).__name__,
        "sealed": True,
        "immutable_bundle": True,
        "actual_parent_regulated_CAR_operator_response_derived": False,
        "actual_parent_same_carrier_one_source_restriction_derived": False,
        "actual_finite_parent_state_evaluation_derived": False,
        "actual_finite_parent_operator_to_scalar_bridge_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    atomic_json(OUT_JSON, payload)
    seal = Path(f"{OUT_JSON}.seal.sha256")
    require(not seal.exists(), f"Blocked-result seal already exists: {seal}")
    seal.write_text(f"{sha256(OUT_JSON)}  {OUT_JSON.name}\n", encoding="ascii")
    for artifact in (OUT_JSON, seal):
        artifact.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)


def verify_sealed_artifact(path: Path) -> str:
    seal = Path(f"{path}.seal.sha256")
    require(path.is_file(), f"Required sealed artifact missing: {path}")
    require(seal.is_file(), f"Required artifact seal missing: {seal}")
    fields = seal.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, f"Malformed artifact seal: {seal}")
    require(fields[1] == path.name, f"Artifact-seal filename mismatch: {seal}")
    digest = sha256(path)
    require(fields[0] == digest, f"Artifact-seal hash mismatch: {path}")
    return digest


def verify_independent_precomparison_commitment() -> dict[str, str]:
    return {
        "json_path": str(INDEPENDENT_JSON.relative_to(ROOT)),
        "json_sha256": verify_sealed_artifact(INDEPENDENT_JSON),
        "npz_path": str(INDEPENDENT_NPZ.relative_to(ROOT)),
        "npz_sha256": verify_sealed_artifact(INDEPENDENT_NPZ),
    }


def verify_authorities() -> str:
    require(sha256(SPEC) == SPEC_SHA256, "Sealed specification drift")
    for relative, expected in AUTHORITIES.items():
        actual = sha256(ROOT / relative)
        require(actual == expected, f"Authority drift: {relative}")
    require(IMPLEMENTATION_MANIFEST.is_file(), "Implementation manifest missing")
    require(IMPLEMENTATION_SEAL.is_file(), "Implementation manifest seal missing")
    seal_fields = IMPLEMENTATION_SEAL.read_text(encoding="ascii").strip().split()
    require(len(seal_fields) == 2, "Malformed implementation seal")
    require(
        seal_fields[0] == sha256(IMPLEMENTATION_MANIFEST),
        "Implementation manifest seal mismatch",
    )
    manifest = json.loads(IMPLEMENTATION_MANIFEST.read_text(encoding="utf-8"))
    rows = manifest.get("files")
    require(isinstance(rows, list) and bool(rows), "Empty implementation manifest")
    row_map = {str(row["path"]): str(row["sha256"]) for row in rows}
    self_relative = str(SELF.relative_to(ROOT))
    require(
        row_map.get(self_relative) == sha256(SELF),
        "Primary executor is not the presealed implementation",
    )
    for relative, expected in row_map.items():
        require(
            sha256(ROOT / relative) == expected,
            f"Presealed implementation drift: {relative}",
        )
    return sha256(IMPLEMENTATION_MANIFEST)


def dirac_matrices() -> tuple[tuple[np.ndarray, ...], np.ndarray]:
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    eye_2 = np.eye(2, dtype=complex)
    zero_2 = np.zeros((2, 2), dtype=complex)
    gamma_0 = np.block([[eye_2, zero_2], [zero_2, -eye_2]])
    gamma_space = tuple(
        np.block([[zero_2, sigma], [-sigma, zero_2]])
        for sigma in (sigma_x, sigma_y, sigma_z)
    )
    gamma_5 = (
        1j
        * gamma_0
        @ gamma_space[0]
        @ gamma_space[1]
        @ gamma_space[2]
    )
    alphas = tuple(gamma_0 @ gamma for gamma in gamma_space)
    source_incidence = -1j * gamma_0 @ gamma_5
    return alphas, source_incidence


def momentum_1d(n: int, ell: float) -> np.ndarray:
    operator = np.zeros((n, n), dtype=complex)
    for column in range(n):
        if column + 1 < n:
            operator[column + 1, column] += (
                1j * math.sqrt(column + 1) / (math.sqrt(2.0) * ell)
            )
        if column > 0:
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


def multiplication_matrices(
    time: float,
    n: int,
    ell: float,
    quadrature: tuple[int, int, int],
) -> tuple[np.ndarray, np.ndarray]:
    radius = min(time, 1.0 - time)
    dimension = n**3
    if not 0.0 < time < 1.0 or radius <= 0.0:
        zero = np.zeros((dimension, dimension), dtype=complex)
        return zero, zero.copy()

    radial_count, polar_count, azimuth_count = quadrature
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
    radius_squared = x * x + y * y + z * z
    s_minus = time * time - radius_squared
    s_plus = (1.0 - time) ** 2 - radius_squared
    inside = (s_minus > 0.0) & (s_plus > 0.0)
    bump = np.zeros_like(radius_squared)
    bump[inside] = np.exp(
        16.0 - 1.0 / (s_minus[inside] * s_plus[inside])
    )

    weights = (wr * wm * rr**2 * azimuth_weight).ravel()
    basis = spatial_basis_values(x, y, z, n, ell)
    cell = basis.conjugate().T @ (weights[:, None] * basis)
    smooth = basis.conjugate().T @ ((weights * bump)[:, None] * basis)
    cell = 0.5 * (cell + cell.conjugate().T)
    smooth = 0.5 * (smooth + smooth.conjugate().T)
    return cell, smooth


def exp_hermitian(operator: np.ndarray, interval: float) -> np.ndarray:
    hermitian = 0.5 * (operator + operator.conjugate().T)
    values, vectors = np.linalg.eigh(hermitian)
    return (
        vectors
        @ np.diag(np.exp(-1j * interval * values))
        @ vectors.conjugate().T
    )


def record_data() -> tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
]:
    record = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    values, vectors = np.linalg.eigh(record)
    projectors = np.array(
        [
            np.outer(vectors[:, index], vectors[:, index].conjugate())
            for index in range(3)
        ]
    )
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    pointer = np.array([0.0, 1.0, 0.0], dtype=complex)
    coefficients = np.array(
        [projector @ ready for projector in projectors],
        dtype=complex,
    ).T
    probabilities = np.array(
        [np.vdot(ready, projector @ ready) for projector in projectors],
        dtype=complex,
    )
    pointer_weights = np.array(
        [np.vdot(pointer, projector @ ready) for projector in projectors],
        dtype=complex,
    )
    return record, values, projectors, probabilities, pointer_weights


def build_time_data(
    ell: float,
    steps: int,
    quadrature: tuple[int, int, int],
    alphas: tuple[np.ndarray, ...],
    source_incidence: np.ndarray,
) -> tuple[
    np.ndarray,
    tuple[np.ndarray, ...],
    tuple[np.ndarray, ...],
    tuple[float, ...],
]:
    dt = 1.0 / steps
    cells: list[np.ndarray] = []
    connections: list[np.ndarray] = []
    envelopes: list[float] = []
    for index in range(steps):
        time = (index + 0.5) * dt
        cell, smooth = multiplication_matrices(
            time, N, ell, quadrature
        )
        radius = min(time, 1.0 - time)
        envelope = (math.pi / math.sqrt(2.0)) * 32.0 * radius**3
        cells.append(np.kron(cell, source_incidence))
        connections.append(-np.kron(smooth, alphas[0]))
        envelopes.append(envelope)
    h0 = free_dirac(N, ell, alphas)
    return h0, tuple(cells), tuple(connections), tuple(envelopes)


def propagate_spectral(
    h0: np.ndarray,
    cells: tuple[np.ndarray, ...],
    connections: tuple[np.ndarray, ...],
    envelopes: tuple[float, ...],
    history: float,
    record_value: float,
) -> np.ndarray:
    steps = len(cells)
    dt = 1.0 / steps
    free_half = exp_hermitian(h0, 0.5 * dt)
    value = np.eye(h0.shape[0], dtype=complex)
    for cell, connection, envelope in zip(cells, connections, envelopes):
        external_half = exp_hermitian(history * connection, 0.5 * dt)
        record_step = exp_hermitian(
            record_value * envelope * cell,
            dt,
        )
        step = free_half @ external_half @ record_step @ external_half @ free_half
        value = step @ value
    return value


def ready_injection(source_dimension: int) -> np.ndarray:
    injection = np.zeros(
        (source_dimension * 3, source_dimension),
        dtype=complex,
    )
    for source in range(source_dimension):
        injection[3 * source, source] = 1.0
    return injection


def propagate_direct(
    h0: np.ndarray,
    cells: tuple[np.ndarray, ...],
    connections: tuple[np.ndarray, ...],
    envelopes: tuple[float, ...],
    record: np.ndarray,
    history: float,
) -> np.ndarray:
    steps = len(cells)
    dt = 1.0 / steps
    source_dimension = h0.shape[0]
    identity_record = np.eye(3, dtype=complex)
    free_half = np.kron(
        exp_hermitian(h0, 0.5 * dt),
        identity_record,
    )
    value = ready_injection(source_dimension)
    for cell, connection, envelope in zip(cells, connections, envelopes):
        external_half = np.kron(
            exp_hermitian(history * connection, 0.5 * dt),
            identity_record,
        )
        record_step = exp_hermitian(
            envelope * np.kron(cell, record),
            dt,
        )
        step = free_half @ external_half @ record_step @ external_half @ free_half
        value = step @ value
    return value


def kraus_blocks(
    stinespring: np.ndarray,
    record_dimension: int = 3,
) -> tuple[np.ndarray, ...]:
    source_dimension = stinespring.shape[1]
    require(
        stinespring.shape[0] == source_dimension * record_dimension,
        "Stinespring carrier dimensions are inconsistent",
    )
    tensor = stinespring.reshape(
        source_dimension,
        record_dimension,
        source_dimension,
    )
    return tuple(tensor[:, outcome, :] for outcome in range(record_dimension))


def gaussian_responses(
    unitaries_minus: tuple[np.ndarray, ...],
    unitaries_plus: tuple[np.ndarray, ...],
    probabilities: np.ndarray,
    pointer_weights: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, tuple[np.ndarray, ...]]:
    source_dimension = unitaries_plus[0].shape[0]
    cross = tuple(
        unitaries_minus[left].conjugate().T @ unitaries_plus[right]
        for left in range(3)
        for right in range(3)
    )
    all_response = np.zeros(
        (source_dimension, source_dimension),
        dtype=complex,
    )
    for index in range(3):
        all_response += probabilities[index] * cross[3 * index + index]
    pointer_response = np.zeros_like(all_response)
    for left in range(3):
        for right in range(3):
            pointer_response += (
                pointer_weights[left].conjugate()
                * pointer_weights[right]
                * cross[3 * left + right]
            )
    return all_response, pointer_response, cross


def direct_responses(
    blocks_minus: tuple[np.ndarray, ...],
    blocks_plus: tuple[np.ndarray, ...],
    selected_outcome: int = 1,
) -> tuple[np.ndarray, np.ndarray]:
    require(
        len(blocks_minus) == len(blocks_plus) > selected_outcome,
        "Kraus outcome inventory is inconsistent",
    )
    all_response = sum(
        (
            left.conjugate().T @ right
            for left, right in zip(blocks_minus, blocks_plus)
        ),
        np.zeros_like(blocks_plus[0]),
    )
    pointer_response = (
        blocks_minus[selected_outcome].conjugate().T
        @ blocks_plus[selected_outcome]
    )
    return all_response, pointer_response


def matrix_norm(value: np.ndarray) -> float:
    return float(np.linalg.norm(value, ord=2))


def tag_ell(index: int) -> str:
    return f"ell{index}"


def common_discrete_labels() -> dict[str, object]:
    return {
        "ell": [tag_ell(index) for index in range(len(ELLS))],
        "histories": [f"a{index}" for index in range(len(HISTORIES))],
        "history_pairs": [
            [f"a{plus}", f"a{minus}"] for plus, minus in PAIRS
        ],
        "pairs": [f"p{index}" for index in range(len(PAIRS))],
        "record_labels": [f"l{index}" for index in range(3)],
        "outcome_labels": [f"x{index}" for index in range(3)],
        "kernels": ["all", "pointer"],
    }


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
            for record_index in range(3)
        },
        "propagators": {},
        "cross_operators": {},
        "direct_kraus_members": {},
        "direct_responses": {},
        "aggregate_kernels": {},
    }
    for ell_index in range(len(ELLS)):
        ell_tag = tag_ell(ell_index)
        for history_index in range(len(HISTORIES)):
            for record_index in range(3):
                identifier = f"{ell_tag}.a{history_index}.l{record_index}"
                matrix_components["propagators"][identifier] = (
                    f"u__{ell_tag}__a{history_index}__l{record_index}"
                )
            for outcome in range(3):
                identifier = f"{ell_tag}.a{history_index}.x{outcome}"
                matrix_components["direct_kraus_members"][identifier] = (
                    f"direct_kraus__{ell_tag}__a{history_index}__x{outcome}"
                )
        for pair_index in range(len(PAIRS)):
            for left in range(3):
                for right in range(3):
                    identifier = (
                        f"{ell_tag}.p{pair_index}.mu{left}.l{right}"
                    )
                    matrix_components["cross_operators"][identifier] = (
                        f"cross__{ell_tag}__p{pair_index}__c{3 * left + right}"
                    )
            for kernel in ("all", "pointer"):
                identifier = f"{ell_tag}.p{pair_index}.{kernel}"
                matrix_components["direct_responses"][identifier] = (
                    f"direct_{kernel}__{ell_tag}__p{pair_index}"
                )
                matrix_components["aggregate_kernels"][identifier] = (
                    f"gaussian_{kernel}__{ell_tag}__p{pair_index}"
                )
    referenced = {
        npz_key
        for category in matrix_components.values()
        for npz_key in category.values()
    }
    require(referenced <= set(arrays), "Primary common component inventory is incomplete")
    return {
        "dimensions": {
            "source_dimension": 4 * N**3,
            "record_dimension": 3,
            "spatial_dimension": N**3,
        },
        "discrete_labels": common_discrete_labels(),
        "scalar_components": scalar_components,
        "matrix_components": matrix_components,
        "basis_overlap_key": None,
        "npz_keys": sorted(arrays),
    }


def primary_comparison_diagnostics(
    reports: dict[str, object],
    sensitivity: dict[str, object],
    record_values: np.ndarray,
    projectors: np.ndarray,
    probabilities: np.ndarray,
) -> dict[str, object]:
    internal_keys = (
        "maximum_gaussian_direct",
        "maximum_kraus_component",
        "maximum_kraus_compression",
        "maximum_hermiticity",
        "maximum_unitarity",
        "maximum_direct_isometry",
        "maximum_same_identity",
        "maximum_pointer_bound",
        "maximum_adjoint",
        "maximum_contraction",
    )
    local_gate_maxima = {
        key: max(
            float(reports[tag]["internal_residuals"][key])
            for tag in sorted(reports)
        )
        for key in internal_keys
    }
    local_gate_maxima.update(
        {
            "record_eigenvalue_error": float(
                np.max(np.abs(record_values - np.asarray(RECORD_VALUES)))
            ),
            "record_spectral_completeness": matrix_norm(
                np.sum(projectors, axis=0) - np.eye(3, dtype=complex)
            ),
            "record_projector_idempotence": max(
                matrix_norm(projector @ projector - projector)
                for projector in projectors
            ),
            "probability_sum": float(abs(np.sum(probabilities) - 1.0)),
        }
    )
    convergence: dict[str, dict[str, object]] = {}
    quadrature: dict[str, dict[str, float]] = {}
    connection: dict[str, dict[str, float]] = {}
    for tag in sorted(reports):
        report = reports[tag]
        convergence[tag] = {}
        quadrature[tag] = {}
        for pair_index in (1, 2):
            for kernel in ("all", "pointer"):
                source_key = f"pair{pair_index}_gaussian_{kernel}"
                logical_key = f"p{pair_index}.{kernel}"
                convergence[tag][logical_key] = report["convergence"][source_key]
                quadrature[tag][logical_key] = float(
                    report["quadrature_differences"][source_key]
                )
        connection[tag] = {
            "signal_norm": float(sensitivity[tag]["signal_norm"]),
            "maximum_connection_norm": float(
                sensitivity[tag]["maximum_connection_norm"]
            ),
        }
    return {
        "local_gate_maxima": local_gate_maxima,
        "primary_convergence": convergence,
        "primary_quadrature_differences": quadrature,
        "connection": connection,
    }


def execute_resolution(
    ell: float,
    steps: int,
    quadrature: tuple[int, int, int],
    alphas: tuple[np.ndarray, ...],
    source_incidence: np.ndarray,
    record: np.ndarray,
    probabilities: np.ndarray,
    pointer_weights: np.ndarray,
) -> dict[str, object]:
    h0, cells, connections, envelopes = build_time_data(
        ell,
        steps,
        quadrature,
        alphas,
        source_incidence,
    )
    unitaries: dict[int, tuple[np.ndarray, ...]] = {}
    stinespring: dict[int, np.ndarray] = {}
    blocks: dict[int, tuple[np.ndarray, ...]] = {}
    for history_index, history in enumerate(HISTORIES):
        unitaries[history_index] = tuple(
            propagate_spectral(
                h0,
                cells,
                connections,
                envelopes,
                history,
                record_value,
            )
            for record_value in RECORD_VALUES
        )
        stinespring[history_index] = propagate_direct(
            h0,
            cells,
            connections,
            envelopes,
            record,
            history,
        )
        blocks[history_index] = kraus_blocks(stinespring[history_index])

    pair_data: dict[int, dict[str, object]] = {}
    maximum_gaussian_direct = 0.0
    maximum_kraus_compression = 0.0
    for pair_index, (plus_index, minus_index) in enumerate(PAIRS):
        gaussian_all, gaussian_pointer, cross = gaussian_responses(
            unitaries[minus_index],
            unitaries[plus_index],
            probabilities,
            pointer_weights,
        )
        direct_all, direct_pointer = direct_responses(
            blocks[minus_index],
            blocks[plus_index],
        )
        compression = (
            stinespring[minus_index].conjugate().T
            @ stinespring[plus_index]
        )
        maximum_gaussian_direct = max(
            maximum_gaussian_direct,
            matrix_norm(gaussian_all - direct_all),
            matrix_norm(gaussian_pointer - direct_pointer),
        )
        maximum_kraus_compression = max(
            maximum_kraus_compression,
            matrix_norm(direct_all - compression),
        )
        pair_data[pair_index] = {
            "gaussian_all": gaussian_all,
            "gaussian_pointer": gaussian_pointer,
            "direct_all": direct_all,
            "direct_pointer": direct_pointer,
            "compression": compression,
            "cross": cross,
        }

    maximum_kraus_component = 0.0
    projectors = record_data()[2]
    for history_index in range(len(HISTORIES)):
        gaussian_blocks = tuple(
            sum(
                (
                    projector[outcome, 0]
                    * unitaries[history_index][record_index]
                    for record_index, projector in enumerate(
                        projectors
                    )
                ),
                np.zeros_like(unitaries[history_index][0]),
            )
            for outcome in range(3)
        )
        maximum_kraus_component = max(
            maximum_kraus_component,
            max(
                matrix_norm(left - right)
                for left, right in zip(
                    gaussian_blocks,
                    blocks[history_index],
                )
            ),
        )

    maximum_hermiticity = max(
        matrix_norm(h0 - h0.conjugate().T),
        max(matrix_norm(cell - cell.conjugate().T) for cell in cells),
        max(
            matrix_norm(connection - connection.conjugate().T)
            for connection in connections
        ),
    )
    maximum_unitarity = max(
        matrix_norm(unitary.conjugate().T @ unitary - np.eye(unitary.shape[0]))
        for history_unitaries in unitaries.values()
        for unitary in history_unitaries
    )
    maximum_direct_isometry = max(
        matrix_norm(
            value.conjugate().T @ value
            - np.eye(value.shape[1], dtype=complex)
        )
        for value in stinespring.values()
    )
    maximum_same_identity = 0.0
    maximum_pointer_bound = 0.0
    for history_index in range(len(HISTORIES)):
        same_all, same_pointer, _ = gaussian_responses(
            unitaries[history_index],
            unitaries[history_index],
            probabilities,
            pointer_weights,
        )
        identity = np.eye(same_all.shape[0], dtype=complex)
        maximum_same_identity = max(
            maximum_same_identity,
            matrix_norm(same_all - identity),
        )
        eigenvalues = np.linalg.eigvalsh(
            0.5 * (same_pointer + same_pointer.conjugate().T)
        )
        maximum_pointer_bound = max(
            maximum_pointer_bound,
            max(0.0, -float(eigenvalues[0])),
            max(0.0, float(eigenvalues[-1]) - 1.0),
        )

    maximum_adjoint = 0.0
    maximum_contraction = 0.0
    for plus_index, minus_index in PAIRS[1:]:
        forward_all, forward_pointer, _ = gaussian_responses(
            unitaries[minus_index],
            unitaries[plus_index],
            probabilities,
            pointer_weights,
        )
        reverse_all, reverse_pointer, _ = gaussian_responses(
            unitaries[plus_index],
            unitaries[minus_index],
            probabilities,
            pointer_weights,
        )
        maximum_adjoint = max(
            maximum_adjoint,
            matrix_norm(forward_all.conjugate().T - reverse_all),
            matrix_norm(forward_pointer.conjugate().T - reverse_pointer),
        )
        maximum_contraction = max(
            maximum_contraction,
            max(0.0, matrix_norm(forward_all) - 1.0),
            max(0.0, matrix_norm(forward_pointer) - 1.0),
        )

    return {
        "h0": h0,
        "cells": cells,
        "connections": connections,
        "unitaries": unitaries,
        "stinespring": stinespring,
        "blocks": blocks,
        "pairs": pair_data,
        "maximum_gaussian_direct": maximum_gaussian_direct,
        "maximum_kraus_component": maximum_kraus_component,
        "maximum_kraus_compression": maximum_kraus_compression,
        "maximum_hermiticity": maximum_hermiticity,
        "maximum_unitarity": maximum_unitarity,
        "maximum_direct_isometry": maximum_direct_isometry,
        "maximum_same_identity": maximum_same_identity,
        "maximum_pointer_bound": maximum_pointer_bound,
        "maximum_adjoint": maximum_adjoint,
        "maximum_contraction": maximum_contraction,
        "maximum_connection_norm": max(
            matrix_norm(connection) for connection in connections
        ),
    }


def copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def current_route2_route1_architecture_reduction(
    arrays: dict[str, np.ndarray],
) -> dict[str, object]:
    """Reduce the current Stinespring/PVM response architecture to O6."""

    ready = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0)
    completed_vector = ready.copy()
    other_vector = np.array([1.0, -1.0], dtype=complex) / math.sqrt(2.0)
    projectors = (
        np.outer(completed_vector, completed_vector.conjugate()),
        np.outer(other_vector, other_vector.conjugate()),
    )
    comparator_basis = np.column_stack((completed_vector, other_vector))
    ready_basis_vector = np.array([1.0, 0.0], dtype=complex)
    route1_histories = HISTORIES[1:]
    unitaries = {
        theta: np.diag([1.0, np.exp(1j * theta)]).astype(complex)
        for theta in route1_histories
    }
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
        stinespring_plus = (
            comparator_basis.conjugate().T
            @ unitaries[plus]
            @ comparator_basis
            @ ready_basis_vector[:, None]
        )
        stinespring_minus = (
            comparator_basis.conjugate().T
            @ unitaries[minus]
            @ comparator_basis
            @ ready_basis_vector[:, None]
        )
        blocks_plus = kraus_blocks(stinespring_plus, record_dimension=2)
        blocks_minus = kraus_blocks(stinespring_minus, record_dimension=2)
        exhaustive_matrix, completed_matrix = direct_responses(
            blocks_minus,
            blocks_plus,
            selected_outcome=0,
        )
        completed = completed_matrix[0, 0]
        exhaustive = exhaustive_matrix[0, 0]
        expected_completed = (
            ((1.0 + np.exp(1j * minus)) / 2.0).conjugate()
            * ((1.0 + np.exp(1j * plus)) / 2.0)
        )
        expected_exhaustive = (
            1.0 + np.exp(1j * (plus - minus))
        ) / 2.0
        completed_error = float(abs(completed - expected_completed))
        all_error = float(abs(exhaustive - expected_exhaustive))
        maximum_completed_error = max(maximum_completed_error, completed_error)
        maximum_all_error = max(maximum_all_error, all_error)
        arrays[
            f"diag_route1_current__r{route_index}__completed"
        ] = np.array([[completed]], dtype=complex)
        arrays[
            f"diag_route1_current__r{route_index}__all"
        ] = np.array([[exhaustive]], dtype=complex)
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
        "current Route-2 architecture failed the Route-1 completed component",
    )
    require(
        maximum_all_error <= 1.0e-10,
        "current Route-2 architecture failed the Route-1 exhaustive kernel",
    )
    return {
        "construction":
            "production_kraus_blocks_and_direct_responses_on_declared_O6_carrier",
        "rows": rows,
        "maximum_completed_component_error": maximum_completed_error,
        "maximum_exhaustive_kernel_error": maximum_all_error,
        "passed": True,
        "actual_parent_route1_line_restriction_derived": False,
    }


def isolated_route1_rerun() -> dict[str, object]:
    canonical_result = (
        ROOT / "stage8_execution/work/T07_primitive_operator_response_v001.json"
    )
    canonical_hash_before = sha256(canonical_result)
    expected_canonical = (
        "6dbda44a0f21a28b57f114654a6df79fc091ccfd601c38518fd5cf5f21697dcc"
    )
    require(
        canonical_hash_before == expected_canonical,
        "Canonical Route-1 result drift before isolated rerun",
    )

    executor_relative = Path(
        "scripts/derive_stage8_t7_primitive_operator_response_v001.py"
    )
    snapshot = (
        ROOT
        / "stage8_execution/isolated_route1_rerun/"
        / AUTHORITIES[str(executor_relative)][:16]
    )
    require(
        not snapshot.exists(),
        f"Immutable isolated Route-1 snapshot already exists: {snapshot}",
    )

    fixed_files = [
        executor_relative,
        Path(f"{executor_relative}.seal.sha256"),
        Path("STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md"),
        Path("STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md.seal.sha256"),
        Path("STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_EXACT_DERIVATION_V001.md"),
        Path("STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_EXACT_DERIVATION_V001.md.seal.sha256"),
        Path("STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_AUTHORITY_AMENDMENT_V001.md"),
        Path("STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_AUTHORITY_AMENDMENT_V001.md.seal.sha256"),
        Path("provenance/stage8_t7_numpy_runtime_manifest_v001.json"),
        Path("provenance/stage8_t7_numpy_runtime_manifest_v001.json.seal.sha256"),
        Path("scripts/build_stage8_t7_numpy_runtime_manifest_v001.py"),
    ]
    direct_files = [
        Path(relative)
        for relative in (
            "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md",
            "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md",
            "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md",
            "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md",
            "COMPLETE_ONE_CELL_CTP_KERNEL_GATE_V001.md",
            "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md",
            "STAGE8_T7_FOUR_AXIS_SCOPE_EXTENSION_ADJUDICATION_RESULT_V001.md",
        )
    ]
    bundle_files = [
        Path(
            "stage8_execution/t7_actual_parent_record_amplitude/"
            "T07_ACTUAL_PARENT_RECORD_AMPLITUDE_V001.seal.sha256"
        ),
        Path("STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_RESULT_V001.seal.sha256"),
    ]

    all_files = list(fixed_files) + direct_files + bundle_files
    for bundle_relative in bundle_files:
        for line in (ROOT / bundle_relative).read_text(encoding="ascii").splitlines():
            if line.strip():
                _, child = line.split(maxsplit=1)
                all_files.append(Path(child))

    manifest_rows = []
    seen: set[str] = set()
    for relative in all_files:
        key = str(relative)
        if key in seen:
            continue
        seen.add(key)
        source = ROOT / relative
        require(source.is_file(), f"Missing Route-1 snapshot input: {relative}")
        copy_file(source, snapshot / relative)
        manifest_rows.append(
            {"path": key, "sha256": sha256(source)}
        )

    manifest_path = snapshot / "SNAPSHOT_INPUT_MANIFEST.json"
    atomic_json(
        manifest_path,
        {
            "schema": "stage8_route1_isolated_snapshot_v001",
            "files": manifest_rows,
        },
    )
    command = [
        sys.executable,
        "-I",
        "-S",
        str(snapshot / executor_relative),
    ]
    completed = subprocess.run(
        command,
        cwd=snapshot,
        check=False,
        capture_output=True,
        text=True,
    )
    require(
        completed.returncode == 0,
        "Isolated Route-1 rerun failed: " + completed.stderr[-2000:],
    )
    snapshot_result = (
        snapshot / "stage8_execution/work/T07_primitive_operator_response_v001.json"
    )
    require(snapshot_result.is_file(), "Isolated Route-1 result missing")
    rerun = json.loads(snapshot_result.read_text(encoding="utf-8"))
    require(
        rerun.get("overall_verdict")
        == "FINITE_PRIMITIVE_OPERATOR_RESPONSE_BUNDLE_DERIVED",
        "Isolated Route-1 verdict changed",
    )
    route1 = rerun.get("route1_special_case_consistency_falsifier", {})
    require(
        route1.get("maximum_completed_component_error", 1.0) <= 1.0e-10,
        "Isolated Route-1 completed component failed",
    )
    require(
        route1.get("maximum_all_kernel_error", 1.0) <= 1.0e-10,
        "Isolated Route-1 exhaustive kernel failed",
    )
    canonical_hash_after = sha256(canonical_result)
    require(
        canonical_hash_after == expected_canonical,
        "Canonical Route-1 result changed during isolated rerun",
    )
    return {
        "snapshot_manifest_sha256": sha256(manifest_path),
        "snapshot_result_sha256": sha256(snapshot_result),
        "canonical_hash_before": canonical_hash_before,
        "canonical_hash_after": canonical_hash_after,
        "maximum_completed_component_error":
            route1["maximum_completed_component_error"],
        "maximum_exhaustive_kernel_error":
            route1["maximum_all_kernel_error"],
        "passed": True,
    }


def execute() -> dict[str, object]:
    runtime_attestation = require_runtime_attestation()
    require(not OUT_JSON.exists(), f"Immutable output already exists: {OUT_JSON}")
    require(not OUT_NPZ.exists(), f"Immutable output already exists: {OUT_NPZ}")
    implementation_manifest_sha256 = verify_authorities()
    independent_commitment = verify_independent_precomparison_commitment()
    alphas, source_incidence = dirac_matrices()
    record, record_values, projectors, probabilities, pointer_weights = (
        record_data()
    )
    require(
        np.max(np.abs(record_values - np.array(RECORD_VALUES))) <= RECORD_TOL,
        "Record eigenvalues changed",
    )
    require(
        matrix_norm(np.sum(projectors, axis=0) - np.eye(3)) <= RECORD_TOL,
        "Record projectors are incomplete",
    )
    require(
        max(matrix_norm(projector @ projector - projector) for projector in projectors)
        <= RECORD_TOL,
        "Record projector idempotence failed",
    )
    require(
        abs(np.sum(probabilities) - 1.0) <= RECORD_TOL,
        "Ready probabilities do not sum to one",
    )
    require(
        np.max(
            np.abs(
                pointer_weights
                - np.array([-0.25, 0.5, -0.25], dtype=complex)
            )
        )
        <= RECORD_TOL,
        "Derived pointer weights changed",
    )

    arrays: dict[str, np.ndarray] = {
        "record_eigenvalues": record_values,
        "record_projectors": projectors,
        "record_probabilities": probabilities,
        "record_pointer_weights": pointer_weights,
        "history_values": np.array(HISTORIES),
        "history_pairs": np.array(PAIRS, dtype=np.int64),
    }
    for record_index, projector in enumerate(projectors):
        arrays[f"record_projector__l{record_index}"] = projector
    reports: dict[str, object] = {}
    all_internal_residuals: list[float] = []
    all_ratios: list[float] = []
    sensitivity: dict[str, object] = {}

    for ell_index, ell in enumerate(ELLS):
        tag = tag_ell(ell_index)
        by_resolution = {
            steps: execute_resolution(
                ell,
                steps,
                PRIMARY_QUADRATURE,
                alphas,
                source_incidence,
                record,
                probabilities,
                pointer_weights,
            )
            for steps in RESOLUTIONS
        }
        secondary = execute_resolution(
            ell,
            48,
            SECONDARY_QUADRATURE,
            alphas,
            source_incidence,
            record,
            probabilities,
            pointer_weights,
        )

        convergence: dict[str, object] = {}
        for pair_index in (1, 2):
            for kernel in ("gaussian_all", "gaussian_pointer"):
                at_12 = by_resolution[12]["pairs"][pair_index][kernel]
                at_24 = by_resolution[24]["pairs"][pair_index][kernel]
                at_48 = by_resolution[48]["pairs"][pair_index][kernel]
                d_12_24 = matrix_norm(at_24 - at_12)
                d_24_48 = matrix_norm(at_48 - at_24)
                require(d_24_48 > 1.0e-15, "Unresolved primary convergence tail")
                ratio = d_12_24 / d_24_48
                require(
                    ratio >= CONVERGENCE_RATIO_MIN,
                    f"Primary convergence ratio failed: {tag} pair {pair_index} {kernel}",
                )
                convergence[f"pair{pair_index}_{kernel}"] = {
                    "d_12_24": d_12_24,
                    "d_24_48": d_24_48,
                    "ratio": ratio,
                }
                all_ratios.append(ratio)

        production = by_resolution[48]
        quadrature_differences: dict[str, float] = {}
        for pair_index in (1, 2):
            for kernel in ("gaussian_all", "gaussian_pointer"):
                difference = matrix_norm(
                    production["pairs"][pair_index][kernel]
                    - secondary["pairs"][pair_index][kernel]
                )
                quadrature_differences[f"pair{pair_index}_{kernel}"] = difference

        internal_residuals = {
            key: max(
                float(by_resolution[steps][key])
                for steps in RESOLUTIONS
            )
            for key in (
                "maximum_gaussian_direct",
                "maximum_kraus_component",
                "maximum_kraus_compression",
                "maximum_hermiticity",
                "maximum_unitarity",
                "maximum_direct_isometry",
                "maximum_same_identity",
                "maximum_pointer_bound",
                "maximum_adjoint",
                "maximum_contraction",
            )
        }
        require(
            internal_residuals["maximum_hermiticity"] <= STRUCTURAL_TOL,
            f"Hermiticity failed for {tag}",
        )
        for key in (
            "maximum_gaussian_direct",
            "maximum_kraus_component",
            "maximum_kraus_compression",
            "maximum_same_identity",
            "maximum_pointer_bound",
            "maximum_adjoint",
            "maximum_contraction",
        ):
            require(
                internal_residuals[key] <= INTERNAL_TOL,
                f"Internal operator identity failed: {tag} {key}",
            )
            all_internal_residuals.append(internal_residuals[key])

        source_dimension = production["h0"].shape[0]
        labels = np.array(
            [
                (a, b, c, spin)
                for a in range(N)
                for b in range(N)
                for c in range(N)
                for spin in range(4)
            ],
            dtype=np.int64,
        )
        require(labels.shape == (source_dimension, 4), "Basis labels changed")
        arrays[f"basis_labels__{tag}"] = labels
        arrays[f"h0__{tag}"] = production["h0"]
        midpoint = len(production["connections"]) // 2
        arrays[f"connection_midpoint__{tag}"] = production["connections"][midpoint]
        arrays[f"diag_h0__{tag}"] = production["h0"]
        arrays[f"diag_connection_midpoint__{tag}"] = production["connections"][
            midpoint
        ]

        for history_index in range(len(HISTORIES)):
            for record_index in range(3):
                arrays[
                    f"u__{tag}__a{history_index}__l{record_index}"
                ] = production["unitaries"][history_index][record_index]
            for outcome in range(3):
                arrays[
                    f"direct_kraus__{tag}__a{history_index}__x{outcome}"
                ] = production["blocks"][history_index][outcome]

        for pair_index in range(len(PAIRS)):
            pair = production["pairs"][pair_index]
            for cross_index, matrix in enumerate(pair["cross"]):
                arrays[f"cross__{tag}__p{pair_index}__c{cross_index}"] = matrix
            for name in (
                "gaussian_all",
                "gaussian_pointer",
                "direct_all",
                "direct_pointer",
                "compression",
            ):
                arrays[f"{name}__{tag}__p{pair_index}"] = pair[name]
        for pair_index in (1, 2):
            for kernel in ("all", "pointer"):
                for steps in RESOLUTIONS:
                    arrays[
                        f"diag_primary__{tag}__n{steps}"
                        f"__p{pair_index}__{kernel}"
                    ] = by_resolution[steps]["pairs"][pair_index][
                        f"gaussian_{kernel}"
                    ]
                arrays[
                    f"diag_primary_secondary_quadrature__{tag}__n48"
                    f"__p{pair_index}__{kernel}"
                ] = secondary["pairs"][pair_index][f"gaussian_{kernel}"]

        signal = matrix_norm(
            production["pairs"][1]["gaussian_all"]
            - np.eye(source_dimension, dtype=complex)
        )
        partial_error = max(
            convergence["pair1_gaussian_all"]["d_24_48"],
            quadrature_differences["pair1_gaussian_all"],
        )
        sensitivity[tag] = {
            "signal_norm": signal,
            "primary_partial_error": partial_error,
            "signal_to_primary_partial_error": (
                signal / partial_error if partial_error > 0.0 else None
            ),
            "maximum_connection_norm":
                production["maximum_connection_norm"],
            "awaiting_independent_error_terms": True,
        }
        require(
            production["maximum_connection_norm"] > 1.0e-6,
            f"Connection insertion vanished for {tag}",
        )

        reports[tag] = {
            "ell": ell,
            "source_dimension": source_dimension,
            "convergence": convergence,
            "quadrature_differences": quadrature_differences,
            "internal_residuals": internal_residuals,
        }

    route1_current = current_route2_route1_architecture_reduction(arrays)
    route1 = isolated_route1_rerun()
    manifest = common_component_manifest(
        arrays,
        record_values,
        probabilities,
        pointer_weights,
    )
    diagnostics = primary_comparison_diagnostics(
        reports,
        sensitivity,
        record_values,
        projectors,
        probabilities,
    )
    result = {
        "schema": BUNDLE_SCHEMA,
        "lane": "primary",
        "spec_sha256": SPEC_SHA256,
        "executor_sha256": sha256(SELF),
        "implementation_manifest_sha256": implementation_manifest_sha256,
        "runtime_attestation": runtime_attestation,
        "authorities_verified": len(AUTHORITIES),
        "npz_path": str(OUT_NPZ.relative_to(ROOT)),
        "manifest": manifest,
        "manifest_sha256": canonical_sha256(manifest),
        "comparison_diagnostics": diagnostics,
        "sealed": True,
        "immutable_bundle": True,
        "precomparison_committed": False,
        "primary_output_paths_readable_during_construction": None,
        "array_count": len(arrays),
        "reports": reports,
        "connection_sensitivity_partial": sensitivity,
        "route1_isolated_reexecution": route1,
        "route1_current_route2_architecture_reduction": route1_current,
        "maximum_internal_operator_residual": max(all_internal_residuals),
        "minimum_primary_convergence_ratio": min(all_ratios),
        "primary_operator_bundle_derived": True,
        "independent_precomparison_consumed": False,
        "independent_precomparison_commitment_verified": True,
        "independent_precomparison_commitment": independent_commitment,
        "actual_parent_regulated_CAR_operator_response_derived": False,
        "actual_parent_same_carrier_one_source_restriction_derived": False,
        "route1_special_case_consistency_falsifier_frozen": True,
        "route1_special_case_consistency_falsifier_passed": True,
        "route1_special_case_reexecution_passed": True,
        "route1_current_route2_architecture_reduction_passed": True,
        "actual_parent_route1_line_restriction_derived": False,
        "actual_finite_parent_state_evaluation_derived": False,
        "actual_finite_parent_operator_to_scalar_bridge_derived": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "ER_fork_closed": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
        "overall_verdict": "PRIMARY_OPERATOR_BUNDLE_DERIVED_AWAITING_COMPARISON",
    }
    final_result = atomic_write_bundle(arrays, result)
    print(json.dumps(final_result, indent=2, sort_keys=True))
    return final_result


def main() -> None:
    # A launcher failure is not a physics-lane result and must not create an
    # immutable BLOCKED artifact.
    require_runtime_attestation()
    try:
        execute()
    except Exception as error:
        write_blocked_result(error)
        raise


if __name__ == "__main__":
    main()
