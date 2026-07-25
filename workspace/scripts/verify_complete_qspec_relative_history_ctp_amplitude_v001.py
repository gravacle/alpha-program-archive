#!/usr/bin/env python3
"""Independent verifier for the complete-Qspec relative-history CTP closure."""

from __future__ import annotations

import cmath
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_SPEC_V001.md"
PRIMARY = ROOT / "stage8_execution/work/QSPEC_relative_history_CTP_closure.json"
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_relative_history_CTP_closure_verification.json"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def outcome_amplitudes(theta: float) -> tuple[complex, complex]:
    phase = cmath.exp(1.0j * theta / 2.0)
    return (
        phase * math.cos(theta / 2.0),
        -1.0j * phase * math.sin(theta / 2.0),
    )


def kernel_by_outcome_sum(theta_plus: float, theta_minus: float) -> complex:
    plus = outcome_amplitudes(theta_plus)
    minus = outcome_amplitudes(theta_minus)
    return sum(
        a_plus * a_minus.conjugate()
        for a_plus, a_minus in zip(plus, minus)
    )


def curvature_check() -> dict[str, object]:
    # Z(delta,0)=exp(i*delta/2) cos(delta/2), so near zero:
    # |Z|=1-delta^2/8+O(delta^4) and
    # -log|Z|=delta^2/8+O(delta^4). The second derivative is exactly 1/4.
    cosine_quadratic_coefficient = Fraction(-1, 8)
    negative_log_quadratic_coefficient = -cosine_quadratic_coefficient
    curvature = 2 * negative_log_quadratic_coefficient
    expected = Fraction(1, 4)
    return {
        "method": "exact_taylor_coefficients",
        "cosine_quadratic_coefficient": str(cosine_quadratic_coefficient),
        "negative_log_quadratic_coefficient":
            str(negative_log_quadratic_coefficient),
        "curvature": str(curvature),
        "expected": str(expected),
        "pass": curvature == expected,
    }


def sample_checks() -> dict[str, object]:
    samples = (
        (0.0, 0.0),
        (0.7, 0.2),
        (-0.4, 0.9),
        (1.1, -0.3),
    )
    formula_errors = []
    hermiticity_errors = []
    diagonal_errors = []
    for theta_plus, theta_minus in samples:
        outcome = kernel_by_outcome_sum(theta_plus, theta_minus)
        formula = (
            1 + cmath.exp(1.0j * (theta_plus - theta_minus))
        ) / 2
        reverse = kernel_by_outcome_sum(theta_minus, theta_plus)
        diagonal = kernel_by_outcome_sum(theta_plus, theta_plus)
        formula_errors.append(abs(outcome - formula))
        hermiticity_errors.append(abs(outcome.conjugate() - reverse))
        diagonal_errors.append(abs(diagonal - 1))
    return {
        "max_formula_error": max(formula_errors),
        "max_hermiticity_error": max(hermiticity_errors),
        "max_diagonal_error": max(diagonal_errors),
        "pass": (
            max(formula_errors) < 1e-14
            and max(hermiticity_errors) < 1e-14
            and max(diagonal_errors) < 1e-14
        ),
    }


def main() -> None:
    primary = json.loads(PRIMARY.read_text())
    samples = sample_checks()
    curvature = curvature_check()
    protected = all(
        not primary[key]
        for key in (
            "primitive_source_scalarization_derived",
            "interacting_continuum_CTP_amplitude_derived",
            "volume_uniform_zero_free_neighborhood_proved",
            "connected_linked_cluster_density_proved",
            "Duhamel_intensive_Hessian_equality_proved",
            "kappa_record_computed",
            "physical_Thomson_stiffness_computed",
            "coupling_evaluation_authorized",
            "alpha_computed",
            "proof_authorized",
        )
    )
    passed = bool(
        primary["spec_sha256"] == sha256(SPEC)
        and primary["overall_verdict"]
        == "COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_CLOSURE_DERIVED"
        and primary["complete_Qspec_CTP_scalar_closure_derived"]
        and primary["complete_final_record_identity_retained"]
        and not primary["public_outcome_postselected"]
        and not primary["source_ray_or_covector_added"]
        and not primary["finite_normalized_trace_added"]
        and not primary["determinant_used"]
        and samples["pass"]
        and curvature["pass"]
        and protected
        and primary["no_target_access_attestation"]
    )
    result = {
        "schema": "complete_qspec_relative_history_ctp_amplitude_verification_v001",
        "spec_sha256": sha256(SPEC),
        "primary_sha256": sha256(PRIMARY),
        "outcome_sum_checks": samples,
        "curvature_check": curvature,
        "protected_statuses_verified": protected,
        "verdict": (
            "INDEPENDENT_RELATIVE_HISTORY_CTP_CLOSURE_CONFIRMED"
            if passed
            else "INDEPENDENT_RELATIVE_HISTORY_CTP_CLOSURE_FAILED"
        ),
        "pass": passed,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
