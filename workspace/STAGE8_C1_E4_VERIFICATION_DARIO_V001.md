# STAGE 8 / 7A / [PLAN:C1-PRE] — E4: ONE CONJUNCT PROVED, ONE SUPPLIED UNDER ADOPTED RULES, ONE OBSTRUCTED AT A NAMED OBJECT

Lane: DARIO (Builder B, independent verifier). Relay 799.
State brief pinned: `PROGRAM_STATE_BRIEF_V005.md` = `e26f0d16055f3e83…` — digest matches, seal OK,
read before task work. Drift check: V005 current.
Governing: my own **798 / Q-704** — E4 is the named missing verification. Law 8 on every seal.
**Q-704's lesson applied: my own corpus got the same hunt discipline as foreign stock — I read the
sealed paragraphs, not my restatements of them.** All headline items **CLAIMED**.

## Lead determination — CLAIMED

**E4 is a three-conjunct statement. One conjunct is outright proved from the sealed construction,
one is supplied under already-adopted rules, and the third is obstructed at an object the record
explicitly forbids selecting now.**

```text
E4a  the colimit's DYNAMICS is exhaustion-independent        *** PROVED ***
E4b  the stabilized local RECORD STATES agree                SUPPLIED under adopted rules (scoped)
E4c  the DRESSED MAPS agree                                  *** OBSTRUCTED ***
```

**E4a is stronger than the relay asked for, and the sealed text hands it over directly.** The
packet-sealed direct-limit theorem constructs the colimit from `B`, *"the unit-weight incidence
generator"* on `l2(V)` — **`B` is defined on the whole complex and does not mention any
exhaustion.** Every exhaustion gives `P_n → I` strongly, so every exhaustion yields the *same*
strong limit `exp(-itB)ψ`.

> **Cofinality is not even needed. ANY two exhaustions agree, a fortiori any two cofinal ones.**

**E4c is the obstruction, and it is exact.** The falsifier is a disjunction — *"different
stabilized local record states **or** dressed maps"* — so verifying E4 requires **both** conjuncts,
and the dressed-maps conjunct needs the **global infinite-future source Møller unitary**, which is
flagged `false` in **two** sealed files and which the architecture adjudication expressly bars from
being chosen:

> *"A direct sum of label-preserving outgoing channels would provide such recovery, but **selecting
> that channel decomposition now would assume the object the gate must derive**."*

```text
E4 = OBSTRUCTED (failing step typed: the dressed-maps conjunct; missing object named).
```

**Net for C1: the common cell may now be built without fixing an exhaustion as far as the dynamics
goes — that is new and it is proved — while carrying the dressed-maps disjunct as a live,
untested falsifier.**

---

## 0. Preflight

```text
OUTPUT NAME  probed recursively: artifact and sidecar ABSENT.
LAW 8 on every seal.  The CDL family carries NO adjacent sidecars in either spelling; all are
   sealed by MODE 3 (packet-manifest membership), STAGE7_PACKET_MANIFEST_V001.sha256 verified.
ARCH  CAUSAL_DIRECT_LIMIT_ARCHITECTURE_ADJUDICATION_RESULT_V001.md  9be3f55fd527b9a8…  6,299 B
CDLP  CAUSAL_DIRECT_LIMIT_RECORD_PRINCIPLE_V001.md                  625b4ed9c91b28dd…  2,325 B
RED   CAUSAL_DIRECT_LIMIT_REDUNDANT_RECORD_RESULT_V001.md           3359960fb411eff8…  2,338 B
CIS   CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md                    b0c636f3b2b00f06…  doubly sealed
798   STAGE8_B1B_INDEX_BRIDGE_DARIO_V001.md                         6e663972846c2db2…  .md.seal OK

GATES: alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false.
No member binding; no fixed-point execution; no end test; no numeric evaluation of physical
quantities; no comparison to measured constants.  NO COMPLEX SELECTED.  NO F-RULE SELECTED.
NO SMOOTH IMPORT (S26).  NO EM IDENTIFICATION (S08).  No common cell formed; no junction map
evaluated.  PE-1..PE-7 pointer-known, zero weight, not opened, not consulted.
```

