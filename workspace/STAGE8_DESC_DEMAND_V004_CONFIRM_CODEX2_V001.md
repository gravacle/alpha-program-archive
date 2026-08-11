CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY
PREDECLARATION_OUTPUT_SCAN = 0 hits
VERDICT_BEARING_SET = exactly the 15 content-addressed files below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = CODEX 2
ROLE_THIS_RELAY = OPPOSITE-LANE CONFIRMATION OF DEMAND V004
CLOSURE_END_BYTE = 2702
```

| # | Closed file | SHA-256 | Role |
|---:|---|---|---|
| 1 | `relay_inbox/RELAY_PASTE_996_DEMAND_V004_CONFIRM_CODEX2_V001.md` | `bffae3b96240ce3282d97f11855372a8daf07c517782cab40940bc43ba22241f` | assignment |
| 2 | `STAGE8_DESC_DEMAND_DARIO_V004.md` | `bed63c314a779b499fe5c7aaae46221f32fa6255778d9a6a7bb0f597c48e880e` | subject |
| 3 | `build_v004.py` | `110006d42079cb705fefd4d9e1b9f07658920ad5b9e94656e076964e9ed17e93` | executable construction under test |
| 4 | `STAGE8_DESC_DEMAND_DARIO_V003.md` | `fbf76d210bfc0981f51ead63d0e31de4c63785c845c61cc8d005100f2793e31e` | build base and diff input |
| 5 | `STAGE8_DESC_DEMAND_V003_CHECK_CODEX2_V001.md` | `ba67264055f9191e864e2757a5380a5bdbfe3d5e5104ebb77d8f2f4b047429a1` | prior opposite-lane findings |
| 6 | `STAGE8_DESC_DEMAND_DARIO_V002.md` | `c883d3732af61800f6ac2219e87406ccbbae60f7928172a80281e2e2cae951e3` | diff and set input |
| 7 | `STAGE8_DESC_DEMAND_DARIO_V001.md` | `da32dc9dfff38a32668b673e0c1b9e05fee27d02cd49b2f7ed99a78b71c51da9` | diff input |
| 8 | `<archive-root>/relay_inbox/RELAY_PASTE_995_DEMAND_V004_DARIO_V001.md` | `542e579f9ed98cfee3d03656c0d7e26f3594cdd9da83c4ea9aebd66f7700d1d7` | subject assignment and member-01 test |
| 9 | `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | state pin |
| 10 | `LOCKED_PROCESS.md` | `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb` | process law |
| 11 | `DECLINE_REGISTER_V002.md` | `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | S01-S37 flattening guard |
| 12 | `STAGE8_P5_COMMON_ORIGIN_DESCENT_REQUIREMENT_V001.md` | `a33be83c1ee7cbfbda2cc3857425cb9e7e90a23bbe3d61c9ec89432e50b77874` | integrity-sweep spot check 1 |
| 13 | `STAGE8_AXN_B0_ACCEPTANCE_INVERSE_CODEX2_V001.md` | `ae93720f5f5534a8d0d9915ab84368639f3fd96927b0d51a206a35c6b40b6019` | integrity-sweep spot check 2 |
| 14 | `STAGE8_AXN_STATE_ALGEBRA_MAP_CODEX2_V001.md` | `a67ed4352e939bd92e886672b9dfdb848cfcaa453a3760f0daa83d6586d60782` | integrity-sweep spot check 3 |
| 15 | `/opt/homebrew/opt/diffutils/bin/diff` | `1a6176bc00fc8f529eecf223a9aec75a44d89a30cf6e514e57d2ecd9d59cca6f` | GNU diffutils 3.12 replay executable |

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

CLOSURE_DECLARATION_END

# STAGE 8 — DESCENT DEMAND V004 — OPPOSITE-LANE CONFIRMATION

## 1. Verdict

**REMAINS.** The U12 demand map remains substantively closed, member 01 rehashes, the local §6.5 set
deltas are correct, and three source/span families spot-check cleanly. The sealed construction method
does not reproduce sealed V004, four of the nine replacements are wrong or incomplete, all three
claimed GNU diff triples are wrong, the `PATH_RULE` fails on three other closure files, and stale
false carriage claims remain in the final block.

These are documentary/custody failures. No demand condition, supply object, or physical result is
re-adjudicated here.

## 2. Reproducible-build execution [PROVABLE]

The sealed V003 base and script were copied byte-for-byte to an isolated temporary directory after
their seals passed:

```text
V003 input = fbf76d210bfc0981f51ead63d0e31de4c63785c845c61cc8d005100f2793e31e
script     = 110006d42079cb705fefd4d9e1b9f07658920ad5b9e94656e076964e9ed17e93
interpreter = Python 3.9.6
command     = python3 build_v004.py
```

The script completed and reported nine named replacements. Its product does **not** byte-match the
sealed subject:

| Object | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| executed build product | 683 | 44,897 | `21c07639accab8d6cf8e31c743ee2098d7e65b973915cabbb9832eabd0a59f06` |
| sealed V004 | 816 | 53,232 | `bed63c314a779b499fe5c7aaae46221f32fa6255778d9a6a7bb0f597c48e880e` |

GNU unified comparison between the generated and sealed products is five hunks, 136 insertions, and
3 deletions. The generated product:

1. leaves `CLOSURE_END_BYTE = 6784` rather than sealed V004's `7279`;
2. leaves `@@H34@@`, `@@I34@@`, and `@@D34@@` placeholders;
3. does not insert §6.6's 115-line embedded script;
4. leaves the final closure-end display at 6784; and
5. does not insert the five new final-summary lines (`DIFFS`, `METHOD`, `SET_CLAIM`, `MEMBER01`,
   `SUBSTANCE`).

Thus the sealed file contains non-scripted edits, while §6.6 says the nine replacements are the
complete difference. The method note is not reproducible as sealed.

## 3. The nine replacement texts [PROVABLE]

| R | Replacement purpose | Press result | Finding |
|---:|---|---|---|
| 1 | add `PATH_RULE` | **WRONG** | `workspace/` is not root-anchored and, under the only concrete archive-workspace reading, member-15's three files are absent; see §6 |
| 2 | replace member 01 with archive-rooted 995 assignment | **CORRECT** | exact archive-root path exists and hashes to `542e579f...` |
| 3 | extend member 02 with V003 | **CORRECT** | filename and digest match sealed V003 |
| 4 | extend member 03 with the 994 check | **CORRECT** | filename and digest match the sealed check |
| 5 | retitle V003 as V004 | **CORRECT** | version title only |
| 6 | relabel relay 993 as 995 | **CORRECT** | assignment/version label only |
| 7 | replace the diff certificate and diagnosis | **WRONG** | all three advertised GNU triples differ from GNU 3.12 replay; the `difflib` causal diagnosis is also false; placeholders prevent direct reproduction |
| 8 | replace the false V002-to-V003 set paragraph | **INCOMPLETE** | §6.5's new text is correct, but the old opposite assertion survives in the final `CLOSURE_DELTA` line |
| 9 | insert the reproducible-method paragraph | **WRONG** | it says §6.6 is reproduced and the script recreates V004, but the executed script does neither |

**Replacement result: 5/9 correct; R1, R7, R8, and R9 fail.** The unique-target assertions in the
script all pass, demonstrating the relay's own warning: correct target occurrence is not correct
replacement content.

## 4. GNU diff replay [PROVABLE]

The replay used the content-pinned GNU diffutils 3.12 executable in the closure with three context
lines. Counts begin only after a hunk header, so file headers are excluded and content lines are
counted exactly.

| Transition | V004 claim | GNU 3.12 replay | Result |
|---|---:|---:|---|
| V001 -> V002 | `2 / 372 / 347` | `2 / 382 / 357` | MISMATCH |
| V002 -> V003 | `10 / 158 / 38` | `10 / 157 / 37` | MISMATCH |
| V003 -> V004 | `7 / 183 / 16` | `8 / 185 / 18` | MISMATCH |

All replay triples preserve the sealed line-count balances `+25`, `+120`, and `+167` respectively.
V004 copied the Apple/Git unified counts displayed in the 994 check and promoted them to GNU counts.
That promotion is false.

The diagnosis of V003 is also false as written. Python 3.9.6 `difflib.unified_diff` replay gives
`2/456/431` and `10/160/40`, not V004's asserted `457/422` and `160/39`. In particular, no lawful
line diff can yield V003's imbalanced `457-422=35` over a `+25` line delta.

The old contradictory final lines were not removed: `H_TABLE` still repeats `2/457/422` and
`10/158/37`, while `CLOSURE_DELTA` still repeats that V002-to-V003 removed nothing. These stale
statements independently prevent a clean certificate even if §6.3 and §6.5 were correct.

## 5. Set deltas [PROVABLE]

Closure-file tokens were extracted from each declared closure before `CLOSURE_DECLARATION_END` and
compared as sets:

| Transition | Retained | Added | Dropped | Dropped member |
|---|---:|---:|---:|---|
| V002 -> V003 | 13 | 7 | 1 | `relay_inbox/RELAY_PASTE_989_DEMAND_V002_DARIO_V001.md` |
| V003 -> V004 | 19 | 3 | 1 | `relay_inbox/RELAY_PASTE_993_DEMAND_V003_DARIO_V001.md` |

The three V003-to-V004 additions are the archive-rooted 995 assignment, V003 itself, and the 994
check. This matches §6.5's row-level description: one assignment row replaced and rows 02/03
extended. It does not match the stale final `CLOSURE_DELTA` assertion inherited from V003.

## 6. Member 01 and `PATH_RULE` [PROVABLE]

Member 01 is sound under its explicit branch of the rule:

```text
/Users/bgm/MB Work/alpha-program-archive/relay_inbox/
  RELAY_PASTE_995_DEMAND_V004_DARIO_V001.md
