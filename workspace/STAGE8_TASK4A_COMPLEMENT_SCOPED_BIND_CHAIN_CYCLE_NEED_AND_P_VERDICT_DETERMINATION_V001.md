# Stage 8 Task 4a Complement-Scoped B_ind Chain, Cycle Need, and p-Verdict Determination v001

Date: 2026-08-03  
Relay: **PASTE 407 — CODEX LANE 1 (HIGH EFFORT)**  
Task: determine whether the complement-scoped `B_ind` chain needs the cycle sector and execute the symbolic `p` verdict if complete  
Status: **CHAIN INCOMPLETE; CYCLE-FREEDOM NOT PROVED; VERDICT DOES NOT EXECUTE**  
Custody: lane artifact; seal and mirror only; no register, plan, tracker, git, commit, or push action

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

---

## 0. Lead determination

**The `B_ind` chain does not execute. C40 removes the requirement to invert a
pure cycle direction, but it does not construct the physical propagating
complement, its stationary action, its reducing/block-separation theorem, or
the physical `Pi_R,ind[G_K]` that `p_loc` consumes.**

The first exact stop is the formation of the argument of `p_loc`:

```text
B_ind(K)=p_loc[Pi_R,ind[G_K]].                       (BC-1)
```

The outer functional `p_loc` is background-agnostic in its own signature.
That does not make `(BC-1)` background-agnostic. The live v004 source defines
`G_K` as a candidate normalized saddle, requires a valid saddle to satisfy
the complete residual and stationarity system, and makes `Pi_R,ind` a
completed physical response output (`primitive_record_cell_selection_
principle_v004.md:115-180`). Q-314 proves this distinction explicitly.

The built stack reaches:

```text
source germ and P2/P4 calculus
  -> unique P_src and Leg_W
  -> source action graph
  -> bounded connected raw correlator
     G^007=-hbar^2 q(1-q) L tensor L
  -> exact finite/source restrictions and zero ordered-retarded shadows.
```

It does **not** reach:

```text
physical complement inside the independent (Abar,G) tangent carrier
  -> completed physical Gamma_2PI on that complement
  -> nonempty physical critical/stationary locus and G_K
  -> stationary AA/AG/GG/GA blocks on one domain
  -> complement inverse/Schur with a reducing-subspace certificate
  -> physical RetHess and Pi_R,ind
  -> instantiated p_loc on that physical operator class
  -> B_ind.                                         (BC-2)
```

Q-318 proves that `P_src` and `Leg_W` are **source-side**. Its only local
critical point lies on the diagnostic scalar quotient
`E_src/ker(lambda)`, and it refutes identifying that point with a physical
background. Q-315 proves that the bounded raw restrictions are not physical
`(Abar,G)` tangent, stationary, Schur, or `RetHess` restrictions. Q-316 and
Q-317 leave the physical action, locus, background, stationary blocks, and
`Pi_R,ind` unbuilt. No DoR-016 exists at the current head; every attempted
physical-action proposal remains unratified.

Therefore the relay's input-completeness premise is refuted:

```text
RELAY_ARE_INPUTS_PRESENT = false | TYPE-R |
  test: Q-314/Q-315/Q-316/Q-317/Q-318 distinguish the built source/raw stack
        from the missing physical complement stationary-response stack

C40_SUPPLIES_COMPLEMENT_SCOPED_INVERSE_RULE = true
C40_SUPPLIES_PHYSICAL_COMPLEMENT_INSTANCE = false | TYPE-R |
  test: the ruling changes Q-52 applicability; it adds no carrier, action,
        stationary locus, block system, or response map

B_IND_CHAIN_COMPLETE = false | TYPE-U
B_IND_EXECUTION_CHECK = BLOCKED | TYPE-C |
  constraints: the objects in (BC-2) are absent
```

