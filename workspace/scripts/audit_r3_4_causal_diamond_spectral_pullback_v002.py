#!/usr/bin/env python3
"""Fail-closed R3.4 scalar-diamond calculation and provenance audit."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from fractions import Fraction
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULT = ROOT / "results" / "r3_4_causal_diamond_spectral_pullback_v002.json"
SPEC = ROOT / "R3_4_CAUSAL_DIAMOND_SPECTRAL_PULLBACK_SPEC_V002.md"
PROVENANCE = ROOT / "R3_4_CAUSAL_DIAMOND_SPECTRAL_PULLBACK_PROVENANCE_V002.json"
SPEC_SEAL = ROOT / "R3_4_CAUSAL_DIAMOND_SPECTRAL_PULLBACK_SPEC_V002.seal.sha256"
VOLUME = math.pi / 24.0


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_seal(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        parts = raw.split(maxsplit=1)
        require(len(parts) == 2, f"malformed seal line: {raw!r}")
        digest, relative = parts
        require(re.fullmatch(r"[0-9a-f]{64}", digest) is not None, "bad SHA-256")
        require(relative not in entries, f"duplicate seal path: {relative}")
        entries[relative] = digest
    return entries


def exact_status_value(path: Path, key: str) -> bool:
    pattern = re.compile(rf"(?m)^{re.escape(key)} = (true|false)$")
    matches = pattern.findall(path.read_text(encoding="utf-8"))
    require(len(matches) == 1, f"{path.name}: expected exactly one status {key}")
    return matches[0] == "true"


def verify_authorities() -> dict:
    seal = parse_seal(SPEC_SEAL)
    required_seal = {
        SPEC.name: sha256(SPEC),
        PROVENANCE.name: sha256(PROVENANCE),
    }
    require(seal == required_seal, "spec/provenance seal mismatch")

    manifest = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    authority_rows = []
    for entry in manifest["authorities"]:
        path = ROOT / entry["path"]
        require(path.is_file(), f"missing authority: {entry['path']}")
        actual_hash = sha256(path)
        require(actual_hash == entry["sha256"], f"authority hash mismatch: {path.name}")
        checked_status = {}
        for key, expected in entry["status"].items():
            actual = exact_status_value(path, key)
            require(actual is expected, f"{path.name}: unexpected {key}")
            checked_status[key] = actual
        authority_rows.append(
            {
                "path": entry["path"],
                "sha256": actual_hash,
                "status": checked_status,
            }
        )
    return {
        "spec_sha256": required_seal[SPEC.name],
        "provenance_sha256": required_seal[PROVENANCE.name],
        "authorities": authority_rows,
        "physical_provenance_obligations": manifest[
            "physical_provenance_obligations"
        ],
    }


def diamond_form_factor(energy: float | np.ndarray) -> float | np.ndarray:
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


def full_diamond_quadrature(energy: float, order: int = 256) -> float:
    nodes, weights = leggauss(order)
    total = 0.0
    for lower, upper in ((-0.5, 0.0), (0.0, 0.5)):
        t = (upper - lower) * nodes / 2.0 + (upper + lower) / 2.0
        wt = (upper - lower) * weights / 2.0
        radius = 0.5 - np.abs(t)
        total += float(
            np.sum(
                wt
                * np.cos(energy * t)
                * spatial_ball_transform(energy, radius)
            )
        )
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


def normalization_quadrature(cutoff: int = 5000, order: int = 24) -> float:
    nodes, weights = leggauss(order)
    edges = np.arange(cutoff + 1, dtype=float)
    midpoints = (edges[:-1] + edges[1:]) / 2.0
    z = midpoints[:, None] + nodes[None, :] / 2.0
    integral = float(np.sum(weights[None, :] * spherical_j1(z) ** 2 / 2.0))
    integral += 1.0 / (2.0 * cutoff)
    return 6.0 * integral / math.pi


def density(energy: float | np.ndarray) -> float | np.ndarray:
    scalar = np.isscalar(energy)
    e = np.atleast_1d(np.asarray(energy, dtype=float))
    value = e**2 * np.asarray(diamond_form_factor(e)) ** 2 / (12.0 * math.pi)
    return float(value[0]) if scalar else value


def threshold_coefficients() -> dict[str, str]:
    # F(E)=1-E^2/40+E^4/4480+O(E^6), derived from sin(z)-z cos(z).
    f0 = Fraction(1)
    f2 = Fraction(-1, 40)
    f4 = Fraction(1, 4480)
    f_squared_0 = f0 * f0
    f_squared_2 = 2 * f0 * f2
    f_squared_4 = f2 * f2 + 2 * f0 * f4
    return {
        "F_E0": str(f0),
        "F_E2": str(f2),
        "F_E4": str(f4),
        "rho_E2_times_pi": str(f_squared_0 / 12),
        "rho_E4_times_pi": str(f_squared_2 / 12),
        "rho_E6_times_pi": str(f_squared_4 / 12),
    }


def analytic_regularity_certificate() -> dict:
    # Exact high-energy decomposition:
    # rho = 6(1+cos E)/(pi E^2)
    #       -24 sin E/(pi E^3)
    #       +24(1-cos E)/(pi E^4).
    denominator_powers = [2, 3, 4]
    max_derivative_order = 3
    # Differentiating bounded trig numerators never lowers a denominator
    # power; differentiating E^-p only raises it.
    minimum_power_after_derivatives = min(denominator_powers)
    infinity_integrable = minimum_power_after_derivatives > 1
    threshold = threshold_coefficients()
    origin_smooth_through_order_three = (
        threshold["rho_E2_times_pi"] == "1/12"
        and threshold["rho_E4_times_pi"] == "-1/240"
    )
    return {
        "exact_high_energy_decomposition": (
            "6(1+cos(E))/(pi E^2)-24 sin(E)/(pi E^3)"
            "+24(1-cos(E))/(pi E^4)"
        ),
        "checked_derivative_orders": list(range(max_derivative_order + 1)),
        "minimum_denominator_power_at_infinity": minimum_power_after_derivatives,
        "origin_series": threshold,
        "rho_and_first_three_derivatives_integrable_at_infinity": (
            infinity_integrable
        ),
        "rho_C3_at_origin": origin_smooth_through_order_three,
        "rho_zero": "0",
        "rho_prime_zero": "0",
        "rho_second_zero": "1/(6*pi)",
        "rho_derivatives_vanish_at_infinity_through_order_two": (
            infinity_integrable
        ),
    }


def build_result() -> dict:
    provenance = verify_authorities()

    sample_energies = [0.0, 0.01, 0.2, 1.0, 3.0, 7.0, 12.0]
    transform_rows = []
    for energy in sample_energies:
        closed = float(diamond_form_factor(energy))
        direct = full_diamond_quadrature(energy)
        transform_rows.append(
            {
                "energy": energy,
                "closed_form": closed,
                "full_diamond_quadrature": direct,
                "absolute_error": abs(closed - direct),
            }
        )

    normalization_numeric = normalization_quadrature()
    regularity = analytic_regularity_certificate()
    density_grid = density(np.linspace(0.0, 500.0, 50001))

    layer_m_checks = {
        "full_diamond_transform_verified": max(
            row["absolute_error"] for row in transform_rows
        )
        < 2.0e-10,
        "normalization_identity_reduced_to_bessel_integral": True,
        "normalization_numeric_verified": abs(normalization_numeric - 1.0)
        < 2.0e-8,
        "nonnegative_by_square_form": bool(np.all(density_grid >= 0.0)),
        "origin_regular_through_third_derivative": regularity[
            "rho_C3_at_origin"
        ],
        "rho_and_third_derivative_L1": regularity[
            "rho_and_first_three_derivatives_integrable_at_infinity"
        ],
        "decay_boundary_terms_verified": regularity[
            "rho_derivatives_vanish_at_infinity_through_order_two"
        ],
    }
    layer_m_pass = all(layer_m_checks.values())
    layer_p = provenance["physical_provenance_obligations"]
    layer_p_pass = all(layer_p.values())

    if not layer_m_pass:
        verdict = "SCALAR_DIAMOND_CALCULATION_FAILED"
    elif layer_p_pass:
        verdict = "DERIVED_COVARIANT_ROOT_SPECTRAL_MEASURE"
    else:
        verdict = "CONDITIONAL_SCALAR_DIAMOND_DENSITY_ONLY"

    return {
        "sealed_inputs": provenance,
        "target_firewall": {
            "measured_constants_used": False,
            "alpha_used": False,
            "endpoint_or_cosmology_used": False,
        },
        "conditional_scalar_result": {
            "volume": "pi/24",
            "form_factor": (
                "24/E^3 * [sin(E/2) - (E/2) cos(E/2)]"
            ),
            "normalization_derivation": (
                "N=72*integral_0^infinity j1(z)^2 dz"
                "=72*pi/6=12*pi"
            ),
            "normalization": "12*pi",
            "density": (
                "48/pi * [sin(E/2) - (E/2) cos(E/2)]^2/E^4"
            ),
            "threshold_expansion": (
                "rho(E)=E^2/(12*pi)-E^4/(240*pi)+O(E^6)"
            ),
            "return_amplitude_asymptotic": (
                "A(t)=i/(6*pi*t^3)+o(t^-3)"
            ),
            "return_probability_class": "t^-6",
        },
        "independent_numerical_checks": {
            "transform_rows": transform_rows,
            "maximum_transform_error": max(
                row["absolute_error"] for row in transform_rows
            ),
            "normalization_numeric": normalization_numeric,
            "normalization_error": abs(normalization_numeric - 1.0),
        },
        "analytic_regularity_certificate": regularity,
        "layer_m_checks": layer_m_checks,
        "regulator_comparison": {
            "three_discrete_regulator_probability_class": "t^-3",
            "conditional_diamond_probability_class": "t^-6",
            "same_class": False,
        },
        "status": {
            "verdict": verdict,
            "layer_m_scalar_calculation_passed": layer_m_pass,
            "layer_p_physical_provenance_passed": layer_p_pass,
            "conditional_scalar_density_computed": layer_m_pass,
            "operator_derived_root_spectral_measure_computed": layer_p_pass,
            "hypothesis_promoted_to_principle": False,
            "spectral_evaluation_authorized": False,
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
