# STAGE8 TASK 4A: FAMILY-NATURAL PREFIX-TO-CYCLE DESCENT — CODEX LANE 2 V001

Date: 2026-08-03  
Task: PASTE 433 / Task 4a / family-natural prefix-to-cycle descent  
Lane: CODEX LANE 2  
Register head: Q-350  
Parallel work: relay 432 / Lane 1 / bounded `j_NM^Q` repair — **PENDING**

```text
LEAD_RESULT = CONSTRUCTED-WITH-BOUNDARY

CONSTRUCTED_OBJECT = D_prefix->cycle

DOMAIN =
  complete every-prefix DoR-016 trace family on every finite signed,
  edge-resolved realization member, modulo simultaneous signed relabeling

CODOMAIN =
  Q_G=U(1)^(E_G)/Gamma_G, equivalently Hom(C_G,U(1)),
  C_G=ker(B_G^T) intersect Z^(E_G)

FORMULA =
  r_j=Z_(j-1)^(-1)Z_j;
  h_(epsilon(j))=r_j^(s_j);
  D_(G,epsilon,s)(Z)=q_G(h)

EQUIVALENT_BASIS_FREE_FORM =
  Hol_G(D(Z))(c)=product_j r_j^(s_j c_(epsilon(j)))

ALL_FINITE_CYCLE_RANKS = CONSTRUCTED | TYPE-P |
  premises: DoR-009, DoR-015, DoR-016, Q-348/Q-349

LAWFUL_KERNEL = Gate-4 vertex rephasing only |
  ker(D_G)=Phi_G^(-1)(Gamma_G)

NO_RECORD_VISIBLE_CYCLE_DELETED = true | TYPE-P |
  proof: Phi_G is an edge-coordinate isomorphism and q_G is surjective;
         equivalently D_G^* is injective on C_G

BOUNDARY =
  a history/realization class with no declared signed cell-to-edge chain map;
  there the residual family is the family of such chain maps iota, and a
  member whose restriction to C_G has kernel deletes that kernel cycle

NON_EDGE_RESOLVED_EXTENSION = NOT_BUILT / TYPE-U
ACTION_OR_2PI_COMPARISON_SQUARE = NOT_BUILT / TYPE-U

RANK01_LANE1_REPAIR = PENDING
RANK01_REPAIR_USED_AS_LOAD_BEARING_PREMISE = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The construction is total on the finite edge-resolved carrier actually used
by V005: a realized cell is an oriented edge, while all enumerations,
orientations, frames, and realization members remain in the family. It does
not manufacture a map from an arbitrary untyped history cell to a physical
edge. That latter seam is the exact boundary.

---

## 1. Preflight and custody

### 1.1 Foundation hashes

Every required foundation was hash-verified before it was read:

| Foundation | Verified SHA-256 | Result |
|---|---|---|
| Q-348 sufficiency theorem | `d9a507fc8b5645981ed1519a04e180620ee7c22f65d5c9425437a701185f9001` | PASS; sidecar OK |
| Q-350 extension cross-review | `4bcc286e1cb1adf5fbdbc725d0bbd1947c04c56bfa72b2394afeb129a237c1a3` | PASS; sidecar OK |
| Q-313 Map 1 | `ea8f4e9a79a9e4aca4a0b9e9aab470d78cd4d9c78794c20d9e979c0db16fbeab` | PASS; sidecar OK |
| DoR-015 / V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | PASS; sidecar OK |
| DoR-016 / V004 | `69f4d93b9f84075a3112fb011b9838f380fb8c0341610572170cf7a13d5aed08` | PASS; sidecar OK |

The Q-349 cross-review of the sufficiency theorem was also checked after the
register sweep:

```text
Q349_cross_review_sha256 =
  f9900a13884ade20d8ab57ed3c36f473d928b9aedd249da9b25d333f20b47899
Q349_sidecar = PASS
```

### 1.2 Register and process

The live questions-settled file ends at Q-350, as required. Its reviewer-
maintained sidecar does not match its current bytes; Q-349 already records
this as a reviewer-custody discrepancy. This lane neither repairs nor uses
that sidecar as theorem evidence. The stated head itself passes.

`LOCKED_PROCESS.md` was read in full.

```text
DOES_THE_OBJECT_EXIST = yes | the descent contract is commissioned
IS_THE_VERSION_CURRENT = yes | live register head Q-350
ARE_THE_INPUTS_PRESENT = yes | finite edge-resolved scope
PREFLIGHT = PASS

