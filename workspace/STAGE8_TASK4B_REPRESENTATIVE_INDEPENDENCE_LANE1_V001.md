# STAGE 8 TASK 4B — REPRESENTATIVE INDEPENDENCE — LANE 1 V001

Date: 2026-08-03  
Task: PASTE 473 / Task 4b  
Lane: CODEX LANE 1  
Custody: derivation only; no registration authority

```text
REGISTER_HEAD_AT_PREFLIGHT = Q-394
PREFLIGHT = PASS
REGISTER_HEAD_AT_SEND_TIME = Q-395
SEND_TIME_RECHECK = PASS | Q-395 narrows downstream scope, no proof change

LEAD_RESULT = THE_DECISION_BLOCK_IS_NOT_REPRESENTATIVE_INDEPENDENT

DECISION_BLOCK = NOT_INVARIANT |
  witness pair I_0 and I_mu in the DoR-008-admissible completion family;
  for every source coordinate i and nonzero common-cycle direction x,

  B_i[I_mu](x,0)-B_i[I_0](x,0)
   =dot_omega_i mu_i
      [f(s) R_K+2 f_1(s) x^flat tensor x^flat] !=0,
    s=||x||_K^2,

  with the reality-completion factor carried by mu_i and no value selected

ADMISSIBLE_FAMILY_EMPTY = false | premise: DoR-017 R5
ADMISSIBLE_FAMILY_UNIQUE = false | TYPE-R
COMPLETION_CHOICE_IS_R5_OPERATOR_RESPONSE_PHYSICS = true |
  TYPE-P conditional on DoR-017 R5
P38_ALONE_IS_REGISTERED_FIXED_POINT_CRITERION = false | Q-395

FINITE_FALSIFIERS = PASS
REGISTERED_P_VERDICT_WRITTEN = false
P_VERDICT_DECLARED_BY_THIS_ARTIFACT = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The decision object is not constant on the admissible completion family.
The family contains a target-blind, covariance-complete Keldysh block
deformation built from the ratified `K_cycle` metric, its Riesz map, the
sealed common/difference injections, and the already-ratified smooth-flat
gate.  All block coefficients are carried before `RetExtract` is applied;
no support is selected for its consequence.

The mixed coefficient gives an explicit witness.  Its deformation is
K/K-only and independent of the complement variable.  Consequently the
complement critical family, `A`, `B`, `C`, `A^(-1)`, and the stationary
pullback are unchanged exactly.  Only `D` moves, so the Schur variation is
the deformation's K-Hessian itself.  Differentiating its symbolic `p_i`
coefficient and applying the kernel theorem reads off the displayed nonzero
ordered `(delta,c)` block.

Every finite active jet of the deformation is zero to all orders.  Hence it
reproduces Q-243, Q-279, Q-309, identity zero-extension, batching, reality,
and the entire independent R3 bottom-leg table.  It also passes the four
tests that killed the quadratic fallback: its action-unit coefficient is
declared, it uses no C/K seam, it makes no source/action identification, and
its complete support family is fixed before the response block is read.

Thus the completion representative is physical input, not gauge, for the
ratified R5 operator response.  The minimal witnessed fiber is an affine
action-unit/reality torsor in each covariant source orbit; the full fiber is
larger.  No member of that fiber is selected here.  Per the send-time Q-395
scope audit, this does not alone decide the registered `B_ind` fixed-point
question: that later map consumes the varying operator through `p_loc`.

---

## 0. Preflight, process, and authority ledger

### 0.1 Locked-process preflight

`alpha_supervision/LOCKED_PROCESS.md` was read before construction.  Its
live and archive copies were byte-identical.  The questions-settled register
and sidecar verified at head `Q-394`.

```text
DOES_THE_OBJECT_EXIST = no at start |
  Q-394 commissions the representative-independence theorem

IS_THE_VERSION_CURRENT = yes |
  Q-393 and Q-394 are included; DoR-016/017/018/019 are in force

ARE_ITS_INPUTS_PRESENT = yes |
  the exact kernel, the failed-instance deformation anatomy, the R2/R3/R5
  family interfaces, and the ratified carrier geometry are present

