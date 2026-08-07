#!/usr/bin/env python3
"""RD-22 Builder A producer.

This direct child is intentionally self-contained so isolated mode never needs
to add the package directory to ``sys.path``.  It evaluates only structural
opcodes.  Gated descriptors are returned before any procedure is started.
"""

import argparse
import ast
import hashlib
import json
import os
import re
import sys
import time
from fractions import Fraction
from pathlib import Path


SCHEMA = "rd22.producer-output.v001"
RECEIPT_SCHEMA = "rd22.child-receipt.v001"
STATUS_SET = {"PASS", "FAIL", "NOT_RUN_GATE", "ERROR"}
GATED_CLASS = "GATED-EXECUTION"
STRUCTURAL_CLASS = "STRUCTURAL"
MASK_FIELDS = {"process_id", "monotonic_duration", "python_optimize"}
SPEC_FIXED = {
    "ADMITTED",
    "REJECTED",
    "FAILS",
    "ALLOWED",
    "REJECTED_DIMENSIONFUL",
    "CONTAINED",
    "INSUFFICIENT",
    "INDEX_ONE",
    "Z_NOT_SUFFICIENT",
    "INTERTWINER_IDENTITY",
}


class BuildFailure(Exception):
    pass


def fail(code, detail):
    raise BuildFailure(f"{code}: {detail}")


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def file_bytes(path):
    try:
        return Path(path).read_bytes()
    except OSError as exc:
        fail("READ_FAILED", f"{path}: {exc}")


def verify_file(path, expected):
    data = file_bytes(path)
    actual = sha256_bytes(data)
    if actual != expected:
        fail("HASH_MISMATCH", f"{path}: expected {expected}, got {actual}")
    return data


def reject_constant(value):
    fail("STRICT_JSON_NONFINITE", value)


