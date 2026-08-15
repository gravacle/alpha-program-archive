# STAGE 8 — SYMMETRIC AUDIT OF THE ADMISSION AND CERTIFICATION RULES DETERMINATION — O8SR AUDIT V001

## AUDITOR — CODENAME RULES-AUDIT — COMMISSION O8SR — 2026-08-15

DEFAULT-REFUTE. Testimony zero weight; every step re-derived at bytes in a fresh
venv. DETERMINATION ONLY. **This artifact PROPOSES NOTHING, ADOPTS NOTHING,
RECOMMENDS NOTHING.** It displays what it found and what it could not break.

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

OUTPUT-PATH PROBE: `/Users/bgm/MB Work/alpha-program-archive/workspace/
STAGE8_CERTIFICATION_RULES_O8SR_AUDIT_V001.md` and its `.seal.sha256` sidecar —
**both probed ABSENT** (`ls` exit 1 on both) before any write.

TARGET SEAL, verified FROM THE ARTIFACT'S OWN DIRECTORY before any reliance:
`shasum -a 256 -c STAGE8_CERTIFICATION_RULES_O8SR_V001.md.seal.sha256` -> **OK**
(`5da05d533792247a3b42a1d42024be1a35811eb8b756be09d4abba96e4f14112`).

---

## 0. VERDICT IN ONE LINE

```text
**CONFIRMED-WITH-CORRECTIONS overall — but the artifact's HEADLINE FIND IS
REFUTED, and it is refuted at bytes.

THE CORE DETERMINATION SURVIVES INTACT.  The commissioned question — is the
closure blocked by mathematics or by its own rules — is answered soundly.  I
re-derived every symbolic step independently (23/23 PASS, fresh venv) and
re-verified every quoted rule at its sealed source; the rule inventory, the
barrier test, and all three per-point classifications (FP-1 MIXED, FP-2
RULE-IMPOSED, FP-3 RULE-IMPOSED) STAND.  I could not break them.

WHAT FAILS IS THE PROVENANCE HEADLINE.  The build declares "THE HUNTED OBJECT
IS FOUND" — a load-bearing blocking rule of provenance (iii) INHERITED
CONVENTION, NEVER RATIFIED ANYWHERE: the exclusivity of C-L2's certification
type.  IT IS NOT (iii).  At bytes the restriction is a sentence of a SEALED
SPEC CLAUSE (E1 V002 :1141, "so the certification must be in a quadratic
form"), and E1 V002 is sealed, seal-verified, and the very instrument class
the build's own SS6.4 exhibits entering authority tables by name+hash+
SEAL_MATCH.  Under the build's OWN taxonomy that is (ii) ADOPTED BY A SEALED
ACT — and the build itself classes F3-c, another E1 sentence in the same
sealed spec, as (ii).  The taxonomy is applied inconsistently to two sentences
of one sealed document.  What the build actually established, and established
well, is that the clause's STATED RATIONALE does not deductively carry: the
rule is ADOPTED WITHOUT A DISPLAYED DERIVATION.  "Not derived" is not "not
ratified" [audit E3, the two propositions are independent].
AND TWO OF ITS THREE GROUNDS FAIL SEPARATELY.  GROUND 2 ("the clause narrows
itself WITHOUT GROUND") is refuted by ground the build itself consumed:
CERT-A :87-93 derives that on the certification domain the quadratic-form
route is "equivalent-or-stronger" than the Besov route (H^1 SUBSET the Besov
trace domain), and CERT SS3.1 closes on Q = D(h_0) with "the Besov display is
named, not needed."  The narrowing HAS a displayed, audited ground.  GROUND 3
equivocates: S2's ||.||_2 is a norm inside the DEFINITION of a different
quantity, not a CERTIFICATION TYPE at C-L2's site, whose operator-norm
exclusion is object-specific.  Only GROUND 1 stands, and it proves only
"not derived."
THE SECOND FIND SURVIVES.  F3-e — which type S2b demands — is genuinely (iv)
UNLOCATABLE.  I re-ran the sweep UNCAPPED over BOTH corpus roots and found no
instrument ruling it; CERT-A SS4.5 :233-241 independently confirms the
ambiguity is unruled and belongs to the spec author/registrar.

THE LOCALIZATION DELIVERABLE IS INFLATED, EXACTLY ONCE AND MEASURABLY.  The
build reports blindness proper surviving "at FP-1 and FP-3 ONLY — 2 of 3."
The arithmetic is right; the VARIABLE is not.  ORIG's own SS5.1 table names
FP-1's grading variable "carrier count n", annotated by ORIG itself
"(op-grade enclosure is n-UNIFORM)".  A carrier count is not a localization
variable, and the audited claim is ORIG-A's transcription "DEGREE >= 0 IN THE
LOCALIZATION VARIABLE ITS OWN OBSTRUCTION IS GRADED IN".  The build silently
substitutes "the point's own grading variable" and then reports the count
under the LOCALIZATION heading.  Under the claim's own variable,
LOCALIZATION-blindness proper survives at FP-3 ONLY — ONE of three.
AND THE "SURVIVING FORM" IS NOT THIS LANE'S.  ORIG-A already supplied it
verbatim at :211-213 as its CORRECTION REQUIRED, same triple (3/2, 2, 2).
The genuine increment — recasting it as distance to a half-line, which does
answer A3 — is real but small, and is nowhere disclosed as an increment.

NO FENCE WAS TOUCHED.  No lens token, no alpha value, no program-quantity
value, no measured-constant comparison, no authored physics, no git.  No rule
change is proposed, adopted, or recommended — though SS6.2's "cheapest-shaped
act in the inventory" is a costing that contradicts SS6's own declaration
"not a costing", and is the artifact's single closest approach to the fence.
EVERY NEGATIVE HERE IS ONE-SIDED.  Nothing is retired; no witness moves; no
failure point moves; the completion map is untouched.**
```

---

## 1. SEALS RE-VERIFIED INDEPENDENTLY; SWEEP CUTOFF DECLARED

Every file was re-verified by me with `shasum -a 256 -c` **run from the
artifact's own directory**, against its own `.seal.sha256` sidecar, BEFORE any
reliance. I did not accept the build's seal table; I recomputed it.

```text
TARGET (1):   STAGE8_CERTIFICATION_RULES_O8SR_V001.md            OK  5da05d53...
THE BUILD'S 17 CONSUMED FILES:  17/17 OK, zero mismatches, none unverifiable.
  241262ff W3     d05f22be W3-A    a04c446a ORIG   0db4de90 ORIG-A
  806d5ec4 W1     2dcf3167 W1-A    eacd810c W2     d95f4285 W2-A
  e6838ffc CERT   180114a7 CERT-A  afc3a79c MAP    4504cd14 MAP-A
  46846730 E1     80db260f WALL    61c6de58 AUTH   0a10c030 ASMQ
  27bc36ae FHB-A
OPENED BY THIS AUDIT BEYOND THE BUILD'S STOCK (1), seal verified OK:
  STAGE8_T7_E1_SPEC_V002_AMENDMENT_001.md — the sealed append-only AMENDMENT
  to the very spec whose clause C-L2 is under audit.  THE BUILD DID NOT SWEEP
  IT.  I read it in full (210 lines).  See SS5 C-3.
EVERY CLAIMED DIGEST PREFIX RECOMPUTED AND MATCHED, including the build's
  digest-pin resolution 0a10c030 -> STAGE8_ASSEMBLY_QUANTIFIER_V001.md, which
  I confirmed by recomputing that file's sha256 rather than trusting the pin.
```

### 1.1 SWEEP CUTOFF — DECLARED

