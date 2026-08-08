# STAGE 8 / 7A / STEP 8 — THE FULL CUBICAL FREE SPACE

**Lane:** CODEX 2  
**Date:** 2026-08-08  
**Scope:** relay 740 only — close the cubical scope flag in Q-645  
**Governing:** corrected verdict `c854c8b25dcc4e9e5bc2845925f9c197853aa9958f18cffb42c13b436cedc1e6`; cross-check `97587de8c7a468590cb150b54dae25e5d4aa132f82aa4ba6788062dc9220e049`

## 0. Preflight and exact interface

Relay 740 verified at
`083f3df8d058c6c144c2d446c78beb4b8691761634995653a0950b3d5b346976`.
The requested output name was absent from the cleanroom and archive before this write.
Both governing artifacts verified against their seal sidecars.

The sealed family-A construction is the bisection of the unit 4-cube into 16
subcubes of volume `1/16` each (`08b91543…[19632,19996)`). I used its full
`3 x 3 x 3 x 3` cubical grid. The calculation is exact rational structural
arithmetic; no floating point is used in any verdict step.

On each subcube, the cubical analogue of the 737 affine-Whitney reconstruction is
the tensor-product Whitney 1-form. For component `(i,j)`, its four parallel fine
plaquette fluxes form a vector `q_(ij,c)`. Exact integration over the two transverse
coordinates gives

```text
M = [[1/3,1/6],
     [1/6,1/3]],

E_L(a) = sum_c sum_(i<j)
           [V_c/(h_i^2 h_j^2)]
           q_(ij,c)^T (M tensor M) q_(ij,c),

q = d_1' a.
```

Every weight is positive. Thus `E_L` is positive definite on the refined flux
space `im(d_1')`; its only edge-space kernel is gauge.

## 1. VV1 — full configuration-space census

The exact cubical counts are

```text
vertices                         = 3^4 = 81
fine oriented edges              = 4 * 2 * 3^3 = 216
fine segments on parent edges    = 32 * 2 = 64
other fine edges                 = 216 - 64 = 152
```

Fixing a parent edge fixes the sum of its two fine segments, not either segment
separately. The 32 parent-edge equations are independent. Each pair of fine
segments therefore retains one split coordinate. Hence

```text
free affine edge coordinates = 152 + 32 = 184
                             = 216 - 32.
```

This includes every new edge and every boundary-edge split; no one-parameter
share ansatz is imposed.

### 1.1 Gauge kernel and exact rank

The fine cube is contractible, so `ker(d_1')=im(d_0')`. On 81 vertices,
`rank(d_0')=80`. A gauge perturbation preserves every fixed parent-edge sum iff
its vertex potential agrees at the endpoints of each parent edge. The 16 corner
vertices form a connected coarse cube, so this adds 15 independent equalities.
Consequently

```text
gauge nullity in the 184-dimensional tangent space = 80 - 15 = 65,
rank(E)                                             = 184 - 65 = 119.
```

This is an exact rank certificate. After quotienting gauge, `E` is a
positive-definite rank-119 quadratic.

### 1.2 An exact minimum certificate for the unit parent

Take parent `F=dx_0 wedge dx_1`, so `E_parent=E(x_F)=1`. A global fine plaquette
is indexed by its pair `(i,j)`, in-plane interval starts
`s_i,s_j in {0,1}`, and transverse grid coordinates `r_k,r_l in {0,1,2}`.
Define

```text
A = [[ 1/4,  -1/24,  1/4 ],
     [-1/24,  1/24, -1/24],
     [ 1/4,  -1/24,  1/4 ]],

B = [[ 7/48, -1/24,  7/48],
     [ 0,      0,     0   ],
     [-7/48,  1/24, -7/48]].
```

The following closed 2-cochain is the exact minimizing flux:

```text
q_01(s_0,s_1;r_2,r_3) = A[r_2,r_3],

q_0k(s_0,s_k;r_1,r_l) = (-1)^(s_k)   B[r_1,r_l],  k in {2,3},
q_1k(s_1,s_k;r_0,r_l) = (-1)^(s_k+1) B[r_0,r_l],  k in {2,3},

q_23 = 0,
```

where `l` is the remaining transverse axis. The exact certificate checks are:

```text
24/24 coarse square-face sums reproduce the parent flux;
96/96 oriented fine 3-cube d_2 q checks equal zero;
contractibility therefore gives q in im(d_1');
184/184 admissible edge-direction derivatives of E equal zero;
E(q) = 5/24 exactly.
```

Because the quadratic is positive on `im(d_1')`, feasibility plus zero gradient
proves global minimality. Thus, for the licensed unit family-A member,

