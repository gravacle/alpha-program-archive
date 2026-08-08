"""Output contracts transcribed from the sealed spec V005 §9.4.

These are the EXACT field inventories. They are consumed as contracts, which
the RD-22 custody ruling expressly permits Builder B to read. No producer code
or receipt informs this module.
"""

import re

from .canonical_json import VerifierFault, require_exact_fields
from .replay import declared_opcodes

LEDGER_FIELDS = (
    "schema",
    "spec_sha256",
    "runner_sha256",
    "verifier_sha256",
    "runtime_subject",
    "authorization",
    "subject_lineage",
    "check_map_sha256",
    "fixture_manifest_sha256",
    "children",
    "trust_snapshots",
    "checks",
    "fixtures",
    "producer_comparison",
    "summary",
    "scope",
    "authority_firewall",
    "terminal_content_sha256",
)

CHECK_ROW_FIELDS = (
    "blocker_id",
    "source",
    "check_id",
    "check_spec_sha256",
    "execution_class",
    "input_root_sha256",
    "deterministic_procedure",
    "prerequisites",
    "required_gate",
    "expected_predicate",
    "procedure_started",
    "status",
    "observed_evidence_sha256s",
    "reason",
    # Added at relay 690. Builder B specified this field at 686 §2.3 because
    # payload roles and byte-span linkage are not derivable without it; Builder
    # A emitted it at 687; the exact inventory then refused it as undeclared.
    # Receiving one's own specification is part of specifying it.
    "invocation",
)

SOURCE_FIELDS = ("path", "sha256", "byte_span")

# The closed opcode set, read off the sealed spec's §2.2 table. FOURTEEN, not
# thirteen: `STRICT` is the only row written without a parenthesised operand,
# so a pattern that requires "(" silently drops it.
OPCODES = (
    "STRICT", "SCHEMA", "TYPE", "EXACT", "KERNEL", "ENUM", "DOMAIN", "UNITS",
    "DAG", "M2", "SYMBOLIC", "SPECTRAL", "COMPARE", "RUNTIME",
)

# One recorded invocation. SEVEN fields, transcribed from the SEALED SPEC's
# §9.4 row schema -- not from Builder B's 686 write-out, which named four and
# is superseded. V008 §9.4: "This is the byte-span linkage required for
# independent replay; the blocker-ledger source.byte_span and a digest without
# the source slice are not substitutes for it." Both builders were short of the
# spec here; the spec wins.
INVOCATION_FIELDS = ("opcode", "result_name", "args", "instance_id",
                     "source_sha256", "span", "span_sha256")

# `<symbol>@<source_sha256>:[start,end)` -- the grounding citation, encoded.
_INSTANCE_ID = re.compile(
    r"^([A-Za-z0-9_.\-]+)@([0-9a-f]{64}):\[(\d+),(\d+)\)$")
_RESULT_NAME = re.compile(r"^r_[A-Za-z0-9_]+$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")

CHILD_ROW_FIELDS = (
    "manifest_sha256",
    "target_sha256",
    "optimize",
    "output_sha256",
    "receipt_sha256",
    "runtime_before_sha256",
    "runtime_after_sha256",
    "module_ledger_sha256",
    "native_ledger_sha256",
    "open_event_ledger_sha256",
    "process_event_ledger_sha256",
    "network_event_ledger_sha256",
    "mutation_event_ledger_sha256",
    "receipt_authoritative",
)

# Integration addendum §1.3: the six event-ledger carriers on the child row.
# These are DIGESTS, not ledger objects. `runtime` is already carried by the
# runtime_before/after pair, which is why there are six and not seven.
EVENT_LEDGER_FIELDS = (
    "module_ledger_sha256",
    "native_ledger_sha256",
    "open_event_ledger_sha256",
    "process_event_ledger_sha256",
    "network_event_ledger_sha256",
    "mutation_event_ledger_sha256",
)

# Integration addendum §2.3: the exact fixtures[] row inventory.
FIXTURE_ROW_FIELDS = (
    "fixture_id",
    "source",
    "fixture_spec_sha256",
    "primary_check_ids",
    "execution_class",
    "input_root_sha256",
    "mutation_ids",
    "deterministic_procedure",
    "prerequisites",
    "required_gate",
    "expected_verdict_fields",
    "procedure_started",
    "status",
    "observed_verdict_fields",
    "observed_evidence_sha256s",
    "reason",
)

