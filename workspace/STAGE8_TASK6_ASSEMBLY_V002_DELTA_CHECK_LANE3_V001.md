# STAGE 8 / TASK 6 / SUBGATE — BOUNDED DELTA RE-CHECK: THE ASSEMBLY V002 — LANE 3 V001

Lane: Codex Lane 3 (SOL), bounded delta-check custody  
Task: PASTE 629 / Task 6 / subgate  
Date: 2026-08-06  
Scope: V001 → V002 carriage and D1–D8 implementation only; no fresh review of the assembly's mathematical merits

```text
REGISTER_HEAD = Q-564
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_PHYSICAL_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none
```

## 0. Preflight and bounded-review rule

### 0.1 Access and immutable subjects

| Item | Verification |
|---|---|
| Living register | head Q-564 verified; Q-562 consumed by entry, not by whole-file hash |
| V002 under review | `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V002.md`; SHA-256 `11e4e6e4a37572dad1f86ed91fb6ed692195ec282876456418c4fcdac5021037`; sidecar matched |
| V001 base | `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V001.md`; SHA-256 `a2fdd7c0502083cc9973b766464a30807a3ba3b36b9305011df404671635422c`; sidecar matched |
| Review of record | `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_REVIEW_LANE3_V001.md`; SHA-256 `f8bfff5bb01ce33f2e973a9ae58fb80bd07650dd9f0d83f02202eda9b3bc48ee`; sidecar matched |
| Q-557 decision | `DECISION_S03_EXPLICIT_INCOMPLETENESS_2026-08-06.md`; SHA-256 `f0a535214f946b6813f4896c8bc1b7be7a6e34c16278fc6cc18ed688a0194d67`; sidecar matched |
| Sealed Q-spec ledger | `STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.md`; SHA-256 `7995f6fda75e78795cbfe167f8c8df634170ea3b43affd5bbe6e22bcda8f6ffe`; cleanroom/archive bytes matched; line 168 read |
| Sealed V011 packet copy | `review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md`; SHA-256 `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a`; matched packet manifest entry; lines 1592–1605 read |
| Required output | absent in the cleanroom and archive workspace before writing |

[PROVABLE] The named byte subjects and their hashes are fixed above. No register,
tracker, plan, commit, push, repository mutation, member-binding, evaluation, or
end-test action is performed by this certificate.

### 0.2 The Q-562 qualification and this relay's boundary

Q-562 registered V002 with an express qualification: the sixteen-row table was
treated as covering substantive slot/physics content, while V001 §0.4 and the
battery/verb-audit regions had been restructured without table rows; this bounded
relay was queued to classify the residue. Thus Q-562 did not pre-decide the result
of this re-diff.

[YOURS] I do not re-adjudicate the slot grades, the appeal dissolutions, the S03
disposition, or the freeze theory. I ask only:

1. does every changed byte region have a delta-table row;
2. does each named correction occur at the location that the table names;
3. did an untabled deletion remove content that the review said must survive; and
4. are V002's own carriage verbs supported by the displayed comparison?

### 0.3 Classification vocabulary

```text
COVERED Δnn = the hunk implements the V002 delta-table row named nn.
U-HE         = uncovered but harmless editorial/provenance change; no operative
               claim is added, lost, weakened, or strengthened.
U-CB         = uncovered and content-bearing; a claim, condition, display,
               classification, or audit method is added, lost, weakened, or
               strengthened.
MIXED        = one part is covered and another is uncovered.
```

This classification is deliberately stricter than “the new prose is reasonable.”
The carriage claim is finite equality. A substantively sound untabled edit still
refutes that finite-equality claim.

## 1. K1 — mechanical V001 → V002 re-diff

### 1.1 Command and totals

The comparison was executed with the fixed subjects above:

```text
/usr/bin/diff -U 0 V001 V002

ZERO-CONTEXT HUNKS = 73
V002 LINES ADDED   = 267
V001 LINES DELETED = 306
NET LINE CHANGE    = -39
```

