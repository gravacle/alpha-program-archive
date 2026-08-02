# Stage 8 Task 4a Cycle-Kernel Response and 2PI Descent Bridge Determination V001

Date: 2026-08-02  
Task: PASTE 392 / Task 4a  
Lane: CODEX LANE 1  
Status: **BRIDGE 1 REFUTED; THE SOURCE-KERNEL/PROBE MAP IS THE ZERO MAP AND LIFTS IN THE P2 NORM; NO PHYSICAL 2PI DESCENT EXISTS; p-VERDICT REMAINS `NO_VERDICT`**

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013,
                   DoR-014 as amended (2 + N), DoR-015

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead determination

The proposed first bridge fails on the sealed finite carrier. CTP closure and
incidence-cycle closure are different operations.

The relay also undercounts the typed objects. There are four, not three:

```text
Z_law,N       sequential relative-history CTP character;
Phi_c         V005 Gate-4 graph-cycle character;
Phi_square    the separate sealed composition-loop path-ratio phase;
R             an independent symmetric bilocal probe.
```

V005 states this distinction in its own symbol-collision clause:

> `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md:948-951` —
> “`holonomy` here means Gate-4 graph-cycle holonomy only. It is not ... the
> composition loop phase.”

Thus `Phi_c` is not the separate sealed composition-loop phase, and `R` is not
a cycle carrier. Those are typed carrier corrections, not nomenclature.

At finite `N`, the CTP law gives the character

```text
Z_law,N=product_j r_j^n,
r_j=conjugate(z_(-,j))z_(+,j),
n in {+1,-1}.
```

Its character vector is `n 1_N` on the sequential relative-history torus. On
the sealed square, the incidence boundary in edge order
`(e_a0,e_0b,e_ab,e_ba)` is

```text
partial_1 =
[[-1,-1, 0, 0],
 [ 1, 0,-1, 0],
 [ 0, 1, 0,-1],
 [ 0, 0, 1, 1]].
```

An independent exact integer check gives

```text
partial_1 ( 1, 1, 1, 1)^T = (-2,0,0, 2)^T,
partial_1 (-1,-1,-1,-1)^T = ( 2,0,0,-2)^T,
partial_1 ( 1,-1, 1,-1)^T = ( 0,0,0, 0)^T.
```

Therefore even the most favorable provisional identification `j=e` does not
send the CTP all-unit character to the admitted cycle character. The CTP
forward/backward closure is per sequential cell; the incidence closure is the
zero-boundary condition on oriented edges. CTP closure alone does not supply
the orientation-bearing cell-to-edge intertwiner that would be needed to turn
one into the other.

```text
CTP_CLOSURE_IDENTIFIES_Z_LAW_WITH_PHI_C = false | TYPE-R |
  test: exact K_square boundary calculation

Z_LAW_ALL_UNIT_CHARACTER_IS_K_SQUARE_CYCLE = false | TYPE-R |
  test: partial_1(plus_or_minus 1_4) is nonzero

V005_PHI_C_IS_THE_SEPARATE_COMPOSITION_LOOP_PHASE = false | TYPE-R |
  test: V005:948-951 explicit scope clause

R_IS_A_CYCLE_CARRIER = false | TYPE-R |
  test: Q-279 types R as an independent symmetric bilocal source
```

An intertwiner could be proposed. For example, after choosing `j=e`, the sign
operator `S=diag(1,-1,1,-1)` sends `1_4` to `c_square`. But neither `j=e` nor
`S` is supplied by the ratified CTP law. Choosing them here would select from
the unresolved sequential-label-to-incidence realization family and then
define the desired result into existence. It is not performed.

The second requested bridge has a narrower derived result. On the already
built placement of cycle directions into the physical linear-source kernel,
the bilocal probe action through the current scalar germ is exactly the zero
map:

```text
beta_N : K_N x R_N -> C,
beta_N(k,r):=D^2W_N[(k,0),(0,r)]=0,
K_N=ker L_N.
```

This zero lifts to the completed source kernel in the inherited P2 norm. It is
independent of `p` because the kernel leg vanishes before the scalar coefficient
acts. It is a source-port orthogonality theorem, not a carrier identification
and not physical 2PI dynamics.

The 2PI descent does not execute. The density argument lifts a continuous zero
inside one carrier; it cannot create the absent map from that carrier to the
stationary `Gamma_2PI` tangent system. The scalar germ factors through
`J/ker L`, so any descent using only that germ either remains singular on the
record-visible cycle sector or deletes that sector by quotienting. The latter
route is already refuted by Q-308.

