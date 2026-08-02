# Stage 8 Task 4a p_loc Tail-Annihilation Certificate Determination v001

Date: 2026-08-02
Lane: CODEX LANE 1
Task: 4a
Authority: DoR-011, reading and proof only
Register head at start: Q-253
Register head at completion: Q-254

## 0. Lead determination

**THE SEALED DEFINITION OF `p_loc` IS OUTPUT-LOCAL AND
CONSUMPTION-UNTYPED. THE CERTIFICATE `p_loc|Tail_ind=0` CANNOT BE DERIVED
FROM THE CURRENT SEALED TEXT.**

The live sources specify all of the following:

```text
p_loc : physical retarded action kernels -> dimensionless scalars,
p_loc is linear and covariant,
p_loc[L_T]=1,
Pi_loc=(b -> b L_T) compose p_loc,
p_loc extracts the coefficient of the local Maxwell tensor channel,
p_loc must be derived target-independently from the complete physical operator.
```

They do not specify how the functional consumes a completed kernel. In
particular, the lineage supplies none of the three mechanisms that would decide
the tail question:

```text
(a) factorization through finite restrictions or finite-region shadows;
(b) membership in the norm/module class separated at Q-247;
(c) a weak-star or bidual pairing capable of seeing the Q-247 tail.
```

The word `local` types the **coefficient returned** and the one-dimensional
operator channel `span{L_T}`. It does not type the **information read** from the
completed input. The active spine is explicit that the global retarded kernel
is primary and that a `D x D` support restriction is only a probe restriction,
not the unrestricted kernel domain.

The result is therefore class (d), with a useful refinement:

```text
P_LOC_CONSUMPTION_CLASS = OUTPUT_LOCAL_INPUT_CONSUMPTION_UNTYPED

P_LOC_FINITE_SHADOWED_DEFINITION_FOUND = false | TYPE-S |
  roots: parent program Markdown root; governing cleanroom Markdown root;
         supervision register through Q-254 |
  excl: review-packet duplicates; archive mirrors as independent authority;
        scripts/results as defining prose; sidecars as content;
        a32_holdout/custodian_private |
  fences: DoR-011 reading/proof only |
  query: p_loc, Pi_loc, coefficient functional, finite-stage, finite-N,
         finite-region, restriction, support, quasi-local, local limit,
         norm-continuous, adjointable, cylindrical, predual

P_LOC_NORM_MODULE_CLASS_DEFINITION_FOUND = false | TYPE-S |
  roots: same |
  excl: same |
  fences: same |
  query: p_loc with norm, continuous, bounded, adjointable, module,
         left-multiplier, topology, completion

P_LOC_WEAK_STAR_BIDUAL_PAIRING_DEFINITION_FOUND = false | TYPE-S |
  roots: same |
  excl: same |
  fences: same |
  query: p_loc with weak-star, weak-*, bidual, predual, B**, z_tail,
         M_cyl, pairing, normal functional

P_LOC_TAIL_ANNIHILATION_CERTIFICATE_DERIVED = false | TYPE-U |
  would-build: instantiate the physical RetHess class, its physical finite
               restrictions and Tail_ind; derive p_loc on that same class;
               then prove factorization through the restriction quotient or
               prove class membership to which Q-247 separation applies

P_LOC_SEES_TAIL_IND = NO_VERDICT |
  prerequisite: instantiate one admitted t_ind in Tail_ind and one lawful
                completed-domain p_loc with p_loc(t_ind)!=0

B_IND_FIXED_POINT_TAIL_BLIND_AT_FIXED_BACKGROUND_AND_P_LOC = NO_VERDICT |
  prerequisite: p_loc|Tail_ind=0
```

This is not a proof that the tail affects the fixed point. It is also not a
proof that the tail is inert. It is a proof that the current source words do
not decide which consumption rule `p_loc` has.

The Q-252 boundary remains load-bearing:

```text
p_loc|Tail_ind=0 would close the tail channel at fixed completed background;
it would not close the separate stationary-background channel.
```

Q-254 landed before sealing and bears directly. It packages `p_loc`, `Pi_loc`,
`B_ind`, `C_EM`, and `R_comp` as the unbuilt P9 local-projection consumer and
records the finite-authority principle as battery item B13. It does not type
`p_loc` into class (a), (b), or (c), so the determination above is unchanged.
It does change the commissioning order: P9 is downstream of the shared physical
layer, and the current first commissioning target is Q-254's
`SOURCE_GERM_PHYS`, not an authored `p_loc`.

No response, fixed point, stiffness, coupling, scale, or measured quantity is
evaluated.

