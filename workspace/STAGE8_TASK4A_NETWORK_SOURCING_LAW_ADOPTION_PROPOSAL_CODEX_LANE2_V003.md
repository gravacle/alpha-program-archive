# Stage 8 Task 4a Network-Sourcing Law Adoption Proposal — Codex Lane 2 V003

**PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION (DoR-016/017 RESERVED)**

Date: 2026-08-03  
Task: PASTE 422 / Task 4a / second bounded repair  
Lane: CODEX LANE 2  
Register head: Q-339  
Custody: builder repairing its own V002; Lane 1 re-review required  

```text
NETWORK_SOURCING_LAW_V003 = PROPOSED_NOT_ADOPTED
V002_DISPOSITION = KILLED_BRANCH_A_BY_S8A; KILLED_BRANCH_B_BY_S5B_AND_S8B

BRANCH_A_ROUTE_1 = PROJECTIVELY_CONSERVED_HISTORY_FAMILY
BRANCH_A_ROUTE_2 = W3_ADJOINT_SOURCE_RESTRICTION_SQUARE
BRANCH_A_ROUTE_2_STRONG_HISTORY_SQUARE = REFUTED | TYPE-R
BRANCH_A_ROUTE_2_C5_CHARACTER_SQUARE = REFUTED_GLOBALLY | TYPE-R
BRANCH_A_ROUTE_2_S8A_C5_SPECIAL_CASE = PASS_WITHIN_PROPOSAL

BRANCH_B = DOUBLED_CTP_ENDPOINT_ACCESS
BRANCH_SELECTED = false | TYPE-S | scope: this proposal family

AUTONOMOUS_READY_NETWORK_NO_IGNITION = NO_VERDICT / TYPE-U
ONE_TIER_DELAY = AUTHORED_NOT_UNIQUELY_FORCED

TYPE_P_CLAIMS_IN_THIS_PROPOSAL = 0
RANK_PAIR_SELECTED = false | TYPE-S | scope: every displayed formula
RANK_RATIO_EVALUATED = false | TYPE-S | scope: every displayed formula
ORIENTATION_MEMBER_SELECTED = false | TYPE-S | scope: covariant representatives only
ENDPOINT_FRAME_SELECTED = false | TYPE-S | scope: full torsor family retained

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 0. Lead determination

The two named V002 repairs have now been executed.

**Branch A splits.** The projective family is a genuine restriction-natural
source law: every prefix is conserved by membership, and its coefficients are
exactly the direct product of the cycle kernels introduced at each stage
increment. On the S8-A tower with base edges `{a,b}` and later edge `{d}`, the
family is

```text
q_M=(s,s,0).
```

It is nonzero for `s!=0`, and the reciprocal-loop `x`, `Xi`, and `A_k` remain
unchanged. The W3 adjoint route is also instantiated, but its verdict is
split: it is the lawful physical source restriction, but it does **not**
commute with the sealed raw-history restriction. On the permanent triple it
sends

```text
(1,0,-1) -> (1/2,1/2),
```

where the raw history restriction is `(1,0)`. The C5 character happens to
agree on that balanced two-edge stage. A second explicit stage proves that
the C5 square also fails globally: a later edge closing an old dangling edge
has nontrivial raw restricted character but W3 image zero. Therefore W3
cannot replace the history restriction without an additional authored
history map. These are proved failures, not defects hidden by V003.

**Branch B is repaired at the doubled level.** It exports `(T_+,T_-)`, forms

```text
R_CTP=T_-^dagger T_+,
```

and only then runs the exact finite C5 ready-record trace. Raw access, relative
endomorphism, and scalar contraction are distinct objects. The existing
single-record finite contraction licenses an ordered per-system finite tower.
No joint two-system state/effect contraction or completed physical contraction
is claimed; those remain `TYPE-U` doors.

Neither physical branch is selected. The failed W3 strong square is removed
by proof, not by outcome-aware selection.

---

## 1. Preflight, verified review, and authorities

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = yes_partly |
  V002 and its sealed re-review exist; V003 did not

IS_THE_VERSION_CURRENT = yes_through_Q339

ARE_ITS_INPUTS_PRESENT = yes |
  V002, the re-review, DoR-009, DoR-014 plus amendments and V007,
  DoR-015/V005 including W3, and Q-335 through Q-339

PREFLIGHT = PASS
```

The re-review was hashed before it was read:

```text
RE_REVIEW_ARTIFACT =
  STAGE8_TASK4A_NETWORK_SOURCING_LAW_V002_RE_REVIEW_LANE1_V001.md
EXPECTED_SHA256 =
  e8a4e8ff00fa68418210669e391649f2a2bf6d924994817766d3217baaae678e
VERIFIED_SHA256 =
  e8a4e8ff00fa68418210669e391649f2a2bf6d924994817766d3217baaae678e
RE_REVIEW_SIDECAR_CHECK = PASS
```

Only after that check was the re-review read in full.

### 1.2 Frozen authorities

