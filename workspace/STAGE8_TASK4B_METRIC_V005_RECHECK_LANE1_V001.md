# STAGE8 TASK 4B - CARRIER METRIC V005 RE-CHECK - LANE 1 V001

```text
TASK = PASTE 464 | bounded re-check of carrier metric V005
REGISTER_HEAD = Q-382
REVIEWED_ARTIFACT_SHA256 = 2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961

LEAD_RESULT:
  UNIT_DUALITY_STRUCTURE = PASS
  NO_IMPLICIT_CROSS_SECTOR_UNIT = PASS
  V004_CONTENT_INTACT = PASS
  COMPLETE_GAP_LEDGER = CLOSED
  FRESH_ATTACK = PASS | paired hidden conversions are caught before cancellation

METRIC_PACKAGE = READY
READY_FOR_DOR019_RULING = yes

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Preflight and custody

Preflight passed before V005 was read.

| Check | Result |
|---|---|
| register head | `Q-382` exactly |
| V005 SHA-256 | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` - match |
| V005 sidecar | verified `OK` |
| V004 re-check standard | `5e0ddafe8ff3b961308965996a75d0f976d8406ab0da6ae0a00f833d71713d40` |
| original gap standard | `2e1b011069043c1cc03277178be061a8b7d1704d2146be97eb799965aef9c679`, Section 4.2 |
| fullness standard | `f422a0340e253a72223f3c11d240b9b6a08b25a78ebf309085e84e965d8067ad` |
| V003 final-check standard | `8c72435ec53225d3dfe9fb4bba180f39ccf41009a025d36d42c404a3bce36571` |
| locked process | sidecar verified `OK` |
| register sidecar | verified `OK` |

Custody remained review-only. No register, plan, tracker, git, commit, push,
physical-value, root, `alpha`, `K_*`, or p-verdict action was performed.

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| A1 unit-duality structure | **PASS** | V005 explicitly supplies the dual C/K unit classes, corrected Riesz dual classes, orthogonal-torsor isomorphism classes, and the R4-only conversion set with finite/completed standing separated |
| A2 no implicit cross-sector unit | **PASS** | the certificate is failure-capable, excludes the forbidden bare identity, types every Schur factor, leaves `nu` symbolic, and requires any new conversion arrow to be separately declared |
| A3 V004 intact / quadruple delta | **PASS** | direct V004-to-V005 comparison finds no changed finite metric, fullness, W3, quotient, unit-power, or regression equation; the prior V001-V004 content ledger is complete |
| A4 complete gap ledger, battery, fresh attack | **PASS** | every previously missing object is derived or openly proposed, all permanent regressions pass, and the paired-hidden-conversion attack is rejected arrow by arrow even though its final units cancel |

## 2. A1 - unit-duality structure

### 2.1 Carrier and dual unit classes

V005 starts from the canonical Gate-4 pairing

```text
beta:C_prop x K_cycle -> R,
beta(c,k)=<c,k>.                                  (A1-1)
```

The finite pairing is the already-derived map

```text
beta_G([x])(c)=c^T x,
```

so it is scalar-valued and has no independent coefficient. If `C_prop`
has unit class `U_C` and `K_cycle` has unit class `U_K`, dimensionality of
`(A1-1)` gives

```text
U_C tensor U_K isomorphic to 1,
U_C=U_K^dual,
[K_cycle^*]=U_K^(-1)=U_C,
[C_prop^*]=U_C^(-1)=U_K.                         (A1-2)
```

This is forced on the finite/dense core by the nondegenerate pairing. V005
correctly separates the completed statement: transporting `(A1-2)` to the
named R5 carriers remains part of the proposed
`CARRIER_IDENTIFICATION_CERT` and is not mislabeled as already ratified.

```text
FINITE_UNIT_DUALITY = TYPE-P | beta
COMPLETED_UNIT_DUALITY = PROPOSED_NOT_ADOPTED
```

### 2.2 Corrected Riesz dual classes

For either carrier `A in {C,K}`, V005 uses

