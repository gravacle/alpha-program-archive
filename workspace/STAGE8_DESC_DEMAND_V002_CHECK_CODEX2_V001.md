CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
CLOSURE_END_BYTE = 00002836
FIRST_SUBSTANTIVE_BYTE = 00002838
PREDECLARATION_REGION = EMPTY
PREDECLARATION_OUTPUT_SCAN = 0 hits for this artifact and its sidecar
VERDICT_BEARING_SET = exactly the 12 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = CODEX 2
ROLE_THIS_RELAY = opposite-lane spot-check of the fold; prior findings are references, not self-verified conclusions
```

| # | Closed member | SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_991_DEMAND_V002_CHECK_CODEX2_V001.md` | `9416e8c48d76343b42a3dd9cb693d1d6bb4e16eb42936ddfaf9a2229632850d3` | assignment |
| 02 | `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | pinned program state |
| 03 | **SUBJECT** `STAGE8_DESC_DEMAND_DARIO_V002.md` | `c883d3732af61800f6ac2219e87406ccbbae60f7928172a80281e2e2cae951e3` | demand V002 under check; verified against its own sidecar before reading |
| 04 | `STAGE8_DESC_DEMAND_DARIO_V001.md` | `da32dc9dfff38a32668b673e0c1b9e05fee27d02cd49b2f7ed99a78b71c51da9` | byte-carriage base |
| 05 | `STAGE8_DESC_DEMAND_CHECK_CODEX2_V001.md` | `f3704df1bc4d7b2f45833fb12a40352117751e8f1b036ba0ab7de9fd4cfa1414` | relay-987 reference findings; not re-adjudicated here |
| 06 | `STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` | `2b6291227b7ac5967796014c2ad217c9eb084b5bb6df23fed0a7bca464e8bfab` | no-inspection/common-origin source |
| 07 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V004.md` | `a195edb03b36be44bf8ce1b71dbf1a01a3a0956c4afc65ddf17382cdca4ed0ab` | Q20 and SM-row source |
| 08 | `STAGE8_AXN_ENTRY_DECISION_INSTRUMENT_CODEX2_V002.md` | `af26ab0354420f64718942b9bdcc61a4e6826a885b7ac0440988a25d7f0c95e1` | Q21 source |
| 09 | `STAGE8_AXN_B0_ACCEPTANCE_INVERSE_CODEX2_V001.md` | `ae93720f5f5534a8d0d9915ab84368639f3fd96927b0d51a206a35c6b40b6019` | U7–U10 consumer clauses |
| 10 | `STAGE8_B0_MD3_DESCENT_NON_DEGENERACY_ACCEPTANCE_TEST_V001.md` | `23f5427159b2505a29629b28a3985f33efd090f5e852f43a337e58f4b0d5270f` | U11 consumer |
| 11 | `STAGE8_AXN_STATE_ALGEBRA_MAP_CODEX2_V001.md` | `a67ed4352e939bd92e886672b9dfdb848cfcaa453a3760f0daa83d6586d60782` | U12 placement source and boundary finding |
| 12 | `STAGE8_TASK2D_MULTIAXIAL_STATE_TRANSITION_ENVELOPE_SPECIFICATION_V001.md` | `bda00e99e964bd75d60429549e5f6c70762bf1607270b9a6294dc4c97cf2c635` | PathCert schema source |

Every member and adjacent sidecar passed before substantive reliance. The subject and V001 were
compared directly; source spans used below were rehashed from sealed bytes. Files inspected only for
hash existence outside this set receive no premise, inference, or verdict weight.

CLOSURE_DECLARATION_END

# STAGE 8 — DESCENT DEMAND V002 SPOT-CHECK — CODEX 2 LANE
## RELAY 991 — `[PLAN:DESC-7]` — FOLD, CARRIAGE, AND COUNT

