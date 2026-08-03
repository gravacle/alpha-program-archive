# STAGE8 TASK 4A: TRANSVERSE ACTION DETERMINER UNDER DoR-016 (LANE 1 V001)

**DERIVATION ARTIFACT -- NO RATIFICATION, REGISTER, OR DOWNSTREAM EVALUATION**

```text
LEAD_RESULT = BLOCKED_ON_DOOR_7_NETWORK_CTP_TOWER_TO_TRANSVERSE_CYCLE_ACTION_DESCENT

DOR016_FIXES_FINITE_NETWORK_INPUT = true | TYPE-P |
  premises: DoR-009, DoR-015, DoR-016

DOR016_FIXES_TRANSVERSE_ACTION_DETERMINING_PRINCIPLE = false | TYPE-R |
  reason: none of the ratified network carriers has domain X_phys or K_cycle;
          the one-edge finite test refutes direct factorization

TRANSVERSE_ACTION_RESIDUE = NOT_DETERMINED / TYPE-U

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Preflight, custody, and currency

All preflight checks passed before the draft was read.

| Item | Result |
|---|---|
| register head | `Q-344` |
| current register SHA-256 | `d580a2f827099c42c747b441fa4156bc430e4c558b848654a3c9908fa1168411` |
| locked process | seal verified; SHA-256 `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` |
| target draft | hash matched before reading; seal verified |
| target draft SHA-256 | `ed49624b6f5f0bcda94ee88a939a5751113b30d73192b2c28a5aec25829e1797` |
| DoR-016 | in force; seal verified |
| DoR-016 SHA-256 | `b4157df6f327e261f40389d5a3011a0aef66ee0f198d8ebba8b1b9303142d708` |
| V004 source law | seal verified; SHA-256 `69f4d93b9f84075a3112fb011b9838f380fb8c0341610572170cf7a13d5aed08` |
| DoR-015 V005 carrier authority | SHA-256 `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` |

The object under determination exists as an unbuilt residue, the version is
current through Q-344, and the inputs required for this typing determination
are present.

```text
DOES_THE_OBJECT_EXIST = yes | standing: named unbuilt residue
IS_THE_VERSION_CURRENT = yes | register: Q-344
ARE_THE_INPUTS_PRESENT = yes | scope: structural typing determination
```

## 2. D1 -- the gap, exactly as the draft states it

### 2.1 Target object

The draft at lines 33-38 requires an object with the signature

```text
phi_div : X_phys or K_cycle -> scalar action correction.
```

It then states at lines 73-75 that the missing construction is

```text
a common-origin, stage-compatible, topology-declared map from a
certified divergence datum to a scalar functional on K_cycle.
```

This is not merely a missing scalar coefficient. The target is a functional
whose argument is the physical incidence-cycle carrier and whose value is an
action correction.

### 2.2 Undetermined freedom

Before DoR-016, the draft found:

```text
1. no certified divergence datum that is already a cycle action;
2. no map identifying a depth variable with the sequential record system;
3. no quotient-compatible map to X_phys or K_cycle;
4. no stage-compatible action accumulation rule and topology;
5. no source/depth-to-physical-action comparison square;
6. no generated member or uniqueness theorem;
7. no complete action-form certificates;
8. no common-origin provenance square reaching the action.
```

The exact determination condition appears at draft lines 565-605 as the
eight-field `DIVERGENCE_TO_CYCLE_ACTION_BRIDGE`:

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

The draft's own final sentence is controlling: a scalar coefficient without
items 2-8 cannot enter the Q-408 action formulas.

### 2.3 What changed after that draft

The old draft predates the verified finite-depth tower and DoR-016. Current
authority now supplies more finite structure than the draft had:

```text
Q-330/Q-331: an exact source-conditioned finite accumulation exists;
Q-333: its full P2 form is source-dependent and has no universal growth law;
Q-334: the closed pre-network theory remains on the identity slice;
DoR-016: actual neighboring histories now supply exact doubled CTP access
         and a finite multiplicative receiver tower.
