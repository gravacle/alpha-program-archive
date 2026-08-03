# STAGE8 TASK 4A: PREFIX-TO-CYCLE DESCENT CROSS-REVIEW - LANE 1 V001

Date: 2026-08-03  
Task: PASTE 434 / Task 4a / adversarial cross-review  
Lane: CODEX LANE 1  
Reviewed artifact: `STAGE8_TASK4A_FAMILY_NATURAL_PREFIX_TO_CYCLE_DESCENT_LANE2_V001.md`  
Reviewed SHA-256: `5c5d2c828a62e302920c827e95678c9e9e00b2fdc1a2415c553383fcbbfe3a84`

```text
LEAD_RESULT = KILLED

KILL_1 = V002_RANK1_COMPONENT_MISMATCH |
  a nontrivial pendant-edge character is Gate-4 gauge and is therefore
  removed by D, but it remains a factor of V002's terminal Z_M and is
  injected by T_M^char into the unique cycle coordinate

KILL_2 = CYCLE_CREATING_IDENTITY_EXTENSION_HAS_NO_QUOTIENT_MAP |
  extending an old quotient representative by a new edge coordinate 1 is
  not representative-independent when that edge creates a cycle

FIXED_STAGE_DESCENT_FORMULA = CONFIRMED
FIXED_STAGE_KERNEL_THEOREM = CONFIRMED
GENERAL_CONTRAVARIANT_CELLULAR_RESTRICTION = CONFIRMED

DESCENT = KILLED | items: Z4, Z7
V002_SEAMS_CLOSED = no |
  P-432-1 fails;
  P-432-2 closes only after precomposition on the zero-extension image,
  not as equality of the full rank-one components;
  P-432-3 remains open

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The kill is bounded. The formula

```text
r_j=Z_(j-1)^(-1)Z_j,
h_(epsilon(j))=r_j^(s_j),
D_G(Z)=q_G(h)
```

is a sound fixed-stage descent on a typed signed edge-resolved realization,
and its kernel is exactly vertex rephasing. What fails is the artifact's
stronger package: the unrestricted identity-zero-extension certificate and
the claimed merge path with the now-completed V002 terminal-scalar family.

---

## 0. Preflight, custody, and authority verification

### 0.1 Mandatory preflight

The reviewed artifact was hash-verified before reading:

```text
expected = 5c5d2c828a62e302920c827e95678c9e9e00b2fdc1a2415c553383fcbbfe3a84
actual   = 5c5d2c828a62e302920c827e95678c9e9e00b2fdc1a2415c553383fcbbfe3a84
sidecar  = OK
```

The live questions-settled register ended at Q-352. Its local sidecar and the
local `LOCKED_PROCESS.md` sidecar both verified. `LOCKED_PROCESS.md` was read
in full.

```text
DOES_THE_OBJECT_EXIST = yes | commissioned cross-review
IS_THE_VERSION_CURRENT = yes | live register head Q-352
ARE_THE_INPUTS_PRESENT = yes | all named seams hash-verified
PREFLIGHT = PASS
```

### 0.2 Seam authorities

| Authority | Verified SHA-256 | Result |
|---|---|---|
| extension V002 | `eb3675d525af7d1420c4ed033a5e5b94eb7494c1bac1305029b25ac9169567a0` | sidecar OK |
| Q-313 Map 1 | `ea8f4e9a79a9e4aca4a0b9e9aab470d78cd4d9c78794c20d9e979c0db16fbeab` | sidecar OK |
| DoR-015 / FIELD_SIGNATURE V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | sidecar OK |
| DoR-016 / network law V004 | `69f4d93b9f84075a3112fb011b9838f380fb8c0341610572170cf7a13d5aed08` | sidecar OK |
| prefix sufficiency theorem | `d9a507fc8b5645981ed1519a04e180620ee7c22f65d5c9425437a701185f9001` | sidecar OK |
| Q-349 sufficiency cross-review | `f9900a13884ade20d8ab57ed3c36f473d928b9aedd249da9b25d333f20b47899` | sidecar OK |

The DoR-016 decision itself also verified under SHA-256
`b4157df6f327e261f40389d5a3011a0aef66ee0f198d8ebba8b1b9303142d708`.

### 0.3 Symbol collisions bearing on this review

```text
Z_m          = every-prefix scalar trace through cell m;
r_j          = Z_(j-1)^(-1)Z_j, a faithful cell character;
Q_rel,N      = relative-history source carrier;
Q_G          = Gate-4 edge-cochain quotient;
j_NM^Q       = source-side zero-extension Q_rel,N -> Q_rel,M;
rho_f        = target-side contravariant restriction Q_M -> Q_N;
j_NM^Q,phys  = the artifact's asserted target-side upward extension;
Gamma_G      = image of vertex rephasing in the edge-cochain torus;
C_G          = integral cycle lattice ker(B_G^T) intersect Z^(E_G).
```

The distinction between `j_NM^Q` and `j_NM^Q,phys` is decisive. V002 repairs
the former. It does not construct the latter.

---

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| Z1 - formula and well-definedness | **PASS** | simultaneous signed relabeling preserves the reconstructed oriented edge cochain exactly; the holonomy formula is basis-free |
| Z2 - kernel theorem | **PASS** | `Phi_G` is an edge-coordinate isomorphism and `ker(q_G)=Gamma_G`, so `ker(D_G)=Phi_G^(-1)(Gamma_G)`; surjectivity and dual injectivity follow |
| Z3 - Y3 obstruction re-fired | **PASS** | on S8-A the edge exchange acts covariantly as `c1<->c2`, `c3->-c3`; `H_c3` is inverted, not deleted |
| Z4 - certificates and V002 seams | **KILL** | identity-zero-extension is false for cycle-creating edge additions, and V002's full rank-one terminal map disagrees with `D` on nonidentity tree-edge characters |
| Z5 - boundary honesty | **PASS** | the non-edge-resolved chain-map boundary is real; `ker(iota_G)` is exactly the cycle-deletion subspace |
| Z6 - selection scan | **PASS** | the simultaneous presentation quotient selects no member; the missing cell-to-edge map remains explicitly outside the built domain |
| Z7 - fresh attack | **KILL** | the tree-to-parallel-edge counterexample proves no target quotient inclusion can satisfy the displayed identity-extension square |

---

## 2. Z1 - formula and well-definedness

### 2.1 Prefix inversion

For a finite prefix family with `Z_0=1`, define

```text
r_j=Z_(j-1)^(-1)Z_j.                              (Z1-1)
```

Then telescoping gives

```text
Z_m=product_(j=1)^m r_j.                          (Z1-2)
```

The map between `(Z_1,...,Z_N)` and `(r_1,...,r_N)` is therefore a group
isomorphism. No logarithm or branch is used.

### 2.2 Signed presentation change

Let a signed relabeling send the old cell index `k` to the new index `j`
with sign `tau_j in {+1,-1}`. The recovered characters and signed
presentation transform as

```text
r'_j=r_k^(tau_j),
epsilon'(j)=epsilon(k),
s'_j=tau_j s_k.                                   (Z1-3)
```

The reconstructed edge coordinate is unchanged:

```text
h'_(epsilon'(j))
 =(r'_j)^(s'_j)
 =(r_k^tau_j)^(tau_j s_k)
 =r_k^(s_k)
 =h_(epsilon(k)).                                 (Z1-4)
