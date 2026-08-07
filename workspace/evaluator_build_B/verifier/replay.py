"""Independent replay of PASS predicates and fixture expectations.

The verifier never imports the producer's evaluator. It re-derives each
verdict from (a) the criterion string carried in the sealed descriptor and
(b) the content-addressed evidence bundle the producer emitted. If the two
disagree, the run fails closed.

Criterion language (spec V005 §2.2): a PASS criterion is opcode-reducible —
every atom is an opcode success/result field, a field admitted by a
content-addressed closed schema, an exact content-addressed input or expected
fixture record, a finite conjunction over an ENUM result, or a term defined by
those forms. That closure is what makes independent replay possible at all.
"""

import re

from .canonical_json import VerifierFault, loads_strict
from .hashing import require_sha256, sha256_bytes

# Opcodes whose use is permitted only inside a GATED-EXECUTION row after its
# gate opens (spec V005 opcode table).
GATED_ONLY_OPCODES = ("SYMBOLIC", "SPECTRAL")

_ATOM_SUCCESS = re.compile(r"^(r_[A-Za-z0-9_]+)\.success$")
_ATOM_FIELD = re.compile(r"^(r_[A-Za-z0-9_]+)\.([A-Za-z0-9_]+)\s*=\s*(.+)$")
_ATOM_FORALL = re.compile(
    r"^for every\s+(\w+)\s+in\s+(r_[A-Za-z0-9_]+)\.items:\s*(.+)$")
_ASSIGN = re.compile(r"(r_[A-Za-z0-9_]+)\s*:=\s*([A-Z][A-Z0-9_]*)\s*\(")


def declared_opcodes(procedure_text):
    """Opcodes a descriptor's procedure assigns, in order of appearance."""
    return [(m.group(1), m.group(2)) for m in _ASSIGN.finditer(procedure_text)]


def split_conjuncts(criterion):
    """Split a PASS criterion into atoms on top-level ` and `.

    Parenthesised finite conjunctions are preserved whole so the universal
    quantifier is replayed as one atom over an ENUM result.
    """
    if not isinstance(criterion, str):
        raise VerifierFault("criterion must be a string")
    atoms, depth, current = [], 0, []
    tokens = re.split(r"(\(|\)|\band\b)", criterion)
    for token in tokens:
        if token == "(":
            depth += 1
            current.append(token)
        elif token == ")":
            depth -= 1
            if depth < 0:
                raise VerifierFault("unbalanced parenthesis in criterion")
            current.append(token)
        elif token == "and" and depth == 0:
            atoms.append("".join(current).strip())
            current = []
        else:
            current.append(token)
    if depth != 0:
        raise VerifierFault("unbalanced parenthesis in criterion")
    atoms.append("".join(current).strip())
    return [a.strip("` ") for a in atoms if a.strip("` ")]


class EvidenceBundle(object):
    """Content-addressed opcode results emitted by the producer.

    The bundle is admitted only if its canonical bytes hash to a digest the
    check row declares. Its *contents* are then replayed, never trusted.
    """

    def __init__(self, raw_bytes, declared_sha256, where):
        require_sha256(declared_sha256, "%s: evidence digest" % where)
        observed = sha256_bytes(raw_bytes)
        if observed != declared_sha256:
            raise VerifierFault(
                "%s: evidence digest mismatch (declared %s, observed %s)"
                % (where, declared_sha256, observed))
        try:
            text = raw_bytes.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise VerifierFault("%s: evidence not UTF-8: %s" % (where, exc))
        parsed = loads_strict(text)
        if not isinstance(parsed, dict):
            raise VerifierFault("%s: evidence must be a JSON object" % where)
        self.results = parsed
        self.sha256 = observed
        self.where = where

    def result(self, name):
        row = self.results.get(name)
        if row is None:
            raise VerifierFault(
                "%s: evidence has no result %r" % (self.where, name))
        if not isinstance(row, dict):
            raise VerifierFault(
                "%s: result %r is not an object" % (self.where, name))
        return row

    def success(self, name):
        row = self.result(name)
        if "success" not in row:
            raise VerifierFault(
                "%s: result %r has no success field" % (self.where, name))
        value = row["success"]
        if value is not True and value is not False:
            raise VerifierFault(
                "%s: result %r success is not a boolean" % (self.where, name))
        return value

    def field(self, name, field):
        row = self.result(name)
        if field not in row:
            raise VerifierFault(
                "%s: result %r has no field %r" % (self.where, name, field))
        return row[field]

    def items(self, name):
        value = self.field(name, "items")
        if not isinstance(value, list):
            raise VerifierFault(
                "%s: result %r items is not a list" % (self.where, name))
        return value


def _literal(token):
    token = token.strip().strip("`").strip()
    if token == "empty":
        return []
    if token in ("true", "True"):
        return True
    if token in ("false", "False"):
        return False
    return token


def replay_atom(atom, bundle):
    """Replay one criterion atom. Returns True/False; never raises to PASS."""
    atom = atom.strip().strip("`").strip()

    if atom == "P0":
        # P0 is the parent's content-addressed admission of every input.
        return bundle.success("P0") if "P0" in bundle.results else False

    match = _ATOM_SUCCESS.match(atom)
    if match:
        return bundle.success(match.group(1))

    match = _ATOM_FORALL.match(atom.strip("()").strip())
    if match:
        var, enum_name, body = match.group(1), match.group(2), match.group(3)
        members = bundle.items(enum_name)
        if not members:
            # A finite conjunction over an empty ENUM is vacuously true. The
            # verifier records that fact rather than hiding it; a row that
            # relies on it is flagged by the caller.
            return True
        for member in members:
            for sub in split_conjuncts(body):
                concrete = sub.replace("_%s" % var, "_%s" % str(member))
                if not replay_atom(concrete, bundle):
                    return False
        return True

    match = _ATOM_FIELD.match(atom)
    if match:
        name, field, expected = match.groups()
        return bundle.field(name, field) == _literal(expected)

    raise VerifierFault("criterion atom not opcode-reducible: %r" % atom)


def replay_predicate(criterion, bundle):
    """Replay a full PASS criterion. Any non-reducible atom is an ERROR."""
    for atom in split_conjuncts(criterion):
        if not replay_atom(atom, bundle):
            return False
    return True


def replay_fixture(fixture, bundle):
    """Replay one fixture's expected result from evidence bytes.

    A fixture must declare its own content address and its expected record;
    the verifier recomputes the observed record's digest and compares.
    """
    for field in ("fixture_id", "expected_sha256", "observed_result_name"):
        if field not in fixture:
            raise VerifierFault("fixture missing %r" % field)
    require_sha256(fixture["expected_sha256"], "fixture expected_sha256")
    observed = bundle.field(fixture["observed_result_name"], "record")
    from .canonical_json import encode_canonical
    observed_sha = sha256_bytes(encode_canonical(observed))
    return {
        "fixture_id": fixture["fixture_id"],
        "expected_sha256": fixture["expected_sha256"],
        "observed_sha256": observed_sha,
        "match": observed_sha == fixture["expected_sha256"],
    }
