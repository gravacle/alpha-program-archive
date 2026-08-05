# STAGE8 TASK 5 — REVIEW OF THE XI_N DRAFT AND THE TWO MANDATED DISPLAYS

Lane: CODEX LANE 3 (SOL, HIGH EFFORT)  
Version: V001  
Date: 2026-08-05  
Custody: cross-family review of Dario's amendment draft  
Scope: symbolic determination only; no adoption, member binding, route selection, fixed-point execution, end test, or numerical evaluation

## 0. Preflight

[PROVABLE — access and no-clobber check] The cleanroom, archive workspace, and supervision roots
are readable. The requested output and its seal were absent in both the cleanroom and archive before
construction.

[PROVABLE — register check] The tail of
`QUESTIONS_SETTLED_REGISTER_V001.md` ends at `Q-506` before its usage instructions.

[PROVABLE — input check] The artifact was hash-verified before it was read, and its sealed sidecar
also verifies:

```text
STAGE8_TASK5_XI_N_CANDIDATE_DARIO_V001.md
lines   = 364
SHA-256 = 1b878d7a89fc2d48290dcdbd6494bb05c382124b74ae99d58a9e7f6f3e63409a
sidecar = OK
```

The gates remain

```text
alpha_computed = false;
proof_authorized = false;
kappa_record_computed = false.
```

## 1. Authority ledger and the reused-object audit

### 1.1 Verified authorities

| Key | Authority | SHA-256 |
|---|---|---|
| `DRAFT` | `STAGE8_TASK5_XI_N_CANDIDATE_DARIO_V001.md` | `1b878d7a89fc2d48290dcdbd6494bb05c382124b74ae99d58a9e7f6f3e63409a` |
| `A1` | `DOR_020_A1_WHERE_CLAUSES_AMENDMENT_2026-08-04.md` | `c4dc5976d7e65fe8a6597870629e64cabe6a031b95de97f5572bb36379abb588` |
| `WHERE` | `STAGE8_TASK5_EQ6_WHERE_CLAUSES_LANE2_V005.md` | `19b2060392b6e04448c1c13416b87b67decf401246e3414a783b288fdb5d80ec` |
| `WHERE-CHECK` | `STAGE8_TASK5_EQ6_WHERE_CLAUSES_FINAL_CHECK_LANE1_V001.md` | `b4c901f512379251b55d31aae6914d1fce9af6280c8f65081afeabfd4e75f219` |
| `FIELD` | `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md` | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` |
| `DOR015` | decision ratifying `FIELD` | `617bd51a70860d2cfb2066640630ba37ec289d56255ebbe1433bc0dfcba0159d` |
| `METRIC` | `STAGE8_TASK4B_CARRIER_METRIC_AND_UNITS_PROPOSAL_LANE2_V005.md` | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` |
| `DOR019` | `DOR_019_CARRIER_METRIC_AND_UNITS_RATIFICATION_2026-08-03.md` | `6ab72b0cb3a93e123eb1d3c5088fc83361d86c6dc739f0a886380dbd2d143f1f` |
| `LOC` | `STAGE8_TASK5_EQ6_THE_LOC_BUILD_LANE3_V001.md` | `b53d9e931efe1ebde333ef49fb4243e41917bb5d467f5a86e7052102ae5a0310` |
| `KER` | `STAGE8_TASK5_R4_KERNEL_REALIZATION_AND_SYMBOL_CALCULUS_LANE2_V001.md` | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` |
| `GAMMA-H` | `STAGE8_TASK5_GAMMA_H_ROUTE_LANE3_V001.md` | `f2317e41367dc906ffa23f6055f2ed96a0f59f74b4e412966809d292c23e5402` |
| `AUDIT` | `STAGE8_TASK5_CHAIN_CONFORMANCE_AUDIT_LANE3_V002.md` | `44202c060821728fba2c46b81b82487002e639f3242565b7a5fed387e41fcae8` |
| `A7` | `DOR_020_A7_EC_BRANCH_CARRIED_2026-08-05.md` | `834e46029a292122c1e4c604af4f3e3249e6a9ee2638255464685623fba5eb8f` |
| `A8` | `DOR_020_A8_GAMMA_BOTH_ROUTES_2026-08-05.md` | `0ee6c897055f803b31bc570b9f4ef852ccb3c4aba21fcd5274a7d740c8eb601d` |

### 1.2 The cycle carrier and the period functional

[PROVABLE] To avoid a collision with `FIELD`'s separate quotient map named `K_N`, write

```text
K_N^(cyc,R)
 :=ker(B_N^T:R^(E_N)->R^(V_N)),                 (R1)

