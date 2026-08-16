# STAGE 8 — DEFAULT-REFUTE AUDIT OF `STAGE8_TYPER_ESCAPES_O46SR_V001.md` — O46SR AUDIT V001

## AUDIT LANE — DEFAULT VERDICT REFUTED — 2026-08-16

```text
alpha_computed        = false [TERMINAL_FENCE_DECLARATION]
proof_authorized      = false [TERMINAL_FENCE_DECLARATION]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION]
```

TARGET `/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_TYPER_ESCAPES_O46SR_V001.md`
TARGET SHA-256 `0372e2937c408058dcb955a2f003d01551dd987f1c8aace7f1114d2af506e78c` — recomputed
by this lane from the artifact's own directory, matches the build's claim.

---

## 0. OVERALL GRADE — **CONFIRMED-WITH-CORRECTIONS**

The default verdict is REFUTED and this lane worked to sustain it. It could not.

The build's population ladder is the most reproducible this lane has audited. Re-derived
independently, from a corpus enumerated by this lane's own globs, with this lane's own
regexes: **L0a 812 exact · L1 4,602 exact · L2 1,944 exact · L4 157 exact · L5 54 exact
by SET EQUALITY of all 54 names · L7 19 exact · L7a 49 exact · the 35 exact.** Every
quoted span this lane checked reproduces verbatim at bytes with its adverse clauses
intact — zero early closures, which is the program's most-repeated defect and the build
did not commit it. Seals 7/7 OK and sidecars 2/2 OK, re-verified here.

**But one dimension is REFUTED,** and it is the one carrying half the headline. Every
row in the build's §6.2 MATCHED table is graded against a "consumer" that the build's
own Q3 denominator rule excludes. The Q3 conclusion **survives** this lane's independent
re-derivation — 0 consumers widen — but the itemised evidence displayed for it is void,
and the build's own §7.2 paragraph claims a reconciliation it did not perform.

| # | Dimension | Grade |
|---|---|---|
| 1 | Population and sampling | **CONFIRMED-WITH-CORRECTIONS** |
| 2 | Every graded row | **CONFIRMED-WITH-CORRECTIONS** |
| 3 | Quotation integrity | **CONFIRMED** |
| 4 | Second-hand reliance | **CONFIRMED-WITH-CORRECTIONS** |
| 5 | Headline versus evidence | **REFUTED** |
| 6 | Bars | **CONFIRMED** |

---

## 1. CHOICE LEDGER

| # | Choice | Alternative not taken | Why |
|---|---|---|---|
| A1 | **Re-enumerate the corpus from scratch** with this lane's own `find` + BAR array rather than trusting the build's 5,949. | Accept the declared file list. | An undeclared or wrong population makes every tally meaningless. The dimension says check first. |
| A2 | **Re-extract with independently written regexes**, not the build's. | Re-run the build's stated patterns. | Reproducing a build's own regex reproduces its blind spots. Writing fresh is what found COR-B. |
| A3 | **Spread computed over MENTIONS (token match), not typings.** | Substring match, as `rg -F` would give. | The build's C4 says "appears in ≥2 basenames". Token match is the stricter, less inflating reading; it reproduced 157/54 exactly, so the choice is validated by agreement. |
| A4 | **Grade the Q3 population by the build's own stated rule** ("mentions the flag without itself typing it") and test each cited consumer against it. | Accept the build's row assignments. | This is the whole of COR-A. The rule is the build's; applying it is not a new standard. |
| A5 | **Read all 19 rows' real non-typing consumers by eye**, not only by pattern sweep. | Rely on the widening-token sweep alone. | A sweep cannot see widening phrased outside its 14 patterns. The eye-read is what confirmed 0 widening independently, and what found the two genuine MATCHED rows the build missed. |
| A6 | **Report the Q3 conclusion as SURVIVING** even though its displayed support is void. | Refute the conclusion along with its evidence. | Bad evidence for a true claim is a correction, not a refutation. This lane re-derived the claim itself and it holds. |
| A7 | **Grade E2–E5 down to INDETERMINATE-AT-BYTES rather than reversing to CLEAN.** | Call them CLEAN, or leave them NAMES-AN-ESCAPE. | Bytes show the adjacent theorem addresses different predicates. Bytes do not show the source closing the alternatives either. INDETERMINATE is what bytes decide. |

---

## 2. CORPUS, BAR, IMPORT AUDIT

### 2.1 Roots entered — identical to the build's, independently enumerated

```text
ROOT A  /Users/bgm/MB Work/alpha-program-archive/workspace
ROOT B  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
        alpha_fundamental_record_action_cleanroom_v003
PLUS    DOR_* under /Users/bgm/MB Work/alpha-program-archive/supervision/
        (directory listing enumerated only; no non-DOR file opened)
```

**Note on the build's §2.1.** The build's ROOT B line reads `.../alpha_fundamental_record_action_cleanroom_v003`
and its build report abbreviated it as sitting beside ROOT A. It does not — it is under
`/Users/bgm/Documents/New project/...`. The build's artifact §2.1 states the correct full
path; only the relay summary was loose. No count depends on it.

### 2.2 REGISTER BAR — exclusion globs as an ARRAY, per-pattern leak counter

```zsh
typeset -a BAR
BAR=('*REGISTER*' '*TRACKER*' 'THE_PLAN*' 'ROAD_REMAINING*' 'THE_HANDOFF*'
     'OBSERVATIONS_REGISTER*' '*DECISION_SHEET*'
     'STAGE8_TYPER_ESCAPES_O46SR_AUDIT_V001.md')
```

Leak counter, run against this lane's permitted list after construction:

```text
PATTERN                                  | LEAKS_IN_PERMITTED_LIST
*REGISTER*                               | 0
*TRACKER*                                | 0
THE_PLAN*                                | 0
ROAD_REMAINING*                          | 0
THE_HANDOFF*                             | 0
OBSERVATIONS_REGISTER*                   | 0
*DECISION_SHEET*                         | 0
STAGE8_TYPER_ESCAPES_O46SR_AUDIT_V001.md | 0   [SELF-EXCLUDED]
STAGE8_TYPER_ESCAPES_O46SR_V001.md       | 0   [target; excluded from sweeps, read only as target]
```

`QUESTIONSSETTLED_REGISTER_V001.md` **exists** at
`/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/QUESTIONSSETTLED_REGISTER_V001.md`,
is caught by `*REGISTER*`, occurs **0 times** in this lane's permitted list, and was
never opened. The build's identical claim is **verified true**.

### 2.3 IMPORT AUDIT — what this lane took from outside its own reading

