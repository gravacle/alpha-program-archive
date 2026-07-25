#!/usr/bin/env python3
"""Fixture-only integration tests for the v002 actual-parent CAR controller.

Every scenario runs against a throwaway fixture workspace built under a
temporary directory (scratchpad when STAGE8_T7_TEST_SCRATCH is set) with stub
lane scripts, a stub launcher, a fixture implementation manifest, and a
throwaway GPG home holding a generated test key. The canonical workspace is
only ever read (the controller source is copied out, never executed against
the canonical root), and the real disclosure key is never invoked.
"""

from __future__ import annotations

import hashlib
import json
import os
import stat
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTROLLER_SOURCE = ROOT / "scripts/run_stage8_t7_actual_parent_car_pipeline_v002.py"
PINNED_PYTHON = Path(
    "/Users/bgm/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/python/bin/python3"
)
GPG = Path("/opt/homebrew/bin/gpg")
DISCLOSURE_FINGERPRINT = "18488605D44F65A9B57B610AA5F3A86512A04D61"
RUNTIME_MANIFEST_SHA256 = (
    "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b"
)
PASS_VERDICT = "ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_COMPARISON_PASSED"

CONTROLLER_RELATIVE = "scripts/run_stage8_t7_actual_parent_car_pipeline_v002.py"
LAUNCHER_RELATIVE = "scripts/launch_stage8_t7_content_addressed_runtime_v002.py"
INDEPENDENT_RELATIVE = (
    "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
    "independent_v002.py"
)
PRIMARY_RELATIVE = (
    "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
    "primary_v002.py"
)
COMPARATOR_RELATIVE = (
    "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
    "v002.py"
)
TEST_ROWS = (
    "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
    "primary_v002.py",
    "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
    "independent_v002.py",
    "scripts/test_compare_stage8_t7_actual_parent_regulated_car_operator_"
    "response_v002.py",
)
REQUIRED_ROWS = (
    CONTROLLER_RELATIVE,
    LAUNCHER_RELATIVE,
    PRIMARY_RELATIVE,
    INDEPENDENT_RELATIVE,
    COMPARATOR_RELATIVE,
    *TEST_ROWS,
)

INDEPENDENT_JSON_RELATIVE = (
    "stage8_execution/work/"
    "T07_actual_parent_regulated_car_operator_response_"
    "independent_precomparison_v001.json"
)
PRIMARY_JSON_RELATIVE = (
    "stage8_execution/work/"
    "T07_actual_parent_regulated_car_operator_response_primary_v001.json"
)
COMPARISON_JSON_RELATIVE = (
    "stage8_execution/work/"
    "T07_actual_parent_regulated_car_operator_response_comparison_v001.json"
)
INDEPENDENT_RECEIPT_RELATIVE = (
    "provenance/stage8_t7_actual_parent_car_independent_execution_receipt_v001.json"
)
PRIMARY_RECEIPT_RELATIVE = (
    "provenance/stage8_t7_actual_parent_car_primary_execution_receipt_v001.json"
)
COMPARISON_RECEIPT_RELATIVE = (
    "provenance/stage8_t7_actual_parent_car_comparison_execution_receipt_v001.json"
)

STUB_HELPERS = '''
import hashlib
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def file_sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def seal(path):
    digest = file_sha256(path)
    Path(str(path) + ".seal.sha256").write_text(
        digest + "  " + Path(path).name + "\\n", encoding="ascii"
    )


def log_lane(name):
    with open(ROOT / "stage8_execution/work/lane_order.log", "a") as handle:
        handle.write(name + "\\n")
'''

STUB_LAUNCHER = f'''#!/usr/bin/env python3
"""Fixture stub launcher: cooperative marker only, no runtime verification."""
{STUB_HELPERS}
import runpy


def main():
    target = (ROOT / sys.argv[1]).resolve()
    attestation = {{
        "schema": "stage8_t7_content_addressed_runtime_attestation_v001",
        "runtime_manifest_sha256": "{RUNTIME_MANIFEST_SHA256}",
        "python_isolated": True,
        "python_no_site": True,
        "launcher_sha256": file_sha256(Path(__file__)),
        "attestation_is_launcher_cooperative_only": True,
        "target_sha256": file_sha256(target),
    }}
    setattr(sys, "_stage8_t7_content_addressed_runtime_v001", attestation)
    sys.argv = [str(target)] + sys.argv[2:]
    runpy.run_path(str(target), run_name="__main__")


main()
'''

