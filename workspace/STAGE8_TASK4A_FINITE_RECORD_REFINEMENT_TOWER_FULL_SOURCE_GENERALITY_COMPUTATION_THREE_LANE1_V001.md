# Stage 8 Task 4a Finite Record-Refinement Tower at Full Source Generality - Computation Three - Lane 1 V001

Date: 2026-08-03  
Task: PASTE 415 / Task 4a / finite depth program computation three  
Lane: CODEX LANE 1  
Register head at freeze: Q-331  
Status: **THE FINITE TOWER EXTENDS EXACTLY TO ARBITRARY P2 COMPLETED SOURCE SEQUENCES. THE GENERALIZED BILOCAL ACCUMULATION IS THE PARTIAL-SUM FUNCTIONAL `D_k=(1/2)SUM_T Q_n^even(R_T)`. FULL SOURCE GENERALITY FORCES NO UNIVERSAL GROWTH CLASS: BOUNDED, SUBLINEAR, LINEAR, SUPER-LINEAR, OSCILLATORY, AND ARBITRARY PRESCRIBED PARTIAL-SUM BEHAVIOR ALL OCCUR. THE UNNORMALIZED FIXED-K SUPREMUM IS INFINITE. P2'S FINITE-CORNER FILTRATION SUPPLIES ONE EXPLICIT BOUNDED TELESCOPING SUBFAMILY, BUT NO SEALED MAP IDENTIFIES ITS CELL CUTOFF `N` WITH REFINEMENT DEPTH `k`; IT IS NOT SELECTED AS THE PHYSICAL FEED. THE PHYSICAL RECORD-STATE WEIGHTS REMAIN EXACTLY `(1-p,p)` FOR EVERY SOURCE SEQUENCE AND EVERY FINITE TIER.**

```text
FULL_P2_SOURCE_FINITE_TOWER_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014 and the verified tower |
  scope: every finite k and every stagewise sequence in the P2 source class

GENERALIZED_BILOCAL_ACCUMULATION
  = D_k[R_1,...,R_k]=(1/2)sum_(t=1)^k Q_n^even(R_t) | TYPE-P

UNIVERSAL_FULL_SOURCE_GROWTH_CLASS_EXISTS = false | TYPE-R |
  counterfamilies: alternating, harmonic, constant, linearly intensified,
                   and arbitrary prescribed partial sums

FULL_UNNORMALIZED_FIXED_K_SUPREMUM_IS_FINITE = false | TYPE-R |
  counterfamily: scale one nonzero completed bilocal source

PHYSICAL_BRANCH_WEIGHTS_MOVE_WITH_COMPLETED_SOURCE = false | TYPE-R |
  test: the source enters the charged generating factor, not rho_S or p_[A]

ONE_COMPLETED_SOURCE_SHELL_ACCUMULATION_IS_BOUNDED = true | TYPE-P |
  premise: the explicitly declared P2 finite-corner shell feed

P2_CELL_STAGE_TO_REFINEMENT_TIER_MAP_IS_FORCED = false | TYPE-R |
  counterfamily: shell, repeated-source, and cumulative-corner feeds all
                 satisfy the full source-sequence interface

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 0. Lead determination

The full-generality tower exists at every finite tier without selecting a
source-sequence topology. Let the character label `n` and rank class `[A]`
be fixed, with

```text
p:=p_[A]=r_ch/(r_0+r_ch)
```

left symbolic. For each tier `t`, choose an arbitrary P2 completed source

```text
s_t=(J_(+,t),J_(-,t),R_t) in E_src,
E_src=(ell^1_+ direct-sum ell^1_-)
      direct-sum S_1,sym(H_CTP).
```

Define the live V007 exponent

```text
Xi_t:=Xi_n^007(s_t)
     =L_n^Theta(J_t)-(1/2)Q_n^even(R_t).             (FG-1)
```

Then the exact finite tower is

```text
rho_tower,k
 =P_0 rho_S P_0 tensor_(t=1)^k E_R,t
  +P_ch rho_S P_ch tensor_(t=1)^k E_P,t,            (FG-2)

omega_tower,k
 =(1-p) tensor_t E_R,t+p tensor_t E_P,t,            (FG-3)

F_tower,k[s_1,...,s_k]
 =P_0+exp(sum_(t=1)^k Xi_t)P_ch,                    (FG-4)