The cycle question also remains open. The amended chain directly inverts no
cycle direction, so C40's void clause does not fire. But **no theorem proves
that the physical complement reduces the stationary 2PI system**, and no
theorem proves that the stationary evaluation point `G_K` is independent of
cycle-sector action content. The exact possible cycle-touching step is the
unbuilt formation of `Pi_R,ind[G_K]`, through:

1. cycle/complement mixed stationary blocks; and
2. the dependence of the full stationary saddle `G_K` on the cycle-sector
   operator equation.

This is not a conflation of `B_ind` with `R_comp`: `R_comp` is not inserted
as `B_ind`'s output. Its role is only the sealed validity condition on the
same `G_K` at which `Pi_R,ind` is evaluated.

```text
B_IND_DIRECTLY_INVERTS_CYCLE_DIRECTION = false | TYPE-S |
  scope: C40-amended chain

B_IND_CHAIN_IS_CYCLE_FREE = NO_VERDICT |
  prerequisite: physical complement realization, reducing-block theorem,
                and cycle-independent or family-uniform stationary evaluation

P_APPEARS_IN_PHYSICAL_B_IND_ARGUMENT = NO_VERDICT
P_CANCELS_FROM_PHYSICAL_B_IND_ARGUMENT = NO_VERDICT
PHYSICAL_P_VERDICT_EXECUTED = false | TYPE-C |
  constraints: Pi_R,ind[G_K] and p_loc's physical instance do not exist
```

What remains proved is the finite/source shadow: the symbolic state weight
appears in the bounded raw difference/difference block and is absent from the
exact Q-243/Q-279 ordered-retarded shadow. That is support separation, not a
physical `B_ind` verdict.

---

## 1. Scope, currency, and authorities

### 1.1 Current standing

The send-time starting head is Q-324 with C40 in force.

Bearing current results:

1. Q-306: the unique normalization `N` is installed; Door D passes; bounded
   `G^007` exists; inverse/Schur, retarded response, background, and consumer
   classes remain absent.
2. Q-313: Map 1 and the source-level zero descent exist; the physical
   stationary 2PI descent does not.
3. Q-314: `p_loc` alone is background-agnostic, while `B_ind` requires a
   stationary/on-shell argument.
4. Q-315: source/raw squares exist; physical `rho_G,N`, `rho_H,N`, common
   stationary domain, and Schur square do not.
5. Q-316/Q-317: neither the physical stationary background nor the completed
   physical action/critical locus exists.
6. Q-318: `P_src`, `Leg_W`, and the source action graph derive uniquely; they
   do not instantiate the independent physical `(Abar,G)` action.
7. Q-323/C40: a pure cycle inverse is removed from Q-52's applicability.
   The cycle action is carried separately; no physical complement is created.
8. Q-324: the cycle action remains bounded/open, and only direct
   alpha-facing dependence is undecided.

No later authority supersedes the carrier and stationarity stops above.

### 1.2 Version difference that controls this relay

C40 changes exactly one requirement:

```text
old Q-52 scope: inverse on the full physical quotient;
C40 scope:       inverse on an independently proved propagating complement,
                 with the record-cycle summand carried separately.
```

It does not say:

```text
E_src/ker(lambda) is the physical propagating complement;
GraphAct_W is Gamma_2PI;
the diagnostic source critical point is G_K;
source Hessian blocks are stationary 2PI blocks;
rho_raw,N is rho_G,N or rho_H,N;
p_loc is instantiated on the completed physical response class.
```

Those identifications remain refuted or unbuilt under Q-313 through Q-318.

### 1.3 Roots entered

```text
/Users/bgm/MB Work/alpha_supervision/
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003/
```

The protected `a32_holdout/custodian_private/` tree was not entered.

