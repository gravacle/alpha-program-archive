# Stage 8 SOURCE_GERM_PHYS v005 — DoR-014 Amendment 1 execution

**AMENDMENT-EXECUTION DRAFT — PENDING CROSS-LANE VERIFICATION**

Date: 2026-08-02  
Task: PASTE 384 / Task 4a  
Lane: CODEX LANE 2

Premise-dependent positives are marked:

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013,
                   DoR-014 as amended, DoR-015
```

```text
alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead determination

The tensor replacement ordered by DoR-014 Amendment 1 is unique and passes
the same-correlator algebra, but it does **not** define a valid v005 germ with
the rest of v004 untouched. The obstruction is the already-ratified U1
reality involution.

For the live linear source form, the amendment requires

```text
b_n(f,h):=i hbar L_n^Theta(f)L_n^Theta(h).             (SG5-1)
```

This form is bounded, symmetric, quotient-compatible, finite-restriction
natural, and compatible with the W3 adjoint restriction squares. It is also
exactly the unique form for which

```text
D_J Abar=(i/hbar)(2D_R W-Abar tensor Abar).
```

However, the ratified source involution and v004 reality certificate require

```text
L_(-n)^Theta(Theta_J f)=conjugate(L_n^Theta(f)),
Q_(-n)(Theta_R R)=conjugate(Q_n(R)).                  (SG5-2)
```

On a rank-one symmetric source `R=f symtensor h`, (SG5-1) instead gives

```text
Q_(-n)^L(Theta_R R)
  = i hbar conjugate(L_n(f))conjugate(L_n(h))
  = -conjugate(Q_n^L(R)).                             (SG5-3)
```

For the nontrivial character directions required by charge/flux access, the
right side is not zero. Thus the amended exponent fails the exact U1 relation
at nonzero `R`. This is not a missing proof and not a choice of convention:
the two signs are algebraically opposite under the fixed anti-linear
involution.

```text
TENSOR_PRECERTIFICATE_FIXED_N = PASS
SAME_CORRELATOR_TENSOR_IDENTITY = PASS
U1_REALITY_OF_AMENDED_NONZERO_R_GERM = false | TYPE-R |
  test: SG5-2 versus SG5-3 on an admitted nontrivial character direction
SOURCE_GERM_PHYS_V005_VALID = false | TYPE-R
BATTERY_V005 = 10_PASS / 3_CONDITIONAL_TYPE_U / 1_FAIL
```

Accordingly this artifact records the attempted minimal successor and its
failed certificate. It does not install v005, alter the U1 involution, add a
character-dependent sign, or modify the principal's required tensor.

## 1. Scope, currency, and exact authority

### 1.1 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha_supervision
/Users/bgm/MB Work/alpha-program-archive/workspace  [mirror destination only]
```

The following load-bearing artifacts were read at source:

| Authority | SHA-256 | Use |
|---|---|---|
| `DECISION_OF_RECORD_014_AMENDMENT_1_CB_DERIVED_PAIRING_2026-08-02_V001.md` | `8191feb4316ddeb08ef832b644c41847b31698224f6ab16b65dc1e1e2a574e56` | required pairing and unchanged-falsifier condition (`:4-25`) |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md` | `d4cdbb6623797df6accb7dc9b24134d179bfc8e8d039c585d5c91ae23255869e` | live germ, derivative interface, and battery (`:90-122,338-402`) |
| `STAGE8_TASK4A_DOOR_D_FALSIFIER_CARRIER_AND_CHECK_DIAGNOSIS_V001.md` | `b105a2c9f769c19bad420e4cbc71a23e4fcb5dcc4fc2365a825c331fad1eac97` | exact tensor necessity (`:255-303`) |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U1_DOR008_ASSEMBLY_DETERMINATION_V001.md` | `1b0e928c452c10a8be72be22ff81fd7677f5045d2ad8d398a9f7f7f57b9ab3b0` | anti-linear source involutions and U1-real source domain (`:230-264,322-347,515-528`) |
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md` | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | physical quotient, A4/A6 carriers, and Door D |
| `STAGE8_FIELD_SIGNATURE_PHYS_V005_THIRD_PASS_ADVERSARIAL_REVIEW_DETERMINATION_V001.md` | `c2251ed0e903ef4a0841e4008c1da612a41c57ef6778eff42dea00629a9fc1b1` | W3 adjoint-restriction precision (`:443-487`) |
| `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md` | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | raw-domain reality and same-correlator requirements (`:639-673`) |

The settled-question register head at construction start was Q-301, SHA-256
`37858be7b6162da6fc8ec020342ce5badf8840d9385a3a05b7679418a436705c`.
The send-time recheck returned the same Q-301 head and the same hash; no later
bearing entry exists.

