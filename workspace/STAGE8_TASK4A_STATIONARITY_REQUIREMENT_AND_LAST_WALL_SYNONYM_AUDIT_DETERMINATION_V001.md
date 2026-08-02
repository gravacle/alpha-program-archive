# Stage 8 Task 4a Stationarity Requirement and Last-Wall Synonym Audit Determination V001

Date: 2026-08-02  
Lane: CODEX LANE 1  
Task: 4a  
Relay: PASTE 396 V003  
Register head at start and completion: Q-313  
Status: SEALED-SOURCE AUDIT COMPLETE; PHYSICAL-EVALUATION SCOPE EMPTY | TYPE-S

```text
alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead determination

### 0.1 New classes required by the sealed signatures

Two requested outputs do not fit the relay's three evaluation categories because
their definitions contain no background-evaluation slot. This is a category
finding under Q-80, not missing information.

```text
NEW_CLASS_1 = BACKGROUND_AGNOSTIC_OPERATOR_FUNCTIONAL
definition:
  a map whose sealed signature acts on an operator or coefficient space and
  neither receives nor selects a background evaluation point
member:
  p_loc
resists_existing_categories:
  stationary/on-shell, declared-reference, and unspecified-evaluation all
  presuppose an evaluation-point argument that p_loc does not have

NEW_CLASS_2 = BACKGROUND_INAPPLICABLE_FINITE_QUOTIENT
definition:
  a finite source-state or outgoing-record quotient whose domain contains no
  physical background, completed response, or evaluation-point variable
members:
  response-visible p_ch quotient; outgoing-record-visible p_ch quotient
resists_existing_categories:
  the quotient is already completely typed on a different carrier, so
  'evaluation unspecified' would falsely turn a scope boundary into missing data
```

### 0.2 Overall verdict

**STATIONARITY IS REQUIRED by the live sealed value path.** The active v004
definition makes `B_ind(K)` a functional of `Pi_R,ind[G_K]` at a candidate
normalized saddle and requires the valid saddle to satisfy the full residual plus
source, metric, Gauss, record-effect, interval, and boundary stationarity. The
first-record phase is evaluated only after the first durable record solves the
full Dyson, source/metric/constraint, boundary, and public-closure equations.

```text
VERDICT_PATH = STATIONARITY_REQUIRED

SEALED_VALUE_PATH_REQUIRES_STATIONARY_ON_SHELL_EVALUATION = true
  witnesses: B_ind(K), DeltaPhi[K;X_K]
  authority: primitive_record_cell_selection_principle_v004.md:127-166,186-206

ALL_ALPHA_FACING_OUTPUTS_REQUIRE_STATIONARITY = false | TYPE-R |
  test: p_loc has no evaluation-point argument; kappa_Thomson uses the distinct
        complete-amplitude A=0 reference; both quotients live on finite state or
        record carriers

Q252_FINITE_NO_STATIONARY_POINT_REMOVES_COMPLETE_STATIONARITY = false | TYPE-R |
  test: Q-252:51-55 expressly limits the finite theorem to the relative-history
        phase summand and leaves common-history, field, metric, boundary, record,
        and source terms outside that theorem

C1_REFERENCE_DISCHARGES_V004_STATIONARY_SADDLE = false | TYPE-R |
  test: C1 is the a=0 operator-reduction certificate; v004 requires a completed
        source-free stationary 2PI solution and full first-record residual

C1_PLUS_FORCED_STATE_INSTANTIATES_THOMSON_REFERENCE = false | TYPE-R |
  test: V011 requires a distinct complete Q_spec charged amplitude; C1 plus the
        forced state supplies neither that amplitude nor its Ward, regulator,
        threshold, and limit package

LAST_WALL_IS_ONE_UNDIFFERENTIATED_STATIONARY_OBJECT = false | TYPE-R |
  test: the background and 2PI blocks are stationarity objects; the common
        completed domain and restriction/Tail squares are transport
        infrastructure with independent signatures
```

The synonym test returns zero built identifications. The gap count therefore
stays four, now typed as two stationary physics objects plus two
transport-infrastructure objects.

```text
POST_DEDUP_UNBUILT_OBJECT_COUNT = 4
POST_DEDUP_STATIONARY_CORE_COUNT = 2
POST_DEDUP_TRANSPORT_INFRASTRUCTURE_COUNT = 2
SYNONYM_COLLAPSE_COUNT = 0 | TYPE-R |
  test: all four candidate identifications fail the carrier/signature or
        instantiated-object test in Section 5
