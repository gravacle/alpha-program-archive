#!/usr/bin/env python3
"""Fixture-only integration tests for the v003 actual-parent CAR controller.

Every scenario runs against a throwaway fixture workspace built under a
temporary directory (scratchpad when STAGE8_T7_TEST_SCRATCH is set) with stub
lane scripts, a stub launcher, and a fixture implementation manifest. The
canonical workspace is only ever read (the controller source is copied out,
never executed against the canonical root).

v003 (repair binding V002, S1-3/S1-4): GPG is fully removed; the controller
runs one lane per invocation (--lane) with lane order enforced through
verified receipts; every fail-closed precondition is pre-flighted BEFORE any
canonical path consumption; receipts record paths_verified_absent (the exact
absence list checked); the comparison lane passes both lane-receipt digests
to the v003 comparator and cross-checks the recorded values. The stub
comparator implements the real v003 comparator CLI contract exactly.
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
CONTROLLER_SOURCE = ROOT / "scripts/run_stage8_t7_actual_parent_car_pipeline_v003.py"
PINNED_PYTHON = Path(
    "/Users/bgm/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/python/bin/python3"
)
RUNTIME_MANIFEST_SHA256 = (
    "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b"
)
PASS_VERDICT = "ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_COMPARISON_PASSED"
RECEIPT_SCHEMA = "stage8_t7_local_sealed_execution_receipt_v003"

CONTROLLER_RELATIVE = "scripts/run_stage8_t7_actual_parent_car_pipeline_v003.py"
LAUNCHER_RELATIVE = "scripts/launch_stage8_t7_content_addressed_runtime_v003.py"
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
    "v003.py"
)
TEST_ROWS = (
    "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
    "primary_v002.py",
    "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
    "independent_v002.py",
    "scripts/test_compare_stage8_t7_actual_parent_regulated_car_operator_"
    "response_v003.py",
    "scripts/test_stage8_t7_launcher_v003.py",
    "scripts/test_stage8_t7_controller_v003.py",
)
REQUIRED_ROWS = (
    CONTROLLER_RELATIVE,
    LAUNCHER_RELATIVE,
    PRIMARY_RELATIVE,
    INDEPENDENT_RELATIVE,
    COMPARATOR_RELATIVE,
    *TEST_ROWS,
)

MANIFEST_RELATIVE = (
    "provenance/"
    "stage8_t7_actual_parent_regulated_car_operator_response_"
    "implementation_v002.json"
)

INDEPENDENT_JSON_RELATIVE = (
    "stage8_execution/work/"
    "T07_actual_parent_regulated_car_operator_response_"
    "independent_precomparison_v001.json"
)
INDEPENDENT_NPZ_RELATIVE = INDEPENDENT_JSON_RELATIVE[:-5] + ".npz"
PRIMARY_JSON_RELATIVE = (
    "stage8_execution/work/"
    "T07_actual_parent_regulated_car_operator_response_primary_v001.json"
)
PRIMARY_NPZ_RELATIVE = PRIMARY_JSON_RELATIVE[:-5] + ".npz"
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

EXPECTED_PATHS_VERIFIED_ABSENT = {
    "independent": [
        INDEPENDENT_JSON_RELATIVE,
        INDEPENDENT_NPZ_RELATIVE,
        PRIMARY_JSON_RELATIVE,
        PRIMARY_NPZ_RELATIVE,
        COMPARISON_JSON_RELATIVE,
        INDEPENDENT_RECEIPT_RELATIVE,
        PRIMARY_RECEIPT_RELATIVE,
        COMPARISON_RECEIPT_RELATIVE,
    ],
    "primary": [
        PRIMARY_JSON_RELATIVE,
        PRIMARY_NPZ_RELATIVE,
        COMPARISON_JSON_RELATIVE,
        PRIMARY_RECEIPT_RELATIVE,
        COMPARISON_RECEIPT_RELATIVE,
    ],
    "comparison": [
        COMPARISON_JSON_RELATIVE,
        COMPARISON_RECEIPT_RELATIVE,
    ],
}

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

# The stub comparator mirrors the REAL v003 comparator CLI contract exactly:
# every v002 argument, plus the required --independent-receipt-sha256 and
# --primary-receipt-sha256, recorded verbatim in the sealed output under
# independent_receipt_sha256 / primary_receipt_sha256 (repair binding V002,
# S1-1d). A controller that omits either flag fails this stub's argparse.
STUB_COMPARATOR_TEMPLATE = '''#!/usr/bin/env python3
"""Fixture stub comparator lane (real v003 CLI contract)."""
{helpers}
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--independent-json", type=Path, required=True)
    parser.add_argument("--independent-npz", type=Path, required=True)
    parser.add_argument("--primary-json", type=Path, required=True)
    parser.add_argument("--primary-npz", type=Path, required=True)
    parser.add_argument("--independent-json-sha256", required=True)
    parser.add_argument("--independent-npz-sha256", required=True)
    parser.add_argument("--primary-json-sha256", required=True)
    parser.add_argument("--primary-npz-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--controller-context", default=None)
    parser.add_argument("--independent-receipt-sha256", required=True)
    parser.add_argument("--primary-receipt-sha256", required=True)
    arguments = parser.parse_args()
    output = arguments.output
    payload = {{
        "schema": "fixture_stub_comparison_v003",
        "overall_verdict":
            "ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_COMPARISON_PASSED",
        "comparison_supports_actual_parent_regulated_CAR_operator_response": True,
        "comparison_supports_actual_parent_same_carrier_one_source_restriction": True,
        "resolved_input_paths": {{
            "independent_json": str(arguments.independent_json.resolve()),
            "independent_npz": str(arguments.independent_npz.resolve()),
            "primary_json": str(arguments.primary_json.resolve()),
            "primary_npz": str(arguments.primary_npz.resolve()),
        }},
        "resolved_output_path": str(output.resolve()),
        "controller_context": arguments.controller_context,
        "independent_receipt_sha256": arguments.independent_receipt_sha256,
        "primary_receipt_sha256": arguments.primary_receipt_sha256,
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
SPOOFED_RECEIPT_DIGEST = (
    '    payload["independent_receipt_sha256"] = "0" * 64\n'
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
        tempfile.mkdtemp(prefix=f"stage8_t7_controller_{label}_", dir=base)
    ).resolve()


def build_fixture(
    label: str,
    *,
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

    (fixture / CONTROLLER_RELATIVE).write_text(
        CONTROLLER_SOURCE.read_text(encoding="utf-8"), encoding="utf-8"
    )

    rows = [
        {"path": row, "sha256": sha256(fixture / row)}
        for row in REQUIRED_ROWS
        if row != omit_manifest_row
    ]
    manifest = fixture / MANIFEST_RELATIVE
    manifest.write_text(
        json.dumps(
            {
                "schema": (
                    "stage8_t7_actual_parent_regulated_car_operator_response_"
                    "implementation_v002"
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
    return fixture


def run_controller(fixture: Path, lane: str) -> subprocess.CompletedProcess:
    environment = dict(os.environ)
    environment.pop("STAGE8_T7_CONTROLLER_CONTEXT", None)
    return subprocess.run(
        [
            sys.executable,
            str(fixture / LAUNCHER_RELATIVE),
            CONTROLLER_RELATIVE,
            "--lane",
            lane,
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


def no_canonical_artifacts(fixture: Path) -> bool:
    """True when no canonical output, receipt, or adjacent seal exists."""
    for relative in (
        INDEPENDENT_JSON_RELATIVE,
        INDEPENDENT_NPZ_RELATIVE,
        PRIMARY_JSON_RELATIVE,
        PRIMARY_NPZ_RELATIVE,
        COMPARISON_JSON_RELATIVE,
        INDEPENDENT_RECEIPT_RELATIVE,
        PRIMARY_RECEIPT_RELATIVE,
        COMPARISON_RECEIPT_RELATIVE,
    ):
        if (fixture / relative).exists():
            return False
        if Path(f"{fixture / relative}.seal.sha256").exists():
            return False
    return True


def test_gpg_fully_removed() -> None:
    # Functional GPG remnants must be gone: the binary path, the pinned
    # fingerprint, signing/verification invocations, signature-path
    # constants, and the signature fields. (The docstring may still NAME
    # the removal, so prose words are not scanned.)
    source = CONTROLLER_SOURCE.read_text(encoding="utf-8")
    for forbidden in (
        "18488605",
        "/opt/homebrew/bin/gpg",
        "detach-sign",
        "VALIDSIG",
        "sign_receipt",
        "SIGNING_FINGERPRINT",
        "IMPLEMENTATION_SIGNATURE",
        "implementation_signature_fingerprint",
        "output_paths_absent_before_execution",
    ):
        require(
            forbidden not in source,
            f"controller v003 must not reference {forbidden!r}",
        )


def test_happy_path_and_immutability() -> None:
    fixture = build_fixture("happy")
    manifest_rows = {
        row["path"]: row["sha256"]
        for row in json.loads(
            (fixture / MANIFEST_RELATIVE).read_text(encoding="utf-8")
        )["files"]
    }

    lane_receipt_digests: dict[str, str] = {}
    for lane, receipt_relative in (
        ("independent", INDEPENDENT_RECEIPT_RELATIVE),
        ("primary", PRIMARY_RECEIPT_RELATIVE),
        ("comparison", COMPARISON_RECEIPT_RELATIVE),
    ):
        completed = run_controller(fixture, lane)
        require(
            completed.returncode == 0,
            f"happy-path {lane} lane failed: {completed.stderr[-4000:]}",
        )
        summary = json.loads(completed.stdout)
        require(summary.get("lane") == lane, f"{lane} summary lane mismatch")
        if lane == "comparison":
            require(
                summary.get("schema")
                == "stage8_t7_actual_parent_car_pipeline_summary_v003",
                "comparison summary schema mismatch",
            )
            require(
                summary.get("overall_verdict") == PASS_VERDICT,
                "summary verdict mismatch",
            )
        else:
            require(
                summary.get("schema")
                == "stage8_t7_actual_parent_car_lane_summary_v003",
                f"{lane} summary schema mismatch",
            )
            require(
                summary.get("receipt_sha256")
                == sha256(fixture / receipt_relative),
                f"{lane} summary receipt digest mismatch",
            )
        lane_receipt_digests[lane] = sha256(fixture / receipt_relative)

    require(
        lane_order(fixture) == ["independent", "primary", "comparison"],
        "lane order is not independent-then-primary-then-comparison",
    )

    for lane, receipt_relative, target_relative in (
        ("independent", INDEPENDENT_RECEIPT_RELATIVE, INDEPENDENT_RELATIVE),
        ("primary", PRIMARY_RECEIPT_RELATIVE, PRIMARY_RELATIVE),
        ("comparison", COMPARISON_RECEIPT_RELATIVE, COMPARATOR_RELATIVE),
    ):
        receipt = fixture / receipt_relative
        receipt_seal = Path(f"{receipt}.seal.sha256")
        require(receipt.is_file(), f"receipt absent: {receipt_relative}")
        require(receipt_seal.is_file(), f"receipt seal absent: {receipt_relative}")
        require(
            not Path(f"{receipt}.asc").exists(),
            f"no signature file may ever exist: {receipt_relative}",
        )
        require(read_only(receipt), f"receipt is not immutable: {receipt_relative}")
        require(read_only(receipt_seal), f"receipt seal is writable: {receipt_relative}")
        seal_fields = receipt_seal.read_text(encoding="ascii").split()
        require(seal_fields[0] == sha256(receipt), "receipt seal digest mismatch")
        payload = json.loads(receipt.read_text(encoding="utf-8"))
        require(
            payload.get("schema") == RECEIPT_SCHEMA,
            "receipt schema mismatch",
        )
        require(payload.get("status") == "SUCCEEDED", "receipt status mismatch")
        require(payload.get("lane") == lane, "receipt lane mismatch")
        require(
            "output_paths_absent_before_execution" not in payload,
            "hardcoded absence boolean must be gone from the v003 receipt",
        )
        require(
            "implementation_signature_fingerprint" not in payload,
            "signature fields must be gone from the v003 receipt",
        )
        require(
            payload.get("paths_verified_absent")
            == EXPECTED_PATHS_VERIFIED_ABSENT[lane],
            f"{lane} receipt paths_verified_absent is not the exact checked list",
        )
        expected_target = manifest_rows[target_relative]
        require(
            payload.get("target_sha256") == expected_target
            and payload.get("target_sha256_pre_execution") == expected_target
            and payload.get("target_sha256_post_execution") == expected_target,
            "receipt pre/post target digests do not match the manifest row",
        )

    # Receipt-digest passthrough: the sealed comparison output must record
    # the true digests of the two sealed lane-receipt FILES verbatim.
    comparison = json.loads(
        (fixture / COMPARISON_JSON_RELATIVE).read_text(encoding="utf-8")
    )
    require(
        comparison.get("independent_receipt_sha256")
        == lane_receipt_digests["independent"],
        "comparison output did not record the independent receipt digest",
    )
    require(
        comparison.get("primary_receipt_sha256") == lane_receipt_digests["primary"],
        "comparison output did not record the primary receipt digest",
    )

    # Re-running any lane must block in pre-flight on the existing artifacts.
    rerun = run_controller(fixture, "independent")
    require(rerun.returncode != 0, "rerun must block on existing canonical paths")
    require(
        "pre-flight: canonical path already exists" in rerun.stderr,
        "rerun did not block in pre-flight",
    )


def test_lane_order_refusal() -> None:
    fixture = build_fixture("lane_order")

    primary_first = run_controller(fixture, "primary")
    require(primary_first.returncode != 0, "primary without independent must block")
    require(
        "lane-order violation" in primary_first.stderr
        and "independent receipt is absent" in primary_first.stderr,
        "primary-first refusal used the wrong fence",
    )
    require(lane_order(fixture) == [], "no lane may run on a lane-order refusal")
    require(
        no_canonical_artifacts(fixture),
        "lane-order refusal must precede any canonical artifact",
    )

    comparison_first = run_controller(fixture, "comparison")
    require(comparison_first.returncode != 0, "comparison without receipts must block")
    require(
        "lane-order violation" in comparison_first.stderr,
        "comparison-first refusal used the wrong fence",
    )
    require(no_canonical_artifacts(fixture), "comparison-first refusal wrote artifacts")

    independent = run_controller(fixture, "independent")
    require(independent.returncode == 0, "independent lane should run first")

    skip_primary = run_controller(fixture, "comparison")
    require(skip_primary.returncode != 0, "comparison without primary must block")
    require(
        "lane-order violation" in skip_primary.stderr
        and "primary receipt is absent" in skip_primary.stderr,
        "primary-skip refusal used the wrong fence",
    )
    require(
        lane_order(fixture) == ["independent"],
        "comparison must not run without the primary receipt",
    )
    require(
        not (fixture / COMPARISON_RECEIPT_RELATIVE).exists()
        and not (fixture / COMPARISON_JSON_RELATIVE).exists(),
        "primary-skip refusal must precede any comparison artifact",
    )


def test_missing_manifest_row_blocks() -> None:
    fixture = build_fixture("missing_row", omit_manifest_row=TEST_ROWS[2])
    completed = run_controller(fixture, "independent")
    require(completed.returncode != 0, "missing required row must block")
    require(
        "implementation manifest is missing required rows" in completed.stderr,
        "missing-row block used the wrong fence",
    )
    require(lane_order(fixture) == [], "no lane may run when a required row is missing")
    require(
        no_canonical_artifacts(fixture),
        "missing-row block must precede any canonical artifact",
    )


def test_preexisting_canonical_output_blocks() -> None:
    # B1 attestation direction: a pre-existing PRIMARY output must block the
    # INDEPENDENT lane in pre-flight, before the lane runs or any receipt or
    # output of this invocation exists.
    fixture = build_fixture("preexisting")
    stray = fixture / PRIMARY_JSON_RELATIVE
    stray.write_text("{\"stray\": true}\n", encoding="utf-8")
    completed = run_controller(fixture, "independent")
    require(completed.returncode != 0, "pre-existing canonical output must block")
    require(
        "pre-flight: canonical path already exists" in completed.stderr,
        "pre-existing output block used the wrong fence",
    )
    require(lane_order(fixture) == [], "no lane may run past a dirty pre-flight")
    require(
        not (fixture / INDEPENDENT_JSON_RELATIVE).exists()
        and not (fixture / INDEPENDENT_RECEIPT_RELATIVE).exists(),
        "pre-flight failure must precede any output of this invocation",
    )


def test_pre_execution_rehash_blocks() -> None:
    # The independent lane's stub mutates the primary target; the primary
    # invocation's pre-flight must catch the drift before anything runs.
    fixture = build_fixture("pre_swap", independent_extra=CROSS_MUTATION)
    independent = run_controller(fixture, "independent")
    require(
        independent.returncode == 0,
        f"independent lane should succeed here: {independent.stderr[-2000:]}",
    )
    completed = run_controller(fixture, "primary")
    require(completed.returncode != 0, "pre-execution target swap must block")
    require(
        f"implementation drift: {PRIMARY_RELATIVE}" in completed.stderr,
        "pre-execution swap used the wrong fence",
    )
    require(
        lane_order(fixture) == ["independent"],
        "the swapped primary lane must never run",
    )
    require(
        not (fixture / PRIMARY_RECEIPT_RELATIVE).exists()
        and not (fixture / PRIMARY_JSON_RELATIVE).exists(),
        "no receipt may attribute provenance to unexamined code",
    )


def test_post_execution_rehash_blocks() -> None:
    fixture = build_fixture("post_swap", independent_extra=SELF_MUTATION)
    completed = run_controller(fixture, "independent")
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
        lane_order(fixture) == ["independent"],
        "pipeline must stop at the drifted lane",
    )
    # The self-mutated independent target now also breaks the manifest
    # binding, so the next invocation must die in pre-flight.
    blocked_primary = run_controller(fixture, "primary")
    require(
        blocked_primary.returncode != 0
        and f"implementation drift: {INDEPENDENT_RELATIVE}" in blocked_primary.stderr,
        "the drifted workspace must block the next lane in pre-flight",
    )
    require(
        not (fixture / PRIMARY_JSON_RELATIVE).exists()
        and not (fixture / PRIMARY_RECEIPT_RELATIVE).exists(),
        "the blocked primary invocation must not produce artifacts",
    )


def test_blocked_prior_receipt_refused() -> None:
    # A prior receipt that exists and seals correctly but records BLOCKED
    # must not satisfy lane-order enforcement.
    fixture = build_fixture("blocked_receipt")
    receipt = fixture / INDEPENDENT_RECEIPT_RELATIVE
    receipt.write_text(
        json.dumps(
            {
                "schema": RECEIPT_SCHEMA,
                "lane": "independent",
                "status": "BLOCKED",
                "runtime_manifest_sha256": RUNTIME_MANIFEST_SHA256,
                "outputs": [],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    Path(f"{receipt}.seal.sha256").write_text(
        f"{sha256(receipt)}  {receipt.name}\n", encoding="ascii"
    )
    completed = run_controller(fixture, "primary")
    require(completed.returncode != 0, "a BLOCKED prior receipt must block")
    require(
        "does not record a SUCCEEDED lane" in completed.stderr,
        "BLOCKED-receipt refusal used the wrong fence",
    )
    require(lane_order(fixture) == [], "no lane may run behind a BLOCKED receipt")
    require(
        not (fixture / PRIMARY_JSON_RELATIVE).exists()
        and not (fixture / PRIMARY_RECEIPT_RELATIVE).exists(),
        "BLOCKED-receipt refusal must precede any artifact",
    )


def test_comparator_path_crosscheck_blocks() -> None:
    fixture = build_fixture("spoofed_paths", comparator_override=SPOOFED_OUTPUT_PATH)
    for lane in ("independent", "primary"):
        completed = run_controller(fixture, lane)
        require(completed.returncode == 0, f"{lane} lane should pass here")
    completed = run_controller(fixture, "comparison")
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


def test_receipt_digest_crosscheck_blocks() -> None:
    fixture = build_fixture(
        "spoofed_receipt_digest", comparator_override=SPOOFED_RECEIPT_DIGEST
    )
    for lane in ("independent", "primary"):
        completed = run_controller(fixture, lane)
        require(completed.returncode == 0, f"{lane} lane should pass here")
    completed = run_controller(fixture, "comparison")
    require(completed.returncode != 0, "spoofed recorded receipt digest must block")
    require(
        "comparator did not record the independent receipt digest verbatim"
        in completed.stderr,
        "receipt-digest cross-check used the wrong fence",
    )


def main() -> int:
    require(PINNED_PYTHON.is_file(), "pinned runtime python is absent")
    tests = (
        test_gpg_fully_removed,
        test_happy_path_and_immutability,
        test_lane_order_refusal,
        test_missing_manifest_row_blocks,
        test_preexisting_canonical_output_blocks,
        test_pre_execution_rehash_blocks,
        test_post_execution_rehash_blocks,
        test_blocked_prior_receipt_refused,
        test_comparator_path_crosscheck_blocks,
        test_receipt_digest_crosscheck_blocks,
    )
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"controller_v003_tests_passed {len(tests)}/{len(tests)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