REGISTER_SIDECAR_CURRENT = false |
  reviewer-custody discrepancy, not edited by this lane
```

### 1.3 Pending parallel repair accounting

Relay 432 is repairing Q-347 E2.4 by inserting

```text
j_NM^Q:Q_rel,N->Q_rel,M
```

into the rank-one naturality square. Its result is **PENDING**. This build
does not treat that repair as complete and does not inherit Q-347's killed
rank-one naturality certificate.

Every place where the repaired artifact would otherwise be consumed is
listed here:

| Pending point | Location in this artifact | Standing |
|---|---|---|
| P-432-1 | G1 agreement with the **rank-one family theorem**, beyond pointwise Q-313 agreement | PENDING; not load-bearing |
| P-432-2 | G2 comparison of this independently proved cellular square with Q-347's repaired rank-one square | PENDING; not load-bearing |
| P-432-3 | final joint-foundation readiness statement for the later action-comparison commission | PENDING external review/merge |

The finite Q-313 square and Q-315's already-built square are not pending;
only Lane 1's attempted extension of them is.

```text
PENDING_REPAIR_CONSUMPTION_POINTS = 3
PENDING_REPAIR_USED_TO_PROVE_D_PREFIX_TO_CYCLE = false
```

---

## 2. Questions-settled register sweep

The following entries were checked before construction:

| Entry | Constraint or theorem consumed |
|---|---|
| Q-239 | relative-history and incidence quotients are distinct; scalar descent does not identify their carriers |
| Q-241 | verdict invariance over 1,088 filtrations does not create a realization map |
| Q-261 | the 1,088 support filtrations are not the complete geometric realization family |
| Q-293 | the physical carrier retains the full realization/frame family and then quotients path-invisible content |
| Q-299 | `ker(B_G^T)` is the complete record-visible scalar-cycle dual; open paths remain endpoint-covariant access |
| Q-310 | CTP closure is not incidence closure; orientation must be carried by a map, never presumed |
| Q-313 | the sealed rank-one square Map 1 is unique and arbitrary-cellulation naturality was still unbuilt |
| Q-315 | Q-313's fixed-square restriction square exists; it is not the full-family square |
| Q-341 | filtration-member-dependent physical content is forbidden by DoR-015 family naturality |
| Q-343 | exact CTP composition/character multiplication is batching-natural |
| Q-346 | DoR-016's trace is Q-313's consumed scalar; Map 1 must be consumed rather than rivaled |
| Q-347 | one terminal scalar is obstructed at rank at least two |
| Q-348 | the complete prefix family is isomorphic to all cellwise relative characters |
| Q-349 | prefix availability is ratified; permutation acts by the forced automorphism `J_pi` |
| Q-350 | the terminal obstruction is scoped; the prefix escape is open; rank-one repair pending |

The sweep yields four binding instructions:

```text
CTP_CLOSURE_MAY_BE_IDENTIFIED_WITH_INCIDENCE_CLOSURE = false | TYPE-R
ONE_TERMINAL_SCALAR_IS_ENOUGH_AT_RANK_GE_2 = false | TYPE-R
FILTRATION_MEMBER_MAY_BE_SELECTED = false | TYPE-R
PREFIX_COORDINATES_MUST_TRANSFORM_COVARIANTLY = true | TYPE-P
```

---

## 3. Symbol and carrier ledger

```text
Z_m^CTP       = ratified finite prefix trace through cell m;
r_j           = Z_(j-1)^(-1)Z_j, the faithful relative character of cell j;
R_CTP,j       = relative endpoint endomorphism before faithful character;
G             = a finite connected V005 realized graph;
E_G           = its oriented edge/cell set;
C_1(G)        = Z^(E_G), the integral edge-chain lattice;
partial_G     = B_G^T:C_1(G)->Z^(V_G);
C_G           = ker(partial_G), the integral conserved-cycle lattice;
A_G           = Hom(C_1(G),U(1)) isomorphic to U(1)^(E_G), edge cochains;
Gamma_G       = vertex-rephasing subgroup in A_G;
Q_G           = A_G/Gamma_G, the V005 physical finite cycle quotient;
q_G           = quotient map A_G->Q_G;
Hol_G         = Q_G->Hom(C_G,U(1)), V005's separating isomorphism;
epsilon       = an enumeration of E_G, never selected globally;
s_j           = signed traversal of epsilon(j), never selected globally;
J_omega       = forced signed-permutation action on prefix coordinates;
D_G           = the descent constructed below;
R             = independent bilocal source elsewhere in the program, not R_CTP.
```

“Cell” in this construction means an edge-resolved finite realization cell.
A raw CTP history segment with no signed incidence realization is not silently
renamed an edge; it is the boundary in Section 8.

---

## 4. G1 — the object

### 4.1 Signed enumerated realization members

For a finite connected realized graph `G`, a signed enumeration is

```text
eta=(epsilon,s),
epsilon:{1,...,N}->E_G a bijection,
s=(s_1,...,s_N), s_j in {+1,-1}.
```

`s_j=+1` means the record cell is read in the declared edge orientation;
`s_j=-1` means it is read oppositely. Retaining every `eta` is the
no-selection family. No enumeration or orientation is privileged.

For one member, define its prefix carrier

```text
P_eta={Z=(Z_0,...,Z_N):Z_0=1, Z_j in U(1)}.
```

Q-348/Q-349 give the global inverse

```text
r_j(Z)=Z_(j-1)^(-1)Z_j.                           (G1-1)
```

No logarithm or local branch enters.

### 4.2 Signed-permutation covariance

Let `omega` be a signed permutation of cells. On recovered cell characters,
it permutes coordinates and inverts precisely those with negative sign. The
forced action on prefixes is

```text
J_omega:=Pi_N compose omega compose Pi_N^(-1),     (G1-2)
```

where `Pi_N` is Q-348's triangular prefix map. Q-349 proves `(G1-2)` is a
global group automorphism and is the correct response to an edge-order
permutation.

Define the no-selection prefix object over `G` as the associated family

```text
P_G^fam := (disjoint union_eta P_eta)/~,