PREFLIGHT = PASS
```

### 0.2 Hash-verified authorities

| Authority | Verified SHA-256 | Use |
|---|---|---|
| certificate route | `6b7f8f985cb0915e3fa1c154a5f638c42eb03c39b58db5f79e3db91960d4f962` | exact `ker(RetExtract)` characterization |
| instance route | `f061e5d31feaed45690874a843c19cb115182e447d0fcc12601eee774289787e` | representative fiber and four failed fallback tests |
| confirmed p computation | `27790d53b018a84f5f02e97f68e885de0ebb332735307ae0fa433322a6053189` | exact `(P3-5)` / `(P3-8)` object |
| carrier metric V005 | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | completed K metric, Riesz map, units, isometries |
| square V004 | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | R2 action class, R3 bottom leg, R5 stationary package |
| DoR-008 decision | `d51a6d5c5bb0020a081cfd2adfb545b9f5ed86ce660d3feacadc5ef68140fb19` | standing finite-restriction falsifier |
| DoR-017 decision | `ee9d81bf78ab0ac9361cad5b48dde2b6b8b1e9fb0e28a4fdbba41e1c43db3e45` | nonempty R5 package premise and downstream void clause |
| Q-243 finite Keldysh transport | `70185aa842bc500724719c65bd66b5f07005e2214b97be0d35e07fd029d5c68c` | exact finite retarded zero |
| Q-279 nonzero-probe reference | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | all finite source/probe shadows |
| Q-309 kernel determination | `a4c916a7cfa82c2130c82d8947c869f118e224959d7824bba45695711b4919c3` | finite kernel and mixing zeros |
| Q-395 seam audit | `337769f4a122512de5c79a9fe4f936c4edac2170bfe3bc471484d4ff85724a34` | operator-response versus fixed-point scope |

The live supervision mirrors verified as:

```text
LOCKED_PROCESS.md =
  e8a4c00d3cd13126bd8d20588419aba344a50d27c6d084a8243ed5494d7721f2
QUESTIONS_SETTLED_REGISTER_V001.md_AT_INITIAL_PREFLIGHT =
  1068ca5689c1b0484727d6bdf5581b16aaff8238fbc91681c8925c32db181eb4
QUESTIONS_SETTLED_REGISTER_V001.md_AT_SEND_TIME_RECHECK =
  35c74caa5c5216bd34d1e1b14d6ec2689e7cf4f4e1df010df5de1a299d00e108
```

### 0.3 Register sweep

The following entries were checked for action representatives, flat fibers,
stationary pullbacks, Schur support, and restriction authority:

```text
Q-243   finite ordered (delta,c) block is zero and p-free;
Q-247   finite separation has named class/retraction hypotheses;
Q-252   no finite stationary point exists; zero source is not a stationary
        evaluation rule;
Q-279   all probe-on finite blocks and p weights are exact;
Q-309   finite kernel, complement-mixing, and probe-mixing blocks are zero;
Q-313   source correlator data cannot substitute for a physical action Hessian;
Q-315   bounded restriction squares and zero-tail scope;
Q-321-Q-324
        finite jets do not select an off-section physical action; flat
        deformations remain finite-visible off the active section;
Q-326   off-section flat deformations can change mixing and stationary data;
Q-358-Q-367
        R2/R3/R5 family interfaces and DoR-017 ratification;
Q-384   DoR-019 ratified the completed carrier metric and units;
Q-390   DoR-018 ratified Shape K, leaving the base p-jet member-independent;
Q-391-Q-392
        exact decision formula and its component boundary;
Q-393   ker(RetExtract) is exactly the zero ordered (delta,c) block;
Q-394   carrier completion does not select Gamma_base; the quadratic
        fallback failed normalization, seam, source/action, and support;
Q-395   P3-8 gates the R5 operator response, while the registered fixed-point
        criterion is p_loc[X_p] plus the fixed-point branch condition.
