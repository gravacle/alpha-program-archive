#!/usr/bin/env python3
"""Tests for comparator v006 (generation G7): pins, prologue hoist, scope.

This suite covers the FOUR enumerated v006 deltas and nothing else, because
nothing else changed: the numerical gates, tolerances, reconstruction oracle
and verdict rules are byte-identical to comparator v005, and that claim is
itself driven here by test_v006_diff_scope_is_exactly_the_enumerated_deltas
(discipline rule 4 -- a prose claim of byte-identity is a checkable claim).
The v005 numerics regressions therefore remain the coverage of record for
those regions and are NOT re-run here.

  test_pins_name_one_generation                 items 1 and 2
  test_provenance_prologue_blocks_without_consuming_the_output_path
                                                item 3, manifest leg
  test_prologue_blocks_a_launcher_skew_without_consuming_the_output_path
                                                item 3, the B1 wedge leg
  test_enforcement_point_still_asserts_the_same_equalities
                                                item 3, condition-identity
  test_v006_diff_scope_is_exactly_the_enumerated_deltas
                                                items 1-4, scope

NO STUB COMPONENT is used: the comparator is the real module, loaded from a
disposable workspace copy, and the runtime is the real launcher.  Two legs
supply FIXTURE BUNDLE JSON -- input data carrying the four provenance fields
the prologue reads -- which is data, not a substitute component; the leg's
whole point is that the prologue rejects those bundles before any bundle
content is loaded at all.

Never writes to, and never chmods, the canonical workspace.
"""

from __future__ import annotations

import ast
import difflib
import hashlib
import importlib.util
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
PINNED_PYTHON = Path(
    "/Users/bgm/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/python/bin/python3"
)
COMPARATOR_V005_RELATIVE = (
    "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
    "v005.py"
)
COMPARATOR_RELATIVE = (
    "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
    "v006.py"
)
LAUNCHER_RELATIVE = "scripts/launch_stage8_t7_content_addressed_runtime_v007.py"
BUILDER_RELATIVE = (
    "scripts/build_stage8_t7_actual_parent_car_implementation_manifest_v006.py"
)
MANIFEST_RELATIVE = (
    "provenance/"
    "stage8_t7_actual_parent_regulated_car_operator_response_implementation_"
    "v006.json"
)
BRIDGE_MANIFEST_RELATIVE = (
    "provenance/"
    "stage8_t7_actual_parent_regulated_car_operator_response_implementation_"
    "v001.json"
)
EXPECTED_MANIFEST_PIN = MANIFEST_RELATIVE
EXPECTED_LAUNCHER_PIN = LAUNCHER_RELATIVE
FENCED_RELATIVES = ("stage8_execution/work", "provenance")
AT_REST_MODE = 0o555
RUNTIME_MARKER = "_stage8_t7_content_addressed_runtime_v001"
COPY_EXCLUDES = (".proof_deps", ".pytest_cache", ".git", ".git_disabled")

# The enumerated v006 deltas, as markers.  Every changed region of the file
# must contain one of these, and every marker must be exercised.
ENUMERATED_DELTA_MARKERS = (
    # the v006 header (items 1-4 enumerated in prose)
    "v006 — GENERATION G7 COMPARATOR",
    # item 1: the manifest pin and its explanatory comment
    "v006 item 1:",
    "implementation_v006.json",
    # item 2: the launcher repoint and its explanatory comment
    "v006 item 2 (FUNCTIONAL CHANGE)",
    "runtime_v007.py",
    # item 3: the provenance prologue and its wiring
    "def verify_provenance_prologue",
    "v006 item 3: PROVENANCE PROLOGUE",
    "verify_provenance_prologue(independent_json, primary_json)",
    # item 4: the stale-comment sweep
    "STALE-COMMENT",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def scratch_directory(label: str) -> Path:
    base = os.environ.get("STAGE8_T7_TEST_SCRATCH")
    if base:
        Path(base).mkdir(parents=True, exist_ok=True)
    return Path(
        tempfile.mkdtemp(prefix=f"stage8_t7_compare_v006_{label}_", dir=base)
    ).resolve()


def copy_workspace(label: str) -> Path:
    destination = scratch_directory(label) / "workspace"
    shutil.copytree(
        ROOT,
        destination,
        symlinks=True,
        ignore=shutil.ignore_patterns(*COPY_EXCLUDES),
    )
    for relative in FENCED_RELATIVES:
        (destination / relative).chmod(AT_REST_MODE)
    return destination


def build_manifest(workspace: Path) -> str:
    completed = subprocess.run(
        [
            str(PINNED_PYTHON),
            "-I",
            "-S",
            str(workspace / LAUNCHER_RELATIVE),
            BUILDER_RELATIVE,
            "--l4-raise-and-record",
        ],
        cwd=workspace,
        check=False,
        capture_output=True,
        text=True,
    )
    require(
        completed.returncode == 0,
        f"manifest builder failed: {completed.stderr[-3000:]}",
    )
    return str(json.loads(completed.stdout)["manifest_sha256"])


def load_comparator(workspace: Path):
    path = workspace / COMPARATOR_RELATIVE
    name = f"comparator_v006_under_test_{abs(hash(str(path)))}"
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, "unable to load comparator")
    module = importlib.util.module_from_spec(spec)
    # Register before exec: the comparator declares a @dataclass, which
    # resolves its own module from sys.modules.
    sys.modules[name] = module
    spec.loader.exec_module(module)
    require(module.ROOT == workspace, "comparator ROOT is not the disposable copy")
    return module


