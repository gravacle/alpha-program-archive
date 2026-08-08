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

from .canonical_json import VerifierFault, encode_canonical, loads_strict
from .ground_atoms import (GroundAtomRefusal, normalize_ground_atom,
                           resolve_ground_atom)
from .hashing import require_sha256, sha256_bytes

# Opcodes whose use is permitted only inside a GATED-EXECUTION row after its
# gate opens (spec V005 opcode table).
GATED_ONLY_OPCODES = ("SYMBOLIC", "SPECTRAL")

# --- payload roles ---------------------------------------------------------
# A row's evidence may carry payloads of two kinds, and they are true in two
# different ways:
#
#   CONSUMABLE     a structured argument the recorded invocation consumes. Its
#                  truth is STRUCTURAL: it must parse, be a JSON object, and be
#                  canonical, because an opcode reads its fields.
#   RAW_GROUNDING  an exact byte span of a sealed source, carried to ground the
#                  row in the record. Its truth is BYTE-IDENTITY: a slice of a
#                  larger JSON or markdown file is lawfully not standalone
#                  parseable, and demanding that it parse is a category error.
#
# Both are digest-verified. Only the first is parsed.
PAYLOAD_CONSUMABLE = "CONSUMABLE"
PAYLOAD_RAW_GROUNDING = "RAW_GROUNDING"

# `<symbol>@<source_sha256>:[start,end)`. Duplicated deliberately from
# contracts: replay must not import contracts (contracts imports replay), and
# one shared regex across a cycle is worse than two lines that agree.
_INSTANCE_ID = re.compile(
    r"^([A-Za-z0-9_.\-]+)@([0-9a-f]{64}):\[(\d+),(\d+)\)$")

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


def invocation_arguments(invocation, where):
    """Canonical bytes of every structured argument the invocation consumes.

    Roles are derived from the INVOCATION, never from a producer-declared
    `role` label. The distinction is not stylistic: a label could exculpate a
    broken payload by renaming it raw, whereas an argument cannot -- a producer
    that drops a payload out of the invocation drops it out of the computation
    and fails the coverage guard below. A producer-declared object may accuse;
    it may never exculpate (BR-1).

    Returns a list of (argument_name, canonical_bytes, is_object), or None
    when the row records no invocation. `is_object` decides whether coverage
    can apply: only an object-valued argument can be reproduced by a consumable
    payload, because only a JSON object is admitted as one.
    """
    if invocation is None:
        return None
    items = invocation if isinstance(invocation, list) else [invocation]
    if not items:
        return None
    out = []
    for item in items:
        if not isinstance(item, dict):
            raise VerifierFault("%s: invocation must be an object" % where)
        args = item.get("args")
        if not isinstance(args, dict):
            raise VerifierFault("%s: invocation args must be an object" % where)
        out.append(("<args>", encode_canonical(args), True))
        for name in sorted(args):
            value = args[name]
            out.append((name, encode_canonical(value), isinstance(value, dict)))
    return out


def declared_spans(invocation):
    """Span lengths the recorded invocations declare, from their instance_ids.

    Returns a list of (byte_length, instance_id). Empty when nothing is
    span-grounded -- a COMPARE over two digests legitimately carries a null
    instance_id, so an empty result is a fact about the row, not a defect.
    """
    if invocation is None:
        return []
    items = invocation if isinstance(invocation, list) else [invocation]
    out = []
    for item in items:
        if not isinstance(item, dict):
            continue
        match = _INSTANCE_ID.match(item.get("instance_id") or "")
        if match:
            start, end = int(match.group(3)), int(match.group(4))
            out.append((end - start, item["instance_id"]))
    return out


def _parses_as_json(blob):
    """(ok, parsed). A raw source span is admitted ONLY by failing this.

    `loads_strict` raises VerifierFault for the canon violations it screens
    (duplicate keys, nonfinite literals) and lets the decoder's own ValueError
    through for malformed text. A raw span is malformed by construction, so
    both must be caught here or the verifier CRASHES on the very payload this
    function exists to classify -- which is how the demonstration found it.
    """
    try:
        return True, loads_strict(blob.decode("utf-8"))
    except (UnicodeDecodeError, ValueError, VerifierFault):
        return False, None