A_tower,k[s_1,...,s_k]
 =(1-p)+p exp(sum_(t=1)^k Xi_t).                    (FG-5)
```

Separate the two continuous source coordinates:

```text
L_k[J_1,...,J_k]:=sum_t L_n^Theta(J_t),
D_k[R_1,...,R_k]:=(1/2)sum_t Q_n^even(R_t),
Xi_k=L_k-D_k.                                       (FG-6)
```

At full complex source generality, `D_k` is a complex bilocal source
coordinate. Its real part is the attenuation coordinate and its imaginary
part shifts phase. On the admitted real-probe subfamily it reduces to the
real dephasing exponent used by Q-330.

The exact answer is therefore a partial-sum theorem, not a universal linear
law. `kQ/2` is the constant-sequence special case. The full P2 class is an
unbounded Banach space and P2 ratifies no norm or measure on the sequence
index `t`; consequently no finite global supremum or unique growth law can be
inferred without adding a source budget.

P2's finite-stage label `N` and the tower's refinement-depth label `k` are
different objects. This computation never identifies them. A P2 finite-corner
sequence can be inserted as one lawful tower source sequence, but it is not
the unique or selected physical feed.

The physical state `(FG-3)` is independent of all `s_t`. Nonzero sources can
change the generating amplitude `(FG-5)`, but they do not change the record
state's branch weights.

---

## 1. Custody, preflight, and authorities

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = PARTIAL |
  tier-local tower: sealed and doubly verified at Q-330/Q-331 |
  full completed-source tower: constructed here

IS_THE_VERSION_CURRENT = true |
  register head: Q-331 |
  register SHA-256 at start:
    87f0e61c94b2a4716c441658720985d1ff78ec91499b5dcb36d6368e19f3b652

ARE_ITS_INPUTS_PRESENT = true |
  P2 completed source class, finite restrictions, source functional,
  verified tower algebra, state, and rank family are present
```

The filename is lane-tagged because Q-331 records the relay-413 file
collision. No untagged tower-verification artifact is edited here.

### 1.2 Roots and exclusions

Roots entered:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003/
/Users/bgm/MB Work/alpha_supervision/
/Users/bgm/MB Work/alpha-program-archive/workspace/
```

Excluded:

```text
a32_holdout/custodian_private/                       NOT ENTERED
relay 414 intrinsic-tower outcome                    NOT CONSULTED OR USED
continuum response, bridge, inverse, or stationary   NOT CONSTRUCTED
rank-pair member                                     NOT SELECTED
physical residual, root, coupling, or scale          NOT EVALUATED
comparison to a measured constant                    NOT PERFORMED
register, governing plan, tracker, git, commit, push NOT TOUCHED
```

### 1.3 Frozen authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | fences, typing, custody |
| `RELAY_PASTE_415_THE_TOWER_AT_FULL_SOURCE_GENERALITY_V001.md` | `225bed80210fa39579bc3beb6791f5ff8c6fd14514da89e2489fb7773377692b` | task contract |
| tower exact computation V001 | `034a7aabe316cdab91093c1fc82170e623c6bd112230676e1069aefe77c2fbe0` | finite tower algebra |
| surviving cross-verification V001 | `16ddb6823b045adf49f80996b098c3d5aeaa24c134dea74c74ec1a95a5747d9b` | Q-331 scope boundary |
| P2 physical source topology V002 | `40b2af34443e051fffdc7bf2ec7025c811a98c501a82d19164596ee6f37f00c1` | completed source class and finite corners |
| source germ V006 | `343117b7f75eba02725c6955086e5988116c51c1717d809b4822c0ba3110e4dd` | full `Q_n^even` and its certificates |
| source germ V007 | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | live exponent; V006 source functional unchanged |
| finite nonzero-R reference V001 | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | finite source restriction controls |
| Door-D transport audit V001 | `0fcf42e8ca682c8e655f8d41a3e9b4713b3f45d1adc5be9e1743d2e05720b632` | `K_R`, W3, pairing transport |

All consumed local sidecars verified before use. The current source
functional is V007/V006's rank-one even pairing, not the void historical C-B
same-cell trace.

---

## 2. The admitted full-source sequence family

### 2.1 What P2 seals

P2 seals the Banach source class

```text
E_src=E_J direct-sum E_R,
E_J=ell^1_+ direct-sum ell^1_-,
E_R=S_1,sym(H_CTP),
||s||_src=||J_+||_1+||J_-||_1+||R||_1,trace,
```

and the contractive finite restrictions and isometric zero extensions

```text
rho_src,N(J_+,J_-,R)=(P_NJ_+,P_NJ_-,P_NRP_N),
iota_src,N:E_src,N -> E_src,
||iota_src,N rho_src,N(s)-s||_src ->0.              (FG-7)
```

It does not seal an `ell^p`, supremum, probability, or other norm on a
sequence of separate completed sources indexed by refinement tier.

### 2.2 Maximal finite cylinder family

For each finite `k`, define

```text
Seq_P2,k:=E_src^k.
```

The compatible family `{Seq_P2,k}` under prefix restriction is the maximal
stagewise source family needed for finite computation. No infinite product
topology is required: every formula at tier `k` consumes only the first `k`
sources. Proofs about this family count as instantiation under C19/Q-200.

```text
FULL_SEQUENCE_TOPOLOGY_RATIFIED = false | TYPE-S |
  roots: P2 V002 and V007 |
  query: tier sequence norm, product measure, ell-p over tiers, source budget

