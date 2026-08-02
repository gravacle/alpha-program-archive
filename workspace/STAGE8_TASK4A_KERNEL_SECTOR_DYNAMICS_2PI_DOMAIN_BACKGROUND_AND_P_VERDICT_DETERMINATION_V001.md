# Stage 8 Task 4a Kernel-Sector Dynamics, 2PI, Domain, Background, and p-Verdict Determination V001

Date: 2026-08-02  
Task: PASTE 391 / Task 4a  
Lane: CODEX LANE 2  
Status: **SHARP STOP — THE CURRENT RESPONSE FUNCTIONAL IS EXACTLY CONSTANT ON `ker L`; NO PHYSICAL KERNEL-SECTOR DYNAMICS OR 2PI DESCENT INSTANCE IS BUILT; p-VERDICT REMAINS `NO_VERDICT`**

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013,
                   DoR-014 as amended (2 + N), DoR-015

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead determination

The relay's proposed kernel dynamics is not present in the ratified response
functional. The carrier comparison fails before the 2PI construction.

There are two different phase objects:

```text
Z_law,N[a_+,a_-]
  =product_(j=1)^N conjugate(z_(-,j))z_(+,j),

Phi_c([A])
  =-i Log_0 product_(e in E_N)
      (h_e(A)h_e(A_0)^(-1))^(c_e),
  c in ker(B_N^T).
```

The first is the ratified sequential relative-CTP-history character. The
second is V005's Gate-4 composition-cycle phase on the incidence quotient.
No sealed map identifies their cell index `j` with the incidence edge `e`,
their all-unit exponent with a cycle coefficient `c`, or their carriers.

Q-279 makes a second distinction explicit: its dephasing expression

```text
1-p+p exp[-Q_N(R)/2]
```

comes from the **independent symmetric bilocal probe** `R`. It is not a
cycle-current response unless a cycle-to-`R` map is built. No sealed such map
was found.

On the response chain that actually exists, let

```text
K_N:=ker L_N,
Z_ref,N[J,R]
  =(1-p)+p exp(L_N(J)-Q_N(R)/2),
W_N=-i hbar Log_0 Z_ref,N.
```

For every `k in K_N`, every source point `(J,R)`, and every parameter `t`,

```text
Z_ref,N[J+t k,R]=Z_ref,N[J,R].                       (KR-1)
```

Therefore every derivative with a `K_N` leg is exactly zero:

```text
D_K W_N=0,
D^2_(K,K)W_N=0,
D^2_(K,J/K)W_N=0,
D^2_(K,R)W_N=0.                                     (KR-2)
```

For the square witness, `L_N(c_square)=0` and the independently coded exact
check returns `Z_ref,N[t c_square,0]=1`, first derivative zero, and second
derivative zero. The probes-on mixed derivative with `R` is also zero.

This is a stronger finite result than the relay anticipated: the current
scalar response germ has **no** kernel block and **no** kernel mixing block.
The `p`-dependent coefficient lives only on the quotient/`R` block. But this
is not the physical cancellation verdict. A zero connected Hessian on the
physical response sector is not an invertible retarded response; it is an
absent kernel-sector dynamics.

The untraced transition law retains individual-cell operators, but no sealed
common-origin descent carries its off-ready matrix elements into the V005
cycle-current bilocal or into `Gamma_2PI`. Consequently the stationary 2PI
blocks, physical operator domains, and stationary background remain unbuilt.

```text
CURRENT_SCALAR_GERM_NONTRIVIAL_ON_KER_L = false | TYPE-R |
  test: exact factorization (KR-1)

FINITE_KERNEL_BLOCK = zero | TYPE-P
FINITE_KERNEL_COMPLEMENT_MIXING = zero | TYPE-P
FINITE_KERNEL_R_MIXING = zero | TYPE-P

PHYSICAL_KERNEL_SECTOR_RESPONSE_BUILT = false | TYPE-U |
  would-build: the cycle-to-response and 2PI descent package in Section 10

P_APPEARS_IN_PHYSICAL_KERNEL_RETHESS = NO_VERDICT
P_CANCELS_FROM_PHYSICAL_KERNEL_RETHESS = NO_VERDICT
```

