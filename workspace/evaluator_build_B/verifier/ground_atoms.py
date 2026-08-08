"""V010-M1: R9 alone resolves closed ground atoms.

A ground atom has NO producer carrier. R9 reconstructs it from its own
P0-verified evidence table plus constants read out of the sealed descriptor row,
and a producer-emitted invocation or result object purporting to supply one is a
BR-1 contract fault.

The rule is an IFF against a closed schema, and V010-M1 closes it explicitly: of
the fourteen descriptor opcodes only a COMPARE atom satisfying every field and
every source-binding condition qualifies, "and no class is admitted by analogy."
This module therefore qualifies by CONSTRUCTION AND REFUSAL, never by example:
anything that fails one condition is not a ground atom, and an atom that is
neither producer-carried nor qualifying is a named refusal.

The five source-binding conditions, quoted in the spec's order:

  1. `result_name` and the complete atom occur in the same sealed descriptor row
  2. `member_key` resolves exactly one row in R9's own P0-verified evidence table
  3. R9 obtains the evidence operand by rehashing that row's supplied bytes
  4. `constant_name=value` occurs literally in that same descriptor row
  5. neither operand nor the comparison truth depends on a producer output,
     receipt, result, or choice

Conditions 1, 3, 4 and 5 are decidable from sealed bytes. Condition 2 was NOT
until V011-O1, which resolves it through the sealed source-and-span citation:
see `resolve_member_key_by_citation`. `resolve_member_key` is retained only as
the pre-V011 exact-key path and is no longer reached when a descriptor row is
supplied.
"""

import re

from .canonical_json import VerifierFault, require_exact_fields
from .hashing import sha256_bytes

GROUND_ATOM_SCHEMA = "rd22.r9-ground-atom.v001"
GROUND_ATOM_CLASS = "P0_EVIDENCE_SHA256_EQ_SEALED_SPEC_SHA256"

GROUND_ATOM_FIELDS = ("schema", "atom_class", "opcode", "result_name",
                      "evidence_operand", "constant_operand", "operand_order",
                      "mask")
EVIDENCE_OPERAND_FIELDS = ("source", "member_key", "field")
CONSTANT_OPERAND_FIELDS = ("source", "constant_name", "value")
OPERAND_ORDERS = ("evidence_left_constant_right", "constant_left_evidence_right")

EVIDENCE_SOURCE = "P0.evidence_files"
CONSTANT_SOURCE = "SEALED_DESCRIPTOR_CONSTANT"

# V011-O1: the condition-2 citation-key amendment. Closed schema, and the three
# forbidden mappings are consts -- they are refusals here, not preferences.
CITATION_AMENDMENT_SCHEMA = "rd22.r9-ground-atom-citation-key-amendment.v001"
CITATION_CARRIER = "SEALED_DESCRIPTOR_ROW.atom[result_name].source_and_span"
P0_CITATION_TABLE = "R9.P0.evidence_files_by_citation"
CITATION_KEY_FIELDS = ("source_sha256", "span")
CITATION_INTERVAL = "ZERO_BASED_HALF_OPEN"
CITATION_MATCH = "EXACT_TUPLE_EQUALITY"
CITATION_CARDINALITY = "EXACTLY_ONE"
CITATION_MEMBER_BINDING = (
    "MEMBER_KEY_BINDS_EXACT_ROW_MATCHING_DESCRIPTOR_ATOM_CITATION")
FORBIDDEN_MAPPINGS = ("PAYLOAD_FILENAME", "CONSTANT_DIGEST_SELF_REFERENCE",
                      "PRODUCER_SUPPLIED")
CITATION_AMENDMENT_FIELDS = ("schema", "amends", "condition", "atom_class",
                             "result_name", "member_key",
                             "descriptor_citation", "p0_index",
                             "forbidden_mappings")
