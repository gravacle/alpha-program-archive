# Stage 8 Envelope Finite PathCert Dynamics Subtrace Construction v001

Date: 2026-08-01  
Lane: CODEX LANE 2  
Task: Task 2d  
Register head consulted: Q-237  
Standing: `TYPE-P | premises: DoR-008, DoR-009` wherever the ratified carrier
or source-coupled transition law is consumed

## 0. Lead determination

**The envelope now has an exact certified finite lower-row path for every
finite `N`.** The ratified source-coupled law maps the ready source-record node
to the completed finite node; record restriction gives a compatible finite
outgoing functional; and those functionals embed isometrically into the sealed
outgoing record GNS limit:

```text
PathCert_N^dyn(rho_S,n,a):

rho_ready,N(rho_S)
  --U_N^(n)[a]-->
rho_N(rho_S)
  --Rec_N-->
(R_N,omega_N^(rho_S))
  --iota_N / J_N-->
(R_infinity,omega_out^(rho_S),GNS_out).
```

This is a finite dynamics/provenance **subtrace**, not the complete physical
`PathCert(Omega)`. All lower-row objects descend from one frozen finite input
tuple, but the physical source state is an admitted input rather than an
output of the ratified law. The subtrace therefore does not satisfy P5's
stronger derivational common-origin condition.

```text
FINITE_PATHCERT_DYNAMICS_SUBTRACE_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009
FINITE_LOWER_ROW_PATH_COMMUTES_FOR_ALL_N = true | TYPE-P |
  premises: DoR-008, DoR-009
FINITE_COMMON_CONSTRUCTION_TRACE_EXISTS = true | TYPE-P |
  premises: DoR-008, DoR-009 |
  scope: one frozen law/state/ready/history tuple and its finite descendants

FINITE_PHYSICAL_P5_COMMON_ORIGIN_WITNESS_EXISTS = false | TYPE-U |
  would-build: one microscopic trace descending state, law, effects, domains,
               and dynamics together rather than receiving rho_S as input
COMPLETE_ENVELOPE_PATHCERT_INSTANTIATED = false | TYPE-U |
  would-build: full C0 ports, restriction square, completed joint node, full
               outgoing node, and one P5 origin
```

The finite lower-row path family can now be declared before output inspection.
The original envelope protocol remains blocked on complete physical paths:

```text
FINITE_LOWER_ROW_PATH_FAMILY_DECLARABLE = true
COMPLETE_PHYSICAL_PATH_FAMILY_DECLARABLE_AT_STEP1 = false | TYPE-C |
  constraint: no complete upper-row path instance exists
FORCING_PROTOCOL_RUNNABLE_ON_COMPLETE_ENVELOPE = false | TYPE-C |
  constraint: step 1 requires instantiated complete physical path members
```

No second variation, kernel, `B_ind`, stiffness, transport map, coupling,
scale, or root is constructed or evaluated.

## 1. Preflight, currency, and authorities

### 1.1 Send-time preflight

```text
DOES_THE_OBJECT_EXIST = true
  Q-235 names the subtrace and supplies the clean finite-edge receipt
IS_THE_VERSION_CURRENT = true
  register head Q-237 was checked; DoR-010 is current but is not consumed by
  this non-variation construction
ARE_ITS_INPUTS_PRESENT = true
  envelope interfaces, U_N, ready states, finite completed states, record
  restrictions, and outgoing record GNS are instances
```

### 1.2 Authorities

