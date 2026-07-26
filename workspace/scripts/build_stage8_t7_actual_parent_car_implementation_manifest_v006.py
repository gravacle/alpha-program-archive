#!/usr/bin/env python3
"""Build and seal the generation-G7 implementation manifest (v006).

Authored in the cycle-7 package under
STAGE8_T7_PRODUCTION_GATE_NOGO_AND_PIPELINE_REPAIR_BINDING_V001 (Part A
item A1) and STAGE8_T7_DIRECTORY_PERMISSION_FENCE_EVALUATION_AND_PROBES_
V001 (limitation L4: the construction lane must raise and drop the fence
DELIBERATELY, and must record each raise).

WHAT IT DOES.  It reads the twelve-row generation-G7 inventory FROM
controller v007 -- the frozen GENERATION_MEMBERS / REQUIRED_MANIFEST_ROWS
structures, parsed out of the controller's own bytes on disk with ast, never
imported and never executed -- hashes each row's file, and writes
provenance/stage8_t7_actual_parent_regulated_car_operator_response_
implementation_v006.json plus its adjacent seal.  Because the row set comes
from the controller's own frozen table rather than from a hand-typed list
here, the manifest and the controller's generation-coherence check cannot
disagree about what generation G7 is.  That is the whole point: a hand-typed
row list in a builder is exactly the shape that produced six one-pin lags.

FAIL-CLOSED.  It refuses to overwrite an existing manifest or seal; it
refuses to run if any row is missing from disk; and it refuses to write into
a read-only provenance directory unless the operator passes
--l4-raise-and-record, which raises the fence, writes, drops it again, and
prints the L4 raise record.

FENCE ROLE, recorded honestly: this builder is the SECOND of the two
components the coherence table's fence row lists as permitted to raise the
fence (the first is controller v007).  It can create only the manifest and
its seal, at one fixed path, and only when they do not already exist; it
drops the fence in a finally path.  It cannot write a lane artifact.

NO MEASURED CONSTANT is introduced: every value in the manifest is either a
path from the controller's frozen table or a SHA-256 of a file on disk.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import stat
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
CONTROLLER_RELATIVE = "scripts/run_stage8_t7_actual_parent_car_pipeline_v007.py"
MANIFEST_RELATIVE = (
    "provenance/"
    "stage8_t7_actual_parent_regulated_car_operator_response_implementation_"
    "v006.json"
)
MANIFEST_SCHEMA = (
    "stage8_t7_actual_parent_regulated_car_operator_response_implementation_v006"
)
FENCED_DIRECTORIES = (ROOT / "stage8_execution/work", ROOT / "provenance")
FENCE_AT_REST_MODE = 0o555
FENCE_RAISED_MODE = 0o755
FENCE_WRITE_BITS = stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH

DESCRIPTION = (
    "Implementation authority v006 for the Route-2 Phase-A production "
    "pipeline: GENERATION G7 (controller v007 + launcher v007 + comparator "
    "v006) plus the shared byte-frozen v002 derive lanes, reached only "
    "through the sealed v001-path bridge manifest. Authorized by "
    "STAGE8_T7_PRODUCTION_GATE_NOGO_AND_PIPELINE_REPAIR_BINDING_V001 "
    "(Part A A1-A5; Part B B1/B2/B5 and the MAJORs) and "
    "STAGE8_T7_DIRECTORY_PERMISSION_FENCE_EVALUATION_AND_PROBES_V001. "
    "Controller, launcher, comparator and this manifest all name generation "
    "G7, and controller v007 runs a mechanical generation-coherence check "
    "over every pin on disk before any lane. Canonical output directories "
    "are read-only at rest behind the directory-permission write fence. "
    "No GPG (superseded); authority = external anchoring + recorded "
    "principal authorization. Production remains PROHIBITED: the "
    "production-gate verdict is NO_GO and there is no typed authorization."
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


def module_dict_pin(path: Path, symbol: str) -> dict[str, str]:
    """Read a module-level dict-of-strings pin from a file's bytes on disk.

    Parsed with ast; never imported, never executed.  Handles the dict
    literal shape controller v007 uses, including `**OTHER_DICT` unpacking of
    another module-level dict literal in the same file.
    """
    require(path.is_file(), f"pin source is absent: {path}")
    tree = ast.parse(path.read_bytes(), filename=str(path))
    assignments: dict[str, ast.AST] = {}
    for statement in tree.body:
        if not isinstance(statement, ast.Assign):
            continue
        for target in statement.targets:
            if isinstance(target, ast.Name):
                require(
                    target.id not in assignments,
                    f"pin {target.id} is assigned more than once in {path.name}",
                )
                assignments[target.id] = statement.value
    require(symbol in assignments, f"pin {symbol} is absent from {path.name}")

    def resolve(node: ast.AST) -> dict[str, str]:
        require(
            isinstance(node, ast.Dict),
            f"pin {symbol} in {path.name} is not a dict literal",
        )
        assert isinstance(node, ast.Dict)
        resolved: dict[str, str] = {}
        for key, value in zip(node.keys, node.values):
            if key is None:
                require(
                    isinstance(value, ast.Name) and value.id in assignments,
                    f"pin {symbol} unpacks an unresolvable value",
                )
                assert isinstance(value, ast.Name)
                for inner_key, inner_value in resolve(assignments[value.id]).items():
                    resolved[inner_key] = inner_value
                continue
            require(
                isinstance(key, ast.Constant) and isinstance(key.value, str),
                f"pin {symbol} in {path.name} has a non-string key",
            )
            assert isinstance(key, ast.Constant)
            literal = string_literal(value)
            require(
                literal is not None,
                f"pin {symbol}[{key.value}] in {path.name} is not a string literal",
            )
            resolved[key.value] = str(literal)
        return resolved

    return resolve(assignments[symbol])


def string_literal(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = string_literal(node.left)
        right = string_literal(node.right)
        if left is not None and right is not None:
            return left + right
    return None


def generation_rows() -> list[str]:
    """The twelve manifest rows, derived from controller v007's frozen table."""
    controller = ROOT / CONTROLLER_RELATIVE
    members = module_dict_pin(controller, "GENERATION_MEMBERS")
    require(
        members.get("manifest") == MANIFEST_RELATIVE,
        "the controller's manifest pin does not name this manifest: "
        f"{members.get('manifest')!r} != {MANIFEST_RELATIVE!r}",
    )
    require(
        members.get("controller") == CONTROLLER_RELATIVE,
        "the controller's own membership row does not name the controller "
        f"this builder read: {members.get('controller')!r}",
    )
    require(
        members.get("manifest_builder") == str(SELF.relative_to(ROOT)),
        "the controller's generation does not include this builder: "
        f"{members.get('manifest_builder')!r}",
    )
    rows = sorted(path for key, path in members.items() if key != "manifest")
    require(
        len(rows) == 12,
        f"the generation-G7 inventory is {len(rows)} rows, expected 12: {rows}",
    )
    return rows


