#!/usr/bin/env python3
"""Independent verifier for the R3.4 incidence-continuum scaling result."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "r3_4_incidence_continuum_scaling_v001.json"


def fail(message: str) -> None:
    raise RuntimeError(message)


def block(d: np.ndarray) -> np.ndarray:
    result = np.zeros((4, 4), dtype=complex)
    result[0, 1:] = np.conjugate(d)
    result[1:, 0] = d
    return result


def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    k = np.array([0.4, -0.7, 1.2])
    continuum = block(1j * k)
    errors = []
    for a in (0.5, 0.25, 0.125, 0.0625):
        discrete = block((np.exp(1j * a * k) - 1.0) / a)
        errors.append(float(np.linalg.norm(discrete - continuum, 2)))
    if not all(errors[i + 1] < errors[i] for i in range(len(errors) - 1)):
        fail("independent symbol convergence failed")

    eigenvalues = np.linalg.eigvalsh(continuum)
    expected = np.array([-np.linalg.norm(k), 0.0, 0.0, np.linalg.norm(k)])
    if not np.allclose(eigenvalues, expected, atol=1.0e-12, rtol=0.0):
        fail("continuum incidence spectrum failed")

    status = data["status"]
    if status["operator_derived_positive_branch_root_measure_computed"] is not True:
        fail("free root measure was not retained")
    if status["physical_positive_energy_record_branch_selected"] is not False:
        fail("positive-energy record branch was silently promoted")
    if status["complete_outgoing_root_spectral_measure_derived"] is not False:
        fail("write-defect gap was erased")
    if data["root_measure"]["sharp_root_mean_energy_finite"] is not False:
        fail("sharp-root energy divergence was hidden")
    if status["alpha_computed"] is not False:
        fail("alpha firewall failed")
    print("R3_4_INCIDENCE_CONTINUUM_V001_INDEPENDENT_VERIFICATION_PASS")


if __name__ == "__main__":
    main()
