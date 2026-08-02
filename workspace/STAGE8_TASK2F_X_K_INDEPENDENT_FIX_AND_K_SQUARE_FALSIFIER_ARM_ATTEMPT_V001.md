# Stage 8 Task 2f `X_K` Independent-Fix and `K_square` Falsifier-Arm Attempt v001

Date: 2026-08-01  
Lane: CODEX LANE 2  
Task: PASTE 326 -- Task 2f  
Register head supplied by relay: Q-242  
Artifact status: RESULT / ATTEMPT  

## 0. Lead result

**THE ONLY `X_K` FAMILY CONSTRUCTIBLE FROM THE SUPPLIED INCIDENCE DATA IS A
1,088-MEMBER FAMILY OF COORDINATE COPIES OF THE SEALED `K_square` INCIDENCE
OPERATOR. EVERY MEMBER INTERTWINES AND REPRODUCES THE SEALED CHARACTERISTIC
POLYNOMIAL, BUT NONE IS A FINITE RESTRICTION OF `C0_008`. THE ANTI-RELABELING
KILL THEREFORE FIRES: THIS IS A TARGET-SPECIFICATION COPY, NOT THE FIRST
NONTAUTOLOGICAL CONTACT BETWEEN DoR-008 AND `K_square`.**

```text
INCIDENCE_COPY_FAMILY_INSTANTIATED = true
INCIDENCE_COPY_FAMILY_CARDINALITY = 1088
INCIDENCE_COPY_INTERTWINING_TEST = PASS
INCIDENCE_COPY_CHARACTERISTIC_POLYNOMIAL_TEST = PASS

INCIDENCE_COPY_IS_C0_008_FINITE_RESTRICTION = false | TYPE-R |
  test: compare the candidate's provenance, algebra, carrier, and representation
        with the ratified C0_008 tuple; the candidate imports the K_square cell
        set and incidence, while C0_008 supplies only sequential character labels
        and a Hilbert-C-star-module representation

INDEPENDENT_C0_SOURCE_INCIDENCE_OPERATOR_X_K_FIXED = false | TYPE-U |
  would-build: a target-independent finite-complex restriction package carrying
               a finite C0 algebra/subquotient, comparison-capable carrier,
               representation, cellular object/degree map, and source-side
               incidence generator fixed before the B_K output is inspected

K_SQUARE_DOR008_FALSIFIER_ARM_EXECUTED = false | TYPE-C |
  constraint: no eligible C0_008-side X_K and representation intertwiner exist |
  release: the package named immediately above

K_SQUARE_SEALED_RESULT_REPRODUCED_BY_C0_008 = NO_VERDICT
K_SQUARE_SEALED_RESULT_DISAGREES_WITH_C0_008 = NO_VERDICT
DOR008_FALSIFIER_FIRED = NO_VERDICT
DOR008_VOIDED_BY_THIS_ATTEMPT = false | TYPE-S |
  scope: this artifact exhibits no eligible C0_008/K_square comparison result
```

The polynomial agreement is real mathematics on a declared finite fixture. It
is not reported as a DoR-008 pass. Q-241's choice-invariance removes the need to
choose one filtration, but it does not turn target incidence data into a
completion-side operator.

## 1. Preflight and current authorities

```text
DOES_THE_REQUIREMENT_EXIST = true
CURRENT_LINEAGE_USED = Q-241 plus Q-242 anti-relabeling standard
SUPPLIED_INPUTS_EXIST = true |
  scope: sealed K_square incidence/holonomy data, the 1088 support-map family,
         C0_008, U1_008 conventions, and DoR-008 source maps
ELIGIBLE_C0_SOURCE_OPERATOR_EXISTS_BEFORE_THIS_ATTEMPT = false | TYPE-U |
  source: Q-241 exact stopping point
```

