# Stage 8 Task 4a source-to-output normalization N uniqueness, install, and Door-D re-execution V001

Date: 2026-08-02  
Task: PASTE 388 / Task 4a  
Lane: CODEX LANE 2  
Status: **UNIQUENESS PROVED ON THE ACTIVE IMAGE; INSTALLED; FULL DOOR D PASSES**

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013,
                   DoR-014 as amended (2), DoR-015, C38

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead theorem and execution verdict

The two requires force the normalization uniquely **on the exact domain C38
names**: the generated even source image consumed by Door D.

```text
N_n(lambda b_n^even)=i lambda b_n^even,
b_n^even=hbar L_n tensor L_n.                        (N-1)
```

There is no residual phase or map family on this domain:

* the same-correlator identity fixes the complete complex coefficient to
  `i` on every nonzero open-path direction;
* U1 reality fixes the even-to-odd anti-intertwining law;
* cycles contribute only the zero input, which linearity sends to zero;
* quotient and W3 naturality propagate the generator through every finite
  restriction.

The counterexample hunt matters: at each fixed stage the two requires leave
an algebraic complement untested if the domain is silently enlarged to the
complete bilocal dual. Whether W3 naturality fixes a unique global extension
on that larger space is `NO_VERDICT`. No such extension is needed, installed,
or claimed.

With the unique map installed in source germ v007, the full Door-D vector is:

```text
(bounded, cycles, endpoint-covariant open paths, U1 reality)
  = (PASS,PASS,PASS,PASS).
```

The freeze lifts. The physical lift runs through the bounded connected raw
bilocal. It then stops at the separately known physical inverse/Schur and
completed-domain package; no inverse or retarded instance is manufactured.

## 1. Preflight, custody, and roots

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = true |
  object: C38's declared normalization problem and generated source image
IS_THE_VERSION_CURRENT = true |
  register: Q-305 at construction start
ARE_INPUTS_PRESENT = true |
  inputs: Q-305 factor theorem, Q-303 parity table, Amendment-2 even pairing,
          U1 involution, W3, physical quotient, Door-D suite
```

### 1.2 Roots entered

1. `/Users/bgm/MB Work/alpha_supervision/LOCKED_PROCESS.md`
2. `/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md`
3. `/Users/bgm/MB Work/alpha_supervision/TASK_LIST_HERE_TO_ALPHA_2026-08-01_V002.md`
4. `STAGE8_TASK4A_DOOR_D_TRANSPORT_JACOBIAN_CTP_METRIC_AND_FACTOR_AUDIT_V001.md`
5. `STAGE8_TASK4A_RATIFIED_BILOCAL_INVOLUTION_REALITY_LAW_DETERMINATION_V001.md`
6. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V006.md`
7. `STAGE8_TASK4A_DOR014_AMENDMENT2_EVEN_PAIRING_FULL_DOOR_D_REEXECUTION_V001.md`
8. `STAGE8_CTP_PHYS_INPUT_PACKAGE_U1_DOR008_ASSEMBLY_DETERMINATION_V001.md`
9. `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md`
10. `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md`
11. `STAGE8_TASK4A_FINITE_HESSIAN_TO_DELTAPHI_TRANSPORT_MAP_CONSTRUCTION_AND_P_CH_TRACE_V001.md`
12. `STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md`

All unqualified Stage-8 paths are rooted at the current cleanroom.

### 1.3 Exclusions

```text
a32_holdout/custodian_private/               NOT ENTERED
unconsumed bilocal complement                 NOT NORMALIZED
physical inverse or retarded operator         NOT INSTANTIATED
rank, anchor, torsor, cycle, or background   NOT SELECTED
alpha, kappa, coupling, scale, or root        NOT COMPUTED
measured-constant comparison                  NOT PERFORMED
register, plan, tracker, git, commit, push    NOT TOUCHED
```

### 1.4 Bearing symbol distinctions

1. `N` is the new normalization map. It is not the finite-stage index `N`.
2. `R` is the bilocal source, not the retarded block.
3. `b_even` is the exponent/source tensor; `N(b_even)` is the raw-output
   coefficient.
4. `Theta_R` is slotwise source involution; `tau_R` is separate slot exchange.
5. `L_n^Theta` is the source covector, not a cellular incidence operator.