| Authority | Content used |
|---|---|
| `STAGE8_TASK2D_MULTIAXIAL_STATE_TRANSITION_ENVELOPE_SPECIFICATION_V001.md:36-63` | lower-row graph and upper-row ceiling |
| same, `:274-352` | finite nodes and outgoing record node |
| same, `:393-430` | finite dynamics and record-limit edges |
| same, `:505-578` | full `PathCert` signature and squares |
| same, `:641-699` | protocol stop and build order |
| `STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md:135-218` | `U_N`, ready state, exact finite law |
| same, `:221-282`, `:382-404` | `N=1,2` and zero-extension |
| `R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_RESULT_V002.md:48-106` | completed states and compatibility |
| `R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md:25-100` | record limit, GNS, finite embeddings |
| same, `:157-183` | record-only ceiling |
| `PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md:15-88` | one-parent covariance and no-separate-selection |
| `STAGE8_P5_COMMON_ORIGIN_DESCENT_REQUIREMENT_V001.md:60-125` | derivational common-origin certificate |
| `STAGE8_RATIFIED_FINITE_N_INFLUENCE_FUNCTIONAL_FOUR_CONSUMER_HANDOFF_RECEIPTS_V001.md:389-466` | finite edge and named subtrace build |
| `STAGE8_SHARED_FINITE_STATE_EFFECT_CONDITIONED_AMPLITUDE_SHARP_STOP_V001.md:185-223` | exact `p_ch` quotient |
| `STAGE8_FINITE_P_CH_DEPENDENCE_AND_PHASE_RESIDUAL_TRANSPORT_DETERMINATION_V001.md:93-119` | Q-237 currency |

The cleanroom and archive supervision roots were entered. The private
custodian root was not entered. No register, baseline, or prior artifact was
edited.

Symbol distinctions bearing on this construction:

```text
a                  holonomy history, not a charge label
n in {+1,-1}       character orientation, not a CTP branch
omega_N            finite record restriction, not full rho_N
omega_out          record-only limit, not full outgoing rho
PathCert_N^dyn     finite lower-row subtrace, not full PathCert(Omega)
p_ch               record-visible charge weight, not complete rho_S
```

Queries used: `PathCert`, `d_dynamics`, `d_fin`, `E_finite`, `E_record`,
`Res_N`, `iota_NM`, `rho_ready`, `rho_N`, `omega_N`, `omega_out`, `GNS`,
`common-origin`, `zero-extension`, `one-cell`, `equal-history`, `p_ch`, and
`charge-superselected`. No corpus-wide absence claim is made.

## 2. Frozen finite input family

Define the exact admitted source family

```text
Sigma_src := {
  rho_S >= 0,
  Tr(rho_S)=1,
  rho_S=P_0 rho_S P_0+P_ch rho_S P_ch
}.

p_ch(rho_S):=Tr(P_ch rho_S),
Tr(P_0 rho_S)=1-p_ch.
```

`p_ch` is the exact quotient visible to the scalar influence and outgoing
record marginal. It is not the complete state: the finite completed node
retains `P_0 rho_S P_0` and `P_ch rho_S P_ch`.

```text
P_CH_IS_THE_ONLY_FREE_DATUM_OF_THE_FULL_FINITE_STATE_PATH = false | TYPE-R |
  test: rho_N retains full source blocks while p_ch retains their traces only
P_CH_IS_THE_ONLY_OUTGOING_RECORD_VISIBLE_SOURCE_DATUM = true
  scope: omega_N and omega_out
PHYSICAL_SOURCE_STATE_SELECTED = false | TYPE-U |
  would-build: StatePort/common-origin descent
```

This corrects the phrase “the path's one free datum”: it is one free
**record-visible scalar**. No sealed equivalence identifies all source states
with the same scalar.

For each `N>=1`, freeze before output:

```text
Hist_N^rat := {
  z=(z_1,...,z_N) in U(1)^N |
  z_j=chi_n(h_j[a_j]) for the ratified open-chain source placement
}.
```

The law depends on a background presentation `a` only through this concrete
holonomy-character tuple. Background presentations with the same tuple produce
the identical operator `U_N`; the family below can therefore be indexed by
`z in U(1)^N` without adding a history-selection rule.

```text
Omega_fin,N(rho_S,n,a) := (
  DoR-008 carrier/conventions,
  DoR-009 E_post law,
  rho_S in Sigma_src,
  |R_N><R_N|,
  n in {+1,-1},
  a in Hist_N^admitted,
  canonical iota_NM
).
```

This is one finite construction tuple. It is not one microscopic origin,
because `rho_S` and the law are independent inputs.

