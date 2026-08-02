# Stage 8 Task 4a P5 Maximal Chain and Accounting Cross-Verification Determination V001

Date: 2026-08-02  
Lane: CODEX LANE 1  
Task: 4a, relay 369  
Register head at start: Q-285  
Status: DEFECT IN ACCOUNTING IDENTITY; FINITE CHAIN CONFIRMED

```text
alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead verdict

**DEFECT. Q-284'S FINITE DERIVATIVES, FULL Q-279 RESTRICTION, P-CLEAN
FINITE RETARDED IMAGE, AND RAW-G STOP ALL RECOMPUTE. ITS FOUR-ROW TABLE IS
NOT, HOWEVER, THE FOUR-ARROW ACCOUNTING PACKAGE Q-282 REQUIRED.**

Q-282 defines the required chain explicitly as

```text
F_chain = F_domain compose F_boundary compose F_contour compose F_measure
```

and requires one `DEP_ACCOUNT_k` for each of those four operations
(`STAGE8_TASK4A_FOUR_DEPENDENCE_PRESERVATION_CERTIFICATES_FAMILY_LEVEL_DETERMINATION_V001.md:508-582`).
Q-284 instead accounts for:

```text
1  source differentiation / proposed raw-G lift;
2  physical inversion plus a finite quotient reciprocal diagnostic;
3  Keldysh rotation / ordered retarded projection;
4  induced response.
```

Those are useful response-chain rows, but they are different arrows. Measure,
contour boundary value, joint boundary/contact reduction, and unbounded-domain
closure appear only as unbuilt fields distributed across the response rows;
none receives Q-282's required carrier, `p`-submodule, kernel, image, sector
transfer, tail action, restriction square, provenance, and target-independence
account. The statement at Q-284:601 that no operation is omitted is therefore
refuted.

A second omission is internal to the response chain. The live raw-map
specification requires stationary 2PI reduction and, when applicable, the
physical Schur complement

```text
D^2 Gamma_1PI
  = Gamma_(Abar Abar)
    - Gamma_(Abar G) Gamma_(G G)^(-1) Gamma_(G Abar).
```

Q-284 names stationary Schur data as missing but gives that operation no
kernel/applicability, image, sector-transfer, restriction, tail, or `p` account.
Q-285 then adds a further current obligation at the raw-`G` boundary:
`DEP_ACCOUNT_class_formation`, including the raw-`G` class, topology, completion
act, and `image intersect Tail_R`. Q-284 could not have consumed this later
ruling, but the table cannot now serve as the load-bearing current account
without it.

The lawful inheritance split is:

```text
Q284_DERIVATIVE_TENSOR = CONFIRMED | TYPE-P
Q284_FULL_Q279_RESTRICTION = CONFIRMED | TYPE-P
Q284_P_CLEAN_BUILT_RETARDED_IMAGE = CONFIRMED | TYPE-P
Q284_RAW_G_STOP = CONFIRMED | TYPE-P

Q284_RESPONSE_CHAIN_PARTIAL_ACCOUNT = CONFIRMED_WITH_NOTES | TYPE-P

Q284_ACCOUNTING_TABLE_IS_Q282_REQUIRED_FOUR_ARROW_PACKAGE = false | TYPE-R |
  test: Q-282 arrows are measure/contour/boundary/domain; Q-284 rows are
        differentiation/inversion/Keldysh/induced-response

Q284_NO_OPERATION_OMITTED = false | TYPE-R |
  test: the four Q-282 field operations and stationary Schur reduction lack
        per-operation accounts

FOUR_ARROW_DEPENDENCE_ACCOUNTING_PACKAGE_ASSEMBLED_AS_Q282_DEFINED = false |
  TYPE-U |
  would-build: DEP_ACCOUNT_measure, DEP_ACCOUNT_contour,
               DEP_ACCOUNT_boundary, and DEP_ACCOUNT_domain on the physical
               P5/P6 class and restrictions

