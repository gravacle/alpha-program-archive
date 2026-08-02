# Stage 8 SOURCE_GERM_PHYS v006 — DoR-014 Amendment 2 execution

**AMENDMENT-EXECUTION DRAFT — NOT INSTALLED; DOOR-D RELEASE CERTIFICATE FAILED**

Date: 2026-08-02  
Task: PASTE 386 / Task 4a  
Lane: CODEX LANE 2

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013,
                   DoR-014 as amended (2), DoR-015

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead determination

The corrected source-slot tensor

```text
b_n^even(f,h):=hbar L_n^Theta(f)L_n^Theta(h)          (SG6-1)
```

passes the complete tensor precertificate and is exactly `Theta`-even. The
source germ's internal 14-row battery is consequently clean at its former U1
failure: 11 pass / 3 conditional `TYPE-U` / 0 fail.

It does **not** pass the unchanged Door-D same-correlator identity on the
nontrivial endpoint-covariant source sector. With v004's unchanged exponent,
raw-correlator definition, and `W=-i hbar Log Z`, direct differentiation gives

```text
D_J Abar[f,h]
  =-i hbar q(1-q)L(f)L(h),

(i/hbar)G_even(f,h)
  =-hbar q L(f)L(h)+i hbar q^2 L(f)L(h).             (SG6-2)
```

Their exact residual is

```text
D_J Abar-(i/hbar)G_even
  =hbar q(1-i)L(f)L(h).                              (SG6-3)
```

It vanishes on cycle directions killed by `L`, but not on the admitted open
directions with nonzero linear-source product. Thus the parity repair works
and the claimed normalization repair does not.

```text
EVEN_TENSOR_PRECERTIFICATE = PASS
EVEN_TENSOR_THETA_PARITY = PASS
SOURCE_GERM_INTERNAL_BATTERY_V006 = 11_PASS / 3_CONDITIONAL_TYPE_U / 0_FAIL

DOOR_D_CYCLE_IDENTITY = PASS
DOOR_D_ENDPOINT_COVARIANT_IDENTITY = FAIL | TYPE-R
DOOR_D_RELEASE_CERTIFICATE = FAIL | TYPE-R
SOURCE_GERM_PHYS_V006_INSTALLED = false | TYPE-C |
  constraint: Amendment 2 requires a clean full Door-D pass
```

No normalization, involution, source/output map, or physical family is
changed beyond the exact Amendment-2 substitution.

## 1. Scope, currency, and authorities

### 1.1 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha_supervision
/Users/bgm/MB Work/alpha-program-archive/workspace  [mirror destination only]
```

| Authority | SHA-256 | Use |
|---|---|---|
| `DECISION_OF_RECORD_014_AMENDMENT_2_EVEN_PAIRING_NORMALIZATION_2026-08-02_V001.md` | `460da8c34e8a33503c0a5737f1d94b7a68cbb31fe636cd74c49e59a493efc282` | even pairing and full Door-D condition (`:4-22`) |
| `STAGE8_TASK4A_RATIFIED_BILOCAL_INVOLUTION_REALITY_LAW_DETERMINATION_V001.md` | `323852e8835175c30d503f0383ef735405d8bc40a98109e09f5974e49c603c22` | exact source/output parity table |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md` | `d4cdbb6623797df6accb7dc9b24134d179bfc8e8d039c585d5c91ae23255869e` | live exponent and derivative calculus |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V005.md` | `b3b0a7d8f6694221a2857b0ed68fe295f2a99232cf1d6a2ba5f32d810c12f67e` | verified tensor/restriction machinery and Amendment-1 failure |
| `STAGE8_TASK4A_DOR014_AMENDMENT1_DERIVED_PAIRING_AND_DOOR_D_REEXECUTION_V001.md` | `365db191e3867129a02b2216fcf10b5fc83f53b0a03cef590dfe0671c63588d9` | prior four-domain execution machinery |
| `STAGE8_TASK4A_RAW_G_RERUN_ON_RATIFIED_SIGNATURE_AND_DOOR_D_EXECUTION_V001.md` | `bffd7ef240204232a957422d60ce164151131fdbb46433def7d943d21b915382` | original Door-D suite |
| `STAGE8_TASK4A_DOOR_D_FALSIFIER_CARRIER_AND_CHECK_DIAGNOSIS_V001.md` | `b105a2c9f769c19bad420e4cbc71a23e4fcb5dcc4fc2365a825c331fad1eac97` | exact iff normalization |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U1_DOR008_ASSEMBLY_DETERMINATION_V001.md` | `1b0e928c452c10a8be72be22ff81fd7677f5045d2ad8d398a9f7f7f57b9ab3b0` | source involution and U1 domain |
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md` | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | A4/A6 physical carrier and Door D |
| `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md` | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | unchanged raw-domain identity |

The settled-question register head at construction start was Q-303, SHA-256
`fb6aaad868bb109dbd0e67abd65ee34abb2bfe4b0a6a570c4c79eddb67d94bc3`.

### 1.2 Exclusions

```text
a32_holdout/custodian_private/               NOT ENTERED
rank, anchor, torsor, or background member    NOT SELECTED
physical response, coupling, scale, or root   NOT EVALUATED
measured-constant comparison                  NOT PERFORMED
register, plan, tracker, git, commit, push    NOT TOUCHED
```

### 1.3 Bearing symbol distinctions

1. `b_n^even` is the source-slot bilinear coefficient. It is not the
   `Theta`-odd `W`-Hessian.
2. `L_n^Theta` is the accumulated linear-source covector, not the incidence
   map also called `L_N`.
3. `R` is the symmetric bilocal source, not a retarded label.
4. The `i` in `W=-i hbar Log Z` and the `i` in the raw identity's
   `(i/hbar)` prefactor occur in different operations; neither may be silently
   deleted.

## 2. Minimal diff from v004

### 2.1 Base and authorship

Replace the void C-B field by the derived certificate:

```text
b_base^006 := (A0,Tr_A,P_0,P_ch,n,
               C-A,TensorCert_L_even,D_src,topology_src,Diff_src,
               source restriction and zero-extension data).
