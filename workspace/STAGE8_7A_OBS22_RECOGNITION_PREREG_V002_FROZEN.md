# STAGE 8 / 7A HANDOFF — THE OBS-22 RECOGNITION PREREGISTRATION — **V002, FROZEN**

Lane: Dario (Claude Opus 5), cross-family reviewer
Task: PASTE 709 / 7A handoff — the junction-arc recognition spec, **frozen**
Base: `STAGE8_7A_OBS22_RECOGNITION_PREREG_DARIO_V001.md` = `c9c1f2dc00a70682bc526948e8624346f04164318a089b50f1e25dba14d5489d`,
carried by BYTE-COPY plus three asserted replacements (§D)
Ruling: `DECISION_F1_SPLIT_K2_SLOT_2026-08-08.md` = `e76746aeea351bf6a7e6bb97297ae21a9811ac7e05d0aebff31288102ca2d6a7`
Authority: principal directive `NOTE_7A_RECOGNITION_SPEC_REQUIREMENT_2026-08-08.md`,
**re-hashed at close** = `49aed793fb77247a3b38ec0b39822840b3ca06a6ae5dd48e876f0767a8689b7c`
(3,640 B). It was `6e144dcc…` (2,677 B) when I opened it: **ADDENDUM 2 and
REQUIREMENT 5 were appended mid-relay**, and §5A carries them.
**THIS ARTIFACT COMPUTES NOTHING AND EVALUATES NO MAP.**

