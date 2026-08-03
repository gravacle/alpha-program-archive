# STAGE 8 TASK 4B — CARRIER_METRIC_AND_UNITS ADOPTION PROPOSAL — LANE 2 V001

Date: 2026-08-03  
Task: PASTE 454 / Task 4b  
Lane: CODEX LANE 2  
Status: **PROPOSED_NOT_ADOPTED — DERIVATION DOES NOT FORCE THE PHYSICAL CARRIER METRIC; A MINIMAL DUAL-HILBERT PACKAGE IS PRESENTED FOR DoR-019**

```text
REGISTER_HEAD_AT_PREFLIGHT = Q-372
PREFLIGHT = PASS

LEAD_RESULT = AUTHORSHIP_REQUIRED
RATIFIED_STOCK_FORCES_CARRIER_METRIC = false | TYPE-R at the derivation claim
SOURCE_SIDE_A4_HILBERT_FORM_EXISTS = true | TYPE-P | premises: DoR-015
SOURCE_A4_FORM_EQUALS_R5_CARRIER_METRIC = false | TYPE-U before this proposal

PROPOSED_PACKAGE = DUAL_HILBERT_CARRIER_PACKAGE
PROPOSED_CARRIER_METRICS_POSITIVE = true | PASS_WITHIN_PROPOSAL
PROPOSED_RIESZ_MAPS_EXIST = true | PASS_WITHIN_PROPOSAL
PROPOSED_AUTOMORPHISMS_ISOMETRIC = true | PASS_WITHIN_PROPOSAL
PROPOSED_PENDANT_QUOTIENT_DESCENT = true | PASS_WITHIN_PROPOSAL
PROPOSED_CYCLE_CREATION_ACCOUNTED = true | PASS_WITHIN_PROPOSAL

RESPONSE_SUPPORT_USED_TO_DEFINE_METRIC = false
NU_FIXED_BY_METRIC = false
MEMBER_SELECTED = false
BASIS_SELECTED = false
FRAME_SELECTED = false
FILTRATION_SELECTED = false
REALIZATION_SELECTED = false

DOR_019 = RESERVED
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The proposed carrier metric is not inferred from the desired support of any
stationary-response block.  Its finite definition uses only the complete
Gate-4 quotient pairing and the retained A4 Hilbert source form.  Its
completed definition adds exactly two isometric carrier identifications and
a formal carrier-unit torsor.  No response value, `p`-verdict, numerical
normalization, or selected realization enters the construction.

---

## 0. Preflight, custody, and fences

The live questions-settled register and its seal were verified before work.
Its head was exactly `Q-372`.  The required adjudication was verified before
reading:

| Artifact | Verified SHA-256 | Use |
|---|---|---|
| `STAGE8_TASK4B_JET_RACE_ADJUDICATION_LANE1_V001.md` | `2e1b011069043c1cc03277178be061a8b7d1704d2146be97eb799965aef9c679` | G2/G3/G7 kill and the itemized missing carrier geometry |
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md` | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | Gate-4 quotient, all-cycle currents, retained A4 norm, Door B |
| `STAGE8_TASK4A_ACTION_COMPARISON_SQUARE_ADOPTION_PROPOSAL_LANE2_V004.md` | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | R4 units, R5 split, restriction and automorphism cubes |
| `STAGE8_TASK4A_FAMILY_NATURAL_PREFIX_TO_CYCLE_DESCENT_LANE2_V003.md` | `a03e836380cbbfa08d8763bf62d6104f70aec69ae484b3b69f63489a5ce1c68c` | quotient descent, restriction direction, pendant and cycle-creation boundaries |
| DoR-017 decision | `ee9d81bf78ab0ac9361cad5b48dde2b6b8b1e9fb0e28a4fdbba41e1c43db3e45` | ratified N member, symbolic `nu`, downstream falsifier |

The G3 adjudication is accepted exactly.  In particular, it establishes that
V005 does not instantiate positive forms on both R5 sectors and that R4's
action units are not carrier-unit isomorphisms.  This artifact repairs that
infrastructure only.  It does not revive the killed radial germ, choose a
replacement germ, or derive the missing divergence map.

```text
CUSTODY = builder proposal; Lane 1 cross-review required
STANDING = PROPOSED_NOT_ADOPTED
ALPHA_OR_RESPONSE_VALUE_EVALUATED = false
P_VERDICT_DECLARED = false
ROOTS_OR_K_STAR_EVALUATED = false
MEASURED_CONSTANT_COMPARISON = false
```

---