Date: 2026-08-11  
Verdict: **REMAINS.** The 35+1 acceptance shape re-derives and the three substantive corrections are
present, but the artifact cannot register its requested closure claim: U12's state-map citation is
not right-closed, the byte-verbatim carriage claim is false, and the H1–H13 table is a semantic change
inventory rather than the actual unified diff.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Method and jurisdiction

This is the opposite-lane check of Dario's V002 fold. Relay 987 supplies the authorized reference
list U7–U12 and the three corrections. Builder-never-verifies is preserved: this report does not
re-rule those earlier findings; it asks whether V002 folded them at the cited consumers, applied the
three corrections, carried V001 as claimed, accounted for its delta, and recomputed the unified
condition count.

The checks were mechanical and structural:

1. rehash each U7–U12 span and inspect both byte edges;
2. compare conditions 1–18 field-by-field between V001 and V002;
3. test each V001 O1–O4/U1–U6 table row for exact byte presence in V002;
4. run a unified V001→V002 diff with three context lines and count hunks, insertions, and deletions;
5. recount the numbered condition rows under the subject's declared atomicity.

No feasibility, construction, selector, or physical-value question is reached by those procedures.

## 2. U7–U12 fold replay

| Fold | Sealed span replay | Edge check | V002 condition mapping | Result |
|---|---|---|---|---|
| U7 — A01–A05 | B0 acceptance `[7262,10112)`, `843c25b5f88255919b20587fe25fecc8b5d908974af50b5aa4af8b0094088b70` | begins `### A01`; ends immediately before A06 | 19–23 | **RIGHT-CLOSED** |
| U8 — A06–A09, with A08 already condition 13 | `[10112,12021)`, `5d3a233b21eda18b06975b786ff5e2d11cc289247ac1b258f90be7baf9d7efe3` | begins `### A06`; ends immediately before A10 | 24–26; no A08 duplicate | **RIGHT-CLOSED** |
| U9 — A10–A13, with A12 already condition 5 | `[12021,13587)`, `1944cfd0553316c6401cb008e68894f1a26672ec5bfb0e6fc1eed6e160038e8b` | begins `### A10`; ends immediately before A14 | 27–29; no A12 duplicate | **RIGHT-CLOSED** |
| U10 — A14–A17 | `[13587,19040)`, `c48efc3118bdcd0a0221ec0ec1c91a7bd3b9b68dea2357b669262f522d57f04e` | begins `### A14`; closes A17 and its controls before the next section | 30–33 | **RIGHT-CLOSED** |
| U11 — MD-3 | `[8794,11563)`, `d37bddd34151f7986c51719b9537487427855a97c9bdaac96c49bb5137a83378` | begins `## 4. MD-3 acceptance test`; closes its negative controls before the next section | 34 | **RIGHT-CLOSED** |
| U12 — StatePort placement | state-map `[16822,17244)`, `7b1ee5198923d54eb03d3f0942acfa8a8dfed7d96fa7edbdf2b20658da06ee47`; instrument SM rows `[36914,38169)`, `35030c25f9cd3343bb848cefdd8336e68745a393f5d300833ac89a51c001467a` | SM span is closed; state-map span begins on prose, not a heading, and ends after `Therefore the exact missing composition is:` but before that composition | 35 | **NOT RIGHT-CLOSED** |

The U12 condition is materially supported by the companion SM table—especially SM-4, SM-6, and
SM-7—but that does not make the subject's state-map citation right-closed or make its statement
“all six spans open exactly on a clause heading and close exactly on the next” true. The omitted
bytes `[17244,17540)`, span SHA-256
`d3d545b052817637a6ba33098cd177eb157ffeaf32b00c03c905c2e9cb8788e5`, display the
`MISSING_COMPOSITION` object, including the common-origin producer, joint state/density, commuting
placement square, and provenance/no-supplementation certificates.

