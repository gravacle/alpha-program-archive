# STAGE 8 TASK 5 - PACKAGE V003 FINAL CROSS-CHECK - LANE 1 V001

Date: 2026-08-04  
Task: PASTE 495 / Task 5 / continuum package  
Lane: Codex Lane 1  
Custody: final adversarial cross-check of the two Route-A/Route-B candidates

## Lead result

```text
ROUTE_A_BOUNDARY = NOT_EXACT |
  V003 correctly starts from Q-408's physical finite kernel and correctly
  stops before a full physical PL realization.  It nevertheless leaves a
  derivable rank-preserving path-subdivision square on the table.  Existing
  realized paths can be split by parameter restriction; the test-form map is
  the identity; path-current additivity gives A_n=S_nm^* A_m; and on the
  rank-preserving cycle image the Q-408 bilocal kernel square follows.

  The exact first unbuilt part is the extension from that path-only physical
  subcategory to newly introduced/interior PL edges and cells, together with
  their coframe/density/Riesz/Hodge data.  Route A's main TYPE-U obstruction
  is real, but its boundary is one subpackage too early.

ROUTE_B = DEFECTIVE |
  the conditional theory is nearly sound, but its end-test quantifiers are
  wrong.  H_020 = exists P in ContAdm_020 plus a generic theorem yields a
  P-indexed/existential family of results.  Failure of one exhibited P
  refutes that P, not the entire continuum package.  Whole-package
  refutation requires a uniform member-independent prediction, proof that
  every admissible P fails, or proof that ContAdm_020 is empty.

  Likewise, present failure to supply P leaves H_020 TYPE-U; it does not by
  itself refute H_020.  The licensing table says this elsewhere, but Cases 2
  and 3 and the retained package-wide end-test overclaim it.

REGRESSIONS = PASS |
  the abstract-kernel, circular-pi, false-reader-nonemptiness, and Hodge
  regressions are installed and V003 does not recur on any of them.

READY_FOR_DOR020_RULING = no
```

No route is selected or recommended.  Both defects are structural and
target-blind.  No response, threshold, fixed point, protected value, or
empirical comparison is evaluated.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
numeric_evaluation = false
registered_verdict_written = false
member_selected = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```

---

## 0. Preflight and custody

### 0.1 Three-line preflight

```text
DOES_THE_OBJECT_EXIST = yes | V003 contains Route A and Route B
IS_THE_VERSION_CURRENT = yes | register head Q-416
ARE_ITS_INPUTS_PRESENT = yes_for_final_cross_check
PREFLIGHT = PASS
```

The locked process was read in full.  V003 was SHA-256 verified and its
sidecar returned `OK` before V003 was read.

| Authority | Verified SHA-256 | Use |
|---|---|---|
| locked process | `e8a4c00d3cd13126bd8d20588419aba344a50d27c6d084a8243ed5494d7721f2` | custody and fences |
| register at Q-416 | `5c783e1cdbd78ed7ba92b64e5ff46c233ea9c32d11c138813e12fc4278fd2fd0` | current scope |
| V003 under review | `ee69fd1cb2a519d44d15520f838d243aff4fe734f6a120dda7523cffe751b938` | two-route proposal |
| Q-415 hostile check | `510ebda9c05220b3eb229e865a0a41868f5ce166ff2a5805762d540309a6ab1b` | kill anatomy and surviving PL core |
| Q-411 constraint system | `d7dcbc3ad7c470c8aaf0d8407db625d3e910cf180cd7b035fbc96bdfe58471b4` | J1-J15 standard |
| Q-413 adjudication | `67c4a5886c0b01cedae5ada0e13286cdf767f7247f7b36ebe4a65823fcd37885` | three repairs and witness burden |

### 0.2 Register sweep

```text
Q-408  Q-408's finite path-current and bilocal distribution maps are exact.
Q-409  C1-C3 are conditional on the physical completion/refinement package.
Q-410  the finite skeleton does not supply the full physical continuum seam.
Q-411  J1-J15 form one equalizer; inhabitance is independent.
Q-413  absence of a supplied member is TYPE-S for the artifact, not a no-go.
Q-415  F_PLDEC is killed; the PL divisibility/common-refinement core survives.
Q-416  V003 offers the concrete-witness route and conditional-inhabitance route.
```

### 0.3 Bearing symbol distinctions

```text
Ref_path   = refinements obtained by subdividing already realized Q-408 paths;
Ref_PL     = full order-complex/edgewise PL category, including new edges;
Ref_path is a nonempty physical subcategory, not all of Ref_PL.

