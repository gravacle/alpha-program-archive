# STAGE8 TASK 4A NETWORK-SOURCING LAW CROSS-REVIEW - LANE 1 V001

Date: 2026-08-03  
Task: PASTE 419 / Task 4a / adversarial cross-review  
Lane: CODEX LANE 1  
Custody: reviewer of the Lane-2 proposal  

```text
ARTIFACT_UNDER_REVIEW =
  STAGE8_TASK4A_NETWORK_SOURCING_LAW_ADOPTION_PROPOSAL_CODEX_LANE2_V001.md
EXPECTED_SHA256 =
  87f696261651567e04242abc1a54d5a2b457a19e07926e9e9856b02dc1719eb1
VERIFIED_SHA256 =
  87f696261651567e04242abc1a54d5a2b457a19e07926e9e9856b02dc1719eb1

REVIEW_POSTURE = ADVERSARIAL
PROPOSAL_STATUS = PROPOSED_NOT_ADOPTED

LEAD_FINDING = KILL
KILLING_ITEM = R7
KILLING_COUNTEREXAMPLE =
  the proposal emits a generic open-edge q as a scalar V007 source,
  but DoR-015 ratifies only conserved cycle currents ker(B_N^T) as
  scalar physical sources; a one-edge history gives B_N^T q != 0

SECOND_INDEPENDENT_KILL = R3
SECOND_KILL =
  the all-tier no-ignition induction has no recurrence for the compact
  write history; only its base emission is defined

TYPE_ACCOUNTING_KILL = R8
TYPE_ACCOUNTING_DEFECT =
  the unsupported all-tier bootstrap claim is upgraded to TYPE-R

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The proposal is killed. Its local logarithmic `d_J` seam and its V007
rank-one exponent algebra are correct on their stated local source chart. The
failure is one layer later and more physical: the proposal identifies every
such local difference coordinate with a scalar physical source. DoR-015
forbids that identification. Scalar physical sources are conserved cycle
currents; open-path content is endpoint-covariant transport. The proposal
contains neither the conservation restriction nor the endpoint-covariant
intertwiner needed to cross that seam.

Independently, the proposal proves only that identity history emits zero at
the next tier. It cannot repeat that statement inductively because it openly
lacks the map from received ports back to the next compact write history.

---

## 1. Preflight and custody

### 1.1 LOCKED_PROCESS

`/Users/bgm/MB Work/alpha_supervision/LOCKED_PROCESS.md` was read before the
review.

```text
LOCKED_PROCESS_SHA256 =
  f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba
FOUR_STEPS_ARE_REVIEWER_STEPS = true
LANE_ACTION = seal, mirror, report, stop
```

No reviewer-only register, plan, tracker, commit, or push action is taken by
this artifact.

### 1.2 Register head

The live register was checked before reading the proposal.

```text
REGISTER_HEAD = Q-336
REGISTER_SHA256 =
  8f1bae6ef276077e64fa67250703a1854bd7485156327c791bd9496ac457f2c1
