# STAGE 8 / 7A / STEP 8 — BRANCH-F CROSS-FAMILY CHECK

**Lane:** CODEX 2  
**Date:** 2026-08-08  
**Scope:** relay 737 only — recompute the three claimed locks and type the side condition  
**Charge:** instructed to refute; no branch is adopted here

## 0. Preflight, custody, and method

The relay was read only after its seal verified. The requested output name was absent
from both the cleanroom and the archive workspace before this write.

| Object | SHA-256 | Verification |
|---|---|---|
| relay 737 | `c072c33eafec70bf116d07313670d65c8f92475b4deadd03517721610c4ba13c` | sidecar `OK` |
| subject, `STAGE8_7A_XI_F_REQUIRE_HUNT_DARIO_V001.md` | `c434f392f286598264142777649b51ad463727aee62e70f5275535f8ea3f3c7b` | sidecar `OK` |
| packet V011 | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` | packet-manifest member |
| packet manifest | `9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311` | current sealed packet inventory |
| executed intrinsic-measure result | `e60aec3c44cfc5f1ef5715d3445e53783b0185ef93e54d94e442ff1df2ae9b59` | packet-manifest member |
| lineage-V2 matrix | `fe4c083d915c00824575fe6ae53339500a805f4c1fd0b5f3174a74fdb8c9dba8` | sidecar `OK` |
| exact family-A/B construction | `08b91543fdb72f656c756ca5f8df8233b87eb5487284c7fd2170cba67f7e0e3b` | sidecar `OK` |

All computations below use exact integer/rational arithmetic. No floating-point value,
physical quantity, or measured constant was evaluated. The Freudenthal check constructs
a countermodel consistent with the displayed finite cochain and coframe interfaces; it
does not adopt that countermodel as program content.

## 1. L1 — the intensive quadratic coefficient

### 1.1 Pinned source blocks

The packet manifest lists V011 with the whole-file digest above. The cited half-open
spans are in-bounds blocks of that packet member:

| V011 span | Span SHA-256 | Content |
|---|---|---|
| `[45718,46068)` | `1624f905e81ca375317deb628c1fa9815532072b4c616a33f62dbbe92a3721e6` | orthogonal-cell `V_cell`, `xi = ell ell F + higher-order terms`, and the positive face metric |
| `[46074,46387)` | `dffd13b31d56c212bb69a86ff522600f0b95b5f229dd702f0e9886c96edc8c43` | per-cell `V_cell sum F^2` conclusion and general-coframe map |
| `[47025,47247)` | `9ff6852634e78e6d886896c27bce16b4ec9e092620642a86bae00848df2f276c` | common-refinement commutation and the boundary/four-volume tolerance |

The last block says, exactly, that the response map must commute with pullback to a
common refinement and that the intensive quadratic coefficient must be invariant under
each elementary refinement up to a boundary term whose ratio to four-volume tends to
zero. It is therefore a requirement, not a commentary line.

### 1.2 Exact identity and anisotropic controls

For the displayed quadratic coefficient, set

```text
xi_(mu nu) = ell_mu ell_nu F_(mu nu).
```

Then, independently for every pair `(mu,nu)`,

```text
[V_cell/(ell_mu^2 ell_nu^2)] xi_(mu nu)^2 / V_cell
  = [xi_(mu nu)/(ell_mu ell_nu)]^2
  = F_(mu nu)^2.
