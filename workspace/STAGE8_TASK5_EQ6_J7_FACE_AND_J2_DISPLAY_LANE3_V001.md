# STAGE 8 / TASK 5 / EQ6 — J7 COEFFICIENT FACE AND J2 DISPLAY

Lane: **Codex Lane 3**  
Version: **V001**  
Date: **2026-08-05**  
Register head checked before construction: **Q-488**

This is a Lane 3 repair artifact. Every Lane 2 artifact cited below is a
hash-verified input; no Lane 2 custody or authorship is asserted here. This
artifact addresses only the three mathematical items in Dario review section
7.1--7.3. It does not assert the membership theorem, repair the omitted
consumer-arrow class, enlarge the proved FC6 scope, or discharge the remaining
exhibition and provenance items.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_binding = none
fixed_point_execution = none
end_test = none
numeric_evaluation = none
measured_constant_comparison = none
MACHINERY_APPEAL = false
```

## 0. Preflight and sealed inputs

The corrected Lane 3 output name was absent in both the cleanroom and the
archive workspace before this file was written. The review and the three
named inputs match the requested digests:

| Input | Verified SHA-256 | Use here |
|---|---|---|
| `STAGE8_TASK5_EQ6_MEMBERSHIP_REVIEW_DARIO_V001.md` | `9caef0f7fa23b7f77fd2dfa27e003b706b3572419480e6333e8b851cfcfe2906` | D2, D3, and section 7 items 1--3 |
| `STAGE8_TASK5_EQ6_J2_BUILD_LANE2_V001.md` | `7c52c1a8d4e1158097cb6e6ea8cdbb921ff45c78764ae38e1a19c958445748f6` | line-69 typing defect and line-79 display debt |
| `STAGE8_TASK5_EQ6_PARTIAL_JOINT_DIAMONDS_LANE2_V001.md` | `5539b53ddeb208638af314f34e018591e1e6bd93403906e6a5edd46bc34e4766` | D2 item 2, the actual J7 coefficient contract |
| `STAGE8_TASK5_EQ6_PROJECTOR_CERT_V003_LANE1_V001.md` | `0bef9a003abb586666535689e98d7af29e7fc75b81e06fe439397ce2b8ef9100` | rank-preserving intertwiners and branch boundary |

The supporting sealed stock used in the displayed calculations is:

| Input | Verified SHA-256 | Exact content consumed |
|---|---|---|
| `STAGE8_TASK5_EQ6_PHYSICAL_J2_LANE2_V001.md` | `3fd4b924ec1a70f3e730bcf99f406d697c53937b26467d2ae6d5aa8c1bb6822c` | profile quotient, coefficient extraction, rank-one and `Delta B_i` formulas |
| `STAGE8_TASK5_EQ6_MAXWELL_HODGE_PROJECTOR_CERT_LANE2_V001.md` | `f074ca24e8b96c576f5c64b856377f39ed8d4fc729c02cbf591326322558f816` | `Loc_N^fin`, `m_T,N`, and scalar normalization on `m_T,N != 0` |
| `STAGE8_TASK5_EQ6_PROJECTOR_LOCALITY_REDUCING_CERT_V002_LANE1_V001.md` | `c81f61c4921275f1e38edd1c48c698788523e5f3ab5960b611b106dc2b66d837` | typed projector comparison and projected bottom mate |
| `STAGE8_TASK5_CONTINUUM_PACKAGE_CONSTRAINT_ARM_LANE1_V001.md` | `d7dcbc3ad7c470c8aaf0d8407db625d3e910cf180cd7b035fbc96bdfe58471b4` | coefficient covariance |
| `STAGE8_TASK4B_LOCAL_MAXWELL_SYMBOL_AND_PLOC_RK_LANE2_V001.md` | `70dde1c0cb776abec4a61cac118d4edf1f4c75a1185a2e984dc341961d4b643c` | local rank-one symbol |
| `STAGE8_TASK4B_REPRESENTATIVE_INDEPENDENCE_LANE1_V001.md` | `f0f8b09b1aa6a16c0ed0dffedbd275aba9e647fb5841fc8ce06ce9e6a8b00857` | `H_mix` and `Delta B_i` representatives |
| `STAGE8_TASK5_CONTINUUM_PACKAGE_ADOPTION_PROPOSAL_LANE2_V004.md` | `fa73114214d7653d9a5d181a684b3bd65f0d6e9f91fd2256fb159ca97e56c4bf` | explicit nonidentity `Ref_path` subdivision |
| `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md` | `a46beae26048a0d093de339363fb8597d362a0101d103cfc06305edabac53f4c` | response-bottom type and old-image/new-cycle boundary |
| `STAGE8_TASK5_EQ6_SCOPED_MATE_CERT_LANE1_V001.md` | `088eccd9ee642fcffb83e9f1ef1bb64ef479fd68534a6f3fb55d6aebce1393ce` | old-image A6 comparison |
| `DOR_020_A5_CONTACT_LAPLACIAN_REDUCING_2026-08-04.md` | `5beccc617f4c5f5f76aba777c664f3dd4393f72257fc850950e2246109a7a424` | A6's licensed old-image projector descent |
| `DOR_020_A6_J2_SCOPED_PROJECTED_LAW_2026-08-05.md` | `202234ac77136592fdc24a96838909f1dad7e8f6a79fdab81342c5f12d6e82cd` | cycle-creating old-image boundary |

## 1. Definitive carrier and map typing

### 1.1 Profile, quotient, kernel, and localization

At a finite stage `N`, set

```text
E_N
 := R L_T,N (+)_1 R Rhat_K,N (+)_1 S_1,sa(K_N),

