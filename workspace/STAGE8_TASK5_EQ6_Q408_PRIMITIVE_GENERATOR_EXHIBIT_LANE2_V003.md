# STAGE 8 TASK 5 / EQ6 — Q-408 PRIMITIVE GENERATOR EXHIBIT — LANE 2 V003

Date: 2026-08-04  
Lane: Codex Lane 2  
Task: 5 / EQ6 / `B_Q408_REFINEMENT`  
Custody: builder repair after Q-430; hostile check required

## Lead result

```text
LOCALITY_SUPPORT =
  PROVEN_PER_GENERATOR_ON(
    ACTUAL_FINITE_OBJECTS
    + ADMITTED_SURFACE_ISOMORPHISMS
    + FINITE_RESTRICTIONS
    + ZERO_EXTENSION
    + RANK_PRESERVING_Ref_path
    + GATE4_QUOTIENT_DESCENT
  );

  STOPPED_AT(
    CYCLE_CREATING_Ext_cycle:
      ACTUAL_PATH_CURRENT_SUPPORT_CORRESPONDENCE
      + SUPPORT_LOCAL_TEST_TRANSPORT
      + DISJOINT_SECTOR_ORTHOGONALITY_OF_THE_RATIFIED_RIESZ_MAP
      + LOCAL_COFRAME_DENSITY_CONNECTION_CURVATURE_TRANSPORT
  )

SECTOR_MIXING_REGRESSION = PASS |
  THE_RIESZ_INDUCED_MIXER_FAILS_LOCALITY_MEMBERSHIP

PHYSICAL_KERNEL_SQUARE =
  PROVEN_ON_Ref_path;
  CYCLE_CREATING_Ext_cycle = CONDITIONAL_THEOREM_ONLY
  + NOT_INSTANTIATED

GEOMETRY_ANCHORS = PROVEN_ON_BUILT_SCOPE
COMPOSITION = PROVEN_ON_BUILT_SCOPE
COMMON_REFINEMENT = PROVEN_ON_ACTUAL_Ref_path_DIAMONDS
COVARIANCE_FAMILY = FULL_NO_SELECTION_FAMILY_ON_BUILT_SCOPE
ALL_STAGE_SKELETON = STAGEWISE_ONLY

GENERATORS = PARTIAL_EXHIBIT
B_Q408_REFINEMENT_FULL_ROOT = OPEN / TYPE-U
MISSING_KIND = LOCAL_SUPPORT_GEOMETRY_AND_LOCAL_DUALITY_DATA
JOINT_EQ6 = OPEN
C1_RESUMPTION = N/A
EQ6_MEMBER_BOUND = false
```

V003 does not repair the Q-430 kill by adding another commuting diagram.
It first defines the geometric locality and support conditions that a
physical generator must satisfy.  The already geometric generators pass.
The cycle-creating algebraic pullback is then tested against those conditions
and fails on the reviewer's Riesz mixer.

The failure is exact.  Q-408's arbitrary-profile kernel square together with
the actual path orientation forces a unique test-class map.  That map is
V002's Riesz-induced map.  It is
support-local if and only if the retained Riesz form and the cycle-creation
map satisfy an additional disjoint-sector locality condition.  DoR-019
ratifies positivity, units, covariance, and its stated restriction squares;
it does not ratify this cycle-creating support orthogonality.  DoR-015 and
Q-408 supply actual paths and supports objectwise, but no path/support
correspondence along a cycle-creating arrow.

Thus the largest honest exhibit remains the actual finite plus `Ref_path`
subcategory already identified at Q-425.  The newly isolated missing datum is
not a seventh root: it is the physical locality content of the existing
`B_Q408_REFINEMENT` root.

---

## 0. Preflight, authorities, and register sweep

### 0.1 Three-line preflight

```text
DOES THE OBJECT EXIST?  The locality/support specification and its maximal
                        built subobject are constructed below; the full
                        cycle-creating generator does not exist in the
                        ratified stack.
IS THE VERSION CURRENT? YES, through register head Q-430.
ARE ITS INPUTS PRESENT? YES: the sealed Q-430 hostile check, V002, V005,
                        Q-408, DoR-019, Ref_path, C1, and DoR-020.
PREFLIGHT = PASS
```