```

## 1. Preflight, roots, and frozen authorities

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = true
  object: the evaluation-requirement and synonym questions

IS_THE_VERSION_CURRENT = true
  register head: Q-313
  Q-313 artifact: STAGE8_TASK4A_RELATIVE_HISTORY_CYCLE_FACTORIZATION_AND_2PI_DESCENT_VERDICT_BUILD_V001.md

ARE_ITS_INPUTS_PRESENT = true
  inputs: live v004, historical v002, V011, Q-252, Q-251 output audit,
          Q-257 P7, Q-288 ledger, Q-309/Q-313, Q-281 background audit,
          DoR-015/V005, Q-239, Q-278, and P2 V002
```

### 1.2 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003/
/Users/bgm/MB Work/alpha_supervision/
/Users/bgm/MB Work/alpha-program-archive/workspace/
```

### 1.3 Exclusions and acts not performed

```text
a32_holdout/custodian_private/                       NOT ENTERED | TYPE-S
physical response, coupling, root, or value evaluation NOT PERFORMED | TYPE-S
comparison to any measured constant                  NOT PERFORMED | TYPE-S
rank, background, contour, or extension selection    NOT PERFORMED | TYPE-S
register, plan, tracker, git, commit, push, deploy   NOT TOUCHED | TYPE-S
```

### 1.4 Frozen hashes

| Authority | SHA-256 | Use |
|---|---|---|
| `alpha_supervision/LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | process, fences, typing |
| `alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md` | `92fe0933c02e37feec6208a0c786f7a28e2628049ae6fe299a172a7aa22ba730` | Q-313 head |
| `alpha_supervision/DECISION_OF_RECORD_015_FIELD_SIGNATURE_PHYS_RATIFIED_2026-08-02_V001.md` | `617bd51a70860d2cfb2066640630ba37ec289d56255ebbe1433bc0dfcba0159d` | adopted external-background family and opened lift fiber |
| `primitive_record_cell_selection_principle_v004.md` | `13d227ceb2198d96b0e4e2fef57b874cea71cb755320508fbf4c6d64a00c507e` | active zero-bare 2PI, B_ind, saddle, first-record requirement |
| `primitive_complete_boundary_transition_functional_principle_v002.md` | `be79ca5e08010b53285cd157ba4c18d2029f08bc93bea2db02d5423b67428c34` | earlier stationary-history and on-shell-cell wording |
| `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `20a3a17d44e15841baded9eaed3fdbecfde0ecb14bdb8162ea41a8bcd21d1a48` | complete Thomson reference |
| `STAGE8_TASK4A_BACKGROUND_CHANNEL_STATIONARY_EVALUATION_POINT_DETERMINATION_V001.md` | `7cefd2c252e57c9ba63c2780c8cac308afb9b5670d189ea77293c5a2aa2cf3ae` | Q-252 finite/complete split and three-zero distinction |
| `STAGE8_TASK4A_ALPHA_FACING_OUTPUT_TAIL_ANNIHILATION_THEOREM_DETERMINATION_V001.md` | `a71d4e59fcde1a7df10e8051e46befb9b4b6653a0917bb03a0c0403179717fef` | sealed output signatures and quotient domains |
| `STAGE8_TASK4A_P7_FINITE_CORE_SEPARATION_T5_COMMUTING_SQUARE_CERTIFICATE_V001.md` | `07205bf5e1888bd39a97d4e86543852d5e9b88b103e5c0b429c76bd77290d6be` | conditional P7 theorem and unbuilt physical maps |
| `STAGE8_TASK4A_P5_MAXIMAL_TRANSPORT_CHAIN_AND_DEPENDENCE_ACCOUNTING_PACKAGE_V002.md` | `31a738ec17696ea01e1cb6a6ee7a37a29e6c0ca24d6fb8cc050d06aed32a583f` | Q-288 field, Schur, restriction, and Tail accounts |
| `STAGE8_TASK4A_KERNEL_SECTOR_DYNAMICS_2PI_DOMAIN_BACKGROUND_AND_P_VERDICT_DETERMINATION_V001.md` | `a4c916a7cfa82c2130c82d8947c869f118e224959d7824bba45695711b4919c3` | Q-309 two-sector/source block and distinctions |
| `STAGE8_TASK4A_ANCHORED_ORIGIN_TO_PHYSICAL_BACKGROUND_MAP_IDENTIFICATION_DETERMINATION_V001.md` | `f893d210191551bd8b6af060f85a73510f8119171c8709c46e925a6708314ed2` | Q-281 seed versus physical pair and lift fiber |
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md` | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | ratified external-background family and unbuilt stationary member |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U3_DOR008_DOR009_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` | `b0118d89e0b4b321fbf9caab5bfb811a0b5fd572e808d02615ee8503db2bc1ac` | Q-239 field (4), bounded and unbounded domain split |
| `STAGE8_TASK4A_P3_LAW_SIDE_SUBPACKAGE_CROSS_VERIFICATION_DETERMINATION_V001.md` | `aaff995613e60fdf792473dcb8d3ffefcc2390428f4e6aa21ea9fef12ec97e27` | Q-278 bounded-domain scope |
| `STAGE8_TASK4A_P2_PHYSICAL_SOURCE_TOPOLOGY_AND_DIFFERENTIAL_CALCULUS_CONSTRUCTION_V002.md` | `40b2af34443e051fffdc7bf2ec7025c811a98c501a82d19164596ee6f37f00c1` | source topology and closures |
| `STAGE8_TASK4A_RELATIVE_HISTORY_CYCLE_FACTORIZATION_AND_2PI_DESCENT_VERDICT_BUILD_V001.md` | `ea8f4e9a79a9e4aca4a0b9e9aab470d78cd4d9c78794c20d9e979c0db16fbeab` | Q-313 last-wall statement and Map 1 |

## 2. Per-output evaluation-requirement table

| Output | Sealed defining text | Actual evaluation structure | Is C1 plus forced state an instance? | Determination |
|---|---|---|---|---|
| `p_loc` | v004:125-150: covariant linear coefficient functional, `p_loc[L_T]=1` | **NEW CLASS: BACKGROUND_AGNOSTIC_OPERATOR_FUNCTIONAL** | Not applicable: no evaluation-point port | `BACKGROUND_EVALUATION_SLOT_EXISTS=false | TYPE-S` |
| `B_ind(K)` | v004:127-166: `G_K` candidate normalized saddle; `B_ind=p_loc[Pi_R,ind[G_K]]`; valid saddle carries full stationarity | **STATIONARY/ON-SHELL** | No; C1 does not supply `G_K` or full residual | `STATIONARITY_REQUIRED=true` |
| `DeltaPhi[K;X_K]` | v002:93-104 and v004:186-206: complete on-shell cell / first durable record after full equations | **STATIONARY/ON-SHELL** | No; C1 is not `X_K` or a first durable record | `STATIONARITY_REQUIRED=true` |
| `kappa_Thomson` | V011:1587-1655: complete `Q_spec`; `Z_Q[A]/Z_Q[0]`; branch at `A=0`; transverse coefficient and `q^2->0` limit | **DECLARED REFERENCE** | No; the required complete charged amplitude and its checks are absent from C1 | `DECLARED_REFERENCE_REQUIRED=true` |
| response-visible quotient | Q-251 output audit: finite `C_src=span{P_0,P_ch}` and `p_ch=omega(P_ch)` | **NEW CLASS: BACKGROUND_INAPPLICABLE_FINITE_QUOTIENT** | Not applicable | `BACKGROUND_EVALUATION_SLOT_EXISTS=false | TYPE-S` |
| outgoing-record-visible quotient | Q-251 output audit: finite source state and outgoing-record marginal | **NEW CLASS: BACKGROUND_INAPPLICABLE_FINITE_QUOTIENT** | Not applicable | `BACKGROUND_EVALUATION_SLOT_EXISTS=false | TYPE-S` |

### 2.1 `p_loc`: map-level structure, not an evaluation prescription

The active definition is:

```text
p_loc[L_T] = 1,
iota_loc(b) = b L_T,
Pi_loc = iota_loc compose p_loc.
```

The same section types `p_loc` as a covariant linear coefficient functional
from an inverse-kernel operator to a dimensionless coefficient. Its required
future data concern the operator domain, projection, and any pairing used for
orthogonality. No `Abar`, `G_*`, `G_K`, `X_K`, or reference-point argument
occurs in the signature.

```text
P_LOC_REQUIRES_STATIONARY_BACKGROUND = false | TYPE-S |
  scope: p_loc's own signature

