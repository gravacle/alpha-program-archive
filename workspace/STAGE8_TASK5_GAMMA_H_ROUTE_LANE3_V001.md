# STAGE8 TASK 5 — THE GAMMA BUILD, H ROUTE
## Assembly first; four joints tested separately

Lane: CODEX LANE 3 (SOL, HIGH EFFORT)  
Version: V001  
Date: 2026-08-05  
Custody: builder artifact for Dario review  
Mode: symbolic only; no member selection, end test, fixed-point execution, or numerical evaluation

## 0. Preflight and determination discipline

[PROVABLE — access check] The register head is `Q-504` in
`QUESTIONS_SETTLED_REGISTER_V001.md`. The output artifact and its seal were absent in both the
Lane-3 workspace and the archive before this build.

[PROVABLE — law check] DoR-020-A8 was read in full and its byte hash verified:

```text
DOR_020_A8_GAMMA_BOTH_ROUTES_2026-08-05.md
SHA-256 = 0ee6c897055f803b31bc570b9f4ef852ccb3c4aba21fcd5274a7d740c8eb601d
```

It requires the H and HOL constructions to be carried in parallel, keeps both A7 branches,
and makes agreement a falsifier wherever both periods are actually formed. It does not license
an identification before formation.

[PROVABLE — review check] The controlling review and input audit were read and verified:

```text
STAGE8_TASK5_AUDIT_V002_REVIEW_DARIO_V001.md
SHA-256 = af955f8159e1cc4c464966d38070ddbda501828b39630a9f585e86ce7693e610

STAGE8_TASK5_CHAIN_CONFORMANCE_AUDIT_LANE3_V002.md
SHA-256 = 44202c060821728fba2c46b81b82487002e639f3242565b7a5fed387e41fcae8
```

The two review repairs are executed in section 7. In particular, this artifact does not consume
V002's weakened `(M9)` and does not book Q mode as a debt.

The gates remain

```text
alpha_computed = false;
proof_authorized = false;
kappa_record_computed = false.
```

No structural conclusion below is obtained from the false anchor

```text
pi_Mx compose Loc compose Kernbar compose Q = 1.
```

That equation is not consumed as a theorem.

## 1. Piece ledger — every piece before any joint

Fix an address `a=(w,N,gamma)`, its orientation reverse `a^-=(w,N,-gamma)`, a carried A7 label
`epsilon in {0,1}`, and, where needed, a return parameter `K`. “Specification seal” means that the cited sealed artifact states the
required type but does not provide an inhabited map. Such a row is not silently promoted to
stock.

### 1.1 Seal key