```

Thus simultaneous signed relabeling changes only the presentation. Holding
the prefix tuple fixed while relabeling would be wrong, but the reviewed
artifact does not do that.

### 2.3 Basis-free form

For every integral cycle `c in C_G`,

```text
Hol_G(D_G(Z))(c)
 =product_(e in E_G) h_e^(c_e)
 =product_(j=1)^N r_j^(s_j c_(epsilon(j))).        (Z1-5)
```

This quantifies over `C_G`; it does not select a cycle basis. Equations
`(Z1-4)` and `(Z1-5)` establish well-definedness on the no-selection
presentation quotient.

```text
Z1 = PASS
```

---

## 3. Z2 - kernel, image, and S8-A survival

### 3.1 Fixed-stage exact sequence

On a fixed signed edge-resolved realization, the map

```text
Phi_G:P_G^fam -> A_G=U(1)^(E_G)
```

is an isomorphism. Surjectivity follows by taking, in any signed
presentation,

```text
r_j=h_(epsilon(j))^(s_j),
Z_m=product_(j=1)^m r_j.                          (Z2-1)
```

Applying the construction recovers `h`. Injectivity follows from prefix
inversion and the simultaneous-presentation quotient: two family classes
with the same oriented edge cochain have the same recovered characters in
every presentation.

V005 defines

```text
q_G:A_G -> Q_G=A_G/Gamma_G.                       (Z2-2)
```

Consequently

```text
D_G=q_G compose Phi_G,
ker(D_G)=Phi_G^(-1)(Gamma_G).                     (Z2-3)
```

There is no larger fixed-stage kernel. Presentation relabeling is equality
inside `P_G^fam`, not an additional physical kernel.

### 3.2 Surjectivity and dual injectivity

Both `Phi_G` and `q_G` are surjective, hence `D_G` is surjective. Its pullback
on the integral cycle characters is

```text
D_G^*:C_G -> Hom(P_G^fam,U(1)),
(D_G^*c)(Z)=Hol_G(D_G(Z))(c).                     (Z2-4)
```

If `D_G^*c` is trivial, surjectivity of `D_G` makes `Hol_G(q)(c)=1` for every
`q in Q_G`. V005's cycle-character separation then gives `c=0`. Therefore

```text
ker(D_G^*)={0}.                                   (Z2-5)
```

No nonzero record-visible cycle is deleted at a fixed typed stage.

### 3.3 S8-A recomputation

With edge order `(a,b,d)`, take

```text
c_1=(1,1,0),
c_2=(0,1,1),
c_3=(1,0,-1)=c_1-c_2.                            (Z2-6)
```

Prefix inversion gives

```text
r_a=Z_1,
r_b=Z_1^(-1)Z_2,
r_d=Z_2^(-1)Z_3.                                 (Z2-7)
```

The three named characters are

```text
H_(c_1)=r_a r_b=Z_2,
H_(c_2)=r_b r_d=Z_1^(-1)Z_3,
H_(c_3)=r_a r_d^(-1)=Z_1 Z_2 Z_3^(-1).           (Z2-8)
```

`H_(c_3)` is not identically one. It obeys only the required relation

```text
H_(c_3)=H_(c_1)H_(c_2)^(-1).                     (Z2-9)
```

```text
Z2 = PASS
```

---

## 4. Z3 - the terminal obstruction acts covariantly here

Let `sigma` exchange the parallel edges `a` and `d`. The cell characters
transform as

```text
(r_a,r_b,r_d) -> (r_d,r_b,r_a).                  (Z3-1)
```

Re-prefixing rather than holding the source fixed gives

```text
Z'_1=Z_2^(-1)Z_3,
Z'_2=Z_1^(-1)Z_3,
Z'_3=Z_3.                                         (Z3-2)
```

Substituting `(Z3-2)` into `(Z2-8)` yields

```text
H'_(c_1)=H_(c_2),
H'_(c_2)=H_(c_1),
H'_(c_3)=H_(c_3)^(-1).                            (Z3-3)
```

This is exactly the target action

```text
c_1 <-> c_2,
c_3 -> -c_3.                                      (Z3-4)
```

The Q-347/Y3 obstruction required an input scalar fixed by the exchange and
an output cycle moved by it. The complete prefix source is not fixed. The
descent is covariant and deletes nothing.

```text
Z3 = PASS
```

---

## 5. Z4 - certificate audit and the V002 seams

### 5.1 General contravariant cellular restriction passes

For a declared signed chain map

```text
f_1:C_1(G_N)->C_1(G_M),
partial_M f_1=f_0 partial_N,                      (Z4-1)
```

the edge-cochain pullback is

```text
(f_1^*h_M)(e)=h_M(f_1e).                          (Z4-2)
```

For a fine vertex coboundary `delta_M g`,

```text
f_1^*(delta_M g)=delta_N(f_0^*g),                 (Z4-3)
```

so pullback descends to

```text
rho_f:Q_M->Q_N.                                   (Z4-4)
```

Recovering fine ratios, multiplying and inverting according to `f_1`, and
re-prefixing defines `P_f`. Direct substitution gives

```text
D_N P_f
 =q_N f_1^* Phi_M
 =rho_f q_M Phi_M
 =rho_f D_M.                                      (Z4-5)