DESCRIPTOR_CITATION_FIELDS = ("carrier", "source_sha256", "span")
P0_INDEX_FIELDS = ("table", "key_fields", "interval", "match", "cardinality",
                   "member_binding")

_MEMBER_KEY = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_CONSTANT_NAME = re.compile(r"^[A-Z][A-Z0-9_]*_SHA256$")
_RESULT_NAME = re.compile(r"^r_[A-Za-z0-9_]+$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")

# The one atom shape V010-M1 admits, read off a descriptor row:
#   r_X:=COMPARE(P0.evidence_files[key].sha256,CONST_SHA256,empty)
# and its mirror. Nothing else is matched, so nothing else can qualify.
_ATOM_EVIDENCE_LEFT = re.compile(
    r"(r_[A-Za-z0-9_]+)\s*:=\s*COMPARE\(\s*P0\.evidence_files\[([A-Za-z_][A-Za-z0-9_]*)\]\.sha256\s*,"
    r"\s*([A-Z][A-Z0-9_]*_SHA256)\s*,\s*empty\s*\)")
_ATOM_CONSTANT_LEFT = re.compile(
    r"(r_[A-Za-z0-9_]+)\s*:=\s*COMPARE\(\s*([A-Z][A-Z0-9_]*_SHA256)\s*,"
    r"\s*P0\.evidence_files\[([A-Za-z_][A-Za-z0-9_]*)\]\.sha256\s*,\s*empty\s*\)")


class GroundAtomRefusal(Exception):
    """This atom is neither producer-carried nor qualifying. NOT a FAIL."""

    def __init__(self, result_name, reason):
        Exception.__init__(self, reason)
        self.result_name = result_name
        self.reason = reason


def sealed_constant(descriptor_row, constant_name):
    """Condition 4: `constant_name=value` occurs LITERALLY in this row."""
    found = re.findall(r"\b%s\s*=\s*([0-9a-f]{64})\b" % re.escape(constant_name),
                       descriptor_row)
    if len(found) != 1:
        return None
    return found[0]


def normalize_ground_atom(result_name, descriptor_row):
    """Build the closed record for `result_name`, or None if it is not this shape.

    None means "not a ground atom", which is a fact about the atom and not a
    fault: most atoms are carried by the producer's structured invocation.
    """
    for pattern, order in ((_ATOM_EVIDENCE_LEFT, OPERAND_ORDERS[0]),
                           (_ATOM_CONSTANT_LEFT, OPERAND_ORDERS[1])):
        for match in pattern.finditer(descriptor_row):
            if match.group(1) != result_name:
                continue                      # condition 1: same row, same name
            if order == OPERAND_ORDERS[0]:
                member_key, constant_name = match.group(2), match.group(3)
            else:
                constant_name, member_key = match.group(2), match.group(3)
            value = sealed_constant(descriptor_row, constant_name)
            if value is None:
                raise GroundAtomRefusal(
                    result_name,
                    "constant %s does not occur exactly once as "
                    "%s=<64 hex> in the sealed descriptor row (condition 4)"
                    % (constant_name, constant_name))
            return {
                "schema": GROUND_ATOM_SCHEMA,
                "atom_class": GROUND_ATOM_CLASS,
                "opcode": "COMPARE",
                "result_name": result_name,
                "evidence_operand": {"source": EVIDENCE_SOURCE,
                                     "member_key": member_key,
                                     "field": "sha256"},
                "constant_operand": {"source": CONSTANT_SOURCE,
                                     "constant_name": constant_name,
                                     "value": value},
                "operand_order": order,
                "mask": [],
            }
    return None


