# STAGE8 TASK 4A NETWORK-SOURCING LAW V002 RE-REVIEW - LANE 1 V001

Date: 2026-08-03  
Task: PASTE 421 / Task 4a / adversarial re-review  
Lane: CODEX LANE 1  
Custody: independent reviewer of the Lane-2 V002 repair  

```text
ARTIFACT_UNDER_REVIEW =
  STAGE8_TASK4A_NETWORK_SOURCING_LAW_ADOPTION_PROPOSAL_CODEX_LANE2_V002.md
EXPECTED_SHA256 =
  9b2e42f8c1cf2791ce859ca8be64864dbce84d87a357426989db083b0db8641f
VERIFIED_SHA256 =
  9b2e42f8c1cf2791ce859ca8be64864dbce84d87a357426989db083b0db8641f

BRANCH_A_LEAD = KILL | item: S8-A
BRANCH_A_FAILURE =
  fixed-stage conservation is not closed under finite restriction;
  a conserved larger-stage cycle can restrict to a nonconserved smaller-stage
  coefficient, so the Branch-A emitter becomes undefined without the
  projector it explicitly refuses

BRANCH_B_LEAD = KILL | items: S5-B and S8-B
BRANCH_B_FAILURE =
  the emitter starts from a doubled CTP history but outputs one endpoint
  morphism; the exact C5 tower needs the pair (T_+,T_-) through
  T_-^dagger T_+, and the displayed scalar zeta/product is not determined by
  the single covariant morphism without an additional endpoint contraction

V001_ONE_EDGE_KILL_REPAIRED_AT_FIXED_STAGE = true
V001_NO_IGNITION_STANDING_REPAIRED = true

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

Both branches are killed, but not by recurrence of V001's defects. V002
correctly repairs the one-edge scalar error in both branches and correctly
removes the all-tier no-ignition claim. The new failures are composition
failures:

1. Branch A defines a legal scalar source at each isolated finite stage but
   not a restriction-compatible family across stages.
2. Branch B defines a legal endpoint-covariant access object at one branch
   and one tier but does not carry the doubled CTP pair needed for its claimed
   influence-factor tower.

The fixed-stage graph algebra in Sections 4.2-4.4 of V002 is correct. The
five named doors are also genuinely absent. Those passes are preserved below.

---

## 1. Preflight, custody, and authorities

### 1.1 Locked process

`/Users/bgm/MB Work/alpha_supervision/LOCKED_PROCESS.md` was read in full
before the review.

```text
LOCKED_PROCESS_SHA256 =
  f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba
LANE_ACTION = seal, mirror artifact and sidecar, report hashes, stop
REVIEWER_ONLY_ACTIONS_TAKEN = none
```

### 1.2 Register head

The live register was checked before the proposal was opened.

```text
REGISTER_HEAD = Q-338
REGISTER_SHA256_AT_PREFLIGHT =
  193534d28cf4a7d18e945efc506299b7596866d71b23a1e91574004c90287448
