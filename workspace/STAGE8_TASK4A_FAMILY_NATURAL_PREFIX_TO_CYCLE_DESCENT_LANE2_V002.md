# STAGE8 TASK 4A: FAMILY-NATURAL PREFIX-TO-CYCLE DESCENT — CODEX LANE 2 V002

Date: 2026-08-03  
Task: PASTE 436 / Task 4a / descent scope repair and P-432-3 derivation  
Lane: CODEX LANE 2  
Register head: Q-353  
Custody: builder repair; returns to Lane 1 for final review

```text
LEAD_RESULT = REPAIRED_FOR_FINAL_REVIEW
DESCENT_V002 = READY_FOR_FINAL_REVIEW

FIXED_STAGE_DESCENT = CONFIRMED_AND_UNCHANGED
LAWFUL_KERNEL = Gate-4 vertex rephasing only
NO_RECORD_VISIBLE_CYCLE_DELETED = true | TYPE-P

UPWARD_NATURALITY = PASS | TYPE-P |
  scope: cycle-rank-preserving identity extensions only;
  construction: inverse of the physical contravariant restriction isomorphism

CYCLE_CREATING_UPWARD_MAP = IMPOSSIBLE | TYPE-R |
  witness: one-edge tree plus an identity parallel edge

RANK1_SPLIT = PROVED |
  D=T^char on the sealed square and its j_NM^Q zero-extension image;
  no component-level equality off that image;
  permanent witness: cycle characters 1, pendant character w!=1

P_432_3 = CLOSED_BY_DERIVATION | TYPE-P |
  DoR-015 forces every physical scalar/action consumer to factor through
  the Gate-4 quotient; therefore it consumes D, while T^char remains only
  on its sealed square / zero-extension scope

ACTION_OR_2PI_COMPARISON_SQUARE = NOT_BUILT / TYPE-U
NON_EDGE_RESOLVED_EXTENSION = NOT_BUILT / TYPE-U

JOINT_INFORMATION_LAYER = COHERENT |
  D at every finite signed edge-resolved rank;
  T^char on its sealed rank-0/1 scope;
  restriction-natural agreement on im(j_NM^Q);
  permanent off-image disagreement theorem

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The repair changes scope, not the descent formula. The cross-review confirmed
the formula, kernel theorem, S8-A survival, contravariant restriction,
boundary, and selection scan. Those results are carried below without
mathematical alteration. The two killed statements are removed: there is no
upward quotient map across a cycle-creating identity addition, and there is
no full-component merge with the terminal-character family.

---

## 0. Preflight, authorities, and custody

### 0.1 Mandatory preflight

The kill determination was hash-verified before reading:

```text
reviewed_artifact =
  STAGE8_TASK4A_DESCENT_CROSS_REVIEW_LANE1_V001.md
expected_sha256 =
  58b5aef03ac43f365bfbc805bd659c7e6012d3cd292ac1ae9183b4ab9788a2b9
actual_sha256 =
  58b5aef03ac43f365bfbc805bd659c7e6012d3cd292ac1ae9183b4ab9788a2b9
sidecar = PASS