```

No entry identifies the admissible representative fiber as gauge and no
entry proves the decision block constant on that fiber.

### 0.4 Send-time Q-395 compatibility addendum

Q-395 arrived after the initial `Q-394` preflight and before shipment.  Its
scope theorem defines

```text
X_p:=RetExtract[dot Schur_base],
partial_p B_ind(K,p)=p_loc[X_p],
dK/dp=[1-partial_K B_ind]^(-1)p_loc[X_p]          (N0-1)
```

when the displayed fixed-point inverse is licensed.  The present artifact
proves that `X_p` varies across admissible R5 completion representatives.
It does **not** prove that `p_loc[X_p]` varies: `p_loc` may annihilate all or
part of the affine direction `(N2-24)`, and its R5 consumption typing remains
`TYPE-U`.  Therefore:

```text
Q395_CHANGES_N2_NONINVARIANCE_PROOF = false
Q395_NARROWS_CONSEQUENCE = true |
  noninvariance is established for the R5 operator response;
  registered fixed-point dependence still requires p_loc and branch data
SEND_TIME_RECHECK = PASS                              (N0-2)
```

### 0.5 Symbol distinctions

```text
I              = one admissible completion tuple, not a selected physical one;
Gamma_base,I   = physical base action, not -Log Z or a source Hessian;
mu             = symbolic action-unit/reality-torsor coefficient, not nu;
K              = K_cycle, not K_* and not kappa_record;
k=(x,y)        = common/difference Keldysh coordinates on K, not a chosen
                 graph-cycle basis;
R_K            = ratified K-sector Riesz map, not retarded response;
B_i[I]         = ordered (delta,c) block of the base Schur p_i derivative;
RetExtract     = structural block extraction, not a numerical evaluation;
representative = completion/action datum, not an orientation or frame member.
```

---

## 1. N1 — the admissible completion family

### 1.1 Family definition

Let `Adm_base` be the family of tuples

```text
I=(Gamma_base,I,(Gamma_base,I,N)_N,(v_(M|N),I),
   Crit_I,c_star,I,A_I,B_I,C_I,D_I,C_red,I,Inv_CC,I,
   Schur_I,RetExtract_I,
   Cov_I,Real_I,Batch_I,Restrict_I,Units_I).       (N1-1)
```

Membership means all of the following.

**A. R2 completed-action structure.**

```text
Gamma_base,I in Act_phys^017;
rho_Gamma,N Gamma_base,I=Gamma_base,I,N;
Gamma_base,I,M
 =Gamma_base,I,N compose rho_(M,N)+v_(M|N),I;
the vertical increments obey the R2 cocycle;
rank-preserving identity extensions have zero vertical increment;
the declared renormalized scalar net converges in the R2 topology.
                                                               (N1-2)
```

**B. DoR-008 and R3 finite authority.**

For every finite stage,

```text
pi_Jet,N(Gamma_base,I,N)=BaseJet_N^bot,           (N1-3)
```

and the independent finite action leg reproduces every sealed finite result,
including:

```text
equal-history normalization;
the exact Q-243/Q-279 source/probe table;
the zero, p-free ordered (delta,c) block;
the exact kappa_eta noise and J_delta/R weights;
Q-309's zero kernel, kernel-complement, and kernel-R blocks;
one-edge/tree zero-cycle behavior;
S8-A signed-exchange covariance;
identity zero-extension and every subsequently sealed finite theorem.
                                                               (N1-4)