## 1. Preflight, currency, roots, and authorities

### 1.1 Corrected preflight

```text
DOES_THE_OBJECT_EXIST = SPLIT |
  completed source kernel and exact finite kernel block: yes |
  physical kernel dynamics, 2PI blocks, domains, background: no

IS_THE_VERSION_CURRENT = true |
  register: Q-308 at construction start

ARE_INPUTS_PRESENT = false | TYPE-R |
  test: no cycle-kernel-to-untraced-dynamics/R/2PI map; Q-288 leaves every
        stationary block uninstantiated; P3 and Q-281 leave domains/background
        unbuilt
```

The relay's statement that the inputs are present is refuted at the exact
cycle-to-response link. This does not refute a future physical kernel action.

### 1.2 Roots entered

1. `/Users/bgm/MB Work/alpha_supervision/LOCKED_PROCESS.md`
2. `/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md`
3. `STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md`
4. `STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md`
5. `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md`
6. `STAGE8_COMPOSITION_LOOP_STRUCTURAL_PREDICTION_BUILD_V001.md`
7. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V007.md`
8. `STAGE8_TASK4A_PHYSICAL_INVERSE_SCHUR_COMPLETED_DOMAIN_AND_P_VERDICT_ATTEMPT_V001.md`
9. `/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_TASK4A_P5_MAXIMAL_TRANSPORT_CHAIN_AND_DEPENDENCE_ACCOUNTING_PACKAGE_V002.md`
10. `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md`
11. `STAGE8_TASK4A_P3_SECOND_ATTACK_LAW_SIDE_CONSTRUCTION_AND_NARROWED_STOP_V001.md`
12. `STAGE8_TASK4A_ANCHORED_ORIGIN_TO_PHYSICAL_BACKGROUND_MAP_IDENTIFICATION_DETERMINATION_V001.md`
13. `STAGE8_TASK4A_FINITE_HESSIAN_TO_DELTAPHI_TRANSPORT_MAP_CONSTRUCTION_AND_P_CH_TRACE_V001.md`

All unqualified paths are rooted at the current cleanroom.

### 1.3 Frozen authorities

| Authority | SHA-256 | Load-bearing use |
|---|---|---|
| Register through Q-308 | `51d0681c6a8245b6cb8867666b1cafa5725d2602af44c22d6b030c447915b560` | current standing and kernel-resolution commission |
| Ratified finite influence result | `2cd1ffcefd68ac03c6c09a4eca0dc9fe8d1adc8ac564cc0d050dfd41d79e6d0f` | exact `Z_law,N`, `F_N`, carriers, and trace ceiling |
| Q-279 probes-on finite reference | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | exact `J/R` germ and complete derivative table |
| Field signature V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | physical cycle currents and phase calculus |
| Composition-loop build | `5810377123b823e680891a3337855750ac8f362951dca048dad3a78a34c79d79` | `K_square`, `c_square`, and carrier scope |
| Source germ V007 | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | current scalar response germ |
| Q-308 kernel determination | `c09783785546a8d6273b2fd104f3aeea0751e83c337ee4e8ac7677d9df87f3d0` | physical kernel obstruction and diagnostic-only quotient |
| Q-288 six-account ledger V002 | `31a738ec17696ea01e1cb6a6ee7a37a29e6c0ca24d6fb8cc050d06aed32a583f` | stationary-Schur interfaces |
| Raw correlator-to-RetHess spec | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | physical inverse and 2PI requirements |
| P3 law-side stop | `8e9a09c104f4b6352263591037b2e0bb9a82b659aa1b6276cdd48117f872acec` | exact domain/measure/contour boundary |
| Q-281 background determination | `f893d210191551bd8b6af060f85a73510f8119171c8709c46e925a6708314ed2` | source seed versus physical stationary pair |

All hashes were recomputed before construction.

### 1.4 Exclusions

```text
a32_holdout/custodian_private/                  NOT ENTERED
Z_law,N identified with Phi_c                   NOT DONE
bilocal R identified with a cycle current       NOT DONE
untraced U_N promoted to Gamma_2PI              NOT DONE
complement, projector, background, or domain    NOT SELECTED
quotient reciprocal promoted to physical        NOT DONE
alpha, kappa, coupling, scale, or root           NOT COMPUTED
measured-constant comparison                    NOT PERFORMED
register, plan, tracker, git, commit, push       NOT TOUCHED
```

## 2. Bearing symbol and carrier distinctions

1. `Z_law,N` is the charged relative-history product in the ratified finite
   transition. `Z_ref,N` is the scalar state/source germ. Q-279 explicitly
   says they are different objects (`:150-168`).
2. The law index `j=1,...,N` labels sequential record cells. The V005 edge
   index labels a finite incidence complex. No sealed object map identifies
   them.
3. `L_n` is the accumulated linear-source covector. `L_N` in V005 is the
   connection-incidence line-integral map. They are not the same operator.
4. `R` is the independent symmetric bilocal probe. It is not the record
   vector and not a retarded block.
5. `c_square` is the composition-loop incidence coefficient. Its physical
   current realization is `u_square=u_(c_square)`.
6. `Gamma_GG` is a 2PI tangent block. It is not raw connected `G^007` and not
   the finite source Hessian `D^2W_N`.
7. Q-308's existing field/source lift places `u_square` in the linear-source
   carrier `J_phys` and proves it lies in `ker L`. The missing arrow starts
   after that placement: it must make the kernel dynamics-bearing in the
   untraced law, bilocal port, or 2PI system.

These distinctions are exactly where an apparent kernel resolution could be
manufactured by name transport.

## 3. Phase-carrier adjudication

### 3.1 What the ratified law supplies

The finite law defines (`STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md:12-50,117-165,167-213`):

```text
Z_law,N[a_+,a_-]
 =product_j conjugate(chi_n(h_j[a_-]))chi_n(h_j[a_+]),

