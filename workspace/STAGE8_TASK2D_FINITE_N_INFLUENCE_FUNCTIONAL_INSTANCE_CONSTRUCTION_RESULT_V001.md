# Stage 8 Task 2d Finite-N Influence-Functional Instance Construction Result v001

Date: 2026-08-01

## 0. Verdict

The existing exact finite source-record transition does compose with its ready
record input into one exact finite object:

```text
I_N(a_+,a_-)
  := <R_N|(V_(a_-)^(N))^dagger V_(a_+)^(N)|R_N>,

a_+,a_- in {0,ch},
N >= 1.
```

It is the normalized doubled branch-overlap kernel for the finite
neutral/charged endpoint histories. Exact evaluation gives

```text
I_N = [[1,0],
       [0,1]]
```

for every `N >= 1`. Its associated reduced source channel is

```text
Phi_N(rho)
  = P_0 rho P_0 + P_ch rho P_ch.
```

This is an exact finite source-record influence/decoherence kernel in operator
form. It is not an instance of the requested source/field functional
`F_N[J_+,J_-]`, and it is not `DynPort_U2_008`. The corpus supplies no
source-history-dependent finite dynamics `J or A -> U_N[J or A]`; the ratified
`C0_008` module supplies no scalar state, trace, or admitted record effect; and
no common-origin map joins the exact finite endpoint dynamics to the `C0_008`
field/CTP carrier.

The one-cell falsifier splits by object type:

```text
untraced N=1 dilation reproduces the sealed one-cell transition = PASS
traced I_1 reproduces that transition                         = INAPPLICABLE
I_1 equals the continuous probability F_R(theta)              = REFUTED_BY_TYPE
```

Tracing out the record cannot be required to reproduce the record transition
that it discards. `F_R(theta)=cos^2(theta/2)` is a continuously parameterized
probability-level observable; `I_1` is a fixed discrete branch-overlap kernel.
The sealed corpus supplies no map identifying their arguments or codomains.

Therefore the exact narrow construction is retained, but the four full-CTP
fronts named in the relay do not open.

```text
FINITE_NEUTRAL_CHARGED_BRANCH_OVERLAP_KERNEL_CONSTRUCTED = true
FINITE_REDUCED_SOURCE_CHANNEL_CONSTRUCTED = true
FINITE_KERNEL_SEQUENTIALLY_COMPATIBLE_FOR_N_GE_1 = true

SOURCE_FIELD_INFLUENCE_FUNCTIONAL_F_N_J_PLUS_J_MINUS_CONSTRUCTED = false |
  TYPE-U |
  would-build: one common-origin family U_N[J,A,g] on the completed scalar
               source-record-field carrier, with StatePort, EffectPort,
               contact/domain data, and a certified finite-to-C0 descent

DYNPORT_U2_008_PHYSICAL_INSTANCE_EXISTS = false | TYPE-U |
  would-build: the complete source-history-dependent construction above and
               its U1/CTP, normalization, covariance, and provenance certificates

FENCE_BLOCKED_STRUCTURAL_RESULT = false
MACHINERY_APPEAL = NOT_TRIGGERED

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Preflight, scope, and authority

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = SPLIT
  exact finite endpoint dynamics and ready inputs exist;
  the full source/field influence-functional instance does not

IS_THE_VERSION_CURRENT = true
  register read through Q-226; no later ruling was consulted

ARE_THE_INPUTS_PRESENT = PARTIAL
  present: exact finite transition, finite ready record state, ratified CTP
           branch embeddings, sequential finite record embeddings
  absent: source-history dependence, scalar C0 state/trace/effects,
          finite-to-C0 common-origin descent
```

### 1.2 Roots entered

The search entered:

```text
/Users/bgm/MB Work/alpha_supervision
/Users/bgm/Documents/New project/gravity_emergence_evidence_program
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
```