```text
FROZEN = true
DELTAS = F1' + K-2 slot + freeze execution only
CRITERIA = 15 unchanged (13 grounded / 2 ungrounded, each named)
UNGROUNDED = 2 carried
VERDICTS = 3 closed + ledger channel (byte-faithful from V001)
CLASSICAL_TESTS = 0 (audited)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+items at §D.3)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**THIS ARTIFACT IS FROZEN AS OF ITS SEAL.** The principal's summary review is
complete and the freeze is approved (15 criteria, 3 verdicts + ledger, 2
UNGROUNDED items listed rather than manufactured). §5 is now executed rather than
proposed. From this seal, **any change to a criterion, test, evidence form,
guard, verdict definition, kill condition, or ledger schema is a REVISION OF
RECORD, surfaced to the principal before it takes effect.**

---

## 0. THE GOVERNING WORRY, AND WHY THE CORPUS ALREADY AGREES

The directive's worry is not whether the record face of gravity is at the
junction. It is that **the machinery will not recognize it** and the program will
loop expecting classical gravity at the record level.

The corpus has already ruled on the general form of that error, in a **principal
decision**, and the ruling names gravity as the case:

> `*** A RULE THAT HALTS ON THAT DIVERGENCE FORBIDS THE MEASUREMENT THE THEORY REQUIRES. ***`
> — `STAGE8_Q2STOP_DIVERGENCE_STOP_STRUCK_PRINCIPAL_DECISION_V001.md`
> `71439758769ff6f1b41b2ba2908e5144a560a014a98bb896d94cc9f01ecd3cdd` `[3220,3309)`

> "**Gravity is the existence proof.** A coupling arising from a divergence is not
> a pathology" — `STAGE8_T7_CL3_NONZERO_TYPING_PRINCIPAL_DECISION_V001.md`
> `c7686d57cfb567f54e57223e2fcfe174225db96baa7a014b2124a93334269009` `[2209,2301)`

So the design constraint is not novel and is not mine: **a criterion of the shape
"is it zero / is it finite / is it unique" applied to an object that may itself be
the coupling is the program's characteristic failure**, and the corpus struck one
rule for having it.

And the pre-metric footing is likewise sealed. **DoR-007**: *"smooth structure
must arise from a cellulation-independent refinement theorem; the adopted smooth
background is not a refinement input"* —
`STAGE8_TASK5_JREF_AND_LOCAL_KERNEL_ESTIMATES_LANE2_V001.md`
`8dd59b35bb9f63f8c8107d438c757c0cb9a110ee1078c173213c6da657bdfb24` `[5970,6118)`.
The smooth/metric face is a **derived** corollary; importing it is forbidden.
That is why no criterion below mentions one.

---

## 1. T1 — RECORD-NATIVE RECOGNITION CRITERIA

Every criterion names its **object**, its **test**, and its **evidence form**.
Every grounded criterion carries `source sha256 [start,end)`.

### 1.1 The corpus's own recognition bar, adopted verbatim

[PROVABLE] Before any criterion, the bar that decides whether *anything* has
landed:

> "A declaration or commuting square in abstract carriers is not a surface
> `PASS`. A `PASS` below requires the displayed map or equality on the named
> actual stage, cycle, arrow, or certified diamond. Where an actual manifest is
> absent, totality is not inferred."
> — `STAGE8_TASK5_JII_REALIZATION_LANE3_V001.md`
> `fdf20bd475b875ee000157d367869f4d7c31e18590b6eeb2ce1f60345c881e70` `[52660,52920)`

**A rail is not a member.** Every criterion below inherits this: a signature, a
declaration, or a diagram discharges nothing.

### 1.2 OBJECT A — the Ward-symbol map (J-II)

All spans in `fdf20bd475b875ee…` unless stated.

| # | Criterion | Test | Evidence form | Ground | Tag |
|---|---|---|---|---|---|
| **R1** | **The cell rule exists** | A member supplies the sealed prequotient rule `Phitilde_N(s)(delta_e) := incidence/integration/evaluation of s on the named k-cell e` (JD-3) and its linear extension (JD-3a) | the sealed rule itself, as bytes, plus one displayed evaluation on a **named** oriented k-cell | `[45349,45957)` | PROVABLE |
| **R2** | **Orientation covariance** | the rule's behaviour under reversal of the cell's orientation is proved, not asserted | proof object over the named cell and its reverse | `[45349,45957)` | PROVABLE |
| **R3** | **Presentation independence** | the rule's value does not depend on the presentation of `s` | proof object; a displayed pair of presentations with equal value | `[45349,45957)` | PROVABLE |
| **R4** | **Contact-kernel annihilation** | `Ctc_N^sym ⊆ ker(Phitilde_N)` — the two clauses that make `Phi_N` and `iota_N^H` presentation-independent quotient maps | proof object | `[45349,45957)` | PROVABLE |
| **R5** | **Continuity in member-named topologies** | the member provides continuous linear maps **in topologies the member names**: `Loc_N^phys`, `iotatilde_N^H`, `iota_N^H`, and the composite `Loc_N^C` (SPEC-7) | named topologies + continuity proof for each arrow | `[12334,12643)` | PROVABLE |
| **R6** | **Representation independence of the symbol map** | `sigma_2^ker(Sch_N(A)) := sigma_2^op(A)` is well defined — either via the required injectivity of `Sch_N`, or by the stated alternative discharge `Sch_N(A)=Sch_N(B) ⟹ sigma_2^op(A)=sigma_2^op(B)` (SPEC-5/6) | injectivity certificate, **or** the alternative implication proved | `[11817,12332)` | PROVABLE |
| **R7** | **Descent and confinement, as a proved factorization** | `[E_C,N,Delta_N]=0`; `Ctc_N^sym ⊆ ker(iotatilde_N^H)`; and the confinement identity holds **universally over `[s]`** as a declared and proved factorization (SPEC-9) | proof object quantified over `[s]`; **not** an evaluation on any distinguished object | `[12801,13353)` | PROVABLE |
| **R8** | **The symbol-side action is the fixed formula** | `D_N^Loc ⊆ Sch_N(Op_N^(loc,2))` and `Loc_N^phys(K) := [sigma_2^ker(K)]_(Ctc_N^sym)` (SPEC-8) | the eligibility inclusion and the formula, discharged **without** admitting a classical-operator-class resemblance as the discharge (see G-3) | `[12645,12799)` | PART-PROVABLE |
| **R9** | **Naturality is closure-wide, not prototype-only** | naturality is established across the generated certified family, not on the three executed prototypes | the closure induction over the generating schemas | `[55893,55989)` | PROVABLE |

**R7 and the struck clause.** SPEC-9's passage also records that *neither*
`P_H,N Loc_N^C(kappa_T,N) != 0` *nor its negation* is a membership clause, and
that the struck range clause is **not** restored. That refusal is inside the
cited span and is carried whole. It is the corpus applying the anti-scar rule to
this very object, before OBS-22 existed.

### 1.3 OBJECT B — the length normalization

Spans in `STAGE8_CROSS_SECTOR_METRIC_RULE_ADMISSIBILITY_SPEC_V001.md`
= `3c008ecccc2b01ac72c8583e0fdea6601a12db7e2755edaa25bd8174f314525a`, and in
`STAGE8_TASK6_JII_BETA_IDENTIFICATION_DARIO_V001.md`
= `8e31df94fd2076cdb7803b0c516457fee577538f290f2ace3679cf1f4cfa4a76`.

| # | Criterion | Test | Evidence form | Ground | Tag |
|---|---|---|---|---|---|
| **R10** | **Typed same-cell inputs on both sides** | the object's declared domain and codomain are inhabited **on one and the same record cell** — internal/projective geometry in, dimensional length normalization out, dimensionless output | the two typed inputs, named to the same cell | `8e31df94…[5064,5266)` | PROVABLE |
| **R11** | **Target-blind output** | the output is produced without reference to any later use of it | the derivation, with the target-blindness clause discharged | `3c008ecc…[11554,11624)` | PROVABLE |
| **R12** | **Overdetermination** | two **independent** requirements, with exactly one common positive output — not one permission (F3) | both requirements, and the intersection argument | `3c008ecc…[10785,10811)` | PROVABLE |
| **R13** | **No dimensional analogy** | the relation is derived same-cell, not obtained by matching dimensions to a record interval, Planck length, horizon scale, or endpoint length (F2) | the derivation, plus an explicit statement that no dimensional match was used | `3c008ecc…[10585,10608)` | PROVABLE |
| **R14** | **No value-shaped selection** | the candidate is not chosen because its later output is favourable, simple, or close to a known number (F5) | the selection record, plus the anti-tuning ledger | `3c008ecc…[11063,11082)` | PROVABLE |

**R10–R14 are properties of the normalization object.** None compares its output
to a measured value; F5 forbids exactly that, and F2 forbids the dimensional
shortcut that would smuggle one in.

### 1.4 The two UNGROUNDED criteria, named with what is missing

| # | Criterion a record-native reader wants | Why UNGROUNDED — what is missing |
|---|---|---|
| **U1** | **Joint landing** — the Ward-symbol map and the length normalization land *compatibly*, not merely each on its own | No sealed statement says what joint landing means. My own sealed determination types the two objects **OVERLAPPING** and states the sharp consequence: *"a spacetime length normalization is not progress on `(JD-3)`"* (`8e31df94…[12199,12257)`). So the corpus knows they are neither identical nor independent — and nowhere states the compatibility condition. **Missing carrier: a sealed statement of the shared-core obligation both objects must jointly discharge.** |
| **U2** | **Sufficiency** — that R1–R14 *exhaust* "the maps land geometric" | Each criterion above is grounded as **necessary**. No sealed text states that any list is **sufficient**. I can ground every member and cannot ground the set. **Missing carrier: a sealed closure statement over recognition criteria.** Until one exists, a full sweep of R1–R14 licenses `CONFIRMED` **for the criteria as stated** and nothing more — which is precisely what verdict-3's name says. |

**I do not manufacture grounding for either.** Listing them is the point: a
preregistration that hid its own incompleteness would be the failure it exists to
prevent.

---

## 2. THE ANTI-SCAR GUARDS

These are **rules on the criteria**, not criteria. They exist because four of the
criteria above carry the scar shape, and one inherited falsifier would false-kill
the program's central result.

### 2.1 [PROVABLE] G-1 — no criterion may be a vanishing, finiteness, or uniqueness test on an evaluated distinguished object

Warrant: the principal decision at §0, and the corpus's own two flags —

> "`THE LOGARITHMIC DIVERGENCES … ARE SUMS OVER k = LATTICE DISTANCE BETWEEN CELLS
> … THEY ARE NOT EVIDENCE ABOUT G_hs AT ALL.` … `Anyone assembling the shell counts
> into a forcing argument would be committing the program's characteristic error
> on the separation-versus-coincidence axis. Flagged so no one does.`"
> — `STAGE8_IS_RL2B_FAILURE_FORCED_BY_F5_DETERMINATION_V001.md`
> `83750234b1fc072e915580c230bad796ca5d66df2332795356713062786fb242` `[9736,10636)`

> "`The phrase "the log divergence is the coupling" is not an executable scalar
> action rule in the current corpus.`"
> — `STAGE8_TASK4A_DIVERGENCE_DETERMINED_TRANSVERSE_CYCLE_ACTION_DRAFT_DETERMINATION_V001.md`
> `ed49624b6f5f0bcda94ee88a939a5751113b30d73192b2c28a5aec25829e1797` `[10147,10553)`

The second matters as much as the first: the scar cuts **both** ways. "It is the
coupling" is not a licence either. G-1 forbids the test, not the observation.

### 2.2 [YOURS] G-2 — R5's topology is member-named, never pre-fixed

A logarithmic divergence **is** a boundedness failure in a naively chosen
topology. If OBS-22 fixes a topology and then tests boundedness, it reproduces
the scar exactly. The phrase *"in named topologies"* is load-bearing and is
carried into R5 verbatim.

### 2.3 [YOURS] G-3 — R8's eligibility may not be discharged by classical resemblance

`D_N^Loc ⊆ Sch_N(Op_N^(loc,2))` is naturally discharged by certificates of
classical pseudodifferential calculus — proper support, wavefront, order,
principal symbol. Those are criteria of **resemblance to a classical operator
class**, and order counting is exactly what produces a logarithm at the marginal
case. R8 is therefore tagged PART-PROVABLE: the inclusion is checkable, but a
failure of it may **not** be reported as a recognition failure without G-1
review.

### 2.4 **G-4 — F1 IS SPLIT; F1' GOVERNS THE JUNCTION ARC**

[PROVABLE] The V001 finding — that the inherited falsifier F1 would false-kill a
running normalization — was accepted. **The principal ruled the split before any
junction map is computed** (`e76746ae…`, Ruling 1). The original F1 remains
sealed and of record, **superseded by split**; F1' is authored here and governs.

**The two, side by side:**

| | **F1 — sealed, superseded of record** | **F1' — successor, governs the junction arc** |
|---|---|---|
| Text | "after applying the candidate, beta remains a positive continuous family" | a surviving positive continuous family is **typed before it is judged** |
| Weak-rule reading | fires as failure | **fires as failure, exactly as F1 did** — if the family exists because the rule underdetermines beta, that is a real defect and F1' kills it |
| Scale-dependence reading | fires as failure — **the defect** | **routes to MEASUREMENT** under §5A's preregistered kill conditions K-1 (coefficient class) and K-3 (locus) |
| How the coupling reading can lose | it cannot lose *and* cannot win — family-hood alone decides | **it can still lose — by K-1 or K-3, never by mere family-hood** |
| Status | sealed at `3c008ecc… [10484,10508)`; not re-worded, not deleted | authored into this frozen preregistration |

**F1' does not weaken F1; it types F1's input.** Family-hood stops being a
verdict and becomes a question with two answers, one of which still kills. The
half that made the original dangerous — a "must be a unique number" test on
something that may be the running conversion itself — is the only half that
moved, and what it moved to is a measurement with a pre-stated way to lose.

**Superseded, not silenced.** The original F1 is not re-worded in its own sealed
file; this artifact records the supersession. That is the same discipline the
V001 draft applied when it flagged F1 and refused to edit it.

The finding that produced the split, retained verbatim from V001:

```text
F1 beta_family_survives:
  after applying the candidate, beta remains a positive continuous family.
                       -- 3c008ecc… [10484,10508)