FINITE_CYLINDER_SOURCE_FAMILY_INSTANTIATED = true | TYPE-P |
  object: {E_src^k,prefix_(k+1,k)}_(k>=1)

ARBITRARY_INFINITE_SEQUENCE_LIMIT_TAKEN = false | TYPE-S
```

### 2.3 Why the full bilocal source is lawful

The live bilocal functional is

```text
ell_n:=L_n^Theta compose K_J^(-1),
b_n^even:=hbar ell_n tensor ell_n,
Q_n^even(R):=<b_n^even,K_R(R)>_(Bil,S_1).           (FG-8)
```

V006 proves `Q_n^even` continuous on the complete symmetric trace-class
source, quotient-compatible, W3-restriction-natural, and Theta-even. V007
leaves `(FG-8)` unchanged. Thus every `R_t in E_R`, including sources with
arbitrary cross-cell bilocal blocks on its P2 carrier, has one exact scalar
`Q_n^even(R_t)`. No cell-local decomposition of `R_t` is needed to define
`(FG-6)`.

### 2.4 The inter-tier carrier is not P2

P2's `H_CTP` carries cell and CTP-branch labels. The refinement tier `t` is a
new external index of the tower source sequence. No sealed P2 object is a
single trace-class bilocal on

```text
H_CTP tensor ell^2(refinement tiers).
```

Consequently `(FG-6)` is full P2 generality **at each tier**, with arbitrary
completed `R_t`, but it does not smuggle in a new bilocal kernel coupling
different refinement tiers. Such a kernel would not factor into scalar
`Xi_t` terms and would require a new carrier, topology, pairing, restriction,
and falsifier certificate.

```text
SINGLE_COMPLETED_INTER_TIER_BILOCAL_CARRIER_EXISTS_IN_P2 = false | TYPE-S |
  roots: P2 V002, V006, V007 |
  query: refinement-tier tensor factor, cross-tier source block, tier-pair R

FULL_P2_GENERALITY_AT_EACH_TIER = true | TYPE-P
FULL_NEW_INTER_TIER_BILOCAL_GENERALITY = false | TYPE-U |
  would-build: S_1,sym(H_CTP tensor ell^2(tier)) and its complete certificates
```

---

## 3. Exact tower at full source generality

### 3.1 Operator induction

For a fresh record factor at tier `t`, the source-controlled write has the
two-sector form

```text
U_t=P_0 tensor I+P_ch tensor W_t.
```

Projector orthogonality gives

```text
product_(t=1)^k U_t
 =P_0 tensor I+P_ch tensor product_(t=1)^k W_t.      (FG-9)