```text
FINITE_INPUT_TUPLE_FROZEN_PRE_OUTPUT = true | TYPE-P |
  premises: DoR-008, DoR-009
FINITE_INPUT_TUPLE_IS_A_DERIVATIONAL_P5_ROOT = false | TYPE-R |
  test: rho_S is received rather than descended from the law
```

## 3. General finite path

### 3.1 Ready and completed nodes

```text
R_N=tensor_(j=1)^N M_3(C),
|R_N>=|r>^(tensor N),
|P_N>=|p_Q>^(tensor N),

rho_ready,N=rho_S tensor |R_N><R_N|.
```

The ratified dynamics is

```text
W_(1,j)^(n)[a_j]=D_(n,j)[a_j]S_j,
W_N^(n)[a]=tensor_j W_(1,j)^(n)[a_j],

U_N^(n)[a]
 =P_0 tensor I_(3^N)+P_ch tensor W_N^(n)[a].
```

Set

```text
d_dynamics,N(Omega_fin)=U_N^(n)[a],
d_fin,N(Omega_fin)=Ad_(U_N^(n)[a])(rho_ready,N).
```

Since

```text
W_N^(n)[a]|R_N>=(product_j z_j^(n)[a_j])|P_N>
```

and each character has unit modulus, the phase cancels in the density:

```text
rho_N
 =P_0 rho_S P_0 tensor |R_N><R_N|
  +P_ch rho_S P_ch tensor |P_N><P_N|.            (1)
```

Thus the source-coupled law lands exactly on the sealed completed-state node.

```text
SOURCE_COUPLED_EDGE_LANDS_ON_SEALED_COMPLETED_NODE = true | TYPE-P |
  premises: DoR-008, DoR-009
HOLONOMY_PHASE_CHANGES_SINGLE_HISTORY_RECORD_DENSITY = false | TYPE-R |
  test: unit character cancels against its adjoint in equation (1)
```

The holonomy remains in the two-history operator `F_N`; it is retained in the
dynamics certificate even though the single-history density is phase-blind.

### 3.2 Finite outgoing-record stage

For `A in R_N`, define

```text
omega_N^(rho_S)(A)
 :=Tr[rho_N(I_src tensor A)]
  =(1-p_ch)<R_N|A|R_N>+p_ch<P_N|A|P_N>.          (2)

N_out,N^R(rho_S):=(R_N,omega_N^(rho_S)).
```

The arrow `Rec_N:rho_N->omega_N` is restriction to record observables, not
source-preserving time evolution.

```text
FINITE_OUTGOING_RECORD_STAGE_INSTANTIATED = true
FINITE_COMPLETED_TO_RECORD_STAGE_IS_DYNAMICAL_EVOLUTION = false | TYPE-R |
  test: Rec_N is observable restriction
RECORD_RESTRICTION_PRESERVES_FULL_SOURCE_STATE = false | TYPE-R |
  test: equation (2) retains rho_S only through p_ch
```

### 3.3 GNS stages and outgoing limit

For `N<=M`,

```text
iota_NM(A)=A tensor I_(M-N),
omega_M o iota_NM=omega_N.                       (3)
```

Standard finite GNS gives

```text
H_N=completion(R_N/N_omega_N),
pi_N(A)[B]=[AB],
Omega_N=[I],
J_NM[A]=[iota_NM(A)].
```

Equation (3) proves `J_NM` is isometric, and canonical embedding associativity
gives `J_ML J_NM=J_NL`. Their direct limit is the sealed record-only triple

```text
(pi_out,H_out,Omega_out)=GNS(R_infinity,omega_out),
omega_out o iota_N=omega_N.                      (4)
```

Finite GNS is imported standard mathematics applied to sealed matrix states;
it adds no physical state or selection.

```text
FINITE_GNS_STAGE_SYSTEM_INSTANTIATED = true
FINITE_GNS_EMBEDDINGS_ISOMETRIC = true
OUTGOING_RECORD_GNS_REACHED = true
OUTGOING_RECORD_GNS_IS_FULL_SOURCE_INCLUSIVE_GNS = false | TYPE-R |
  test: Rec_N removes the source and sealed authority withholds the full limit
```

## 4. Explicit paths at N=1 and N=2

