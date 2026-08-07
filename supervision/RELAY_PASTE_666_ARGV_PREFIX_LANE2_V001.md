## PASTE 666 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / BUILD] THE ARGV PREFIX: DIRECT-SCRIPT FORM

(Same Lane 2 session rules: cleanroom writes; the registrar mirrors.)

CONTEXT: run 013 stopped at `VERIFIER_ARGV_PREFIX` — your parent expects `['python3', '-m', <entry>]`, the exact form that CANNOT resolve under the pinned `-I -S -B` isolation (registrar-reproduced at run 012; B demonstrated it as a control). Your own producer children launch as DIRECT SCRIPTS. The contract (`rd22.verifier-manifest.v001`) admits either form; the hard-coded `-m` prefix is an authored expectation contradicting both the runtime physics and your own pattern.

TASK: accept the direct-script prefix `['python3', '<script>', ...]` where `<script>` is validated against the manifest's entry declaration and resolves (package-relative) to a file inside the verifier package whose digest is covered by `verifier_root_sha256`; keep rejecting `-c`, `-m`-less arbitrary flags, and anything outside the package. Static self-check; disclosed delta; PIN CHECK; audit line: no other launch-form expectation is authored against the runtime physics.

OUTPUT: updated parent + one sealed artifact
`STAGE8_TASK6_ARGV_PREFIX_FIX_LANE2_V001.md`
with final lines: `PREFIX = direct-script accepted (+validation)`, `AUDIT = no other authored launch-form / (+items)`, `SELF_CHECK = passed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal in the cleanroom, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