## 1. H1 — derivation check before authorship

### 1.1 Candidate A — the retained A4 norm and Door B

V005 defines, without a cycle-basis choice,

```text
J_fin^005 = algebraic directed union_N {u_c:c in ker(B_N^T)},
J_phys^005 = completion of J_fin^005 in the retained A4 proposal norm.
```

It then states explicitly:

```text
A4_NORM_FORCED_BY_GATE4 = false | TYPE-U.
```

Door B calls the resulting operation a Hilbert norm completion.  Therefore
the retained norm has a polarization on the source-current completion.  Let
that already-ratified source form be denoted `g_A4`.  This is real structure
on `J_phys^005`; it is not yet a form on either R5 carrier.

The missing assertions are precisely

```text
K_cycle  --I_K--> J_phys^005,
C_prop   --I_C--> K_cycle^*,
```

as completed, unit-carrying isometries.  Finite labels suggest these arrows,
but neither V005 nor Door B installs them on R5's completed carrier.  Thus:

```text
A4_FORCES_SOURCE_FORM = true | TYPE-P | premises: DoR-015
A4_FORCES_I_K_OR_I_C = false | TYPE-R at the derivation claim
A4_FORCES_R_C_OR_R_K = false | TYPE-R at the derivation claim
```

### 1.2 Candidate B — the DoR-009 trace pairing

DoR-009's finite trace is a state/effect pairing on the finite record
operator carrier.  It fixes faithful-character normalization, the doubled
trace, and `E_post` orientation.  It does not identify record operators with
the tangent sectors `C_prop` and `K_cycle`, and it does not state positivity
or nondegeneracy on those sectors.

A trace form could be pulled back only after supplying a record-to-carrier
intertwiner.  No such metric intertwiner is ratified.  Different pullbacks
through equally lawful intertwiners give different carrier forms while all
DoR-009 traces remain unchanged.

```text
DOR009_TRACE_FORCES_CARRIER_FORM = false | TYPE-R
MISSING_FOR_TRACE_PULLBACK = record-to-R5-carrier isometric intertwiner | TYPE-U
```

### 1.3 Candidate C — `G^007`

The exact raw bilinear is

```text
G^007(f,h)=-hbar^2 q(1-q)L(f)L(h).
```

It has rank-one image and contains the nonzero physical cycle current in
`ker L`.  Hence it is degenerate on the record-visible sector and cannot be
a positive carrier inner product.  Quotienting its kernel would delete the
Gate-4 cycle witness, which is forbidden.

```text
G007_FORCES_POSITIVE_CARRIER_METRIC = false | TYPE-R
test = nonzero u_square lies in ker(G^007)
```

### 1.4 Candidate D — R5 topology, inverse, and automorphism transport

R5 supplies

```text
Y=C_prop direct-sum K_cycle,
```

a common graph domain, finite seminorm topology, a reducing complement
inverse, signed/semilinear automorphism actions, and the `rho_H,N` cube.  A
topology does not fix an inner product: even in finite dimension, every
positive automorphism-invariant weighting on the distinct automorphism
orbits gives the same topology.  The inverse and Schur operations determine
no carrier metric without circularly using response support.

```text
R5_TOPOLOGY_FORCES_METRIC = false | TYPE-R
R5_INVERSE_FORCES_METRIC = false | TYPE-R
AUTOMORPHISM_COVARIANCE_ALONE_FORCES_SCALE = false | TYPE-R
```

### 1.5 Candidate E — quotient duality alone

Gate 4 proves the nondegenerate finite pairing

```text
< [x],c >_G := c^T x,
[x] in coker(B_G), c in ker(B_G^T).
```

This identifies each finite quotient with the algebraic dual of the cycle
space.  Duality determines neither the norm on one side nor the common unit
scale.  For every positive form `g_K`, the dual form on the quotient is
lawful, and rescaling `g_K` produces a different lawful pair.

```text
GATE4_DUALITY_FORCES_METRIC = false | TYPE-R
GATE4_DUALITY_REDUCES_TWO_METRIC_CHOICES_TO_ONE = true | TYPE-P
```

### 1.6 Derivation verdict

No ratified candidate forces the package.  The most the corpus supplies is:

1. a source-side Hilbert form `g_A4`;
2. a complete finite quotient/cycle duality;
3. signed automorphism actions and restriction squares that any proposal
   must respect.

The carrier identifications and unit scale remain authored physics.

