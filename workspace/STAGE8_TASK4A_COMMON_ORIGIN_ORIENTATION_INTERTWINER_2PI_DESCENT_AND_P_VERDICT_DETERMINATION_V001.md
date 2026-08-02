# Stage 8 Task 4a Common-Origin Orientation Intertwiner, 2PI Descent, and p-Verdict Determination V001

Date: 2026-08-02  
Task: PASTE 393 / Task 4a  
Lane: CODEX LANE 2  
Status: **THE COMMON-ORIGIN SQUARE IS NOT INDUCED; GLOBAL ORIENTATION INTERTWINER UNBUILT; 2PI DESCENT BLOCKED; PHYSICAL p-VERDICT REMAINS `NO_VERDICT`**

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013,
                   DoR-014 as amended (2 + N), DoR-015

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead determination

The requested intertwiner is **not derived by the ratified common origin**.
The load-bearing premise of the relay fails at the level of the map signatures:

```text
d_ready(Omega_prim,N)=C|r>^(tensor N),

d_law(Omega_prim,N;a)
 =P_0 tensor I_(3^N)+P_ch tensor W_N^(n)[a].
```

`d_ready` generates a ready **ray**, not the global incidence-cycle carrier
`ker(B_N^T)`. `d_law` generates the untraced sequential transition law; the
relative-history character `Z_law,N` is obtained later from its doubled trace.
The local rooted signed-incidence primitive supplies the one-cell write matrix
`S_inc`; it does not supply a sequential-cell-to-oriented-edge realization of
`K_square`, a branch-to-path assignment, or a map into `ker(B_N^T)`.

DoR-013 ratifies three maps—`d_state`, `d_ready`, and `d_law`—and a common-input
certificate. It does **not** ratify a map between the images of `d_ready` and
`d_law`, nor a fourth map producing V005's physical cycle carrier. Common
origin is therefore not a substitute for an intertwiner.

The exact mathematical obstruction to the proposed inference is the
factorization criterion. Given maps

```text
f:Omega -> X,
g:Omega -> Y,
```

an induced map `T:im(f)->Y` satisfying `g=T o f` exists exactly when

```text
f(omega_1)=f(omega_2)  implies  g(omega_1)=g(omega_2).
```

Equivalently, in the linear case, `ker(f) subset ker(g)`. Sharing a domain does
not prove this condition. Here the putative global-cycle generation map `g`
is absent, so its fiber condition cannot even be posed from the ratified
origin. Installing `g` by reading the desired cycle backward would be the
anti-relabeling failure prohibited by the Q-242 lineage.

The Q-310 boundary computation remains decisive:

```text
partial_1( 1, 1, 1, 1)^T = (-2,0,0, 2)^T,
partial_1( 1,-1, 1,-1)^T = ( 0,0,0, 0)^T.
```

The origin's local sign and `E_post` determine the one-cell write direction,
but they do not determine the alternating global edge sign needed to turn the
CTP all-unit character into the square cycle. The candidate

```text
S_square=diag(1,-1,1,-1)
```

would pass this one coefficient test, but selecting it would add the missing
branch/path and cell/edge assignment. It is not installed.

Consequently the requested 2PI descent does not execute. The already proved
completed source zero

```text
beta(k,r)=0,  k in ker L,
```

remains valid and p-free in the P2 norm, but no lawful map transports it into
the incidence-cycle 2PI tangent system. A zero in one carrier cannot certify a
physical zero in an unbuilt target carrier.

```text
DOR013_GENERATES_READY_RAY = true | TYPE-P
DOR013_GENERATES_RATIFIED_FINITE_LAW = true | TYPE-P

D_READY_CODOMAIN_IS_GLOBAL_INCIDENCE_CYCLE_CARRIER = false | TYPE-R |
  test: V003:638-645 gives C|r>^(tensor N) and no orientation coordinate

DOR013_COMMON_INPUT_ALONE_INDUCES_INTER_IMAGE_MAP = false | TYPE-R |
  test: factorization criterion above; no fiber-compatibility clause is ratified

GLOBAL_CYCLE_GENERATION_MAP_IN_DOR013_FOUND = false | TYPE-S |
  roots: DoR-013, Gen_Omega V001-V003, V003 review |
  exclusions: local one-cell S_inc and ready-ray map |
  fences: word-bounded, case-insensitive, no identity transport |
  query: global cycle output, ker(B^T), branch-to-path, cell-to-edge

CTP_RELATIVE_HISTORY_TO_INCIDENCE_CYCLE_DYNAMICS_INTERTWINER_BUILT =
  false | TYPE-U |
  would-build: the factorization-and-orientation package in Section 9

TWO_PI_DESCENT_EXECUTED = false | TYPE-C |
  constraints: no lawful CTP-to-cycle dynamics intertwiner and no instantiated
               physical cycle 2PI block system

P_IS_ABSENT_FROM_COMPLETED_SOURCE_KERNEL_MIXING = true | TYPE-P
P_APPEARS_IN_PHYSICAL_CYCLE_RETHESS = NO_VERDICT
P_CANCELS_FROM_PHYSICAL_CYCLE_RETHESS = NO_VERDICT
```