### 1.4 Principal authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | fences, Q-54 typing, custody |
| `QUESTIONS_SETTLED_REGISTER_V001.md` | `e7adc6f975d700253aaabc311ee7566766278c572d9193abbbd52c5a8ac97078` | Q-306 through Q-324 currency |
| `TASK_LIST_HERE_TO_ALPHA_2026-08-01_V002.md` | `304ebfc33c849ce446a7cc9f12d885279c236ce921e6820f36a2590e259d59d3` | C40 ruling and void clause |
| `RELAY_PASTE_407_THE_COMPLEMENT_SCOPED_VERDICT_V001.md` | `7e925d5c3e532f0f0f898438f16537fa305d3ab06e3220427b34774a52dec843` | task contract |
| `primitive_record_cell_selection_principle_v004.md` | `13d227ceb2198d96b0e4e2fef57b874cea71cb755320508fbf4c6d64a00c507e` | live `R_phys`, `Pi_R,ind`, `G_K`, `p_loc`, `B_ind`, and stationarity signature |
| `STAGE8_TASK4A_SOURCE_TO_OUTPUT_NORMALIZATION_N_UNIQUENESS_INSTALL_AND_FULL_DOOR_D_REEXECUTION_V001.md` | `00414b0d5617e44b12e9f7faef4484803c858992be6ed1951df38c22719b2696` | `G^007`, Door-D pass, inverse/retarded stop |
| `STAGE8_TASK4A_RELATIVE_HISTORY_CYCLE_FACTORIZATION_AND_2PI_DESCENT_VERDICT_BUILD_V001.md` | `ea8f4e9a79a9e4aca4a0b9e9aab470d78cd4d9c78794c20d9e979c0db16fbeab` | Map 1 and source/physical 2PI separation |
| `STAGE8_TASK4A_STATIONARITY_REQUIREMENT_AND_LAST_WALL_SYNONYM_AUDIT_DETERMINATION_V001.md` | `671a94a7f55a5649cc8280bb0cb460a3a08b758b629279ab2ec06d982d0965a8` | stationary `B_ind` requirement and four-object wall |
| `STAGE8_TASK4A_TRANSPORT_INFRASTRUCTURE_COMMON_DOMAIN_AND_PHYSICAL_SQUARES_BUILD_ATTEMPT_V001.md` | `f886284c632f238bb01d02de2cc64e3f7ed76c0bae4ba14487ac0b2bde7a22e3` | built source/raw squares and absent physical squares |
| `STAGE8_TASK4A_PHYSICAL_BACKGROUND_REALIZATION_ON_ADOPTED_FIELD_BUILD_ATTEMPT_V001.md` | `a8375af0fee05d756287e2702b7031dacd0bfc53b2bcc09920e72bcbf489adf5` | absent `G_K`/stationary realization |
| `STAGE8_TASK4A_COMPLETED_RECORD_GEOMETRY_GEOMETRIC_LOCUS_CANONICAL_FUNCTIONAL_TEST_V001.md` | `cd29b21bfab2781dc047151d76821a9e977c5eb1f3e86bfddf7e2882d9c847a0` | absent physical action and critical locus |
| `STAGE8_TASK4A_COMPLETED_PHYSICAL_LEGENDRE_PAIRING_AND_ACTION_MAP_DERIVATION_ATTEMPT_V001.md` | `d220a4dc9f5d49674cb88c6b08272e3304795117121c2b3a742152120bc1cfb7` | unique source Legendre layer and six physical residues |
| `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md` | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | conditional physical inverse/Schur/retarded contract |
| `STAGE8_TASK4A_P_LOC_TAIL_ANNIHILATION_CERTIFICATE_DETERMINATION_V001.md` | `df2dbdccb25d5ee62e0de9051a8300c3933fb4c07250e765632d2f6247a6df45` | `p_loc` is declared but not instantiated on a physical consumption class |
| `STAGE8_TASK4A_FINITE_HESSIAN_TO_DELTAPHI_TRANSPORT_MAP_CONSTRUCTION_AND_P_CH_TRACE_V001.md` | `70185aa842bc500724719c65bd66b5f07005e2214b97be0d35e07fd029d5c68c` | exact finite ordered-retarded zero |
| `STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md` | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | probes-on exact finite blocks |
| `STAGE8_TASK4A_OFF_SECTION_FLAT_GERM_EXACT_FINITE_DATA_AND_RELEVANCE_DETERMINATION_V001.md` | `64561aca2a2cf7f2f0decf64278b6745018d6eb8052b8fa037efa5ff36a543a1` | Q-324 cycle-action and relevance standing |