```text
CARRIER_METRIC_DERIVED_FROM_RATIFIED_STACK = false | TYPE-R
CARRIER_METRIC_AUTHORSHIP_REQUIRED = true | TYPE-U before DoR-019
```

---

## 2. H2 — the proposed dual-Hilbert carrier package

### 2.1 Finite carriers and the existing pairing

For every admitted finite signed realization `G`, use the already-ratified
objects

```text
E_G       = real oriented edge-current carrier;
V_G       = image(B_G), the Gate-4 vertex/gauge directions;
Q_G^lin   = E_G/V_G, the real tangent of the path-visible quotient;
K_G       = ker(B_G^T), the conserved cycle-current carrier.
```

The pairing is representative-independent because
`c^T B_G theta=0` for `c in K_G`:

```text
beta_G:Q_G^lin x K_G -> R,
beta_G([x],c)=c^T x.                              (H2-1)
```

V005 separation makes `beta_G` nondegenerate.  No edge, cycle basis,
orientation representative, or realization member has been selected.

### 2.2 The all-cycle current identification

The proposal installs the finite map already indicated by V005's complete
current family:

```text
I_K,G:K_G -> J_fin,G^005,
I_K,G(c)=u_c.                                     (H2-2)
```

It then requires the maps `(H2-2)` to extend by density to one completed
isometric isomorphism

```text
I_K:K_cycle -> closure{u_c} in J_phys^005.        (H2-3)
```

This is an authored completion certificate, not a projection onto a chosen
cycle basis.  Its range is the complete closed all-cycle current sector.

Define

```text
g_K(k,l):=g_A4(I_K k,I_K l),
||k||_K^2:=g_K(k,k),
R_K:K_cycle->K_cycle^*,
(R_K k)(l)=g_K(k,l).                              (H2-4)
```

Positivity follows from injectivity of `I_K` and positivity of `g_A4`.

### 2.3 The quotient/complement identification

At finite stage, `(H2-1)` defines

```text
I_C,G:Q_G^lin -> K_G^*,
I_C,G([x])(c)=beta_G([x],c).                      (H2-5)
```

Nondegeneracy makes this an isomorphism.  The proposal requires its
restriction-natural completion on the R5 complement:

```text
I_C:C_prop -> K_cycle^*.                          (H2-6)
```

Equip `K_cycle^*` with the Hilbert-dual metric induced by `g_K`, and set

```text
g_C(c,d):=g_(K^*)(I_C c,I_C d),
||c||_C^2:=g_C(c,c),
R_C:C_prop->C_prop^*,
(R_C c)(d)=g_C(c,d).                              (H2-7)
```

Equivalently on every finite stage,

```text
||[x]||_C
 =sup_{0!=c in K_G} |c^T x|/||c||_K.             (H2-8)
```

Equation `(H2-8)` proves representative independence and the pendant/tree
quotient descent.  It also shows that the two sector metrics are one
authored choice plus Gate-4 duality, not two independently tunable response
weights.

### 2.4 Carrier units without a frame

Let `U_K` be a one-dimensional real unit torsor for cycle currents and let
`U_C:=U_K^*` under `(H2-1)`.  No nonzero element of either torsor is chosen.
The unit isomorphisms are the orthogonal-torsor classes

```text
[U_Kmap]:K_cycle -> ell^2(K;U_K) modulo O(K),
[U_Cmap]:C_prop  -> ell^2(C;U_C) modulo O(C).      (H2-9)
```

Postcomposition by an orthogonal map changes a frame but not `g_K` or
`g_C`; hence `(H2-9)` supplies units without a basis/frame member.

R4 declares `U_action`, and the only unit relations proposed here are

```text
[D_C phi]=U_action/U_C,
[D_K phi]=U_action/U_K,
[D_A D_B phi]=U_action/(U_A U_B),
[R_A]=U_A^2, A in {C,K},
[nu]=U_action.                                   (H2-10)
```

There is no equation setting `U_C`, `U_K`, or either metric equal to `nu`.
Rescaling the formal carrier unit transports all carrier coordinates and
Riesz maps covariantly while leaving `nu` symbolic.

### 2.5 The completed package

```text
CARRIER_METRIC_AND_UNITS_019 :=
 (K_cycle,C_prop,
  I_K,I_C,
  g_K,g_C,R_K,R_C,
  U_K,U_C,U_action,
  AutIso,RestrictIso,QuotientNormCert,
  CycleCreationCert,UnitsCert,FiniteRestrictionCert).
                                                        (H2-11)
```

