# STAGE8 TASK 4A: MAP-1 EXTENSION CROSS-REVIEW — CODEX LANE 2 V001

Date: 2026-08-03  
Task: PASTE 430 / Task 4a / adversarial cross-review of Q-347  
Lane: CODEX LANE 2  
Register head: Q-348

```text
LEAD_RESULT = SPLIT

EXTENSION_RANK01 = KILLED
KILL_LOCATION = E2.4_RESTRICTION_NATURALITY_SQUARE_AS_WRITTEN
KILL_REASON =
  rho_G,MN compose T_(M,G_M)^char and T_(N,G_N)^char have different
  source domains; the required precomposition by j_NM^Q is absent

CORRECTED_BUT_NOT_INSTALLED_EQUATION =
  rho_G,MN compose T_(M,G_M)^char compose j_NM^Q
    = T_(N,G_N)^char

RANK2_OBSTRUCTION = CONFIRMED
SCOPE = maps depending only on the single consumed terminal scalar Z_N

PREFIX_FAMILY_ESCAPE = OPEN |
  Q-348 removes the one-dimensional information obstruction, but the
  family-natural relative-cell-to-incidence-edge realization and its
  batching/restriction square remain unbuilt

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The restriction-square failure is bounded and repairable by inserting the
already-cited source inclusion. It is nevertheless a kill of the reviewed
rank-0/1 theorem **as written**: this review does not repair Lane 1's build or
self-certify the corrected object. The fixed-stage classification, the S8-A
automorphism obstruction, and its kernel/image witness survive independently.

---

## 1. Preflight, custody, and authorities

The artifact under review was hash-verified before it was read:

```text
artifact =
  alpha-program-archive/workspace/
  STAGE8_TASK4A_MAP1_FULL_FAMILY_EXTENSION_LANE1_V001.md

expected_sha256 =
  04002fb49fcf91a544544a798519cfe56017f42659a1eb6d6947f9defbc76a5a

actual_sha256 =
  04002fb49fcf91a544544a798519cfe56017f42659a1eb6d6947f9defbc76a5a