DOES_THE_OBJECT_EXIST = yes | bounded successor commissioned by Q-353
IS_THE_VERSION_CURRENT = yes | live register head Q-353
ARE_THE_INPUTS_PRESENT = yes | all named authorities verified
PREFLIGHT = PASS
```

`LOCKED_PROCESS.md` was read in full. This lane edits no reviewer-owned
register, plan, tracker, observation, continuation, or git state.

### 0.2 Load-bearing authorities

| Authority | Verified SHA-256 | Use |
|---|---|---|
| descent V001 | `5c5d2c828a62e302920c827e95678c9e9e00b2fdc1a2415c553383fcbbfe3a84` | confirmed core and the two claims repaired here |
| descent cross-review | `58b5aef03ac43f365bfbc805bd659c7e6012d3cd292ac1ae9183b4ab9788a2b9` | bounded kills Z4/Z7 and exact repair boundary |
| extension V002 | `eb3675d525af7d1420c4ed033a5e5b94eb7494c1bac1305029b25ac9169567a0` | corrected `j_NM^Q` square and scoped rank-one family |
| extension V002 cross-review | `d5cccfae3227597827a95c3e1791dcb834e5c84874304c74c5d533e83f20d995` | V002 confirmed; two mathematical seams closed |
| DoR-015 / FIELD_SIGNATURE V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | physical Gate-4 quotient and consumer typing |
| DoR-016 / network law V004 | `69f4d93b9f84075a3112fb011b9838f380fb8c0341610572170cf7a13d5aed08` | prefix trace family and doubled CTP source |
| Q-313 Map 1 | `ea8f4e9a79a9e4aca4a0b9e9aab470d78cd4d9c78794c20d9e979c0db16fbeab` | sealed primitive-square character map |

### 0.3 Register sweep

The following settled entries were re-read: Q-313, Q-315, Q-341,
Q-343, and Q-348 through Q-353. The new binding facts are:

```text
Q351 = extension V002 built with j_NM^Q
Q352 = descent V001 built and edge-resolved boundary stated
Q353 = descent core confirmed; Z4/Z7 killed; exact split proved
```

### 0.4 Symbols whose collision matters

```text
j_NM^Q       = source-side zero-extension Q_rel,N -> Q_rel,M;
rho_f        = target-side contravariant restriction Q_M -> Q_N;
j_NM^phys    = target-side upward map, present only when rho_f is an
               isomorphism on the cycle quotient;
D_G          = prefix-family -> Gate-4 physical cycle quotient descent;
T_G^char     = terminal-character map fixed by Hol_c T=Z on its rank-one
               component;
Q_G          = U(1)^(E_G)/Gamma_G = Hom(C_G,U(1));
Gamma_G      = Gate-4 vertex-rephasing subgroup;
C_G          = ker(B_G^T) intersect Z^(E_G).
```

`j_NM^Q` is not `j_NM^phys`. Extension V002 repairs the former. This
artifact constructs the latter only on the exact class where the physical
restriction is an isomorphism.

---

## 1. Delta table against V001

| Delta | V001 | V002 | Reason |
|---|---|---|---|
| D01 | register Q-350; relay 432 pending | register Q-353; V002 and both reviews in force | currency |
| D02 | P-432-1 pending full rank-one family agreement | agreement only on sealed square and `im(j_NM^Q)`; permanent pendant disagreement installed | Q-353 Z4 |
| D03 | P-432-2 pending comparison | restriction square closed on `im(j_NM^Q)`; no component merge | confirmed V002 + Q-353 split |
| D04 | P-432-3 pending external merge | closed by DoR-015 typing theorem; physical consumer must use `D` | S3 derivation below |
| D05 | unrestricted identity-zero-extension certificate | upward naturality only for cycle-rank-preserving identity extensions | Q-353 Z7 |
| D06 | target upward map asserted by appending edge coordinate one | target map defined as inverse of the quotient restriction isomorphism | representative independence |
| D07 | no cycle-creating impossibility theorem | Z7 theorem installed verbatim as a permanent non-certificate | requested repair |
| D08 | rank-one agreement text implied attached tree cells were always identity | equality scoped to the actual zero-extension image | pendant regression |
| D09 | identity regression globally PASS | split into rank-preserving PASS and cycle-creating TYPE-R impossibility | exact scope |
| D10 | joint foundation pending | coherent split layer; comparison/action content still TYPE-U | final board |

Everything else confirmed by the review is preserved in substance and in
the displayed formulas below: fixed-stage formula and well-definedness,
kernel/image theorem, S8-A calculation, contravariant cellular restriction,
batching, reality covariance, edge-resolved boundary, `iota` family, and the
selection/door account. No equation among those confirmed results is changed.

```text
CONFIRMED_CORE_MATHEMATICS_CHANGED = false
KILLED_SCOPE_CLAIMS_RETAINED = false
NEW_PHYSICAL_MEMBER_SELECTED = false
```

---

## 2. The confirmed fixed-stage descent, carried unchanged

### 2.1 Domain and formula

For a finite connected realized graph `G`, retain every signed enumeration

```text
eta=(epsilon,s),
epsilon:{1,...,N}->E_G a bijection,
s_j in {+1,-1}.
```

For `Z_0=1`, prefix inversion is

```text
r_j=Z_(j-1)^(-1)Z_j,                              (2.1)
Z_m=product_(j=1)^m r_j.                          (2.2)
```

The no-selection family remains

```text
P_G^fam := (disjoint union_eta P_eta)/~,
(eta,Z)~(eta omega^(-1),J_omega Z),               (2.3)
```

where `J_omega=Pi_N compose omega compose Pi_N^(-1)` is the forced signed
permutation of prefix coordinates. Recover the edge cochain by

```text
Phi_eta(Z)=h in A_G,
h_(epsilon(j)):=r_j^(s_j),                         (2.4)

