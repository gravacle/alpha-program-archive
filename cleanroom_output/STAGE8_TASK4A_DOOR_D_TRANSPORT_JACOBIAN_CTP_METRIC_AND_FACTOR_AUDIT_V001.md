# STAGE8 TASK 4A DOOR D TRANSPORT JACOBIAN CTP METRIC AND FACTOR AUDIT V001

Date: 2026-08-02

Lane: CODEX LANE 1

Task: PASTE 387 / Task 4a

Register head issued: Q-303

Register head incorporated at completion: Q-304

## 0. LEAD VERDICT

`DOOR_D_TRANSPORT_AUDIT_VERDICT = TEST-CLEAN`

The two prior Door-D firings are not artifacts of a dropped source Jacobian,
an omitted CTP metric sign, a repeated Keldysh transformation, or a duplicated
factor of `i/hbar`. The full transport is covariant under the ratified source
intertwiners, and every map between the germ chart and the comparison carrier
is real and factor-free in the complex scalar slot. None can supply or remove
the complex phase at issue.

The exact source-chart calculation is:

```text
Xi=L-(1/2)Q,
Z=(1-p)+p exp(Xi),
q=p exp(Xi)/Z,
W=-i hbar Log_0 Z,

D_J Abar
  =-i hbar q(1-q)L tensor L,

G_b
  =i hbar q b+hbar^2 q^2 L tensor L,

D_J Abar-(i/hbar)G_b
  =q[b-i hbar L tensor L].                         (TA-1)
```

Every Jacobian and branch transformation acts on both tensors in (TA-1) by
the same pullback. Therefore the equality is invariant under transport. The
factor `i` in the required source tensor is not a second copy of the `i` in
`W`; it is the coefficient left after the separately sealed `(i/hbar)` raw
identity acts on the bilocal derivative.

Consequences:

```text
Q300_IDENTITY_FIRING_SURVIVES_TRANSPORT_AUDIT = true
Q302_U1_SIGN_FIRING_SURVIVES_TRANSPORT_AUDIT = true
Q304_EVEN_PAIRING_RESIDUAL_SURVIVES_TRANSPORT_AUDIT = true

TEST_TRANSPORT_DEFECT_FOUND = false | TYPE-S |
  roots: Sections 5-9 complete transport diagram |
  exclusions: no repair or alternative source law installed |
  fences: audit only |
  query: omitted Jacobian, metric, branch sign, Keldysh transform, quotient,
         restriction adjoint, duplicated i, omitted hbar, or missing factor 2
```

The Q-304 residual

```text
hbar q(1-i)L tensor L
```

is consequently not a plumbing residual. It is the exact mismatch between a
`Theta`-even source-slot coefficient and the coefficient required by the
unchanged same-correlator identity. Resolving that mismatch requires a
principal disposition or a separately derived source-to-output structure; no
such structure is silently present in the ratified transport.

## 1. GATES, CUSTODY, AND LATER RULING

```text
alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

The register was Q-303 at the start of this audit. Before authoring, Q-304
landed and directly bore on the item. It is incorporated as later authority,
as required by the relay.

```text
REGISTER_HEAD_AT_START = Q-303 |
  register_sha256=fb6aaad868bb109dbd0e67abd65ee34abb2bfe4b0a6a570c4c79eddb67d94bc3

REGISTER_HEAD_AT_COMPLETION = Q-304 |
  register_sha256=60b02a2d75b794dfb23226dca8d748dbceb01381060c637f0b2d399406e2c706

LATER_BEARING_REGISTER_ENTRY_FOUND = true |
  entry: Q-304 |
  effect: adds the even-pairing residual and holds disposition for this audit
```

Q-304 was not used to choose the verdict. The factor audit below independently
derives (TA-1); Q-304 is then checked against it.

Custody follows
`/Users/bgm/MB Work/alpha_supervision/LOCKED_PROCESS.md`: this lane writes,
seals, verifies, mirrors artifact and sidecar, reports, and stops.

```text
REGISTER_TRACKER_PLAN_EDITED = false | TYPE-S |
  roots: this lane's custody acts |
  exclusions: reviewer-only steps |
  fences: Q-91 custody |
  query: register, tracker, or plan edit

