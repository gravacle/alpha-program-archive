# AUDIT — STAGE 8 THRESHOLD FORM O19SR V001 — CODENAME THRESHOLD-AUDIT

## COMMISSION O19SR — 2026-08-15 — DEFAULT-REFUTE, TESTIMONY ZERO WEIGHT

DETERMINATION ONLY. Nothing is proposed, authored, adopted, or retired. This
artifact re-derives at bytes; the target's own testimony about itself carried
zero weight and every claim below was checked against the sealed source spans.

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

OUTPUT-PATH PROBE: `STAGE8_THRESHOLD_FORM_O19SR_AUDIT_V001.md` and its
`.seal.sha256` sidecar were probed ABSENT before any write (`ls` returned
"No such file or directory").

---

## 0. STEP 0 — TARGET SEAL

```text
TARGET: STAGE8_THRESHOLD_FORM_O19SR_V001.md   (64595 bytes, 1081 lines)
SIDECAR: STAGE8_THRESHOLD_FORM_O19SR_V001.md.seal.sha256
RUN FROM THE ARTIFACT'S OWN DIRECTORY:
  shasum -a 256 -c STAGE8_THRESHOLD_FORM_O19SR_V001.md.seal.sha256
  => STAGE8_THRESHOLD_FORM_O19SR_V001.md: OK
DIGEST: 83115d2cb1c568975a2552718264d932636aae61254f7f6932ccc9724983e037
NOT BLOCKED. Audit proceeds.
```

## 0.1 CONSUMED SEALS — ALL RE-VERIFIED INDEPENDENTLY

Every carrier the target relies on was re-verified by THIS audit with
`shasum -a 256 -c` **run from the artifact's own directory**, and every digest
recomputed independently. 12/12 `OK`. All twelve recomputed digests agree
character-for-character with the table the target displays at its §1.

```text
a04c446a…  OBSTRUCTION_ORIGIN_O6SR_V001            [ORIG]     OK / match
0db4de90…  OBSTRUCTION_ORIGIN_O6SR_AUDIT_V001      [ORIG-A]   OK / match
241262ff…  W3_GCM_HS_TYPE_O3SR_V001                [W3]       OK / match
d05f22be…  W3_GCM_HS_TYPE_O3SR_AUDIT_V001          [W3-A]     OK / match
cfa2fb97…  IDEAL_EXTENT_S9AD_V001                  [EXT]      OK / match
eda2ba74…  IDEAL_EXTENT_S9AD_AUDIT_V001            [EXT-A]    OK / match
5e12af0b…  PARTITION_THEOREM_T16SR_V001            [PT]       OK / match
a307651e…  PARTITION_THEOREM_T16SR_AUDIT_V001      [PT-A]     OK / match
e1c2ac80…  ALLOW_REQUIRE_JUNCTION_T14SR_V001       [JCT]      OK / match
0057b134…  ALLOW_REQUIRE_JUNCTION_T14SR_AUDIT_V001 [JCT-A]    OK / match
ae52417f…  DISCHARGERS_VS_PARTITION_O11SR_V001     [DVP]      OK / match
5da05d53…  CERTIFICATION_RULES_O8SR_V001           [CR]       OK / match
NO CARRIER WAS UNVERIFIABLE. The target's seal-table claim is CONFIRMED.
```

---

## 1. FENCE-SCAN — RUN AS COMMISSIONED, THEN RUN AGAIN

```text
STANDARD APPLIED: every line scanned for (i) an evaluated threshold, (ii) a
numeral standing as A VALUE OF A PROGRAM QUANTITY, (iii) an approximation,
(iv) a numeric inequality. 418 lines of the target carry a digit; every one
was classified. TWO PASSES, the second independent of the first.

**RESULT: NO FENCE-HIT.** Stated plainly and not hedged: this artifact
produces, approximates, bounds, or compares NO value of any program quantity.
```

### 1.1 THE NEAREST APPROACH — NAMED LOUDLY, AND IT HELD

```text
FA-1  **THE COUPLING ROW (§2.4 / FLAG-1) — THE HEAVIEST ITEM IN THE ARTIFACT.**
      The target displays that Axis B's condition is COUPLING-EXPRESSIBLE and
      quotes [ORIG] :1103-1106 to do it. RE-DERIVED AT BYTES: the row is
        h_A_sym = kmag - q * A3
        sp.diff(h_A_sym, x1) == -q and sp.simplify(sp.diff(h_A_sym, x1)) != 0
      This is an EXACT SYMBOLIC DERIVATIVE returning a SYMBOL. No numeral is
      attached to q anywhere in the artifact. The battery carries the factor as
      `Q = sp.Symbol('Q')` with the source comment "DELIBERATELY UNINTERPRETED"
      ([target] :828), and `Q` is never substituted, never bounded, never
      compared. The `!= 0` is a NON-VANISHING, not an ordering against a value.
      **THE HALT IS REAL AND IT IS AT THE ROW.** VERIFIED, NOT ACCEPTED.

FA-2  **THE ONLY NUMERALS-AS-THRESHOLD-VALUES IN THE ARTIFACT (CH-8 :646).**
      "HS threshold 3/2" vs "HS threshold -3/2". These ARE numerals standing as
      values of a threshold. ADJUDICATION: they are (a) verbatim quotations from
      [ORIG]'s own FLAG-3, re-verified at [ORIG] :213-214 and :850-852; (b) a
      regularity/smoothing ORDER — a structural exponent, not a coupling, a
      scale, or a record constant; (c) explicitly NOT reconciled, the target
      stating that reconciling two sealed conventions would be authorship.
      CLASSIFIED FENCE-ADJACENT, QUOTED-AND-QUARANTINED. NOT A FENCE-HIT — but
      it is the loudest numeral in the file and it is named here for that.

FA-3  **EVERY NUMERIC INEQUALITY, ENUMERATED AND CLASSIFIED.** The strict
      reading of the standard returns these and only these:
        "dim M_N >= 2"        (:164, :373, :387-388, :391, :442, :465, :550)
        "{m < 0}" / "{k3<0}"  (:252, :254)
        r >= 1 ; dg <= 0 ; d >= 1 ; D >= 2   (battery :808, :842, :872, :935)
        "dim ker(qtilde_N) is in {1,2}"       (:401)
      EVERY ONE is posed on a STRUCTURAL INDEX — a dimension, a rank, a degree,
      a menu size — and every one is either quoted from a sealed carrier or is
      the declared indicator of such a quoted condition. NONE is a value of a
      program quantity. The target's own preamble declares exactly this class as
      its permitted material, and the declaration is HONOURED throughout.

FA-4  NO APPROXIMATION OF ANY KIND. No `evalf`, no `N()`, no `float()`, no
      tolerance, no "approximately", no "of order", no "roughly". Confirmed by
      scan. The IMPORT AUDIT's "NO FLOAT ANYWHERE" claim is consistent with
      every byte of the displayed source.

FA-5  Remaining numerals are counts and versions — 1758 files, 109M, 40/13/21
      carriers, 25 checks, 12 seals, sympy 1.14.0, python 3.9.6. Not program
      quantities.
```

