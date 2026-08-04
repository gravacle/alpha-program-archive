# STAGE 8 TASK 5 / EQ6 — ASSEMBLY STAGE 1 V002 REVIEW — LANE 1 V001

```text
ARTIFACT_TYPE = ADVERSARIAL_REVIEW_OF_RECORD
REGISTER_HEAD_CHECKED = Q-462
ARTIFACT_UNDER_REVIEW = STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V002.md
ARTIFACT_UNDER_REVIEW_SHA256 = e5381e6687dbdd5aed792bdddd1050ea7f39d17e748d6c9e374746c4cee37731
PRIOR_REVIEW_STANDARD_SHA256 = 049f6386835adcf5089a74d49add67c76973c5bb89fe3571c1e5fbceb8b0f5df

STAGE1_V002 = DEFECTIVE (Y1,Y2,Y3,Y4,Y5)
J4_J12_J15 = OPEN (J4 finite-coordinate map; J12 contact extension; J15 covariant bottom leg)

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Preflight and custody

The requested output and sidecar did not exist at preflight. The reviewed
artifact and its sidecar verified before reading. The sealed
questions-settled register verified at SHA-256
`e3541dfda05efd8e750ed9ed031d2183d7731942adb467814135066d9aff7802`
and ended at Q-462. Q-462 records V002 as pending this review; it does not
ratify any of V002's claims. `alpha_supervision/LOCKED_PROCESS.md` was read in
full.

| Authority | Verified SHA-256 | Use |
|---|---|---|
| artifact under review | `e5381e6687dbdd5aed792bdddd1050ea7f39d17e748d6c9e374746c4cee37731` | reviewed object |
| prior V001 review | `049f6386835adcf5089a74d49add67c76973c5bb89fe3571c1e5fbceb8b0f5df` | V1-V6 repair standard |
| J1-J15 constraint system | `d7dcbc3ad7c470c8aaf0d8407db625d3e910cf180cd7b035fbc96bdfe58471b4` | governing J4/J12/J15 equations |
| DoR-017 square V004 | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | actual R2 finite-coordinate type |
| representative-family theorem | `f0f8b09b1aa6a16c0ed0dffedbd275aba9e647fb5841fc8ce06ce9e6a8b00857` | `Adm_base`, vertical increments, flat-family freedom |
| local excision certificate | `d61a550a33bf1215c35f4d6f27cd2ec5d644b93a05e16d08fe3d43ded3416817` | contact and cycle-creating scope |

Custody is clean. This lane did not build V002. No register, plan, tracker,
git, commit, push, member binding, fixed-point execution, end test, or
numerical evaluation was performed.

## 2. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| Y1 action-family certificate | **KILL** | the two displayed composition calculations pass only on an enriched completed tuple; R2 does not make the source finite coordinate a function of the target finite coordinate when a vertical increment is allowed, and `(W1-11)` is false on that scope |
| Y2 forward square | **KILL** | `(W2-3)` is a valid represented-carrier map and never misuses compression, but `(W2-4)` is not well defined on a nontrivial represented/contact intersection; J13's cocycle does not supply the missing overlap equality |
| Y3 package square | **KILL** | the rank-preserving spot instance passes, but the cycle-creating response bottom needs an unbuilt covariant lift of the new-cycle shadow; V002 simultaneously says that shadow is retained and that `Bot(f)` returns only the old-stage shadow |
| Y4 J4/J12/J15 | **KILL** | J4 is blocked by Y1, J12 by Y2, and J15 by Y3; none of the three closures is confirmed |
| Y5 fresh attack | **KILL** | a target-coordinate collision defeats `rho_f^Gamma`, and an overlap-decomposition collision defeats the full `Eta_f`; both survive every equation V002 actually cites |

## 3. Y1 — action-family certificate

### 3.1 Two nontrivial composition calculations

Let `n -f-> m -g-> l`, with a rank-preserving `f` followed by a
cycle-creating `g`. R2 gives

```text
a_m = a_n o rho_(m,n),
a_l = a_m o rho_(l,m) + v_(l|m).
```

Hence

```text
a_l
 = a_n o rho_(m,n) o rho_(l,m) + v_(l|m)
 = a_n o rho_(l,n) + v_(l|n),

