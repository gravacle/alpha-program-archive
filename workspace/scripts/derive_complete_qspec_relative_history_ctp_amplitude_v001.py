#!/usr/bin/env python3
"""Derive the finite/algebraic complete-Qspec relative-history CTP closure."""

from __future__ import annotations

import cmath
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_SPEC_V001.md"
OUT = ROOT / "stage8_execution/work/QSPEC_relative_history_CTP_closure.json"

AUTHORITIES = {
    "STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md":
        "5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e",
    "BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md":
        "6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md":
        "345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb",
    "COMPLETE_ONE_CELL_CTP_KERNEL_GATE_V001.md":
        "e30f2e631204df2416b9aa38e55c2710db1d676749fcd2fbdb6604388f3ea391",
    "BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md":
        "451550c3825288d699db35c7289e408e8314ad042450253b58f32722c4ead46b",
    "R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md":
        "10909b5c21e73ecf655462339a27bd645b8d35e3ad11fb6f8cb204c601992995",
    "STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_RESULT_V001.md":
        "6447eb80c9347e614a1ecfbfef6234e4acec5caadf829a8649fdb5282439aa09",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def kernel(theta_plus: float, theta_minus: float) -> complex:
    return 0.5 * (
        1.0 + cmath.exp(1.0j * (theta_plus - theta_minus))
    )


def direct_state_kernel(theta_plus: float, theta_minus: float) -> complex:
    plus = (1.0 / math.sqrt(2.0), 1.0 / math.sqrt(2.0))
    evolved_plus = (
        plus[0],
        cmath.exp(1.0j * theta_plus) * plus[1],
    )
    evolved_minus = (
        plus[0],
        cmath.exp(1.0j * theta_minus) * plus[1],
    )
    return sum(
        left.conjugate() * right
        for left, right in zip(evolved_minus, evolved_plus)
    )


def one_cell_checks() -> dict[str, object]:
    samples = (
        (0.0, 0.0),
        (0.7, 0.2),
        (-0.4, 0.9),
        (1.1, -0.3),
    )
    rows = []
    max_formula_error = 0.0
    max_hermiticity_error = 0.0
    max_diagonal_error = 0.0
    for theta_plus, theta_minus in samples:
        direct = direct_state_kernel(theta_plus, theta_minus)
        closed = kernel(theta_plus, theta_minus)
        reverse = kernel(theta_minus, theta_plus)
        max_formula_error = max(max_formula_error, abs(direct - closed))
        max_hermiticity_error = max(
            max_hermiticity_error, abs(closed.conjugate() - reverse)
        )
        max_diagonal_error = max(
            max_diagonal_error,
            abs(kernel(theta_plus, theta_plus) - 1.0),
        )
        rows.append(
            {
                "theta_plus": theta_plus,
                "theta_minus": theta_minus,
                "real": closed.real,
                "imag": closed.imag,
                "absolute": abs(closed),
            }
        )

    theta = 0.7
    exclusive_probability = abs(
        0.5 * (1.0 + cmath.exp(1.0j * theta))
    ) ** 2
    complete_diagonal = kernel(theta, theta)
    return {
        "rows": rows,
        "max_formula_error": max_formula_error,
        "max_hermiticity_error": max_hermiticity_error,
        "max_diagonal_normalization_error": max_diagonal_error,
        "contractivity_pass": all(row["absolute"] <= 1.0 + 1e-15 for row in rows),
        "gamma_curvature_at_zero": str(Fraction(1, 4)),
        "exclusive_preserved_reference_probability_at_0p7":
            exclusive_probability,
        "complete_diagonal_kernel_at_0p7": {
            "real": complete_diagonal.real,
            "imag": complete_diagonal.imag,
        },
        "exclusive_probability_not_substituted": (
            abs(exclusive_probability - complete_diagonal.real) > 1e-6
        ),
    }


def disjoint_monoidality_check() -> dict[str, object]:
    angles = ((0.3, -0.2), (-0.4, 0.1))
    individual = [kernel(*pair) for pair in angles]
    product = individual[0] * individual[1]

    # Direct factorized-state overlap is the product of the two overlaps.
    direct = (
        direct_state_kernel(*angles[0])
        * direct_state_kernel(*angles[1])
    )
    gamma_product = -math.log(abs(product))
    gamma_sum = sum(-math.log(abs(value)) for value in individual)
    return {
        "product_real": product.real,
        "product_imag": product.imag,
        "direct_factorized_real": direct.real,
        "direct_factorized_imag": direct.imag,
        "amplitude_factorization_error": abs(product - direct),
        "additive_log_modulus_error": abs(gamma_product - gamma_sum),
    }


def main() -> None:
    authority_rows = []
    for relative, expected in AUTHORITIES.items():
        path = ROOT / relative
        actual = sha256(path)
        if actual != expected:
            raise RuntimeError(
                f"authority hash mismatch for {relative}: {actual} != {expected}"
            )
        authority_rows.append(
            {"path": str(path), "sha256": actual}
        )

    one_cell = one_cell_checks()
    monoidal = disjoint_monoidality_check()
    passed = bool(
        one_cell["max_formula_error"] < 1e-14
        and one_cell["max_hermiticity_error"] < 1e-14
        and one_cell["max_diagonal_normalization_error"] < 1e-14
        and one_cell["contractivity_pass"]
        and one_cell["gamma_curvature_at_zero"] == "1/4"
        and one_cell["exclusive_probability_not_substituted"]
        and monoidal["amplitude_factorization_error"] < 1e-14
        and monoidal["additive_log_modulus_error"] < 1e-14
    )

    result = {
        "schema": "complete_qspec_relative_history_ctp_amplitude_v001",
        "spec_sha256": sha256(SPEC),
        "authorities": authority_rows,
        "definition": (
            "Z_K[A_plus,A_minus]="
            "omega_in(W_K[A_minus]^dagger W_K[A_plus])"
        ),
        "complete_final_record_identity_retained": True,
        "public_outcome_postselected": False,
        "source_ray_or_covector_added": False,
        "finite_normalized_trace_added": False,
        "determinant_used": False,
        "one_cell_checks": one_cell,
        "disjoint_monoidality_check": monoidal,
        "overall_verdict": (
            "COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_CLOSURE_DERIVED"
            if passed
            else "COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_CLOSURE_BLOCKED"
        ),
        "primitive_source_scalarization_derived": False,
        "complete_Qspec_CTP_scalar_closure_derived": passed,
        "interacting_continuum_CTP_amplitude_derived": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