| Key | Sealed authority | SHA-256 |
|---|---|---|
| `A8` | `DOR_020_A8_GAMMA_BOTH_ROUTES_2026-08-05.md` | `0ee6c897055f803b31bc570b9f4ef852ccb3c4aba21fcd5274a7d740c8eb601d` |
| `A7` | `DOR_020_A7_EC_BRANCH_CARRIED_2026-08-05.md` | `834e46029a292122c1e4c604af4f3e3249e6a9ee2638255464685623fba5eb8f` |
| `MET` | `DOR_019_CARRIER_METRIC_AND_UNITS_RATIFICATION_2026-08-03.md` | `6ab72b0cb3a93e123eb1d3c5088fc83361d86c6dc739f0a886380dbd2d143f1f` |
| `AV2` | `STAGE8_TASK5_CHAIN_CONFORMANCE_AUDIT_LANE3_V002.md` | `44202c060821728fba2c46b81b82487002e639f3242565b7a5fed387e41fcae8` |
| `RV2` | `STAGE8_TASK5_AUDIT_V002_REVIEW_DARIO_V001.md` | `af955f8159e1cc4c464966d38070ddbda501828b39630a9f585e86ce7693e610` |
| `LOC` | `STAGE8_TASK5_EQ6_THE_LOC_BUILD_LANE3_V001.md` | `b53d9e931efe1ebde333ef49fb4243e41917bb5d467f5a86e7052102ae5a0310` |
| `LF2` | `STAGE8_TASK5_EQ6_LOC_FAMILY_V002_LANE3_V001.md` | `c4826773456c68972c1f70f5aea5a8ca8387b1b61c55923fd4f3902aaccf1b41` |
| `LF3` | `STAGE8_TASK5_EQ6_LOC_FAMILY_V003_AND_EC_LANE3_V001.md` | `258680c45cbec53ceceabca6d5b3e1a10f8ff4d2c9b8197bfb986c1f9a0cfb48` |
| `NAT` | `STAGE8_TASK5_EQ6_LOC_NATURALITY_LANE3_V001.md` | `474bf721517f77b240e2a215325a86227d4e0fd4934e89ba910d955627b5ab60` |
| `PROJ` | `STAGE8_TASK5_EQ6_PROJECTOR_CERT_V003_LANE1_V001.md` | `0bef9a003abb586666535689e98d7af29e7fc75b81e06fe439397ce2b8ef9100` |
| `TYPE` | `STAGE8_TASK5_EQ6_J7_FACE_AND_J2_DISPLAY_LANE3_V001.md` | `9c74ed3dbe748450e525102128b0367ce21c0e5029929eab33a111ca9802dc3c` |
| `AS3` | `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md` | `a46beae26048a0d093de339363fb8597d362a0101d103cfc06305edabac53f4c` |
| `AS4` | `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V004.md` | `9bf34e27da9aca51966feb2b41f34b0060e2121bd85d783d35a81685bbb63514` |
| `SYM` | `STAGE8_TASK5_R4_LOCAL_SYMBOL_MAP_BUILD_LANE1_V001.md` | `bae34116c4d6792b5e39b913addeeff1650989660d89ba01bf5de62ec2d9aa50` |
| `KER` | `STAGE8_TASK5_R4_KERNEL_REALIZATION_AND_SYMBOL_CALCULUS_LANE2_V001.md` | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` |
| `SCAL` | `STAGE8_TASK5_SCALAR_CARRIER_BUILD_AND_MODULUS_LANE1_V001.md` | `aebe708d2e7ba4b67e828976bd01eae2d5eec04afbb6a28f3f77f9dc8003fc97` |

### 1.2 Typed piece census

| No. | Piece and exact type | Carrier | Seal/status |
|---:|---|---|---|
| 1 | `E_N := R L_T,N direct-sum R Rhat_K,N direct-sum S_(1,sa)(K_N)` and `Q_N:E_N->O_prof,N:=E_N/Rel_N` | raw profile and quotient profile | `SYM`, refined by `LOC`; sealed source/quotient types |
| 2 | `E_N^cyc:={0} direct-sum R Rhat_K,N direct-sum S_(1,sa)(K_N)` and `O_N^cyc:=Q_N(E_N^cyc)` | cycle-only subsource and its quotient image | `LOC`; sealed scope correction |
| 3 | `Kernbar_N^cyc:O_N^cyc->Ker_N^Q408` | Q-408 path-bilocal kernel carrier | `KER`,`LOC`; sealed only on the cycle scope |
| 4 | `iota_N^Q408:Ker_N^Q408->D_N^ker` | one proposed common topological kernel carrier | `LOC` specification; no construction seal |
| 5 | `M_N^loc:=delta_(g,N)d:Omega^1(M_N;ad P_N)->Omega^1(M_N;ad P_N)`, with `M_N^loc in Op_N^(loc,2)` | local second-order operator carrier | `LOC`; operator typed, common kernel realization not built |
| 6 | `Sch_N:Op_N^(loc,2)->D_N^ker` | Schwartz-kernel realization into the same `D_N^ker` | `LOC` specification; no construction seal |
| 7 | `Krawhat_N:E_N->D_N^ker` and `kappa_T,N:=Krawhat_N(L_T,N)=Sch_N(M_N^loc)` | raw profile to common physical kernel; Maxwell direction in its range | `LOC`,`LF2`,`LF3` specification; no family member sealed |
| 8 | `D_N^Loc:=Krawhat_N(E_N) subset D_N^ker` and `Kernbarhat_N:O_prof,N->D_N^Loc`, `Kernbarhat_N(Q_Nz):=Krawhat_N(z)` | physical localization domain | `LOC` specification, conditional on `Rel_N subset ker(Krawhat_N)`; no inhabitant |
| 9 | `Res_a^resp:O_w^resp->O_a^resp`, `Y_(a,epsilon)^H(K) in O_a^resp`, and `Rhat_(Kcycle,a):=Res_a^resp(Rhat_(Kcycle,w)) in O_a^resp` with required `Rhat_(Kcycle,a)!=0` | addressed response carrier and response-line direction | `AV2`,`RV2` specification; addressed restriction/nonzero-line certificate unbuilt |
| 10 | `Ker_(a,K):O_a^resp->D_N^Loc` | response-to-physical-kernel leg | `AV2`,`RV2` specification; no definition or image certificate sealed |
| 11 | `Sym_N^loc:=Sigma_N^(2),Ward/Ctc_N^sym` | local Ward-symbol quotient | `LOC`; target carrier specified |
| 12 | `sigma_2^op:Op_N^(loc,2)->Sigma_N^(2),Ward` and `sigma_2^ker:Sch_N(Op_N^(loc,2))->Sigma_N^(2),Ward` | operator/kernel principal-symbol carrier | `LOC` specification; the required Q-408-domain inclusion is unproved |
| 13 | `C3_N^fin=(Ward_N^fin,sigma_N^fin)` | finite shadow datum | `LOC`; sealed datum component, explicitly not a kernel map |
| 14 | `Loc_N^phys:D_N^Loc->Sym_N^loc` | physical symbol localization | `LOC`,`LF2`,`LF3` candidate-family coordinate; no member sealed |
| 15 | `iota_N^H:Sym_N^loc->C_N^k` | symbol-to-finite-Hodge-cochain realization | `LOC`,`LF2`,`LF3` candidate-family coordinate; no member sealed |
| 16 | `Loc_N^C:=iota_N^H compose Loc_N^phys:D_N^Loc->C_N^k` | cochain-valued physical localization | `LOC` exact definition; uninhabited because pieces 14–15 are uninhabited |
| 17 | `d_N^r:C_N^r->C_N^(r+1)`, `delta_N^(r+1):C_N^(r+1)->C_N^r`, `Delta_N=d_N delta_N+delta_N d_N` | finite Hodge cochain complex | `MET`,`PROJ`; sealed fixed-stage machinery |
| 18 | `P_H,N:=1_0(Delta_N):C_N^k->C_N^k` and `H_N^k:=im(P_H,N)` | harmonic line/subspace in the cochain carrier | `PROJ`; sealed projector |
| 19 | `E_C,N:C_N^k->C_N^k`, `[E_C,N,Delta_N]=0`, with `E_C,RL c_RL=epsilon c_RL` on the carried branch | contact projector on the Hodge carrier | `A7`,`LF3`; both `epsilon=0,1` carried, none selected |
| 20 | `Gamma_(a,epsilon,K)^H:=Loc_N^C compose Ker_(a,K):O_a^resp->C_N^k` | addressed response to Hodge cochain | `AV2` specification; no construction seal |
| 21 | `lambda_x:H_N^k->ChargeUnit_N`, `lambda_x(h):=<x,h>_N` | dual harmonic functional induced by the ratified metric | `MET`,`AV2`; formula specified once `x` exists |
| 22 | `c_(N,gamma) in H_N^k` and `ev_(N,gamma):(H_N^k)^*->ChargeUnit_N`, `ev_(N,gamma)(lambda):=lambda(c_(N,gamma))` | fixed primitive harmonic representative and evaluation | `AV2`; evaluation formula specified; orientation law required |
| 23 | `Per_(a,epsilon,K)^H:O_a^resp->(H_N^k)^*`, `Per(Y):=lambda_(P_H,N Gamma^H(Y))` | global harmonic-period functional | `AV2`; subject unformed until piece 20 exists |
| 24 | `K_amb:=Scalar_dimless^real isomorphic to R` | dimensionless real scalar carrier | `SCAL`; sealed carrier |
| 25 | `U_a^H:ChargeUnit_N->K_amb` and `u_a^H:=U_a^H compose ev_(N,gamma):(H_N^k)^*->K_amb` | unit/orientation seam to scalar carrier | `AV2`,`RV2` specification; no lawful map member sealed |
| 26 | `p_Mx,N^sym:Sym_N^loc->R` and `p_Mx,N^sym compose Loc_N^phys:D_N^Loc->R` | physical-symbol scalar coordinate | `LOC`; candidate physical face, not a bottom map |
| 27 | `pi_N^resp:P_N->Bot_N^resp` | package-to-response-bottom projection | `TYPE`; sealed, but no global `C_N^k->P_N` input arrow is supplied |
| 28 | `J_(N|f)^bot:D_f^old->Bot_N^resp` and `r_f^Bot:Bot_M^resp->Bot_N^resp` | arrow-restricted old-image response bottom | `TYPE`,`AS3`,`AS4`; sealed only on its displayed restricted domain; no `Bot->R` map |
| 29 | `etahat_f:D_N^Loc->D_M^Loc`, `j_f^Sym:Sym_N^loc->Sym_M^loc`, `j_f^C:C_N^k->C_M^k`, and `rho_f^C:=(j_f^C)^*:C_M^k->C_N^k` | rank-preserving transports | `LOC`,`NAT`,`PROJ`; Hodge transport/intertwiners sealed, physical `etahat/j^Sym` squares only family clauses |
| 30 | `j_f^E:E_N->E_M`, `j_f^prof:O_prof,N->O_prof,M`, and represented `eta_f^K:Ker_N^Q408->Ker_M^Q408` | raw/quotient/represented-kernel transport | `NAT`,`AS3`,`AS4`; represented transport sealed, generic quotient descent not sealed |

The ledger has thirty pieces. The finite datum `sigma_N^fin` is listed because it is the tempting
look-alike at Joint II; its lack of a kernel-map type is itself load-bearing. The A8 agreement
falsifier is law, not a thirty-first map: it becomes applicable only after H and HOL yield periods
on a common formed cell.

## 2. Joint I — kernel-side domain assembly

### 2.1 The only lawful single-map formula

[PART-PROVABLE — conditional display] Let

```text
z=(a,b,C)=a L_T,N+(0,b,C) in E_N.
```

If pieces 4–7 are supplied as one future full-gate member, the single raw map must be

```text
Krawhat_N^pre(z)
 :=a Sch_N(M_N^loc)
   +iota_N^Q408 Kernbar_N^cyc(Q_N(0,b,C))
 :E_N->D_N^ker.                                  (JI-1)
