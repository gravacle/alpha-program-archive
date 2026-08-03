# Stage 8 Task 4a Network-Sourcing Law Adoption Proposal — Codex Lane 2 V001

**PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION (DoR-016/017 RESERVED)**

Date: 2026-08-03  
Task: PASTE 418 / Task 4a / drive race, authored arm  
Lane: CODEX LANE 2  
Register head at initial draft: Q-334  
Register head at send-time reconciliation: Q-335  
Status: **A FOUR-FIELD MUTUAL-SOURCING PACKAGE IS DRAFTED: THE Q-335-COMPATIBLE ZERO-ANCHORED LOCAL HISTORY CHART, ITS EXACT DIFFERENCE-PORT `d_J`, AN AUTHORED RANK-ONE BILOCAL `d_R`, AND RECIPROCAL ONE-TIER-DELAYED NETWORK TRANSPORT. IT IS TYPE-CORRECT, ZERO-PRESERVING, AND EXACTLY COMPUTABLE. IT TRANSMITS GENUINE DRIVE FROM A NONTRIVIAL LOCAL-CHART HISTORY BUT DOES NOT SPONTANEOUSLY IGNITE TWO HISTORY-FREE READY SYSTEMS. A FULLY AUTONOMOUS FEEDBACK LOOP STILL NEEDS A PORT-TO-WRITE-HISTORY UPDATE, WHICH THIS COMMISSION DID NOT AUTHOR.**

```text
NETWORK_SOURCING_LAW_V001 = PROPOSED_NOT_ADOPTED
PROPOSED_AUTHORED_FIELD_COUNT = 4
PROPOSED_PACKAGE = {H,J,R,N}

H = zero_anchored_relative_character_log_chart_and_l1_history_domain
J = C5_matched_difference_port_emission
R = unit_rank_one_bilocal_autocorrelation_emission
N = reciprocal_matched_carrier_one_tier_delayed_network_rule

TWO_READY_HISTORY_FREE_SYSTEMS_IGNITE = false | TYPE-R |
  test: every proposed emission map vanishes at identity history

NONTRIVIAL_HISTORY_CAN_EMIT_GENUINE_DRIVE = true [PROPOSAL THEOREM]

AUTONOMOUS_PORT_TO_WRITE_HISTORY_UPDATE_INCLUDED = false | TYPE-S |
  scope: the commissioned d_J/d_R emission package

AUTONOMOUS_NETWORK_FEEDBACK_CLOSURE = false | TYPE-U |
  would-build: a certified V007-port-to-compact-write-history update map

TYPE_P_CLAIMS_IN_THIS_PROPOSAL = 0

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 0. Lead result

The least explicit mutual-sourcing package found in the commissioned class is
history-driven and zero-preserving. It uses the ratified write history only
before the completed-record trace:

```text
untraced CTP history of system a
  -> zero-anchored local character coordinate eta_a
  -> neighbor b's J_delta and symmetric R ports
  -> neighbor b's next-tier source germ.
```

It never claims that a completed record exports a history. Q-332 remains
binding: after trace, the record exports only its scalar branch weight. The
new proposal operates on the still-available **history**, not on the completed
record density.

For a directed edge `a->b`, the proposed maps are

```text
q_(a->b)[h_a] :=(i n_b)^(-1) tau_(ba) eta_a[h_a],

d_J^(a->b)[h_a]
  :=T_(CTP,J,b)^(-1)(0,q_(a->b)[h_a]),

v_(a->b)[h_a]
  :=K_(J,b)(d_J^(a->b)[h_a])
   =iota_delta,b q_(a->b)[h_a],

d_R^(a->b)[h_a] :=
  v_(a->b)[h_a] symtensor v_(a->b)[h_a].           (NS-1)
```

The edge acts only at the next tier. The construction contains no additive
source, reference state, selected rank, selected anchor, noise seed, or
target-aware coefficient.

The exact receiving exponent is

```text
x_(b<-a,t):=ell_(b,n_b)(v_(a->b)[h_(a,t)]),

Xi_(b<-a,t)
  =x_(b<-a,t)-(hbar/2)x_(b<-a,t)^2.                (NS-2)
```

Thus a nontrivial history gives genuine drive whenever `x!=0`. At identity
history, `x=0`, both maps vanish, and no bootstrap occurs. The draft does not
add a spontaneous source merely to make the tower deepen.

This is an authored proposal. Equations `(NS-1)` and the network incidence
rule are not claimed to follow from C5. C5 constrains the receiving class; it
does not fix an emitter.

---

## 1. Custody, preflight, and authorities

**PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION (DoR-016/017 RESERVED)**

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = no |
  commissioned proposal only; no ratified d_J or d_R exists

IS_THE_VERSION_CURRENT = yes |
  initial draft checked through Q-334 and governing-plan change C44;
  send-time reconciliation checked Q-335

ARE_ITS_INPUTS_PRESENT = yes |
  compact write histories, faithful characters, V007/P2 port types,
  exact tower machinery, and the Q-332/Q-335 scope boundaries exist
```

Q-334 is load-bearing: it refutes the identification
of `d_state` with either germ source port and names the mutual-sourcing law as
authored/derivation territory. Q-335 arrived after the independent draft was
formed. Its send-time reconciliation is also load-bearing: the `d_J` image
must reproduce C5's finite relative character in V007's zero-anchored local
`J` chart, while C5 supplies no `R` datum. V001 was narrowed to that exact
chart before sealing. No Lane-1 emission choice was imported.

