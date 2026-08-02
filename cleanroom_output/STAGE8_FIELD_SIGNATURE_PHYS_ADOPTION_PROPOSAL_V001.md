# Stage 8 FIELD_SIGNATURE_PHYS Adoption Proposal V001

Date: 2026-08-02  
Lane: CODEX LANE 1  
Task: 4a, relay 372  
Register head at start: Q-288  
Status: PROPOSED_NOT_ADOPTED -- PENDING PRINCIPAL RATIFICATION (DoR-015 RESERVED)

This is the authored arm of the Q-287/Q-288 field-signature race. It is a
proposal, not a derivation and not an adopted premise. Every construction and
certificate below is conditional on the proposed fields. No proposal-level
positive is promoted to premise-conditional physical content.

```text
PROPOSAL_PAGE_FLAG = PROPOSED_NOT_ADOPTED -- PENDING PRINCIPAL RATIFICATION
DOR_015_STATUS = RESERVED

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead determination

**A COMPLETE, EXACTLY TYPED FIELD-SIGNATURE PROPOSAL EXISTS. ITS LARGEST
PRICE IS EXPLICIT: IT AUTHORS A LOCALLY COVARIANT 3+1 LORENTZIAN BACKGROUND
CATEGORY AND AN INCIDENCE-REALIZATION FAMILY. IT DOES NOT CLAIM THAT
SPACETIME WAS DERIVED FROM THE RECORD SURFACE.**

The proposal has nine named fields:

```text
FIELD_SIGNATURE_PHYS_prop := (
  F1  LocInc4,             # physical background category
  F2  Real_inc,            # ratified-incidence realization
  F3  Conn_U1,             # compact connection-field carrier
  F4  Rig_src,             # localized source rigging
  F5  U1_phys,             # CTP orientation/reality/index extension
  F6  AlgField_phys,       # algebraic represented field coordinates
  F7  BilocClass_phys,     # symmetric bilocal and raw-G class
  F8  Emb_cyl,             # T_cyl embedding and finite restrictions
  F9  ProvFam_phys         # provenance and family discipline
).
```

Fields F1-F4 and F6-F8 add seven authored structures beyond the ratified
stack. F5 extends already-ratified U1 conventions pointwise and does not alter
their signs, branch order, or reality involution. F9 is the governance and
provenance wrapper; it adds no field equation or value.

The proposal does **not** include a state, dynamics, history measure,
interacting contour limit, boundary/contact reduction, unbounded closure,
stationary solution, response kernel, induced coefficient, or evaluation
rule. Those remain the separately accounted analytic operations in Q-288.

```text
FIELD_SIGNATURE_PHYS_PROPOSAL_WRITTEN = true [PROPOSAL-LEVEL FACT]
PROPOSED_COMPONENT_COUNT = 9 [PROPOSAL-LEVEL COUNT]
PROPOSED_NEW_AUTHORED_STRUCTURE_COUNT = 7 [PROPOSAL-LEVEL COUNT]
INHERITED_U1_EXTENSION_COUNT = 1 [PROPOSAL-LEVEL COUNT]
GOVERNANCE_WRAPPER_COUNT = 1 [PROPOSAL-LEVEL COUNT]

FIELD_SIGNATURE_PHYS_ADOPTION_STATUS = PENDING_DOR015_PRINCIPAL_RATIFICATION

FIELD_SIGNATURE_PHYS_DERIVED_FROM_RECORD_SURFACE = false | TYPE-S |
  roots: authored arm sources through Q-288 |
  exclusions: independent derivation arm and any later result |
  fences: none |
  query: "Does this authored proposal itself derive its smooth field signature?"

GATE_VERDICT = DRAFT_COMPLETE_FOR_INDEPENDENT_ADVERSARIAL_REVIEW
```

## 1. Preflight, scope, and authorities

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = THIS_PROPOSAL_ONLY; NO RATIFIED FIELD_SIGNATURE_PHYS
IS_THE_VERSION_CURRENT = true through Q-288 at construction start
ARE_THE_INPUTS_PRESENT = true for drafting and conditional consistency tests;
  false for physical execution, which still needs DoR-015 and Q-288 fields
```

### 1.2 Roots and exclusions

Entered roots:

```text
/Users/bgm/MB Work/alpha_supervision
/Users/bgm/MB Work/alpha-program-archive/workspace
/Users/bgm/Documents/New project/gravity_emergence_evidence_program
```

Excluded:

```text
a32_holdout/custodian_private/                         NOT ENTERED
the concurrent derivation arm                         NOT READ OR COORDINATED
alpha/kappa/coupling/root/scale evaluation            NOT PERFORMED
rank-pair selection or ratio evaluation               NOT PERFORMED
measured-constant comparison                          NOT PERFORMED
register/plan/tracker/git/commit/push                  NOT TOUCHED
```

### 1.3 Frozen authorities

| Authority | SHA-256 | Load-bearing use |
|---|---|---|
| `alpha_supervision/LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | custody, typing, act-based fences |
| `alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md` | `f7bc21b4701a6902f2ca48069448bc24d8d98f98aa6731f5689e4074ccc6eb47` | ruling set through Q-288 at start |
| `STAGE8_TASK4A_RAW_G_SOURCE_TO_PHYSICAL_FIELD_LIFT_CONSTRUCTION_AND_TCYL_VERDICT_V001.md` | `3ef35b34cfdeb7f7b8381dce65a37d026769f29f4e2bbc6184fb581b5a394024` | Q-287 exact deficit and failed bounded route |
| `STAGE8_TASK4A_P5_MAXIMAL_TRANSPORT_CHAIN_AND_DEPENDENCE_ACCOUNTING_PACKAGE_V002.md` | `31a738ec17696ea01e1cb6a6ee7a37a29e6c0ca24d6fb8cc050d06aed32a583f` | Q-288 six-account schema and door flags |
| `STAGE8_TASK4A_P2_PHYSICAL_SOURCE_TOPOLOGY_AND_DIFFERENTIAL_CALCULUS_CONSTRUCTION_V002.md` | `40b2af34443e051fffdc7bf2ec7025c811a98c501a82d19164596ee6f37f00c1` | live transported `ell^1` source topology and finite-core discipline |
| `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md` | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | raw-G domain, codomain, support, reality, inverse, and restrictions |
| `alpha_complete_dimension_convention_ledger_v004.md` | `bbf2bdddfcefe851e985c4db03a62906082660af9a3c639d259afc93b4bbcc66` | 3+1 units, Lorentz signature, CTP and Keldysh conventions |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U1_DOR008_ASSEMBLY_DETERMINATION_V001.md` | `1b0e928c452c10a8be72be22ff81fd7677f5045d2ad8d398a9f7f7f57b9ab3b0` | ratified branch orientation, metric, reality, source symmetry, and order |
| `STAGE8_TASK4D_STITCHING_THEOREM_GERM_INDEPENDENT_HALF_V001.md` | `430f09715146cc03dabb0e349c422ae2499cff893d4e46b490fc0870954d1cb4` | T_cyl and the unbuilt T_ref/T_phys interfaces |
| `STAGE8_TASK4D_CELLULATION_INDEPENDENCE_OD3_VERDICT_INVARIANCE_THEOREM_V001.md` | `f20639a6a1d5c8d73312bd646ceb2e0c74059c6f6206dca04032289f307e217b` | nonfactorization and exact missing geometric fields |
| `STAGE8_SOURCE_COUPLED_RECORD_TRANSITION_LAW_ADOPTION_PROPOSAL_V002.md` | `db1808e4da38cbfed8b12017885aff1bf63b0378e9971c37294e21fa08766fee` | DoR-009 E_post finite law and locality boundary |
| `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md` | `1be5f6a7e40c34586f3b5ab78f9129de0b5d2041cb6695b0e549443ddd6c6ee0` | DoR-013 incidence primitive and origin discipline |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md` | `d4cdbb6623797df6accb7dc9b24134d179bfc8e8d039c585d5c91ae23255869e` | live germ family and finite source restrictions |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md` | `1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6` | ratified C0/T_cyl carrier and source embeddings |
| `STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md` | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | Q-279 finite falsifier tuple |