The 73-hunk count and 267/306 counts come from the zero-context stream after the
first hunk delimiter; identical moved separators are not counted as changes. The
classification below accounts for all 73 hunk headers in their emitted order.
These are document-line counts, not physical quantities.

### 1.2 Complete hunk partition

| Hunk | Zero-context span `V001 → V002` | Partition | Classification and finding |
|---:|---|---|---|
| H01 | `-1 → +1` | uncovered | U-HE — version title only. |
| H02 | `-4,4 → +4,6` | uncovered | U-HE — task/supersession/custody metadata; no assembly proposition changes. |
| H03 | `-10,5 → +12,6` | MIXED: Δ01, Δ03; uncovered remainder | U-CB — SLOTS and FREEZE are covered; the promised Δ02 `UNUSED_PREDICTION` replacement is absent, the duplicate THOMSON lead field is dropped, and new `DELTA`/`CARRIAGE` assertions appear untabled. |
| H04 | `-18 → +21` | COVERED Δ04 | Machinery-appeal lead field updated. |
| H05 | `-21,6 → +24` | uncovered | U-CB — the independent zero-fill corroboration and the parameter-free/target-value-free demand-object headline are deleted; the latter typing is load-bearing below. |
| H06 | `-28,2 → +25,0` | uncovered | U-HE — duplicate §0 heading removed. |
| H07 | `-32,5 → +28,5` | uncovered | U-HE — preflight/source-provenance table refreshed; the fixed subjects are independently verified here. |
| H08 | `-38 → +34` | uncovered | U-HE — §0.1 heading replaced. |
| H09 | `-40,40 → +35,0` | uncovered | U-CB — deletes the target-awareness standard and two disclosure pins, the authoritative `Q_spec` demand, and the introduction to the exact C7 spine. |
| H10 | `-81,11 → +37,4` | uncovered | U-CB — deletes the displayed nine-member C7 chain and anti-selection equation; inserts the finite carriage rule. |
| H11 | `-94,4 → +43,2` | uncovered | U-CB — deletes the C7 anti-tuning explanation; adds the single-counterexample falsifier for carriage. |
| H12 | `-99 → +46` | uncovered | U-HE — method heading becomes delta-table heading. |
| H13 | `-101,7 → +48,18` | uncovered | U-CB — drops the five-researcher method narrative (acceptable provenance) and inserts the sixteen-row delta instrument (content-bearing metadata). |
| H14 | `-108,0 → +67,2` | uncovered | U-CB — adds the false sentence “Everything not in this table carries verbatim from V001.” |
| H15 | `-113,2 → +73,5` | uncovered | U-CB — adds D1's provenance rationale for restoring literal ledger characters; the rationale is sound but is not itself delta row 11's named S11 edit. |
| H16 | `-118 → +81` | COVERED Δ05 | D7's `T_R`/`T_K` distinction; incidental typography is harmless. |
| H17 | `-120,5 → +83,5` | COVERED Δ06–Δ09, but pin execution incomplete | D2/D3 content is present; Δ06 and Δ07 fail their complete promised display, as shown in §3. |
| H18 | `-126 → +89` | COVERED Δ10 | D6 successor typing for S09. |
| H19 | `-128,2 → +91,2` | COVERED Δ11–Δ12 | D1 Moller restoration and D2 S12 re-posing. |
| H20 | `-132 → +95` | uncovered | U-HE — S15 wording only; semantic force unchanged. |
| H21 | `-134,2 → +97` | MIXED: COVERED Δ13; uncovered S17 deletion | U-CB — S18 grade/character restoration is covered; S17 is removed from its ledger-table position without a delta row. |
| H22 | `-136,0 → +99,4` | uncovered | U-CB — S17 is reinserted as a footnote after S18, changing the review-confirmed order/display. |
| H23 | `-138,3 → +104` | COVERED Δ13 | Counts become 0/18/0. |
| H24 | `-143 → +107` | COVERED Δ14 | Contradiction section re-headed as scheme covariance. |
| H25 | `-145,2 → +109,5` | COVERED Δ14 | Dissolution introduced. |
| H26 | `-148 → +115,3` | COVERED Δ14 | O-SC display introduced. |
| H27 | `-150,4 → +119,4` | COVERED Δ12/Δ14 | Origin/covariance distinction and non-inhabitance displayed. |
| H28 | `-155,3 → +124` | COVERED Δ14 | Old appeal board removed and appeal 1 dissolution displayed. |
| H29 | `-158,0 → +126,6` | COVERED Δ04, Δ06, Δ08, Δ14 | Appeals 2 and 3 carried at summary level. |
| H30 | `-163 → +136` | uncovered | U-HE — S16 heading compression only. |
| H31 | `-165,4 → +138,3` | uncovered | U-HE — S16 question condensed without changing its demanded object. |
| H32 | `-170,2 → +142,4` | uncovered | U-CB — S16 audit return and source pin are condensed untabled; the core status survives. |
| H33 | `-173,9 → +147,6` | uncovered | U-CB — the raw S16 flag block becomes prose; all three review-required precisions survive, but exact raw flags/tags are dropped. |
| H34 | `-183,4 → +154,3` | uncovered | U-CB — S16 TYPE-U and anti-tuning prose are consolidated untabled; no review-required precision is lost. |
| H35 | `-188 → +158` | MIXED: COVERED Δ15; uncovered S16 relocation | S18 is re-headed TYPE-U; the displaced S16 “Three precisions” heading is an untabled harmless consolidation. |
| H36 | `-190,13 → +160` | MIXED: COVERED Δ15; uncovered S16 consolidation | U-CB — Δ15 adds the S18 withdrawal heading, while the detailed S16 three-precision list is compressed into earlier prose without a table row. |
| H37 | `-204,5 → +162,7` | MIXED: COVERED Δ15; uncovered S16 consolidation | U-CB — the S18 withdrawal is required, while S16's expanded anti-tuning paragraph is consolidated without a table row; its operative rule survives. |
| H38 | `-210 → +170,3` | COVERED Δ15 | False falsifier role withdrawn. |
| H39 | `-212,3 → +174,5` | COVERED Δ15 | Self-correction displayed. |
| H40 | `-216 → +180` | COVERED Δ15 | Eligibility section introduced. |
| H41 | `-218,7 → +182,3` | MIXED: COVERED Δ15; uncovered deletion | U-CB — eligibility predicate starts, but the review-confirmed OBS-22 declination is deleted untabled. |
| H42 | `-226 → +186,8` | COVERED Δ15 | Five eligibility conjuncts displayed. |
| H43 | `-228,2 → +195,4` | COVERED Δ15 | No candidate satisfies the bar. |
| H44 | `-231,4 → +200` | COVERED Δ15 | Candidate-shape section introduced. |
| H45 | `-236,4 → +202` | COVERED Δ15 | PART-PROVABLE confined to candidate shape. |
| H46 | `-241,15 → +203,0` | COVERED Δ15 | False S18 qualification table and source argument removed. |
| H47 | `-257,6 → +205,4` | COVERED Δ15 | Conditional discontinuity replaces false prediction/falsifier. |
| H48 | `-265,4 → +211,5` | COVERED Δ15 | Candidate shape explicitly not selected or filling. |
| H49 | `-270,2 → +217,3` | COVERED Δ15 | S18 anti-tuning strengthened. |
| H50 | `-273,5 → +220,0` | COVERED Δ15 | Obsolete blind-prediction anti-tuning paragraph deleted. |
| H51 | `-280 → +223` | COVERED Δ16 | Freeze section corrected. |
| H52 | `-282 → +225` | COVERED Δ16 | “Ready” subsection corrected. |
| H53 | `-284,5 → +227,3` | COVERED Δ16 | Internal contradiction blocker withdrawn. |
| H54 | `-290,4 → +231` | COVERED Δ16 | Corrected freeze statement introduced. |
| H55 | `-295,2 → +232,0` | COVERED Δ01/Δ16 | Old remaining-type subsection removed. |
| H56 | `-298,3 → +234,11` | COVERED Δ01/Δ16 | 18 TYPE-U and external gates displayed. |
| H57 | `-303 → +247,3` | COVERED Δ16 | Consequence of moving blocker outside document. |
| H58 | `-305,8 → +251` | COVERED Δ04, Δ06, Δ08, Δ14, Δ16 | Old three-ruling list removed; replacement subsection starts. |
| H59 | `-314,3 → +253` | COVERED Δ01/Δ16 | All-eighteen TYPE-U board. |
| H60 | `-317,0 → +255,5` | COVERED Δ04/Δ16 | No remaining internal ruling displayed. |
| H61 | `-324,5 → +266,5` | uncovered | U-CB — F_PLDEC is strengthened at the construction end, but the two target-adjacent disclosures are removed. |
| H62 | `-330 → +272` | uncovered | U-HE — section-heading relocation; the new anti-tuning content is H63. |
| H63 | `-332,3 → +274,4` | uncovered | U-CB — deletes V001's named-actual-object inventory and inserts the supported but untabled S03/S18 anti-tuning strengthening. |
| H64 | `-336,3 → +279` | uncovered | U-CB — the old awaiting-member rail block is deleted while the surface-anchor heading is relocated; replacement rails occur at H66. |
| H65 | `-340,3 → +281,3` | uncovered | U-CB — deletes V001's three-line “actual-object column almost empty” anchor observation and inserts V002's new named-object inventory. |
| H66 | `-344 → +285,3` | uncovered | U-CB — deletes V001's `### 4.3 M-2 searches` heading and inserts V002's new awaiting-member rail inventory. |
| H67 | `-346,5 → +289` | uncovered | U-CB — the explicit fixed-string/normalized/scope/bounded-negative M-2 method is deleted while the M-2 heading is relocated. |
| H68 | `-352 → +291,4` | uncovered | U-CB — a compressed M-2 summary and custody pin replace the old verb-audit heading; the bounded-negative guard survives but the mechanics do not. |
| H69 | `-353,0 → +296,2` | uncovered | U-HE — verb-audit heading/table spacing. |
| H70 | `-356,10 → +300,11` | uncovered | U-CB — verb board replaced; it adds the unsupported claim that the release condition and carriage were displayed. |
| H71 | `-368,0 → +314,2` | uncovered | U-CB — carriage-verification section added. |
| H72 | `-370,29 → +317,45` | MIXED: Δ01–Δ16 propagation; uncovered certificate | U-CB — final correction summary is mostly authorized, but “every substantive change” and “outside text carries verbatim” are false; D8 again names rather than displays the release condition. |
| H73 | `-402,7 → +365,5` | MIXED: Δ13/Δ16; uncovered loss | U-CB — corrected grade/freeze conclusion is covered; parameter-free target typing, C7 display, and the old blind-prediction/falsifier synthesis disappear from the closing synthesis. |