```text
SWEEP_CUTOFF = 2026-08-15, this session.
ROOTS SWEPT — BOTH, UNCAPPED.  This is the material difference from the build,
  which consumed only the primary root and bounded its central negative to it.
  (R-a) /Users/bgm/MB Work/alpha-program-archive/workspace          1,882 .md
  (R-b) /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
        alpha_fundamental_record_action_cleanroom_v003              2,308 .md
SWEEPS RUN, patterns declared verbatim, BOTH ROOTS, no cap on hit count:
  (u-1) "only permitted certification"
  (u-2) files containing "C-L2" INTERSECT files containing "exhaustiv"
  (u-3) root-B coverage probe: "C-L2" (9 files), "S2b" (5 files)
  (u-4) "S2b" INTERSECT (form-typed|HS-typed|which type|type conflict|rules
        which|resolv)
  (u-5) every file named *AMENDMENT*|*PRINCIPAL_DECISION*|*RATIF*|*BINDING*|
        *SUPERSED*|*ADOPT*, grepped for C-L2 / "only permitted certification" /
        "quadratic form"
  (u-6) "(certification|norm|form).{0,40}(menu|dichotom)" and its converse
  (u-7) "no other (certification|norm|type)" ; "only two (certification|norm|
        type)"
  (u-8) files containing "C-L2" INTERSECT (exclusiv|only permitted|sole
        permitted)
  (u-9) "Besov", every occurrence, both roots
  (u-10) fence scan of the target: alpha-pattern, lens-pattern, fence tokens,
        proposal/recommend/adopt/costing patterns — every hit inspected AT
        BYTES before being called or cleared.
EXCLUDED AT PATTERN LEVEL, UNREAD: every register / tracker / road / plan /
  continuation file.  QUESTIONSSETTLED_REGISTER_V001.md surfaced as an
  incidental grep hit ONCE and was NOT opened.  "Q-..." tokens
  EXPECTED-UNLOCATABLE, carried as opaque labels, never chased.  Artifacts
  sealed after this commission's fire time UNSWEPT.  No git.
THE NEGATIVES THIS AUDIT CARRIES, and their exact bound: (u-2) returned ZERO
  files in EITHER root pairing "C-L2" with "exhaustiv"; (u-4)/(u-8) located NO
  instrument ruling which type S2b demands; (u-6)/(u-7) located no derivation
  that any certification-type menu is closed.  These are ABSENCES OF DISPLAY
  over both roots at the patterns named, not proofs of absence, and are
  reported as such.  They CONFIRM the build's negatives and WIDEN their bound
  from one root to two.
```

---

## 2. THE KILLS — hardest first

### K-1 — THE PROVENANCE DOWNGRADE IS NOT AT BYTES: F3-a's EXCLUSIVITY IS (ii), NOT (iii) — **REFUTES THE HEADLINE FIND**

```text
CLAIM AUDITED (target SS0, SS3.1, SS3.2, SS6.1, FLAG BLOCK), verbatim:
  "THE EXCLUSIVITY OF THE QUADRATIC FORM: **(iii) INHERITED CONVENTION, NEVER
   RATIFIED ANYWHERE.**"
  and SS0: "THE HUNTED OBJECT IS FOUND, AND IT IS AT FP-3.  **A LOAD-BEARING
   BLOCKING RULE WITH PROVENANCE (iii) INHERITED CONVENTION, NEVER RATIFIED
   ANYWHERE.**"

THE BUILD'S OWN CLASS DEFINITIONS (target SS3), verbatim:
  "(i) DERIVED of record (a theorem ...); **(ii) ADOPTED/AUTHORED by a sealed
   act**; (iii) INHERITED CONVENTION never ratified anywhere; (iv) UNLOCATABLE
   at bytes."

THE BYTES.  The restriction is a sentence of E1 V002's clause C-L2, which I
  read at its own source (E1 46846730, seal OK, :1137-1144), verbatim:
    "Norm-based control is unavailable (||[h_0, 1_B]|| = +infinity for
     first-order h_0 against a sharp indicator), so **the certification must
     be in a quadratic form** and the artifact must state WHICH form and WHY
     the operator-norm route is excluded."
  E1 V002 IS A SEALED SPEC.  Its seal verifies OK from its own directory.  It
  is precisely the instrument class the build's OWN SS6.4 exhibits as the
  standing vehicle of sealed acts, entering authority tables "by name and hash
  with SEAL_MATCH".  A sentence of a sealed spec clause is an act of
  authorship performed under seal.  THAT IS THE DEFINITION OF (ii).

THE INCONSISTENCY, INTERNAL TO THE TARGET AND DECISIVE.  The build classes
  F3-c — ANOTHER SENTENCE OF THE SAME SEALED SPEC — as:
    "F3-c  (ii) ADOPTED (E1's own R.3 display fixes the consuming type as HS)."
  Two sentences of one sealed document, both prescriptive, both load-bearing,
  are assigned to different provenance classes.  Nothing at bytes distinguishes
  them on the axis the taxonomy grades.

WHAT THE BUILD ACTUALLY ESTABLISHED, and it is worth keeping: the clause's
  STATED RATIONALE — the word "so" — does not deductively carry without an
  exhaustiveness premise that is displayed nowhere.  I re-derived that and it
  is correct [audit E1/E2, PASS; and my UNCAPPED both-root sweep (u-2) returned
  ZERO files pairing "C-L2" with "exhaustiv", which STRENGTHENS the build's
  negative and widens its bound from one root to two].
THE ERROR IS THE INFERENCE FROM THAT TO (iii).  "The stated rationale does not
  carry" and "the rule was never ratified" are INDEPENDENT propositions
  [audit E3, PASS: a model satisfies the first and falsifies the second].  A
  sealed clause whose accompanying reason is unsound is still a sealed clause.
CORRECT CLASSIFICATION: **(ii) ADOPTED BY A SEALED ACT, WITH NO DISPLAYED
  DERIVATION OF THE RESTRICTION.**  That is a real and reportable defect —
  it is just not the hunted object, and it is not "never ratified anywhere".

WHAT SURVIVES THIS KILL, SAID SO THE KILL IS NOT OVERREAD:
  - FP-3's barrier classification RULE-IMPOSED is **UNAFFECTED**.  An adopted
    rule imposes exactly as an unratified one does; the barrier test SS4.1
    turns on whether mathematics excludes the object, not on the rule's class.
  - The observation itself survives in restated form, and the restatement is
    the build's own SS6.2 (form-1)/(form-2) language: the record contains no
    displayed derivation that the type restriction is forced.
  - The build's SS3.4 (n-4) already bounds its classifications honestly.  This
    kill is not about the bound; it is about the class.
```

### K-2 — GROUND 2 IS REFUTED BY GROUND THE BUILD ITSELF CONSUMED

```text
CLAIM AUDITED (target SS3.2), verbatim heading and body:
  "GROUND 2 — THE CLAUSE NARROWS ITSELF, MID-CLAUSE, **WITHOUT GROUND** [CAS
   R2d]. ... The record treats these as DISTINCT, not synonymous ... So the
   menu the clause itself opens with is already larger than the menu it
   enforces."
  and SS2.3: "The narrowing is internal and **unexplained** (CAS R2d)."

THE GROUND EXISTS, AND IT IS IN THE BUILD'S OWN COMMISSIONED STOCK.
  CERT-A (180114a7, seal OK — the build lists it as ground [CERT-A]), :87-93,
  verbatim:
    "The auditor's independent route (Besov boundary-trace) and the build's
     route (h_0-relative form via the anticommutator flip) differ; **on D(h_0)
     the build's is equivalent-or-stronger (H^1 SUBSET the Besov trace
     domain)**, and the C-L2 clause assigns the WHICH-form naming act to the
     artifact (E1 :1141-1143)."
  CERT (e6838ffc, seal OK) SS3.1 :200-204, verbatim:
    "Besov-type variant, displayed for the clause's '/ Besov-type' branch: ...
     controlled on the Besov space B^{1/2}_{2,1}(R^3) (the sharp trace domain).
     The certification below is stated and closed on Q = D(h_0); **the Besov
     display is named, not needed.**"

THEREFORE: on the certification domain D(h_0) = H^1, the quadratic-form route
  SUBSUMES the Besov route — the inclusion is displayed and the comparison is
  AUDITED ("equivalent-or-stronger ... Judged admissible and superior; no
  deduction", CERT-A :92-93).  A narrowing from {quadratic-form, Besov-type}
  to {quadratic-form} on a domain where the second is contained in the first
  is NOT a narrowing "without ground".  The ground is displayed of record.
THE BUILD QUOTES THE HALF THAT HELPS IT.  It cites CERT SS3.1's "the Besov
  display is named, not needed" — and omits both the inclusion H^1 SUBSET the
  Besov trace domain and CERT-A's "equivalent-or-stronger" finding, which are
  precisely the ground it declares absent.  This is not a sweep gap: CERT-A is
  commissioned ground the build seal-verified and consumed elsewhere.
SECONDARY, AND NOT RELIED ON: the clause's own string is "a QUADRATIC-FORM /
  Besov-type norm".  The build reads the solidus as a disjunction yielding two
  types and presents that reading as a bytes fact ("SENTENCE 1 permits
  {quadratic-form, Besov-type}").  A reading of the solidus as a single
  compound naming one family is available and is not displayed as an
  alternative.  I do not decide the string; the inclusion above is sufficient.
GROUND 2: **REFUTED.**
```