### 1.2 Exclusions

```text
a32_holdout/custodian_private/               NOT ENTERED
physical parameter or rank-member selection  NOT PERFORMED
response value, coupling, scale, or root      NOT EVALUATED
measured-constant comparison                  NOT PERFORMED
register, tracker, plan, git, commit, push    NOT TOUCHED
```

### 1.3 Symbol distinctions

1. `L_n^Theta` is the accumulated **linear source covector**. It is not the
   connection-incidence map also denoted `L_N` in field-signature documents.
2. `b_n=i hbar L_n^Theta tensor L_n^Theta` is the amended symmetric bilinear
   pairing. It is not the void same-cell trace `Q_delta^Theta`.
3. `Theta_R` is the anti-linear CTP source involution. It is not the operator
   adjoint `sharp`, and W3's adjoint restriction maps do not replace it.
4. `R` is the symmetric bilocal source. Its letter does not mean “retarded.”

## 2. Exact minimal diff from v004

Only the following clauses are candidates for change.

### 2.1 Base tuple and authorship count

Replace the void `C-B` coordinate in the v004 base by the derived certificate:

```text
b_base^005 := (A0,Tr_A,P_0,P_ch,n,
               C-A,TensorCert_L,D_src,topology_src,Diff_src,
               source restriction and zero-extension data).
```

`TensorCert_L` is a theorem from the required pairing, not an authored
coordinate. The number of authored germ choices would therefore fall from
two to one, with C-A the sole survivor.

### 2.2 Pairing and bilocal functional

Transport the live covector to the ratified physical source carrier:

```text
ell_n:=L_n^Theta compose K_J^(-1) in (J_phys^005)^*.
```

Define on the complete physical carrier:

```text
b_n:=i hbar ell_n tensor ell_n
    in Bil_cont(J_phys^005 x J_phys^005;C).           (SG5-4)
```

The A6 field representation identifies bounded symmetric bilinear forms with
continuous functionals on its trace-class symmetric source through the
standard bounded/trace-class dual pairing. Denote that functional by

```text
Q_n^L(R):=<b_n,K_R(R)>_(Bil,S_1),
Q_n^L(f symtensor h)=b_n(f,h)                        (SG5-5)
```

on every finite rank-one source. No kernel, scale, contact, or additional
pairing datum is introduced.

### 2.3 Attempted germ clause

The exact requested replacement of v004 `SG4-1` is

```text
Xi_[A],n^005[J,R]
  :=L_n^Theta(J)-(1/2)Q_n^L(R),

Z_[A],n^005[J,R]
  :=(1-p_[A])+p_[A]exp(Xi_[A],n^005[J,R]),

W_[A],n^005:=-i hbar Log_0 Z_[A],n^005.              (SG5-6)
```

All A0 rank-family, Gen_Omega, anchor/transient quotient, same-rank gauge,
topology, logarithm-branch, no-selection, and no-supplementation clauses are
unchanged.

## 3. Explicit tensor precertificate

Fix a character label and an admitted physical source component.

### 3.1 Existence, uniqueness, and boundedness

Because `ell_n` is a bounded covector on the ratified A4 Hilbert/source norm,

```text
|b_n(f,h)|
 <= |hbar| ||ell_n||^2 ||f|| ||h||.
```

Thus (SG5-4) is a continuous symmetric rank-one form. The Q-301 reduction
proves uniqueness: if the same-correlator identity holds for every `f,h`, its
bilocal pairing must equal (SG5-4) pointwise. No member is selected.

### 3.2 Physical quotient

If `v` is in the physical source kernel, then the descended covector obeys
`ell_n(v)=0`. Therefore

```text
b_n(v,h)=b_n(h,v)=0
```

for every `h`. The form descends through the Gate-4/path-invisible quotient.
This does not restrict the admitted physical source family.

### 3.3 Finite restrictions and W3 adjoints

For an isometric inclusion `i_NM:C_N->C_M`, W3 fixes
`rho_MN=i_NM^*`. Put

```text
ell_N=ell_M compose i_NM,
b_N=i_NM^* b_M i_NM
   =i hbar ell_N tensor ell_N.                       (SG5-7)
```

Then for `N<=M<=K`, functoriality of adjoints gives the full commuting
restriction square. This is not naive edge truncation. On the trace-class
source, the corresponding corner is `R_N=i_NM^* R_M i_NM`, and trace duality
gives `Q_N^L(R_N)=Q_M^L(i_NM R_N i_NM^*)`.

### 3.4 Tail and class account

Finite sources are dense in the A4/P2 norm classes. Since `b_n` is bounded,
its values are fixed by the finite core. The construction creates no
restriction-invisible source or Door-D tail.