### 4.1 One cell

```text
rho_ready,1=rho_S tensor |r><r|

 --Ad_(P_0 tensor I_3+P_ch tensor D_n[a_1]S)-->

rho_1
 =P_0 rho_S P_0 tensor |r><r|
  +P_ch rho_S P_ch tensor |p_Q><p_Q|

 --Rec_1-->

omega_1^(p)(A)
 =(1-p)<r|A|r>+p<p_Q|A|p_Q>

 --iota_1 / J_1-->

(R_infinity,omega_out^(p),GNS_out),

omega_out^(p)(iota_1(A))=omega_1^(p)(A).
```

### 4.2 Two cells

```text
rho_ready,2=rho_S tensor |r r><r r|

 --Ad_(P_0 tensor I_9+P_ch tensor
       (D_n[a_1]S tensor D_n[a_2]S))-->

rho_2
 =P_0 rho_S P_0 tensor |r r><r r|
  +P_ch rho_S P_ch tensor |p_Q p_Q><p_Q p_Q|

 --Rec_2-->

omega_2^(p)(A)
 =(1-p)<r r|A|r r>+p<p_Q p_Q|A|p_Q p_Q>

 --iota_2 / J_2-->

(R_infinity,omega_out^(p),GNS_out).
```

For `iota_12(A)=A tensor I_3`,

```text
omega_2^(p)(iota_12(A))=omega_1^(p)(A).
```

This is the first nontrivial whole-lower-row commuting square.

## 5. Emitted certificate

```text
PathCert_N^dyn(rho_S,n,a) := (
  Omega_fin,N,
  d_ready,N=rho_ready,N,
  d_dynamics,N=U_N^(n)[a],
  d_fin,N=Ad_(U_N^(n)[a])(rho_ready,N),
  d_record,N=Rec_N,
  omega_N,
  {iota_NM},{J_NM},
  d_out=omega_out,
  Cert_charge_superselection,
  Cert_ready_normalization,
  Cert_DoR009_law,
  Cert_one_cell,
  Cert_equal_history,
  Cert_zero_extension,
  Cert_record_restriction,
  Cert_GNS_isometry,
  Cert_target_independence,
  Cert_no_post_output_supplementation,
  FreeDatum_record_visible=p_ch,
  ScopeCeiling=record_only_outgoing
).
```

Absent full-PathCert fields are `d_state` from one microscopic origin,
`d_effect`, `d_domain`, physical `Res_N`, `E_joint`, `N_completed^C0`,
`E_out^C0`, `N_out^C0`, and their full-carrier certificates.

```text
PATHCERT_N_DYN_FIELDS_INSTANTIATED = true | TYPE-P |
  premises: DoR-008, DoR-009
COMPLETE_PATHCERT_FIELD_SET_INSTANTIATED = false | TYPE-U |
  missing: the full-carrier fields listed above
```

## 6. Failure-capable checks

### 6.1 One-cell falsifier

At `N=1`, zero history reduces at operator level to the sealed write `S`;
`rho_1` and `omega_1` are its exact sealed state restrictions.

```text
CERT_ONE_CELL = PASS | TYPE-P | premises: DoR-008, DoR-009
ONE_CELL_FALSIFIER_FIRES = false | TYPE-R |
  test: U_1, rho_1, and omega_1 reproduce the sealed objects
```

Verdict owner: `Cert_one_cell`.

### 6.2 Equal-history collapse

```text
<R_N|U_N[a]^dagger U_N[a]|R_N>=P_0+P_ch=I_src.
```

Every normalized `rho_S` gives scalar contraction one, and both branches land
on the same single-history density `rho_N`.

```text
CERT_EQUAL_HISTORY = PASS_FOR_ALL_RHO_S | TYPE-P |
  premises: DoR-008, DoR-009
EQUAL_HISTORY_CHECK_SELECTS_RHO_S_OR_P_CH = false | TYPE-R |
  test: every member of Sigma_src passes
```

Verdict owner: `Cert_equal_history`.

### 6.3 Whole-path zero-extension

Let `T_NM` trace the final `M-N` record factors after canonical addition of
ready cells and zero history on new factors. Then

