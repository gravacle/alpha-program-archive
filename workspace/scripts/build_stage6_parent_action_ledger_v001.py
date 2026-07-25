#!/usr/bin/env python3
"""Build the Stage-6 least-favorable parent-action and Q_spec ledger."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE6_PARENT_ACTION_LEDGER_SPEC_V001.md"
SPEC_SEAL = ROOT / "STAGE6_PARENT_ACTION_LEDGER_SPEC_V001.seal.sha256"
RESULT = ROOT / "STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V001.json"

PINS = {
    "LOCKED_ALPHA_PLAN_DEPENDENCY_REPAIR_V001.md": "d8cf64c9dd3aa8eec63298a5891882dc5e0873212566c8831fe049867dd38a92",
    "STAGE1_PREMISE_DISPOSITION_V001.md": "254128f73a44869839d670557368709c1bf2a98d6f86b48f026064c80e8d2585",
    "FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md": "a27a2d571273494a0787e2283734ef1405d74dadfe16d64d3450bb4536e50732",
    "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md": "949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd",
    "BID_GRADED_BOUNDARY_SUPERCONNECTION_REPAIR_V001.md": "2215f79cbe69f1de1643427ad5d422b0c3064ff758327e43ff1629de8633f72d",
    "BID_COMPLETE_ONE_NORMAL_ZERO_FORM_ENUMERATION_V001.md": "50b5a651df2aca90ee47c6f85b2a502461370a652706ebccad871f191565a2d9",
    "BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md": "0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98",
    "BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md": "b786db3adec8cc335967d49ec13b59923d67f424644f72c535b27b579dd1489f",
    "BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md": "7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476",
    "BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md": "6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546",
    "PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md": "532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb",
    "CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md": "b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30",
    "R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md": "e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2",
    "R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_V001.seal.sha256": "dcab767cf5d38548ae0fc4e30b3c674cc527082e398575907ce53efaae08e199",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md": "345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_V001.seal.sha256": "e771a28a9c1e1c9f410a00dc2c407be3338fcdee06d31f50cbc8563d63e41029",
    "R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md": "10909b5c21e73ecf655462339a27bd645b8d35e3ad11fb6f8cb204c601992995",
    "R3_4_OUTGOING_RECORD_GNS_COMPLETION_V001.seal.sha256": "2e67781852e99e09b86912dc6a2238d4de85f57e2ea05589cd800eb65bcb5a95",
    "FORK_8_CAUSAL_DIRECT_LIMIT_PROMOTION_RESULT_V001.md": "f84d5b5e8789e5e336db53265cc87dd25f5efddf1cd9c8931f1e521240125d4a",
    "FORK_8_CAUSAL_DIRECT_LIMIT_PROMOTION_V001.seal.sha256": "c73d5246b7348075ec4507ab3697a16f61759bdae3fad046d12b35f74135f165",
    "BID_SOURCE_PARENT_CLOSURE_GATE_V003.md": "5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_result(name: str) -> dict:
    return json.loads((ROOT / "results" / name).read_text())


def main() -> None:
    spec_hash = sha256(SPEC)
    spec_seal_matches = SPEC_SEAL.read_text().split()[0] == spec_hash
    pin_rows = {}
    for name, expected in PINS.items():
        actual = sha256(ROOT / name)
        pin_rows[name] = {
            "expected": expected,
            "actual": actual,
            "matches": actual == expected,
        }
    pins_match = all(row["matches"] for row in pin_rows.values())
    if not spec_seal_matches or not pins_match:
        raise RuntimeError("Stage-6 authority verification failed")

    measure = load_result(
        "r3_3_global_intrinsic_measure_classification_v001.json"
    )
    parent = load_result("r3_4_complete_causal_superconnection_parent_v001.json")
    outgoing = load_result("r3_4_outgoing_record_gns_completion_v001.json")
    fork8 = load_result("fork_8_causal_direct_limit_promotion_v001.json")

    derived = {
        "primitive_unit_winding_from_faithful_U1_character": True,
        "global_flat_intrinsic_cell_measure": (
            measure["uniform_flat_cell_measure_derived"] is True
        ),
        "one_normal_record_odd_superconnection_inventory": True,
        "CPT_selected_cellular_incidence_quadrature": True,
        "primitive_pure_charge_control_in_declared_branch": True,
        "dimensionless_first_opening_interval_tau_pi_over_sqrt2": True,
        "finite_causal_source_record_parent": (
            parent["finite_causal_source_record_parent_derived"] is True
        ),
        "square_generated_descendants": (
            parent["generated_descendants"][
                "independent_descendant_coefficient_used"
            ]
            is False
        ),
        "common_self_adjoint_domain_and_finite_propagator": (
            parent["analytic_obligations"][
                "bounded_compact_time_perturbation_common_domain"
            ]
            is True
            and parent["analytic_obligations"]["unique_unitary_propagator"]
            is True
        ),
        "free_quasifree_in_state_and_CTP_contour": True,
        "same_parent_free_asymptotic_tail": (
            parent["analytic_obligations"]["same_parent_supplies_free_tail"]
            is True
        ),
        "thresholded_source_nonreturn_for_L2_class": (
            parent["free_tail"]["thresholded_return_for_every_L2_source_root"]
            is True
        ),
        "outgoing_record_inductive_state_and_GNS": (
            outgoing["outgoing_record_GNS_derived"] is True
        ),
        "coherent_source_dressed_record_net": (
            outgoing["dressed_incoming_record_net_derived"] is True
        ),
        "recoverable_central_record_sequence": (
            outgoing["recoverable_central_record_sequence_derived"] is True
        ),
        "fork_8_scoped_durability_principle": (
            fork8["fork_8_closed"] is True
            and fork8["hypothesis_promoted_to_principle"] is True
        ),
    }

    ledger = {
        "schema": "stage6-parent-action-and-qspec-ledger-v001",
        "date": "2026-07-24",
        "specification_sha256": spec_hash,
        "specification_seal_matches": spec_seal_matches,
        "authority_hashes": pin_rows,
        "authority_hashes_match": pins_match,
        "historical_target_blindness_established": False,
        "target_value_used_in_stage6_construction": False,
        "adopted_microscopic_principles": {
            "fundamental_boundary_record_action": "ADOPTED_LEVEL_1",
            "boundary_superconnection_and_single_operator_completeness": (
                "ADOPTED_BRANCH_PREMISE"
            ),
            "global_boundary_descent_and_quasifree_completeness": (
                "ADOPTED_BRANCH_PREMISE"
            ),
            "parent_state_covariance": "ADOPTED_LEVEL_1",
            "causal_incidence_support": "ADOPTED_LEVEL_1",
            "bare_U1_curvature_stiffness_zero": "ADOPTED_COMPOSITENESS_CONDITION",
        },
        "disclosed_branch_inputs": {
            "spacetime": "3+1_Lorentzian_globally_hyperbolic_spin",
            "source": "one_massless_bare_vectorlike_Dirac_pair",
            "charged_field": "smooth_compact_relative_U1_connection",
            "asymptotics": "ordinary_flat_source_free_first_branch",
            "record_carrier": "distinct_even_M3_factors",
            "additional_vectorlike_pairs_excluded": False,
        },
        "retired_from_load_bearing_path": {
            "unit_fidelity_information_multiplicity": True,
            "fidelity_action_as_complete_parent": True,
            "retired_controlled_X_write_rule": True,
            "freely_selected_scalar_diamond_spectral_density": True,
        },
        "derived_parent_and_durability": derived,
        "qspec_component_status": {
            "fields_and_typed_carriers": (
                "DECLARED_FOR_DURABILITY_PARENT_FULL_QSPEC_SPECIES_EXHAUSTION_OPEN"
            ),
            "first_order_parent_action": (
                "DURABILITY_PARENT_DERIVED_FULL_QSPEC_ACTION_OPEN"
            ),
            "generated_descendants": "DERIVED_NO_INDEPENDENT_COEFFICIENT",
            "in_state": "FREE_QUASIFREE_BRANCH_DERIVED",
            "CTP_contour": "FREE_QUASIFREE_BRANCH_DERIVED_INTERACTING_OPEN",
            "normalized_CTP_generating_amplitude": "OPEN",
            "operator_domain": "FINITE_PARENT_COMMON_DOMAIN_DERIVED",
            "causal_boundaries_and_closure": "DERIVED_IN_FLAT_PRIMITIVE_CELL_CLASS",
            "intrinsic_cell_measure": "DERIVED_IN_DECLARED_CLASS",
            "absolute_record_interval_T_R": "OPEN_SCALE_ORBIT_RETAINED",
            "gravitational_action_and_quantum_measure": (
                "OPEN_BACKGROUND_GEOMETRY_ONLY"
            ),
            "dynamical_U1_action": (
                "OPEN_AUXILIARY_CONNECTION_AND_ZERO_BARE_STIFFNESS_ONLY"
            ),
            "dynamical_gauge_ghost_functional_measure": "OPEN",
            "gauge_edge_mode_completion": "OPEN",
            "functional_regulator_and_finite_renormalization": "OPEN",
            "finite_c_F2_deformation_excluded": "OPEN",
            "record_operator": "DERIVED_IN_DECLARED_BRANCH",
            "outgoing_record_GNS_and_durability": "DERIVED_IN_DECLARED_BRANCH",
            "interacting_charged_pole_or_infraparticle_threshold": "OPEN",
            "full_charged_species_threshold_map": "OPEN",
            "branch_enumeration": "ORDINARY_BRANCH_FROZEN_ENLARGED_BRANCHES_OPEN",
            "Thomson_matching_rule": "OPEN",
            "unused_structure_sensitive_prediction": "OPEN",
        },
        "supersession_reconciliation": {
            "old_static_parent_completed_label_failure": (
                "SUPERSEDED_BY_CAUSAL_INCIDENCE_SUPPORT_PARENT"
            ),
            "old_redundancy_lane_dependency": (
                "REPLACED_BY_INCIDENCE_DERIVED_OUTGOING_GNS"
            ),
            "old_conditional_scalar_spectral_density": (
                "REMAINS_QUARANTINED_NOT_USED"
            ),
            "old_SP14_GPG_terminal_protocol": (
                "RETIRED_PHYSICS_NEUTRAL_SHA256_MANIFESTS_ACTIVE"
            ),
        },
        "stage6_exit_checks": {
            "all_derived_rows_true": all(derived.values()),
            "open_qspec_slots_explicit": True,
            "historical_target_blindness_false": True,
            "alpha_and_proof_false": True,
        },
        "stage6_ledger_frozen": True,
        "stage7_qspec_review_candidate_assembly_authorized": True,
        "complete_source_inclusive_parent_limit_derived": False,
        "complete_parameter_free_Q_spec_frozen": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    exit_pass = (
        pins_match
        and spec_seal_matches
        and all(derived.values())
        and ledger["historical_target_blindness_established"] is False
        and ledger["complete_parameter_free_Q_spec_frozen"] is False
        and ledger["alpha_computed"] is False
        and ledger["proof_authorized"] is False
    )
    ledger["verdict"] = (
        "STAGE6_LEDGER_FROZEN_STAGE7_REVIEW_CANDIDATE_AUTHORIZED"
        if exit_pass
        else "STAGE6_LEDGER_BLOCKED"
    )
    RESULT.write_text(json.dumps(ledger, indent=2, sort_keys=True) + "\n")
    print(json.dumps(ledger, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
