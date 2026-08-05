# STAGE 8 / TASK 5 / EQ6 — THE LOC-NATURALITY LEMMA, STANDALONE

Lane: Codex Lane 3  
Artifact: `STAGE8_TASK5_EQ6_LOC_NATURALITY_LANE3_V001.md`  
Register head checked: `Q-493`  
Mode: symbolic only

## 0. Preflight, authorities, and result convention

The three STEP-0 locations were accessible. The supervision register ended
at `Q-493`; its SHA-256 at read time was
`1e2b26eae45c30aa00f0c572f9d5acee628f217f8ae9d3b41e5b4dfb87333506`.
The audited input in the archive workspace recomputed to its commissioned
digest:

```text
STAGE8_TASK5_EQ6_TWO_LEMMAS_LANE3_V001.md
SHA-256 = 48616c239ccdd777d1ac7cf5a049f324b98ca6abdba84966c5dc98151c461de4
```

The requested output and sidecar were absent from both the cleanroom and the
archive workspace before creation.

The sealed inputs used below were hash-verified against the archive:

| Input | SHA-256 | Exact content consumed |
|---|---|---|
| `STAGE8_TASK5_EQ6_TWO_LEMMAS_LANE3_V001.md` | `48616c239ccdd777d1ac7cf5a049f324b98ca6abdba84966c5dc98151c461de4` | custody handoff; L2 was not run there |
| `STAGE8_TASK5_EQ6_J7_REVIEW_AND_ADJUDICATION_DARIO_V001.md` | `f76139e5424c34d1198faf15ce2d0fa06d2e984f53c7da6854b8dad79384f80b` | F1(b), including the precise `(F1)` and `(F3)` debts |
| `STAGE8_TASK5_EQ6_J7_FACE_AND_J2_DISPLAY_LANE3_V001.md` | `9c74ed3dbe748450e525102128b0367ce21c0e5029929eab33a111ca9802dc3c` | declared finite `Loc` typing, reciprocal-loop and `q=2` displays |
| `STAGE8_TASK5_R4_LOCAL_SYMBOL_MAP_BUILD_LANE1_V001.md` | `bae34116c4d6792b5e39b913addeeff1650989660d89ba01bf5de62ec2d9aa50` | profile presentation, relations, signed-isomorphism covariance, W3 restriction |
| `STAGE8_TASK5_R4_KERNEL_REALIZATION_AND_SYMBOL_CALCULUS_LANE2_V001.md` | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | actual `sigma_cyl`, Q-408 kernel covariance, Ward/faithfulness before reader pullback |
| `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md` | `e21cee3081da06417109697352abe570c58dc6dda7d46e78f690d666bed128f5` | finite C3 datum and its field/test pullback |
| `STAGE8_TASK5_EQ6_ASSEMBLY_STAGE1_REVIEW_LANE1_V001.md` | `049f6386835adcf5089a74d49add67c76973c5bb89fe3571c1e5fbceb8b0f5df` | V001 C3 survives only on admitted maps |
| `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V002.md` | `e5381e6687dbdd5aed792bdddd1050ea7f39d17e748d6c9e374746c4cee37731` | represented-kernel `Eta_f` definition and composition |
| `STAGE8_TASK5_EQ6_STAGE1_V002_REVIEW_LANE1_V001.md` | `312dbe14efebd167b5287ccde773d69e64eb17b9bcfe91137d1e4cea50b15e0e` | confirms `Eta_f` only on `im(Kernbar)`; V002 globally defective |
| `STAGE8_TASK5_CONTINUUM_PACKAGE_ADOPTION_PROPOSAL_LANE2_V004.md` | `fa73114214d7653d9a5d181a684b3bd65f0d6e9f91fd2256fb159ca97e56c4bf` | actual nonidentity `Ref_path` current/kernel square and Hodge boundary |
| `STAGE8_TASK5_EQ6_PROJECTOR_CERT_V003_LANE1_V001.md` | `0bef9a003abb586666535689e98d7af29e7fc75b81e06fe439397ce2b8ef9100` | proved rank-preserving `d`, `delta`, Laplacian, and `P_H` intertwiners only |
| `STAGE8_TASK5_EQ6_PHYSICAL_J2_LANE2_V001.md` | `3fd4b924ec1a70f3e730bcf99f406d697c53937b26467d2ae6d5aa8c1bb6822c` | finite-shadow/physical-`Loc` distinction |

`PROVEN` below means the complete equality is displayed from those
sealed definitions. `SUBSCOPE` means the equality is proved on a named
proper subcategory and is neither proved nor refuted outside it. A logical
non-entailment control is not relabelled an actual-surface counterexample.

## 1. Exact type ledger

