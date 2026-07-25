#!/usr/bin/env python3
"""Algebra audit for the primitive binary closure generator.

The script verifies the displayed two-state algebra only. It does not certify
the physical inputs or compute a coupling.
"""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def overlap(x: float) -> complex:
    return 0.5 * (1.0 + cmath.exp(-1j * x))


def main() -> None:
    first = math.pi
    roots = [(2 * n + 1) * math.pi for n in range(4)]
    residuals = [abs(overlap(root)) for root in roots]

    assert first == min(roots)
    assert max(residuals) < 1e-15
    assert abs(overlap(0.0) - 1.0) < 1e-15
    assert abs(overlap(0.5 * math.pi)) > 0.5

    out = {
        "status": "PASS_BINARY_CLOSURE_GENERATOR_ALGEBRA_ALPHA_FALSE",
        "first_positive_phase": first,
        "tested_odd_roots": roots,
        "max_root_residual": max(residuals),
        "source_mass_identified_with_record_gap": False,
        "alpha_computed": False,
        "scope": "two_state_algebra_only",
    }
    result_path = ROOT / "results" / "primitive_binary_closure_generator_v001.json"
    result_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
