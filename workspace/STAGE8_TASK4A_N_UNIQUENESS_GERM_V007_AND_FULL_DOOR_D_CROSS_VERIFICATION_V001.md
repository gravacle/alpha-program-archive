# Stage 8 Task 4a N-uniqueness, germ V007, and full Door-D cross-verification V001

Date: 2026-08-02

Lane: CODEX LANE 1

Task: PASTE 389 / Task 4a

Register head: Q-306

## 0. Lead verdict

```text
VERDICT = CONFIRMED

N_UNIQUENESS_ON_DOOR_D_ACTIVE_IMAGE = CONFIRMED | TYPE-P
SOURCE_GERM_PHYS_V007_INSTALL = CONFIRMED | TYPE-P
DOOR_D_SUBTEST_VECTOR = (PASS,PASS,PASS,PASS)
DOR015_FREEZE_LIFT_STANDS = true | TYPE-P
```

The proof, installation, and four-subtest execution survive independent
recomputation. On the exact active image commissioned by C38,

```text
E_n=span_C{b_n^even},
b_n^even=hbar L_n tensor L_n,
N_n=i Id_(E_n)
```

is the unique bounded complex-linear source-to-output normalization satisfying
both condition 6 and the U1 even-to-odd anti-intertwining law. The resulting
connected bilocal is

```text
G_n^007=-hbar^2 q(1-q)L_n tensor L_n,
```

and it obeys

```text
D_J Abar=(i/hbar)G_n^007
```

on cycles and endpoint-covariant open paths. Its U1 parity is correct.

The confirmation is deliberately narrow. The theorem does not determine an
operator on the unused complete bilocal complement. No such extension is
installed, and no currently built consumer reaches that complement. The chain
still stops before the physical two-sided inverse, stationary Schur reduction,
completed domains, and physical retarded instance.

## 1. Preflight, custody, and scope

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = yes
IS_THE_VERSION_CURRENT = yes | register head Q-306
ARE_ITS_INPUTS_PRESENT = yes
```

The two Q-306 artifacts and their local sidecars verify:

| Artifact | SHA-256 |
|---|---|
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V007.md` | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` |
| `STAGE8_TASK4A_SOURCE_TO_OUTPUT_NORMALIZATION_N_UNIQUENESS_INSTALL_AND_FULL_DOOR_D_REEXECUTION_V001.md` | `00414b0d5617e44b12e9f7faef4484803c858992be6ed1951df38c22719b2696` |

The workspace-mirror copies have the same hashes. The current register hash at
the verification start is:

```text
QUESTIONS_SETTLED_REGISTER_V001.md
48387264f248dfbd17f097937e82d2af99b1b7a2b2dc43dfb28b62e7815e6e72
```

### 1.2 Roots entered

1. `/Users/bgm/MB Work/alpha_supervision/LOCKED_PROCESS.md`
2. `/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md`
3. `/Users/bgm/MB Work/alpha_supervision/TASK_LIST_HERE_TO_ALPHA_2026-08-01_V002.md`, C38 only
4. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V006.md`
5. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V007.md`
6. `STAGE8_TASK4A_SOURCE_TO_OUTPUT_NORMALIZATION_N_UNIQUENESS_INSTALL_AND_FULL_DOOR_D_REEXECUTION_V001.md`
7. `STAGE8_TASK4A_DOOR_D_TRANSPORT_JACOBIAN_CTP_METRIC_AND_FACTOR_AUDIT_V001.md`
8. `STAGE8_TASK4A_RATIFIED_BILOCAL_INVOLUTION_REALITY_LAW_DETERMINATION_V001.md`
9. `STAGE8_TASK4A_DOR014_AMENDMENT2_EVEN_PAIRING_FULL_DOOR_D_REEXECUTION_V001.md`
10. `STAGE8_CTP_PHYS_INPUT_PACKAGE_U1_DOR008_ASSEMBLY_DETERMINATION_V001.md`
11. `STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md`
12. `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md`
13. `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md`
14. `STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md`

Unqualified Stage-8 paths are rooted at:

`/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/`

### 1.3 Exclusions and acts not performed

```text
A32_PRIVATE_ROOT_ENTERED = false | TYPE-S |
  roots: declared verification roots |
  exclusions: a32_holdout/custodian_private/ |
  fences: standing custody fence |
  query: any read, write, or traversal of the private root