= 542e579f9ed98cfee3d03656c0d7e26f3594cdd9da83c4ea9aebd66f7700d1d7
```

Its adjacent sidecar verifies.

The rule as a whole is not sound. It says unqualified names resolve in `workspace/` without
root-anchoring that directory. Under the concrete archive interpretation
`<archive-root>/workspace/`, 18 of the 21 unqualified closure files exist at their declared digests,
but these three do not exist:

```text
PROGRAM_STATE_BRIEF_V005.md
LOCKED_PROCESS.md
DECLINE_REGISTER_V002.md
```

They exist only at the cleanroom root in this custody view. Interpreting `workspace/` as the Codex
workspace root fails for every member, because the files are nested under the cleanroom. The rule
therefore supplies no single resolution that covers every unqualified member. A sound rule must
name the cleanroom root or root-anchor each exceptional file; the correct member-01 branch does not
repair the other branch.

## 7. Integrity-sweep spot check [PROVABLE]

Three closure source families were selected before rehashing. Whole-file and every cited span below
match V004's closure table:

| Artifact | Checked spans | Result |
|---|---|---|
| P5 common-origin requirement `a33be83c...` | `[2044,6922)`, `[3001,5172)`, `[6923,8531)`, `[8533,9079)` | 4/4 MATCH |
| B0 acceptance inverse `ae93720f...` | `[7262,10112)`, `[10112,12021)`, `[12021,13587)`, `[13587,19040)` | 4/4 MATCH |
| state-algebra map `a67ed435...` | `[16298,17631)`, `[17244,17540)` | 2/2 MATCH |

The scoped spot check is clean. It does not validate V004's broader stale sentence “all 14 members”:
the V004 closure has 16 numbered rows and 22 file tokens, and the new path rule fails on three of
them as described above.

## 8. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT   = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the relay-996 checklist; sealed V001-V004 bytes; sealed build_v004.py; the 994 findings; the
  root-anchored 995 assignment; the three integrity-sweep source families; state/process/decline
  laws; all standard gates.

DERIVED HERE:
  the isolated build-product digest and byte comparison; per-replacement findings; three GNU-diff
  triples; two exact closure-set deltas; member-01 resolution; failure of the other PATH_RULE branch;
  ten source-span rehash results.

SELECTED HERE:
  nothing. No descent object, candidate, trace, map, certificate instance, manifest, state, measure,
  `omega_phys`, acceptance branch, or release route is constructed, supplied, selected, or scored.

SCALING WEIGHTS:
  none consumed, fixed, formed, compared, or substituted.
```

