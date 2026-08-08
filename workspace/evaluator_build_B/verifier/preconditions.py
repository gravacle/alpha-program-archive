"""R9's independent P0 computation (spec V008 statement V008-R9-1).

V008-R9-1: "R9 itself computes every one of the six §2.1 `P0` conjuncts from
the supplied, hash-verified `BASE` carriers before replaying a criterion. A
producer-emitted P0 result object is a contract fault and is never an input."

Spec §2.1 fixes the six conjuncts:

    P0 := strict_parse(BASE)
       and every_declared_sha256_matches_the_supplied_bytes
       and content_root(subject_files)=subject_manifest.declared_root
       and content_root(evidence_files)=evidence_manifest.declared_root
       and no_duplicate_path_or_key
       and every_required_input_present.

Three outcomes, and they are three, not two:

    P0 = true                      every conjunct evaluated and satisfied
    P0 = false                     every conjunct evaluated, one is false
    PRECONDITION_NOT_REPLAYABLE    a conjunct could not be evaluated at all

The third is V008-R9-3's closed refusal value, and it exists because a FAIL
that was never evaluated is not a verdict. This module never collapses the
third case into the second.
"""

from .canonical_json import VerifierFault, loads_strict, require_exact_fields
from .contracts import (PRECONDITION_REFUSAL_FIELDS, PRECONDITION_REFUSAL_SCHEMA,
                        PRECONDITION_NOT_REPLAYABLE, SUBJECT_MANIFEST_FIELDS,
                        MANIFEST_FILE_FIELDS)
from .hashing import content_root, read_bytes, sha256_bytes

# The six §2.1 conjuncts, in the spec's own order. Named so a refusal can say
# which one it could not evaluate.
P0_CONJUNCTS = (
    "strict_parse_BASE",
    "every_declared_sha256_matches_the_supplied_bytes",
    "content_root_subject_files_equals_declared_root",
    "content_root_evidence_files_equals_declared_root",
    "no_duplicate_path_or_key",
    "every_required_input_present",
)


def precondition_refusal(missing_carrier, conjunct):
    """The closed V008-R9-3 value. Distinct from a criterion result of FAIL."""
    if not missing_carrier:
        raise VerifierFault("precondition refusal needs a named carrier")
    value = {
        "schema": PRECONDITION_REFUSAL_SCHEMA,
        "status": PRECONDITION_NOT_REPLAYABLE,
        "criterion_evaluated": False,
        "missing_carrier": missing_carrier,
    }
    require_exact_fields(value, PRECONDITION_REFUSAL_FIELDS,
                         "precondition refusal")
    if conjunct not in P0_CONJUNCTS:
        raise VerifierFault("unknown P0 conjunct %r" % conjunct)
    return value


class PreconditionNotReplayable(Exception):
    """Carries the closed refusal value. NOT a VerifierFault, and NOT a FAIL."""

    def __init__(self, value):
        Exception.__init__(self, value["missing_carrier"])
        self.value = value


def _manifest_triples(manifest, where):
    out = []
    for i, entry in enumerate(manifest["files"]):
        require_exact_fields(entry, MANIFEST_FILE_FIELDS,
                             "%s.files[%d]" % (where, i))
        out.append((entry["relative_path"], entry["byte_length"],
                    entry["sha256"]))
    return out


def load_manifest(path, declared_sha256, where):
    """strict_parse + content address. Conjunct 1 for this carrier."""
    data = read_bytes(path)
    observed = sha256_bytes(data)
    if observed != declared_sha256:
        raise VerifierFault(
            "%s: content-address mismatch (declared %s, observed %s)"
            % (where, declared_sha256, observed))
    manifest = loads_strict(data.decode("utf-8"))
    if not isinstance(manifest, dict):
        raise VerifierFault("%s: manifest is not an object" % where)
    return manifest


def compute_p0(subject_manifest, evidence_manifest, evidence_index, where):
    """Compute all six conjuncts. Returns the P0 result object.

    `evidence_index` maps sha256 -> bytes for every file R9 was actually
    supplied. A declared file absent from it makes conjunct 2 UNEVALUABLE for
    that file -- not false. Raises PreconditionNotReplayable in that case,
    naming the carrier, because "no mismatch found" and "never compared" are
    different facts and only one of them is a discharged duty.
    """
    conjuncts = {}

    # 1 -- strict_parse(BASE). Both manifests already parsed strictly and were
    # admitted by content address in load_manifest; the ledger likewise.
    require_exact_fields(subject_manifest, SUBJECT_MANIFEST_FIELDS,
                         "%s.subject_manifest" % where)
    subject_files = _manifest_triples(subject_manifest,
                                      "%s.subject_manifest" % where)
    if "payload_inventory" not in evidence_manifest:
        raise PreconditionNotReplayable(precondition_refusal(
            "evidence_manifest.payload_inventory",
            "strict_parse_BASE"))
    evidence_files = [(e["relative_path"], e["byte_length"], e["sha256"])
                      for e in evidence_manifest["payload_inventory"]]
    conjuncts["strict_parse_BASE"] = True

    # 5 -- no duplicate path or key. loads_strict already rejects duplicate
    # OBJECT KEYS; duplicate PATHS inside a manifest are this check.
    for label, triples in (("subject", subject_files),
                           ("evidence", evidence_files)):
        paths = [p for p, _n, _s in triples]
        if len(set(paths)) != len(paths):
            conjuncts["no_duplicate_path_or_key"] = False
            break
    else:
        conjuncts["no_duplicate_path_or_key"] = True

    # 3 and 4 -- content roots. Fully evaluable from the manifests' own
    # declared triples: content_root is defined over declared path/length/
    # digest, so this is the manifests' internal consistency, and conjunct 2
    # is what ties a declaration to bytes.
    conjuncts["content_root_subject_files_equals_declared_root"] = (
        content_root(subject_files) == subject_manifest["declared_root"])
    conjuncts["content_root_evidence_files_equals_declared_root"] = (
        content_root(evidence_files) == evidence_manifest["declared_root"])

    # 2 -- every declared sha256 matches the SUPPLIED bytes. A declared file
    # whose bytes R9 was not supplied is UNEVALUABLE, and V008-R9-3 is the
    # value for exactly that.
    table = {}
    matched = True
    for label, triples in (("subject_files", subject_files),
                           ("evidence_files", evidence_files)):
        for path, length, digest in triples:
            blob = evidence_index.get(digest)
            if blob is None:
                raise PreconditionNotReplayable(precondition_refusal(
                    "%s[%s] bytes (sha256 %s) are declared but not supplied "
                    "to R9" % (label, path, digest),
                    "every_declared_sha256_matches_the_supplied_bytes"))
            if sha256_bytes(blob) != digest or len(blob) != length:
                matched = False
            if label == "evidence_files":
                table[path] = {"sha256": digest, "byte_length": length}
    conjuncts["every_declared_sha256_matches_the_supplied_bytes"] = matched

    # 6 -- every required input present: both manifests, and every declared
    # member of each, are in hand. Reaching here means they are.
    conjuncts["every_required_input_present"] = True

    missing = [c for c in P0_CONJUNCTS if c not in conjuncts]
    if missing:
        raise PreconditionNotReplayable(precondition_refusal(
            "P0 conjunct %s was never evaluated" % missing[0], missing[0]))

    return {"success": all(conjuncts[c] for c in P0_CONJUNCTS),
            "conjuncts": dict(conjuncts),
            "evidence_files": table}