UNUSED_BILOCAL_COMPLEMENT_NORMALIZED = false | TYPE-S |
  roots: active-image theorem and V007 install |
  exclusions: future complement consumers |
  fences: C38 minimal install |
  query: any normalization outside E_active
PHYSICAL_INVERSE_SCHUR_PACKAGE_CONSTRUCTED = false | TYPE-U |
  would-build: completed inverse, Schur, measure, contour, boundary/contact,
               and common-domain package
PHYSICAL_RETHESS_INSTANCE_CONSTRUCTED = false | TYPE-U |
  would-build: the inverse/Schur package followed by retarded extraction
RANK_ANCHOR_TORSOR_CYCLE_BASIS_OR_BACKGROUND_SELECTED = false | TYPE-S |
  roots: this verification and its exact source set |
  exclusions: none |
  fences: no-selection |
  query: a selected rank, anchor, torsor, cycle basis, or background
BARRED_EVALUATION_OR_COMPARISON_PERFORMED = false | TYPE-S |
  roots: this verification's commands and artifact |
  exclusions: none |
  fences: LOCKED_PROCESS act-based fences |
  query: physical root, coupling, scale, or measured comparison
REGISTER_TRACKER_OR_PLAN_EDITED = false | TYPE-S |
  roots: this lane's custody acts |
  exclusions: reviewer-only records |
  fences: Q-91 custody |
  query: register, tracker, or plan edit
GIT_COMMIT_PUSH_OR_DEPLOY_PERFORMED = false | TYPE-S |
  roots: this lane's custody acts |
  exclusions: none |
  fences: Q-91 custody |
  query: git, commit, push, or deploy
```

```text
PREMISE_BEYOND_CURRENT_STACK_INTRODUCED = false | TYPE-S |
  roots: sections 1-8 |
  exclusions: none |
  fences: F-GK3 premise disclosure |
  query: any premise not in the Q-306 stack
```

## 2. Independent N-uniqueness derivation

### 2.1 Candidate family is not target-narrowed

C38 commissions the source-to-output coefficient normalization first and says
to derive it if the two requirements leave one survivor. The ratified bilocal
source is the symmetric complex-linear part of `D_J tensor_alg D_J`. The
admissible active image in the Q-306 proof is therefore

```text
E_n=span_C{b_n^even},
O_n=the corresponding generated raw-output coefficient line,
N_n:E_n->O_n bounded and complex-linear.
```

This is the complete bounded complex-linear map class on the ruled one-line
interface. It does not assume unit modulus, a phase, or the desired answer.
Every member has

```text
N_n(b_n^even)=lambda_n b_n^even
```

for one complex scalar `lambda_n`.

### 2.2 Condition 6 fixes the coefficient

Start from the independently certified Q-305 source-chart formulas:

```text
Xi=L-(1/2)Q,
Z=(1-p)+p exp(Xi),
q=p exp(Xi)/Z,
W=-i hbar Log_0 Z.
```

The linear-source Hessian is

```text
D_J Abar=-i hbar q(1-q)L tensor L.                  (CV-1)
```

After the boundary map, the connected bilocal is

```text
G_N=i hbar q N(b_even)+hbar^2 q^2 L tensor L
   =i hbar^2 q lambda_n L tensor L
      +hbar^2 q^2 L tensor L.                       (CV-2)
```

Applying condition 6 gives

```text
D_J Abar-(i/hbar)G_N
 =hbar q(lambda_n-i)L tensor L
 =q(lambda_n-i)b_even.                              (CV-3)
