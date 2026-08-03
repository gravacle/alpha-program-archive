# STAGE 8 TASK 4B — CARRIER_METRIC_AND_UNITS ADOPTION PROPOSAL — LANE 2 V002

Date: 2026-08-03  
Task: PASTE 457 / Task 4b  
Lane: CODEX LANE 2  
Status: **PROPOSED_NOT_ADOPTED — FORCED SEMIFORM INSTALLED; VISIBLE-CURRENT QUOTIENT PROVED NATURAL; FULL DESCENT EXPOSES THE REMAINING CARRIER CHOICE**

```text
REGISTER_HEAD_AT_PREFLIGHT = Q-375
PREFLIGHT = PASS

LEAD_RESULT = FORCED_SEMIFORM_DERIVED

FINITE_FORCED_SEMIFORM:
  s_G(c,d)=g_A4(u_c,u_d) | TYPE-P | premises: DoR-015
  ker(s_G)=ker(I_K,G) | TYPE-P

INJECTIVITY_FROM_RATIFIED_CLAUSES = false | TYPE-R |
  test: R2 finite countermodel
ACTUAL_KERNEL_ZERO_AT_EVERY_STAGE = NO_VERDICT | TYPE-U |
  would-build: FULLNESS_CERT

VISIBLE_CURRENT_METRIC_CARRIER = K_G^vis:=K_G/ker(I_K,G)
VISIBLE_CURRENT_QUOTIENT_NONDEGENERATE = true | TYPE-P
VISIBLE_CURRENT_QUOTIENT_FAMILY_NATURAL = true | TYPE-P on certified maps

FULL_D_G_FACTORS_THROUGH_VISIBLE_CURRENT_QUOTIENT
  = iff ker(I_K,G)={0} | TYPE-P theorem
NONZERO_INTEGRAL_CURRENT_NULL_CYCLE_IF_PRESENT_IS_D_G_VISIBLE = true |
  TYPE-P theorem

A4_AUTOMORPHISM_ISOMETRY_DERIVED = false | TYPE-R
A4_RANK_PRESERVING_ISOMETRY_DERIVED = false | TYPE-R
A4_ISOMETRY_CERTIFICATE = PROPOSED_NOT_ADOPTED

R_A_UNIT = U_A^(-2)
R_A_INVERSE_UNIT = U_A^(2)

READY_FOR_CROSS_REVIEW = yes
READY_FOR_DOR019_RULING = no | unresolved full-carrier branch
DOR_019 = RESERVED

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

V002 narrows the authored territory.  The finite semiform is not proposed
physics; it is forced by the retained A4 form and the already-ratified cycle
current map.  The semiform becomes a positive metric on the visible-current
quotient without choice.  What remains for DoR-019 is completion, carrier
fullness or null-sector treatment, A4 isometry, the R5 carrier identification,
and units.

The R2 countermodel also exposes a boundary that V001 missed: a cycle may be
invisible as an A4 source current while remaining visible to the ratified
prefix-to-cycle descent.  Such a direction cannot be erased merely to obtain
a Riesz map.

---

## 0. Preflight, custody, and verified authorities

The live questions-settled register and sidecar were checked before work.
The head was exactly `Q-375`.  The required cross-review was hash-verified
before reading.

| Artifact | Verified SHA-256 | Use |
|---|---|---|
| carrier metric cross-review V001 | `55975bfa4358a720b9bffe091a6c5b246e6231d2d974dd4d270021040056eec5` | R1/R2/R4/R6/R7 kills and bounded repair |
| carrier metric proposal V001 | `657fa2bc5d0dcd81dbc3c6201bd5ec1ce9178ee7929b36d0b597ea7e00552386` | repaired baseline |
| DoR-015 / field signature V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | A4 form, cycle currents, quotient, zero extension |
| square V004 | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | R4 units, R5 carriers, automorphism/restriction cubes |
| DoR-017 decision | `ee9d81bf78ab0ac9361cad5b48dde2b6b8b1e9fb0e28a4fdbba41e1c43db3e45` | N member, symbolic `nu`, standing falsifier |
| divergence-datum descent | `c39de7a0ef5a29e92ded5fc961b54dfe933171ea291b221c38bf0aa3a9c0dcf3` | DP1–DP10 and executability boundary |

```text
DOES_THE_OBJECT_EXIST = yes | V002 repair target and forced semiform exist
IS_THE_VERSION_CURRENT = yes | Q-375
ARE_ITS_INPUTS_PRESENT = yes for the repair |
  no for proving FULLNESS_CERT, typed below