```

The germ has one authored field, C-A. The even tensor is forced by Amendment
2 and is not entered on the choice table.

### 2.2 Pairing and source functional

On the ratified physical source carrier define

```text
ell_n:=L_n^Theta compose K_J^(-1),
b_n^even:=hbar ell_n tensor ell_n
  in Bil_cont(J_phys^005 x J_phys^005;C),

Q_n^even(R):=<b_n^even,K_R(R)>_(Bil,S_1),
Q_n^even(f symtensor h)=hbar ell_n(f)ell_n(h).        (SG6-4)
```

### 2.3 Germ formula

The only formula substitution is

```text
Xi_[A],n^006[J,R]
  :=L_n^Theta(J)-(1/2)Q_n^even(R),

Z_[A],n^006[J,R]
  :=(1-p_[A])+p_[A]exp(Xi_[A],n^006[J,R]),

W_[A],n^006:=-i hbar Log_0 Z_[A],n^006.              (SG6-5)
```

All A0 rank-family, Gen_Omega, plus-root, topology, anchored-logarithm,
same-rank gauge, anchor/transient quotient, no-selection, and
no-supplementation clauses remain byte-for-byte in force by reference.

## 3. Even tensor precertificate

### 3.1 Boundedness and uniqueness inside the ruling

```text
|b_n^even(f,h)|
 <=|hbar| ||ell_n||^2 ||f|| ||h||.
```

It is a continuous symmetric rank-one form. Amendment 2 supplies its exact
coefficient, so the execution introduces no family or normalization choice.

### 3.2 Quotient compatibility

If `v` is a physical source null, the descended covector satisfies
`ell_n(v)=0`. Therefore the even tensor vanishes with `v` in either slot and
descends through the Gate-4/path-invisible quotient.

### 3.3 W3 restriction naturality

For W3's isometric inclusion `i_NM:C_N->C_M` and adjoint restriction
`rho_MN=i_NM^*`,

```text
ell_N=ell_M compose i_NM,
b_N^even=i_NM^* b_M^even i_NM
        =hbar ell_N tensor ell_N.                    (SG6-6)
```

The trace-class source corner is the corresponding adjoint corner. No naive
edge truncation occurs.

### 3.4 Theta parity

The ratified source law gives

```text
L_(-n)(Theta_J f)=conjugate(L_n(f)).
```

Because `hbar` is real in the standing convention,

```text
b_(-n)^even(Theta_J f,Theta_J h)
 =hbar conjugate(L_n(f))conjugate(L_n(h))
 =conjugate(b_n^even(f,h)).                           (SG6-7)
