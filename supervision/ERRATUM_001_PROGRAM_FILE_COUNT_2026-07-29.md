# ERRATUM 001 — THE PROGRAM FILE-COUNT FIGURE WAS WRONG IN BOTH DIRECTIONS

Issued 2026-07-29 by the reviewer lane at the principal's direction. APPEND-ONLY. Corrects a
figure that propagated through the supervision record by citation rather than by verification.
Every artifact citing the old figure is listed below and should be read against this erratum.

## THE FIGURE AS CITED, AND WHY IT WAS CHECKED

Throughout 2026-07-28/29 the supervision record stated that the week's sweeps had covered
"840 of ~4800 files", with the parent tree given as ~3271 files and the remainder made up of
"~800 in memory-bank, ~614 in alpha-program-archive, ~101 in _external_handoffs". The principal
asked why anything would be stored in memory-bank. That question exposed the error.

## CORRECTION 1 — memory-bank IS NOT PART OF THIS PROGRAM

`/Users/bgm/MB Work/memory-bank` is the MEMORY BANK WEB/MOBILE APPLICATION: capacitor.config.ts,
lambda/, node_modules, package.json, deploy scripts, 142 tracked files. BOUNDED NEGATIVE: grep
for `gravacle`, `kappa_record`, `alpha_computed`, `Q_spec` across its `*.md`, `*.py`, `*.ts`
returns ZERO files. It contains no program content of any kind. Its ~800 files (142 tracked;
the rest vendored `node_modules`) were counted as program files and must not be.

## CORRECTION 2 — AND THE PARENT TREE WAS UNDERCOUNTED BY MORE THAN memory-bank ADDED

Measured 2026-07-29, `*.md`/`*.py`/`*.json`/`*.csv`, excluding `.proof_deps`, `.python_deps`,
`site-packages`, `sympy`, `node_modules`, `.cache`, `.git`, `external/`, `third_party/`,
`sources/`, and duplicated `review_packet` subtrees:

```text
cleanroom (alpha_fundamental_record_action_cleanroom_v003)   1,138
parent tree, EXCLUDING the cleanroom                          5,930
MB Work/alpha_supervision                                       128
_external_handoffs                                              229
                                                            -------
DISTINCT PROGRAM CONTENT                                      7,425
MB Work/alpha-program-archive (tracked)                       3,662  <- MIRROR, not distinct
```

*** THE PARENT TREE ALONE IS 5,930 FILES, NOT ~3,271. *** So the net effect of both corrections
is that the scope error reported on 2026-07-28 was WORSE than stated, not better. The reviewer's
first reaction to correction 1 — that the searched fraction was therefore HIGHER than reported —
WAS WRONG AND IS WITHDRAWN. The cleanroom is roughly 1,138 of ~7,425 distinct program files,
i.e. about 15%, against the 17.5% implied by the old figure.

## THE CORRECTED STATEMENT, for use in future citations

The week's sweeps of 2026-07-25 to 2026-07-28 ran against the cleanroom only: approximately
1,138 files out of approximately 7,425 files of distinct program content, with the parent tree
alone accounting for about 5,930 of them. The archive is a mirror and is not counted as distinct
content. memory-bank is a separate application and is not program content at all.
ALL FIGURES ARE APPROXIMATE AND SCOPE-DEPENDENT: they exclude vendored dependency trees and
duplicated review packets, and a different but defensible exclusion list gives a different total.
ANY FUTURE CITATION MUST STATE ITS EXCLUSIONS, per the same discipline the scope finding itself
established.

## ARTIFACTS CITING THE OLD FIGURE

SEALED (this erratum is referenced from it; the artifact is not edited):
  GRAVITY_EVIDENCE_REGISTER_V001_2026-07-29.md
UNSEALED (read against this erratum):
  BOHM_CLEANROOM_SCOPE_PROVENANCE_2026-07-28.md · BOHM_CTP_ABSOLUTE_RESPONSE_ROUTE_SWEEP_2026-07-28.md ·
  BOHM_C4_CONSUMER_SWEEP_RESULTS_2026-07-28.md · BOHM_ROUTE_RUNNABILITY_WORKFLOW_RECOVERED_2026-07-28.md ·
  BOHM_REPLAN_AUDIT_RESULTS_2026-07-29.md · PLAN_TO_ALPHA_V006_2026-07-29.md ·
  STAGE7_INDEPENDENT_REVIEWS_2026-07-24.md · STAGE8_KAPPA_RECORD_THEOREM_BATTERY_SPEC_V002.md ·
  CONTINUATION_STATE.md
NO CLEANROOM ARTIFACT CITES THE FIGURE. Bounded: the five cleanroom files matching `4800|3271`
match only inside SHA-256 hash substrings (e.g. `...485cc4800549aae...`), verified by inspection.
NO ERRATUM IS OWED IN THE GOVERNING CHAIN.

## WHY THIS MATTERS BEYOND THE NUMBER

The figure was itself the headline of the scope correction — the finding that the program had
been searching a fraction of itself. It was then repeated for two days without anyone opening
the directories it counted. That is the same failure class as the `C_R` symbol collision and the
substring-certified audit flags: A VALUE PROPAGATED BY CITATION RATHER THAN BY VERIFICATION.
Recommended: add to the corpus_check candidate list a check for QUANTITATIVE CLAIMS REPEATED
ACROSS ARTIFACTS WITHOUT A PRODUCER — a figure cited in N artifacts and computed in none.

alpha_computed = false; proof_authorized = false.