---

## 1. AS1 — E4, POSED

### 1.1 The construction the falsifier guards — `ARCH` §3, verbatim

> *"Let `V_n` exhaust a locally finite infinite causal complex `V`, let `P_n` be the corresponding
> projections on `l2(V)`, and let `B` be the unit-weight incidence generator. Under the
> cycle-7/DC3 bounded-incidence condition, `sup_n ||P_n B P_n|| <= ||B|| < infinity`. Define
> `B_n = P_n B P_n`, extended by zero outside `P_n H`. Since `P_n -> I` strongly, for every `psi`:
> `||B_n psi - B psi|| <= ||P_n B(P_n psi - psi)|| + ||(P_n - I)B psi|| -> 0`. Uniform boundedness
> and polynomial approximation of the exponential then give `exp(-itB_n)P_n psi -> exp(-itB)psi`
> strongly and uniformly for `t` in every compact interval. **Thus the direct limit exists for the
> declared bounded-degree operator class.**"*

### 1.2 The falsifier — `CDLP`, verbatim

> *"**two cofinal physical exhaustions give different stabilized local record states or dressed
> maps**"*

**Typed.** The falsifier is a **disjunction**. Its negation — the theorem candidate — is a
**conjunction**:

```text
E4  :=  for any two cofinal physical exhaustions {V_n}, {W_m} of the same causal complex V,
        (E4a) the colimit dynamics agree,               AND
        (E4b) the stabilized local record states agree,  AND
        (E4c) the dressed maps agree,
        up to the family's own sealed equivalence.

OBJECTS TYPED:  V a locally finite infinite causal complex; V_n, W_m finite subcomplexes
   increasing with union V; P_n, Q_m the corresponding orthogonal projections on l2(V);
   B the unit-weight incidence generator on l2(V); B_n = P_n B P_n; the record states the
   stabilized quasi-local outgoing states of CDLP; the dressed maps the Moller-type maps CDLP
   names alongside them.
```

[YOURS] **I state the conjunction explicitly because at 788 I collapsed a conjunctive sealed
clause and it cost a headline.** Verifying E4 means discharging **three** conjuncts, and a proof
of one is not a proof of E4.

---

## 2. AS2 — THE PROOF ATTEMPT

### 2.1 E4a — **PROVED** from sealed ingredients

```text
CLAIM.  For any two exhaustions {V_n}, {W_m} of V satisfying bounded incidence, the colimit
        dynamics coincide.

PROOF.  By ARCH section 3, B is the unit-weight incidence generator ON l2(V).  Its definition
        quantifies over V, not over any exhaustion: B is the SAME operator for both.
        Each exhaustion gives P_n -> I and Q_m -> I strongly (this is what "exhaust" means).
        ARCH section 3's estimate then gives, for every psi and every compact t-interval,
            exp(-itB_n) P_n psi -> exp(-itB) psi      and
            exp(-itB'_m) Q_m psi -> exp(-itB) psi,
        the SAME limit, because the right-hand side contains no reference to the exhaustion.
        Hence the two colimit dynamics agree.  QED
```

**Carried hypothesis:** the cycle-7/DC3 bounded-incidence condition (`sup_n ||P_n B P_n|| ≤ ||B||`),
which `ARCH` states as the theorem's own condition. **Nothing further is assumed.**

**Strength, stated exactly:** cofinality is **not used**. The argument holds for *any* two
exhaustions. E4a is therefore proved *a fortiori* for cofinal ones.

*Instrument note, disclosed:* I ran a finite numerical check (three different exhaustion orders of
a 60-site bounded-degree complex, deviation `0.0` at full exhaustion). **That check is nearly
trivial** — at full exhaustion every projection is the identity — and it confirms only that I read
the construction correctly. **The proof is the structural observation above, not the numerics, and
I do not present the numerics as evidence for the theorem.**

### 2.2 E4b — **SUPPLIED under already-adopted rules**, with its scope named

`RED`, verbatim:

> *"Spacelike-disjoint controlled writes commute. Different linear extensions of the same causal
> order therefore give the same circuit whenever they differ only by interchanging
> spacelike-disjoint writes. Causally dependent writes retain their causal order."*

with `causal_linear_extension_independence_scoped = true` and
`outgoing_record_recoverability_derived_under_adopted_write_rule = true`.

```text
SUPPLIED: the record-state half, under the ALREADY ADOPTED primitive controlled-write rule.
CARRIED AS HYPOTHESES, NOT ASSUMED (all flagged false of record):
   primitive_write_rule_derived_here = false        (adopted elsewhere, carried)
   ready_state_boundary_condition_derived = false
   finite interaction-window closure                (inherited by RED's own scope clause)
SUB-GAP, NAMED RATHER THAN WAVED THROUGH:
   RED's independence is SCOPED to differences by spacelike-disjoint interchange.  Two cofinal
   EXHAUSTIONS are increasing sequences of finite subcomplexes, not literally two linear
   extensions of one order; that any two such sequences differ only by spacelike-disjoint
   interchange is NOT stated in RED and I do not supply it.  E4b is therefore SUPPLIED-MODULO
   this identification, not proved outright.
```

### 2.3 E4c — **OBSTRUCTED. The exact failing step**

The falsifier names **dressed maps** as a separate disjunct. Verifying E4 requires them to agree.
The object that would let one compare them is flagged **false** in two sealed files:

```text
CDLP  global_infinite_future_source_Moller_unitary_derived = false
CIS   outgoing_Moller_sector_derived = false
```

and `ARCH` §4 states the same in prose as one of the five things *"the disclosed inputs do not
currently force"*:

> *"a label-preserving outgoing or tail algebra from which the written alternative is publicly
> recoverable."*

with the bar on supplying it now, verbatim:

> *"A direct sum of label-preserving outgoing channels would provide such recovery, but **selecting
> that channel decomposition now would assume the object the gate must derive**."*

```text
THE FAILING STEP, TYPED:
   Two cofinal exhaustions each induce a dressing of the local algebra by their own outgoing
   channel data.  To compare the two dressed maps one needs the global infinite-future source
   Moller unitary intertwining them.  That unitary is NOT DERIVED (two sealed flags), and the
   channel decomposition that would supply it MAY NOT BE SELECTED (ARCH section 4).
   MISSING OBJECT, NAMED: the global infinite-future source Moller unitary / the label-preserving
   outgoing channel decomposition — derivable, per ARCH section 5, only "from the same
   target-independent source-record-gravity-gauge action required by R3".
   THIS IS NOT A SHRUG: the object is named, its two sealed false-flags are cited, and the record
   states both why it is absent and the only lawful route to it.
```

### 2.4 Verdict

```text
E4 = OBSTRUCTED.  E4a PROVED; E4b SUPPLIED-MODULO one named identification; E4c OBSTRUCTED at a
     named missing object.  The conjunction does not close.
```

---

## 3. AS3 — THE SCOPE-FLAG LEDGER

```text
DISCHARGED by this relay:
   NONE of the listed flags.  E4a is a NEW statement (exhaustion-independence of the colimit
   dynamics) that no flag tracks; it discharges no false flag and I claim no flag flip.
   *** Stated plainly so the proof is not read as a promotion. ***

CONSUMED AS HYPOTHESIS (carried, never assumed true):
   the cycle-7/DC3 bounded-incidence condition        [ARCH section 3's own condition]
   primitive_write_rule_derived_here = false          [adopted elsewhere; RED carries it]
   ready_state_boundary_condition_derived = false
   finite interaction-window closure                  [RED's inherited scope]

BLOCKING E4c (the obstruction):
   global_infinite_future_source_Moller_unitary_derived = false      [CDLP]
   outgoing_Moller_sector_derived = false                            [CIS]
   recoverable_outgoing_record_algebra_derived = false               [ARCH]

UNTOUCHED by this relay:
   unique_microscopic_causal_complex_selected = false
   unique_covariant_spectral_measure_derived = false
   global_source_inclusive_state_limit_derived = false
   curved_nonstationary_extension_derived = false
   absolute_charged_response_normalization_derived = false
   complete_parent_action_derived = false ; fork_8_closed = false
   hypothesis_promoted_to_principle = false ; physical_durability_derived = false
```

