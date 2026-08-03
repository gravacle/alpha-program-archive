# STAGE8 TASK 4B: N-MEMBER JET INSTANTIATION PROPOSAL — LANE 2 V001

Date: 2026-08-03  
Task: PASTE 452 / Task 4b / jet-race author arm  
Lane: CODEX LANE 2  
Register head at preflight: Q-369  
Reserved ruling: DoR-018  
Custody: authored proposal; cross-review and principal ruling required

**PROPOSED_NOT_ADOPTED — PENDING REVIEW AND PRINCIPAL RATIFICATION
(DoR-018 RESERVED)**

```text
LEAD_RESULT = RADIAL_FLAT_N_MEMBER_STATIONARY_GERM_PROPOSED

PROPOSAL_OBJECT = N_MEMBER_JET_INSTANTIATION_R001
LIVE_MEMBER = the already-ratified DoR-017 N member only
ADDITIONAL_MEMBER_SELECTED = false

PHI_m(c,k)
 =nu (1+(1/2)||c||_C^2) f(||k||_K^2),

f(s)=exp(-1/s) for s>0,
f(0)=0.

STATIONARY_FAMILY =
  y_star,m(p,nu;k)=(c_star,m(p,nu;k),k),
  c_star,m = the R5 local inverse branch of
    D_C Gamma_base(p;c,k)+nu f(||k||^2) R_C c=0.

FINITE_ACTIVE_MEMBER_JETS = 0 | all orders
N_MEMBER_NONZERO_OFF_SECTION = true | nu symbolic and nonzero
NU_DOMAIN = real_symbolic_nonzero | reality required
NU_HOMOGENEITY = manifest

P_VERDICT_COMPUTED = false
NUMERIC_RESPONSE_VALUE_COMPUTED = false
PROPOSAL_READY_FOR_CROSS_REVIEW = yes

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

This proposal authors a stationary **germ** of the already-ratified N member.
It does not choose another member, a rank, an orientation, a realization, or
a stationary point from the carried cycle family.  The profile is fixed
before the Schur expression is consulted and contains no response, p, alpha,
or target datum.

---

## 0. Preflight, register sweep, and authorities

### 0.1 Preflight

`LOCKED_PROCESS.md` was read in full.  The live questions-settled register
and local sidecar verified, and its head was Q-369.  Every named authority
was hash-verified before it was read.

| Authority | Verified SHA-256 | Use |
|---|---|---|
| square V004 | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | R1 tuple, R2/R5 restrictions, covariance cube |
| stationary response computation | `be570c182ef875b557395b62c382ee875420ac0462e2efb5774e9600f794b27a` | exact Schur consumer |
| stationary response cross-verification | `cac131d949a917576e30332b2f4ec76ca7db57d6d4683e91cfeac658994c499b` | confirmed jet boundary and tags |
| divergence/action draft | `ed49624b6f5f0bcda94ee88a939a5751113b30d73192b2c28a5aec25829e1797` | flat-family countermodels and missing generator |
| DoR-017 decision | `ee9d81bf78ab0ac9361cad5b48dde2b6b8b1e9fb0e28a4fdbba41e1c43db3e45` | ratified N member and falsifier discipline |
| DoR-016 law V004 | `69f4d93b9f84075a3112fb011b9838f380fb8c0341610572170cf7a13d5aed08` | doubled CTP batching and ordered towers |
| DoR-015 field signature V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | physical quotient and Hilbert source norms |

```text
DOES_THE_OBJECT_EXIST = no | the executable stationary germ is Q-369 TYPE-U
IS_THE_VERSION_CURRENT = yes | Q-369
ARE_ITS_INPUTS_PRESENT = yes | R1 interface, physical norms, R5 domain,
  response consumer, and full certificate battery