P_LOC_EVALUATION_STRUCTURE_UNSPECIFIED = false | TYPE-R |
  test: the definition is complete enough to show that evaluation-point data
        are inapplicable, not missing
```

This does not make `B_ind` background-free: `B_ind` applies `p_loc` to an
operator already evaluated on `G_K`.

### 2.2 `B_ind`: stationary saddle required by the live definition

The active text states:

```text
Let G_K be a candidate normalized saddle ...
B_ind(K) = p_loc[Pi_R,ind[G_K]],
C_EM(K)  = p_loc[R_phys[G_K]] = K - B_ind(K).
```

It immediately says that the scalar equation is only a necessary projected
consequence and that a valid saddle must also satisfy `R_comp[G_K]=0` together
with source, metric, Gauss, record-effect, interval, and boundary stationarity
(v004:127-168). The same file defines the stationary 2PI-to-1PI reduction at
`G_*(Abar)` (v004:170-180).

```text
B_IND_REQUIRES_STATIONARY_ON_SHELL_INPUT = true
B_IND_CAN_BE_EVALUATED_FROM_C1_REFERENCE_ALONE = false | TYPE-R |
  test: C1 supplies neither G_K nor the full Dyson/complementary residual and
        stationarity package
B_IND_CAN_BE_EVALUATED_FROM_FORCED_STATE_ALONE = false | TYPE-R |
  test: the state is an input to the generating functional, not the solved
        physical propagator