```

On the nonzero Log_0 germ, `q` is nonzero. The faithful admitted source class
contains endpoint-covariant pairs with nonzero `L(f)L(h)`. Universal equality
therefore forces

```text
lambda_n=i.                                         (CV-4)
```

This fixes modulus and phase together. No unit-phase premise is used.

### 2.3 U1 fixes the law and checks the survivor

Let `C_E` be the anti-linear partner transport on the even coefficient line.
An even-to-odd boundary map must obey

```text
N_(-n) C_E=-C_E N_n.                                (CV-5)
```

For scalar multiplication this is exactly

```text
lambda_(-n)=-conjugate(lambda_n).                   (CV-6)
```

Both constant imaginary orientations satisfy U1, but condition 6 distinguishes
them:

| Candidate | U1 | Condition 6 |
|---|---|---|
| `+1` | fail | fail |
| `-1` | fail | fail |
| `+i` | pass | pass |
| `-i` | pass | fail |
| `1+i` | fail | fail |

The exact condition-6 residual coefficient is `lambda-i`; the table is only a
finite control on the symbolic result. The survivor count is one.

### 2.4 Cycles add no freedom

For every Door-D cycle in the linear-source kernel,

```text
L_n(c)=0,
b_n^even(c,h)=0.
```

The unique active-line map evaluates to

```text
N_n(b_n^even)(c,h)=i b_n^even(c,h)=0.
```

Thus cycles neither create a second coefficient nor receive a phase-bearing
value. This is linearity at zero, not a selection of a cycle representative.

### 2.5 Restriction naturality

For the W3 inclusion `i_NM`, the sealed source tensor obeys

```text
b_N^even=i_NM^* b_M^even i_NM.
```

Multiplication by `i` commutes with this corner:

```text
N_N(b_N^even)
 =i b_N^even
 =i_NM^* N_M(b_M^even)i_NM.                         (CV-7)
```

The same scalar identity proves quotient descent. No stage, character, basis,
representative, or endpoint frame is chosen.

### 2.6 Unused complement: the theorem stops honestly

At a fixed stage, suppose the complete bilocal dual admits an algebraic split

```text
E_n directsum F_n,
```

with unused `F_n`. Every bounded `K_n:F_n->F_n` gives the same active verdict
for

```text
i Id_(E_n) directsum K_n.
```

No W3-natural complement family is supplied, so this is not promoted to a
global counterfamily. It is enough to block any full-dual uniqueness claim.

A word-bounded corpus search at head Q-306 finds `N`, `TensorNormCert_N`, and
`G^007` only in V007 and the Q-306 determination. No later built consumer
reaches `F_n`. The raw-map specification may eventually need a complete
two-sided inverse, but that package is explicitly unbuilt and is exactly the
Q-306 stop.

```text
N_UNIQUE_ON_E_ACTIVE = true | TYPE-P
N_UNIQUE_ON_COMPLETE_BILOCAL_DUAL = NO_VERDICT |
  missing: a W3-natural complement-extension theorem or counterfamily
N_EXTENSION_TO_UNUSED_COMPLEMENT_INSTALLED = false | TYPE-S |
  roots: V007 and Q-306 install clauses |
  exclusions: future inverse/Schur and unrelated bilocal consumers |
  fences: C38 active-image scope |
  query: K_n or any installed action outside E_active
CURRENT_BUILT_CONSUMER_REQUIRING_UNUSED_COMPLEMENT_FOUND = false | TYPE-S |
  roots: cleanroom Markdown at register head Q-306 |
  exclusions: unbuilt future packages |
  fences: word-bounded exact-symbol search |
  query: N, TensorNormCert_N, G^007, and V007 hash
```

## 3. Independent G007 and factor recomputation

With `lambda_n=i`, (CV-2) becomes

```text
G_n^007
 =i hbar^2 q i L_n tensor L_n+hbar^2 q^2 L_n tensor L_n
 =-hbar^2 q L_n tensor L_n+hbar^2 q^2 L_n tensor L_n
 =-hbar^2 q(1-q)L_n tensor L_n.                     (CV-8)
```

Then

```text
(i/hbar)G_n^007
 =-i hbar q(1-q)L_n tensor L_n
 =D_J Abar_n.                                       (CV-9)
```

The factor ownership is one-to-one:

| Factor | Owner | Effect |
|---|---|---|
| `-i hbar` | `W=-i hbar Log_0 Z` | source-functional derivatives |
| `i` | the derived `N` | even source coefficient to odd raw coefficient |
| `i/hbar` | sealed raw-map condition 6 | raw output to same-correlator comparison |

Deleting any one factor breaks (CV-9); applying any twice also breaks it.

```text
FACTOR_OWNER_MISSING = false | TYPE-R |
  test: direct recomputation CV-1 through CV-9