REGISTER_PREFLIGHT = PASS
```

### 1.3 Proposal hash before reading

The archived proposal was hashed before substantive reading. It matched the
relay exactly, and its sidecar verified.

```text
PROPOSAL_HASH_CHECK = PASS
PROPOSAL_SIDECAR_CHECK = PASS
```

### 1.4 Seam authorities

| Authority | Verified SHA-256 | Use |
|---|---|---|
| Lane-1 C5 derivation, Q-335 | `e73a3716aa8141bbbb501ae24138050f27f1eca7b66dde05fee25334d6db67e7` | receiver-only direction, local J chart, absent network R |
| Lane-1 V001 cross-review, Q-337 | `e937869879b4613175c814c6b5a02eabc54607c1f9751a4e758d475ced6de21b` | R1-R8, one-edge attack, corrected no-ignition standing |
| DoR-009 | `11632fa30dfe9225c228f07a3be4717c73bdfc9e38b0c76c46d905d3fe193bc5` | C1-C8 and E_post |
| DoR-014 | `b6e4116df63403478d28be8cdb6589b091cc1aa8b6ad5a40776a28b135cd138f` | source germ ratification |
| DoR-014 Amendment 1 | `8191feb4316ddeb08ef832b644c41847b31698224f6ab16b65dc1e1e2a574e56` | amended pairing |
| DoR-014 Amendment 2 | `460da8c34e8a33503c0a5737f1d94b7a68cbb31fe636cd74c49e59a493efc282` | even normalization |
| source germ V007 | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | live L, Q, Xi, Z, W |
| DoR-015 | `617bd51a70860d2cfb2066640630ba37ec289d56255ebbe1433bc0dfcba0159d` | physical scalar cycle source versus endpoint transport |
| FIELD_SIGNATURE_PHYS V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | `ker(B_N^T)`, W3, tree theorem, endpoint covariance |
| transition law V002 | `db1808e4da38cbfed8b12017885aff1bf63b0378e9971c37294e21fa08766fee` | exact C5 raw and doubled finite laws |

Q-336 is used only through Q-337's correction. Q-338 is the receipt of the
repair under review, not independent evidence for its correctness.

### 1.5 Preflight verdict

```text
DOES_THE_OBJECT_EXIST = yes
IS_THE_VERSION_CURRENT = yes through Q-338
ARE_ITS_INPUTS_PRESENT = yes
CUSTODY_VALID = yes
PREFLIGHT = PASS
```

---

## 2. S1-S8 verdict table

| Item | Branch A | Branch B | One-line reason |
|---|---|---|---|
| S1 prior kills re-fired | **PASS** | **PASS** | A emits the unique zero scalar on the one-edge stage; B emits endpoint transport only; both state autonomous no ignition as `NO_VERDICT / TYPE-U`. |
| S2 restriction versus projection | **PASS** | **PASS / N/A** | At one fixed stage A's maximal preimage of `ker(B_N^T)` is forced by scalar port typing, not a selected projector; B performs no cycle restriction. |
| S3 minimal-stage computation | **PASS** | **PASS / N/A** | `ker(B_2^T)=span{(1,1)}`, the simple underlying-graph minimum is a triangle, and the displayed `x`, `Xi`, and `A_k` algebra is exact. |
| S4 connected-tree theorem | **PASS** | **PASS / N/A** | For every finite connected tree, incidence rank is `V-1` and `E=V-1`, hence `ker(B_N^T)={0}`. |
| S5 Branch-B typing | **PASS / N/A** | **KILL** | The global scalar d_J and network R costs are honest, but the claimed tower collapses a doubled CTP input to one raw endpoint morphism and then scalarizes it as `zeta`. |
| S6 five doors | **PASS** | **PASS** | All five maps are absent from the bounded ratified stack and are correctly `TYPE-U`; none is silently opened. |
| S7 selection-freedom | **PASS** | **PASS** | No branch, rank, ratio, physical orientation, cycle basis, or endpoint frame is selected; the comparison table does not recommend. |
| S8 fresh attacks | **KILL** | **KILL** | A fails finite restriction on an explicit conserved larger-stage cycle; B loses the CTP branch pair and has no family-wide scalar product of endpoint morphisms. |

```text
S1_A = PASS
S1_B = PASS
S2_A = PASS
S2_B = PASS_NOT_APPLICABLE
S3_A = PASS
S3_B = PASS_NOT_APPLICABLE
S4_A = PASS
S4_B = PASS_NOT_APPLICABLE
S5_A = PASS_NOT_APPLICABLE
S5_B = KILL
S6_A = PASS
S6_B = PASS
S7_A = PASS
S7_B = PASS
S8_A = KILL
S8_B = KILL
```

---

## 3. S1 - re-fire R7, R3, and R8

### 3.1 Branch A on the one-edge stage

Use the exact V001 counterexample:

```text
B_1=[-1,1],
u_e=exp(i epsilon),
eta_e=i epsilon,
q_e^0=(i)^(-1)eta_e=epsilon !=0.                    (S1-1)
```

Then

```text
B_1^T q^0=(-epsilon,epsilon)^T !=0.                 (S1-2)
```

V002's Branch-A scalar codomain on a connected one-edge tree is
`ker(B_1^T)={0}`. There is exactly one map from any history set to the zero
space. V002 uses it:

```text
q^A=0,
d_J^A=0,
d_R^A=0.                                           (S1-3)
```

No nonzero scalar is emitted. The old R7 counterexample therefore passes at
this fixed stage. This is explicit at V002 `:420-454`.

### 3.2 Branch B on the one-edge stage

V002 defines

```text
d_acc^B[h]=(E_e^s,E_e^t,T_e[h]),
T_e:E_e^s->E_e^t,
T_e[g.h]=g_t T_e[h] g_s^(-1).                       (S1-4)
```

There is no displayed map

```text
d_J^B:Trans_ep->E_J
```

and no `d_R^B`. V002 explicitly denies both scalar-port insertions at
`:493-499,513-540,595-609`. The R7 one-edge transport is allowed, but it does
not reach `E_J` or `E_R`.

```text
BRANCH_B_ONE_EDGE_TRANSPORT = allowed proposal object
BRANCH_B_ONE_EDGE_SCALAR_SOURCE = none
```

This old regression passes. S5 and S8 test a later claim, not the emission
signature in `(S1-4)`.

### 3.3 R3/R8 standing scan

The exact required statement appears at V002 lines 24 and 714-725:

```text
AUTONOMOUS_READY_NETWORK_NO_IGNITION = NO_VERDICT / TYPE-U
NS28_AUTONOMOUS_INDUCTION = NOT_AVAILABLE / TYPE-U.  (S1-5)
```

The only positive base case is:

```text
READY_IDENTITY_FIRST_EMISSION = ZERO_OR_IDENTITY |
  PASS_WITHIN_PROPOSAL.                              (S1-6)