```text
HUNKS_ACCOUNTED = 73 / 73
UNCOVERED_HARMLESS_EDITORIAL_OR_PROVENANCE = present
UNCOVERED_CONTENT_BEARING = present
```

### 1.3 The finite-equality counterexample

V002 makes three mechanically testable statements:

> “Everything not in this table carries verbatim from V001.”

> “Every substantive change is accounted for by a row of the §0.2 delta table”

> “Structural/section text outside the table carries verbatim.”

[PROVABLE] Any one untabled content-bearing hunk refutes those finite-equality
claims. H09, H10, H15, H36, H37, H41, H61, H63–H68, and H70 are independent witnesses.
Therefore the registrar's known method/battery residue is not wholly harmless,
and `CARRIAGE = verified_by_rediff` does not survive the re-diff.

## 2. K3 — nothing lost: exact survivor audit

### 2.1 Load-bearing content absent from V002

The review of record says the following survive review: the eighteen concepts in
their correct order, C7, the target-value-free/historically-target-aware standard,
the zero-filled count, S01–S17 TYPE-U, S16's three precisions, and the OBS-22
declination. The bounded comparison finds these absences.

#### L1 — target-value-free but historically target-aware, plus disclosures

V001 states:

> “These are target-value-free but historically target-aware.”

It then identifies two target-adjacent sealed references, says neither is usable
as a filling, and says neither is used. V002 contains neither the quoted standard
nor the two disclosures. Its F_PLDEC assertion remains a conduct claim, but its
historical-target disclosure is weakened by deletion.

