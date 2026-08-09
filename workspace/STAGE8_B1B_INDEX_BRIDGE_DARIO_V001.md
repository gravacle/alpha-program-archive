# STAGE 8 / 7A / [PLAN:B1b-2] — THE INDEX BRIDGE: IT IS THE COFRAME SQUARE, AND IT WAS ALREADY BUILT

Lane: DARIO (Builder B, independent verifier). Relay 798.
State brief pinned: `PROGRAM_STATE_BRIEF_V005.md` = `e26f0d16055f3e83…` — digest matches, seal OK,
read before task work. Drift check: V005 current.
Governing: my own **792 / Q-701** — B1b's obstacle is the exhaustion-vs-refinement index mismatch.
Law 8 applied to every seal probe. All headline items **CLAIMED**.

## Lead determination — CLAIMED

**Three threads the record has been carrying as separate blockers are one object, and 795 built
its candidate set two relays ago.**

My 792 wrote that "no sealed object carries one index to the other." **That was too weak a reading
of my own IDX.** IDX §3.3 does not say the bridge is missing — it names it:

> *"the exhaustion-vs-refinement gap: the sealed density instance remains exhaustion-indexed. LL1
> supplies a refinement index; it does NOT transport the sealed instance onto it, **because that
> transport is the measure functoriality §2 finds unproven**."*

And IDX §2.3 says exactly what that functoriality needs:

> *"Transporting the measure along it requires that `V_cell · Σ_{μ<ν} F_{μν}²` (the parent's
> contribution) be recovered by summing the sub-cells' contributions — **which requires a rule
> assigning `F` on each new sub-face.**"*

```text
   THE INDEX BRIDGE  =  THE MEASURE FUNCTORIALITY  =  A RULE ASSIGNING F ON EACH NEW SUB-FACE
                                                   =  THE F'/F COFRAME SQUARE  (795)
```

**And 795 already tested exactly the condition IDX §2.3 states.** The "parent's contribution
recovered by summing the sub-cells' contributions" is the quadratic-preservation test I ran:

```text
(a1) form-inheritance        children/parent = 1.813, 1.825, 3.041, 4.014, 1.682, 4.691  ELIMINATED
(a2) component-inheritance   children/parent = 1.000000 every trial                      RECOVERS
(b2) orientation-weighted    children/parent = 1.000000 every trial                      RECOVERS
```

**So the bridge is not absent. It exists, it is exhibited by either surviving candidate, and it is
NOT UNIQUE** — 795's residual is 843 dimensions.

```text
BRIDGE = FREE (two complete displays, inherited from 795; neither adopted).
```

**A correction I nearly made in the other direction, caught before it entered.** The hunt surfaced
`R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT` with the verdict
`INHERITED_REFINEMENT_NATURALITY_FORCES_UNIFORM_MEASURE`, and I was one step from reporting that it
discharges IDX §2. **It does not.** R33 forces the measure's per-cell **value** on a child; IDX §2
needs the **F-assignment rule**. Different objects. Reading a verdict *name* as the proposition it
resembles is the name-match trap in its purest form, and I nearly ran it on myself.

---

## 0. Preflight

```text
OUTPUT NAME  probed recursively: artifact and sidecar ABSENT.
LAW 8 applied to every seal probe below (all three modes).
IDX   STAGE8_7A_RA27_2_INDEX_BUILT_DARIO_V001.md    66f078baf5ff980f…  .md.seal OK
795   STAGE8_B1A_COFRAME_HALF_DARIO_V001.md         590b3979d5a0fadf…  .md.seal OK
792   STAGE8_B1B_SUPPORT_QUESTION_DARIO_V001.md     585d309dcf4d362a…  .md.seal OK
788   STAGE8_B1A_REFINEMENT_CARRIER_DARIO_V001.md   97f073c101d8cf4a…  .md.seal OK
753   STAGE8_7A_SIMPLICIAL_COFRAME_DARIO_V001.md    d6f490b80e8d8775…  .md.seal OK
R33   R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md    e60aec3c44cfc5f1…
      NO adjacent sidecar in EITHER spelling — sealed by MODE 3, packet-manifest membership:
      STAGE7_PACKET_MANIFEST_V001.sha256 -> "./R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md: OK"
R33G  R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md  e4cfaef14309b3ac…  manifest OK
CDL   CAUSAL_DIRECT_LIMIT_RECORD_PRINCIPLE_V001.md   packet member, manifest OK
CIS   CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md     b0c636f3b2b00f06…  doubly sealed

GATES: alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false.
No member binding; no fixed-point execution; no end test; no numeric evaluation of physical
quantities; no comparison to measured constants.  NO COMPLEX SELECTED.  NO SMOOTH IMPORT (S26).
NO EM IDENTIFICATION (S08).  No common cell formed; no junction map evaluated.
PE-1..PE-7 pointer-known, zero weight, not opened, not consulted.
```

