"""R9 — the independent verifier child. Builder B entry point.

Invoked by Custodian C, never by Builder B. Emits a canonical-JSON verdict on
stdout and exits non-zero on any fault (fail-closed).

Independence attestation: this package imports nothing from the producer. Its
expectations are derived from the sealed specification bytes (spec_census),
from the sealed output contracts (contracts), and from the RD-22 runtime pin.
"""

import argparse
import os
import sys

from .canonical_json import (VerifierFault, dumps_canonical, encode_canonical,
                             loads_strict)
from .contracts import (validate_authority_firewall, validate_check_row,
                        validate_child_row, validate_fixture_row,
                        validate_ledger_shape)
from .comparison import (check_authorization, check_gate_discipline,
                         compare_semantic_outputs)
from .hashing import (load_addressed, read_bytes, require_sha256,
                      sha256_bytes, sha256_file_unverified)
from .preconditions import (PreconditionNotReplayable, compute_p0,
                            load_manifest)
from .ground_atoms import GroundAtomRefusal
from .replay import (EvidenceBundle, classify_payloads,
                     recompute_results, replay_fixture, replay_predicate)
from .runtime_state import (CONTEXT_VERIFIER_INPUT, reclassify_events,
                            revalidate_trust_snapshots,
                            validate_runtime_subject)
from .spec_census import SPEC_SHA256, SpecCensus

VERIFIER_SCHEMA = "gravacle.a35.verifier-verdict.v1"
RD22_AUTHORIZATION_SHA256 = (
    "ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340")

# RD-22 authorizes implementation and a structural run; nothing else may be true.
RD22_FIREWALL_TRUE_FIELDS = ("implemented", "executed")


def _fault(findings, code, detail):
    findings.append({"code": code, "detail": detail})


def _load_all_payloads(evidence_dir, digests, where):
    """Digest-verify EVERY payload the row observes, whatever its role.

    The pre-change code admitted `digests[0]` and never looked at the rest:
    it was simultaneously too strict (it demanded the one it happened to pick
    parse as an object) and too lax (it left the others unverified). Roles
    change what is parsed; they never change what is digest-verified.
    """
    return [(d, load_addressed("%s/%s.json" % (evidence_dir.rstrip("/"), d),
                               d, "%s payload %s" % (where, d)))
            for d in digests]


def _index_evidence(evidence_dir):
    """sha256 -> bytes for every file R9 was actually supplied.

    Content-addressed by construction: the key is the OBSERVED digest of the
    bytes, never a declared one, so a mislabelled file indexes under its true
    digest and simply fails to satisfy any declaration.
    """
    index = {}
    for name in sorted(os.listdir(evidence_dir)):
        path = os.path.join(evidence_dir, name)
        if not os.path.isfile(path):
            continue
        blob = read_bytes(path)
        # A LIST, not a single value: V009-J3 requires EXACTLY ONE payload per
        # subject row, and a dict keyed by digest would silently collapse two
        # copies into one and hide the ambiguity it exists to catch.
        index.setdefault(sha256_bytes(blob), []).append((name, blob))
    return index


def _recorded_invocation(row):
    """The row's recorded invocation(s), or None.

    OWED CHANGE DISCHARGED (relay 690). Builder B specified this field at 686
    because roles and byte-span linkage are not derivable without it; Builder A
    emitted it at 687; the row contract now declares and TYPES it (15 fields).
    Rows with nothing to record carry null, and role derivation falls back to
    parse admissibility exactly as before -- the fallback was not removed, it
    stopped being the only path.
    """
    return row.get("invocation")