GIT_COMMIT_PUSH_DEPLOY_PERFORMED = false | TYPE-S |
  roots: this lane's custody acts |
  exclusions: none |
  fences: Q-91 custody |
  query: git, commit, push, deploy

DOR015_FREEZE_LIFTS = false | TYPE-C |
  constraint: this audit diagnoses the test and performs no principal
              disposition or source-germ installation
```

## 2. SCOPE

### 2.1 Roots entered

1. `/Users/bgm/MB Work/alpha_supervision/LOCKED_PROCESS.md`
2. `/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md`
3. `/Users/bgm/MB Work/alpha_supervision/DECISION_OF_RECORD_015_FIELD_SIGNATURE_PHYS_RATIFIED_2026-08-02_V001.md`
4. `STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md`
5. `STAGE8_CTP_PHYS_INPUT_PACKAGE_U1_DOR008_ASSEMBLY_DETERMINATION_V001.md`
6. `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V002.md`
7. `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md`
8. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md`
9. `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md`
10. `../primitive_record_cell_selection_principle_v004.md`
11. `STAGE8_TASK4A_FINITE_HESSIAN_TO_DELTAPHI_TRANSPORT_MAP_CONSTRUCTION_AND_P_CH_TRACE_V001.md`
12. `STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md`
13. `STAGE8_TASK4A_RAW_G_RERUN_ON_RATIFIED_SIGNATURE_AND_DOOR_D_EXECUTION_V001.md`
14. `STAGE8_TASK4A_DOOR_D_FALSIFIER_CARRIER_AND_CHECK_DIAGNOSIS_V001.md`
15. `STAGE8_TASK4A_DOR014_AMENDMENT1_DERIVED_PAIRING_AND_DOOR_D_REEXECUTION_V001.md`
16. `STAGE8_TASK4A_RATIFIED_BILOCAL_INVOLUTION_REALITY_LAW_DETERMINATION_V001.md`
17. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V006.md`
18. `STAGE8_TASK4A_DOR014_AMENDMENT2_EVEN_PAIRING_FULL_DOOR_D_REEXECUTION_V001.md`

All unqualified Stage-8 paths are rooted at:

`/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/`

### 2.2 Exclusions

- `a32_holdout/custodian_private/` was not entered.
- Relay 386 was not consulted before its result became registered Q-304.
- No alternative source map, metric, involution, normalization, pairing, or
  physical source family was installed.
- No DoR-015-dependent downstream construction was entered.
- No response, inverse, root, coupling, scale, spectrum, interval, or measured
  comparison was evaluated.
- No rank, anchor, frame, cycle basis, background, or endpoint member was
  selected.

### 2.3 Word-bounded queries

```text
K_J
K_R
U_B
source map
source intertwiner
Jacobian
s_J
s_R
eta_CTP
T_CTP
metric
Keldysh
i/hbar
W=-i hbar
same-correlator
restriction adjoint
cycle current
endpoint-covariant
Theta_J
Theta_R
```

### 2.4 Premises beyond the current stack

`PREMISES_BEYOND_CURRENT_STACK = none`

The chain-rule and symmetric-square identities used below are ordinary finite
and Banach-space calculus applied to the ratified maps. They introduce no
physical premise.

## 3. VERIFIED AUTHORITIES

| Authority | SHA-256 | Load-bearing use |
|---|---|---|
| Questions register through Q-304 | `60b02a2d75b794dfb23226dca8d748dbceb01381060c637f0b2d399406e2c706` | current ruling and later-bearing entry |
| DoR-015 | `617bd51a70860d2cfb2066640630ba37ec289d56255ebbe1433bc0dfcba0159d` | adopted V005 carrier, W3 precision, open Door D |
| Field signature V002 | `deaa86ee58edb9f841ae3f7bae8ccf9b1cf659328b99fb60cd290a348641e1ad` | `U_B`, `K_J`, `K_R`, frozen Door-D rerun |
| Field signature V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | cycle restriction, current source and bilocal classes |
| Field/CTP presentation V002 | `76916244bdbcac7c2a6d4afae40f35127540d1d9e4cfc86fb72318506671161f` | linear and bilocal insertion maps, factor `1/2` |
| U1_008 | `1b0e928c452c10a8be72be22ff81fd7677f5045d2ad8d398a9f7f7f57b9ab3b0` | branch metric, Keldysh matrix, source involutions |
| Source germ V004 | `d4cdbb6623797df6accb7dc9b24134d179bfc8e8d039c585d5c91ae23255869e` | live `Xi`, `Z`, and `W` calculus |
| Raw-map specification | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | raw `G` and condition 6 |
| Active v004 principle | `13d227ceb2198d96b0e4e2fef57b874cea71cb755320508fbf4c6d64a00c507e` | source exponent and physical Legendre convention |
| Q-243 finite transport | `70185aa842bc500724719c65bd66b5f07005e2214b97be0d35e07fd029d5c68c` | exact branch/Keldysh finite control |
| Q-279 finite nonzero-R reference | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | exact independent J/R chart |
| Q-300 Door-D execution | `bffd7ef240204232a957422d60ce164151131fdbb46433def7d943d21b915382` | first firing |
| Q-302 Door-D execution | `365db191e3867129a02b2216fcf10b5fc83f53b0a03cef590dfe0671c63588d9` | second firing |
| Q-303 reality determination | `323852e8835175c30d503f0383ef735405d8bc40a98109e09f5974e49c603c22` | exact source/output parity split |
| Q-304 source germ V006 | `343117b7f75eba02725c6955086e5988116c51c1717d809b4822c0ba3110e4dd` | even candidate and residual |
| Q-304 Door-D execution | `bf74ee5be76c70c688c2becf04d1ca3ad127f79253001ac7c5b6dfb70cadddf1` | third firing held for this audit |

## 4. OBJECT AND INDEX DISTINCTIONS

1. `J` is a linear source covector. It is not a field vector merely because
   the A4 Hilbert rigging represents both with the same coefficient labels.
2. `R` is the symmetric bilocal source. It is not the retarded block.
3. `K_R` is the symmetric-square transport induced by `K_J`. It is not a
   second unrelated source choice.
4. `eta_CTP` identifies oriented branch indices. It is not the positive
   Hilbert inner product used to represent a bounded bilinear form.
5. `T_CTP` changes branch coordinates. It does not add a complex phase.
6. `P_delta` names the difference block. It is not a hidden application of
   `eta_CTP`.
7. The factor `1/2` in `s_R` and in `Xi` is owned by symmetric bilocal-source
   insertion. The factor `2` in `G=2D_R W-Abar tensor Abar` cancels it once.
8. The factor `-i hbar` is owned by `W=-i hbar Log_0 Z`.
9. The factor `i/hbar` is owned by raw-domain condition 6. It is not supplied
   by the definition of `W`.
10. `Theta_R` is the anti-linear source involution. Slot exchange is the
    separate `tau_R`.

## 5. THE COMPLETE TRANSPORT DIAGRAM

The comparison is most clearly written in source-coordinate-free form.

```text
finite germ source coefficients (j,r)
    |  s_J(j), s_R(r)                                  [C0 source maps]
    v