```

F1 fires as **failure**. But a *running* normalization — one carrying genuine
scale dependence — **is** a positive continuous family. F1 therefore cannot
distinguish

```text
(i)  beta is a family because the rule is too weak       -> a real defect
(ii) beta is a family because the object carries scale   -> possibly THE RESULT
```

That is the log-divergence scar, aimed at the length normalization: a
"must be a unique number" test applied to something that may be the running
conversion itself. Under the principal decision at §0, a rule that halts there
forbids the measurement the theory requires.

**Disposition — RULED AND EXECUTED.** V001 proposed the split and refused to make
it; the principal made it. F1' above is the ruling authored, not my proposal
promoted. One difference from the V001 proposal is worth recording: V001 routed
the scale-dependence reading to `NOT-RECOGNIZABLE-AS-STATED`; **the ruling routes
it to MEASUREMENT under K-1/K-3 instead**, which is stronger — a third-verdict
routing would have parked the reading, whereas measurement under a preregistered
kill condition can still lose. The ruling's route is the one authored.

### 2.5 [PROVABLE] G-5 — the homonym trap, both directions

`R_C,N`, the "metric Riesz isomorphism" from DoR-019, is an inner product on the
**finite cochain carrier** `C_N^k`. It is not a spacetime metric: no distance, no
dimensionful constant, no measured value. **A contamination filter that rejected
a criterion for containing the word "metric" would itself be a false kill.** The
audit direction matters too: `iota_N^H := R_C,N^(-1) Phi_N` must not be read as
though Riesz were the content — the content is `Phi_N`, and the corpus states
flatly that *"The metric and finite shadow do not create that rule"*
(`fdf20bd4…[57642,57695)`).

---

## 3. T2 — THE THREE VERDICTS, CLOSED

```json
{
  "schema": "obs22.recognition-verdict.v001",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema", "criterion_id", "object", "verdict", "evidence",
               "missing_carrier"],
  "properties": {
    "schema":       {"const": "obs22.recognition-verdict.v001"},
    "criterion_id": {"pattern": "^(R([1-9]|1[0-4])|U[12])$"},
    "object":       {"enum": ["WARD_SYMBOL_MAP_JII", "LENGTH_NORMALIZATION"]},
    "verdict":      {"enum": ["CONFIRMED",
                              "INERT",
                              "NOT_RECOGNIZABLE_AS_STATED"]},
    "evidence":     {"type": "array", "items": {"type": "object"}},
    "missing_carrier": {"type": ["string", "null"], "minLength": 1}
  },
  "allOf": [
    {"if":   {"properties": {"verdict": {"const": "NOT_RECOGNIZABLE_AS_STATED"}}},
     "then": {"properties": {"missing_carrier": {"type": "string"}},
              "required": ["missing_carrier"]}},
    {"if":   {"properties": {"verdict": {"enum": ["CONFIRMED", "INERT"]}}},
     "then": {"properties": {"missing_carrier": {"const": null}}}}
  ]
}
```

```text
CONFIRMED                   the criterion applied, and the object satisfied it.
INERT                       the criterion applied, and the object did not.
                            A real negative about the object.