```

This is a sum of two images in the same named carrier; it is not a juxtaposition of summands and
does not assert that the two images intersect trivially. Its two restrictions are displayed:

```text
Krawhat_N^pre(L_T,N)
 =Sch_N(M_N^loc)
 =kappa_T,N,                                     (JI-2)

Krawhat_N^pre(0,b,C)
 =iota_N^Q408 Kernbar_N^cyc(Q_N(0,b,C)).         (JI-3)
```

The quotient descent is not a naming convention. If `Q_Nz=Q_Nz'`, then a future member must prove

```text
Q_Nz=Q_Nz'
 =>z-z' in Rel_N
 =>Krawhat_N^pre(z-z')=0
 =>Krawhat_N^pre(z)=Krawhat_N^pre(z').           (JI-4)
```

The middle implication in `(JI-4)` is exactly

```text
Rel_N subset ker(Krawhat_N^pre).                 (JI-5)
```

Only under `(JI-5)` does the following definition exist:

```text
Kernbarhat_N(Q_Nz):=Krawhat_N^pre(z)
 :O_prof,N->D_N^Loc.                             (JI-6)
```

Then every intermediate equality carrying the local direction is

```text
Kernbarhat_N(Q_N(a,b,C))
 =Krawhat_N^pre(a,b,C)
 =a Krawhat_N^pre(L_T,N)+Krawhat_N^pre(0,b,C)
 =a kappa_T,N
   +iota_N^Q408 Kernbar_N^cyc(Q_N(0,b,C)),       (JI-7)

Kernbarhat_N(Q_N(L_T,N))
 =Krawhat_N^pre(L_T,N)
 =kappa_T,N
 =Sch_N(M_N^loc).                                (JI-8)
```

