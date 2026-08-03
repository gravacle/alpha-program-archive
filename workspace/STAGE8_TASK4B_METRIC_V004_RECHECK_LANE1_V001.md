# STAGE8 TASK 4B - CARRIER METRIC V004 RE-CHECK - LANE 1 V001

```text
TASK = PASTE 462 | bounded re-check of carrier metric V004
REGISTER_HEAD = Q-380
REVIEWED_ARTIFACT_SHA256 = c819d03a9b540ae1cd2bf76e90277ecc2b146ce951618e54729798d3201649f5

LEAD_RESULT:
  FOUR_REQUESTED_RESTORATIONS = PASS
  V003_CLEANUP = PASS
  DOUBLE_DELTA = KILL | one third loss is omitted
  ORIGINAL_GAP_LIST = KILL | carrier-unit isomorphisms remain absent
  FRESH_ATTACK = succeeds | hidden cross-sector conversion unit

METRIC_PACKAGE = NOT_READY (Y3, Y4)
READY_FOR_DOR019_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Preflight and custody

Preflight passed before the artifact was read.

| Check | Result |
|---|---|
| register head | `Q-380` exactly |
| V004 SHA-256 | `c819d03a9b540ae1cd2bf76e90277ecc2b146ce951618e54729798d3201649f5` - match |
| V004 sidecar | verified `OK` |
| V003 final-check standard | `8c72435ec53225d3dfe9fb4bba180f39ccf41009a025d36d42c404a3bce36571` |
| fullness standard | `f422a0340e253a72223f3c11d240b9b6a08b25a78ebf309085e84e965d8067ad` |
| original gap standard | `2e1b011069043c1cc03277178be061a8b7d1704d2146be97eb799965aef9c679`, Section 4.2 |
| V002 baseline | `7788e29da98be54e983a660768c0c70258e7d6d89eb51a2dafc4dbe17a9ea825` |
| V003 baseline | `29ec770a8299fccadd68456b150f041eb64651ca2ba080b8a1c56c102f120fc9` |

Custody remained review-only. No register, plan, tracker, git, commit, push,
physical-value, root, `alpha`, or `K_*` action was performed.

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| Y1 four dropped items | **PASS** | V004 explicitly constructs finite `g_C,G`, `R_C,G`, the representative-independent quotient norm, and the pendant/tree regression, and each computation is correct |
| Y2 V003 cleanup | **PASS** | the A2-R10 fullness chain, removal of null branches, W3 rank-preserving isometry, corrected `U_A^(-2)` Riesz units, and four-row authored residue are retained |
| Y3 double delta | **KILL** | V004's delta tables omit the continuing loss of the dual carrier-unit relation and the carrier-unit isomorphism classes present in V001 and required by the original gap standard |
| Y4 full gap list, battery, regressions, fresh attack | **KILL** | the metric and quotient regressions pass, but formal unit labels plus Riesz powers do not supply carrier-unit isomorphisms; the fresh hidden-conversion-unit attack succeeds |

The Y3/Y4 defect does not refute the restored metrics. It is a bounded missing
interface in the fourth authored row.

## 2. Y1 - the four requested restorations

### 2.1 Finite C-side metric

V004 defines, at every admitted finite stage `G`,

```text
beta_G:Q_G^lin -> K_G^*,
beta_G([x])(c)=c^T x,

g_(K_G^*)(ell,m)
  =g_K,G(R_K,G^(-1)ell,R_K,G^(-1)m),

