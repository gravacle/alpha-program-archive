#!/usr/bin/env python3
"""Fixture-only tests for the v007 (generation-G7) runtime launcher.

Never touches the canonical workspace: every mutable fixture lives in a
temporary directory (scratchpad when STAGE8_T7_TEST_SCRATCH is set). The
canonical launcher and runtime manifest are only ever read.

Ported from the v006 suite and repointed to launcher v007, keeping the
READ-ONCE A/B/A swap-resistance test and the subprocess self-echo
attestation test, under the sealed standing discipline
STAGE8_REAL_COMPONENT_PRECONDITION_DISCIPLINE_V001 rule 1 (the REAL
launcher module's ALLOWED_TARGETS is asserted, never a copy of it).  The
allowlist fence at this generation asserts:

- the controller-v007 and comparator-v006 rows MUST be present (the row
  class whose absence was Blocking B1 two generations running);
- the allowlist must equal the frozen eleven-row generation-G7 contract
  set EXACTLY, so a foreign-generation row cannot be added silently;
- NO controller or comparator row of ANY earlier generation may remain --
  and the v005/v006 legs are the strong form: those files EXIST at their
  canonical paths (they are not quarantined), so a block there proves the
  allowlist, not mere absence, does the work;
- the quarantined v003/v004 entry points must still be absent from their
  canonical paths, and their surviving quarantine copies must still block.

WHAT THIS SUITE DOES NOT CLAIM (discipline rule 4): it says nothing about
whether launcher v005 or v006 can still launch their own chains -- they
can.  What stops those chains from producing artifacts is the
directory-permission write fence, driven by the controller-v007 suite and
by the no-stub rehearsal, not by anything in this file.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
LAUNCHER = ROOT / "scripts/launch_stage8_t7_content_addressed_runtime_v007.py"
PINNED_PYTHON = Path(
    "/Users/bgm/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/python/bin/python3"
)
RUNTIME_MARKER = "_stage8_t7_content_addressed_runtime_v001"
EXPECTED_MANIFEST_SHA256 = (
    "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b"
)
ECHO_ENVIRONMENT_KEY = "STAGE8_T7_LAUNCHER_TEST_ECHO_ATTESTATION"

# The frozen generation-G7 interface-contract allowlist: the eleven
# launchable rows of the twelve-row G7 implementation set (the twelfth is
# the launcher itself, which is not a launch target; its self-test is the
# --selftest flag, which requires no allowlist row).
EXPECTED_ALLOWED_TARGETS = frozenset(
    {
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v002.py",
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "independent_v002.py",
        "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v002.py",
        "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
        "independent_v002.py",
        "scripts/run_stage8_t7_actual_parent_car_pipeline_v007.py",
        "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
        "v006.py",
        "scripts/test_stage8_t7_controller_v007.py",
        "scripts/test_stage8_t7_launcher_v007.py",
        "scripts/test_compare_stage8_t7_actual_parent_regulated_car_operator_"
        "response_v006.py",
        "scripts/test_stage8_t7_real_chain_rehearsal_v001.py",
        "scripts/build_stage8_t7_actual_parent_car_implementation_manifest_"
        "v006.py",
    }
)
# Every controller generation this launcher must refuse.
SUPERSEDED_CONTROLLERS = (
    "scripts/run_stage8_t7_actual_parent_car_pipeline_v001.py",
    "scripts/run_stage8_t7_actual_parent_car_pipeline_v002.py",
    "scripts/run_stage8_t7_actual_parent_car_pipeline_v003.py",
    "scripts/run_stage8_t7_actual_parent_car_pipeline_v004.py",
    "scripts/run_stage8_t7_actual_parent_car_pipeline_v005.py",
    "scripts/run_stage8_t7_actual_parent_car_pipeline_v006.py",
)
# Every comparator generation this launcher must refuse.
SUPERSEDED_COMPARATORS = (
    "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
    "v001.py",
    "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
    "v002.py",
    "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
    "v003.py",
    "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
    "v004.py",
    "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
    "v005.py",
)
# Quarantined entry points: absent from the canonical paths, present under
# scripts/superseded_quarantine/, and blocked either way.
QUARANTINED_ENTRY_POINTS = (
    "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
    "v003.py",
    "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
    "v004.py",
    "scripts/run_stage8_t7_actual_parent_car_pipeline_v003.py",
    "scripts/run_stage8_t7_actual_parent_car_pipeline_v004.py",
)
# NOT quarantined: these exist at their canonical paths, so a block proves
# the allowlist -- not absence -- refuses them.
PRESENT_BUT_REFUSED = (
    "scripts/run_stage8_t7_actual_parent_car_pipeline_v005.py",
    "scripts/run_stage8_t7_actual_parent_car_pipeline_v006.py",
    "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
    "v005.py",
    "scripts/run_stage8_t7_actual_parent_car_pipeline_v002.py",
    "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
    "v002.py",
    "scripts/launch_stage8_t7_content_addressed_runtime_v006.py",
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
    # Canonicalize: on macOS tempfile may return /var/... while resolve()
    # canonicalizes to /private/var/..., which would break relative_to
    # checks against a monkeypatched fixture ROOT.
    return Path(
        tempfile.mkdtemp(prefix=f"stage8_t7_launcher_{label}_", dir=base)
    ).resolve()


def load_launcher_module():
    spec = importlib.util.spec_from_file_location("launcher_v007_under_test", LAUNCHER)
    require(spec is not None and spec.loader is not None, "unable to load launcher")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expect_block(callable_, fragment: str, label: str) -> None:
    try:
        callable_()
    except RuntimeError as error:
        require(
            fragment in str(error),
            f"{label}: blocked with unexpected message: {error}",
        )
        return
    raise RuntimeError(f"{label}: expected a RuntimeError block, none was raised")


def test_allowlist_regression_fence() -> None:
    """Blocking-2 regression fence (re-audit B1/B2; discipline rule 1):
    asserted against the REAL launcher module's ALLOWED_TARGETS, and the
    negative legs against the REAL resolve_target on the canonical
    workspace (the superseded comparator/controller files exist on disk,
    so only the allowlist can block them)."""
    module = load_launcher_module()

    # B1 repair at this generation: the G7 controller and comparator rows
    # are present.  Their absence was Blocking B1 in two prior cycles.
    for present in (
        "scripts/run_stage8_t7_actual_parent_car_pipeline_v007.py",
        "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_"
        "response_v006.py",
    ):
        require(
            present in module.ALLOWED_TARGETS,
            f"generation-G7 row is absent from the v007 launcher allowlist "
            f"(the B1 defect class): {present}",
        )

    # B2 fence: NO controller or comparator row of any earlier generation.
    for stale in SUPERSEDED_CONTROLLERS + SUPERSEDED_COMPARATORS:
        require(
            stale not in module.ALLOWED_TARGETS,
            f"superseded chain remains armed: {stale}",
        )

    # Frozen interface contract: the allowlist is EXACTLY the contract set.
    require(
        module.ALLOWED_TARGETS == EXPECTED_ALLOWED_TARGETS,
        "v007 allowlist differs from the frozen generation-G7 contract row "
        f"set: extra={sorted(module.ALLOWED_TARGETS - EXPECTED_ALLOWED_TARGETS)} "
        f"missing={sorted(EXPECTED_ALLOWED_TARGETS - module.ALLOWED_TARGETS)}",
    )

    # STRONG NEGATIVE LEG: these files EXIST at their canonical paths (they
    # are not quarantined), so a block proves the allowlist, not absence,
    # refuses them.
    for value in PRESENT_BUT_REFUSED:
        require(
            (ROOT / value).is_file(),
            f"regression-fence precondition: {value} should exist on disk",
        )
        expect_block(
            lambda v=value: module.resolve_target(v),
            "not allowlisted",
            f"present-but-superseded target must block: {value}",
        )

    # QUARANTINE LEG (Brian-authorized disarm, quarantine manifest
    # provenance/stage8_t7_superseded_chain_quarantine_manifest_v001.json):
    # the v003/v004 entry points no longer exist at their CANONICAL paths
    # (asserted), and their surviving quarantine copies — which DO exist on
    # disk — are blocked by the allowlist.
    for stale in QUARANTINED_ENTRY_POINTS:
        require(
            not (ROOT / stale).exists(),
            f"quarantine regression: {stale} reappeared at its canonical path",
        )
        quarantined = (
            "scripts/superseded_quarantine/" + Path(stale).name
        )
        require(
            (ROOT / quarantined).is_file(),
            f"regression-fence precondition: {quarantined} should exist on disk",
        )
        for value in (stale, quarantined):
            expect_block(
                lambda v=value: module.resolve_target(v),
                "not allowlisted",
                f"superseded target must block: {value}",
            )


def test_allowlist_escape_blocked() -> None:
    module = load_launcher_module()
    expect_block(
        lambda: module.resolve_target(
            "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
            "primary_v001.py"
        ),
        "not allowlisted",
        "v001 target must not be allowlisted by the v007 launcher",
    )
    expect_block(
        lambda: module.resolve_target(
            "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
            "v002.py"
        ),
        "not allowlisted",
        "v002 comparator must not be allowlisted by the v007 launcher",
    )
    expect_block(
        lambda: module.resolve_target(
            "scripts/run_stage8_t7_actual_parent_car_pipeline_v002.py"
        ),
        "not allowlisted",
        "v002 controller must not be allowlisted by the v007 launcher",
    )
    expect_block(
        lambda: module.resolve_target("scripts/../../outside_root.py"),
        "outside the clean-room root",
        "relative traversal escape",
    )
    expect_block(
        lambda: module.resolve_target("/etc/hosts"),
        "outside the clean-room root",
        "absolute path escape",
    )
    expect_block(
        lambda: module.resolve_target("scripts/nonexistent_target_v007.py"),
        "not allowlisted",
        "unknown script name",
    )


def test_symlink_handling() -> None:
    module = load_launcher_module()
    fixture = scratch_directory("symlink")
    (fixture / "scripts").mkdir(parents=True)
    outside = fixture.parent / f"{fixture.name}_payload.py"
    outside.write_text("raise SystemExit('escaped payload ran')\n", encoding="utf-8")
    escape_link = (
        fixture
        / "scripts/run_stage8_t7_actual_parent_car_pipeline_v007.py"
    )
    escape_link.symlink_to(outside)
    canonical = (
        fixture
        / "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v002.py"
    )
    canonical.write_text("# fixture lane placeholder\n", encoding="utf-8")
    alias_link = fixture / "scripts/unlisted_alias_v007.py"
    alias_link.symlink_to(canonical)
    plain_unlisted = fixture / "scripts/plain_unlisted_v007.py"
    plain_unlisted.write_text("# unlisted\n", encoding="utf-8")

    original_root = module.ROOT
    try:
        module.ROOT = fixture
        expect_block(
            lambda: module.resolve_target(str(escape_link)),
            "outside the clean-room root",
            "allowlisted-name symlink escaping the root must block",
        )
        resolved, relative = module.resolve_target(str(alias_link))
        require(
            resolved == canonical.resolve(),
            "symlink alias did not collapse to its canonical target",
        )
        require(
            relative
            == "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_"
            "response_primary_v002.py",
            "symlink alias did not report the canonical allowlisted identity",
        )
        expect_block(
            lambda: module.resolve_target(str(plain_unlisted)),
            "not allowlisted",
            "unlisted in-root file must block",
        )
    finally:
        module.ROOT = original_root


def test_runtime_drift_detection() -> None:
    require(
        sys.flags.isolated == 1 and sys.flags.no_site == 1,
        "drift tests require -I -S (re-exec guard failed)",
    )
    fixture = scratch_directory("drift")

    # Case A: absent manifest.
    module = load_launcher_module()
    module.RUNTIME_MANIFEST = fixture / "absent_manifest.json"
    module.RUNTIME_SEAL = fixture / "absent_manifest.json.seal.sha256"
    expect_block(
        module.verify_runtime,
        "sealed NumPy runtime manifest is absent",
        "absent runtime manifest",
    )

    # Case B: manifest byte drift against the pinned digest.
    module = load_launcher_module()
    drifted = fixture / "drifted_manifest.json"
    real_manifest = ROOT / "provenance/stage8_t7_numpy_runtime_manifest_v001.json"
    drifted.write_bytes(real_manifest.read_bytes() + b"\n")
    drifted_seal = fixture / "drifted_manifest.json.seal.sha256"
    drifted_seal.write_bytes(Path(f"{real_manifest}.seal.sha256").read_bytes())
    module.RUNTIME_MANIFEST = drifted
    module.RUNTIME_SEAL = drifted_seal
    expect_block(
        module.verify_runtime,
        "NumPy runtime manifest drift",
        "runtime manifest byte drift",
    )

    # Case C: intact manifest, corrupted adjacent seal digest.
    module = load_launcher_module()
    copied = fixture / "copied_manifest.json"
    copied.write_bytes(real_manifest.read_bytes())
    bad_seal = fixture / "copied_manifest.json.seal.sha256"
    bad_seal.write_text(
        f"{'0' * 64}  provenance/stage8_t7_numpy_runtime_manifest_v001.json\n",
        encoding="ascii",
    )
    module.RUNTIME_MANIFEST = copied
    module.RUNTIME_SEAL = bad_seal
    expect_block(
        module.verify_runtime,
        "NumPy runtime seal digest mismatch",
        "runtime seal digest drift",
    )

    # Case D: deep drift — a NumPy file whose bytes differ from its manifest row.
    module = load_launcher_module()
    site = fixture / "site-packages"
    (site / "numpy").mkdir(parents=True)
    (site / "numpy-2.3.5.dist-info").mkdir(parents=True)
    init_file = site / "numpy/__init__.py"
    init_file.write_text("# drifted fixture numpy\n", encoding="utf-8")
    metadata_file = site / "numpy-2.3.5.dist-info/METADATA"
    metadata_file.write_text("Name: numpy\n", encoding="utf-8")
    executable = Path(sys.executable).resolve()
    fake_manifest = {
        "schema": "stage8_t7_numpy_runtime_manifest_v001",
        "python_executable": str(executable),
        "python_executable_sha256": sha256(executable),
        "python_isolated": True,
        "python_no_site": True,
        "site_packages": str(site),
        "package_roots": ["numpy", "numpy-2.3.5.dist-info"],
        "files": [
            {
                "path": "numpy/__init__.py",
                "sha256": "0" * 64,
                "bytes": init_file.stat().st_size,
            },
            {
                "path": "numpy-2.3.5.dist-info/METADATA",
                "sha256": sha256(metadata_file),
                "bytes": metadata_file.stat().st_size,
            },
        ],
    }
    fake_path = fixture / "fake_runtime_manifest.json"
    fake_path.write_text(json.dumps(fake_manifest, indent=2) + "\n", encoding="utf-8")
    fake_digest = sha256(fake_path)
    fake_seal = fixture / "fake_runtime_manifest.json.seal.sha256"
    fake_seal.write_text(
        f"{fake_digest}  provenance/stage8_t7_numpy_runtime_manifest_v001.json\n",
        encoding="ascii",
    )
    module.RUNTIME_MANIFEST = fake_path
    module.RUNTIME_SEAL = fake_seal
    module.EXPECTED_MANIFEST_SHA256 = fake_digest
    saved_path = list(sys.path)
    try:
        expect_block(
            module.verify_runtime,
            "NumPy hash drift: numpy/__init__.py",
            "content drift inside the runtime inventory",
        )
    finally:
        sys.path[:] = saved_path


READ_ONCE_TARGET_TEMPLATE = '''\
import hashlib
import json
import sys
from pathlib import Path

attestation = getattr(sys, "_stage8_t7_content_addressed_runtime_v001")
Path(r"{sentinel}").write_text(
    json.dumps(
        {{
            "ran": "{leg}",
            "attested_target_sha256": attestation["target_sha256"],
            "dunder_name": __name__,
            "dunder_file": __file__,
        }}
    ),
    encoding="utf-8",
)
'''


def run_launcher_main_inprocess(module, target: Path) -> dict:
    """Drive the real launcher main() in-process with a stubbed
    verify_runtime, so resolve/read/hash/execute run exactly as authored."""
    saved_argv = list(sys.argv)
    saved_marker = getattr(sys, RUNTIME_MARKER, None)
    module.verify_runtime = lambda: {
        "schema": "stage8_t7_content_addressed_runtime_attestation_v001",
        "runtime_manifest_sha256": EXPECTED_MANIFEST_SHA256,
        "attestation_is_launcher_cooperative_only": True,
    }
    try:
        sys.argv = ["launcher_under_test", str(target)]
        result = module.main()
        require(result == 0, "in-process launcher main did not return 0")
        attestation = getattr(sys, RUNTIME_MARKER, None)
        require(isinstance(attestation, dict), "launcher did not publish the marker")
        return dict(attestation)
    finally:
        sys.argv = saved_argv
        if saved_marker is None:
            if hasattr(sys, RUNTIME_MARKER):
                delattr(sys, RUNTIME_MARKER)
        else:
            setattr(sys, RUNTIME_MARKER, saved_marker)


def test_read_once_execution_and_swap_resistance() -> None:
    """A/B/A: the attestation digest equals the digest of the source that
    actually executed — in the honest leg (A) and under an adversarial swap
    attempt after target resolution (B replaces A on disk post-resolve; the
    launcher must then attest and execute the SAME bytes, never hash one
    version and execute another)."""
    fixture = scratch_directory("read_once")
    (fixture / "scripts").mkdir(parents=True)
    target = fixture / "scripts/run_stage8_t7_actual_parent_car_pipeline_v007.py"
    sentinel = fixture / "sentinel.json"

    source_a = READ_ONCE_TARGET_TEMPLATE.format(sentinel=sentinel, leg="A")
    source_b = READ_ONCE_TARGET_TEMPLATE.format(sentinel=sentinel, leg="B")
    digest_a = hashlib.sha256(source_a.encode("utf-8")).hexdigest()
    digest_b = hashlib.sha256(source_b.encode("utf-8")).hexdigest()
    require(digest_a != digest_b, "A/B fixture sources must differ")

    # Leg 1 (honest A): executed bytes are A, attestation must equal sha256(A).
    module = load_launcher_module()
    module.ROOT = fixture
    target.write_text(source_a, encoding="utf-8")
    attestation = run_launcher_main_inprocess(module, target)
    witness = json.loads(sentinel.read_text(encoding="utf-8"))
    require(witness["ran"] == "A", "honest leg did not execute source A")
    require(
        witness["attested_target_sha256"] == digest_a
        and attestation["target_sha256"] == digest_a,
        "honest-leg attestation digest is not the digest of the executed source",
    )
    require(
        witness["dunder_name"] == "__main__",
        "read-once execution lost __main__ semantics",
    )
    require(
        Path(witness["dunder_file"]).resolve() == target.resolve(),
        "read-once execution lost __file__ semantics",
    )
    sentinel.unlink()

    # Leg 2 (adversarial swap after resolve): the on-disk target is swapped
    # to B immediately after resolve_target returns. Whatever source then
    # executes, the attested digest MUST be the digest of those executed
    # bytes — the v002 hash-then-re-read window is gone by construction.
    module = load_launcher_module()
    module.ROOT = fixture
    target.write_text(source_a, encoding="utf-8")
    original_resolve = module.resolve_target

    def swapping_resolve(value: str):
        resolved = original_resolve(value)
        resolved[0].write_text(source_b, encoding="utf-8")
        return resolved

    module.resolve_target = swapping_resolve
    attestation = run_launcher_main_inprocess(module, target)
    witness = json.loads(sentinel.read_text(encoding="utf-8"))
    require(
        witness["ran"] == "B",
        "swap leg fixture error: the swapped source did not execute",
    )
    require(
        witness["attested_target_sha256"] == digest_b
        and attestation["target_sha256"] == digest_b,
        "swap-leg attestation digest is not the digest of the executed source",
    )
    require(
        attestation["target_sha256"] != digest_a,
        "swap-leg attestation still carries the pre-swap digest (TOCTOU)",
    )
    sentinel.unlink()

    # Leg 3 (honest A again): confirm the property is stable after the swap.
    module = load_launcher_module()
    module.ROOT = fixture
    target.write_text(source_a, encoding="utf-8")
    attestation = run_launcher_main_inprocess(module, target)
    witness = json.loads(sentinel.read_text(encoding="utf-8"))
    require(
        witness["ran"] == "A"
        and witness["attested_target_sha256"] == digest_a
        and attestation["target_sha256"] == digest_a,
        "final honest leg attestation digest mismatch",
    )


def launcher_subprocess(arguments: list[str], environment: dict[str, str]):
    return subprocess.run(
        [str(PINNED_PYTHON), "-I", "-S", str(LAUNCHER), *arguments],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        env=environment,
    )


def test_attestation_content() -> None:
    require(PINNED_PYTHON.is_file(), "pinned runtime python is absent")

    selftest = launcher_subprocess(["--selftest"], dict(os.environ))
    require(
        selftest.returncode == 0,
        f"launcher selftest failed: {selftest.stderr[-2000:]}",
    )
    attestation = json.loads(selftest.stdout)
    require(
        attestation.get("schema")
        == "stage8_t7_content_addressed_runtime_attestation_v001",
        "attestation schema mismatch",
    )
    require(
        attestation.get("runtime_manifest_sha256") == EXPECTED_MANIFEST_SHA256,
        "attestation runtime-manifest digest mismatch",
    )
    require(
        attestation.get("launcher_sha256") == sha256(LAUNCHER),
        "attestation launcher self-hash mismatch",
    )
    require(
        attestation.get("attestation_is_launcher_cooperative_only") is True,
        "attestation must disclose it is launcher-cooperative only",
    )
    require(
        "target_sha256" not in attestation,
        "selftest attestation must not carry a target hash",
    )

    environment = dict(os.environ)
    environment[ECHO_ENVIRONMENT_KEY] = "1"
    echoed = launcher_subprocess(
        ["scripts/test_stage8_t7_launcher_v007.py"], environment
    )
    require(
        echoed.returncode == 0,
        f"launcher echo run failed: {echoed.stderr[-2000:]}",
    )
    launched = json.loads(echoed.stdout)
    require(
        launched.get("target_sha256") == sha256(SELF),
        "attestation target_sha256 does not match the resolved target bytes",
    )
    require(
        launched.get("attestation_is_launcher_cooperative_only") is True,
        "launched attestation lost the cooperative-only disclosure",
    )
    require(
        launched.get("launcher_sha256") == sha256(LAUNCHER),
        "launched attestation launcher self-hash mismatch",
    )
    require(
        launched.get("runtime_manifest_sha256") == EXPECTED_MANIFEST_SHA256,
        "launched attestation runtime-manifest digest mismatch",
    )


def main() -> int:
    if os.environ.get(ECHO_ENVIRONMENT_KEY) == "1":
        attestation = getattr(sys, RUNTIME_MARKER, None)
        require(isinstance(attestation, dict), "echo mode requires the launcher marker")
        print(json.dumps(copy.deepcopy(attestation), indent=2, sort_keys=True))
        return 0
    if sys.flags.isolated != 1 or sys.flags.no_site != 1:
        completed = subprocess.run(
            [sys.executable, "-I", "-S", str(SELF), *sys.argv[1:]],
            cwd=ROOT,
            check=False,
        )
        return completed.returncode
    tests = (
        test_allowlist_regression_fence,
        test_allowlist_escape_blocked,
        test_symlink_handling,
        test_runtime_drift_detection,
        test_read_once_execution_and_swap_resistance,
        test_attestation_content,
    )
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"launcher_v007_tests_passed {len(tests)}/{len(tests)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
