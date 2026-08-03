# STAGE8 TASK 4B - CARRIER METRIC CROSS-REVIEW - LANE 1 V001

```text
ARTIFACT = STAGE8_TASK4B_CARRIER_METRIC_CROSS_REVIEW_LANE1_V001.md
LANE = CODEX LANE 1
TASK = PASTE 456 | adversarial cross-review of the carrier metric and units proposal
DATE = 2026-08-03
STATUS = COMPLETE | REVIEW ONLY | NOTHING ADOPTED

LEAD_RESULT:
  METRIC_PACKAGE = NOT_READY
  KILLING_ITEM = R2
  CORE_DEFECT = V005 point-separation of T_phys is not injectivity of c -> u_c on all K_G
  CONSEQUENCE = proposed g_K can be degenerate; R_K need not be a Riesz isomorphism
  ADDITIONAL_KILLS = R1 | R4 | R6 | R7
  DP_STANDING = only carrier-side pieces of DP1 and DP7 become checkable; DP1-DP10 do not discharge

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Preflight and custody

The preflight passed before the proposal was read.

| Check | Result |
|---|---|
| register head | `Q-374` exactly |
| proposal SHA-256 | `657fa2bc5d0dcd81dbc3c6201bd5ec1ce9178ee7929b36d0b597ea7e00552386` - match |
| proposal sidecar | match |
| adjudication standard | `2e1b011069043c1cc03277178be061a8b7d1704d2146be97eb799965aef9c679` - match |
| divergence-provenance standard | `c39de7a0ef5a29e92ded5fc961b54dfe933171ea291b221c38bf0aa3a9c0dcf3` - match |
| DoR-015 / V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` - match |
| square V004 | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` - match |
| DoR-017 decision | `ee9d81bf78ab0ac9361cad5b48dde2b6b8b1e9fb0e28a4fdbba41e1c43db3e45` - match |

Custody is adversarial review. This artifact adopts nothing and does not modify any
register, plan, tracker, decision, or proposal.

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| R1 - derivation check | **KILL** | the full positive package is not forced, but the proposal misses the finite forced pullback semiform `s_G(c,d)=g_A4(u_c,u_d)` and therefore misstates what DoR-019 would author |
| R2 - gap list one-to-one | **KILL** | `I_K` injectivity and the completed `I_C:C_prop -> K_cycle^*` identification are asserted, not proved; an admitted finite countermodel makes `g_K` degenerate |
| R3 - provenance | **PASS** | the displayed definitions do not inspect a Hessian, Schur block, response support, `p`, or a desired output; no rank, cycle basis, or numerical scale is selected |
| R4 - compatibility theorems | **KILL** | automorphism and rank-preserving isometry of the retained A4 form are premises restated as proofs; V005 supplies covariance/separation, not A4 isometry |
| R5 - DP executability | **PASS** | the proposal honestly leaves the divergence-to-carrier door open; at most metric/unit portions of DP1 and DP7 become executable |
| R6 - choice table | **KILL** | the table omits the live `K_G/ker(I_K,G)` alternative and the missing fullness/carrier-identification certificate; its minimality claim is therefore incomplete |
| R7 - fresh attack | **KILL** | the Riesz-map unit law has the dual power reversed: a map `A -> A*` carries `U_A^-2`, not `U_A^2`, under the proposal's own derivative units |

## 2. R1 - derivation check

### 2.1 What is not forced

The proposal is correct on the main negative result. None of the following forces a
positive Hilbert metric on both completed R5 carriers:

1. The A4 source norm lives on `J_phys^005`, not directly on `C_prop` or `K_cycle`.
2. The DoR-009 trace pairing is on the finite record operator carrier and lacks a
   record-to-R5 isometric intertwiner.
3. `G^007(f,h)=-hbar^2 q(1-q)L(f)L(h)` is rank one and is not a positive
   nondegenerate carrier metric.
4. R5's topology, complement inverse, and covariance cube do not determine an inner
   product.
5. Gate-4 duality fixes an algebraic pairing, not a norm or its scale.

Thus the statement

```text
FULL_POSITIVE_COMPLETED_CARRIER_METRIC_FORCED = false
```

is confirmed.

### 2.2 The partially forced form the proposal omits

V005 nevertheless supplies both inputs of a finite pullback form:

```text
I_K,G(c)=u_c,
g_A4 on J_fin,G^005 subset J_phys^005.
```

Therefore every finite stage already carries the forced positive-semidefinite form

```text
s_G(c,d):=g_A4(I_K,G c,I_K,G d)
         =g_A4(u_c,u_d).                          (R1-1)
