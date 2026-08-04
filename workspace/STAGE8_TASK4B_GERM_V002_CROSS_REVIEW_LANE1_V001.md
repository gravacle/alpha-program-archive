# STAGE8 TASK 4B - GERM V002 CROSS-REVIEW - LANE 1 V001

```text
TASK = PASTE 466 | adversarial cross-review of both V002 germ shapes
REGISTER_HEAD = Q-385
REVIEWED_ARTIFACT_SHA256 = c673b6f59dda3981e02088676b11fa5606c882880d8f3b7111682e08175c5aa5

LEAD_RESULT:
  SHAPE_K = READY
  SHAPE_CK = NOT_READY | H1,H4,H6,H7
  KILLING_COUNTERFAMILY =
    phi_CK,lambda=nu(1+lambda q_C)f(s_K)
  OMITTED_PARAMETER = lambda | dimensionless relative complement coupling
  DISPLAYED_JETS = algebraically correct at lambda=1
  METRIC_AND_UNIT_CERTIFICATES = pass

READY_FOR_DOR018_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Preflight and custody

Preflight passed before V002 was read.

| Check | Result |
|---|---|
| register head | `Q-385` exactly |
| germ V002 SHA-256 | `c673b6f59dda3981e02088676b11fa5606c882880d8f3b7111682e08175c5aa5` - match |
| germ V002 sidecar | verified `OK` |
| DoR-019 decision | `6ab72b0cb3a93e123eb1d3c5088fc83361d86c6dc739f0a886380dbd2d143f1f` - sidecar verified `OK` |
| metric V005 | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` |
| V001 adjudication standard | `2e1b011069043c1cc03277178be061a8b7d1704d2146be97eb799965aef9c679` |
| DP1-DP10 standard | `c39de7a0ef5a29e92ded5fc961b54dfe933171ea291b221c38bf0aa3a9c0dcf3` |
| response computation | `be570c182ef875b557395b62c382ee875420ac0462e2efb5774e9600f794b27a` |
| square V004 | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` |
| locked process and register | both sidecars verified `OK` |

```text
DOES_THE_OBJECT_EXIST = yes
IS_THE_VERSION_CURRENT = yes | Q-385
ARE_ITS_INPUTS_PRESENT = yes | DoR-019 in force
```

Custody remained review-only. No register, plan, tracker, git, commit, push,
physical-value, root, `alpha`, `K_*`, or p-verdict action was performed.

## 1. Verdict table

| Item | Shape K | Shape CK | Reason |
|---|---|---|---|
| H1 G2 repair | **PASS** | **KILL** | carrying K and CK neutrally repairs support selection, but CK fixes the relative coefficient in `1+q_C` and justifies it by the Hessian it produces; the lawful `lambda` family is omitted |
| H2 G3 repair | **PASS** | **PASS** | DoR-019 supplies the norms, Riesz maps, unit classes, automorphism isometries, quotient descent, and restriction machinery; the displayed germs satisfy the resulting covariance and Hessian certificates |
| H3 G7 repair | **PASS** | **PASS** | vertical action/Hessian cocycles are claimed, while cycle-creating stationary-root restriction remains honestly `TYPE-U` |
| H4 DP1-DP10 | **PASS** | **KILL** | K discloses its free gate representative; CK fails DP6/DP9 because `lambda` is neither generated nor included in the complete residual family |
| H5 jets and Schur | **PASS** | **PASS at displayed lambda=1** | both derivative towers and structural substitutions recompute correctly; every mixed CK term uses the ratified R4 seam |
| H6 fiber statement | **PASS** | **KILL** | `{K,CK,reject}` omits the nonredundant internal CK fiber `lambda`; consequences therefore are not fully typed neutrally |
| H7 fresh attack | **PASS** | **KILL** | a K-wide amplitude is absorbed into symbolic `nu`; the analogous CK relative coefficient cannot be absorbed and survives as physical member freedom |

Because the commissioned fiber carries both shapes, one incomplete live
shape keeps the DoR-018 package from the principal.

## 2. Common definitions and independent derivative check

Use the ratified carrier invariants

```text
s=s_K(k)=||k||_K^2,
q=q_C(c)=(1/2)||c||_C^2,
c^flat=R_C c,
k^flat=R_K k,

