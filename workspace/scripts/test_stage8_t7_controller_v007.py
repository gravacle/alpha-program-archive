#!/usr/bin/env python3
"""Tests for controller v007 (generation G7): coherence, fence, A4 order.

DISCIPLINE POSITION OF THIS FILE.  Every test here drives REAL components:
the real controller v007 bytes, the real launcher v007, the real comparator
v006, the real manifest builder, and the real byte-frozen v002 derive lanes.
There is NO stub lane, NO stub launcher, NO stub comparator and NO
monkeypatch of any production function anywhere in this file.  The mutations
some tests apply are DELIBERATE ONE-PIN SKEWS of a real component inside a
DISPOSABLE WORKSPACE COPY -- that is the defect under test, not a substitute
for the component.

The canonical workspace is only ever READ.  Every writable fixture is a
copy under a temporary directory (the scratchpad when STAGE8_T7_TEST_SCRATCH
is set).  No test writes to, or chmods, the canonical root.

WHAT IS COVERED, and by which test:

  A1 generation coherence
    test_pin_table_is_total                      structural totality
    test_coherent_generation_passes              happy path, real files
    test_single_lagging_pin_blocks               EIGHT one-pin skews, each
                                                blocking by pin id -- the
                                                exact defect that recurred
                                                for six cycles
  Fence (record items 1 and 3, limitation L3)
    test_fence_raise_and_drop_cycle              raise -> writable ->
                                                drop -> not writable
    test_fence_at_rest_preflight_self_heals      L3: found writable -> the
                                                fence is dropped and the
                                                anomaly is RECORDED
    test_l3_sigterm_during_the_raised_window_drops_the_fence
                                                real controller subprocess,
                                                real signal, verified drop
  A4 receipt order
    test_a4_blocked_lane_seals_no_receipt        REAL run_lane driving the
                                                REAL launcher and the REAL
                                                comparator to a nonzero
                                                returncode: no receipt, no
                                                seal, retry path open
    test_a4_receipt_seal_follows_the_checks_in_source
                                                source-order assertion
  Preconditions
    test_precondition_tuple_and_dispatch_agree   frozen tuple parity

WHAT THIS FILE IS NOT.  It is not startability evidence.  PREFLIGHT_OK is
not startability evidence either (A2).  The only accepted startability
evidence is scripts/test_stage8_t7_real_chain_rehearsal_v001.py.
"""

from __future__ import annotations

import importlib.util
import json
import os
import shutil
import signal
import stat
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
PINNED_PYTHON = Path(
    "/Users/bgm/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/python/bin/python3"
)
CONTROLLER_RELATIVE = "scripts/run_stage8_t7_actual_parent_car_pipeline_v007.py"
LAUNCHER_RELATIVE = "scripts/launch_stage8_t7_content_addressed_runtime_v007.py"
COMPARATOR_RELATIVE = (
    "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
    "v006.py"
)
BUILDER_RELATIVE = (
    "scripts/build_stage8_t7_actual_parent_car_implementation_manifest_v006.py"
)
DERIVE_PRIMARY_RELATIVE = (
    "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
    "primary_v002.py"
)
MANIFEST_RELATIVE = (
    "provenance/"
    "stage8_t7_actual_parent_regulated_car_operator_response_implementation_"
    "v006.json"
)
FENCED_RELATIVES = ("stage8_execution/work", "provenance")
AT_REST_MODE = 0o555
COPY_EXCLUDES = (".proof_deps", ".pytest_cache", ".git", ".git_disabled")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def scratch_directory(label: str) -> Path:
    base = os.environ.get("STAGE8_T7_TEST_SCRATCH")
    if base:
        Path(base).mkdir(parents=True, exist_ok=True)
    return Path(
        tempfile.mkdtemp(prefix=f"stage8_t7_controller_v007_{label}_", dir=base)
    ).resolve()


def copy_workspace(label: str) -> Path:
    """Copy the canonical workspace to a DISPOSABLE location, modes included.

    The copy starts in the SAME at-rest state as the canonical root (the
    fenced directories mode 555), so every fence test exercises the real
    at-rest condition rather than a convenient one.
    """
    destination = scratch_directory(label) / "workspace"
    shutil.copytree(
        ROOT,
        destination,
        symlinks=True,
        ignore=shutil.ignore_patterns(*COPY_EXCLUDES),
    )
    for relative in FENCED_RELATIVES:
        directory = destination / relative
        require(directory.is_dir(), f"copy is missing {relative}")
        directory.chmod(AT_REST_MODE)
    return destination