| Authority | SHA-256 / standing | Use |
|---|---|---|
| `LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | custody, fences, types |
| V002 proposal | `9b2e42f8c1cf2791ce859ca8be64864dbce84d87a357426989db083b0db8641f` | bounded repair base |
| V002 re-review | `e8a4e8ff00fa68418210669e391649f2a2bf6d924994817766d3217baaae678e` | S8-A/S8-B kills and ten survivors |
| DoR-009 | `11632fa30dfe9225c228f07a3be4717c73bdfc9e38b0c76c46d905d3fe193bc5` | C1-C8, `E_post`, doubled finite trace |
| transition-law V002 | `db1808e4da38cbfed8b12017885aff1bf63b0378e9971c37294e21fa08766fee` | exact `F_N`, `Z_N[A_+,A_-]` |
| source germ V007 | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | scalar `L`, `Q`, `Xi`, `Z`, W3 naturality |
| DoR-015 | `617bd51a70860d2cfb2066640630ba37ec289d56255ebbe1433bc0dfcba0159d` | physical source/transport typing and W3 precision |
| FIELD_SIGNATURE_PHYS V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | cycle kernels, endpoint torsors, zero extension |
| V005 final review | `c2251ed0e903ef4a0841e4008c1da612a41c57ef6778eff42dea00629a9fc1b1` | `rho_MN=i_NM^*` restriction precision |
| Q-335 | `e73a3716aa8141bbbb501ae24138050f27f1eca7b66dde05fee25334d6db67e7` | receiver-only C5 seam and absent network `R` |
| Q-337/Q-339 | live register standing | permanent regressions and corrected scope |

### 1.3 Custody and exclusions

This artifact is a proposal, not a self-certification. It performs no
register, governing-plan, tracker, git, commit, or push action. The fenced
holdout was not entered, listed, or searched.

---

## 2. The ten V002 survivors — preserved verbatim

The following text is copied verbatim from the re-review Section 12.1:

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

V003 changes none of those findings. The exact preserved operational forms
are restated where consumed below.

---

## 3. Shared local chart, timing, and fixed-stage facts

**PROPOSED_NOT_ADOPTED — PASS_WITHIN_PROPOSAL ONLY**

Retain V002's doubled local history chart:

```text
u_(a,n)[h_a]_j
  :=conjugate(z_(a,-,j)^n)z_(a,+,j)^n,

eta_(a,n)[h_a]_j:=Log_0(u_(a,n)[h_a]_j),

q_N^0[h]:=(i n_b)^(-1)tau_(ba)eta_(a,n_a)[h].      (NS3-1)
```

Only the common zero-anchored `Log_0` chart is used. Identity and equal CTP
histories give `eta=0`; reality and finite history restriction retain the
V002 laws.

The temporal rule remains

```text
t:    execute the E_post write and retain its doubled untraced history;
t:    evaluate the selected proposal branch;
t+d:  deliver to the neighbor for an authored fixed integer d>=1. (NS3-2)
```

No-post-output supplementation forces positive delay. It does not force
`d=1`. Every displayed tower uses the authored minimal representative
`d=1`, while the proposal retains the full positive-delay family.

```text
POSITIVE_DELAY_REQUIRED = true | inherited constraint
EXACT_ONE_TIER_DELAY_DERIVED = false | TYPE-R |
  counterfamily: every fixed d>=1 obeys the timing constraints
EXACT_ONE_TIER_DELAY = AUTHORED_NOT_UNIQUELY_FORCED
```

At each fixed stage the scalar type remains:

```text
q_N is physical scalar iff q_N in C_N:=ker(B_N^T). (NS3-3)
```

The maximal fixed-stage history domain is the preimage of `C_N`; no projector
is inferred. On a connected tree, incidence rank gives

```text
dim C_N=E-V+1=0,
```

so the unique scalar emission is zero. Branch B remains outside this scalar
theorem.

---

## 4. Branch A, route 1 — the projectively conserved family

**PROPOSED_NOT_ADOPTED — RESTRICTION-NATURAL BY CONSTRUCTION**

### 4.1 Definition

Let `Hist_M` be the doubled histories at a finite stage `M`, with sealed raw
history restrictions `r_MN:Hist_M->Hist_N`. Define

```text
Hist_A,M^proj
  :={h_M in Hist_M:
       B_N^T q_N^0(r_MN h_M)=0 for every N<=M},

q_A,N^proj(h_M):=q_N^0(r_MN h_M) in C_N.           (NS3-A1)
```

For a compatible completed history `h=(h_N)_N`, equivalently

```text
Hist_A^proj
  :={h in inverse_limit Hist_N:
       B_N^T q_N^0(h_N)=0 for every finite N}.      (NS3-A2)
```

The scalar and rank-one bilocal at stage `N` are unchanged:

```text
d_J,A,N^proj[h]
  :=T_(CTP,J,N)^(-1)(0,q_A,N^proj[h]),

v_A,N^proj[h]:=iota_(delta,N)q_A,N^proj[h],

d_R,A,N^proj[h]
  :=v_A,N^proj[h] symtensor v_A,N^proj[h].          (NS3-A3)
```

The `R` formula remains openly authored and has no C5 network-R provenance.

### 4.2 Restriction closure

Take `h_M in Hist_A,M^proj` and `L<=N<=M`. By definition,

```text
B_L^T q_L^0(r_ML h_M)=0.                            (NS3-A4)
```

History functoriality gives `r_ML=r_NL r_MN`. Hence

```text
B_L^T q_L^0(r_NL(r_MN h_M))=0
```

for every `L<=N`. Therefore

```text
r_MN h_M in Hist_A,N^proj,
r_MN(Hist_A,M^proj) subset Hist_A,N^proj.           (NS3-A5)
```

No converse or projector is used. Restriction closure is a membership
theorem, not an assertion that raw truncation preserves every stagewise cycle.

### 4.3 General coefficient characterization

Write the declared stage growth as disjoint edge increments

```text
E_m=E_(m-1) disjoint_union Delta E_m,
B_m=[B_(m-1); C_m],
q_m=(q_(m-1),r_m).                                  (NS3-A6)
```

Vertex zero-extension is implicit when new vertices appear. If the prefix is
already conserved, then

```text
B_m^Tq_m
  =j_V(B_(m-1)^Tq_(m-1))+C_m^T r_m
  =C_m^T r_m.                                       (NS3-A7)