```

No all-tier no-ignition theorem survives. The remaining `TYPE-R` statements
say that V001's promotion is not retained; they do not repeat the killed
physical claim.

```text
R7_REPAIRED_AT_ONE_EDGE_A = true
R7_REPAIRED_AT_ONE_EDGE_B = true
R3_RECURRENCE_REPEATED = false
R8_TYPE_R_NO_IGNITION_REPEATED = false
S1_A = PASS
S1_B = PASS
```

---

## 4. S2 - fixed-stage restriction versus projection

### 4.1 Typing chain

At a fixed finite stage, the chain is:

```text
h in Hist_emit,N
  -> q_N^0(h) in R^(E_N)
  -> scalar physical source is legal iff B_N^T q_N^0(h)=0
  -> q_N^0(h) in ker(B_N^T)=J_fin,N.                 (S2-1)
```

The second implication is DoR-015/V005, not a V002 preference. V005 states
that the Gate-4 tangent is `coker(B_N)` and its scalar source dual is
`ker(B_N^T)`; a literal open-edge scalar does not descend
(`STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md:90-124`).

V002 takes the maximal domain on which the already defined `q_N^0` is well
typed:

```text
Hist_A,N=(q_N^0)^(-1)(ker(B_N^T)),
q_N^A=q_N^0|Hist_A,N.                               (S2-2)
```

No inner product, cycle basis, complement, or map
`P_cyc:R^(E_N)->ker(B_N^T)` is used. Every history whose unchanged output is
already physical is retained. Thus `(S2-2)` is a type-domain restriction, not
a selected projection.

### 4.2 What this pass does not prove

The pass is fixed-stage only. It does not show that the family
`{Hist_A,N}_N` is closed under the sequential restriction maps. That separate
claim fails in S8-A. Fixed-stage port typing and interstage naturality are
different obligations.

```text
FIXED_STAGE_RESTRICTION_FORCED_BY_DOR015 = true
CANONICAL_PROJECTOR_RATIFIED = false
PROJECTOR_USED_BY_V002 = false
FIXED_STAGE_DOMAIN_SELECTION_HIDDEN = false
INTERSTAGE_RESTRICTION_CLOSURE = tested separately in S8-A
S2_A = PASS
S2_B = PASS_NOT_APPLICABLE
```

---

## 5. S3 - independent minimal-stage computation

### 5.1 Reciprocal two-edge multigraph

For

```text
e_12:1->2,
e_21:2->1,
B_2=[[-1, 1],
     [ 1,-1]],                                      (S3-1)
