"""Mutation-sensitive checks for the V011 authority delta."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_current_authority_v011.py"
LEDGER = ROOT / "CURRENT_AUTHORITY_LEDGER_V011.json"


def load_module():
    spec = importlib.util.spec_from_file_location("authority_v011", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load V011 authority audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_nominal_authority_delta() -> None:
    module = load_module()
    result = module.build_result()
    if result["verified_new_seals"] != 16:
        raise AssertionError("Wrong new-seal count")
    if result["complete_source_record_environment_operator_derived"] is not False:
        raise AssertionError("Complete operator promoted")
    if result["alpha_computed"] is not False or result["proof_authorized"] is not False:
        raise AssertionError("Alpha/proof promoted")


def test_false_to_true_promotions_fail_closed() -> None:
    module = load_module()
    original = json.loads(LEDGER.read_text(encoding="utf-8"))
    false_keys = [
        key
        for key, value in original["execution_state_additions"].items()
        if value is False
    ]
    false_keys.extend(
        key
        for key, value in original["protected_parent_flags"].items()
        if value is False
    )
    for key in false_keys:
        mutated = copy.deepcopy(original)
        if key in mutated["execution_state_additions"]:
            mutated["execution_state_additions"][key] = True
        else:
            mutated["protected_parent_flags"][key] = True
        try:
            module.build_result(mutated)
        except RuntimeError:
            continue
        raise AssertionError(f"False-to-true promotion passed: {key}")


def test_missing_and_unknown_state_keys_fail_closed() -> None:
    module = load_module()
    original = json.loads(LEDGER.read_text(encoding="utf-8"))

    missing = copy.deepcopy(original)
    missing["execution_state_additions"].pop(
        "complete_source_record_environment_operator_derived"
    )
    try:
        module.build_result(missing)
    except RuntimeError:
        pass
    else:
        raise AssertionError("Missing addition key passed")

    unknown = copy.deepcopy(original)
    unknown["execution_state_additions"]["alpha_solved_by_wishful_thinking"] = True
    try:
        module.build_result(unknown)
    except RuntimeError:
        pass
    else:
        raise AssertionError("Unknown addition key passed")


def test_fail_closed_require_survives_optimized_mode() -> None:
    module = load_module()
    try:
        module.require(False, "sentinel")
    except RuntimeError:
        pass
    else:
        raise AssertionError("Fail-closed require did not raise")