v_(l|n)=v_(l|m).
```

Projecting the **stored tuple** first along `g` and then `f` returns `a_n`,
as does projection along `gf`. This composition calculation passes.

For a cycle-creating `f` followed by a common-refinement arrow `g`,

```text
a_m = a_n o rho_(m,n) + v_(m|n),
a_l = a_m o rho_(l,m) + v_(l|m),
```

so

```text
a_l
 =a_n o rho_(l,n)
  +v_(m|n) o rho_(l,m)+v_(l|m).
```

The R2 cocycle identifies the final two terms with `v_(l|n)`. Again, the two
projections of the **stored tuple** agree. Thus V002 correctly checks the
cocycle; this is not yet a map on the finite stage object.

### 3.2 The type inflation in `(W1-3)`

DoR-017 R2 defines a completed member as

```text
(a,(a_N)_N,(v_(M|N))_(N<=M)),
```

with each `a_N in Act_N^quot` and with

```text
rho_Gamma,N(a)=a_N.
```

It does not define

```text
rho_f^Gamma:Act_m^quot -> Act_n^quot
```

from the bare target coordinate. V002 acknowledges the problem by declaring
at `(W1-3a)` that its argument is a certified tuple, not a bare scalar
function. That changes the domain. If the entire ancestral tuple is carried
at stage `m`, projection to `a_n` is tautological; it is not the all-arrow
finite action map that J4 and `F_phys(m)` require.

The distinction is witnessed on one cycle-creating arrow. Start with any R2
tuple and any nonzero admissible flat source action `psi_n`. Define a second
local R2 tuple by

```text
a'_n := a_n+psi_n,
a'_m := a_m,
v'_(m|n) := v_(m|n)-psi_n o rho_(m,n).             (Y1-1)
```

Then

```text
a'_n o rho_(m,n)+v'_(m|n)
 =a_n o rho_(m,n)+v_(m|n)
 =a_m=a'_m.                                        (Y1-2)
```

Both tuples satisfy the R2 decomposition and have the same target finite
action. Their source finite actions differ. The vertical increment is allowed
on a cycle-creating arrow. Flatness leaves the sealed active finite jets
unchanged. The cocycle extends this countermodel through a two-step chain by
setting

```text
delta v_(l|m)=0,
delta v_(l|n)=-psi_n o rho_(l,n),
```

which obeys

```text
delta v_(l|n)
 =delta v_(m|n) o rho_(l,m)+delta v_(l|m).
```

Therefore no function of `a_m` alone can return both `a_n` and `a'_n`.
R2's zero common-tail condition does not help: it says two completed members
with **every** finite coordinate equal are equal, not that one target
coordinate determines all earlier coordinates.

### 3.3 The old V6 witness and `(W1-11)`

On a rank-preserving identity extension R2 requires `v_(m|n)=0`. There the
old V6 mismatch is indeed forced to zero. That regression passes on that
scope.

V002 then says the same subtraction forces zero on a general arrow. It does
not. On a cycle-creating arrow, the governing R2 equation is

```text
a_m-a_n o rho_(m,n)=v_(m|n),                       (Y1-3)
```

not zero. Equation `(W1-11)` silently drops the allowed vertical term. The
countermodel `(Y1-1)` is a fresh incompatible-section witness: the mismatch
is absorbed by a lawful change of vertical increment while the target action
and every active finite jet remain fixed.

Consequently `Sec_R1(I_F)` is a legitimate **subfamily defined by an extra
equalizer condition**, but V002 does not prove that the whole retained
`Adm_base` family lands in it. Calling that subfamily the image of all
`Adm_base` members does not establish the missing theorem.

```text
Y1 = KILL
RANK_PRESERVING_V6_REGRESSION = PASS
GENERAL_ARROW_V6_REGRESSION = FAIL
ACTION_COMPOSITION_ON_ENRICHED_TUPLES = PASS
ACTION_MAP_ON_FINITE_COORDINATES = NOT_BUILT
```

## 4. Y2 — forward `Eta` square

### 4.1 What passes on the represented carrier

On

```text
R_n^rep=im(Kernbar_n),
```

finite faithfulness gives

```text
Kernbar_n(H)=Kernbar_n(H') => H=H' in Q_prof,n.
```