The search excluded `a32_holdout/custodian_private/` absolutely. It did not
open, parse, list, summarize, or quote that path or anything below it.

Queries included word-boundaried and case-insensitive searches for:

```text
finite transition, charged incidence, outgoing GNS, U_N, W_N, rho_N,
ready, partial trace, trace out, influence, CTP, A_+, A_-, J_+, J_-,
U_BR, E_r, effect, source map, s_J, s_R, StatePort, EffectPort, DynPort,
Gen_C0, G_joint, F_R, cos^2, one-cell, sequential, inclusion, zero-extension
```

Searches over the exact finite-transition and outgoing-record-GNS producers
returned no occurrence of `A_+`, `A_-`, `J_+`, `J_-`, `U_BR`, `influence`,
`CTP`, or an admitted physical record effect.

### 1.3 Frozen authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_SPEC_V002.md` | `4a7600caa23d0c7a98eeef8a79941c20ca4e28a4f5a2c1cf5c2362e88c7d4721` | Finite transition grammar and continuous-parent boundary |
| `R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_RESULT_V002.md` | `2be95d5b58ea000df9a30b717a809374a90693f78a893d87b73a12e4be97fa21` | Exact endpoint unitary and arbitrary-N product |
| `R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md` | `10909b5c21e73ecf655462339a27bd645b8d35e3ad11fb6f8cb204c601992995` | Sequential record compatibility and record-only scope |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md` | `1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6` | Ratified C0 branch embeddings and source-map interface |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` | `2b6291227b7ac5967796014c2ad217c9eb084b5bb6df23fed0a7bca464e8bfab` | State/effect/dynamics port boundaries |
| `STAGE8_TASK2D_MULTIAXIAL_STATE_TRANSITION_ENVELOPE_SPECIFICATION_V001.md` | `bda00e99e964bd75d60429549e5f6c70762bf1607270b9a6294dc4c97cf2c635` | Q-226 four-consumer gap and path certificate |
| `primitive_complete_boundary_transition_functional_principle_v002.md` | `be79ca5e08010b53285cd157ba4c18d2029f08bc93bea2db02d5423b67428c34` | Full normalized CTP target |
| `ONE_CELL_FIDELITY_ACTION_SELECTOR_GATE_V001.md` | `84ab5b01a5279037cee85e4f9e7616b6bdea9bcec2bf53275d35a04683e463b8` | One-cell probability observable and object-type warning |
| Decision of Record 008 | `d51a6d5c5bb0020a081cfd2adfb545b9f5ed86ce660d3feacadc5ef68140fb19` | Premise standing for the ratified field/CTP presentation |

## 2. Existing exact finite dynamics

The finite producer derives, rather than inserts, the one-cell endpoint action
(`R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_RESULT_V002.md:13-46`):

```text
S = [[0,1,0],
     [1,0,0],
     [0,0,-1]],

S|r>   = |p_Q>,
S|p_Q> = |r>,
S|e_Q> = -|e_Q>.
```

Let

```text
P_0  = I-P_ch,
V_0^(N)  = I_R_N,
V_ch^(N) = S_N := tensor_(j=1)^N S_j,
|R_N>    = |r>^tensor_N,
|P_N>    = |p_Q>^tensor_N.
```

The arbitrary-N endpoint unitary is the exact analytic result at
`R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_RESULT_V002.md:48-84`:

```text
U_N = P_0 tensor I_R_N + P_ch tensor S_N.
```

Its finite ready-input output for charge-superselected source states is

```text
rho_N
  = P_0 rho_S P_0 tensor |R_N><R_N|
    + P_ch rho_S P_ch tensor |P_N><P_N|.
```

The exact transition is conditional on the declared causal-support branch; it
does not derive the complete continuous parent dynamics
(`R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_RESULT_V002.md:108-167`).

## 3. Exact doubled finite kernel

### 3.1 Definition from existing instances