```

`(N1-3)` fixes the physical finite jet class.  It does not identify
`Gamma_base,I,N` with the source functional.

**C. R5 stationary package.**

```text
Crit_I={y in D_017:D_C Gamma_base,I(y)=0};
the complete critical family is retained without root selection;
A_I=H_CC,I, B_I=H_CK,I, C_I=H_KC,I, D_I=H_KK,I;
C_red,I reduces A_I and Inv_CC,I is its declared two-sided inverse;
Schur_I=D_I-C_I Inv_CC,I B_I;
RetExtract_I is the sealed ordered Keldysh extraction. (N1-5)
```

The R5 restriction/inverse cube, automorphism covariance, reality, and
batching certificates must commute on this tuple.

**D. Ratified carrier and unit discipline.**

All fields live on DoR-019's completed `C_prop direct-sum K_cycle` carrier.
Every C/K map uses the R4-only seam; `R_C` and `R_K` remain same-sector;
no implicit cross-sector unit or selected unit frame is permitted.

### 1.2 The four failed-gate tests as family boundaries

The four failures of the instance fallback become explicit membership
conditions, not commentary:

| Boundary test | Admissibility condition | Failure |
|---|---|---|
| normalization | every action coefficient is derived or carried as an explicit symbolic member of its unit/reality torsor | setting a carrier metric coefficient to `1`, or identifying it silently with `nu`, excludes the tuple |
| mixed seam | every C/K mixed block factors through the named R4 conversion set; zero is used only when proved | a bare C/K identity, implicit unit, or convenient `B=C=0` assumption excludes the tuple |
| source/action | `Gamma_base`, its Hessian, and its stationary equation are physical-action data independent of `-Log Z`, `W`, and source Hessians | any direct source/action relabeling excludes the tuple |
| support | the support class/family is declared before `RetExtract` or any `(P3-8)` consequence is read; causal/contact and quotient conditions are checked independently | choosing a block because it lands in or out of `ker(RetExtract)` excludes the tuple |

These tests are failure-capable.  Passing finite jets alone is insufficient.

### 1.3 Nonemptiness and the affine action

DoR-017 ratifies the five R1-R5 fields, including the supplied
`Gamma_base`/R5 package.  Therefore

```text
Adm_base != empty                                      (N1-6)
```

as a ratified premise.  This statement does not produce or select an
executable member.  If no R5 member exists, DoR-017's downstream-failure
clause fires; that is not the standing branch of this derivation.

Let `V_adm` be the vector space of physical base-action deformations whose
finite coordinates are flat on every active `S_N`, whose R2 vertical
increments obey the cocycle, and which satisfy covariance, reality,
batching, quotient, unit, and the four boundary tests.  Then

```text
I in Adm_base and Psi in V_adm
 => I+Psi in Adm_base                                  (N1-7)
```

whenever the unchanged R5 reducing domain remains valid.  The witness below
is K/K-only, so it leaves that reducing domain and inverse unchanged exactly.

---

## 2. N2 — exact variation of the decision block

### 2.1 General variation

For `I_t=I_0+t Psi`, write all blocks at the full complement critical family
of `I_t`.  The exact decision block is

```text
B_i[I_t]
 :=RetExtract_(I_t)[X_i[I_t]],

X_i[I_t]
 :=partial_(p_i)^tot[
      D_t-C_t A_t^(-1)B_t
    ].                                                (N2-1)
```

The Schur variation at fixed `t` has the exact algebraic form

```text
delta Schur
 =delta D
  -delta C A^(-1)B
  +C A^(-1)delta A A^(-1)B
  -C A^(-1)delta B,                                  (N2-2)
```

where every `delta` includes any change induced through the stationary
family.  Therefore

```text
delta B_i
 =RetExtract[
    partial_(p_i)^tot(delta Schur)
  ]                                                   (N2-3)
```

on the R5 domain.  Formula `(N2-3)` is the family-variation version of
`(P3-5)`; it assumes no representative.

### 2.2 Target-blind complete Keldysh deformation family

Use the ratified orthogonal K metric and write a Keldysh vector as

```text
k=(x,y),
x=k_c,
y=k_delta,
s_K(k)=||x||_K^2+||y||_K^2.                       (N2-4)
```

Let

```text
f(s)=exp(-1/s) for s>0,
f(0)=0,
f_1(s)=f(s)/s^2 for s>0.                          (N2-5)
```

This is the same parameter-free smooth-flat gate already certified on the
ratified K norm.  Before applying `RetExtract`, form the complete
carrier-minimal Keldysh block family

```text
Q_(a,b,d)
 :=[[a R_K, Adv(b R_K)],
    [b R_K, d R_K]]_(c,delta),                    (N2-6)
```

where:

```text
a and d range over their full reality-compatible coefficient torsors;
b ranges over the full retarded coefficient torsor;
Adv(b R_K) is fixed by the ratified reality law;
all coefficients carry the action-unit factor explicitly;
no coefficient value is selected.
```

Every block in `(N2-6)` is contact-supported, hence inside the sealed
causal/contact support allowance.  The family uses the full Riesz map and
no graph-cycle basis.  It is defined before any response block is inspected.

Set

```text
q_(a,b,d)(k):=(1/2)<k,Q_(a,b,d)k>,

