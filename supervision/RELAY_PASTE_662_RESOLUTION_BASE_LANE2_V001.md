## PASTE 662 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / BUILD] THE RESOLUTION BASE: RUN ROOT, NOT PACKAGE

(Same Lane 2 session rules: cleanroom writes; the registrar mirrors.)

CONTEXT: run 009 stopped at `VERIFIER_OUTPUT_CONTRACT` with the CORRECT names. Root cause at parent.py:561 — `base = Path(path).resolve().parent` resolves B's relative output/receipt declarations against the MANIFEST's directory (B's immutable package), then demands equality with `run_root/verifier.output.json` — unsatisfiable for any relative declaration, since the run root does not exist when B seals its manifest. The principle B proved (a package never receives writes) makes the correct base unambiguous.

TASK: resolve relative `output_path`/`receipt_path` declarations against the RUN ROOT (absolute declarations remain rejected unless equal — or simply reject absolute declarations outright as un-sealable; state your choice); static self-check; disclosed delta; PIN CHECK; one audit line: no other contract check resolves a run-scoped path against a package base.

OUTPUT: updated parent + one sealed artifact
`STAGE8_TASK6_RESOLUTION_BASE_FIX_LANE2_V001.md`
with final lines: `BASE = run root (+absolute-declaration policy)`, `AUDIT = no other package-based run-path resolution / (+items)`, `SELF_CHECK = passed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal in the cleanroom, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
