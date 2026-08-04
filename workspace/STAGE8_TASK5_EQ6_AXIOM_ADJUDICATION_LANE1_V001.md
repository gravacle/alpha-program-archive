# STAGE 8 TASK 5 / EQ6 - COMPLETED-EXISTENCE AXIOM ADJUDICATION - LANE 1 V001

Date: 2026-08-04  
Lane: Codex Lane 1  
Task: PASTE 529 / Task 5 / EQ6  
Custody: adversarial adjudication; DoR-020-A2 reserved

## Lead result

```text
AXIOM = NOT_READY

KILLS =
  M16 / N7:
    FC12 imports C_ret branch regularity into EQ6 eligibility;
  T3 / T5-TRIVIALITY:
    no actual F_actual is proved to satisfy FC1-FC13 jointly, so the
    guarded universal may be vacuous or may miss the program's live tower;
  T4:
    Step 1 is therefore not discharged for the actual DoR-020 package.

MUST_TABLE = 15 PASS + 1 KILL (M16)
MUST_NOT_TABLE = 17 PASS + 1 KILL (N7)

FINITE_CONSERVATIVITY = PASS_RELATIVE
MEMBER_SELECTION = NONE / PASS
READER_CHI_FIBERS = UNTOUCHED / PASS
SKOLEM_ATTACK = PASS_WITH_NON_SKOLEM_SEMANTICS

READY_FOR_DOR020A2_RULING = no

MACHINERY_APPEAL = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The draft has the right completed-existence output and the wrong eligibility
edge.  It correctly asks for one covariant, non-selected, six-generator
J1-J15 family with exact finite reduct.  But it partly absorbs `C_ret` into
the guard and does not prove that the guard is inhabited by the actual
program datum.  Those are not editorial defects: together they mean the
proposed axiom does not yet discharge the obstruction for which DoR-020-A2
is being considered.

## 0. Preflight and authority verification

### 0.1 Three-line preflight

```text
DOES_THE_OBJECT_EXIST = yes
  | the Lane-2 draft exists at the named path
IS_THE_VERSION_CURRENT = yes
  | questions-settled register head Q-453 verified
ARE_ITS_INPUTS_PRESENT = yes
  | draft, 34-constraint standard, DoR-020+A1, counterexamples,
    Q-451/Q-452 stops, and twelve-step map are present