## 1. Scope, currency, and authorities

### 1.1 Preflight

```text
DOES_THE_CERTIFICATE_EXIST = true
  Q-253 names p_loc|Tail_ind=0 as the exact certificate.

IS_THE_REGISTER_HEAD_CURRENT = true_through_Q_254
  The register ended at Q-253 when the run began. Q-254 landed before sealing,
  was read in its sealed artifact, and is incorporated in Sections 0, 1, 3,
  7, 8, and 10.

ARE_THE_INPUTS_PRESENT = true_for_lineage_and_typing_audit
  The p_loc lineage and the Q-247/Q-253 theorem statements are sealed.

ARE_THE_INPUTS_PRESENT_FOR_CERTIFICATE_PROOF = false | TYPE-U |
  would-build: RetHess_phys, physical restrictions, Tail_ind, and an
               instantiated p_loc consumption law on their common domain
```

### 1.2 Current authorities

`alpha_post_cleanroom_route_state_v002.md:16-26` appoints the v004 dimension
ledger, v004 symbolic spine, v004 record-cell selection principle, and v003
symbolic gate. The v004 projection principle supersedes v003 on its face.

| Authority | SHA-256 | Content used |
|---|---|---|
| `primitive_record_cell_selection_principle_v004.md` | `13d227ceb2198d96b0e4e2fef57b874cea71cb755320508fbf4c6d64a00c507e` | live signature, linearity, covariance, normalization, full-CTP extension |
| `primitive_zero_bare_induced_response_projection_principle_v004.md` | `d386bb74c28424a55a68a1bdb78108711537a7bc36ffffd1a76fe5ffd8a4eb80` | coefficient extraction after complete-kernel derivation and spectral/long-wavelength projection |
| `alpha_surface_symbolic_spine_v004.md` | `74a1d6224ed402e7f6622e0d1c2fe00a4f4311fba2897d7e162930e807b9573a` | global-kernel proviso and probe-support restriction |
| `alpha_complete_dimension_convention_ledger_v004.md` | `bbf2bdddfcefe851e985c4db03a62906082660af9a3c639d259afc93b4bbcc66` | domain `physical retarded action kernels` |
| `alpha_symbolic_first_proof_gate_v003.md` | `2ec93961c2e764cc7218dd24608af42fc2b7db2c61e5bb9b52a383df502ccabd` | unique target-independent projector remains a Step-5 derivation |
| `alpha_post_cleanroom_route_state_v002.md` | `a3ad6898f55456ec137acf2f3d5aee78ad3dc6c96091011e6695a69586c487b3` | active authority and route assignment |
| `STAGE8_TASK4A_FINITE_RESTRICTION_SEPARATION_AND_BIDUAL_TAIL_DETERMINATION_V001.md` | `60b5b4c5788eca2be2d9f11d67983b2e7a5823066cdabf9a734f7a59aae0ecd1` | Q-247 category-relative separation and bidual tail |
| `STAGE8_TASK4A_ALPHA_FACING_OUTPUT_TAIL_ANNIHILATION_THEOREM_DETERMINATION_V001.md` | `a71d4e59fcde1a7df10e8051e46befb9b4b6653a0917bb03a0c0403179717fef` | Q-251 unresolved p_loc consumption |
| `STAGE8_TASK4A_BIND_INPUT_SIGNATURE_AND_DOMAIN_TAIL_BLINDNESS_DETERMINATION_V001.md` | `790ae95bfa7f7747f383a387842939cb8f024d3e0107a9cbe15683666058c73f` | Q-253 exact reduction to p_loc on Tail_ind |
| `STAGE8_TASK4A_BACKGROUND_CHANNEL_STATIONARY_EVALUATION_POINT_DETERMINATION_V001.md` | `7cefd2c252e57c9ba63c2780c8cac308afb9b5670d189ea77293c5a2aa2cf3ae` | Q-252 background channel remains separate |
| `STAGE8_TASK4A_MISSING_PHYSICAL_LAYER_CONSOLIDATED_SPEC_AND_CONSTRAINT_BATTERY_V001.md` | `241bf43f04aed7f215bad6ea80170a9c7733000896df839ac80974769d0a46c3` | Q-254 P9 package, B9/B13, and commissioning order |
| `DECISION_OF_RECORD_008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER_2026-08-01_V001.md` | `d51a6d5c5bb0020a081cfd2adfb545b9f5ed86ce660d3feacadc5ef68140fb19` | finite-result authority and limit-only caveat at `:16-31` |
| `RELAY_PASTE_337_P_LOC_ON_THE_TAIL_V001.md` | `44a914cc5042e3dc97b93e37a503032453580f05f563b35117b118808ab93510` | commissioned alternatives and finite-authority test |