(eta,Z)~(eta omega^(-1),J_omega Z).                (G1-3)
```

This quotient changes presentation and source coordinates together. It does
not average, symmetrize, or hold the prefix tuple fixed while changing an
edge label—the precise error behind the terminal-scalar obstruction.

### 4.3 Codomain and required natural transformation

The target is V005's finite physical quotient

```text
Q_G=A_G/Gamma_G
   isomorphic to Hom(C_G,U(1)).                    (G1-4)
```

The desired object is a component for every finite realized `G`,

```text
D_G:P_G^fam->Q_G,                                  (G1-5)
```

natural under every declared signed cellular arrow and every change of
realization presentation.

```text
G1_OBJECT_STATED = COMPLETE
```

---

## 5. G2 — construction and certificates

### 5.1 Edge-cochain reconstruction

For a representative `(eta,Z)` with `eta=(epsilon,s)`, recover `r_j` by
`(G1-1)` and define an edge cochain

```text
Phi_eta(Z)=h in A_G,
h_(epsilon(j)):=r_j^(s_j).                         (G2-1)
```

This is the orientation-bearing seam. It does not assert that a CTP-closed
word is already an incidence cycle. It transports every relative character
to the edge named by the realization member, with the member's sign.

Define

```text
D_G([eta,Z]):=q_G(Phi_eta(Z)).                     (G2-2)
```

Equivalently, without choosing a cycle basis,

```text
Hol_G(D_G([eta,Z]))(c)
 =product_(j=1)^N r_j^(s_j c_(epsilon(j)))
 for every c in C_G.                               (G2-3)
```

Equation `(G2-3)` is a proof coordinate, not the definition of a selected
cycle basis; it quantifies over the complete lattice.

### 5.2 Well-definedness under the no-selection relation

Suppose

```text
(eta',Z')=(eta omega^(-1),J_omega Z).
```

By `(G1-2)`, recovering the cell characters from `Z'` gives exactly the
signed permutation `omega r`. The simultaneous change of `eta` sends each
permuted/inverted character back to the same oriented edge cochain. Hence

```text
Phi_(eta')(Z')=Phi_eta(Z),
D_G([eta',Z'])=D_G([eta,Z]).                       (G2-4)
```

Thus `(G2-2)` is independent of enumeration, orientation presentation, and
filtration member. No averaging can delete an antisymmetric cycle.

```text
SIGNED_ENUMERATION_INDEPENDENCE = PASS | TYPE-P
ORIENTATION_MEMBER_SELECTED = false | TYPE-S
EDGE_ORDER_SELECTED = false | TYPE-S
```