F_N[a_+,a_-]=P_0+Z_law,N[a_+,a_-]P_ch.
```

`F_N` is an operator on the neutral/charged source span and a functional of
two sequential connection histories. The record sandwich leaves no scalar
physical amplitude until a state/effect is supplied.

### 3.2 What the physical cycle family supplies

V005 instead defines (`STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md:81-124,286-385`):

```text
u_c(a)=sum_e c_e integral_(gamma_e) a,
c in ker(B_N^T),
d Phi_c=u_c.
```

The composition-loop carrier is the unfilled four-edge graph with
`c_square=(1,-1,1,-1)` and a path-ratio phase
(`STAGE8_COMPOSITION_LOOP_STRUCTURAL_PREDICTION_BUILD_V001.md:132-181,186-225`).

The two products have different indices, exponent data, carrier definitions,
and provenance. A word-bounded case-insensitive intersection search found
only one file containing both `K_square` and `Z_N`; inspection shows them in
separate U3 inventory sections and supplies no identity. No file containing
`composition-loop` and `Z_N` supplies a cross-carrier map.

```text
Z_LAW_IS_V005_COMPOSITION_LOOP_FUNCTIONAL = false | TYPE-R |
  test: carrier/index/exponent comparison

SEALED_COMPOSITION_LOOP_TO_Z_LAW_MAP_FOUND = false | TYPE-S |
  roots: cleanroom Markdown excluding custodian_private |
  exclusions: inventory co-occurrence without an identity |
  fences: word-bounded, case-insensitive; no unproved transport |
  query: composition-loop/K_square intersect Z_N