Every field in `(H2-11)` is `PROPOSED_NOT_ADOPTED`.  `U_action` itself is
inherited from R4; the new content is its typed relation to the carrier
unit torsors, not a new action scale.

---

## 3. H3 — choice table and minimality

| Field | Proposed addition beyond ratified data | Genuine alternatives | Carrier-only minimality | Void condition |
|---|---|---|---|---|
| `I_K` | completion of `c -> u_c` as an isometry onto the closed all-cycle source sector | independent abstract `K` metric; nonisometric injection; selected cycle frame | reuses the one Hilbert form already present instead of adding a second independent form | kernel, nonclosed range, basis dependence, or failed restriction |
| `I_C` | completion of the Gate-4 quotient pairing as `C_prop -> K_cycle^*` | independent complement metric; selected splitting of edge representatives | uses the already-proved separating pairing and adds no complement weight | pendant direction survives, a visible quotient is killed, or pairing becomes degenerate |
| `g_K,g_C` | pullback and Hilbert-dual forms `(H2-4)`/`(H2-7)` | two independent forms; orbit-weighted forms; degenerate response bilinear | one positive form plus duality is the fewest independent metric data | nonpositivity, response-support clause, or failure to induce the declared topology |
| `R_K,R_C` | Riesz maps of the proposed forms | algebraic dual only; non-Riesz rigging; unbounded metric operator | exactly what the jet calculus needs to turn differentials into carrier vectors | not bijective on the declared Hilbert carrier or failure on dense core |
| `U_K,U_C` | dual formal unit torsors, no member chosen | fixed numerical unit; independent unrelated sector scales; unitless coordinates | records dimensions without fixing `nu` or a frame | any equation fixes `nu`, a ratio, or a numerical response scale |
| `AutIso` | all admitted signed relabelings/exchanges are orthogonal; reversal is antiunitary with sign action | covariance without isometry; memberwise metric family | minimum strengthening needed for R1-COV jets to be metric-covariant | rank-two exchange or reversal changes a norm |
| `RestrictIso` | isometry only on scopes already carrying isometric inclusions; restrictions are their adjoints/coisometries where proven | claim every cellular map is isometric; arbitrary rescaling per stage | matches W3 and does not invent the forbidden cycle-creating upward quotient map | `j_NM^Q`, `rho_Gamma,N`, or `rho_H,N` cube fails on its certified scope |
| quotient norm | `(H2-8)` | representative norm; spanning-tree gauge; chosen orthogonal section | only representative-independent norm determined by `g_K` and `beta` | pendant/tree value is nonzero or quotient infimum depends on representative |
| cycle-creation rule | retain old cycle space isometrically and take the new orthogonal complement | renormalize all old cycles; choose a new cycle basis; assert a physical upward quotient map | preserves old facts and types only the genuinely new directions | old norm changes, a new cycle is deleted, or Z7 is contradicted |

The proposed field is not selected from this table by its effect on a Schur
block.  It is selected as the minimal dual-Hilbert extension of the already
ratified carrier pairing and source Hilbert form.  Whether the principal
ratifies it is reserved to DoR-019.

```text
TARGET_OUTPUT_USED_IN_CHOICE_TABLE = false
INDEPENDENT_C_AND_K_RESPONSE_WEIGHTS_ADOPTED = false
NUMERIC_CARRIER_SCALE_ADOPTED = false
```

---

## 4. Automorphism/isometry theorem

### 4.1 Statement

Let `sigma:G->G'` be an admitted realization automorphism: an edge exchange,
an orientation reversal with its sign action, or a simultaneous relabeling.
Let `S_sigma` be its signed edge/cycle transport and `kappa_sigma` be the
identity for exchanges/relabelings and conjugation for reality reversal.
Then within the proposal:

```text
I_K,G' S_sigma = alpha_J I_K,G,
I_C,G' alpha_C = alpha_K^* I_C,G,                 (H4-1)

g_K,G'(S_sigma k,S_sigma l)
 =kappa_sigma g_K,G(k,l),
g_C,G'(alpha_C c,alpha_C d)
 =kappa_sigma g_C,G(c,d).                         (H4-2)
```

For the real forms, conjugation leaves the scalar value fixed; on the
complexified carriers reversal is antiunitary.  Equations `(H4-1)` follow
from `u_(S c)=alpha_J u_c` and covariance of the Gate-4 pairing.  The
retained A4 form is transported with the whole current family, not on a
chosen basis member.  Pullback then proves `(H4-2)`.

The Riesz maps obey