### 1.2 FENCE VERDICT

```text
FENCE-HIT COUNT: **ZERO.**
The commission ran nearer the fences than any other today and the artifact
stopped where it said it stopped. alpha_computed = false ;
proof_authorized = false ; kappa_record_computed = false — all three HELD.
```

---

## 2. (E) QUOTATION INTEGRITY AGAINST FULL SOURCE SPANS

The day's recurring defect. Every quotation in the target was re-read against
its full source span, not against the fragment quoted. **THIS ARTIFACT IS THE
DAY'S CLEANEST ON THIS AXIS.** Fourteen quotations checked; fourteen exact;
every elision marked with `...` or `…`; no span fabricated; no quotation
carrying a meaning its source does not bear.

```text
Q-CHK  SOURCE SPAN                          RESULT
  1  [ORIG] :1084-1111  O6-1d1..d5 rows     EXACT — all five rows verbatim
  2  [ORIG] :1103-1106  the coupling row     EXACT
  3  [ORIG] :1057 O6-1b2                     EXACT
  4  [ORIG] :1067 O6-1c2                     EXACT
  5  [ORIG] :1036 O6-1a5                     EXACT
  6  [ORIG] :213-214, :850-852 FLAG-3        EXACT (CH-8)
  7  [ORIG-A] :254-267  F-4a                 EXACT, ellipsis marked
  8  [EXT] :8-12   the dim M_N biconditional EXACT, ellipsis marked
  9  [EXT] :53-59  the two-entry extent menu EXACT, ellipses marked
 10  [EXT] :39-40  "NOT-CLOSABLE-TODAY"      EXACT
 11  [EXT] :90-93  missing closure object    EXACT
 12  [JCT] :294-313  THE DELIVERABLE QUOTE   EXACT, ellipses marked
 13  [JCT] :321-336  §5.3 verdict            EXACT, ellipses marked
 14  [JCT] :283-285  §5.1 rigidity           EXACT, ellipsis marked
 15  [PT] :146, :149, :156-157, :198-199,
      :421, :185-188                         EXACT
 16  [DVP] :508-515                          EXACT, ellipsis marked
```

**THE DELIVERABLE QUOTE, CHECKED HARDEST.** [JCT] :294-313 is the one quotation
on which the whole boundary-moves finding rests, so it was compared
character-by-character against the full §5.2 block. Both operative clauses are
verbatim: `— the B-1 permission OPENS here.` and `— the SAME quantity is not a
permission but a forced kill.` The two elisions (`((LM1-10), (S8), the displayed
generators, L_T,N != 0)` and the R-5/R-6/X-3 parenthetical) are MARKED and drop
nothing that bears on the flip. Double-quotes were re-rendered as single quotes
for nesting only. **NO DEFECT.**

### 2.1 MINOR CITATION SLIPS — NOTED, NONE SUBSTANTIVE

```text
M-1  [PT] :188 writes "residual −2" with U+2212 MINUS SIGN; the target renders
     "residual -2" with an ASCII hyphen. Character normalization only.
M-2  §3.2 TH-1 quotes [EXT] :100-101 as "(at undisplayed dim M_N the kill does
     not close)" — the source paren continues "; round 3 §5.2)". A tail dropped
     inside a paren without an ellipsis mark. No meaning changed.
M-3  §4.2 cites [EXT] :76-82 but the quoted tail "no sealed byte fixes the bit"
     runs to :83. Cited span one line short of its own quote. Also drops "(§5)"
     unmarked after "What remains open, exactly".
M-4  §0 renders `kmag - q*A3`; the source is `kmag - q * A3`. Whitespace.
M-5  §2.4 generalizes the row to "the coupling times the potential's gradient".
     The row itself yields exactly `-q`, the gradient being 1 for [ORIG]'s
     A_3(x) = x_1. A mild extrapolation; the quantity stays uninterpreted, so it
     approaches nothing. NOT a fence issue.
```

---

## 3. (F) VERDICT PROPOSALS — NONE. (G) LENS TOKENS — NONE.

```text
(F)  NO proposal, adoption, or conclusion about any carrier's verdict was found.
     The target restates four sealed verdicts and every restatement is EXACT:
       [PT]  "VERDICT = PARTITION-THEOREM-DERIVED (unconditional over its
             stated scope)"                              — [PT] :459, verbatim
       [JCT] "JUNCTION-CONTINGENT"                       — [JCT] :321, verbatim
       [EXT] "NOT-CLOSABLE-TODAY"                        — [EXT] :39, verbatim
       [ORIG-A] "CONFIRMED-WITH-CORRECTIONS"             — consistent
     §4.3's "NOTHING ABOVE MOVES ANY VERDICT" is borne out at bytes. The only
     hit on proposal-vocabulary in the whole file (:545) is a DISCLAIMER
     ("NEITHER PROPOSED, RANKED, NOR RECOMMENDED BY THIS ARTIFACT"), attached
     to [EXT]'s own named missing-closure object, which the target displays as
     the record's text and does not rank. LAWFUL.
     The target's own VERDICT = THRESHOLD-SHAPED is its commissioned
     determination, not a proposal about another carrier. In scope.

(G)  NO LENS TOKEN. The string "lens" occurs EXACTLY ONCE in 1081 lines
     ([target] :168) and it occurs INSIDE THE EXCLUDED-FILE LIST — naming the
     class of files the sweep refused to read. That is an exclusion notice, not
     a token in use. CLEAN.
```

---

## 4. (B) THRESHOLD-SHAPED WHERE THE BYTES SHOW PRESENCE/ABSENCE