| Import | Source | Status |
|---|---|---|
| The four-type definitions (`TYPE-R`/`TYPE-U`/`TYPE-S`/`TYPE-C`) | The build's §3.2, itself quoting `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:136-147`, itself quoting `NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md` outside the corpus | **SECOND-HAND (third-hand).** Not load-bearing on any grade in this audit; no grade here turns on the definition of TYPE-U or TYPE-S. |
| The FP-2 / C6 confirmed instance | `STAGE8_CERTIFICATION_RULES_O8SR_V001.md:543-548` and `STAGE8_CERTIFICATION_RULES_O8SR_AUDIT_V001.md:426-431` | **PRIMARY** — both opened and read whole at bytes by this lane. |
| The E1 spec v002 behind FP-2 | not in the permitted corpus | **SECOND-HAND.** Not relied on: this audit's §7 finding concerns whether the barrier is TYPE-R-typed, which is decided in-corpus. |
| `T_R_and_k_R_have_derived_bridge` origin (`BOHM_GR_EM_RELATION_REFUTED:52`) | outside the permitted corpus | **SECOND-HAND.** The build's INDETERMINATE grade is sustained; see §6. |
| Logic used | Set difference and set equality over basenames; token-boundary regex; the standard reading of a restrictive relative clause. No mathematics of the object domain. | Named. |

**No numeric value of any coupling, scale, root, eigenvalue, norm or constant was
computed, approached, or transcribed anywhere in this artifact.**

---

## 3. DIMENSION 1 — POPULATION AND SAMPLING — **CONFIRMED-WITH-CORRECTIONS**

### 3.1 The ladder, re-derived at bytes

Every number below was produced by this lane's own enumeration and its own regexes,
without reading the build's scripts.

```text
RUNG  QUANTITY                                   BUILD    THIS AUDIT   VERDICT
──────────────────────────────────────────────────────────────────────────────
L0    permitted files (.md/.txt/.json, BAR)      5,949    5,950        off by 1 (COR-G)
L0a   files containing token TYPE-R                812      812        EXACT
L0b   occurrences of token TYPE-R                6,452    6,453        off by 1 (COR-G)
L1    typed-negative sites, forms 1+2            4,602    4,602        EXACT
        of which single-line                     4,574    4,574        EXACT
        of which value-on-next-line                 28       28        EXACT
L2    distinct identifiers, forms 1+2            1,944    1,944        EXACT
        multi-line-only identifiers                 10       10        EXACT
L4    spread >= 2 by basename (mentions)           157      157        EXACT
L4a   boilerplate/common-word removals              11       11        EXACT
L5    ADJUDICATED SET, spread >= 3                  54       54        EXACT — SET EQUALITY
L5r   DECLARED RESIDUE, spread == 2                103       92        WRONG (COR-C)
L7    rows with >=1 non-typing artifact             19       19        EXACT (under build's rule)
L7a   rows typed in >= 2 artifacts                  49       49        EXACT
      rows with zero non-typing consumer            35       35        EXACT
```

**The 54 are set-equal.** This lane built its adjudicable set from spread ≥ 3 with the
11 boilerplate and the wrap fragments removed, then compared name-by-name against the
build's 32 NAMES-AN-ESCAPE + 3 CLEAN + 8 INDETERMINATE + 11 NOT-A-BARRIER:

```text
IN THIS AUDIT NOT IN THE BUILD : []
IN THE BUILD NOT IN THIS AUDIT : []
SET EQUAL                      : True
```

**The population is real and it was not silently sampled.** The spread-2 cutoff is
declared at C6, at S9 and at §7.3, the residue is counted, and no row is dropped without
a name. On the dimension's own terms — "Is the declared population real? Did the build
sample without saying so?" — the answer is yes and no respectively.

The 11 boilerplate removals were each re-verified at bytes by mention-spread, and every
one is a genuine template/common-word token, not a suppressed barrier:

```text
PASS 833 · FENCE_BLOCKED_STRUCTURAL_RESULT 142 · ARE_ITS_INPUTS_PRESENT 100
ARE_THE_INPUTS_PRESENT 53 · Tail_R 58 · TARGET_TUNING_USED 16 · ARE_INPUTS_PRESENT 7
B5_DISCHARGED 4 · B6_DISCHARGED 4 · B9_DISCHARGED 4 · RELAY_ARE_INPUTS_PRESENT 3
```

### 3.2 COR-C — the residue is 92, not 103

**Deciding file:line — `STAGE8_TYPER_ESCAPES_O46SR_V001.md:220` and `:731`.**

The build removes 11 boilerplate identifiers from the 157 at L4a, leaving 146. It then
reports the spread-2 residue as **103**. But `54 + 103 = 157`, which re-admits the 11 it
had just removed. The arithmetic that closes is:

```text
157  (spread >= 2)
 -11 (boilerplate, L4a — all of them at spread >= 3, verified above)
 -54 (adjudicated, spread >= 3)
 = 92  <-- the true residue
```

This lane's direct count of spread-2 identifiers with boilerplate and wrap fragments
removed is **92**, independently confirming the subtraction.

**Consequence.** S9's extrapolation — "If NAMES-AN-ESCAPE runs at the same 74% there,
roughly 76 further barriers sit beside a named door" — is arithmetic on the wrong
residue. At 92 the same (explicitly hypothetical) figure would be roughly 68. The build
correctly flags this as "arithmetic on an unread set and it is stated as such, not
claimed", so nothing load-bearing rests on it. It is nonetheless exactly the COUNT
HYGIENE failure the standing discipline names: two counts over different populations.

### 3.3 COR-B — a third flag form the build never handled

**Deciding file:line — `STAGE8_7A_EMPTY_CHAMBER_DARIO_V001.md:144-145`, whole span:**

```text
[PROVABLE] **(e) The route by derivation-from-the-clause is barred.** `4d`
`430f0971…[20690,20930)`: `C_REF_AS_WRITTEN_DERIVES_SMOOTH_DATA_FROM_GATE4 = false |
TYPE-R`.
```

The build's C2 corrected for one wrap form (`IDENT =` ⏎ `false | TYPE-R`, its own defect
D1, 10 identifiers recovered). The corpus also writes a **third** form the build never
searched for: **`IDENT = false |` ⏎ `TYPE-R`**. Swept over the permitted corpus:

```text
FORM 3   'IDENT = false |' EOL + 'TYPE-R'   sites 38   identifiers 19
FORM 4   'IDENT = false' EOL + '| TYPE-R'   sites  0   identifiers  0
```

Of the 19, **13 are real identifiers absent from the build's 1,944** (one further hit,
`_implies_full_source_determination`, is itself a wrap fragment of
`P5_common_origin_descent_implies_full_source_determination` and is removed).

This is the same mid-sentence line-wrap hazard the standing discipline names, and the
same one the build itself caught twice in its own draft (D1, D3). It escaped a third time.

**Three consequences, in rising order of severity.**

**(i) The counting rungs shift.** L1 → 4,640 sites. L2 → 1,958 identifiers. L3 → ~1,952
after wrap removal. None of these is load-bearing on any tally.