D_G([eta,Z]):=q_G(Phi_eta(Z)).                    (2.5)
```

Equivalently, without selecting a cycle basis,

```text
Hol_G(D_G([eta,Z]))(c)
 =product_(j=1)^N r_j^(s_j c_(epsilon(j)))
 for every c in C_G.                               (2.6)
```

The cross-review confirmed `(2.1)`–`(2.6)`. Under a simultaneous signed
presentation change,

```text
r'_j=r_k^(tau_j),
epsilon'(j)=epsilon(k),
s'_j=tau_j s_k,

h'_(epsilon'(j))
 =(r'_j)^(s'_j)
 =(r_k^tau_j)^(tau_j s_k)
 =r_k^(s_k)
 =h_(epsilon(k)).                                  (2.7)
```

Thus no realization, edge order, orientation, or cycle basis is selected.

### 2.2 Confirmed kernel and image theorem

On a fixed signed edge-resolved realization,

```text
Phi_G:P_G^fam -> A_G=U(1)^(E_G)
```

is an isomorphism. Applying the Gate-4 quotient gives

```text
D_G=q_G compose Phi_G,
ker(D_G)=Phi_G^(-1)(Gamma_G).                      (2.8)
```

Both `Phi_G` and `q_G` are surjective, so `D_G` is surjective. Its dual is

```text
D_G^*:C_G -> Hom(P_G^fam,U(1)),
(D_G^*c)(Z)=Hol_G(D_G(Z))(c).                     (2.9)
```

If `D_G^*c` is trivial, surjectivity makes `Hol_G(q)(c)=1` for every
`q in Q_G`; DoR-015/V005 separation gives `c=0`. Hence

```text
ker(D_G^*)={0}.                                   (2.10)
```

No record-visible cycle is deleted at any finite edge-resolved rank.

### 2.3 Confirmed contravariant cellular restriction

For a declared signed chain map

```text
f_1:C_1(G_N)->C_1(G_M),
partial_M f_1=f_0 partial_N,                      (2.11)
```

the edge-cochain pullback is

```text
(f_1^*h_M)(e)=h_M(f_1e).                          (2.12)
```

For a fine vertex coboundary,

```text
f_1^*(delta_M g)=delta_N(f_0^*g),                 (2.13)
```

so pullback descends to `rho_f:Q_M->Q_N`. Recovering ratios, applying
`f_1^*`, and re-prefixing defines `P_f`, and direct substitution gives

```text
D_N P_f
 =q_N f_1^* Phi_M
 =rho_f q_M Phi_M
 =rho_f D_M.                                      (2.14)