PREFLIGHT_REGISTER_CHECK = PASS
```

### 1.3 Proposal hash before reading

The proposal hash was computed before substantive reading and matched the
relay exactly. Its local sidecar also matched.

```text
PROPOSAL_HASH_CHECK = PASS
PROPOSAL_SIDECAR_CHECK = PASS
```

### 1.4 Frozen authorities

The bounded authority set used in the review is:

| Authority | SHA-256 or standing | Use |
|---|---|---|
| DoR-009 | `11632fa30dfe9225c228f07a3be4717c73bdfc9e38b0c76c46d905d3fe193bc5` | C1-C8 and `E_post` |
| DoR-014 | `b6e4116df63403478d28be8cdb6589b091cc1aa8b6ad5a40776a28b135cd138f` | germ ratification |
| DoR-014 Amendment 1 | `8191feb4316ddeb08ef832b644c41847b31698224f6ab16b65dc1e1e2a574e56` | amended germ structure |
| DoR-014 Amendment 2 | `460da8c34e8a33503c0a5737f1d94b7a68cbb31fe636cd74c49e59a493efc282` | even source pairing |
| source germ V007 | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | live `L`, `Q`, `Xi`, `Z`, `W`, `N`, `G^007` |
| DoR-015 | `617bd51a70860d2cfb2066640630ba37ec289d56255ebbe1433bc0dfcba0159d` | physical quotient and source domain |
| FIELD_SIGNATURE_PHYS V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | conserved cycle sources and endpoint-covariant open paths |
| Q-334 | sealed register standing | closed theory depth-free; drive interface opened |
| Q-335 | `e73a3716aa8141bbbb501ae24138050f27f1eca7b66dde05fee25334d6db67e7` | independent C5 receiver-only and J-chart determination |
| Q-336 | live register head | proposal received for review |

DoR-009 states that `E_post` is the time-oriented assignment under which
charge follows the write's direction
(`DECISION_OF_RECORD_009_THE_TRANSITION_LAW_RATIFIED_E_POST_2026-08-02_V001.md:8-17`).

DoR-015 ratifies V005 and says, without an inference step, that:

1. `u_c`, `c in ker(B^T)`, are the physical response family; and
2. open-path content is endpoint-covariant transport, never a scalar
   coordinate

(`DECISION_OF_RECORD_015_FIELD_SIGNATURE_PHYS_RATIFIED_2026-08-02_V001.md:5-24`).

### 1.5 Preflight verdict

```text
DOES_REVIEW_OBJECT_EXIST = yes
IS_VERSION_CURRENT = yes through Q-336
ARE_INPUTS_PRESENT = yes
CUSTODY_VALID = yes
PREFLIGHT = PASS
```

---

## 2. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| R1 `d_J` seam | **PASS** | On the zero-anchored V007 chart, `L_b^Theta(d_J)=sum eta` and exponentiation reproduces the exact finite C5 relative character. |
| R2 exact tier exponents | **PASS** | V007 gives `Q^even(v symtensor v)=hbar ell(v)^2`; hence `Xi=x-(hbar/2)x^2`, with the Q-276 sign and every `hbar` owned once. |
| R3 no-ignition proof | **KILL** | `h_0=1 -> d_J=d_R=0` is a base case only; no port-to-write-history recurrence exists to prove `h_t=1` at the next tier. |
| R4 scope-boundary typing | **PASS** | The bounded ratified sweep finds receiver laws, source functionals, holonomy/current maps, and intertwiners, but no received-port tuple to compact write-history update. |
| R5 reciprocity and time arrow | **PASS** | Both reciprocal arrows run from tier `t` output to tier `t+1` input and preserve `E_post`; exact one-tier delay is authored, not uniquely forced. |
| R6 tower echo | **PASS** | The exponential is inherited from V007 and orthogonal projector multiplication; `k Xi` follows from repeated identical emissions rather than a fit. |
| R7 self-kill plus fresh attack | **KILL** | Fresh one-edge counterexample: generic proposal `q` is not in `ker(B_N^T)`, so an endpoint-covariant open path is smuggled into the scalar physical source port. |
| R8 TYPE-P smuggling scan | **KILL** | No positive TYPE-P or rank evaluation appears, but the unproved all-tier no-ignition statement is nevertheless promoted to TYPE-R. |

```text
R1 = PASS
R2 = PASS
R3 = KILL
R4 = PASS
R5 = PASS
R6 = PASS
R7 = KILL
R8 = KILL
```

---

## 3. R1 - independent `d_J` seam recomputation

### 3.1 Live finite receiver formula

On V007's finite zero-anchored chart, the receiver character covector has the
form

```text
L_(b,n_b)^Theta(J)=i n_b sum_j (J_delta)_j.          (R1-1)
```

This is the local additive chart for the exact finite relative character. It
is a receiver statement. Q-335 independently proved that it does not derive a
network emitter, but any proposed emitter must satisfy it
(`STAGE8_TASK4A_C5_EXTERNAL_HISTORY_TO_MUTUAL_SOURCING_DRIVE_DERIVATION_ARM_LANE1_V001.md:15-36,318-362`).

The proposal defines, on matched labels,

```text
u_(a,j)=conjugate(z_(a,-,j)^n_a) z_(a,+,j)^n_a,
eta_(a,j)=Log_0(u_(a,j)),

