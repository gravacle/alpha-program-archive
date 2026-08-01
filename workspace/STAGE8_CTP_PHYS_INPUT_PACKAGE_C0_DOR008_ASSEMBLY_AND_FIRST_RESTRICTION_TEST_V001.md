# Stage 8 CTP Physical-Input Package C0 DoR-008 Assembly and First Restriction Test v001

Date: 2026-08-01

Lane: Codex 1

Task: governing-plan Task 2b, relay 295

Status: CONDITIONAL C0 INSTANCE ASSEMBLED / PREMISE-LEVEL DESCENT ASSEMBLED /
FIRST FINITE RESTRICTION PASS / K_SQUARE RESTRICTION MAP UNBUILT

## 0. Lead result

The ratified presentation is sufficient to assemble one exact `C0` instance,
conditional on Decision of Record 008. All six C0 fields are total and retain
the narrow C0 exclusion boundary.

The premise-level descent map from the DoR-008 presentation to that C0 instance
is also total. It is not the independently derived common-origin map required
by the B0 package contract. The two maps are kept distinct below.

The first finite restriction check passes at C0's algebra/representation scope:
at stage `N=1`, the assembled object retains the sealed one-record factor
`M_3(C)`, the finite source-record algebra, and its represented action exactly
through the tensor-unit embedding.

The requested `K_square` check cannot be executed. The ratified presentation
has only Q-201's sequential record-stage category `N<=M`; it deliberately has
no finite-incidence-complex restriction functor. The sealed composition-loop
carrier is the different object
`C_0(K_square) direct-sum C_1(K_square)`. No sealed map relates that carrier to
the sequential C0 module. Choosing `N=4` from the four vertices or four edges
would be an unratified identification.

This is not a disagreement with the finite spectrum and therefore is not
reported as the standing falsifier firing. It is an unbuilt test interface.
The DoR-008 finite-authority condition has not yet passed for `K_square`, so the
conditional C0 instance is not certified against the full standing falsifier.

```text
C0_DOR008_ASSEMBLED = true | TYPE-P |
  premises: DoR-008 and the inherited Q-201/Q-43 source-record tuple

d_C0_DOR008_PREMISE_MAP_ASSEMBLED = true | TYPE-P |
  premises: DoR-008; domain is the ratified presentation package, not an
            independently derived common-origin B0 candidate

d_C0_COMMON_ORIGIN_PROVENANCE_DERIVED = false | TYPE-U |
  would-build: the five-item common-origin construction in Section 5

ONE_CELL_C0_RESTRICTION = PASS | TYPE-P |
  premises: DoR-008 and Q-201's exact N=1 record embedding

K_SQUARE_C0_RESTRICTION_MAP_DERIVED = false | TYPE-U |
  would-build: an explicit finite-complex restriction/correspondence functor
               from the DoR-008 presentation to the Gate-3 incidence carrier

K_SQUARE_RESTRICTION_CONSISTENCY = NO_VERDICT |
  prerequisite: K_SQUARE_C0_RESTRICTION_MAP remains TYPE-U

DOR008_STANDING_FALSIFIER_FULLY_PASSED = false | TYPE-U |
  would-build: execute every finite-complex restriction, beginning with the
               missing K_square map, without identifying package C0 with
               Gate-3 C_0

DOR008_VOID_CONDITION_TRIGGERED_BY_THIS_RUN = NO_VERDICT |
  prerequisite: no K_square restriction comparison was defined or executed;
                no finite disagreement was obtained
```

## 1. Currency, authority, and frozen inputs

Register head checked before construction: Q-212. No later bearing ruling was
consulted.

Decision of Record 008 is
`DECISION_OF_RECORD_008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER_2026-08-01_V001.md`,
hash
`d51a6d5c5bb0020a081cfd2adfb545b9f5ed86ce660d3feacadc5ef68140fb19`.
At lines 8-14 it ratifies the seven declared premises in
`STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md`, hash
`76916244bdbcac7c2a6d4afae40f35127540d1d9e4cfc86fb72318506671161f`.
At lines 16-22 it makes finite restriction a standing falsifier. At lines
33-37 it makes `C0_prop` available under `TYPE-P` while expressly leaving
`d_C0` common-origin provenance undischarged.