```text
BRIDGE_1_VERDICT = REFUTED | TYPE-R
BRIDGE_2_VERDICT = ZERO_SOURCE_ACTION_ONLY | TYPE-P
PHYSICAL_2PI_DESCENT_VERDICT = UNBUILT | TYPE-U

P_IS_ABSENT_FROM_COMPLETED_SOURCE_KERNEL_MIXING = true | TYPE-P
P_APPEARS_IN_PHYSICAL_CYCLE_RETHESS = NO_VERDICT
P_CANCELS_FROM_PHYSICAL_CYCLE_RETHESS = NO_VERDICT
```

The exact failed first object is
`CTP_RELATIVE_HISTORY_TO_INCIDENCE_CYCLE_DYNAMICS_INTERTWINER`. Until it and
the subsequent untraced-law-to-2PI descent exist, the finite support separation
cannot be promoted to physical cancellation.

## 1. Preflight, currency, roots, and authorities

### 1.1 Preflight at send-time basis

```text
DOES_THE_OBJECT_EXIST = SPLIT |
  Z_law,N, Phi_c, Phi_square, R, K, and beta=0: yes |
  cross-carrier dynamics intertwiner and stationary 2PI descent: no | TYPE-U

IS_THE_VERSION_CURRENT = true |
  register head: Q-309 |
  no later ruling bears on this item at construction freeze

LATER_BEARING_RULING_FOUND = false | TYPE-S |
  roots: register through Q-309 at construction freeze |
  exclusions: hash-only custody change with no new register row |
  query: every row after Q-309

ARE_INPUTS_PRESENT = false | TYPE-R |
  test: no ratified cell-edge/orientation intertwiner and no stationary 2PI
        block system; the relay's bridgehead list does not compose as typed
```

The register hash changed while this lane was reading, but the head remained
Q-309 and no superseding row landed. Both observed hashes are recorded below.

### 1.2 Roots entered

1. `/Users/bgm/MB Work/alpha_supervision/LOCKED_PROCESS.md`
2. `/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md`
3. `STAGE8_TASK4A_KERNEL_SECTOR_DYNAMICS_2PI_DOMAIN_BACKGROUND_AND_P_VERDICT_DETERMINATION_V001.md`
4. `STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md`
5. `STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md`
6. `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md`
7. `STAGE8_COMPOSITION_LOOP_STRUCTURAL_PREDICTION_BUILD_V001.md`
8. `STAGE8_TASK2F_FINITE_INCIDENCE_REALIZATION_FUNCTOR_FORCING_PROTOCOL_RESULT_V001.md`
9. `STAGE8_TASK4D_STITCHING_THEOREM_GERM_INDEPENDENT_HALF_V001.md`
10. `STAGE8_TASK4A_PHYSICAL_INVERSE_SCHUR_COMPLETED_DOMAIN_AND_P_VERDICT_ATTEMPT_V001.md`
11. `STAGE8_TASK4A_P2_PHYSICAL_SOURCE_TOPOLOGY_AND_DIFFERENTIAL_CALCULUS_CONSTRUCTION_V002.md`
12. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V007.md`
13. `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md`
14. `STAGE8_TASK4A_SOURCE_TO_OUTPUT_NORMALIZATION_N_UNIQUENESS_INSTALL_AND_FULL_DOOR_D_REEXECUTION_V001.md`

All unqualified paths are rooted at the current cleanroom.

### 1.3 Frozen hashes

| Authority | SHA-256 | Load-bearing use |
|---|---|---|
| Locked process | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | fences, typing, custody |
| Register through Q-309, construction freeze | `4306122d33a9db3dbba77c8cda3751d9b2b75ab2b1adade3898525344730200d` | current standing |
| Q-309 determination | `a4c916a7cfa82c2130c82d8947c869f118e224959d7824bba45695711b4919c3` | exact finite kernel theorem and named gap |
| Ratified finite influence result | `2cd1ffcefd68ac03c6c09a4eca0dc9fe8d1adc8ac564cc0d050dfd41d79e6d0f` | `Z_law,N`, CTP carrier, operator-valued ceiling |
| Q-279 probe reference | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | exact `J/R` derivatives |
| Field signature V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | graph-cycle quotient, `u_c`, `Phi_c`, scope clause |
| Composition-loop build | `5810377123b823e680891a3337855750ac8f362951dca048dad3a78a34c79d79` | `K_square`, boundary, separate path-ratio phase |
| Realization forcing result | `a4d8b9c44fd0705ba97fd49d1e0c8373c28e12e2c3acea9409b60217b274a0f8` | 1,088 support survivors and missing operator preimage |
| Stitching theorem attempt | `430f09715146cc03dabb0e349c422ae2499cff893d4e46b490fc0870954d1cb4` | sequential labels versus incidence-complex mismatch |
| Q-308 inverse determination | `c09783785546a8d6273b2fd104f3aeea0751e83c337ee4e8ac7677d9df87f3d0` | cycle placement in `ker L` and quotient prohibition |
| P2 V002 | `40b2af34443e051fffdc7bf2ec7025c811a98c501a82d19164596ee6f37f00c1` | norm topology, calculus, finite-core density |
| Source germ V007 | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | current scalar/raw-correlator source dependence |
| Raw correlator-to-RetHess spec | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | stationary 2PI and Schur signatures |

### 1.4 Scope and queries

```text
ROOTS = current cleanroom Markdown plus the two supervision files above
EXCLUDED = a32_holdout/custodian_private; git metadata; binary/media; mirrors
WORD_BOUNDARY = case-insensitive where text was swept