```

After the ready-record doubled sandwich, the charged factor at tier `t` is
`exp(Xi_t)`. Scalar factors commute, so `(FG-9)` gives `(FG-4)`. Contracting
the unchanged source state gives `(FG-5)`. The same realized-branch copier
induction gives `(FG-2)` and `(FG-3)`.

No step uses finite support of `R_t`; only the scalar continuity of
`Q_n^even` is required.

### 3.2 Closed forms

For `s^(k)=(s_1,...,s_k)`, define

```text
S_Xi,k[s^(k)] :=sum_t Xi_n^007(s_t),
S_L,k[J^(k)]  :=sum_t L_n^Theta(J_t),
S_Q,k[R^(k)]  :=sum_t Q_n^even(R_t).
```

Then

```text
S_Xi,k=S_L,k-(1/2)S_Q,k,
D_k=(1/2)S_Q,k,
F_k=P_0+exp(S_Xi,k)P_ch,
A_k=(1-p)+p exp(S_Xi,k).                            (FG-10)
```

Where `A_k` lies in the declared nonzero `Log_0` chart,

```text
Gamma_k=Log_0[(1-p)+p exp(S_Xi,k)].                 (FG-11)
```

Arbitrary completed sources can move `(FG-11)` outside that chart or onto a
zero of `A_k`. The operator and scalar amplitude `(FG-10)` remain defined;
no branch or global logarithm is selected.

### 3.3 Physical state weights versus tilted coefficients

The physical record-state weights are read from `(FG-3)`:

```text
weight_0(k)=1-p,
weight_ch(k)=p                                      (FG-12)
```

for every source sequence and every finite `k`.

One may algebraically rewrite `(FG-5)`, when nonzero, using source-tilted
coefficients

```text
w_0^tilt=(1-p)/A_k,
w_ch^tilt=p exp(S_Xi,k)/A_k.
```

These generally depend on the sources and may be complex. They are
generating-functional coefficients, not probabilities and not the branch
weights of `omega_tower,k`. Treating them as physical weights would conflate
the source port with the state port.

```text
FULL_SOURCE_REQUIRE_SIDE_WEIGHT_INVARIANCE = PASS | TYPE-P
SOURCE_TILTED_COEFFICIENTS_INVARIANT = false | TYPE-R
SOURCE_TILTED_COEFFICIENTS_ARE_PHYSICAL_RECORD_WEIGHTS = false | TYPE-R
```

---

## 4. Generalized `D_k` and complete growth classification

### 4.1 Scalar reduction

Set

```text
a_t:=Q_n^even(R_t),
D_k=(1/2)sum_(t=1)^k a_t.                           (FG-13)
```

Because `Q_n^even` is a nonzero continuous linear functional on `E_R`,
choose one admitted `R_0` with `Q_n^even(R_0)=1` after scalar rescaling. For
any prescribed scalar sequence `(d_k)` with `d_0=0`, define

```text
R_t:=2(d_t-d_(t-1))R_0.                             (FG-14)
```

Then `(FG-13)` gives `D_k=d_k` exactly. On a U1-real subfamily, take real
`d_k`; on the complete complex source class, complex `d_k` are admitted.

Therefore the full unbudgeted P2 cylinder family permits every partial-sum
growth pattern. No constraint in the record law narrows it.

### 4.2 Growth classes

The exact classifications are:

```text
bounded       iff sup_k |sum_(t<=k)a_t| < infinity;
convergent    if sum_t a_t converges;
sublinear     iff |sum_(t<=k)a_t|/k ->0;
linear        if (1/k)sum_(t<=k)a_t -> a_bar !=0;
super-linear if |sum_(t<=k)a_t|/k -> infinity.
```

Instantiated witnesses, with the common nonzero `R_0`, are:

| Source sequence | Exact `D_k` behavior |
|---|---|
| `R_t=(-1)^(t+1)R_0` | bounded and oscillatory |
| `R_t=R_0/t` | harmonic, unbounded sublinear |
| `R_t=R_0` | exact linear `k/2` in the normalized coordinate |
| `R_t=tR_0` | exact quadratic `k(k+1)/4` |
| `(FG-14)` | arbitrary prescribed partial sums |

The normalized coordinate in the table is only the proof witness
`Q(R_0)=1`; it is not a physical value or selected source.

### 4.3 Supremum behavior

Let

```text
q_norm:=||Q_n^even||_(E_R^*),
```

which is finite and nonzero by the V006 boundedness and finite-source
certificates.

On the full unbounded class `E_R^k`, for every `k>=1`,

```text
sup |D_k| = infinity.                               (FG-15)
```

It suffices to scale one source with nonzero `Q`.

If an external per-tier norm budget is stated,

```text
||R_t||_1 <= M,
```

then duality gives the exact supremum envelope

```text
sup |D_k|=(k/2)M q_norm.                            (FG-16)
```

The equality is a supremum statement: choose norm-approximating sources and
align their scalar phases. Under a total budget

```text
sum_t ||R_t||_1 <= B,
```

the all-tier envelope is

```text
sup_k |D_k| <= (B/2)q_norm,                         (FG-17)
```

with the bound sharp as a supremum. Neither `M` nor `B` is sealed by P2;
`(FG-16)` and `(FG-17)` are conditional mathematical controls, not new
physical inputs.

Uniformly norm-bounded source sequences cannot have super-linear `D_k`.
Every super-linear witness in the full class necessarily has unbounded
average source norm or cancellation-free growth beyond a uniform budget.

```text
FULL_CLASS_GROWTH_CAN_BE_BOUNDED = true | TYPE-P
FULL_CLASS_GROWTH_CAN_BE_LINEAR = true | TYPE-P
FULL_CLASS_GROWTH_CAN_BE_SUPER_LINEAR = true | TYPE-P
FULL_CLASS_GROWTH_IS_UNIVERSALLY_MONOTONE = false | TYPE-R
FULL_CLASS_FIXED_K_SUPREMUM = infinity | TYPE-P |
  scope: unbudgeted P2 source cylinder