The second independent adversarial pass is
`STAGE8_FIELD_CTP_V002_SECOND_ADVERSARIAL_KILL_DETERMINATION_V001.md`, hash
`58f2c82121e7fb34c91212ca0181c71c455eca077ce9f6d060835eb0407c3c93`.
It found the repaired presentation internally total and preserved the C0
boundary, but it did not run the later DoR-008 finite restriction condition.

The inherited source-record tuple is frozen by
`STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DESCENT_BUILD_ATTEMPT_V001.md`, hash
`f64d12def129b7dcd382d0857046d54d5bdc696cc62fbe0124f34fd9f2a2d8b4`.
Its source-record subpresentation is retained byte-for-byte and not rebuilt.

### 1.1 Frozen construction input

Define the exact premise package

```text
P_008 := (
  Q201_tuple,
  Q43_source_record_graded_tensor_typing,
  adopted_compact_unit_character_U1_connection,
  I_rec = the Q201 sequential category N<=M,
  the seven fields ratified by DoR-008,
  the four consequences conditional on those fields,
  the DoR-008 provenance ceiling,
  the DoR-008 finite-authority falsifier
).
```

No state, dynamics, quotient, measure, effect, contact, Ward identity, inverse,
response, continuum realization, or value is added.

## 2. The assembled C0 instance

### 2.1 Inherited source-record face

From Q-201 and the v002 presentation at lines 176-204:

```text
A_src      := CAR(H_src)
(pi_C,H_C) := the inherited source representation projection
R_inf      := the outgoing-record inductive-limit algebra
(pi_out,H_out) := the inherited record representation projection

A_SR := A_src graded-tensor_min R_inf
H_SR := H_C tensor H_out
pi_SR(a tensor r) := pi_C(a) tensor pi_out(r).
```

The finite record system is

```text
R_N = tensor_(j=1)^N M_3(C),
iota_NM(A) = A tensor I_(M-N),  N<=M.
```

### 2.2 Ratified field and branch algebras

From v002 Fields 1-6 (`:212-366`):

```text
Lambda_N := Z^N,
j_NM^Lambda(n_1,...,n_N) := (n_1,...,n_N,0,...,0),
Lambda := direct-sum_(j>=1) Z e_j,

A_F := C*(Lambda),
A_F_CTP := A_F,+ tensor_min (A_F,-)^op,
A_C0 := A_SR graded-tensor_min A_F_CTP.
```

The field/CTP algebra is even. This is the ratified kinematic commutation
premise; it is not a state-factorization or dynamical-independence theorem.

### 2.3 Joint carrier and representation

Let

```text
B := A_F_CTP,
E_F := B_B,
<x,y>_B := x* y,
L_f(x) := f x,

E_C0 := H_SR external-tensor E_F,
<xi tensor x,eta tensor y>_B := <xi,eta>_H_SR x* y,

pi_C0(a tensor f)(xi tensor x)
  := pi_SR(a)xi tensor f x.
```

Then

```text
pi_C0 : A_C0 -> L_B(E_C0)
```

is a nondegenerate joint Hilbert-C-star-module representation, faithful on the
field factor and carrying exactly the inherited standing of `pi_SR` on the
source-record factor.

```text
JOINT_CARRIER_EXECUTED = true | TYPE-P | premises: DoR-008
JOINT_ALGEBRA_EXECUTED = true | TYPE-P | premises: DoR-008
JOINT_REPRESENTATION_EXECUTED = true | TYPE-P | premises: DoR-008
```

Certificate `C0-008-C1`: every object is an instantiated algebra, Hilbert
module, or total represented map. No schema placeholder occurs in the tuple.