QUERY_1 = Z_N intersect Phi_c / composition-loop / K_square
QUERY_2 = u_c or c_square intersect bilocal R / Q_N(R) / 2PI
QUERY_3 = CTP intersect incidence-cycle / cycle map / intertwiner / descent
QUERY_4 = stationary Gamma_AA / Gamma_AG / Gamma_GG / Gamma_GA / G_*
```

A targeted word-bounded line sweep for the exact cross-carrier combinations
returned no candidate identity. Q-309's broader intersection sweep supplies
the inherited scope-empty finding. The finite realization corpus supplies an
explicit nonuniqueness result rather than an identity.

```text
SEALED_CTP_TO_INCIDENCE_CYCLE_INTERTWINER_FOUND = false | TYPE-S |
  roots: the roots above |
  exclusions: generic co-occurrence and target-only incidence definitions |
  fences: no name transport; word-bounded matching |
  queries: QUERY_1 and QUERY_3

SEALED_CYCLE_TO_BILOCAL_R_DYNAMICS_MAP_FOUND = false | TYPE-S |
  roots: the roots above |
  exclusions: the zero derivative relation proved below |
  fences: R is an independent bilocal source |
  queries: QUERY_2
```

### 1.5 Exclusions and custody

```text
a32_holdout/custodian_private/                   NOT ENTERED
Z_law,N identified with Phi_c                    NOT DONE | TYPE-R blocks
Phi_c identified with Phi_square                 NOT DONE | TYPE-R blocks
R identified with a cycle carrier                NOT DONE | TYPE-R blocks
one of 1,088 support realizations selected        NOT DONE | TYPE-S
orientation sign map selected                    NOT DONE | TYPE-S
source Hessian identified with a 2PI block        NOT DONE | TYPE-R blocks
ker L quotiented out of the physical carrier      NOT DONE | TYPE-R blocks
measure, contour, background, domain selected     NOT DONE | TYPE-S
weak-star or bidual completion invoked            NOT DONE | TYPE-S
alpha, kappa, coupling, scale, or root             NOT COMPUTED
measured-constant comparison                      NOT PERFORMED
register, plan, tracker, git, commit, or push      NOT TOUCHED
```

## 2. The four typed carriers

### 2.1 Sequential relative-history CTP character

The ratified finite law defines
(`STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md:12-50,117-165,167-213`):

```text
z_(+,j)^n=chi_n(h_j[a_+]),
z_(-,j)^n=chi_n(h_j[a_-]),

r_j:=conjugate(z_(-,j))z_(+,j),
Z_law,N=product_(j=1)^N r_j^n.
```

The index `j` labels sequential record cells. The closure is branch-relative:
each factor compares the forward and backward history at one sequential cell.
In the character lattice of `U(1)^N`, the exponent is

```text
m_CTP=n(1,...,1).
```

`F_N=P_0+Z_law,N P_ch` remains an operator on the two source sectors after the
record sandwich. It is not the scalar physical response.

### 2.2 V005 graph-cycle character

V005 defines (`:286-385`)

```text
Q_K=U(1)^(E_K)/Gamma_K,
c in ker(B_K^T),

Phi_c([A];[A_0])
 =-i Log_0 product_(e in E_K)
   (h_e(A)h_e(A_0)^(-1))^(c_e),

