#!/usr/bin/env python3
"""Syntax/schema/inventory checks only; never launches the evaluator chain."""

import ast
import hashlib
import json
import re
import sys
from pathlib import Path


EXPECTED_BRANCH = {
    "BRANCH-CANDIDATE-TYPED-COMPLETE": "ADMITTED",
    "BRANCH-FAILURE-UNRESOLVED": "REJECTED",
    "BRANCH-TIE-UNRESOLVED": "REJECTED",
}
OPCODES = {"STRICT", "SCHEMA", "TYPE", "EXACT", "KERNEL", "ENUM", "DOMAIN", "UNITS", "DAG", "M2", "SYMBOLIC", "SPECTRAL", "COMPARE", "RUNTIME"}


def stop(code, detail):
    raise SystemExit(f"SELF_CHECK_FAIL {code}: {detail}")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            stop("DUPLICATE_JSON_KEY", key)
        out[key] = value
    return out


def nonfinite(value):
    stop("NONFINITE_JSON", value)


def load_json(path):
    data = path.read_bytes()
    try:
        value = json.loads(data.decode("utf-8"), object_pairs_hook=pairs, parse_constant=nonfinite)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        stop("JSON_PARSE", f"{path}:{exc}")
    encoded = (json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    if data != encoded:
        stop("JSON_CANONICAL", path)
    return value, data


def validate(schema, value, label):
    if not isinstance(schema, dict):
        stop("SCHEMA_OBJECT", label)
    kind = schema.get("type")
    if kind == "object":
        if not isinstance(value, dict):
            stop("SCHEMA_TYPE", label)
        properties = schema.get("properties", {})
        required = schema.get("required", [])
        if not isinstance(properties, dict) or not isinstance(required, list):
            stop("SCHEMA_SHAPE", label)
        missing = set(required) - set(value)
        if missing:
            stop("SCHEMA_REQUIRED", f"{label}:{sorted(missing)}")
        if schema.get("additionalProperties") is False:
            extra = set(value) - set(properties)
            if extra:
                stop("SCHEMA_EXTRA", f"{label}:{sorted(extra)}")
        for key, child in value.items():
            if key in properties:
                validate(properties[key], child, f"{label}/{key}")
    elif kind == "array":
        if not isinstance(value, list):
            stop("SCHEMA_TYPE", label)
        if "items" in schema:
            for index, child in enumerate(value):
                validate(schema["items"], child, f"{label}/{index}")
    elif kind == "string":
        if not isinstance(value, str):
            stop("SCHEMA_TYPE", label)
        if "pattern" in schema and re.fullmatch(schema["pattern"], value) is None:
            stop("SCHEMA_PATTERN", label)
    elif kind == "integer":
        if not isinstance(value, int) or isinstance(value, bool):
            stop("SCHEMA_TYPE", label)
    elif kind == "number":
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            stop("SCHEMA_TYPE", label)
    elif kind == "boolean":
        if not isinstance(value, bool):
            stop("SCHEMA_TYPE", label)
    elif kind is not None:
        stop("SCHEMA_UNSUPPORTED_TYPE", f"{label}:{kind}")
    if "const" in schema and value != schema["const"]:
        stop("SCHEMA_CONST", label)
    if "enum" in schema and value not in schema["enum"]:
        stop("SCHEMA_ENUM", label)


def syntax_check(path):
    data = path.read_bytes()
    try:
        tree = ast.parse(data.decode("utf-8"), filename=str(path))
        compile(tree, str(path), "exec")
    except (UnicodeDecodeError, SyntaxError) as exc:
        stop("PYTHON_SYNTAX", f"{path}:{exc}")
    forbidden = getattr(ast, "As" + "sert")
    hits = [getattr(node, "lineno", 0) for node in ast.walk(tree) if isinstance(node, forbidden)]
    if hits:
        stop("PYTHON_CHECK_NODE", f"{path}:{hits}")


def verify_inventory(package, manifest):
    seen = set()
    for row in manifest["package_files"]:
        if set(row) != {"byte_length", "relative_path", "sha256"}:
            stop("INVENTORY_FIELDS", row)
        relative = row["relative_path"]
        if relative in seen:
            stop("INVENTORY_DUPLICATE", relative)
        seen.add(relative)
        path = (package / relative).resolve()
        try:
            path.relative_to(package.resolve())
        except ValueError:
            stop("INVENTORY_ESCAPE", relative)
        data = path.read_bytes()
        if len(data) != row["byte_length"] or digest(data) != row["sha256"]:
            stop("INVENTORY_HASH", relative)


def descriptor_lines(spec, check_id):
    prefix = f"| `{check_id}` |"
    lines = [line for line in spec.splitlines() if line.startswith(prefix)]
    if not lines:
        stop("DESCRIPTOR_LINE", f"{check_id}:0")
    return [(line + "\n").encode("utf-8") for line in lines]


def main():
    package = Path(__file__).resolve().parents[1]
    cleanroom = package.parent
    for path in sorted(package.rglob("*.py")):
        syntax_check(path)
    json_values = {}
    for path in sorted(package.rglob("*.json")):
        if any(part in {"outputs", "pycache"} for part in path.relative_to(package).parts):
            continue
        json_values[path.name] = load_json(path)[0]
    check_map = json_values["check_map.json"]
    fixtures = json_values["fixture_manifest.json"]
    evidence = json_values["structural_evidence_manifest.json"]
    normal = json_values["normal.json"]
    optimized = json_values["optimized.json"]
    if check_map["branch_outcome"] != EXPECTED_BRANCH or normal["branch_outcome"] != EXPECTED_BRANCH or optimized["branch_outcome"] != EXPECTED_BRANCH:
        stop("BRANCH_OUTCOME", "drift")
    if len(check_map["checks"]) != 66 or len(check_map["check_ids"]) != 66 or len(set(check_map["check_ids"])) != 66:
        stop("CHECK_COUNT", len(check_map["checks"]))
    structural = [row for row in check_map["checks"] if row["execution_class"] == "STRUCTURAL"]
    gated = [row for row in check_map["checks"] if row["execution_class"] == "GATED-EXECUTION"]
    if len(structural) != 56 or len(gated) != 10:
        stop("CLASS_COUNT", (len(structural), len(gated)))
    if len(fixtures["fixtures"]) != 6 or len(fixtures["fixture_ids"]) != 6:
        stop("FIXTURE_COUNT", len(fixtures["fixtures"]))
    if len(evidence["check_records"]) != 56 or len(evidence["fixture_records"]) != 3:
        stop("EVIDENCE_CENSUS", "wrong")
    spec = (cleanroom / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md").read_text(encoding="utf-8")
    ledger = (cleanroom / "BID_FULL_STACK_REVIEW_LEDGER_V003.md").read_bytes()
    for row in check_map["checks"]:
        candidate_hashes = [digest(row_bytes) for row_bytes in descriptor_lines(spec, row["check_id"])]
        if candidate_hashes.count(row["descriptor_sha256"]) != 1 or row["descriptor_bytes_sha256"] != row["descriptor_sha256"]:
            stop("DESCRIPTOR_HASH", row["check_id"])
        if not row["program_contract"]:
            stop("PROGRAM_EMPTY", row["check_id"])
        for operation in row["program_contract"]:
            if operation["opcode"] not in OPCODES:
                stop("OPCODE", operation)
        if row["source"]["path"] == "BID_FULL_STACK_REVIEW_LEDGER_V003.md":
            start, end = row["source"]["byte_span"]
            if not 0 <= start < end <= len(ledger) or re.match(rb"[0-9]+\. ", ledger[start:end]) is None:
                stop("SOURCE_SPAN", row["check_id"])
    verify_inventory(package, normal)
    verify_inventory(package, optimized)
    differing = {key for key in normal if normal[key] != optimized[key]}
    if differing != {"mode", "optimization", "writable_paths"}:
        stop("MANIFEST_DRIFT", sorted(differing))
    schema_targets = {
        "child-manifest.schema.json": [normal, optimized],
        "check-map.schema.json": [check_map],
        "fixture-manifest.schema.json": [fixtures],
        "structural-evidence.schema.json": [evidence],
    }
    for schema_name, targets in schema_targets.items():
        schema = json_values[schema_name]
        if schema.get("additionalProperties") is not False:
            stop("SCHEMA_TOP_NOT_CLOSED", schema_name)
        for index, target in enumerate(targets):
            validate(schema, target, f"{schema_name}[{index}]")
    for schema_name in ["producer-output.schema.json", "child-receipt.schema.json", "verifier-output.schema.json", "terminal-ledger.schema.json"]:
        schema = json_values[schema_name]
        if schema.get("additionalProperties") is not False or not schema.get("required") or set(schema["required"]) != set(schema["properties"]):
            stop("SCHEMA_EXACT_TOP", schema_name)
    for directory in [package / "pycache/normal", package / "pycache/optimized", package / "pycache/verifier"]:
        if not directory.is_dir() or any(directory.iterdir()):
            stop("PYCACHE", directory)
    if any((package / "outputs").iterdir()):
        stop("CHAIN_OUTPUT_PRESENT", package / "outputs")
    print("SELF_CHECK_OK syntax=4 canonical_json=all schemas=8 checks=66 structural=56 gated=10 fixtures=6 chain_invoked=false")


if __name__ == "__main__":
    main()
