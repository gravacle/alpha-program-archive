# Stage 8 Task 4a Determiner Result and Door 7 Cross-Review — Lane 2 V001

Date: 2026-08-03  
Task: PASTE 427 / Task 4a / adversarial cross-review  
Lane: CODEX LANE 2  
Register head: Q-345  
Artifact under review: `STAGE8_TASK4A_TRANSVERSE_ACTION_DETERMINER_UNDER_DOR016_LANE1_V001.md`  

```text
OVERALL_REVIEW = SPLIT

DETERMINER_RESULT = CONFIRMED
DOOR_7_DECLARATION = KILLED

KILLING_ITEMS_FOR_DOOR_7 = X2, X5, X7
SURVIVING_RESIDUE =
  Q313_MAP1_FULL_FAMILY_EXTENSION_PLUS_TRANSVERSE_ACTION_COMPARISON_SQUARE

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 0. Lead determination

The physical conclusion survives: DoR-016 does not determine the transverse
physical action. The finite network-fed CTP accumulation is exact, but no
ratified action-comparison/2PI square turns that datum into the transverse
action required by the Q-408 chain.

Door 7 does **not** survive as declared. Its central D2 premise—no ratified
network carrier or composite reaches an incidence-cycle carrier—omits Q-313.
Q-313 already constructs, uniquely and `TYPE-P`,

```text
T_N^char := Hol_(c_square)^(-1) compose Z_N,
```

and proves that it factors `Z_N`, `F_N`, and `A_N` through the primitive
incidence-cycle quotient. DoR-016's `Z_N^CTP` is the same scalar character
product. Q-315 also certifies Map 1's physical restriction square. Therefore
the ratified composite

```text
doubled network history
  -> R_CTP cells
  -> Z_N^CTP = Z_N
  -> T_N^char
  -> Q_square subset of the physical incidence-cycle quotient
```

already exists at scalar-character level.

That composite is not the transverse action. It is square-scoped, does not
intertwine the full untraced dynamics, and has no action/Legendre/2PI
comparison square. The correct next object is consequently narrower than
Door 7: extend the existing Map 1 naturally over the complete realization
family where such an extension exists, then build the transverse
action-comparison square with an explicit trace-kernel sufficiency theorem.

---

## 1. Preflight, seals, and authorities

### 1.1 Mandatory preflight

```text
REGISTER_HEAD_REQUIRED = Q-345
REGISTER_HEAD_OBSERVED = Q-345

UNDER_REVIEW_EXPECTED_SHA256 =
  1d1cea3415c648597ac2f6793d5f00bdec6c0983e93469b2ef7aa694532f177f
UNDER_REVIEW_VERIFIED_SHA256 =
  1d1cea3415c648597ac2f6793d5f00bdec6c0983e93469b2ef7aa694532f177f
UNDER_REVIEW_SIDECAR_CHECK = PASS