H_020      = exists an evaluable P with certificate C(P);
[P,c_P]    = a particular bound witness and its certificate;
H_020 alone does not name P.

T(P)       = member-sensitive consequence;
T_uniform  = proved member-independent consequence;
one failed T(P) does not refute every P.
```

---

## 1. L1 - Route A's exact stopping point

### 1.1 What V003 gets right

Route A withdraws every false F_PLDEC claim and begins with the actual finite
map

```text
(A_G a)(c)=sum_e c_e integral_(gamma_e) a,

Kern_G^fin(H)[a,b]
 =H(R_K,G^(-1)A_G a,R_K,G^(-1)A_G b).            (L1-1)
```

It keeps the target-blind PL category but no longer calls its coefficient
operator a physical kernel.  It also correctly lists the still-unbuilt full
objects: physical density/Hodge data, uniform physical-kernel estimates,
completed faithfulness, independent localization/Maxwell projection,
physical readers, and action-derived response details.

Those stops reproduce Q-415 accurately.

### 1.2 The derivable path-subdivision subcategory

Let an already realized oriented edge have a parametrized Q-408 path

```text
gamma_e:[0,1]->M.
```

For a `q`-fold edge refinement, define child paths only from this existing
datum:

```text
gamma_(e,j)(t)
 :=gamma_e((j-1+t)/q),
j=1,...,q.                                         (L1-2)
```

This imports no smooth target and chooses no physical scale.  It merely
restricts the already adopted path parameter.  Concatenation and line
integration give, for every existing test one-form `a`,

```text
sum_(j=1)^q integral_(gamma_(e,j)) a
 =integral_(gamma_e) a.                            (L1-3)
```

Let `S_nm` copy the coarse current coefficient to its oriented child edges,
and keep the test-form space fixed, so `P_nm=id`.  Then

```text
J_(S_nm c)^m(a)=J_c^n(a),
A_n=S_nm^* A_m.                                    (L1-4)
```

On a pure path subdivision the cycle rank is unchanged.  The physical
current embedding identifies the coarse and refined current, so the
DoR-019 current metric restricts isometrically on this image.  Consequently
the Riesz map intertwines there, and direct substitution in `(L1-1)` gives
the rank-preserving Q-408 restriction square on that image.

```text
REF_PATH_PHYSICAL_CURRENT_SQUARE = BUILT
REF_PATH_Q408_KERNEL_SQUARE = BUILT_ON_RANK_PRESERVING_IMAGE
```

This is strictly narrower than a full realization of the order-complex
edgewise category.  Interior/barycentric edges that are not restrictions of
an existing `gamma_e` still have no physical path.  New cell densities,
coframes, Hodge masses, and cycle-creating directions also remain absent.

### 1.3 Corrected boundary

The exact Route-A order is therefore:

| Order | Status | Object |
|---|---|---|
| A0 | **BUILT** | Q-408 finite path-current/bilocal kernel on each actual carrier |
| A0.5 | **BUILT** | physical current and kernel square on rank-preserving subdivisions of already realized paths |
| A1 | **TYPE-U** | realization of genuinely new/interior PL edges and cells, plus density/Riesz compatibility |
| A2 onward | **TYPE-U** | full coframes/Hodge data, uniform completion, Loc/Maxwell split, reader, response/boundary |

V003 places the stop before A0.5 and says the cellular core supplies neither
the child paths nor test-form map.  Equations `(L1-2)`-`(L1-4)` refute that
claim on a nonempty subcategory.  The main obstruction survives, but the
boundary is not exact.

```text
L1 = KILL / derivable_rank_preserving_path_square_omitted
ROUTE_A_BOUNDARY = NOT_EXACT
```

---

## 2. L2 - Route B's conditional formalization

### 2.1 Sound core

V003 defines

```text
ContAdm_020=Eq(J1,...,J15),
H_020:=there exists an evaluable proof-carrying P in ContAdm_020. (L2-1)
```

It correctly states:

```text
no unconditional member exists;
no reader family is inferred from Q-407;
C1-C3 and DoR-008 are conditional on P and its certificates;
member-sensitive output remains P-indexed;
no posterior member choice or averaging is licensed;
no protected scalar is licensed without an evaluable P and authorization.
```

The correct theorem form is

```text
for every P, C(P) -> T(P).                         (L2-2)
```

With `H_020`, equation `(L2-2)` implies only

```text
there exists P such that C(P) and T(P).            (L2-3)
```

It does not produce a distinguished P or a unique member-sensitive value.
V003's licensing table mostly respects this.

### 2.2 Free-P notation must be bound

The tag `[H_020;P]` is sound only when it abbreviates a bound pair

```text
[P,c_P] with c_P:C(P).                             (L2-4)
```

If `H_020` is merely an existential proposition, P remains unbound.  Route B
can retain all generic theorems as `(L2-2)` and the full family
`{T(P):C(P)}`.  It cannot evaluate one branch without an exhibited witness
or a separately adopted selection rule.

This is a notation/quantifier repair, not a rejection of conditional
theories.

### 2.3 The end-test cases are not package-exact

V003 Case 2 says:

```text
one exhibited/evaluable P passes the chain but disagrees
 -> the continuum package is refuted whole.         (L2-5)