```text
rank(E) = 119,
min(E)  = 5/24,
E(x_F)  = E_parent = 1.
```

The strict inequality `5/24 < 1` already rules out a single-point level set
through `x_F`.

## 2. VV2 — the equal-energy set and a verified witness

### 2.1 Dimension

On the 119-dimensional physical quotient, a positive-definite quadratic with
minimum below `1` has a level ellipsoid

```text
{E=1} ~= S^118.
```

In the unquotiented 184-dimensional edge space, the same set is the cylinder
`R^65 x S^118`, of total dimension 183. The verdict-relevant assignment freedom
is the **118-dimensional physical sphere**, not the 65 gauge directions.

### 2.2 A one-edge rational witness

Use integer grid coordinates `0,1,2`, corresponding to physical coordinates
`0,1/2,1`. Let

```text
e_* : (0,0,0,1) -> (1,0,0,1)
```

be the positive axis-0 edge. It is not a parent-edge segment: it lies at the
intermediate axis-3 coordinate. Keep every Branch-F edge value except

```text
x_alt(e_*) = x_F(e_*) - 3/8 = -3/8.
```

Along this direction the exact unit-cube polynomial is

```text
E(x_F + t e_*) = 1 + t/4 + (2/3)t^2.
```

At `t=-3/8`, the linear decrement `-3/32` and quadratic increment `+3/32`
cancel, so `E(x_alt)=1` exactly.

The evidence checks are structural, not inferential:

```text
24/24 coarse square-face flux changes = 0;

the four nonzero fine-plaquette changes are
  delta q_01 at (0,0,0,1) = -3/8,
  delta q_02 at (0,0,0,1) = -3/8,
  delta q_03 at (0,0,0,0) = +3/8,
  delta q_03 at (0,0,0,1) = -3/8;

xi_alt = d_1' x_alt, hence xi_alt in im(d_1');
d_1'(x_alt-x_F) != 0, hence the witness is not gauge.
```

This is a non-F, equal-energy, coarse-flux-preserving refined configuration in the
full cubical space.

### 2.3 Three anisotropic exact-rational controls

For parent extents `L=(L_0,L_1,L_2,L_3)`, parent `F_01=1`, and the same physical
edge direction, write `V=product L_i` and

```text
S = 1/L_1^2 + 1/L_2^2 + 1/L_3^2,

E_L(t) = V + 2 g_L t + q_L t^2,
g_L    = V/(8 L_0 L_1),
q_L    = [2V/(9 L_0^2)] S,
t_alt  = -2g_L/q_L.
```

All weights remain positive, so the rank remains 119. Three anisotropic controls
were:

| `L` | `E_F=V` | `g_L` | `q_L` | nonzero equal-energy `t_alt` | `E_L(t_alt)-V` |
|---|---:|---:|---:|---:|---:|
| `(2,3,5,7)` | `210` | `35/8` | `1891/945` | `-33075/7564` | `0` |
| `(1/2,4/3,5/2,7/5)` | `7/3` | `7/16` | `24161/9450` | `-33075/96644` | `0` |
| `(3/2,5/4,7/3,11/2)` | `385/16` | `77/48` | `126989/62370` | `-800415/507956` | `0` |

Each witness changes the same non-parent edge, so all coarse flux and
`im(d_1')` checks above remain exact. Since `g_L != 0` and `q_L>0`, the point
`t=-g_L/q_L` lies strictly below the Branch-F energy in every row; the nonzero
root is therefore the second intersection of the same positive quadratic level.

## 3. VV3 — consequence for Q-645

The corrected verdict's split stands, and its sole road-side scope flag closes in
the same direction as the simplicial calculation:

```text
energy      fixed at the selected level under the exhibited transport;
assignment  not forced on either licensed move.
```

The earlier statement “cubical assignment forced” remains valid only on the
one-parameter equal two-child share slice. It is false on the full 184-coordinate
cubical space. Both family A and family B now have explicit, non-gauge,
coarse-flux-preserving, `im(d_1')` equal-energy survivors. No consumer analysis is
performed or changed here.

## 4. VOID and verb audit

No member was bound, no common cell or junction was formed, no fixed point or end
test was executed, no physical quantity was numerically evaluated, and no measured
constant was consulted. Exact rational structural calculations are the task's
authorized scope. `minimum`, `rank`, `sphere`, and `witness` are used only where the
displayed exact certificate receives them; no branch or program content is adopted.

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

FREE_EDGES = 184 (counted)
E = rank 119 / min 5/24 / BranchF 1
VERDICT = SPHERE (dim 118 physical, witness verified)
CONSEQUENCE = Q-645 split stands; cubical scope flag closes assignment-free
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
