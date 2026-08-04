# STAGE 8 TASK 4B - GERM V003 RE-CHECK - LANE 1 V002

Date: 2026-08-03  
Task: PASTE 468 amended V002 / Task 4b  
Lane: CODEX LANE 1  
Status: **BOUNDED RE-CHECK COMPLETE - BOTH LIVE SHAPES READY**

```text
REGISTER_HEAD_AT_PREFLIGHT = Q-388
PREFLIGHT = PASS

ARTIFACT_UNDER_REVIEW =
  STAGE8_TASK4B_N_MEMBER_JET_INSTANTIATION_PROPOSAL_LANE2_V003.md
ARTIFACT_UNDER_REVIEW_SHA256 =
  231bbd1d77c39a45249149b47f9bb543e7a748c67b477dfde1f245efecd4aa13

BUILD_COMPARISON = AGREES
SHAPE_K = READY
SHAPE_CK_LAMBDA = READY
READY_FOR_DOR018_RULING = yes

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The archive artifact was hash-verified before it was read.  This review is
of that artifact of record.  The cleanroom product of Lane 1's accidental
467 execution is used only as a comparison object.

---

## 0. Preflight and custody disclosure

### 0.1 Preflight

The live questions-settled register was seal-verified and ended at `Q-388`.
The required inputs were present and independently hash-verified:

| Object | SHA-256 | Result |
|---|---|---|
| artifact under review, Lane 2 V003 | `231bbd1d77c39a45249149b47f9bb543e7a748c67b477dfde1f245efecd4aa13` | **PASS before read** |
| V002 baseline | `c673b6f59dda3981e02088676b11fa5606c882880d8f3b7111682e08175c5aa5` | **PASS** |
| Lane 1 V002 cross-review | `29787542deac3c45d71499e13a042d26ca959deb8a1557efd0ea85d246454331` | **PASS** |
| locked process | sidecar check | **PASS** |
| questions-settled register | sidecar check | **PASS** |

```text
DOES_THE_OBJECT_EXIST = yes
IS_THE_VERSION_CURRENT = yes | Q-388
ARE_ITS_INPUTS_PRESENT = yes
```

### 0.2 J0 - mispaste disclosure

Relay 467 was a Lane 2 build commission.  It was accidentally pasted into
Lane 1, and Lane 1 executed it as a builder.  The accidental run produced:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003/
  STAGE8_TASK4B_N_MEMBER_JET_INSTANTIATION_PROPOSAL_LANE2_V003.md

/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003/
  STAGE8_TASK4B_N_MEMBER_JET_INSTANTIATION_PROPOSAL_LANE2_V003.md.seal.sha256
```

The accidental run also issued the commission's mirror copy to the archive
pathname.  Therefore this lane does **not** make the historically stronger
claim that no filesystem write to that pathname was attempted.  The
reproducible custody claim is narrower and complete:

```text
SHA256(cleanroom build) =
  231bbd1d77c39a45249149b47f9bb543e7a748c67b477dfde1f245efecd4aa13

SHA256(archive artifact of record) =
  231bbd1d77c39a45249149b47f9bb543e7a748c67b477dfde1f245efecd4aa13

cmp(cleanroom build,archive artifact) = exit 0
CONTENT_OR_HASH_OVERWRITE = false
ZERO_FILESYSTEM_WRITE_ATTEMPT_ATTESTATION = not made
```

Thus the artifact of record is intact at its registrar-verified hash.  This
is the content-integrity meaning of Q-388's no-overwrite determination; it
does not erase the disclosed mirror command.

### 0.3 Build comparison

The comparison is byte-exact, so it is stronger than formula-by-formula
agreement but is not substituted for the adversarial review below.

| Commission item | Lane 1 accidental build | Artifact under review | Comparison |
|---|---|---|---|
| CK family | `nu(1+lambda q_C)f(s_K)`, `lambda in R` | same | **AGREES** |
| unabsorbability | constant and `q_C` coefficient comparison | same | **AGREES** |
| jets | all C/C, C/K, K/C, K/K blocks parameterized by `lambda` | same | **AGREES** |
| fiber | K / CK-lambda family / reject | same | **AGREES** |
| free inputs | ranks + `nu`; ranks + `nu+lambda` | same | **AGREES** |

No mathematical divergence exists between the two byte streams.

---

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| J0 mispaste disclosure and comparison | **PASS** | the accidental paths and mirror command are disclosed; archive content remains byte-identical at the registered hash; builds agree, with no zero-write-attempt claim |
| J1 Shape K unchanged | **PASS** | the complete Section 2 extraction compares byte-for-byte with V002, `cmp` exit `0` |
| J2 lambda retype | **PASS** | complete real relative-coefficient family, correct identifiability proof and jets, family-level DP1-DP10, no selected member |
| J3 free inputs and fiber | **PASS** | K has ranks plus `nu`; CK has ranks plus `nu+lambda`; future lambda disposition is derive-or-gate; reject remains live |
| J4 regression, delta, battery, fresh attack | **PASS** | the reviewer subfiber is permanent, every relevant certificate carries lambda, the delta is true, and the negative-lambda attack finds no undeclared premise |