Positive claims using the ratified stack are `TYPE-P | premises: DoR-008,
DoR-009, DoR-013, DoR-014 as amended, DoR-015` where applicable. There is no
DoR-016 premise.

---

## 2. The live `B_ind` contract

The live construction order is not merely

```text
p_loc compose a known operator.
```

It is:

```text
complete physical Gamma_2PI and source-free stationary solution
  -> G_K and stationary AA/AG/GG/GA blocks
  -> physical inverse/Schur and Keldysh retarded extraction
  -> Pi_R,ind[G_K]
  -> completed physical p_loc
  -> B_ind(K).                                      (BC-3)
```

The active v004 text states:

```text
R_phys[G] := H_R[G]-Pi_R,ind[G]=0,

B_ind(K)=p_loc[Pi_R,ind[G_K]],

R_comp[G_K]=(I-Pi_loc)R_phys[G_K]=0,
```

and requires the valid saddle to satisfy the remaining source, metric, Gauss,
record-effect, interval, and boundary stationarity. It also defines the 1PI
functional by stationary reduction at `G_*(Abar)`.

### 2.1 Background-agnostic outer map versus stationary argument

Q-314 proves:

```text
P_LOC_REQUIRES_STATIONARY_BACKGROUND = false | TYPE-S
B_IND_REQUIRES_STATIONARY_ON_SHELL_INPUT = true.
```

These statements are compatible. A linear functional can be independent of
the evaluation point while its **argument** depends on that point.

```text
P_LOC_IS_BACKGROUND_AGNOSTIC_OPERATOR_FUNCTIONAL = true
B_IND_IS_BACKGROUND_AGNOSTIC = false | TYPE-R |
  test: its displayed argument is Pi_R,ind[G_K]
```

### 2.2 `p_loc` is still an abstract role

The v004 definition says only after the complete operator derives the
projection, any required pairing, and extension to every physical CTP block
may `(BC-1)` be defined. Q-255 finds:

```text
P_LOC_INSTANTIATED = false | TYPE-U
P_LOC_INPUT_CONSUMPTION = UNSPECIFIED.
```

C40 changes the inverse domain but does not instantiate this functional on a
physical complement response class.

---

## 3. Object-by-object chain trace

