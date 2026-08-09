# STAGE 8 / 7A / [PLAN:B1a-9] — DIVERGENCE LOCATED: THE 802 MAP APPLIED THE WRONG FRAME CONVERSION

Lane: CODEX 2. Relay 805. All headline determinations are **CLAIMED** pending registrar cross-check.

## Lead determination

The relay-802 certificate is withdrawn. Its exact-arithmetic elimination was internally consistent with the matrix it assembled, but that matrix was not the sealed local-component receiver. The implementation formed

```text
L_802,p = W_p^(-T) B_p.
```

Here `B_p` had already been defined and built as the coordinate-component map. The extra `W_p^(-T)` was therefore a second frame conversion, with the transpose on the wrong variance as well. The identity control rejects in all 24 blocks under `L_802`; it passes exactly after the erroneous factor is removed. This is an implementation/representation bug, not a lawful-reading dispute.

The corrected A2 system is nonempty. Using Dario 804's independently rebuilt exact Gram data, the identity point lies in a positive-dimensional Gram-completion family: the exact algebraic dimension of the corrected A2 solution set is `243`. No dimension is claimed here for additional, not-yet-jointly-instantiated cross-generator carrier equations.

## 0. Preflight, pins, and custody

| object | SHA-256 | custody result |
|---|---|---|
| `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | digest and adjacent seal verified; read before task work |
| subject 802, `STAGE8_B1A_FULL_SPACE_SOLVE_CODEX2_V001.md` | `520a3fa2391be8876584c6b4360aef4a1357bffefd2395d357dad2f876441d44` | adjacent seal verified |
| governing 804, `STAGE8_B1A_CERTIFICATE_VERIFY_DARIO_V001.md` | `0267098a2372171a36e116f1a802f95a506388c2caf386a6b5d98f188e70863d` | adjacent seal verified before reading |
| 797, `STAGE8_B1A_FULL_SOLUTION_SET_CODEX2_V001.md` | `78882cbe04c460bf7a7000277e3d24048c4639d3cdcaa6e37dd04050a8bfb5d9` | adjacent seal verified |
| 795, `STAGE8_B1A_COFRAME_HALF_DARIO_V001.md` | `590b3979d5a0fadfd570e3a73a13bb3a717d5450f7eb5c9f2e79f481039fc1e2` | adjacent seal verified |
| packet `review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` | packet-manifest membership verified |

Decisive sealed spans:

| content | sealed span | span SHA-256 |
|---|---:|---|
| 802 equation `(I) M-LS=0` and exact counts | 802 `[3641,4247)` | `d1a976b62595884a8351c04ed139aac940f47565b24c075e2e8be694f2b23b0f` |
| 797 definition of `B` as the coordinate-component map | 797 `[5864,6994)` | `0fde68695d414ae5f5f762a1aba6cdf05e31f8dc9a8f6dbcb173dc05d85b8458` |
| 795 component-inheritance identity and quadratic | 795 `[4903,7018)` | `72c1e849dbf8a53e73669c8500bf00f3b26013bcae02dab1e67f1017229c9ca4` |
| packet V011 general-coframe pull-through rule | packet V011 `[46074,46387)` | `dffd13b31d56c212bb69a86ff522600f0b95b5f229dd702f0e9886c96edc8c43` |
| 804 exact identity exhibit | 804 `[513,3683)` | `68d9c11804ec66ad6546a089957c2ad827f91ced68333f7dd2ccc0d7db2ac0e6` |

The exact 802 construction below was recovered from the local execution record for that turn. That execution record is not used as authority; this sealed report publishes the construction so it is now reproducible and reviewable. PE-1 through PE-7 were pointer-known only, unopened, unconsulted, and carry zero weight.

## 1. AS1 — exact publication of the `L` used in 802

### 1.1 Ordered bases

All arithmetic is over `Q`.

```text
vertex order:       lexicographic order on {0,1}^4
edge order:         lexicographic pairs (u,v), u<v, with u_i <= v_i for i=0..3
edge count:         65
bivector order:     (01,02,03,12,13,23)
simplex order:      lexicographic permutations p of (0,1,2,3)
simplex count:      24
```

For a permutation `p`, set `v_0=(0,0,0,0)` and

```text
v_(k+1) = v_k + e_(p_k),       k=0,1,2,3.
```

Let `A_p` be the `5 x 5` matrix whose row `i` is `(1,v_i)`. If `A_p^-1=(a_rs)`, define the barycentric gradients

```text
g_i^mu = (A_p^-1)_(mu+1,i),    i=0..4, mu=0..3.
```

The exact `6 x 65` block `B_p` used in 802 is

```text
(B_p)_((mu,nu), edge(v_i,v_j))
  = 2 (g_i^mu g_j^nu - g_i^nu g_j^mu),    0 <= i < j <= 4,
```

and zero on global edges not in that simplex. The factor `2` is the complete normalization in `B`; no further scalar was applied. This is exactly the 797 formula that calls `B` the map to the six constant coordinate-curvature components.

Let `E_p` have rows `v_1,v_2,v_3,v_4`, and define, with both row and column pairs in `(01,02,03,12,13,23)` order,

```text
(W_p)_((i,j),(mu,nu))
  = E_(i,mu) E_(j,nu) - E_(i,nu) E_(j,mu).