### 1.4 Contract-derived component list

The list is not guessed from ordinary field theory. It is the union of the
following sealed requirements:

1. Q-287:144-154 requires `V_phys`, `I=(a,mu,x)`, represented `A^I`, completed
   bilocal source, intertwiners, connected subtraction, restrictions, topology,
   and provenance.
2. The raw-map specification:641-670 requires a symmetric physical bilocal
   source, oriented branch metric, invariant spacetime pairing, fixed reality,
   quotient, source agreement, and one common physical domain.
3. The codomain at raw-map specification:675-688 requires retarded support,
   reality, covariance, and endpoint/domain compatibility.
4. Q-287:612-627 and Q-261 identify what `T_cyl` lacks: cell/edge/path
   realization, spacetime point, connection one-form, local derivative,
   measure carrier, and response assignment.

The proposal stops at the signature inputs to those operations. It does not
manufacture the operations themselves.

### 1.5 Imported-framework disclosures

Three frameworks are imported into the authored proposal and are not reported
as corpus derivations:

1. the category-of-backgrounds shape of F1 is imported from ordinary locally
   covariant field theory;
2. smooth globally hyperbolic Lorentz geometry is imported as authored
   background structure, with the dimension and sign constrained by the live
   ledger; and
3. Hilbert source bases, trace ideals, Banach completions, and continuous bilinear
   duals are imported functional analysis.

They apply here only because the sealed raw-G contract independently asks for
background-parametric causal support, physical field indices, symmetric
bilocal sources, and a declared topology. DoR-015, if issued, adopts their use;
their ordinary status outside this program supplies no authority by itself.

## 2. Exact proposed tuple

```text
PROPOSAL_PAGE_FLAG = PROPOSED_NOT_ADOPTED -- PENDING PRINCIPAL RATIFICATION
```

### 2.1 F1 -- `LocInc4`: physical-background category

`LocInc4` is proposed as the category whose objects are tuples

```text
B = (M,g,o,t; P_M),
```

where:

1. `M` is a smooth, paracompact, four-dimensional manifold;
2. `g` is globally hyperbolic with Lorentz signature `(+---)`;
3. `o` and `t` are spatial and time orientations;
4. `P_M -> M` is a principal U(1) bundle of the already-adopted compact
   connection type.

Morphisms preserve `g`, both orientations, causal order, and the U(1) bundle
type. Incidence realizations are deliberately absent from F1 and supplied only
by F2. The object is a locally covariant background **family**. No one
manifold, metric, or bundle member is selected by the proposal.

This is the proposal's largest authored premise. The dimension and sign agree
with the live dimension ledger, but the existence and physical use of this
background category are not derived by that ledger.

```text
F1_LOCINC4_PROPOSED = true [PROPOSAL FIELD]
F1_SMOOTH_BACKGROUND_DERIVED_FROM_RECORD = false | TYPE-U |
  would-build: the independent derivation arm's record-surface realization theorem
F1_FIXED_BACKGROUND_MEMBER_SELECTED = false | TYPE-S |
  roots: this proposal's object and morphism definitions |
  exclusions: downstream stationary/evaluation choice |
  fences: none |
  query: "Does F1 name a particular member (M,g)?"
```

### 2.2 F2 -- `Real_inc`: incidence realization and causal support

Over every `B`, F2 forms the complete family of tuples

```text
(B, K_rat, iota_cell),
K_rat={K_N^rat}_{N>=1},
iota_cell={iota_N},
```

where `K_rat` is the already-ratified finite signed incidence/write system,
not a newly generated complex. For every finite stage, F2 supplies an
injective cellular map

```text
iota_N : K_N^rat -> M
```

with these exact rules:

```text
R1  vertices map to events;
R2  each oriented write edge maps to a future-directed causal path gamma_j;
R3  each record cell maps to a causally convex support region D_j;
R4  signed incidence and boundary are preserved;
R5  finite locality restricts exactly on realized generator supports:
      Adj_phys(D_j,D_k) iff Adj_rat(j,k), with the same incidence sign;
R6  iota_M compose j_NM = iota_N under the ratified N<=M inclusion;
R7  Hol_N:Conn_U1(M)->U(1)^N is onto for every finite N;
R8  no one of the 1,088 support filtrations is selected; all realization
    members satisfying R1-R7 remain in the proposed family.
```

R7 is a finite failure-capable independence condition. It is present so the
`T_cyl` map in F8 is a monomorphism, not an unannounced quotient. R5 is the
required restriction of physical locality to the ratified origin. It consumes
the signed incidence primitive; it does not define a second adjacency.

```text
F2_REAL_INC_PROPOSED = true [PROPOSAL FIELD]
F2_REALIZATION_MEMBER_SELECTED = false | TYPE-S |
  roots: complete R1-R8 family |
  exclusions: downstream background or response selection |
  fences: none |
  query: "Is one realization member privileged?"
```

### 2.3 F3 -- `Conn_U1`: compact connection-field carrier

On each F1 member, define