linear and symmetric-bilocal insertions in the CTP exponent
    |  branch orientation epsilon; eta_CTP             [U1]
    |  branch <-> (c,delta) coordinates by T_CTP        [U1]
    v
Xi=L(j)-(1/2)Q(r)
    |  Z=(1-p)+p exp(Xi)
    |  W=-i hbar Log_0 Z
    v
D_J W, D_J^2 W, 2D_R W
    |  K_J=U_B, K_R=U_B(.)U_B^*                        [A4]
    |  K_R=Sym^2(K_J)
    v
physical linear and bilocal source tensors
    |  Gate-4/path-visible quotient
    |  cycle restriction K_J|ker(B^T)
    |  W3 adjoint finite corners i_N^*(.)i_N
    v
D_J Abar  compared with  (i/hbar)[2D_R W-Abar tensor Abar]
    |  Theta_J / Theta_R source-reality check
    v
Door-D condition-6 and U1 verdicts
```

The raw identity is imposed before retarded projection. The later ordered
`(delta,c)` extraction therefore does not own any factor in this comparison.

### 5.1 Linear source Jacobian

The ratified C0 presentation defines at
`STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md:475-508`:

```text
s_J(j)=sum_I j_I A^I.
```

It is linear, so its Jacobian is `s_J` itself and appears once. Field signature
V002 defines at `:358-375`:

```text
K_J=U_B.
```

V005 restricts the physical scalar source family to
`c in ker(B_N^T)` and defines `u_c=sum_e c_e u_e` at `:81-124,286-320`.
Therefore the current finite linear transport is exactly the restriction

```text
K_J,N^cyc=U_B restricted to ker(B_N^T),
K_J,N^cyc(c)=u_c.
```

No basis is selected. On the source image the inverse used in Q-300/Q-302 is
the inverse of this isometric restriction.

### 5.2 Bilocal source Jacobian

The C0 presentation defines:

```text
s_R(r)=(1/2)sum_(I,J)r_IJ A^I A^J.
```

The factor `1/2` is present once. V002 defines:

```text
K_R(R)=U_B R U_B^*.
```

On finite symmetric rank-one sources this is:

```text
K_R(j symtensor h)
  =K_J(j) symtensor K_J(h).
