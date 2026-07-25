"""Hostile mutation tests for the snapshot-bound V013 authority delta."""

from __future__ import annotations

import copy
from contextlib import redirect_stdout
from dataclasses import replace
import hashlib
import inspect
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import sys
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_current_authority_v013.py"
LEDGER = ROOT / "CURRENT_AUTHORITY_LEDGER_V013.json"


def load_module():
    name = "authority_v013_under_test"
    spec = importlib.util.spec_from_file_location(name, SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load V013 authority audit")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def expect_runtime_error(callback, label: str) -> None:
    try:
        callback()
    except RuntimeError:
        return
    raise AssertionError(f"Fail-closed audit accepted: {label}")


def expect_type_error(callback, label: str) -> None:
    try:
        callback()
    except TypeError:
        return
    raise AssertionError(f"Removed interface remained callable: {label}")


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def ledger_data() -> dict:
    return json.loads(LEDGER.read_text(encoding="utf-8"))


def mutate_value(value):
    if type(value) is bool:
        return not value
    if type(value) is int:
        return value + 1
    if type(value) is str:
        return value + "_MUTATED"
    if type(value) is list:
        return value + ["MUTATED"]
    raise AssertionError(f"Unhandled mutation type: {type(value).__name__}")


def clone_authority_tree(module, destination: Path) -> Path:
    destination.mkdir()
    for name in sorted(set(module.authority_role_paths().values())):
        source = ROOT / name
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    return destination


def replace_snapshot_bytes(module, snapshot, data: bytes):
    return replace(
        snapshot,
        data=data,
        digest=hashlib.sha256(data).hexdigest(),
    )


def replace_json_snapshot(module, snapshots, role: str, value: dict):
    changed = dict(snapshots)
    data = json.dumps(value, indent=2, ensure_ascii=True).encode("utf-8") + b"\n"
    changed[role] = replace_snapshot_bytes(module, snapshots[role], data)
    return changed


def evaluate_with_ledger(module, value: dict):
    snapshots = module.collect_authority_snapshots(ROOT)
    return module.evaluate_snapshots(
        replace_json_snapshot(module, snapshots, "current.ledger", value)
    )


def reseal_raw_snapshot_pair(
    module,
    snapshots,
    target_role: str,
    seal_role: str,
    target_data: bytes,
):
    changed = dict(snapshots)
    changed[target_role] = replace_snapshot_bytes(
        module,
        snapshots[target_role],
        target_data,
    )
    seal_data = (
        f"{changed[target_role].digest}  "
        f"{Path(changed[target_role].name).name}\n"
    ).encode("utf-8")
    changed[seal_role] = replace_snapshot_bytes(
        module,
        snapshots[seal_role],
        seal_data,
    )
    return changed


def reseal_snapshot_pair(module, snapshots, target_name: str, value: dict):
    target_role = module._role_for_new_target(target_name)
    seal_role = module._role_for_new_seal(target_name)
    target_data = (
        json.dumps(value, indent=2, ensure_ascii=True).encode("utf-8") + b"\n"
    )
    return reseal_raw_snapshot_pair(
        module,
        snapshots,
        target_role,
        seal_role,
        target_data,
    )


def reseal_file(module, root: Path, target_name: str) -> None:
    target = root / target_name
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    seal = root / module.NEW_SEALED_INPUTS[target_name]
    seal.write_text(
        f"{digest}  {Path(target_name).name}\n",
        encoding="utf-8",
    )


def reseal_parent_file(module, root: Path, role: str) -> None:
    target_name = module.EXPECTED_PARENT_AUTHORITY[role]
    seal_name = module.EXPECTED_PARENT_AUTHORITY[f"{role}_seal"]
    target = root / target_name
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    (root / seal_name).write_text(
        f"{digest}  {Path(target_name).name}\n",
        encoding="utf-8",
    )


def test_nominal_snapshot_semantics_and_stored_result_parity() -> None:
    module = load_module()
    snapshots = module.collect_authority_snapshots(ROOT)
    computed = module.evaluate_snapshots(snapshots)
    stored = module.load_json_snapshot(
        snapshots["current.result"],
        "stored V013 result",
    )
    module.validate_result_parity(stored, computed)
    check(computed["verified_authority_roles"] == 54, "Wrong authority-role count")
    check(computed["verified_unique_role_inodes"] == 54, "Wrong inode count")
    check(
        computed["verified_single_link_authority_roles"] == 54,
        "Wrong single-link role count",
    )
    check(
        computed["verified_approved_artifact_digests"] == 40,
        "Wrong approved-digest count",
    )
    check(
        computed["verified_parent_execution_state_keys"] == 53,
        "Wrong parent-state count",
    )
    check(
        computed["verified_effective_execution_state_keys"] == 71,
        "Wrong effective-state count",
    )
    check(computed["verified_subordinate_results"] == 4, "Wrong subordinate count")
    check(
        computed["verified_subordinate_result_fields"] == 109,
        "Wrong subordinate-field count",
    )
    check(computed["alpha_computed"] is False, "Alpha promoted")
    check(computed["proof_authorized"] is False, "Proof authorized")


def test_caller_supplied_ledger_bypass_is_removed_and_main_uses_build() -> None:
    module = load_module()
    snapshots = module.collect_authority_snapshots(ROOT)
    fake_ledger = ledger_data()
    fake_ledger["execution_state_additions"][
        "complete_physical_write_operator_derived"
    ] = True

    check(
        list(inspect.signature(module.evaluate_snapshots).parameters) == ["snapshots"],
        "evaluate_snapshots still accepts caller semantic data",
    )
    check(
        list(inspect.signature(module.build_result).parameters) == ["root"],
        "build_result still accepts caller semantic data",
    )
    expect_type_error(
        lambda: module.evaluate_snapshots(snapshots, fake_ledger),
        "evaluate_snapshots caller-data injection",
    )
    expect_type_error(
        lambda: module.build_result(data=fake_ledger),
        "build_result caller-data injection",
    )

    changed = replace_json_snapshot(
        module,
        snapshots,
        "current.ledger",
        fake_ledger,
    )
    expect_runtime_error(
        lambda: module.evaluate_snapshots(changed),
        "mutated snapshotted ledger",
    )

    output = io.StringIO()
    with mock.patch.object(
        module,
        "build_result",
        return_value={"status": "CANONICAL_BUILD_SENTINEL"},
    ) as build:
        with redirect_stdout(output):
            module.main()
    check(build.call_count == 1, "main did not call build_result exactly once")
    check(
        output.getvalue().strip() == "CANONICAL_BUILD_SENTINEL",
        "main bypassed canonical build output",
    )


def test_target_and_seal_comutation_cannot_defeat_approved_digest_pins() -> None:
    module = load_module()
    baseline = module.collect_authority_snapshots(ROOT)
    check(
        set(module.APPROVED_SEALED_ARTIFACT_SHA256)
        == module.approved_sealed_artifact_paths(),
        "Approved digest inventory is incomplete",
    )
    check(
        len(module.APPROVED_SEALED_ARTIFACT_SHA256) == 40,
        "Approved digest inventory has the wrong size",
    )

    sealed_role_pairs = [
        (f"parent.{role}", f"parent.{role}_seal")
        for role in ("ledger", "audit", "test", "result")
    ]
    sealed_role_pairs.extend(
        (
            module._role_for_new_target(target_name),
            module._role_for_new_seal(target_name),
        )
        for target_name in module.NEW_SEALED_INPUTS
    )
    check(len(sealed_role_pairs) == 20, "Wrong sealed target/seal pair count")

    for target_role, seal_role in sealed_role_pairs:
        changed = reseal_raw_snapshot_pair(
            module,
            baseline,
            target_role,
            seal_role,
            baseline[target_role].data
            + b"\nHOSTILE_CO_MUTATION\n",
        )
        expect_runtime_error(
            lambda changed=changed: module.evaluate_snapshots(changed),
            f"co-mutated pinned target and seal: {target_role}",
        )

    for _, seal_role in sealed_role_pairs:
        seal_only = dict(baseline)
        seal_only[seal_role] = replace_snapshot_bytes(
            module,
            baseline[seal_role],
            baseline[seal_role].data + b"\n",
        )
        expect_runtime_error(
            lambda seal_only=seal_only: module.evaluate_snapshots(seal_only),
            f"semantically equivalent but unapproved seal bytes: {seal_role}",
        )


def test_build_result_is_canonical_and_enforces_stored_parity(
    tmp_path: Path,
) -> None:
    module = load_module()
    tree = clone_authority_tree(module, tmp_path / "authority")
    result_path = tree / "results" / "current_authority_v013.json"
    result = json.loads(result_path.read_text(encoding="utf-8"))
    result["verified_authority_roles"] += 1
    result_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    snapshots = module.collect_authority_snapshots(tree)
    computed_without_parity = module.evaluate_snapshots(snapshots)
    check(
        computed_without_parity["verified_authority_roles"] == 54,
        "Core snapshot evaluation was influenced by stored result",
    )
    expect_runtime_error(
        lambda: module.build_result(root=tree),
        "canonical build accepted stored-result drift",
    )


def test_exact_ledger_schema_maps_and_strict_booleans_fail_closed() -> None:
    module = load_module()
    original = ledger_data()

    unknown_top = copy.deepcopy(original)
    unknown_top["unreviewed_authority"] = True
    expect_runtime_error(
        lambda: evaluate_with_ledger(module, unknown_top),
        "unknown top-level key",
    )

    missing_top = copy.deepcopy(original)
    missing_top.pop("subordinate_result_bindings")
    expect_runtime_error(
        lambda: evaluate_with_ledger(module, missing_top),
        "missing top-level key",
    )

    for section in (
        "current_authority",
        "parent_authority",
        "new_sealed_results",
        "subordinate_result_bindings",
        "new_level_1_postulates",
        "superseded_or_rejected_since_v010",
        "execution_state_additions",
        "protected_parent_flags",
    ):
        emptied = copy.deepcopy(original)
        emptied[section] = {}
        expect_runtime_error(
            lambda emptied=emptied: evaluate_with_ledger(module, emptied),
            f"empty {section}",
        )

        unknown = copy.deepcopy(original)
        unknown[section]["unknown_role_or_claim"] = False
        expect_runtime_error(
            lambda unknown=unknown: evaluate_with_ledger(module, unknown),
            f"unknown key in {section}",
        )

    for section in ("execution_state_additions", "protected_parent_flags"):
        for key, value in original[section].items():
            changed = copy.deepcopy(original)
            changed[section][key] = not value
            expect_runtime_error(
                lambda changed=changed: evaluate_with_ledger(module, changed),
                f"{section}.{key} boolean flip",
            )
            integer = copy.deepcopy(original)
            integer[section][key] = int(value)
            expect_runtime_error(
                lambda integer=integer: evaluate_with_ledger(module, integer),
                f"{section}.{key} bool-to-int",
            )


def test_absolute_escape_and_symlink_roles_fail_closed(tmp_path: Path) -> None:
    module = load_module()
    original = ledger_data()

    absolute = copy.deepcopy(original)
    absolute["parent_authority"]["ledger"] = str(
        (ROOT / "CURRENT_AUTHORITY_LEDGER_V010.json").resolve()
    )
    expect_runtime_error(
        lambda: evaluate_with_ledger(module, absolute),
        "absolute authority path",
    )

    escaping = copy.deepcopy(original)
    escaping["parent_authority"]["ledger"] = "../CURRENT_AUTHORITY_LEDGER_V010.json"
    expect_runtime_error(
        lambda: evaluate_with_ledger(module, escaping),
        "parent traversal",
    )

    tree = clone_authority_tree(module, tmp_path / "authority")
    target = tree / "results" / "current_authority_v010.json"
    target.unlink()
    target.symlink_to(ROOT / "results" / "current_authority_v010.json")
    expect_runtime_error(
        lambda: module.collect_authority_snapshots(tree),
        "symlinked authority role",
    )


def test_hardlink_inode_alias_across_authority_roles_fails(tmp_path: Path) -> None:
    module = load_module()
    tree = clone_authority_tree(module, tmp_path / "authority")
    first = tree / "CURRENT_AUTHORITY_LEDGER_V012.json"
    second = tree / "results" / "current_authority_v012.json"
    second.unlink()
    os.link(first, second)
    expect_runtime_error(
        lambda: module.collect_authority_snapshots(tree),
        "hardlink authority-role alias",
    )


def test_single_link_rule_rejects_external_and_mid_snapshot_hardlinks(
    tmp_path: Path,
) -> None:
    module = load_module()

    tree = clone_authority_tree(module, tmp_path / "authority")
    authority_file = tree / "results" / "current_authority_v013.json"
    os.link(authority_file, tmp_path / "external_alias.json")
    expect_runtime_error(
        lambda: module.collect_authority_snapshots(tree),
        "authority file with an external hardlink",
    )

    race_root = tmp_path / "race"
    race_root.mkdir()
    race_file = race_root / "artifact.bin"
    race_file.write_bytes(b"stable snapshot payload")
    race_alias = tmp_path / "race_alias.bin"
    real_read = module.os.read
    linked = {"done": False}

    def read_after_link(fd, size):
        if not linked["done"]:
            os.link(race_file, race_alias)
            linked["done"] = True
        return real_read(fd, size)

    with mock.patch.object(module.os, "read", side_effect=read_after_link):
        expect_runtime_error(
            lambda: module.snapshot_regular_file(
                race_root,
                "artifact.bin",
                "mid-snapshot-hardlink",
            ),
            "hardlink created during snapshot",
        )
    check(linked["done"], "mid-snapshot hardlink attack did not execute")


def test_complete_parent_state_resealed_promotions_and_key_drift_fail(
    tmp_path: Path,
) -> None:
    module = load_module()

    promoted_tree = clone_authority_tree(module, tmp_path / "promoted")
    parent_path = promoted_tree / "CURRENT_AUTHORITY_LEDGER_V010.json"
    parent = json.loads(parent_path.read_text(encoding="utf-8"))
    check(len(parent["execution_state"]) == 53, "Parent fixture is not 53 keys")
    parent["execution_state"]["physical_public_EM_connection_derived"] = True
    parent_path.write_text(json.dumps(parent, indent=2) + "\n", encoding="utf-8")
    reseal_parent_file(module, promoted_tree, "ledger")
    expect_runtime_error(
        lambda: module.build_result(root=promoted_tree),
        "resealed nonprotected parent promotion",
    )

    drift_tree = clone_authority_tree(module, tmp_path / "key_drift")
    parent_path = drift_tree / "CURRENT_AUTHORITY_LEDGER_V010.json"
    parent = json.loads(parent_path.read_text(encoding="utf-8"))
    inherited = parent["execution_state"].pop(
        "source_branch_charge_basis_corrected"
    )
    parent["execution_state"]["unknown_parent_claim_same_count"] = inherited
    check(len(parent["execution_state"]) == 53, "Key substitution changed count")
    parent_path.write_text(json.dumps(parent, indent=2) + "\n", encoding="utf-8")
    reseal_parent_file(module, drift_tree, "ledger")
    expect_runtime_error(
        lambda: module.build_result(root=drift_tree),
        "resealed same-count parent key substitution",
    )


def test_all_subordinate_fields_are_exact_and_resealed_promotions_fail() -> None:
    module = load_module()
    baseline = module.collect_authority_snapshots(ROOT)

    for label, target_name in module.EXPECTED_SUBORDINATE_BINDINGS.items():
        expected = module.EXPECTED_SUBORDINATE_RESULTS[label]
        for key, value in expected.items():
            mutated = copy.deepcopy(expected)
            mutated[key] = mutate_value(value)
            expect_runtime_error(
                lambda mutated=mutated, expected=expected, label=label:
                    module.validate_exact_map(
                        mutated,
                        expected,
                        f"subordinate result {label}",
                    ),
                f"exact subordinate field mutation {label}.{key}",
            )
            snapshots = reseal_snapshot_pair(
                module,
                baseline,
                target_name,
                mutated,
            )
            expect_runtime_error(
                lambda snapshots=snapshots: module.evaluate_snapshots(snapshots),
                f"resealed subordinate field mutation {label}.{key}",
            )

        missing = copy.deepcopy(expected)
        missing.pop(next(iter(missing)))
        expect_runtime_error(
            lambda missing=missing, expected=expected, label=label:
                module.validate_exact_map(
                    missing,
                    expected,
                    f"subordinate result {label}",
                ),
            f"exact missing subordinate field {label}",
        )
        snapshots = reseal_snapshot_pair(module, baseline, target_name, missing)
        expect_runtime_error(
            lambda snapshots=snapshots: module.evaluate_snapshots(snapshots),
            f"missing subordinate field {label}",
        )

        unknown = copy.deepcopy(expected)
        unknown["unknown_claim"] = False
        expect_runtime_error(
            lambda unknown=unknown, expected=expected, label=label:
                module.validate_exact_map(
                    unknown,
                    expected,
                    f"subordinate result {label}",
                ),
            f"exact unknown subordinate field {label}",
        )
        snapshots = reseal_snapshot_pair(module, baseline, target_name, unknown)
        expect_runtime_error(
            lambda snapshots=snapshots: module.evaluate_snapshots(snapshots),
            f"unknown subordinate field {label}",
        )

    flux_name = module.EXPECTED_SUBORDINATE_BINDINGS[
        "conditional_source_flux_record_holonomy"
    ]
    promoted_flux = copy.deepcopy(
        module.EXPECTED_SUBORDINATE_RESULTS[
            "conditional_source_flux_record_holonomy"
        ]
    )
    promoted_flux["alpha_computed"] = True
    promoted_flux["proof_authorized"] = True
    snapshots = reseal_snapshot_pair(
        module,
        baseline,
        flux_name,
        promoted_flux,
    )
    expect_runtime_error(
        lambda: module.evaluate_snapshots(snapshots),
        "resealed subordinate alpha/proof promotion",
    )


def test_semantic_parse_uses_the_same_snapshotted_bytes(tmp_path: Path) -> None:
    module = load_module()
    tree = clone_authority_tree(module, tmp_path / "authority")
    snapshots = module.collect_authority_snapshots(tree)
    before = module.evaluate_snapshots(snapshots)
    check(before["alpha_computed"] is False, "Baseline alpha was promoted")

    target_name = module.EXPECTED_SUBORDINATE_BINDINGS[
        "conditional_source_flux_record_holonomy"
    ]
    target = tree / target_name
    changed = json.loads(target.read_text(encoding="utf-8"))
    changed["alpha_computed"] = True
    target.write_text(json.dumps(changed, indent=2) + "\n", encoding="utf-8")
    reseal_file(module, tree, target_name)

    after_disk_mutation_from_old_snapshot = module.evaluate_snapshots(snapshots)
    check(
        after_disk_mutation_from_old_snapshot == before,
        "Semantic evaluation reread disk after snapshot",
    )
    expect_runtime_error(
        lambda: module.build_result(root=tree),
        "new snapshot sees resealed semantic promotion",
    )


def test_duplicate_json_keys_result_schema_and_every_parity_field_fail() -> None:
    module = load_module()
    expect_runtime_error(
        lambda: module.loads_strict(
            '{"alpha_computed": false, "alpha_computed": true}'
        ),
        "duplicate JSON key",
    )

    computed = module.build_result()
    for key, value in computed.items():
        mutated = copy.deepcopy(computed)
        mutated[key] = mutate_value(value)
        expect_runtime_error(
            lambda mutated=mutated: module.validate_result_parity(
                mutated,
                computed,
            ),
            f"stored result mutation {key}",
        )

    missing = copy.deepcopy(computed)
    missing.pop("proof_authorized")
    expect_runtime_error(
        lambda: module.validate_result_schema(missing),
        "missing result field",
    )
    unknown = copy.deepcopy(computed)
    unknown["unreviewed_success"] = True
    expect_runtime_error(
        lambda: module.validate_result_schema(unknown),
        "unknown result field",
    )
    wrong_type = copy.deepcopy(computed)
    wrong_type["alpha_computed"] = 0
    expect_runtime_error(
        lambda: module.validate_result_schema(wrong_type),
        "result bool-to-int",
    )


def test_require_remains_fail_closed_under_current_interpreter_mode() -> None:
    module = load_module()
    expect_runtime_error(
        lambda: module.require(False, "optimized-mode sentinel"),
        "require sentinel",
    )