```

Thus `Q_(-n)^even(Theta_R R)=conjugate(Q_n^even(R))` on the complete
symmetric source class by finite-rank density and continuity.

### 3.5 Tail

The tensor is bounded and determined by finite corners. It creates no source
or Door-D tail.

```text
EVEN_TENSOR_WELL_DEFINED = true | TYPE-P
EVEN_TENSOR_QUOTIENT_COMPATIBLE = true | TYPE-P
EVEN_TENSOR_RESTRICTION_NATURAL = true | TYPE-P
EVEN_TENSOR_W3_ADJOINT_COMPATIBLE = true | TYPE-P
EVEN_TENSOR_THETA_EVEN = true | TYPE-P
EVEN_TENSOR_CREATED_TAIL = false | TYPE-R |
  test: bounded finite-core determination
```

## 4. Bookkeeping chain — no implicit factors

Set

```text
q:=p_[A]exp(Xi^006)/Z^006.
```

The unchanged exponent and W convention give, in order:

```text
D_J Xi[f]                 =L(f),
D_R Xi[f symtensor h]     =-(1/2)b_even(f,h),

D_J Log Z[f]              =qL(f),
D_R Log Z[f symtensor h]  =-(q/2)b_even(f,h),

Abar(f)=D_J W[f]          =-i hbar qL(f),
D_J Abar[f,h]             =-i hbar q(1-q)L(f)L(h),

2D_R W[f symtensor h]
  =i hbar q b_even(f,h)
  =i hbar^2 q L(f)L(h),

Abar(f)Abar(h)
  =-hbar^2 q^2L(f)L(h),

G_even(f,h)
  =2D_R W-Abar tensor Abar
  =i hbar^2 qL(f)L(h)+hbar^2q^2L(f)L(h),

(i/hbar)G_even(f,h)
  =-hbar qL(f)L(h)+i hbar q^2L(f)L(h).               (SG6-8)
```

Comparison with `D_J Abar` leaves (SG6-3). The `i` from W has not been
dropped: it appears explicitly in `2D_R W`. Multiplication by the identity's
own `i/hbar` turns that leading coefficient into a real minus sign. This is
why the statement “W supplies the i” is insufficient.

An independent exact Gaussian-integer coefficient check returned:

```text
left  (q,q^2)=(-i,+i),
right (q,q^2)=(-1,+i),
residual       =(1-i,0),
PASS=false.
```

As a control, the superseded odd coefficient returned equal pairs
`(-i,+i)`; the calculation therefore distinguishes the two normalizations.

## 5. Fresh 14-row battery

The source-germ battery and Door D are distinct gates. The former tests the
germ interface; the latter tests promotion to one physical raw correlator.

| Row | V006 verdict | Certificate / residual condition |
|---|---|---|
| B1 finite restriction | **PASS / TYPE-P** | `R=0` sealed amplitudes are unchanged; amended nonzero-`R` finite corners are explicit, restriction-natural, and U1-even. Historical C-B rows are superseded, not claimed reproduced. |
| B2 Q-243 finite retarded baseline | **PASS / TYPE-P** | At `R=0`, the J-Hessian and zero ordered block are unchanged. |
| B3 finite retarded restrictions | **PASS / TYPE-P** | W3 adjoint corners preserve B2 stagewise. |
| B4 extension mechanism | **PASS / TYPE-P** | bounded tensor on the ratified norm class; no naive extension. |
| B5 named separation class | **CONDITIONAL / TYPE-U** | would-build: physical `RetHess_phys` class and injective representation. |
| B6 explicit tail | **CONDITIONAL / TYPE-U** | would-build: physical `Tail_R` and germ-to-tail theorem. |
| B7 modulo-tail determinacy | **PASS / TYPE-P** | finite-core density fixes the tensor elementwise. |
| B8 finite-visible quotient | **PASS / TYPE-P** | symbolic ordered ranks and `p_[A]` remain unevaluated. |
| B9 consumer tail certificate | **CONDITIONAL / TYPE-U** | would-build: six consumer-specific factorization certificates. |
| B10 stationary point | **PASS / TYPE-P** | no background or stationary point is inferred. |
| B11 C1/evaluation | **PASS / TYPE-P** | zero source remains normalization data, not an evaluation rule. |
| B12 zero surfaces | **PASS / TYPE-P** | source, holonomy, and difference-field zero remain distinct. |
| B13 finite authority | **PASS / TYPE-P** | the tensor has explicit finite restrictions and no invisible component. |
| B14 provenance | **PASS / TYPE-P** | the even tensor uses only `L`; Gen_Omega descent and no supplementation are unchanged. |

```text
BATTERY_V006_PASS_COUNT = 11
BATTERY_V006_CONDITIONAL_TYPE_U_COUNT = 3
BATTERY_V006_FAIL_COUNT = 0
```

The battery does not override the failed Door-D release certificate.

## 6. Version and restriction accounting

| Object | Standing after Amendment 2 |
|---|---|
| v004 C-B same-cell trace | void since Q-300/Q-301 |
| v005 `i hbar L tensor L` | superseded by Amendment 2 |
| v006 `hbar L tensor L` | U1-valid source-germ candidate; raw identity failure |
| Q-243 `R=0` rows | reproduced exactly |
| Q-279 J-only and `R=0` rows | reproduced exactly |
| Q-279 historical C-B-dependent rows | scope-superseded by the two amendments |
| amended nonzero-`R` finite rows | explicitly recomputed and W3-natural |

The later specific ruling controls the pairing-dependent finite rows. No
historical C-B value is silently called an amended restriction.

## 7. Exact changed-clause ledger

```text
C-B                              -> void
Amendment-1 TensorCert_L_odd     -> superseded
TensorCert_L_even                -> derived replacement
Q_delta^Theta                    -> Q_n^even
Xi/Z/D_R formulas                -> mechanical Q replacement
authored germ-choice count       -> one (C-A only)
U1 reality certificate           -> PASS
Door-D same-correlator release   -> FAIL on open sector
```

Everything else in v004 is inherited unchanged by reference.

## 8. Final ledger

```text
DOR014_AMENDMENT2_EVEN_PAIRING_EXECUTED = true | TYPE-P
NEW_PAIRING_CHOICE_ADDED = false | TYPE-R |
  test: exact Amendment-2 requirement
