# STAGE 8 TASK 4B - p-DEPENDENCE COMPUTATION - LANE 1 V001

Date: 2026-08-03  
Task: PASTE 469 / Task 4b  
Lane: CODEX LANE 1  
Status: **EXACT SYMBOLIC COMPUTATION COMPLETE - CROSS-VERIFICATION REQUIRED**

```text
REGISTER_HEAD_AT_PREFLIGHT = Q-390
PREFLIGHT = PASS

THE_COMPUTATION_FINDS =
  at fixed physical cycle argument k,
  Response_K(p,nu;k)=Response_base(p;k)+nu Response_flat(k);
  every possible p_i dependence is exactly the stationary pullback of the
  base Schur response, no dependence on (r_0,r_ch) survives beyond p_i,
  and nu enters affinely with a p_i-free coefficient.

P_DEPENDENCE = CONDITIONAL_WITH_EXACT_CONDITION |
  dependent iff the total p_i derivative of the base stationary Schur
  response displayed in (P3-8) is nonzero for at least one i;
  Shape K contributes zero to that derivative

RANK_PAIR_DEPENDENCE_BEYOND_P = none_on_the_ratified_chain

NU_DEPENDENCE = affine |
  coefficient=RetExtract[T_K(k)] | p_i-free;
  nu dependence is nontrivial iff that coefficient is nonzero

FINITE_ACTIVE_RETARDED_BLOCK = 0 |
  p_i-free | nu-free | every finite stage | probes included

VOID_CANDIDATE = false
VOID_ON_COVARIANCE_FAILURE = false
VOID_ON_REALITY_FAILURE = false
VOID_ON_BATCHING_FAILURE = false
VOID_ON_RESTRICTION_FAILURE = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

This artifact computes and reports the dependence structure.  It does not
register the program's p verdict.  The result becomes a registered verdict
only after independent cross-verification and the registrar's entry.

---

## 0. Preflight, register sweep, and authorities

### 0.1 Preflight

`alpha_supervision/LOCKED_PROCESS.md` and its sidecar were read and verified.
The live questions-settled register and sidecar verified before computation;
its head was exactly `Q-390`.

```text
DOES_THE_OBJECT_EXIST = yes |
  DoR-018 ratifies the executable Shape K stationary jets

IS_THE_VERSION_CURRENT = yes |
  Q-390 and DoR-016/017/018/019 are in force

ARE_ITS_INPUTS_PRESENT = yes |
  confirmed stationary Schur expression, ratified Shape K jets,
  ratified carrier metric, and every finite restriction target are present

