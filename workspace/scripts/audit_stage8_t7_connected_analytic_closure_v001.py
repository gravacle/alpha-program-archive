#!/usr/bin/env python3
"""Audit the remaining Stage-8 T7 connected analytic obligations."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_CONNECTED_ANALYTIC_CLOSURE_SPEC_V001.md"
SPEC_SEAL = ROOT / "STAGE8_T7_CONNECTED_ANALYTIC_CLOSURE_SPEC_V001.seal.sha256"
OUTPUT = ROOT / "stage8_execution" / "work" / "T07_connected_analytic_closure.json"

AUTHORITIES = {
    "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md":
        "e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6",
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md":
        "6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb",
    "FINITE_PARENT_ANALYTIC_AUTHORITY_V001.md":
        "f72b4714d5189279171c51f1efd25abb2883ab7bc91358d23ca4a5039a242a8c",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md":
        "345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb",
    "PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md":
        "532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb",
    "CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md":
        "b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30",
    "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md":
        "949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd",
    "STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_AUTHORITY_FABLE_V002.md":
        "ddb36cbfe4edfc2a0520e9ae58063295214c64afed5cad5a64e9f311826358f5",
    "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md":
        "aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a",
}

REQUIRED_OPEN_STATEMENTS = {
    "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md": (
        "connected_preparation_derived = false",
    ),
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md": (
        "source_inclusive_state_projective_limit_derived = false",
        "complete_parent_to_outgoing_GNS_map_derived = false",
    ),
    "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md": (
        "connected_linked_cluster_density_proved = false",
        "volume_uniform_zero_free_neighborhood_proved = false",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    spec_hash = SPEC_SEAL.read_text().split()[0]
    require(sha256(SPEC) == spec_hash, "Connected analytic spec seal mismatch")

    authority_rows = []
    for relative, expected in AUTHORITIES.items():
        path = ROOT / relative
        actual = sha256(path)
        authority_rows.append({
            "path": relative,
            "expected_sha256": expected,
            "actual_sha256": actual,
            "verified": actual == expected,
        })
    require(all(row["verified"] for row in authority_rows), "Authority drift")

    open_rows = []
    for relative, statements in REQUIRED_OPEN_STATEMENTS.items():
        text = (ROOT / relative).read_text()
        for statement in statements:
            open_rows.append({
                "path": relative,
                "statement": statement,
                "present": statement in text,
            })
    require(all(row["present"] for row in open_rows), "Open-status audit failed")

    # Exact algebraic identity used at every finite K. For an analytic scalar
    # a(s,t) with a_0 != 0:
    # d_s d_t[-log|a/a_0|]_0
    #   = -Re(a_st/a_0 - a_s a_t/a_0^2).
    finite_log_hessian_identity = {
        "amplitude": "a(s,t)",
        "baseline_condition": "a_0 != 0",
        "mixed_log_hessian":
            "-Re(a_st/a_0 - a_s*a_t/a_0^2)",
        "Duhamel_requirement":
            "a_s and a_st must be differentiated from the same propagator, "
            "preparation, and final boundary",
        "identity_exact": True,
        "identity_does_not_prove_uniform_limit": True,
    }

    # Hostile zero-free witness. The local generator is a sum of uniformly
    # bounded one-site terms, but a non-clustering GHZ preparation has
    # Z_N(A)=cos(N*tau*A), so its first zero approaches A=0 as 1/N.
    # This does not assert that the sealed parent prepares GHZ. It proves that
    # bounded locality and finite-volume analyticity alone cannot discharge C3.
    tau = math.pi / math.sqrt(2.0)
    volumes = (1, 2, 4, 8, 16, 32, 64)
    first_zeros = [math.pi / (2.0 * tau * n) for n in volumes]
    scaled = [zero * n for zero, n in zip(first_zeros, volumes)]
    expected_scaled = math.pi / (2.0 * tau)
    ghz_witness = {
        "preparation": "(|0...0>+|1...1>)/sqrt(2)",
        "local_generator": "sum_j Z_j",
        "local_term_norm": 1,
        "normalized_amplitude": "Z_N(A)=cos(N*tau_R*A)",
        "first_zero": "pi/(2*N*tau_R)",
        "volumes": list(volumes),
        "first_zeros": first_zeros,
        "scaled_first_zeros": scaled,
        "scaled_identity_error": max(
            abs(value - expected_scaled) for value in scaled
        ),
        "zero_approaches_origin": first_zeros[-1] < first_zeros[0],
        "purpose":
            "necessity witness for a derived uniform preparation/clustering "
            "bound; not a claim that the sealed parent is GHZ",
    }

    result = {
        "schema": "stage8-t7-connected-analytic-closure-v001",
        "custody": {
            "spec_sha256": sha256(SPEC),
            "spec_verified": True,
            "authority_rows": authority_rows,
        },
        "C1_connected_preparation": {
            "finite_parent_propagator_exists": True,
            "one_cell_complex_closure_derived": True,
            "disjoint_monoidality_derived": True,
            "connected_preparation_derived": False,
            "all_finite_K_baselines_nonzero_proved": False,
            "canonical_connected_scalar_closed": False,
            "pass": False,
        },
        "C2_finite_Duhamel": {
            "formal_finite_scalar_identity": finite_log_hessian_identity,
            "same_object_as_V011_G_L_proved": False,
            "pass": False,
        },
        "C3_uniform_zero_free": {
            "necessity_witness": ghz_witness,
            "uniform_parent_clustering_bound_proved": False,
            "tau_R_inside_certified_cluster_domain": False,
            "pass": False,
        },
        "C4_linked_cluster_density": {
            "local_return_decay_is_cumulant_bound": False,
            "uniform_absolute_cumulant_summability_proved": False,
            "subextensive_boundary_correction_proved": False,
            "pass": False,
        },
        "C5_thermodynamic_Duhamel": {
            "locally_uniform_first_two_derivative_convergence_proved": False,
            "limit_derivative_interchange_proved": False,
            "pass": False,
        },
        "open_status_rows": open_rows,
        "target_value_used": False,
        "new_principle_adopted": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "kappa_record_computed": False,
        "physical_charged_amplitude_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "verdict": "T7_CONNECTED_PREPARATION_BLOCKED",
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