## 9. Flattening, blind, and custody

- **F_PLDEC:** only sealed-byte hashing, scripted text replacement, exact comparison, line-diff
  accounting, file-path resolution, and finite set comparison were executed.
- **FLATTENING CHECK:** unique replacement targets are not flattened into correct replacement text;
  Apple/Git unified counts are not flattened into GNU counts; a locally correct §6.5 paragraph is not
  flattened into document-wide correction while the opposite final line survives; one sound
  root-anchored member is not flattened into a sound rule for every unqualified member; a script
  printed inside its alleged product is not flattened into a script that actually emits that product.
- **ANTI-TUNING:** the build ran before its product was compared; GNU was installed and pinned rather
  than inferred from the platform `diff`; each set and span result follows the sealed bytes.
- **BLIND HELD:** no rank, ratio, response value, fiber value, physical quantity, or measured constant
  was read, formed, evaluated, or compared. All scales remain symbolic.
- **PE-1..PE-16:** pointer-only, zero verdict weight.
- **BUILDER-NEVER-VERIFIES:** this opposite lane verifies Dario's V004 and constructs no demand or
  supply object.
- **PIN CHECK:** the relay, subject, script, state brief, prior sealed references, and the 995 archive
  assignment passed their seals before semantic use. Output and sidecar names were absent before
  authoring.
- **DOES NOT DO:** no member binding, fixed-point execution of the physical program, end test, chain
  invocation, proof authorization, numeric evaluation of a physical quantity, or comparison to a
  measured constant.

Verb audit: **CLEAN.** “Executed” refers to the documentary build script and diff tooling only;
“replayed” refers to finite text diffs. No physical execution, supply verdict, or member binding is
claimed.

CLOSURE = declared-first (byte 0; closure end 2702; scan 0 hits)
BUILD = DIVERGES (5 hunks; generated 44897 bytes vs sealed 53232 bytes)
REPLACEMENTS = 5/9-CORRECT (R1, R7, R8, R9 wrong or incomplete)
DIFFS = 3/3-REPLAYED (GNU: 2/382/357; 10/157/37; 8/185/18; all differ from V004)
SET_DELTAS = RECOMPUTED-MATCH (13/7/1 and 19/3/1; stale final contradiction remains)
MEMBER01+RULE = MEMBER01-SOUND / RULE-UNSOUND (three unqualified members unresolved)
SWEEP = SPOT-VERIFIED (3 artifacts; 10 spans; all match)
VERDICT = REMAINS (non-reproducible build; wrong GNU triples; incomplete replacements; unsound path rule)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