CURRENT_TAIL_ACCOUNT_COMPLETE_AFTER_Q285 = false | TYPE-U |
  would-build: the four Q-282 accounts plus DEP_ACCOUNT_stationary_schur and
               DEP_ACCOUNT_class_formation

VERDICT = DEFECT
```

The defect does **not** provide a path by which `p` reaches the built finite
retarded image. It invalidates the completeness/accounting claim, not the exact
finite calculation.

## 1. Scope, authorities, and method

### 1.1 Roots entered

| Authority | SHA-256 | Use |
|---|---|---|
| `alpha_supervision/LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | custody, typing, act-based fences |
| `alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md` | `32d3b0718b5437d836e10064558ddaa62d3736077fed51349c491f3a1fec177e` | ruling set through Q-285 at start |
| `workspace/STAGE8_TASK4A_P5_MAXIMAL_TRANSPORT_CHAIN_AND_DEPENDENCE_ACCOUNTING_PACKAGE_V001.md` | `2fc227d0707f2720fece37bc90e966783887f79989412d127455409c05430d22` | object under review |
| `workspace/STAGE8_TASK4A_P2_PHYSICAL_SOURCE_TOPOLOGY_AND_DIFFERENTIAL_CALCULUS_CONSTRUCTION_V002.md` | `40b2af34443e051fffdc7bf2ec7025c811a98c501a82d19164596ee6f37f00c1` | source topology, corrected sign, restriction naturality, `Tail_src=0` |
| `workspace/STAGE8_TASK4A_P4_PHYSICAL_LOG_GERM_ON_P2_CALCULUS_CONSTRUCTION_V001.md` | `b4c77ea948a02f3736fc824976f9ebd6381deff35f5c339a646739ea159725c5` | `W=-i hbar Log_0 Z`, derivative tower, raw-`G` boundary |
| `workspace/STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md` | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | Q-279 complete finite restriction oracle |
| `workspace/STAGE8_TASK4A_FINITE_HESSIAN_TO_DELTAPHI_TRANSPORT_MAP_CONSTRUCTION_AND_P_CH_TRACE_V001.md` | `70185aa842bc500724719c65bd66b5f07005e2214b97be0d35e07fd029d5c68c` | Q-243 exact CTP rotation and finite/physical type boundary |
| `workspace/STAGE8_TASK4A_ANCHORED_ORIGIN_TO_PHYSICAL_BACKGROUND_MAP_IDENTIFICATION_DETERMINATION_V001.md` | `f893d210191551bd8b6af060f85a73510f8119171c8709c46e925a6708314ed2` | Q-281 seed, raw-`G` maps, and stationary lift fiber |
| `workspace/STAGE8_TASK4A_MINIMAL_CONSUMPTION_AUDIT_AND_CORE_REDUCTION_DETERMINATION_V001.md` | `9ede28633b49081e4c6b1461663d14653b2b1017900c6a8c3e0076cc53545144` | Q-280 four-field/P5/P6/background/consumer dependency split |
| `workspace/STAGE8_TASK4A_FOUR_DEPENDENCE_PRESERVATION_CERTIFICATES_FAMILY_LEVEL_DETERMINATION_V001.md` | `78ec90ce3274c706622fb96cd639ae3fd7d65a101aa3287a0c311618275433b5` | Q-282 exact four-arrow definition and account schema |
| `workspace/STAGE8_TASK4A_P_LOC_CANDIDATE_W_BATTERY_AND_CONSUMPTION_TYPING_DETERMINATION_V001.md` | `5582cb146126f0bddb7a34c6b343ff5bb66ea538433b96290ab6db691b923964` | Q-283 consumer fork |
| `workspace/STAGE8_TASK4A_W_GEN_TAIL_CREATION_IMAGE_THEOREM_DETERMINATION_V001.md` | `5f341414cda1001369fb97484729d9bef6475e9e8e21d12c41a2f2b3af433c44` | Q-285 weak-star creator and class-formation account |
| `workspace/STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md` | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | raw `G`, inverse, stationary Schur, and retarded signatures |

