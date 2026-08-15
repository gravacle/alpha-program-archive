# STAGE 8 — U(1)_rel AND ELECTROMAGNETISM: THE IDENTIFICATION AS AN OBJECT
## IDENT-BUILD, commission O14SR, 2026-08-15 — STATUS DETERMINATION ONLY

**THE SUBJECT.** The record's derived compact `U(1)_rel`, and its identification —
or non-identification — with the electromagnetic gauge group. A prior determination
(O4SR) established that this identification stands NO_VERDICT and is fenced across
many files, and that consequently "gauge-active" findings are NOT "EM-active"
findings. That caveat is now load-bearing in at least three separate sealed results.
Nobody has ever established the identification's OWN status as an object. This
artifact does that, and only that.

**WHAT THIS ARTIFACT MAY NOT DO.** It may not decide the identification, argue for
it, or argue against it. No sentence below advances the question in either
direction. Every substantive claim is a claim about what the corpus SAYS, quoted at
its bytes, with its grade recorded. Where the corpus is silent, the silence is
displayed as silence and never filled.

---

## §0 — GROUND, SEALS, SWEEP CUTOFF

### §0.1 SWEEP CUTOFF

```text
SWEEP_CUTOFF = 2026-08-15T20:00:05Z
All counts below are as of this instant. Later writes to either root are
outside this artifact's knowledge and are NOT covered by its counts.
ROOT_A (primary) = /Users/bgm/MB Work/alpha-program-archive/workspace
                   6807 files at cutoff
ROOT_B (cleanroom) = /Users/bgm/Documents/New project/gravity_emergence_evidence_
                   program/alpha_fundamental_record_action_cleanroom_v003
                   7805 files at cutoff
```

### §0.2 SEALS VERIFIED — `shasum -a 256 -c` RUN FROM EACH ARTIFACT'S OWN DIRECTORY

Commission-named ground (8/8 OK):

```text
STAGE8_EM_PARTICIPATION_O4SR_V001.md                            OK
STAGE8_EM_PARTICIPATION_O4SR_AUDIT_V001.md                      OK
STAGE8_OBSTRUCTION_ORIGIN_O6SR_V001.md                          OK
STAGE8_OBSTRUCTION_ORIGIN_O6SR_AUDIT_V001.md                    OK
STAGE8_PARTITION_THEOREM_T16SR_V001.md                          OK
STAGE8_PARTITION_THEOREM_T16SR_AUDIT_V001.md                    OK
STAGE8_TASK4B_LOCAL_MAXWELL_SYMBOL_AND_PLOC_RK_LANE2_V001.md    OK
STAGE8_TASK5_R4_KERNEL_REALIZATION_AND_SYMBOL_CALCULUS_LANE2_V001.md  OK
```

Further consumed ground, seals verified at path (4/4 OK):

```text
STAGE8_DELTAPHI_PI_PROTECTION_DETERMINATION_V001.md             OK
STAGE8_ETHER_COLD_CONFIRM_OPUS_V001.md                          OK
STAGE8_UREL_DETERMINACY_CHECK_OPUS_V001.md                      OK
STAGE8_LOAD_BEARING_HOLONOMY_DERIVABILITY_DETERMINATION_V001.md OK
```

**THE DEFINING SOURCE CARRIES NO SIDECAR SEAL — recorded exactly.** The two files
that DEFINE `U(1)_rel` have no `.seal.sha256` sidecar in either root. They are
instead HASH-LOCKED by executable audit + results JSON (§1.4). Their bytes are
IDENTICAL across both roots, which this artifact verified directly:

```text
PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md
  sha256 = 45f6015c74593fd25f7862aa7bf6407e124f449ff7635dcf2f9d4c2c2303f08f
  IDENTICAL in ROOT_A and ROOT_B (both computed at path)
PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md
  sha256 = 42691711c55b30484be3b4087043c57b8b3cd969043d56248338cc8f1f40a460
  IDENTICAL in ROOT_A and ROOT_B (both computed at path)
```

This is a STATUS fact and is carried into the FLAG BLOCK: the object whose
identification is at issue is defined in files sealed by a different mechanism
(audit-lock) than the artifacts that consume it (sidecar-lock).

---

## §1 — DELIVERABLE 1: WHAT `U(1)_rel` IS, AT ITS DEFINING BYTES

### §1.1 HOW IT ARISES, AND WHAT DERIVES IT

`U(1)_rel` is not posited. It is a QUOTIENT, derived from a stabilizer of the
primitive two-alternative record carrier. Its defining source, quoted:

```text
PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md :12-38 (VERBATIM)
  "Let |0> and |1> be the two alternatives of one primitive comparison
   record. A change of local basis representatives acts by
     (u_0,u_1) in U(1) x U(1),
     |0> -> u_0 |0>,
     |1> -> u_1 |1>.
   The diagonal subgroup
     U(1)_diag = {(u,u)}
   changes only the common representative phase. It changes no projective state
   or public record statistic and is removed by the physical null quotient.
   The surviving comparison group is therefore
     [U(1) x U(1)] / U(1)_diag
       isomorphic to U(1)_rel,
     (u_0,u_1) -> u_1 u_0^(-1)."
```

The corrected companion states the SAME quotient from the stabilizer side, and
is explicit that the statement is ACTIVE, not a passive relabelling:

```text
PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md :31-57 (VERBATIM)
  "The unitary stabilizer that preserves each endpoint ray separately is
     Stab(P_0,P_1) = U(1) x U(1).
   This is an active stabilizer statement. A passive change of basis,
   accompanied by the inverse coordinate change, is only a description change
   and supplies no physical gauge field.
   ... The center
     U(1)_diag = {(u,u)}
   acts as a common phase and is null on projective record statistics. The
   effective active stabilizer is therefore
     Stab(P_0,P_1) / U(1)_diag
       isomorphic to U(1)_rel,
     (u_0,u_1) -> u_1 u_0^(-1)."
```

**WHAT DERIVES IT, exactly.** Three inherited inputs and no more: (i) the
hash-locked primitive two-alternative record carrier, supplying the two durable
endpoint projectors `P_0 = |0><0|`, `P_1 = |1><1|` — "Their existence is
inherited" (STABILIZER_V002 :24); (ii) a DECLARED comparison ORDER — "The order is
a declared comparison convention: it records which endpoint is the reference and
which is the compared alternative. If that convention were removed, endpoint
exchange would add a discrete `Z_2` factor" (STABILIZER_V002 :24-27); (iii) the
physical/response-null quotient, which removes the common phase. Nothing
electromagnetic is among the inputs, and both files say so in their own scope
lines: "It uses no electromagnetic coupling, particle mass, endpoint value, or
candidate alpha equation" (CONNECTION_V001 :7-9); "It evaluates no
electromagnetic response or coupling" (STABILIZER_V002 :11-12).

### §1.2 WHAT IT ACTS ON

It acts on the RELATIVE PHASE of the two endpoint alternatives of one primitive
comparison record — equivalently, on the ordered pair of endpoint rays modulo
common phase. Its generator and character set, at bytes:

```text
CONNECTION_V001 :46-75 (VERBATIM, condensed to the displayed blocks)
  "U_rel(theta) = diag(1, exp(i theta))."
  "Q = |1><1| = diag(0,1)."
  "Q_0 = Q - (1/2) I = diag(-1/2,1/2)."
  "Endpoint exchange sends Q_0 -> -Q_0; it does not produce a second physical
   generator."
  "Continuous characters of U(1)_rel are
     chi_n(theta) = exp(i n theta),  n in Z."
```

A blind cross-lineage verifier confirmed the carrier-level facts independently:

```text
STAGE8_UREL_DETERMINACY_CHECK_OPUS_V001.md :63-67 (seal OK) (VERBATIM)
  "FINDING Q1: CONFIRMED. The physical/response-null (gauge) quotient removes
   U(1)_diag only; the surviving carrier is the full U(1)_rel = [U(1) x U(1)] /
   U(1)_diag; generator Q = |1><1|; character lattice Z. No sealed text in the
   read set removes ker(chi_n) at the group/carrier level — the surviving group
   retains every Z_|n| subgroup."
```