PREFLIGHT = PASS
```

### 0.2 Register sweep

The following settled entries were checked before computing:

```text
Q-243   finite Keldysh rotation; ordered-retarded block zero and p-free;
Q-279   exact probe-on finite table; omega_i and kappa_i;
Q-306   physical raw correlator and even pairing normalization;
Q-309   all finite source-kernel blocks zero with p absent;
Q-313   Map 1 and source-to-cycle restriction target;
Q-315   physical restriction squares and exact finite-shadow reproduction;
Q-334   closed self-fed theory depth-free;
Q-344   DoR-016 network law ratified;
Q-365   R5 Hessian cube, inverse, Schur, and retarded covariance;
Q-367   DoR-017 square and symbolic N member ratified;
Q-368   exact stationary response expression and p-entry localization;
Q-369   response cross-verification and former jet boundary;
Q-370   jets underivable from the thin datum;
Q-372-Q-383  target-tuning kill and carrier-metric gate sequence;
Q-384   DoR-019 carrier metric ratified;
Q-385-Q-389  germ V002/V003, lambda repair, and final re-check;
Q-390   DoR-018 Shape K jets ratified; evaluation commissioned.
```

No later register entry existed at computation preflight.

### 0.3 Hash-verified authorities

Every authority below matched its expected hash before it was read.

| Authority | SHA-256 | Use |
|---|---|---|
| DoR-016 decision | `b4157df6f327e261f40389d5a3011a0aef66ee0f198d8ebba8b1b9303142d708` | ordered doubled network law |
| DoR-017 decision | `ee9d81bf78ab0ac9361cad5b48dde2b6b8b1e9fb0e28a4fdbba41e1c43db3e45` | square, N member, tags, void clause |
| DoR-018 decision | `57532849d0766741a365d001596275ef4f2ca612063ef6d05031292711a0614d` | ratified Shape K jets |
| DoR-019 decision | `6ab72b0cb3a93e123eb1d3c5088fc83361d86c6dc739f0a886380dbd2d143f1f` | C/K metrics, Riesz maps, units, routing |
| response computation | `be570c182ef875b557395b62c382ee875420ac0462e2efb5774e9600f794b27a` | confirmed Schur expression and p map |
| response cross-verification | `cac131d949a917576e30332b2f4ec76ca7db57d6d4683e91cfeac658994c499b` | independent X1-X7 standard |
| germ V003 | `231bbd1d77c39a45249149b47f9bb543e7a748c67b477dfde1f245efecd4aa13` | Shape K definition and jets |
| metric V005 | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | ratified norms and no implicit unit |
| square V004 | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | R5 stationary package and cube |
| source germ DoR-014 | seal verified | rank-pair gauge theorem and p ratio |

### 0.4 Load-bearing symbol distinctions

```text
p_i       = r_ch,i/(r_0,i+r_ch,i), symbolic source-sector weight;
nu        = symbolic Shape K normalizer, independent free input;
N         = finite stage when used in Z_N, not the N member;
k         = physical cycle argument, not K_* and not a root;
C         = reducing propagating complement, not a Keldysh common source;
R         = bilocal probe, not RetExtract;
T_K       = Shape K Hessian coefficient, not a response value;
Response  = completed retarded extraction, not any numerical observable.
```

---

## 1. P1 - Shape K substitution

### 1.1 Ratified Shape K jets

On the DoR-019 K carrier let

```text
s=s_K(k)=||k||_K^2,
k^flat=R_K k,
f(s)=exp(-1/s) for s>0 and f(0)=0.
```

DoR-018 installs

```text
phi_K(k)=nu f(s),                                  (P1-1)

D_C phi_K=0,
F_CC^K=D_C^2 phi_K=0,
F_CK^K=D_C D_K phi_K=0,
F_KC^K=D_K D_C phi_K=0,                           (P1-2)

F_KK^K=D_K^2 phi_K=nu T_K(k),

T_K(k):=2f_1(s)R_K
       +4f_2(s)k^flat tensor k^flat.              (P1-3)
```

Every line in `(P1-1)`-`(P1-3)` is **MEMBER-SENSITIVE** except the ratified
metric/Riesz structure.  `T_K` is member-independent geometry; its
coefficient `nu` and its inclusion as the N-member correction are
member-sensitive.  At `k=0`, smooth flatness gives `T_K(0)=0`.

### 1.2 Exact block substitution

Write the base blocks at the Shape K stationary point as

```text
A(p;k):=H_CC^base(p;c_star(p,k),k),
B(p;k):=H_CK^base(p;c_star(p,k),k),
C(p;k):=H_KC^base(p;c_star(p,k),k),
D(p;k):=H_KK^base(p;c_star(p,k),k).               (P1-4)
```

These base blocks are **MEMBER-INDEPENDENT**.  Shape K gives, exactly,

```text
H_CC^K=A,
H_CK^K=B,
H_KC^K=C,
H_KK^K=D+nu T_K.                                  (P1-5)
```

Thus the complement inverse is the base inverse:

```text
Inv_CC^K=A^(-1).                                  (P1-6)
```

`(P1-5)` and `(P1-6)` are **MEMBER-SENSITIVE EQUALITIES** because replacing
the adopted N member by Z removes only the `nu T_K` summand; their base
objects and inverse operation are member-independent.

### 1.3 Completed Schur response

Substitution into the confirmed R5 Schur expression gives

```text
Schur_K(p,nu;k)
 =D+nu T_K-C A^(-1)B
 =Schur_base(p;k)+nu T_K(k),                      (P1-7)

Schur_base(p;k):=D-C A^(-1)B.                    (P1-8)
```

The sealed retarded extraction is linear on a fixed orientation carrier.
Therefore

```text
Response_K(p,nu;k)
 =RetExtract[Schur_base(p;k)]
  +nu RetExtract[T_K(k)]

 =Response_base(p;k)+nu Response_flat(k),         (P1-9)