### 1.2 Exclusions and search scope

Entered roots:

```text
/Users/bgm/MB Work/alpha_supervision/
/Users/bgm/MB Work/alpha-program-archive/workspace/
```

Excluded: `a32_holdout/custodian_private/`; all value, root, coupling, rank,
scale, and response evaluations; all measured comparisons; construction of any
missing physical map. No git command was run.

Queries were exact or word-boundaried for `W`, `Log_0`, `D^2`, `Q_N`,
`kappa_eta`, `T_CTP`, `kernel`, `image`, `sector_transfer`, `restriction`,
`Tail_R`, `weak-star`, `weak-*`, `bidual`, `topology`, `limit`, `completion`,
`measure`, `contour`, `boundary`, `domain`, `stationary`, `Schur`, `raw G`,
`Pi_R,ind`, `p_loc`, and `would-build`.

### 1.3 Independent method

The derivative tensor was recomputed directly from the scalar source family,
without copying Q-284's table. The CTP block result was recomputed by exact
matrix multiplication. Kernels and images were then derived from the resulting
rank-one forms. The account identity was checked by comparing Q-284's row
domains against Q-282's defining equation and schema, not by name matching.

## 2. X1: independent derivative-tensor recomputation

At a finite probe write

```text
Z_0 := 1-p+p u,
u   := exp[-Q_N(R)/2],
omega := p u/Z_0,
kappa := omega(1-omega)
       = p(1-p)u/(1-p+p u)^2.
```

For a source increment `(j_c,j_delta,r)`, the finite exponent has derivative

```text
lambda(j_c,j_delta,r)
  = i n ell_N(j_delta) - (1/2)Q_N(r),

lambda(j_c,0,0)=0.
```

Since the exponent is linear, direct quotient differentiation gives

```text
D Log Z[h] = omega lambda(h),
D omega[h] = kappa lambda(h),
D^2 Log Z[h_1,h_2]
  = kappa lambda(h_1)lambda(h_2).
```

With Q-276's response convention `W=-i hbar Log Z`:

```text
D W[h] = -i hbar omega lambda(h),
D^2 W[h_1,h_2]
  = -i hbar kappa lambda(h_1)lambda(h_2).
```

Using `n^2=1`, expansion by source block gives independently:

| Block | Recomputed exact form |
|---|---|
| `D_(J_c)W` | `0` |
| `D_(J_delta)W` | `hbar n omega ell_N` |
| `D_R W` | `(i hbar/2)omega Q_N` |
| `D^2_(c,c)W`, `D^2_(c,delta)W`, `D^2_(delta,c)W` | `0` |
| `D^2_(delta,delta)W` | `i hbar kappa ell_N tensor ell_N` |
| `D^2_(delta,R)W` and transpose | `-(hbar n/2)kappa ell_N tensor Q_N` and transpose |
| `D^2_(R,R)W` | `-(i hbar/4)kappa Q_N tensor Q_N` |

This matches Q-284:207-235 and 290-303 exactly. In particular, Q-276's
minus sign in `D^2 Log Z` on a phase direction is present because
`(i n)^2=-1`; multiplying by `-i hbar` gives the displayed positive
`i hbar kappa` W-Hessian. No sign is lost.

The conditional linear-source shadow also recomputes:

```text
G_JJ,src := (hbar/i)D_J^2W
          = hbar^2 kappa ell_N tensor ell_N
```

in the pure difference/difference block. Its coefficient is nonzero for the
declared real probe and `0<p<1`; its finite null directions are every common
source direction plus `ker(ell_N)` in the difference sector.

```text
X1_DERIVATIVE_TENSOR_MATCHES = PASS | TYPE-P |
  premises: sealed finite source family and Q-276 W convention

X1_Q276_SIGN_DEFECT_IN_Q284 = false | TYPE-R |
  test: direct differentiation carries the corrected sign through every block
```