---

## 1. AS1 — PATH (a): THE HUNT

### 1.1 Searched space and probes

```text
GLOB: ./workspace/**/*.{md,json} + ./supervision/**/*.{md,json}, evaluator_build_A/ and checks/
      EXCLUDED BY LAW; memory-bank never searched.
TARGETS per the relay: the CDL family; IDX 3.3's own context; the tau-density stock; the
      conservation law's four-volume carrier; 755's exhaustion spans.
PROBES, token + content-synonym: exhaustion/refinement compatibility; cofinal embedding; functor
      between index categories; two-index diagram; "growing volume" vs "subdivision"; measure
      functoriality; pullback naturality; refinement bridge; density transport.
```

### 1.2 Survivors — meaning-probed, not counted

| # | object | what it DISPLAYS | bearing |
|---|---|---|---|
| **S1** | **IDX §3.3** (mine, sealed) | names the bridge outright: the transport **is** the measure functoriality §2 finds unproven | **decisive — the bridge is a named proposition, not a missing object** |
| **S2** | **IDX §2.3** (mine, sealed) | states what that functoriality requires: *"a rule assigning `F` on each new sub-face"*, and that the change-of-coframe law *"says nothing about this"* | **decisive — identifies the bridge with the coframe square** |
| **S3** | `4d` `430f0971…[21855,21975)`, quoted in IDX §2.2 | *"This proves the local density transformation given the coframe. It does not derive the coframe or the refinement bridge."* | confirms the gap is the bridge, not the coframe law |
| **S4** | `BATT` `14ddfc15…[4496,4636)`, quoted in IDX §2.3 | *"T11's gap is FUNCTORIALITY OF A MEASURE — does the response-map pullback commute with refinement, and is the boundary term subextensive?"* | a **non-Dario** lane names the same gap |
| **S5** | **R33** (packet-sealed) | `INHERITED_REFINEMENT_NATURALITY_FORCES_UNIFORM_MEASURE`; its binding item 4 is *"response must commute with common refinement"* | **NEAR-MISS — see §1.3** |
| **S6** | CDL family (792's find) | the exhaustion-side directed architecture; cofinality-invariance as a falsifier | the exhaustion index's home; unchanged |

### 1.3 The near-miss, disclosed rather than banked

**S5 is not a survivor for the bridge.** R33's verdict forces the measure's **per-cell value** on a
child (*"a subregion promoted to an elementary cell must be evaluated by that child's intrinsic
cell measure"*). IDX §2 needs the **rule assigning `F`**. A measure value is not an `F`-assignment.
**Reading `INHERITED_REFINEMENT_NATURALITY…` as "refinement naturality is proven" would be the
name-match trap** — the same failure the Q-69 census exists to prevent, run on a verdict token
instead of an object name.

*Its real bearing is different and worth keeping:* R33's item 4 is **D11 conjunct 1**, which 788
established is exact and untoleranced. So the record already uses conjunct 1 productively — to
force the measure — which is evidence that conjunct 1 is a working constraint, not an inert clause.

```text
HUNT = 6 hits, 5 survivors (S1, S2, S3, S4, S6); 1 near-miss disclosed (S5).
   No object relating the two index CATEGORIES as such was found.  What was found is better:
   the bridge is a NAMED PROPOSITION whose content is the coframe square.
```

---

## 2. AS2 — PATH (b): THE POSING

### 2.1 The requirement, as typed equations

"Simultaneously cofinal-invariant and `Ref_a`-natural" against the CDL architecture and the now
**PROVED** incidence half (Q-702):

```text
E1  Ref_a-NATURALITY of the incidence half:  sd*_2 d_1' = d_1 sd*_1  on every generator,
    and L_(h o g) = L_h o L_g, L_id = id.
E2  MEASURE TRANSPORT (IDX §2.3):  sum_i Vol_4(C'_i) ||F'_i||^2 = Vol_4(C) ||F||^2 + B_g,
    with B_g admissible under D11 conjunct 2.
E3  THE F-RULE:  F'_i = M_i F, natural in g.                       [ = the coframe square ]
E4  COFINAL-INVARIANCE (CDL):  the colimit over the causal exhaustion is invariant under
    passage to a cofinal subsystem.
E5  COMPATIBILITY:  E1-E3 (refinement side) and E4 (exhaustion side) hold of ONE correspondence.
```

### 2.2 What is proved from stock

```text
E1  PROVED.  Q-702: builder derivation 788 + independent adversarial confirmation 794 — the
    cochain-map identity as an EXACT INTEGER MATRIX IDENTITY on all three cases plus 771
    random-cochain trials, zero mismatches; L_id = id and per-generator existence PROVED at 795.
E2  PROVED FOR THE SURVIVING CANDIDATES, with B_g = 0 exactly: 795's (a2) and (b2) both give
    children/parent = 1.000000.  Exact recovery is STRONGER than D11 conjunct 2 requires.
E3  POSED AND FREE.  795: (a1) ELIMINATED by E2; (a2) and (b2) survive; residual 843 dimensions.
```

### 2.3 What fails

```text
NONE NEW.  The one thing that failed is already of record: 788 §3.3's min-norm rule, killed at
Q-702 (Freudenthal A2 fails at 1.20e-1, mixed composite at 1.36e-1).  It was the strongest
forcing candidate for E3 and it is dead — which leans E3 free and proves nothing.
```

### 2.4 What is unposeable — the missing object, named

```text
E4 and E5.  CDL's cofinal-invariance is stated as a FALSIFIER, never as a verified property, and
its own scope flags are false (global_source_inclusive_state_limit_derived = false; ...).  So E4
cannot be evaluated, and E5 — the single correspondence satisfying both sides — cannot be posed
until E4 is.
MISSING OBJECT, NAMED: a verified cofinal-invariance statement for the CDL colimit.  Not a
missing carrier now — the carrier exists (E1-E3) — but a missing VERIFICATION on the exhaustion
side.
```

---

## 3. AS3 — CLASSIFICATION

```text
BRIDGE = FREE.
   It is not UNDECIDABLE: the bridge is exhibited.  Either 795 candidate supplies E3 and satisfies
   E2 exactly, and E1 is PROVED — so a bridge from the refinement side EXISTS and is displayed.
   It is not FORCED: 843 dimensions of residual, two inequivalent complete candidates, and the
   strongest forcing candidate is dead of record.
   TWO COMPLETE DISPLAYS (from 795, neither adopted):
     (a2)  F'_i = F        — component inheritance, exact recovery
     (b2)  F'_i = sgn(p_i) F — orientation-weighted, exact recovery, differing on 12 of 24 children
   SCOPE, STATED: this is a bridge on the REFINEMENT side satisfying E1-E3.  E5 — that one
   correspondence serves both indices — awaits E4, which is unposeable.  I do NOT claim the
   exhaustion index is thereby reached.
```

### 3.1 What B1b inherits

```text
B1B_STATUS: RE-SCOPED, NOT BLOCKED.  792 left it "blocked at an index gap with no object".  It is
   now: the object is IDENTIFIED (the F-assignment rule), BUILT (795's candidate set), and FREE
   (843-dim residual, two candidates).  What remains for B1b is not construction but SELECTION —
   and selection is principal business under the void condition, not lane business.
   The one genuinely open item is E4's verification on the exhaustion side.
```

### 3.2 What C1 inherits

```text
C1_INHERITS: (i) a bridge that EXISTS but is not unique — so the common cell may be built against
   E1-E3 without waiting, provided it carries the F-rule as a PARAMETER and never fixes it;
   (ii) an unverified cofinal-invariance requirement (E4) which it must not assume — CDL states it
   as a falsifier, so C1 inherits a testable failure condition, not a granted property;
   (iii) the 792 finding unchanged: the uniqueness C1 needs is cofinality-invariance, not
   object-selection.
   NET CHANGE FROM 792: C1's blocker moves from "no bridge object" to "an unselected bridge plus
   one unverified exhaustion-side property".  Strictly better posed; not closed.
```

---

## 4. AS4 — FREEDOMS CONSUMED, FLATTENING CHECK

### 4.1 `FREEDOMS_CONSUMED` — item by item against §1–§3 (law 2a)

| datum | tag | where |
|---|---|---|
| the `F`-assignment rule (`M_i`) | **NOT ADOPTED** — two candidates carried, one eliminated of record | §2.2, §3 |
| child coframes `E_p`, orientation `sgn(p)` | **CARRIED AS DERIVED** (753) | §3 via 795 |
| intrinsic `Vol_4` | **CARRIED AS FORCED/CLASSIFIED** | §2.1 E2 |
| the parent frame `e = I` | **CARRIED AS THE SEALED INSTANCE, disclosed** — 795's scope statement is inherited unchanged; the E2 numbers are that instance's | §2.2 |
| the cofinal exhaustion | **CARRIED-AS-PARAMETER** — none selected; E4 stated as a demand | §2.4 |
| CDL's scope flags | **CARRIED AS FALSE, not assumed true** | §2.4 |
| `B_g` (the D11 conjunct-2 boundary term) | **CARRIED AS ADMISSIBLE, and not used** — the candidates give `B_g = 0` exactly, so no tolerance is consumed | §2.2 |
| the section freedom `J_1` | **CARRIED AS PARAMETER** — 788's residual, untouched | §2.1 E1 |
| scaling weights (law 2a) | **NONE CONSUMED** — no `beta`-graded statement here | — |
| a metric | **NOT ADOPTED** — the min-norm rule is dead of record and is not revived | §2.3 |

**SUBSTITUTED: none.**

### 4.2 `FLATTENING_CHECK`

```text
S26  C_ref barred as a source                    CLEAN — the bridge is built from IDX's own
     statement, 753's frames and the classified Vol_4; the smooth constituent supplies no step.
S08  no EM / smooth-field identification         CLEAN — F is a local frame two-form throughout.
S27, S28, S01 and the remaining rows: not touched.
FLATTENING_CHECK = clean (37 rows walked; 2 live, both discharged).
```

---

## 5. JURISDICTION AND VERB AUDIT

**Jurisdiction.** *What was the rule written to protect?* "Hunt before build, build before rule."
The hunt found the bridge already named in my own artifact; building was 795's; ruling is the
principal's, and §3.1 says so rather than selecting. *Does the outcome space distinguish a real
unblocking from a restatement?* Yes — §2.4 leaves E4/E5 unposeable and §3 scopes the FREE verdict
to the refinement side. *Would evidence look different if 792's "no object" were right?* Yes: IDX
§2.3 would not name the rule, and 795's candidates would not satisfy E2 exactly. Both do.

**VOID CONDITION.** No `F`-rule adopted, no complex selected, no exhaustion chosen. The candidate
that would be tidiest is not preferred; both are carried.

**BR-1.** The relay authorises settling the bridge; it does not authorise the result. §1.3 reports
a near-miss against my own interest, and §3's FREE is weaker than a FORCED would have been.

**Builder independence.** No `evaluator_build_A/` or `checks/` file read. Q-702's cross-check is
cited, not re-derived. `~/.codex` untouched; `memory-bank` never searched.

### 5.1 Self verb audit — **NOT CLEAN: three disclosures**

1. **792's "no sealed object carries one index to the other" was too weak a reading of my own
   IDX.** IDX §3.3 *names* the bridge and IDX §2.3 *states its content*. I wrote 792 having read
   755's restatement of the gap rather than IDX's own paragraphs. **Second time this arc I have
   under-read my own sealed artifact** — 795 disclosed the same failure about 753.
2. **I nearly ran the name-match trap on a verdict token.** `INHERITED_REFINEMENT_NATURALITY_
   FORCES_UNIFORM_MEASURE` reads like "refinement naturality is proven"; it is a statement about
   the measure's per-cell **value**, not the `F`-assignment rule. I was one step from banking it as
   the discharge of IDX §2. Caught by reading the body instead of the name.
3. **The FREE verdict is scoped to the refinement side and I say so before it can be misread.**
   E4 (cofinal-invariance) is unposeable and E5 unreachable; a bridge satisfying E1–E3 is *not* a
   bridge between the two indices, and I do not claim it is.

*Direction check:* 1 and 2 run against me; 3 bounds my own result. The finding that most flatters
this relay — that the bridge exists — is immediately limited by §3's scope statement and §2.4's
named missing verification.

---

```text
HUNT = 6 hits, 5 survivors, 1 near-miss disclosed.
   SURVIVORS: S1 IDX section 3.3 (names the bridge: the transport IS the measure functoriality);
   S2 IDX section 2.3 (states its content: "a rule assigning F on each new sub-face", and that the
   change-of-coframe law "says nothing about this"); S3 4d 430f0971…[21855,21975) ("It does not
   derive the coframe or the refinement bridge"); S4 BATT 14ddfc15…[4496,4636) — a NON-DARIO lane
   naming the same gap as "FUNCTORIALITY OF A MEASURE"; S6 the CDL family (exhaustion-side
   architecture, unchanged from 792).
   NEAR-MISS DISCLOSED: S5 R33 (packet-manifest sealed, mode 3), verdict INHERITED_REFINEMENT_
   NATURALITY_FORCES_UNIFORM_MEASURE.  It does NOT discharge IDX section 2: it forces the
   measure's per-cell VALUE on a child; IDX needs the F-ASSIGNMENT RULE.  Banking it would have
   been the name-match trap run on a verdict token.  Its real bearing: R33's binding item 4 IS
   D11 conjunct 1, which 788 showed is exact and untoleranced — so the record already uses
   conjunct 1 productively.
   NO object relating the two index CATEGORIES as such was found.  What was found is better: the
   bridge is a NAMED PROPOSITION whose content is the coframe square.
PATH_B = posed (5 equations).  PROVED: E1 Ref_a-naturality of the incidence half (Q-702 — builder
   788 + independent 794; exact integer matrix identity on all three cases plus 771 random-cochain
   trials, zero mismatches; L_id = id and per-generator existence at 795); E2 measure transport
   with B_g = 0 EXACTLY for both surviving candidates (children/parent = 1.000000), which is
   STRONGER than D11 conjunct 2 requires.  POSED AND FREE: E3 the F-rule — 795's square, (a1)
   ELIMINATED by E2, (a2) and (b2) surviving, residual 843 dimensions.  FAILED: none new; the one
   failure is of record — 788 section 3.3's min-norm rule, killed at Q-702 (Freudenthal A2 at
   1.20e-1, mixed composite at 1.36e-1), the strongest forcing candidate for E3.  UNPOSEABLE:
   E4 cofinal-invariance and hence E5 — CDL states cofinal-invariance as a FALSIFIER, never as a
   verified property, and its own scope flags are false.  MISSING OBJECT NAMED: a verified
   cofinal-invariance statement for the CDL colimit — a missing VERIFICATION on the exhaustion
   side, no longer a missing carrier.
BRIDGE = FREE (two complete displays, neither adopted).  NOT UNDECIDABLE: the bridge is EXHIBITED —
   either 795 candidate supplies E3 and satisfies E2 exactly, with E1 PROVED.  NOT FORCED: 843
   dimensions of residual, two inequivalent complete candidates, and the strongest forcing
   candidate dead of record.  DISPLAYS: (a2) F'_i = F, component inheritance, exact recovery;
   (b2) F'_i = sgn(p_i) F, orientation-weighted from 753's derived orientation, exact recovery,
   differing on 12 of 24 children.  SCOPE STATED: this is a bridge on the REFINEMENT side
   satisfying E1-E3; E5 — one correspondence serving BOTH indices — awaits E4, which is
   unposeable.  I do NOT claim the exhaustion index is thereby reached.
B1B_STATUS = RE-SCOPED, NOT BLOCKED.  792 left it "blocked at an index gap with no object".  The
   object is now IDENTIFIED (the F-assignment rule), BUILT (795's candidate set) and FREE.  What
   remains is not construction but SELECTION — principal business under the void condition, not
   lane business — plus E4's verification on the exhaustion side.
C1_INHERITS = (i) a bridge that EXISTS but is not unique, so the common cell may be built against
   E1-E3 without waiting, PROVIDED it carries the F-rule as a PARAMETER and never fixes it;
   (ii) an UNVERIFIED cofinal-invariance requirement (E4) which it must not assume — CDL states it
   as a falsifier, so C1 inherits a testable failure condition, not a granted property; (iii) 792's
   finding unchanged, that the uniqueness C1 needs is cofinality-invariance, not object-selection.
   NET CHANGE FROM 792: C1's blocker moves from "no bridge object" to "an unselected bridge plus
   one unverified exhaustion-side property".  Strictly better posed; not closed.
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+3): (1) 792's "no sealed object carries one index to the other" was
   TOO WEAK A READING OF MY OWN IDX — section 3.3 names the bridge and section 2.3 states its
   content; I wrote 792 from 755's restatement rather than IDX's own paragraphs, the SECOND time
   this arc I have under-read my own sealed artifact (795 disclosed the same about 753); (2) I
   NEARLY RAN THE NAME-MATCH TRAP ON A VERDICT TOKEN — INHERITED_REFINEMENT_NATURALITY_FORCES_
   UNIFORM_MEASURE reads like the proposition IDX needs but is about the measure's per-cell value,
   and I was one step from banking it as the discharge; caught by reading the body instead of the
   name; (3) the FREE verdict is SCOPED to the refinement side and stated so before it can be
   misread — E4 is unposeable and E5 unreachable, and a bridge satisfying E1-E3 is not a bridge
   between the two indices.  1 and 2 run against me; 3 bounds my own result.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