### K-3 — GROUND 3 EQUIVOCATES: A DEFINING NORM IS NOT A CERTIFICATION TYPE

```text
CLAIM AUDITED (target SS0, SS3.2 GROUND 3, CAS R2c, FLAG BLOCK), verbatim:
  "THE SAME SPEC CERTIFIES THE SIBLING QUANTITY G_hs IN A HILBERT-SCHMIDT TYPE
   AT S2 (R2c) — so **the two-element menu is refuted at the spec's own
   bytes**."
  and the CAS label: "the spec's OWN text exhibits at least FOUR certification
   types ... => the two-element menu is refuted at the spec's own bytes".

THE BYTES.  E1 S2 (:696-700), read at source, verbatim AND COMPLETE:
    "S2. G_hs(C, eps)  := |C|_4^{-alpha} . || C(V(a) - V(0))C ||_2
       [SUBTRACTED HILBERT-SCHMIDT DENSITY. MUST be a TWO-TIME (cell-S-matrix)
        object; the equal-time version is FALSE by C6. *** THE EXPONENT alpha
        IS NOT ASSERTED. *** v001 wrote 1/2 without derivation; R-L2b must
        DERIVE it. Until R-L2b closes, alpha is a symbol, not 1/2.]"

TWO DEFECTS, THE FIRST MATERIAL.
 (a) THE EQUIVOCATION.  S2 is a DEFINITION: it defines a quantity whose
     defining expression contains an HS norm applied to C(V(a)-V(0))C.  C-L2's
     menu governs the CERTIFICATION TYPE of a CONTROL ESTIMATE on a DIFFERENT
     object, the commutator [h_0, M(t) (x) S], whose operator-norm exclusion is
     OBJECT-SPECIFIC (||[h_0, 1_B]|| = +infinity for a first-order operator
     against a SHARP INDICATOR).  That another object's definition uses an HS
     norm says nothing about which types are available AT C-L2's SITE.  The
     inference from "the architecture uses four norms across four objects" to
     "the two-element menu at C-L2's site is refuted" does not follow.
     THE BUILD'S OWN CLOSING SENTENCE OF GROUND 3 IS THE DEFENSIBLE READING:
     "THE RESTRICTION IS PER-CLAUSE AND AUTHORED, NOT AN ARCHITECTURE-WIDE
     DICHOTOMY."  That is true and I confirm it.  SS0, the R2c label and the
     FLAG BLOCK assert the stronger claim the ground does not carry.
 (b) THE QUOTE IS TRUNCATED AND PRESENTED AS COMPLETE.  The build cites
     "E1 S2 (:695-701), verbatim" and closes the bracket after "FALSE by C6.]"
     — but :698-700, INSIDE THE CITED RANGE, carry "*** THE EXPONENT alpha IS
     NOT ASSERTED. *** ... alpha is a symbol, not 1/2", dropped without
     ellipsis.  Immaterial to the argument; a quote-integrity defect in an
     artifact whose whole method is quotation at bytes.
GROUND 3: **DOES NOT CARRY THE CLAIM MADE FROM IT.**

NET ON FIND 1, stated exactly: GROUND 1 stands as logic and proves "NOT
  DERIVED"; GROUND 2 is REFUTED (K-2); GROUND 3 overreaches (K-3); and the
  class is (ii), not (iii) (K-1).  **FIND 1 DOES NOT SURVIVE AS "THE HUNTED
  OBJECT".**  It survives as: a sealed-adopted type restriction carrying no
  displayed derivation — which is worth recording and is not what was claimed.
```

### K-4 — THE LOCALIZATION-BLINDNESS COUNT IS INFLATED: FP-3 ONLY, NOT 2 OF 3

```text
CLAIM AUDITED (target SS5.3, CAS R3e, FLAG BLOCK field
LOCALIZATION_BLINDNESS), verbatim:
  "BLINDNESS PROPER (asset degree EXACTLY 0 in the point's grading variable)
   holds at **FP-1 and FP-3 ONLY — two of three** [CAS R3e]."

THE ARITHMETIC IS RIGHT.  I re-derived it: degrees (0, -1, 0), so exactly two
  entries are 0 [audit B6, PASS].  THE DEFECT IS NOT ARITHMETIC.  IT IS THE
  VARIABLE THE COUNT IS TAKEN IN.

THE BYTES.  ORIG's OWN SS5.1 table (a04c446a, seal OK, :643-654) names the
  three grading variables — the column the build's SS5.2 does not reproduce:
    "POINT   THE GRADING VARIABLE          ASSET'S DEGREE
     FP-1    **carrier count n**            0  (op-grade enclosure is
                                               **n-UNIFORM**)
     FP-2    diagonal-symbol degree        -1
             at the volume diagonal
     FP-3    momentum-coincidence degree    0"
AND THE CLAIM UNDER AUDIT IS ABOUT A LOCALIZATION VARIABLE.  ORIG-A (0db4de90,
  seal OK) :173-175 transcribes it verbatim:
    "EVERY CERTIFIED ASSET OF THE CLOSURE HAS DEGREE >= 0 **IN THE LOCALIZATION
     VARIABLE ITS OWN OBSTRUCTION IS GRADED IN**, WHILE EVERY OBSTRUCTION'S
     REQUIREMENT IS STRICTLY ON THE LOCALIZED SIDE."

THE SUBSTITUTION.  The build's SS5.3 silently replaces "the localization
  variable" with "the point's grading variable", and then reports the resulting
  count under a deliverable headed THE LOCALIZATION-BLINDNESS CLAIM and in a
  FLAG BLOCK field named LOCALIZATION_BLINDNESS.  A reader of that field takes
  "blindness proper ... 2 of 3" to be a statement about localization.  It is not.
  FP-1's variable is a CARRIER COUNT.  Degree 0 in a carrier count is
  n-UNIFORMITY — ORIG's own annotation says so in the same cell — and
  n-uniformity is a property in the carrier-size direction, not in a
  localization direction.  FP-2's and FP-3's variables ARE localization-type
  (a diagonal-symbol degree; a momentum-coincidence degree), and of those two
  only FP-3 carries degree 0.
CORRECTED COUNT: **LOCALIZATION-blindness proper survives at FP-3 ONLY — ONE
  of three.**  Under the substituted "own grading variable" reading the build's
  2-of-3 is arithmetically correct, and must then be stated WITHOUT the word
  localization anywhere near it.
NOTE, IN THE BUILD'S FAVOUR: this does NOT restore ORIG's universal, which
  stays refuted; and it does not disturb the SHORTFALL triple (3/2, 2, 2),
  which I re-derived exactly [audit B1-B4, PASS].  It narrows a surviving
  sub-family from two members to one.
```

### K-5 — THE "SURVIVING FORM" WAS ALREADY SUPPLIED BY ORIG-A, VERBATIM