def validate_ground_atom(record, where):
    """The closed schema, field by field. An iff, so every clause is required."""
    require_exact_fields(record, GROUND_ATOM_FIELDS, where)
    if record["schema"] != GROUND_ATOM_SCHEMA:
        raise VerifierFault("%s: schema must be %r" % (where, GROUND_ATOM_SCHEMA))
    if record["atom_class"] != GROUND_ATOM_CLASS:
        raise VerifierFault("%s: atom_class must be %r" % (where, GROUND_ATOM_CLASS))
    if record["opcode"] != "COMPARE":
        raise VerifierFault(
            "%s: opcode %r is not a ground-atom opcode; V010-M1 admits COMPARE "
            "only and no class by analogy" % (where, record["opcode"]))
    if not _RESULT_NAME.match(record["result_name"] or ""):
        raise VerifierFault("%s: result_name is not an r_<name> symbol" % where)
    ev = record["evidence_operand"]
    require_exact_fields(ev, EVIDENCE_OPERAND_FIELDS, "%s.evidence_operand" % where)
    if ev["source"] != EVIDENCE_SOURCE:
        raise VerifierFault("%s.evidence_operand.source must be %r"
                            % (where, EVIDENCE_SOURCE))
    if not _MEMBER_KEY.match(ev["member_key"] or ""):
        raise VerifierFault("%s.evidence_operand.member_key is not an identifier"
                            % where)
    if ev["field"] != "sha256":
        raise VerifierFault("%s.evidence_operand.field must be 'sha256'" % where)
    co = record["constant_operand"]
    require_exact_fields(co, CONSTANT_OPERAND_FIELDS, "%s.constant_operand" % where)
    if co["source"] != CONSTANT_SOURCE:
        raise VerifierFault("%s.constant_operand.source must be %r"
                            % (where, CONSTANT_SOURCE))
    if not _CONSTANT_NAME.match(co["constant_name"] or ""):
        raise VerifierFault("%s.constant_operand.constant_name does not match "
                            "[A-Z][A-Z0-9_]*_SHA256" % where)
    if not _SHA256.match(co["value"] or ""):
        raise VerifierFault("%s.constant_operand.value is not a lowercase sha256"
                            % where)
    if record["operand_order"] not in OPERAND_ORDERS:
        raise VerifierFault("%s.operand_order is outside the closed enum" % where)
    if record["mask"] != []:
        raise VerifierFault("%s.mask must be empty (maxItems 0)" % where)
    return record


def descriptor_citation(descriptor_row, result_name, where):
    """The (source_sha256, span) the SEALED DESCRIPTOR ROW carries for this atom.

    V011-O1 fixes the carrier as
    `SEALED_DESCRIPTOR_ROW.atom[result_name].source_and_span`, so the row is the
    only lawful source: `forbidden_mappings` names PRODUCER_SUPPLIED, which rules
    out the producer's invocation linkage even though it carries both fields.

    Returns (source_sha256, span). Raises a named refusal identifying WHICH key
    field the row does not carry -- never a guess, and never a fallback to a
    forbidden carrier.
    """
    # V011-O1's carrier const is `...source_and_span` -- ONE unit. So the
    # source identity must be SYNTACTICALLY BOUND to the span in the row, not
    # merely present somewhere in it. This matters: the V009-06 row carries a
    # second, unrelated 64-hex digest (the precedence decision), and a rule that
    # took "the one digest that is not the atom's constant" would have silently
    # adopted it as the source identity. Found by running this, not reading it.
    bound = re.findall(r"([0-9a-f]{64})\s*:\s*\[(\d+),(\d+)\)", descriptor_row)
    bound += re.findall(r"@\s*([0-9a-f]{64})\s*:\s*\[(\d+),(\d+)\)", descriptor_row)
    spans = re.findall(r"\[(\d+),(\d+)\)", descriptor_row)
    if len(spans) != 1:
        raise GroundAtomRefusal(
            result_name,
            "the sealed descriptor row carries %d half-open spans; V011-O1 "
            "requires exactly one source_and_span citation" % len(spans))
    span = [int(spans[0][0]), int(spans[0][1])]
    if len(bound) == 1:
        return bound[0][0], span
    paths = re.findall(r"`([A-Za-z0-9_./-]+\.(?:json|md))`", descriptor_row)
    others = [d for d in re.findall(r"\b([0-9a-f]{64})\b", descriptor_row)]
    raise GroundAtomRefusal(
        result_name,
        "V011-O1 descriptor_citation.source_sha256 has no lawful carrier: the "
        "carrier const is SEALED_DESCRIPTOR_ROW...source_and_span, ONE unit, "
        "but the row binds its span [%d,%d) to a PATH (%s) and to no SHA-256. "
        "The row's %d other 64-hex digests are the atom's own constant and the "
        "precedence decision, neither of which is the cited source, and "
        "adopting an unbound digest would be a guess. The producer invocation "
        "does carry source_sha256 and is barred (forbidden_mappings includes "
        "PRODUCER_SUPPLIED); the atom's constant is barred "
        "(CONSTANT_DIGEST_SELF_REFERENCE); the filename is barred "
        "(PAYLOAD_FILENAME). SPEC GAP, two parts: (1) the descriptor row must "
        "carry the source SHA-256 bound to the span it already carries; and "
        "(2) the cited source must be a supplied payload, or R9 can derive no "
        "row's citation to match against"
        % (span[0], span[1], (paths or ["<none>"])[0], len(others)))