## 2. The admissible class

For each retained character/stage label `n`, define

```text
E_n:=span_C{b_n^even}
  subset Bil_cont(J_n x J_n;C),

O_n:=the corresponding generated raw-output coefficient line.
```

The class `Norm_adm` consists of families `N={N_n}` satisfying:

1. `N_n:E_n->O_n` is bounded and complex-linear.
2. **Condition 6:** after replacing the direct coefficient crossing by
   `N_n`, `D_J Abar=(i/hbar)G_N` for the complete admitted source family.
3. **U1:** if `C_E` is the anti-linear partner transport on the even source
   line, then

   ```text
   N_(-n) C_E = - C_E N_n.                           (N-2)
   ```

   This is the derived transformation law for an even-to-odd map.
4. Every other crossing remains coefficient-neutral, as Q-305 proves.
5. `N` commutes with the Gate-4/path-visible quotient and with W3 adjoint
   finite restrictions.
6. `N` adds no tail and makes no member selection.

This class is declared before the coefficient is solved. It contains actual
maps, not schemas: on a complex line every member is multiplication by a
specific scalar family `lambda_n`.

## 3. N-uniqueness theorem

### Theorem

On `Norm_adm`, there is exactly one family:

```text
N_n=i Id_(E_n).                                      (N-3)
```

### 3.1 Identity fixes the coefficient

Write

```text
N_n(b_n^even)=lambda_n b_n^even.
```

Q-305's factor theorem, with the direct crossing replaced by `N`, is

```text
D_J Abar-(i/hbar)G_N
 =q[N_n(b_n^even)-i hbar L_n tensor L_n]
 =q(lambda_n-i)b_n^even.                             (N-4)
```

On the anchored nonzero germ, `q` is nonzero. The ratified source law is
faithful, so admitted endpoint-covariant directions exist with
`b_n^even(f,h)!=0`. Universal condition 6 therefore gives

```text
lambda_n=i.                                          (N-5)
```

This fixes modulus and phase together. No preliminary unit-phase assumption
is needed.

### 3.2 U1 fixes and verifies the transformation law

For a scalar `lambda_n`, (N-2) is equivalent to

```text
lambda_(-n)=-conjugate(lambda_n).                    (N-6)
```

The identity solution obeys it:

```text
i=-conjugate(i).
```

U1 by itself permits a purely imaginary scalar family; for a constant unit
phase it leaves both signs. Condition 6 selects the positive orientation
`i`, so the conjunction has one member.

An independent exact Gaussian-integer check returned:

```text
lambda=+1: odd law FAIL, identity FAIL
lambda=-1: odd law FAIL, identity FAIL
lambda=+i: odd law PASS, identity PASS
lambda=-i: odd law PASS, identity FAIL
lambda=1+i: odd law FAIL, identity FAIL
```

The table is a check; equations (N-4)-(N-6) are authoritative.

### 3.3 Degenerate cycle directions

For every cycle direction used by the Door-D scalar quotient,
`L_n(c)=0` where that cycle lies in the linear-source kernel. Hence

```text
b_n^even(c,h)=0,
N_n(0)=0.
```

The identity constrains no nonzero coefficient there because no nonzero
generated source-image vector exists there. This is not residual freedom:
linearity has exactly one value at zero.

### 3.4 Naturality propagates the solution

W3 gives

```text
b_N^even=i_NM^* b_M^even i_NM.
```

Thus

```text
N_N(b_N^even)
 =i b_N^even
 =i_NM^*N_M(b_M^even)i_NM.
```

The same equation proves quotient descent and restriction naturality. No
stage, cycle basis, character, or representative is selected.

### 3.5 Obstruction to an over-broad theorem

At a fixed finite stage let the complete bilocal dual split algebraically as
`E_n directsum F_n` with nonzero unused complement `F_n`. For any bounded
operator `K_n` on `F_n`,

```text
N_n^(K)=i Id_(E_n) directsum K_n
```

has the same Door-D verdict on the generated image. Neither condition tests
`K_n` at that stage. A W3-natural complement and compatible family `K_n` are
not supplied by the sealed record, so this is an obstruction to claiming a
full-space theorem, not a proof of a global natural counterfamily. Therefore:

```text
N_UNIQUE_ON_E_ACTIVE = true | TYPE-P
N_UNIQUE_ON_COMPLETE_BILOCAL_DUAL = NO_VERDICT |
  missing: a proof that W3 naturality either fixes or leaves freedom on the
           unused complement
FULL_COMPLEMENT_EXTENSION_REQUIRED_BY_DOOR_D = false | TYPE-S |
  roots: condition 6 and current source germ image |
  exclusions: future unrelated bilocal consumers |
  fences: C38 declared domain |
  query: any tested coefficient outside E_active
```

The install is consequently maximal where forced and absent where not.

## 4. Installation certificate

Source germ v007 installs (N-3) as `TensorNormCert_N`. The source pairing,
exponent, amplitude, logarithm, and all v006 interfaces remain unchanged.

```text
N_INSTALL_PROVENANCE = two_requires_jointly
N_AUTHORED = false | TYPE-R |
  test: singleton survivor in Norm_adm
N_SELECTED_FROM_FAMILY = false | TYPE-R |
  test: survivor quotient has exactly one member
SOURCE_SLOT_PARITY_CHANGED = false | TYPE-R |
  test: b_even remains in the exponent
UNUSED_COMPLEMENT_EXTENSION_INSTALLED = false | TYPE-S |
  roots: v007 clauses |
  exclusions: none |
  fences: minimal diff |
  query: K on F_n
```

## 5. Full four-subtest Door-D re-execution

### 5.1 Bounded extension

`N=i Id` has norm-preserving scalar action on `E_active`; `b_even` is bounded;
the ratified field lift is bounded. The connected result is

```text
G_n^007=-hbar^2 q(1-q)L_n tensor L_n.                (N-7)
```

It belongs to the ratified bounded bilinear class and has zero created tail.

```text
DOOR_D_BOUNDED_EXTENSION = PASS | TYPE-P
```

### 5.2 Cycle identity

On a cycle in `ker L_n`, both sides of condition 6 vanish. `N` does not turn
zero into a phase-bearing cycle value.

```text
DOOR_D_CYCLE_SAME_CORRELATOR = PASS
```

### 5.3 Endpoint-covariant open paths

For every admitted `f,h`, including nontrivial open directions:

```text
D_J Abar_n(f,h)
 =-i hbar q(1-q)L_n(f)L_n(h),

(i/hbar)G_n^007(f,h)
 =-i hbar q(1-q)L_n(f)L_n(h).
```

```text
DOOR_D_ENDPOINT_COVARIANT_SAME_CORRELATOR = PASS
```

### 5.4 U1 reality

The source exponent remains even. The boundary coefficient
`N(b_even)=i b_even` is odd by (N-2). Therefore

```text
G_(-n)^007(Theta f,Theta h)
 =conjugate(G_n^007(f,h)),

(i/hbar)G_(-n)^007(Theta f,Theta h)
 =-conjugate((i/hbar)G_n^007(f,h)),
```

which is the same odd law as `D_J Abar`.

```text
DOOR_D_U1_REALITY = PASS | TYPE-P
```

### 5.5 Conjunctive verdict

```text
DOOR_D_SUBTEST_VECTOR = (PASS,PASS,PASS,PASS)
DOOR_D_EXECUTION = PASS
DOR015_FALSIFIER_FIRES_ON_V007 = false | TYPE-R |
  test: all four registered subtests pass after the derived repair
DOR015_FREEZE_LIFTS = true | TYPE-P
```

## 6. Finite restriction execution

### 6.1 Q-243

`N` changes no source amplitude or J-Hessian. The exact finite Keldysh
difference/difference block and its ordered `(delta,c)` zero are reproduced.
The raw coefficient square commutes with the same finite Keldysh map.

```text
Q243_R0_RESTRICTION = PASS | TYPE-P
Q243_FINITE_ORDERED_RETARDED_BLOCK = ZERO_AND_P_FREE | TYPE-P
```

### 6.2 Q-279

The Amendment-2 source derivatives remain:

```text
D_R W=(i hbar/2)q Q_even,
D_JD_R W=(i hbar/2)q(1-q)L tensor Q_even,
D_R^2W=-(i hbar/4)q(1-q)Q_even tensor Q_even.
```