**(ii) One barrier row is missing from the adjudicated set.** Exactly one Form-3
identifier reaches mention-spread ≥ 3:

```text
NONTRIVIAL_ONE_SIDED_CONTACT_FROM_DECLARED_OPEN_HOLONOMY_EXISTS   spread 3
  typed  STAGE8_SOURCE_COUPLED_RECORD_TRANSITION_LAW_ADOPTION_PROPOSAL_V002.md:157-159
  typed  STAGE8_SOURCE_COUPLED_RECORD_TRANSITION_LAW_ADVERSARIAL_KILL_DETERMINATION_V001.md:558-560
  consumed (non-typing)  STAGE8_TWIST_EVIDENCE_O40SR_V001.md:1105
```

Its typing site, whole:

```text
NONTRIVIAL_ONE_SIDED_CONTACT_FROM_DECLARED_OPEN_HOLONOMY_EXISTS = false |
  TYPE-R |
  test: covariance functional equation plus C(1)=I
```

So **L4 = 158, L5 = 55**, and the Q2 denominator gains a genuine barrier. Its grade is
settled in §5.3 below.

**(iii) Two rows leave the Q3 denominator.** Because Form 3 is a typing, the two
artifacts the build treated as *non-typing consumers* are in fact typing artifacts:

```text
C_REF_AS_WRITTEN_DERIVES_SMOOTH_DATA_FROM_GATE4
  + STAGE8_7A_EMPTY_CHAMBER_DARIO_V001.md                          becomes TYPING
EPOST_ENDPOINT_ORIENTATION_EQUALS_INTERACTING_I_EPSILON_PRESCRIPTION
  + STAGE8_TASK4A_P3_SECOND_ATTACK_LAW_SIDE_CONSTRUCTION_AND_NARROWED_STOP_V001.md:358
                                                                    becomes TYPING
```

Both rows' non-typing consumer sets become empty. **L7 = 19 − 2 + 1 = 18.**

### 3.4 COR-G — two off-by-one counts

`L0` 5,949 → **5,950** and `L0b` 6,452 → **6,453**. The L0 slip is fully explained and
benign: `STAGE8_RESERVATION_UNION_O46SR_V001.md` was written into ROOT A at 02:42, ten
minutes before the target artifact at 02:52, so the build enumerated before it existed.
It contains 0 occurrences of `TYPE-R`, so it does not explain the L0b slip, which
remains a 1-in-6,453 unexplained residue (0.015%). Nothing rests on either.

---

## 4. DIMENSION 3 — QUOTATION INTEGRITY — **CONFIRMED**

This is the program's most-repeated defect and the dimension this lane attacked hardest.
**Zero early closures and zero dropped adverse clauses were found.** Every span below
was opened at its cited file and line, read past its closing quotation mark, and
wrap-checked.

| Build § | Cited span | Verified at bytes |
|---|---|---|
| §3.1 mandate | `STAGE8_ACCESSOR_THEOREM_SUBSTITUTION_ADJUDICATION_EINSTEIN_V001.md:346` | verbatim |
| §5.1 E1 | `STAGE8_7A_COMPLETENESS_PROOF_DARIO_V001.md:18-23` | **verbatim, whole.** "barred as a SOURCE … not excluded from the CLASS" is complete; the qualifier "as a source" is present; the closing sentence "it does not delete the moves from the class it froze" is present |
| §5.1 E2–E5 | `STAGE8_7A_DBR_SPECTRUM_DARIO_V001.md:188-203` | **verbatim, whole.** Flag block at :189-192, "and one positive theorem, conditional:" at :195, TYPE-C block at :198-203, all exact |
| §5.1 E6 | `STAGE8_COMPOSITION_LOOP_STRUCTURAL_PREDICTION_BUILD_V001.md:55-60` | **verbatim.** `K_square_forced_if_commuting_two_handle_diamond_is_supplied = true | CONDITIONAL` present on the line after the flag, as claimed |
| §5.4 P5 guard | `STAGE8_P5_COMMON_ORIGIN_DESCENT_REQUIREMENT_V001.md:149-150` | **verbatim, whole**, including the adverse final sentence "'Some source exists' or 'all fields appear in one file' is insufficient." |
| §6.1 representative 1 | `STAGE8_LEGENDRE_ACTION_PHYS_ADOPTION_PROPOSAL_V002.md:831-838` | **verbatim.** "universal" does belong to `closure_uniqueness_proved`, not `restriction_square` |
| §6.1 representative 2 | `STAGE8_TASK4A_FAMILY_NATURAL_PREFIX_TO_CYCLE_DESCENT_LANE2_V002.md:874-881` | **verbatim.** "impossible" does belong to `upward_square`, and the wrap across :879-880 is correctly reproduced |
| §6.2 consumer | `STAGE8_SECTOR_REACH_REQUIREMENT_V001.md:518-519` | **verbatim**, including the wrap "does not / by itself imply sector reach" |
| §6.2 consumer | `STAGE8_DESC_B03_DARIO_V001.md:302-304` | **verbatim, whole** |
| §6.2 consumer | `STAGE8_REQUIRE_G3_CHECK_V001.md:179-181` | **verbatim, whole**, "of record" thrice as claimed |
| §6.2 consumer | `STAGE8_7A_DBR_PUBLIC_LAYER_DARIO_V001.md:243` and `:247` | **verbatim** |
| §6.5 barrier | `STAGE8_CERTIFICATION_RULES_O8SR_V001.md:543-548` | **verbatim, whole** |
| §6.5 corroboration | `STAGE8_CERTIFICATION_RULES_O8SR_AUDIT_V001.md:426-431` | **verbatim, whole**, including "I could not break it." |

The build's handling of the E11 quotation deserves specific credit against the dimension:
it reproduces the quoted artifact's own citation of a **barred register** rather than
truncating the span to hide it, and then declares at §9.3 that the register was not
opened. That is the correct disposition of the conflict between quotation integrity and
the bar, and this lane confirms the register was not opened by either lane.

---

## 5. DIMENSION 2 — EVERY GRADED ROW — **CONFIRMED-WITH-CORRECTIONS**

### 5.1 COR-D — the sub-kind split contradicts the build's own itemisation

**Deciding file:line — `STAGE8_TYPER_ESCAPES_O46SR_V001.md:471`, repeated at `:658-659`.**

The build states **"CLASS-DISPLAYED-VIABLE 14, WOULD-BUILD-NAMED 18"**. Counting the
sub-kind labels the build itself attaches to E1–E32 in §5.1:

```text
CDV  E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11, E12, E16, E17, E19, E25   = 16
WBN  E13, E14, E15, E18, E20, E21, E22, E23, E24, E26, E27, E28, E29,
     E30, E31, E32                                                            = 16
TOTAL                                                                          32
```

