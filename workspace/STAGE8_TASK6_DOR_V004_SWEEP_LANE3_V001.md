# STAGE 8 / TASK 6 / STEP 2 — FINAL MECHANICAL SWEEP OF DoR V004

Lane: Codex Lane 3 (SOL, high effort)  
Date: 2026-08-06  
Register citation: living entry Q-547; the preflight head was Q-547  
Custody: final mechanical sweep; no adoption, ruling, execution, or gate movement

## Lead verdict

```text
DOR_V004 = DEFECTIVE (+4 items)

K1  E5 IS INCOMPLETE:
    the V001 V5-5 verb rows are restored, but the promised V001 final board
    (DECLARATION / GATE_MAP / NOT_COMPUTED / DISPOSITIONS) is absent;

K2  PART D IS FALSE:
    the V003->V004 mechanical diff contains substantive clause additions,
    deletions, re-tags, and dependency-table deletions outside P-1/E1-E5;

K3  C-V4'S VERB IS SELF-CONTRADICTORY:
    C-V4 universally asserts exhaustive enumeration and an unchanged
    remainder, while V5-5 and the conclusion say that V004 makes no universal
    carriage assertion;

K4  THE CERTIFICATE SENTENCE IS TOO BROAD:
    the anti-tuning conjunction is sound, but "no d^per certificate is of
    record" must distinguish an uninstantiated route-specific certificate
    from the sealed Q-mode schema that is VACUOUS_UNDER_M2.

RULING_READY_PENDING_SUBGATE = no.
```

The mathematical guard newly attached to P-1 is sound:

```text
ANTI_TUNING_PERIOD_CURE = PASS_WITH_CERTIFICATE_MODE_PRECISION
OUT_OF_LATTICE_TO_VERDICT_ATTACK = BLOCKED
SIX_RESTORATION_CONTENT = 5_PASS / 1_FAIL_E5
EXACT_FULL_BLOCK_VERBS = OVERSTATED
ENUMERATION = FAIL
```

Protected state remains:

```text
alpha_computed            = false
proof_authorized          = false
kappa_record_computed     = false
MEMBER_BOUND              = false
FIXED_POINT_EXECUTED      = false
END_TEST_EXECUTED         = false
NUMERIC_EVALUATION        = false
MEASURED_CONSTANT_COMPARE = none
```

## 0. Preflight and mechanical protocol

### 0.1 Preflight

| Check | Result |
|---|---|
| STEP 0 access | **PASS** — cleanroom, archive workspace, and supervision roots readable. |
| Living register | **PASS** — Q-547 was terminal at preflight; it records V004 and the fixed-string caution. |
| Artifact under sweep | **PASS** — `STAGE8_TASK6_EVALUATION_DOR_DARIO_V004.md`, SHA-256 `1e3e24289b97303bba1e8f57612e09dbace897e482ee9d25c2af35953524b000`, verified against its adjacent seal before reading. |
| Checklist sources | **PASS** — V001, V003, and the Lane-3 re-confirm verified against adjacent seals before comparison. |
| Output collision | **PASS** — this artifact and sidecar were absent from cleanroom and archive before creation. |
| Fences | **PASS** — textual comparison requires no protected operation. |

### 0.2 Sealed comparison set

| Key | Source and SHA-256 | Use |
|---|---|---|
| `V4` | `STAGE8_TASK6_EVALUATION_DOR_DARIO_V004.md` — `1e3e24289b97303bba1e8f57612e09dbace897e482ee9d25c2af35953524b000` | Subject. |
| `V3` | `STAGE8_TASK6_EVALUATION_DOR_DARIO_V003.md` — `da5b03e151bc1b391ba1c666b3c3500f3f474461d4f1e669184ad09ce905b913` | Immediate predecessor. |
| `V1` | `STAGE8_TASK6_EVALUATION_DOR_DRAFT_DARIO_V001.md` — `9704f27355ec97f447c23e180d0e52f1177b7bd713773c347061d8fe1b1616d8` | Claimed restored text. |
| `RC3` | `STAGE8_TASK6_DOR_V003_RECONFIRM_LANE3_V001.md` — `8cc53e9b1f6f1742040ed896b6aa687a26580b69a034627a7c7cc4e5d66551e3` | P-1/E1-E5 checklist. |
| `GH` | `STAGE8_TASK5_GAMMA_H_ROUTE_LANE3_V001.md` — `f2317e41367dc906ffa23f6055f2ed96a0f59f74b4e412966809d292c23e5402` | Q-mode certificate typing. |
| `AUD2` | `STAGE8_TASK5_CHAIN_CONFORMANCE_AUDIT_LANE3_V002.md` — `44202c060821728fba2c46b81b82487002e639f3242565b7a5fed387e41fcae8` | Two certificate modes. |