def verify(spec_path, ledger_path, ledger_sha256, evidence_dir,
           snapshot_path, gate_path, subject_manifest_path,
           subject_manifest_sha256, evidence_manifest_path,
           evidence_manifest_sha256):
    """Run the R9 duties. Returns (verdict_dict, ok_boolean)."""
    findings = []

    # --- independently derive every expectation from the sealed spec --------
    census = SpecCensus(spec_path, SPEC_SHA256)

    # --- admit the producer ledger by content address ----------------------
    ledger_bytes = load_addressed(ledger_path, ledger_sha256, "producer ledger")
    ledger = loads_strict(ledger_bytes.decode("utf-8"))
    validate_ledger_shape(ledger)

    # --- V008-R9-1: R9 computes P0 itself, before any criterion -----------
    subject_manifest = load_manifest(subject_manifest_path,
                                     subject_manifest_sha256,
                                     "subject manifest")
    evidence_manifest = load_manifest(evidence_manifest_path,
                                      evidence_manifest_sha256,
                                      "evidence manifest")
    evidence_index = _index_evidence(evidence_dir)
    p0_value, p0_refusal = None, None
    try:
        p0_value = compute_p0(subject_manifest, evidence_manifest,
                              evidence_index, "P0")
    except PreconditionNotReplayable as exc:
        p0_refusal = exc.value
        _fault(findings, "PRECONDITION", exc.value)

    if ledger.get("spec_sha256") != SPEC_SHA256:
        _fault(findings, "SPEC_BINDING",
               "ledger spec_sha256 %r is not the governing spec"
               % ledger.get("spec_sha256"))

    # --- runtime pin and trust --------------------------------------------
    subject = validate_runtime_subject(ledger["runtime_subject"],
                                       "runtime_subject")
    # Q-601: the verifier's own input ledger carries T0-T3 exactly. A T4 here
    # is a post-verifier snapshot attested before the verifier ran.
    revalidate_trust_snapshots(ledger["trust_snapshots"],
                               subject["trust_root"], "trust_snapshots",
                               context=CONTEXT_VERIFIER_INPUT)

    # --- authorization and firewall ---------------------------------------
    check_authorization(ledger["authorization"], RD22_AUTHORIZATION_SHA256,
                        "authorization")
    validate_authority_firewall(ledger["authority_firewall"],
                                RD22_FIREWALL_TRUE_FIELDS, "authority_firewall")

    # --- children: receipts are never authoritative ------------------------
    children = ledger["children"]
    if not isinstance(children, list):
        raise VerifierFault("children must be a list")
    for i, child in enumerate(children):
        validate_child_row(child, "children[%d]" % i)
        # D7 / addendum §1.3: all SIX event classes are reclassified from the
        # child's own declared digests. Previously only three were reachable.
        try:
            reclassify_events(child, evidence_dir, "children[%d]" % i,
                              load_addressed)
        except VerifierFault as exc:
            _fault(findings, "EVENT_LEDGER", str(exc))

    # --- the check census --------------------------------------------------
    rows = ledger["checks"]
    if not isinstance(rows, list):
        raise VerifierFault("checks must be a list")

    seen_ids = []
    for i, row in enumerate(rows):
        validate_check_row(row, "checks[%d]" % i)
        seen_ids.append(row["check_id"])

    expected_ids = census.check_ids()
    if sorted(seen_ids) != expected_ids:
        missing = sorted(set(expected_ids) - set(seen_ids))
        extra = sorted(set(seen_ids) - set(expected_ids))
        _fault(findings, "CENSUS",
               "check universe mismatch (missing=%s undeclared=%s)"
               % (missing, extra))
    if len(seen_ids) != len(set(seen_ids)):
        _fault(findings, "CENSUS", "duplicate check_id rows")

    # --- class partition and descriptor binding ----------------------------
    for row in rows:
        cid = row["check_id"]
        if cid not in census.descriptors:
            continue
        expected_class = census.execution_class(cid)
        if row["execution_class"] != expected_class:
            _fault(findings, "CLASS",
                   "%s: class %r, spec says %r"
                   % (cid, row["execution_class"], expected_class))
        expected_digest = census.check_spec_sha256(cid)
        if row["check_spec_sha256"] != expected_digest:
            _fault(findings, "DESCRIPTOR_DIGEST",
                   "%s: check_spec_sha256 %s does not match the sealed "
                   "descriptor row digest %s"
                   % (cid, row["check_spec_sha256"], expected_digest))

    # --- gate discipline ---------------------------------------------------
    for violation in check_gate_discipline(rows, census.gated_ids(), "checks"):
        _fault(findings, "GATE", violation)

    # --- replay each PASS predicate from evidence bytes --------------------
    replayed = []
    for row in rows:
        cid = row["check_id"]
        if row["execution_class"] == "GATED-EXECUTION":
            replayed.append({"check_id": cid, "replayed": False,
                             "status": row["status"],
                             "note": "NOT_RUN_GATE by construction"})
            continue
        digests = row["observed_evidence_sha256s"]
        if not isinstance(digests, list) or not digests:
            _fault(findings, "EVIDENCE",
                   "%s: no observed evidence digests" % cid)
            continue
        try:
            payloads = _load_all_payloads(evidence_dir, digests,
                                          "%s evidence" % cid)
            roles = classify_payloads(payloads, _recorded_invocation(row), cid)
            for detail in roles["faults"]:
                _fault(findings, "PAYLOAD_ROLE", detail)
            if roles["faults"]:
                raise VerifierFault(roles["faults"][0])
            digest, blob, _ = roles["consumable"][0]
            # R9 replays FROM EVIDENCE BYTES (spec V010 R9). The bundle is
            # built from RECOMPUTED opcode results, not from producer-emitted
            # ones: reading .success off a producer object would let a
            # producer-declared object carry the criterion's direction.
            recorded = _recorded_invocation(row)
            invocations = recorded if isinstance(recorded, list) else (
                [recorded] if recorded else [])
            results = recompute_results(
                invocations, cid,
                descriptor_row=census.descriptor_row(cid),
                criterion=row["expected_predicate"].strip("`"),
                evidence_table=(p0_value or {}).get("evidence_files"),
                evidence_index=evidence_index)
            for _d, _b, _parsed in roles["consumable"]:
                if "P0" in _parsed:
                    raise VerifierFault(
                        "%s: a producer-emitted P0 result object is a contract "
                        "fault and is never an input (V008-R9-1)" % cid)
            if p0_refusal is not None:
                replayed.append({"check_id": cid, "replayed": False,
                                 "status": p0_refusal["status"],
                                 "note": p0_refusal["missing_carrier"]})
                continue
            results["P0"] = p0_value
            bundle = EvidenceBundle(
                encode_canonical(results), sha256_bytes(encode_canonical(results)),
                cid)
            recomputed = replay_predicate(row["expected_predicate"], bundle)
        except GroundAtomRefusal as exc:
            # V010-M1 + V008-R9-3: neither carried nor qualifying. A refusal,
            # never a criterion FAIL -- the atom was not evaluated.
            _fault(findings, "GROUND_ATOM", {"check_id": cid,
                                             "result_name": exc.result_name,
                                             "reason": exc.reason})
            replayed.append({"check_id": cid, "replayed": False,
                             "status": "PRECONDITION_NOT_REPLAYABLE",
                             "note": exc.reason})
            continue
        except VerifierFault as exc:
            _fault(findings, "REPLAY", "%s: %s" % (cid, exc))
            replayed.append({"check_id": cid, "replayed": False,
                             "status": "ERROR", "note": str(exc)})
            continue
        claimed = row["status"] == "PASS"
        if recomputed != claimed:
            _fault(findings, "REPLAY_DISAGREE",
                   "%s: producer says %s, independent replay says %s"
                   % (cid, row["status"], "PASS" if recomputed else "FAIL"))
        replayed.append({"check_id": cid, "replayed": True,
                         "status": "PASS" if recomputed else "FAIL",
                         "note": ""})

    # --- fixtures: quarantine + named-record replay (D8) --------------------
    fixture_rows = ledger["fixtures"]
    if not isinstance(fixture_rows, list):
        raise VerifierFault("fixtures must be a list")
    fixtures_replayed = []
    for i, fixture in enumerate(fixture_rows):
        where = "fixtures[%d]" % i
        try:
            validate_fixture_row(fixture, where)
        except VerifierFault as exc:
            _fault(findings, "FIXTURE_CONTRACT", str(exc))
            continue
        if fixture["execution_class"] == "GATED-EXECUTION":
            if fixture["status"] != "NOT_RUN_GATE":
                _fault(findings, "GATE",
                       "%s: gated fixture status %r; RD-22 authorizes the "
                       "structural run only" % (where, fixture["status"]))
            fixtures_replayed.append({"fixture_id": fixture["fixture_id"],
                                      "replayed": False,
                                      "note": "NOT_RUN_GATE by construction"})
            continue
        digests = fixture["observed_evidence_sha256s"]
        if not isinstance(digests, list) or not digests:
            _fault(findings, "FIXTURE_EVIDENCE",
                   "%s: no observed evidence digests" % where)
            continue
        try:
            payloads = _load_all_payloads(evidence_dir, digests,
                                          "%s evidence" % where)
            roles = classify_payloads(payloads, _recorded_invocation(fixture),
                                      where)
            for detail in roles["faults"]:
                _fault(findings, "PAYLOAD_ROLE", detail)
            if roles["faults"]:
                raise VerifierFault(roles["faults"][0])
            digest, blob, _ = roles["consumable"][0]
            bundle = EvidenceBundle(blob, digest, fixture["fixture_id"])
            outcome = replay_fixture(fixture, bundle)
        except VerifierFault as exc:
            _fault(findings, "FIXTURE_REPLAY", "%s: %s" % (where, exc))
            continue
        if not outcome["match"]:
            _fault(findings, "FIXTURE_DISAGREE", outcome)
        fixtures_replayed.append(outcome)

    # --- normal vs optimized, common member only ---------------------------
    comparison = ledger["producer_comparison"]
    if not isinstance(comparison, dict):
        raise VerifierFault("producer_comparison must be an object")
    normal_rows = comparison.get("normal", [])
    optimized_rows = comparison.get("optimized", [])
    comparison_result = compare_semantic_outputs(normal_rows, optimized_rows)
    if not comparison_result["agree"]:
        _fault(findings, "NORMAL_OPT_DISAGREE", comparison_result)

    # --- verdict -----------------------------------------------------------
    ok = not findings
    verdict = {
        "schema": VERIFIER_SCHEMA,
        "spec_sha256": SPEC_SHA256,
        "verifier_sha256": _self_digest(),
        "runtime_subject": subject,
        "authorization_sha256": RD22_AUTHORIZATION_SHA256,
        "census": census.summary(),
        "checks_replayed": replayed,
        "fixtures_replayed": fixtures_replayed,
        "producer_comparison": comparison_result,
        "findings": findings,
        "independence": {
            "producer_code_imported": False,
            "expectations_source": "sealed specification bytes",
        },
        "authority_firewall": dict(ledger["authority_firewall"]),
        "verdict": "VERIFIED" if ok else "FAIL",
    }
    verdict["terminal_content_sha256"] = sha256_bytes(
        encode_canonical({k: v for k, v in verdict.items()
                          if k != "terminal_content_sha256"}))
    return verdict, ok