### §1.3 WHAT ITS COMPACTNESS AND ITS RELATIVENESS CONSIST IN

```text
COMPACTNESS consists in: being a quotient of the COMPACT stabilizer
  U(1) x U(1) by the closed central subgroup U(1)_diag. Its operative
  consequence of record is the INTEGER character lattice — "chi_n(theta) =
  exp(i n theta), n in Z" (CONNECTION_V001 :68-72) — booked as
  `primitive_character_lattice = Z` and `relative_character_lattice = Z`.
  Compactness is what makes the character index DISCRETE; nothing else in the
  defining bytes carries that role.

RELATIVENESS consists in: being the quotient BY the common phase, so that only
  the DIFFERENCE u_1 u_0^(-1) survives. The map "is onto and its kernel is
  exactly U(1)_diag, so the quotient contains one compact relative-phase handle
  and no second independent phase handle" (CONNECTION_V001 :40-42). The
  relativeness is therefore the statement that ABSOLUTE endpoint phase is
  response-null and only the ordered DIFFERENCE is record-bearing. Note that
  relativeness is purchased by the DECLARED order (§1.1(ii)): without it a
  Z_2 appears.

DIMENSION: "the relative Lie algebra is one-dimensional: there is one
  independent generator modulo the identity" (STABILIZER_V002 :59-61).
```

### §1.4 THE TWO DEFINING FILES DISAGREE ABOUT LOCALIZATION — RECORDED, NOT RESOLVED

This is a status fact about the defining object itself and is reported because it
conditions everything downstream. `CONNECTION_V001` DERIVES a local comparison
connection; `STABILIZER_V002` — which explicitly RETIRES claims of a predecessor
— makes the same connection CONDITIONAL and undischarged.

```text
CONNECTION_V001 :86-104 asserts it (VERBATIM):
  "Ordinary differentiation of local representatives is not invariant under
   this patch change. A comparison connection a is therefore required:
     D z_1 = (d - i a) z_1,
     a -> a + d theta,
     f = da."
  booked: `local_record_comparison_connection_derived = true`

STABILIZER_V002 :94-115 withholds it (VERBATIM):
  "The result above is pointwise. It does not imply that the relative active
   stabilizer may vary independently at every surface point.
   If a later target-independent theorem establishes all of the following:
     the endpoint comparison frame is local;
     independent smooth relative-frame changes are physically redundant;
     comparison data must be transported between overlapping patches;
   then a connection with D = d - i a, a -> a + d theta is required for
   covariant comparison. Those premises are not established by the current
   sealed sources. Accordingly, this document neither introduces a as a
   physical field nor identifies it with electromagnetism."
  booked: `local_relative_frame_redundancy_derived = false`
          `physical_comparison_connection_derived = false`
          `unique_dynamical_connection_derived = false`

STABILIZER_V002 :3-8 on why (VERBATIM):
  "Version 001 incorrectly promoted passive basis rephasing into a physical
   local gauge freedom. ... Those claims are retired."
```

**STATUS OF THE DISAGREEMENT: UNADJUDICATED IN THE READ SET.** Both files are
live in both roots at cutoff; neither is marked superseded by the other; they
carry different version stems (`CONNECTION_V001` vs `STABILIZER_V002`) so no
version ordering resolves it. This artifact does not resolve it and does not need
to: **on the EM identification itself the two files AGREE exactly** — both book
`identification_with_unique_exterior_EM_connection_derived = false`, and
STABILIZER_V002 additionally states in prose that it "neither introduces `a` as a
physical field nor identifies it with electromagnetism." The disagreement is about
LOCALIZATION, which §3 shows is a NAMED PRECONDITION of the identification, not
the identification itself.

---

## §2 — DELIVERABLE 2: THE IDENTIFICATION'S STATUS, EVERYWHERE THE CORPUS ADDRESSES IT

### §2.1 THE REGISTER — every located place, operative sentence quoted, grade recorded

**I-1 — THE DEFINING SOURCE (CONNECTION side). GRADE: NOT-YET-DERIVED (booked false).**

```text
PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md :118-127, under "Not yet derived:"
  "that this record connection is the unique exterior electromagnetic field;"
booked flag :147
  "identification_with_unique_exterior_EM_connection_derived = false"
```

**I-2 — THE DEFINING SOURCE (STABILIZER side). GRADE: REFUSED IN PROSE + booked false.**

```text
PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md :113-115
  "Accordingly, this document neither introduces a as a physical field nor
   identifies it with electromagnetism."
:11-12  "It evaluates no electromagnetic response or coupling."
booked flag :136  "identification_with_unique_exterior_EM_connection_derived = false"
status line :154  "EM_IDENTIFICATION_OPEN"
```

**I-3 — THE MACHINE RECORD. GRADE: BOOKED FALSE, EXECUTABLE.**

```text
results/primitive_relative_phase_connection_v001.json
  "identification_with_unique_exterior_EM_connection_derived": false
  "overall": "PASS_PRIMITIVE_RELATIVE_PHASE_CONNECTION_EM_IDENTIFICATION_OPEN_
              ALPHA_FALSE"
results/primitive_relative_phase_stabilizer_v002.json
  "identification_with_unique_exterior_EM_connection_derived": false
  "overall": "PASS_ORDERED_ENDPOINT_PROJECTIVE_STABILIZER_ONLY_LOCAL_CONNECTION_
              OPEN_ALPHA_FALSE"
```

The status is carried in the OVERALL PASS STRING itself. A run that derived the
identification could not emit these strings; the openness is part of what "PASS"
means for these two objects.

**I-4 — DELTAPHI. GRADE: NO_VERDICT, with the identification named as THE BLOCKER.**

```text
STAGE8_DELTAPHI_PI_PROTECTION_DETERMINATION_V001.md (seal OK) :429-432, verdict block
  "DeltaPhi_is_holonomy = NO_VERDICT |
     blocker: physical local connection / EM identification remains open in the
     current stabilizer and transport-only records"
:180-186
  "It is not sealed as a Berry phase, spectral flow, index, or already physical
   electromagnetic holonomy. ... The same artifact explicitly leaves local
   physical connection and EM identification open."
```

This is the strongest form in the register: the identification is not merely
unbooked, it is the NAMED OBSTACLE preventing a different result from landing.

**I-5 — ETHER COLD. GRADE: OPEN AND DOWNSTREAM (the identification placed outside
the asked object).**

```text
STAGE8_ETHER_COLD_CONFIRM_OPUS_V001.md (seal OK) :169-174
  "every one of those flags is about the PHYSICAL LOCALIZATION and the EM
   identification — the promotion of the bare invariant to a localized,
   scale-bearing electromagnetic normalization 'on which alpha directly
   depends.' ... the missing pieces are DOWNSTREAM of the asked object, not
   inside it"
:111  "The comparison group is U(1)_rel, and it is derived (record-native) as a
       compact group"
```

**I-6 — LOAD-BEARING HOLONOMY DERIVABILITY. GRADE: EXPLICITLY WITHHELD.**

```text
STAGE8_LOAD_BEARING_HOLONOMY_DERIVABILITY_DETERMINATION_V001.md (seal OK) :236-239
  "The no-unproved-identity rule still limits this bridge to that
   representation; it does not identify the resulting operator with the
   complete physical electromagnetic connection."
```

**I-7 — THE FUNDAMENTAL PRINCIPLE. GRADE: ASSUMED-FOR-DISPLAY — BUT OF THE
LOCALIZATION ONLY, AND WITH THE EM ROUTE EXPRESSLY DISCLAIMED.**

This is the one place an adoption is made, and its exact scope matters:

```text
FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md :48-60 (VERBATIM)
  "The ordinary charged-record branch contains a smooth principal U(1)_rel
   bundle and an auxiliary compact connection a on that bundle. This
   localization and connection are adopted Level-1 field content.
   They are not derived from:
     the common phase of a projective lift;
     a passive basis rephasing;
     the demand to reproduce electromagnetism;
     or the measured value of alpha."
:24-26
  "It is an adopted microscopic theory premise, not a consequence of the sealed
   pre-alpha results."
:28-30
  "The project historically knows the electromagnetic target. Consequently,
   even a complete forward derivation under this principle requires a genuinely
   unused prediction before it can defeat the hindsight objection."
```

