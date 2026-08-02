# Stage 8 Task 2d Source-History Map from Covariant Incidence — Derivation Adjudication v001

Date: 2026-08-01  
Lane: CODEX LANE 2  
Task: Task 2d — source-history map  
Register head at issue: Q-227

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Lead verdict

**Decorating the exact finite record transition with the Gate-4 `U(1)`
holonomy is a choice, not a theorem of Gate 4. The build therefore stops before
constructing `U_N[A]` or evaluating `F_N[A_+,A_-]`.**

Gate 4 derives a narrower and exact result. On its own incidence carrier, after
the edge parallel transport `U_e` and its character have already been supplied,
closure and normalization force the two incidence coefficients to coincide and
have unit modulus:

```text
D_(a,b),e x = i_t(a_e U_e x) - i_s(b_e x)
                         -> a_e=b_e, |a_e|=1 modulo vertex gauge.
```

The phrase **unit-weight covariant incidence** refers to the coefficient
`a_e=b_e=1` chosen as a representative of that normalized differential class.
It does **not** derive:

1. the `U(1)` character/charge with which the physical source transforms;
2. a map from the incidence-line transport `U_e:L_s->L_t` to the finite record
   swap `S:M_3(C)->M_3(C)` or the controlled transition
   `P_0 tensor I + P_ch tensor S`;
3. where the connection enters the actual Lorentzian generator; or
4. a common-origin dynamics family consuming the ratified source maps.

Those distinctions are explicit in the sealed sources:

- BID v011 introduces `rho_joint` and the associated line bundle as a
  **Common Total-Action Character Premise** before Gate 4
  (`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:194-239`).
- Gate 4's hostile family varies `(a_e,b_e)`, Hilbert forms, the `D_x`
  continuum, and residual phases; it does not vary the character representation
  or an attachment to the record transition
  (`30_GATE4_DIFFERENTIAL_UNIQUENESS_SPEC_V001.md:12-33`).
- The adopted Transport-Only principle, not Gate 4, states `q_primitive=1`
  and says expressly that gauge and Lorentz covariance do not imply this rule
  (`PRIMITIVE_TRANSPORT_ONLY_PHASE_COMPLETE_GENERATOR_PRINCIPLE_V001.md:3-7,15-37,62-75`).
- The premise ledger classifies the compact connection and unit-character
  transport as adopted/disclosed inputs, and identifies unit charge/minimality
  as underived (`01_PREMISE_LEDGER.md:10-40`).
- DoR-008's ratified carrier contains the entire integer character-label system
  `Lambda_N=Z^N` and bounded source maps, but no dynamics selecting one label or
  connecting those maps to the finite transition.

The decisive carrier mismatch is:

```text
Gate 4:  U_e : L_s -> L_t                  [incidence line transport]
Q-227:   S   : C^3 -> C^3                  [record endpoint swap]
Q-227:   U_N^0 = P_0 tensor I + P_ch tensor S_N
                                                 [fixed source-record unitary]
Target:  U_N[A,g,J]                        [history-dependent physical dynamics]
```

No sealed functor, intertwiner, or common-origin descent identifies these
objects. Covariance of the first does not decorate the other three by identity
transport.

```text
GATE4_NORMALIZED_INCIDENCE_CLASS_DERIVED = true | TYPE-P |
  premises: Common Total-Action Character Premise, Gate-3 forms, operational
            closure, one-record normalization, and the enumerated Gate-4 family

GATE4_UNIT_WEIGHT_IS_UNIT_CHARGE = false | TYPE-R |
  test: unit weight fixes |a_e| in D_(a,b); unit charge fixes the character
        acting through U_e or the physical source generator

UNIT_CHARACTER_DERIVED_BY_GATE4 = false | TYPE-R |
  test: U_e/rho_joint is fixed before the hostile family; Gate 4 never
        quantifies over alternative characters

FINITE_TRANSITION_HOLONOMY_DECORATION_DERIVED_BY_GATE4 = false | TYPE-R |
  test: compare carrier, domain, codomain, and the Gate-4 quantifier

MINIMAL_COUPLING_DERIVED_HERE = false | TYPE-R |
  test: the Transport-Only authority calls it an adopted principle and says
        covariance alone does not imply it

PROPOSED_DECORATION_STANDING = CHOICE

SOURCE_HISTORY_MAP_U_N_A_CONSTRUCTED = false | TYPE-U |
  would-build: a selected character plus an actual common-origin attachment
               from the C0 source maps/connection to the finite dynamics

BUILD_STEPS_1_THROUGH_4_EXECUTED = false | TYPE-C |
  constraint: the relay mandates a stop when the decoration is a choice

FENCE_BLOCKED_STRUCTURAL_RESULT = false
MACHINERY_APPEAL = NOT_TRIGGERED
```

