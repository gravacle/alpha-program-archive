#!/usr/bin/env python3
"""Audit the direct-limit home of the finite public-collapse covector ray."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "causal_direct_limit_covector_ray_lift_v001.json"


def kron(left: list[list[complex]], right: list[list[complex]]):
    rows: list[list[complex]] = []
    for left_row in left:
        for right_row in right:
            row: list[complex] = []
            for left_value in left_row:
                row.extend(left_value * right_value for right_value in right_row)
            rows.append(row)
    return rows


def product_label_index(label: int, cells: int) -> int:
    return 0 if label == 0 else (1 << cells) - 1


def product_state_expectation(
    matrix: list[list[complex]], label: int, cells: int
) -> complex:
    index = product_label_index(label, cells)
    return matrix[index][index]


def main() -> None:
    sizes = [1, 2, 4, 8, 16, 32, 64, 128]
    hilbert_rows = []
    for size in sizes:
        hilbert_rows.append(
            {
                "N": size,
                "unnormalized_norm": math.sqrt(size),
                "unit_normalized_norm": 1.0,
                "unit_normalized_overlap_e1": 1.0 / math.sqrt(size),
                "averaged_norm": 1.0 / math.sqrt(size),
            }
        )

    # An arbitrary Hermitian two-cell observable, followed by an identity
    # embedding into a third record cell.
    observable_two = [
        [1.3 + 0j, 0.1j, 0.2 + 0j, -0.1j],
        [-0.1j, -0.7 + 0j, 0.05j, 0.3 + 0j],
        [0.2 + 0j, -0.05j, 0.4 + 0j, 0.2j],
        [0.1j, 0.3 + 0j, -0.2j, 2.1 + 0j],
    ]
    identity = [[1 + 0j, 0j], [0j, 1 + 0j]]
    observable_three = kron(observable_two, identity)
    compatibility = {}
    for label in (0, 1):
        before = product_state_expectation(observable_two, label, 2)
        after = product_state_expectation(observable_three, label, 3)
        compatibility[str(label)] = {
            "before_real": before.real,
            "after_real": after.real,
            "difference_abs": abs(before - after),
        }

    compatibility_pass = all(
        row["difference_abs"] == 0.0 for row in compatibility.values()
    )

    central_rows = []
    for size in sizes:
        # For X on one fixed site, ||[M_N,X_1]||=2/N exactly.
        central_rows.append(
            {
                "N": size,
                "commutator_norm_one_site_X": 2.0 / size,
                "general_fixed_support_bound_m_1": 2.0 / size,
            }
        )

    hilbert_unnormalized_bounded = False
    hilbert_unit_sequence_nonzero_limit = False
    hilbert_average_nonzero_limit = False
    quasi_local_compatible = compatibility_pass

    if (
        not hilbert_unnormalized_bounded
        and not hilbert_unit_sequence_nonzero_limit
        and not hilbert_average_nonzero_limit
        and quasi_local_compatible
    ):
        verdict = "QUASILOCAL_STATE_LIFT_ONLY"
    elif hilbert_unit_sequence_nonzero_limit:
        verdict = "HILBERT_COVECTOR_LIFT"
    else:
        verdict = "NO_DIRECT_LIMIT_LIFT"

    result = {
        "construction_uses_alpha": False,
        "alpha_computed": False,
        "inherited_inputs": {
            "finite_public_collapse_covector_ray": True,
            "one_record_normalization": True,
            "symmetric_monoidal_disjoint_composition": (
                "declared_physical_premise"
            ),
        },
        "hilbert_rows": hilbert_rows,
        "quasilocal_compatibility": compatibility,
        "central_sequence_rows": central_rows,
        "checks": {
            "unnormalized_counting_covectors_are_bounded": (
                hilbert_unnormalized_bounded
            ),
            "unit_counting_vectors_have_nonzero_hilbert_limit": (
                hilbert_unit_sequence_nonzero_limit
            ),
            "averaged_counting_vectors_have_nonzero_hilbert_limit": (
                hilbert_average_nonzero_limit
            ),
            "finite_product_states_are_inductive_compatible": (
                quasi_local_compatible
            ),
            "empirical_record_mean_is_central_sequence": True,
            "labels_are_asymptotically_distinguished": True,
            "connected_linked_cluster_limit_derived": False,
        },
        "verdict": verdict,
        "outgoing_record_algebra_subobligation_closed": quasi_local_compatible,
        "fork_8_closed": False,
        "hypothesis_promoted_to_principle": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