```text
Conn_U1(P_M) = affine space of smooth U(1) connections on P_M,
Conn_U1(M)   := Conn_U1(P_M) when B fixes P_M,
Gauge_c(P_M) = compactly supported U(1) gauge transformations,
V_M = Omega^1(M;iR) / {d lambda : lambda in C_c^infinity(M;iR)},
Curr_Epost(M) = compactly supported one-currents whose boundary is confined
                to the declared incoming/outgoing E_post endpoints,
```

and use the holonomy

```text
Hol_A(gamma)=exp(integral_gamma A).
```

The physical field label is the local one-form component `mu`; after CTP
doubling the exact compound index is

```text
I=(a,mu,x),  a in {+,-},  mu in {0,1,2,3},  x in M.
```

Closed-current pairings factor through the quotient. Open path currents remain
endpoint-covariant under the already-ratified E_post representations; they are
not silently treated as gauge invariant. No gauge representative, Ward
identity, state, action, or field equation is installed. Those remain
downstream.

```text
F3_CONN_U1_PROPOSED = true [PROPOSAL FIELD]
F3_GAUGE_FIXING_SUPPLIED = false | TYPE-S |
  roots: F3 definition |
  exclusions: physical U3 quotient and Ward package |
  fences: none |
  query: "Does F3 choose a gauge representative or propagator?"
```

### 2.4 F4 -- `Rig_src`: localized source rigging

For each F2 realization, propose an incidence-indexed localized orthonormal
source basis in a declared Hilbert norm

```text
u_j in Curr_Epost(M),
support(u_j) subset D_j,
u_j(A)=integral_(gamma_j) A,
H_1(B) = closure_span{u_j} in the declared frame norm,
U_B : ell^2(N) -> H_1(B),  e_j -> u_j,
U_B^* U_B = I and U_B U_B^* = I_(H_1(B)).
```

The CTP source rigging is

```text
H_CTP(B)=H_1(B)_+ direct-sum H_1(B)_-,
D_0(B)=union_N span{u_1,...,u_N}_+/- ,
J_phys(B)=U_B(ell^1(N)_+ direct-sum ell^1(N)_-),
tau_test=the transported ell^1 norm,
D_0(B) dense-subset J_phys(B) subset H_CTP(B) subset J_phys(B)^*.
```

The stage maps are coherent under zero extension. The P2 source maps enter by

```text
K_J(J)=U_B J,
K_R(R)=U_B R U_B^*,
```

with branch doubling understood. The proposal deliberately chooses the
declared norm in which the localized incidence-indexed family is an
orthonormal basis, rather than a redundant Parseval frame or weighted Riesz
basis. This is a physical normalization premise, disclosed before any output.
It is not claimed to be forced by incidence.

```text
F4_RIG_SRC_PROPOSED = true [PROPOSAL FIELD]
F4_ORTHONORMAL_NORMALIZATION_DERIVED = false | TYPE-U |
  would-build: a record-surface theorem forcing the localized orthonormal basis and norm
F4_FRAME_MEMBER_SELECTED_AFTER_OUTPUT = false | TYPE-S |
  roots: proposal freeze order |
  exclusions: any response, p-content, or target value |
  fences: none |
  query: "Was the frame changed after inspecting a downstream output?"
```

### 2.5 F5 -- `U1_phys`: inherited CTP extension

Extend U1_008 pointwise over `(mu,x)` without changing it:

```text
B_CTP={+,-}; bar(+)=-; bar(-)=+;
epsilon(+)=+1; epsilon(-)=-1;
eta_CTP=diag(+1,-1);

A_c=(A_+ + A_-)/2;
A_delta=A_+ - A_-;

Theta_phys(A_+(f))=A_-(conjugate(f));
Theta_phys(A_-(f))=A_+(conjugate(f));

D_R,phys={R: R_IJ=R_JI and Theta_R R=R}.
```

The coordinate order is `(a,mu,x)` and the response derivative block remains
`(delta,c)`. Charge-conjugate doubling is not introduced. F5 is an extension
of ratified branch grammar, not a new CTP choice.

```text
F5_U1_PHYS_EXTENSION_PROPOSED = true [PROPOSAL FIELD; INHERITED CONVENTIONS]
F5_BRANCH_SIGN_OR_ORDER_CHANGED = false | TYPE-R |
  test: direct component comparison with U1_008
F5_CHARGE_CONJUGATE_DOUBLING_INSERTED = false | TYPE-S |
  roots: F5 definitions |
  exclusions: none |
  fences: none |
  query: branch and involution generators
```

### 2.6 F6 -- `AlgField_phys`: algebraic field-coordinate representation

For each background, let `Cyl_poly(Conn_U1(M))` be the complex algebra of
polynomial cylinder functions generated by the smeared affine coordinates

```text
A(f): Conn_U1(M) -> C,
A(f)(A)=f(A),
```

for `f in J_phys(B)`, modulo test-gauge exact directions. Use two CTP copies,
the backward copy opposite-ordered as in C0_008. Represent the generators by
multiplication on the common algebraic cylinder domain:

```text
(pi_alg(A_a(f)) Psi)(A_+,A_-)
  = A_a(f) Psi(A_+,A_-).
```

This supplies an algebraic represented `A^I` without a scalar product, state,
measure, commutator, symplectic form, or closure. The latter omissions are
intentional: adding CCR/Weyl relations would pre-form dynamics and the domain
operation that Q-288 keeps separate.

```text
F6_ALG_FIELD_PHYS_PROPOSED = true [PROPOSAL FIELD]
F6_STATE_OR_MEASURE_SUPPLIED = false | TYPE-S |
  roots: algebra and multiplication representation above |
  exclusions: Q-288 measure operation |
  fences: none |
  query: every defining datum of pi_alg
F6_CCR_OR_FIELD_EQUATION_SUPPLIED = false | TYPE-S |
  roots: F6 relation set |
  exclusions: downstream dynamics |
  fences: none |
  query: commutators, symplectic forms, kinetic operators, equations of motion
```

### 2.7 F7 -- `BilocClass_phys`: source and raw-G class

Propose the physical source and bilocal classes

```text
E_J,phys(B) = J_phys(B),
E_R,phys(B) = S_1,sym(H_CTP(B)),

Bil_phys(B) = Bil_cont(J_phys(B) x J_phys(B); C),
RawGClass(B)=Bil_phys(B) intersect CTP-real symmetric forms.
```

`Bil_phys` carries the bounded-bilinear norm induced by the transported
`ell^1` source norm. The primary object is a continuous bilinear form; kernel
notation is a representation in the continuous source dual and introduces no
additional completion. The connected subtraction is typed by the common
codomain map

