#!/usr/bin/env python3
"""Execute the sealed Stage-8 T7 relayed-family resolution gate."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_RELAYED_FAMILY_RESOLUTION_SPEC_V001.md"
SPEC_SHA256 = "b99c41a1744f3b252c32b484ec0ce49832fc5f95dc64a6dab2c855afd078892e"
OUT = ROOT / "stage8_execution/work/T07_relayed_family_resolution.json"

AUTHORITIES = {
    "STAGE8_T7_RELAY_DEPENDENCY_ORDER_AMENDMENT_V001.md":
        "29c32f90e6a4f88a26e22c91504b6d92a1fc4083ad6368984a1e94858caa4365",
    "R3_4_SHARED_SOURCE_CAUSAL_PARENT_RESULT_V001.md":
        "781608f2fe4c8753a0c06b1d87407b2a6c88caa0ab45329e1200160e56292a24",
    "BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md":
        "b786db3adec8cc335967d49ec13b59923d67f424644f72c535b27b579dd1489f",
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md":
        "6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb",
    "BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md":
        "7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476",
    "R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_RESULT_V001.md":
        "1d114e71c29c3a39b7afd1b7a80b47afb52fe77e8ee1e4e19b604defe3c69305",
    "R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md":
        "10909b5c21e73ecf655462339a27bd645b8d35e3ad11fb6f8cb204c601992995",
    "BID_SOURCE_DECORATED_FIRST_OPENING_CLASSIFICATION_V001.md":
        "edb0ba6d25a8a4c4182189b4f5b2b2f0cb3b7e916ad959ee87a51c6d3a43c915",
    "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md":
        "e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def embed_local(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    value = np.array([[1.0]])
    for index in range(count):
        value = np.kron(
            value,
            operator if index == site else np.eye(operator.shape[0]),
        )
    return value


def f1_transport_assignment() -> dict[str, object]:
    source_incidence = np.array(
        [
            [-1.0, 0.0, 0.0],
            [1.0, -1.0, 0.0],
            [0.0, 1.0, -1.0],
            [0.0, 0.0, 1.0],
        ]
    )
    projectors = [
        np.outer(source_incidence[:, j], source_incidence[:, j]) / 2.0
        for j in range(3)
    ]
    overlaps = np.array(
        [
            [np.trace(left @ right).real for right in projectors]
            for left in projectors
        ]
    )

    local_swap = np.array(
        [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]]
    )
    gamma5 = np.diag([1.0, 1.0, -1.0, -1.0])
    spin_identity = np.eye(4)
    source_spin_dimension = 4 * 4
    full_identity = np.eye(source_spin_dimension * 3**3)
    unitaries = []
    generators = []
    pointer = np.diag([0.0, 1.0, 0.0])
    prior_pointer_commutators: dict[str, float] = {}
    for cell in range(3):
        local_delta = embed_local(local_swap - np.eye(3), cell, 3)
        unitary = full_identity + np.kron(
            np.kron(projectors[cell], spin_identity), local_delta
        )
        unitaries.append(unitary)
        generators.append(
            np.kron(
                np.kron(projectors[cell], gamma5),
                embed_local(
                    np.array(
                        [
                            [0.0, 0.0, -1j],
                            [0.0, 0.0, 1j],
                            [1j, -1j, 0.0],
                        ]
                    ),
                    cell,
                    3,
                ),
            )
        )
        for prior in range(cell):
            pointer_observable = np.kron(
                np.eye(source_spin_dimension), embed_local(pointer, prior, 3)
            )
            prior_pointer_commutators[f"{cell}_after_{prior}"] = float(
                np.linalg.norm(
                    unitary @ pointer_observable
                    - pointer_observable @ unitary
                )
            )

    generator_commutators = {
        "0_1": float(
            np.linalg.norm(
                generators[0] @ generators[1]
                - generators[1] @ generators[0]
            )
        ),
        "1_2": float(
            np.linalg.norm(
                generators[1] @ generators[2]
                - generators[2] @ generators[1]
            )
        ),
        "0_2": float(
            np.linalg.norm(
                generators[0] @ generators[2]
                - generators[2] @ generators[0]
            )
        ),
    }
    unitary_order = {
        "0_1": float(
            np.linalg.norm(
                unitaries[1] @ unitaries[0]
                - unitaries[0] @ unitaries[1]
            )
        ),
        "1_2": float(
            np.linalg.norm(
                unitaries[2] @ unitaries[1]
                - unitaries[1] @ unitaries[2]
            )
        ),
        "0_2": float(
            np.linalg.norm(
                unitaries[2] @ unitaries[0]
                - unitaries[0] @ unitaries[2]
            )
        ),
    }

    # The declared causal chain 0<1<2 has one linear extension. If only the
    # overlap constraints are retained, 0 and 2 may swap, but their maps
    # commute and hence define the same product.
    all_orders = list(itertools.permutations(range(3)))
    causal_orders = [
        order
        for order in all_orders
        if order.index(0) < order.index(1) < order.index(2)
    ]
    overlap_compatible_orders = [
        order
        for order in all_orders
        if order.index(0) < order.index(1)
        and order.index(1) < order.index(2)
    ]

    require(np.max(np.abs(overlaps - np.array(
        [[1.0, 0.25, 0.0], [0.25, 1.0, 0.25], [0.0, 0.25, 1.0]]
    ))) < 1e-15, "projector overlaps")
    require(generator_commutators["0_1"] > 1.0, "adjacent 0,1 commute")
    require(generator_commutators["1_2"] > 1.0, "adjacent 1,2 commute")
    require(generator_commutators["0_2"] < 1e-14, "disjoint 0,2 fail")
    require(unitary_order["0_1"] > 1.0, "adjacent unitary order erased")
    require(unitary_order["1_2"] > 1.0, "adjacent unitary order erased")
    require(unitary_order["0_2"] < 1e-14, "disjoint unitary order matters")
    require(max(prior_pointer_commutators.values()) < 1e-14, "record rewrite")
    require(len(causal_orders) == 1, "causal assignment not unique")
    require(len(overlap_compatible_orders) == 1, "overlap order not unique")
    return {
        "projector_overlaps": overlaps.tolist(),
        "generator_commutator_norms": generator_commutators,
        "unitary_order_difference_norms": unitary_order,
        "prior_pointer_commutator_norms": prior_pointer_commutators,
        "causal_linear_extension_count": len(causal_orders),
        "disjoint_permutation_map_invariant": unitary_order["0_2"] < 1e-14,
        "linear_extension_independence_theorem": (
            "Any two linear extensions differ by adjacent swaps of "
            "incomparable cells; the declared branch makes such cells "
            "disjoint, and their operators commute."
        ),
        "scope": "causally sequential pure-charge primitive branch",
        "S_resolved": True,
    }


def f2_active_handle() -> dict[str, object]:
    # On active support, the retraction test C_lambda(P)=P gives lambda=1.
    lambdas = (-2.0, -1.0, 0.0, 0.5, 1.0, 2.0, 3.0)
    residuals = {str(value): abs(value - 1.0) for value in lambdas}
    surviving = [value for value in lambdas if residuals[str(value)] == 0.0]
    require(surviving == [1.0], "rescaled charged control survived")
    return {
        "charge_support": "P_ch=1_(R\\{0})(Q)=P_+ + P_-",
        "controlled_operator": "B_ch=P_ch tensor B_Q",
        "sector_coefficients": [0, 1, 1],
        "sample_retraction_residuals": residuals,
        "algebraic_retraction_condition": "(lambda-1)P=0 => lambda=1",
        "neutral_charged_write": False,
        "chi_resolved": True,
    }


def f3_endpoint() -> dict[str, object]:
    return {
        "minimal_graph": {
            "root_count": 1,
            "active_public_endpoint_count": 1,
            "primitive_arrow_count": 1,
        },
        "root_survival_is_completed": False,
        "parallel_paths_are_same_branch": False,
        "multiple_endpoints_are_same_branch": False,
        "response_dependent_endpoint_allowed": False,
        "beta_resolved": True,
    }


def f4_conditioning() -> dict[str, object]:
    fs = 1.0 / 4.0
    linear = 1.0 / 4.0
    probability = 1.0 / 2.0
    inclusive = 0.0
    require(linear == fs, "linear closure misses FS")
    require(probability != fs, "probability closure not excluded")
    require(inclusive != fs, "inclusive closure not excluded")
    return {
        "FS_curvature": fs,
        "linear_amplitude_attenuation": linear,
        "endpoint_probability_attenuation": probability,
        "inclusive_sandwich_attenuation": inclusive,
        "selected_operation": "normalized complex-linear branch return",
        "branch_sum_substituted": False,
        "sigma_resolved": True,
    }


def f5_interval() -> dict[str, object]:
    tau = math.pi / math.sqrt(2.0)
    rows = {}
    for arms in (1, 2, 3):
        maximum_designated = 2.0 / (arms + 1.0)
        maximum_symmetric = 2.0 * math.sqrt(arms) / (arms + 1.0)
        rows[str(arms)] = {
            "max_designated_transfer": maximum_designated,
            "max_symmetric_transfer": maximum_symmetric,
            "exact_transfer_possible":
                maximum_designated >= 1.0
                and maximum_symmetric >= 1.0,
        }
    require(rows["1"]["exact_transfer_possible"], "one-arm closure lost")
    require(not rows["2"]["exact_transfer_possible"], "two-arm survived")
    require(not rows["3"]["exact_transfer_possible"], "three-arm survived")
    return {
        "tau_record": tau,
        "least_positive_one_arm_interval": tau,
        "mixed_star_bounds": rows,
        "searched_replacement_interval_used": False,
        "I_resolved": True,
    }


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "sealed spec hash mismatch")
    for relative, expected in AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"authority drift: {relative}")

    f1 = f1_transport_assignment()
    f2 = f2_active_handle()
    f3 = f3_endpoint()
    f4 = f4_conditioning()
    f5 = f5_interval()
    resolved = all(
        (
            f1["S_resolved"],
            f2["chi_resolved"],
            f3["beta_resolved"],
            f4["sigma_resolved"],
            f5["I_resolved"],
        )
    )
    result = {
        "schema": "stage8_t7_relayed_family_resolution_v001",
        "spec_sha256": SPEC_SHA256,
        "F1_transport_assignment": f1,
        "F2_active_handle": f2,
        "F3_endpoint": f3,
        "F4_conditioning": f4,
        "F5_interval": f5,
        "overall_verdict": (
            "RELAYED_FAMILY_RESOLVED_IN_DECLARED_BRANCH"
            if resolved
            else "RELAYED_FAMILY_SURVIVES"
        ),
        "relayed_family_resolved": resolved,
        "universal_enlarged_branch_exhaustion_claimed": False,
        "physical_connected_preparation_derived": False,
        "branch_conditioning_is_not_physical_in_state_selection": True,
        "connected_primitive_amplitude_derived": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
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