def raise_copy_fence(workspace: Path) -> None:
    """Deliberate L4-style raise INSIDE A DISPOSABLE COPY (never canonical)."""
    for relative in FENCED_RELATIVES:
        (workspace / relative).chmod(0o755)


def drop_copy_fence(workspace: Path) -> None:
    for relative in FENCED_RELATIVES:
        (workspace / relative).chmod(AT_REST_MODE)


def directory_mode(directory: Path) -> int:
    return stat.S_IMODE(directory.stat().st_mode)


def build_manifest(workspace: Path) -> str:
    """Build the G7 manifest in the copy with the REAL builder script."""
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
        f"manifest builder failed in the copy: {completed.stderr[-3000:]}",
    )
    summary = json.loads(completed.stdout)
    require(
        summary.get("row_count") == 12,
        f"manifest builder wrote {summary.get('row_count')} rows, expected 12",
    )
    for relative in FENCED_RELATIVES:
        require(
            directory_mode(workspace / relative) == AT_REST_MODE,
            f"the builder did not drop the fence on {relative}",
        )
    return str(summary["manifest_sha256"])


def load_controller(workspace: Path):
    """Load the controller module FROM THE COPY, so every ROOT-derived
    constant (including the fenced directories) points into the copy."""
    path = workspace / CONTROLLER_RELATIVE
    name = f"controller_v007_under_test_{abs(hash(str(path)))}"
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, "unable to load controller")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    require(module.ROOT == workspace, "controller ROOT is not the disposable copy")
    return module


def substitute_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    require(
        text.count(old) == 1,
        f"skew fixture: {old!r} appears {text.count(old)} times in {path.name}",
    )
    path.write_text(text.replace(old, new), encoding="utf-8")


def expect_block(action: Callable[[], Any], fragment: str, label: str) -> str:
    try:
        action()
    except RuntimeError as error:
        require(
            fragment in str(error),
            f"{label}: blocked, but not on {fragment!r}: {error}",
        )
        return str(error)
    raise RuntimeError(f"{label}: expected a RuntimeError block; none was raised")


# ==========================================================================
# A1 GENERATION COHERENCE
# ==========================================================================


def test_pin_table_is_total() -> None:
    module = load_controller(copy_workspace("pin_table"))
    module.verify_pin_table_is_total()
    require(
        len(module.GENERATION_COHERENCE_PINS) >= 14,
        "the pin table lost rows; every enforcement point must be pinned",
    )
    identifiers = [pin["id"] for pin in module.GENERATION_COHERENCE_PINS]
    require(len(identifiers) == len(set(identifiers)), "duplicate pin identifiers")
    # Every family named by the launcher's own allowlist must be a pinned
    # family, so an allowlist row can never be an unclassified string.
    launcher_module_rows = module.read_source_pin(
        module.ROOT / module.GENERATION_MEMBERS["launcher"], "ALLOWED_TARGETS"
    )
    for row in launcher_module_rows:
        require(
            module.family_of(row) is not None,
            f"launcher allowlist row is not classified by any family: {row}",
        )


def test_coherent_generation_passes() -> None:
    workspace = copy_workspace("coherent")
    build_manifest(workspace)
    module = load_controller(workspace)
    evaluated = module.evaluate_generation_coherence()
    require(
        evaluated["generation_tag"] == "stage8_t7_generation_g7",
        f"unexpected generation tag: {evaluated['generation_tag']}",
    )
    require(
        len(evaluated["pins"]) == len(module.GENERATION_COHERENCE_PINS),
        "the evaluated table does not cover every pin",
    )
    # The launcher pin and the comparator's launcher pin must name the SAME
    # launcher -- the equality whose absence was the B1 wedge.
    controller_launcher = evaluated["pins"]["P01_controller_launcher_pin"]["named"]
    comparator_launcher = evaluated["pins"]["P08_comparator_launcher_pin"]["named"]
    require(
        controller_launcher == comparator_launcher == [module.GENERATION_MEMBERS["launcher"]],
        "controller and comparator do not name the same launcher: "
        f"{controller_launcher} vs {comparator_launcher}",
    )
    controller_manifest = evaluated["pins"]["P02_controller_manifest_pin"]["named"]
    comparator_manifest = evaluated["pins"]["P07_comparator_manifest_pin"]["named"]
    require(
        controller_manifest == comparator_manifest == [module.GENERATION_MEMBERS["manifest"]],
        "controller and comparator do not name the same manifest: "
        f"{controller_manifest} vs {comparator_manifest}",
    )
    # The bridge pins must name the bridge generation, never the frontier.
    for pin_id in (
        "P03_controller_bridge_manifest_pin",
        "P09_comparator_bundle_binding_pin",
        "P13_derive_primary_manifest_pin",
        "P14_derive_independent_manifest_pin",
    ):
        require(
            evaluated["pins"][pin_id]["named"]
            == [module.BRIDGE_GENERATION_MEMBERS["manifest"]],
            f"{pin_id} does not name the bridge manifest",
        )
    require(
        evaluated["fence_row"]["at_rest_mode"] == AT_REST_MODE,
        "the fence row lost the at-rest mode",
    )