```text
Conn_B : J_phys(B)^* x J_phys(B)^* -> Bil_phys(B),
Conn_B(alpha,beta)(f,h)=alpha(f) beta(h).
```

F7 does not assert that a physical scalar functional exists, that raw `G` has
been differentiated, or that the displayed subtraction has been executed.

The finite-current core `D_0` is dense in `J_phys` by the authored ell-one
completion, and finite restrictions are evaluations on the frame modes.
Hence, conditional on the proposed source norm, a continuous bilinear form killed by every finite
restriction is zero. This is the proposal's separation certificate; it does
not follow from the current ratified stack.

```text
F7_BILOC_CLASS_PROPOSED = true [PROPOSAL FIELD]
F7_RAW_G_CONSTRUCTED = false | TYPE-U |
  would-build: scalar physical functional/measure, source differentiation,
               connected subtraction, and Q-279 restriction execution
F7_FINITE_CORE_DENSITY_IS_AUTHORED_PREMISE = true [PROPOSAL PRICE]
```

### 2.8 F8 -- `Emb_cyl`: canonical embedding and restrictions

For every finite stage define the pullback of holonomy functions

```text
Emb_N : C(U(1)^N) -> C_b(Conn_U1(M)),
(Emb_N f)(A)=f(Hol_A(gamma_1),...,Hol_A(gamma_N)).
```

F2-R7 makes the finite holonomy map onto. Therefore `Emb_N` is an injective
isometric star-homomorphism. Naturality F2-R6 gives

```text
Emb_M compose j_NM = Emb_N
```

on the finite cylinder algebra, so the universal C-star property yields

```text
Emb_cyl:T_cyl -> C_b(Conn_U1(M)_+ x Conn_U1(M)_-).
```

The image is the bounded holonomy-cylinder subalgebra. It is not identified
with the unbounded linear field coordinates or the raw correlator. In
particular, F8 does not revive Q-287's refuted unweighted trace-class-to-
`T_cyl` bilocal map.

The proposed physical restriction maps are

```text
rho_A,N(A)=(Hol_A(gamma_j))_(j<=N),
rho_J,N(f)=(<u_j,f>)_(j<=N),
rho_R,N(R)=(<u_j,R u_k>)_(j,k<=N),
rho_G,N(G)=(G(u_j,u_k))_(j,k<=N).
```

They are fixed before any physical output.

```text
F8_EMB_CYL_PROPOSED = true [PROPOSAL FIELD]
F8_TCYL_IDENTIFIED_WITH_FULL_FIELD_ALGEBRA = false | TYPE-R |
  test: bounded holonomy cylinders and algebraic linear field coordinates have
        different carriers and operations
F8_Q287_REFUTED_BILOCAL_MAP_REINSTATED = false | TYPE-R |
  test: F8 never maps completed trace-class R into the T_cyl sup norm
```

### 2.9 F9 -- `ProvFam_phys`: provenance and family discipline

F9 freezes the full tuple before output and records:

```text
ProvFam_phys := (
  hashes of DoR-008, DoR-009, DoR-013, DoR-014 descendants,
  LocInc4 and complete F2 realization family,
  all F3-F8 choices and topologies,
  no selected anchor, rank pair, realization, or background,
  naturality requirement for every future consumer,
  DoR-008 finite restriction falsifier,
  Q-279 full-tuple restriction target,
  Q-285 class-formation door flags,
  no post-output supplementation
).
```

Any future consumer must either be natural over this whole family or carry an
independently ratified member-selection rule. Equality of unavailable outputs
does not count as family invariance.

```text
F9_PROV_FAM_PROPOSED = true [PROPOSAL FIELD]
POST_OUTPUT_SUPPLEMENTATION_STATUS = FORBIDDEN_VOID_CONDITION
```

## 3. Choice table and true authorship price

```text
PROPOSAL_PAGE_FLAG = PROPOSED_NOT_ADOPTED -- PENDING PRINCIPAL RATIFICATION
```

| Field | Proposed choice | Alternatives considered | Why this member is minimal for the sealed contract | Void condition |
|---|---|---|---|---|
| F1 `LocInc4` | all oriented, time-oriented, globally hyperbolic `3+1` Lorentzian U(1) backgrounds | one fixed `(M,g)`; nonsmooth causal locale; Euclidean background | preserves the sealed four-dimensional and retarded grammar without selecting an evaluation background or duplicating F2 | category empty; signature differs from `(+---)`; no causal support operation can be stated |
| F2 `Real_inc` | complete family of coherent, causal, incidence-preserving realizations | select one of 1,088 support filtrations; arbitrary non-incidence supports; no realization | consumes the ratified primitive while refusing a hidden member choice | adjacency, orientation, zero-extension, or finite holonomy-surjectivity failure |
| F3 `Conn_U1` | compact U(1) connection one-form modulo compact exact test directions | curvature-only field; noncompact additive field; generic vector field | raw G's source couples to `A`, while compact holonomy is already ratified | finite characters fail to equal realized U(1) holonomies or an extra gauge scale appears |
| F4 `Rig_src` | incidence-indexed localized orthonormal source basis in the declared norm | redundant Parseval frame; weighted/Riesz basis; arbitrary basis; no Hilbert rigging | gives unique source coordinates and one declared norm in which linear and trace-class bilocal sources can be retested | no such localized basis; zero-extension fails; basis normalization becomes output-dependent |
| F5 `U1_phys` | pointwise extension of U1_008 | reversed branch metric; changed Keldysh normalization; charge-conjugate doubling | no new CTP choice is needed; the finite conventions already fix it | any finite branch, reality, source symmetry, or `(delta,c)` restriction differs |
| F6 `AlgField_phys` | polynomial cylinder coordinate algebra with multiplication representation | Weyl/CCR algebra; Fock representation; bounded holonomy algebra only | gives represented field coordinates without importing dynamics, state, or closure | relation set requires a state/measure or changes E_post/compact holonomy |
| F7 `BilocClass_phys` | symmetric trace-class source, bounded-bilinear raw class on the transported `ell^1` source space, dense finite core | Hilbert-Schmidt source; norm C-star raw class; weak-star/bidual class; pure finite cylinders | matches P2's source topology and permits contact terms without adjoining a second completion | density or continuity fails; a nonzero all-finite-invisible bilinear survives |
| F8 `Emb_cyl` | generator-preserving holonomy monomorphism and frame restrictions | quotient map; weighted generator map; no T_cyl embedding | canonical once F2/F3 are given and preserves every finite character | finite holonomy map not onto, monomorphism fails, or restriction square fails |
| F9 `ProvFam_phys` | family-level freeze and natural consumers | select background/realization now; permit post-output completion | keeps the proposal target-blind and makes every future selection explicit | hidden member selection, missing topology flag, or post-output mutation |

