## PASTE 658 — CODEX LANE 2 = BUILDER A (GPT-5.6-SOL, EXTRA-HIGH) — [TASK 6 / BUILD] THE MANIFEST'S DECLARED_ROOT

(Same Lane 2 session rules: cleanroom writes; the registrar mirrors.)

CONTEXT (Q-598): run 007's three-way disagreement is adjudicated by the spec's own P0: `content_root(evidence_files) = evidence_manifest.declared_root`. Your parent bound `evidence_root_sha256` to the manifest FILE's digest — not the contract's meaning — and your manifest lacks the P0-required `declared_root` entirely. B's filename-relative content root (`e7820ca5…`) was one lawful reading of an underdetermined base; the base dissolves by declaration.

TASK:
P1. **The manifest fix:** add to `structural_evidence_manifest.json` the payload inventory — one row per evidence file: {relative_path, byte_length, sha256} — and `declared_root` = the spec's content_root over exactly those rows' recorded strings. The relative_path values you declare are the law (each row self-verifies by its sha256; no path trust).
P2. **The parent fix:** bind the `evidence_root_sha256` expectation to the manifest's `declared_root` (read from the P0-verified manifest, never recomputed from directory listings).
P3. Regenerate/rehash affected canonical artifacts; static self-check; disclosed delta; PIN CHECK. State plainly the corrected reading: the field is a content root, not a file digest.

OUTPUT: updated package + one sealed artifact
`STAGE8_TASK6_DECLARED_ROOT_FIX_LANE2_V001.md`
with final lines: `MANIFEST = inventory rows + declared_root (+value)`, `PARENT = binds declared_root`, `SELF_CHECK = passed`, `DELTAS = N disclosed`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal in the cleanroom, report hashes, STOP (the registrar mirrors). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