Q_N : E_N -> O_prof,N,

Kernbar_N : O_prof,N -> Ker_N^Q408.
```

Let `C_N^k` be the actual positive finite Hodge cochain carrier, with the
DoR-019 inner product `<.,.>_N`. On the finite rank-preserving branch, the
localization symbol has the single definition

```text
Loc_N : Ker_N^Q408 -> C_N^k,
Loc_N(K) := Loc_N^fin(K) := sigma_N^fin(K).         (T1)
```

This `Loc_N` is the sealed finite-symbol leg used on `A_RP`; it is not an
assertion of the unformed post-scope physical localization on a target-only
new-cycle factor. The Hodge projector is the endomorphism

```text
P_H,N : C_N^k -> C_N^k,
H_N := im(P_H,N) subset C_N^k.
```

### 1.2 Scalar Maxwell projection

Define the normalized transverse harmonic symbol

```text
m_T,N
 := P_H,N Loc_N Kernbar_N Q_N(L_T,N).              (T2)
```

The Maxwell coefficient line is `L_Mx,N:=span{m_T,N} subset H_N`; the full
harmonic carrier `H_N` is not identified with that line.

The sealed normalization branch is

```text
m_T,N != 0.                                        (T3)
```

On `(T3)`, define

```text
lambda_N : H_N -> R,
lambda_N(h)
 := <m_T,N,h>_N / <m_T,N,m_T,N>_N,                (T4)

pi_Mx,N : C_N^k -> R,
pi_Mx,N := lambda_N o P_H,N.                       (T5)
```

Equation `(T5)` is the definitive undecorated `pi_Mx,N` used by the scalar
physical-J2 reader. It contains `P_H,N` and contains no `Loc_N`. Hence

```text
pi_Mx,N Loc_N
 = lambda_N P_H,N Loc_N                            (T6)
```

contains exactly one localization.

### 1.3 The response-bottom leg is a different bundled map

The sealed assembly also has

```text
pi_N^resp : P_N -> Bot_N^resp.                     (T7)
```

For each cycle-creating `f:N->M`, let `D_f^old` denote the licensed old-image
input domain of the A6 projected bottom leg. The sealed V002/V003/A6 stock
supplies the two restricted bundled maps

```text
D_f^old subset Ker_N^Q408,                         (T8)

J_(N|f)^bot : D_f^old -> Bot_N^resp,
J_(M|f)^bot : eta_f(D_f^old) -> Bot_M^resp.       (T9)
```

Prior sources spell these bundled legs with the legacy string
`pi_N^resp P_H,N Loc_N`. Here that string names the already sealed bundled
old-image leg; it is not promoted to a newly factored global map from
`C_N^k` into `P_N`. The A6 square is

```text
r_f^Bot J_(M|f)^bot eta_f
 = J_(N|f)^bot
 : D_f^old -> Bot_N^resp.                         (T10)