```text
R_A:A[U_A] -> A^*[U_A^(-1)],
[R_A]=U_A^(-2),
[R_A^(-1)]=U_A^(2),
(A^*)^* [U_A] isomorphic to A[U_A].              (A1-3)
```

The powers are correct: a map from an input of class `U_A` to an output of
class `U_A^(-1)` carries `U_A^(-2)`. This retains the V002 correction and
does not revive V001's obsolete forward-map power.

### 2.3 Orthogonal-torsor isomorphism classes

V005 explicitly supplies

```text
[U_Kmap] in Iso_isom(
  K_cycle,ell^2(I_Kindex;U_K))/O(I_Kindex),

[U_Cmap] in Iso_isom(
  C_prop,ell^2(I_Cindex;U_C))/O(I_Cindex).        (A1-4)
```

Only the Hilbert multiplicity classes are used. Postcomposition by an
orthogonal map changes a representative but not the metric or unit class.
Thus `(A1-4)` supplies the carrier-unit isomorphism classes required by the
original Section 4.2 gap without selecting an index set, basis, frame, or
isomorphism member.

The covariance scope is honest:

1. Rank-preserving W3 inclusions transport the classes by the ratified
   isometry/adjoint square.
2. Realization automorphisms and reality transport are conditional on the
   existing authored A4 isometry certificate.
3. Generic batching is not upgraded.
4. A cycle-creating stage receives its own class; no prohibited upward
   quotient map is inferred.

### 2.4 R4-only conversion set

The action Hessian blocks are typed as

```text
H_CK:K_cycle -> C_prop^*,
[H_CK]=U_action U_C^(-1)U_K^(-1),

H_KC:C_prop -> K_cycle^*,
[H_KC]=U_action U_K^(-1)U_C^(-1).                (A1-5)
```

V005's physical response conversion set is

```text
Conv_R4 := {
  H_CK,H_KC,
  reality-required adjoints,
  ordinary compositions through Inv_CC on its declared reducing domain
}.                                                (A1-6)
```

The finite pairing and same-sector Riesz maps remain available for duality
and domain typing, but V005 does not silently promote their mathematical
composites to new physical response arrows. Any new C/K mixing arrow must
be declared separately. This is exactly the requested R4-only boundary.

```text
A1 = PASS
```

## 3. A2 - NO_IMPLICIT_CROSS_SECTOR_UNIT

### 3.1 Failure-capable certificate

For every live expression, V005 requires:

```text
1. typed C/K inputs and outputs;
2. every mixing arrow named in Conv_R4;
3. R_C and R_K confined to their own sectors;
4. beta used only as dimensionless duality;
5. no U_C/U_K conversion coefficient or U_beta silently set to one;
6. transport of classes, not selected representatives.              (A2-1)
```

The package voids when any expression lacks such a factorization. This is
stronger than checking only the final output's dimensions.

### 3.2 Forbidden implicit-unit regression

The proposed bare coordinate identification

```text
chi_CK:C_prop -> K_cycle
```

has class

```text
[chi_CK]=U_K U_C^(-1)=U_K^2.                    (A2-2)
```

Writing `chi_CK=Id` therefore chooses a nonzero member of `U_K^2`. It is
neither the duality pairing nor an R4 block. Clauses 2 and 5 of `(A2-1)`
reject it, making the regression genuinely failure-capable.

### 3.3 Completed Schur mixing

The completed response consumes

```text
Schur=H_KK-H_KC Inv_CC H_CK,

[Inv_CC]=U_action^(-1)U_C^2.                    (A2-3)
```

Independent multiplication of the three mixed factors gives

```text
[H_KC Inv_CC H_CK]
 =(U_action U_K^(-1)U_C^(-1))
  (U_action^(-1)U_C^2)
  (U_action U_C^(-1)U_K^(-1))
 =U_action U_K^(-2)
 =[H_KK].                                        (A2-4)
```