NOT_RECOGNIZABLE_AS_STATED  THE CRITERION COULD NOT SEE THIS OBJECT.
                            Not a fact about the object at all. The named
                            missing carrier is REQUIRED and is the whole content.
```

**The third never collapses into the second.** The schema enforces it: a
`NOT_RECOGNIZABLE_AS_STATED` row without a `missing_carrier` is invalid, and a
`CONFIRMED`/`INERT` row that carries one is invalid.

### 3.1 [PROVABLE] The three-outcome discipline is already sealed in this corpus

Not an import from my build lane. The J-II realization already carries it, on
this very family:

> "A8 is `UNEXECUTABLE/PENDING`: it is **neither passed, failed, nor vacuously
> true**." — `fdf20bd475b875ee…` `[58574,58653)`

and, in the same section, the corpus's own refusal of the classical-shaped test:

> "Both sides move together, so `(R9-V002)` does not force a zero period."
> — `fdf20bd475b875ee…` `[58357,58427)`

And a `NOT_RECOGNIZABLE_AS_STATED` instance with its carrier named, already of
record:

> "The failure is not a fence. It is the exact DoR-007 boundary: the record
> surface has not supplied the geometric refinement and uniform-locality data
> from which the physical limit is required to be derived."
> — `8dd59b35bb9f63f8…` `[2471,2677)`

The two-outcome alternative is what produced the scar. Three outcomes convert a
typing gap into **a named criterion revision** instead of a false kill or a loop.

---

## 4. T3 — THE CORRESPONDENCE LEDGER CHANNEL

```json
{
  "schema": "obs22.correspondence-observation.v001",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema", "observation_id", "record_object", "familiar_structure",
               "likeness", "observed_by", "verdict_weight", "feeds"],
  "properties": {
    "schema":            {"const": "obs22.correspondence-observation.v001"},
    "observation_id":    {"pattern": "^CORR-[0-9]{4}$"},
    "record_object":     {"type": "string", "minLength": 1},
    "familiar_structure":{"type": "string", "minLength": 1},
    "likeness":          {"type": "string", "minLength": 1},
    "observed_by":       {"type": "string", "minLength": 1},
    "verdict_weight":    {"const": 0},
    "feeds":             {"const": ["DISCOVERIES_DIGEST"]}
  }
}
```

**Four properties, and each is a prohibition:**

1. `verdict_weight` is `const 0`. A correspondence can never tighten or loosen a
   verdict. It cannot be cited in an `evidence` array — the two schemas share no
   field by which one could enter the other.
2. `feeds` is `const ["DISCOVERIES_DIGEST"]`. One destination, examined **after**
   the record-native results are sealed.
3. Logging is **free and immediate**. There is no admission test, because an
   admission test would make correspondences into criteria by the back door.
4. A correspondence is never grounds for adding, removing, or re-wording a
   criterion. That route is §5's revision of record, and it goes to the
   principal.

[YOURS] **Why the channel is generous and the criteria are not.** The scar is not
that the old friend was absent — under Susskind–Uglum and Sakharov the friend was
*present*, and the classically-shaped test mistyped it. The ledger lets the
program say "that looks like the running coupling" out loud, immediately, without
that observation touching a verdict. Suppressing the observation and admitting it
as evidence are both errors; this channel is how the program does neither.

---

## 5A. REQUIREMENT 5 — DIVERGENCE TYPING, AND A PRE-STATED WAY TO LOSE

[PROVABLE] **This requirement was appended to the directive while the V001 draft
was being written.** I re-hashed the note at close, found it grown from 2,677 to
3,640 bytes, and read the addition rather than sealing against the version I
started from. `REQUIREMENT 5` occupies `49aed793…[2822,3640)`.

Its two halves are equally binding, and the second is the one a lane in my
position would be tempted to skip:

```text
MEASURE, DON'T HALT
  the corpus types a nonzero divergence as failure; the junction arc MUST NOT
  inherit that typing. A divergence encountered at the junction is MEASURED AND
  RECORDED -- its coefficient, dependence, and locus are data -- never halted on.

AND A PRE-STATED WAY TO LOSE
  because "the divergence is the signal" is ALSO THE FITTER'S MOVE, the typing
  rule carries its KILL CONDITION PREREGISTERED: the measured structure that
  would count AGAINST the coupling reading is stated BEFORE any map is computed.
