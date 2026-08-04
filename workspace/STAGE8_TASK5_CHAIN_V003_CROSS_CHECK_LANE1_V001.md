# STAGE 8 TASK 5 — LICENSED CONDITIONAL CHAIN V003 CROSS-CHECK — LANE 1 V001

```text
ARTIFACT_TYPE = ADVERSARIAL_CROSS_CHECK_OF_RECORD
REGISTER_HEAD_CHECKED = Q-460
ARTIFACT_UNDER_REVIEW = STAGE8_TASK5_LICENSED_CONDITIONAL_CHAIN_LANE2_V003.md
ARTIFACT_UNDER_REVIEW_SHA256 = f2b0b786ca20df1b96714d870811e14effa414724c1cfe08b35d63e31e301b7b

X1_ENTRANCE_GATE = PASS
X2_D_W_CERTIFICATE = PASS
X3_BOUNDED_DELTA = KILL (INFINITE_EDGE_BRANCH_NOT_INSTALLED_ON_THRESHOLD_LINE)
X4_FRESH_METRIC_DERIVATIVE_ATTACK = KILL

CHAIN_V003 = DEFECTIVE (X3,X4)

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Preflight and custody

The requested output and its seal did not exist at preflight. The artifact
under review was SHA-256 verified before reading, and its sidecar verified.
The questions-settled register sidecar verified and the head was Q-460.
`LOCKED_PROCESS.md` was read in full.

| Object | Verified SHA-256 | Role |
|---|---|---|
| chain V003 under review | `f2b0b786ca20df1b96714d870811e14effa414724c1cfe08b35d63e31e301b7b` | repaired chain |
| chain V002 | `1069e4f442ebfd083944c7cf6df8ba04058c531846fa61e1b6452d7ba551a269` | bounded-delta base |
| V002 cross-check | `9a8008b98ed48e61886e7e2d1e380dc72fe3d3a0b48480f2274b238ac05e0965` | exact K2/K3 repair standard |
| live questions-settled register | `d983fc12ab2a56c2f557a53c8e7d33dbd4970e8d6406ac724cc763966408d1e4` | Q-460 state |
| locked process | `1ee1c4188cf1ac1d37f40537a611407c0fd344387bd39421688f8b18478d8469` | governing process |

Custody is clean. This lane did not build V003. No register, plan, tracker,
git, commit, push, member binding, fixed-point execution, end test, numerical
evaluation, or measured-constant comparison was performed.

## 2. Verdict table

| Item | Verdict | Reason |
|---|---|---|
| X1 entrance gate | **PASS** | Step 0 requires the finite package certificate, adopted A2, and the inhabited actual antecedent; all remain conditional and undischarged |
| X2 `D_w` certificate | **PASS** | completeness is now an independent, falsifiable witness and Steps 4–7 cite it; Q-448 remains a branch-scope rejection only |
| X3 bounded delta | **KILL** | R1/R2 propagation is otherwise bounded, but the required `A_loop=infinity, chi_K=0` pointwise branch is still absent from Step 10 |
| X4 fresh attack | **KILL** | the alternate complete metric witness does not certify that Step 8's coordinate derivative computes Step 9's `d_w` Lipschitz modulus |

## 3. X1 — entrance gate

V003 defines

```text
ENTRANCE_020(F_actual,A2)
 := JOINT_FINITE_CERT(F_actual)
    and ADOPTED(A2)
    and FiniteCoherent_020(F_actual).                (X1-1)
