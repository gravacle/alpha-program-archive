# Stage 8 Task 4a Relative-History/Cycle Factorization and 2PI Descent Verdict Build V001

Date: 2026-08-02  
Task: PASTE 395 / Task 4a  
Lane: CODEX LANE 2  
Status: **MAP ONE BUILDS AT THE CHARACTER-QUOTIENT LEVEL; THE COMPLETED CYCLE/SOURCE ZERO MAP BUILDS; THE PHYSICAL 2PI DESCENT DOES NOT; PHYSICAL p-VERDICT REMAINS `NO_VERDICT`**

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013,
                   DoR-014 as amended (2 + N), DoR-015,
                   V011 sealed c_square citation

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead determination

The two-map build splits.

**Map one constructs uniquely for the scalar relative-history character.** Let

```text
Q_rel,N isomorphic to U(1)^N,
Z_N(r)=product_(j=1)^N r_j^n,

Q_square:=U(1)^4/Gamma_square,
c_square=(1,-1,1,-1),
Hol_c([h])=product_e h_e^(c_e).
```

The square is connected, has cycle rank one, and `c_square` is primitive.
Therefore its cycle character

```text
Hol_c:Q_square -> U(1)
```

is an isomorphism. Define

```text
T_N^char
  :=Hol_c^(-1) compose Z_N
  :Q_rel,N -> Q_square.                                (M1)
```

Then, exactly,

```text
Hol_c compose T_N^char = Z_N.                          (M1-cert)
```

This is the requested factorization of **`Z_law,N`'s scalar relative-history
content** through the sealed cycle basis. It chooses no edge representative.
In V011's already sealed gauge it may be displayed as

```text
T_N^char(r)
  =[1,1,1,Z_N(r)^(-1)],
```

because the final edge has coefficient `-1`. The displayed representative is
only a check; (M1) is the quotient-level definition.

The map is exact under sequential zero-extension, Gate-4 quotienting, and the
reality law:

```text
T_M^char compose j_NM^Q = T_N^char,
T_N^char(Theta_Q r)=Theta_square(T_N^char(r)).
```

It also resolves Q-310's exact boundary comparison without pretending the
identity map worked:

```text
partial_1(1,1,1,1)^T=(-2,0,0,2)^T,
partial_1 c_square=0.
```

The source all-unit coefficient is not itself a cycle. `T_N^char` first takes
its scalar character and then uses the primitive cycle character to recover
the unique quotient class. That is why the construction closes without a
cell-to-edge bijection.

**The full dynamics-bearing version of map one does not build.** `U_N` is an
endpoint-covariant operator family, not a scalar quotient function. Equation
(M1) factors `Z_N`, `F_N`, and the conditioned scalar amplitude insofar as they
depend only on `Z_N`; it does not intertwine the full untraced `U_N` operator,
its state/effect matrix elements, or its lost per-cell information.

**The executable core of map two also constructs, but only at the completed
source-Hessian level.** V005/Q-308 already place the cycle-current line in
`K=ker L`. Let

```text
iota_c:Cyc_square -> K
```

be that existing placement, and let Q-310's continuous source mixing be

```text
beta:K x R -> C,
beta(k,r)=0.
```

Define

```text
D_beta(c,r):=beta(iota_c(c),r)=0.                      (M2-core)
```

This is a continuous, restriction-natural, reality-covariant zero map on the
completed cycle/source sector. It proves that symbolic `p` is absent from the
descended **cycle/source mixing block**.

It is not the physical stationary 2PI descent. The required codomain still
does not exist: `Gamma_AA`, `Gamma_AG`, `Gamma_GG`, `Gamma_GA`, stationary
`G_*`, the physical inverse/prescription, common measure/contour/boundary
domain, and cycle-to-2PI tangent realization remain uninstantiated. Q-309 and
Q-312 say this explicitly. Moreover, Q-308 proves that the live raw
correlator has no full inverse on the cycle sector; the cycle direction lies
in its kernel. A zero connected correlator block cannot be renamed a zero
action Hessian—the inverse/Schur object is undefined there until independent
kernel dynamics is supplied.

Therefore the requested physical cycle-sector `RetHess` does not exist at the
end of this build, and no physical cancellation/survival verdict is licensed.