```

G-1 already forbade halting. **It did not supply the kill condition**, and
without one "measure, don't halt" is unfalsifiable — every divergence becomes
evidence for the reading. The directive names the three axes; the corpus grounds
two of them, on a logarithm it has already mistyped once.

### 5A.1 The preregistered kill condition — three axes

Ground: `STAGE8_IS_RL2B_FAILURE_FORCED_BY_F5_DETERMINATION_V001.md`
= `83750234b1fc072e915580c230bad796ca5d66df2332795356713062786fb242` `[9736,10636)`,
where the corpus separates a logarithm that IS evidence from one that is not.

| Axis | What is recorded | What counts **AGAINST** the coupling reading | Grounded |
|---|---|---|---|
| **K-1 coefficient class** | the divergence's coefficient, as an exact object, with the class it belongs to | the coefficient falls in a class the sealed corpus has already assigned to a **different** mechanism — the RL2B passage distinguishes `24 H_K + 2 zeta(3)` / `64 H_K + 16 zeta(3)` from the `n=1` line's `2/pi` at the coincidence end | PROVABLE `[9736,10636)` |
| **K-2 dependence** — **NAMED-OPEN SLOT, NOT IN THE FROZEN KILL SET** | which variable the divergence runs in, displayed. **The datum is still recorded**; what is absent is the rule that judges it | *undetermined* — no sealed statement fixes the admissible dependence class, and writing one here would be the fitting REQUIREMENT 5 exists to stop | **OPEN** — fillable only by a sealed grounding, entering as a surfaced revision of record (`e76746ae…`, Ruling 2) |
| **K-3 locus** | where the divergence lives: which cells, and whether at coincidence or across separation | it lives at **cross-cell separation** when the object under test is the per-cell coincidence object, or the reverse — the corpus flags exactly this: *"CROSS-CELL SEPARATION, not the per-cell coincidence object. THEY ARE NOT EVIDENCE ABOUT G_hs AT ALL"* | PROVABLE `[9736,10636)` |

**THE KILL SET FREEZES AS {K-1, K-3}.** If either fires, the coupling reading
LOSES on that divergence. Not `INERT` and not `NOT-RECOGNIZABLE` — those are
verdicts about criteria seeing objects. This is a verdict about a *reading of
data*, and it is recorded in the correspondence ledger's sibling column with the
same zero verdict weight, then surfaced.

**K-2 is a NAMED-OPEN SLOT** (`e76746ae…`, Ruling 2). The directive names
dependence as an axis; no sealed statement fixes the admissible dependence class,
and guessing one would be the fitting REQUIREMENT 5 exists to stop. So the slot
is named, left empty, and frozen empty:

```text
K-2  status        NAMED-OPEN SLOT
     in kill set   NO -- the frozen kill set is exactly {K-1, K-3}
     recorded      YES -- the dependence datum is measured and recorded regardless
     fillable by   a SEALED statement grounding the admissible dependence class
     entering as   a SURFACED REVISION OF RECORD against this frozen digest
```

**An empty slot is not a silent omission.** K-2 is written into the frozen
artifact precisely so that its absence is visible at every future reading, and so
that filling it must pass through the revision route rather than appear as though
it had been there all along.

### 5A.2 [YOURS] Why this is the hardest requirement in the directive

G-1 and REQUIREMENT 5 point in opposite directions on purpose. G-1 stops the
program killing its central result with a classically-shaped test. K-1..K-3 stop
the program *saving* that result by reading every divergence as the coupling. The
corpus already carries both halves — the principal decision that halting forbids
the measurement, and the flat statement that *"the phrase 'the log divergence is
the coupling' is not an executable scalar action rule in the current corpus"*
(`ed49624b…[10147,10553)`).

A preregistration with only the first half is not neutral machinery. It is a
machine that cannot lose.

## 5. T4 — THE FREEZE CONDITION

```text
WHAT IS FROZEN  -- executed at this artifact's seal
  §1 R1-R14 and U1-U2, with their tests, evidence forms and grounds
  §2 G-1 .. G-5, with F1' authored at G-4
  §3 the three verdicts and the verdict schema
  §4 the correspondence schema
  §5A REQUIREMENT 5: measure-don't-halt AND the kill set {K-1, K-3},
     with K-2 frozen as a NAMED-OPEN SLOT

WHEN  -- DONE
  the principal's summary review is complete and the freeze is approved; this
  seal executes it, and it precedes any junction map being computed or evaluated.
  The criteria are sealed against a computation that has not happened.

HOW SEALED
  this artifact is sealed by sha256 with a sidecar, and its digest is carried in
  the 7A handoff package.

AFTER THE FREEZE
  any change to a criterion, a test, an evidence form, a guard, a verdict
  definition, or the ledger schema is a REVISION OF RECORD:
    - it is written as a delta against the frozen digest;
    - it states which criterion changed and why;
    - it states what was already observed at the time of the change;
    - it is SURFACED TO THE PRINCIPAL before it takes effect.
  A criterion revised after seeing results, without that surfacing, is
  indistinguishable from tuning.
```

[PROVABLE] The freeze convention is the corpus's own, adopted verbatim in form:

> "These falsifiers are written before any candidate is evaluated. They are not a
> derivation and they authorize no computation."
> — `3c008ecccc2b01ac…` `[11398,11461)`

**What the freeze does not do.** It does not make the criteria sufficient (U2);
it does not authorize any computation; and it does not convert
`NOT-RECOGNIZABLE-AS-STATED` into a failure. A frozen criterion that cannot see
its object is a criterion due for revision — that is the third verdict's whole
purpose, and the revision route above is how it gets one.

---

## 6. THE CLASSICAL-TESTS AUDIT, AND ONE PRECEDENT I COULD NOT GROUND

### 6.1 [PROVABLE] `CLASSICAL_TESTS = 0`

Audited criterion by criterion against the directive's forbidden list:

```text
"metric-like"                         0 criteria
"reproduces Newton" / Newtonian limit 0 criteria
comparison to classical gravity's numerical signatures   0 criteria
comparison to classical gravity's structural signatures  0 criteria
comparison to any measured constant   0 criteria   (R14/F5 forbids it explicitly)
appeal to a spacetime metric          0 criteria   (DoR-007 forbids the import;
                                                    G-5 records the homonym)