This is an underdetermination result, not a physical no-go. A lawful
orientation-bearing intertwiner may exist after the missing global descent
data are supplied. Current ratified material does not derive it.

## 1. Preflight, currency, roots, and authorities

### 1.1 Preflight at construction basis

```text
DOES_THE_OBJECT_EXIST = false | TYPE-U |
  object: CTP_RELATIVE_HISTORY_TO_INCIDENCE_CYCLE_DYNAMICS_INTERTWINER |
  existing: local S_inc, ready ray, U_N, Z_law,N, V005 cycle carrier |
  missing: a lawful map between the relative-history and cycle carriers

IS_THE_VERSION_CURRENT = true |
  register head: Q-310 at construction basis

ARE_THE_INPUTS_PRESENT = false | TYPE-S |
  missing input: global incidence-cycle generation map from Omega_prim,
                 plus its fiber/factorization and orientation certificates
```

The relay's phrase “both carriers share one generator” is checked, not
assumed. DoR-013 proves common primitive provenance for the state, ready ray,
and law. It does not list the V005 global incidence-cycle carrier among its
outputs.

### 1.2 Roots entered

1. `/Users/bgm/MB Work/alpha_supervision/LOCKED_PROCESS.md`
2. `/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md`
3. `/Users/bgm/MB Work/alpha_supervision/DECISION_OF_RECORD_013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL_2026-08-02_V001.md`
4. `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V001.md`
5. `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V002.md`
6. `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md`
7. `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_V003_ADVERSARIAL_REVIEW_DETERMINATION_V001.md`
8. `STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md`
9. `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md`
10. `STAGE8_TASK4A_KERNEL_SECTOR_DYNAMICS_2PI_DOMAIN_BACKGROUND_AND_P_VERDICT_DETERMINATION_V001.md`
11. `STAGE8_TASK4A_CYCLE_KERNEL_RESPONSE_AND_2PI_DESCENT_BRIDGE_DETERMINATION_V001.md`
12. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V007.md`
13. `STAGE8_MINIMAL_OMEGA_P5_COMMON_ORIGIN_ROLE_REALIZATION_ATTEMPT_V001.md`

All unqualified paths are rooted at the current cleanroom. The archive mirror
was read only for custody comparison. `a32_holdout/custodian_private/` was not
entered.

### 1.3 Frozen authority hashes

| Authority | SHA-256 | Load-bearing use |
|---|---|---|
| Locked process | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | fences and custody |
| Register through Q-310, construction basis | `96ca828bb5cda01e53b12d3eb0689ed3a085491448c4f50779b56e9b300bc3b6` | current standing |
| DoR-013 | `f2a7838d41b7b7df42ae92bc3d59399ee04bbec65cecadc8a43f6a36ac4756ec` | exact ratified fields, maps, and falsifiers |
| Gen_Omega V003 | `1be5f6a7e40c34586f3b5ab78f9129de0b5d2041cb6695b0e549443ddd6c6ee0` | primitive tuple and map signatures |
| V003 adversarial review | `ae1f60b049f21073c7513f8133712d17b9abf4dfb8c46ccc6ea894fc2283c7eb` | ratification-readiness and scope |
| Q-310 determination | `a4a4f4e76c22a41caea00c434055099b6b9401626ac6ef523ab3741017b3e03e` | exact boundary falsifier and completed beta zero |
| Q-309 determination | `a4c916a7cfa82c2130c82d8947c869f118e224959d7824bba45695711b4919c3` | kernel-sector support separation |
| V005 field signature | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | physical quotient and cycle current family |
| Ratified finite influence result | `2cd1ffcefd68ac03c6c09a4eca0dc9fe8d1adc8ac564cc0d050dfd41d79e6d0f` | untraced law and relative-history character |
| Source germ V007 | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | current scalar source dependence |

### 1.4 Search and exclusions

```text
ROOTS = current cleanroom Markdown plus the supervision authorities above
EXCLUDED = a32_holdout/custodian_private; git metadata; binary/media;
           archive duplicates as independent authorities