```

Induction yields the exact characterization:

```text
q in Hist_A^proj
  iff q_base in ker(B_base^T)
      and r_m in ker(C_m^T) for every later stage increment m.
                                                               (NS3-A8)
```

Thus the projective coefficient family is the compatible product of the
cycle kernels introduced **within each declared increment**. A singleton
non-loop edge increment has zero kernel and must carry coefficient zero. A
stage increment containing a closed cycle may carry any coefficient in that
increment's full cycle kernel. This is the exact price of demanding naive
history-restriction naturality.

The characterization also states the refinement sensitivity honestly. If a
reciprocal pair is introduced as one stage block, it supports its cycle. If a
finer declared tower introduces the two non-loop edges one at a time, each
singleton increment is forced to zero. V003 selects neither filtration and
does not promote a fiberwise nonzero result to a family-invariant theorem.

### 4.4 S8-A stage and nonemptiness

Use the permanent stages

```text
N:{a:1->2,b:2->1},
M:{a:1->2,b:2->1,d:1->2}.
```

At `N`, conservation gives

```text
q_N=(s,s).
```

The later singleton increment has

```text
C_d=[-1,1],
ker(C_d^T)={0},
```

so `(NS3-A8)` gives exactly

```text
q_M=(s,s,0).                                        (NS3-A9)
```

For every sufficiently small nonzero `s` in the common chart, this is a
nonzero instantiated projective history. Extend it to every later stage by
V005 zero-extension and take every new history coordinate to be equal-CTP.
V005 gives

```text
B_L^T j_ML(q_M)=j_V(B_M^Tq_M)=0,
```

and every prefix remains the already verified projective prefix. Hence a
nonzero **completed** projective history exists; the family is not a zero
schema on the S8-A tower.

The killing V002 coefficient

```text
q_M^kill=(1,0,-1)
```

is excluded because its `N` restriction `(1,0)` is not conserved.

```text
S8A_UNIT_TRIPLE_PROJECTIVE_RESULT = EXCLUDED_BY_MEMBERSHIP |
  PASS_WITHIN_PROPOSAL
```

### 4.5 Reciprocal-loop tower

On the admitted base loop `q_N=s_t(1,1)`, the ten-item survivor algebra is
unchanged:

```text
x_t=2 i n s_t,
Xi_t=2 i n s_t+2 hbar s_t^2,

S_k=sum_(t=1)^k Xi_t,
D_k=(hbar/2)sum_(t=1)^k x_t^2,

A_k=(1-p)+p exp(S_k).                               (NS3-A10)
```

For repeated admitted `s_t=s`,

```text
A_k=(1-p)+p exp(k[2 i n s+2 hbar s^2]).             (NS3-A11)
```

Later singleton edge increments are zero by `(NS3-A8)`, so they do not alter
this tower. Later increments that are themselves cycles add independent
admitted cycle coordinates and use the general partial sum `(NS3-A10)`.

Therefore the minimal-cycle tower survives unchanged on the S8-A declared
tower and on every tower in which that reciprocal loop is a conserved base or
single increment. It does not survive a finer edge-by-edge filtration that
never introduces a nonzero cyclic increment. That dependence is reported,
not resolved by selecting a filtration.

### 4.6 R7 regressions

On the one-edge connected tree, `C_1={0}` and the unique Branch-A scalar is
zero for every history. On every connected tree, the same rank theorem gives

```text
q_A=d_J,A=d_R,A=0.                                  (NS3-A12)
```

Both the one-edge R7 regression and the complete tree-zero theorem survive
verbatim.

---

## 5. Branch A, route 2 — the W3 adjoint square

**PROPOSED_NOT_ADOPTED — SOURCE MAP INSTANTIATED; STRONG HISTORY SQUARE REFUTED**

### 5.1 W3 source restriction

V005's retained A4 Hilbert structure gives, for the isometric zero-extension
of conserved sources,

```text
i_NM:C_N=ker(B_N^T)->C_M=ker(B_M^T),
i_NM(c)=(c,0),

rho_MN^W3:=i_NM^*:C_M->C_N.                        (NS3-A13)
```

The maps are basis-free once the ratified A4 norm is fixed, obey

```text
rho_LN^W3=rho_MN^W3 rho_LM^W3,
rho_MN^W3 i_NM=Id_(C_N),                            (NS3-A14)
```

and are the lawful physical-source restrictions. No new basis or projector
choice is authored here.

Applied to the history emitter at stage `M`, the candidate W3-restricted
source is

```text
q_A,N^W3(h_M):=rho_MN^W3(q_A,M(h_M)).               (NS3-A15)
```

### 5.2 The two squares

The strong history/source square would require

```text
q_N^0(r_MN h_M)
  =rho_MN^W3(q_M^0(h_M)).                           (NS3-A16)
