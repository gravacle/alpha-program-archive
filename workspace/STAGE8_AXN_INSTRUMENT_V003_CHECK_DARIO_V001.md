CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; no text precedes it)
PREDECLARATION_OUTPUT_SCAN = 0 hits in authored prose (27-token sweep)
VERDICT_BEARING_SET = exactly the 8 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = DARIO (verifier)   SUBJECT_LANE = CODEX 2 (producer)
SEVERITY_BAR = corruption of a governing act (the 918/921 standard)
STANDING = my 952 ruled the item this repairs; it defines what must be answered, and certifying
           that it was answered is a separate act
```

| # | Closed member | SHA-256 / bounded span SHA-256 | Role |
|---:|---|---|---|
| 01 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V003.md` | `79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e` | the subject under check |
| 02 | `relay_inbox/RELAY_PASTE_958_INSTRUMENT_V003_CHECK_DARIO_V001.md` | `77735ae2a230928fd37e0e2eef152727858fcb2304136274afe3c581e63a760b` | assignment |
| 03 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V002.md` | `58b966ed371b23b29b9e3ceed280eb30c804484becb2b17ca6ea465668e951bc` | the superseded instrument; byte-copy base |
| 04 | — V002 suite `[22341,23332)`; anti-flattening guard `[23337,23541)`; JAC-11 escape at byte 20989 | `ccbdeed389ebd45603ef49e6e6858d2ac0ad5ec96cfa5c458e1d7e03c017d450`; `f60997825571eb47685d1790beaa465aef0832eec67c3832ab51554e1e38bf86` | the repaired field; the guard; the neighbour the escape is drawn from |
| 05 | `STAGE8_AXN_INSTANCE_V003_CROSSCHECK_DARIO_V001.md` | `477847430c1e36a470c736e953d5b66c237cc03ebf1a0356c3382b6869a15497` | my 952 four-leg ruling — ground 2 of the repair |
| 06 | `JOINT_ANCHOR_DECISION_INSTANCE_V003.md` | `089af246cbc0d66e6ce70971dbb14d355a78ee0f5e294706a1acaeacd0d4236d` | ground 1, the boundary display |
| 07 | `STAGE8_AXN_GAUNTLET_RUN2_CODEX2_V001.md` | `fff09aba84500f339b12bc5cab6b888d7d2981c88b8222346d33231ddb204a15` | ground 3, the run-2 rejection at the G0 receiver |
| 08 | `PROGRAM_STATE_BRIEF_V005.md`; `LOCKED_PROCESS.md`; `DECLINE_REGISTER_V002.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`; `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb`; `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | state pin, process law, S01-S37 authority |

```text
ALL THREE GROUNDS RESOLVED BY DIGEST TO ACTUAL SEALED ARTIFACTS, INCLUDING MY OWN 952.
SUBJECT SEAL VERIFIED BEFORE READING.  NUMERAL GREP RUN OVER EVERY COUNT-BEARING SENTENCE.
```

CLOSURE_DECLARATION_END

# STAGE 8 — AXN INSTRUMENT V003 CROSS-CHECK — DARIO LANE — V001
## RELAY 958 — `[PLAN:AXN-BUILD-D57]` — THE ONE-CLAUSE REPAIR

Date: 2026-08-10
Status: **THE REPAIR ANSWERS ALL FOUR OF MY LEGS AND DODGES NONE. VERDICT:
READY-FOR-THE-PRINCIPAL, with one non-blocking observation on two deleted attestations.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. The bar, stated first

The severity bar here is **corruption of a governing act**, and it is the highest-stakes object in this
series: the subject supersedes the instrument that governs an act already ADOPTED-AND-FROZEN, so a
defect would not merely mislead a round — it would alter the terms under which a frozen act was
approved.

The bar cuts both ways. **A repair that genuinely answers my ruling must be allowed to pass**, and I do
not get to keep a field open because I was the one who closed it. The relay states the test exactly:
*a repair that dodges rather than answers your legs is not a repair.* So I take each leg in turn and
ask whether the objection **dissolves** or is merely routed around.

## 2. The clause, tested leg by leg [PROVABLE — ALL FOUR ANSWERED]

The repaired field is `finite_stage_inventory: exactly one closed variant { FINITE_ENUMERATION | BOUNDED_CLASS }`.

**LEG 1 — the category substitution.** My objection: the receipts fill a *separate* schema key, so
offering them as the inventory is a substitution the key structure forbids. **Dissolved, and carefully.**
`BOUNDED_CLASS` does not put the receipts in the inventory's place. It demands seven distinct
components — a `bounded_class_definition`, the universal receipts, an `ordered_receipt_root_sha256`,
an `explicit_reopening_trigger`, and a `for_class` bundle — and it adds
`outer_receipts_identity: exact byte/digest identity with restriction_and_limit_square_receipts`, which
**forces the inner copy to BE the outer field rather than a second list**. That is the opposite of a
substitution: the separate key survives, and double-counting is explicitly barred.