The parent program Markdown root, governing cleanroom root, supervision
register, DoR-008, and relay 337 were entered. `a32_holdout/custodian_private/`
was not entered, listed, searched, opened, or read.

## 2. Complete parent p_loc lineage

An exact word-boundaried `p_loc` search found twelve parent Markdown artifacts.
They form six paired lineages. Every occurrence is listed here; the older member
of each pair is retained only as superseded history.

| Artifact and lines | Standing | Sealed characterization | Consumption class supplied |
|---|---|---|---|
| `alpha_complete_dimension_convention_ledger_v003.md:306-320` | superseded by v004 | operator kernels of dimension `L^-6` to dimensionless scalars; scalar coefficient functional | `UNSPECIFIED` |
| `alpha_complete_dimension_convention_ledger_v004.md:355-389` | **live ledger** | physical retarded action kernels to dimensionless scalars; normalized projector | `UNSPECIFIED` |
| `alpha_post_cleanroom_route_state_v001.md:52-71` | historical route summary | derive a typed coefficient functional and projector | `UNSPECIFIED` |
| `alpha_post_cleanroom_route_state_v002.md:52-77` | **current route** | derive a typed coefficient functional and require the complementary residual to vanish | `UNSPECIFIED` |
| `alpha_surface_symbolic_spine_v003.md:95-129` | superseded by v004 | low-eigenvalue coefficient; scalar coefficient functional on complete response | `UNSPECIFIED` |
| `alpha_surface_symbolic_spine_v004.md:69-84,106-146` | **live spine** | low-eigenvalue covariant coefficient of the global retarded kernel; `D x D` is a probe restriction only | `UNSPECIFIED` |
| `alpha_symbolic_first_proof_gate_v002.md:48-71` | superseded by v003 | complete operator must derive normalized `p_loc` | `UNSPECIFIED` |
| `alpha_symbolic_first_proof_gate_v003.md:23-37,50-79` | **live gate** | complete physical operator must derive one unique covariant local coefficient functional | `UNSPECIFIED` |
| `primitive_record_cell_selection_principle_v003.md:85-120` | superseded by v004 | covariant linear functional from inverse-kernel operator to dimensionless coefficient | `UNSPECIFIED` |
| `primitive_record_cell_selection_principle_v004.md:125-168` | **live definition** | same linear normalized role, now on complete action-valued retarded response and every physical CTP block | `UNSPECIFIED` |
| `primitive_zero_bare_induced_response_projection_principle_v003.md:67-100` | superseded by v004 | coefficient of complete induced kernel after derivative expansion | `UNSPECIFIED` |
| `primitive_zero_bare_induced_response_projection_principle_v004.md:71-106` | **live projection definition** | derived spectral/long-wavelength separation of local `F^2` from complete kernel | `UNSPECIFIED` |

The exact source hashes, including the superseded members, are:

```text
e21c902c2ced578ad1a9179a6ea1144323066f1456de6ade6094eca1fab05fce  alpha_complete_dimension_convention_ledger_v003.md
bbf2bdddfcefe851e985c4db03a62906082660af9a3c639d259afc93b4bbcc66  alpha_complete_dimension_convention_ledger_v004.md
f3d5bb13999404200b3fbae8f297b078adaae226b28c97e8846628ee4d54fdfe  alpha_post_cleanroom_route_state_v001.md
a3ad6898f55456ec137acf2f3d5aee78ad3dc6c96091011e6695a69586c487b3  alpha_post_cleanroom_route_state_v002.md
9cd11b3f7f735c50ae63b40b15db802aa4c7d924d5f88537c9bcf6d8cb7b05b7  alpha_surface_symbolic_spine_v003.md
74a1d6224ed402e7f6622e0d1c2fe00a4f4311fba2897d7e162930e807b9573a  alpha_surface_symbolic_spine_v004.md
01644d023e875f3a3964f35bd3d652046badcaa50899b554012ae5d60ef3b8b0  alpha_symbolic_first_proof_gate_v002.md
2ec93961c2e764cc7218dd24608af42fc2b7db2c61e5bb9b52a383df502ccabd  alpha_symbolic_first_proof_gate_v003.md
3ea70741b15a2842e1103a1153ff397e7354ebef429258e889ba08db92b39982  primitive_record_cell_selection_principle_v003.md
13d227ceb2198d96b0e4e2fef57b874cea71cb755320508fbf4c6d64a00c507e  primitive_record_cell_selection_principle_v004.md
2fda20e2f9e68083e539f87d83db32f36626dc1758aee2bd723f81a7ffcd50fd  primitive_zero_bare_induced_response_projection_principle_v003.md
d386bb74c28424a55a68a1bdb78108711537a7bc36ffffd1a76fe5ffd8a4eb80  primitive_zero_bare_induced_response_projection_principle_v004.md
```

