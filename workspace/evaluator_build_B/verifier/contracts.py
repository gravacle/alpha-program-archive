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
    "receipt_authoritative",
)

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