```

This is the lawful general direction. It remains confirmed for every
declared signed cellular arrow, including those that create cycles.

### 2.4 Confirmed batching and reality

For a signed batch `[a,b]`,

```text
r_[a,b]=product_(j=a)^b r_j^(sign_j),             (2.15)
```

and for an unsigned consecutive batch,

```text
r_[a,b]=Z_(a-1)^(-1)Z_b.                          (2.16)
```

This is exactly the cochain pullback in `(2.12)`. Conjugation sends

```text
Z_m->conjugate(Z_m),
r_j->conjugate(r_j),
h_e->conjugate(h_e),
```

and therefore

```text
D_G(Theta_P Z)=Theta_G D_G(Z).                    (2.17)
```

This is covariance, not pointwise invariance.

---

## 3. S1 — repaired upward naturality

### 3.1 Exact admissible class

Let `i:G_N->G_M` be a declared identity extension: old edge characters are
unchanged and each added source character is one. V002 claims an upward
physical map only when the extension is cycle-rank-preserving:

```text
rank(C_M)=rank(C_N).                               (3.1)
```

For an injective graph identity extension, `i_*:C_N->C_M` is injective.
Under `(3.1)` the added-edge subgraph is a relative forest: if an added edge
lay on a new integral cycle, that cycle would be independent of the old
edge-supported cycle lattice and would raise its rank. Leaf elimination on
that relative forest forces every conserved integral chain to have zero
coefficient on every added edge. Consequently

```text
C_M=i_*(C_N)                                      (3.1a)
```

as integral lattices, not merely after tensoring with the reals. Thus `i_*`
is an isomorphism. Equivalently, every added edge lies in the relative
forest/bridge sector and introduces no conserved cycle direction.

DoR-015 identifies

```text
Q_G isomorphic to Hom(C_G,U(1)).                  (3.2)
```

The already-confirmed restriction is precomposition with `i_*`:

```text
rho_i:Q_M->Q_N,
rho_i(chi_M)=chi_M compose i_*.                   (3.3)
```

Since `i_*` is an isomorphism, so is `rho_i`. Define—not by choosing an
edge representative, but intrinsically—

```text
j_NM^phys := rho_i^(-1):Q_N->Q_M.                 (3.4)
```

This definition is representative-independent and selects no forest gauge.

### 3.2 Commuting square

Let `j_NM^prefix` be the source identity extension. For `c_M=i_*c_N`, the
added identity characters contribute one, so

```text
Hol_M(D_M j_NM^prefix Z)(i_*c_N)
 =Hol_N(D_N Z)(c_N).                              (3.5)
```

By separation of all cycle characters and `(3.4)`,

```text
D_M compose j_NM^prefix
 =j_NM^phys compose D_N.                          (3.6)
```

This proves upward naturality on the entire claimed class.

```text
CYCLE_RANK_PRESERVING_IDENTITY_EXTENSION = PASS | TYPE-P
TARGET_UPWARD_MAP = inverse physical restriction isomorphism
REPRESENTATIVE_APPENDING_USED_AS_DEFINITION = false | TYPE-R
```

### 3.3 Z7 impossibility theorem — verbatim non-certificate

The following theorem text is carried verbatim from the Q-353 cross-review
and is a permanent non-certificate, not a defect to repair by choosing a
gauge:

#### 3.3.1 Attack construction

Start with the connected one-edge tree

```text
G_N: s --e--> t.                                  (Z7-1)
```

Its edge-cochain quotient is a point:

```text
Q_N=U(1)^{\{e\}}/U(1)^{\{s,t\}}={*}.             (Z7-2)
```

Now add a second parallel edge `a:s->t`, declared to carry the identity
source character:

```text
G_M: s ==(e,a)==> t,
h_a=1.                                            (Z7-3)
```

The new graph has one cycle. Its quotient is detected by

```text
H([h_e,h_a])=h_e h_a^(-1).                        (Z7-4)
```

#### 3.3.2 Representative-independence fails

In `Q_N`, the old edge representatives `h_e=1` and `h_e=w` are gauge
equivalent for every `w in U(1)`. Appending the coordinate `1` gives

```text
[1]   -> [1,1], whose H is 1;
[w]   -> [w,1], whose H is w.                     (Z7-5)
```

For `w!=1`, the two target classes differ. Hence

```text
[h_e] |-> [h_e,1]                                 (Z7-6)
```

is not a well-defined function `Q_N->Q_M`.

#### 3.3.3 The displayed descent square cannot be repaired by another target map

At source level, let the old relative character be `r_e=w` and append the
identity character `r_a=1`. Then

```text
D_N(w)=*                                          (Z7-7)
```

for every `w`, while

```text
Hol(D_M(w,1))=w.                                  (Z7-8)
```

Any function from the one-point `Q_N` to `Q_M` has one fixed value, so no
target map `j_NM^Q,phys` can satisfy

```text
D_M j_NM^prefix=j_NM^Q,phys D_N                  (Z7-9)
```

for all `w`.

This does not refute contravariant restriction `rho_f:Q_M->Q_N`, which is
the unique map to the point and still satisfies `(Z4-5)`. It refutes only
the artifact's unscoped upward identity-extension certificate. The
certificate can survive on cycle-rank-preserving extensions for which a
quotient-compatible target inclusion is separately proved.

```text
FRESH_ATTACK = cycle-creating identity edge
RESULT = KILL
Z7 = KILL
```

In V002 this is recorded as:

```text
CYCLE_CREATING_IDENTITY_EXTENSION_UPWARD_MAP = false | TYPE-R
Z7 = INSTALLED_PERMANENT_REGRESSION
```

Contravariant restriction `(2.14)` remains valid. No upward story is claimed
when cycle rank grows.

---

## 4. S2 — corrected rank-one agreement and permanent split

### 4.1 Sealed-square agreement

For the sealed square, the primitive traversal is

```text
c_square=(1,-1,1,-1).
```

With `s_j=c_(epsilon(j))`,

```text
Hol_(c_square)(D_G(Z))
 =product_j (r_j^(s_j))^(c_(epsilon(j)))
 =product_j r_j
 =Z_N.                                            (4.1)