CUSTODY = builder repair; Lane 1 review required
STANDING = PROPOSED_NOT_ADOPTED
P_VERDICT_DECLARED = false
NUMERIC_RESPONSE_EVALUATED = false
ROOT_OR_K_STAR_EVALUATED = false
MEASURED_CONSTANT_COMPARISON = false
```

---

## 1. S1 — the forced semiform, installed as derived content

### 1.1 Inputs already in DoR-015

At every admitted finite realization `G`, V005 supplies

```text
K_G:=ker(B_G^T),
I_K,G:K_G->J_fin,G^005,
I_K,G(c):=u_c,
```

and the retained A4 Hilbert form `g_A4,G` on the finite current image.  No
metric choice is needed to compose these existing objects.

### 1.2 Forced definition

Define

```text
s_G:K_G x K_G->R,
s_G(c,d):=g_A4,G(I_K,G c,I_K,G d)
         =g_A4,G(u_c,u_d).                       (S1-1)
```

This is the pullback of a positive form, hence

```text
s_G(c,c)=||u_c||_A4^2>=0.                         (S1-2)
```

Moreover,

```text
s_G(c,c)=0
 iff ||I_K,G c||_A4=0
 iff I_K,G c=0,
```

so

```text
ker(s_G)=ker(I_K,G)=:N_G.                        (S1-3)
```

Equations `(S1-1)`–`(S1-3)` are derived content:

```text
FINITE_A4_PULLBACK_SEMIFORM_FORCED = true | TYPE-P |
  premises: DoR-015/V005
SEMIFORM_KERNEL_FORCED = true | TYPE-P
SEMIFORM_POSITIVE_DEFINITE_ON_FULL_K_G = NO_VERDICT | TYPE-U
```

### 1.3 What remains authored

The following are not contained in `(S1-1)`:

1. a proof that `N_G={0}` on every admitted stage and completion;
2. a decision whether `N_G` is quotiented, retained with a new positive
   metric, or shown absent by fullness;
3. a completion topology and completed carrier identification;
4. A4 automorphism and rank-preserving isometry;
5. carrier-unit torsors and their relation to R4 action units;
6. identification of R5 `C_prop` with the correct Hilbert dual.

These items, and only these items, comprise the DoR-019 residue.

---

## 2. S2 — injectivity audit and the R2 permanent countermodel

### 2.1 What V005 proves

V005's realized physical tangent is

```text
T_phys,G
 =image(L_G)/(image(L_G) intersection image(B_G))
 subset coker(B_G).                               (S2-1)
```

The family `{u_c:c in K_G}` separates points of `T_phys,G`.  This means

```text
t!=0 in T_phys,G => some c has u_c(t)!=0.         (S2-2)
```

It does not mean

```text
c!=0 in K_G => u_c!=0 on T_phys,G.                (S2-3)
```

The missing implication is equivalent to the finite fullness condition

```text
image(L_G)+image(B_G)=E_G,
equivalently T_phys,G=coker(B_G).                 (S2-4)
```

No ratified artifact proves `(S2-4)`.

### 2.2 Permanent R2 regression

Use the reviewer's admitted finite model:

```text
Q_G^lin=R^2,
K_G=R^2,
beta(q,c)=q^T c,
T_phys,G=span{e_1},
u_(c_1,c_2)(t e_1)=c_1 t.                        (S2-5)
```

The current family separates `T_phys,G`, but

```text
I_K,G(e_2)=u_e2=0,
N_G=span{e_2},
matrix(s_G)=diag(1,0).                            (S2-6)
```

Thus the semiform is degenerate and the full-carrier Riesz map asserted in
V001 does not exist.

```text
R2_COUNTERMODEL = INSTALLED_PERMANENT_REGRESSION
I_K_INJECTIVITY_DERIVABLE_FROM_V005 = false | TYPE-R
ACTUAL_I_K_KERNEL = NO_VERDICT | TYPE-U
```

### 2.3 The visible-current quotient

Define without choosing a complement:

```text
K_G^vis:=K_G/N_G,
pi_G:K_G->K_G^vis,