```text
T_NM(rho_ready,M)=rho_ready,N,
T_NM(rho_M)=rho_N,
omega_M o iota_NM=omega_N,
J_ML J_NM=J_NL,
omega_out o iota_N=omega_N.
```

The same `rho_S`, hence the same `p_ch`, is carried throughout.

```text
CERT_WHOLE_PATH_ZERO_EXTENSION = PASS_FOR_ALL_N_LE_M | TYPE-P |
  premises: DoR-008, DoR-009
ZERO_EXTENSION_REQUIRES_POST_OUTPUT_STATE_SUPPLEMENT = false | TYPE-R |
  test: every datum is frozen in Omega_fin before output
```

Verdict owner: `Cert_zero_extension`.

### 6.4 Target independence

All `rho_S in Sigma_src`, both orientations, and all admitted finite histories
enter the family. No downstream output narrows it.

```text
CERT_TARGET_INDEPENDENCE = PASS
CERT_NO_POST_OUTPUT_SUPPLEMENTATION = PASS
TARGET_AWARE_OUTPUT_USED_TO_NARROW_PATH_FAMILY = false | TYPE-S |
  scope: family predicate and equations (1)-(4)
```

Verdict owners: `Cert_target_independence` and
`Cert_no_post_output_supplementation`.

### 6.5 Independent exact arithmetic control

A separately coded rational-arithmetic control used two nontrivial unit
Gaussian phases, checked phase cancellation at `N=1,2`, checked
`omega_2 o iota_12=omega_1` on an independently chosen record observable,
checked equal-history normalization, and exhibited two distinct diagonal
source densities with the same `p_ch`. All exact assertions passed.

```text
INDEPENDENT_EXACT_PATH_CONTROL = PASS
```

## 7. Adversarial attacks and ceiling

1. **Call the tuple one microscopic origin.** Refuted: P5 requires descent
   maps producing state, effects, domains, and dynamics; `Omega_fin` receives
   `rho_S` separately.
2. **Call `p_ch` the complete state path.** Refuted: two densities with the
   same charged trace give the same equation (2) but different source blocks
   in equation (1).
3. **Transport the record limit upward.** Refuted: `Rec_N` removes the source,
   while the upper row requires a completed source-record-field/CTP state.
4. **Identify dynamics paths by equal density output.** Refuted: the certificate
   retains `U_N^(n)[a]`; no step-2 equivalence identifies histories or
   orientations.

```text
FINITE_COMMON_CONSTRUCTION_IMPLIES_P5_COMMON_ORIGIN = false | TYPE-R
SAME_P_CH_IMPLIES_IDENTICAL_FULL_FINITE_STATE_PATH = false | TYPE-R
RECORD_ONLY_PATH_IS_THE_COMPLETE_UPPER_ROW_PATH = false | TYPE-R
IDENTICAL_RECORD_DENSITY_OUTPUT_IDENTIFIES_DYNAMICS_PATHS = false | TYPE-R
```

No attack breaks the finite lower-row path; the attacks establish its ceiling.

## 8. Forcing-protocol position

Declare before any forcing output:

```text
Family_fin^path := {
  PathCert_N^dyn(rho_S,n,a) |
  N>=1,
  rho_S in Sigma_src,
  n in {+1,-1},
  z in Hist_N^rat
}.
```

Every member is generated by exact maps and the membership predicate is
explicit. This is Q-200-compliant family instantiation, not schemas passed as
instances. At fixed `N` the family has continuum cardinality; countably many
`N` leave that cardinality unchanged. Its outgoing-record-state quotient is
`p_ch in [0,1]`. If durable correlation is imposed separately, the relevant
subfamily is `0<p_ch<1`; no interior value is selected.

```text
FINITE_PATH_STEP1_FAMILY_DECLARED = true
FINITE_PATH_FAMILY_CARDINALITY = CONTINUUM
FINITE_OUTGOING_RECORD_STATE_QUOTIENT_CARDINALITY = CONTINUUM
FINITE_PATH_STEP1_USES_INSTANTIATED_MEMBERS = true
```