Threshold is the wanted answer here and therefore the suspect one. For EVERY
threshold call the target makes, this audit demanded the operative sentence
exhibiting A QUANTITY AND A CROSSING, at bytes, and killed any call resting on
a paraphrase. Two calls survived. **TWO DID NOT.**

### 4.1 THE CRITERION THE TARGET BOUND ITSELF TO

```text
[target] §2.1, fixed BEFORE the evidence by the target's own account:
  BINARY     iff g admits exactly TWO values of record
  THRESHOLD  iff g admits MORE THAN TWO values of record AND the indicator is
             MONOTONE in g and NON-CONSTANT
  "These three are mutually exclusive on any single g."
THE VALUES-OF-RECORD CLAUSE IS NECESSARY, NOT DECORATIVE, AND IT IS PER-g.
The target enforces it for Axis A (check T19-1a1, `len(set(mult_vals)) == 3`).
It is enforced NOWHERE ELSE IN THE ARTIFACT.
```

### 4.2 SURVIVING THRESHOLD CALLS — CONFIRMED AT BYTES

```text
TH-3 / AXIS A — CONFIRMED. Three distinct displayed values of the negative
  spectral multiplicity, each re-verified in [ORIG] at its own line:
    :1057  "O6-1b2  {m < 0} is EMPTY  =>  C = 0  =>  C T C = 0  =>  THEOREM
            VACUOUS"                                            — value 0
    :1067  "O6-1c2  {m<0} = half-space {k3<0} is NONEMPTY => C != 0"
                                                                — value 1
    :1036  "O6-1a5  rank(P_-) = 2 per k  (tr P_- = 2)"          — value 2
  QUANTITY: a rank. CROSSING: empty -> inhabited, a strict change at a stated
  index. MORE THAN TWO VALUES OF RECORD: YES, three, each quoted. Monotone and
  non-constant. **GENUINE THRESHOLD. The call stands.** The displayed-slack
  finding (record site strictly above the turn-on) also stands: 2 > 1.

TH-1 / THE STAGE DIMENSION — CONFIRMED. Operative sentence at [EXT] :8-12,
  verbatim: "at dim M_N >= 2 with TOP-1/TOP-2, B-1 INHABITED <=> NO MIXING
  RELATION at the anchor stages". QUANTITY: dim M_N. CROSSING: >= 2, an
  inequality against a stated index over an unbounded range. The complement is
  displayed too ([EXT] :100-101, "at undisplayed dim M_N the kill does not
  close"). **GENUINE THRESHOLD. The call stands.**
  Lesser note, not a kill: the battery supplies stage_dims = [1,2,3] rather
  than quoting three displayed values, as it did for Axis A. The `>= 2` form
  over an unbounded index carries the clause on its own, so the asymmetry in
  rigour is noted and not charged.

TH-0 / THE QUANTIZATION CONDITION — CORRECTLY EXCLUDED, AND THE EXCLUSION IS
  THE ARTIFACT'S BEST SINGLE PIECE OF WORK. A congruence is not a threshold;
  the non-monotone indicator is exhibited, not asserted; and the target
  volunteers that counting it would have "inflated the inventory and
  misdescribed the partition's own require-side". CONFIRMED.
```

### 4.3 **F-1 — PRINCIPAL CORRECTION: AXIS B IS NOT A THRESHOLD OF RECORD**

```text
THE CALL: [target] §2.3 / §3.2 TH-4 / closing line THRESHOLD_AXIS_B —
  "THRESHOLD FORM IN A STRUCTURAL DEGREE".

THE DEMAND: the operative sentences exhibiting a quantity and a crossing.
THE BYTES RETURN EXACTLY TWO VALUES OF THE POSITION-DEGREE, AND NO MORE:
  [ORIG] :1107-1111  "a CONSTANT potential shifts the symbol only: d/dx = 0"
                     — A_const, position-degree 0
  [ORIG] :1096-1101  "e.g. A_3(x) = x1" ; "A(x+a) - A(x) = a != 0"
                     — A_3(x) = x_1, position-degree 1
  A GLOBAL PHASE (:1088-1095) changes no degree at all.
SWEPT FOR A THIRD: every occurrence of `A3`, `A_3`, `A_const`, `A(x)` and
  "potential" in [ORIG] was read. **NO SEALED DISPLAY ANYWHERE CARRIES A
  POSITION-DEGREE 2, OR ANY DEGREE ABOVE 1.**

THE MECHANISM OF THE SLIP, AT THE TARGET'S OWN BYTES:
  [target] :841  `deg_vals = [sp.Integer(0), sp.Integer(1), sp.Integer(2)]`
  The third value is SUPPLIED BY THE BATTERY, not read off any display. And
  the battery contains NO analogue of T19-1a1 for Axis B — there is no
  `len(set(deg_vals)) == 3` check, and no check of any kind that the
  values-of-record clause is met. THE CLAUSE IS ENFORCED FOR AXIS A AND
  SILENTLY OMITTED FOR AXIS B. §2.3's Axis B block invokes only monotone +
  non-constant (T19-1b4/b5) and never the clause that the criterion makes
  necessary.

THE SEALED GROUND TYPES IT THE OTHER WAY, IN ITS OWN CHOICE LEDGER:
  [ORIG] :1379-1382, verbatim — "CH-2  THE GAUGE COUNTERFACTUAL'S POTENTIAL.
  A_3(x) = x_1 was chosen as the non-constant U(1) potential. UNFORCED — any
  non-constant A gives d(symbol)/dx != 0. CLASS: generic placeholder. The
  finding is the SIGN of the derivative's non-vanishing, not the potential."
  THE GROUND CALLS ITS OWN AXIS-B CONTENT A NON-VANISHING — a presence/absence
  — and says the potential is a placeholder carrying no graded content.

WHY FLAG-3 DOES NOT DISCHARGE THIS. FLAG-3 raises the right doubt and then
  resolves it for BOTH axes on ONE axis's evidence: "I classify them THRESHOLD
  on the strength of the record displaying THREE values of Axis A's quantity".
  The criterion is stated per-g and "mutually exclusive on any single g".
  AXIS A's THREE VALUES ARE NOT AXIS B's. The transfer is not licensed by the
  criterion the target itself fixed before the evidence.
  CH-2 discloses the competing two-valued reading and is credited — but
  disclosure of a choice does not satisfy a criterion.

**CORRECTION F-1.** Of record, Axis B is BINARY — equivalently a NON-VANISHING
  condition — on the position-degree. THRESHOLD_AXIS_B should read
  NON-VANISHING / BINARY-OF-RECORD; or, if the graded reading is kept, §2.1's
  values-of-record clause must be struck for both axes and the criterion
  restated. IT CANNOT BE BOTH.
WHAT SURVIVES F-1, AND IT IS MOST OF THE FINDING:
  * The BINARY-IN-U(1)-PRESENCE REFUTATION IS UNTOUCHED AND IS CORRECT. U(1)
    structure is present in all three displayed cases and the hypotheses move
    in one; the map from U(1)-presence to escape is not well defined. VERIFIED
    at [ORIG] :1088-1111. This is the target's soundest claim.
  * The WINDOW claim survives in substance: a LOWER condition on a rank
    conjoined with an UPPER condition on a degree, running in opposite senses,
    is still not a single presence/absence bit. One of the two conjuncts is
    simply not a threshold.
  * FLAG-5 / §2.5 — that the cell above Axis B is UNDECIDED, not "escaped" —
    is CONFIRMED exactly, against [ORIG-A] :254-267 read in full.
```