q_(a->b)=(i n_b)^(-1) tau_(ba) eta_a,
d_J^(a->b)=T_(CTP,J,b)^(-1)(0,q_(a->b)).            (R1-2)
```

For the proposal's instantiated identity cell matching, `tau_(ba)=Id`.
Therefore:

```text
L_(b,n_b)^Theta(d_J^(a->b))
 =i n_b sum_j q_(a->b,j)
 =i n_b sum_j (i n_b)^(-1) eta_(a,j)
 =sum_j eta_(a,j).                                  (R1-3)
```

Because every component is in the common connected `Log_0` chart,

```text
exp(L_(b,n_b)^Theta(d_J^(a->b)))
 =exp(sum_j Log_0 u_(a,j))
 =product_j u_(a,j).                                (R1-4)
```

At identity/equal history, `u_j=1`, so zero anchoring gives

```text
eta_j=Log_0(1)=0,
q=0,
d_J=0.                                              (R1-5)
```

The scalar coefficient is also locally forced. Replacing `d_J` by
`lambda d_J` would require

```text
exp(lambda sum eta)=exp(sum eta)
```

on a connected neighborhood of zero. Differentiation at zero gives
`lambda=1`.

### 3.2 Scope of the pass

This computation proves the local C5 receiver-character seam exactly. It
does **not** prove that arbitrary `q in ell^1` belongs to DoR-015's physical
scalar source carrier. That separate domain question is R7 and kills the
proposal.

```text
R1_LOCAL_CHARACTER_REPRODUCTION = PASS
R1_ZERO_ANCHOR = PASS
R1_UNIT_SCALAR_COEFFICIENT = FORCED_ON_CONNECTED_CHART
R1_PHYSICAL_CYCLE_DOMAIN_CERTIFICATE = NOT_PROVIDED_BY_R1
R1 = PASS
```

---

## 4. R2 - exact tier exponents and factor ownership

### 4.1 V007 formula used

V007 leaves the source functional unchanged:

```text
Xi_n[J,R]=L_n^Theta(J)-(1/2)Q_n^even(R),
Z_n[J,R]=(1-p_[A])+p_[A] exp(Xi_n[J,R]),
W_n[J,R]=-i hbar Log_0 Z_n[J,R].                    (R2-1)
```

The exact source is
`STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V007.md:102-124`.

The even rank-one bilocal pairing inherited by V007 is

```text
b_n^even=hbar ell_n tensor ell_n,
Q_n^even(f symtensor h)=hbar ell_n(f)ell_n(h),       (R2-2)
```

from
`STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V006.md:131-153`, retained
unchanged in V007 at `:18-27`.

### 4.2 Recompute NS-17 through NS-20

Let the proposal's transported physical difference vector be `v` and define

```text
x:=ell_n(v).                                        (R2-3)
```

The proposed rank-one bilocal is `v symtensor v`. Applying `(R2-2)` once:

```text
Q_n^even(v symtensor v)
 =hbar ell_n(v)ell_n(v)
 =hbar x^2.                                         (R2-4)
```

The linear source was normalized in R1, hence

```text
L_n^Theta(d_J)=x.                                   (R2-5)
```

Substitution in `(R2-1)` gives

```text
Xi=x-(1/2)(hbar x^2)
  =x-(hbar/2)x^2.                                   (R2-6)