### 2.1 What changed across versions

The live repair narrows the **operator type**, not the consumption mechanism:

```text
v003: p_loc acts on inverse-kernel / K_ind shorthand;
v004: p_loc acts on physical retarded action kernels / Pi_R,ind.
```

The v004 ledger at `:370-380` makes that change explicit. The v004 selection
principle at `:149-155` additionally requires the complete operator to derive
the projection and extend it to every physical CTP block. The v004 projection
principle at `:140-157` still records

```text
unique_covariant_local_projection_derived = false |
  legacy source flag; current Q-54 type: TYPE-U
```

which is current Q-54 type `TYPE-U`: the role is specified, the instantiated
functional is unbuilt.

```text
P_LOC_ROLE_SPECIFIED = true
P_LOC_DOMAIN_BROADLY_TYPED = COMPLETED_PHYSICAL_RETARDED_ACTION_KERNELS
P_LOC_CODOMAIN_TYPED = DIMENSIONLESS_SCALARS
P_LOC_LINEARITY_AND_COVARIANCE_REQUIRED = true
P_LOC_NORMALIZATION_REQUIRED = p_loc[L_T]=1

P_LOC_INSTANTIATED = false | TYPE-U |
  would-build: derive the complete physical response class and one unique
               target-independent coefficient functional on it, including its
               topology, support/domain law, and all CTP-block extensions
```

## 3. Complete cleanroom characterization inventory

Fifteen sealed cleanroom artifacts contain exact-word `p_loc` hits. They add
typing and status; none supplies a competing functional or a consumption law.

| Artifact and bearing lines | Characterization | New consumption typing? |
|---|---|---|
| `STAGE8_C_RECORD_LIVE_DEFINITION_CURRENCY_AUDIT_V001.md:160-203` | v003/v004 residual currency | `NO | TYPE-S`; restatement only |
| `STAGE8_GAMMA_K_FINITE_REVERSIBLE_WRITE_OBS05_TEST_V001.md:221-230` | current `C_EM` application | `NO | TYPE-S`; restatement only |
| `STAGE8_GAMMA_K_RESPONSE_OPERATOR_CORRESPONDENCE_DETERMINATION_V001.md:348-409` | operator-to-scalar type; local projector unbuilt | `NO | TYPE-S`; signature only |
| `STAGE8_K_NORMALIZATION_IDENTITY_AND_SURROGATE_SLOT_ADVERSARIAL_VERIFICATION_V001.md:188-203` | normalization-slot check | `NO | TYPE-S`; normalization only |
| `STAGE8_ONE_SEAM_OR_THREE_SEAMS_ADJUDICATION_V001.md:137-158` | external response-side, not finite/discrete | `NO | TYPE-S`; sector only |
| `STAGE8_P1_P7_CONSUMER_STRUCTURE_REQUIREMENT_AUDIT_V001.md:360-385` | p_loc follows complete induced kernel and derived covariant limit | `NO | TYPE-S`; dependency only |
| `STAGE8_P5_SECTOR_ASSIGNMENT_V001.md:181-198` | p_loc belongs to external completed response package | `NO | TYPE-S`; sector only |
| `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:281-288,468-496,1052` | downstream scalarization on retarded operator; unbuilt | `NO | TYPE-S`; domain/codomain only |
| `STAGE8_RESPONSE_STATE_FACTORIZATION_TEST_FIXTURE_RESULT_V001.md:382-390` | state-blind at fixed operator input | `NO | TYPE-S`; state port only |
| `STAGE8_SECTOR_REACH_REQUIREMENT_V001.md:180-187,726-733` | external response-side and dimensionless | `NO | TYPE-S`; sector only |
| `STAGE8_TASK2D_ALPHA_CHAIN_STATE_IDENTITY_DEPENDENCY_AUDIT_V001.md:273-323` | operator-geometric at fixed input; state variation may survive | `NO | TYPE-S`; state dependence only |
| `STAGE8_TASK4A_RESPONSE_CLASS_FORCING_AND_TAIL_OUTPUT_INERTNESS_DETERMINATION_V001.md:438-450` | complete-operator map; restriction factorization absent | `NO | TYPE-S`; records the same gap |
| `STAGE8_TASK4A_ALPHA_FACING_OUTPUT_TAIL_ANNIHILATION_THEOREM_DETERMINATION_V001.md:177-212` | normalization leaves tail action open | `NO | TYPE-S`; Q-251 gap statement |
| `STAGE8_TASK4A_BIND_INPUT_SIGNATURE_AND_DOMAIN_TAIL_BLINDNESS_DETERMINATION_V001.md:287-315,317-382` | completed domain and exact `p_loc(t_ind)` reduction | `NO | TYPE-S`; Q-253 reduction only |
| `STAGE8_TASK4A_MISSING_PHYSICAL_LAYER_CONSOLIDATED_SPEC_AND_CONSTRAINT_BATTERY_V001.md:372-407,549-562,588-600` | P9 packages the local consumers; B9/B13 bind; Q-254 leaves the projection unbuilt | `NO | TYPE-S`; package and battery only |

