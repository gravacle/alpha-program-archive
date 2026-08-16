# STAGE 8 — TYPE-R BARRIERS ON LIVE OBLIGATIONS: DOES THE SOURCE DRAW A DOOR WHERE THE CONSUMER INHERITED A WALL? — O46SR V001

## BUILD LANE — COMMISSION O46SR — 2026-08-16

```text
alpha_computed        = false [TERMINAL_FENCE_DECLARATION]
proof_authorized      = false [TERMINAL_FENCE_DECLARATION]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION]
```

---

## 0. VERDICT IN ONE LINE

**NAMES-AN-ESCAPE is COMMON — 32 of 43 graded barriers (74%); CONSUMER-WIDER is
RARE — 0 of 19 barriers that have a consumer outside their own typing artifact.**
The two findings are not in tension and together they locate the defect precisely:
the corpus's TYPE-R typings routinely sit next to a named escape, **and the
downstream consumers of those typed barriers do not over-read them.** The one
confirmed consumer-wider instance this commission was given — the equal-time /
Shale-Stinespring impossibility consumed at FP-2 — is, at bytes, **not typed
TYPE-R anywhere in the permitted corpus** (0 hits of `TYPE-R` within ±5 lines of
any of the 25 `Shale-Stinespring` occurrences). The over-reading happened at a
barrier that never entered the Q-54 typing protocol at all.

---

## 1. CHOICE LEDGER

Every choice this lane made that another lane could have made differently, with
the alternative named.

| # | Choice | Alternative not taken | Why |
|---|---|---|---|
| C1 | **A TYPE-R negative is an identifier `X` for which `X = false \| TYPE-R` (or `/ TYPE-R`) occurs at bytes.** | Treat any prose sentence carrying "TYPE-R" as a negative. | The typed-flag form is the protocol's own unit; prose mentions are commentary about flags, and counting them would inflate the population ~40%. |
| C2 | **Allow the value to sit on the line after the `=`.** | Single-line only. | My first pass was single-line and **missed 10 identifiers** written across a wrap. Corrected; see FLAG BLOCK D1. |
| C3 | **Line-wrap fragments removed by the rule "previous line ends in `_`".** | A looser heuristic. | The looser heuristic I first wrote condemned 237 identifiers including obviously real ones (`FALSIFIER_FIRED`, `DOR_013_RATIFICATION_READY`). The tight rule removes exactly 5, each verified by eye. See FLAG BLOCK D2. |
| C4 | **"Load-bearing" is operationalised as: the identifier appears in ≥2 distinct artifact BASENAMES.** | Require an explicit "because of X" citation. | No corpus-wide citation graph exists; basename spread is byte-decidable and mirror-safe (the two roots collapse to one basename). |
| C5 | **"On a live obligation" is established from the artifacts themselves, not from an obligation register.** | Read the settled-questions register. | **The register is BARRED by this commission.** This is a real methodological constraint, not a convenience — see §2.4. |
| C6 | **Q2/Q3 adjudicated at spread ≥ 3, giving 54 named barriers.** Spread-2 rows (103 further identifiers) are declared and **NOT** read. | Adjudicate all 157. | Whole-span reading of 157 sources was not reachable in this commission. The cutoff is declared, the residue is counted, and no row is silently dropped. **This is a declared sample, not a silent one.** |
| C7 | **11 of the 54 are reported as NOT-A-BARRIER and excluded from the Q2 denominator.** | Grade them as barriers. | A TYPE-R negative that refutes a *defect claim* or a *requirement* (`HIDDEN_ANCHOR_SELECTION_FOUND = false`, `P5_logically_requires_unique_complete_origin = false`) removes an obstruction rather than imposing one. Counting them as barriers would corrupt the Q2 ratio. Each is itemised in §5.4. |
| C8 | **NAMES-AN-ESCAPE is split into two displayed sub-kinds** (`CLASS-DISPLAYED-VIABLE` / `WOULD-BUILD-NAMED`). | One undifferentiated grade. | The commission's confirmed instance is the first kind ("CAN WORK"); most corpus rows are the second. Collapsing them would overstate the match to the confirmed instance. |
| C9 | **The negative-typing protocol's own definitions are marked SECOND-HAND.** | Quote them as primary. | The protocol file sits at `/Users/bgm/MB Work/alpha_supervision/`, **outside the permitted corpus**. See §2.3. |

---

## 2. CORPUS, BAR, AND WHAT COULD NOT BE REACHED

### 2.1 Roots entered

```text
ROOT A  /Users/bgm/MB Work/alpha-program-archive/workspace
ROOT B  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
        alpha_fundamental_record_action_cleanroom_v003
PLUS    DOR_* under /Users/bgm/MB Work/alpha-program-archive/supervision/
        (DOR_016 … DOR_020 and their A1–A9 amendments; nothing else there opened)
```

Permitted file list after exclusions: **5,949 files** (`.md`, `.txt`, `.json`).

### 2.2 REGISTER BAR — exclusion globs as an ARRAY, per-pattern leak counter

The exclusion set was carried as a shell **array**, never a string variable:

```zsh
typeset -a BAR
BAR=('*REGISTER*' '*TRACKER*' 'THE_PLAN*' 'ROAD_REMAINING*' 'THE_HANDOFF*'
     'OBSERVATIONS_REGISTER*' '*DECISION_SHEET*'
     'STAGE8_TYPER_ESCAPES_O46SR_V001.md')
```

Per-pattern leak counter, run against the permitted list after construction:

```text
PATTERN                             | LEAKS_IN_PERMITTED_LIST
*REGISTER*                          | 0
*TRACKER*                           | 0
THE_PLAN*                           | 0
ROAD_REMAINING*                     | 0
THE_HANDOFF*                        | 0
OBSERVATIONS_REGISTER*              | 0
*DECISION_SHEET*                    | 0
STAGE8_TYPER_ESCAPES_O46SR_V001.md  | 0   [SELF-EXCLUDED]
```

`QUESTIONSSETTLED_REGISTER_V001.md` in the second root is caught by `*REGISTER*`
and was never opened. The self-exclude is live in every sweep including the rg
index, so this artifact cannot read itself back.

### 2.3 IMPORT AUDIT — what this lane took from outside its own reading

| Import | Source | Status |
|---|---|---|
| The four-type definitions (`TYPE-R`/`TYPE-U`/`TYPE-S`/`TYPE-C`) | `/Users/bgm/MB Work/alpha_supervision/NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md:35-53`, **quoted inside** the permitted-corpus file `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:136-147` | **SECOND-HAND.** The protocol file itself is outside the permitted corpus. Everything in §3 resting on it is marked accordingly. |
| The Q-54 mandate sentence | `STAGE8_ACCESSOR_THEOREM_SUBSTITUTION_ADJUDICATION_EINSTEIN_V001.md:346` | PRIMARY — in corpus, read at bytes. |
| The FP-2 / C6 quantifier finding | `STAGE8_CERTIFICATION_RULES_O8SR_V001.md:541-578` and `STAGE8_CERTIFICATION_RULES_O8SR_AUDIT_V001.md:410-440` | PRIMARY as to those two artifacts; **SECOND-HAND as to the E1 spec v002 itself**, which is not in the permitted corpus. |
| `T_R_and_k_R_have_derived_bridge` | carried from `BOHM_GR_EM_RELATION_REFUTED:52` | **SECOND-HAND** — origin file not in the permitted corpus. Graded INDETERMINATE-AT-BYTES for that reason. |
| Logic used | Set difference over basenames; the standard reading of a restrictive relative clause; no mathematics of the object domain. | Named. |