### 1.1 Three objects called “symbol” in the stock

[PROVABLE] The genuine Q-408 cylindrical symbol is

```text
sigma_cyl,N:
 Hom(K_N^fin,(K_N^fin)^*)
 -> D'(M_N x M_N;T^*M_N boxtimes T^*M_N),

sigma_cyl,N(H)=Kern_N^fin(H).                     (T1)
```

It is an actual path-bilocal distribution. It is not a Hodge cochain.

[PROVABLE] Stage 1 separately carries the finite C3 datum

```text
C3_N^fin=(Ward_N^fin,sigma_N^fin)                 (T2)
```

and defines its target-to-source field/test pullback by

```text
rho_f^C3(Ward_M^fin,sigma_M^fin)
 :=((j_f^H)^* Ward_M^fin S_f^J,
    (j_f^fld)^* sigma_M^fin j_f^fld).             (T3)
```

Equation `(T3)` is a contravariant datum-level pullback. It does not state a
map

```text
sigma_N^fin:Ker_N^Q408 -> C_N^k,                  (T4)
```

does not state its linearity, and does not identify `j_f^fld` with the Hodge
cochain inclusion `j_f^C`.

[PART-PROVABLE] The face artifact later declares the finite reader-facing
typing

```text
Loc_N:Ker_N^Q408 -> C_N^k,
Loc_N(K):=Loc_N^fin(K):=sigma_N^fin(K).           (T5)
```

The present relay grants `(T5)` as the target's internal map declaration so
that the proposed square is composable. It does not promote `(T2)`--`(T3)`
into a construction of `(T4)`, nor add a missing arrow law.

The physical-J2 artifact makes the boundary explicit by declaring its finite
`Loc_N^shadow(K):=sigma_N^fin(K)` built and reader-independent, while the
stronger physical localization

```text
Ker_N^Q408 -> Sym_N^loc                           (T6)
```

with contact/local/Maxwell structure is not built.

### 1.2 Kernel and Hodge transports

[PROVABLE] On represented Q-408 kernels, Stage 1 defines

```text
eta_f^K(Kernbar_N H)
 := Kernbar_M(j_f^prof H).                        (T7)
```

Finite faithfulness makes `(T7)` representative-independent, and

```text
eta_id^K=id,
eta_g^K eta_f^K=eta_gf^K.                        (T8)
```

[PROVABLE] Independently, the Hodge stock has

```text
j_f^C:C_N^k -> C_M^k,
rho_f^C:=(j_f^C)^*:C_M^k -> C_N^k,               (T9)
```

and on its certified rank-preserving chain/adjoint scope proves

```text
rho_f^C d_M=d_N rho_f^C,
rho_f^C delta_M=delta_N rho_f^C,
rho_f^C P_H,M=P_H,N rho_f^C,
P_H,M j_f^C=j_f^C P_H,N.                         (T10)
```

No equality in `(T7)`--`(T10)` connects `eta_f^K` to `j_f^C` through `Loc`.
That missing bridge is exactly

```text
Loc_M eta_f^K = j_f^C Loc_N.                     (LOC)
```

## 2. X1 — `Loc`-naturality

### 2.1 [PROVABLE] The identity-arrow subcategory

Define the intensional certified scope

```text
A_RP^Loc
 := {f:N->M in A_RP:
       a map-level certificate for (LOC) is displayed}.        (L1)
```

Every identity belongs to `(L1)`. For `x in Ker_N^Q408`, every intermediate
equality is

```text
Loc_N eta_id,N^K(x)
 = Loc_N(id_Ker,N(x))
 = Loc_N(x)
 = id_C,N(Loc_N(x))
 = j_id,N^C Loc_N(x).                            (L2)
```

Thus `(LOC)` is proved on the identity-arrow subcategory.

### 2.2 [PART-PROVABLE] Reciprocal-loop generator display

Let `u:N->M` be a nonidentity rank-preserving member of the sealed
reciprocal-loop generator class, and let `K in Ker_N^Q408`. The two routes,
using every available definition, are

```text
Loc_M eta_u^K(K)
 = sigma_M^fin(eta_u^K K)                        by (T5)
 ?= j_u^C sigma_N^fin(K)                         missing (LOC-RL)
 = j_u^C Loc_N(K)                                by (T5).       (L3)
```

The earlier reciprocal-loop calculation proves only

```text
P_H,M j_u^C(s)
 = j_u^C P_H,N(s)                                (L4)
```

by the rank-one harmonic formula. It never evaluates either side of the
question-marked equality in `(L3)`. In the prior `RL4` reader chain, the
step from `Loc_M eta_u^K` to `j_u^C Loc_N` is therefore a use of the missing
premise, not its proof.

