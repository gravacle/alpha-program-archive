"""Adversarial tests for the hardened V012 authority delta."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_current_authority_v012.py"
LEDGER = ROOT / "CURRENT_AUTHORITY_LEDGER_V012.json"
RESULT = ROOT / "results" / "current_authority_v012.json"


def load_module():
    spec = importlib.util.spec_from_file_location("authority_v012", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load V012 authority audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expect_runtime_error(callback, label: str) -> None:
    try:
        callback()
    except RuntimeError:
        return
    raise AssertionError(f"Fail-closed audit accepted: {label}")


def ledger_data():
    return json.loads(LEDGER.read_text(encoding="utf-8"))


def test_nominal_delta_and_stored_result_parity() -> None:
    module = load_module()
    computed = module.build_result()
    stored = module.load_json_file(RESULT, "stored V012 result")
    module.validate_result_parity(stored, computed)
    if computed["verified_parent_seals"] != 4:
        raise AssertionError("Wrong parent-seal count")
    if computed["verified_new_seals"] != 16:
        raise AssertionError("Wrong new-seal count")
    if computed["verified_effective_execution_state_keys"] != 71:
        raise AssertionError("Wrong effective-state key count")
    if computed["alpha_computed"] is not False:
        raise AssertionError("Alpha promoted")
    if computed["proof_authorized"] is not False:
        raise AssertionError("Proof authorized")


def test_all_false_to_true_and_bool_int_promotions_fail() -> None:
    module = load_module()
    original = ledger_data()
    for section in ("execution_state_additions", "protected_parent_flags"):
        for key, value in original[section].items():
            if value is False:
                promoted = copy.deepcopy(original)
                promoted[section][key] = True
                expect_runtime_error(
                    lambda promoted=promoted: module.build_result(promoted),
                    f"{section}.{key} false-to-true",
                )
                integer_false = copy.deepcopy(original)
                integer_false[section][key] = 0
                expect_runtime_error(
                    lambda integer_false=integer_false: module.build_result(integer_false),
                    f"{section}.{key} bool-to-int zero",
                )
            elif value is True:
                integer_true = copy.deepcopy(original)
                integer_true[section][key] = 1
                expect_runtime_error(
                    lambda integer_true=integer_true: module.build_result(integer_true),
                    f"{section}.{key} bool-to-int one",
                )


def test_exact_top_level_and_delta_maps_fail_closed() -> None:
    module = load_module()
    original = ledger_data()

    unknown_top = copy.deepcopy(original)
    unknown_top["alpha_authorized_elsewhere"] = True
    expect_runtime_error(lambda: module.build_result(unknown_top), "unknown top-level key")

    missing_top = copy.deepcopy(original)
    missing_top.pop("new_level_1_postulates")
    expect_runtime_error(lambda: module.build_result(missing_top), "missing top-level key")

    for section in (
        "new_sealed_results",
        "new_level_1_postulates",
        "superseded_or_rejected_since_v010",
        "execution_state_additions",
        "protected_parent_flags",
    ):
        emptied = copy.deepcopy(original)
        emptied[section] = {}
        expect_runtime_error(
            lambda emptied=emptied: module.build_result(emptied),
            f"empty {section}",
        )

    collision = copy.deepcopy(original)
    collision["execution_state_additions"]["alpha_computed"] = False
    expect_runtime_error(lambda: module.build_result(collision), "parent/addition collision")


def test_parent_roles_and_paths_are_exact_and_confined() -> None:
    module = load_module()
    original = ledger_data()

    role_collision = copy.deepcopy(original)
    for role in ("audit", "test", "result"):
        role_collision["parent_authority"][role] = (
            "CURRENT_AUTHORITY_LEDGER_V010.json"
        )
        role_collision["parent_authority"][f"{role}_seal"] = (
            "CURRENT_AUTHORITY_LEDGER_V010.seal.sha256"
        )
    expect_runtime_error(
        lambda: module.build_result(role_collision),
        "parent role collision",
    )

    absolute = copy.deepcopy(original)
    absolute["parent_authority"]["ledger"] = str(
        (ROOT / "CURRENT_AUTHORITY_LEDGER_V010.json").resolve()
    )
    expect_runtime_error(lambda: module.build_result(absolute), "absolute parent path")

    escaping = copy.deepcopy(original)
    escaping["parent_authority"]["ledger"] = "../CURRENT_AUTHORITY_LEDGER_V010.json"
    expect_runtime_error(lambda: module.build_result(escaping), "escaping parent path")

    with mock.patch.object(Path, "is_symlink", return_value=True):
        expect_runtime_error(
            lambda: module.confined_regular_file(
                "CURRENT_AUTHORITY_LEDGER_V010.json", "mock symlink"
            ),
            "symlinked path",
        )


def test_seal_role_and_parent_result_semantics_fail_closed() -> None:
    module = load_module()
    expect_runtime_error(
        lambda: module.verify_seal(
            "CURRENT_AUTHORITY_LEDGER_V010.json",
            "scripts/audit_current_authority_v010.seal.sha256",
        ),
        "wrong role seal",
    )

    bad_parent = copy.deepcopy(module.EXPECTED_PARENT_RESULT)
    bad_parent["alpha_computed"] = True
    expect_runtime_error(
        lambda: module.validate_exact_map(
            bad_parent, module.EXPECTED_PARENT_RESULT, "mutated parent result"
        ),
        "promoted parent result",
    )


def test_parent_state_and_result_inheritance_mutations_fail_closed() -> None:
    module = load_module()
    original_load = module.load_json_file
    parent_ledger = original_load(
        ROOT / "CURRENT_AUTHORITY_LEDGER_V010.json", "parent ledger fixture"
    )
    parent_result = original_load(
        ROOT / "results" / "current_authority_v010.json", "parent result fixture"
    )

    def run_with(parent_ledger_value, parent_result_value) -> None:
        def replacement(path, label):
            if path.name == "CURRENT_AUTHORITY_LEDGER_V010.json":
                return copy.deepcopy(parent_ledger_value)
            if path.name == "current_authority_v010.json":
                return copy.deepcopy(parent_result_value)
            return original_load(path, label)

        with mock.patch.object(module, "load_json_file", side_effect=replacement):
            module.build_result()

    promoted_state = copy.deepcopy(parent_ledger)
    promoted_state["execution_state"]["alpha_computed"] = True
    expect_runtime_error(
        lambda: run_with(promoted_state, parent_result),
        "parent state alpha promotion",
    )

    integer_state = copy.deepcopy(parent_ledger)
    integer_state["execution_state"]["alpha_computed"] = 0
    expect_runtime_error(
        lambda: run_with(integer_state, parent_result),
        "parent state boolean replaced by integer",
    )

    extra_state = copy.deepcopy(parent_ledger)
    extra_state["execution_state"]["unreviewed_parent_success"] = True
    expect_runtime_error(
        lambda: run_with(extra_state, parent_result),
        "parent state key addition",
    )

    promoted_result = copy.deepcopy(parent_result)
    promoted_result["alpha_computed"] = True
    expect_runtime_error(
        lambda: run_with(parent_ledger, promoted_result),
        "parent result alpha promotion",
    )


def test_duplicate_json_keys_and_result_schema_fail_closed() -> None:
    module = load_module()
    expect_runtime_error(
        lambda: module.loads_strict('{"alpha_computed": false, "alpha_computed": true}'),
        "duplicate JSON key",
    )

    valid = module.build_result()
    missing = copy.deepcopy(valid)
    missing.pop("proof_authorized")
    expect_runtime_error(
        lambda: module.validate_result_schema(missing),
        "missing result key",
    )

    unknown = copy.deepcopy(valid)
    unknown["unreviewed_success"] = True
    expect_runtime_error(
        lambda: module.validate_result_schema(unknown),
        "unknown result key",
    )

    wrong_type = copy.deepcopy(valid)
    wrong_type["alpha_computed"] = 0
    expect_runtime_error(
        lambda: module.validate_result_schema(wrong_type),
        "result boolean replaced by integer",
    )


def test_every_stored_result_field_mutation_breaks_parity() -> None:
    module = load_module()
    computed = module.build_result()
    for key, value in computed.items():
        mutated = copy.deepcopy(computed)
        if type(value) is bool:
            mutated[key] = not value
        elif type(value) is int:
            mutated[key] = value + 1
        elif type(value) is str:
            mutated[key] = value + "_MUTATED"
        else:
            raise AssertionError(f"Unhandled result type for mutation: {key}")
        expect_runtime_error(
            lambda mutated=mutated: module.validate_result_parity(
                mutated, computed
            ),
            f"stored result mutation: {key}",
        )


def test_fail_closed_require_survives_optimized_mode() -> None:
    module = load_module()
    expect_runtime_error(lambda: module.require(False, "sentinel"), "require sentinel")