d Phi_c=u_c,
u_c(a)=sum_e c_e integral_(gamma_e) a.
```

The closure is incidence-relative: `B_K^T c=0` makes vertex-rephasing factors
telescope. Its character lattice is the cycle lattice, not the sequential
cell lattice.

### 2.3 Separate composition-loop phase

The composition-loop build defines the path-ratio carrier on the selected
unfilled square (`:132-181`):

```text
u_ab u_a0 (u_ba u_0b)^(-1)=exp(i Phi_square).
```

Its graph-cycle coefficient is

```text
c_square=(1,-1,1,-1).
```

The same graph and coefficient can serve as a visible witness for V005's
cycle family. That shared witness does not identify the two phase functionals;
V005's `:948-951` explicitly withholds that identity.

### 2.4 Independent bilocal probe

Q-279 defines (`:215-239`)

```text
R in Sym(doubled finite-cell carrier),
Q_N(R)=U1-real same-cell difference/difference trace,
Xi_N[J,R]=L_N(J)-Q_N(R)/2.
```

`R` is a source port. It is not a cycle current and it is not a retarded block.
Its exact relation to `K=ker L` is obtained by differentiation in Section 4.

```text
NUMBER_OF_TYPED_OBJECTS_IN_RELAY_PREMISE = 4 | TYPE-P
THREE_CYCLE_CARRIER_DESCRIPTION_IS_CORRECT = false | TYPE-R |
  test: Phi_square is distinct and R is bilocal-source typed
```

## 3. Bridge 1: `Z_law,N` to the incidence-cycle phase

### 3.1 What a lawful bridge would have to be

A finite bridge must include at least

```text
iota_N : sequential cells -> oriented incidence edges,
S_N    : relative-history character lattice -> incidence cycle lattice,

S_N(n 1_N) in ker(B_K^T),
```

and certify:

1. branch/path orientation;
2. naturality under sequential zero-extension and finite-complex refinement;
3. preservation of the untraced transition, not merely its scalar character;
4. compatibility with the Gate-4 quotient and V005 phase charts; and
5. common-origin provenance independent of the desired response verdict.

No such tuple is ratified.

### 3.2 Exact square falsifier

The most favorable identity-like attempt is `N=4`, `j=e` in the frozen edge
order, and `S_N=Id`. It fails because

```text
partial_1(n 1_4) !=0 for n=+1 and n=-1.
```

The unique square cycle line is instead spanned by `c_square`. Thus an
orientation/sign map is necessary even after a cell-edge assignment has been
chosen.

One map satisfying only the coefficient equation is

```text
S_square=diag(1,-1,1,-1),
S_square 1_4=c_square.
```

This display proves possibility of a kinematic map, not its derivation. It is
not selected because:

* the CTP law does not assign branches to the two square paths;
* the sequential index is not an incidence-edge index;
* the map has no untraced-dynamics or state/effect certificate; and
* the finite realization forcing protocol leaves 1,088 support maps even before
  representation and operator-preimage data are supplied
  (`STAGE8_TASK2F_FINITE_INCIDENCE_REALIZATION_FUNCTOR_FORCING_PROTOCOL_RESULT_V001.md:423-590`).

```text
IDENTITY_SUPPORT_MAP_PASSES_K_SQUARE_CYCLE_TEST = false | TYPE-R
CTP_CLOSURE_ALONE_SUPPLIES_ORIENTATION_SIGNS = false | TYPE-R |
  test: branch-relative product has coefficient n 1_N

S_SQUARE_IS_DERIVED = false | TYPE-U |
  would-build: branch-to-path and cell-to-edge provenance plus naturality

FULL_CTP_TO_CYCLE_DYNAMICS_INTERTWINER_BUILT = false | TYPE-U |
  would-build: the five-item tuple in Section 3.1
```

### 3.3 Verdict on the proposed identification

The statement “the doubled contour closes, therefore `Z_N` is `Phi_c`” is
refuted. The antecedent describes CTP closure; the consequent requires
incidence closure. A map may be built between the resulting objects, but it
cannot be omitted.

```text
BRIDGE_Z_TO_PHI = REFUTED_AS_DEFINITIONAL_IDENTITY | TYPE-R
BRIDGE_Z_TO_PHI_EXISTS_AS_DERIVED_DYNAMICS_MAP = NO_VERDICT |
  prerequisite: CTP_RELATIVE_HISTORY_TO_INCIDENCE_CYCLE_DYNAMICS_INTERTWINER
```

## 4. Bridge 2: bilocal-probe action on the source kernel

### 4.1 Exact finite zero map

At finite `N`, Q-279 gives

```text
Z_ref,N[J,R]=(1-p)+p exp(Xi_N[J,R]),
Xi_N[J,R]=L_N(J)-Q_N(R)/2,

D^2W_N[h_1,h_2]
 =-i hbar omega(1-omega) lambda_N(h_1)lambda_N(h_2),

lambda_N(j,r)=L_N(j)-Q_N(r)/2.
```

Let `K_N=ker L_N`. For `k in K_N` and any bilocal direction `r`,

```text
lambda_N(k,0)=0,

