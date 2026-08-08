## PASTE 698 — CODEX 2 LANE = BUILDER A (5.6 SOL EXTRA HIGH) — [TASK 6 / TRANCHE] G2: THE STALE MEMBERS COPY — ONE BOUNDED FIX

(Same Codex 2 session rules. CLEANROOM-ONLY writes; the registrar mirrors. THE FIRST-TIME-RIGHT RULES apply. B's 697 re-pin is mirrored: new verifier root 10622f17… over 13 members, per-row bindings registrar-verified; B report 79649121….)

CONTEXT (Q-613): B's envelope check confirms your V009 whole — and P0 is TRUE on real inputs, all six conjuncts. One finding blocks run 031, registrar-confirmed in the bytes: your `inputs/verifier_root_members.generated.json` declares B's SUPERSEDED 695 root 43cff85d… with 7/13 digests stale (exactly the files 697 changed), under key `members` where your own V009 schema says `verifier_root_members`. That is the J4 failure mode relocated — a moment-in-time snapshot posing as generated data. Also of record (no code change): your stated +5/+5 mechanism was wrong — autojunk=True is the cause, but replace blocks go DOWN 14→10 and what rises is lines-per-side; the register carries the correction.

TASK (bounded):
L1. Make the members file UNABLE to go stale: either (a) regenerate it from B's current sealed package bytes as a validated step of your build tooling — with the schema key `verifier_root_members` — AND have the parent refuse at launch if the generated copy disagrees with B's sealed instance; or (b) remove the redundant copy entirely and let the parent consume only B's sealed instance (which the registrar verifies per-row). Pick the smaller lawful surface and say why. No new schema; no descriptor rows.
L2. Pin closure: grep value AND name for 43cff85d… and the stale digests; package inventory + manifests regenerated. Dry-run the parent's manifest-validation path against B's real sealed instance (rule 3).
OUTPUT: updated package + one sealed artifact `STAGE8_TASK6_G2_MEMBERS_FIX_CODEX2_V001.md`
with final lines: `FIX = (a) regenerated+refuse-on-disagree / (b) copy removed`, `SCHEMA_KEY = verifier_root_members / n-a`, `PIN_CLOSURE = N hits, all resolved`, `DRY_RUN = executed against B's sealed instance`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the name exists, STOP. Seal, report hashes, STOP (the registrar mirrors and invokes RUN 031 immediately). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