The true ask is not "assume a field exists." It is:

```text
AUTHORED_ASK = (
  locally covariant smooth Lorentzian background family,
  causal incidence realization,
  compact connection carrier,
  localized orthonormal source rigging,
  algebraic field-coordinate representation,
  separated bilocal/raw-G topology,
  canonical T_cyl holonomy embedding
).
```

The inherited U1 extension and the governance wrapper are binding parts of the
proposal but are not counted as new physical structures.

## 4. Consistency obligations and proposal-level certificates

```text
PROPOSAL_PAGE_FLAG = PROPOSED_NOT_ADOPTED -- PENDING PRINCIPAL RATIFICATION
```

### 4.1 C1 -- E_post orientation

DoR-009 fixes the forward finite law to attach the character once to the
written output. F2 maps every write edge to a future-directed path. F5 retains
the forward `+` branch and opposite/backward `-` branch. F8 sends the finite
character to holonomy on that same path:

```text
U_(e_j) -> Hol_A(gamma_j),
Theta_phys(Hol_+(gamma_j))=Hol_-(gamma_j)^*.
```

No pre-write factor or `E_conj` endpoint representation is introduced. The
proposal changes the carrier of the character, not its attachment order.

```text
C1_E_POST_ORIENTATION = PASS_AS_PROPOSAL |
  certificate: same outgoing edge, same plus branch, adjoint backward branch
```

### 4.2 C2 -- incidence locality

F2-R4 and R5 make physical support pull back to the existing signed incidence:

```text
iota_N^*(boundary/support adjacency)=boundary/incidence of K_N^rat.
```

Removing one incidence edge removes the corresponding admitted local
adjacency. Adding a physical adjacency not in the finite primitive violates
R5. The condition can therefore fail and is not a decorative compatibility
statement.

```text
C2_INCIDENCE_LOCALITY = PASS_AS_PROPOSAL |
  certificate: exact pullback rule with add/remove-edge victims
```

### 4.3 C3 -- canonical T_cyl embedding

For an onto map `q:X->Y`, pullback `q^*:C(Y)->C(X)` is injective and
isometric. F2-R7 applies this finite-stage theorem to `Hol_N`; F2-R6 makes the
maps compatible under `N<=M`. The inductive universal property then gives F8.

This is a mathematical certificate conditional on the authored F2 fields. It
does not derive F2-R7 from the record structure.

```text
C3_TCYL_EMBEDDING = PASS_AS_PROPOSAL |
  premise-price: finite holonomy surjectivity in F2-R7
```

### 4.4 C4 -- DoR-008 finite restriction discipline

The proposal supplies a restriction target per component:

| Component | Finite restriction obligation |
|---|---|
| F1/F2 | recover the same finite signed incidence and E_post orientation |
| F3 | recover each compact character as path holonomy |
| F4 | recover the finite source basis and zero extension |
| F5 | recover U1_008 exactly |
| F6 | recover finite algebraic field insertions without adding a scalar state |
| F7 | recover finite symmetric bilocal coefficients |
| F8 | recover C0/T_cyl generators and restrictions |

These component squares are posed by the proposal. The physical scalar raw
`G`, connected subtraction, Q-279 tuple, and retarded image are not constructed
here, so the standing falsifier is armed but not executed.

```text
C4_COMPONENT_RESTRICTION_SQUARES_POSED = true [PROPOSAL-LEVEL FACT]
C4_Q279_FULL_TUPLE_REPRODUCED = false | TYPE-U |
  would-build: scalar physical functional, raw-G differentiation, connected
               subtraction, and execution of every rho_G,N comparison
```

### 4.5 C5 -- B14-style noncircularity

Each obligation is antecedent to the output it constrains:

| Obligation | Reads only | Forbidden read |
|---|---|---|
| E_post orientation | ratified edge, branch, endpoint law | response or field value |
| incidence locality | signed incidence and support pullback | raw `G`, `p`, or target |
| T_cyl embedding | holonomy maps and C-star generators | correlator output |
| finite restriction | component input and ratified finite carrier | completed response |
| topology/tail | declared class and restriction kernels | desired cancellation |

The mutation test is explicit: changing an output while holding these inputs
fixed cannot change membership in the proposal. Changing a listed input can.

```text
C5_B14_STYLE_NONCIRCULARITY = PASS_AS_PROPOSAL |
  test: fixed-input output mutation leaves membership unchanged
```

## 5. Q-288 class-formation door flags

```text
PROPOSAL_PAGE_FLAG = PROPOSED_NOT_ADOPTED -- PENDING PRINCIPAL RATIFICATION
```

### 5.1 Door A -- T_cyl to physical holonomy cylinders

```text
CLASS_FORMATION_DOOR_FLAGS_A := (
  input_class=T_cyl norm C-star,
  input_topology=C-star norm,
  input_restrictions=canonical finite-coordinate retractions,
  formation_or_completion_operation=F8 holonomy pullback monomorphism,
  output_class=bounded holonomy-cylinder C-star subalgebra,
  output_topology=sup norm,
  output_restrictions=finite holonomy coordinates,
  topology_changed=false,
  every_limit_named=true,
  limit_topology=C-star norm,
  weak_star_invoked=false,
  bidual_invoked=false,
  distributional_completion_invoked=false,
  nonseparating_extension_invoked=false,
  Tail_output={0} conditional on F2-R7,
  created_tail_image=0 by injective isometric embedding,
  class_separation_proved=true conditional on F2-R7,
  quotient_exactness_proved=NOT_APPLICABLE,
  closure_uniqueness_proved=true by C-star universal property,
  restriction_square=PASS_AS_PROPOSAL,
  Q279_full_tuple_reproduced=TYPE-U | would-build: physical scalar raw-G and Q-279 restriction run,
  common_origin_provenance=TYPE-U | would-build: ratified descent from the common microscopic origin,
  target_independence=PASS_AS_PROPOSAL,
  door_verdict=CLOSED_SEPARATED_ZERO_CREATED_TAIL_AS_PROPOSAL
).
```

### 5.2 Door B -- finite source modes to Hilbert source carrier