PREFLIGHT = PASS_FOR_AUTHORING
```

### 0.2 Register sweep

The following settled entries were checked before authoring:

```text
Q-243  exact zero and p-free finite ordered-retarded block;
Q-279  exact probe-on finite Hessian table;
Q-309  finite kernel/mixing zero;
Q-318  one-dimensional source-image theorem and physical-identification refusal;
Q-322/Q-324  all-orders-flat family and off-section freedom;
Q-326  flatness does not kill off-section mixing or stationary shifts;
Q-327  divergence-to-action bridge requirements;
Q-347-Q-357  all-rank quotient descent and consumer scope;
Q-358  quotient-only phi_div consumer and five square residues;
Q-361-Q-366  action-square repairs and completed Hessian cube;
Q-367  DoR-017 ratifies the N member with symbolic nu;
Q-368  stationary response operator expression;
Q-369  cross-verification and exact jet boundary.
```

The parallel derive arm was not read, searched, or anticipated.

### 0.3 Symbol and ownership distinctions

```text
nu              = symbolic N-member normalization, not a response value;
p               = symbolic base-state weight, not an input to the profile;
k in K_cycle    = carried cycle coordinate, not a selected cycle basis;
c in C_prop     = complement coordinate, not a Keldysh common source;
f(||k||^2)      = flat gate, not a fitted regulator;
y_star,m(k)     = full covariant stationary family, not one chosen point;
R_C             = Riesz map of the ratified complement norm, not probe R;
N member        != finite stage N.
```

---

## 1. E1 — the proposed executable object

### 1.1 Ratified carrier terms

Work in the R5 local physical chart

```text
Y_G=C_G direct-sum K_G,
S_G=C_G direct-sum {0},
D_017,G subset Y_G,
```

where `K_G` is the Gate-4 record-visible cycle tangent and `C_G` is the
propagating complement.  DoR-015 supplies the basis-free physical Hilbert
norms.  Here `||.||_C` and `||.||_K` mean their dimensionless coordinate
forms after the carrier-unit isomorphisms already required by R1/R4; those
unit maps are consumed, not re-chosen.  If either unit map is absent, J1
voids rather than inserting a width parameter.  No new scale is introduced.

Define the invariant scalars

```text
a_G(c):=1+(1/2)||c||_C^2,
s_G(k):=||k||_K^2.                                 (E1-1)
```

For an admitted signed realization arrow `alpha:G->G'`, the R5 transports
are isometric, hence

```text
a_(G')(alpha_C c)=a_G(c),
s_(G')(alpha_K k)=s_G(k).                          (E1-2)
```

### 1.2 Primitive datum, generation maps, and member

The authored primitive datum is weaker than the output action:

```text
delta_rad,G(y):=(a_G(c),s_G(k)),

delta_div,m^R001:=delta_rad,

Depth_G(y):=delta_rad,G(y),

Accum_(M|N):=(a_M,s_M)-(a_N compose rho_C,N,
                       s_N compose rho_K,N),

f(s):={exp(-1/s), s>0; 0, s=0},

Gen_G(delta_rad):=nu a_G f(s_G),

psi_G(c,k):=a_G(c)f(s_G(k)),
phi_m,G:=nu psi_G.                                 (E1-3)
```

`Accum` is the R2 vertical cocycle.  It vanishes on rank-preserving isometric
identity extensions and satisfies the three-stage cocycle by telescoping.
Cycle-creating additions are handled contravariantly with this disclosed
increment; no forbidden upward quotient map is introduced.

More precisely, the completed member is the R2 object

```text
phi_m=((phi_m,N)_N,(v_(M|N))_(N<=M)),

phi_m,N(c_N,k_N)=nu a_N(c_N)f(s_N(k_N)),

rho_Gamma,N(phi_m)=phi_m,N,
v_(M|N)=phi_m,M-phi_m,N compose rho_(M,N).         (E1-3a)
```

The completed notation in `(E1-3)` denotes the declared R2 renormalized
limit of this coordinate family.  Differentiation and restriction are thus
coordinatewise rather than a naive truncation of an infinite norm.

The normalizer is coefficient extraction on the generated line:

```text
Norm_G(lambda psi_G):=lambda,
Norm_G(phi_m,G)=nu.                                (E1-4)
```

Thus neither `phi_m` nor its jet is hidden inside the primitive datum.
`Gen` actually computes the action germ from the two radial record
invariants.  For symbolic `nu!=0`, `phi_m` is nonzero at every point with
`k!=0`.