```

For a member-sensitive family, the valid conclusion is only

```text
P is refuted.                                       (L2-6)
```

The whole package is refuted only if one of the following is proved:

```text
all P with C(P) disagree;
the prediction is uniform over every P and that common prediction disagrees;
ContAdm_020 is empty or one of J1-J15 is inconsistent. (L2-7)
```

V003 Case 3 also needs its two readings separated:

```text
no P has yet been supplied -> H_020 remains TYPE-U/uninstantiated;
proof that no P can exist   -> H_020 is false and Route B is refuted.
                                                        (L2-8)
```

An unsuccessful search is not an emptiness theorem.  This is the same scope
precision Q-413 required of V001.

The earlier retained package-wide end test in Section 5.2 repeats `(L2-5)`
without the uniformity/member qualification, so the later licensing table
does not cure the internal conflict.

### 2.4 Correct sealed-test table

| Event | Licensed conclusion |
|---|---|
| exhibited P agrees | that instantiated P survives the end test; no other P is established |
| exhibited P disagrees | that P is refuted |
| proved uniform prediction disagrees | the entire inhabited package family is refuted |
| every admissible P proved to disagree | the package's physical family is refuted |
| no P currently supplied | Route B remains conditional/TYPE-U |
| ContAdm proved empty | H_020 is false |
| apparent agreement without P | no inhabitance evidence |

```text
L2 = KILL / end_test_quantifiers_and_free_P_binding
ROUTE_B = DEFECTIVE
```

---

## 3. L3 - permanent regression review

| Regression | Installed? | Exercised against V003? | Verdict |
|---|---|---|---|
| abstract-kernel substitution | yes, `REG-PHYS-KERNEL` | Route A uses exact Q-408 `(A-1)`; Route B requires J15 | **PASS** |
| circular physical projection | yes, `REG-NONCIRCULAR-PI` | Route A order `(A-5)` is independent; Route B requires J2 dependency order | **PASS** |
| false reader nonemptiness | yes, `REG-NONEMPTY-READER` | Route A leaves it conditional; Route B places it inside H_020 | **PASS** |
| Hodge from isometry | yes, `REG-HODGE-REFINEMENT` | Route A requires an intertwiner/form theorem; Route B puts it in certified P | **PASS** |

No F_PLDEC claim survives elsewhere in V003.  Algebraic reciprocal/S8-A
reader checks are explicitly marked conditional and are not promoted to
physical nonemptiness.

```text
L3 = PASS
```

---

## 4. L4 - comparison, delta, and battery

### 4.1 Neutrality

The route table states costs, licenses, risks, and falsifiers for A and B.
It contains no recommendation; `ROUTE_RECOMMENDED=none` and
`ROUTE_SELECTED=none` are honored.  Route B's status as the only currently
formalized option is not presented as evidence for its physical truth.

```text
NEUTRAL_COMPARISON = PASS
```

### 4.2 Delta

Direct V002/V003 comparison confirms the claimed substantive changes:

```text
F_PLDEC witness and 15/15 claims withdrawn;
J2/J5/J13 package rules retained;
PL category retained only as a formal core;
Route A rebuilt from the exact Q-408 finite map;
Route B introduced with H_020;
DoR-008 and algebraic readers retyped conditionally;
all four hostile regressions installed;
final board changed to two routes with no selection.
```

No killed W-9, W-17, physical-reader-nonempty, response-detail, or Hodge
claim remains live.

```text
DELTA_TABLE = PASS
```

### 4.3 Battery

Target tuning, compensation, posterior selection, graph norm, smooth-target
import, finite-injectivity promotion, contact deletion, cycle-creating
upward maps, hidden normalization, and abstract-kernel/circular-reader
attacks are handled honestly.

The battery does not catch the two findings here:

```text
Route A marks the entire physical path refinement TYPE-U although the
rank-preserving path restriction square is derivable;