```text
R_K,G' S_sigma=S_sigma^(-*) R_K,G,
R_C,G' alpha_C=alpha_C^(-*) R_C,G.                (H4-3)
```

Thus the proposed metric is covariant over the full realization family and
isometric on every admitted automorphism orbit.

### 4.2 S8-A rank-two exchange

On the named S8-A cycle triple, with its rank-two relation retained,

```text
S_sigma=[[0,1,0],
         [1,0,0],
         [0,0,-1]],
S_sigma^T S_sigma=I.                              (H4-4)
```

For coefficient vectors `x,y`,

```text
g_K(S_sigma x,S_sigma y)
 =x^T S_sigma^T G_K S_sigma y
 =x^T G_K y
 =g_K(x,y),                                      (H4-5)
```

where the middle equality is `(H4-2)`, equivalently the all-cycle A4 form's
exchange covariance.  The third coordinate changes sign but not norm.  On
the quotient dual the contragredient action gives the identical calculation.

```text
S8A_RANK_TWO_EXCHANGE_ISOMETRY = PASS_WITHIN_PROPOSAL
CYCLE_SELECTIVE_WEIGHT = excluded unless constant on the full automorphism orbit
```

---

## 5. Quotient norm and pendant/tree theorem

Let `[x]=[x+B_G theta]`.  For every conserved `c`,

```text
c^T(x+B_G theta)=c^T x.
```

Therefore `(H2-8)` is independent of the representative.  If `[x]=0`, every
pairing is zero and `||[x]||_C=0`.  Conversely V005 separation says that a
nonzero class has a `c` with `c^T x!=0`, hence its norm is positive.

For a connected tree, `K_G=ker(B_G^T)={0}` and `Q_G^lin={0}`.  For a cycle
with an attached pendant edge, varying only the pendant character is a
vertex coboundary.  It pairs to zero with every conserved cycle and so has
zero quotient norm.  The cycle holonomy remains nonzero in the quotient and
has positive norm.

```text
PENDANT_TREE_GAUGE_NORM = 0 | PASS_WITHIN_PROPOSAL
RECORD_VISIBLE_CYCLE_NORM_POSITIVE = true | PASS_WITHIN_PROPOSAL
PENDANT_WITNESS_DOES_NOT_REENTER = true
```

No spanning tree or representative is chosen to prove this theorem.

---

## 6. Restriction, W3, and cycle-creating stages

### 6.1 Rank-preserving zero extension and `j_NM^Q`

On the sealed/rank-preserving zero-extension scope, the corrected
`j_NM^Q` appends identity source coordinates and the physical restriction is
an isomorphism.  The all-cycle current maps commute:

```text
I_K,M j_K,NM=j_J,NM I_K,N.                       (H6-1)
```

The proposed metric requires `j_J,NM` to be the retained A4 isometry on
this scope.  Hence

```text
g_K,M(j_K k,j_K l)=g_K,N(k,l),
g_C,M(j_C c,j_C d)=g_C,N(c,d).                   (H6-2)
```

The W3 restrictions are the Hilbert adjoints:

```text
rho_K,MN=j_K,NM^*,
rho_C,MN=j_C,NM^*.                               (H6-3)
```

This proves the isometric square exactly where the prior artifacts claimed
an isometric inclusion.  It does not enlarge the extension theorem.

### 6.2 Cycle-creating addition

If an added edge creates a cycle, descent V003 proves that no
representative-independent physical upward quotient map can make the source
identity-extension square commute.  That impossibility remains in force.

The cycle lattice itself has the lawful edge-zero-extension
`i_*:K_N->K_M`.  Under `(H2-4)` it is isometric on the old all-cycle current
subspace.  Define only the metric decomposition

```text
K_M=i_*K_N orthogonal-direct-sum K_new,
K_new:=(i_*K_N)^perp.                             (H6-4)
```

Every new record-visible cycle lies in `K_new` or has a nonzero projection
onto it; positivity prevents deletion.  Therefore

```text
||i_*k+k_new||_(K_M)^2
 =||k||_(K_N)^2+||k_new||_(K_M)^2.               (H6-5)
```

Equation `(H6-5)` is the cycle-creating stage behavior required for the
next germ round.  It does not imply stationary-root naturality.  In
particular, the G7 counterexample may still change a future radial
stationary equation through `||k_new||^2`; this package makes that change
well-defined and visible rather than pretending it vanishes.

