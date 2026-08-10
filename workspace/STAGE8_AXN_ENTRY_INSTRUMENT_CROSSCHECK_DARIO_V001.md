# STAGE 8 — AXN — CROSS-CHECK OF THE ENTRY-COMPLETION INSTRUMENT (929)
## DARIO LANE — RELAY 932 — `[PLAN:AXN-BUILD-D31]`

## 0. Preflight

Relay 932 verified before reading at
`b0c6276d2b7a6439ef68a6dfd45a448556fba439e58bbdfaddaf053fdc439651`. Lane guard read DARIO; the
pickup ACK was written before content access. `PROGRAM_STATE_BRIEF_V005.md` verified and read before
task work at `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`. The subject verified
against its own sidecar at the digest the relay states. The output name was clear.

---

## 1. Law-9b closure — declared first

```text
C_932 = {
 1  RELAY_PASTE_932_INSTRUMENT_CROSSCHECK_DARIO_V001.md
      b0c6276d2b7a6439ef68a6dfd45a448556fba439e58bbdfaddaf053fdc439651
 2  supervision/PROGRAM_STATE_BRIEF_V005.md
      e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c
 3  STAGE8_AXN_ENTRY_DECISION_INSTRUMENT_CODEX2_V001.md                 [SUBJECT — 929]
      c650c578c8625ffba7e1e33713e65a10623adb41444a5bb95f76d76c4ced5046
 4  STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V002.md                         [the schemas the demands quote]
      58b966ed371b23b29b9e3ceed280eb30c804484becb2b17ca6ea465668e951bc
 5  JOINT_ANCHOR_DECISION_OF_RECORD_V001.md                             [the entered enum — §5]
      f0179d43b4b2ed89f4cfb9adc1daa8c7cc0c9c5f038e3bbe7332727fdddaaa8f
 6  JOINT_ANCHOR_CERTIFICATE_MANIFEST_V001.md                           [the entered enum — §5]
      589c12f7cb76b5f4a2ba895d5942061ec3d801d6983f656304b172bfde964b27
 7  JOINT_ANCHOR_DECISION_INSTANCE_V002.md                              [my 925 — the stopped fields]
      72191e0115d6f36d2327236e7a6d16e21f953422ba3fb2188b75e3db009cea99
 8  STAGE8_AXN_ENTRY_CANDIDATE_SURVEY_DARIO_V001.md                     [my 927 — the reference; §4]
      4440af4f8d4a75c7e4b026d4fd901e4e290676f928275897bb55ce803b4c03db
 9  STAGE8_AXN_CARRIER_CONSTRUCTIONS_DARIO_V001.md                      [my 928 — the two new fields]
      3c59ba330e84d2062600aa3021dd61e1cca1a31b3967263b7ca4c211880bf0b0
10  STAGE8_AXN_RECORD_LABELLING_DARIO_V001.md                           [my 930 — §8]
      32ad8a9fe8524742b09e6003a015e6c5fb4560a02e054d5c46bfd118b2c25402
}
```

**Name probe.** `STAGE8_AXN_ENTRY_INSTRUMENT_CROSSCHECK_DARIO_V001.md` and its sidecar: clear at
pickup.

---

## 2. The standard, stated before the findings

Both halves of what I set at 918 and 921 bind me here:

- **READY only if actually ready.** At 918 I returned a complete-looking instrument on four items.
- **Gaps fixed is ready unless something else is wrong.** At 921 I said withholding READY to look
  careful is its own failure. I have not manufactured a finding to look thorough.