No sealed reciprocal-loop witness makes the two existing values unequal.
Hence `(LOC-RL)` is unestablished, not refuted.

### 2.3 [PART-PROVABLE] The nonidentity `q=2` refinement display

Take the actual `Ref_path` subdivision `s_nm:n->m`:

```text
gamma_(e,1)(t)=gamma_e(t/2),
gamma_(e,2)(t)=gamma_e((1+t)/2),
P_nm=id.                                         (L5)
```

Let `S_nm` be its oriented current map. For a coarse represented profile
`H`, the sealed construction gives

```text
eta_nm^K(Kernbar_n H)
 = Kernbar_m(j_nm^H H),                           (L6)

Kern_m^fin(j_nm^H H)[P_nm a,P_nm b]
 = Kern_n^fin(H)[a,b].                            (L7)
```

Applying the declared finite `Loc` typing writes the complete attempted
square:

```text
Loc_m eta_nm^K(Kernbar_n H)
 = Loc_m(Kernbar_m(j_nm^H H))                     by (L6)
 = sigma_m^fin(Kernbar_m(j_nm^H H))              by (T5)
 ?= j_nm^C sigma_n^fin(Kernbar_n H)              missing (LOC-RF)
 = j_nm^C Loc_n(Kernbar_n H)                     by (T5).       (L8)
```

Equations `(L5)`--`(L7)` contain paths, currents, Riesz data, and the
bilocal Q-408 kernel. They contain neither a cochain-valued `sigma` formula
nor the equality `(LOC-RF)`. Their sealing source expressly says that its
kernel square cannot be promoted to a Hodge square and stops before the
coframe/density/Hodge/localization package.

Thus the required equality already lacks a base case on this explicit
nonidentity refinement.

### 2.4 [YOURS] Failure-capable non-entailment control

The following does not claim an observed failure of the unbuilt physical
`Loc`; it proves that the sealed downward and projector laws cannot imply
the forward equality.

Use this fully explicit abstract rank-preserving model, with the standard
inner products so that each displayed `rho_f` is the adjoint of `j_f`:

```text
Ker_N=R,                 Ker_M=R,
eta_f^K=id_R,

C_N^(k-1)=0,             C_N^k=R,
C_M^(k-1)=R,             C_M^k=R direct_sum R,
C_N^(k+1)=0,             C_M^(k+1)=0,

j_f^(k-1):0->R,          j_f^C(x)=(x,0),
rho_f^(k-1):R->0,        rho_f^C(a,b)=a,

d_N^(k-1)=d_N^k=0,       delta_N^k=0,
d_M^(k-1)(t)=(0,t),      d_M^k=0,
delta_M^k(a,b)=b,

P_H,N=id_R,              P_H,M(a,b)=(a,0).        (L9)
```

All cochain degrees and differential/adjoint components not listed in
`(L9)` are zero.

Here the target's second coordinate is a contractible exact direction, so
the harmonic rank is unchanged. Indeed, at degree `k`,

```text
Delta_N(x)=0,
Delta_M(a,b)
 =d_M^(k-1) delta_M^k(a,b)+delta_M^(k+1) d_M^k(a,b)
 =d_M^(k-1)(b)+0
 =(0,b),

ker(Delta_N)=R,
ker(Delta_M)=R direct_sum {0},
P_H,N=id_R,
P_H,M(a,b)=(a,0).                                (L9-H)
```

The chain, adjoint, and projector equations are displayed directly:

```text
rho_f^C d_M^(k-1)(t)
 =rho_f^C(0,t)
 =0
 =d_N^(k-1) rho_f^(k-1)(t),

rho_f^(k-1) delta_M^k(a,b)
 =0
 =delta_N^k rho_f^C(a,b),

rho_f^C P_H,M(a,b)
 =rho_f^C(a,0)
 =a
 =P_H,N rho_f^C(a,b),

P_H,M j_f^C(x)
 =P_H,M(x,0)
 =(x,0)
 =j_f^C P_H,N(x).                                (L10)
```

Define the two localization maps, without inspecting any reader, by

```text
Loc_N(x):=x,
Loc_M(y):=(y,y).                                  (L11)
```

The stronger old-image square passes:

```text
rho_f^C Loc_M eta_f^K(x)
 =rho_f^C Loc_M(x)
 =rho_f^C(x,x)
 =x
 =Loc_N(x).                                       (L12)
```

For a symbolic nonzero `x`, however, the forward square fails:

```text
Loc_M eta_f^K(x)
 =Loc_M(x)
 =(x,x)
 !=(x,0)
 =j_f^C Loc_N(x).                                (L13)
```