PREFLIGHT = PASS
```

The artifact hash and sidecar were verified before the artifact was read.
`LOCKED_PROCESS.md` was then read in full. No preflight condition failed.

### 1.2 Load-bearing authorities

| Authority | SHA-256 / standing | Use in this review |
|---|---|---|
| transverse-action draft | `ed49624b6f5f0bcda94ee88a939a5751113b30d73192b2c28a5aec25829e1797` | original `phi_div` signature and eight-field bridge |
| network law V004 | `69f4d93b9f84075a3112fb011b9838f380fb8c0341610572170cf7a13d5aed08` | doubled export, trace, tower, doors and falsifiers |
| DoR-016 | `b4157df6f327e261f40389d5a3011a0aef66ee0f198d8ebba8b1b9303142d708` | ratifies V004's single law |
| FIELD_SIGNATURE_PHYS V005 / DoR-015 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | physical quotient and conserved-cycle dual |
| Q-313 Map-1 build | `ea8f4e9a79a9e4aca4a0b9e9aab470d78cd4d9c78794c20d9e979c0db16fbeab` | existing scalar-character cycle factorization |
| Q-315 transport squares | `f886284c632f238bb01d02de2cc64e3f7ed76c0bae4ba14487ac0b2bde7a22e3` | Map-1 physical restriction square |
| Q-334 through Q-345 | live register | network-source lineage and current disposition |

### 1.3 Symbol-collision ledger

The following collisions are load-bearing:

1. `Z_N^CTP` in DoR-016 and `Z_N` in Q-313 are the same consumed scalar
   character after setting
   `r_j=conjugate(z_(-,j))z_(+,j)`; they are not independent objects.
2. `Q_rel,N` is the common-gauge relative-history quotient;
   `Q_square` is the Gate-4 incidence-cycle quotient; the bilocal probe
   `Q_N(R)` is neither.
3. `K_cycle,1={0}` is the same-stage one-edge conserved-current carrier.
   It is not Q-313's fixed primitive `Q_square` target.
4. `NetAcc` is a multiplicative trace product, not an action, a logarithm,
   `Gamma_2PI`, or `RetHess_phys`.

No argument below crosses those types silently.

---

## 2. Verdict table X1–X7

| Item | Verdict | Determination |
|---|---|---|
| X1 — D1 gap statement | **PASS** | draft signature and eight-field determination condition quoted accurately |
| X2 — D2 typing chain | **KILL** | Q-313/Q-315 supply an omitted ratified indirect cycle route at scalar-character level |
| X3 — D3 determination | **PASS** | scoped to a supplied finite delivered-history sequence: `NetAcc` and each per-system tower are exact; no autonomous network dynamics is inferred |
| X4 — one-edge falsifier | **PASS** | narrow scope: exact values refute factorization through the one-edge stage's zero cycle carrier; they do not refute Q-313's cross-carrier Map 1 |
| X5 — Door 7 definition | **KILL** | duplicates built Map 1 and omits trace-kernel sufficiency/locality plus several regression-level certificates |
| X6 — independence from Doors 1–6 | **PASS** | after narrowing, the action-comparison residue is genuinely distinct; Door 5 is a completed-form prerequisite and Doors 1/4 are conditional routes |
| X7 — fresh attack | **KILL** | Q-313 constructs the cycle descent; a second product-kernel attack shows `NetAcc` alone is not a sufficient action determiner |

---

## 3. X1 — the D1 gap statement

### 3.1 Exact draft signature

The source draft states:

```text
phi_div : X_phys or K_cycle -> scalar action correction.
```

It further requires a common-origin, stage-compatible, topology-declared map
from a certified divergence datum to a scalar functional on `K_cycle`.
The artifact under review reproduces both statements without weakening
“action correction” to “scalar value.”

### 3.2 Exact determination package

The draft's required bridge has eight fields:

```text
DivergenceDatum,
DepthMap,
CycleMap,
AccumulationRule,
ActionComparisonSquare,
GeneratorAndUniquenessCertificate,
FormCertificates,
ProvenanceCertificate.
```

The artifact quotes all eight and correctly records that a scalar coefficient
without fields 2–8 cannot enter Q-408. Its conclusion that the present
network law does not, by itself, supply an action-comparison square is not a
strawman.

The later reduction to “CycleMap plus ActionComparisonSquare” is not a quote
from the draft; it is the artifact's current-state assessment. X2 shows that
the `CycleMap` half of that assessment is stale, but this does not impeach the
accuracy of its D1 quotation.

```text
X1 = PASS
```

---

## 4. X2 — carrier-by-carrier typing and the omitted composite

### 4.1 Direct network carriers

The artifact's direct-carrier table is correct:

| Object | Actual carrier | Direct action signature? |
|---|---|---|
| `(T_+,T_-)` | doubled endpoint-covariant open-path morphisms | no scalar and no action argument |
| `R_CTP=T_-^dagger T_+` | relative endpoint endomorphism | conjugation-covariant, not an incidence action |
| `Z_N^CTP` | scalar function on finite doubled histories | scalar codomain only; not itself an action |
| `F_(i,k),A_(i,k)` | one receiver's charged-projector/tower carrier | conditioned operator/amplitude, not action |
| ordered tower pair | ordered product object | no joint contraction and no scalar network action |

No one object in that table directly has domain `X_phys` or `K_cycle`.

### 4.2 The ratified indirect route the artifact missed

Q-313 begins with the common-gauge relative coordinate

```text
r_j=conjugate(z_(-,j))z_(+,j)
```

and its exact scalar character

```text
Z_N(r)=product_j r_j^n.
```

DoR-016 gives exactly

```text
Z_N^CTP
 =product_j conjugate(z_(-,j)^n)z_(+,j)^n
 =product_j r_j^n
 =Z_N(r).                                           (X2-1)