EVEN_TENSOR_PRECERTIFICATE_BUILT = true | TYPE-P
EVEN_TENSOR_THETA_EVEN = true | TYPE-P

SOURCE_GERM_INTERNAL_BATTERY_V006 = 11_PASS / 3_CONDITIONAL_TYPE_U / 0_FAIL
SOURCE_GERM_V006_U1_REAL = true | TYPE-P

SAME_CORRELATOR_IDENTITY_ON_COMPLETE_SOURCE_FAMILY = false | TYPE-R |
  test: SG6-3 on admitted nontrivial open directions
DOOR_D_RELEASE_CERTIFICATE = FAIL | TYPE-R
SOURCE_GERM_PHYS_V006_INSTALLED = false | TYPE-C |
  constraint: full Door D did not pass

NEXT_REQUIRED_OBJECT = EVEN_SOURCE_TO_ODD_RAW_OUTPUT_NORMALIZATION_DISPOSITION |
  standing: TYPE-U as an object; unchanged direct identification refuted |
  no option selected

SELECTED_MEMBER_FOUND = false | TYPE-S |
  roots: full source family and universal tensor calculations |
  exclusions: hostile witnesses used only for tests |
  fences: no-selection discipline |
  query: selected rank, anchor, torsor, intertwiner, cycle, or background

UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S |
  roots: bounded tensor and trace-dual formation |
  exclusions: inverse and retarded classes not formed |
  fences: W3/Q-288 accounting |
  query: unnamed completion, bidual, weak-star, distributional, tail

REGISTER_HEAD_AT_SEND_TIME = Q-303 |
  register_sha256=fb6aaad868bb109dbd0e67abd65ee34abb2bfe4b0a6a570c4c79eddb67d94bc3
LATER_BEARING_REGISTER_ENTRY_FOUND = false | TYPE-S |
  roots: QUESTIONS_SETTLED_REGISTER_V001.md through Q-303 |
  exclusions: no later register row existed at send time |
  query: Amendment 2, even pairing, Door D, source germ v006

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

**AMENDMENT-EXECUTION DRAFT — SOURCE-GERM BATTERY CLEAN; DOOR-D RELEASE FAILED**
