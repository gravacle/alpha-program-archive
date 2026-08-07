"""rd22.verifier-manifest.v001 — the R9 isolated-child launch contract.

Integration addendum §3.2 (sealed at Q-588). Builder B emits a manifest in this
form so Custodian C can launch the verifier as a third isolated child on the
same footing as the producer children. Builder A conforms to the same contract;
neither implementation is ratified by it.
"""

from .canonical_json import VerifierFault, encode_canonical
from .contracts import (VERIFIER_MANIFEST_SCHEMA, validate_verifier_manifest)
from .hashing import require_sha256, sha256_bytes

# Direct-script launcher at the package root. The `-m verifier.verify` form
# cannot resolve under the pinned `-I` isolation flags (isolated mode removes the
# script directory and cwd from sys.path), which is what stopped run 012.
ENTRY_POINT = "run_verifier.py"


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