```

Q-313 uniqueness under `Hol_c T=Z_N` gives

```text
D_(G_square)=Hol_(c_square)^(-1) compose Z_N
            =T_N^char.                            (4.2)
```

This is exact.

### 4.2 Agreement on the repaired zero-extension image

For a cycle-rank-preserving extension from the sealed component, extension
V002 proves

```text
rho_G,MN compose T_M^char compose j_NM^Q=T_N^char. (4.3)
```

Section 3 proves

```text
rho_G,MN compose D_M compose j_NM^Q=D_N.          (4.4)
```

Here `rho_G,MN` is an isomorphism, and `(4.2)` identifies the right-hand
sides. Therefore

```text
D_M compose j_NM^Q
 =T_M^char compose j_NM^Q.                        (4.5)
```

Thus the merge is exact on `im(j_NM^Q)`, and only there is it certified.

### 4.3 Pendant disagreement — permanent regression

Take a connected rank-one graph consisting of one cycle plus a pendant tree
edge `t`. Set

```text
r_e=1 for every cycle edge e,
r_t=w with w in U(1), w!=1.                       (4.6)
```

For the physical descent, every cycle holonomy is one:

```text
Hol_c(D_M(Z))=1.                                  (4.7)
```

The pendant coordinate is a vertex coboundary and disappears in `Q_G`.
For the terminal-character component,

```text
Z_M=product_e r_e=w,
Hol_c(T_M^char(Z))=w.                             (4.8)
```

Hence

```text
D_M(Z) != T_M^char(Z) for w!=1.                  (4.9)
```

The witness is outside `im(j_NM^Q)` because zero-extension fixes the new
pendant character to one. It refutes component-level equality but does not
disturb either map on its proven scope.

```text
PENDANT_W_NOT_1_REGRESSION = PASS
FULL_RANK1_COMPONENT_MERGE = false | TYPE-R
AGREEMENT_ON_IM_J_NM_Q = true | TYPE-P
SEALED_SQUARE_AGREEMENT = true | TYPE-P
```

The exact split is now part of the object, not a footnote.

---

## 5. S3 — P-432-3 derivation from DoR-015 typing

### 5.1 Ratified typing chain

DoR-015/V005 states, in its physical-carrier construction:

```text
Q_N = U(1)^(E_N)/Gamma_N,
K_N=q_N compose H_N,