```text
CLASS_FORMATION_DOOR_FLAGS_B := (
  input_class=finite-support source modes,
  input_topology=finite-dimensional norm at each N,
  input_restrictions=coordinate truncations,
  formation_or_completion_operation=orthonormal Hilbert completion,
  output_class=H_CTP(B),
  output_topology=Hilbert norm,
  output_restrictions=orthogonal frame truncations,
  topology_changed=true,
  every_limit_named=true,
  limit_topology=Hilbert norm,
  weak_star_invoked=false,
  bidual_invoked=false,
  distributional_completion_invoked=false,
  nonseparating_extension_invoked=false,
  Tail_output={0} conditional on frame completeness,
  created_tail_image=0 by dense orthonormal span,
  class_separation_proved=true conditional on F4,
  quotient_exactness_proved=NOT_APPLICABLE,
  closure_uniqueness_proved=true for a fixed frame norm,
  restriction_square=PASS_AS_PROPOSAL,
  Q279_full_tuple_reproduced=TYPE-U | would-build: physical scalar raw-G and Q-279 restriction run,
  common_origin_provenance=TYPE-U | would-build: ratified descent from the common microscopic origin,
  target_independence=PASS_AS_PROPOSAL,
  door_verdict=CLOSED_SEPARATED_ZERO_CREATED_TAIL_AS_PROPOSAL
).
```

### 5.3 Door C -- bilocal trace-class completion

```text
CLASS_FORMATION_DOOR_FLAGS_C := (
  input_class=finite symmetric matrices on frame modes,
  input_topology=finite trace norm,
  input_restrictions=finite matrix corners,
  formation_or_completion_operation=trace-norm completion under R->U_B R U_B^*,
  output_class=S_1,sym(H_CTP(B)),
  output_topology=trace norm,
  output_restrictions=frame matrix corners,
  topology_changed=true,
  every_limit_named=true,
  limit_topology=trace norm,
  weak_star_invoked=false,
  bidual_invoked=false,
  distributional_completion_invoked=false,
  nonseparating_extension_invoked=false,
  Tail_output={0} conditional on trace-norm density,
  created_tail_image=0 by finite-rank density in trace class,
  class_separation_proved=true conditional on F4,
  quotient_exactness_proved=NOT_APPLICABLE,
  closure_uniqueness_proved=true for trace-norm completion,
  restriction_square=PASS_AS_PROPOSAL,
  Q279_full_tuple_reproduced=TYPE-U | would-build: physical scalar raw-G and Q-279 restriction run,
  common_origin_provenance=TYPE-U | would-build: ratified descent from the common microscopic origin,
  target_independence=PASS_AS_PROPOSAL,
  door_verdict=CLOSED_SEPARATED_ZERO_CREATED_TAIL_AS_PROPOSAL
).
```

### 5.4 Door D -- test fields to bounded-bilinear raw class

```text
CLASS_FORMATION_DOOR_FLAGS_D := (
  input_class=J_phys(B) x J_phys(B),
  input_topology=tau_test, the transported ell^1 norm,
  input_restrictions=frame-mode evaluations,
  formation_or_completion_operation=continuous-bilinear dual formation,
  output_class=RawGClass(B),
  output_topology=bounded-bilinear operator norm,
  output_restrictions=rho_G,N,
  topology_changed=false,
  every_limit_named=true,
  limit_topology=NOT_APPLICABLE; dual formation takes no new limit,
  weak_star_invoked=false,
  bidual_invoked=false,
  distributional_completion_invoked=false,
  nonseparating_extension_invoked=false,
  Tail_output={0} conditional on F7 finite-core density,
  created_tail_image=0 conditional on continuity plus density,
  class_separation_proved=true conditional on F7 density,
  quotient_exactness_proved=TYPE-U | would-build: physical quotient map on RawGClass,
  closure_uniqueness_proved=TYPE-U | would-build: physical raw-G image and its closure proof,
  restriction_square=TYPE-U | would-build: physical raw-G image and all rho_G,N maps,
  Q279_full_tuple_reproduced=TYPE-U | would-build: physical scalar raw-G and Q-279 restriction run,
  common_origin_provenance=TYPE-U | would-build: ratified descent from the common microscopic origin,
  target_independence=PASS_AS_PROPOSAL,
  door_verdict=NO_VERDICT | prerequisite: physical raw-G image, quotient, and restrictions
).
```

Door D uses the Banach-dual class already induced by P2's transported `ell^1`
source norm. No weak-star, bidual, or distributional completion is proposed,
and continuity plus finite-core density separates the class. Quotient
exactness, physical restriction, and the actual image remain unbuilt.
Therefore Door D is not reported closed.

```text
UNFLAGGED_CLASS_FORMATION_STEP_FOUND = false | TYPE-S |
  roots: F1-F9 and Doors A-D |
  exclusions: future analytic operations not performed here |
  fences: none |
  query: every completion, closure, dual, limit, and topology word in the proposal

WEAK_STAR_OR_BIDUAL_STEP_PROPOSED = false | TYPE-S |
  roots: Doors A-D |
  exclusions: alternatives retained in the choice table |
  fences: none |
  query: weak-star, bidual, nonseparating extension

PHYSICAL_TAIL_CREATION_STATUS = NO_VERDICT |
  prerequisite: execute Door D on the physical raw-G image and its restriction maps
```

## 6. Consumer test statements

```text
PROPOSAL_PAGE_FLAG = PROPOSED_NOT_ADOPTED -- PENDING PRINCIPAL RATIFICATION
```

### 6.1 Raw-G lift: bounded-extension rerun

Q-287's refutation remains valid in its codomain:

```text
S_1(H_CTP) -> T_cyl with the unweighted character-product sup norm
```

is unbounded. The proposed rerun is a different, predeclared test:

```text
Domain:   S_1,sym(H_CTP(P2))
Map:      R -> U_B R U_B^*
Codomain: S_1,sym(H_CTP(B))
Topology: trace norm
Then:     insert the resulting bilocal coefficient on the common algebraic
          cylinder domain and test continuity/closability separately.
```

The rerun must check:

1. the exact Q-287 rank-one moving-support family;
2. uniform trace-norm boundedness of the coefficient map;
3. the operator-domain action of the quadratic insertion;
4. every finite restriction square;
5. the connected-subtraction codomain;
6. Door D's image intersection with physical `Tail_R`; and
7. the full Q-279 tuple.

This proposal does not execute that test and does not predict its verdict.

```text
RAW_G_BOUNDED_EXTENSION_RERUN_POSED = true [PROPOSAL-LEVEL FACT]
RAW_G_BOUNDED_EXTENSION_RERUN_EXECUTED = false | TYPE-U |
  would-build: ratified F1-F9, scalar physical functional, operator-domain
               realization, and the seven checks above
```

### 6.2 Four analytic fields