g_K,G^vis([c],[d]):=s_G(c,d).                    (S2-7)
```

Well-definedness follows because every `n in N_G` is in the radical of
`s_G`.  If `g_K,G^vis([c],[c])=0`, then `c in N_G`, hence `[c]=0`.
Therefore

```text
g_K,G^vis is positive definite.                  (S2-8)
```

This nondegeneracy is derived, not authored.

The corresponding finite Riesz map is

```text
R_K,G^vis:K_G^vis->(K_G^vis)^*,
(R_K,G^vis[c])([d])=g_K,G^vis([c],[d]).           (S2-9)
```

It is an isomorphism at finite dimension.  Its completed bounded
isomorphism remains conditional on the authored completion topology.

### 2.4 Family naturality of the quotient

For an admitted realization automorphism `alpha:G->G'`, current covariance
gives

```text
I_K,G' alpha_K=alpha_J I_K,G.                    (S2-10)
```

Since `alpha_J` is invertible,

```text
alpha_K(N_G)=N_G'.                               (S2-11)
```

Hence

```text
alpha_K^vis([c]):=[alpha_K c]                    (S2-12)
```

is well-defined and invertible.  No realization member is selected.

For every certified restriction/current square

```text
rho_J I_K,M=I_K,N rho_K,                         (S2-13)
```

one has `rho_K(N_M) subset N_N`, so

```text
rho_K^vis([c_M]):=[rho_K c_M]                    (S2-14)
```

is well-defined.  For a certified directed inclusion

```text
I_K,M j_K=j_J I_K,N,                             (S2-15)
```

the quotient inclusion exists.  It is injective whenever the retained
current inclusion `j_J` is injective, because

```text
j_K c in N_M
 =>j_J I_K,N c=0
 =>I_K,N c=0
 =>c in N_N.                                     (S2-16)
```

Thus the quotient is family-natural under automorphisms, restrictions, and
the certified rank-preserving inclusions.

### 2.5 What lives in `N_G`?

By definition,

```text
N_G=ann(T_phys,G) subset K_G.                    (S2-17)
```

Its elements carry no A4 source-current content on the realized tangent.
They are current-invisible.  They need not, however, be record-invisible on
the full Gate-4 quotient.

Write `K_G^Z` for the integral cycle lattice and `K_G` for its real carrier.
The ratified prefix-to-cycle descent is surjective onto the full character
quotient `Hom(K_G^Z,U(1))`, and its dual `D_G^*` is injective on `K_G^Z`.
Its tangent is surjective onto `K_G^*`.  Therefore

```text
0!=n in N_G cap K_G^Z => D_G^* n is nontrivial,
0!=n in N_G => some tangent value pairs nontrivially with n. (S2-18)
```

In the countermodel, `e_2` is precisely such a direction: it vanishes on
`T_phys,G=span{e_1}` but detects the second coordinate of the full quotient.

This is the first-order carrier distinction:

```text
CURRENT_INVISIBLE does not imply RECORD_INVISIBLE.
```

No actual nonzero `N_G` has been computed for the sealed stages; its
existence is `NO_VERDICT`.  But the ratified clauses admit it, and if it is
nonzero its elements are record-visible by `(S2-18)`.

### 2.6 Does `D_G` compose with the quotient?

The linear dual of `K_G^vis=K_G/N_G` consists of those tangent quotient
characters that annihilate `N_G`:

```text
(K_G^vis)^* isomorphic to N_G^perp subset K_G^*. (S2-19)
```

For the full tangent descent to factor as

```text
D_G^vis:Prefix_G->(K_G^vis)^*,                   (S2-20)
```

every tangent value of `D_G` would have to annihilate `N_G`.  Since the
tangent descent is surjective onto `K_G^*` on the edge-resolved family,
this happens iff

```text
N_G={0}.                                         (S2-21)
```