```text
RELATIVE_HISTORY_TO_CYCLE_CHARACTER_FACTORIZATION_BUILT = true | TYPE-P
RELATIVE_HISTORY_TO_CYCLE_FULL_OPERATOR_INTERTWINER_BUILT = false | TYPE-U

COMPLETED_CYCLE_SOURCE_MIXING_DESCENT_BUILT = true | TYPE-P
P_IS_ABSENT_FROM_COMPLETED_CYCLE_SOURCE_MIXING = true | TYPE-P

CYCLE_TO_STATIONARY_2PI_DESCENT_BUILT = false | TYPE-U
PHYSICAL_CYCLE_RETHESS_BUILT = false | TYPE-U
TWO_PI_DESCENT_EXECUTED = false | TYPE-C |
  constraints: stationary 2PI carrier, blocks, inverse, background, and common
               physical domain absent

P_SURVIVES_IN_PHYSICAL_CYCLE_RESPONSE = NO_VERDICT
P_CANCELS_FROM_PHYSICAL_CYCLE_RESPONSE = NO_VERDICT
```

This is not a fence stop. It is a carrier/inverse obstruction. The result is
stronger than Q-312 on map one and no stronger than the available physics on
map two.

## 1. Preflight, currency, roots, and authorities

### 1.1 Preflight at construction basis

```text
DOES_THE_OBJECT_EXIST = SPLIT |
  T_N^char: built here |
  D_beta: built here |
  full U_N intertwiner: no | TYPE-U |
  stationary cycle-to-2PI descent and RetHess: no | TYPE-U

IS_THE_VERSION_CURRENT = true |
  register head: Q-312 at construction basis

ARE_THE_INPUTS_PRESENT = SPLIT |
  scalar-character factorization: yes |
  completed cycle/source zero: yes |
  stationary physical 2PI descent: no | TYPE-S |
  missing: instantiated Gamma_2PI block system, stationary background,
           inverse/prescription, and common physical domains
```

The relay's preflight statement “every input does” is therefore true for
`T_N^char` and `D_beta`, but false for the physical `RetHess` construction.
Q-312 itself lists the absent 2PI objects at its lines 490-499.

### 1.2 Roots entered