```

The exact C5 character square is weaker. Let

```text
Char_N(q):=exp(i n sum_(e in E_N)q_e).
```

It requires

```text
Char_N(q_N^0(r_MN h_M))
  =Char_N(rho_MN^W3(q_M^0(h_M))).                  (NS3-A17)
```

These are different obligations: C5 can be insensitive to a source vector
in the kernel of its character covector. Equality in `(NS3-A17)` for all
stages would require the C5 Riesz covector to lie in the retained old cycle
subspace at every restriction. The ratified data does not impose that on raw
history coordinates.

### 5.3 S8-A permanent regression, computed

Scale the regression vector by a sufficiently small chart parameter
`epsilon`:

```text
q_M=epsilon(1,0,-1) in C_M.                         (NS3-A18)
```

The old cycle line is `C_N=span{c_N}`, `c_N=(1,1)`, and its isometric
inclusion is `i_NM(c_N)=(1,1,0)`. In the retained orthonormal A4 coefficient
norm,

```text
rho_MN^W3(q_M)
  =[<q_M,(1,1,0)>/<(1,1,0),(1,1,0)>](1,1)
  =(epsilon/2)(1,1).                                (NS3-A19)
```

The sealed raw history restriction is

```text
q_N^0(r_MN h_M)=epsilon(1,0).                       (NS3-A20)
```

Therefore `(NS3-A16)` fails exactly:

```text
epsilon(1,0)!=(epsilon/2)(1,1).                    (NS3-A21)
```

The W3 map is not wrong; it is the physical adjoint restriction. What fails
is identifying it with naive history truncation.

The C5 character nevertheless agrees at the restricted stage:

```text
Char_N(epsilon(1,0))
  =exp(i n epsilon),

Char_N((epsilon/2)(1,1))
  =exp(i n epsilon).                                (NS3-A22)
```

At the unit regression value requested by S8-A, this reads exactly

```text
rho_MN^W3(1,0,-1)=(1/2,1/2),
Char_N(1,0)=Char_N(1/2,1/2)=exp(i n).               (NS3-A22a)
```

Thus the exact character square `(NS3-A17)` passes on the permanent
regression. The retained C5 sum covector lies on the old cycle line in this
specific balanced two-edge stage, so orthogonal W3 restriction preserves its
pairing while deleting the nonconserved component.

At stage `M`, `sum q_M=0`, whereas the restricted-stage character is
`exp(i n epsilon)`. This is not a failure of `(NS3-A17)`: finite restriction
forgets edge `d`, so the exact finite C5 character itself changes. V003 does
not assert cross-stage equality of different finite characters.

### 5.4 Global C5 counterexample

The S8-A character agreement is not a general theorem. Let the old stage
contain

```text
a:1->2,
b:2->1,
c:2->3,
```

so its old cycle space is `span{(1,1,0)}`. Let the larger stage add

```text
d:3->2.
```

The larger-stage coefficient

```text
q_M=epsilon(0,0,1,1)                                (NS3-A23)
```

is conserved: the two last edges form a reciprocal cycle. Raw history
restriction gives

```text
q_N^0(r_MN h_M)=epsilon(0,0,1),                     (NS3-A24)
```

whose C5 character is `exp(i n epsilon)`. The W3 adjoint projects the new
cycle orthogonally to the old cycle line and therefore gives

```text
rho_MN^W3(q_M)=0.                                   (NS3-A25)
```

Its C5 character is `1`, unequal to `exp(i n epsilon)` for generic small
`epsilon`. Hence both the strong square and the exact C5 character square
fail over the full admitted stage family.

This counterexample uses the ratified orthonormal A4 coefficient norm and no
selected cycle basis. It is the same mechanism as S8-A, with a stage whose
C5 raw covector is not contained in the old cycle subspace.

### 5.5 Route-2 verdict

```text
W3_PHYSICAL_SOURCE_RESTRICTION = PASS_WITHIN_PROPOSAL
W3_FUNCTORIALITY = PASS_WITHIN_PROPOSAL
W3_STRONG_HISTORY_SOURCE_SQUARE = REFUTED | TYPE-R |
  counterexample: epsilon(1,0,-1)
W3_S8A_RESTRICTED_C5_CHARACTER = PASS_WITHIN_PROPOSAL
W3_GLOBAL_C5_CHARACTER_SQUARE = REFUTED | TYPE-R |
  counterexample: epsilon(0,0,1,1) closing an old dangling edge
```

A history law using `(NS3-A15)` would have to replace the sealed raw history
restriction by a new W3-compatible history map. No such map is ratified or
proposed here. Therefore Route 2 does not furnish a complete
history-to-source law, even though its physical source map and C5 scalar
consumer are individually lawful.

```text
W3_COMPATIBLE_HISTORY_RESTRICTION = NOT_BUILT / TYPE-U |
  would-build: a history-level lift of i_NM^* with endpoint, reality,
               C5, and no-supplementation certificates
```

The projective route remains the completed Branch-A history law in V003 by
proof of Route 2's failed strong square, not by a choice based on tower output.

---

## 6. Branch B — doubled CTP endpoint access

**PROPOSED_NOT_ADOPTED — THREE LEVELS KEPT DISTINCT**

### 6.1 Level I: raw doubled endpoint-covariant access

For each oriented open path/cell and CTP branch `sigma in {+,-}`, retain the
endpoint fibers and export

```text
T_sigma[h]:E_(sigma,s)->E_(sigma,t),