**The asymmetry that applies:** this instrument runs a *principal entry round*. Under-constraint lets
authored content enter as a clerical act; over-constraint blocks a lawful entry. §4 therefore runs
**both** directions and reports the second even though it came back empty.

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
JOINT_ANCHOR_DERIVED = false
```

All items **CLAIMED**. I adopt nothing, change nothing, fill no field, and take no position on any
route. **BUILDER-NEVER-VERIFIES cuts clean:** the subject is the opposite lane's. **BLIND held**, and
§7 is itself a blindness audit run by checking route endpoints rather than by walking a route.

**BR-1, in an unusual shape.** The relay names my 927 as the reference for option completeness. I
compared the grammar to the **pinned objects** my survey listed, re-checked here, not to my
conclusions about them — and §4.2 records where the instrument found a lawful option **I missed**.

---

## 3. Receivers — 8/8 confirmed

All twenty-three cited spans were recomputed from the sealed bytes. **23/23 MATCH**, including all
eight receiver demands, the reverse-A2 receiver, both pairing seeds, the two history-control grounds,
the tensor presentation and sibling-embedding spans, all three `i_src` declarations, all four blind
pointer extents, and the live-register `Q-834` span.

**Do the quoted demands match the instance's actual stopped fields?** My 925 stopped nineteen. The
instrument covers eight and its scope says so: *"the seven genuine decisions plus the two-site
`P_ch_sha256` pointer choice."* Against my 927 classification — 7 genuine · 8 construction-needed · 4
pointer-entry — the split is exact:

| 927 class | count | in this instrument |
|---|---|---|
| GENUINE-DECISION | 7 | **all 7** |
| POINTER-ENTRY with two sites (`P_ch`) | 1 | **yes** |
| POINTER-ENTRY with one site (`i_R`, `i_B`, `P_0`) | 3 | correctly **excluded** — a single-site pointer needs no decision round |
| CONSTRUCTION-NEEDED | 8 | correctly **excluded** — those need a lane, not the principal |

```text
RECEIVERS = 8/8 CONFIRMED
```

---

## 4. Option spaces — both directions

### 4.1 Missing lawful options: none — and one the instrument found that I did not

Checked against the pinned objects my 927 located:

| receiver | my 927's pinned candidates | instrument's classes | verdict |
|---|---|---|---|
| pairing | two source-sector seeds (HS, carrier-tracial) | `P-HS`, `P-CT`, `P-NEW`, `P-BLANK` | complete, **plus** the non-extension class |
| `i_src` | three wrong-codomain declarations | `S-OBJ0`, `S-JP0`, `S-RANK1`, **`S-TENSOR`**, `S-NEW`, `S-BLANK` | **see §4.2** |
| `I_A` | one status occurrence, not a declaration | `IA-STATUS`, `IA-NEW`, `IA-BLANK` | complete, **and strengthened** — §4.3 |
| `P_ch` | two sites | `PCH-STATUS`, `PCH-TUPLE`, `PCH-BLANK` | complete |
| `fiber_label` | symbolic only | `F-DOR013`, `F-NEW`, `F-BLANK` | complete |
| `equivalence_scope` | none of record | `E-ID`, `E-CLASS`, `E-BLANK` | complete |
| `physical_price` | none by type | full-concatenation or blank | complete |
| `entered_pairing_sha256` | none | four options tracking the pairing | complete |

### 4.2 A correction to me

**`S-TENSOR` is a lawful option my 927 survey did not enumerate.** My survey observed in passing that
the state-algebra map derives `i_R` and `i_B` "though the same presentation would give
`i_src(a) := a ⊗ 1_R_inf ⊗ 1_B`" — and then listed only the three wrong-codomain declarations as
candidates. The instrument turns that observation into a route: after the principal binds the source
factor of the entered `A_C0`, author and seal the canonical tensor injection from member 09's sealed
presentation, with its domain/codomain proof. **That is a genuine option class I named and failed to
count.** The instrument's option space is wider than my survey's, and correctly so.

### 4.3 Unlawful options included: none

The direction I would have expected to find something, and did not:

- A **bare pointer to a source seed** is expressly excluded as a filled option — *"it has the wrong
  carrier"* — with the cross-sector law named as load-bearing content rather than metadata.
- A **raw status-span digest** for `I_A` without the name-binding act is expressly excluded —
  *"would flatten an occurrence into an object declaration and is therefore outside the lawful
  options."* That exclusion is a strengthening over my 927, which recorded the addressability without
  requiring the binding act.
- `H-DIRAC` carries a stated faithfulness condition rather than being offered flat: a direct Dirac
  tensor trace on nontrivial `C(Y)` is not faithful, so the branch is lawful only through a separately
  sealed faithful construction.
- **`P-BLANK`, `F-BLANK`, `E-BLANK`, `S-BLANK`, `IA-BLANK`, `PCH-BLANK`** are each labelled as leaving
  G0 incomplete, so no blank is dressed as a completion.

```text
OPTION_SPACES = COMPLETE, both directions; no unlawful option included
```

---

## 5. Enum propagation — the finding the relay asked me to press

### 5.1 The rule, as the instrument states it

> *"Thus `NEITHER_EQUIVALENCE_PROVED` is not a default: it is barred on `H-HAAR` and `H-DIRAC`,
> required on a certified `H-OTHER`, and **unwarranted when the pairing or certificate is missing**."*

The forcing claims check out at their grounds: `H-HAAR` and `H-DIRAC` each force reclassification
through an exact equivalence certificate, `H-OTHER` warrants `NEITHER` through an exact
nonclassification certificate, and no enum is reachable without a pairing **and** a certificate.

### 5.2 What that rule does to the principal's existing disclosure

`NEITHER_EQUIVALENCE_PROVED` is **already entered and confirmed**. Member 5 carries it as
*"pairing disclosure = NEITHER_EQUIVALENCE_PROVED"*, and member 6 lists it under *"ENTRIES OF RECORD
(principal-confirmed in session, verbatim 'Confirmed')."*

And no pairing and no certificate exist — the instrument's own §2 table says the joint pairing's
record-native value space is **EMPTY** and that for `entered_pairing_sha256` *"no joint pairing object
exists to hash."*

**So by the instrument's own propagation rule, the entered disclosure is presently unwarranted — and
the instrument nowhere says so.** Its only adjacent sentence covers a *change*: *"If the pairing
changes, all three downstream objects and the enum must be regenerated or revalidated."* That is not
the current state; the current state is that the enum never had its warrant.

**The sharper half.** If the round-2 entry selects `H-HAAR` or `H-DIRAC`, the instrument's rule
**forces** the enum to a different value. Member 5 is a sealed principal act carrying
`post_freeze_mutation: FORBIDDEN`. So round 2 can put two principal acts in contradiction, with the
earlier one unmutatable, and **the instrument supplies no disposition for that case** — no
supersession clause, no provisional typing of the round-1 enum, no instruction to re-enter it.

```text
ENUM_PROPAGATION = CORRECTED
  The forcing rules themselves are sound and their grounds verify.
  What is missing is their consequence for the already-entered enum: it is presently
  unwarranted, and two of the three branches would contradict it while it cannot be mutated.
  One clause fixes this — disposition the round-1 enum — and it belongs before the round.