`N` acts only at the raw-output boundary. Its scalar action commutes with
every W3 finite corner, so the amended nonzero-`R` restriction square passes.
Historical C-B rows remain scope-superseded, not rewritten.

```text
Q279_AMENDMENT2_SOURCE_ROWS_UNCHANGED = PASS
Q279_N_BOUNDARY_RESTRICTION_SQUARE = PASS
Q279_HISTORICAL_CB_ROWS_REINSTATED = false | TYPE-S |
  scope: void historical source placement
```

## 7. Lifted chain after the pass

### 7.1 Lifted raw connected bilocal

The A4 linear transport and A6 symmetric-square transport carry (N-7) to the
ratified physical field layer:

```text
G_phys^007
 =K_R[G_n^007]
 =-hbar^2 q(1-q)(K_J L_n) tensor (K_J L_n),          (N-8)
```

with the pullback/pushforward orientation chosen consistently with Q-305.
The coefficient is unchanged by transport.

```text
DOOR_D_ADMISSIBLE_BOUNDED_RAW_G_EXISTS = true | TYPE-P
PHYSICAL_RAW_G_LIFT_EXECUTED = true | TYPE-P
CONNECTED_SUBTRACTION_EXECUTED = true | TYPE-P
```

### 7.2 Sector and p-content

```text
common/common and ordered mixed finite block: zero and p-free;
difference/difference connected block:         q(1-q)-weighted;
cycle directions in ker L:                     zero;
endpoint-covariant nonkernel directions:        q(1-q)-weighted;
created Door-D tail:                            zero;
finite ordered retarded shadow:                 zero and p-free.
```

The symbol `p_[A]` enters only through `q`; no rank ratio is evaluated.

### 7.3 Where the chain stops

The raw-map specification separately requires a two-sided convolution inverse
on the completed physical quotient, with measure, contour prescription,
boundary/contact data, and common unbounded domains. Door D does not construct
those objects. No inverse is selected or regularized here.

```text
FULL_RAW_MAP_DOMAIN_CONDITION_5_DISCHARGED = false | TYPE-C |
  constraints: physical inverse/Schur package and completed domain data absent
PHYSICAL_TWO_SIDED_INVERSE_EXECUTED = false | TYPE-C
PHYSICAL_RETHESS_INSTANCE_EXISTS = false | TYPE-C
P_ENTERS_PHYSICAL_RETHESS = NO_VERDICT
P_SURVIVES_PHYSICAL_CONSUMER = NO_VERDICT
```

## 8. Six-account operation table

| Operation | Kernel/null data | Image | Sector transfer | Restriction square | `Tail_R` action | Verdict |
|---|---|---|---|---|---|---|
| `b_even -> N(b_even)` | zero input and `ker L` evaluations remain zero | odd generated coefficient line | even source to odd raw coefficient | W3 **PASS** | zero | **PASS** |
| germ differentiation | standard `L/Q` kernels | bounded first/second derivatives | source-even exponent to W-odd derivatives | Q-243/Q-279 **PASS** | `Tail_src=0` | **PASS** |
| raw connected subtraction | `ker L` in either leg | `-hbar^2q(1-q)L tensor L` | output coefficient becomes raw-even before condition-6 factor | finite corners **PASS** | zero | **PASS** |
| physical A4/A6 lift | quotient nulls | bounded physical bilinear image | no new CTP block | Door D/W3 **PASS** | zero on built class | **PASS** |
| physical inverse/Schur | not determined | not formed | not formed | not executed | `NO_VERDICT` | **TYPE-C** |
| retarded extraction | inverse/domain prerequisite absent | not formed | finite DD block projects to ordered zero | Q-243 shadow **PASS** | complete `Tail_R` unformed | **TYPE-C** |

No operation is omitted from the accounting. The two `TYPE-C` rows are
downstream constraint blocks, not failures of the built raw bilocal.

## 9. Updated verdict shadow and remaining objects

```text
P_ENTERS_LIFTED_RAW_DD_BLOCK = true [SYMBOLIC DEPENDENCE ONLY]
P_ENTERS_FINITE_ORDERED_RETARDED_SHADOW = false | TYPE-R |
  test: exact Q-243/Q-279 ordered projection
P_ENTERS_DOOR_D_TAIL = false | TYPE-R |
  test: bounded finite-core-separated N and lift
P_ENTERS_PHYSICAL_RETHESS = NO_VERDICT
```