### 0.3 Fixed-string and diff discipline

The drafter's recorded `^`-anchor false negative was honored. Each decisive
anchor below was searched as a fixed string; regex anchoring was not used.

The immediate-predecessor comparison gives:

```text
V3 -> V4, zero-context unified diff:
  hunk groups   = 64
  added lines   = 205
  deleted lines = 135                                      (M-1)
```

The addition/deletion totals were independently summed from BSD `diff -n`'s 62
add commands and 54 delete commands. `(M-1)` is not itself a defect: restoration
and control metadata create legitimate churn. The test is whether each
substantive clause edit maps to Part C's six rows. Version, task number,
preflight-head, and supersession metadata are excluded; mathematical, gate,
disposition, dependency, and verb-audit text is not.

## 1. The six restorations, line by line against V001

### 1.1 P-1 — period cure

V001 lines 139–147 carry one continuous clause block. Its load-bearing sentence
is:

```text
The cure is carried `CARRIED-CONDITIONAL` and requires a
formed period route and the true `d^per` modulus certificate.       (P1-V1)
```

The exact fixed string beginning `The cure is carried
\`CARRIED-CONDITIONAL\` and requires a` occurs in V001 at line 142 and does not
occur in V004. V004 lines 218–231 re-render the same three terms as a separate
display and then add the availability paragraph. Normalized, V004's content is:

```text
STATUS       = CARRIED-CONDITIONAL;
CONDITION_1  = formed period route;
CONDITION_2  = true d^per modulus certificate;
AVAILABILITY = CONDITION_1 and CONDITION_2.                        (P1-V4)
```

The mathematical content is faithful and stronger against misuse. The verb
`restored in its full block` is nevertheless not literal line-level identity:
the original block is rearranged and new text is inserted.

`P-1 = PASS_SUBSTANCE / FAIL_LITERAL_FULL_BLOCK_VERB`.

### 1.2 E1 — residual A7 rule

V001 lines 170–175 and V004 lines 259–265 both display:

```text
If the prediction-map schema cannot carry both branches,
that is an unresolved gate, not permission to choose one.          (E1-1)
```

The fixed strings `If the prediction-map schema cannot carry both branches`
and `an unresolved gate, not permission to choose one` are both present in
V004. The placement is the correct V1-6 block and V4-3 retains the matching
disposition. V004 changes the surrounding provenance/rendering from V001's
`[YOURS]` narrative to a `[PROVABLE]` restoration, so it is faithful carriage,
not byte identity.

`E1 = PASS`.

### 1.3 E2 — exact arithmetic as a precondition

V001 lines 196–203 and V004 lines 290–298 both display all five listed terms:

```text
exact rational or exact symbolic arithmetic;
implementation named and hashed;
enclosures as exact rational strings (`lower`, `upper`);
precondition on every numeric step, not a post-hoc audit;
float-path result is not a value.                                  (E2-1)
```