The hostile check was verified before reading:

```text
STAGE8_TASK5_EQ6_EXHIBIT_V002_HOSTILE_CHECK_LANE1_V001.md
SHA-256 = 4bfe044d62247950089142715e1534695922ac17c34e239cc63097df090347a1
SEAL = PASS
```

Verified authorities:

| Authority | SHA-256 | Use |
|---|---|---|
| locked process with Q-427 rule | `d537e294c03b3fc50fa49844f5b166bdcee1d64fe1513b9201047f602cd1518f` | custody; surface/rails split |
| register at Q-430 | `f1ec3a155883bf8b4092186669205e01b560c4849c85765aa05622f4979d2c03` | current scope |
| V002 hostile check | `4bfe044d62247950089142715e1534695922ac17c34e239cc63097df090347a1` | sector mixer and kill anatomy |
| V002 | `686b2c4a0e6c60f54a9173d8554efce116df4a332fc318cb1ffae32bb4cdf930` | bounded repair source |
| field signature V005 / DoR-015 object | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | paths, incidence, support, cycles, quotient |
| Q-408 current/kernel realization | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | actual currents, test analysis, kernels, support |
| carrier metric V005 / DoR-019 object | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | retained Riesz maps and units |
| derived `Ref_path` square | `fa73114214d7653d9a5d181a684b3bd65f0d6e9f91fd2256fb159ca97e56c4bf` | physical rank-preserving refinement |
| C1 completion build | `5203347c9bba7f99c2f033467815defa7ac047f74ea73b313972f44975d250a5` | maximal physical subcategory `Ref_0` |
| frontier map | `b8294e917531dd4f1731aedd54fd1c52a320840335061bbb4ab872830d001028` | root contract |
| DoR-020 | `bead32b7a12dd70b48a5ddd729395f23914dce06047783226a33d3ccb1eafa31` | conditional equalizer and prohibitions |

### 0.2 Register sweep

```text
Q-297  physical current carrier is the complete ker(B^T) family on the
       Gate-4/path-visible quotient;
Q-355  cycle-creating upward extension is impossible in general; lawful
       contravariant restriction survives;
Q-384  the retained carrier metric and Riesz map exist;
Q-408  actual finite currents and bilocal kernels exist, with path support;
Q-418  actual rank-preserving path subdivision is derived;
Q-423  finite and Ref_path subpackages are genuine;
Q-424  B_Q408_REFINEMENT is the first new-physics root;
Q-425  Ref_0 is the maximal physical refinement scope then available;
Q-427  actual surface geometry must be separated from rails;
Q-428  V001 killed by the false cycle-creating square, orbit, and skeleton;
Q-429  V002 repairs the old-image square and preserves new-cycle kernels;
Q-430  V002 killed because Riesz pullback can mix disjoint cycle sectors.
```

No settled entry supplies a support-local cycle-creating current/test map or
a theorem that the DoR-019 metric orthogonalizes disjoint physical supports.

### 0.3 Bearing symbols

```text
M_G                 = actual DoR-015 surface member at stage G;
gamma_(G,e)         = its actual oriented physical path for edge e;
B_G                 = signed incidence map;
K_G=ker(B_G^T)      = complete conserved cycle-current carrier;
J_G(c)              = actual Q-408 distributional current;
Supp_G(c)           = support of J_G(c) in M_G;

T_G                 = compactly supported physical connection tests;
q_G:T_G->Tbar_G     = quotient by ker(A_G);
Tbar_G(O)           = q_G{a:supp(a) subset O};
Abar_G:Tbar_G->K_G* = Q-408 analysis isomorphism;
R_G:K_G->K_G*       = retained DoR-019 Riesz map;
Phi_G=R_G^(-1)Abar_G;
Kern_G(H)           = actual Q-408 bilocal kernel;

F_R                 = required actual map of physical support regions;
S_R                 = signed cycle-current map;
P_R                 = required physical test-class transport;
I_R^T               = V002's uniquely forced algebraic pullback;

Ref_0               = actual finite stages plus rank-preserving Ref_path;
Ext_cycle            = proposed cycle-creating physical refinement;
signed chain map     != physical support refinement;
kernel commutation   != locality;
objectwise support   != support transport between objects.
```