def test_single_lagging_pin_blocks() -> None:
    """THE SIX-CYCLE DEFECT, one pin at a time.

    Each leg advances the generation everywhere EXCEPT one pin -- exactly
    the shape of every one of the six recorded failures -- and requires the
    mechanical check to block, naming that pin.  The legs are applied to
    REAL component files inside disposable copies.
    """
    launcher_v006 = "scripts/launch_stage8_t7_content_addressed_runtime_v006.py"
    launcher_v007 = "scripts/launch_stage8_t7_content_addressed_runtime_v007.py"
    manifest_v004 = (
        "provenance/stage8_t7_actual_parent_regulated_car_operator_response_"
        "implementation_v004.json"
    )
    legs: tuple[tuple[str, str, Callable[[Path], None]], ...] = (
        (
            "controller launcher pin lags one bump",
            "P01_controller_launcher_pin",
            lambda workspace: substitute_once(
                workspace / CONTROLLER_RELATIVE,
                'ROOT / "scripts/launch_stage8_t7_content_addressed_runtime_v007.py"',
                'ROOT / "scripts/launch_stage8_t7_content_addressed_runtime_v006.py"',
            ),
        ),
        (
            "comparator launcher pin lags (the literal B1 wedge)",
            "P08_comparator_launcher_pin",
            lambda workspace: substitute_once(
                workspace / COMPARATOR_RELATIVE,
                '"scripts/launch_stage8_t7_content_addressed_runtime_v007.py"',
                '"scripts/launch_stage8_t7_content_addressed_runtime_v005.py"',
            ),
        ),
        (
            "comparator manifest pin lags (the B1 root cause)",
            "P07_comparator_manifest_pin",
            lambda workspace: substitute_once(
                workspace / COMPARATOR_RELATIVE,
                '"stage8_t7_actual_parent_regulated_car_operator_response_'
                'implementation_v006.json"',
                '"stage8_t7_actual_parent_regulated_car_operator_response_'
                'implementation_v004.json"',
            ),
        ),
        (
            "launcher allowlist carries a foreign-generation controller",
            "P06_launcher_allowlist",
            lambda workspace: substitute_once(
                workspace / LAUNCHER_RELATIVE,
                '"scripts/run_stage8_t7_actual_parent_car_pipeline_v007.py",',
                '"scripts/run_stage8_t7_actual_parent_car_pipeline_v007.py",\n'
                '        "scripts/run_stage8_t7_actual_parent_car_pipeline_v006.py",',
            ),
        ),
        (
            "launcher allowlist drops the comparator row",
            "P06_launcher_allowlist",
            lambda workspace: substitute_once(
                workspace / LAUNCHER_RELATIVE,
                '        "scripts/compare_stage8_t7_actual_parent_regulated_car_'
                'operator_response_"\n        "v006.py",\n'
                '        "scripts/test_stage8_t7_controller_v007.py",\n',
                '        "scripts/test_stage8_t7_controller_v007.py",\n',
            ),
        ),
        (
            "controller manifest pin lags one bump",
            "P02_controller_manifest_pin",
            lambda workspace: substitute_once(
                workspace / CONTROLLER_RELATIVE,
                '    / "provenance/"\n'
                '    "stage8_t7_actual_parent_regulated_car_operator_response_'
                'implementation_v006.json"\n',
                '    / "provenance/"\n'
                '    "stage8_t7_actual_parent_regulated_car_operator_response_'
                'implementation_v005.json"\n',
            ),
        ),
        (
            "controller lane-target pin lags on the comparator",
            "P04_controller_lane_targets_pin",
            lambda workspace: substitute_once(
                workspace / CONTROLLER_RELATIVE,
                '    "comparison": (\n'
                '        "scripts/compare_stage8_t7_actual_parent_regulated_car_'
                'operator_response_"\n        "v006.py"\n    ),\n}',
                '    "comparison": (\n'
                '        "scripts/compare_stage8_t7_actual_parent_regulated_car_'
                'operator_response_"\n        "v005.py"\n    ),\n}',
            ),
        ),
        (
            "byte-frozen derive lane repointed off the bridge manifest",
            "P13_derive_primary_manifest_pin",
            lambda workspace: substitute_once(
                workspace / DERIVE_PRIMARY_RELATIVE,
                '"stage8_t7_actual_parent_regulated_car_operator_response_'
                'implementation_v001.json"',
                '"stage8_t7_actual_parent_regulated_car_operator_response_'
                'implementation_v004.json"',
            ),
        ),
    )
    for index, (label, expected_pin, skew) in enumerate(legs):
        workspace = copy_workspace(f"skew{index}")
        build_manifest(workspace)
        skew(workspace)
        module = load_controller(workspace)
        message = expect_block(
            module.evaluate_generation_coherence,
            "GENERATION INCOHERENCE",
            f"one-pin skew must block: {label}",
        )
        require(
            expected_pin in message,
            f"one-pin skew blocked on the wrong pin ({label}): expected "
            f"{expected_pin}, message was: {message}",
        )
        shutil.rmtree(workspace.parent, ignore_errors=True)