Equivalently, if `n!=0` lies in `N_G`, choose a tangent prefix family with
`D_G(Z)(n)!=0`; two representatives of `[n]=0` then receive different
linearized holonomy, so `(S2-20)` is not well-defined.  At group level the
same argument applies to every nonzero integral null cycle
`n in N_G cap K_G^Z`.  The R2 witness `e_2` is integral, so it exercises both
levels.

```text
D_G_FULL_FAMILY_FACTORS_THROUGH_K_VIS
 = iff N_G={0} | TYPE-P theorem
D_G_COMPOSITION_ON_N_ANNIHILATING_SUBFAMILY = true | TYPE-P
D_G_COMPOSITION_ON_FULL_NO_SELECTION_FAMILY = NO_VERDICT |
  equivalent to FULLNESS_CERT
```

Thus `K_G^vis` is a lawful metric carrier, but it cannot silently replace
the full record-visible `K_G` in the action-comparison square.  The full
R5 carrier choice remains a DoR-019 item.

---

## 3. The repaired two-level carrier account

V002 keeps both carriers explicit:

```text
K_G^rec :=K_G                         full record-visible cycle carrier;
N_G     :=ker(I_K,G)                  current-null subspace;
K_G^vis :=K_G^rec/N_G                 positive metric current carrier.
                                                        (S3-1)
```

The quotient projection is natural by `(S2-12)`–`(S2-16)`.  The full
prefix descent continues to consume `K_G^rec`; the forced metric and finite
Riesz map live on `K_G^vis`.

Three lawful closure routes remain:

1. **Fullness route:** prove `N_G=0` at every admitted stage and completion.
   Then `K_rec=K_vis`, and the descent and metric carriers coincide.
2. **Quotient route:** adopt `K_vis` as the metric carrier while retaining
   `N_G` as a separate nonmetric record sector.  This does not by itself
   close R5 on the full cycle carrier.
3. **Null-extension route:** retain full `K_rec` and author an independent
   positive, family-natural form `h_N` on `N_G`, with an invariant splitting
   or extension theorem, so `s_G+h_N` becomes positive without deleting
   record-visible content.

No route is selected here.

---

## 4. Repaired complement/dual carrier

### 4.1 Finite visible complement

The current family separates `T_phys,G`.  Its evaluation map is

```text
E_G:T_phys,G->(K_G^vis)^*,
E_G(t)([c])=u_c(t).                               (S4-1)
```

It is injective by separation.  At finite dimension, the rank of the
restricted current family equals `dim K_G^vis`, while separation gives
`rank(E_G)=dim T_phys,G`; therefore

```text
dim T_phys,G=dim K_G^vis,
E_G is an isomorphism.                            (S4-2)
```

Define the finite complement metric as the Hilbert-dual metric:

```text
C_G^vis:=T_phys,G,
g_C,G^vis(t,t'):=g_(Kvis^*)(E_G t,E_G t').        (S4-3)
```

This is positive and uses no representative or basis.

### 4.2 Completed/R5 carrier-identification residue

The finite isomorphisms `(S4-1)` do not prove that R5's completed
`C_prop` is exactly the Hilbert completion of `C_G^vis`, nor that R5's
`K_cycle` is `K_vis` rather than `K_rec`.  V002 therefore adds the explicit
certificate rather than assuming it:

```text
CARRIER_IDENTIFICATION_CERT := {
  completed K choice in {K_rec,K_vis,K_vis direct-sum N_metric};
  dense finite core and completion topology;
  completed E:C_prop->(K_metric)^*;
  injectivity, surjectivity, closed range;
  automorphism and restriction naturality;
  compatibility with D_017 and rho_H,N;
  explicit account of N_G and D_G.
}.                                                (S4-4)
```

```text
FINITE_VISIBLE_C_DUALITY = true | TYPE-P
COMPLETED_R5_CARRIER_IDENTIFICATION = PROPOSED_NOT_ADOPTED
```

---

## 5. S3 — A4 isometry theorem, honestly scoped

### 5.1 What follows from V005

V005 proves the current covariance and zero-extension squares:

```text
I_K,G' alpha_K=alpha_J I_K,G,
I_K,M j_K=j_J I_K,N.                             (S5-1)
```

It ratifies a Hilbert norm on the source-current completion.  It does not
prove