```text
CLAIM AUDITED (target SS5.2 heading), verbatim:
  "### 5.2 The form that survives — **derived**, and it meets BOTH objections"
  "**THE SURVIVING STATEMENT: AT EACH OF THE THREE FAILURE POINTS, THE ADMITTED
   ASSET'S DISPLAYED DEGREE IN THAT POINT'S OWN GRADING VARIABLE LIES OUTSIDE
   THAT POINT'S OWN ADMISSIBLE HALF-LINE, AT POSITIVE DISTANCE — (3/2, 2, 2)
   RESPECTIVELY.**"

ORIG-A ALREADY STATED IT.  ORIG-A :210-213, verbatim, under its own heading
  "CORRECTION REQUIRED":
    "A form the bytes DO carry: **'AT EACH FAILURE POINT THE CERTIFIED ASSET'S
     DISPLAYED DEGREE IN THAT POINT'S OWN GRADING VARIABLE FALLS SHORT OF THAT
     POINT'S OWN DISPLAYED THRESHOLD BY A POSITIVE MARGIN (3/2, 2, 2).'**"

The two sentences are the same sentence: same scope ("at each failure point"),
  same variable clause ("in that point's own grading variable"), same triple.
  "Lies outside that point's own admissible half-line, at positive distance"
  is a restatement of "falls short of that point's own displayed threshold by
  a positive margin".
THE GENUINE INCREMENT IS REAL AND SMALL: recasting the margin as a DISTANCE TO
  A SET makes the measure orientation-free and therefore answers ORIG-A's A3
  objection (that the reported triple mixed need-asset and asset-need).  I
  confirm the increment works [audit B1-B4].  It is one definitional move on a
  sentence already of record.
THE DEFECT IS DISCLOSURE.  The build cites ORIG-A F-2, F-3 and A3 by name, and
  SS5.1 even quotes F-2's refutation — but nowhere states that F-2's CORRECTION
  REQUIRED already carried the surviving form.  CH-3 ledgers the definition as
  "YOURS (the definition), PROVABLE (the three values)" without naming the
  prior statement it is a variant of.  Under this lane's own standard for
  F1-b — where it correctly flags a downstream hardening of an upstream
  inventory word — the same standard applies here in reverse.
```

---

## 3. THE RULE-BLAMING HUNT — WHAT I COULD NOT BREAK

This commission's designated failure mode is RULE-BLAMING: a barrier called
RULE-IMPOSED where the mathematics actually forbids the object. For **every**
RULE-IMPOSED call I demanded the display that an object of the required kind is
NOT excluded by any theorem of record, and I was prepared to kill the call if
that display were missing or rested on absence-of-proof. **The calls survive.**
One of them survives on a positive display that is stronger than the build
claims for it.

### 3.1 The barrier test itself

```text
The build's criterion (SS4.1) — MATHEMATICAL iff the displayed impossibility
"QUANTIFIES OVER ALL OBJECTS OF THE REQUIRED KIND ... and its proof does not
consume an admission or certification rule as a premise" — is the correct
criterion and is stated BEFORE it is applied, which is the right order.  The
build ledgers its threshold as unforced at CH-1 and displays the looser reading
and what it would yield.  I attacked the criterion and could not fault it: the
looser reading (counting "impossible on the only permitted route" as
MATHEMATICAL) is self-defeating here exactly as CH-1 says, because "the only
permitted route" IS the rule under audit.  CRITERION: SOUND.
```

### 3.2 FP-2 — the strongest of the three calls, and stronger than claimed

```text
DEMANDED: a display that an object of the required kind is NOT excluded.
FOUND, POSITIVE, AT BYTES.  E1 C6 (:353-358), read at its own source, verbatim
  — the sentence IMMEDIATELY AFTER the divergence the barrier rests on:
    "Equal-time localization of the 3-D massless Dirac sea fails
     Shale-Stinespring: ||[C, 1_B]||_2 = +infinity; a Lipschitz cutoff still
     gives int d^3 r . r^2/r^6 = int dr/r^2, divergent.  **Only TWO-TIME /
     scattering-type objects, where the cell time integration supplies the
     missing decay, can work.**"
THIS IS NOT ABSENCE-OF-PROOF.  The record's own frozen input NAMES A KIND THAT
  CAN WORK.  The quantifier of the impossibility is equal-time localizers; the
  complement is not merely unexcluded, it is affirmatively named as viable by
  the same clause.  The build's FP-2 = RULE-IMPOSED call therefore rests on a
  POSITIVE non-exclusion display, which is the strongest form the commission
  asks for.  I could not break it.
AND THE FOUR BLOCKERS ARE RULES, each verified at its own sealed source:
  F2-a the locus ruling — its OWN word is "ADOPTED OF RECORD (binding R5, from
    the independent system)" (E1 :359-366, verified verbatim, exact).
  F2-b the evidence-form rule; F2-c the supplier-class rule; F2-d the
    procedural bar, whose text carries its own release condition on its face.
  The build's sharpest instance is correct and I confirm it: at F2-d the lane
  reached the point where the identification could be made and DECLINED IT BY
  RULE.  A refusal is not a theorem.
FP-2 = RULE-IMPOSED: **CONFIRMED.**
```

### 3.3 FP-3 — the call survives K-1 unchanged

```text
DEMANDED: for each of the four displayed impossibilities, what does its
quantifier range over?  I checked all four at bytes.
  (1) OPERATOR-NORM EXCLUSION — quantifier: the operator-norm TYPE.  Excludes
      one type.  DERIVED, mechanism-exact.  The build says so and does not
      overreach: it calls this "the one place at FP-3 where mathematics
      genuinely closes a door."  CORRECT.
  (2) SEA-SANDWICH — quantifier: translation-invariant inputs.  W-3's own
      escape clause names the complement (:386, :701: an input that "is NOT
      translation-invariant").  And the invariance is supplied by the admission
      rule, not by the commutator: H(c)'s functional reads psi only through
      ||h_0 psi|| and ||psi||, both invariant.  I re-derived this.  CORRECT.
  (3) GRONWALL — quantifier: the certified class, by its own headline (W-3 SS7
      :568, verbatim: "THE FORM CLASS IS NOT CLOSED UNDER ITS OWN PROPAGATION
      GRONWALL").  A statement about the class.  CORRECT.
  (4) beta KERNEL — quantifier: objects whose cell-dependence is constant, and
      the constancy is CERT u-b's ("holds for the indicator of ANY measurable
      region ... every radius").  I re-derived the reduction [audit D1/D2].
      CORRECT.
AND THE RECORD SAYS IT IN ITS OWN WORDS.  W-3 :682-684, verified at bytes
  (the build renders it in capitals; the source text is lower-case, content
  identical): "(o4) ... is now shown to be NOT A CONSEQUENCE of (o1)-(o3) AT
  ANY STRENGTH. Therefore W-3 CANNOT LAND ON C-L2's OWN PERMITTED ROUTE ALONE:
  its landing requires an input from outside the form class."
NO IMPOSSIBILITY OF RECORD RANGES OVER AN OBJECT OF THE REQUIRED KIND AS SUCH.
FP-3 = RULE-IMPOSED: **CONFIRMED — and unaffected by K-1**, since the barrier
  test turns on whether mathematics excludes the object, not on whether the
  blocking rule is class (ii) or class (iii).
```

### 3.4 FP-1 — MIXED confirmed; one sentence overstates (see C-1)

```text
THE ROUTE-LEVEL IMPOSSIBILITY IS REAL AND EXACT.  I re-derived it independently:
  (4n^3 k)/(2n^3) = 2k exactly, n-free, and lim 2k = 2k != 0 [audit A1/A2].
THE FAILURE-POINT CALL "RULE-IMPOSED-BY-ABSENCE" is honestly named — the build
  puts the word ABSENCE in the label itself — and the NET call is MIXED, not
  RULE-IMPOSED.  I re-derived the W1-AUDIT sufficiency exactly: capped piece
  = 4 n^{3-delta}; q=2 piece = 2c n^{3-delta}(ln2 + (delta/2)ln n); total is
  sub-volume [audit A3/A4/A5, all PASS, exact].  The W1-AUDIT KILL 1 and KILL 2
  characterisations are accurate at bytes (W1-A :138, :250, :282, :338-339).
FP-1 = MIXED: **CONFIRMED**, subject to C-1.
```