#### L2 — the sealed-packet `Q_spec` demand

V001 displays the same demand carried at sealed packet V011:1592–1605:

> “A distinct sealed object `Q_spec` must define the complete physical charged
> transition amplitude. It must contain, with no measured alpha: the charged
> boundary carrier and unit action-character current; all charged source sectors
> and their statistics; the gauge, constraint, ghost if required, and public edge
> sectors; the preparation and durable-record projectors; the microscopic measure
> and regulator; the regulator-removal and locality theorem; the Ward identity and
> transverse physical quotient; the derived charged spectrum and every threshold
> entering the response; decoupling and matching rules; and the zero-momentum
> Thomson prescription.”

V002 contains no replacement display of this demand. That is a demand-side object
definition, not research provenance.

#### L3 — the exact C7 spine and anti-selection equation

V001 displays:

```text
S03 -> S04 -> S05 -> S06 -> S07 -> S08 -> S13 -> S16 -> S17
NO LATER ITEM MAY BE USED TO SELECT AN EARLIER ONE.                 (C7)
```

V002 cites C7 locally, but never displays the nine-member order or the equation.
This is material because the review expressly confirmed both membership and
order, not merely the name “C7.”

#### L4 — S17's place in the eighteen-row ledger

V001 places S17 before S18 in the ledger table. V002 places S18 in the table and
moves S17 into a parenthetical footnote after the table. S17's words survive, but
the eighteen-row table and review-confirmed order do not. This is a display/order
loss, not a lost TYPE-U grade.