PREFLIGHT = PASS
```

The locked process was read in full.  The review hash was verified before
the draft was read.

### 0.2 Hash-verified review objects

| Object | SHA-256 | Result |
|---|---|---|
| Lane-2 axiom draft | `66c71bb619eac824b2d7d53fe36e49750945820428204f5b3db7f892bdfd1464` | **MATCH** |
| Lane-1 34-constraint standard | `96cd90b5bdcc2b77f510ebd21882b215aa5b70c944c9d58b2bdd8855fd52bf11` | **MATCH / seal OK** |
| questions-settled register at Q-453 | `f426dc279c1818f2cc82127e02097144b381458eecf1a79a9d0a6fc0bd86d596` | **MATCH** |
| twelve-step map V002 | `1069e4f442ebfd083944c7cf6df8ba04058c531846fa61e1b6452d7ba551a269` | **MATCH from authority chain** |

### 0.3 Draft clauses used in this review

```text
FC1-FC13                 finite-coherence guard;
completed items 1-9      completed realization requirements;
R1.4                     exact axiom formula;
R1.5                     no-selection / no-C_ret claims;
R2                       exclusions;
R3                       relative finite conservativity;
R4.5                     twelve-step consumption;
R5                       hostile battery and regressions.
```

The register's Q-453 statement that the two arms are aligned is treated as
context, not as an adjudication result.

## 1. T1 - the sixteen MUST constraints

| MUST | Draft clause(s) | Independent verification | Verdict |
|---|---|---|---|
| M1 existence only | R1.4 `NonemptyCovariantFamily`; R1.5; choice-table `strength` | No selector, least member, uniqueness, or canonical representative appears in the axiom formula. | **PASS** |
| M2 one joint equalizer | FC10-FC11; completed item 9; R1.4 | The conclusion requires one `W` carrying `Eq_J1-J15(W)`; six unrelated existentials do not satisfy it. | **PASS** |
| M3 six-generator fullness | completed item 9 and six named projections after it | All six DoR-020 generators are projections of the same completed tuple. | **PASS** |
| M4 DoR-008 conservativity | FC2; completed item 8; R3 | `Res_fin(W)=F` is exact componentwise and diagramwise, not asymptotic. The semantic conservativity proof is recomputed in Section 3. | **PASS** |
| M5 adopted-clause compatibility | FC1, FC6-FC7; finite datum list; completed items 2,5-7 | Path/current, bundle lift, connection, rank, characteristic class, density, contact, and response conditions remain in one tuple. | **PASS** |
| M6 actual surface geometry | FC1; R2.3; R5 A6/A11 | An abstract isomorphic kernel or rail-only diagram fails qualification. Actual Q-408 anchors are required. | **PASS** |
| M7 all-rank/common-refinement coherence | FC3, FC10-FC11; completed items 2,5,7,9 | Stagewise data are insufficient; cofinality, factor completeness, composition, and one joint tuple are output obligations. | **PASS** |
| M8 named completed analytic content | completed items 1,3-7; R5 A9/A12 | The draft uses DoR-019 carriers, one `tau_ker`, completed C1, faithfulness/quotient, C2 boundary, and C3 Hodge-Maxwell closure. A topology switch is rejected. | **PASS** |
| M9 covariance/no-selection | FC5; R1.4 definition of `NonemptyCovariantFamily`; R5 A8 | Full automorphism families are retained; signed/reality actions move the tuple without selecting a member. | **PASS** |
| M10 reality/batching/restrictions/units | FC5, FC7-FC8; completed items 1-2,6,8 | Ordered batching, W3 restrictions, reality, and the R4-only unit seam are explicit; no joint scalar or extra conversion is added. | **PASS** |
| M11 record-visible current preservation | FC4, FC6, FC9; completed items 4-5,8 | New-cycle kernels survive; faithful/quotient handling cannot delete a visible bulk cycle. | **PASS** |
| M12 relative no-leakage/support | FC6; R2.2; R5 A5 | The square-commuting old-to-new mixer fails the physical local-range test. | **PASS** |
| M13 admit `P=id` | R2.2 final sentence; R5.1 Q-432 row | The rank-preserving `P=id` control is admitted because an inherited old-old cross term is not transport leakage. | **PASS** |
| M14 J14 faithfulness dichotomy | FC9; completed item 4; choice-table `faithfulness` | The faithful horn needs a lower/separation certificate; otherwise a disclosed safe quotient with reader/localization annihilation is required. | **PASS** |
| M15 preserve fibers | R1.4-R1.5; choice-table `strength` and `witness form`; R5 A8 | The axiom adds no equality among completion members. The R1, Z/N comparison, reader `(chi_K,T)`, and `chi_K` fibers receive no selector or rigidity equation. | **PASS** |
| M16 `C_ret` separation | FC12; R1.5; R2.1; R4.1 `return scope` | The prose says `C_ret` is independent, but FC12 makes its interval/convex-or-AC branch condition part of EQ6 eligibility. The standard requires `CE_EQ6` to say nothing about this branch and leaves the exclusion to Steps 3-4. | **KILL** |

### 1.1 M16 computation

The constraint standard says:

```text
CE_EQ6 does not assert domain connectivity or branch regularity;
the disconnected branch is rejected later by C_ret clause D.
```

The draft says:

```text
FiniteCoherent_020(F) includes FC12;
FC12 requires an interval/convex or AC certificate when F carries a
stationary-return branch;
the disconnected branch is outside the axiom's domain.
```

Thus FC12 is not merely a statement that A2 fails to prove `C_ret`.  It
imports a `C_ret` predicate into the A2 antecedent and changes which otherwise
EQ6-admissible finite systems receive completion.  An EQ6-completable datum
with a disconnected return branch should receive an EQ6 completion and then
fail `C_ret`; under the draft it receives no A2 conclusion at all.

```text
M16 = KILL
REPAIR = delete FC12 from FiniteCoherent_020;
         move the disconnected-domain test wholly to C_ret/Steps 3-4