def evidence_files_by_citation(evidence_table, evidence_index, span, where):
    """Build `R9.P0.evidence_files_by_citation` -- R9's OWN index.

    A row's citation is DERIVED, never read from a producer record: for each
    supplied payload treated as a candidate source, slice the descriptor's span
    and key the resulting bytes by (sha256(source_bytes), span). Nothing about
    this uses a filename, a producer citation, or the atom's own constant.
    """
    start, end = span
    table = {}
    for source_digest, payloads in sorted(evidence_index.items()):
        for _name, blob in payloads:
            if end > len(blob) or start >= end:
                continue
            table.setdefault((source_digest, (start, end)), []).append(
                blob[start:end])
    return table


def resolve_member_key_by_citation(record, descriptor_row, evidence_table,
                                   evidence_index, where):
    """Condition 2 under V011-O1: EXACT_TUPLE_EQUALITY, EXACTLY_ONE."""
    source_sha256, span = descriptor_citation(
        descriptor_row, record["result_name"], where)
    table = evidence_files_by_citation(evidence_table, evidence_index, span,
                                       where)
    rows = table.get((source_sha256, (span[0], span[1]))) or []
    if len(rows) != 1:
        raise GroundAtomRefusal(
            record["result_name"],
            "citation (source_sha256=%s, span=[%d,%d)) resolves %d rows of %s; "
            "V011-O1 requires EXACTLY_ONE under EXACT_TUPLE_EQUALITY. The "
            "cited source is not among the supplied payloads, so R9 cannot "
            "derive any row's citation for it"
            % (source_sha256, span[0], span[1], len(rows), P0_CITATION_TABLE))
    return rows[0]


def resolve_member_key(member_key, evidence_table, where):
    """Pre-V011 exact-key path, retained and no longer the resolution of record.

    SUPERSEDED by V011-O1: condition 2 now resolves through the sealed
    source-and-span citation, so `resolve_member_key_by_citation` is the path a
    descriptor-bearing caller takes. This function is reached only when no
    descriptor row is supplied, and it still refuses rather than guess. The
    historical reasoning is kept because it is why V011-O1 exists: V010 stated
    the requirement without a mapping, and the two mappings in reach were both
    barred:

      (a) match the identifier against the payload FILENAME. Payload filenames
          are producer-authored, so the comparison's truth would depend on a
          producer CHOICE -- condition 5 forbids exactly that.
      (b) take the row whose digest equals the constant. Then the comparison is
          COMPARE(X,X) and cannot fail -- the vacuity the V007 C-B-V009-06 row
          forbids by name and that this lane convicted at relay 683.

    So the atom is not resolvable without inventing a rule, and inventing one is
    the fabrication BR-1 exists to prevent. Refuse, and name what the spec must
    add. If a future spec supplies the mapping, only this function changes.
    """
    exact = [k for k in evidence_table if k == member_key]
    if len(exact) == 1:
        return exact[0]
    raise GroundAtomRefusal(
        where,
        "member_key %r resolves %d rows of R9's P0-verified evidence table by "
        "exact key match; V010-M1 condition 2 requires exactly one but states "
        "no mapping from an identifier to a content-addressed payload path. "
        "SPEC GAP: the descriptor or §9 must state the member_key -> evidence "
        "row mapping, and it may not be the payload filename (producer choice, "
        "barred by condition 5) nor the constant's own digest (COMPARE(X,X), "
        "barred by the row)" % (member_key, len(exact)))