```

### 2.3 `DeltaPhi`: on-shell first-record cell required

Historical v002 states:

```text
For a coupling-indexed on-shell cell X_K,
C_record(K) = Delta Phi[K;X_K] - pi,
...
the complete coupled saddle must supply X_K and the action partition.
```

The active v004 carries the requirement in zero-bare language:

```text
The first durable record is a simultaneous solution of the full Dyson,
source/metric/constraint, boundary, and public-closure equations. A phase
condition such as Delta Phi=pi can identify the first orthogonal comparison
only after the complete generator supplies the physical spectral gap.
```

Its authorization list requires one stationary first-record interval
(v004:198-207).

```text
DELTAPHI_REQUIRES_COMPLETE_ON_SHELL_FIRST_RECORD = true
DELTAPHI_C1_REFERENCE_IS_X_K = false | TYPE-R |
  test: C1 reduces the finite law at zero connection; X_K is the complete
        coupled saddle and first-record solution
DELTAPHI_FORCED_STATE_IS_X_K = false | TYPE-R |
  test: state identity and solved on-shell cell have different signatures
```

### 2.4 `kappa_Thomson`: a distinct declared reference, not the v004 saddle

V011 defines the complete charged specification as a distinct sealed object
`Q_spec` and then defines:

```text
Z_Q[A]/Z_Q[0],
Gamma_Q[A] = -i Log(Z_Q[A]/Z_Q[0]),
```

with the logarithm branch fixed continuously at `A=0`. The transverse
quadratic response and its finite path-independent limit are then defined at
V011:1621-1635. Pass additionally requires the Ward identity,
gauge-parameter independence, regulator independence, and threshold matching.

```text
KAPPA_THOMSON_REQUIRES_STATIONARY_2PI_BACKGROUND = false | TYPE-S |
  scope: V011's own definition
KAPPA_THOMSON_REQUIRES_DECLARED_A0_REFERENCE = true
KAPPA_THOMSON_COMPLETE_QSPEC_PRESENT = false | TYPE-U |
  would-build: the distinct complete physical charged transition amplitude
               and its Ward/regulator/threshold/limit package
C1_AND_FORCED_STATE_DISCHARGE_QSPEC = false | TYPE-R |
  test: finite operator reduction plus a source-state datum does not construct
        the complete charged transition amplitude
```

The notation `A=0` is shared, but the mathematical roles are not. C1 is a
reduction of the finite law. V011's `A=0` is the branch/reference point of a
complete normalized charged amplitude.

### 2.5 The two quotients: background evaluation is inapplicable

The response-visible quotient consumes the finite source algebra
`span_C{P_0,P_ch}` and retains `p_ch=omega(P_ch)`. The outgoing-record-visible
quotient consumes finite source states and returns the outgoing-record marginal
with the same visible scalar. Neither domain contains `RetHess_phys`, `G_K`,
`X_K`, or a physical background.

```text
VISIBLE_QUOTIENTS_REQUIRE_STATIONARY_BACKGROUND = false | TYPE-S |
  scope: their sealed finite state/record domains
VISIBLE_QUOTIENTS_REQUIRE_DECLARED_BACKGROUND_REFERENCE = false | TYPE-S |
  scope: their sealed finite state/record domains
VISIBLE_QUOTIENTS_ARE_COMPLETE_ALPHA_RESPONSE_OUTPUTS = false | TYPE-R |
  test: Q-251 proves finite source-state/record domains, not the complete
        physical response domain
```

## 3. Q-252 and the three zeros

Q-252 proves, for the exact finite relative-phase functional and every
interior `0<p<1`:

```text
FINITE_RELATIVE_PHASE_STATIONARY_SET = EMPTY | TYPE-P
FINITE_ZERO_HISTORY_IS_STATIONARY = false | TYPE-R
```

The same artifact immediately limits the theorem: the finite object contains
only the relative-history phase summand and no independently varied
common-history argument; the complete stationarity equation may contain
record, field, metric, boundary, and source terms absent from the finite family
(Q-252:51-55).

It then separates:

```text
C1:               a=0       zero connection history in the finite law;
retarded extract: A_delta=0 equal forward/backward histories;
Legendre surface: J=R=0     vanishing external Legendre sources.
```

Q-252 states that C1 is an operator-reduction certificate, `A_delta=0` permits
an arbitrary common background `A_c`, and `J=R=0` makes a completed background
stationary without selecting a member.

```text
THE_THREE_ZEROS_ARE_ONE_EVALUATION_RULE = false | TYPE-R |
  test: their carriers and mathematical roles differ