physical = framed /
  (Gate-4 vertex rephasing + all-finite path-invisible content).
```

It further fixes the physical current family as

```text
{u_c:c in ker(B_N^T)},
```

and its consumer audit requires:

```text
physical outputs use only quotient classes;
A4 consumes ker(B_N^T) conserved currents only;
A5 consumes C(Q_N) invariant cylinders and cycle phases only;
A6 consumes the quotient source domain only;
no bare open-edge scalar is consumed as a gauge-invariant output.
```

It also proves that on a connected tree `coker(B_N)=0`: tree phases are
Gate-4 gauge. These are not optional conventions after DoR-015; they are the
ratified typing of the physical field layer.

### 5.2 Universal-property theorem

Let `A_G` denote the future action-comparison component at finite stage `G`.
Because it is a **physical** scalar/action consumer under DoR-015, its source
leg must be constant on every `Gamma_G` orbit. Equivalently, its source leg
must coequalize vertex rephasing and therefore factor through

```text
q_G:A_G_edge->Q_G.                                (5.1)
```

The descent `D_G=q_G Phi_G` has exactly that property, and its kernel theorem
shows it removes no more than the required gauge:

```text
ker(D_G)=Phi_G^(-1)(Gamma_G).                     (5.2)
```

By contrast, the pendant witness `(4.6)`–`(4.9)` gives two histories with the
same physical Gate-4 class but different full-component `T_M^char` output.
Thus any action leg consuming `T_M^char` on that full component would vary
on a DoR-015 gauge orbit. It would be a nonphysical presentation consumer
forbidden by the ratified carrier typing.

Therefore:

```text
THEOREM_DOR015_FORCED_ACTION_INPUT:
  Every DoR-015-compatible physical action-comparison square on the
  edge-resolved family consumes the physical quotient descent D_G.

  T_G^char may be substituted only on the sealed square or an admitted
  zero-extension image where equation (4.5) proves T_G^char=D_G.

  A full-component T_G^char action input would require changing DoR-015 by
  retaining vertex-coboundary/tree data as physical; that is not a live
  choice under the frozen authority.
```

No genuine ratification choice remains at this seam. Choosing `T^char`
because of a later result would both violate DoR-015 and be target tuning.

```text
P_432_3 = CLOSED_BY_DERIVATION | TYPE-P |
  premise: DoR-015 / FIELD_SIGNATURE_PHYS V005

ACTION_COMPARISON_INPUT_CARRIER = Q_G via D_G
T_CHAR_RETAINED_SCOPE = sealed square + im(j_NM^Q)
GAUGE_BREAKING_ALTERNATIVE_LIVE = false | TYPE-R
```

### 5.3 What this theorem does not build

The theorem fixes the input carrier and map. It does not construct the
action functional, a 2PI Hessian, inverse/Schur blocks, a stationary point,
or a physical response:

```text
ACTION_COMPARISON_SQUARE = NOT_BUILT / TYPE-U |
  would-build: a quotient-natural scalar/action map on Q_G satisfying the
               all-jet finite restrictions and the action-side certificates