WORD_BOUNDARY = case-insensitive where the corpus was swept

QUERY_1 = CTP near incidence / incidence near CTP
QUERY_2 = relative-history near cycle / cycle near relative-history
QUERY_3 = cell-to-edge / branch-to-path / descent-compatibility square
QUERY_4 = Omega_prim near global cycle / ker(B^T)
```

The only exact post-Q-309 occurrence of the requested bridge is Q-310's named
missing object and its illustrative uninstalled `S_square`. No later sealed or
ratified map was found at construction basis.

```text
POST_Q310_SUPERSEDING_INTERTWINER_FOUND = false | TYPE-S |
  roots: register through Q-310 and current cleanroom |
  exclusions: target relay text and Q-310's would-build |
  fences: exact signature required |
  query: QUERY_1 through QUERY_4
```

## 2. What the ratified origin actually generates

### 2.1 Primitive fields versus outputs

Gen_Omega V003 lists (`:607-623`):

```text
Omega_prim,N^v003 := (
  A0,
  P_0,P_ch,E_ch,Tr_A,I_src,
  P_src,anchor tag,Cert_anchor_IF,
  K_cell,iota_cell,plus_root,
  chi_n,E_post,
  tensor/zero-extension grammar,
  declared finite domains
).
```

The same passage expressly says that `rho_S`, the ready ray, `U_N[a]`,
`p_ch`, response, and target output are absent from the tuple. The three maps
then generate only:

| Map | Exact output | What it is not |
|---|---|---|
| `d_state` | the unique normalized fixed state of `P_src` | not a cycle carrier |
| `d_ready` | `C|r>^(tensor N)` | not `C_1(K_square)` and not `ker(B^T)` |
| `d_law` | `P_0 tensor I + P_ch tensor W_N[a]` | not `Phi_c` and not a 2PI block |

DoR-013 itself repeats exactly these three outputs at lines 14-16. Its P5
common-origin completion at line 19 certifies their provenance. It adds no
fourth output and no inter-image map.

```text
DOR013_RATIFIED_GENERATIVE_MAP_COUNT = 3 | TYPE-P
DOR013_RATIFIED_GLOBAL_CYCLE_MAP_COUNT = 0 | TYPE-S |
  scope: DoR-013 fields and V003 executable maps
```

### 2.2 What the signed-incidence primitive supplies

V001 supplies the definition inherited by V003 (`V001:188-209`):

```text
K_cell = one finite oriented cell with vertices v_0,v_1,v_perp,

S_inc|v_0>    = |v_1>,
S_inc|v_1>    = |v_0>,
S_inc|v_perp> =-|v_perp>,

iota_cell:C[K_cell] -> span{|r>,|p>,|e>}.
```

This is a **local one-cell realization** whose certificate is reproduction of
the one-cell write matrix `S`. V001 explicitly calls it weaker than the
terminal package. V003 retains it without adding a global filtration or
refinement object; its review confirms that the incidence primitive did not
become a filtration selection.

Thus the following orientation notions remain distinct:

```text
root/write orientation      v_0 -> v_1 in one record cell;
E_post time orientation     charge follows the write endpoint;
CTP branch orientation      forward versus backward source history;
incidence-edge orientation  signs in C_1(K) and boundary partial_1;
cycle orientation           coefficient c in ker(B^T).
```

The first two constrain the finite write. Neither is a declared map assigning
sequential cells and CTP branches to the four oriented edges of `K_square`.

```text
LOCAL_S_INC_REPRODUCES_ONE_CELL_WRITE = true | TYPE-P
LOCAL_S_INC_IS_GLOBAL_K_SQUARE_INCIDENCE_MAP = false | TYPE-R |
  test: V001 local codomain C[K_cell] versus V005 C_1(K_square)

E_POST_FIXES_WRITTEN_ENDPOINT_TIME_ORIENTATION = true | TYPE-P
E_POST_FIXES_ALTERNATING_K_SQUARE_EDGE_SIGNS = false | TYPE-U |
  would-build: a branch/path functor with an exact boundary certificate