```text
TENSOR_PRECERTIFICATE_WELL_DEFINED = true | TYPE-P |
  premises: DoR-014 as amended, DoR-015 A4/A6
TENSOR_PRECERTIFICATE_QUOTIENT_COMPATIBLE = true | TYPE-P |
  premises: same
TENSOR_PRECERTIFICATE_RESTRICTION_NATURAL = true | TYPE-P |
  premises: same
TENSOR_PRECERTIFICATE_W3_ADJOINT_COMPATIBLE = true | TYPE-P |
  premises: same
TENSOR_PRECERTIFICATE_CREATED_TAIL = false | TYPE-R |
  test: bounded finite-core determination
```

## 4. Exact derivative check at fixed character

Write

```text
q:=p_[A]exp(Xi^005)/Z^005.
```

Direct differentiation gives

```text
D_J W[f]             =-i hbar q L(f),
D_J Abar[f,h]        =-i hbar q(1-q)L(f)L(h),
2D_R W[f symtensor h]= i hbar q b(f,h),
Abar(f)Abar(h)       =-hbar^2 q^2 L(f)L(h).
```

Using `b=i hbar L tensor L`,

```text
G(f,h)
 :=2D_R W[f symtensor h]-Abar(f)Abar(h)
 =-hbar^2 q(1-q)L(f)L(h),

(i/hbar)G(f,h)
 =-i hbar q(1-q)L(f)L(h)
 =D_J Abar[f,h].                                      (SG5-8)
```

An independently coded exact coefficient check compared the coefficients of
`q` and `q^2` and returned equality. It also returned equality after the
cycle substitution `L(f)=0`.

## 5. Mandatory U1 kill-pass

The amendment says all DoR-014 falsifiers remain. V004 inherits the exact
reality relations

```text
L_(-n)^Theta(Theta_J f)=conjugate(L_n^Theta(f)),
Q_(-n)(Theta_R R)=conjugate(Q_n(R)).                 (SG5-9)
```

The second relation is required so that
`Xi_(-n)(Theta_src s)=conjugate(Xi_n(s))`, and hence the scalar germ and its
anchored logarithm have the ratified CTP reality.

Apply the amended rule to `R=f symtensor h`:

```text
Q_(-n)^L(Theta_R R)
 =i hbar L_(-n)(Theta_J f)L_(-n)(Theta_J h)
 =i hbar conjugate(L_n(f))conjugate(L_n(h)),

conjugate(Q_n^L(R))
 =-i hbar conjugate(L_n(f))conjugate(L_n(h)).        (SG5-10)
```

They differ by sign. Charge/flux access supplies admitted directions for
which both linear factors are nonzero, so the contradiction is not confined
to the zero form. Equations (SG5-9) and (SG5-10) can coexist only if the live
linear source form vanishes identically, which is excluded by the same access
requirement used to derive the amendment.

The independent exact sign check returned coefficients `+i` and `-i`.

```text
AMENDED_PAIRING_THETA_REAL = false | TYPE-R
AMENDED_XI_THETA_REAL = false | TYPE-R
AMENDED_Z_U1_REAL_AT_NONZERO_R = false | TYPE-R
U1_SOURCE_DOMAIN_REQUIREMENT_PRESERVED = false | TYPE-R
```

No repair is installed. Changing the involution, the tensor coefficient, the
character rule, or the same-correlator normalization would exceed the ordered
minimal diff and requires a new principal disposition.

## 6. Fresh 14-row battery

Rows touched by C-B are re-proved here. Unaffected rows are rechecked against
the exact unchanged clauses rather than silently credited.

| Row | V005 verdict | Fresh certificate / residual condition |
|---|---|---|
| B1 finite restriction | **FAIL / TYPE-R** | `R=0` restrictions still reproduce the sealed amplitude, but an admitted finite nonzero-`R` source violates the ratified U1 restriction by SG5-10. |
| B2 Q-243 finite retarded baseline | **PASS / TYPE-P** | At `R=0` the amended term vanishes; the exact J-Hessian and zero ordered block are unchanged. |
| B3 finite retarded restrictions | **PASS / TYPE-P** | Stagewise consequence of B2 under W3 adjoint restrictions. |
| B4 extension mechanism | **PASS / TYPE-P** | The tensor form is bounded and finite-core determined in the ratified A4/A6 norm classes; no naive extension is used. |
| B5 named separation class | **CONDITIONAL / TYPE-U** | would-build: physical `RetHess_phys` class and injective representation. |
| B6 explicit tail | **CONDITIONAL / TYPE-U** | would-build: physical `Tail_R` and a germ-to-physical-tail theorem. |
| B7 modulo-tail determinacy | **PASS / TYPE-P** | The amended bounded tensor is determined elementwise by its finite corners. |
| B8 finite-visible quotient | **PASS / TYPE-P** | symbolic `p_[A]` and ordered rank data are unchanged; none is evaluated. |
| B9 consumer tail certificate | **CONDITIONAL / TYPE-U** | would-build: six consumer-specific factorization certificates. |
| B10 stationary point | **PASS / TYPE-P** | No stationary point or background is inferred. |
| B11 C1/evaluation | **PASS / TYPE-P** | Zero source remains normalization/restriction data, not an evaluation rule. |
| B12 zero surfaces | **PASS / TYPE-P** | Holonomy zero, source zero, and difference-field zero remain distinct. |
| B13 finite authority | **PASS / TYPE-P** | The amended pairing has explicit finite corners and no invisible component. |
| B14 provenance | **PASS / TYPE-P** | `b` uses only the pre-existing `L`; no pairing datum is added after output and the Gen_Omega descent is unchanged. |