```

Its kernel is determined, not authored:

```text
ker(s_G)=ker(I_K,G).                              (R1-2)
```

The proposal instead treats the completed isometric identification and the metric as
one authored field. That is too coarse. The lawful authorship question begins after
`(R1-1)`: prove `ker(I_K,G)=0`, quotient it, or add new physical directions. Those are
different DoR-019 choices with different carriers.

```text
FINITE_A4_PULLBACK_SEMIFORM_FORCED = true | premise: DoR-015
FINITE_A4_PULLBACK_POSITIVE_DEFINITE = not proved
R1_VERDICT = KILL | partial forcing omitted from the ruling content
```

## 3. R2 - the one-to-one gap audit

### 3.1 The load-bearing inference is invalid

V005 proves point-separation of the physical tangent:

```text
T_phys,G = image(L_G)/(image(L_G) intersection image(B_G))
           subset coker(B_G),

[L_G a] != 0  implies  some c in ker(B_G^T) has c^T L_G a != 0.
```

This says the family `{u_c}` separates points of `T_phys,G`. It does not say that the
map from coefficient labels to functionals is injective:

```text
c != 0  does not imply  u_c != 0 on T_phys,G.     (R2-1)
```

Injectivity would follow from the additional fullness theorem

```text
image(L_G)+image(B_G)=E_G,
equivalently T_phys,G=coker(B_G),                 (R2-2)
```

but neither V005 nor the proposal proves `(R2-2)`.

### 3.2 Explicit finite countermodel

Take the finite Gate-4 dual pair

```text
Q_G^lin = R^2,
K_G     = R^2,
beta(q,c)=q^T c,
T_phys,G=span{e_1} subset Q_G^lin.
```

Define the V005 current on the admitted tangent by

```text
u_(c_1,c_2)(t e_1)=c_1 t.
```

The complete current family separates `T_phys,G`: if every `u_c(t e_1)` vanishes,
choose `c=e_1` and obtain `t=0`. Thus the exact V005 separation theorem passes.

But

```text
u_e2=0,
ker(I_K,G)=span{e_2} != {0}.                     (R2-3)
```

With the standard retained source norm on the one-dimensional functional image,
the proposal's pullback is

```text
g_K(c,d)=c_1 d_1,
matrix(g_K)=diag(1,0).                            (R2-4)
```

So `g_K` is semidefinite, `R_K` has nonzero kernel, and no bounded Riesz isomorphism
`K_cycle -> K_cycle^*` follows. This countermodel uses no response data and satisfies
the cited V005 point-separation statement.

### 3.3 Consequences for every requested field

| Required field | Proposal status after `(R2-3)` |
|---|---|
| `g_K`, `||.||_K` | formula supplied, positivity not proved |
| `R_K` | formula supplied, bijectivity refuted in the countermodel |
| `I_C:C_prop -> K_cycle^*` | finite full-quotient duality exists, but the identification of R5 `C_prop` with that completion is not proved |
| `g_C`, `||.||_C`, `R_C` | conditional on the unproved completed `I_C` and nondegenerate `g_K` |
| carrier-unit isomorphisms | torsor notation supplied, but it cannot repair a degenerate carrier form |
| orthogonal transport | conditional on forms that have not been installed consistently |
| quotient norm | correct on finite `Q_G^lin` once a positive `g_K` is available; not yet a completed R5 norm |
| automorphism isometry | additional authored premise, not a theorem of the retained norm |

The exact repair boundary is one of:

```text
FULLNESS_CERT:
  image(L_G)+image(B_G)=E_G at every admitted finite stage,
  plus a natural completed fullness/isometry theorem;