The live package required by Q-241 is
`C0_FINITE_INCIDENCE_OPERATOR_PREIMAGE_PACKAGE`, including a finite C0
algebra/subquotient, a comparison-capable carrier, a representation, `X_K`,
`T_K`, both intertwinings, and pre-output provenance
(`STAGE8_TASK2F_K_SQUARE_CHOICE_INVARIANT_FALSIFIER_CONTENT_DETERMINATION_V001.md:377-430`).

The relevant sealed object is the unfilled square with four named vertices and
four oriented edges
(`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1836-1851`). Its edge transports
and incidence rule are

```text
u_a0 = u_ab = u_0b = 1,
u_ba = exp(-i Phi),

partial_rho,e x = u_e x v_target - x v_source
```

(`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1860-1879`). The target block
operator is defined only afterward from this differential and its adjoint
(`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1881-1888`). That ordering permits
an incidence-first diagnostic without consulting the displayed `B_square`
matrix.

### 1.1 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003

/Users/bgm/MB Work/alpha_supervision
```

The second root was entered only for `LOCKED_PROCESS.md`. No
`a32_holdout/custodian_private/` directory was entered.

### 1.2 Bounded source set

```text
BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md
STAGE8_V011_COMPOSITION_LOOP_MATRIX_EXPERIMENT_RESULT_V001.md
STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md
STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md
STAGE8_TASK2F_FINITE_INCIDENCE_REALIZATION_FUNCTOR_FORCING_PROTOCOL_RESULT_V001.md
STAGE8_TASK2F_K_SQUARE_CHOICE_INVARIANT_FALSIFIER_CONTENT_DETERMINATION_V001.md
/Users/bgm/MB Work/alpha_supervision/LOCKED_PROCESS.md
```

### 1.3 Queries actually run

Word-boundaried, case-insensitive intersections were run over the bounded source
set for

```text
incidence | boundary | D_square | B_square | source operator | preimage |
intertwiner | finite representation | K_square | Lambda_N | s_J | s_R
```

The query returned 232 bearing lines. The decisive source-side hits are:

1. `Lambda_N=Z^N` labels sequential stages and has no functorial action on
   `K_square`
   (`STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md:417-438`).
2. `V_N=C tensor_Z Lambda_N=C^N` is explicitly only a test linear carrier; it
   does not represent `A_F`, scalarize `E_C0`, or construct a C0 incidence
   operator
   (`STAGE8_TASK2F_FINITE_INCIDENCE_REALIZATION_FUNCTOR_FORCING_PROTOCOL_RESULT_V001.md:120-129`).
3. The ratified source maps are finite sums of represented character unitaries
   (`STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md:475-516`),
   not a cellular differential.

Exclusions: `.git`, binary/media files, duplicate seal sidecars as independent
authority, archive mirrors as additional votes, and every
`a32_holdout/custodian_private/` directory.

## 2. Step 1 -- freeze the candidate family before testing

### 2.1 Incidence data that can determine an operator

For an admissible cellular filtration

```text
o = (c_1,...,c_8) in LE(K_square),
```

let

```text
V_8^o := C^8,
q_i := the sequential coordinate carrying the declared cell label c_i,
V_8^o = V_0^o direct-sum V_1^o
```

where the degree of `q_i` is the degree of `c_i`. This uses Q-241's complete
support-map family, whose exact size is 1,088. Before defining any comparison
map and without consulting any `B_square` matrix element, define the direct
incidence operator `delta_o` by the square's own edge rule:

```text
delta_o(q_e) := u_e q_target(e) - q_source(e),

X_o^inc := [[0,       delta_o],
            [delta_o^dagger, 0]].
```

The candidate family is frozen as

```text
F_X^inc(K_square)
  := { (V_8^o, X_o^inc) : o in LE(K_square) }.