FINITE_PURE_PHASE_NO_STATIONARY_POINT_REFUTES_COMPLETED_SADDLE_EXISTENCE = false | TYPE-R |
  test: Q-252's own scope excludes the complete common-history and coupled terms
PHYSICAL_COMMON_BACKGROUND_INSTANTIATED_BY_Q252 = false | TYPE-U |
  would-build: completed source germ and its source-free stationary 2PI-to-1PI
               solution
```

The pure-phase finite result is physical content about the finite relative
sector. It is not evidence that stationarity itself was imported into the
complete route by later bookkeeping.

## 4. Provenance of `stationary` and the 2PI requirement

### 4.1 Chronology

1. `primitive_complete_boundary_transition_functional_principle_v002.md:46`
   already says, "Near a stationary physical history the quadratic functional
   has the form ..." It then defines the on-shell cell `X_K` at :93-104 and
   requires the stationary proper interval to be an output at :110-123.
2. The active v004 corrects the bare-versus-induced role of `K`, but retains
   and sharpens the stationary architecture. It defines the normalized CTP
   bilocal Legendre transform, proves the exact identities
   `delta Gamma_2PI/delta Abar=-J-R Abar` and
   `delta Gamma_2PI/delta G=-R/2`, and therefore obtains stationarity at
   vanishing physical sources (v004:71-95).
3. v004 then places `B_ind` on `G_K`, a candidate normalized saddle, requires
   the full residual and stationarity conditions, and defines the first durable
   record as a simultaneous solution of the complete equations
   (v004:125-206).
4. Q-249/Q-254 and later P5/P7 specifications expose the block, domain,
   restriction, and Tail interfaces needed to execute that already-live
   architecture. They do not originate the physical stationarity requirement.

```text
STATIONARITY_FIRST_ENTERED_AT_Q249_OR_Q254 = false | TYPE-R |
  test: v002 and active v004 precede those specifications and state the
        stationary/on-shell requirements directly

STATIONARITY_IS_ONLY_A_REVIEWER_LABEL = false | TYPE-R |
  test: active v004 defines exact 2PI Legendre identities, a normalized saddle,
        full stationarity conditions, and a stationary first-record interval

PHYSICAL_STATIONARY_SOLUTION_EXISTS_AND_IS_SELECTED = false | TYPE-U |
  would-build: the completed physical functional, stationary solution class,
               existence/uniqueness result, and evaluation map
```

`primitive_complete_boundary_transition_functional_principle_v002.md:46` is
the earliest stationarity statement located in the surveyed deciding-chain
lineage. This is a lineage result, not a corpus-global priority claim.

```text
EARLIEST_LOCATED_DECIDING_CHAIN_STATIONARITY_AUTHORITY =
  primitive_complete_boundary_transition_functional_principle_v002.md:46
CORPUS_GLOBAL_FIRST_USE_OF_STATIONARY_PROVED = false | TYPE-S |
  scope: this relay audits the deciding chain, not every historical use of the
         token in every program root
```

### 4.2 Imported-framework scrutiny

The 2PI Legendre formalism is imported mathematical/ordinary-QFT machinery.
Its use here is not justified by name matching. It applies because active v004
explicitly instantiates its required objects: `Z_inc[J,R]`, `W`, `Abar`, `G`,
and `Gamma_2PI`, and states the exact derivative identities. The stationarity
condition `R=0 => delta Gamma_2PI/delta G=0` is then an algebraic consequence
inside the declared program object.

The stronger claim that a physical stationary first-record solution exists is
not supplied by the imported framework.

```text
G_STATIONARITY_AT_R0_DERIVED_FROM_DECLARED_LEGENDRE_IDENTITY = true
PHYSICAL_STATIONARY_FIRST_RECORD_EXISTENCE_DERIVED = false | TYPE-U |
  would-build: the complete coupled solution and its existence certificate
IMPORTED_2PI_FORMALISM_SELECTS_THE_PHYSICAL_BACKGROUND = false | TYPE-R |
  test: the formalism yields equations, not a member of their solution set
