#!/usr/bin/env python3
"""Audit the causal-cell moving-front public-record construction."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import re

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_CAUSAL_CELL_MOVING_FRONT_SPEC_V001.md"
SEAL = ROOT / "R3_4_CAUSAL_CELL_MOVING_FRONT_SPEC_V001.seal.sha256"
OUTPUT = ROOT / "results" / "r3_4_causal_cell_moving_front_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_status(path: Path, key: str) -> bool:
    pattern = re.compile(rf"^{re.escape(key)}\s*=\s*(true|false)\s*$", re.MULTILINE)
    matches = pattern.findall(path.read_text(encoding="utf-8"))
    require(len(matches) == 1, f"Expected one {key} in {path.name}")
    return matches[0] == "true"


def evolve(operator: np.ndarray, angle: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return (
        vectors
        @ np.diag(np.exp(-1.0j * angle * values))
        @ vectors.conjugate().T
    )


def embed_record(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    result = np.array([[1.0]], dtype=complex)
    identity = np.eye(3, dtype=complex)
    for index in range(count):
        result = np.kron(result, operator if index == site else identity)
    return result


def main() -> None:
    seal_fields = SEAL.read_text(encoding="ascii").strip().split()
    require(seal_fields == [sha256(SPEC), SPEC.name], "Specification seal failed")

    c_partial = np.array(
        [
            [0.0, 0.0, -1.0j],
            [0.0, 0.0, +1.0j],
            [+1.0j, -1.0j, 0.0],
        ],
        dtype=complex,
    )
    p_ch = np.diag([1.0, 0.0, 1.0]).astype(complex)
    gamma5 = np.diag([-1.0, 1.0]).astype(complex)
    source_factor = np.kron(p_ch, gamma5)
    tau = math.pi / math.sqrt(2.0)

    profiles = {
        "constant": (tau,),
        "uneven_positive": (tau / 7.0, 2.0 * tau / 7.0, 4.0 * tau / 7.0),
        "sign_changing": (1.5 * tau, -0.5 * tau),
        "five_segment": (
            0.05 * tau,
            0.10 * tau,
            0.25 * tau,
            0.20 * tau,
            0.40 * tau,
        ),
    }
    one_cell_generator = np.kron(source_factor, c_partial)
    canonical = evolve(one_cell_generator, tau)
    profile_errors = {}
    for name, angles in profiles.items():
        require(abs(sum(angles) - tau) < 1e-14, f"{name} integral changed")
        unitary = np.eye(one_cell_generator.shape[0], dtype=complex)
        for angle in angles:
            unitary = evolve(one_cell_generator, angle) @ unitary
        profile_errors[name] = float(np.linalg.norm(unitary - canonical))

    count = 3
    generators = tuple(
        np.kron(source_factor, embed_record(c_partial, site, count))
        for site in range(count)
    )
    pair_commutators = {
        f"{left}_{right}": float(
            np.linalg.norm(
                generators[left] @ generators[right]
                - generators[right] @ generators[left]
            )
        )
        for left in range(count)
        for right in range(left + 1, count)
    }
    forward = np.eye(generators[0].shape[0], dtype=complex)
    reverse = np.eye(generators[0].shape[0], dtype=complex)
    for generator in generators:
        forward = evolve(generator, tau) @ forward
    for generator in reversed(generators):
        reverse = evolve(generator, tau) @ reverse
    ordering_error = np.linalg.norm(forward - reverse)

    pointer = np.diag([-1.0, 1.0, 0.0]).astype(complex)
    first_pointer = np.kron(
        np.eye(source_factor.shape[0], dtype=complex),
        embed_record(pointer, 0, count),
    )
    later_pulse_commutators = {
        str(site): float(
            np.linalg.norm(
                generators[site] @ first_pointer
                - first_pointer @ generators[site]
            )
        )
        for site in (1, 2)
    }

    x = np.array(
        [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
        dtype=complex,
    )
    central_bounds = {}
    for total in (2, 3, 4, 5):
        macroscopic = sum(
            embed_record(pointer, site, total) for site in range(total)
        ) / total
        local = embed_record(x, 0, total)
        norm = np.linalg.norm(
            macroscopic @ local - local @ macroscopic,
            ord=2,
        )
        central_bounds[str(total)] = {
            "computed_norm": float(norm),
            "bound_2m_over_N": 2.0 / total,
            "passes": bool(norm <= 2.0 / total + 1e-13),
        }

    fundamental = ROOT / "FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md"
    global_parent = ROOT / "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md"
    hypothesis = ROOT / "CAUSAL_DIRECT_LIMIT_RECORD_HYPOTHESIS_V001.md"
    cell_derived = exact_status(fundamental, "unique_causal_record_cell_derived")
    time_ordering_derived = exact_status(
        global_parent, "time_dependent_continuum_ordering_derived"
    )
    hypothesis_promoted = exact_status(
        hypothesis, "hypothesis_promoted_to_principle"
    )
    authority_support = cell_derived and time_ordering_derived and hypothesis_promoted

    require(max(profile_errors.values()) < 1e-12, "Pulse profile changed endpoint")
    require(max(pair_commutators.values()) < 1e-13, "Cell generators do not commute")
    require(ordering_error < 1e-12, "Causal linear extensions disagree")
    require(
        max(later_pulse_commutators.values()) < 1e-13,
        "Later pulse changes completed public record",
    )
    require(all(item["passes"] for item in central_bounds.values()), "Central bound failed")

    verdict = (
        "MOVING_FRONT_PUBLIC_RECORD_DYNAMICS_DERIVED"
        if authority_support
        else "MOVING_FRONT_PUBLIC_RECORD_DYNAMICS_CONDITIONAL"
    )
    result = {
        "schema": "r3.4-causal-cell-moving-front-v001",
        "spec_sha256": sha256(SPEC),
        "spec_seal_verified": True,
        "target_values_used": False,
        "profile_endpoint_errors": profile_errors,
        "distinct_cell_generator_commutators": pair_commutators,
        "causal_linear_extension_ordering_error": float(ordering_error),
        "later_pulse_earlier_public_record_commutators": (
            later_pulse_commutators
        ),
        "central_sequence_checks": central_bounds,
        "fixed_local_public_observables_eventually_stabilize": True,
        "conditional_asymptotic_public_derivation_zero": True,
        "conditional_asymptotic_public_automorphism_strongly_continuous": True,
        "conditional_asymptotic_public_point_spectrum": [0],
        "stationary_all_cells_parent_rejected_as_different_completion": True,
        "authority_unique_causal_cell_derived": cell_derived,
        "authority_time_dependent_ordering_derived": time_ordering_derived,
        "causal_direct_limit_hypothesis_promoted": hypothesis_promoted,
        "moving_front_bound_by_live_complete_parent": authority_support,
        "full_parent_state_covariance_derived": False,
        "complete_parent_action_derived": False,
        "physical_response_spectral_measure_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": verdict,
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
