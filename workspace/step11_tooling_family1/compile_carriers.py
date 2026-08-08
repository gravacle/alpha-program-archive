#!/usr/bin/env python3
"""Deterministic Step-11 carrier compiler for the relay-723 bounded target set.

Standard-library only.  The compiler consumes content-addressed schema, target,
and source manifests, validates the closed JSON-schema subset used by the four
sealed box schemas, verifies all content/span references, and writes canonical
JSON without a trailing newline.  It never invents an unavailable instance.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Any


HEX64 = re.compile(r"^[0-9a-f]{64}$")


class ToolError(Exception):
    def __init__(self, code: str, detail: str):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


def canonical_bytes(value: Any) -> bytes:
    try:
        return json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ToolError("CANONICAL_JSON", str(exc)) from exc


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_bytes(path: Path) -> bytes:
    try:
        return path.read_bytes()
    except OSError as exc:
        raise ToolError("INPUT_READ", f"{path}: {exc}") from exc


def verify_file(path: Path, expected_sha256: str) -> bytes:
    if not HEX64.fullmatch(expected_sha256):
        raise ToolError("HASH_FORM", f"{path}: {expected_sha256!r}")
    data = read_bytes(path)
    actual = sha256_bytes(data)
    if actual != expected_sha256:
        raise ToolError("HASH_MISMATCH", f"{path}: expected {expected_sha256}, got {actual}")
    return data


def load_json_bytes(data: bytes, label: str) -> Any:
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ToolError("UTF8", f"{label}: {exc}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ToolError("JSON_PARSE", f"{label}: {exc}") from exc


def load_pinned_json(path: Path, expected_sha256: str) -> Any:
    return load_json_bytes(verify_file(path, expected_sha256), str(path))


def write_canonical(path: Path, value: Any) -> str:
    data = canonical_bytes(value)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise ToolError("OUTPUT_COLLISION", str(path))
    try:
        path.write_bytes(data)
    except OSError as exc:
        raise ToolError("OUTPUT_WRITE", f"{path}: {exc}") from exc
    return sha256_bytes(data)


def resolve_under(root: Path, relative_path: str) -> Path:
    rel = Path(relative_path)
    if rel.is_absolute() or not relative_path or any(part == ".." for part in rel.parts):
        raise ToolError("PATH_FORM", relative_path)
    base = root.resolve()
    resolved = (base / rel).resolve()
    try:
        resolved.relative_to(base)
    except ValueError as exc:
        raise ToolError("PATH_ESCAPE", relative_path) from exc
    return resolved


def _type_ok(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    return False


def _resolve_ref(root_schema: dict[str, Any], ref: str) -> dict[str, Any]:
    prefix = "#/$defs/"
    if not ref.startswith(prefix) or "/" in ref[len(prefix):]:
        raise ToolError("SCHEMA_REF", ref)
    key = ref[len(prefix):]
    try:
        target = root_schema["$defs"][key]
    except (KeyError, TypeError) as exc:
        raise ToolError("SCHEMA_REF", ref) from exc
    if not isinstance(target, dict):
        raise ToolError("SCHEMA_REF", ref)
    return target


def validate_schema(value: Any, schema: dict[str, Any], root_schema: dict[str, Any], path: str = "$") -> None:
    if "$ref" in schema:
        validate_schema(value, _resolve_ref(root_schema, schema["$ref"]), root_schema, path)
        return
    if "const" in schema and value != schema["const"]:
        raise ToolError("SCHEMA_CONFORMANCE", f"{path}: const")
    if "enum" in schema and value not in schema["enum"]:
        raise ToolError("SCHEMA_CONFORMANCE", f"{path}: enum")
    expected = schema.get("type")
    if expected is not None and not _type_ok(value, expected):
        raise ToolError("SCHEMA_CONFORMANCE", f"{path}: expected {expected}")
    if isinstance(value, dict):
        required = schema.get("required", [])
        missing = [key for key in required if key not in value]
        if missing:
            raise ToolError("SCHEMA_CONFORMANCE", f"{path}: missing {missing}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extras = sorted(set(value) - set(properties))
            if extras:
                raise ToolError("SCHEMA_CONFORMANCE", f"{path}: extra {extras}")
        for key, item in value.items():
            if key in properties:
                validate_schema(item, properties[key], root_schema, f"{path}.{key}")
    elif isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            raise ToolError("SCHEMA_CONFORMANCE", f"{path}: minItems")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            raise ToolError("SCHEMA_CONFORMANCE", f"{path}: maxItems")
        prefix_items = schema.get("prefixItems", [])
        for index, item_schema in enumerate(prefix_items):
            if index < len(value):
                validate_schema(value[index], item_schema, root_schema, f"{path}[{index}]")
        tail_schema = schema.get("items")
        if tail_schema is False and len(value) > len(prefix_items):
            raise ToolError("SCHEMA_CONFORMANCE", f"{path}: tuple tail")
        if isinstance(tail_schema, dict):
            for index in range(len(prefix_items), len(value)):
                validate_schema(value[index], tail_schema, root_schema, f"{path}[{index}]")
        if schema.get("uniqueItems"):
            encoded = [canonical_bytes(item) for item in value]
            if len(encoded) != len(set(encoded)):
                raise ToolError("SCHEMA_CONFORMANCE", f"{path}: uniqueItems")
    elif isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            raise ToolError("SCHEMA_CONFORMANCE", f"{path}: minLength")
        if "pattern" in schema and re.fullmatch(schema["pattern"], value) is None:
            raise ToolError("SCHEMA_CONFORMANCE", f"{path}: pattern")
    elif isinstance(value, int) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            raise ToolError("SCHEMA_CONFORMANCE", f"{path}: minimum")


def contract_def(contract: dict[str, Any], name: str) -> dict[str, Any]:
    try:
        result = contract["$defs"][name]
    except (KeyError, TypeError) as exc:
        raise ToolError("CONTRACT_DEF", name) from exc
    if not isinstance(result, dict):
        raise ToolError("CONTRACT_DEF", name)
    return result


def validate_contract_instance(value: Any, contract: dict[str, Any], name: str) -> None:
    validate_schema(value, contract_def(contract, name), contract, f"${name}")


def verify_span_ref(ref: dict[str, Any], source_root: Path) -> None:
    path = resolve_under(source_root, ref["relative_path"])
    data = verify_file(path, ref["source_sha256"])
    start, end = ref["span"]
    if start > end or end > len(data):
        raise ToolError("SPAN_BOUNDS", f"{ref['relative_path']}:{start}:{end}:{len(data)}")
    actual = sha256_bytes(data[start:end])
    if actual != ref["span_sha256"]:
        raise ToolError("SPAN_HASH_MISMATCH", f"{ref['relative_path']}:{start}:{end}")


def verify_content_ref(ref: dict[str, Any], source_root: Path) -> None:
    path = resolve_under(source_root, ref["relative_path"])
    data = verify_file(path, ref["sha256"])
    if len(data) != ref["byte_length"]:
        raise ToolError("BYTE_LENGTH_MISMATCH", ref["relative_path"])


def verify_instance_refs(value: Any, source_root: Path) -> None:
    if isinstance(value, dict):
        keys = set(value)
        if keys == {"relative_path", "source_sha256", "span", "span_sha256"}:
            verify_span_ref(value, source_root)
            return
        if keys == {"relative_path", "byte_length", "sha256"}:
            verify_content_ref(value, source_root)
            return
        for item in value.values():
            verify_instance_refs(item, source_root)
    elif isinstance(value, list):
        for item in value:
            verify_instance_refs(item, source_root)


def verify_delta_grounding(delta: dict[str, Any], source_root: Path) -> int:
    count = 0
    registry = delta.get("grounding_registry")
    if not isinstance(registry, dict):
        raise ToolError("DELTA_SHAPE", "grounding_registry")
    for refs in registry.values():
        if not isinstance(refs, list):
            raise ToolError("DELTA_SHAPE", "grounding refs")
        for ref in refs:
            verify_span_ref({
                "relative_path": ref["relative_path"],
                "source_sha256": ref["sha256"],
                "span": ref["span"],
                "span_sha256": ref["span_sha256"],
            }, source_root)
            count += 1
    probe = delta.get("probe_record")
    if not isinstance(probe, dict):
        raise ToolError("DELTA_SHAPE", "probe_record")
    verify_span_ref({
        "relative_path": probe["relative_path"],
        "source_sha256": probe["sha256"],
        "span": probe["span"],
        "span_sha256": probe["span_sha256"],
    }, source_root)
    return count + 1


def generate_targets(delta: dict[str, Any], delta_sha256: str) -> dict[str, Any]:
    targets: list[dict[str, Any]] = []
    for box in delta.get("schemas", []):
        schema_id = box["instance_schema"].get("$id", "")
        for target_id in box["direct_c_elements"]:
            targets.append({
                "target_id": target_id,
                "box_id": box["box_id"],
                "row_id": box["row_id"],
                "consumer_family": box["consumer_family"],
                "source_class": "SCHEMA",
                "state": "CONTRACT_READY",
                "schema_id": schema_id,
            })
    for box in delta.get("moved_to_u", []):
        for target_id in box["direct_c_elements"]:
            targets.append({
                "target_id": target_id,
                "box_id": box["box_id"],
                "row_id": box["row_id"],
                "consumer_family": box["consumer_family"],
                "source_class": "U",
                "state": "OUT_OF_SCOPE_U",
                "schema_id": "",
            })
    targets.sort(key=lambda item: item["target_id"])
    ids = [item["target_id"] for item in targets]
    if len(ids) != 19 or len(ids) != len(set(ids)):
        raise ToolError("TARGET_CENSUS", f"expected 19 unique, got {len(ids)}/{len(set(ids))}")
    return {
        "schema": "rd22.step11.tooling-family1-targets.v001",
        "schema_delta_sha256": delta_sha256,
        "targets": targets,
    }


def generate_sources(targets: dict[str, Any], delta: dict[str, Any], targets_sha256: str) -> dict[str, Any]:
    u_by_box = {item["box_id"]: item for item in delta.get("moved_to_u", [])}
    entries = []
    for target in targets["targets"]:
        if target["state"] == "OUT_OF_SCOPE_U":
            missing = ";".join(u_by_box[target["box_id"]]["missing"])
            owner = f"OUT_OF_SCOPE_U:{missing}"
        else:
            owner = "SEALED_INSTANCE_SOURCE_NOT_OF_RECORD"
        entries.append({
            "target_id": target["target_id"],
            "available": False,
            "instance_relative_path": "",
            "instance_sha256": "",
            "missing_owner": owner,
        })
    return {
        "schema": "rd22.step11.tooling-family1-sources.v001",
        "target_manifest_sha256": targets_sha256,
        "entries": entries,
    }


def schema_lookup(delta: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for box in delta.get("schemas", []):
        for target_id in box["direct_c_elements"]:
            result[target_id] = box["instance_schema"]
    return result


def compile_run(
    contract: dict[str, Any],
    delta: dict[str, Any],
    delta_sha256: str,
    targets: dict[str, Any],
    targets_sha256: str,
    sources: dict[str, Any],
    sources_sha256: str,
    source_root: Path,
    output_root: Path,
) -> dict[str, Any]:
    validate_contract_instance(targets, contract, "target_manifest")
    validate_contract_instance(sources, contract, "source_manifest")
    if targets["schema_delta_sha256"] != delta_sha256:
        raise ToolError("ROOT_BINDING", "target manifest -> schema delta")
    if sources["target_manifest_sha256"] != targets_sha256:
        raise ToolError("ROOT_BINDING", "source manifest -> target manifest")
    pin_count = verify_delta_grounding(delta, source_root)
    source_by_target = {item["target_id"]: item for item in sources["entries"]}
    if set(source_by_target) != {item["target_id"] for item in targets["targets"]}:
        raise ToolError("SOURCE_CENSUS", "target/source IDs disagree")
    schemas = schema_lookup(delta)
    outcomes: list[dict[str, Any]] = []
    produced = 0
    out_of_scope = 0
    missing = 0
    for target in targets["targets"]:
        source = source_by_target[target["target_id"]]
        component_path = ""
        component_sha256 = ""
        if target["state"] == "OUT_OF_SCOPE_U":
            if source["available"]:
                raise ToolError("U_INPUT_FORBIDDEN", target["target_id"])
            status = "OUT_OF_SCOPE_U"
            out_of_scope += 1
        elif not source["available"]:
            status = "MISSING_INPUT"
            missing += 1
        else:
            if not source["instance_relative_path"] or not HEX64.fullmatch(source["instance_sha256"]):
                raise ToolError("SOURCE_ENTRY_FORM", target["target_id"])
            instance_path = resolve_under(source_root, source["instance_relative_path"])
            instance_data = verify_file(instance_path, source["instance_sha256"])
            instance = load_json_bytes(instance_data, str(instance_path))
            try:
                schema = schemas[target["target_id"]]
            except KeyError as exc:
                raise ToolError("SCHEMA_LOOKUP", target["target_id"]) from exc
            validate_schema(instance, schema, schema)
            verify_instance_refs(instance, source_root)
            canonical = canonical_bytes(instance)
            component_sha256 = sha256_bytes(canonical)
            component_path = f"components/{component_sha256}.json"
            destination = output_root / component_path
            if destination.exists():
                if read_bytes(destination) != canonical:
                    raise ToolError("CONTENT_ADDRESS_COLLISION", component_path)
            else:
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(canonical)
            status = "PRODUCED"
            produced += 1
        outcomes.append({
            "target_id": target["target_id"],
            "box_id": target["box_id"],
            "row_id": target["row_id"],
            "status": status,
            "component_relative_path": component_path,
            "component_sha256": component_sha256,
            "missing_owner": "" if status == "PRODUCED" else source["missing_owner"],
            "admission": "BARRED_STEP11_SUBGATE",
        })
    rows: list[dict[str, Any]] = []
    for row_id in sorted({item["row_id"] for item in outcomes}):
        row_outcomes = [item for item in outcomes if item["row_id"] == row_id]
        bindings = sorted(
            [item["component_sha256"] for item in row_outcomes if item["status"] == "PRODUCED"]
        )
        owners = sorted(
            {item["missing_owner"] for item in row_outcomes if item["missing_owner"]}
        )
        if bindings and len(bindings) == len(row_outcomes):
            state = "STATEABLE_COMPONENTS_PRESENT_ADMISSION_BARRED"
        elif any(item["status"] == "MISSING_INPUT" for item in row_outcomes):
            state = "PARTIAL_SCHEMA_READY_INPUT_ABSENT"
        else:
            state = "UNCHANGED_OUT_OF_SCOPE_U"
        rows.append({
            "row_id": row_id,
            "state": state,
            "component_sha256": bindings,
            "missing_owners": owners,
            "admission": "BARRED_STEP11_SUBGATE",
        })
    result = {
        "schema": "rd22.step11.tooling-family1-result.v001",
        "schema_delta_sha256": delta_sha256,
        "target_manifest_sha256": targets_sha256,
        "source_manifest_sha256": sources_sha256,
        "grounding_pins_verified": pin_count,
        "summary": {
            "targets": len(outcomes),
            "produced": produced,
            "missing_input": missing,
            "out_of_scope_u": out_of_scope,
        },
        "targets": outcomes,
        "rows": rows,
        "admission": "BARRED_STEP11_SUBGATE",
        "chain_invoked": False,
    }
    validate_contract_instance(result, contract, "result")
    output_root.mkdir(parents=True, exist_ok=True)
    result_sha = write_canonical(output_root / "compilation_result.json", result)
    for row in rows:
        safe_name = re.sub(r"[^A-Za-z0-9_.-]", "_", row["row_id"])
        write_canonical(output_root / "rows" / f"{safe_name}.status.json", row)
    write_canonical(
        output_root / "result_pin.json",
        {"relative_path":"compilation_result.json","sha256":result_sha},
    )
    return result


def emit_pins(root: Path, relative_paths: list[str], output: Path) -> None:
    rows = []
    for relative_path in sorted(relative_paths):
        path = resolve_under(root, relative_path)
        data = read_bytes(path)
        rows.append({"relative_path":relative_path,"byte_length":len(data),"sha256":sha256_bytes(data)})
    write_canonical(output, {"schema":"rd22.generated-pins.v001","rows":rows})


def emit_inventory(root: Path, output: Path) -> None:
    rows = []
    output_resolved = output.resolve()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        if path.resolve() == output_resolved:
            continue
        data = read_bytes(path)
        rows.append({
            "relative_path": path.relative_to(root).as_posix(),
            "byte_length": len(data),
            "sha256": sha256_bytes(data),
        })
    write_canonical(output, {
        "schema":"rd22.step11.tooling-family1-inventory.v001",
        "inventory_self_excluded":True,
        "files":rows,
    })


def self_check(contract: dict[str, Any], delta: dict[str, Any]) -> dict[str, Any]:
    controls = []
    with tempfile.TemporaryDirectory(prefix="rd22-family1-") as temp_name:
        temp = Path(temp_name)
        blob = b"abcdef"
        (temp / "blob.bin").write_bytes(blob)
        blob_sha = sha256_bytes(blob)
        bx01 = next(item for item in delta["schemas"] if item["box_id"].startswith("BX01-"))
        schema = bx01["instance_schema"]
        content_ref = {"relative_path":"blob.bin","byte_length":len(blob),"sha256":blob_sha}
        valid = {
            "schema":"rd22.step11.v008-05.noncommuting-plaquette.v001",
            "source_bindings":[{
                "relative_path":"blob.bin","source_sha256":blob_sha,
                "span":[0,len(blob)],"span_sha256":blob_sha,
            }],
            "universal_word":content_ref,
            "representation":content_ref,
            "target_word":content_ref,
            "inverse_competitor":content_ref,
            "fixture_assignments":content_ref,
        }
        validate_schema(valid, schema, schema)
        verify_instance_refs(valid, temp)
        controls.append({"control":"positive_valid_instance","expected":"ACCEPT","observed":"ACCEPT"})
        try:
            verify_file(temp / "blob.bin", "0" * 64)
            observed = "ACCEPT"
        except ToolError as exc:
            observed = exc.code
        controls.append({"control":"perturbed_input_digest","expected":"HASH_MISMATCH","observed":observed})
        nonconforming = dict(valid)
        nonconforming.pop("representation")
        try:
            validate_schema(nonconforming, schema, schema)
            observed = "ACCEPT"
        except ToolError as exc:
            observed = exc.code
        controls.append({"control":"nonconforming_instance","expected":"SCHEMA_CONFORMANCE","observed":observed})
        truncated = dict(valid)
        truncated["source_bindings"] = [{
            "relative_path":"blob.bin","source_sha256":blob_sha,
            "span":[0,len(blob)-1],"span_sha256":blob_sha,
        }]
        try:
            validate_schema(truncated, schema, schema)
            verify_instance_refs(truncated, temp)
            observed = "ACCEPT"
        except ToolError as exc:
            observed = exc.code
        controls.append({"control":"truncated_span","expected":"SPAN_HASH_MISMATCH","observed":observed})
    passed = all(item["expected"] == item["observed"] for item in controls)
    if not passed:
        raise ToolError("SELF_CHECK", repr(controls))
    return {
        "schema":"rd22.step11.tooling-family1-self-check.v001",
        "passed":True,
        "controls":controls,
    }


def parser() -> argparse.ArgumentParser:
    top = argparse.ArgumentParser()
    sub = top.add_subparsers(dest="command", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--contract", type=Path, required=True)
    common.add_argument("--contract-sha256", required=True)
    common.add_argument("--schema-delta", type=Path, required=True)
    common.add_argument("--schema-delta-sha256", required=True)
    p = sub.add_parser("targets", parents=[common])
    p.add_argument("--output", type=Path, required=True)
    p = sub.add_parser("sources", parents=[common])
    p.add_argument("--targets", type=Path, required=True)
    p.add_argument("--targets-sha256", required=True)
    p.add_argument("--output", type=Path, required=True)
    p = sub.add_parser("compile", parents=[common])
    p.add_argument("--targets", type=Path, required=True)
    p.add_argument("--targets-sha256", required=True)
    p.add_argument("--sources", type=Path, required=True)
    p.add_argument("--sources-sha256", required=True)
    p.add_argument("--source-root", type=Path, required=True)
    p.add_argument("--output-root", type=Path, required=True)
    p = sub.add_parser("self-check", parents=[common])
    p.add_argument("--output", type=Path, required=True)
    p = sub.add_parser("pins")
    p.add_argument("--root", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("relative_paths", nargs="+")
    p = sub.add_parser("inventory")
    p.add_argument("--root", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    return top


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.command == "pins":
            emit_pins(args.root, args.relative_paths, args.output)
            return 0
        if args.command == "inventory":
            emit_inventory(args.root, args.output)
            return 0
        contract = load_pinned_json(args.contract, args.contract_sha256)
        delta = load_pinned_json(args.schema_delta, args.schema_delta_sha256)
        if args.command == "targets":
            value = generate_targets(delta, args.schema_delta_sha256)
            validate_contract_instance(value, contract, "target_manifest")
            write_canonical(args.output, value)
        elif args.command == "sources":
            targets = load_pinned_json(args.targets, args.targets_sha256)
            validate_contract_instance(targets, contract, "target_manifest")
            value = generate_sources(targets, delta, args.targets_sha256)
            validate_contract_instance(value, contract, "source_manifest")
            write_canonical(args.output, value)
        elif args.command == "compile":
            targets = load_pinned_json(args.targets, args.targets_sha256)
            sources = load_pinned_json(args.sources, args.sources_sha256)
            compile_run(
                contract, delta, args.schema_delta_sha256,
                targets, args.targets_sha256, sources, args.sources_sha256,
                args.source_root, args.output_root,
            )
        elif args.command == "self-check":
            write_canonical(args.output, self_check(contract, delta))
        return 0
    except ToolError as exc:
        print(f"RD22_TOOLING_FAMILY1_REFUSE {exc.code} {exc.detail}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