```

No sealed map `Bot_N^resp -> R`, and no sealed global placement
`H_N -> P_N`, identifies `(T9)` with `(T5)`. The two maps therefore remain
distinct throughout this artifact.

### 1.4 Prior-occurrence resolution

| Prior occurrence | Definitive reading here |
|---|---|
| Physical-J2 scalar formula and Maxwell/Hodge `(2-3)`--`(2-5)` | on `m_T,N!=0`, `(T5)`: `pi_Mx,N = lambda_N P_H,N`, followed by the separate finite `Loc_N` |
| Constraint-arm scalar coefficient reader | `(T5)` |
| Projector-locality V002 `(L3-10)` | arrow-restricted bundled bottom-valued maps in `(T9)`; no global scalar factorization is imported |
| Projector V003 line 84 | `(T10)`; the abbreviated right route is the complete bundled `J_(N|f)^bot` route |
| Projector V003 lines 155--160 | the bundled old-image leg `(T9)`, not standalone scalar `pi_Mx` |
| Scoped-mate line 49 and ratified A6 line 7 | `(T10)` |
| Scoped-mate line 55 | the bundled `(T10)` route; its legacy expansion requires the right-route finite `Loc_N` |
| J2 build line 46 | scalar stage reader using `(T5)` on `m_T,N!=0` |
| J2 build line 53 | bottom-valued old-image law `(T10)` |
| J2 build line 69 | bundled `J_(N|f)^bot` in `(T9)`; assigning its legacy triple to standalone scalar `pi_Mx,N` creates the rejected double-`Loc` expression |
| J2 build line 79 | replaced by the displays in sections 2--4 below |

This table retires the former scalar/bottom overload. It also exposes a
second typing repair: the quotient reader and its pullback to `E_N` require
different names.

## 2. Rank-preserving Hodge and coefficient-line transport

Fix `f : N -> M` in the rank-preserving category `A_RP`. On the finite Hodge
cochain carrier use

```text
j_f^C : C_N^k -> C_M^k,
rho_f^C:=(j_f^C)^* : C_M^k -> C_N^k.
```

The degrees are suppressed only where both sides visibly have the same
degree.

### 2.1 The three intertwiner displays

The sealed equations are

```text
rho_f^C d_M = d_N rho_f^C,                         (H1)
rho_f^C delta_M = delta_N rho_f^C.                 (H2)
```

With `Delta_X=d_X delta_X+delta_X d_X`, every intermediate equality is

```text
rho_f^C Delta_M
 = rho_f^C(d_M delta_M + delta_M d_M)
 = (rho_f^C d_M)delta_M + (rho_f^C delta_M)d_M
 = d_N rho_f^C delta_M + delta_N rho_f^C d_M
 = d_N delta_N rho_f^C + delta_N d_N rho_f^C
 = (d_N delta_N + delta_N d_N)rho_f^C
 = Delta_N rho_f^C.                               (H3)
```

On the union of the two finite spectra, take the finite polynomial `p` with
`p(0)=1` and `p(lambda)=0` at each nonzero spectral value. Then

```text
rho_f^C P_H,M
 = rho_f^C p(Delta_M)
 = p(Delta_N)rho_f^C
 = P_H,N rho_f^C.                                 (H4)
```

Taking adjoints, using `rho_f^C=(j_f^C)^*` and self-adjointness of `P_H`,
gives the forward square

```text
P_H,M j_f^C = j_f^C P_H,N.                        (H5)
```

### 2.2 All factor squares

Write the induced forward maps as

```text
j_f^E       : E_N -> E_M,
j_f^prof    : O_prof,N -> O_prof,M,
eta_f^K     : Ker_N^Q408 -> Ker_M^Q408,
j_f^K       : K_N -> K_M,
j_f^C       : C_N^k -> C_M^k,
J_f^S1      : S_1,sa(K_N) -> S_1,sa(K_M).
```

On the rank-preserving represented image, fix the explicit coefficient and
profile transport notation

```text
J_f^S1(C):=j_f^K C (j_f^K)^*,
j_f^E(a,b,C):=(a,b,J_f^S1(C)),
j_f^E(0,1,0)=(0,1,0).                             (F0)
```

On `A_RP`, the actual Q-408 and local-symbol stock supplies

```text
Q_M j_f^E = j_f^prof Q_N,                         (F1)
Kernbar_M j_f^prof = eta_f^K Kernbar_N,           (F2)
Loc_M eta_f^K = j_f^C Loc_N,                      (F3)
P_H,M j_f^C = j_f^C P_H,N.                       (F4)
```

Equation `(F4)` is `(H5)` on the finite local-symbol carrier. The R4 unit
seam transports the normalized transverse profile:

```text
j_f^E(L_T,N)=L_T,M.                               (F5)
```

Substitution displays the normalization-line transport:

```text
m_T,M
 = P_H,M Loc_M Kernbar_M Q_M(L_T,M)
 = P_H,M Loc_M Kernbar_M Q_M j_f^E(L_T,N)
 = P_H,M Loc_M Kernbar_M j_f^prof Q_N(L_T,N)
 = P_H,M Loc_M eta_f^K Kernbar_N Q_N(L_T,N)
 = P_H,M j_f^C Loc_N Kernbar_N Q_N(L_T,N)
 = j_f^C P_H,N Loc_N Kernbar_N Q_N(L_T,N)
 = j_f^C m_T,N.                                   (F6)