```

Q-313 proves for the sealed primitive square cycle

```text
Hol_c:Q_square->U(1)
```

that `Hol_c` is an isomorphism, then constructs uniquely

```text
T_N^char:=Hol_c^(-1) compose Z_N.                   (X2-2)
```

It proves:

```text
Hol_c compose T_N^char=Z_N,
T_M^char compose j_NM^Q=T_N^char,
T_N^char(Theta_rel r)=Theta_square(T_N^char(r)),
```

and explicitly records:

```text
M1_FACTORS_Z_N = true | TYPE-P
M1_FACTORS_F_N_AND_A_N_THROUGH_THEIR_Z_N_CONTENT = true | TYPE-P.
```

Q-315 subsequently certifies `MAP1_SCALAR_RESTRICTION_SQUARE = PASS |
TYPE-P` and lists the image as the primitive cycle quotient character.

Combining `(X2-1)` and `(X2-2)` yields a ratified composite from the
DoR-016 network trace to an incidence-cycle quotient. Therefore these claims
in the reviewed artifact are false as stated:

```text
NO_RATIFIED_NETWORK_COMPOSITE_REACHES_A_CYCLE_CARRIER
CYCLE_MAP = TYPE-U_WITHOUT_EXISTING_LOWER_LEG
ONE_EDGE_TEST_CONFIRMS_NECESSITY_OF_AN_ENTIRE_NEW_CYCLE_DESCENT
```

### 4.3 What the omitted route does not solve

Map 1 has a strict ceiling:

```text
M1_INTERTWINES_FULL_UNTRACED_U_N = false | TYPE-U
M1_ARBITRARY_CELLULATION_NATURALITY_BUILT = false | TYPE-U
M1_IS_A_FULL_DYNAMICS_INTERTWINER = false | TYPE-R
```

Its target is the sealed primitive `Q_square`, not a completed
family-natural action on every realization. It factors scalar `Z`, `F`, and
`A` content only. It does not build `Gamma_2PI`, an action normalization, the
physical inverse/Schur block, or the action-comparison square. Thus X2 kills
the door's claimed necessity and interface breadth, not the ultimate
`TRANSVERSE_ACTION_RESIDUE = NOT_DETERMINED` result.

```text
X2 = KILL
KILL_TARGET = D2_NO_INDIRECT_CYCLE_ROUTE_AND_DOOR7_ENTIRE_CYCLEMAP_CLAIM
```

---

## 5. X3 — maximal finite determination

For each receiver `i`, supplied tier `t`, and finite cell set,

```text
Z_(i,t)^CTP[h]
 =product_j conjugate(z_(-,i,t,j)^n)z_(+,i,t,j)^n,

NetAcc_(i,k)[h]
 =product_(t=1)^k Z_(i,t)^CTP[h],

A_(i,k)[h]
 =(1-p_i)+p_i NetAcc_(i,k)[h].                     (X3-1)
```

Given the delivered doubled histories, every operation in `(X3-1)` is fixed
by DoR-009 and DoR-016:

- `R_CTP` uses both branches and the sealed adjoint order;
- the faithful-character content is the ratified family, with no member
  selected;
- identity delivery contributes one;
- coarse/refined batching agrees by composition and character
  multiplicativity;
- `p_i` remains symbolic;
- each receiver remains separate and the network output is an ordered pair.

There is no hidden contraction or normalization in this finite receiver
functional.

The scope is essential. DoR-016 does not uniquely fix the positive delay
member and does not supply the port-to-write-history update. Hence it does not
determine an autonomous sequence of future histories. The exact claim is:

```text
FINITE_NETWORK_FED_CTP_ACCUMULATION_GIVEN_DELIVERED_HISTORIES
  = DETERMINED | TYPE-P |
    premises: DoR-009, DoR-015, DoR-016