For the two finite endpoint history labels `a_+,a_- in {0,ch}`, take one
forward copy and one opposite-backward copy of the same exact endpoint map.
Tracing the complete finite record carrier in the ready state gives

```text
I_N(a_+,a_-)
  := Tr_R_N[
       V_(a_+)^(N) |R_N><R_N| (V_(a_-)^(N))^dagger
     ]

   = <R_N|(V_(a_-)^(N))^dagger V_(a_+)^(N)|R_N>.
```

This trace is canonical on the finite matrix algebra `R_N`; it does not import
a trace onto the ratified Hilbert C-star-module `C0_008`.

Calling the two copies forward/backward uses the ratified CTP branch grammar:

```text
FINITE_BRANCH_DOUBLING_TYPED = true | TYPE-P | premises: DoR-008
```

The matrix evaluation itself follows from the derived finite unitary and
finite matrix trace, independent of any field/CTP scalarization.

### 3.2 Exact evaluation at N=1

With `|r>=(1,0,0)^T`,

```text
S|r> = |p_Q> = (0,1,0)^T,
<r|p_Q> = 0.
```

Hence

```text
I_1(0,0)   = 1,
I_1(ch,ch) = 1,
I_1(0,ch)  = I_1(ch,0) = 0,

I_1 = [[1,0],
       [0,1]].
```

### 3.3 Exact evaluation at N=2

At two cells,

```text
S_2|R_2> = (S|r>) tensor (S|r>) = |P_2>,
<R_2|P_2> = <r|p_Q>^2 = 0.
```

Therefore

```text
I_2 = [[1,0],
       [0,1]].
```

An independent exact-integer matrix evaluation returned:

```text
N = 1  kernel = ((1,0),(0,1))  offdiag = 0
N = 2  kernel = ((1,0),(0,1))  offdiag = 0
```

No floating-point tolerance enters this result.

### 3.4 Arbitrary N and the reduced source channel

For every `N>=1`,

```text
S_N|R_N> = |P_N>,
<R_N|P_N> = product_(j=1)^N <r|p_Q> = 0.
```

Thus `I_N=delta_(a_+,a_-)` exactly. The channel obtained by tracing the
record carrier is

```text
Phi_N(rho)
  = Tr_R_N[U_N(rho tensor |R_N><R_N|)U_N^dagger]
  = sum_(a,b in {0,ch}) I_N(a,b) P_a rho P_b
  = P_0 rho P_0 + P_ch rho P_ch.
```

On the sealed charge-superselected input class this reduces to
`Phi_N(rho_S)=rho_S`. The last equality is not absence of a record write; it is
the consequence of tracing out a record that perfectly distinguishes the two
declared charge-history classes.

The extension of `Phi_N` to source states with neutral/charged coherence is a
structural channel calculation on the derived unitary. Such coherent inputs
are not admitted as physical inputs by the finite specification
(`R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_SPEC_V002.md:52-53,139-150`).

## 4. Provenance trace

The narrow construction has one frozen trace:

```text
B_ch and tau_R
  -> exact one-cell endpoint S
  -> exact controlled U_1
  -> edge-local product U_N
  -> ready finite record vector |R_N>
  -> doubled endpoint pair (U_N,U_N^dagger)
  -> finite record trace
  -> I_N and Phi_N.
```

The antecedent status is mixed:

| Part | Standing |
|---|---|
| Endpoint matrix `S` and controlled `U_N` | Derived inside the declared primitive pure-charge, vacuum-plus-one-source, single-incidence branch |
| Causal one-use support of the complete parent | Not derived; the finite result is conditional on it |
| Forward/backward labeling | `TYPE-P | premises: DoR-008` |
| Finite matrix trace and overlap evaluation | Structural mathematics on instantiated finite matrix carriers |
| Field/source histories `J,A,g` | Not present in the finite producer |
| Scalar C0 state, trace, effects, dynamics | Not present |

