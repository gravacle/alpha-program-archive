#!/usr/bin/env python3
"""Matrix audit for the adopted primitive controlled record write.

The audit verifies the finite matrix identities only. It does not derive the
adopted extension, the physical interval, or a coupling.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    identity = np.eye(2, dtype=complex)
    x_gate = np.array([[0, 1], [1, 0]], dtype=complex)
    p0 = np.diag([1, 0]).astype(complex)
    p1 = np.diag([0, 1]).astype(complex)

    u_write = np.kron(p0, identity) + np.kron(p1, x_gate)
    generator_integral = (np.pi / 2.0) * np.kron(p1, identity - x_gate)

    eigvals, eigvecs = np.linalg.eigh(generator_integral)
    u_from_generator = eigvecs @ np.diag(np.exp(-1j * eigvals)) @ eigvecs.conj().T

    ket00 = np.array([1, 0, 0, 0], dtype=complex)
    ket10 = np.array([0, 0, 1, 0], dtype=complex)
    ket11 = np.array([0, 0, 0, 1], dtype=complex)

    unitarity_defect = np.linalg.norm(u_write.conj().T @ u_write - np.eye(4))
    exponential_defect = np.linalg.norm(u_from_generator - u_write)
    write0_defect = np.linalg.norm(u_write @ ket00 - ket00)
    write1_defect = np.linalg.norm(u_write @ ket10 - ket11)

    assert unitarity_defect < 1e-14
    assert exponential_defect < 1e-14
    assert write0_defect < 1e-14
    assert write1_defect < 1e-14

    out = {
        "status": "PASS_ADOPTED_CONTROLLED_RECORD_WRITE_MATRIX_ALPHA_FALSE",
        "unitarity_defect": float(unitarity_defect),
        "principal_exponential_defect": float(exponential_defect),
        "write_zero_defect": float(write0_defect),
        "write_one_defect": float(write1_defect),
        "extension_derived_from_unitarity_alone": False,
        "field_history_control_projectors_derived": False,
        "alpha_computed": False,
        "scope": "adopted_finite_matrix_identity_only",
    }
    result_path = ROOT / "results" / "primitive_reversible_record_write_v001.json"
    result_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