```

Thus `K_R=Sym^2(K_J)` on the dense finite core, and continuity gives the
trace-class extension. Restriction to cycles preserves the same square:

```text
K_R,N^cyc=Sym^2(K_J,N^cyc).
```

This is the exact joint-Jacobian condition required for connected subtraction.
It rules out one-source-read-through-unrelated-coordinates as an explanation
of the firings.

### 5.3 Chain-rule covariance of condition 6

Let `K_J` be any admitted isometric source transport and
`K_R=Sym^2(K_J)`. For the pulled-back physical germ:

```text
L_phys=L compose K_J^(-1),
b_phys=(K_R^(-1))^* b.
```

Then:

```text
b_phys=i hbar L_phys tensor L_phys

iff

b=i hbar L tensor L.
```

The direction chosen for writing `K_R` versus `K_R^(-1)` changes only which
side is called source or target; the displayed equivalence is invariant. No
Jacobian can change the coefficient because `K_R` is the symmetric square of
the same `K_J`.

```text
LINEAR_JACOBIAN_APPLIED_ONCE = PASS
BILOCAL_JACOBIAN_APPLIED_ONCE = PASS
JOINT_JACOBIAN_SYMMETRIC_SQUARE = PASS
JACOBIAN_GENERATES_COMPLEX_NORMALIZATION = false | TYPE-R |
  test: K_J and K_R act on carrier indices and preserve scalar coefficients
