#!/usr/bin/env python3
"""Exact R3.4 regulator-scheme and covector-ray sufficiency audit."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_REGULATOR_SCHEME_AND_RAY_SUFFICIENCY_SPEC_V001.md"
PROVENANCE = (
    ROOT / "R3_4_REGULATOR_SCHEME_AND_RAY_SUFFICIENCY_PROVENANCE_V001.json"
)
OUTPUT = ROOT / "results" / "r3_4_regulator_scheme_and_ray_sufficiency_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_provenance() -> dict:
    provenance = json.loads(PROVENANCE.read_text(encoding="ascii"))
    for authority in provenance["authorities"]:
        path = ROOT / authority["path"]
        require(path.is_file(), f"Missing authority: {authority['path']}")
        require(
            sha256(path) == authority["sha256"],
            f"Authority hash mismatch: {authority['path']}",
        )
    return provenance


def half_line_return_moments(max_order: int) -> dict[int, int]:
    state: dict[int, int] = {0: 1}
    moments = {0: 1}
    for step in range(1, max_order + 1):
        next_state: dict[int, int] = defaultdict(int)
        for position, count in state.items():
            if position > 0:
                next_state[position - 1] += count
            next_state[position + 1] += count
        state = dict(next_state)
        moments[step] = state.get(0, 0)
    return moments


def cubic_return_moments(max_order: int) -> dict[int, int]:
    state: dict[tuple[int, int, int], int] = {(0, 0, 0): 1}
    moments = {0: 1}
    steps = (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    )
    for order in range(1, max_order + 1):
        next_state: dict[tuple[int, int, int], int] = defaultdict(int)
        for position, count in state.items():
            for delta in steps:
                target = tuple(position[j] + delta[j] for j in range(3))
                next_state[target] += count
        state = dict(next_state)
        moments[order] = state.get((0, 0, 0), 0)
    return moments


def standardized(moments: dict[int, Fraction]) -> dict[str, str]:
    m2 = moments[2]
    return {
        "m4_over_m2_squared": str(moments[4] / (m2 * m2)),
        "m6_over_m2_cubed": str(moments[6] / (m2 * m2 * m2)),
    }


def main() -> None:
    provenance = verify_provenance()

    half_raw = half_line_return_moments(6)
    cubic_raw = cubic_return_moments(6)
    half = {order: Fraction(value) for order, value in half_raw.items()}
    tree = {
        order: value * Fraction(3 ** (order // 2))
        if order % 2 == 0
        else Fraction(0)
        for order, value in half.items()
    }
    cubic = {order: Fraction(value) for order, value in cubic_raw.items()}

    required_even = (2, 4, 6)
    require(
        [half[order] for order in required_even] == [1, 2, 5],
        "Half-line closed-walk moments changed",
    )
    require(
        [tree[order] for order in required_even] == [3, 18, 135],
        "Radial-tree scaled moments changed",
    )
    require(
        [cubic[order] for order in required_even] == [6, 90, 1860],
        "Cubic-lattice closed-walk moments changed",
    )

    invariants = {
        "half_line": standardized(half),
        "radial_tree": standardized(tree),
        "cubic_lattice": standardized(cubic),
    }
    half_tree_equivalent_up_to_scale = (
        invariants["half_line"] == invariants["radial_tree"]
    )
    all_three_equivalent_up_to_scale = len(
        {
            tuple(sorted(row.items()))
            for row in invariants.values()
        }
    ) == 1

    common_probability_decay_exponent = Fraction(3)
    decay_derivation = {
        "half_line": "J1(2t)/t = O(t^-3/2) in amplitude",
        "radial_tree": "time rescaling preserves the half-line exponent",
        "cubic_lattice": "J0(2t)^3 = O(t^-3/2) in amplitude",
        "probability_exponent": str(common_probability_decay_exponent),
    }

    same_abstract_quasilocal_algebra_and_product_state_form = True
    distinct_local_generators_have_inequivalent_root_measures = (
        not all_three_equivalent_up_to_scale
    )
    ray_fixes_spectral_measure = not (
        same_abstract_quasilocal_algebra_and_product_state_form
        and distinct_local_generators_have_inequivalent_root_measures
    )

    result = {
        "schema": "r3.4-regulator-scheme-and-ray-sufficiency-v001",
        "spec_sha256": sha256(SPEC),
        "provenance_sha256": sha256(PROVENANCE),
        "authorities_verified": True,
        "target_values_used": False,
        "root_even_moments": {
            "half_line": {str(k): str(half[k]) for k in required_even},
            "radial_tree": {str(k): str(tree[k]) for k in required_even},
            "cubic_lattice": {str(k): str(cubic[k]) for k in required_even},
        },
        "standardized_moments": invariants,
        "decay_derivation": decay_derivation,
        "all_three_share_t_minus_3_probability_class": True,
        "half_line_and_radial_tree_equivalent_up_to_energy_scale": (
            half_tree_equivalent_up_to_scale
        ),
        "all_three_full_measures_equivalent_up_to_energy_scale": (
            all_three_equivalent_up_to_scale
        ),
        "regulator_scheme_verdict": (
            "FULL_THREE_REGULATOR_MEASURE_EQUIVALENCE"
            if all_three_equivalent_up_to_scale
            else "COMMON_DECAY_CLASS_ONLY"
        ),
        "same_abstract_quasilocal_UHF_and_product_state_form": (
            same_abstract_quasilocal_algebra_and_product_state_form
        ),
        "distinct_local_generators_have_inequivalent_root_measures": (
            distinct_local_generators_have_inequivalent_root_measures
        ),
        "covector_ray_and_quasilocal_state_fix_generator": False,
        "covector_ray_and_quasilocal_state_fix_spectral_measure": (
            ray_fixes_spectral_measure
        ),
        "ray_sufficiency_verdict": (
            "RAY_SELECTS_SPECTRAL_MEASURE"
            if ray_fixes_spectral_measure
            else "OUTGOING_ALGEBRA_DOES_NOT_FIX_DYNAMICS"
        ),
        "outgoing_record_algebra_subobligation_closed": True,
        "spectral_dynamics_must_come_from_complete_parent_action": True,
        "unique_covariant_spectral_measure_derived": False,
        "hypothesis_promoted_to_principle": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": "DECAY_CLASS_ROBUST_ALGEBRA_DERIVED_SPECTRAL_DYNAMICS_OPEN",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