```

Therefore the old statement "there is no finite accumulated datum" is
superseded in this narrow network-fed sense. The stronger statement "there is
no map from that datum to a scalar functional on K_cycle" remains to be tested
below.

```text
OLD_FINITE_INPUT_ABSENCE = SUPERSEDED_IN_NETWORK_FED_SCOPE
OLD_CYCLE_ACTION_BRIDGE_ABSENCE = REOPENED_AND_TESTED_HERE
D1 = COMPLETE
```

## 3. D2 -- carrier-by-carrier seam typing

### 3.1 Ratified law chain

V004 lines 288-307, ratified by DoR-016, supply the Level-I emission

```text
T_sigma[h] : E_(sigma,s) -> E_(sigma,t),
d_acc^B[h] = (T_+[h],T_-[h]).
```

This is an ordered pair of endpoint-covariant open-path morphisms. Under the
full retained endpoint torsor family,

```text
T_sigma[g_sigma.h]
 = g_(sigma,t) T_sigma[h] g_(sigma,s)^(-1).
```

V004 lines 309-346 supply the Level-II receiver object

```text
R_CTP[h] = T_-[h]^dagger T_+[h] in End(E_s),
R_CTP -> g_s R_CTP g_s^(-1),
R_CTP[Theta h] = R_CTP[h]^dagger.
```

V004 lines 348-383 supply the only ratified scalar consumption:

```text
Z_N^CTP[h]
 = product_(j=1)^N chi_n(R_(CTP,j)[h])
 = product_(j=1)^N conjugate(z_(-,j)^n) z_(+,j)^n.
```

This is a finite single-receiver DoR-009 ready-record trace. It is not the
unbuilt joint two-system contraction and not a completed physical
contraction.

V004 lines 386-419 then give, per receiving system,

```text
P_(i,k)[h] := product_(t=1)^k Z_(i,t)^CTP[h],

F_(i,k)^B = P_(0,i) + P_(i,k)[h] P_(ch,i),

A_(i,k)^B = (1-p_i) + p_i P_(i,k)[h].
```

The complete network object is only the ordered pair of per-system towers.
No multiplication of the two amplitudes is licensed.

### 3.2 Required action carrier

DoR-015 V005 lines 90-124 type the finite physical scalar source as the
complete basis-free conserved family

```text
K_cycle,N := ker(B_N^T),
u_c(a) = <c,L_N a>,
c in K_cycle,N.
```

Individual open-edge scalars do not descend. V005 lines 268-270 further state
that on every tree stage

```text
ker(B_N^T) = {0};
```

tree phase content is Gate-4 gauge. Across stages, the completed physical
cycle source is generated from the directed family of these kernels. The
draft's target is consequently in a function class such as

```text
phi : X_phys or K_cycle -> scalar action correction,
```

not a function on endpoint histories.

### 3.3 Type table

| Ratified object | Domain/carrier | Covariance | Can it directly fill the action determiner? |
|---|---|---|---|
| `(T_+,T_-)` | two open-path endpoint morphisms | independent branchwise endpoint covariance | **No**; wrong domain and no scalar |
| `R_CTP` | `End(E_s)` | common endpoint conjugation; adjoint under reality | **No**; wrong domain and no map to incidence cycles |
| `Z_N^CTP` | finite doubled histories | conjugation-invariant scalar after the DoR-009 trace | **No**; scalar codomain matches, but domain does not |
| `P_(i,k)` | finite network-fed trace sequence | identity extension and batching compatible | **Partial input only**; exact multiplicative accumulation, not an action functional |
| `F_(i,k), A_(i,k)` | one receiver's charged-projector/tower carrier | reality and finite restrictions inherited | **No**; no cycle argument or action comparison square |
| ordered tower pair | product of the two per-system tower objects | node exchange permutes entries | **No**; no joint contraction and no scalar action |
| `phi_div` target | `X_phys` or `K_cycle` | quotient-defined, reality-covariant action | target remains unbuilt |

The scalar codomain of `Z_N^CTP` does not repair the mismatch. A scalar-valued
function on open-path histories and a scalar-valued functional on conserved
incidence cycles are different typed objects.

### 3.4 Eight-field bridge after DoR-016

| Draft field | Standing after DoR-016 | Reason |
|---|---|---|
| `DivergenceDatum` | `TYPE-U` | `Z` and `A` are finite trace/amplitude data, not a certified divergence coefficient or action |
| `DepthMap` | **partial `TYPE-P`** | tiered neighboring histories now feed an exact receiver tower; no identification with shell/spectral depth is made |
| `CycleMap` | `TYPE-U`, direct candidate `TYPE-R` | no map to `X_phys/K_cycle`; the one-edge test below refutes direct factorization |
| `AccumulationRule` | **partial `TYPE-P`** | `P_(i,k)=product_t Z_(i,t)` is exact and finite; no subtraction, action normalization, or completion topology is supplied |
| `ActionComparisonSquare` | `TYPE-U` | no trace/tower-to-physical-action square exists |
| generator/uniqueness | `NO_VERDICT` | no action member is generated |
| form certificates | partial only | CTP reality and finite restrictions hold; `Flat(S)`, off-section content, and action quotient do not |
| provenance | partial only | common origin reaches the finite trace/tower, not the physical action |

```text
SEAM_FULLY_TYPES = false | TYPE-R
FINITE_NETWORK_ACCUMULATION_INPUT = DETERMINED | TYPE-P |
  premises: DoR-009, DoR-015, DoR-016