### 1.3 Smoothness and flatness

For every integer `r>=0`,

```text
lim_(s->0+) s^(-r) exp(-1/s)=0.
```

Therefore `f(s_G(k))` extends smoothly by zero at `k=0`; every derivative
vanishes on `S_G`.  Consequently

```text
phi_m in Flat(S_G),
j_infinity(phi_m)|_(S_G)=0.                       (E1-5)
```

This is smooth rather than analytic.  No analyticity premise exists in P2
or R1.

### 1.4 Exact stationary jets

For `s>0`, define

```text
f_0(s):=exp(-1/s),
f_1(s):=d f_0/ds=f_0(s)/s^2,
f_2(s):=d^2 f_0/ds^2
       =f_0(s)(1/s^4-2/s^3).                      (E1-6)
```

Let `R_C:C_G->C_G^*` and `R_K:K_G->K_G^*` be the ratified Riesz maps, and
write `c^flat=R_C c`, `k^flat=R_K k`.  Direct differentiation of `(E1-3)`
gives

```text
D_C phi_m=nu f_0(s)c^flat,

F_CC^m:=D_C^2 phi_m=nu f_0(s) R_C,

F_CK^m:=D_C D_K phi_m
  =2nu f_1(s) c^flat tensor k^flat,

F_KC^m:=D_K D_C phi_m=(F_CK^m)^T,

F_KK^m:=D_K^2 phi_m
  =nu a(c)[2f_1(s)R_K+4f_2(s)k^flat tensor k^flat].
                                                               (E1-7)
```

Here `u^flat tensor v^flat` denotes the bilinear form
`(x,y)->u^flat(x)v^flat(y)`, with the displayed sector order.  At `s=0`,
all five expressions are defined to be zero by `(E1-5)`.

### 1.5 Stationary-point family

No cycle coordinate is selected.  For every carried `k`, define

```text
F_(p,nu,k)(c)
 :=D_C Gamma_base(p;c,k)+nu f_0(s(k))c^flat,

c_star,m(p,nu;k)
 :=the R5 local inverse branch F_(p,nu,k)^(-1)(0),

y_star,m(p,nu;k):=(c_star,m(p,nu;k),k).            (E1-8)
```

R5 already supplies the reducing complement and invertible total
`H_CC^m`; the implicit-function theorem therefore makes `(E1-8)` an
executable local symbolic map on that declared branch.  If more than one
R5 branch exists, the complete covariant family is retained and no branch
is selected.  A branch-dependent scalar output is forbidden until it is
proved family-invariant or separately ratified.

The Jacobian used by the solve is explicit:

```text
D_C F_(p,nu,k)
 =H_CC^base(p;c,k)+nu f_0(s(k))R_C.                (E1-9)
```

Thus `(E1-7)` and `(E1-8)` supply exactly the missing stationary jet record
without assigning a numerical point.

```text
E1_OBJECT_COMPLETE = PASS_WITHIN_PROPOSAL
E1_NEW_NUMERIC_PARAMETER = none
E1_STATIONARY_BRANCH_SELECTED = false
E1_RESPONSE_VALUE_EVALUATED = false
```

---

## 2. E2 — choice table and full gate

### 2.1 Authored choice table

| ID | Proposed field | Alternatives considered | Minimality | Void condition |
|---|---|---|---|---|
| J1 | radial primitive `(a,s)` from the ratified Hilbert norms and declared unit maps | selected cycle character; arbitrary tensor field; endpoint transport | least basis-free nonconstant datum on both R5 sectors | unit map absent, norm not restriction-natural, or datum chosen from a response target |
| J2 | standard smooth flat gate `f(s)=exp(-1/s)` | another normalized flat gate; analytic gate; zero gate | one explicit parameter-free nonzero representative of `Flat(S)` | hidden width/scale, loss of smoothness, or finite active jet appears |
| J3 | complement weight `a=1+||c||^2/2` | cycle-only member; linear selected complement covector; general invariant `a(c)` | least even norm weight with nonzero CC and potentially nonzero CK jets | complement direction selected or weight fitted to Schur cancellation |
| J4 | full R5 local inverse-branch family `(E1-8)` | choose one root; impose active-section root; add a new stationary oracle | consumes the already-ratified R5 inverse and selects nothing | branch omitted, inverse absent, or root chosen by response outcome |
| J5 | coefficient normalizer `(E1-4)` | norm-based nonlinear scale; numerical normalization; free rescaling | removes the profile/scale ambiguity while keeping `nu` symbolic | `Norm(phi_m)!=nu` or a number is assigned |