### 1.2 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003/
/Users/bgm/MB Work/alpha_supervision/
/Users/bgm/MB Work/alpha-program-archive/supervision/
/Users/bgm/MB Work/alpha-program-archive/workspace/  [mirror destination]
```

Excluded:

```text
a32_holdout/custodian_private/                        NOT ENTERED
the derivation arm during initial choice formation     NOT CONSULTED
the Q-335 registered constraint at send-time           CONSULTED AS BINDING CURRENCY
anchor, rank, character sign, or network history       NOT SELECTED
continuum response, bridge, root, coupling, or scale   NOT COMPUTED
comparison to a measured constant                      NOT PERFORMED
register, plan, tracker, git, commit, push              NOT TOUCHED
```

### 1.3 Frozen authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | typing, fences, custody |
| `RELAY_PASTE_418_DRAFT_THE_NETWORK_LAW_V001.md` | `dd479c0f06ccd45282fb05d5450992925655881c8fabd8dcaecee20352529ce2` | task contract |
| governing plan through C44 | `5051d2333d5516cfd74402345481a4407de488c332858b0b5f8dea89ad0cbce9` | commission and lane split |
| DoR-009 | `11632fa30dfe9225c228f07a3be4717c73bdfc9e38b0c76c46d905d3fe193bc5` | E_post and exact source-coupled write law |
| transition-law proposal V002 | `db1808e4da38cbfed8b12017885aff1bf63b0378e9971c37294e21fa08766fee` | C1-C8 and compact-history formulas |
| P2 physical source construction V002 | `40b2af34443e051fffdc7bf2ec7025c811a98c501a82d19164596ee6f37f00c1` | `E_J`, `E_R`, Keldysh map, restrictions |
| source germ V007 | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | live port functional and `Q_n^even` |
| exact refinement tower | `034a7aabe316cdab91093c1fc82170e623c6bd112230676e1069aefe77c2fbe0` | finite tower consumer |
| Q-332 feedback typecheck | `99d294e5b2d511e6e6abf3f0cee8bc6892e5ab6eba2a474cc9a9e6abe55d6ad7` | record/history boundary |
| Q-333 full-source tower | `fc63b0d885450d3d23f0cdfca0bbb46d96c3be7c23f5f3a905a1d1bfe19efbcb` | arbitrary-source partial-sum formula |
| Q-334 origin-fed stop | `4e00c7edbec105cd9c60cba483f11c1888a541e5963f3c1168fc6d00085669b0` | exact missing `d_J/d_R` contract |
| Q-335 derivation arm | `e73a3716aa8141bbbb501ae24138050f27f1eca7b66dde05fee25334d6db67e7` | C5 local-`J` receiving constraint and absence of `R` data |

All consumed local sidecars were verified. Archived decision sidecars were
verified from their own directories.

---

## 2. Bearing types and symbol collisions

**PROPOSED_NOT_ADOPTED — NO POSITIVE CLAIM IN THIS SECTION IS TYPE-P**

### 2.1 Ratified receiver types

The receiver ports are

```text
E_J,b := ell^1(N)_+ direct-sum ell^1(N)_-,
E_R,b := S_1,sym(H_CTP,b),
E_src,b:=E_J,b direct-sum E_R,b.                    (NS-3)
```

The bounded Keldysh transform gives common/difference coordinates. Denote
its exact inverse by `T_(CTP,J,b)^(-1)` and the difference-sector inclusion
in the branch-doubled Hilbert carrier by `iota_delta,b`.

### 2.2 History domain

For system `a`, a finite doubled compact history is

```text
h_a=(h_(a,+,j),h_(a,-,j))_(j=1)^N,