1. `/Users/bgm/MB Work/alpha_supervision/LOCKED_PROCESS.md`
2. `/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md`
3. `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md`
4. `STAGE8_COMPOSITION_LOOP_STRUCTURAL_PREDICTION_BUILD_V001.md`
5. `STAGE8_TASK4A_ORIENTATION_SEALED_FACT_REALITY_INVARIANCE_AND_P_VERDICT_DETERMINATION_V001.md`
6. `STAGE8_TASK4A_COMMON_ORIGIN_ORIENTATION_INTERTWINER_2PI_DESCENT_AND_P_VERDICT_DETERMINATION_V001.md`
7. `STAGE8_CTP_PHYS_INPUT_PACKAGE_U3_DOR008_DOR009_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md`
8. `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md`
9. `STAGE8_TASK4A_KERNEL_SECTOR_DYNAMICS_2PI_DOMAIN_BACKGROUND_AND_P_VERDICT_DETERMINATION_V001.md`
10. `STAGE8_TASK4A_PHYSICAL_INVERSE_SCHUR_COMPLETED_DOMAIN_AND_P_VERDICT_ATTEMPT_V001.md`
11. `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md`
12. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V007.md`
13. `STAGE8_TASK4A_P2_PHYSICAL_SOURCE_TOPOLOGY_AND_DIFFERENTIAL_CALCULUS_CONSTRUCTION_V002.md`

All unqualified paths are rooted at the current cleanroom.
`a32_holdout/custodian_private/` was not entered, listed, or inspected.

### 1.3 Frozen authority hashes

| Authority | SHA-256 | Load-bearing use |
|---|---|---|
| Locked process | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | fences and custody |
| Register through Q-312, construction basis | `8ac9bd2739fbbf9ca8125f21ce0d30c8d28ef2c2555b7ee3037f9a53056d0dce` | live standing |
| V011 | `20a3a17d44e15841baded9eaed3fdbecfde0ecb14bdb8162ea41a8bcd21d1a48` | sealed edges, order, traversal, and gauge |
| Composition-loop structural build | `5810377123b823e680891a3337855750ac8f362951dca048dad3a78a34c79d79` | ordinary boundary, rank-one cycle, primitive generator |
| Q-312 determination | `0a5ea70df1f4fd708cfdd346780b7c55daee5d94b72f8c8f0d303c4147f2f82a` | orientation closure and covariance correction |
| Q-311 determination | `b556fb2496e2edf32c91824dcbcd3eb842397af25a26d5d62950e2bee19cbfd7` | factorization criterion and four-carrier account |
| U3 finite quotient | `b0118d89e0b4b321fbf9caab5bfb811a0b5fd572e808d02615ee8503db2bc1ac` | `Q_N`, `q_N`, `Z_N`, zero-extension, reality |
| Field signature V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | physical cycle quotient, `Phi_c`, `u_c` |
| Q-309 determination | `a4c916a7cfa82c2130c82d8947c869f118e224959d7824bba45695711b4919c3` | two-sector source zero and absent 2PI blocks |
| Q-308 inverse attempt | `c09783785546a8d6273b2fd104f3aeea0751e83c337ee4e8ac7677d9df87f3d0` | no full inverse on cycle sector |
| Raw correlator-to-RetHess spec | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | physical inverse, Schur, and RetHess signatures |
| Source germ V007 | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | live connected raw correlator |
| P2 V002 | `40b2af34443e051fffdc7bf2ec7025c811a98c501a82d19164596ee6f37f00c1` | source topology and completed-kernel continuity |

### 1.4 Symbol collisions bearing on the result

```text
Z_N                  scalar relative-history character, not U_N;
U_N                  endpoint-covariant operator law, not a function on Q_N;
Q_rel,N              common-gauge relative-history quotient, not Q_square;
Q_square             Gate-4 edge-connection quotient, not the CTP quotient;
c_square             primitive incidence cycle, not the all-unit CTP exponent;
beta                 connected source Hessian block, not Gamma_2PI;
G^007                 raw connected correlator, not its action-Hessian inverse;
RetHess_phys          stationary reduced action Hessian, not a zero source block.
```

No identity below crosses these typings silently.

## 2. Map one: the scalar character factorization

### 2.1 Source quotient and consumed content

The U3 result defines (`:190-253`)

```text
q_N:X_N -> Q_rel,N isomorphic to U(1)^N,
q_N(z_+,z_-)=r,
r_j=conjugate(z_(-,j))z_(+,j).
```

It proves this is the complete common-gauge orbit invariant. The scalar law
content descends exactly (`:258-306`):

```text
Z_N(r)=product_j r_j^n,
Fbar_N(r)=P_0+Z_N(r)P_ch,
Abar_N^(p)(r)=(1-p)+p Z_N(r).
```

`U_N` does not descend as a scalar quotient function; it remains endpoint
covariant (`:295-310`). Thus the maximal honest source for map one is
`Z_N` and every existing object already proved to factor through it.

### 2.2 Target quotient and primitive character

V011 freezes the oriented square and edge order at `:1840-1901`. The
structural build proves

```text
rank(partial_1)=3,
ker(partial_1)=Z c_square,
c_square=(1,-1,1,-1),
```

with `c_square` primitive. V005 defines the Gate-4 quotient and its cycle
character:

```text
Q_square=U(1)^4/Gamma_square,
Hol_c([h])=product_e h_e^(c_e).
```

Because the graph is connected and has one cycle, `Q_square` has one compact
`U(1)` coordinate. V005's separation theorem says the complete cycle family
separates the quotient. Here the family is generated by the single primitive
`c_square`; hence

```text
Hol_c:Q_square -> U(1)
```

is injective and surjective. Surjectivity is also explicit in V011's fixed
gauge: for any `z in U(1)`, the class of `(1,1,1,z^(-1))` has cycle holonomy
`z`. Therefore `Hol_c` is an isomorphism without a selected physical gauge
representative.

```text
HOL_C_IS_PRIMITIVE_CYCLE_COORDINATE = true | TYPE-P
HOL_C_IS_Q_SQUARE_TO_U1_ISOMORPHISM = true | TYPE-P
```

### 2.3 Construction and uniqueness

Define (M1):

```text
T_N^char:=Hol_c^(-1) compose Z_N.
```

It is the unique map `T:Q_rel,N->Q_square` satisfying

```text
Hol_c compose T=Z_N.
```

Proof: existence is the displayed composition. If `T'` obeys the same
identity, injectivity of `Hol_c` gives `T'=T` pointwise.