f(s)=exp(-1/s), s>0; f(0)=0,
f_1(s)=f'(s)=f(s)/s^2,
f_2(s)=f''(s)=f(s)(s^(-4)-2s^(-3)).             (C0-1)
```

The carrier derivatives are

```text
D_C q=c^flat,       D_C^2 q=R_C,
D_K s=2k^flat,      D_K^2 s=2R_K.                (C0-2)
```

The smooth zero extensions of `f`, `f_1`, and `f_2`, including all radial
derivatives, vanish at `k=0`. Thus both displayed profiles reproduce the
finite active zero jet to all orders.

## 3. H1 - G2 repair and reverse-engineering

### 3.1 Shape K

V002 proposes

```text
phi_K(c,k)=nu f(s).                               (H1-K1)
```

A target engineer seeking a nonzero off-section member with no direct C or
mixed member block would indeed arrive at a K-only profile. The proposal,
however, does not use that consequence to choose K over CK: both support
classes survive, and the K definition is justified by the ratified radial
invariant, smooth flatness, and absence of a selected cycle direction.

The exact flat gate is openly authored, other certified flat gates are
listed as alternatives, and no uniqueness or divergence-determined status
is claimed. The order ledger therefore repairs the old support-selection
kill for Shape K.

```text
H1_K = PASS
```

### 3.2 Shape CK

V002 proposes

```text
phi_CK(c,k)=nu(1+q)f(s).                          (H1-C1)
```

Retaining Shape K alongside Shape CK repairs the old binary support choice,
but it does not fix the internal CK normalization. The full carrier-lawful
family is

```text
phi_CK,lambda(c,k)
  :=nu(1+lambda q)f(s),                           (H1-C2)
```

where `lambda` is a dimensionless real authored parameter. For every
`lambda`:

```text
isometry invariance = true;
reality = true;
all-orders finite flatness = true;
origin normalization at c=0 = true;
R4 unit typing = true;
quotient and pendant descent = true.
```

For `lambda!=0`, every member has exactly the same CK support class and the
same lowest even complement degree. `lambda=0` is the K boundary. Therefore
carrier invariance, degree, and origin normalization do not force
`lambda=1`.

Nor can `lambda` be absorbed into `nu`. If

```text
nu(1+lambda q)=nu'(1+q) for every q,
```

then comparison of the constant and quadratic coefficients gives

```text
nu'=nu,
nu lambda=nu,
lambda=1.                                        (H1-C3)
```

Thus distinct `lambda` values are distinct members at fixed symbolic `nu`.

The proposal's Section 1.1 says the chosen factor's complement Hessian is
`R_C` as part of the reason for choosing it. That is a jet consequence,
not carrier data, and it occurs before the chronology claims jets are first
computed. A tuner requesting the normalized member correction

```text
F_CC=nu f(s)R_C
```

reverse-engineers `lambda=1` exactly. This is the bounded remnant of the G2
failure: shape-level neutrality is repaired, coefficient-level neutrality
is not.

```text
CK_RELATIVE_COEFFICIENT_FORCED = false
CK_RELATIVE_COEFFICIENT_DISCLOSED = false
CONSEQUENCE_READ_BEFORE_CK_COEFFICIENT_FIXED = true
H1_CK = KILL
```

## 4. H2 - certificates on the DoR-019 geometry

For either displayed profile, admitted automorphisms preserve `q` and `s`.
Therefore

```text
phi_S,G'(alpha_C c,alpha_K k)=phi_S,G(c,k),       (H2-1)
```

and twice differentiating gives the correctly typed block covariance

```text
H_AB,G'^S alpha_B=alpha_H,A H_AB,G^S.             (H2-2)
```

DoR-019 now supplies every premise V001 lacked:

1. positive completed C/K norms and same-sector Riesz maps;
2. realization-automorphism isometry and reality transport;
3. W3 rank-preserving isometry and adjoint restriction;
4. carrier-unit duality and R4-only cross-sector routing;
5. pendant/tree quotient descent;
6. the R5-generated Hessian restriction cube.

The finite bottom profiles are instantiated by the same carrier formulas.
Using the ratified R5 definition

```text
rho_H,N(D^2 Gamma):=D^2(rho_Gamma,N Gamma),
```

gives

```text
rho_H,N H_AB^S=H_AB,N^S rho_D,N                 (H2-3)
```

on the declared R5-generated domain. This is not an arbitrary external
Hessian claim. Rank-two exchanges preserve the norms and carry the Riesz
covectors/tensors. Pendant and tree directions are removed before either
radius is formed, so neither profile reintroduces quotient gauge content.

The same proofs apply to every `lambda` in `(H1-C2)` because `lambda` is a
scalar. Thus the metric repair is complete even though the CK member fiber
is not.

```text
H2_K = PASS
H2_CK = PASS
```

## 5. H3 - cycle-creating scope

V002 correctly separates:

```text
completed-to-finite Hessian restriction;
rank-preserving W3 naturality;
cycle-creating vertical action/Hessian differences.               (H3-1)
```

For a cycle-creating arrow it defines only

```text
v_MN^S=phi_M^S-phi_N^S compose rho_MN,
DeltaH_MN^S=H_M^S-H_N^S compose rho_D,MN,        (H3-2)
```

whose three-stage cocycles telescope. It expressly does not claim

```text
rho_C,N(Crit_M^S)=Crit_N^S.
```

Shape CK acknowledges the exact V001 countermodel. Shape K claims only the
base critical naturality independently present in R5. The unbuilt
stationary-root theorem is typed rather than smuggled.

```text
CYCLE_CREATING_STATIONARY_RESTRICTION = TYPE-U
H3_K = PASS
H3_CK = PASS
```

## 6. H4 - DP1-DP10 audit

### 6.1 Shape K

Shape K correctly records:

```text
LOG_DIVERGENCE_PROVENANCE = false;
shape tag = authored;
flat-gate representative = authored with alternatives;
finite legs = independently instantiated from finite ratified metrics;
finite active jets = zero;
target consequence = absent from membership;
cycle-creating stationary restriction = TYPE-U.
```

Its datum-to-profile map is thin and largely ignores the datum, but V002
does not call the result log-divergence-determined. DP9 discloses the K
support, flat-gate representative/family, `nu`, and stationary branch
family. That is the honest result allowed by the reach theorem when the
authored profile fiber carries the load.

```text
DP_K = PASS_WITHIN_PROPOSAL
H4_K = PASS
```

### 6.2 Shape CK

DP1-DP5 and DP7-DP8 are correctly typed for the displayed member. The
failure is DP6/DP9:

1. DP6 requires target-independent generation. The `lambda=1` coefficient
   is justified in part by the Hessian it produces.
2. DP9 requires a complete residual family for every feature outside the
   image of DP1-DP8.
3. The datum is shape-thin and supplies no coefficient identity for
   `lambda`.
4. The choice table discloses the gate family but not the independent
   relative complement family `(H1-C2)`.

All finite squares remain valid for arbitrary `lambda`, so no finite
falsifier removes this family.

```text
DP6_CK_TARGET_INDEPENDENCE = not proved
DP9_CK_RESIDUAL_DISCLOSURE = incomplete | missing lambda
H4_CK = KILL
```

## 7. H5 - jets and Schur substitutions

### 7.1 Shape K jets

Independent application of `(C0-2)` gives

```text
D_C phi_K=0,
F_CC^K=F_CK^K=F_KC^K=0,