g_C,G(q,q')
  =g_(K_G^*)(beta_G q,beta_G q').                 (Y1-1)
```

The definition is positive definite. If `g_C,G(q,q)=0`, then
`beta_G q=0`; fullness and Gate-4 nondegeneracy make `beta_G` injective, so
`q=0`. No response-facing datum or basis is used.

```text
FINITE_C_METRIC_RESTORED = true | TYPE-P
```

### 2.2 Finite C-side Riesz map

V004 then displays

```text
R_C,G:C_G -> C_G^*,
(R_C,G q)(q')=g_C,G(q,q').                        (Y1-2)
```

Finite dimensionality and positive definiteness make `R_C,G` an
isomorphism. This is derived finite content and is correctly excluded from
the DoR-019 authored residue.

```text
FINITE_R_C_RESTORED = true | TYPE-P
```

### 2.3 Quotient norm

V004 restores

```text
||[x]||_C
  =sup_(0!=c in K_G) |c^T x|/||c||_K.             (Y1-3)
```

For a vertex rephasing `x -> x+B_G theta`,

```text
c^T(x+B_G theta)
  =c^T x+(B_G^T c)^T theta
  =c^T x.                                         (Y1-4)
```

Thus `(Y1-3)` is representative-independent. It is zero exactly on the
zero Gate-4 class: one direction is immediate, while the converse follows
from the nondegenerate pairing of `Q_G^lin` with `K_G`.

```text
FINITE_QUOTIENT_NORM_RESTORED = true | TYPE-P
```

### 2.4 Pendant/tree regression

On a connected tree,

```text
K_G=ker(B_G^T)=0,
Q_G^lin=0.                                        (Y1-5)
```

For a cyclic graph with a pendant tree edge, a pendant-only variation is a
vertex coboundary and therefore has zero pairing with every `c in K_G`.
Equation `(Y1-3)` gives it zero quotient norm. A nonzero cycle-holonomy
class has a cycle `c` with `c^T x!=0`, hence positive norm.

```text
PENDANT_TREE_REGRESSION = PASS
VISIBLE_CYCLE_SURVIVES = true
```

### 2.5 Source precision

The task describes all four objects as reinstated "verbatim from V002".
That description is not literally true at the text level:

1. V002 contains the finite evaluation map and finite dual C metric.
2. V002 does not display the finite `R_C,G` equation.
3. V002 does not display the quotient supremum formula.
4. V002 mentions the pendant regression but does not contain V004's full
   theorem in this form.

Those latter formulas are restored from the earlier metric package and the
original gap standard, then corrected by the V002/V003 findings. This is a
provenance-precision note, not a mathematical Y1 kill: every requested
object is present and independently passes.

```text
Y1 = PASS
```

## 3. Y2 - V003 cleanup retained

### 3.1 Fullness and positive K form

V004 retains the A2-R10 chain

```text
-i h_e^(-1) d h_e(a,theta)
  =(L_G a)_e+(B_G theta)_e,

A2-R10 => image(L_G)+image(B_G)=E_G.              (Y2-1)
```

If `c in ker(B_G^T)` and `u_c=0`, then for every
`x=L_G a+B_G theta`,

```text
c^T x=u_c(a)+(B_G^T c)^T theta=0.
```

Nondegeneracy gives `c=0`. Hence

```text
ker(I_K,G)=0,
g_K,G(c,d)=g_A4(u_c,u_d)
```

is positive definite on the full admitted cycle carrier. The old
countermodel is correctly retained only as an inadmissibility regression
because it violates R10.

### 3.2 Null branches and W3

V004 correctly closes the former null alternatives:

```text
K_G/ker(I_K,G)=K_G/0=K_G.
```

It also preserves the exact W3 scope: rank-preserving source inclusions are
isometric and finite restrictions are their adjoints. It does not promote
that theorem to generic batching, cycle-creating upward maps, or realization
automorphisms. The latter remains an authored certificate.

### 3.3 Riesz powers and authored count

The unit powers are dimensionally correct:

```text
R_A:A->A^*,
[R_A]=U_A^(-2),
[R_A^(-1)]=U_A^(2), A in {C,K}.                   (Y2-2)
```

The live authored residue still has four rows:

```text
1. completed-carrier identification;
2. positivity/reality completion convention;
3. A4 automorphism isometry;
4. carrier units and the R4 seam.
```

No rank, ratio, frame, cycle basis, unit member, `nu`, or response value is
selected.

```text
Y2 = PASS
```

## 4. Y3 - the double delta is incomplete

The two delta tables correctly account for the four restored geometric
items and the V003 fullness/W3 cleanup. They are not complete against the
original carrier package and Section 4.2 gap standard.

The original carrier package explicitly supplied

```text
U_C:=U_K^*,

[U_Kmap]:K_cycle -> ell^2(K;U_K) modulo O(K),
[U_Cmap]:C_prop  -> ell^2(C;U_C) modulo O(C).      (Y3-1)
```

No frame member was selected: the maps were orthogonal-torsor classes.
The original gap standard then expressly found that R4 contained no
carrier-unit isomorphism for `C_prop` or `K_cycle`.

V004 contains only:

```text
formal U_C,U_K;
the Riesz powers (Y2-2);
the action-derivative unit table;
the statement that no torsor member is selected.
```

It contains neither `U_C:=U_K^*` nor either isomorphism class in `(Y3-1)`.
Its V003 delta nevertheless says the four-item residue is unchanged and its
final board says the carrier units/R4 seam is complete. Therefore:

```text
THIRD_LOSS = carrier-unit duality and isomorphism classes
DELTA_V002 = incomplete
DELTA_V003 = incomplete
Y3 = KILL
```

This does not require a fifth authored row if repaired correctly. It belongs
inside the existing carrier-units/R4 row.

## 5. Y4 - original gap list and fresh attack

### 5.1 Gap ledger

| Original required object | V004 standing | Verdict |
|---|---|---|
| positive finite K metric | derived from A4 plus A2-R10 | **PASS** |
| finite `R_K` | derived Riesz isomorphism | **PASS** |
| positive finite C metric | restored by pullback through `beta_G` | **PASS** |
| finite `R_C` | restored explicitly | **PASS** |
| quotient-norm descent | restored by the supremum formula | **PASS** |
| pendant/tree gauge regression | restored and passed | **PASS** |
| completed carrier identification | live authored certificate with alternatives and void conditions | **PASS / PROPOSED** |
| rank-preserving orthogonal transport | W3-derived on its exact scope | **PASS** |
| realization automorphism isometry | openly authored with failure tests | **PASS / PROPOSED** |
| carrier units | formal torsor labels present | **PARTIAL** |
| carrier-unit isomorphisms | absent | **KILL** |
| R4 action-unit seam | derivative and Riesz powers displayed, `nu` symbolic | **PASS subject to the missing unit maps** |

### 5.2 Battery and permanent regressions

The following V004 tests recompute successfully:

```text
R10 countermodel exclusion;
positive finite K and C forms;
finite R_K and R_C isomorphisms;
representative independence;
pendant/tree zero norm;
visible cycle positive norm;
W3 rank-preserving isometry and adjoint restriction;
no cycle-creating upward map;
no null branch;
no response-support selection;
correct U_A^(-2) Riesz power.
```

The battery does not test for the presence of the maps `(Y3-1)`. Its unit
test catches a reversed Riesz power or a fixed numerical scale, but not an
untyped relation between the two carrier-unit torsors.

### 5.3 Fresh attack - hidden cross-sector conversion unit

The finite Gate-4 pairing is canonical:

```text
beta_G([x])(c)=c^T x.                              (Y4-1)
```

Let `[c]=U_K` and `[x]=U_C`. Because `(Y4-1)` is a scalar evaluation,
dimensional consistency has only two lawful forms:

```text
(A) beta is dimensionless:
    U_C U_K = 1, hence U_C=U_K^*;

(B) beta carries a conversion torsor U_beta:
    U_beta U_C U_K = 1.                            (Y4-2)
```

V004 states neither horn. Horn (A) is exactly the missing dual-unit relation.
Horn (B) introduces an independent cross-sector conversion unit. That is a
fifth authored field or hidden scale not present in the four-item choice
table, and it conflicts with the claim that the C metric is simply the dual
of the K metric with no independently tunable sector weight.

The Riesz powers do not settle `(Y4-2)`: they type maps inside each carrier,
not the canonical pairing between the carriers. Merely naming `U_C` and
`U_K` also does not realize either physical carrier as a unit-valued Hilbert
space. The orthogonal-torsor classes in `(Y3-1)` are the missing no-frame
certificate.

```text
FRESH_ATTACK = succeeds
HIDDEN_CONVERSION_UNIT_EXCLUDED = not proved
CARRIER_UNIT_ISOMORPHISMS = TYPE-U in V004
Y4 = KILL
```

### 5.4 Bounded repair surface

A repair need not alter any metric theorem or add a response-facing choice.
Inside the existing fourth authored row it must:

```text
1. state whether the canonical beta pairing forces U_C:=U_K^*;
2. install [U_Kmap] and [U_Cmap] as orthogonal-torsor classes, not members;
3. prove restriction and admitted-automorphism covariance of those classes;
4. rerun the unit/R4 seam and hidden-scale regression;
5. add these changes to both delta tables.
```

If the package instead permits a nontrivial `U_beta`, that object must be
disclosed as an additional authored field with alternatives and a void
condition. It cannot remain implicit.

## 6. Final determination

V004 successfully repairs every concrete finite metric, Riesz, quotient,
and pendant/tree omission ordered by the V003 review. It also retains the
fullness theorem and W3 cleanup without reopening a null branch.

The package is not yet ratification-ready. Its claim that the original
Section 4.2 gap list is fully supplied is false as written: the carrier-unit
isomorphisms remain absent, and the double delta does not disclose that
loss. The missing interface is bounded to the existing carrier-units/R4
choice row.

```text
Y1 = PASS
Y2 = PASS
Y3 = KILL
Y4 = KILL

METRIC_PACKAGE = NOT_READY (Y3, Y4)
READY_FOR_DOR019_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