This proves Q-311's fiber condition for the scalar content. If

```text
Z_N(r)=Z_N(r'),
```

then

```text
T_N^char(r)=Hol_c^(-1)(Z_N(r))
           =Hol_c^(-1)(Z_N(r'))
           =T_N^char(r').
```

The fibers deliberately collapse the `N-1` relative-history directions that
the scalar law already discards. No extra loss is introduced beyond `Z_N`'s
sealed consumption signature.

```text
T_CHAR_N_EXISTS = true | TYPE-P
T_CHAR_N_UNIQUE = true | TYPE-P
T_CHAR_N_FIBER_FACTORIZATION_CERTIFICATE = PASS | TYPE-P
T_CHAR_N_SELECTS_EDGE_REPRESENTATIVE = false | TYPE-R |
  test: codomain is Q_square and definition uses Hol_c inverse on classes
```

### 2.4 Exact boundary certificate

For `N=4`, the rejected coefficient identity gives

```text
partial_1(1,1,1,1)^T=(-2,0,0,2)^T.
```

Map (M1) does not assert this vector is a cycle. Its target coordinate is the
primitive class represented by `c_square`, and

```text
partial_1 c_square=0.
```

In V011's fixed gauge the output representative

```text
h(r)=(1,1,1,Z_N(r)^(-1))
```

obeys

```text
Hol_c([h(r)])=Z_N(r).
```

Thus the Q-310 nonclosure is reproduced on the rejected identity candidate,
and exact closure is reproduced on the constructed target. No boundary datum
is altered.

```text
M1_REPRODUCES_Q310_NONCLOSURE = true | TYPE-P
M1_TARGET_IS_IN_INCIDENCE_CYCLE_QUOTIENT = true | TYPE-P
```

### 2.5 Restriction and quotient naturality

U3 proves for `N<=M`:

```text
j_NM^Q(r_1,...,r_N)=(r_1,...,r_N,1,...,1),
Z_M compose j_NM^Q=Z_N.
```

Therefore

```text
T_M^char compose j_NM^Q
 =Hol_c^(-1) compose Z_M compose j_NM^Q
 =Hol_c^(-1) compose Z_N
 =T_N^char.
```

Gate-4 quotient naturality is built into the codomain: `Hol_c` is defined on
classes and is representative-independent because `partial_1 c=0`.

```text
M1_ZERO_EXTENSION_NATURALITY = PASS | TYPE-P
M1_GATE4_QUOTIENT_NATURALITY = PASS | TYPE-P
```

This does not assert naturality under an arbitrary finite-complex refinement.
No general refinement functor from sequential cells to arbitrary incidence
complexes is used or created.

```text
M1_ARBITRARY_CELLULATION_NATURALITY_BUILT = false | TYPE-U |
  would-build: a functor assigning a primitive cycle-coordinate system to
               each admitted finite complex, with refinement squares
```

### 2.6 Reality covariance

On the relative quotient,

```text
Theta_rel(r)=conjugate(r),
Z_N(Theta_rel r)=conjugate(Z_N(r)).
```

On the square quotient let

```text
Theta_square([h])=[conjugate(h)].
```

Then

```text
Hol_c(Theta_square[h])=conjugate(Hol_c([h])).
```

By injectivity of `Hol_c`,

```text
T_N^char(Theta_rel r)=Theta_square(T_N^char(r)).
```

This is covariance, not pointwise invariance. Under traversal reversal
`c->-c`, the coordinate inverts; Q-312's orientation-family theorem preserves
zero support and symbolic `p` dependence.

```text
M1_REALITY_COVARIANCE = PASS | TYPE-P
M1_POINTWISE_REALITY_INVARIANCE_CLAIMED = false | TYPE-R |
  test: nontrivial classes map to inverse/conjugate partners
```

### 2.7 Scope ceiling of map one

Map (M1) factors only the scalar character consumed by `F_N` and `A_N`.
The U3 authority expressly says (`:295-302`) that `U_N` is an endpoint-
covariant operator family and no fiber trivialization turns it into a scalar
function on `Q_rel,N`. It also says (`:700-718`) that `q_N` does not express
the incidence operator or close the comparison intertwiners.

Accordingly:

```text
M1_FACTORS_Z_N = true | TYPE-P
M1_FACTORS_F_N_AND_A_N_THROUGH_THEIR_Z_N_CONTENT = true | TYPE-P
M1_INTERTWINES_FULL_UNTRACED_U_N = false | TYPE-U |
  would-build: endpoint-representation and state/effect operator descent on
               the global incidence carrier
M1_IS_A_FULL_DYNAMICS_INTERTWINER = false | TYPE-R |
  test: scalar quotient codomain versus endpoint-covariant operator codomain
```

## 3. Map two: what descends and what resists

### 3.1 Existing cycle placement

V005 supplies the cycle current and differential:

```text
u_c(a)=<c,L_edge a>,
d Phi_c=u_c.
```

Q-308/Q-309 place the nonzero square cycle current in the completed physical
linear-source kernel:

```text
iota_c:Cyc_square -> K=ker L.
```

No cycle basis is selected: in the rank-one square, `Cyc_square` is the line
generated by the sealed primitive cycle, and reversal is handled covariantly.

### 3.2 Completed zero descent

Q-310 proves in the P2 norm:

```text
beta:K x R -> C,
beta(k,r)=D^2W[(k,0),(0,r)]=0.
```

Define (M2-core):

```text
D_beta:Cyc_square x R -> C,
D_beta(c,r):=beta(iota_c(c),r).
```

Then `D_beta=0`. Continuity follows from continuity of `iota_c` on the named
finite cycle line and Q-310's P2-continuous beta. The dense finite cycle core
is mapped into the dense finite kernel core, and zero has the unique P2
continuous extension. Reality covariance gives

```text
D_beta(-c,Theta r)=conjugate(D_beta(c,r))=0.
```

No topology beyond the inherited P2 norm is used.

```text
M2_COMPLETED_CYCLE_SOURCE_ZERO_MAP_BUILT = true | TYPE-P
M2_SOURCE_TOPOLOGY = inherited_P2_norm
M2_FINITE_CORE_DENSE = true | TYPE-P
M2_RESTRICTION_NATURALITY = PASS | TYPE-P
M2_REALITY_COVARIANCE = PASS | TYPE-P
M2_CREATED_TAIL = false | TYPE-R |
  test: continuous zero extension inside the existing norm class
P_DEPENDENCE_IN_M2_SOURCE_ZERO_MAP = false | TYPE-R |
  test: kernel factor vanishes before the q(1-q) coefficient acts
```

### 3.3 Why this is not the stationary 2PI descent

The raw-map specification defines the physical response through:

```text
delta Gamma_2PI/delta G |_(G_*,R=0)=0,

D^2 Gamma_1PI
 =Gamma_AA-Gamma_AG Gamma_GG^(-1) Gamma_GA,

H_C[G]=i hbar I_C[G],
H_R=(T_CTP^T H_C T_CTP)_(delta,c).
```

All objects must share one physical quotient, measure, contour, boundary
prescription, and domain. These are action/Legendre objects. `D_beta` is a
connected source derivative.

The distinction is refuted as an identity by Q-309:

```text
FINITE_SOURCE_BLOCK_EQUALS_STATIONARY_2PI_BLOCK_SYSTEM = false | TYPE-R.
```

The variables, differentiation, carriers, and stationary condition differ.
Map (M1) does not change this typing; it only transports the scalar character.

```text
M2_SOURCE_ZERO_IS_GAMMA_2PI_CYCLE_BLOCK = false | TYPE-R |
  test: source Hessian versus stationary action-Hessian signatures
```

### 3.4 The inverse obstruction survives map one

The live raw correlator is

```text
G^007=-hbar^2 q(1-q)L tensor L.
```

Q-308 proves that the physical cycle current is nonzero and lies in `ker L`.
Therefore `G^007` has no full inverse on the physical carrier. Map (M1)
changes only how the scalar character is represented; it does not add a
nondegenerate kernel-sector block.

A zero correlator block is not a zero inverse block. On the cycle sector the
inverse is undefined, not zero. Assigning zero to the action Hessian would
replace the missing inverse/Schur dynamics with the desired verdict.

```text
G007_FULL_PHYSICAL_INVERSE_EXISTS_AFTER_M1 = false | TYPE-R |
  test: the nonzero cycle current remains in ker L

ZERO_CONNECTED_BLOCK_IMPLIES_ZERO_ACTION_HESSIAN = false | TYPE-R |
  test: inversion is undefined on the zero/kernel block
```