---

## 4. AS4 — C1 CONSEQUENCE

```text
OUTCOME REACHED: OBSTRUCTED.  The consequences below are for that outcome; the other two are
stated for completeness because AS4 asks for each.

C1_MAY_ASSUME (under OBSTRUCTED):
   (i)  THE COLIMIT DYNAMICS IS EXHAUSTION-INDEPENDENT (E4a, PROVED).  The common cell may be
        built WITHOUT fixing or selecting an exhaustion, as far as the dynamics is concerned.
        This is new and it is the relay's positive result.
   (ii) The record-state half, PROVIDED it carries E4b's three hypotheses explicitly and the
        sub-gap of section 2.2 as an open identification — assume it only in that conditioned form.

C1_MUST_CARRY (under OBSTRUCTED):
   (i)  THE DRESSED-MAPS DISJUNCT AS A LIVE FALSIFIER.  C1 may NOT assume two cofinal exhaustions
        give the same dressed maps.  If they differ, CDLP's falsifier fires and the architecture
        C1 is built on fails in its declared branch.
   (ii) The named missing object as a prerequisite, not a detail: the global infinite-future
        source Moller unitary, obtainable only from the complete target-independent parent action.
   (iii) The bar: C1 may NOT select a label-preserving outgoing channel decomposition to close the
        gap — ARCH forbids exactly that move.

HAD E4 PROVED: C1 could treat cofinal-invariance as granted and build the common cell against the
   colimit directly; the 792/798 requirement would be discharged.
HAD E4 BEEN UNPOSEABLE: C1 would inherit no testable condition at all and would have to wait; that
   is NOT the outcome — the falsifier is posed, typed, and testable once the Moller object exists.
```

---

## 5. FREEDOMS CONSUMED, FLATTENING CHECK

### 5.1 `FREEDOMS_CONSUMED` — item by item against §1–§4 (law 2a)

| datum | tag | where |
|---|---|---|
| the exhaustion `{V_n}` | **CARRIED-AS-PARAMETER — and E4a proves the dynamics does not depend on it** | §2.1 |
| bounded incidence (cycle-7/DC3) | **CONSUMED AS HYPOTHESIS** — `ARCH` §3's own condition, cited not assumed | §2.1 |
| the primitive controlled-write rule | **CARRIED AS ADOPTED ELSEWHERE**, not derived here | §2.2 |
| the ready-state boundary condition | **CARRIED AS HYPOTHESIS** (flag false) | §2.2 |
| the outgoing channel decomposition | **NOT SELECTED — explicitly barred by `ARCH` §4** | §2.3 |
| the Møller unitary | **CARRIED AS ABSENT**, named as the obstruction | §2.3 |
| the root spectral measure / its density `rho_f` | **NOT SELECTED** — `ARCH` §4 displays the whole admissible family; none chosen | not used |
| the causal complex `V` | **CARRIED-AS-PARAMETER** — no complex selected | §1.2 |
| the `F`-assignment rule (798/795) | **NOT SELECTED** — untouched by this relay | — |
| scaling weights (law 2a) | **NONE CONSUMED** — no `beta`-graded statement here | — |

**SUBSTITUTED: none.**

### 5.2 `FLATTENING_CHECK` — against `DECLINE_REGISTER_V002` (S01–S37)

```text
S26  C_ref barred as a source            CLEAN — not invoked; the entire argument is
     operator-theoretic on l2(V) plus the sealed CDL/CIS/RED clauses.
S08  no EM / smooth-field identification CLEAN — B is the unit-weight incidence generator; no
     physical field reading is attached.
S24  "any lane reach for a CLUSTERING AXIOM blocks immediately; adoption is principal-only and may
     not rescue a route"                 LIVE AND OBSERVED — E4c is NOT rescued by reaching for a
     clustering or channel-decomposition axiom; the bar is quoted and obeyed.
S27, S28, S01 and the remaining rows: not touched.
FLATTENING_CHECK = clean (37 rows walked; 3 live, all discharged).
```