Lambda_N^cyc
 :=ker(B_N^T) intersection Z^(E_N).             (R2)
```

`METRIC` defines the real carrier `(R1)` and `DOR019` ratifies it. For
`z in K_N^(cyc,R)`, the ratified infinitesimal current is

```text
u_z:T_A Conn(P_N)->R,

u_z(a)
 :=<z,L_N a>
 =sum_(e in E_N) z_e integral_(gamma_e) a.       (R3)
```

Thus the draft is right that the real cycle carrier and the tangent functional already exist. It is
not right to merge their two roles:

```text
z in Lambda_N^cyc
 ->bounded gauge-invariant U(1) character;

z in K_N^(cyc,R)
 ->real Lie-algebra cotangent/current functional. (R4)
```

`FIELD` states this separation explicitly: the integer kernel supplies the bounded `U(1)`
characters, while its real span supplies the full Lie-algebra cotangent. That distinction is the
decisive issue in Display I.

### 1.3 What A1 actually adopts

[PROVABLE] A1 adopts a possibly empty membership law, not one selected connection. For an arbitrary
alleged field member

```text
E_R=(e_M,mu_M,A_M,F_M,tilde_f_R,iota_R)
    in FieldExt_adm(R),                          (R5)
```

the conditional connection transport is genuinely adopted and typed:

```text
eta_conn,R(A_M)
 :=tilde_f_R^*A_M
 =iota_R^*(f_R^*A_M),