Here `NO | TYPE-S` means the named artifact contains no additional consumption
definition within the line scope stated in the row. It is not a claim that the
artifact lacks useful content.

## 4. What the live word local means

### 4.1 Output locality is sealed

`primitive_record_cell_selection_principle_v004.md:134-145` calls `p_loc` a
covariant linear coefficient functional and defines its image through

```text
p_loc[L_T]=1,
iota_loc(b)=b L_T,
Pi_loc=iota_loc compose p_loc.
```

The returned scalar is the coefficient of the normalized local Maxwell kernel.
The operator projector has one-dimensional image `span{L_T}`. This is a precise
locality statement about the selected tensor/derivative channel.

### 4.2 Input locality is not sealed

The same live lineage puts the input in the completed global response layer:

1. `alpha_complete_dimension_convention_ledger_v004.md:370-380` types the domain
   as physical retarded action kernels.
2. `primitive_record_cell_selection_principle_v004.md:149-155` requires
   extension to every physical CTP block.
3. `primitive_zero_bare_induced_response_projection_principle_v004.md:81-100`
   starts only after the complete induced kernel and its low-eigenvalue
   derivative expansion are derived.
4. `alpha_surface_symbolic_spine_v004.md:69-84` calls the global kernel primary
   and expressly limits `D x D` to probe support.
5. `alpha_complete_dimension_convention_ledger_v004.md:292-309` keeps the
   unrestricted retarded term on `D x M`; support in `D` does not turn a global
   common history into a field supported in `D`.

Accordingly:

```text
PROBE_SUPPORT_RESTRICTION_EQUALS_Q247_FINITE_STAGE_RESTRICTION = false | TYPE-R |
  test: the live spine expressly calls D x D a probe restriction and keeps the
        unrestricted global kernel primary

LOW_EIGENVALUE_LONG_WAVELENGTH_PROJECTION_EQUALS_FINITE_RESTRICTION = false | TYPE-R |
  test: the live projection principle applies the limit only after the complete
        induced kernel is derived and uses it to separate derivative orders

P_LOC_LOCAL_LABEL_IMPLIES_FINITE_SHADOWED_CONSUMPTION = false | TYPE-R |
  test: the sealed definition fixes the image channel but provides no
        factorization p_loc=p_tilde compose R_fin; the two explicit candidate
        finite readings above fail their own source signatures
```

The classification is therefore not ambiguous between finite-stage and
completed-stage. `p_loc` is completed-stage. What is untyped is the topology and
information path **within** that completed stage.

## 5. The four-way classification

### 5.1 Class (a): finite-shadowed

The needed definition would have to exhibit a physical restriction family

```text
R_fin(H)=(rho_H,N(H))_N
```

and a functional `p_tilde` such that

```text
p_loc = p_tilde compose R_fin.
```

The live sources display neither equation. Probe support and a long-wavelength
coefficient extraction do not supply it.

```text
P_LOC_CLASS_A_FINITE_SHADOWED = NO_VERDICT |
  prerequisite: instantiate rho_H,N and derive the displayed factorization
```

### 5.2 Class (b): norm/module class

Q-247 proves separation on the ratified norm C-star algebra, standard Hilbert
module, and represented adjointable left multipliers. Transport to the physical
response requires `RetHess_phys` membership and identification of the physical
restriction maps with Q-247's retractions. The `p_loc` lineage supplies neither.

```text
P_LOC_CLASS_B_NORM_MODULE = NO_VERDICT |
  prerequisite: type Dom(p_loc) inside Q-247's separated class and certify the
                physical restriction square
```

### 5.3 Class (c): weak-star/bidual-capable

Q-247 proves the mathematical bidual tail