## 3. X2: full Q-279 restriction recomputation

The finite zero extension `iota_NM` appends identity holonomies and zero
bilocal components. Therefore

```text
ell_M(iota_NM j)=ell_N(j),
Q_M(iota_NM R)=Q_N(R),
u_M=u_N,
omega_M=omega_N,
kappa_M=kappa_N.
```

Every first and second derivative in Section 2 consequently restricts
componentwise. Equal linear histories give

```text
Z_N[J_delta=0,R]=1-p+p exp[-Q_N(R)/2],
```

and the full zero-source surface gives unity. Setting `R=0` gives
`omega=p` and `kappa=p(1-p)`, recovering Q-243.

For the J/J branch Hessian, use

```text
M_DD = [[1,-1],[-1,1]],
T_CTP = [[1,1/2],[1,-1/2]].
```

Independent exact multiplication gives

```text
T_CTP^T M_DD T_CTP = [[0,0],[0,1]].
```

Thus the `(delta,c)` entry is zero for every finite `N`, character orientation,
rank class, and admitted probe. The `p`-carrying `kappa` coefficient remains in
the DD noise block and the J-delta/R and R/R probe blocks. It is not divided
out or normalized away.

```text
X2_Q279_FULL_TUPLE_MATCHES = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

X2_P_ENTERS_FINITE_ORDERED_RETARDED_BLOCK = false | TYPE-R |
  test: exact transformed matrix has zero (delta,c) entry before its scalar
        coefficient acts
```

## 4. X3: row-by-row accounting audit

### 4.1 Q-284 Row 1: differentiation / proposed raw-G lift

The built image and finite null directions are correct. Differentiation on the
connected local germ has constants as its functional kernel; the finite CJJ
bilinear has `J_c direct-sum ker(ell_N)` as null directions. P2 naturality gives
the source restriction square. P2's topology is the ratified sum norm on
`ell^1 direct-sum ell^1 direct-sum trace-class`; weak-star, bidual,
distributional, and weighted completions are outside P2
(P2 V002:248-267). The built operation therefore performs no hidden weak-star
completion.

The physical raw-`G` lift is absent. Consequently its carrier, class, kernel,
image, topology, restriction square, and `Tail_R` action are not supplied by
Row 1. Q-284 labels that physical part `NO_VERDICT`, correctly. Under Q-285 the
row now additionally requires `DEP_ACCOUNT_class_formation`.

### 4.2 Q-284 Row 2: inversion

The source-shadow bilinear is rank one on the difference space. It is singular
on the full finite carrier and nondegenerate only on
`E_(J_delta),N/ker(ell_N)`. Its algebraic reciprocal remains DD and carries
reciprocal `kappa` dependence. Q-284 correctly refuses to identify this
diagnostic with the physical convolution inverse.

No physical inverse, restriction square, or `Tail_R` action exists. There is no
limit or completion in the finite reciprocal diagnostic. This row is correct
within its declared partial scope.

It is not a complete account of the physical second arrow. The raw-map
specification:724-755 separately requires stationary 2PI reduction and a Schur
complement. Naming `stationary Schur data` under Row 3's missing fields does not
account for that nonlinear operation's domain, applicability, image, sector
transfer, restrictions, tail action, or `p` action.

### 4.3 Q-284 Row 3: finite Keldysh extraction

`T_CTP` is invertible, so congruence has zero kernel. On the transformed
carrier, ordered projection has kernel `{H:H_(delta,c)=0}` and image the
declared `(delta,c)` block space. Every built J/J two-point tensor is DD and is
therefore killed. J-delta/R and R/R forms have a bilocal-source leg and do not
enter this J/J block projection at all. No built sector-transfer map converts
them to a common-linear-source leg.

The Q-243/Q-279 finite restriction square passes. The physical
`RetHess_phys` class and restrictions are absent, so `Tail_R_action=NO_VERDICT`
is correct. No weak-star, bidual, boundary-value, or domain-closure act is
hidden in the finite matrix congruence or component projection.