### 5.3 Gate-4 quotient compatibility

For vertex phases `g in U(1)^(V_G)`, let `delta_G g in A_G` be the edge
coboundary. Replacing `h` by `(delta_G g)h` leaves `q_G(h)` unchanged. On
cycles,

```text
product_e (delta_G g)_e^(c_e)=1
```

because `B_G^T c=0`. Therefore `(G2-2)` is representative-independent and
uses exactly V005's physical quotient.

```text
GATE4_QUOTIENT_COMPATIBILITY = PASS | TYPE-P
FRAME_SELECTED = false | TYPE-S
```

### 5.4 Family automorphisms

Let `alpha:G->G'` be a signed incidence isomorphism. It induces:

```text
alpha_1:C_1(G)->C_1(G'),
alpha_A:A_G->A_(G'),
alpha_Q:Q_G->Q_(G'),
J_alpha:P_G^fam->P_(G')^fam.
```

The definitions give

```text
Phi_(G') J_alpha=alpha_A Phi_G,
D_(G') J_alpha=alpha_Q D_G.                        (G2-5)
```

This is covariance, not pointwise invariance.

### 5.5 General signed cellular restriction

Let a coarse stage `G_N` be realized inside/refined by `G_M` through an
integral signed chain map

```text
f_1:C_1(G_N)->C_1(G_M),
partial_M f_1=f_0 partial_N.                       (G2-6)
```

For a fine edge cochain `h_M`, its coarse pullback is defined before any
output is read:

```text
(f_1^*h_M)(e)
 :=h_M(f_1 e)
 =product_(e' in E_M) h_M(e')^((f_1)_(e',e)).     (G2-7)
```

At prefix level, `(G2-7)` is executable using only:

```text
recover cell characters by consecutive ratios;
multiply characters for batching;
invert characters for reversed orientation;
re-prefix with Pi_N.
```

All four operations are ratified or proved in Q-348/Q-349 and DoR-016.
Call the resulting source map `P_f`.

The chain identity `(G2-6)` sends vertex coboundaries to vertex
coboundaries, so `(G2-7)` descends to

```text
rho_f:Q_(G_M)->Q_(G_N),
rho_f([h_M])=[f_1^*h_M].                           (G2-8)
```

Now compute, without tuning any map to the output:

```text
D_(G_N) P_f([eta_M,Z_M])
 =q_(G_N)(f_1^* Phi_(G_M)([eta_M,Z_M]))
 =rho_f q_(G_M)(Phi_(G_M)([eta_M,Z_M]))
 =rho_f D_(G_M)([eta_M,Z_M]).                     (G2-9)
```

Hence the physical square commutes. Composition is automatic from
`(g_1 f_1)^*=f_1^* g_1^*`.

```text
FAMILY_RESTRICTION_NATURALITY = PASS | TYPE-P |
  scope: declared signed cellular arrows
```

This proof does not consume Q-347 E2.4. At rank one, comparing `(G2-9)` to
Lane 1's repaired artifact is pending point P-432-2.

### 5.6 Batching

If one coarse cell is a signed path of fine cells, `(G2-7)` reads

```text
r_coarse=product_(j in batch) r_j^(sign_j).        (G2-10)
```

Q-349's batching identity reconstructs that product from fine prefixes. The
fine-to-coarse square is `(G2-9)`. No inverse claim is made: one coarse
terminal character does not reconstruct the interior fine factors.

The Q-341 pathology does not occur. A coarse and an edge-by-edge
presentation are not assigned different physical rules; they are related by
the one chain map `(G2-6)` and the same pullback `(G2-7)`.

```text
BATCHING_COVARIANCE = PASS | TYPE-P
COARSE_TO_FINE_INTERIOR_RECONSTRUCTION = false | TYPE-R
FILTRATION_MEMBER_SELECTED = false | TYPE-S
```

### 5.7 Reality

The ratified involution sends

```text
r_j->conjugate(r_j)=r_j^(-1),
h_e->conjugate(h_e),
q_G(h)->Theta_G q_G(h).
```

Consecutive ratios commute with conjugation, and so do signed products.
Therefore

```text
D_G(Theta_P Z)=Theta_G D_G(Z).                     (G2-11)
```

This is covariance only.