The split is **16 / 16**, not 14 / 18. The total of 32 is unaffected. This matters
because C8 justifies the split precisely on the ground that "The commission's confirmed
instance is the first kind … most corpus rows are the second" — at bytes of its own
itemisation, the two kinds are **equinumerous**, and the stated asymmetry that motivated
the split does not exist.

### 5.2 COR-F — E2–E5, four of the 32, escape to a different predicate

**Deciding file:line — `STAGE8_7A_DBR_SPECTRUM_DARIO_V001.md:183` against `:198-203`.**

The build grades four barriers CLASS-DISPLAYED-VIABLE on one adjacent block, and
writes: *"Four negatives, and the very next line names the regime that works."* The
quotation is exact (§4 above). The **grade** is not supported.

The four refuted predicates are about the **public** (quotiented) layer:

```text
Phi_dagger_Phi_forces_uniform_positive_public_gap       = false | TYPE-R
parent_Casimir_forces_uniform_positive_public_gap       = false | TYPE-R
unquotiented_skeleton_satisfies_public_cardinality_one  = false | TYPE-R
compact_topology_forces_simple_public_bottom            = false | TYPE-R
```

The adjacent positive theorem is about the **raw** skeleton, and its conclusions are
compact resolvent and isolated spectral clusters:

```text
raw_BR_skeleton_compact_resolvent_theorem      = true | TYPE-C | condition: …
raw_BR_skeleton_has_isolated_spectral_clusters = true | TYPE-C
```

Compact resolvent on the raw skeleton is not a uniform positive **public** gap, nor
public cardinality one, nor a simple public bottom. Decisively, the same source block
states the public gap question is **open**, five lines above the flags —
`STAGE8_7A_DBR_SPECTRUM_DARIO_V001.md:183`, whole line:

```text
complete_public_BR_gap_exists_by_structure           = NO_VERDICT
```

A source that types the very quantity at `NO_VERDICT` is not naming a class that delivers
it. The block is a **status inventory** — "and four shortcuts already refuted … and one
positive theorem, conditional" — not a door drawn beside a wall.

Bytes do not establish an escape. Bytes also do not establish that the source closes the
alternatives. **Corrected grade for E2–E5: INDETERMINATE-AT-BYTES**, per the standing
discipline. This moves 4 rows from the Q2 numerator to the INDETERMINATE bucket.

**A structural note the build should have made.** The 32 are not 32 independent findings.
E2–E5 share one block; E22/E23 share one block; E26/E27/E28 share one block; E24/E25
share one file. Fourteen of the 32 rest on four pieces of text. The build discloses the
shared sources honestly in its table, but never says what the concentration means for
the ratio.

### 5.3 The row the build missed — graded here

`NONTRIVIAL_ONE_SIDED_CONTACT_FROM_DECLARED_OPEN_HOLONOMY_EXISTS` (§3.3) is a genuine
barrier: it refutes the existence of a nontrivial one-sided contact from declared open
holonomy. Its consumer displays the source's own scope limit —
`STAGE8_TWIST_EVIDENCE_O40SR_V001.md:1104-1108`, whole span:

> with the result block at `:149-160` including
> `NONTRIVIAL_ONE_SIDED_CONTACT_FROM_DECLARED_OPEN_HOLONOMY_EXISTS = false`
> and the scope limit at `:162-165`: "It does not quantify over a different
> endpoint-charge package or over new parent, curvature, closed-loop, state,
> effect, metric, continuum, or contact data."

The source names the data classes it does **not** quantify over. **Grade:
NAMES-AN-ESCAPE (CLASS-DISPLAYED-VIABLE).** It is also a Q3 row, and its consumer
narrows explicitly — **MATCHED**, not consumer-wider.

### 5.4 What survives unchanged

The other 28 NAMES-AN-ESCAPE grades, the 3 CLEAN grades, the 8 INDETERMINATE grades and
the 11 NOT-A-BARRIER exclusions were checked against their cited spans and this lane
sustains them. Two are worth naming because they cut against the build's own thesis and
the build reported them anyway:

- **C7 / §5.4.** Removing 11 barrier-*removing* TYPE-R rows from the numerator is
  correct and costs the build 11 easy points. `P5_logically_requires_unique_complete_origin = false | TYPE-R`
  at `STAGE8_P5_COMMON_ORIGIN_DESCENT_REQUIREMENT_V001.md:145-146` does remove a
  requirement rather than impose one. Sustained.
- **DOR_013_RATIFICATION_READY graded CLEAN.** Sustained, and correctly scoped: the
  build says "Closed for V002 as written," and at bytes the flag is `= true` in a later
  artifact (`STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_V003_ADVERSARIAL_REVIEW_DETERMINATION_V001.md:572`).
  A lane looking to inflate its escape count would have graded this NAMES-AN-ESCAPE. It
  did not.

---

## 6. DIMENSION 4 — SECOND-HAND RELIANCE — **CONFIRMED-WITH-CORRECTIONS**

The build's SECOND-HAND labelling is accurate and, where it matters, conservative. Three
of the eight INDETERMINATE rows are marked SECOND-HAND and **none is load-bearing**: they
sit in the INDETERMINATE bucket, which by construction supports no claim.

| Item | Load-bearing? | This lane's finding |
|---|---|---|
| Four-type definitions (protocol file outside corpus) | **No** | No grade in the build or this audit turns on them. Correctly marked. |
| `T_R_and_k_R_have_derived_bridge` (`BOHM_GR_EM_RELATION_REFUTED:52`) | **No** | Correctly marked; graded INDETERMINATE, supports nothing. **Correction:** the build says it is reached only out-of-corpus, but it has three in-corpus non-typing consumers — `STAGE8_INSIDE_OUTSIDE_CONSISTENCY_CONDITION_EINSTEIN_V001.md:192`, `STAGE8_MARGINALITY_ENERGY_PHRASING_ADJUDICATION_EINSTEIN_V001.md:230`, `STAGE8_PROSE_FLAG_DEPENDENCY_EXTRACTION_V001.md:107`. The INDETERMINATE grade stands (the *typing origin* is out of corpus) but the row was reachable for Q3 and was not used. |
| `CANONICAL_SCALAR_F_N_FROM_RECORD_SANDWICH_ALONE`, `public_trace_rule_satisfied` | **No** | Correctly marked SECOND-HAND and graded INDETERMINATE. |
| E1 spec v002 behind FP-2 | **No** | The §6.5 finding is decided in-corpus by a byte sweep, not by the spec. Correctly marked. |

**One bar-adjacent observation, reported not acted on.**
`STAGE8_PROSE_FLAG_DEPENDENCY_EXTRACTION_V001.md:107` cites `supervision/EXECUTION_TRACKER.md:78`
— a **barred** filename pattern. This is the quoted artifact's own citation inside the
permitted corpus. Neither the build nor this lane opened it. No content from it is
relied on here.

---

## 7. DIMENSION 5 — HEADLINE VERSUS EVIDENCE — **REFUTED**

