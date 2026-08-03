# STAGE8 TASK 4A: DESCENT V002 FINAL REVIEW - LANE 1 V001

Date: 2026-08-03  
Task: PASTE 437 / Task 4a / final foundation review  
Lane: CODEX LANE 1  
Reviewed artifact: `STAGE8_TASK4A_FAMILY_NATURAL_PREFIX_TO_CYCLE_DESCENT_LANE2_V002.md`  
Reviewed SHA-256: `89d98c3c5c8eedc6de90c2a24569a1e91cec0dc227af6e265447924991496af3`

```text
LEAD_RESULT = KILLED

KILL = P_432_3_UNIVERSAL_CONSUMER_THEOREM_IS_TOO_STRONG |
  DoR-015 permits two physical scalar routes:
  (1) closed-cycle quotient products; or
  (2) endpoint-covariant transport contracted with matching endpoint data.
  Route (2) is gauge invariant but does not factor through q_G(h) alone.

BOUNDED_REPAIR_F1 = CONFIRMED
BOUNDED_REPAIR_F2 = CONFIRMED
FIXED_STAGE_CORE = CONFIRMED
PERMANENT_REGRESSIONS = PASS

P_432_3 = OPEN |
  missing certificate: the action-comparison consumer is quotient-only and
  excludes the ratified endpoint-covariant contraction route

DESCENT_V002 = KILLED (+F3,F6,F7)
INFORMATION_LAYER = INCOMPLETE |
  remains: physical action-consumer class/typing at the D-versus-endpoint
  contraction seam; action/2PI square and non-edge-resolved extension remain
  TYPE-U as already disclosed

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

V002 repairs both mathematical scope defects from the first review. Its
fixed-stage descent and quotient mathematics remain sound. The final failure
is not another map defect: it is a universal consumer-typing inference that
DoR-015 does not license. The narrower theorem is valid: every scalar that
depends only on the edge cochain and is invariant under vertex rephasing
factors uniquely through `q_G`. V002 does not prove that the future action
consumer belongs to that narrower class.

---

## 0. Preflight, custody, and authorities

### 0.1 Mandatory preflight

The reviewed artifact was hash-verified before reading:

```text
expected = 89d98c3c5c8eedc6de90c2a24569a1e91cec0dc227af6e265447924991496af3
actual   = 89d98c3c5c8eedc6de90c2a24569a1e91cec0dc227af6e265447924991496af3
sidecar  = OK
```

The live questions-settled register ended at Q-354. Its local sidecar and
the `LOCKED_PROCESS.md` sidecar both verified. `LOCKED_PROCESS.md` was read
in full.

```text
DOES_THE_OBJECT_EXIST = yes | final foundation review commissioned
IS_THE_VERSION_CURRENT = yes | live register head Q-354
ARE_THE_INPUTS_PRESENT = yes | all named seams available and sealed
PREFLIGHT = PASS
```

### 0.2 Hash-verified authorities

| Authority | Verified SHA-256 | Use |
|---|---|---|
| descent V002 | `89d98c3c5c8eedc6de90c2a24569a1e91cec0dc227af6e265447924991496af3` | object under review |
| Lane-1 Z4/Z7 review | `58b5aef03ac43f365bfbc805bd659c7e6012d3cd292ac1ae9183b4ab9788a2b9` | binding repair standard |
| extension V002 | `eb3675d525af7d1420c4ed033a5e5b94eb7494c1bac1305029b25ac9169567a0` | repaired `j_NM^Q` square and terminal map scope |
| DoR-015 / FIELD_SIGNATURE V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | quotient and consumer typing |
| DoR-016 / network V004 | `69f4d93b9f84075a3112fb011b9838f380fb8c0341610572170cf7a13d5aed08` | prefix traces and endpoint access |

The first-review artifact, extension V002, and V005 sidecars all verified
independently during this review.

### 0.3 Symbol collisions bearing on the verdict

```text
A_G(edge)      = U(1)^(E_G), the edge-cochain torus;
A_G(action)    = V002 Section 5.2's future action-comparison component;
q_G            = edge-cochain quotient A_G(edge)->Q_G;
Q_G            = Gate-4 cycle quotient;
T_e            = endpoint-covariant open-edge transport;
T_G^char       = terminal-character cycle map on its scoped domain;
D_G            = prefix-to-Gate-4 descent;
endpoint data  = matching source/target data allowed by V005 Section 8.
```

The two uses of `A_G` are distinct. More importantly, quotient invariance of
a joint tuple `(endpoint data,T_e)` is not the same as factorization through
the edge-only quotient `q_G(T_e)`.

---

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| F1 - Z7 repair | **PASS** | on cycle-rank-preserving graph inclusions the integral cycle map and its dual restriction are isomorphisms; the inverse defines the upward map, while cycle-creating additions remain expressly impossible |
| F2 - Z4 repair | **PASS** | agreement is limited to the sealed square and `im(j_NM^Q)`; the pendant witness is permanent and no full-component merge is claimed |
| F3 - P-432-3 derivation | **KILL** | V005 expressly permits endpoint-covariant transport contracted with matching endpoint data, a physical scalar route not forced through `q_G(h)` alone |
| F4 - confirmed core | **PASS** | fixed-stage reconstruction, kernel/image theorem, S8-A covariance, boundary, and selection statements are substantively unchanged |
| F5 - regressions | **PASS** | pendant, cycle-creating edge, S8-A, one-edge, reality, batching, and contravariant restriction all recompute |
| F6 - joint-layer statement | **KILL** | its mathematical split is coherent, but `P_432_3=CLOSED` and `INFORMATION_LAYER=COMPLETE` exceed the cited authority |
| F7 - fresh attack | **KILL** | a one-edge endpoint-contraction scalar is gauge invariant, varies while `Q_G` is a point, and therefore refutes universal edge-quotient factorization |

---

## 2. F1 - the Z7 repair is exact

### 2.1 Cycle-rank-preserving extension

Let

```text
i:G_N->G_M                                      (F1-1)
```

be an injective connected graph identity extension that leaves old edges in
place and adds identity-source edges. Assume

```text
rank(C_M)=rank(C_N).                              (F1-2)
```

The induced map `i_*:C_N->C_M` is injective. If an added edge belonged to an
integral cycle not supported on the old graph, its cycle class would be
independent of the old edge-supported cycle lattice and would increase the
cycle rank. Thus the relative added subgraph is a forest attached without
closing a new loop.

Leaf elimination in that relative forest shows that every conserved
integral chain has zero coefficient on each added edge. Therefore

```text
C_M=i_*(C_N)                                     (F1-3)
```

as integral lattices. Hence `i_*` is an isomorphism, not merely a real-rank
equivalence.

### 2.2 The inverse restriction exists

Using V005's cycle-character representation,

```text
Q_G isomorphic to Hom(C_G,U(1)),                 (F1-4)
```

the contravariant restriction is

```text
rho_i:Q_M->Q_N,
rho_i(chi_M)=chi_M compose i_*.                  (F1-5)
```

Since `i_*` is an isomorphism, `rho_i` is an isomorphism. Its inverse

```text
j_NM^phys=rho_i^(-1)                             (F1-6)
```

is intrinsic and representative-independent. It does not append a chosen
edge representative.

For source identity extension `j_NM^prefix`, added characters are one. For
every `c_M=i_*c_N`,

```text
Hol_M(D_M j_NM^prefix Z)(c_M)
 =Hol_N(D_N Z)(c_N).                             (F1-7)