---

## 6. JURISDICTION AND VERB AUDIT

**Jurisdiction.** *What was the rule written to protect?* AS2's "786 standard" forbids returning a
shrug where an obstruction is due. The risk was live: E4 could have been reported "unposeable" a
second time. It is not — §2.3 names the object, cites two false flags, and quotes the record's own
bar and its only lawful route. *Does the outcome space distinguish a proof from a gesture?* Yes:
E4a is proved and E4c is obstructed in the same artifact, so the instrument separates them.
*Would evidence look different if E4a were false?* Yes — `ARCH` §3 would have to define `B`
per-exhaustion. It does not.

**VOID CONDITION.** No exhaustion selected, no channel decomposition selected, no spectral density
selected. The one move that would close E4c is precisely the one `ARCH` bars, and §2.3 quotes the
bar rather than stepping around it.

**BR-1.** The relay authorises the campaign, not its result. The result is an obstruction.

**Builder independence.** No `evaluator_build_A/` or `checks/` file read. `~/.codex` untouched;
`memory-bank` never searched.

### 6.1 Self verb audit — **NOT CLEAN: three disclosures**

1. **My numerical check for E4a is nearly trivial and I say so rather than let it decorate the
   result.** At full exhaustion every projection is the identity, so the three orders agreeing is
   bookkeeping. The proof is structural — `B` does not mention the exhaustion — and the numerics
   verify only my reading.
2. **I typed the falsifier as a disjunction before using it**, because at 788 I collapsed a
   conjunctive sealed clause and lost a headline to it. Here the negation is a three-conjunct
   statement, and proving one conjunct is not proving E4 — stated at §1.2 *before* §2 could blur
   it.
3. **E4b is SUPPLIED-MODULO, not proved, and the sub-gap is mine to name.** `RED`'s independence is
   scoped to spacelike-disjoint interchange; that two cofinal *exhaustions* differ only so is a
   step `RED` does not take and I did not supply. It would have been easy to let "linear
   extensions" and "exhaustions" pass as the same object — the name-match trap in its ordinary
   clothes.

*Direction check:* all three bound or weaken my own result. The relay's positive finding — E4a —
is delivered with its strength stated exactly (cofinality unused) **and** with §3's note that it
discharges no flag, so it cannot be read as a promotion.

---