```

## 5. Synonym audit

### 5.1 Summary table

| Q-313 named object | Candidate prior object | Result | Consequence |
|---|---|---|---|
| restriction/Tail squares | Q-257 P7 plus Q-288 ledger columns | **DISTINCT-PROVEN from built content** | P7 is a conditional theorem; the physical maps/squares remain instances to build. Ledger columns are typed accounts, not maps. |
| stationary 2PI blocks | Q-309 two-sector source block plus Q-243 finite retarded blocks | **DISTINCT-PROVEN** | Variables, derivatives, carriers, and stationarity differ; no gap shrink. |
| physical background realization | Q-281 lift fiber plus DoR-015 external-background field | **THREE-LAYER DISTINCTION PROVEN** | adopted family -> lift/solution fiber -> realized stationary pair; no member or map has been built. |
| common completed domain | Q-278 bounded domains, P2 closures, Q-239 field (4) | **DISTINCT-FROM-BUILT; SHARED UNBUILT SUBOBJECT WITH Q-239(4)** | lower-scope domains do not discharge it; Q-239(4) is the same missing unbounded-domain obligation at a broader package interface, not a built synonym. |

### 5.2 Restriction/Tail squares versus P7 and Q-288

P7 expressly distinguishes the canonical sequential retractions
`r_N^B,q_N,Pi_N` from the physical maps `rho_G,N,rho_H,N`
(Q-257 artifact:36-45). Its theorem is conditional:

```text
If P2-P6 instantiate the physical core, RetHess embedding, physical
restrictions, package preservation, and naturality, then Tail_R={0} and the
upper T5 square commutes.
```

The same artifact flags:

```text
P7_OBJECT_SIDE_PHYSICAL_CERTIFICATE_EXISTS = false | TYPE-U
P7_FULL_T5_CERTIFICATE_EXISTS = false | TYPE-U
```

Q-288 records `physical_closure_restriction_square=TYPE-U`,
`commuting_stationary_schur_square=TYPE-U`, and
`physical_restrictions=TYPE-U`. A ledger cell stating that a map is missing is
not the map.

```text
Q257_P7_ALREADY_INSTANTIATES_PHYSICAL_RESTRICTION_TAIL_SQUARES = false | TYPE-R |
  test: P7's own antecedents name those unbuilt instances
Q288_LEDGER_COLUMNS_ARE_EXECUTED_PHYSICAL_SQUARES = false | TYPE-R |
  test: the columns carry TYPE-U values and future would-builds
RESTRICTION_TAIL_SQUARES_RENAME_PROVEN = false | TYPE-R |
  test: prior work proves the conditional theorem but lacks the physical maps
```

P7 remains useful: once the physical maps and preservation predicates exist,
its composition theorem prevents a second separation proof. That is a proof
dependency, not a synonym collapse.

### 5.3 Stationary 2PI blocks versus the two-sector and finite retarded blocks

Q-309 constructs the exact source Hessian block over the short exact sequence

```text
0 -> K_N -> J_N -> im(L_N) -> 0.
```

Its first row and column vanish, including finite kernel/complement and
kernel/probe mixing. Q-309 then proves the distinction explicitly:

```text
FINITE_SOURCE_TWO_SECTOR_BLOCK_EQUALS_STATIONARY_2PI_BLOCK_SYSTEM = false |
  TYPE-R |
  test: variables, derivatives, carriers, and stationary condition differ
```

The source Hessian is `D^2W_N`. The physical stationary block system consists
of `Gamma_AA`, `Gamma_AG`, `Gamma_GG`, and `Gamma_GA` on one common physical
domain at source-free stationary `G_*`, followed by the `GG` inverse and Schur
reduction. Q-243's finite mixed retarded block is a finite Keldysh
source-derivative result, not that system.

```text
Q309_TWO_SECTOR_BLOCK_IS_STATIONARY_2PI_BLOCK_SYSTEM = false | TYPE-R
Q243_FINITE_RETHESS_BLOCK_IS_PHYSICAL_STATIONARY_RETHESS = false | TYPE-R |
  test: finite source derivative versus completed inverse/Schur action Hessian
STATIONARY_2PI_BLOCKS_RENAME_PROVEN = false | TYPE-R
STATIONARY_2PI_BLOCKS_BUILT = false | TYPE-U |
  would-build: physical Gamma_2PI and AA/AG/GG/GA blocks on one domain at G_*
```

### 5.4 Physical background realization versus lift fiber and adopted field

DoR-015 adopts A1 as a full external-background family and opens the
`STAT_BG_LIFT_FIBER`; it does not select a member. The ratified V005 choice
table says:

```text
A1 = full globally hyperbolic oriented Lorentzian U(1)-bundle family,
     with no fixed member.
```

V005 also flags `STATIONARY_BACKGROUND_BUILT=false | TYPE-U` with the
would-build `stationary lift fiber, 2PI blocks, and stationary selector`
(V005:968-975).

Q-281 proves that the anchored invariant state lives in a trace-class source
space, while `Abar_*` lives in the completed physical common-field space and
`G_*` in the completed connected-bilocal operator space. It constructs the
bounded source-analytic seed but states that the seed is not yet the physical
pair and names the missing source-to-field, pairing, quotient, and stationary
Legendre maps.

Thus the three objects are:

```text
EXTERNAL_BACKGROUND_FAMILY:
  adopted admissible carrier/family; no member selected