```

Cycle-character separation then gives

```text
D_M j_NM^prefix=j_NM^phys D_N.                   (F1-8)
```

The scope is exactly cycle-rank-preserving identity extensions.

### 2.3 Cycle-creating impossibility remains explicit

V002 reproduces the one-edge-tree plus parallel-identity-edge theorem. In
the old graph `Q_N={*}`. In the new graph,

```text
H([h_e,h_a])=h_e h_a^(-1).                       (F1-9)
```

The old representatives `h_e=1` and `h_e=w` are equivalent, but appending
`h_a=1` gives new holonomies `1` and `w`. Therefore no
representative-independent upward map exists when the added edge creates a
cycle. V002 makes no such claim.

```text
F1 = PASS
```

---

## 3. F2 - the rank-one split is repaired exactly

### 3.1 Sealed square

For `c_square=(1,-1,1,-1)` and the sealed signed traversal,

```text
Hol_(c_square)(D_G(Z))
 =product_j r_j
 =Z_N.                                           (F2-1)
```

Q-313 uniqueness under the exact equation `Hol_c T=Z_N` gives

```text
D_(G_square)=T_N^char.                           (F2-2)
```

### 3.2 Zero-extension image

Extension V002 gives

```text
rho_G,MN T_M^char j_NM^Q=T_N^char.               (F2-3)
```

Descent V002 gives

```text
rho_G,MN D_M j_NM^Q=D_N.                         (F2-4)
```

On the cycle-rank-preserving scope `rho_G,MN` is an isomorphism, and the
right sides agree by `(F2-2)`. Therefore

```text
D_M j_NM^Q=T_M^char j_NM^Q.                      (F2-5)
```

This proves agreement only on `im(j_NM^Q)`.

### 3.3 Pendant witness

On a rank-one cycle with pendant tree edge `t`, set

```text
r_e=1 for every cycle edge,
r_t=w,
w!=1.                                             (F2-6)
```

The physical descent removes the pendant coboundary:

```text
Hol_c(D_M(Z))=1.                                  (F2-7)
```

The terminal map consumes the full product:

```text
Z_M=w,
Hol_c(T_M^char(Z))=w.                             (F2-8)
```

Hence `D_M!=T_M^char` off the zero-extension image. V002 installs this as a
permanent regression and explicitly rejects full-component equality.

```text
F2 = PASS
```

---

## 4. F3 - P-432-3 is not forced by DoR-015

### 4.1 The narrower quotient theorem is valid

Let `S:A_G(edge)->C` be a scalar depending only on the edge cochain. If

```text
S(g.h)=S(h) for every vertex rephasing g,         (F3-1)
```

then `S` is constant on the fibers of

```text
q_G:A_G(edge)->Q_G.                              (F3-2)
```

The universal property of a quotient gives a unique scalar

```text
S_bar:Q_G->C
```

such that

```text
S=S_bar compose q_G.                             (F3-3)
```

Because `D_G=q_G Phi_G`, every edge-only gauge-invariant scalar may consume
`D_G`. The pendant witness proves that full-component `T_G^char` cannot
replace `D_G` on this edge-only quotient class.

This theorem is sound. It has a necessary hypothesis: the consumer depends
only on the edge cochain.

### 4.2 V005's actual consumer clauses

V005 does require quotient-only consumption for the field components it
already types:

```text
A4 consumes ker(B_N^T) conserved currents only;
A5 consumes C(Q_N) invariant cylinders and cycle phases only;
A6 consumes the A4 quotient source domain only.
```

It also states that non-invariant `f(H_N)` is not consumed physically and
that a bare open-edge scalar is not a gauge-invariant output.

But V005's endpoint consumer clause is broader. It says physical scalar
consumers use either:

```text
1. closed-cycle products, for which endpoint factors cancel; or
2. endpoint-covariant transport contracted with matching endpoint data.
                                                               (F3-4)