PHYSICAL_CYCLE_ACTION_FUNCTIONAL = NOT_BUILT / TYPE-U
D2 = COMPLETE
```

## 4. D3 -- maximal determination that is now lawful

The full seam does not type, so no `phi_div` is constructed. Nevertheless,
DoR-016 determines a strictly larger upstream subpackage than the old draft
possessed.

For each receiving system `i` and finite tier `k`, define only the already
ratified quantities

```text
NetAcc_(i,k)[h]
  := product_(t=1)^k product_(j=1)^(N_(i,t))
       conjugate(z_(-,i,t,j)^n) z_(+,i,t,j)^n,

A_(i,k)[h]
  := (1-p_i) + p_i NetAcc_(i,k)[h].
```

These formulas are exact, symbolic, and family-wide:

```text
p_i remains symbolic;
the faithful character family is not reduced to a chosen orientation;
no endpoint frame is selected;
no filtration member is selected;
no joint network contraction is formed.
```

Identity delivery adds a factor one. Coarse-versus-refined CTP batching is
invariant by exact composition and character multiplicativity. Thus
`NetAcc_(i,k)` is a genuine stage-compatible finite network datum.

What DoR-016 does not determine is any of

```text
phi_div([a]) for [a] in X_phys,
phi_div(c) for c in K_cycle,
D_C D_K phi_div,
D_C(delta phi_div),
the additive/logarithmic branch of NetAcc,
a completed action topology,
a unique member of the flat transverse action family.
```

Taking a logarithm would add branch and domain data not contained in DoR-016.
Calling `A_(i,k)` an action would add the missing action comparison square by
name only.

```text
NEWLY_DETERMINED = finite network-fed CTP multiplicative accumulation
STILL_FREE = complete transverse cycle-action residue
D3 = MAXIMAL_LAWFUL_SUBPACKAGE_ONLY
```

## 5. D4 -- exact mismatch and the door

### 5.1 Why the existing doors do not silently solve it

Three existing DoR-016 doors are adjacent:

1. **Door 1, Branch-B scalarization.** Required only for a route that first
   converts endpoint access into V007's scalar source port. It is unbuilt and
   cannot be bypassed by renaming `Z_N^CTP` as a source.
2. **Door 4, joint two-system contraction.** Required if one wants one scalar
   from the ordered pair of per-system towers. A per-system action route need
   not use it, so it is not the universal first blocker.
3. **Door 5, completed physical contraction.** Required before a finite trace
   can become a completed physical state/effect object. It remains necessary,
   but even a completed contraction would not by itself define an incidence-
   cycle action functional.

The determination therefore waits on a new door, whose absence was already
the draft's `CycleMap + ActionComparisonSquare` residue.

### 5.2 New Door 7

```text
DOOR_7_NETWORK_CTP_TOWER_TO_TRANSVERSE_CYCLE_ACTION_DESCENT := (
  domain:
    the full no-selection family of finite doubled network histories,
    their R_CTP endomorphisms, and their DoR-009 traces/towers;

  codomain:
    a scalar action functional on X_phys or K_cycle;

  required factorization:
    endpoint-covariant history
      -> finite CTP trace/tower
      -> DoR-015 path-visible quotient and conserved cycle carrier
      -> transverse physical action;

  certificates:
    annihilates tree/open-path gauge content,
    preserves every record-visible cycle,
    family-natural with no frame/orientation/filtration selection,
    U1 reality-covariant,
    identity-zero-extension and CTP-batching compatible,
    stage-restriction compatible,
    action normalization and any logarithm branch declared,
    completion topology and Door-5 use declared,
    no joint contraction unless Door 4 is separately opened,
    common-origin provenance,
    generator/uniqueness or an explicit unselected residual family
).
```

This is a new interface, not content already hidden in the six doors.
Door 5 is a prerequisite for its completed version; Door 7 is the actual
cycle-action descent.

```text
ACTION_DETERMINER_BLOCKER = DOOR_7 | TYPE-U
DOOR_5_STATUS = NECESSARY_PREREQUISITE / TYPE-U
DOOR_4_STATUS = CONDITIONAL_ON_JOINT_ACTION_ROUTE / TYPE-U
DOOR_1_STATUS = CONDITIONAL_ON_SOURCE_PORT_ROUTE / TYPE-U
D4 = COMPLETE
```

## 6. D5 -- finite falsifier, executed

### 6.1 Test construction

Take the finite connected graph with one oriented edge `e:s->t`. DoR-015
gives

```text
K_cycle,1 = ker(B_1^T) = {0}.
```

Choose a symbolic admitted Branch-B open-path history

```text
T_-[h_e] = I,
T_+[h_e] = exp(i epsilon),
epsilon != 0 symbolically.
```

No numerical value is selected. For either retained faithful character
orientation `n`,

```text
R_CTP[h_e] = exp(i epsilon),
Z_1^CTP[h_e] = exp(i n epsilon),
A_1[h_e] = (1-p) + p exp(i n epsilon).
```

At identity history,

```text
R_CTP[I] = I,
Z_1^CTP[I] = 1,
A_1[I] = 1.
```

The two histories have the same physical incidence-cycle argument because
that argument space is the singleton `{0}`, but their DoR-016 finite trace
and tower values differ generically.

### 6.2 Factorization contradiction

If the ratified trace or tower directly determined a functional on
`K_cycle,1`, there would be maps `q` and `Phi` such that

```text
NetAcc = Phi compose q,
q(h_e)=q(I)=0.
```

Then `NetAcc(h_e)=NetAcc(I)` would follow. The exact values above refute that
equality. Therefore neither `Z_1^CTP` nor `A_1` factors through the physical
cycle carrier.

This does not falsify DoR-016. DoR-016 deliberately types the nontrivial
one-edge result as open-path access and forbids promoting it to a scalar cycle
source. The test falsifies only the attempted direct seam from the ratified
network law to the transverse cycle action.

```text
FINITE_TEST = ONE_EDGE_OPEN_PATH_VERSUS_ZERO_CYCLE_CARRIER
FINITE_TEST_EXECUTED = true
DIRECT_TRACE_TO_K_CYCLE_FACTORIZATION = REFUTED | TYPE-R
DOR016_ONE_EDGE_REGRESSION = PASS
DOOR_7_NECESSITY = CONFIRMED
D5 = COMPLETE
```

## 7. D6 -- fence and scope scan

No barred act was performed.

```text
alpha evaluated                         false | TYPE-S
K_* or any root evaluated               false | TYPE-S
physical response value evaluated       false | TYPE-S
measured constant consulted             false | TYPE-S
rank or rank ratio selected             false | TYPE-S
orientation member selected             false | TYPE-S
endpoint frame selected                 false | TYPE-S
filtration member selected              false | TYPE-S
joint contraction selected              false | TYPE-S
action/log branch selected               false | TYPE-S
weak-* or bidual completion invoked      false | TYPE-S
register, plan, tracker, git changed     false | TYPE-S