```

### 2.3 The ready map is not the incidence-side carrier

The live V003 text is especially explicit (`:638-645`):

```text
d_ready(Omega_prim,N^v003):=C|r>^(tensor N).
There is no orientation coordinate and no exchanged member.
```

The “no orientation coordinate” statement removes the old root binary. It
does not encode a global cycle coordinate. Transporting the rooted ray into
`ker(B^T)` would need a new map with a different codomain.

```text
D_READY_IS_READY_RAY_MAP = true | TYPE-P
D_READY_IS_INCIDENCE_CYCLE_GENERATOR = false | TYPE-R
```

## 3. The factorization theorem: why common input is insufficient

### 3.1 Exact criterion

Let `f:Omega->X` and `g:Omega->Y`. A function

```text
T:im(f)->Y,  T(f(omega)):=g(omega)
```

is well defined if and only if `g` is constant on every fiber of `f`:

```text
for all omega_1,omega_2,
f(omega_1)=f(omega_2) => g(omega_1)=g(omega_2).       (F1)
```

Proof:

* Necessity: if `g=T o f`, equality of `f`-images gives equality of
  `T`-images.
* Sufficiency: define `T(x)=g(omega)` for any `omega` with `f(omega)=x`;
  (F1) makes the value independent of the representative.

For linear maps, (F1) is `ker(f) subset ker(g)`. This is the exact
anti-relabeling condition for an inter-image descent.

### 3.2 Application to DoR-013

For the requested square one would need, at minimum,

```text
f_rel:Omega_prim,N -> H_rel,N,
g_cyc:Omega_prim,N -> ker(B_K^T),
T_N:im(f_rel) -> im(g_cyc),
g_cyc=T_N o f_rel.
```

DoR-013 supplies neither displayed carrier map:

* `d_law` maps to the full operator `U_N[a]`; `Z_law,N` is a later trace
  character, so an explicit `f_rel` must name that trace and quotient.
* no `g_cyc` maps the primitive tuple to the V005 global cycle lattice.

CO1-CO4 certify output-free primitives, orbit collapse, executable generation
of the three named outputs, and no supplementation. None states (F1), a kernel
inclusion, or a commuting diagram between relative histories and cycles.

```text
COMMON_INPUT_CERTIFICATE_IMPLIES_FIBER_COMPATIBILITY = false | TYPE-R |
  test: factorization theorem and absence of (F1) from CO1-CO4

RELATIVE_HISTORY_OUTPUT_MAP_F_REL_INSTANTIATED_AT_ORIGIN_LEVEL = false | TYPE-U |
  would-build: typed doubled trace/character quotient from d_law

GLOBAL_CYCLE_OUTPUT_MAP_G_CYC_INSTANTIATED = false | TYPE-U |
  would-build: global finite-complex assembly and cycle extraction from Omega_prim

FIBER_COMPATIBILITY_CERTIFICATE_BUILT = false | TYPE-U |
  would-build: proof of (F1), or ker(f_rel) subset ker(g_cyc), family-wide
```

### 3.3 Q-242 blocks the shortcut

Q-242 rejected an earlier tuple because two outputs placed in one container
with projection maps were a relabeling, not a derivational origin. The same
standard applies one level later: two derived outputs from one primitive
tuple do not acquire a map between themselves merely because both arrows
start at `Omega_prim`.

Installing `T_N` by the rule “send the relative-history vector to the desired
cycle” would bundle the answer into the map. It would not be the origin's
descent.

```text
ORIGIN_MAP_CAN_BE_DEFINED_BY_DESIRED_TARGET = false | TYPE-R |
  test: Q-242 root-not-bag / anti-relabeling standard
```

## 4. Exact orientation test on `K_square`

### 4.1 The two closures

In the frozen edge order `(e_a0,e_0b,e_ab,e_ba)`, Q-310 uses

```text
partial_1 =
[[-1,-1, 0, 0],
 [ 1, 0,-1, 0],
 [ 0, 1, 0,-1],
 [ 0, 0, 1, 1]].