```

The rank-preserving `j_f^C` is an isometric inclusion on the finite Hodge
carrier. For every `h_N in H_N`, `(F6)` gives

```text
lambda_M(j_f^C h_N)
 = <m_T,M,j_f^C h_N>_M / <m_T,M,m_T,M>_M
 = <j_f^C m_T,N,j_f^C h_N>_M
     / <j_f^C m_T,N,j_f^C m_T,N>_M
 = <m_T,N,h_N>_N / <m_T,N,m_T,N>_N
 = lambda_N(h_N).                                 (F7)
```

On the forward image, `rho_f^C j_f^C=id`, so the typed downward form is

```text
lambda_N(rho_f^C j_f^C h_N)
 = lambda_N(h_N)
 = lambda_M(j_f^C h_N).                           (F8)
```

The scalar coefficient square is therefore

```text
pi_Mx,M j_f^C
 = lambda_M P_H,M j_f^C
 = lambda_M j_f^C P_H,N
 = lambda_N P_H,N
 = pi_Mx,N.                                       (F9)
```

Define the exact nonzero subcategory

```text
A_RP^+
 := {f:N->M in A_RP : m_T,N != 0 and m_T,M != 0}. (F10)
```

Equation `(F6)` shows that nonzero normalization is constant along every
rank-preserving connected component once it holds at one object. The sealed
stock does not establish that every such component lies in `(F10)`.

## 3. Full scalar J2, displayed on `A_RP^+`

### 3.1 Quotient reader, prequotient reader, and coefficient reconstruction

Define the quotient reader

```text
ell_N^Mx
 := pi_Mx,N Loc_N Kernbar_N
 = lambda_N P_H,N Loc_N Kernbar_N
 : O_prof,N -> R,                                 (J2-1)
```

and its prequotient pullback

```text
reader_N^E
 := ell_N^Mx Q_N
 = pi_Mx,N Loc_N Kernbar_N Q_N
 : E_N -> R.                                      (J2-2)
```

Thus the string formerly written with an arrow label as `reader_f` is a
stage component `reader_N^E`; the arrow statement is the covariance square
in `(J2-9)` below. Equations `(J2-1)` and `(J2-2)` also prevent applying
`Q_N` twice.

Normalization is displayed directly:

```text
reader_N^E(L_T,N)
 = lambda_N P_H,N Loc_N Kernbar_N Q_N(L_T,N)
 = lambda_N(m_T,N)
 = <m_T,N,m_T,N>_N / <m_T,N,m_T,N>_N
 = 1.                                             (J2-3)
```

Define the induced coefficients by

```text
chi_K,N^Mx
 := ell_N^Mx(Q_N(0,1,0)),                         (J2-4)

Tr(T_N^Mx C)
 := ell_N^Mx(Q_N(0,0,C))                          (J2-5)
```

for every represented `C in S_1,sa(K_N)`. The class of `T_N^Mx` is unique
modulo the represented annihilator

```text
Ann_N
 := {S : Tr(SC)=0 for every represented C}.       (J2-6)
```

For `z=(a,b,C) in E_N`, linearity and `(J2-3)`--`(J2-5)` give every term:

```text
reader_N^E(a,b,C)
 = a reader_N^E(L_T,N)
   + b reader_N^E(0,1,0)
   + reader_N^E(0,0,C)
 = a + b chi_K,N^Mx + Tr(T_N^Mx C)
 = ell_(chi^Mx,T^Mx),N^E(a,b,C).                 (J2-7)
```

Equation `(J2-7)` is the displayed full physical J2 equality for the
independently induced coefficient pair. For an externally preassigned pair
`(chi_N,T_N)`, the exact difference is

```text
ell_(chi,T),N^E(a,b,C)-reader_N^E(a,b,C)
 = b(chi_N-chi_K,N^Mx)
   + Tr((T_N-T_N^Mx)C).                           (J2-8)
```

Consequently an arbitrary earlier reader is not identified here unless both
displayed coefficient conditions vanish.

### 3.2 General arrowwise chain

For `f:N->M` in `A_RP^+` and `z in E_N`, substitute `(F1)`--`(F4)` and
`(F7)` one factor at a time:

```text
reader_M^E(j_f^E z)
 = lambda_M P_H,M Loc_M Kernbar_M Q_M(j_f^E z)
 = lambda_M P_H,M Loc_M Kernbar_M j_f^prof Q_N(z)
 = lambda_M P_H,M Loc_M eta_f^K Kernbar_N Q_N(z)
 = lambda_M P_H,M j_f^C Loc_N Kernbar_N Q_N(z)
 = lambda_M j_f^C P_H,N Loc_N Kernbar_N Q_N(z)
 = lambda_N P_H,N Loc_N Kernbar_N Q_N(z)
 = reader_N^E(z).                                 (J2-9)