```

one obtains

```text
B_2^T(q_12,q_21)^T
 =(-q_12+q_21, q_12-q_21)^T.                        (S3-2)
```

Both components vanish iff `q_12=q_21=s`. Hence

```text
ker(B_2^T)=span{(1,1)}.                             (S3-3)
```

The graph has `V=2`, `E=2`, and cycle rank `E-V+1=1`. A connected
two-vertex one-edge graph has cycle rank zero. Thus the displayed directed
multigraph is minimal in the category allowing two distinct antiparallel
arcs.

If the network category is an underlying simple graph in which an undirected
vertex pair supports only one edge, a two-vertex cycle is forbidden. The
smallest connected simple graph with `E-V+1=1` has `V=3`, `E=3`, namely a
triangle. V002 states this category condition explicitly; it does not claim
that every definition of a simple digraph excludes a directed digon.

### 5.2 Exact contraction and exponent

On the matched local chart, take

```text
q^A=s(1,1),
n in {+1,-1}.                                       (S3-4)
```

Then

```text
x=L_n^Theta(d_J^A)
 =i n(q_12+q_21)
 =2 i n s.                                          (S3-5)
```

V007 gives

```text
Q_n^even(d_R^A)=hbar x^2.                           (S3-6)
```

Since `n^2=1`,

```text
x^2=(2 i n s)^2=-4s^2,

Xi=x-(hbar/2)x^2
  =2 i n s-(hbar/2)(-4s^2)
  =2 i n s+2 hbar s^2.                              (S3-7)
```

For repeated admitted history:

```text
S_k=k Xi,
A_k=(1-p)+p exp(k Xi).                              (S3-8)
```

The `+2 hbar s^2` in `(S3-7)` follows from the minus in
`Xi=L-(1/2)Q` and `i^2=-1`. It does not reverse the Q-276 correction. Q-276
states

```text
D^2 Log Z|_0=-p(1-p) ell_delta tensor ell_delta,    (S3-9)
```

which is a Hessian sign downstream of `Xi`, not a replacement of `(S3-7)`.
The W convention `W=-i hbar Log Z` also enters after `Xi` and contributes no
second `hbar` here.

### 5.3 Orientation covariance

Let `D` be a diagonal edge reorientation matrix with entries `+1` or `-1`.
Under change of oriented edge basis,

```text
B' = D B,
q' = D q,
ell' = ell compose D.                               (S3-10)
```

Because `D^T D=I`,

```text
(B')^T q'=B^T D^T D q=B^T q,
ell'(q')=ell(D D q)=ell(q).                         (S3-11)
```

Thus row, coefficient, and dual covector change together. The invariant
object is `ell(iota_delta q)`; `2 i n s` is its coordinate in the displayed
orientation, not a selected physical orientation.

```text
S3_KERNEL = PASS
S3_SIMPLE_UNDERLYING_GRAPH_TRIANGLE = PASS
S3_x = 2*i*n*s
S3_Xi = 2*i*n*s+2*hbar*s^2
S3_TOWER = PASS
S3_ORIENTATION_COVARIANCE = PASS
S3_A = PASS
S3_B = PASS_NOT_APPLICABLE
```

---

## 6. S4 - connected-tree zero theorem

For any finite connected directed graph, changing edge orientations does not
change incidence rank. The incidence matrix has

```text
rank(B_N)=V-1.                                      (S4-1)
```

Therefore

```text
dim ker(B_N^T)
 =E-rank(B_N^T)
 =E-(V-1)
 =E-V+1.                                            (S4-2)