Thus all displayed rank-preserving `d`/`delta`/projector laws, and even a
stronger downward `Loc` square, can hold while unprojected `(LOC)` fails. A
new proof must supply both

```text
rho_f^C Loc_M eta_f^K=Loc_N,
Loc_M eta_f^K(Ker_N^Q408) subset im(j_f^C),       (L14)
```

or an equivalent no-extra-target-symbol theorem. Neither clause in `(L14)`
is sealed for a nonidentity rank-preserving arrow. Because `(L9)`--`(L13)`
are an abstract model rather than an actual surface stage, this is a
non-entailment result, not a refutation of the target equality.

### 2.5 [PROVABLE] Conditional composition and displayed induction

If `f:N->M` and `g:M->L` already belong to `A_RP^Loc`, then for every `x`

```text
Loc_L eta_gf^K(x)
 = Loc_L eta_g^K eta_f^K(x)                      by (T8)
 = j_g^C Loc_M eta_f^K(x)                        by (LOC) for g
 = j_g^C j_f^C Loc_N(x)                          by (LOC) for f
 = j_gf^C Loc_N(x).                              (L15)
```

For a finite word

```text
N_0 -f_1-> N_1 -f_2-> ... -f_k-> N_k,
F_k:=f_k...f_1.                                  (L16)
```

The base case is the certified generator equality itself:

```text
Loc_N1 eta_F1^K
 =Loc_N1 eta_f1^K
 =j_f1^C Loc_N0
 =j_F1^C Loc_N0.                                 (L17)
```

Assume `Loc_Nk eta_Fk^K=j_Fk^C Loc_N0`. For a further certified generator
`f_(k+1):N_k->N_(k+1)`, the complete induction step is

```text
Loc_N(k+1) eta_F(k+1)^K
 =Loc_N(k+1) eta_f(k+1)^K eta_Fk^K
 =j_f(k+1)^C Loc_Nk eta_Fk^K
 =j_f(k+1)^C j_Fk^C Loc_N0
 =j_F(k+1)^C Loc_N0.                             (L18)
```

This proves `(LOC)` on every word whose generators already have certified
base squares. It cannot start on the nonidentity reciprocal-loop or `q=2`
generators because `(L3)` and `(L8)` lack those base equalities. The
cross-family review's F1(b) records a workspace-wide search finding no
sealed nonidentity `Loc` square; the W3, common-refinement, and consumer
stocks add no map-level `Loc` law. Therefore, in the corpus sealed through
`Q-493`, the maximal **certified** scope is the identity-arrow subcategory.
This is a statement about available proof certificates, not a refutation of
the equality on any actual nonidentity arrow.

```text
LOC_NATURALITY_SCOPE = identity-arrow subcategory
NONIDENTITY_LOC_STATUS = UNESTABLISHED, NOT REFUTED
```

## 3. X2 — the `(F1)` quotient companion

### 3.1 [PROVABLE] Presentation and exact descent criterion

Separate the prequotient realization from the quotient map. Define

```text
E_N
 := R L_T,N direct_sum_1 R R_K,N
      direct_sum_1 S_1,sa(K_N),

qtilde_N(a,b,C)
 := a L_T,N+j_R4,N(b R_K,N+C),                   (Q1)

Rel_N:=closure(ker qtilde_N),
O_prof,N:=E_N/Rel_N,
Q_N:E_N -> O_prof,N.                             (Q2)
```

Separate algebraic-dual transport from Hilbert-operator notation. For a
Riesz-dressed coefficient form `C:K_N->K_N^*`, write

```text
C_hat:=R_K,N^(-1) C:K_N->K_N,
(j_f^K)^dagger:K_M->K_N,

J_f^coef(C)
 :=R_K,M j_f^K C_hat (j_f^K)^dagger
 :K_M->K_M^*.                                    (Q3-T)
```

This is the typed meaning of the earlier shorthand `j_f^K C (j_f^K)^*`.
On a carrier isomorphism it is equivalently

```text
J_f^form(C):=(j_f^K)^(-*) C (j_f^K)^(-1),        (Q3-F)
```

where `(-*)` is inverse algebraic-dual transport. In Hilbert-operator
notation the same coefficient is transported as
`j_f^K C_hat (j_f^K)^dagger`. These stars are not interchanged below.

For a rank-preserving carrier map with this coefficient transport, the
proposed prequotient map is

```text
j_f^E(a,b,C)
 :=(a,b,J_f^coef(C)).                             (Q3)
```

If `(Q5)` holds, the proposed prequotient map induces

```text
bar(j_f^E)(Q_N z):=Q_M(j_f^E z).                 (Q4)
```

This induced map is well defined exactly when

```text
j_f^E(Rel_N) subset Rel_M.                       (Q5)
```