sidecar_verification = PASS
```

The live questions-settled register was checked through Q-348. Q-347 is the
Lane-1 extension theorem under review; Q-348 is the parallel trace-kernel
sufficiency theorem. No later entry supersedes either one.

The following load-bearing authorities and their sidecars were also verified:

| Authority | Verified SHA-256 | Use in this review |
|---|---|---|
| Q-313 Map-1 build | `ea8f4e9a79a9e4aca4a0b9e9aab470d78cd4d9c78794c20d9e979c0db16fbeab` | exact square map and sequential source inclusion |
| Q-315 physical squares | `f886284c632f238bb01d02de2cc64e3f7ed76c0bae4ba14487ac0b2bde7a22e3` | fixed-square restriction square |
| DoR-015 / V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | physical quotient and complete conserved-cycle separation |
| DoR-016 / V004 | `69f4d93b9f84075a3112fb011b9838f380fb8c0341610572170cf7a13d5aed08` | doubled relative character, batching, and zero extension |
| Q-348 sufficiency arm | `d9a507fc8b5645981ed1519a04e180620ee7c22f65d5c9425437a701185f9001` | every-prefix trace isomorphism |

`LOCKED_PROCESS.md` was read in full. This artifact performs review and
structural mathematics only. It does not edit the register, governing plan,
tracker, or git state.

```text
DOES_THE_OBJECT_EXIST = yes | Q-347 artifact
IS_THE_VERSION_CURRENT = yes | register head Q-348
ARE_THE_INPUTS_PRESENT = yes
PREFLIGHT = PASS
```

---

## 2. Verdict table Y1–Y7

| Item | Verdict | Determination |
|---|---|---|
| Y1 rank-0/1 extension | **KILL** | Uniqueness and all non-restriction certificates recompute, but E2.4's displayed naturality equation is ill-typed because `j_NM^Q` is missing. |
| Y2 fixed-stage classification | **PASS** | Continuous batching-compatible scalar lifts are exactly the `Hom(C_G,Z)` family; affine, nonlinear, and orientation-reversed candidates add no unclassified member. |
| Y3 automorphism obstruction | **PASS** | The S8-A edge exchange fixes terminal `Z_N`, sends `c_3` to `-c_3`, and forces `lambda(c_3)=0` without using a relative-label-to-edge functor. |
| Y4 kernel/image disclosure | **PASS** | `Ann(image s_G^lambda)=ker(lambda)` and the rank/dimension bounds are exact. |
| Y5 prefix-family escape audit | **PASS WITH SCOPE CORRECTION** | The obstruction is conclusive for one terminal scalar only. Q-348's prefix family admits enough coordinates to evade the dimension and fixed-domain automorphism arguments; the actual family-natural descent remains `TYPE-U`. |
| Y6 regressions and selection scan | **PASS, excluding killed E2.4 certificate** | One-edge, S8-A, reality, and identity-zero-extension results recompute; no hidden member is selected. |
| Y7 fresh attack | **PASS WITH DEPENDENCY DISCLOSURE** | Powers, affine translates, nonlinear maps, and wild homomorphisms do not evade the fixed-stage classification. Rank-one uniqueness, however, is uniqueness under the exact equation `Hol_c T=Z`, not a consequence of square compatibility alone on unrelated rank-one objects. |

---

## 3. Y1 — rank-zero/rank-one extension

### 3.1 Rank zero

For a connected tree,

```text
C_G=ker(B_G^T) intersect Z^(E_G)={0},
Q_G=U(1)^(E_G)/Gamma_G={*}.
```

There is exactly one map `Q_rel,N -> {*} `. Its quotient compatibility,
reality covariance, and target-side naturality are automatic. A nontrivial
open-path trace may remain on DoR-016's endpoint-covariant access carrier,
but DoR-015 supplies no scalar cycle coordinate on a tree. The reviewed
artifact correctly discloses that the terminal map does not satisfy a
nonexistent equation `Hol compose T=Z` there.

```text
Y1_RANK0_UNIQUENESS = PASS
Y1_RANK0_ALLOW_REQUIRE_SPLIT = PASS
```

### 3.2 Rank one: existence and conditional uniqueness

Let `C_G=Z c_G` for the primitive oriented generator carried by a realization
member. DoR-015 gives the quotient coordinate isomorphism

```text
Hol_(c_G):Q_G -> U(1).
```

Consequently

```text
T_(N,G)^char=Hol_(c_G)^(-1) compose Z_N
```

exists and is the unique map satisfying

```text
Hol_(c_G) compose T_(N,G)^char=Z_N.                (Y1-1)
```

If `T'` satisfies `(Y1-1)`, injectivity of `Hol_(c_G)` gives `T'=T`
pointwise. This is exact uniqueness under the Map-1 factorization condition.

The orientation family is handled covariantly:

```text
c_G -> -c_G,
Z_N -> conjugate(Z_N),
T -> Theta_G T.
```

No generator is selected globally.

```text
Y1_RANK1_EXISTENCE = PASS
Y1_RANK1_UNIQUENESS_UNDER_HOL_T_EQUALS_Z = PASS
Y1_ORIENTATION_SELECTION = false | TYPE-S
Y1_QUOTIENT_COMPATIBILITY = PASS
```

### 3.3 The firing: restriction naturality is ill-typed as written

The reviewed artifact declares

```text
rho_G,MN:Q_(G_M)->Q_(G_N),
T_(M,G_M)^char:Q_rel,M->Q_(G_M),
T_(N,G_N)^char:Q_rel,N->Q_(G_N),
j_NM^Q:Q_rel,N->Q_rel,M.
```

It then displays

```text
rho_G,MN compose T_(M,G_M)^char
  =T_(N,G_N)^char.                                 (reviewed E2.4)
```

The left side has domain `Q_rel,M`; the right side has domain `Q_rel,N`.
They cannot be equal. Moreover, applying `Hol_(c_GN)` to the displayed left
side gives `Z_M`, not the claimed `Z_N`.

The type-correct square would be

```text
rho_G,MN compose T_(M,G_M)^char compose j_NM^Q
  =T_(N,G_N)^char.                                 (Y1-2)
```

Indeed, the authorities cited by the artifact would prove `(Y1-2)`:

```text
Hol_(c_GN) rho_G,MN T_(M,G_M)^char j_NM^Q
 =Hol_(c_GM) T_(M,G_M)^char j_NM^Q
 =Z_M j_NM^Q
 =Z_N
 =Hol_(c_GN) T_(N,G_N)^char.