### 7.1 COR-A — every §6.2 MATCHED row is outside the Q3 denominator

**Deciding file:line — `STAGE8_TYPER_ESCAPES_O46SR_V001.md:574-580`, judged against the
build's own rule at `:236`.**

The build defines its Q3 denominator at `:236`, whole sentence:

> Only **19** have an artifact that mentions the flag *without* itself typing it.

That rule is correct, this lane reproduced the 19 exactly, and the build is right to
insist on it over 49 or 54. **The build then grades seven MATCHED rows against
consumers that fail it.** For each §6.2 row, the artifact cited as CONSUMER, and whether
that artifact types the flag itself:

| §6.2 row | Cited "consumer" | Types the flag? |
|---|---|---|
| `route4_existing_skeleton_reaches_external_continuum_sector` | `STAGE8_SECTOR_REACH_REQUIREMENT_V001.md:518` | **YES** — and the build knows: its own D1 says it found the multi-line form by "reading `STAGE8_SECTOR_REACH_REQUIREMENT_V001.md` at bytes and noticing its flags were absent from my own list" |
| `UNIQUE_SCALARIZATION_FORCED` | `STAGE8_DESC_B03_DARIO_V001.md:302` | **YES** |
| `UNIQUE_SCALARIZATION_FORCED` (2nd) | `STAGE8_REQUIRE_G3_CHECK_V001.md:179` | **YES** |
| `unquotiented_skeleton_satisfies_public_cardinality_one` | `STAGE8_7A_DBR_PUBLIC_LAYER_DARIO_V001.md:243` | **YES** — the cited line *is itself the typing*: it writes `unquotiented_skeleton_satisfies_public_cardinality_one = false \| TYPE-R` inside the table cell |
| `Phi_dagger_Phi_…` + `parent_Casimir_…` | `STAGE8_7A_DBR_PUBLIC_LAYER_DARIO_V001.md:247` | **YES** |
| `strict_untrapped_inequality_alone_selects_unique_scale` | `STAGE8_MARGINALITY_ENERGY_PHRASING_ADJUDICATION_EINSTEIN_V001.md:176` | **YES** |
| `C_REF_AS_WRITTEN_DERIVES_SMOOTH_DATA_FROM_GATE4` | `STAGE8_7A_COMPLETENESS_PROOF_DARIO_V001.md:18,22-23` | **YES — and it is the barrier's own SOURCE**, the identical file and lines the build cites as the source at E1 |

**Zero of seven** are drawn from the Q3 population. Three of them
(`unquotiented_skeleton_satisfies_public_cardinality_one`,
`Phi_dagger_Phi_forces_uniform_positive_public_gap`,
`parent_Casimir_forces_uniform_positive_public_gap`) have **empty** non-typing-consumer
sets — they belong to the 35 CANNOT-DETERMINE, by the build's own count, and cannot
carry a Q3 grade at all. The last row is not a consumer comparison at all: it compares
the source with itself.

This is precisely the failure the standing discipline names — *"Different populations
make a comparison rhetorically strong and arithmetically empty"* — committed inside the
section that exists to prevent it, and by a lane that caught the same error in its own
denominator at D4.

### 7.2 COR-E — the MATCHED tally disagrees with its own table

**Deciding file:line — `STAGE8_TYPER_ESCAPES_O46SR_V001.md:672` against `:574-580`.**

§7.2 reports **MATCHED 6**, and §7.3 says "the **6** rows I read whole all came back
MATCHED". The §6.2 table contains **7 rows** naming **7 distinct barriers** (the two
`UNIQUE_SCALARIZATION_FORCED` rows share a barrier, but the row at :578 names two
distinct barriers). The build never reconciles 6 against 7. The arithmetic
`6 + 13 = 19` in §7.2 is internally tidy and externally unsupported.

### 7.3 The reconciliation paragraph is itself unsound

`:679-686` is headed **"Reconciliation against my own sweep block, as required before
sealing."** It reconciles the sweep (17 raw, 0 genuine) against the headline, which is
sound. It then asserts "the 6 rows I read whole all came back MATCHED" as positive
support. Those rows are the void ones. The build checked its headline against its sweep
and did **not** check its itemised rows against its own denominator. That is the
dimension's question — "Report any disagreement it failed to reconcile" — and this is
the answer.

### 7.4 What survives: the Q3 conclusion itself — independently re-derived, **0**

The build's conclusion is **not** refuted. This lane re-ran the widening hunt from
scratch over the corrected population and by eye.

**(a) Pattern sweep, re-run.** 14 widening patterns, ±4-line window, over every
non-typing consumer of the adjudicated set:

```text
RAW HITS                                              11   (build reported 17 — COR-H)
  of which on the identifier `restriction_square`     11
  of which genuine citations of the TYPE-R flag        0
GENUINE CONSUMER-WIDER ROWS                            0
```

All 11 were opened. All are the false positive the build correctly diagnosed:
`restriction_square` is a template field in a door-verdict tuple; "universal" attaches to
`closure_uniqueness_proved` (9 hits) and "impossible" to `upward_square` (2 hits). The
build's count of 17 is not reproducible here, but its **finding is exactly right** and
its two representative spans are verbatim at bytes.

**(b) Eye-read of every real consumer.** Because a 14-pattern sweep cannot see widening
phrased outside it, this lane opened the actual non-typing consumer context for all
19 rows. **None widens.** Several narrow explicitly, and two are genuine MATCHED rows
the build never found:

- `K_square_forced_by_general_composition` — `STAGE8_GLUED_TOPOLOGY_CHECK_V001.md:128-130`,
  a genuine non-typing consumer, quoting the source whole: *"the loop is only
  **permitted** — **not forced** — by the sealed composition law"*. Explicit narrowing.
- `NONTRIVIAL_ONE_SIDED_CONTACT_FROM_DECLARED_OPEN_HOLONOMY_EXISTS` — the row the build
  missed entirely (§5.3), whose consumer reproduces the source's scope limit verbatim.
- `NEW_FREE_STATE_SLOT_FOUND` / `HIDDEN_ANCHOR_SELECTION_FOUND` /
  `CONDITIONAL_ROWS_QUIETLY_UPGRADED` — `STAGE8_SOURCE_GERM_PHYS_V003_CONFIRMATION_REVIEW_DETERMINATION_V001.md:153-155`
  reviews each typing and narrows it in the review column: *"correct **inside a fixed
  base**; A0 is explicit rather than hidden"*, *"correct: anchor tags do not enter the
  germ formula"*, *"correct: B5/B6/B9 remain conditional"*.
- Several rows' only non-typing "consumers" are **bare keyword lists**, not statements —
  e.g. `route4_existing_skeleton_reaches_external_continuum_sector` at
  `STAGE8_ONE_SEAM_OR_THREE_SEAMS_ADJUDICATION_V001.md:356` and
  `STAGE8_P5_SECTOR_ASSIGNMENT_V001.md:108` are lines inside a `text` block of search
  terms. They cannot widen anything, and they cannot match anything either.