def expect_blocked(action: Callable[[], Any], fragment: str, label: str) -> str:
    try:
        action()
    except Exception as error:  # ComparisonBlocked is a RuntimeError subclass
        require(
            fragment in str(error),
            f"{label}: blocked, but not on {fragment!r}: {error}",
        )
        return str(error)
    raise RuntimeError(f"{label}: expected a block; none was raised")


def test_pins_name_one_generation() -> None:
    workspace = copy_workspace("pins")
    module = load_comparator(workspace)
    require(
        str(module.IMPLEMENTATION_MANIFEST.relative_to(workspace))
        == EXPECTED_MANIFEST_PIN,
        "comparator v006 does not pin the generation-G7 manifest: "
        f"{module.IMPLEMENTATION_MANIFEST}",
    )
    require(
        module.RUNTIME_LAUNCHER_PATH == EXPECTED_LAUNCHER_PIN,
        "comparator v006 does not pin the generation-G7 launcher: "
        f"{module.RUNTIME_LAUNCHER_PATH}",
    )
    require(
        str(module.BUNDLE_BINDING_MANIFEST.relative_to(workspace))
        == BRIDGE_MANIFEST_RELATIVE,
        "comparator v006 lost the v001-path bridge binding: "
        f"{module.BUNDLE_BINDING_MANIFEST}",
    )
    for lane, executor in module.EXECUTOR_PATHS.items():
        require(
            executor.endswith("_v002.py"),
            f"comparator v006 repointed the byte-frozen {lane} lane: {executor}",
        )
    shutil.rmtree(workspace.parent, ignore_errors=True)