STAT_BG_LIFT_FIBER([A]):
  the admissible maps/solutions carrying source-origin data into stationary
  physical background pairs

PHYSICAL_BACKGROUND_REALIZATION:
  one actual pair (Abar_*,G_*(Abar_*)) satisfying the source-free Legendre and
  stationarity equations
```

```text
DOR015_EXTERNAL_BACKGROUND_IS_PHYSICAL_STATIONARY_PAIR = false | TYPE-R |
  test: DoR-015 opens the lift fiber and V005 keeps the stationary pair TYPE-U
Q281_BOUNDED_BACKGROUND_SEED_IS_PHYSICAL_STATIONARY_PAIR = false | TYPE-R |
  test: source-state and physical-field/bilocal codomains differ
STAT_BG_LIFT_FIBER_IS_AN_ALREADY_REALIZED_BACKGROUND = false | TYPE-R |
  test: a fiber of admissible lifts/solutions is not a selected member
PHYSICAL_BACKGROUND_RENAME_PROVEN = false | TYPE-R
PHYSICAL_BACKGROUND_REALIZATION_BUILT = false | TYPE-U |
  would-build: lift, stationary solution/existence class, and evaluation rule
```

### 5.5 Common completed domain versus Q-278, P2, and Q-239 field (4)

Q-278's verified `Dom_rec^bdd` is the full domain of the bounded outgoing
record representation. Its verifier states that it is not a domain for any
unbuilt unbounded physical endpoint, inverse, or response operator.

P2 supplies the source Banach topology, dense finite source core,
contractive restrictions, and source differential calculus. Q-239/P3 states
that `Diff_src` is not a common domain theorem for later unbuilt unbounded
endpoint operators.

Q-239 field (4) is the still-unbuilt obligation:

```text
endpoint domains for the later unbounded physical operators
```

and specifies one common dense endpoint domain invariant under those operators
and the gauge action, with preparation/gluing boundary conditions
(Q-239:464-506). Q-313's common completed domain is the response-side
instantiation of this obligation for `Gamma_AA`, `Gamma_AG`, `Gamma_GG`,
`Gamma_GA`, the inverse, and the Schur map.

```text
Q278_BOUNDED_DOMAIN_DISCHARGES_COMMON_COMPLETED_DOMAIN = false | TYPE-R |
  test: bounded outgoing-record representation versus unbounded physical
        response/inverse operators
P2_SOURCE_CLOSURE_DISCHARGES_COMMON_COMPLETED_DOMAIN = false | TYPE-R |
  test: source-parameter calculus versus physical operator graph/closure domain
Q239_FIELD4_IS_ALREADY_BUILT = false | TYPE-U |
  would-build: named unbounded physical operators, common invariant dense
               domain, closure, and boundary conditions
Q313_DOMAIN_AND_Q239_FIELD4_SHARE_ONE_UNBUILT_SUBOBJECT = true
Q313_DOMAIN_EQUALS_Q239_FIELD4_IN_FULL = false | TYPE-R |
  test: Q-313 additionally requires the four 2PI blocks, inverse, and Schur
        operations to be jointly defined on the domain
COMMON_COMPLETED_DOMAIN_RENAME_OF_BUILT_OBJECT = false | TYPE-R
```

This is the only synonym row with genuine overlap. It removes duplicated
tracking language, not an unbuilt mathematical obligation.

## 6. Corrected last-wall decomposition and build order

The four Q-313 names should not be grouped as one stationary package. Their
dependency structure is:

```text
T1  COMMON_COMPLETED_PHYSICAL_DOMAIN
    named AA/AG/GG/GA, inverse, response, and endpoint operators;
    common invariant dense core; closures; boundary conditions;
    relation: includes/discharges the response-facing part of Q-239 field (4)

T2  PHYSICAL_RESTRICTION_AND_TAIL_SQUARES
    instantiate rho_G,N and rho_H,N and package-preservation/naturality maps;
    then consume Q-257's already-proved conditional P7 composition theorem

S1  PHYSICAL_STATIONARY_BACKGROUND_REALIZATION
    construct the completed source-free Legendre solution pair
    (Abar_*,G_*(Abar_*)) inside the adopted external-background family;
    prove existence and state whether the evaluation is member-independent or
    uniquely selected

S2  STATIONARY_2PI_BLOCK_SYSTEM_AND_SCHUR
    construct Gamma_AA, Gamma_AG, Gamma_GG, Gamma_GA on T1 at S1;
    construct the prescribed GG inverse and Schur reduction;
    execute T2 and the Q-279 restrictions