FACTOR_DOUBLE_BILLED = false | TYPE-R |
  test: coefficient ledger and exact residual lambda-i
```

## 4. Four Door-D subtests, independently rerun

### 4.1 Bounded extension

On the active line,

```text
||N_n x||=||x||.
```

The source tensor is a bounded rank-one bilinear form, `q` is defined on the
nonzero local Log_0 domain, and the ratified A4/A6 lift is bounded. Therefore
`G^007` belongs to the built bounded bilinear class. Scalar multiplication by
`i` creates no tail.

```text
DOOR_D_BOUNDED_EXTENSION = PASS | TYPE-P
```

### 4.2 Cycle same-correlator identity

On `c in ker L_n`, both (CV-1) and (CV-9) vanish. No quotient representative
or cycle basis enters.

```text
DOOR_D_CYCLE_SAME_CORRELATOR = PASS
```

### 4.3 Endpoint-covariant same-correlator identity

For arbitrary admitted endpoint-covariant `f,h`, including nonkernel pairs,
(CV-1) and (CV-9) agree pointwise. This is the failure-capable subtest that
rejected V006; its old residual becomes

```text
hbar q(lambda-i)L tensor L=0
```

only because the uniqueness theorem fixed `lambda=i`.

```text
DOOR_D_ENDPOINT_COVARIANT_SAME_CORRELATOR = PASS
```

### 4.4 U1 reality

The source tensor is even and `N(b_even)=i b_even` is odd under the anti-linear
partner law. Since `hbar` is real and

```text
q_(-n)(Theta s)=conjugate(q_n(s)),
L_(-n)(Theta f)=conjugate(L_n(f)),
```

(CV-8) gives

```text
G_(-n)^007(Theta f,Theta h)=conjugate(G_n^007(f,h)).
```

The separate condition-6 factor then gives

```text
(i/hbar)G_(-n)^007(Theta f,Theta h)
 =-conjugate((i/hbar)G_n^007(f,h)),
```

which is the same odd law obeyed by `D_J Abar`.

```text
DOOR_D_U1_REALITY = PASS | TYPE-P
DOOR_D_SUBTEST_VECTOR = (PASS,PASS,PASS,PASS)
DOOR_D_FAILURE_ON_CROSS_VERIFICATION_FOUND = false | TYPE-S |
  roots: all four failure-capable subtests above |
  exclusions: unbuilt inverse/Schur and retarded packages |
  fences: Door-D registered test boundary |
  query: boundedness, cycle identity, open identity, or U1 failure
```

## 5. V007 minimality and battery inheritance

### 5.1 Semantic diff from V006

V006 and V007 retain the same source pairing and source functional:

```text
b_even=hbar L tensor L,
Xi=L-(1/2)Q_even,
Z=(1-p)+p exp(Xi),
W=-i hbar Log_0 Z.
```

The semantic additions are exactly:

```text
E_n,
O_n,
N_n:E_n->O_n,
TensorNormCert_N,
G_n^007.
```

`N` acts after source differentiation. No source exponent, rank family,
Gen_Omega descent, topology, calculus, logarithm, quotient, background, or
authored choice table changes. The Markdown files are not byte-identical as
whole documents; the claimed minimality is a changed-clause claim, and that
claim passes.

```text
V006_AND_V007_WHOLE_FILES_BYTE_IDENTICAL = false | TYPE-R |
  test: full unified diff; V007 necessarily adds install and verdict sections
V007_SOURCE_PAIRING_CHANGED = false | TYPE-R |
  test: V006 SG6-1/SG6-4 against V007 sections 0 and 2
V007_UNDECLARED_SEMANTIC_CHANGE_FOUND = false | TYPE-S |
  roots: full V006-to-V007 diff and changed-clause manifests |
  exclusions: prose, status, authority, and verdict updates required by install |
  fences: semantic minimality test |
  query: source exponent, source pairing, rank, topology, calculus,
         logarithm, quotient, background, or choice-table drift
V007_ADDED_AUTHORED_FIELD = false | TYPE-R |
  test: singleton survivor in the predeclared Norm_adm family
