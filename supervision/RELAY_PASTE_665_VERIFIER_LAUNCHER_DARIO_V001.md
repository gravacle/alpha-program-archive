## PASTE 665 — DARIO LANE = BUILDER B (OPUS 5 ULTRA, HIGH EFFORT) — [TASK 6 / BUILD] THE DIRECT-SCRIPT LAUNCHER

(Same Dario session rules. ARCHIVE-SIDE ONLY; the registrar mirrors.)

CONTEXT: run 012 is the deepest yet — R8 PASSED (the two producers agree semantically), the producer ledger was composed, the parent bound your ledger sentinel exactly as your handshake expects (`verifier.manifest.bound.json` exists), and YOUR VERIFIER WAS LAUNCHED. It exited with empty stdout because `-m verifier.verify` cannot resolve under the pinned isolation flags (`-I` ignores cwd and PYTHONPATH; registrar-reproduced: ModuleNotFoundError). The producer pattern of record is a DIRECT SCRIPT at package root.

TASK:
U1. Add a root-level launcher `evaluator_build_B/run_verifier.py` — a direct script that imports and dispatches to `verifier.verify`'s main with sys.argv passed through (the script's own directory lands on sys.path under direct execution, so `import verifier` resolves; no path mutation code beyond what direct execution provides).
U2. Update the manifest instance: `entry_point` and argv to the direct-script form (the parent substitutes tokens; the script path may be declared package-relative if the parent resolves launch paths against the package — from the bound manifest the parent already rewrote argv[0] and absolute paths, so declare the launcher the way the contract's launch section expects; if the contract only admits `-m` form, that is a finding to state, and the launcher name goes in argv[1] as a package-relative script path).
U3. Verify by executing the launcher yourself under `-I -S -B` with a synthetic --help or dry-run flag that exits 2 cleanly WITHOUT consuming run inputs (no chain invocation); sidecar; canonical form; disclosed delta.

OUTPUT: launcher + updated instance/sidecar + one sealed artifact
`STAGE8_TASK6_VERIFIER_LAUNCHER_DARIO_V001.md`
with final lines: `LAUNCHER = direct script at package root`, `RESOLVES_UNDER = -I -S -B (demonstrated)`, `INSTANCE = updated, canonical, sidecar-pinned`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