```

## 2. T2 - the eighteen MUST-NOT constraints

| MUST-NOT | Draft clause(s) | Independent verification | Verdict |
|---|---|---|---|
| N1 no marginal-to-joint substitution | FC10-FC11; completed item 9; R5 A3 | Six nonempty marginal fibers with incompatible shared data produce no `W`; the axiom conclusion is false. | **PASS** |
| N2 no stagewise-to-coherent substitution | completed items 2,5,7,9; R4.2 | Stagewise input does not count as completed/cofinal output. | **PASS** |
| N3 no choice/canonicalization | R1.4-R1.5; choice table | No `s(F)`, minimum, basis, frame, orientation, filtration, rank, or representative is introduced. | **PASS** |
| N4 no member-fiber collapse | R1.5; choice-table `strength` | Neither uniqueness nor contractibility is asserted; member-sensitive alternatives remain distinct. | **PASS** |
| N5 no reader/`chi_K` selection | finite datum includes the supplied reader; output includes `ell_bar`; no FC or output equation fixes `(chi_K,T)` | The axiom applies fiberwise to qualifying reader data and adds no reader value. | **PASS** |
| N6 no threshold/response tuning | FC13; R1.5; R5 A7 and order ledger | No response, modulus, threshold, fixed point, end value, or measured result occurs in a justification. | **PASS** |
| N7 no `C_ret` absorption | FC12; R2.1; R4.1 | FC12 imports exactly the branch-regularity clause reserved to `C_ret`. Labeling it `eligibility` does not remove the absorption. | **KILL** |
| N8 no new finite theorem | FC2; completed item 8; R3 | Every supplied completion has the same finite reduct. The relative semantic conservativity theorem passes; see Section 3. | **PASS** |
| N9 no abstract-kernel stand-in | FC1; R2.3; R5 A6 | Abstract dimensions/isomorphism do not satisfy the actual surface-anchor fields. | **PASS** |
| N10 no circular completion | finite datum exclusion after R1.1; FC13; R5 A2 | Completed Hodge/cofinal data and downstream readers are absent from the guard; no graph/response norm defines the input. | **PASS** |
| N11 no current deletion/false cycle square | FC4, FC6, FC9; R2.4; R5 A10 | Old-image restriction may be zero on a new test, but the target kernel remains nonzero and retained. | **PASS** |
| N12 no sector mixer | FC6; R2.2 | `1_(S2)P_mix1_(S1)!=0` fails RNL/local range even when rail squares commute. | **PASS** |
| N13 do not exclude `P=id` | R2.2; R5.1 | The draft distinguishes inherited old-old cross terms from created old-to-new leakage. | **PASS** |
| N14 no covariance-as-existence | FC5 is a guard; R1.4 separately postulates nonemptiness | Covariance transports output members but is not used as the proof of nonemptiness. | **PASS** |
| N15 no all-stage overclaim | R1.1 exclusion; completed items 3-7; R5.1 | Finite skeletons remain input cores and are not relabeled completed closures. | **PASS** |
| N16 no clause nonemptiness | FC7 treats A1 as finite law; R1.4 supplies only completed existence | The where-laws are not rewritten as witness theorems. | **PASS** |
| N17 no Hodge/isometry/objectwise shortcut | completed items 3,6; R2.4; R5 A9/A12 | Hodge closure, lower bounds, and one natural family remain substantive output certificates. Objectwise minima are absent. | **PASS** |
| N18 no bundle/topology/flat-holonomy laundering | FC1-FC2, FC7-FC8; completed items 1,8; R5 A12 | Bundle/rank/class mismatches and topology switches fail directly. A record-visible flat-holonomy change also changes the actual connection/old-path reduct and violates `Res_fin(W)=F`. | **PASS** |

### 2.1 Excluded counterexamples rerun

#### Disconnected return branch - wrong layer

For

```text
D={-1,1},
b(K)=K^3/2-3K/2,
```

the exact values are:

```text
b(-1)=1,
b(1)=-1,
b'(-1)=b'(1)=0,
q_der=0,
q_true=|1-(-1)|/|-1-1|=1,
Fix(b|D)=empty.
```

The draft correctly does not manufacture a fixed point, but it rejects the
datum through FC12.  The standard requires A2 to remain silent and `C_ret`
to reject it later.  Therefore the numerical-symbolic regression passes and
the layer placement fails: **N7 KILL**.

#### Sector mixer

Let an old `S1` current acquire a disjoint `S2` component.  Then

```text
1_(S2) P_mix 1_(S1) != 0.
```

FC6 fails independently of any commuting outer square.  **PASS / EXCLUDED.**

#### Abstract kernel

An isomorphic `K_abs` lacks the actual paths, connection, supports, tests,
and Q-408 map required by FC1.  **PASS / EXCLUDED.**

#### `P=id` witness

On rank-preserving `Ref_path`, there is no new local cycle sector and
`P=id`.  An inherited old-old metric cross term does not make
`1_(Snew)P1_(Sold)` nonzero.  **PASS / ADMITTED.**

#### Pure new-cycle profile

A target test supported only on a newly created cycle has zero old-image
restriction while the target physical kernel is nonzero.  FC4 and exact
restriction retain the target class; no upward quotient is inferred.
**PASS / RETAINED.**

#### Flat-holonomy mismatch

Take equal characteristic class and curvature but connections differing on
an old record-visible path by a closed non-gauge one-form.  FC7 alone would
not separate them.  FC1 fixes the actual connection and FC2/completed item 8
require exact old-path reduct, so the changed holonomy fails qualification or
`Res_fin(W)=F`.  **PASS / EXCLUDED BY ACTUALITY PLUS EXACT REDUCT.**

#### Infinite-support completed null vector

Finite faithful restrictions do not prove completed faithfulness.  Completed
item 4 requires a lower/separation certificate or the safe quotient horn.
**PASS / FAITHFUL-HORN CLAIM REJECTED.**

## 3. Finite-conservativity recomputation

The draft's symbol-replacement proof is informal, but the theorem follows
semantically on its stated relative scope.

Let `K_fin` be the class of finite structures satisfying the guard with FC12
temporarily ignored for the EQ6 question, and let `K_ext` be the class of
completed structures satisfying the output conditions.  Exact restriction
gives:

```text
Red_Lfin(K_ext) subset K_fin.
```

If the completion axiom is true for every datum in its declared domain, then
every guarded finite structure has at least one expansion, so:

```text
Red_Lfin(K_ext) = K_fin.
```

Therefore, for every finite-language sentence `phi`,

```text
K_ext models phi  implies  K_fin models phi.
```

No finite object or value changes, and no finite theorem is added relative to
the guard.  This proves M4/N8 for the axiom form.  It does not prove the guard
is inhabited and does not cure the scope defects below.

```text
FINITE_CONSERVATIVITY = PASS_RELATIVE
ABSOLUTE_UNGUARDED_CONSERVATIVITY = not_claimed
```

## 4. T3 - scope audit

### 4.1 Overbreadth

The draft does not quantify over arbitrary formal diagrams.  FC1-FC11/FC13
restrict the domain to actual finite-coherent surface data, and the output
must extend the same actual reduct.  Its universal range is broader than the
single `I_flip` datum, but that broader range is openly authored axiom content
and remains failure-capable.  No overbreadth counterexample survives the
guard.

```text
SCOPE_OVERBROAD = false on FC1-FC11/FC13
```

### 4.2 Underbreadth from FC12

An otherwise qualifying EQ6 datum may carry a disconnected return branch.
EQ6 completion and C_ret admissibility are independent by Q-448/Q-450.  FC12
removes that datum from A2 even though its EQ6 completion question is well
typed.  Thus the domain is under-inclusive by an unrelated predicate.

```text
SCOPE_UNDERBROAD = true / FC12
```

### 4.3 Domain inhabitance / triviality

The draft does not construct an `F_actual` and prove

```text
FiniteCoherent_020(F_actual).
```

It says only that the current stock "supplies the kinds" in FC1-FC13 on its
proved finite/Ref_path/flip scopes.  That is not the conjunction:

```text
exists one F_actual:
  FC1(F_actual) and ... and FC13(F_actual).