```

Only route 1 is forced through the edge-only quotient `q_G`. Route 2 is
invariant under a joint action on transport and endpoint data. It need not
be a function of `q_G(h)` alone.

### 4.3 The unbuilt-consumer clauses prevent a universal upgrade

V005 expressly leaves the following absent:

```text
A5_SCALAR_PHYSICAL_FUNCTIONAL_BUILT = false / TYPE-U;
A6_RAW_G_PHYSICAL_IMAGE_EXISTS = false / TYPE-U;
PHYSICAL_SCALAR_FUNCTIONAL_BUILT = false / TYPE-U;
RAW_G_PHYSICAL_IMAGE_BUILT = false / TYPE-U;
STATIONARY_BACKGROUND_BUILT = false / TYPE-U.
```

These are exactly the layers that would type a future action consumer. The
fact that currently built quotient fields consume `Q_G` does not prove that
an unbuilt action can use only route 1 of `(F3-4)`.

### 4.4 Converse audit

The question "does anything ratified permit a physical consumer not through
the edge-only quotient?" has answer **yes**: V005 route 2 explicitly permits
endpoint-covariant transport contracted with matching endpoint data.

This does not authorize a bare open-edge scalar. It authorizes a joint
gauge-invariant scalar on the endpoint-transport carrier. Conflating those
two statements is the gap in V002's universal theorem.

The strongest derivable standing is therefore:

```text
IF action_consumer_class = edge-only scalar invariant under Gamma_G,
THEN action input factors uniquely through D_G.