**No numeric value of any coupling, scale, root, eigenvalue, norm or constant was
computed, approached, or transcribed anywhere in this artifact.**

### 2.4 What could not be reached, and what rests on it

The corpus contains **no barrier catalogue**. A sweep for
`BARRIER (CATALOGUE|LEDGER|TABLE|INVENTORY)`, `CATALOGUED BARRIER`, and
`catalogue of barriers` over the permitted corpus returns **0 files**. There is
therefore no pre-existing set for this commission to check against; the set in §4
is established here for the first time, which is why §1/C4–C6 declare its
construction rule rather than citing one.

Second, and more consequential: **the artifact that records which obligations are
open is the settled-questions register, and the register is barred.** "Live
obligation" could therefore only be established from the artifacts themselves.
The vocabulary sweep shows how thin the in-artifact signal is:

```text
SWEEP: obligation-status vocabulary, permitted corpus
"LIVE OBLIGATION"   | 0 hits
"live obligation"   | 11 hits   (in 5 distinct basenames)
"OPEN OBLIGATION"   | 4 hits
"still open"        | 53 hits
"LOAD-BEARING"      | 185 hits
"load-bearing"      | 2,862 hits
```

**Consequence, stated plainly:** every "live obligation" judgment in this artifact
rests on the consuming artifact's own words (`UNBUILT`, `NO_VERDICT`, `PENDING`,
`remains`, `not discharged`), never on a register row. Where a row's obligation
status could not be settled that way, the row is graded
**INDETERMINATE-AT-BYTES** rather than assumed live.

---

## 3. THE PROTOCOL AND THE CLAIM UNDER TEST

### 3.1 The mandate — PRIMARY, in corpus

`STAGE8_ACCESSOR_THEOREM_SUBSTITUTION_ADJUDICATION_EINSTEIN_V001.md:346`, whole
line, verbatim:

```text
- **Q-54:** every negative typed with test, would-build, scope, or release.
```

Four fields. The prior scout's claim that the protocol *exempts* one type is
**not repeated here**; it is false at bytes and this lane records that it did not
rely on it. All four types are covered.

### 3.2 The four types — SECOND-HAND (quoted inside a permitted-corpus artifact)

`STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:136-147` quotes
`NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md:35-53`. Whole quoted block:

```text
TYPE-R — REFUTED. A test capable of failing was executed and returned
evidence against the claim.

TYPE-U — UNBUILT. The object has not been constructed. Says nothing about
whether it can be.

TYPE-S — SCOPE-EMPTY. A bounded search returned nothing.

TYPE-C — CONSTRAINT-BLOCKED. A constraint prevented the check from running.
```

### 3.3 The narrower claim under test — CONFIRMED at bytes

Map the four mandated fields onto the four types:

```text
TYPE-R  -> test          "what was run, and failed"
TYPE-U  -> would-build   "what would have to be built"        REMOVAL-STATING
TYPE-S  -> scope         "how far the search reached"         REMOVAL-BOUNDING
TYPE-C  -> release       "what would release the constraint"  REMOVAL-STATING
```

**TYPE-R is the only type whose mandated field is a report of a completed
experiment rather than a statement bearing on what would remove the negative.**
This is confirmed at bytes and it is the structural fact this commission rests
on. A TYPE-R row can therefore stand on a live obligation with nothing in its own
four-field typing saying what would lift it.

**But — and this is the finding — the corpus mostly does not leave it there.**
See §5.

---

## 4. Q1 — THE POPULATION, DECLARED AT EVERY RUNG

Nothing here is sampled silently. Each rung states its rule and its count, and
every count below is over **the same population and the same scope**: distinct
identifiers, permitted corpus, both roots, mirrors collapsed by basename.

```text
RUNG  RULE                                                          COUNT
────────────────────────────────────────────────────────────────────────
L0    files in the permitted corpus                                 5,949
L0a   files containing the token TYPE-R                               812
L0b   occurrences of the token TYPE-R                               6,452
────────────────────────────────────────────────────────────────────────
L1    typed-negative SITES: `X = false | TYPE-R` (single- or
      multi-line form)                                              4,602
L2    DISTINCT identifiers so typed                                 1,944
L2a   of L2, line-wrap fragments (previous line ends in `_`):
      ALONE, DISCHARGES_J_REF, ENDPOINT_OPERATOR, ON_FULL_A1_FAMILY,
      _ALONE                                                            5
────────────────────────────────────────────────────────────────────────
L3    REAL distinct TYPE-R negatives                                1,939   <-- Q1 answer (a)
L4    of L3, appearing in >= 2 distinct artifact basenames
      ("consumed beyond a single artifact")                           157   <-- Q1 answer (b)
L4a   of L4, non-claim boilerplate / template / common-word tokens,
      each verified at bytes (PASS, FENCE_BLOCKED_STRUCTURAL_RESULT,
      ARE_ITS_INPUTS_PRESENT, ARE_THE_INPUTS_PRESENT,
      ARE_INPUTS_PRESENT, RELAY_ARE_INPUTS_PRESENT, Tail_R,
      TARGET_TUNING_USED, B5_DISCHARGED, B6_DISCHARGED,
      B9_DISCHARGED)                                                   11
────────────────────────────────────────────────────────────────────────
L5    ADJUDICATED SET: spread >= 3, boilerplate removed                54   <-- Q2/Q3 population
L5r   DECLARED RESIDUE: spread == 2, not read                         103
────────────────────────────────────────────────────────────────────────
L6    of L5, rows that are genuine BARRIERS
      (11 refute a defect-claim or a requirement — §5.4)               43   <-- Q2 denominator
L7    of L5, rows with >= 1 artifact that is NOT a typing artifact      19   <-- Q3 denominator
L7a   of L5, rows re-typed verbatim in >= 2 artifacts                   49
```

**How the set was decided, in one sentence:** a TYPE-R negative is load-bearing
beyond its own artifact exactly when its identifier is reproduced in a second
artifact; barriers whose identifier is reproduced in three or more were read
whole, and the 103 reproduced in exactly two are declared and left unread.

**Read L7a carefully — it is the count that most invites a mistake.** 49 of the
54 are "typed in ≥ 2 artifacts", but in the great majority that second artifact
is a **check/audit artifact quoting the flag block verbatim**, not an independent
consumer. Only **19** have an artifact that mentions the flag *without* itself
typing it. The Q3 denominator is 19, not 49, and not 54. Any ratio built on the
larger numbers would be rhetorically stronger and arithmetically empty.

