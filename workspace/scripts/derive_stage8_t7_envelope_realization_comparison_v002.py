#!/usr/bin/env python3
"""Higher-resolution blind ER-A/ER-B Hermite-Galerkin comparison."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np

import derive_stage8_t7_hermite_galerkin_baseline_v001 as base


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_NUMERICS_SUCCESSOR_SPEC_V001.md"
OUT = ROOT / "stage8_execution/work/T07_envelope_realization_comparison_v002.json"

AUTHORITIES = {
    "R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md":
        "e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2",
    "STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.md":
        "202f8d8db60046a8069b1cd8fcc38f505eb95fa29578e094e005f56e967c3a35",
    "STAGE8_T7_HERMITE_GALERKIN_BASELINE_SPEC_V001.md":
        "80aa4e1722c117e8195ce0fb2ae3fc37262bc8fc2ba5d79a6dd38cd1029bc26d",
    "STAGE8_T7_HERMITE_GALERKIN_NUMERICS_PROTOCOL_V001.md":
        "950e957ec2aa1022509b57df48f4f701e717e5dcbb18731332abbf55bf57dadd",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def envelope_value(mode: str, midpoint: float) -> float:
    radius = min(midpoint, 1.0 - midpoint)
    tau = math.pi / math.sqrt(2.0)
    if mode == "ER-A":
        return tau * 32.0 * radius**3
    if mode == "ER-B":
        return tau * 24.0 / math.pi
    raise ValueError(mode)


def propagate_histories(
    h0: np.ndarray,
    source_incidence: np.ndarray,
    multiplications: tuple[np.ndarray, ...],
    mode: str,
) -> tuple[np.ndarray, ...]:
    steps = len(multiplications)
    dt = 1.0 / steps
    half_free = base.exp_hermitian(h0, 0.5 * dt)
    free_full = base.exp_hermitian(h0, 1.0)
    output = []
    for record_value in (-math.sqrt(2.0), 0.0, math.sqrt(2.0)):
        if record_value == 0.0:
            output.append(free_full)
            continue
        value = np.eye(h0.shape[0], dtype=complex)
        for index, multiplication in enumerate(multiplications):
            midpoint = (index + 0.5) / steps
            value = half_free @ value
            value = base.apply_interaction(
                value,
                multiplication,
                source_incidence,
                record_value * envelope_value(mode, midpoint) * dt,
            )
            value = half_free @ value
        output.append(value)
    return tuple(output)


def stored_complex(value: dict[str, float]) -> complex:
    return complex(value["real"], value["imag"])


def run_case(
    n: int,
    ell: float,
    alphas: tuple[np.ndarray, ...],
    incidence: np.ndarray,
) -> dict[str, object]:
    h0 = base.free_dirac(n, ell, alphas)
    values, vectors = np.linalg.eigh(h0)
    occupied = vectors[:, values < 0.0]
    covariance = base.mixed_covariance(n, alphas)

    branches: dict[str, object] = {}
    maximum_unitarity_error = 0.0
    for mode in ("ER-A", "ER-B"):
        amplitudes: dict[str, object] = {}
        for steps in (24, 48, 96):
            multiplications = base.cell_matrices(n, ell, steps, (10, 10, 20))
            histories = propagate_histories(h0, incidence, multiplications, mode)
            maximum_unitarity_error = max(
                maximum_unitarity_error,
                max(
                    float(
                        np.linalg.norm(
                            unitary.conjugate().T @ unitary
                            - np.eye(unitary.shape[0], dtype=complex)
                        )
                    )
                    for unitary in histories
                ),
            )
            mixed, pure, _, _ = base.completed_amplitudes(
                histories, covariance, occupied
            )
            amplitudes[str(steps)] = {
                "mixed": base.complex_json(mixed),
                "pure": base.complex_json(pure),
            }

        secondary_m = base.cell_matrices(n, ell, 96, (12, 12, 24))
        secondary_h = propagate_histories(h0, incidence, secondary_m, mode)
        secondary_mixed, secondary_pure, _, _ = base.completed_amplitudes(
            secondary_h, covariance, occupied
        )

        convergence = {}
        for scheme, secondary in (
            ("mixed", secondary_mixed),
            ("pure", secondary_pure),
        ):
            a24 = stored_complex(amplitudes["24"][scheme])
            a48 = stored_complex(amplitudes["48"][scheme])
            a96 = stored_complex(amplitudes["96"][scheme])
            first = abs(a24 - a48)
            second = abs(a48 - a96)
            convergence[scheme] = {
                "24_to_48": float(first),
                "48_to_96": float(second),
                "ratio": float(first / second if second else math.inf),
                "improving": bool(second < first),
                "secondary_quadrature_difference": float(abs(a96 - secondary)),
            }
        branches[mode] = {
            "amplitudes": amplitudes,
            "secondary_quadrature_96": {
                "mixed": base.complex_json(secondary_mixed),
                "pure": base.complex_json(secondary_pure),
            },
            "convergence": convergence,
        }

    a = branches["ER-A"]["amplitudes"]["96"]
    b = branches["ER-B"]["amplitudes"]["96"]
    return {
        "n": n,
        "ell": ell,
        "spinor_dimension": int(h0.shape[0]),
        "branches": branches,
        "ER_A_to_ER_B_absolute_difference_N96": {
            scheme: float(abs(stored_complex(a[scheme]) - stored_complex(b[scheme])))
            for scheme in ("mixed", "pure")
        },
        "maximum_unitarity_error": maximum_unitarity_error,
    }


def main() -> None:
    for relative, expected in AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"Authority drift: {relative}")

    alphas, incidence, clifford_error = base.dirac_matrices()
    cases = [
        run_case(n, ell, alphas, incidence)
        for n in (2, 4)
        for ell in (1.0, math.sqrt(2.0))
    ]
    numerics_pass = (
        clifford_error < 1e-12
        and all(case["maximum_unitarity_error"] < 2e-10 for case in cases)
        and all(
            branch["convergence"][scheme]["improving"]
            for case in cases
            for branch in case["branches"].values()
            for scheme in ("mixed", "pure")
        )
        and all(
            branch["convergence"][scheme]["secondary_quadrature_difference"] < 5e-4
            for case in cases
            for branch in case["branches"].values()
            for scheme in ("mixed", "pure")
        )
    )
    result = {
        "schema": "stage8_t7_envelope_realization_comparison_v002",
        "spec_sha256": sha256(SPEC),
        "cases": cases,
        "numerics_pass": numerics_pass,
        "overall_verdict": (
            "ENVELOPE_BRANCH_HIGH_RESOLUTION_BASELINES_COMPUTED"
            if numerics_pass
            else "ENVELOPE_BRANCH_NUMERICS_BLOCKED"
        ),
        "ER_A_selected": False,
        "ER_B_selected": False,
        "envelope_realization_derived": False,
        "physical_regulator_completed_record_baseline_derived": False,
        "sharp_cell_implementability_proved": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not numerics_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