```

Three near-misses, each disposed rather than hidden:

- **R8** could be discharged by classical-operator-class resemblance. Tagged
  PART-PROVABLE and fenced by G-3.
- **R5** could become a boundedness test in a pre-fixed topology. Fenced by G-2.
- **F1**, inherited, is a uniqueness test on a possibly-running object. Fenced by
  G-4 and routed to the principal.

The count is 0 because those three are fenced, not because they were absent.

### 6.2 [YOURS] The singlet-ratio precedent — **NOT LOCATED**

The directive cites *"the singlet-ratio hunt (a classically-shaped expectation,
proven empty)"* as a precedent. **I could not find it in the sealed corpus**, and
I searched: `singlet ratio`, `singlet-ratio`, `ratio of singlets`,
`singlet sector ratio`, `ratio hunt`, `proven empty`, `empty on the carrier`.
`singlet` alone appears in 56 files, none in a ratio-hunt sense.

Nearest sealed relatives, offered as candidates and **not** adopted as the
precedent:

- `STAGE8_RECORD_SIDE_DIMENSIONLESS_RATIO_SELECTOR_CONSTRUCTION_EINSTEIN_V001.md`
  `c363c7876dd5a405db647d71bb7d68169670db79518c5c9effb0e8ce0ff94abc` — a
  dimensionless **ratio selector**, whose bar is "a REQUIRE whose output is a
  singleton and whose existence and uniqueness are both derived".
- My own J-II member hunt, swept by content and returning `MEMBER_FOUND = none` —
  a genuinely proven-empty hunt, but for a *member*, not a ratio.

The three-verdict design does not depend on this precedent: it is grounded twice
over in §0 and §3.1. I record the gap so the principal can supply the citation or
correct the reference — **not** so a substitute can be quietly adopted.

---

## 7. SELF VERB AUDIT

| My verb | Check |
|---|---|
| Directive verified before use | `6e144dcc…` hashed from bytes, not transcribed. |
| Every criterion grounded or declared ungrounded | 13 with `source sha256 [start,end)`; 2 named UNGROUNDED with the missing carrier stated. |
| Every span verified by me | Recomputed from the source bytes; a parallel survey supplied candidates and **none entered without my own byte check**. |
| **A finding against a sealed falsifier** | G-4: F1 would false-kill a running normalization. Raised, not quietly re-worded — a sealed falsifier is not mine to edit. |
| The scar cuts both ways | G-1 forbids the halting test **and** records that "the log divergence is the coupling" is not an executable rule either. Neither direction is a licence. |
| **The contamination filter audited too** | G-5: rejecting `R_C,N` for containing "metric" would itself be a false kill. A filter that only looks for contamination will find it where it is not. |
| Sufficiency not claimed | U2 says plainly that I can ground each criterion as necessary and no sealed text makes any list sufficient. |
| Precedent gap disclosed | §6.2: the singlet-ratio hunt is not locatable; the searches are listed and no substitute is adopted. |
| Nothing computed | No map evaluated, no junction object formed, no numeric produced. |

---

## D. THE V001 -> V002 DELTA NOTE

[PROVABLE] **Method: byte-copy plus asserted surgical replacement.** V002 was
produced by copying `STAGE8_7A_OBS22_RECOGNITION_PREREG_DARIO_V001.md`
= `c9c1f2dc00a70682bc526948e8624346f04164318a089b50f1e25dba14d5489d` byte for
byte, then applying **fourteen** named string replacements, each asserted to match
**exactly once** before it was applied. "Nothing else moves" is therefore true by
construction rather than by claim — the standard this lane has held Builder A to
for twenty relays, applied to itself.

### D.1 The three authorized deltas, and the fourteen replacements that carry them

Every replacement is listed; none is summarized into a group count.

```text
D1  F1'  AUTHORED PER RULING 1                                        2 replacements
      D1.1  §2.4 heading and lead -> F1 / F1' side-by-side table
      D1.2  §2.4 "Proposed disposition" -> "Disposition -- RULED AND EXECUTED"

D2  K-2  NAMED-OPEN SLOT PER RULING 2                                 2 replacements
      D2.1  §5A.1 the K-2 table row -> NAMED-OPEN SLOT, not in the kill set
      D2.2  §5A.1 the kill-set paragraph -> kill set freezes as {K-1, K-3},
            with the slot's five-field status block

D3  FREEZE  EXECUTED PER RULING 3                                    10 replacements
      D3.1   title: DRAFT FOR PRINCIPAL REVIEW -> V002, FROZEN
      D3.2   task/authority header: base digest, ruling digest, carriage method
      D3.3   status paragraph: "This is a draft. It seals nothing." -> FROZEN
      D3.4   §5 WHAT FREEZES / WHEN -> WHAT IS FROZEN / WHEN -- DONE
      D3.5   header summary block -> the V002 status block
      D3.6   closing tail paragraph -> F1 split recorded as executed
      D3.7   §5A "this draft" -> "the V001 draft"
      D3.8   final CHAIN_INVOKED line -> no longer a draft; this seal executes
      D3.9   verb-audit K-2 sentence -> the ruled named-open-slot disposition
      D3.10  insertion point for §D and the V002 final lines
                                                                 TOTAL  14
```

[YOURS] **The count was wrong in my first pass and I caught it in my own pin
check.** I wrote "nine" while making fourteen — the exact defect class this lane
charged Builder A with at relay 683 (58 declared, 63 true) and 695 (160/26
declared, 155/21 true). The cure is the one I demanded there: enumerate every
item rather than summarizing groups, so the total cannot drift from the list.

### D.2 What did NOT move — asserted, not assumed

```text
§1.1  the corpus's PASS bar                      byte-identical
§1.2  R1-R9,  the Ward-symbol map criteria       byte-identical
§1.3  R10-R14, the length-normalization criteria byte-identical
§1.4  U1 and U2, the two UNGROUNDED items        byte-identical
§2.1  G-1   §2.2 G-2   §2.3 G-3   §2.5 G-5       byte-identical
§3    the three verdicts and the verdict schema  byte-identical
§4    the correspondence ledger schema           byte-identical
§5A.1 K-1 and K-3 rows                           byte-identical
§6    the classical-tests audit and §6.2         byte-identical
every citation, digest and byte span carried     byte-identical
```

**G-4 is the one guard that moved**, and it moved only because F1' is authored
there; that change is D1 and is authorized by Ruling 1. Every other guard is
untouched.

### D.3 [YOURS] Two things I did not do

**I did not re-word the sealed F1.** Ruling 1 says the original "remains sealed
and of record"; `3c008ecc… [10484,10508)` is unchanged on disk and this artifact
records the supersession rather than performing it in someone else's file. That
is the same refusal V001 made when it flagged F1 and declined to edit it.

**I did not fill K-2.** The slot is frozen empty with its name on it. Filling it
would have been the fitting REQUIREMENT 5 exists to stop, and Ruling 2 reserves
it for a sealed grounding arriving as a surfaced revision.

One correction of record, carried at §2.4: **the ruling's routing is stronger
than the one V001 proposed.** V001 would have sent the scale-dependence reading
to `NOT-RECOGNIZABLE-AS-STATED`, which parks it. The ruling sends it to
measurement under K-1/K-3, which can still lose. The authored F1' follows the
ruling, not my draft.

---

```text
FROZEN = true (this artifact is the frozen OBS-22 recognition preregistration.
  The principal's summary review is complete and the freeze approved; this seal
  executes it, and it precedes any junction map being computed. From this seal any
  change to a criterion, test, evidence form, guard, verdict definition, kill
  condition or ledger schema is a REVISION OF RECORD, written as a delta against
  this digest and SURFACED TO THE PRINCIPAL before it takes effect.)