d_acc^B[h]:=(T_+[h],T_-[h]).                        (NS3-B1)
```

Under the endpoint torsor family,

```text
T_sigma[g_sigma.h]
  =g_(sigma,t) T_sigma[h] g_(sigma,s)^(-1).         (NS3-B2)
```

No endpoint frame is selected. The pair, not either component alone, is the
emitted object. Under CTP reality, branch exchange and adjoint send the pair
to the corresponding reversed pair; no scalar reality claim is made before
Level II.

### 6.2 Level II: relative CTP endomorphism

For the common physical endpoint identification used by the ratified doubled
trace, define

```text
R_CTP[h]:=T_-[h]^dagger T_+[h]
  in End(E_s).                                      (NS3-B3)
```

Under a common endpoint change on both CTP branches,

```text
T_+ -> g_t T_+ g_s^(-1),
T_- -> g_t T_- g_s^(-1),

T_-^dagger -> g_s T_-^dagger g_t^(-1),

R_CTP ->g_s T_-^dagger g_t^(-1)g_tT_+g_s^(-1)
       =g_s R_CTP g_s^(-1).                         (NS3-B4)
```

The target-frame factors cancel exactly. `R_CTP` is an endomorphism at the
source endpoint and transforms by conjugation. For U(1) its character is
invariant, but V003 retains the conjugation law rather than using abelianity
to erase the carrier.

Independent endpoint changes on `+` and `-` do not cancel; they encode a
relative source transformation and are not part of the common physical gauge
quotient. This is covariance, not an invariance overclaim.

CTP branch exchange gives

```text
R_CTP[Theta h]=R_CTP[h]^dagger,                     (NS3-B5)
```

with the faithful-character law supplying complex conjugation.

### 6.3 Level III: exact finite C5 trace, and the contraction sweep

At a finite receiver stage, the ratified ready-record trace exists. For each
cell `j`, let `z_(+,j)` and `z_(-,j)` be the faithful characters of the two
raw transports. Then

```text
Z_N^CTP[h]
  :=product_(j=1)^N chi_n(R_(CTP,j)[h])
   =product_(j=1)^N conjugate(z_(-,j)^n)z_(+,j)^n. (NS3-B6)
```

This is exactly the DoR-009 finite doubled trace. Since characters are
conjugation-invariant, `(NS3-B6)` is family-wide over the endpoint torsor;
no frame is selected.

The three levels are:

| Level | Object | Standing |
|---|---|---|
| I | `(T_+,T_-)`, two raw endpoint-covariant morphisms | proposed Branch-B emission |
| II | `R_CTP=T_-^dagger T_+`, relative endpoint endomorphism | derived within proposal from Level I |
| III-a | single-receiver finite ready-record trace `Z_N^CTP` | ratified finite C5 consumer, used proposal-conditionally |
| III-b | joint two-system scalar state/effect contraction | not found, `TYPE-U` |
| III-c | completed physical/continuum contraction | not found, `TYPE-U` |

The bounded sweep is unchanged from the re-review: DoR-009 supplies III-a
inside one finite receiver, but Q-335 and the five-door audit find no joint
network contraction and no completed physical contraction. V003 does not
identify III-a with either missing object.

```text
FINITE_SINGLE_RECORD_C5_CONTRACTION = EXISTS |
  PASS_WITHIN_PROPOSAL
JOINT_TWO_SYSTEM_STATE_EFFECT_CONTRACTION = NOT_BUILT / TYPE-U
COMPLETED_PHYSICAL_STATE_EFFECT_CONTRACTION = NOT_BUILT / TYPE-U
```

### 6.4 Tower, only where Level III licenses it

Let `Z_(i,t)^CTP` be the already traced scalar `(NS3-B6)` for receiver `i`
at tier `t`. The exact charged-projector multiplication gives

```text
F_(i,t)^B=P_(0,i)+Z_(i,t)^CTP P_(ch,i),

product_(t=1)^k F_(i,t)^B
  =P_(0,i)+[product_(t=1)^k Z_(i,t)^CTP]P_(ch,i),

A_(i,k)^B
  =(1-p_i)+p_i product_(t=1)^k Z_(i,t)^CTP.        (NS3-B7)
```

This is not V002's bare product of raw endpoint coordinates. Every factor is
the frame-independent result of the exact doubled C5 trace. The complete
network object is only the ordered pair

```text
Tower_AB,k^B:=((F_(1,k)^B,A_(1,k)^B),
               (F_(2,k)^B,A_(2,k)^B)).             (NS3-B8)
```

V003 does not multiply the two amplitudes. Such a product would consume the
missing joint state/effect contraction.

For a repeated doubled history with `Z_(i,t)^CTP=Z_i^CTP`,

```text
A_(i,k)^B=(1-p_i)+p_i(Z_i^CTP)^k.                  (NS3-B9)
```

All `p_i` remain symbolic rank-ratio forms; no pair or value is selected.

### 6.5 S8-B permanent pair regression

Fix `T_+` and take `T_-!=T_-'`. The raw exports differ:

```text
(T_+,T_-) != (T_+,T_-').                            (NS3-B10)
```

Since the transports are unitary on the compact U(1) fibers,

```text
T_-^dagger T_+ != (T_-')^dagger T_+                (NS3-B11)
```