A_N=eta_conn,R(A_M) on the old image.            (R6)
```

Every compatible member remains in the family, and the family may be empty. Therefore all formulas
below are universal statements about an arbitrary alleged member. No `A_N` is bound or selected.

### 1.4 Objects the draft calls reused but stock does not inhabit

[PROVABLE] The following are specifications, not sealed inhabitants:

```text
D_N^Loc:=Krawhat_N(E_N),
Ker_(a,K):O_a^resp->D_N^Loc,
etahat_f:D_N^Loc->D_M^Loc.                      (R7)
```

`LOC` makes `D_N^Loc` conditional on a common kernel carrier, `Sch_N`, `Krawhat_N`, and
`Rel_N subset ker(Krawhat_N)`. `GAMMA-H` confirms that none of these source-extension/descent data,
the response bridge `Ker_(a,K)`, or the physical D-side transport compatibility is inhabited.

The support types also differ before a bridge is supplied:

```text
support of a Q-408 bilocal kernel lies in M_N x M_N;
support of a cycle current lies in the record path/surface carrier M_N. (R8)
```

No sealed projection or incidence map compares the two supports in the form used by `(X3)`.

### 1.5 The “one new map” claim

[YOURS — review verdict] Syntactically, the nine clauses declare one map symbol, `Xi_N`. As a claim
about a complete route assembled from stock, “exactly one new map” is false. The draft additionally
consumes:

```text
an inhabited D_N^Loc with topology, units, support, and transports;
Ker_(a,K):O_a^resp->D_N^Loc;
a real-cycle extension/lift of geometric U(1) holonomy;
a typed cross-support comparison.               (R9)
```

The first two are already-named common debts, but they are not sealed resources. The third does not
exist in the cited ingredients. Consequently the amendment may still be designed around one new
correspondence, but this draft has not demonstrated the advertised one-new-map closure.

## 2. N1 — audit of all nine clauses

| Clause | Verdict | Audit against adopted stock |
|---|---|---|
| `(X1)` type/linearity | **DEFECTIVE PREMISE** | `K_N^(cyc,R)` is ratified, but `D_N^Loc`, its quotient topology, units, and actions are uninhabited. If the codomain is repaired to the integral lattice needed by geometric holonomy, R-linearity is not typeable on that non-vector-space lattice; a continuous additive replacement is necessarily zero. |
| `(X2)` derived composite | **DEFECTIVE** | `Hol_(A_N)(z)=exp(iu_z(A_N))` is ill-typed on an affine connection and wrong on the full real carrier; `Ker_(a,K)` is also unbuilt. The corrected relative integral-cycle display is in section 4. |
| `(X3)` support | **UNFORMED** | Kernel support and cycle support live on different carriers in `(R8)`; no comparison map or support projection is displayed. Therefore the purported anti-counterterm test cannot yet be run. |
| `(X4)` covariance/no selection | **PART-PROVABLE** | Retaining the full family is conformal with A1. The equation must separately type `u_D:D_N^Loc->D_N^Loc` and `u_K:K_N^(cyc,R)->K_N^(cyc,R)`; the D-side action is not sealed. |
| `(X5)` units | **DEFECTIVE / UNDERSPECIFIED** | `U_K` is ratified, but no inhabited D-side unit class is available, and unit compatibility neither supplies the real-to-integral holonomy passage nor fixes a dimensionless scale. |
| `(X6)` restriction/naturality | **DEFECTIVE** | `j_f^K` is ratified on W3 rank-preserving scope and A1's connection pullback is conditionally derived. The draft's “sealed D-side transport” is not sealed, and the cycle-creating downward old-image equation is not written. |
| `(X7)` reader/consequence freedom | **CONFIRMED AS A CANDIDATE CONDITION** | It is reader-, threshold-, fixed-point-, and end-test-free and conflicts with no adopted stock. It does not establish inhabitance. |
| `(X8)` address | **UNFORMED** | Neither the addressed D-side datum nor the required equality is named. The raw addressed response and factor basis live in `O_a^resp`, while `Xi_N` consumes `D_N^Loc`; the missing `Ker_(a,K)` bridge is load-bearing. |
| `(X9)` A7 repayment | **ILL-TYPED / PARTIAL** | It applies `Xi_N` to response-side objects without precomposing `Ker_(a,K)`, inherits the real/integer defect, and supplies only raw holonomy neutrality—not the arc/log/unit conjuncts of `(HOL2)`. Section 6 gives the corrected conditional form. |

[YOURS] The clause ledger is not confirmable. The decisive incompatibility is already internal to
`(X1)`–`(X2)`:

```text
geometric bounded holonomy needs Lambda_N^cyc;
X1 demands an R-linear continuous map into K_N^(cyc,R);
Lambda_N^cyc is not an R-vector space, so X1 cannot simply be
retyped with that codomain.                              (C1)
```

Two lawful repairs both expose the obstruction. First, if linearity is weakened to a continuous
additive-group homomorphism

```text
Xi_N:(D_N^Loc,+)->(Lambda_N^cyc,+),             (C2)
```

then the connected additive group `D_N^Loc` has connected image in the discrete lattice. The image
is one point; a homomorphism sends zero to zero, so the image is `{0}`.

Second, retain the draft's typed map

```text
Xi_N:D_N^Loc->K_N^(cyc,R)
```

but add the geometric-holonomy requirement `im(Xi_N) subset Lambda_N^cyc`. For every `x`,

```text
{Xi_N(t x):t in R}
 ={t Xi_N(x):t in R}
 subset Lambda_N^cyc.                           (C3)
