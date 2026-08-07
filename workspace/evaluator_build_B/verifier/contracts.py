"""Output contracts transcribed from the sealed spec V005 §9.4.

These are the EXACT field inventories. They are consumed as contracts, which
the RD-22 custody ruling expressly permits Builder B to read. No producer code
or receipt informs this module.
"""

from .canonical_json import VerifierFault, require_exact_fields

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
)

SOURCE_FIELDS = ("path", "sha256", "byte_span")

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
INPUT_ROOTS_FIELDS = (
    "spec_sha256",
    "ledger_sha256",
    "evidence_root_sha256",
    "runtime_snapshot_sha256",
    "runtime_gate_sha256",
)
STDOUT_DISCIPLINE_FIELDS = ("format", "lines", "other_output_permitted")
EXIT_CONTRACT_FIELDS = ("verified", "faults_found", "fail_closed")

VERIFIER_MANIFEST_SCHEMA = "rd22.verifier-manifest.v001"

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


def validate_check_row(row, where):
    require_exact_fields(row, CHECK_ROW_FIELDS, where)
    require_exact_fields(row["source"], SOURCE_FIELDS, "%s.source" % where)
    if row["status"] not in STATUS_ALPHABET:
        raise VerifierFault(
            "%s: status %r outside the closed alphabet %s"
            % (where, row["status"], list(STATUS_ALPHABET)))
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
