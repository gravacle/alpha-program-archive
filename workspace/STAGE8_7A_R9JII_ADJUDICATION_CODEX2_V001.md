# STAGE 8 / 7A / STEP 6 — R9-JII CROSS-FAMILY ADJUDICATION

Version: V001  
Lane: CODEX 2  
Date: 2026-08-08  
Subject: `STAGE8_7A_JUNCTION_U1_SHARED_CORE_DARIO_V001.md`  
Sealed carrier: `STAGE8_7A_R9JII_JOINT_LANDING_TEST_V001.md`

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
MEMBER_BOUND = false
COMMON_CELL_FORMED = false
JUNCTION_MAP_EVALUATED = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none
```

## 0. Queue, custody, and output preflight

The single queued relay was
`relay_inbox/RELAY_PASTE_714_R9JII_CARRIER_CODEX2_V001.md`, SHA-256
`17354d5033cebf05c9dc7be589e826b1f1549d8e38182922877537a92fb0746c`.
Its `.seal.sha256` verified and its header names `CODEX 2`. The required
`relay_outbox/714_ACK.md` was written before source work. Both requested output
names, both output seal names, the archive output names, and `714_DONE.md` were
absent before writing.

The subject source verified at
`ec96235121896d146e7f49031a4e0f4f36876cd0580b7cf0351c7f478d2bc1fa`.
The corrected carrier is sealed at
`5f4979d50c905c009c1fa18cec65cde6d9812b7f6c8e7c6870e4e6bea6cf78d5`.
Its §1 manifest gives the full names, current SHA-256 values, and corrected byte
spans for eleven sealed inputs. Each input and sidecar was independently rehashed.

## 1. Z1 — grounding envelope check

### 1.1 Span resolution

Four cited spans did not cover the complete text attributed to them. The carrier
uses generated full-clause spans rather than copying the truncated endpoints.

| Finding | Subject citation | Byte result | Corrected sealed span |
|---|---|---|---|
| GF-01 | sequenced-program `[1069,1360)` | stops at `dimensionless parame`; the quoted `parameter.` lies outside | `DECISION_SEQUENCED_PROGRAM_2026-08-06.md` `eaeffd37…[1069,1365)` |
| GF-02 | DoR-019 routing `[737,878)` | stops at `exists undeclar`; it does not carry the completed certificate sentence | `DOR_019_CARRIER_METRIC_AND_UNITS_RATIFICATION_2026-08-03.md` `6ab72b0c…[737,904)` |
| GF-03 | DoR-019 discipline `[1140,1325)` | stops at `member-sensitivity tagging an`; the cited permanent-attack list is outside | same source `6ab72b0c…[1140,1533)` |
| GF-04 | R9/R9-V002 `[1786,2042)` | stops at `as one a`; it does not carry `associated-orbit object on each A8-common formed instance` | `STAGE8_TASK5_COMMON_SEAMS_LANE3_V002.md` `2525096b…[1786,2100)` |

The other load-bearing subject spans carry their stated clauses: A2 clauses 7–8,
F'-5, original F1, the common-cell row, R9 falsifier typing, R9 PENDING carriage,
and Q-126. Some are over-wide, but none omits a claimed token.

### 1.2 Clause direction

| Clause | Envelope verdict | Evidence and consequence |
|---|---|---|
| J1 | REPAIRED | The declaration law and R4-only routing are carried. But DoR-019 only **names** the paired-hidden-conversion attack. Its sealed regression source, `STAGE8_TASK4B_METRIC_V005_RECHECK_LANE1_V001.md` `d2bbd0eb…[12504,13458)`, defines the attack as two reciprocal **hidden** crossings whose factors cancel in the aggregate and says the pair must be omitted or declared as a new seam field. Therefore S01's statement that “two separately declared units” are themselves the attack is directionally false. The carrier requires visible declarations and catches undeclared reciprocal pairs without criminalizing declaration. |
| J2 | CARRIED | JD-3's presentation-independence obligation is present at `fdf20bd4…[45349,45957)` and F'-5's exact prohibited data are present at `3c008ecc…[5052,5150)`. Their application is conditional on the common value named by R9-JII; no cell is formed by the clause. |
| J3 | REPAIRED | The no-implicit-unit limb is carried. The family limb in S01 is not current law: principal decision `e76746ae…[99,1236)` and frozen preregistration `9f0d12b4…[13091,16444)` supersede unconditional F1. Weak-rule underdetermination still kills; genuine scale dependence routes to K-1/K-3 measurement and never loses by family-hood alone. The carrier uses F1'. |
| J4 | ADOPTED WITH STATUS SURFACED | The corrected span carries the H/HOL R9-V002 template exactly: one associated-orbit object on each common formed instance. It does not historically name the Ward/beta pair. Applying that shape to this pair is the new carrier's expressly authorized adoption, not a fact back-dated into the source. |

Thus three source families carry the direct law (J1 declaration/routing, J2, and
J3 implicitness), the principal split repairs J3's direction, and the new sealed
carrier makes J4's pair-specific adoption explicit. No analogy is presented as an
old source quote.

### 1.3 Grounding findings census

```text
SOURCE_SPAN_DRIFT = 4  (GF-01..GF-04)
J1_DIRECTION_DRIFT = 1 (declared != hidden)
J3_DIRECTION_DRIFT = 1 (F1 superseded by F1')
J4_STATUS_DRIFT = 1    (template carried; pair application adopted here)
TOTAL_GROUNDING_FINDINGS = 7
```

## 2. Z2 — proposed-line adjudication

### 2.1 Old proposal, displayed

The following is S01's proposed carrier content at `[25153,27190)`:

```text
R9-JII :  one common formed record cell e on which BOTH
            (A) the Ward-symbol map's declared cross-sector unit, and
            (B) the length normalization's beta
          exist independently.

          By Q-10 the record cell already carries (B)'s internal projective and
          external Lorentzian structures of record, so the open half is exactly:
          (JD-3)'s named oriented k-cell IS that record cell.

          On such an e, agreement of (A)'s declared unit with (B)'s beta is a
          FALSIFIER, not a constructor: disagreement kills; agreement builds
          neither map and discharges neither residue.

NOTE, carried with it:  by the sealed Q-126 census, R9-JII is satisfiable
non-vacuously only at a junction that is both DERIVED and beta-SENSITIVE, and no
such junction presently exists.  Sealing R9-JII therefore states the test; it does
not make it runnable.  Both facts should travel together, or the carrier will read
as more progress than it is.
```

### 2.2 Why repair was required

The proposal is correctly falsifier-typed and preserves the Q-126 warning, but it
does not state the complete J1–J4 test:

1. it gives agreement without the declaration/R4 and paired-hidden controls;
2. it omits J2's presentation and F'-5 predicates;
3. it omits J3's implicit-unit predicate and, through S01's surrounding J3,
   inherits the superseded unconditional-F1 direction;
4. it does not state J4's one-associated-object versus independent-return test;
5. its Q-10 paragraph discusses how the missing cell identification would be
   supplied, while the commissioned carrier must be silent on formation.

### 2.3 New sealed line, displayed

```text
R9-JII: For every common formed record cell e on which (A) the Ward-symbol map's declared cross-sector unit and (B) the length normalization's beta exist independently, compare A and B as one R4-routed associated object; this falsifier fires iff (J1) A's declared unit and beta are unequal, either crossing is undeclared, or an undeclared reciprocal crossing pair is hidden by aggregate cancellation, (J2) their common value is not invariant under cell re-presentation or depends on ell, truncation level, cellulation-family index, or cellulation geometric datum, (J3) the value is implicit (including silently fixed to 1) or a surviving positive beta-family is caused by weak-rule underdetermination—while genuine scale dependence routes to measurement under K-1/K-3 and never fires by family-hood alone—or (J4) the two typed returns are compared as independently formed returns rather than as one associated object on e; with no such e, R9-JII remains PENDING, and non-firing builds neither map and discharges neither residue.
```

This is one physical line in the sealed carrier. It is quantified only over a
**common formed** cell and neither forms nor identifies that cell. It states every
J1–J4 receiving predicate, uses the governing F1' direction, remains a falsifier,
and carries the PENDING/non-construction effects.

## 3. Z3 — carrier and entry conditions

The carrier's two entry conditions are byte-verbatim from their sealed sources:

1. common-cell row: `fdf20bd4…[55251,55373)`;
2. Q-126 derived-plus-beta-sensitive census: current sealed register
   `ee21e03b…[328133,328395)`.

Fixed-byte comparison against the source slices passed for both blocks. The carrier
also displays the warning required by the relay:

> **THIS STATES THE TEST WITHOUT MAKING IT RUNNABLE.** Forming the common cell or
> assuming the identification is barred by the armed R9 falsifier until sealed.

The entry conditions remain unsatisfied of record. They were copied, not executed.

## 4. Jurisdiction, pin check, and verb audit

- The cross-sector declaration law is applied only to a cross-sector arrow, the
  risk it was written to police.
- F1' distinguishes weak-rule underdetermination from genuine scale dependence, so
  the test cannot halt on the true signal merely because it is a family.
- R9-JII is PENDING without a formed common cell and cannot convert inability to see
  the object into a negative verdict.
- K-1/K-3 remain preregistered; no kill condition was loosened.
- Eleven source hashes and sidecars verified. Corrected spans were generated from
  byte searches and re-read at their endpoints. Both entry-condition slices compare
  exactly.
- No executable path was added. `DRY_RUN = not_applicable`; the relay expressly
  requires dry-running nothing.
- No common cell was formed, no junction map was evaluated, and the chain was not
  invoked. No register, plan, tracker, or git action occurred.

GROUNDING = J1-J4 all carried (+7 drift findings corrected/surfaced)
LINE = repaired (old/new displayed)
ENTRY_CONDITIONS = 2 carried verbatim
RUNNABLE = false, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