beta_N(k,r)
 :=D^2W_N[(k,0),(0,r)]
 =0.                                                     (BR-1)
```

The same argument gives all blocks with a `K_N` leg:

```text
D_K W_N=0,
D^2_(K,K)W_N=0,
D^2_(K,J/K)W_N=0,
D^2_(K,R)W_N=0.                                        (BR-2)
```

The coefficient `omega(1-omega)`, including all of its symbolic `p` content,
is multiplied only after the zero kernel factor appears. Thus the zero is
structural and probes-on exact.

```text
FINITE_CYCLE_SOURCE_TO_R_ACTION = ZERO_MAP | TYPE-P
FINITE_K_R_MIXING = zero | TYPE-P
P_DEPENDENCE_IN_FINITE_K_R_MIXING = false | TYPE-R |
  test: lambda_N(k,0)=0 before omega(1-omega) acts
```

### 4.2 Completed source lift

P2 makes `L` continuous. Therefore `K=ker L` is closed in the inherited P2
norm. Q-309's finite-core correction

```text
k_m=x_m-[L(x_m)/L(e)]e
```

gives a dense finite kernel core. The source Hessian is continuous in P2's
Frechet calculus. For finite-core approximants `k_m->k`,

```text
beta(k,r)=lim_m beta_m(k_m,r)=0.                       (BR-3)
```

This uses the P2 norm throughout. It invokes no weak-star, bidual, projective,
or unnamed completion.

```text
COMPLETED_SOURCE_KERNEL_K_EXISTS = true | TYPE-P
FINITE_KERNEL_CORE_DENSE_IN_K = true | TYPE-P
COMPLETED_K_R_ACTION = ZERO_MAP | TYPE-P
K_R_ZERO_LIFT_TOPOLOGY = inherited_P2_norm
K_R_ZERO_LIFT_CREATED_TAIL = false | TYPE-R |
  test: continuous extension inside the existing norm class
```

### 4.3 What the zero map does not provide

`beta=0` is the complete action of the current scalar source germ on
`K x R`. It does not identify `R` with `Phi_c`, and it does not descend the
untraced law into `Gamma_2PI`. Its image contains no dynamics-bearing cycle
datum.

```text
ZERO_BETA_IDENTIFIES_R_WITH_CYCLE_PHASE = false | TYPE-R |
  test: zero bilinear derivative versus distinct source and phase carriers

COMPLETED_SOURCE_ZERO_IS_PHYSICAL_2PI_ZERO = false | TYPE-U |
  would-build: a continuous source-kernel-to-2PI-tangent intertwiner and
               restriction square
```

## 5. The 2PI descent attempt

### 5.1 The required target

The raw correlator-to-RetHess specification requires
(`STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:708-819`):

```text
delta Gamma_2PI/delta G |_(G_*,R=0)=0,

D^2 Gamma_1PI
 =Gamma_AA-Gamma_AG Gamma_GG^(-1) Gamma_GA,

H_C[G]=i hbar I_C[G],
H_R=(T_CTP^T H_C T_CTP)_(delta,c).
```

All blocks must share one completed physical domain, quotient, measure,
contour, boundary/contact convention, and stationary background.

### 5.2 Factor-through-quotient theorem for the available source germ

The current scalar germ has the exact form

```text
W[J,R]=W_tilde(L(J),Q(R)).
```

Hence it factors through

```text
(J,R) -> (J/ker L,Q(R)).
```

Its derivative in a kernel direction is zero at every source point, and its
Legendre image in the linear-source variable is contained in `span{L}`. The
record-visible cycle subspace is absent from this scalar image.

Therefore a construction using only this scalar germ has two possibilities:

1. retain the physical cycle carrier, in which case the Legendre/source map is
   singular on that carrier; or
2. quotient `ker L`, in which case it deletes the surviving cycle witness.

Q-308 refutes option 2 as a physical inverse because `u_square` is nonzero,
record-visible, and lies in `ker L`.

```text
SCALAR_GERM_FACTORS_THROUGH_J_MOD_K = true | TYPE-P
SCALAR_GERM_SUPPLIES_CYCLE_DYNAMICS = false | TYPE-R |
  test: exact invariance under J -> J+k for every k in K

QUOTIENTING_K_IS_A_PHYSICAL_2PI_DESCENT = false | TYPE-R |
  test: deletes the record-visible u_square witness