```text
g_A4,G'(alpha_J u,alpha_J v)=g_A4,G(u,v),         (S5-2)
```

or

```text
g_A4,M(j_J u,j_J v)=g_A4,N(u,v).                 (S5-3)
```

Covariance of labels is weaker than isometry of the norm.  The rank-two
counterform `diag(1,2)` remains a permanent witness: the exchange matrix
`P` gives `P^T diag(1,2)P=diag(2,1)`.

```text
A4_AUTOMORPHISM_ISOMETRY_FROM_V005 = false | TYPE-R
A4_RANK_PRESERVING_ISOMETRY_FROM_V005 = false | TYPE-R
```

### 5.2 The proposed failure-capable certificate

The metric gate therefore contains, rather than presupposes,

```text
A4_ISOMETRY_CERT := {
  for every admitted alpha,
    g_A4,G'(alpha_J u,alpha_J v)=g_A4,G(u,v);

  for every certified rank-preserving inclusion j,
    g_A4,M(j_J u,j_J v)=g_A4,N(u,v);

  for every restriction rho_J=j_J^* on that scope;

  reality reversal antiunitary after complexification;
  batching bounded, with isometry claimed only where independently proved;
  stabilizer invariance at every stage.
}.                                                (S5-4)
```

If `(S5-4)` is ratified, `(S5-1)` descends it to `K_vis`:

```text
g_K,G'^vis(alpha_K^vis[c],alpha_K^vis[d])
 =g_K,G^vis([c],[d]),                             (S5-5)
```

and similarly for rank-preserving inclusions.  This is now a conditional
proof from an explicit authored premise, not the premise restated as its own
proof.

### 5.3 Alternatives

The live alternatives are:

1. retain the A4 norm and author `(S5-4)` as a new law;
2. replace it by a family-natural invariant form, with equivalence to the
   retained A4 topology and every restriction square re-proved;
3. keep only bounded covariance, not isometry, and abandon orthogonal/Riesz
   propagation at the completed R5 level;
4. reject the metric package.

No invariantization by averaging is silently used: an average needs a
group, measure, stabilizer compatibility, and cross-stage theorem of its
own.

---

## 6. S4 — corrected unit algebra

Let a carrier vector in sector `A in {C,K}` carry unit `U_A`.  A scalar
covector in `A^*` carries `U_A^(-1)`.  Therefore

```text
R_A:A->A^*,
[R_A]=U_A^(-2),
[R_A^(-1)]=U_A^(2).                              (S6-1)
```

The complete corrected table is:

| Object | Unit |
|---|---|
| `a in A` | `U_A` |
| `ell in A^*` | `U_A^(-1)` |
| scalar metric `g_A(a,b)` | `1` |
| `R_A:A->A^*` | `U_A^(-2)` |
| `R_A^(-1):A^*->A` | `U_A^(2)` |
| action `phi` and `nu` | `U_action` |
| `D_A phi` | `U_action U_A^(-1)` |
| `D_A D_B phi:B->A^*` | `U_action U_A^(-1)U_B^(-1)` |
| `R_A^(-1)D_A phi` | `U_action U_A` |
| `R_A^(-1)D_A D_B phi` | `U_action U_A U_B^(-1)` |

Thus the inverse Riesz map—not the forward map—carries the positive square
of the carrier unit.  Every occurrence of the V001 assignment
`[R_A]=U_A^2` is withdrawn.

The unit torsors remain formal; no nonzero member, numerical scale, rank
ratio, or relation setting a carrier unit equal to `nu` is selected.

```text
R7_UNIT_REGRESSION = PASS
NU_FIXED_BY_CARRIER_UNITS = false
```

---

## 7. S5 — completed choice table and true DoR-019 content