```

The left side is connected and contains zero; the right side is discrete. Hence the line in `(C3)`
is `{0}` and `Xi_N(x)=0`. A nonzero primitive-cycle assignment therefore requires a different
type—such as a nonlinear map to actual integral cycles—or additional lift/reference structure.

## 3. Audit of the eight void conditions

| Void | Verdict | Failure-capability audit |
|---|---|---|
| `V1` dependency | **FAILURE-CAPABLE** | A dependency trace reaching a reader, response consequence, threshold, fixed point, or end test exhibits failure. |
| `V2` curvature relabeling | **FAILURE-CAPABLE** | A definition path through curvature or `c_1` rather than connection transport exhibits failure; A1's flat-holonomy attack is the permanent regression. |
| `V3` hidden counterterm/support | **UNFORMED** | Until `(R8)` is bridged, `supp(Xi_N(x)) subset supp(x)` is not a typed predicate, so no alleged datum can pass or fail it. |
| `V4` discipline omnibus | **PARTIAL** | Reality/no-upward-lift tests are meaningful; its support, unit, and D-side covariance arms inherit the untyped objects above. |
| `V5` selection | **FAILURE-CAPABLE** | A consumer that binds a candidate or gauge/connection representative supplies an explicit text-level witness. |
| `V6` A8 identification | **CONDITIONALLY FAILURE-CAPABLE** | A displayed disagreement is a first-order failure, but A8 voids the disagreeing construction(s) pending adjudication. It does not identify `Xi_N` as the culprit without a separate fault isolation. |
| `V7` identity branch | **NOT WELL-FORMED AS WRITTEN** | The response/D-side domain error and real/integer character error prevent its proposed witness from being typed. The direct `Hol != 1` repair is in section 6. |
| `V8` empty family | **STOP CONDITION, NOT SINGLE-DATUM VOID** | Emptiness is a global nonexistence result. A1 treats the empty torsor as allowed but non-witnessing; it belongs on the inhabitance/stopping board rather than among directly exhibited member falsifiers. |

[YOURS] The eight-item list is not a complete failure-capable gate: `V3` and `V7` are unformed,
`V4` is partial, and `V8` is misclassified. This is independent of the Display-I defect.

## 4. N2 — Display I: the maximal lawful holonomy identification

### 4.1 Exact types

Fix no member. Let `(R5)` be an arbitrary alleged A1 member and take two connections on the same
admitted bundle,

```text
A_0,A_1 in Conn(P_N),
a:=A_1-A_0 in T_(A_0)Conn(P_N),
A_t:=A_0+t a.                                   (D1-1)
```

Let `z in Lambda_N^cyc`. The integral restriction is essential. The ratified edge differential is
read with the same admitted endpoint framing on `A_0,A_1` and with the frame tangent held fixed:

```text
-i h_e(A_t)^(-1) d/dt h_e(A_t)
 =(L_N a)_e
 =integral_(gamma_e) a.                         (D1-2)
```

Because `U(1)` is abelian, integrating `(D1-2)` gives

```text
h_e(A_1)h_e(A_0)^(-1)
 =exp(i (L_N a)_e).                             (D1-3)
```

### 4.2 Integral-cycle product and relative formula

Define the geometric character on the integral cycle lattice by

```text
Hol_A(z):=product_(e in E_N) h_e(A)^(z_e).       (D1-4)
```

Every equality identifying the sealed relative period is

```text
Hol_(A_1)(z) Hol_(A_0)(z)^(-1)
 =product_e h_e(A_1)^(z_e)
    product_e h_e(A_0)^(-z_e)
 =product_e (h_e(A_1)h_e(A_0)^(-1))^(z_e)
 =product_e exp(i z_e (L_N a)_e)
 =exp(i sum_e z_e (L_N a)_e)
 =exp(i sum_e z_e integral_(gamma_e) a)
 =exp(i u_z(a))
 =exp(i u_z(A_1-A_0)).                          (D1-5)
```

This is the exponential form of `FIELD`'s sealed local phase formula

```text
Phi_z([A,p];[A_0,p_0])
 :=-i Log_0 product_e
      (h_e(A,p)h_e(A_0,p_0)^(-1))^(z_e),