### 3.5 Everything else I verified at bytes and could not fault

```text
- The C-L2 clause quote: verbatim AND COMPLETE, exact, character for character.
- The C6 + ADOPTED locus refinement quote (E1 :353-366): exact.
- S2b (:702-708) and R.3 (:811-813): exact; "A(0) IS the C-L2 error" is
  confirmed by E1's own parenthetical "(where A(0) is the C-L2 error, NOT a
  baseline norm)".
- WALL's rank cap (:302) and the F1/F2/F3 verdict block: quoted verbatim-exact.
- CERT SS2.3's type-conflict statement, CERT ch-5's "the spec author/registrar
  owns it", CERT ch-2's "Tag: YOURS (naming)": all exact.
- MAP's hardening of the inventory word: confirmed at MAP :352 ("F1's only
  escape is the sub-volume rate"), which is exactly the hardening the build
  flags.  The build's criticism of MAP here is correct.
- FIND 2 ((iv), which type S2b demands): CONFIRMED.  My UNCAPPED both-root
  sweep (u-4, u-8) located no instrument ruling it, and CERT-A SS4.5 :233-241
  independently confirms — "The build carries both readings without repairing
  the clause — the correct posture; the ambiguity belongs to the spec
  author/registrar."  The build's posture (CH-7, adopt neither) is correct.
- FP-S: correctly held outside the barrier test; FS-a is a quantifier rule and
  the build moves it in neither direction.  The 0a10c030 pin resolves as
  claimed — I recomputed the digest rather than trusting it.
- ALL 26 of the build's CAS results reproduce.  My independent battery, written
  from the record's displayed degrees rather than copied from the build's
  script, returns 23/23 PASS and contradicts none of them.
```

---

## 4. CORRECTIONS

```text
C-1  SS4.2 OVERSTATES BY ONE STEP.  Verbatim: "IS AN OBJECT OF THE REQUIRED
     KIND EXCLUDED?  **NO — and the record positively derives the opposite.**"
     The W1-AUDIT result is an IMPLICATION, not an existence: IF a q=2 counting
     bound N_n(s) <= c n^{3-delta} s^{-2} holds, THEN the layer-cake total is
     sub-volume.  Its hypothesis carries free parameters c and delta and is
     nowhere a theorem of record [audit A6, PASS: the conclusion depends on
     both symbols].  Exhibiting a SUFFICIENT CONDITION for X is not a
     derivation that X is unexcluded.
     THE BUILD'S OWN OTHER WORDINGS ARE CORRECT: SS0 says "SUFFICES", the label
     says "RULE-IMPOSED-BY-ABSENCE", and SS4.2's own closing line says "a
     SUFFICIENT CONDITION for it is exhibited of record."  Only the quoted
     sentence overstates.  FIX: strike "positively derives the opposite";
     the surrounding paragraph already says the right thing.  The MIXED verdict
     at FP-1 is unaffected.

C-2  UNDECLARED SECOND AND THIRD NEGATIVES.  SS1.1 declares "**THE ONE
     NEGATIVE THIS SWEEP CARRIES**" and bounds only the (s-3) exhaustiveness
     absence.  But SS4.3 carries "No mathematics excludes a volume-diagonal-
     supported asset", SS4.4 carries "No impossibility is displayed for an
     object of the required kind as such", and SS3.3 carries the (iv) absence —
     three further absence-of-display negatives of the same shape.  SS3.4 (n-4)
     bounds the PROVENANCE classifications but not the SS4 barrier negatives.
     FIX: bound all four in SS1.1, or drop the word "ONE".
     (My own uncapped both-root re-run supplies the wider bound for all of
     them; see SS1.1 of this audit.)

C-3  SWEEP INCOMPLETENESS — LOCATED, OPENED, AND CLOSED HERE.  The build's
     (s-4) revision-discipline sweep did not surface
     `STAGE8_T7_E1_SPEC_V002_AMENDMENT_001.md` — a SEALED, APPEND-ONLY
     AMENDMENT to E1 V002, the very spec whose clause C-L2 the commission puts
     under audit, sitting in the primary root under a filename containing
     "AMENDMENT".  Given that the build's central find is that a clause of that
     spec was "NEVER RATIFIED ANYWHERE", an unopened amendment to that spec is
     the single most load-bearing thing its sweep could have missed.
     **I VERIFIED ITS SEAL (OK) AND READ IT IN FULL.**  It carries U1/U2/U3 and
     the projection-tail conditional into E1's governing chain, append-only,
     "governs ONLY BY ADDING OBLIGATIONS".  It contains **ZERO** occurrences of
     C-L2, S2b, "certification", "quadratic", or "Besov".
     **MATERIALITY: NONE.**  The build's negative survives the omission.  But
     the omission is real and is recorded, because "an unlocated source is not
     the same as an absent one" and the build's negative was stated as if the
     sweep had been complete.

C-4  THE ARTIFACT CONTRADICTS ITS OWN NO-COSTING DECLARATION.  SS6 preamble
     :793, verbatim: "It is **not a proposal, not a recommendation, not an
     adoption, and not a costing.**"  SS6.2 :840-842, verbatim:
       "This is **the cheapest-shaped act in the inventory**, because it
        decides between two readings BOTH ALREADY DISPLAYED of record; it
        authors no new object.  It is also **the one whose absence most changes
        what FP-3's failure even IS** (SS3.3)."
     Those two sentences ARE a costing and a priority ranking, applied to one
     act singled out of the inventory, and together they supply exactly the two
     premises a recommendation would need — lowest cost, highest consequence.
     **I DO NOT FIND THIS SUFFICIENT TO VOID THE ARTIFACT**: no deontic verb is
     used, the act described is a RULING BETWEEN TWO READINGS ALREADY OF RECORD
     rather than a change of rule content, and SS6 disclaims three times
     (:791-797, :836, :905-909).  But it is the artifact's single closest
     approach to the display-only fence, and a stricter registrar could read it
     the other way.  FIX: strike both sentences or restate them as pure form
     ("this act authors no new object; it selects between two displayed
     readings"), which is the load-bearing content and carries no ranking.

C-5  A PROFILE-DEPENDENT NUMBER IS GIVEN VERDICT PROMINENCE.  SS0 :74 and the
     FLAG BLOCK :1418-1419 report the certified object's localized majorant as
     having "a strict interior maximum at r = 1/sqrt(2)" with no mention of the
     profile it came from.  That value is an artefact of CH-4's UNFORCED
     instrument f(rho) = exp(-rho^2).  I re-derived: the equally admitted H^1
     radial profile f(rho) = exp(-rho^2/2) gives stationary point **1**, not
     1/sqrt(2) [audit C4, PASS].
     THE QUALITATIVE CONCLUSION IS PROFILE-INDEPENDENT AND STANDS: the exact
     object's localized majorant is not flat in r, under both profiles [audit
     C2/C5, PASS], and the build's CH-4 correctly says the conclusion is
     profile-independent.  The NUMBER is not.  FIX: the value must not appear
     in SS0 or the FLAG BLOCK without its profile attached, since a reader of a
     flag block takes it for a property of the certified object.

C-6  THE HALF-LINE DEFINITION MISSTATES THE ONE OPEN ROW.  SS5.2 defines the
     shortfall as "the DISTANCE from the admitted asset's displayed degree to
     that point's own admissible half-line (**zero if inside**)".  FP-2's
     half-line is OPEN — "strict < -3" — so the distance is an infimum that is
     not attained, and at the boundary point -3 the distance is 0 while -3 is
     NOT admissible [audit B7, PASS].  NON-MATERIAL at the actual degree (-1,
     distance 2), and the triple (3/2, 2, 2) is unaffected.  FIX: state the
     FP-2 row's distance as an infimum, or say "zero if inside; note the FP-2
     half-line is open, so distance zero does not imply admissibility."

C-7  TWO LINE ANCHORS ARE WRONG (contents are right).  SS2.1 cites the WALL F1
     verdict at "WALL :408-413" and "The four tasked quantities are traces and
     HS masses" at "WALL :400-407".  At bytes the F1 verdict is **WALL
     :402-407** and the traces/HS-masses sentence is **WALL :300-301**;
     :408-413 is the F2 block, a different rule.  Both QUOTES are
     verbatim-exact — only the anchors point elsewhere.  (The rank cap anchor
     :302 is correct, so the numbering base is not the issue.)  Minor: E1 R.3
     is at :811-813, cited :810-813.  FIX: repoint.  In an artifact whose
     method is "every rule quoted AT its sealed source", the anchor is part of
     the claim.

C-8  A RESERVED SYMBOL IS EXTENDED BEYOND ITS RECORD DEFINITION.  CAS R5b
     extends the beta kernel fact "to the radius", using beta for a RADIUS
     exponent.  At bytes beta is defined only as the exponent of |C|_4 (E1 S2b
     :702-707: "beta is derived with alpha under R-L2b"), and reading the
     admitted bound as r^beta . G is an ansatz nowhere of record.  The result
     is labelled CORROBORATION and nothing load-bearing rests on it, and it is
     a KERNEL (no-information) fact rather than a supply — so F3-d's
     "PRODUCTION PROHIBITED" is not breached in substance.  But the symbol
     reuse is not of record and no CHOICE LEDGER entry flags it.  FIX: rename
     the radius exponent, or ledger the reuse.

C-9  THE CAS SCRIPT DIGEST IS NOT INDEPENDENTLY REPRODUCIBLE.  The build pins
     its script at `a8094e4e...` but the file lives in another session's
     scratchpad and is not in either corpus root, so the digest cannot be
     checked at path.  I did not treat this as a defect in the RESULTS — I
     re-derived every result independently instead, and all reproduce — but the
     pin is unverifiable and should be read as such.
```