whenever the backward transports differ. Their faithful characters therefore
change generically, and the exact C5 trace detects the change outside its
ordinary character kernel.

```text
S8B_FIXED_FORWARD_VARY_BACKWARD_CHANGES_EXPORT = PASS_WITHIN_PROPOSAL
S8B_RELATIVE_CTP_OBJECT_PRESERVED = PASS_WITHIN_PROPOSAL
S8B_SINGLE_MORPHISM_COLLAPSE_REPEATED = false | TYPE-S |
  scope: every Branch-B signature
```

### 6.6 Branch-B costs preserved

There is still no global map from raw endpoint transport to V007's scalar
`E_J`, and C5 still contains no network `R` receiver. The repaired finite CTP
trace is an access-side consumer, not a construction of either missing port.

```text
GLOBAL_BRANCH_B_SCALAR_dJ = NOT_BUILT / TYPE-U
BRANCH_B_NETWORK_R_RECEIVER = NOT_BUILT / TYPE-U
LOCAL_C5_J_CHART_CHECK = PASS_WITHIN_PROPOSAL
```

---

## 7. No-ignition standing, reciprocity, and delay

**PROPOSED_NOT_ADOPTED — BOTH BRANCHES**

The exact standing is preserved verbatim:

```text
READY_IDENTITY_FIRST_EMISSION = ZERO_OR_IDENTITY |
  PASS_WITHIN_PROPOSAL

ALL_ZERO_EXTERNALLY_STIPULATED_HISTORY_SEQUENCE = IDENTITY_TOWER |
  CONDITIONAL

AUTONOMOUS_READY_NETWORK_NO_IGNITION = NO_VERDICT / TYPE-U |
  missing: the port-to-write-history update and a zero-fixed-point certificate
```

For Branch A, identity gives the zero cycle source. For Branch B, identity
gives `(T_+,T_-)=(I,I)`, `R_CTP=I`, and `Z_N^CTP=1` at the first delivery.
No induction to the next compact history exists.

Reciprocal node exchange preserves `E_post` and the forward tier order. It
does not reverse time, identify histories, or select a proposal branch.

```text
NS27_BASE_CASE = PASS_WITHIN_PROPOSAL
NS28_AUTONOMOUS_INDUCTION = NOT_AVAILABLE / TYPE-U
RECIPROCITY = PASS_WITHIN_PROPOSAL
E_POST_NETWORK_ORDER = PASS_WITHIN_PROPOSAL
ONE_TIER_DELAY = AUTHORED_NOT_UNIQUELY_FORCED
PORT_TO_WRITE_HISTORY_UPDATE = NOT_BUILT / TYPE-U
```

---

## 8. The five doors — preserved verbatim in content

| Door | V003 result | Type |
|---|---|---|
| Branch-B transport to scalar source | absent | `TYPE-U` |
| Branch-B network R receiver | absent | `TYPE-U` |
| received object to write history | absent | `TYPE-U` |
| joint network state/effect contraction | absent | `TYPE-U` |
| continuum response | absent | `TYPE-U` |

```text
DOOR_B_SCALAR_SOURCE = NOT_OPENED / TYPE-U
DOOR_B_NETWORK_R = NOT_OPENED / TYPE-U
DOOR_PORT_TO_HISTORY_UPDATE = NOT_OPENED / TYPE-U
DOOR_JOINT_SCALAR_NETWORK = NOT_OPENED / TYPE-U
DOOR_CONTINUUM_RESPONSE = NOT_OPENED / TYPE-U
```

The new finite C5 trace is not a quiet opening of the first, second, or fourth
door: it is the already-ratified single-record receiver trace.

---

## 9. Restriction and operation ledger

**PROPOSED_NOT_ADOPTED — ACCOUNTING DOES NOT RATIFY V003**

| Operation | Domain | Image | Kernel | Restriction / covariance | Tail/class | Standing |
|---|---|---|---|---|---|---|
| local doubled chart | common `Log_0` histories | `q_N^0` | equal/common histories | sealed raw history restriction | finite/`ell^1` | retained proposal field |
| projective membership | all finite history restrictions | compatible `C_N` family | histories failing any prefix excluded | closed by `(NS3-A5)` | no created tail | PASS_WITHIN_PROPOSAL |
| projective `d_J` | compatible cycle history | scalar V007 finite core | source quotient kernel | raw-history natural by construction | finite cycle source | PASS_WITHIN_PROPOSAL |
| projective `d_R` | compatible cycle vector | rank-one symmetric bilocal | quadratic sign identification | W3 corners after source formation | trace class | PASS_WITHIN_PROPOSAL |
| W3 adjoint | `C_M` | `C_N` | orthogonal complement of old-cycle image | functorial adjoint | A4 Hilbert norm | PASS as source map |
| W3/history comparison | stage-M conserved history | raw stage-N history coordinate versus `C_N` | S8 difference direction | strong square fails | no tail issue | TYPE-R refutation |
| doubled raw access | `(T_+,T_-)` | endpoint morphism pair | common-history identity | branchwise covariance | full torsor | PASS_WITHIN_PROPOSAL |
| relative endomorphism | raw pair | `End(E_s)` | pairs with same relative product | common-gauge conjugation | finite bounded | PASS_WITHIN_PROPOSAL |
| finite C5 trace | relative endomorphisms | `Z_N^CTP` | faithful-character kernel | conjugation invariant | finite scalar | existing finite consumer |
| tier multiplication | traced per-tier scalars | ordered per-system tower | scalar cancellations | prefix exact | finite only | PASS_WITHIN_PROPOSAL |
| joint contraction | no map | none | unbuilt | no square | new network class | TYPE-U |
| autonomous update | no map | none | unbuilt | no square | new dynamics | TYPE-U |

