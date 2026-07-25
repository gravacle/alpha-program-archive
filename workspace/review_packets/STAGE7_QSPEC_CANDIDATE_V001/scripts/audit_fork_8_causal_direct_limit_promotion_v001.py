#!/usr/bin/env python3
"""Adjudicate the sealed Fork-8 promotion bar from pinned upstream results."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "FORK_8_CAUSAL_DIRECT_LIMIT_PROMOTION_SPEC_V001.md"
SPEC_SEAL = ROOT / "FORK_8_CAUSAL_DIRECT_LIMIT_PROMOTION_SPEC_V001.seal.sha256"
RESULT = ROOT / "results" / "fork_8_causal_direct_limit_promotion_v001.json"

PINNED_HASHES = {
    "CAUSAL_DIRECT_LIMIT_RECORD_HYPOTHESIS_V001.md": (
        "60c82b021a7f5ffcb514ae8c20f083a7b2c9b42872586922b1c0464c4822d73f"
    ),
    "NEEDS_THEORY_DECISION_V002.md": (
        "ee595048f542e91a9c06016fead93b7852453bf23016f048f51b79945bf800b2"
    ),
    "CAUSAL_DIRECT_LIMIT_ARCHITECTURE_ADJUDICATION_RESULT_V001.md": (
        "9be3f55fd527b9a857bdd4ea2298105e44a69e85db79b90772ecb30001aba022"
    ),
    "R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md": (
        "e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2"
    ),
    "R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_V001.seal.sha256": (
        "dcab767cf5d38548ae0fc4e30b3c674cc527082e398575907ce53efaae08e199"
    ),
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md": (
        "345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb"
    ),
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_V001.seal.sha256": (
        "e771a28a9c1e1c9f410a00dc2c407be3338fcdee06d31f50cbc8563d63e41029"
    ),
    "R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md": (
        "10909b5c21e73ecf655462339a27bd645b8d35e3ad11fb6f8cb204c601992995"
    ),
    "R3_4_OUTGOING_RECORD_GNS_COMPLETION_V001.seal.sha256": (
        "2e67781852e99e09b86912dc6a2238d4de85f57e2ea05589cd800eb65bcb5a95"
    ),
    "CAUSAL_DIRECT_LIMIT_COVECTOR_RAY_LIFT_RESULT_V001.md": (
        "7c81c625c41adae66e4c72f4b4e351507760bca74e68f555053fac87ae70c859"
    ),
    "CAUSAL_DIRECT_LIMIT_REDUNDANT_RECORD_RESULT_V001.md": (
        "3359960fb411eff8ac0360a8c052bfc4d00a6281bd151c390fa3addd3603d05a"
    ),
    "PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md": (
        "532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb"
    ),
    "CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md": (
        "b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30"
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(name: str) -> dict:
    return json.loads((ROOT / "results" / name).read_text())


def main() -> None:
    spec_hash = sha256(SPEC)
    specification_seal_matches = SPEC_SEAL.read_text().split()[0] == spec_hash
    authority_hashes = {}
    for name, expected in PINNED_HASHES.items():
        actual = sha256(ROOT / name)
        authority_hashes[name] = {
            "expected": expected,
            "actual": actual,
            "matches": actual == expected,
        }
    authority_hashes_match = all(
        row["matches"] for row in authority_hashes.values()
    )
    if not specification_seal_matches or not authority_hashes_match:
        raise RuntimeError("Fork-8 sealed-input verification failed")

    architecture = load_json("causal_direct_limit_architecture_audit_v001.json")
    measure = load_json(
        "r3_3_global_intrinsic_measure_classification_v001.json"
    )
    parent = load_json("r3_4_complete_causal_superconnection_parent_v001.json")
    outgoing = load_json("r3_4_outgoing_record_gns_completion_v001.json")
    outgoing_verify = load_json(
        "r3_4_outgoing_record_gns_completion_verification_v001.json"
    )
    ray = load_json("causal_direct_limit_covector_ray_lift_v001.json")

    selector = architecture["covariance_selector"]
    obligations = parent["analytic_obligations"]
    free_tail = parent["free_tail"]
    central = outgoing["central_sequence"]
    ray_checks = ray["checks"]

    expected_architectures = [
        "A1_causal_half_line",
        "A2_three_branch_causal_tree",
        "A3_three_dimensional_spatial_lattice",
        "A4_Lorentz_covariant_causal_complex_continuum",
        "A5_effective_environment_continuum",
    ]
    p1_checks = {
        "only_A4_is_physical_class": selector["physical_class"]
        == ["A4_Lorentz_covariant_causal_complex_continuum"],
        "A1_A3_are_regulators": selector["regulator_classes"]
        == expected_architectures[:3],
        "A5_is_effective": selector["effective_descriptions"]
        == [expected_architectures[4]],
        "uniform_intrinsic_measure_is_global": (
            measure["global_classification_pass"] is True
            and measure["uniform_flat_cell_measure_derived"] is True
        ),
        "completed_record_response_is_exhaustion_compatible": (
            outgoing["all_record_restrictions_pass"] is True
            and outgoing["dressed_net_stabilizes"] is True
            and outgoing["dressed_incoming_record_net_derived"] is True
        ),
    }
    p2_checks = {
        "outgoing_inductive_limit_state": (
            outgoing["outgoing_record_inductive_limit_state_derived"] is True
        ),
        "outgoing_GNS": outgoing["outgoing_record_GNS_derived"] is True,
        "record_generator_is_strongly_continuous_identity": (
            outgoing[
                "outgoing_record_identity_dynamics_strongly_continuous"
            ]
            is True
        ),
        "same_parent_supplies_free_tail": (
            obligations["same_parent_supplies_free_tail"] is True
            and obligations["same_parent_supplies_asymptotic_quasifree_state"]
            is True
        ),
        "source_tail_has_derived_AC_spectrum": (
            free_tail["source_spectrum_purely_absolutely_continuous"] is True
            and free_tail["source_point_spectrum_absent"] is True
        ),
    }
    p3_checks = {
        "thresholded_nonreturn_for_declared_source_class": (
            free_tail["thresholded_return_for_every_L2_source_root"] is True
        ),
        "completed_record_restrictions_are_exact": (
            outgoing["all_record_restrictions_pass"] is True
            and obligations["reduced_record_persistence_exact"] is True
        ),
        "nonreturn_and_persistence_are_distinct": (
            obligations["root_return_and_record_recoverability_kept_distinct"]
            is True
        ),
    }
    p4_checks = {
        "recoverable_central_sequence": (
            outgoing["recoverable_central_record_sequence_derived"] is True
            and central["bound_pass"] is True
        ),
        "public_labels_are_separated": central["label_separation_pass"] is True,
        "independent_numerical_route_agrees": (
            outgoing_verify["independent_verification_pass"] is True
        ),
    }
    p5_checks = {
        "cell_measure_and_envelope_are_fixed": (
            measure["uniform_flat_cell_measure_derived"] is True
            and parent["intrinsic_envelope"]["normalized"] is True
        ),
        "no_independent_descendant_coefficient": (
            parent["generated_descendants"]["independent_descendant_coefficient_used"]
            is False
        ),
        "state_and_tail_come_from_same_parent": (
            obligations["same_parent_supplies_asymptotic_quasifree_state"] is True
            and obligations["same_parent_supplies_free_tail"] is True
        ),
        "no_target_selected_architecture": (
            architecture["target_values_used"] is False
            and architecture["winner_or_ranking_emitted"] is False
        ),
        "all_construction_inputs_exclude_alpha": (
            measure["construction_uses_alpha"] is False
            and parent["construction_uses_alpha"] is False
            and outgoing["construction_uses_alpha"] is False
            and ray["construction_uses_alpha"] is False
        ),
    }
    p6_checks = {
        "nonzero_Hilbert_covector_limit_fails": (
            ray_checks["unit_counting_vectors_have_nonzero_hilbert_limit"]
            is False
            and ray_checks["averaged_counting_vectors_have_nonzero_hilbert_limit"]
            is False
        ),
        "quasilocal_state_and_central_sequence_survive": (
            ray_checks["finite_product_states_are_inductive_compatible"] is True
            and ray_checks["empirical_record_mean_is_central_sequence"] is True
            and ray_checks["labels_are_asymptotically_distinguished"] is True
        ),
        "incoming_record_net_is_source_dressed": (
            obligations["incoming_pullback_is_dressed_monomorphism"] is True
            and parent["finite_parent_regression"][
                "dressed_pointer_bare_algebra_distance"
            ]
            > 1e-3
        ),
    }
    p7_checks = {
        "all_five_architectures_reported_in_sealed_order": (
            architecture["architectures_reported_in_sealed_order"]
            == expected_architectures
        ),
        "no_winner_or_ranking": architecture["winner_or_ranking_emitted"] is False,
        "no_target_values": architecture["target_values_used"] is False,
    }

    rows = {
        "P1_physical_architecture_or_response_equivalent_class": p1_checks,
        "P2_direct_limit_and_self_adjoint_generator": p2_checks,
        "P3_thresholded_durability": p3_checks,
        "P4_recoverable_outgoing_labels": p4_checks,
        "P5_no_separate_spectral_or_architecture_knob": p5_checks,
        "P6_unassumed_architecture_sensitive_consequence": p6_checks,
        "P7_complete_reporting": p7_checks,
    }
    promotion_tests = {
        name: all(checks.values()) for name, checks in rows.items()
    }
    all_promotion_tests_pass = all(promotion_tests.values())

    if all_promotion_tests_pass:
        verdict = (
            "FORK_8_PROMOTED_TO_SCOPED_CAUSAL_DIRECT_LIMIT_RECORD_PRINCIPLE"
        )
    elif promotion_tests["P3_thresholded_durability"] and promotion_tests[
        "P4_recoverable_outgoing_labels"
    ]:
        verdict = "FORK_8_COMPONENTS_DERIVED_PROMOTION_BLOCKED"
    else:
        verdict = "FORK_8_REMAINS_HYPOTHESIS"

    result = {
        "schema": "fork-8-causal-direct-limit-promotion-v001",
        "specification_sha256": spec_hash,
        "specification_seal_matches": specification_seal_matches,
        "authority_hashes": authority_hashes,
        "authority_hashes_match": authority_hashes_match,
        "promotion_scope": (
            "ordinary_3_plus_1_flat_asymptotic_completed_record_branch"
        ),
        "promotion_rows": rows,
        "promotion_tests": promotion_tests,
        "all_promotion_tests_pass": all_promotion_tests_pass,
        "verdict": verdict,
        "fork_8_closed": all_promotion_tests_pass,
        "hypothesis_promoted_to_principle": all_promotion_tests_pass,
        "global_source_inclusive_state_limit_derived": False,
        "global_infinite_future_source_Moller_unitary_derived": False,
        "curved_nonstationary_extension_derived": False,
        "interacting_gauge_infraparticle_spectrum_derived": False,
        "absolute_charged_response_normalization_derived": False,
        "complete_parameter_free_Q_spec_frozen": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