---

## 1. X1 — locality and support certificates defined before construction

### 1.1 The ratified local surface carriers

For `c in K_G`, Q-408 and V005 give

```text
J_G(c)[a]
 =sum_(e in E_G)c_e integral_(gamma_(G,e)) a.    (X1-1)
```

Define the actual current support

```text
Supp_G(c):=supp J_G(c)
 subset closure(union_(c_e !=0) gamma_(G,e)([0,1])).  (X1-2)
```

For every open physical region `O subset M_G`, define the local sectors

```text
K_G(O):={c in K_G:Supp_G(c) subset O},
Tbar_G(O):=q_G{a in T_G:supp(a) subset O}.       (X1-3)
```

These definitions use the actual V005 paths and Q-408 distributions.  They
do not infer support from the abstract cycle lattice or from the Riesz map.
If `O_1 intersect O_2` is empty, elements of `K_G(O_1)` and `K_G(O_2)` are
disjoint physical cycle sectors.

Let `Loc_G` denote the poset generated by these relatively compact open
regions and the closed current supports they contain.  This lets the support
map below act on both test neighborhoods and the actual closed supports
without identifying either with an abstract cycle coordinate.

### 1.2 Definition of a locality/support-preserving generator

A proposed physical generator `R:G->G'` must carry the following geometric
data and certificates.  These clauses are the build specification, not
consequences inferred from a commuting algebraic square.

**LS-1 — actual region map.**  A declared proper local embedding `f_R` and
its induced support map

```text
f_R:M_G->M_G',
F_R:Loc_G->Loc_G'                                (X1-4)
```

preserves inclusions, finite unions, and disjointness.  It is induced by an
actual surface/path relation, not merely by the signed chain map.

**LS-2 — actual path and incidence refinement.**  There is an oriented
cell/path realization `f_R` with

```text
f_R compose gamma_(G,e)
 = ordered concatenation of the declared target child paths,
partial_(G') s_R=s_R^0 partial_G.                (X1-5)
```

The induced `S_R:K_G->K_G'` is injective for a primitive refinement and
preserves the complete old record-visible cycle family.

**LS-3 — current naturality and support.**  For every old cycle,

```text
J_G'(S_R c)=f_(R*)J_G(c),
Supp_G'(S_R c) subset F_R(Supp_G(c)).            (X1-6)
```

Consequently disjoint old sectors have disjoint target supports.

**LS-4 — support-local test transport.**  A map defined from the actual
field geometry,

```text
P_R:Tbar_G->Tbar_G',
P_R(Tbar_G(O)) subset Tbar_G'(F_R(O)),            (X1-7)
```

obeys the actual connection/current pairing square.  In particular, a test
supported over one old sector has zero pairing with every target current
whose support is disjoint from its image.

**LS-5 — kernel and local-duality compatibility.**  The support-local map,
not an algebraically manufactured substitute, must satisfy

```text
Phi_G' P_R=S_R Phi_G.                            (X1-8)
```

Then, and only then, arbitrary-profile restriction is physical:

```text
Kern_G'(H')[P_R a,P_R b]
 =Kern_G(S_R^*H'S_R)[a,b].                       (X1-9)
```

Equation `(X1-8)` also requires the Riesz duality to respect the local
old/new support split.  For disjoint target sectors it implies the
failure-capable condition

```text
g_(K,G')(S_R K_G(O),K_G'(V))=0
whenever F_R(O) intersect V=empty,               (X1-10)
```

together with the retained old-sector metric relation.  Positivity alone is
not `(X1-10)`.

**LS-6 — local field transport.**  On the old image, coframe, density,
connection, and curvature data obey their actual pullback/restriction laws;
their supports remain in `F_R(O)`.  E_post orientation and CTP reality are
carried covariantly.