```

This exactly reproduces NS-17 through NS-20.

### 4.3 Sign and `hbar` ledger

| Factor | Owner | Consequence here |
|---|---|---|
| `hbar` in `Q^even` | V007/Amendment-2 pairing `b^even=hbar ell tensor ell` | supplies the single `hbar` in `hbar x^2` |
| `-1/2` | sealed germ exponent `Xi=L-(1/2)Q` | supplies the minus sign and half |
| `-i hbar` | `W=-i hbar Log Z` convention | enters only after `Xi` and does not multiply `Xi` again |
| Q-276 sign | `D^2 Log Z|_0=-p(1-p) ell_delta tensor ell_delta` | controls the connected Hessian, not the sign of `Q` inside `Xi` |
| `N=i Id` | V007 source-to-output boundary | is not inserted into the exponent (`STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V007.md:92-100`) |

Thus neither the `W` convention nor `N=i Id` supplies a second `i` or a
second `hbar` to the tier exponent.

### 4.4 Scope of the pass

The algebra is valid for a rank-one bilocal built over an admitted physical
source vector. R7 shows that the proposal's generic `v` need not be admitted
by DoR-015. The formula passes; the generic physical application does not.

```text
R2_LINEAR_TERM = x
R2_QUADRATIC_TERM = hbar*x^2
R2_EXPONENT = x-(hbar/2)*x^2
R2_W_CONVENTION_DOUBLE_BILL = false
R2_Q276_SIGN_CONFLICT = false
R2 = PASS
```

---

## 5. R3 - hostile no-ignition audit

### 5.1 What the proposal actually proves

At the declared initial surface the two ready systems have identity/equal
history:

```text
h_(1,0)=1,
h_(2,0)=1.                                          (R3-1)
```

Zero anchoring proves:

```text
eta(h_(i,0))=0,
d_J(h_(i,0))=0,
d_R(h_(i,0))=0.                                    (R3-2)
```

The one-tier transport consequently supplies zero source tuples to tier 1:

```text
(J_(1,1),R_(1,1))=(0,0),
(J_(2,1),R_(2,1))=(0,0).                            (R3-3)
```

This is an exact base case and passes.

### 5.2 Missing induction arrow

To repeat `(R3-2)` at tier 1, an induction proof needs

```text
(J_(i,1),R_(i,1))=(0,0)  =>  h_(i,1)=1.             (R3-4)
```

No map with signature

```text
U_hist,i : (h_(i,t),J_(i,t+1),R_(i,t+1))
           -> h_(i,t+1)                             (R3-5)
```

or even the narrower

```text
F_hist,i : (J_(i,t+1),R_(i,t+1)) -> h_(i,t+1)       (R3-6)
```

exists in the proposal or in the bounded ratified stack. The proposal admits
this at its own lines 729-739 and 881-910.

Therefore the asserted induction

```text
h_(i,t)=1 -> emissions at t are zero
           -> h_(i,t+1)=1                           (R3-7)
```

breaks at its second arrow. The first arrow is proved. The second arrow is
unbuilt.

### 5.3 Model-theoretic countercheck

The partial proposal is compatible with at least two future closures:

```text
C_zero: F_hist(0,0)=1,
C_star: F_hist(0,0)=h_star,
        eta(h_star)!=0.                             (R3-8)
```

`C_star` is not adopted here and is not endorsed. It is a countermodel to the
claim that the current four fields entail all-tier no ignition. The current
four fields contain no predicate capable of excluding it because they contain
no `F_hist` at all.

Equivalently, if the histories are treated as external sequences, the
proposal itself says its tower consumes the actual supplied sequence. The
admitted sequence

```text
h_0=1,
h_1=h_star,
eta(h_star)!=0                                      (R3-9)
```

obeys every defined proposal map but makes the next emission nonzero. Calling
`(R3-9)` a declared history merely confirms the point: "no declared history"
can mean either that all future histories are externally fixed to identity,
in which case NS-28 is a tautological conditional, or that histories must be
generated autonomously, in which case the generating map is missing. Neither
reading yields the proposal's TYPE-R bootstrap theorem.

### 5.4 Correct standing

```text
READY_IDENTITY_FIRST_EMISSION = ZERO | PASS_WITHIN_PROPOSAL
READY_IDENTITY_FIRST_DELIVERED_PORT = (0,0) | PASS_WITHIN_PROPOSAL
ALL_ZERO_EXTERNALLY_STIPULATED_HISTORY_SEQUENCE = IDENTITY_TOWER |
  CONDITIONAL
AUTONOMOUS_READY_NETWORK_NO_IGNITION = NO_VERDICT / TYPE-U |
  missing: port-to-write-history update and zero-fixed-point certificate