```text
Tail_B**=M_cyl(Y)^perp=z_tail B**
```

and exhibits a bounded functional that detects one moving-tail witness. It does
not identify that mathematical tail with `Tail_ind`, type `p_loc` as a bidual
pairing, or place the physical retarded Hessian in `B**`.

```text
P_LOC_CLASS_C_BIDUAL_CAPABLE = NO_VERDICT |
  prerequisite: instantiate a physical bidual response class, Tail_ind in it,
                and the pairing by which p_loc consumes that class
```

### 5.4 Class (d): unspecified

Class (d) is the corpus verdict. The role, domain family, codomain, linearity,
covariance, and normalization are specified. The consumption topology,
restriction factorization, and tail pairing are not.

```text
P_LOC_CLASS_D_CONSUMPTION_UNSPECIFIED = UNSPECIFIED | TYPE-S |
  roots: Section 1.2 |
  excl: Section 0 |
  fences: DoR-011 reading/proof only |
  query: Section 0 exact queries, read in context across every file in Sections
         2 and 3
```

## 6. Certificate adjudication

Q-253 proves, at fixed background and fixed functional,

```text
B_ind^(t)(K)-B_ind(K)=p_loc(t_ind),

B_ind tail-blind on Tail_ind
  iff p_loc(t_ind)=0 for every t_ind in Tail_ind
  iff p_loc factors through the induced-response quotient by Tail_ind.
```

Linearity exposes the exact test. It does not settle it. The normalization
`p_loc[L_T]=1` fixes one value on one non-tail reference direction and supplies
no value on `Tail_ind`.

If class (a) were derived, then for `t_ind in Tail_ind`,

```text
R_fin(t_ind)=0
=> p_loc(t_ind)=p_tilde(0)=0.
```

If class (b) were derived and the physical tail were the common kernel in the
Q-247 separated class, then

```text
t_ind=0
=> p_loc(t_ind)=0.
```

Neither antecedent is sealed. Class (c) would permit a nonzero tail pairing but
is likewise uninstantiated. The lawful conclusion is:

```text
P_LOC_RESTRICTION_TO_TAIL_IND_DERIVED = false | TYPE-U |
  would-build: class (a) factorization or class (b) membership/restriction
               certificate on an instantiated physical response class

P_LOC_RESTRICTION_TO_TAIL_IND_REFUTED = NO_VERDICT |
  prerequisite: class (c) or another lawful completed consumer and one admitted
                t_ind with nonzero pairing

TAIL_CHANNEL_INTO_B_IND = NO_VERDICT
BACKGROUND_CHANNEL_INTO_B_IND = NO_VERDICT
```

## 7. The two authored versions for principal consideration

These are specifications of the two lawful choices requested by relay 337.
They are not implementations, derivations, adoptions, or recommendations.
Under Q-254 they are future P9 typing alternatives, not the current
commissioning target; P1-P6 and P8 must expose the physical class, restrictions,
tail, and background before either can lawfully become an instantiated consumer.

### 7.1 Candidate F: finite-shadowed p_loc

```text
P_LOC_FINITE_SHADOWED_ADOPTION_CANDIDATE
status = PROPOSED_NOT_ADOPTED
derived = false | TYPE-U |
  would-build: derive the fully instantiated factorization and certificates;
               adoption alone would remain a premise

data:
  1. an instantiated physical response class R_phys_class;
  2. physical finite restrictions rho_H,N;
  3. R_fin(H)=(rho_H,N(H))_N;
  4. one named topology tau_fin on Im(R_fin);
  5. one covariant linear tau_fin-continuous coefficient functional p_tilde;
  6. p_loc^F := p_tilde compose R_fin;
  7. p_loc^F[L_T]=1 and target-independent freeze before output;
  8. CTP reality, Ward, support, boundary, domain, and regulator certificates.

consequence:
  p_loc^F|Tail_ind=0 by factorization;
  at fixed background and fixed p_loc^F, B_ind is tail-blind;
  the separate background channel remains open.
```

This is the minimal authored version that proves the requested certificate. It
does not follow merely from naming a finite region; the physical restriction
maps and topology are load-bearing fields.

### 7.2 Candidate W: bidual-capable p_loc

