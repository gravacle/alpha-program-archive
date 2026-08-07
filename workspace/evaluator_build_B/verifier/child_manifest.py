"""rd22.verifier-manifest.v001 — the R9 isolated-child launch contract.

Integration addendum §3.2 (sealed at Q-588). Builder B emits a manifest in this
form so Custodian C can launch the verifier as a third isolated child on the
same footing as the producer children. Builder A conforms to the same contract;
neither implementation is ratified by it.
"""

import os

from .canonical_json import VerifierFault, encode_canonical
from .contracts import (VERIFIER_MANIFEST_SCHEMA, validate_verifier_manifest)
from .hashing import require_sha256, sha256_bytes, sha256_file_unverified

# Direct-script launcher at the package root. The `-m verifier.verify` form
# cannot resolve under the pinned `-I` isolation flags (isolated mode removes the
# script directory and cwd from sys.path), which is what stopped run 012.
ENTRY_POINT = "run_verifier.py"

# The load-bearing byte set of this package, as one root.
#
# Builder A stopped run 013 correctly: an entry script that dispatches the whole
# verifier is load-bearing, and a root that does not cover it leaves an unpinned
# file able to change behaviour. The remedy adopted here is ROOT INCLUSION --
# one root over every load-bearing byte -- rather than a second, separately
# pinned entry digest, because one root is one thing to check and cannot drift
# out of step with a companion value.
#
# MEMBER LIST (12), by package-relative path, sorted lexicographically:
#     contracts/verifier_verdict.schema.json
#     run_verifier.py
#     verifier/__init__.py
#     verifier/canonical_json.py
#     verifier/child_manifest.py
#     verifier/comparison.py
#     verifier/contracts.py
#     verifier/hashing.py
#     verifier/replay.py
#     verifier/runtime_state.py
#     verifier/spec_census.py
#     verifier/verify.py
#
# COMPUTATION (unchanged in scheme, extended in membership):
#     verifier_root_sha256 := SHA256( concat( sha256_hex(member_bytes)
#                                             for member in sorted(members) ) )
# The verdict schema is load-bearing for the handshake: it is the contract
# Builder A validates this verifier's verdict against. Pinned by its own sidecar
# since 674, it sat OUTSIDE this root -- the same shape as the launcher question
# A raised at 667, and resolved the same way, by root inclusion. One root over
# every load-bearing byte; a file outside it is not load-bearing.
ROOT_MEMBERS = (
    "contracts/verifier_verdict.schema.json",
    "run_verifier.py",
)
ROOT_PACKAGE_DIR = "verifier"                # every *.py inside is a member


def package_root_members(base_dir):
    """Exact, sorted, package-relative member list. One definition, one caller."""
    members = list(ROOT_MEMBERS)
    pkg = os.path.join(base_dir, ROOT_PACKAGE_DIR)
    for name in sorted(os.listdir(pkg)):
        if name.endswith(".py"):
            members.append("%s/%s" % (ROOT_PACKAGE_DIR, name))
    return sorted(members)


def package_root_digest(base_dir):
    """verifier_root_sha256 over every load-bearing byte, launcher included."""
    parts = [sha256_file_unverified(os.path.join(base_dir, rel))
             for rel in package_root_members(base_dir)]
    return sha256_bytes("".join(parts).encode("utf-8"))


def build_manifest(verifier_root_sha256, input_roots, output_path,
                   receipt_path, optimize):
    """Construct the launch manifest. `optimize` is DECLARED, never inferred."""
    require_sha256(verifier_root_sha256, "verifier_root_sha256")
    if optimize is not True and optimize is not False:
        raise VerifierFault("optimize must be declared as a boolean")

    # argv is concrete except for six NAMED substitution tokens the parent
    # fills. A parent that knows nothing of this package's internals can launch
    # it by substituting exactly these and nothing else.
    argv = ["python3"]
    if optimize:
        argv.append("-O")
    argv += [
        ENTRY_POINT,
        "--spec", "${SPEC_PATH}",
        "--ledger", "${LEDGER_PATH}",
        "--ledger-sha256", "${LEDGER_SHA256}",
        "--evidence-dir", "${EVIDENCE_DIR}",
        "--runtime-snapshot", "${RUNTIME_SNAPSHOT_PATH}",
        "--runtime-gate", "${RUNTIME_GATE_PATH}",
    ]

    manifest = {
        "schema": VERIFIER_MANIFEST_SCHEMA,
        "verifier_root_sha256": verifier_root_sha256,
        "entry_point": ENTRY_POINT,
        "argv": argv,
        "optimize": optimize,
        "input_roots": dict(input_roots),
        "output_path": output_path,
        "receipt_path": receipt_path,
        "stdout_discipline": {
            "format": "canonical-json",
            "lines": 1,
            "other_output_permitted": False,
        },
        "exit_contract": {
            "verified": 0,
            "faults_found": 1,
            "fail_closed": 2,
        },
        "receipt_authoritative": False,
    }
    return validate_verifier_manifest(manifest, "verifier manifest")


def manifest_sha256(manifest):
    """Content address of the manifest, for the parent's child row."""
    return sha256_bytes(encode_canonical(
        validate_verifier_manifest(manifest, "verifier manifest")))