No use of `U_C=U_K^dual` is even needed for the cancellation in `(A2-4)`;
the C factors cancel because every arrow is correctly typed. The Schur
subtraction is therefore lawful. Retarded extraction consumes the K-sector
result and adds no C/K identification.

### 3.4 Residual-parameter audit

There is no undeclared metric conversion parameter:

1. A separate `U_beta` is explicitly forbidden.
2. A bare C/K map is outside `Conv_R4` and requires its own declaration.
3. The scalar content of `H_CK` and `H_KC` belongs to the already-declared
   action/Hessian member; it is not a new metric conversion field.
4. A member of `U_C`, `U_K`, or `U_K^2` cannot be equated to `U_action`
   through any displayed seam.

Under dimensionless member scaling `phi_m -> lambda phi_m`, the jets and
`nu` scale while the carrier-unit torsors and orbit classes do not. Hence

```text
NU_HOMOGENEITY_PRESERVED = true
NU_FIXED_BY_UNIT_DUALITY = false
RESIDUAL_METRIC_CONVERSION_PARAMETER = none
```

```text
A2 = PASS
```

## 4. A3 - V004 content and quadruple delta

### 4.1 Direct V004-to-V005 audit

The direct unified diff has 339 insertions and 33 changed/deleted lines.
The non-insertion changes are version/preflight wording, references from
V004 to V005, the fourth choice-table row, expanded ledgers, and the final
board. No prior mathematical equation is altered.

The following V004 load-bearing content is present unchanged:

| V004 object | V005 check |
|---|---|
| A2-R10 fullness and `ker(I_K,G)=0` | present and unchanged |
| finite `g_K,G` and `R_K,G` | present and unchanged |
| `beta_G`, finite `g_C,G`, and `R_C,G` | present and unchanged |
| quotient supremum norm | present and unchanged |
| pendant/tree theorem | present and regression passes |
| W3 rank-preserving isometry and adjoint restriction | present on exact prior scope |
| null/quotient branch closure | present; no branch revived |
| corrected Riesz powers | present in every unit table |
| four-item authored residue | count unchanged; fourth row completed |
| R10, pendant, Z7, response-support, and hidden-scale regressions | retained and passing |

### 4.2 Four-baseline lineage audit

| Baseline | Content that must survive | V005 standing |
|---|---|---|
| V001 | dual C/K units and no-frame isomorphism classes | restored with corrected Riesz powers |
| V002 | forced semiform, finite C dual construction, unit table, and boundary accounting | retained; refuted null alternatives removed by later theorem |
| V003 | fullness, W3 derivation, null cleanup, four-item residue | retained |
| V004 | finite C metric/Riesz, quotient norm, pendant regression, complete restore | retained |

The V005 tables explicitly cover V002, V003, and V004. V001's required
unit surface is cited in the authority table and carried in the V002 delta
as the restored original unit-duality classes. Independent comparison with
V001 confirms the only intentional correction is
`[R_A]=U_A^(-2)` rather than its obsolete `U_A^2` assignment.

```text
FOURTH_LOSS = none found
QUADRUPLE_DELTA = PASS
A3 = PASS
```

## 5. A4 - complete gap ledger and fresh attack

### 5.1 Gap ledger

