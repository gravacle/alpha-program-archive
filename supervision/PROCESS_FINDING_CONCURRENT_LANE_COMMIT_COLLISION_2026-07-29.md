# PROCESS FINDING — TWO LANES SHARE ONE GIT WORKING TREE, AND IT NEARLY FROZE A WRONG BASELINE

Recorded 2026-07-29 by the reviewer lane. This is a real near-miss, not a nuisance. It should be
read before the next time both lanes are active at once.

## WHAT HAPPENED, WITH TIMESTAMPS

```
19:48:30  reviewer rsyncs MB Work/alpha_supervision -> archive/supervision (113 files, new)
19:5x     reviewer's commit BLOCKED by pre-commit hook: 4 YELLOW growth classes
             relay_sequence_head 3 -> 14 · scope_declaration 107 -> 232
             unsourced_quantitative_claim 16 -> 37 · superseded_path_hardwire 548 -> 560
19:52:36  reviewer edits corpus_check.py to fix the cause (see below)
19:53:11  CODEX REWRITES corpus_check_baseline_v001.json
19:5x     Codex commits the ENTIRE working tree as 077a9d1 "Mirror supervision record state"
             -- including the reviewer's two sealed results and the reviewer's apparatus fix
19:5x     reviewer's own commit returns "nothing to commit"; its prepared message is LOST
```

## THE UNDERLYING DEFECT THE HOOK CAUGHT (correctly), AND ITS FIX

`archive/supervision/` is a byte-copy of `MB Work/alpha_supervision`, and `corpus_check.py`
scans BOTH — the first as part of `archive`, the second as `supervision_root`. `walk_files`
dedupes by `Path.resolve()`, which cannot see through a physical copy, so every supervision file
was read twice and every metric derived from that content doubled. `relay_sequence_head` was the
loudest: every paste number appeared twice, so every number became a "duplicate class", 3 -> 14.

FIXED by excluding a mirror root that duplicates an authoritative root scanned elsewhere
(`MIRROR_ROOTS` / `is_mirror_path`, populated in `roots_from_args`, empty whenever the
authoritative root IS the mirror — so a fresh clone with no `MB Work` still scans correctly).
NOT fixed by re-baselining: re-baselining would have frozen the double-counted numbers and
destroyed the baseline's meaning. Selftest passes, 0 asserts, verdict unchanged under `-O`, all
nine YELLOW metrics equal baseline exactly, overall GREEN.

## THE NEAR-MISS

Codex rewrote the frozen baseline at 19:53:11 — 35 seconds after the reviewer changed the very
code that produces it. The written values (`superseded 518`, `scope 100`, `hardcoded 2926`,
`unsourced 15`) are the MIRROR-FREE counts, i.e. they happen to match the post-fix checker
exactly. **THAT WAS LUCK, NOT DESIGN.** Had Codex re-baselined thirty seconds earlier, the
double-counted numbers (560 / 232 / 37 / 14) would have been frozen as the permanent baseline,
and the apparatus built specifically to detect drift would have been silently calibrated to a
double-count. Nothing in the current setup prevents that.

## WHAT IS ACTUALLY IN COMMIT 077a9d1, SINCE ITS MESSAGE DOES NOT SAY

The message reads "Mirror supervision record state". The commit in fact carries:
- `supervision/RESULT_TRACE_COLLAPSE_THEOREM_AND_GRAVITY_GAUGE_IMPOSSIBILITY_2026-07-29.md`
  (sealed `a7b82f9a...`) — the verified general-N trace-collapse theorem; the refutation of its
  own novelty; the impossibility proof that no x-independent gravity-to-gauge ratio exists on
  this carrier; and the live `|H|`-flux counterexample inside the program's own operator.
- `supervision/RESULT_FENCE_INVENTORY_AND_WHAT_IS_TESTABLE_TODAY_2026-07-29.md` (sealed) — the
  eleven-instrument fence inventory; G3's non-authority and nonexistent release condition; the
  standing diagnostic permission; and two corrections of reviewer claims made the same day.
- `corpus_check.py` — the mirror double-count fix above.
- Errata pointers appended to four previously sealed artifacts, each re-sealed.
- 113 supervision artifacts mirrored for the first time.

THE ARTIFACTS CARRY THEIR OWN CONTENT AND SEALS, SO THE RECORD IS INTACT. Only the git log is
misleading, and this note is the index entry that corrects it.

## WHAT TO DO ABOUT IT

Three options, none yet adopted — this is a finding, not a ruling:
1. Give each lane its own clone and merge deliberately. Cost: merge work.
2. Make the baseline write refuse when `corpus_check.py` is dirty in the working tree. Cheap,
   narrow, and closes the exact near-miss above. Recommended as the minimum.
3. Require the writing lane to name itself and the checker's git blob hash in the baseline
   payload, so a baseline written against modified code is identifiable after the fact.

Option 2 is a one-condition change and would have converted this near-miss into a clean refusal.

alpha_computed = false; proof_authorized = false.