```text
BATTERY_V005_PASS_COUNT = 10
BATTERY_V005_CONDITIONAL_TYPE_U_COUNT = 3
BATTERY_V005_FAIL_COUNT = 1
```

The 14-row table does not clear the germ: B1 is a load-bearing finite/U1
failure, and the raw-map domain independently requires a fixed CTP reality
involution.

## 7. Exact changed-clause and inheritance ledger

| V004 clause | Attempted V005 disposition |
|---|---|
| base tuple `C-B` | voided and replaced by derived `TensorCert_L` |
| `Q_delta^Theta` | replaced by `Q_n^L`, the trace-dual of `i hbar L_n tensor L_n` |
| `Xi`, `Z`, `D_R Z` formulas | mechanically changed by `Q_delta^Theta -> Q_n^L` |
| authored germ-choice count | reduced by one |
| raw same-correlator certificate | newly passes at fixed character |
| U1 reality certificate | **fails; no inheritance** |
| A0 rank family and quotient | unchanged |
| Gen_Omega descent | unchanged |
| C-A topology and calculus | unchanged |
| anchor/transient and same-rank quotients | unchanged |
| no-selection/no-supplementation clauses | unchanged |
| B5/B6/B9 | unchanged `TYPE-U` |

This is the complete intended diff. No other clause was edited or silently
reinterpreted.

## 8. Final ledger

```text
DOR014_AMENDMENT1_PAIRING_DERIVED = true | TYPE-P |
  premises: DoR-014 as amended
NEW_PAIRING_CHOICE_ADDED = false | TYPE-R |
  test: b is pointwise forced by the same-correlator identity
EXPLICIT_TENSOR_PRECERTIFICATE_BUILT = true | TYPE-P |
  premises: DoR-014 as amended, DoR-015

FIXED_CHARACTER_SAME_CORRELATOR_IDENTITY = PASS
W3_ADJOINT_RESTRICTION_SQUARE = PASS
PHYSICAL_QUOTIENT_DESCENT = PASS

U1_REALITY_CERTIFICATE = FAIL | TYPE-R
SOURCE_GERM_PHYS_V005_VALID = false | TYPE-R
SOURCE_GERM_PHYS_V005_INSTALLED = false | TYPE-R

WOULD_BUILD_AFTER_FAILURE = U1_REAL_TENSOR_PAIRING_COMPATIBILITY_DISPOSITION |
  standing: TYPE-U as an object; the current conjunction is refuted TYPE-R |
  must disposition at least one of: fixed U1 source involution,
    exact tensor coefficient, character transformation, or raw identity |
  no option selected here

SELECTED_ANCHOR_TORSOR_INTERTWINER_RANK_MEMBER_FOUND = false | TYPE-S |
  roots: attempted v005 definitions and proofs |
  exclusions: arbitrary finite test directions are witnesses, not selections |
  fences: full family retained |
  query: selected member or evaluated rank

UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S |
  roots: tensor, trace-dual, and restriction constructions |
  exclusions: physical inverse and retarded classes not formed |
  fences: W3 and Q-288 accounting |
  query: unnamed completion, weak-star, bidual, distributional, tail

REGISTER_HEAD_AT_SEND_TIME = Q-301 |
  register_sha256=37858be7b6162da6fc8ec020342ce5badf8840d9385a3a05b7679418a436705c |
  later_bearing_entry_found=false | TYPE-S |
  roots: QUESTIONS_SETTLED_REGISTER_V001.md after Q-301 |
  exclusions: DoR-014 Amendment 1 already consumed as governing authority |
  fences: send-time currency check |
  query: any later Door-D, C-B, tensor-pairing, or U1 disposition

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

**AMENDMENT-EXECUTION DRAFT — FAILED U1 CERTIFICATE; NOT INSTALLED**