def test_manifest_row_skew_blocks() -> None:
    """A lagging MANIFEST row set blocks too (P11), not only a source pin."""
    workspace = copy_workspace("manifest_skew")
    build_manifest(workspace)
    manifest = workspace / MANIFEST_RELATIVE
    (workspace / "provenance").chmod(0o755)
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    payload["files"] = [
        row
        for row in payload["files"]
        if row["path"] != CONTROLLER_RELATIVE
    ] + [
        {
            "path": "scripts/run_stage8_t7_actual_parent_car_pipeline_v006.py",
            "sha256": "0" * 64,
        }
    ]
    manifest.chmod(0o644)
    manifest.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    manifest.chmod(0o444)
    (workspace / "provenance").chmod(AT_REST_MODE)
    module = load_controller(workspace)
    message = expect_block(
        module.evaluate_generation_coherence,
        "GENERATION INCOHERENCE",
        "a manifest row of a foreign generation must block",
    )
    require(
        "P11_frontier_manifest_rows" in message,
        f"manifest row skew blocked on the wrong pin: {message}",
    )
    shutil.rmtree(workspace.parent, ignore_errors=True)


# ==========================================================================
# THE DIRECTORY-PERMISSION WRITE FENCE
# ==========================================================================


def test_fence_raise_and_drop_cycle() -> None:
    workspace = copy_workspace("fence_cycle")
    module = load_controller(workspace)
    for directory in module.FENCED_DIRECTORIES:
        require(
            module.directory_mode(directory) == AT_REST_MODE,
            f"copy did not start at rest: {directory}",
        )
        require(not module.fence_is_writable(directory), "at-rest dir is writable")
    raised = module.raise_fence()
    require(len(raised) == 2, f"raise did not cover both directories: {raised}")
    probes: list[Path] = []
    for directory in module.FENCED_DIRECTORIES:
        require(module.fence_is_writable(directory), f"raise failed: {directory}")
        probe = directory / ".fence_probe_v007"
        probe.write_text("probe\n", encoding="ascii")
        probes.append(probe)
    for probe in probes:
        probe.unlink()
    dropped = module.drop_fence()
    require(len(dropped) == 2, f"drop did not cover both directories: {dropped}")
    for directory in module.FENCED_DIRECTORIES:
        require(
            module.directory_mode(directory) == AT_REST_MODE,
            f"drop did not restore the at-rest mode: {directory}",
        )
        try:
            (directory / ".fence_probe_after_drop").write_text("x", encoding="ascii")
        except PermissionError:
            continue
        raise RuntimeError(f"post-drop write succeeded: {directory}")
    # Idempotent: a second drop is a no-op and never raises.
    require(module.drop_fence() == [], "a second drop was not a no-op")
    shutil.rmtree(workspace.parent, ignore_errors=True)