### 4.4 Q-284 Row 4: induced response

The row is honestly interface-only. `Pi_R,ind`, its restrictions, tail action,
kernel, image, sector transfer, and `p` action are uninstantiated. It neither
adds nor deletes a result.

### 4.5 The identity failure

The four rows above are not Q-282's four `F_k`. Q-282:280-506 treats, in order:

```text
F_measure,
F_contour,
F_boundary,
F_domain.
```

Q-282:508-582 then defines their composition and requires a separate
`DEP_ACCOUNT_k` for each. Q-284's table supplies none of those four instances.
Its `missing_fields` cells are not substitutes for per-operation accounts.

```text
X3_Q284_RESPONSE_ROWS_INTERNALLY_CORRECT_ON_BUILT_SCOPE = true | TYPE-P

X3_Q282_REQUIRED_ARROW_IDENTITY_MATCHES_Q284_ROWS = false | TYPE-R |
  test: exact domain/codomain and operation lists are pairwise different

X3_Q282_MEASURE_ACCOUNT_EXISTS = false | TYPE-U |
  would-build: the instantiated physical measure operation and full Q-282 schema
X3_Q282_CONTOUR_ACCOUNT_EXISTS = false | TYPE-U |
  would-build: the named-topology boundary-value operation and full Q-282 schema
X3_Q282_BOUNDARY_ACCOUNT_EXISTS = false | TYPE-U |
  would-build: joint boundary/contact/null-reduction operation and full schema
X3_Q282_DOMAIN_ACCOUNT_EXISTS = false | TYPE-U |
  would-build: physical closure/extension operation and full Q-282 schema

X3_STATIONARY_SCHUR_ACCOUNT_EXISTS = false | TYPE-U |
  would-build: physical 2PI stationary reduction, Schur blocks, restrictions,
               topology, tail action, and p account

X3_CLASS_FORMATION_ACCOUNT_EXISTS = false | TYPE-U |
  would-build: Q-285 RawGLiftPackage/raw_G_class topology and
               image-intersect-Tail_R certificate
```

## 5. X4: adversarial `p`-cleanliness attack

Every candidate built path was composed explicitly:

1. `D_J^2W -> G_JJ,src` multiplies the DD tensor by a scalar and does not mix
   CTP sectors.
2. Passing to the one-dimensional quotient and taking its reciprocal changes
   `kappa` to reciprocal `kappa` but remains DD.
3. The exact Keldysh congruence sends branch-difference rank one to DD.
4. Ordered projection kills DD.
5. The J-delta/R and R/R tensors cannot enter the J/J projection without an
   additional source-field/bilocal intertwiner. None is built.
6. The `p`-carrying one-point covector could enter the connected subtraction
   `Abar tensor Abar` only after `i_A`, `i_G`, and `Conn` place both terms in one
   physical bilocal carrier. That is the raw-`G` lift and is unbuilt.

The topology attack gives the same result. P2 is norm/trace-class; P4 uses
bounded Frechet derivatives; the finite reciprocal is finite-dimensional; and
the CTP map is a finite matrix. No built operation takes a weak-star limit,
enters a bidual, forms a nonexact completed quotient, or chooses a closed
extension. Q-285's creator is therefore not hidden in Q-284's built subchain.

```text
BUILT_WEAK_STAR_OR_BIDUAL_COMPLETION_FOUND = false | TYPE-S |
  roots: Q-284, P2 V002, P4, Q-243, Q-279 |
  exclusions: unbuilt physical raw-G/P5/P6 operations |
  fences: none bearing on structural topology audit |
  query: word-boundaried weak-star, weak-*, bidual, topology, limit,
         completion, closure, and every built map signature

X4_P_CARRYING_BUILT_PATH_TO_RETARDED_IMAGE_EXISTS = false | TYPE-R |
  test: every built composition either remains DD or lies outside the J/J
        retarded-projection domain

X4_RETARDED_IMAGE_P_CLEAN_ON_ALL_BUILT_CONTENT = true | TYPE-P
```