DELTAS = F1' + K-2 slot + freeze execution only (byte-copy of V001 c9c1f2dc… plus
  FOURTEEN named string replacements -- 2 + 2 + 10, every one enumerated at §D.1 --
  each asserted to match EXACTLY ONCE before application, grouped into exactly the
  three authorized deltas -- D1 authors F1'
  per Ruling 1, D2 writes K-2 as the named-open slot per Ruling 2, D3 executes the
  freeze per Ruling 3. "Nothing else moves" holds BY CONSTRUCTION, not by claim.
  F1' displayed side by side with F1: the weak-rule reading STILL KILLS exactly as
  F1 did; the scale-dependence reading ROUTES TO MEASUREMENT under K-1/K-3 and can
  still lose there, never by mere family-hood. The original F1 is not re-worded in
  its own sealed file -- it stays sealed at 3c008ecc… [10484,10508), superseded of
  record. The kill set freezes as {K-1, K-3}; K-2 is frozen EMPTY WITH ITS NAME ON
  IT so its absence is visible at every future reading and filling it must pass
  through the revision route.)
CRITERIA = 15 unchanged (R1-R14 and U1-U2 carried BYTE-IDENTICALLY from V001, with
  their objects, tests, evidence forms, tags and byte-span grounds; the guards G-1,
  G-2, G-3 and G-5 likewise byte-identical, G-4 being the single guard that moved
  and only because F1' is authored there under Ruling 1.)
UNGROUNDED = 2 carried (U1 JOINT LANDING and U2 SUFFICIENCY, byte-identical, still
  declared rather than manufactured. The freeze does not ground them and does not
  pretend to: U2 in particular still says that every criterion is grounded as
  NECESSARY and that no sealed text makes any list SUFFICIENT, so a full sweep
  licenses CONFIRMED for the criteria as stated and nothing more.)
CHAIN_INVOKED = false (no junction map was computed or evaluated in this relay, no
  junction object formed, no numeric produced, no member bound, no fixed point, no
  end test, no comparison to any measured constant.)
VERB_AUDIT_SELF = CLEAN (+1 MISCOUNT IN MY OWN DELTA CERTIFICATE, caught by my own
  pin check before sealing: I wrote NINE replacements and had made FOURTEEN -- the
  exact defect class this lane charged Builder A with at 683 and 695, now enumerated
  item by item at §D.1 so the total cannot drift from the list. +3 items at §D.3 and the carried V001 audit below: I did
  NOT re-word the sealed F1, because Ruling 1 keeps it of record and editing another
  file's sealed text is not mine to do; I did NOT fill K-2, because that is the
  fitting REQUIREMENT 5 exists to stop; and I recorded that THE RULING'S ROUTING IS
  STRONGER THAN MY OWN V001 PROPOSAL -- V001 would have parked the scale-dependence
  reading at NOT-RECOGNIZABLE-AS-STATED, the ruling sends it to measurement where it
  can still lose, and the authored F1' follows the ruling rather than my draft.)
```

---

## D.4 THE V001 AUDIT, CARRIED VERBATIM

The V001 findings below are carried unchanged; they are the record of how the
frozen criteria were arrived at.

```text
CRITERIA = 15 record-native (13 grounded / 2 ungrounded, each named:
  GROUNDED -- R1 the cell rule exists (JD-3/JD-3a), R2 orientation covariance,
  R3 presentation independence, R4 contact-kernel annihilation, R5 continuity in
  MEMBER-NAMED topologies, R6 representation independence of the symbol map,
  R7 descent and confinement as a PROVED FACTORIZATION rather than an evaluation,
  R8 the fixed symbol-side action, R9 closure-wide naturality -- all nine on the
  Ward-symbol map J-II; and R10 typed same-cell inputs, R11 target-blind output,
  R12 overdetermination by two independent requirements, R13 no dimensional
  analogy, R14 no value-shaped selection -- five on the length normalization.
  Each carries its object, its test, its evidence form, and a source sha256 with
  a byte span, every span recomputed by me from the source bytes.
  UNGROUNDED -- U1 JOINT LANDING: no sealed statement says what it means for both
  junction objects to land compatibly, though the corpus types them OVERLAPPING
  and states that a spacetime length normalization is not progress on (JD-3);
  missing carrier is a sealed shared-core obligation. U2 SUFFICIENCY: every
  criterion is grounded as NECESSARY and no sealed text makes any list
  SUFFICIENT, so a full sweep licenses CONFIRMED for the criteria as stated and
  nothing more; missing carrier is a sealed closure statement over recognition
  criteria. Both are declared rather than manufactured.)
VERDICTS = 3 closed + ledger channel (CONFIRMED / INERT /
  NOT_RECOGNIZABLE_AS_STATED under obs22.recognition-verdict.v001, an
  additionalProperties:false schema whose conditional clauses make the third
  verdict REQUIRE a nonempty missing_carrier and forbid the other two from
  carrying one -- so the third can never collapse into the second by omission.
  The discipline is not imported from the build lane: this corpus already carries
  it on this very family, where A8 is "neither passed, failed, nor vacuously
  true", where the same section refuses to let (R9-V002) force a zero period, and
  where a DoR-007 boundary is recorded as "not a fence" with its missing carrier
  named. FOURTH CHANNEL: obs22.correspondence-observation.v001, verdict_weight
  const 0 and feeds const [DISCOVERIES_DIGEST], sharing no field with the verdict
  schema by which a correspondence could enter evidence; logging is free and
  immediate because the scar was never that the old friend was absent -- under
  Susskind-Uglum and Sakharov the friend was PRESENT and the classically-shaped
  test mistyped it.)
FREEZE = stated (criteria, guards, verdicts, the ledger schema AND REQUIREMENT 5's
  divergence typing with its K-1..K-3 kill condition seal on the
  principal's approval and BEFORE any junction map is computed; the successor is
  sealed by sha256 with a sidecar and carried in the 7A handoff package. After the
  freeze, any change to a criterion, test, evidence form, guard, verdict or schema
  is a REVISION OF RECORD written as a delta against the frozen digest, stating
  what changed, why, and what had already been observed, and SURFACED TO THE
  PRINCIPAL before taking effect -- because a criterion revised after seeing
  results, without surfacing, is indistinguishable from tuning. The convention is
  the corpus's own: "These falsifiers are written before any candidate is
  evaluated. They are not a derivation and they authorize no computation." The
  freeze does NOT make the criteria sufficient, does NOT authorize computation,
  and does NOT convert NOT-RECOGNIZABLE-AS-STATED into a failure.)
CLASSICAL_TESTS = 0 (audited) (zero criteria invoke "metric-like", a Newtonian
  limit, any numerical or structural signature of classical gravity, or any
  measured constant -- R14/F5 forbids the last explicitly and DoR-007 forbids
  importing smooth structure at all. THE COUNT IS 0 BECAUSE THREE NEAR-MISSES ARE
  FENCED, NOT BECAUSE THEY WERE ABSENT: R8's eligibility could be discharged by
  classical pseudodifferential resemblance (G-3, and R8 is tagged PART-PROVABLE);
  R5 becomes a boundedness test if the topology is pre-fixed rather than
  member-named, and a logarithm IS a boundedness failure in a naive topology
  (G-2); and the INHERITED falsifier F1 "beta remains a positive continuous
  family" cannot distinguish an underdetermined beta from an object that genuinely
  carries scale dependence, because A RUNNING NORMALIZATION IS A POSITIVE
  CONTINUOUS FAMILY -- the log-divergence scar aimed straight at the central
  result (G-4). I flag F1 and route the split to the principal; a sealed falsifier
  is not mine to re-word. G-5 audits the filter itself: R_C,N is a Riesz inner
  product on the finite cochain carrier and rejecting a criterion for containing
  the word "metric" would itself be a false kill.)
CHAIN_INVOKED = false (no junction map was evaluated, no junction object formed,
  no numeric produced, no member bound, no fixed point, no end test, no comparison
  to any measured constant. This is preregistration only. It is no longer a draft:
  the principal's review is complete, the freeze is approved, and THIS SEAL
  EXECUTES IT -- before any junction map is computed.)
VERB_AUDIT_SELF = CLEAN (+1 DIRECTIVE THAT GREW UNDER ME, §5A: I re-hashed the
  principal's note at close and found it 2,677 -> 3,640 bytes, with ADDENDUM 2 and
  REQUIREMENT 5 appended mid-relay. I read the addition and carried it rather than
  sealing against the version I started from -- and the addition is not cosmetic:
  it requires a PREREGISTERED KILL CONDITION that G-1 alone did not supply, without
  which "measure, don't halt" is unfalsifiable and every divergence becomes evidence
  for the coupling reading. K-1 and K-3 are grounded on the corpus's own
  separation-versus-coincidence flag; K-2 was routed to the freeze review because no
  sealed statement fixes the admissible dependence, AND THE PRINCIPAL RULED IT A
  NAMED-OPEN SLOT -- the kill set freezes as {K-1, K-3} and K-2 is frozen EMPTY WITH
  ITS NAME ON IT, fillable only by a sealed grounding entering as a surfaced
  revision. +1 MY OWN AUDIT PROBE
  FLAGGED A PROHIBITION AS CONTAMINATION: the phrases "measured value" and "known
  number" appear in the criteria section only inside F5's own FORBIDDING language
  and inside my statement that nothing compares to a measured value -- exactly the
  over-application G-5 warns about, occurring inside my own pin check. +1 A RAW
  SUBSTRING ASSERTION OF MINE TRIPPED ON LINE WRAPPING FOR THE FOURTH TIME THIS
  SESSION -- the sentence was present and split across a newline. Whitespace-
  normalize before concluding that any sealed or drafted sentence is absent; that
  is now a standing rule of this lane, not an incident. +1 PRECEDENT I COULD NOT
  GROUND, §6.2: the directive
  cites the singlet-ratio hunt as a precedent and I could not locate it in the
  sealed corpus under any of seven spellings I searched; two nearest relatives are
  named and NEITHER IS ADOPTED as a substitute, and the three-verdict design does
  not rest on it, being grounded twice over independently. +1 FINDING AGAINST A
  SEALED FALSIFIER, §2.4: F1 would false-kill a running length normalization, and
  the junction arc would have inherited it silently. +1 AUDIT OF THE FILTER
  ITSELF, §2.5: a contamination sweep that rejects the word "metric" would kill a
  clean criterion, so the anti-classical discipline needed its own guard against
  over-application. +NOTE: a parallel survey supplied candidate spans and NONE
  entered this artifact without my own byte-level verification; the survey's own
  audit found that its gathered set had captured the UNFALSIFIABLE form of the
  central criterion -- the arrow type (L0) rather than the cell rule (JD-3) with
  its four obligations -- and R1-R4 are built on (JD-3) for that reason.)
```

The directive's worry is that the machinery will not recognize the record face of
gravity. The strongest thing the V001 draft found is that the machinery already
held one criterion that would refuse it: F1 fires on a beta that "remains a
positive continuous family", and a running conversion is exactly that. **The
junction arc would have inherited that falsifier without anyone deciding to.** It
no longer will: F1 is split, F1' governs, and the reading that was going to be
killed for free must now lose on a coefficient class or a locus or not at all.

Everything else here is bookkeeping around one distinction the corpus already
made twice — between a rule that halts on a divergence and a rule that reads it.
What freezes today is that distinction, plus one empty slot with its name on it.