| Order | Object or operation | Exact standing | Cycle status | Can the next arrow run? |
|---|---|---|---|---|
| 1 | P2 source topology/calculus | built `TYPE-P` | source carrier only | yes, to P4/source derivatives |
| 2 | P4 `W=-i hbar Log Z` | built `TYPE-P` | factors through `lambda` | yes |
| 3 | `P_src` and `Leg_W` | unique, built `TYPE-P` | constant on `ker lambda`; source-dual only | yes, to source graph |
| 4 | `GraphAct_W` | built `TYPE-P` | no transverse physical action | yes only as source-parametrized graph |
| 5 | diagnostic quotient `E_src/ker lambda` | local source Legendre chart exists | removes record-visible cycle; not physical quotient | **no physical promotion** |
| 6 | normalization `N` and pairing | unique on active image, built `TYPE-P` | unused complement unnormalized | yes, to bounded raw output |
| 7 | `G^007=-hbar^2 q(1-q)L tensor L` | bounded physical raw bilinear, built `TYPE-P` | zero on `ker L`; symbolic weight in nonkernel raw block | yes, to built raw restrictions only |
| 8 | Map 1 and source-level two-sector descent | built `TYPE-P` | finite/completed source mixing zero and p-free | yes on source/cycle character layer only |
| 9 | source/raw restriction squares | built `TYPE-P`; Q-243/Q-279 exact | `Tail_raw={0}` on bounded class | yes on the same raw class |
| 10 | physical propagating complement in independent `(Abar,G)` tangents | **unbuilt `TYPE-U`** | no physical projector/inclusion/reducing theorem | **STOP** |
| 11 | physical measure, contour, contacts, boundary form, common graph domain | **unbuilt `TYPE-U`** | required even on complement | no |
| 12 | completed physical `Gamma_2PI` on the complement | **unbuilt `TYPE-U`** | no cycle/complement block theorem | no |
| 13 | physical critical locus / normalized saddle `G_K` | **unbuilt `TYPE-U`** | cycle-independence `NO_VERDICT` | no |
| 14 | stationary `AA/AG/GG/GA` blocks | **unbuilt `TYPE-U`** | mixed cycle/complement blocks `NO_VERDICT` | no |
| 15 | complement `GG` inverse and Schur reduction | **unbuilt `TYPE-U`** | C40 forbids cycle inversion; reduction certificate absent | no |
| 16 | physical Keldysh retarded extraction / `Pi_R,ind` | **unbuilt `TYPE-U`** | cycle transfer `NO_VERDICT` | no |
| 17 | `rho_H,N`, physical restriction, and Tail square | **unbuilt `TYPE-U`** | finite zero cannot be promoted | no |
| 18 | instantiated `p_loc` on the physical complement response class | **unbuilt `TYPE-U`** | outer map is background-agnostic; consumption class unspecified | no |
| 19 | `B_ind` | only a sealed conditional signature | p-content `NO_VERDICT` | no execution |

The chain stops at row 10, before any physical inverse is attempted.

```text
FIRST_MISSING_OBJECT =
  PHYSICAL_PROPAGATING_COMPLEMENT_TANGENT_AND_RESTRICTION_REALIZATION | TYPE-U

FIRST_MISSING_PHYSICAL_ACTION_OBJECT =
  COMPLEMENT_SCOPED_PHYSICAL_LEGENDRE_ACTION_AND_DOMAIN_PACKAGE | TYPE-U

PI_R_IND_PHYSICAL_INSTANCE_EXISTS = false | TYPE-U
B_IND_PHYSICAL_INSTANCE_EXISTS = false | TYPE-U
```

---

## 4. Does the chain touch the cycle sector?

### 4.1 What C40 proves

C40 proves a machinery statement:

```text
the displayed alpha-facing consumers do not require a two-sided inverse
on a pure record-cycle direction.
```

Therefore a lawful architecture may invert only a separately proved
propagating complement and carry the record-cycle summand without inversion.

```text
CYCLE_DIRECTION_INVERSE_REQUIRED_BY_B_IND_SIGNATURE = false | TYPE-S
CYCLE_DIRECTION_INVERSE_USED_IN_THIS_RUN = false | TYPE-S
C40_VOID_CLAUSE_FIRED = false | TYPE-S
```

### 4.2 What C40 does not prove

Let a future physical tangent carrier have a direct-sum notation solely for
this countermodel:

```text
T_phys = C_prop direct-sum K_cycle.
```

Even without inverting `K_cycle`, a physical stationary operator can contain
a mixed arrow

```text
M_CK : K_cycle -> C_prop.                           (BC-4)
```

If `M_CK=0` and the stationary background is family-uniform over the cycle
sector, the complement response can be cycle-free. If `M_CK` is nonzero, or
if the valid stationary `G_K` varies with the carried cycle-sector action,
the complement argument of `p_loc` can depend on cycle content without any
cycle inverse.

Both possibilities are compatible with the built source/raw shadows because
Q-313/Q-315/Q-318 provide no physical action restriction that constrains
`M_CK`, and Q-324 leaves the cycle action open.

This countermodel refutes the inference

```text
no cycle inverse => no cycle dependence.
```