```

The relative-history character is `n 1_4`. The incidence-cycle generator is
`c_square=(1,-1,1,-1)`. Exact multiplication gives

```text
partial_1( 1, 1, 1, 1)^T = (-2,0,0, 2)^T,
partial_1(-1,-1,-1,-1)^T = ( 2,0,0,-2)^T,
partial_1( 1,-1, 1,-1)^T = ( 0,0,0, 0)^T.
```

Thus CTP closure and incidence closure remain different even though the
one-cell write is oriented.

```text
CTP_ALL_UNIT_CHARACTER_IS_IN_KER_PARTIAL_1 = false | TYPE-R
ALTERNATING_SQUARE_CHARACTER_IS_IN_KER_PARTIAL_1 = true | TYPE-P
```

### 4.2 What the orientation data do and do not determine

At the coefficient level,

```text
S_square=diag(1,-1,1,-1),
S_square 1_4=c_square
```

repairs the boundary. But it is only one map after the edge order and path
assignment have been frozen. The ratified input fixes:

* plus root rather than exchanged root;
* `E_post` rather than the rejected endpoint-charge alternative;
* faithful character `n`;
* tensor/zero-extension of sequential cells.

It does not fix:

* which sequential cell labels become which oriented square edges;
* which CTP branch contribution receives each alternating edge sign;
* which of the admitted finite-complex realizations is used;
* how the full untraced operator law, rather than one character vector, is
  transported;
* how state/effect traces and 2PI tangent data descend.

```text
S_SQUARE_PASSES_COEFFICIENT_BOUNDARY_TEST = true | TYPE-P |
  scope: illustrative frozen edge order only

S_SQUARE_DERIVED_FROM_DOR013 = false | TYPE-U |
  would-build: all five missing assignments/certificates above

S_SQUARE_INSTALLED = false | TYPE-S |
  scope: this determination; no realization member selected
```

The boundary vectors are not a failure of the origin or DoR-013. They refute
only the claim that the origin's existing maps already provide the requested
global square.

## 5. Four-carrier provenance account

The current chain contains four distinct carriers relevant to this relay:

| Carrier | Present map/provenance | Direct connection supplied | Missing connection |
|---|---|---|---|
| `Omega_prim,N` | ratified primitive family | `d_state`, `d_ready`, `d_law` | global cycle-generation map |
| relative-history carrier | trace/character of doubled `d_law`; `Z_law,N` | sequential CTP character | cell/edge and branch/path map |
| V005 incidence-cycle carrier | `c in ker(B_N^T)`, `Phi_c`, `u_c=dPhi_c` | Gate-4 quotient and cycle calculus | origin/relative-history dynamics map |
| stationary physical 2PI carrier | named block system | none instantiated | cycle tangent, blocks, domain, background |

The actual arrows are:

```text
Omega_prim --d_law--> U_N[a] --doubled trace--> Z_law,N,

Omega_prim --d_ready--> ready ray,

K_cell --S_inc/iota_cell--> one-cell write representation,

V005 field carrier --cycle quotient--> (Phi_c,u_c).
```

There is no current arrow

```text
Z_law,N -> (Phi_c,u_c) -> stationary 2PI cycle tangent.
```

```text
FOUR_CARRIER_ACCOUNTING_COMPLETE = true | TYPE-P
DIRECT_RELATIVE_HISTORY_TO_CYCLE_ARROW_EXISTS = false | TYPE-U
DIRECT_CYCLE_TO_2PI_ARROW_EXISTS = false | TYPE-U
```

## 6. Naturality, quotient, adjoint, and orientation certificates

Because the main map is absent, the requested certificates separate into
what is inherited and what remains unbuilt:

| Certificate | Existing result | Intertwiner result |
|---|---|---|
| sequential `N<=M` restriction | exact for `d_law` and zero-extension | target cycle refinement square **TYPE-U** |
| Gate-4 quotient | V005 cycles descend under vertex rephasing | source-to-quotient compatibility **TYPE-U** |
| adjoint compatibility | W3 restrictions exist on current field layer | intertwiner adjoint square **TYPE-U** |
| CTP/U1 covariance | finite law certificates pass | branch/path-to-edge covariance **TYPE-U** |
| orientation | plus root and `E_post` fixed | alternating global edge assignment **TYPE-U** |
| family discipline | no anchor member selected | realization-family invariance proof **TYPE-U** |
| common provenance | DoR-013 CO1-CO4 pass | inter-image fiber condition **TYPE-U** |

No certificate failure here voids DoR-013. The certificates were never in
DoR-013's declared role. They are the precise extension needed for this new
consumer.

## 7. The 2PI descent attempt

### 7.1 What remains proved

Q-310 proves on the completed source kernel in the P2 norm:

```text
beta(k,r):=D^2W[(k,0),(0,r)]=0,  k in K=ker L.
```

This statement is exact, continuous, p-free, and tail-free on its named
source carrier.

```text
COMPLETED_SOURCE_BETA_ZERO = true | TYPE-P
COMPLETED_SOURCE_BETA_ZERO_TOPOLOGY = inherited_P2_norm
P_DEPENDENCE_IN_COMPLETED_SOURCE_BETA = false | TYPE-R |
  test: kernel factor vanishes before the p-bearing scalar acts