No continuum completion or response operation is introduced.

---

## 10. Full hostile battery

**PROPOSED_NOT_ADOPTED — BOTH BRANCHES, NO INHERITED CREDIT**

### 10.1 The six V001 attacks

| Attack | Branch A projective law | Branch B doubled law |
|---|---|---|
| additive/replacement offset | **PASS_WITHIN_PROPOSAL**: membership and emission remain zero-anchored | **PASS_WITHIN_PROPOSAL**: identity exports `(I,I)`; fixed nonidentity pairs excluded |
| state-valued freedom | **PASS_WITHIN_PROPOSAL**: rank-one `R` contains only the admitted cycle vector, while its authored status stays explicit | **PASS_WITHIN_PROPOSAL**: no network `R` map or free density is introduced |
| declared-data disguise | **PASS_WITHIN_PROPOSAL**: every input is an actual restricted untraced history | **PASS_WITHIN_PROPOSAL**: both raw transports come from the actual doubled history |
| circularity/target awareness | **PASS_WITHIN_PROPOSAL**: all-prefix conservation precedes the tower computation | **PASS_WITHIN_PROPOSAL**: pair retention is forced by exact CTP typing, not its tower result |
| hidden normalization | **PASS_WITHIN_PROPOSAL with residue**: C5 fixes the admitted scalar coefficient; `R` unit weight remains authored | **PASS_WITHIN_PROPOSAL**: faithful-character normalization belongs to DoR-009; no scalar emitter normalization added |
| history-update attack | **FINDS TYPE-U**: a compatible cycle source does not generate the next history | **FINDS TYPE-U**: the received access pair does not generate the next history |

### 10.2 R7 regressions

Branch A emits the unique zero scalar on the one-edge tree. Branch B may emit
a nonidentity doubled endpoint pair but emits no bare scalar into `E_J` or
`E_R`.

```text
R7_BRANCH_A_ONE_EDGE = PASS_WITHIN_PROPOSAL
R7_BRANCH_B_ONE_EDGE = PASS_WITHIN_PROPOSAL
```

### 10.3 S8-A regression

```text
q_M=epsilon(1,0,-1).
```

The projective route excludes it because its raw restriction is nonconserved.
The W3 route maps it to `(epsilon/2)(1,1)`, preserves the restricted C5
character, and fails the strong history/source square. Every clause is
computed in Sections 4-5.

```text
S8A_PROJECTIVE_ROUTE = EXCLUDED_BY_MEMBERSHIP | PASS_WITHIN_PROPOSAL
S8A_W3_IMAGE = (epsilon/2)(1,1)
S8A_W3_STRONG_SQUARE = REFUTED | TYPE-R
S8A_W3_C5_CHARACTER = PASS_WITHIN_PROPOSAL
```

### 10.4 S8-B regression

Fixed `T_+` and varied `T_-` change the raw pair and the relative CTP
endomorphism. No forward-only export remains.

```text
S8B_PAIR_TEST = PASS_WITHIN_PROPOSAL
```

### 10.5 Fresh Branch-A attack: filtration-refinement attack

**Attack.** Refine a stage that introduced a complete reciprocal loop into
two stages, each introducing one non-loop edge. Does the nonzero projective
cycle survive?

**Result.** No. `(NS3-A8)` forces each singleton coefficient to zero. The
projective family remains well-defined and restriction-natural, but its
nonzero sector depends on which cycles are complete within a declared stage
increment. V003 reports the dependence and makes no filtration-invariant
nonzero claim.

```text
PROJECTIVE_NONZERO_SECTOR_FILTRATION_INVARIANT = false | TYPE-R |
  counterexample: split the reciprocal-pair increment into two singleton increments
PROJECTIVE_RESTRICTION_NATURALITY = PASS_WITHIN_PROPOSAL
FILTRATION_MEMBER_SELECTED = false | TYPE-S | scope: all route statements are fiberwise
```

This is a cost of Route 1, not a reason to select Route 2 after Route 2's
strong-square failure.

### 10.6 Fresh Branch-B attack: common-versus-independent endpoint gauges

**Attack.** Demand conjugation covariance of `R_CTP` under independently
chosen `+/-` endpoint changes.

**Result.** The demand is false: independent changes leave relative mismatch
factors. The sealed physical gauge action is common on the doubled pair;
under that action `(NS3-B4)` proves conjugation. Independent branch changes
are source transformations, not gauge redundancies. V003 states this scope
before taking the character.

```text
R_CTP_COMMON_GAUGE_COVARIANCE = PASS_WITHIN_PROPOSAL
R_CTP_INDEPENDENT_BRANCH_GAUGE_INVARIANCE = false | TYPE-R |
  test: uncancelled g_(-,t)^(-1)g_(+,t) factor
```

### 10.7 Fresh Branch-B attack: joint-contraction smuggling

**Attack.** Multiply the two receiver amplitudes after constructing their
finite towers.

**Result.** Refused. The ratified ready-record trace is local to one finite
record system. No joint network state/effect contraction exists. The output
is the ordered pair `(NS3-B8)` only.