---

## 2. J1 - Shape K byte custody

Both baselines matched their registered hashes before comparison.  The
compared byte span begins at `## 2. B1` and ends immediately before the next
level-two heading.  The command-level result was:

```text
cmp(Shape-K-section(V002),Shape-K-section(V003)) = exit 0
```

This covers the definition, generation statement, exact jets, stationary
structure, and neutral response consequence.  Shape K is not merely
mathematically equivalent; it is byte-unchanged as commissioned.

```text
J1 = PASS
SHAPE_K_VERBATIM = true
```

---

## 3. J2 - the lambda-family retype

### 3.1 Completeness on the commissioned CK skeleton

The V003 family is

```text
q_C(c)=(1/2)||c||_C^2,
s_K(k)=||k||_K^2,

phi_CK,lambda(c,k)
  =nu(1+lambda q_C(c))f(s_K(k)),
lambda in R.                                      (J2-1)
```

This is complete for the commissioned origin-normalized, lowest-even CK
relative-coefficient skeleton.  The reviewer's missing family is exactly
its displayed family, not merely a special member.  `lambda=0` is Shape K;
every nonzero real `lambda` is a CK member.  No positivity premise exists
that would lawfully narrow the real domain.

This completeness claim is deliberately scoped.  It does not claim that
all possible invariant smooth functions of `(q_C,s_K)` have been classified;
the flat-gate alternatives and reject remain in the authored choice table.

### 3.2 Unabsorbability

Assume two members agree for all `q` at a point with `f(s)!=0`:

```text
nu(1+lambda q)=nu'(1+lambda' q).                 (J2-2)
```

The constant coefficient gives `nu'=nu`.  For the nonzero N member, the
coefficient of `q` then gives

```text
nu lambda=nu lambda' => lambda=lambda'.          (J2-3)
```

In particular, rewriting a member as `nu'(1+q)` is possible only at
`lambda=1`.  A global amplitude multiplying both terms can be absorbed in
`nu`; the relative complement coefficient cannot.  V003 also states the
honest boundary: at `nu=0` all members degenerate to the Z member.

### 3.3 Independent jet recomputation

Let `c^flat=R_C c`, `k^flat=R_K k`, `q=q_C(c)`, and `s=s_K(k)`.  For
variations `h` in C and `u` in K,

```text
Dq[h]=<c,h>_C,
D^2q[h_1,h_2]=<h_1,h_2>_C,
Ds[u]=2<k,u>_K,
D^2s[u_1,u_2]=2<u_1,u_2>_K.                     (J2-4)
```

Differentiating `(J2-1)` gives

```text
D_C phi=nu lambda f(s)c^flat,
F_CC=nu lambda f(s)R_C,

D_K phi=2nu(1+lambda q)f_1(s)k^flat,

F_CK=2nu lambda f_1(s)c^flat tensor k^flat,
F_KC=(F_CK)^T,

F_KK=nu(1+lambda q)
  [2f_1(s)R_K+4f_2(s)k^flat tensor k^flat].      (J2-5)
```

These are exactly V003's four Hessian blocks.  Smooth flatness of `f` makes
the full derivative tower zero at `k=0`, including every finite active
restriction.  At `lambda=1` the formulas reproduce V002; at `lambda=0`
they reproduce Shape K.

### 3.4 DP1-DP10 family audit

| DP row | Re-check |
|---|---|
| DP1 | CK carrier explicitly includes the real dimensionless lambda coordinate; it is not hidden in `delta_div` |
| DP2 | no logarithmic coefficient is claimed consumed; `LOG_DIVERGENCE_PROVENANCE=false` remains explicit |
| DP3 | the authored coordinate and both carrier radii are displayed; datum-orbit directions are disclosed in the kernel |
| DP4 | lambda is constant under stage transport; only the displayed carrier coordinates acquire vertical differences |
| DP5 | the existing prefix-to-cycle handoff and ratified R5 C carrier are used; no rival map appears |
| DP6 | the generator takes `(delta,CK,lambda)` before jets or response consequences are read |
| DP7 | realization maps act trivially on lambda and covariantly/isometrically on C/K; all formulas are family-natural on the stated scope |
| DP8 | the independently stated finite leg contains lambda and vanishes to all orders on `k_N=0` |
| DP9 | full real lambda, `nu`, gate representative, shape tag, and branch family are disclosed as residual authored data |
| DP10 | the chronology fixes the family before differentiating or loading the Schur consumer |