```

This theorem does not exclude additional dynamics in the untraced transition.
It says that such dynamics is not present in the scalar object currently
being differentiated.

### 5.3 Why density cannot cross the carrier gap

Density proves uniqueness of a continuous extension after domain, codomain,
map, and topology are fixed. Here only the source-domain side is fixed. The
following data are absent:

```text
rho_cycle,2PI : K -> T_(Abar,G)Gamma_2PI,
Gamma_AA, Gamma_AG, Gamma_GG, Gamma_GA,
G_*, Gamma_GG^(-1), common physical domain,
physical restriction square.
```

The equation `beta=0` cannot define `rho_cycle,2PI`; doing so would be the
tautological pullback prohibited by the realization-functor precedent. Nor can
continuity certify a target topology that has not been instantiated.

```text
SOURCE_KERNEL_TO_2PI_TANGENT_MAP_BUILT = false | TYPE-U |
  would-build: rho_cycle,2PI with common-origin and restriction certificates

STATIONARY_2PI_BLOCK_SYSTEM_BUILT = false | TYPE-U |
  would-build: the four blocks, stationary fiber, inverse, and common domain

PHYSICAL_2PI_MIXING_ZERO_PROVED = false | TYPE-U |
  would-build: the map, then lift BR-1 through its proved continuity

PHYSICAL_2PI_MIXING_NONZERO_PROVED = false | TYPE-S |
  roots: no physical 2PI block exists to witness a nonzero term |
  exclusions: source quotient/R blocks |
  fences: no name transport |
  query: instantiated Gamma_KQ/Gamma_KG term
```

### 5.4 2PI verdict

```text
TWO_PI_DESCENT_EXECUTED = false | TYPE-C |
  constraints: Bridge 1 and rho_cycle,2PI absent; stationary block system absent

FINITE_MIXING_ZEROS_LIFT_TO_PHYSICAL_2PI = NO_VERDICT |
  prerequisite: source-kernel-to-2PI-tangent intertwiner in a named topology

PHYSICAL_RESPONSE_LIVES_ONLY_ON_CYCLE_CONTENT = NO_VERDICT |
  prerequisite: completed RetHess image/support theorem
```

The correct current statement remains support separation in the scalar source
germ. It is not physical cancellation.

## 6. Restriction checks

### 6.1 Executed finite/source checks

| Check | Result | Standing |
|---|---|---|
| `K_square` all-unit character boundary | nonzero | **REFUTES identity / TYPE-R** |
| `K_square` `c_square` boundary | zero | **PASS / TYPE-P** |
| Q-243 `R=0` kernel blocks | all zero | **PASS / TYPE-P** |
| Q-279 probes-on `K x K`, `K x J/K`, `K x R` | all zero | **PASS / TYPE-P** |
| sequential zero-extension of `L`, `Q`, and beta | commutes | **PASS / TYPE-P** |
| finite kernel core to completed source kernel | norm-dense | **PASS / TYPE-P** |
| completed source beta | zero by norm continuity | **PASS / TYPE-P** |

### 6.2 Unexecutable physical checks

```text
PHYSICAL_CYCLE_DYNAMICS_RESTRICTION_SQUARE_EXECUTED = false | TYPE-C |
  constraints: no CTP-to-cycle dynamics intertwiner

PHYSICAL_2PI_RESTRICTION_SQUARE_EXECUTED = false | TYPE-C |
  constraints: no stationary 2PI block system

PHYSICAL_RETHESS_RESTRICTION_TO_FINITE_ZERO = NO_VERDICT |
  prerequisite: completed RetHess and restriction map
```

The DoR-008 finite discipline is satisfied wherever an object exists. It does
not manufacture a missing physical object from its finite shadows.

## 7. Six-account table

| Account | Kernel/applicability | Image | Sector transfer | Restriction square | Tail action | Verdict |
|---|---|---|---|---|---|---|
| measure | finite trace and scalar source functional only | scalar finite/source values | none from `K` | Q-243/Q-279 pass | none created | completed physical measure **TYPE-U** |
| contour | ratified finite CTP branch-relative character | all-unit relative-history character | branch pair -> relative cell coordinate | finite pass | none created | incidence-cycle transport **TYPE-U** |
| boundary/contact | finite incidence boundary separately available | `c_square` cycle line | none into `R` or 2PI | boundary test executed | none created | physical contact/gluing **TYPE-U** |
| domain closure | `K=ker L` closed; finite core dense | completed source kernel | beta remains zero | norm square passes | zero | source **PASS / TYPE-P**; physical operator domain **TYPE-U** |
| stationary Schur | four blocks and `G_*` absent | none | `NO_VERDICT` | unexecutable | `NO_VERDICT` | **TYPE-U / TYPE-C check** |
| class formation | P2 closed-subspace operation only | norm-class `K`; no new class | none | finite restrictions separate source class | zero created tail | source **PASS / TYPE-P**; physical 2PI class **TYPE-U** |

Every completed operation names the inherited P2 norm. There is no weak-star,
bidual, distributional, or projective class formation in this determination.

## 8. Door flags and kill passes

### 8.1 Door flags

```text
DOOR_D_PHYSICAL_IMAGE_EXECUTED_HERE = false | TYPE-C |
  constraint: this relay stops before raw-G inversion/RetHess construction

