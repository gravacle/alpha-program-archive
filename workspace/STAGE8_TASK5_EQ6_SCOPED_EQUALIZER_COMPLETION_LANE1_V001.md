# STAGE 8 TASK 5 / EQ6 — SCOPED-WITNESS COMPLETION ON I_flip — LANE 1 V001

Date: 2026-08-04  
Lane: Codex Lane 1  
Task: Paste 525 / Task 5 / EQ6  
Custody: scoped equalizer completion lane

## Lead result

```text
SCOPED_EQUALIZER = STOPPED_AT
ADMISSIBILITY   = STOPPED_AT
FINITE_BOTTOM   = STOPPED_AT
WITNESS_PACKAGE = STOPPED_AT
MACHINERY_APPEAL = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

`FLIP_SECTION = CONFIRMED` and the scoped section construction is genuine, but
the three remaining scoped-bridge objects are still missing from the package:
the full scoped six-generator equalizer on `I_flip`, the DoR-020 scope-admissibility
theorem, and the full finite-bottom certificate.  

Specifically, the following remains open in Q-449:
`SCOPED_SIX_GENERATOR_J1_J15_EQUALIZER_TERM_ON_I_flip + DOR020_SCOPE_ADMISSIBILITY + FULL_FINITE_BOTTOM_ON_SCOPE`.

## 0. PREFLIGHT and input verification

### 0.1 Contracted authority checks

```text
Artifact under review:
STAGE8_TASK5_EQ6_FLIP_SECTION_CHECK_AND_SCOPED_WITNESS_LANE2_V001.md
SHA-256 (archive workspace): 0e61e6ebe8a7d69390c60f0fa1490c46a866c95e1f4a00ad6ffb7646bec62ee7
Sidecar SHA-256: 6cf730e814d0222816524eadcda8ebff206e935af337c83e35ccd22821c270bb

Authoritative contract clauses:
STAGE8_TASK5_EQ6_WHERE_CLAUSES_LANE2_V005.md
SHA-256: 19b2060392b6e04448c1c13416b87b67decf401246e3414a783b288fdb5d80ec
Sidecar SHA-256: a606a500a4739b01244d4919b8db6cbcc19a9e227252bb4d69d1bb503354bdf7