| Field/decision | Proposed/live content | Alternatives | Minimality | Void condition |
|---|---|---|---|---|
| forced semiform | `s_G(c,d)=g_A4(u_c,u_d)` | none; derived | exact pullback of two ratified inputs | any modification or response-dependent term |
| `FULLNESS_CERT` | prove `image L_G+image B_G=E_G`, all stages and completion | fail/unknown | only theorem that identifies `K_rec=K_vis` without authorship | countermodel realized or completion loses fullness |
| visible-current quotient | `K_vis=K_rec/N_G`, metric `(S2-7)` | keep full semiform; add metric on null sector | minimal nondegenerate carrier forced by `s_G` | quotient called full physical carrier while `N_G!=0` or `D_G` fails to factor |
| null-sector treatment | retain `N_G` separately, or add positive natural `h_N` | delete it; prove it zero | preserves any D-visible current-null content | response support used, nonnatural splitting, or D-visible content erased |
| `CARRIER_IDENTIFICATION_CERT` | completed `C_prop` equals dual of the selected metric carrier on dense finite core | independent complement metric; nondual R5 carrier | makes the R5 seam explicit | not full, not onto, not natural, or wrong D_017 domain |
| A4 automorphism isometry | authored `(S5-4)` | invariant replacement; bounded covariance only | required for orthogonal automorphism transport | rank-two exchange/stabilizer changes norm |
| A4 stage isometry | rank-preserving current inclusions isometric; restrictions adjoints | contractive only; stage weights | exactly W3 scope, no cycle-creating upward map | explicit N≤M square fails |
| visible Riesz maps | finite derived; completed bounded isomorphisms after topology choice | rigged/unbounded dual | no Riesz claim on degenerate full carrier | kernel, nonclosed range, or wrong units |
| unit torsors | `U_C,U_K`, with `(S6-1)` and R4 action-unit typing | fixed numeric units; unrelated hidden scale | dimensional bookkeeping without normalization | fixes `nu` or any numeric response scale |
| cycle creation | old subspace retained; new quotient/null content disclosed | selected cycle basis; false upward quotient map | preserves Z7 and exposes new directions | old record content deleted or root naturality asserted |
| reject | no metric adoption | — | keeps present TYPE-U honestly | — |

### 7.1 Minimality re-argument

V001 incorrectly called a full dual-Hilbert package minimal.  V002's exact
minimal derived object is only

```text
(K_G,s_G,N_G,K_G^vis,g_K,G^vis).                 (S7-1)
```

Everything beyond `(S7-1)` is either a theorem to be proved (`FULLNESS_CERT`)
or an authored carrier choice.  In particular, the quotient alternative is
live but nonclosing for the full action square unless `D_G` factors.

### 7.2 DoR-019 alternatives, with no selection

| Option | Principal would ratify | Consequence |
|---|---|---|
| `F` — fullness | the fullness/completed identification theorem plus `(S5-4)` and units | `K_rec=K_vis`; full descent and positive metric share one carrier |
| `Q` — visible quotient | `K_vis` as metric carrier, `N` retained separately, plus completed `C_vis` duality | positive current metric exists; R5/full descent remains two-level until a null-sector consumer rule is added |
| `N` — positive null extension | family-natural positive `h_N`, carrier-only splitting/extension, plus `(S5-4)` and units | full `K_rec` obtains a metric without deleting D-visible null cycles |
| reject | no new carrier physics | forced semiform remains; jet/germ execution stays TYPE-U |

No option is recommended or selected.

---

## 8. Restriction, automorphism, and descent ledger

| Map | Kernel behavior | Quotient descent | Isometry standing | Full-descent standing |
|---|---|---|---|---|
| realization automorphism `alpha_K` | `alpha_K N_G=N_G'` | `alpha_K^vis` is well-defined and invertible | conditional on authored A4 certificate | full `D_G` covariance unchanged on `K_rec` |
| rank-preserving `j_K` | `j_K N_N subset N_M`; equality/preimage from injective `j_J` | quotient inclusion well-defined and injective | conditional on authored A4 stage isometry | sealed square retained |
| restriction `rho_K` | `rho_K N_M subset N_N` | quotient restriction well-defined | adjoint only after A4 stage isometry | contravariant direction retained |
| batching | kernel maps by current square | quotient map if square exists | bounded only; no generic isometry claimed | existing batching covariance retained |
| cycle-creating addition | old kernel/image and new kernel disclosed | stagewise quotient exists | no upward physical quotient is inferred | Z7 impossibility retained |
| prefix descent `D_G` | detects every nonzero element of `K_rec` by `D_G^*` injectivity | factors through `K_vis` iff `N_G=0` | not a metric claim | exact obstruction `(S2-21)` |
| `rho_Gamma,N` | action restriction, not carrier map | derivatives use selected quotient/full carrier | conditional | existing scalar square retained |
| `rho_H,N` | R5-generated class only | Riesz upgrade after metric branch and isometry | conditional | existing algebraic cube retained |