```

This contravariant restriction square is well typed and passes on every
declared signed cellular arrow.

### 5.2 Batching passes

For a signed batch `[a,b]`,

```text
r_[a,b]=product_(j=a)^b r_j^(sign_j).             (Z4-6)
```

The unsigned consecutive case is the exact prefix identity

```text
r_[a,b]=Z_(a-1)^(-1)Z_b.                          (Z4-7)
```

Equations `(Z4-6)` and `(Z4-7)` are precisely the cochain pullback
`(Z4-2)`. Batching therefore passes in the fine-to-coarse direction.

### 5.3 Reality passes

Conjugation sends

```text
Z_m->conjugate(Z_m),
r_j->conjugate(r_j),
h_e->conjugate(h_e).                              (Z4-8)
```

Because signed products commute with conjugation,

```text
D_G(Theta_P Z)=Theta_G D_G(Z).                    (Z4-9)
```

This is covariance, not pointwise invariance.

### 5.4 Family-automorphism covariance passes

For a signed incidence isomorphism `alpha`, reconstruction commutes with the
forced prefix automorphism:

```text
Phi_(G') J_alpha=alpha_A Phi_G,
D_(G') J_alpha=alpha_Q D_G.                       (Z4-10)
```

The S8-A computation in Section 4 independently exercises `(Z4-10)`.

### 5.5 Q-313 rank-zero and sealed-square agreement passes

At cycle rank zero, `Q_G` is a point, so `D_G` is the unique cycle
projection. For the sealed square, its signed primitive traversal has
`s_j=c_(epsilon(j))` and `c_e in {+1,-1}`. Hence

```text
Hol_(c_square)(D_G(Z))
 =product_j r_j^(s_j c_(epsilon(j)))
 =product_j r_j
 =Z_N.                                            (Z4-11)
```

Q-313 uniqueness under the exact equation `Hol_c T=Z_N` gives

```text
D_(G_square)=Hol_(c_square)^(-1) compose Z_N
             =T_N^char.                           (Z4-12)
```

This agreement is exact and does not rely on V002.

### 5.6 P-432-1 fails: full rank-one component mismatch

V002 defines, for every connected rank-one stage,

```text
T_M^char=Hol_c^(-1) compose Z_M                   (Z4-13)
```

under the exact factorization equation `Hol_c T_M^char=Z_M`. The descent
instead maps every edge character to `Q_G` and then removes tree-edge phases
as vertex rephasing.

Take a connected rank-one graph consisting of one cycle plus a pendant tree
edge `t`. Use a signed presentation matching the primitive cycle. Set

```text
r_e=1 for every cycle edge e,
r_t=w with w in U(1), w!=1.                       (Z4-14)
```

For the reviewed descent, every cycle holonomy is one:

```text
Hol_c(D_M(Z))=1.                                  (Z4-15)
```

The pendant coordinate is a vertex coboundary and disappears in `Q_G`.
For V002, however,

```text
Z_M=product_e r_e=w,
Hol_c(T_M^char(Z))=w.                             (Z4-16)
```

Therefore

```text
D_M(Z) != T_M^char(Z) for w!=1.                   (Z4-17)
```

The descent artifact's claim that attached tree cells are identity zero
extensions is true only on the image of the source precomposition that sets
those new characters to one. It is not true on V002's full component domain
`Q_rel,M`.

```text
P_432_1 = FAIL
```

### 5.7 P-432-2 closes only on the zero-extension image

V002's repaired square is

```text
rho_G,MN compose T_M^char compose j_NM^Q=T_N^char. (Z4-18)
```

For an attached tree refinement, `j_NM^Q` sets every new tree character to
one. On that image, `(Z4-14)` is unavailable and the two constructions agree:

```text
rho_G,MN D_M j_NM^Q=D_N,
rho_G,MN T_M^char j_NM^Q=T_N^char.                (Z4-19)
```

Thus the corrected `j_NM^Q` precomposition does its intended job. But it
does not imply `D_M=T_M^char` away from `im(j_NM^Q)`. Equations `(Z4-17)` and
`(Z4-19)` give the exact split.

```text
P_432_2 = PARTIAL |
  restriction square closes on im(j_NM^Q);
  full rank-one component comparison fails
```

### 5.8 P-432-3 remains open

Because the component-level merge fails, the two artifacts cannot yet be
declared one joint family-natural foundation. The action-comparison square
could consume the physical descent `D` and retain V002 only on the sealed
square/zero-extension image, but that scope decision is not made here.

```text
P_432_3 = OPEN
```

### 5.9 Identity-zero-extension fails when cycle rank grows

The artifact asserts an upward target map

```text
j_NM^Q,phys:Q_N->Q_M,
D_M j_NM^prefix=j_NM^Q,phys D_N.                  (Z4-20)
```

No such quotient map is defined by "append edge coordinate 1" when the new
edge creates a cycle. The explicit counterexample is in Section 8. This is
independent of the pendant-edge V002 mismatch.

```text
IDENTITY_ZERO_EXTENSION_ALL_DECLARED_STAGES = FAIL
```

### 5.10 Z4 verdict

```text
restriction_contravariant = PASS
batching = PASS
reality = PASS
family_automorphism_covariance = PASS
Q313_fixed_square_agreement = PASS
V002_P_432_1 = FAIL
V002_P_432_2 = PARTIAL
V002_P_432_3 = OPEN
identity_zero_extension_unscoped = FAIL

Z4 = KILL
```

---

## 6. Z5 - boundary honesty

### 6.1 The missing typing is real

The edge-resolved construction needs a signed map from the relative cell
lattice to the realized edge-chain lattice. Prefix inversion provides the
characters `r_j`; it does not say which edge each character inhabits. If that
association is absent, the candidate datum is an integral map

```text
iota_G:C_G->Z^N.                                  (Z5-1)
```

It induces

```text
Hol_G(D_iota(r))(c)
 =product_(j=1)^N r_j^((iota_G c)_j).             (Z5-2)
```

### 6.2 Exact deletion criterion

If `0!=c in ker(iota_G)`, then `(Z5-2)` is one for every source tuple, so
the cycle `c` is deleted. Conversely, if `iota_G` is injective, restriction
of characters from `Z^N` to `iota_G(C_G)` is surjective because `U(1)` is a
divisible abelian group. The induced map onto `Hom(C_G,U(1))` is therefore
surjective.

Thus

```text
NO_CYCLE_DELETION iff ker(iota_G)={0}.             (Z5-3)
```

The artifact correctly leaves existence and family naturality of such maps
`TYPE-U` outside edge-resolved realizations. Its phrase "a member with
kernel deletes that cycle" refers to the unrestricted candidate family; the
admissible subfamily then imposes injectivity. That distinction is coherent.

```text
Z5 = PASS
```

---

## 7. Z6 - selection and domain-quotient audit

The built fixed-stage domain is

```text
(disjoint union over signed presentations eta of P_eta)
  / simultaneous signed relabeling.               (Z6-1)
```

Equation `(Z1-4)` proves this quotient identifies presentations of the same
edge cochain. It neither averages over physical cycle coordinates nor holds
the source fixed while changing labels.

```text
realization member selected = false
edge selected = false
orientation selected = false
filtration member selected = false
cycle basis selected = false
chain-map member selected outside edge-resolved scope = false
rank or rank ratio selected = false
p evaluated = false
```

The typed edge-resolved association is consumed as presentation data. Where
it is absent, the artifact reports a residual `iota` family rather than
choosing one. The two kills above arise from map scope, not hidden member
selection.

```text
Z6 = PASS
```

---

## 8. Z7 - fresh attack: cycle-creating identity edge

### 8.1 Attack construction

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

### 8.2 Representative-independence fails

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

### 8.3 The displayed descent square cannot be repaired by another target map

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

---

## 9. Consolidated determination

### 9.1 What remains proved

The following fixed-stage and contravariant claims survive this review:

```text
PREFIX_INVERSION = PASS
SIGNED_PRESENTATION_WELL_DEFINEDNESS = PASS
BASIS_FREE_HOLONOMY_FORM = PASS
FIXED_STAGE_KERNEL = Phi_G^(-1)(Gamma_G)
FIXED_STAGE_SURJECTIVITY = PASS
FIXED_STAGE_DUAL_INJECTIVITY = PASS
S8A_C3_SURVIVAL = PASS
Y3_AUTOMORPHISM_COVARIANCE = PASS
GENERAL_SIGNED_CELLULAR_RESTRICTION = PASS
BATCHING_FINE_TO_COARSE = PASS
REALITY_COVARIANCE = PASS
Q313_SEALED_SQUARE_AGREEMENT = PASS
NON_EDGE_RESOLVED_BOUNDARY = HONEST
SELECTION_SCAN = PASS
```

### 9.2 What is killed

```text
FULL_V002_RANK1_COMPONENT_AGREEMENT = false | TYPE-R |
  counterexample: nonidentity pendant-edge character

UNSCOPED_IDENTITY_ZERO_EXTENSION = false | TYPE-R |
  counterexample: one-edge tree plus identity parallel edge

JOINT_FOUNDATION_READY = false |
  reason: component merge and upward quotient square are not established
```

### 9.3 Repair boundary

A bounded successor could retain the fixed-stage descent and:

1. remove the asserted upward identity-extension square;
2. state only the proved contravariant restriction square;
3. scope any identity extension to cycle-rank-preserving arrows with an
   independently well-defined quotient map;
4. limit V002 compatibility to Q-313's sealed square and to the image of
   `j_NM^Q`, unless V002's terminal map is itself replaced or quotiented so
   tree-edge characters cannot enter the cycle coordinate.

No repair is executed in this cross-review.

```text
DESCENT = KILLED (+Z4,Z7)
V002_SEAMS_CLOSED = no (+P-432-1; P-432-2 only on im(j_NM^Q); P-432-3 open)

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No physical response value, prohibited root, rank ratio, or measured
comparison was evaluated.
