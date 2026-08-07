"""Runtime pin, trust records, and event reclassification.

Runtime pin authorized by RD-22 (DECISION_RD22_BUILD_AUTHORIZED_2026-08-07,
sha256 ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340):

    snapshot_sha256 = 50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb
    gate_sha256     = 2ad7f72a88184c11e1253f2c47598fca11e60d05e8e71a26db4e19b16bf98d42
    trust_root      = extracted from the pinned snapshot at R0 and displayed

The v014 substitution is expressly NOT authorized. A trust-root mismatch stops
the run; the pin is re-ruled with the fact displayed.
"""

from .canonical_json import VerifierFault, loads_strict, require_exact_fields
from .hashing import load_addressed, require_sha256, sha256_bytes

AUTHORIZED_SNAPSHOT_SHA256 = (
    "50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb")
AUTHORIZED_GATE_SHA256 = (
    "2ad7f72a88184c11e1253f2c47598fca11e60d05e8e71a26db4e19b16bf98d42")
UNAUTHORIZED_SNAPSHOT_SHA256 = (
    "fb74b7566b5c7ae8da64096754b16570dc613c8afdd140abd7a0100d5fcc1a08")  # v014

RUNTIME_SUBJECT_FIELDS = ("snapshot_sha256", "gate_sha256", "trust_root")

# Integration addendum §1.3 (OWED CHANGE 1): the child row carries DIGESTS,
# not ledger objects. The pre-conformance code indexed objects named
# `module_ledger` etc.; the sealed child-row pattern is `<class>_ledger_sha256`.
# The spec won over the adapter's convenience.
from .contracts import EVENT_LEDGER_FIELDS

# Canonical digest of the empty event list. Addendum §1.3: a class with no
# events carries THIS, never null and never an omitted field, so that
# "no events occurred" and "events were not recorded" stay distinguishable.
EMPTY_LEDGER_SHA256 = sha256_bytes(b"[]")


def load_runtime_subject(snapshot_path, gate_path):
    """Admit the pinned runtime and extract the trust root from it (R0)."""
    snapshot_bytes = load_addressed(
        snapshot_path, AUTHORIZED_SNAPSHOT_SHA256, "runtime snapshot v012")
    load_addressed(gate_path, AUTHORIZED_GATE_SHA256, "runtime gate v010")

    try:
        snapshot = loads_strict(snapshot_bytes.decode("utf-8"))
    except UnicodeDecodeError as exc:
        raise VerifierFault("runtime snapshot not UTF-8: %s" % exc)
    if not isinstance(snapshot, dict):
        raise VerifierFault("runtime snapshot must be a JSON object")

    trust_root = snapshot.get("trust_root")
    if trust_root is None:
        raise VerifierFault(
            "runtime snapshot carries no trust_root; the pin cannot be "
            "completed and the run must stop for a principal re-ruling")
    require_sha256(trust_root, "trust_root")

    return {
        "snapshot_sha256": AUTHORIZED_SNAPSHOT_SHA256,
        "gate_sha256": AUTHORIZED_GATE_SHA256,
        "trust_root": trust_root,
    }


def validate_runtime_subject(subject, where):
    require_exact_fields(subject, RUNTIME_SUBJECT_FIELDS, where)
    if subject["snapshot_sha256"] == UNAUTHORIZED_SNAPSHOT_SHA256:
        raise VerifierFault(
            "%s: runtime v014 substituted; expressly NOT authorized by RD-22"
            % where)
    if subject["snapshot_sha256"] != AUTHORIZED_SNAPSHOT_SHA256:
        raise VerifierFault(
            "%s: snapshot %s is not the authorized pin %s"
            % (where, subject["snapshot_sha256"], AUTHORIZED_SNAPSHOT_SHA256))
    if subject["gate_sha256"] != AUTHORIZED_GATE_SHA256:
        raise VerifierFault(
            "%s: gate %s is not the authorized pin %s"
            % (where, subject["gate_sha256"], AUTHORIZED_GATE_SHA256))
    require_sha256(subject["trust_root"], "%s.trust_root" % where)
    return subject


def revalidate_trust_snapshots(snapshots, authorized_trust_root, where):
    """Require T4 = T3 = T2 = T1 = T0 = authorized_trust_root (spec R9/R10)."""
    if not isinstance(snapshots, dict):
        raise VerifierFault("%s: trust_snapshots must be an object" % where)
    expected_labels = ("T0", "T1", "T2", "T3", "T4")
    require_exact_fields(snapshots, expected_labels, where)
    drifted = []
    for label in expected_labels:
        value = snapshots[label]
        require_sha256(value, "%s.%s" % (where, label))
        if value != authorized_trust_root:
            drifted.append(label)
    if drifted:
        raise VerifierFault(
            "%s: trust drift at %s; run stops fail-closed"
            % (where, ",".join(drifted)))
    return True


def reclassify_events(child_row, evidence_dir, where, loader):
    """Reclassify all six event classes from the child row's OWN digests.

    Addendum §1.3. Each carrier names a content-addressed ledger; the verifier
    fetches it by that digest, recomputes the canonical digest of the event
    list, and compares. The producer's labels are recomputed, never accepted.

    `loader(path, digest, where)` is injected so this stays testable without a
    live filesystem; it must fail closed on mismatch.
    """
    from .canonical_json import encode_canonical, loads_strict

    out = {}
    for field in EVENT_LEDGER_FIELDS:
        if field not in child_row:
            raise VerifierFault("%s: missing event carrier %r" % (where, field))
        digest = child_row[field]
        require_sha256(digest, "%s.%s" % (where, field))

        if digest == EMPTY_LEDGER_SHA256:
            out[field] = {"sha256": digest, "event_count": 0,
                          "note": "declared-empty"}
            continue

        blob = loader("%s/%s.json" % (evidence_dir.rstrip("/"), digest),
                      digest, "%s.%s" % (where, field))
        events = loads_strict(blob.decode("utf-8"))
        if not isinstance(events, list):
            raise VerifierFault(
                "%s.%s: ledger is not a list" % (where, field))
        recomputed = sha256_bytes(encode_canonical(events))
        if recomputed != digest:
            raise VerifierFault(
                "%s.%s: canonical digest %s != declared %s"
                % (where, field, recomputed, digest))
        out[field] = {"sha256": recomputed, "event_count": len(events)}
    return out
