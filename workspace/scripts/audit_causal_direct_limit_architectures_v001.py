#!/usr/bin/env python3
"""Blind architecture and decay audit for the causal direct-limit hypothesis."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "CAUSAL_DIRECT_LIMIT_ARCHITECTURE_TEST_SPEC_V001.md"
EXPECTED_SPEC_SHA256 = (
    "e8635914554741333f05db3fea8b055bfb76df2cfca322c1c177c53a99a50317"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def path_endpoint_amplitude(times: np.ndarray, scale: float = 1.0) -> np.ndarray:
    count = 16384
    k = (np.arange(count, dtype=float) + 0.5) * math.pi / count
    weights = np.sin(k) ** 2
    weights /= weights.sum()
    eigenvalues = 2.0 * scale * np.cos(k)
    return np.exp(-1.0j * np.outer(times, eigenvalues)) @ weights


def cubic_lattice_amplitude(times: np.ndarray) -> np.ndarray:
    count = 16384
    k = (np.arange(count, dtype=float) + 0.5) * 2.0 * math.pi / count
    one_axis = np.exp(-1.0j * np.outer(times, 2.0 * np.cos(k))).mean(axis=1)
    return one_axis**3


def covariant_continuum_amplitude(times: np.ndarray) -> np.ndarray:
    return (1.0 + 1.0j * times) ** -3


def effective_continuum_amplitude(times: np.ndarray) -> np.ndarray:
    return (1.0 + 1.0j * times) ** -1


def interval_averages(amplitude_function) -> tuple[list[dict[str, float]], float]:
    windows = [(8.0, 12.0), (12.0, 18.0), (18.0, 27.0),
               (27.0, 40.0), (40.0, 60.0), (60.0, 90.0)]
    rows: list[dict[str, float]] = []
    centers: list[float] = []
    means: list[float] = []
    for lower, upper in windows:
        times = np.linspace(lower, upper, 256, dtype=float)
        probability = np.abs(amplitude_function(times)) ** 2
        mean_probability = float(probability.mean())
        center = math.sqrt(lower * upper)
        centers.append(center)
        means.append(mean_probability)
        rows.append(
            {
                "lower_t": lower,
                "upper_t": upper,
                "geometric_center_t": center,
                "mean_root_probability": mean_probability,
            }
        )
    slope, _ = np.polyfit(np.log(centers), np.log(means), 1)
    return rows, float(-slope)


def finite_path_amplitude(size: int, times: np.ndarray, scale: float) -> np.ndarray:
    mode = np.arange(1, size + 1, dtype=float)
    k = mode * math.pi / (size + 1)
    eigenvalues = 2.0 * scale * np.cos(k)
    root_weights = 2.0 * np.sin(k) ** 2 / (size + 1)
    return np.exp(-1.0j * np.outer(times, eigenvalues)) @ root_weights


def finite_ring_axis_amplitude(size: int, times: np.ndarray) -> np.ndarray:
    k = 2.0 * math.pi * np.arange(size, dtype=float) / size
    return np.exp(-1.0j * np.outer(times, 2.0 * np.cos(k))).mean(axis=1)


def convergence_rows() -> dict[str, list[dict[str, float]]]:
    times = np.linspace(0.0, 10.0, 201, dtype=float)
    half_reference = path_endpoint_amplitude(times)
    tree_reference = path_endpoint_amplitude(times, math.sqrt(3.0))
    lattice_reference = cubic_lattice_amplitude(times)
    output: dict[str, list[dict[str, float]]] = {
        "A1_causal_half_line": [],
        "A2_three_branch_tree_radial_sector": [],
        "A3_cubic_lattice": [],
        "A4_covariant_continuum_quadrature": [],
    }
    for size in (16, 32, 64, 128):
        half = finite_path_amplitude(size, times, 1.0)
        tree = finite_path_amplitude(size, times, math.sqrt(3.0))
        lattice = finite_ring_axis_amplitude(size, times) ** 3
        output["A1_causal_half_line"].append(
            {"size": size, "max_compact_time_amplitude_error":
             float(np.max(np.abs(half - half_reference)))}
        )
        output["A2_three_branch_tree_radial_sector"].append(
            {"size": size, "max_compact_time_amplitude_error":
             float(np.max(np.abs(tree - tree_reference)))}
        )
        output["A3_cubic_lattice"].append(
            {"size": size, "max_compact_time_amplitude_error":
             float(np.max(np.abs(lattice - lattice_reference)))}
        )

    exact = covariant_continuum_amplitude(times)
    for size in (128, 256, 512, 1024):
        energy_max = 24.0
        energy = (np.arange(size, dtype=float) + 0.5) * energy_max / size
        weights = 0.5 * energy**2 * np.exp(-energy)
        weights /= weights.sum()
        approximate = np.exp(-1.0j * np.outer(times, energy)) @ weights
        output["A4_covariant_continuum_quadrature"].append(
            {"size": size, "max_compact_time_amplitude_error":
             float(np.max(np.abs(approximate - exact)))}
        )
    return output


def sampled_thresholds(amplitude_function) -> list[dict[str, float | bool]]:
    times = np.linspace(0.0, 240.0, 12001, dtype=float)
    probability = np.abs(amplitude_function(times)) ** 2
    rows: list[dict[str, float | bool]] = []
    for delta in (1.0e-1, 1.0e-2, 1.0e-3):
        exceed = np.flatnonzero(probability >= delta)
        last = float(times[exceed[-1]]) if exceed.size else 0.0
        rows.append(
            {
                "delta": delta,
                "last_sampled_exceedance_t": last,
                "tail_below_delta_on_sampled_grid": bool(
                    np.all(probability[times > last] < delta)
                ),
                "certified_for_all_later_times": False,
            }
        )
    return rows


def main() -> None:
    actual_hash = file_sha256(SPEC)
    require(actual_hash == EXPECTED_SPEC_SHA256, "Frozen specification changed")

    architectures = [
        (
            "A1_causal_half_line",
            path_endpoint_amplitude,
            "REGULATOR_OR_RADIAL_REDUCTION",
            "one-dimensional causal/radial evolution has no faithful "
            "microscopic 3+1 Lorentz action",
        ),
        (
            "A2_three_branch_causal_tree",
            lambda times: path_endpoint_amplitude(times, math.sqrt(3.0)),
            "REGULATOR_OR_RADIAL_REDUCTION",
            "the rooted tree carries a preferred branching foliation; its "
            "radial sector may regulate a covariant limit",
        ),
        (
            "A3_three_dimensional_spatial_lattice",
            cubic_lattice_amplitude,
            "REGULATOR_OR_RADIAL_REDUCTION",
            "the cubic symmetry group is discrete and the finite lattice "
            "selects a preferred frame",
        ),
        (
            "A4_Lorentz_covariant_causal_complex_continuum",
            covariant_continuum_amplitude,
            "PHYSICAL_CLASS",
            "the physical limit can carry the disclosed 3+1 Lorentz action "
            "and causal composition without a preferred frame",
        ),
        (
            "A5_effective_environment_continuum",
            effective_continuum_amplitude,
            "EFFECTIVE_DESCRIPTION",
            "a reduced spectral environment is physical only after its "
            "density is derived from the covariant parent",
        ),
    ]

    decay_rows = []
    for name, amplitude_function, classification, reason in architectures:
        averages, exponent = interval_averages(amplitude_function)
        decay_rows.append(
            {
                "architecture": name,
                "covariance_classification": classification,
                "classification_reason": reason,
                "late_time_probability_exponent_fit": exponent,
                "interval_averages": averages,
                "sampled_thresholds": sampled_thresholds(amplitude_function),
            }
        )

    convergence = convergence_rows()
    convergence_improves = {}
    for name, rows in convergence.items():
        errors = [row["max_compact_time_amplitude_error"] for row in rows]
        convergence_improves[name] = bool(errors[-1] < errors[0])

    direct_limit = {
        "bounded_degree_exhaustion_suffices_for_bounded_self_adjoint_limit":
            True,
        "finite_compressions_converge_strongly_on_compact_time_intervals":
            True,
        "numerical_regulator_convergence_improves":
            convergence_improves,
        "L1_absolutely_continuous_root_spectral_density_implies_decay":
            True,
        "Lorentz_covariance_forces_unique_causal_complex": False,
        "Lorentz_covariance_forces_unique_root_spectral_density": False,
        "Lorentz_covariance_forces_absolute_continuity": False,
        "record_principles_derive_label_preserving_outgoing_tail_algebra":
            False,
        "thresholded_root_return_durability_is_conditional": True,
        "full_outgoing_record_recoverability_proved": False,
    }

    result = {
        "schema": "causal-direct-limit-architecture-audit-v001",
        "frozen_spec_sha256": actual_hash,
        "target_values_used": False,
        "coupling_evaluated": False,
        "architectures_reported_in_sealed_order": [
            row["architecture"] for row in decay_rows
        ],
        "winner_or_ranking_emitted": False,
        "covariance_selector": {
            "status": "CLASS_LEVEL_SELECTOR_ONLY",
            "physical_class": [
                "A4_Lorentz_covariant_causal_complex_continuum"
            ],
            "regulator_classes": [
                "A1_causal_half_line",
                "A2_three_branch_causal_tree",
                "A3_three_dimensional_spatial_lattice",
            ],
            "effective_descriptions": [
                "A5_effective_environment_continuum"
            ],
            "unique_microscopic_complex_selected": False,
            "unique_spectral_measure_selected": False,
        },
        "decay_laws": decay_rows,
        "finite_regulator_convergence": convergence,
        "direct_limit_existence_attempt": direct_limit,
        "fork_8_closed": False,
        "hypothesis_promoted_to_principle": False,
        "complete_parent_action_derived": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": "HYPOTHESIS_NOT_PROMOTED_CLASS_SELECTED_DYNAMICS_OPEN",
    }

    output = ROOT / "results" / "causal_direct_limit_architecture_audit_v001.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
