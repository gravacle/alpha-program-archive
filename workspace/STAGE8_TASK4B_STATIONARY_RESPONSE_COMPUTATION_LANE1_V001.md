# STAGE8 TASK 4B: STATIONARY RESPONSE COMPUTATION - LANE 1 V001

Date: 2026-08-03  
Task: PASTE 449 / Task 4b / stationary response on the ratified square  
Lane: CODEX LANE 1  
Register head at preflight: Q-367  
Custody: computation lane; Lane 2 cross-verification required  
Authority: DoR-017 in force

```text
LEAD_RESULT = MAXIMAL_EXACT_STATIONARY_RESPONSE_STRUCTURE_COMPUTED

COMPLETED_RESPONSE =
  RetExtract_m[
    H_KK^base + D_K^2 phi_m
    -(H_KC^base + D_K D_C phi_m)
      (H_CC^base + D_C^2 phi_m)^(-1)
      (H_CK^base + D_C D_K phi_m)
  ] at y_star,m

STATIONARY_EQUATION =
  D_C Gamma_base(p_i;y_star,m)+D_C phi_m(y_star,m)=0

FINITE_ACTIVE_REFERENCE_RETARDED_BLOCK = 0 |
  p_i-free | nu-free | every finite stage | probes included

COMPLETED_P_APPEARANCE = LOCALIZED_NOT_DECIDED |
  p_i enters the base finite restrictions through omega_i and kappa_i;
  the completed base blocks and stationary point retain that inherited label;
  the ratified N-member has no declared p_i/rank dependence theorem

COMPLETED_NU_APPEARANCE = MEMBER_SENSITIVE_BUT_NOT_SCALAR_CLOSED |
  Norm(phi_m)=nu and scaling phi_m by lambda scales nu and every direct
  member jet by lambda, but nu alone does not determine those jets

VOID_CANDIDATE = false |
  covariance, reality, batching, and restriction all pass downstream

EXACT_COMPONENT_EVALUATION = TYPE-U |
  missing: evaluable N-member stationary jet and stationary-point data

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

DoR-017 makes the R1-R5 square and the nonzero N-member authoritative.  It
does not supply a closed formula for the member's `phi_m`, its divergence
generator, or its stationary jet.  The response can therefore be assembled
exactly as an operator expression and checked against every finite shadow,
but it cannot be reduced to a scalar function of `p_i` and `nu` alone.  This
is an instantiation boundary, not a failed member certificate and not a
physical p verdict.

---

## 0. Preflight, register sweep, and authorities

### 0.1 Preflight

`alpha_supervision/LOCKED_PROCESS.md` was read in full and its local sidecar
verified.  The live questions-settled register and sidecar verified before
the computation.  Its head was exactly Q-367.

```text
DOES_THE_OBJECT_EXIST = yes |
  the DoR-017 R5 stationary package and N-member exist as ratified objects

IS_THE_VERSION_CURRENT = yes | Q-367 and DoR-017

ARE_ITS_INPUTS_PRESENT = partial |
  complete for formal assembly and finite restrictions;
  incomplete for component evaluation because the N-member stationary jet
  is not written as an evaluable functional

PREFLIGHT = PASS_WITH_TYPED_EVALUATION_BOUNDARY
```

### 0.2 Register sweep

The following entries were checked before computing:

```text
Q-243  finite Keldysh rotation and p-free ordered-retarded block;
Q-279  exact finite nonzero-R table and kappa_eta;
Q-309  finite source-kernel block/mixing zeros;
Q-310  completed source-kernel zero and carrier distinction;
Q-311  origin alone does not derive the orientation intertwiner;
Q-312  sealed cycle orientation and reality covariance;
Q-313  scoped Map 1 and stationary-package residue;
Q-325  two stationary cycle-dependence routes;
Q-326  exact off-section mixing and stationary-shift forms;
Q-327  divergence-to-action bridge requirements;
Q-334  closed self-fed theory is depth-free;
Q-335  C5 is receiver-only;
Q-347-Q-357  Map 1 boundary, prefix sufficiency, all-rank descent,
             and final information-layer scope;