def reject_pairs(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            fail("STRICT_JSON_DUPLICATE_KEY", key)
        out[key] = value
    return out


def strict_json_bytes(data, label):
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail("STRICT_JSON_UTF8", f"{label}: {exc}")
    try:
        value = json.loads(
            text,
            object_pairs_hook=reject_pairs,
            parse_constant=reject_constant,
        )
    except (json.JSONDecodeError, BuildFailure) as exc:
        fail("STRICT_JSON_PARSE", f"{label}: {exc}")
    return value


def canonical_bytes(value):
    try:
        text = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
    except (TypeError, ValueError) as exc:
        fail("CANONICAL_JSON", str(exc))
    return (text + "\n").encode("utf-8")


def exact_keys(value, required, label):
    if not isinstance(value, dict):
        fail("SCHEMA_TYPE", f"{label} is not an object")
    actual = set(value)
    wanted = set(required)
    if actual != wanted:
        fail(
            "SCHEMA_FIELDS",
            f"{label}: missing={sorted(wanted-actual)}, extra={sorted(actual-wanted)}",
        )


def content_root(entries):
    records = []
    seen = set()
    for entry in entries:
        exact_keys(entry, {"relative_path", "byte_length", "sha256"}, "content entry")
        path = entry["relative_path"]
        if path in seen:
            fail("DUPLICATE_PATH", path)
        seen.add(path)
        if not isinstance(entry["byte_length"], int) or entry["byte_length"] < 0:
            fail("BYTE_LENGTH", path)
        digest = entry["sha256"]
        if not isinstance(digest, str) or re.fullmatch(r"[0-9a-f]{64}", digest) is None:
            fail("SHA256_FORMAT", path)
        records.append(f"{path}\0{entry['byte_length']}\0{digest}\n")
    payload = b"A35-CONTENT-ROOT-v1\0" + "".join(sorted(records)).encode("utf-8")
    return sha256_bytes(payload)


def pointer_get(value, pointer):
    if pointer in ("", "/"):
        return value
    node = value
    for raw in pointer.lstrip("/").split("/"):
        part = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(node, list):
            try:
                node = node[int(part)]
            except (ValueError, IndexError):
                fail("POINTER", pointer)
        elif isinstance(node, dict) and part in node:
            node = node[part]
        else:
            fail("POINTER", pointer)
    return node


def validate_closed_schema(schema, value, label="$"):
    if not isinstance(schema, dict):
        return False, f"{label}: schema not object"
    kind = schema.get("type")
    if kind == "object":
        if not isinstance(value, dict):
            return False, f"{label}: not object"
        props = schema.get("properties", {})
        required = schema.get("required", [])
        if schema.get("additionalProperties") is not False:
            return False, f"{label}: schema is not closed"
        if set(value) - set(props):
            return False, f"{label}: extra fields {sorted(set(value)-set(props))}"
        if set(required) - set(value):
            return False, f"{label}: missing fields {sorted(set(required)-set(value))}"
        for key, child in value.items():
            ok, why = validate_closed_schema(props[key], child, f"{label}/{key}")
            if not ok:
                return False, why
    elif kind == "array":
        if not isinstance(value, list):
            return False, f"{label}: not array"
        if "minItems" in schema and len(value) < schema["minItems"]:
            return False, f"{label}: too short"
        if schema.get("uniqueItems"):
            forms = [canonical_bytes(item) for item in value]
            if len(forms) != len(set(forms)):
                return False, f"{label}: duplicate items"
        child_schema = schema.get("items")
        if child_schema is not None:
            for index, child in enumerate(value):
                ok, why = validate_closed_schema(child_schema, child, f"{label}/{index}")
                if not ok:
                    return False, why
    elif kind == "string":
        if not isinstance(value, str):
            return False, f"{label}: not string"
        if "enum" in schema and value not in schema["enum"]:
            return False, f"{label}: outside enum"
        if "pattern" in schema and re.fullmatch(schema["pattern"], value) is None:
            return False, f"{label}: pattern mismatch"
    elif kind == "integer":
        if not isinstance(value, int) or isinstance(value, bool):
            return False, f"{label}: not integer"
    elif kind == "boolean":
        if not isinstance(value, bool):
            return False, f"{label}: not boolean"
    elif kind == "null":
        if value is not None:
            return False, f"{label}: not null"
    elif kind is None:
        if "const" not in schema and "enum" not in schema:
            return False, f"{label}: untyped schema"
    else:
        return False, f"{label}: unsupported type {kind}"
    if "const" in schema and value != schema["const"]:
        return False, f"{label}: const mismatch"
    if "enum" in schema and value not in schema["enum"]:
        return False, f"{label}: enum mismatch"
    return True, ""


def rational(value):
    if isinstance(value, int) and not isinstance(value, bool):
        return Fraction(value, 1)
    if isinstance(value, str) and re.fullmatch(r"-?[0-9]+(?:/[1-9][0-9]*)?", value):
        return Fraction(value)
    fail("EXACT_RATIONAL", repr(value))


def normalize_expr(expr):
    if isinstance(expr, (str, int, bool)) or expr is None:
        return expr
    if isinstance(expr, list):
        return [normalize_expr(item) for item in expr]
    if not isinstance(expr, dict):
        fail("EXACT_EXPRESSION", repr(expr))
    op = expr.get("op")
    if op is None:
        return {key: normalize_expr(expr[key]) for key in sorted(expr)}
    args = expr.get("args", [])
    if op == "rational":
        value = rational(expr.get("value"))
        return {"denominator": value.denominator, "numerator": value.numerator}
    if op in {"add", "mul"}:
        values = [rational(normalize_numeric(item)) for item in args]
        out = sum(values, Fraction(0, 1)) if op == "add" else Fraction(1, 1)
        if op == "mul":
            for value in values:
                out *= value
        return {"denominator": out.denominator, "numerator": out.numerator}
    if op == "neg":
        value = -rational(normalize_numeric(args[0]))
        return {"denominator": value.denominator, "numerator": value.numerator}
    if op == "pairwise_distinct":
        forms = [canonical_bytes(normalize_expr(item)) for item in args]
        return len(forms) == len(set(forms))
    if op == "exactly_one_true":
        return sum(1 for item in args if normalize_expr(item) is True) == 1
    if op == "contains":
        return normalize_expr(args[1]) in normalize_expr(args[0])
    if op == "equals":
        return normalize_expr(args[0]) == normalize_expr(args[1])
    fail("EXACT_OPCODE", op)


def normalize_numeric(expr):
    value = normalize_expr(expr)
    if isinstance(value, dict) and set(value) == {"denominator", "numerator"}:
        return f"{value['numerator']}/{value['denominator']}"
    return value


def opcode_strict(args):
    data = args.get("bytes_utf8")
    if not isinstance(data, str):
        return result(False, "STRICT_INPUT")
    try:
        encoded = data.encode("utf-8")
    except UnicodeEncodeError:
        return result(False, "STRICT_UTF8")
    mode = args.get("mode", "text")
    if mode == "json":
        try:
            value = strict_json_bytes(encoded, "STRICT")
        except BuildFailure as exc:
            return result(False, str(exc))
        if canonical_bytes(value) != encoded:
            return result(False, "STRICT_NOT_CANONICAL")
        return result(True, "", value=value)
    if mode != "text":
        return result(False, "STRICT_MODE")
    return result(True, "", sha256=sha256_bytes(encoded))


def opcode_schema(args):
    ok, why = validate_closed_schema(args.get("schema"), args.get("value"))
    return result(ok, why, normalized=args.get("value"), classification=args.get("value", {}).get("classification") if isinstance(args.get("value"), dict) else None)


def opcode_type(args):
    graph = args.get("graph")
    if not isinstance(graph, dict):
        return result(False, "TYPE_GRAPH")
    objects = graph.get("objects")
    edges = graph.get("edges")
    if not isinstance(objects, list) or not isinstance(edges, list):
        return result(False, "TYPE_FIELDS")
    if len(objects) != len(set(objects)):
        return result(False, "TYPE_DUPLICATE_OBJECT")
    object_set = set(objects)
    names = set()
    for edge in edges:
        if not isinstance(edge, dict) or set(edge) != {"codomain", "domain", "name"}:
            return result(False, "TYPE_EDGE_SHAPE")
        if edge["name"] in names or edge["domain"] not in object_set or edge["codomain"] not in object_set:
            return result(False, "TYPE_EDGE")
        names.add(edge["name"])
    for composition in graph.get("compositions", []):
        if not isinstance(composition, list) or any(name not in names for name in composition):
            return result(False, "TYPE_COMPOSITION")
    return result(True, "", object_count=len(objects), edge_count=len(edges))


def opcode_exact(args):
    try:
        if "expression" in args:
            normal = normalize_expr(args["expression"])
            truth = normal is True if isinstance(normal, bool) else True
            return result(truth, "" if truth else "EXACT_FALSE", normal_form=normal)
        left = normalize_expr(args.get("left"))
        right = normalize_expr(args.get("right"))
    except BuildFailure as exc:
        return result(False, str(exc))
    return result(left == right, "" if left == right else "EXACT_MISMATCH", normal_form=left)


def opcode_kernel(args):
    axioms = args.get("axioms")
    proof = args.get("proof")
    goal = args.get("goal")
    if not isinstance(axioms, dict) or not isinstance(proof, dict) or goal is None:
        return result(False, "KERNEL_INPUT")
    axiom_map = axioms.get("axioms")
    steps = proof.get("steps")
    if not isinstance(axiom_map, dict) or not isinstance(steps, list):
        return result(False, "KERNEL_SHAPE")
    derived = []
    used = []
    for index, step in enumerate(steps):
        if not isinstance(step, dict):
            return result(False, f"KERNEL_STEP_{index}")
        rule = step.get("rule")
        conclusion = step.get("conclusion")
        if rule == "AXIOM":
            digest = step.get("axiom_sha256")
            if digest not in axiom_map or axiom_map[digest] != conclusion:
                return result(False, f"KERNEL_AXIOM_{index}")
            used.append(digest)
        elif rule == "REFLEXIVE":
            if not isinstance(conclusion, dict) or conclusion.get("left") != conclusion.get("right"):
                return result(False, f"KERNEL_REFLEXIVE_{index}")
        elif rule == "SYMMETRY":
            source = step.get("source")
            if not isinstance(source, int) or source < 0 or source >= len(derived):
                return result(False, f"KERNEL_SOURCE_{index}")
            prior = derived[source]
            if not isinstance(prior, dict) or conclusion != {"left": prior.get("right"), "right": prior.get("left")}:
                return result(False, f"KERNEL_SYMMETRY_{index}")
        elif rule == "TRANSITIVITY":
            sources = step.get("sources")
            if not isinstance(sources, list) or len(sources) != 2:
                return result(False, f"KERNEL_TRANSITIVITY_{index}")
            if any(not isinstance(item, int) or item < 0 or item >= len(derived) for item in sources):
                return result(False, f"KERNEL_SOURCE_{index}")
            first, second = derived[sources[0]], derived[sources[1]]
            wanted = {"left": first.get("left"), "right": second.get("right")}
            if first.get("right") != second.get("left") or conclusion != wanted:
                return result(False, f"KERNEL_CHAIN_{index}")
        else:
            return result(False, f"KERNEL_RULE_{index}")
        derived.append(conclusion)
    if not derived or derived[-1] != goal:
        return result(False, "KERNEL_GOAL")
    return result(True, "", conclusion=goal, used_axiom_hashes=sorted(set(used)))


def enumerate_grammar(grammar):
    if not isinstance(grammar, dict):
        fail("ENUM_GRAMMAR", "not object")
    kind = grammar.get("kind")
    if kind == "explicit":
        items = grammar.get("items")
        if not isinstance(items, list):
            fail("ENUM_ITEMS", "not list")
        return items
    if kind == "product":
        axes = grammar.get("axes")
        if not isinstance(axes, list) or any(not isinstance(axis, list) for axis in axes):
            fail("ENUM_AXES", "bad product")
        items = [[]]
        for axis in axes:
            items = [prefix + [value] for prefix in items for value in axis]
        return items
    if kind == "integer_range":
        start = grammar.get("start")
        stop = grammar.get("stop")
        if not isinstance(start, int) or not isinstance(stop, int) or stop < start:
            fail("ENUM_RANGE", "bad range")
        return list(range(start, stop))
    fail("ENUM_KIND", repr(kind))


def opcode_enum(args):
    try:
        items = enumerate_grammar(args.get("grammar"))
    except BuildFailure as exc:
        return result(False, str(exc))
    cert = args.get("certificate")
    if not isinstance(cert, dict):
        return result(False, "ENUM_CERTIFICATE")
    ids = []
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            return result(False, "ENUM_ITEM_ID")
        ids.append(item["id"])
    if ids != sorted(ids) or len(ids) != len(set(ids)):
        return result(False, "ENUM_ORDER_OR_DUPLICATE")
    grammar_sha = sha256_bytes(canonical_bytes(args.get("grammar")))
    if cert.get("grammar_sha256") != grammar_sha or cert.get("ids") != ids:
        return result(False, "ENUM_CERT_MISMATCH")
    if cert.get("nonempty") is True and not ids:
        return result(False, "ENUM_EMPTY")
    return result(True, "", ids=ids, items=items)


def opcode_domain(args):
    function = args.get("function")
    used_domain = args.get("used_domain")
    if not isinstance(function, dict) or "declared_domain" not in function:
        return result(False, "DOMAIN_INPUT", status="OUTSIDE")
    ok = normalize_expr(function["declared_domain"]) == normalize_expr(used_domain)
    return result(ok, "" if ok else "DOMAIN_MISMATCH", status="IN_DOMAIN" if ok else "OUTSIDE")


def unit_eval(expr, declarations):
    if isinstance(expr, str):
        if expr not in declarations:
            fail("UNITS_SYMBOL", expr)
        return declarations[expr]
    if isinstance(expr, int):
        return {}
    if not isinstance(expr, dict):
        fail("UNITS_EXPR", repr(expr))
    op = expr.get("op")
    args = expr.get("args", [])
    if op == "mul":
        out = {}
        for child in args:
            for key, power in unit_eval(child, declarations).items():
                out[key] = out.get(key, 0) + power
        return {key: value for key, value in out.items() if value != 0}
    if op == "div" and len(args) == 2:
        left = unit_eval(args[0], declarations)
        right = unit_eval(args[1], declarations)
        out = dict(left)
        for key, power in right.items():
            out[key] = out.get(key, 0) - power
        return {key: value for key, value in out.items() if value != 0}
    if op == "add":
        values = [unit_eval(child, declarations) for child in args]
        if not values or any(value != values[0] for value in values[1:]):
            fail("UNITS_ADD", "incompatible")
        return values[0]
    if op == "pow" and len(args) == 2 and isinstance(args[1], int):
        return {key: power * args[1] for key, power in unit_eval(args[0], declarations).items()}
    fail("UNITS_OP", repr(op))


def opcode_units(args):
    declarations = args.get("declarations")
    if not isinstance(declarations, dict):
        return result(False, "UNITS_DECLARATIONS")
    try:
        actual = unit_eval(args.get("expression"), declarations)
    except BuildFailure as exc:
        return result(False, str(exc))
    expected = args.get("expected")
    return result(actual == expected, "" if actual == expected else "UNITS_MISMATCH", dimensions=actual, classification=args.get("classification"))


def opcode_dag(args):
    graph = args.get("graph")
    required = args.get("required_parents")
    if not isinstance(graph, dict) or not isinstance(required, dict):
        return result(False, "DAG_INPUT")
    if graph != required:
        return result(False, "DAG_PARENT_MISMATCH")
    nodes = set(graph)
    for node, parents in graph.items():
        if not isinstance(parents, list) or node in parents or any(parent not in nodes for parent in parents):
            return result(False, "DAG_PARENT")
    visiting = set()
    visited = set()

    def visit(node):
        if node in visiting:
            return False
        if node in visited:
            return True
        visiting.add(node)
        for parent in graph[node]:
            if not visit(parent):
                return False
        visiting.remove(node)
        visited.add(node)
        return True

    if any(not visit(node) for node in sorted(nodes)):
        return result(False, "DAG_CYCLE")
    return result(True, "", nodes=sorted(nodes))


def variants(text):
    folded = text.casefold()
    joint = re.sub(r"[-_\s]+", " ", folded)
    spaced = re.sub(r"\s+", " ", folded).strip()
    return folded, spaced, joint.strip()


def opcode_m2(args):
    query = args.get("query")
    sources = args.get("sources")
    if not isinstance(query, str) or not isinstance(sources, list):
        return result(False, "M2_INPUT", hits=[])
    hits = []
    q_fixed, q_space, q_joint = variants(query)
    for source in sources:
        if not isinstance(source, dict) or set(source) != {"path", "text"}:
            return result(False, "M2_SOURCE", hits=[])
        text = source["text"]
        if not isinstance(text, str):
            return result(False, "M2_TEXT", hits=[])
        candidates = variants(text)
        modes = []
        if q_fixed in candidates[0]:
            modes.append("fixed")
        if q_space in candidates[1]:
            modes.append("whitespace")
        if q_joint in candidates[2]:
            modes.append("hyphen_space_underscore")
        try:
            tree = ast.parse(text)
            tokens = [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]
            if query in tokens:
                modes.append("ast_scope")
        except SyntaxError:
            pass
        if modes:
            start = text.casefold().find(q_fixed)
            hits.append({"modes": sorted(set(modes)), "path": source["path"], "span": [max(start, 0), max(start, 0) + len(query)]})
    return result(True, "", hits=hits)


def remove_mask(value, mask):
    if isinstance(value, dict):
        return {key: remove_mask(child, mask) for key, child in sorted(value.items()) if key not in mask}
    if isinstance(value, list):
        return [remove_mask(child, mask) for child in value]
    return value


def opcode_compare(args):
    mask = args.get("mask", [])
    if not isinstance(mask, list) or any(field not in MASK_FIELDS for field in mask):
        return result(False, "COMPARE_MASK")
    left = remove_mask(args.get("left"), set(mask))
    right = remove_mask(args.get("right"), set(mask))
    ok = canonical_bytes(left) == canonical_bytes(right)
    return result(ok, "" if ok else "COMPARE_MISMATCH", normal_form=left)


def opcode_runtime(args):
    record = args.get("record")
    contract = args.get("contract")
    if not isinstance(record, dict) or not isinstance(contract, dict):
        return result(False, "RUNTIME_INPUT")
    forbidden = []
    for field in ("process_events", "network_events", "unknown_events"):
        if record.get(field):
            forbidden.append(field)
    if record.get("writes") != contract.get("allowed_writes"):
        forbidden.append("writes")
    return result(not forbidden, "" if not forbidden else "RUNTIME_FORBIDDEN", forbidden=forbidden)


def result(success, reason, **fields):
    out = {"reason": reason, "success": bool(success)}
    out.update(fields)
    return out


OPCODES = {
    "STRICT": opcode_strict,
    "SCHEMA": opcode_schema,
    "TYPE": opcode_type,
    "EXACT": opcode_exact,
    "KERNEL": opcode_kernel,
    "ENUM": opcode_enum,
    "DOMAIN": opcode_domain,
    "UNITS": opcode_units,
    "DAG": opcode_dag,
    "M2": opcode_m2,
    "COMPARE": opcode_compare,
    "RUNTIME": opcode_runtime,
}


def validate_program_contract(descriptor, evidence):
    exact_keys(evidence, {"descriptor_sha256", "input_files", "input_root_sha256", "invocations"}, "evidence record")
    if evidence["descriptor_sha256"] != descriptor["descriptor_sha256"]:
        fail("DESCRIPTOR_BINDING", descriptor["check_id"])
    if not isinstance(evidence["input_files"], list):
        fail("INPUT_FILES", descriptor["check_id"])
    if content_root(evidence["input_files"]) != evidence["input_root_sha256"]:
        fail("INPUT_ROOT", descriptor["check_id"])
    invocations = evidence["invocations"]
    if not isinstance(invocations, list):
        fail("INVOCATIONS", descriptor["check_id"])
    contracts = descriptor["program_contract"]
    allowed = {(item["result_name"], item["opcode"]): item for item in contracts}
    seen = {}
    for invocation in invocations:
        exact_keys(invocation, {"args", "instance_id", "opcode", "result_name"}, "invocation")
        key = (invocation["result_name"], invocation["opcode"])
        if key not in allowed:
            fail("INVOCATION_NOT_DECLARED", f"{descriptor['check_id']}:{key}")
        seen[key] = seen.get(key, 0) + 1
        if invocation["instance_id"] is not None and not isinstance(invocation["instance_id"], str):
            fail("INSTANCE_ID", descriptor["check_id"])
    for key, contract in allowed.items():
        count = seen.get(key, 0)
        if contract["repeatable"]:
            if count < 1:
                fail("INVOCATION_MISSING", f"{descriptor['check_id']}:{key}")
        elif count != 1:
            fail("INVOCATION_CARDINALITY", f"{descriptor['check_id']}:{key}:{count}")
    return invocations


def execute_structural(descriptor, evidence):
    try:
        invocations = validate_program_contract(descriptor, evidence)
    except BuildFailure as exc:
        return "FAIL", False, [], f"INPUT_INTEGRITY: {exc}"
    outputs = []
    for invocation in invocations:
        opcode = invocation["opcode"]
        if opcode in {"SYMBOLIC", "SPECTRAL"}:
            return "ERROR", True, [sha256_bytes(canonical_bytes(outputs))], f"F_PLDEC_OPCODE_IN_STRUCTURAL:{opcode}"
        function = OPCODES.get(opcode)
        if function is None:
            return "ERROR", True, [sha256_bytes(canonical_bytes(outputs))], f"UNKNOWN_OPCODE:{opcode}"
        try:
            value = function(invocation["args"])
        except BuildFailure as exc:
            value = result(False, str(exc))
        outputs.append(
            {
                "instance_id": invocation["instance_id"],
                "opcode": opcode,
                "result": value,
                "result_name": invocation["result_name"],
            }
        )
    ok = all(item["result"].get("success") is True for item in outputs)
    if "hits=empty" in descriptor["expected_predicate"].replace(" ", ""):
        ok = ok and all(not item["result"].get("hits") for item in outputs if "hits" in item["result"])
    digest = sha256_bytes(canonical_bytes(outputs))
    return ("PASS" if ok else "FAIL"), True, [digest], "" if ok else "PREDICATE_FALSE"


class AuditRecorder:
    def __init__(self):
        self.open_events = []
        self.process_events = []
        self.network_events = []
        self.mutation_events = []
        self.environment_events = []
        self.write_events = []

    def hook(self, event, args):
        text_args = []
        for value in args:
            if isinstance(value, (str, int, bool)) or value is None:
                text_args.append(value)
            else:
                text_args.append(type(value).__name__)
        record = {"args": text_args, "event": event}
        if event == "open":
            self.open_events.append(record)
        elif event.startswith("subprocess") or event in {"os.exec", "os.posix_spawn", "os.system"}:
            self.process_events.append(record)
        elif event.startswith("socket"):
            self.network_events.append(record)
        elif event in {"os.putenv", "os.unsetenv"}:
            self.environment_events.append(record)


def module_ledger():
    rows = []
    native = []
    for name, module in sorted(sys.modules.items()):
        path = getattr(module, "__file__", None)
        if not isinstance(path, str):
            rows.append({"kind": "builtin_or_frozen", "module": name, "path": None, "sha256": None})
            continue
        resolved = str(Path(path).resolve())
        suffix = Path(resolved).suffix.lower()
        try:
            data = Path(resolved).read_bytes()
            digest = sha256_bytes(data)
        except OSError:
            digest = None
        row = {"kind": "native" if suffix in {".so", ".dylib"} else "source", "module": name, "path": resolved, "sha256": digest}
        rows.append(row)
        if row["kind"] == "native":
            native.append(row)
    return rows, native


def exclusive_write(path, data):
    target = Path(path)
    if not target.parent.is_dir():
        fail("OUTPUT_PARENT", str(target.parent))
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    try:
        fd = os.open(str(target), flags, 0o600)
    except OSError as exc:
        fail("EXCLUSIVE_CREATE", f"{target}: {exc}")
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    except OSError as exc:
        fail("OUTPUT_WRITE", f"{target}: {exc}")


def check_manifest(manifest, optimize):
    required = {
        "allowed_events",
        "authority_firewall",
        "branch_outcome",
        "check_ids",
        "check_map_sha256",
        "evidence_manifest_sha256",
        "external_inputs",
        "fixture_ids",
        "fixture_manifest_sha256",
        "mode",
        "optimization",
        "package_files",
        "runtime_subject",
        "schema",
        "specification_sha256",
        "subject_lineage_root",
        "writable_paths",
    }
    exact_keys(manifest, required, "child manifest")
    if manifest["schema"] != "rd22.child-manifest.v001" or manifest["optimization"] != optimize:
        fail("MANIFEST_MODE", manifest.get("mode"))
    if optimize not in (0, 1):
        fail("OPTIMIZATION", optimize)
    expected_firewall = {
        "CORE_RESULT_SEAL": False,
        "FINAL_CLAIM_SEAL": False,
        "SPEC_SEAL": False,
        "alpha_computed": False,
        "authorization_claimed": False,
        "executed": False,
        "implemented": True,
        "kappa_record_computed": False,
        "proof_authorized": False,
    }
    if manifest["authority_firewall"] != expected_firewall:
        fail("AUTHORITY_FIREWALL", "manifest")


def make_check_row(descriptor, evidence_records, requirement_sha):
    check_id = descriptor["check_id"]
    base = {
        "blocker_id": descriptor["blocker_id"],
        "source": descriptor["source"],
        "check_id": check_id,
        "check_spec_sha256": descriptor["descriptor_sha256"],
        "execution_class": descriptor["execution_class"],
        "input_root_sha256": requirement_sha,
        "deterministic_procedure": descriptor["deterministic_procedure"],
        "prerequisites": ["P0"],
        "required_gate": descriptor["required_gate"],
        "expected_predicate": descriptor["expected_predicate"],
        "procedure_started": False,
        "status": "ERROR",
        "observed_evidence_sha256s": [],
        "reason": "",
    }
    if descriptor["execution_class"] == GATED_CLASS:
        base["status"] = "NOT_RUN_GATE"
        base["reason"] = "RD22_STRUCTURAL_ONLY_GATE_CLOSED"
        return base
    record = evidence_records.get(check_id)
    if not isinstance(record, dict) or record.get("available") is not True:
        base["status"] = "FAIL"
        base["reason"] = "INPUT_INTEGRITY: STRUCTURAL_EVIDENCE_NOT_SUPPLIED"
        return base
    status, started, hashes, reason = execute_structural(descriptor, record.get("evidence"))
    if status not in STATUS_SET:
        status = "ERROR"
        reason = "INVALID_INTERNAL_STATUS"
    base["procedure_started"] = started
    base["status"] = status
    base["observed_evidence_sha256s"] = hashes
    base["reason"] = reason
    if isinstance(record.get("evidence"), dict):
        base["input_root_sha256"] = record["evidence"].get("input_root_sha256", requirement_sha)
    return base


def fixture_base(fixture, requirement_sha):
    return {
        "fixture_id": fixture["fixture_id"],
        "source": fixture["source"],
        "fixture_spec_sha256": fixture["fixture_spec_sha256"],
        "primary_check_ids": fixture["primary_check_ids"],
        "execution_class": fixture["execution_class"],
        "input_root_sha256": requirement_sha,
        "mutation_ids": fixture["mutation_ids"],
        "deterministic_procedure": fixture["deterministic_procedure"],
        "prerequisites": fixture["prerequisites"],
        "required_gate": fixture["required_gate"],
        "expected_verdict_fields": fixture["expected_verdict_fields"],
        "procedure_started": False,
        "status": "ERROR",
        "observed_verdict_fields": {},
        "observed_evidence_sha256s": [],
        "reason": "",
    }


def make_fixture_row(fixture, fixture_records, requirement_sha):
    fixture_id = fixture["fixture_id"]
    base = fixture_base(fixture, requirement_sha)
    if fixture["execution_class"] == GATED_CLASS:
        base["status"] = "NOT_RUN_GATE"
        base["reason"] = "RD22_STRUCTURAL_ONLY_GATE_CLOSED"
        return base
    record = fixture_records.get(fixture_id)
    if not isinstance(record, dict) or record.get("available") is not True:
        base["status"] = "FAIL"
        base["reason"] = "STRUCTURAL_FIXTURE_EVIDENCE_NOT_SUPPLIED"
        return base
    observed = record.get("observed_verdict_fields")
    evidence_hashes = record.get("observed_evidence_sha256s")
    if not isinstance(observed, dict) or not isinstance(evidence_hashes, list):
        base["reason"] = "FIXTURE_OBSERVATION_SCHEMA"
        return base
    if any(not isinstance(item, str) or re.fullmatch(r"[0-9a-f]{64}", item) is None for item in evidence_hashes):
        base["reason"] = "FIXTURE_EVIDENCE_HASH"
        return base
    unexpected = sorted(set(observed) - set(fixture["expected_verdict_fields"]))
    base["procedure_started"] = True
    base["observed_verdict_fields"] = observed
    base["observed_evidence_sha256s"] = evidence_hashes
    if unexpected:
        base["reason"] = f"FIXTURE_QUARANTINE_UNDECLARED_FIELDS:{unexpected}"
        return base
    ok = observed == fixture["expected_verdict_fields"]
    base["reason"] = "" if ok else "FIXTURE_EXPECTATION_MISMATCH"
    base["status"] = "PASS" if ok else "FAIL"
    return base


def parse_args():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--manifest-sha256", required=True)
    parser.add_argument("--check-map", required=True)
    parser.add_argument("--check-map-sha256", required=True)
    parser.add_argument("--fixtures", required=True)
    parser.add_argument("--fixtures-sha256", required=True)
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--evidence-sha256", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--receipt", required=True)
    return parser.parse_args()