AUTONOMOUS_NETWORK_HISTORY_SEQUENCE = NOT_DETERMINED / TYPE-U
```

The reviewed artifact uses `NetAcc[h]` as a functional of histories and does
not execute an autonomous recurrence. With that scope, D3 is sound.

```text
X3 = PASS
```

---

## 6. X4 — exact one-edge falsifier

### 6.1 Recalculation

For one oriented edge `e:s->t`, the incidence transpose sends a scalar edge
coefficient to

```text
B_1^T q=(-q,q),
```

so

```text
K_cycle,1=ker(B_1^T)={0}.                           (X4-1)
```

Take

```text
T_-=I,
T_+=exp(i epsilon),
```

with `epsilon` symbolic and outside the character's identity kernel. Then

```text
R_CTP=exp(i epsilon),
Z_1^CTP=exp(i n epsilon),
A_1=(1-p)+p exp(i n epsilon).                       (X4-2)
```

At identity history,

```text
R_CTP=I,
Z_1^CTP=1,
A_1=1.                                              (X4-3)
```

`Z_1^CTP` is nontrivial under the stated character condition. `A_1` is also
nontrivial when `p!=0`; its exact displayed value remains correct even at a
degenerate symbolic endpoint.

### 6.2 Exact scope of the contradiction

Let `q_1` be the same-stage path-visible projection to `(X4-1)`. Then

```text
q_1(h_e)=q_1(I)=0.
```

No `Phi` can obey `Z_1^CTP=Phi compose q_1` on both histories, because
`(X4-2)` and `(X4-3)` differ. The same conclusion holds for `A_1` under the
nondegenerate `p` condition.

This is a valid refutation of the **same-stage direct quotient**. It leaves
DoR-016's R7 regression intact: the one-edge datum is access, not a scalar
cycle source.

It does not refute Q-313's cross-carrier construction. `T_1^char` maps the
scalar character to the separately sealed primitive `Q_square`, whose cycle
carrier is nonzero. Therefore the line
`DOOR_7_NECESSITY=CONFIRMED` does not follow from the one-edge test without
the additional premise that every lawful descent must target the same-stage
one-edge kernel. No such premise is sealed.

```text
X4 = PASS | scope: same-stage direct factorization only
GLOBAL_NO_CYCLE_DESCENT_FROM_X4 = false | TYPE-R |
  counterexample: Q-313 T_N^char
```

---

## 7. X5 — Door 7 interface and certificates

### 7.1 Domain audit

The words “full no-selection family” are present, and the listed domain
includes doubled histories, `R_CTP`, traces, and towers. It does not select a
frame, orientation, rank, filtration, or joint contraction. At the level of
declared membership, this part passes.

The interface nevertheless conflates four possible consumption levels:

```text
raw doubled history;
cellwise R_CTP endomorphisms;
product trace Z_N^CTP / NetAcc;
conditioned projector tower A_N.
```

Those maps have different kernels. A door cannot claim one determination
until it declares which level the action consumes and proves that the
discarded fibers are action-invisible.

### 7.2 Factorization-chain audit

The required chain is not correctly current. Its scalar-character lower leg
already exists by Q-313 and its restriction square by Q-315. A lawful
successor must consume or extend Map 1, not define a rival `CycleMap`.

The remaining chain is:

```text
DoR-016 finite scalar character
  -> existing Q-313 Map 1 on Q_square
  -> full-family extension, if it exists
  -> transverse action-comparison / 2PI descent.