This is not a no-go against a source-history map. It is a refutation of the
claim that Gate 4 already derives this particular map.

## 1. Preflight, currency, and authorities

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = SPLIT
  target U_N[J,A,g]: absent
  Gate-4 covariant incidence and Q-227 finite transition: present separately

IS_THE_VERSION_CURRENT = YES
  register checked at send-time through Q-227; no later row exists

ARE_ITS_INPUTS_PRESENT = NO_FOR_THE_PROPOSED_COMPOSITION
  present: each endpoint object separately
  absent: character selector and carrier-attachment/descent map between them
```

Under the locked preflight rule, the missing composition is the result. No
candidate history-dependent unitary is instantiated by choosing it.

### 1.2 Frozen authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `STAGE8_TASK2D_FINITE_N_INFLUENCE_FUNCTIONAL_INSTANCE_CONSTRUCTION_RESULT_V001.md` | `c49d31200460e96209375f06a7a655d343767695ef09805f1e396d1814833b6b` | Q-227 baseline and three missing inputs |
| `30_GATE4_DIFFERENTIAL_UNIQUENESS_SPEC_V001.md` | `2f9acdfee9c81d95e7a22944fac738f1e222ce98e6dfd08d89c32d818bda41a4` | Exact hostile family and constraints |
| `32_GATE4_DIFFERENTIAL_UNIQUENESS_RESULT_V001.md` | `a0d8b3f71632bd56cc3646fa59e84a2c2776539fadf04be733c7a1eaa997bdbb` | Unit-weight differential theorem and scope ceiling |
| `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `20a3a17d44e15841baded9eaed3fdbecfde0ecb14bdb8162ea41a8bcd21d1a48` | Character premise, associated line, and Gate-4 quantifier |
| `35_GATE1_COMPARISON_GROUP_RESULT_V001.md` | `7ec4e290201840a6e4a000c96d590fe08138d385afe2eb0f7a2c9887b1d46357` | Conditional group classification |
| `PRIMITIVE_TRANSPORT_ONLY_PHASE_COMPLETE_GENERATOR_PRINCIPLE_V001.md` | `aa2ef0e78a1ad975a04596831eef2ea7587b78c4fa9d979ae8a742308cd7c214` | Adopted unit-character minimal-coupling branch |
| `01_PREMISE_LEDGER.md` | `5916bea8bfa7de59331b315e50284d62bc90ebf4300da929b433ab55d4f3dc09` | Least-favorable premise status |
| `STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md` | `76916244bdbcac7c2a6d4afae40f35127540d1d9e4cfc86fb72318506671161f` | Ratified integer character-label system |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md` | `1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6` | Instantiated carrier and source maps, no dynamics |
| `R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_RESULT_V002.md` | `2be95d5b58ea000df9a30b717a809374a90693f78a893d87b73a12e4be97fa21` | Exact finite record transition |
| `STAGE8_T7_ACTUAL_PRIMITIVE_TRANSITION_RESPONSE_AUDIT_SPEC_V001.md` | `8b53704d5ba0f49bec6c385984ea8d68d00a04f218c0db47092e5890bdbe127d` | Prior incidence-phase decoration test |
| `STAGE8_T7_ACTUAL_PRIMITIVE_CAUSAL_TRANSITION_MAP_RESULT_V001.md` | `7020b3cbe37e96e5aef6eb49a75117e3335b62280b3bbece58a5673cbbdcb00f` | Promotion refutation and actual-parent requirement |

### 1.3 Roots, exclusions, and queries

Roots entered:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/workspace
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output
/Users/bgm/MB Work/alpha_supervision
```

