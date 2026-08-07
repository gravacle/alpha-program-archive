#!/usr/bin/env python3
"""Assemble D1 by copying sealed bytes and recording bounded absences.

This tool never manufactures an opcode invocation or fixture observation.  It
copies selected sealed search/display sources byte-for-byte, searches the full
sealed packet plus named sealed workspace records, and emits metadata stating
whether the exact runtime evidence envelope is of record.
"""

import hashlib
import json
import re
import shutil
from pathlib import Path


PACKET_MANIFEST_SHA256 = "9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311"
EXPECTED_SOURCES = {
    "BID_FULL_STACK_REVIEW_LEDGER_V003.md": "c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8",
    "STAGE8_TASK6_A21_OPEN_LEG_DISPOSITION_LANE2_V001.md": "414067e25dbae39f7767d57144c953a0f98bb11d4c34178ec70097efabc0ebf7",
    "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md": "f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b",
    "STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md": "bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362",
    "STAGE8_TASK6_LP_MATRIX_LEDGER_REVIEW_DARIO_V001.md": "a83289e67615d6faa2c1c942105ee6b595034f78d31fcf4e16ac5366fd1d7743",
    "STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md": "76589e94bb4af318880c61c3d677dc2518add8480100a7afaf675e4dd3a394a8",
}
PACKET_COPIES = {
    "BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md": "0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98",
    "BID_SOURCE_PARENT_CLOSURE_GATE_V003.md": "5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf",
    "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md": "aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a",
    "STAGE7_PACKET_MANIFEST_V001.sha256": PACKET_MANIFEST_SHA256,
}
MODES = [
    "fixed_string",
    "whitespace_normalized",
    "self_reference_scope",
    "hyphen_space_underscore",
]
ENVELOPE_FIELDS = ["descriptor_sha256", "input_files", "input_root_sha256", "invocations"]
OPCODE_WORDS = {
    "COMPARE", "DAG", "DOMAIN", "ENUM", "EXACT", "KERNEL", "M2",
    "RUNTIME", "SCHEMA", "SPECTRAL", "STRICT", "SYMBOLIC", "TYPE", "UNITS",
}


def fail(code, detail):
    raise SystemExit(f"EVIDENCE_ASSEMBLY_FAIL {code}: {detail}")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def read_json(path):
    data = path.read_bytes()
    value = json.loads(data.decode("utf-8"))
    if canonical(value) != data:
        fail("NONCANONICAL_JSON", path)
    return value


def verify(path, expected):
    data = path.read_bytes()
    actual = sha(data)
    if actual != expected:
        fail("PIN", f"{path}: expected {expected}, got {actual}")
    return data


def normalize_ws(text):
    return re.sub(r"\s+", " ", text.casefold()).strip()


def normalize_variant(text):
    return re.sub(r"[-_\s]+", " ", text.casefold()).strip()


def count_occurrences(haystack, needle):
    if not needle:
        return 0
    return haystack.count(needle)


def source_row(path, relative, role, expected=None):
    data = path.read_bytes()
    digest = sha(data)
    if expected is not None and digest != expected:
        fail("SOURCE_PIN", f"{relative}: {digest}")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        text = ""
    return {
        "data": data,
        "path": path,
        "relative_path": relative,
        "role": role,
        "sha256": digest,
        "text": text,
        "fixed": text.casefold(),
        "whitespace": normalize_ws(text),
        "variant": normalize_variant(text),
    }


def packet_rows(packet, manifest_path):
    manifest = verify(manifest_path, PACKET_MANIFEST_SHA256).decode("utf-8")
    rows = []
    seen = set()
    for line in manifest.splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  \./(.+)", line)
        if match is None:
            fail("PACKET_MANIFEST_LINE", line)
        expected, relative = match.groups()
        if relative in seen:
            fail("PACKET_DUPLICATE", relative)
        seen.add(relative)
        path = packet / relative
        rows.append(source_row(path, f"review_packets/STAGE7_QSPEC_CANDIDATE_V001/{relative}", "sealed_packet", expected))
    if len(rows) != 113:
        fail("PACKET_CENSUS", len(rows))
    return rows


def content_root(rows):
    records = [f"{row['relative_path']}\0{len(row['data'])}\0{row['sha256']}\n" for row in rows]
    return sha(b"A35-CONTENT-ROOT-v1\0" + "".join(sorted(records)).encode("utf-8"))