```

Every connected tree has `E=V-1`, so `(S4-2)` is zero. A zero-dimensional
kernel is exactly `{0}`:

```text
ker(B_N^T)={0}.                                     (S4-3)
```

This holds for every connected finite tree, not just the one-edge tree.
Consequently every Branch-A scalar and its rank-one bilocal vanish on every
tree stage. Branch B's endpoint access remains outside this scalar theorem.

```text
CONNECTED_TREE_SCALAR_SOURCE_KERNEL = {0}
CONNECTED_TREE_BRANCH_A_dJ = 0
CONNECTED_TREE_BRANCH_A_dR = 0
S4_A = PASS
S4_B = PASS_NOT_APPLICABLE
```

---

## 7. S5 - Branch-B typing and exact costs

### 7.1 What is correctly typed

The Branch-B emitter itself is an endpoint-covariant tuple, not a V007
source. Its law

```text
T_e[g.h]=g_t T_e[h] g_s^(-1)                       (S5-1)
```

matches V005's open-path side. V005 permits a physical scalar consumer only
after either closed-cycle cancellation or contraction with matching endpoint
data
(`STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md:458-464`).

V002 correctly does not send `(S5-1)` directly into `E_J` or `E_R`.

### 7.2 The global d_J cost is honest

The R1 equation remains true in any common connected local chart:

```text
exp(i n sum q)=product u.                           (S5-2)
```

It does not globalize to a scalar V007 `d_J` for two independent reasons:

1. there is no global single-valued additive `Log` on `U(1)`; and
2. DoR-015 removes bare open-edge scalar coordinates from the physical
   quotient.

Q-335 already made exactly this distinction: local finite J-chart matching
passes, while global equality with `E_J` is refuted
(`STAGE8_TASK4A_C5_EXTERNAL_HISTORY_TO_MUTUAL_SOURCING_DRIVE_DERIVATION_ARM_LANE1_V001.md:318-340`).

V002 therefore does not give up too much. The lawful surviving statement is
an access-chart check, not a global scalar source map.

### 7.3 The network-R cost is honest

Q-335 reads the ratified C5 law and finds it independent of the V007 bilocal
`R` port. V005 supplies a bilocal source carrier, but no network map from an
endpoint transport to that carrier and no C5 access-side receiver for a
network `R` datum. A carrier is not a receiver law.

```text
GLOBAL_BRANCH_B_dJ = absent correctly
LOCAL_BRANCH_B_J_CHART_CHECK = retained
NETWORK_R_ACCESS_RECEIVER = TYPE-U
```

### 7.4 Hidden scalarization in the claimed tower

The pass ends before V002 Section 5.3. The shared input is explicitly a
**doubled** compact history:

```text
h=(z_+,z_-),
u=conjugate(z_-)z_+.                                (S5-3)
```

See V002 `:140-161`. The exact ratified finite C5 trace is likewise

```text
Z_N[A_+,A_-]
 =product_j conjugate(z_(-,j))z_(+,j),              (S5-4)
```

at
`STAGE8_SOURCE_COUPLED_RECORD_TRANSITION_LAW_ADOPTION_PROPOSAL_V002.md:395-425`.

But Branch B outputs one morphism

```text
T[h]:E_s->E_t                                       (S5-5)
```

with raw endpoint covariance, then defines

```text
zeta=chi(T),
F=P_0+zeta P_ch,
A_k=(1-p)+p product_t zeta_t.                       (S5-6)
```

There are only two possible readings of `(S5-5)`:

1. **Raw-branch reading.** `T` is one of `T_+` or `T_-`. Its covariance
   `g_t T g_s^(-1)` is correct, but one raw morphism does not determine
   `conjugate(z_-)z_+`.
2. **Relative-CTP reading.** `T` is intended to encode
   `T_-^dagger T_+`. Then its declared type and covariance are wrong. The
   relative object is an endomorphism of an endpoint fiber, and under common
   endpoint gauge it transforms by conjugation there; for `U(1)` it is
   invariant. It is not a raw `E_s->E_t` morphism obeying `(S5-1)`.

No third map is displayed that combines the pair into a raw-covariant
morphism while retaining exact `(S5-4)`. Such a map would require reference
endpoint transport or matching endpoint data and would be another field.

An exact counterpair makes the loss visible. Fix the same forward transport
`z_+` and choose two different backward transports `z_-` and `z_-'`. The
singular forward object is identical, but

```text
conjugate(z_-)z_+ != conjugate(z_-')z_+             (S5-7)
```

for a generic choice. Therefore no function of the single raw `T_+` can
reproduce the exact doubled character.

The phrase "evaluated by C5 with matching endpoint data" at V002 `:544-565`
does not instantiate the missing pair or contraction. It also conflicts with
the statement at `:488-491` that no scalar contraction is selected.