UNTRACED_U_N_TO_CYCLE_2PI_DESCENT_BUILT = false | TYPE-U |
  would-build: a common-origin map from the full finite operator law, with
               state/effect matrix elements, to the V005 cycle response and
               physical 2PI blocks
```

### 3.3 The Q-279 dephasing factor does not fill the gap

Q-279 defines (`:150-239,262-290`):

```text
Xi_N[J,R]=L_N(J)-Q_N(R)/2,
Z_ref,N[J,R]=(1-p)+p exp(Xi_N[J,R]).
```

At equal connection histories it gives
`1-p+p exp[-Q_N(R)/2]`. But `Q_N(R)` is a same-cell
difference/difference trace of the independent bilocal source. Q-279 warns
that the mixed `J_delta/R` derivative is not the retarded
`(delta,c)` block (`:401-425`).

```text
Q279_DEPHASING_WEIGHT_IS_V005_CYCLE_RESPONSE = false | TYPE-R |
  test: independent R-port versus cycle-current carrier and role

CYCLE_CURRENT_TO_BILOCAL_R_MAP_FOUND = false | TYPE-S |
  roots: cleanroom Markdown excluding custodian_private |
  exclusions: generic source-field and finite incidence maps |
  fences: word-bounded, case-insensitive |
  query: u_c/c_square/Phi_c/ker(B^T) with R_delta/Q_N(R)/2PI

CYCLE_CURRENT_TO_BILOCAL_R_MAP_BUILT = false | TYPE-U |
  would-build: an explicit map preserving cycle phase, U1/CTP reality,
               restrictions, response, and common-origin provenance
```

## 4. Exact finite kernel theorem

### 4.1 Factorization through `L_N`

For a fixed finite stage, set

```text
K_N:=ker L_N,
lambda_N(j,r):=L_N(j)-Q_N(r)/2.
```

Q-279's exact derivative identity is

```text
D^2W_N[h_1,h_2]
 =-i hbar omega(1-omega)
    lambda_N(h_1)lambda_N(h_2).                      (KR-3)
```

If `k in K_N` is placed in a linear-source leg, then
`lambda_N(k,0)=0`. Hence (KR-2) follows directly, at every source point and
for every admitted bilocal probe.

### 4.2 Exact two-sector source block

Use the canonical short exact sequence, without choosing a complement:

```text
0 -> K_N -> J_N --L_N--> im(L_N) -> 0.              (KR-4)
```

For display only, any algebraic splitting `J_N=K_N direct-sum S_N` gives the
same block pattern:

```text
D^2W_N on (K_N,S_N,R_N) =

  [ 0       0       0      ]
  [ 0     H_SS    H_SR     ]
  [ 0     H_RS    H_RR     ].                       (KR-5)
```

The bottom-right block carries `omega(1-omega)` and Q-279's exact
`J_delta/J_delta`, `J_delta/R`, and `R/R` forms. The entire first row and
column vanish independently of the splitting. Thus no complement is selected
and no zero is assumed.

For `c_square=(1,-1,1,-1)`, the accumulated covector gives
`L_N(c_square)=0`. A separate symbolic checker evaluated

```text
Z(t)=1-p+p exp(i t L_N(c_square)),
W(t)=-i hbar Log Z(t)
```

and returned

```text
L_N(c_square)=0,
Z(t)=1,
D_t Z=0,
D_t^2 W=0.
```

With a symbolic bilocal probe factor present it separately returned
`D_tW=D_t^2W=D_tD_RW=0`. The symbolic calculation is a check; (KR-1) through
(KR-3) are authoritative.

```text
FINITE_K_N_IS_RADICAL_OF_CURRENT_SOURCE_HESSIAN = true | TYPE-P
FINITE_KK_BLOCK = zero | TYPE-P
FINITE_K_QUOTIENT_MIXING_BLOCK = zero | TYPE-P
FINITE_K_R_MIXING_BLOCK = zero | TYPE-P
P_DEPENDENCE_IN_FINITE_K_BLOCK = false | TYPE-R |
  test: block vanishes before omega(1-omega) acts