**RECORDED PRECISELY:** what is adopted is the BUNDLE AND CONNECTION (the
localization of §1.4), NOT the identification with electromagnetism. The file
explicitly lists "the demand to reproduce electromagnetism" among the things the
adoption is NOT derived from. So I-7 is assumed-for-display on LOCALIZATION and
SILENT-BY-REFUSAL on IDENTIFICATION. It does not supply a YES.

**I-8 — THE LOCALIZATION THEOREM BUILD. GRADE: BLOCKED (the precondition itself
did not land).**

```text
STAGE8_TARGET_INDEPENDENT_LOCALIZATION_THEOREM_BUILD_RESULT_V001.md (UNSEALED —
no sidecar; consumed for STATUS ONLY) :302
  "TARGET_INDEPENDENT_LOCALIZATION_BUILD_VERDICT =
   BLOCKED_BY_MISSING_CANONICAL_BRIDGE"
:169  "prps_premise_2_smooth_relative_frame_redundancy_derived = false | TYPE-U"
:231  "smooth_relative_frame_redundancy_target_independent = false | TYPE-U"
```

**I-9 — THE EM SELECTOR, BARRED. GRADE: QUARANTINED AND DECLARED UNNECESSARY.**

The only place the corpus contemplates USING electromagnetism to select the
comparison group, it quarantines the move and records that the classification
went through without it:

```text
stage8_execution/t0_lineage/core_scripts/34_gate1_comparison_group_v001.py :97-101
  "P3 PASS: unique survivor per axis is U(1); over the three
            adopted axes, the action-character torus. The
            classification used only sealed target-independent
            structure — the quarantined 'because electromagnetism
            is established' selector is UNNECESSARY"
```

This is a BARRED grade and it runs in the NO-CONSUMPTION direction: EM may not be
used as an input to fix the group. Note carefully what it does NOT say — it does
not say `U(1)_rel` is not EM; it says EM was not needed to find `U(1)`.

**I-10 — O4SR, THE PRIOR DETERMINATION. GRADE: NO_VERDICT AND FENCED.**

```text
STAGE8_EM_PARTICIPATION_O4SR_V001.md (seal OK) :563-566
  "the record's U(1) is a DERIVED COMPACT group of the bare record invariant —
   U(1)_rel — and its promotion to an electromagnetic normalization is (i) not
   made, (ii) explicitly fenced, and (iii) named as the open blocker that would
   be needed even to call the phase a HOLONOMY."
:840-842
  "The identification is fenced ... NO_VERDICT of record, and this artifact
   neither makes it, licenses it, nor recommends it."
```

**I-11 — O4SR AUDIT. GRADE: THE PROPOSITION CONFIRMED; ITS DECORATION CORRECTED.**

```text
STAGE8_EM_PARTICIPATION_O4SR_AUDIT_V001.md (seal OK) :246-251
  "56 is the count for the BROADER token 'EM identification', self-excluded. It
   is not the count for the quoted phrase the sentence attributes it to, which
   is 45/44. IMMATERIAL to every verdict: the proposition the count decorates —
   that the EM identification is OPEN and FENCED of record — is independently
   carried by two sealed verdict blocks this audit verified verbatim"
:352  "The record's group is derived and compact; its EM identification is ..."
```

### §2.2 THE GRADE TALLY

```text
NO_VERDICT (explicit)                     I-4, I-10, I-11
BOOKED-FALSE / NOT-YET-DERIVED            I-1, I-3
REFUSED IN PROSE                          I-2, I-6
OPEN-AND-DOWNSTREAM                       I-5
ASSUMED-FOR-DISPLAY (localization only,
  EM route expressly disclaimed)          I-7
BLOCKED (precondition failed)             I-8
BARRED / QUARANTINED (as a selector)      I-9

AFFIRMED (identification made)            NONE LOCATED
DENIED (identification refuted)           NONE LOCATED
```

**Nowhere in either root, at this sweep, does any artifact ASSERT that `U(1)_rel`
IS the electromagnetic gauge group, or that it IS NOT.** Every located treatment
is one of: booked false, refused, deferred, blocked, quarantined, or NO_VERDICT.

### §2.3 THE GUARD SWEEP — UNCAPPED, BOTH ROOTS, SELF-EXCLUDED

All counts exclude this artifact itself. Uncapped `grep -rli` over every file in
each root (not just `.md`), at SWEEP_CUTOFF.

```text
PATTERN                                            ROOT_A      ROOT_B
identification_with_unique_exterior_EM_
  connection_derived      (the canonical flag)          7           7
EM_IDENTIFICATION_OPEN    (status-string form)          4           4
"EM identification = none" (ledger form)               10          16
"no EM identification"     (charter-fence form)        48          93
"EM identification"        (broad token)               60         119
UNION of all guard forms                               78         132
```

**RECONCILIATION WITH O4SR's "56".** O4SR reported 56; its own audit corrected the
attribution (A-3: 56 is the broad token self-excluded, over `.md` only, not the
quoted phrase, which was 45/44). My sweep is BROADER on two axes — all file types,
not only `.md`; and both roots, not only the primary — which is why my primary-root
broad-token count is 60 rather than 57/56. **No contradiction: different declared
scope.** The proposition is unchanged and, per the audit, was never load-bearing on
the count.

### §2.4 WHAT THE GUARDS ACTUALLY FORBID — the question asked, answered exactly

The commission asks whether the guards forbid ASSUMPTION, ASSERTION, CONSUMPTION,
or all three. They are not one guard. There are FOUR distinct mechanisms with
DIFFERENT scopes, and only by separating them is the answer exact.

**G-1 — THE EXECUTABLE FLAG BAR. FORBIDS: ASSERTION. Mechanism: fail-closed
literal + test assertion.**

```text
scripts/audit_primitive_relative_phase_stabilizer_v002.py :94-103, :132-134
  required_false includes
    "identification_with_unique_exterior_EM_connection_derived = false"
  check: "unsupported_statuses_fail_closed": all(phrase in note for phrase in
          required_false)
tests/test_primitive_relative_phase_connection_v001.py :34-36
  self.assertFalse(
      payload["identification_with_unique_exterior_EM_connection_derived"])
```

The document must CONTAIN the literal "= false" string or the audit fails; the
JSON must carry `false` or the test fails. So the identification cannot be
asserted, and it cannot be passed over in silence either — the denial of
derivation is COMPULSORY TEXT. **It forbids assertion; it does not reach
assumption or consumption elsewhere.**

**G-2 — THE PROSE REFUSAL. FORBIDS: ASSERTION, within the issuing document only.**

```text
PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md :113-115 — "this document neither
introduces a as a physical field nor identifies it with electromagnetism."
```

Scope word is "this document". It binds the issuer, not readers.

**G-3 — THE CHARTER FENCE ("no EM identification"). FORBIDS: MAKING THE
IDENTIFICATION IN THE ARTIFACT THAT CARRIES THE FENCE. Mechanism: a self-declared
standing condition, recited in the artifact's own fence line.**

The recurring forms, counted at §2.3, are self-declarations of the form:

```text
"Charter fences live; nothing selected; no smooth import; no EM identification;
 no ..."                                                   (13 + 11 occurrences)
"All charter fences live. No smooth import; no EM identification; no member
 binding; no fixed-point ..."                                    (4 occurrences)
```

This is a DECLARATION BY THE AUTHOR THAT NONE WAS MADE — a certification of
output, not a prohibition on future work. It forbids the fenced artifact from
making the identification. It does not forbid a future authorized artifact from
deriving it.

**G-4 — THE DECLINE ROW S08. FORBIDS: IDENTIFICATION OF THE ALLIED DISCRETE
OBJECT — and this one reaches CONSUMPTION.**

Quoted from a SEALED artifact that recites it (the register itself was NOT opened,
per commission bar on register files):