def bundle_fixture(
    workspace: Path,
    lane: str,
    *,
    stamp: str,
    executor_sha256: str,
    launcher_sha256: str,
    target_sha256: str,
) -> Path:
    """Write a bundle JSON carrying exactly the four provenance fields the
    prologue reads.  This is INPUT DATA, not a substitute component: the
    prologue must reject it before any bundle content is loaded."""
    work = workspace / "stage8_execution/work"
    work.chmod(0o755)
    path = work / f"fixture_{lane}_provenance_bundle.json"
    path.write_text(
        json.dumps(
            {
                "lane": lane,
                "implementation_manifest_sha256": stamp,
                "executor_sha256": executor_sha256,
                "runtime_attestation": {
                    "schema": (
                        "stage8_t7_content_addressed_runtime_attestation_v001"
                    ),
                    "launcher_sha256": launcher_sha256,
                    "target_sha256": target_sha256,
                },
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    work.chmod(AT_REST_MODE)
    return path


def test_provenance_prologue_blocks_without_consuming_the_output_path() -> None:
    """Item 3, manifest leg: an unsealed/absent own manifest must RAISE, not
    seal a BLOCKED verdict at the canonical comparison path.

    In v005 verify_implementation_manifest() ran inside the try whose except
    clause sealed the blocked payload, so this exact condition consumed the
    canonical path on the first production run.
    """
    workspace = copy_workspace("prologue_manifest")
    module = load_comparator(workspace)
    output = workspace / "stage8_execution/work/prologue_leg_output.json"
    # The G7 manifest has deliberately NOT been built in this copy, so the
    # comparator's own authority is absent.
    require(
        not (workspace / MANIFEST_RELATIVE).exists(),
        "fixture error: the manifest should be absent for this leg",
    )
    (workspace / "stage8_execution/work").chmod(0o755)
    try:
        expect_blocked(
            lambda: module.compare_bundles(
                independent_json=workspace / "absent_independent.json",
                independent_npz=workspace / "absent_independent.npz",
                primary_json=workspace / "absent_primary.json",
                primary_npz=workspace / "absent_primary.npz",
                independent_json_sha256="0" * 64,
                independent_npz_sha256="1" * 64,
                primary_json_sha256="2" * 64,
                primary_npz_sha256="3" * 64,
                output=output,
                independent_receipt_sha256="4" * 64,
                primary_receipt_sha256="5" * 64,
                controller_context="prologue-hoist-test",
            ),
            "implementation manifest missing",
            "an absent own manifest must raise from the prologue",
        )
    finally:
        (workspace / "stage8_execution/work").chmod(AT_REST_MODE)
    require(
        not output.exists(),
        "HOIST FAILURE: the prologue leg consumed the canonical output path: "
        f"{output}",
    )
    require(
        not Path(f"{output}.seal.sha256").exists(),
        "HOIST FAILURE: the prologue leg sealed an output",
    )
    shutil.rmtree(workspace.parent, ignore_errors=True)


def test_prologue_blocks_a_launcher_skew_without_consuming_the_output_path() -> None:
    """Item 3, THE B1 WEDGE LEG.

    A bundle whose attestation records a launcher other than the generation's
    launcher is the precise condition that would have sealed a BLOCKED
    verdict at the canonical comparison path on the first production run.
    Here it must RAISE from the prologue with the output path untouched.
    """
    workspace = copy_workspace("prologue_launcher")
    build_manifest(workspace)
    module = load_comparator(workspace)
    manifest = json.loads(
        (workspace / MANIFEST_RELATIVE).read_text(encoding="utf-8")
    )
    rows = {str(row["path"]): str(row["sha256"]) for row in manifest["files"]}
    bridge = json.loads(
        (workspace / BRIDGE_MANIFEST_RELATIVE).read_text(encoding="utf-8")
    )
    bridge_digest = sha256(workspace / BRIDGE_MANIFEST_RELATIVE)
    del bridge
    independent = bundle_fixture(
        workspace,
        "independent",
        stamp=bridge_digest,
        executor_sha256=rows[module.EXECUTOR_PATHS["independent"]],
        # THE SKEW: launcher v006's digest instead of the generation's.
        launcher_sha256=sha256(
            workspace
            / "scripts/launch_stage8_t7_content_addressed_runtime_v006.py"
        ),
        target_sha256=rows[module.EXECUTOR_PATHS["independent"]],
    )
    primary = bundle_fixture(
        workspace,
        "primary",
        stamp=bridge_digest,
        executor_sha256=rows[module.EXECUTOR_PATHS["primary"]],
        launcher_sha256=rows[LAUNCHER_RELATIVE],
        target_sha256=rows[module.EXECUTOR_PATHS["primary"]],
    )
    output = workspace / "stage8_execution/work/launcher_skew_output.json"
    (workspace / "stage8_execution/work").chmod(0o755)
    try:
        expect_blocked(
            lambda: module.compare_bundles(
                independent_json=independent,
                independent_npz=workspace / "absent_independent.npz",
                primary_json=primary,
                primary_npz=workspace / "absent_primary.npz",
                independent_json_sha256="0" * 64,
                independent_npz_sha256="1" * 64,
                primary_json_sha256="2" * 64,
                primary_npz_sha256="3" * 64,
                output=output,
                independent_receipt_sha256="4" * 64,
                primary_receipt_sha256="5" * 64,
                controller_context="b1-wedge-leg",
            ),
            "provenance prologue: independent runtime-launcher provenance "
            "mismatch",
            "a launcher skew must raise from the prologue",
        )
    finally:
        (workspace / "stage8_execution/work").chmod(AT_REST_MODE)
    require(
        not output.exists(),
        "B1 REGRESSION: a launcher skew consumed the canonical output path: "
        f"{output}",
    )
    require(
        not Path(f"{output}.seal.sha256").exists(),
        "B1 REGRESSION: a launcher skew sealed an output",
    )
    shutil.rmtree(workspace.parent, ignore_errors=True)


def test_enforcement_point_still_asserts_the_same_equalities() -> None:
    """Condition-identity (A3): hoisting must not REMOVE the enforcement.

    The four per-bundle equalities must still be asserted inside
    compare_bundles' own loop, against the hashed read-once buffers.  A hoist
    that moved them out instead of duplicating them would weaken the
    comparator, so this test reads the enforcement point itself.
    """
    source = (ROOT / COMPARATOR_RELATIVE).read_text(encoding="utf-8")
    tree = ast.parse(source)
    compare_bundles = None
    prologue = None
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            if node.name == "compare_bundles":
                compare_bundles = node
            if node.name == "verify_provenance_prologue":
                prologue = node
    require(compare_bundles is not None, "compare_bundles is absent")
    require(prologue is not None, "verify_provenance_prologue is absent")
    assert compare_bundles is not None and prologue is not None

    def segment(node: ast.AST) -> str:
        return ast.get_source_segment(source, node) or ""

    enforcement_body = ""
    for node in ast.walk(compare_bundles):
        if isinstance(node, ast.Try):
            enforcement_body += segment(node)
    prologue_body = segment(prologue)
    equalities = (
        'get("implementation_manifest_sha256")',
        'get("executor_sha256")',
        'get("launcher_sha256")',
        'get("target_sha256")',
    )
    for equality in equalities:
        require(
            equality in enforcement_body,
            f"the enforcement point no longer asserts {equality}; a hoist may "
            "duplicate a condition but may never remove it",
        )
        require(
            equality in prologue_body,
            f"the prologue does not assert {equality}; the hoist is not "
            "condition-identical",
        )
    # The prologue must be CALLED before the try, not inside it.
    prologue_calls = [
        node.lineno
        for node in ast.walk(compare_bundles)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "verify_provenance_prologue"
    ]
    try_lines = [
        node.lineno for node in ast.walk(compare_bundles) if isinstance(node, ast.Try)
    ]
    require(len(prologue_calls) == 1, f"expected one prologue call: {prologue_calls}")
    require(bool(try_lines), "compare_bundles has no try block")
    require(
        prologue_calls[0] < min(try_lines),
        f"HOIST FAILURE: the prologue is called at line {prologue_calls[0]}, "
        f"inside or after the try at line {min(try_lines)}",
    )


def test_v006_diff_scope_is_exactly_the_enumerated_deltas() -> None:
    """Rule 4: the header claims byte-identity outside four deltas.

    Every changed region between v005 and v006 must contain one of the
    enumerated delta markers, and every marker must appear in some changed
    region.  A fifth, unenumerated change therefore fails this test.
    """
    old = (ROOT / COMPARATOR_V005_RELATIVE).read_text(encoding="utf-8").splitlines(
        keepends=True
    )
    new = (ROOT / COMPARATOR_RELATIVE).read_text(encoding="utf-8").splitlines(
        keepends=True
    )
    matcher = difflib.SequenceMatcher(a=old, b=new, autojunk=False)
    unexplained: list[str] = []
    used: set[str] = set()
    regions = 0
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        regions += 1
        changed = "".join(new[j1:j2]) + "".join(old[i1:i2])
        matched = [
            marker for marker in ENUMERATED_DELTA_MARKERS if marker in changed
        ]
        if not matched:
            unexplained.append(
                f"[{tag} old {i1}:{i2} new {j1}:{j2}] {changed[:400]!r}"
            )
        used.update(matched)
    require(
        not unexplained,
        "UNENUMERATED CHANGE between comparator v005 and v006 (the header "
        "claims byte-identity outside the four enumerated deltas): "
        + "\n".join(unexplained),
    )
    unused = sorted(set(ENUMERATED_DELTA_MARKERS) - used)
    require(
        not unused,
        f"enumerated deltas that do not appear in any changed region: {unused}",
    )
    require(regions > 0, "v006 is byte-identical to v005; the deltas are absent")


def main() -> int:
    # This suite must be LAUNCHED (it is an allowlisted target of launcher
    # v007): the comparator's prologue asserts the runtime attestation first,
    # so a bare invocation could not exercise the prologue at all.  There is
    # deliberately no self-re-exec here -- re-execing would drop the marker.
    require(
        isinstance(getattr(sys, RUNTIME_MARKER, None), dict),
        "this suite must run under the sealed runtime launcher: "
        f"{PINNED_PYTHON} -I -S {LAUNCHER_RELATIVE} "
        f"{SELF.relative_to(ROOT)}",
    )
    tests = (
        test_pins_name_one_generation,
        test_enforcement_point_still_asserts_the_same_equalities,
        test_v006_diff_scope_is_exactly_the_enumerated_deltas,
        test_provenance_prologue_blocks_without_consuming_the_output_path,
        test_prologue_blocks_a_launcher_skew_without_consuming_the_output_path,
    )
    for test in tests:
        test()
        print(f"PASS {test.__name__}", flush=True)
    print(f"comparator_v006_tests_passed {len(tests)}/{len(tests)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