Excluded absolutely:

```text
a32_holdout/custodian_private/
.git/
external/
third_party/
sidecars as substantive evidence
byte-identical mirrors as independent authorities
```

No private-custodian path was entered. Word-boundaried, case-insensitive
queries included:

```text
covariant incidence | unit weight | unit character | minimal coupling
U_e | D_(a,b) | character covariance | rho_joint | holonomy
charge magnitude | q_primitive | Lambda_N | source map | s_J | s_R
finite transition | U_N | S_N | P_ch | A_+ | A_- | J_+ | J_-
source-history map | connection phase | actual Lorentzian parent
```

## 2. What Gate 4 actually proves

### 2.1 Its input already contains transport

BID v011 first declares the associated Hermitian line bundle

```text
L = P x_(rho_joint) C,
```

and `U_e` as parallel transport in that bundle
(`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:224-239`). Its local incidence
family is then

```text
D_(a,b),e x = i_t(a_e U_e x) - i_s(b_e x),
```

with `U_e` held fixed while `(a_e,b_e)` vary (`:515-548`). Thus Gate 4 does not
derive the existence of `U_e` by eliminating a non-covariant competitor. It
derives which normalized incidence column survives **conditional on** that
transport and character-covariance premise.

### 2.2 “Unit weight” has one exact referent

Gate 4 composes adjacent columns. Interior closure gives

```text
a_e = b_e' = constant
```

on a connected complex. One-record normalization then gives

```text
|a|=1.
```

Vertex rephasing removes the common phase on trees; loop holonomy remains.
Choosing `a=b=1` is a representative of this equivalence class
(`30_GATE4...:35-60`; `32_GATE4...:9-31`).

No step in this proof varies a charge `n`, a representation `rho_n`, the
source projector `P_ch`, the record swap `S`, or an interaction Hamiltonian.

```text
GATE4_FIXES_INCIDENCE_COEFFICIENT_MAGNITUDE = true | TYPE-P |
  premises: the declared Gate-4 family and inputs

GATE4_FIXES_PHYSICAL_SOURCE_CHARGE = false | TYPE-R |
  test: source charge is not a variable in the Gate-4 family

GATE4_FIXES_CONNECTION_ATTACHMENT_TO_RECORD_SWAP = false | TYPE-R |
  test: S and P_ch do not occur in the Gate-4 family
```

### 2.3 Countermodel against character selection

On a compact `U(1)` line, integer characters give transports

```text
U_e^(n) = (U_e)^n,  n in Z.
```

For every predeclared `n`, the incidence column

```text
D_e^(n)x = i_t(U_e^(n)x) - i_s(x)
```

has the same coefficient closure and one-record norm as the `n=1` column.
Gate 4's proof therefore returns unit coefficient weight for each fixed
character; it does not distinguish the characters.

The check is structural and pre-response:

```text
U_bar(e)^(n) = (U_e^(n))^-1,
U_(e2 o e1)^(n) = U_e2^(n) U_e1^(n),
||i_t(U_e^(n)x)-i_s(x)||^2 = ||x||^2+||x||^2 = 2||x||^2.
```

Thus orientation, path composition, and C3 normalization survive. On a loop
with holonomy `H`, the character changes the invariant to `H^n`; this is not
removed by vertex rephasing in general. The alternatives therefore are not
merely different representatives of Gate 4's coefficient equivalence class.

This is not an imported hypothetical family pasted onto the corpus. DoR-008
ratifies `Lambda_N=Z^N`, its direct limit, and character generators
(`STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md:229-295`;
`C0_DOR008:147-278`).

If the independent **faithfulness** premise for a one-dimensional `U(1)`
action is also imposed, the integer family reduces to the two faithful
characters `n=+1` and `n=-1`. No sealed equivalence in the entered sources
identifies those two as the same physical source-history map. Without that
premise the displayed DoR-008 label family is countably infinite.

