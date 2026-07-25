#!/usr/bin/env python3
"""Audit the conditional two-state orthogonalization algebra.

This script explicitly tests general populations. It does not certify a
durable-record condition or a physical generator.
"""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def overlap(p: float, x: float) -> complex:
    return p + (1.0 - p) * cmath.exp(-1j * x)


def main() -> None:
    populations = [0.1, 0.25, 0.5, 0.75, 0.9]
    phase_samples = 200_001
    rows = []

    for p in populations:
        minimum = min(
            abs(overlap(p, 2.0 * math.pi * j / (phase_samples - 1)))
            for j in range(phase_samples)
        )
        analytic_minimum = abs(2.0 * p - 1.0)
        rows.append(
            {
                "p": p,
                "numerical_minimum": minimum,
                "analytic_minimum": analytic_minimum,
                "orthogonalization_exists": analytic_minimum == 0.0,
            }
        )
        assert abs(minimum - analytic_minimum) < 1e-12

    balanced = next(row for row in rows if row["p"] == 0.5)
    unbalanced = [row for row in rows if row["p"] != 0.5]
    assert balanced["orthogonalization_exists"] is True
    assert all(row["orthogonalization_exists"] is False for row in unbalanced)

    out = {
        "status": "PASS_CONDITIONAL_BALANCED_ORTHOGONALIZATION_ALGEBRA",
        "population_rows": rows,
        "balanced_calibration_derived": False,
        "durable_record_condition_established": False,
        "physical_record_generator_derived": False,
        "alpha_computed": False,
        "scope": "conditional_autocorrelation_algebra_only",
    }
    result_path = ROOT / "results" / "primitive_binary_closure_generator_v002.json"
    result_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
