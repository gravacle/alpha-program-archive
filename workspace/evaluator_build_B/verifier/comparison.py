"""Normal vs optimized semantic comparison, and authorization/gate discipline.

Spec V005 §12.5 — R9_QUANTIFICATION = COMMON_MEMBER_ONLY. Results are compared
only at the same common_member_key. The verifier does not compare different
`c`, `tau`, statistics, evolution, preparation, orientation-address, or
physical-branch members as if they were one, and selects no representative.
"""

from .canonical_json import VerifierFault, encode_canonical, require_exact_fields
from .contracts import COMMON_MEMBER_KEY_FIELDS, STATUS_ALPHABET
from .hashing import require_sha256, sha256_bytes


def common_member_key(row, where):
    """Build the §12.5 key. A missing component fails closed."""
    key = {}
    for field in COMMON_MEMBER_KEY_FIELDS:
        if field not in row:
            raise VerifierFault("%s: missing key component %r" % (where, field))
        key[field] = row[field]
    return sha256_bytes(encode_canonical(key))


def index_by_member(rows, where):
    index = {}
    for i, row in enumerate(rows):
        key = common_member_key(row, "%s[%d]" % (where, i))
        if key in index:
            raise VerifierFault(
                "%s[%d]: duplicate common_member_key" % (where, i))
        index[key] = row
    return index


def compare_semantic_outputs(normal_rows, optimized_rows):
    """Compare only at shared keys; report unmatched members, never merge them.

    An unmatched member is NOT quietly dropped: it is returned so the caller
    can fail closed. This is the R9 quantification lesson — a comparison that
    silently intersects is a comparison that can be satisfied by omission.
    """
    normal = index_by_member(normal_rows, "normal")
    optimized = index_by_member(optimized_rows, "optimized")

    shared = sorted(set(normal) & set(optimized))
    only_normal = sorted(set(normal) - set(optimized))
    only_optimized = sorted(set(optimized) - set(normal))

    mismatches = []
    for key in shared:
        a, b = normal[key], optimized[key]
        if a.get("status") != b.get("status"):
            mismatches.append({
                "common_member_key": key,
                "normal_status": a.get("status"),
                "optimized_status": b.get("status"),
            })
    return {
        "quantification": "COMMON_MEMBER_ONLY",
        "compared_members": len(shared),
        "only_in_normal": only_normal,
        "only_in_optimized": only_optimized,
        "status_mismatches": mismatches,
        "agree": (not mismatches and not only_normal and not only_optimized),
    }


def check_authorization(authorization, expected_sha256, where):
    """Bind the run to its content-addressed authorization artifact."""
    if not isinstance(authorization, dict):
        raise VerifierFault("%s: authorization must be an object" % where)
    for field in ("artifact_sha256", "scope"):
        if field not in authorization:
            raise VerifierFault("%s: missing %r" % (where, field))
    require_sha256(authorization["artifact_sha256"],
                   "%s.artifact_sha256" % where)
    if authorization["artifact_sha256"] != expected_sha256:
        raise VerifierFault(
            "%s: authorization %s is not the RD-22 artifact %s"
            % (where, authorization["artifact_sha256"], expected_sha256))
    return authorization


def check_gate_discipline(check_rows, gated_ids, where):
    """Gated rows must be NOT_RUN_GATE unless their gate is separately opened.

    RD-22 authorizes the FIRST STRUCTURAL RUN only: the 10 GATED-EXECUTION
    checks return NOT_RUN_GATE by construction. A gated row reporting PASS or
    FAIL is unauthorized gated execution and fails the run.
    """
    gated = set(gated_ids)
    violations = []
    gated_seen = 0
    for i, row in enumerate(check_rows):
        check_id = row.get("check_id")
        status = row.get("status")
        if status not in STATUS_ALPHABET:
            raise VerifierFault(
                "%s[%d]: status %r outside the closed alphabet"
                % (where, i, status))
        if check_id in gated:
            gated_seen += 1
            if status != "NOT_RUN_GATE":
                violations.append({
                    "check_id": check_id,
                    "status": status,
                    "reason": "unauthorized gated execution under RD-22",
                })
            if row.get("procedure_started") is True:
                violations.append({
                    "check_id": check_id,
                    "status": status,
                    "reason": "gated procedure started without an open gate",
                })
    if gated_seen != len(gated):
        raise VerifierFault(
            "%s: %d gated rows present, expected %d"
            % (where, gated_seen, len(gated)))
    return violations