```

The three conjuncts match the K2 repair one for one:

1. `JOINT_FINITE_CERT` is the full, cross-certified finite package, including
   its package functor, bottom, physical J2/J7, finite J1–J15 term, and joint
   diamonds. It is not a componentwise or provisional artifact.
2. `ADOPTED(A2)` is an adoption predicate, not the existence of a draft.
3. `FiniteCoherent_020(F_actual)` is the actual inhabited antecedent
   membership theorem, not six separate marginal memberships.

The current values are stated honestly:

```text
JOINT_FINITE_CERT(F_actual) = UNDER_CONSTRUCTION;
ADOPTED(A2) = false;
FiniteCoherent_020(F_actual) = unproved;
ENTRANCE_020 = NOT_YET_DISCHARGED.                  (X1-2)
```

Q-459's later killing of the provisional Stage-1 closures only strengthens
the first line of `(X1-2)`; it does not invalidate the gate's type.

Only under `(X1-1)` does Step 1 apply A2 and obtain a nonempty covariant
completed family. The result is existential and family-wide, not a Skolem
function. Step 2 is explicitly barred from manufacturing an entrance
conjunct. Steps 3–12 inherit Step 0, and the theorem-summary lines retain the
entrance condition. No later requirement was weakened to compensate.

The pending-certificate laundering test therefore passes: neither the Q-458
build nor any component certificate is accepted as an entrance token.

```text
X1 = PASS
ENTRANCE_PREMISES = three / exact
ENTRANCE_DISCHARGED = false
MEMBER_SELECTED = false
```

## 4. X2 — the complete physical return domain

### 4.1 Separate certificate

V003 adds `domain_complete_cert_w` to `C_ret[w]` and permits exactly two
witness forms:

```text
ClosedWitness_w:
  D_w is closed in complete K_amb,
  hence D_w is complete in the induced metric;

CompleteMetricWitness_w:
  (D_w,d_w) is complete,
  the inclusion into K_amb is continuous,
  and later norm/difference estimates use d_w.      (X2-1)

D_COMPLETE_w := ClosedWitness_w or CompleteMetricWitness_w. (X2-2)
```

This is failure-capable and independent of interval/convexity or absolute
continuity. It is fixed before the modulus, threshold, fixed point, or root.

Steps 4–7 now use the right object:

```text
Step 4: certify D_COMPLETE_w with the rest of C_ret;
Step 5: prove the bound on the same complete domain;
Step 6: prove B_w:D_w->D_w on that domain;
Step 7: invoke completeness from D_COMPLETE_w, not from K_amb. (X2-3)
```

Step 8 inherits all four steps explicitly. Ambient completeness plus branch
scope is no longer presented as a proof.

### 4.2 Foreclosed failure mode

For

```text
D_open=(0,1),
B_open(K)=(K+1)/2,
```

`D_open` is nonempty, interval-convex, invariant under `B_open`, and the exact
ordinary Lipschitz modulus is `1/2`. Nevertheless the iterates converge to
`1`, which is outside `D_open`; the induced ordinary metric is incomplete.
V003 rejects this at `(A2)` before the Banach steps. This exactly closes the
K3 witness.

The Q-448 domain `{-1,1}` is closed and complete, so the new item does not
misclassify it. It remains excluded only because it has no interval/convex or
absolute-continuity branch connecting the two points. The M16/N7 separation
is preserved.

```text
X2 = PASS
D_W_COMPLETENESS = independent_per-w_certificate
Q448_LAYER = Steps_3-4_branch_scope_only
```

## 5. X3 — bounded delta and retained attacks

### 5.1 Repair-surface comparison

The structural diff against V002 is confined to the required repair and its
necessary propagation:

- the new entrance block and Step 0;
- conditional Step 1 application of A2;
- `domain_complete_cert_w` and the `(A2)` witness alternatives;
- separation of completeness from branch regularity;
- propagation through Steps 4–7 and the cumulative Step-8 gate;
- the nonclosed-domain regression;
- strengthened condition/status tags and the corresponding falsifiers.

The stationary tuple, reader and Schur interfaces, symbolic `A_loop` formula,
Steps 8–12 escrow, no-selection rules, and protected-action registry are not
otherwise changed. The hidden-uniformity attack still passes only per `w`:
there is no common domain, no `sup_w q_w<1`, and no family-wide perturbation
theorem. The gate-bypass attack also passes because Step 8 explicitly inherits
Steps 0–7. The pending-cert entrance attack is honest and now even stronger
under Q-459.

### 5.2 Required edge branch omitted

The repair authority did not permit Step 10 to remain exactly as V002 wrote
it. It required the threshold line to state explicitly:

```text
A_loop=infinity and chi_K=0:
  q_loop=0 by pointwise annihilation,
  not by the undefined extended-real product 0 times infinity. (X3-1)