Response_flat(k):=RetExtract[T_K(k)].             (P1-10)
```

Equation `(P1-9)` is the completed symbolic response with every Shape K jet
substituted.  The first summand is **MEMBER-INDEPENDENT BASE CONTENT**.  The
second is **MEMBER-SENSITIVE**, p-free, and degree one in `nu`.  The total
response remains **MEMBER-SENSITIVE**.

No complement inverse, mixed block, stationary point, or retarded operation
contains `nu` after this substitution.  This is stronger than the generic
N-member homogeneity result: for Shape K the full response is affine in
`nu`, not merely the direct jet.

---

## 2. P2 - complement stationary equation

### 2.1 Exact stationary locus

The generic installed equation was

```text
D_C Gamma_base(p;c,k)+D_C phi_m(c,k)=0.
```

Shape K makes the second term identically zero, so

```text
D_C Gamma_base(p;c_star(p,k),k)=0.                (P2-1)
```

Consequently

```text
c_star,K(p,k)=c_star,base(p,k),
Crit_K=Crit_base.                                  (P2-2)
```

on the complete covariant R5 branch family.  These equalities are
**MEMBER-INDEPENDENT UNDER THE RATIFIED K/Z COMPARISON**: Shape K does not
move the complement stationary family.  The cycle argument `k` is carried;
no root or cycle member is selected.  The full R5 stationary two-point
object is not identified with a Z/base object: it remains member-sensitive
through the K/K block and the response term in `(P1-9)`.

### 2.2 Exact p derivative of the stationary family

On the R5 reducing domain, `A=H_CC^base` is invertible.  Differentiating
`(P2-1)` at fixed `k` gives

```text
partial_(p_i)c_star
 =-A^(-1) partial_(p_i)[D_C Gamma_base]
    evaluated at (p,c_star(p,k),k).               (P2-3)
```

Here `partial_(p_i)` on the right means the explicit p derivative before
the stationary pullback.  Formula `(P2-3)` is exact; it evaluates no root.
It proves that every stationary-point p dependence is base-only and
member-independent.  In particular, `nu` contributes neither directly nor
through motion of the evaluation point.

---

## 3. P3 - exact p, rank-pair, and nu dependence

### 3.1 The only p input map

For system `i` and symbolic probe attenuation `u_i`, define

```text
d_i(p_i):=1-p_i+p_i u_i,

omega_i(p_i)=p_i u_i/d_i,

kappa_i(p_i)=omega_i(1-omega_i)
 =p_i(1-p_i)u_i/d_i^2.                            (P3-1)
```

Q-368 and its cross-verification establish the only explicit p port:

```text
p_i -> (omega_i,kappa_i)
    -> base first/noise/probe restrictions
    -> Gamma_base and base stationary blocks
    -> c_star(p,k), Schur_base(p;k), Response_base(p;k). (P3-2)
```

Shape K adds no p port.  The exact derivatives of the finite coordinates are

```text
d omega_i/dp_i=u_i/d_i^2,

d kappa_i/dp_i
 =(1-2omega_i)u_i/d_i^2.                          (P3-3)
```

At the zero-probe reference, `u_i=1`, so `omega_i=p_i` and
`kappa_i=p_i(1-p_i)` without any numerical evaluation.

### 3.2 Exact conditional-dependence criterion

For one chosen symbolic `p_i`, place a dot over a base block to denote its
total derivative along the stationary family:

```text
dot X:=partial_(p_i)X+(D_C X)[partial_(p_i)c_star]. (P3-4)
```

Using `(P2-3)` and differentiating `(P1-8)` gives

```text
dot Schur_base
 =dot D
  -dot C A^(-1)B
  +C A^(-1)dot A A^(-1)B
  -C A^(-1)dot B.                                (P3-5)
```

The Shape K term has zero p derivative:

```text
partial_(p_i)[nu T_K(k)]=0                       (P3-6)
```

at fixed `k` and independent free input `nu`.  Since `RetExtract` itself
has no p content,

```text
partial_(p_i)Response_K
 =RetExtract[dot Schur_base].                     (P3-7)