**LS-7 — new physical support is retained.**  New target cycles and their
test classes remain outside `image(S_R)` and `image(P_R)`.  A new-cycle
kernel may be nonzero and may mix with another genuinely adjacent target
sector.  Locality forbids spurious mixing of disjoint sectors; it does not
delete new physics.

**LS-8 — family and refinement coherence.**  All preceding data form a
covariant no-selection family, compose on actual surface arrows, and agree
on actual common-refinement diamonds.  A formal diamond is not enough.

```text
LOCALITY_SUPPORT_CERTIFICATE = LS-1_THROUGH_LS-8
COMMUTING_RAIL_SQUARE_ALONE_SUFFICIENT = false / TYPE-R
```

### 1.3 Uniqueness theorem — why locality cannot be added after the square

Suppose `(X1-9)` is required for every bilinear profile `H'` and all test
classes.  Put

```text
v=Phi_G'P_R a,
w=S_R Phi_G a.                                   (X1-11)
```

Equality for every `H'` identifies the two tensor maps.  On each nonzero
connected batched component this gives

```text
Phi_G'P_R=sigma_R S_R Phi_G,
sigma_R in {+1,-1}.                              (X1-12)
```

The possible common sign is not ignored: LS-2/LS-3 require the transported
oriented current to be the actual forward path current, and E_post fixes that
orientation.  Hence `sigma_R=+1`.  Cross-component batching fixes the same
statement componentwise without selecting an orientation.  Since `Phi_G'`
is an isomorphism on the surface-visible test quotient,

```text
P_R
 =Phi_G'^(-1) S_R Phi_G
 =Abar_G'^(-1)R_G'S_RR_G^(-1)Abar_G
 =I_R^T.                                         (X1-13)
```

Thus V002's map is the unique arbitrary-profile pullback.  A physical
cycle-creating generator exists only when this unique map also satisfies
LS-1 through LS-7.  No alternative local map can be silently substituted
while retaining the full Q-408 square.

### 1.4 Generator-by-generator build result

| Generator | Actual locality/support proof | Status |
|---|---|---|
| identity | `F=id`, paths/tests/currents/supports unchanged | **PROVEN / TYPE-P** |
| admitted relabeling, frame-torsor, reality | ratified surface/bundle isomorphism maps paths and supports; orientation/reality acts covariantly | **PROVEN / TYPE-P** |
| finite restriction | retains the named old paths/tests and forgets later ones; cannot create support | **PROVEN on sealed restriction scope / TYPE-P** |
| zero-extension | old current is unchanged; identity cells carry zero current; support unchanged | **PROVEN / TYPE-P** |
| rank-preserving `Ref_path` | target children are parameter subpaths whose union is the parent path; `J` and kernel are literally the same distribution on the old image | **PROVEN / TYPE-P** |
| Gate-4 quotient descent | removes vertex coboundary presentation only; the complete conserved current and its actual support remain | **PROVEN / TYPE-P** |
| `Ext_cycle` | only `S_R` and objectwise endpoint surfaces exist; no `F_R,f_R,P_R`, `(X1-10)`, or LS-6 transport is ratified | **STOPPED / TYPE-U** |
| common refinement with only `Ref_path` legs | compositions of actual parameter subdivisions; supports agree | **PROVEN / TYPE-P** |
| common refinement with an `Ext_cycle` leg | two signed rails plus a target object do not supply local legs | **STOPPED / TYPE-U** |

The positive rows form exactly `Ref_0`, the maximal physical category named
at Q-425.  V003 neither shrinks that established scope nor promotes the open
rows.

---

## 2. X2 — sector-mixing counterexample as the leading regression

### 2.1 The permitted rail data

Let the old cycle live in physical region `U` and the new target cycle in a
disjoint region `V`.  On their localized cycle/test coordinates take

```text
K_G=R,
K_G'=R e_U direct-sum R e_V,
S_R x=(x,0),
Abar_G=Abar_G'=id,
R_G=1,
R_G'=[[1,epsilon],[epsilon,1]],
0<|epsilon|<1.                                   (X2-1)
```