```

Thus `W_p` maps coordinate two-form components to the six oriented child-frame face components.

### 1.2 The quotient basis and the exact erroneous map

Stack the 24 blocks `B_p` in simplex order and perform exact left-to-right RREF on the 65 columns. The 50 pivot edge indices, zero-based in the edge order above, are

```text
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,22,23,24,
 25,26,27,29,30,32,33,34,35,36,37,39,40,42,43,46,47,48,49,50,
 51,53,54,56,57,60,61].
```

Write `B_p^H` for restriction to those 50 columns. The matrix actually used in 802 was

```text
L_802,p = transpose(inverse(W_p)) B_p^H,
L_802   = vertical_stack_p L_802,p,              shape 144 x 50,
G_802   = (1/24) L_802^T L_802.
```

This is an exact generating rule for every entry. For an additional byte-level reproducibility control, encode each rational as the string `n` or `n/d`, matrices in row-major order, and tight JSON with no trailing newline. Then

```text
SHA256(canonical B^H)     = fc1137dc91c035dbb9d5b5bc3153809092f44092570078f42cb08729f0b52155
SHA256(canonical L_802)   = e6a7df6445d5fa898b15a33d4270648c97b0eb4bb5295800e39955815505e057
```

No determinant weight, orientation sign, optimizer, threshold, or floating approximation appears.

## 2. AS2 — identity test in the 802 system

For each ordered pair `(mu,nu)`, use the exact constant-form edge representative

```text
a_(mu,nu)(u,v)
  = (1/2) [u_mu (v_nu-u_nu) - u_nu (v_mu-u_mu)].