```

## 6. CTP METRIC, KELDYSH ROTATION, AND SOURCE REALITY

### 6.1 Metric

U1_008 defines at `:177-220`:

```text
eta_CTP=diag(+1,-1),
T_CTP^T eta_CTP T_CTP=[[0,1],[1,0]].
```

The A4 transport is branch diagonal:

```text
K_J=I_CTP tensor U_B.
```

Therefore:

```text
K_J eta_CTP=eta_CTP K_J,
K_R Sym^2(eta_CTP)=Sym^2(eta_CTP)K_R.
```

The metric can lower or raise the declared branch position and, in Keldysh
coordinates, exchange common and difference index positions. It is real,
invertible, and applied equally to the two sides of the tensor identity. It
cannot turn a nonzero tensor into zero or multiply one side by `i`.

### 6.2 Keldysh coordinate change

The sealed matrix is real:

```text
T_CTP=[[1,1/2],[1,-1/2]].
```

Because `U_B` acts on the non-branch label and `T_CTP` acts on the branch
label:

```text
K_J T_CTP=T_CTP K_J,
K_R Sym^2(T_CTP)=Sym^2(T_CTP)K_R.
```

Consequently the condition-6 residual transforms as a bilinear tensor. A
vanishing residual stays zero; a nonzero residual stays nonzero. The exact
finite difference/difference versus mixed-retarded classification remains a
later projection and adds no coefficient here.

### 6.3 Reality

U1_008 defines at `:244-264,322-347`:

```text
Theta_J: anti-linear branch exchange on J,
Theta_R: anti-linear branch exchange in each R slot,
tau_R:   separate slot exchange.
```

The branch-diagonal, real `U_B` intertwines these maps. Therefore a scalar
coefficient's conjugation parity is unchanged by `K_J`, `K_R`, `eta_CTP`, or
`T_CTP`. In particular, none can make `i hbar L tensor L` `Theta`-even.

```text
CTP_METRIC_CROSSING = PASS
KELDYSH_CROSSING = PASS
SOURCE_INVOLUTION_CROSSING = PASS
OMITTED_ARGUMENT_SWAP_IN_Q302 = false | TYPE-R |
  test: Theta_R is slotwise and tau_R is separate; symmetry makes a later
        swap coefficient-neutral
METRIC_OR_KELDYSH_I_FACTOR_EXISTS = false | TYPE-S |
  roots: U1_008 complete metric and coordinate definitions |
  exclusions: unratified alternative conventions |
  fences: audit only |
  query: imaginary entry or scalar phase in eta_CTP or T_CTP
```

## 7. QUOTIENT, W3 RESTRICTION, AND COMPARISON SITE

V005's scalar physical source space is the completion of all finite cycle
currents. The square-cycle witness is in that space because
`B_square^T c_square=0`. The quotient does not alter its coefficient tensor.

W3 requires finite restrictions to be adjoints of isometric inclusions:

```text
rho_G,N(G)(f,h)=G(i_N f,i_N h)
              =<i_N^* G i_N f,h>.
```

For the source maps:

```text
K_J,M i_NM=i_NM^phys K_J,N,
K_R,M Sym^2(i_NM)=Sym^2(i_NM^phys)K_R,N.
```

Hence restriction commutes with both the J-Hessian and the bilocal
derivative, and with their comparison. W3 cannot remove the Q-300 mismatch or
the Q-302 parity sign.

Endpoint-covariant transport is not scalarized by this audit. Where Q-302 and
Q-304 state the tensor identity on that retained family, the calculation is
equivariant and uses no frame member. The scalar cycle restriction remains an
independent complete subtest.

```text
QUOTIENT_CROSSING = PASS
W3_ADJOINT_RESTRICTION_CROSSING = PASS
CYCLE_MEMBER_OR_BASIS_SELECTED = false | TYPE-S |
  roots: complete ker(B_N^T) family |
  exclusions: c_square used only as a fixed universal-test witness |
  fences: no-selection |
  query: selected cycle basis or quotient representative
NAIVE_TRUNCATION_USED = false | TYPE-R |
  test: all displayed restrictions are adjoint corners
```

## 8. EVERY FACTOR OF 2, i, AND hbar

Start from the live chart:

```text
Xi=L-(1/2)Q,
q=p exp(Xi)/Z,
W=-i hbar Log_0 Z.
```

For linear directions `f,h` and a symmetric rank-one bilocal direction
`f symtensor h`, write `Q(f symtensor h)=b(f,h)`. Direct differentiation gives:

```text
D_J W[f] = -i hbar q L(f),

D_J Abar[f,h]
  =D_J^2 W[f,h]
  =-i hbar q(1-q)L(f)L(h),

D_R W[f symtensor h]
  =(-i hbar)q[-(1/2)b(f,h)]
  =(i hbar/2)q b(f,h),

2D_R W[f symtensor h]
  =i hbar q b(f,h),