FENCE_BLOCKED_STRUCTURAL_RESULT = false
D6 = PASS
```

## 8. Typed conclusion

DoR-016 does real work: it replaces the old absence of a network-fed finite
accumulation with one exact object, `NetAcc_(i,k)`, and fixes its covariance,
reality, restriction, batching, and symbolic-`p` behavior. That is the maximal
new determination.

It does not fix the transverse action's determining principle. The ratified
law lives on open-path endpoint access; the physical transverse action lives
on the quotient incidence-cycle carrier. The finite one-edge computation
proves these cannot be identified directly. A new Door 7 must supply the
descent and action comparison, with Door 5 explicitly accounted if a
completed physical contraction is used.

```text
LEAD_RESULT = BLOCKED_ON_DOOR_7_NETWORK_CTP_TOWER_TO_TRANSVERSE_CYCLE_ACTION_DESCENT

FINITE_NETWORK_INPUT = DETERMINED
TRANSVERSE_ACTION_DETERMINER = NOT_DETERMINED / TYPE-U
DIRECT_IDENTIFICATION = REFUTED / TYPE-R
FALSIFIER_OUTCOME = DIRECT_SEAM_FAILS; DOR016_PASSES

Q408_DELTA_M_EXECUTED = false | TYPE-U
Q408_DELTA_G_K_EXECUTED = false | TYPE-U
PI_R_IND_EXECUTED = false | TYPE-U
PHYSICAL_P_VERDICT = NO_VERDICT

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