```

The cancellation is term-by-term; summing does not create it. Three exact anisotropic
controls, with component order `(01,02,03,12,13,23)`, gave:

| `ell` | `V_cell` | `contribution/V_cell` | `sum F^2` | Equal |
|---|---:|---:|---:|---|
| `(2,3,5,7)` | `210` | `1623786649/901800900` | `1623786649/901800900` | yes |
| `(1/2,4/3,5/2,7/5)` | `7/3` | `1946957/1270080` | `1946957/1270080` | yes |
| `(3/2,5/4,7/3,11/2)` | `385/16` | `11659/6480` | `11659/6480` | yes |

This confirms the identity for the intensive **quadratic coefficient** extracted by
V011. It does not erase V011's written `higher-order terms`; those are outside this
coefficient and would need their own refinement bound. Within the claimed coefficient,
the invariance requirement is a requirement on the `F_(mu nu)` terms exactly.

**L1 verdict: CONFIRMED, at the quadratic-coefficient scope actually stated.**

## 2. L2 — both licensed moves

### 2.1 Cubical two-child bisection

For one nonzero component, let the parent face area be `A`, the parent four-volume
`V`, and `xi=A F`. A bisection into two equal subcells and two equal in-plane face
areas, with Branch-xi shares `s` and `1-s`, gives

```text
F_1 = (s xi)/(A/2)       = 2s F,
F_2 = ((1-s) xi)/(A/2)   = 2(1-s) F,

Q_refined = (V/2) F_1^2 + (V/2) F_2^2
          = V F^2 [1 + (2s-1)^2],

residual                 = V F^2 (2s-1)^2,
residual / V             = F^2 (2s-1)^2.
```

Three independent exact controls were:

| `ell`; `F`; `s` | Parent | Refined | Residual | Residual / `V` |
|---|---:|---:|---:|---:|
| `(2,3,5,7)`; `2/5`; `1/3` | `168/5` | `112/3` | `56/15` | `4/225` |
| `(1/2,4/3,5/2,7/5)`; `-3/7`; `2/5` | `3/7` | `78/175` | `3/175` | `9/1225` |
| `(3/2,5/4,7/3,11/2)`; `5/6`; `7/10` | `9625/576` | `11165/576` | `385/144` | `1/9` |

For `F != 0`, the residual vanishes exactly iff `s=1/2`. Since the subface area is
`A/2`, Branch F gives `xi_i=(A/2)F=xi/2`, hence precisely `s=1/2`. The zero-flux
sector is degenerate and cannot distinguish a share rule; it does not supply a
non-F rule on nonzero inputs. The tolerance block `[47025,47247)` excludes every
nonzero constant ratio displayed above.

**Cubical sub-verdict: CONFIRMED for the stated equal two-child bisection.**

### 2.2 Freudenthal move — exact non-F survivor

The other licensed move is not optional. The sealed construction at
`08b91543…[19632,19996)` (span SHA-256
`b3c67e8c433385a4cb519c2f564649e98b2a9686491487db663592b4b48d6b43`)
defines the oriented order-simplex/Freudenthal subdivision of the unit 4-cube into
24 simplices, each of exact four-volume `1/24`.

I reconstructed that complex directly:

```text
vertices                  = {0,1}^4                              (16)
4-simplices               = monotone chains for all S_4 orders  (24)
edges                      = 65
parent cube edges fixed   = 32
new diagonal/interior     = 33
```

Take the parent field `F=dx_0 wedge dx_1`, represented by the edge potential
`A=x_0 dx_1`. Fix its exact integral on all 32 parent cube edges. On each affine
4-simplex, reconstruct the affine Whitney 1-form from the 10 edge-cochain values,
apply `d_1'`, and evaluate V011's Euclidean general-coframe quadratic form. This is
an exact rational realization of `xi'=d_1'a'`; no face outside `im(d_1')` is used.

Writing the 33 free edge values as `x`, the resulting positive quadratic is
`E(x)`. Exact elimination gave:

```text
rank(Hessian(E))           = 33
E_min                      = 191/252
E(Branch-F edge values)    = 1
```

Let `x_min` be that unique rational minimizer and `x_F` the Branch-F values. The
reflection

```text
x_alt := 2 x_min - x_F
```

is rational and satisfies `E(x_alt)=E(x_F)=1` exactly, because the linear term
vanishes at `x_min`. It is not Branch F:

```text
22 of 33 new-edge values differ from x_F.

edge (0,0,0,0)->(0,1,0,1):  x_F=0, x_alt= 1/7
edge (0,0,0,0)->(1,0,0,1):  x_F=0, x_alt=-1/7
edge (0,0,0,0)->(0,1,1,1):  x_F=0, x_alt= 1/3
```

Its local component vector on the first simplex, in order
`(01,02,03,12,13,23)`, is

```text
(1, -43/84, -13/84, 43/84, 13/84, 0),
```

not `(1,0,0,0,0,0)`. Yet all 24 oriented coarse square-face fluxes reproduce
the parent values exactly, `xi'=d_1'a'` by construction, and

```text
sum_(24 simplices) (1/24) ||F_simplex||^2 = 1 = V_parent ||F_parent||^2.
```

Thus this non-F rule has zero quadratic residual on the Freudenthal elementary
move. It supplies neither an inserted compensator nor a residual scalar. This is
the explicit survivor the cubical-only calculation did not test.

**Freudenthal sub-verdict: REFUTED — a non-F exact cochain survives.**

Because relay 737 makes a surviving non-F simplicial rule a refutation of forcing,
**L2 verdict: REFUTED (cubical confirmed; Freudenthal refuted).**

## 3. L3 — the two cited bars and their object types

### 3.1 Spans and lineage are genuine

| Source + span | Span SHA-256 | Verified content |
|---|---|---|
| V011 `aa7c6d49…[46589,46710)` | `5273d94e8a92421359b9e8dd9a73e3e11114a7ed78f55b05155d11e4a8400100` | inverse weight, inserted compensator, or residual shape-dependent scalar fails A27 |
| R3.3 result `e60aec3c…[69,123)` | `299930a007a9134f21dd296c9a329ed54952541fb87e5530f7ff56f4084406af` | `INHERITED_REFINEMENT_NATURALITY_FORCES_UNIFORM_MEASURE` |
| R3.3 result `e60aec3c…[551,740)` | `fcc2db2591d172c912a071f9265fd39774ee2cb03061df2929bac4eb0a952b9b` | child intrinsic measure; no arbitrarily chosen parent weighting profile |

The lineage-V2 artifact records the complete D038 object at
`fe4c083d…[11039,11359)` and binds it to A27 at `[14891,14946)`:

```json
{"documents":["D002","D012","D013","D038"],"row":"A27"}
```

So the text, execution status, packet custody, and A27 lineage binding all verify.

### 3.2 The claimed mappings fail

The R7 bar is a bar on an inverse face weight, an inserted compensator, or a
**residual shape-dependent scalar in the response coefficient**. The exact
Freudenthal survivor changes a refined edge cochain and hence the local `F` values;
it inserts no scalar and leaves no residual coefficient at all. Calling every
cochain extension parameter a “shape-dependent scalar” changes the barred object's
type and is not licensed by the span.

The executed R3.3 result is narrower still. Its own displayed test compares the
parent-restricted and child-intrinsic normalized measures

```text
d mu_a proportional to [1+a u_cell(x)] d^4x,  a>=0,
```

and proves that only `a=0` survives. Its “weighting profile” is this measure profile.
A Branch-xi refinement chooses the new-edge 1-cochain `a'`, with
`xi'=d_1'a'`; it does not retain `u_parent`, `mu_parent,a`, or any parent-defined
measure density. The shared letter `a` is incidental: one is a scalar parameter in
a measure family, the other is an edge 1-cochain. Therefore the executed result
does not map onto the branch selector.

Branch F is compatible with intrinsic per-cell evaluation, but the executed
measure result does not prove it is the only cochain refinement compatible with
that evaluation. The Freudenthal survivor is an explicit counterexample to the
claimed exclusivity under the displayed coefficient.

### 3.3 Barred clause