```

Therefore the exact classification is

```text
Response_K is p_i-free
  iff RetExtract[
       dot D-dot C A^(-1)B
       +C A^(-1)dot A A^(-1)B
       -C A^(-1)dot B
     ]=0 for every i;                             (P3-8)

Response_K is p-dependent
  iff the displayed quantity is nonzero for at least one i. (P3-9)
```

Equations `(P3-3)`-`(P3-5)` make every p input and the stationary-point
pullback explicit.  The ratified chain supplies no theorem that forces the
quantity in `(P3-8)` either to vanish or to be nonzero on the completed
stationary family.  Thus `CONDITIONALLY_DEPENDENT` is the exact computation,
not a missing-object claim and not an inference from notation.

The nonconstancy of `omega_i` or `kappa_i` alone proves a live base input;
it does not prove that the final retarded pullback fails to annihilate it.
Conversely, the finite zero theorem cannot prove `(P3-8)` because the finite
active reference is not the completed stationary point.

### 3.3 Ordered rank pair beyond p

DoR-014 proves that presentations with the same ordered ranks are gauge:
the trace-preserving block-unitary quotient leaves `p_i`, `Z_inc`, and every
exported derivative invariant.  Across different ordered rank pairs, the
ratified normalized source formulas contain the pair only through

```text
p_i=r_ch,i/(r_0,i+r_ch,i).                        (P3-10)
```

The later operations do not introduce another rank port:

```text
DoR-016 trace/tower law     -> p_i only;
Gamma_base/base restrictions -> omega_i(p_i),kappa_i(p_i) only;
DoR-019 C/K metric         -> record-cycle geometry, no source-rank factor;
Shape K                    -> nu and K norm only;
inverse/Schur/RetExtract   -> no independent rank input.        (P3-11)
```

Hence, at fixed `nu` and fixed record realization,

```text
Response_K(r_0,r_ch;nu;k)
 =R_hat(p(r_0,r_ch);nu;k),                        (P3-12)

RANK_PAIR_DEPENDENCE_BEYOND_P = none.             (P3-13)
```

Same-rank presentation freedom is removed by the gauge theorem; equality
for distinct integer pairs with the same ratio follows from the explicit
factorization `(P3-10)`-`(P3-12)`.  No rank or ratio is selected or
evaluated.

### 3.4 Symbolic nu dependence

Equation `(P1-9)` gives the complete result:

```text
Response_K(p,nu;k)
 =Response_base(p;k)+nu Response_flat(k).         (P3-14)
```

Thus the response is affine in `nu`; its direct N/Z difference is exactly

```text
Response_K-Response_Z=nu Response_flat(k).        (P3-15)
```

The coefficient is p-free and rank-pair-free.  The dependence on `nu` is
nontrivial exactly when `Response_flat(k)!=0`.  At `k=0`, all-orders
flatness gives `Response_flat(0)=0`, so every finite active shadow is
nu-free.  No value of `nu` or response is evaluated.

---

## 4. P4 - minimal stages

### 4.1 Reciprocal loop

DoR-016 keeps the two systems as an ordered pair; no joint scalar
contraction is permitted.  For `i in {1,2}`, define the base stationary
Schur and Shape K coefficient on the reciprocal-loop carrier by

```text
S_base,i(p_i;k_i)
 :=D_i-C_i A_i^(-1)B_i,

T_i(k_i)
 :=2f_1(s_i)R_K,i
   +4f_2(s_i)k_i^flat tensor k_i^flat.            (P4-1)
```

The exact completed ordered response is

```text
Response_loop,K
 :=(
   RetExtract_1[S_base,1(p_1;k_1)+nu T_1(k_1)],
   RetExtract_2[S_base,2(p_2;k_2)+nu T_2(k_2)]
   )

 =(
   Response_base,1(p_1;k_1)+nu Response_flat,1(k_1),
   Response_base,2(p_2;k_2)+nu Response_flat,2(k_2)
   ).                                             (P4-2)