Abar(f)Abar(h)
  =(-i hbar q)^2L(f)L(h)
  =-hbar^2q^2L(f)L(h),

G_b(f,h)
  =i hbar q b(f,h)+hbar^2q^2L(f)L(h),

(i/hbar)G_b(f,h)
  =-q b(f,h)+i hbar q^2L(f)L(h).
```

Subtracting yields (TA-1). Factor ownership is therefore:

| Factor | Owner | Count | Audit |
|---|---|---:|---|
| `1/2` | symmetric bilocal insertion in `Xi`/`s_R` | one | cancelled once by `2D_R` |
| `2` | definition of raw `G` | one | correct |
| `-i hbar` | definition of `W` | one | correct |
| `i/hbar` | condition 6 | one | correct |
| `i hbar` in required `b` | algebraic consequence of the preceding independent owners | one | not imported or duplicated |

```text
FACTOR_TWO_ACCOUNT = PASS
W_CONVENTION_FACTOR_ACCOUNT = PASS
RAW_IDENTITY_FACTOR_ACCOUNT = PASS
DOUBLE_SUPPLIED_I_FOUND = false | TYPE-R |
  test: the explicit coefficient calculation above has one owner per factor
OMITTED_HBAR_FOUND = false | TYPE-R |
  test: dimensions and coefficients match in every displayed line
```

## 9. RE-DERIVATION OF THE FIRINGS

### 9.1 Q-300

Q-300 used the admitted cycle `c_square` with:

```text
L(c_square)=0,
b_delta(c_square,c_square)!=0.
```

Equation (TA-1) gives:

```text
Residual_Q300
  =q b_delta(c_square,c_square)
  !=0.
```

All carrier maps preserve the zero/nonzero distinction. The Q-300
same-correlator firing survives.

```text
Q300_FAILURE_WAS_TRANSPORT_ARTIFACT = false | TYPE-R |
  test: (TA-1) on the admitted square cycle after every certified crossing
```

### 9.2 Q-302

Amendment 1 set:

```text
b_odd=i hbar L tensor L.
```

Equation (TA-1) vanishes identically, so condition 6 passes. Under the sealed
anti-linear source involution:

```text
b_odd,(-n)(Theta_J f,Theta_J h)
  =+i hbar conjugate(L_n(f)L_n(h)),

conjugate(b_odd,n(f,h))
  =-i hbar conjugate(L_n(f)L_n(h)).
```

The metric, Keldysh matrix, source intertwiners, quotient, and W3 restrictions
are all real/intertwining and do not change that sign. The Q-302 source-reality
firing survives.

```text
Q302_FAILURE_WAS_TRANSPORT_ARTIFACT = false | TYPE-R |
  test: exact anti-linear coefficient comparison after every certified crossing
```

### 9.3 Q-304, the later-bearing ruling

Q-304 set:

```text
b_even=hbar L tensor L.
```

Substitution in (TA-1) gives independently:

```text
Residual_Q304
  =hbar q(1-i)L tensor L.
```

This matches the registered Q-304 residual exactly. The proposal repairs
source parity but not the unchanged same-correlator coefficient. The phrase
"W supplies the i" is insufficient: W's `-i hbar` is already present in both
derivative routes before condition 6 supplies its separate `i/hbar`.

```text
Q304_RESIDUAL_REPRODUCED_INDEPENDENTLY = PASS
Q304_RESIDUAL_REMOVED_BY_RATIFIED_TRANSPORT = false | TYPE-R |
  test: K_J, K_R, eta_CTP, T_CTP, quotient, and restrictions are coefficient-free