```text
REALITY_COVARIANCE = PASS | TYPE-P
POINTWISE_REALITY_INVARIANCE_CLAIMED = false | TYPE-R
```

### 5.8 Identity zero extension

Appending an identity cell gives

```text
Z_(N+1)=Z_N,
r_(N+1)=Z_N^(-1)Z_(N+1)=1.
```

The corresponding new edge cochain coordinate is one. It contributes one to
every cycle holonomy and commutes with the physical restriction. Thus

```text
D_(N+1) j_NM^prefix=j_NM^Q,phys D_N              (G2-12)
```

for the declared identity extension.

```text
IDENTITY_ZERO_EXTENSION = PASS | TYPE-P
```

### 5.9 Agreement with Q-313 at cycle rank zero and one

At cycle rank zero, `Q_G` is the point and `(G2-2)` is the unique terminal
cycle projection. Nontrivial open-path access remains upstream.

For the sealed rank-one square, use the **sealed** signed traversal—not a new
orientation choice—whose primitive cycle is

```text
c_square=(1,-1,1,-1).
```

The signed realization reads the four relative cell characters in the
traversal direction, so `s_j=c_(epsilon(j))`. Then

```text
Hol_(c_square)(D_G(Z))
 =product_j (r_j^(s_j))^(c_(epsilon(j)))
 =product_j r_j
 =Z_N,                                             (G2-13)
```

because each nonzero coefficient is `+1` or `-1` and `s_j c_e=1`.
Q-313 proves there is a unique quotient class with this holonomy. Hence

```text
D_(G_square)=Hol_(c_square)^(-1) compose Z_N
            =T_N^char.                             (G2-14)
```

Attached tree cells under the Q-313/Q-347 rank-preserving domain are identity
zero extensions and contribute one. Thus the same comparison applies to the
Q-313-compatible rank-one family.

```text
Q313_POINTWISE_AGREEMENT = PASS | TYPE-P
Q315_FIXED_SQUARE_AGREEMENT = PASS | TYPE-P
Q347_REPAIRED_RANK1_FAMILY_AGREEMENT = PENDING | point:P-432-1
```

No line in `(G2-13)` or `(G2-14)` uses Lane 1's pending repair. The pending
item is only the merge with Q-347's attempted all-rank-one naturality claim.

### 5.10 Construction standing

```text
D_PREFIX_TO_CYCLE_EDGE_RESOLVED = CONSTRUCTED | TYPE-P |
  premises: DoR-009, DoR-015, DoR-016, Q-348, Q-349

ARBITRARY_CYCLE_RANK_LIMIT = none | TYPE-R |
  test: formula G2-3 quantifies over all c in C_G

CYCLE_BASIS_SELECTED = false | TYPE-S
REALIZATION_MEMBER_SELECTED = false | TYPE-S
EDGE_SELECTED = false | TYPE-S
ORIENTATION_SELECTED = false | TYPE-S
```

---

## 6. G3 — kernel and no-deletion certificate

### 6.1 Prefix-coordinate kernel

Q-348 proves that the complete prefix map has trivial kernel on the
cellwise faithful relative characters:

```text
ker(Pi_N)={identity}.                              (G3-1)
```

Thus no kernel is introduced before edge-cochain reconstruction.

### 6.2 Physical descent kernel

The map `Phi_G:P_G^fam->A_G` induced by `(G2-1)` is an isomorphism: an edge
cochain produces its compatible prefix family in every signed enumeration,
and `(G2-1)` recovers it uniquely.

Since `D_G=q_G Phi_G`,

```text
ker(D_G)=Phi_G^(-1)(Gamma_G).                      (G3-2)
```

Equivalently, two prefix families have the same output exactly when their
edge-cochain ratio is a vertex coboundary. In cycle language,

```text
D_G(Z)=D_G(Z')
 iff product_e (h'_e h_e^(-1))^(c_e)=1
     for every c in C_G.                           (G3-3)
```

The equivalence of `(G3-2)` and `(G3-3)` is the finite exact dual sequence
behind V005's separation theorem. A spanning tree may prove it locally, but
no spanning tree is used by or frozen into the construction.

Presentation relabelings in `(G1-3)` are not additional physical kernel;
they are equality of two descriptions of the same edge cochain. The raw-pair
fiber `(T_+,T_-) -> R_CTP` lies upstream of the declared domain and is not
silently counted as a kernel of `D_G`.