The smallest heading-to-heading correction is the complete state-map §4 span `[16298,17631)`,
SHA-256 `2fd79b2e25c7afc381df9b65f7195b8aa0954b729d4b84c37292490a7653e012`.
This report does not amend the subject; it records the repair boundary.

## 3. Three corrections

| Correction | Replay | Result |
|---|---|---|
| no-inspection split | U2 C6 `[23900,24472)`, `19d3ca3fe6573d2714e08e3d2bec05ef6ec2a52547cccb7d45dc835dfd8c1431`, supplies the temporal words and names the ad-hoc assembly; A15 supplies the independent provenance conjunction | **APPLIED** |
| PathCert partial form | `[19909,21513)`, `02e56051cb65a2428f86111064205f8aa137117889c1d54e669ce02bdc73915f`, supplies the tuple and commuting fields; V002 leaves exact canonical serialization/digest open and the instance absent | **APPLIED** |
| quote attributions | Q20 at instrument `[39637,39732)`, `7803f1a8cf15293faf673e4c9daedbb1cbe13f3b22c734a1fea3bee2941048e8`; Q21 at entry decision `[20579,20661)`, `5895a4ab33eccfb7fb533d8c5ba2ce98f16119df0aea7d21c0cc949f293252dc` | **APPLIED** |

Thus the substantive correction tally is **3/3**. One self-description inside correction 1 is not
accurate: §1.1 says conditions 15 and 16 keep “their numbers, their text, and their grounds,” while
the V002 table adds labels to both texts and adds A15 to condition 16's ground. Those additions are
lawful correction content, but they must be reported as changes rather than called byte-identical.

## 4. Byte carriage and hunk table

### 4.1 Conditions 1–18

A field-by-field comparison gives:

```text
CONDITION_TEXT_EXACT = 15/18
CONDITION_TEXT_CHANGED = 13, 15, 16
GROUND_FIELDS_REKEYED_OR_EXTENDED = 18/18
```

Conditions 13, 15, and 16 add, respectively, the delivery-constraint annotation, the temporal label,
and the compositional/provenance label. These are authorized and appear in the subject's H4/H5/H7
accounting, but they refute H2's statement “no condition text altered” and the final claim that only
ground columns changed.

### 4.2 O1–O4 and U1–U6

All ten V001 table rows were tested as exact lines against V002:

```text
V001_OU_ROWS = 10
EXACT_OU_ROWS_PRESENT_IN_V002 = 0
```

V002 summarizes their labels and says they stand; it does not carry the ten rows byte-for-byte.
This is semantic carriage, not byte-verbatim carriage. The statements in §7, §8, and the final lines
that the O/U tables travel byte-for-byte are therefore false.

### 4.3 Actual unified diff

The direct three-context unified diff returns:

```text
ACTUAL_UNIFIED_HUNKS = 2
INSERTIONS = 359
DELETIONS = 323
```

The subject's H1–H13 table is useful as a **semantic change-class inventory**, but it is not a table
of the actual unified diff hunks. Because the body was reorganized nearly continuously, the raw diff
has two hunks: closure metadata and the rewritten body. Consequently the claims “thirteen-hunk
V001→V002 accounting,” “13 hunks,” and “nothing was deleted” do not survive byte comparison.

H12 also does not describe the closure-set delta exactly. V001's 10-row set is not a subset of
V002's 14-row set: the assignment is replaced, and V001's register/process/decline and induction-
provenance rows are not present in V002's closure. “Members 07, 11, 12, 13, 14 added; nothing
removed” is neither a finite member-set delta nor arithmetically sufficient to turn 10 into 14.

The repair is documentary, not mathematical: label H1–H13 as semantic delta classes; supply the
actual two-hunk/359/323 diff certificate; replace broad VERBATIM claims with a precise 15/18 condition-
text result plus semantic O/U carriage, or restore the V001 bytes literally; and give the exact
closure member-set replacement.

## 5. Unified count re-derived

The count is internally consistent under the subject's declared atomicity:

```text
V001_OBJECT_CONDITIONS = 18
A01_A17_NEW = 17 - 2 already carried (A08=condition 13; A12=condition 5) = 15
MD3_NEW = 1
PLACEMENT_NEW = 1
OBJECT_CONDITIONS_TOTAL = 18 + 15 + 1 + 1 = 35
VERDICT_RELATIVE_COVERAGE = 1
UNIFIED_SHAPE = 35 + 1 verdict-relative
```

The numbered table contains rows 1–36 exactly once. The four-field stack remains a mandatory
upstream prerequisite rather than a numbered condition, and K7 remains condition 18 as a downstream
receiver. No weakening, duplicate A08/A12 row, or count target was used to obtain 35+1.

## 6. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT   = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the relay-987 reference list without re-adjudication; V001 and V002 sealed bytes; the six consumer
  groups and three correction sources at their pinned spans; the standard gates.

DERIVED HERE:
  span-edge results for U7-U12; the U12 omitted/full-section span hashes; 15/18 exact condition-text
  carriage; 0/10 exact O/U-row carriage; the actual two-hunk 359/323 diff; the structural 35+1 count.

SELECTED HERE:
  nothing. No descent object, candidate, trace, map, certificate instance, manifest, measure,
  omega_phys, acceptance branch, or release route is constructed, supplied, selected, or scored.

SCALING WEIGHTS:
  none consumed, fixed, formed, compared, or substituted.
```

## 7. Flattening, blind, and custody

- **F_PLDEC:** only byte hashing, text comparison, set membership, span boundaries, and finite
  structural counts were evaluated. No physical quantity or response was evaluated.
- **ANTI-TUNING:** the 35+1 recount follows the subject's declared atoms and duplicate exclusions;
  no row, source boundary, or correction was changed to obtain a desired verdict.
- **FLATTENING CHECK:** material support for condition 35 is not a right-closed citation; semantic
  carriage is not byte carriage; a semantic change-class table is not a unified-diff hunk table; an
  authorized text addition is not byte identity; a field schema is not canonical serialization or
  an instance; the four-field prerequisite is not a numbered P5 component; K7 is not a field.
- **BLIND HELD:** no rank, ratio, response value, fiber value, physical quantity, or measured constant
  was read, formed, evaluated, or compared. All scales remain symbolic.
- **PE-1..PE-16:** pointer-only, zero verdict weight.
- **BUILDER-NEVER-VERIFIES:** relay 987's findings were treated as the authorized checklist. This
  report verifies only V002's fold, sources, carriage, diff, and count.
- **PIN CHECK:** all 12 closure members and adjacent sidecars passed. The subject's own sidecar was
  verified before reading. The output artifact and sidecar names were absent before authoring.
- **DOES NOT DO:** no member binding, fixed-point execution, end test, chain run, construction,
  adoption, principal freeze, proof authorization, physical numeric evaluation, comparison to a
  measured constant, or board movement.

Verb audit: **CLEAN**. “Applied” refers to the presence of corrections in the opposite-lane subject;
“derived here” is limited to byte spans, diff statistics, and a finite structural count. No descent
object is claimed built, no selector is exercised, and no downstream verdict is evaluated.

CLOSURE = declared-first (byte 0; closure end 2836; first substantive byte 2838; scan 0 hits)
SUBJECT_DIGEST = c883d3732af61800f6ac2219e87406ccbbae60f7928172a80281e2e2cae951e3
FOLD = U7-U11 RIGHT-CLOSED; U12 FAILS state-map boundary `[16822,17244)`
CORRECTIONS = 3/3
CARRIED = NOT-VERBATIM (15/18 condition texts; 0/10 O/U table rows; actual diff 2 hunks)
COUNT = RE-DERIVED (35 conditions + 1 verdict-relative)
VERDICT = REMAINS (U12 right-closure; byte-carriage and unified-diff certificate)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