```text
E4_POSED = statement displayed (spans cited).  The construction: ARCH section 3, packet-sealed —
   "Let V_n exhaust a locally finite infinite causal complex V, let P_n be the corresponding
   projections on l2(V), and let B be the unit-weight incidence generator... exp(-itB_n)P_n psi ->
   exp(-itB)psi strongly and uniformly for t in every compact interval.  Thus the direct limit
   exists for the declared bounded-degree operator class."  The falsifier: CDLP — "two cofinal
   physical exhaustions give different stabilized local record states or dressed maps."  It is a
   DISJUNCTION, so E4 is the THREE-CONJUNCT negation: for any two cofinal physical exhaustions,
   (E4a) the colimit dynamics agree AND (E4b) the stabilized local record states agree AND (E4c)
   the dressed maps agree.  Objects typed at section 1.2.
E4 = OBSTRUCTED (failing step typed; missing object named).
   E4a PROVED: B is the unit-weight incidence generator ON l2(V) — its definition quantifies over
   V, not over any exhaustion, so it is the SAME operator for both.  Every exhaustion gives
   P_n -> I strongly, so ARCH section 3's estimate yields the SAME strong limit exp(-itB)psi for
   each.  COFINALITY IS NOT USED: any two exhaustions agree, a fortiori any two cofinal ones.
   Carried hypothesis: the cycle-7/DC3 bounded-incidence condition, ARCH's own.
   E4b SUPPLIED-MODULO one named identification: RED gives "Spacelike-disjoint controlled writes
   commute.  Different linear extensions of the same causal order therefore give the same circuit
   whenever they differ only by interchanging spacelike-disjoint writes", with
   causal_linear_extension_independence_scoped = true and
   outgoing_record_recoverability_derived_under_adopted_write_rule = true.  SUB-GAP NAMED: two
   cofinal EXHAUSTIONS are increasing sequences of finite subcomplexes, not literally two linear
   extensions of one order; that any two differ only by spacelike-disjoint interchange is NOT
   stated in RED and I do not supply it.
   E4c OBSTRUCTED — THE FAILING STEP: two cofinal exhaustions each induce a dressing by their own
   outgoing channel data, and comparing the dressed maps requires the GLOBAL INFINITE-FUTURE
   SOURCE MOLLER UNITARY intertwining them.  Flagged FALSE in two sealed files
   (CDLP global_infinite_future_source_Moller_unitary_derived = false ; CIS
   outgoing_Moller_sector_derived = false), with ARCH section 4 naming the same absence in prose
   and BARRING the fix: "selecting that channel decomposition now would assume the object the gate
   must derive."  Only lawful route, per ARCH section 5: "from the same target-independent
   source-record-gravity-gauge action required by R3."
FLAGS = discharged: NONE (E4a is a new statement no flag tracks; no flag flip claimed, stated so
   the proof is not read as a promotion) / consumed-as-hypothesis: cycle-7/DC3 bounded incidence;
   primitive_write_rule_derived_here = false; ready_state_boundary_condition_derived = false;
   finite interaction-window closure / blocking E4c:
   global_infinite_future_source_Moller_unitary_derived = false;
   outgoing_Moller_sector_derived = false; recoverable_outgoing_record_algebra_derived = false /
   untouched: unique_microscopic_causal_complex_selected, unique_covariant_spectral_measure_derived,
   global_source_inclusive_state_limit_derived, curved_nonstationary_extension_derived,
   absolute_charged_response_normalization_derived, complete_parent_action_derived, fork_8_closed,
   hypothesis_promoted_to_principle, physical_durability_derived — all false, all untouched.
C1_MAY_ASSUME = (i) THE COLIMIT DYNAMICS IS EXHAUSTION-INDEPENDENT (E4a, PROVED) — the common cell
   may be built WITHOUT fixing or selecting an exhaustion, as far as the dynamics is concerned;
   (ii) the record-state half ONLY in conditioned form, carrying E4b's three hypotheses explicitly
   and section 2.2's sub-gap as an open identification.
C1_MUST_CARRY = (i) THE DRESSED-MAPS DISJUNCT AS A LIVE FALSIFIER — C1 may not assume two cofinal
   exhaustions give the same dressed maps; if they differ, CDLP's falsifier fires and the
   architecture C1 is built on fails in its declared branch; (ii) the global infinite-future source
   Moller unitary as a PREREQUISITE, obtainable only from the complete target-independent parent
   action; (iii) the BAR — C1 may not select a label-preserving outgoing channel decomposition to
   close the gap, since ARCH forbids exactly that move (and S24 bars reaching for a clustering
   axiom to rescue a route).
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+3): (1) my numerical check for E4a is NEARLY TRIVIAL — at full
   exhaustion every projection is the identity — and it verifies only my reading, not the theorem;
   the proof is structural and I say so rather than let the numerics decorate it; (2) I TYPED THE
   FALSIFIER AS A DISJUNCTION BEFORE USING IT, because at 788 I collapsed a conjunctive sealed
   clause; proving one conjunct is not proving E4, stated at section 1.2 before section 2 could
   blur it; (3) E4b is SUPPLIED-MODULO, not proved — RED's independence is scoped to
   spacelike-disjoint interchange, and that two cofinal EXHAUSTIONS differ only so is a step RED
   does not take and I did not supply; letting "linear extensions" and "exhaustions" pass as one
   object would have been the name-match trap in ordinary clothes.
   All three bound or weaken my own result; E4a is delivered with its strength stated exactly and
   with the note that it discharges no flag.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
