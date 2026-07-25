#!/usr/bin/env python3
"""Build the append-only Stage-6/7 ledger successor after external review."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE6_PARENT_ACTION_LEDGER_SPEC_V002.md"
SPEC_SEAL = ROOT / "STAGE6_PARENT_ACTION_LEDGER_SPEC_V002.seal.sha256"
PREDECESSOR = ROOT / "STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V001.json"
RESULT = ROOT / "STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.json"

PINS = {
    "STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V001.json": (
        "894755a50280a7cf2f50336774d80434c3fcd3366287248ec070e7eea3005318"
    ),
    "STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V001.md": (
        "32bbb4f7394e0dda6a486ec58f213680597d33bd072603999381686093d78ea1"
    ),
    "STAGE6_PARENT_ACTION_LEDGER_V001.seal.sha256": (
        "d393f9fa343296c45fc025c48f54b7245f20d51f07be71ae021898d14401e6f8"
    ),
    "STAGE7_QSPEC_REVIEW_CANDIDATE_V001.md": (
        "ac0b49e591bf40415bf98d29866a834b6b964634cb7fecf5e4184904550c3e81"
    ),
    "STAGE7_QSPEC_REVIEW_CANDIDATE_V001.seal.sha256": (
        "5f5e0606a193a06f100f07f622c58b33ca731c34c1815823fafc0f9c87c228cc"
    ),
    "STAGE7_INDEPENDENT_REVIEW_VERDICTS_V001.md": (
        "9bd3d2da8f8cb0b3fd34338f18f894e9f08aba900cea01c01fd24fc71eb81491"
    ),
    "STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.md": (
        "202f8d8db60046a8069b1cd8fcc38f505eb95fa29578e094e005f56e967c3a35"
    ),
    "R3_4_CONCURRENT_CELL_SCOPE_ERRATUM_V001.md": (
        "32b03d8ffaf03df25c4e85f8d6a483a8e9c1a7e1bdbc6d63cc450be5296da403"
    ),
    "CAUSAL_DIRECT_LIMIT_RECORD_PRINCIPLE_V002.md": (
        "7333204581ef3183665c9dd056d79f2caa073724e3566295ab888ccc5494c53a"
    ),
    "FINITE_PARENT_ANALYTIC_AUTHORITY_V001.md": (
        "f72b4714d5189279171c51f1efd25abb2883ab7bc91358d23ca4a5039a242a8c"
    ),
    "EM_DEPENDENCY_ORDER_FREEZE_V001.md": (
        "46052f5c4663d5e2284297b3d2f0ca46565e3c9440adcf2af88e7bf1e2bc6c4d"
    ),
}

NEW_SEALS = (
    "STAGE7_INDEPENDENT_REVIEW_VERDICTS_V001.seal.sha256",
    "STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.seal.sha256",
    "R3_4_CONCURRENT_CELL_SCOPE_ERRATUM_V001.seal.sha256",
    "CAUSAL_DIRECT_LIMIT_RECORD_PRINCIPLE_V002.seal.sha256",
    "FINITE_PARENT_ANALYTIC_AUTHORITY_V001.seal.sha256",
    "EM_DEPENDENCY_ORDER_FREEZE_V001.seal.sha256",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def seal_matches(path: Path) -> bool:
    fields = path.read_text().split()
    if len(fields) < 2:
        return False
    target = ROOT / fields[1]
    return target.is_file() and sha256(target) == fields[0]


def main() -> None:
    spec_hash = sha256(SPEC)
    spec_seal_matches = seal_matches(SPEC_SEAL)

    pin_rows = {}
    for name, expected in PINS.items():
        actual = sha256(ROOT / name)
        pin_rows[name] = {
            "expected": expected,
            "actual": actual,
            "matches": actual == expected,
        }
    pins_match = all(row["matches"] for row in pin_rows.values())
    new_seal_rows = {name: seal_matches(ROOT / name) for name in NEW_SEALS}
    new_seals_match = all(new_seal_rows.values())

    base = json.loads(PREDECESSOR.read_text())
    if not (
        spec_seal_matches
        and pins_match
        and new_seals_match
        and base["authority_hashes_match"] is True
        and base["alpha_computed"] is False
        and base["proof_authorized"] is False
    ):
        raise RuntimeError("Stage-6/7 v002 authority verification failed")

    ledger = copy.deepcopy(base)
    ledger.update(
        {
            "schema": "stage6-parent-action-and-qspec-ledger-v002",
            "date": "2026-07-24",
            "supersedes_status_only": (
                "STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V001"
            ),
            "specification_sha256": spec_hash,
            "specification_seal_matches": spec_seal_matches,
            "authority_hashes": pin_rows,
            "authority_hashes_match": pins_match,
            "successor_seals": new_seal_rows,
            "successor_seals_match": new_seals_match,
        }
    )

    ledger["adopted_microscopic_principles"] = {
        "fundamental_boundary_record_action": "ADOPTED_LEVEL_1",
        "parent_state_covariance": "ADOPTED_LEVEL_1",
        "causal_incidence_support": "ADOPTED_LEVEL_1",
        "boundary_superconnection_single_operator_completeness": (
            "ADOPTED_BRANCH_PREMISE"
        ),
        "global_boundary_descent_quasifree_completeness": (
            "ADOPTED_BRANCH_PREMISE"
        ),
        "zero_independent_bare_F2_compositeness": (
            "ADOPTED_COMPOSITENESS_CONDITION"
        ),
    }
    ledger["disclosed_branch_inputs"].update(
        {
            "stationary_quasifree_in_state": "DISCLOSED_BRANCH_STATE",
            "envelope_realization": (
                "ER_A_TIME_MARGINAL_AS_AMPLITUDE_DISCLOSED_BRANCH_PREMISE"
            ),
            "cell_complex": "CAUSALLY_SEQUENTIAL_PRIMITIVE_DIAMOND_EXHAUSTION",
        }
    )
    ledger["standard_theory_and_kinematic_inputs"] = {
        "Dirac_and_CAR_framework": "DISCLOSED_STANDARD_INPUT",
        "standard_CPT_structure": "DISCLOSED_STANDARD_INPUT",
        "spin_statistics_and_functional_analysis": "DISCLOSED_STANDARD_INPUT",
        "record_axioms": "DISCLOSED_KINEMATIC_INPUT",
    }

    derived = ledger["derived_parent_and_durability"]
    derived.pop("free_quasifree_in_state_and_CTP_contour", None)
    derived["free_CTP_contour_from_disclosed_stationary_quasifree_state"] = True
    derived["common_self_adjoint_domain_and_finite_propagator"] = True
    derived["smooth_to_sharp_under_L1_operator_norm_hypothesis"] = True
    derived["exact_record_compatibility_causally_sequential_only"] = True
    derived["fork_8_scoped_durability_principle"] = True

    ledger["explicitly_not_derived"] = {
        "stationary_quasifree_in_state": False,
        "spacetime_concurrent_exact_record_compatibility": False,
        "spacelike_disjoint_write_commutation": False,
        "spacelike_swap_independence": False,
        "source_inclusive_state_projective_limit": False,
        "infinite_future_source_Moller_limit": False,
        "continuum_regulator_independence_of_source_limit": False,
    }

    status = ledger["qspec_component_status"]
    status.update(
        {
            "in_state": "DISCLOSED_STATIONARY_QUASIFREE_BRANCH_STATE",
            "CTP_contour": (
                "FREE_CONTOUR_DERIVED_FROM_DISCLOSED_STATE_INTERACTING_OPEN"
            ),
            "operator_domain": "FINITE_PARENT_COMMON_DOMAIN_DERIVED",
            "causal_boundaries_and_closure": (
                "DERIVED_FOR_CAUSALLY_SEQUENTIAL_PRIMITIVE_CELL_CLASS"
            ),
            "intrinsic_cell_measure": (
                "MEASURE_DERIVED_ENVELOPE_REALIZATION_ER_A_DISCLOSED"
            ),
            "admitted_finite_energy_excitation_class": (
                "DEFINED_PER_STATE_THRESHOLD_QUANTIFIERS"
            ),
            "admissible_cell_complex_and_packing_class": (
                "CAUSALLY_SEQUENTIAL_PACKING_NORMALIZATION_FORBIDDEN"
            ),
            "source_inclusive_state_projective_limit": "OPEN",
            "infinite_future_source_Moller_limit": "OPEN",
            "source_limit_continuum_regulator_independence": "OPEN",
            "intermediate_asymptotic_unitary_implementability": (
                "NOT_CLAIMED_OFF_DIAGONAL_NOT_HILBERT_SCHMIDT"
            ),
        }
    )

    ledger["stage7_independent_review"] = {
        "completed": True,
        "mathematical_operator": "PASS_WITH_CONDITIONS",
        "physical_QED": "PASS_WITH_CONDITIONS",
        "provenance_anti_circularity": "PASS_WITH_CONDITIONS",
        "unanimous": True,
        "fail_count": 0,
        "blocking_finding_count": 0,
    }
    ledger["stage7_review_conditions"] = {
        "C1_open_slots_and_scope_visible": True,
        "C2_concurrent_scope_erratum_landed": True,
        "C3_free_in_state_reclassified": True,
        "C4_premises_and_standard_inputs_visible": True,
        "C5_analytic_authority_corrected": True,
        "C6_representation_scope_visible": True,
        "C7_EM_dependency_order_frozen": True,
    }
    ledger["EM_dependency_order"] = [
        "dynamical_U1_action",
        "gauge_fixing_ghosts_edge_modes",
        "normalized_interacting_CTP_amplitude",
        "parent_derived_regulator_and_finite_renormalization",
        "polarization_transversality_and_photon_mass_exclusion",
        "Lorentz_and_packing_independent_renormalized_response",
        "interacting_charged_pole_or_infraparticle_threshold",
        "threshold_conditioned_Thomson_matching",
        "CISP_descendant_test_on_outgoing_public_records",
    ]

    ledger.update(
        {
            "stage7_independent_reviews_completed": True,
            "stage7_review_conditions_landed": True,
            "stage8_theorem_battery_authored": False,
            "stage8_cross_execution_ready": True,
            "stage8_cross_execution_completed": False,
            "complete_source_inclusive_parent_limit_derived": False,
            "complete_parameter_free_Q_spec_frozen": False,
            "physical_Thomson_stiffness_computed": False,
            "coupling_evaluation_authorized": False,
            "alpha_computed": False,
            "proof_authorized": False,
        }
    )

    conditions_landed = all(ledger["stage7_review_conditions"].values())
    derived_rows_true = all(derived.values())
    exit_pass = (
        spec_seal_matches
        and pins_match
        and new_seals_match
        and conditions_landed
        and derived_rows_true
        and ledger["historical_target_blindness_established"] is False
        and ledger["complete_source_inclusive_parent_limit_derived"] is False
        and ledger["complete_parameter_free_Q_spec_frozen"] is False
        and ledger["physical_Thomson_stiffness_computed"] is False
        and ledger["coupling_evaluation_authorized"] is False
        and ledger["alpha_computed"] is False
        and ledger["proof_authorized"] is False
    )
    ledger["stage6_exit_checks"] = {
        "predecessor_and_successor_authorities_verify": (
            pins_match and new_seals_match
        ),
        "all_current_derived_rows_true": derived_rows_true,
        "C1_through_C6_landed": all(
            ledger["stage7_review_conditions"][f"C{i}_{suffix}"]
            for i, suffix in (
                (1, "open_slots_and_scope_visible"),
                (2, "concurrent_scope_erratum_landed"),
                (3, "free_in_state_reclassified"),
                (4, "premises_and_standard_inputs_visible"),
                (5, "analytic_authority_corrected"),
                (6, "representation_scope_visible"),
            )
        ),
        "C7_dependency_order_frozen": (
            ledger["stage7_review_conditions"][
                "C7_EM_dependency_order_frozen"
            ]
        ),
        "alpha_and_proof_false": (
            ledger["alpha_computed"] is False
            and ledger["proof_authorized"] is False
        ),
    }
    ledger["verdict"] = (
        "STAGE7_CONDITIONS_LANDED_STAGE8_CROSS_EXECUTION_READY"
        if exit_pass
        else "STAGE7_CONDITION_IMPLEMENTATION_BLOCKED"
    )
    RESULT.write_text(json.dumps(ledger, indent=2, sort_keys=True) + "\n")
    print(json.dumps(ledger, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