```

Q-451 records `SCOPED_GENERATOR_COUNT=1/6`, no full finite-bottom package,
and no scoped J1-J15 term.  Q-452 builds the five local cores but still records
`JOINT_ON_IFLIP=STOPPED_AT`, with the simultaneous term and consumer-complete
scope absent.  The draft's FC10-FC11 require exactly one finite joint term.

Two consequences follow:

1. If no `F` satisfies the guard, the universal implication is vacuously
   true and supplies no completed existence.
2. If some small/trivial finite `F` satisfies it, that does not establish the
   guard for the actual DoR-020 program tower.

The current artifact proves neither the domain's nonemptiness nor membership
of the live program datum.  The triviality attack therefore succeeds.

```text
ACTUAL_DOMAIN_INHABITED = NOT_PROVEN / TYPE-U
AXIOM_APPLICABLE_TO_LIVE_PROGRAM_DATUM = NOT_PROVEN / TYPE-U
T3_SCOPE = KILL

REPAIR =
  construct and name F_actual;
  prove FC1-FC11 and FC13 jointly on it;
  prove its declared domain is covariant and consumer-complete;
  remove FC12.
```

This repair is not the forbidden completed witness: it proves the finite
antecedent on one actual tuple.  The axiom would then supply only its completed
extension.

## 5. T4 - twelve-step consumption

| Step | Draft claim | Adjudicated status |
|---|---|---|
| 1 joint EQ6 verification | discharged for each qualifying `F` | **CONDITIONAL FORM CORRECT; LIVE DISCHARGE NOT PROVEN because no `F_actual` membership theorem exists** |
| 2 finite/rail regressions | inputs, not replaced | **PASS / STILL MANDATORY** |
| 3 construct `C_ret` | not discharged | **FORMALLY PASS, but FC12 must be removed to make separation genuine** |
| 4 certify `C_ret` and branch | not discharged | **FORMALLY PASS, same FC12 defect** |
| 5 boundedness | `[EQ6]+C_ret` conditional | **OPEN** |
| 6 closure | `[EQ6]+C_ret` conditional | **OPEN** |
| 7 branch completeness | `C_ret_SCOPE` conditional | **OPEN** |
| 8-10 derivative/modulus/threshold | structurally consumable only after prior gates | **OPEN / NOT EXECUTED** |
| 11 fixed point | theorem-only and escrowed | **OPEN / NOT EXECUTED** |
| 12 sensitivity/evaluation | A32 and evaluation still required | **OPEN** |

What survives after a repaired A2 adoption:

```text
checkpoint certification;
C_ret and its branch scope;
all completion/member fibers;
the R1 and Z/N-sensitive member structure;
the reader (chi_K,T) and chi_K fibers;
member binding;
A32;
fixed-point execution;
evaluation/end test.
```

The present V001 cannot truthfully report Step 1 discharged for the live
program until the finite guard is inhabited.  Its table is propositionally
correct and operationally premature.

## 6. T5 - battery audit and fresh attacks

### 6.1 Draft battery

| Draft attack | Recheck | Verdict |
|---|---|---|
| A1 triviality/proves too much | It rejects abstract diagrams but never proves `exists F_actual FiniteCoherent_020(F_actual)`. This tests overbreadth, not vacuity. | **KILL / INCOMPLETE ATTACK** |
| A2 circularity | No completed output field is used as an antecedent. | **PASS** |
| A3 componentwise equalizer | One tuple is required. | **PASS** |
| A4 disconnected return | Computation correct; placement in FC12 violates N7. | **KILL / WRONG LAYER** |
| A5 sector mixer | FC6 detects the mixer. | **PASS** |
| A6 abstract kernel | FC1 detects the stand-in. | **PASS** |
| A7 target tuning | Construction order is blind to outcomes. | **PASS** |
| A8 hidden selection | Full covariance family retained. | **PASS** |
| A9 finite/completed faithfulness | Hidden completed null vector defeats faithful horn absent lower certificate. | **PASS** |
| A10 cycle compression | FC4 plus exact reduct retain the target kernel. | **PASS** |
| A11 rail-only completion | FC1/FC6/FC7 reject it. | **PASS** |
| A12 topology switch | One `tau_ker` requirement rejects it. | **PASS** |

### 6.2 Fresh attack 1 - genuine triviality

Interpret the axiom in any structure with:

```text
Fin_020 = empty.
```

Then

```text
for every F, FiniteCoherent_020(F) -> NonemptyCovariantFamily(...)
```

is true, while no completed family exists.  The draft contains no theorem
excluding this model.  Replacing `Fin_020=empty` by a category containing only
a small control datum produces the same failure for the live program tower.

```text
FRESH_TRIVIALITY_ATTACK = SUCCEEDS
```

### 6.3 Fresh attack 2 - Skolem-style choice

The axiom formula contains a nonemptiness proposition over the definable
groupoid of all admissible `W`.  It does not introduce a symbol

```text
s : F -> W
```

or an elimination rule that binds `s(F)`.  Classical Skolemization can add a
fresh function in an equisatisfiable meta-language, but that function is not
part of the proposed physical theory and cannot be consumed by the
twelve-step map.  The draft also explicitly forbids member binding.

Thus the Skolem attack does not find a choice function in V001.  To keep this
pass stable, any A2 decision text must preserve nonemptiness as a proposition
(or propositionally truncated existence) and must not name a witness.

```text
FRESH_SKOLEM_ATTACK = PASS
HIDDEN_CHOICE_FUNCTION = absent
```

### 6.4 Fresh attack 3 - guard strengthening by downstream structure

Take two identical EQ6 finite data, one carrying no return branch and one
carrying the disconnected Q-448 branch as additional downstream data.  Their
EQ6 finite reducts and completion problem are identical.  The draft completes
the first and refuses even to state completion for the second.  Hence FC12
changes A2 applicability using data that the completed-existence conclusion
does not consume.  This independently confirms the M16/N7 kill.

```text
FRESH_GUARD_STRENGTHENING_ATTACK = SUCCEEDS
```

### 6.5 Geometry versus rails

```text
SURFACE_GEOMETRY:
  FC1-FC11/FC13 correctly anchor the antecedent in actual finite paths,
  currents, cycles, supports, bundle fields, and exact restrictions.