```

Let `rho_f^E` be the sealed profile restriction on the forward image, with
`rho_f^E j_f^E=id_E,N`. Its reader statement is

```text
reader_N^E rho_f^E(j_f^E z)
 = reader_N^E(z)
 = reader_M^E(j_f^E z).                           (J2-10)
```

Only the Hodge restriction `rho_f^C` in `(H1)`--`(H5)` is identified with a
Hilbert adjoint. The profile, quotient, and kernel restrictions retain their
independently sealed types.

### 3.3 Reciprocal-loop generator class

The sealed stock names a reciprocal-loop generator class, not a preferred
single arrow. Let `u:N->M` be any rank-preserving member of that class. Its
harmonic carrier is rank one. Choose a transported cycle vector with the
admitted orientation sign `epsilon_u in {+1,-1}`:

```text
H_N=span{c_N},
H_M=span{c_M},
c_M=epsilon_u j_u^C c_N,
P_H,N(s)=<s,c_N>_N/<c_N,c_N>_N c_N.              (RL1)
```

The projector square is a direct calculation:

```text
P_H,M(j_u^C s)
 = <j_u^C s,c_M>_M/<c_M,c_M>_M c_M
 = epsilon_u <s,c_N>_N/<c_N,c_N>_N
     epsilon_u j_u^C c_N
 = j_u^C(<s,c_N>_N/<c_N,c_N>_N c_N)
 = j_u^C P_H,N(s).                                (RL2)
```

For the symbolic nontrivial loop profile, put

```text
P_re,N(r):=r^2 Rhat_K,N,
z_r := (0,f(r^2),2f_1(r^2)P_re,N(r)),
H_re,N(r)
 := [f(r^2)+2r^2 f_1(r^2)] Rhat_K,N.              (RL3)
```

No value of `r`, `f`, or `f_1` is evaluated. The complete reader chain on
this generator class is

```text
reader_M^E(j_u^E z_r)
 = lambda_M P_H,M Loc_M Kernbar_M Q_M(j_u^E z_r)
 = lambda_M P_H,M Loc_M Kernbar_M j_u^prof Q_N(z_r)
 = lambda_M P_H,M Loc_M eta_u^K Kernbar_N Q_N(z_r)
 = lambda_M P_H,M j_u^C Loc_N Kernbar_N Q_N(z_r)
 = lambda_M j_u^C P_H,N Loc_N Kernbar_N Q_N(z_r)
 = lambda_N P_H,N Loc_N Kernbar_N Q_N(z_r)
 = reader_N^E(z_r).                               (RL4)
```

### 3.4 One nonidentity refinement arrow

Take the sealed `q=2` subdivision of an already realized path:

```text
gamma_(e,1)(t)=gamma_e(t/2),
gamma_(e,2)(t)=gamma_e((1+t)/2).                  (RF1)
```

For `s_nm:n->m`, the exact refinement data are

```text
P_nm=id,
A_n=S_nm^* A_m,
S_nm^* R_K,m S_nm=R_K,n,                          (RF2)

j_nm^K:=S_nm,

(J_nm^bil H_n)(S_nm x,S_nm y)=H_n(x,y),          (RF3)

Kern_m^fin(J_nm^bil H_n)[a,b]
 = Kern_n^fin(H_n)[a,b].                          (RF4)
```

Set

```text
J_nm^S1(C):=j_nm^K C (j_nm^K)^*,
j_nm^E(a,b,C):=(a,b,J_nm^S1(C)).                  (RF5)
```

The induced finite Hodge cochain map is denoted `j_nm^C`; its current
component is `S_nm`. Here `J_nm^bil` is the bilinear-profile transport denoted
`j_nm^H` in the refinement source, while `J_nm^S1` is the typed trace-class
coefficient transport. For arbitrary `z in E_n`, every refinement equality
is

```text
reader_m^E(j_nm^E z)
 = lambda_m P_H,m Loc_m Kernbar_m Q_m(j_nm^E z)
 = lambda_m P_H,m Loc_m Kernbar_m j_nm^prof Q_n(z)
 = lambda_m P_H,m Loc_m eta_nm^K Kernbar_n Q_n(z)
 = lambda_m P_H,m j_nm^C Loc_n Kernbar_n Q_n(z)
 = lambda_m j_nm^C P_H,n Loc_n Kernbar_n Q_n(z)
 = lambda_n P_H,n Loc_n Kernbar_n Q_n(z)
 = reader_n^E(z).                                 (RF6)
```

This is a genuine nonidentity refinement display; `(RF1)`--`(RF4)` expose
the underlying path, current, metric, and Q-408 kernel maps.

### 3.5 General-arrow induction and route equality

Let

```text
N_0 -f_1-> N_1 -f_2-> ... -f_k-> N_k            (IND1)
```

be a finite word in certified `A_RP^+` generators, and write

```text
j_(f_k...f_1)^E
 := j_f_k^E ... j_f_1^E.                          (IND2)