DOOR_F_PROJECTIVE_LIMIT_INVOKED = false | TYPE-S |
  roots: finite stages plus P2 norm completion only |
  exclusions: T_cyl projective alternatives |
  query: projective limit operation in this construction

WEAK_STAR_OR_BIDUAL_CREATOR_INVOKED = false | TYPE-S |
  roots: every completed arrow in Sections 4-7 |
  exclusions: unbuilt physical response class |
  query: weak-star, bidual, distributional completion

UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S |
  roots: closed kernel and continuous beta extension |
  exclusions: classes merely named as TYPE-U |
  query: every completion and closure arrow

DOR008_FINITE_FALSIFIER_FIRED = false | TYPE-R |
  test: every executable finite restriction agrees; no disagreement found
```

### 8.2 Kill passes

1. The common word “loop” does not identify CTP branch closure with incidence
   closure.
2. `Phi_c` is not transported into the separate composition-loop phase against
   V005's explicit scope clause.
3. `R` is not relabeled as a cycle current.
4. The zero derivative map is not reported as dynamics.
5. The source Hessian is not relabeled as `Gamma_2PI`.
6. Density is used only after domain, codomain, map, and topology are fixed.
7. The 1,088-member realization family is not reduced by selecting the desired
   orientation map.
8. `ker L` is retained; the record-visible square witness is not deleted.
9. No background, measure, contour, contact form, operator domain, inverse, or
   anchor member is selected.
10. No class-formation door is crossed silently.

## 9. Exact remaining object

The Q-309 package decomposes into two ordered maps. The first is the failed
bridge and is the immediate floor:

```text
CTP_RELATIVE_HISTORY_TO_INCIDENCE_CYCLE_DYNAMICS_INTERTWINER := (
  instantiated sequential-cell-to-oriented-edge realization;
  forward/backward-branch-to-oriented-path assignment;
  character-lattice map S_N with S_N(n 1_N) in ker(B_K^T);
  naturality under N<=M and admitted finite-complex refinement;
  intertwining of the full untraced U_N law, not only Z_law,N;
  state/effect trace or operator-valued continuation retaining cycle matrix
    elements;
  compatibility with Gate-4 quotient, U1/CTP reality, and Phi_c charts;
  common-origin provenance independent of p or any downstream verdict
).
```

After that map exists, the second required object is

```text
UNTRACED_LAW_TO_STATIONARY_2PI_CYCLE_DESCENT := (
  cycle-kernel tangent realization in (Abar,G) variables;
  Gamma_AA, Gamma_AG, Gamma_GG, Gamma_GA;
  stationary G_* and source-free surface;
  GG inverse/prescription on one common completed domain;
  measure, contour, boundary/contact, and operator-domain certificates;
  restriction squares and Tail_R action;
  proof whether BR-1 lifts through the instantiated map
).
```

The first tuple cannot be replaced by the coefficient equation
`S_square 1_4=c_square`: that equation fixes one visible target after it is
known and supplies none of the dynamics or provenance fields.

```text
NEXT_REQUIRED_OBJECT =
  CTP_RELATIVE_HISTORY_TO_INCIDENCE_CYCLE_DYNAMICS_INTERTWINER

NEXT_REQUIRED_OBJECT_BUILT = false | TYPE-U |
  would-build: the complete first tuple above

SUBSEQUENT_2PI_DESCENT_BUILT = false | TYPE-U |
  would-build: the complete second tuple above

NEW_AUTHORED_PHYSICS_PROVED_NECESSARY = NO_VERDICT |
  prerequisite: attempt the first tuple from the full untraced ratified law
                across the complete realization family
```

## 10. Physical p-verdict

| Stage | p content | Standing |
|---|---|---|
| `Z_law,N` relative-history character | no state weight; operator-valued law character | **TYPE-P** |
| scalar source germ on `K_N` | constant | **TYPE-P** |
| finite `K x K`, `K x J/K`, `K x R` blocks | zero before p coefficient acts | **TYPE-P** |
| completed source `K x R` action | zero by P2 norm continuity | **TYPE-P** |
| CTP-to-incidence dynamics bridge | unbuilt after definitional identity refuted | **TYPE-U** |
| physical cycle-kernel 2PI blocks | unbuilt | **TYPE-U** |
| physical RetHess on cycle content | unbuilt | **TYPE-C check** |
| evaluated physical response | background/domain absent | **NO_VERDICT** |

The derived mechanism is exactly:

```text
CURRENT_SOURCE_SUPPORT_SEPARATION = true | TYPE-P |
  reason: all p-bearing source Hessian factors through L and Q, while K=ker L