```

### 5.2 Fourteen-row battery

The battery independently recomputes as follows:

| Row | Cross-verdict | Reason |
|---|---|---|
| B1 finite restriction | PASS | scalar `N` commutes with every bilinear corner |
| B2 Q-243 baseline | PASS | amplitude and J-Hessian unchanged |
| B3 finite retarded restrictions | PASS | W3 naturality; ordered mixed block remains zero |
| B4 extension mechanism | PASS | norm-one map on the generated line |
| B5 named separation class | CONDITIONAL / TYPE-U | complete `RetHess_phys` class unbuilt |
| B6 explicit tail | CONDITIONAL / TYPE-U | complete physical `Tail_R` unbuilt |
| B7 modulo-tail determinacy | PASS | no invisible component is added on the active line |
| B8 finite-visible quotient | PASS | ordered ranks remain symbolic |
| B9 consumer tail certificate | CONDITIONAL / TYPE-U | consumer-specific factorizations unbuilt |
| B10 stationary point | PASS | no background selected |
| B11 C1/evaluation | PASS | zero source is not promoted to an evaluation rule |
| B12 zero surfaces | PASS | source, history, and difference zeros remain distinct |
| B13 finite authority | PASS | scalar action is fixed and checked at every finite generator |
| B14 provenance | PASS | `N` is the singleton satisfying condition 6 plus U1 under C38 |

```text
SOURCE_GERM_INTERNAL_BATTERY_V007 = 11_PASS / 3_CONDITIONAL_TYPE_U / 0_FAIL
BATTERY_REGRESSION_FOUND = false | TYPE-S |
  roots: all fourteen inherited rows |
  exclusions: no conditional row upgraded |
  fences: V007 changed-clause scope |
  query: a V006 passing row broken or a conditional row silently discharged
```

## 6. Exact finite restrictions

### 6.1 Q-243 at zero bilocal probe

V007 does not change `Z`, `W`, or their source derivatives. The finite
difference/difference Hessian and the ordered `(delta,c)` zero are therefore
unchanged. `N` acts only at the raw-output boundary and commutes with the same
finite Keldysh square.

```text
Q243_R0_RESTRICTION = PASS | TYPE-P
Q243_FINITE_ORDERED_RETARDED_BLOCK = ZERO_AND_P_FREE | TYPE-P
```

### 6.2 Q-279 at nonzero bilocal probe

At the Q-279 reference point,

```text
q=omega_eta,
q(1-q)=kappa_eta,
L_n=i n ell_N,
n^2=1.
```

Thus

```text
L_n tensor L_n=-ell_N tensor ell_N,

G_n^007
 =+hbar^2 kappa_eta ell_N tensor ell_N,

(i/hbar)G_n^007
 =+i hbar kappa_eta ell_N tensor ell_N.              (CV-10)
```

Equation (CV-10) is exactly Q-279's finite `(delta,delta)` noise row. At
`eta=0`, `omega_eta=p` and `kappa_eta=p(1-p)`, reproducing Q-243. The charged
dephasing amplitude and all first/mixed `J/R` source rows are unchanged because
`N` does not alter `Z`, `W`, or `Q_even`.

Every block with a common-source leg remains zero because

```text
D_(J_c)Xi=0.
```

Hence the ordered `(delta,c)` finite retarded shadow remains zero before any
`q`-dependent coefficient can act. It is zero and p-free without division,
normalization, or cancellation.

```text
Q279_NOISE_WEIGHT_RESTRICTION = PASS | TYPE-P
Q279_KAPPA_ETA_AT_ETA_ZERO = PASS | TYPE-P
Q279_DEPHASING_AND_SOURCE_ROWS_UNCHANGED = PASS | TYPE-P
Q279_FINITE_ORDERED_RETARDED_SHADOW = ZERO_AND_P_FREE | TYPE-P
FINITE_RESTRICTION_MISMATCH_FOUND = false | TYPE-S |
  roots: Q-243 and Q-279 exact derivative tables |
  exclusions: historical void C-B rows |
  fences: amended V006/V007 source placement |
  query: sign, q weight, kappa_eta, dephasing weight, or ordered-block mismatch