### 4.4 **F-2 — TH-2 "THE EXTENT THRESHOLD" FAILS THE SAME CLAUSE**

```text
THE CALL: [target] §3.2 — "TH-2  THE EXTENT THRESHOLD ... A THRESHOLD IN: the
  DIMENSION OF THE RELATION IDEAL'S EXTENT", carried into the closing line
  THRESHOLDS_ELSEWHERE as "TH-2 extent dimension".

THE BYTES, WHICH THE TARGET ITSELF QUOTES AND THEN READS PAST:
  [EXT] :59, verbatim — "dim ker(qtilde_N) is in {1,2} — no third extent
  exists."  EXACTLY TWO VALUES OF RECORD, and the carrier says so in the same
  breath. The target's own check T19-3a asserts `len(extent_menu) == 2`.
  BY §2.1, EXACTLY TWO VALUES OF RECORD IS THE DEFINITION OF **BINARY**.

AND THE BYTES SHOW PRESENCE/ABSENCE LITERALLY. [EXT] :55-58 —
  "E-1 (no mixing): ker = span{(0,1,-R_K)}, dim 1"
  "E-2 (mixing):    ker = span{(0,1,-R_K), (-a_K,1,0)}, dim 2"
  The two entries are the ABSENCE and the PRESENCE of a mixing relation. The
  dimension is a LABEL on the two cases, not a graded coordinate. THIS IS THE
  COMMISSION'S HUNT (B) IN ITS PUREST FORM: a threshold asserted where the
  bytes show presence/absence.

**CORRECTION F-2.** TH-2 is BINARY. Strike "THRESHOLD" from its name and from
  THRESHOLDS_ELSEWHERE.
WHAT SURVIVES F-2 — AND THE DELIVERABLE DOES SURVIVE:
  The §3.3 finding is that ONE NAMED CONTENT is classified differently on the
  two sides. That is exhibited at bytes and is not damaged by the parameter
  being a bit rather than a graded index. What must change is only the FORM
  word attached to the parameter. The target's own §4.3 ST-1 already writes
  "Menu / bit" for this very site — the artifact contradicts itself between
  §3.2 and §4.3, and §4.3 has it right.
```

---

## 5. (C) BINARY ASSERTED WHERE THE BYTES SHOW A STAGE- OR RANK-INDEXED CONDITION

```text
HUNTED, NOT FOUND. The target asserts BINARY exactly once — of U(1)-PRESENCE,
and only to REFUTE it. Re-derived at [ORIG] :1088-1111: U(1) structure is
carried in all three displayed cases (global phase; constant potential;
non-constant potential) and the hypotheses move in exactly one. The refutation
is sound and the direction of the error runs the OTHER way in this artifact —
toward over-calling threshold (§4), not toward over-calling binary.
NO INSTANCE OF (C). CLEAN.
```

---

## 6. (D) THE BOUNDARY-MOVES CLAIM — AND THE HUNT FOR WHAT THE BUILD MISSED

A short list is the comfortable outcome, so the hunt for missed instances was
run harder than the check of the one instance offered.

### 6.1 THE OFFERED INSTANCE — CONFIRMED, SAME CONTENT QUOTED ON BOTH SIDES

```text
The commission's test: the SAME content classified differently on the two
sides of the parameter, QUOTED. [JCT] :294-313 delivers it and the quotation
is exact (§2 above):
  LOWER SIDE (ker dim 1): "— the B-1 permission OPENS here."      ALLOW
  UPPER SIDE (ker dim 2): "the SAME quantity is not a permission
                           but a forced kill."                    REQUIRE
  THE CARRIER ITSELF SAYS "the SAME quantity". The content is not inferred to
  be the same; the source asserts identity in its own words. B-1 inhabitance
  is one named content, and its modality flips across the menu.
**INSTANCE CONFIRMED AT BYTES.** CH-5 is also credited as correct and careful:
  the target claims only that the CONTENT is permitted below and its NEGATION
  required above, refusing the stronger and unsupported reading. That is the
  right call and the byte is the point.
```

### 6.2 **F-3 — THE SWEEP REGEX IS ONE-SIDED; EVERY UPPER THRESHOLD FELL OUTSIDE IT**