PHYSICAL_CANCELLATION_MECHANISM_ESTABLISHED = false | TYPE-U |
  would-build: both ordered maps in Section 9 and the lifted zero theorem

P_SURVIVES_IN_PHYSICAL_CYCLE_RESPONSE = NO_VERDICT
P_CANCELS_FROM_PHYSICAL_CYCLE_RESPONSE = NO_VERDICT
```

Calling the present result cancellation would conflate a zero map in the
available scalar source germ with a derived physical response on the
record-visible cycle sector. Calling `p` physical would make the opposite
unsupported transport. Both are refused.

## 11. Final typed ledger

```text
NUMBER_OF_TYPED_OBJECTS_IN_RELAY_PREMISE = 4 | TYPE-P
THREE_CYCLE_CARRIER_DESCRIPTION_IS_CORRECT = false | TYPE-R

CTP_CLOSURE_IDENTIFIES_Z_LAW_WITH_PHI_C = false | TYPE-R
Z_LAW_ALL_UNIT_CHARACTER_IS_K_SQUARE_CYCLE = false | TYPE-R
V005_PHI_C_IS_THE_SEPARATE_COMPOSITION_LOOP_PHASE = false | TYPE-R
R_IS_A_CYCLE_CARRIER = false | TYPE-R

SEALED_CTP_TO_INCIDENCE_CYCLE_INTERTWINER_FOUND = false | TYPE-S
SEALED_CYCLE_TO_BILOCAL_R_DYNAMICS_MAP_FOUND = false | TYPE-S
FULL_CTP_TO_CYCLE_DYNAMICS_INTERTWINER_BUILT = false | TYPE-U

FINITE_CYCLE_SOURCE_TO_R_ACTION = ZERO_MAP | TYPE-P
COMPLETED_K_R_ACTION = ZERO_MAP | TYPE-P
P_DEPENDENCE_IN_COMPLETED_K_R_ACTION = false | TYPE-R

SCALAR_GERM_SUPPLIES_CYCLE_DYNAMICS = false | TYPE-R
SOURCE_KERNEL_TO_2PI_TANGENT_MAP_BUILT = false | TYPE-U
STATIONARY_2PI_BLOCK_SYSTEM_BUILT = false | TYPE-U
PHYSICAL_2PI_MIXING_ZERO_PROVED = false | TYPE-U
TWO_PI_DESCENT_EXECUTED = false | TYPE-C

CURRENT_SOURCE_SUPPORT_SEPARATION = true | TYPE-P
PHYSICAL_CANCELLATION_MECHANISM_ESTABLISHED = false | TYPE-U
P_SURVIVES_IN_PHYSICAL_CYCLE_RESPONSE = NO_VERDICT
P_CANCELS_FROM_PHYSICAL_CYCLE_RESPONSE = NO_VERDICT

SELECTED_REALIZATION_MEMBER_FOUND = false | TYPE-S |
  roots: 1,088 support family and all displays here |
  exclusions: illustrative S_square is not installed |
  fences: no-selection |
  query: selected filtration, branch-path assignment, cycle basis

UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S
FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-R |
  test: all permitted structural calculations were executed

REGISTER_HEAD_AT_ISSUE = Q-309
REGISTER_HASH_OBSERVED_BEFORE_FINAL_FREEZE =
  40a4c54f3241499cf7081661d2c28d4b98fdedc904eabda36beecadc1bf775e5
REGISTER_HEAD_AT_CONSTRUCTION_FREEZE = Q-309
REGISTER_SHA256_AT_CONSTRUCTION_FREEZE =
  4306122d33a9db3dbba77c8cda3751d9b2b75ab2b1adade3898525344730200d
REGISTER_HEAD_AT_SEND_TIME = Q-309
REGISTER_SHA256_AT_SEND_TIME =
  4306122d33a9db3dbba77c8cda3751d9b2b75ab2b1adade3898525344730200d

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

The task's proposed shortcut was self-imposed: it asked one closure word to
perform an unbuilt carrier map. Once the closures are typed separately, the
finite theorem remains strong but honest: the source-kernel/probe action is
zero and p-free, while the physical cycle response still awaits the first
dynamics-bearing intertwiner.