The proposal selects the J1–J5 candidate only **as the item submitted to
DoR-018**.  It has no standing before ratification.  The alternatives remain
on the record; no lane result is consumed from any of them.

### 2.2 Minimality and target independence

The profile uses only the two already-ratified norms, ordinary arithmetic,
and the explicit parameter-free flat gate displayed above.  Its definition
contains none of

```text
p, omega, kappa, H_base, Schur, RetExtract,
response sign, response zero, alpha, K_*, or a measured value.
```

`p` enters only later through `Gamma_base` in the stationary solve.  The
profile was fixed before substitution into the response.  Therefore no
coefficient or tensor can have been reverse-engineered from a desired p
behavior.

### 2.3 R1-COV, reality, and the completed Hessian cube

By `(E1-2)`,

```text
phi_(G'),m(alpha_C c,alpha_K k)=phi_G,m(c,k).
                                                               (E2-1)
```

Differentiating gives the four V004 block covariance equations.  The Riesz
maps commute with isometries; the rank-one terms in `(E1-7)` carry both
signed indices.  Hence

```text
H_AB,(G')^m alpha_B=alpha_H,A H_AB,G^m.            (E2-2)
```

Finite restriction is defined by the R2 coordinate family generated from
the same finite norms.  Differentiation commutes with that restriction, so

```text
rho_H,N,(G') alpha_H,A
 =alpha_H,A,N rho_H,N,G                            (E2-3)
```

and V004's completed `rho_H,N` cube closes unchanged.  Under orientation
reversal, `k` changes by its signed/semilinear action but `s=||k||^2` is
fixed; the real scalar profile is conjugated to itself and the tensor
indices carry their signs.  Reality passes.

### 2.4 Batching and restriction

`Depth` and `Accum` consume each DoR-016 system separately.  Batching changes
only the parenthesization of the same E_post-ordered prefix data; it does not
multiply the two systems or mix their norms.  The network output remains an
ordered tuple of per-system germs.

On rank-preserving identity extensions, the Hilbert inclusions are
isometric, so the vertical increment in `(E1-3)` is zero.  On a
cycle-creating extension, the difference is the disclosed R2 vertical
cocycle and is tested at the new stage; only contravariant restriction is
claimed.  Thus batching and restriction pass without selecting a
filtration.

### 2.5 DoR-008 finite falsifier

The independent finite R3 bottom correction is instantiated directly on the
finite physical carrier, without reading the completed output:

```text
b_N^R001(c_N,k_N):=nu a_N(c_N)f(s_N(k_N)).         (E2-4a)
```

The physical bottom-leg comparison is failure-capable: compute
`rho_Gamma,N(phi_m)` through the R2 coordinate projection and compare it to
the separately finite expression `(E2-4a)`.  Equation `(E1-3a)` gives exact
equality at every stage.  A later alteration of either the completed
vertical cocycle or the finite carrier norm would make this check fail.

Every finite active reference lies in `S_N`, so `(E1-5)` gives

```text
rho_Gamma,N(phi_m)|_(S_N)=0,
D rho_Gamma,N(phi_m)|_(S_N)=0,
D^r rho_Gamma,N(phi_m)|_(S_N)=0 for every r>=2.
                                                               (E2-4)
```

Therefore the complete Q-243/Q-279 closed forms—not merely their two-jets—
remain the independently instantiated R3 base table.  In particular,

```text
finite ordered-retarded block =0 | p-free | nu-free,
finite noise/probe blocks      =exact kappa table,
equal-history/reality/batching =unchanged.         (E2-5)
```

Off the active section, `(E2-4a)` is the proposed member-sensitive finite
correction.  It is not called a sealed Q-279 value; it remains subject to
the standing exact finite bottom-leg comparison and any future sealed
off-section datum.  This preserves the Q-406 bounded/open standing rather
than turning absence of a contradiction into a theorem.