NS27_BASE_CASE = PASS
NS28_ALL_TIER_INDUCTION = FAIL
R3 = KILL
```

This kill does not manufacture ignition. It refuses to certify a recurrence
that is not present.

---

## 6. R4 - bounded sweep for a port-to-write-history update

### 6.1 Query and roots

The scoped search covered:

1. DoR-009 and the ratified transition law V002, including C1-C8 and
   `E_post`;
2. DoR-014, both amendments, and source germ V007;
3. DoR-015 and FIELD_SIGNATURE_PHYS V005;
4. the exact source/current restrictions and endpoint-intertwiner clauses;
5. Q-334 and Q-335's explicit interface accounting.

The query sought any ratified map with a received `J/R` port tuple in its
domain and a compact write history, connection holonomy history, or next write
operator in its codomain.

### 6.2 Maps found, with direction

| Found ratified map | Direction | Why it is not the missing update |
|---|---|---|
| C5 receiver law | external compact history -> charged write modification | same direction as the existing receiver; not an inverse or next-history map |
| `E_post` write law | compact history -> finite write operator | consumes history; does not generate it from `J/R` |
| V007 source germ | `(J,R) -> Xi -> Z -> W` and derivatives | produces scalar/source-response data, not compact history |
| `K_J` / `K_R` source rigging | abstract source -> physical current/bilocal carrier | changes source representation, not source into write history |
| V005 `A -> H_N(A)` | connection representative -> finite holonomies | requires a connection `A` as input; it is not a source-driven evolution law for `A` |
| V005 `d Phi_c=u_c` | quotient tangent -> cycle phase differential | a kinematic differential identity, not history integration or evolution |
| endpoint torsor/intertwiner family | open-path transport plus matching endpoint data | transports an already given connection/history; does not create it from ports |

Q-335 already records the same boundary independently:

```text
MUTUAL_SOURCING_MAP_CONSTRUCTED = false | TYPE-U
DOOR_NETWORK_J_EMISSION = NOT_OPENED | TYPE-U
DOOR_NETWORK_R_EMISSION = NOT_OPENED | TYPE-U
DOOR_NETWORK_HISTORY_COMPLETION = NOT_OPENED | TYPE-U
```

at
`STAGE8_TASK4A_C5_EXTERNAL_HISTORY_TO_MUTUAL_SOURCING_DRIVE_DERIVATION_ARM_LANE1_V001.md:25-36,680-690`.

### 6.3 Verdict

```text
PORT_TO_WRITE_HISTORY_UPDATE_EXISTS_IN_BOUNDED_RATIFIED_STACK = false |
  TYPE-S |
  roots: DoR-009, transition V002, DoR-014 plus amendments, V007,
         DoR-015, V005, Q-334, Q-335 |
  exclusions: receiver maps, source scalarizations, source riggings,
              connection-to-holonomy maps, kinematic differentials,
              endpoint transport intertwiners |
  query: received J/R tuple -> compact write history or next connection

AUTONOMOUS_CLOSURE = TYPE-U
R4 = PASS
```

R4's pass strengthens R3's kill: the scope boundary is honestly absent, so it
cannot lawfully serve as an unstated induction step.

---

## 7. R5 - reciprocity and `E_post` time orientation

### 7.1 Exact temporal order

DoR-009 fixes the local write orientation: charge follows the write's
direction. The proposal's network rule has the following order:

```text
t:
  execute the local E_post write using history h_(a,t)
  retain the untraced history
  evaluate d_J[h_(a,t)] and d_R[h_(a,t)]

t+1:
  insert that tuple into neighbor b's source ports.                 (R5-1)