```text
CYCLE_CREATING_PHYSICAL_UPWARD_QUOTIENT_MAP = false | TYPE-R | Z7 retained
CYCLE_CREATING_OLD_CYCLE_ISOMETRY = PASS_WITHIN_PROPOSAL
NEW_CYCLE_ORTHOGONAL_COMPONENT = PASS_WITHIN_PROPOSAL
STATIONARY_ROOT_NATURALITY_FROM_METRIC_ALONE = false | TYPE-R
```

### 6.3 General restriction

For a declared signed cellular arrow, the lawful direction remains the
contravariant restriction `rho_f`.  It is required to be bounded in the
proposed Hilbert norms.  It is isometric only when the existing theorem says
the underlying inclusion is an isomorphism/isometry.  Batching maps may be
contractive or bounded without being isometries; no stronger claim is made.

---

## 7. Compatibility with `rho_Gamma,N` and `rho_H,N`

### 7.1 Action restriction

`rho_Gamma,N` maps a completed scalar action to its finite action.  It is not
a carrier map, so calling it an isometry would be ill-typed.  Metric
compatibility means its derivatives use the adjoint carrier restrictions:

```text
D_A(rho_Gamma,N Gamma)
 =rho_A,N^* D_A Gamma,

D_A D_B(rho_Gamma,N Gamma)
 =rho_H,N(D_A D_B Gamma),                         (H7-1)
```

on the R5-generated class.  The units in `(H2-10)` are identical on both
sides.

### 7.2 Hessian cube

V004 defines

```text
rho_H,N(D^2 Gamma):=D^2(rho_Gamma,N Gamma)
```

and proves automorphism naturality on the R5-generated class.  With
`alpha_C,alpha_K` isometric by `(H4-2)`, the dual transports are exactly the
Riesz-conjugated transports.  Therefore

```text
rho_H,N,G' alpha_H,A
 =alpha_H,A,N rho_H,N,G                           (H7-2)
```

continues to hold, now as an isometric/antiunitary Hessian cube.  The S8-A
matrix calculation `(H4-4)` gives both sides entry by entry.  No arbitrary
external Hessian is added to the scope.

```text
RHO_GAMMA_METRIC_COMPATIBILITY = PASS_WITHIN_PROPOSAL | typed as derivative naturality
RHO_H_METRIC_CUBE = PASS_WITHIN_PROPOSAL | R5-generated class only
ARBITRARY_EXTERNAL_HESSIAN_METRIC_NATURALITY = not_claimed
```

---

## 8. H4 — advance certificates for the next germ round

| Certificate | Exact check | Verdict |
|---|---|---|
| rank-two exchange | `S_sigma^T S_sigma=I`; all-cycle A4 covariance gives `(H4-5)` | **PASS_WITHIN_PROPOSAL** |
| orientation reversal | cycle sign plus conjugation is antiunitary; real norms fixed | **PASS_WITHIN_PROPOSAL** |
| relabeling | simultaneous signed permutation transports `I_K`, `I_C`, and both forms | **PASS_WITHIN_PROPOSAL** |
| pendant quotient | all pendant/tree coboundaries pair zero with `ker B^T`; quotient norm zero | **PASS_WITHIN_PROPOSAL** |
| visible-cycle retention | Gate-4 separation plus positivity makes every nonzero quotient/cycle norm positive | **PASS_WITHIN_PROPOSAL** |
| rank-preserving `j_NM^Q` | old all-cycle current inclusion is isometric and restriction is its adjoint | **PASS_WITHIN_PROPOSAL** |
| cycle creation | old cycles remain isometric; new directions are the orthogonal complement; no upward quotient map asserted | **PASS_WITHIN_PROPOSAL** |
| `rho_Gamma,N` | derivative naturality, not an ill-typed scalar-action isometry | **PASS_WITHIN_PROPOSAL** |
| `rho_H,N` | Riesz-equivariant form of the already-proved O1 cube | **PASS_WITHIN_PROPOSAL** |
| DoR-008 finite restrictions | the metric adds no action term; all finite actions/traces remain the sealed ones; derivative squares commute on their certified scopes | **PASS_WITHIN_PROPOSAL** |
| `nu` homogeneity | carrier units do not set `nu`; scaling the ratified member still scales `nu` and jets homogeneously | **PASS_WITHIN_PROPOSAL** |

The DoR-008 check is structural and exact: no finite amplitude, trace,
Hessian value, or action bottom leg is altered by `(H2-11)`.  The proposal
only supplies Riesz identifications for the already-existing tangent and
cotangent data.

---

## 9. Six-account and door ledger