### 2.2 Exact stop

[YOURS — determination] No sealed member supplies the common `D_N^ker`, `iota_N^Q408`, `Sch_N`,
`Krawhat_N^pre`, or `(JI-5)`. The old Physical-J2 all-profile `Kernbar` assertion is not consumed:
the later `KER/LOC` scope correction leaves only `Kernbar_N^cyc` sealed.

Even if `(JI-6)` were inhabited, its domain would be `O_prof,N`, while the route demands

```text
Ker_(a,K):O_a^resp->D_N^Loc.                     (JI-9)
```

No sealed arrow `O_a^resp->O_prof,N`, and no independent definition of `(JI-9)` with certified
image in `D_N^Loc`, exists. The represented assembly transports already represented Q-408 images;
it does not supply either missing bridge.

```text
MACHINERY-APPEAL(JI)
 =source extension/common-kernel realization
  +quotient descent
  +addressed response-to-profile (or response-to-DLoc) bridge.
```

**Joint I is STOPPED.** Equations `(JI-1)`–`(JI-8)` are the conditional contract, not an
inhabited composite.

## 3. Joint II — landing on the Hodge carrier

### 3.1 Finite shadow is not physical localization

[PROVABLE] The sealed finite item is only

```text
C3_N^fin=(Ward_N^fin,sigma_N^fin).               (JII-1)
```

There is no sealed domain/codomain declaration making `sigma_N^fin` a map out of
`Ker_N^Q408` or `D_N^Loc`. Therefore neither `sigma_N^fin(K)` nor
`P_H,N sigma_N^fin(K)` is formed here.

### 3.2 The physical attempted landing

[PART-PROVABLE — conditional display] A future source member whose image lies in the admitted
symbol-calculus domain would have to define

```text
Loc_N^phys(K)
 :=[sigma_2^ker(K)]_(Ctc_N^sym)
 in Sym_N^loc,                                   (JII-2)

iota_N^H:Sym_N^loc->C_N^k,                      (JII-3)

Loc_N^C(K)
 :=iota_N^H(Loc_N^phys(K))
 =iota_N^H([sigma_2^ker(K)]_(Ctc_N^sym))
 in C_N^k,                                      (JII-4)

P_H,N Loc_N^C(K)
 =P_H,N iota_N^H([sigma_2^ker(K)]_(Ctc_N^sym))
 in H_N^k.                                      (JII-5)
```

The stock proves `P_H,N:C_N^k->C_N^k`, but it does not prove

```text
D_N^Loc subset Sch_N(Op_N^(loc,2)),              (JII-6)
```

does not build `(JII-2)` on Q-408 kernels, and does not build the separate symbol-to-cochain map
`(JII-3)`. Hodge theory begins after a cochain exists; it cannot manufacture `(JII-3)`.

### 3.3 Both A7 branches, without selection

[PART-PROVABLE — consequence of a future family member] The honest Loc-family clause requires

```text
E_C,N Loc_N^C(K)=0,
[E_C,N,P_H,N]=0.                                 (JII-7)
```

Thus, if `(JII-4)` is someday inhabited,

```text
E_C,N P_H,N Loc_N^C(K)
 =P_H,N E_C,N Loc_N^C(K)
 =P_H,N 0
 =0,

P_H,N Loc_N^C(K)
 in im(P_H,N) intersection ker(E_C,N).           (JII-8)
```

At the reciprocal stage, `im(P_H,RL)=span{c_RL}`. Therefore the two carried cases are

```text
epsilon=1:
 E_C,RL c_RL=c_RL
 =>span{c_RL} intersection ker(E_C,RL)={0}
 =>P_H,RL Loc_RL^C(K)=0;                        (JII-9)

epsilon=0:
 E_C,RL c_RL=0
 =>span{c_RL} subset ker(E_C,RL),
```

and the last line does not decide whether `P_H,RL Loc_RL^C(K)` is zero. Neither branch creates
`Loc_N^phys` or `iota_N^H`.

```text
MACHINERY-APPEAL(JII)
 =physical principal-symbol domain/member
  +reader-free symbol-to-cochain realization.
```