```

The identity word gives

```text
reader_N0^E j_id^E = reader_N0^E.                 (IND3)
```

For the induction step, apply `(J2-9)` to the last generator and retain every
stage:

```text
reader_Nk^E j_(f_k...f_1)^E
 = reader_Nk^E j_f_k^E j_(f_(k-1)...f_1)^E
 = reader_N(k-1)^E j_(f_(k-1)...f_1)^E
 = reader_N(k-2)^E j_(f_(k-2)...f_1)^E
 = ...
 = reader_N1^E j_f_1^E
 = reader_N0^E.                                   (IND4)
```

Nested subdivision has `S_nl=S_ml S_nm`, while all other sealed factor maps
obey the same composition law. On a diamond

```text
N -a-> B -g-> D,
N -f-> C -h-> D,
g a = h f,                                        (IND5)
```

functoriality and `(IND4)` display both routes:

```text
reader_D^E j_g^E j_a^E
 = reader_B^E j_a^E
 = reader_N^E
 = reader_C^E j_f^E
 = reader_D^E j_h^E j_f^E.                       (IND6)
```

## 4. The actual J7 rank-one coefficient face

### 4.1 Fixed-stage extraction and rank-one comparison

For `x in K_N`, set

```text
s_N:=||x||_K,N^2,
P_x:=x^flat tensor x^flat,

H_mix,N(x)
 := f(s_N) Rhat_K,N + 2 f_1(s_N) P_x.             (C1)
```

Under the profile coordinates, `H_mix,N(x)` is `(0,f(s_N),2f_1(s_N)P_x)`.
Let

```text
q_N:=(mu_N,i_N,dot_omega_(i_N,N),mu_(i_N,N))
```

denote the symbolic represented response data at this stage. These data are
consumed only after the structural maps in sections 1--3 are fixed. For the
independently constructed reader, every coefficient step is

```text
reader_N^E(mu_N H_mix,N(x))
 = mu_N ell_N^Mx(Q_N(0,f(s_N),2f_1(s_N)P_x))
 = mu_N[
     f(s_N) ell_N^Mx(Q_N(0,1,0))
     + 2f_1(s_N) ell_N^Mx(Q_N(0,0,P_x))
   ]
 = mu_N[
     f(s_N) chi_K,N^Mx
     + 2f_1(s_N) Tr(T_N^Mx P_x)
   ]
 = mu_N[
     f(s_N) chi_K,N^Mx
     + 2f_1(s_N)<x,T_N^Mx x>_K,N
   ].                                             (C2)
```

The sealed representative identity is

```text
Delta B_(i_N,N)
 = dot_omega_(i_N,N) mu_(i_N,N) H_mix,N(x).       (C3)
```

Therefore

```text
reader_N^E(Delta B_(i_N,N))
 = reader_N^E(
     dot_omega_(i_N,N) mu_(i_N,N) H_mix,N(x))
 = dot_omega_(i_N,N) mu_(i_N,N)
     reader_N^E(H_mix,N(x))
 = dot_omega_(i_N,N) mu_(i_N,N)[
     f(s_N) chi_K,N^Mx
     + 2f_1(s_N)<x,T_N^Mx x>_K,N
   ].                                             (C4)
```

Equations `(C2)` and `(C4)` are the J7 coefficient comparison. They are not
the J2 functional equation `(J2-7)` and they are not the A6 bottom square
`(T10)`.

### 4.2 Coefficient naturality on `A_RP^+`

For `f:N->M` in `A_RP^+`, the normalized scalar and rank-one coordinates
transport as follows:

```text
chi_K,M^Mx
 = reader_M^E(0,1,0)
 = reader_M^E j_f^E(0,1,0)
 = reader_N^E(0,1,0)
 = chi_K,N^Mx.                                    (C5)
```

For every represented `C`,

```text
Tr(T_M^Mx J_f^S1(C))
 = Tr(T_M^Mx j_f^K C (j_f^K)^*)
 = Tr((j_f^K)^* T_M^Mx j_f^K C)
 = reader_M^E(0,0,J_f^S1(C))
 = reader_M^E j_f^E(0,0,C)
 = reader_N^E(0,0,C)
 = Tr(T_N^Mx C).                                  (C6)
```

Equivalently,

```text
[T_N^Mx]
 = [(j_f^K)^* T_M^Mx j_f^K]  mod Ann_N.           (C7)
```

For composable `f:N->M` and `g:M->L`, the two-step coefficient transport is

```text
[T_N^Mx]
 = [(j_f^K)^* T_M^Mx j_f^K]
 = [(j_f^K)^*(j_g^K)^* T_L^Mx j_g^K j_f^K]
 = [(j_g^K j_f^K)^* T_L^Mx(j_g^K j_f^K)]
     mod Ann_N.                                    (C8)