```

### 7.2 Why the zero does not descend automatically

If a physical block were already defined as a continuous pushforward of
`beta`, any linear pushforward would preserve its zero. That conditional does
not instantiate the physical block. The untraced law can carry cycle dynamics
that the scalar germ discarded, and the physical 2PI action could contain
kernel-sector terms not in the source pullback.

The absent data are:

```text
T_N                         relative-history to incidence-cycle intertwiner;
rho_cycle,2PI               cycle tangent map;
Gamma_AA,Gamma_AG,
Gamma_GG,Gamma_GA           stationary 2PI blocks;
G_* and source-free surface physical background;
common completed domain;
restriction and Tail_R squares.
```

Defining the target block to be zero because the source block is zero would
be answer-defined transport. It is not performed.

```text
SOURCE_ZERO_PUSHFORWARD_CONDITIONAL =
  true | TYPE-P | premise: physical block is defined solely as continuous
                           pushforward through a lawful T_N

PHYSICAL_BLOCK_IS_SUCH_A_PUSHFORWARD = false | TYPE-U |
  would-build: T_N plus rho_cycle,2PI and the stationary block descent

PHYSICAL_2PI_MIXING_ZERO_PROVED = false | TYPE-U
PHYSICAL_2PI_MIXING_NONZERO_PROVED = false | TYPE-S |
  roots: no instantiated physical mixing block exists |
  exclusions: source beta and illustrative coefficient maps |
  fences: no name transport |
  query: physical Gamma_cycle,complement / Gamma_cycle,R block
```

### 7.3 2PI verdict

```text
TWO_PI_DESCENT_EXECUTED = false | TYPE-C |
  constraints: T_N, rho_cycle,2PI, and stationary blocks absent

LIFTED_FINITE_ZEROS_BECOME_PHYSICAL_CYCLE_ZEROS = NO_VERDICT
PHYSICAL_COMPLETION_GENERATES_NONZERO_MIXING = NO_VERDICT
```

## 8. Restriction checks, six-account rows, and door flags

### 8.1 Executed restriction checks

| Check | Result | Standing |
|---|---|---|
| DoR-013 one-cell ready/write reproduction | pass | **TYPE-P** |
| DoR-009 sequential zero-extension | pass | **TYPE-P** |
| Q-310 all-unit square boundary | nonzero | **refutes identity / TYPE-R** |
| Q-310 alternating square boundary | zero | **pass / TYPE-P** |
| Q-243 finite retarded kernel shadow | zero and p-free | **TYPE-P** |
| Q-279 probes-on kernel mixing | zero and p-free | **TYPE-P** |
| completed P2 source beta | zero | **TYPE-P** |
| physical intertwiner restriction square | unexecutable | **TYPE-C** |
| physical 2PI restriction square | unexecutable | **TYPE-C** |

Every executable finite restriction remains consistent. No standing
falsifier fires.

```text
DOR008_FINITE_FALSIFIER_FIRED = false | TYPE-R |
  test: no executable restriction disagrees with a sealed finite result

DOR013_NEUTRALITY_FALSIFIER_FIRED = false | TYPE-R |
  test: this result does not select an anchor member or split the state image
```

### 8.2 Six-account table

| Account | Kernel/applicability | Image | Sector transfer | Restriction square | Tail action | Verdict |
|---|---|---|---|---|---|---|
| measure | finite trace/source functional only | scalar relative character | none to cycle | finite passes | none created | physical measure **TYPE-U** |
| contour | finite CTP branch grammar | relative-history carrier | branch pair to relative cell only | finite passes | none created | branch/path-to-edge transfer **TYPE-U** |
| boundary/contact | local signed cell plus separate `partial_1` | one-cell write / cycle boundary | no global transfer | exact Q-310 boundary test | none created | orientation map **TYPE-U** |
| domain closure | completed source `K=ker L` | source beta zero | no physical cycle image | P2 norm square passes | zero | source **TYPE-P**; physical domain **TYPE-U** |
| stationary Schur | no instantiated physical blocks | none | `NO_VERDICT` | unexecutable | `NO_VERDICT` | **TYPE-U / TYPE-C check** |
| class formation | existing P2 and V005 classes separately | separate source/cycle classes | no inter-class map | separate finite checks pass | none created here | inter-class formation **TYPE-U** |

### 8.3 Door flags

```text
DOOR_D_PHYSICAL_IMAGE_EXECUTED_HERE = false | TYPE-C |
  constraint: no physical cycle 2PI image exists