```text
CHARACTER_ALTERNATIVE_FAMILY_WITH_DOR008_LABELS = countably_infinite
  members: n in Z

FAITHFUL_ONE_DIMENSIONAL_CHARACTER_SUBFAMILY_SIZE = 2
  members: n=+1, n=-1

PHYSICAL_EQUIVALENCE_IDENTIFIES_N_PLUS_1_AND_N_MINUS_1 = NO_VERDICT

GATE4_SELECTS_N_EQUALS_PLUS_1 = false | TYPE-R |
  test: every fixed-n column passes the coefficient closure/normalization proof
```

The program's `n=+1`/unit-charge selection exists, but as adopted/disclosed
physical content, not as this theorem's output.

## 3. Why the finite transition does not inherit the connection

### 3.1 Distinct carriers and maps

Q-227's exact fixed transition is

```text
U_N^0 = P_0 tensor I_R_N + P_ch tensor S_N,
S_N = tensor_(j=1)^N S_j.
```

It acts on the source charge-sector decomposition and the finite record matrix
algebra. It has no `A`, `J`, or `g` argument
(`STAGE8_TASK2D_FINITE_N_INFLUENCE_FUNCTIONAL_INSTANCE_CONSTRUCTION_RESULT_V001.md:140-182,381-412`).

Gate 4's `U_e` acts between incidence-line fibers. DoR-008's `s_J,s_R` land in
bounded adjointable operators on the ratified carrier. No dynamics consumes
their outputs. These three maps cannot be identified by notation.

An attachment must specify at least:

```text
Attach : (connection/source history, finite incidence, U_N^0)
         -> U_N[A,J,g]
```

together with its representation, carrier embeddings, orientation law,
time-ordering, and common-origin certificate. No such `Attach` exists.

```text
SEALED_ATTACH_MAP_EXISTS = false | TYPE-S |
  roots/exclusions/queries: Section 1.3

FINITE_TRANSITION_IS_GATE4_DIFFERENTIAL = false | TYPE-R |
  test: domain/codomain/signature comparison

DOR008_SOURCE_MAPS_ARE_DYNAMICS = false | TYPE-R |
  test: their codomain is a represented operator algebra; C0/U2 expressly
        withhold the consuming action/evolution
```

### 3.2 Attachment alternatives already visible

The corpus exposes at least three inequivalent attachment locations:

| Placement | Corpus object | Standing |
|---|---|---|
| Incidence-line decoration | `d_j(A_j)=-|v_j>+exp(iA_j)|v_(j+1)>`, hence `P_j(A)` | Explicit stripped fixture; does not promote to the physical map |
| Actual source generator | `h_0[g,A]` inside the time-ordered Lorentzian parent | Required by the actual-parent result; physical instance unbuilt |
| Record endpoint/write operator | inserting a phase into or around `S_j`/the controlled write | The relay's proposed decoration; no sealed map or rule selects its placement |

A fourth possibility is the constant history-independent family `U_N[A]=U_N^0`.
Q-227 already identifies that as a new uncoupled dynamics choice that would
preassign zero field response; it is not derived by the finite producer.

The three nonconstant locations are not an exhaustive family. The action can
also be distributed among source propagation, interaction, contact terms, and
record transport in a common-origin parent. Because the corpus supplies no
closed attachment grammar, its total cardinality is `NO_VERDICT`, with at
least the three named nonconstant placements above plus the trivial one.

```text
NAMED_ATTACHMENT_PLACEMENTS_COUNT = at_least_4
ATTACHMENT_FAMILY_COVERAGE_PROVED = false | TYPE-S |
  scope: no sealed exhaustive grammar for placing the connection in the finite
         source-record dynamics

RELAY_PROPOSED_RECORD_DECORATION_UNIQUELY_SELECTED = false | TYPE-R |
  test: incidence-line and actual-source placements are inequivalent live
        alternatives; the proposed record placement has no selector
```

### 3.3 Prior adversarial result

The earlier sealed transition audit actually executed the incidence-line
decoration. It obtained an open-line phase-only overlap, but the adjudication
withheld promotion because:

- the candidate did not evolve the actual Lorentzian parent;
- it contained no nonzero connection variable in that parent;
- it used an `A`-dependent incidence fixture rather than an `A`-dependent
  adjoint transport in the physical source dynamics; and
- the tree carrier made all connection phases gauge-removable
  (`STAGE8_T7_ACTUAL_PRIMITIVE_CAUSAL_TRANSITION_MAP_RESULT_V001.md:44-84`).

That prior result does not refute all source-history maps. It refutes the
shortcut from a phase-decorated open incidence line to the physical map.

```text
PHASE_DECORATED_INCIDENCE_FIXTURE_IS_PHYSICAL_SOURCE_HISTORY_MAP = false |
  TYPE-R |
  test: sealed actual-parent adjudication

PRIOR_FIXTURE_REFUTES_ALL_SOURCE_HISTORY_MAPS = false | TYPE-R |
  test: it tests one stripped carrier and expressly names the actual-parent
        construction as the remaining obligation
```

## 4. DoR-008 and TYPE-P do not rescue the build

DoR-008 supplies, conditionally:

```text
Lambda_N=Z^N,
character unitaries U_lambda,
CTP branch tensor factors,
bounded finite-support source maps s_J and s_R.
```

Those are `TYPE-P | premises: DoR-008`. They deliberately export no scalar
state, dynamics, quotient, measure, or response. In particular:

1. the integer label system contains alternatives rather than selecting one;
2. `s_J,s_R` provide sources in an algebra but no evolution that consumes them;
3. the record-stage inclusion and field-character inclusion are not a dynamics
   descent; and
4. DoR-008 contains no certified map to `S_N`.

The adopted Transport-Only principle separately supplies `q_primitive=1` and
minimal transport as a physical premise. A build using it could be marked
`TYPE-P`, but it would still need the missing attachment map and would no longer
be a derivation from Gate 4 plus Q-227 alone. The relay's standing question is
therefore answered `CHOICE`, and its stop rule applies.

```text
DOR008_SELECTS_ONE_PHYSICAL_CHARACTER = false | TYPE-R |
  test: Lambda_N contains all integer finite-support labels

DOR008_CONNECTS_SOURCE_MAPS_TO_FINITE_TRANSITION = false | TYPE-R |
  test: no action/evolution map is part of C0_008

UNIT_CHARACTER_AVAILABLE_AS_ADOPTED_PREMISE = true | TYPE-P |
  premises: Transport-Only Phase-Complete Generator Principle and disclosed
            vectorlike unit-charge branch

ADOPTED_UNIT_CHARACTER_SUPPLIES_ATTACH_MAP = false | TYPE-R |
  test: a representation choice does not specify where/how it enters U_N^0
```

## 5. Consequence for the requested construction

No `N=1` or `N=2` source-dependent functional was written. Doing so would
silently choose both a character and an attachment. The Q-227 baseline remains
untouched:

```text
I_N = identity on the neutral/charged history labels;
Phi_N(rho) = P_0 rho P_0 + P_ch rho P_ch.
```

Those are zero-source results. This artifact neither impeaches nor extends
them.

The smallest lawful next object is not a decorated matrix. It is a frozen
attachment candidate with:

```text
one declared character n;
one declared carrier placement;
one actual Lorentzian parent action/evolution;
one map consuming the DoR-008 source operators;
one finite restriction to U_N^0 at zero source;
U1 branch/reality and gauge-covariance certificates;
one common-origin descent trace;
and a hostile comparison against the other named placements.
```

That is a sized adoption/theorem candidate for the principal. It is not built
here.

```text
U_N_A_N1_CONSTRUCTED = false | TYPE-C |
  constraint: choice standing triggered the mandatory stop

U_N_A_N2_CONSTRUCTED = false | TYPE-C |
  constraint: choice standing triggered the mandatory stop

F_N_A_PLUS_A_MINUS_CONSTRUCTED = false | TYPE-U |
  would-build: selected and certified source-history dynamics plus the Q-227
               finite trace

EQUAL_HISTORY_CHECK_EXECUTED = false | TYPE-C |
GAUGE_COVARIANCE_CHECK_EXECUTED = false | TYPE-C |
ZERO_HOLONOMY_DEPHASING_CHECK_EXECUTED = false | TYPE-C |
  constraint for all three: no lawful candidate map was instantiated

Q227_ZERO_SOURCE_BASELINE_RETAINED = true
  scope: this adjudication makes no modification to I_N or Phi_N
```