Certificate `C0-008-C2`: the field algebra's nuclearity makes the spatial join
unambiguous within the ratified premise package; restriction to the
source-record tensor factor is the inherited action tensored with the module
identity.

### 2.4 Common domain

Every generator and every finite-support source-map output is bounded and
adjointable. Set

```text
D_C0 := E_C0.
```

It is dense in itself and invariant under every operator admitted to C0.
This certificate does not extend to later unbounded local fields, actions,
response operators, or scalar Hilbert-space realizations.

```text
COMMON_DOMAIN_EXECUTED = true | TYPE-P | premises: DoR-008
EVERY_C0_UNBOUNDED_GENERATOR_VERIFIED_ON_D_C0 = true |
  explanation: C0 admits no unbounded generator; every admitted generator is
               bounded adjointable, so the quantified unbounded set is empty
```

Certificate `C0-008-C3`: all represented C0 generators and source-map outputs
preserve `D_C0` by adjointable boundedness and finite support.

### 2.5 CTP branch embeddings and source maps

For `a in A_F`, define

```text
e_plus(a)  := 1_A_SR tensor (a tensor 1),
e_minus(a) := 1_A_SR tensor (1 tensor a^op).
```

These are unital injective star-homomorphisms with commuting ranges and are
represented by `pi_C0 compose e_plus/minus` on `D_C0`.

With

```text
D_J := C_c({+,-} x (Lambda without {0}); C),
D_R := D_J tensor_alg D_J,
```

define

```text
s_J(j) := sum_(a,lambda) j(a,lambda) pi_C0(e_a(U_lambda)),

s_R(r) := (1/2) sum_(a,lambda,b,mu)
          r((a,lambda),(b,mu))
          pi_C0(e_a(U_lambda)e_b(U_mu)).
```

Every sum is finite and lands in `L_B(E_C0)`. The involutions and star
covariance are exactly those in v002 Field 10 (`:475-516`).

```text
CTP_BRANCH_EMBEDDINGS_EXECUTED = true | TYPE-P | premises: DoR-008
FINITE_SUPPORT_SOURCE_MAPS_EXECUTED = true | TYPE-P | premises: DoR-008
```

Certificate `C0-008-C4`: branch maps are total, injective, commuting, and
distinct from charge conjugation and record-stage embeddings.

Certificate `C0-008-C5`: source maps have fixed domains/codomains, finite
outputs, and star covariance. They include no physical branch metric,
orientation, reality involution, or compound-index order; those remain U1.

### 2.6 Exact conditional C0 tuple

The assembled instance is

```text
C0_008 := (
  carrier              = E_C0,
  algebra              = A_C0,
  representation       = pi_C0:A_C0->L_B(E_C0),
  common_domain        = D_C0=E_C0,
  branch_embeddings    = (e_plus,e_minus),
  physical_source_maps = (s_J,s_R),
  provenance_record    = Prov_C0_008
).
```

Here `Prov_C0_008` is v002's exact antecedent tuple with the seven proposal
marks replaced only by `ADOPTED_BY_DOR008`; all derived-within-proposal marks
become `TYPE-P | premises: DoR-008`. No formula or antecedent is changed.

```text
C0_008_IS_AN_INSTANCE = true | TYPE-P | premises: DoR-008
C0_008_IS_UNCONDITIONALLY_DERIVED_PHYSICS = false | TYPE-P |
  premises: its existence is conditional on DoR-008 rather than derived from
            the prior physical stack
```

## 3. The two descent maps that must not be conflated

### 3.1 Premise-level assembly descent

The ratification makes this total map legal:

```text
d_C0^P : P_008 -> C0_008,
d_C0^P(P_008) := Assemble_C0_prop_v002(P_008) = C0_008.
```

Its frozen trace is the ordered construction in Section 2. It supplies every
C0 field before any descendant output is inspected and uses no post-output
supplementation.