Fixed-string hits in V004 occur for `precondition on every numeric step, not a
post-hoc` at line 296 and for the remaining terms immediately above/below. The
paragraph is split and re-tagged, so `restored in full` means full content here,
not a verbatim line block. V004 line 292 also drops V001's predicate `are
computed`, leaving `All finite-L objects in exact ... arithmetic` grammatically
incomplete; this does not defeat the targeted precondition, but independently
confirms that the block is not literal/full carriage.

`E2 = PASS_SUBSTANCE / NOT_VERBATIM`.

### 1.4 E3 — type-erasure rationale

V001 lines 275–277 and V004 lines 363–366 both carry:

```text
type preservation binds every gate;
type erasure may occur at any handoff;
the failure ladder arms it without limiting it to a step.          (E3-1)
```

Fixed strings `a failure mode that can occur at any handoff` and `without
limiting it to a step` occur at V004 lines 365–366.

The content is complete, but the formatting and connective wording differ.

`E3 = PASS_SUBSTANCE / NOT_VERBATIM`.

### 1.5 E4 — count-stop supersession

E4 does not restore V001's obsolete stop as a live rule. It must retain the
history and record the lawful supersession. V004 lines 409–410 do exactly that:

```text
V001's fifth row — a stop before Step 10 pending the count — is deleted,
and no count ambiguity remains: CELLS = six_of_record by C1.       (E4-1)
```

Both fixed-string anchors occur. The stop is not silently dropped and is not
re-activated.

`E4 = PASS`.

### 1.6 E5 — V5-5 plus the final board

V004 lines 543–566 restore six V001 V5-5 rows and retain the two K3/K4 rows as
explicitly superseded. That half passes.

The second half does not. V001 lines 438–457 contain the four-block final board.
These four fixed strings occur in V001 and return no V004 hit:

```text
DECLARATION = DRAFTED (+10 V1 clauses
GATE_MAP = BOUND (gate 0 the Step-2 ruling
NOT_COMPUTED = enumerated (9 rows
DISPOSITIONS = pre-registered (lattice cells                   (E5-MISS)
```

V004 lines 571–585 substitute a P-1/E1–E5 repair summary and only retain
`VERB_AUDIT_SELF = CLEAN`. A summary of the restoration is not the restored
final declaration/gate/not-computed/disposition board.

```text
E5_V5_5_ROWS   = PASS;
E5_FINAL_BOARD = ABSENT;
E5             = FAIL.                                           (E5-1)
```

### 1.7 Six-item result

```text
CONTENT:
  P-1, E1, E2, E3, E4 = PASS;
  E5                   = FAIL (final board absent).

LITERAL FULL-BLOCK CLAIMS:
  P-1, E2, and E3 are faithful re-renderings, not literal block reproductions;
  E5 is incomplete, not merely re-rendered.

SIX_RESTORATION_CONTENT = 5_PASS / 1_FAIL_E5.                    (R-6)
```

## 2. Enumeration audit: Part D is not empty

### 2.1 Part A's `unchanged` assertion fails

V004 Part A calls D1, D2, and U1–U5 `carried from V003, unchanged`. Fixed-string
comparison produces direct counterexamples:

| Witness | V003 fixed string / line | V004 result | Mechanical finding |
|---|---|---|---|
| A1 | `ALPHA-RESULT-SEAL and its four parents = certified;` at line 99 | no hit | D1's displayed `(F-1)` valuation and its explanatory block were deleted. |
| A2 | `[YOURS] The display standard is the point:` at line 386 | no hit | D2's self-correction/display-standard paragraph was deleted. |
| A3 | `\| Rendering \| Direct consumers re-walked \| Result \|` at line 465 | no hit | U4 Table B's Result column and all four findings were deleted; Table C's Result column was also deleted. |
| A4 | V003 V3 ends `local route is a **shadow** route.` | V004 adds three anti-mistaking lines at 389–391 | U5 is changed, not unchanged. |

These are clause/audit changes, not version metadata.

### 2.2 Substantive edits with no Part-C row

The following independent witnesses remain after assigning the advertised
P-1/E1–E5 edits:

| ID | V3→V4 edit | Why Part C does not enumerate it |
|---|---|---|
| X1 | Delete V003 lines 95–110: D1's `(F-1)` valuation and internal-inconsistency reasoning. | Part A calls D1 unchanged; no Part-C row names deletion. |
| X2 | Add/re-tag V1-10 at V004 lines 313–315 with the `LOCAL-SHADOW` assembly sentence. | No Part-C row names V1-10. |
| X3 | Add `ladder is unformed at its root, not partway up` at V004 lines 368–370. | E3 names the type-erasure rationale only. |
| X4 | Add the V3 anti-mistaking rationale at V004 lines 389–391. | Part A calls U5 unchanged. |
| X5 | Add the pre-registration timing clause at V004 lines 397–398. | No Part-C row names the V4 preamble. |
| X6 | Expand cell 4 with the alternate-metric/MODULUS_CERT explanation at V004 line 406. | E4 names only the count-stop sentence. |
| X7 | Expand the chi-zero/polar conflation paragraph at V004 lines 421–424. | No Part-C row names V4-2. |
| X8 | Delete V003 lines 386–388, D2's display-standard self-correction. | Part A calls D2 unchanged. |
| X9 | Delete the Result columns and conclusions from U4 Tables B/C at V004 lines 512–525. | Part A calls U4 unchanged. |

One witness suffices to refute an exhaustive enumeration; X1–X9 are nine.

### 2.3 P-1's new consumers are not delta rows

Part C's P-1 row names only `(V1-5)` and says `restored in its full block`. V004
also changes:

```text
(V1-5)  new availability paragraph, lines 226–231;
(V5-2)  new cure anti-tuning row, line 481;
(V5-3)  new d^per rail, lines 491–492;
(V5-5)  new P-1 verb row, line 565;
final    new P-1 summary, lines 573–576.                          (P1-D)
```

Table D of the dependency re-audit mentions some consumers, but it is not the
§0.2 delta board that C-V4 calls complete. `(P1-D)` therefore gives a second,
independent enumeration failure.

### 2.4 Delta verdict

```text
PART_C_ROWS_PRESENT         = yes;
PART_C_SIX_LABELS_GENUINE   = yes;
PART_D_EMPTY                = false;
NOTHING_UNENUMERATED_CHANGED = false;
C_V4_ENUMERATION            = FAIL.                              (D-FAIL)
```

## 3. The new anti-tuning row

### 3.1 Correct typing of availability

The cure's lawful availability is mode-specific:

```text
CURE_AVAILABLE_OF_RECORD(a,epsilon,r,Q)
  := ROUTE_FORMED_TRUE_OF_RECORD(a,epsilon,r)
     and M2_SUBJECT_FORMED_TRUE_OF_RECORD(a,epsilon,r)
     and PERIOD_MODULUS_COMPATIBILITY_CERT_TRUE_OF_RECORD
           [a,epsilon,r;Q];
// for r=H in the direct-M2 presentation, the last conjunct is
// VACUOUS_UNDER_M2 once that M2 subject is formed; this is not asserted
// route-generically.

CURE_AVAILABLE_OF_RECORD(a,epsilon,r,FACTOR)
  := ROUTE_FORMED_TRUE_OF_RECORD(a,epsilon,r)
     and FIXED_PERIOD_FACTOR_CERT_TRUE_OF_RECORD(a,epsilon,r)
     and PERIOD_MODULUS_COMPATIBILITY_CERT_TRUE_OF_RECORD
           [a,epsilon,r;FACTOR].                                  (AT-1)

CARRIED-CONDITIONAL does not imply either availability predicate. (AT-2)
```

V004 lines 218–231 state the coarse two-conjunct guard and forbid use of the
carriage label to turn the current out-of-lattice reading into a verdict. Its
V5-2 row repeats that guard. `(AT-1)` resolves it mode-specifically from `GH`
and `AUD2`; `(AT-2)` is V004's correct anti-tuning content.

### 3.2 Certificate-mode precision

The sealed stock distinguishes modes:

```text
PERIOD_MODULUS_COMPATIBILITY_CERT[a,epsilon,H;Q]
  = VACUOUS_UNDER_M2 in the direct-M2 presentation;               (AT-Q)

PERIOD_MODULUS_COMPATIBILITY_CERT[...,FACTOR]
  = a live debt unavailable without formed route subjects.        (AT-F)
```

`GH` lines 745–756 display the H-route `(AT-Q)`/`(AT-F)` split; `AUD2` lines
213–230 type both modes route-generically. The H-route Q-mode statement is
schema-level: without a formed route and its `M2` subject, it does not
instantiate a cure. Other routes retain their route-specific Q-certificate
conjunct. Consequently neither current availability predicate is established:
the route and its subject are unformed of record, not proved nonexistent.

V004's sentences `no d^per modulus certificate is of record` and `both
conditions are unmet` are too broad unless read as:

```text
no instantiated route-specific certificate in the mode consumed by a
formed route is of record; the H/direct-M2 Q-mode schema is
VACUOUS_UNDER_M2 but has no formed-route instance, and no such vacuity is
silently exported to another route.                               (AT-R)
```

`(AT-R)` is the required precision repair. It does not weaken the guard.

### 3.3 Fresh attack

Attempt:

```text
seed = 0;
chi_K = polar / OUT_OF_LATTICE;
CARRIED-CONDITIONAL is misread as AVAILABLE;
the H/direct-M2 Q-mode schema is cited as VACUOUS_UNDER_M2;
an outcome is requested through the period cure.                  (FA-1)
```

Structural reduction:

```text
ROUTE_FORMED_STATUS = UNFORMED_OF_RECORD;
therefore neither mode's CURE_AVAILABLE_OF_RECORD predicate is established,
and CERT_instance is unformed;
therefore invocation is barred and (FA-1) cannot convert
OUT_OF_LATTICE into a verdict.                                    (FA-2)
```

V004 lines 226–231 and 417–423 block exactly this move. The fresh attack is
blocked even after the Q-mode schema is granted; the route/subject conjunct is
not true of record and is independently decisive.

```text
FRESH_ATTACK = BLOCKED;
ANTI_TUNING_PERIOD_CURE = PASS_WITH_CERTIFICATE_MODE_PRECISION.    (FA-3)
```

No seed was evaluated and no end test was run.

## 4. Verb audit and consequence

### 4.1 V004's internal verb contradiction

The fixed string at V004 line 73 says:

```text
Every V002->V003 and V003->V004 clause edit appears as a delta row. (CV-A)
```

Lines 74–75 add that the list is complete and anything else is unchanged. This
is a finite universal exhaustiveness assertion. V004 line 566 then says:

```text
V004 makes no universal carriage claim.                            (CV-B)
```

The conclusion repeats `(CV-B)`. `(CV-A)` and `(CV-B)` cannot both be true.
The lawful repair is not to remove the finite test; it is to say:

```text
V004 makes no unbounded/class-wide clause-carriage claim;
V004 does make the finite universal enumeration claim C-V4.        (CV-R)
```

Because `(D-FAIL)` also falsifies the finite claim on the present text, the
current `VERB_AUDIT_SELF = CLEAN` cannot stand.

### 4.2 Finite repair board

No new physics is required. A bounded redraft must:

1. append the actual V001 four-block final board, or enumerate and justify its
   supersession instead of claiming E5 restoration;
2. enumerate X1–X9 and every P-1 consumer in §0.2, or revert those edits
   line-for-line to V003;
3. replace the `no universal` sentence with `(CV-R)`;
4. replace the broad certificate sentence with `(AT-R)`;
5. reserve `restored in full block` for literal block reproduction and use
   `faithfully re-rendered` where the text is reorganized.

Until then Step 2 is not ruling-ready, independently of the still-false M5a
subgate.

### 4.3 Surface, fences, and self verb audit

| Surface | Result |
|---|---|
| LOCAL-SHADOW typing | Preserved; no promotion. |
| A7 carriage | Local vacuity preserved; ZERO and IDENTITY retained for later period machinery. |
| Six-cell lattice | Preserved. |
| P-1 anti-tuning | Sound after certificate-mode precision. |
| Reader/fixed point/end test | Not consumed or executed. |
| Numeric/measured data | None formed or accessed. |
| Cross-sector unit | No bridge or silent unit introduced. |

`MACHINERY-APPEAL = none`.

| My verb | Display | Result |
|---|---|---|
| `PASS` | P-1 substance, E1–E4, and `(AT-1)`–`(FA-3)` | **CLEAN** |
| `FAIL` / `DEFECTIVE` | `(E5-1)`, X1–X9, `(D-FAIL)`, `(CV-A)`/`(CV-B)` | **CLEAN** |
| `line-level` | Fixed strings and exact source/subject line locations | **CLEAN** |
| `mechanical` | 64 hunks plus two independent line-count methods | **CLEAN** |
| `not ready` | E5, enumeration, and verb failures remain | **CLEAN** |

No draft is called adopted, no process defect is promoted to a mathematical
refutation, and no gate is called open.

## Final board

```text
REGISTER_HEAD_AT_PREFLIGHT       = Q-547
V004_HASH                       = 1e3e24289b97303bba1e8f57612e09dbace897e482ee9d25c2af35953524b000
P1_CONTENT                      = PASS
E1                              = PASS
E2                              = PASS
E3                              = PASS
E4                              = PASS
E5                              = FAIL_FINAL_BOARD_ABSENT
SIX_RESTORATION_CONTENT         = 5_PASS_1_FAIL
EXACT_FULL_BLOCK_VERBS          = OVERSTATED
PART_D_EMPTY                    = false
C_V4_ENUMERATION                = FAIL
ANTI_TUNING_PERIOD_CURE         = PASS_WITH_CERTIFICATE_MODE_PRECISION
FRESH_ATTACK                    = BLOCKED
V004_VERB_AUDIT                 = NOT_CLEAN
M5A_SUBGATE                     = false_of_record
alpha_computed                  = false
proof_authorized                = false
kappa_record_computed           = false
MEMBER_BOUND                    = false
NUMERIC_EVALUATION              = false
MEASURED_CONSTANT_COMPARISON    = none
MACHINERY_APPEAL                = none
```

DOR_V004 = DEFECTIVE (+E5 final-board restoration incomplete; +Part-D unenumerated substantive edits; +C-V4 universal-claim contradiction; +certificate-mode wording)
RULING_READY_PENDING_SUBGATE = no
VERB_AUDIT_SELF = CLEAN