Door D and the source/output normalization are no longer on the residue list.
The exact remaining objects are:

1. physical inverse/Schur package, including the missing measure, contour,
   boundary/contact, and common unbounded-domain inputs;
2. `STAT_BG_LIFT_FIBER` background map;
3. completed restriction and `Tail_R` accounting;
4. induced response `Pi_R,ind`;
5. the consumer signature.

```text
NEXT_REQUIRED_OBJECT = PHYSICAL_INVERSE_SCHUR_AND_COMPLETED_DOMAIN_PACKAGE
NEXT_REQUIRED_OBJECT_BUILT = false | TYPE-U |
  would-build: the five-part first item above with its restriction and
               no-selection certificates
BACKGROUND_AND_CONSUMPTION_ONLY_REMAIN = false | TYPE-R |
  test: physical inverse/Schur package still precedes them
```

## 10. Kill passes

### 10.1 No phase selected

The candidate class was all bounded complex-linear maps on the active line.
The identity and U1 equations were attached before solving. Their survivor is
a singleton. No desired phase was inserted into the family definition.

### 10.2 No complement hidden

The fixed-stage `N^(K)` family blocks any unsupported full-space uniqueness
claim. Its W3-natural globalization is not asserted. V007 contains no `K`,
projection, or extension on the complement.

### 10.3 No double billing

The ownership table keeps `W`'s factor, `N`'s factor, and condition 6's factor
on separate arrows. Equation (N-7) is recomputed from all three.

### 10.4 No forbidden completion or selection

The chain stops before inverse, Schur, retarded, background, and consumer
class formation. No rank, anchor, torsor, cycle basis, endpoint frame,
background, contour, or prescription is selected.

## 11. Final typed ledger

```text
N_ADMISSIBLE_CLASS_FROZEN_BEFORE_SOLUTION = true
N_UNIQUENESS_ON_ACTIVE_IMAGE = PROVED | TYPE-P
N_SURVIVOR_COUNT = one
N_FORMULA = i Id_(E_active)
N_FULL_BILOCAL_EXTENSION_UNIQUE = NO_VERDICT |
  missing: W3-natural complement-extension theorem

SOURCE_GERM_PHYS_V007_INSTALLED = true | TYPE-P
DOOR_D_SUBTEST_VECTOR = (PASS,PASS,PASS,PASS)
DOOR_D_EXECUTION = PASS
DOR015_FREEZE_LIFTS = true | TYPE-P

PHYSICAL_RAW_G_LIFT_EXECUTED = true | TYPE-P
CONNECTED_SUBTRACTION_EXECUTED = true | TYPE-P
PHYSICAL_INVERSE_SCHUR_EXECUTED = false | TYPE-C
PHYSICAL_RETHESS_INSTANCE_EXISTS = false | TYPE-C

SELECTED_MEMBER_FOUND = false | TYPE-S |
  roots: complete one-line candidate family and singleton proof |
  exclusions: unused complement not installed |
  fences: no-selection |
  query: chosen phase, map, rank, anchor, torsor, cycle, or background

UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S |
  roots: E_active, O_active, raw bounded class, and A4/A6 lift |
  exclusions: inverse/Schur/retarded/background classes not formed |
  fences: Q-288 accounting |
  query: unnamed completion, bidual, weak-star, distributional, tail

REGISTER_HEAD_AT_START = Q-305 |
  register_sha256=520a79983a91c207689c85557d2845f5c88e9e2b6b9c348f29568a241f6dba40
REGISTER_HEAD_AT_SEND_TIME = Q-305 |
  register_sha256=520a79983a91c207689c85557d2845f5c88e9e2b6b9c348f29568a241f6dba40
LATER_BEARING_REGISTER_ENTRY_FOUND = false | TYPE-S |
  roots: QUESTIONS_SETTLED_REGISTER_V001.md through Q-305 |
  exclusions: no later register row existed at send time |
  query: normalization N, germ v007, Door D, physical raw G

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

The theorem is exact where the program consumes it and deliberately silent
where the program does not. On that lawful scope, the normalization is
derived, the germ is installed, Door D passes, and the bounded physical raw
bilocal exists.