z_(a,+,j)^(n_a):=chi_(n_a)(h_(a,+,j)),
z_(a,-,j)^(n_a):=chi_(n_a)(h_(a,-,j)).             (NS-4)
```

This `h` is the background history consumed by the ratified write law. It is
not:

1. the normalized origin density `rho_S`;
2. the completed record state;
3. the P2 source coordinate `J`;
4. the bilocal probe `R`; or
5. the scalar branch weight `p`.

The proposal constructs maps between these already distinct types; it does
not rename one as another.

### 2.3 Required distinctions

```text
n_a              faithful character orientation, not CTP branch;
+/-              CTP branch, not charge sector;
P_ch             charge projector, not p_[A];
p_[A]            source-state quotient, not emitted history;
R                symmetric bilocal source, not a retarded label;
N                 finite cell cutoff, not refinement tier k;
d_R               emission map, not a response derivative;
network edge      causal feeding arrow, not E_post endpoint charge.
```

These collisions bear directly on the proposal. In particular, treating the
completed record's `p` as `J` or `R` would repeat Q-332 and is forbidden.

---

## 3. Choice table — four authored fields

**PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION (DoR-016/017 RESERVED)**

The four rows form one indivisible package. Rows `J` and `R` depend on row
`H`; row `N` says how their outputs are delivered. The dependency is stated
instead of being counted as independent evidence.

| Row | Proposed authored content | Real alternatives considered | What the row adds | Void conditions |
|---|---|---|---|---|
| `H` — emitted history coordinate | On C5/V007's zero-anchored finite chart, use `eta_n(h)_j=Log_0(conj(z_(-,j)^n)z_(+,j)^n)`; admit the completed local-history class for which `eta_n(h)` is in `ell^1`. | The first-difference surrogate `u-1`; a different logarithm branch; an arbitrary bounded function; finite-only histories. | The exact local additive coordinate whose exponent reproduces C5's relative character. The local-chart requirement is inherited from Q-335; identifying the neighbor's history with this edge coordinate remains authored. | Voids if `exp(L(d_J))` fails to reproduce C5 on any finite restriction, the common chart fails, reality fails, or the completed coordinate is not `ell^1`. |
| `J` — linear source emission | Put `q=(i n_b)^(-1)tau eta` in the receiver's Keldysh difference coordinate, set `J_c=0`, and apply the sealed inverse branch transform: `d_J=T_CTP,J^(-1)(0,q)`. | A kernel-valued addition; mixed common/difference representative; a nonunit scalar/operator weight; the zero map. | One explicit `history -> E_J` edge map satisfying Q-335's receive-interface equation exactly. The scalar normalization is fixed by that equation; the pure-difference zero-kernel representative remains authored. | Voids if the map misses `E_J`, violates reality/quotient/restriction, has a hidden offset, or fails the exact relative-character equation. |
| `R` — bilocal source emission | Emit the symmetric rank-one autocorrelation of the same transported difference history: `d_R=v symtensor v`, at unit port normalization. | Zero `R`; diagonal-only intensity; lagged/cross-cell kernel; arbitrary positive or complex symmetric kernel; nonunit weight. | One explicit `history -> E_R` map with no reference density or free covariance kernel. | Voids if it is not trace class/symmetric, violates reality/restriction, contains a state-valued offset, or fails the V007 finite formula. |
| `N` — network incidence | On matched carriers, use the reciprocal two-node swap, no self-edge, identity cell matching, and one-tier delay. | Directed graph; weighted edge; self-sourcing; a nontrivial cell permutation/intertwiner; same-tier/retroactive feeding. | The sender/receiver assignment and causal delivery rule. | Voids if reciprocity or E_post orientation fails, a cell matching is silently selected outside the matched-carrier class, or output feeds the tier that produced it. |

The proposed authored count is exactly four. Q-335 removes one apparent
choice: on the connected zero-anchored chart, the scalar normalization of
row `J` is fixed by exact reproduction of C5's relative character. A
rescaling fails that equation. Row `J` still contains an authored
**representative** choice because C5 does not select among kernel-valued
additions or edge routings. Row `R` has no C5 receiving counterpart at all;
its rank-one form and unit normalization remain fully authored. A lane may
not tune them.

```text
PROPOSED_FIELD_COUNT = 4
PROPOSED_FIELDS_ARE_LOGICALLY_INDEPENDENT = false |
  disclosed dependencies: J<-H, R<-H, delivery<-N

UNIT_J_NORMALIZATION_REMAINS_AUTHORED = false | TYPE-R |
  test: exact C5 local-character reproduction forces unit scalar coefficient
J_ZERO_KERNEL_REPRESENTATIVE_REMAINS_AUTHORED = true [PROPOSAL STATUS]
UNIT_R_NORMALIZATION_DERIVED_FROM_C5 = false | TYPE-R
C5_CONTAINS_NETWORK_R_PORT_DATA = false | TYPE-R |
  test: Q-335 source-level audit of the exact C5 formula
GLOBAL_BRANCH_LOGARITHM_IMPORTED = false | TYPE-S
LOCAL_LOG0_CHART_USED = true [PROPOSAL SCOPE; Q-335 REQUIREMENT]
REFERENCE_STATE_IN_EMISSION_MAP = false | TYPE-S
```

### 3.1 Minimality argument

At least one nonzero port map is necessary to leave Q-334's identity tower.
Row `H` uses the exact zero-anchored local character chart required by Q-335.
The earlier `u-1` candidate is rejected because it reproduces the relative
character only infinitesimally, not exactly. Row `J` uses no additional
history kernel. Row `R` is the lowest-rank nonzero symmetric bilocal made
from the same history vector. Row `N` uses the unique off-diagonal adjacency
on two labeled nodes.

This proves minimality only inside the disclosed matched-carrier,
zero-offset, local-chart class. It does not prove that nature uses
rank-one bilocal emission or unit normalization.

```text
GLOBAL_UNIQUENESS_CLAIMED = false | TYPE-S
MINIMALITY_SCOPE = matched_two_node__zero_offset__local_Log0_chart
```

---

## 4. The proposed emission law

**PROPOSED_NOT_ADOPTED — EVERY CONSTRUCTION BELOW IS PROPOSAL-RELATIVE**

### 4.1 Relative-history local chart

Define the relative character and, only on V007's common zero-anchored
logarithmic chart, its additive coordinate:

```text
u_(a,n)[h_a]_j
  :=conjugate(z_(a,-,j)^(n)) z_(a,+,j)^(n),

eta_(a,n)[h_a]_j:=Log_0(u_(a,n)[h_a]_j).           (NS-5)
```

At every finite `N`, `eta` has finite support while the history remains in
the common chart. The proposed completed emission domain is

```text
Hist_emit,a^(n)
  :={h_a: every u_j is in the common Log_0 chart and
           eta_(a,n)[h_a] is in ell^1(N)}.          (NS-6)