```

This is an instantiated family, not a schema: `LE(K_square)` was exhaustively
counted and its members are the exact linear extensions of the eight-cell face
poset
(`STAGE8_TASK2F_FINITE_INCIDENCE_REALIZATION_FUNCTOR_FORCING_PROTOCOL_RESULT_V001.md:423-487`).

```text
X_FAMILY_DECLARED_BEFORE_COMPARISON_OUTPUT = true
X_FAMILY_USES_B_K_MATRIX_ELEMENTS = false | TYPE-S |
  scope: definitions in this section
X_FAMILY_USES_T_K = false | TYPE-S |
  scope: definitions in this section
X_FAMILY_MEMBER_COUNT = 1088
X_FAMILY_UNIQUE_AS_RAW_SEQUENTIAL_REALIZATION = false | TYPE-R |
  test: Q-241's exact linear-extension count
X_FAMILY_FINAL_ABSTRACT_OPERATOR_CLASS_COUNT = 1 |
  equivalence: unitary coordinate transport after the K_square cell labels have
               already been imported
```

That last one-class quotient is a statement about coordinate copies of the
same target incidence object. It is not a physical equivalence between 1,088
C0 restrictions; no such restrictions exist yet.

### 2.2 Canonical displayed representative

For the frozen order

```text
o_A = (v_00,v_10,v_01,v_11,e_a0,e_0b,e_ab,e_ba)
```

and the sealed evaluated transports, the edge rule alone gives

```text
D_inc =
[[-1,-1, 0, 0],
 [ 1, 0,-1, 0],
 [ 0, 1, 0,-1],
 [ 0, 0, 1,-1]],

X_A^inc = [[0_4, D_inc],
           [D_inc^T, 0_4]].
```

The formula was written from the four oriented edges and their transports,
not copied from `STAGE8_V011_COMPOSITION_LOOP_MATRIX_EXPERIMENT_RESULT_V001.md`.
The sealed matrix display was withheld from the construction and used only in
the later comparison.

## 3. Step 2 -- construct and freeze `T_o` independently

After `F_X^inc` was frozen, define

```text
T_o : V_8^o -> H_square,
T_o(q_i) := the normalized elementary-cell basis vector named by c_i,
            in its declared orientation and vertex frame.
```

This is exactly Q-241's sealed comparison signature for the complete support
map
(`STAGE8_TASK2F_FINITE_INCIDENCE_REALIZATION_FUNCTOR_FORCING_PROTOCOL_RESULT_V001.md:202-243`).
It is unitary for the Gate-3 identity forms. Vertex-gauge and orientation
representatives are handled by the already sealed conventions; `T_o` is not
tuned using a matrix outcome.

```text
T_FAMILY_FROZEN_BEFORE_INTERTWINING_TEST = true
T_FAMILY_USES_B_K_MATRIX_ELEMENTS = false | TYPE-S |
  scope: displayed definition
T_FAMILY_TUNED_TO_PASS = false | TYPE-S |
  scope: T_o is the pre-existing normalized support map for every o
```

## 4. Step 3 -- execute the algebraic intertwining diagnostic

For each edge coordinate `q_e`, direct substitution gives

```text
T_o delta_o(q_e)
  = u_e v_target(e) - v_source(e)
  = partial_rho T_o(q_e).
```

Taking the adjoint under the identity Hilbert forms gives the vertex-to-edge
half. Therefore, for every `o in LE(K_square)`,

```text
T_o X_o^inc = B_square T_o.
```

This proof covers all 1,088 coordinate choices. It uses the common upstream
incidence rule on both carriers. It does not use a matrix pullback
`T_o^(-1) B_square T_o`.

```text
INCIDENCE_COPY_INTERTWINING_HOLDS_FOR_ALL_1088 = true
INTERTWINING_PROOF_IS_MATRIX_PULLBACK = false | TYPE-R |
  test: construction order and edge-basis proof above