The target metric is positive.  The Q-430 review establishes that the
standing covariance and positivity clauses do not force `epsilon=0`.
V002's unique rail pullback is

```text
I_R^T(1)=R_G'S_R(1)=(1,epsilon).                 (X2-2)
```

Its kernel square commutes because

```text
R_G'^(-1)I_R^T(1)=S_R(1).                       (X2-3)
```

### 2.2 Locality failure

The first coordinate in `(X2-2)` has support in `U`; the second is a test
coordinate on the disjoint sector `V`.  Hence

```text
I_R^T(Tbar_G(U)) not_subset Tbar_G'(F_R(U)),      (X2-4)
```

and the transported old test pairs nontrivially with a disjoint target
cycle.  LS-4 and `(X1-10)` fail.  The map is therefore rejected before it is
admitted as a physical generator.

### 2.3 A local replacement cannot preserve the full square

The geometrically local candidate is

```text
P_geo(1)=(1,0).                                  (X2-5)
```

But

```text
Phi_G'P_geo(1)
 =R_G'^(-1)(1,0)
 =(1/(1-epsilon^2))(1,-epsilon)
 !=(1,0)=S_R Phi_G(1).                           (X2-6)
```

By the uniqueness theorem, some rank-one profile detects this difference,
so `(X1-9)` fails.  The counterexample cannot be repaired by choosing the
local map after seeing the algebra.

### 2.4 Exact condition exposed

In block form relative to old support plus disjoint new support,

```text
R_G'=[[R_oo,R_on],[R_no,R_nn]].                  (X2-7)
```

Simultaneous locality and arbitrary-profile kernel compatibility require

```text
R_no=R_on=0,
R_oo transports R_G on the actual old image,     (X2-8)
```

as well as LS-1 through LS-7.  Equation `(X2-8)` is the coordinate form of
the basis-free support orthogonality `(X1-10)`.

```text
SECTOR_MIXING_WITNESS_COMMUTES_ALGEBRAICALLY = true
SECTOR_MIXING_WITNESS_LOCALITY_SUPPORT = FAIL
SECTOR_MIXING_WITNESS_ADMITTED_IN_V003 = false
SECTOR_MIXING_REGRESSION = PASS
```

This is a surface-geometry result, not a rail result: it uses the disjoint
actual supports of the Q-408 currents to reject a map that every abstract
carrier square accepts.

---

## 3. X3 — prior content re-proven on the locality/support specification

### 3.1 Cycle-creating and rank-preserving kernel squares

On `Ref_path`, parameter subdivision gives an actual local `P_R=id` on the
same physical test-form space.  Parent support equals the union of child
supports, the Riesz/current square is the Q-418 theorem, and direct
substitution gives `(X1-9)`.  Thus both the kernel and support squares are
proved.

For `Ext_cycle`, V002's algebraic identity remains a correct theorem:

```text
(I_R^T)^*Kern_G'(H')=Kern_G(S_R^*H'S_R).         (X3-1)
```

V003 retypes `(X3-1)` as a rail theorem.  It becomes a physical theorem only
after the independently geometric LS-1 through LS-8 package proves that
`I_R^T=P_R` is support-local.  That package is not instantiated.

The old pure-new-profile regression remains correctly handled.  If

```text
K_G'=S_RK_G direct-sum N_new,
H_new has support only on N_new,                  (X3-2)
```

then the old pullback is zero while fine new-cycle tests may see a nonzero
kernel.  LS-7 requires this content to survive.  Locality removes no adjacent
new-cycle physics; it only forbids support transfer between disjoint sectors.

```text
Ref_path_KERNEL_AND_SUPPORT_SQUARE = PROVEN
Ext_cycle_RAIL_KERNEL_SQUARE = PROVEN
Ext_cycle_PHYSICAL_KERNEL_AND_SUPPORT_SQUARE = TYPE-U
NEW_CYCLE_KERNEL_DELETED = false
```

### 3.2 Stagewise anchors