```

V003 Step 10 states only

```text
0<A_loop<infinity: |chi_K|<A_loop^(-1),
or the separately typed A_loop=0 case.             (X3-2)
```

It later says that prior branch-edge checks are unchanged, but it never puts
`(X3-1)` into the authorization map's threshold gate. That is not enough: the
chain's Step 10 is the consumer-facing exhaustive case split. On
`A_loop=infinity, chi_K=0`, `(X3-2)` supplies no licensed branch, while the
authority's pointwise theorem does.

This is a bounded omission, not a change to the finite-positive theorem. It
nevertheless violates the explicit repair condition and makes the delta
table's claim that edge typing was preserved false.

```text
X3 = KILL
HIDDEN_UNIFORMITY = PASS_PER_w_ONLY
GATE_BYPASS = PASS
PENDING_CERT_LAUNDERING = REJECTED
MISSING_EDGE = A_loop_infinity_and_chi_K_zero
```

## 6. X4 — fresh metric/derivative compatibility attack

This attack is new. It targets the second alternative in `(X2-1)`, not the
closed-subset horn.

Let

```text
D=(0,1),
h(x)=Log(x/(1-x)),
d_h(x,y)=|h(x)-h(y)|.                               (X4-1)
```

Then `(D,d_h)` is complete because `h` is an isometry onto the real line, and
the inclusion into the ambient scalar line is continuous. Thus `(X4-1)` can
carry V003's `CompleteMetricWitness` even though `D` is not closed in the
ordinary metric.

For a symbolic `a` with `0<a<1`, define

```text
B_a(x)=h^(-1)(a h(x)).                              (X4-2)
```

It is a self-map of `D`, and in the certified metric

```text
d_h(B_a(x),B_a(y))=a d_h(x,y).                     (X4-3)
```

Hence its true `d_h` contraction modulus is `a`. But its derivative in the
ambient scalar coordinate is

```text
B_a'(x)=a B_a(x)(1-B_a(x))/(x(1-x)).               (X4-4)
```

As `x` approaches `0`, `B_a(x)` is asymptotic to `x^a`, so
`B_a'(x)` is asymptotic to `a x^(a-1)` and is unbounded. Therefore

```text
sup_D |B_a'(x)|=infinity,
while Lip_(d_h)(B_a)=a<1.                           (X4-5)
```

V003 Step 5 correctly says the difference estimate must use `d_w`, but Steps
8–9 retain the coordinate derivative formula and identify its supremum with
the exact modulus. An arbitrary complete `d_w` plus continuous inclusion does
not justify that identification. A metric alone does not supply a compatible
differential norm.

The chain needs one further failure-capable condition on the
`CompleteMetricWitness` horn:

```text
either d_w is the restriction of the scalar norm used by the Schur derivative;
or a certified chart makes d_w a norm metric and Step 8 differentiates in it;
or Step 9 defines the modulus directly by the d_w difference quotient and
   separately proves equality with the displayed derivative coefficient. (X4-6)
```

Without `(X4-6)`, Step 9 can misreport the true contraction modulus even when
the repaired completeness and return gates pass. The fresh attack therefore
kills the repaired chain independently of X3.

```text
X4 = KILL
EXACT_GAP = D_W_METRIC_TO_STEP8_DIFFERENTIAL_COMPATIBILITY_CERTIFICATE
```

## 7. Final determination

The two original kills are repaired: the chain no longer starts beyond the
finite-package/A2 entrance, and it no longer infers completeness of `D_w`
from ambient completeness. No protected action was executed.

Confirmation still fails for two bounded reasons. The authority-required
infinite/zero edge branch is absent from Step 10, and the newly allowed
complete-metric horn lacks the compatibility theorem needed to identify the
Step-8 derivative supremum with the Step-9 metric modulus.

```text
X1 = PASS
X2 = PASS
X3 = KILL (A_loop=infinity,chi_K=0 branch absent from Step 10)
X4 = KILL (d_w/differential compatibility absent)

CHAIN_V003 = DEFECTIVE (X3,X4)

MEMBER_BINDING = none
FIXED_POINT_EXECUTION = none
END_TEST = none
NUMERIC_EVALUATION = none

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