**Joint II is STOPPED.** The exact type path is displayed, but its first two physical arrows are
not sealed inhabitants.

## 4. Joint III — codomain reconciliation and the scalar/bottom seam

### 4.1 The lawful evaluation interface

[PART-PROVABLE — conditional on a formed Hodge response] For `x in H_N^k`, define

```text
lambda_x:H_N^k->ChargeUnit_N,
lambda_x(h):=<x,h>_N.                            (JIII-1)
```

Once `Gamma^H` exists, the period-side equalities would be

```text
x_(a,epsilon,K)(Y)
 :=P_H,N Gamma_(a,epsilon,K)^H(Y),               (JIII-2)

Per_(a,epsilon,K)^H(Y)
 :=lambda_(x_(a,epsilon,K)(Y)),                  (JIII-3)

ev_(N,gamma)(Per_(a,epsilon,K)^H(Y))
 =Per_(a,epsilon,K)^H(Y)(c_(N,gamma))
 =lambda_(x_(a,epsilon,K)(Y))(c_(N,gamma))
 =<P_H,N Gamma_(a,epsilon,K)^H(Y),
    c_(N,gamma)>_N
 in ChargeUnit_N.                                (JIII-4)
```

Thus `ev_(N,gamma):(H_N^k)^*->ChargeUnit_N` is a lawful evaluation formula once its input is
formed. It does not by itself land in `K_amb`.

The remaining seam must be an independently fixed linear, continuous, unit-compatible map

```text
U_a^H:ChargeUnit_N->K_amb,                       (JIII-5)

u_a^H
 :=U_a^H compose ev_(N,gamma)
 :(H_N^k)^*->K_amb.                              (JIII-6)
```

The required orientation display is

```text
c_(N,-gamma)=-c_(N,gamma)
 =>ev_(N,-gamma)=-ev_(N,gamma),                  (JIII-7)

U_(a^-)^H=-U_a^H
 =>u_(a^-)^H
   =U_(a^-)^H compose ev_(N,-gamma)
   =(-U_a^H) compose (-ev_(N,gamma))
   =U_a^H compose ev_(N,gamma)
   =u_a^H.                                       (JIII-8)
```

`K_amb` is sealed, but no sealed law or metric identity determines a member of `(JIII-5)`.
Choosing one merely because the codomain is real would be an invented cross-sector arrow.

### 4.2 The bottom carrier stays separate

[PROVABLE — typing boundary] The following arrows are not identified or silently composed:

```text
p_Mx,N^sym compose Loc_N^phys:D_N^Loc->R,        (JIII-9)

pi_N^resp:P_N->Bot_N^resp,                       (JIII-10)

C_N^k -/-> P_N,                                 (JIII-10a)

J_(N|f)^bot:D_f^old->Bot_N^resp.                (JIII-11)
```

The barred arrow in `(JIII-10a)` records absence, not a zero map. Thus the legacy string
`pi_N^resp P_H,N Loc_N^C` is not a global factorization; the sealed object is the already-bundled,
arrow-restricted map `(JIII-11)`. There is also no sealed `Bot_N^resp->R` or
`Bot_N^resp->ChargeUnit_N`. Consequently `U^H` cannot be obtained by re-reading a bottom leg, and
the old scalar/bottom overload is not revived.

```text
MACHINERY-APPEAL(JIII)
 =independently fixed ChargeUnit-to-Kamb map
  +its orientation/unit/continuity certificate.
```

**Joint III is STOPPED.** Evaluation is displayed through `ChargeUnit_N`; the final lawful scalar
conversion has no sealed inhabitant.

## 5. Joint IV — naturality beyond identities

Fix a rank-preserving `f:N->M`. The physical square needed by the H route is

```text
Loc_M^C compose etahat_f
 =j_f^C compose Loc_N^C
 :D_N^Loc->C_M^k.                               (JIV-1)
```

Using `Loc^C=iota^H compose Loc^phys`, every step that would establish `(JIV-1)` is

```text
Loc_M^C etahat_f
 =iota_M^H Loc_M^phys etahat_f
 ?=iota_M^H j_f^Sym Loc_N^phys
 ?=j_f^C iota_N^H Loc_N^phys
 =j_f^C Loc_N^C.                                (JIV-2)
```

The first question mark is the uninstantiated family clause `(S24)`; the second is `(S25)`.
Projector naturality

```text
P_H,M j_f^C=j_f^C P_H,N                         (JIV-3)
```

is sealed, but it operates only after `(JIV-2)` has landed a cochain.

### 5.1 Reciprocal-loop generator

Let `u:N->M` be the actual reciprocal rank-preserving generator and let
`K_N^Q(H):=Kernbar_N^cyc(H)` be in represented Q-408 scope. The assembly supplies

```text
eta_u^K(K_N^Q(H))
 =Kernbar_M^cyc(j_u^prof(H)).                    (JIV-RL-1)
```

A future Joint-I source member would separately form the physical-domain elements

```text
K_N^D(H)
 :=iota_N^Q408(K_N^Q(H)) in D_N^Loc,

K_M^D(j_u^prof H)
 :=iota_M^Q408(Kernbar_M^cyc(j_u^prof H))
 in D_M^Loc.                                    (JIV-RL-2)
```