```text
STAGE8_AXN_FAMILY_BOUNDING_CODEX2_V001.md (seal OK) :280-281
  "S08  discrete incidence connection not identified with EM, Maxwell, smooth
   field, or response:
        obeyed; E2/E3 remain finite carrier geometry only."
STAGE8_B2_GLUING_SCOPE_AND_RUN_CODEX2_V001.md :169, :175
  "| electromagnetic identification | none; S08 remains intact |"
  "S08 remains clean: the finite coframe and response signatures are not
   identified with electromagnetism, gravity, or a smooth public field."
STAGE8_AXN_BUILD_CALCULUS_CROSSCHECK_CODEX2_V001.md :330
  "S08/S26 prevent interpreting the discrete carrier ..."
```

"PREVENT INTERPRETING" is a consumption bar: downstream results may not READ the
discrete carrier as EM. **NOTE THE OBJECT DIFFERENCE, recorded and not smoothed:**
S08 names the DISCRETE INCIDENCE CONNECTION, not `U(1)_rel`. It is an allied but
distinct guard. This artifact does not merge them.

**G-5 — THE SELECTOR QUARANTINE. FORBIDS: CONSUMPTION OF EM AS AN INPUT (the
reverse direction).**

Per I-9, the "because electromagnetism is established" selector is quarantined and
recorded UNNECESSARY at Gate 1. This bars EM from being ASSUMED in order to fix
the group.

**THE ANSWER, EXACTLY:**

```text
ASSERTION  — FORBIDDEN, and executably enforced (G-1), reinforced in prose (G-2)
             and by self-certification across 78/132 files (G-3).
ASSUMPTION — FORBIDDEN IN THE REVERSE DIRECTION ONLY (G-5): EM may not be assumed
             as an input to select the group. NO GUARD LOCATED forbids assuming
             the identification for the sake of a displayed conditional — and in
             fact O4SR §4.5 and T16SR-dependent readings DO display such
             conditionals lawfully (§4).
CONSUMPTION — FORBIDDEN for the ALLIED discrete object by S08 (G-4). For
             `U(1)_rel` ITSELF, NO EXPLICIT CONSUMPTION BAR WAS LOCATED. What
             stands in its place is O4SR's derived TYPING rule: gauge-active
             findings are not EM-active findings, so an EM reading simply has no
             booked warrant to consume.
ALL THREE   — NO. The guards are not uniform. Assertion is hard-barred;
             consumption is barred only for the allied object; assumption is
             barred only in the EM-as-input direction.
```

---

## §3 — DELIVERABLE 3: WHAT WOULD DECIDE IT

**RESULT: A DECIDER IS NAMED, at sealed bytes, in two mutually-citing artifacts.**
Prior determinations (O4SR included) recorded the identification as OPEN and
FENCED but did not locate the object that would settle it. It exists. It is
stated as a numbered release condition whose FOURTH item IS the identification.

### §3.1 THE DECIDER, AT ITS SOURCE

```text
STAGE8_COMPARISON_FRAME_LOCALIZATION_STEP1_RESULT_V001.md (seal OK)
:209-220, section titled "What would discharge Step 1" (VERBATIM)

  "A Step-1 discharge would need one target-independent theorem, or an
   equivalent chain of theorems, establishing:

   1. the endpoint comparison frame is local;
   2. independent smooth relative-frame changes are physically redundant;
   3. comparison data must be transported between overlapping patches;
   4. the resulting connection is the physical public electromagnetic
      connection, not merely an auxiliary comparison connection in an adopted
      microscopic field-content branch.

   Until then, Steps 2-4 of the holonomy discharge route remain downstream of an
   adopted physical connection."
```

Items 1-3 are exactly `STABILIZER_V002`'s three localization premises (§1.4).
**ITEM 4 IS THE IDENTIFICATION ITSELF, NAMED AS A SEPARATE DISCHARGE OBLIGATION**
— and named with the precise contrast that keeps it from being satisfied by I-7's
adoption: "not merely an auxiliary comparison connection in an adopted
microscopic field-content branch."

### §3.2 THE DECIDER, RESTATED AS A BOOKED "would-build"

An independent sealed audit books the same object as a machine-readable
release condition:

```text
STAGE8_DOWNSTREAM_SMOOTH_CONNECTION_REQUIREMENT_AUDIT_V001.md (seal OK)
:154-158 (VERBATIM)
  "physical_public_EM_connection_derived = false | TYPE-U |
     would-build: the three-premise target-independent localization theorem plus
     a separate theorem identifying its connection with the physical public EM
     connection, or a certified equivalent bridge"

:144-151 (VERBATIM)
  "Its exact release condition at :210-223 requires the three smooth
   localization premises and a separate identification with the physical public
   electromagnetic connection. This is not merely charge/flux access or a public
   comparison functional. The obligation itself asks for patchwise smooth
   redundancy, overlap transport, the covariant derivative, and the EM
   identification. Gate-4 edge transport does not discharge it."

:333-337 (flag block, VERBATIM)
  "PHYSICAL_PUBLIC_EM_CONNECTION_DERIVED = false | TYPE-U |
     would-build: Step 1 plus the separate EM-identification theorem, or a
     ..."
```

The phrase **"a separate theorem identifying its connection with the physical
public EM connection"** is the corpus naming the deciding object in its own
words. It is a THEOREM-SHAPED object, typed TYPE-U (unbuilt), with a stated
sufficiency condition and a stated non-sufficiency condition.

### §3.3 THE ROUTES NAMED, AND WHAT IS EXPRESSLY NOT A ROUTE

```text
STAGE8_DOWNSTREAM_SMOOTH_CONNECTION_REQUIREMENT_AUDIT_V001.md :281-292 (VERBATIM)
  "The requirement can be met in either of two typed ways:
     A. derive the smooth PRPS/public-EM localization route currently named by
        Step 1; or
     B. derive a different, target-independent discrete-to-continuum equivalence
        theorem that supplies the same downstream domains, operators, and
        covariance laws.
   Neither route is complete. Option B is an equivalence obligation, not a
   license to identify discrete and smooth objects by shared terminology."

STAGE8_PRPS_SMOOTH_PHRASING_IMPORT_ADJUDICATION_V001.md (seal OK) :288-300
  (VERBATIM) — the same fork stated for the smooth demand:
  "for any claim that the record-side structure has become a smooth
   physical/public electromagnetic connection, the smooth demand is required.
   The program then has exactly the two branches already identified:
     1. build a record-derived smooth-domain / patch / overlap / bridge theorem; or
     2. adopt/import the smooth domain and smooth bundle/connection explicitly.
   There is no third route in this artifact that turns Gate-4 finite edge
   incidence into a smooth exterior-derivative connection without additional
   structure."
```

**EXPRESSLY NOT ROUTES, of record:**

```text
NOT A ROUTE  Gate-4 edge transport ("does not discharge it", DOWNSTREAM :151)
NOT A ROUTE  charge/flux access or a public comparison functional
             ("This is not merely charge/flux access ...", DOWNSTREAM :148)
NOT A ROUTE  shared terminology between discrete and smooth objects
             ("not a license to identify ... by shared terminology", :291-292)
NOT A ROUTE  the Level-1 adoption of bundle+connection — expressly excluded by
             the decider's own item-4 wording ("not merely an auxiliary
             comparison connection in an adopted microscopic field-content
             branch")
BARRED       "because electromagnetism is established" as a selector — the
             quarantined Gate-1 move (I-9), declared UNNECESSARY
```

### §3.4 THE CURRENT STATE OF THE DECIDER'S PRECONDITION

The three-premise localization theorem — items 1-3, the decider's own
prerequisite — has been ATTEMPTED and did not land:

```text
STAGE8_TARGET_INDEPENDENT_LOCALIZATION_THEOREM_BUILD_RESULT_V001.md (UNSEALED;
  status-only) :302
  "TARGET_INDEPENDENT_LOCALIZATION_BUILD_VERDICT =
   BLOCKED_BY_MISSING_CANONICAL_BRIDGE"
```

So the decider is named, its prerequisite is named, the prerequisite was
attempted, and the attempt is blocked. Item 4 — the identification theorem
proper — has, at this sweep, **no located attempt at all.**

### §3.5 THE ASYMMETRY, DISPLAYED

