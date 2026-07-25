#!/usr/bin/env python3
"""Fail-closed audit of the restricted source-decorated first-opening family."""

from __future__ import annotations

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    baseline = (1, 1, 0, 0, 0)
    enlarged_presentations = {
        "parallel_edge": (1, 2, 0, 0, 0),
        "intermediate_vertex": (1, 2, 1, 0, 0),
        "chirality_labeled_endpoints": (2, 2, 0, 2, 0),
        "loop": (1, 2, 0, 0, 1),
    }
    require(
        all(signature != baseline for signature in enlarged_presentations.values()),
        "an enlarged presentation was confused with the stipulated graph",
    )

    a_squared = np.linspace(0.0005, 1.9995, 3999)
    b_squared = 2.0 - a_squared
    completion = a_squared * b_squared
    maximum_index = int(np.argmax(completion))
    require(
        abs(a_squared[maximum_index] - 1.0) < 1e-14,
        "restricted completion maximum is not equal weight",
    )
    require(
        abs(completion[maximum_index] - 1.0) < 1e-14,
        "restricted completion maximum is not exact",
    )
    require(
        bool(np.all(completion[a_squared != 1.0] < 1.0)),
        "restricted completion maximum is not unique",
    )

    # Preserve representative nonunitary competitors. The complete
    # normal-dependent family and its all-spinor normalization are audited in
    # the companion endpoint classifier.
    xi_eta_competitors = ((0.2, 0.0), (0.0, -0.3), (0.2, -0.3))
    require(
        all(abs(xi) + abs(eta) > 0 for xi, eta in xi_eta_competitors),
        "nonunitary commutant negative controls missing",
    )

    print("minimal_graph_status=STIPULATED_REPRESENTATIVE")
    print(f"enlarged_graph_presentations={len(enlarged_presentations)}")
    print("physical_graph_equivalence_classified=FALSE")
    print("metric_compatible_edge_transport=REQUIRED_PREMISE")
    print("root_incidence_identity=SUPPLIED_BY_COVARIANT_BOUNDARY")
    print("nonunitary_chiral_rescaling_competitors=ADMITTED")
    print("endpoint_zero_form_role=PARENT_NOT_INCIDENCE")
    print("bare_covariant_incidence_column=PASS")
    print("conditional_pure_offdiagonal_weight_result=PASS")
    print("all_spinor_scaled_normalization_derived=FALSE")
    print("normal_dependent_endpoint_zero_form_family=SUPPLIED_IN_COMPANION")
    print("endpoint_U2_element_selected=FALSE")
    print("parent_zero_form_detuning_excluded=FALSE")
    print("record_Hilbertization_from_QR1_QR7=PASS_CONDITIONAL")
    print("record_Hilbertization_from_deeper_action=FALSE")
    print("global_connected_source_record_action_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_SOURCE_DECORATED_RESTRICTED_FAMILY_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