**LEG 2 — the per-entry demand and the empty inventory.** My objection: `for_each_stage` demands a
`delta0_basis`, a `phi_restriction_matrix` and six certificates per entry, none of which exists as a
filled object, so the produced reading yields an *empty* inventory. **Dissolved twice over.** Under
`BOUNDED_CLASS`, `for_each_stage` does not apply; it is replaced by `for_class`, which demands eight
**total replay families on the bounded class** — a class witness in place of a per-stage bundle. And
independently, the `FINITE_ENUMERATION` variant now reads
`exhaustive_ordered_content_addressed_list: **nonempty list**`, which closes the empty-inventory hole
my leg 2 exposed. The repair did not merely add an escape; it also shut the loophole the objection
found.

**LEG 3 — content-addressing.** My objection: the inventory is typed content-addressed while the
receipts are universal statements with no per-stage content to address. **Dissolved.** Every
`BOUNDED_CLASS` component is content-addressed by construction —
`bounded_class_definition: exact content-addressed index/object/map/limit rule`, the universal receipts
as an `exhaustive ordered content-addressed list`, an `ordered_receipt_root_sha256`, and
`explicit_reopening_trigger: exact content-addressed predicate`.

**LEG 4 — both "finite" and "exhaustive" must do work.** My objection: the schema wrote both, and only
the all-stages reading gave both words work. **Answered in the only way a schema-level objection can
be answered — by amending the schema.** Leg 4 was an argument about how to *read* V002; V003 changes
what there is to read. `FINITE_ENUMERATION` keeps both words load-bearing and adds nonemptiness;
`BOUNDED_CLASS` supplies a different satisfaction condition for the case the grammar is infinite. The
variants are exclusive — *exactly one closed variant* — so nothing is left ambiguous.

**No leg is dodged.** I record the reason I am satisfied rather than merely agreeable: the bounded-class
witness is **strictly more demanding in kind** than the thing my ruling rejected. It requires eight
total replay families on the class, a class definition, a root, an identity binding to the outer field,
and a reopening predicate. It is not a weakening that lets the field pass cheaply.

**The escape is a genuine neighbour, not an invention.** Its text —
`"or state a bounded class and explicit reopening trigger"` — sits in V002 itself at byte 20989, inside
JAC-11's coverage/reopening battery: *"enumerate the admitted family with completeness certificate, or
state a bounded class and explicit reopening trigger."* The repair imports V002's own already-ratified
alternative into the neighbouring field rather than authoring a new escape.

## 3. Instantiation, grounds, and guards [PROVABLE]

**Grounds resolve by digest to actual sealed artifacts**, each independently located by me:

```text
089af246cbc0d66e...  -> JOINT_ANCHOR_DECISION_INSTANCE_V003.md      (boundary display)
477847430c1e36a4...  -> STAGE8_AXN_INSTANCE_V003_CROSSCHECK_DARIO_V001.md   (MY 952 ruling)
fff09aba84500f33...  -> STAGE8_AXN_GAUNTLET_RUN2_CODEX2_V001.md     (run-2 rejection)
```

**INSTANTIATION = BOOKED-MATERIAL-ONLY.** The bounded-class components consume the `N>=1` stage ground,
the seven receipts, the ordered root, the identity binding and the reopening predicate — all objects
already booked or typed as content-addressed receivers. No new mathematical object is introduced by the
clause.

**GUARDS.** The anti-flattening guard at V002 `[23337,23541)` rehashes to
`f60997825571eb47...` — **MATCH** — and is present **byte-verbatim** in V003: *"The finite matrix is
stage-wise; the limit conclusion is received only by the separately displayed restriction/limit squares.
No finite certificate is promoted into an unproved completed-carrier identity."* That is precisely the
guard the escape sits nearest, and it is untouched. The V002 suite span is correctly **not** verbatim in
V003 — the inventory clause is the one change, exactly as claimed.

## 4. The supersession form [PROVABLE — LAWFUL]

This is the form that exists to answer the question I declined at 952, and it does so by leaving it with
the principal rather than settling it by construction:

```text
V003_SUPERSESSION_APPROVAL = [PRINCIPAL ENTRY — BLANK]
"the post-adoption repair proposal was not flattened into approval or governing effect"
"No theorem, certificate, state, member, PASS, or governing effect is claimed."
the repair-of-record disclosure is plain: "The governing instrument of an adopted act is being
  proposed for amendment post-adoption. The cause is not preference: both lanes independently
  found finite_stage_inventory unsatisfiable ... and run 2 rejected at that exact G0 receiver."
"Exactly one logical clause changes ... No entry is refilled and no rejected run is rewritten."
```