This confirmation is finite/source-level only. It does not decide whether the
unbuilt raw-`G` lift, Schur reduction, physical completion, tail, background,
induced response, or consumer carries `p`.

## 6. X5: stop point and residue census

### 6.1 Stop point

Q-281:358-408 types the built derivatives in `E_J^*` and `E_R^*` and lists the
absent maps:

```text
i_A, i_G, Conn, Leg, Stat.
```

The physical definition

```text
G = 2D_R W - Abar tensor Abar
```

cannot be formed until `i_A`, `i_G`, and `Conn` put both terms in the same
physical bilocal carrier. The linear-source shadow does not bypass this type
boundary. The first physical stop is therefore exactly the raw-`G` lift.

```text
X5_CHAIN_STOPS_AT_RAW_G_LIFT = true | TYPE-P |
  premises: Q-281 and the raw-map domain signature
```

### 6.2 Six-object residue

Q-284's six categories cover the outstanding physical path at coarse grain:

| Q-284 category | Cross-verified contents |
|---|---|
| raw-`G` lift | `i_A`, `i_G`, `Conn`, physical quotient/pairing, raw-`G` class, and Q-285 class-formation topology |
| physical inverse package | convolution measure/delta, prescription, contacts, boundary and domains |
| P5/P6 transport | physical classes, restrictions, extraction and commuting squares |
| background lift | `Leg`, `Stat`, `STAT_BG_LIFT_FIBER([A])`, stationary 2PI solve |
| induced response | complete induced operator, exact second variation, `Pi_R,ind`, subtraction and `Tail_ind` |
| consumption | target-independent `p_loc`/output signature and the Q-283 F/W_gen tail action |

No seventh coarse category is forced by Q-280, Q-281, Q-283, or Q-285. But the
categories are not an operation-level accounting census. In particular, the
four Q-282 fields are distributed across the first three categories, stationary
Schur reduction crosses the inverse/background categories, and class formation
crosses raw `G` and P5/P6. Each still requires its own account.

```text
X5_SIX_COARSE_RESIDUE_CATEGORIES_COMPLETE = true | TYPE-P |
  premises: Q-280, Q-281, Q-283, Q-285

X5_SIX_CATEGORIES_DISCHARGE_OPERATION_LEVEL_ACCOUNTING = false | TYPE-R |
  test: Q-282 requires four per-field accounts and Q-285 requires a
        class-formation image account
```

## 7. Inheritance and required next action

The following Q-284 results remain load-bearing:

```text
SOURCE_DERIVATIVE_TENSOR_BUILT
LINEAR_SOURCE_CONNECTED_SHADOW_BUILT
FINITE_SHADOW_FULL_CARRIER_INVERSE_EXISTS = false | TYPE-R
FINITE_SHADOW_DD_QUOTIENT_RECIPROCAL_EXISTS
FINITE_ORDERED_RETARDED_IMAGE_P_CLEAN
Q279_ENTIRE_PATTERN_REPRODUCED_ON_BUILT_RESTRICTION
P5_MAXIMAL_PARTIAL_RECEIPT_BUILT
P5_PHYSICAL_CHAIN_BUILT = false | TYPE-U
```

The following claims do not survive at their stated strength:

```text
FOUR_ARROW_DEPENDENCE_ACCOUNTING_PACKAGE_ASSEMBLED = true
No operation is omitted.
Q-282's corrected object exists.
```

The existing four-row table should be retained as
`P5_RESPONSE_CHAIN_PARTIAL_DEPENDENCE_ACCOUNT`. The would-build needed before
it can serve as the current load-bearing account is:

```text
DEP_ACCOUNT_measure
DEP_ACCOUNT_contour
DEP_ACCOUNT_boundary
DEP_ACCOUNT_domain
DEP_ACCOUNT_stationary_schur
DEP_ACCOUNT_class_formation
```