Each finite object retains V002's correct anchor:

```text
S_G=(G,B_G,K_G,Q_G,Tbar_G,Abar_G,R_G,Kern_G),    (X3-3)
```

with incidence/cycles/paths/support from V005, current/test/kernel maps from
Q-408, and Riesz data from DoR-019.  V003 adds the local sector functor
`O |-> (K_G(O),Tbar_G(O))`, which is derived objectwise from actual supports.

The relation anchor is separate.  `Ref_path` has one; `Ext_cycle` does not.
Two actual endpoint objects plus a signed map do not prove LS-1 through
LS-8.  This preserves Q-430's object-versus-relation distinction.

```text
STAGEWISE_OBJECT_ANCHORS = PROVEN
STAGEWISE_LOCAL_SECTORS = DERIVED_OBJECTWISE
Ext_cycle_RELATION_ANCHOR = OPEN / TYPE-U
```

### 3.3 Covariance family and orbit discipline

The one-orbit fiction remains deleted.  On the built scope, admitted actual
surface isomorphisms map

```text
K_G(O)->K_(fG)(fO),
Tbar_G(O)->Tbar_(fG)(fO),                        (X3-4)
```

and preserve disjointness, current support, reality, orientation signs, and
the Q-408 kernel formula.  No basis, frame, orientation, or realization
member is selected.

For the open cycle-creating scope, locality data must be supplied as a
covariant family over the full admitted surface groupoid.  One supported map
at one representative would not prove this family theorem.

```text
COVARIANCE_ON_BUILT_LOCAL_CATEGORY = PROVEN
COVARIANCE_ONE_ORBIT = false / TYPE-R
Ext_cycle_LOCAL_COVARIANT_FAMILY = OPEN / TYPE-U
```

### 3.4 Skeleton scope

There is still no all-stage embedded master skeleton.  Every support in
`(X1-2)` belongs to one actual finite member.  Maps compare stages only when
an actual support relation is present.  Edge-interior separation is asserted
only within the finite surface where Q-408 uses it.

```text
ALL_STAGE_MASTER_SKELETON = false / TYPE-R
STAGEWISE_ACTUAL_LOCAL_SURFACES = PROVEN
```

### 3.5 Composition

For built generators `R:G->G'` and `S:G'->G''`, the actual support maps and
test transports compose:

```text
F_(S compose R)=F_S compose F_R,
S_(S compose R)=S_S S_R,
P_(S compose R)=P_S P_R.                         (X3-5)
```

The support inclusions compose, disjointness is preserved, and

```text
Phi_G''P_SP_R=S_S Phi_G'P_R=S_SS_R Phi_G.        (X3-6)
```

Thus the kernel square composes on `Ref_0`.  This is a physical proof because
`F,P` are actual on that scope, not because `I^T` composes abstractly.

For `Ext_cycle`, `(X3-5)` is the required composition certificate after the
missing data exist.  Algebraic composition of `I^T` alone remains
insufficient.

```text
COMPOSITION_Ref_0 = PROVEN
COMPOSITION_Ext_cycle_PHYSICAL = OPEN / TYPE-U
```

### 3.6 Common refinement

An actual `Ref_path` diamond is a pair of parameter subdivisions of the same
realized paths into a common subdivision.  The child path unions, current
distributions, test maps, and supports agree route by route, so the physical
diamond commutes.

A diamond containing `Ext_cycle` must supply one actual target surface and
two LS-1 through LS-8 legs.  Signed-chain equality at the bottom does not
establish support equality.  No such full diamond family is ratified.

```text
COMMON_REFINEMENT_Ref_path = PROVEN
COMMON_REFINEMENT_Ext_cycle = OPEN / TYPE-U
FORMAL_OVERLAY_IS_PHYSICAL_REFINEMENT = false / TYPE-R
```

### 3.7 Surface geometry versus rails, re-run

