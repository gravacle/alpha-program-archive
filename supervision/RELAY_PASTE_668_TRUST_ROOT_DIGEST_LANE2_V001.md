## PASTE 668 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / BUILD] ONE TRUST-ROOT DEFINITION: THE DIGEST, EVERYWHERE

(Same Lane 2 session rules: cleanroom writes; the registrar mirrors.)

CONTEXT: run 014 — THE VERIFIER EXECUTED and fail-closed with a true diagnostic: `runtime_subject.trust_root: not a lowercase sha256 hex digest`. Registrar root-cause: parent.py computes the trust root TWO WAYS — `trust_hash(runtime["native_system_trust_root"])` at :897 and the RAW STRUCTURE comparison at :1015 — so the value handed to the verifier is the object, not the 64-hex digest the contract (and the RD-22 pin's "trust root extracted and displayed") demands. This is exactly the two-places hazard Builder B found and fixed in its own package unasked at 667.

TASK: one definition — the trust root as a value is ALWAYS `trust_hash(native_system_trust_root)` (64-hex); every site (the T0-T4 comparisons, the bound manifest, the verifier environment, the terminal ledger, :1015's check) consumes that single function; the raw structure remains internal to the hash's input only. Audit every trust-root touchpoint and list them; demonstrate agreement between the sites in the self-check. Disclosed delta; PIN CHECK.

OUTPUT: updated parent + one sealed artifact
`STAGE8_TASK6_TRUST_ROOT_DIGEST_LANE2_V001.md`
with final lines: `TRUST_ROOT = single definition, digest everywhere (+N sites)`, `SELF_CHECK = passed (+site agreement shown)`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal in the cleanroom, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