```

---

## 5. One completed source: a P2 telescoping subfamily, not a forced feed

P2's own finite-cell filtration gives one exact way to turn a completed
source into an admitted tower source sequence. For

```text
s=(J_+,J_-,R) in E_src,
```

define its completed finite corners

```text
hat_s_t:=iota_src,t rho_src,t(s),
hat_s_0:=0,
delta_s_t:=hat_s_t-hat_s_(t-1).                    (FG-18)
```

Every `delta_s_t` is an admitted P2 completed source with finite support.
For the bilocal part,

```text
delta_R_t=P_t R P_t-P_(t-1)R P_(t-1).              (FG-19)
```

This increment includes the cross-cell bilocal blocks that first become
visible at stage `t`; it is not a diagonal-only or tier-local assumption.

The finite sum telescopes:

```text
sum_(t=1)^k delta_s_t=hat_s_k.                      (FG-20)
```

Linearity of `L` and `Q` gives

```text
sum_t Xi(delta_s_t)=Xi(hat_s_k),
D_k^shell[R]=(1/2)Q_n^even(hat_R_k).                (FG-21)
```

P2 proves `hat_s_k -> s` in source norm. Continuity of `Q` and `Xi` therefore
gives

```text
D_k^shell[R] -> (1/2)Q_n^even(R),
A_k^shell[s] -> (1-p)+p exp(Xi_n^007(s)).           (FG-22)
```

Moreover, compression is contractive, so

```text
|D_k^shell[R]| <= (1/2)q_norm ||R||_1              (FG-23)
```

for every `k`. This constructs one unrestricted completed-bilocal
**subfamily**: arbitrary cross-cell blocks are carried by the telescoping P2
corners. It does not prove that this is the tower's physical source feed.
P2's `N` counts finite cell labels; the tower's `k` counts refinement tiers.
No sealed map identifies those labels, and the arbitrary source-sequence
theorem does not require one.

### 5.1 Distinct repeated-source experiments

Three source-sequence constructions must remain distinct:

| Construction from one `R` | Tier input | Growth |
|---|---|---|
| distribute once by P2 shells | `delta_R_t=hat_R_t-hat_R_(t-1)` | bounded; converges to `Q(R)/2` |
| repeat the same completed source | `R_t=R` | exact linear `kQ(R)/2` |
| reapply cumulative corner | `R_t=hat_R_t` | `D_k/k -> Q(R)/2` by Cesaro; asymptotically linear if `Q(R)!=0` |

Only the first is a decomposition of one source without double counting
**relative to P2's finite-cell filtration**. The other two are lawful members
of the arbitrary source-sequence family, but they repeatedly supply already
counted source content. The corpus neither identifies these three experiments
nor selects one as refinement dynamics.

```text
ONE_COMPLETED_SOURCE_DECOMPOSES_BY_P2_CORNERS = true | TYPE-P
CROSS_STAGE_BILOCAL_BLOCKS_DROPPED = false | TYPE-R |
  test: FG-19 carries every block entering the next finite corner
ONE_COMPLETED_SOURCE_FORCES_LINEAR_DEPTH = false | TYPE-R |
  counterexample: P2 shell sequence FG-18 through FG-23