IF endpoint-matched consumer data are admitted,
THEN DoR-015 alone does not force factorization through D_G.
```

No sealed clause in the cited chain types the future action-comparison square
into the first branch and excludes the second.

```text
P_432_3 = OPEN
MISSING_CERTIFICATE = ACTION_CONSUMER_IS_QUOTIENT_ONLY |
  must exclude endpoint-covariant matching-data consumption for this square
F3 = KILL
```

---

## 5. F4 - confirmed core remains intact

### 5.1 Fixed-stage formula

V002 retains

```text
r_j=Z_(j-1)^(-1)Z_j,
h_(epsilon(j))=r_j^(s_j),
D_G([eta,Z])=q_G(h),                              (F4-1)
```

with basis-free character

```text
Hol_G(D_G(Z))(c)
 =product_j r_j^(s_j c_(epsilon(j))).             (F4-2)
```

Under simultaneous signed relabeling,

```text
r'_j=r_k^(tau_j),
s'_j=tau_j s_k,
(r'_j)^(s'_j)=r_k^(s_k),                         (F4-3)
```

so the oriented edge cochain is unchanged.

### 5.2 Kernel and no deletion

The carried map `Phi_G:P_G^fam->U(1)^(E_G)` remains an isomorphism. Thus

```text
ker(D_G)=Phi_G^(-1)(Gamma_G).                    (F4-4)
```

Surjectivity of `Phi_G` and `q_G` makes `D_G` surjective. Pullback of cycle
characters is injective:

```text
ker(D_G^*:C_G->Hom(P_G^fam,U(1)))={0}.            (F4-5)
```

### 5.3 S8-A covariance

The retained coordinates are

```text
H_(c_1)=Z_2,
H_(c_2)=Z_1^(-1)Z_3,
H_(c_3)=Z_1 Z_2 Z_3^(-1).                        (F4-6)
```

Under the parallel-edge exchange,

```text
H_(c_1)'=H_(c_2),
H_(c_2)'=H_(c_1),
H_(c_3)'=H_(c_3)^(-1).                           (F4-7)
```

`c_3` survives covariantly.

### 5.4 Boundary and selection

The non-edge-resolved candidate remains

```text
iota_G:C_G->Z^N,
Hol_G(D_iota(r))(c)=product_j r_j^((iota_Gc)_j), (F4-8)
```

with exact no-deletion condition `ker(iota_G)={0}`. No member of the
residual `iota` family is selected. The no-selection family quotient and all
rank/orientation/frame/basis exclusions are retained.

```text
F4 = PASS
```

---

## 6. F5 - regression suite

| Regression | Recomputed result |
|---|---|
| pendant `w!=1` | `D=1`, `T^char=w`; full equality refuted |
| cycle-creating identity edge | no representative-independent upward quotient map |
| S8-A `c_3` | `H_c3=Z_1 Z_2 Z_3^(-1)`; inverted under exchange, not deleted |
| one edge | `C_G=0`, `Q_G={*}`, endpoint access remains upstream |
| reality | conjugation commutes with prefix inversion and signed products |
| batching | `r_[a,b]=Z_(a-1)^(-1)Z_b`, with signed inversions as required |
| contravariant restriction | `D_N P_f=rho_f D_M` by cochain pullback |
| rank-preserving upward map | `j_NM^phys=rho_i^(-1)` and equation `(F1-8)` |

Every permanent regression passes. The failure in F3 is outside those
finite map computations.

```text
F5 = PASS
```

---

## 7. F6 - joint-layer board is overclaimed at one line

The following mathematical board is coherent:

```text
D_G exists at every finite signed edge-resolved rank;
T_G^char exists on its sealed/scoped terminal-character domain;
D_G=T_G^char on the sealed square and im(j_NM^Q);
D_G!=T_G^char on the pendant witness off that image;
cycle-creating upward naturality is impossible;
cycle-rank-preserving upward naturality is proved.
```

The following doors are also honestly retained:

```text
ACTION_OR_2PI_COMPARISON_SQUARE = NOT_BUILT / TYPE-U
NON_EDGE_RESOLVED_EXTENSION = NOT_BUILT / TYPE-U
```

What the artifacts do not support is the additional line

```text
P_432_3 = CLOSED_BY_DERIVATION
```

or the resulting unconditional statement that the information layer is
complete for the action-comparison consumer. V005 leaves a permitted
endpoint-matched scalar route and does not type the unbuilt action square
away from it.

The repaired map layer is coherent; the consumer-facing information layer
is incomplete by one exact typing certificate.

```text
F6 = KILL
```

---

## 8. F7 - fresh one-edge endpoint-contraction attack

### 8.1 Construction

Take the one-edge tree `e:s->t`. Let its endpoint transport transform as

```text
T_e -> g_t T_e g_s^(-1).                         (F7-1)
```

Let matching endpoint vectors transform as

```text
v_s->g_s v_s,
v_t->g_t v_t.                                    (F7-2)
```

Define the scalar

```text
S_e(v_t,T_e,v_s)=<v_t,T_e v_s>.                  (F7-3)
```

For unitary endpoint actions,

```text
S_e(g_t v_t,g_t T_e g_s^(-1),g_s v_s)
 =<g_t v_t,g_t T_e v_s>
 =<v_t,T_e v_s>.                                 (F7-4)
