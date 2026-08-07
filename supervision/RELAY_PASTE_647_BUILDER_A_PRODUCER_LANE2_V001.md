## PASTE 647 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / BUILD] THE PARENT RUNNER + PRODUCER, PER SPEC V005

(Same Lane 2 session rules: write and seal in the CLEANROOM only; the registrar mirrors. You are BUILDER A of the RD-22 custody graph.)

PREFLIGHT (verify before starting; report any failure and STOP; live-append tolerance applies):
- Register head: Q-585 (the RD-22 authorization of record: `DECISION_RD22_BUILD_AUTHORIZED_2026-08-07.md`, SHA-256 stated there; read it — it binds scope, pin, and custody).
- THE GOVERNING SPEC: cleanroom `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md` = `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b`. Verify before reading. It is law: the R0-R10 state machine, the closed opcode set, the 66 descriptors, the manifests, the verdict-ledger schema, the fixtures, the authority firewall.
- THE RUNTIME PIN (authorized, not yours to vary): snapshot `50a6fc14…` (runtime_snapshot_v012.json) + gate `2ad7f72a…` (gate_v010) + trust root extracted from the snapshot at R0 and displayed.
- CUSTODY LIMITS: you implement the PARENT and the PRODUCER (and the check executors, manifests, schemas, fixture descriptors). You do NOT implement the verifier (Builder B's, independent). You do NOT invoke the full chain — Custodian C (the registrar) invokes. Syntax-level self-checks (imports parse, schemas validate) are permitted; no check executes against the subject lineage in your session.

TASK:
B1. **The code package**, written under a new cleanroom subdirectory `evaluator_build_A/`: the parent (direct script honoring R0's preflight conditions, `-I -S -B` invocation contract, self-hash, manifest verification, trust snapshots T0-T4, child launching, parent-side reclassification R7, producer comparison R8 with the three-field mask, terminal ledger R10); the producer child (the 56 STRUCTURAL check executors per their exact descriptors — the 10 gated rows emit NOT_RUN_GATE without starting; the structural fixtures; canonical-JSON output per the ledger schema); the closed manifests (normal, optimized; exact file inventories with hashes; the BRANCH_OUTCOME per-ID values DISPLAYED per the Q-583 obligation); the schemas; nothing of the verifier.
B2. **Content addressing throughout**: every input hash-pinned; the check-map root and descriptor hashes from the sealed spec; no path trust; load-bearing `assert` nowhere (explicit fail-closed branches with nonzero exit).
B3. **The build manifest artifact** (markdown, sealed): the complete file inventory with per-file SHA-256, the entry points, the invocation contract for Custodian C (exact command lines for R0), the BRANCH_OUTCOME display, what is implemented vs deferred (anything deferred is a listed item, not a silent gap), and your self-check transcript (syntax/schema validation only).
B4. Battery: F_PLDEC (no physical quantity in any code path outside gated stubs); anti-tuning; PIN CHECK on the manifest artifact; VERDICT-LINE SCOPE RULE.

OUTPUT: code under cleanroom `evaluator_build_A/` + one sealed artifact
`STAGE8_TASK6_EVALUATOR_BUILD_A_MANIFEST_LANE2_V001.md`
with final lines: `PACKAGE = complete / (+deferred list)`, `FILES = N (+inventory hashed)`, `GATED_ROWS = emit NOT_RUN_GATE without starting`, `BRANCH_OUTCOME = displayed per-ID`, `SELF_CHECK = syntax/schema only (+transcript)`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the output artifact name already exists, STOP and report — do not overwrite. Seal the manifest in the cleanroom, report hashes, STOP (the registrar mirrors and invokes). No register, plan, tracker, git, commit, or push action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation of any physical quantity; no comparison to measured constants. If a fence blocks a structural result, flag MACHINERY-APPEAL and continue.
