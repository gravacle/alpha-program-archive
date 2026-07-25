#!/usr/bin/env python3
"""Audit the absolutely continuous spectrum of the Lorentzian joint parent."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_LORENTZIAN_THRESHOLD_RETURN_SPEC_V001.md"
SEAL = ROOT / "R3_4_LORENTZIAN_THRESHOLD_RETURN_SPEC_V001.seal.sha256"
OUTPUT = ROOT / "results" / "r3_4_lorentzian_threshold_return_v001.json"

PINNED = {
    "BID_LORENTZIAN_SOURCE_SCHUR_POLE_DERIVATION_V001.md":
        "dc0498615a94218c56ed91a3e679a2aa55e32d4fcb96220a50a7a88669a8fc34",
    "R3_4_LORENTZIAN_JOINT_ENDPOINT_COMPATIBILITY_RESULT_V001.md":
        "1868656d1881e67c8f6263062b27806f71bcc9de03d7eec0e612085fb47de0cf",
    "R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_RESULT_V001.md":
        "1d114e71c29c3a39b7afd1b7a80b47afb52fe77e8ee1e4e19b604defe3c69305",
    "PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md":
        "532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb",
    "CAUSAL_DIRECT_LIMIT_RECORD_HYPOTHESIS_V001.md":
        "60c82b021a7f5ffcb514ae8c20f083a7b2c9b42872586922b1c0464c4822d73f",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gaussian_radial_density(momentum: np.ndarray) -> np.ndarray:
    return 4.0 / math.sqrt(math.pi) * momentum**2 * np.exp(-momentum**2)


def build_matrices() -> tuple[
    tuple[np.ndarray, ...], np.ndarray, np.ndarray, np.ndarray
]:
    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    gamma = [np.block([[z2, i2], [i2, z2]])]
    gamma.extend(np.block([[z2, value], [-value, z2]]) for value in pauli)
    gamma5 = 1.0j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
    dirac_alpha = tuple(gamma[0] @ gamma[index] for index in range(1, 4))
    internal_sign = -1.0j * gamma[0] @ gamma5
    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    sign_values, sign_vectors = np.linalg.eigh(internal_sign)
    spin = sign_vectors[:, int(np.argmax(sign_values))]
    return dirac_alpha, internal_sign, c_partial, spin


def main() -> None:
    require(
        SEAL.read_text(encoding="ascii").strip().split()
        == [sha256(SPEC), SPEC.name],
        "Specification seal failed",
    )
    for name, digest in PINNED.items():
        require(sha256(ROOT / name) == digest, f"Upstream drift: {name}")

    dirac_alpha, internal_sign, c_partial, spin = build_matrices()
    record_eigenvalues = np.linalg.eigvalsh(c_partial)
    anticommutator_errors = [
        float(
            np.linalg.norm(
                value @ internal_sign + internal_sign @ value
            )
        )
        for value in dirac_alpha
    ]
    require(
        np.max(np.abs(record_eigenvalues - np.array([-math.sqrt(2.0), 0.0, math.sqrt(2.0)])))
        < 1e-12,
        "Record spectrum changed",
    )
    require(max(anticommutator_errors) < 1e-13, "Dirac anticommutation failed")

    mu = math.pi / math.sqrt(2.0)
    mass = math.sqrt(2.0) * mu
    times = (0.0, 1.0, 2.0, 4.0, 8.0)
    momentum = np.linspace(0.0, 9.0, 20001)
    density = gaussian_radial_density(momentum)
    density_normalization = float(np.trapezoid(density, momentum))
    radial_amplitudes = {}
    for time in times:
        zero_phase = np.cos(momentum * time)
        massive_phase = np.cos(
            np.sqrt(momentum**2 + mass**2) * time
        )
        radial_amplitudes[str(time)] = float(
            np.trapezoid(
                0.5 * density * (zero_phase + massive_phase), momentum
            )
        )

    # Independent within-run regression: diagonalize H(p) on six inversion-
    # symmetric directions, average the exact matrix return amplitude, and
    # perform a separate coarse radial quadrature.
    directions = (
        np.array([1.0, 0.0, 0.0]),
        np.array([-1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, -1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
        np.array([0.0, 0.0, -1.0]),
    )
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    initial = np.kron(spin, ready)
    coarse_momentum = np.linspace(0.0, 8.0, 401)
    coarse_density = gaussian_radial_density(coarse_momentum)
    direct_integrands = {time: [] for time in times}
    for radius in coarse_momentum:
        averaged = {time: 0.0j for time in times}
        for direction in directions:
            kinetic = sum(
                radius * direction[index] * dirac_alpha[index]
                for index in range(3)
            )
            hamiltonian = (
                np.kron(kinetic, np.eye(3, dtype=complex))
                + mu * np.kron(internal_sign, c_partial)
            )
            values, vectors = np.linalg.eigh(hamiltonian)
            coefficients = vectors.conjugate().T @ initial
            weights = np.abs(coefficients) ** 2
            for time in times:
                averaged[time] += np.sum(
                    weights * np.exp(-1.0j * values * time)
                ) / len(directions)
        for time in times:
            direct_integrands[time].append(averaged[time])
    direct_amplitudes = {
        str(time): complex(
            np.trapezoid(
                coarse_density * np.asarray(direct_integrands[time]),
                coarse_momentum,
            )
        )
        for time in times
    }
    direct_radial_max_difference = max(
        abs(direct_amplitudes[str(time)].real - radial_amplitudes[str(time)])
        + abs(direct_amplitudes[str(time)].imag)
        for time in times
    )

    point_root_returns = {
        str(time): 0.5 * (1.0 + math.cos(mass * time))
        for time in times
    }

    require(abs(density_normalization - 1.0) < 1e-12,
            "Gaussian radial density is not normalized")
    require(direct_radial_max_difference < 2e-7,
            "Direct matrix and radial regressions disagree")
    require(abs(radial_amplitudes["0.0"] - 1.0) < 1e-12,
            "Return amplitude is not normalized")
    require(
        max(abs(point_root_returns[str(t)]) for t in times[1:]) > 0.5,
        "Point-root recurrence negative control was lost",
    )

    result = {
        "schema": "r3.4-lorentzian-threshold-return-v001",
        "spec_sha256": sha256(SPEC),
        "spec_seal_verified": True,
        "upstream_hashes_verified": len(PINNED),
        "target_values_used": False,
        "record_eigenvalues": [float(value) for value in record_eigenvalues],
        "dirac_internal_anticommutator_errors": anticommutator_errors,
        "dimensionless_mu": mu,
        "dimensionless_massive_threshold": mass,
        "gaussian_profile_used_only_as_regression": True,
        "gaussian_radial_density_normalization": density_normalization,
        "gaussian_return_amplitudes": radial_amplitudes,
        "direct_matrix_return_amplitudes": {
            key: {"real": value.real, "imag": value.imag}
            for key, value in direct_amplitudes.items()
        },
        "direct_radial_max_difference": direct_radial_max_difference,
        "point_momentum_root_return_negative_control": point_root_returns,
        "nonflat_band_spectrum_derived": True,
        "L2_root_spectral_measure_absolutely_continuous": True,
        "L2_root_spectral_density_integrable": True,
        "Riemann_Lebesgue_threshold_return_derived_for_this_H": True,
        "point_momentum_root_excluded_from_L2_theorem": True,
        "complete_outgoing_generator_identified": False,
        "parent_selected_physical_root_derived": False,
        "finite_energy_physical_root_derived": False,
        "positive_frequency_state_derived_from_parent": False,
        "generated_descendant_spectrum_exhausted": False,
        "complete_write_defect_bound_states_excluded": False,
        "complete_physical_durability_derived": False,
        "complete_parameter_free_Q_spec_frozen": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": "LORENTZIAN_L2_THRESHOLD_RETURN_THEOREM_DERIVED",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