---

## 5. FENCE-SCAN OF THE TARGET — every alpha-pattern hit inspected at bytes

```text
FENCE TOKENS: present and correct, at head (:13) and in the FLAG BLOCK
  (:1370-1372): alpha_computed = false ; proof_authorized = false ;
  kappa_record_computed = false.  DECLARED TWICE, NEVER CONTRADICTED.

ALPHA-PATTERN HITS — 11 total, ALL inspected at bytes, ALL CLEARED:
  :13, :1370          the fence token itself.
  :16, :130, :133,    corpus PATHS (alpha-program-archive;
  :893                 alpha_fundamental_record_action_cleanroom_v003;
                       alpha_supervision) — path strings, not quantities.
  :273, :404          inside VERBATIM E1 quotes: |C|_4^{alpha} (R.3) and
                       |C|_4^{-alpha} (S2).  Reproduced symbols in a quotation.
  :280                "beta is reserved to R-L2b and 'derived with alpha'
                       (E1 S2b)" — a quotation of the reservation itself.
  :751, :752          "alpha.n-hat" — the DIRAC ALPHA MATRIX in CERT's
                       of-record distributional display.  Not the program alpha.
  :993, :1056         CAS comments naming the same two E1 symbols.
  NO VALUE OF alpha IS PRODUCED, ASSERTED, ESTIMATED, OR COMPARED ANYWHERE.

LENS TOKEN: NONE.  No lens/register/tracker/road/plan/continuation token
  appears in the target, and none was consumed by it.
NUMBERS: every numeral in the target is one of — a sealed artifact's own
  displayed degree or threshold reproduced (0, -1, 3/2, -3, -2), an exact
  symbolic result of an identity (2k, 4n^3, 4 n^{3-delta}, beta = 0), a line
  or digest reference, or an instrument's own property (1/sqrt(2) — see C-5).
  NO number is offered as a value of a program quantity.  NO measured constant
  appears.  NO measured-constant comparison is made.  NO float is a premise.
KAPPA: no kappa value, rate, or record computation anywhere in the target.
GATES / FENCES / QUANTIFIERS: none moved.  FP-S's one-way quantifier wall is
  respected in both directions.  MAP SS3.4/SS3.5 untouched.
WITNESSES: none created, none retired, none moved.
GIT: not used by the build; not used by this audit.
```

---

## 6. AUDIT CAS BATTERY — INDEPENDENT, fresh venv, sympy 1.14.0

Written from the record's own displayed degrees and the record's own displayed
identities — **not copied from the target's script**. Fresh venv
`o8auditvenv`; sympy 1.14.0 (the same version the target ran under, so no
version difference can explain agreement or divergence). Script digest
`305be1f4d156a513e61b443a661b1e37ea7f0851407ce9f1a80d9d157ef2a393`.
**23 checks, 23 PASS, 0 FAIL.** Exact symbolic only.

```text
PASS A1 rank x op = 4n^3*k over same-power carrier 2n^3 equals 2k, n-free
PASS A2 2k is not o(1): limit_{n->oo} 2k = 2k (nonzero for k>0)
PASS A3 capped piece = 4*n^(3-delta) exactly
PASS A4 q=2 piece = 2*c*n^(3-delta)*(log2 + (delta/2)*log n) exactly
PASS A5 total/n^(3-(delta-eps)) -> 0 (eps=1/4, delta=1/2, c=1): SUB-VOLUME
PASS A6 AUDIT: the derivation is an IMPLICATION - its hypothesis
        N_n(s) <= c*n^(3-delta)*s^-2 is a PREMISE, not a theorem of record
PASS B1 dist(0,[3/2,oo)) = 3/2
PASS B2 dist(-1,(-oo,-3)) = 2
PASS B3 dist(0,(-oo,-2]) = 2
PASS B4 all three strictly positive
PASS B5 headline universal 'degree >= 0' FALSE at FP-2
PASS B6 degree exactly 0 holds at FP-1 and FP-3 only (2 of 3) under the
        "point's own grading variable" reading
PASS B7 AUDIT DEFECT: at the FP-2 boundary point -3 the distance is 0 yet -3
        is NOT admissible (strict < -3)
PASS C1 admitted bound is r-flat: d/dr = 0 and r not free
PASS C2 sphere mass for f=exp(-rho^2) is NOT r-flat
PASS C3 its unique positive stationary point is 1/sqrt(2)
PASS C4 AUDIT: profile f=exp(-rho^2/2) (equally admitted, H^1 radial) gives
        stationary point 1 != 1/sqrt(2) => the VALUE is profile-dependent
PASS C5 the QUALITATIVE conclusion (non-flat in r) is profile-independent
PASS D1 two-cell reduction: log((V1/V2)^beta) = beta*log(V1/V2)
PASS D2 beta*L = 0 with L != 0 has unique solution beta = 0
PASS E1 '~OP therefore QF' is INVALID without an exhaustiveness premise
PASS E2 with (OP or QF) supplied the inference is VALID
PASS E3 AUDIT: 'the stated inference does not carry' and 'the rule is
        unratified' are independent propositions

AUDIT BATTERY: 23/23 PASS
```

```text
AGREEMENT WITH THE TARGET: on every step both batteries compute, they AGREE.
  I found no arithmetic error, no symbolic error, and no CAS check whose label
  overstates its own condition — the defect ORIG-A caught in ORIG (F-3) does
  NOT recur here.  Every one of the target's 26 checks is a true statement of
  what its code tests.
DIVERGENCE FROM THE TARGET: none at the level of computation.  A6, B7, C4 and
  E3 are ADDITIONAL checks the target did not run, and each supports a
  correction or a kill above rather than contradicting a target result.
```

---

## 7. VERDICT, PER DELIVERABLE AND OVERALL