```text
LAWFUL_KERNEL = vertex rephasing Gamma_G
OPEN_PATH_ACCESS_MAY_SURVIVE_UPSTREAM = true
RAW_PAIR_KERNEL_ASSIGNED_TO_D_G = false | TYPE-R
```

### 6.3 Surjectivity and no record-visible deletion

For any physical quotient class `[h] in Q_G`, choose a representative only
inside this existence proof. Form its compatible prefix family using
`r_j=h_(epsilon(j))^(s_j)` and cumulative products. Then `(G2-1)` recovers
`h`, so

```text
D_G([Z_h])=[h].                                    (G3-4)
```

Therefore `D_G` is surjective at every finite cycle rank.

Dualizing, the pullback on physical cycle characters is

```text
D_G^*:C_G->Hom(P_G^fam,U(1)),
(D_G^*c)(Z)=Hol_G(D_G(Z))(c).                      (G3-5)
```

If `D_G^*c` is the trivial character, surjectivity says `Hol_G(q)(c)=1` for
every `q in Q_G`. V005 separation then gives `c=0`. Hence

```text
ker(D_G^*)={0}.                                    (G3-6)
```

This is the certificate the terminal scalar failed: every nonzero
record-visible cycle remains visible after descent.

```text
DESCENT_SURJECTIVE_ALL_RANKS = true | TYPE-P
NO_RECORD_VISIBLE_CYCLE_DELETED = true | TYPE-P
TARGET_ANNIHILATOR = {0}
```

---

## 7. G4 — exact boundary and residual family

### 7.1 Edge-resolved scope

The construction above requires a typed signed association between relative
cells and the realized finite edge-chain carrier. On V005's finite
edge-resolved objects this association is presentation data, and retaining
all signed enumerations removes selection.

An arbitrary raw history object may instead arrive with no declared chain
realization. Then its cell lattice `Z^N` and the incidence lattice
`C_1(G)=Z^(E_G)` are merely two finite free lattices. Their ranks need not
agree, and no ratified clause says which cell contributes to which edge.

### 7.2 General candidate and exact criterion

The most general cellwise-character descent of the same structural kind is
specified by an integral cycle-to-cell map

```text
iota_G:C_G->Z^N.                                   (G4-1)
```

It would act by

```text
Hol_G(D_iota(r))(c)=product_(j=1)^N r_j^((iota_G c)_j).
                                                               (G4-2)
```

For a family, these maps must obey the chain/naturality square for every
realization arrow. No such `iota_G` is manufactured by Q-348; Q-348 supplies
the `r_j`, not their geometric incidence meaning.

The exact no-deletion criterion is

```text
ker(iota_G restricted to C_G)={0}.                (G4-3)
```

If `0!=c in ker(iota_G)`, `(G4-2)` makes the record-visible `c` character
identically one: deletion is proved. Conversely, if `iota_G` is injective,
every `U(1)` character on its image extends to the finite free cell lattice
because `U(1)` is divisible; the induced torus map is surjective onto
`Hom(C_G,U(1))`. Thus `(G4-3)` is also sufficient for no deletion.

The edge-resolved construction uses the canonical inclusion

```text
C_G subset C_1(G)=Z^(E_G),
```

expressed in every signed enumeration, so `(G4-3)` holds automatically.

### 7.3 Boundary verdict

For a non-edge-resolved history class, the residual family is

```text
Iota_G^adm={iota_G:C_G->Z^N integral, injective,
            family-natural under every admitted arrow}.        (G4-4)
```

The ratified corpus does not supply a member of `(G4-4)` or prove that the
family is nonempty for every arbitrary history/realization pairing. Choosing
one would be the same missing geometry that Q-313 and Q-349 refused to
invent.

```text
EDGE_RESOLVED_FULL_FAMILY = CONSTRUCTED | TYPE-P
NON_EDGE_RESOLVED_HISTORY_FAMILY = NO_CONSTRUCTION / TYPE-U
MISSING_INPUT = family-natural signed chain realization iota_G
RESIDUAL_FAMILY = Iota_G^adm
BOUNDARY_DEPENDS_ON_CYCLE_RANK = false | TYPE-R
BOUNDARY_DEPENDS_ON_REALIZATION_TYPING = true
```

This boundary is a full success of the audit: no rank-two obstruction
survives once the edge-resolved prefix family is present; only an untyped
cell-to-geometry seam remains outside that family.