STATIONARY_2PI_DESCENT = NOT_BUILT / TYPE-U
PHYSICAL_P_VERDICT = NO_VERDICT
```

The input typing is derived; the consumer remains unbuilt.

---

## 6. S4 — full permanent regression suite

### 6.1 Pendant `w!=1`

Equations `(4.6)`–`(4.9)` recompute:

```text
D=1 on the unique cycle coordinate;
T^char=w;
w!=1;
FULL_COMPONENT_EQUALITY = REFUTED.
```

The difference is exactly tree/gauge content.

### 6.2 Cycle-creating identity edge

The one-edge tree has `Q_N={*}`. Adding a parallel identity edge produces a
rank-one quotient with holonomy `h_e h_a^(-1)`. Old representatives `1` and
`w` map to target holonomies `1` and `w`. Hence no representative-independent
upward map exists.

```text
CYCLE_CREATING_UPWARD_CERTIFICATE = REFUTED | TYPE-R
CONTRAVARIANT_RESTRICTION = PASS
```

### 6.3 S8-A `c_3` covariant survival — unchanged

With edge order `(a,b,d)`, retain

```text
c_1=(1,1,0),
c_2=(0,1,1),
c_3=(1,0,-1)=c_1-c_2.                            (6.1)
```

Prefix inversion gives

```text
r_a=Z_1,
r_b=Z_1^(-1)Z_2,
r_d=Z_2^(-1)Z_3.                                 (6.2)
```

The cycle characters remain

```text
H_(c_1)=r_a r_b=Z_2,
H_(c_2)=r_b r_d=Z_1^(-1)Z_3,
H_(c_3)=r_a r_d^(-1)=Z_1 Z_2 Z_3^(-1).           (6.3)
```

Under `a<->d`,

```text
H_(c_1)'=H_(c_2),
H_(c_2)'=H_(c_1),
H_(c_3)'=H_(c_3)^(-1).                            (6.4)
```

Thus `c_3` is inverted covariantly, never deleted.

```text
S8A_C3_SURVIVAL = PASS
S8A_AUTOMORPHISM_COVARIANCE = PASS
```

### 6.4 One edge

For a connected one-edge tree,

```text
C_G={0},
Q_G={*}.
```

The prefix character may be nonidentity, and DoR-016 keeps its endpoint-
covariant access upstream; `D_G` lands at the point because the edge phase
is a vertex coboundary.

```text
ONE_EDGE_DESCENT = zero cycle class | PASS
ONE_EDGE_ACCESS_DELETED_UPSTREAM = false | TYPE-R
```

### 6.5 Reality, batching, and restriction

```text
REALITY_REGRESSION = PASS | equation (2.17)
BATCHING_REGRESSION = PASS | equations (2.15)-(2.16)
GENERAL_RESTRICTION_REGRESSION = PASS | equation (2.14)
RANK_PRESERVING_UPWARD_REGRESSION = PASS | equation (3.6)
```

### 6.6 Fresh hostile attack: a terminal consumer after quotienting

**Attack.** Let the future physical action first consume `D_G`, then recover
the full terminal product—including a pendant character—from the quotient.

**Result.** Refuted. The quotient identifies every pendant/tree coboundary;
two prefix histories differing only by `(4.6)` have the same `D_G` output.
No function of `D_G` can recover `w`. This is the lawful information loss
mandated by DoR-015, not a missing inverse.

```text
PENDANT_RECOVERY_FROM_PHYSICAL_QUOTIENT = false | TYPE-R
NO_RECORD_VISIBLE_CYCLE_LOST = true | TYPE-P
```

The attack confirms the direction of P-432-3: physical comparison may not
silently re-import the discarded gauge coordinate.

---

## 7. S5 — boundary, `iota` family, selections, and doors

### 7.1 Edge-resolved boundary unchanged

If a raw history lacks a declared signed map from its cell lattice to the
realized edge-chain lattice, the general structural candidate remains

```text
iota_G:C_G->Z^N,                                  (7.1)

Hol_G(D_iota(r))(c)
 =product_(j=1)^N r_j^((iota_G c)_j).             (7.2)
```

The exact no-deletion criterion remains

```text
ker(iota_G restricted to C_G)={0}.                (7.3)
```

The residual family is unchanged:

```text
Iota_G^adm={iota_G:C_G->Z^N integral, injective,
            family-natural under every admitted arrow}.        (7.4)