```text
D1  THE RULE INVENTORY AT BYTES        = **CONFIRMED-WITH-CORRECTIONS**
    Ten live rules plus one quantifier rule, each located and each quoted
    accurately at its sealed source.  I re-read every quote; all are
    verbatim-exact in content.  Corrections: C-7 (two wrong line anchors),
    K-3(b) (the S2 quote is truncated and closed as if complete).

D2  THE PROVENANCE OF EACH RULE        = **REFUTED at its headline find**
    FIND 1 — C-L2's exclusivity as "(iii) INHERITED CONVENTION, NEVER RATIFIED
      ANYWHERE" — **REFUTED.**  Correct class is (ii) ADOPTED BY A SEALED ACT
      (K-1); GROUND 2 refuted (K-2); GROUND 3 overreaches (K-3).  What survives
      is the weaker and still-useful statement that the restriction carries no
      displayed derivation.
    FIND 2 — F3-e as (iv) UNLOCATABLE — **CONFIRMED**, and independently
      corroborated by my uncapped both-root sweep and by CERT-A SS4.5.
    THE REST OF THE TABLE — F1-a, F1-c, F2-a..F2-d, F3-b, F3-c, F3-d, FS-a —
      **CONFIRMED** at bytes.  F1-b's "ONLY" carries the same (iii)-vs-(ii)
      defect as K-1 in miniature; the build's own CH-6 already ledgers that
      classification as marginal and immaterial, which is the correct posture.

D3  THE BARRIER TEST, PER FAILURE POINT = **CONFIRMED-WITH-CORRECTIONS**
    FP-1 MIXED — CONFIRMED (correction C-1, one overstating sentence).
    FP-2 RULE-IMPOSED — CONFIRMED, on a POSITIVE non-exclusion display that is
      stronger than the build claims for it (SS3.2 of this audit).
    FP-3 RULE-IMPOSED — CONFIRMED, and unaffected by K-1.
    FP-S — correctly excluded from the test.
    THE COMMISSIONED QUESTION IS ANSWERED SOUNDLY.  I hunted rule-blaming
    specifically and found none: no barrier is called RULE-IMPOSED where the
    mathematics forbids the object.

D4  THE LOCALIZATION-BLINDNESS CLAIM    = **CONFIRMED-WITH-CORRECTIONS on the
    arithmetic; REFUTED on the blindness count and on the attribution**
    The refutation of ORIG's universal STANDS and is correctly re-derived.
    The shortfall triple (3/2, 2, 2) STANDS exactly (corrections C-6, and the
    orientation fix genuinely answers ORIG-A's A3).
    "Blindness proper ... 2 of 3" — **REFUTED** (K-4): under the claim's own
    LOCALIZATION variable it is FP-3 only, 1 of 3, because FP-1's grading
    variable is a carrier count and its degree-0 entry is n-uniformity.
    "The form that survives — derived" — **REFUTED as attribution** (K-5):
    ORIG-A supplied it verbatim; the increment is the orientation recast only.
    SS5.4 (the blindness is created at the admission step) — CONFIRMED as to
    its qualitative content, subject to C-5 on the number.

D5  DISPLAY ONLY, NO PROPOSAL           = **CONFIRMED-WITH-CORRECTIONS**
    No rule is proposed, adopted, recommended, or changed.  No alternative
    certification type is named as viable.  The three refusals the build
    records as correct (CERT ch-5, W-3 g-3, W-2's refusal to form the cell)
    ARE correct and I confirm them.  Correction C-4: SS6.2's "cheapest-shaped
    act" is a costing that contradicts SS6's own "not a costing" and is the
    single closest approach to the fence.  NOT sufficient to void the artifact.

OVERALL = **CONFIRMED-WITH-CORRECTIONS**, with D2's FIND 1 REFUTED.
  The determination the commission asked for is sound and survives a hostile
  re-derivation at bytes.  The artifact's own headline — that the hunted
  object was found — does not.  Nine corrections; five kills; no fence touched;
  every negative one-sided.
```

---

## 8. CHOICE LEDGER (commission O8SR AUDIT; every unforced choice, classified)

```text
CH-1 TREATING A SEALED SPEC CLAUSE AS PROVENANCE (ii).  This is the hinge of
     K-1.  FORCED-BY-THE-TARGET'S-OWN-TAXONOMY: the build defines (ii) as
     "ADOPTED/AUTHORED by a sealed act" and itself classes F3-c, a sentence of
     the same sealed spec, as (ii).  I applied the build's definition
     consistently rather than substituting one of my own.  A reader who thinks
     sealing a spec does not adopt each of its clauses would have to reclassify
     F3-c, F3-d and F2-b..F2-d too, and the build's table would lose most of
     its (ii) entries.  Tag: FORCED-BY-GROUND.
CH-2 NOT VOIDING THE ARTIFACT OVER SS6.2's COSTING.  UNFORCED, and it is the
     closest call in this audit.  Grounds for voiding: the commission says a
     lane that recommends a rule change voids its artifact, and "cheapest ...
     most changes what the failure even IS" supplies a recommendation's two
     premises.  Grounds for the reading I took: no deontic verb; the act
     described selects between two readings ALREADY of record rather than
     changing rule content; SS6 disclaims three times.  BOTH READINGS ARE
     DISPLAYED so the registrar may take either.  Tag: YOURS, alternative
     displayed.
CH-3 READING FP-1's GRADING VARIABLE AS NON-LOCALIZATION (K-4).
     FORCED-BY-GROUND: ORIG's own SS5.1 table names it "carrier count n" and
     annotates the degree-0 entry "(op-grade enclosure is n-UNIFORM)", and
     ORIG-A transcribes the audited claim as ranging over "THE LOCALIZATION
     VARIABLE".  I did not supply either word.  Tag: FORCED.
CH-4 THE SECOND RADIAL PROFILE exp(-rho^2/2) IN AUDIT CHECK C4.  UNFORCED —
     any second admitted H^1 radial profile with a different sphere-mass
     maximum serves.  It is an INSTRUMENT of a refutation of the claim that
     1/sqrt(2) is a record datum, and it is itself an admitted state of the
     record's own domain D(h_0).  Tag: YOURS (the profile), PROVABLE (the
     conclusion: the value is profile-dependent).
CH-5 OPENING ONE ARTIFACT BEYOND THE BUILD'S STOCK
     (STAGE8_T7_E1_SPEC_V002_AMENDMENT_001.md).  FORCED by the commission's
     instruction to re-run the provenance sweeps UNCAPPED and by the rule that
     "an unlocated source is not the same as an absent one": a sealed amendment
     to the spec whose clause is called unratified must be read before that
     call can be tested.  Seal verified; read in full; found immaterial and
     reported as immaterial.  Tag: FORCED-BY-COMMISSION.
CH-6 SWEEPING BOTH ROOTS RATHER THAN THE PRIMARY ONLY.  FORCED by the
     commission ("re-run the provenance sweeps UNCAPPED").  Consequence: my
     negatives are bounded across 4,190 .md files in two roots rather than
     1,882 in one.  Tag: FORCED-BY-COMMISSION.
CH-7 CALLING D2 "REFUTED at its headline find" RATHER THAN THE WHOLE ARTIFACT
     REFUTED.  UNFORCED.  Grounds for whole-artifact REFUTED: the headline find
     is what the build presents as the commission's yield.  Grounds for the
     word I took: the commissioned QUESTION is the barrier classification, and
     that survives entirely under hostile re-derivation; ten of twelve
     provenance rows survive; FIND 2 survives.  Refuting the whole would
     misdescribe a determination whose core I could not break.  Tag: YOURS,
     with the alternative displayed.
CH-8 NOT RULING WHETHER C-L2's SOLIDUS ("QUADRATIC-FORM / Besov-type") IS A
     DISJUNCTION.  FORCED: reading a spec clause's punctuation to fix how many
     types it permits would be a construction on the spec, which this lane may
     not perform.  K-2 does not need it — the domain inclusion suffices.
     Tag: FORCED.
ZERO entries in class OPEN.
```

## 9. TOY_SEPARATION