This is common origin for `I_N` and `Phi_N` only. It is not the path-level
common-origin witness required by Q-226 for the completed source-record-field
object.

```text
FINITE_KERNEL_COMMON_ORIGIN_TRACE_CERTIFIED = true

FULL_C0_PATH_COMMON_ORIGIN_CERTIFIED = false | TYPE-U |
  would-build: d_state, d_effect, d_domain, d_dynamics, finite descent maps,
               and the commuting PathCert squares on the same parent object
```

## 5. Sequential compatibility

The outgoing record theorem uses

```text
R_N = tensor_(j=1)^N M_3(C),
iota_NM(A)=A tensor I_(M-N),
```

and proves exact record-state compatibility
(`R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md:25-75`).

For the narrow kernels, adding ready cells and applying the same exact
charge-controlled write gives

```text
I_M(a,b)
  = I_N(a,b)
    product_(j=N+1)^M <r|V_b^dagger V_a|r>
  = delta_(a,b)
  = I_N(a,b),
```

for all `M>=N>=1`. Therefore `{I_N}_{N>=1}` and `{Phi_N}_{N>=1}` are exact
constant compatible families under the finite record-cell inclusions.

This result does not prove compatibility under the ratified field-label
inclusions `Lambda_N -> Lambda_M`. No map sends those field labels or the
finite-support source maps `s_J,s_R` to the finite incidence transition.

```text
FINITE_RECORD_CELL_KERNEL_COMPATIBILITY = true

C0_FIELD_LABEL_TO_FINITE_DYNAMICS_COMPATIBILITY = false | TYPE-U |
  would-build: a canonical common-origin map from Gen_C0 and the physical
               source histories to the finite controlled transition family
```

## 6. Why this is not `F_N[J_+,J_-]`

The complete target is

```text
Z_r[A_+,g_+;A_-,g_-]
  = Tr(E_r U_BR[A_+,g_+] rho_pre U_BR[A_-,g_-]^dagger)
    / Tr(E_r U_BR[0,g_0] rho_pre U_BR[0,g_0]^dagger),
Gamma_r = -i log Z_r.
```

It is sealed as architecture at
`primitive_complete_boundary_transition_functional_principle_v002.md:16-35`
and as the DynPort output at
`STAGE8_TASK2D_MULTIAXIAL_STATE_TRANSITION_ENVELOPE_SPECIFICATION_V001.md:453-488`.

Three independent type gaps prevent promotion of `I_N` to that object.

### 6.1 No source-history-dependent finite family

The finite producer supplies one fixed endpoint unitary, not a family
`U_N[J_+,A_+,g_+]`. Neither `J`, `A`, nor `g` occurs in its specification or
result. The ratified maps `s_J,s_R` land in bounded adjointable C0 operators,
but no dynamics consumes their outputs
(`STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md:223-265`).

The symbol roles are kept separate. `G_joint` is the already ratified `U(1)`
comparison group. It is not the response-generator interface. Q-226 names
`Gen_C0` only inside a hypothetical future completed-state predicate and marks
the response map absent
(`STAGE8_TASK2D_MULTIAXIAL_STATE_TRANSITION_ENVELOPE_SPECIFICATION_V001.md:593-619`).
No instantiated `Gen_C0` connects `s_J,s_R` to `U_N`.

Declaring the fixed `I_N` constant in `J` would be a new uncoupled dynamics
choice. It would preassign a zero field response and would not descend from the
finite incidence producer.

```text
SOURCE_HISTORY_TO_FINITE_UNITARY_MAP_EXISTS = false | TYPE-S |
  roots: finite transition spec/result, outgoing GNS result, C0 assembly,
         U2 partial assembly, Q-226 envelope
  exclusions: a32_holdout/custodian_private/, superseded v001 transition
  fences: no physical-value evaluation; no post-output supplementation
  query: word-boundaried searches for J_+, J_-, A_+, A_-, U_BR, source map,
         contact, influence, CTP, and dynamics

SOURCE_HISTORY_DEPENDENT_FINITE_DYNAMICS_CONSTRUCTED = false | TYPE-U |
  would-build: an instantiated action/evolution consuming the certified C0
               source maps on a common physical scalar domain
```