#### L5 — OBS-22's disposition

V001 states:

> “OBS-22 is not a physics prediction and I decline it for this slot.”

and explains that it concerns the program's obstruction topology rather than a
world-refutable physical prediction. The review expressly confirms this
declination. V002 contains no OBS-22 occurrence.

#### L6 — parameter-free demand-object typing

V001 types the assembled demand side as one “parameter-free, target-value-free
object.” V002 retains “demand-side document” and the no-measured-input discipline,
but no `parameter-free` occurrence survives. This is a type-level qualifier of the
object offered to the seal rail, and the sealed Q-spec ledger gives its exact
status field at line 168:

```text
complete_parameter_free_Q_spec_frozen = false
```

#### L7 — explicit M-2 mechanics

V001 lists fixed strings, whitespace-normalized probes, scope/synonym checks, and
the rule that a bounded negative proves no emptiness. V002 reduces this to “Three
guards throughout” plus the bounded-negative sentence. The exact search mechanics
are therefore not carried verbatim and are not fully restated.

### 2.2 Acceptable drops and consolidations

| V001 material absent or compressed | Classification | Reason |
|---|---|---|
| §0.4 five-researcher/adversarial-verifier narrative | provenance narrative — acceptable drop | It describes how V001's grades were found, not a surviving slot obligation; the corrected grades are sourced to the review. |
| Old task/head/custody/preflight wording | provenance/editorial — acceptable drop | V002 legitimately refreshes version metadata and authorities. |
| Independent `closed_slots = 0` corroboration and headline rhetoric | provenance/duplicate — acceptable drop | The operative 0/18/0 count remains displayed. |
| Expanded S16 raw flag block and repeated citations | semantic-preserving consolidation — acceptable | V002 retains `MISSING_SPECIFICATION`, UNDETERMINED transport, unexecuted protocol, re-posed source, S13 meaning, and LP-JII coupling. |
| Old S18 false prediction/falsifier prose | required substantive deletion — covered Δ15 | D4/D5 require its withdrawal. |
| Old S06/S12 contradiction and freeze blocker | required substantive deletion — covered Δ14/Δ16 | D2 requires its withdrawal. |
| Closing rhetoric tied to the old grade/freeze state | required/harmless consolidation | The corrected state replaces it. |