d Phi_z=u_z.                                    (D1-6)
```

An integral circulation decomposes as an integer sum of oriented closed graph cycles. Formula
`(D1-4)` is independent of a chosen decomposition because it is indexed by the coefficient vector
itself; no cycle basis is selected.

### 4.3 Gauge invariance displayed

For a vertex gauge function `g`, edge transport changes by

```text
h_e(A^g)=g_(t(e)) h_e(A) g_(s(e))^(-1).         (D1-7)
```

Then

```text
Hol_(A^g)(z)
 =product_e (g_(t(e))h_e(A)g_(s(e))^(-1))^(z_e)
 =product_e h_e(A)^(z_e)
    product_v g_v^((B_N^T z)_v)
 =Hol_A(z) product_v g_v^0
 =Hol_A(z).                                     (D1-8)
```

Integer powers and `B_N^Tz=0` are both used. For a nonintegral real vector, the expressions
`h_e^(z_e)` require logarithm branches; a large-gauge shift produces

```text
exp(i 2 pi <z,n>),                              (D1-9)
```

which is not identically one for arbitrary real `z`.

### 4.4 Adopted transport displayed

Let `R:G->G'` be an arbitrary admitted A1 relation. The path/current law and connection pullback give

```text
f_R gamma_(G,e)
 =the ordered child chain encoded by s_R,

S_R=s_R|_(ker(B_G^T)),

A_G=eta_conn,R(A_G')=tilde_f_R^*A_G'.           (D1-10)
```

For a tangent `a'` at `A_G'`, every current equality is

```text
u_z(D eta_conn,R(a'))
 =sum_e z_e integral_(gamma_(G,e)) f_R^*a'
 =sum_e z_e integral_(f_R gamma_(G,e)) a'
 =sum_(e') (S_R z)_(e') integral_(gamma_(G',e')) a'
 =u_(S_R z)(a').                                (D1-11)
```

Exponentiating the integral-cycle relation gives

```text
Hol_(eta_conn,R(A_G'))(z)
 =Hol_(A_G')(S_R z),                            (D1-12)

Hol_(eta_conn,R(A_1'))(z)
 Hol_(eta_conn,R(A_0'))(z)^(-1)
 =Hol_(A_1')(S_Rz) Hol_(A_0')(S_Rz)^(-1).       (D1-13)
```

A1's bundle-isomorphism associator gives

```text
eta_conn,(S compose R)
 =eta_conn,R compose eta_conn,S,

S_(S compose R)=S_S compose S_R.                (D1-14)
```

Hence composition is displayed:

```text
Hol_(eta_conn,(S compose R)(A_G''))(z)
 =Hol_(eta_conn,R(eta_conn,S(A_G'')))(z)
 =Hol_(eta_conn,S(A_G''))(S_R z)
 =Hol_(A_G'')(S_S S_R z)
 =Hol_(A_G'')(S_(S compose R)z).                (D1-15)
```

On an A1 common-refinement diamond, the two composite cycle maps agree and the two bundle
isomorphisms agree up to admitted gauge. Applying `(D1-8)` to that gauge yields equality of the two
holonomies. The scope is the admitted old-image transport; no upward lift of a newly created target
cycle is introduced.

### 4.5 Why the draft's absolute display does not follow

[PROVABLE] The draft asks for

```text
Hol_(A_N)(z)=exp(i u_z(A_N))
 for every z in K_N^(cyc,R).                    (D1-16)
```

The exact failures are:

1. `Conn(P_N)` is affine and `(R3)` consumes a tangent. `u_z(A_N)` is not typed.
2. `(D1-5)` is relative. An absolute formula requires a reference `A_0` with
   `Hol_(A_0)(z)=1` and an identification of `A_N` with `A_N-A_0`; A1 selects neither a reference nor
   a global trivialization and admits nontrivial bundles.
3. The bounded character `(D1-4)` is sealed on `Lambda_N^cyc`, not on the full real carrier.
4. A1 is law-only and may be empty, so the display is conditional on an alleged member, never an
   inhabited singular `A_N`.