### 3.5 Exact absent 2PI data

Q-309 (`:419-490`) and Q-312 (`:481-525`) jointly leave absent:

```text
rho_cycle,2PI;
Gamma_AA, Gamma_AG, Gamma_GG, Gamma_GA;
stationary G_* and the source-free background;
Gamma_GG inverse/prescription;
common physical measure and contour;
boundary/contact form;
common invariant operator domain;
physical restriction and Tail_R squares;
proof excluding additional kernel-sector action terms outside the source
  pullback.
```

These are inputs to the physical `RetHess`, not optional certificates after it
has been formed. No operation in (M1) or (M2-core) supplies them.

```text
STATIONARY_2PI_BLOCK_SYSTEM_BUILT = false | TYPE-U
PHYSICAL_BACKGROUND_REALIZATION_BUILT = false | TYPE-U
COMPLETED_PHYSICAL_OPERATOR_DOMAIN_BUILT = false | TYPE-U
PHYSICAL_CYCLE_TO_2PI_TANGENT_MAP_BUILT = false | TYPE-U
PHYSICAL_RETHESS_BUILT = false | TYPE-U
```

### 3.6 Map-two verdict

```text
MAP_TWO_SOURCE_LEVEL_CORE = BUILT | TYPE-P
MAP_TWO_STATIONARY_2PI_DESCENT = UNBUILT | TYPE-U
MAP_TWO_EXECUTION_CHECK = BLOCKED | TYPE-C |
  constraints: exact absent data in Section 3.5
```

This is the exact typed obstruction requested by the relay's fallback clause.
It is not an assertion that no admissible 2PI completion exists.

## 4. Symbolic p trace

### 4.1 Built chain

The symbolic dependence through the built maps is:

```text
q or p-state datum
  -> Abar_N and G^007 complement block through q(1-q)
  -> scalar character Z_N
  -> T_N^char cycle quotient coordinate;

cycle source direction
  -> iota_c(Cyc_square) subset ker L
  -> D_beta=0 before q(1-q) acts.
```

Thus:

```text
P_APPEARS_IN_CHARACTER_VALUE_T_N = false | TYPE-R |
  test: T_N depends on Z_N and sealed c_square, not the state weighting

P_APPEARS_IN_CONDITIONED_SCALAR_AMPLITUDE = true | TYPE-P |
  form: existing conditional coefficient outside T_N

P_APPEARS_IN_COMPLEMENT_RAW_CORRELATOR = true | TYPE-P |
  form: existing q(1-q) coefficient

P_APPEARS_IN_COMPLETED_CYCLE_SOURCE_MIXING = false | TYPE-R |
  test: D_beta=0 before the coefficient acts
```

### 4.2 Why the physical verdict still does not follow

The physical question concerns `RetHess_phys`, an inverse/Schur action
operator. It is not the character value, conditioned amplitude, raw
correlator, or source mixing. The missing kernel-sector inverse and 2PI mixing
could determine whether complement dependence reaches the physical cycle
action. No current map settles that transfer.

```text
P_APPEARS_IN_PHYSICAL_CYCLE_RETHESS = NO_VERDICT
P_SURVIVES_IN_PHYSICAL_CYCLE_RESPONSE = NO_VERDICT
P_CANCELS_FROM_PHYSICAL_CYCLE_RESPONSE = NO_VERDICT
```

The finite and completed source evidence remains one-sided and exact; it is
not promoted across a missing Legendre/inverse operation.

## 5. Restriction certificates

| Check | Result | Standing |
|---|---|---|
| Q-310 all-unit boundary | `(-2,0,0,2)` | **PASS / TYPE-P** |
| sealed `c_square` boundary | zero | **PASS / TYPE-P** |
| `Hol_c T_N=Z_N` | exact | **PASS / TYPE-P** |
| equal-history `r=1` | trivial cycle class | **PASS / TYPE-P** |
| `N<=M` zero-extension | `T_M j_NM=T_N` | **PASS / TYPE-P** |
| Gate-4 quotient | representative-independent | **PASS / TYPE-P** |
| reality | covariant, not invariant | **PASS / TYPE-P** |
| Q-243 finite cycle/source mixing | zero and p-free | **PASS / TYPE-P** |
| Q-279 probes-on cycle/source mixing | zero and p-free | **PASS / TYPE-P** |
| P2 completed cycle/source mixing | zero and p-free | **PASS / TYPE-P** |
| full untraced `U_N` intertwining | unexecutable | **TYPE-C** |
| physical 2PI restriction | unexecutable | **TYPE-C** |