Route B labels a one-member mismatch package-wide despite explicitly
retaining member-sensitive P-indexed outputs.
```

Therefore the battery is genuine but not passing as a final package audit.

```text
L4 = KILL / neutrality_and_delta_pass_battery_misses_L1_L2
```

---

## 5. L5 - fresh attacks

### 5.1 Route A fresh attack: path restriction

The construction `(L1-2)`-`(L1-4)` is independent of V003's prior battery.
It uses only the already realized Q-408 path and additivity of line
integration.  It recovers a nonempty physical restriction subcategory before
the stated A1 stop.

```text
FRESH_ATTACK_ROUTE_A = KILL / omitted_derivable_subsquare
```

### 5.2 Route B fresh attack: singleton refutation fallacy

Take two admissible members `P_1,P_2` with member-sensitive results
`T(P_1)!=T(P_2)`, a possibility V003 expressly retains.  If the opened test
disagrees with `T(P_1)` but agrees with `T(P_2)`, Case 2 declares the whole
package refuted while `P_2` remains an inhabitant that passes.  This is a
direct countermodel to the claimed package-wide conclusion.

```text
FRESH_ATTACK_ROUTE_B = KILL / one_member_is_not_the_family
```

---

## 6. Bounded repair

Route A needs a narrower boundary, not a new physical choice:

1. Add the derived `Ref_path` current and kernel restriction square.
2. State the TYPE-U stop at new/interior PL edges and cells plus their
   density/Riesz/Hodge realization.
3. Keep A2-A8 unchanged downstream of that corrected stop.

Route B needs a quantifier repair:

1. Replace `[H_020;P]` by explicit generic `[P,c_P]` theorem schemas.
2. Let H_020 assert only nonemptiness and license existential/family results.
3. Retype an individual mismatch as refuting that P.
4. Reserve package-wide refutation for uniform failure, all-member failure,
   or proved emptiness/inconsistency.
5. Separate "not yet supplied" from "proved nonexistent."

Neither repair chooses a route, member, scale, reader, or result.

---

## 7. Final verdict table

| Item | Verdict | Reason |
|---|---|---|
| L1 Route A boundary | **KILL** | rank-preserving physical path-subdivision square is derivable before the stated stop |
| L2 Route B | **KILL** | free-P binding and package-wide end-test quantifiers are wrong |
| L3 regressions | **PASS** | all hostile regressions installed and no recurrence |
| L4 comparison/delta/battery | **KILL** | comparison and delta pass; battery misses the two live defects |
| L5 fresh attacks | **KILL** | explicit counterexamples for each route |

```text
ROUTE_A_BOUNDARY = NOT_EXACT (+DERIVED_REF_PATH_SQUARE_REMAINS)
ROUTE_B = DEFECTIVE (+END_TEST_AND_EXISTENTIAL_BINDING)
READY_FOR_DOR020_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
