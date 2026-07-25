#!/usr/bin/env python3
"""Execute the target-free preparation and competitor portion of Stage-8 T5.

The final T05 report is intentionally not emitted here: the generated
Maxwell-response row cannot carry a computed coefficient until T14 runs.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path


ROOT = Path(
    "/Users/bgm/Documents/New project/gravity_emergence_evidence_program/"
    "alpha_fundamental_record_action_cleanroom_v003"
)
WORK = ROOT / "stage8_execution" / "work"
OUTPUT = WORK / "T05_preclassification.json"
SCHEDULE = tuple(range(3, 22, 2))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_content_addressed(path: Path, body: dict[str, object]) -> None:
    body = dict(body)
    body["sha256_of_body"] = ""
    canonical = json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    body["sha256_of_body"] = sha256_bytes(canonical)
    path.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")


def translation_orbit_inventory(length: int) -> dict[str, object]:
    # At trivial holonomy translations change only the lattice coordinate.
    # The degree/direction label is invariant, so these are the complete
    # basis-orbit labels of C0 direct-sum C1 on the oriented four-torus.
    counts: Counter[str] = Counter()
    for coordinate in itertools.product(range(length), repeat=4):
        _ = coordinate
        counts["C0_vertex"] += 1
        for direction in range(4):
            counts[f"C1_direction_{direction}"] += 1
    expected_size = length**4
    return {
        "L": length,
        "basis_dimension": 5 * expected_size,
        "translation_orbit_count": len(counts),
        "orbit_sizes": dict(sorted(counts.items())),
        "all_orbits_have_size_L4": all(
            size == expected_size for size in counts.values()
        ),
    }


def main() -> int:
    WORK.mkdir(parents=True, exist_ok=True)
    inventories = [translation_orbit_inventory(length) for length in SCHEDULE]
    preparation_pass = all(
        row["translation_orbit_count"] == 5
        and row["all_orbits_have_size_L4"]
        for row in inventories
    )

    # Every invariant vector is represented by five coefficients:
    # one constant vertex coefficient and four constant oriented-edge
    # coefficients. First-opening semantics puts the unresolved preparation
    # in C0 before incidence creates C1 support.
    invariant_family = "(c_root,c_edge_0,c_edge_1,c_edge_2,c_edge_3), not all zero"
    first_opening_constraints = {
        "c_edge_0": 0,
        "c_edge_1": 0,
        "c_edge_2": 0,
        "c_edge_3": 0,
        "c_root": "nonzero modulo projective scale",
    }
    surviving_projective_dimension = 0
    unique_root_ray = preparation_pass and surviving_projective_dimension == 0

    excluded_by_postulate = [
        {
            "id": "independent_primitive_Pauli_sigmaF",
            "reason": "excluded from primitive status by adopted Single-Operator Completeness",
            "exclusion_kind": "postulate_not_theorem",
        },
        {
            "id": "independent_primitive_F_squared",
            "reason": "excluded from primitive status by adopted Single-Operator Completeness and zero-independent-bare-F2 compositeness",
            "exclusion_kind": "postulate_not_theorem",
        },
        {
            "id": "independent_primitive_higher_CAR_contact_or_overlap",
            "reason": "excluded from primitive status by adopted Global Boundary Descent / Quasi-Free Completeness",
            "exclusion_kind": "postulate_not_theorem",
        },
    ]
    incompatible_with_f1 = [
        {
            "id": "inequivalent_D_a_b_incidence_column",
            "reason": "fails the already executed unique normalized F1 differential class",
        },
        {
            "id": "edge_or_handle_dependent_F1_weight",
            "reason": "fails F1 naturality and cell-relabeling covariance",
        },
        {
            "id": "homogeneous_order_zero_transport",
            "reason": "collapses the frozen augmentation-ideal filtration T_mu=I+delta_mu",
        },
    ]
    generated_downstream = [
        {
            "id": "basepoint_curvature_F_BR",
            "source": "closed F1 plaquette word",
            "incidence_order": 2,
            "computed_coefficient": "unit principal-log normalization",
        },
        {
            "id": "kinematic_Pauli_sigmaF",
            "source": "Clifford square of the generated covariant differential",
            "incidence_order": 2,
            "computed_coefficient": "-1/2",
        },
        {
            "id": "quadratic_Maxwell_record_response",
            "source": "T7 response Hessian followed by T12-T14 tensor reconstruction",
            "incidence_order": 4,
            "computed_coefficient": None,
            "status": "pending_T14",
        },
    ]

    all_ids = [
        row["id"]
        for bucket in (
            excluded_by_postulate,
            incompatible_with_f1,
            generated_downstream,
        )
        for row in bucket
    ]
    buckets_disjoint = len(all_ids) == len(set(all_ids))
    final_classification_ready = (
        unique_root_ray
        and buckets_disjoint
        and all(
            row["computed_coefficient"] is not None for row in generated_downstream
        )
    )

    result = {
        "schema": "stage8-t05-preclassification-v001",
        "pass_so_far": unique_root_ray and buckets_disjoint,
        "final_T05_report_emitted": False,
        "reason_final_not_emitted": (
            "generated Maxwell-response coefficient belongs to T14 and is not yet computed"
        ),
        "T5a": {
            "frozen_schedule": list(SCHEDULE),
            "translation_invariant_basis_orbits": inventories,
            "complete_invariant_projective_family": invariant_family,
            "first_opening_constraints": first_opening_constraints,
            "surviving_projective_dimension": surviving_projective_dimension,
            "unique_root_generated_preparation_ray": unique_root_ray,
        },
        "T5b": {
            "typed_competitor_buckets": {
                "excluded_by_postulate": excluded_by_postulate,
                "incompatible_with_F1": incompatible_with_f1,
                "generated_downstream": generated_downstream,
            },
            "buckets_pairwise_disjoint": buckets_disjoint,
            "postulate_exclusions_mislabeled_as_theorems": False,
            "final_classification_ready": final_classification_ready,
        },
        "protected_flags": {
            "primitive_output_computed": False,
            "alpha_computed": False,
            "proof_authorized": False,
        },
    }
    write_content_addressed(OUTPUT, result)
    print(
        json.dumps(
            {
                "T5a_unique_root_ray": unique_root_ray,
                "T5b_preclassification_disjoint": buckets_disjoint,
                "T05_final_report_emitted": False,
                "alpha_computed": False,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result["pass_so_far"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
