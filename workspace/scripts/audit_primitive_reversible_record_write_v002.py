#!/usr/bin/env python3
"""Audit only the selected controlled-X finite matrix identities."""

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
    selected_logarithm = (np.pi / 2.0) * np.kron(p1, identity - x_gate)

    eigvals, eigvecs = np.linalg.eigh(selected_logarithm)
    u_selected = eigvecs @ np.diag(np.exp(-1j * eigvals)) @ eigvecs.conj().T
    u_negative = eigvecs @ np.diag(np.exp(+1j * eigvals)) @ eigvecs.conj().T

    ket00 = np.array([1, 0, 0, 0], dtype=complex)
    ket10 = np.array([0, 0, 1, 0], dtype=complex)
    ket11 = np.array([0, 0, 0, 1], dtype=complex)

    unitarity_defect = np.linalg.norm(u_write.conj().T @ u_write - np.eye(4))
    selected_logarithm_defect = np.linalg.norm(u_selected - u_write)
    sign_nonuniqueness_defect = np.linalg.norm(u_negative - u_write)
    write0_defect = np.linalg.norm(u_write @ ket00 - ket00)
    write1_defect = np.linalg.norm(u_write @ ket10 - ket11)

    assert unitarity_defect < 1e-14
    assert selected_logarithm_defect < 1e-14
    assert sign_nonuniqueness_defect < 1e-14
    assert write0_defect < 1e-14
    assert write1_defect < 1e-14

    out = {
        "status": "PASS_SELECTED_CONTROLLED_X_MATRIX_IDENTITIES_ONLY_PHYSICAL_CLAIMS_BLOCKED",
        "unitarity_defect": float(unitarity_defect),
        "selected_logarithm_exponential_defect": float(
            selected_logarithm_defect
        ),
        "opposite_sign_logarithm_exponential_defect": float(
            sign_nonuniqueness_defect
        ),
        "write_zero_defect": float(write0_defect),
        "write_one_defect": float(write1_defect),
        "standard_principal_matrix_log_exists": False,
        "controlled_x_extension_unique": False,
        "durable_record_established": False,
        "candidate_is_active_Level_1_postulate": False,
        "alpha_computed": False,
        "scope": "selected_finite_matrix_identities_only",
    }
    result_path = ROOT / "results" / "primitive_reversible_record_write_v002.json"
    result_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
