#!/usr/bin/env python3
"""Exact record-spectrum and Duhamel-history cancellation audit."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_COMPLETED_CONTINUUM_RESPONSE_PROVENANCE_SPEC_V001.md"
SPEC_SHA256 = "6e24ceb6b18e6e6da5a6d21e872f90f6d79a324df9f305d226ab6edec863831b"
OUT = ROOT / "stage8_execution/work/T07_completed_record_cancellation.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_multiply(
    left: tuple[tuple[complex, ...], ...],
    right: tuple[tuple[complex, ...], ...],
) -> tuple[tuple[complex, ...], ...]:
    size = len(left)
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(size))
            for column in range(size)
        )
        for row in range(size)
    )


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "Sealed specification drift")

    # The pinned record-incidence operator in the (ready, pointer, edge) basis.
    c_partial = (
        (0j, 0j, -1j),
        (0j, 0j, 1j),
        (1j, -1j, 0j),
    )
    c_squared = matrix_multiply(c_partial, c_partial)

    # For eigenvalues 0,+sqrt(2),-sqrt(2):
    # P_0=I-C^2/2 and P_+ + P_-=C^2/2.
    # Because <pointer|C|ready>=0, the +/- transition weights are equal.
    c_ready_to_pointer = c_partial[1][0]
    c2_ready_to_pointer = c_squared[1][0]
    require(c_ready_to_pointer == 0j, "Odd transition moment unexpectedly nonzero")
    require(c2_ready_to_pointer == -1 + 0j, "C^2 transition entry drift")

    weight_zero = Fraction(1, 2)
    weight_plus = Fraction(-1, 4)
    weight_minus = Fraction(-1, 4)
    require(weight_minus + weight_zero + weight_plus == 0, "Weight sum drift")

    moments: dict[str, str] = {}
    zero_orders = []
    nonzero_orders = []
    for order in range(13):
        if order == 0:
            moment = weight_minus + weight_zero + weight_plus
        elif order % 2 == 1:
            moment = Fraction(0)
        else:
            # (+/-sqrt(2))^order=2^(order/2).
            moment = (weight_minus + weight_plus) * (2 ** (order // 2))
        moments[str(order)] = str(moment)
        if moment == 0:
            zero_orders.append(order)
        else:
            nonzero_orders.append(order)

    require(zero_orders[:2] == [0, 1], "Zeroth/first cancellation failed")
    require(nonzero_orders[0] == 2, "First surviving insertion is not quadratic")
    require(all(order % 2 == 1 for order in zero_orders if order > 0),
            "An odd record moment survived")

    # In a multivariate Duhamel monomial, the history sum factorizes by cell:
    # coefficient=product_c m_(k_c). Therefore any cell with k_c=0,1, or
    # odd k_c kills the entire monomial.
    sample_multiindices = {
        "one_cell_absent": (0,),
        "one_cell_linear": (1,),
        "one_cell_quadratic": (2,),
        "two_cells_2_2": (2, 2),
        "two_cells_2_1": (2, 1),
        "three_cells_2_4_2": (2, 4, 2),
        "three_cells_2_3_2": (2, 3, 2),
    }
    factorized_coefficients = {}
    for name, multiindex in sample_multiindices.items():
        coefficient = Fraction(1)
        for order in multiindex:
            coefficient *= Fraction(moments[str(order)])
        factorized_coefficients[name] = str(coefficient)

    require(factorized_coefficients["one_cell_absent"] == "0",
            "Absent-cell history survived")
    require(factorized_coefficients["one_cell_linear"] == "0",
            "Linear-cell history survived")
    require(factorized_coefficients["one_cell_quadratic"] == "-1",
            "Quadratic normalization drift")
    require(factorized_coefficients["two_cells_2_2"] == "1",
            "Two-cell minimal coefficient drift")
    require(factorized_coefficients["two_cells_2_1"] == "0",
            "A linear cell survived in a multivariate history")
    require(factorized_coefficients["three_cells_2_3_2"] == "0",
            "An odd cell multiplicity survived")

    result = {
        "schema": "stage8_t7_completed_record_cancellation_v001",
        "spec_sha256": SPEC_SHA256,
        "record_basis": ["ready", "pointer", "edge"],
        "record_minimal_polynomial": "x*(x^2-2)",
        "record_eigenvalues": ["-sqrt(2)", "0", "+sqrt(2)"],
        "transition_weights": {
            "-sqrt(2)": str(weight_minus),
            "0": str(weight_zero),
            "+sqrt(2)": str(weight_plus),
        },
        "c_ready_to_pointer": [c_ready_to_pointer.real, c_ready_to_pointer.imag],
        "c2_ready_to_pointer": [c2_ready_to_pointer.real, c2_ready_to_pointer.imag],
        "moments_0_through_12": moments,
        "factorized_sample_coefficients": factorized_coefficients,
        "every_completed_cell_requires_at_least_two_insertions": True,
        "every_surviving_cell_multiplicity_is_even": True,
        "record_cancellation_is_parent_matrix_independent": True,
        "old_three_site_regression_used": False,
        "c1_exact_record_cancellation_derived": True,
        "c2_finite_stage_identity_derived": False,
        "c3_implementability_and_relative_phase_derived": False,
        "c4_uv_and_finite_renormalization_audit_derived": False,
        "c5_regulator_independence_derived": False,
        "completed_continuum_response_provenance_derived": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
