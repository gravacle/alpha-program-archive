## PASTE 667 — DARIO LANE = BUILDER B (OPUS 5 ULTRA, HIGH EFFORT) — [TASK 6 / BUILD] BRING THE LAUNCHER INSIDE THE PINNED ROOT

(Same Dario session rules. ARCHIVE-SIDE ONLY; the registrar mirrors.)

CONTEXT: Builder A stopped before implementing the direct-script acceptance — correctly: your `verifier_root_sha256` (`b32b700f…`) covers the ten `verifier/*.py` files but NOT `run_verifier.py` (`2c8caad0…`). An unpinned script may not be load-bearing. A's stated remedy options: include the launcher in the verifier root, or add an independently pinned entry-script digest to the contract.

TASK:
V1. Choose and implement — the root-inclusion form is the simpler custody shape (one root covers every load-bearing byte): recompute `verifier_root_sha256` over the ten modules PLUS `run_verifier.py` (state the exact member list and computation), update the manifest instance + sidecar (canonical tight form), and display old/new root values. If you instead judge the separate entry-digest cleaner, implement that and say why.
V2. Confirm the dry-run demonstration still passes under `-I -S -B` with the updated pinning.
V3. Disclosed delta; PIN CHECK.

OUTPUT: updated instance/sidecar (+ contract if V1 chose the entry-digest form) + one sealed artifact
`STAGE8_TASK6_LAUNCHER_IN_ROOT_DARIO_V001.md`
with final lines: `ROOT = covers launcher (+member count, old->new)` / `ENTRY_DIGEST = pinned (+value)`, `DRY_RUN = passes under -I -S -B`, `INSTANCE = canonical, sidecar-pinned`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal, report hashes, STOP (the registrar mirrors; Builder A then proceeds on its stopped task). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