def _self_digest():
    """The package's load-bearing root, launcher included.

    Delegates to child_manifest.package_root_digest so the manifest and the
    verdict can never disagree about what the root covers.
    """
    import os
    from .child_manifest import package_root_digest
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return package_root_digest(base)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="A35 independent verifier (Builder B, spec V005 R9)")
    parser.add_argument("--spec", required=True)
    parser.add_argument("--ledger", required=True)
    parser.add_argument("--ledger-sha256", required=True)
    parser.add_argument("--evidence-dir", required=True)
    parser.add_argument("--subject-manifest", required=True)
    parser.add_argument("--subject-manifest-sha256", required=True)
    parser.add_argument("--evidence-manifest", required=True)
    parser.add_argument("--evidence-manifest-sha256", required=True)
    parser.add_argument("--runtime-snapshot", required=True)
    parser.add_argument("--runtime-gate", required=True)
    args = parser.parse_args(argv)

    try:
        verdict, ok = verify(args.spec, args.ledger, args.ledger_sha256,
                             args.evidence_dir, args.runtime_snapshot,
                             args.runtime_gate, args.subject_manifest,
                             args.subject_manifest_sha256,
                             args.evidence_manifest,
                             args.evidence_manifest_sha256)
    except VerifierFault as exc:
        # D9 / addendum §3.3 clause 2: stdout carries the verdict and nothing
        # else. Diagnostics go to stderr. Exit 2 (could not start) and exit 1
        # (ran, found faults) are different facts and must not be conflated.
        sys.stderr.write("fail-closed: %s\n" % exc)
        # Q-594 canon: stdout carries ONE tight canonical JSON value and
        # nothing else -- no trailing newline. "No insignificant whitespace"
        # governs the stream exactly as it governs the file.
        sys.stdout.write(dumps_canonical({
            "schema": VERIFIER_SCHEMA,
            "verdict": "FAIL",
            "fault": str(exc),
        }))
        return 2

    sys.stdout.write(dumps_canonical(verdict))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
