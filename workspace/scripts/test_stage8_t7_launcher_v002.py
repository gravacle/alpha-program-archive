#!/usr/bin/env python3
"""Fixture-only tests for the v002 content-addressed runtime launcher.

Never touches the canonical workspace: every mutable fixture lives in a
temporary directory (scratchpad when STAGE8_T7_TEST_SCRATCH is set). The
canonical launcher and runtime manifest are only ever read.
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
LAUNCHER = ROOT / "scripts/launch_stage8_t7_content_addressed_runtime_v002.py"
PINNED_PYTHON = Path(
    "/Users/bgm/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/python/bin/python3"
)
RUNTIME_MARKER = "_stage8_t7_content_addressed_runtime_v001"
EXPECTED_MANIFEST_SHA256 = (
    "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b"
)
ECHO_ENVIRONMENT_KEY = "STAGE8_T7_LAUNCHER_TEST_ECHO_ATTESTATION"


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
    spec = importlib.util.spec_from_file_location("launcher_v002_under_test", LAUNCHER)
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


def test_allowlist_escape_blocked() -> None:
    module = load_launcher_module()
    expect_block(
        lambda: module.resolve_target(
            "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
            "primary_v001.py"
        ),
        "not allowlisted",
        "v001 target must not be allowlisted by the v002 launcher",
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
        lambda: module.resolve_target("scripts/nonexistent_target_v002.py"),
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
        / "scripts/run_stage8_t7_actual_parent_car_pipeline_v002.py"
    )
    escape_link.symlink_to(outside)
    canonical = (
        fixture
        / "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v002.py"
    )
    canonical.write_text("# fixture lane placeholder\n", encoding="utf-8")
    alias_link = fixture / "scripts/unlisted_alias_v002.py"
    alias_link.symlink_to(canonical)
    plain_unlisted = fixture / "scripts/plain_unlisted_v002.py"
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
        ["scripts/test_stage8_t7_launcher_v002.py"], environment
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
        test_allowlist_escape_blocked,
        test_symlink_handling,
        test_runtime_drift_detection,
        test_attestation_content,
    )
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"launcher_v002_tests_passed {len(tests)}/{len(tests)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