```text
C40_NO_CYCLE_INVERSE_IMPLIES_CYCLE_FREE_B_IND = false | TYPE-R |
  countermodel: the mixed arrow (BC-4) or a cycle-dependent stationary G_K

PHYSICAL_CYCLE_TO_COMPLEMENT_MIXING_ZERO = NO_VERDICT
PHYSICAL_STATIONARY_G_K_CYCLE_INDEPENDENT = NO_VERDICT
B_IND_CHAIN_IS_CYCLE_FREE = NO_VERDICT
```

### 4.3 Exact cycle-touching step

The first possible touch is not `p_loc`. It is the construction of
`Pi_R,ind[G_K]`:

1. the physical stationary block system must be reduced by a complement that
   is invariant under every block used in the response;
2. the cycle-to-complement and complement-to-cycle mixed blocks must be
   proved zero or proved irrelevant to the `p_loc` image; and
3. the stationary evaluation must be proved independent of the carried cycle
   action, or the final projected response must be proved uniform over the
   stationary family.

No one of these certificates exists.

---

## 5. The maximal symbolic p-trace that actually runs

### 5.1 Built source/raw path

On the installed source graph, the state weight enters through the scalar
function `F` and its derivatives. After the unique source-to-output
normalization and connected subtraction, Q-306 gives

```text
G^007=-hbar^2 q(1-q)L tensor L.                    (BC-5)
```

Here Q-306's `q` is the symbolic source-state weight on the installed family;
it is not a momentum, charge, coupling, or evaluated rank ratio.

The exact finite/source sector pattern is:

```text
difference/difference raw connected block: q(1-q)-weighted;
source-kernel/cycle direction:              zero;
finite ordered-retarded shadow:             zero and p-free;
Q-279 probe mixed retarded-candidate block: zero and p-free.
```

```text
P_DEPENDENCE_IN_BOUNDED_RAW_NONKERNEL_BLOCK = present_symbolically | TYPE-P
P_DEPENDENCE_IN_Q243_Q279_ORDERED_RETARDED_SHADOW = absent | TYPE-P
P_DEPENDENCE_IN_SOURCE_KERNEL_MIXING = absent | TYPE-P
```

### 5.2 Where the trace stops

The next required transformation is not the already-executed finite Keldysh
rotation. It is the physical completed action-valued inverse/Schur and
retarded extraction at `G_K`, on a common physical domain. Its missing
operations may preserve, cancel, invert, or redistribute the raw symbolic
factor on the complement. No current theorem decides which.

Therefore:

```text
P_TRACE_REACHES_PHYSICAL_PI_R_IND = false | TYPE-C |
  constraints: rows 10-17 of the chain trace are absent

P_APPEARS_IN_PHYSICAL_PI_R_IND = NO_VERDICT
P_CANCELS_FROM_PHYSICAL_PI_R_IND = NO_VERDICT
P_APPEARS_IN_B_IND_ARGUMENT = NO_VERDICT
P_CANCELS_FROM_B_IND_ARGUMENT = NO_VERDICT
```

The finite p-free shadow is an exact restriction target for a future
physical response. It is not itself the completed physical response.

---

## 6. Minimal would-build after C40

C40 genuinely shrinks the missing physical action package: the `B_ind` path
need not supply an inverse on the carried cycle sector. The minimal remaining
object is:

```text
COMPLEMENT_SCOPED_PHYSICAL_STATIONARY_RESPONSE_PACKAGE := (
  C_prop and its inclusion/projection in the physical Abar/G tangent carrier,
  finite physical restrictions rho_A,N and rho_G,N,
  invariant physical measure and delta pairing,
  interacting contour and boundary/contact variational data,
  common invariant graph domain and closure,
  Gamma_2PI restricted to C_prop,
  nonempty source-free stationary class and G_K evaluation,
  stationary AA/AG/GG/GA blocks on C_prop,
  reducing certificate excluding cycle/complement transfer,
  complement GG inverse and Schur map,
  physical Keldysh retarded extraction and Pi_R,ind,
  rho_H,N and the Q-243/Q-279 restriction squares,
  target-independent p_loc instance on the resulting operator class
).
```