```text
THE DEFECT, AT THE TARGET'S OWN BYTES ([target] :160-162):
  (S-ii)  (dim|rank|degree|codimension)[^,.;]{0,25}(>=|>=|≥) ?[0-9]
  THE ALTERNATION LISTS `>=` TWICE AND CARRIES NO `<=`, NO `≤`, NO `<`.
  IT CAN ONLY EVER RETURN **LOWER** THRESHOLDS.

THIS IS THE EXACT BLIND SPOT THE TARGET'S OWN HEADLINE WARNS OF. §0(2) and
  §2.3 find that the two axes "run in OPPOSITE SENSES — Axis A is a LOWER
  condition and Axis B an UPPER condition". The artifact discovers that upper
  thresholds exist and are load-bearing, and then sweeps the corpus for lower
  thresholds only.

THE COMPLEMENT SWEEP, RUN HERE (same quantities, `<=|≤|<`, same root (R-a),
  same excluded-file filter): **46 CARRIERS** — MORE than the 40 the one-sided
  sweep returned. Two hits are decisive and both are missing from §3.2's
  inventory:

  MISSED-1  [STAGE8_AMPLITUDE_JUNCTION_S9AD_V001.md] :283, verbatim:
    "the record's bundle is a **fixed line bundle** — fibers of dimension 1.
     Frame-function forcing fails in dimension ≤ 2 even when full inner-product
     structure is granted; on dim-1 fibers there is no nontrivial frame
     consistency to force anything. The ground's own carrier is below the
     forcing threshold."
    A THRESHOLD IN A DIMENSION, with a quantity (fiber dimension), a crossing
    (≤ 2 fails / 3 and above forces), and the record's own site displayed
    BELOW it. AND IT IS A **FORCING** THRESHOLD — it governs whether content is
    FORCED, i.e. it sits directly on the allow/require axis this commission was
    sent to survey. Its carrier is named at [AJ] :682 and :570.
    ABSENT FROM TH-0..TH-4.

  MISSED-2  [ORIG] :320, :507, :1117-1118, verbatim:
    "A degree-(<= -1) symbol cannot identically cancel a degree-0 symbol."
    An UPPER threshold IN A DEGREE — the same kind of quantity as Axis B —
    inside THE TARGET'S OWN PRIMARY SEALED GROUND, a carrier it verified,
    quoted from repeatedly, and read at least four separate spans of.
    ABSENT FROM TH-0..TH-4.

WHY FLAG-2 DOES NOT COVER THIS. FLAG-2 bounds the negative to thresholds
  "written with a STRUCTURAL QUANTITY against a NUMERAL" and discloses that
  word-only and symbolic-bound thresholds would be missed. BOTH MISSED HITS
  ARE WRITTEN WITH A STRUCTURAL QUANTITY AGAINST A NUMERAL. They fall inside
  FLAG-2's declared class and outside the regex that implements it. The
  disclosure and the instrument do not match, and the gap is undisclosed.

**CORRECTION F-3.** §3.2's inventory is not exhaustive even for its own
  declared numeral class. FLAG-2's bound must be restated as "`>=` and `≥`
  only — no upper threshold was swept for". The exhaustiveness language at
  §1.1 ("that list IS the sweep's extent") and at §3.4 must be re-scoped
  accordingly.
```

### 6.3 **F-4 — SWEEP (S-iv) WAS DECLARED AND NEVER DISCHARGED**

```text
[target] :166 declares:
  "(S-iv) FIXED-STRING sweep for side assignments: 'allow-side' |
   'require-side'."
**ITS RETURN IS REPORTED NOWHERE IN THE ARTIFACT.** (S-ii) reports 40 and
lists them; (S-iii) reports 13 and lists them; (S-iv) reports nothing. It is
the one sweep aimed squarely at the deliverable and it is the one sweep whose
result never appears.

RUN HERE, root (R-a), same excluded-file filter, target itself excluded:
  **21 CARRIERS.**
  5D_SYMMETRIC_AUDIT_T13SR ; 5D_REREAD_T13SR ; ALLOW_REQUIRE_JUNCTION_T14SR ;
  DISCHARGERS_VS_PARTITION_O11SR (+AUDIT) ; EM_PARTICIPATION_O4SR (+AUDIT) ;
  FORCING_NOTION_O12SR (+AUDIT) ; GATE_SIGNATURE_O18SR ;
  ITEMS_1_6_COVERAGE_AUDIT_FABLE ; PARTITION_THEOREM_T16SR (+AUDIT) ;
  SUMMED_MECHANISM_O7SR (+AUDIT) ; TASK4A_NETWORK_SOURCING_LAW_V004_FINAL_
  REVIEW_LANE1 ; TASK4A_ORIGIN_FED_REFINEMENT_TOWER_GENOMEGA_PORT_TYPECHECK_
  DETERMINATION_CODEX_LANE2 ; TASK4A_FINITE_RECORD_REFINEMENT_TOWER_CROSS_
  VERIFICATION_DETERMINATION ; TASK4A_NETWORK_SOURCING_LAW_ADOPTION_PROPOSAL_
  CODEX_LANE2 ; TASK5_FIXED_POINT_SENSITIVITY_AUDIT_LANE1 ;
  U1REL_EM_IDENTIFICATION_O14SR ; THRESHOLD_FORM_O19SR (the target).

AGAINST THIS, [target] §3.4 states: "the ones carrying an allow/require SIDE
  ASSIGNMENT at all are the junction pair, the partition pair, [DVP] and [CR]"
  — SIX files. (S-iv) returns 21. Moreover [CR] and [JCT-A] are NOT among the
  21 at all, so even the six named are not the right six.

THE CARRIER THE SWEEP MOST NEEDED TO SEE, AND DID NOT:
  [STAGE8_FORCING_NOTION_O12SR_V001.md] carries dedicated inventories
  "§1.2 REQUIRE-SIDE ROWS R-1 … R-10" and "§1.3 ALLOW-SIDE ROWS A-1 … A-13",
  each row given with its OPERATIVE SENTENCE — the densest side-assignment
  carrier in the corpus, and the only one that tabulates the junction survey's
  own rows by notion. It has ZERO (S-ii) matches, so it was invisible to the
  sweep that was actually run.
  Its A-1 row, at bytes, displays a SECOND two-model witness:
    "TWO-MODEL WITNESS, executed: f₁ … and f₂ = f₁² satisfy every displayed
     clause simultaneously (AJ CAS M8/M9) and differ as functions"; "two
     models of every displayed clause exist that differ on the junction"
  and types it **MT. The record's executed instance.** Its A-2 row is the J-2
  instance the target found, typed "the record's second live instance".
  THE RECORD ITSELF NUMBERS THE TARGET'S INSTANCE **SECOND**.

**ADJUDICATION, AND IT IS THE FAIR ONE — THE COUNT SURVIVES.** A-1 is NOT a
  second boundary-MOVES instance under the deliverable's own test. f₂ = f₁² is
  a DIFFERENT MODEL, not a parameter crossing a value; no single content is
  classified differently on the two sides of an index. It witnesses
  NON-FORCING, not a moving boundary. **"ONE INSTANCE" STANDS AS THE ANSWER.**

**WHAT DOES NOT SURVIVE IS THE WARRANT.** §3.3's unscoped bold claim — "IT IS
  THE ONLY ONE THE DECLARED SWEEP RETURNS" — is false as written, because
  (S-iv) is a declared sweep and it returns FORCING_NOTION_O12SR and sixteen
  other unexamined side-assignment carriers. §3.4's negative is saved only by
  its leading scope clause ("Of the 40 carriers of sweep (S-ii)"); §3.3's is
  not scoped and is not saved.

**CORRECTION F-4.** Either discharge (S-iv) and report its 21 carriers, or
  strike (S-iv) from the declared terms and re-scope §3.3's "ONLY ONE" to
  sweep (S-ii) explicitly, as §3.4 already does.
```