The represented equality `(JIV-RL-1)` does not itself prove compatibility with the physical
transport. That missing display is

```text
etahat_u(K_N^D(H))
 ?=iota_M^Q408 eta_u^K(K_N^Q(H))
 =iota_M^Q408 Kernbar_M^cyc(j_u^prof H)
 =K_M^D(j_u^prof H).                            (JIV-RL-3)
```

Only after `(JIV-RL-3)` is supplied does the requested Loc display reach its own gap:

```text
Loc_M^C etahat_u(K_N^D(H))
 ?=Loc_M^C(K_M^D(j_u^prof H))
 ?=j_u^C Loc_N^C(K_N^D(H)).                     (JIV-RL-4)
```

The `(F1)` quotient companion reaches a separate gap:

```text
Q_M j_u^E(z)
 =[j_u^E(z)]_(Rel_M)
 ?=j_u^prof([z]_(Rel_N))
 =j_u^prof Q_N(z).                               (JIV-RL-5)
```

The middle equality needs

```text
j_u^E(Rel_N) subset Rel_M,
bar(j_u^E)=j_u^prof.                             (JIV-RL-6)
```

`(F1)` is proven on the separately certified linear `A_iso` subscope; stock does not show that
the generic actual reciprocal generator used here is wholly in that subscope. Even an
`A_iso` certificate would not close `(JIV-RL-3)` or `(JIV-RL-4)`.

### 5.2 One nontrivial refinement generator

For the actual `q=2` refinement `s_nm:n->m`, the represented kernel square is

```text
eta_nm^K(Kernbar_n^cyc(H))
 =Kernbar_m^cyc(j_nm^prof(H)).                   (JIV-RF-1)
```

A future Joint-I source member would form

```text
K_n^D(H):=iota_n^Q408 Kernbar_n^cyc(H) in D_n^Loc,

K_m^D(j_nm^prof H)
 :=iota_m^Q408 Kernbar_m^cyc(j_nm^prof H)
 in D_m^Loc.                                    (JIV-RF-2)
```

The two independent missing equalities are then displayed:

```text
etahat_nm(K_n^D(H))
 ?=iota_m^Q408 eta_nm^K(Kernbar_n^cyc(H))
 =iota_m^Q408 Kernbar_m^cyc(j_nm^prof H)
 =K_m^D(j_nm^prof H),                           (JIV-RF-3)

Loc_m^C etahat_nm(K_n^D(H))
 ?=Loc_m^C(K_m^D(j_nm^prof H))
 ?=j_nm^C Loc_n^C(K_n^D(H)).                    (JIV-RF-4)
```

The named rank-one zero relation `r_x=(0,-t,P_x)` is preserved, so for that relation alone

```text
r_x in Rel_n
 =>j_nm^E(r_x) in Rel_m
 =>Q_m j_nm^E(r_x)=0
 =j_nm^prof Q_n(r_x).                            (JIV-RF-5)
```

But `(JIV-RF-5)` does not prove the general companion. For every `z`, the needed equality is

```text
Q_m j_nm^E(z)
 =[j_nm^E(z)]_(Rel_m)
 ?=j_nm^prof([z]_(Rel_n))
 =j_nm^prof Q_n(z),                              (JIV-RF-6)
```

which still requires `j_nm^E(Rel_n) subset Rel_m` and identification of the descended map with
`j_nm^prof`.

### 5.3 Displayed induction and why it cannot start

[PART-PROVABLE — conditional induction] If two composable generators `f:N->M` and `g:M->P`
satisfied `(JIV-1)`, then

```text
Loc_P^C etahat_(g compose f)
 =Loc_P^C etahat_g etahat_f
 =j_g^C Loc_M^C etahat_f
 =j_g^C j_f^C Loc_N^C
 =j_(g compose f)^C Loc_N^C.                    (JIV-I-1)
```

Likewise, if their quotient base squares held,

```text
Q_P j_(g compose f)^E
 =Q_P j_g^E j_f^E
 =j_g^prof Q_M j_f^E
 =j_g^prof j_f^prof Q_N
 =j_(g compose f)^prof Q_N.                     (JIV-I-2)
```

Equations `(JIV-I-1)`–`(JIV-I-2)` give word induction after generator base cases; they do not
manufacture either base case. The reciprocal generator stops on `(JIV-RL-3)`, `(JIV-RL-4)`, and
generic `(JIV-RL-5)`. The refinement generator stops on `(JIV-RF-3)`, `(JIV-RF-4)`, and
`(JIV-RF-6)`.

```text
MACHINERY-APPEAL(JIV)
 =physical-embedding/transport compatibility
  +inhabited S24/S25 naturality base squares
  +generic quotient-relation descent/identification.
```

**Joint IV is STOPPED.** For any future typed physical member, the identity equation is
tautological; there is presently no inhabited physical F3 square, and the two requested
nonidentity base cases are not supplied.

## 6. Assembly and consequence board

### 6.1 End-to-end type and assembly verdict

The end-to-end H specification is