# Integration addendum §3.2: rd22.verifier-manifest.v001.
VERIFIER_MANIFEST_FIELDS = (
    "schema",
    "verifier_root_sha256",
    "entry_point",
    "argv",
    "optimize",
    "input_roots",
    "output_path",
    "receipt_path",
    "stdout_discipline",
    "exit_contract",
    "receipt_authoritative",
)
# V008-R9-2: seven, transcribed from the sealed input_roots schema and then
# VERIFIED against those bytes by the self-check (derivation, not typing).
INPUT_ROOTS_FIELDS = (
    "spec_sha256",
    "ledger_sha256",
    "evidence_root_sha256",
    "runtime_snapshot_sha256",
    "runtime_gate_sha256",
    "subject_manifest_sha256",
    "evidence_manifest_sha256",
)

# V008-R9-3: the closed precondition-refusal value. It is NOT a row status --
# §2.3's alphabet is still the closed four -- it is R9's refusal to evaluate.
PRECONDITION_REFUSAL_SCHEMA = "rd22.r9-precondition-refusal.v001"
PRECONDITION_NOT_REPLAYABLE = "PRECONDITION_NOT_REPLAYABLE"
PRECONDITION_REFUSAL_FIELDS = ("schema", "status", "criterion_evaluated",
                               "missing_carrier")

SUBJECT_MANIFEST_FIELDS = ("schema", "declared_root", "files")
MANIFEST_FILE_FIELDS = ("relative_path", "byte_length", "sha256")
STDOUT_DISCIPLINE_FIELDS = ("format", "lines", "other_output_permitted")
EXIT_CONTRACT_FIELDS = ("verified", "faults_found", "fail_closed")

VERIFIER_MANIFEST_SCHEMA = "rd22.verifier-manifest.v001"

# Addendum §3.2 requires all five input_roots to be 64-hex. Two of them --
# ledger_sha256 and evidence_root_sha256 -- are RUN-SCOPED: they are digests of
# the producer's outputs and cannot exist when the launch manifest is authored.
# The instance therefore carries this sentinel for them, and the verifier
# REFUSES it at run time. A placeholder that can pass unnoticed is worse than
# no placeholder; this one fails closed.
UNBOUND_ROOT_SENTINEL = "0" * 64
RUN_SCOPED_ROOTS = ("ledger_sha256", "evidence_root_sha256")

# Spec V005 §9.4: the specification-time authority firewall is exact.
AUTHORITY_FIREWALL_FIELDS = (
    "implemented",
    "executed",
    "authorization_claimed",
    "alpha_computed",
    "proof_authorized",
    "kappa_record_computed",
    "SPEC_SEAL",
    "CORE_RESULT_SEAL",
    "FINAL_CLAIM_SEAL",
)

# Fields that may never be true without a separate principal authorization
# naming them. RD-22 authorizes implementation and a structural run only.
FIREWALL_NEVER_TRUE_UNDER_RD22 = (
    "alpha_computed",
    "proof_authorized",
    "kappa_record_computed",
    "SPEC_SEAL",
    "CORE_RESULT_SEAL",
    "FINAL_CLAIM_SEAL",
)

STATUS_ALPHABET = ("PASS", "FAIL", "NOT_RUN_GATE", "ERROR")

# Spec V005 §12.5.
COMMON_MEMBER_KEY_FIELDS = (
    "subject_lineage_root",
    "check_id",
    "check_spec_sha256",
    "input_root_sha256",
    "fixture_id_or_null",
)


def validate_ledger_shape(ledger):
    require_exact_fields(ledger, LEDGER_FIELDS, "verdict ledger")
    return ledger


def parse_instance_id(value, where):
    """`<symbol>@<source_sha256>:[start,end)` -> dict, or None when null.

    The span is the byte-span linkage Builder B recorded as UNDELIVERED at 686:
    the raw grounding payload's length must equal `end - start`. Note the limit
    that remains -- the verifier still cannot RE-SLICE the source, because the
    source file is not a run input. Linkage is the payload's independently
    verified digest plus this declared arithmetic, not a re-derivation.
    """
    if value is None:
        return None
    if not isinstance(value, str):
        raise VerifierFault("%s: instance_id must be a string or null" % where)
    match = _INSTANCE_ID.match(value)
    if not match:
        raise VerifierFault(
            "%s: instance_id %r does not parse as "
            "<symbol>@<source_sha256>:[start,end)" % (where, value))
    symbol, source_sha256, start, end = match.groups()
    start, end = int(start), int(end)
    if end <= start:
        raise VerifierFault(
            "%s: instance_id span [%d,%d) is empty or inverted"
            % (where, start, end))
    return {"symbol": symbol, "source_sha256": source_sha256,
            "span": [start, end], "byte_length": end - start}