```

### 4.1 Mandatory anti-relabeling attack

The equality is nonetheless not the DoR-008 falsifier equation. The type and
provenance comparison is:

| Field | Incidence-copy candidate | Required C0-side field | Result |
|---|---|---|---|
| Algebra | none; `V_8^o` is only a vector space | finite algebra/subquotient `A_C0,K` | MISSING / TYPE-U |
| Carrier | `C tensor_Z Lambda_8=C^8`, relabeled by target cells | finite restriction of `E_C0=H_SR external-tensor B_B` | MISSING / TYPE-U |
| Representation | none | `rho_C0,K` induced from `pi_C0` | MISSING / TYPE-U |
| Cellular degree | imported from `c_i in Cell(K_square)` | image of a source-side object/degree map | MISSING / TYPE-U |
| Incidence | copied from the sealed target edge rule | generated by a C0-side source operator | MISSING / TYPE-U |
| `T_o` representation intertwining | not posable | `T_o rho_C0,K(a)=rho_K(a)T_o` | UNEXECUTABLE / TYPE-C |
| Operator equality | passes because both sides use the same target incidence specification | comparison of independently descended source and target operators | INELIGIBLE AS DoR-008 TEST / TYPE-R |

The ratified C0 carrier is a Hilbert `C*`-module and its source maps are sums of
character unitaries
(`STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md:159-190,223-265`).
It deliberately exports neither a scalar finite Hilbert realization nor a
cellular differential. The candidate introduces both the cell identities and
the differential from `K_square`; nothing in `C0_008` descends them.

Thus the candidate is stronger than the forbidden literal formula
`X=T^(-1)BT`--it reconstructs the same operator from the common incidence
specification--but it still fails the Q-242 role test. Renaming the tuple

```text
(Cell(K_square), partial_rho, Gate-3 forms)
```

as a C0 source object does not make it a restriction of `C0_008`. The missing
derivational arrow is exactly the object under test.

```text
ANTI_RELABELING_KILL_FIRED = true
INCIDENCE_COPY_PROVES_C0_008_REPRODUCTION = false | TYPE-R |
  test: the candidate has no C0 algebra, C0 representation, or source-to-cell
        descent; its operator is generated from the target cell complex
```

## 5. Step 4 -- strongest-result diagnostic

Because the proxy intertwining holds, the characteristic polynomial was checked
on the canonical incidence-built representative. This is reported as a fixture
diagnostic, not as the DoR-008 restriction test.

Exact Faddeev-LeVerrier arithmetic on `X_A^inc` returned coefficients

```text
[0, -8, 0, 20, 0, -16, 0, 4]
```

and hence

```text
det(z I_8 - X_A^inc)
  = z^8 - 8 z^6 + 20 z^4 - 16 z^2 + 4.
```

A separately coded exact rational Gaussian determinant check at the nine
integer arguments `z=-4,...,4` agreed at every argument. Since both sides are
monic degree-eight polynomials, those nine agreements independently certify
the polynomial identity. The result equals the sealed characteristic
polynomial at
`STAGE8_V011_COMPOSITION_LOOP_MATRIX_EXPERIMENT_RESULT_V001.md:150-162`.

For every other `o`, Q-241 supplies a permutation matrix `P_o` with

```text
X_o^inc = P_o^T X_A^inc P_o,
```

so the polynomial verdict is family-invariant.

```text
PROXY_CHARPOLY_EXACT = z^8 - 8 z^6 + 20 z^4 - 16 z^2 + 4
PROXY_CHARPOLY_MATCHES_SEALED_RESULT = true
PROXY_CHARPOLY_MATCH_INVARIANT_ACROSS_1088 = true
PROXY_CHARPOLY_MATCH_COUNTS_AS_DOR008_PASS = false | TYPE-R |
  test: eligibility table in Section 4.1
```

No eigenvalue, root of the physical residual, coupling, scale, or measured
comparison was computed.

## 6. Exact stopping point and would-build

The route reaches:

```text
sealed K_square incidence
  -> complete 1088-member coordinate-copy X family
  -> independently frozen support maps T_o
  -> exact family-wide intertwining
  -> exact family-wide characteristic-polynomial agreement.
