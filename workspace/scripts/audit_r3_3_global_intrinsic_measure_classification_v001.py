#!/usr/bin/env python3
"""Exact audit of the global intrinsic flat-cell measure classification."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_SPEC_V001.md"
SPEC_SEAL = (
    ROOT
    / "R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_SPEC_V001.seal.sha256"
)
RESULT = (
    ROOT
    / "results"
    / "r3_3_global_intrinsic_measure_classification_v001.json"
)

PINNED_HASHES = {
    "R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_SPEC_V001.md": (
        "d9262ea2b4302896702f4849d1084dadc9406f77fede726079f47c9d039fbde8"
    ),
    "R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md": (
        "e60aec3c44cfc5f1ef5715d3445e53783b0185ef93e54d94e442ff1df2ae9b59"
    ),
    "BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md": (
        "451550c3825288d699db35c7289e408e8314ad042450253b58f32722c4ead46b"
    ),
    "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md": (
        "aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a"
    ),
    "CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md": (
        "b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30"
    ),
    "PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md": (
        "532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb"
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def zero_matrix(size: int = 4) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(size)] for _ in range(size)]


def rotation(first: int, second: int) -> list[list[Fraction]]:
    matrix = zero_matrix()
    matrix[first][second] = Fraction(-1)
    matrix[second][first] = Fraction(1)
    return matrix


def boost(spatial: int) -> list[list[Fraction]]:
    matrix = zero_matrix()
    matrix[0][spatial] = Fraction(1)
    matrix[spatial][0] = Fraction(1)
    return matrix


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*matrix)]


def matmul(
    left: list[list[Fraction]],
    right: list[list[Fraction]],
) -> list[list[Fraction]]:
    return [
        [
            sum(
                (left[row][inner] * right[inner][column] for inner in range(4)),
                Fraction(0),
            )
            for column in range(4)
        ]
        for row in range(4)
    ]


def subtract(
    left: list[list[Fraction]],
    right: list[list[Fraction]],
) -> list[list[Fraction]]:
    return [
        [left[row][column] - right[row][column] for column in range(4)]
        for row in range(4)
    ]


def matrix_rank(rows: list[list[Fraction]]) -> int:
    work = [list(row) for row in rows if any(value != 0 for value in row)]
    if not work:
        return 0
    row_count = len(work)
    column_count = len(work[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if work[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = work[row][column]
            if factor:
                work[row] = [
                    work[row][entry] - factor * work[pivot_row][entry]
                    for entry in range(column_count)
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def flatten(matrix: list[list[Fraction]]) -> list[Fraction]:
    return [value for row in matrix for value in row]


def lorentz_generators() -> dict[str, list[list[Fraction]]]:
    return {
        "J12": rotation(1, 2),
        "J13": rotation(1, 3),
        "J23": rotation(2, 3),
        "K01": boost(1),
        "K02": boost(2),
        "K03": boost(3),
    }


def fixed_covector_constraints(
    generators: dict[str, list[list[Fraction]]],
) -> list[list[Fraction]]:
    rows: list[list[Fraction]] = []
    for generator in generators.values():
        rows.extend(transpose(generator))
    return rows


def commutator_span_rank(
    generators: dict[str, list[list[Fraction]]],
) -> tuple[int, int]:
    values = list(generators.values())
    generator_rank = matrix_rank([flatten(value) for value in values])
    commutators = []
    for left_index, left in enumerate(values):
        for right in values[left_index + 1 :]:
            commutators.append(
                flatten(subtract(matmul(left, right), matmul(right, left)))
            )
    return generator_rank, matrix_rank(commutators)


def exact_mu_a_negative_control() -> dict[str, object]:
    # Earlier exact calculation:
    # Delta<t> = 3a/[4(960+19a)]
    # Delta<u_C> = -a(a+45)/[7(a+60)(19a+960)].
    time_numerator_roots = {Fraction(0)}
    child_u_numerator_roots = {Fraction(0), Fraction(-45)}
    common_nonnegative_roots = sorted(
        root
        for root in time_numerator_roots & child_u_numerator_roots
        if root >= 0
    )
    return {
        "delta_t_numerator_roots": [
            f"{root.numerator}/{root.denominator}"
            for root in sorted(time_numerator_roots)
        ],
        "delta_u_child_numerator_roots": [
            f"{root.numerator}/{root.denominator}"
            for root in sorted(child_u_numerator_roots)
        ],
        "common_nonnegative_roots": [
            f"{root.numerator}/{root.denominator}"
            for root in common_nonnegative_roots
        ],
        "only_uniform_member_survives": common_nonnegative_roots == [0],
    }


def main() -> None:
    authority_hashes = {
        name: {
            "expected": expected,
            "actual": sha256(ROOT / name),
            "matches": sha256(ROOT / name) == expected,
        }
        for name, expected in PINNED_HASHES.items()
    }
    authority_hashes_match = all(
        item["matches"] for item in authority_hashes.values()
    )

    expected_spec_hash = SPEC_SEAL.read_text().split()[0]
    actual_spec_hash = sha256(SPEC)
    spec_seal_matches = expected_spec_hash == actual_spec_hash

    spec_text = SPEC.read_text()
    assumption_text_checks = {
        "positive_absolute_continuity": "### A1. Positive absolute continuity"
        in spec_text,
        "intrinsic_restriction_naturality": (
            "### A2. Intrinsic restriction naturality" in spec_text
        ),
        "poincare_covariance": (
            "### A3. Proper-orthochronous Poincare covariance" in spec_text
        ),
        "continuous_density_ray": (
            "### A4. Regularity of the density ray" in spec_text
        ),
        "no_preferred_covector": (
            "No preferred origin, inertial frame, timelike covector" in spec_text
        ),
    }
    assumptions_textually_pinned = all(assumption_text_checks.values())

    generators = lorentz_generators()
    constraints = fixed_covector_constraints(generators)
    constraint_rank = matrix_rank(constraints)
    fixed_covector_nullity = 4 - constraint_rank

    basis_covectors = [
        [Fraction(1 if row == column else 0) for row in range(4)]
        for column in range(4)
    ]
    basis_failures = {}
    for index, covector in enumerate(basis_covectors):
        violated_rows = sum(
            1
            for row in constraints
            if sum(
                (row[column] * covector[column] for column in range(4)),
                Fraction(0),
            )
            != 0
        )
        basis_failures[f"e{index}"] = violated_rows

    generator_rank, commutator_rank = commutator_span_rank(generators)
    lorentz_lie_algebra_perfect = (
        generator_rank == 6 and commutator_rank == generator_rank
    )

    # A nonzero continuous translation character exists before Lorentz
    # covariance is imposed: its logarithm is the additive map a -> k.a.
    sample_k = [Fraction(1), Fraction(2), Fraction(-1), Fraction(3)]
    sample_a = [Fraction(2), Fraction(-1), Fraction(4), Fraction(1)]
    sample_b = [Fraction(-3), Fraction(5), Fraction(1), Fraction(2)]
    dot = lambda left, right: sum(
        (left[index] * right[index] for index in range(4)), Fraction(0)
    )
    additive_exponent_pass = dot(
        sample_k,
        [sample_a[index] + sample_b[index] for index in range(4)],
    ) == dot(sample_k, sample_a) + dot(sample_k, sample_b)
    sample_k_violates_lorentz = any(
        sum(
            (row[column] * sample_k[column] for column in range(4)),
            Fraction(0),
        )
        != 0
        for row in constraints
    )

    mu_a_control = exact_mu_a_negative_control()
    global_classification_pass = all(
        (
            authority_hashes_match,
            spec_seal_matches,
            assumptions_textually_pinned,
            fixed_covector_nullity == 0,
            all(value > 0 for value in basis_failures.values()),
            lorentz_lie_algebra_perfect,
            additive_exponent_pass,
            sample_k_violates_lorentz,
            mu_a_control["only_uniform_member_survives"],
        )
    )

    if global_classification_pass:
        verdict = "GLOBAL_INTRINSIC_FLAT_CELL_MEASURE_CLASSIFIED"
    elif fixed_covector_nullity > 0:
        verdict = "NONUNIFORM_POINCARE_COVARIANT_DENSITY_RAY_SURVIVES"
    elif mu_a_control["only_uniform_member_survives"]:
        verdict = "FAMILY_TEST_ONLY_GLOBAL_CLASSIFICATION_OPEN"
    else:
        verdict = "R3_3_GLOBAL_CLASSIFICATION_BLOCKED"

    result = {
        "specification_sha256": actual_spec_hash,
        "specification_seal_matches": spec_seal_matches,
        "authority_hashes": authority_hashes,
        "authority_hashes_match": authority_hashes_match,
        "assumption_text_checks": assumption_text_checks,
        "assumptions_textually_pinned": assumptions_textually_pinned,
        "lorentz_generator_count": len(generators),
        "fixed_covector_constraint_rank": constraint_rank,
        "fixed_covector_nullity": fixed_covector_nullity,
        "basis_covector_violated_constraint_counts": basis_failures,
        "lorentz_generator_span_rank": generator_rank,
        "lorentz_commutator_span_rank": commutator_rank,
        "lorentz_lie_algebra_perfect": lorentz_lie_algebra_perfect,
        "translation_character_additive_exponent_pass": additive_exponent_pass,
        "translations_alone_permit_nonuniform_character": additive_exponent_pass,
        "sample_nonzero_character_violates_lorentz": (
            sample_k_violates_lorentz
        ),
        "mu_a_negative_control": mu_a_control,
        "global_classification_pass": global_classification_pass,
        "verdict": verdict,
        "uniform_flat_cell_measure_derived": global_classification_pass,
        "spectral_density_derived": False,
        "complete_parent_generator_derived": False,
        "hypothesis_promoted_to_principle": False,
        "construction_uses_alpha": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