```

## 10. PER-CROSSING AUDIT TABLE

| Crossing | Sealed map | Verification | Effect on firings |
|---|---|---|---|
| linear source insertion | `s_J(j)=sum j_I A^I` | linear Jacobian once | none |
| bilocal insertion | `s_R(r)=(1/2)sum r_IJ A^I A^J` | symmetric Jacobian and factor once | supplies the `2D_R` cancellation |
| A4 linear transport | `K_J=U_B`, restricted to cycles in V005 | isometric, real, branch diagonal | coefficient unchanged |
| A4 bilocal transport | `K_R=U_B(.)U_B^*` | `Sym^2(K_J)` | tensor equality covariant |
| CTP metric | `eta=diag(+1,-1)` | commutes with A4; real and invertible | no complex phase |
| Keldysh transform | real `T_CTP` | commutes with A4 | block relabeling only |
| quotient | Gate-4/path-visible quotient | `c_square` admitted; tensor descends | Q-300 witness retained |
| W3 | adjoints of isometric inclusions | linear and bilocal squares commute | finite firings retained |
| `W` | `-i hbar Log_0 Z` | one factor | exact derivatives above |
| raw condition 6 | `(i/hbar)G` | one independent factor | forces `b=i hbar L tensor L` |
| U1 source reality | `Theta_J`, `Theta_R` | anti-linear and slotwise | detects Amendment-1 sign |

`UNLISTED_TRANSPORT_CROSSING_FOUND = false | TYPE-S | roots: all source, U1, A4/A6, quotient, W3, and raw-map interfaces listed in Section 2; exclusions: post-Door-D inverse/retarded consumers; fences: audit boundary; query: any map between germ source definition and condition-6/U1 comparison`

## 11. FINAL TYPED LEDGER

```text
DOOR_D_TRANSPORT_AUDIT_VERDICT = TEST-CLEAN

LINEAR_SOURCE_JACOBIAN = CERTIFIED
BILOCAL_SOURCE_JACOBIAN = CERTIFIED
JOINT_JACOBIAN_SQUARE = CERTIFIED
CTP_METRIC_CONTRACTION = CERTIFIED
KELDYSH_COORDINATE_CHANGE = CERTIFIED
QUOTIENT_PULLBACK = CERTIFIED
W3_ADJOINT_RESTRICTIONS = CERTIFIED
FACTOR_OWNERSHIP = CERTIFIED

Q300_IDENTITY_FIRING_SURVIVES = true
Q302_U1_SIGN_FIRING_SURVIVES = true
Q304_NORMALIZATION_RESIDUAL_SURVIVES = true

TEST_DEFECT_FOUND = false | TYPE-S |
  roots: complete transport diagram and per-crossing table |
  exclusions: no alternative unratified map |
  fences: no repair |
  query: false Door-D firing caused by plumbing

RATIFIED_EVEN_TO_ODD_NORMALIZATION_MAP_EXISTS = false | TYPE-S |
  roots: C0, U1, source germ, field signature, raw-map spec |
  exclusions: candidate repairs and unregistered conventions |
  fences: audit only |
  query: a separate complex source-to-output normalization map

CURRENT_DIRECT_IDENTIFICATION_COMPATIBLE_WITH_BOTH_SOURCE_REALITY_AND_CONDITION_6
  = false | TYPE-R |
  test: Q-302 sign equation plus Q-304 residual, both preserved by transport

DOOR_D_DISPOSITION_SELECTED = false | TYPE-C |
  constraint: principal act; this lane audits and does not repair

REPAIR_OR_RESPECIFICATION_EXECUTED = false | TYPE-S |
  roots: this artifact |
  exclusions: none |
  fences: relay 387 diagnosis-only scope |
  query: installed source map, pairing, normalization, involution, or Door-D change
```

The narrow conclusion is exact: this was a legitimate candidate for a
self-imposed bookkeeping failure, but the candidate is refuted. Door D's
transport is clean. The remaining mismatch belongs to the source/output
architecture itself, with the principal's disposition still required.

## 12. CUSTODY PRE-SEAL

The artifact is written only in the cleanroom, then sealed with a
`.seal.sha256` sidecar, verified locally, and mirrored with the sidecar to:

1. `/Users/bgm/MB Work/alpha-program-archive/cleanroom_output/`
2. `/Users/bgm/MB Work/alpha-program-archive/workspace/`

No register, tracker, plan, git, commit, push, gate, or deployment act belongs
to this lane.