**CONSUMER-WIDER-THAN-SOURCE = 0** is **CONFIRMED at bytes** over the corrected
population of 18. The build's headline half — *"CONSUMER-WIDER is RARE — 0"* — stands.
Its displayed support does not.

### 7.5 The structural finding — **CONFIRMED at bytes**

The build's §6.5 claim is the one this lane most expected to break, and it holds exactly.
Re-run independently:

```text
files containing "Shale-Stinespring"                             25   (build 25) EXACT
files containing "FP-2"                                          33   (build 33) EXACT
occurrences of TYPE-R within +-5 lines of any "Shale-Stinespring"  0   (build  0) EXACT
```

The commission's one confirmed consumer-wider instance carries **zero** TYPE-R typing in
the permitted corpus. The build's reading — that this is the boundary of TYPE-R's
coverage rather than a defect of TYPE-R, and that the exposure lives at barriers which
never entered the typing protocol — is supported by bytes. This lane adds nothing and
subtracts nothing from it.

---

## 8. DIMENSION 6 — BARS — **CONFIRMED**

```text
FENCES                          alpha_computed=false, proof_authorized=false,
                                kappa_record_computed=false — HELD in the target and here.
                                No value computed or approached by either lane.
NUMERIC BOUNDARY                The target reproduces three symbolic expressions inside
                                quoted spans (§9.1 of the target declares all three).
                                Verified: each is a whole-span quotation required by
                                quotation integrity, none is evaluated, compared or
                                approached. NOT a violation.
AUTHORED / DRAFTED / PROPOSED   none found in the target. `CLASS-DISPLAYED-VIABLE` and
                                `WOULD-BUILD-NAMED` are declared at §10 as the lane's own
                                display device, "not proposed as corpus vocabulary" —
                                correct disposition, no new class constituted.
ADVOCACY                        BOUNDARY NOTE, not a violation. Target §7.3 writes
                                "Every catalogued TYPE-R barrier should be re-read with
                                its following text". This is an imperative about reading
                                practice, issued inside a section the commission asked
                                for ("WHAT THIS SUPPORTS"), and immediately fenced by
                                "This lane authored no re-typing and proposes none".
                                Recorded, not charged.
RE-READ NEGATIVES               0 re-typed, re-graded or re-adjudicated by either lane.
                                Reading catalogued negatives for their escape text is
                                the commission itself.
BARRED FILES OPENED             0 by the target; 0 by this lane.
                                QUESTIONSSETTLED_REGISTER_V001.md verified PRESENT in
                                ROOT B and verified ABSENT from both permitted lists.
                                Leak counter 0/0/0/0/0/0/0/0/0 including self-exclude.
SUPERVISION DIRECTORY           directory listing enumerated only; no non-DOR file opened.
GAPS FILLED                     none. E2-E5 moved TO IndETERMINATE, not resolved.
GIT                             none, by either lane.
```

### 8.1 Seals — re-verified by this lane from the artifact's own directory

```text
$ cd "/Users/bgm/MB Work/alpha-program-archive/workspace" && shasum -a 256 -c <sidecar>

STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_PROTOCOL_RESULT_V001.md: OK
STAGE8_CERTIFICATION_RULES_O8SR_V001.md:                                OK
STAGE8_CERTIFICATION_RULES_O8SR_AUDIT_V001.md:                          OK
STAGE8_BRIDGE_DECAY_DETERMINATION_V001.md:                              OK
STAGE8_T7_D3_QUANTIFIER_READING_FREEZE_AND_LEMMA_CONSUMPTION_V001.md:   OK
STAGE8_DESC_B03_DARIO_V001.md:                                          OK
STAGE8_REQUIRE_G3_CHECK_V001.md:                                        OK
                                                                     7/7 OK

TARGET SIDECARS
STAGE8_TYPER_ESCAPES_O46SR_V001.md.seal.sha256:                         OK
STAGE8_TYPER_ESCAPES_O46SR_V001.seal.sha256:                            OK
                                                                     2/2 OK
```

Both target sidecars carry `0372e2937c…f506e78c`, which equals this lane's independently
recomputed digest of the artifact. The build's seal claims are **true**. Its declaration
that seal coverage is partial and that nothing is upgraded on an absent seal is also
true and is the correct disposition.

---

## 9. SWEEP CUTOFFS — PATTERN, HITS, LEAK COUNTER

Every sweep below was executed by this lane. Counts are actual.

| # | Pattern / rule | Scope | Hits | Leaks |
|---|---|---|---|---|
| X1 | file enumeration `*.md *.txt *.json` minus BAR array | both roots | **5,950** files | 0 (per-pattern, §2.2) |
| X2 | token `TYPE-R` | permitted corpus | **6,453** occurrences in **812** files | 0 |
| X3 | `IDENT = false [\|/] TYPE-R` single-line | permitted corpus | **4,574** sites | — |
| X4 | `IDENT =` EOL + `false [\|/] TYPE-R` | permitted corpus | **28** sites, 10 identifiers | — |
| X5 | **`IDENT = false [\|/]` EOL + `TYPE-R`** (form the build missed) | permitted corpus | **38** sites, **19** identifiers, **13 new** | — |
| X6 | `IDENT = false` EOL + `[\|/] TYPE-R` | permitted corpus | **0** | — |
| X7 | wrap-fragment rule (prev line ends `_`) | X3+X4 identifiers | **4** removed (build declared 5; `_ALONE` not reproduced here) | — |
| X8 | mention index, token-boundary, basename-collapsed | permitted corpus | 1,944 identifiers indexed | 0 |
| X9 | mention-spread ≥ 2 | the 1,944 | **157** (**158** with X5) | — |
| X10 | boilerplate removal, each re-verified at bytes by spread | the 157 | **11** removed | — |
| X11 | mention-spread ≥ 3 | the 146 | **54** (**55** with X5) — SET-EQUAL to the build's 54 | — |
| X12 | mention-spread == 2, boilerplate/wrap removed | the 146 | **92** (build declared 103) | — |
| X13 | rows with ≥1 non-typing mentioning artifact | the 54 | **19** (**18** corrected for X5) | — |
| X14 | rows typed in ≥ 2 artifacts | the 54 | **49** | — |
| X15 | widening-token set (14 patterns, ±4 lines) over non-typing consumers | the 54 | **11 raw, 0 genuine** | 11 opened, all `restriction_square` template-field false positives |
| X16 | eye-read of every non-typing consumer context | the 19 | **0 widening**; 2 genuine MATCHED rows the build missed | — |
| X17 | `TYPE-R` within ±5 lines of `Shale-Stinespring` | permitted corpus | **0** | 0 |
| X18 | files containing `Shale-Stinespring` / `FP-2` | permitted corpus | **25** / **33** | 0 |