The commissioned `(F1)` uses the **already sealed** quotient transport
`j_f^prof`, not a newly named map. Hence its exact criterion is the pair

```text
j_f^E(Rel_N) subset Rel_M,
bar(j_f^E)=j_f^prof.                             (Q6)
```

Once both clauses of `(Q6)` are displayed, every intermediate equality in
`(F1)` is

```text
Q_M j_f^E(z)
 = [j_f^E z]_Rel_M
 = bar(j_f^E)([z]_Rel_N)
 = j_f^prof([z]_Rel_N)
 = j_f^prof Q_N(z).                              (Q6-D)
```

### 3.2 [PROVABLE] Full linear realization-isomorphism subscope

Let `A_iso` be the admitted **linear** realization isomorphisms/relabelings
(including linear orientation signs) for which the sealed R5 covariance
maps `U` and `Alpha_U` exist. The separate antiunitary reality branch is not
silently folded into this linear equation. The prequotient stock gives

```text
alpha_U(a,b,C):=(a,b,J_U^coef(C))
               equivalent in operator notation to
               (a,b,U C_hat U^dagger),           (Q7)

qtilde_M alpha_U=Alpha_U qtilde_N,               (Q8)

alpha_U(Rel_N)=Rel_M.                            (Q9)
```

The same sealed covariance clause says that `alpha_U` descends isometrically
to the existing quotient transport. Thus, on this scope, every required
identification is

```text
j_f^E=alpha_U,
bar(j_f^E)=bar(alpha_U),
j_f^prof=bar(alpha_U),
bar(j_f^E)=j_f^prof.                             (Q9-ID)
```

Equations `(Q8)`--`(Q9-ID)` prove both clauses of `(Q6)`, so the full
equality `(Q6-D)` holds for every `z in E_N`, including arbitrary mixed
`L_T`/Riesz/trace-class relations.

### 3.3 [PART-PROVABLE] Reciprocal-loop generator display

First let `u:N->M` be a reciprocal-loop relabeling lying in `A_iso`, and
write its rank-one carrier map as `U_u`. For arbitrary `z=(a,b,C)`, the raw
route is

```text
qtilde_M j_u^E(a,b,C)
 = qtilde_M(a,b,J_Uu^coef(C))
 = Alpha_u qtilde_N(a,b,C)                       by (Q8).       (Q10)
```

Hence for `r in Rel_N`,

```text
j_u^E(r)
 = alpha_Uu(r)
 in alpha_Uu(Rel_N)
 = Rel_M,                                        (Q11)
```

and the quotient routes are

```text
Q_M j_u^E(a,b,C)
 = [j_u^E(a,b,C)]_Rel_M
 = bar(alpha_Uu)([a,b,C]_Rel_N)
 = j_u^prof([a,b,C]_Rel_N)                       by (Q9-ID)
 = j_u^prof Q_N(a,b,C).                          (Q12)
```

This proves the full companion on reciprocal-loop relabelings that lie in
`A_iso`. The sealed stock does not prove that every rank-preserving member
of the reciprocal-loop generator class is such a realization isomorphism.
For a generic reciprocal-loop arrow `v`, the commissioned routes stop at

```text
Q_M j_v^E(z)
 =[j_v^E z]_Rel_M
 ?=j_v^prof([z]_Rel_N)                            needs both
       FORMATION: j_v^E(Rel_N) subset Rel_M,
       IDENTIFICATION AFTER FORMATION:
         bar(j_v^E)=j_v^prof
 =j_v^prof Q_N(z).                               (Q12-RL)
```

Neither question-marked reciprocal-loop premise is sealed outside
`A_iso`. No violating relation is exhibited, so the generic case is
unestablished rather than refuted. A reciprocal-loop `Ref_path` subdivision
has the still sharper one-sided boundary in the next section.

### 3.4 [PART-PROVABLE] The `q=2` Ref_path relation display

For `s_nm:n->m`, the sealed path construction proves that

```text
S_nm:K_n -> K_m
```

is an isometric isomorphism of the complete conserved carrier in this scope
and seals the contravariant Riesz law

```text
S_nm^* R_K,m S_nm=R_K,n.                         (Q13)
```

Here `S_nm^*:K_m^*->K_n^*` is the algebraic dual. Because `S_nm` is
bijective, `(S_nm^*)^(-1)=S_nm^(-*)`, and `(Q13)` gives the typed forward
form transport

```text
R_K,m
 =S_nm^(-*) S_nm^* R_K,m S_nm S_nm^(-1)
 =S_nm^(-*) R_K,n S_nm^(-1),

J_nm^form(C)
 :=S_nm^(-*) C S_nm^(-1):K_m->K_m^*.             (Q13-F)
```