No executable restriction disagrees with sealed finite material.

```text
DOR008_FINITE_FALSIFIER_FIRED = false | TYPE-R |
  test: every executable restriction agrees

DOR013_NEUTRALITY_FALSIFIER_FIRED = false | TYPE-R |
  test: no anchor member or state weighting selected

DOR015_DOOR_FIRED = false | TYPE-S |
  roots: maps M1 and M2-core only |
  exclusions: unexecutable physical 2PI image |
  fences: no passing claim for an absent check |
  query: a disagreement on an executed field-layer restriction
```

## 6. Six-account rows and doors

### 6.1 Six-account table

| Account | Kernel/applicability | Image | Sector transfer | Restriction square | Tail action | Verdict |
|---|---|---|---|---|---|---|
| measure | no measure consumed by M1/M2-core | quotient character / scalar zero | none | finite checks pass | none created | physical 2PI measure **TYPE-U** |
| contour | relative quotient and Theta action | covariant cycle quotient | scalar character only | zero-extension/reality pass | none created | full branch/operator transfer **TYPE-U** |
| boundary/contact | primitive cycle character | `Q_square`, then zero source mixing | relative scalar to cycle class | exact boundary pass | none created | physical contact descent **TYPE-U** |
| domain closure | P2-completed `K`; finite cycle line | continuous zero map | cycle source to bilocal dual | dense-core square passes | zero | source **TYPE-P**; physical operator domain **TYPE-U** |
| stationary Schur | no block system/inverse | none | `NO_VERDICT` | unexecutable | `NO_VERDICT` | **TYPE-U / TYPE-C check** |
| class formation | compact quotient isomorphism; P2 zero extension | `Q_square`; completed source zero | no 2PI class transfer | named topologies pass | no tail created | 2PI class **TYPE-U** |

### 6.2 Door flags

```text
DOOR_D_CHARACTER_QUOTIENT_IMAGE = PASS | TYPE-P
DOOR_D_PHYSICAL_2PI_IMAGE_EXECUTED = false | TYPE-C |
  constraint: no physical cycle 2PI image or RetHess

DOOR_F_PROJECTIVE_LIMIT_INVOKED = false | TYPE-S |
  roots: compact finite quotients and inherited P2 completion |
  exclusions: arbitrary cellulation refinement |
  query: projective class formation in M1 or M2-core

WEAK_STAR_OR_BIDUAL_CREATOR_INVOKED = false | TYPE-S |
  roots: every executed arrow |
  exclusions: absent physical response class |
  query: weak-star, bidual, distributional completion

UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S |
  roots: Q_rel,N, Q_square, P2 K, and both maps |
  exclusions: objects only named TYPE-U |
  query: every quotient, inverse image, completion, and descent
```

## 7. Exact remaining object

Map one removes the scalar-character part of Q-312's residue. What remains is
not another orientation datum. It is:

```text
FULL_UNTRACED_DYNAMICS_AND_STATIONARY_2PI_DESCENT_PACKAGE := (
  endpoint-covariant operator intertwiner for U_N on the incidence carrier;
  state/effect trace preserving the per-cell matrix elements discarded by Z_N;
  cycle-to-2PI tangent realization rho_cycle,2PI;
  an instantiated physical Gamma_2PI;
  Gamma_AA, Gamma_AG, Gamma_GG, Gamma_GA at stationary G_*;
  kernel-sector dynamics making the physical inverse/Schur operation defined
    without deleting the record-visible cycle;
  common measure, contour, boundary/contact data, and invariant domain;
  restriction, adjoint, reality, Tail_R, and door squares;
  theorem whether the cycle block is solely the pushforward of D_beta or
    contains additional kernel-sector dynamics.
).
```

```text
NEXT_REQUIRED_OBJECT =
  FULL_UNTRACED_DYNAMICS_AND_STATIONARY_2PI_DESCENT_PACKAGE

NEXT_REQUIRED_OBJECT_BUILT = false | TYPE-U

NEW_AUTHORED_PHYSICS_PROVED_NECESSARY = NO_VERDICT |
  prerequisite: attempt the package from the full untraced ratified law and
                physical domain data
```