```

No output is inserted into the tier that produced it. The edge `a->b` is
therefore a forward edge in tier time.

### 7.2 Reciprocity does not reverse time

The reciprocal adjacency

```text
Adj_2 = [[0,1],[1,0]]                                (R5-2)
```

contains two spatial/node arrows:

```text
1 at t -> 2 at t+1,
2 at t -> 1 at t+1.                                  (R5-3)
```

Node exchange swaps the arrows but leaves `t<t+1` unchanged. There is no
backward-time edge and no same-tier simultaneity.

### 7.3 Authored delay precision

No-post-output supplementation forces delivery later than the producing
tier. It does not select exactly one tier over any positive integer delay.
The exact one-tier delay is consequently part of authored field `N`, as the
proposal's own choice table correctly discloses. The prose statement that
"the delay is forced" is valid only for the positive-delay property, not for
the value one.

```text
E_POST_LOCAL_ORIENTATION_PRESERVED = true
RECIPROCAL_NODE_EXCHANGE_REVERSES_TIME = false
SAME_TIER_RETROACTION = false
POSITIVE_DELAY_REQUIRED = true
EXACT_DELAY_EQUALS_ONE_DERIVED = false
EXACT_DELAY_EQUALS_ONE = AUTHORED_IN_N
R5 = PASS
```

---

## 8. R6 - tower echo recomputation

### 8.1 One-tier factor

V007 supplies the exact one-tier operator/scalar branch form

```text
F_t=P_0+exp(Xi_t)P_ch,                               (R6-1)
```

with orthogonal projectors

```text
P_0 P_ch=0,
P_0^2=P_0,
P_ch^2=P_ch.                                        (R6-2)
```

### 8.2 Product through depth

Multiplying the factors exactly:

```text
product_(t=1)^k F_t
 =P_0+exp(sum_(t=1)^k Xi_t)P_ch.                    (R6-3)
```

The cross terms vanish by `(R6-2)`. Contracting against the already forced
symbolic branch weights gives

```text
A_k=(1-p)+p exp(sum_(t=1)^k Xi_t).                  (R6-4)
```

For a stationary repeated emitted value `Xi_t=Xi`,

```text
A_k=(1-p)+p exp(k Xi),
Xi=x-(hbar/2)x^2.                                   (R6-5)
```

The exponential in `(R6-5)` is not introduced by the network proposal to fit
the known tower. It is inherited from V007's sealed `Z=(1-p)+p exp Xi`; the
network computation supplies the partial sum through exact multiplication.
The rank-one `R` choice supplies the particular quadratic term inside `Xi`,
not the exponential architecture.

### 8.3 Scope

This is a correct consequence for an admitted source sequence. It does not
repair R3's missing autonomous recurrence or R7's physical source-domain
failure.

```text
TOWER_EXPONENTIAL_OWNER = V007
TOWER_PARTIAL_SUM_OWNER = exact orthogonal-projector multiplication
STATIONARY_k_EXPONENT = computed conditional consequence
TOWER_FORM_FITTED_TO_KNOWN_RESULT = false
R6 = PASS
```

---

## 9. R7 - self-kill audit and fresh physical-domain attack

### 9.1 Assessment of the proposal's six self-attacks

| Proposal self-attack | Adversarial status | Review determination |
|---|---|---|
| additive-offset attack | failure-capable | Genuine: `J_0` or `R_0` would defeat zero anchoring and target independence. |
| state-valued freedom attack | failure-capable but formula-local | Genuine for the displayed `d_R`; it excludes an explicit free covariance slot. |
| declared-data disguise attack | failure-capable | Genuine: the map reads compact history, not an independent declared probe. |
| circularity/target-awareness attack | failure-capable | Genuine at formula level; no downstream value appears in membership. |
| normalization attack | strong | Genuine: J normalization is fixed locally; R normalization remains honestly authored. |
| missing history-update attack | strongest self-attack | Correctly finds the missing map, but fails to propagate that finding back into NS-28 and the TYPE-R bootstrap claim. |

The self-kill set is not cosmetic. It finds real vulnerabilities. It is
nevertheless incomplete because it tests the P2/V007 source chart without
rechecking the narrower physical source domain ratified later by DoR-015.

### 9.2 Fresh attack: conserved-current domain

FIELD_SIGNATURE_PHYS V005 proves and DoR-015 ratifies:

```text
Gate-4 tangent = coker(B_N),
scalar physical source dual = ker(B_N^T),
u_c(a)=<c,L_N a>,  c in ker(B_N^T).                 (R7-1)
```

The exact source lines are
`STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md:86-113,286-327`.
V005 then defines

```text
J_fin^005 = union_N {u_c : c in ker(B_N^T)},
J_phys^005 = completion(J_fin^005),                 (R7-2)
```

at `:319-320`, and the physical bilocal source class is built on that
quotient source domain at `:390-413`.

V005 is explicit that a bare open-edge scalar is not a physical scalar:

```text
open-path content = endpoint-covariant transport,
closed-cycle content = scalar physical source.      (R7-3)
```

See `:458-464`; DoR-015 repeats the distinction at its lines 15-18.

The proposal instead permits every local coordinate

```text
eta in ell^1,
q=(i n)^(-1) eta,                                   (R7-4)
```

and declares the resulting pure-difference object to be in the receiver's
scalar source port. It imposes no condition

```text
B_N^T q=0.                                          (R7-5)
```

### 9.3 Exact one-edge counterexample

Take one finite oriented edge `e:s->t`. In V005's convention,

```text
(B_N theta)_e=theta_t-theta_s,
B_N=[-1  1].                                        (R7-6)
```

Choose `n_b=+1` and a nonzero real `epsilon` small enough to remain in the
common `Log_0` chart. Let the sender relative history on the edge be

```text
u_e=exp(i epsilon),
eta_e=Log_0(u_e)=i epsilon.                          (R7-7)
```

The proposal emits

```text
q_e=(i n_b)^(-1)eta_e
   =(i)^(-1)(i epsilon)
   =epsilon.                                        (R7-8)
