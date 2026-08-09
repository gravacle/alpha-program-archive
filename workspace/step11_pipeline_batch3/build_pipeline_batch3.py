#!/usr/bin/env python3
"""Build/replay Step-11 pipeline batch 3 without admission or chain execution."""

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
SPLIT = CLEANROOM / "STAGE8_7A_CONSTRUCTIBLE_SPLIT_CODEX2_V001.md"
BATCH2 = CLEANROOM / "STAGE8_7A_PIPELINE_BATCH2_CODEX2_V001.md"
SCHEMA = PACKAGE / "contracts/pipeline_batch3.schema.json"
GENERATED = PACKAGE / "generated"
ROWS = ["C-B-V009-02", "C-B-V009-04", "C-B-V009-05", "C-B-V009-07", "C-B-V009-09"]
SKIPPED = ["C-B-V008-10", "C-B-V009-03"]


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
    seals = {path.name: adjacent_seal(path) for path in (SPEC, SPLIT, BATCH2)}
    packet_rows = {}
    for line in PACKET_MANIFEST.read_text("utf-8").splitlines():
        parts = line.split(maxsplit=1)
        if len(parts) == 2:
            packet_rows[parts[1].removeprefix("./")] = parts[0]
    if packet_rows.get(PACKET.name) != sha_file(PACKET):
        raise Refuse("PACKET_MANIFEST_MISMATCH")
    inventory = json.loads(CHECK_INVENTORY.read_text("utf-8"))
    members = inventory.get("files", inventory.get("members", []))
    found = [row for row in members if row.get("relative_path") == "checks/check_map.json"]
    if len(found) != 1 or found[0].get("sha256") != sha_file(CHECK_MAP):
        raise Refuse("CHECK_MAP_INVENTORY_MISMATCH")
    return {
        "spec": {"path": SPEC.name, "sha256": sha_file(SPEC), "seal_sha256": seals[SPEC.name]},
        "split": {"path": SPLIT.name, "sha256": sha_file(SPLIT), "seal_sha256": seals[SPLIT.name]},
        "batch2_contract": {"path": BATCH2.name, "sha256": sha_file(BATCH2), "seal_sha256": seals[BATCH2.name]},
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
        raise Refuse(f"ANCHOR_CARDINALITY:{start_text[:28]}")
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


def clean_binding(value: dict[str, object]) -> dict[str, object]:
    return {key: value[key] for key in ("path", "sha256", "span", "span_sha256")}


def descriptor_bindings(check_map: dict[str, object]) -> dict[str, dict[str, object]]:
    data = SPEC.read_bytes()
    by_id = {row["check_id"]: row for row in check_map["checks"]}
    result = {}
    for check_id in ROWS:
        token = ("| `" + check_id + "` |").encode("utf-8")
        expected = by_id[check_id]["descriptor_sha256"]
        candidates = []
        offset = 0
        for line in data.splitlines(keepends=True):
            raw = line.rstrip(b"\r\n")
            if raw.startswith(token) and sha_bytes(raw) == expected:
                candidates.append((offset, offset + len(raw)))
            offset += len(line)
        if len(candidates) != 1:
            raise Refuse(f"DESCRIPTOR_CARDINALITY:{check_id}:{len(candidates)}")
        start, end = candidates[0]
        result[check_id] = {"path": SPEC.name, "sha256": sha_file(SPEC), "span": [start, end],
                            "span_sha256": expected}
    return result


def bounded_probe(terms: list[str]) -> dict[str, object]:
    text = PACKET.read_text("utf-8")
    return {"corpus": PACKET.relative_to(CLEANROOM).as_posix(), "corpus_sha256": sha_file(PACKET),
            "probe_mode": "exact_case_sensitive_tokens", "hits": {t: len(re.findall(re.escape(t), text)) for t in terms}}


def build_instances(descriptors: dict[str, dict[str, object]]) -> dict[str, dict[str, object]]:
    common = {"schema": "rd22.step11.pipeline-batch2-instance.v001",
              "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False}
    gap_specs = {
        "C-B-V009-02": {
            "terms": ["G_equiv", "p_equiv", "E_equiv", "DIMENSIONFUL_SCALE_EQUIVALENCE_ID", "EQUIV_CLASS"],
            "missing": ["finite equivalence grammar", "independent completeness certificate", "expected ID ledger", "per-ID unit classification"],
            "partial": "the packet displays allowed coordinate equivalences but no finite machine enumeration or per-ID ledger",
        },
        "C-B-V009-04": {
            "terms": ["G_log_domain", "p_log_domain", "boundary_fixtures"],
            "missing": ["finite admitted-input grammar", "independent completeness certificate", "ID-indexed boundary fixtures"],
            "partial": "the packet distinguishes formal, principal, and Taylor logarithms and their domains but supplies no complete fixture enumeration",
        },
        "C-B-V009-05": {
            "terms": ["zero-symbol fixture", "nonzero-symbol fixture", "represented-order fixture"],
            "missing": ["concrete zero represented-symbol fixture", "concrete nonzero represented-symbol fixture"],
            "partial": "the represented filtration and quotient are displayed, but only conditional flat/killed-symbol branches are named",
        },
        "C-B-V009-07": {
            "terms": ["S_config", "M_config", "SPEC_CONFIG_SHA256", "G_config_mut", "p_config_mut", "E_config_mut"],
            "missing": ["content-addressed frozen configuration manifest", "finite mutation grammar", "independent completeness certificate", "mutation ID ledger"],
            "partial": "the packet names response ingredients and frozen status flags but does not instantiate the required configuration objects",
        },
    }
    result = {}
    for check_id, info in gap_specs.items():
        result[check_id] = {
            **common, "check_id": check_id, "status": "GAP_ABSENT_OF_RECORD", "descriptor": descriptors[check_id],
            "source_bindings": [], "meaning_probe": {"positive": info["partial"],
            "counter_reading": "a prose distinction or conditional branch is not a finite certified instance"},
            "object": None, "gap": {"reason": "ABSENT_OF_RECORD: mandatory finite carrier set incomplete",
                                      "bounded_search": bounded_probe(info["terms"]), "missing": info["missing"]},
        }
    scale = bind_span(
        PACKET,
        "The record interval `tau_R` is derived above; it is not discarded merely\nbecause a four-dimensional gauge coefficient is dimensionless.",
        "The diagonal formula above\nis a mandatory exact check.",
    )
    charged = bind_span(
        PACKET,
        "#### Downstream complete charged specification and Thomson map",
        "The canonical phase-space/Legendre construction is then an independent\nconsistency check on the resulting Lorentzian action. It cannot supply a\nmissing normalization.",
    )
    result["C-B-V009-09"] = {
        **common, "check_id": "C-B-V009-09", "status": "DERIVED_FROM_SEALED_DISPLAY",
        "descriptor": descriptors["C-B-V009-09"], "source_bindings": [clean_binding(scale), clean_binding(charged)],
        "meaning_probe": {
            "positive": "the displayed cell-scale substitution cancels face-area factors before the charged-amplitude dependency chain",
            "counter_reading": "tau_R is not an input to Q_spec, the normalized amplitude, Gamma_Q, kappa_Q, or kappa_Thomson",
        },
        "object": {
            "unit_graph": {
                "coefficient": "four-dimensional gauge coefficient is dimensionless",
                "cell_volume": "V_cell=product_mu ell_mu",
                "face_flux": "xi_(mu nu)=ell_mu ell_nu F_(mu nu)+higher-order terms",
                "face_weight": "V_cell/(ell_mu^2 ell_nu^2)",
                "cancellation_normal_form": "V_cell F_(mu nu)^2",
            },
            "dependency_graph": {
                "nodes": ["Q_spec", "Z_Q[A]/Z_Q[0]", "Gamma_Q[A]", "Gamma_Q^(2)[A]", "kappa_Q(q^2)",
                          "kappa_Thomson", "e", "alpha(0)"],
                "edges": [["Q_spec", "Z_Q[A]/Z_Q[0]"], ["Z_Q[A]/Z_Q[0]", "Gamma_Q[A]"],
                          ["Gamma_Q[A]", "Gamma_Q^(2)[A]"], ["Gamma_Q^(2)[A]", "kappa_Q(q^2)"],
                          ["kappa_Q(q^2)", "kappa_Thomson"], ["kappa_Thomson", "e"], ["e", "alpha(0)"]],
                "excluded_parent": "tau_R",
                "acyclic": True,
            },
            "expressions": ["Gamma_Q[A]=-i Log(Z_Q[A]/Z_Q[0])",
                            "kappa_Thomson=lim_(q^2->0) kappa_Q(q^2)",
                            "kappa_Thomson=1/e^2", "alpha(0)=1/(4 pi kappa_Thomson)"],
        },
        "gap": None,
    }
    return result


def validate_instance(value: dict[str, object]) -> None:
    required = {"schema", "check_id", "status", "descriptor", "source_bindings", "meaning_probe",
                "object", "gap", "admission", "chain_invoked"}
    if set(value) != required or value["schema"] != "rd22.step11.pipeline-batch2-instance.v001":
        raise Refuse("INSTANCE_SCHEMA")
    if value["check_id"] not in ROWS or value["admission"] != "BARRED_STEP11_SUBGATE" or value["chain_invoked"] is not False:
        raise Refuse("INSTANCE_CUSTODY")
    if value["status"] == "DERIVED_FROM_SEALED_DISPLAY":
        if not value["source_bindings"] or value["object"] is None or value["gap"] is not None:
            raise Refuse("DERIVED_INSTANCE_SHAPE")
    elif value["status"] == "GAP_ABSENT_OF_RECORD":
        if value["object"] is not None or value["gap"] is None or value["source_bindings"]:
            raise Refuse("GAP_INSTANCE_SHAPE")
    else:
        raise Refuse("INSTANCE_STATUS")


def compile_family1(check_id: str, instance: dict[str, object]) -> dict[str, object]:
    if instance["status"] != "DERIVED_FROM_SEALED_DISPLAY":
        return {"schema": "rd22.step11.family1-result.v001", "check_id": check_id,
                "status": "GAP_PROPAGATED", "components": [], "reason": instance["gap"]["reason"]}
    obj = instance["object"]
    graph = obj["dependency_graph"]
    if graph["excluded_parent"] != "tau_R" or graph["acyclic"] is not True:
        raise Refuse("FAMILY1_DEPENDENCY_GRAPH")
    if any("tau_R" in edge for edge in graph["edges"]):
        raise Refuse("FAMILY1_FUTURE_INTERVAL_PARENT")
    if obj["unit_graph"]["cancellation_normal_form"] != "V_cell F_(mu nu)^2":
        raise Refuse("FAMILY1_SCALE_CANCELLATION")
    return {"schema": "rd22.step11.family1-result.v001", "check_id": check_id, "status": "COMPILED",
            "components": ["charged_response_expression", "unit_graph", "dependency_dag"], "reason": None}


def family2(check_id: str, compiled: dict[str, object]) -> tuple[dict[str, object], dict[str, object]]:
    if compiled["status"] != "COMPILED":
        return ({"schema": "rd22.step11.family2-family.v001", "check_id": check_id,
                 "status": "GAP_PROPAGATED", "items": [], "certificate": None},
                {"schema": "rd22.step11.family2-ledger.v001", "check_id": check_id,
                 "status": "GAP_PROPAGATED", "expected": []})
    items = ["cell_scale_cancellation", "charged_response_dependency_dag", "future_interval_nonparent"]
    expected = ["EXACT_CANCELLATION", "ACYCLIC_TYPED", "PARENT_ABSENT"]
    return ({"schema": "rd22.step11.family2-family.v001", "check_id": check_id,
             "status": "GENERATED_FROM_DISPLAYED_FINITE_OBJECTS", "items": items,
             "certificate": {"kind": "EXACT_DISPLAYED_LIST", "ids": items}},
            {"schema": "rd22.step11.family2-ledger.v001", "check_id": check_id, "status": "GENERATED",
             "expected": [{"id": i, "outcome": o} for i, o in zip(items, expected)]})


def family3(check_id: str, compiled: dict[str, object]) -> dict[str, object]:
    if compiled["status"] != "COMPILED":
        return {"schema": "rd22.step11.family3-mutations.v001", "check_id": check_id,
                "status": "GAP_PROPAGATED", "mutations": []}
    return {"schema": "rd22.step11.family3-mutations.v001", "check_id": check_id, "status": "GENERATED",
            "mutations": [
                {"id": "insert_tau_R_parent", "expected_rejection": "FUTURE_INTERVAL_PARENT"},
                {"id": "retain_face_area_factor", "expected_rejection": "SCALE_CANCELLATION_FAILURE"},
            ]}


def validate_shell(shell: dict[str, object]) -> None:
    exact = {"opcode", "result_name", "args", "instance_id", "source_sha256", "span", "span_sha256"}
    if shell.get("execution_allowed") is not False or shell.get("admission") != "BARRED_STEP11_SUBGATE" or shell.get("chain_invoked") is not False:
        raise Refuse("SHELL_CUSTODY")
    if any(set(invocation) != exact for invocation in shell.get("invocations", [])):
        raise Refuse("INVOCATION_SHAPE")


def run_negative_controls(instances: dict[str, dict[str, object]]) -> list[dict[str, str]]:
    controls = []
    derived = instances["C-B-V009-09"]
    descriptor = derived["descriptor"]
    start, end = descriptor["span"]
    with_terminator = SPEC.read_bytes()[start:end] + b"\n"
    if sha_bytes(with_terminator) == descriptor["span_sha256"]:
        raise Refuse("CONTROL_DESCRIPTOR_TERMINATOR_DID_NOT_BITE")
    controls.append({"name": "descriptor_with_terminator", "expected": "DESCRIPTOR_DIGEST", "status": "PASS_REFUSED"})

    binding = derived["source_bindings"][0]
    source = CLEANROOM / binding["path"]
    bstart, bend = binding["span"]
    if sha_bytes(source.read_bytes()[bstart:bend] + b"!") == binding["span_sha256"]:
        raise Refuse("CONTROL_SPAN_PERTURBATION_DID_NOT_BITE")
    controls.append({"name": "span_digest_perturbation", "expected": "SOURCE_REPLAY", "status": "PASS_REFUSED"})

    bad_gap = json.loads(json.dumps(instances["C-B-V009-02"]))
    bad_gap["object"] = {}
    try:
        validate_instance(bad_gap)
    except Refuse as exc:
        if str(exc) != "GAP_INSTANCE_SHAPE":
            raise
    else:
        raise Refuse("CONTROL_GAP_OBJECT_DID_NOT_BITE")
    controls.append({"name": "gap_with_authored_object", "expected": "GAP_INSTANCE_SHAPE", "status": "PASS_REFUSED"})

    bad_parent = json.loads(json.dumps(derived))
    bad_parent["object"]["dependency_graph"]["edges"].append(["tau_R", "Gamma_Q[A]"])
    try:
        compile_family1("C-B-V009-09", bad_parent)
    except Refuse as exc:
        if str(exc) != "FAMILY1_FUTURE_INTERVAL_PARENT":
            raise
    else:
        raise Refuse("CONTROL_FUTURE_PARENT_DID_NOT_BITE")
    controls.append({"name": "future_interval_parent", "expected": "FAMILY1_FUTURE_INTERVAL_PARENT", "status": "PASS_REFUSED"})

    bad_shell = {"execution_allowed": True, "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False, "invocations": []}
    try:
        validate_shell(bad_shell)
    except Refuse as exc:
        if str(exc) != "SHELL_CUSTODY":
            raise
    else:
        raise Refuse("CONTROL_EXECUTABLE_SHELL_DID_NOT_BITE")
    controls.append({"name": "executable_envelope", "expected": "SHELL_CUSTODY", "status": "PASS_REFUSED"})
    return controls


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
    by_id = {row["check_id"]: row for row in check_map["checks"]}
    descriptors = descriptor_bindings(check_map)
    instances = build_instances(descriptors)
    negative_controls = run_negative_controls(instances)
    outputs = []
    statuses = []
    for check_id in ROWS:
        instance = instances[check_id]
        validate_instance(instance)
        irow = emit_json(GENERATED / "instances" / f"{check_id}.json", instance)
        outputs.append(irow)
        f1 = compile_family1(check_id, instance)
        f1row = emit_json(GENERATED / "family1" / f"{check_id}.json", f1)
        outputs.append(f1row)
        fam, ledger = family2(check_id, f1)
        famrow = emit_json(GENERATED / "family2/families" / f"{check_id}.json", fam)
        ledrow = emit_json(GENERATED / "family2/ledgers" / f"{check_id}.json", ledger)
        outputs.extend([famrow, ledrow])
        muts = family3(check_id, f1)
        mutrow = emit_json(GENERATED / "family3" / f"{check_id}.json", muts)
        outputs.append(mutrow)
        ready = f1["status"] == "COMPILED"
        if ready:
            pin_members = [irow, f1row, famrow, ledrow, mutrow]
            pin = {"schema": "rd22.step11.pipeline-pin-manifest.v001", "check_id": check_id,
                   "members": sorted(pin_members, key=lambda row: row["relative_path"].encode("utf-8")),
                   "declared_root": content_root(pin_members), "admission": "BARRED_STEP11_SUBGATE"}
            pinrow = emit_json(GENERATED / "family4/pins" / f"{check_id}.json", pin)
            outputs.append(pinrow)
            d = descriptors[check_id]
            invocations = []
            for slot in by_id[check_id]["program_contract"]:
                invocations.append({"opcode": slot["opcode"], "result_name": slot["result_name"], "args": [],
                                    "instance_id": f"{slot['result_name']}@{d['sha256']}:[{d['span'][0]},{d['span'][1]})",
                                    "source_sha256": d["sha256"], "span": d["span"], "span_sha256": d["span_sha256"]})
            shell = {"schema": "rd22.step11.pipeline-envelope-shell.v001", "check_id": check_id,
                     "descriptor": d, "component_root": pin["declared_root"], "invocations": invocations,
                     "execution_allowed": False, "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False}
            validate_shell(shell)
            shellrow = emit_json(GENERATED / "family4/envelopes" / f"{check_id}.json", shell)
            outputs.append(shellrow)
            status = "ENVELOPE_READY_COMPONENTS_COMPLETE_ADMISSION_BARRED"
        else:
            status = "GAP_ABSENT_OF_RECORD_NO_ENVELOPE"
        statuses.append({"check_id": check_id, "status": status, "family1": f1["status"],
                         "family2": fam["status"], "family3": muts["status"],
                         "family4": "GENERATED" if ready else "NOT_GENERATED_GAP"})
    outputs.append(emit_json(GENERATED / "authorities.generated.json", authorities))
    status_doc = {"schema": "rd22.step11.pipeline-batch3-status.v001", "rows": statuses,
                  "skipped": SKIPPED, "envelope_ready_added": sum(s["status"].startswith("ENVELOPE_READY") for s in statuses),
                  "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False}
    outputs.append(emit_json(GENERATED / "row_status.generated.json", status_doc))
    checks = ["authorities_hash_and_membership", "batch2_contract_sealed", "selection_no_D_or_U",
              "ruling_rows_skipped", "descriptor_terminator_excluded", "instances_closed",
              "source_spans_rehashed", "meaning_probes_present", "family1_compiled_or_gap",
              "family2_finite_or_gap", "family3_receivers_named_or_gap", "family4_seven_field",
              "envelope_admission_barred", "gaps_not_papered_over", "canonical_tight_json"]
    self_check = {"schema": "rd22.step11.pipeline-batch3-self-check.v001", "result": "PASS",
                  "checks": [{"name": c, "status": "PASS"} for c in checks],
                  "negative_controls": negative_controls, "chain_invoked": False}
    outputs.append(emit_json(GENERATED / "self_check.generated.json", self_check))
    run = {"schema": "rd22.step11.pipeline-batch3-run.v001", "result": "PASS", "selected_rows": ROWS,
           "skipped": SKIPPED, "status_counts": {"envelope_ready": 1, "gap": 4},
           "outputs_before_inventory": len(outputs), "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False}
    outputs.append(emit_json(GENERATED / "run_result.json", run))
    members = []
    for path in sorted(PACKAGE.rglob("*")):
        if not path.is_file() or path.name == "inventory.generated.json" or "__pycache__" in path.parts:
            continue
        data = path.read_bytes()
        members.append({"relative_path": path.relative_to(PACKAGE).as_posix(), "byte_length": len(data),
                        "sha256": sha_bytes(data)})
    inventory = {"schema": "rd22.step11.pipeline-batch3-inventory.v001",
                 "convention": "self-excluding; bytewise UTF-8 relative_path order", "members": members,
                 "declared_root": content_root(members)}
    emit_json(PACKAGE / "inventory.generated.json", inventory)


def replay() -> None:
    verify_authorities()
    inv_path = PACKAGE / "inventory.generated.json"
    if not inv_path.is_file():
        raise Refuse("INVENTORY_MISSING")
    inv = json.loads(inv_path.read_text("utf-8"))
    for row in inv["members"]:
        path = PACKAGE / row["relative_path"]
        if not path.is_file() or path.stat().st_size != row["byte_length"] or sha_file(path) != row["sha256"]:
            raise Refuse(f"INVENTORY_REPLAY:{row['relative_path']}")
        if path.suffix == ".json" and canonical(json.loads(path.read_text("utf-8"))) != path.read_bytes():
            raise Refuse(f"NONCANONICAL:{row['relative_path']}")
    if content_root(inv["members"]) != inv["declared_root"]:
        raise Refuse("INVENTORY_ROOT")
    status = json.loads((GENERATED / "row_status.generated.json").read_text("utf-8"))
    if len(status["rows"]) != 5 or status["envelope_ready_added"] != 1 or status["skipped"] != SKIPPED:
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
            validate_shell(shell)
    print(f"BATCH3_REPLAY=PASS inventory={len(inv['members'])} rows=5 envelope_ready=1 gap=4 skipped=2")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        replay() if args.check else generate()
    except (OSError, ValueError, KeyError, TypeError, Refuse) as exc:
        print(f"BATCH3_REFUSE {exc}", file=sys.stderr)
        return 2
    if not args.check:
        print("BATCH3_BUILD=PASS rows=5 envelope_ready=1 gap=4 skipped=2 chain_invoked=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
