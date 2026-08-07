"""Canonical UTF-8 JSON, per spec V005 §9.4.

Sorted keys, no insignificant whitespace, no duplicate keys, no NaN/Infinity,
no undeclared fields. Fail-closed: every rejection raises VerifierFault.

No `assert` appears in this module (B-V011-SP2-07: a load-bearing audit must be
free of Python `assert`; `python -O` must not change behaviour).
"""

import json
import math


class VerifierFault(Exception):
    """Raised on any contract violation. Never caught to produce a PASS."""


def _reject_nonfinite(node, path="$"):
    if isinstance(node, float):
        if math.isnan(node) or math.isinf(node):
            raise VerifierFault("nonfinite number at %s" % path)
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not isinstance(k, str):
                raise VerifierFault("non-string key at %s" % path)
            _reject_nonfinite(v, "%s.%s" % (path, k))
        return
    if isinstance(node, (list, tuple)):
        for i, v in enumerate(node):
            _reject_nonfinite(v, "%s[%d]" % (path, i))
        return


def _no_duplicate_keys(pairs):
    seen = {}
    for k, v in pairs:
        if k in seen:
            raise VerifierFault("duplicate key %r" % k)
        seen[k] = v
    return seen


def loads_strict(text):
    """Parse JSON rejecting duplicate keys and nonfinite numbers."""
    if not isinstance(text, str):
        raise VerifierFault("loads_strict expects str")

    def _no_constant(name):
        raise VerifierFault("nonfinite literal %r rejected" % name)

    obj = json.loads(text, object_pairs_hook=_no_duplicate_keys,
                     parse_constant=_no_constant)
    _reject_nonfinite(obj)
    return obj


def dumps_canonical(obj):
    """Serialize to canonical form: sorted keys, no insignificant whitespace."""
    _reject_nonfinite(obj)
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False)


def encode_canonical(obj):
    """Canonical bytes (UTF-8) for content addressing."""
    return dumps_canonical(obj).encode("utf-8")


def require_exact_fields(obj, allowed, where):
    """Exact field inventory: missing and undeclared fields both fail."""
    if not isinstance(obj, dict):
        raise VerifierFault("%s: expected object" % where)
    have = set(obj)
    want = set(allowed)
    missing = sorted(want - have)
    extra = sorted(have - want)
    if missing or extra:
        raise VerifierFault(
            "%s: field inventory mismatch (missing=%s undeclared=%s)"
            % (where, missing, extra))
    return obj