```

Injectivity of `Hol_(c_GN)` would then close the proof. But `(Y1-2)` is not
the equation the reviewed artifact certifies. Installing it is a repair to
Lane 1's object, outside this cross-review's custody.

```text
Y1_RESTRICTION_NATURALITY_AS_WRITTEN = FAIL
Y1_FAILURE_TYPE = DOMAIN_MISMATCH
Y1_MINIMAL_REPAIR = insert j_NM^Q on the left
Y1_CORRECTED_SQUARE_DERIVABLE_LOOKING = true
Y1_VERDICT = KILL
```

### 3.4 Remaining rank-one certificates

Identity zero extension contributes a unit character and leaves `T`
unchanged. Batching is multiplicative after separating the scalar section
`s_G=Hol_(c_G)^(-1)`:

```text
s_G(Z_2 Z_1)=s_G(Z_2)s_G(Z_1).
```

On the sealed square, `c_G=c_square` and the formula is exactly Q-313's
`T_N^char`; Q-315's already-built fixed-square restriction square is not
altered.

```text
Y1_REALITY = PASS
Y1_BATCHING = PASS
Y1_IDENTITY_ZERO_EXTENSION = PASS
Y1_Q313_AGREEMENT = PASS
Y1_Q315_FIXED_SQUARE_AGREEMENT = PASS
```

These passes do not cure the missing arrow in E2.4.

---

## 4. Y2 — complete fixed-stage classification

Let `rank C_G=b`. DoR-015 identifies

```text
Q_G isomorphic to Hom(C_G,U(1)).
```

A lift depending only on one terminal scalar and respecting exact CTP
batching is a continuous homomorphism

```text
s_G:U(1)->Hom(C_G,U(1)).
```

For each `c in C_G`, evaluation gives a continuous character of `U(1)`:

```text
ev_c compose s_G:U(1)->U(1),
(ev_c compose s_G)(z)=z^(lambda(c))
```

for one integer `lambda(c)`. Since `s_G(z)` is itself a character in `c`,
the exponent is additive:

```text
lambda(c+c')=lambda(c)+lambda(c').
```

Thus `lambda in Hom(C_G,Z)` and

```text
Hol_G(s_G(z))(c)=z^(lambda(c)).                    (Y2-1)
```

Conversely every `lambda in Hom(C_G,Z)` defines a continuous group
homomorphism by `(Y2-1)`. Hence

```text
Hom_cont(U(1),Q_G)
 isomorphic to Hom(C_G,Z).
```

The classification is exhaustive for the declared class.

Potential escape constructions fail as follows:

1. An affine translate `q_0 s_G(z)` violates batching unless
   `q_0=q_0^2`, hence `q_0` is the identity in a group.
2. A nonlinear continuous phase rule violates multiplicativity and is not a
   CTP-batching-compatible scalar-character lift.
3. Complex conjugation and orientation reversal are already the negative
   integer covectors.
4. A discontinuous abstract group homomorphism is outside the finite compact
   topology and the continuous character class required by the source and
   quotient structures.

```text
UNCLASSIFIED_CONTINUOUS_BATCHING_LIFT_FOUND = false
FIXED_STAGE_LIFT_FAMILY = Hom(C_G,Z)
Y2_VERDICT = PASS
```

Terminology precision: nonprimitive `lambda` gives a homomorphism with a
finite source kernel, not an embedded one-parameter subtorus. The artifact
states this later in its kernel account, so retaining all `lambda` does not
invalidate the classification.

---

## 5. Y3 — S8-A automorphism obstruction

Use the admitted two-vertex, three-edge stage

```text
a:1->2,
b:2->1,
d:1->2.
```

In edge order `(a,b,d)`, conservation is

```text
B_M^T(q_a,q_b,q_d)
 =(-q_a+q_b-q_d, q_a-q_b+q_d).