```text
R1_COV = PASS_WITHIN_PROPOSAL
REALITY = PASS_WITHIN_PROPOSAL
BATCHING = PASS_WITHIN_PROPOSAL
RESTRICTION = PASS_WITHIN_PROPOSAL
RHO_H_N_CUBE = PASS_WITHIN_PROPOSAL
DOR008_Q243_Q279 = PASS_WITHIN_PROPOSAL
VOID_CANDIDATE = false
```

### 2.6 Member-sensitivity tags

| Object/result | Tag |
|---|---|
| radial Hilbert norms and flat-gate operation | MEMBER-INDEPENDENT PROPOSAL STRUCTURE |
| normalized direction `psi_G`, `phi_m`, its gradient, and `(E1-7)` | MEMBER-SENSITIVE |
| active-section member jets | MEMBER-INDEPENDENT ZERO over the proposed scaling line |
| `c_star,m`, `y_star,m` | MEMBER-SENSITIVE |
| base blocks and finite Q-243/Q-279 table | MEMBER-INDEPENDENT |
| total blocks, inverse instance, Schur and response values | MEMBER-SENSITIVE |
| differentiation, restriction, covariance, reality, batching, RetExtract | MEMBER-INDEPENDENT STRUCTURE/CERTIFICATES |

No result is consumed without a tag.

---

## 3. F3 — manifest nu homogeneity

For symbolic `lambda`,

```text
nu -> lambda nu
implies
phi_m -> lambda phi_m,
D_C phi_m -> lambda D_C phi_m,
F_AB^m -> lambda F_AB^m,
Norm(phi_m) -> lambda Norm(phi_m).                 (E3-1)
```

The shape `psi_G` and the stationary carrier do not change.  The stationary
point generally moves because `(E1-8)` contains `nu`, and the inverse/Schur
response is not homogeneous.  No contrary claim is made.

```text
NU_SYMBOLIC = true
DIRECT_MEMBER_JETS_DEGREE = one
STATIONARY_POINT_DEGREE = not_claimed
RESPONSE_DEGREE = not_claimed
```

---

## 4. E4 — minimal-stage instantiations

### 4.1 Reciprocal loop

The minimal reciprocal-loop cycle carrier is one-dimensional.  Choose only a
temporary unit coordinate `u_K` on that line and write `k=t u_K`; reversal
sends `t->-t`.  Keep the complete physical complement vector `c`—Q-318's
source-image line is not promoted to the physical complement.  Put

```text
s=t^2,
a=1+(1/2)||c||^2.
```

At `t!=0`, `(E1-7)` becomes

```text
F_CC^m=nu f_0(t^2)R_C,

F_CK^m=2nu t f_1(t^2)c^flat tensor u_K^flat,
F_KC^m=(F_CK^m)^T,

F_KK^m
 =nu(1+(1/2)||c||^2)
   [2f_1(t^2)+4t^2 f_2(t^2)]R_K.                 (E4-1)
```

The stationary complement vector is the exact local branch

```text
c_star(p,nu;t)
 =Root_R5[
   D_C Gamma_base(p;c,t u_K)
    +nu f_0(t^2)R_C c=0].                         (E4-2)
```

Substitution into the confirmed Schur expression gives

```text
S_loop,m=
 H_KK^base
 +nu(1+(1/2)||c_star||^2)[2f_1+4t^2 f_2]R_K
 -(H_KC^base+2nu t f_1 u_K^flat tensor c_star^flat)
   (H_CC^base+nu f_0 R_C)^(-1)
   (H_CK^base+2nu t f_1 c_star^flat tensor u_K^flat),
                                                               (E4-3)
```

with all `f_r` evaluated at `t^2` and all base blocks at
`(p;c_star,t u_K)`.  `(E4-3)` is MEMBER-SENSITIVE.  The operation forming it is
MEMBER-INDEPENDENT.  No response value or p conclusion is taken.

At `t=0`, every displayed member term is zero.  This is the exact finite
active-reference restriction, not a completed stationary evaluation.