Psi_(a,b,d)(p;c,k)
 :=sum_i omega_i(p_i) f(s_K(k_i))
      q_(a_i,b_i,d_i)(k_i),                       (N2-7)

omega_i(p_i)=p_i u_i/(1-p_i+p_i u_i),
dot_omega_i:=partial_(p_i)omega_i
             =u_i/(1-p_i+p_i u_i)^2.
```

On the admitted source domain, `u_i` is nonzero and the anchored logarithm
excludes a zero denominator.  Hence `dot_omega_i` is symbolically nonzero.

For a connected realization with one source weight, the sum has one term.
For a network it is componentwise.  Under relabeling, the coefficient tuple
is transported with the source orbit; under batching, the sum concatenates.
No source sector is selected.

The coefficients `(a_i,b_i,d_i)` are completion-representative fields.
They are neither set equal to `nu` nor assigned numerical values.  Their
explicit unit/reality torsors satisfy the normalization boundary.  Because
`Psi` is K/K-only, it adds no C/K map and cannot violate the mixed seam.  It
uses the physical K carrier, not a source Hessian.  Its full support family
was fixed in `(N2-6)`, so the support boundary is also satisfied.

### 2.3 R2 and finite admissibility of the deformation

At every finite stage define `Psi_N` by `(N2-4)`–`(N2-7)` using the finite
ratified metric and Riesz map.  Since `f(s)q(k)` is smooth-flat at `k=0`,

```text
D^m Psi_N|_(S_N)=0 for every finite derivative order m. (N2-8)
```

Thus `(N1-3)` and every sealed finite jet in `(N1-4)` are unchanged.

On rank-preserving identity extensions, DoR-019/W3 isometry gives

```text
Psi_M=Psi_N compose rho_(M,N),                    (N2-9)
```

so the vertical increment is zero.  On a cycle-creating extension define

```text
v^Psi_(M|N)
 :=Psi_M-Psi_N compose rho_(M,N).                 (N2-10)
```

Then, using functoriality of `rho`,

```text
v^Psi_(L|N)
 =v^Psi_(M|N) compose rho_(L,M)+v^Psi_(L|M),     (N2-11)
```

which is exactly the R2 cocycle.  This does not invent a forbidden upward
map; it supplies the allowed contravariant coordinate family and its
declared vertical difference.

For the directed finite-core approximants `k_N->k` in the DoR-019 K norm,
isometry gives `s_K(k_N)->s_K(k)` and continuity of the Riesz pairing gives
`q_N(k_N)->q(k)`.  Continuity of `f` then yields

```text
Psi_N(p;k_N)->Psi(p;k)                            (N2-11a)
```

in the declared scalar topology.  Thus the completed value is the R2
renormalized finite-coordinate limit; no weak-star, bidual, or silent
class-formation step is used.

Reality holds by the `Adv` completion in `(N2-6)`.  Batching holds by the
componentwise sum.  Quotient compatibility follows because `R_K` is defined
on the physical quotient and tree/pendant directions are absent before
`Psi` is formed.

Consequently

```text
Psi_(a,b,d) in V_adm.                             (N2-12)
```

### 2.4 Exact block dependence

The deformation is independent of the complement variable.  Hence, for
every value of its coefficients,

```text
Crit_(I+Psi)=Crit_I,
c_star,(I+Psi)=c_star,I as the full unselected family,

delta A=0,
delta B=0,
delta C=0,
delta D=D_K^2 Psi.                                (N2-13)
```

No inverse or stationary-pullback remainder is hidden.  Substituting
`(N2-13)` into `(N2-2)` gives the exact finite-deformation identity

```text
Schur_(I+Psi)=Schur_I+D_K^2 Psi,                 (N2-14)

X_i[I+Psi]
 =X_i[I]+dot_omega_i
    D_K^2[f(s_K)q_(a_i,b_i,d_i)].                (N2-15)