Because the actual profile transport `j_prof,f` is defined on that quotient,

```text
Eta_f(Kernbar_n(H)):=Kernbar_m(j_prof,f H)          (Y2-1)
```

is independent of the representative. This is the forward leg absent from
V001.

For a rank-preserving `Ref_path` arrow,

```text
Eta_f(Kernbar_n H)=Kernbar_m(j_f H),
```

and no new response summand occurs. For a flip/cycle-creating arrow,

```text
Eta_f(Kernbar_n H)
 =S_f^J Kernbar_n(H)+v_new,                         (Y2-2)
```

with the actual `v_new` retained. For either arrow and a composable `g`,

```text
Eta_g Eta_f(Kernbar_n H)
 =Kernbar_l(j_g j_f H)
 =Eta_(gf)(Kernbar_n H).
```

These are exact calculations. V002 also states `(W2-10)` correctly:
compression determines a forward leg only where its kernel intersects the
admitted image trivially (or where an independent range certificate supplies
that fact). The artifact does not use compression to infer `(Y2-2)` on the
general cycle-creating scope. Those parts pass.

### 4.2 The full physical carrier is not covered

V002 extends `(Y2-1)` by writing

```text
Eta_f(r+b)=Eta_f(r)+eta_f^boundary(b),
r in R_n^rep,
b in I_contact,n.                                  (Y2-3)
```

It explicitly allows a nontrivial intersection between `R_n^rep` and
`I_contact,n`. Let

```text
x in R_n^rep intersect I_contact,n.
```

The same physical element has decompositions `x+0` and `0+x`. Formula
`(Y2-3)` is well defined only if

```text
Eta_f^rep(x)=eta_f^boundary(x)                      (Y2-4)
```

in the stated quotient/direct-sum member. V002 neither states the quotient
relation nor proves `(Y2-4)`.

The cited J13 law is

```text
beta_(gf)=beta_g+Eta_g(beta_f)
```

together with closure, invariance, restriction naturality, and absence of a
record-visible bulk cycle in `I_contact`. It is a path cocycle. It does not
imply equality of the represented and boundary transports on their
intersection. Indeed one can alter `eta_f^boundary(x)` by a nonzero contact
element and propagate the alteration by the same cocycle while preserving
all equations V002 cites. The two decompositions then receive different
images.

Thus the represented forward leg is built, but the claimed map on
`R_n^phys` is not. Common-refinement agreement inherits the same unresolved
overlap.

```text
Y2 = KILL
ETA_ON_R_REP = BUILT_AND_FUNCTORIAL
W2_10_SCOPE_DISCIPLINE = PASS
ETA_ON_R_PHYS = NOT_WELL_DEFINED_WITHOUT_INTERSECTION_CERTIFICATE
```

## 5. Y3 — package square and explicit instances

### 5.1 Instance A: rank-preserving `Ref_path`

With zero vertical increment and no new response summand,

```text
L_m(jJ)=L_n(J),
Q_m(jR)=Q_n(R).
```

Both finite routes therefore return

```text
(1-p)+p exp(L_n(J)-Q_n(R)/2).                      (Y3-1)
```

The Q-279 instance passes. The exact finite Keldysh rotation also preserves
the Q-243 zero ordered retarded block on this arrow. This confirms a common
finite shadow, not the all-arrow package square.

### 5.2 Instance B: cycle creation exposes the bottom-leg gap

For `r_n=Kernbar_n(H)`, V002 correctly retains

```text
r_m=Eta_f(r_n)=S_f^J r_n+v_new.                    (Y3-2)
```

Its naturality equation requires

```text
rho_m^resp(r_m)=Bot_resp(f)(rho_n^resp(r_n)).       (Y3-3)
```

The left side includes the independently sealed target shadow of `v_new`
whenever that new-cycle response is record-visible. The right side can
include it only if `Bot_resp(f)` is an independently constructed **covariant
lift** from the old bottom to the new bottom.

The available DoR-008 finite authority is a restriction back to the old
stage. V002 supplies no covariant lift theorem. Its own Instance B says both
that `Bot(f)` returns the old-stage shadow and that `Bot_m` retains the
new-cycle target shadow. Those statements make `(Y3-3)` unequal unless the
new shadow vanishes. Setting it to zero would contradict V002's pure
new-cycle regression and would reinstate V001's deleted-content error.