### 6.2 No scalar C0 state, trace, or effect port

`C0_008` is a Hilbert C-star-module. It intentionally exports no positive
functional `B->C`, scalar Hilbert realization, density operator, or trace.
The U2 determination records StatePort and nontrivial EffectPort as
uninstantiated. The finite matrix trace used in Section 3 cannot be transported
to C0 by name.

```text
SCALAR_C0_TRACE_FOR_DYNPORT_EXISTS = false | TYPE-U |
  would-build: StatePort_U2_008, including omega_phys, H_omega, rho_pre,
               trace, state domain, descent map, and provenance certificate

ADMITTED_RECORD_EFFECT_PORT_INSTANCE_EXISTS = false | TYPE-U |
  would-build: concrete effects on the same scalar realization with domains,
               completeness where claimed, and common-origin provenance
```

### 6.3 No common-origin finite-to-C0 dynamics descent

The exact finite dynamics acts on the finite source-record carrier. The
ratified C0 object adds the field/CTP algebra as a module presentation. No
artifact maps the former dynamics to an action on the latter, and the
outgoing GNS theorem is explicitly record-only
(`R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md:157-170`).

```text
FINITE_DYNAMICS_TO_C0_DESCENT_EXISTS = false | TYPE-U |
  would-build: d_dynamics from one parent object, a certified scalar C0 action,
               compatible finite restrictions, and the Q-226 PathCert squares
```

### 6.4 Logarithm and differentiability

The exact discrete kernel has zero off-diagonal entries. There is no supplied
nonzero differentiable neighborhood connecting its two charge-history labels,
so `-i log I_N` is not a completed local response functional. A continuous
interpolation of the endpoint pulse would be a new dynamics family; the finite
result expressly does not derive the complete continuous parent.

```text
FINITE_KERNEL_LOG0_RESPONSE_NEIGHBORHOOD_EXISTS = false | TYPE-U |
  would-build: a source-history-dependent nonzero neighborhood with a fixed
               logarithm branch and certified contacts/domains
```

## 7. One-cell falsifier adjudication

### 7.1 Untraced restriction

At `N=1`, the dilation is exactly

```text
U_1 = P_0 tensor I + P_ch tensor S.
```

This is the sealed derived one-cell record transition itself. Therefore:

```text
UNTRACED_ONE_CELL_TRANSITION_RESTRICTION = PASS
```

No disagreement with DoR-008 or the finite authority is found at this level.

### 7.2 Traced kernel versus the transition

`I_1` and `Phi_1` are produced only after the record carrier is traced out.
They cannot reproduce the record pointer output because that output is no
longer in their codomain. Requiring them to do so is an object-type mismatch,
not a failed physical prediction.

```text
TRACED_KERNEL_MUST_REPRODUCE_UNTRACED_RECORD_OUTPUT = false | TYPE-R |
  test: compare codomains before and after the stipulated record trace
```

### 7.3 Traced kernel versus `F_R(theta)`

The one-cell selector gate states at
`ONE_CELL_FIDELITY_ACTION_SELECTOR_GATE_V001.md:97-111` that
`F_R(theta)=cos^2(theta/2)` is a probability-level reference-preservation
quantity and does not by itself distinguish a single amplitude, doubled CTP
influence action, noise kernel, or real unitary kinetic action.

The gate retains it only as a possible diagonal probability observable of a
later complete CTP theory and requires one complete parent transition kernel
to reopen the route (`:118-152`).

The present exact finite kernel does not supply a `theta` or source-history
argument, and `I_1` is matrix-valued on `{0,ch}^2`, not a scalar function of a
continuous phase. Thus:

