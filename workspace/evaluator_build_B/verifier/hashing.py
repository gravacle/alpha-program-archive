"""Content addressing. No path trust: a path is a locator, never an identity.

Every input is admitted only after its bytes hash to an independently supplied
expected digest. Spec V005 §12.2: every indexed manifest must carry the SHA-256
of what it indexes and must match the P0-verified supplied bytes.
"""

import hashlib
import os

from .canonical_json import VerifierFault

_HEX = set("0123456789abcdef")


def is_sha256(value):
    return (isinstance(value, str) and len(value) == 64
            and all(c in _HEX for c in value))


def require_sha256(value, where):
    if not is_sha256(value):
        raise VerifierFault("%s: not a lowercase sha256 hex digest" % where)
    return value


def sha256_bytes(data):
    if not isinstance(data, (bytes, bytearray)):
        raise VerifierFault("sha256_bytes expects bytes")
    return hashlib.sha256(bytes(data)).hexdigest()


def read_bytes(path):
    """Read a file as bytes. Existence failure is fail-closed, not silent."""
    if not isinstance(path, str) or path == "":
        raise VerifierFault("read_bytes: empty path")
    if not os.path.isfile(path):
        raise VerifierFault("read_bytes: not a regular file: %s" % path)
    handle = open(path, "rb")
    try:
        return handle.read()
    finally:
        handle.close()


def load_addressed(path, expected_sha256, where):
    """Return bytes only if they hash to `expected_sha256`.

    This is the sole admitted way to bring an external file into the verifier.
    """
    require_sha256(expected_sha256, "%s: expected_sha256" % where)
    data = read_bytes(path)
    actual = sha256_bytes(data)
    if actual != expected_sha256:
        raise VerifierFault(
            "%s: content-address mismatch for %s (expected %s, observed %s)"
            % (where, path, expected_sha256, actual))
    return data


def sha256_file_unverified(path):
    """Digest a file whose expected value is not yet known.

    Used only to REPORT an observed digest (for example when re-hashing a
    producer artifact whose digest the verifier must derive rather than
    assume). It never admits content on trust: callers compare the result.
    """
    return sha256_bytes(read_bytes(path))