```

The following cycles are conserved:

```text
c_1=(1,1,0),
c_2=(0,1,1),
c_3=(1,0,-1)=c_1-c_2.
```

They span a rank-two lattice. The admitted automorphism `sigma` exchanges
the parallel edges `a` and `d` and fixes `b`, so

```text
sigma(c_1)=c_2,
sigma(c_2)=c_1,
sigma(c_3)=-c_3.                                  (Y3-1)
```

For a construction whose only source datum is terminal `Z_N`, the source
datum has no incidence-edge label and is fixed by `sigma`. Naturality gives

```text
lambda compose sigma=lambda.
```

Therefore

```text
lambda(c_1)=lambda(c_2),
lambda(c_3)=lambda(c_1-c_2)=0.                    (Y3-2)
```

Equivalently, applying invariance directly to `c_3` gives
`lambda(c_3)=lambda(-c_3)=-lambda(c_3)`, hence zero in `Z`.

Consequently

```text
Hol_G(s_G^lambda(z))(c_3)=1
```

for every source scalar. V005 retains the complete basis-free current family
`ker(B_M^T)` and proves it separates the Gate-4 quotient. Since `c_3` is a
nonzero member, quotient classes with nontrivial `c_3` holonomy are
record-visible but absent from the lift's image.

The proof uses only:

```text
target cycle lattice,
target edge-exchange automorphism,
terminal scalar's lack of an edge label,
family naturality.
```

It does not assign a relative-history cell to an incidence edge and therefore
does not assume the unbuilt relative-label-to-edge functor.

```text
Y3_SIGMA_ACTION = PASS
Y3_LAMBDA_C3_ZERO = PASS
Y3_C3_RECORD_VISIBLE = PASS
Y3_UNBUILT_FUNCTOR_USED = false | TYPE-S
Y3_VERDICT = PASS
```

---

## 6. Y4 — kernel and image disclosure

For the classified map `s_G^lambda`, a cycle `c` annihilates its entire image
exactly when

```text
z^(lambda(c))=1 for every z in U(1),
```

which holds exactly when `lambda(c)=0`. Hence

```text
Ann(image(s_G^lambda))=ker(lambda).                (Y4-1)
```

If `lambda` is nonzero, its image in `Z` has rank one, so rank-nullity over
the free abelian lattice gives

```text
rank ker(lambda)=rank(C_G)-1.
```

For `lambda=0`, the annihilator is all of `C_G`; the artifact's weaker
uniform bound

```text
rank ker(lambda)>=rank(C_G)-1
```

is therefore correct in every case.

On compact tori,

```text
dim image(s_G^lambda)<=1,
dim Q_G=rank(C_G).
```

Thus for `rank(C_G)>=2`, no one-scalar lift is surjective or separating on
the complete target quotient. If `lambda` is primitive, `s_G^lambda` is
injective and the only source kernel before it is `ker Z_N`; if `lambda` has
content `d>1`, the additional source kernel is the finite group of `d`th
roots; `lambda=0` kills the entire scalar source.

For S8-A, `(Y3-2)` supplies the exact target-side witness
`c_3 in Ann(image)`.

```text
Y4_ANNIHILATOR_IDENTITY = PASS
Y4_RANK_BOUND = PASS
Y4_DIMENSION_BOUND = PASS
Y4_S8A_WITNESS = PASS
Y4_VERDICT = PASS
```

---

## 7. Y5 — escape-hatch audit: the complete prefix family

### 7.1 What Q-347's obstruction actually proves

Q-347 classifies maps with source

```text
single terminal scalar z=Z_N in U(1).
```

That source has dimension one and carries the trivial action of the S8-A
edge exchange because it has forgotten every cell label. The dimension bound
and `(Y3-2)` are conclusive for that class.

They do **not** classify maps whose source is the Q-348 projective family

```text
(Z_0,Z_1,...,Z_N),
Z_0=1.
```

Q-348 proves the exact inverse

```text
r_j=Z_(j-1)^(-1)Z_j,                              (Y5-1)
```

uniformly for both faithful orientations. Therefore the prefix source at
stage `N` is isomorphic to the full cellwise relative-character torus
`U(1)^N`, not one `U(1)`.

### 7.2 Explicit S8-A algebra showing the obstruction does not persist

To test only the algebraic sufficiency—not to install an unratified map—take
three recovered cell characters provisionally associated with the three
S8-A edges:

```text
(r_a,r_b,r_d).
```

Define a quotient character by

```text
Hol_G(S(r))(c)=r_a^(c_a) r_b^(c_b) r_d^(c_d).
```

Then

```text
Hol_G(S(r))(c_1)=r_a r_b,
Hol_G(S(r))(c_2)=r_b r_d,
Hol_G(S(r))(c_3)=r_a r_d^(-1).                    (Y5-2)
```

The `c_3` coordinate is no longer forced to one. Under the simultaneous
domain action

```text
(r_a,r_b,r_d)->(r_d,r_b,r_a)
```

and target action `(Y3-1)`, `(Y5-2)` is equivariant: the first two
coordinates exchange and the third inverts. Thus the fixed-domain
automorphism argument and the one-dimensional image bound both disappear
once the source retains the edge-permuted cellwise family.

This is a countermodel to any claim that Q-347 forbids **all** prefix-family
descents. It is not yet a ratified construction.

### 7.3 Why the escape remains open rather than constructed

The displayed algebra used a provisional association

```text
relative cell labels (1,2,3) <-> incidence edges (a,b,d).
```

Q-348 reconstructs the cellwise characters, but it does not provide that
association over the complete no-selection realization family. The live
stack still needs:

1. a family-natural relative-cell-to-incidence-edge realization map;
2. its action on prefix coordinates under every admitted graph automorphism;
3. compatibility with rank-changing restriction/refinement arrows;
4. the batching square showing how fine interior prefixes descend when a
   coarse source batch forgets them;
5. agreement with Q-313 and Q-315 on the sealed square;
6. proof that no incidence-cycle direction is lost after quotienting.

Without these certificates, `(Y5-2)` is a typed diagnostic, not Map 1.

```text
SINGLE_TERMINAL_SCALAR_OBSTRUCTION = CONFIRMED | TYPE-R
PREFIX_DATA_REMOVES_DIMENSION_OBSTRUCTION = true | TYPE-P | premise:Q-348
PREFIX_DATA_REMOVES_TRIVIAL_DOMAIN_ACTION_ASSUMPTION = possible, not installed
PREFIX_FAMILY_MAP1_DESCENT = NOT_BUILT / TYPE-U
RELATIVE_LABEL_TO_EDGE_REALIZATION = NOT_BUILT / TYPE-U
PREFIX_BATCHING_RESTRICTION_SQUARE = NOT_BUILT / TYPE-U
Y5_VERDICT = PASS_WITH_SCOPE_CORRECTION
```

Accordingly, Q-347's broad board line
`FULL_FAMILY_MAP1_EXTENSION=NO-EXTENSION` is valid only with its E3.1
qualifier “depending only on the traced scalar `z=Z_N`.” It must not be used
as a no-go theorem against the Q-348 prefix-family domain.

---

## 8. Y6 — regressions and selection scan

### 8.1 One edge

For one connected edge,

```text
C_G={0},
Q_G={*}.
```

The unique cycle projection is the point even when
`Z_1^CTP=chi_n(R_CTP,1)` is nontrivial. The nontrivial datum remains
endpoint-covariant access under DoR-016; no scalar cycle is manufactured.

```text
ONE_EDGE_REGRESSION = PASS
```

### 8.2 S8-A triple

The direct calculation gives

```text
B_M^T(1,0,-1)=(0,0),
c_3 !=0.
```

For a single terminal-scalar, no-selection lift, `lambda(c_3)=0`; V005's
complete conserved-current family retains `c_3`. The stage therefore remains
the exact witness against a scalar-only full extension.

```text
S8A_REGRESSION = PASS_AGAINST_SINGLE_SCALAR_EXTENSION
```

### 8.3 Reality

Reality sends `Z_N` to `conjugate(Z_N)` and target holonomies to their
conjugates. Integer covectors are closed under the corresponding inverse
operation. No pointwise invariance is asserted.

```text
REALITY_REGRESSION = PASS
```

### 8.4 Identity zero extension

Appending an identity cell multiplies the terminal character by one. It
also appends a repeated final prefix, from which `(Y5-1)` reconstructs an
identity cell. Both the scalar theorem and the prefix escape audit respect
zero extension.

```text
IDENTITY_ZERO_EXTENSION_REGRESSION = PASS
```

### 8.5 Selection scan

```text
realization member selected = false | TYPE-S
edge selected = false | TYPE-S
cycle basis selected = false | TYPE-S
orientation selected = false | TYPE-S
frame selected = false | TYPE-S
filtration selected = false | TYPE-S
lambda selected = false | TYPE-S
rank or rank ratio selected = false | TYPE-S
contraction selected = false | TYPE-S
p evaluated = false | TYPE-S
```

The full `Hom(C_G,Z)` family is retained. The provisional edge association
in Y5 is explicitly a countermodel showing the limit of a no-go proof; it is
not consumed as a selected construction.

```text
Y6_VERDICT = PASS_EXCEPT_NO_CREDIT_FOR_KILLED_E2_4
```

---

## 9. Y7 — fresh attack

### 9.1 Attack: can an unclassified scalar rule evade the no-go?

Take the strongest fixed-stage alternatives not written as `(Y2-1)`:

```text
affine translate q_0 s_lambda(z),
nonlinear phase s(z),
orientation-dependent conjugate rule,
discontinuous abstract homomorphism.
```

The affine translate fails exact batching unless `q_0` is the identity. The
nonlinear rule fails multiplicativity. Conjugation is the negative-covector
member already classified. The discontinuous rule violates the declared
compact/source topology and restriction continuity. No alternative survives
inside the admissible scalar-character class.

```text
FRESH_UNCLASSIFIED_SCALAR_LIFT_FOUND = false
FIXED_STAGE_CLASSIFICATION_SURVIVES_FRESH_ATTACK = true
```

### 9.2 Dependency attack on rank-one uniqueness

At an arbitrary rank-one realization, maps

```text
Hol_(c_G)^(-1) compose Z_N^m,
m in Z,
```

are continuous, batching-compatible, reality-covariant scalar maps. They are
excluded only by the exact Map-1 equation `(Y1-1)`, which forces `m=1`.
Agreement with Q-313 on `Q_square` alone does not force `m=1` on a disconnected
rank-one realization component unless a natural realization arrow connects
that component to the square.

The reviewed construction does state `(Y1-1)`, so this attack does not kill
its conditional uniqueness. It does constrain downstream wording:

```text
RANK1_UNIQUENESS_PROVEN_FROM = exact factorization Hol_(c_G) T=Z_N
RANK1_UNIQUENESS_PROVEN_FROM_Q313_SQUARE_AGREEMENT_ALONE = false | TYPE-R
```

This dependency is separate from the E2.4 type failure.

```text
Y7_VERDICT = PASS_WITH_DEPENDENCY_DISCLOSURE
```

---

## 10. Final determination

The reviewed artifact contains two independent mathematical results and one
failed certificate:

1. The rank-zero terminal projection and the rank-one formula are correct,
   but the claimed rank-one restriction naturality square is ill-typed as
   written. The extension theorem therefore does not pass this review.
2. Every continuous batching-compatible lift from one terminal scalar is
   classified by `Hom(C_G,Z)`. The S8-A automorphism and dimension witnesses
   prove that such a scalar-only lift cannot preserve the complete rank-two
   physical cycle quotient.
3. Q-348 changes the source class. Its every-prefix family reconstructs all
   cellwise relative characters and can carry a nontrivial automorphism
   action, so Q-347's scalar-only no-go does not close that route. The missing
   family-natural cell-to-edge realization and batching/restriction squares
   keep the escape open and uninstantiated.

```text
Y1 = KILL
Y2 = PASS
Y3 = PASS
Y4 = PASS
Y5 = PASS_WITH_SCOPE_CORRECTION
Y6 = PASS_EXCEPT_KILLED_NATURALITY_CERTIFICATE
Y7 = PASS_WITH_DEPENDENCY_DISCLOSURE

EXTENSION_RANK01 = KILLED
RANK2_OBSTRUCTION = CONFIRMED
PREFIX_FAMILY_ESCAPE = OPEN |
  the prefix family defeats the single-scalar information obstruction,
  but no ratified family-natural relative-cell-to-edge descent and no
  compatible batching/restriction square presently instantiate it

TRANSVERSE_ACTION_COMPARISON_SQUARE = NOT_BUILT / TYPE-U
PHYSICAL_P_VERDICT = NO_VERDICT

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No machinery appeal was needed for the structural verdicts. No alpha,
`K_*`, root, response value, rank ratio, or measured constant was evaluated.

