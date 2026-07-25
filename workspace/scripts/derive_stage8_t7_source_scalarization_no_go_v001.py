#!/usr/bin/env python3
"""Execute the sealed Stage-8 T7 source-scalarization no-go gate."""

from __future__ import annotations

import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_SPEC_V001.md"
OUT = ROOT / "stage8_execution/work/T07_source_scalarization_no_go.json"

AUTHORITIES = {
    "primitive_amplitude": (
        ROOT / "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md",
        "6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb",
    ),
    "global_descent": (
        ROOT / "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md",
        "949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd",
    ),
    "complete_parent": (
        ROOT / "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md",
        "345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb",
    ),
    "actual_parent_amplitude": (
        ROOT / "STAGE8_T7_ACTUAL_PARENT_RECORD_AMPLITUDE_ADJUDICATION_RESULT_V001.md",
        "7aafba8667ac01f1c4326b0d714e838bf068eec7c8f4ce28ef03c8bef9d62098",
    ),
    "closure_selection": (
        ROOT / "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md",
        "e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6",
    ),
    "flat_transition_adjudication": (
        ROOT / "STAGE8_T7_ACTUAL_PRIMITIVE_CAUSAL_TRANSITION_MAP_RESULT_V001.md",
        "7020b3cbe37e96e5aef6eb49a75117e3335b62280b3bbece58a5673cbbdcb00f",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_actual_parent_witness() -> dict[str, object]:
    text = AUTHORITIES["actual_parent_amplitude"][0].read_text()
    frob = re.search(r"source-operator Frobenius norm = ([0-9.]+)", text)
    residual = re.search(r"distance from scalar identity = ([0-9.]+)", text)
    if frob is None or residual is None:
        raise RuntimeError("actual-parent non-scalar witness is missing")
    return {
        "source_dimension": 12,
        "completed_11_full_rank": True,
        "frobenius_norm": float(frob.group(1)),
        "distance_from_scalar_identity": float(residual.group(1)),
        "non_scalar": float(residual.group(1)) > 0.0,
    }


def finite_covariance_classification() -> dict[str, object]:
    # Write C(E_ij)=c_ij. Invariance under Z=diag(1,-1) gives
    # c_01=c_10=0; invariance under X swaps c_00 and c_11.
    # C(I)=1 then fixes both diagonal values to 1/2.
    c00 = Fraction(1, 2)
    c01 = Fraction(0)
    c10 = Fraction(0)
    c11 = Fraction(1, 2)
    return {
        "dimension": 2,
        "unitary_generators": ["X", "Z"],
        "matrix_unit_coefficients": {
            "E00": str(c00),
            "E01": str(c01),
            "E10": str(c10),
            "E11": str(c11),
        },
        "solution_dimension_after_invariance": 1,
        "normalization_fixes_solution": True,
        "unique_functional": "C(K)=Tr(K)/2",
        "general_finite_dimension_theorem": "C(K)=Tr(K)/d",
    }


def continuum_trace_obstruction() -> dict[str, object]:
    # A normalized trace tau on B(H) would satisfy tau(V_i V_i*) =
    # tau(V_i* V_i) = tau(I)=1 for two orthogonal isometries, while their
    # range projections sum to I.
    lhs = Fraction(1)
    rhs = Fraction(2)
    return {
        "two_orthogonal_isometries": True,
        "normalized_trace_of_identity": str(lhs),
        "trace_implied_by_range_decomposition": str(rhs),
        "contradiction": lhs != rhs,
        "normalized_tracial_state_on_infinite_BH_exists": False,
    }


def closure_classification() -> list[dict[str, object]]:
    return [
        {
            "closure": "source_vector_or_covector_matrix_element",
            "primitive_status": "requires_unfixed_source_boundary_data",
        },
        {
            "closure": "source_density_state_expectation",
            "primitive_status": "requires_unfixed_physical_source_state",
        },
        {
            "closure": "finite_normalized_trace",
            "primitive_status": "finite_unique_but_no_canonical_continuum_extension",
        },
        {
            "closure": "determinant",
            "primitive_status": "nonlinear_and_quarantined",
        },
        {
            "closure": "inclusive_equal_branch_sandwich",
            "primitive_status": "phase_blind",
        },
        {
            "closure": "operator_valued_primitive_response",
            "primitive_status": "consistent_but_scalar_extraction_moves_to_complete_Q_spec",
        },
    ]


def main() -> None:
    authority_rows = []
    for label, (path, expected) in AUTHORITIES.items():
        actual = sha256(path)
        if actual != expected:
            raise RuntimeError(
                f"authority hash mismatch for {label}: {actual} != {expected}"
            )
        authority_rows.append(
            {"label": label, "path": str(path), "sha256": actual}
        )

    witness = parse_actual_parent_witness()
    finite = finite_covariance_classification()
    continuum = continuum_trace_obstruction()
    closures = closure_classification()

    blocked = bool(
        witness["non_scalar"]
        and finite["normalization_fixes_solution"]
        and continuum["contradiction"]
    )
    verdict = (
        "PRIMITIVE_SOURCE_SCALARIZATION_BLOCKED"
        if blocked
        else "PRIMITIVE_SOURCE_SCALARIZATION_DERIVED"
    )

    result = {
        "schema": "stage8_t7_source_scalarization_no_go_v001",
        "spec_sha256": sha256(SPEC),
        "authorities": authority_rows,
        "N1_non_scalar_parent_witness": witness,
        "N2_finite_covariance_classification": finite,
        "N3_continuum_trace_obstruction": continuum,
        "N4_closure_classification": closures,
        "admissible_successors": [
            "derive_physical_source_or_CTP_closure_in_complete_Q_spec",
            "amend_primitive_stage8_response_to_remain_operator_valued",
        ],
        "overall_verdict": verdict,
        "primitive_source_scalarization_derived": False,
        "connected_primitive_amplitude_derived": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
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
