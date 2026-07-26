#!/usr/bin/env python3
"""Integration tests for the v005 actual-parent CAR controller.

Two disjoint regimes, per STAGE8_REAL_COMPONENT_PRECONDITION_DISCIPLINE_V001:

FIXTURE regime (lane INTERNALS stubbed, as before): every scenario runs
against a throwaway fixture workspace built under a temporary directory
(scratchpad when STAGE8_T7_TEST_SCRATCH is set) with stub lane scripts, a
stub launcher, a fixture git archive (bare file:// remote), copies of the
REAL sealed authority files (M2 digests must verify against real bytes),
and BOTH fixture manifests: the controller's own v004-path implementation
manifest and the bridge (v001-path) manifest the frozen derive lanes verify
and stamp. The canonical workspace is only ever read; the copied
controller's pinned archive-repository path is repointed at the fixture
archive.

REAL-COMPONENT regime (discipline rule 1, the MECHANICAL-RULE test the
prior suites lacked): test_real_chain_startability drives the REAL v005
launcher at its canonical path -> the REAL v005 controller --preflight-only
--lane independent against the CANONICAL workspace, read-only. Until the
sealed v004 implementation manifest exists, this must exit nonzero with the
precise block reason naming the absent manifest — which PROVES the real
chain starts, the launcher's allowlist resolves the controller (the exact
B1 defect), the runtime-marker gate passes, and pre-flight is reached with
zero artifacts. The test also proves --preflight-only performs no canonical
write (before/after tree scan of the controller's entire write surface).

v005 additions covered: M1 bundle-stamp pre-flight member (happy path plus
the inter-invocation regeneration hazard), M2 authority-digest pre-flight
(happy path, tampered authority, absent authority), --preflight-only
(PREFLIGHT_OK with zero writes anywhere; precise block reasons), and the
frozen PRECONDITIONS enumeration.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTROLLER_SOURCE = ROOT / "scripts/run_stage8_t7_actual_parent_car_pipeline_v005.py"
REAL_LAUNCHER = ROOT / "scripts/launch_stage8_t7_content_addressed_runtime_v005.py"
PINNED_PYTHON = Path(
    "/Users/bgm/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/python/bin/python3"
)
RUNTIME_MANIFEST_SHA256 = (
    "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b"
)
PASS_VERDICT = "ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_COMPARISON_PASSED"
RECEIPT_SCHEMA = "stage8_t7_local_sealed_execution_receipt_v003"
ARCHIVE_PATH_LITERAL = "/Users/bgm/MB Work/alpha-program-archive"

CONTROLLER_RELATIVE = "scripts/run_stage8_t7_actual_parent_car_pipeline_v005.py"
LAUNCHER_RELATIVE = "scripts/launch_stage8_t7_content_addressed_runtime_v005.py"
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
    "v005.py"
)
TEST_ROWS = (
    "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
    "primary_v002.py",
    "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
    "independent_v002.py",
    "scripts/test_compare_stage8_t7_actual_parent_regulated_car_operator_"
    "response_v005.py",
    "scripts/test_stage8_t7_launcher_v005.py",
    "scripts/test_stage8_t7_controller_v005.py",
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
    "implementation_v004.json"
)
BRIDGE_MANIFEST_RELATIVE = (
    "provenance/"
    "stage8_t7_actual_parent_regulated_car_operator_response_"
    "implementation_v001.json"
)
# The production v001-path manifest also carries frozen v002-era rows the
# derive lanes verify against disk; the fixture mirrors that shape with one
# legacy row backed by a stub file.
LEGACY_BRIDGE_RELATIVE = "scripts/launch_stage8_t7_content_addressed_runtime_v002.py"
BRIDGE_ROWS = (INDEPENDENT_RELATIVE, PRIMARY_RELATIVE, LEGACY_BRIDGE_RELATIVE)

# M2: the REAL sealed authority files the frozen derive lanes and comparator
# verify at runtime. The fixture copies these canonical bytes verbatim so
# the controller's frozen AUTHORITY_DIGESTS inventory verifies against real
# sealed content (no fabricated digests). Read-only with respect to the
# canonical workspace.
AUTHORITY_RELATIVES = (
    "STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md",
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md",
    "STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md",
    "STAGE8_ROUTE1_SPECIAL_CASE_CONSISTENCY_BINDING_V001.md",
    "STAGE8_ROUTE2_CAR_STATE_BRIDGE_SCOPE_CORRECTION_V001.md",
    "STAGE8_ROUTE2_COMPLETE_QSPEC_STATE_BINDING_V001.md",
    "STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md",
    "STAGE8_T7_EXACT_HERMITE_MIXED_COVARIANCE_RESULT_V001.md",
    "STAGE8_T7_GAUSSIAN_PATH_SUM_REDUCTION_RESULT_V001.md",
    "STAGE8_T7_HERMITE_GALERKIN_BASELINE_SPEC_V001.md",
    "STAGE8_T7_HERMITE_GALERKIN_NUMERICS_PROTOCOL_V001.md",
    "STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_"
    "AMENDMENT_V001.md",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_RESULT_V001.md",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md",
    "STAGE8_T7_PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_RESULT_V001.md",
    "provenance/stage8_t7_numpy_runtime_manifest_v001.json",
    "scripts/derive_stage8_t7_primitive_operator_response_v001.py",
    "stage8_execution/work/T07_hermite_galerkin_baseline.json",
    "stage8_execution/work/T07_hermite_galerkin_baseline_verification.json",
)

EXPECTED_PRECONDITIONS = (
    "runtime_attestation",
    "implementation_manifest",
    "authority_digests",
    "bridge_binding",
    "push_capability",
    "prior_receipts",
    "comparison_bundle_stamps",
    "canonical_absences",
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
CANONICAL_ARTIFACT_RELATIVES = (
    INDEPENDENT_JSON_RELATIVE,
    INDEPENDENT_NPZ_RELATIVE,
    PRIMARY_JSON_RELATIVE,
    PRIMARY_NPZ_RELATIVE,
    COMPARISON_JSON_RELATIVE,
    INDEPENDENT_RECEIPT_RELATIVE,
    PRIMARY_RECEIPT_RELATIVE,
    COMPARISON_RECEIPT_RELATIVE,
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

# M1: the stub derive lanes mirror the REAL byte-frozen lanes' bundle stamp:
# implementation_manifest_sha256 = the digest of the sealed manifest at the
# canonical v001 path, recomputed from disk at stamping time.
STUB_DERIVE_TEMPLATE = '''#!/usr/bin/env python3
"""Fixture stub {lane} lane (stamps the v001-path manifest digest)."""
{helpers}

def main():
    work = ROOT / "stage8_execution/work"
    work.mkdir(parents=True, exist_ok=True)
    bridge = ROOT / "{bridge_relative}"
    out_json = work / "{json_name}"
    out_npz = out_json.with_suffix(".npz")
    out_json.write_text(
        json.dumps(
            {{
                "lane": "{lane}",
                "implementation_manifest_sha256": file_sha256(bridge),
            }}
        )
        + "\\n",
        encoding="utf-8",
    )
    out_npz.write_bytes(b"NPZ-STUB-{lane}")
    seal(out_json)
    seal(out_npz)
    log_lane("{lane}")
{extra}

main()
'''

# The stub comparator mirrors the REAL comparator CLI contract exactly:
# every v002 argument, plus the required --independent-receipt-sha256 and
# --primary-receipt-sha256, recorded verbatim in the sealed output under
# independent_receipt_sha256 / primary_receipt_sha256 (repair binding V002,
# S1-1d; unchanged by v005, which is pre-flight-side, not CLI-side).
# A controller that omits either flag fails this stub's argparse.
STUB_COMPARATOR_TEMPLATE = '''#!/usr/bin/env python3
"""Fixture stub comparator lane (real v005 CLI contract)."""
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
        "schema": "fixture_stub_comparison_v005",
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


def git(*args: str) -> None:
    completed = subprocess.run(
        ["git", *args], check=False, capture_output=True, text=True
    )
    require(
        completed.returncode == 0,
        f"fixture git command failed: git {' '.join(args)}: {completed.stderr}",
    )


def initialise_archive_fixture(fixture: Path, *, push_broken: bool) -> None:
    """Fixture archive: a work repository whose origin is a bare file://
    remote (push --dry-run succeeds without any network), or — for the
    fail-closed scenario — a nonexistent remote (push --dry-run fails)."""
    remote = fixture / "archive_remote.git"
    work = fixture / "archive_work"
    git("init", "-q", "--bare", str(remote))
    git("init", "-q", "-b", "main", str(work))
    git(
        "-C",
        str(work),
        "-c",
        "user.email=fixture@example.invalid",
        "-c",
        "user.name=fixture",
        "commit",
        "--allow-empty",
        "-q",
        "-m",
        "fixture anchor point",
    )
    if push_broken:
        url = (fixture / "absent_remote.git").as_uri()
    else:
        url = remote.as_uri()
    git("-C", str(work), "remote", "add", "origin", url)


def build_fixture(
    label: str,
    *,
    independent_extra: str = "",
    comparator_override: str = "",
    omit_manifest_row: str = "",
    bridge_mismatch_row: str = "",
    push_broken: bool = False,
) -> Path:
    fixture = scratch_directory(label)
    (fixture / "scripts").mkdir()
    (fixture / "provenance").mkdir()
    (fixture / "stage8_execution/work").mkdir(parents=True)
    initialise_archive_fixture(fixture, push_broken=push_broken)

    # M2: copy the REAL sealed authority files verbatim (canonical workspace
    # read-only) so the controller's frozen digests verify against real bytes.
    for relative in AUTHORITY_RELATIVES:
        source_path = ROOT / relative
        require(source_path.is_file(), f"canonical authority absent: {relative}")
        destination = fixture / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source_path, destination)

    (fixture / LAUNCHER_RELATIVE).write_text(STUB_LAUNCHER, encoding="utf-8")
    (fixture / INDEPENDENT_RELATIVE).write_text(
        STUB_DERIVE_TEMPLATE.format(
            lane="independent",
            helpers=STUB_HELPERS,
            bridge_relative=BRIDGE_MANIFEST_RELATIVE,
            json_name=Path(INDEPENDENT_JSON_RELATIVE).name,
            extra=independent_extra,
        ),
        encoding="utf-8",
    )
    (fixture / PRIMARY_RELATIVE).write_text(
        STUB_DERIVE_TEMPLATE.format(
            lane="primary",
            helpers=STUB_HELPERS,
            bridge_relative=BRIDGE_MANIFEST_RELATIVE,
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
    (fixture / LEGACY_BRIDGE_RELATIVE).write_text(
        "# fixture legacy v002 launcher stub (bridge-manifest disk row)\n",
        encoding="utf-8",
    )

    source = CONTROLLER_SOURCE.read_text(encoding="utf-8")
    require(
        ARCHIVE_PATH_LITERAL in source,
        "controller v005 must pin the archive repository path",
    )
    (fixture / CONTROLLER_RELATIVE).write_text(
        source.replace(ARCHIVE_PATH_LITERAL, str(fixture / "archive_work")),
        encoding="utf-8",
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
                    "implementation_v004"
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

    # Bridge (v001-path) manifest: the object the frozen derive lanes verify
    # and stamp. Rows are consistent with the own manifest unless a
    # mismatched-rows scenario is requested.
    bridge_rows = []
    for row in BRIDGE_ROWS:
        digest = sha256(fixture / row)
        if row == bridge_mismatch_row:
            digest = "0" * 64
        bridge_rows.append({"path": row, "sha256": digest})
    bridge_manifest = fixture / BRIDGE_MANIFEST_RELATIVE
    bridge_manifest.write_text(
        json.dumps(
            {
                "schema": (
                    "stage8_t7_actual_parent_regulated_car_operator_response_"
                    "implementation_v001"
                ),
                "files": bridge_rows,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    Path(f"{bridge_manifest}.seal.sha256").write_text(
        f"{sha256(bridge_manifest)}  {bridge_manifest.name}\n", encoding="ascii"
    )
    return fixture


def run_controller(
    fixture: Path, lane: str, *extra: str
) -> subprocess.CompletedProcess:
    environment = dict(os.environ)
    environment.pop("STAGE8_T7_CONTROLLER_CONTEXT", None)
    return subprocess.run(
        [
            sys.executable,
            str(fixture / LAUNCHER_RELATIVE),
            CONTROLLER_RELATIVE,
            "--lane",
            lane,
            *extra,
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
    for relative in CANONICAL_ARTIFACT_RELATIVES:
        if (fixture / relative).exists():
            return False
        if Path(f"{fixture / relative}.seal.sha256").exists():
            return False
    return True


def tree_scan(root: Path, *, exclude_top: tuple[str, ...] = ()) -> dict[str, tuple]:
    """Map every file under root (minus excluded top-level entries) to its
    (size, mtime_ns): any write — create, modify, delete, touch — changes
    the map."""
    result: dict[str, tuple] = {}
    for current, directories, files in os.walk(root):
        current_path = Path(current)
        if current_path == root:
            directories[:] = [
                name for name in directories if name not in exclude_top
            ]
        for name in files:
            path = current_path / name
            try:
                info = path.stat()
            except FileNotFoundError:
                continue
            result[str(path.relative_to(root))] = (info.st_size, info.st_mtime_ns)
    return result


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
            f"controller v005 must not reference {forbidden!r}",
        )


def test_preconditions_enumerated() -> None:
    # Sealed discipline rule 2: the preconditions are ENUMERATED in the
    # controlling artifact as a module-level frozen tuple, in the documented
    # order. Executed module-level (no main()), no writes.
    namespace = {
        "__file__": str(CONTROLLER_SOURCE),
        "__name__": "controller_v005_under_test",
    }
    exec(  # noqa: S102 - deliberate: load the real module-level constants
        compile(
            CONTROLLER_SOURCE.read_text(encoding="utf-8"),
            str(CONTROLLER_SOURCE),
            "exec",
        ),
        namespace,
    )
    preconditions = namespace.get("PRECONDITIONS")
    require(
        isinstance(preconditions, tuple),
        "PRECONDITIONS must be a module-level tuple",
    )
    require(
        preconditions == EXPECTED_PRECONDITIONS,
        f"PRECONDITIONS enumeration mismatch: {preconditions!r}",
    )
    steps = namespace.get("PRECONDITION_STEPS")
    require(
        isinstance(steps, dict) and set(steps) == set(EXPECTED_PRECONDITIONS),
        "every enumerated precondition must have exactly one dispatch step",
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

    # M1 happy path is load-bearing here: the comparison lane ran only
    # because both stub bundles' stamped implementation_manifest_sha256
    # equalled the recomputed v001-path manifest digest.

    # The push-capability pre-flight is a DRY RUN: after all three lanes the
    # bare fixture remote must still hold no refs (nothing was pushed).
    refs = subprocess.run(
        ["git", "-C", str(fixture / "archive_remote.git"), "for-each-ref"],
        check=False,
        capture_output=True,
        text=True,
    )
    require(
        refs.returncode == 0 and refs.stdout.strip() == "",
        "the push-capability dry run must never actually push",
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
            "hardcoded absence boolean must be gone from the receipt",
        )
        require(
            "implementation_signature_fingerprint" not in payload,
            "signature fields must be gone from the receipt",
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


def test_bridge_row_mismatch_blocks() -> None:
    # FIX 1 (retained): the entire bridge condition is pre-flighted BEFORE
    # any lane runs. A v001-path manifest whose derive-executor row disagrees
    # with the controller's own manifest must block with ZERO artifacts.
    fixture = build_fixture(
        "bridge_mismatch", bridge_mismatch_row=PRIMARY_RELATIVE
    )
    completed = run_controller(fixture, "independent")
    require(completed.returncode != 0, "mismatched bridge rows must block")
    require(
        f"bridge pre-flight: manifest row mismatch for {PRIMARY_RELATIVE}"
        in completed.stderr,
        "bridge-mismatch block used the wrong fence",
    )
    require(lane_order(fixture) == [], "no lane may run past a broken bridge")
    require(
        no_canonical_artifacts(fixture),
        "the bridge pre-flight must block BEFORE any canonical artifact exists",
    )


def test_bridge_manifest_absent_blocks() -> None:
    # The bridge condition requires the sealed v001-path manifest ON DISK;
    # its absence must block before any lane and before any artifact.
    fixture = build_fixture("bridge_absent")
    (fixture / BRIDGE_MANIFEST_RELATIVE).unlink()
    completed = run_controller(fixture, "independent")
    require(completed.returncode != 0, "absent bridge manifest must block")
    require(
        "bridge pre-flight: v001-path implementation manifest is absent"
        in completed.stderr,
        "bridge-absence block used the wrong fence",
    )
    require(lane_order(fixture) == [], "no lane may run without the bridge manifest")
    require(
        no_canonical_artifacts(fixture),
        "bridge-absence block must precede any canonical artifact",
    )


def test_authority_digest_mismatch_blocks() -> None:
    # M2: a tampered runtime authority must block in pre-flight, before any
    # lane runs and before any canonical artifact exists (previously the
    # drift surfaced only inside a lane, after canonical commitment).
    tampered = "STAGE8_T7_HERMITE_GALERKIN_BASELINE_SPEC_V001.md"
    fixture = build_fixture("authority_tamper")
    (fixture / tampered).write_text(
        "# tampered authority (fixture)\n", encoding="utf-8"
    )
    completed = run_controller(fixture, "independent")
    require(completed.returncode != 0, "tampered authority must block")
    require(
        f"authority pre-flight: authority digest mismatch: {tampered}"
        in completed.stderr,
        "authority-tamper block used the wrong fence",
    )
    require(lane_order(fixture) == [], "no lane may run past a tampered authority")
    require(
        no_canonical_artifacts(fixture),
        "authority-tamper block must precede any canonical artifact",
    )


def test_authority_absent_blocks() -> None:
    # M2: an absent runtime authority must block in pre-flight with the
    # precise fence naming the file.
    absent = "STAGE8_T7_GAUSSIAN_PATH_SUM_REDUCTION_RESULT_V001.md"
    fixture = build_fixture("authority_absent")
    (fixture / absent).unlink()
    completed = run_controller(fixture, "independent")
    require(completed.returncode != 0, "absent authority must block")
    require(
        f"authority pre-flight: authority is absent: {absent}" in completed.stderr,
        "authority-absence block used the wrong fence",
    )
    require(lane_order(fixture) == [], "no lane may run without its authorities")
    require(
        no_canonical_artifacts(fixture),
        "authority-absence block must precede any canonical artifact",
    )


def test_bundle_stamp_mismatch_blocks() -> None:
    # M1: the inter-invocation regeneration hazard. Both derive lanes run
    # honestly; then the independent bundle is regenerated on disk with a
    # foreign manifest stamp and a VALID adjacent seal (exactly what a lane
    # re-run against a different manifest would leave). The comparison
    # invocation's pre-flight must catch the stamp mismatch BEFORE the
    # canonical comparison path is consumed: no comparison lane run, no
    # comparison output, no comparison receipt.
    fixture = build_fixture("bundle_stamp")
    for lane in ("independent", "primary"):
        completed = run_controller(fixture, lane)
        require(completed.returncode == 0, f"{lane} lane should pass here")
    bundle = fixture / INDEPENDENT_JSON_RELATIVE
    payload = json.loads(bundle.read_text(encoding="utf-8"))
    payload["implementation_manifest_sha256"] = "0" * 64
    bundle.write_text(json.dumps(payload) + "\n", encoding="utf-8")
    Path(f"{bundle}.seal.sha256").write_text(
        f"{sha256(bundle)}  {bundle.name}\n", encoding="ascii"
    )
    completed = run_controller(fixture, "comparison")
    require(completed.returncode != 0, "a foreign bundle stamp must block")
    require(
        "bundle-stamp pre-flight: independent bundle stamp does not equal "
        "the recomputed v001-path manifest digest" in completed.stderr,
        "bundle-stamp block used the wrong fence",
    )
    require(
        lane_order(fixture) == ["independent", "primary"],
        "the comparison lane must never run behind a foreign bundle stamp",
    )
    require(
        not (fixture / COMPARISON_JSON_RELATIVE).exists()
        and not (fixture / COMPARISON_RECEIPT_RELATIVE).exists(),
        "the bundle-stamp block must precede any comparison artifact",
    )


def test_push_capability_failure_blocks() -> None:
    # Retained from v004: a push failure discovered after sealing reproduces
    # the GPG wedge, so push capability is pre-flighted fail-closed.
    fixture = build_fixture("push_broken", push_broken=True)
    completed = run_controller(fixture, "independent")
    require(completed.returncode != 0, "a failing dry-run push must block")
    require(
        "push-capability pre-flight failed" in completed.stderr,
        "push-capability block used the wrong fence",
    )
    require(lane_order(fixture) == [], "no lane may run without push capability")
    require(
        no_canonical_artifacts(fixture),
        "push-capability block must precede any canonical artifact",
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
    # A pre-existing PRIMARY output must block the INDEPENDENT lane in
    # pre-flight, before the lane runs or any receipt or output of this
    # invocation exists.
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


def test_preflight_only_ok_and_writes_nothing() -> None:
    # The sealed discipline's instrument, fixture side: --preflight-only on
    # a clean workspace runs EVERY enumerated precondition, exits 0 with a
    # one-line PREFLIGHT_OK json, and performs NO write anywhere in the
    # workspace (full before/after tree scan; the fixture git archive is
    # excluded as test scaffolding — the happy-path test separately proves
    # the dry run pushes nothing).
    fixture = build_fixture("preflight_ok")
    before = tree_scan(fixture, exclude_top=("archive_remote.git", "archive_work"))
    completed = run_controller(fixture, "independent", "--preflight-only")
    after = tree_scan(fixture, exclude_top=("archive_remote.git", "archive_work"))
    require(
        completed.returncode == 0,
        f"--preflight-only should pass on a clean fixture: {completed.stderr[-4000:]}",
    )
    lines = [line for line in completed.stdout.splitlines() if line.strip()]
    require(len(lines) == 1, "--preflight-only must print exactly one line")
    summary = json.loads(lines[0])
    require(
        summary.get("schema") == "stage8_t7_preflight_only_summary_v001"
        and summary.get("status") == "PREFLIGHT_OK"
        and summary.get("lane") == "independent",
        "PREFLIGHT_OK summary malformed",
    )
    require(
        tuple(summary.get("preconditions", ())) == EXPECTED_PRECONDITIONS,
        "PREFLIGHT_OK must enumerate the frozen PRECONDITIONS in order",
    )
    require(
        summary.get("paths_verified_absent")
        == EXPECTED_PATHS_VERIFIED_ABSENT["independent"],
        "PREFLIGHT_OK absence list is not the exact checked list",
    )
    require(
        summary.get("implementation_manifest_sha256")
        == sha256(fixture / MANIFEST_RELATIVE)
        and summary.get("bridge_manifest_sha256")
        == sha256(fixture / BRIDGE_MANIFEST_RELATIVE),
        "PREFLIGHT_OK must record both recomputed manifest digests",
    )
    require(before == after, "--preflight-only must not write anywhere")
    require(lane_order(fixture) == [], "--preflight-only must not run any lane")
    require(
        no_canonical_artifacts(fixture),
        "--preflight-only must leave zero canonical artifacts",
    )


def test_preflight_only_blocks_lane_order() -> None:
    # --preflight-only must surface the same precise fail-closed fences,
    # still with zero writes.
    fixture = build_fixture("preflight_block")
    before = tree_scan(fixture, exclude_top=("archive_remote.git", "archive_work"))
    completed = run_controller(fixture, "comparison", "--preflight-only")
    after = tree_scan(fixture, exclude_top=("archive_remote.git", "archive_work"))
    require(
        completed.returncode != 0,
        "--preflight-only comparison without receipts must exit nonzero",
    )
    require(
        "lane-order violation" in completed.stderr
        and "independent receipt is absent" in completed.stderr,
        "--preflight-only block used the wrong fence",
    )
    lines = [line for line in completed.stdout.splitlines() if line.strip()]
    require(len(lines) == 1, "blocked --preflight-only must print exactly one line")
    summary = json.loads(lines[0])
    require(
        summary.get("status") == "PREFLIGHT_BLOCKED"
        and "lane-order violation" in str(summary.get("reason")),
        "blocked --preflight-only summary malformed",
    )
    require(before == after, "blocked --preflight-only must not write anywhere")
    require(lane_order(fixture) == [], "--preflight-only must not run any lane")
    require(
        no_canonical_artifacts(fixture),
        "blocked --preflight-only must leave zero canonical artifacts",
    )


def test_real_chain_startability() -> None:
    # THE MECHANICAL-RULE TEST (sealed discipline rule 1; the test every
    # prior suite lacked). Drives the REAL v005 launcher at its canonical
    # path -> the REAL v005 controller --preflight-only --lane independent
    # against the CANONICAL workspace, read-only: no copy, no stub, no
    # monkeypatch. This is the exact invocation shape of production.
    #
    # Until the sealed v004 implementation manifest exists (it is built by
    # the construction lane AFTER verification), the run must exit nonzero
    # with the precise block reason naming the absent manifest. That block
    # reason PROVES, on the real components: the chain starts; the launcher
    # allowlist resolves this controller (the exact B1 defect class); the
    # runtime-marker gate passes (the failure is NOT the marker fence); and
    # pre-flight is reached with zero artifacts. Once the manifest exists,
    # the same invocation must instead reach a strictly later enumerated
    # precondition or PREFLIGHT_OK — either way the chain is startable.
    require(
        REAL_LAUNCHER.is_file(),
        "REAL-COMPONENT FINDING: canonical launcher v005 is absent; "
        "the real chain cannot be driven (discipline rule 1 requires "
        "dispositioning this before sealing)",
    )
    require(PINNED_PYTHON.is_file(), "pinned runtime python is absent")
    manifest = ROOT / MANIFEST_RELATIVE

    for relative in CANONICAL_ARTIFACT_RELATIVES:
        require(
            not (ROOT / relative).exists(),
            f"canonical artifact already exists before the startability probe: "
            f"{relative}",
        )

    # The controller's entire canonical write surface: receipts + seals go
    # under provenance/, outputs + seals under stage8_execution/. Scan both
    # completely (size + mtime_ns) before and after.
    before_provenance = tree_scan(ROOT / "provenance")
    before_execution = tree_scan(ROOT / "stage8_execution")

    environment = dict(os.environ)
    environment.pop("STAGE8_T7_CONTROLLER_CONTEXT", None)
    completed = subprocess.run(
        [
            str(PINNED_PYTHON),
            "-I",
            "-S",
            str(REAL_LAUNCHER),
            CONTROLLER_RELATIVE,
            "--lane",
            "independent",
            "--preflight-only",
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        env=environment,
    )

    after_provenance = tree_scan(ROOT / "provenance")
    after_execution = tree_scan(ROOT / "stage8_execution")

    # Startability facts, provable from the observed fences regardless of
    # outcome: the launcher accepted the controller target (no allowlist
    # fence) and the controller saw the launcher's marker (no marker fence).
    require(
        "runtime target is not allowlisted" not in completed.stderr,
        "REAL-COMPONENT FINDING (B1 class): launcher v005 does not "
        f"allowlist the v005 controller: {completed.stderr[-2000:]}",
    )
    require(
        "pipeline requires the sealed runtime launcher" not in completed.stderr,
        "the real launcher's runtime marker did not reach the controller",
    )

    if not manifest.is_file():
        # Pre-construction: the precise enumerated block, nothing else.
        require(
            completed.returncode != 0,
            "the pre-construction probe must block (manifest v004 absent)",
        )
        expected_reason = (
            "implementation manifest is absent: "
            "provenance/stage8_t7_actual_parent_regulated_car_operator_"
            "response_implementation_v004.json"
        )
        require(
            expected_reason in completed.stderr,
            "the block reason must name the absent v004 manifest precisely; "
            f"got: {completed.stderr[-2000:]}",
        )
        lines = [line for line in completed.stdout.splitlines() if line.strip()]
        require(
            len(lines) == 1,
            "blocked --preflight-only must print exactly one line",
        )
        summary = json.loads(lines[0])
        require(
            summary.get("status") == "PREFLIGHT_BLOCKED"
            and expected_reason in str(summary.get("reason"))
            and tuple(summary.get("preconditions", ()))
            == EXPECTED_PRECONDITIONS,
            "blocked PREFLIGHT summary must carry the precise reason and the "
            "frozen enumeration",
        )
    else:
        # Post-construction: the same real invocation must reach a strictly
        # later enumerated precondition or pass outright.
        lines = [line for line in completed.stdout.splitlines() if line.strip()]
        require(
            len(lines) == 1, "--preflight-only must print exactly one line"
        )
        summary = json.loads(lines[0])
        require(
            summary.get("status") in ("PREFLIGHT_OK", "PREFLIGHT_BLOCKED"),
            "unexpected preflight summary status",
        )
        if summary.get("status") == "PREFLIGHT_OK":
            require(completed.returncode == 0, "PREFLIGHT_OK must exit 0")
        else:
            require(
                "implementation manifest is absent" not in str(summary.get("reason")),
                "manifest exists yet the absent-manifest fence fired",
            )

    # NO write anywhere on the canonical write surface, and zero artifacts.
    require(
        before_provenance == after_provenance,
        "--preflight-only wrote under provenance/ on the canonical workspace",
    )
    require(
        before_execution == after_execution,
        "--preflight-only wrote under stage8_execution/ on the canonical workspace",
    )
    for relative in CANONICAL_ARTIFACT_RELATIVES:
        require(
            not (ROOT / relative).exists(),
            f"the startability probe created a canonical artifact: {relative}",
        )


def main() -> int:
    require(PINNED_PYTHON.is_file(), "pinned runtime python is absent")
    require(shutil.which("git") is not None, "git is required for the fixtures")
    tests = (
        test_gpg_fully_removed,
        test_preconditions_enumerated,
        test_happy_path_and_immutability,
        test_bridge_row_mismatch_blocks,
        test_bridge_manifest_absent_blocks,
        test_authority_digest_mismatch_blocks,
        test_authority_absent_blocks,
        test_bundle_stamp_mismatch_blocks,
        test_push_capability_failure_blocks,
        test_lane_order_refusal,
        test_missing_manifest_row_blocks,
        test_preexisting_canonical_output_blocks,
        test_pre_execution_rehash_blocks,
        test_post_execution_rehash_blocks,
        test_blocked_prior_receipt_refused,
        test_comparator_path_crosscheck_blocks,
        test_receipt_digest_crosscheck_blocks,
        test_preflight_only_ok_and_writes_nothing,
        test_preflight_only_blocks_lane_order,
        test_real_chain_startability,
    )
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"controller_v005_tests_passed {len(tests)}/{len(tests)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
