#!/usr/bin/env python3
"""Independent numerical audit of the complete two-outcome comparator kernel.

No electromagnetic coupling or target value is used.
"""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "complete_one_cell_ctp_kernel_v001.json"


def amplitudes(theta: float) -> tuple[complex, complex]:
    phase = cmath.exp(1j * theta)
    return (1.0 + phase) / 2.0, (1.0 - phase) / 2.0


def complete_kernel(theta_plus: float, theta_minus: float) -> complex:
    plus_p, minus_p = amplitudes(theta_plus)
    plus_m, minus_m = amplitudes(theta_minus)
    return plus_p * plus_m.conjugate() + minus_p * minus_m.conjugate()


def analytic_kernel(theta_plus: float, theta_minus: float) -> complex:
    delta = theta_plus - theta_minus
    return (1.0 + cmath.exp(1j * delta)) / 2.0


def main() -> None:
    grid = tuple(-2.75 + 0.125 * index for index in range(45))
    completeness_error = 0.0
    formula_error = 0.0
    diagonal_error = 0.0
    hermiticity_error = 0.0
    fidelity_component_gap = 0.0

    for theta in grid:
        plus_amp, minus_amp = amplitudes(theta)
        completeness_error = max(
            completeness_error,
            abs(abs(plus_amp) ** 2 + abs(minus_amp) ** 2 - 1.0),
        )
        diagonal_error = max(
            diagonal_error,
            abs(complete_kernel(theta, theta) - 1.0),
        )

        survival_fidelity = abs(plus_amp) ** 2
        fidelity_component_gap = max(
            fidelity_component_gap,
            abs(complete_kernel(theta, theta).real - survival_fidelity),
        )

        for other in grid:
            computed = complete_kernel(theta, other)
            formula_error = max(
                formula_error,
                abs(computed - analytic_kernel(theta, other)),
            )
            hermiticity_error = max(
                hermiticity_error,
                abs(computed.conjugate() - complete_kernel(other, theta)),
            )

    tolerance = 5.0e-14
    checks = {
        "two_outcome_probabilities_are_complete": (
            completeness_error < tolerance
        ),
        "complete_kernel_matches_closed_form": formula_error < tolerance,
        "ctp_diagonal_is_normalized": diagonal_error < tolerance,
        "ctp_hermiticity_holds": hermiticity_error < tolerance,
        "survival_fidelity_is_not_complete_diagonal_kernel": (
            fidelity_component_gap > 1.0e-3
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_COMPLETE_CTP_KERNEL_FIDELITY_PARENT_ACTION_BLOCKED_ALPHA_FALSE"
        if not failed
        else "FAIL_COMPLETE_ONE_CELL_CTP_KERNEL_V001"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "max_errors": {
            "completeness": completeness_error,
            "closed_form": formula_error,
            "diagonal_normalization": diagonal_error,
            "hermiticity": hermiticity_error,
        },
        "minimum_demonstrated_fidelity_component_gap": (
            fidelity_component_gap
        ),
        "analytic_complete_kernel": (
            "I(theta_plus,theta_minus)="
            "(1+exp(i(theta_plus-theta_minus)))/2"
        ),
        "complete_kernel_on_diagonal": 1,
        "survival_fidelity_is_complete_kernel": False,
        "fidelity_weight_is_parent_ctp_action": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "executable_role": "NUMERICAL_CROSSCHECK_OF_SYMBOLIC_CTP_IDENTITY",
    }
    RESULT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(overall)
    print(f"max_completeness_error={completeness_error:.3e}")
    print(f"max_kernel_formula_error={formula_error:.3e}")
    print(f"max_diagonal_error={diagonal_error:.3e}")
    print("fidelity_weight_is_parent_ctp_action=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