```text
O_a^resp
 --Ker_(a,K)-->D_N^Loc
 --Loc_N^phys-->Sym_N^loc
 --iota_N^H-->C_N^k
 --P_H,N-->H_N^k
 --(x maps to lambda_x)-->(H_N^k)^*
 --ev_(N,gamma)-->ChargeUnit_N
 --U_a^H-->K_amb.                               (G-1)
```

The proposed cochain realization would be

```text
Gamma_(a,epsilon,K)^H
 :=Loc_N^C compose Ker_(a,K)
 =iota_N^H compose Loc_N^phys compose Ker_(a,K)
 :O_a^resp->C_N^k.                              (G-2)
```

Because Joints I and II are stopped, `(G-2)` is an uninhabited specification, not an assembled
map. Accordingly, the reciprocal period and coefficient subjects remain unformed:

```text
Per_(a,epsilon,K)^H(Rhat_(Kcycle,a))
 :=lambda_(P_H,N Gamma_(a,epsilon,K)^H(
             Rhat_(Kcycle,a)))                  (G-3: UNFORMED),

chi_(a,epsilon,K)^per,H
 :=U_a^H(
     ev_(N,gamma)(
      Per_(a,epsilon,K)^H(Rhat_(Kcycle,a))))     (G-4: UNFORMED).
```

The `K` index in `(G-4)` is mandatory before a fixed-factor certificate. That certificate would
have to set `L_a^resp:=span{Rhat_(Kcycle,a)}` and exhibit one fixed linear map

```text
F_(a,epsilon)^H:L_a^resp->K_amb
```

such that, for every admitted `K`,

```text
(u_a^H compose Per_(a,epsilon,K)^H)|_(L_a^resp)
 =F_(a,epsilon)^H,                               (G-4a)

chi_(a,epsilon,K)^per,H
 =F_(a,epsilon)^H(Rhat_(Kcycle,a))
 =chi_(a,epsilon,K')^per,H.                     (G-4b)
```

Only after `(G-4a)`–`(G-4b)` may the common value be named
`chi_(a,epsilon)^per,H`. No evaluation of `(G-3)` or `(G-4)` is made. Joint III independently shows that even a formed
`(G-3)` would still lack the sealed `U^H` seam. Joint IV independently shows that naturality could
not yet be exported to any inhabited naturality square.

The A7 implications remain branch-carried conditional facts, pointwise for every admitted `K`
and `Y`:

```text
epsilon=1 and a future H-route member
 =>P_H,RL Gamma_(a,1,K)^H(Y)=0;

epsilon=0 and a future H-route member
 =>P_H,RL Gamma_(a,0,K)^H(Y) lies in span{c_RL},
   with zero/nonzero undetermined.               (G-5)
```

No branch is selected. Since the H period is not formed, A8's H/HOL identification falsifier is
not yet triggered and no HOL value is imported.

### 6.2 What review relays R4–R8 can run

| Review relay | Status after this build | Exact reason |
|---|---|---|
| `R4 — FIXED_PERIOD_FACTOR_CERT` | cannot run | `Gamma^H`, `Per^H`, the addressed nonzero response line, and `u^H` are unformed |
| `R5 — PERIOD_MODULUS_COMPATIBILITY_CERT / (M5)` | Q mode is vacuous under `(M2)`; FACTOR mode cannot run | the review repair removes Q-mode debt, while factor mode needs the unformed fixed coefficient and response-line secant |
| `R6 — Steps 4/5 reissue` | cannot run | no branchwise scalar self-map `B^(per,H)` or certified scalar return domain exists |
| `R7 — Step-10 lattice transfer` | cannot run as a theorem | only the conditional A7 identity-branch zero display survives; no formed carrier/map/certificates support transfer |
| `R8 — residues and witness boundary` | can run only as bookkeeping | retain residues `3/6/9/12`, attach the four joint gaps, and stop before witness certification |

### 6.3 Seed and membership consequences

The seed subject is still not well posed as an inhabited term:

```text
P_H,N iota_N^H Loc_N^phys(kappa_T,N)             (G-6)
```

because `kappa_T,N`, `Loc_N^phys`, and `iota_N^H` all lack a common sealed member. No assertion
about the value or nonvanishing of `(G-6)` is made.

The rank-preserving J2 premise board is therefore unchanged:

| Premise | Status |
|---|---|
| `(F1)` quotient/profile square | proved on linear `A_iso`; generic reciprocal/refinement relation descent and descended-map identification remain open |
| `(F2)` represented-kernel transport | proved on the sealed cycle-profile/Q-408 represented scope; no `L_T` extension |
| `(F3)` physical Loc naturality | no inhabited square; the identity equation is conditionally tautological for a future typed member, while reciprocal and refinement base squares stop in section 5 |
| `(F4)` Hodge/projector square | proved on rank-preserving scope |
| scalar/bottom reconciliation | no global seam; restricted bottom law remains distinct from scalar and period outputs |

Thus neither `A_RP^+` inhabitance nor the coefficient face's physical inhabitance basis is supplied
by this artifact.

## 7. Mandated audit repairs

### 7.1 Repair 1 — `(M9)` carries collinearity and the metric identity