```

No ratified member is supplied outside the signed edge-resolved family.

```text
EDGE_RESOLVED_FULL_FAMILY = CONSTRUCTED | TYPE-P
NON_EDGE_RESOLVED_HISTORY_FAMILY = NO_CONSTRUCTION / TYPE-U
MISSING_INPUT = family-natural signed chain realization iota_G
RESIDUAL_FAMILY = Iota_G^adm
```

### 7.2 No-selection audit unchanged

```text
realization member selected = false | TYPE-S
edge selected = false | TYPE-S
orientation member selected = false | TYPE-S
frame selected = false | TYPE-S
filtration selected = false | TYPE-S
cycle basis selected = false | TYPE-S
spanning tree selected = false | TYPE-S
rank or rank ratio selected = false | TYPE-S
character orientation n selected = false | TYPE-S
joint contraction selected = false | TYPE-S
p evaluated = false | TYPE-S
```

The repair introduces no new member, gauge, tree, basis, or orientation.

### 7.3 Six-account rows

```text
DOOR_PREFIX_FAMILY_QUOTIENT := (
  input_class = disjoint union of finite signed prefix presentations,
  equivalence = simultaneous signed relabeling by J_omega,
  topology = finite compact product topology,
  kernel = presentation equivalence only,
  image = edge-cochain torus A_G,
  sector_transfer = relative cell character -> oriented edge cochain,
  restriction_square = equation (2.14) PASS,
  Tail_action = none; finite compact class,
  selection = none
).

DOOR_GATE4_DESCENT := (
  input_class = A_G,
  operation = q_G,
  kernel = Gamma_G,
  image = Q_G all ranks,
  sector_transfer = edge cochain -> physical cycle quotient,
  restriction_square = equation (2.14) PASS,
  upward_square = equation (3.6) only on cycle-rank-preserving identity
                    extensions; impossible on cycle-creating additions,
  Tail_action = none; finite,
  no_deletion = D_G^* injective on C_G
).
```

No continuum completion, measure, contour, inverse, action, or 2PI class is
formed.

```text
UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S
FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S
```

---

## 8. S6 — final joint-foundation board

The information layer is one coherent split object:

```text
complete prefix traces
  --consecutive ratios-->
cellwise faithful relative characters
  --signed edge realization-->
edge cochain h
  --Gate-4 quotient-->
D_G in Q_G, the physical cycle class.
```

Alongside it:

```text
T_G^char=Hol_c^(-1) compose Z
```

is retained on Q-313's sealed primitive square and the confirmed rank-0/1
extension scope. On `im(j_NM^Q)`, it agrees with `D_G`. Off that image, the
pendant theorem proves the two maps are not one component. That discrepancy
is exactly Gate-4 tree/gauge content.

DoR-015 resolves the consumer seam: physical action comparison uses `D_G`.
The terminal map remains a valid sealed scalar-character factorization where
its own square says it is; it is not promoted into a physical quotient map on
arbitrary full-component histories.

```text
FIXED_STAGE_DESCENT_FORMULA = CONFIRMED
FIXED_STAGE_KERNEL_THEOREM = CONFIRMED
GENERAL_CONTRAVARIANT_CELLULAR_RESTRICTION = CONFIRMED
CYCLE_RANK_PRESERVING_UPWARD_NATURALITY = PROVED
CYCLE_CREATING_UPWARD_NATURALITY = IMPOSSIBLE | TYPE-R

Q313_SEALED_SQUARE_AGREEMENT = PASS
V002_AGREEMENT_ON_IM_J_NM_Q = PASS
FULL_COMPONENT_MERGE = false | TYPE-R

P_432_1 = CLOSED_BY_SCOPE |
  sealed square and im(j_NM^Q) agree; no broader claim
P_432_2 = CLOSED |
  repaired source precomposition and physical restriction compose on scope
P_432_3 = CLOSED_BY_DERIVATION |
  physical action input forced to D_G by DoR-015 quotient typing

JOINT_FOUNDATION_INFORMATION_LAYER = COMPLETE_ON_EDGE_RESOLVED_FAMILY
ACTION_OR_2PI_COMPARISON_SQUARE = NOT_BUILT / TYPE-U
NON_EDGE_RESOLVED_EXTENSION = NOT_BUILT / TYPE-U |
  would-build: family-natural iota_G satisfying equation (7.3)

PHYSICAL_P_VERDICT = NO_VERDICT
LEAD_RESULT = REPAIRED_FOR_FINAL_REVIEW
DESCENT_V002 = READY_FOR_FINAL_REVIEW

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No alpha, `K_*`, root, response value, rank ratio, or measured constant was
evaluated.