[YOURS — determination] The requested absolute identification has an exact gap. The relative
integral-cycle formula `(D1-5)` and its naturality are the strongest result derived from sealed stock.

## 5. N3 — Display II: single-cycle minimality

Let `x` be a future formed D-side element and define the typed supported cycle subspace

```text
S_x:=the record-visible surface support assigned to x,

K_N(S_x)
 :={z in K_N^(cyc,R):supp(z) subset S_x}.        (D2-1)
```

Neither `S_x` nor the comparison in `(D2-1)` is presently sealed. Grant them temporarily and grant
the stronger rank-one theorem the draft needs:

```text
K_N(S_x)=R c_x,
c_x a fixed nonzero primitive orientation class. (D2-2)
```

Then `(X3)` gives the complete lawful reduction

```text
supp(Xi_N(x)) subset S_x
 =>Xi_N(x) in K_N(S_x)
 =>Xi_N(x) in R c_x
 =>there exists lambda_x in R such that
      Xi_N(x)=lambda_x c_x.                     (D2-3)
```

The unit clause gives only

```text
[Xi_N(x)]=U_K,
[c_x]=U_K
 =>[lambda_x]=1,                                (D2-4)
```

meaning that `lambda_x` is dimensionless. It does not give `lambda_x=1`, `lambda_x=-1`, or any
other value.

The surviving freedom is exhibited without selecting a member. On symbolic one-dimensional carriers

```text
D=R x,
K=R c,
Xi_a(t x):=a t c
 for arbitrary dimensionless nonzero a,         (D2-5)
```

each `Xi_a` is R-linear, continuous, support-preserving, unit-compatible, reader-free, and covariant
under the trivial admitted action. Distinct dimensionless `a` give distinct assignments with the same
unit class.

If `(X8)` intends to fix the addressed value, it must write the missing equality

```text
Xi_N(x_addr)=c_addr.                             (D2-6)
```

Then `(D2-6)`, not `(X5)`, supplies an authored normalization at that one address. It does not prove
the general single-cycle reduction claimed in the draft.

[YOURS — determination] Display II stops twice: the supported-rank-one theorem `(D2-2)` is absent,
and even granting it, units type but do not normalize the remaining scalar.

## 6. N4 — audit of the `(X9)` repayment

### 6.1 Correct subjects

For a future formed response bridge, the objects to which `Xi_N` may be applied are

```text
k_(a,K)
 :=Ker_(a,K)(Y_(a,1)^Hol(K)) in D_N^Loc,

khat_(a,K)
 :=Ker_(a,K)(Rhat_(Kcycle,a)) in D_N^Loc.        (X9-1)
```

The draft instead quantifies `x` over response-side objects and applies `Xi_N` directly; that is the
domain error. For a repaired geometric holonomy and a typed image `Xi_N(k) in Lambda_N^cyc`, the
exact neutrality statement is

```text
Xi_N(k) in ker(Hol_A)
 <=>Hol_A(Xi_N(k))=1_(U(1)).                    (X9-2)
```

On the additional relative/integral-cycle typing of section 4, `(D1-5)` gives only

```text
Hol_A(Xi_N(k))=1_(U(1))
 <=>exp(i u_(Xi_N(k))(A-A_0))
     =Hol_(A_0)(Xi_N(k))^(-1).                  (X9-3)
```

Only with the additional reference-neutrality hypothesis

```text
Hol_(A_0)(Xi_N(k))=1_(U(1))                     (X9-3a)
```

does `(X9-3)` reduce to

```text
Hol_A(Xi_N(k))=1_(U(1))
 <=>u_(Xi_N(k))(A-A_0) in 2 pi Z.               (X9-3b)
```

Thus even the repaired period criterion needs the lattice, reference, and reference-neutrality
restrictions displayed. The draft's unqualified `u_(Xi_N(x))(A_N) in 2 pi Z` is not licensed.

### 6.2 Single-element refutability

[PROVABLE — conditional] For one alleged, fully typed tuple `(A,Ker,Xi)`, either exhibit in `(X9-1)`