```text
BRANCH_B_EMISSION_TO_EJ_ER = absent correctly
BRANCH_B_GLOBAL_dJ_COST = honest
BRANCH_B_NETWORK_R_COST = honest
BRANCH_B_CTP_PAIR_PRESERVED = false
BRANCH_B_EXACT_ACCESS_TOWER = FAIL
S5_A = PASS_NOT_APPLICABLE
S5_B = KILL
```

---

## 8. S6 - five-door audit

### 8.1 B scalar-source map

No ratified map has signature

```text
Trans_ep -> E_J.                                    (S6-1)
```

V005 permits endpoint-covariant consumption with matching endpoint data, but
that is not a map to the scalar V007 source port. Q-335 proves only a local
chart compatibility. The required global source scalarization remains
unbuilt.

### 8.2 B network-R receiver

No ratified map has signature

```text
Trans_ep or endpoint bilocal -> C5 network R input. (S6-2)
```

C5 contains no `R` datum. V007's `R` carrier and functional do not create a
network receiver.

### 8.3 Port-to-write-history update

The bounded sweep from the V001 review remains current. The stack contains
history-to-write maps, source functionals, source riggings, holonomy maps,
and endpoint intertwiners, but no

```text
(received port tuple or access object, current history)
  -> next compact write history.                    (S6-3)
```

### 8.4 Joint network state/effect contraction

The finite ready-record trace within one ratified record system is not a
joint contraction of two network systems. Q-335 states that multiplying the
two system amplitudes needs an independently certified joint state and
interaction rule, and C5 supplies neither
(`STAGE8_TASK4A_C5_EXTERNAL_HISTORY_TO_MUTUAL_SOURCING_DRIVE_DERIVATION_ARM_LANE1_V001.md:551-559`).

### 8.5 Continuum response

No object in the bounded network proposal or frozen finite authorities is a
completed continuum response map. The relevant measure, contour, domains,
background, inverse/Schur, and response image remain outside this proposal.

### 8.6 Type verdict

Each door is required by a named possible consumer but not built. `TYPE-U`,
not `TYPE-S`, is therefore correct.

| Door | Ratified-stack result | Type |
|---|---|---|
| Branch-B transport to scalar source | absent | `TYPE-U` |
| Branch-B network R receiver | absent | `TYPE-U` |
| received object to write history | absent | `TYPE-U` |
| joint network state/effect contraction | absent | `TYPE-U` |
| continuum response | absent | `TYPE-U` |

The Branch-B kill in S5 does not mean a door was silently opened. It means
the proposal claimed an exact tower without constructing the data one of
these boundaries requires.

```text
S6_A = PASS
S6_B = PASS
```

---

## 9. S7 - selection and target-independence scan

### 9.1 Family choices

The proposal retains both branches and explicitly sets

```text
BRANCH_SELECTED=false.                              (S7-1)
```

Branch A uses the whole kernel, not a cycle basis. `(1,1)` is a proof
representative of a one-dimensional displayed kernel. Branch B retains the
whole endpoint torsor/intertwiner family. No endpoint frame is selected.

The orientation computation in S3 is covariant under all edge-basis
reorientations; no physical orientation member is selected by displaying
one incidence matrix.

### 9.2 Rank discipline

Every occurrence of

```text
p_i=r_(ch,i)/(r_(0,i)+r_(ch,i))                     (S7-2)
```

is symbolic. No rank pair is chosen and no ratio is evaluated.

### 9.3 Target audit

The branch definitions are justified from DoR-015's type fork. Neither uses
the resulting exponent, tower growth, response, coupling, or any terminal
quantity as a membership predicate. The comparison table at V002 Section 10
lists costs symmetrically and contains no ranking or recommendation.

Textual occurrences of downstream fenced words occur only in terminal scope
declarations and door descriptions, not in construction criteria.

