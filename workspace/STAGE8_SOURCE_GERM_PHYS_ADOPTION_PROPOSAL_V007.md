# Stage 8 SOURCE_GERM_PHYS v007 — derived source-to-output normalization install

**DERIVED INSTALLATION — FULL DOOR-D RELEASE CERTIFICATE PASSES**

Date: 2026-08-02  
Task: PASTE 388 / Task 4a  
Lane: CODEX LANE 2

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013,
                   DoR-014 as amended (2), DoR-015, C38

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Installation verdict

The source germ keeps the Amendment-2 source pairing unchanged:

```text
b_n^even = hbar L_n^Theta tensor L_n^Theta.
```

V007 installs one new **derived boundary map**, not a new source pairing:

```text
N_n(lambda b_n^even):=i lambda b_n^even.             (SG7-1)
```

Its domain is exactly the generated, Door-D-active source image
`E_n=span_C{b_n^even}`. Its codomain is the corresponding raw-output line
with the `Theta`-odd real structure. The two requirements force (SG7-1)
uniquely on that domain. No extension to the unused complement of `E_n` is
made or needed.

The resulting raw connected bilocal is

```text
G_n^007
 =i hbar q N_n(b_n^even)+hbar^2 q^2 L_n tensor L_n
 =-hbar^2 q(1-q)L_n tensor L_n,                      (SG7-2)
```

so

```text
(i/hbar)G_n^007
 =-i hbar q(1-q)L_n tensor L_n
 =D_J Abar_n.                                        (SG7-3)
```

The full Door-D vector is `(PASS,PASS,PASS,PASS)`. The C35 freeze therefore
lifts for the Door-D-dependent construction chain.

## 1. Currency, scope, and authorities

### 1.1 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha_supervision
/Users/bgm/MB Work/alpha-program-archive/workspace  [mirror destination only]
```

| Authority | SHA-256 | Use |
|---|---|---|
| `QUESTIONS_SETTLED_REGISTER_V001.md` through Q-305 | `520a79983a91c207689c85557d2845f5c88e9e2b6b9c348f29568a241f6dba40` | current standing |
| `STAGE8_TASK4A_DOOR_D_TRANSPORT_JACOBIAN_CTP_METRIC_AND_FACTOR_AUDIT_V001.md` | `0fcf42e8ca682c8e655f8d41a3e9b4713b3f45d1adc5be9e1743d2e05720b632` | exact residual `q[b-i hbar L tensor L]` and coefficient-neutral crossings |
| `STAGE8_TASK4A_RATIFIED_BILOCAL_INVOLUTION_REALITY_LAW_DETERMINATION_V001.md` | `323852e8835175c30d503f0383ef735405d8bc40a98109e09f5974e49c603c22` | even source / odd output parity |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V006.md` | `343117b7f75eba02725c6955086e5988116c51c1717d809b4822c0ba3110e4dd` | immediate base |
| `STAGE8_TASK4A_DOR014_AMENDMENT2_EVEN_PAIRING_FULL_DOOR_D_REEXECUTION_V001.md` | `bf74ee5be76c70c688c2becf04d1ca3ad127f79253001ac7c5b6dfb70cadddf1` | third firing and four-subtest machinery |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U1_DOR008_ASSEMBLY_DETERMINATION_V001.md` | `1b0e928c452c10a8be72be22ff81fd7677f5045d2ad8d398a9f7f7f57b9ab3b0` | anti-linear source involution |
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md` | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | physical quotient, cycle family, W3 |
| `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md` | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | raw-domain conditions |

No identity is transported beyond the named source.

### 1.2 Exclusions

```text
a32_holdout/custodian_private/                 NOT ENTERED
full bilocal-complement normalization          NOT INSTALLED
rank, anchor, torsor, cycle, or background     NOT SELECTED
inverse, root, coupling, or scale               NOT EVALUATED
measured-constant comparison                    NOT PERFORMED
register, plan, tracker, git, commit, push      NOT TOUCHED
```

### 1.3 Bearing distinctions

1. `b_n^even` remains the `Theta`-even source-slot tensor.
2. `N_n(b_n^even)` is the `Theta`-odd raw-output coefficient. It is not
   inserted back into the exponent.
3. The `i` in `W=-i hbar Log Z`, the sealed `i/hbar` in condition 6, and the
   derived `i` in `N` are owned by three different arrows.
4. `E_n` is the generated coefficient line in the bilinear dual. It is not
   the complete symmetric bilocal-source space.

## 2. Minimal diff from v006

The source functional is unchanged:

```text
Xi_n^007[J,R]=L_n^Theta(J)-(1/2)Q_n^even(R),
Z_n^007[J,R]=(1-p_[A])+p_[A]exp(Xi_n^007[J,R]),
W_n^007=-i hbar Log_0 Z_n^007.
```

The only new clauses are:

```text
E_n:=span_C{b_n^even},
O_n:=the same generated coefficient line with odd output real structure,
N_n:E_n->O_n,
N_n(lambda b_n^even)=i lambda b_n^even,
TensorNormCert_N:=the uniqueness, parity, quotient, and W3 certificate,
G_n^007:=i hbar q N_n(b_n^even)+hbar^2 q^2 L_n tensor L_n.
```

No field in v006's source exponent, rank family, Gen_Omega descent, topology,
calculus, logarithm, quotient, or authored choice table changes.

```text
V007_CHANGED_SOURCE_PAIRING = false | TYPE-R |
  test: byte-level formula comparison above
V007_ADDED_AUTHORED_FIELD = false | TYPE-R |
  test: N is fixed by the theorem, not selected
V007_INSTALLED_MAP_DOMAIN = E_active_only
```

## 3. TensorNormCert_N

### 3.1 Linearity and boundedness

For `x=lambda b_n^even`:

```text
N_n(x)=i x,
||N_n x||=||x||.
```

Thus `N_n` is complex-linear, bounded, invertible on `E_n`, and introduces no
normalization modulus or phase family.

### 3.2 Even-to-odd transformation

Let `C_E` denote the anti-linear partner transport induced by `Theta_R` on
the source line. Source evenness says

```text
C_E(b_n^even)=b_(-n)^even.
```

The required odd boundary law is

```text
N_(-n) C_E = - C_E N_n.                             (SG7-4)
```

On the generator:

```text
N_(-n)C_E(b_n^even)=i b_(-n)^even,
-C_E N_n(b_n^even)=-C_E(i b_n^even)=i b_(-n)^even.
```

Therefore `N` changes the real-structure parity without changing the source
slot's parity.

### 3.3 Quotient and cycles

If a source direction lies in `ker L_n`, `b_n^even` vanishes when that
direction occupies either slot. The map sends that zero to zero. It cannot
create a cycle value or select a cycle representative.

### 3.4 W3 naturality

For the retained isometric inclusion `i_NM` and its adjoint bilinear corner:

```text
b_N^even=i_NM^* b_M^even i_NM,
N_N(b_N^even)=i b_N^even
 =i_NM^* N_M(b_M^even)i_NM.                         (SG7-5)
```

Thus the normalization commutes with every W3 restriction square. The map is
skew-adjoint on its coefficient line, `N^*=-N`; W3 requires adjoint
restriction naturality, not self-adjointness.

### 3.5 Tail

`N` is a unit scalar map on a finite-core-separated generated line. It creates
no source or raw-output tail.

```text
N_COMPLEX_LINEAR = true | TYPE-P
N_BOUNDED_UNIT_FACTOR = true | TYPE-P
N_EVEN_TO_ODD_ANTI_INTERTWINER = true | TYPE-P
N_QUOTIENT_COMPATIBLE = true | TYPE-P
N_W3_NATURAL = true | TYPE-P
N_CYCLE_KERNEL_PRESERVED = true | TYPE-P
N_CREATED_TAIL = false | TYPE-R |
  test: finite-core-separated scalar action
```

## 4. Exact identity bookkeeping

Set `q=p_[A]exp(Xi^007)/Z^007`. The source derivatives are unchanged:

```text
Abar_n(f)=-i hbar q L_n(f),
D_J Abar_n(f,h)=-i hbar q(1-q)L_n(f)L_n(h).          (SG7-6)
```

At the source-to-output boundary:

```text
N_n(b_n^even)=i hbar L_n tensor L_n.
```

The raw connected output is therefore:

```text
2D_R W |_raw
 :=i hbar q N_n(b_n^even)
 =-hbar^2 q L_n tensor L_n,

Abar_n tensor Abar_n
 =-hbar^2 q^2 L_n tensor L_n,

G_n^007
 =2D_R W |_raw-Abar_n tensor Abar_n
 =-hbar^2 q(1-q)L_n tensor L_n.                     (SG7-7)
```

Finally:

```text
(i/hbar)G_n^007
 =-i hbar q(1-q)L_n tensor L_n
 =D_J Abar_n.                                        (SG7-8)
```

No `i` is double-billed:

| Factor | Owner | Role |
|---|---|---|
| `-i hbar` | `W` convention | source-functional derivative |
| `i` | `N` theorem | even source to odd raw coefficient |
| `i/hbar` | sealed condition 6 | raw output to same-correlator comparison |

