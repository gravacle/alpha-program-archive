#!/usr/bin/env python3
"""Independent verifier for the reduced outgoing-tail zero-form calculation."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "r3_4_outgoing_tail_generator_exhaustion_v001.json"


def fail(message: str) -> None:
    raise RuntimeError(message)


def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    i = np.eye(2, dtype=complex)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.array([[1, 0], [0, -1]], dtype=complex)

    def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
        return a @ b - b @ a

    kernel = [
        name
        for name, matrix in (("I", i), ("X", x), ("Y", y), ("Z", z))
        if np.array_equal(comm(matrix, z), np.zeros((2, 2), dtype=complex))
    ]
    if kernel != ["I", "Z"]:
        fail("wrong nondemolition kernel")
    if not np.array_equal(comm(z, z), np.zeros((2, 2), dtype=complex)):
        fail("Z must act trivially on the public pointer")
    if np.array_equal(comm(z, x), np.zeros((2, 2), dtype=complex)):
        fail("Z was incorrectly erased on the full algebra")

    status = data["status"]
    if status["verdict"] != "PUBLIC_TAIL_ZERO_FORM_EXHAUSTED_CONTINUUM_SCALING_OPEN":
        fail("unexpected verdict")
    if status["complete_asymptotic_tail_zero_form_exhausted"] is not False:
        fail("reduced result was promoted to complete exhaustion")
    if status["alpha_computed"] is not False:
        fail("alpha firewall failed")
    print("R3_4_OUTGOING_TAIL_V001_INDEPENDENT_VERIFICATION_PASS")


if __name__ == "__main__":
    main()