```

R1 still passes:

```text
exp(i n_b q_e)=exp(i epsilon)=u_e.                  (R7-9)
```

But physical source conservation fails exactly:

```text
B_N^T q
 =[-1;1] epsilon
 =[-epsilon;epsilon]
 !=0.                                               (R7-10)
```

Therefore

```text
q notin ker(B_N^T).                                 (R7-11)
```

At a connected tree stage V005 proves `ker(B_N^T)={0}` and calls the phase
sector scope-empty (`STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md:268-276`).
The proposal nevertheless emits the nonzero scalar `(R7-8)`. That is a direct
counterexample to its B1 physical port-typing claim.

### 9.4 Bilocal inheritance of the defect

The problem is not cured by the rank-one bilocal:

```text
v=K_J(d_J),
d_R=v symtensor v.                                  (R7-12)
```

DoR-015's physical bilocal class is a trace-class/symmetric class over
`J_phys^005`. Because the one-edge `d_J` is not in that physical scalar
source domain, `(R7-12)` is not a physical rank-one bilocal over the ratified
domain. Trace-class boundedness alone does not repair the wrong base carrier.

Consequently NS-19 and NS-20 are algebraically correct only after adding the
missing hypothesis

```text
q in ker(B_N^T),                                    (R7-13)
```

or after replacing scalar consumption by an endpoint-covariant construction.

### 9.5 Repair shapes, not executed

Two honest repair families exist, neither licensed silently here:

1. **Cycle restriction:** replace `Hist_emit` by the subfamily whose
   transported `q` satisfies `B_N^T q=0` at every finite stage. This changes
   the proposal's emission domain and may remove generic C5 open-path access.
2. **Endpoint-covariant emission:** retain open paths but emit a transport
   morphism together with matching endpoint data through the ratified torsor
   and intertwiner families. It must not be inserted as a bare scalar V007
   source.

A projection `q -> P_cycle q` is not an automatic repair. No canonical
projection is ratified, and projection would generally change the exact C5
character equation `(R1-4)`.

### 9.6 Fresh-attack verdict

```text
PROPOSAL_GENERIC_q_IN_PHYSICAL_SOURCE_DOMAIN = false | TYPE-R |
  counterexample: one-edge relative phase with B_N^T q!=0

OPEN_PATH_ENDPOINT_COVARIANCE_PRESERVED_BY_PROPOSAL = false |
  test: q is consumed as a scalar without endpoint data