The status remains `PASS_WITHIN_PROPOSAL`, not derived physics.  The
family coordinate is visible in DP1, DP3, DP4, DP6, DP8, and DP9, exactly
where the V002 review found it missing.

### 3.5 No-selection scan

Literal `lambda=0` and `lambda=1` occurrences are boundary and regression
checks only.  The proposal carries every real member, says
`LAMBDA_SELECTED=none`, keeps the rank pair symbolic, selects no root,
orientation, basis, frame, or branch, and computes no response value.

```text
J2 = PASS
LAMBDA_FAMILY_COMPLETE_ON_DECLARED_SKELETON = true
LAMBDA_SELECTED = none
```

---

## 4. J3 - free-input and fiber accounting

V003 states the free inputs exactly:

```text
Shape K:
  (r_0,r_ch) + nu;

Shape CK-lambda family:
  (r_0,r_ch) + nu + lambda;

reject:
  no new germ input; jet object remains TYPE-U.                 (J3-1)
```

The rank pair, `nu`, and `lambda` remain symbolic.  The family is a union
with identified boundary because `CK,lambda=0` equals K.  At the separate
zero-normalizer boundary, every germ equals the Z member; this disclosed
degeneration does not select a lambda value.

If the CK family is ratified, lambda's future disposition is explicitly:

```text
derive from new target-blind ratified structure;
or pass through its own explicit ratification gate.             (J3-2)
```

No preference is stated among K, the CK family, and reject, and no CK
member is recommended.  Member-sensitive consequences are labeled rather
than used to decide the fiber.

```text
J3 = PASS
FREE_INPUT_ACCOUNTING = exact
FIBER = K | CK_lambda_family | reject
```

---

## 5. J4 - regression, delta, battery, and fresh attack

### 5.1 Permanent lambda-subfiber regression

The battery now constructs

```text
{nu(1+lambda q_C)f(s_K):lambda in R}             (J4-1)
```

and confirms that every family certificate sees lambda.  The finite leg,
stationary equation, four Hessian blocks, R1-COV cube, stage cocycle,
DP table, minimal stages, operation ledger, free-input table, and final
board all carry the coordinate.  This closes H1/H4/H6/H7 from the V002
cross-review.

### 5.2 Delta truth

The complete textual diff against V002 was classified by the V003 delta
table.  The changed mathematics consists only of widening the implicit
`lambda=1` CK member to the full family and propagating that coordinate
through its certificates, jets, stationary equation, ledgers, and fiber.
Metadata and final-board label changes are separately listed.  The only
commissioned byte-carry requirement, Shape K Section 2, passes exact `cmp`.

No V002 passing metric, unit, covariance, cycle-creation scope, or fence
claim was silently weakened.

### 5.3 Existing battery

The ten recorded attacks pass on their stated scope: anti-tuning chronology,
finite flatness, rank-two covariance, pendant/tree quotient descent,
cycle-creating root honesty, cross-sector unit routing, zero degeneration,
stabilizers, hidden scale, and the lambda subfiber.  In particular, no
certificate obtains membership from a downstream block consequence.

### 5.4 Fresh attack - negative-lambda nodal shell

For `lambda<0`, the CK factor vanishes on the invariant shell

```text
q_C(c)=-1/lambda.                                (J4-2)
```

This is a genuine stress test of the claimed all-real domain.  It creates a
member-sensitive nodal shell and a sign change, and for fixed nonzero `k`
the C derivative is generally nonzero there:

```text
D_C phi|_(J4-2)=nu lambda f(s)c^flat.             (J4-3)
```

The shell does not break reality, isometry covariance, quotient descent,
R4 unit typing, finite flatness at `k=0`, or the local R5 scope.  No ratified
premise requires the action correction to be positive, pointwise nonzero
off the active section, or globally coercive.  Restricting to
`lambda>=0` would therefore be a new selection, not a derivation.

The attack passes but records a useful boundary: any future positivity or
global-coercivity requirement would narrow the admissible lambda set and
must be derived or separately gated.

```text
FRESH_ATTACK = negative_lambda_nodal_shell
FRESH_ATTACK_RESULT = PASS_WITH_DISCLOSED_MEMBER_SENSITIVITY
J4 = PASS
```

---

## 6. Fence and final board

No alpha, `K_*`, root, response value, rank ratio, or measured constant was
evaluated.  No p verdict was issued.  Structural differentiation and
family comparison only were performed.

```text
BUILD_COMPARISON = AGREES
SHAPE_K = READY
SHAPE_CK_LAMBDA = READY
READY_FOR_DOR018_RULING = yes

MACHINERY_APPEAL = false
P_VERDICT_COMPUTED = false
NUMERIC_RESPONSE_VALUE_COMPUTED = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No register, plan, tracker, git, commit, or push action was performed.