```text
P_LOC_BIDUAL_CAPABLE_ADOPTION_CANDIDATE
status = PROPOSED_NOT_ADOPTED
derived = false | TYPE-U |
  would-build: derive the fully instantiated physical tail pairing and
               certificates; adoption alone would remain a premise

data:
  1. an instantiated physical response class R_phys_class containing a declared
     weak-star/bidual completion;
  2. physical restrictions rho_H,N and a physical Tail_ind;
  3. a certified embedding or identity placing Tail_ind in that completion;
  4. a declared cylindrical/finite-shadowed component p_cyl;
  5. a declared tail projection or splitting H=H_cyl+t;
  6. a covariant linear tail functional ell_tail with
       ell_tail(t)!=0 for at least one admitted t in Tail_ind;
  7. p_loc^W(H_cyl+t):=p_cyl(H_cyl)+ell_tail(t);
  8. p_loc^W[L_T]=1 and target-independent freeze before output;
  9. CTP reality, Ward, support, boundary, domain, regulator, and physical
     provenance certificates for ell_tail.

consequence:
  B_ind^(t)(K)-B_ind(K)=ell_tail(t_ind) can be nonzero;
  the tail is a physical input to the fixed-point map at fixed background.
```

The splitting and `ell_tail` are part of the authorship price. Omitting either
would hide the actual choice. Q-247's mathematical `B**` witness shows this
shape is consistent mathematics; it does not supply the physical embedding or
the physical functional.

### 7.3 Why these are the honest two readings

Candidate F makes the completion answerable to finite shadows and proves the
certificate. Candidate W permits a completion-level response invisible to all
finite restrictions and therefore exposes a tail term. The current source
language is compatible with either because it specifies only the output tensor
channel.

```text
SEALED_TEXT_SELECTS_CANDIDATE_F = false | TYPE-S |
  roots: Section 1.2 | excl: Section 0 | fences: DoR-011 |
  query: exact class-(a) terms in Section 0

SEALED_TEXT_SELECTS_CANDIDATE_W = false | TYPE-S |
  roots: Section 1.2 | excl: Section 0 | fences: DoR-011 |
  query: exact class-(c) terms in Section 0

FUTURE_P9_TYPING_DECISION_REQUIRED_IF_DERIVATION_IS_NOT_COMMISSIONED = true
CURRENT_COMMISSIONING_TARGET = SOURCE_GERM_PHYS | Q-254
```

## 8. Finite-authority battery

DoR-008`:18-22` requires every completed framework to reproduce every sealed
finite result on restriction and makes finite results authoritative. Its stated
basis at `:26-31` also recognizes that some quantities live only at the limit
and require their own theorems.

Q-254`:588-600` makes the output-side rule explicit as B13: a consumer may not
see tail physics merely because finite theory leaves it unconstrained; any
tail-sensitive term needs declared physical provenance and must survive B1-B12.

Candidate F aligns its consumer with finite shadows by construction. Candidate
W can still reproduce every finite restriction because its tail term is killed
there. Therefore finite-restriction agreement alone does not refute Candidate
W. Q-250 already proves this modulo-tail freedom.

The finite-authority consequence is stricter than simple agreement:

> An authored `p_loc` that sees `Tail_ind` imports non-finite physics into the
> map that defines `B_ind`. Finite silence is not provenance for that term.

Such a consumer would need an independent physical origin, declared before any
output, and would have to survive the full support/reality/Ward/boundary/domain,
restriction, and target-independence battery. This is a new premise, not an
interpretation of existing finite data.

```text
BIDUAL_CAPABLE_P_LOC_AUTOMATICALLY_VIOLATES_DOR008_RESTRICTION_TEST = false | TYPE-R |
  test: every Tail_ind element is killed by every physical finite restriction,
        so a tail term can leave all finite verdicts unchanged

BIDUAL_CAPABLE_P_LOC_HAS_FINITE_AUTHORITY_PROVENANCE = false | TYPE-U |
  would-build: a target-independent microscopic/completed origin for the tail
               pairing, plus every finite-restriction and physical-domain
               certificate

FINITE_RESTRICTION_SILENCE_AUTHORIZES_TAIL_SENSITIVE_P_LOC = false | TYPE-R |
  test: DoR-008 makes the completion answerable to finite results and reserves
        limit-only claims for separate theorems; it supplies no positive origin
        for restriction-invisible content
```

## 9. Kill-passes

### 9.1 The name local does no hidden work

No inference uses the substring `local`. The source-defined image, domain, and
global-kernel proviso were read separately.

```text
LOCAL_SUBSTRING_USED_AS_CONSUMPTION_TYPING = false | TYPE-R |
  test: classification follows the displayed domain, image, and global-kernel
        statements, not the shared word
```

### 9.2 No topology switch

Finite-shadowed, norm/module, and weak-star/bidual readings remain separate.
The Q-247 bidual witness is never transported into the physical response class.