[YOURS — repaired certificate text] Fix one formed route/branch hypothetically **and** suppose its
`FIXED_PERIOD_FACTOR_CERT` has supplied the K-independent common value in `(G-4b)`. Only under that
explicit premise abbreviate

```text
D:=D_(a,epsilon)^(per,H),
B:=B_(a,epsilon)^(per,H),
d:=d_(a,epsilon)^(per,H),
chi:=chi_(a,epsilon)^(per,H),
Rhat:=Rhat_(Kcycle,a) !=0.
```

The direct factor certificate must require one and the same coefficient

```text
a_sec:{(K,K') in D x D:K!=K'}->K_amb            (AR-1)
```

to satisfy both displays, for every `K!=K'`:

```text
Y_(a,epsilon)^per,H(K)-Y_(a,epsilon)^per,H(K')
 =a_sec(K,K') d(K,K') Rhat,                     (AR-2)

d(B(K),B(K'))
 =|chi| |a_sec(K,K')| d(K,K').                  (AR-3)
```

`(AR-2)` is the same addressed response-line collinearity condition; `(AR-3)` is the identity in
Banach's actual period metric. Neither may replace the other. Only after both hold may one set

```text
A_loop:=sup_(K!=K') |a_sec(K,K')|,
q_loop=|chi| A_loop,                             (AR-4)
```

with the separately stated zero-times-infinity convention. When `chi=0`, `(AR-3)` requires the
return to be `d`-constant; division by `chi` is not used. This repairs the existentially trivial
V002 form.

### 7.2 Repair 2 — Q mode is not a debt

[PROVABLE — review correction adopted] In direct Q mode,

```text
q_loop
 :=sup_(K!=K' in D)
    d(B(K),B(K'))/d(K,K')                       (AR-5)
```

uses Banach's own metric by definition. Therefore

```text
PERIOD_MODULUS_COMPATIBILITY_CERT[a,epsilon,H;Q]
 =VACUOUS_UNDER_M2.                              (AR-6)
```

It is neither an additional hypothesis nor a residue. Only

```text
PERIOD_MODULUS_COMPATIBILITY_CERT[a,epsilon,H;FACTOR]
```

remains a live Step-9 debt, and it is unavailable here because `(AR-1)`–`(AR-3)` have no formed
H-route subjects.

## 8. Battery

### 8.1 F_PLDEC and false-anchor audit

The dependency path attempted here is

```text
surface/bundle/Hodge stock
 ->cycle-profile kernel plus independent L_T realization
 ->physical Loc
 ->Hodge projector
 ->harmonic evaluation
 ->independent unit seam.
```

No algebraic reader, `chi_K`, threshold, response result, fixed-point root, desired coupling,
or false-anchor equality constructs a piece. `p_Mx`, the bottom leg, and `U^H` are kept as three
different types. `F_PLDEC = CLEAN`.

### 8.2 Anti-tuning ledger

| Check | Result |
|---|---|
| No A7 branch selected to obtain a preferred period | clean; both labels carried |
| No Loc-family member selected | clean; no member exists in sealed stock |
| No `sigma_N^fin` look-alike promoted to physical Loc | clean |
| No `Bot->R`, `Bot->ChargeUnit`, or `ChargeUnit->K_amb` arrow invented | clean |
| No HOL construction imported to fill an H-route gap | clean |
| No A8 equality assumed before both periods form | clean |
| No nonzero seed or coefficient assumed | clean |
| No number, magnitude, measured constant, end test, or fixed point evaluated | clean |
| No conclusion selected from a desired downstream numeric consequence | clean |

### 8.3 Self verb audit

| Verb used | Display/control |
|---|---|
| `verified` | file bytes were hash-checked in section 0 and the no-clobber check was run before writing |
| `sealed/proved` | reserved for the cited Q-408 scoped kernel, finite Hodge projector/intertwiners, A7 law, and restricted assembly maps |
| `defined` | used only for sealed definitions or explicitly conditional future-member formulas |
| `displayed` | means all intermediate equalities are written; it does not claim inhabitance |
| `stopped` | followed by the exact missing map, descent, or base square in sections 2–5 |
| `assembled` | not used affirmatively for `Gamma^H`; `(G-2)` is explicitly uninhabited |
| `formed` | denied for the reciprocal period, coefficient, seed, and scalar return |

The audit finds no verb that outruns its displayed antecedent.

PIECES = listed (+30)
JOINT_I = STOPPED (+no inhabited source-extension/quotient-descent package; no O_resp->O_prof or response-to-DLoc bridge)
JOINT_II = STOPPED (+physical Loc and symbol-to-cochain realization have no sealed member; sigma_fin is not the arrow)
JOINT_III = STOPPED (+evaluation reaches ChargeUnit, but no sealed orientation/unit map ChargeUnit->K_amb exists; bottom remains separate)
JOINT_IV = STOPPED (+etahat_f iota_N^Q408 = iota_M^Q408 eta_f^K and reciprocal/refinement Loc base squares are unproved; generic F1 descent also remains open)
GAMMA_H = PARTIAL (+all four conditional joint specifications displayed; joints I/II/III/IV stopped)
AUDIT_REPAIRS = DONE
VERB_AUDIT_SELF = CLEAN