| Q-288 field account | Structure supplied by the proposed signature | Still not supplied |
|---|---|---|
| measure | `M`, causal support regions, test spaces, and Lorentz volume-density carrier | branch-joint history measure, marginal consistency, scalar functional, descended `dmu_C` operation |
| contour | time orientation, pointwise U1 doubling, common/difference indices, and bounded-bilinear output class | interacting `i-epsilon` family, boundary-value map, limit, retarded prescription |
| boundary/contact | realized cell boundaries, causal support strata, incidence pullback, and finite restriction maps | physical boundary form, contacts, null/private reduction, microcausal gluing theorem |
| domain closure | common algebraic cylinder domain and rigged source triple | closability, self-adjoint/closed extension, graph/resolvent topology, Ward-compatible endpoint domain |

The signature gives each analytic operation a carrier on which it can be
posed. It does not perform any of the four operations.

### 6.3 Other consumers

```text
raw-G lift gains: field indices, represented algebraic A(f), source rigging,
                  bilocal codomain, T_cyl embedding, restrictions, topology;

background fiber gains: the same field carrier and restriction floor;
background still lacks: Legendre/stationary/evaluation rule;

stationary Schur gains: a common proposed block carrier;
stationary Schur still lacks: Gamma_2PI blocks, stationary solution, inverse;

class formation gains: explicit Doors A-D;
class formation still lacks: physical Door-D image and tail certificate.
```

```text
RAW_G_CONSUMER_READY_FOR_EXECUTION = false | TYPE-U |
  would-build: DoR-015 ratification plus measure, contour, boundary/domain,
               scalar functional, and source differentiation
FOUR_ANALYTIC_FIELD_OPERATIONS_BUILT = false | TYPE-U |
  would-build: the four Q-288 physical interfaces on the proposed carriers
```

## 7. Mandatory self-kill passes

```text
PROPOSAL_PAGE_FLAG = PROPOSED_NOT_ADOPTED -- PENDING PRINCIPAL RATIFICATION
```

### K1 -- hidden-adoption audit

The following are new authorship and are not attributed to the sealed record:

```text
smooth locally covariant Lorentzian background category;
causal cellular realization family;
connection-field carrier on that category;
localized incidence-indexed orthonormal source basis;
algebraic multiplication representation;
Banach-dual bilinear output class and finite-density premise;
holonomy embedding as the physical bridge.
```

```text
HIDDEN_ADOPTION_FOUND = false | TYPE-S |
  roots: F1-F9 and the choice table |
  exclusions: alternatives explicitly retained |
  fences: none |
  query: every datum not already present in DoR-008/009/013/014
```

### K2 -- `(M,g)` and smooth-structure audit

F1 openly introduces smooth `(M,g)` structure. This is not a finding that no
smooth structure is used; it is the central price of the authored arm. DoR-015
would knowingly adopt it. No sentence says that `T_cyl`, incidence, or the
dimension ledger derives it.

```text
SMOOTH_STRUCTURE_USED = true [DISCLOSED PROPOSAL PRICE]
SMOOTH_STRUCTURE_SMUGGLED_AS_DERIVED = false | TYPE-S |
  roots: F1-F9, authorities, and choice table |
  exclusions: no concurrent derivation-arm result read |
  fences: none |
  query: every occurrence of M, g, smooth, Lorentz, causal, and volume
```

### K3 -- answer-defined membership and target tuning

No F1-F9 membership predicate contains `p`, `p_ch`, a response coefficient,
an induced stiffness, a residual, a root, alpha, or a measured target. The
The orthonormal source normalization is selected for a source-map topology before any output,
not to obtain a response value. Door D remains undecided rather than being
declared tail-free for convenience.

```text
ANSWER_DEFINED_COMPONENT_FOUND = false | TYPE-S |
  roots: all F1-F9 membership predicates |
  exclusions: consumer consequences in Section 6 |
  fences: none |
  query: every component-definition token and dependency

TARGET_TUNING_FOUND = false | TYPE-S |
  roots: proposal construction trace |
  exclusions: no physical output was computed |
  fences: no target-aware act permitted or performed |
  query: p, p_ch, response, stiffness, residual, root, alpha, measured
```

### K4 -- duplication and contradiction audit

The proposal consumes rather than replaces:

```text
DoR-009 E_post orientation;
DoR-013 signed-incidence primitive;
DoR-008 T_cyl and U1_008;
DoR-014 source/germ restrictions.
```

F2 has no independent adjacency field. F5 has no independent branch sign.
F8 leaves T_cyl as a proper bounded subalgebra. The proposal adds a realization
and field carrier around these objects.

```text
RATIFIED_INCIDENCE_DUPLICATED = false | TYPE-R |
  test: F2 locality is the pullback of K_N^rat and has no second generator
RATIFIED_CTP_GRAMMAR_CONTRADICTED = false | TYPE-R |
  test: F5 component equality with U1_008
TCYL_COLLAPSED_WITH_PHYSICAL_FIELD_ALGEBRA = false | TYPE-R |
  test: F8 proper-subalgebra and signature comparison
```

### K5 -- refuted-route laundering audit

Q-287's unweighted `S_1 -> T_cyl` map remains refuted. The proposed test uses
a new trace-class coefficient codomain declared in advance. It may pass or
fail for its own operator-domain reasons; no claim here repairs the old map.

```text
Q287_TYPE_R_REFUTATION_REPAIRED_OR_WITHDRAWN = false | TYPE-S |
  roots: Q-287 theorem and Sections 2.4, 2.7, 6.1 |
  exclusions: no execution of the new test |
  fences: none |
  query: domain, codomain, and topology identity
```

### K6 -- analytic-field smuggling audit

F1 supplies a volume-density carrier, F2 support/boundaries, F5 contour
orientation, and F6 an algebraic domain. It does not supply a history measure,
contour limit, contact form, or closed operator. Section 6.2 records the exact
boundary.

```text
Q288_FIELD_OPERATION_SMUGGLED_INTO_SIGNATURE = false | TYPE-S |
  roots: F1-F9 operation inventory |
  exclusions: carriers and interfaces explicitly allowed by this task |
  fences: none |
  query: integration, marginalization, epsilon limit, contact reduction,
         closure, self-adjoint extension, stationary solve
```

### K7 -- family-selection and finite-authority audit

No `(M,g)`, realization, frame member, rank pair, or anchor member is selected.
This leaves a real burden: physical consumers must be natural over the family
or later selection must be independently ratified. The DoR-008/Q-279 physical
restriction test remains unexecuted and is not called a pass.

```text
HIDDEN_FAMILY_MEMBER_SELECTION_FOUND = false | TYPE-S |
  roots: F1, F2, F4, F9 |
  exclusions: no downstream evaluation member |
  fences: none |
  query: constants, distinguished members, evaluation backgrounds, frame labels

DOR008_FULL_PHYSICAL_FALSIFIER_PASS = NO_VERDICT |
  prerequisite: ratified signature, raw-G construction, and Q-279 restriction run
```