Q-358  quotient-only consumer certificate and five-item square residue;
Q-361-Q-366  square repair, covariance, cube, and final confirmation;
Q-367  DoR-017 ratification of the N-member with symbolic nu.
```

No later register entry existed at computation preflight.

### 0.3 Hash-verified authorities

| Authority | Verified SHA-256 | Use |
|---|---|---|
| DoR-017 | `ee9d81bf78ab0ac9361cad5b48dde2b6b8b1e9fb0e28a4fdbba41e1c43db3e45` | ratified N-member and test discipline |
| square V004 | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | R1-R5 stationary package |
| derive standard | `a9b733c711a692d5eedad8ae6acb5e2829c357c2c6aa3870c1aca2c570604136` | forced diagram and Q-408 placement |
| descent V003 | `a03e836380cbbfa08d8763bf62d6104f70aec69ae484b3b69f63489a5ce1c68c` | all-rank quotient descent |
| DoR-016 law V004 | `69f4d93b9f84075a3112fb011b9838f380fb8c0341610572170cf7a13d5aed08` | doubled endpoint access and ordered per-system towers |
| DoR-015 field signature V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | physical cycle carrier and no-selection discipline |
| divergence draft | `ed49624b6f5f0bcda94ee88a939a5751113b30d73192b2c28a5aec25829e1797` | member-interface and former bridge boundary |
| Q-243 transport | `70185aa842bc500724719c65bd66b5f07005e2214b97be0d35e07fd029d5c68c` | zero-source finite reference |
| Q-279 nonzero-R reference | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | complete finite derivative table |
| Q-309 kernel theorem | `a4c916a7cfa82c2130c82d8947c869f118e224959d7824bba45695711b4919c3` | finite support zeros |
| Q-313 factorization build | `ea8f4e9a79a9e4aca4a0b9e9aab470d78cd4d9c78794c20d9e979c0db16fbeab` | scoped source-to-cycle map |
| Q-326 stationary-family determination | `30532ecb2c08d21e28af05f1228b9c29264be99731f63c8cf5b30273bb51e7b8` | exact mixing and stationary-shift dependence |

All listed sidecars passed before their artifacts were read.

### 0.4 Load-bearing symbol distinctions

```text
N in phi_m        = the DoR-017 nonzero member alternative;
N in Z_N          = finite stage depth;
these are not the same index.

C_prop            = propagating complement in the physical R5 tangent;
J_c               = common Keldysh source coordinate;
C_prop            != J_c.

K_cycle           = physical cycle tangent in R5;
K_N=ker L_N       = finite source-kernel subspace;
their bridge is the Q-347-Q-358 information layer, not an identity.

R                 = independent bilocal probe;
RetExtract        = physical retarded extraction;
R is not a retarded leg.

nu                = symbolic homogeneous normalizer value of phi_m;
nu is not an explicit formula for phi_m or its Hessian.
```

---

## 1. W1 - stationary system with the N-member installed

### 1.1 Ratified action and stationary locus

Let `m` denote the single N-alternative member ratified by DoR-017.  No new
member is selected here.  The installed completed action is

```text
Gamma_m(p;y) = Gamma_base(p;y)+phi_m(y),
Norm_m(phi_m)=nu.                                  (W1-1)
```

Here `p` abbreviates the ordered symbolic family

```text
p_i = r_ch,i/(r_0,i+r_ch,i).
```

The complement-stationary locus and adopted stationary family are

```text
Crit_m = {y=(c,k) in D_017:
          D_C Gamma_base(p;y)+D_C phi_m(y)=0},

y_star,m=(c_star,m,k),
G_star,m = the R5 stationary two-point member/family on Crit_m. (W1-2)
```

`Crit_m` and `G_star,m` are **MEMBER-SENSITIVE** because replacing N by Z
removes every `phi_m` term.

### 1.2 Exact stationary blocks

At `y_star,m`, define

```text
F_CC^m := D_C^2 phi_m,
F_CK^m := D_C D_K phi_m,
F_KC^m := D_K D_C phi_m,
F_KK^m := D_K^2 phi_m.
```

Then the installed R5 Hessian is exactly

```text
H_CC^m = H_CC^base(p)+F_CC^m,
H_CK^m = H_CK^base(p)+F_CK^m,
H_KC^m = H_KC^base(p)+F_KC^m,
H_KK^m = H_KK^base(p)+F_KK^m.                     (W1-3)
```

Every total block in `(W1-3)` is **MEMBER-SENSITIVE**.  The base summand is
member-independent; each `F_AB^m` is member-sensitive.

### 1.3 Complement inverse, Schur block, and response

On the ratified reducing complement `C_red,m`, R5 supplies

```text
Inv_CC^m = (H_CC^m)^(-1),

Schur_m
  =H_KK^m-H_KC^m Inv_CC^m H_CK^m,                 (W1-4)

Response_m
  =RetExtract_m(Schur_m).                          (W1-5)