| Claim | Surface geometry | Rails |
|---|---|---|
| finite Q-408 objects | actual paths, currents, supports, kernels | compatible finite diagrams |
| `Ref_path` | actual parameter subpaths and equal current supports | commuting restriction square |
| V002 `I_R^T` | no locality theorem | unique arbitrary-profile pullback |
| `Ext_cycle` | LS-1 through LS-8 absent | signed-chain/Riesz equations commute |
| common refinement | actual only on `Ref_path` diamonds | formal signed diamonds available |

The Q-429 rail-artifact audit also survives: no complete root is removable,
and the same three rail-only clauses remain removed.  The locality package is
physical because disjoint Q-408 supports distinguish it.  It is internal to
`B_Q408_REFINEMENT`, not a new declaration root.

```text
RAIL_ARTIFACT_ROOTS = none
RAIL_ARTIFACT_CLAUSES_REMOVED = 3
ROOT_COUNT_CHANGE = 0
```

---

## 4. X4 — falsifiers, anti-tuning, and exact stopping point

### 4.1 Seven cumulative regressions

| Regression | V003 execution | Result |
|---|---|---|
| pure new-cycle profile | old pullback can vanish while new target kernel remains; LS-7 protects it | **PASS** |
| covariance orbit/moduli | full no-selection family retained; one orbit not substituted | **PASS** |
| all-stage skeleton | finite local surfaces only | **PASS** |
| rank-preserving `Ref_path` | parameter-subpath/current-support proof rerun | **PASS** |
| cycle-creating upward quotient | none defined; V003 contravariant restriction retained | **PASS** |
| arbitrary-profile restriction | physical on `Ref_path`; rail-only/conditional on `Ext_cycle` | **PASS WITH HONEST SCOPE** |
| Riesz sector mixer | equations `(X2-1)`--`(X2-6)`; fails LS-4/LS-5 | **PASS — REJECTED** |

### 4.2 Five permanent regressions and joint condition

| Regression | Result |
|---|---|
| abstract-kernel substitution | **PASS** — all finite kernels are actual Q-408 kernels |
| circular `pi_Mx` | **PASS** — no reader or localization output defines support |
| misstated nonemptiness | **PASS** — full local Ext_cycle family remains TYPE-U |
| Hodge from isometry | **PASS** — locality or Hodge is never inferred from carrier isometry |
| objectwise minimum/restriction | **PASS** — no minimum or representative is selected |
| joint equalizer | **PASS** — no separate subpackage is promoted to EQ6 inhabitance |

### 4.3 Additional geometry falsifiers

1. **Unrelated paths.**  An injective signed map between cycles supported in
   disjoint unrelated regions satisfies the rails but has no `f_R` satisfying
   `(X1-5)`--`(X1-6)`; it fails membership.
2. **Disjoint-sector metric mixing.**  The symbolic `epsilon` witness fails
   `(X1-10)` and is rejected.
3. **Local-map substitution.**  `P_geo` is local but fails `(X1-8)`; it cannot
   be used to paper over the Riesz defect.
4. **Cycle deletion.**  Any primitive arrow with `ker(S_R)` nonzero deletes a
   V005-separated old cycle and fails LS-2.
5. **New-cycle deletion.**  Any restriction equality asserted on every fine
   test class would delete LS-7 content and fails.
6. **Formal common target.**  A combinatorial overlay without actual paths
   and supports fails LS-1/LS-2 before any square is formed.
7. **Support-local but field-incompatible.**  A path map without compatible
   coframe/density/connection/curvature transport fails LS-6.

### 4.4 Anti-tuning ledger

```text
1  Verify Q-430 and freeze its sector-mixing witness.
2  Freeze actual V005 paths/support and Q-408 current/kernel definitions.
3  Define local sectors before proposing any transport.
4  State LS-1 through LS-8 without inspecting a response consequence.
5  Prove the arbitrary-profile uniqueness theorem.
6  Run the Riesz mixer; accept the failure.
7  Re-prove only the already geometric Ref_0 generators.
8  Type Ext_cycle and its common refinements at the first absent datum.
9  Re-run the seven cumulative and five permanent regressions.
10 Inspect no response value, fixed point, end test, or measured datum.
```

### 4.5 Exact stopping point and missing kind

