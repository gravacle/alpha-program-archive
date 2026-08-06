# STAGE 8 / TASK 6 / STEP 1 — REVIEW OF THE A32 PREPARATION AND THE INSTRUMENT — DARIO V001

Lane: Dario (Claude Opus 5), cross-family review lane
Task: PASTE 600 / Task 6, Step 1
Authority to review: DoR-020-A8. **THIS ARTIFACT RATIFIES NOTHING AND LIFTS NO GATE.**
Custody: the ratification rests on this review.

```text
REGISTER_HEAD = Q-533
A32_PREP = DEFECTIVE (+1 missed sealed principal act; +2 NOTES)
MISSED_SOURCES = found (+1: PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29)
M5A = DEFECTIVE (+1, inherited from the missed act; repairable)
INSTRUMENT = NOT READY_FOR_RATIFICATION (+1, the same inheritance; otherwise strong)
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none of my own
```

**The defect is conservative in direction and repairable in one row, but it sits
in the gate that licenses Step 2 and all numerical execution, so it should be
repaired before ratification rather than after.** Everything else in this
preparation is strong, and §3's instrument is the best-built gate text I have
reviewed in this program.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-533 | verified |
| `STAGE8_TASK6_A32_PREP_LANE3_V001.md` = `0f5976a29b3990073bbb57bc9250fa4e7a164f3e0f1479462387adb8b79baa6b` | **verified before reading** |
| 867 lines as stated | verified |
| Output name collision (workspace + cleanroom) | none — clear to write |

---

## G1. THE SOURCE CONSOLIDATION — **DEFECTIVE (+1)**

### G1.1 The fifteen hashes, recomputed by me — 14 exact, 1 live-mutable

I recomputed all fifteen independently rather than accept the census.

**Fourteen reproduce byte-exactly** (sources 1–9 and 11–15). Mirrors in
`alpha_supervision` and `alpha-program-archive/supervision` agree, consistent
with the census's "duplicate archive mirrors are not separate sources."

**Source 10 does not, and this is register advance rather than a bad pin.** The
census pins `QUESTIONS_SETTLED_REGISTER_V001.md` at `89cab162…`; I compute
`906e1274…`, and the file's own sidecar now reads `906e1274…`. The cause is
visible in the file: **Q-533 was appended after the prep was written — and Q-533
is the entry that records this very prep artifact.** The register grew from
13,121 to 13,142 lines.

[PROVABLE] The prep's content citations survive the advance. I checked
`:13119-13121` and it still resolves exactly to the Q-532 entry, because the
register is append-only before a fixed trailer, so existing entry line numbers do
not shift.

### N1 — NOTE: a live document cannot be pinned the way a sealed one can