or

VISIBLE_CURRENT_QUOTIENT:
  K_G^vis=K_G/ker(I_K,G),
  with a newly audited dual carrier and no claim that it equals all of K_G.
```

Neither is in V001. R2 is therefore a kill under the commission's rule that a merely
asserted item does not fill the gap.

## 4. R3 - provenance and hidden-scale attacks

The construction does not use response support. Its displayed metric data depend on
the retained source form, the Gate-4 pairing, and the new carrier identifications.
No CC/CK block, Schur term, stationary root, retarded result, `p`, or desired output
appears in the definitions.

The proposed unit torsors also do not select a numerical element, rank, ratio, cycle
basis, orientation member, or realization member. `nu` remains symbolic. The source
norm may carry an authored scale, but V001 does not equate that scale to `nu` or infer a
numerical action calibration from it.

```text
RESPONSE_SUPPORT_TUNING_FOUND = false
HIDDEN_NU_FIXING_FOUND = false
R3_VERDICT = PASS
```

This pass does not cure R2: clean provenance can still lead to an undefined or
degenerate metric.

## 5. R4 - compatibility theorems

### 5.1 Automorphism isometry is assumed

The proposal derives

```text
g_K(S k,S l)=g_K(k,l)
```

from covariance of `c -> u_c` and says the retained A4 form is transported with the
family. The needed middle premise is actually

```text
g_A4(alpha_J u,alpha_J v)=g_A4(u,v).             (R4-1)
```

V005 ratifies a retained A4 norm and the covariance/separation of the current family;
it does not prove `(R4-1)`. Indeed V005 expressly leaves the norm unforced by Gate 4.

For a rank-two current image, a positive retained form with matrix

```text
G_A4=diag(1,2)
```

still supplies a Hilbert norm and separation. Under the edge exchange

```text
P=[[0,1],[1,0]],
P^T G_A4 P=diag(2,1) != G_A4.                    (R4-2)
```

Thus covariance of the labels does not imply isometry of the retained norm. V001 may
author an invariant replacement or an invariantization rule, but it cannot call H4-2
a pullback theorem without doing so. Its displayed S8-A calculation uses the desired
equality as its own middle step.

### 5.2 Restriction and cycle creation

The cycle-creating accounting is honest in one important respect: it preserves the Z7
impossibility of a physical upward quotient map and keeps only the old cycle injection
plus a proposed orthogonal complement. That scope passes.

The stronger rank-preserving claim still requires the retained source inclusions to be
isometric in `g_A4`. V005 gives a directed Hilbert completion and commuting coefficient
maps, but V001 does not exhibit the claimed isometric finite-stage equation for the
retained form. It places `RestrictIso` in the authored package and then cites that
requirement as proof.

### 5.3 `rho_Gamma,N` and `rho_H,N`

The derivative and Hessian cubes from square V004 remain valid on the R5-generated
class. Their reinterpretation as Riesz-equivariant or isometric cubes is conditional on
valid `R_C`, `R_K`, and isometric carrier actions. Because R2 and `(R4-1)` are open,
that stronger propagation is not established.

```text
Z7_CYCLE_CREATION_BOUNDARY_RETAINED = true
R5_DERIVATIVE_CUBES_RETAINED = true
METRIC_ISOMETRY_UPGRADE_PROVED = false
R4_VERDICT = KILL
```

## 6. R5 - DP1 through DP10 executability

The metric proposal does not discharge the divergence-provenance certificate, and it
does not claim to. Assuming a repaired metric package, the exact effect is:

| DP item | Effect of metric package |
|---|---|
| DP1 datum | **partly checkable**: carrier topology and carrier/action unit typing; explicit `Div_G`, `delta_G`, and datum action remain absent |
| DP2 log relation | **open**: no logarithmic coefficient-to-datum equality is added |
| DP3 Depth | **open** |
| DP4 Accum | **open** |
| DP5 existing-map handoff | **open** |
| DP6 executable Gen | **open** |
| DP7 naturality | **partly checkable**: metric/isometry compatibility can be tested after R2/R4 repair; generator naturality remains open |
| DP8 finite square | **open**: no generated finite bottom leg |
| DP9 residual disclosure | **open for any future profile** |
| DP10 target and origin | **unchanged**: still required of a future generator |

```text
DP1_DP10_EXECUTABLE_FROM_METRIC_ALONE = false
NEWLY_CHECKABLE = DP1 carrier units/topology | DP7 metric covariance, conditionally
DIVERGENCE_PROVENANCE_STANDING = TYPE-U
R5_VERDICT = PASS | boundary stated honestly
```

## 7. R6 - choice table audit

The table includes genuine alternatives for independent metrics, algebraic versus
Riesz duality, unit normalizations, automorphism covariance, and cycle creation. Its
void conditions are generally testable.

It is not complete at the load-bearing carrier seam. It omits:

1. `K_G/ker(I_K,G)` with the forced semiform descended to the visible-current quotient;
2. the fullness certificate `(R2-2)` as a separate proposed/required field;
3. a `C_prop` that is not the Hilbert dual of all `K_cycle`, which remains possible
   because R5 only names `Y=C_prop direct-sum K_cycle`;
4. invariantization or replacement of a retained A4 form that fails `(R4-1)`;
5. the correct unit typing for the Riesz maps.

Consequently the claim that the proposal is the minimal dual-Hilbert extension of
ratified data is not yet failure-capable: the table has not exposed the decision that
makes the pullback positive and the two R5 carriers dual.

```text
CHOICE_TABLE_COMPLETE = false
R6_VERDICT = KILL
```

## 8. R7 - fresh attack: dual-unit consistency

This attack is independent of the faithfulness defect.

V001 declares

```text
[D_A phi]=U_action/U_A,
R_A:A -> A*,
[R_A]=U_A^2.                                     (R7-1)
```

If an `A` vector carries unit `U_A`, a scalar-valued covector in `A*` carries unit
`U_A^-1`. Therefore a linear map from `A` to `A*` carries

```text
[R_A]=[A*]/[A]=U_A^-1/U_A=U_A^-2.                (R7-2)
```

Equivalently, the inverse Riesz map carries `U_A^2`, which is the factor needed to
turn a covector coefficient into a vector coefficient. V001 assigns that power to the
forward map instead.

Using `(R7-1)` literally, `R_A^-1 D_A phi` has unit

```text
U_A^-2 * U_action/U_A = U_action/U_A^3,
```

not the unit of an `A` vector. If V001 intended a unit-valued bilinear form rather than
a scalar-valued Riesz map, then its declared codomain must be changed from `A*` to a
twisted dual and the derivative equations retyped. Neither reading makes `(R7-1)`
correct as written.

```text
R7_FRESH_ATTACK = succeeds
R7_VERDICT = KILL
```

## 9. Final determination

The proposal has a sound high-level instinct: use the retained source-current form and
Gate-4 duality, keep `nu` symbolic, and expose every completion. It is not ready for
ratification because its central positive-metric theorem assumes the very carrier
faithfulness it must establish.

The bounded repair target is:

```text
1. decide/prove FULLNESS_CERT or adopt VISIBLE_CURRENT_QUOTIENT;
2. instantiate the completed C_prop/K_cycle duality on that repaired carrier;
3. prove or explicitly author A4 automorphism and rank-preserving isometry;
4. correct the Riesz-map unit law and rerun the cubes;
5. update the choice table and DP ledger without changing the response-independent scope.
```

```text
METRIC_PACKAGE = NOT_READY (R2; also R1, R4, R6, R7)
READY_FOR_DOR019_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