```text
I_1_IDENTIFIED_WITH_F_R_THETA = false | TYPE-R |
  test: compare domain, codomain, and supplied parameter maps

SEALED_MAP_FROM_FINITE_ENDPOINT_LABELS_TO_THETA_EXISTS = false | TYPE-S |
  roots: one-cell fidelity gate, finite transition spec/result, Q-226 envelope
  exclusions: a32_holdout/custodian_private/, fitted endpoint identifications
  fences: no coupling or response evaluation
  query: word-boundaried searches for F_R, theta, charged incidence, endpoint,
         U_N, influence, CTP, and parent transition
```

The relay's one-cell falsifier therefore passes only at the untraced dilation
level. It yields `NO_VERDICT` on the full `F_N[J_+,J_-]`, because that object is
unbuilt, and it refutes an identification of the traced discrete kernel with
the continuous one-cell fidelity function.

## 8. Consumer consequences

The exact narrow object can be consumed only as:

```text
one finite endpoint charge-history overlap kernel;
one finite reduced source channel;
one exact compatible family under record-cell extension.
```

It does not instantiate:

```text
U2 DynPort's source/field dynamics port;
Task 3a's complete Lorentzian influence-functional instance;
Task 3c's completed state family;
or the multiaxial envelope's full common-origin dynamics edges.
```

Those consumers require the field/source-dependent scalar construction that
Sections 6.1-6.3 show absent.

```text
U2_DYNAMICS_PORT_OPENED = false | TYPE-U |
  would-build: full source/field DynPort instance

TASK3A_COMPLETE_INSTANCE_OPENED = false | TYPE-U |
  would-build: full normalized record-conditioned CTP functional

TASK3C_COMPLETED_FAMILY_OPENED = false | TYPE-U |
  would-build: compatible completed source-record-field state/evolution family

MULTIAXIAL_ENVELOPE_FULL_DYNAMICS_EDGES_OPENED = false | TYPE-U |
  would-build: completed dynamics edges with common-origin provenance
```

These are object absences, not relay-fence blocks. No `MACHINERY-APPEAL` is
available or needed.

## 9. Final status block

```text
FINITE_NEUTRAL_CHARGED_BRANCH_OVERLAP_KERNEL_CONSTRUCTED = true
FINITE_REDUCED_SOURCE_CHANNEL_CONSTRUCTED = true
FINITE_N1_EXACT_MATRIX_CHECK = PASS
FINITE_N2_EXACT_MATRIX_CHECK = PASS
FINITE_ARBITRARY_N_ANALYTIC_CHECK = PASS
FINITE_N_GE_1_SEQUENTIAL_COMPATIBILITY = PASS
FINITE_COMMON_ORIGIN_TRACE = PASS
UNTRACED_ONE_CELL_RESTRICTION = PASS

SOURCE_FIELD_INFLUENCE_FUNCTIONAL_INSTANCE = NO_VERDICT |
  reason: the required physical object is unbuilt; the exact narrow kernel does
          not have its history-dependent domain, scalar C0 codomain, or descent

DOUBLED_CTP_INFLUENCE_FUNCTIONAL_COMMON_ORIGIN_INSTANCE_EXISTS = false |
  TYPE-U |
  would-build: complete source-history-dependent DynPort_U2_008

ONE_CELL_FIDELITY_IDENTIFICATION = false | TYPE-R |
  test: domain/codomain/parameter-map comparison

FENCE_BLOCKED_STRUCTURAL_RESULT = false
MACHINERY_APPEAL = NOT_TRIGGERED

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
coupling_evaluation_authorized = false
production_authorized = false
```

## 10. Custody

This lane act creates this append-only result and its verified SHA-256 sidecar,
mirrors both to `alpha-program-archive/workspace/`, reports, and stops. It does
not register, commit, push, amend a ruling, or alter any existing artifact.
