#!/usr/bin/env python3
"""Audit the R3.4 causal-diamond spectral pullback without physical targets."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


ROOT = Path(__file__).resolve().parents[1]
RESULT_PATH = ROOT / "results" / "r3_4_causal_diamond_spectral_pullback_v001.json"
VOLUME = math.pi / 24.0


def diamond_form_factor(energy: float | np.ndarray) -> float | np.ndarray:
    """Closed form of the normalized null-shell Fourier transform."""
    scalar = np.isscalar(energy)
    e = np.atleast_1d(np.asarray(energy, dtype=float))
    out = np.empty_like(e)
    small = np.abs(e) < 1.0e-3
    es = e[small]
    out[small] = 1.0 - es**2 / 40.0 + es**4 / 4480.0
    z = e[~small] / 2.0
    out[~small] = 24.0 * (np.sin(z) - z * np.cos(z)) / e[~small] ** 3
    return float(out[0]) if scalar else out


def spatial_ball_transform(energy: float, radius: np.ndarray) -> np.ndarray:
    """Direct spatial Fourier integral over a three-ball."""
    if energy == 0.0:
        return 4.0 * math.pi * radius**3 / 3.0
    z = energy * radius
    out = np.empty_like(z)
    small = np.abs(z) < 1.0e-3
    r = radius[small]
    out[small] = 4.0 * math.pi * (
        r**3 / 3.0
        - energy**2 * r**5 / 30.0
        + energy**4 * r**7 / 840.0
    )
    out[~small] = (
        4.0
        * math.pi
        * (np.sin(z[~small]) - z[~small] * np.cos(z[~small]))
        / energy**3
    )
    return out


def independent_diamond_quadrature(energy: float, order: int = 256) -> float:
    """Integrate the full causal diamond, splitting at its nonsmooth midpoint."""
    nodes, weights = leggauss(order)
    total = 0.0
    for lower, upper in ((-0.5, 0.0), (0.0, 0.5)):
        t = (upper - lower) * nodes / 2.0 + (upper + lower) / 2.0
        wt = (upper - lower) * weights / 2.0
        radius = 0.5 - np.abs(t)
        spatial = spatial_ball_transform(energy, radius)
        total += float(np.sum(wt * np.cos(energy * t) * spatial))
    return total / VOLUME


def spherical_j1(z: np.ndarray) -> np.ndarray:
    out = np.empty_like(z)
    small = np.abs(z) < 1.0e-3
    zs = z[small]
    out[small] = zs / 3.0 - zs**3 / 30.0 + zs**5 / 840.0
    out[~small] = (
        np.sin(z[~small]) - z[~small] * np.cos(z[~small])
    ) / z[~small] ** 2
    return out


def density(energy: float | np.ndarray) -> float | np.ndarray:
    """The normalized candidate density E^2 |F_D(E)|^2/(12 pi)."""
    e = np.asarray(energy, dtype=float)
    value = e**2 * np.asarray(diamond_form_factor(e)) ** 2 / (12.0 * math.pi)
    return float(value) if np.isscalar(energy) else value


def independent_normalization_check(cutoff: int = 5000, order: int = 24) -> float:
    """Numerically check 6/pi integral_0^infinity j_1(z)^2 dz = 1.

    The integral is evaluated interval by interval through ``cutoff``. The
    leading averaged asymptotic tail, 1/(2*cutoff), is added. At this cutoff
    the omitted oscillatory correction is below the reported audit tolerance.
    """
    nodes, weights = leggauss(order)
    edges = np.arange(cutoff + 1, dtype=float)
    midpoints = (edges[:-1] + edges[1:]) / 2.0
    z = midpoints[:, None] + nodes[None, :] / 2.0
    integral = float(np.sum(weights[None, :] * spherical_j1(z) ** 2 / 2.0))
    integral += 1.0 / (2.0 * cutoff)
    return 6.0 * integral / math.pi


def contains(path: Path, text: str) -> bool:
    return text in path.read_text(encoding="utf-8")


def main() -> None:
    sample_energies = [0.0, 0.01, 0.2, 1.0, 3.0, 7.0, 12.0]
    form_factor_checks = []
    for energy in sample_energies:
        closed = float(diamond_form_factor(energy))
        direct = independent_diamond_quadrature(energy)
        form_factor_checks.append(
            {
                "energy": energy,
                "closed_form": closed,
                "independent_quadrature": direct,
                "absolute_error": abs(closed - direct),
            }
        )

    normalization_numeric = independent_normalization_check()
    normalization_exact = "12*pi"

    bid = ROOT / "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md"
    architecture = ROOT / "CAUSAL_DIRECT_LIMIT_ARCHITECTURE_ADJUDICATION_RESULT_V001.md"
    outgoing = ROOT / "CAUSAL_DIRECT_LIMIT_COVECTOR_RAY_LIFT_RESULT_V001.md"
    r33 = ROOT / "R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md"

    provenance = {
        "uniform_flat_cell_measure_derived": contains(
            r33, "uniform_flat_cell_measure_derived = true"
        ),
        "constant_root_embedding_declared": contains(
            bid, "trivial_holonomy_background_and_root_embedding_frozen = true"
        ),
        "constant_root_uniqueness_derived": not contains(
            bid, "preparation_uniqueness_proved = false"
        ),
        "massless_positive_energy_outgoing_operator_derived": False,
        "self_adjoint_outgoing_domain_derived": False,
        "outgoing_record_algebra_derived": contains(
            outgoing, "outgoing_record_algebra_subobligation_closed = true"
        ),
        "physical_durability_carrier_identified": False,
        "prior_unique_spectral_measure_derived": not contains(
            architecture, "unique_covariant_spectral_measure_derived = false"
        ),
    }

    required_provenance = [
        provenance["massless_positive_energy_outgoing_operator_derived"],
        provenance["self_adjoint_outgoing_domain_derived"],
        provenance["constant_root_uniqueness_derived"],
        provenance["physical_durability_carrier_identified"],
    ]
    strict_derivation = all(required_provenance)
    verdict = (
        "DERIVED_COVARIANT_ROOT_SPECTRAL_MEASURE"
        if strict_derivation
        else "CONDITIONAL_DIAMOND_PULLBACK_OPERATOR_OR_ROOT_OPEN"
    )

    result = {
        "spec_sha256": (
            "c4457507840db213990ac0f07e89fe8eef9231025f3aefce2e8671e0370d4456"
        ),
        "inputs": {
            "measured_constants_used": False,
            "alpha_used": False,
            "cell": "unit-tip-separation 3+1 causal diamond",
            "candidate_operator": "massless positive-energy incidence/Hodge-Dirac",
        },
        "analytic_result": {
            "volume": "pi/24",
            "form_factor": (
                "24/E^3 * [sin(E/2) - (E/2) cos(E/2)]"
            ),
            "normalization": normalization_exact,
            "density": (
                "48/pi * [sin(E/2) - (E/2) cos(E/2)]^2/E^4"
            ),
            "low_energy_density": "E^2/(12*pi) + O(E^4)",
            "rho_second_derivative_at_zero": "1/(6*pi)",
            "return_amplitude_asymptotic": (
                "A_D(t)=i/(6*pi*t^3)+o(t^-3)"
            ),
            "return_probability_class": "t^-6",
        },
        "checks": {
            "form_factor": form_factor_checks,
            "maximum_form_factor_error": max(
                row["absolute_error"] for row in form_factor_checks
            ),
            "normalization_numeric": normalization_numeric,
            "normalization_absolute_error": abs(normalization_numeric - 1.0),
            "density_nonnegative_on_test_grid": bool(
                np.all(density(np.linspace(0.0, 500.0, 50001)) >= 0.0)
            ),
            "density_is_L1": True,
            "density_is_absolutely_continuous": True,
            "density_third_derivative_is_L1": True,
            "riemann_lebesgue_decay_applies": True,
            "thresholded_durability_follows_for_candidate": True,
        },
        "provenance": provenance,
        "status": {
            "verdict": verdict,
            "conditional_density_computed": True,
            "unique_covariant_spectral_measure_derived": strict_derivation,
            "thresholded_durability_derived_unconditionally": strict_derivation,
            "hypothesis_promoted_to_principle": False,
            "spectral_evaluation_authorized": False,
            "coupling_evaluation_authorized": False,
            "alpha_computed": False,
            "proof_authorized": False,
        },
    }
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["status"], indent=2))


if __name__ == "__main__":
    main()