```text
YES-DIRECTION DECIDER  NAMED. §3.1 item 4 + §3.2 "a separate theorem
                       identifying its connection with the physical public EM
                       connection, or a certified equivalent bridge".
NO-DIRECTION DECIDER   NOT LOCATED. At this sweep, in either root, NO artifact
                       names an object, theorem, test, or determination whose
                       landing would establish that U(1)_rel is NOT the
                       electromagnetic gauge group. The corpus names how the
                       identification could be MADE; it nowhere names how it
                       could be REFUTED.
```

This asymmetry is reported as a status fact. This artifact does not infer
anything from it — in particular it does not treat the absence of a
refutation route as evidence for the identification, which would be advancing
the question.

---

## §4 — DELIVERABLE 4: THE DEPENDENCY MAP

Enumerated at bytes: every sealed result whose READING would change if the
identification landed, in either direction. "Reading" is used strictly — a
result's TRUTH may be untouched while what it MEANS changes. Both are recorded
separately, because conflating them is how a gauge finding silently becomes an
EM finding.

### §4.1 D-1 — THE O6SR ESCAPE-SIDE FINDING (obstruction destroyed by switching
real U(1)/EM structure ON)

```text
STAGE8_OBSTRUCTION_ORIGIN_O6SR_V001.md (seal OK) :472-487 (VERBATIM)
  "COUNTERFACTUAL B — SWITCH GAUGE/EM STRUCTURE ON: what happens to the
   blocker when the content genuinely carries U(1)/EM structure? THE BLOCKER
   IS DESTROYED, NOT CREATED (O6-1d):
     GLOBAL U(1): a constant phase e^{i theta} is unitary and central; it
       leaves ||h psi|| and ||psi|| unchanged, hence leaves the class, C, and
       the sandwich all exactly as they were. It neither creates nor removes
       the blocker — it is invisible to it.
     LOCAL U(1) / A REAL EM POTENTIAL: with A(x) non-constant, the generator's
       symbol acquires a POSITION dependence (d/dx of the symbol is -q != 0),
       so it is NO LONGER A FOURIER MULTIPLIER. Hypotheses (h-1) and (h-2)
       FAIL. The theorem does not apply.
     CONSTANT (PURE-GAUGE) POTENTIAL: d/dx = 0, translation invariance
       RESTORED — the blocker returns exactly when the gauge field is trivial."
:500-501
  "GAUGE STRUCTURE SITS ON THE ESCAPE SIDE OF THIS BLOCKER, NOT ITS ORIGIN SIDE."
:1489-1492 (flag block)
  "BLOCKER_ORIGIN_FP3 = GENERIC( symmetry: translation invariance; survives on
   scalar indefinite content; DESTROYED by switching real U(1)/EM structure on;
   subordinate (h-4) is SPECTRAL indefiniteness, spinor-supplied, not gauge )"
```

```text
UNDER YES (U(1)_rel IS the EM gauge group):
  TRUTH        UNCHANGED. The counterfactual is executed on the hypotheses
               (h-1)/(h-2) of a Fourier-multiplier theorem; whether the local
               U(1) is "the" EM group is irrelevant to whether a non-constant
               A(x) breaks translation invariance.
  READING      CHANGES, materially. The escape ceases to be a statement about
               a FOREIGN structure one could switch on, and becomes a statement
               about the record's OWN derived group: the record would then
               already carry, in U(1)_rel, the very structure whose activation
               destroys FP-3's blocker. "Switching EM structure on" would stop
               being a counterfactual and become a question about whether the
               record's own field is non-constant.
  GRADE MOVE   The O6SR verdict FP-3 = GENERIC does NOT move (see §5, IND-2):
               it rests on translation invariance being a property of
               CONSTANT-COEFFICIENT content, which no identification alters.

UNDER NO (U(1)_rel is NOT the EM gauge group):
  TRUTH        UNCHANGED, identically.
  READING      CHANGES the other way: "real U(1)/EM structure" is confirmed as
               an object EXTERNAL to the record's derived group, and the
               counterfactual stays a genuine counterfactual — a hypothetical
               import, not a latent record property.
  GRADE MOVE   None.

PRECONDITION CHAIN, recorded: for D-1 to be about U(1)_rel AT ALL, U(1)_rel must
  first be LOCALIZED (§1.4, decider items 1-3), since counterfactual B's active
  limb requires a non-constant A(x). Localization is itself open. So D-1's
  reading is downstream of TWO open questions, not one.
```

### §4.2 D-2 — THE PARTITION THEOREM'S REQUIRE HALF (the gauge-active clauses)

The require-half's chain and the clauses O4SR classified GAUGE-ACTIVE:

```text
STAGE8_PARTITION_THEOREM_T16SR_V001.md (seal OK) :175-180 (VERBATIM)
  "S1 [Σ4, SI.3] Sector-n phase data enter ONLY as U(1) characters χ_n on the
      holonomy argument: z^(n) = χ_n(h), with g = exp(iθ) ∈ U(1).
   S2 [Σ4's own domain typing] χ_n is a map ON U(1): h and h + 2π present the
      same group point, so well-definedness (single-valuedness) of the
      displayed clause itself demands χ_n(h + 2π) = χ_n(h)."
:149-151, claim (I) (VERBATIM)
  "(I) REQUIRE-HALF. In EVERY model of Σ, the quantization class holds: every
   sector/winding label admissible under Σ4's single-valued closure lies in ℤ —
   exactly ℤ, no more — and the definitional pair {+1, −1} inhabits it."
:159-160, claim (III)(a) (VERBATIM)
  "(III) EXCLUSIVITY. No model of Σ places them otherwise: (a) no model places
   the quantization class allow-side"
:267-269, COR-1 (VERBATIM)
  "COR-1 [Σ5, Σ6 only] The charge structure holds in every model: transition
   covariance at symbolic n and unit-modulus invariant content [PT6];
   conjugate closure magnitude-free [PT3e]."
```

O4SR's classification of exactly these:

```text
STAGE8_EM_PARTICIPATION_O4SR_V001.md :571-581 (VERBATIM)
  "Sigma4-under-its-reading, (I), (III)(a), COR-1
     = GAUGE-ACTIVE (U(1)-ACTIVE): their truth turns on compactness +
       character theory of the record's derived U(1)_rel. DERIVED, at the
       audit's own substitution experiment.
     = EM-ACTIVE ONLY CONDITIONALLY: they become EM-active exactly when, and
       only when, the open EM identification lands. Today it is fenced and
       NO_VERDICT. So today these clauses carry a GAUGE premise, not an EM
       premise."
```

```text
UNDER YES:
  TRUTH        UNCHANGED. S1-S5 is algebra on characters of a compact group;
               naming the group "EM" adds no step and removes none. The class
               is still exactly ℤ.
  READING      CHANGES, and this is the map's principal entry. Per O4SR
               :826-830 (VERBATIM): "THEN clauses Sigma4-under-its-reading,
               claim (I), claim (III)(a), and COR-1 convert from GAUGE-ACTIVE
               to EM-ACTIVE, and the partition theorem's REQUIRE half would
               then carry an EM-specific premise of record." The integer
               quantization class would become a statement about ELECTRIC
               CHARGE quantization rather than about record-winding labels.
  GRADE MOVE   Per T16SR's own scope clause :426-427 (VERBATIM): such a landing
               "RE-POSES the question; the theorem forecloses nothing about
               changed ground." So the theorem is not overturned — it is
               re-posed on new ground.

UNDER NO:
  TRUTH        UNCHANGED.
  READING      STABILIZES. The clauses are confirmed permanently GAUGE-ACTIVE
               and never EM-active; the "only conditionally" qualifier in
               O4SR's classification would be dischargeable and could be
               dropped. O4SR's MIXED verdict would become defensible as a
               permanent partition rather than a provisional one.
  GRADE MOVE   None to the theorem. O4SR's CH-3 choice (§4.4) would be
               retrospectively vindicated rather than left open.

WHAT DOES NOT MOVE EITHER WAY, quoted (O4SR :830-833):
  "AND EVEN THEN the magnitude's allow-side placement does NOT convert: (II)
   and (III)(b)/(c2)/(c3) are denotation-robust, so they are untouched by any
   identification made to the character map's group."
```