```

The topology is the pullback of the `ell^1` norm through `eta`, modulo
the common-history gauge kernel. This topology is a proposed history-domain
field, not a new topology on the already ratified P2 codomain.

Exact properties:

```text
eta[identity history]=0,
eta[equal CTP histories]=0,
eta_(a,-n)[Theta h]=conjugate(eta_(a,n)[h]),
rho_N eta_M=eta_N rho_N for N<=M.                  (NS-7)
```

The last two follow algebraically within the proposed extractor from the
sealed character reality, the common `Log_0` chart, and coordinate
restrictions. No globalization through a branch cut is claimed.

### 4.2 Edge transport

For a matched-carrier edge `a->b`, let

```text
tau_(ba):ell^1_a -> ell^1_b
```

be the declared identity label match. On a general reciprocal edge family,
the proposal would require isometric intertwiners with

```text
tau_(ab)=Theta_a tau_(ba)^* Theta_b.                (NS-8)
```

V001 instantiates only the matched two-node class, so no permutation or
intertwiner is selected.

Define the receiver-oriented additive difference coordinate and its
branch-doubled vector:

```text
q_(a->b)[h_a]
  :=(i n_b)^(-1) tau_(ba) eta_(a,n_a)[h_a]
  in ell^1_b,

v_(a->b)[h_a]
  :=K_(J,b)(d_J^(a->b)[h_a])
   =iota_(delta,b) q_(a->b)[h_a]
  in H_CTP,b.                                      (NS-9)
```

Because `ell^1` embeds continuously in `ell^2`, `(NS-9)` is square summable.

### 4.3 The two emission maps

The proposal is

```text
d_J^(a->b)[h_a]
  :=T_(CTP,J,b)^(-1)(0,q_(a->b)[h_a])
  in E_J,b,                                        (NS-10)

d_R^(a->b)[h_a]
  :=v_(a->b)[h_a] symtensor v_(a->b)[h_a]
  in E_R,b.                                        (NS-11)
```

The rank-one trace norm obeys

```text
||d_R[h]||_1,trace=||v[h]||_2^2
                 <=||eta[h]||_1^2.                 (NS-12)
```

Thus both maps land in the live V007/P2 ports. No density matrix, reference
covariance, or arbitrary source vector is inserted.

The Q-335 receive-interface check is exact on every finite restriction:

```text
L_(b,n_b)^Theta(d_J^(a->b)[h_a])
  =i n_b sum_j q_(a->b,j)
  =sum_j eta_(a,n_a,j),

exp(L_(b,n_b)^Theta(d_J^(a->b)[h_a]))
  =product_j u_(a,n_a)[h_a]_j.                     (NS-12a)
```

The cell matching and character/reality label transport are part of row `N`.
Equation `(NS-12a)` is the void condition that kills the earlier `u-1`
surrogate and every nonunit scalar rescaling of `d_J` on the connected chart.

### 4.4 One-tier delivery

For every directed edge `a->b`, the history at tier `t` supplies the
neighbor's source at tier `t+1`:

```text
(J_(b,t+1),R_(b,t+1))
  :=(d_J^(a->b)[h_(a,t)],d_R^(a->b)[h_(a,t)]).      (NS-13)
```

For several incoming edges, V001 does not define a sum: that would introduce
a new aggregation law. The instantiated network has two nodes and one
incoming edge per node, so `(NS-13)` is complete.

The delay is forced by the no-post-output-supplementation discipline once an
emission map is proposed. Same-tier retroactive insertion is not a candidate.

---

## 5. Consistency obligations

**PROPOSED_NOT_ADOPTED — CERTIFICATES ARE `PASS_WITHIN_PROPOSAL`, NOT TYPE-P**

### 5.1 Port typing

Equations `(NS-10)`–`(NS-12)` prove

```text
d_J:Hist_emit,a -> E_J,b,
d_R:Hist_emit,a -> E_R,b.
```

Finite histories give finite-support sources. Completed histories in
`Hist_emit` give `ell^1` linear sources and trace-class bilocals.

```text
PORT_TYPECHECK = PASS_WITHIN_PROPOSAL
```

### 5.2 Reciprocity

For the two-node matched network, the adjacency is

```text
Adj_2=[[0,1],[1,0]].                                (NS-14)
```

The same map form applies on both arrows. Reciprocity means law covariance
under node exchange, not equality of the two histories or outputs. Exchanging
nodes in `(NS-13)` exchanges the two source tuples and changes no coefficient.

```text
RECIPROCITY = PASS_WITHIN_PROPOSAL
HISTORY_EQUALITY_ASSUMED = false | TYPE-S
```

### 5.3 E_post and network time arrow

DoR-009 fixes charge after the write. The proposed network order is

```text
tier t:    execute the E_post write and retain its untraced history;
tier t:    evaluate the emitter on that history;
tier t+1:  insert the emitted tuple in the neighbor's source port.
```

No output is added to the write that produced it. Reversing the network arrow
uses the reciprocal map and the conjugate character orientation; it does not
replace E_post by the refuted exchanged root.

```text
E_POST_NETWORK_ORDER = PASS_WITHIN_PROPOSAL
NO_POST_OUTPUT_SUPPLEMENTATION = PASS_WITHIN_PROPOSAL
```

### 5.4 Reality and quotient

From `(NS-7)`–`(NS-11)`:

```text
d_J^(-n)(Theta h)=Theta_J d_J^(n)(h),
d_R^(-n)(Theta h)=Theta_R d_R^(n)(h).               (NS-15)
```

The common-history gauge action cancels in `u`; `eta`, `v`, and both
emissions therefore descend through that kernel. Histories with the same
relative character deliberately have the same emission. This is the
declared quotient, not a hidden loss of record-visible data.

```text
REALITY = PASS_WITHIN_PROPOSAL
COMMON_HISTORY_QUOTIENT = PASS_WITHIN_PROPOSAL
```

### 5.5 Rank and family discipline

No map in `(NS-5)`–`(NS-13)` contains `p_[A]`, an ordered rank pair, an
anchor tag, or transient preparation-channel data. The receiver's symbolic
`p_[A]` enters only when its already ratified state contracts the emitted
source functional.

```text
ANCHOR_MEMBER_SELECTED = false | TYPE-S
RANK_PAIR_SELECTED = false | TYPE-S
CHARACTER_SIGN_SELECTED = false | TYPE-S
```

### 5.6 Identity network

If the network is empty, no edge supplies a source. If an edge exists but the
sender history is identity/equal-history, `(NS-7)` gives

```text
d_J[0_hist]=0,
d_R[0_hist]=0.                                     (NS-16)
```

The receiving tier therefore reproduces the sealed identity slice.

```text
EMPTY_NETWORK_IDENTITY = PASS_WITHIN_PROPOSAL
IDENTITY_HISTORY_IDENTITY = PASS_WITHIN_PROPOSAL
```

### 5.7 Declared tower override

The declared-source experiment is recovered by replacing `(NS-13)` with an
independently declared tuple:

```text
(J_(b,t),R_(b,t)):=(J_(b,t)^decl,R_(b,t)^decl).
```

This is an override, not an addition. It returns the exact Q-330/Q-333 tower.
The proposal does not call declared data a network emission.

```text
DECLARED_TOWER_OVERRIDE = PASS_WITHIN_PROPOSAL
DECLARED_SOURCE_ADDED_TO_NETWORK_EMISSION = false | TYPE-S
```

---

## 6. Exact two-system network tower

**PROPOSED_NOT_ADOPTED — SYMBOLIC COMPUTATION WITHIN THE DRAFT ONLY**

### 6.1 Tier-local exponents

Let systems `1` and `2` have symbolic origin weights

```text
p_1=r_(ch,1)/(r_(0,1)+r_(ch,1)),
p_2=r_(ch,2)/(r_(0,2)+r_(ch,2)),                   (NS-17)
```

with no rank selected and no ratio evaluated.

For tier `t>=1`, define

```text
v_(2->1,t):=v_(2->1)[h_(2,t-1)],
v_(1->2,t):=v_(1->2)[h_(1,t-1)],