**Declared cutoff of this audit.** This lane graded, at bytes, the rungs of the ladder,
the full §6.2 MATCHED table, the §6.1 sweep, the §6.5 structural finding, the 11
NOT-A-BARRIER exclusions, the 11 boilerplate removals, all 19 Q3 consumer contexts, and
14 quoted spans across §3, §5, §6. It did **not** re-open the source text of all 28
surviving NAMES-AN-ESCAPE rows individually; E1, E2–E5, E6 and the E17–E32 table entries
for `K_square`, `restriction_square` and the missed row were opened. **The 92-row
spread-2 residue was not read by either lane.** That is declared, not hidden.

---

## 10. CORRECTIONS IN SEVERITY ORDER

| ID | Correction | Deciding file:line |
|---|---|---|
| **COR-A** | **All 7 rows in the §6.2 MATCHED table are graded against artifacts that type the flag themselves, and so are excluded from the build's own Q3 denominator of 19. Three of them have empty non-typing-consumer sets and belong to the 35 CANNOT-DETERMINE. One compares the source with itself.** The Q3 conclusion survives independent re-derivation; its displayed support does not. | `STAGE8_TYPER_ESCAPES_O46SR_V001.md:574-580` against its own rule at `:236`; decided at `STAGE8_7A_DBR_PUBLIC_LAYER_DARIO_V001.md:243` |
| **COR-B** | **A third flag form, `IDENT = false \|` ⏎ `TYPE-R`, was never swept.** 38 sites, 13 new identifiers. One barrier row is missing from the adjudicated set; two rows must leave the Q3 denominator because their "consumers" are typing artifacts. | `STAGE8_7A_EMPTY_CHAMBER_DARIO_V001.md:144-145`; also `STAGE8_TASK4A_P3_SECOND_ATTACK_LAW_SIDE_CONSTRUCTION_AND_NARROWED_STOP_V001.md:358` |
| **COR-C** | **The declared spread-2 residue is 92, not 103.** The build computed 157 − 54 without removing the 11 boilerplate it had already excluded. | `STAGE8_TYPER_ESCAPES_O46SR_V001.md:220` and `:731` |
| **COR-D** | **The NAMES-AN-ESCAPE sub-kind split is 16 CDV / 16 WBN, not 14 / 18**, by count of the build's own labels. The asymmetry that motivates choice C8 does not exist at bytes. | `STAGE8_TYPER_ESCAPES_O46SR_V001.md:471`, repeated `:658-659`, against `:253-469` |
| **COR-E** | **The MATCHED tally of 6 disagrees with the 7 rows and 7 distinct barriers itemised in §6.2**, and the disagreement is never reconciled. | `STAGE8_TYPER_ESCAPES_O46SR_V001.md:672` against `:574-580` |
| **COR-F** | **E2–E5 (4 of the 32) are over-graded.** The adjacent positive theorem concerns the *raw* skeleton's compact resolvent and isolated clusters, not the four refuted *public* predicates; the source types the public gap `NO_VERDICT` five lines above the flags. Corrected to INDETERMINATE-AT-BYTES. | `STAGE8_7A_DBR_SPECTRUM_DARIO_V001.md:183` against `:198-203` |
| **COR-G** | **Two off-by-one counts:** L0 5,949 → 5,950 (explained: `STAGE8_RESERVATION_UNION_O46SR_V001.md` written at 02:42, after enumeration); L0b 6,452 → 6,453 (unexplained, 0.015%). | `STAGE8_TYPER_ESCAPES_O46SR_V001.md:198` and `:200` |
| **COR-H** | **The S10 raw hit count of 17 is not reproducible; this lane gets 11.** The finding — all hits false positives on `restriction_square`, 0 genuine — is confirmed, and both representative spans are verbatim. | `STAGE8_TYPER_ESCAPES_O46SR_V001.md:542` |

---

## 11. CORRECTED TALLIES — STATED EXPLICITLY

### 11.1 Corrected population ladder

```text
                                                  BUILD      CORRECTED
L0   permitted files                              5,949      5,950
L0a  files containing TYPE-R                        812        812   (EXACT)
L0b  occurrences of TYPE-R                        6,452      6,453
L1   typed-negative sites                         4,602      4,640   (+38, form 3)
L2   distinct identifiers                         1,944      1,958   (+14, form 3)
L3   real distinct TYPE-R negatives               1,939     ~1,952
L4   spread >= 2                                    157        158
L4a  boilerplate removed                             11         11   (EXACT)
L5   ADJUDICATED SET (spread >= 3)                   54         55
L5r  DECLARED RESIDUE (spread == 2), unread         103         92
L6   Q2 denominator (genuine barriers)               43         44
L7   Q3 denominator (non-typing consumer exists)     19         18
L7a  typed in >= 2 artifacts                         49         49   (EXACT)
```

### 11.2 Corrected Q2 tally

```text
POPULATION: 44 graded TYPE-R BARRIERS
  = 55 adjudicated rows (spread >= 3, boilerplate and wrap fragments removed)
    minus the 11 NOT-A-BARRIER rows, which this lane sustains.
  Scope: both roots, permitted corpus, mirrors collapsed by basename,
         read at the barrier and at the text immediately following it.

NAMES-AN-ESCAPE          29 / 44  =  66%      (build: 32/43 = 74%)
  = 32 build rows - 4 (E2-E5, COR-F) + 1 (the row missed at COR-B)
  of which
    CLASS-DISPLAYED-VIABLE  13    (build stated 14; itemised 16; -4 +1)
    WOULD-BUILD-NAMED       16    (build stated 18; itemised 16)
CLEAN                     3 / 44  =   7%      (unchanged)
INDETERMINATE-AT-BYTES   12 / 44  =  27%      (build: 8/43; +4 from COR-F)
  of which SECOND-HAND     3
```

**NAMES-AN-ESCAPE remains COMMON.** The corrected rate is 66%, not 74%. The build's
qualitative conclusion — that a lane stopping at the `test:` field will usually miss a
door the same source drew within a few lines — **survives at two rows in three** rather
than three in four.

### 11.3 Corrected Q3 tally

```text
POPULATION: 18 rows with >= 1 artifact that mentions the identifier
  WITHOUT itself typing it (19 by the build's rule, minus C_REF and EPOST
  per COR-B, plus the row missed at COR-B). The other 37 have no
  independent consumer statement in the corpus.

CONSUMER-WIDER-THAN-SOURCE     0 / 18   CONFIRMED AT BYTES — the build's
                                        conclusion stands, independently re-derived
                                        by pattern sweep AND by eye-read of every
                                        real consumer context.

MATCHED, as displayed by the build      0 valid   (all 7 rows outside the
                                                   denominator — COR-A)
MATCHED, re-derived by this lane        5+        K_square_forced_by_general_composition;
                                                  NONTRIVIAL_ONE_SIDED_CONTACT_...;
                                                  NEW_FREE_STATE_SLOT_FOUND;
                                                  HIDDEN_ANCHOR_SELECTION_FOUND;
                                                  CONDITIONAL_ROWS_QUIETLY_UPGRADED
CANNOT-DETERMINE                       37 / 55    (no independent consumer exists)
                                       13 / 18    (consumer exists but states no
                                                   comparable quantifier, or is a
                                                   bare keyword list)
```