```

---

## 6. Prices and cascade

**Prices.** Each filled route carries a per-option draft, and each draft names the pairing it prices:
`P-HS` names the Hilbert–Schmidt seed and its cross-sector extension; `P-CT` names the carrier-tracial
seed and its conversion; `P-NEW` names the complete independent pairing. Each closes with *"No joint
pairing is called source-derived"* or its equivalent, which is the reverse-A2 guard applied. The
history branches append their own price, the fiber, embedding, and equivalence-scope drafts are
appended, and **a partial price is expressly not a filled option**.

```text
PRICES = CONFIRMED
```

**Cascade.** The leak the relay names — a source-seed digest standing where the entered joint digest
belongs — is guarded at three separate places: the bare-pointer exclusion (*"wrong carrier"*), the
propagation chain (*"No source-seed digest may substitute for `entered_pairing_sha256`"*), and the
§4 option text, which reads *digest of the exact selected joint object*, never of the seed. The seeds
are pinned separately as **grounds**, at their own spans, so a reader can tell ground from entry.

```text
CASCADE = LEAK-PROOF
```

---

## 7. Blind routes — audited by endpoints, not by walking one

Testing a blind route by taking it would breach the thing under test. I checked the **entered extents**
instead, for rank-shaped content:

```text
IA-STATUS   extent [781,794)      rank-shaped tokens: NONE
PCH-STATUS  extent [884,898)      rank-shaped tokens: NONE
PCH-TUPLE   context [23013,23148) rank-shaped tokens: NONE
PCH-TUPLE   member  [23081,23085) rank-shaped tokens: NONE
```

All four extents a principal would seal are clean of `r_0`, `r_ch`, `rank`, and `p_[A]`. The routes
are pointer/digest only: `FiberLabelPointer.v001` validates by digest and pointer equality; `IA-STATUS`
seals a name-binding record of source digest, span, and span digest; the `P_ch` routes seal source and
span extents. **Every blind field can be entered from opaque pointer records without opening anything
rank-shaped.**

```text
BLIND_ROUTES = CONFIRMED (all four entered extents verified clean)
```

---

## 8. Law-9b tables, advocacy, and the two new fields

**Law-9b.** The §2 authority column cites my 927's sections, which in turn pin the sealed objects by
digest and span; the instrument pins my 927 by digest. That is a valid two-step chain, and I
re-verified the underlying objects rather than the section numbers. Each *EMPTY* claim traces to a
pinned object.

```text
LAW9B = CONFIRMED
```

**Advocacy.** An independent scan of the whole document over `recommend`, `should`, `advisable`,
`urge`, `prefer`, `cheaper`, `simplest`, `natural choice`, `best` returns **three** hits, none
advocacy: one is *"a preferred history measure"* quoting the reverse-A2 clause, and two are the
instrument's own anti-advocacy sentences. Every filled pairing family receives the same three history
branches and the same certification rule.

**The two new decision-shaped fields.** A scan returns **zero** occurrences of
`stage_index_and_limit_rule`, `joint_superselection_map`, or `E_joint`, and **zero** references to my
930 labelling report. The instrument's scope excludes them by design.

**Are they presentable alongside, or is a supplement needed?** They are **coupled to a field the
instrument does cover**, and the coupling is exact. Member 4 defines

```text
Delta_0^joint := { Delta : Tr_joint(Delta) = 0 and E_joint(Delta) = Delta }
```

and the anchor family's admission condition is `ker(Phi_joint restricted to Delta_0^joint) = {0}`,
whose warrant is the faithfulness certificate every filled pairing route requires. **`Delta_0^joint`
is defined by the trace and the superselection map jointly.** This instrument sets `Tr_joint` — the
pairing — and does not reach `E_joint`. So a pairing entered under it yields a faithfulness condition
stated on a space that is not yet defined, and the certificate the route demands cannot be written.

```text
NEW_FIELDS = SUPPLEMENT-NEEDED
  Not because the fields are large, but because Delta_0^joint needs BOTH the entered trace and
  E_joint, and the pairing routes' faithfulness certificates quantify over it. The superselection
  field is on the critical path of a field this instrument already covers.
  Reported as a finding. I changed nothing and touched neither field.