DOOR_F_PROJECTIVE_LIMIT_INVOKED = false | TYPE-S |
  roots: finite origin, finite boundary test, existing P2 norm completion |
  exclusions: unbuilt refinement alternatives |
  query: projective limit in a new arrow

WEAK_STAR_OR_BIDUAL_CREATOR_INVOKED = false | TYPE-S |
  roots: every executed operation in this artifact |
  exclusions: unbuilt physical response classes |
  query: weak-star, bidual, distributional completion

UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S |
  roots: Sections 2-8 |
  exclusions: classes named only as TYPE-U |
  query: every quotient, completion, induced image, and descent
```

## 9. Exact remaining object

The smallest honest would-build is not “choose `S_square`.” It is the
following family-level factorization package:

```text
ORIGIN_TO_GLOBAL_CYCLE_FACTORIZATION_AND_ORIENTATION_PACKAGE := (
  f_rel,N:
    Omega_prim,N -> doubled relative-history character carrier,
    including the exact trace/quotient from d_law;

  g_cyc,K:
    Omega_prim,N -> C_1(K) with image in ker(B_K^T),
    including a global finite-complex assembly from local K_cell data;

  iota_N:
    sequential cells -> oriented incidence edges;

  sigma_N:
    CTP branch signs -> oriented path/edge signs;

  fiber certificate:
    f_rel(omega_1)=f_rel(omega_2)
      implies g_cyc(omega_1)=g_cyc(omega_2);

  induced T_N:
    im(f_rel,N) -> im(g_cyc,K),
    g_cyc=T_N o f_rel;

  chain/orientation certificate:
    partial_1 T_N sends admitted closed relative histories to zero-boundary
    cycles and reproduces the exact Q-310 nonclosures when closure fails;

  full-dynamics certificate:
    T_N intertwines the untraced U_N law, not only one character vector;

  naturality:
    N<=M zero-extension, finite-complex refinement, Gate-4 quotient,
    adjoints/W3, U1/CTP reality;

  family discipline:
    no anchor, realization, cycle basis, rank, or orientation member selected;
    every consumed verdict invariant across the admitted family;

  2PI continuation:
    rho_cycle,2PI, stationary blocks, background, common domains,
    restriction square, Tail_R account
).
```

The new primitive, if the factorization cannot be derived from the existing
tuple, is precisely:

```text
GLOBAL_ORIENTED_CELLULAR_ASSEMBLY_AND_BRANCH_PATH_DESCENT_RULE
```

It must turn the local rooted signed-incidence cells and the CTP branch
grammar into a global oriented complex functorially. It is not a numerical
parameter and does not select a cycle after output.

```text
NEXT_REQUIRED_OBJECT =
  ORIGIN_TO_GLOBAL_CYCLE_FACTORIZATION_AND_ORIENTATION_PACKAGE

NEXT_REQUIRED_OBJECT_BUILT = false | TYPE-U

NEW_AUTHORED_PHYSICS_PROVED_NECESSARY = NO_VERDICT |
  prerequisite: attempt the global assembly/fiber theorem across the complete
                admitted realization family
```

## 10. Physical p-verdict

| Stage | p content | Standing |
|---|---|---|
| ratified relative-history law | operator character, no state weighting | **TYPE-P** |
| scalar source germ on `ker L` | constant | **TYPE-P** |
| finite kernel and mixing blocks | zero before p factor acts | **TYPE-P** |
| completed source beta | zero and p-free in P2 norm | **TYPE-P** |
| origin-to-cycle factorization | unbuilt | **TYPE-U** |
| physical cycle 2PI blocks | unbuilt | **TYPE-U** |
| physical cycle RetHess | unbuilt | **TYPE-C check** |

The strongest current statement remains:

```text
CURRENT_SOURCE_SUPPORT_SEPARATION = true | TYPE-P

SUPPORT_SEPARATION_SURVIVES_TO_PHYSICAL_CYCLE_RESPONSE = false | TYPE-U |
  would-build: Section 9 package and lifted-zero theorem

