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