```text
JOINT_NETWORK_AMPLITUDE_CONSTRUCTED = false | TYPE-U |
  missing: joint state, effect, and interaction contraction
```

### 10.8 Standing and selection audit

```text
R3_UNSUPPORTED_INDUCTION_REPEATED = false | TYPE-S | scoped claim audit
R8_TYPE_R_OVERPROMOTION_REPEATED = false | TYPE-S | scoped claim audit
BRANCH_SELECTED = false | TYPE-S | scope: V003
RANK_OR_RATIO_SELECTED = false | TYPE-S | scope: V003
ORIENTATION_OR_FRAME_SELECTED = false | TYPE-S | scope: V003
CYCLE_BASIS_SELECTED = false | TYPE-S | scope: V003
TARGET_OUTPUT_USED_FOR_MEMBERSHIP = false | TYPE-S | scoped formula audit
```

V003 does not self-certify. Lane 1 owns the next adversarial pass.

---

## 11. Updated branch comparison — no recommendation

| Question | Branch A — projective scalar law | Branch B — doubled endpoint access |
|---|---|---|
| Physical object | compatible family of conserved cycle coefficients | raw doubled pair `(T_+,T_-)` |
| Restriction repair | all-prefix conservation by membership | both CTP branches retained through every restriction |
| Exact interstage map | sealed raw history restriction inside `Hist_A^proj` | branchwise endpoint restriction, then relative product |
| W3 role | valid source adjoint; strong history square and global C5 square refuted; S8-A C5 special case passes | downstream source restrictions unchanged; no scalar `d_J` inferred |
| S8-A triple | excluded; W3 comparison image `(1/2,1/2)` | not applicable |
| S8-B pair | not applicable | fixed `T_+`, varied `T_-` changes export and `R_CTP` |
| Tree scalar | exactly zero | no scalar emitted; access may be nonzero |
| Minimal nonzero carrier | reciprocal two-edge cycle if complete within one declared increment; triangle in simple graph category | one open path with both CTP branch transports |
| Exact finite tower | V007 `Xi=x-(hbar/2)x^2` on projective cycle histories | exact C5 `Z^CTP`, then per-system projector tower |
| Tower cost | nonzero sector depends on declared increment/refinement | scalar tower only after ratified single-record trace; no bare endpoint product |
| Network `R` | rank-one cycle bilocal remains authored | absent, `TYPE-U` |
| Joint network scalar | absent, `TYPE-U` | absent, `TYPE-U` |
| Autonomous closure | port-to-history update absent, `TYPE-U` | access-to-history update absent, `TYPE-U` |
| Delay | positive forced; exact one-tier member authored | positive forced; exact one-tier member authored |
| No-ignition | `NO_VERDICT / TYPE-U` | `NO_VERDICT / TYPE-U` |
| Selection here | none | none |

No row recommends or ranks a branch.

---

## 12. Release ceiling and final board

**PROPOSED_NOT_ADOPTED — PENDING LANE-1 RE-REVIEW**

```text
TEN_V002_SURVIVORS_PRESERVED = true | PASS_WITHIN_PROPOSAL

BRANCH_A_PROJECTIVE_HISTORY_LAW = BUILT_WITHIN_PROPOSAL
BRANCH_A_PROJECTIVE_RESTRICTION_CLOSURE = PASS_WITHIN_PROPOSAL
BRANCH_A_PROJECTIVE_NONZERO_S8_FAMILY = {(s,s,0)}
BRANCH_A_MINIMAL_CYCLE_TOWER = UNCHANGED_ON_ADMITTED_STAGE_FIBER

BRANCH_A_W3_SOURCE_MAP = INSTANTIATED
BRANCH_A_W3_STRONG_HISTORY_SQUARE = REFUTED | TYPE-R
BRANCH_A_W3_S8A_C5_CHARACTER = PASS_WITHIN_PROPOSAL
BRANCH_A_W3_GLOBAL_C5_CHARACTER_SQUARE = REFUTED | TYPE-R

BRANCH_B_DOUBLED_PAIR = BUILT_WITHIN_PROPOSAL
BRANCH_B_RELATIVE_CTP_ENDOMORPHISM = BUILT_WITHIN_PROPOSAL
BRANCH_B_FINITE_C5_TRACE = EXECUTED_WITHIN_PROPOSAL
BRANCH_B_ORDERED_FINITE_TOWER = BUILT_WITHIN_PROPOSAL

AUTONOMOUS_READY_NETWORK_NO_IGNITION = NO_VERDICT / TYPE-U
ONE_TIER_DELAY = AUTHORED_NOT_UNIQUELY_FORCED

NETWORK_SOURCING_LAW_V003_RATIFIED = false [PROPOSAL STATUS; Q54_EXEMPT]
V003_SELF_CERTIFIED = false [PROCESS STATUS; Q54_EXEMPT]
REVIEW_CUSTODY = LANE_1

FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S |
  scope: every requested structural calculation was permitted

REGISTER_HEAD_AT_BUILD = Q-339

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 13. Custody

This lane seals the lane-tagged V003 artifact, verifies its sidecar, mirrors
both files byte-identically to
`/Users/bgm/MB Work/alpha-program-archive/workspace/`, reports both hashes,
and stops. It does not edit the register, governing plan, tracker, or git
state and performs no commit or push action.