```

Direct exact substitution gives

```text
B_p a = I_6                  for every one of the 24 children,
C a   = I_6                  for the 1/4 average over the four parallel parent faces.
```

Therefore the lawful coordinate-component receiver `L_p=B_p` accepts `M_p=I_6` exactly. But 802's assembled receiver returns

```text
L_802,p a = W_p^(-T).
```

For the first simplex `p=(0,1,2,3)`, the exact block is

```text
W_p^(-T) =
[ 1 -1  0  1  0  0 ]
[ 0  1 -1 -1  1  0 ]
[ 0  0  1  0 -1  0 ]
[ 0  0  0  1 -1  1 ]
[ 0  0  0  0  1 -1 ]
[ 0  0  0  0  0  1 ].
```

Hence equation `(I) M-LS=0` has the nonzero residual

```text
I_6-W_p^(-T) =
[ 0  1  0 -1  0  0 ]
[ 0  0  1  1 -1  0 ]
[ 0  0  0  0  1  0 ]
[ 0  0  0  0  1 -1 ]
[ 0  0  0  0  0  1 ]
[ 0  0  0  0  0  0 ].
```

All `24/24` child blocks reject. The rejecting equation is 802 equation `(I)`, sealed at 802 `[3641,4247)`; the intended identity/component-inheritance law is sealed at 795 `[4903,7018)`, and the general-coframe conversion law is packet V011 `[46074,46387)`.

Equations `(II)` and `(III)` do not reject the witness:

```text
C a = I_6,
(1/24) sum_p I_6^T I_6 = I_6.
```

The failure is isolated to the left side of `(I)`.

## 3. AS3 — exact divergence from 804

The exact divergence is the composition of two incompatible representations:

1. 797 defines and 802 builds `B_p` using barycentric gradients as a map to **coordinate components**.
2. The code then treats that output as though it were a child-frame flux carrier and applies `W_p^(-T)`.
3. With the displayed index convention, child-frame flux is `Phi_p=W_p F`. Pulling it back to coordinate components is `W_p^-1 Phi_p=F`, not `W_p^-T F`.
4. Because `B_p` already returns `F`, the direct lawful receiver is simply `L_p=B_p`. Equivalently, if one first constructs frame-face flux `Phi_p=W_p B_p`, the lawful pullback is `W_p^-1 Phi_p=B_p`.

So `W_p^-T B_p` is neither lawful route. It is a duplicated frame conversion and a transpose/variance error. That is the exact implementation bug that created 802's anisotropic `G_0` and false positive excess.

This accounts for every directional fact in 804:

- 802's arithmetic reproduces exactly once the wrong `L` is supplied;
- the sign pattern can survive because the same Freudenthal symmetry remains;
- the diagonal/off-diagonal and isotypic ratios change because `W_p^-T` injects a non-orthogonal anisotropy;
- Dario's exact identity exhibit is rejected only by the erroneous `(I)` carrier;
- removing that carrier error makes the obstruction disappear.

There is no competing sealed-span reading under which the 802 map is right. I withdraw the 802 `UNSATISFIABLE` certificate and its downstream short-circuit.

## 4. AS4 — corrected solution-set status

### 4.1 Nonempty and not isolated

Dario 804 supplies an exact member: the constant-form lift with `M_p=I_6`. Its rebuilt minimum has

```text
F_*^T G_0 F_* = 11/56,
```

and its two exact `S_4`-isotypic eigenvalues have ratio `7/12`. Since `G_0` is positive definite and `||F_*||^2=2`, these exact data put both eigenvalues strictly below `1`; consequently

```text
R := I_6-G_0
```

is positive definite, hence rank `6`.

Now use the same exact orthogonal decomposition as 802, but with lawful `G`:

```text
S = S_0+N,          C N=0,
N^T G N = R,
dim ker C = 44.
```

In exact `G`-orthogonal coordinates on `ker C`, this is the generalized Stiefel equation

```text
Y^T Y=R,            Y in Mat_(44 x 6).
```

Because `R` has rank `6`, the 21 symmetric equations have full differential rank at every full-rank solution, including the identity exhibit. Therefore

```text
dimension = 44*6 - 6*7/2 = 264-21 = 243.
```

The identity law is not isolated. It is one exact rational member of a `243`-dimensional algebraic family in the corrected A2 linear-law block. The corresponding `M` is determined by `M=LS`, so adjoining `M` does not change that dimension.

This dimension is for the A2 block whose alleged emptiness was used by 802 to short-circuit the joint problem. The full cross-generator intersection remains **NONEMPTY by the 804 identity exhibit**, but this relay does not assign a dimension to further A0/A1/composition/common-refinement carriers that have not been supplied as one exact common matrix system.

### 4.2 Independent exact control in the published 802 basis

As a control, deleting only the erroneous `W_p^-T` from the now-published 802 construction gives

```text
G_0 =
[ 325/444  -15/296  -15/296   15/296   15/296         0 ]
[ -15/296  325/444  -15/296  -15/296         0    15/296 ]
[ -15/296  -15/296  325/444         0   -15/296  -15/296 ]
[  15/296  -15/296         0   325/444  -15/296   15/296 ]
[  15/296         0   -15/296  -15/296  325/444  -15/296 ]
[        0    15/296  -15/296   15/296  -15/296  325/444 ].
```

The exact no-pivot LDL diagonal of `I_6-G_0` is

```text
[119/444, 54619/211344, 7913/31413, 283/1158, 39032/163857, 82/357],
```

all positive. This independently gives the same rank-6 completion and dimension `243`. It is a control under the explicitly published coordinate-component convention, not a new law selection and not a replacement for 804's separately stated convention.

## 5. Freedoms consumed

| datum | status |
|---|---|
| `L_802` | **PUBLISHED AS THE REJECTED INSTRUMENT**, not adopted |
| corrected `L=B` control | **TESTED AS THE COORDINATE-COMPONENT READING**, not adopted as program law |
| law entries `M_p` | **CARRIED AS VARIABLES**; `M_p=I_6` is a refutation witness, not a selected member |
| lift `S` | **CARRIED AS VARIABLE**; constant-form lift used only for the identity control |
| parent two-form | **CARRIED SYMBOLICALLY** over `Q`; no physical value evaluated |
| A2 representative | Freudenthal receiver already in subject scope; no cellulation adopted or eliminated |
| `C` aggregation | 804's stated `1/4` face average used for the control; no hidden convention |
| coframe frames and orientations | derived sealed inputs; no freedom spent |
| metric or compensator | none introduced or adopted |
| smooth constituent | not imported; S26 remains barred |
| electromagnetic identification | none; S08 remains intact |

`SUBSTITUTED = none.` The identity exhibit is diagnostic evidence against a universal negative, not member binding.

## 6. Flattening, gates, and verb audit

`FLATTENING_CHECK = clean.` The finite cochain and bivector-coordinate calculation is not identified with a smooth public field or electromagnetism. No smooth constituent is imported. No member, law, metric, cellulation, or compensator is selected by outcome. The control changes no program board, seal, or authorization state.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member binding = none
fixed-point execution = none
end test = none
numeric evaluation of physical quantities = none
comparison to measured constants = none
smooth import = none
EM identification = none
exact arithmetic only = true
```

Self verb audit: **NOT CLEAN — two disclosures.** First, 802 described `L` only in prose while the computation used the unpublished `W_p^-T B_p`; that made the certificate non-reproducible from its artifact. Second, 802 did not run the identity control before sealing `UNSATISFIABLE`. The missing control would have rejected all 24 blocks immediately. Both defects are displayed and the prior verdict is withdrawn here.

L_PUBLISHED = exact (displayed)
IDENTITY_TEST = rejected by equation (I) `M-LS=0`, 802 `[3641,4247)` (802 defect located: duplicated, transposed frame conversion `W_p^-T B_p`)
DIVERGENCE = located (implementation/representation bug at `L` assembly: `B_p` already returns coordinate components; the added `W_p^-T` is unlawful)
CORRECTED_STATUS = NONEMPTY; identity is one point of a family of exact algebraic dimension 243 in the corrected A2 linear-law block (full cross-generator dimension not assigned)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+2 items: unpublished unlawful `L`; missing identity control)