RAILS:
  the new principle is existence of the completed joint equalizer.

DEFECT:
  no actual surface tuple is proved to inhabit the rail's guard, and FC12
  imports the separate return rail into that guard.
```

The draft is not killed for lacking geometric content in its definition.  It
is killed because the defined rail is not shown to start from the live
geometry and because it bills an independent rail to entry.

## 7. Repair boundary and final verdict

The repair is bounded and exact:

```text
R1  remove FC12 from FiniteCoherent_020;
R2  state that disconnected return data remain eligible for A2 and fail only
    when C_ret is separately attempted;
R3  construct/name F_actual on the live program finite tower;
R4  prove FC1-FC11 and FC13 jointly for F_actual, including the actual
    finite-bottom and covariance/no-selection domain certificate;
R5  change the consumption board from "for each qualifying F" to an actual
    Step-1 discharge only after R3-R4.
```

Everything else in V001 may be carried forward subject to a true delta.  No
member, reader, completion, or result needs to be selected to make this
repair.

## Final board

```text
M1-M15 = PASS
M16 = KILL

N1-N6 = PASS
N7 = KILL
N8-N18 = PASS

FINITE_CONSERVATIVITY = PASS_RELATIVE
SCOPE_OVERBROAD = false
SCOPE_UNDERBROAD = true / FC12
ACTUAL_DOMAIN_INHABITED = NOT_PROVEN / TYPE-U
STEP1_LIVE_DISCHARGE = NOT_PROVEN
MEMBER_SELECTION = NONE
C_RET_ABSORBED = true_in_guard_only / defect
READER_CHI_FIBERS = UNTOUCHED
SKOLEM_CHOICE = absent

AXIOM = NOT_READY (M16, N7, T3, T4, T5-triviality)
READY_FOR_DOR020A2_RULING = no

FENCE_BLOCKED_STRUCTURAL_RESULT = false
MACHINERY_APPEAL = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
