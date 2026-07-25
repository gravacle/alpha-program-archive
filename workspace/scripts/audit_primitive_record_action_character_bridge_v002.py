#!/usr/bin/env python3
"""Fail-closed exact audit of the primitive action-character/FS bridge."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import math
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "PRIMITIVE_RECORD_ACTION_CHARACTER_BRIDGE_GATE_V002.md"
PROVENANCE = ROOT / "provenance_inputs_v003.json"
ONSET_NOTE = ROOT / "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md"
ONSET_NOTE_SEAL = ROOT / "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.seal.sha256"
ONSET_RESULT = ROOT / "results" / "boundary_record_onset_saturation_action_v003.json"
ONSET_RESULT_SEAL = ROOT / "results" / "boundary_record_onset_saturation_action_v003.seal.sha256"
RESULT = ROOT / "results" / "primitive_record_action_character_bridge_v002.json"

EXPECTED_SINGLE_HANDLE_PATH = (
    "../../gravacle_v159_final_review_zenodo_candidate_2026-06-30/"
    "reports/gravacle_v156_single_handle_recombination_theorem.md"
)
EXPECTED_SINGLE_HANDLE_HASH = (
    "0b0ef6ea4802d0aba43b237163d326802985f7f3f9a9e078f447965e0ca27e7b"
)

RationalMatrix = tuple[tuple[Fraction, ...], ...]
RationalVector = tuple[Fraction, ...]
Gaussian = tuple[Fraction, Fraction]
GaussianMatrix = tuple[tuple[Gaussian, ...], ...]

I2: RationalMatrix = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1)),
)
U_HALF_TURN: RationalMatrix = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(-1)),
)
CENTERED_GENERATOR: RationalMatrix = (
    (Fraction(-1, 2), Fraction(0)),
    (Fraction(0), Fraction(1, 2)),
)
READY_NUM: RationalVector = (Fraction(1), Fraction(1))
CHARACTER_WINDING = 1
ACTION_PERIOD_PI_UNITS = 2
DECLARED_COMPARISON_PLANE_COUNT = 1
PURE_READY_STATE_DECLARED = True
BALANCED_GEODESIC_SCOPE_DECLARED = True
UNIT_CHARACTER_MODULUS_SQUARED = Fraction(1)

G_ZERO: Gaussian = (Fraction(0), Fraction(0))
G_ONE: Gaussian = (Fraction(1), Fraction(0))
G_NEG_I: Gaussian = (Fraction(0), Fraction(-1))
G_I: Gaussian = (Fraction(0), Fraction(1))
CENTERED_HALF_TURN: GaussianMatrix = (
    (G_NEG_I, G_ZERO),
    (G_ZERO, G_I),
)
COMMON_PHASE_I: GaussianMatrix = (
    (G_I, G_ZERO),
    (G_ZERO, G_I),
)
GAUSSIAN_U_HALF_TURN: GaussianMatrix = (
    (G_ONE, G_ZERO),
    (G_ZERO, (Fraction(-1), Fraction(0))),
)
G_X: GaussianMatrix = (
    (G_ZERO, G_ONE),
    (G_ONE, G_ZERO),
)
G_Y: GaussianMatrix = (
    (G_ZERO, G_NEG_I),
    (G_I, G_ZERO),
)
G_NEG_X: GaussianMatrix = (
    (G_ZERO, (Fraction(-1), Fraction(0))),
    ((Fraction(-1), Fraction(0)), G_ZERO),
)
G_NEG_Y: GaussianMatrix = (
    (G_ZERO, G_I),
    (G_NEG_I, G_ZERO),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_seal(target: Path, seal: Path) -> None:
    require(target.is_file(), f"Missing sealed target: {target}")
    require(seal.is_file(), f"Missing seal: {seal}")
    parts = seal.read_text(encoding="utf-8").strip().split()
    require(len(parts) == 2, f"Malformed seal: {seal}")
    require(parts[1] == target.name, f"Seal target mismatch: {seal}")
    require(parts[0] == sha256(target), f"Seal hash mismatch: {target}")


def mat_vec(matrix: RationalMatrix, vector: RationalVector) -> RationalVector:
    return tuple(
        sum(
            (matrix[row][column] * vector[column] for column in range(len(vector))),
            Fraction(0),
        )
        for row in range(len(matrix))
    )


def inner(left: RationalVector, right: RationalVector) -> Fraction:
    return sum(
        (left[index] * right[index] for index in range(len(left))),
        Fraction(0),
    )


def expectation(
    vector: RationalVector,
    operator: RationalMatrix,
) -> Fraction:
    norm = inner(vector, vector)
    require(norm > 0, "Zero ready vector")
    return inner(vector, mat_vec(operator, vector)) / norm


def square(matrix: RationalMatrix) -> RationalMatrix:
    size = len(matrix)
    return tuple(
        tuple(
            sum(
                (
                    matrix[row][index] * matrix[index][column]
                    for index in range(size)
                ),
                Fraction(0),
            )
            for column in range(size)
        )
        for row in range(size)
    )


def g_add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def g_mul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def g_conj(value: Gaussian) -> Gaussian:
    return value[0], -value[1]


def g_dagger(matrix: GaussianMatrix) -> GaussianMatrix:
    return tuple(
        tuple(g_conj(matrix[column][row]) for column in range(len(matrix)))
        for row in range(len(matrix[0]))
    )


def g_mat_mul(left: GaussianMatrix, right: GaussianMatrix) -> GaussianMatrix:
    size = len(left)

    def entry(row: int, column: int) -> Gaussian:
        total = G_ZERO
        for index in range(size):
            total = g_add(total, g_mul(left[row][index], right[index][column]))
        return total

    return tuple(
        tuple(
            entry(row, column)
            for column in range(size)
        )
        for row in range(size)
    )


def fraction_sqrt(value: Fraction) -> Fraction:
    require(value >= 0, "Cannot take square root of a negative rational")
    numerator = math.isqrt(value.numerator)
    denominator = math.isqrt(value.denominator)
    require(
        numerator * numerator == value.numerator
        and denominator * denominator == value.denominator,
        "Rational is not an exact square",
    )
    return Fraction(numerator, denominator)


def format_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def format_pi_hbar(value: Fraction) -> str:
    if value == 1:
        return "pi*hbar"
    if value.numerator == 1:
        return f"pi*hbar/{value.denominator}"
    if value.denominator == 1:
        return f"{value.numerator}*pi*hbar"
    return f"{value.numerator}*pi*hbar/{value.denominator}"


def solve_orthogonality_root() -> tuple[Fraction, Fraction, Fraction]:
    """Solve p+(1-p)(x+i y)=0 with x^2+y^2=1 and 0<p<1."""

    require(
        UNIT_CHARACTER_MODULUS_SQUARED == 1,
        "Unit-character modulus normalization drift",
    )

    # Since 0 < p < 1, the imaginary equation (1-p)y=0 forces y=0.
    y = Fraction(0)

    # The unit-character equation then gives the two exact real roots x=+/-1.
    radius = fraction_sqrt(UNIT_CHARACTER_MODULUS_SQUARED)
    x_roots = (-radius, radius)
    solutions: list[tuple[Fraction, Fraction, Fraction]] = []
    for x in x_roots:
        # The real equation is p+(1-p)x=0, hence p=-x/(1-x).
        if x == 1:
            continue
        p = -x / (1 - x)
        if not (0 < p < 1):
            continue
        require(p + (1 - p) * x == 0, "Computed real overlap root is invalid")
        require((1 - p) * y == 0, "Computed imaginary overlap root is invalid")
        require(
            x * x + y * y == UNIT_CHARACTER_MODULUS_SQUARED,
            "Computed phase root is off the unit circle",
        )
        solutions.append((p, x, y))

    require(len(solutions) == 1, "Orthogonality root is not unique")
    return solutions[0]


def principal_angle_in_pi_units(
    x: Fraction,
    y: Fraction,
) -> Fraction:
    """Map exact real unit-character roots to the imported principal interval."""

    require(ACTION_PERIOD_PI_UNITS == 2, "Principal action period drift")
    require(CHARACTER_WINDING == 1, "Principal root map uses unit winding")
    require(y == 0, "Root is not on the real character axis")
    if x == 1:
        return Fraction(0)
    if x == -1:
        return Fraction(1)
    raise RuntimeError("Unsupported exact unit-character root")


def build_result() -> dict[str, object]:
    note = NOTE.read_text(encoding="utf-8")
    provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))

    verify_seal(ONSET_NOTE, ONSET_NOTE_SEAL)
    verify_seal(ONSET_RESULT, ONSET_RESULT_SEAL)
    onset = json.loads(ONSET_RESULT.read_text(encoding="utf-8"))
    require(
        onset["status"]
        == "PASS_RELATIVE_FS_BUDGET_CONDITIONAL_PHYSICAL_ACTION_OPEN",
        "Unexpected onset parent status",
    )
    require(onset["relative_FS_budget"] == "pi*hbar/2", "Wrong onset budget")
    require(onset["physical_dynamical_action_fixed"] is False, "Parent scope promoted")
    require(onset["alpha_computed"] is False, "Parent alpha flag promoted")

    single_handle_rows = [
        row
        for row in provenance["inputs"]
        if row.get("path") == EXPECTED_SINGLE_HANDLE_PATH
    ]
    require(len(single_handle_rows) == 1, "Single-handle provenance row is not unique")
    row = single_handle_rows[0]
    require(
        row.get("sha256") == EXPECTED_SINGLE_HANDLE_HASH,
        "Single-handle declared hash changed",
    )
    source = (ROOT / EXPECTED_SINGLE_HANDLE_PATH).resolve()
    require(source.is_file(), "Single-handle source is missing")
    require(sha256(source) == EXPECTED_SINGLE_HANDLE_HASH, "Single-handle source drift")

    require(I2 != U_HALF_TURN, "Half-turn is the identity")
    require(square(U_HALF_TURN) == I2, "Half-turn does not square to identity")
    require(
        type(PURE_READY_STATE_DECLARED) is bool and PURE_READY_STATE_DECLARED,
        "Pure ready-state scope is not declared",
    )
    require(
        type(BALANCED_GEODESIC_SCOPE_DECLARED) is bool
        and BALANCED_GEODESIC_SCOPE_DECLARED,
        "Balanced geodesic scope is not declared",
    )
    require(
        DECLARED_COMPARISON_PLANE_COUNT == 1,
        "Gate is scoped to one comparison plane",
    )
    require(abs(CHARACTER_WINDING) == 1, "Character is not primitive and faithful")
    require(
        ACTION_PERIOD_PI_UNITS == 2,
        "Imported action-character period is not 2*pi*hbar",
    )
    require(
        g_mat_mul(COMMON_PHASE_I, CENTERED_HALF_TURN)
        == GAUSSIAN_U_HALF_TURN,
        "Centered half-angle lift is not the diagonal half-turn up to common phase",
    )
    centered_dagger = g_dagger(CENTERED_HALF_TURN)
    require(
        g_mat_mul(
            g_mat_mul(CENTERED_HALF_TURN, G_X),
            centered_dagger,
        )
        == G_NEG_X,
        "Hilbert half-angle does not induce the full half-turn on X",
    )
    require(
        g_mat_mul(
            g_mat_mul(CENTERED_HALF_TURN, G_Y),
            centered_dagger,
        )
        == G_NEG_Y,
        "Hilbert half-angle does not induce the full half-turn on Y",
    )
    ready_norm = inner(READY_NUM, READY_NUM)
    require(ready_norm == 2, "Ready state is not balanced")
    endpoint_overlap_numerator = inner(
        READY_NUM,
        mat_vec(U_HALF_TURN, READY_NUM),
    )
    require(endpoint_overlap_numerator == 0, "Half-turn endpoint is not orthogonal")

    mean = expectation(READY_NUM, CENTERED_GENERATOR)
    second_moment = expectation(READY_NUM, square(CENTERED_GENERATOR))
    variance = second_moment - mean * mean
    require(mean == 0, "Centered generator has nonzero balanced-state mean")
    require(variance == Fraction(1, 4), "Wrong balanced-state generator variance")
    generator_uncertainty = fraction_sqrt(variance)
    solved_population, phase_x, phase_y = solve_orthogonality_root()
    require(
        solved_population == Fraction(1, 2),
        "Continuous orthogonality solve did not force balanced population",
    )
    require(
        (phase_x, phase_y) == (Fraction(-1), Fraction(0)),
        "Continuous orthogonality solve did not force the half-turn root",
    )
    relative_angle_in_pi_units = principal_angle_in_pi_units(phase_x, phase_y)
    action_marker_in_pi_hbar_units = relative_angle_in_pi_units
    fs_budget_in_pi_hbar_units = (
        generator_uncertainty * relative_angle_in_pi_units
    )
    require(
        fs_budget_in_pi_hbar_units == Fraction(1, 2),
        "Computed FS budget coefficient is not 1/2",
    )
    action_to_fs_ratio = (
        action_marker_in_pi_hbar_units / fs_budget_in_pi_hbar_units
    )
    require(action_to_fs_ratio == 2, "Computed action/FS ratio is not 2")

    required_note_lines = (
        "pure_C2_comparison_representation_imported = true",
        "Hermitian_Born_overlap_imported = true",
        "Fubini_Study_convention_imported = true",
        "standard_additive_action_character_imported = true",
        "primitive_unit_winding_imported = true",
        "relative_action_marker_interval = pi*hbar",
        "unique_primitive_carrier_derived = false",
        "bloch_ball_derived = false",
        "M2C_algebra_derived = false",
        "historical_target_blindness_established = false",
        "physical_onset_action_derived = false",
        "complete_physical_dynamical_action_fixed = false",
        "complete_source_record_environment_operator_derived = false",
        "record_generated_source_mass_derived = false",
        "coupling_evaluation_authorized = false",
        "alpha_computed = false",
        "proof_authorized = false",
    )
    require(
        all(line in note for line in required_note_lines),
        "Gate note is missing fail-closed status lines",
    )
    forbidden = (
        re.compile("137" + r"[.]0[0-9]+"),
        re.compile("0" + r"[.]00729[0-9]+"),
        re.compile("17" + r"[.]543"),
    )
    target_hits = [pattern.pattern for pattern in forbidden if pattern.search(note)]
    require(not target_hits, "Target-number literal found in bridge gate")

    out: dict[str, object] = {
        "status": "PASS_PRIMITIVE_ACTION_CHARACTER_FS_BRIDGE_PHYSICAL_ACTION_OPEN",
        "single_handle_source_hash_verified": True,
        "ordinary_two_endpoint_comparison_face_inherited_conditionally": True,
        "unique_primitive_carrier_derived": False,
        "bloch_ball_derived": False,
        "M2C_algebra_derived": False,
        "pure_C2_comparison_representation_imported": True,
        "Hermitian_Born_overlap_imported": True,
        "Fubini_Study_convention_imported": True,
        "standard_additive_action_character_imported": True,
        "action_character_period": "2*pi*hbar",
        "primitive_character_winding": CHARACTER_WINDING,
        "primitive_unit_winding_imported": True,
        "primitive_unit_winding_derived_here": False,
        "hilbert_space_half_turn_lift_verified": True,
        "orientation_plane_half_turn_adjoint_verified": True,
        "balanced_ready_state_derived_from_orthogonality": True,
        "orthogonalizing_population": format_fraction(solved_population),
        "first_half_turn_derived_from_orthogonality": True,
        "orthogonality_character_root": {
            "real": format_fraction(phase_x),
            "imaginary": format_fraction(phase_y),
        },
        "relative_character_angle_in_pi_units": format_fraction(
            relative_angle_in_pi_units
        ),
        "centered_generator_mean": "0",
        "centered_generator_variance": "1/4",
        "centered_generator_uncertainty": format_fraction(generator_uncertainty),
        "relative_action_marker_interval_fixed": True,
        "relative_action_marker_in_pi_hbar_units": format_fraction(
            action_marker_in_pi_hbar_units
        ),
        "relative_action_marker_interval": (
            format_pi_hbar(action_marker_in_pi_hbar_units)
        ),
        "relative_FS_budget_bridge_derived": True,
        "relative_FS_budget_in_pi_hbar_units": format_fraction(
            fs_budget_in_pi_hbar_units
        ),
        "relative_FS_budget": (
            format_pi_hbar(fs_budget_in_pi_hbar_units)
        ),
        "relative_action_to_FS_budget_ratio": format_fraction(action_to_fs_ratio),
        "relative_action_marker_equals_two_FS_budgets": action_to_fs_ratio == 2,
        "historical_target_blindness_established": False,
        "physical_onset_action_derived": False,
        "complete_physical_dynamical_action_fixed": False,
        "complete_source_record_environment_operator_derived": False,
        "orthogonal_reduced_record_supports_derived": False,
        "physical_durability_derived": False,
        "unique_causal_record_interval_numerically_derived": False,
        "record_generated_source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "target_literal_hits": target_hits,
        "scope": "conditional_primitive_unit_action_character_and_relative_holonomy_only",
    }
    required_keys = {
        "status",
        "single_handle_source_hash_verified",
        "ordinary_two_endpoint_comparison_face_inherited_conditionally",
        "unique_primitive_carrier_derived",
        "bloch_ball_derived",
        "M2C_algebra_derived",
        "pure_C2_comparison_representation_imported",
        "Hermitian_Born_overlap_imported",
        "Fubini_Study_convention_imported",
        "standard_additive_action_character_imported",
        "action_character_period",
        "primitive_character_winding",
        "primitive_unit_winding_imported",
        "primitive_unit_winding_derived_here",
        "hilbert_space_half_turn_lift_verified",
        "orientation_plane_half_turn_adjoint_verified",
        "balanced_ready_state_derived_from_orthogonality",
        "orthogonalizing_population",
        "first_half_turn_derived_from_orthogonality",
        "orthogonality_character_root",
        "relative_character_angle_in_pi_units",
        "centered_generator_mean",
        "centered_generator_variance",
        "centered_generator_uncertainty",
        "relative_action_marker_interval_fixed",
        "relative_action_marker_in_pi_hbar_units",
        "relative_action_marker_interval",
        "relative_FS_budget_bridge_derived",
        "relative_FS_budget_in_pi_hbar_units",
        "relative_FS_budget",
        "relative_action_to_FS_budget_ratio",
        "relative_action_marker_equals_two_FS_budgets",
        "historical_target_blindness_established",
        "physical_onset_action_derived",
        "complete_physical_dynamical_action_fixed",
        "complete_source_record_environment_operator_derived",
        "orthogonal_reduced_record_supports_derived",
        "physical_durability_derived",
        "unique_causal_record_interval_numerically_derived",
        "record_generated_source_mass_derived",
        "spectral_evaluation_authorized",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
        "target_literal_hits",
        "scope",
    }
    require(set(out) == required_keys, "Result schema drift")
    return out


def main() -> None:
    out = build_result()
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