### §4.3 D-3 — DELTAPHI'S NO_VERDICT (a grade stated as conditional on the
identification)

```text
STAGE8_DELTAPHI_PI_PROTECTION_DETERMINATION_V001.md (seal OK) :429-432
  "DeltaPhi_is_holonomy = NO_VERDICT |
     blocker: physical local connection / EM identification remains open in the
     current stabilizer and transport-only records"

UNDER YES:
  TRUTH        The NO_VERDICT is DISCHARGEABLE — the named blocker is removed.
               This is the one entry where a grade is written to MOVE on the
               identification. Note the blocker is a CONJUNCTION ("physical
               local connection / EM identification"); the identification alone
               removes one conjunct, and per §3.1 items 1-3 must land anyway.
  READING      DeltaPhi would become a physical electromagnetic holonomy, which
               :180-182 currently denies of record ("It is not sealed as a Berry
               phase, spectral flow, index, or already physical electromagnetic
               holonomy").
  GRADE MOVE   NO_VERDICT -> potentially resolvable. THIS ARTIFACT DOES NOT
               RESOLVE IT and does not assert that it would resolve YES.

UNDER NO:
  TRUTH        The NO_VERDICT becomes PERMANENT on this route — the blocker is
               not removable, it is refuted, so DeltaPhi cannot be a holonomy
               VIA the EM identification. Other routes are not assessed here.
  READING      DeltaPhi stays a "dimensionless accumulated action-phase
               difference in the primitive two-character U(1) record map"
               (:425-427) with no promotion available on this route.
  GRADE MOVE   NO_VERDICT -> settled-negative on this route only.
```

### §4.4 D-4 — O4SR's OWN CHOICE CH-3

```text
STAGE8_EM_PARTICIPATION_O4SR_V001.md :865-876, CHOICE LEDGER (VERBATIM excerpt)
  "CH-3 SCORING Sigma4-UNDER-ITS-READING AS GAUGE-ACTIVE BUT NOT (TODAY)
        EM-ACTIVE: PREMISE(named), and the single most consequential choice
        here ... THE ALTERNATIVE (score it EM-ACTIVE on the commission's literal
        'different gauge group' clause) is displayed, not suppressed, and
        the verdict is written so BOTH readings are recoverable: under the
        literal reading the verdict is still MIXED with the SAME clause
        partition — only the label on the active side changes from
        GAUGE-ACTIVE to EM-ACTIVE. No downstream display depends on which
        label is chosen."

UNDER YES:  CH-3's chosen label becomes the WRONG label; its displayed
            ALTERNATIVE becomes the right one. O4SR states this is IMMATERIAL —
            same partition, only the label moves — so O4SR's verdict (MIXED)
            survives intact. THIS IS O4SR PROTECTING ITSELF IN ADVANCE, and it
            works.
UNDER NO:   CH-3's chosen label is confirmed. No movement.
```

### §4.5 D-5 — THE MAXWELL-SYMBOL / WARD-COMPATIBLE THREAD

The commission names two Lane-2 artifacts. Their status in this map is
NON-DEPENDENT-BY-CONSTRUCTION, and O4SR says so at bytes:

```text
STAGE8_EM_PARTICIPATION_O4SR_V001.md :800-805 (VERBATIM)
  "'This Ward property holds for the whole (chi_K,T) family and cannot select a
   reader coordinate'; 'the cylindrical Ward identity is homogeneous'; 'No
   algebraic Ward identity turns that support into the diagonal.' The record's
   EM structure, where it is built, is displayed as NON-SELECTING; the closure,
   where it fails, is displayed as CLASS-QUANTIFIED. The two threads do not
   touch, and each says so about itself."

UNDER YES:  The Maxwell-symbol thread would ACQUIRE a connection to the record's
            own group that it currently lacks. Its own results are NON-SELECTING
            by their own statements, so no displayed verdict moves; what changes
            is that the two threads would no longer be independent, and O4SR's
            "the two threads do not touch" would need re-posing.
UNDER NO:   The separation is confirmed permanent.
```

### §4.6 THE MAP, COMPACT

```text
ENTRY  OBJECT                          TRUTH@YES  TRUTH@NO  READING MOVES?
D-1    O6SR FP-3 escape-side finding     same       same     YES, both ways
D-2    T16SR require-half (I),(III)(a),
       COR-1, Σ4-under-its-reading       same       same     YES, both ways
D-2b   T16SR allow-half (II),(III)(b/c)  same       same     NO — denotation-robust
D-3    DELTAPHI DeltaPhi_is_holonomy     n/a        n/a      GRADE ITSELF MOVES
D-4    O4SR CH-3 label                   same       same     LABEL ONLY (immaterial
                                                             by O4SR's own design)
D-5    Maxwell-symbol / Ward thread      same       same     THREAD-SEPARATION
                                                             claim re-posed @YES
```

**ONE GRADE MOVES (D-3). NO TRUTH MOVES. FOUR READINGS MOVE.** That is the exact
shape of the dependency, and it is why the caveat became load-bearing without any
result becoming wrong.

---

## §5 — DELIVERABLE 5: THE INDEPENDENCE CHECK

**QUESTION.** Is any result currently BOOKED as established WEAKENED by the
identification landing either way — i.e. has anything of record quietly assumed
one answer?

### §5.1 THE INSTRUMENT