def classify_payloads(payloads, invocation, where):
    """Partition already-digest-verified payloads by DERIVED role.

    `payloads` is an ordered list of (digest, blob); every one of them has
    already been admitted through `load_addressed`, so digest verification
    covers ALL payloads regardless of role. This function decides only which
    of them are parsed.

    Two guards, in both directions:

      GUARD A -- strictness is preserved where it applies. Anything that parses
        is treated as consumable and must be a canonical JSON object. A payload
        cannot dodge the structural check by being merely malformed-but-parseable.

      GUARD B -- no silent promotion or demotion. When the row records its
        invocation, EVERY argument must be reproduced by some payload; a
        corrupted consumable therefore fails coverage rather than sliding into
        the raw class, and a raw payload is never handed to the bundle to stand
        in for a missing argument.

    Returns {"consumable": [...], "raw": [...], "faults": [...]}.
    """
    wanted = invocation_arguments(invocation, where)
    spans = declared_spans(invocation)
    consumable, raw, faults, unrequired = [], [], [], []

    for digest, blob in payloads:
        ok, parsed = _parses_as_json(blob)
        if not ok:
            # Cannot be a structured argument to any opcode: nothing can read
            # fields off bytes that do not parse. Admitting it as raw therefore
            # concedes nothing, which is why this test is not an escape hatch.
            entry = {"sha256": digest, "byte_length": len(blob),
                     "role": PAYLOAD_RAW_GROUNDING, "linkage": "digest"}
            # BYTE-SPAN LINKAGE (686 recorded this as undelivered; the field
            # arrived at 687). The payload's independently verified digest is
            # its identity; the declared span must agree on its LENGTH. The
            # verifier still cannot re-slice the source -- the source file is
            # not a run input -- so this is arithmetic against a declaration,
            # not a re-derivation, and it is labelled as such.
            if spans:
                match = [sid for length, sid in spans if length == len(blob)]
                if match:
                    entry["linkage"] = "digest+span"
                    entry["instance_id"] = match[0]
                else:
                    faults.append(
                        "%s: raw payload %s is %d bytes but no recorded "
                        "instance_id declares a span of that length (%s)"
                        % (where, digest, len(blob),
                           ", ".join("%d" % l for l, _ in spans)))
            raw.append(entry)
            continue
        if not isinstance(parsed, dict):
            faults.append("%s: payload %s parses but is not a JSON object"
                          % (where, digest))
            continue
        if encode_canonical(parsed) != blob:
            # Q-594 canon. A non-canonical consumable is a canon fault, not a
            # licence to reclassify it as raw.
            faults.append("%s: consumable payload %s is not canonical" % (where, digest))
            continue
        consumable.append((digest, blob, parsed))

    if wanted is not None:
        have = set(blob for _, blob, _ in consumable)
        for name, want_bytes, is_object in wanted:
            if name == "<args>":
                continue
            if not is_object:
                # NOT EVIDENCE, so not coverable. A consumable payload is
                # admitted only if it parses to a JSON OBJECT, so only
                # object-valued arguments can ever be reproduced by one.
                # Demanding a payload for a spec-fixed constant, a P0-derived
                # digest, or an empty mask is the same category error the
                # registrar identified for raw payloads at 686, moved into the
                # argument dimension: an unsatisfiable demand, not a guard.
                # Scalars cannot slide into the raw class either -- they are
                # not payloads -- so nothing is conceded by exempting them.
                unrequired.append(name)
                continue
            if want_bytes not in have and not any(
                    parsed.get(name) is not None
                    and encode_canonical(parsed[name]) == want_bytes
                    for _, _, parsed in consumable):
                faults.append(
                    "%s: invocation argument %r is not reproduced by any "
                    "digest-verified payload" % (where, name))
    if not faults and len(consumable) != 1:
        # The predicate replays against exactly one structured object. Zero and
        # many are both fail-closed: a raw payload must never be promoted to
        # stand in for a missing one, and picking among several by list
        # position is the ordering dependency this function exists to remove.
        faults.append(
            "%s: expected exactly one consumable payload, found %d (%d raw "
            "grounding payload(s) digest-verified and not parsed)"
            % (where, len(consumable), len(raw)))

    return {"consumable": consumable, "raw": raw, "faults": faults,
            "unrequired_args": sorted(unrequired)}


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