The cycle action may remain bounded/open for `B_ind` **only if** the reducing
and stationary-uniformity certificates above prove that no carried cycle
content reaches the complement argument. Without those certificates, the
cycle-action identification problem remains on the critical path.

```text
C40_REMOVES_CYCLE_INVERSE_FROM_MINIMAL_PACKAGE = true
C40_REMOVES_CYCLE_ACTION_FROM_FULL_PROGRAM = false | TYPE-R |
  test: Q-324 R_comp relevance and the open mixing/background routes

COMPLEMENT_SCOPED_PHYSICAL_STATIONARY_RESPONSE_PACKAGE_EXISTS = false | TYPE-U
```

No member, background, complement splitting, contour, domain, action, or
`p_loc` extension is selected here.

---

## 7. Restriction checks, six-account rows, and doors

### 7.1 Executed restrictions

The restrictions that can lawfully be executed remain the built ones:

```text
P2 source restriction/retraction: PASS;
Map 1 zero-extension square:      PASS;
G^007 raw finite square:          PASS;
Q-243 ordered-retarded shadow:    exact zero, p-free;
Q-279 probes-on mixed shadow:      exact zero, p-free;
Tail_raw on bounded class:         {0}.
```

No physical `Pi_R,ind` restriction is executed because `rho_H,N` and its
domain do not exist. This is a typed stop, not a failed restriction.

### 7.2 Six-account table

| Operation | Kernel/applicability | Image | Sector transfer | Restriction square | Tail action | Verdict |
|---|---|---|---|---|---|---|
| source differentiation / `Leg_W` | affine `ker lambda` cosets | one-dimensional source-dual line | none to physical action | source squares pass | `Tail_src={0}` | **PASS / TYPE-P** |
| normalization and raw lift | active generated image; `ker L` evaluates to zero | bounded `G^007` raw bilinear | source to raw output only | Door D, Q-243/Q-279 pass | `Tail_raw={0}` | **PASS / TYPE-P** |
| form physical complement | no physical tangent realization/projector | none | cycle/complement split unformed | none | `Tail_R NO_VERDICT` | **TYPE-U / TYPE-C check** |
| physical stationary evaluation | no `Gamma_2PI`, locus, or `G_K` | none | possible cycle dependence `NO_VERDICT` | none | `NO_VERDICT` | **TYPE-U / TYPE-C check** |
| complement inverse/Schur/retarded extraction | blocks/domain/reducing theorem absent | none | mixed transfer `NO_VERDICT` | physical square absent | `NO_VERDICT` | **TYPE-U / TYPE-C check** |
| instantiate `p_loc` and form `B_ind` | physical response class and consumption law absent | none | outer map unexecuted | none | tail and cycle dependence `NO_VERDICT` | **TYPE-U / TYPE-C check** |

### 7.3 Door flags

```text
Door Source:
  OPENED previously; P2/P4/P_src/Leg_W certified.

Door Raw:
  OPENED previously; N, G^007, and raw finite squares certified.

Door Complement:
  NOT OPENED; no independently proved physical propagating complement.

Door Action:
  NOT OPENED; no completed physical complement action or DoR-016.

Door Crit:
  NOT OPENED; no physical action/domain, so no physical G_K.

Door Schur:
  NOT OPENED; no blocks, domain, or reducing certificate.

Door RetHess:
  NOT OPENED; no Pi_R,ind or rho_H,N.

Door Consumer:
  NOT OPENED; p_loc remains an uninstantiated completed-operator role.

C40 cycle-inverse door:
  NOT OPENED BY DESIGN; void clause not fired.
```

### 7.4 Kill-passes

1. **No cycle inverse.** No operation in this run acts with an inverse on a
   cycle direction.
2. **No source/physical promotion.** `E_src/ker(lambda)` is not renamed the
   physical complement.