[YOURS] Source 10 is categorically different from the other fourteen: it is a
living, append-only record whose file hash has a lifetime of one register entry.
The census presents all fifteen under one verification idiom ("The hash in every
numbered row below was recomputed"). Neither I at Q-533 nor the principal at
Q-534 can reproduce source 10's pin — not because anyone erred, but by
construction.

Repair, one line: mark source 10 **live-mutable** and treat the **entry
citations** (Q-number plus quoted text) as its pin, which the census already
supplies in its load-bearing-lines column and which are stable under appends.

### G1.2 The V011 byte-version trap — caught by the prep, confirmed by me

[PROVABLE] I reproduced both byte-versions independently: root V011 =
`20a3a17d…` with **no seal attachment found**, sealed packet V011 = `aa7c6d49…`,
manifest-verified. §1.2's finding is exactly right, and the lawful composite (S2)
is the correct disposition. This is a real corpus-audit trap and the prep did not
walk into it.

§1.3's drift board likewise **displays** rather than harmonizes. The row I
consider the best moment in the census is the refusal to backdate: the unsealed
root says comparator expressions are *"cited before"*, ratified V002 says
*"citable BEFORE"*, and the prep rules the V002 phrase controls and *"no
backdated citation claim is invented."*

### G1.3 The twenty obligations and the count

[PROVABLE] The count is exact and structurally sourced: V000's **13 mechanical
items** + **6 principal items** + **A20** (Q-28's comparator-precision clause) =
20, with V002 itself carrying the *"Count correction of record: THIRTEEN items,
not twelve."* No double-counting and no silent merge.

The obligations I checked against their cited lines are faithful in both
directions — neither hardened nor softened. In particular the Q-25 limitation is
carried at **full** strength (permanent; process independence and independent
attestation never established; travels with every headline), and the scalar-only
caveat carries **both** conjuncts (collector revision **and** recommitment before
prediction).

### G1.4 THE MISSED SOURCE — a sealed principal act, never cited

[PROVABLE — verified end to end by me]

```text
supervision/PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29.md
computed   70c4080eae018bd644a3f0694557f1c0e854d621aa61097c775737887fec528f
sidecar    70c4080eae018bd644a3f0694557f1c0e854d621aa61097c775737887fec528f   (match)
dated      2026-07-29 — ONE DAY AFTER the A32 V002 ratification
standing   "A PRINCIPAL ACT ... THE ACT IS AUTHORITY AND IS DISCLOSED AS AUTHORITY"
```

**The prep never cites it.** Its single lexical near-match is census **source 15**
(`STAGE8_PREREGISTRATION_ENCODING_PRECEDENCE_AND_A32_PREPARED_TEMPLATE_AUTHORITY_RECORD_V001.md`)
— a *workspace record* with a confusingly similar name and a different subject
(V001 prepared/not-ratified). The *supervision principal decision* is absent.

**What it rules.** It ranks two encodings of the seal graph that were both already
present:

> 1. `stage_dependencies` **IS AUTHORITATIVE FOR GRAPH STRUCTURE** — the node set,
>    the edges, and therefore the fail-closed descendant computation.
> 2. `stage_dag` **IS DESCRIPTIVE** and remains binding for the non-seal
>    preconditions it carries … every one of them still binds.
> 4. THE STRICTER READING IS ADOPTED DELIBERATELY … **This act cannot loosen any
>    gate.**

**I verified the authoritative encoding myself** rather than take the ruling's
summary:

```text
NODE COUNT = 11                          (the prose DAG has 10)
SPEC-SEAL                      <- []
QSPEC-SPEC-SEAL                <- ['SPEC-SEAL']
HOLDOUT-UNIVERSE-SEAL          <- ['SPEC-SEAL']
PREDICTION-MAP-SEAL            <- ['HOLDOUT-UNIVERSE-SEAL', 'QSPEC-SPEC-SEAL']
END-TO-END-RECONSTRUCTION-SEAL <- ['ALPHA-RESULT-SEAL', 'HOLDOUT-RESULT-SEAL']
FINAL-CLAIM-SEAL               <- ['END-TO-END-RECONSTRUCTION-SEAL', 'HOLDOUT-RESULT-SEAL']
```

All four differences the ruling names are real: the eleventh node exists,
`HOLDOUT-UNIVERSE-SEAL` gains the parent `SPEC-SEAL`, `PREDICTION-MAP-SEAL` gains
the additional parent `QSPEC-SPEC-SEAL`, and `QSPEC-SPEC-SEAL` gains `SPEC-SEAL`.

**Why it is admissible as source 16 under the prep's own rules.** The prep admits
a source that supplies *"an A32 obligation or authorization dependency"* or *"a
later principal amendment or supersession."* This decision is both, is sealed, is
dated after the A32 ratification, and nothing in the register supersedes it.

**Aggravating, and worth stating plainly:** both `HOLDOUT-UNIVERSE-SEAL` and
`PREDICTION-MAP-SEAL` are on the prep's **own declared §0.2 sweep list**, and both
tokens appear verbatim in the missed decision. The prep's stated method should
have surfaced it.

**Mitigating, and equally worth stating:** the missed encoding is **stricter in
every difference**. The prep therefore *under-demands*; it cannot have licensed
anything unlawful, and no substantive conclusion of the preparation
(`A32 = RATIFIED_PROCEDURE_NOT_ATTAINED`, no gate lifted, no number) is disturbed.

**Consequence:** `A32_SOURCE_CENSUS = 15_LOAD_BEARING_SOURCES` is falsified as
displayed; the correct count is **16**. Repair: add one census row and redisplay
the ladder against the ruled encoding.

I separately checked the prep's three **exclusion** arguments — the
dependency-map exclusion and the Q-23/Q-24 and Q-28 supersession claims — and all
three are sound.

---

## G2. THE MAPPING — **PASS, +1 NOTE**

[PROVABLE] The arithmetic is displayed rather than inferred, and it verifies:

```text
SATISFIABLE-AS-INHERITED = {M1,M2,M5,M7,M8,P1}          = 6;
NEEDS-A-TASK-6-STEP      = {M10,M11,P2,P5,P6,A20}       = 6;
IN-TENSION               = {M3,M4,M6,M9,M12,M13,P3,P4}  = 8;   TOTAL = 20.
```

The three category definitions are stated before use, and the satisfiable
definition carries the right disclaimer — it *"does not mean the corresponding
ladder seal is true."*

**Two rows recomputed by me against the actual sources:**

- **P3 (IN-TENSION) — faithful.** Source 12 states verbatim: *"Five of six
  families do not yet support a formula-level comparator payload. The sixth …
  has a published formula payload frozen before any theory prediction, but Q-28
  now refutes that precision branch."* The prep's row matches, and the source's
  *"Zero of the six … eligibility stage has not been executed"* is carried at P6.
- **M2 (SATISFIABLE-AS-INHERITED) — faithful.** The CODATA 2022 fixed-vintage
  registry is ruled of record (*"Registry = CODATA 2022 fixed-vintage artifact"*).
  The "unparseable version excluded" half is handled separately at M4, which is
  filed IN-TENSION — a correct separation rather than a row doing double duty.

I found **no mis-filed row in either direction**.

### N2 — NOTE: the tension board is heterogeneous, and the summary flattens it

[PART-PROVABLE] The eight tensions are not of one kind, and (M5a) cannot close
three of them:

- **M9** is **permanent by principal disposition**. Its own row says so —
  Q-25 *"records permanently that process independence and independent
  attestation were never established."* No implementation closes it; the correct
  treatment is carriage and disclosure, which the instrument does exactly.
- **P3** and **P4** are **type/observable gaps, not custody gaps.** P3: *"No
  source establishes that a published physical comparator consumes `LOCAL-SHADOW`
  faithfully."* P4: the product is `LOCAL-SHADOW`, and *"a candidate lacking an
  exact domain bridge is ineligible."* No amount of schema or ID engineering
  supplies a published comparator that can consume the product's type.

**The prep itself is honest about each row** and never claims all eight are
implementation gaps — I checked; the phrase does not occur in the artifact. The
flattening appears in the **register's Q-533 summary** (*"8 IN TENSION — all
implementation-custody gaps"*), which is what a ratifying reader is most likely
to see. I raise it here because ratifications are often taken from summaries.

**The consequence the principal should carry:** completing (M5a) does **not**
clear the tension board. Three tensions survive full compliance — one permanently,
two pending an object no Task-6 custody step supplies. And P4's *"exact domain
bridge"* from `LOCAL-SHADOW` to a physical alpha-adjacent observable is the same
type-crossing the J-II obstruction blocks at Q-521. **The A32 board inherits
Task 5's structural fact rather than escaping it.**

---

## G3. THE (M5a) SUBGATE — **DEFECTIVE (+1, inherited)**

### G3.1 The sequencing law — binding, and correctly anti-circular

[PROVABLE] The ordering is stated without an exploratory loophole: (M5a) is
*"before the Step-2 scope DoR and **before any numerical execution**"*, and — the
clause that matters most — *"**It is not Task-6 Step 8.** Step 8 later seals the
number and prediction outputs produced through the already-sealed interface."*
The (M7) ladder repeats it: Step 8 *"does NOT create the prerequisite
prediction-map seal."*

That closes the retroactive-sealing attack, which is the way this kind of gate
usually fails: sealing the map after the number exists. The prep names its own
motive — *"to prevent the old 'attain A32' / new 'A32 preparation' wording from
creating a circular board."*

I also credit the anti-pressure clause, because the empty screen is exactly when
the temptation appears: *"The current all-three-condition screen being empty is
not permission to relax a rule, select a favorable branch, or strip the shadow
type."*

### G3.2 THE DEFECT — (M5a) is built on the demoted encoding

[PROVABLE] (M5a) conjoins `HOLDOUT-UNIVERSE-SEAL` and `PREDICTION-MAP-SEAL` as
readiness conditions. Under the encoding a sealed principal act **ruled
authoritative**, those seals carry parents (M5a) never names:

```text
required but unnamed in (M5a):  SPEC-SEAL          (parent of HOLDOUT-UNIVERSE-SEAL)
required but unnamed in (M5a):  QSPEC-SPEC-SEAL    (parent of PREDICTION-MAP-SEAL)
absent from the prep entirely:  END-TO-END-RECONSTRUCTION-SEAL  (the 11th node)
```

This matters because (M5a) is to be **evaluator-certified**. An evaluator
certifying the eight stated conjuncts item by item could certify
`PREDICTION-MAP-SEAL` without ever reaching `QSPEC-SPEC-SEAL` or `SPEC-SEAL`. On
the alternative reading — that naming a seal implicitly imports its parents under
fail-closed descendant computation — (M5a) is merely terser than the graph. But a
gate that licenses all numerical execution should not depend on which reading its
certifier adopts.

The ruling's own words make the direction unambiguous: *"This act cannot loosen
any gate."* An (M5a) drawn from the demoted encoding does exactly that, by
inheritance rather than by intent.

**Also unnamed:** the non-seal preconditions the ruling expressly preserves —
passed A-matrix rows, executed Gates 1–5, the composition-loop result, the beacon
rule, the complete target-free `Q_spec`, unanimous report counts, A33
reconstruction — *"ARE NOT DISCARDED … every one of them still binds."* The
twenty-row table carries none of them as a row.

**Repair, and it is small:** admit the decision as source 16, redisplay the ladder
against `stage_dependencies`, and name the two parent seals (and, where relevant,
the eleventh node) inside (M5a)'s conjunction.

### G3.3 No other weakening

I compared (M5a)'s conjuncts against the twenty obligations for softened scopes,
"must"→"should" drift, or cheaper substitutes, and found none. Conjunct 3
correctly carries the Q-25 qualification rather than pretending to resolve it.

---

## G4. THE INSTRUMENT — **NOT READY (+1, the same inheritance); otherwise strong**

The operative gate text is a single unbroken blockquote. I verified each required
carry is **inside** it, not in surrounding commentary.

**1. The number's type — INSIDE.**
`COMPUTATION_SCOPE = LOCAL`, `PRODUCT_TYPE = LOCAL-SHADOW`,
`TRIAL = ONE-SIDED_ON_CURRENT_FINITE_CHI_LATTICE`, `PERIOD_NATIVE = false`, with
the anti-rename clause: it *"may not be renamed a global period, holonomy charge,
period-native Maxwell quantity, `kappa_Thomson`, physical alpha, or a two-sided
trial."* And the anti-laundering clause: *"`LOCAL-SHADOW` is not promoted by
passing through A32."*

**2. The one-sided rider — INSIDE.** *"a nonzero seed may confirm inside the
licensed local lattice, while seed zero is a pole/out-of-lattice condition and is
**not a negative verdict**"* — which matches the seed adjudication's one-sidedness
exactly. The period cure is carried at item 3 as `CARRIED-CONDITIONAL`, requiring
a formed period route and the true `d^per` modulus certificate.

**3. The Q-25 permanent limitation — INSIDE, at full strength.** *"Every A32
headline and any `FINAL-CLAIM` shall state: cryptographic concealment is accepted,
but process independence between collector and custodian was never established and
no independent attestation exists,"* reinforced by *"M9 is carried exactly as
Q-25's accepted permanent limitation, **never restated as independent custody
proved**."* That closes the restatement attack.

**4. The scalar-only caveat — INSIDE, both conjuncts.** *"The present collector is
confined to the scalar fixed-column universe. Any vector or multicomponent
extension requires collector revision **and** recommitment before any prediction
exists."*

**Refuses attainment-by-preparation — yes, by enumeration.** The instrument opens
by denying each specific thing: it does not declare A32 attained, create any of
the five named seals, authorize numerical evaluation, bind a member, execute a
fixed point or end test, compute a number, compare with a measured central value,
or change a protected flag. The (L0) four-way distinction is fixed in the lead and
honoured in the text.

**Nothing authored beyond binding — yes.** §3.1's (I0) table sources every field,
and books the only new act honestly: *"The only new act is the proposed conjunction
of those existing fields on one named subject. The draft is `[YOURS]`."*

**Two clauses I want on the record as unusually good.** Both A7 branches must be
*"computed and reported per branch, with neither selected, averaged, merged, or
dropped"*, and — closing the implementation-pressure loophole — *"If the
prediction-map schema cannot carry both branches, that is an unresolved gate, not
permission to choose one."* And on out-of-lattice: *"no value is invented; the
payload records `OUT_OF_LATTICE` or noncomputable."*

I also note that my Q-521 cross-sector-unit obligation is now inside the operative
text (item 7: *"every required cross-sector-unit factorization … with no
conversion silently set to one"*) and armed in the failure ladder as *"undeclared
cross-sector conversion."* I record the carriage as verified; I do not claim
causation.

**Why NOT READY:** the instrument's pre-evaluation conditions name
`HOLDOUT-UNIVERSE-SEAL` and `PREDICTION-MAP-SEAL` without the parents the ruled
encoding requires — the same inheritance as G3.2. The text is otherwise ready;
this is a one-row repair, not a redraft.

---

## G5. FRESH ATTACK, SURFACE ANCHOR, VERB AUDIT

**Fresh attack** — delivered at N2: the tension board is heterogeneous, (M5a)
cannot close M9 (permanent), P3 or P4 (type/observable), and P4's missing domain
bridge is the J-II type-crossing under a new name. Ratifying the preparation and
completing (M5a) leaves three tensions standing, one of them forever.

**Surface anchor** — present and honest. §4's geometry/rails split, the failure
ladder's eighteen failure-capable items (including *"type erasure"*, *"undeclared
cross-sector conversion"*, and *"any attempted numerical execution before its
gate"*), and the closing discipline *"No item in (B2) is tested by a desired
numerical consequence."*

**Verb audit on my own board**

| My verb | Check |
|---|---|
| `MISSED_SOURCES = found` | The act is sealed, sidecar-matched, dated after the A32 ratification, uncited by the prep, and I verified its authoritative encoding myself rather than relying on its own summary. |
| `A32_PREP = DEFECTIVE` | Defective **as displayed** on the census count and the ladder's encoding basis. Its substantive conservatism — A32 not attained, no gate lifted, no number — is correct and undisturbed, and I say so. |
| `M5A = DEFECTIVE` | Defective by **inheritance**, in the conservative direction (under-demanding). Not a claim that anything unlawful was licensed. |
| `INSTRUMENT = NOT READY` | Not ready **pending one repair**. Its four carries, its refusals, and its provenance all pass; I did not let one inherited defect discount the rest. |
| Source 10 | Reported as **register advance, not a bad pin** — the corpus-audit trap runs in both directions and I declined the easy charge. |
| N2's "flattening" | Aimed at the **register summary**, not the prep, because I checked the prep's own words and the phrase is not there. |
| Agent reliance | 14 agents; the two refuters **split** on the missed source, so I adjudicated it myself from the sealed decision and the JSON encoding. No unverified agent claim is on this board. |

---

```text
A32_PREP = DEFECTIVE (+1 missed sealed principal act:
  PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29 70c4080e...,
  which rules stage_dependencies AUTHORITATIVE for graph structure and demotes the
  V011 prose DAG the prep's ladder is built on; census count is 16, not 15.
  +N1 source 10 is a live append-only register and cannot bear a file-hash pin;
  +N2 the tension board is heterogeneous and (M5a) closes neither M9 nor P3/P4)
MISSED_SOURCES = found (+1, admissible under the prep's own inclusion rule 1 and 3)
M5A = DEFECTIVE (+1 inherited: names HOLDOUT-UNIVERSE-SEAL and PREDICTION-MAP-SEAL
  without their ruled parents SPEC-SEAL and QSPEC-SPEC-SEAL, and omits the 11th
  node END-TO-END-RECONSTRUCTION-SEAL; the sequencing law itself is correctly
  binding and correctly anti-circular)
INSTRUMENT = NOT READY_FOR_RATIFICATION (+1, the same inheritance in the
  pre-evaluation conditions; all four required carries are INSIDE the operative
  text, attainment-by-preparation is refused by enumeration, and nothing is
  authored beyond the conjunction, which §3.1 books honestly)
VERB_AUDIT_SELF = CLEAN
```

The preparation is careful work that caught a real byte-version trap and drafted a
gate text I would otherwise call ready. It missed one sealed principal act, and
because that act is strictly stricter than what was consumed, the error runs in the
safe direction — but it lands in (M5a), the gate that licenses Step 2 and every
numerical execution after it. Repair the census row, redisplay the ladder against
the ruled encoding, and name the two parent seals inside the subgate; then this
instrument is ready.