# --- opcode recomputation ---------------------------------------------------
# Spec V011 R9: the verifier "replays each pass predicate FROM EVIDENCE BYTES".
# Reading `.success` off a producer-emitted result object would let a
# producer-declared object carry the criterion's direction -- the BR-1
# violation this lane has enforced against Builder A for twenty relays, and it
# was in Builder B's own replay. These recompute the atoms instead.
IMPLEMENTED_OPCODES = ("COMPARE", "DAG")


def opcode_compare(args, where):
    """`COMPARE(x,y,mask)` -- spec §2.2: canonicalize only the predeclared
    process-local fields in `mask`, then require byte equality of all else."""
    for field in ("left", "right", "mask"):
        if field not in args:
            raise VerifierFault("%s: COMPARE needs %r" % (where, field))
    mask = args["mask"]
    if not isinstance(mask, list):
        raise VerifierFault("%s: COMPARE mask must be a list" % where)
    left, right = args["left"], args["right"]
    if isinstance(left, dict) and isinstance(right, dict):
        left, right = dict(left), dict(right)
        for field in mask:
            left.pop(field, None)
            right.pop(field, None)
    elif mask:
        raise VerifierFault(
            "%s: COMPARE mask is non-empty but the operands are not objects; "
            "only predeclared process-local FIELDS may be masked" % where)
    equal = encode_canonical(left) == encode_canonical(right)
    return {"success": equal, "equal": equal}


def opcode_dag(args, where):
    """`DAG(G,P)` -- spec §2.2: parse nodes and exact parent lists; reject
    cycles, self-parenting and missing parents; compare with required parents.

    The single-authority form is the ONLY one implemented here, because it is
    the only one V011 authorises for a one-object encoding: `P` must be the
    spec-fixed sentinel, and the comparison clause is then discharged by the
    principal ruling's identity -- NOT by synthesizing COMPARE(X,X), which the
    row expressly forbids and which this function therefore never performs.
    """
    graph = args.get("graph")
    authority = args.get("authority")
    if authority != "PRINCIPAL_SINGLE_AUTHORITY":
        raise VerifierFault(
            "%s: DAG second operand %r is not the spec-fixed single-authority "
            "sentinel; the two-object form is not implemented" % (where, authority))
    if not isinstance(graph, dict):
        raise VerifierFault("%s: DAG graph must be an object" % where)
    nodes = set(graph)
    for node, parents in graph.items():
        if not isinstance(parents, list) or not all(
                isinstance(p, str) for p in parents):
            raise VerifierFault(
                "%s: DAG parent list for %r is not a list of node names"
                % (where, node))
        if node in parents:
            return {"success": False, "reason": "self-parenting at %r" % node}
        missing = [p for p in parents if p not in nodes]
        if missing:
            return {"success": False,
                    "reason": "missing parents %s at %r" % (sorted(missing), node)}
        if len(set(parents)) != len(parents):
            return {"success": False, "reason": "duplicate parent at %r" % node}
    # Kahn: a total topological order over every node, or a cycle exists.
    remaining = dict((n, len(graph[n])) for n in graph)
    children = dict((n, []) for n in graph)
    for node, parents in graph.items():
        for parent in parents:
            children[parent].append(node)
    queue = sorted(n for n in graph if remaining[n] == 0)
    order = []
    while queue:
        node = queue.pop(0)
        order.append(node)
        for child in children[node]:
            remaining[child] -= 1
            if remaining[child] == 0:
                queue.append(child)
        queue.sort()
    if len(order) != len(graph):
        return {"success": False,
                "reason": "cycle: %d of %d nodes ordered" % (len(order), len(graph))}
    return {"success": True, "nodes": len(graph), "order": order,
            "roots": sorted(n for n in graph if not graph[n]),
            "sinks": sorted(n for n in graph if not children[n])}