```text
Hol_A(Xi_N(k_(a,K))) !=1_(U(1)),
```

or exhibit

```text
Hol_A(Xi_N(khat_(a,K))) !=1_(U(1)).              (X9-4)
```

Either single element refutes `(X9)` for that candidate member. It does not prove the entire retained
`Xi` family empty; every remaining member must still be tested or excluded structurally.

### 6.3 What `(X9)` repays and what remains

[PART-PROVABLE] Corrected `(X9-2)` repays the two raw-neutrality equations in `(HOL2)`. It does not
supply the other conjuncts:

```text
1_(U(1)) in U_b,
log_b(1_(U(1)))=0,
U_(a,1)^Hol(0)=0,                               (X9-5)
```

nor does it inhabit `A`, `D_N^Loc`, `Ker`, or either A7-indexed `Xi` family. Only after
`(X9-2)` and `(X9-5)` are inhabited does the displayed audit chain give

```text
Theta_(a,K)^Hol(Y_(a,1)^Hol(K))=1
 =>log_b(Theta_(a,K)^Hol(Y_(a,1)^Hol(K)))=0
 =>B_(a,1)^(per,Hol)(K)=U_(a,1)^Hol(0)=0 for every K
 =>q_1^Hol=0.                                   (X9-6)

Theta_(a,K)^Hol(Rhat_(Kcycle,a))=1
 =>log_b(Theta_(a,K)^Hol(Rhat_(Kcycle,a)))=0
 =>chi_1^Hol
    :=U_(a,1)^Hol(
        log_b(Theta_(a,K)^Hol(Rhat_(Kcycle,a))))
     =U_(a,1)^Hol(0)
     =0.                                        (X9-7)
```

The zero branch remains unconstrained and retains its full conditional lattice. Thus `(X9)` does not
select an A7 branch, but actual two-sidedness is conditional on nonempty formed route families and
the remaining seam. The draft's unconditional `PROVABLE` two-sidedness language outruns its premises.

## 7. N5 — fresh attack: full response-line winding versus one logarithm arc

[YOURS — structural attack; no program value evaluated] Grant the draft's full-real character
extension, grant all missing maps, and additionally fix a reference satisfying `(X9-3a)` on the
factor image solely for this attack. Let

```text
L_a^resp:=R Rhat_(Kcycle,a),
p:=u_(Xi_N(Ker_(a,K)(Rhat_(Kcycle,a))))(A-A_0). (A1)
```

Linearity of `Ker` and `Xi` would give, for symbolic `t in R`,

```text
Theta_(a,K)^Hol(t Rhat_(Kcycle,a))
 =exp(i u_(Xi_N(Ker_(a,K)(t Rhat)))(A-A_0))
 =exp(i u_(t Xi_N(Ker_(a,K)(Rhat)))(A-A_0))
 =exp(i t p).                                    (A2)
```

Basis neutrality in `(X9)` supplies only

```text
exp(i p)=1
 <=>p in 2 pi Z.                                (A3)
```

If `p` is a nonzero lattice period, the map `t |-> exp(i t p)` winds through all of `U(1)`. In
particular, a symbolic `t` satisfying `t p=pi` maps to `-1`. Hence the full factor line cannot lie in
one proper response-independent arc `U_b` carrying a single-valued logarithm. If `p=0`, the whole
line maps to `1` and its scalarized coefficient is zero.

Therefore basis neutrality alone does not produce the global factor/log interface later relays
consume. A viable route must either:

```text
restrict the response domain to a certified logarithm chart;
strengthen the period condition from p in 2 pi Z to p=0 on the full line;
or replace the claimed global linear factorization.                (A4)
```

This attack is independent of the affine-domain defect in Display I. It confirms that `(X9)` is a
partial raw-neutrality clause, not the complete scalar-route repayment.

## 8. Consequence and repair board