D_K phi_K=2nu f_1(s)k^flat,
F_KK^K
 =nu[2f_1(s)R_K+4f_2(s)k^flat tensor k^flat].    (H5-K1)
```

The structural Schur block is

```text
Schur_K
 =(H_KK^base+F_KK^K)
  -H_KC^base (H_CC^base)^(-1) H_CK^base.         (H5-K2)
```

The profile, direct jet, total block, inverse instance, stationary family,
and Schur result are member-sensitive. The carrier metrics, operation, base
blocks, covariance, units, and active-section zero are member-independent.

### 7.2 Shape CK jets

For the displayed `lambda=1` member, differentiation gives exactly

```text
D_C phi_CK=nu f(s)c^flat,
F_CC^CK=nu f(s)R_C,
F_CK^CK=2nu f_1(s)c^flat tensor k^flat,
F_KC^CK=(F_CK^CK)^T,

D_K phi_CK=2nu(1+q)f_1(s)k^flat,
F_KK^CK
 =nu(1+q)[2f_1(s)R_K
           +4f_2(s)k^flat tensor k^flat].        (H5-C1)
```

The general lawful family instead has

```text
F_CC^(CK,lambda)=nu lambda f(s)R_C,
F_CK^(CK,lambda)=2nu lambda f_1(s)c^flat tensor k^flat,
F_KC^(CK,lambda)=(F_CK^(CK,lambda))^T,

F_KK^(CK,lambda)
 =nu(1+lambda q)[2f_1(s)R_K
                  +4f_2(s)k^flat tensor k^flat]. (H5-C2)