```

### 7.3 Eleven-item list: covered and missing

The reviewed list does cover the specifically named gate-cycle hazards:

| Hazard | Covered? | Clause |
|---|---|---|
| tree/open-path gauge | yes | annihilate tree/open-path gauge content |
| record-visible cycles | yes | preserve every record-visible cycle |
| family naturality | yes | full no-selection family-natural clause |
| frames/orientations/filtrations | yes | explicit no-selection clause |
| U1 reality | yes | reality covariance |
| identity extension | yes | zero-extension compatibility |
| CTP batching | yes | batching compatibility |
| stage restriction | yes | restriction compatibility |
| action/log convention | yes | normalization and branch declaration |
| Door 4 | yes | no joint contraction unless separately opened |
| common origin and uniqueness | yes | final two clauses |

But completeness fails. The following certificates are missing:

1. **Existing-Map compatibility.** A commuting comparison with Q-313 Map 1
   and Q-315's restriction square; otherwise Door 7 can author a rival cycle
   descent over a built theorem.
2. **Trace-kernel sufficiency/locality.** Proof that histories with the same
   `Z_N^CTP`/`NetAcc` must have the same transverse action, or an explicit
   declaration that the action consumes cellwise `R_CTP` data instead.
3. **Kernel/image and sector-transfer disclosure.** The one-edge test proves
   that a cycle descent must delete some nontrivial access variation. The door
   must state exactly which kernel is lawful and prove that no
   record-visible cycle is deleted.
4. **Exact finite-falsifier reproduction.** General “restriction compatible”
   is weaker than reproducing DoR-008, S8-B backward-branch sensitivity,
   R7, reality, and identity/batching formulas at the correct carrier level.
5. **Timing and autonomy scope.** Positive-delay covariance,
   no-post-output supplementation, and an explicit statement that no
   port-to-history recurrence is inferred while Door 3 remains closed.
6. **Tail/finite-authority accounting.** The completed action map needs an
   explicit Tail/action-class row; “completion topology declared” does not
   certify that completion creates no action-visible non-finite content.

Any one omission prevents a commissioning-grade interface. The first two
are decisive because Q-313 and the trace-product kernel are already concrete.

```text
X5 = KILL
KILL_TARGET = DOOR7_INTERFACE_AND_CERTIFICATE_COMPLETENESS
```

---

## 8. X6 — independence from Doors 1–6

After removal of the duplicated CycleMap claim, the remaining
action-comparison/2PI descent is genuinely distinct from all six DoR-016
doors:

| Existing door | Why it does not imply the residual action comparison |
|---|---|
| 1 — Branch-B scalarization | converts endpoint access to V007 scalar source; it does not define a transverse action |
| 2 — network `R` | supplies a bilocal network receiver, not the cycle-action comparison |
| 3 — port-to-history update | closes autonomous recurrence, not action descent |
| 4 — joint two-system contraction | may supply a joint scalar route, but no action interpretation or cycle comparison follows |
| 5 — completed physical contraction | supplies completed state/effect consumption, but not the action map; it is a prerequisite for Door 7's completed version |
| 6 — W3-compatible history restriction | supplies an alternative history restriction, not the action/2PI square |

Door 5 is correctly identified as necessary for a **completed** physical
contraction route. A finite/cylindrical precursor can be discussed without
claiming Door 5 is open, but it cannot be promoted to the completed physical
action. Doors 1 and 4 are correctly conditional alternatives: a source-port
route would use Door 1; a joint-network scalar route would use Door 4.

The omitted prerequisite is existing Map 1, not content of Doors 1–6.

```text
X6 = PASS | scope: narrowed action-comparison residue
DOOR_RESIDUE_DISTINCT_FROM_DOORS_1_THROUGH_6 = true
```

---

## 9. X7 — fresh attacks

### 9.1 Strongest derivation attempt from ratified content

Use only ratified/built objects:

```text
T_N^char=Hol_c^(-1) compose Z_N^CTP,

Atilde_p([x]):=(1-p)+p Hol_c([x])
  for [x] in Q_square.