| Required object | V005 standing | Verdict |
|---|---|---|
| positive finite K metric | A4 pullback plus A2-R10 fullness | **SUPPLIED / TYPE-P** |
| finite `R_K` | positive finite Riesz isomorphism | **SUPPLIED / TYPE-P** |
| positive finite C metric | dual pullback through `beta_G` | **SUPPLIED / TYPE-P** |
| finite `R_C` | explicitly displayed finite Riesz isomorphism | **SUPPLIED / TYPE-P** |
| quotient-norm formula | representative-independent supremum | **SUPPLIED / TYPE-P** |
| pendant/tree quotient | zero gauge norm and positive visible-cycle regression | **SUPPLIED / TYPE-P** |
| faithful completion | forced mathematical completion; R5 naming remains proposed | **SUPPLIED / SPLIT** |
| rank-preserving transport | W3 isometry and adjoint restriction | **SUPPLIED / TYPE-P** |
| automorphism isometry | existing authored certificate with void tests | **SUPPLIED / PROPOSED** |
| positivity/reality convention | explicit completed convention | **SUPPLIED / PROPOSED** |
| carrier unit classes | formal `U_C,U_K` with no member | **SUPPLIED / PROPOSED** |
| dual carrier-unit relation | finite-derived and completed-proposed | **SUPPLIED / SPLIT** |
| carrier-unit isomorphism classes | orthogonal-torsor orbit classes | **SUPPLIED / PROPOSED** |
| corrected Riesz unit maps | `U_A^(-2)` / `U_A^2` | **SUPPLIED / TYPE-P** |
| R4-only conversion seam | `Conv_R4` with explicit exclusion rule | **SUPPLIED / PROPOSED** |
| no implicit cross-sector unit | failure-capable certificate and regressions | **SUPPLIED / PROPOSED** |

Every item from the original gap standard, the fullness review, the V003
final check, and the V004 re-check is now present with its actual standing.

### 5.2 Battery and permanent regressions

The following independent checks pass:

```text
R10 countermodel rejected as inadmissible;
fullness kernel zero;
finite C metric and R_C cannot evaporate;
quotient representative independence;
pendant/tree zero and visible-cycle positivity;
no response-support construction;
no nu calibration;
W3 not re-authored or overextended;
automorphism anisotropy remains a void test;
Riesz unit power corrected;
no null branch;
Z7 cycle-creation boundary retained;
external completed enlargement excluded;
single implicit C/K identity excluded;
Schur units homogeneous;
unit-map representative not selected.
```

### 5.3 Fresh attack - paired hidden conversions

An output-only dimensional test can be evaded by inserting two reciprocal
hidden arrows:

```text
chi_CK:C->K,       [chi_CK]=U_K U_C^(-1),
chi_KC:K->C,       [chi_KC]=U_C U_K^(-1),

chi_KC chi_CK:C->C,
[chi_KC chi_CK]=1.                               (A4-1)
```

A scalar parameter `s` could be placed in the first arrow and `s^(-1)` in
the second. Their units and parameter cancel in the final round trip, so a
check only on the final Schur/output class would miss them.

V005 still rejects `(A4-1)`: clauses 2 and 5 of its certificate inspect
each crossing, and neither `chi_CK` nor `chi_KC` is in `Conv_R4`. The pair
must therefore be omitted or declared as a new seam field even when always
consumed together. This demonstrates that the certificate is locally
failure-capable rather than merely an aggregate units check.

```text
FRESH_ATTACK = PASS
PAIRED_HIDDEN_CONVERSION_EVASION = excluded
```

### 5.4 Duality-rescaling control

For completeness, replace the pairing by `beta' = lambda beta`.

1. If `lambda` changes the actual pairing, it changes the sealed finite
   relation `beta_G([x])(c)=c^T x` and fails the finite falsifier.
2. If `lambda` only changes reciprocal representatives of the abstract
   unit torsors, it is unit bookkeeping and changes no orbit class or
   physical expression.

Thus there is no third case in which a physical cross-sector conversion
parameter survives silently.

```text
COMPLETE_GAP_LEDGER = CLOSED
A4 = PASS
```

## 6. Final determination

V005 closes the last metric-stratum gap without selecting a scale or
adding a fifth authored object. The finite Gate-4 pairing forces dual unit
classes; the no-frame carrier realizations are explicit orbit classes; the
completed statement remains honestly proposal-conditional; and every
physical C/K response crossing factors through the declared R4 blocks.

The full prior metric, fullness, quotient, W3, unit-power, and regression
content remains intact. No residual conversion parameter is silent: any
new conversion arrow is a separately declared ratification item by the
failure-capable certificate.

```text
A1 = PASS
A2 = PASS
A3 = PASS
A4 = PASS

METRIC_PACKAGE = READY
READY_FOR_DOR019_RULING = yes

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