This uses inverses only inside algebraic transport along the already sealed
carrier isomorphism. It neither adds an `m->n` arrow to `I_F` nor promotes
the adjoint restriction to a new physical morphism.

On the reciprocal rank-one source carrier let `e_n` be a normalized carrier
vector, put `x=r e_n`, retain `r` symbolically, and set `t:=r^2`. The actual
source relation and its proposed prequotient image are

```text
P_x=t R_K,n,
r_x:=(0,-t,P_x) in Rel_n,

e_m:=S_nm e_n,
S_nm x=r e_m,
||e_m||_m=||e_n||_n,

J_nm^form(P_x)(S_nm y,S_nm z)
 =P_x(y,z)
 =<x,y>_n <x,z>_n
 =<S_nm x,S_nm y>_m <S_nm x,S_nm z>_m
 =P_(S_nm x)(S_nm y,S_nm z),

J_nm^form(P_x)
 =P_(S_nm x)
 =t R_K,m,

j_nm^E(r_x)
 =(0,-t,J_nm^form(P_x))
 =(0,-t,t R_K,m).                                (Q14)
```

The equality of forms uses surjectivity of `S_nm`; the last line is the
sealed rank-one identity at stage `m` applied to the displayed transported
normalized vector.

The exact target-relation calculation is therefore

```text
qtilde_m(0,-t,J_nm^form(P_x))
 =j_R4,m(J_nm^form(P_x)-t R_K,m)
 =j_R4,m(t R_K,m-t R_K,m)
 =0.                                              (Q15)
```

Thus the named source relation is preserved:

```text
j_nm^E(r_x)
 =(0,-t,J_nm^form(P_x))
 in Rel_m.                                       (Q16)
```

On this single zero-class relation, both quotient routes are fully
displayed without needing a general quotient-map identification:

```text
Q_m j_nm^E(r_x)
 =[(0,-t,J_nm^form(P_x))]_Rel_m
 =[0]_Rel_m
 =0
 =j_nm^prof(0)
 =j_nm^prof(Q_n r_x).                            (Q17)
```

For a general relation `r=(a,b,C) in Rel_n`, full `(F1)` would require both

```text
j_nm^E(a,b,C)
 =(a,b,J_nm^form(C)),

j_nm^E(r)
 =(a,b,J_nm^form(C))
 in Rel_m                                        for every r in Rel_n,

j_nm^E(Rel_n) subset Rel_m,                       formation

bar(j_nm^E)=j_nm^prof                             identification only
                                                   after formation. (Q18)
```

The named relation calculation does not provide `(Q18)` for arbitrary mixed
`L_T`/Riesz/trace-class relations and does not identify the two general
quotient maps. The lawful general W3 profile map instead runs
target-to-source:

```text
rho_mn(a,b,C)=(a,b,S_nm^* C S_nm).               (Q19)
```

Using the already sealed quotient map `j_nm^prof` to assert the missing
general identification in `(Q18)` would be circular. No sealed relation
violating `(Q18)` is exhibited. Hence `(F1)` as a map on this nonidentity
refinement is unestablished, not refuted; only the displayed rank-one
zero-class relation is certified.

### 3.5 [PROVABLE] Displayed induction on the stated subscopes

On `A_iso`, let the carrier maps for `f` and `g` be `U_f` and `U_g`. The
prequotient functorial law is displayed on arbitrary `(a,b,C)`:

```text
j_g^E j_f^E(a,b,C)
 =j_g^E(a,b,J_f^form(C))
 =(a,b,J_g^form(J_f^form(C)))
 =(a,b,U_g^(-*) U_f^(-*) C U_f^(-1) U_g^(-1))
 =(a,b,(U_g U_f)^(-*) C (U_g U_f)^(-1))
 =(a,b,J_gf^form(C))
 =j_gf^E(a,b,C).                                 (Q20-E)
```

The existing quotient maps are the descended covariance maps, so for every
`[z] in O_prof,N`,

```text
j_g^prof j_f^prof([z])
 =bar(alpha_Ug) bar(alpha_Uf)([z])
 =[alpha_Ug alpha_Uf(z)]_Rel_L
 =[alpha_Ugf(z)]_Rel_L
 =bar(alpha_Ugf)([z])
 =j_gf^prof([z]).                                (Q20-P)
```

For composable arrows `f:N->M`, `g:M->L` in `A_iso`, every composition
equality is

```text
Q_L j_gf^E
 =Q_L j_g^E j_f^E                                by (Q20-E)
 =j_g^prof Q_M j_f^E                             by (Q6-D) for g
 =j_g^prof j_f^prof Q_N                          by (Q6-D) for f
 =j_gf^prof Q_N                                  by (Q20-P).   (Q21)
```

