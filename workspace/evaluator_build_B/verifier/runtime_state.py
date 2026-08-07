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

EVENT_LEDGERS = (
    "module_ledger",
    "native_ledger",
    "open_event_ledger",
    "process_event_ledger",
    "network_event_ledger",
    "mutation_event_ledger",
)


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


def reclassify_events(ledgers, where):
    """Recompute each event ledger's digest and summarise its classification.

    The verifier reclassifies rather than accepting the producer's labels: a
    ledger is admitted only when its recomputed digest matches its declared
    one, and any event class outside the closed set fails closed.
    """
    if not isinstance(ledgers, dict):
        raise VerifierFault("%s: event ledgers must be an object" % where)
    require_exact_fields(ledgers, EVENT_LEDGERS, where)

    from .canonical_json import encode_canonical
    out = {}
    for name in EVENT_LEDGERS:
        ledger = ledgers[name]
        if not isinstance(ledger, dict):
            raise VerifierFault("%s.%s: not an object" % (where, name))
        for field in ("declared_sha256", "events"):
            if field not in ledger:
                raise VerifierFault(
                    "%s.%s: missing %r" % (where, name, field))
        events = ledger["events"]
        if not isinstance(events, list):
            raise VerifierFault("%s.%s.events: not a list" % (where, name))
        recomputed = sha256_bytes(encode_canonical(events))
        declared = ledger["declared_sha256"]
        require_sha256(declared, "%s.%s.declared_sha256" % (where, name))
        if recomputed != declared:
            raise VerifierFault(
                "%s.%s: ledger digest mismatch (declared %s, recomputed %s)"
                % (where, name, declared, recomputed))
        out[name] = {
            "sha256": recomputed,
            "event_count": len(events),
        }
    return out