---

## 8. G5 — regressions

### 8.1 One edge

For one connected oriented edge,

```text
C_G={0},
Q_G={*}.
```

The prefix family may contain a nonidentity relative character `r_1`, and
DoR-016 retains the corresponding endpoint-covariant access upstream.
Equation `(G2-2)` lands at the point because the entire edge cochain is a
vertex coboundary on a tree.

```text
ONE_EDGE_DESCENT = zero cycle class | PASS
ONE_EDGE_ACCESS_DELETED_UPSTREAM = false | TYPE-R
```

### 8.2 S8-A rank-two stage

Use oriented edge order `(a,b,d)` and

```text
c_1=(1,1,0),
c_2=(0,1,1),
c_3=(1,0,-1)=c_1-c_2.
```

For the matching signed member, Q-348 gives

```text
r_a=Z_1,
r_b=Z_1^(-1)Z_2,
r_d=Z_2^(-1)Z_3.
```

The constructed descent gives

```text
H_(c_1)=r_a r_b=Z_2,
H_(c_2)=r_b r_d=Z_1^(-1)Z_3,
H_(c_3)=r_a r_d^(-1)=Z_1 Z_2 Z_3^(-1).            (G5-1)
```

All three named cycle characters are present; only two are independent, as
they must satisfy `H_(c_3)=H_(c_1)H_(c_2)^(-1)`. In particular `H_(c_3)` is
not forced to one.

Under the edge exchange `a<->d`, the recovered characters transform as

```text
(r_a,r_b,r_d)->(r_d,r_b,r_a),
```

and the prefixes transform by Q-349's forced automorphism

```text
Z_1'=Z_2^(-1)Z_3,
Z_2'=Z_1^(-1)Z_3,
Z_3'=Z_3.                                          (G5-2)
```

Substitution into `(G5-1)` yields

```text
H_(c_1)'=H_(c_2),
H_(c_2)'=H_(c_1),
H_(c_3)'=H_(c_3)^(-1),                            (G5-3)
```

matching `c_1<->c_2`, `c_3->-c_3`. The source is not held fixed, so Q-347's
terminal-scalar automorphism obstruction has no premise here.

```text
S8A_C1_HIT = PASS
S8A_C2_HIT = PASS
S8A_C3_HIT = PASS
S8A_C3_DELETED = false | TYPE-R
S8A_AUTOMORPHISM_COVARIANCE = PASS
```

### 8.3 Reality

Applying conjugation to every prefix and edge cochain gives `(G2-11)`.

```text
REALITY_REGRESSION = PASS
```

### 8.4 Batching

For a batch from fine cells `a` through `b`,

```text
r_[a,b]=Z_(a-1)^(-1)Z_b.
```

With signs, inverses are inserted exactly as in `(G2-10)`. The quotient
square is `(G2-9)`.

```text
BATCHING_REGRESSION = PASS
```

### 8.5 Identity zero extension

The new ratio is one and creates no holonomy.

```text
IDENTITY_ZERO_EXTENSION_REGRESSION = PASS
```

### 8.6 Hostile symmetrization attack

**Attack.** Avoid choosing an enumeration by averaging or multiplying over
all edge assignments while holding one terminal/prefix input fixed.

**Result.** Killed. On S8-A this makes the antisymmetric `c_3` coordinate
constant and recreates Q-347's obstruction. The lawful construction instead
quotients simultaneous changes `(eta,Z)->(eta omega^(-1),J_omega Z)`; it
never symmetrizes physical edge content.

```text
INVARIANT_AVERAGE_OVER_REALIZATIONS = REFUTED | TYPE-R
SIMULTANEOUS_COVARIANT_FAMILY_QUOTIENT = REQUIRED
```

---

## 9. G6 — typing, selections, and doors

### 9.1 Standing

| Object | Standing |
|---|---|
| prefix/cell triangular isomorphism | `TYPE-P`, Q-348/Q-349 |
| edge-resolved family object `P_G^fam` | derived class formation from all signed presentations; `TYPE-P` on finite V005 carriers |
| `Phi_G` edge-cochain reconstruction | `TYPE-P` |
| Gate-4 descent `D_G=q_G Phi_G` | `TYPE-P` |
| all-rank no-deletion certificate | `TYPE-P` |
| arbitrary non-edge-resolved `iota_G` | `TYPE-U` |
| Lane-1 repaired Q-347 rank-one family theorem | `PENDING` |
| transverse action comparison | `TYPE-U`, outside commission |
| 2PI/Legendre/stationary map | `TYPE-U`, outside commission |