```text
TOPOLOGY_CHANGED_MID_ARGUMENT = false | TYPE-R |
  test: every implication names finite-shadow, norm/module, or weak-star/bidual
        topology before use
```

### 9.3 No normalization overreach

`p_loc[L_T]=1` fixes one direction. It neither annihilates nor detects
`Tail_ind`.

```text
NORMALIZATION_EXTENDED_TO_TAIL_WITHOUT_PROOF = false | TYPE-R |
  test: every tail verdict remains NO_VERDICT unless a factorization or witness
        is supplied
```

### 9.4 No physical tail manufactured

`Tail_ind` remains a conditional physical subspace. The mathematical tail
`z_tail B**` is not identified with it.

```text
MATHEMATICAL_BIDUAL_TAIL_IDENTIFIED_WITH_PHYSICAL_TAIL = false | TYPE-R |
  test: Candidate W lists the embedding/identity as an authored required field
```

### 9.5 No background collapse

The result is at fixed completed background and fixed `p_loc`. Q-252's
stationary-background channel remains open.

```text
TAIL_CHANNEL_IDENTIFIED_WITH_BACKGROUND_CHANNEL = false | TYPE-R |
  test: the former varies a common-kernel summand at fixed G_K; the latter
        varies G_K and may change finite restrictions
```

### 9.6 No principal act performed

Candidates F and W are `PROPOSED_NOT_ADOPTED`. This lane selects neither and
does not add a premise.

```text
PRINCIPAL_ACT_PERFORMED = false | TYPE-R |
  test: every candidate flag is PROPOSED_NOT_ADOPTED and no source flag is
        changed by this artifact
```

## 10. Final verdict and would-build

```text
P_LOC_LIVE_ROLE = COVARIANT_LINEAR_LOCAL_MAXWELL_COEFFICIENT_FUNCTIONAL
P_LOC_LIVE_DOMAIN = COMPLETED_PHYSICAL_RETARDED_ACTION_KERNELS
P_LOC_LIVE_CODOMAIN = DIMENSIONLESS_SCALARS
P_LOC_LOCALITY_SCOPE = OUTPUT_TENSOR_DERIVATIVE_CHANNEL
P_LOC_INPUT_CONSUMPTION = UNSPECIFIED

P_LOC_FINITE_SHADOWED = NO_VERDICT
P_LOC_NORM_MODULE_CLASS = NO_VERDICT
P_LOC_BIDUAL_CAPABLE = NO_VERDICT

P_LOC_TAIL_ANNIHILATION_CERTIFICATE_DERIVED = false | TYPE-U |
  would-build:
    1. instantiate RetHess_phys and rho_H,N;
    2. instantiate Tail_ind on that physical class;
    3. derive p_loc target-independently on the same class;
    4. prove Candidate-F factorization or class-(b) membership and
       physical separation;
    5. otherwise exhibit and certify a lawful nonzero tail pairing;
    6. run all finite-authority and physical-domain certificates.

P_LOC_TAIL_ANNIHILATION_CERTIFICATE_REFUTED = NO_VERDICT
B_IND_FIXED_POINT_TAIL_BLIND_AT_FIXED_BACKGROUND = NO_VERDICT
B_IND_FIXED_POINT_TAIL_SENSITIVE_AT_FIXED_BACKGROUND = NO_VERDICT
STATIONARY_BACKGROUND_CHANNEL = OPEN | Q-252

FUTURE_P9_TYPING_PACKAGE =
  CANDIDATE_F_FINITE_SHADOWED versus CANDIDATE_W_BIDUAL_CAPABLE

CURRENT_COMMISSIONING_TARGET = SOURCE_GERM_PHYS | Q-254
P_LOC_AUTHORSHIP_BEFORE_Q254_UPSTREAM_PACKAGES = false | TYPE-C |
  constraint: Q-254 commissioning order |
  release: instantiate P1-P6 and P8, then select P9 by road relevance rather
           than desired output

REGISTER_HEAD_AT_START = Q-253
REGISTER_HEAD_AT_COMPLETION = Q-254
LATER_BEARING_RULING_OBSERVED_DURING_RUN = true | Q-254 |
  effect: P9 and B13 sharpened; consumption classification unchanged;
          current commissioning target moved upstream to SOURCE_GERM_PHYS

FENCE_BLOCKED_STRUCTURAL_RESULT = NONE
MACHINERY_APPEAL = NOT_TRIGGERED

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

Custody: seal this artifact, verify its sidecar, mirror both files to
`/Users/bgm/MB Work/alpha-program-archive/workspace/`, report, and stop. No
register, git, commit, push, gate, or deploy act is performed by this lane.
