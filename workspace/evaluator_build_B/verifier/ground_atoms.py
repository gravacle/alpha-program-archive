"""V010-M1: R9 alone resolves closed ground atoms.

A ground atom has NO producer carrier. R9 reconstructs it from its own
P0-verified evidence table plus constants read out of the sealed descriptor row,
and a producer-emitted invocation or result object purporting to supply one is a
BR-1 contract fault.

The rule is an IFF against a closed schema, and V010 closes it explicitly: of
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

Conditions 1, 3, 4 and 5 are decidable from sealed bytes. Condition 2 is NOT:
see `resolve_member_key`.
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

_MEMBER_KEY = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_CONSTANT_NAME = re.compile(r"^[A-Z][A-Z0-9_]*_SHA256$")
_RESULT_NAME = re.compile(r"^r_[A-Za-z0-9_]+$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")

# The one atom shape V010 admits, read off a descriptor row:
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


def resolve_member_key(member_key, evidence_table, where):
    """Condition 2 -- and this is where V010 stops determining.

    SPEC GAP. V010 says only that `member_key` "resolves exactly one row in R9's
    own P0-verified evidence table". It never says BY WHAT MAPPING, and the
    member_key pattern is an identifier while the table is keyed by
    content-addressed relative paths. Two mappings are in reach and V010 bars
    both:

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


def resolve_ground_atom(record, evidence_table, evidence_index, where):
    """Evaluate a validated ground atom from R9's OWN sources.

    `evidence_table` is P0's evidence_files table; `evidence_index` maps digest
    to the supplied payload list. Condition 3 is honoured literally: the
    operand is obtained by REHASHING the resolved row's bytes, never by reading
    a declared digest.
    """
    validate_ground_atom(record, where)
    key = resolve_member_key(record["evidence_operand"]["member_key"],
                             evidence_table, where)
    declared = evidence_table[key]["sha256"]
    payloads = evidence_index.get(declared) or []
    if len(payloads) != 1:
        raise GroundAtomRefusal(
            record["result_name"],
            "evidence row %r resolves %d supplied payloads; exactly one is "
            "required to rehash" % (key, len(payloads)))
    observed = sha256_bytes(payloads[0][1])          # condition 3: REHASH
    constant = record["constant_operand"]["value"]
    equal = observed == constant
    return {"success": equal, "equal": equal,
            "atom_class": record["atom_class"],
            "evidence_sha256_rehashed": observed,
            "constant_sha256": constant,
            "resolved_by": "R9",
            "producer_carrier": False}