### 6.4 F-5 — MINOR COUNT DISCREPANCY

```text
(S-ii) reproduced here returns 42 carriers (41 excluding the target itself);
the artifact reports 40. The full list IS displayed at §3.1, which is what
bounds the negative, so the defect is small and self-correcting. NOTED ONLY.
```

---

## 7. SWEEP CUTOFF — DECLARED

```text
SWEEP CUTOFF: 2026-08-15, this session, THRESHOLD-AUDIT.
ROOTS: (R-a) /Users/bgm/MB Work/alpha-program-archive/workspace   (primary)
       (R-b) /Users/bgm/Documents/New project/gravity_emergence_evidence_
             program/alpha_fundamental_record_action_cleanroom_v003
TERMS RUN BY THIS AUDIT, all scoped, all declared:
  (A-i)   REPRODUCTION of the target's (S-ii) regex, root (R-a). Returned 42.
  (A-ii)  **COMPLEMENT** of (S-ii): same quantities against `<=|≤|<`. This is
          the term the target never ran. Returned 46. Basis of F-3.
  (A-iii) DISCHARGE of the target's declared (S-iv): fixed strings
          "allow-side" | "require-side", root (R-a). Returned 21. Basis of F-4.
  (A-iv)  two-model | two models | model-dependent, root (R-a). Returned 21.
  (A-v)   Targeted reads of every source span the target cites, read in FULL
          (not at the fragment), plus full-file numeral classification of the
          target itself.
EXCLUDED BY COMMISSION, NOT READ: every register / tracker / road / plan /
  continuation / ledger / lens / THE_HANDOFF file. Filter applied to every
  sweep result BEFORE any read. "Q-..." tokens EXPECTED-UNLOCATABLE; none was
  resolved and none was sought.
EXHAUSTIVENESS OF THIS AUDIT, STATED HONESTLY: the missed-threshold finding
  (F-3) is exhaustive for STRUCTURAL QUANTITY AGAINST A NUMERAL IN EITHER
  DIRECTION. A threshold written purely in words remains outside BOTH the
  target's sweep and mine. THAT LIMIT IS MINE AND IS NOT HIDDEN — see AF-3.
NO GIT. No existing file edited. ONE output file plus its seal sidecar.
```

---

## 8. CHOICE LEDGER

```text
AC-1  I ENFORCED THE TARGET'S OWN CRITERION AGAINST IT, RATHER THAN MINE.
      §2.1's three-cell test is the target's own, fixed by its account before
      the evidence. I did not substitute a criterion of my own; I applied the
      one on the page, including the values-of-record clause the target
      enforced for Axis A and dropped for Axis B. ALTERNATIVE NOT TAKEN:
      judging the form on monotonicity alone, which would have passed both
      axes and produced a cleaner and less true audit.
AC-2  I DID NOT RE-EXECUTE THE BATTERY. No venv, no CAS, no run. The defect at
      F-1 is in the battery's SOURCE — the supplied `deg_vals` list at :841 and
      the absent values-of-record check — and is visible at bytes without
      running anything. Re-running would have reproduced 25 PASS and told me
      nothing, since every check passes on its own supplied inputs. DISCLOSED
      SO THE CHOICE IS CHECKABLE: I did not verify that the displayed OUTPUT
      block was produced by the displayed SOURCE. See AF-1.
AC-3  I RAN THE COMPLEMENT SWEEP THE TARGET DID NOT. This is the single
      judgement that produced F-3. It was prompted by the target's own finding
      that its two axes run in opposite senses — the artifact told me where to
      look and I looked there.
AC-4  I ADJUDICATED A-1 **IN THE TARGET'S FAVOUR**. FORCING_NOTION_O12SR's A-1
      is a second two-model witness of record and the record numbers the
      target's instance SECOND. It would have been easy, and wrong, to report
      a missed instance. A-1 has no parameter and no crossing, so it fails the
      deliverable's own test and the "ONE INSTANCE" count stands. The finding
      is against the WARRANT, not against the ANSWER.
AC-5  I TREATED STRUCTURAL-INDEX INEQUALITIES AS FENCE-ADJACENT, NOT
      FENCE-HITS. A strict reading of the commission's scan standard returns
      every `dim M_N >= 2`. I classified by whether a numeral stands as a value
      of a PROGRAM QUANTITY, and none does. ALTERNATIVE NOT TAKEN: reporting
      seven fence-hits on quoted dimensions, which would have made the word
      "fence-hit" useless on the day it mattered most. THE FULL ENUMERATION IS
      GIVEN AT FA-3 SO A READER WHO WEIGHTS IT DIFFERENTLY CAN.
AC-6  I DID NOT RECONCILE THE HS-THRESHOLD SIGN CONVENTION. Carried forward
      untouched, exactly as [ORIG] and the target both left it. Reconciling two
      sealed conventions would be authorship.
AC-7  I DID NOT RESOLVE "Q-..." TOKENS — EXPECTED-UNLOCATABLE, per commission.
AC-8  I GRADED THE THREE DELIVERABLES SEPARATELY BEFORE GRADING THE WHOLE, so
      that a correction on question (1) does not silently drag down question
      (2), which is the commission's actual deliverable and which survives.
```

## 9. TOY_SEPARATION

```text
ACTUAL SURFACE (the object of this audit):
  * The target's bytes, and the sealed bytes of the twelve carriers it
    consumes, read at their own line numbers.
  * The seal state of all thirteen files, verified from each artifact's own
    directory.
  * The extent of the target's declared sweeps, reproduced and complemented.
  * The FORM of each threshold call, tested against the target's own criterion.

NOT ACTUAL SURFACE — QUARANTINED, NEVER RELIED ON AS PHYSICS:
  * [ORIG]'s scalar symbols m(k) = |k|, m(k) = k_3 and the potential
    A_3(x) = x_1. These are [ORIG]'s own quarantined toys. I read them ONLY to
    count how many distinct position-degrees the record displays (F-1). No
    property of the program is inferred from any of them, and I neither extend
    nor re-author them.
  * f₁ and f₂ = f₁² in [FORCING_NOTION]'s A-1 row. Cited ONLY to adjudicate
    whether A-1 is a parameter crossing. They are the AJ carrier's declared
    toys and are not treated as content.
  * The regexes and file counts in §7. Instruments, not results.

NOTHING IN THIS AUDIT IS A CANDIDATE, A MEMBER, A ROUTE, A REPAIR, OR A
PROPOSAL. No toy is promoted. This is a determination about form and bytes.
```