### 4.2 S8-A rank-two stage

Use the complete rank-two cycle carrier without choosing a cycle basis.  In
any orthonormal chart let `k=(t_1,t_2)` and

```text
s=t_1^2+t_2^2,
a(c)=1+(1/2)||c||^2.
```

The instantiated tensors are the invariant forms

```text
F_CC^m=nu f_0(s)R_C,

F_CK^m=2nu f_1(s)c^flat tensor k^flat,

F_KC^m=(F_CK^m)^T,

F_KK^m=nu a(c)[2f_1(s)R_K
                       +4f_2(s)k^flat tensor k^flat].          (E4-4)
```

Define

```text
c_star=Root_R5[
  D_C Gamma_base(p;c,k)+nu f_0(s)c^flat=0],

M_CC=H_CC^base+nu f_0(s)R_C,
M_CK=H_CK^base+2nu f_1(s)c_star^flat tensor k^flat,
M_KC=H_KC^base+2nu f_1(s)k^flat tensor c_star^flat,
M_KK=H_KK^base
 +nu a(c_star)[2f_1(s)R_K+4f_2(s)k^flat tensor k^flat].
                                                               (E4-5)
```

Then

```text
S_S8A,m=M_KK-M_KC M_CC^(-1)M_CK.                 (E4-6)
```

Under the admitted exchange `c_1<->c_2`, `c_3->-c_3`, the induced signed
orthogonal map preserves `s`, `R_K`, and transforms `k^flat tensor k^flat`
by conjugation.  Hence every block in `(E4-4)` obeys R1-COV and `(E4-6)`
obeys the V004 Schur covariance theorem.  The old `c_1`-selective witness is
not admitted.

```text
RECIPROCAL_LOOP_JETS = EXPLICIT | E4-1
RECIPROCAL_LOOP_SCHUR = STRUCTURALLY_SUBSTITUTED | E4-3
S8A_JETS = EXPLICIT | E4-4
S8A_SCHUR = STRUCTURALLY_SUBSTITUTED | E4-6
P_VERDICT = not_computed
```

---

## 5. E5 — self-kill battery

| Attack | Execution | Verdict |
|---|---|---|
| target tuning | definitions `(E1-1)`–`(E1-4)` contain no p, base block, Schur, response, alpha, or desired sign/zero | PASS |
| hidden normalization | profile line fixed by `Norm(psi)=1`; `nu` is the only coefficient and remains symbolic | PASS |
| rank-two automorphism witness | radial invariants are fixed by the full signed orthogonal action; no `c_1` or cycle basis occurs | PASS |
| pendant witness | `k` is already the Gate-4/path-visible quotient coordinate; pendant/tree characters lie in the descent kernel and cannot change `s` | PASS |
| zero-jet degeneration | `nu->0` sends `phi` and every direct jet continuously to zero; the stationary branch continues to the Z/base branch wherever the R5 inverse remains uniform | PASS_WITH_BOUNDARY |
| flat-gate differentiability | apparent powers `s^-r` are killed by `exp(-1/s)` at `s=0`; every derivative extends by zero | PASS |
| cycle-creating restriction | no upward representative map is used; the exact R2 vertical cocycle carries the new radial contribution | PASS |
| member-direction collapse | radial profile is nonzero for every `k!=0` and has nonzero KK jet generically; it is not the Z member in disguise | PASS |

### 5.1 Zero-member boundary, exactly

The N member is the symbolic nonzero region `nu!=0`.  Its closure at
`nu=0` is

```text
phi_m=0,
F_AB^m=0,
F_(p,0,k)(c)=D_C Gamma_base(p;c,k).                (E5-1)
```

On any R5 chart whose complement inverse remains uniform down to zero, the
implicit-function theorem gives continuous convergence of `c_star,m` to the
base/Z branch.  If the inverse support jumps, only the direct jets converge;
the stationary branch is then a boundary between charts and no continuity
claim is made.  DoR-018 would adopt `nu!=0`, not silently replace N by Z.

### 5.2 Cardinal target-awareness test