```

## 7. Honest stop and inheritance boundary

The A4 linear transport and A6 symmetric-square transport carry the verified
rank-one connected bilocal to the built bounded physical class without
changing its scalar coefficient. This establishes the bounded raw physical
lift and connected subtraction on the active image.

It does not establish raw-map domain condition 5. The next operation requires
a two-sided convolution inverse on the completed physical quotient together
with measure, contour, boundary/contact data, and common unbounded domains.
None is supplied by V007 or the uniqueness theorem.

The retarded extraction is therefore not executed. The exact DD raw block is
`q(1-q)`-weighted, while its finite ordered retarded shadow is zero and p-free.
No claim is transported from that shadow to the unbuilt physical retarded
operator.

```text
BOUNDED_PHYSICAL_RAW_G_LIFT = CONFIRMED | TYPE-P
CONNECTED_SUBTRACTION = CONFIRMED | TYPE-P
PHYSICAL_INVERSE_SCHUR_PACKAGE_BUILT = false | TYPE-U |
  would-build: two-sided inverse plus measure, contour, boundary/contact,
               common-domain, restriction, and no-selection certificates
FULL_RAW_MAP_DOMAIN_CONDITION_5_CHECK_EXECUTED = false | TYPE-C |
  constraint: its required physical inverse/Schur package is unbuilt
PHYSICAL_RETHESS_INSTANCE_BUILT = false | TYPE-U |
  would-build: the completed-domain inverse followed by the sealed retarded
               extraction
P_ENTERS_PHYSICAL_RETHESS = NO_VERDICT
P_SURVIVES_PHYSICAL_CONSUMER = NO_VERDICT
UNBUILT_COMPLEMENT_USED_AS_IF_INSTALLED = false | TYPE-S |
  roots: V007, Q-306 determination, and current exact consumers |
  exclusions: future inverse/Schur attempt |
  fences: active-image install |
  query: complement projection, extension, inverse, or regularization
```

## 8. Final cross-verification ledger

```text
N_ADMISSIBLE_CLASS_PREDECLARED = true
N_UNIQUENESS_ON_ACTIVE_IMAGE = CONFIRMED | TYPE-P
N_SURVIVOR_COUNT = one
N_FORMULA = i Id_(E_active)
N_UNIQUENESS_ON_COMPLETE_BILOCAL_DUAL = NO_VERDICT

SOURCE_GERM_PHYS_V007 = CONFIRMED | TYPE-P
V007_SEMANTIC_DIFF = MINIMAL
SOURCE_GERM_INTERNAL_BATTERY_V007 = 11_PASS / 3_CONDITIONAL_TYPE_U / 0_FAIL

G007_FORMULA = -hbar^2 q(1-q)L tensor L
SAME_CORRELATOR_IDENTITY = PASS
U1_REALITY = PASS
DOOR_D_SUBTEST_VECTOR = (PASS,PASS,PASS,PASS)
DOOR_D_EXECUTION = PASS
DOR015_FREEZE_LIFT_STANDS = true | TYPE-P

Q243_RESTRICTION = PASS
Q279_RESTRICTION = PASS
FINITE_ORDERED_RETARDED_SHADOW = ZERO_AND_P_FREE | TYPE-P
PHYSICAL_RETHESS = NO_VERDICT

CROSS_VERIFICATION_DEFECT_FOUND = false | TYPE-S |
  roots: uniqueness, install, four Door-D subtests, fourteen battery rows,
         Q-243/Q-279 restrictions, and stop audit |
  exclusions: unused complete bilocal complement and unbuilt downstream
              inverse/Schur/retarded packages |
  fences: PASTE 389 scope |
  query: a defect that reimposes the DoR-015 freeze

REGISTER_HEAD_AT_START = Q-306 |
  register_sha256=48387264f248dfbd17f097937e82d2af99b1b7a2b2dc43dfb28b62e7815e6e72
REGISTER_HEAD_AT_COMPLETION = Q-306 |
  register_sha256=48387264f248dfbd17f097937e82d2af99b1b7a2b2dc43dfb28b62e7815e6e72
LATER_BEARING_REGISTER_ENTRY_FOUND = false | TYPE-S |
  roots: QUESTIONS_SETTLED_REGISTER_V001.md through Q-306 |
  exclusions: no later register row existed at completion |
  fences: send-time currency check |
  query: N uniqueness, germ V007, Door D, or physical raw G

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

The freeze lift stands. The next real object is the physical inverse/Schur and
completed-domain package; V007 does not pretend to have built it.