## 6. Symbol collisions bearing on the verdict

1. **`a_+`,`a_-`.** In Q-227 they label discrete endpoint histories in
   `{0,ch}`. In this relay they denote background connection histories. This
   artifact uses `sigma_+`,`sigma_-` for the discrete labels and `A_+`,`A_-`
   for connection histories.
2. **`U_N`.** Q-227's `U_N^0` is a fixed source-record unitary. The target
   `U_N[A,J,g]` is an unbuilt family. They are not the same object.
3. **unit weight / unit charge.** Gate 4's unit weight is the normalized
   incidence coefficient. Unit charge is a character choice. They are not the
   same scalar.
4. **holonomy.** This adjudication concerns Gate-4 edge/graph transport. It does
   not identify that object with the sealed quarter-turn record-changing
   holonomy, a plaquette Wilson loop, or the composition-loop phase.
5. **`G_joint`.** It remains the BID comparison group, not the response
   generator interface `Gen_C0`.

## 7. Complete negative ledger — DoR-006

| Negative | Type | Reason |
|---|---|---|
| Gate-4 unit weight is unit charge | `TYPE-R` | Different variables and quantifiers |
| Unit character derived by Gate 4 | `TYPE-R` | Character is fixed before the hostile family |
| Gate 4 derives finite-transition decoration | `TYPE-R` | Carrier/signature/quantifier mismatch |
| Minimal coupling derived here | `TYPE-R` | Transport-Only authority explicitly calls it adopted |
| Gate 4 fixes physical source charge | `TYPE-R` | Charge absent from candidate family |
| Gate 4 fixes attachment to `S_N` | `TYPE-R` | `S_N` and `P_ch` absent from Gate-4 family |
| Gate 4 selects `n=+1` | `TYPE-R` | Fixed-`n` counterfamily passes the same coefficient proof |
| Physical equivalence identifies `n=+1,-1` | `NO_VERDICT` | No sealed physical equivalence located |
| Sealed `Attach` map exists | `TYPE-S` | Scoped whole-program search |
| Finite transition is Gate-4 differential | `TYPE-R` | Different domains and codomains |
| DoR-008 source maps are dynamics | `TYPE-R` | C0 assembly exports no evolution |
| Attachment-family coverage proved | `TYPE-S` | No exhaustive placement grammar found |
| Proposed record decoration uniquely selected | `TYPE-R` | Other inequivalent placements remain |
| Decorated incidence fixture is physical map | `TYPE-R` | Prior actual-parent adjudication |
| Prior fixture refutes all history maps | `TYPE-R` | Its own scope names a remaining route |
| DoR-008 selects one physical character | `TYPE-R` | It contains the integer label system |
| DoR-008 connects sources to finite transition | `TYPE-R` | No dynamics/descent map |
| Adopted unit character supplies attachment | `TYPE-R` | Character and placement are distinct data |
| Source-history map constructed | `TYPE-U` | Character/attachment/common-origin dynamics absent |
| `N=1,2` builds executed | `TYPE-C` | Mandatory choice-stop |
| Three checks executed | `TYPE-C` | No lawful candidate exists to test |
| Full `F_N[A_+,A_-]` constructed | `TYPE-U` | Source-history dynamics remains absent |

`TYPE-C` is used only for checks blocked by the relay's mandatory stop after the
choice verdict. Missing construction objects are `TYPE-U`; scoped search
absences are `TYPE-S`; only tested false identities/claims are `TYPE-R`.

## 8. Scope and custody close

This artifact adjudicates provenance and object identity. It does not decorate
a transition, evaluate a holonomy or phase, construct an influence functional,
take a variation, extract a kernel, or compute a response. It does not compute
alpha, `kappa_record`, `kappa_Thomson`, a coupling, a scale, a physical root,
or any measured comparison.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
MACHINERY_APPEAL = NOT_TRIGGERED
```