def test_fence_at_rest_preflight_self_heals() -> None:
    """Fence limitation L3: found writable -> dropped AND recorded."""
    workspace = copy_workspace("fence_l3")
    module = load_controller(workspace)
    # Simulate the hard-kill window: the directories are left open.
    raise_copy_fence(workspace)
    context: dict[str, Any] = {}
    module.preflight_fence_at_rest("independent", context)
    anomalies = context["fence_anomalies"]
    require(
        len(anomalies) == 2,
        f"L3 self-heal did not record both anomalies: {anomalies}",
    )
    for anomaly in anomalies:
        require(
            anomaly["writable_at_rest"] is True
            and anomaly["action"] == "dropped_to_at_rest_mode",
            f"anomaly record is incomplete: {anomaly}",
        )
    for directory in module.FENCED_DIRECTORIES:
        require(
            module.directory_mode(directory) == AT_REST_MODE,
            f"L3 self-heal did not drop {directory}",
        )
    # A second pass on an at-rest workspace records NO anomaly.
    context = {}
    module.preflight_fence_at_rest("independent", context)
    require(
        context["fence_anomalies"] == [],
        "an at-rest workspace reported a spurious fence anomaly",
    )
    shutil.rmtree(workspace.parent, ignore_errors=True)


def test_l3_sigterm_during_the_raised_window_drops_the_fence() -> None:
    """A REAL controller subprocess, a REAL signal, a verified drop.

    This narrows the L3 window; it does not close it.  SIGKILL cannot be
    caught, which is why the pre-flight self-heal above remains the
    mitigation of record.
    """
    workspace = copy_workspace("fence_sigterm")
    build_manifest(workspace)
    process = subprocess.Popen(
        [
            str(PINNED_PYTHON),
            "-I",
            "-S",
            str(workspace / LAUNCHER_RELATIVE),
            CONTROLLER_RELATIVE,
            "--lane",
            "independent",
        ],
        cwd=workspace,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    try:
        raised_observed = False
        deadline = time.monotonic() + 120.0
        while time.monotonic() < deadline:
            if process.poll() is not None:
                break
            modes = [
                directory_mode(workspace / relative)
                for relative in FENCED_RELATIVES
            ]
            if all(mode != AT_REST_MODE for mode in modes):
                raised_observed = True
                break
            time.sleep(0.05)
        require(
            raised_observed,
            "never observed the raised window; the controller exited early: "
            f"returncode={process.poll()} stderr={(process.stderr.read() if process.stderr else '')[-2000:]}",
        )
        process.send_signal(signal.SIGTERM)
        process.wait(timeout=60)
    finally:
        if process.poll() is None:
            process.kill()
            process.wait(timeout=30)
    for relative in FENCED_RELATIVES:
        require(
            directory_mode(workspace / relative) == AT_REST_MODE,
            f"SIGTERM left {relative} writable (mode "
            f"{directory_mode(workspace / relative):04o})",
        )
    shutil.rmtree(workspace.parent, ignore_errors=True)


# ==========================================================================
# A4 RECEIPT ORDER
# ==========================================================================


def test_a4_blocked_lane_seals_no_receipt() -> None:
    """A blocked lane must leave ZERO canonical artifacts.

    NO STUB: run_lane is the real controller function, the subprocess is the
    REAL launcher v007 driving the REAL comparator v006, and the nonzero
    returncode is the comparator's own refusal of an invocation with no
    bundle arguments.  In v006 this sequence sealed a BLOCKED receipt at the
    canonical receipt path before the returncode was ever inspected, and
    canonical_absences then blocked every retry.
    """
    workspace = copy_workspace("a4_blocked")
    manifest_digest = build_manifest(workspace)
    module = load_controller(workspace)
    manifest = json.loads(
        (workspace / MANIFEST_RELATIVE).read_text(encoding="utf-8")
    )
    rows = {str(row["path"]): str(row["sha256"]) for row in manifest["files"]}
    receipt = module.COMPARISON_RECEIPT
    seal = Path(f"{receipt}.seal.sha256")
    raise_copy_fence(workspace)
    try:
        message = expect_block(
            lambda: module.run_lane(
                lane="comparison",
                target=module.TARGETS["comparison"],
                arguments=[],
                outputs=module.LANE_OUTPUTS["comparison"],
                receipt=receipt,
                implementation_digest=manifest_digest,
                implementation_rows=rows,
                paths_verified_absent=[],
                fence_anomalies=[],
            ),
            "no receipt",
            "a nonzero lane returncode must block before sealing",
        )
        require(
            "comparison lane blocked" in message,
            f"unexpected block message: {message}",
        )
    finally:
        drop_copy_fence(workspace)
    require(
        not receipt.exists(),
        "A4 VIOLATION: a blocked lane sealed a canonical receipt: "
        f"{receipt}",
    )
    require(
        not seal.exists(),
        f"A4 VIOLATION: a blocked lane sealed a canonical receipt seal: {seal}",
    )
    for output in module.LANE_OUTPUTS["comparison"]:
        require(
            not output.exists(),
            f"A4 VIOLATION: a blocked lane left a canonical output: {output}",
        )
    shutil.rmtree(workspace.parent, ignore_errors=True)


def test_a4_receipt_seal_follows_the_checks_in_source() -> None:
    """Source-order assertion: the seal call comes AFTER both checks.

    A behavioural test alone can pass by luck of the failure mode; this leg
    reads the ORDER out of run_lane's own AST, so an inversion fails even if
    no lane happens to block during a test run.
    """
    import ast

    tree = ast.parse((ROOT / CONTROLLER_RELATIVE).read_bytes())
    run_lane = None
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "run_lane":
            run_lane = node
    require(run_lane is not None, "run_lane is absent from controller v007")
    assert run_lane is not None
    seal_lines: list[int] = []
    target_check_lines: list[int] = []
    returncode_check_lines: list[int] = []
    for node in ast.walk(run_lane):
        if not isinstance(node, ast.Call):
            continue
        function = node.func
        if isinstance(function, ast.Name) and function.id == "atomic_sealed_json":
            seal_lines.append(node.lineno)
        if isinstance(function, ast.Name) and function.id == "require":
            first = node.args[0] if node.args else None
            if isinstance(first, ast.Name) and first.id == "target_intact":
                target_check_lines.append(node.lineno)
            if (
                isinstance(first, ast.Compare)
                and isinstance(first.left, ast.Attribute)
                and first.left.attr == "returncode"
            ):
                returncode_check_lines.append(node.lineno)
    require(len(seal_lines) == 1, f"expected one seal call, found {seal_lines}")
    require(
        len(target_check_lines) == 1,
        f"expected one target-intact check, found {target_check_lines}",
    )
    require(
        len(returncode_check_lines) == 1,
        f"expected one returncode check, found {returncode_check_lines}",
    )
    require(
        max(target_check_lines + returncode_check_lines) < seal_lines[0],
        "A4 VIOLATION IN SOURCE: the receipt is sealed at line "
        f"{seal_lines[0]}, before the target-intact check at "
        f"{target_check_lines[0]} and/or the returncode check at "
        f"{returncode_check_lines[0]}",
    )


def test_precondition_tuple_and_dispatch_agree() -> None:
    workspace = copy_workspace("preconditions")
    module = load_controller(workspace)
    require(
        set(module.PRECONDITIONS) == set(module.PRECONDITION_STEPS),
        "the frozen precondition tuple and the dispatch table disagree",
    )
    require(
        module.PRECONDITIONS[0] == "runtime_attestation"
        and module.PRECONDITIONS[1] == "generation_coherence"
        and module.PRECONDITIONS[2] == "fence_at_rest",
        "coherence and the fence at-rest assertion must precede every other "
        f"precondition: {module.PRECONDITIONS[:3]}",
    )
    require(
        module.PRECONDITIONS[-1] == "canonical_absences",
        "canonical_absences must remain the last precondition",
    )
    require(
        "comparator_authority" in module.PRECONDITIONS,
        "the comparator-authority hoist is not an enumerated precondition",
    )
    shutil.rmtree(workspace.parent, ignore_errors=True)


def main() -> int:
    if sys.flags.isolated != 1 or sys.flags.no_site != 1:
        completed = subprocess.run(
            [sys.executable, "-I", "-S", str(SELF), *sys.argv[1:]],
            cwd=ROOT,
            check=False,
        )
        return completed.returncode
    tests = (
        test_pin_table_is_total,
        test_coherent_generation_passes,
        test_single_lagging_pin_blocks,
        test_manifest_row_skew_blocks,
        test_fence_raise_and_drop_cycle,
        test_fence_at_rest_preflight_self_heals,
        test_a4_receipt_seal_follows_the_checks_in_source,
        test_precondition_tuple_and_dispatch_agree,
        test_a4_blocked_lane_seals_no_receipt,
        test_l3_sigterm_during_the_raised_window_drops_the_fence,
    )
    for test in tests:
        test()
        print(f"PASS {test.__name__}", flush=True)
    print(f"controller_v007_tests_passed {len(tests)}/{len(tests)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