P_DEPENDENCE_IN_FINITE_QUOTIENT_R_BLOCK = true | TYPE-P |
  form: Q-279 omega(1-omega) family
```

### 4.3 What this does and does not say about the dynamics

The untraced tensor-product transition contains individual per-cell factors.
The ready-record sandwich collapses them to `Z_law,N`, and the state/source
scalarization collapses further to `Z_ref,N`. The current physical response
chain consumes the latter derivatives.

It is therefore lawful to say:

```text
CURRENT_SCALAR_RESPONSE_GERM_IS_SILENT_ON_K_N = true | TYPE-P
```

It is not lawful to conclude that every matrix element of the untraced law is
silent or that a future 2PI realization cannot expose one. That would require
the absent descent map in Section 3.

## 5. Completed source-kernel domain

P2 makes `L` continuous on the completed physical source class. Therefore

```text
K:=ker L
```

is a closed Banach subspace. It carries the inherited norm and creates no new
tail or completion.

The finite kernel core is dense. Choose one finite-core direction `e` with
`L(e)!=0`, which exists because the one-cell authority has nontrivial
`L_n,N(J)=i n sum_j J_delta,j`. For any `k in K`, take finite-core
approximants `x_m->k` and set

```text
k_m:=x_m-[L(x_m)/L(e)]e.
```

Then `k_m` is finite-core, lies in `K`, and converges to `k` by continuity.
Thus the kernel source domain and its restrictions are constructed exactly.

```text
COMPLETED_SOURCE_KERNEL_K_EXISTS = true | TYPE-P
FINITE_KERNEL_CORE_DENSE_IN_K = true | TYPE-P
KERNEL_FORMATION_TOPOLOGY = inherited_P2_norm
KERNEL_FORMATION_CREATED_TAIL = false | TYPE-R |
  test: closed subspace of the existing Banach source class
```

This is not the requested completed **physical operator** domain. It supplies
no history measure, contour boundary value, contact data, unbounded operator,
or common invariant core.

```text
COMPLETED_PHYSICAL_KERNEL_OPERATOR_DOMAIN_BUILT = false | TYPE-U |
  would-build: named physical kernel operator, completed measure/contour,
               boundary/contact form, invariant core, and closure certificate
```

## 6. Stationary 2PI block attempt

The source Hessian (KR-5) is not the stationary 2PI block system. The raw-map
specification requires

```text
D^2 Gamma_1PI
 =Gamma_AA-Gamma_AG Gamma_GG^(-1) Gamma_GA
```

at a source-free stationary `G_*`, with every block on one physical domain.
The Q-288 ledger states that `Gamma_AA`, `Gamma_AG`, `Gamma_GG`, `Gamma_GA`,
the stationary fiber, the `GG` inverse, its restriction square, and its tail
action are all uninstantiated (`Q-288 V002:426-499`).

The finite source zeros do not instantiate those blocks:

1. `D^2W_N` is a connected source Hessian, not `D^2Gamma_2PI`.
2. `K_N` is a source kernel, not an identified `G`-tangent subspace.
3. A zero finite mixing block cannot be transported through an absent
   source-to-2PI map.
4. Calling `Gamma_GG` the finite quotient block would be a new identity and
   would still leave its physical inverse/domain absent.

```text
FINITE_SOURCE_TWO_SECTOR_BLOCK_BUILT = true | TYPE-P
FINITE_SOURCE_BLOCK_EQUALS_STATIONARY_2PI_BLOCK_SYSTEM = false | TYPE-R |
  test: variables, derivatives, carriers, and stationary condition differ

STATIONARY_2PI_KERNEL_BLOCK_BUILT = false | TYPE-U |
  would-build: physical 2PI functional and cycle-kernel tangent realization
STATIONARY_2PI_MIXING_BLOCKS_BUILT = false | TYPE-U |
  would-build: Gamma_KQ/Gamma_QK and Gamma_KG/Gamma_GK on one domain