REPEATED_COMPLETED_SOURCE_GIVES_LINEAR_DEPTH = true | TYPE-P
P2_SHELL_FEED_IS_FORCED_AS_REFINEMENT_DYNAMICS = false | TYPE-R |
  counterfamily: the three rows above obey the same stagewise source interface |
  missing object: a sealed map from P2 cell filtration to refinement tiers
```

---

## 6. Recovery of Q-330 and finite controls

### 6.1 Declared tier-local probe tower

Take each `R_t` to be the previously declared tier-local probe and each
`J_t` the declared tier history. Then `(FG-10)` is exactly Q-330's

```text
D_k=(1/2)sum_t Q_t.
```

If `Q_n^even(R_t)=Q` and `Xi_t=Xi` for every tier,

```text
D_k=kQ/2,
A_k=(1-p)+p exp(kXi).                               (FG-24)
```

Thus the verified tower is recovered without changing a coefficient or
sign.

### 6.2 Tier 1

At `k=1`, `(FG-10)` gives

```text
F_1=P_0+exp(Xi_n^007[J_1,R_1])P_ch,
A_1=(1-p)+p exp(Xi_n^007[J_1,R_1]),                 (FG-25)
```

which is the live V007 complete-source germ. On the sealed one-cell finite
corner it reproduces the current one-cell source structure. At `R=0` it
reproduces the Q-243/Q-279 source-free finite rows; no void historical C-B
nonzero-R row is revived.

### 6.3 Identity

For `J_t=0` and `R_t=0` at every tier,

```text
Xi_t=0,
F_k=P_0+P_ch=I_src,
A_k=1,
D_k=0                                                (FG-26)
```

for every finite `k`.

### 6.4 Restriction and finite-core approximation

Prefix restriction removes the final source from the input family. The
state restriction is exact for every source sequence. The amplitude obeys

```text
A_(k+1)[s_1,...,s_k,0]=A_k[s_1,...,s_k].           (FG-27)
```

A nonzero last source changes the charged factor and is not falsely called
an amplitude restriction.

For fixed `k`, replace every completed source `s_t` by its P2 finite corner
`hat_s_(t,N)`. Norm convergence and continuity of `L`, `Q`, finite sums, and
the exponential give

```text
A_k[hat_s_(1,N),...,hat_s_(k,N)]
  ->A_k[s_1,...,s_k].                               (FG-28)
```

Thus arbitrary full-source rows are determined by sealed finite corners; no
source tail is introduced.

### 6.5 Reality, quotient, and rank

V006/V007 give, tierwise,

```text
L_(-n)^Theta(Theta_J J_t)=conjugate(L_n^Theta(J_t)),
Q_(-n)^even(Theta_R R_t)=conjugate(Q_n^even(R_t)).
```

Summing proves

```text
Xi_(-n),k(Theta s^(k))=conjugate(Xi_n,k(s^(k))),
A_(-n),k(Theta s^(k))=conjugate(A_n,k(s^(k))).      (FG-29)
```

Each `L` and `Q` descends through the ratified source quotient before the
sum, so the tower descends componentwise. The rank family enters only through
symbolic `p_[A]`; no rank pair or ratio value is selected.

```text
TIER_LOCAL_TOWER_RECOVERY = PASS
TIER_ONE_COMPLETE_SOURCE = PASS
IDENTITY_FALSIFIER = PASS
PREFIX_ZERO_EXTENSION = PASS
P2_FINITE_CORE_DETERMINATION = PASS
REALITY = PASS
QUOTIENT = PASS
RANK_DISCIPLINE = PASS
```

---

## 7. Scope, six-account, and door ledger

| Operation | Domain | Image | Restriction | Tail/class action | Standing |
|---|---|---|---|---|---|
| tier source evaluation | `E_src` | scalar `Xi_t` | W3/P2 natural | bounded; no source tail | built |
| finite source sum | `E_src^k` | scalar `S_Xi,k` | prefix and finite-core exact | finite only | built |
| controlled tower product | source plus finite record tensor | two-sector operator | tier-one and identity exact | finite matrix class | inherited/built |
| scalar contraction | two-sector operator | `A_k` | zero-tier exact | no new class | built |
| `Log_0` | nonzero local chart only | local scalar germ | common-chart only | no global branch | conditional domain |
| arbitrary infinite sequence limit | no ratified sequence topology | not formed | absent | could require new class | `TYPE-U` |
| single inter-tier bilocal kernel | no P2 tier-pair carrier | not formed | absent | new trace-class class required | `TYPE-U` |
| intrinsic feedback | record output to next source | not formed | absent | computation two territory | excluded |

Door flags:

```text
DOOR_P2_COMPLETED_SOURCE = OPENED_UNCHANGED |
  topology: P2 sum norm on each source |
  Tail_src: {0}