x_(1<-2,t):=ell_(1,n_1)(v_(2->1,t)),
x_(2<-1,t):=ell_(2,n_2)(v_(1->2,t)).               (NS-18)
```

By V007's exact rank-one bilocal formula, consumed inside the proposal,

```text
L_(1,n_1)^Theta(d_J^(2->1)[h_2])=x_(1<-2,t),
Q_(1,n_1)^even(d_R^(2->1)[h_2])
  =hbar x_(1<-2,t)^2,

L_(2,n_2)^Theta(d_J^(1->2)[h_1])=x_(2<-1,t),
Q_(2,n_2)^even(d_R^(1->2)[h_1])
  =hbar x_(2<-1,t)^2.                              (NS-19)
```

Therefore the exact network-fed tier exponents are

```text
Xi_(1<-2,t)=x_(1<-2,t)-(hbar/2)x_(1<-2,t)^2,
Xi_(2<-1,t)=x_(2<-1,t)-(hbar/2)x_(2<-1,t)^2.       (NS-20)
```

No sign, magnitude, or growth behavior was used to choose `(NS-1)`.

### 6.2 Finite depth `k`

Define

```text
S_(1,k):=sum_(t=1)^k Xi_(1<-2,t),
S_(2,k):=sum_(t=1)^k Xi_(2<-1,t),                  (NS-21)

D_(1,k):=(hbar/2)sum_(t=1)^k x_(1<-2,t)^2,
D_(2,k):=(hbar/2)sum_(t=1)^k x_(2<-1,t)^2.         (NS-22)
```

The ordered pair of exact system amplitudes is

```text
A_(1,k)=(1-p_1)+p_1 exp(S_(1,k)),
A_(2,k)=(1-p_2)+p_2 exp(S_(2,k)).                  (NS-23)
```

Their physical branch weights remain

```text
(1-p_1,p_1),
(1-p_2,p_2)                                        (NS-24)
```

at every tier. The proposed emission changes the allow-side exponent, not
the origin state.

The pair `(NS-23)` is the complete two-system tower that follows without
adding a joint scalar contraction. Multiplying the two amplitudes would
assume an independent product contraction after histories have been coupled;
V001 does not do that.

```text
ORDERED_TWO_SYSTEM_TOWER_CONSTRUCTED = true [PROPOSAL THEOREM]
JOINT_SCALAR_NETWORK_AMPLITUDE_CONSTRUCTED = false | TYPE-U |
  would-build: a certified joint state/effect contraction for the coupled histories
```

### 6.3 Repeated stationary histories

If each sender presents the same admitted history at every tier, write

```text
x_(1<-2,t)=x_(1<-2),
x_(2<-1,t)=x_(2<-1).
```

Then

```text
S_(1,k)=k[x_(1<-2)-(hbar/2)x_(1<-2)^2],
D_(1,k)=k(hbar/2)x_(1<-2)^2,

S_(2,k)=k[x_(2<-1)-(hbar/2)x_(2<-1)^2],
D_(2,k)=k(hbar/2)x_(2<-1)^2,                       (NS-25)

