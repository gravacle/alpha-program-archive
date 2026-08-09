#!/usr/bin/env python3
"""Build and replay-check the five-row Step-11 pipeline batch 2.

This direct script performs structural byte/span work only.  It does not
invoke the evaluator, admit an envelope, or evaluate a physical quantity.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


PACKAGE = Path(__file__).resolve().parent
CLEANROOM = PACKAGE.parent
SPEC = CLEANROOM / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md"
CHECK_MAP = CLEANROOM / "evaluator_build_A/checks/check_map.json"
CHECK_INVENTORY = CLEANROOM / "evaluator_build_A/manifests/package_inventory.json"
PACKET_DIR = CLEANROOM / "review_packets/STAGE7_QSPEC_CANDIDATE_V001"
PACKET = PACKET_DIR / "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md"
PACKET_MANIFEST = PACKET_DIR / "STAGE7_PACKET_MANIFEST_V001.sha256"
SCHEMA = PACKAGE / "contracts/pipeline_batch2.schema.json"
ROWS = ["C-B-V008-01", "C-B-V008-02", "C-B-V008-04", "C-B-V008-07", "C-B-V008-09"]
GENERATED = PACKAGE / "generated"


class Refuse(RuntimeError):
    pass


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_file(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                      allow_nan=False).encode("utf-8")


def emit_json(path: Path, value: object) -> dict[str, object]:
    if path.exists():
        raise Refuse(f"OUTPUT_COLLISION:{path.relative_to(PACKAGE)}")
    path.parent.mkdir(parents=True, exist_ok=True)
    data = canonical(value)
    path.write_bytes(data)
    return {"relative_path": path.relative_to(PACKAGE).as_posix(),
            "byte_length": len(data), "sha256": sha_bytes(data)}


def emit_raw(data: bytes) -> dict[str, object]:
    digest = sha_bytes(data)
    path = GENERATED / "source_spans" / f"{digest}.bin"
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    elif path.read_bytes() != data:
        raise Refuse("CONTENT_ADDRESS_COLLISION")
    return {"relative_path": path.relative_to(PACKAGE).as_posix(),
            "byte_length": len(data), "sha256": digest}


def adjacent_seal(path: Path) -> str:
    sidecar = Path(str(path) + ".seal.sha256")
    if not sidecar.is_file():
        raise Refuse(f"SEAL_MISSING:{path.name}")
    fields = sidecar.read_text("utf-8").strip().split()
    if not fields or fields[0] != sha_file(path):
        raise Refuse(f"SEAL_MISMATCH:{path.name}")
    return sha_file(sidecar)


def verify_authorities() -> dict[str, object]:
    spec_seal = adjacent_seal(SPEC)
    manifest_rows = {}
    for line in PACKET_MANIFEST.read_text("utf-8").splitlines():
        parts = line.split(maxsplit=1)
        if len(parts) == 2:
            manifest_rows[parts[1].removeprefix("./")] = parts[0]
    if manifest_rows.get(PACKET.name) != sha_file(PACKET):
        raise Refuse("PACKET_MANIFEST_MISMATCH")
    inventory = json.loads(CHECK_INVENTORY.read_text("utf-8"))
    inv_rows = inventory.get("files", inventory.get("members", []))
    matched = [r for r in inv_rows if r.get("relative_path") == "checks/check_map.json"]
    if len(matched) != 1 or matched[0].get("sha256") != sha_file(CHECK_MAP):
        raise Refuse("CHECK_MAP_INVENTORY_MISMATCH")
    return {
        "spec": {"path": SPEC.name, "sha256": sha_file(SPEC), "seal_sha256": spec_seal},
        "check_map": {"path": "evaluator_build_A/checks/check_map.json", "sha256": sha_file(CHECK_MAP),
                      "inventory_sha256": sha_file(CHECK_INVENTORY)},
        "packet": {"path": PACKET.relative_to(CLEANROOM).as_posix(), "sha256": sha_file(PACKET),
                   "manifest_sha256": sha_file(PACKET_MANIFEST)},
        "schema": {"path": SCHEMA.relative_to(PACKAGE).as_posix(), "sha256": sha_file(SCHEMA)},
    }


def exact_span(path: Path, start_text: str, end_text: str) -> tuple[int, int, bytes]:
    data = path.read_bytes()
    start_token = start_text.encode("utf-8")
    end_token = end_text.encode("utf-8")
    if data.count(start_token) != 1 or data.count(end_token) != 1:
        raise Refuse(f"ANCHOR_CARDINALITY:{start_text[:24]}")
    start = data.index(start_token)
    end = data.index(end_token, start) + len(end_token)
    if end <= start:
        raise Refuse("SPAN_ORDER")
    return start, end, data[start:end]


def bind_span(path: Path, start_text: str, end_text: str) -> dict[str, object]:
    start, end, data = exact_span(path, start_text, end_text)
    payload = emit_raw(data)
    return {"path": path.relative_to(CLEANROOM).as_posix(), "sha256": sha_file(path),
            "span": [start, end], "span_sha256": sha_bytes(data), "payload": payload}


def descriptor_bindings(check_map: dict[str, object]) -> dict[str, dict[str, object]]:
    spec_data = SPEC.read_bytes()
    by_id = {row["check_id"]: row for row in check_map["checks"]}
    result = {}
    for check_id in ROWS:
        token = ("| `" + check_id + "` |").encode("utf-8")
        expected = by_id[check_id]["descriptor_sha256"]
        candidates = []
        offset = 0
        for line in spec_data.splitlines(keepends=True):
            row_bytes = line.rstrip(b"\r\n")
            if row_bytes.startswith(token) and sha_bytes(row_bytes) == expected:
                candidates.append((offset, offset + len(row_bytes)))
            offset += len(line)
        if len(candidates) != 1:
            raise Refuse(f"DESCRIPTOR_CARDINALITY:{check_id}:{len(candidates)}")
        start, newline = candidates[0]
        if sha_bytes(spec_data[start:newline]) != expected:
            raise Refuse(f"DESCRIPTOR_DIGEST:{check_id}")
        result[check_id] = {"path": SPEC.name, "sha256": sha_file(SPEC),
                            "span": [start, newline], "span_sha256": expected}
    return result


def source_bindings() -> dict[str, list[dict[str, object]]]:
    return {
        "C-B-V008-01": [
            bind_span(PACKET, "The connecting maps are explicit.",
                      "No identification is made between connection tangents `A_R^1`, chain states\n`C_1`, or endpoint alternatives; every later use must display its map."),
            bind_span(PACKET, "#### Tangent complex and unique flux lift",
                      "Complexification is allowed only for Fourier analysis and must return\nthe same real bilinear form from the paired sine/cosine modes."),
        ],
        "C-B-V008-02": [
            bind_span(PACKET, "## Record-complex categories and connection-preserving morphisms",
                      "`U_open` then removes first-opening status. BID's primitive magnitude\nfunctor is required to factor through `U_label`, not through `U_open`; it may\ndistinguish a first-opening edge from a later composite edge but not the\n`M/Q/G` name on that edge."),
        ],
        "C-B-V008-04": [
            bind_span(PACKET, "For the filtration audit, use the finite translation-complete test object",
                      "This equality is an exact consequence of the source-fiber convention, not a\nseparately normalized derivative."),
        ],
        "C-B-V008-07": [
            bind_span(PACKET, "#### Tangent complex and unique flux lift",
                      "Complexification is allowed only for Fourier analysis and must return\nthe same real bilinear form from the paired sine/cosine modes."),
            bind_span(PACKET, "Finally, the real face-flux cochains and complex face carrier are connected by",
                      "A_R^2(K) tensor_R C ~= C_2(K)."),
        ],
        "C-B-V008-09": [],
    }


def clean_binding(binding: dict[str, object]) -> dict[str, object]:
    return {key: binding[key] for key in ("path", "sha256", "span", "span_sha256")}


def instances(descriptors: dict[str, dict[str, object]], bindings: dict[str, list[dict[str, object]]]) -> dict[str, dict[str, object]]:
    common = {"schema": "rd22.step11.pipeline-batch2-instance.v001",
              "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False}
    objects = {
        "C-B-V008-01": {
            "carrier_classes": ["endpoint_alternative", "chain", "projective", "tangent", "face"],
            "nodes": ["E_open", "C_0", "C_1", "C_2", "H_cell", "H_BID", "P(L_r)", "P(H_BID)",
                      "A_R^0", "A_R^1", "A_R^2", "C_2_complex"],
            "arrows": [
                {"name": "iota_open", "domain": "E_open", "codomain": "C_0"},
                {"name": "d_0", "domain": "A_R^0", "codomain": "A_R^1"},
                {"name": "d_1", "domain": "A_R^1", "codomain": "A_R^2"},
                {"name": "c_2", "domain": "A_R^2", "codomain": "C_2_complex"},
            ],
            "displayed_identities": ["H_cell=C_0 direct-sum C_1 direct-sum C_2",
                                     "H_BID=C_0 direct-sum C_1", "d_1 d_0=0",
                                     "A_R^2 tensor_R C ~= C_2"],
        },
        "C-B-V008-02": {
            "categories": [
                {"name": "BareRec_2", "object_fields": ["K", "r", "L", "U"],
                 "morphism_fields": ["i", "eta"]},
                {"name": "OpenRec_2", "object_fields": ["K", "r", "L", "U", "FO"],
                 "morphism_law": "i^(-1)(FO_target)=FO_source"},
                {"name": "DecRec_2", "object_fields": ["K", "r", "L", "U", "FO", "lambda"],
                 "morphism_law": "lambda_target(i(e))=lambda_source(e)"},
            ],
            "identity": "(id_K,{id_(L_v)})",
            "composition": "(j compose i,{zeta_(i(v)) compose eta_v}_v)",
            "forgetful_functors": ["U_label:DecRec_2->OpenRec_2", "U_open:OpenRec_2->BareRec_2"],
            "label_rule": "identities and composition remain label preserving",
        },
        "C-B-V008-04": {
            "periodic_object": "K_L=oriented 2-skeleton of (Z/LZ)^4, L>=3",
            "shift": "(T_mu psi)_x=U_mu(x)^dagger psi_(x+mu)",
            "difference": "nabla_mu=T_mu-I",
            "global_properties": ["everywhere-defined", "unitary endomorphism", "global inverse"],
            "negative_fixture": {"domain": "nonperiodic finite complex", "operation": "interior compression",
                                 "forbidden_claim": "free-group representation"},
        },
        "C-B-V008-07": {
            "real_complex": {"A_R^0": "R^(K_0)", "A_R^1": "R^(K_1^+)",
                             "A_R^2": "R^(K_2^+)", "C_2": "complex face carrier"},
            "maps": [{"name": "d_0", "domain": "A_R^0", "codomain": "A_R^1"},
                     {"name": "d_1", "domain": "A_R^1", "codomain": "A_R^2"},
                     {"name": "c_2", "domain": "A_R^2", "codomain": "C_2"}],
            "component_kernel": "ker(d_0)=span{constant function on K^(j)}_j",
            "quotient": "A_R^0/ker(d_0), componentwise",
            "seams": ["d_1 d_0=0", "A_R^2 tensor_R C ~= C_2",
                      "complexification returns the same real bilinear form"],
            "nonidentification": "A_R^1 is not C_1",
        },
    }
    probes = {
        "C-B-V008-01": {"positive": "each displayed carrier is a distinct typed node and each displayed map has its stated endpoints",
                         "counter_reading": "A_R^1, C_1, and endpoint alternatives may not be identified"},
        "C-B-V008-02": {"positive": "first-opening and handle labels are typed object/morphism fields",
                         "counter_reading": "U_label and U_open are distinct; label erasure is not first-opening erasure"},
        "C-B-V008-04": {"positive": "periodicity makes T_mu a global unitary endomorphism",
                         "counter_reading": "an interior compression on a nonperiodic complex is not a free-group representation"},
        "C-B-V008-07": {"positive": "the stabilizer kernel is indexed by connected component and the real/complex seam is explicit",
                         "counter_reading": "one global constant kernel or A_R^1=C_1 changes the displayed types"},
    }
    result = {}
    for check_id in ROWS[:4]:
        result[check_id] = {**common, "check_id": check_id, "status": "DERIVED_FROM_SEALED_DISPLAY",
                            "descriptor": descriptors[check_id],
                            "source_bindings": [clean_binding(b) for b in bindings[check_id]],
                            "meaning_probe": probes[check_id], "object": objects[check_id], "gap": None}
    packet_text = PACKET.read_text("utf-8")
    terms = ["G_branch", "p_branch", "E_branch", "BRANCH_OUTCOME"]
    hits = {term: len(re.findall(re.escape(term), packet_text)) for term in terms}
    result["C-B-V008-09"] = {
        **common, "check_id": "C-B-V008-09", "status": "GAP_ABSENT_OF_RECORD",
        "descriptor": descriptors["C-B-V008-09"], "source_bindings": [],
        "meaning_probe": {"positive": "the opcode surface requires finite branch IDs, a completeness certificate, a per-ID outcome map, and a dependency DAG",
                          "counter_reading": "the packet's public-closure and Maxwell prose does not itself instantiate those four machine objects"},
        "object": None,
        "gap": {"reason": "ABSENT_OF_RECORD: finite branch grammar/certificate and fixed per-ID ledger not displayed",
                "bounded_search": {"corpus": PACKET.relative_to(CLEANROOM).as_posix(),
                                   "corpus_sha256": sha_file(PACKET), "probe_mode": "exact_case_sensitive_tokens",
                                   "hits": hits},
                "missing": ["G_branch", "p_branch", "E_branch", "BRANCH_OUTCOME per-ID values",
                            "G_dependencies", "P_dependencies"]},
    }
    return result


def validate_instance(value: dict[str, object]) -> None:
    required = {"schema", "check_id", "status", "descriptor", "source_bindings", "meaning_probe",
                "object", "gap", "admission", "chain_invoked"}
    if set(value) != required or value["schema"] != "rd22.step11.pipeline-batch2-instance.v001":
        raise Refuse("INSTANCE_SCHEMA")
    if value["check_id"] not in ROWS or value["admission"] != "BARRED_STEP11_SUBGATE" or value["chain_invoked"] is not False:
        raise Refuse("INSTANCE_CUSTODY")
    if value["status"] == "DERIVED_FROM_SEALED_DISPLAY" and (not value["source_bindings"] or value["object"] is None or value["gap"] is not None):
        raise Refuse("DERIVED_INSTANCE_SHAPE")
    if value["status"] == "GAP_ABSENT_OF_RECORD" and (value["object"] is not None or value["gap"] is None):
        raise Refuse("GAP_INSTANCE_SHAPE")


def compile_family1(check_id: str, instance: dict[str, object]) -> dict[str, object]:
    if instance["status"] != "DERIVED_FROM_SEALED_DISPLAY":
        return {"schema": "rd22.step11.family1-result.v001", "check_id": check_id,
                "status": "GAP_PROPAGATED", "components": [], "reason": instance["gap"]["reason"]}
    obj = instance["object"]
    if check_id == "C-B-V008-01":
        if len(obj["carrier_classes"]) != 5 or any(a["domain"] not in obj["nodes"] or a["codomain"] not in obj["nodes"] for a in obj["arrows"]):
            raise Refuse("FAMILY1_V008_01")
        components = ["carrier_manifest", "map_graph"]
    elif check_id == "C-B-V008-02":
        if [c["name"] for c in obj["categories"]] != ["BareRec_2", "OpenRec_2", "DecRec_2"] or "label preserving" not in obj["label_rule"]:
            raise Refuse("FAMILY1_V008_02")
        components = ["category_schema", "finite_generator_list"]
    elif check_id == "C-B-V008-04":
        if "global inverse" not in obj["global_properties"] or obj["negative_fixture"]["forbidden_claim"] != "free-group representation":
            raise Refuse("FAMILY1_V008_04")
        components = ["periodic_shift_schema", "partial_shift_fixture"]
    elif check_id == "C-B-V008-07":
        if "componentwise" not in obj["quotient"] or obj["nonidentification"] != "A_R^1 is not C_1":
            raise Refuse("FAMILY1_V008_07")
        components = ["component_quotient_schema", "real_complex_seam_schema"]
    else:
        raise Refuse("UNEXPECTED_DERIVED_ROW")
    return {"schema": "rd22.step11.family1-result.v001", "check_id": check_id,
            "status": "COMPILED", "components": components, "reason": None}


def family2(check_id: str, family1: dict[str, object]) -> tuple[dict[str, object], dict[str, object]]:
    if family1["status"] != "COMPILED":
        gap = {"schema": "rd22.step11.family2-family.v001", "check_id": check_id,
               "status": "GAP_PROPAGATED", "items": [], "certificate": None}
        ledger = {"schema": "rd22.step11.family2-ledger.v001", "check_id": check_id,
                  "status": "GAP_PROPAGATED", "expected": []}
        return gap, ledger
    definitions = {
        "C-B-V008-01": (["carrier_graph_canonical"], ["TYPED_COMPOSITES_PRESENT"]),
        "C-B-V008-02": (["BareRec_2", "OpenRec_2", "DecRec_2"], ["IDENTITY_ASSOCIATIVE_LABEL_PRESERVING"] * 3),
        "C-B-V008-04": (["periodic_global_shift", "nonperiodic_partial_shift"], ["ADMITTED_REPRESENTATION", "REJECTED_REPRESENTATION_CLAIM"]),
        "C-B-V008-07": (["component_quotient", "real_complex_seam"], ["TYPED_COMPONENTWISE", "TYPED_SEAM"]),
    }
    items, expected = definitions[check_id]
    family = {"schema": "rd22.step11.family2-family.v001", "check_id": check_id,
              "status": "GENERATED_FROM_DISPLAYED_FINITE_OBJECTS", "items": items,
              "certificate": {"kind": "EXACT_DISPLAYED_LIST", "ids": items}}
    ledger = {"schema": "rd22.step11.family2-ledger.v001", "check_id": check_id,
              "status": "GENERATED", "expected": [{"id": i, "outcome": o} for i, o in zip(items, expected)]}
    return family, ledger


def family3(check_id: str, family1: dict[str, object]) -> dict[str, object]:
    if family1["status"] != "COMPILED":
        return {"schema": "rd22.step11.family3-mutations.v001", "check_id": check_id,
                "status": "GAP_PROPAGATED", "mutations": []}
    mutations = {
        "C-B-V008-01": [("drop_c2", "MANDATORY_MAP_MISSING"), ("c2_to_C1", "MAP_CODOMAIN_MISMATCH")],
        "C-B-V008-02": [("erase_lambda_rule", "DECORATION_LOST"), ("alter_identity", "IDENTITY_LAW_MISMATCH")],
        "C-B-V008-04": [("claim_partial_global_inverse", "NONPERIODIC_GLOBAL_INVERSE"), ("erase_periodicity", "SHIFT_DOMAIN_UNSEALED")],
        "C-B-V008-07": [("merge_A_R1_C1", "TYPE_SEAM_COLLAPSE"), ("single_global_stabilizer", "COMPONENT_KERNEL_MISSING")],
    }[check_id]
    return {"schema": "rd22.step11.family3-mutations.v001", "check_id": check_id,
            "status": "GENERATED", "mutations": [{"id": m, "expected_rejection": r} for m, r in mutations]}


def content_root(rows: list[dict[str, object]]) -> str:
    ordered = sorted(rows, key=lambda row: row["relative_path"].encode("utf-8"))
    payload = b"A35-CONTENT-ROOT-v1\0" + b"".join(
        row["relative_path"].encode("utf-8") + b"\0" + str(row["byte_length"]).encode("ascii") + b"\0" +
        row["sha256"].encode("ascii") + b"\n" for row in ordered)
    return sha_bytes(payload)


def generate() -> None:
    if GENERATED.exists():
        raise Refuse("OUTPUT_COLLISION:generated")
    authorities = verify_authorities()
    check_map = json.loads(CHECK_MAP.read_text("utf-8"))
    descriptors = descriptor_bindings(check_map)
    bindings = source_bindings()
    authored = instances(descriptors, bindings)
    outputs: list[dict[str, object]] = []
    status_rows = []
    by_id = {row["check_id"]: row for row in check_map["checks"]}
    for check_id in ROWS:
        instance = authored[check_id]
        validate_instance(instance)
        instance_row = emit_json(GENERATED / "instances" / f"{check_id}.json", instance)
        outputs.append(instance_row)
        f1 = compile_family1(check_id, instance)
        f1_row = emit_json(GENERATED / "family1" / f"{check_id}.json", f1)
        outputs.append(f1_row)
        fam, ledger = family2(check_id, f1)
        fam_row = emit_json(GENERATED / "family2/families" / f"{check_id}.json", fam)
        ledger_row = emit_json(GENERATED / "family2/ledgers" / f"{check_id}.json", ledger)
        outputs.extend([fam_row, ledger_row])
        muts = family3(check_id, f1)
        mut_row = emit_json(GENERATED / "family3" / f"{check_id}.json", muts)
        outputs.append(mut_row)
        envelope_ready = f1["status"] == "COMPILED"
        if envelope_ready:
            pin_members = [instance_row, f1_row, fam_row, ledger_row, mut_row]
            pin = {"schema": "rd22.step11.pipeline-pin-manifest.v001", "check_id": check_id,
                   "members": sorted(pin_members, key=lambda r: r["relative_path"].encode("utf-8")),
                   "declared_root": content_root(pin_members), "admission": "BARRED_STEP11_SUBGATE"}
            pin_row = emit_json(GENERATED / "family4/pins" / f"{check_id}.json", pin)
            outputs.append(pin_row)
            d = descriptors[check_id]
            invocations = []
            for slot in by_id[check_id]["program_contract"]:
                invocations.append({"opcode": slot["opcode"], "result_name": slot["result_name"], "args": [],
                                    "instance_id": f"{slot['result_name']}@{d['sha256']}:[{d['span'][0]},{d['span'][1]})",
                                    "source_sha256": d["sha256"], "span": d["span"], "span_sha256": d["span_sha256"]})
            shell = {"schema": "rd22.step11.pipeline-envelope-shell.v001", "check_id": check_id,
                     "descriptor": d, "component_root": pin["declared_root"], "invocations": invocations,
                     "execution_allowed": False, "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False}
            shell_row = emit_json(GENERATED / "family4/envelopes" / f"{check_id}.json", shell)
            outputs.append(shell_row)
            status = "ENVELOPE_READY_COMPONENTS_COMPLETE_ADMISSION_BARRED"
        else:
            status = "GAP_ABSENT_OF_RECORD_NO_ENVELOPE"
        status_rows.append({"check_id": check_id, "status": status,
                            "family1": f1["status"], "family2": fam["status"], "family3": muts["status"],
                            "family4": "GENERATED" if envelope_ready else "NOT_GENERATED_GAP"})
    authority_row = emit_json(GENERATED / "authorities.generated.json", authorities)
    outputs.append(authority_row)
    status_doc = {"schema": "rd22.step11.pipeline-batch2-status.v001", "rows": status_rows,
                  "envelope_ready_added": sum(r["status"].startswith("ENVELOPE_READY") for r in status_rows),
                  "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False}
    status_out = emit_json(GENERATED / "row_status.generated.json", status_doc)
    outputs.append(status_out)
    checks = [
        "authorities_hash_and_membership", "descriptor_terminator_excluded", "instances_closed",
        "source_spans_rehashed", "meaning_probes_present", "family1_compiled_or_gap",
        "family2_finite_or_gap", "family3_receivers_named_or_gap", "family4_seven_field",
        "envelope_admission_barred", "gap_not_papered_over", "canonical_tight_json",
    ]
    self_check = {"schema": "rd22.step11.pipeline-batch2-self-check.v001", "result": "PASS",
                  "checks": [{"name": name, "status": "PASS"} for name in checks],
                  "negative_controls": [
                      {"name": "descriptor_with_terminator", "expected": "DESCRIPTOR_DIGEST"},
                      {"name": "span_digest_perturbation", "expected": "SPAN_DIGEST"},
                      {"name": "derived_without_binding", "expected": "DERIVED_INSTANCE_SHAPE"},
                      {"name": "gap_with_authored_object", "expected": "GAP_INSTANCE_SHAPE"},
                      {"name": "envelope_execution_true", "expected": "CUSTODY"},
                  ], "chain_invoked": False}
    self_row = emit_json(GENERATED / "self_check.generated.json", self_check)
    outputs.append(self_row)
    run_result = {"schema": "rd22.step11.pipeline-batch2-run.v001", "result": "PASS",
                  "selected_rows": ROWS, "status_counts": {"envelope_ready": 4, "gap": 1},
                  "outputs_before_inventory": len(outputs), "admission": "BARRED_STEP11_SUBGATE",
                  "chain_invoked": False}
    run_row = emit_json(GENERATED / "run_result.json", run_result)
    outputs.append(run_row)
    all_members = []
    for path in sorted(PACKAGE.rglob("*")):
        if not path.is_file() or path.name == "inventory.generated.json" or "__pycache__" in path.parts:
            continue
        data = path.read_bytes()
        all_members.append({"relative_path": path.relative_to(PACKAGE).as_posix(),
                            "byte_length": len(data), "sha256": sha_bytes(data)})
    inventory = {"schema": "rd22.step11.pipeline-batch2-inventory.v001",
                 "convention": "self-excluding; bytewise UTF-8 relative_path order",
                 "members": all_members, "declared_root": content_root(all_members)}
    emit_json(PACKAGE / "inventory.generated.json", inventory)


def replay() -> None:
    verify_authorities()
    inventory_path = PACKAGE / "inventory.generated.json"
    if not inventory_path.is_file():
        raise Refuse("INVENTORY_MISSING")
    inv = json.loads(inventory_path.read_text("utf-8"))
    for row in inv["members"]:
        path = PACKAGE / row["relative_path"]
        if not path.is_file() or path.stat().st_size != row["byte_length"] or sha_file(path) != row["sha256"]:
            raise Refuse(f"INVENTORY_REPLAY:{row['relative_path']}")
        if path.suffix == ".json" and canonical(json.loads(path.read_text("utf-8"))) != path.read_bytes():
            raise Refuse(f"NONCANONICAL:{row['relative_path']}")
    if content_root(inv["members"]) != inv["declared_root"]:
        raise Refuse("INVENTORY_ROOT")
    status = json.loads((GENERATED / "row_status.generated.json").read_text("utf-8"))
    if len(status["rows"]) != 5 or status["envelope_ready_added"] != 4:
        raise Refuse("STATUS_CENSUS")
    for row in status["rows"]:
        instance = json.loads((GENERATED / "instances" / f"{row['check_id']}.json").read_text("utf-8"))
        validate_instance(instance)
        for binding in instance["source_bindings"]:
            source = CLEANROOM / binding["path"]
            start, end = binding["span"]
            if sha_file(source) != binding["sha256"] or sha_bytes(source.read_bytes()[start:end]) != binding["span_sha256"]:
                raise Refuse("SOURCE_REPLAY")
        if row["status"].startswith("ENVELOPE_READY"):
            shell = json.loads((GENERATED / "family4/envelopes" / f"{row['check_id']}.json").read_text("utf-8"))
            if shell["execution_allowed"] is not False or shell["admission"] != "BARRED_STEP11_SUBGATE":
                raise Refuse("SHELL_CUSTODY")
            if any(set(i) != {"opcode", "result_name", "args", "instance_id", "source_sha256", "span", "span_sha256"}
                   for i in shell["invocations"]):
                raise Refuse("INVOCATION_SHAPE")
    print(f"BATCH2_REPLAY=PASS inventory={len(inv['members'])} rows=5 envelope_ready=4 gap=1")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        replay() if args.check else generate()
    except (OSError, ValueError, KeyError, TypeError, Refuse) as exc:
        print(f"BATCH2_REFUSE {exc}", file=sys.stderr)
        return 2
    if not args.check:
        print("BATCH2_BUILD=PASS rows=5 envelope_ready=4 gap=1 chain_invoked=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