Changing the profile to make `(E4-3)` or `(E4-6)` cancel a p-bearing base
term would violate J1/J3 immediately and void the proposal.  No such
comparison was used.  The formulas are reported without simplifying any p
dependence.

```text
SELF_KILL_ATTACKS_RUN = 8
SELF_KILL_FAILURE_FOUND = false
TARGET_AWARE_FIELD = none
ZERO_MEMBER_SILENTLY_SELECTED = false
```

---

## 6. E6 — doors and exact scope

| Door | Standing | Exact would-build/interface |
|---|---|---|
| global stationary-germ extension | `TYPE-U` beyond the R5 chart | a covariant global extension agreeing with `(E1-3)` on every stationary chart and preserving the R2 vertical cocycle |
| branch-uniform response | `TYPE-U` if multiple R5 branches survive | proof that the Schur/RetExtract output is identical on the complete covariant branch family, or a separately ratified branch rule |
| support-rank transition | `TYPE-U` at inverse-chart boundaries | graph-domain continuation through a change of `C_red`; no common inverse is assumed |
| non-edge-resolved completion | `TYPE-U` unchanged | the already-open extension beyond the edge-resolved physical carrier |
| numerical `nu` | A32/final evaluation gate | an independently sealed scale; no value is present here |
| p verdict | expressly outside this proposal | consume the cross-verified instantiated response only after DoR-018 and its cross-review |
| numerical response/alpha | expressly fenced | later Task 5/6 authorizations and public end test |

The first door does not make this jet proposal incomplete: the commissioned
object is the stationary germ and its jets, while DoR-017 already owns the
global abstract member.  It prevents this local formula from being promoted
to a new global action without a separate proof.

---

## 7. Operation ledger and final board

| Operation | Domain/kernel | Image | Sector transfer | Restriction | Tail/topology | Tag/standing |
|---|---|---|---|---|---|---|
| radial depth | R5 local carrier; quotient kernel already removed | `(a,s)` | C and K to two scalars | finite norms plus R2 cocycle | P2 Hilbert topology | PROPOSED structure |
| flat generation | radial pair | scalar action germ | both sectors through product | exact finite coordinate family | zero all-order active jet | MEMBER-SENSITIVE output |
| differentiation | smooth flat germ | four Hessian blocks | CK/KC explicit | commutes with `rho_H,N` | Fréchet/P2 | MEMBER-INDEPENDENT operation |
| stationary solve | R5 complement branch | `c_star(p,nu;k)` | K carried; C solved | finite restrictions commute on declared branch | graph topology on `C_red` | MEMBER-SENSITIVE output |
| Schur substitution | four total blocks | cycle response operator | complement eliminated only through `C_red` | V004 cube | no new tail | MEMBER-SENSITIVE value, independent operation |

```text
PROPOSED_NOT_ADOPTED -- PENDING REVIEW AND PRINCIPAL RATIFICATION

E1_EVALUABLE_STATIONARY_GERM = PROPOSED_COMPLETE
E2_CERTIFICATE_BATTERY = PASS_WITHIN_PROPOSAL
F3_NU_HOMOGENEITY = MANIFEST
E4_RECIPROCAL_LOOP = EXPLICIT_STRUCTURAL_RESULT
E4_S8A = EXPLICIT_STRUCTURAL_RESULT
E5_SELF_KILL = PASS
E6_DOORS = TYPED

DOR018_RATIFICATION_ITEM = radial_flat_N_member_stationary_germ_R001
DOR018_ITEM_SELECTED_BY_LANE = false
ADDITIONAL_ACTION_MEMBER_SELECTED = false
RANK_RATIO_ORIENTATION_FRAME_SELECTED = false
TARGET_TUNING = false

MEMBER_SENSITIVITY_TAGGING = COMPLETE
VOID_CANDIDATE = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false

P_VERDICT_COMPUTED = false
NUMERIC_RESPONSE_VALUE_COMPUTED = false
NU_EVALUATED = false

PROPOSAL_READY_FOR_CROSS_REVIEW = yes

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No alpha, `K_*`, root, numerical response value, rank ratio, or measured
constant was evaluated.  No p verdict was issued.  No register, plan,
tracker, git, commit, or push action was performed.