STATIONARY_GG_BLOCK_AND_INVERSE_BUILT = false | TYPE-U |
  would-build: Gamma_GG, stationary fiber, prescription, and inverse domain
STATIONARY_SCHUR_EXECUTION = BLOCKED | TYPE-C |
  constraints: physical 2PI blocks and stationary fiber absent
```

## 7. Domain and background attempt

The domain and background results are unchanged by taking `ker L`:

| Component | Present | Missing | Verdict |
|---|---|---|---|
| finite/source kernel | closed `K`, dense finite kernel core | none | **PASS / TYPE-P** |
| branch-joint measure | finite trace and cylinder amplitudes | marginally consistent physical history measure and `dmu_C` | **TYPE-U** |
| interacting contour | CTP order and `E_post` orientation | analytic family, insertion rule, boundary value, limit topology | **TYPE-U** |
| boundary/contact | finite glue and two separate exact limits | joint physical carrier, contact/boundary form, null/private removal | **TYPE-U** |
| unbounded domains | bounded source calculus and record-only GNS | named physical operators, invariant core, closed/self-adjoint realization | **TYPE-U** |
| source background | anchored state and exact derivative seed | physical `Abar_*`, `G_*`, Legendre map, stationary solve | **TYPE-U** |
| response tail | source kernel creates none | physical `Tail_R` domain and action | **TYPE-U / NO_VERDICT** |

The source background is flat along `K`:

```text
D_K W(0)=0,
D^2_(K,*)W(0)=0.
```

That is restricted source stationarity only. Q-281 proves that the anchored
state/seed is not the physical stationary pair and leaves `STAT_BG_LIFT_FIBER`
unbuilt (`Q-281:284-408,410-467`).

```text
K_RESTRICTED_SOURCE_GRADIENT_ZERO = true | TYPE-P
K_RESTRICTED_SOURCE_FLATNESS_IS_PHYSICAL_2PI_STATIONARITY = false | TYPE-R |
  test: source derivative versus physical 2PI stationary signature

PHYSICAL_BACKGROUND_REALIZATION_BUILT = false | TYPE-U |
  would-build: i_A, i_G, connected subtraction on the physical carrier,
               Legendre map, stationary solve, and common-origin certificate
```

## 8. Restriction and dependence certificates

### 8.1 Exact finite restrictions

For every finite stage and every admitted `R`, Q-279 proves the complete
source Hessian table and the zero ordered retarded block. Restricting that
table to `K_N` gives (KR-5). W3 naturality maps finite kernels into later
kernels because `L_M iota_NM=L_N`.

```text
FINITE_KERNEL_RESTRICTION_TO_Q243 = PASS | TYPE-P
FINITE_KERNEL_RESTRICTION_TO_Q279 = PASS | TYPE-P
KERNEL_ZERO_EXTENSION_SQUARE = PASS | TYPE-P
COMPLETED_SOURCE_KERNEL_ZERO_BY_CONTINUITY = PASS | TYPE-P
```

### 8.2 What does not restrict yet

No physical kernel response, 2PI Schur block, physical domain, or background
exists. Their restriction squares cannot be executed.

```text
PHYSICAL_KERNEL_RESPONSE_RESTRICTION_SQUARE = false | TYPE-C |
  constraints: no physical kernel response operator
PHYSICAL_2PI_RESTRICTION_SQUARE = false | TYPE-C |
  constraints: no stationary 2PI block system