Governing effect is withheld until approval, downstream digest updates are forbidden pre-approval, the
adopted entries are not altered, and the earlier rejection is not converted into a pass. **I still
decline the governance question itself** — whether amending the governing terms of an adopted act is
lawful post-adoption is the principal's or registrar's to answer. What I can and do verify is that the
form does not answer it silently.

## 5. Carriage and advocacy [PROVABLE]

```text
diff -d -U0 replay against V002 : 24 hunks  =  24 declared   MATCH
advocacy, 12-term independent scan : 5 occurrences, 0 advocacy
```

The five term-hits are prohibitions or explicit anti-advocacy: *"no ratio, preference, or downstream
predicate may select the fiber"*; the reverse-A2 clause's *"already encodes a preferred measure"*; *"The
cause is not preference"*; and two instances of the instrument recommending **neither** disposition,
including *"The instrument recommends neither disposition. The choice and every principal entry belong
to the"* principal. **ADVOCACY = 5 hits, 0 advocacy.**

## 6. The one observation returned [PROVABLE — non-blocking]

**Two pure-deletion hunks remove a V002-era attestation block, and two phrases leave the instrument
entirely.** The deleted lines are V002's *carriage controls from V001*:

```text
-Carriage controls, checked as exact V001 substrings after writing:
-DB_STRENGTHENING = carried unchanged: "already entered" pairing/trace; no free reference density
-SYM_STRENGTHENING = carried unchanged: finite/content-addressed action
-LIMIT_SQUARE_ADDITION = carried unchanged: every finite/cylindrical restriction and limit square commutes
-OVER_CONSTRAINT_FINDING = carried: none found; {BI} remains a lawful one-tag entry
```

I tested whether the *strengthenings themselves* went with the attestations, since a deletion inside a
governing-instrument supersession is exactly where a weakening could hide. They did not:

```text
"already entered"            V002 2 -> V003 1     substantive occurrence survives
"no free reference density"  V002 3 -> V003 2     survives
"restriction and limit square" V002 2 -> V003 1   survives
BI / DB / SYM variant tokens   9/10/10 -> 9/11/11  present, and slightly expanded
```

Each count falls by exactly one — the copy that lived in the deleted attestation block — and the
operative machinery survives, with the `anchor_certificate` field still demanding *exactly one closed
BI / DB / SYM variant* and the bounded-class form demanding *exactly one total closed BI / DB / SYM
replay family*. **No clause, scan, obligation or gauntlet stage is weakened.**

What does vanish from the instrument entirely is two *phrases*: `finite/content-addressed action` and
`one-tag` (from `{BI} remains a lawful one-tag entry`). The lawfulness of a one-tag `{BI}` entry remains
**structurally** true — the schema permits exactly one variant — so nothing operative is lost. But a
reader diffing V002 against V003 finds `SYM_STRENGTHENING` and `OVER_CONSTRAINT_FINDING` absent with no
replacement statement in V003's own carriage block.

**This does not block.** It is bookkeeping from a previous revision, superseded by V003's own carriage
accounting, and it corrupts no governing act. I return it so the registrar can decide whether the two
attestations should be restated in V003's carriage block rather than simply retired.

## 7. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  my 952 four-leg ruling as the standard the repair must answer;
  the V002 suite bytes, the anti-flattening guard, and the JAC-11 escape at its byte;
  the three grounds at their digests.

SUBSTITUTED:
  NOTHING. I approved no supersession, entered no field, and chose no variant.
  I adopted nothing and registered nothing.

DECLINED DELIBERATELY:
  the governance question underneath item 3 -- whether amending the governing terms of an adopted
  act is lawful post-adoption. I verified that the FORM leaves it with the principal; I did not
  answer it, at 952 or here.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

## 8. Flattening, custody, byte audit

- **S01-S37 FLATTENING CHECK:** walked. A repair was not identified with a dodge — each of my four legs
  was tested for dissolution, not for adjacency (§2). An escape was not identified with an invention —
  it is V002's own JAC-11 text at its byte. A deleted attestation was not identified with a deleted
  clause (§6), and I tested the strengthenings rather than assuming. A verified form was not identified
  with an answered governance question (§4).
- **F_PLDEC:** digests, span arithmetic and schema reading only. No physical quantity evaluated.
- **M-2 / four modes:** exact-name and byte-span checks covered `finite_stage_inventory`,
  `for_each_stage`, `for_class`, `outer_receipts_identity`, the escape text, the guard, and every
  strengthening phrase in the deleted block.
- **BLIND:** held. No rank read, no ratio formed, no fiber compared or opened.
- **PE-1..PE-14:** pointer-only, zero verdict weight.
- **BR-1:** my 952 defined what had to be answered and certified nothing; the subject's claims located
  what to test and discharged no test.