P_SURVIVES_IN_PHYSICAL_CYCLE_RESPONSE = NO_VERDICT
P_CANCELS_FROM_PHYSICAL_CYCLE_RESPONSE = NO_VERDICT
```

The record supports neither survival nor cancellation. Reporting cancellation
would identify a completed source zero with an unbuilt physical 2PI block.
Reporting survival would invent a mixing term that no instantiated physical
block contains. Both transports are refused.

## 11. Kill passes and final typed ledger

### 11.1 Kill passes

1. A shared primitive domain was not treated as a map between output images.
2. `d_ready` was kept a ready-ray map; it was not renamed an incidence-cycle
   map.
3. Local `S_inc` was not promoted to a global `K_square` assembly.
4. Plus-root orientation, `E_post`, CTP branch orientation, and edge-cycle
   orientation were not conflated.
5. The illustrative `S_square` was not selected or installed.
6. The four carriers—origin, relative history, incidence cycle, and physical
   2PI—were kept separate.
7. The completed source zero was not relabeled physical dynamics.
8. No anchor member, realization member, cycle basis, rank, background,
   measure, contour, domain, or contact prescription was selected.
9. No class formation or completion was crossed silently.
10. No response value, root, scale, coupling, or measured target was
    evaluated.

### 11.2 Final typed ledger

```text
DOR013_GENERATES_READY_RAY = true | TYPE-P
DOR013_GENERATES_RATIFIED_FINITE_LAW = true | TYPE-P
DOR013_GENERATES_GLOBAL_INCIDENCE_CYCLE_CARRIER = false | TYPE-R |
  test: exact ratified output list and V003 map codomains

D_READY_IS_INCIDENCE_CYCLE_GENERATOR = false | TYPE-R
LOCAL_S_INC_IS_GLOBAL_K_SQUARE_INCIDENCE_MAP = false | TYPE-R
COMMON_INPUT_ALONE_INDUCES_INTER_IMAGE_MAP = false | TYPE-R

GLOBAL_CYCLE_GENERATION_MAP_FOUND = false | TYPE-S
FIBER_COMPATIBILITY_CERTIFICATE_FOUND = false | TYPE-S
BRANCH_PATH_TO_EDGE_ORIENTATION_MAP_FOUND = false | TYPE-S

CTP_RELATIVE_HISTORY_TO_INCIDENCE_CYCLE_DYNAMICS_INTERTWINER_BUILT =
  false | TYPE-U
ORIGIN_TO_GLOBAL_CYCLE_FACTORIZATION_PACKAGE_BUILT = false | TYPE-U

COMPLETED_SOURCE_BETA_ZERO = true | TYPE-P
P_DEPENDENCE_IN_COMPLETED_SOURCE_BETA = false | TYPE-R

PHYSICAL_2PI_DESCENT_BUILT = false | TYPE-U
TWO_PI_DESCENT_EXECUTED = false | TYPE-C
PHYSICAL_2PI_MIXING_ZERO_PROVED = false | TYPE-U

CURRENT_SOURCE_SUPPORT_SEPARATION = true | TYPE-P
PHYSICAL_CANCELLATION_MECHANISM_ESTABLISHED = false | TYPE-U
P_SURVIVES_IN_PHYSICAL_CYCLE_RESPONSE = NO_VERDICT
P_CANCELS_FROM_PHYSICAL_CYCLE_RESPONSE = NO_VERDICT

SELECTED_ORIENTATION_OR_REALIZATION_MEMBER_FOUND = false | TYPE-S |
  roots: all displays and constructions in this artifact |
  exclusions: illustrative S_square is not installed |
  fences: family and no-selection disciplines |
  query: selected edge order, branch/path assignment, cycle basis, anchor

UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S
FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-R |
  test: all permitted structural calculations were executed

REGISTER_HEAD_AT_CONSTRUCTION_BASIS = Q-310
REGISTER_SHA256_AT_CONSTRUCTION_BASIS =
  96ca828bb5cda01e53b12d3eb0689ed3a085491448c4f50779b56e9b300bc3b6

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

The common origin earns exactly what it was ratified to earn: genuine shared
provenance for state, ready ray, and law. It does not silently earn a fourth
global cellular output or a map between distinct descendants. The verdict's
last object is therefore still last—but now its missing mathematical content
is explicit: a global oriented assembly, a fiber-factorization theorem, and
the dynamics/2PI descent that follows them.