```

---

## 9. FREEDOMS-CONSUMED (law 2a)

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN ; JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the subject's eight receivers, option classes, prices, and propagation rules as CLAIMED;
  member 4's schemas and the Delta_0^joint definition; members 5 and 6's entered enum;
  my 927's pinned objects as the comparison set, re-checked rather than cited;
  my 928 and 930 as the source of the two new fields' content, used only in section 8.

CONDITIONED-ON:
  section 5's consequence on members 5 and 6 carrying the enum as a confirmed entry rather
  than a provisional one, which is how both artifacts label it;
  section 8's call on Delta_0^joint's definition requiring both factors, which is member 4's
  own formula.

SUBSTITUTED:
  NOTHING. No route selected, ranked, or recommended; no field filled; no clause written into
  the subject; no disposition proposed for the round-1 enum beyond naming that one is needed;
  neither new field touched.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

---

## 10. Flattening check, verb audit, byte audit

**FLATTENING CHECK — S01–S37 walked, clean.** A matching span digest was not identified with a
correct claim about its content. A sound forcing rule was not identified with a fully propagated one —
§5 separates the rule from its unstated consequence. An option my survey missed was reported as a
correction to me, not absorbed silently. A blank route was not identified with a completion. A
two-step authority chain was not identified with a direct one, and I re-verified the underlying
objects. An endpoint audit was not identified with walking a blind route. A coupling was not
identified with a merger: §8 says the superselection field is on the pairing's critical path, not that
the two fields are one.

**BUILDER-B INDEPENDENCE:** the subject is the opposite lane's. Members 7–10 are mine; 8 is the
comparison set and was used through its pinned objects, and 9–10 supply only §8's content.

**SELF VERB AUDIT.** "Confirmed" is used for receivers, prices, cascade, blind routes, law-9b and the
option spaces, each with its check displayed. "Corrected" is used once, for enum propagation, and the
correction is to the rule's *consequence*, not to the rule. "A correction to me" is used in those
words at §4.2. "Supplement-needed" is a reported finding and no supplement was drafted. No route,
disposition, or verdict on the anchor is recommended. `VERB_AUDIT_SELF = CLEAN`.

**BYTE-POSITION SELF-AUDIT.** §1's heading begins at byte **572**, its closure fence opens at byte
**621**, and the exact member list ends at byte **2236**. A scan of bytes `[0,621)` over `no `,
`not `, `none`, `never`, `absent`, `missing`, `without`, `lack`, `fail`, `gap`, ` open`,
`unresolved`, `underived`, `false`, `cannot`, `zero`, `stop`, `block`, `wrong`, `refus`, `unswept`,
`unsealed` returns **zero hits**.

---

## 11. Final lines

```text
CLOSURE = declared-first (sec-1 heading 572, closure fence 621, members end 2236; pre-closure scan over 22 forms = 0 hits)
RECEIVERS = 8/8 CONFIRMED. All 23 cited spans recomputed and MATCHED. The eight quoted demands map exactly onto my 927 classification — all 7 GENUINE-DECISIONS plus the one two-site pointer — with the 3 single-site pointers and the 8 construction-needed fields correctly excluded, since neither class needs a principal decision round.
OPTION_SPACES = COMPLETE, tested in BOTH directions. No lawful option is missing — and the instrument found one I did not: S-TENSOR, the canonical tensor injection i_src(a) = a (x) 1_R_inf (x) 1_B from the sealed presentation, which my 927 mentioned in passing and FAILED TO COUNT AS A ROUTE. That is a correction to me and the instrument's space is wider than my survey's. No unlawful option is included, and the exclusions are the right ones: a bare source-seed pointer is barred as wrong-carrier, a raw status-span digest for I_A is barred as flattening an occurrence into a declaration (a strengthening over my 927), H-DIRAC carries its faithfulness condition rather than being offered flat, and every BLANK route is labelled as leaving G0 incomplete.
PRICES = CONFIRMED. Every filled route is priced, each price names the pairing it prices, each closes with the reverse-A2 guard applied ("no joint pairing is called source-derived"), and a partial price is expressly not a filled option.
ENUM_PROPAGATION = CORRECTED. The forcing rules are SOUND and their grounds verify: HAAR and DIRAC each forced by an exact equivalence certificate, NEITHER warranted only on a certified H-OTHER, no enum without pairing AND certificate. WHAT IS MISSING IS THE CONSEQUENCE FOR THE ENUM ALREADY ENTERED. NEITHER_EQUIVALENCE_PROVED is a CONFIRMED entry of record in both the decision and the manifest, while the instrument's own table says the joint pairing space is EMPTY and no joint pairing object exists to hash — so by its own rule that entry is PRESENTLY UNWARRANTED, and the instrument nowhere says so; its only adjacent sentence covers a pairing that CHANGES, not one that never existed. SHARPER: if round 2 selects H-HAAR or H-DIRAC the rule FORCES a different enum, while the round-1 decision carries post_freeze_mutation = FORBIDDEN — so two principal acts could contradict with the earlier one unmutatable, and NO DISPOSITION IS SUPPLIED. One clause fixes it and it belongs before the round.
CASCADE = LEAK-PROOF. The source-seed substitution is guarded at three separate places — the wrong-carrier exclusion, the explicit propagation prohibition, and the option text reading "exact selected joint object" — with the seeds pinned separately as grounds so ground and entry stay distinguishable.
BLIND_ROUTES = CONFIRMED. Audited by ENDPOINTS rather than by walking a route, since taking one would breach the thing under test. All four extents a principal would seal — IA-STATUS [781,794), PCH-STATUS [884,898), PCH-TUPLE context [23013,23148) and member token [23081,23085) — verified CLEAN of r_0, r_ch, rank and p_[A]. Every blind field is enterable from opaque pointer records without opening anything rank-shaped.
LAW9B = CONFIRMED. The authority column runs a two-step chain — instrument to my 927 (digest-pinned) to the sealed objects (digest and span pinned) — which is valid, and I re-verified the underlying objects rather than the section numbers. ADVOCACY: independently scanned over nine terms across the whole document; three hits, NONE advocacy (one quoting the reverse-A2 clause's "preferred history measure", two the instrument's own anti-advocacy sentences).
NEW_FIELDS = SUPPLEMENT-NEEDED. The instrument contains zero occurrences of stage_index_and_limit_rule, joint_superselection_map, or E_joint, and no reference to my 930 labelling facts. They are not merely adjacent: Delta_0^joint := {Delta : Tr_joint(Delta)=0 and E_joint(Delta)=Delta} is defined by the trace AND the superselection map JOINTLY, and the anchor's admission condition ker(Phi_joint|Delta_0^joint) = {0} is exactly what every filled pairing route's faithfulness certificate must warrant. This instrument sets Tr_joint and does not reach E_joint, so a pairing entered under it has its faithfulness condition stated on a space not yet defined. The superselection field is ON THE CRITICAL PATH of a field the instrument already covers. Reported as a finding; I changed nothing and touched neither field.
VERDICT = NOT-READY, on two items, both specific and both fixable by a clause: (1) disposition the already-entered NEITHER_EQUIVALENCE_PROVED — presently unwarranted by the instrument's own rule, and contradicted outright by two of three round-2 branches while frozen against mutation; (2) supply or sequence the superselection field, since Delta_0^joint needs it before any pairing's faithfulness certificate can be written. EVERYTHING ELSE IS SOUND AND I SAY SO PROMINENTLY: 23/23 spans, receivers 8/8, option spaces complete in both directions with one route better than my own survey's, prices confirmed with the reverse-A2 guard applied per option, cascade leak-proof at three guards, all four blind extents clean, law-9b chains valid, advocacy zero. This is a NOT-READY on two items, not a criticism of the document.
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
```
