#!/usr/bin/env python3
"""Integration tests for the v006 actual-parent CAR controller.

Base: test_stage8_t7_controller_v005.py, every scenario ported.  Authored
under STAGE8_T7_CONTROLLER_V006_REPAIR_BINDING_V001 and the sealed
discipline STAGE8_REAL_COMPONENT_PRECONDITION_DISCIPLINE_V001 (+ rule-4
supplement).  Two disjoint regimes:

FIXTURE regime (lane INTERNALS stubbed, as before): every scenario runs
against a throwaway fixture workspace built under a temporary directory
(scratchpad when STAGE8_T7_TEST_SCRATCH is set) with stub lane scripts, a
stub launcher, a fixture git archive (bare file:// remote), copies of the
REAL sealed authority files (M2 digests must verify against real bytes),
copies of the REAL Route-1 readiness surface (the pinned canonical result
and the full snapshot input inventory, so the hoisted M-a/M-b pre-flight
verifies real bytes), and BOTH fixture manifests: the controller's own
v005-path implementation manifest and the bridge (v001-path) manifest the
frozen derive lanes verify and stamp.  The canonical workspace is only
ever read; the copied controller's pinned archive-repository path is
repointed at the fixture archive.  The stub derive lanes mirror the REAL
byte-frozen lanes' bundle provenance fields (implementation-manifest
stamp, executor_sha256, and the launcher/target attestation hashes), so
the BLOCKING-3 hoisted pre-flight verifies the same fields production
bundles carry.

v006 additions covered, one negative per newly hoisted precondition, each
blocking with ZERO artifacts BEFORE any canonical write:
  - BLOCKING 3 (comparison_bundle_provenance): executor-row, launcher-row,
    and attested-target-hash mismatches in a bundle on disk (the
    manifest-stamp member keeps its ported v005 negative).
  - M-a/M-b (primary_route1_readiness): pinned-digest mismatch, missing
    snapshot input, and pre-existing isolated-rerun snapshot.

REAL-COMPONENT regime (discipline rule 1; M-c teeth restored):
  - test_real_chain_startability drives the REAL v005 launcher at its
    canonical path against the CANONICAL workspace, read-only, plus the
    REAL v006 controller bare (--preflight-only, blocked at the first
    enumerated step), asserting the FULL enumerated precondition content
    against the canonical root with zero writes.  It also carries the one
    permitted quarantine regression: the canonical-path invocation of the
    quarantined v004 controller name must fail closed.
  - test_real_chain_fixture_manifest_corruption drives the REAL launcher
    v005 and the REAL controller v006 (byte-identical copies; no stub, no
    monkeypatch, no source edit) against a fixture workspace whose v005
    implementation manifest carries ONE corrupted row: the run must block
    at the enumerated implementation_manifest step naming exactly that
    row, with zero writes and zero artifacts, and its blocked summary
    must carry the full enumerated precondition content.

NAMED GAPS (rule 1 corollary — enumerated, not worked around; the
manifest-v005 cycle must disposition them):
  1. LAUNCHER-ALLOWLIST, controller row: launcher v005's frozen
     ALLOWED_TARGETS carries the v005 controller name and NO row for
     run_stage8_t7_actual_parent_car_pipeline_v006.py.  The canonical
     startability probe therefore asserts the mechanical allowlist fence
     until the disposition lands (post-disposition branches assert the
     absent-v005-manifest block, then PREFLIGHT_OK — hard, per M-c).  The
     fixture-root real-chain test launches the REAL v006 controller bytes
     under the allowlisted v005 controller name for the same reason.
  2. LAUNCHER-ALLOWLIST, test row: launcher v005 allowlists
     test_stage8_t7_controller_v005.py but NOT this file; this suite
     therefore runs bare under the pinned runtime.
  3. The binding's M-c clause says "eight-step enumeration content"
     (written against the v005 tuple); its clause 1b extends the tuple,
     and the v006 tuple has TEN steps.  This suite asserts the full
     ten-step enumeration content, which subsumes the v005 eight.
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
CONTROLLER_SOURCE = ROOT / "scripts/run_stage8_t7_actual_parent_car_pipeline_v006.py"
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

CONTROLLER_RELATIVE = "scripts/run_stage8_t7_actual_parent_car_pipeline_v006.py"
LAUNCHER_RELATIVE = "scripts/launch_stage8_t7_content_addressed_runtime_v005.py"
# NAMED GAP 1: launcher v005's frozen allowlist carries no v006 controller
# row; the fixture-root real-chain test launches the REAL v006 controller
# bytes under this allowlisted name (byte-identical content, real launcher,
# real controller — no stub, no monkeypatch).
REAL_CHAIN_PLACEMENT_RELATIVE = (
    "scripts/run_stage8_t7_actual_parent_car_pipeline_v005.py"
)
# The one permitted quarantined-name regression (superseded chains live in
# scripts/superseded_quarantine/; their canonical-path names must stay
# unlaunchable — discipline rule 3).
QUARANTINED_CONTROLLER_RELATIVE = (
    "scripts/run_stage8_t7_actual_parent_car_pipeline_v004.py"
)
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
    "scripts/test_stage8_t7_controller_v006.py",
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
    "implementation_v005.json"
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

# M-a/M-b: the REAL Route-1 readiness surface the hoisted
# primary_route1_readiness pre-flight verifies. The literals mirror the
# byte-frozen primary lane (and controller v006's ROUTE1_* constants).
ROUTE1_RESULT_RELATIVE = (
    "stage8_execution/work/T07_primitive_operator_response_v001.json"
)
ROUTE1_PINNED_SHA256 = (
    "6dbda44a0f21a28b57f114654a6df79fc091ccfd601c38518fd5cf5f21697dcc"
)
ROUTE1_SNAPSHOT_RELATIVE = (
    "stage8_execution/isolated_route1_rerun/"
    + "3d8aea1a4779b0bfe7a472dca1fab0642750e8e010e339b9e3b100197b75a18c"[:16]
)
ROUTE1_FIXED_RELATIVES = (
    "scripts/derive_stage8_t7_primitive_operator_response_v001.py",
    "scripts/derive_stage8_t7_primitive_operator_response_v001.py.seal.sha256",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md.seal.sha256",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_EXACT_DERIVATION_V001.md",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_EXACT_DERIVATION_V001.md"
    ".seal.sha256",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_AUTHORITY_AMENDMENT_V001.md",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_AUTHORITY_AMENDMENT_V001.md"
    ".seal.sha256",
    "provenance/stage8_t7_numpy_runtime_manifest_v001.json",
    "provenance/stage8_t7_numpy_runtime_manifest_v001.json.seal.sha256",
    "scripts/build_stage8_t7_numpy_runtime_manifest_v001.py",
)
ROUTE1_DIRECT_RELATIVES = (
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md",
    "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md",
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md",
    "COMPLETE_ONE_CELL_CTP_KERNEL_GATE_V001.md",
    "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md",
    "STAGE8_T7_FOUR_AXIS_SCOPE_EXTENSION_ADJUDICATION_RESULT_V001.md",
)
ROUTE1_SEAL_LIST_RELATIVES = (
    "stage8_execution/t7_actual_parent_record_amplitude/"
    "T07_ACTUAL_PARENT_RECORD_AMPLITUDE_V001.seal.sha256",
    "STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_RESULT_V001.seal.sha256",
)
# A seal-list CHILD that is neither an authority nor a bridge/manifest row:
# deleting it in a fixture must trip exactly the route1 inventory fence.
ROUTE1_MISSING_INPUT_PROBE = "STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_SPEC_V001.md"

EXPECTED_PRECONDITIONS = (
    "runtime_attestation",
    "implementation_manifest",
    "authority_digests",
    "bridge_binding",
    "push_capability",
    "prior_receipts",
    "primary_route1_readiness",
    "comparison_bundle_stamps",
    "comparison_bundle_provenance",
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

# M1 + BLOCKING 3: the stub derive lanes mirror the REAL byte-frozen lanes'
# bundle provenance fields exactly as comparator v005 and the hoisted v006
# pre-flight consume them: implementation_manifest_sha256 = the digest of
# the sealed manifest at the canonical v001 path recomputed at stamping
# time; executor_sha256 = the executing lane script's own digest; and the
# launcher attestation's launcher_sha256/target_sha256 bound verbatim.
STUB_DERIVE_TEMPLATE = '''#!/usr/bin/env python3
"""Fixture stub {lane} lane (v001-path manifest stamp + provenance fields)."""
{helpers}

def main():
    work = ROOT / "stage8_execution/work"
    work.mkdir(parents=True, exist_ok=True)
    bridge = ROOT / "{bridge_relative}"
    marker = getattr(sys, "_stage8_t7_content_addressed_runtime_v001")
    out_json = work / "{json_name}"
    out_npz = out_json.with_suffix(".npz")
    out_json.write_text(
        json.dumps(
            {{
                "lane": "{lane}",
                "implementation_manifest_sha256": file_sha256(bridge),
                "executor_sha256": file_sha256(Path(__file__).resolve()),
                "runtime_attestation": {{
                    "launcher_sha256": marker["launcher_sha256"],
                    "target_sha256": marker["target_sha256"],
                }},
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
# S1-1d; unchanged by v005/v006, which are pre-flight-side, not CLI-side).
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


def load_module_constants(path: Path, name: str) -> dict:
    """Execute a real module's source read-only (module level only; the
    __main__ guard keeps main() from running) to obtain its frozen
    constants. No stub: these are the real bytes on disk."""
    namespace = {"__file__": str(path), "__name__": name}
    exec(  # noqa: S102 - deliberate: load the real module-level constants
        compile(path.read_text(encoding="utf-8"), str(path), "exec"),
        namespace,
    )
    return namespace


def route1_relatives() -> list[str]:
    """The REAL Route-1 readiness surface: the pinned canonical result plus
    the full snapshot input inventory, including the children the two REAL
    seal-list files enumerate (parsed from canonical bytes, read-only)."""
    inventory = [ROUTE1_RESULT_RELATIVE]
    inventory.extend(ROUTE1_FIXED_RELATIVES)
    inventory.extend(ROUTE1_DIRECT_RELATIVES)
    inventory.extend(ROUTE1_SEAL_LIST_RELATIVES)
    for seal_list in ROUTE1_SEAL_LIST_RELATIVES:
        source_path = ROOT / seal_list
        require(
            source_path.is_file(),
            f"canonical Route-1 seal-list file absent: {seal_list}",
        )
        for line in source_path.read_text(encoding="ascii").splitlines():
            if line.strip():
                _, child = line.split(maxsplit=1)
                inventory.append(child)
    return inventory


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

    # M-a/M-b: copy the REAL Route-1 readiness surface verbatim (canonical
    # workspace read-only) so the hoisted primary_route1_readiness step
    # verifies real bytes: the pinned canonical result and every snapshot
    # input, including all seal-list children.
    for relative in route1_relatives():
        source_path = ROOT / relative
        require(
            source_path.is_file(),
            f"canonical Route-1 input absent: {relative}",
        )
        destination = fixture / relative
        if destination.exists():
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source_path, destination)
    require(
        sha256(fixture / ROUTE1_RESULT_RELATIVE) == ROUTE1_PINNED_SHA256,
        "REAL-COMPONENT FINDING: the canonical Route-1 result does not carry "
        "the pinned digest the byte-frozen primary lane requires",
    )

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
        "controller v006 must pin the archive repository path",
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
                    "implementation_v005"
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


def corrupt_bundle_field(fixture: Path, bundle_relative: str, mutate) -> None:
    """Rewrite one field of a sealed fixture bundle on disk and restore a
    VALID adjacent seal (exactly what an inter-invocation regeneration
    would leave behind)."""
    bundle = fixture / bundle_relative
    payload = json.loads(bundle.read_text(encoding="utf-8"))
    mutate(payload)
    bundle.write_text(json.dumps(payload) + "\n", encoding="utf-8")
    Path(f"{bundle}.seal.sha256").write_text(
        f"{sha256(bundle)}  {bundle.name}\n", encoding="ascii"
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
            f"controller v006 must not reference {forbidden!r}",
        )


def test_preconditions_enumerated() -> None:
    # Sealed discipline rule 2: the preconditions are ENUMERATED in the
    # controlling artifact as a module-level frozen tuple, in the documented
    # order (the v006 ten-step tuple: the v005 eight plus the M-a/M-b
    # primary_route1_readiness step and the BLOCKING-3
    # comparison_bundle_provenance step). Executed module-level (no
    # main()), no writes. Also pins the v006 manifest binding and the
    # ten-row inventory rows the binding prescribes.
    namespace = load_module_constants(
        CONTROLLER_SOURCE, "controller_v006_under_test"
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
    require(
        set(namespace.get("REQUIRED_MANIFEST_ROWS", ())) == set(REQUIRED_ROWS),
        "REQUIRED_MANIFEST_ROWS must be exactly the ten-row v006 inventory",
    )
    manifest_path = namespace.get("IMPLEMENTATION_MANIFEST")
    require(
        str(manifest_path).endswith(
            "stage8_t7_actual_parent_regulated_car_operator_response_"
            "implementation_v005.json"
        ),
        "controller v006 must bind the sealed v005 implementation manifest",
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

    # BLOCKING 3 + M1 happy path is load-bearing here: the comparison lane
    # ran only because both stub bundles' stamped
    # implementation_manifest_sha256 equalled the recomputed v001-path
    # manifest digest AND their executor/launcher/target provenance fields
    # equalled the manifest rows (the hoisted comparison_bundle_provenance
    # step). M-a/M-b happy path likewise: the primary lane ran only after
    # primary_route1_readiness verified the pinned Route-1 digest, the
    # snapshot absence, and the full input inventory in the fixture.

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
    # M1 (the manifest-stamp member of the four hoisted BLOCKING-3
    # conditions): the inter-invocation regeneration hazard. Both derive
    # lanes run honestly; then the independent bundle is regenerated on
    # disk with a foreign manifest stamp and a VALID adjacent seal (exactly
    # what a lane re-run against a different manifest would leave). The
    # comparison invocation's pre-flight must catch the stamp mismatch
    # BEFORE the canonical comparison path is consumed: no comparison lane
    # run, no comparison output, no comparison receipt.
    fixture = build_fixture("bundle_stamp")
    for lane in ("independent", "primary"):
        completed = run_controller(fixture, lane)
        require(completed.returncode == 0, f"{lane} lane should pass here")

    def mutate(payload: dict) -> None:
        payload["implementation_manifest_sha256"] = "0" * 64

    corrupt_bundle_field(fixture, INDEPENDENT_JSON_RELATIVE, mutate)
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


def test_bundle_executor_provenance_mismatch_blocks() -> None:
    # BLOCKING 3 (executor-row member): a bundle on disk whose recorded
    # executor_sha256 differs from the manifest row of its lane executor
    # must block the comparison invocation in pre-flight, BEFORE the
    # canonical comparison path is consumed (previously only comparator
    # v005 enforced this, inside the comparison lane, after the canonical
    # comparison path was already committed).
    fixture = build_fixture("bundle_executor")
    for lane in ("independent", "primary"):
        completed = run_controller(fixture, lane)
        require(completed.returncode == 0, f"{lane} lane should pass here")

    def mutate(payload: dict) -> None:
        payload["executor_sha256"] = "0" * 64

    corrupt_bundle_field(fixture, PRIMARY_JSON_RELATIVE, mutate)
    completed = run_controller(fixture, "comparison")
    require(completed.returncode != 0, "a foreign bundle executor hash must block")
    require(
        "comparison-provenance pre-flight: primary bundle executor "
        "provenance mismatch" in completed.stderr,
        "executor-provenance block used the wrong fence",
    )
    require(
        lane_order(fixture) == ["independent", "primary"],
        "the comparison lane must never run behind a foreign executor hash",
    )
    require(
        not (fixture / COMPARISON_JSON_RELATIVE).exists()
        and not (fixture / COMPARISON_RECEIPT_RELATIVE).exists(),
        "the executor-provenance block must precede any comparison artifact",
    )


def test_bundle_launcher_provenance_mismatch_blocks() -> None:
    # BLOCKING 3 (launcher-row member): a bundle whose attestation records
    # a foreign launcher hash must block the comparison invocation in
    # pre-flight with zero comparison artifacts.
    fixture = build_fixture("bundle_launcher")
    for lane in ("independent", "primary"):
        completed = run_controller(fixture, lane)
        require(completed.returncode == 0, f"{lane} lane should pass here")

    def mutate(payload: dict) -> None:
        payload["runtime_attestation"]["launcher_sha256"] = "0" * 64

    corrupt_bundle_field(fixture, INDEPENDENT_JSON_RELATIVE, mutate)
    completed = run_controller(fixture, "comparison")
    require(completed.returncode != 0, "a foreign bundle launcher hash must block")
    require(
        "comparison-provenance pre-flight: independent bundle "
        "runtime-launcher provenance mismatch" in completed.stderr,
        "launcher-provenance block used the wrong fence",
    )
    require(
        lane_order(fixture) == ["independent", "primary"],
        "the comparison lane must never run behind a foreign launcher hash",
    )
    require(
        not (fixture / COMPARISON_JSON_RELATIVE).exists()
        and not (fixture / COMPARISON_RECEIPT_RELATIVE).exists(),
        "the launcher-provenance block must precede any comparison artifact",
    )


def test_bundle_target_hash_mismatch_blocks() -> None:
    # BLOCKING 3 (attested-target-hash member): a bundle whose attestation
    # records a target_sha256 different from the manifest row of its lane
    # executor must block the comparison invocation in pre-flight with zero
    # comparison artifacts.
    fixture = build_fixture("bundle_target")
    for lane in ("independent", "primary"):
        completed = run_controller(fixture, lane)
        require(completed.returncode == 0, f"{lane} lane should pass here")

    def mutate(payload: dict) -> None:
        payload["runtime_attestation"]["target_sha256"] = "0" * 64

    corrupt_bundle_field(fixture, PRIMARY_JSON_RELATIVE, mutate)
    completed = run_controller(fixture, "comparison")
    require(completed.returncode != 0, "a foreign attested target hash must block")
    require(
        "comparison-provenance pre-flight: primary bundle "
        "runtime-attestation target-hash binding mismatch" in completed.stderr,
        "target-hash block used the wrong fence",
    )
    require(
        lane_order(fixture) == ["independent", "primary"],
        "the comparison lane must never run behind a foreign target hash",
    )
    require(
        not (fixture / COMPARISON_JSON_RELATIVE).exists()
        and not (fixture / COMPARISON_RECEIPT_RELATIVE).exists(),
        "the target-hash block must precede any comparison artifact",
    )


def test_route1_digest_mismatch_blocks() -> None:
    # M-a: a canonical Route-1 result that does not carry the pinned digest
    # must block the PRIMARY invocation in pre-flight, before the primary
    # lane runs and before any primary artifact exists (previously the
    # byte-frozen lane discovered this only in-lane, where
    # write_blocked_result had already consumed the canonical primary
    # path). The independent lane must be unaffected (documented no-op).
    fixture = build_fixture("route1_digest")
    (fixture / ROUTE1_RESULT_RELATIVE).write_text(
        "# tampered route1 result (fixture)\n", encoding="utf-8"
    )
    independent = run_controller(fixture, "independent")
    require(
        independent.returncode == 0,
        "the independent lane must not gate on the primary lane's Route-1 "
        f"readiness: {independent.stderr[-2000:]}",
    )
    completed = run_controller(fixture, "primary")
    require(completed.returncode != 0, "a drifted Route-1 result must block")
    require(
        "route1 pre-flight: canonical Route-1 result digest mismatch"
        in completed.stderr,
        "route1-digest block used the wrong fence",
    )
    require(
        lane_order(fixture) == ["independent"],
        "the primary lane must never run behind a drifted Route-1 result",
    )
    require(
        not (fixture / PRIMARY_JSON_RELATIVE).exists()
        and not (fixture / PRIMARY_RECEIPT_RELATIVE).exists(),
        "the route1-digest block must precede any canonical primary write",
    )


def test_route1_missing_input_blocks() -> None:
    # M-b (input inventory): a missing Route-1 snapshot input — here a
    # seal-list CHILD, so the fence proves the pre-flight parses the
    # seal-list enumeration exactly as the byte-frozen lane does — must
    # block the PRIMARY invocation in pre-flight with zero primary
    # artifacts. The independent lane must be unaffected.
    fixture = build_fixture("route1_missing")
    (fixture / ROUTE1_MISSING_INPUT_PROBE).unlink()
    independent = run_controller(fixture, "independent")
    require(
        independent.returncode == 0,
        "the independent lane must not gate on the Route-1 input inventory: "
        f"{independent.stderr[-2000:]}",
    )
    completed = run_controller(fixture, "primary")
    require(completed.returncode != 0, "a missing Route-1 input must block")
    require(
        "route1 pre-flight: snapshot input is absent: "
        f"{ROUTE1_MISSING_INPUT_PROBE}" in completed.stderr,
        "route1-inventory block used the wrong fence",
    )
    require(
        lane_order(fixture) == ["independent"],
        "the primary lane must never run without its Route-1 inputs",
    )
    require(
        not (fixture / PRIMARY_JSON_RELATIVE).exists()
        and not (fixture / PRIMARY_RECEIPT_RELATIVE).exists(),
        "the route1-inventory block must precede any canonical primary write",
    )


def test_route1_snapshot_exists_blocks() -> None:
    # M-b (Route-1 rerun precondition): a pre-existing immutable isolated
    # Route-1 snapshot must block the PRIMARY invocation in pre-flight with
    # zero primary artifacts. The independent lane must be unaffected.
    fixture = build_fixture("route1_snapshot")
    (fixture / ROUTE1_SNAPSHOT_RELATIVE).mkdir(parents=True)
    independent = run_controller(fixture, "independent")
    require(
        independent.returncode == 0,
        "the independent lane must not gate on the Route-1 snapshot: "
        f"{independent.stderr[-2000:]}",
    )
    completed = run_controller(fixture, "primary")
    require(completed.returncode != 0, "a pre-existing Route-1 snapshot must block")
    require(
        "route1 pre-flight: immutable isolated Route-1 snapshot already "
        "exists" in completed.stderr,
        "route1-snapshot block used the wrong fence",
    )
    require(
        lane_order(fixture) == ["independent"],
        "the primary lane must never run over an existing Route-1 snapshot",
    )
    require(
        not (fixture / PRIMARY_JSON_RELATIVE).exists()
        and not (fixture / PRIMARY_RECEIPT_RELATIVE).exists(),
        "the route1-snapshot block must precede any canonical primary write",
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
    # a clean workspace runs EVERY enumerated precondition (the v006
    # ten-step tuple), exits 0 with a one-line PREFLIGHT_OK json, and
    # performs NO write anywhere in the workspace (full before/after tree
    # scan; the fixture git archive is excluded as test scaffolding — the
    # happy-path test separately proves the dry run pushes nothing).
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
    # THE MECHANICAL-RULE TEST (sealed discipline rule 1; M-c teeth,
    # canonical-root half). Read-only against the CANONICAL workspace:
    #
    #   PROBE A drives the REAL v005 launcher at its canonical path with
    #   the v006 controller as target, in the exact invocation shape of
    #   production. The expected outcome is keyed to MECHANICAL disk state
    #   (never to a disjunction over unknown outcomes): (1) while launcher
    #   v005's frozen allowlist carries no v006 controller row — NAMED GAP
    #   1, disposition deferred to the manifest-v005 cycle by the binding's
    #   clause 3 — the probe must fail at exactly the allowlist fence;
    #   (2) once a launcher generation allowlists this controller and the
    #   sealed v005 manifest is still absent, the probe must block at
    #   exactly the absent-manifest fence with the full enumerated
    #   precondition content; (3) with the manifest present it must assert
    #   PREFLIGHT_OK outright (M-c: no either-way escape).
    #
    #   PROBE B drives the REAL v006 controller bare (--preflight-only):
    #   it must block at the FIRST enumerated precondition
    #   (runtime_attestation) and its one-line summary must carry the FULL
    #   enumerated precondition content — the ten-step v006 tuple —
    #   asserted here against the canonical root, read-only.
    #
    #   Plus the one permitted quarantine regression (discipline rule 3):
    #   the canonical-path invocation of the quarantined v004 controller
    #   name must fail closed at the allowlist.
    require(
        REAL_LAUNCHER.is_file(),
        "REAL-COMPONENT FINDING: canonical launcher v005 is absent; "
        "the real chain cannot be driven (discipline rule 1 requires "
        "dispositioning this before sealing)",
    )
    require(CONTROLLER_SOURCE.is_file(), "canonical controller v006 is absent")
    require(PINNED_PYTHON.is_file(), "pinned runtime python is absent")
    manifest = ROOT / MANIFEST_RELATIVE

    for relative in CANONICAL_ARTIFACT_RELATIVES:
        require(
            not (ROOT / relative).exists(),
            f"canonical artifact already exists before the startability probe: "
            f"{relative}",
        )

    # The REAL launcher's frozen allowlist, loaded from the real bytes on
    # disk (module level only, read-only): the branch below keys on this
    # mechanical state, not on an observed outcome.
    launcher_constants = load_module_constants(
        REAL_LAUNCHER, "launcher_v005_under_test"
    )
    allowed_targets = launcher_constants.get("ALLOWED_TARGETS")
    require(
        isinstance(allowed_targets, frozenset) and bool(allowed_targets),
        "launcher v005 must carry a frozen ALLOWED_TARGETS set",
    )
    controller_allowlisted = CONTROLLER_RELATIVE in allowed_targets
    if not controller_allowlisted:
        print(
            "FLAG launcher-allowlist disposition pending: launcher v005 "
            f"carries no row for {CONTROLLER_RELATIVE} "
            "(manifest-v005 cycle must disposition; binding clause 3)"
        )
    if TEST_ROWS[-1] not in allowed_targets:
        print(
            "FLAG launcher-allowlist disposition pending: launcher v005 "
            f"carries no row for {TEST_ROWS[-1]}; this suite runs bare "
            "(manifest-v005 cycle must disposition)"
        )

    environment = dict(os.environ)
    environment.pop("STAGE8_T7_CONTROLLER_CONTEXT", None)

    # Quarantine regression (rule 3; the one permitted quarantined-name
    # assertion): the canonical-path invocation of the quarantined v004
    # controller name must fail closed, launching nothing.
    require(
        QUARANTINED_CONTROLLER_RELATIVE not in allowed_targets,
        "REAL-COMPONENT FINDING (B2 class): launcher v005 allowlists the "
        "quarantined v004 controller name",
    )
    quarantined = subprocess.run(
        [
            str(PINNED_PYTHON),
            "-I",
            "-S",
            str(REAL_LAUNCHER),
            QUARANTINED_CONTROLLER_RELATIVE,
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        env=environment,
    )
    require(
        quarantined.returncode != 0
        and "runtime target is not allowlisted" in quarantined.stderr,
        "the canonical-path invocation of the quarantined v004 controller "
        f"name must fail closed: {quarantined.stderr[-2000:]}",
    )

    # The controller's entire canonical write surface: receipts + seals go
    # under provenance/, outputs + seals under stage8_execution/. Scan both
    # completely (size + mtime_ns) before and after BOTH probes.
    before_provenance = tree_scan(ROOT / "provenance")
    before_execution = tree_scan(ROOT / "stage8_execution")

    # PROBE A: REAL launcher -> v006 controller, production invocation shape.
    probe_a = subprocess.run(
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

    # PROBE B: REAL v006 controller bare — blocked at the FIRST enumerated
    # precondition; the summary carries the full v006 enumeration.
    probe_b = subprocess.run(
        [
            str(PINNED_PYTHON),
            "-I",
            "-S",
            str(CONTROLLER_SOURCE),
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

    if not controller_allowlisted:
        # NAMED GAP 1 state: the mechanical rule-3 fence, and nothing after
        # it, fires. The controller startability through the REAL launcher
        # is proven by test_real_chain_fixture_manifest_corruption until
        # the allowlist disposition lands.
        require(
            probe_a.returncode != 0,
            "the launcher must fail closed on a non-allowlisted controller",
        )
        require(
            f"runtime target is not allowlisted: {CONTROLLER_RELATIVE}"
            in probe_a.stderr,
            "the allowlist fence must name the v006 controller precisely; "
            f"got: {probe_a.stderr[-2000:]}",
        )
    elif not manifest.is_file():
        # Post-disposition, pre-construction: the precise enumerated block,
        # nothing else.
        require(
            "runtime target is not allowlisted" not in probe_a.stderr,
            "allowlisted controller yet the allowlist fence fired",
        )
        require(
            "pipeline requires the sealed runtime launcher" not in probe_a.stderr,
            "the real launcher's runtime marker did not reach the controller",
        )
        require(
            probe_a.returncode != 0,
            "the pre-construction probe must block (manifest v005 absent)",
        )
        expected_reason = (
            "implementation manifest is absent: "
            "provenance/stage8_t7_actual_parent_regulated_car_operator_"
            "response_implementation_v005.json"
        )
        require(
            expected_reason in probe_a.stderr,
            "the block reason must name the absent v005 manifest precisely; "
            f"got: {probe_a.stderr[-2000:]}",
        )
        lines = [line for line in probe_a.stdout.splitlines() if line.strip()]
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
            "full frozen enumeration",
        )
    else:
        # Post-disposition, post-construction: M-c teeth — PREFLIGHT_OK
        # asserted outright; no either-way escape.
        require(
            probe_a.returncode == 0,
            "with the sealed v005 manifest present the real-chain probe "
            f"must reach PREFLIGHT_OK: {probe_a.stderr[-4000:]}",
        )
        lines = [line for line in probe_a.stdout.splitlines() if line.strip()]
        require(len(lines) == 1, "--preflight-only must print exactly one line")
        summary = json.loads(lines[0])
        require(
            summary.get("status") == "PREFLIGHT_OK"
            and tuple(summary.get("preconditions", ()))
            == EXPECTED_PRECONDITIONS,
            "PREFLIGHT_OK must carry the full frozen enumeration",
        )

    # PROBE B assertions (always): blocked at the FIRST enumerated step,
    # one line, full enumeration content against the canonical root.
    require(
        probe_b.returncode != 0,
        "the bare controller must block at runtime_attestation",
    )
    require(
        "pipeline requires the sealed runtime launcher" in probe_b.stderr,
        "the bare-controller block must be the runtime_attestation fence; "
        f"got: {probe_b.stderr[-2000:]}",
    )
    lines_b = [line for line in probe_b.stdout.splitlines() if line.strip()]
    require(
        len(lines_b) == 1,
        "the blocked bare probe must print exactly one line",
    )
    summary_b = json.loads(lines_b[0])
    require(
        summary_b.get("status") == "PREFLIGHT_BLOCKED"
        and summary_b.get("lane") == "independent"
        and "pipeline requires the sealed runtime launcher"
        in str(summary_b.get("reason")),
        "bare-probe summary malformed",
    )
    require(
        tuple(summary_b.get("preconditions", ())) == EXPECTED_PRECONDITIONS,
        "the bare probe must carry the FULL enumerated precondition content "
        "(the ten-step v006 tuple) against the canonical root",
    )

    # NO write anywhere on the canonical write surface, and zero artifacts.
    require(
        before_provenance == after_provenance,
        "the startability probes wrote under provenance/ on the canonical "
        "workspace",
    )
    require(
        before_execution == after_execution,
        "the startability probes wrote under stage8_execution/ on the "
        "canonical workspace",
    )
    for relative in CANONICAL_ARTIFACT_RELATIVES:
        require(
            not (ROOT / relative).exists(),
            f"the startability probe created a canonical artifact: {relative}",
        )


def test_real_chain_fixture_manifest_corruption() -> None:
    # M-c teeth, fixture-root half (a corruption regression is impossible
    # against the read-only canonical root): the REAL v005 launcher and the
    # REAL v006 controller — byte-identical copies of the canonical files;
    # no stub, no monkeypatch, no source edit — run against a fixture
    # workspace whose v005 implementation manifest carries ONE corrupted
    # row. The run must block at the enumerated implementation_manifest
    # step naming exactly that row, BEFORE any canonical write, with zero
    # writes anywhere in the fixture, and its blocked summary must carry
    # the full enumerated precondition content through the REAL chain.
    #
    # NAMED GAP 1 (see module docstring): launcher v005's frozen allowlist
    # carries no v006 controller row, so the REAL v006 controller bytes are
    # placed at the allowlisted v005 controller name. The launcher's
    # read-once attestation hashes the bytes it executes, and the fixture
    # manifest's self-binding row pins that placement, so the executed code
    # is provably the canonical v006 controller byte for byte.
    require(PINNED_PYTHON.is_file(), "pinned runtime python is absent")
    fixture = scratch_directory("real_chain")
    (fixture / "scripts").mkdir()
    (fixture / "provenance").mkdir()
    (fixture / "stage8_execution/work").mkdir(parents=True)

    real_rows = list(REQUIRED_ROWS)
    for relative in real_rows:
        source_path = ROOT / relative
        require(
            source_path.is_file(),
            f"canonical implementation file absent: {relative}",
        )
        destination = fixture / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source_path, destination)
    # The REAL launcher's own runtime authority (verify_runtime reads the
    # sealed NumPy runtime manifest and adjacent seal from the fixture root).
    for relative in (
        "provenance/stage8_t7_numpy_runtime_manifest_v001.json",
        "provenance/stage8_t7_numpy_runtime_manifest_v001.json.seal.sha256",
    ):
        shutil.copyfile(ROOT / relative, fixture / relative)
    # The byte-identical v006 controller at the allowlisted name (NAMED
    # GAP 1 above).
    shutil.copyfile(
        ROOT / CONTROLLER_RELATIVE, fixture / REAL_CHAIN_PLACEMENT_RELATIVE
    )
    require(
        sha256(fixture / REAL_CHAIN_PLACEMENT_RELATIVE)
        == sha256(ROOT / CONTROLLER_RELATIVE),
        "the placed controller must be byte-identical to canonical v006",
    )

    # Fixture v005 implementation manifest: the corrupted row FIRST (row
    # order is verification order in the controller's drift loop), then
    # every other required row plus the placement-path self-binding row,
    # all with true digests of the real bytes on disk.
    rows = [{"path": COMPARATOR_RELATIVE, "sha256": "0" * 64}]
    for relative in real_rows + [REAL_CHAIN_PLACEMENT_RELATIVE]:
        if relative == COMPARATOR_RELATIVE:
            continue
        rows.append({"path": relative, "sha256": sha256(fixture / relative)})
    manifest = fixture / MANIFEST_RELATIVE
    manifest.write_text(
        json.dumps(
            {
                "schema": (
                    "stage8_t7_actual_parent_regulated_car_operator_response_"
                    "implementation_v005"
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

    environment = dict(os.environ)
    environment.pop("STAGE8_T7_CONTROLLER_CONTEXT", None)
    before = tree_scan(fixture)
    completed = subprocess.run(
        [
            str(PINNED_PYTHON),
            "-I",
            "-S",
            str(fixture / LAUNCHER_RELATIVE),
            REAL_CHAIN_PLACEMENT_RELATIVE,
            "--lane",
            "independent",
            "--preflight-only",
        ],
        cwd=fixture,
        check=False,
        capture_output=True,
        text=True,
        env=environment,
    )
    after = tree_scan(fixture)

    # Startability facts on the REAL components: the launcher accepted the
    # target (no allowlist fence), its verified-runtime marker reached the
    # controller (no marker fence), and the self-binding row held (the
    # block is not the self-binding fence).
    require(
        "runtime target is not allowlisted" not in completed.stderr,
        "REAL-COMPONENT FINDING (B1 class): the real launcher refused the "
        f"placed real controller: {completed.stderr[-2000:]}",
    )
    require(
        "pipeline requires the sealed runtime launcher" not in completed.stderr,
        "the real launcher's runtime marker did not reach the real controller",
    )
    require(
        "pipeline is not implementation-bound" not in completed.stderr,
        "the placement self-binding row failed",
    )
    require(
        completed.returncode != 0,
        "one corrupted manifest row must block the real chain",
    )
    require(
        f"implementation drift: {COMPARATOR_RELATIVE}" in completed.stderr,
        "the real chain must block at the enumerated implementation_manifest "
        f"step naming the corrupted row; got: {completed.stderr[-2000:]}",
    )
    lines = [line for line in completed.stdout.splitlines() if line.strip()]
    require(
        len(lines) == 1,
        "the blocked real-chain probe must print exactly one line",
    )
    summary = json.loads(lines[0])
    require(
        summary.get("status") == "PREFLIGHT_BLOCKED"
        and f"implementation drift: {COMPARATOR_RELATIVE}"
        in str(summary.get("reason")),
        "the real-chain blocked summary must carry the precise drift reason",
    )
    require(
        tuple(summary.get("preconditions", ())) == EXPECTED_PRECONDITIONS,
        "the real-chain blocked summary must carry the FULL enumerated "
        "precondition content (the ten-step v006 tuple)",
    )
    require(
        before == after,
        "the blocked real-chain probe must not write anywhere in the fixture",
    )
    require(
        no_canonical_artifacts(fixture),
        "the blocked real-chain probe must leave zero canonical artifacts",
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
        test_bundle_executor_provenance_mismatch_blocks,
        test_bundle_launcher_provenance_mismatch_blocks,
        test_bundle_target_hash_mismatch_blocks,
        test_route1_digest_mismatch_blocks,
        test_route1_missing_input_blocks,
        test_route1_snapshot_exists_blocks,
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
        test_real_chain_fixture_manifest_corruption,
    )
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"controller_v006_tests_passed {len(tests)}/{len(tests)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
