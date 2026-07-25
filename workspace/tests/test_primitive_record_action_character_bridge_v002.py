"""Independent tests for the primitive action-character/FS bridge gate."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_primitive_record_action_character_bridge_v002.py"
RESULT = ROOT / "results" / "primitive_record_action_character_bridge_v002.json"


def load_module():
    spec = importlib.util.spec_from_file_location("action_character_bridge", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load action-character bridge audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_exact_character_overlap_and_variance_independently() -> None:
    ready = (Fraction(1), Fraction(1))
    half_turn = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-1)),
    )
    generator = (
        (Fraction(-1, 2), Fraction(0)),
        (Fraction(0), Fraction(1, 2)),
    )

    transformed = (
        half_turn[0][0] * ready[0] + half_turn[0][1] * ready[1],
        half_turn[1][0] * ready[0] + half_turn[1][1] * ready[1],
    )
    overlap = ready[0] * transformed[0] + ready[1] * transformed[1]
    if overlap != 0:
        raise AssertionError("Independent half-turn overlap is nonzero")

    norm = sum(value * value for value in ready)
    mean = (
        ready[0] * generator[0][0] * ready[0]
        + ready[1] * generator[1][1] * ready[1]
    ) / norm
    second = (
        ready[0] * generator[0][0] ** 2 * ready[0]
        + ready[1] * generator[1][1] ** 2 * ready[1]
    ) / norm
    if mean != 0 or second - mean * mean != Fraction(1, 4):
        raise AssertionError("Independent generator variance is not 1/4")


def test_population_minimum_has_unique_zero() -> None:
    module = load_module()
    population, phase_x, phase_y = module.solve_orthogonality_root()
    if population != Fraction(1, 2):
        raise AssertionError("Exact solve did not force balanced population")
    if (phase_x, phase_y) != (Fraction(-1), Fraction(0)):
        raise AssertionError("Exact solve did not force the half-turn root")
    if module.principal_angle_in_pi_units(phase_x, phase_y) != 1:
        raise AssertionError("Half-turn root did not map to theta/pi=1")


def test_fail_closed_scope() -> None:
    module = load_module()
    out = module.build_result()
    if out["relative_action_marker_interval"] != "pi*hbar":
        raise AssertionError("Wrong relative action-marker interval")
    if out["relative_FS_budget"] != "pi*hbar/2":
        raise AssertionError("Wrong FS budget")
    if out["relative_action_to_FS_budget_ratio"] != "2":
        raise AssertionError("Action/FS ratio was not computed as 2")
    if out["orthogonality_character_root"] != {"real": "-1", "imaginary": "0"}:
        raise AssertionError("Wrong computed orthogonality root")
    if out["relative_action_marker_equals_two_FS_budgets"] is not True:
        raise AssertionError("Factor-two bridge was not established")
    for false_flag in (
        "unique_primitive_carrier_derived",
        "bloch_ball_derived",
        "M2C_algebra_derived",
        "primitive_unit_winding_derived_here",
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
    ):
        if out[false_flag] is not False:
            raise AssertionError(f"Premature promotion: {false_flag}")
    try:
        module.require(False, "sentinel")
    except RuntimeError:
        pass
    else:
        raise AssertionError("Fail-closed require did not raise")


def test_representation_mutations_fail_closed() -> None:
    mutations = (
        ("U_HALF_TURN", ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))),
        ("READY_NUM", (Fraction(1), Fraction(2))),
        (
            "CENTERED_GENERATOR",
            ((Fraction(-1), Fraction(0)), (Fraction(0), Fraction(1))),
        ),
        ("CHARACTER_WINDING", 2),
        ("ACTION_PERIOD_PI_UNITS", 4),
        ("DECLARED_COMPARISON_PLANE_COUNT", 2),
        ("PURE_READY_STATE_DECLARED", False),
        ("BALANCED_GEODESIC_SCOPE_DECLARED", False),
        ("UNIT_CHARACTER_MODULUS_SQUARED", Fraction(4)),
        (
            "COMMON_PHASE_I",
            (((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0))),
             ((Fraction(0), Fraction(0)), (Fraction(1), Fraction(0)))),
        ),
    )
    for name, value in mutations:
        module = load_module()
        setattr(module, name, value)
        try:
            module.build_result()
        except RuntimeError:
            continue
        raise AssertionError(f"Malformed {name} mutation passed")


def test_root_solver_mutation_fails_closed() -> None:
    module = load_module()
    module.solve_orthogonality_root = lambda: (
        Fraction(1, 2),
        Fraction(1),
        Fraction(0),
    )
    try:
        module.build_result()
    except RuntimeError:
        pass
    else:
        raise AssertionError("Altered orthogonality root passed")


def test_subprocess_result_matches_direct_result() -> None:
    completed = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    if "PASS_PRIMITIVE_ACTION_CHARACTER_FS_BRIDGE_PHYSICAL_ACTION_OPEN" not in completed.stdout:
        raise AssertionError("Unexpected subprocess status")
    stored = json.loads(RESULT.read_text(encoding="utf-8"))
    direct = load_module().build_result()
    if stored != direct:
        raise AssertionError("Stored result differs from direct result")
