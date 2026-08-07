#!/usr/bin/env python3
"""Direct-script launcher for the A35 independent verifier (Builder B, spec V005 R9).

WHY THIS FILE EXISTS
--------------------
`python3 -m verifier.verify` cannot resolve under the pinned isolation flags.
`-I` (isolated mode) implies `-E` and `-s`, and it also removes the script's
directory and the current working directory from `sys.path`. Empirically, on
CPython 3.9.6:

    $ python3 -I -S -B probe.py
    sys.path[0] = '.../python39.zip'
    import pkg.mod: FAILED -> ModuleNotFoundError

So a direct script ALONE does not fix it either: under `-I` the script's own
directory is NOT placed on `sys.path`. The launcher therefore derives its own
location from `__file__` and puts exactly that one directory on the path.

This is not path TRUST. It adds nothing from the environment, nothing from the
caller's cwd, and nothing from `PYTHONPATH` -- all of which `-I` correctly
suppresses and which this file does not reintroduce. It adds precisely the
directory this file is in, which is the package root, so that a self-contained
package can find its own modules under isolation. Content addressing is
unaffected: every input is still admitted only by digest.

CONTRACT
--------
Invoked by Custodian C, never by Builder B. Passes `sys.argv[1:]` through to
`verifier.verify.main` unchanged and propagates its exit code:

    0 = VERIFIED
    1 = ran, found faults
    2 = fail-closed before a verdict could be formed

`--dry-run-launch` resolves the package and exits 2 WITHOUT consuming any run
input: no spec, ledger, evidence, snapshot or gate is opened. It exists so the
launch path can be proved under the pinned flags without invoking the chain.

No `assert` appears in this file (B-V011-SP2-07).
"""

import os
import sys

# The package root is this file's directory, derived from __file__ so that it is
# correct under `-I`, under a rewritten argv[0], and under any cwd.
_PACKAGE_ROOT = os.path.dirname(os.path.abspath(__file__))
if _PACKAGE_ROOT not in sys.path:
    sys.path.insert(0, _PACKAGE_ROOT)

DRY_RUN_FLAG = "--dry-run-launch"
EXIT_FAIL_CLOSED = 2


def _dry_run():
    """Prove the launch path resolves; consume no run input; exit 2."""
    try:
        from verifier import verify as _verify
        from verifier.canonical_json import dumps_canonical
        from verifier.spec_census import SPEC_SHA256
    except Exception as exc:                      # noqa: BLE001 - fail closed
        sys.stderr.write("dry-run-launch: import failed: %s: %s\n"
                         % (type(exc).__name__, exc))
        return EXIT_FAIL_CLOSED

    payload = {
        "schema": "rd22.verifier-launch-dryrun.v001",
        "entry_point": os.path.basename(os.path.abspath(__file__)),
        "package_root_resolved": True,
        "verifier_module": _verify.__name__,
        "governing_spec_sha256": SPEC_SHA256,
        "isolated": bool(sys.flags.isolated),
        "no_site": bool(sys.flags.no_site),
        "dont_write_bytecode": bool(sys.dont_write_bytecode),
        "run_inputs_consumed": False,
        "chain_invoked": False,
        "verdict": "NO_VERDICT_DRY_RUN",
    }
    # Same canon as the real verdict: one tight value, no trailing newline.
    sys.stdout.write(dumps_canonical(payload))
    return EXIT_FAIL_CLOSED


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if DRY_RUN_FLAG in args:
        return _dry_run()

    try:
        from verifier.verify import main as verify_main
    except Exception as exc:                      # noqa: BLE001 - fail closed
        sys.stderr.write("launch: cannot import verifier.verify: %s: %s\n"
                         % (type(exc).__name__, exc))
        return EXIT_FAIL_CLOSED

    return verify_main(args)


if __name__ == "__main__":
    sys.exit(main())