| Item | Review result |
|---|---|
| ratified real cycle carrier | confirmed, renamed `K_N^(cyc,R)` to avoid collision |
| ratified `u_z` | confirmed as a tangent/current functional |
| A1 connection transport | confirmed conditionally for an arbitrary alleged member |
| singular adopted `A_N` | rejected; A1 is a possibly empty family law |
| `D_N^Loc`, `Ker`, D-side transport called sealed | rejected; all remain uninhabited specifications |
| one-new-map closure | not demonstrated |
| absolute real-cycle holonomy display | gap; only relative integral-cycle formula derived |
| single-cycle forced assignment | gap; support-rank theorem and normalization absent |
| X9 single-element test | valid only after `Ker` precomposition and geometric-holonomy repair |
| X9 two-sidedness | conditional; raw neutrality alone does not finish `(HOL2)` |
| eight-void gate | incomplete/failure-capability defects in `V3`, `V4`, `V7`, `V8` |

[YOURS] A revised draft must choose and display one coherent route:

1. map nonlinearly to actual integral cycles/loops and then use geometric A1 holonomy; or
2. retain the real carrier but add and gate a reference/logarithmic lift, acknowledging the extra
   authored structure.

It must also parameterize every claim over arbitrary alleged A1 members, stop calling `(R7)` sealed,
type the support comparison, write `(X8)` as an equality if normalization is intended, precompose
`(X9)` with `Ker`, and leave the arc/log/unit seam separate. These changes alter load-bearing clauses,
so the present draft is not ready for a principal's ruling.

```text
MACHINERY-APPEAL
 =integral-cycle/absolute-holonomy interface
  +DLoc/Ker/D-side transport inhabitance
  +kernel-to-cycle support comparison;

review continues because these are structural gaps, not value fences.
```

## 9. Battery and self verb audit

### 9.1 Anti-tuning and fence ledger

| Check | Result |
|---|---|
| No A1 connection member selected | clean; every display is universally conditional |
| No `Xi` member selected or bound | clean; counterfamilies are symbolic exhibits |
| No A7 branch selected | clean; both labels retained |
| No `2 pi Z` condition inferred from a desired coefficient | clean; it is audited as a draft clause |
| No real-cycle logarithm branch silently chosen | clean; its absence is the Display-I gap |
| No response, threshold, fixed point, end test, or measured constant consumed | clean |
| No number or magnitude evaluated | clean; the winding attack is structural and symbolic |
| No H/HOL equality assumed | clean; A8's falsifier remains conditional |

### 9.2 Verb audit

| Verb | Matched display |
|---|---|
| `verified` | hashes, line count, sidecar, roots, no-clobber, and register head were checked before review |
| `ratified/adopted` | reserved for `DOR015`, `DOR019`, A1 membership law, and A7/A8 decisions |
| `derived` | used for `(D1-5)` and `(D1-11)`–`(D1-13)`, with every equality and scope displayed |
| `confirmed` | restricted to the real carrier, tangent functional, and conditional A1 transport |
| `defective/unformed/gap` | each is followed by its exact type, inhabitance, support, or normalization witness |
| `refutes` | scoped to one alleged candidate member in `(X9-4)`, never the full family |
| `preserves` | two-sidedness is not asserted unconditionally; its remaining premises are displayed |
| `ready` | denied because revisions affect load-bearing clauses and the gate |

The self audit finds no verb stronger than the displays above.

XI_N_DRAFT = DEFECTIVE (+real-cycle/integer-holonomy mismatch; affine u_z(A_N) type error; unsealed DLoc/Ker/D-transport reused as stock; X3/X8 support-address gaps; X9 domain and repayment defects; void gate incomplete)
DISPLAY_I = GAP (+sealed result is Hol_A1(z) Hol_A0(z)^-1 = exp(i u_z(A1-A0)) for integral z; absolute reference and full-real-carrier extension are absent)
DISPLAY_II = GAP (+no sealed supported-rank-one theorem; units make the residual scalar dimensionless but do not normalize it)
READY_FOR_RULING = no
VERB_AUDIT_SELF = CLEAN