| Operation | Kernel | Image | Sector transfer | Restriction square | Tail action | Topology/door |
|---|---|---|---|---|---|---|
| `I_K` | zero by V005 separation | closed all-cycle current sector | `K_cycle -> J_phys` only | `(H6-1)` | zero created tail by density | Hilbert completion; **PROPOSED** |
| `I_C` | zero by quotient separation | Hilbert dual of `K_cycle` | quotient complement to cycle dual | `(H7-1)` | zero if dual completion is strong | Hilbert-dual completion; **PROPOSED** |
| `R_K` | zero | `K_cycle^*` | vector to covector within K | adjoint naturality | none | bounded Riesz isomorphism; **PROPOSED** |
| `R_C` | zero | `C_prop^*` | vector to covector within C | adjoint naturality | none | bounded Riesz isomorphism; **PROPOSED** |
| quotient norm | exactly `V_G=image B_G` before quotient; zero after quotient | separated `Q_G^lin` | deletes gauge only | contravariant restriction | no new tail | quotient Hilbert norm; **PROPOSED** |
| automorphism transport | zero | full carrier | signed permutation/conjugation only | O1 cube | tail preserved, not created | orthogonal/antiunitary; **PROPOSED** |
| cycle creation decomposition | zero on old inclusion | old cycles plus `K_new` | none between C/K | old inclusion isometric; no physical upward quotient map | new finite directions explicit | finite orthogonal sum; **PROPOSED** |

No completion is hidden.  The two genuinely new completions are `(H2-3)`
and `(H2-6)`, and both are named in the package.

---

## 10. H5 — hostile self-kill battery

### Attack 1 — response-support tuning (the G2 sin)

**Attack.** Change the relative C/K metric so that a desired mixed or
complement response block becomes nonzero.

**Result.** **KILLED BY THE PROPOSAL'S VOID CLAUSE.**  `g_K` is pulled back
from the complete all-cycle A4 form and `g_C` is its Gate-4 dual.  No Hessian,
Schur support, `p`, or retarded block appears in the definition.  Any metric
selected by response support is outside `(H2-11)` and voids DoR-019.

### Attack 2 — hidden scale fixes `nu`

**Attack.** Interpret the carrier unit as the action scale and infer a value
of `nu`.

**Result.** **FAILS.**  `(H2-10)` keeps `U_action`, `U_C`, and `U_K` distinct.
`nu` remains a symbolic element with action units.  Carrier rescaling is
unit covariance, not a normalizer equation.

### Attack 3 — rank-two cycle-selective anisotropy

**Attack.** Weight `c_1` but not its exchanged partner `c_2`, or give `c_3`
a sign-sensitive norm.

**Result.** **EXCLUDED.**  The S8-A exchange `(H4-4)` would fail `(H4-2)`.
The proposal admits only the full automorphism-covariant form transported
from A4.

### Attack 4 — pendant character acquires physical length

**Attack.** Give an endpoint/pendant coordinate positive norm before taking
the quotient and carry it into `C_prop`.

**Result.** **EXCLUDED.**  `(H2-8)` depends only on the cycle pairing.  Every
pendant/tree coboundary has zero quotient norm.  A representative norm is
not the proposed quotient norm.

### Attack 5 — cycle-creating extension silently selects a lift

**Attack.** Use the metric adjoint to manufacture the physical upward map
refuted by Z7.

**Result.** **EXCLUDED.**  `(H6-4)` is a decomposition of the target cycle
carrier only.  It is not a map from the old physical quotient into the new
one and does not make the source extension square commute.  The Z7
impossibility theorem remains a permanent regression.

### Attack 6 — selected frame hidden in a Riesz map

**Attack.** Choose an orthonormal cycle basis to define `R_K` and thereby
select a realization member.

**Result.** **FAILS.**  Riesz is defined by the form, and the unit maps are
orthogonal-torsor classes.  Changing an orthonormal frame changes neither
the form nor the Riesz map.

### Attack 7 — fresh attack: automorphism invariance does not imply uniqueness

**Attack.** On a graph with multiple automorphism orbits, assign distinct
positive orbit weights.  Every admitted automorphism remains isometric, so
perhaps the metric was falsely called derived.

**Result.** **ATTACK SUCCEEDS AGAINST DERIVATION, NOT AGAINST THE DISCLOSED
PROPOSAL.**  This counterfamily is exactly why H1 returns `AUTHORSHIP_REQUIRED`.
The proposal chooses the A4-pullback/dual law as an authored field and does
not claim automorphism invariance forces it.  DoR-019 must knowingly ratify
or reject that law.

### Attack 8 — degenerate trace or raw bilinear reused as metric