The already-proved algebraic `rho_Gamma,N` and `rho_H,N` cubes are not
withdrawn.  Only V001's unsupported upgrade of them to metric-isometric
cubes is withdrawn pending `(S5-4)` and the carrier branch.

---

## 9. DP1/DP7 executability, restated

The divergence-provenance certificate remains open.

### DP1

The forced semiform now supplies a derived finite carrier semitopology.  On
`K_vis` it supplies a positive finite metric.  It does not supply

```text
Div_G, delta_G, alpha_Div, the completed topology, or the selected carrier
branch and carrier units.
```

Therefore:

```text
DP1_METRIC_SUBCLAUSE = finite semiform executable | TYPE-P
DP1_POSITIVE_COMPLETED_CARRIER = TYPE-U | DoR-019 branch
DP1_DATUM = TYPE-U
```

### DP7

Automorphism and restriction actions descend to `K_vis` algebraically by
`(S2-12)`–`(S2-16)`.  Their isometry is conditional on `(S5-4)`.  Generator
naturality remains uninstantiated, and full `D_G` handoff is equivalent to
fullness if the quotient branch is used.

```text
DP7_QUOTIENT_NATURALITY = TYPE-P on certified maps
DP7_METRIC_ISOMETRY = TYPE-U | A4_ISOMETRY_CERT
DP7_GENERATOR_NATURALITY = TYPE-U
DP7_FULL_DESCENT_HANDOFF_ON_Q_BRANCH = TYPE-U | FULLNESS_CERT

DP1_DP10_DISCHARGED_BY_METRIC = false
```

---

## 10. S6 — hostile battery rerun

### B1 — response-support attack

No definition of `s_G`, `N_G`, or `K_vis` contains a Hessian, Schur block,
stationary root, `p`, or desired output.  A null-sector metric chosen for its
response effect violates the N-option's carrier-only clause.

```text
RESPONSE_SUPPORT_TUNING = NOT_FOUND | PASS
```

### B2 — hidden-scale attack

The corrected unit algebra separates carrier units from `U_action`; `nu`
remains symbolic.  Neither the semiform nor quotient fixes a numerical unit
torsor member.

```text
HIDDEN_NU_FIXING = NOT_FOUND | PASS
```

### B3 — R2 degeneracy regression

On `(S2-5)`, V002 computes

```text
s=diag(1,0), N=span(e_2), K_vis isomorphic to span([e_1]),
g_K^vis([e_1],[e_1])=1.
```

The quotient metric is nondegenerate; the full Riesz map is not claimed.

```text
R2_COUNTERMODEL = PASS
```

### B4 — record-visible-null regression

In the same model, a full quotient character with nonzero second coordinate
is detected by `e_2`, while `I_K(e_2)=0`.  V002 retains `e_2` in `K_rec` and
refuses to factor full `D_G` through `K_vis`.

```text
RECORD_VISIBLE_NULL_DELETED = false | PASS
```

### B5 — A4 anisotropic exchange

For `G_A4=diag(1,2)` and exchange `P`, V002 obtains
`P^T G_A4 P=diag(2,1)`.  The retained norm is not called isometric; the
candidate fails `(S5-4)` as required.

```text
A4_ISOMETRY_ASSUMED = false | PASS
```

### B6 — Riesz unit regression

`[R_A]=U_A^-2` and `[R_A^-1]=U_A^2` everywhere.  The V001 power is absent.

```text
R7_UNIT_POWER = PASS
```

### B7 — pendant/tree quotient

Pendant/tree coboundaries remain zero in the Gate-4 physical tangent.  The
visible quotient is formed after the current map and does not resurrect an
endpoint coordinate.

```text
PENDANT_GAUGE_REINTRODUCED = false | PASS
```

### B8 — cycle-creating upward-map attack

No metric adjoint is promoted to the physical upward quotient map refuted by
Z7.  Old/current/new kernel data are accounted stagewise; stationary-root
naturality is not inferred.