An uncapped co-occurrence detector over both roots (all file types, self-excluded):
every file mentioning `U(1)_rel` was scanned for EM-loaded vocabulary
("electromagnetic gauge group", "EM gauge group", "the photon", "photon field",
"electric charge", "electromagnetic field strength", "Maxwell field", "the
electromagnetic U(1)", "EM U(1)", "electromagnetic connection") occurring within
400 characters of the `U(1)_rel` token — i.e. close enough to be predicating the
EM term OF the record's group.

```text
FILES MENTIONING U(1)_rel        ROOT_A 64   ROOT_B 61
CO-OCCURRENCE WINDOWS FOUND      2 (both roots, deduplicated)
DISTINCT LOADED TOKENS MATCHED   1 ("electromagnetic connection")
```

### §5.2 BOTH HITS ARE DENIALS, NOT ASSUMPTIONS

```text
HIT 1 — STAGE1_PREMISE_DISPOSITION_V001.md :44-47 (VERBATIM)
  "It does not derive the existence of a physical local electromagnetic
   connection, which remains adopted Level-1 field content."

HIT 2 — STAGE8_COMPARISON_FRAME_LOCALIZATION_STEP1_RESULT_V001.md :218-220
  (VERBATIM) — the decider clause itself:
  "the resulting connection is the physical public electromagnetic connection,
   not merely an auxiliary comparison connection in an adopted microscopic
   field-content branch."
```

Neither predicates EM of `U(1)_rel`. Both do the opposite: one denies the
derivation, the other names it as an outstanding obligation.

### §5.3 THE FOUR STRONGEST CANDIDATES FOR A QUIET ASSUMPTION, TESTED INDIVIDUALLY

**IND-1 — THE UNIT WINDING `|n| = 1`. Does it quietly assume YES?**
NO. The sealed forcing route is FAITHFULNESS, not EM, and a blind cross-lineage
verifier established this at bytes:

```text
STAGE8_UREL_DETERMINACY_CHECK_OPUS_V001.md (seal OK) :212-213 (flag)
  "FORCING_MECHANISM_IN_SEALED_TEXT = FAITHFULNESS (STAGE1:41; FABLE:161-172,
   300-307), not kernel-on-q_N"
:140-141  "So every sealed route to |n| = 1 runs through FAITHFULNESS"
```

And the defining source pre-empts the EM reading explicitly:

```text
PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md :76-77
  "This yields stable integral charge units for the primitive record handle
   without using the observed electromagnetic coupling."
PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md :90-91
  "It is not newly derived here as an electromagnetic charge spectrum."
```

INDEPENDENT. (Its OWN open question is faithfulness — VERDICT = UNVERIFIED at
`:235` — which is a separate matter this artifact does not touch.)

**IND-2 — O6SR's FP-3 = GENERIC. Does it quietly assume NO?**
NO. The verdict rests on a property of constant-coefficient content, stated
without reference to which group is switched on:

```text
STAGE8_OBSTRUCTION_ORIGIN_O6SR_V001.md :491-494 (VERBATIM)
  "VERDICT AT FP-3 [DERIVED]: GENERIC. The blocking property — translation
   invariance — does NOT follow from the
   content being gauge/EM-carrying; it follows from the content being
   CONSTANT-COEFFICIENT, which is the absence of a gauge background rather than
   its presence."
```

INDEPENDENT. Only its READING moves (§4.1), never its verdict.

**IND-3 — T16SR's REQUIRE HALF. Does it quietly assume either?**
NO. S1-S5 consumes `Σ4`'s own displayed "∈ U(1)" and pure algebra. T16SR is
explicit that the corroborating surface sentence is "cited as CORROBORATION, not
premise" (:180-181), and its exclusivity claim (III)(c) turns on the class's
output being "an integer label, not a continuum response magnitude" (:161-162) —
a typing fact, not an EM fact. INDEPENDENT.

**IND-4 — GATE 1's COMPARISON GROUP `U(1)`. Does it quietly assume YES?**
NO — and this is the corpus's only ACTIVE independence certificate on the
question, quoted at §2.4 G-5: the classification "used only sealed
target-independent structure — the quarantined 'because electromagnetism is
established' selector is UNNECESSARY". The EM route was available, was
quarantined, and the result was obtained without it. INDEPENDENT, certified.

### §5.4 THE ONE ADOPTION, AND WHY IT IS NOT A QUIET ASSUMPTION

`FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md` adopts a `U(1)_rel`
bundle and connection as Level-1 field content (I-7). Three reasons it does not
constitute a quiet assumption of either answer:

```text
(a) It is SELF-DECLARED AS ADOPTED, not booked as established: "It is an adopted
    microscopic theory premise, not a consequence of the sealed pre-alpha
    results" (:24-26).
(b) It expressly excludes the EM route from its own derivation: the adoption is
    "not derived from ... the demand to reproduce electromagnetism" (:53-59).
(c) It adopts LOCALIZATION, not IDENTIFICATION — and the decider's item 4
    (§3.1) is written precisely to exclude this adoption from counting as the
    identification ("not merely an auxiliary comparison connection in an
    adopted microscopic field-content branch").
```

### §5.5 THE INDEPENDENCE VERDICT

```text
NOTHING BOOKED AS ESTABLISHED IS WEAKENED BY THE IDENTIFICATION LANDING EITHER
WAY, at this sweep.

  Results whose TRUTH depends on the identification            NONE LOCATED
  Results that quietly ASSUME the identification (YES)         NONE LOCATED
  Results that quietly ASSUME its negation (NO)                NONE LOCATED
  Results whose GRADE is stated as conditional on it           ONE — DELTAPHI's
                                                               DeltaPhi_is_holonomy
                                                               = NO_VERDICT, and it
                                                               is stated OPENLY, not
                                                               quietly (§4.3)
  Results whose READING moves                                  FOUR (§4.6)
```

The corpus has kept this clean, and it did not happen by accident: the guards of
§2.4 — an executable flag bar, a fail-closed literal, a test assertion, a
quarantined selector, and a self-certification recited in 78 files of ROOT_A and
132 of ROOT_B — are exactly the machinery that prevented a quiet assumption from
forming. The one place the record could have taken the EM shortcut (Gate 1), it
recorded that it did not need it.

---

## §6 — VERDICT

```text
VERDICT = MIXED (partial namings, exact)
```

**THE EXACT PARTITION, which is the verdict:**

```text
YES-DIRECTION  FULLY AND EXACTLY NAMED, at sealed bytes, in two mutually-citing
               artifacts, with routes and non-routes enumerated:
                 the deciding object  — "a separate theorem identifying its
                   connection with the physical public EM connection, or a
                   certified equivalent bridge"
                   (DOWNSTREAM_SMOOTH_CONNECTION_REQUIREMENT_AUDIT :154-158)
                 its exact content   — discharge item 4, "the resulting
                   connection is the physical public electromagnetic connection,
                   not merely an auxiliary comparison connection in an adopted
                   microscopic field-content branch"
                   (COMPARISON_FRAME_LOCALIZATION_STEP1_RESULT :218-220)
                 its prerequisite    — the three-premise target-independent
                   localization theorem (items 1-3), ATTEMPTED and
                   BLOCKED_BY_MISSING_CANONICAL_BRIDGE
                 its typed routes    — A / B (DOWNSTREAM :281-292); branches
                   1 / 2 (PRPS_SMOOTH_PHRASING :288-300)
                 its non-routes      — Gate-4 edge transport; charge/flux
                   access; shared terminology; the Level-1 adoption; the
                   quarantined EM selector
               This is NOT a vague naming. It is a booked TYPE-U release
               condition with a stated sufficiency and a stated insufficiency.

NO-DIRECTION   NOT NAMED ANYWHERE, in either root, at this sweep. No artifact
               names an object, theorem, test, determination, or bridge whose
               landing would establish that U(1)_rel is NOT the electromagnetic
               gauge group. The corpus states how the identification could be
               MADE and never how it could be REFUTED.
```

**THE ALTERNATIVE READING, DISPLAYED so the record is recoverable.** Item 4 is
stated as a PROPOSITION ("the resulting connection is the physical public
electromagnetic connection"). A reader who treats a named proposition as
two-sided — provable or refutable — would read this artifact's located bytes as
**DECIDER-NAMED**, since establishing the negation of item 4 would settle NO.
This artifact scores MIXED because the corpus frames item 4 exclusively as a
DISCHARGE OBLIGATION and a `would-build`, and nowhere contemplates its
refutation. **THE LOCATED BYTES ARE IDENTICAL UNDER BOTH READINGS; only the
label moves.** No deliverable below §3 depends on which label is chosen.

**NOT UNDECIDABLE-TODAY, and not NO-DECIDER-OF-RECORD** — both are excluded by
§3.1/§3.2, which are sealed, verified, and quoted.

**THE COMMISSION'S PREMISE, CHECKED.** The commission states "nobody has ever
established the identification's own status as an object." Confirmed as to
STATUS — no prior artifact registers the grades, the guard mechanisms, or the
dependency map. **But the DECIDER was already of record and had simply never
been collected**: it was written on 2026-08-01-era Step-1 work and re-booked by
the DOWNSTREAM audit, and O4SR (which searched this exact territory) did not
surface it — O4SR named the identification's status as blocker and its
consequences, but not the object that would settle it. This artifact's
contribution on Deliverable 3 is LOCATION, not creation.

---

## §7 — CHOICE LEDGER (commission O14SR; every unforced choice, classified)

```text
CH-1 TREATING PRIMITIVE_RELATIVE_PHASE_{CONNECTION_V001, STABILIZER_V002} AS
     "THE DEFINING BYTES" DESPITE THEIR HAVING NO SIDECAR SEAL:
     FORCED in substance. The commission asks for the definition "at its sealed
     source"; these are the only files in either root that DEFINE the quotient,
     they are hash-locked by executable audit + results JSON (an equivalent and
     stated seal discipline), and their bytes are IDENTICAL across both roots
     (verified, §0.2). The discrepancy in SEAL MECHANISM is disclosed rather
     than smoothed, and carried into the FLAG BLOCK.

CH-2 REPORTING THE CONNECTION/STABILIZER LOCALIZATION DISAGREEMENT (§1.4)
     RATHER THAN PICKING ONE: FORCED by the determination-only fence. Picking
     one would decide whether U(1)_rel is localized, which is decider item 1-3
     and therefore advances the question. MATERIAL: the disagreement is why
     D-1's reading sits downstream of two open questions, not one.

CH-3 SCORING I-7 (FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002) AS
     "ASSUMED-FOR-DISPLAY OF THE LOCALIZATION ONLY" RATHER THAN AS AN ADOPTION
     OF THE IDENTIFICATION: PREMISE(named), and the most consequential choice
     here. GROUND: the file lists "the demand to reproduce electromagnetism"
     among what the adoption is NOT derived from (:53-59), and the decider's
     item 4 is worded expressly to exclude an "adopted microscopic
     field-content branch" from counting. THE ALTERNATIVE (score it as a quiet
     YES-assumption) is displayed at §5.4 with all three grounds, so a reader
     who disagrees can recover it. If the alternative were taken, §5.5's line
     "Results that quietly ASSUME the identification (YES) — NONE LOCATED"
     would become "ONE — I-7", and NOTHING ELSE in this artifact would change.

CH-4 SCORING THE VERDICT MIXED RATHER THAN DECIDER-NAMED: PREMISE(named).
     Displayed at §6 with the alternative reading stated in full and the note
     that the located bytes are identical either way. UNFORCED, IMMATERIAL to
     Deliverables 1-5.

CH-5 SEPARATING S08 (the DISCRETE INCIDENCE CONNECTION) FROM THE U(1)_rel
     GUARD RATHER THAN COUNTING IT AS ONE FENCE: FORCED — they name different
     objects. MATERIAL: it is why §2.4's consumption answer is "barred only for
     the allied object", not "barred".

CH-6 COUNTING THE GUARD SWEEP OVER ALL FILE TYPES AND BOTH ROOTS, WHERE O4SR
     COUNTED .md IN ONE ROOT: UNFORCED. Declared, and reconciled explicitly at
     §2.3 so neither count impeaches the other. Chosen because the commission
     said "uncapped sweep of both roots".

CH-7 CONSUMING TWO UNSEALED FILES FOR STATUS ONLY
     (STAGE8_TARGET_INDEPENDENT_LOCALIZATION_THEOREM_BUILD_RESULT_V001.md,
     EM_DEPENDENCY_ORDER_FREEZE_V001.md): UNFORCED but disclosed at each use
     with the words "UNSEALED — status only". Neither carries a verdict here;
     removing both would delete §3.4's blocked-prerequisite line and one
     non-route, and would change no grade.

ZERO OPEN.
```

---

## §8 — TOY_SEPARATION

```text
NO TOY WAS BUILT, RUN, OR CONSULTED. This artifact contains no model, no
simulation, no worked example, no illustrative instance, and no constructed
object of any kind.

THE TWO SCRIPTS I WROTE ARE SWEEP INSTRUMENTS, NOT TOYS:
  decider_sweep.py   — regex co-occurrence over both roots (§3 instrument)
  independence.py    — regex co-occurrence over both roots (§5 instrument)
Both live OUTSIDE both corpus roots (in this session's scratchpad), read only,
wrote nothing into either root, and produce FILE/LINE LOCATIONS ONLY. Every
finding they surfaced was then opened and quoted at its own bytes; no verdict
rests on a script's summary. Neither script models any physics, evaluates any
quantity, or represents any record object.

THE CORPUS'S OWN EXECUTABLE OBJECTS (audit scripts, tests, results JSON) were
READ AS RECORD — as evidence of what the guards enforce (§2.4) — and were NOT
RUN. No audit was re-executed; no flag was recomputed; no status was moved.

ACTUAL SURFACE, NOT A TOY: every quoted sentence is from a file in the corpus at
its stated path and line, with seals verified where sidecars exist and bytes
compared across roots where they do not.
```

---

## §9 — IMPORT AUDIT

```text
MACHINERY IMPORTED                    NONE.
  No smooth-manifold language, no GR, no QFT apparatus, no carrier, no
  measure, no scale, no renormalization concept was brought in from outside
  the quoted bytes. Where the corpus's own text uses such language it is
  QUOTED, never paraphrased into a claim of mine.

PREMISES ADOPTED BY ME                NONE.
  Faithfulness: NOT used (it is UREL_DETERMINACY_CHECK's open item; I report
    its status only).
  Localization of U(1)_rel: NOT assumed (§1.4 left open by CH-2).
  The EM identification: NOT assumed in either direction — the whole point.

EXTERNAL SOURCES                      NONE. No web, no memory-bank search, no
  ~/.codex, no other project directory. Both corpus roots only, plus this
  session's scratchpad for the two instruments.

REGISTER/TRACKER/ROAD/PLAN/CONTINUATION FILES   NONE OPENED.
  DECLINE_REGISTER_V002.md was NOT opened. S08's content (§2.4 G-4) is quoted
  from STAGE8_AXN_FAMILY_BOUNDING_CODEX2_V001.md (seal OK), which recites it,
  and corroborated from two further sealed artifacts that recite it. This is
  disclosed so no reader mistakes the citation for a register read.
  PROGRAM_STATE_BRIEF, PE-* and similar were neither opened nor consulted.

"Q-..." OBJECTS                       EXPECTED-UNLOCATABLE; none chased, none
  cited, none inferred.

GIT                                   NONE. No git command was run.

FILES WRITTEN                         EXACTLY TWO, both at the commissioned
  path: this artifact and its seal sidecar. No existing file in either root was
  edited, moved, or renamed. Output path was probed ABSENT before first write.
```

---

## §10 — FLAG BLOCK

```text
alpha_computed                  = false
proof_authorized                = false
kappa_record_computed           = false
coupling_evaluation_authorized  = false

DETERMINATION_ONLY              = HELD. No adoption; no authored physics; no
                                  value, no number as a value of anything; no
                                  float; no measured-constant comparison; no CAS.
EM_IDENTIFICATION_MADE          = false
EM_IDENTIFICATION_LICENSED      = false
EM_IDENTIFICATION_RECOMMENDED   = false
EM_IDENTIFICATION_ARGUED_EITHER_WAY = false
NO_GATE_FLAG_WITNESS_OR_STATUS_OF_ANY_CONSUMED_ARTIFACT_MOVED = true
NOTHING_HERE_DISCHARGES_ANY_ABSENCE_OR_ANY_FAILURE_POINT      = true

SWEEP_CUTOFF                    = 2026-08-15T20:00:05Z
SWEEPS_UNCAPPED_BOTH_ROOTS      = true (all file types; self-excluded)
SEALS_VERIFIED                  = 8/8 commissioned + 4/4 further consumed,
                                  each `shasum -a 256 -c` run from the
                                  artifact's own directory
DEFINING_SOURCE_SEAL_MECHANISM  = AUDIT-LOCK, NOT SIDECAR (disclosed, §0.2);
                                  bytes identical across both roots (verified)
UNSEALED_CONSUMED_FOR_STATUS_ONLY = 2 (disclosed at each use, CH-7)

U1REL_DEFINITION_LOCATED        = true (§1)
IDENTIFICATION_STATUS           = NO_VERDICT / FENCED / never asserted, never
                                  denied, anywhere in either root (§2)
GUARD_FILES  ROOT_A = 78   ROOT_B = 132  (union of all guard forms, self-excluded)
GUARDS_FORBID                   = ASSERTION (hard, executable);
                                  ASSUMPTION only in the EM-as-input direction;
                                  CONSUMPTION only for the allied discrete
                                  object (S08). NOT all three. (§2.4)
DECIDER_NAMED_YES_DIRECTION     = true  (§3.1, §3.2 — quoted, sealed)
DECIDER_NAMED_NO_DIRECTION      = false (§3.5 — none located)
DECIDER_PREREQUISITE_STATUS     = BLOCKED_BY_MISSING_CANONICAL_BRIDGE
DECIDER_ITEM4_ATTEMPTS_LOCATED  = 0
DEPENDENCY_MAP_ENTRIES          = 5 + 1 non-moving (§4.6)
GRADES_THAT_MOVE                = 1 (DELTAPHI DeltaPhi_is_holonomy)
TRUTHS_THAT_MOVE                = 0
READINGS_THAT_MOVE              = 4
INDEPENDENCE                    = CLEAN — nothing booked as established is
                                  weakened either way; no quiet assumption
                                  located in either direction (§5)

CHOICE_LEDGER                   = 7 rows; CH-3 and CH-4 PREMISE(named) with
                                  alternatives displayed; ZERO OPEN
TOY_SEPARATION                  = clean (§8)
IMPORT_AUDIT                    = clean (§9)
VERDICT                         = MIXED (partial namings, exact)
```

---

*END OF ARTIFACT — STAGE8_U1REL_EM_IDENTIFICATION_O14SR_V001*