def validate_invocation(invocation, where):
    """Type one recorded invocation. Shape AND vocabulary, not mere presence."""
    require_exact_fields(invocation, INVOCATION_FIELDS, where)
    if invocation["opcode"] not in OPCODES:
        raise VerifierFault(
            "%s: opcode %r is outside the closed opcode set"
            % (where, invocation["opcode"]))
    name = invocation["result_name"]
    if not isinstance(name, str) or not _RESULT_NAME.match(name):
        raise VerifierFault(
            "%s: result_name %r is not an r_<name> result symbol"
            % (where, name))
    if not isinstance(invocation["args"], dict):
        raise VerifierFault("%s: args must be an object" % where)
    parsed = parse_instance_id(invocation["instance_id"],
                               "%s.instance_id" % where)
    span = invocation["span"]
    if parsed is None:
        if span is not None or invocation["source_sha256"] is not None \
                or invocation["span_sha256"] is not None:
            raise VerifierFault(
                "%s: instance_id is null but the linkage fields are not"
                % where)
        return invocation
    if (not isinstance(span, list) or len(span) != 2
            or span != parsed["span"]):
        raise VerifierFault(
            "%s: span %r does not agree with the instance_id span %r"
            % (where, span, parsed["span"]))
    if invocation["source_sha256"] != parsed["source_sha256"]:
        raise VerifierFault(
            "%s: source_sha256 does not agree with the instance_id source"
            % where)
    for field in ("source_sha256", "span_sha256"):
        value = invocation[field]
        if not isinstance(value, str) or not _SHA256.match(value):
            raise VerifierFault("%s: %s is not a lowercase sha256"
                                % (where, field))
    return invocation


def recorded_invocations(row, where):
    """Normalize and validate `row["invocation"]` -> list (possibly empty).

    Accepts null, one object, or a list of objects. The list form is not
    laxity: every element is validated identically, and a row whose descriptor
    declares several opcode assignments cannot record them all in the singular
    form Builder B wrote out at 686 -- a gap in that write-out, named at §2.2
    of the relay artifact rather than papered over.
    """
    value = row["invocation"]
    if value is None:
        return []
    items = value if isinstance(value, list) else [value]
    if not isinstance(value, (list, dict)):
        raise VerifierFault(
            "%s.invocation: must be null, an object, or a list of objects"
            % where)
    out = []
    for i, item in enumerate(items):
        out.append(validate_invocation(
            item, "%s.invocation[%d]" % (where, i)))
    return out


def validate_check_row(row, where):
    require_exact_fields(row, CHECK_ROW_FIELDS, where)
    require_exact_fields(row["source"], SOURCE_FIELDS, "%s.source" % where)
    if row["status"] not in STATUS_ALPHABET:
        raise VerifierFault(
            "%s: status %r outside the closed alphabet %s"
            % (where, row["status"], list(STATUS_ALPHABET)))
    invocations = recorded_invocations(row, where)
    # Cross-check against the SEALED DESCRIPTOR's own program. A recorded
    # invocation the descriptor does not declare is a fault: that direction is
    # an accusation, and a producer-declared object may accuse. The converse --
    # declared but not recorded -- is reported by the caller and NOT faulted
    # here, because Builder B's own 686 write-out specified a singular field
    # and it would be unjust to fault Builder A for conforming to it.
    declared = dict((n, op) for n, op in
                    declared_opcodes(row["deterministic_procedure"]))
    for i, inv in enumerate(invocations):
        name, opcode = inv["result_name"], inv["opcode"]
        if name not in declared:
            raise VerifierFault(
                "%s.invocation[%d]: result %r is not declared by the sealed "
                "descriptor's procedure" % (where, i, name))
        if declared[name] != opcode:
            raise VerifierFault(
                "%s.invocation[%d]: result %r is declared as %s, recorded as %s"
                % (where, i, name, declared[name], opcode))
    return row


def validate_child_row(row, where):
    require_exact_fields(row, CHILD_ROW_FIELDS, where)
    if row["receipt_authoritative"] is not False:
        raise VerifierFault(
            "%s: receipt_authoritative must be false (receipt promotion)"
            % where)
    return row