PHYSICAL_RETHESS_RESTRICTS_TO_KERNEL_FINITE_ZERO = NO_VERDICT
```

## 9. Six-account operation table

| Operation | Kernel/applicability | Image | Sector transfer | Restriction square | Tail action | Verdict |
|---|---|---|---|---|---|---|
| form `K=ker L` | kernel of continuous `L` | closed source subspace | none | finite kernels commute | no created tail | **PASS / TYPE-P** |
| restrict `Z_ref,W` to `K` | all `K` directions are invariances | constant scalar / zero derivatives | none | Q-243/Q-279 **PASS** | zero | **PASS / TYPE-P** |
| source Hessian on `K -> J/K -> R` | `K` is the radical | quotient/`R` block only | no transfer from `K` | finite and completed-source **PASS** | source tail zero | **PASS / TYPE-P** |
| cycle-to-response/2PI descent | no carrier map | none | `NO_VERDICT` | cannot execute | physical tail absent | **TYPE-U** |
| stationary 2PI/Schur | blocks and stationary fiber absent | none | `NO_VERDICT` | cannot execute | `NO_VERDICT` | **TYPE-U / TYPE-C check** |
| physical RetHess/background evaluation | no contour Hessian/domain/background | finite zero only | `NO_VERDICT` | cannot execute | `Tail_R` `NO_VERDICT` | **TYPE-C** |

No operation is omitted. In particular, the table does not treat the
one-dimensional quotient reciprocal as a kernel-sector response.

## 10. Exact remaining object

The narrowed next object is:

```text
CYCLE_KERNEL_RESPONSE_AND_2PI_DESCENT_PACKAGE := (
  retain the existing Q-308 placement K_N subset J_N, and for every finite
    stage construct its missing dynamics-bearing continuation into the full
    untraced history/operator data and/or bilocal/2PI carrier, preserving
    incidence, connection, CTP/U1 reality, W3 restrictions, and common-origin
    provenance;

  an executable state/effect trace or operator-to-functional descent from
    the full untraced U_N law that determines the response on K_N rather
    than merely its all-unit product character;

  a proof whether the resulting kernel functional is forced by DoR-009 or
    requires new authored dynamics, with no member selected by target;

  a splitting-independent physical K -> quotient block system, including
    every kernel, image, and mixing map;

  Gamma_AA/Gamma_AG/Gamma_GG/Gamma_GA on one common completed domain,
    stationary G_*, the GG inverse/prescription, and the Schur map;

  completed measure, contour, boundary/contact, operator domains, response
    class, restriction squares, and Tail_R action;

  the physical background realization or a theorem that the p verdict is
    uniform over its full admissible fiber
).
```

Its first map is the true new floor. Without it, the later 2PI/domain fields
have no kernel dynamics to complete.

```text
NEXT_REQUIRED_OBJECT = CYCLE_KERNEL_RESPONSE_AND_2PI_DESCENT_PACKAGE
NEXT_REQUIRED_OBJECT_BUILT = false | TYPE-U |
  would-build: the complete tuple above

NEW_AUTHORED_PHYSICS_PROVED_NECESSARY = NO_VERDICT |
  prerequisite: first attempt derivation from the full untraced ratified law
                through a lawful state/effect and carrier descent
```

## 11. Physical p verdict

The symbolic dependence trace is now exact up to the missing descent:

| Stage | Kernel-sector p content | Standing |
|---|---|---|
| ratified scalar germ on `K_N` | none; functional is constant | **TYPE-P** |
| finite connected kernel Hessian | zero before any p coefficient acts | **TYPE-P** |
| finite kernel/complement mixing | zero | **TYPE-P** |
| finite quotient/`R` noise block | carries `omega(1-omega)` | **TYPE-P** |
| completed source kernel | zero by continuity | **TYPE-P** |
| physical kernel dynamics | not built | **TYPE-U** |
| stationary 2PI kernel/mixing blocks | not built | **TYPE-U** |
| physical `RetHess` on kernel | not built | **TYPE-C check** |
| evaluated physical response | background absent | **NO_VERDICT** |

The finite mechanism is **support separation**, not an evaluated
cancellation: the current p-bearing scalar Hessian factors through `L` and
has no support on `ker L`. Calling this the physical answer would confuse
“no kernel dynamics has been supplied” with “a completed kernel response was
derived and p canceled from it.”

```text
P_IS_ABSENT_FROM_CURRENT_FINITE_KERNEL_BLOCK = true | TYPE-P
P_IS_CONFINED_TO_CURRENT_FINITE_QUOTIENT_R_BLOCK = true | TYPE-P