For a word `F_k:=f_k...f_1` of `A_iso` generators, the base case is

```text
Q_N1 j_F1^E
 =Q_N1 j_f1^E
 =j_f1^prof Q_N0
 =j_F1^prof Q_N0.                                (Q22)
```

Assume `Q_Nk j_Fk^E=j_Fk^prof Q_N0`. For one further certified generator
`f_(k+1):N_k->N_(k+1)`, the complete induction step is

```text
Q_N(k+1) j_F(k+1)^E
 =Q_N(k+1) j_f(k+1)^E j_Fk^E
 =j_f(k+1)^prof Q_Nk j_Fk^E
 =j_f(k+1)^prof j_Fk^prof Q_N0
 =j_F(k+1)^prof Q_N0.                            (Q23)
```

This proves full `(F1)` on words in `A_iso`. It cannot start on a generic
reciprocal-loop generator because `(Q12-RL)` lacks both base clauses, or on
the nonidentity `Ref_path` generator because the pointwise zero-class result
`(Q17)` does not supply the general clauses `(Q18)`.

```text
F1_FULL_CERTIFIED_SCOPE = A_iso
F1_GENERIC_RECIPROCAL = UNESTABLISHED, NOT REFUTED
F1_REFPATH_NAMED_RANK_ONE_RELATION = PROVEN
F1_REFPATH_GENERAL = UNESTABLISHED, NOT REFUTED
F1_FULL_A_RP = UNESTABLISHED, NOT REFUTED
```

## 4. X3 — consequence for the displayed J2 chain

### 4.1 Premise ledger

| J2 step | Status after this relay | Reason |
|---|---|---|
| `(F1)` `Q_M j_f^E=j_f^prof Q_N` | **SUBSCOPE** | full on linear `A_iso`; `Ref_path` named rank-one zero relation preserved, but generic reciprocal and general `Ref_path` descent/map identification remain open at `(Q12-RL)`, `(Q18)` |
| `(F2)` `Kernbar_M j_f^prof=eta_f^K Kernbar_N` | **PROVEN on represented scope** | definition `(T7)` and finite faithfulness |
| `(F3)` `Loc_M eta_f^K=j_f^C Loc_N` | **SUBSCOPE: identities only** | reciprocal `(L3)` and refinement `(L8)` lack their base equality |
| `(F4)` `P_H,M j_f^C=j_f^C P_H,N` | **PROVEN on certified rank-preserving intertwining scope** | independent `d`/`delta`/projector theorem `(T10)` |
| normalized-line transport | **CONDITIONAL** | separately awaits a nonzero seed; not retried here |

### 4.2 Exact stopping point in the arrowwise chain

For a general nonidentity rank-preserving `f`, the intended display is

```text
lambda_M P_H,M Loc_M Kernbar_M Q_M j_f^E
 ?= lambda_M P_H,M Loc_M Kernbar_M j_f^prof Q_N  needs full (F1)
 =  lambda_M P_H,M Loc_M eta_f^K Kernbar_N Q_N   by (F2)
 ?= lambda_M P_H,M j_f^C Loc_N Kernbar_N Q_N     needs (F3)
 =  lambda_M j_f^C P_H,N Loc_N Kernbar_N Q_N     by (F4).       (J1)
```

On an `A_iso` arrow the first question mark is closed by `(Q6-D)`, but the
second remains. On a nonidentity `Ref_path` arrow both question marks remain
for a general profile. The isolated zero-class equality `(Q17)` does not
supply the missing map equality in `(J1)`. On identities the two naturality
substitutions reduce tautologically, but that does not construct or prove
linearity of the map declared in `(T5)`.

In addition, the prior coefficient reconstruction uses linearity of the
declared cochain-valued localization `(T5)`. The sealed finite C3 datum and
`(T5)` do not display that map-level construction or linear structure. Thus
the finite rank-preserving J2 reconstruction remains premise-incomplete even
independently of the seed question. The stronger physical landing theorem
`(T6)` remains a separate physical-package debt; it is not counted as an
extra premise of the finite cochain chain `(J1)`.

```text
F1_F3_SUBSTITUTIONS = TAUTOLOGICAL only on identities
J2_RP_GENERAL = INCOMPLETE
REMAINING = nonidentity (F3)
            + F1 relation descent and existing-map identification
              on generic reciprocal/Ref_path/W3 arrows
            + sealed map-level Loc construction/linearity
```

## 5. X4 — battery

### 5.1 F_PLDEC circularity

[PROVABLE] The reader-free dependency separation is