A_(1,k)=(1-p_1)+p_1
  exp(k[x_(1<-2)-(hbar/2)x_(1<-2)^2]),

A_(2,k)=(1-p_2)+p_2
  exp(k[x_(2<-1)-(hbar/2)x_(2<-1)^2]).             (NS-26)
```

Thus repeated nonzero network histories produce exact linear accumulation in
the exponent. This is a computed consequence of the proposed rank-one map,
not its selection criterion. General evolving histories retain the exact
partial sums `(NS-21)`–`(NS-22)` and need not grow linearly.

### 6.4 Genuine-drive certificate

Because the live covector `ell_(b,n_b)` is nonzero, its finite core contains
an instantiated direction outside its kernel. For a matched edge whose
local relative-character coordinate reaches such a direction,

```text
x_(b<-a,t)!=0.
```

Then at least one of the linear or bilocal emitted port evaluations is
nonzero. If every local relative-history coordinate of an admitted edge landed
in `ker ell_b`, row `J/R` would void by its stated nondegeneracy condition.

```text
NONZERO_HISTORY_DRIVE_CLASS_NONEMPTY = true [PROPOSAL EXISTENCE THEOREM]
ALL_NONZERO_HISTORIES_GIVE_NONZERO_DRIVE = false | TYPE-R |
  counterclass: histories whose transported local coordinate lies in ker ell_b
```

---

## 7. Bootstrap computation

**PROPOSED_NOT_ADOPTED — THE NEGATIVE BOOTSTRAP RESULT IS EXACT WITHIN THE PROPOSAL**

### 7.1 Two ready systems

Take both systems ready, with no declared history and the zero/equal CTP
history at the first emission surface. Then

```text
eta_1=eta_2=0,
v_(1->2)=v_(2->1)=0,
d_J=d_R=0,
x_(1<-2)=x_(2<-1)=0.                               (NS-27)
```

At the next tier, both amplitudes are the identity value. Since the proposal
contains no offset or autonomous history generator, the same argument repeats
at every finite tier:

```text
A_(1,k)=A_(2,k)=1,
D_(1,k)=D_(2,k)=0                                  (NS-28)
```

for all finite `k`.

```text
TWO_READY_SYSTEM_BOOTSTRAP = NO_IGNITION | TYPE-R |
  scope: V001 zero-offset emission package with no declared histories
```

This is not repaired. Adding a constant `J_0`, `R_0`, a random seed, a
reference density, or a spontaneous-history rule would be another adoption.
Choosing one because `(NS-28)` is trivial would be target tuning.

### 7.2 Seeded network

If either system has a nontrivial write history, its neighbor receives the
corresponding nonzero port tuple at the next tier whenever the nondegeneracy
condition holds. The law therefore transmits and reciprocates existing
history; it does not create history from exact identity.

The proposal does not map a received V007 source tuple back into a compact
write history. Consequently a one-sided seed does not by itself prove an
endless autonomous ping-pong. The exact tower `(NS-21)` consumes the actual
write-history sequence supplied by the two systems' executions.

```text
SEEDED_ONE_STEP_TRANSMISSION = PASS_WITHIN_PROPOSAL
PORT_TO_WRITE_HISTORY_UPDATE_EXISTS = false | TYPE-S |
  bounded proposal fields: H,J,R,N
ENDLESS_AUTONOMOUS_PING_PONG_DERIVED = false | TYPE-U |
  would-build: port-to-write-history update and its fixed-point/reciprocity certificates
```

This is the proposal's sharp scope boundary, not a hidden fifth field.

---

## 8. Fresh battery

**PROPOSED_NOT_ADOPTED — NO INHERITED CREDIT AND NO TYPE-P UPGRADE**

| Row | Failure-capable victim | V001 result |
|---|---|---|
| B1 exact port typing | A history map outside `ell^1` or trace class | **PASS_WITHIN_PROPOSAL** by `(NS-10)`–`(NS-12)` |
| B2 tier-one restriction | A map that changes the sealed zero/declared one-cell interfaces | **PASS_WITHIN_PROPOSAL**; identity is exact and declared override is exact |
| B3 declared tower recovery | Emission silently added to declared data | **PASS_WITHIN_PROPOSAL** by replacement, not addition |
| B4 Q-332 boundary | A map reading completed-record density as history | **PASS_WITHIN_PROPOSAL**; domain is untraced compact history |
| B5 C5 receiver compatibility | A `d_J` whose exponent does not reproduce the exact finite relative character | **PASS_WITHIN_PROPOSAL** by `(NS-12a)` on the Q-335 local chart; no global equality claimed |
| B6 reciprocity | Different law or coefficient on reversed edge | **PASS_WITHIN_PROPOSAL** on the matched two-node swap |
| B7 E_post time arrow | Same-tier or retroactive feeding | **PASS_WITHIN_PROPOSAL** by the one-tier delay |
| B8 reality | An emitter not covariant under character/source involution | **PASS_WITHIN_PROPOSAL** by `(NS-15)` |
| B9 quotient | Dependence on common gauge or absolute frame | **PASS_WITHIN_PROPOSAL** through the relative character and local chart |
| B10 rank/no-selection | A coefficient chosen from one rank or anchor member | **PASS_WITHIN_PROPOSAL**; no emitter contains `p` or rank data |
| B11 identity | Additive or replacement-source offset | **PASS_WITHIN_PROPOSAL**; both maps vanish at identity history |
| B12 genuine drive | Entire emitted family lands in receiver kernel | **PASS_WITHIN_PROPOSAL** on the instantiated nonkernel history class; row voids otherwise |
| B13 no supplementation | Output inserted after its consumer output is inspected | **PASS_WITHIN_PROPOSAL**; next-tier only |
| B14 target independence | Map or coefficient chosen for depth, response, or target behavior | **PASS_WITHIN_PROPOSAL**; choice order precedes `(NS-20)`–`(NS-28)` |

```text
NETWORK_LAW_V001_BATTERY = 14_PASS_WITHIN_PROPOSAL / 0_FAIL
NETWORK_LAW_V001_RATIFIED = false | TYPE-C |
  constraint: DoR-016/017 reserved; adversarial review has not run