---

## 5. Q2 — DOES THE SOURCE NAME A CLASS, REGIME, OR OBJECT THAT CAN WORK?

Each of the 54 was read **at the barrier and in the text immediately following
it**. Sub-kinds inside NAMES-AN-ESCAPE:

- **`CLASS-DISPLAYED-VIABLE`** — the source affirmatively names an existing class
  or object as viable (the shape of the commission's confirmed instance).
- **`WOULD-BUILD-NAMED`** — the source names the object whose construction would
  remove the negative, typically on the adjacent TYPE-U row or in the sentence
  after the flag block.

### 5.1 NAMES-AN-ESCAPE — **32 of 43 graded barriers**

Itemised in full. Barrier quoted whole, escape quoted whole.

**E1 · `C_REF_AS_WRITTEN_DERIVES_SMOOTH_DATA_FROM_GATE4` — CLASS-DISPLAYED-VIABLE**
Source: `STAGE8_7A_COMPLETENESS_PROOF_DARIO_V001.md:18-23`. Barrier and escape are
in one sentence, and the artifact is explicit that the two are different:

> **The third constituent is barred as a SOURCE. It is not excluded from the CLASS**, and
> sealed text says both things in one block — `4d` `430f0971…[20690,20930)`:
> `C_REF_AS_WRITTEN_DERIVES_SMOOTH_DATA_FROM_GATE4 = false | TYPE-R` **and**
> `C_REF_USABLE_AS_TARGET_INTERFACE = true`. FC-1 uses the same qualifier: *"barred **as a
> source**."* A TYPE-R verdict forbids deriving *from* a clause; it does not delete the moves
> from the class it froze.

This is the cleanest instance in the corpus of the door drawn beside the wall.

**E2–E5 · the four DBR coercivity/bottom barriers — CLASS-DISPLAYED-VIABLE**
Source: `STAGE8_7A_DBR_SPECTRUM_DARIO_V001.md:188-203`. Four TYPE-R rows, and the
block **immediately following** names the conditions under which a positive
theorem holds:

```text
Phi_dagger_Phi_forces_uniform_positive_public_gap    = false | TYPE-R
parent_Casimir_forces_uniform_positive_public_gap    = false | TYPE-R
unquotiented_skeleton_satisfies_public_cardinality_one = false | TYPE-R
compact_topology_forces_simple_public_bottom         = false | TYPE-R
```

> **and one positive theorem, conditional:**

```text
raw_BR_skeleton_compact_resolvent_theorem = true | TYPE-C |
  condition: smooth compact Riemannian record surface, finite-rank Hermitian
  carrier, unitary connection, smooth self-adjoint odd term, and standard
  self-adjoint Sobolev realization
raw_BR_skeleton_has_isolated_spectral_clusters = true | TYPE-C
```

Four negatives, and the very next line names the regime that works.

**E6 · `K_square_forced_by_general_composition` — CLASS-DISPLAYED-VIABLE**
Source: `STAGE8_COMPOSITION_LOOP_STRUCTURAL_PREDICTION_BUILD_V001.md:55-60`, whole
block:

```text
K_square_protocol_mandated = true
K_square_forced_by_general_composition = false | TYPE-R |
  test: compare V011's general and sequential composition laws with the
        square's required two-path commuting/confluence shape
K_square_forced_if_commuting_two_handle_diamond_is_supplied = true | CONDITIONAL
```

The escape is the next line of the same block and it is stated as `true`.

**E7 · `TREE_PHASE_DECLARED_PHYSICAL` — CLASS-DISPLAYED-VIABLE**
Source: `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md:275-278`:

```text
TREE_PHASE_DECLARED_PHYSICAL = false | TYPE-R |
  test: coker(B_N) is zero on a connected tree
RECORD_VISIBLE_SURVIVING_WITNESS = composition-loop connection pair with
  unequal K_N class along c_square
```

The refutation covers connected trees; the surviving witness is named on the
next line.

**E8 · `EXACT_ONE_TIER_DELAY_DERIVED` — CLASS-DISPLAYED-VIABLE**
Source: `STAGE8_TASK4A_NETWORK_SOURCING_LAW_ADOPTION_PROPOSAL_CODEX_LANE2_V004.md:486-489`:

```text
POSITIVE_DELAY_REQUIRED = true | inherited constraint
EXACT_ONE_TIER_DELAY_DERIVED = false | TYPE-R |
  counterfamily: every fixed positive integer delay obeys the timing constraints
ONE_TIER_DELAY = AUTHORED_NOT_UNIQUELY_FORCED
```

The counterfamily *is* the escape: an entire class (every fixed positive integer
delay) is displayed as working.

**E9 · `Misner_Sharp_and_Brown_York_candidates_coincide_at_marginality` — CLASS-DISPLAYED-VIABLE**
Source: `STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md:124-134`. Barrier
block, then the text immediately following, whole:

> This is a genuine physical/typing fork, not a convention already settled by a sealed rule. It is
> also not necessarily a binary "choose Misner-Sharp or Brown-York" act: the scale bridge requires
> the complete target-independent microscopic theory to derive the relevant Hamilton-Jacobi energy.
> The sealed text explicitly refuses automatic selection by either named energy.

A third route is named where a consumer might have read a binary.

**E10 · `V011_carrier_selection_derived_from_composition` — CLASS-DISPLAYED-VIABLE**
Source: `STAGE8_V011_COMPOSITION_LOOP_MATRIX_EXPERIMENT_RESULT_V001.md:283-288`.
The escape is inside the `test:` field itself:

```text
V011_carrier_selection_derived_from_composition = false | TYPE-R |
test: the standing sealed result says V011's composition law permits sequential
chains and never derives the commuting two-handle diamond that would
necessitate K_square.
```

**E11 · `strict_untrapped_inequality_alone_selects_unique_scale` — CLASS-DISPLAYED-VIABLE**
Read at `STAGE8_MARGINALITY_ENERGY_PHRASING_ADJUDICATION_EINSTEIN_V001.md:174-181`,
whole span including the adverse clause:

> **The strict-untrapped TYPE-R, kill boundary exact:**
> `strict_untrapped_inequality_alone_selects_unique_scale = false | TYPE-R` (BID `:136-142`,
> `:167`; register `:2503-2504`) killed **the inequality-as-selector only** — `C_R <= 1` leaves the
> half-line `T_R >= 2 sqrt(pi) t_P`, no unique cell. It never tested an expansion-based route,
> **because no such route was ever written** — that absence is TYPE-U/TYPE-S, not TYPE-R, and the
> diagnosis says so itself (`:96`: *"missing input… not a refutation of the marginality premise"*).
> It left alive the cell-boundary characterization — indeed it is the corpus's own argument for
> needing the boundary-point rule.

Note: the register citation inside that quotation is the *quoted artifact's* own
citation. This lane did not open the register.

**E12 · `response_layers_same_object` — CLASS-DISPLAYED-VIABLE, and a model row**
Read at `STAGE8_PARENT_NORMALIZATION_FROM_RECORD_STRUCTURE_DETERMINATION_EINSTEIN_V001.md:84-90`:

> - And the two response layers the two routes are built on are typed **DIFFERENT OBJECTS** by an executed
>   test: `response_layers_same_object = false | TYPE-R`
>   (`STAGE8_RESPONSE_LAYER_IDENTITY_COMPARISON_AUDIT_V001.md:36-38`).
>
> `alpha_expressible_in_derived_dimensionless_data_alone = false | NO_VERDICT | TYPE-U`, would-build: the
> Stage-10 response object and its matching map. **Not TYPE-R** — nothing refutes the possibility; the
> construction is absent.

The artifact draws the exact distinction this commission is about, unprompted.

**E13 · `internal_finite_record_algebra_terminates_tower` — WOULD-BUILD-NAMED, with explicit narrowing**
Source: `STAGE8_ROUTE1_CUTOFF_EXISTENCE_AUDIT_V001.md:79-86`:

```text
route1_cutoff_supplied = false | TYPE-U | would-build: a finite cutoff/order theorem or genuine all-orders termination theorem for the exact response-changing source-record-field action universe
internal_finite_record_algebra_terminates_tower = false | TYPE-R | test: the sealed higher-derivative theorem places the tower on continuum source/field variables plus record variables, while Gate 2/Gate 4 only constrain the finite incidence/holonomy sector and explicitly leave higher-degree or nonlocal differentials outside theorem reach
```

Text immediately following, whole:

> This is not the claim that no cutoff can exist. It is the narrower finding that
> the sealed corpus supplies no cutoff or finite-order termination for the exact
> response tower, and that the finite record incidence algebra does not by itself
> terminate that tower.

**E14 · `route4_existing_skeleton_reaches_external_continuum_sector` — WOULD-BUILD-NAMED, with explicit narrowing**
Source: `STAGE8_ROUTE4_NATIVE_FINITE_ALGEBRA_THEOREM_AUDIT_V001.md:115-129`:

```text
route4_existing_skeleton_reaches_external_continuum_sector = false | TYPE-R |
  test: Route-1 typing plus source texts; the tower's variables include
  continuum source/field variables and record variables, while the current
  native skeleton is finite stationary incidence/source-record structure and
  expressly leaves continuum, time-dependent, CTP, measure, and response layers
  unclaimed

route4_upgrade_from_derived_material_currently_supplied = false | TYPE-U |
  would-build: independent derivation of the primitive incidence/single-
  operator/quasi-free class boundary, plus response-complete coefficient
  descent and no-outside theorem
```

Text immediately following, whole:

> This is not a theorem that Route 4 is impossible. It is the narrower result
> that the current native skeleton does not supply the Route-4 closure.

**E15 · `LAW_SIDE_LIMIT_PAIR_EQUALS_COMPLETE_CTP_BOUNDARY_PACKAGE` — WOULD-BUILD-NAMED**
Source: `STAGE8_TASK4A_P3_SECOND_ATTACK_LAW_SIDE_CONSTRUCTION_AND_NARROWED_STOP_V001.md:430-443`.
Barrier, adjacent would-build, and the sentence after, whole:

```text
LAW_SIDE_LIMIT_PAIR_EQUALS_COMPLETE_CTP_BOUNDARY_PACKAGE = false | TYPE-R |
  test: completed joint carrier, preparation variation, physical boundary
        orbit/functionals, microcausal support, and boundary-form certificate
        are absent

COMPLETE_CTP_BOUNDARY_EDGE_PACKAGE_BUILT = false | TYPE-U |
  would-build: a common-origin completed joint carrier plus preparation/
               gluing variation, boundary orbit, edge reduction/functionals,
               microcausal support, global boundary-form certificate, and
               intertwiners to both exact limits
```

> This narrows the boundary stop: no new finite glue is needed. The missing datum
> is the **joint physical completion and its boundary structure**.

**E16 · `CANDIDATE_SURVIVES_RELABELING_TEST` — CLASS-DISPLAYED-VIABLE**
Source: `STAGE8_MINIMAL_OMEGA_P5_COMMON_ORIGIN_ROLE_REALIZATION_ATTEMPT_V001.md:44-57`.
Text immediately following the flag block, whole:

> This result does not refute the role route. Q-194/Q-240 remain intact: a unique
> microscopic origin is unnecessary. What fails is this particular attempt to
> realize the role without adding a generation/preparation rule.

**E17–E32 · the remaining sixteen, each with its escape located**

| # | Barrier | Source : line | Escape, located |
|---|---|---|---|
| E17 | `C7_IMPLIES_KOLMOGOROV_MARGINAL_CONSISTENCY` | `STAGE8_TASK4A_P3_SECOND_ATTACK_LAW_SIDE_CONSTRUCTION_AND_NARROWED_STOP_V001.md:252` | §3.3 next, :259 *"A complex/oscillatory measure is lawful in principle, but it still requires:"* — CLASS-DISPLAYED-VIABLE |
| E18 | `DOR015_FREEZE_LIFTS` | `STAGE8_TASK4A_DOR014_AMENDMENT1_DERIVED_PAIRING_AND_DOOR_D_REEXECUTION_V001.md:71` | the `test:` field itself names the lifting condition — *"Amendment 1 condition requires Door D to pass, not one subtest"* — WOULD-BUILD-NAMED |
| E19 | `EPOST_ENDPOINT_ORIENTATION_EQUALS_INTERACTING_I_EPSILON_PRESCRIPTION` | `STAGE8_AXN_S2_REALIZATION_DARIO_V001.md:268` | :274-276 *"A statement stronger than 'the sign is underived' is available, and it changes how the gap should be weighted."* — CLASS-DISPLAYED-VIABLE |
| E20 | `M1_IS_A_FULL_DYNAMICS_INTERTWINER` | `STAGE8_TASK4A_TRACE_KERNEL_SUFFICIENCY_ARM_LANE2_V001.md:312` | :315-323 names the missing 2PI blocks exhaustively — WOULD-BUILD-NAMED |
| E21 | `P2_SOURCE_LIMIT_IDENTIFIED_WITH_RECORD_GNS_LIMIT` | `STAGE8_TASK4A_P3_SECOND_ATTACK…_V001.md:413` | §5.2 *"Exact remaining boundary datum"*, :419-424 — WOULD-BUILD-NAMED |
| E22 | `P_ENTERS_DOOR_D_TAIL` | `STAGE8_TASK4A_SOURCE_TO_OUTPUT_NORMALIZATION_N_UNIQUENESS_INSTALL_AND_FULL_DOOR_D_REEXECUTION_V001.md:463` | :468-476 *"Door D and the source/output normalization are no longer on the residue list. The exact remaining objects are:"* + five named items — WOULD-BUILD-NAMED |
| E23 | `P_ENTERS_FINITE_ORDERED_RETARDED_SHADOW` | same file :461 | same block — WOULD-BUILD-NAMED |
| E24 | `SECTION_DERIVABLE` | `STAGE8_TASK5_EQ6_CERT_CHECK_AND_ZERO_DEFECT_SECTION_LANE1_V001.md:509` | :510 `SECTION_EXHIBITED = false / TYPE-U` on the next line — WOULD-BUILD-NAMED |
| E25 | `SECTION_DERIVABLE_FROM_CURRENT_STACK` | same file :18 | :26-30 *"The remaining stop is geometric inhabitance, not a missing rail."* — CLASS-DISPLAYED-VIABLE |
| E26 | `UNIQUE_MEMBER_FROM_DOR008_FALSIFIER` | `STAGE8_TASK4A_ACTION_COMPARISON_SQUARE_ADOPTION_PROPOSAL_LANE2_V004.md:1001` | §5.2 :1006-1014 `DOR017_ITEM :=` names the exact ratification fiber — WOULD-BUILD-NAMED |
| E27 | `UNIQUE_MEMBER_FROM_DOR009_CONVENTIONS` | same file :1000 | same block — WOULD-BUILD-NAMED |
| E28 | `UNIQUE_MEMBER_FROM_DRAFT_NORMALIZATION_CLAUSE` | same file :999 | same block — WOULD-BUILD-NAMED |
| E29 | `UNIQUE_SCALARIZATION_FORCED` | `STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_PROTOCOL_RESULT_V001.md:32` | :50-53 `U2_STATE_PORT_OPEN = false \| TYPE-U \| would-build: derive or select one omega_phys before output inspection, construct its scalar Hilbert realization and concrete rho_pre, and certify common origin` — WOULD-BUILD-NAMED. The source also refuses to close: *"The physical survivor count is therefore `NO_VERDICT`, not zero and not one."* |
| E30 | `ZERO_CONNECTED_BLOCK_IMPLIES_ZERO_ACTION_HESSIAN` | `STAGE8_LEGENDRE_ACTION_PHYS_ADOPTION_PROPOSAL_V003.md:393` | :396-400 names *"the very cycle-to-2PI tangent/action map still missing in Q-313"* — WOULD-BUILD-NAMED |
| E31 | `joint_system_determines_B0` | `STAGE8_B0_MD3_DESCENT_NON_DEGENERACY_ACCEPTANCE_TEST_V001.md:104` | :106 `Residual fiber: IprimPresentedCodomainCompatibleBoundaryOriginRealizer`, then :109-110 — WOULD-BUILD-NAMED |
| E32 | `restriction_square` | `STAGE8_LEGENDRE_ACTION_PHYS_ADOPTION_PROPOSAL_V003.md:740` | :744-745 `common_origin_provenance=false \| TYPE-U \| would-build: independent kernel-sector physical dynamics` inside the same tuple — WOULD-BUILD-NAMED |

Sub-kind split of the 32: **CLASS-DISPLAYED-VIABLE 14**, **WOULD-BUILD-NAMED 18**.

### 5.2 CLEAN — **3 of 43**

Each closes its alternatives; the closing is quoted.

| Barrier | Source : line | The closing, quoted whole |
|---|---|---|
| `LIVE_NULL_SECTOR` | `STAGE8_TASK4B_CARRIER_METRIC_AND_UNITS_PROPOSAL_LANE2_V003.md:249` | :247-252 — `VISIBLE_QUOTIENT_BRANCH_AS_OPTION = closed by theorem \| quotient is identity` / `NULL_METRIC_EXTENSION_BRANCH = scope-empty \| TYPE-S` / then *"No record-visible content is deleted: there is nothing in the kernel."* Both alternative branches are disposed on the two lines above the flag. |
| `R2_ADMITTED_BY_DOR015` | `STAGE8_TASK4B_FULLNESS_CERTIFICATE_AND_METRIC_V002_REVIEW_LANE1_V001.md:240` | :253 — *"But the antecedent is empty on the admitted family by `(T2-7)`. Hence there is no…"* The escape is closed by an emptiness result on the admitted family, not by absence of search. |
| `DOR_013_RATIFICATION_READY` | `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_V002_ADVERSARIAL_KILL_DETERMINATION_V001.md:30` | :29 — `OVERALL_VERDICT = DEAD`, and the decisive counterexample is exhibited immediately after at :34-42 (*"The decisive A1 counterexample is already V002's own nonemptiness witness."*). Closed for V002 as written. |

### 5.3 INDETERMINATE-AT-BYTES — **8 of 43**

| Barrier | Why bytes do not decide |
|---|---|
| `ANCHOR_MEMBER_SELECTED` | Sits inside a self-kill battery; the following lines are further self-kill flags, none bearing on removal. Neither escape nor closing at bytes. |
| `BACKGROUND_AND_CONSUMPTION_ONLY_REMAIN` | `test:` names an ordering (*"physical inverse/Schur package still precedes them"*), which is not the same as naming what works; following section is a kill-pass list. |
| `CANONICAL_SCALAR_F_N_FROM_RECORD_SANDWICH_ALONE` | Its first in-corpus site is a **citation** (`STAGE8_F0_COMPUTAND_CHAIN_V001.md:339`), not the typing source; the typing source (M06 / FORM B8) is reached only through that citation. **SECOND-HAND.** |
| `FREE_REFINEMENT_CATEGORY_DISCHARGES_J_REF` | Bare flag in a three-line block; following section describes an interface, not a removal condition. |
| `INCIDENCE_FORCES_GEOMETRIC_SCALE` | Same three-line block, same reason. |
| `THIN_ZERO_EXTENSION_FORCES_REFINEMENT` | Same three-line block, same reason. |
| `T_R_and_k_R_have_derived_bridge` | Carried from `BOHM_GR_EM_RELATION_REFUTED:52`, **outside the permitted corpus**. **SECOND-HAND**; not graded on a quotation of it. |
| `public_trace_rule_satisfied` | Reached only via `STAGE8_7A_DBR_PUBLIC_LAYER_DARIO_V001.md:244`, which attributes it to `SPEC`; the `SPEC` typing site was not reached in the permitted corpus. **SECOND-HAND.** |

### 5.4 NOT-A-BARRIER — **11 of 54, excluded from the Q2 denominator**

These are TYPE-R negatives that **remove** an obstruction or record that a
searched-for defect was absent. Grading them as barriers would corrupt the ratio,
so they are itemised rather than buried.

```text
CONDITIONAL_ROWS_QUIETLY_UPGRADED          audit negative: no silent upgrade found
DOR008_FINITE_FALSIFIER_FIRED              a falsifier did NOT fire
HIDDEN_ANCHOR_SELECTION_FOUND              audit negative: no hidden selection
JOINT_UNSATISFIABLE                        refutes an unsatisfiability claim
NEW_FREE_STATE_SLOT_FOUND                  audit negative: no new free slot
ONE_EDGE_ACCESS_DELETED_UPSTREAM           audit negative: nothing deleted
P5_common_origin_descent_implies_full_source_determination   removes a requirement
P5_logically_requires_unique_complete_origin                 removes a requirement
RESIDUE_ITEM_SILENTLY_DROPPED              audit negative: nothing dropped
inclusive_identity_is_P5_mutation          refutes a mutation claim
two_incompatible_alpha_formulas_found      audit negative: no incompatibility
```

**A hazard worth naming, since it is the mirror of this commission's question:**
the two `P5_*` rows are TYPE-R negatives that *widen* what is permitted. Their
source guards against exactly the converse over-read —
`STAGE8_P5_COMMON_ORIGIN_DESCENT_REQUIREMENT_V001.md:149-150`, whole:

> This does not reduce common origin to a bare existential assertion. A concrete construction trace and
> commuting descent data are required. "Some source exists" or "all fields appear in one file" is insufficient.

A barrier-removing TYPE-R can be over-read as a licence just as a barrier-imposing
one can be over-read as a wall. This lane found the source guarding against it.

---

## 6. Q3 — QUANTIFIER MATCH: SOURCE VERSUS CONSUMER

### 6.1 The sweep, run not listed

Over all 54 barriers, every artifact that mentions the identifier **and is not
itself a typing artifact** was scanned in a ±4-line window for widening tokens:

```text
PATTERN SET: "no <x> can", "cannot exist", "impossible", "impossibility",
             "in general", "general barrier", "any <x> whatsoever", "universal",
             "all routes", "every route", "no route can", "rules out",
             "excluded outright", "blanket"

RAW HITS                                              17
  of which on the identifier `restriction_square`     17
  of which genuine citations of the TYPE-R flag        0
GENUINE CONSUMER-WIDER ROWS                            0
```

**The 17 raw hits were each opened and are false positives**, verified at bytes:
`restriction_square` is a *template field name* in a door-verdict tuple, not a
citation of the flag. Two representative sites:

`STAGE8_TASK4A_FAMILY_NATURAL_PREFIX_TO_CYCLE_DESCENT_LANE2_V002.md:874-881`,
whole span — the word "impossible" belongs to `upward_square`, a different row:

```text
  restriction_square = equation (2.14) PASS,
  upward_square = equation (3.6) only on cycle-rank-preserving identity
                    extensions; impossible on cycle-creating additions,
```

`STAGE8_LEGENDRE_ACTION_PHYS_ADOPTION_PROPOSAL_V002.md:831-838`, whole span — the
word "universal" belongs to `closure_uniqueness_proved`:

```text
  quotient_exactness_proved=true | compatible right-inverse proof,
  closure_uniqueness_proved=true | projective universal property,
  restriction_square=PASS_AS_PROPOSAL,
```

### 6.2 MATCHED — six read whole, quantifier displayed on both sides

| Barrier | SOURCE quantifier, quoted | CONSUMER quantifier, quoted | Grade |
|---|---|---|---|
| `route4_existing_skeleton_reaches_external_continuum_sector` | *"the **current** native skeleton is finite stationary incidence/source-record structure"*; and *"This is not a theorem that Route 4 is impossible. It is the **narrower** result that the **current** native skeleton does not supply the Route-4 closure."* | `STAGE8_SECTOR_REACH_REQUIREMENT_V001.md:518-519`: *"This is the strongest existing TYPE-R witness that internal exactness does not **by itself** imply sector reach."* | **MATCHED** |
| `UNIQUE_SCALARIZATION_FORCED` | *"After imposing **every presently executable constraint in the relay** — normalization, U1 branch/reality compatibility, and the one-cell tensor-unit restriction — a continuum of inequivalent functionals still survives."* | `STAGE8_DESC_B03_DARIO_V001.md:302-304`: *"**`TYPE-R` is a refutation, not an absence.** The record does not merely lack a forcing argument; it has refuted the claim that **the executable constraints** force one — and refuted it constructively, with a witness family, at the exact receiver."* | **MATCHED** |
| `UNIQUE_SCALARIZATION_FORCED` (second consumer) | as above | `STAGE8_REQUIRE_G3_CHECK_V001.md:179-181`: *"Is mu forced/derivable **of record**? NO. The weights are outputs of the unbuilt scalarization/state-port pair (TYPE-R/TYPE-U). **Nothing of record** forces both nonzero; **nothing of record** computes them. mu is neither forced nonzero nor evaluable."* | **MATCHED** — "of record", thrice, not "impossible" |
| `unquotiented_skeleton_satisfies_public_cardinality_one` | quantifier: the **unquotiented** skeleton | `STAGE8_7A_DBR_PUBLIC_LAYER_DARIO_V001.md:243`: *"`unquotiented_skeleton_satisfies_public_cardinality_one = false \| TYPE-R` **closes the do-nothing option**"* | **MATCHED** — "the do-nothing option" is exactly the unquotiented case |
| `Phi_dagger_Phi_forces_uniform_positive_public_gap` + `parent_Casimir_forces_uniform_positive_public_gap` | two **named** coercivity routes | `STAGE8_7A_DBR_PUBLIC_LAYER_DARIO_V001.md:247`: *"**FREE / UNBUILT.** **Both coercivity routes** TYPE-R refuted (§2.1)"* | **MATCHED** — "both", not "all" |
| `strict_untrapped_inequality_alone_selects_unique_scale` | the inequality **alone**, as selector | `STAGE8_MARGINALITY_ENERGY_PHRASING_ADJUDICATION_EINSTEIN_V001.md:176`: *"killed **the inequality-as-selector only**"*, and *"It **left alive** the cell-boundary characterization"* | **MATCHED**, and the consumer volunteers the escape |
| `C_REF_AS_WRITTEN_DERIVES_SMOOTH_DATA_FROM_GATE4` | barred **as a source** | `STAGE8_7A_COMPLETENESS_PROOF_DARIO_V001.md:18,22-23`: *"barred as a SOURCE. It is **not excluded from the CLASS**"*; *"A TYPE-R verdict forbids deriving *from* a clause; it does not delete the moves from the class it froze."* | **MATCHED**, and the consumer is itself policing the widening |

### 6.3 CONSUMER-WIDER-THAN-SOURCE — **0 rows**

No row in the adjudicated population of 54 has a consumer that states a wider
quantifier than its source. This is the answer this commission most needed, and
it is negative.

### 6.4 CANNOT-DETERMINE — **35 of 54**

The 35 barriers with `downstream = 0`: every artifact reproducing the identifier
is itself a typing artifact (a check or audit quoting the flag block verbatim).
There is no independent consumer statement to compare a quantifier against, so
no Q3 grade is available and none is invented.

### 6.5 The confirmed instance, placed correctly — and it is NOT a TYPE-R row

The commission's confirmed instance is real and this lane verifies it at the two
in-corpus artifacts that adjudicate it.

**The barrier, whole**, as displayed at
`STAGE8_CERTIFICATION_RULES_O8SR_V001.md:543-548`:

> THE DISPLAYED IMPOSSIBILITY (E1 C6): "Equal-time localization of the 3-D
>   massless Dirac sea fails Shale-Stinespring: ||[C, 1_B]||_2 = +infinity; a
>   Lipschitz cutoff still gives int d^3 r . r^2/r^6 = int dr/r^2, divergent."
>   REAL MATHEMATICS.

**The escape, whole**, the same source's very next sentence, same block:

> ITS QUANTIFIER: **equal-time localizers.**  C6's own next sentence draws the
> boundary itself: "Only TWO-TIME / scattering-type objects, where the cell
> time integration supplies the missing decay, CAN WORK."  So C6 does not
> exclude an object of the required kind — it NAMES THE KIND THAT CAN WORK.

Corroborated independently at
`STAGE8_CERTIFICATION_RULES_O8SR_AUDIT_V001.md:426-431`, whole:

> THIS IS NOT ABSENCE-OF-PROOF.  The record's own frozen input NAMES A KIND THAT
>   CAN WORK.  The quantifier of the impossibility is equal-time localizers; the
>   complement is not merely unexcluded, it is affirmatively named as viable by
>   the same clause.  The build's FP-2 = RULE-IMPOSED call therefore rests on a
>   POSITIVE non-exclusion display, which is the strongest form the commission
>   asks for.  I could not break it.

**And now the placement, which is the structural finding of this commission:**

```text
SWEEP: is the C6 barrier typed under the protocol anywhere in the permitted corpus?
  files containing "Shale-Stinespring"                    25
  files containing "Equal-time localization"               8
  files containing "FP-2"                                 33
  occurrences of TYPE-R within +-5 lines of any
    "Shale-Stinespring" occurrence                         0
```

**Zero.** The one barrier known to have been consumed downstream as a general
wall where its source drew a door **was never run through the Q-54 typing
protocol**. It entered as an untyped impossibility sentence in a frozen external
input and was consumed as such.

This is not a defect of TYPE-R. It is the boundary of TYPE-R's coverage.

---

## 7. Q4 — THE TALLY, WITH ITS POPULATION

### 7.1 Q2 tally

```text
POPULATION: 43 graded TYPE-R BARRIERS
  = the 54 adjudicated rows (spread >= 3, boilerplate removed)
    minus the 11 NOT-A-BARRIER rows itemised at Section 5.4.
  Scope: both roots, permitted corpus, mirrors collapsed by basename,
         read at the barrier and at the text immediately following it.

NAMES-AN-ESCAPE          32 / 43   =  74%
  of which
    CLASS-DISPLAYED-VIABLE  14
    WOULD-BUILD-NAMED       18
CLEAN                     3 / 43   =   7%
INDETERMINATE-AT-BYTES    8 / 43   =  19%   (3 of the 8 SECOND-HAND)
```

### 7.2 Q3 tally

```text
POPULATION: 19 of the 54 adjudicated rows — those with at least one
  artifact that mentions the identifier WITHOUT itself typing it.
  The other 35 have no independent consumer statement in the corpus.
  Scope: identical to Section 7.1.

MATCHED                        6 read whole and displayed (Section 6.2)
CONSUMER-WIDER-THAN-SOURCE     0
CANNOT-DETERMINE              35 / 54   (no independent consumer exists)
                              13 / 19   (consumer exists but states no quantifier
                                         this lane could compare at bytes)
```

**Reconciliation against my own sweep block, as required before sealing.** My
headline says CONSUMER-WIDER is rare. My sweep returned 17 raw hits and 0 genuine
rows; the 6 rows I read whole all came back MATCHED, and four of the six
volunteered the narrowing themselves. Headline and evidence agree. The headline
does **not** say "no consumer anywhere over-reads a barrier" — 35 rows have no
consumer to test and the whole spread-2 residue of 103 was not read. What the
evidence supports is exactly: **within the 19 TYPE-R barriers of this corpus that
have a testable downstream consumer, none widens the quantifier.**

### 7.3 What follows — said plainly in both directions

**NAMES-AN-ESCAPE is COMMON (74%).** Three quarters of the graded barriers sit
next to a named door. **The recommendation this supports is narrow and it is
about reading, not re-typing:** a lane that meets a TYPE-R row and stops at the
`test:` field will, three times in four, have missed a class, regime, object, or
would-build that the same source named within a few lines. **Every catalogued
TYPE-R barrier should be re-read *with its following text*, not re-read as a
typing.** The typings are sound; it is the truncation at the flag boundary that
loses the door. This lane authored no re-typing and proposes none — describing
the gap is the whole of the mandate.

**CONSUMER-WIDER is RARE — 0 of 19, and that closes the question, which is worth
as much.** The hypothesis that this commission was built to catch — inherited
walls where sources drew doors — **does not reproduce inside the TYPE-R-typed
population.** The corpus's consumers of typed barriers are careful: they say "of
record", "by itself", "the inequality-as-selector only", "both coercivity
routes", "closes the do-nothing option". Several consumers are actively policing
the widening (E11, E12, E32 / §6.2 rows 5 and 7). **No fleet-wide re-reading is
warranted on Q3 grounds and this lane does not recommend one.**

The two results together locate the exposure precisely, and it is not where the
prior scout looked: **the risk lives at barriers that never entered the typing
protocol**, of which the confirmed FP-2 instance is one and carries zero TYPE-R
typing at bytes. That population is not enumerated here — it is not TYPE-R, and
enumerating it is not this commission.

---

## 8. SWEEP CUTOFFS — PATTERN, HITS, LEAK COUNTER

Every sweep was executed. Counts are actual.

| # | Pattern / rule | Scope | Hits | Leaks |
|---|---|---|---|---|
| S1 | file enumeration `*.md *.txt *.json` minus BAR array | both roots | 5,949 files | 0 (per-pattern table, §2.2) |
| S2 | token `TYPE-R` | permitted corpus | 6,452 occurrences in 812 files | 0 |
| S3 | `X = false \| TYPE-R` single-line | permitted corpus | 4,574 sites / 1,934 identifiers | — |
| S4 | S3 **plus** value-on-next-line form | permitted corpus | 4,602 sites / 1,944 identifiers | 10 identifiers recovered that S3 missed |
| S5 | wrap-fragment rule (prev line ends `_`) | the 1,944 | 5 removed | tightened from a heuristic that falsely condemned 237 — §9/D2 |
| S6 | identifier index (rg `-F -f`, BAR globs) | permitted corpus | 28,359 mention-lines | 0 |
| S7 | spread ≥ 2 by basename | the 1,939 | 157 | — |
| S8 | boilerplate/common-word removal, each verified at bytes | the 157 | 11 removed | — |
| S9 | spread ≥ 3 (adjudication cutoff) | the 146 | **54 adjudicated**, **103 declared unread** | — |
| S10 | Q3 widening-token set (14 patterns) over non-typing consumers | the 54 | **17 raw, 0 genuine** | 17 false positives opened and shown at §6.1 |
| S11 | `CAN WORK` | permitted corpus | 6 occurrences in 4 distinct basenames | 0 |
| S12 | `TYPE-R` within ±5 lines of `Shale-Stinespring` | permitted corpus | **0** | 0 |
| S13 | barrier-catalogue existence | permitted corpus | **0 files** | 0 |
| S14 | obligation-status vocabulary (6 patterns) | permitted corpus | 0 / 11 / 4 / 53 / 185 / 2,862 | 0 |

**Declared cutoff.** S9 is the only cutoff that discards evidence: **103
TYPE-R negatives appearing in exactly two artifacts were not read.** They are
counted, not hidden. If NAMES-AN-ESCAPE runs at the same 74% there, roughly 76
further barriers sit beside a named door — but that is arithmetic on an unread
set and it is stated as such, not claimed.

---

## 9. FLAG BLOCK

### 9.1 Fences

```text
alpha_computed        = false   [held; no coupling value approached]
proof_authorized      = false   [held; nothing proved, nothing authored]
kappa_record_computed = false   [held]
```

No numeric value of any coupling, scale, root, eigenvalue, norm, or constant was
computed or transcribed. Three quotations in §5.1/§6.5 contain symbolic
expressions belonging to their sources (`int dr/r^2`, `T_R >= 2 sqrt(pi) t_P`,
`||[C, 1_B]||_2 = +infinity`). These are **quoted spans of other artifacts,
reproduced whole for quotation integrity**, and no value was evaluated,
compared, or approached from any of them.

### 9.2 Seals — verified from each artifact's own directory

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
```

**Seal coverage is partial and this is declared, not glossed.** Sidecars exist
for 7 of the artifacts relied on; the majority of sources quoted in §5 carry no
`.seal.sha256` in the workspace. Those quotations are byte-reads at path,
unsealed. No claim in this artifact is upgraded on the strength of a seal that
does not exist.

### 9.3 Bar incidents

```text
BARRED FILES OPENED                                   0
  QUESTIONSSETTLED_REGISTER_V001.md (second root)     NOT OPENED (caught by *REGISTER*)
  any *TRACKER*, THE_PLAN*, ROAD_REMAINING*,
    THE_HANDOFF*, OBSERVATIONS_REGISTER*,
    *DECISION_SHEET*                                  NOT OPENED (leak counter 0/0/0/0/0/0)
SELF-EXCLUSION                                        LIVE in every sweep
SUPERVISION DIRECTORY                                 only the DOR_* listing enumerated;
                                                      no non-DOR file there opened
CATALOGUED NEGATIVES RE-READ                          0  (barriers were read for their
                                                      escape text; none was re-typed,
                                                      re-graded, or re-adjudicated)
AUTHORING / ADVOCACY / ADOPTION                       none
GAPS FILLED                                           none; 8 rows left
                                                      INDETERMINATE-AT-BYTES
```

One boundary note: two quoted spans (§5.1/E11 and §3.2) contain **the quoted
artifact's own citation** of a barred register and of an out-of-corpus protocol
file. Those citations are reproduced because quotation integrity requires whole
spans. **Neither file was opened by this lane**, and nothing here rests on their
contents beyond what the in-corpus quoting artifact itself states.

### 9.4 Own-draft defects — found by this lane, in this lane's work, and corrected

**D1 — MULTI-LINE FLAG FORM MISSED.** My first extraction required
`X = false | TYPE-R` on one line. The corpus also writes

```text
route4_existing_skeleton_reaches_external_continuum_sector =
  false | TYPE-R | test:
```

Ten distinct identifiers exist **only** in that form, including
`internal_finite_record_algebra_terminates_tower`,
`dimensionful_reach_necessary_for_sector_reach`, and
`dimensionful_reach_sufficient_for_sector_reach`. Population corrected from 1,934
to 1,944 before any grading. Caught by reading
`STAGE8_SECTOR_REACH_REQUIREMENT_V001.md` at bytes and noticing its flags were
absent from my own list.

**D2 — WRAP HEURISTIC OVER-FIRED.** My first line-wrap detector condemned **237**
identifiers as fragments, including `FALSIFIER_FIRED`, `DOR_013_RATIFICATION_READY`,
and `COVARIANCE_ONE_ORBIT` — all real flags sitting under an indented uppercase
line. Replaced with the byte-decidable rule "previous line ends in `_`", which
removes exactly 5, each inspected by eye. Had D2 shipped, roughly one identifier
in eight would have been wrongly deleted from the population.

**D3 — GENERIC-TOKEN CONTAMINATION.** The identifier extractor returned
`PASS` (832 basenames), `ALONE`, `Tail_R`, `ARE_ITS_INPUTS_PRESENT` and others.
These are template fields and common words, not barrier names; their apparent
"spread" is unrelated text. Each of the 11 was opened at bytes before removal —
e.g. `ALONE` at `STAGE8_R_RECORD_L_FORM_FABLE_V001.md:121` is a wrap of
`CANONICAL_SCALAR_..._ALONE`, exactly the mid-sentence line-wrap hazard the
standing discipline names.

**D4 — A COUNT THAT WOULD HAVE BEEN RHETORICALLY STRONG AND ARITHMETICALLY
EMPTY.** 49 of the 54 are "typed in ≥ 2 artifacts". Reporting *that* as the Q3
denominator would have made "0 consumer-wider" sound like a 49-row result. It is
a **19**-row result, because in 30 of those 49 the second artifact is a check
quoting the flag block verbatim rather than a consumer relying on it. Denominator
corrected before the tally; both numbers are shown at §4.

**D5 — SCOPE HONESTY.** 103 barriers of spread exactly 2 were not read. This is
declared at C6, at S9, and again at §7.3. No tally in this artifact silently
includes them, and no ratio is extrapolated onto them as a claim.

---

## 10. DISCIPLINE

- **Q-54:** every negative this lane *reports* is reported with its own source's
  typing quoted; this lane **typed no new negative** and re-typed none.
- **Q-80:** no new class constituted. `CLASS-DISPLAYED-VIABLE` and
  `WOULD-BUILD-NAMED` are **this lane's own display device** for splitting the
  commission's own grade NAMES-AN-ESCAPE, named as such, not proposed as corpus
  vocabulary.
- **BARS:** no authoring, no advocacy, no adoption. Gaps described, never filled.
  8 rows stand at INDETERMINATE-AT-BYTES rather than be resolved by inference.
- **PRESSURE, BOTH DIRECTIONS:** the escape-hunt was resisted as hard as it was
  pursued — 3 rows graded CLEAN against the lane's own thesis, 11 rows removed
  from the numerator as NOT-A-BARRIER, and the Q3 result is **negative**, which
  is the opposite of the finding this commission was set up to catch. The
  confirmed instance was *not* counted into the TYPE-R tally to inflate it; it
  was checked, found untyped, and reported as outside the population.
- **No `git` of any kind.** Artifact and both sidecars written in the archive
  workspace from its own directory. Nothing published.

```text
alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
```