- **NUMERAL GREP:** run over every count-bearing sentence in this report — the four legs, the 24 hunks,
  the 5 advocacy hits, the 2 deletions, and each V002→V003 token count — every numeral re-derived from
  a command output rather than carried.
- **CHAIN:** no anchor act, member binding, fixed-point execution, end test, gauntlet run, numerical
  evaluation, or comparison with a measured constant was invoked.

```text
CLOSURE_BEGIN_BYTE = 0
CLOSURE_END_BYTE = 2576
PREDECLARATION_OUTPUT_SCAN = 0 hits
LEGS_ANSWERED = 4/4 ; LEGS_DODGED = 0
GROUNDS_RESOLVED = 3/3 ; GUARD = byte-verbatim ; CARRIAGE = 24/24 ; ADVOCACY = 0
DEFECTS_RETURNED = 0 ; OBSERVATIONS_RETURNED = 1
```

Self verb audit: "answered" and "dissolved" are used of my four legs, each tested individually against
the repaired clause with the mechanism shown. "Verified" applies to the grounds, the guard, the
carriage and the advocacy count, each recomputed. "Declined" names the governance question I refuse at
958 as I refused it at 952. I approved no supersession and chose no variant.
`VERB_AUDIT_SELF = CLEAN`.

## 9. Final lines

```text
CLOSURE = declared-first (byte position 0, closure end 2576; scan 0 hits)
CLAUSE = ANSWERS-ALL-FOUR-LEGS. Leg 1 (category substitution) dissolves: BOUNDED_CLASS demands seven distinct components and adds outer_receipts_identity forcing the inner copy to BE the outer field, so the separate key survives and double-counting is barred — the opposite of a substitution. Leg 2 dissolves TWICE: for_each_stage is replaced by for_class demanding eight TOTAL REPLAY FAMILIES on the class, and independently FINITE_ENUMERATION is now a NONEMPTY list, which shuts the empty-inventory hole my leg 2 exposed. Leg 3 dissolves: every bounded-class component is content-addressed by construction. Leg 4 is answered the only way a schema-level objection can be — by AMENDING the schema, since leg 4 was an argument about how to read V002 and V003 changes what there is to read; both variants are closed and exclusive. NO LEG DODGED, and I record why I am satisfied rather than merely agreeable: the bounded-class witness is STRICTLY MORE DEMANDING IN KIND than what my ruling rejected, so this is not a weakening that lets the field pass cheaply. The escape is a genuine neighbour, not an invention — its text sits in V002 itself at byte 20989 inside JAC-11's coverage/reopening battery
INSTANTIATION = BOOKED-MATERIAL-ONLY (the N>=1 stage ground, the seven receipts, the ordered root, the identity binding and the reopening predicate; no new mathematical object enters by the clause). All three grounds resolved BY DIGEST to actual sealed artifacts, including my own 952 at 477847430c1e36a4...
GUARDS = VERBATIM+UNWEAKENED. The anti-flattening guard rehashes to f60997825571eb47... MATCH and is present BYTE-VERBATIM in V003 — and it is precisely the guard the escape sits nearest. The V002 suite span is correctly NOT verbatim in V003, since the inventory clause is the one change
FORM = LAWFUL (blank approval; effect withheld). V003_SUPERSESSION_APPROVAL = [PRINCIPAL ENTRY — BLANK]; governing effect withheld until approval; downstream digest updates forbidden pre-approval; adopted entries unaltered and the earlier rejection not converted into a pass; the repair-of-record disclosure plain and grounded in two independent lane findings plus an actual G0 rejection. I STILL DECLINE THE GOVERNANCE QUESTION ITSELF, as at 952 — what I verify is that the form does not answer it silently
CARRIAGE = 24-CONFIRMED (24 hunks replayed under the declared convention = 24 declared)
ADVOCACY = 5 hits, 0 advocacy (all five are prohibitions or explicit anti-advocacy, including two instances of the instrument recommending NEITHER disposition)
VERDICT = READY-FOR-THE-PRINCIPAL. ONE NON-BLOCKING OBSERVATION: the two pure-deletion hunks remove V002's carriage-control attestations from V001, and two phrases leave the instrument entirely — "finite/content-addressed action" and "one-tag". I tested whether the STRENGTHENINGS THEMSELVES went with the attestations, since a deletion inside a governing-instrument supersession is exactly where a weakening could hide: they did not. Each token count falls by exactly one — the copy in the deleted block — the substantive occurrences survive, and the BI/DB/SYM machinery is present and slightly expanded. No clause, scan, obligation or gauntlet stage is weakened. What is lost is two attestation phrases with no replacement statement in V003's own carriage block; that is superseded bookkeeping and corrupts no governing act, so it does not block, but I return it for the registrar to decide whether to restate rather than retire them
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