```

This uses exactly the ratified base-entry map through `omega_i`; no new
rank port is introduced.  At zero probe `u_i=1` and `dot_omega_i=1`
symbolically, but no `p_i` value is evaluated.

Now apply the kernel theorem.  The decision-block variation is

```text
B_i[I+Psi]-B_i[I]
 =dot_omega_i RetExtract{
    D_K^2[f(s_K)q_(a_i,b_i,d_i)]
  }.                                              (N2-16)
```

Only after `(N2-6)`–`(N2-16)` are fixed do we inspect the ordered block.
Take a nonzero common-cycle test direction and no difference component:

```text
k=(x,0),
s=||x||_K^2>0,
x^flat=R_K x.                                     (N2-17)
```

The diagonal coefficients `a_i,d_i` contribute no ordered mixed block at
`(x,0)`.  The complete mixed coefficient gives, by two exact derivatives,

```text
RetExtract{
  D_K^2[f(s_K)q_(a_i,b_i,d_i)]
 }_(x,0)

 =b_i[
      f(s)R_K
      +2f_1(s)x^flat tensor x^flat
    ].                                            (N2-18)
```

Indeed, for test directions `xi` in the common slot and `eta` in the
difference slot,

```text
D_delta D_c[f(s_K)q_b]_(x,0)[eta,xi]
 =b_i{
    f(s)g_K(eta,xi)
    +2f_1(s)g_K(x,eta)g_K(x,xi)
   }.                                             (N2-19)
```

For `s>0`, `f(s)>0`; `R_K` is an isomorphism by DoR-019.  Therefore the
operator in brackets is nonzero.  The reality factor carried by `b_i` does
not change nonzeroness.

### 2.5 Witness pair and non-invariance theorem

Let `I_0` be any member of the ratified nonempty family `Adm_base`.  Define

```text
I_zero :=I_0+Psi_(0,0,0),
I_mu   :=I_0+Psi_(0,mu,0),                       (N2-20)
```

where `mu` is an arbitrary symbolic nonzero member of the required
action-unit/reality torsor, transported family-wide.  Neither member is
selected as physical.  By `(N2-12)`, both are admissible.  By `(N2-18)`,

```text
B_i[I_mu](x,0)-B_i[I_zero](x,0)
 =dot_omega_i mu_i[
      f(s)R_K
      +2f_1(s)x^flat tensor x^flat
    ]
 !=0.                                             (N2-21)
```

This refutes representative independence:

```text
DECISION_BLOCK_CONSTANT_ON_Adm_base = false | TYPE-R
ADMISSIBLE_FAMILY_UNIQUE = false | TYPE-R
DECISION_BLOCK = NOT_INVARIANT | witness (N2-20)-(N2-21)
                                                               (N2-22)
```

The proof neither chooses `mu` nor evaluates it.  It shows that the decision
map has a nonzero direction on the admissible representative fiber.

### 2.6 The physical fiber exposed

Define

```text
Dec:Adm_base -> product_i RetHess_i,
Dec(I):=(B_i[I])_i.                               (N2-23)
```

The witnessed affine subfiber is

```text
Dec(I_0)+{
  (dot_omega_i b_i H_mix,i)_i:
  b is a covariant section of the action-unit/reality torsor
},                                                (N2-24)

H_mix,i(x)
 :=f(||x||^2)R_K
   +2f_1(||x||^2)x^flat tensor x^flat.            (N2-25)
```

The full image of `Dec` may be larger because complement-coupled flat
deformations also remain.  `(N2-24)` is the minimal proven fiber, not an
exhaustion claim.

The fiber cannot be absorbed into Shape K's `nu`:

```text
nu is p-independent and belongs to the ratified N member;
b_i multiplies an explicit p_i-dependent base deformation;
the mixed Keldysh profile q_b is not the radial Shape K profile;
identifying b_i with nu would violate the normalization boundary.
```

Thus completion-representative physics adds a new declared R5 operator-
response field unless a future theorem kills or fixes `(N2-24)`.  That field,
or an exhaustive larger replacement, is the object for ratification at this
layer.  The later `p_loc` consumption and fixed-point branch remain separate.

---

## 3. N3 — falsifiers and minimal stages

### 3.1 Full finite check

At every finite active section, `k=0`.  The smooth-flat identity `(N2-8)`
gives

```text
Psi_N=0,
D Psi_N=0,
D^2 Psi_N=0,
...
```

to every finite order.  Therefore the deformation changes none of:

```text
Q-243:
  T_CTP^T [[1,-1],[-1,1]] T_CTP=[[0,0],[0,1]],
  H_(delta,c),N=0;