### 2.3 Untabled surface-anchor dependency refresh

The battery's dependency inventory also changes without a delta row. V001 names
`Z_K[A_+,A_-]`, `W_K`, `omega_in`, `Ξ_N`, `(Z3)`, `(Z4)`, and the winding lattice;
V002 removes them while adding `Z_ext`, `A_hist`, `C_fin`, O-SC1/O-SC2, and the
five-conjunct eligibility predicate. V001's rails include the complete microscopic
charged generator and gravitational quantum measure; V002 removes those names,
changes `every one of S01–S17` to `all eighteen slots`, and adds the
promotion/measure bridge above `Z_ext`, the evaluator, and `SPEC-SEAL`. V001's
observation that the actual-object column is almost empty relative to the rails is
also deleted.

[YOURS] Some of this refresh follows the corrected S05/S18 story and may be the
right dependency board. That does not make it verbatim carriage. The exact
inventory replacement is content-bearing and audit-bearing; V003 must enumerate
it in the finite delta or restore the intended surviving anchors.

[YOURS] The acceptable §0.4 drop does not cure L1–L7. Those items are separately
load-bearing or audit-bearing, and several were explicitly named as survivors by
the review.

## 3. K2 — D1–D8 pin-by-pin implementation

| Item | Required correction | V002 pin evidence | Verdict |
|---|---|---|---|
| D1 | restore `Moller` and list-leading `and`, or weaken “verbatim” | S11 has `Moller`; S18 begins `and`; rationale is displayed | PASS |
| D2 | dissolve S06/S12 contradiction; carry scheme covariance; correct freeze | S12, §1.1, §3, and final board display O-SC1/O-SC2 compatibility, non-inhabitance, and external freeze gates | PASS |
| D3 | `Z_ext` built; integrated object is unbuilt layer; no arity fork | S05 and appeal 2 display exactly that distinction | PASS |
| D4 | S18 TYPE-U; remove derived-integrality claim | S18 body and count board comply; however Δ02 promises an operative lead-board replacement which is absent | PARTIAL — PIN DEFECT |
| D5 | do not use `(F-S18)` as provenance falsifier; carry real eligibility bar | §2.2 withdraws the use and displays the five-conjunct bar; however the same Δ02 lead-board pin is absent | PARTIAL — PIN DEFECT |
| D6 | S09 successor typing | S09 displays S9-A determination/S9-B exit, adopted zero-bare branch, false universal exclusion | PASS |
| D7 | keep `T_R` and `T_K` distinct | S01 displays the distinction and retired route | PASS |
| D8 / Q-557 | explicit incompleteness; no adopted completion/residue; S04–S08 object-side inheritance; exact release condition | S03 and summary carry the disposition and anti-tuning ground; S04 and S06 carry inheritance at their rows; the defects below remain | PARTIAL — TWO PIN DEFECTS |

### 3.1 D4/D5 lead-board defect (delta row 2)

Delta row 2 promises at **Lead board**:

```text
UNUSED_PREDICTION = TYPE-U (candidate shape carried, not chosen)
```