```text
BRANCH_MEMBER_SELECTED = false
RANK_OR_RATIO_SELECTED = false
ORIENTATION_MEMBER_SELECTED = false
CYCLE_BASIS_SELECTED = false
ENDPOINT_FRAME_SELECTED = false
TARGET_OUTPUT_USED_FOR_BRANCH_MEMBERSHIP = false
COMPARISON_TABLE_RECOMMENDS = false
S7_A = PASS
S7_B = PASS
```

---

## 10. S8-A - fresh Branch-A restriction-naturality counterexample

This attack is not V002's hidden-projector or empty-domain attack. It tests
the opposite arrow of the directed system: restriction of a new large-stage
cycle to an old stage.

### 10.1 Two finite stages

Let stage `N` have two distinct oriented edges:

```text
a:1->2,
b:2->1,

B_N=[[-1, 1],
     [ 1,-1]].                                      (S8A-1)
```

Its scalar source kernel is `span{(1,1)}`.

Let stage `M` retain `a,b` and add a third distinct edge

```text
d:1->2,

B_M=[[-1, 1],
     [ 1,-1],
     [-1, 1]].                                      (S8A-2)
```

Take the larger-stage coefficient

```text
q_M=(1,0,-1).                                       (S8A-3)
```

Direct multiplication gives

```text
B_M^T q_M
 =(-1,1)+(1,-1)
 =(0,0).                                            (S8A-4)
```

Thus `q_M` is an admitted nonzero Branch-A scalar source at stage `M`.

### 10.2 Restriction failure

The shared history restriction in V002 `NS2-2` forgets the later edge. Its
candidate coordinate is therefore

```text
rho_MN q_M=(1,0).                                   (S8A-5)
```

But

```text
B_N^T(1,0)=(-1,1) !=0.                              (S8A-6)
```

Hence the restricted history is outside `Hist_A,N`, even though its parent
history was inside `Hist_A,M`:

```text
rho_MN(Hist_A,M) not_subset Hist_A,N.               (S8A-7)
```

Branch A is therefore not a restriction-compatible family.

### 10.3 Why V005 zero-extension does not repair it

V005 proves the forward inclusion statement

```text
B_M^T j_NM(c)=j_V(B_N^T c)=0.                       (S8A-8)
```

An old cycle remains a cycle after zero-extension. `(S8A-8)` says nothing
about the reverse restriction of an arbitrary new cycle, and `(S8A-3)` is an
exact counterexample to that converse.

V005's W3 precision says physical source restrictions are adjoints of the
retained isometric inclusions; naive truncation is invalid. Applying such an
adjoint would land in `ker(B_N^T)`, but it is a projection-like source map
depending on the retained source norm. V002 neither instantiates that map on
its history coordinate nor proves that it preserves the exact C5 character.
It instead explicitly refuses a cycle projector.

### 10.4 Repair shapes, not executed

Two bounded repairs are visible:

1. replace the stagewise domains by the projective subfamily whose every
   finite restriction is conserved; or
2. use the ratified W3 adjoint source restriction and prove a new commuting
   square against the history restriction and C5 character.

Neither construction appears in V002. The first is a further domain
restriction; the second is the missing map V002's fixed-stage discussion
avoids.

```text
BRANCH_A_FIXED_STAGE_PORT_TYPING = PASS
BRANCH_A_ZERO_EXTENSION_NATURALITY = PASS
BRANCH_A_GENERAL_FINITE_RESTRICTION_NATURALITY = FAIL
BRANCH_A_COMPLETED_HISTORY_DOMAIN = NOT_CONSTRUCTED
S8_A = KILL
```

---

## 11. S8-B - fresh Branch-B CTP-pair and endpoint-product attack

### 11.1 Pair-loss attack

The exact input is doubled:

```text
h=(T_+,T_-).                                        (S8B-1)
```

The exact C5 relative factor is determined by both components:

```text
R_CTP=T_-^dagger T_+,
zeta_CTP=conjugate(z_-)z_+.                         (S8B-2)
```

V002 Branch B exports only one morphism `T:E_s->E_t`. A map from a pair to
one raw morphism cannot be injective on the relative factor in general. For
fixed `T_+`, changing `T_-` leaves a forward-only export unchanged while
changing `(S8B-2)`. For a relative-only export, the declared raw endpoint
covariance and domain/codomain are wrong, as shown in S5.

