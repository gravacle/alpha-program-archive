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
    if len(contracts.VERIFIER_MANIFEST_FIELDS) != 11:
        faults += fail("VERIFIER_MANIFEST_FIELDS: %d, addendum says 11"
                       % len(contracts.VERIFIER_MANIFEST_FIELDS))
    else:
        sys.stdout.write("VERIFIER_MANIFEST_FIELDS  : 11 fields\n")
    if len(contracts.EVENT_LEDGER_FIELDS) != 6:
        faults += fail("EVENT_LEDGER_FIELDS: %d, addendum says 6"
                       % len(contracts.EVENT_LEDGER_FIELDS))
    else:
        sys.stdout.write("EVENT_LEDGER_FIELDS       : 6 digest carriers\n")

    # the launch manifest validates against its own closed contract
    from verifier import child_manifest
    try:
        m = child_manifest.build_manifest(
            "0" * 64,
            {"spec_sha256": "1" * 64, "ledger_sha256": "2" * 64,
             "evidence_root_sha256": "3" * 64,
             "runtime_snapshot_sha256": "4" * 64,
             "runtime_gate_sha256": "5" * 64},
            "out/verdict.json", "out/receipt.json", False)
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

    # the census must be derivable from the sealed spec
    spec = os.path.join(os.path.dirname(ROOT),
                        "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md")
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