[PROVABLE] A fixed-string search finds that text only inside the delta table. It is
absent from the operative lead board and the final board. The S18 body is
corrected, so this is not relitigation of D4/D5; it is failure to perform the
table's declared edit at its declared pin.

### 3.2 D8 release-condition defect (delta row 6)

Q-557's release condition is:

```text
Re-open only by:
  (a) a sealed derivation bounding or classifying the mutation family from
      record structure alone;
  (b) Task 7 external-realization junction work supplying a selector or a
      bounding principle; or
  (c) a principal re-ruling of record.
Any future adoption must use authored-residue discipline after the family is
first bounded.
```

V002's S03 row displays explicit incompleteness and no adoption/residue, but it
does not display this release condition. The verb board says the release condition
is carried, and the final board says `release condition of record`; both name the
missing display rather than supply it.

### 3.3 D8 inheritance defect (delta row 7)

Q-557 states that S04–S08 inherit the block on the object side while the demand
side is unaffected. Delta row 7 locates that correction at `§1 rows S04–S08`.
The row-level display is:

```text
S04  explicit object-side inheritance                 PRESENT
S05  built external object / missing promotion layer  inheritance NOT STATED
S06  explicit object-side inheritance                 PRESENT
S07  no member / interacting-theory demand             inheritance NOT STATED
S08  no member                                          inheritance NOT STATED
```

The final summary asserts the collective inheritance, but it does not make the
promised row-level edits at S05, S07, and S08. This is a pin-level carriage defect;
it does not refute the ruling itself.

### 3.4 Corrected D1–D8 board

```text
D1 = PASS
D2 = PASS
D3 = PASS
D4 = BODY_PASS / LEAD_PIN_MISSING
D5 = BODY_PASS / LEAD_PIN_MISSING
D6 = PASS
D7 = PASS
D8 = DISPOSITION_PASS / RELEASE_DISPLAY_MISSING /
     S05_S07_S08_ROW_INHERITANCE_MISSING
```

No appeal is relitigated: appeal 1 and appeal 2 remain DISSOLVED, appeal 3 remains
RULED. The corrected freeze statement and both strengthened anti-tuning rows are
substantively supported. The bounded defects are carriage/display defects.

## 4. K4 — verdict, consequence, and battery

### 4.1 Required V003 delta

[YOURS] V002 needs a V003 because its own finite-equality certificate is false and
because review-confirmed survivor content is absent. A bounded V003 can repair
this without reopening any physics determination:

1. add a truthful delta addendum covering every retained content-bearing rewrite;
2. restore the target-awareness standard and two disclosures;
3. restore the authoritative `Q_spec` demand display;
4. restore the exact C7 nine-member order and anti-selection equation;
5. restore S17 to the eighteen-row ledger before S18;
6. restore the OBS-22 declination;
7. restore the parameter-free demand-object qualifier and explicit M-2 mechanics;
8. enumerate and justify the surface-anchor dependency refresh;
9. execute Δ02 at the operative lead/final board;
10. display Q-557's full release condition; and
11. carry object-side inheritance at each S04–S08 row, or revise the delta row to
    name honestly where the collective display resides.

Until that occurs, V002's corrected grades and rulings may be cited at their true
substantive strength, but V002 cannot certify its own C-V5 carriage.

### 4.2 Seal-rail consequence

This artifact neither freezes nor unfreezes QSPEC. It determines only that the
specific V002 document does not meet its claimed finite-equality carriage form.
The evaluator and SPEC-SEAL remain external gates exactly as V002 reports; this
certificate adds a document-repair prerequisite before V002 itself can serve as a
carriage-clean demand-side subject.

### 4.3 `F_PLDEC` and fence discipline

| Attack | Result |
|---|---|
| Reader/false-anchor influence | none; the comparison consumes only sealed text and byte differences |
| Desired physical outcome | none consulted |
| Coupling/threshold/period evaluation | none performed |
| Fixed point or end test | none performed |
| Member selection | none performed |
| Measured constant | none read or compared |