PROPOSAL_B1_EXACT_PHYSICAL_PORT_TYPING = FAIL
PROPOSAL_B9_PHYSICAL_QUOTIENT_DESCENT = FAIL_FOR_GENERIC_HISTORIES
R7 = KILL
```

This attack is not among the proposal's six self-attacks.

---

## 10. R8 - TYPE-P, rank, and standing audit

### 10.1 Positive-claim scan

The proposal repeatedly marks its certificates as
`PASS_WITHIN_PROPOSAL`, and its positive theorems as proposal theorems. It
does not mark any authored field or positive proposal consequence `TYPE-P`.

```text
POSITIVE_TYPE_P_SMUGGLING_FOUND = false | scoped textual audit
PROPOSED_NOT_ADOPTED_MARKS_PRESENT = true
PASS_WITHIN_PROPOSAL_MARKS_PRESENT = true
```

### 10.2 Rank discipline

NS-17 retains

```text
p_i=r_(ch,i)/(r_(0,i)+r_(ch,i))                     (R8-1)
```

symbolically. No ordered rank pair is selected and no ratio is evaluated.

```text
RANK_PAIR_SELECTED = false
RANK_RATIO_EVALUATED = false
```

### 10.3 Smuggled negative standing

The proposal nevertheless states:

```text
TWO_READY_HISTORY_FREE_SYSTEMS_IGNITE = false | TYPE-R
TWO_READY_SYSTEM_BOOTSTRAP = NO_IGNITION | TYPE-R
TWO_READY_BOOTSTRAP_REFUTED = true | TYPE-R.         (R8-2)
```

Those claims occur at proposal lines 22-23, 714-715, and 984-986. R3 proves
that only the first zero-emission base case exists; the autonomous recurrence
is TYPE-U. Thus `(R8-2)` upgrades an unbuilt-closure result beyond proposal-
conditional standing even though no positive TYPE-P is used.

The lawful replacement is:

```text
IDENTITY_HISTORY_ZERO_EMISSION = PASS_WITHIN_PROPOSAL
AUTONOMOUS_TWO_READY_BOOTSTRAP = NO_VERDICT / TYPE-U
```

```text
R8_TYPE_P_SCAN = PASS
R8_RANK_DISCIPLINE = PASS
R8_ALL_CLAIMS_REMAIN_PROPOSAL_CONDITIONAL = FAIL
R8 = KILL
```

---

## 11. Consolidated determination

### 11.1 What survived

The following proposal-local mathematics survives independent review:

1. the zero-anchored local `Log_0` history coordinate;
2. exact local C5 relative-character reproduction by `d_J`;
3. the rank-one V007 evaluation
   `Q^even(v symtensor v)=hbar ell(v)^2`;
4. the exponent `Xi=x-(hbar/2)x^2` with correct signs and factors;
5. first-tier zero emission from identity history;
6. one-tier-delayed temporal compatibility with `E_post`;
7. exact V007 tower multiplication for an admitted supplied source sequence;
8. symbolic rank discipline and absence of positive TYPE-P claims.

### 11.2 What killed the proposal

Two independent load-bearing claims fail:

1. **Physical port domain, R7:** generic `q` is an arbitrary local open-edge
   coordinate, while DoR-015 admits scalar physical sources only from
   `ker(B_N^T)`. The one-edge calculation `(R7-6)` through `(R7-11)` is an
   exact counterexample. The proposal therefore does not compose with the
   ratified physical source carrier it claims to feed.
2. **Autonomous no ignition, R3:** the compact-history recurrence needed for
   the induction does not exist. The proposal proves a base case and then
   promotes it to an all-tier TYPE-R claim.

The R4 search confirms that the second failure is not repaired elsewhere in
the ratified stack.

### 11.3 Disposition

The proposal is not ratification-ready. A repair must, at minimum:

1. choose openly between cycle-restricted scalar emission and a fully
   endpoint-covariant open-path emission interface;
2. re-run R1 and R2 on that corrected carrier;
3. remove the all-tier TYPE-R no-ignition claim unless a port-to-write-history
   update and its zero-fixed-point theorem are supplied; and
4. re-run the battery with DoR-015 physical source descent as a separate,
   failure-capable row.

No repair is executed in this reviewer artifact.

```text
NETWORK_SOURCING_LAW_V001_LOCAL_J_SEAM = SURVIVES
NETWORK_SOURCING_LAW_V001_RANK_ONE_ALGEBRA = SURVIVES
NETWORK_SOURCING_LAW_V001_PHYSICAL_SOURCE_DESCENT = KILLED
NETWORK_SOURCING_LAW_V001_AUTONOMOUS_BOOTSTRAP = KILLED

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

OVERALL = KILLED (R7; independently R3 and R8)