```

### 4.3 Every position of a rank-preserving diamond

Take the diamond `(IND5)` wholly in `A_RP^+`. For `x_N in K_N`, define

```text
x_B:=j_a^K x_N,
x_C:=j_f^K x_N,
x_D:=j_g^K x_B=j_h^K x_C.                         (D1)
```

Let `tau_r` denote the sealed action-unit/reality transport on the symbolic
response tuple along an arrow `r`. Display its two diamond routes:

```text
q_B:=tau_a(q_N),
q_C:=tau_f(q_N),
q_D:=tau_g(q_B)=tau_h(q_C),

s_B=||j_a^K x_N||_B^2=s_N,
s_C=||j_f^K x_N||_C^2=s_N,
s_D=||j_g^K j_a^K x_N||_D^2
   =||j_h^K j_f^K x_N||_D^2=s_N.                 (D1a)
```

Write the components of `q_v` as
`(mu_v,i_v,dot_omega_(i_v,v),mu_(i_v,v))`.

At its four positions, the coefficient face is explicitly

```text
J7_N(x_N)
 = mu_N[f(s_N)chi_K,N^Mx
      +2f_1(s_N)<x_N,T_N^Mx x_N>_N],

J7_B(x_B)
 = mu_B[f(s_B)chi_K,B^Mx
      +2f_1(s_B)<x_B,T_B^Mx x_B>_B],

J7_C(x_C)
 = mu_C[f(s_C)chi_K,C^Mx
      +2f_1(s_C)<x_C,T_C^Mx x_C>_C],

J7_D(x_D)
 = mu_D[f(s_D)chi_K,D^Mx
      +2f_1(s_D)<x_D,T_D^Mx x_D>_D].              (D2)
```

The corresponding four derivative entries are

```text
J7Delta_N(x_N)
 = dot_omega_(i_N,N) mu_(i_N,N)[
     f(s_N)chi_K,N^Mx
     +2f_1(s_N)<x_N,T_N^Mx x_N>_N],

J7Delta_B(x_B)
 = dot_omega_(i_B,B) mu_(i_B,B)[
     f(s_B)chi_K,B^Mx
     +2f_1(s_B)<x_B,T_B^Mx x_B>_B],

J7Delta_C(x_C)
 = dot_omega_(i_C,C) mu_(i_C,C)[
     f(s_C)chi_K,C^Mx
     +2f_1(s_C)<x_C,T_C^Mx x_C>_C],

J7Delta_D(x_D)
 = dot_omega_(i_D,D) mu_(i_D,D)[
     f(s_D)chi_K,D^Mx
     +2f_1(s_D)<x_D,T_D^Mx x_D>_D].               (D3)
```

The coefficient routes themselves are

```text
chi_K,N^Mx
 = chi_K,B^Mx
 = chi_K,D^Mx
 = chi_K,C^Mx,                                    (D4)

[T_N^Mx]
 = [(j_g^K j_a^K)^* T_D^Mx(j_g^K j_a^K)]
 = [(j_h^K j_f^K)^* T_D^Mx(j_h^K j_f^K)]
     mod Ann_N.                                    (D5)
```

The rank-one routes and derivative routes are

```text
J7_D(j_g^K j_a^K x_N;q_D)
 = J7_B(j_a^K x_N;q_B)
 = J7_N(x_N;q_N)
 = J7_C(j_f^K x_N;q_C)
 = J7_D(j_h^K j_f^K x_N;q_D),                    (D6)

J7Delta_D(j_g^K j_a^K x_N;q_D)
 = J7Delta_B(j_a^K x_N;q_B)
 = J7Delta_N(x_N;q_N)
 = J7Delta_C(j_f^K x_N;q_C)
 = J7Delta_D(j_h^K j_f^K x_N;q_D).               (D7)