### 11.4 Reconciliation of this audit's headline against its own sweep block

This lane's headline is that the build is **CONFIRMED-WITH-CORRECTIONS overall with one
REFUTED dimension**. Checked against X1–X18 before sealing:

- The population claim is sustained by X1, X2, X3, X4, X9, X10, X11, X13, X14 — nine
  sweeps, seven of them returning the build's number exactly and one returning set
  equality of all 54 names. A REFUTED grade on population would contradict this lane's
  own evidence.
- The Q3 conclusion is sustained by X15 and X16 — a pattern sweep returning 0 genuine
  and an eye-read of every real consumer returning 0 widening. This lane therefore
  **cannot** refute the headline claim, only its displayed support, and says so.
- The REFUTED grade on Dimension 5 rests on COR-A, which is decided by a single byte
  fact — `STAGE8_7A_DBR_PUBLIC_LAYER_DARIO_V001.md:243` types the flag it is cited as
  consuming — and on the build's own denominator rule at `:236`. It does not rest on a
  disagreement about method.
- COR-F moves 4 rows and is the only grade reversal in this audit. It changes 74% to
  66%. It does not change "common" to "rare", and this lane does not claim it does.

---

## 12. FLAG BLOCK

### 12.1 Fences

```text
alpha_computed        = false   [held; no coupling value approached]
proof_authorized      = false   [held; nothing proved, nothing authored]
kappa_record_computed = false   [held]
```

No numeric value of any coupling, scale, root, eigenvalue, norm or constant was computed,
transcribed or approached by this lane. This audit reproduces **no** symbolic magnitude
expressions from the target's quoted spans; where the target's §9.1 declares three, this
lane verified them in place at their sources and did not carry them forward.

### 12.2 Seals

7/7 OK on the artifacts the target relied on, plus 2/2 OK on the target's own sidecars —
all re-run by this lane with `shasum -a 256 -c` from `/Users/bgm/MB Work/alpha-program-archive/workspace`.
Seal coverage across quoted sources is **partial**, as the target declares; most sources
opened by this audit carry no `.seal.sha256`. Those reads are byte-reads at path,
unsealed, and **no grade in this audit is upgraded on the strength of an absent seal.**

### 12.3 Bar incidents

```text
BARRED FILES OPENED                                   0
  QUESTIONSSETTLED_REGISTER_V001.md (ROOT B)          VERIFIED PRESENT, VERIFIED EXCLUDED,
                                                      NOT OPENED
  any *TRACKER*, THE_PLAN*, ROAD_REMAINING*,
    THE_HANDOFF*, OBSERVATIONS_REGISTER*,
    *DECISION_SHEET*                                  NOT OPENED (leak counter 0 x 7)
SELF-EXCLUSION                                        LIVE in every sweep; the target was
                                                      excluded from all sweeps and read
                                                      only as the target
AUTHORING / ADVOCACY / ADOPTION                       none. No re-typing, no proposal, no
                                                      recommendation issued by this lane.
GAPS FILLED                                           none. 4 rows moved TO
                                                      INDETERMINATE-AT-BYTES (COR-F); no
                                                      row resolved by inference.
GIT                                                   none.
```

### 12.4 Own-draft defects — found by this lane, in this lane's work, corrected

**A-D1 — FIRST SPREAD PASS USED TYPINGS, NOT MENTIONS.** This lane's first spread
computation counted only basenames where an identifier is *typed*, giving 125 at spread
≥2 and 45 at ≥3 against the build's 157/54. This lane's first instinct was to report a
32-row divergence as a refutation of the population. Re-reading the build's C4 at bytes —
*"the identifier **appears** in ≥2 distinct artifact BASENAMES"* — showed the build's
rule is mentions, and re-running on mentions reproduced 157 and 54 exactly. **Had this
defect shipped, this audit would have filed a false REFUTED on Dimension 1** on the
strength of a population mismatch that was its own.

**A-D2 — WRAP-FRAGMENT COUNT NOT FULLY REPRODUCED.** This lane's wrap rule ("previous
line ends in `_`") removes 4 identifiers where the build declared 5; `_ALONE` was not
reproduced. Rather than assert the build wrong, this audit reports the discrepancy as
unresolved and excludes `_ALONE` from its own adjudicable set by name, so that the
set-equality test at §3.1 is unaffected either way.

**A-D3 — LINE TRUNCATION IN THE CONSUMER DUMP.** The consumer-context dump truncated
lines at 150 characters, which hid the identifier on three long lines
(`1024_DONE.md:18`, `RELAY_PASTE_895_…:5`, `STAGE8_STANDING_PREMISE_TEST_CLASSIFICATION_V001.md:229`)
and briefly suggested false matches. Each was re-opened at full width before any grade
was assigned. No grade rests on a truncated line.

**A-D4 — THE TEMPTATION TO REFUTE THE Q3 CONCLUSION ALONG WITH ITS EVIDENCE.** Having
established COR-A, the cheap move was to call the whole Q3 result unsupported. This lane
instead re-ran the widening hunt itself, twice, by two methods, and found the conclusion
true. **The evidence is void and the claim is sound, and this audit reports both.**

---

## 13. WHAT THIS AUDIT LEAVES STANDING

The build set out to test whether TYPE-R barriers in this corpus sit next to doors their
sources drew, and whether downstream consumers over-read them. Both answers survive.

**NAMES-AN-ESCAPE is COMMON — 29 of 44 corrected (66%), down from 32 of 43 (74%).**

**CONSUMER-WIDER is ZERO — 0 of 18 corrected, and this lane re-derived it independently
by two methods rather than accepting it.** The corpus's consumers of typed barriers do
not widen their sources' quantifiers. Several actively police the widening. The build's
recommendation *against* a fleet-wide re-reading on Q3 grounds is sustained.

**The structural finding is exact.** The one barrier known to have been inherited as a
wall where its source drew a door — the equal-time / Shale-Stinespring impossibility at
FP-2 — carries **0** TYPE-R typings within ±5 lines across all 25 files that mention it.
The exposure lives at barriers that never entered the typing protocol. That is the
build's own conclusion, it is correct at bytes, and nothing in this audit disturbs it.

What the corrections change is the **arithmetic and the displayed support**, not the
direction of either finding. The single most consequential defect is COR-A, and it is
the one the standing discipline warns about most explicitly: a comparison drawn across
two different populations, committed inside the section written to prevent it.

```text
alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
```