V011 `[46882,47019)` (span SHA-256
`093ece5a5f70491ac2ed6ab7ccaf1b964eff8a81ac06e568c8b852616eb4f08c`)
includes common refinements “preserving the same smooth coframe and connection.”
The subject artifact explicitly did not use that clause, and this check does not
use it either. It was not load-bearing in the stated three-lock chain. If promoted
from barred target-interface data to a source premise, it could exclude the
piecewise non-F connection used in the countermodel; doing so would be exactly the
barred move, not a repair of R7 or R9.

**L3 verdict: REFUTED. The spans and lineage verify; the Branch-xi mappings do not.**

## 4. Side condition — exact type and sealed bearings

For a refined complex `K'`, let `D_(ell')` denote the tetrad/coframe integration map
from a local-frame two-form to the refined face-flux cochain. In the orthogonal
display it is

```text
(D_(ell') F)_(mu nu) = ell'_mu ell'_nu F_(mu nu).
```

The side condition is the finite linear-algebra statement

```text
xi' := D_(ell') F  in im(d_1': A_R^1(K') -> A_R^2(K')).
```

Equivalently, at least one refined real edge 1-cochain `a'` must exist with
`d_1'a'=xi'`; equivalently `z^T xi'=0` for every `z in ker((d_1')^T)`. To make this
a **refinement** of a particular parent rather than an objectwise membership test,
one additionally needs typed coarse/fine maps `J_1,J_2` satisfying

```text
d_1' J_1 = J_2 d_1,
J_2(D_ell F) = D_(ell') F',
```

plus the declared relation between `F'` and `F`. A path spelling alone is not such
a carrier.

Meaning-probes covered: `im(d_1)`/exact/coboundary preservation; subdivision or
refinement cochain maps; `d_1`-commuting squares; Whitney/de-Rham/prolongation terms;
coframe/connection preservation; and face-flux transport.

Sealed text bears on the type but does not discharge it:

1. V011 defines `F_phys=im(d_1)`, `xi=d_1a`, and refuses lifts outside that image.
   This fixes the membership target.
2. V011 gives both the orthogonal and general-coframe maps. This fixes
   `D_(ell')`, but not a refined edge preimage.
3. V011's early `J_1,J_2` are induced by an injective cellular map that sends a
   domain face to one target face. No sealed statement binds those maps to the
   coarse-to-Freudenthal subdivision used here.
4. Sealed signed-chain/cochain-pullback squares elsewhere establish naturality for
   their declared graph arrows, but none names this `K -> K'`, its `D_(ell')`, and
   the required face-flux square together. They are analogous machinery, not a
   carrier for this side condition.
5. The same-smooth-connection C_ref clause bears directly but is barred as a source.

Accordingly the general Branch-F side condition remains a **typed open carrier**.
It is not a reason to rescue Branch xi or to book Branch F. Notably, the explicit
Freudenthal survivor in §2.2 itself satisfies membership because it is constructed
as `d_1'a'`; membership alone does not restore forcing.

## 5. Verdict and audit

The first lock is sound at the stated quadratic-coefficient scope. The second lock
fails on the other licensed move: exact rational Freudenthal data exhibit a non-F
member with the same parent fluxes and identical coefficient. The third lock cites
genuine sealed text but applies it to the wrong object types. Therefore the claimed
three-lock forcing does not hold.

No common cell was formed, no junction map was evaluated, no member was bound, no
physical quantity was evaluated numerically, no measured constant was consulted,
and nothing was adopted. `CONFIRMED` is used only for reproduced identities or
pinned bytes; `REFUTED` is used only where the displayed counterexample or a typed
domain mismatch defeats the claimed implication; `OPEN` is used for the uncarried
side condition.

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

L1 = CONFIRMED
L2 = REFUTED (cubical confirmed; Freudenthal non-F survivor)
L3 = REFUTED
SIDE_CONDITION = typed (sealed bearings named; no discharging carrier)
OVERALL = FORCING REFUTED
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