```text
ACTUAL SURFACE — the thing itself; every kill and every correction rests here:
  - The TARGET's own bytes, at a verified seal, read in full (1,464 lines).
  - The RULES at their own sealed sources, re-read by me and not accepted from
    the target's quotation: E1's C-L2 (:1137-1144), C6 + the ADOPTED locus
    refinement (:353-370), S2 (:696-700), S2b (:702-708), R.3 (:811-813);
    WALL's rank cap (:302) and F1/F2/F3 block (:400-419); CERT SS2.3, SS3.1,
    ch-2, ch-5, u-b; CERT-A SS4.5 and :87-93; ORIG SS5.1; ORIG-A F-2/F-3/A3;
    W-3 SS7/SS8; W1-A KILL 1/KILL 2; MAP :352, :416.
  - The record's OWN displayed degrees and thresholds (0, -1, 0; 3/2, -3, -2),
    re-entered to re-run the record's own arithmetic — not modelled.
  - Seventeen consumed seals plus the target's plus one amendment's,
    recomputed by me from each artifact's own directory.

INSTRUMENT, NOT SURFACE — constructed here solely to test a claim:
  - The truth-table entailment checker in E1/E2/E3.
  - The second radial profile exp(-rho^2/2) in C4 (CH-4).
  - The boundary point -3 in B7.
  - The generic symbols k, c, delta, eps, L in A and D.
  NONE models the closure.  NONE stands in for, approximates, or bounds any
  record object.  NO quantity computed from any of them is offered as a value.

WHY THIS IS NOT A TOY: every instrument appears ONLY in the refuting direction
  — to show that a value is profile-dependent (C4), that a definition misstates
  an open set (B7), that two propositions are independent (E3), that a
  sufficiency carries free premises (A6).  Refutation attributes nothing.  No
  kill, correction, provenance call, or verdict in this audit rests on a
  constructed object; each rests on a quotation at a verified seal or on an
  identity in the record's own displayed symbols.  NO TOY IS SUBSTITUTED FOR
  THE ACTUAL SURFACE ANYWHERE.
```

---

```text
FLAG BLOCK — STAGE8_CERTIFICATION_RULES_O8SR_AUDIT_V001
COMMISSION = O8SR | RULES-AUDIT | 2026-08-15 | DETERMINATION ONLY | DEFAULT-REFUTE
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
VERDICT_OVERALL = CONFIRMED-WITH-CORRECTIONS, with D2's FIND 1 REFUTED
VERDICT_D1 = CONFIRMED-WITH-CORRECTIONS (C-7 anchors; K-3(b) truncated quote)
VERDICT_D2 = REFUTED at FIND 1 (K-1, K-2, K-3); FIND 2 CONFIRMED; rest of the
  provenance table CONFIRMED
VERDICT_D3 = CONFIRMED-WITH-CORRECTIONS (C-1); FP-1 MIXED, FP-2 RULE-IMPOSED,
  FP-3 RULE-IMPOSED all STAND under independent re-derivation
VERDICT_D4 = CONFIRMED-WITH-CORRECTIONS on the arithmetic; REFUTED on the
  "2 of 3" blindness count (K-4) and on the attribution of the surviving form
  (K-5)
VERDICT_D5 = CONFIRMED-WITH-CORRECTIONS (C-4)
KILLS = K-1 the (iii) classification is not at bytes: a sealed spec clause is
  (ii) by the target's own taxonomy, applied inconsistently against its own
  F3-c row | K-2 GROUND 2 refuted by CERT-A :87-93 + CERT SS3.1 (H^1 SUBSET the
  Besov trace domain; the quadratic-form route is "equivalent-or-stronger" on
  D(h_0)) | K-3 GROUND 3 equivocates a DEFINING norm for a CERTIFICATION TYPE |
  K-4 LOCALIZATION-blindness survives at FP-3 ONLY (1 of 3), not 2 of 3,
  because FP-1's grading variable is a carrier count | K-5 the "surviving form"
  was already supplied verbatim by ORIG-A :211-213
CORRECTIONS = C-1 "positively derives the opposite" overstates a sufficiency |
  C-2 three undeclared negatives beyond the declared "ONE" | C-3 an unswept
  sealed AMENDMENT to E1 V002 — located, opened, seal-verified, read, and found
  IMMATERIAL | C-4 SS6.2's costing contradicts SS6's "not a costing" | C-5
  1/sqrt(2) is profile-dependent and must not stand unqualified in the verdict |
  C-6 the half-line definition misstates the one OPEN row | C-7 two wrong line
  anchors (contents exact) | C-8 beta reused for a radius exponent, unledgered |
  C-9 the build's CAS script digest is not reproducible at path
RULE_BLAMING_HUNT = RUN AGAINST ALL THREE CALLS; NONE FOUND. For every
  RULE-IMPOSED call the required non-exclusion display exists and was verified
  at bytes; FP-2's is POSITIVE and stronger than the build claims (E1 C6 :356-
  358 names the kind that CAN work). No barrier is called RULE-IMPOSED where
  the mathematics forbids the object.
SEALS = 19/19 OK (target + 17 consumed + 1 amendment opened by this audit),
  `shasum -a 256 -c` run FROM EACH ARTIFACT'S OWN DIRECTORY, before any
  reliance; zero mismatches; every claimed digest prefix recomputed; the
  0a10c030 pin re-resolved by recomputation, not trusted.
SWEEP_CUTOFF = DECLARED (SS1.1: BOTH ROOTS, UNCAPPED, 4,190 .md files;
  patterns u-1..u-10 listed verbatim; register/tracker/road/plan/continuation
  excluded at pattern level, UNREAD; "Q-..." EXPECTED-UNLOCATABLE, noted not
  chased; artifacts sealed after fire time UNSWEPT). The build's central
  negatives are CONFIRMED and their bound WIDENED from one root to two.
CAS = fresh venv o8auditvenv, sympy 1.14.0, 23 checks, 23 PASS, 0 FAIL,
  written independently of the target's script; digest 305be1f4...
  All 26 target results reproduce; no computational divergence found.
FENCES = alpha-pattern hits 11/11 inspected at bytes and CLEARED; no lens
  token; no alpha value; no kappa value; no program-quantity value; no
  measured-constant comparison; no float as premise; no authored physics.
  V_clauses_touched = none ; gates_moved = none ; fences_moved = none ;
  quantifiers_moved = none.
PROPOSED = NOTHING. ADOPTED = NOTHING. RECOMMENDED = NOTHING. No rule changed,
  no route selected, no certification type named as viable, no reading of S2b
  adopted, no object constructed for supply.
FP1_FP2_FP3 = ALL STAND, unmoved by this audit. FP-S untouched; its one-way
  quantifier wall respected in both directions.
WITNESSES = E1_RECORD_KINK_COMMUTATOR_FORM_UNCERTIFIED STANDS |
  SCAD_HS_SCALING_EXPONENT_UNDERIVED STANDS |
  E1_SEA_OFFDIAGONAL_HS_SHARP_RECORD_LOCALIZER STANDS
witnesses_created_here = none ; witnesses_retired_here = none (registrar's act)
MAP_SS3_4_AND_3_5 = UNTOUCHED; {W-1,W-2,W-3} still the unique minimal set.
  K-1 changes the CLASS of the rule that leg inherits, not the leg.
NOT_REFUTED = carried in full. Every negative here is ONE-SIDED. No divergence
  of any closure quantity is exhibited. All consuming quantities remain
  UNDECIDED.
new_numbers_frozen = none. Every constant is exact symbolic; every degree is a
  sealed artifact's own displayed degree, reproduced not computed.
CHOICE_LEDGER = CH-1..CH-8 (SS8): 5 FORCED, 3 YOURS with every alternative
  displayed; ZERO OPEN. TOY_SEPARATION = clean (SS9).
GIT = not used. OUTPUT = ONE artifact + seal sidecar at the commissioned path,
  both probed ABSENT before first write; no existing file edited.
ALL_RESULTS = CLAIMED until the registrar routes; this lane routes nothing.
O8SR_CERTIFICATION_RULES_AUDIT_RESULT = SEALED.
```