This artifact reports the defect and does not repair Q-284 or construct any of
those operations.

## 8. Final typed ledger

```text
VERDICT = DEFECT

X1_DERIVATIVE_TENSOR_MATCHES = PASS | TYPE-P
X1_Q276_SIGN_DEFECT_IN_Q284 = false | TYPE-R
X2_Q279_FULL_TUPLE_MATCHES = PASS | TYPE-P
X2_P_ENTERS_FINITE_ORDERED_RETARDED_BLOCK = false | TYPE-R

X3_Q284_RESPONSE_ROWS_INTERNALLY_CORRECT_ON_BUILT_SCOPE = true | TYPE-P
X3_Q282_REQUIRED_ARROW_IDENTITY_MATCHES_Q284_ROWS = false | TYPE-R
X3_Q282_MEASURE_ACCOUNT_EXISTS = false | TYPE-U
X3_Q282_CONTOUR_ACCOUNT_EXISTS = false | TYPE-U
X3_Q282_BOUNDARY_ACCOUNT_EXISTS = false | TYPE-U
X3_Q282_DOMAIN_ACCOUNT_EXISTS = false | TYPE-U
X3_STATIONARY_SCHUR_ACCOUNT_EXISTS = false | TYPE-U
X3_CLASS_FORMATION_ACCOUNT_EXISTS = false | TYPE-U

X4_P_CARRYING_BUILT_PATH_TO_RETARDED_IMAGE_EXISTS = false | TYPE-R
X4_RETARDED_IMAGE_P_CLEAN_ON_ALL_BUILT_CONTENT = true | TYPE-P

X5_CHAIN_STOPS_AT_RAW_G_LIFT = true | TYPE-P
X5_SIX_COARSE_RESIDUE_CATEGORIES_COMPLETE = true | TYPE-P
X5_SIX_CATEGORIES_DISCHARGE_OPERATION_LEVEL_ACCOUNTING = false | TYPE-R

Q284_ACCOUNTING_TABLE_IS_Q282_REQUIRED_FOUR_ARROW_PACKAGE = false | TYPE-R
Q284_NO_OPERATION_OMITTED = false | TYPE-R
FOUR_ARROW_DEPENDENCE_ACCOUNTING_PACKAGE_ASSEMBLED_AS_Q282_DEFINED = false |
  TYPE-U
CURRENT_TAIL_ACCOUNT_COMPLETE_AFTER_Q285 = false | TYPE-U

PHYSICAL_RETARDED_IMAGE_P_CLEAN = NO_VERDICT |
  prerequisite: raw-G lift, physical inverse, stationary reduction,
                RetHess class/restrictions, and their tail accounts
PHYSICAL_W_GEN_NONEMPTY = NO_VERDICT |
  prerequisite: a physically admitted creator and generated tail action

FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S |
  roots: relay 369 and LOCKED_PROCESS C19 |
  exclusions: barred value/evaluation acts only |
  fences: no structural proof fence applied |
  query: "Did any standing act-based fence prevent the recomputation or
          accounting counterexample?"
MACHINERY_APPEAL = NOT_TRIGGERED

REGISTER_HEAD_AT_START = Q-285
REGISTER_HEAD_AT_SEND_TIME = Q-285
LATER_BEARING_RULING_CONSUMED = false | TYPE-S |
  roots: QUESTIONS_SETTLED_REGISTER_V001.md through Q-285 |
  exclusions: no unregistered in-flight relay result assumed |
  fences: none |
  query: "Did a registered ruling later than Q-285 bear on the P5 chain or
          accounting identity before sealing?"

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

Custody: seal this artifact, verify its sidecar, mirror artifact and sidecar to
`/Users/bgm/MB Work/alpha-program-archive/workspace/`, report hashes and exact
paths, and stop. No register, git, commit, push, gate, or deploy action is
performed by this lane.