3. **No raw/action promotion.** `G^007` is not renamed `G_K`, `Gamma_GG`,
   `RetHess`, or `Pi_R,ind`.
4. **No finite/completed promotion.** Q-243/Q-279 zeros remain exact
   restriction targets, not the completed verdict.
5. **No R_comp conflation.** Its cycle requirement is used only to type the
   validity of `G_K`; it is not substituted for `B_ind`.
6. **No selection.** No background, complement splitting, action, contour,
   rank, anchor, torsor, orientation, or cycle representative is chosen.
7. **No evaluation.** No coupling, root, scale, eigenvalue, rank ratio, or
   measured constant is evaluated.

---

## 8. Final typed ledger

```text
C40_COMPLEMENT_SCOPED_INVERSE_RULE_IN_FORCE = true
C40_CYCLE_DIRECTION_INVERSE_USED = false | TYPE-S
C40_VOID_CLAUSE_FIRED = false | TYPE-S

P_SRC_AND_LEG_W_DERIVED = true | TYPE-P
SOURCE_ACTION_GRAPH_EXISTS = true | TYPE-P
G007_BOUNDED_RAW_CORRELATOR_EXISTS = true | TYPE-P
MAP1_AND_SOURCE_ZERO_DESCENT_EXIST = true | TYPE-P
Q243_Q279_FINITE_ORDERED_RETHESS_SHADOW_P_FREE = true | TYPE-P

DIAGNOSTIC_SOURCE_QUOTIENT_IS_PHYSICAL_COMPLEMENT = false | TYPE-R
PHYSICAL_PROPAGATING_COMPLEMENT_REALIZED = false | TYPE-U
PHYSICAL_COMPLEMENT_REDUCING_CERTIFICATE_EXISTS = false | TYPE-U
COMPLETED_PHYSICAL_COMPLEMENT_ACTION_EXISTS = false | TYPE-U
PHYSICAL_G_K_EXISTS = false | TYPE-U
STATIONARY_2PI_BLOCK_SYSTEM_EXISTS = false | TYPE-U
COMPLEMENT_INVERSE_SCHUR_EXISTS = false | TYPE-U
PHYSICAL_PI_R_IND_EXISTS = false | TYPE-U
PHYSICAL_RETHESS_RESTRICTIONS_EXIST = false | TYPE-U
P_LOC_PHYSICAL_INSTANCE_EXISTS = false | TYPE-U
B_IND_PHYSICAL_INSTANCE_EXISTS = false | TYPE-U

B_IND_DIRECT_CYCLE_INVERSE_REQUIRED = false | TYPE-S
B_IND_CHAIN_IS_CYCLE_FREE = NO_VERDICT
CYCLE_TO_COMPLEMENT_MIXING_ZERO = NO_VERDICT
G_K_CYCLE_INDEPENDENT = NO_VERDICT

P_APPEARS_IN_BOUNDED_RAW_BLOCK = present_symbolically | TYPE-P
P_APPEARS_IN_FINITE_ORDERED_RETARDED_SHADOW = absent | TYPE-P
P_APPEARS_IN_PHYSICAL_PI_R_IND = NO_VERDICT
P_APPEARS_IN_B_IND_ARGUMENT = NO_VERDICT
P_CANCELS_FROM_B_IND_ARGUMENT = NO_VERDICT

RELAY_ARE_INPUTS_PRESENT = false | TYPE-R
PHYSICAL_P_VERDICT_EXECUTED = false | TYPE-C

NEXT_WOULD_BUILD =
  COMPLEMENT_SCOPED_PHYSICAL_STATIONARY_RESPONSE_PACKAGE | TYPE-U

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

---

## 9. Custody

This lane creates only this determination artifact and its SHA-256 sidecar,
verifies the sidecar, mirrors both byte-identically to the supervised
workspace, reports the hashes and paths, and stops. It performs no gate,
register, plan, tracker, git, commit, or push action.