Q-279:
  omega_eta=p u_eta/(1-p+p u_eta),
  kappa_eta=p(1-p)u_eta/(1-p+p u_eta)^2,
  H_(delta,c),N(R_eta)=0,
  the exact delta/delta, delta/R, and R/R blocks;

Q-309:
  finite kernel block=0,
  finite kernel-complement mixing=0,
  finite kernel-R mixing=0.                       (N3-1)
```

The finite tables remain owned by `BaseJet_N^bot`; no source/action equality
is used.

### 3.2 Reciprocal loop

For the reciprocal ordered pair, apply `(N2-7)` componentwise:

```text
Psi_pair=Psi_1 direct-sum Psi_2.                  (N3-2)
```

No product, common inverse, or joint contraction is formed.  At the finite
active point both components vanish to all orders.  On either completed
rank-one loop and every nonzero common direction `x_i`, however,

```text
delta B_i
 =dot_omega_i mu_i[
   f(||x_i||^2)R_K,i
   +2f_1(||x_i||^2)x_i^flat tensor x_i^flat
 ] !=0.                                          (N3-3)
```

Thus the minimal reciprocal loop already witnesses non-invariance without
coupling the two ordered systems.

### 3.3 S8-A

On S8-A, use the full rank-two quotient metric and Riesz map.  Under the
admitted signed exchange `sigma`, DoR-019 isometry gives

```text
R_K,(G') sigma_K=sigma_H,K R_K,G,
s_K(sigma_K x)=s_K(x),
(sigma_K x)^flat=sigma_H,K x^flat.               (N3-4)
```

Consequently

```text
H_mix,(G')(sigma_K x)
 =sigma_H,K H_mix,G(x) sigma_K^(-1),             (N3-5)
```

with the coefficient `mu` transported to `sigma.mu`.  The full cycle space,
not a `c_1`, `c_2`, or `c_3` member, is used.  Equation `(N3-3)` therefore
remains nonzero and covariant at S8-A; no cycle-selective witness is hidden.

### 3.4 One-edge, tree, pendant, and batching regressions

| Regression | Exact check | Result |
|---|---|---|
| one-edge / connected tree | `K_cycle=0`, hence `Psi=0` and `delta B=0` | **PASS** |
| pendant quotient | `R_K` is formed after the Gate-4 quotient; no pendant character returns | **PASS** |
| identity zero-extension | W3 isometry gives `(N2-9)` and zero vertical increment | **PASS** |
| cycle-creating extension | only the R2 vertical difference `(N2-10)` is used; its cocycle is `(N2-11)` | **PASS** |
| batching | componentwise sum, with no cross-system contraction | **PASS** |
| reality | `Adv` completion and coefficient parity transport exactly | **PASS** |
| R4-only unit seam | no C/K arrow is added; all K/K action units are explicit | **PASS** |
| source/action | no source functional, source Hessian, or `-Log Z` occurs in `Psi` | **PASS** |
| support anti-tuning | complete `(a,b,d)` family fixed before block extraction | **PASS** |
| rank/ratio | all `p_i`, ranks, `nu`, and `mu` remain symbolic | **PASS** |

### 3.5 Falsifier outcome

The finite falsifier does not identify the representative because every
member of `(N2-20)` has the same sealed finite jet data.  It remains fully
active: any future representative whose finite coordinate changes a sealed
entry is excluded immediately.

```text
N3_DOR008_FINITE_CHECK = PASS
N3_RECIPROCAL_LOOP = PASS_AND_WITNESSES_NONINVARIANCE
N3_S8A = PASS_AND_WITNESSES_NONINVARIANCE
N3_ONE_EDGE_TREE = PASS
FINITE_ZERO_PROMOTED_TO_COMPLETED_ZERO = false
```

---

## 4. Exact consequence and handoff

### 4.1 What is proved

```text
1. Adm_base is nonempty as a DoR-017 R5 premise.
2. Adm_base carries a nontrivial admissible flat-deformation action.
3. The decision map Dec has the nonzero affine direction (N2-24).
4. Therefore the ordered (delta,c) block is not representative-independent.
5. Neither P_FREE nor P_DEPENDENT for the R5 operator response is
   representative-independent before the completion fiber is derived or
   ratified.
6. The registered fixed-point result remains downstream at p_loc[X_p] and
   is not declared here.
```

This is a theorem about the family.  It is not a choice inside the family.

### 4.2 Ratification interface

The minimal new physics object is

```text
COMPLETED_BASE_ACTION_REPRESENTATIVE_OR_FIBER_RULE := (
  a covariant section or retained family in Adm_base;
  the action-unit/reality coefficient field b;
  its R2 finite coordinates and vertical cocycle;
  the normalization relation to, or independence from, nu;
  its Keldysh support class declared before response evaluation;
  DoR-008, reality, batching, quotient, restriction, and unit certificates;
  a void clause on any finite disagreement
).                                                (N4-1)
```

Live neutral alternatives include:

```text
derive b=0 or another unique covariant section;
ratify a specified nonzero section with b symbolic;
retain the full covariant fiber and forbid a single p-verdict;
reject the completed base package.
```

No alternative is recommended here.

### 4.3 Six-account disclosure

| Operation | Domain | Image | Kernel / freedom | Restriction | Completion / topology | Standing |
|---|---|---|---|---|---|---|
| finite bottom leg | sealed finite table | physical action jet class | `Flat(S_N)` representative fiber | exact Q-243/Q-279/Q-309 | finite | **RATIFIED** |
| admissible deformation | physical K quotient | base flat-action fiber | all active finite jets | `(N2-8)`–`(N2-11)` | R2 declared topology | **TYPE-P family theorem** |
| complement stationarity | `Gamma_base+Psi` | same full `Crit` | none added by K-only witness | R5 covariance | completed C carrier | **UNCHANGED EXACTLY** |
| Schur variation | K/K Hessian | `D_K^2 Psi` | no C elimination ambiguity | R5 square | completed K carrier | **TYPE-P** |
| decision map | admissible completion | ordered `(delta,c)` block | zero-block kernel from Q-393 | finite output zero | varies by `(N2-24)` | **NOT_INVARIANT / TYPE-R** |
| representative rule | admissible family | physical completion | affine `b` fiber | falsifier retained | not selected | **TYPE-U / ratification object** |

---

## 5. Final board

```text
N1_ADMISSIBLE_FAMILY = DEFINED
N1_FOUR_GATE_BOUNDARIES = BINDING
N1_FAMILY_NONEMPTY = true | premise: DoR-017 R5

N2_GENERAL_VARIATION = (N2-2)-(N2-3)
N2_WITNESS_PAIR = I_zero, I_mu | both admissible
N2_BLOCK_VARIATION =
  dot_omega_i mu_i[f(s)R_K+2f_1(s)x^flat tensor x^flat] !=0

DECISION_BLOCK = NOT_INVARIANT | witness pair (N2-20)-(N2-21)
ADMISSIBLE_FAMILY_UNIQUE = false | TYPE-R
ADMISSIBLE_FAMILY_EMPTY = false | premise: DoR-017 R5
COMPLETION_REPRESENTATIVE_IS_GAUGE = false | TYPE-R
COMPLETION_CHOICE_IS_R5_OPERATOR_RESPONSE_PHYSICS = true |
  TYPE-P conditional on DoR-017 R5
P38_ALONE_IS_REGISTERED_FIXED_POINT_CRITERION = false | Q-395
P_LOC_ON_AFFINE_DIRECTION = TYPE-U

N3_FINITE_FALSIFIERS = PASS
N3_MINIMAL_STAGES = PASS
MACHINERY_APPEAL = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false

REGISTERED_P_VERDICT_WRITTEN = false
P_VERDICT_DECLARED_BY_THIS_ARTIFACT = false
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