The full primitive generator requires a covariant, nonempty family

```text
LOCAL_SUPPORT_REFINEMENT_PACKAGE_R={
  actual local surface/path map f_R and region map F_R;
  support-preserving current map S_R induced by those paths;
  support-local test transport P_R;
  proof P_R=Phi_G'^(-1)S_RPhi_G;
  disjoint-sector orthogonality/locality of the retained Riesz duality;
  coframe/density/connection/curvature pullback on the old image;
  new-cycle support and kernel retention;
  covariance, composition, and actual common-refinement certificates
}.                                                  (X4-1)
```

Neither the ratified stack nor DoR-020 declares an inhabitant of `(X4-1)`.
The missing kind is **local support geometry plus a local-duality
compatibility theorem for cycle creation**.  This is stronger than a signed
chain map, a positive metric, or a commuting kernel square.  It is exactly
the physical datum that the sector-mixing surface can falsify.

```text
MISSING_OBJECT = LOCAL_SUPPORT_REFINEMENT_PACKAGE_R
MISSING_TYPE = GENUINELY_NEW_PHYSICS_MEMBER_DATA_WITHIN_B_Q408 / TYPE-U
NEW_SEVENTH_ROOT = false
MACHINERY_APPEAL = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```

### 4.6 Delta versus V002

| V002 content | V003 disposition |
|---|---|
| stagewise object anchors | retained and extended by objectwise local sectors |
| `Ref_path` physical square | retained; locality/support proof added |
| `Ext_cycle` `I_R^T` called physical | retyped rail-only until LS-1 through LS-8 |
| arbitrary-profile square | uniqueness proved; cannot substitute another local map |
| cycle-creation injectivity | retained as necessary, shown insufficient |
| composition of `I_R^T` | retained as rail theorem; physical composition scoped to built local maps |
| actual common target plus signed legs | shown insufficient; actual local legs required |
| covariance family | retained on built scope; open local family typed |
| stagewise skeleton | retained unchanged |
| three rail-clause removals | retained unchanged |
| full actual signed scope exhibited | withdrawn; maximal exhibit is `Ref_0` |
| sector-mixing regression | installed as leading permanent regression |

## Final board

```text
LOCALITY_SUPPORT = PROVEN_PER_GENERATOR_ON_Ref_0
LOCALITY_SUPPORT_Ext_cycle = STOPPED_AT_(X4-1) / TYPE-U
SECTOR_MIXING_REGRESSION = PASS

GENERATORS_ACTUAL_FINITE_AND_Ref_path = EXHIBITED
GENERATORS_CYCLE_CREATING = NOT_EXHIBITED
CYCLE_CREATING_RAIL_PULLBACK = PROVEN_BUT_NOT_PHYSICAL
CYCLE_CREATING_REAL_KERNEL_SUPPORT = RETAINED_AS_REQUIREMENT

GEOMETRY_ANCHORS_BUILT_SCOPE = PROVEN
COMPOSITION_BUILT_SCOPE = PROVEN
COMMON_REFINEMENT_BUILT_SCOPE = PROVEN
COVARIANCE_ONE_ORBIT = false
ALL_STAGE_MASTER_SKELETON = false

B_Q408_REFINEMENT_FULL_ROOT = OPEN / TYPE-U
RAIL_ARTIFACT_ROOTS = none
RAIL_ARTIFACT_CLAUSES_REMOVED = 3
JOINT_EQ6 = OPEN
C1_RESUMPTION = N/A
READY_FOR_HOSTILE_CHECK = yes

TARGET_TUNING_USED = false
ABSTRACT_STANDIN_USED = false
CIRCULAR_CERTIFICATE_USED = false
MEMBER_SELECTED = false
MACHINERY_APPEAL = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_bound = false
fixed_point_executed = false
end_test_executed = false
numeric_evaluation = false
measured_constant_compared = false
```

Seal this artifact, mirror artifact and sidecar byte-identically to
`alpha-program-archive/workspace/`, report hashes, and stop.  No register,
plan, tracker, git, commit, or push action belongs to this lane.