## 8. Void conditions and adversarial review package

Any one of these kills the proposal as written:

```text
V1  no nonempty F1/F2 family satisfies the exact finite incidence constraints;
V2  E_post orientation or U1 reality fails under finite restriction;
V3  finite holonomy surjectivity fails and Emb_cyl becomes a quotient;
V4  no incidence-indexed localized orthonormal source basis exists;
V5  F4 introduces an output-dependent weight or physical scale;
V6  Door D admits a nonzero all-finite-invisible continuous bilinear despite
    the declared finite-core density;
V7  the raw-G source contract requires a structure omitted from F1-F9;
V8  any F1-F9 field pre-forms state, dynamics, the analytic field operations,
    response, or target output;
V9  a later derivation supplies an inequivalent field signature and the
    principal selects that route;
V10 any completion, topology, or tail-creation act is found unflagged.
```

Recommended independent attacks:

1. construct an F2 no-go or a finite stage where holonomy surjectivity and
   incidence locality conflict;
2. attack localized orthonormal source bases under nested zero extension;
3. rerun Q-287's moving-support family in F4/F7 without assuming bounded field
   multiplication;
4. search Door D for a continuous bilinear element killed by every `rho_G,N`;
5. test whether F1's smooth locally covariant family is more than raw G needs;
6. test whether F6's algebraic multiplication carrier is too weak to support
   the physical connected subtraction;
7. compare all finite branch/reality maps byte for byte with U1_008 and E_post;
8. inspect every proposal predicate for disguised dependence on a consumer
   output.

```text
PROPOSAL_SELF_KILL_STATUS = SURVIVED_INTERNAL_PASS_WITH_DOOR_D_OPEN
ADVERSARIAL_REVIEW_REQUIRED = true [GATE PROCESS FACT]
DOR_015_RATIFICATION_READY = false | TYPE-C |
  constraint: independent derivation race and adversarial review not adjudicated |
  release: principal adjudicates the race after cross-review
```

## 9. Final proposal ledger

```text
PROPOSAL_PAGE_FLAG = PROPOSED_NOT_ADOPTED -- PENDING PRINCIPAL RATIFICATION
DOR_015_STATUS = RESERVED
GATE_VERDICT = DRAFT_COMPLETE_FOR_INDEPENDENT_ADVERSARIAL_REVIEW

FIELD_SIGNATURE_PHYS_PROPOSAL_WRITTEN = true [PROPOSAL-LEVEL FACT]
FIELD_SIGNATURE_PHYS_ADOPTION_STATUS = PENDING_DOR015_PRINCIPAL_RATIFICATION
FIELD_SIGNATURE_PHYS_DERIVED_FROM_RECORD_SURFACE = false | TYPE-S |
  roots: this authored proposal |
  exclusions: concurrent derivation arm |
  fences: none |
  query: proposal provenance

F1_LOCINC4_PROPOSED = true [PROPOSAL FIELD]
F2_REAL_INC_PROPOSED = true [PROPOSAL FIELD]
F3_CONN_U1_PROPOSED = true [PROPOSAL FIELD]
F4_RIG_SRC_PROPOSED = true [PROPOSAL FIELD]
F5_U1_PHYS_EXTENSION_PROPOSED = true [PROPOSAL FIELD]
F6_ALG_FIELD_PHYS_PROPOSED = true [PROPOSAL FIELD]
F7_BILOC_CLASS_PROPOSED = true [PROPOSAL FIELD]
F8_EMB_CYL_PROPOSED = true [PROPOSAL FIELD]
F9_PROV_FAM_PROPOSED = true [PROPOSAL FIELD]

DOOR_A_VERDICT = CLOSED_SEPARATED_ZERO_CREATED_TAIL_AS_PROPOSAL
DOOR_B_VERDICT = CLOSED_SEPARATED_ZERO_CREATED_TAIL_AS_PROPOSAL
DOOR_C_VERDICT = CLOSED_SEPARATED_ZERO_CREATED_TAIL_AS_PROPOSAL
DOOR_D_VERDICT = NO_VERDICT |
  prerequisite: physical raw-G image, quotient, and restriction maps

RAW_G_BOUNDED_EXTENSION_RERUN_POSED = true [PROPOSAL-LEVEL FACT]
RAW_G_BOUNDED_EXTENSION_RERUN_EXECUTED = false | TYPE-U |
  would-build: ratified F1-F9 plus the seven-check physical rerun
RAW_G_CONSUMER_READY_FOR_EXECUTION = false | TYPE-U |
  would-build: DoR-015 plus measure, contour, boundary/domain, scalar functional, and differentiation
FOUR_ANALYTIC_FIELD_OPERATIONS_BUILT = false | TYPE-U |
  would-build: the four Q-288 physical operations on the proposed carriers
DOR008_FULL_PHYSICAL_FALSIFIER_PASS = NO_VERDICT |
  prerequisite: ratified signature and completed physical restriction run

SMOOTH_STRUCTURE_USED = true [DISCLOSED PROPOSAL PRICE]
SMOOTH_STRUCTURE_SMUGGLED_AS_DERIVED = false | TYPE-S |
  roots: F1-F9, authorities, and choice table |
  exclusions: no concurrent derivation-arm result read |
  fences: none |
  query: every occurrence of M, g, smooth, Lorentz, causal, and volume
UNFLAGGED_CLASS_FORMATION_STEP_FOUND = false | TYPE-S |
  roots: Doors A-D |
  exclusions: future operations |
  fences: none |
  query: all class/topology changes
TARGET_TUNING_FOUND = false | TYPE-S |
  roots: F1-F9 definitions |
  exclusions: consumer consequences |
  fences: none |
  query: all membership predicates

REGISTER_HEAD_AT_START = Q-288
REGISTER_HEAD_AT_SEND_TIME = Q-288
LATER_BEARING_RULING_CONSUMED = false | TYPE-S |
  roots: QUESTIONS_SETTLED_REGISTER_V001.md through Q-288 |
  exclusions: concurrent derivation arm remained unregistered and unread |
  fences: no coordination with the concurrent arm |
  query: Q-289, FIELD_SIGNATURE_PHYS, DoR-015, derivation-arm disposition

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

Custody: seal this proposal, verify its sidecar, mirror artifact and sidecar to
`/Users/bgm/MB Work/alpha-program-archive/cleanroom_output/` and
`/Users/bgm/MB Work/alpha-program-archive/workspace/`, report hashes and exact
paths, and stop. No register, plan, tracker, git, commit, push, gate, or deploy
action is performed by this lane.