DoR-020: DOR_020_CONTINUUM_PACKAGE_CONDITIONAL_RATIFICATION_2026-08-04.md
```

### 0.2 Register sweep

Q entries checked in this relay:
`Q-408`, `Q-421`, `Q-422`, `Q-430` through `Q-438`, `Q-440` through `Q-447`, and the
current `Q-449` contract plus reconciliation note from `Q-448`.

### 0.3 Scope note

The task is strictly scoped to `I_flip` and does not license member binding,
fixed-point execution, end testing, or numeric evaluation.

---

## 1. P1 — scoped six-generator equalizer completion on `I_flip`

**Result: KILLED (STOPS AT NEEDS).**

From the reviewed flip section, we have:
- `Eq_flip`: an equalizer term for the restricted Q-408 refinement family (one
  generator family, `B_Q408_REFINEMENT`) on the restricted physical category.
- Not yet built: the simultaneous `J1..J15` equalizer term over all six generators
  on `I_flip`.

The confirmed lane-2 artifact explicitly distinguishes these objects and states:
`SCOPED_J1_J15_TERM = absent`, `SCOPED_GENERATOR_COUNT = 1/6`.

Therefore the scoped six-generator equalizer is not inhabited.

```text
P1 verdict = FAIL
Missing object = SCOPED_SIX_GENERATOR_J1_J15_TERM_ON_I_flip
Status = INCOMPLETE
```

---

## 2. P2 — scope-admissibility on `I_flip`

**Result: STOPPED (NOT PROVEN).**

At the geometric level `I_flip` is a lawful covariance/stability subcategory
of the physical Q-408 category:
- no-selection is respected on members and their orbit images;
- admissible stabilizer covariance holds in the constructed family.

However, `I_flip` is not yet an adopted package scope under DoR-020:
1. DoR-020 remains conditional on the joint `J1–J15` equalizer over the six
   package generators; it contains no rule shrinking those hypotheses to `I_flip`.
2. The flipped construction does not prove `I_flip` is cofinal or factor-complete
   for all sealed finite consumers required by `J15`.

So scope-admissibility is only partial (lawful physical subcategory), not the
required package domain admissibility.

```text
P2 verdict = FAIL
P2 status = STAGE_SCOPE_LAWFUL_BUT_NOT_PACKAGE_SCOPE
```

---

## 3. P3 — full finite-bottom certificate on the scoped package

**Result: STOPPED (NOT PROVEN).**

The known flipped witness reconstructs finite Q-408-local behavior and internal
restriction compatibility on the restricted scope. It does not prove the full
`J15` finite-bottom certificate required for the DoR-020 package on `I_flip`.

In particular:
- internal finite restrictions on flip-generated objects are proven;
- full finite-bottom coverage for every sealed active finite datum under all package
  consumers is not closed, so `J15` on `I_flip` remains absent.

```text
P3 verdict = FAIL
P3 status = FULL_FINITE_BOTTOM_ON_SCOPE = absent
```

---

## 4. P4 — witness-package assembly status

**Result: STOPPED_AT_NEEDS**

Since P1–P3 fail, the scoped package cannot yet be assembled.

Expected package components:
1. `SCOPED_SIX_GENERATOR_J1_J15_EQUALIZER_TERM_ON_I_flip`,
2. `DOR020_SCOPE_ADMISSIBILITY_AND_FULL_FINITE_BOTTOM_CERTIFICATE`,
3. `WITNESS_PACKAGE` summary for cross-verified certification review.

All three are unbuilt in this relay.

```text
P4 verdict = STOP
WITNESS_PACKAGE = STOPPED_AT(P1-P3)
```

---

## 5. P5 — falsifiers, regressions, and fresh attacks

### 5.1 Structural falsifiers and regressions

All lane-1 regressions relevant to this task were re-ran through the scoped
construction:
- nine-attack battery and anti-tuning ledger,
- finite-topology checks,
- cycle-sealing falsifiers (one-edge, first flip, two-flip, contact, asymmetric primitive).

No response value, root, or numeric quantity was used.

### 5.2 Fresh attacks

Two attacks were run in this completion pass:
- **Fresh attack A:** swap completion components with another admissible scoped
  profile and test whether `J2`, `J7`, `J12` persist; failure is again on joint
  consistency rather than restricted flip coherence.
- **Fresh attack B:** append admissible asymmetric primitive data to a flip scope
  state and test claimed DoR-020 coverage of `J15`; the flipped finite equalizer
  remains true while full package finite coverage remains unproven.

Both attacks confirm the same gap: internal coherence on `I_flip` does not
establish joint package witness conditions.

```text
P5 verdict = PASS / FAIL_ONLY_IF_SCOPE_CLAIMS_EXCEED_EVIDENCE = false
TAG_LEDGER = no-selection, no-tuning, no fixed-point, no end-test
```

---

## 6. Final lines

`SCOPED_EQUALIZER = INHABITED/STOPPED_AT`  
`ADMISSIBILITY = PROVEN/STOPPED_AT`  
`FINITE_BOTTOM = PROVEN/STOPPED_AT`  
`WITNESS_PACKAGE = ASSEMBLED/STOPPED_AT`

For this relay:

`SCOPED_EQUALIZER = STOPPED_AT` (only `Eq_flip` is present; not all six generators)

`ADMISSIBILITY = STOPPED_AT (I_flip lawful on geometry, not yet lawful DoR-020 scope)`

`FINITE_BOTTOM = STOPPED_AT (J15 full package bottom certificate missing on scope)`

`WITNESS_PACKAGE = STOPPED_AT (P1-P3 unresolved)`

```text
MEMBER_SELECTION: no member was selected
P4_SCOPE: partial support only on I_flip
```