def copy_payload(source, evidence_dir):
    filename = f"{source['sha256']}--{source['path'].name}"
    target = evidence_dir / filename
    if target.exists():
        if target.read_bytes() != source["data"]:
            fail("PAYLOAD_COLLISION", target)
    else:
        shutil.copyfile(source["path"], target)
    if target.read_bytes() != source["data"] or sha(target.read_bytes()) != source["sha256"]:
        fail("PAYLOAD_COPY", target)
    return f"inputs/evidence/{filename}"


def distinctive_queries(descriptor):
    text = descriptor["inputs"] + " " + descriptor["deterministic_procedure"]
    candidates = set(re.findall(r"[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+", text))
    candidates.update(
        token for token in re.findall(r"\b[A-Z][A-Z0-9]{3,}\b", text)
        if token not in OPCODE_WORDS
    )
    ranked = sorted(candidates, key=lambda item: (-item.count("_"), -len(item), item))
    return ranked[:3]


def query_display(queries, rows):
    displays = []
    for query in queries:
        q_fixed = query.casefold()
        q_ws = normalize_ws(query)
        q_variant = normalize_variant(query)
        fixed = whitespace = variant = 0
        roles = {"requirements": 0, "review_display": 0, "sealed_packet": 0}
        for row in rows:
            fixed += count_occurrences(row["fixed"], q_fixed)
            whitespace += count_occurrences(row["whitespace"], q_ws)
            variant += count_occurrences(row["variant"], q_variant)
            roles[row["role"]] += count_occurrences(row["variant"], q_variant)
        displays.append({
            "fixed_hits": fixed,
            "hyphen_space_underscore_hits": variant,
            "query": query,
            "scope_hits": roles,
            "whitespace_hits": whitespace,
        })
    return displays


def line_span(data, offset):
    start = data.rfind(b"\n", 0, offset) + 1
    end = data.find(b"\n", offset)
    if end < 0:
        end = len(data)
    else:
        end += 1
    return [start, end]


def partial_payloads(queries, copied_sources, payload_paths, role):
    found = []
    used = set()
    for query in queries:
        q = query.casefold()
        for source in copied_sources:
            if source["role"] == "requirements":
                continue
            offset = source["fixed"].find(q)
            if offset < 0:
                continue
            key = source["relative_path"]
            if key in used:
                continue
            used.add(key)
            found.append({
                "payload_path": payload_paths[key],
                "payload_sha256": source["sha256"],
                "role": role,
                "source_path": source["relative_path"],
                "source_sha256": source["sha256"],
                "span": line_span(source["data"], offset),
            })
            break
        if len(found) == 2:
            break
    return found


def envelope_hits(identifier, rows):
    hits = []
    for row in rows:
        text = row["text"]
        if identifier in text and all(field in text for field in ENVELOPE_FIELDS):
            hits.append({"path": row["relative_path"], "sha256": row["sha256"]})
    return hits


def search_record(identifier, queries, rows, scope_sha256):
    complete = envelope_hits(identifier, rows)
    if complete:
        fail("UNADJUDICATED_COMPLETE_RECORD", {"identifier": identifier, "hits": complete})
    return {
        "complete_envelope_hits": complete,
        "modes": MODES,
        "queries": query_display(queries, rows),
        "result": "ABSENT_OF_RECORD",
        "scope_members": len(rows),
        "scope_sha256": scope_sha256,
    }


