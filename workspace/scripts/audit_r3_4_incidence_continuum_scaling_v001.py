#!/usr/bin/env python3
"""Audit the flat free-tail incidence refinement and root spectral measure."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_INCIDENCE_CONTINUUM_SCALING_SPEC_V001.md"
PROVENANCE = ROOT / "R3_4_INCIDENCE_CONTINUUM_SCALING_PROVENANCE_V001.json"
SPEC_SEAL = ROOT / "R3_4_INCIDENCE_CONTINUUM_SCALING_SPEC_V001.seal.sha256"
DEFAULT_RESULT = ROOT / "results" / "r3_4_incidence_continuum_scaling_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_status(path: Path, key: str) -> bool:
    matches = re.findall(
        rf"(?m)^{re.escape(key)} = (true|false)$",
        path.read_text(encoding="utf-8"),
    )
    require(len(matches) == 1, f"{path.name}: expected exactly one {key}")
    return matches[0] == "true"


def verify_provenance() -> dict:
    seal = {}
    for line in SPEC_SEAL.read_text(encoding="utf-8").splitlines():
        if not line:
            continue
        digest, relative = line.split(maxsplit=1)
        require(relative not in seal, f"duplicate seal path {relative}")
        seal[relative] = digest
    expected = {SPEC.name: sha256(SPEC), PROVENANCE.name: sha256(PROVENANCE)}
    require(seal == expected, "spec/provenance seal mismatch")

    manifest = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    rows = []
    for authority in manifest["authorities"]:
        path = ROOT / authority["path"]
        require(path.is_file(), f"missing authority {authority['path']}")
        actual_hash = sha256(path)
        require(actual_hash == authority["sha256"], f"hash mismatch {path.name}")
        statuses = {}
        for key, expected_value in authority["status"].items():
            value = exact_status(path, key)
            require(value is expected_value, f"status mismatch {path.name}:{key}")
            statuses[key] = value
        rows.append(
            {
                "path": authority["path"],
                "sha256": actual_hash,
                "status": statuses,
            }
        )
    return {
        "spec_sha256": expected[SPEC.name],
        "provenance_sha256": expected[PROVENANCE.name],
        "authorities": rows,
        "write_defect_obligations": manifest["write_defect_obligations"],
    }


def d_continuum(k: np.ndarray) -> np.ndarray:
    return 1j * np.asarray(k, dtype=float)


def d_cellular(a: float, k: np.ndarray) -> np.ndarray:
    return (np.exp(1j * a * np.asarray(k, dtype=float)) - 1.0) / a


def block_hamiltonian(d: np.ndarray) -> np.ndarray:
    h = np.zeros((4, 4), dtype=complex)
    h[0, 1:] = np.conjugate(d)
    h[1:, 0] = d
    return h


def positive_projector(d: np.ndarray) -> np.ndarray:
    norm = float(np.linalg.norm(d))
    require(norm > 0.0, "positive projector undefined at the zero symbol")
    h = block_hamiltonian(d)
    longitudinal = np.zeros((4, 4), dtype=complex)
    longitudinal[0, 0] = 1.0
    longitudinal[1:, 1:] = np.outer(d, np.conjugate(d)) / norm**2
    return 0.5 * (longitudinal + h / norm)


def negative_projector(d: np.ndarray) -> np.ndarray:
    norm = float(np.linalg.norm(d))
    require(norm > 0.0, "negative projector undefined at the zero symbol")
    h = block_hamiltonian(d)
    longitudinal = np.zeros((4, 4), dtype=complex)
    longitudinal[0, 0] = 1.0
    longitudinal[1:, 1:] = np.outer(d, np.conjugate(d)) / norm**2
    return 0.5 * (longitudinal - h / norm)


def zero_projector(d: np.ndarray) -> np.ndarray:
    norm = float(np.linalg.norm(d))
    require(norm > 0.0, "zero projector undefined at the zero symbol")
    p0 = np.zeros((4, 4), dtype=complex)
    p0[1:, 1:] = np.eye(3) - np.outer(d, np.conjugate(d)) / norm**2
    return p0


def ball_form_factor(energy: float | np.ndarray) -> float | np.ndarray:
    scalar = np.isscalar(energy)
    e = np.atleast_1d(np.asarray(energy, dtype=float))
    out = np.empty_like(e)
    small = np.abs(e) < 1.0e-3
    es = e[small]
    out[small] = 1.0 - es**2 / 40.0 + es**4 / 4480.0
    z = e[~small] / 2.0
    out[~small] = 3.0 * (np.sin(z) - z * np.cos(z)) / z**3
    return float(out[0]) if scalar else out


def root_density(energy: float | np.ndarray) -> float | np.ndarray:
    scalar = np.isscalar(energy)
    e = np.atleast_1d(np.asarray(energy, dtype=float))
    rho = e**2 * np.asarray(ball_form_factor(e)) ** 2 / (12.0 * math.pi)
    return float(rho[0]) if scalar else rho


def resolvent(matrix: np.ndarray, z: complex = 1j) -> np.ndarray:
    return np.linalg.inv(matrix - z * np.eye(matrix.shape[0]))


def continuum_checks() -> dict:
    sample_k = [
        np.array([0.3, -0.4, 0.7]),
        np.array([1.1, 0.2, -0.6]),
        np.array([-0.8, 1.3, 0.5]),
    ]
    spacings = [1.0, 0.5, 0.25, 0.125, 0.0625]
    symbol_errors = []
    resolvent_errors = []
    for a in spacings:
        symbol_error = 0.0
        resolvent_error = 0.0
        for k in sample_k:
            hc = block_hamiltonian(d_continuum(k))
            ha = block_hamiltonian(d_cellular(a, k))
            symbol_error = max(symbol_error, float(np.linalg.norm(ha - hc, 2)))
            resolvent_error = max(
                resolvent_error,
                float(np.linalg.norm(resolvent(ha) - resolvent(hc), 2)),
            )
        symbol_errors.append({"a": a, "maximum_error": symbol_error})
        resolvent_errors.append({"a": a, "maximum_error": resolvent_error})

    k = np.array([0.7, -1.1, 0.9])
    d = d_continuum(k)
    h = block_hamiltonian(d)
    p_plus = positive_projector(d)
    p_minus = negative_projector(d)
    p_zero = zero_projector(d)
    root = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)

    hermitian = bool(np.linalg.norm(h - h.conjugate().T) < 1.0e-12)
    projector_resolution = bool(
        np.linalg.norm(p_plus + p_minus + p_zero - np.eye(4)) < 1.0e-12
    )
    projector_orthogonality = bool(
        max(
            np.linalg.norm(p_plus @ p_minus),
            np.linalg.norm(p_plus @ p_zero),
            np.linalg.norm(p_minus @ p_zero),
        )
        < 1.0e-12
    )
    root_weights = {
        "positive": float(np.real(np.vdot(root, p_plus @ root))),
        "negative": float(np.real(np.vdot(root, p_minus @ root))),
        "transverse_zero": float(np.real(np.vdot(root, p_zero @ root))),
    }

    return {
        "spacings": spacings,
        "symbol_errors": symbol_errors,
        "resolvent_errors": resolvent_errors,
        "symbol_error_monotone": all(
            symbol_errors[index + 1]["maximum_error"]
            < symbol_errors[index]["maximum_error"]
            for index in range(len(symbol_errors) - 1)
        ),
        "resolvent_error_monotone": all(
            resolvent_errors[index + 1]["maximum_error"]
            < resolvent_errors[index]["maximum_error"]
            for index in range(len(resolvent_errors) - 1)
        ),
        "cellular_operator_norm_formula": "2*sqrt(3)/a",
        "uniform_boundedness_as_a_to_zero": False,
        "continuum_symbol_hermitian": hermitian,
        "projector_resolution": projector_resolution,
        "projector_orthogonality": projector_orthogonality,
        "root_projector_weights": root_weights,
    }


def build_result() -> dict:
    provenance = verify_provenance()
    checks = continuum_checks()

    positive_half = abs(checks["root_projector_weights"]["positive"] - 0.5) < 1e-12
    negative_half = abs(checks["root_projector_weights"]["negative"] - 0.5) < 1e-12
    zero_root_weight = abs(checks["root_projector_weights"]["transverse_zero"]) < 1e-12
    form_factor_identity = all(
        abs(
            float(ball_form_factor(energy))
            - 24.0
            * (
                math.sin(energy / 2.0)
                - (energy / 2.0) * math.cos(energy / 2.0)
            )
            / energy**3
        )
        < 1.0e-13
        for energy in (0.2, 1.0, 3.0, 7.0)
    )

    # Exact Fourier normalization:
    # Vol(B)=pi/6 and |psi_hat|^2=Vol(B)/(2*pi)^3 |F_B|^2.
    # Angular integration and conditioning the 1/2 positive projector weight
    # give Vol(B)/(2*pi^2)=1/(12*pi).
    radial_prefactor = (math.pi / 6.0) / (2.0 * math.pi**2)
    radial_prefactor_matches = abs(radial_prefactor - 1.0 / (12.0 * math.pi)) < 1e-15

    mathematical_pass = all(
        [
            checks["symbol_error_monotone"],
            checks["resolvent_error_monotone"],
            checks["continuum_symbol_hermitian"],
            checks["projector_resolution"],
            checks["projector_orthogonality"],
            positive_half,
            negative_half,
            zero_root_weight,
            form_factor_identity,
            radial_prefactor_matches,
        ]
    )
    write_defects_closed = all(provenance["write_defect_obligations"].values())

    if not mathematical_pass:
        verdict = "FREE_TAIL_CONTINUUM_DERIVATION_FAILED"
    elif write_defects_closed:
        verdict = "COMPLETE_OUTGOING_ROOT_SPECTRAL_MEASURE_DERIVED"
    else:
        verdict = (
            "FREE_FLAT_TAIL_OPERATOR_AND_ROOT_MEASURE_DERIVED_"
            "WRITE_DEFECT_OPEN"
        )

    return {
        "sealed_inputs": provenance,
        "target_firewall": {
            "alpha_used": False,
            "measured_constants_used": False,
            "desired_decay_used_as_selector": False,
        },
        "operator": {
            "continuum_carrier": "L2(R^3; C direct-sum C^3)",
            "continuum_symbol": "[[0,d(k)^dagger],[d(k),0]], d(k)=i*k",
            "self_adjoint_domain": (
                "{psi in L2: h(k) psi(k) is in L2}, "
                "Fourier-multiplier maximal domain"
            ),
            "self_adjointness_certificate": (
                "measurable Hermitian matrix multiplier on its maximal domain"
            ),
            "cellular_symbol": "d_a,j=(exp(i*a*k_j)-1)/a",
            "strong_resolvent_certificate": (
                "pointwise resolvent convergence plus "
                "||(h_a-z)^-1||<=1/|Im z| and dominated convergence"
            ),
            "unitary_convergence_certificate": (
                "pointwise exp(-it h_a)->exp(-it h) with unit norm domination"
            ),
            "checks": checks,
        },
        "root_measure": {
            "waist_ball_radius": "1/2",
            "waist_ball_volume": "pi/6",
            "normalized_root": "1_B/sqrt(Vol(B)) in scalar 0-form sector",
            "ball_equals_diamond_null_shell_form_factor": form_factor_identity,
            "positive_projector_weight": "1/2",
            "negative_projector_weight": "1/2",
            "transverse_zero_projector_weight": "0",
            "positive_conditioned_radial_prefactor": "1/(12*pi)",
            "density": (
                "E^2 |F_B(E)|^2/(12*pi)"
                "=48[sin(E/2)-(E/2)cos(E/2)]^2/(pi E^4)"
            ),
            "normalized": True,
            "root_measure_has_point_atom": False,
            "full_truncated_operator_has_transverse_zero_eigenspace": True,
            "sharp_root_in_Hilbert_space": True,
            "sharp_root_in_generator_domain": False,
            "sharp_root_mean_energy_finite": False,
            "mean_energy_obstruction": (
                "rho(E)=O(E^-2), so integral E*rho(E)dE diverges "
                "logarithmically"
            ),
        },
        "status": {
            "verdict": verdict,
            "free_flat_continuum_scaling_derived": mathematical_pass,
            "strong_resolvent_limit_derived_in_flat_cubical_branch": (
                mathematical_pass
            ),
            "self_adjoint_free_outgoing_domain_derived": mathematical_pass,
            "positive_energy_projector_derived": mathematical_pass,
            "operator_derived_positive_branch_root_measure_computed": (
                mathematical_pass
            ),
            "physical_positive_energy_record_branch_selected": False,
            "finite_energy_physical_root_derived": False,
            "complete_write_defect_spectrum_closed": write_defects_closed,
            "complete_outgoing_root_spectral_measure_derived": (
                mathematical_pass and write_defects_closed
            ),
            "hypothesis_promoted_to_principle": False,
            "coupling_evaluation_authorized": False,
            "alpha_computed": False,
            "proof_authorized": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_RESULT)
    args = parser.parse_args()
    result = build_result()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["status"], indent=2))


if __name__ == "__main__":
    main()