```

Each entry obeys the criterion `(P3-8)` independently.  The pair is
**MEMBER-SENSITIVE** through its additive Shape K terms; its ordering and
per-system operations are member-independent.

At the finite active reference `k_1=k_2=0`, Q-243/Q-279 and flatness give

```text
rho_fin(Response_loop,K)=(0,0),                   (P4-3)
```

before either `omega_i` or `kappa_i` can enter.  This restriction is exactly
p-free and nu-free.  No product of the two zero entries is formed.

### 4.2 S8-A rank-two stage

For arbitrary `k` in the complete rank-two cycle carrier,

```text
Response_S8A,K(p,nu;k)
 =Response_base,S8A(p;k)
  +nu RetExtract_S8A[
     2f_1(||k||_K^2)R_K
     +4f_2(||k||_K^2)k^flat tensor k^flat
   ].                                             (P4-4)
```

Under the admitted signed exchange

```text
sigma(c_1)=c_2,
sigma(c_2)=c_1,
sigma(c_3)=-c_3,
```

the norm is invariant and `k^flat tensor k^flat` transports covariantly.
Therefore both summands in `(P4-4)` obey the R1-COV/R5 response square;
no cycle basis or orientation member is selected.

At the finite active reference `k=0`, the Shape K term is zero and the
ordered-retarded base restriction is zero:

```text
rho_fin(Response_S8A,K)=0                         (P4-5)
```

with no p or nu content.  Off the active section, `(P4-4)` is the complete
symbolic rank-two response and carries the same exact p condition as
`(P3-8)`.

### 4.3 General stage

For every admitted stage/realization G,

```text
Response_G,K(p,nu;k)
 =Response_G,base(p;k)
  +nu RetExtract_G[T_K,G(k)].                     (P4-6)
```

This is family-natural on rank-preserving restrictions and covariant under
all admitted automorphisms.  Cycle-creating arrows retain the ratified
contravariant/vertical accounting; no forbidden upward stationary map is
introduced.

---

## 5. P5 - falsifiers and permanent regressions

### 5.1 Finite-shadow reproduction

For system `i`, the exact finite Q-279 coefficients remain

```text
omega_i=p_i u_i/(1-p_i+p_i u_i),
kappa_i=p_i(1-p_i)u_i/(1-p_i+p_i u_i)^2.         (P5-1)
```

The nonzero finite base blocks remain

```text
D^2_(delta,delta)W_i,N
 =i hbar kappa_i ell_i,N tensor ell_i,N,

D^2_(delta,R)W_i,N
 =-(hbar n/2)kappa_i ell_i,N tensor Q_i,N,

D^2_(R,R)W_i,N
 =-(i hbar/4)kappa_i Q_i,N tensor Q_i,N.          (P5-2)