```

The battery does not certify an autonomous history generator or joint scalar
network contraction. Those are outside the four-field proposal and remain
typed gaps. It also does not upgrade the `R` row to a C5 consequence: B1
certifies its V007 port type, while its network meaning remains authored.

---

## 9. Mandatory self-kill

**PROPOSED_NOT_ADOPTED — HOSTILE TESTS RUN AGAINST THIS EXACT V001**

### 9.1 Constant-source/replacement attack

Consider

```text
d_J'(h)=d_J(h)+J_0,
d_R'(h)=d_R(h)+R_0.
```

These maps are type-correct for arbitrary fixed `J_0,R_0`, but they emit at
identity history and can encode any desired drive. They fail B11 and B14
unless `J_0,R_0` have independent generative provenance. V001 excludes them.

```text
ADDITIVE_SOURCE_OFFSET_SURVIVES = false | TYPE-R
REPLACEMENT_EMITTER_SURVIVES = false | TYPE-R
```

### 9.2 State-valued freedom attack

A bilocal rule

```text
d_R^sigma(h)=v(h) symtensor v(h)+Tr(history datum)sigma
```

could hide an arbitrary state/covariance `sigma`. V001's `d_R` contains only
the transported history vector twice. No density, positive functional,
reference covariance, cyclic vector, or measure occurs. The B14 disease does
not move into `d_R`.

```text
FREE_STATE_OR_COVARIANCE_SLOT_FOUND = false | TYPE-S |
  scope: formulas NS-5 through NS-13
```

### 9.3 Declared-data disguise attack

The only input to the emitter is the sender's actual compact history. No
independent probe appears in `eta`, `v`, `d_J`, or `d_R`. The declared
tower is recovered only under an explicitly different override experiment.

```text
DECLARED_PROBE_DISGUISED_AS_EMISSION = false | TYPE-S
```

### 9.4 Circularity and target-awareness attack

The choice table is frozen before the exponent and tower are computed. It
does not mention linear growth, logarithmic growth, cancellation, survival,
a response, or any target. The repeated-history linear form `(NS-25)` is a
result. The no-ignition result `(NS-28)` is retained even though adding an
offset would produce a more dramatic tower.

```text
DEPTH_FORM_USED_TO_SELECT_EMITTER = false | TYPE-S
P_CONSEQUENCE_USED_TO_SELECT_EMITTER = false | TYPE-S
MEASURED_OR_TARGET_VALUE_USED = false | TYPE-S
```

### 9.5 Hidden normalization attack

Q-335 separates the two ports. On the connected zero-anchored chart,

```text
d_J^(lambda)=lambda_J d_J
```

would give `exp(lambda_J L(d_J))` instead of the exact C5 relative
character. Equality on a neighborhood forces `lambda_J=1`. Thus the scalar
`J` normalization is not an authored freedom after the send-time
reconciliation. Kernel-valued additions remain possible and are removed only
by V001's disclosed pure-difference, zero-kernel representative choice.

C5 contains no `R` datum. Therefore

```text
d_R^(mu)=mu_R d_R
```

remains mathematically admissible subject to reality, restriction, and port
typing. The choice `mu_R=1`, the rank-one form, and the claim that this
bilocal represents network autocorrelation are genuine authored physics.

```text
J_SCALAR_NORMALIZATION_FAMILY_SURVIVES_Q335 = false | TYPE-R |
  test: exact local relative-character equation
J_KERNEL_REPRESENTATIVE_FAMILY_SURVIVES = true [PROPOSAL DISCLOSURE]
R_NORMALIZATION_UNIQUE = false | TYPE-R |
  counterfamily: symbolic mu_R rescaling