### 9.2 No-selection audit

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

Both faithful character orientations are carried. The map contains no `p`;
symbolic `p` remains a downstream state/effect weight.

### 9.3 Class-formation and six-account row

```text
DOOR_PREFIX_FAMILY_QUOTIENT := (
  input_class = disjoint union of finite signed prefix presentations,
  equivalence = simultaneous signed relabeling by J_omega,
  topology = finite compact product topology,
  kernel = presentation equivalence only,
  image = edge-cochain torus A_G,
  sector_transfer = relative cell character -> oriented edge cochain,
  restriction_square = G2-9 PASS,
  Tail_action = none; finite compact class,
  selection = none
).

DOOR_GATE4_DESCENT := (
  input_class = A_G,
  operation = q_G,
  kernel = Gamma_G,
  image = Q_G all ranks,
  sector_transfer = edge cochain -> physical cycle quotient,
  restriction_square = G2-9 PASS,
  Tail_action = none; finite,
  no_deletion = D_G^* injective on C_G
).
```

No continuum completion, bidual, measure, contour, inverse, or action class
is formed.

```text
UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S
FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S
```

### 9.4 Action/2PI fence

The output `Q_G` is a physical cycle quotient class. It is not a scalar
transverse action, a Hessian, a 2PI block, a stationary point, or a response.

```text
ACTION_COMPARISON_SQUARE = NOT_BUILT / TYPE-U
PHYSICAL_TRANSVERSE_ACTION = NOT_BUILT / TYPE-U
PHYSICAL_P_VERDICT = NO_VERDICT
```

---

## 10. Final determination

The open escape constructs on every finite signed edge-resolved realization
and at every cycle rank:

```text
prefix traces
  --consecutive ratios-->
cellwise faithful relative characters
  --signed realization covariance-->
edge cochain h
  --Gate-4 quotient-->
physical cycle class [h].
```

The construction is family-natural because a realization change acts on the
prefix carrier by the forced `J_omega`, not trivially. Its physical kernel is
exactly vertex rephasing. It is surjective, and the pullback of the complete
conserved-cycle lattice is injective; therefore no record-visible cycle is
deleted at any rank. The S8-A `c_3` coordinate survives explicitly.

The construction does not solve an untyped history-to-geometry problem. If a
history class has no signed cell-to-edge chain realization, the residual
family `(G4-4)` remains `TYPE-U`; choosing a member is forbidden. That is the
only boundary found, and it is a carrier-typing boundary rather than a
cycle-rank obstruction.

```text
G1_OBJECT = COMPLETE
G2_CONSTRUCTION = COMPLETE_ON_EDGE_RESOLVED_FAMILY
G3_KERNEL_DISCLOSURE = COMPLETE
G4_BOUNDARY = NON_EDGE_RESOLVED_HISTORY_CLASS
G5_REGRESSIONS = PASS
G6_SELECTION_AND_DOOR_AUDIT = PASS

LEAD_RESULT = CONSTRUCTED-WITH-BOUNDARY

FAMILY_NATURAL_PREFIX_TO_CYCLE_DESCENT = CONSTRUCTED | TYPE-P |
  scope: finite signed edge-resolved V005 realization family, all ranks

TERMINAL_SCALAR_RANK2_OBSTRUCTION = STILL_CONFIRMED | TYPE-R
PREFIX_FAMILY_RANK2_OBSTRUCTION = REFUTED | TYPE-R |
  test: S8-A equations G5-1 through G5-3

NO_RECORD_VISIBLE_CYCLE_DELETED = true | TYPE-P
LAWFUL_KERNEL = vertex rephasing

NON_EDGE_RESOLVED_EXTENSION = NOT_BUILT / TYPE-U |
  would-build: family-natural signed chain realization iota_G satisfying G4-3

RANK01_LANE1_REPAIR = PENDING |
  consumption points: P-432-1, P-432-2, P-432-3;
  not a premise of this construction

ACTION_OR_2PI_COMPARISON_SQUARE = NOT_BUILT / TYPE-U
PHYSICAL_P_VERDICT = NO_VERDICT

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No alpha, `K_*`, root, response value, rank ratio, or measured constant was
evaluated.