def validate_authority_firewall(firewall, authorized_true_fields, where):
    require_exact_fields(firewall, AUTHORITY_FIREWALL_FIELDS, where)
    allowed = set(authorized_true_fields or ())
    for field in AUTHORITY_FIREWALL_FIELDS:
        value = firewall[field]
        if value is not True and value is not False:
            raise VerifierFault("%s.%s: not a boolean" % (where, field))
        if value is True and field not in allowed:
            raise VerifierFault(
                "%s.%s is true without separate authorization" % (where, field))
    for field in FIREWALL_NEVER_TRUE_UNDER_RD22:
        if firewall[field] is True:
            raise VerifierFault(
                "%s.%s is true; RD-22 opens no physical gate" % (where, field))
    return firewall


def validate_fixture_row(row, where):
    """Integration addendum §2.3, with the two rules the inventory cannot carry.

    Rule 1 (quarantine): observed_verdict_fields may contain ONLY the names
    declared in expected_verdict_fields. An undeclared field is ERROR, not PASS
    -- this is spec §10's "no fixture output may populate a live physical-output
    field" made checkable rather than aspirational.

    Rule 2 (expectation direction) is enforced by the caller, which compares
    expected_verdict_fields against the SPEC-FIXED values in spec §10's table.
    """
    require_exact_fields(row, FIXTURE_ROW_FIELDS, where)
    require_exact_fields(row["source"], SOURCE_FIELDS, "%s.source" % where)
    if row["status"] not in STATUS_ALPHABET:
        raise VerifierFault(
            "%s: status %r outside the closed alphabet %s"
            % (where, row["status"], list(STATUS_ALPHABET)))

    expected = row["expected_verdict_fields"]
    observed = row["observed_verdict_fields"]
    if not isinstance(expected, dict):
        raise VerifierFault("%s.expected_verdict_fields: not an object" % where)
    if not isinstance(observed, dict):
        raise VerifierFault("%s.observed_verdict_fields: not an object" % where)

    undeclared = sorted(set(observed) - set(expected))
    if undeclared:
        raise VerifierFault(
            "%s: fixture quarantine breach -- observed fields %s are not "
            "declared in expected_verdict_fields" % (where, undeclared))
    return row


def validate_verifier_manifest(manifest, where):
    """Integration addendum §3.2: rd22.verifier-manifest.v001, closed."""
    require_exact_fields(manifest, VERIFIER_MANIFEST_FIELDS, where)
    if manifest["schema"] != VERIFIER_MANIFEST_SCHEMA:
        raise VerifierFault(
            "%s.schema: %r is not %r"
            % (where, manifest["schema"], VERIFIER_MANIFEST_SCHEMA))
    require_exact_fields(manifest["input_roots"], INPUT_ROOTS_FIELDS,
                         "%s.input_roots" % where)
    require_exact_fields(manifest["stdout_discipline"],
                         STDOUT_DISCIPLINE_FIELDS,
                         "%s.stdout_discipline" % where)
    require_exact_fields(manifest["exit_contract"], EXIT_CONTRACT_FIELDS,
                         "%s.exit_contract" % where)

    discipline = manifest["stdout_discipline"]
    if discipline["format"] != "canonical-json":
        raise VerifierFault("%s.stdout_discipline.format" % where)
    if discipline["lines"] != 1:
        raise VerifierFault("%s.stdout_discipline.lines must be 1" % where)
    if discipline["other_output_permitted"] is not False:
        raise VerifierFault(
            "%s: stdout must carry the verdict and nothing else" % where)

    contract = manifest["exit_contract"]
    if (contract["verified"], contract["faults_found"],
            contract["fail_closed"]) != (0, 1, 2):
        raise VerifierFault(
            "%s.exit_contract: exit 1 (faults found) and exit 2 (fail-closed) "
            "are different facts and must not be conflated" % where)

    if manifest["optimize"] is not True and manifest["optimize"] is not False:
        raise VerifierFault("%s.optimize must be declared as a boolean" % where)
    if manifest["receipt_authoritative"] is not False:
        raise VerifierFault(
            "%s.receipt_authoritative must be false" % where)
    return manifest


def require_roots_bound(manifest, where):
    """Refuse the unbound sentinel at run time (fail-closed placeholder).

    The launch manifest may be authored with RUN_SCOPED_ROOTS unbound. The
    parent MUST rebind them before invoking. If it does not, the verifier stops
    here rather than proceeding against a zero digest.
    """
    roots = manifest["input_roots"]
    unbound = [f for f in INPUT_ROOTS_FIELDS
               if roots.get(f) == UNBOUND_ROOT_SENTINEL]
    if unbound:
        raise VerifierFault(
            "%s: input roots %s are still the UNBOUND sentinel; the parent must "
            "bind the run-scoped roots before launch" % (where, sorted(unbound)))
    return manifest