## 8. Kill passes and final typed ledger

### 8.1 Kill passes

1. The sealed traversal was used as a primitive cycle coordinate, not as a
   full dynamics map.
2. The all-unit CTP coefficient was not relabeled a cycle.
3. `T_N^char` was defined on quotient classes; no edge gauge representative
   was selected.
4. Reality was used as covariance only.
5. Scalar `Z_N` and endpoint-covariant `U_N` were not identified.
6. The source Hessian zero was not renamed a stationary 2PI block.
7. The zero raw-correlator kernel was not naively inverted.
8. No cycle, anchor, realization, rank, background, measure, contour, contact,
   or domain member was selected.
9. No unflagged completion or class formation was invoked.
10. No physical value, root, scale, coupling, or measured target was
    evaluated.

### 8.2 Final typed ledger

```text
HOL_C_IS_Q_SQUARE_TO_U1_ISOMORPHISM = true | TYPE-P
T_CHAR_N_EXISTS = true | TYPE-P
T_CHAR_N_UNIQUE = true | TYPE-P
T_CHAR_N_FIBER_FACTORIZATION_CERTIFICATE = PASS | TYPE-P
M1_BOUNDARY_CERTIFICATE = PASS | TYPE-P
M1_ZERO_EXTENSION_NATURALITY = PASS | TYPE-P
M1_GATE4_QUOTIENT_NATURALITY = PASS | TYPE-P
M1_REALITY_COVARIANCE = PASS | TYPE-P

M1_INTERTWINES_FULL_UNTRACED_U_N = false | TYPE-U
M1_ARBITRARY_CELLULATION_NATURALITY_BUILT = false | TYPE-U

M2_COMPLETED_CYCLE_SOURCE_ZERO_MAP_BUILT = true | TYPE-P
P_DEPENDENCE_IN_M2_SOURCE_ZERO_MAP = false | TYPE-R
M2_CREATED_TAIL = false | TYPE-R

M2_SOURCE_ZERO_IS_GAMMA_2PI_CYCLE_BLOCK = false | TYPE-R
G007_FULL_PHYSICAL_INVERSE_EXISTS_AFTER_M1 = false | TYPE-R
ZERO_CONNECTED_BLOCK_IMPLIES_ZERO_ACTION_HESSIAN = false | TYPE-R

STATIONARY_2PI_BLOCK_SYSTEM_BUILT = false | TYPE-U
PHYSICAL_CYCLE_TO_2PI_TANGENT_MAP_BUILT = false | TYPE-U
PHYSICAL_RETHESS_BUILT = false | TYPE-U
TWO_PI_DESCENT_EXECUTED = false | TYPE-C

P_APPEARS_IN_COMPLETED_CYCLE_SOURCE_MIXING = false | TYPE-R
P_APPEARS_IN_PHYSICAL_CYCLE_RETHESS = NO_VERDICT
P_SURVIVES_IN_PHYSICAL_CYCLE_RESPONSE = NO_VERDICT
P_CANCELS_FROM_PHYSICAL_CYCLE_RESPONSE = NO_VERDICT

SELECTED_ORIENTATION_OR_REALIZATION_MEMBER_FOUND = false | TYPE-S |
  roots: every definition and certificate in this artifact |
  exclusions: V011 gauge used only as a displayed check |
  fences: quotient-level definition and no-selection discipline |
  query: selected edge representative, traversal, cycle basis, anchor

UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S
FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-R |
  test: all permitted constructions and obstruction checks executed

REGISTER_HEAD_AT_CONSTRUCTION_BASIS = Q-312
REGISTER_SHA256_AT_CONSTRUCTION_BASIS =
  8ac9bd2739fbbf9ca8125f21ce0d30c8d28ef2c2555b7ee3037f9a53056d0dce

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

The build retires the scalar factorization honestly: `Z_N` now factors
uniquely through the sealed primitive cycle coordinate, with every requested
finite certificate. It also transports the completed source zero onto the
cycle/source sector. The physical verdict does not follow because the next
operation is not another quotient map—it is an inverse/Schur construction on
an uninstantiated stationary 2PI carrier, and the live correlator is singular
precisely where the physical cycle lives.