DOOR_FINITE_SOURCE_CYLINDER = OPENED |
  topology across tiers: none required or asserted |
  operation: finite product and finite sum only

DOOR_ONE_SOURCE_TELESCOPING_CORNERS = OPENED |
  topology: P2 norm |
  limit: source-norm convergence already sealed by P2 |
  weak-star/bidual: not used |
  physical tier-feed status: unforced

DOOR_INFINITE_SEQUENCE_COMPLETION = NOT_OPENED | TYPE-U
DOOR_INTER_TIER_BILOCAL_CARRIER = NOT_OPENED | TYPE-U
DOOR_INTRINSIC_FEEDBACK = NOT_OPENED | excluded parallel computation
DOOR_CONTINUUM_RESPONSE = NOT_OPENED | TYPE-S
DOOR_BRIDGE = NOT_OPENED | TYPE-S
```

No measure, contour, boundary datum, weak-star completion, bidual, response
operator, bridge map, or physical value is introduced.

---

## 8. Final determination

The widest sealed finite depth data are the family `(FG-10)` over all finite
P2 source cylinders. The generalized depth coordinate is exactly

```text
D_k[R_1,...,R_k]=(1/2)sum_(t=1)^k Q_n^even(R_t).    (FG-30)
```

Its consequences are:

```text
FULL_SOURCE_TOWER_STATE
  =(1-p)sigma_0,k+p sigma_1,k | all sources | all finite k

FULL_SOURCE_TOWER_AMPLITUDE
  =(1-p)+p exp(sum_t[L_n^Theta(J_t)-(1/2)Q_n^even(R_t)])

WEIGHT_INVARIANCE_VERDICT = INVARIANT | TYPE-P

GENERAL_GROWTH_VERDICT = NO_UNIVERSAL_CLASS |
  bounded, sublinear, linear, super-linear, oscillatory, and arbitrary
  prescribed partial sums all instantiated

SUPREMUM_VERDICT = INFINITE |
  scope: full unbudgeted P2 source cylinder at every fixed k>=1

ONE_COMPLETED_SOURCE_DISTRIBUTED_ONCE
  = D_k=(1/2)Q_n^even(iota_k rho_k R)
  ->(1/2)Q_n^even(R) |
  bounded in k | cross-cell blocks retained |
  standing: explicit P2-filtration subfamily, not selected refinement feed

DECLARED_PROBE_SPECIAL_CASE
  = D_k=(1/2)sum_t Q_t -> kQ/2 for identical probes
```

The result supplies the bridge with the widest sealed finite family, but it
does not select a source sequence, a source budget, or a growth class. Any
later use of "the" full-source depth law must state which source-sequence
construction it consumes. In particular, linear growth from repeated input
and bounded convergence from the P2 shell subfamily are distinct exact
objects. Selecting the shell subfamily as physical depth would additionally
require a map from P2's cell-stage filtration to the tower's refinement tiers.

```text
FULL_SOURCE_GENERALITY_COMPUTATION_THREE = COMPLETE | TYPE-P |
  scope: finite tower with one arbitrary completed P2 source per tier and
         the P2 source-norm telescoping subfamily

BRIDGE_CLAIM_MADE = false | TYPE-S
CONTINUUM_RESPONSE_OBJECT_USED = false | TYPE-S
INTRINSIC_TOWER_RESULT_USED = false | TYPE-S
INTER_TIER_BILOCAL_KERNEL_USED = false | TYPE-S
FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S

REGISTER_HEAD_AT_START = Q-331
REGISTER_SHA256_AT_START =
  87f0e61c94b2a4716c441658720985d1ff78ec91499b5dcb36d6368e19f3b652

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 9. Custody

This lane seals this lane-tagged artifact, verifies its sidecar, mirrors the
artifact and sidecar byte-identically, reports hashes, and stops. It does not
edit the register, governing plan, or tracker and performs no git, commit, or
push action.