def main():
    start = time.monotonic()
    args = parse_args()
    optimize = sys.flags.optimize
    if sys.flags.isolated != 1 or sys.flags.no_site != 1 or sys.flags.dont_write_bytecode != 1:
        fail("ISOLATION_FLAGS", repr(sys.flags))
    if optimize not in (0, 1):
        fail("OPTIMIZE_LEVEL", optimize)
    recorder = AuditRecorder()
    sys.addaudithook(recorder.hook)
    manifest_data = verify_file(args.manifest, args.manifest_sha256)
    check_map_data = verify_file(args.check_map, args.check_map_sha256)
    fixture_data = verify_file(args.fixtures, args.fixtures_sha256)
    evidence_data = verify_file(args.evidence, args.evidence_sha256)
    manifest = strict_json_bytes(manifest_data, "manifest")
    check_map = strict_json_bytes(check_map_data, "check_map")
    fixtures = strict_json_bytes(fixture_data, "fixtures")
    evidence = strict_json_bytes(evidence_data, "evidence")
    check_manifest(manifest, optimize)
    if manifest["check_map_sha256"] != args.check_map_sha256 or manifest["fixture_manifest_sha256"] != args.fixtures_sha256 or manifest["evidence_manifest_sha256"] != args.evidence_sha256:
        fail("MANIFEST_ROOT_BINDING", "child inputs")
    exact_keys(check_map, {"branch_outcome", "check_ids", "checks", "descriptor_convention", "schema", "spec_sha256"}, "check_map")
    exact_keys(fixtures, {"fixture_ids", "fixtures", "schema", "spec_sha256"}, "fixtures")
    exact_keys(evidence, {"check_records", "fixture_records", "schema", "subject_lineage_root"}, "evidence")
    fixture_descriptor_fields = {
        "deterministic_procedure",
        "execution_class",
        "expected_verdict_fields",
        "fixture_id",
        "fixture_spec_sha256",
        "mutation_ids",
        "prerequisites",
        "primary_check_ids",
        "required_gate",
        "source",
    }
    for fixture in fixtures["fixtures"]:
        exact_keys(fixture, fixture_descriptor_fields, f"fixture descriptor {fixture.get('fixture_id')}")
    if check_map["check_ids"] != manifest["check_ids"] or fixtures["fixture_ids"] != manifest["fixture_ids"]:
        fail("ID_SET", "manifest mismatch")
    if check_map["branch_outcome"] != manifest["branch_outcome"]:
        fail("BRANCH_OUTCOME", "manifest mismatch")
    if evidence["subject_lineage_root"] != manifest["subject_lineage_root"]:
        fail("SUBJECT_LINEAGE", "evidence mismatch")
    requirement_sha = manifest["subject_lineage_root"]
    checks = [make_check_row(row, evidence["check_records"], requirement_sha) for row in check_map["checks"]]
    fixture_rows = [make_fixture_row(row, evidence["fixture_records"], requirement_sha) for row in fixtures["fixtures"]]
    summary = {
        "error": sum(row["status"] == "ERROR" for row in checks),
        "fail": sum(row["status"] == "FAIL" for row in checks),
        "gated": sum(row["execution_class"] == GATED_CLASS for row in checks),
        "not_run_gate": sum(row["status"] == "NOT_RUN_GATE" for row in checks),
        "pass": sum(row["status"] == "PASS" for row in checks),
        "structural": sum(row["execution_class"] == STRUCTURAL_CLASS for row in checks),
        "total": len(checks),
    }
    output = {
        "authority_firewall": manifest["authority_firewall"],
        "check_map_sha256": args.check_map_sha256,
        "checks": checks,
        "fixture_manifest_sha256": args.fixtures_sha256,
        "fixtures": fixture_rows,
        "manifest_sha256": args.manifest_sha256,
        "monotonic_duration": time.monotonic() - start,
        "process_id": os.getpid(),
        "python_optimize": optimize,
        "schema": SCHEMA,
        "scope": {
            "alpha_computed": False,
            "chain_invoked_by_builder": False,
            "fixed_point_executed": False,
            "kappa_record_computed": False,
            "member_binding": False,
            "physical_quantity_evaluated": False,
            "proof_authorized": False,
        },
        "spec_sha256": manifest["specification_sha256"],
        "subject_lineage_root": manifest["subject_lineage_root"],
        "summary": summary,
    }
    output_bytes = canonical_bytes(output)
    recorder.write_events.extend(
        [
            {"operation": "exclusive_create", "path": str(Path(args.output).resolve())},
            {"operation": "exclusive_create", "path": str(Path(args.receipt).resolve())},
        ]
    )
    recorder.mutation_events.extend(recorder.write_events)
    exclusive_write(args.output, output_bytes)
    modules, native = module_ledger()
    receipt = {
        "authority": False,
        "environment_event_ledger": recorder.environment_events,
        "manifest_sha256": args.manifest_sha256,
        "module_ledger": modules,
        "monotonic_duration": time.monotonic() - start,
        "mutation_event_ledger": recorder.mutation_events,
        "native_ledger": native,
        "network_event_ledger": recorder.network_events,
        "open_event_ledger": recorder.open_events,
        "optimize": optimize,
        "output_sha256": sha256_bytes(output_bytes),
        "process_event_ledger": recorder.process_events,
        "process_id": os.getpid(),
        "schema": RECEIPT_SCHEMA,
        "target_sha256": sha256_bytes(file_bytes(Path(__file__).resolve())),
        "write_event_ledger": recorder.write_events,
    }
    exclusive_write(args.receipt, canonical_bytes(receipt))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BuildFailure as exc:
        sys.stderr.write(f"RD22_PRODUCER_FAIL {exc}\n")
        raise SystemExit(2)