def citation_amendment_record(record, descriptor_row, where):
    """The closed V011-O1 amendment record for this atom, or a named refusal."""
    source_sha256, span = descriptor_citation(
        descriptor_row, record["result_name"], where)
    value = {
        "schema": CITATION_AMENDMENT_SCHEMA,
        "amends": GROUND_ATOM_SCHEMA,
        "condition": 2,
        "atom_class": GROUND_ATOM_CLASS,
        "result_name": record["result_name"],
        "member_key": record["evidence_operand"]["member_key"],
        "descriptor_citation": {"carrier": CITATION_CARRIER,
                                "source_sha256": source_sha256,
                                "span": span},
        "p0_index": {"table": P0_CITATION_TABLE,
                     "key_fields": list(CITATION_KEY_FIELDS),
                     "interval": CITATION_INTERVAL,
                     "match": CITATION_MATCH,
                     "cardinality": CITATION_CARDINALITY,
                     "member_binding": CITATION_MEMBER_BINDING},
        "forbidden_mappings": list(FORBIDDEN_MAPPINGS),
    }
    require_exact_fields(value, CITATION_AMENDMENT_FIELDS, where)
    require_exact_fields(value["descriptor_citation"],
                         DESCRIPTOR_CITATION_FIELDS,
                         "%s.descriptor_citation" % where)
    require_exact_fields(value["p0_index"], P0_INDEX_FIELDS,
                         "%s.p0_index" % where)
    return value


def resolve_ground_atom(record, evidence_table, evidence_index, where,
                        descriptor_row=None):
    """Evaluate a validated ground atom from R9's OWN sources.

    `evidence_table` is P0's evidence_files table; `evidence_index` maps digest
    to the supplied payload list. Condition 3 is honoured literally: the
    operand is obtained by REHASHING the resolved row's bytes, never by reading
    a declared digest.
    """
    validate_ground_atom(record, where)
    if descriptor_row is not None:
        # V011-O1: condition 2 resolves through the sealed source-and-span
        # citation ONLY. The amendment record is constructed and closed first,
        # so a missing key field refuses before any byte is compared.
        citation_amendment_record(record, descriptor_row, where)
        member_bytes = resolve_member_key_by_citation(
            record, descriptor_row, evidence_table, evidence_index, where)
    else:
        key = resolve_member_key(record["evidence_operand"]["member_key"],
                                 evidence_table, where)
        declared = evidence_table[key]["sha256"]
        payloads = evidence_index.get(declared) or []
        if len(payloads) != 1:
            raise GroundAtomRefusal(
                record["result_name"],
                "evidence row %r resolves %d supplied payloads; exactly one is "
                "required to rehash" % (key, len(payloads)))
        member_bytes = payloads[0][1]
    observed = sha256_bytes(member_bytes)            # condition 3: REHASH
    constant = record["constant_operand"]["value"]
    equal = observed == constant
    return {"success": equal, "equal": equal,
            "atom_class": record["atom_class"],
            "evidence_sha256_rehashed": observed,
            "constant_sha256": constant,
            "resolved_by": "R9",
            "producer_carrier": False}
