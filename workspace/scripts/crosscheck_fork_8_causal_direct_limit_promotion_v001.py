#!/usr/bin/env python3
"""Construction-lane crosscheck of the Fork-8 promotion result.

This is not one of the three independent Stage-7 reviews.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "results" / "fork_8_causal_direct_limit_promotion_v001.json"
RESULT = (
    ROOT / "results" / "fork_8_causal_direct_limit_promotion_crosscheck_v001.json"
)


def load(name: str) -> dict:
    return json.loads((ROOT / "results" / name).read_text())


def main() -> None:
    primary = json.loads(PRIMARY.read_text())
    architecture = load("causal_direct_limit_architecture_audit_v001.json")
    measure = load("r3_3_global_intrinsic_measure_classification_v001.json")
    parent = load("r3_4_complete_causal_superconnection_parent_v001.json")
    outgoing = load("r3_4_outgoing_record_gns_completion_v001.json")
    ray = load("causal_direct_limit_covector_ray_lift_v001.json")

    physical = set(architecture["covariance_selector"]["physical_class"])
    regulators = set(architecture["covariance_selector"]["regulator_classes"])
    effective = set(
        architecture["covariance_selector"]["effective_descriptions"]
    )
    architecture_partition = {
        "A1_causal_half_line",
        "A2_three_branch_causal_tree",
        "A3_three_dimensional_spatial_lattice",
        "A4_Lorentz_covariant_causal_complex_continuum",
        "A5_effective_environment_continuum",
    }

    checks = {
        "architecture_partition_is_complete_and_disjoint": (
            physical.isdisjoint(regulators)
            and physical.isdisjoint(effective)
            and regulators.isdisjoint(effective)
            and physical | regulators | effective == architecture_partition
        ),
        "A4_only_physical": physical
        == {"A4_Lorentz_covariant_causal_complex_continuum"},
        "intrinsic_measure_fixed": (
            measure["global_classification_pass"] is True
            and measure["uniform_flat_cell_measure_derived"] is True
        ),
        "tail_nonreturn_and_record_persistence_both_hold": (
            parent["free_tail"]["thresholded_return_for_every_L2_source_root"]
            is True
            and outgoing["all_record_restrictions_pass"] is True
        ),
        "outgoing_GNS_and_recoverability_hold": (
            outgoing["outgoing_record_GNS_derived"] is True
            and outgoing["recoverable_central_record_sequence_derived"] is True
            and outgoing["central_sequence"]["label_separation_pass"] is True
        ),
        "unassumed_direct_limit_consequence_holds": (
            ray["checks"]["unit_counting_vectors_have_nonzero_hilbert_limit"]
            is False
            and ray["checks"]["finite_product_states_are_inductive_compatible"]
            is True
        ),
        "primary_promotes_only_scoped_fork": (
            primary["fork_8_closed"] is True
            and primary["hypothesis_promoted_to_principle"] is True
            and primary["global_source_inclusive_state_limit_derived"] is False
            and primary["complete_parameter_free_Q_spec_frozen"] is False
            and primary["alpha_computed"] is False
            and primary["proof_authorized"] is False
        ),
    }
    result = {
        "review_independence": "CONSTRUCTION_LANE_CROSSCHECK_NOT_INDEPENDENT_REVIEW",
        "checks": checks,
        "crosscheck_pass": all(checks.values()),
        "alpha_computed": False,
        "proof_authorized": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