Thus the exact doubled finite restriction is not reproduced.

### 11.2 Endpoint-coordinate product attack

Even before CTP doubling, a coordinate `zeta_t` of a raw morphism obeying

```text
T_t -> g_t T_t g_s^(-1)                             (S8B-3)
```

is not a frame-free scalar. If the same endpoint change applies at each
tier, the bare coordinate product transforms as

```text
product_(t=1)^k zeta_t
  ->(g_t g_s^(-1))^k product_(t=1)^k zeta_t.        (S8B-4)
```

That is neither invariant nor the covariance law of one endpoint morphism
unless intermediate endpoint data are supplied and contracted at every
tier. V002 says no scalar contraction or endpoint member is selected, and it
leaves the joint state/effect door unbuilt. It cannot simultaneously retain
the full torsor family and treat the bare product in `(S8B-4)` as the scalar
amplitude in `NS2-B6`.

The ratified C5 law can consume raw transports branch by branch as covariant
write operators. To obtain a scalar influence factor it must then execute the
actual doubled ready-record trace, which returns `(S8B-2)`, not the singular
definition `chi(T)`.

### 11.3 Repair shape, not executed

A lawful successor must keep

```text
d_acc^B[h]=(T_+[h],T_-[h])                          (S8B-5)
```

with both endpoint laws, then construct the relative endomorphism and run
the exact C5 doubled trace family-wide. It must distinguish:

1. endpoint-covariant raw access;
2. the relative CTP endomorphism; and
3. any final scalar state/effect contraction.

V002 collapses these three levels in `zeta`.

```text
BRANCH_B_RAW_ACCESS_EMISSION = PARTIAL_PASS
BRANCH_B_CTP_PAIR_EXPORTED = false
BRANCH_B_RELATIVE_ENDOMORPHISM_CONSTRUCTED = false
BRANCH_B_ENDPOINT_PRODUCT_FAMILY_WIDE = false
BRANCH_B_EXACT_TOWER = FAIL
S8_B = KILL
```

---

## 12. Consolidated disposition

### 12.1 Preserved repairs and passes

The following V002 work survives review:

1. both fixed-stage R7 one-edge regressions;
2. the verbatim `NO_VERDICT / TYPE-U` no-ignition correction;
3. the fixed-stage restriction-not-projection typing argument;
4. the complete connected-tree zero theorem;
5. `ker(B_2^T)=span{(1,1)}` and the graph-category distinction;
6. `x=2 i n s`, `Xi=2 i n s+2 hbar s^2`, and the Branch-A fixed-stage
   tower algebra;
7. the honest loss of global Branch-B scalar `d_J`;
8. the honest absence of a Branch-B network-R receiver;
9. all five TYPE-U door findings;
10. the no-selection, symbolic-rank, and target-independence accounting.

### 12.2 Branch A disposition

Branch A is not a completed sequential source law. It is a collection of
fixed-stage maps whose admissible domains are not closed under restriction.
The explicit pair `(S8A-1)` through `(S8A-6)` kills its claimed restriction
and completion standing.

### 12.3 Branch B disposition

Branch B correctly identifies the access-side carrier but does not preserve
the doubled CTP data needed by the exact finite influence functional. Its
single endpoint morphism cannot determine the claimed `zeta` and tower. The
raw access map may be a component of a successor, but V002's Branch B as a
network-sourcing law is incomplete and its exact tower claim fails.

### 12.4 Required repairs, not executed

```text
BRANCH_A_WOULD_REPAIR =
  a projectively conserved history family OR a W3-adjoint source restriction
  square with exact C5 compatibility

BRANCH_B_WOULD_REPAIR =
  an explicit doubled endpoint-transport pair, relative CTP endomorphism,
  and family-wide C5 trace/contraction
```

No branch, repair, graph category, rank, orientation, frame, or physical
output is selected in this reviewer artifact.

```text
FENCE_BLOCKED_STRUCTURAL_RESULT = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

BRANCH_A = KILLED (S8-A)

BRANCH_B = KILLED (S5-B and S8-B)

OVERALL = KILLED (both proposal branches require bounded carrier-composition repairs)