```

Then exactly

```text
A_N=Atilde_p compose T_N^char.                      (X7-1)
```

Thus both the network trace and its conditioned amplitude factor through an
incidence-cycle quotient. `(X7-1)` is a direct counterexample to the reviewed
artifact's broad claim that no ratified composite can make any such descent.

`Atilde_p` is still an amplitude, not a transverse action correction. Calling
it `phi_div` would silently add:

- the action comparison and units/normalization;
- any logarithm and its branch/domain;
- full-realization-family naturality beyond the sealed square;
- the stationary Legendre/2PI placement;
- proof that discarded history fibers are action-invisible.

Therefore the attack reaches the cycle carrier but stops honestly before the
action. It kills Door 7 as an entirely new CycleMap-plus-action bridge while
confirming the narrower physical determiner result.

### 9.2 Fresh trace-product-kernel attack

Take two two-cell relative histories, for arbitrary admitted phases `u,v,w`:

```text
r =(u,   v),
r'=(u w, v w^(-1)).
```

They have the same trace product:

```text
Z_2(r)=u^n v^n=Z_2(r'),
```

and therefore the same `NetAcc`, `F`, and `A`, while their cellwise relative
endomorphism data differ generically. If those cells occupy different
incidence positions, a local or distributed transverse action can distinguish
them without violating any theorem currently cited by Door 7.

Consequently `NetAcc` is not proved to be a sufficient statistic for the
transverse action. A successor must either:

```text
prove ker(Z/NetAcc) subset ker(action descent),
```

family-wide and restriction-naturally, or retain the cellwise `R_CTP` data in
the action interface. The reviewed eleven-item list contains neither
obligation.

```text
X7 = KILL
FRESH_ATTACK_1 = EXISTING_Q313_CYCLE_DESCENT
FRESH_ATTACK_2 = TRACE_PRODUCT_NONINJECTIVITY
```

---

## 10. Repaired residue — finding only, not a construction

This review does not build or ratify a replacement. It records the smallest
interface left after the attacks:

```text
REPAIRED_DOOR_7_RESIDUE := (
  ExistingLowerLeg:
    consume Q-313 T_N^char and Q-315 restriction square;

  FamilyExtension:
    extend Map 1 over the complete no-selection realization family,
    or prove and disclose the exact scoped family on which it exists;

  ConsumptionSignature:
    declare whether the action consumes cellwise R_CTP, Z_N^CTP,
    NetAcc, F, or A;

  TraceKernelCertificate:
    prove the discarded fibers are action-invisible, or retain them;

  ActionComparisonSquare:
    map the cycle quotient content to a scalar transverse action with
    normalization, topology, domains, stationary/2PI placement, restrictions,
    reality, common-origin, Tail, finite-authority, and no-selection proofs;

  DoorDependencies:
    Door 5 for completed contraction;
    Door 4 only for a joint-network route;
    Door 1 only for a source-port route;
    Door 3 remains closed unless autonomous histories are claimed
).
```

This is not the original Door 7. It removes a built component, adds the
missing information-loss theorem, and sharply separates finite character
descent from physical action formation.

---

## 11. Final verdict and custody

```text
X1_D1_GAP_STATEMENT = PASS
X2_D2_TYPING_CHAIN = KILL
X3_D3_FINITE_DETERMINATION = PASS | scope: supplied history sequence
X4_ONE_EDGE_FALSIFIER = PASS | scope: same-stage direct quotient
X5_DOOR7_DEFINITION = KILL
X6_DOOR_INDEPENDENCE = PASS | scope: narrowed action-comparison residue
X7_FRESH_ATTACK = KILL

FINITE_NETWORK_INPUT_GIVEN_HISTORIES = DETERMINED | TYPE-P |
  premises: DoR-009, DoR-015, DoR-016

Q313_SCALAR_CHARACTER_CYCLEMAP_EXISTS = true | TYPE-P
Q315_MAP1_RESTRICTION_SQUARE = PASS | TYPE-P
FULL_FAMILY_MAP1_EXTENSION = NOT_BUILT / TYPE-U
TRANSVERSE_ACTION_COMPARISON_SQUARE = NOT_BUILT / TYPE-U
TRANSVERSE_ACTION_RESIDUE = NOT_DETERMINED / TYPE-U

DETERMINER_RESULT = CONFIRMED
DOOR_7_DECLARATION = KILLED

FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S |
  scope: all requested structural tests were permitted

REGISTER_HEAD_AT_BUILD = Q-345

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

Codex Lane 2 seals this lane-tagged artifact, mirrors the artifact and
sidecar byte-identically to `alpha-program-archive/workspace/`, reports both
hashes, and stops. It does not edit the register, governing plan, tracker, or
git state and performs no commit or push action.