## 10. IMPORT AUDIT

```text
NO CAS WAS RUN. No venv created, no interpreter invoked, no package installed,
  no import of any kind. NOTHING WAS COMPUTED, EVALUATED, APPROXIMATED, OR
  BOUNDED BY THIS AUDIT. See AC-2 for why, and AF-1 for the cost.
TOOLS USED, COMPLETE: `ls`, `shasum -a 256`, `shasum -a 256 -c`, `sed -n`,
  `grep`, `cat`, `wc -l`, `for`. Read-only throughout, except the two writes
  that produce this file and its sidecar.
NO NETWORK. NO GIT. NO FILE EDITED. NO REGISTER, TRACKER, ROAD, PLAN,
  CONTINUATION, LEDGER, LENS, OR HANDOFF FILE OPENED.
NO VALUE OF ANY PROGRAM QUANTITY APPEARS IN THIS ARTIFACT. Every numeral
  written here is a line number, a file count, a sweep return, a seal digest,
  or a structural index quoted from a sealed display.
```

## 11. FLAG BLOCK

```text
AF-1  **I DID NOT RE-EXECUTE THE BATTERY, SO THE DISPLAYED OUTPUT IS UNVERIFIED
      AGAINST THE DISPLAYED SOURCE.** I verified the SOURCE at bytes and found
      F-1 there. I did NOT confirm that the 25 PASS lines at §9.2 were produced
      by the code at §9.1. A reader wanting that link closed must run it. THE
      HEAVIEST LIMIT OF THIS AUDIT AND IT IS MINE.
AF-2  **F-1 AND F-2 REST ON A CRITERION, NOT ON A CONTRADICTION AT BYTES.**
      Axis B and TH-2 are internally inconsistent with §2.1, which is the
      target's own stated test. A reader who holds that the values-of-record
      clause was never meant to bind — that "threshold" should track only
      monotonicity — lands on CONFIRMED for both calls. I do not hold that,
      because §2.1 says "mutually exclusive on any single g" and because the
      target enforced the clause for Axis A. THE DISAGREEMENT CAN BE HAD AT
      BYTES: §2.1 :191-201, :812, :841, and [ORIG] :1096-1111, :1379-1382.
AF-3  **MY OWN SWEEP IS BOUNDED THE SAME WAY THE TARGET'S IS, IN ONE
      DIRECTION.** F-3 is exhaustive for a structural quantity against a
      NUMERAL in EITHER direction. A threshold written purely in words, or
      against a purely symbolic bound, would not be returned by my terms
      either. My negative is my sweep's, not the record's.
AF-4  **THE 46-CARRIER COMPLEMENT WAS NOT READ CARRIER-BY-CARRIER.** I read two
      of the 46 to bytes (MISSED-1, MISSED-2) and stopped, having established
      that the inventory is incomplete. HOW MANY OF THE REMAINING 44 CARRY
      FURTHER MISSING THRESHOLDS IS NOT DETERMINED HERE. The finding is that
      the inventory is not exhaustive; it is NOT a count of what is missing.
AF-5  **THE (S-iv) CARRIERS WERE NOT AUDITED FOR FURTHER MOVING BOUNDARIES.** I
      read FORCING_NOTION_O12SR's allow-side inventory and AMPLITUDE_JUNCTION's
      §6.3 and adjudicated A-1. THE OTHER FIFTEEN UNEXAMINED (S-iv) CARRIERS
      WERE NOT SEARCHED FOR A SAME-CONTENT-BOTH-SIDES INSTANCE. So "ONE
      INSTANCE" survives this audit but is NOT certified exhaustive by it. THAT
      IS THE HONEST STATE AND THE COMFORTABLE ANSWER IS NOT ENDORSED.
AF-6  **NO FENCE-HIT — AND I LOOKED TWICE.** Recorded here as a flag because a
      clean fence result on the day's nearest approach is the finding most
      likely to be doubted. The full enumeration is at FA-1..FA-5 so the result
      is checkable and not merely asserted.
AF-7  **QUOTATION INTEGRITY WAS THE DAY'S RECURRING DEFECT AND THIS ARTIFACT
      DOES NOT HAVE IT.** Sixteen source spans, all exact, all elisions marked.
      Flagged so the contrast with the day's other builds is on the record.
```

---

## 12. VERDICT

### 12.1 PER DELIVERABLE

```text
DELIVERABLE (1) — IS THE GAUGE ESCAPE BINARY OR THRESHOLD-SHAPED?
  **CONFIRMED-WITH-CORRECTIONS.**
  CONFIRMED: BINARY-in-U(1)-presence is genuinely REFUTED at bytes — U(1)
    structure is present in all three displayed cases and the hypotheses move
    in one ([ORIG] :1088-1111). Axis A is a GENUINE THRESHOLD in a rank, with
    three displayed values quoted at three separate lines and displayed slack.
    The §2.5 / FLAG-5 sharpening — that the cell above Axis B is UNDECIDED, not
    "escaped" — is exact against [ORIG-A] :254-267 read in full, and it is the
    artifact's most honest move.
  CORRECTED (F-1): AXIS B IS NOT A THRESHOLD OF RECORD. The position-degree
    admits exactly TWO values in the sealed displays (0 and 1); the third is
    supplied by the battery at :841 and read off nothing. The values-of-record
    clause of the target's own §2.1 is enforced for Axis A and silently omitted
    for Axis B, and [ORIG]'s own CH-2 types the content as "the derivative's
    non-vanishing". Axis B is BINARY / NON-VANISHING.
  NET: the verdict word THRESHOLD-SHAPED is CARRIED BY AXIS A ALONE. The
    WINDOW shape survives as a conjunction of a threshold and a non-vanishing.

DELIVERABLE (2) — DOES THE ALLOW/REQUIRE BOUNDARY MOVE?
  **CONFIRMED.**
  The instance at J-2 is exhibited, not inferred: the SAME content is quoted on
  both sides, the carrier itself asserting "the SAME quantity", and the
  quotation of [JCT] :294-313 is EXACT with every elision marked. CH-5's
  refusal to overstate the flip is correct. THE ANSWER — YES, ONE INSTANCE —
  STANDS, and the search for a missed second instance did not overturn it
  (§6.3).
  CORRECTED (F-2): the parameter is a BIT, not a threshold — [EXT] :59 says
    "no third extent exists" and the two entries are the absence and presence
    of a mixing relation. §4.3 ST-1 already writes "Menu / bit"; §3.2 must
    agree with it.
  CORRECTED (F-3, F-4): the EXHAUSTIVENESS WARRANT does not hold. The sweep
    regex is one-sided and can return no upper threshold; the complement
    returns 46 carriers and two confirmed missing thresholds, one of them a
    FORCING threshold in a dimension and one inside the target's own primary
    ground. Declared sweep (S-iv) was never discharged; run here it returns 21
    side-assignment carriers against the six the artifact names.

DELIVERABLE (3) — WHAT THE MOVING BOUNDARY IMPLIES FOR THE PARTITION.
  **CONFIRMED.**
  The parameter-free, site-scoped reading of the partition theorem verifies at
  [PT] :146, :149, :156-157, :198-199, :421 — every quotation exact. The
  class/member axis is corroborated at [DVP] :508-515, exact. P-1 is correctly
  displayed as LEFT OPEN with its three sealed byte-displays intact. ST-1..ST-4
  overreach nowhere. NOTHING IS PROPOSED, ADOPTED, OR CONCLUDED ABOUT ANY
  VERDICT, and all four restated verdicts are verbatim.
```

