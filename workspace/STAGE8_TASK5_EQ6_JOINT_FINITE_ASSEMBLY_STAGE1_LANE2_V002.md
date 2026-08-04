# STAGE 8 TASK 5 / EQ6 — JOINT FINITE ASSEMBLY STAGE 1 V002 — LANE 2

```text
ARTIFACT_TYPE = FINITE_PHYSICAL_FACE_REPAIR
REGISTER_HEAD_RELAY = Q-459
REGISTER_HEAD_LIVE = Q-460
SOURCE_V001 = STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md
SOURCE_V001_SHA256 = e21cee3081da06417109697352abe570c58dc6dda7d46e78f690d666bed128f5
REVIEW_OF_RECORD = STAGE8_TASK5_EQ6_ASSEMBLY_STAGE1_REVIEW_LANE1_V001.md
REVIEW_SHA256 = 049f6386835adcf5089a74d49add67c76973c5bb89fe3571c1e5fbceb8b0f5df

ACTION_FAMILY_CERT = BUILT
FORWARD_ETA_SQUARE = BUILT
PACKAGE_SQUARE = BUILT
CLASH_FOUND = none

MEMBER_BOUND = false
COMPLETED_AXIOM_INVOKED = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Preflight and governing equations

The output filename did not exist at preflight. The review hash matched
before reading. The sealed register had advanced from the relay's Q-459 to
Q-460; Q-460 only records the unrelated chain-V003 return and explicitly
loads this repair, so the commission remains current.

The V001 closures are struck. This build accepts the review's distinction:

```text
stagewise action fibers + pullback maps != a natural action-family section;
adjoint response compression           != a forward response map;
tagged finite shadows                  != one package natural transformation.
```

The three governing equations are, respectively,

```text
rho_f^Gamma(I_m)=I_n,
rho_f^Hess(D^2 I_m)=D^2 I_n;                       (W0-1 / J4)

Kernbar_m(j_prof,f H)=Eta_f(Kernbar_n(H));         (W0-2 / J12)

Nat_f(rho^pkg)=true in the typed multi-sorted package category,
with contravariant action/Hessian faces and the covariant response face.
                                                       (W0-3 / J15)
```

Every closure below proves its governing equation on the nose. A
compression, equal shadow, or formal composition is retained only in its
weaker role.

### 1.1 Full live tower and symbols

The category `I_F` is unchanged: all active finite stages, W3/DoR-008
restrictions, Ref_path subdivisions, flip/cycle-creating arrows,
disjoint/contact common refinements, covariance orbits, and every sealed
consumer arrow remain present.

| Symbol | Type |
|---|---|
| `Adm_base` | the full ratified nonempty R1/R2/R5 action family, not a selected member |
| `I_n` | the finite action coordinate `rho_Gamma,n(I)` of `I in Adm_base` |
| `R_n^rep` | the actual finite represented response carrier `im(Kernbar_n)` |
| `R_n^phys` | `R_n^rep` together with the declared finite boundary/contact class |
| `C_f` | the lawful old-current adjoint compression `S_f^{J,*}` |
| `Eta_f` | the forward physical response map constructed below |
| `Bot_n` | the independently owned tuple of all sealed finite consumer values at `n` |

No symbol is a reader-defined kernel, an abstract stand-in, or a newly bound
continuum member.

## 2. W1 — action-family compatibility certificate

### 2.1 The section family, not the product of fibers

The V001 domain was effectively

```text
product_(n in I_F) Adm_fin(n),
```

which admits incompatible stage coordinates. Replace that live action
coordinate by the image of the **single ratified family** under all of its
finite coordinate maps:

```text
Sec_R1(I_F) := {
  s_I=(I_n,D^2 I_n,Crit_n,C_red,n,Inv_CC,n)_n
  : I in Adm_base,
    I_n=rho_Gamma,n(I),
    D^2 I_n=rho_H,n(D^2 I)
}.                                                   (W1-1)
```

The map `I -> s_I` is applied to the entire `Adm_base` family. Nothing in
`(W1-1)` selects an `I`.

Nonemptiness is inherited from the ratified statement

```text
Adm_base != empty,                                  (W1-2)
```

not from the completed-existence axiom and not from a new choice. Thus
`Sec_R1(I_F)` is a nonempty covariant family of compatible sections.

### 2.2 Physical arrow maps

For every actual arrow `f:n -> m`, let `rho_f^Gamma` be the R2 finite
coordinate restriction, including its declared vertical-increment/cocycle
data. It is **not** replaced on a cycle-creating arrow by the V001 naive
precomposition formula.

Concretely, an R2 finite coordinate is a certified tuple, not a bare scalar
function.  Its arrow datum contains the unique decomposition

```text
I_m=I_n o rho_(m,n)+v_(m|n),                       (W1-3a)
```

with `I_n` the stored coarse coordinate and `v_(m|n)` the certified vertical
increment.  Define `rho_f^Gamma` on the R2 coordinate object by returning
that `I_n`.  Uniqueness of the finite-coordinate family makes this a map;
the R2 vertical-cocycle equation makes its composites independent of the
chosen factorization of `f`.

The R2 coordinate system obeys the transitivity equation

```text
rho_Gamma,n = rho_f^Gamma o rho_Gamma,m.            (W1-3)
```

This is the finite-coordinate restriction law. On a rank-preserving
Ref_path arrow its vertical increment is zero and it agrees with the lawful
scalar pullback retained from V001. On a cycle-creating arrow, the target
vertical increment remains physical target data while `rho_f^Gamma` returns
the old coordinate; no upward quotient is asserted.

For every `s_I in Sec_R1(I_F)`, equation `(W1-3)` computes

```text
rho_f^Gamma(I_m)
 =rho_f^Gamma(rho_Gamma,m I)
 =rho_Gamma,n I
 =I_n.                                               (W1-4)