```

The displayed structural substitution is algebraically correct:

```text
Schur_CK
 =(H_KK^base+F_KK^CK)
  -(H_KC^base+F_KC^CK)
    (H_CC^base+F_CC^CK)^(-1)
    (H_CK^base+F_CK^CK).                         (H5-C3)
```

Every mixed member tensor is an R4 block

```text
K->C^* or C->K^*,
[F_CK]=[F_KC]=U_action U_C^(-1)U_K^(-1).
```

Consequently

```text
[H_KC Inv_CC H_CK]
 =U_action U_K^(-2)
 =[H_KK],                                        (H5-C4)
```

with no bare C/K map or implicit conversion unit. The omitted `lambda` is
a dimensionless action-member parameter, not a unit-conversion defect.

```text
H5_K = PASS
H5_CK_DISPLAYED_ALGEBRA = PASS
```

## 8. H6 - DoR-018 fiber

Shape K is honestly typed as an exact proposed representative plus a
disclosed flat-gate alternative family and reject. Its overall amplitude is
the already-symbolic `nu` and no additional radial amplitude survives.

Shape CK is not yet an exact item. The lawful authored fiber is at least

```text
{(CK,lambda):lambda in Lambda_adm},               (H6-1)
```

where the admissible real set `Lambda_adm` must be derived from any intended
extra conditions or carried completely. `lambda=0` meets the K boundary;
nonzero values remain CK members. V002's table neither proves
`Lambda_adm={1}` nor presents `(H6-1)` to the principal.

The neutral top-level fiber is therefore not merely

```text
{K,CK,reject}.
```

It contains an undisclosed CK subfiber whose members change the stationary
equation, complement inverse, mixed blocks, and Schur operator. No such
member-sensitive consequence may be stated before this subfiber is
ratified or proved irrelevant.

Both displayed profiles are linear in symbolic `nu`, so their
`nu`-homogeneity is correct. The defect is independent of that scaling.

```text
H6_K = PASS
H6_CK = KILL
```

## 9. H7 - fresh attacks

### 9.1 Shape K - hidden amplitude attack

Introduce a dimensionless amplitude `mu`:

```text
phi_K,mu=nu mu f(s).                              (H7-K1)
```

For nonzero `mu`, set `nu'=nu mu`. Every value and jet then equals the
original Shape K formula with `nu'`. Because `nu` is already the symbolic
homogeneous normalizer and no value is fixed, `mu` is redundant rather than
a new relative member parameter. `mu=0` is the disclosed zero degeneration.

Non-proportional changes of the flat gate are not silently discarded: the
choice table expressly carries another fully certified smooth-flat gate as
an alternative and makes no uniqueness claim.

```text
FRESH_ATTACK_K = PASS
H7_K = PASS
```

### 9.2 Shape CK - relative coupling attack

Apply the same amplitude test only to the complement-dependent part:

```text
phi_CK,lambda=nu f(s)+nu lambda q f(s).           (H7-C1)
```

Unlike `(H7-K1)`, the relative coefficient cannot be absorbed into `nu`
because the constant term fixes `nu` while the quadratic term fixes
`nu lambda`. It survives every stated V002 regression, is covariant and
unit-correct, and changes the member-sensitive jets `(H5-C2)`.

This attack is not V002's gate-alternative row, stabilizer attack, hidden
scale attack, or implicit-unit attack. It is a new continuous freedom
inside the retained CK support class.

```text
FRESH_ATTACK_CK = KILL | missing lambda subfiber
H7_CK = KILL
```

## 10. Final determination and repair surface

The metric and unit repair is successful. Both displayed profiles have
correct jets, correct R4 routing, exact active finite zeros, and honest
cycle-creation scope. Shape K is a complete, neutrally presented DoR-018
candidate.

Shape CK is not complete. A bounded V003 repair must do one of two things:

```text
1. derive lambda=1 from a pre-existing carrier/divergence condition that
   does not mention the Hessian or response consequence; or

2. replace Shape CK by the complete lambda family, put lambda and its
   admissible domain on the DoR-018 choice table, rerun DP6/DP9, and carry
   the lambda-dependent jets and consequences without selecting a member.
```

No new carrier metric or unit field is needed. Until that bounded repair,
ratifying only K would silently resolve the commissioned two-shape fiber by
discarding an incompletely represented alternative.

```text
SHAPE_K = READY
SHAPE_CK = NOT_READY (H1,H4,H6,H7)
READY_FOR_DOR018_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