def main():
    package = Path(__file__).resolve().parents[1]
    cleanroom = package.parent
    packet = cleanroom / "review_packets/STAGE7_QSPEC_CANDIDATE_V001"
    manifest_path = packet / "STAGE7_PACKET_MANIFEST_V001.sha256"
    rows = packet_rows(packet, manifest_path)
    rows.append(source_row(manifest_path, "review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256", "requirements", PACKET_MANIFEST_SHA256))

    workspace_rows = []
    for relative, expected in EXPECTED_SOURCES.items():
        role = "requirements" if relative in {"BID_FULL_STACK_REVIEW_LEDGER_V003.md", "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md"} else "review_display"
        workspace_rows.append(source_row(cleanroom / relative, relative, role, expected))
    rows.extend(workspace_rows)
    scope_sha256 = content_root(rows)

    by_relative = {row["relative_path"]: row for row in rows}
    copy_relatives = list(EXPECTED_SOURCES)
    copy_relatives.extend(f"review_packets/STAGE7_QSPEC_CANDIDATE_V001/{name}" for name in PACKET_COPIES)
    copied_sources = []
    evidence_dir = package / "inputs/evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    payload_paths = {}
    for relative in copy_relatives:
        source = by_relative[relative]
        copied_sources.append(source)
        payload_paths[relative] = copy_payload(source, evidence_dir)
    expected_payload_names = {Path(path).name for path in payload_paths.values()}
    actual_payload_names = {path.name for path in evidence_dir.iterdir() if path.is_file()}
    if actual_payload_names != expected_payload_names:
        fail("PAYLOAD_CENSUS", {"expected": sorted(expected_payload_names), "actual": sorted(actual_payload_names)})

    check_map = read_json(package / "checks/check_map.json")
    fixtures = read_json(package / "fixtures/fixture_manifest.json")
    structural = [row for row in check_map["checks"] if row["execution_class"] == "STRUCTURAL"]
    check_records = {}
    for descriptor in structural:
        distinct = distinctive_queries(descriptor)
        queries = [descriptor["check_id"], descriptor["descriptor_sha256"], "invocations"] + distinct
        search = search_record(descriptor["descriptor_sha256"], queries, rows, scope_sha256)
        check_records[descriptor["check_id"]] = {
            "available": False,
            "descriptor_sha256": descriptor["descriptor_sha256"],
            "missing_objects": [
                f"complete_executable_binding_for:{descriptor['check_id']}",
                "runtime_envelope:{descriptor_sha256,input_files,input_root_sha256,invocations}",
            ],
            "partial_payloads": partial_payloads(distinct, copied_sources, payload_paths, "PARTIAL_DISPLAY_NOT_EXECUTABLE_RECORD"),
            "reason": "ABSENT_OF_RECORD: cited prose/display bytes do not contain the descriptor-bound invocation envelope and demanded machine objects",
            "search": search,
            "status": "ABSENT_OF_RECORD",
        }

    spec_source = by_relative["STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md"]
    fixture_records = {}
    for fixture in fixtures["fixtures"]:
        if fixture["execution_class"] != "STRUCTURAL":
            continue
        queries = [fixture["fixture_id"], "observed_verdict_fields", "observed_evidence_sha256s"] + sorted(fixture["expected_verdict_fields"])
        search = search_record(fixture["fixture_spec_sha256"], queries, rows, scope_sha256)
        start, end = fixture["source"]["byte_span"]
        fixture_records[fixture["fixture_id"]] = {
            "available": False,
            "fixture_spec_sha256": fixture["fixture_spec_sha256"],
            "missing_objects": [
                f"sealed_observation_for:{fixture['fixture_id']}",
                "observed_verdict_fields",
                "observed_evidence_sha256s",
            ],
            "partial_payloads": [{
                "payload_path": payload_paths[spec_source["relative_path"]],
                "payload_sha256": spec_source["sha256"],
                "role": "SPEC_FIXED_SUBJECT_NOT_OBSERVATION",
                "source_path": spec_source["relative_path"],
                "source_sha256": spec_source["sha256"],
                "span": [start, end],
            }],
            "reason": "ABSENT_OF_RECORD: the sealed table fixes the expected record and subject, but no sealed observed verdict/evidence record exists",
            "search": search,
            "status": "ABSENT_OF_RECORD",
        }

    old = read_json(package / "inputs/structural_evidence_manifest.json")
    evidence = {
        "check_records": check_records,
        "fixture_records": fixture_records,
        "schema": "rd22.structural-evidence-manifest.v001",
        "subject_lineage_root": old["subject_lineage_root"],
    }
    (package / "inputs/structural_evidence_manifest.json").write_bytes(canonical(evidence))
    print(json.dumps({
        "authored_payload_bytes": 0,
        "checks_absent": len(check_records),
        "checks_populated": 0,
        "fixtures_absent": len(fixture_records),
        "fixtures_populated": 0,
        "payload_files": len(expected_payload_names),
        "search_scope_members": len(rows),
        "search_scope_sha256": scope_sha256,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