```

The acyclic order is:

```text
T1 -> T2 interface instantiation
T1 + S1 -> S2
S2 + T2 -> physical cycle-sector RetHess and the symbolic p verdict
```

`T2` may be prepared in parallel with `S1` after `T1` fixes the physical class
and domains. P7's theorem is consumed at the end of `T2`; it is not rebuilt.

```text
FRONTAL_STATIONARY_BUILD_HAS_A_SEALED_PURPOSE = true
  purpose: B_ind and DeltaPhi require the completed stationary/on-shell path

FRONTAL_BUILD_SHOULD_REBUILD_P7_SEPARATION_THEOREM = false | TYPE-R |
  test: Q-257 already proves the conditional theorem

FRONTAL_BUILD_SHOULD_TREAT_Q288_LEDGER_ROWS_AS_OBJECTS = false | TYPE-R |
  test: they are typed accounts and door flags

VERDICT_COMPUTABLE_FROM_BUILT_REFERENCE_MATERIAL_ALONE = false | TYPE-R |
  test: source-level zero blocks cannot be transported through absent physical
        domains, restrictions, stationary blocks, and background realization

REMAINING_OBJECTS_ARE_BOUNDED_AND_NAMED = true
  list: T1, T2, S1, S2
```

## 7. Final flags

```text
NEW_CLASS_BACKGROUND_AGNOSTIC_OPERATOR_FUNCTIONAL_FOUND = true
NEW_CLASS_BACKGROUND_INAPPLICABLE_FINITE_QUOTIENT_FOUND = true

OUTPUT_REQUIREMENT_P_LOC = BACKGROUND_AGNOSTIC_OPERATOR_FUNCTIONAL
OUTPUT_REQUIREMENT_B_IND = STATIONARY_ON_SHELL
OUTPUT_REQUIREMENT_DELTAPHI = STATIONARY_ON_SHELL
OUTPUT_REQUIREMENT_KAPPA_THOMSON = DECLARED_A0_COMPLETE_AMPLITUDE_REFERENCE
OUTPUT_REQUIREMENT_RESPONSE_VISIBLE_QUOTIENT = BACKGROUND_INAPPLICABLE_FINITE_QUOTIENT
OUTPUT_REQUIREMENT_OUTGOING_VISIBLE_QUOTIENT = BACKGROUND_INAPPLICABLE_FINITE_QUOTIENT

STATIONARITY_REQUIRED_BY_LIVE_ALPHA_FACING_VALUE_PATH = true
COLLAPSES_TO_REFERENCE = false | TYPE-R |
  test: active v004 B_ind and first-record DeltaPhi require the completed
        stationary/on-shell solution

STATIONARITY_REQUIREMENT_IS_Q249_Q254_IMPORT = false | TYPE-R |
  test: historical v002 and active v004 state it earlier and directly

RESTRICTION_TAIL_SQUARES_ALREADY_BUILT = false | TYPE-U
STATIONARY_2PI_BLOCKS_ALREADY_BUILT = false | TYPE-U
PHYSICAL_BACKGROUND_REALIZATION_ALREADY_BUILT = false | TYPE-U
COMMON_COMPLETED_DOMAIN_ALREADY_BUILT = false | TYPE-U

SYNONYM_COLLAPSE_COUNT = 0
SHARED_UNBUILT_OBLIGATION_COUNT = 1
  object: Q-313 common completed domain overlaps Q-239 field (4)

POST_DEDUP_UNBUILT_OBJECT_COUNT = 4
POST_DEDUP_STATIONARY_CORE_COUNT = 2
POST_DEDUP_TRANSPORT_INFRASTRUCTURE_COUNT = 2

PHYSICAL_CYCLE_SECTOR_RETHESS_EXISTS = false | TYPE-U |
  would-build: T1 + T2 + S1 + S2
P_APPEARS_IN_PHYSICAL_CYCLE_RETHESS = NO_VERDICT |
  prerequisite: physical cycle-sector RetHess
P_CANCELS_FROM_PHYSICAL_CYCLE_RETHESS = NO_VERDICT |
  prerequisite: physical cycle-sector RetHess

PROVABLE =
  stationarity is required for B_ind and DeltaPhi by active v004;
  p_loc and the two quotients require the two Q-80 classes above;
  kappa_Thomson uses its distinct complete-amplitude A=0 reference;
  Q-252's finite no-stationary theorem does not refute complete stationarity;
  none of the four Q-313 objects is a built synonym;
  the last wall decomposes into T1,T2,S1,S2

YOURS =
  none; this audit selects no background, contour, extension, rank member,
  response class, root, or value

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

NONEXECUTION_SCOPE = true | TYPE-S |
  register, plan, tracker, git, commit, push, gate, deployment, value
  evaluation, and measured comparison were outside this relay