```text
d_C0_PREMISE_LEVEL_TOTAL = true | TYPE-P | premises: DoR-008
d_C0_PREMISE_LEVEL_NO_POST_OUTPUT_SUPPLEMENTATION = true | TYPE-P |
  premises: DoR-008 and the exact v002 field list
```

Certificate `C0-008-C6`: every output component has one antecedent in `P_008`,
and the construction order is field labels -> generators/relations -> field
algebra -> branch algebra -> source-record join -> module representation ->
domain -> branch maps -> source maps -> C0 tuple.

### 3.2 Required common-origin descent

The package contract uses the stronger signature

```text
d_C0 : B0_candidate -> C0,
C0 = d_C0(B0_candidate).
```

(`STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md:977-1037`).
DoR-008 expressly does not discharge its common-origin provenance. Therefore
`d_C0^P` is not relabeled as the derived package map.

```text
d_C0^P_EQUALS_DERIVED_COMMON_ORIGIN_d_C0 = false | TYPE-R |
  test: compare domains and provenance claims; P_008 is a ratified premise
        tuple, while the package map begins at an independently supplied
        common-origin B0-role candidate

d_C0_DERIVED = false | TYPE-U |
  would-build: Section 5
```

This is the exact price of the assembly: package C0 exists conditionally, but
its source-record-field common-origin derivation does not.

## 4. DoR-008 first restriction tests

### 4.1 Test R1: one record cell

At `N=1`:

```text
R_1 = M_3(C),
Lambda_1 = Z,
A_F,1 = C*(Z),
B_1 = A_F,1,+ tensor_min (A_F,1,-)^op,

A_SR,1 = A_src graded-tensor M_3(C),
A_C0,1 = A_SR,1 graded-tensor_min B_1.
```

Define the source-record face map

```text
j_SR,1 : A_SR,1 -> A_C0,1,
j_SR,1(a) := a tensor 1_B1.
```

It is an injective unital star-homomorphism. On the assembled carrier,

```text
pi_C0,1(j_SR,1(a))(xi tensor x)
  = pi_SR,1(a)xi tensor x.
```

Thus every source-record algebraic relation and matrix identity is unchanged;
the representation is the exact module amplification of the inherited
one-cell representation. In particular the distinguishable record carrier

```text
R_c = span_C{|r_c>,|p_Q,c>,|e_Q,c>}
```

and its full algebra `B(R_c)=M_3(C)` are the same one-cell factor appearing in
`BID_GLOBAL_CAR_RECORD_COMPOSITION_DERIVATION_V001.md:66-92` and Q-201.

```text
R1_ONE_CELL_ALGEBRA_REPRODUCED = true | TYPE-P | premises: DoR-008
R1_ONE_CELL_SOURCE_RECORD_REPRESENTATION_REPRODUCED = true | TYPE-P |
  premises: DoR-008 and Q-201; equality is at the represented factor-action
            level, with the state-free B-module amplification retained
R1_ONE_CELL_SCALAR_HILBERT_REALIZATION_TESTED = false | TYPE-U |
  would-build: a lawful downstream B->C positive functional and scalarization;
               scalarization is excluded from C0
R1_VERDICT = PASS_AT_C0_SCOPE
```

No state, trace, probability, or physical response is used in this test.

### 4.2 Test R2: `K_square`

The sealed finite authority is
`STAGE8_V011_COMPOSITION_LOOP_MATRIX_EXPERIMENT_RESULT_V001.md`, hash
`29fcbb76748cec8ecbaa8f9debb1e60736c85dbcf54823cb8076c3f17d6e3ffb`.
It fixes the unfilled oriented complex with four vertices and four edges and
the carrier

```text
H_square := C_0(K_square) direct-sum C_1(K_square),
dim H_square = 8.
```

The Gate-3 identity forms, ordered bases, incidence operator, and block
operator act on this carrier. The sealed result gives
`R_square=3/16` at lines 191-197.

The assembled C0 object has no map whose domain or codomain is `H_square`:

1. `I_rec` counts sequential completed record factors; it does not index
   vertices, edges, paths, or finite incidence complexes.
2. `Lambda_N=Z^N` assigns field characters to that sequential stage index.
   It has no functorial action on `K_square`.
3. Q-201's `R_N=M_3(C)^(tensor N)` is a record-factor algebra. It is not the
   chain carrier `C_0(K_square) direct-sum C_1(K_square)`.
4. The standing identity fence explicitly says package `C0` is not Gate-3
   `C_0` (v002 `:701-709`; second kill `:297-312`).
5. The bounded correspondence sweep in Section 7 found no map joining these
   names in the current sources.

Therefore no lawful map

```text
Res_Ksquare : C0_008 -> (H_square,B_square)
```

or reverse finite embedding is supplied. Assigning `N=4` from either the four
vertices or four edges is ambiguous and would reintroduce precisely the
geometric index/path choice removed from v002 Field 1.

```text
R2_K_SQUARE_RESTRICTION_DEFINED = false | TYPE-U |
  would-build: a target-independent finite-complex restriction functor with
               an explicit object map, carrier map, algebra map,
               representation intertwiner, and proof that Gate-3 forms and
               B_square are preserved

R2_K_SQUARE_SPECTRUM_REPRODUCED = NO_VERDICT |
  prerequisite: R2_K_SQUARE_RESTRICTION_DEFINED remains TYPE-U

R2_R_SQUARE_3_OVER_16_CONTRADICTED = NO_VERDICT |
  prerequisite: no comparison map exists; the sealed value was cited, not
                recomputed or transported

R2_VERDICT = UNEXECUTABLE_TYPE_U
```

This is an interface failure, not a finite-result disagreement. This lane does
not declare a principal decision void. It also does not report the standing
falsifier as passed.

## 5. Residual common-origin provenance debt

The required derived `d_C0` still needs all five items preserved in v002
`STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md:755-786`:

1. one admitted `B0`-role realizer or complete role-equivalent origin object;
2. a map from that object to `A_C0`, `pi_C0`, `D_C0`, `e_plus/e_minus`, and
   `s_J/s_R`;
3. coherence witnesses restricting the map to Q-201's source and record
   provenance;
4. proof that the origin reproduces, rather than merely permits, the adopted
   sequential-character and state-free-module presentation; and
5. one frozen no-supplementation certificate.

A complete B0-replacement role realizer for the whole physical-input package
must additionally descend U1, U2, and U3 under the package contract. This
artifact builds none of those objects.

```text
INDEPENDENT_B0_ROLE_REALIZER_SUPPLIED = false | TYPE-U |
  would-build: item 1 above
COMMON_ORIGIN_MAP_TO_ALL_C0_FIELDS_SUPPLIED = false | TYPE-U |
  would-build: items 2-4 above
COMMON_ORIGIN_NO_SUPPLEMENTATION_CERTIFIED = false | TYPE-U |
  would-build: item 5 above
U1_U2_U3_DESCENTS_BUILT = false | TYPE-S |
  roots: this artifact and the exact DoR-008 C0 construction trace |
  excl: later Task-2c/2d/2e work, a32_holdout/custodian_private |
  fences: C0-only task; no post-output supplementation |
  query: exact U1, U2, U3, d_U1, d_U2, d_U3 output fields
```

## 6. C0 exclusion and no-supplementation certificate

| Excluded object | Result |
|---|---|
| joint state / `rho_pre` | absent; no scalar positive functional `B->C` |
| dynamics / action / `U_BR` | absent |
| physical quotient | absent |
| contour, spacetime, gauge, or spectral measure | absent |
| effects or instruments | absent |
| contacts | absent |
| Ward identities | absent |
| inverse, Hessian, or response | absent |
| U1 branch metric/reality/index order | absent |
| local continuum connection | absent; DoR-007 remains open |
| Task 4-6 value or selector | absent |