P_APPEARS_IN_PHYSICAL_KERNEL_RETHESS = NO_VERDICT
P_CANCELS_FROM_PHYSICAL_KERNEL_RETHESS = NO_VERDICT
PHYSICAL_RESPONSE_FREE_PARAMETER_LIST = NO_VERDICT
```

## 12. Kill passes and final typed ledger

### 12.1 Kill passes

1. No `Z_law,N=Phi_c` identity is asserted.
2. No independent bilocal `R` probe is relabeled as a cycle current.
3. No zero finite source block is promoted to a nonzero physical response.
4. No source Hessian is relabeled as a stationary 2PI block.
5. No complement, inverse, background, contour, domain, or anchor member is
   selected.
6. The record-visible kernel is retained; the quotient reciprocal remains
   diagnostic only.
7. Every completed operation names the inherited P2 norm; no unflagged
   class formation or tail creator is used.

### 12.2 Final ledger

```text
COMPLETED_SOURCE_KERNEL_K_EXISTS = true | TYPE-P
FINITE_KERNEL_CORE_DENSE_IN_K = true | TYPE-P

CURRENT_SCALAR_GERM_NONTRIVIAL_ON_KER_L = false | TYPE-R
FINITE_KERNEL_BLOCK = zero | TYPE-P
FINITE_KERNEL_COMPLEMENT_MIXING = zero | TYPE-P
FINITE_KERNEL_R_MIXING = zero | TYPE-P

Z_LAW_IS_V005_COMPOSITION_LOOP_FUNCTIONAL = false | TYPE-R
Q279_DEPHASING_WEIGHT_IS_V005_CYCLE_RESPONSE = false | TYPE-R
SEALED_CYCLE_TO_RESPONSE_MAP_FOUND = false | TYPE-S
CYCLE_KERNEL_RESPONSE_AND_2PI_DESCENT_PACKAGE_BUILT = false | TYPE-U

STATIONARY_2PI_BLOCK_SYSTEM_BUILT = false | TYPE-U
COMPLETED_PHYSICAL_OPERATOR_DOMAIN_BUILT = false | TYPE-U
PHYSICAL_BACKGROUND_REALIZATION_BUILT = false | TYPE-U
PHYSICAL_RETHESS_EXISTS = false | TYPE-C

P_IS_ABSENT_FROM_CURRENT_FINITE_KERNEL_BLOCK = true | TYPE-P
P_APPEARS_IN_PHYSICAL_KERNEL_RETHESS = NO_VERDICT
P_CANCELS_FROM_PHYSICAL_KERNEL_RETHESS = NO_VERDICT

SELECTED_MEMBER_FOUND = false | TYPE-S |
  roots: complete cycle family, source kernel, and exact sequence |
  exclusions: no complement or cycle basis selected |
  fences: family discipline |
  query: selected cycle, splitting, projector, background, domain

UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S |
  roots: P2 Banach source class and closed kernel only |
  exclusions: physical operator/2PI/RetHess classes unformed |
  fences: every limit names topology |
  query: weak-star, bidual, graph, resolvent, distributional completion

REGISTER_HEAD_AT_START = Q-308 |
  register_sha256=51d0681c6a8245b6cb8867666b1cafa5725d2602af44c22d6b030c447915b560

REGISTER_HEAD_AT_SEND_TIME = Q-308 |
  register_sha256=51d0681c6a8245b6cb8867666b1cafa5725d2602af44c22d6b030c447915b560

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

The exact gate is no longer “invert the rank-one correlator.” It is to derive
or openly author how the ratified dynamics reaches the record-visible cycle
kernel at all. Until that carrier-and-dynamics descent exists, the physical
kernel response and its p dependence do not exist as adjudicable objects.