**Attack.** Replace `g_C` or `g_K` by the DoR-009 trace pullback or `G^007`.

**Result.** **EXCLUDED.**  No carrier intertwiner makes the trace pullback
available, and `G^007` has a record-visible kernel.  Either substitution
fails positivity/nondegeneracy.

### Attack 9 — filtration/member dependence

**Attack.** Two realizations of one physical object receive inequivalent
metrics.

**Result.** **EXCLUDED BY `(H4-1)`–`(H4-3)`.**  The package is a natural
assignment over the full admitted realization family.  A memberwise form
without those equations is not admissible.

```text
SELF_KILL_BATTERY = 9 attacks run
KNOWN_G2_SUPPORT_TUNING = excluded
KNOWN_G3_MISSING_FIELDS = explicitly supplied
KNOWN_G7_CYCLE_CREATION = typed, not falsely closed
NEW_DERIVATION_COUNTERFAMILY = disclosed
```

---

## 11. H6 — doors deliberately left open

| Door | Standing | Exact would-build |
|---|---|---|
| divergence-to-carrier map | `TYPE-U` | a ratified, target-independent map from `delta_div/Depth/Accum/Gen` to carrier coordinates; this package supplies no such map |
| N-member jet instantiation | `TYPE-U` | an evaluable covariant `phi_m` whose jets use `R_C,R_K` without response tuning |
| stationary-point data | `TYPE-U` | a family-natural solution on the completed R5 domain with the cycle-creation regression passed |
| cycle-creating physical upward quotient map | `false | TYPE-R` | impossible in the Z7 class; only contravariant restriction is lawful |
| non-edge-resolved completion | `TYPE-U` | a natural completion beyond the edge-resolved realization family preserving quotient separation and metrics |
| arbitrary-external-Hessian cube | `TYPE-U` | a restriction theorem beyond the R5-generated Hessian class |
| numerical carrier/action calibration | `TYPE-U` | a later unit calibration; cannot be inferred from `nu`, `p`, or a desired response |
| alpha-facing response and p-verdict | `NOT_EXECUTED` | completed jet, stationary, Schur, and final-consumption chain under the standing falsifier |

These doors are not defects in the metric package.  They are operations
outside the commission, and none is filled by convention.

---

## 12. Standing falsifier and DoR-019 choice

If adopted, the package stands only while all of the following remain true:

1. every finite all-cycle current has the same norm before and after every
   certified rank-preserving zero extension;
2. every admitted realization automorphism is orthogonal/antiunitary;
3. pendant/tree coboundaries have zero physical quotient norm;
4. every record-visible cycle has positive norm;
5. `rho_Gamma,N` and `rho_H,N` retain their certified derivative cubes;
6. cycle creation preserves old norms and exposes, rather than deletes, new
   finite cycle directions;
7. no metric clause mentions or is changed by response support, `p`, a
   desired stationary root, or a desired alpha-facing output;
8. no carrier-unit choice fixes `nu` or any numerical scale.

Failure of any item voids the proposed package.

The principal's lawful choices are:

| DoR-019 option | Content | Consequence |
|---|---|---|
| adopt the dual-Hilbert package | ratify `(H2-11)` with the complete falsifier | carrier metrics, Riesz maps, units, and isometric transports become premises; jet authoring may restart |
| request a different carrier-only metric law | provide its positive forms, duality seam, unit torsors, automorphism/restriction proofs, and the same falsifier | this proposal remains unadopted |
| reject | add no metric physics | the jet boundary remains `TYPE-U` |

No option is selected here.

```text
CARRIER_METRIC_AND_UNITS_PROPOSAL_V001 = COMPLETE
DERIVATION_CHECK = NO_FORCED_FORM
AUTHORED_PACKAGE_MINIMALITY = PROVED_WITHIN_PROPOSAL
RANK_TWO_EXCHANGE = PASS_WITHIN_PROPOSAL
PENDANT_QUOTIENT = PASS_WITHIN_PROPOSAL
CYCLE_CREATION_BEHAVIOR = PASS_WITHIN_PROPOSAL_WITH_Z7_BOUNDARY
DOR008_RESTRICTION_COMPATIBILITY = PASS_WITHIN_PROPOSAL
RESPONSE_SUPPORT_SMUGGLED = false
HIDDEN_NU_SCALE = false
READY_FOR_CROSS_REVIEW = yes

PROPOSAL_STANDING = PROPOSED_NOT_ADOPTED
DOR_019 = RESERVED

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