```

It stops before:

```text
finite restriction of the ratified C0_008 algebra/module/source maps
  -> eligible C0-side source incidence operator X_K
  -> representation intertwining
  -> DoR-008 K_square falsifier verdict.
```

The smallest adequate would-build is not another matrix. It is

```text
CELLULAR_RESTRICTION_PACKAGE_FROM_I_REC := (
  object map from one declared sequential stage/refinement object to K_square,
  cellular degree and orientation map,
  finite algebra/subquotient A_C0,K,
  comparison-capable carrier E_C0,K,
  representation rho_C0,K inherited from pi_C0,
  source-side incidence generator X_K produced by that representation,
  T_K preserving the algebra action, Gate-3 forms, incidence, and refinement,
  frozen provenance predating inspection of the B_K output
).
```

An adoption of a geometric path/cell functor would also fill the missing slot,
but it would be a new premise: v002 explicitly removed the earlier geometric
path-functor architecture
(`STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md:595-619`).
This artifact neither adopts nor proposes one.

```text
LAWFUL_X_K_CANDIDATE_FAMILY_EMPTY_BY_PROOF = NO_VERDICT |
  reason: absence of the restriction package is TYPE-U, not an impossibility theorem

LAWFUL_X_K_UNDERDETERMINED_WITHIN_AN_INSTANTIATED_FAMILY = false | TYPE-S |
  scope: the lawful family cannot yet be instantiated; the 1088-member family is
         only the covered target-support/copy family

FALSIFIER_CAN_NEVER_BE_AUDITED_ON_THIS_ARM = false | TYPE-R |
  test: the displayed would-build gives a coherent release condition; this
        artifact proves no impossibility of constructing it
```

## 7. Typed negatives and symbol/identity fences

```text
X_K_DEFINED_AS_T_K_INVERSE_B_K_T_K = false | TYPE-S |
  scope: this artifact

PACKAGE_C0_IDENTIFIED_WITH_GATE3_C_0 = false | TYPE-S |
  scope: this artifact; these are distinct carriers

SEQUENTIAL_STAGE_INDEX_IDENTIFIED_WITH_CELLULAR_DEGREE = false | TYPE-S |
  scope: no such identity is asserted; the proxy labels it explicitly as an import

SOURCE_MAP_s_J_OR_s_R_IDENTIFIED_WITH_CELLULAR_INCIDENCE = false | TYPE-S |
  scope: domains, codomains, and formulas differ

RAW_MATRIX_AGREEMENT_REPORTED_AS_PHYSICAL_RESTRICTION = false | TYPE-S |
  scope: this artifact

FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S |
  scope: all requested structural checks were permitted and run
```

Bearing symbol collision: package `C0_008` is not the cellular chain group
`C_0(K_square)`. The shared token `C0`/`C_0` cannot supply the missing carrier
map. Bearing name collision: the `source maps` `s_J,s_R` are represented field
character maps, whereas the requested `source incidence operator` is a
cell-degree-changing comparison operator; the shared word `source` does not
identify them.

## 8. Fence and custody ledger

```text
artifact_status = RESULT_ATTEMPT
task_road = TASK_2F
structural_finite_operator_comparison_performed = true
physical_target_evaluated = false | TYPE-S
a32_custodian_private_touched = false | TYPE-S
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
kappa_Thomson_computed = false
coupling_computed = false
scale_computed = false
physical_residual_root_computed = false
measured_constant_comparison_performed = false
Misner_Sharp_Brown_York_fork_resolved = false
git_command_run = false
register_edited = false
baseline_edited = false
commit_created = false
push_performed = false
```

Lane custody terminates after artifact sealing, sidecar verification, mirroring
of artifact and sidecar, and reporting paths and hashes.