```text
C0_EXCLUSION_LIST_PASSED = true | TYPE-P | premises: DoR-008
NO_POST_OUTPUT_SUPPLEMENTATION_USED = true | TYPE-P | premises: DoR-008
SCALAR_STATE_OR_MEASURE_EXPORTED = false | TYPE-S |
  roots: C0_008 field list and operation codomains |
  excl: downstream U2/U3 scalarization |
  fences: C0 narrow interface |
  query: maps B->C, scalar state, trace, cyclic vector, density, measure
```

The K-square map is reported missing rather than added after the finite output
was inspected.

## 7. Scope and bounded correspondence sweep

Roots entered:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output
/Users/bgm/MB Work/alpha_supervision
```

Material authorities and checks:

```text
Q-201 source-record construction
Q-208 v002 proposal
Q-211 second adversarial pass
Q-212 / DoR-008
Gate-1 through Gate-4 finite result artifacts
V011 composition-loop structural and matrix-result artifacts
B0 stop specification and substitute admissibility adjudication
governing plan Task 2
```

The correspondence sweep used word-boundaried, case-insensitive intersections
of:

```text
K_square; C_0(K_square); composition-loop
with
d_C0; C0_prop; Lambda_N; iota_NM; A_SR; restriction; finite complex.
```

It found finite-incidence restrictions internal to the Gate/V011 carrier and
the separate sequential restrictions internal to Q-201. It found no object,
map, functor, or intertwiner between those two systems.

```text
K_SQUARE_TO_DOR008_PRESENTATION_MAP_FOUND = false | TYPE-S |
  roots: the four roots above |
  excl: .git, mirrors duplicating the cited authority, superseded versions as
        current authority, a32_holdout/custodian_private |
  fences: no name matching; package C0 and Gate-3 C_0 held distinct |
  query: exact intersections listed above
```

`a32_holdout/custodian_private/` was not entered, listed, searched, opened,
summarized, or read.

## 8. Final status

```text
C0_REQUIRED_COMPONENTS_INSTANTIATED = true | TYPE-P | premises: DoR-008
C0_008_ASSEMBLY_TRACE_FROZEN = true | TYPE-P | premises: DoR-008
C0_008_CERTIFICATES_C1_TO_C6_PASSED = true | TYPE-P | premises: DoR-008
C0_008_EXCLUSION_LIST_PASSED = true | TYPE-P | premises: DoR-008

d_C0_PREMISE_LEVEL_TOTAL = true | TYPE-P | premises: DoR-008
d_C0_DERIVED = false | TYPE-U |
  would-build: the common-origin construction in Section 5

ONE_CELL_RESTRICTION_TEST = PASS_AT_C0_SCOPE | TYPE-P | premises: DoR-008
K_SQUARE_RESTRICTION_TEST = UNEXECUTABLE | TYPE-U |
  would-build: the finite-complex restriction functor in Section 4.2

DOR008_FINITE_AUTHORITY_CONDITION_CERTIFIED = false | TYPE-U |
  would-build: K_square correspondence plus the remaining finite restriction
               tests assigned to Task 2f

TASK2B_C0_INSTANCE_EXISTS = true | TYPE-P | premises: DoR-008
TASK2B_COMMON_ORIGIN_DESCENT_COMPLETE = false | TYPE-U |
  would-build: Section 5

PHYSICAL_VERDICT = NO_VERDICT
CONSTRUCTION_VERDICT = C0_ASSEMBLED_CONDITIONALLY__K_SQUARE_RESTRICTION_INTERFACE_UNBUILT

alpha_computed = false [TERMINAL_FENCE_DECLARATION]
proof_authorized = false [TERMINAL_FENCE_DECLARATION]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION]
coupling_evaluation_authorized = false [TERMINAL_FENCE_DECLARATION]
production_authorized = false [TERMINAL_FENCE_DECLARATION]
```

No physical response, coupling, scale, root, spectrum, eigenvalue, beta
function, absolute interval, or measured comparison was computed or evaluated.
No register, git, commit, push, or deployment action was performed.
