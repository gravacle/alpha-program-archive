PASTE 123 — CODEX
TO: Codex (primary construction lane; reported idle). FROM: reviewer lane via principal.
2026-07-29.

SUBJECT: Build `corpus_check.py` — render the program's process rules in CODE.

WHY: the program's process rules are PROSE, and prose is ALLOW-shaped: it permits correct
behaviour and forbids nothing mechanically. Every process failure of the last two days was a
lane being permitted to do the wrong thing by a rule that could not stop it. Measured today:
481 cleanroom .md, 287 WITHOUT sidecars; 303 audit scripts of which 34 certify by substring;
233 scripts writing literal True/False into result payloads; 214 checker-shaped scripts
already exist. *** THE PROGRAM IS NOT SHORT OF CHECKING MACHINERY. IT IS SHORT OF ONE THING
THAT RUNS THE CHECKS TOGETHER AND CAN SAY NO. ***
Design of record (read it first, in full):
/Users/bgm/MB Work/alpha_supervision/PROCESS_HARDENING_DESIGN_2026-07-29.md
sidecar ef7666d2d938d153c4a890c7956f8fb20b806e7482230f477d693b3fe1db4e7b

BUILD: one executable script `corpus_check.py`, committed to the archive repository so it
TRAVELS (hooks are local and not cloned — that is why deploy_status.sh was committed).
Modes: `--report` (default, human-readable, exit 0) and `--gate` (exit non-zero on RED).
ELEVEN CHECKS, each independently reportable and independently switchable:
  1. SEAL INTEGRITY — every *.seal.sha256 verifies; list the unsealed artifact set by class.
  2. DEPLOY STATE — archive ahead-count 0 and working tree clean.
  3. SUBSTRING CERTIFICATION — flag audit scripts whose check-dict values are `X in Y`
     expressions over file text.
  4. HARDCODED CLAIM FLAGS — flag literal True/False assigned to claim-shaped keys in result
     payloads.
  5. VOIDED PASS — any results/ PASS whose hash is named by a later provenance/ failure
     record.
  6. MARKER PREFIX COLLISION — any acceptance marker that is a strict PREFIX of another,
     under substring matching.
  7. SUPERSEDED-PATH HARDWIRE — any script referencing vNNN where vNNN+1 exists (this is the
     defect that still blocks the census gate after today's fingerprint refresh).
  8. FINGERPRINT CURRENCY — recompute every tracked-hash manifest found.
  9. SCOPE DECLARATION — any artifact asserting a negative ("zero hits", "does not exist",
     "nowhere", "no such") must declare its search root within a small line window. *** THIS
     IS THE CHECK THAT WOULD HAVE PREVENTED THE INVERTED CONCLUSION. ***
 10. RELAY SEQUENCE HEAD — report the max paste number across all roots.
 11. AUTHORITY CURRENCY — every principal ruling in /Users/bgm/MB Work/alpha_supervision is
     cited by at least one artifact in the governing cleanroom chain.
RED (gate blocks): 1, 2, 5, 6, 8, 11.  YELLOW (baseline, must not grow): 3, 4, 7, 9, 10.
BASELINE DISCIPLINE: record today's counts for the YELLOW classes ONCE, in a committed
baseline file; the gate fails only if a count INCREASES. Do NOT attempt to clean up 287
unsealed artifacts or 34 substring audits as part of this task — freezing the baseline is the
deliverable, cleanup is separate work.

HARD CONSTRAINTS:
 - The script must NEVER rule, adopt, retire, or seal anything. It reports and it blocks. A
   checker that could rule would be a checker that could FIT. State this in its docstring.
 - It must not compute or read any physical value, and must not open
   a32_holdout/custodian_private/ under any circumstance. Add an explicit refusal.
 - No Python `assert` for any load-bearing check — asserts vanish under `python -O`. This is
   the exact defect that disqualifies stage8_battery_evaluator_v001.py under the corpus's own
   permanent regression obligation 7. Use unconditional checks that survive -O, and include a
   self-test proving the script's own verdict is unchanged under `python3 -O`.
 - Its selftest may NOT construct the condition it then detects (the tautology class the
   red-team charter names). Test against real corpus state or committed fixtures.
 - Report refutations, never repair them: if a check finds a defect, it REPORTS. It must not
   edit, seal, or fix anything.

DELIVERABLES: corpus_check.py (committed to the archive repo); the frozen baseline file; a
short usage note; the first full `--report` output as a sealed artifact so today's state is
on the record. Wire it into the archive's pre-commit hook in `--gate` mode, and state
plainly in the usage note that the hook is LOCAL AND NOT CLONED, so the script — not the
hook — is the durable instrument.

DEFINITION OF DONE: SEALED, MIRRORED, COMMITTED, AND PUSHED; report the output of
sh "/Users/bgm/MB Work/alpha-program-archive/deploy_status.sh" plus the first --report run.
alpha_computed = false; proof_authorized = false.