```

This is J4's first equation on the nose.

### 2.3 Hessians, active sections, and reducing domains

R2 differentiation and the ratified R5 cube give

```text
rho_f^Hess(D^2 I_m)
 =D^2(rho_f^Gamma I_m)
 =D^2 I_n.                                          (W1-5)
```

Define the finite active and reducing data as the finite coordinates of the
same `I`:

```text
S_n(I)       := rho_n^S(S(I)),
Crit_n(I)    := rho_n^Crit(Crit(I)),
C_red,n(I)   := rho_n^red(C_red(I)).                (W1-6)
```

The R5 restriction/inverse cube then supplies, on every admitted arrow,

```text
rho_f^S S_m(I)=S_n(I),
rho_f^Crit Crit_m(I)=Crit_n(I),
rho_f^red C_red,m(I)=C_red,n(I),
rho_f^Inv Inv_CC,m(I)=Inv_CC,n(I).                 (W1-7)
```

Equations `(W1-6)`–`(W1-7)` derive the active-section and reducing-domain
stability that V001 merely asserted as `i_f(S_n) subset S_m`.

Covariance, reality, batching, quotient, R4 units, and automorphism actions
commute because all coordinates are restrictions of the same certified R1
tuple. For an admitted automorphism `sigma`,

```text
s_(sigma.I)(sigma n)=sigma.s_I(n),                 (W1-8)
```

so the whole orbit is retained.

### 2.4 Identity and composition

R2 restriction transitivity gives

```text
rho_id^Gamma=id,
rho_(gf)^Gamma=rho_f^Gamma rho_g^Gamma,
rho_id^Hess=id,
rho_(gf)^Hess=rho_f^Hess rho_g^Hess.               (W1-9)
```

Together with `(W1-4)`–`(W1-7)`, these equations make `Sec_R1(I_F)` a
family section on identities, Ref_path, flip, common-refinement, and every
sealed consumer arrow.

### 2.5 V6-1 excluded by proof

Take the review's pair

```text
Gamma_n=Gamma_m o i_f^Y+Psi_n,
Psi_n != 0,                                         (W1-10)
```

with every active jet of `Psi_n` zero. If this pair belonged to
`Sec_R1(I_F)`, it would satisfy `(W1-4)`. On a rank-preserving arrow, where
the physical coordinate restriction is the retained pullback,

```text
Gamma_n-rho_f^Gamma(Gamma_m)=Psi_n=0,              (W1-11)
```

contradicting `Psi_n != 0`. On a general arrow the same subtraction uses
the R2 coordinate restriction and again forces the mismatch to zero.

The witness is excluded because it fails the defining naturality equation,
not because its arrow or flat direction is removed. Compatible global flat
families remain: if `Psi in V_adm` is one ratified global deformation, then
`s_(I+Psi)` belongs to `Sec_R1(I_F)`. Thus W1 does not quotient the flat
freedom and does not select a representative.

```text
ACTION_FAMILY_CERT = BUILT
GOVERNING_EQUATIONS = (W1-4),(W1-5) ON_THE_NOSE
V6_INCOMPATIBLE_PAIR = EXCLUDED_BY_EQUALIZER_PROOF
```

## 3. W2 — forward `Eta` naturality square

### 3.1 Actual represented response carrier

At each finite stage let

```text
R_n^rep := im(Kernbar_n:Q_prof,n -> R_n^phys).      (W2-1)
```

Finite Q-408 faithfulness makes the represented profile unique on its
physical quotient:

```text
Kernbar_n(H)=Kernbar_n(H') -> H=H' in Q_prof,n.    (W2-2)
```

This is the well-definedness certificate for a forward map. It is not a
choice of inverse on an unrepresented complement.

### 3.2 Definition of the forward leg

For every `f:n -> m`, define on the represented carrier

```text
Eta_f(Kernbar_n(H))
  := Kernbar_m(j_prof,f H).                         (W2-3)
```

Equation `(W2-2)` proves `(W2-3)` independent of the representative `H`.
The right side is the actual Q-408 kernel on the actual refined profile; no
abstract kernel and no reader enters the definition.

For the declared finite boundary/contact class, extend by its already-built
transport:

```text
Eta_f(r+b):=Eta_f(r)+eta_f^boundary(b),
r in R_n^rep,
b in I_contact,n,                                  (W2-4)
```

interpreted on the declared quotient/direct-sum member when the intersection
is nontrivial. J13's safe-ideal law makes `(W2-4)` well defined. No arbitrary
extension to an unrepresented response complement is claimed or consumed by
a sealed finite consumer.

The governing equality is now the definition evaluated on the physical
carrier:

```text
Kernbar_m(j_prof,f H)
 =Eta_f(Kernbar_n(H)).                              (W2-5)
```

This is V1-4/J12-1 on the nose.

### 3.3 Identity, composition, covariance, and common refinements

Actual profile maps satisfy

```text
j_prof,id=id,
j_prof,gf=j_prof,g j_prof,f.                       (W2-6)
```

Therefore, for every represented response,

```text
Eta_id(Kernbar_n H)=Kernbar_n H,

Eta_g Eta_f(Kernbar_n H)
 =Eta_g(Kernbar_m(j_f H))
 =Kernbar_l(j_g j_f H)
 =Eta_(gf)(Kernbar_n H).                           (W2-7)
```

Boundary terms obey the J13 cocycle, so `(W2-7)` descends to `(W2-4)`.
Reality, orientation, frame, bundle gauge, and relabeling covariance follow
because `Kernbar` and `j_prof` carry those actual actions before `Eta` is
formed.

On a common refinement, each path obeys `(W2-5)`; the two results agree on
the physical bulk and differ, where allowed, by the same declared
boundary/contact class. This is the exact J12 common-refinement condition,
not equality manufactured by a zero extension.

### 3.4 Relation to the lawful compression

Retain V001's weaker map

```text
C_f:=S_f^{J,*}:R_m^phys -> R_n^phys.               (W2-8)
```

OLD_FID on the old response coordinate gives

```text
C_f Eta_f(r)=r for r in R_n^rep.                   (W2-9)
```

Thus the compression is a left inverse of the forward leg on the represented
image. It determines that forward leg **only if**

```text
ker(C_f) intersect R_m^adm = {0},                  (W2-10)
```

or an independently proved zero-defect/range certificate restricts the
admissible image to a subspace on which `C_f` is injective.

- On rank-preserving Ref_path arrows there is no new response summand;
  `(W2-10)` holds and the compression and forward map are equivalent.
- On a zero-defect cycle-creating arrow, the certified range condition also
  makes `(W2-10)` hold on the admitted image.
- On a general cycle-creating arrow, `ker C_f` may contain `R_new`, so
  compression alone does **not** determine `Eta_f`.

V002 never infers the forward leg from compression in the last case. Instead
`(W2-3)` determines it from the actual kernel and finite faithfulness. If

```text
Kernbar_m(j_f H)=S_f^J Kernbar_n(H)+v_new,
```

then `Eta_f` carries the actual `v_new`; it does not erase it. Applying
`C_f` recovers the old response by `(W2-9)`, exactly explaining why V1-5 was
weaker while V002's V1-4 is complete.

```text
FORWARD_ETA_SQUARE = BUILT
GOVERNING_EQUATION = (W2-5) ON_THE_NOSE
COMPRESSION_STATUS = RETAINED_AS_LEFT_INVERSE_ON_PROVED_SCOPE
```

## 4. W3 — one exact package square

### 4.1 Corrected package functor

Replace only the two failed V001 coordinates:

```text
F_phys(n) := (
  Sec_R1(I_F) evaluated at n,
  Kern_Q408^fin(n), C1_core^fin(n), Faith_fin(n),
  R_n^phys with Eta,
  C3_fin(n), R2_alg^fin(n), A_fin(n), Where_A1^fin(n)
).                                                   (W3-1)
```

For an arrow `f`, the action coordinate is the section restriction from W1,
and the response coordinate is the forward `Eta_f` from W2. The V001
scalar/Hessian pullback composition is retained on its lawful rank-preserving
scope; the V001 response compression is retained as `(W2-8)`. All other
component maps are carried unchanged.

W1 and W2 prove identity and composition for the repaired coordinates.
Here `FinPackage_020` is the multi-sorted diagram category fixed by J1–J15:
action/Hessian and finite restriction coordinates are contravariant, while
represented response transport is covariant.  Thus `F_phys` is one functor
to the structured package category; it is not an ill-typed ordinary product
of maps with one common variance.

### 4.2 The finite bottom functor

At each stage, `Bot_n` remains the tagged tuple of independently owned sealed
finite values:

```text
Bot_n=(Gate1-4_n,Q243_n,Q279_n,Q309_n,Q408_n,
       ActionBottom_n,WardBottom_n,ReaderBottom_n,WhereBottom_n). (W3-2)
```

For every `f:n -> m`, define `Bot(f)` by the **sealed** finite transition in
each tagged coordinate, with the same variance as its physical coordinate:

```text
Bot(f) := one structured bottom morphism over f, with

  Bot_act(f)  :Bot_act,m  -> Bot_act,n,
  Bot_Hess(f) :Bot_Hess,m -> Bot_Hess,n,
  Bot_resp(f) :Bot_resp,n -> Bot_resp,m,

  and Gate1-4/Q243/Q279/Q309/Q408/Ward/reader/where legs carrying
  their independently sealed variance.                              (W3-3)
```

The maps in `(W3-3)` are not inferred from `F_phys`; they are the independent
DoR-008 finite authorities. Their identities and compositions are the sealed
restriction/zero-extension/common-refinement equations.  `Bot(f)` therefore
denotes one structured bottom morphism, not one scalar arrow forced onto
coordinates of opposite variance.

### 4.3 Package-wide natural transformation

Define one map at each stage

```text
rho_n^pkg:F_phys(n)->Bot_n                         (W3-4)
```

by simultaneous physical coordinates:

```text
action section  -> pi_Jet,n(I_n)=BaseJet_n^bot;
response        -> the actual finite Kernbar/contact bottom;
C3              -> finite Ward/symbol bottom;
reader family   -> sealed algebraic scalar where defined;
Q408/where      -> actual current/path/bundle bottom;
C1/Faith        -> finite norm/bound/separation bottom. (W3-5)
```

The action arrow uses `(W1-4)`–`(W1-5)` before `pi_Jet`; the response arrow
uses `(W2-5)`, not compression. Consequently, for every `f:n->m`, the one
structured naturality square is the following tuple of on-the-nose
equalities:

```text
action:  rho_n^act  o rho_f^Gamma
          =Bot_act(f) o rho_m^act;

Hessian: rho_n^Hess o rho_f^Hess
          =Bot_Hess(f) o rho_m^Hess;

response:rho_m^resp o Eta_f
          =Bot_resp(f) o rho_n^resp;

Ward/where/reader/C1/Faith:
          the corresponding typed covariance equation.               (W3-6)
```

Equation `(W3-6)` is one equality in the multi-sorted package-arrow category:
each coordinate has its governing variance and all coordinates share the
same physical `f`, source/target objects, and bottom datum. It is not a list
of equal boundary values promoted to a square.

### 4.4 Three explicit spot instances

#### Instance A — rank-preserving `Ref_path`

For `f:n -> m` with zero R2 vertical increment,

```text
rho_f^Gamma(I_m)=I_n,
Eta_f Kernbar_n(H)=Kernbar_m(j_f H),
L_m(jJ)=L_n(J),
Q_m(jR)=Q_n(R).
```

Therefore both routes in `(W3-6)` return the same Q-279 expression

```text
(1-p)+p exp(L_n(J)-Q_n(R)/2),                      (W3-7)
```

with the same independent action jet and bundle/path bottom. Equality is on
the nose.

#### Instance B — cycle-creating flip

For a flip arrow, W1 uses the R2 coordinate restriction and retains the
target vertical action increment. W2 uses

```text
Eta_f Kernbar_n(H)=Kernbar_m(j_f H)
                  =old_response+v_new              (W3-8)
```

when the physical new response is nonzero. `Bot(f)` returns the old-stage
shadow, while `Bot_m` continues to contain the new-cycle target shadow.
Q-309's sealed old kernel/mixing zero and the action bottom therefore agree
after either route without deleting `v_new`. This is exact old-stage
restriction, not a false upward quotient.

#### Instance C — mixed/common refinement

For `n -f-> m -g-> l`, W1 gives

```text
rho_f^Gamma rho_g^Gamma(I_l)=I_n,
```

and W2 gives

```text
Eta_g Eta_f(Kernbar_n H)=Kernbar_l(j_g j_f H).
```

The disjoint/contact alternative route has the same bulk value and the J13
boundary cocycle in the same declared contact class. Applying `rho_n^pkg`
or the composite `Bot(gf)` therefore gives the identical Q-243 rotated
finite block and the same Ward/action/path bottoms. This spot instance
tests the package square, not merely either component square.

### 4.5 J15 status and the remaining stage

Equation `(W3-6)` closes the single exact finite package square. It does not
identify the algebraic reader with the physical Maxwell reader. Therefore:

```text
J4  = CLOSED_BY_W1;
J12 = CLOSED_BY_W2;
J15 = CLOSED_BY_W3;

REMAINDER:
  physical J2;
  J7 as the same physical-reader equation;
  simultaneous joint J1-J15 overlap diamonds with J2/J7 inserted.
```

The transport and package squares are now physical; the completed equalizer
and its joint diamonds are not asserted.

```text
PACKAGE_SQUARE = BUILT
GOVERNING_EQUATION = (W3-6) ON_THE_NOSE
```

## 5. W4 — obstruction and clash audit

| Possible obstruction | Governing calculation | Result |
|---|---|---|
| V6 incompatible section | `(W1-11)` forces its mismatch `Psi_n` to zero | **EXCLUDED BY PROOF** |
| no compatible action family | `Sec_R1(I_F)` is the image of nonempty `Adm_base` | **NO OBSTRUCTION** |
| action vertical increment | R2 coordinate restriction carries it; no naive pullback is substituted | **NO CLASH** |
| response variance | actual `Eta` is `(W2-3)`; compression is only its possible left inverse | **REPAIRED** |
| response representation ambiguity | finite faithfulness `(W2-2)` makes `Eta` well defined | **NO OBSTRUCTION** |
| new-cycle response | retained by `Eta` as `v_new`, not discarded | **NO CLASH** |
| package action bottom | every section member has the independently fixed `BaseJet_n^bot` | **AGREE ON THE NOSE** |
| package response bottom | J12 forward equation precedes the bottom restriction | **AGREE ON THE NOSE** |
| physical J2 | not used to claim W1–W3; remains explicit | **OPEN, NOT A CLASH** |

No incompatible existing physical values were found.

```text
CLASH_FOUND = none
HONESTY_STOP_TRIGGERED = false
```

## 6. W5 — battery, anti-tuning, and delta

### 6.1 V6 permanent regression

The V6 pair remains admissible in the product of stage fibers but is not a
section in `Sec_R1(I_F)`. The equalizer calculation `(W1-11)` is rerun for
every arrow orbit. No arrow is deleted and no flat direction is quotiented;
compatible global flat directions remain. **PASS.**

### 6.2 Nine geometric regressions

| Regression | V002 execution | Result |
|---|---|---|
| pure new-cycle profile | `Eta` carries its actual target response; `Bot_m` retains the target shadow | **PASS** |
| covariance orbit/moduli | full `Adm_base` section family and full response/bundle orbits retained | **PASS** |
| all-stage skeleton | W1/W2/W3 defined on every generator of unchanged `I_F` | **PASS** |
| rank-preserving `Ref_path` | R2 vertical increment zero; forward and compression equivalent by `(W2-10)` | **PASS** |
| cycle-creating upward quotient | none defined; target action/response increments remain | **PASS** |
| arbitrary-profile restriction | forward map defined from every physical represented profile; target kernel retained | **PASS** |
| Q-430 old-to-new mixer | cannot replace actual `j_prof` or R2 coordinate maps; RNL/local range still reject it | **PASS — REJECTED** |
| Q-432 `P=id` witness | admitted on rank-preserving arrows without global orthogonality | **PASS — ADMITTED** |
| Q-435 bundle/topology attack | actual smooth lift, pullback-bundle isomorphism, full rank, units, and `c_1` remain required | **PASS — ILL-TYPED MAP REJECTED** |

### 6.3 Additional attacks

| Attack | Result |
|---|---|
| rails look-alike | each closure cites `(W1-4)/(W2-5)/(W3-6)`, not a compression or product shadow | **PASS** |
| abstract kernel | `Eta` is induced only by actual finite `Kernbar` and actual `j_prof` | **PASS** |
| circular reader | no reader defines `Eta`; physical J2 remains open | **PASS** |
| false nonemptiness | only ratified `Adm_base` nonemptiness is used; no completed EQ6 witness asserted | **PASS** |
| contact laundering | only the declared safe contact class enters `(W2-4)` and common-refinement comparison | **PASS** |
| member binding | the entire `Adm_base` image is retained | **PASS** |
| shadow-only bottom | three physical instances exercise `(W3-6)` after W1/W2 | **PASS** |

### 6.4 Surface geometry versus rails

```text
SURFACE_GEOMETRY:
  W1 uses the ratified physical action coordinate family and its R2/R5
  restrictions; W2 uses the actual Q-408 kernel, actual profile transport,
  finite faithfulness, and the declared contact geometry.

RAILS:
  identity/composition bookkeeping and packaging into F_phys/Bot are
  categorical consequences only after W1/W2 supply those physical faces.

RAILS_SUBSTITUTED_FOR_PHYSICS = false.
```

### 6.5 Anti-tuning ledger

```text
1  freeze I_F and the review's three governing equations;
2  take the whole pre-existing Adm_base family and actual Q-408 kernels;
3  construct Sec_R1 and Eta before inspecting finite shadows;
4  prove W1/W2 identities and composition;
5  only then assemble Bot and test three sealed instances;
6  leave J2/J7 and the joint diamonds open.
```

No response consequence, threshold, fixed point, number, or target value
chooses an action section, response lift, or bottom map.

### 6.6 Delta versus V001

| V001 content | V002 disposition |
|---|---|
| scalar pullback composition `(V1-1)` | **KEPT** on its proved rank-preserving/coordinate scope |
| Hessian compression composition `(V1-2)` | **KEPT** as lawful compression; physical section equation supplied by W1 |
| Q-243/Q-279 exact shadows | **KEPT VERBATIM IN SUBSTANCE** and spot-tested in W3 |
| ordinary action/Hessian clash rows | **KEPT** on DoR-017 scope |
| finite Ward clash row | **KEPT** on admitted maps |
| stagewise product of action fibers claimed as J4 | **REPLACED** by `Sec_R1(I_F)` |
| `i_f(S_n) subset S_m` assertion | **REPLACED** by finite coordinates of one R1/R5 tuple, `(W1-6)`–`(W1-7)` |
| adjoint response compression claimed as J12 | **REPLACED** by forward physical `Eta`, `(W2-3)`–`(W2-5)` |
| compression | **RETAINED** as left inverse on its proved scope, `(W2-8)`–`(W2-10)` |
| tagged shadows claimed as J15 | **REPLACED** by the natural transformation `(W3-6)` |
| V001 `J4/J12/J15=CLOSED` claims | **STRUCK AND REPROVED** only through W1/W2/W3 |
| V001 remainder | **REPLACED** by physical J2/J7 plus joint overlap diamonds |
| V6 incompatible-section attack | **NEW PERMANENT REGRESSION**, excluded by `(W1-11)` |

No other V001 component construction is weakened or rebuilt.

## 7. Final board

```text
ACTION_FAMILY_CERT = BUILT
FORWARD_ETA_SQUARE = BUILT
PACKAGE_SQUARE = BUILT
CLASH_FOUND = none

J4 = CLOSED_ON_THE_NOSE_BY_W1
J12 = CLOSED_ON_THE_NOSE_BY_W2
J15 = CLOSED_ON_THE_NOSE_BY_W3

STAGE_2_REMAINDER = physical_J2
                    + physical_J7
                    + simultaneous_joint_J1-J15_overlap_diamonds

MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