STUB_DERIVE_TEMPLATE = '''#!/usr/bin/env python3
"""Fixture stub {lane} lane."""
{helpers}

def main():
    work = ROOT / "stage8_execution/work"
    work.mkdir(parents=True, exist_ok=True)
    out_json = work / "{json_name}"
    out_npz = out_json.with_suffix(".npz")
    out_json.write_text(json.dumps({{"lane": "{lane}"}}) + "\\n", encoding="utf-8")
    out_npz.write_bytes(b"NPZ-STUB-{lane}")
    seal(out_json)
    seal(out_npz)
    log_lane("{lane}")
{extra}

main()
'''

STUB_COMPARATOR_TEMPLATE = '''#!/usr/bin/env python3
"""Fixture stub comparator lane."""
{helpers}

def argument(name):
    return sys.argv[sys.argv.index(name) + 1]


def main():
    output = Path(argument("--output"))
    payload = {{
        "schema": "fixture_stub_comparison_v002",
        "overall_verdict":
            "ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_COMPARISON_PASSED",
        "comparison_supports_actual_parent_regulated_CAR_operator_response": True,
        "comparison_supports_actual_parent_same_carrier_one_source_restriction": True,
        "resolved_input_paths": {{
            "independent_json": str(Path(argument("--independent-json")).resolve()),
            "independent_npz": str(Path(argument("--independent-npz")).resolve()),
            "primary_json": str(Path(argument("--primary-json")).resolve()),
            "primary_npz": str(Path(argument("--primary-npz")).resolve()),
        }},
        "resolved_output_path": str(output.resolve()),
        "controller_context": argument("--controller-context"),
    }}
{override}
    output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\\n", encoding="utf-8"
    )
    seal(output)
    log_lane("comparison")


main()
'''