```

Thus the actual J7 coefficient face is built, with every vertex and both
routes displayed, on the nonzero rank-preserving scalar branch.

### 4.4 Exact obstruction on the full diamond family

The requested all-diamond face has two independent sealed-stock
obstructions.

#### O1. Zero-normalization branch

Projector V003 carries both the branch `m_T,N != 0` and a void zero branch.
At a stage with `m_T,N=0`, `(T4)` reads

```text
lambda_N(h)=<0,h>_N/<0,0>_N,                     (O1)
```

so the scalar `pi_Mx,N`, the scalar reader, and its coefficient pair are not
formed. No all-stage nonvanishing theorem occurs in the sealed stock.

#### O2. Scalar versus response-bottom codomain

The two existing projections have different codomains:

```text
pi_Mx,N : C_N^k -> R,
J_(N|f)^bot : D_f^old -> Bot_N^resp.              (O2)
```

A6 constrains `(T9)` on `D_f^old`; it does not constrain `(T5)`. No sealed
arrow `Bot_N^resp -> R`, and no sealed global map `H_N -> P_N`, closes the
typing gap. Substituting `(T10)` for the coefficient face therefore repeats
the defect identified in Dario review D3.

At a target-only new-cycle position, `(T9)` is defined only on the licensed
old-image domain and the full scalar `Loc/pi_Mx` leg is a retained post-scope
condition. Thus neither `(C2)` nor `(C4)` has a sealed scalar naturality route
through that position. This is the exact missing object, not a reuse of the
J2 equation.

The maximal result is therefore

```text
J7_COEFFICIENT_FACE_ON_A_RP_PLUS = BUILT,
J7_COEFFICIENT_FACE_ON_FULL_DIAMOND_FAMILY
 = OBSTRUCTED(O1,O2).                             (O3)
```

## 5. F_PLDEC rerun and anti-tuning ledger

### 5.1 Dependency order

The complete construction order used above is

```text
actual Q408 maps and finite metric
 -> d, delta, Delta
 -> P_H
 -> finite Loc=Loc^fin=sigma^fin
 -> m_T
 -> lambda and scalar pi_Mx on m_T!=0
 -> ell^Mx and reader^E
 -> chi^Mx and T^Mx extraction
 -> rank-one J7 and Delta B_i face.                (B1)
```

Neither `reader`, `chi`, nor `T` occurs to the left of its own construction
point in `(B1)`. In particular, neither the scalar projection `(T5)` nor the
bundled old-image leg `(T9)` is defined from a reader. The new coefficient
face therefore passes the F_PLDEC circularity rerun on its stated `A_RP^+`
scope.

### 5.2 Anti-tuning ledger

| Forbidden input or action | Occurrence in construction | Result |
|---|---:|---|
| response value or threshold used to choose a structural map | symbolic `q_N` enters only after `(B1)` fixes every structural map; no desired value or threshold enters | clean |
| completed object used as a construction predecessor | none; only the represented finite profile is consumed downstream | clean |
| member or representative selection | none | clean |
| fixed-point execution | none | clean |
| end-test execution | none | clean |
| numerical evaluation | none | clean |
| measured-constant comparison | none | clean |
| reader-derived `Loc` or `pi_Mx` | none; see `(B1)` | clean |
| substitution of A6/J2 for J7 | none; see `(C2)`--`(C4)` and `(O2)` | clean |

No gate prevented a structural calculation. The obstruction in `(O3)` is a
map/branch underdetermination in sealed stock, so no machinery appeal is
entered.

## 6. Self status-verb audit

| Status verb used by this artifact | Display immediately supporting it | Audit |
|---|---|---|
| `DEFINITIVE` for `pi_Mx`/`Loc` typing | `(T1)`--`(T10)` plus the prior-occurrence table | exact domains, codomains, and bundles displayed |
| `DISPLAYED` for the `A_RP^+` J2 reconstruction | `(H1)`--`(H5)`, `(F0)`--`(F9)`, `(J2-1)`--`(J2-10)`, `(RL1)`--`(RL4)`, `(RF1)`--`(RF6)`, `(IND1)`--`(IND6)` | every factor equality written |
| `BUILT` for the `A_RP^+` coefficient face | `(C1)`--`(C8)` and all four positions `(D1)`--`(D7)` | coefficient extraction, response transport, and both routes written |
| `OBSTRUCTED` for the full coefficient face | zero denominator `(O1)` and scalar/bottom typing mismatch `(O2)` | two explicit obstructions written |
| `CLEAN` for circularity and anti-tuning | dependency order `(B1)` and the ledger in section 5.2 | every forbidden predecessor/action absent |

Scope retained at stop:

```text
J2_SCALAR_THEOREM_SCOPE = A_RP^+
UNCONDITIONAL_ALL_A_RP_NORMALIZATION = NOT_ESTABLISHED (+m_T=0 void branch)
FULL_CYCLE_CREATING_SCALAR_J2 = POST_SCOPE_NOT_FORMED
MEMBERSHIP_THEOREM = NOT_ASSERTED
FC6_OR_CONSUMER_ARROW_REPAIR = OUTSIDE_THIS_ARTIFACT
MACHINERY_APPEAL = false
```

COEFFICIENT_FACE = OBSTRUCTED (+m_T=0 denominator; +scalar/bottom codomain mismatch)
J2_RP_RECONSTRUCTION = DISPLAYED
PI_MX_LOC_TYPING = DEFINITIVE
VERB_AUDIT_SELF = CLEAN