```text
Z7_BOUNDARY_RETAINED = true | PASS
```

### B9 — fresh attack: quotient/full-carrier equivocation

Replace `K_rec` by `K_vis` in R5 while still consuming full `D_G`.  If
`N_G!=0`, `(S2-21)` refutes the square.  V002 prevents the equivocation by
the two-level notation `(S3-1)` and the branch table.

```text
QUOTIENT_CALLED_FULL_WITHOUT_FULLNESS = false | PASS
```

### B10 — basis/splitting selection

`K_vis` is a quotient, not an orthogonal complement; no section
`K_vis->K_rec` is chosen.  The N option expressly requires any future
splitting to be family-natural and separately ratified.

```text
NULL_COMPLEMENT_SELECTED = false | PASS
```

---

## 11. Delta table — V001 to V002

| V001 clause | V002 repair | Review item |
|---|---|---|
| full metric treated as one authored package | forced finite semiform `(S1-1)` premise-marked derived; authorship residue separated | R1 |
| `I_K` injective asserted | injectivity derivability refuted; R2 countermodel permanent | R2 |
| no quotient carrier alternative | `K_vis=K/ker I_K` built with positive metric | R2/R6 |
| quotient implicitly full physical carrier | two-level `K_rec/K_vis`; full `D_G` factorization iff kernel zero | R2 |
| completed `I_C` asserted | finite `E_G` proved; completed `CARRIER_IDENTIFICATION_CERT` explicit | R2/R6 |
| A4 covariance used as isometry | derivation withdrawn; `A4_ISOMETRY_CERT` authored with alternatives/void | R4 |
| rank-preserving isometry asserted | conditional on authored stage-isometry clause | R4 |
| `[R_A]=U_A^2` | `[R_A]=U_A^-2`, inverse carries `U_A^2`; all derivative units propagated | R7 |
| choice table omitted fullness/null branch | F/Q/N/reject alternatives added | R6 |
| DP boundary broad | DP1 semiform and DP7 quotient naturality exact; remaining clauses typed | R5/S6 |
| response-support/hidden-scale battery | preserved and rerun | R3 |
| doors | preserved; full-descent/null-sector obstruction added | R5 |

Everything from V001 that passed R3 and R5 is retained in substance:
response-independent provenance, symbolic `nu`, no selected basis/frame/
filtration/member, the Z7 boundary, and the open divergence/germ doors.

---

## 12. Final board and standing falsifier

The forced content is now exact:

```text
s_G(c,d)=g_A4(u_c,u_d),
N_G=ker I_K,G,
K_G^vis=K_G/N_G,
g_K^vis([c],[d])=s_G(c,d).
```

The proposal is void if any downstream use:

1. modifies the forced semiform;
2. calls it positive definite on full `K_G` without `FULLNESS_CERT`;
3. deletes a nonzero element of `N_G` while full `D_G` still detects it;
4. assumes A4 isometry without `(S5-4)`;
5. identifies completed `C_prop` without `(S4-4)`;
6. reverses the Riesz unit power;
7. fixes `nu` or a numerical carrier scale;
8. selects a metric/null branch for a response consequence;
9. invents the forbidden cycle-creating upward quotient map.

```text
CARRIER_METRIC_V002 = COMPLETE_BOUNDED_REPAIR
FORCED_SEMIFORM = INSTALLED_DERIVED
VISIBLE_CURRENT_QUOTIENT = CONSTRUCTED
QUOTIENT_FAMILY_NATURALITY = PROVED
FULL_DESCENT_FACTOR_THEOREM = PROVED_WITH_FULLNESS_BOUNDARY
A4_ISOMETRY = AUTHORED_RESIDUE_DISCLOSED
R7_UNIT_ALGEBRA = CORRECTED
CHOICE_TABLE = COMPLETE_FOR_F_Q_N_REJECT
DP1_DP7_EXECUTABILITY = RESTATED
BATTERY = 10_ATTACKS_RUN

READY_FOR_CROSS_REVIEW = yes
READY_FOR_DOR019_RULING = no | cross-review and carrier branch required
PROPOSAL_STANDING = PROPOSED_NOT_ADOPTED
DOR_019 = RESERVED

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