```

Thus `S_e` is a physical gauge-invariant scalar of precisely V005's allowed
route 2. It is not a bare open-edge scalar.

### 8.2 It cannot factor through the edge-only quotient

For a connected one-edge tree,

```text
Q_G={*}.                                         (F7-5)
```

Every function of `q_G(T_e)` alone is therefore constant. But with
one-dimensional endpoint fibers, take

```text
T_e=1,
v_s=1,
v_t=1                                           (F7-6)
```

and compare it with

```text
T_e=1,
v_s=1,
v_t=u,
u in U(1), u!=1.                                 (F7-7)
```

The edge quotient is the same point in both cases, while

```text
S_e=1 in (F7-6),
S_e=conjugate(u) in (F7-7).                      (F7-8)
```

The two joint tuples are not gauge-equivalent because the invariant scalar
differs. Hence no `S_bar:Q_G->C` can satisfy `S_e=S_bar compose q_G` on the
joint endpoint-transport class.

### 8.3 Consequence

This countermodel is not an imported convention. It instantiates the second
consumer route written in V005 itself. It proves that DoR-015 does not force
every physical scalar/action consumer through the edge-only quotient.

The countermodel does not prove that the future transverse action actually
uses endpoint data. It proves that V002 cannot exclude that possibility from
DoR-015 alone.

```text
FRESH_ATTACK = one-edge endpoint-matched scalar
RESULT = KILL
F7 = KILL
```

---

## 9. Final determination

### 9.1 Surviving foundation

```text
FIXED_STAGE_DESCENT = CONFIRMED
LAWFUL_KERNEL = Gate-4 vertex rephasing only
NO_RECORD_VISIBLE_CYCLE_DELETED = true | TYPE-P
GENERAL_CONTRAVARIANT_RESTRICTION = CONFIRMED
CYCLE_RANK_PRESERVING_UPWARD_MAP = CONFIRMED
CYCLE_CREATING_UPWARD_MAP = IMPOSSIBLE | TYPE-R
SEALED_SQUARE_AGREEMENT = CONFIRMED
AGREEMENT_ON_IM_J_NM_Q = CONFIRMED
PENDANT_DISAGREEMENT = CONFIRMED | TYPE-R
NON_EDGE_RESOLVED_EXTENSION = NOT_BUILT / TYPE-U
```

### 9.2 Unclosed seam

```text
P_432_3 = OPEN

EXACT_MISSING_CERTIFICATE =
  ACTION_COMPARISON_CONSUMER_CLASS_IS_QUOTIENT_ONLY:
    the future action square consumes closed-cycle/invariant-cylinder data
    only and does not consume endpoint-covariant transport contracted with
    matching endpoint data.

WITHOUT_CERTIFICATE =
  DoR-015 permits both classes and does not select between them for the
  still-unbuilt action/2PI square.
```

### 9.3 Required final lines

```text
DESCENT_V002 = KILLED (+F3,F6,F7)
INFORMATION_LAYER = INCOMPLETE (+physical action-consumer typing at the D-versus-endpoint-contraction seam)

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No physical response value, prohibited root, rank ratio, or measured
comparison was evaluated.