def fence_mode(directory: Path) -> int:
    return stat.S_IMODE(directory.stat().st_mode)


def drop_fence() -> list[str]:
    dropped: list[str] = []
    for directory in FENCED_DIRECTORIES:
        if directory.is_dir() and fence_mode(directory) != FENCE_AT_REST_MODE:
            directory.chmod(FENCE_AT_REST_MODE)
            dropped.append(str(directory.relative_to(ROOT)))
    return dropped


def raise_fence() -> list[str]:
    raised: list[str] = []
    for directory in FENCED_DIRECTORIES:
        require(
            directory.is_dir(),
            f"fenced directory is absent: {directory.relative_to(ROOT)}",
        )
        directory.chmod(FENCE_RAISED_MODE)
        raised.append(str(directory.relative_to(ROOT)))
    return raised


def write_manifest(manifest: Path, payload: dict[str, Any]) -> str:
    seal = Path(f"{manifest}.seal.sha256")
    require(not manifest.exists(), f"manifest already exists: {manifest}")
    require(not seal.exists(), f"manifest seal already exists: {seal}")
    temporary = manifest.with_suffix(manifest.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    os.replace(temporary, manifest)
    digest = sha256(manifest)
    seal_temporary = seal.with_suffix(seal.suffix + ".tmp")
    seal_temporary.write_text(f"{digest}  {manifest.name}\n", encoding="ascii")
    os.replace(seal_temporary, seal)
    for artifact in (manifest, seal):
        artifact.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    return digest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--l4-raise-and-record",
        action="store_true",
        help=(
            "Fence limitation L4: raise write permission on the fenced "
            "directories, write the manifest, drop the fence again, and print "
            "the raise record. Without this flag the builder refuses to write "
            "into a read-only provenance directory."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Compute and print the manifest payload without writing anything.",
    )
    arguments = parser.parse_args()

    manifest = ROOT / MANIFEST_RELATIVE
    rows = generation_rows()
    row_records: list[dict[str, str]] = []
    for relative in rows:
        path = ROOT / relative
        require(path.is_file(), f"manifest row is absent from disk: {relative}")
        row_records.append({"path": relative, "sha256": sha256(path)})
    payload = {
        "schema": MANIFEST_SCHEMA,
        "description": DESCRIPTION,
        "phase": "A",
        "files": row_records,
        "alpha_computed": False,
        "proof_authorized": False,
    }

    if arguments.dry_run:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    provenance = manifest.parent
    require(provenance.is_dir(), f"provenance directory is absent: {provenance}")
    fenced = not bool(fence_mode(provenance) & FENCE_WRITE_BITS)
    raised: list[str] = []
    record: dict[str, Any] = {
        "schema": "stage8_t7_l4_construction_lane_raise_record_v001",
        "actor": str(SELF.relative_to(ROOT)),
        "purpose": f"seal {MANIFEST_RELATIVE}",
        "provenance_was_fenced_at_rest": fenced,
    }
    if fenced:
        require(
            arguments.l4_raise_and_record,
            "provenance is read-only at rest (the directory-permission write "
            "fence). Re-run with --l4-raise-and-record to raise it "
            "deliberately, write the manifest, and drop it again; the raise "
            "is recorded on stderr per fence limitation L4.",
        )
        raised = raise_fence()
        record["raised"] = raised
    try:
        digest = write_manifest(manifest, payload)
    finally:
        if raised:
            record["dropped"] = drop_fence()
            record["fence_state_after_drop"] = {
                str(directory.relative_to(ROOT)): f"{fence_mode(directory):04o}"
                for directory in FENCED_DIRECTORIES
            }
            print(json.dumps(record, sort_keys=True), file=sys.stderr)
    print(
        json.dumps(
            {
                "schema": "stage8_t7_implementation_manifest_build_summary_v001",
                "manifest": MANIFEST_RELATIVE,
                "manifest_sha256": digest,
                "row_count": len(row_records),
                "l4_raise_record": record if raised else None,
                "alpha_computed": False,
                "proof_authorized": False,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