def recompute_results(invocations, where, descriptor_row=None,
                      criterion=None, evidence_table=None,
                      evidence_index=None):
    """Recompute every result object the criterion needs, from R9's own sources.

    Two disjoint provenances, and the disjointness is the point (V010-M1):

      producer-carried   the row's structured `invocation` supplies the args;
                         R9 recomputes the opcode over them.
      GROUND ATOM        no producer carrier exists. R9 reconstructs the atom
                         from the sealed descriptor row plus its own P0-verified
                         evidence table. A producer invocation or result object
                         purporting to supply one is a BR-1 contract fault.

    An opcode this package has not implemented is an explicit fault, never a
    silent pass: a criterion the verifier cannot replay is not a criterion the
    verifier has confirmed.
    """
    results = {}
    ground_names = set()
    if descriptor_row and criterion:
        for atom in split_conjuncts(criterion):
            match = _ATOM_SUCCESS.match(atom.strip().strip("`").strip())
            if match:
                record = normalize_ground_atom(match.group(1), descriptor_row)
                if record is not None:
                    ground_names.add(match.group(1))

    for i, inv in enumerate(invocations or []):
        at = "%s.invocation[%d]" % (where, i)
        opcode, name = inv["opcode"], inv["result_name"]
        if name in ground_names:
            raise VerifierFault(
                "%s: %s is a V010-M1 ground atom; no producer carrier exists "
                "for it and a producer-emitted invocation or result object "
                "purporting to supply one is a contract fault under BR-1"
                % (at, name))
        if opcode not in IMPLEMENTED_OPCODES:
            raise VerifierFault(
                "%s: opcode %s is not implemented by this verifier; the "
                "criterion cannot be replayed from evidence bytes" % (at, opcode))
        handler = opcode_compare if opcode == "COMPARE" else opcode_dag
        results[name] = handler(inv["args"], at)

    for name in sorted(ground_names):
        record = normalize_ground_atom(name, descriptor_row)
        results[name] = resolve_ground_atom(
            record, evidence_table or {}, evidence_index or {},
            "%s.%s" % (where, name), descriptor_row=descriptor_row)
    return results


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
        # V008-R9-1: R9 computes P0 itself; the caller injects the computed
        # object under this key. Absence here is a build error, never a
        # criterion FAIL -- relay 693's defect was returning False for an atom
        # that had not been evaluated.
        if "P0" not in bundle.results:
            raise VerifierFault(
                "P0 was not computed before replay; R9 must compute all six "
                "\u00a72.1 conjuncts itself (V008-R9-1)")
        return bundle.success("P0")

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


def replay_fixture(fixture_row, bundle):
    """Replay one fixture against its NAMED EXPECTED RECORD (OWED CHANGE 2).

    Addendum §2.3 rule 2: `expected_verdict_fields` are SPEC-FIXED in spec §10's
    table (`competitor_reproduced=true`, `c_equals_one_selected=false`, ...),
    not producer-supplied. The pre-conformance code compared a single opaque
    `expected_sha256`; a digest cannot be checked against §10's sealed table,
    a named record can. The spec won over the adapter's convenience.

    Rule 1 (quarantine) is enforced by contracts.validate_fixture_row before
    this is reached: no observed field may be undeclared.
    """
    expected = fixture_row["expected_verdict_fields"]
    observed = fixture_row["observed_verdict_fields"]

    mismatches = []
    missing = []
    for name in sorted(expected):
        if name not in observed:
            missing.append(name)
            continue
        if observed[name] != expected[name]:
            mismatches.append({
                "field": name,
                "expected": expected[name],
                "observed": observed[name],
            })

    # Independent recomputation: the observed record must also be reproducible
    # from the evidence bundle, not merely asserted in the ledger row.
    replayed = None
    result_name = fixture_row.get("deterministic_procedure")
    if isinstance(result_name, str) and result_name in bundle.results:
        replayed = bundle.field(result_name, "verdict_fields")
        if replayed != observed:
            mismatches.append({
                "field": "<record>",
                "expected": observed,
                "observed": replayed,
                "note": "ledger row disagrees with the evidence bundle",
            })

    return {
        "fixture_id": fixture_row["fixture_id"],
        "execution_class": fixture_row["execution_class"],
        "expected_fields": len(expected),
        "missing_fields": missing,
        "mismatches": mismatches,
        "match": (not mismatches and not missing),
    }