### 12.2 CROSS-CUTTING

```text
FENCE-SCAN (A)          : **NO FENCE-HIT.** Run twice. The coupling row is
                          displayed and halted at, exactly as claimed. The only
                          numerals-as-values in the file are [ORIG]'s quoted
                          and unreconciled HS-threshold conventions.
QUOTATION INTEGRITY (E) : **CLEAN — 16/16 EXACT.** The day's recurring defect
                          is absent here.
SEALS                   : 13/13 OK (target + 12 consumed), each verified from
                          the artifact's own directory, every digest recomputed
                          and matching the target's own table.
VERDICT PROPOSALS (F)   : NONE.
LENS TOKENS (G)         : NONE.
BINARY-FOR-INDEXED (C)  : NO INSTANCE.
```

### 12.3 OVERALL

```text
**OVERALL VERDICT = CONFIRMED-WITH-CORRECTIONS.**

The artifact's central answers survive: the escape is not binary in
U(1)-presence, one axis is a genuine threshold, the allow/require boundary
does move at exactly one exhibited site, the partition theorem is stated
parameter-free, and the fences held on the day's nearest approach. Its
quotation discipline is exact and its self-flagging is unusually honest —
FLAG-3 and FLAG-5 name real doubts rather than burying them.

FOUR CORRECTIONS ATTACH, and they cluster in one place: THE ARTIFACT IS MORE
RIGOROUS WHERE IT DOUBTS ITSELF THAN WHERE IT ANSWERS. It enforced its own
values-of-record clause on the axis it was unsure of (A) and dropped it on the
axis and the menu that gave it the wanted word (F-1, F-2). It discovered that
upper and lower thresholds are different things and then swept for lower ones
only (F-3). It declared the one sweep aimed at its own deliverable and never
reported its return (F-4). THE ANSWERS ARE SOUNDER THAN THE WARRANTS OFFERED
FOR THEM.

NOTHING IS RETIRED, PROPOSED, AUTHORED, OR ADOPTED BY THIS AUDIT. Every
carrier, including the target, stands exactly as its own seal left it. No
fence, gate, witness, or V-clause is moved. DETERMINATION ONLY.
```

## 13. CLOSING FLAG LINES

```text
OVERALL                     = CONFIRMED-WITH-CORRECTIONS
DELIVERABLE_1_ESCAPE_FORM   = CONFIRMED-WITH-CORRECTIONS (F-1)
DELIVERABLE_2_BOUNDARY_MOVES= CONFIRMED (F-2, F-3, F-4 on form and warrant)
DELIVERABLE_3_PARTITION     = CONFIRMED
FENCE_HITS                  = **ZERO** — scanned twice; coupling row halted at
FENCE_ADJACENT_NAMED        = §2.4 coupling display ; CH-8 quoted "HS threshold
                              3/2 / -3/2" ; structural-index inequalities (FA-3)
QUOTATION_INTEGRITY         = 16 / 16 EXACT, all elisions marked
SEALS_VERIFIED              = 13 / 13 OK, each from the artifact's own
                              directory; all 12 consumed digests match target §1
F-1  AXIS_B                 = NOT A THRESHOLD OF RECORD — two displayed values;
                              third supplied by battery :841; clause enforced
                              for Axis A only; [ORIG] CH-2 types it NON-VANISHING
F-2  TH-2_EXTENT            = BINARY, NOT A THRESHOLD — "no third extent
                              exists"; entries are absence/presence of mixing
F-3  SWEEP_ONE_SIDED        = (S-ii) carries `>=` twice and no `<=`; complement
                              returns 46 carriers; 2 confirmed missing
                              thresholds — [AJ] :283 forcing threshold in a
                              DIMENSION, [ORIG] :320 upper threshold in a DEGREE
F-4  S-iv_UNDISCHARGED      = declared, never reported; returns 21 carriers vs
                              the 6 named; FORCING_NOTION_O12SR unexamined
F-5  SWEEP_COUNT            = (S-ii) reproduces at 42, artifact reports 40
BOUNDARY_INSTANCE_COUNT     = ONE — survives; second candidate (A-1) adjudicated
                              IN THE TARGET'S FAVOUR, no parameter, no crossing
EXHAUSTIVENESS              = NOT CERTIFIED — see AF-4, AF-5
VERDICT_PROPOSALS           = NONE ; LENS_TOKENS = NONE ; BINARY-FOR-INDEXED = NONE
CAS                         = NONE RUN — no venv, no import, nothing computed
SWEEP_CUTOFF                = 2026-08-15, this session; terms and extent at §7
alpha_computed              = false
proof_authorized            = false
kappa_record_computed       = false
NOTHING PROPOSED, NOTHING AUTHORED, NOTHING ADOPTED, NOTHING RETIRED.
NO FENCE, GATE, WITNESS, OR V-CLAUSE MOVED. NO GIT.
```
