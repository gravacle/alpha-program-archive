"""Builder B self-check: SYNTAX AND SCHEMA VALIDATION ONLY.

This never invokes the evaluator chain. Custodian C invokes the chain; Builder B
does not run what Builder B wrote. The self-check compiles every module, asserts
nothing (no load-bearing `assert`), verifies the package imports cleanly, and
validates the declared contracts against the sealed spec's field inventories.
"""

import compileall
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)


def fail(msg):
    sys.stdout.write("FAIL  %s\n" % msg)
    return 1


def main():
    faults = 0
    sys.stdout.write("== Builder B self-check (syntax/schema only) ==\n")

    ok = compileall.compile_dir(os.path.join(ROOT, "verifier"), quiet=2,
                                force=True)
    sys.stdout.write("compileall verifier/ : %s\n" % ("OK" if ok else "FAIL"))
    if not ok:
        faults += 1

    try:
        from verifier import (canonical_json, comparison, contracts, hashing,
                              replay, runtime_state, spec_census, verify)
    except Exception as exc:                      # noqa: BLE001 - fail closed
        return fail("import: %s" % exc)
    sys.stdout.write("import verifier.*    : OK\n")

    # contract inventories are non-empty and duplicate-free
    for name, fields in (("LEDGER_FIELDS", contracts.LEDGER_FIELDS),
                         ("CHECK_ROW_FIELDS", contracts.CHECK_ROW_FIELDS),
                         ("CHILD_ROW_FIELDS", contracts.CHILD_ROW_FIELDS),
                         ("AUTHORITY_FIREWALL_FIELDS",
                          contracts.AUTHORITY_FIREWALL_FIELDS)):
        if len(fields) != len(set(fields)) or not fields:
            faults += fail("%s: empty or duplicated" % name)
        else:
            sys.stdout.write("%-26s: %d fields\n" % (name, len(fields)))

    # conformance inventories (integration addendum, sealed Q-588)
    if len(contracts.CHILD_ROW_FIELDS) != 14:
        faults += fail("CHILD_ROW_FIELDS: %d, addendum says 14"
                       % len(contracts.CHILD_ROW_FIELDS))
    else:
        sys.stdout.write("CHILD_ROW_FIELDS          : 14 fields (+3 carriers)\n")
    if len(contracts.FIXTURE_ROW_FIELDS) != 16:
        faults += fail("FIXTURE_ROW_FIELDS: %d, addendum says 16"
                       % len(contracts.FIXTURE_ROW_FIELDS))
    else:
        sys.stdout.write("FIXTURE_ROW_FIELDS        : 16 fields\n")
    if len(contracts.VERIFIER_MANIFEST_FIELDS) != 12:
        faults += fail("VERIFIER_MANIFEST_FIELDS: %d, V009 §9 says 12"
                       % len(contracts.VERIFIER_MANIFEST_FIELDS))
    else:
        sys.stdout.write("VERIFIER_MANIFEST_FIELDS  : 12 fields "
                         "(+verifier_root_members)\n")
    if len(contracts.EVENT_LEDGER_FIELDS) != 6:
        faults += fail("EVENT_LEDGER_FIELDS: %d, addendum says 6"
                       % len(contracts.EVENT_LEDGER_FIELDS))
    else:
        sys.stdout.write("EVENT_LEDGER_FIELDS       : 6 digest carriers\n")

    # the launch manifest validates against its own closed contract
    from verifier import child_manifest, hashing
    try:
        _rows = child_manifest.root_member_rows(ROOT)
        m = child_manifest.build_manifest(
            contracts.root_from_members(_rows),
            dict((f, "1" * 64) for f in contracts.INPUT_ROOTS_FIELDS),
            "out/verdict.json", "out/receipt.json", False, _rows)
        child_manifest.manifest_sha256(m)
        sys.stdout.write("launch manifest           : validates, addressable\n")
    except Exception as exc:                      # noqa: BLE001 - fail closed
        faults += fail("launch manifest: %s" % exc)

    # fixture quarantine rule bites
    try:
        contracts.validate_fixture_row({
            "fixture_id": "FX", "source": {"path": "", "sha256": "0" * 64,
                                           "byte_span": [0, 0]},
            "fixture_spec_sha256": "0" * 64, "primary_check_ids": [],
            "execution_class": "STRUCTURAL", "input_root_sha256": "0" * 64,
            "mutation_ids": [], "deterministic_procedure": "",
            "prerequisites": [], "required_gate": None,
            "expected_verdict_fields": {"a": True},
            "procedure_started": False, "status": "PASS",
            "observed_verdict_fields": {"a": True, "smuggled": 1},
            "observed_evidence_sha256s": [], "reason": ""}, "fx")
        faults += fail("fixture quarantine did not bite")
    except canonical_json.VerifierFault:
        sys.stdout.write("fixture quarantine        : rejects undeclared field\n")

    # verdict schema: BOTH emission kinds must validate, and tampering must not
    import json as _json, re as _re
    _sch = _json.load(open(os.path.join(ROOT, "contracts",
                                        "verifier_verdict.schema.json"),
                           encoding="utf-8"))

    def _val(node, sch, path, errs):
        if "oneOf" in sch:
            oks = []
            for sub in sch["oneOf"]:
                e = []; _val(node, sub, path, e); oks.append(not e)
            if sum(oks) != 1:
                errs.append("%s: matched %d branches" % (path, sum(oks)))
            return
        if "const" in sch and node != sch["const"]:
            errs.append("%s: const" % path); return
        t = sch.get("type")
        if t == "object":
            if not isinstance(node, dict): errs.append("%s: obj" % path); return
            pr = sch.get("properties", {})
            for r in sch.get("required", []):
                if r not in node: errs.append("%s.%s: missing" % (path, r))
            if sch.get("additionalProperties") is False:
                for k in node:
                    if k not in pr: errs.append("%s.%s: undeclared" % (path, k))
            for k, v in node.items():
                if k in pr: _val(v, pr[k], "%s.%s" % (path, k), errs)
        elif t == "array":
            if not isinstance(node, list): errs.append("%s: arr" % path)
        elif t == "string":
            if not isinstance(node, str): errs.append("%s: str" % path); return
            if "pattern" in sch and not _re.match(sch["pattern"], node):
                errs.append("%s: pattern" % path)
        elif t == "boolean":
            if not isinstance(node, bool): errs.append("%s: bool" % path)

    _H = "0" * 64
    _SPEC = spec_census.SPEC_SHA256
    _full = {"schema": "gravacle.a35.verifier-verdict.v1", "spec_sha256": _SPEC,
             "verifier_sha256": _H,
             "runtime_subject": {"snapshot_sha256": runtime_state.AUTHORIZED_SNAPSHOT_SHA256,
                                 "gate_sha256": runtime_state.AUTHORIZED_GATE_SHA256,
                                 "trust_root": _H},
             "authorization_sha256": _H, "census": {}, "checks_replayed": [],
             "fixtures_replayed": [],
             "producer_comparison": {"quantification": "COMMON_MEMBER_ONLY"},
             "findings": [],
             "independence": {"producer_code_imported": False,
                              "expectations_source": "sealed specification bytes"},
             "authority_firewall": {"implemented": True, "executed": True,
                                    "authorization_claimed": False,
                                    "alpha_computed": False, "proof_authorized": False,
                                    "kappa_record_computed": False, "SPEC_SEAL": False,
                                    "CORE_RESULT_SEAL": False, "FINAL_CLAIM_SEAL": False},
             "verdict": "VERIFIED", "terminal_content_sha256": _H}
    _fault = {"schema": "gravacle.a35.verifier-verdict.v1", "verdict": "FAIL",
              "fault": "example"}
    for _name, _doc, _want_ok in (("full verdict", _full, True),
                                  ("fault verdict", _fault, True),
                                  ("full minus fixtures_replayed",
                                   {k: v for k, v in _full.items()
                                    if k != "fixtures_replayed"}, False),
                                  ("full + undeclared", dict(_full, x=1), False)):
        _e = []; _val(_doc, _sch, "$", _e)
        if bool(_e) == _want_ok:
            faults += fail("verdict schema %s: errors=%s" % (_name, _e[:2]))
        else:
            sys.stdout.write("verdict schema %-28s: %s\n"
                             % (_name, "valid" if _want_ok else "refused"))

    # Q-601 trust-label contexts
    R = "0" * 64
    ok3 = {"T0": R, "T1": R, "T2": R, "T3": R}
    with_t4 = dict(ok3); with_t4["T4"] = R
    try:
        runtime_state.revalidate_trust_snapshots(ok3, R, "in")
        sys.stdout.write("trust T0-T3 (input)  : accepted\n")
    except Exception as exc:                      # noqa: BLE001 - fail closed
        faults += fail("T0-T3 input rejected: %s" % exc)
    try:
        runtime_state.revalidate_trust_snapshots(with_t4, R, "in")
        faults += fail("FABRICATED T4 ACCEPTED in the verifier-input context")
    except canonical_json.VerifierFault as exc:
        if "FABRICATED_SNAPSHOT" in str(exc):
            sys.stdout.write("trust T4 in input    : refused as FABRICATED_SNAPSHOT\n")
        else:
            faults += fail("T4 refused for the wrong reason: %s" % exc)
    try:
        runtime_state.revalidate_trust_snapshots(
            with_t4, R, "term", context=runtime_state.CONTEXT_TERMINAL)
        sys.stdout.write("trust T0-T4 (terminal): accepted\n")
    except Exception as exc:                      # noqa: BLE001 - fail closed
        faults += fail("T0-T4 terminal rejected: %s" % exc)
    try:
        runtime_state.revalidate_trust_snapshots(
            ok3, R, "term", context=runtime_state.CONTEXT_TERMINAL)
        faults += fail("terminal accepted a record missing T4")
    except canonical_json.VerifierFault:
        sys.stdout.write("trust terminal w/o T4: refused\n")

    # canonical JSON round-trip and rejection behaviour
    if canonical_json.dumps_canonical({"b": 1, "a": 2}) != '{"a":2,"b":1}':
        faults += fail("canonical JSON key ordering")
    else:
        sys.stdout.write("canonical JSON       : sorted, compact\n")

    for bad, label in (('{"a":1,"a":2}', "duplicate key"),
                       ('{"a":NaN}', "NaN literal")):
        try:
            canonical_json.loads_strict(bad)
            faults += fail("strict parse accepted %s" % label)
        except canonical_json.VerifierFault:
            sys.stdout.write("strict parse rejects : %s\n" % label)

    # criterion splitting is opcode-reducible
    atoms = replay.split_conjuncts("P0 and r_a.success and (for every x in "
                                   "r_e.items: r_x.success)")
    if len(atoms) != 3:
        faults += fail("criterion split produced %d atoms" % len(atoms))
    else:
        sys.stdout.write("criterion split      : 3 atoms\n")

    # payload roles: digest-verify all, parse only the consumed.
    # Fixtures are SYNTHETIC on purpose -- the self-check must not read the
    # producer's inputs. The real V009-06 pair is demonstrated in the relay
    # artifact; what is asserted permanently here is the machinery.
    import hashlib

    def _p(blob):
        return (hashlib.sha256(blob).hexdigest(), blob)

    span = b'"stage_dependencies": {\n      "A": [],\n      "B": ["A"]\n    }'
    args = canonical_json.encode_canonical({"graph": {"A": [], "B": ["A"]},
                                            "required_parents": {"A": [],
                                                                 "B": ["A"]}})
    invocation = {"opcode": "DAG", "result_name": "r_dag",
                  "args": canonical_json.loads_strict(args.decode("utf-8"))}
    role_cases = [
        ("clean pair (raw first)", [_p(span), _p(args)], invocation, 1, 1, 0),
        ("clean pair, no invocation", [_p(span), _p(args)], None, 1, 1, 0),
        ("GUARD A non-canonical consumable", [_p(span), _p(b'{"graph" : {}}')],
         invocation, 0, 1, 3),
        ("GUARD A consumable not an object", [_p(span), _p(b"[1,2]")],
         invocation, 0, 1, 3),
        ("GUARD B raw alone, invocation", [_p(span)], invocation, 0, 1, 2),
        ("GUARD B raw alone, no invocation", [_p(span)], None, 0, 1, 1),
    ]
    for label, payloads, inv, want_c, want_r, want_f in role_cases:
        try:
            got = replay.classify_payloads(payloads, inv, "selfcheck")
        except Exception as exc:                  # noqa: BLE001 - fail closed
            faults += fail("payload roles %s: %s" % (label, exc))
            continue
        actual = (len(got["consumable"]), len(got["raw"]), len(got["faults"]))
        if actual != (want_c, want_r, want_f):
            faults += fail("payload roles %s: got %s want %s"
                           % (label, actual, (want_c, want_r, want_f)))
        else:
            sys.stdout.write("payload roles        : %s\n" % label)
    # the raw span is never promoted into a bundle, in any case above
    promoted = [label for label, payloads, inv, _c, _r, _f in role_cases
                if any(blob == span for _d, blob, _parsed
                       in replay.classify_payloads(payloads, inv,
                                                   "selfcheck")["consumable"])]
    if promoted:
        faults += fail("raw span promoted to consumable in %s" % promoted)
    else:
        sys.stdout.write("payload roles        : raw never promoted (6/6)\n")

    # the 15-field row contract: the `invocation` field is TYPED, not admitted
    _PROC = ("`r_ground:=COMPARE(a,b,empty)`; `r_dag:=DAG(g,"
             "PRINCIPAL_SINGLE_AUTHORITY)`")
    _IID = "sym@" + ("1" * 64) + ":[10,20)"
    _DAG = {"opcode": "DAG", "result_name": "r_dag", "args": {"g": {}},
            "instance_id": _IID, "source_sha256": "1" * 64,
            "span": [10, 20], "span_sha256": "2" * 64}

    def _row(invocation):
        return {"blocker_id": "B", "source": {"path": "p", "sha256": "0" * 64,
                                              "byte_span": [0, 1]},
                "check_id": "C-B-V009-06", "check_spec_sha256": "1" * 64,
                "execution_class": "STRUCTURAL", "input_root_sha256": "2" * 64,
                "deterministic_procedure": _PROC, "prerequisites": ["P0"],
                "required_gate": "G", "expected_predicate": "P0",
                "procedure_started": False, "status": "FAIL",
                "observed_evidence_sha256s": [], "reason": "r",
                "invocation": invocation}

    def _mut(**kw):
        d = dict(_DAG)
        d.update(kw)
        return d

    row_cases = [
        ("null", None, True),
        ("singular object", _DAG, True),
        ("list of two", [{"opcode": "COMPARE", "result_name": "r_ground",
                          "args": {}, "instance_id": None,
                          "source_sha256": None, "span": None,
                          "span_sha256": None}, _DAG], True),
        ("4-field invocation (spec §9.4 requires 7)",
         {"opcode": "DAG", "result_name": "r_dag", "args": {},
          "instance_id": _IID}, False),
        ("span disagrees with instance_id", _mut(span=[0, 1]), False),
        ("source_sha256 disagrees with instance_id",
         _mut(source_sha256="9" * 64), False),
        ("undeclared field", _mut(extra=1), False),
        ("opcode outside the closed 14", _mut(opcode="GREP"), False),
        ("result_name not an r_ symbol", _mut(result_name="dag"), False),
        ("args not an object", _mut(args=[]), False),
        ("instance_id malformed", _mut(instance_id="sym@beef:[1,2)"), False),
        ("instance_id span inverted", _mut(instance_id="sym@" + "1" * 64
                                           + ":[20,10)"), False),
        ("result not declared by the descriptor",
         _mut(result_name="r_bogus"), False),
        ("declared result, wrong opcode", _mut(opcode="COMPARE"), False),
        ("invocation is a string", "r_dag", False),
    ]
    for label, invocation, want_ok in row_cases:
        try:
            contracts.validate_check_row(_row(invocation), "selfcheck")
            got_ok = True
        except canonical_json.VerifierFault:
            got_ok = False
        if got_ok != want_ok:
            faults += fail("row contract %s: %s, wanted %s"
                           % (label, "accepted" if got_ok else "refused",
                              "accept" if want_ok else "refuse"))
        else:
            sys.stdout.write("row contract         : %s %s\n"
                             % ("accepts" if want_ok else "refuses", label))
    if len(contracts.CHECK_ROW_FIELDS) != 15 or len(contracts.OPCODES) != 14:
        faults += fail("inventories: %d row fields, %d opcodes (want 15, 14)"
                       % (len(contracts.CHECK_ROW_FIELDS),
                          len(contracts.OPCODES)))
    else:
        sys.stdout.write("row contract         : 15 fields, 14 opcodes\n")

    # byte-span linkage, and the non-object arguments that cannot be covered
    span_raw = b'"k": {\n  "A": []\n}'                     # 18 bytes, unparseable
    span_arg = canonical_json.encode_canonical({"g": {"A": []}})
    span_inv = [{"opcode": "DAG", "result_name": "r_dag",
                 "args": {"g": {"A": []}, "authority": "PRINCIPAL"},
                 "instance_id": "sym@" + "1" * 64 + ":[0,%d)" % len(span_raw)}]

    def _pp(blob):
        return (hashlib.sha256(blob).hexdigest(), blob)

    linked = replay.classify_payloads([_pp(span_raw), _pp(span_arg)],
                                      span_inv, "selfcheck")
    if (linked["faults"] or linked["raw"][0]["linkage"] != "digest+span"
            or linked["unrequired_args"] != ["authority"]):
        faults += fail("span linkage: %s" % linked)
    else:
        sys.stdout.write("span linkage         : digest+span; non-object arg "
                         "reported not faulted\n")
    span_inv[0]["instance_id"] = "sym@" + "1" * 64 + ":[0,999)"
    mismatch = replay.classify_payloads([_pp(span_raw), _pp(span_arg)],
                                        span_inv, "selfcheck")
    if not any("span of that length" in f for f in mismatch["faults"]):
        faults += fail("span linkage: length mismatch not faulted")
    else:
        sys.stdout.write("span linkage         : length mismatch refused\n")

    # opcode recomputation: the verifier replays FROM EVIDENCE BYTES
    _S = "PRINCIPAL_SINGLE_AUTHORITY"
    op_cases = [
        ("COMPARE equal", replay.opcode_compare,
         {"left": "a", "right": "a", "mask": []}, True),
        ("COMPARE unequal", replay.opcode_compare,
         {"left": "a", "right": "b", "mask": []}, False),
        ("COMPARE masked field ignored", replay.opcode_compare,
         {"left": {"k": 1, "t": 1}, "right": {"k": 1, "t": 2},
          "mask": ["t"]}, True),
        ("DAG acyclic", replay.opcode_dag,
         {"graph": {"A": [], "B": ["A"]}, "authority": _S}, True),
        ("DAG cycle", replay.opcode_dag,
         {"graph": {"A": ["B"], "B": ["A"]}, "authority": _S}, False),
        ("DAG self-parenting", replay.opcode_dag,
         {"graph": {"A": ["A"]}, "authority": _S}, False),
        ("DAG missing parent", replay.opcode_dag,
         {"graph": {"A": ["Z"]}, "authority": _S}, False),
    ]
    for label, fn, args, want in op_cases:
        try:
            got = fn(args, "selfcheck")["success"]
        except Exception as exc:                  # noqa: BLE001 - fail closed
            faults += fail("opcode %s: %s" % (label, exc))
            continue
        if got is not want:
            faults += fail("opcode %s: got %s want %s" % (label, got, want))
        else:
            sys.stdout.write("opcode replay        : %s\n" % label)
    for label, args in (("non-sentinel authority",
                         {"graph": {}, "authority": "OTHER"}),
                        ("mask on non-object operands",
                         {"left": "a", "right": "a", "mask": ["x"]})):
        fn = replay.opcode_dag if "authority" in args else replay.opcode_compare
        try:
            fn(args, "selfcheck")
            faults += fail("opcode %s: accepted" % label)
        except canonical_json.VerifierFault:
            sys.stdout.write("opcode replay        : refuses %s\n" % label)
    try:
        replay.recompute_results(
            [{"opcode": "KERNEL", "result_name": "r_k", "args": {}}],
            "selfcheck")
        faults += fail("unimplemented opcode silently accepted")
    except canonical_json.VerifierFault:
        sys.stdout.write("opcode replay        : refuses unimplemented opcode\n")

    # V008-R9-1: the P0 atom consumes the COMPUTED object; an uncomputed P0
    # is a build fault, never a criterion FAIL.
    _nop0 = canonical_json.encode_canonical({"r_dag": {"success": True}})
    _b = replay.EvidenceBundle(_nop0, hashlib.sha256(_nop0).hexdigest(), "sc")
    try:
        replay.replay_atom("P0", _b)
        faults += fail("uncomputed P0 did not fault")
    except canonical_json.VerifierFault:
        sys.stdout.write("P0 atom              : uncomputed P0 faults, never "
                         "returns False\n")
    _yes = canonical_json.encode_canonical({"P0": {"success": True}})
    _no = canonical_json.encode_canonical({"P0": {"success": False}})
    got = (replay.replay_atom("P0", replay.EvidenceBundle(
               _yes, hashlib.sha256(_yes).hexdigest(), "sc")),
           replay.replay_atom("P0", replay.EvidenceBundle(
               _no, hashlib.sha256(_no).hexdigest(), "sc")))
    if got != (True, False):
        faults += fail("P0 atom does not track the computed value: %s" % (got,))
    else:
        sys.stdout.write("P0 atom              : tracks the computed value\n")

    # V008-R9-1/3: P0's THREE outcomes, and they are three
    from verifier import preconditions as _pc
    _sm = {"schema": "rd22.subject-lineage-manifest.v001",
           "declared_root": None,
           "files": [{"relative_path": "a", "byte_length": 1,
                      "sha256": hashlib.sha256(b"a").hexdigest()}]}
    _sm["declared_root"] = hashing.content_root(
        [("a", 1, _sm["files"][0]["sha256"])])
    _em = {"declared_root": None, "payload_inventory":
           [{"relative_path": "b", "byte_length": 1,
             "sha256": hashlib.sha256(b"b").hexdigest()}]}
    _em["declared_root"] = hashing.content_root(
        [("b", 1, _em["payload_inventory"][0]["sha256"])])
    # V009-J3: digest -> LIST of (payload_path, bytes); "exactly one" is a rule
    _idx = {hashlib.sha256(b"a").hexdigest(): [("pa", b"a")],
            hashlib.sha256(b"b").hexdigest(): [("pb", b"b")]}
    try:
        _v = _pc.compute_p0(_sm, _em, _idx, "sc")
        if _v["success"] is not True or len(_v["conjuncts"]) != 6:
            faults += fail("P0 true case: %s" % _v)
        else:
            sys.stdout.write("P0 compute           : all six conjuncts true\n")
    except Exception as exc:                      # noqa: BLE001 - fail closed
        faults += fail("P0 true case: %s" % exc)
    _bad = {"schema": _sm["schema"], "declared_root": "0" * 64,
            "files": list(_sm["files"])}
    try:
        _v = _pc.compute_p0(_bad, _em, _idx, "sc")
        if _v["success"] is not False:
            faults += fail("P0 false case did not go false")
        else:
            sys.stdout.write("P0 compute           : a false conjunct gives "
                             "P0=false, not a refusal\n")
    except Exception as exc:                      # noqa: BLE001 - fail closed
        faults += fail("P0 false case: %s" % exc)
    try:
        _pc.compute_p0(_sm, _em, {}, "sc")
        faults += fail("unsupplied bytes did not refuse")
    except _pc.PreconditionNotReplayable as exc:
        v = exc.value
        ok = (sorted(v) == sorted(contracts.PRECONDITION_REFUSAL_FIELDS)
              and v["status"] == contracts.PRECONDITION_NOT_REPLAYABLE
              and v["criterion_evaluated"] is False and v["missing_carrier"])
        if not ok:
            faults += fail("refusal value malformed: %s" % v)
        else:
            sys.stdout.write("P0 compute           : unevaluable -> closed "
                             "PRECONDITION_NOT_REPLAYABLE naming the carrier\n")

    # V009-J3: exactly one payload per subject row, and the closed record
    _dup = dict(_idx)
    _dup[hashlib.sha256(b"a").hexdigest()] = [("pa", b"a"), ("pa2", b"a")]
    try:
        _pc.compute_p0(_sm, _em, _dup, "sc")
        faults += fail("J3: two payloads for one subject row accepted")
    except _pc.PreconditionNotReplayable as exc:
        if "exactly one" not in exc.value["missing_carrier"]:
            faults += fail("J3 refusal does not name the rule: %s" % exc.value)
        else:
            sys.stdout.write("V009 J3              : two payloads for one "
                             "subject row -> refusal naming the rule\n")
    _res = _pc.compute_p0(_sm, _em, _idx, "sc")["subject_resolutions"]
    if len(_res) != 1 or sorted(_res[0]) != sorted(
            contracts.SUBJECT_RESOLUTION_FIELDS):
        faults += fail("J3 resolution record malformed: %s" % _res)
    else:
        sys.stdout.write("V009 J3              : one closed 5-field resolution "
                         "record per subject row\n")

    # V009-J4: membership is instance data; the root derives from it
    _r = child_manifest.root_member_rows(ROOT)
    if contracts.root_from_members(_r) != child_manifest.package_root_digest(ROOT):
        faults += fail("J4: root_from_members disagrees with package_root_digest")
    else:
        sys.stdout.write("V009 J4              : root = SHA256(concat(row.sha256)) "
                         "over %d sealed rows\n" % len(_r))
    for _label, _bad in (("unsorted", list(reversed(_r))),
                         ("empty", []),
                         ("duplicate path", _r + [_r[0]]),
                         ("absolute path",
                          [dict(_r[0], relative_path="/x")])):
        try:
            contracts.validate_root_members(_bad, "sc")
            faults += fail("J4: %s members accepted" % _label)
        except canonical_json.VerifierFault:
            sys.stdout.write("V009 J4              : refuses %s members\n"
                             % _label)
    try:
        child_manifest.build_manifest(
            "0" * 64, dict((f, "1" * 64) for f in contracts.INPUT_ROOTS_FIELDS),
            "o", "r", False, _r)
        faults += fail("J4: root not matching its members accepted")
    except canonical_json.VerifierFault:
        sys.stdout.write("V009 J4              : refuses a root that does not "
                         "derive from its members\n")

    # Launch inventories, verified against the SEALED GOVERNING SPEC bytes
    _spec = os.path.join(os.path.dirname(ROOT),
                         "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V009.md")
    if os.path.isfile(_spec):
        _t = open(_spec, encoding="utf-8").read()
        _decl = _re.search(r'"required":\[("evidence_manifest_sha256"[^\]]*)\]',
                           _t)
        _want = sorted(_re.findall(r'"([a-z_]+_sha256)"', _decl.group(1))) \
            if _decl else []
        if _want != sorted(contracts.INPUT_ROOTS_FIELDS):
            faults += fail("input_roots differ from the sealed schema: %s vs %s"
                           % (_want, sorted(contracts.INPUT_ROOTS_FIELDS)))
        else:
            sys.stdout.write("V009 inventories     : input_roots match the "
                             "sealed schema (7)\n")
        _mr = child_manifest.root_member_rows(ROOT)
        _m = child_manifest.build_manifest(
            contracts.root_from_members(_mr),
            dict((f, "1" * 64) for f in contracts.INPUT_ROOTS_FIELDS),
            "o", "r", False, _mr)
        if len(_m["argv"]) != 22:
            faults += fail("argv is %d items, sealed schema says 22"
                           % len(_m["argv"]))
        else:
            sys.stdout.write("V009 inventories     : argv is the sealed "
                             "22-item schema\n")

    # no load-bearing assert anywhere in the package
    hits = []
    for base, _dirs, files in os.walk(ROOT):
        for fname in files:
            if not fname.endswith(".py"):
                continue
            path = os.path.join(base, fname)
            with open(path, encoding="utf-8") as handle:
                for lineno, line in enumerate(handle, 1):
                    stripped = line.strip()
                    if stripped.startswith("assert ") or stripped == "assert":
                        hits.append("%s:%d" % (path, lineno))
    if hits:
        faults += fail("python assert found: %s" % hits)
    else:
        sys.stdout.write("assert scan          : 0 hits (B-V011-SP2-07)\n")

    # The census must be derivable from the sealed spec. The filename is a
    # LOOKUP HINT ONLY -- SpecCensus loads through load_addressed, so the
    # SPEC_SHA256 const is what admits the bytes. When the pin moved to V007
    # and this string still said V005 the self-check FAILED CLOSED on a
    # content-address mismatch rather than reading the wrong file, which is
    # how this fourth V005 reference was found: it was carried by NAME, so
    # grepping for the old digest could not see it.
    spec = os.path.join(os.path.dirname(ROOT),
                        "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V009.md")
    if os.path.isfile(spec):
        try:
            census = spec_census.SpecCensus(spec)
            s = census.summary()
            sys.stdout.write(
                "spec census          : %d ids (%d blocker + %d discrepancy), "
                "%s, board %s\n"
                % (s["total_ids"], s["blocker_ids"], s["discrepancy_ids"],
                   s["class_partition"], s["binding_board"]))
        except Exception as exc:                  # noqa: BLE001 - fail closed
            faults += fail("spec census: %s" % exc)
    else:
        sys.stdout.write("spec census          : spec not present here\n")

    sys.stdout.write("CHAIN_INVOKED        : false\n")
    sys.stdout.write("== %s ==\n" % ("SELF-CHECK CLEAN" if not faults
                                     else "SELF-CHECK FAULTS: %d" % faults))
    return 1 if faults else 0


if __name__ == "__main__":
    sys.exit(main())