SELF_MUTATION = (
    '    with open(__file__, "a") as handle:\n'
    '        handle.write("# post-execution self mutation\\n")\n'
)
CROSS_MUTATION = (
    '    with open(ROOT / "' + PRIMARY_RELATIVE + '", "a") as handle:\n'
    '        handle.write("# cross-lane mutation of the primary target\\n")\n'
)
SPOOFED_OUTPUT_PATH = (
    '    payload["resolved_output_path"] = "/nonexistent/spoofed_comparison.json"\n'
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
    return Path(tempfile.mkdtemp(prefix=f"stage8_t7_controller_{label}_", dir=base))


def run_gpg(arguments: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        [str(GPG), *arguments], check=False, capture_output=True, text=True
    )


def short_gpg_home(label: str) -> Path:
    # The gpg-agent unix socket lives inside GNUPGHOME and the socket path is
    # limited to ~104 bytes on macOS, so the throwaway keyring cannot live under
    # the (long) scratchpad path. Only this keyring uses the OS per-user temp
    # dir; every fixture workspace stays in the scratchpad.
    home = Path(tempfile.mkdtemp(prefix=f"s8gpg_{label}_")) / "home"
    home.mkdir(mode=0o700)
    require(
        len(str(home)) < 90,
        f"GNUPGHOME path too long for the gpg-agent socket: {home}",
    )
    return home


def make_signing_home() -> tuple[Path, str]:
    home = short_gpg_home("sign")
    generated = run_gpg(
        [
            "--batch",
            "--homedir",
            str(home),
            "--pinentry-mode",
            "loopback",
            "--passphrase",
            "",
            "--quick-generate-key",
            "stage8-t7-fixture-throwaway <fixture@example.invalid>",
            "ed25519",
            "sign",
            "0",
        ]
    )
    require(generated.returncode == 0, f"test key generation failed: {generated.stderr}")
    listing = run_gpg(
        ["--batch", "--homedir", str(home), "--with-colons", "--list-secret-keys"]
    )
    require(listing.returncode == 0, "test key listing failed")
    fingerprint = ""
    for line in listing.stdout.splitlines():
        if line.startswith("fpr:"):
            fingerprint = line.split(":")[9]
            break
    require(len(fingerprint) == 40, "test key fingerprint not found")
    require(
        fingerprint != DISCLOSURE_FINGERPRINT,
        "test key must never be the real disclosure key",
    )
    return home, fingerprint


def make_public_only_home(signing_home: Path, fingerprint: str) -> Path:
    exported = run_gpg(
        ["--batch", "--homedir", str(signing_home), "--armor", "--export", fingerprint]
    )
    require(exported.returncode == 0, "test key export failed")
    home = short_gpg_home("pub")
    key_file = home.parent / "public.asc"
    key_file.write_text(exported.stdout, encoding="ascii")
    imported = run_gpg(["--batch", "--homedir", str(home), "--import", str(key_file)])
    require(imported.returncode == 0, "public-only import failed")
    return home


def build_fixture(
    label: str,
    *,
    signing_home: Path,
    fingerprint: str,
    independent_extra: str = "",
    comparator_override: str = "",
    omit_manifest_row: str = "",
) -> Path:
    fixture = scratch_directory(label)
    (fixture / "scripts").mkdir()
    (fixture / "provenance").mkdir()
    (fixture / "stage8_execution/work").mkdir(parents=True)

    (fixture / LAUNCHER_RELATIVE).write_text(STUB_LAUNCHER, encoding="utf-8")
    (fixture / INDEPENDENT_RELATIVE).write_text(
        STUB_DERIVE_TEMPLATE.format(
            lane="independent",
            helpers=STUB_HELPERS,
            json_name=Path(INDEPENDENT_JSON_RELATIVE).name,
            extra=independent_extra,
        ),
        encoding="utf-8",
    )
    (fixture / PRIMARY_RELATIVE).write_text(
        STUB_DERIVE_TEMPLATE.format(
            lane="primary",
            helpers=STUB_HELPERS,
            json_name=Path(PRIMARY_JSON_RELATIVE).name,
            extra="",
        ),
        encoding="utf-8",
    )
    (fixture / COMPARATOR_RELATIVE).write_text(
        STUB_COMPARATOR_TEMPLATE.format(
            helpers=STUB_HELPERS, override=comparator_override
        ),
        encoding="utf-8",
    )
    for test_row in TEST_ROWS:
        (fixture / test_row).write_text(
            f"# fixture test stub for {test_row}\n", encoding="utf-8"
        )

    controller_text = CONTROLLER_SOURCE.read_text(encoding="utf-8")
    require(
        controller_text.count(DISCLOSURE_FINGERPRINT) == 1,
        "controller source must pin exactly one signing fingerprint",
    )
    (fixture / CONTROLLER_RELATIVE).write_text(
        controller_text.replace(DISCLOSURE_FINGERPRINT, fingerprint),
        encoding="utf-8",
    )

    rows = [
        {"path": row, "sha256": sha256(fixture / row)}
        for row in REQUIRED_ROWS
        if row != omit_manifest_row
    ]
    manifest = fixture / (
        "provenance/"
        "stage8_t7_actual_parent_regulated_car_operator_response_"
        "implementation_v001.json"
    )
    manifest.write_text(
        json.dumps(
            {
                "schema": (
                    "stage8_t7_actual_parent_regulated_car_operator_response_"
                    "implementation_v001"
                ),
                "files": rows,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    Path(f"{manifest}.seal.sha256").write_text(
        f"{sha256(manifest)}  {manifest.name}\n", encoding="ascii"
    )
    signed = run_gpg(
        [
            "--batch",
            "--homedir",
            str(signing_home),
            "--pinentry-mode",
            "loopback",
            "--passphrase",
            "",
            "--local-user",
            fingerprint,
            "--armor",
            "--output",
            f"{manifest}.asc",
            "--detach-sign",
            str(manifest),
        ]
    )
    require(signed.returncode == 0, f"fixture manifest signing failed: {signed.stderr}")
    return fixture


def run_controller(fixture: Path, gpg_home: Path) -> subprocess.CompletedProcess:
    environment = dict(os.environ)
    environment["GNUPGHOME"] = str(gpg_home)
    environment.pop("STAGE8_T7_CONTROLLER_CONTEXT", None)
    return subprocess.run(
        [
            sys.executable,
            str(fixture / LAUNCHER_RELATIVE),
            CONTROLLER_RELATIVE,
        ],
        cwd=fixture,
        check=False,
        capture_output=True,
        text=True,
        env=environment,
    )


def lane_order(fixture: Path) -> list[str]:
    log = fixture / "stage8_execution/work/lane_order.log"
    if not log.is_file():
        return []
    return log.read_text(encoding="utf-8").split()


def read_only(path: Path) -> bool:
    return (path.stat().st_mode & (stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH)) == 0


def test_happy_path_and_immutability(signing_home: Path, fingerprint: str) -> None:
    fixture = build_fixture(
        "happy", signing_home=signing_home, fingerprint=fingerprint
    )
    completed = run_controller(fixture, signing_home)
    require(
        completed.returncode == 0,
        f"happy-path controller run failed: {completed.stderr[-4000:]}",
    )
    summary = json.loads(completed.stdout)
    require(
        summary.get("overall_verdict") == PASS_VERDICT,
        "summary verdict mismatch",
    )
    require(
        summary.get("schema") == "stage8_t7_actual_parent_car_pipeline_summary_v002",
        "summary schema mismatch",
    )
    require(
        lane_order(fixture) == ["independent", "primary", "comparison"],
        "lane order is not independent-then-primary-then-comparison",
    )
    manifest_rows = {
        row["path"]: row["sha256"]
        for row in json.loads(
            (
                fixture
                / "provenance/"
                "stage8_t7_actual_parent_regulated_car_operator_response_"
                "implementation_v001.json"
            ).read_text(encoding="utf-8")
        )["files"]
    }
    for receipt_relative, target_relative in (
        (INDEPENDENT_RECEIPT_RELATIVE, INDEPENDENT_RELATIVE),
        (PRIMARY_RECEIPT_RELATIVE, PRIMARY_RELATIVE),
        (COMPARISON_RECEIPT_RELATIVE, COMPARATOR_RELATIVE),
    ):
        receipt = fixture / receipt_relative
        receipt_seal = Path(f"{receipt}.seal.sha256")
        signature = Path(f"{receipt}.asc")
        require(receipt.is_file(), f"receipt absent: {receipt_relative}")
        require(receipt_seal.is_file(), f"receipt seal absent: {receipt_relative}")
        require(signature.is_file(), f"receipt signature absent: {receipt_relative}")
        require(read_only(receipt), f"receipt is not immutable: {receipt_relative}")
        require(read_only(receipt_seal), f"receipt seal is writable: {receipt_relative}")
        seal_fields = receipt_seal.read_text(encoding="ascii").split()
        require(seal_fields[0] == sha256(receipt), "receipt seal digest mismatch")
        payload = json.loads(receipt.read_text(encoding="utf-8"))
        require(
            payload.get("schema") == "stage8_t7_local_sealed_execution_receipt_v002",
            "receipt schema mismatch",
        )
        require(payload.get("status") == "SUCCEEDED", "receipt status mismatch")
        expected_target = manifest_rows[target_relative]
        require(
            payload.get("target_sha256") == expected_target
            and payload.get("target_sha256_pre_execution") == expected_target
            and payload.get("target_sha256_post_execution") == expected_target,
            "receipt pre/post target digests do not match the manifest row",
        )
        verification = run_gpg(
            [
                "--batch",
                "--homedir",
                str(signing_home),
                "--status-fd",
                "1",
                "--verify",
                str(signature),
                str(receipt),
            ]
        )
        require(
            verification.returncode == 0
            and f"[GNUPG:] VALIDSIG {fingerprint}" in verification.stdout,
            f"receipt signature did not verify: {receipt_relative}",
        )

    rerun = run_controller(fixture, signing_home)
    require(rerun.returncode != 0, "rerun must block on immutable outputs")
    require(
        "immutable output already exists" in rerun.stderr,
        "rerun did not block for immutability",
    )


def test_missing_manifest_row_blocks(signing_home: Path, fingerprint: str) -> None:
    fixture = build_fixture(
        "missing_row",
        signing_home=signing_home,
        fingerprint=fingerprint,
        omit_manifest_row=TEST_ROWS[2],
    )
    completed = run_controller(fixture, signing_home)
    require(completed.returncode != 0, "missing required row must block")
    require(
        "implementation manifest is missing required rows" in completed.stderr,
        "missing-row block used the wrong fence",
    )
    require(lane_order(fixture) == [], "no lane may run when a required row is missing")


def test_pre_execution_rehash_blocks(signing_home: Path, fingerprint: str) -> None:
    fixture = build_fixture(
        "pre_swap",
        signing_home=signing_home,
        fingerprint=fingerprint,
        independent_extra=CROSS_MUTATION,
    )
    completed = run_controller(fixture, signing_home)
    require(completed.returncode != 0, "pre-execution target swap must block")
    require(
        "target drift before execution" in completed.stderr,
        "pre-execution swap used the wrong fence",
    )
    require(
        lane_order(fixture) == ["independent"],
        "the swapped primary lane must never run",
    )
    require(
        not (fixture / PRIMARY_RECEIPT_RELATIVE).exists(),
        "no receipt may attribute provenance to unexamined code",
    )


def test_post_execution_rehash_blocks(signing_home: Path, fingerprint: str) -> None:
    fixture = build_fixture(
        "post_swap",
        signing_home=signing_home,
        fingerprint=fingerprint,
        independent_extra=SELF_MUTATION,
    )
    completed = run_controller(fixture, signing_home)
    require(completed.returncode != 0, "post-execution target drift must block")
    require(
        "target drifted across execution" in completed.stderr,
        "post-execution drift used the wrong fence",
    )
    receipt = fixture / INDEPENDENT_RECEIPT_RELATIVE
    require(receipt.is_file(), "drift evidence receipt must still be sealed")
    payload = json.loads(receipt.read_text(encoding="utf-8"))
    require(payload.get("status") == "BLOCKED", "drifted lane receipt must be BLOCKED")
    require(
        payload.get("target_sha256_post_execution")
        != payload.get("target_sha256_pre_execution"),
        "receipt must record the divergent pre/post digests",
    )
    require(
        Path(f"{receipt}.asc").is_file(),
        "drift evidence receipt must still be signed",
    )
    require(
        lane_order(fixture) == ["independent"],
        "pipeline must stop at the drifted lane",
    )


def test_comparator_path_crosscheck_blocks(
    signing_home: Path, fingerprint: str
) -> None:
    fixture = build_fixture(
        "spoofed_paths",
        signing_home=signing_home,
        fingerprint=fingerprint,
        comparator_override=SPOOFED_OUTPUT_PATH,
    )
    completed = run_controller(fixture, signing_home)
    require(completed.returncode != 0, "spoofed comparator paths must block")
    require(
        "comparator resolved output path does not match" in completed.stderr,
        "comparator path cross-check used the wrong fence",
    )
    require(
        lane_order(fixture) == ["independent", "primary", "comparison"],
        "comparator cross-check fires after the comparison lane",
    )
    require(
        (fixture / COMPARISON_RECEIPT_RELATIVE).is_file(),
        "comparison receipt must exist for the blocked cross-check",
    )


def test_receipt_signing_fails_closed(signing_home: Path, fingerprint: str) -> None:
    public_home = make_public_only_home(signing_home, fingerprint)
    fixture = build_fixture(
        "no_secret_key", signing_home=signing_home, fingerprint=fingerprint
    )
    completed = run_controller(fixture, public_home)
    require(completed.returncode != 0, "absent signing capability must block")
    require(
        "receipt signing failed (fail closed)" in completed.stderr,
        "signing absence used the wrong fence",
    )
    receipt = fixture / INDEPENDENT_RECEIPT_RELATIVE
    require(receipt.is_file(), "sealed receipt should precede the signing failure")
    require(
        not Path(f"{receipt}.asc").is_file(),
        "no signature may exist when signing failed",
    )
    require(
        lane_order(fixture) == ["independent"],
        "pipeline must stop at the first unsigned receipt",
    )


def main() -> int:
    require(PINNED_PYTHON.is_file(), "pinned runtime python is absent")
    require(GPG.is_file(), "gpg binary is absent")
    signing_home, fingerprint = make_signing_home()
    tests = (
        test_happy_path_and_immutability,
        test_missing_manifest_row_blocks,
        test_pre_execution_rehash_blocks,
        test_post_execution_rehash_blocks,
        test_comparator_path_crosscheck_blocks,
        test_receipt_signing_fails_closed,
    )
    for test in tests:
        test(signing_home, fingerprint)
        print(f"PASS {test.__name__}")
    print(f"controller_v002_tests_passed {len(tests)}/{len(tests)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