```

Equivalently, exposing every member term,

```text
Schur_m =
  H_KK^base+F_KK^m
  -(H_KC^base+F_KC^m)
   (H_CC^base+F_CC^m)^(-1)
   (H_CK^base+F_CK^m),                             (W1-6)
```

all evaluated at `y_star,m`.

`Inv_CC^m`, `Schur_m`, and the value of `Response_m` are
**MEMBER-SENSITIVE**.  The operations inverse-on-`C_red`, Schur formation,
and `RetExtract` are **MEMBER-INDEPENDENT STRUCTURE**.

### 1.4 Member-sensitivity ledger

| Object or result | Tag | Reason |
|---|---|---|
| prefix trace, `D_G`, `D_G^*` | MEMBER-INDEPENDENT | forced information layer |
| `Gamma_base` | MEMBER-INDEPENDENT | survives under N/Z replacement |
| `phi_m`, `D phi_m`, `D^2 phi_m` | MEMBER-SENSITIVE | zero under Z, nonzero member under N |
| `Crit_m`, `y_star,m`, `G_star,m` | MEMBER-SENSITIVE | stationarity equation contains `D_C phi_m` |
| base finite Q-243/Q-279 table | MEMBER-INDEPENDENT | owned by R3 base leg |
| finite active-section member jets | MEMBER-INDEPENDENT ZERO over admitted flat members | flatness kills every such jet on the active section |
| total stationary blocks | MEMBER-SENSITIVE | sums in `(W1-3)` |
| reducing support and inverse instance | MEMBER-SENSITIVE | depend on total `H_CC^m` |
| Schur and response values | MEMBER-SENSITIVE | depend on total blocks and stationary point |
| covariance, reality, batching, restrictions | MEMBER-INDEPENDENT CERTIFICATES | R1-COV/R5 structure applies to the installed member |

### 1.5 Downstream member certificates

The four standing certificates survive every constructed stage:

```text
covariance:
  H_AB,(G')^m alpha_B = alpha_H,A H_AB,G^m;
  Schur_(G')^m alpha_K = alpha_H,K Schur_G^m;

reality:
  orientation reversal carries cycle signs and coefficient conjugation;
  RetExtract obeys the ratified semilinear law;

batching:
  DoR-016 prefix products and R2 finite coordinates remain ordered;
  no joint network contraction is inserted;

restriction:
  rho_H,N,(G') alpha_H=alpha_H,N rho_H,N,G;
  rho_H,N(Schur_m)=Schur_m,N on the reducing finite domain.
```

No member-sensitive equality fails.

```text
N_MEMBER_COVARIANCE = PASS
N_MEMBER_REALITY = PASS
N_MEMBER_BATCHING = PASS
N_MEMBER_RESTRICTION = PASS
VOID_ON_DOWNSTREAM_FAILURE = not_triggered
VOID_CANDIDATE = false
```

---

## 2. W2 - exact finite stages and completed response

### 2.1 Per-system finite source reference

For system `i`, stage depth `N`, and symbolic probe attenuation
`u_i=exp(-eta_i/2)`, Q-279 gives

```text
Z_i,N[J,R]
  =(1-p_i)+p_i exp[-Q_i,N(R)/2]
     product_(j=1)^N r_(i,j)^n,

omega_i = p_i u_i/(1-p_i+p_i u_i),

kappa_i = omega_i(1-omega_i)
  =p_i(1-p_i)u_i/(1-p_i+p_i u_i)^2.               (W2-1)
```

At the finite reference point, the exact `W_i,N=-i hbar Log Z_i,N` table is

```text
D^2_(delta,delta)W_i,N
  = i hbar kappa_i ell_i,N tensor ell_i,N,

D^2_(delta,R)W_i,N
  =-(hbar n/2)kappa_i ell_i,N tensor Q_i,N,

D^2_(R,R)W_i,N
  =-(i hbar/4)kappa_i Q_i,N tensor Q_i,N,

D^2_(delta,c)W_i,N=0,
every block with a J_c leg=0.                     (W2-2)
```

The installed N-member's finite bottom correction is all-orders flat on the
active section, so its first and second active-section jets vanish.  Thus
`nu` does not enter `(W2-2)`.

### 2.2 Minimal reciprocal loop

DoR-016 retains two per-system towers as the ordered object

```text
Tower_AB,N=((F_1,N,A_1,N),(F_2,N,A_2,N));
```

it supplies no joint scalar contraction.  Therefore the exact finite
retarded restriction target is the ordered pair

```text
(P_R^fin H_W,1,N, P_R^fin H_W,2,N)=(0,0).         (W2-3)
```

Each zero occurs before `kappa_i` acts, so `(W2-3)` is p-free.  The active
member jets are also zero, so it is nu-free.  Multiplying the two entries or
forming a cross-system inverse would violate DoR-016 and is not done.

The completed reciprocal-loop stationary response is nevertheless only

```text
Response_loop,m
 =RetExtract[
   H_KK,loop^base+F_KK,loop^m
   -(H_KC,loop^base+F_KC,loop^m)
    (H_CC,loop^base+F_CC,loop^m)^(-1)
    (H_CK,loop^base+F_CK,loop^m)
  ]_(y_star,m).                                    (W2-4)
```

There is no finite stationary point to substitute into `(W2-4)`.  Equation
`(W2-3)` is its mandatory finite active-reference restriction, not a claimed
evaluation of `(W2-4)`.

### 2.3 S8-A rank-two stage

The admitted exchange is

```text
sigma(c_1)=c_2,
sigma(c_2)=c_1,
sigma(c_3)=-c_3.
```

At the finite active reference, the ordered-retarded block remains zero and
the noise sector carries `(W2-1)`.  The N-member contributes no active jet.
On the completed stationary carrier, its Schur operator is the rank-two
version of `(W1-6)` and transforms exactly as

```text
Schur_(sigma G),m S_sigma
  =alpha_H,K Schur_G,m,

Response_(sigma G),m
  =alpha_R Response_G,m,                           (W2-5)
```

with coefficient conjugation under reality reversal.  This computes the
covariance of the rank-two response, not its member-dependent entries.

The former `c_1`-selective member fails R1-COV and is not the installed
member.  No cycle basis is selected.

### 2.4 General finite stage

For every finite stage and every admitted bilocal probe:

```text
finite active ordered-retarded block = 0;
p_i content of that block             = none;
nu content of that block              = none;

finite quotient/noise coefficient     = kappa_i;
p_i content of noise/J_delta-R/R-R     = exact formula (W2-1);
nu content of base finite table        = none.
```

On the source kernel `K_N=ker L_N`, Q-309 further gives

```text
finite K_N/K_N block       =0,
finite K_N/complement block=0,
finite K_N/R block         =0.                    (W2-6)
```

The Q-347-Q-358 layer now transports record-visible cycle information to the
physical action quotient, but it does not turn the active reference into a
finite stationary point.  Accordingly, `(W2-6)` remains a restriction
falsifier and support statement; it is not substituted for the completed
stationary blocks in `(W1-6)`.

### 2.5 Exact completed statement

The general completed physical response is exactly `(W1-5)` and `(W1-6)`.
No further algebraic reduction is licensed because neither

```text
F_AB^m(y_star,m)=D_A D_B phi_m(y_star,m)
```

nor `y_star,m` is given in evaluable form.  Off the active section, flatness
does not set those terms to zero.  Q-326's exact sensitivity formulas remain
active:

```text
Delta M_CK = D_C D_K phi_m,

delta c_m[psi]
  =-[H_CC^m]^(-1)D_C psi(c_star,m,k).              (W2-7)
```

```text
FINITE_STAGE_REFERENCE_COMPUTATION = complete
COMPLETED_OPERATOR_FORM = complete
COMPLETED_COMPONENT_VALUES = TYPE-U
```

---

## 3. W3 - p and nu appearance map

This section reports structure only.  It does not issue the program's p
verdict.

| Object/block | `p_i` appearance | `nu` appearance | Member tag |
|---|---|---|---|
| `R_CTP`, faithful character, prefix reconstruction, `D_G` | none in the maps themselves | none | MEMBER-INDEPENDENT |
| per-system finite amplitude `A_i,N` | `(1-p_i)+p_i product Z_i,t^CTP` | none | MEMBER-INDEPENDENT |
| finite first derivatives | `omega_i` | none | MEMBER-INDEPENDENT |
| finite noise, `J_delta/R`, and `R/R` blocks | exact `kappa_i` from `(W2-1)` | none | MEMBER-INDEPENDENT |
| finite ordered-retarded block | none; exact zero | none; exact zero | MEMBER-INDEPENDENT |
| finite N-member active jets | none visible; exact zero | none visible; exact zero | MEMBER-INDEPENDENT ZERO over admissible members |
| `phi_m` and off-section member jets | no declared p/rank dependence theorem | `Norm(phi_m)=nu`; direct jets scale homogeneously with member scaling | MEMBER-SENSITIVE |
| stationary point `y_star,m` | inherited implicitly through `Gamma_base(p)`; exact closed form absent | inherited implicitly through `D_C phi_m` | MEMBER-SENSITIVE |
| `H_CC^m` | base may carry inherited p labels; member contribution's p status unspecified | through `F_CC^m`, not through a known scalar formula | MEMBER-SENSITIVE |
| `H_CK^m,H_KC^m,H_KK^m` | finite active p-free zeros do not fix off-section completed terms | through corresponding member jets | MEMBER-SENSITIVE |
| `Inv_CC^m` | nonlinear through total `H_CC^m` | nonlinear through total `H_CC^m` | MEMBER-SENSITIVE |
| `Schur_m` | exact dependence is `(W1-6)`; not simplifiable | exact dependence is `(W1-6)`; not simplifiable to `nu` alone | MEMBER-SENSITIVE |
| `RetExtract` operation | none | none | MEMBER-INDEPENDENT STRUCTURE |
| physical response value | may inherit p through base/stationary solve; unresolved | may inherit N-member dependence; unresolved | MEMBER-SENSITIVE |

### 3.1 What homogeneity proves about nu

K5-1 and DoR-017 retain the exact scaling law

```text
phi_m -> lambda phi_m,
F_AB^m -> lambda F_AB^m,
nu -> lambda nu.                                  (W3-1)
```

Thus every direct member Hessian correction is degree one along the scaling
orbit.  The inverse, stationary solve, Schur block, and response are not
degree-one objects because `F_CC^m` occurs inside an inverse and because the
evaluation point moves.  Homogeneity therefore does not make the response
proportional to `nu`.

Nor does `Norm(phi_m)=nu` reconstruct `phi_m`: a scalar norm value does not
determine the member's direction in the covariant action class.  DoR-017
selects the N-member as an authoritative object, but the corpus does not
write its evaluable stationary jet.

### 3.2 Rank-pair dependence beyond p

The finite exact source/reference table depends on `(r_0,i,r_ch,i)` only via

```text
p_i=r_ch,i/(r_0,i+r_ch,i).
```

No additional rank-pair factor occurs in `(W2-1)` or `(W2-2)`.  The R1
member interface, however, does not state whether `delta_div`, `Depth`,
`Accum`, `Gen`, or `nu` is invariant under changing the ordered rank pair at
fixed `p_i`.  Therefore:

```text
FINITE_BASE_DEPENDENCE_BEYOND_P = none | exact
COMPLETED_N_MEMBER_DEPENDENCE_BEYOND_P = TYPE-U |
  missing: rank-covariance/invariance law for the instantiated generator
```

### 3.3 Stage-independent finite finding

The following is exact and stage-independent:

```text
For every finite N and admitted probe R,
the ordered-retarded active-reference block is identically zero before
omega_i or kappa_i acts; it contains neither p_i nor nu.
```

This is a finite-shadow finding only.  No completed p verdict is stated.

---

## 4. W4 - falsifiers and regressions

### 4.1 DoR-008 finite restrictions

At `R=0`, `(W2-1)` gives

```text
omega_i -> p_i,
kappa_i -> p_i(1-p_i),

D_(J_delta)W_i,N
  =hbar n p_i ell_i,N,

D^2_(delta,delta)W_i,N
  =i hbar p_i(1-p_i)ell_i,N tensor ell_i,N,

D^2_(delta,c)W_i,N=0.
```

This exactly reproduces Q-243.  At nonzero probe, `(W2-1)` and `(W2-2)`
exactly reproduce Q-279.  The member correction has zero active jet, so it
does not alter either table.

```text
DOR008_Q243_RESTRICTION = PASS
DOR008_Q279_RESTRICTION = PASS
DOR008_FALSIFIER_FIRED = false
```

### 4.2 Equal history, reality, batching, and extension

```text
equal history:
  Z_i,N[0,R]=(1-p_i)+p_i exp[-Q_i,N(R)/2];

reality:
  Z_(-n)(Theta)=conjugate(Z_n),
  W_(-n)(Theta)=-conjugate(W_n),
  first difference derivative changes orientation sign,
  n^2 bilinears and kappa_i are unchanged;

identity zero-extension:
  appended identity factor equals one and leaves every prefix value and
  finite derivative unchanged;

batching:
  products remain E_post ordered per system and the network remains an
  ordered tuple, never a joint scalar product.
```

The R5 cube transports these certificates through the completed inverse,
Schur block, and retarded extraction.

```text
EQUAL_HISTORY = PASS
REALITY = PASS
IDENTITY_ZERO_EXTENSION = PASS
BATCHING = PASS
```

### 4.3 Permanent response-level regressions

| Regression | Execution | Result |
|---|---|---|
| one-edge tree | physical cycle quotient is a point; the N transverse action cannot vary on it; open-path access is not scalarized | PASS |
| pendant character | `D_G` removes only vertex/path-invisible content; the physical response cannot recover the pendant `w` through a quotient action | PASS |
| cycle-creating extension | only contravariant restriction is used; no forbidden upward stationary-response map is asserted | PASS |
| S8-A `c_3` | signed exchange carries `c_3` to `-c_3`; Schur and response transform covariantly | PASS |
| rank-two selective member | the old `c_1` member fails R1-COV and is not used | PASS_BY_EXCLUSION |
| reciprocal network | response shadows remain an ordered pair; no joint contraction/product is smuggled | PASS |
| source-kernel support | `(W2-6)` reproduced without calling it a completed stationary verdict | PASS |

```text
PERMANENT_REGRESSIONS = PASS
MEMBER_SENSITIVE_DOWNSTREAM_FAILURE = none_found
VOID_CANDIDATE = false
```

---

## 5. W5 - honest boundaries

### 5.1 What is complete

The following objects now exist and compose:

```text
DoR-016 doubled access and per-system prefix traces;
all-rank quotient descent and canonical action pullback;
DoR-017 completed action class and N-member interface;
stationary locus, four R5 blocks, complement inverse, Schur operation;
retarded extraction and rho_H,N covariance/restriction cube;
finite Q-243/Q-279 falsifier targets.
```

### 5.2 Exact missing evaluation object

The absent datum is not another response architecture.  It is the evaluable
record of the already-ratified N-member on its stationary locus:

```text
N_MEMBER_STATIONARY_JET_RECORD := (
  explicit delta_div, Depth, Accum, and Gen action;
  explicit phi_m on D_017 or an equivalent evaluation oracle;
  D_C phi_m and all four D_A D_B phi_m at Crit_m;
  explicit Gamma_base off the finite active section;
  a solved or symbolically characterized y_star,m;
  the p_i/rank covariance of the member datum and nu
).
```

DoR-017 names and certifies these fields as a member tuple but neither the
decision nor V004 writes their functional values.  `Norm(phi_m)=nu` supplies
one scalar label, not the missing jet.

```text
N_MEMBER_EXISTS_AS_RATIFIED_OBJECT = true
N_MEMBER_CERTIFICATES = PASS
N_MEMBER_STATIONARY_JET_EVALUABLE = false | TYPE-U
COMPLETED_COMPONENT_RESPONSE_EVALUABLE = false | TYPE-U
```

This boundary does not void DoR-017: no downstream certificate fails.  It
prevents a member-sensitive value claim until the adopted member's own data
are made executable and cross-verified.

### 5.3 No false finite promotion

There is no finite stationary point in the sealed finite system.  The exact
finite tables are restrictions/falsifiers at the active reference, not
finite evaluations of `Crit_m`.  The completed stationary point may lie off
the active section, where flatness gives no zero theorem.  Substituting the
finite zero into `(W1-6)` would repeat the Q-326-refuted shortcut.

```text
FINITE_REFERENCE_IS_STATIONARY_POINT = false | TYPE-R
FINITE_ZERO_IMPLIES_COMPLETED_RESPONSE_ZERO = false | not proved
```

### 5.4 Computation standing

```text
STATIONARY_SYSTEM_ASSEMBLED = true
COMPLEMENT_INVERSE_ASSEMBLED = true
SCHUR_OPERATOR_FORM_COMPUTED = true
RETARDED_RESPONSE_OPERATOR_FORM_COMPUTED = true

FINITE_ACTIVE_RESPONSE_SHADOW = zero | p_i-free | nu-free
COMPLETED_RESPONSE_VALUE = TYPE-U | missing N-member stationary jet record

P_DEPENDENCE_STRUCTURE = reported_not_verdict
NU_DEPENDENCE_STRUCTURE = reported_not_verdict
RANK_DEPENDENCE_BEYOND_P = finite_none / completed_TYPE-U

VOID_CANDIDATE = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No alpha, `K_*`, root, numerical response value, rank ratio, or measured
constant was evaluated.  No register, plan, tracker, git, commit, or push
action was performed.