```

Every block with a common-source leg remains zero.  Shape K's independently
finite bottom germ has `k_N=0`, so all member jets are zero.  Consequently

```text
FINITE_ORDERED_RETARDED_BLOCK = 0
FINITE_ORDERED_RETARDED_P_CONTENT = none
FINITE_ORDERED_RETARDED_NU_CONTENT = none
Q243_REPRODUCTION = PASS
Q279_REPRODUCTION = PASS
```

The p-dependent noise/probe blocks in `(P5-2)` are not relabeled as the
retarded response.

### 5.2 Member certificates

| Certificate | Shape K check | Result |
|---|---|---|
| covariance | K norm, Riesz map, and `T_K` transport isometrically; base R5 blocks already covariant | **PASS** |
| reality | `f_1,f_2,nu` are real symbolic scalars; orientation reversal transports/conjugates tensor coefficients by the ratified law | **PASS** |
| batching | per-system towers stay ordered; Shape K adds no joint contraction | **PASS** |
| restriction | `rho_H,N(T_K)=T_K,N`; active finite target is zero; R5 inverse/Schur cube remains base on C | **PASS** |

No certificate fails after the substitution.

### 5.3 Permanent regressions

| Regression | Re-execution | Result |
|---|---|---|
| one-edge/tree | cycle carrier is zero or pendant content is removed before the K norm; no member response is manufactured | **PASS** |
| reciprocal ordered pair | `(P4-2)` remains an ordered pair; no product or joint inverse | **PASS** |
| S8-A signed exchange | `(P4-4)` transforms covariantly and uses the full invariant norm | **PASS** |
| rank-two cycle-selective witness | excluded member is not reintroduced; Shape K depends on full `s_K` | **PASS** |
| cycle-creating extension | no upward stationary-response map claimed; only ratified restriction/vertical accounting used | **PASS** |
| pendant/tree metric | DoR-019 quotient/fullness regression unchanged | **PASS** |
| implicit C/K unit | Shape K has no mixed member block; base Schur uses only the ratified R4 routing | **PASS** |
| lambda subfiber | inapplicable to adopted Shape K; no hidden CK coefficient enters | **PASS** |
| N/Z visibility | difference remains the explicit `nu Response_flat` term | **PASS** |

### 5.4 Fresh falsifier - p-entry does not prove p-response

**Attack.** Infer completed p dependence merely because `(P3-3)` is
nonzero.  This would be invalid if `RetExtract[dot Schur_base]=0` by support,
symmetry, or cancellation.

**Result.** The attack kills that inference, not the computation.  The
artifact reports the exact iff condition `(P3-8)` and does not upgrade a
nonconstant input coordinate into a nonconstant output without evaluating
the pullback.  Conversely, it does not infer completed p-freedom from the
finite zero theorem.  Both unsupported shortcuts are excluded.

```text
FRESH_FALSIFIER = p_entry_is_not_p_response
UNCONDITIONAL_P_DEPENDENCE_INFERENCE = TYPE-R
UNCONDITIONAL_P_FREEDOM_INFERENCE = TYPE-R
EXACT_CONDITIONAL_CLASSIFICATION = PASS
```

---

## 6. P6 - dependence report and tag ledger

### 6.1 Computed dependence map

| Object/result | p_i | rank pair beyond p | nu | Tag |
|---|---|---|---|---|
| `c_star` / complement critical family | base-only through `(omega_i,kappa_i)` | none | none | MEMBER-INDEPENDENT under K/Z |
| `H_CC,H_CK,H_KC` and inverse | base-only | none | none | MEMBER-INDEPENDENT under K/Z |
| base K/K block and base Schur | base pullback; criterion `(P3-8)` | none | none | MEMBER-INDEPENDENT BASE |
| Shape K `F_KK` | none | none | linear `nu T_K` | MEMBER-SENSITIVE |
| completed Schur | conditional through base only | none | affine, p-free coefficient | MEMBER-SENSITIVE TOTAL |
| `RetExtract` operation | none | none | none | MEMBER-INDEPENDENT STRUCTURE |
| completed response | conditional exactly by `(P3-8)` | none | affine exactly by `(P3-14)` | MEMBER-SENSITIVE TOTAL |
| finite active retarded block | none; exact zero | none | none; exact zero | MEMBER-INDEPENDENT ZERO |
| finite noise/probe blocks | exact `kappa_i(p_i)` | none | none | MEMBER-INDEPENDENT BASE |

### 6.2 Lead result in one sentence

**The computation finds that Shape K factorizes the completed stationary
response as `Response_base(p;k)+nu Response_flat(k)`: p can act only through
the base stationary Schur pullback and does so exactly when `(P3-8)` is
nonzero, no ordered-rank information survives beyond the ratios `p_i`, and
the member scale enters affinely with a p-free coefficient.**

### 6.3 Void and fence board

```text
N_MEMBER_COVARIANCE = PASS
N_MEMBER_REALITY = PASS
N_MEMBER_BATCHING = PASS
N_MEMBER_RESTRICTION = PASS

VOID_CANDIDATE = false
VOID_ON_DOWNSTREAM_FAILURE = not_triggered

BUILD_COMPLETE_FOR_SYMBOLIC_DEPENDENCE = true
CROSS_VERIFICATION_REQUIRED = true
REGISTERED_P_VERDICT_WRITTEN = false

MACHINERY_APPEAL = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false

ALPHA_EVALUATED = false
K_STAR_OR_ROOT_EVALUATED = false
NUMERIC_RESPONSE_VALUE_EVALUATED = false
RANK_OR_RATIO_EVALUATED = false
MEASURED_CONSTANT_COMPARISON = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No register, plan, tracker, git, commit, or push action was performed.