A protocol expressly scoped to the finite lower row may now execute step 1.
This artifact does not execute steps 2-5. The original complete-envelope
protocol remains blocked by absent StatePort descent, physical `Res_N`, upper
joint nodes/edges, P5 origin, completed-carrier predicates, and full coverage.

```text
FINITE_LOWER_ROW_STEP1 = YES
COMPLETE_PHYSICAL_ENVELOPE_STEP1 = NO | TYPE-C
PROTOCOL_STEPS_2_THROUGH_5_EXECUTED_HERE = false | TYPE-S |
  scope: construction and step-1 declaration only
FULL_PATH_COVERAGE_PROVED = false | TYPE-U |
  would-build: upper-row instances and admitted-family coverage proof
```

## 9. Typed negative ledger

| Negative | Type | Basis / release |
|---|---|---|
| Finite physical P5 common-origin witness exists | `TYPE-U` | State/law/effects/domains not descended together |
| Complete envelope `PathCert` instantiated | `TYPE-U` | Upper-row fields absent |
| Complete physical path family declarable | `TYPE-C` | No complete path instance |
| Full forcing protocol runnable | `TYPE-C` | Step-1 prerequisite absent |
| `p_ch` is the only full-path datum | `TYPE-R` | Source blocks survive in `rho_N` |
| Physical source state selected | `TYPE-U` | StatePort/common origin absent |
| Frozen tuple is a P5 root | `TYPE-R` | State and law are independent inputs |
| Holonomy changes single-history density | `TYPE-R` | Unit phase cancels |
| Completed-to-record stage is evolution | `TYPE-R` | It is restriction |
| Record restriction preserves source state | `TYPE-R` | Only `p_ch` survives |
| Outgoing record GNS is source-inclusive | `TYPE-R` | Carrier/scope mismatch |
| Complete `PathCert` fields instantiated | `TYPE-U` | Full fields absent |
| One-cell falsifier fires | `TYPE-R` | Exact restriction passes |
| Equal-history check selects state/weight | `TYPE-R` | All states pass |
| Zero-extension needs later state data | `TYPE-R` | Frozen tuple restricts exactly |
| Target-aware output narrows family | `TYPE-S` | No output consumed |
| Finite construction implies P5 origin | `TYPE-R` | Descent mismatch |
| Same `p_ch` implies same full path | `TYPE-R` | Source blocks distinguish |
| Record-only path equals upper row | `TYPE-R` | Carrier mismatch |
| Same record density identifies dynamics | `TYPE-R` | `U_N` remains certificate data |
| Protocol steps 2-5 executed | `TYPE-S` | Outside scope |
| Full path coverage proved | `TYPE-U` | Upper-row family absent |
| Second variation taken | `TYPE-S` | Outside scope |
| Kernel, `B_ind`, stiffness, or transport built | `TYPE-S` | Outside scope |
| Coupling, scale, root, eigenvalue, or measured comparison produced | `TYPE-S` | Outside scope |

Only `TYPE-R` carries refutational content. `TYPE-U`, `TYPE-S`, and `TYPE-C`
are not physical no-go results.

## 10. Custody and terminal fences

This lane writes and seals this append-only artifact, verifies its sidecar,
mirrors only the artifact and sidecar, reports, and stops. It edits no register,
Decision of Record, prior artifact, or baseline, and runs no git or gate.

```text
alpha_computed = false [TERMINAL_FENCE_DECLARATION]
proof_authorized = false [TERMINAL_FENCE_DECLARATION]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION]
coupling_evaluation_authorized = false [TERMINAL_FENCE_DECLARATION]
production_authorized = false [TERMINAL_FENCE_DECLARATION]
SECOND_VARIATION_TAKEN = false | TYPE-S | scope: this artifact
RESPONSE_KERNEL_EXTRACTED = false | TYPE-S | scope: this artifact
B_IND_CONSTRUCTED = false | TYPE-S | scope: this artifact
STIFFNESS_EVALUATED = false | TYPE-S | scope: this artifact
TRANSPORT_MAP_BUILT = false | TYPE-S | scope: this artifact
```
