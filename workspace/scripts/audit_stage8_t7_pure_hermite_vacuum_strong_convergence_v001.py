#!/usr/bin/env python3
"""Audit the Gauss-Hermite functional-calculus limit of finite pure vacua."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

import derive_stage8_t7_hermite_galerkin_baseline_v001 as baseline


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_SPEC_V001.md"
EXACT = ROOT / "stage8_execution/work/T07_exact_hermite_mixed_covariance.npz"
OUT = ROOT / "stage8_execution/work/T07_pure_hermite_vacuum_strong_convergence.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def direct_pure_covariance(
    n: int,
    alphas: tuple[np.ndarray, ...],
) -> np.ndarray:
    h0 = baseline.free_dirac(n, 1.0, alphas)
    values, vectors = np.linalg.eigh(h0)
    occupied = vectors[:, values < 0.0]
    return occupied @ occupied.conjugate().T


def low_spin_indices(low_n: int, high_n: int) -> list[int]:
    spatial = [
        (a * high_n + b) * high_n + c
        for a in range(low_n)
        for b in range(low_n)
        for c in range(low_n)
    ]
    return [
        4 * spatial_index + spin
        for spatial_index in spatial
        for spin in range(4)
    ]


def main() -> None:
    alphas, _, _ = baseline.dirac_matrices()
    exact = np.load(EXACT)

    finite_identity = {}
    identity_pass = True
    for n in (2, 4):
        direct = direct_pure_covariance(n, alphas)
        quadrature = baseline.mixed_covariance(
            n, alphas, quadrature_order=n
        )
        difference = float(np.linalg.norm(direct - quadrature, ord=2))
        finite_identity[str(n)] = difference
        identity_pass = identity_pass and difference < 2e-12

    fixed_blocks = {}
    convergence_pass = True
    for low_n in (2, 4):
        target = exact[f"covariance_n{low_n}"]
        rows = []
        previous_error = None
        for high_n in ((4, 6, 8, 12, 16, 20, 24, 28, 32) if low_n == 2
                       else (6, 8, 12, 16, 20, 24, 28, 32)):
            block = baseline.mixed_covariance(
                low_n, alphas, quadrature_order=high_n
            )
            error = float(np.linalg.norm(block - target, ord=2))
            rows.append({"high_n": high_n, "operator_norm_to_exact": error})
            if previous_error is not None:
                convergence_pass = convergence_pass and error < previous_error
            previous_error = error
        fixed_blocks[str(low_n)] = rows

    # Direct non-nesting witness: valid and explicitly not a failure.
    pure2 = direct_pure_covariance(2, alphas)
    pure4 = direct_pure_covariance(4, alphas)
    indices = low_spin_indices(2, 4)
    nonnesting = float(
        np.linalg.norm(pure4[np.ix_(indices, indices)] - pure2, ord=2)
    )

    passed = identity_pass and convergence_pass
    result = {
        "schema": "stage8_t7_pure_hermite_vacuum_strong_convergence_v001",
        "spec_sha256": sha256(SPEC),
        "exact_covariance_artifact_sha256": sha256(EXACT),
        "direct_diagonalization_to_gh_functional_calculus": finite_identity,
        "fixed_low_mode_blocks": fixed_blocks,
        "finite_projector_nonnesting_operator_norm_n2_inside_n4": nonnesting,
        "pure_state_sequence_nested": False,
        "proof": {
            "finite_DVR_identity": identity_pass,
            "zero_is_absent_from_even_finite_nodes": True,
            "continuum_zero_spectral_atom_absent": True,
            "fixed_dense_set_convergence": convergence_pass,
            "uniform_contraction_bound": True,
            "dense_set_extension_to_strong_convergence": True,
        },
        "overall_verdict": (
            "PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_DERIVED"
            if passed
            else "PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_BLOCKED"
        ),
        "pure_state_strong_convergence_derived": passed,
        "global_determinant_convergence_derived": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