This is not repaired by calling `Bot(f)` a structured morphism. Variance is a
type, not a source of the missing new-cycle datum.

### 5.3 Instance C and consumer coverage

On the represented bulk, the mixed composite passes because

```text
Eta_g Eta_f(Kernbar_n H)=Kernbar_l(j_g j_f H).
```

On contact terms it still needs `(Y2-4)`. At the bottom it still needs the
covariant lift in `(Y3-3)`. Thus Instance C does not close either missing
face.

The remaining `Ward/where/reader/C1/Faith` row in `(W3-6)` is stated only as
“the corresponding typed covariance equation.” V001 contains lawful
component formulas on their proved scopes, but V002 does not recompute an
all-arrow bottom map for them. More importantly, one failed action coordinate
and one failed response coordinate are already enough to prevent one package
natural transformation. The sealed consumers remain individually exact; they
are not all covered through one verified functor.

```text
Y3 = KILL
REF_PATH_PACKAGE_INSTANCE = PASS
CYCLE_CREATING_PACKAGE_INSTANCE = FAIL
MIXED_PACKAGE_INSTANCE = FAIL_ON_CONTACT_AND_BOTTOM
ONE_FUNCTOR_COVERAGE = NOT_PROVEN
```

## 6. Y4 — J4, J12, and J15

The prior T3 closure conditions are unchanged.

| Constraint | Required object | V002 result |
|---|---|---|
| J4 | compatible action/Hessian family on every actual arrow, with a map on the stated finite coordinate type | **OPEN** — W1 projects an enriched tuple; `(Y1-1)` refutes a map from the bare target coordinate |
| J12 | forward `Eta`, composition, and common-refinement agreement on the full physical response/contact carrier | **OPEN** — represented bulk passes, but the overlap equality `(Y2-4)` is absent |
| J15 | one package-wide exact DoR-008 square on the repaired coordinates | **OPEN** — the action face is ill typed and the cycle-creating bottom lacks the covariant response lift |

The three closures are therefore not confirmed. The honest next remainder is
not only physical J2/J7 and the simultaneous joint diamonds; it still includes
the bounded repairs named above.

```text
Y4 = KILL
J4 = OPEN
J12 = OPEN
J15 = OPEN
```

## 7. Y5 — fresh attacks and geometry/rails split

### 7.1 Fresh attack 1: target-coordinate collision

Equations `(Y1-1)`-`(Y1-2)` give two admitted R2 decompositions with the same
target finite action and different source finite actions. This attacks the
new V002 construction directly; it was not the prior V6 witness. It proves
that attaching the ancestral tuple is essential to W1, hence that W1 has
changed the stage object's type.

### 7.2 Fresh attack 2: overlap-decomposition collision

Equation `(Y2-3)` gives two outputs for one physical response whenever
`R_n^rep intersect I_contact,n` is nontrivial and `(Y2-4)` is absent. This
attack leaves represented faithfulness, the J13 cocycle, covariance, and all
finite bulk shadows intact. It isolates the exact missing certificate.

### 7.3 Surface geometry versus rails

```text
SURFACE_GEOMETRY:
  the actual profile transport and finite Kernbar do produce the represented
  forward response Eta; the R2 vertical increment is actual cycle-creating
  action data and cannot be dropped.

RAILS:
  carrying the entire ancestral tuple at every stage makes projection
  formally functorial, and naming a multi-sorted Bot arrow makes the variance
  look consistent. Neither rail proves a finite-coordinate action map, a
  contact-overlap equality, or a covariant new-cycle bottom lift.

RAILS_SUBSTITUTED_FOR_MISSING_GEOMETRY = true in W1 and W3;
REPRESENTED_ETA_GEOMETRY = genuine but incomplete in W2.
```

No forbidden act occurred. All parameters remain symbolic. The three gates
remain false.

```text
STAGE1_V002 = DEFECTIVE (Y1,Y2,Y3,Y4,Y5)
J4_J12_J15 = OPEN (J4 finite-coordinate map; J12 contact extension; J15 covariant bottom leg)

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