## 5. Fresh source-germ battery

The original 14 rows have the following v007 standing:

| Row | Verdict | V007 certificate |
|---|---|---|
| B1 finite restriction | **PASS / TYPE-P** | N commutes with every finite bilinear corner. |
| B2 Q-243 baseline | **PASS / TYPE-P** | source germ and J-Hessian unchanged. |
| B3 finite retarded restrictions | **PASS / TYPE-P** | W3 naturality (SG7-5). |
| B4 extension mechanism | **PASS / TYPE-P** | bounded map on the generated line. |
| B5 named separation class | **CONDITIONAL / TYPE-U** | would-build: complete `RetHess_phys` class. |
| B6 explicit tail | **CONDITIONAL / TYPE-U** | would-build: complete physical `Tail_R`. |
| B7 modulo-tail determinacy | **PASS / TYPE-P** | N has no invisible component. |
| B8 finite-visible quotient | **PASS / TYPE-P** | ranks remain symbolic. |
| B9 consumer tail certificate | **CONDITIONAL / TYPE-U** | would-build: consumer-specific factorizations. |
| B10 stationary point | **PASS / TYPE-P** | no background is chosen. |
| B11 C1/evaluation | **PASS / TYPE-P** | zero source is not made an evaluation rule. |
| B12 zero surfaces | **PASS / TYPE-P** | source, history, and difference zeros remain distinct. |
| B13 finite authority | **PASS / TYPE-P** | N is determined and checked on every finite generator. |
| B14 provenance | **PASS / TYPE-P** | N descends from two requires and adds no datum. |

```text
SOURCE_GERM_INTERNAL_BATTERY_V007 = 11_PASS / 3_CONDITIONAL_TYPE_U / 0_FAIL
N_BOUNDARY_CERTIFICATE = PASS
```

## 6. Full Door-D certificate

| Door-D subtest | V007 verdict |
|---|---|
| bounded extension | **PASS / TYPE-P** |
| same-correlator identity on cycles | **PASS** |
| same-correlator identity on endpoint-covariant open paths | **PASS** |
| U1 reality under the ratified involution | **PASS / TYPE-P** |

Cycle directions pass because `L=0` there. Open directions pass by (SG7-8).
The source functional remains even; `N(b_even)` is odd; `G^007` is even; and
the sealed factor `(i/hbar)` makes its comparison output odd, matching the
J-Hessian.

```text
DOOR_D_SUBTEST_VECTOR = (PASS,PASS,PASS,PASS)
DOOR_D_EXECUTION = PASS
DOR015_FREEZE_LIFTS = true | TYPE-P
SOURCE_GERM_PHYS_V007_INSTALLED = true | TYPE-P
```

## 7. Version and restriction accounting

| Object | Standing after v007 |
|---|---|
| v004 C-B | void |
| v005 odd source pairing | superseded |
| v006 even pairing under direct identification | source part retained; direct identification refuted |
| v007 even pairing plus derived N | installed |
| Q-243 source/J rows | reproduced exactly |
| Q-279 source-germ rows | Amendment-2 rows unchanged and W3-natural |
| raw same-correlator finite square | passes at every finite stage |

`N` acts after source differentiation. It does not rewrite historical source
derivatives or back-label amended rows as the old C-B result.

## 8. Final ledger

```text
N_UNIQUENESS_ON_DOOR_D_ACTIVE_IMAGE = PROVED | TYPE-P
N_FORMULA = multiplication_by_i_on_E_active
N_EXTENSION_TO_UNUSED_BILOCAL_COMPLEMENT_INSTALLED = false | TYPE-S |
  roots: exact E_active domain |
  exclusions: complete symmetric bilocal complement |
  fences: C38 minimal-install discipline |
  query: arbitrary complement operator

SOURCE_PAIRING_REMAINS_THETA_EVEN = true | TYPE-P
RAW_OUTPUT_COEFFICIENT_IS_THETA_ODD = true | TYPE-P
SAME_CORRELATOR_IDENTITY = PASS
U1_REALITY = PASS
DOOR_D_EXECUTION = PASS
DOR015_FREEZE_LIFTS = true | TYPE-P

SELECTED_PHASE_OR_MAP_FOUND = false | TYPE-S |
  roots: uniqueness proof on the generated image |
  exclusions: no complement extension |
  fences: no-selection |
  query: selected phase, normalizer, rank, anchor, torsor, or cycle

UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S |
  roots: E_active, O_active, and bounded scalar normalization |
  exclusions: physical inverse and retarded classes |
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

**DERIVED INSTALLATION — SOURCE GERM v007 AND FULL DOOR D PASS**