`F_PLDEC = CLEAN` for this certificate. The finding that V002 weakened its own
historical-target disclosure comes from text carriage, not from consulting a
target.

### 4.4 M-2 four-false-negative battery

| False-negative mode | Execution | Result |
|---|---|---|
| regex/metacharacter interpretation | fixed-string searches, not regex interpretations, for `parameter-free`, `historically target-aware`, `OBS-22`, `NO LATER ITEM`, ``A distinct sealed object `Q_spec` ``, and the promised `UNUSED_PREDICTION` field | first five absent from V002; promised field has one literal hit |
| line-wrap/whitespace miss | whitespace-normalized comparison and zero-context diff | omissions persist across wrapping |
| self-reference/scope miss | the promised S18 field's sole hit was located, then the delta table was excluded and the lead/final boards were searched separately; all operative sections were inspected for the other items | the promised text is self-referential evidence only; local references to C7 do not reproduce its ordered display |
| hyphenation/identifier variant | fixed-string families checked `parameter-free` / `parameter free` / `parameter_free`, `target-value-free` / `target value free` / `target_value_free`, and `historically target-aware` / spaced / underscored forms | every listed variant has zero V002 hits |

The separate epistemic guard also passes: every negative above is bounded to the
fixed V002 byte subject. No corpus-wide emptiness is inferred; V001, the review,
the sealed ledger, the sealed packet, and Q-557 supply the positive witnesses.

### 4.5 Surface anchor

**Named actual text objects:** V001 and V002 fixed byte subjects; delta rows 1–16;
slots S01–S18; `Z_ext`; O-SC1/O-SC2; Q-557's release condition; the C7 chain;
the V011 `Q_spec` demand; OBS-22's disposition.

**Rails not crossed:** evaluator execution, SPEC-SEAL, QSPEC-SPEC-SEAL, any action
completion, any physical carrier, any coupling, and every numerical/end-test rail.

### 4.6 Self verb audit

| Verb used here | Display above | Audit |
|---|---|---|
| `verified` hashes/head | §0.1 names each subject and result | CLEAN |
| `accounted` 73/73 | §1.2 lists each hunk exactly once | CLEAN |
| `absent` from V002 | §2 plus §4.4 fixed-string/scope searches; bounded to V002 | CLEAN |
| `PASS` D1–D3/D6/D7 | §3 displays the corrected pin | CLEAN |
| `PARTIAL` D4/D5/D8 | §§3.1–3.3 display each missing pin and the positive content that survives | CLEAN |
| `load-/audit-bearing` | §2 ties each item to the review's survivor board, sealed demand type, sealed status field, or explicit audit method | CLEAN |
| `NEEDS_V003` | §4.1 gives a finite repair list and §1.3 supplies counterexamples to V002 carriage | CLEAN |
| no relitigation | §§0.2 and 3.4 preserve the three appeal dispositions and freeze result | CLEAN |

---

DELTA = NOT_FULLY_ACCOUNTED (+target-awareness/disclosures; +Q_spec demand; +C7 spine/order; +S17 ledger order; +OBS-22 disposition; +parameter-free typing; +battery/surface-anchor/M-2/carriage rewrites)
D1_D8 = NOT_FULLY_CONFIRMED (+D4/D5 lead-board pin absent; +D8 release-condition display absent; +D8 S05/S07/S08 row-level inheritance absent)
LOST_CONTENT = target-awareness/disclosures; Q_spec demand; C7 exact display; S17 table order; OBS-22 declination; parameter-free object qualifier; explicit M-2 mechanics; surface-anchor dependency inventory/observation
ASSEMBLY_V002 = NEEDS_V003 (+restore review-confirmed survivors, execute delta rows 2/6/7 at their pins, and replace the false carriage certificate with a complete finite delta)
VERB_AUDIT_SELF = CLEAN