```text
actual paths/currents + carrier metric
 -> Q-408 Kernbar and sigma_cyl
 -> finite Ward/C3 shadow and its pullbacks;

profile quotient
 -> algebraic reader family;

no arrow from reader/chi/T into the first branch.               (B1)
```

This is a dependency graph, not a claim about register chronology: the R4
reader artifact predates Q-408. Inside the Q-408 construction, Ward and
faithfulness are proved before the unchanged reader is applied/pulled
through the finite kernel map. Neither `(L2)`--`(L18)` nor `(Q1)`--`(Q23)`
uses a reader, `chi`, `T`, a response value, or a desired coefficient.
Therefore

```text
Q408_KERNEL_CONSTRUCTION_READER_FREE = PROVEN
FINITE_C3_DATUM_PULLBACK_READER_FREE = PROVEN
FACE_LOC_DECLARATION_HAS_NO_READER_DEPENDENCY = PROVEN_AS_DECLARATION
F1_ARGUMENT_READER_INDEPENDENT = PROVEN.                         (B2)
```

[PART-PROVABLE] The unbuilt physical map `(T6)`, and the face-declared
cochain map `(T5)` beyond its declaration, cannot receive a stronger
reader-independence status than their construction supplies. Defining the
missing `Loc` arrow law or either `(F1)` clause in `(Q6)` by demanding
agreement with the algebraic reader would be the killed F_PLDEC circular
pullback and is forbidden.

### 5.2 Anti-tuning ledger

| Forbidden adjustment | Execution here | Result |
|---|---|---|
| choose a localization lift to make `(LOC)` true | `(L9)`--`(L13)` is a fully disclosed abstract countermodel only; it is not installed at an actual stage | clean |
| delete logical target-complement modes | the explicit contractible coordinate in `(L9)` is retained throughout the logical test | clean |
| replace `eta_f^K` by an abstract operator transport | actual generator analyses use `(T7)`; `eta=id` occurs only in the disclosed abstract non-entailment model `(L9)` | clean |
| choose relations favorable to `(F1)` | `Rel_N=closure(ker qtilde_N)` is frozen with every mixed relation retained | clean |
| use `j_f^prof` circularly to prove its prequotient lift | the existing-map identification is separately required in `(Q6)` and rejected as an inference at `(Q18)` | clean |
| infer `Loc` from `P_H` naturality | logical control `(L11)`--`(L13)` prevents the inference | clean |
| use a reader or desired coefficient | absent from every construction and proof | clean |
| evaluate a number or measured constant | all scalars and profiles remain symbolic | clean |
| bind a member or run downstream machinery | none performed | clean |

### 5.3 Self verb audit

| Status/verb | Display supporting it | Audit |
|---|---|---|
| `PROVEN` on identities for `(LOC)` | `(L2)` | every intermediate equality displayed |
| `SUBSCOPE` for `Loc` naturality | stops `(L3)`, `(L8)`; conditional closure `(L16)`--`(L18)` | no nonidentity base case promoted |
| `non-entailment` | `(L9)`--`(L13)` | explicitly a logical completion model, not an actual refutation |
| `PROVEN` full `(F1)` on linear `A_iso` | relation descent and existing-map identity `(Q8)`--`(Q12)` | prequotient and quotient routes displayed |
| `PART-PROVABLE` generic reciprocal `(F1)` | stopped route `(Q12-RL)` | conditional isomorphism case not promoted to the whole generator class |
| `PART-PROVABLE` Ref_path `(F1)` | full-isomorphism algebra `(Q13)`--`(Q17)` preserves the named zero relation; general debt `(Q18)` remains | no new categorical W3 arrow installed |
| `INCOMPLETE` for J2 premises | two explicit question marks in `(J1)` plus `Loc` construction/linearity debt | exact remaining premises listed |
| `CLEAN` for the battery | `(B1)`--`(B2)` and anti-tuning ledger | every exclusion displayed |

```text
MACHINERY_APPEAL = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_bound = false
fixed_point_executed = false
end_test_run = false
numeric_evaluation = false
comparison_to_measured_constants = false
```

No register, plan, tracker, git, commit, push, member-binding, fixed-point,
end-test, or numerical-evaluation action was performed.

LOC_NATURALITY = SUBSCOPE (+maximal certified scope through Q-493 is the identity-arrow subcategory; no actual nonidentity equality is refuted)
F1_COMPANION = SUBSCOPE (+full on linear A_iso; generic reciprocal-loop and Ref_path/general-W3 relation descent plus existing-map identification remain open)
J2_RP_PREMISES = (+remaining: nonidentity F3; F1 descent/identification beyond linear A_iso; sealed map-level Loc construction/linearity)
VERB_AUDIT_SELF = CLEAN