UNIT_R_NORMALIZATION_HIDDEN = false | TYPE-S
```

The `R` row is the proposal's weakest authored seam. If the principal
declines to select its form or unit, the correct repair is a family-level
`R` proposal, not a claim that C5 fixed it.

### 9.6 History-update attack

The most consequential hostile finding is that `d_J/d_R` are emission maps,
not a complete autonomous network evolution. They do not turn the received
ports back into the compact connection history used by the next emission.

```text
V001_IS_A_COMPLETE_EMISSION_LAW = true [PROPOSAL STATUS]
V001_IS_A_COMPLETE_AUTONOMOUS_NETWORK_DYNAMICS = false | TYPE-U
```

This does not make the commissioned maps schematic: every member of the
matched two-node class is instantiated. It limits what the tower proves.

---

## 10. Restriction, six-account, and door ledger

**PROPOSED_NOT_ADOPTED — ACCOUNTING DOES NOT RATIFY THE PACKAGE**

| Operation | Domain | Image | Kernel | Restriction square | Tail/class action | Standing |
|---|---|---|---|---|---|---|
| local relative-character logarithm | `Hist_emit` | `ell^1` | equal/common histories | coordinate-natural inside common chart | history pullback topology; no globalization | proposed `H` narrowed by Q-335 |
| edge transport | matched sender `ell^1` | receiver difference direction | none on matched labels | identity square | no new tail | proposed `N` |
| `d_J` | transported difference direction | `E_J` | receiver/source quotient kernel | P2/Keldysh natural | `ell^1`, `Tail_src={0}` | proposed `J` |
| `d_R` | same direction | rank-one `E_R` | zero history plus sign identification of quadratic map | trace-class corner | finite-rank, no source tail | proposed `R` |
| next-tier delivery | tier-`t` history | tier-`t+1` source tuple | empty edge | prefix exact | finite tier only | proposal consequence |
| V007 evaluation | emitted tuple | scalar `Xi` | `ker ell` classes | Q-333 square | existing source class | inherited consumer |
| finite network sum | emitted source cylinder | `S_k,D_k` | cancellation classes | prefix exact | finite only | proposal theorem |
| autonomous history update | no declared map | none | unbuilt | absent | new dynamical class | `TYPE-U` |
| joint scalar contraction | no certified coupled state/effect | none | unbuilt | absent | joint class | `TYPE-U` |

Door flags:

```text
DOOR_HISTORY_EMISSION_CLASS = PROPOSED_OPENING
DOOR_J_EMISSION = PROPOSED_OPENING
DOOR_R_EMISSION = PROPOSED_OPENING
DOOR_RECIPROCAL_NETWORK = PROPOSED_OPENING
DOOR_NEXT_TIER = FILLED_WITH_ONE_TIER_DELAY
DOOR_PORT_TO_HISTORY_UPDATE = NOT_OPENED | TYPE-U
DOOR_JOINT_SCALAR_NETWORK = NOT_OPENED | TYPE-U
DOOR_CONTINUUM_RESPONSE = NOT_OPENED
DOOR_BRIDGE = NOT_OPENED
```

No continuum measure, contour, weak-star completion, bidual, response
operator, bridge, root, physical coupling, or scale is introduced.

---

## 11. Release ceiling and final board

**PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION (DoR-016/017 RESERVED)**

If ratified as one package, V001 would add:

```text
1. one relative-history emission coordinate and its l1 domain;
2. one explicit history-to-J_delta map;
3. one explicit history-to-symmetric-R map;
4. one reciprocal matched-carrier next-tier delivery law.
```

It would make the following exact finite statements available:

```text
NETWORK_TIER_EXPONENT
  = x-(hbar/2)x^2,

NETWORK_DEPTH_ACCUMULATION
  = partial sums of the emitted-history x values and their squares,

REPEATED_HISTORY_DEPTH
  = exact linear k dependence,

TWO_READY_ZERO_HISTORY_BOOTSTRAP
  = no ignition; A_1,k=A_2,k=1 and D_1,k=D_2,k=0.
```

It would not:

```text
derive the emitter from C5;
select a rank, anchor, character orientation, or network history;
generate a compact write history from received J/R ports;
construct a joint scalar network state/effect contraction;
construct a continuum response or divergence bridge;
evaluate any physical parameter.
```

Final typed board:

```text
NETWORK_SOURCING_LAW_V001_WRITTEN = true [PROPOSAL STATUS]
NETWORK_SOURCING_LAW_V001_RATIFIED = false | TYPE-C |
  constraint: DoR-016/017 reserved and cross-lane adversarial review pending

PROPOSED_AUTHORED_FIELD_COUNT = 4
PROPOSED_UNIT_NORMALIZATION_COUNT = 1 [R only]
J_SCALAR_NORMALIZATION_FIXED_BY_RECEIVE_INTERFACE = true [PROPOSAL CERTIFICATE]
C5_NETWORK_R_MEANING_EXISTS = false | TYPE-R

TWO_SYSTEM_EMISSION_MAPS_INSTANTIATED = true [PROPOSAL STATUS]
TWO_SYSTEM_FINITE_TOWER_COMPUTED = true [PROPOSAL THEOREM]
TWO_READY_BOOTSTRAP_REFUTED = true | TYPE-R

GENUINE_DRIVE_FROM_NONZERO_HISTORY = true [PROPOSAL EXISTENCE THEOREM]
GENUINE_DRIVE_FROM_COMPLETED_RECORD_ALONE = false | TYPE-R |
  root: Q-332 record-export theorem

AUTONOMOUS_NETWORK_CLOSURE = false | TYPE-U |
  missing: V007-port-to-compact-write-history update

TARGET_OUTPUT_USED_TO_DRAFT_LAW = false | TYPE-S
FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S
TYPE_P_CLAIMS_IN_THIS_PROPOSAL = 0

REGISTER_HEAD_AT_INITIAL_DRAFT = Q-334
REGISTER_SHA256_AT_INITIAL_DRAFT =
  7f47df26f1ac9c2d9e9a797d530c2cba03d84dc4f62b01ca55a2924fe4d6aa9a

REGISTER_HEAD_AT_SEND_TIME = Q-335
REGISTER_SHA256_AT_SEND_TIME =
  252b65179a3f77595efc0b7b10c9ee667d8e6c18be147239f79e204cb5cf68d6

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 12. Custody

This lane seals this lane-tagged artifact, verifies its sidecar, mirrors the
artifact and sidecar byte-identically, reports hashes, and stops. It does not
edit the register, governing plan, or tracker and performs no git, commit, or
push action.
