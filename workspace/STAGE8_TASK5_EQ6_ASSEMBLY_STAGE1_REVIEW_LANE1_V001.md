# STAGE 8 TASK 5 / EQ6 — JOINT FINITE ASSEMBLY STAGE 1 REVIEW — LANE 1 V001

```text
ARTIFACT_TYPE = ADVERSARIAL_CROSS_REVIEW_OF_RECORD
REGISTER_HEAD_CHECKED = Q-458
ARTIFACT_UNDER_REVIEW = STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md
ARTIFACT_UNDER_REVIEW_SHA256 = e21cee3081da06417109697352abe570c58dc6dda7d46e78f690d666bed128f5

STAGE1_ASSEMBLY = DEFECTIVE (V1,V2,V3,V4,V5,V6)
STAGE2_REMAINDER = INCOMPLETE (all-arrow J4 + forward J12 + package J15 remain before the joint diamonds)

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Preflight and custody

The target review filename and seal did not exist at preflight. The artifact
under review was SHA-256 verified before reading. The sealed questions-settled
register verified through Q-458. `alpha_supervision/LOCKED_PROCESS.md` was read
in full before the review.

| Authority | Verified SHA-256 | Use |
|---|---|---|
| Stage-1 artifact under review | `e21cee3081da06417109697352abe570c58dc6dda7d46e78f690d666bed128f5` | reviewed object |
| absence-typing verification | `e759e3d77524539e22a5e777940c9d84d96e213d43f443356cf73677f09e0a05` | exact T3 closure conditions |
| J1–J15 constraint system | `96cd90b5bdcc2b77f510ebd21882b215aa5b70c944c9d58b2bdd8855fd52bf11` | J4/J12/J15 definitions |
| DoR-017 square V004 | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | ratified action/Hessian scope and finite bottom |
| Q-243 finite Keldysh reference | `70185aa842bc500724719c65bd66b5f07005e2214b97be0d35e07fd029d5c68c` | first independent shadow check |
| Q-279 finite probe reference | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | second independent shadow check |
| local orthogonal excision certificate | `d61a550a33bf1215c35f4d6f27cd2ec5d644b93a05e16d08fe3d43ded3416817` | cycle-creating response scope |

Custody is clean: this lane did not build the reviewed package. No register,
plan, tracker, git, commit, push, member binding, fixed-point execution, end
test, or numerical evaluation was performed.

## 2. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| V1 functor | **KILL** | the scalar/Hessian pullbacks compose, but the action-family closure is asserted rather than certified, and the response coordinate is an adjoint compression rather than J12's forward `Eta` leg |
| V2 bottom | **KILL** | Q-243 and Q-279 shadows pass independently, but no package-wide `Bot(f)`/`rho^pkg` natural transformation is constructed on the failed action and response coordinates |
| V3 closures | **KILL** | J4 needs compatible family members, J12 needs forward response equality, and J15 needs the resulting one exact package square; none follows from the displayed formulas |
| V4 clash audit | **KILL** | ordinary action/Hessian and finite Ward rows pass, but the C2 and package-bottom `AGREE` rows use weaker equations than the governing constraints |
| V5 J7/remainder | **KILL** | J7 is a genuine J2-dependent face, but the stated Stage-2 remainder omits all-arrow J4 and the still-open J12/J15 package certificates |
| V6 fresh attack | **KILL** | an incompatible admissible action-section pair passes the fiberwise pullback construction and every finite shadow while violating J4 |

## 3. V1 — the claimed functor

### 3.1 What does compute correctly

For `n -f-> m -g-> l`, the proposed scalar pullback satisfies

```text
rho_f^Gamma(rho_g^Gamma(Gamma_l))
 = (Gamma_l o i_g^Y) o i_f^Y
 = Gamma_l o (i_g^Y i_f^Y)
 = rho_(gf)^Gamma(Gamma_l).                         (V1-1)
```

For linear carrier maps, the Hessian compression also composes:

```text
rho_f^Hess(rho_g^Hess(H_l))
 = (i_f^Y)^dagger (i_g^Y)^dagger H_l i_g^Y i_f^Y
 = (i_g^Y i_f^Y)^dagger H_l (i_g^Y i_f^Y)
 = rho_(gf)^Hess(H_l).                             (V1-2)
```

The identity laws follow by setting `i_id^Y=id`. The formulas transport whole
fibers and do not select a representative, frame, basis, orientation,
filtration, or cycle member. These algebraic subclaims pass.

### 3.2 The action-family licensing gap

The reviewed artifact's only closure step is

```text
i_f^Y(S_n) subseteq S_m.                            (V1-3)
```

It then concludes that every target member pulls back into `Adm_fin(n)` with
all R1/R2 conditions. But `(V1-3)` is stated, not derived from a cited sealed
clause for every `Ref_path`, flip, common-refinement, and consumer arrow. The
review standard expressly separated the isometric carrier map from the
missing action/Hessian naturality certificate: an isometry of carriers does
not by itself prove that the retained action family, its active sections, its
vertical cocycle, and its reducing domain are stable under that map.

The DoR-017 cube proves `rho_Gamma,N`/`rho_H,N` on its declared finite-stage
and R5-generated scope. It does not make `(V1-3)` automatic on every new
`I_F` arrow. Thus `(C1-2)` and `(C1-3)` are lawful candidate formulas, but the
claimed all-arrow family endomorphisms are not certified.

### 3.3 The C2 variance error

J12 requires the forward equality

```text
Kernbar_m(j_f^H H) = Eta_f(Kernbar_n(H)).            (V1-4)
```

The reviewed artifact instead proves only the scalar/current pullback

```text
(rho_f^ker K_m)(H,J)
 := K_m(j_f^H H,S_f^J J),

S_f^{J,*} Kernbar_m(j_f^H H) = Kernbar_n(H).         (V1-5)
```

`(V1-5)` is the adjoint compression of `(V1-4)`. It is not equivalent to
`(V1-4)` when the target response carrier has a new-cycle summand. In the
typed model

```text
R_m = S_f^J R_n direct_sum R_new,
Kernbar_m(j_f^H H) = S_f^J Kernbar_n(H) + v_new,
v_new != 0,                                         (V1-6)
```

every old-current test in `(V1-5)` passes while `(V1-4)` fails. Excluding
`v_new` requires the physical OLD_FID/RNL/LR zero-defect certificate on the
same arrow. The cited excision artifact proves the cycle-creating diamonds
only conditional on a nonempty covariant physical zero-defect section; it
does not authorize silently setting `(V1-6)` to zero family-wide.

The artifact neither defines `Eta_f` nor proves the target response lies in
its image. Consequently its C2 coordinate is not the full response leg the
T3 standard required. `PACKAGE_FUNCTOR=BUILT` is refuted at V1.

## 4. V2 — exact finite bottom

### 4.1 Independent shadow check 1: Q-243

The sealed branch Hessian is

```text
M_DD = [[1,-1],[-1,1]].
```

The exact Keldysh rotation gives

```text
T_CTP^T M_DD T_CTP = [[0,0],[0,1]].                 (V2-1)
```

Therefore the finite `(delta,c)` retarded entry is exactly zero, while the
`(delta,delta)` noise entry carries
`i p(1-p) w_N tensor w_N`. Compression or rank-preserving pullback preserves
the zero entry on both routes. The Q-243 shadow claimed in the package is
correct.

### 4.2 Independent shadow check 2: Q-279

The probe-on finite functional is

```text
Z_ref,N[J,R]
 = (1-p)+p exp(L_N(J)-Q_N(R)/2).                    (V2-2)
```

For the reference probe `Q_N(R)=eta`, its exact noise coefficient is

```text
kappa_eta
 = p(1-p) exp(-eta/2)
   / (1-p+p exp(-eta/2))^2.                         (V2-3)
```

Zero extension appends identity holonomies and zero bilocal components, so
`L_M(jJ)=L_N(J)` and `Q_M(jR)=Q_N(R)`. Equations `(V2-2)` and `(V2-3)` are
therefore reproduced exactly, and the `J/J` `(delta,c)` block remains zero.
The Q-279 shadow also passes.

### 4.3 Why the package bottom still fails

Individual exact shadows do not construct the joint natural transformation.
The artifact lists the coordinates of `Bot_n`, then writes

```text
rho_n^pkg : F_fin(n) -> Bot_n
```

without defining `Bot(f)` on the tagged, consumer-dependent coordinates or a
map from an arbitrary retained action member to the independently owned R3
bottom. More importantly, its claimed naturality equation uses the failed
all-arrow action leg and the weaker response compression `(V1-5)`. Thus the
two independent spot checks establish common boundary values, exactly as the
absence review already found, but not one package-wide square.

`FULL_FINITE_BOTTOM=BUILT` and J15 closure are therefore not proved.

## 5. V3 — J4, J12, and J15

### 5.1 J4 remains open

J4 is a condition on compatible representative families:

```text
rho_f^Gamma(I_m)=I_n,
rho_f^Hess(D^2 I_m)=D^2 I_n,                        (V3-1)
```

with every covariance, reality, batching, quotient, unit, and reducing-domain
certificate on the same family. Defining maps between stagewise fibers does
not prove that a compatible section of those fibers exists or that every
retained tuple lies in the equalizer `(V3-1)`. The action-family closure gap
in V1 makes this failure explicit.

### 5.2 J12 remains open

J12 requires `(V1-4)`, composition of `Eta`, and common-refinement agreement
modulo the declared boundary/contact class. The artifact proves only
`(V1-5)`, does not construct `Eta`, and invokes the zero-defect conditions
without a family-wide physical inhabitance proof. Hence J12 is not closed.

### 5.3 J15 remains open

J15 is one exact square containing the action, response, reader, and all
sealed finite shadows. Q-243 and Q-279 pass coordinatewise, but the action and
response faces above are not established and the physical J2 reader remains
absent. A tagged product of the existing shadows is not the required joint
square. J15 remains open.

## 6. V4 — independent clash audit

| Recomputed row | Result |
|---|---|
| ordinary stage action pullback | **PASS ON DOR-017 SCOPE** — it is the declared coordinate restriction |
| R5-generated Hessian pullback | **PASS ON DOR-017 SCOPE** — chain rule gives `D^2(rho Gamma)` exactly |
| `Ref_path` action/Hessian | **OPEN, NOT “NO CLASH” AS CLOSURE** — the candidate pullback composes, but retained-family closure is unproved |
| C2 kernel/response | **KILL** — compression `(V1-5)` is weaker than forward naturality `(V1-4)` |
| C3 finite Ward row | **PASS ON ADMITTED MAPS** — `d` and the actual support/bundle pullback preserve the exact zero |
| package bottom | **KILL** — common values exist, but the joint natural transformation does not |

The C2 countermodel `(V1-6)` is equality on every displayed old-current test,
not an “up to” discrepancy. It demonstrates why the artifact's `AGREE` label
cannot substitute for the missing forward square.

## 7. V5 — J7 and the remainder

J7 is genuinely a face of the joint structure. Its formula

```text
ell_(chi,T)(mu H_mix(x))
 = mu[f(s)chi_K+2f_1(s)<x,T x>_K]
```

becomes a physical equation only after J2 independently identifies the
physical reader with the represented coefficient. Recording J7 beside J2 is
therefore not scope creep.

The remainder list is nevertheless incomplete. The governing dependency
table says that after the transport scaffold and component shadows one still
needs:

```text
1. all-arrow J4 action/Hessian family naturality;
2. physical J2 and its J7 equality;
3. the forward J12 response leg on the common package arrows;
4. the one exact J15 package bottom;
5. only then the simultaneous joint J1-J15 overlap diamonds.              (V5-1)
```

The reviewed artifact omits items 1, 3, and 4 by declaring them closed. Its
Stage-2 remainder is therefore incomplete against both the T3 table and the
actual computations above.

## 8. V6 — fresh incompatible-section attack

This attack is not in the reviewed battery. Fix an arrow `f:n->m` and choose
any target member `Gamma_m`. Let `Psi_n` be a nonzero admissible flat action
direction at stage `n`, with every sealed active jet zero, and set

```text
Gamma_n := Gamma_m o i_f^Y + Psi_n.                 (V6-1)
```

Both coordinates belong to the retained stagewise fibers; they have the same
Q-243/Q-279/DoR-008 active shadows, obey the same units and reality law, and
select no frame, basis, orientation, filtration, or downstream outcome. The
artifact's pullback map exists and returns `Gamma_m o i_f^Y`, but the chosen
tuple satisfies

```text
rho_f^Gamma(Gamma_m) != Gamma_n.                    (V6-2)
```

Thus the stagewise family-valued functor, even if granted, does not inhabit
the J4 equalizer. The only ways to exclude `(V6-1)` are to supply the missing
compatible-section certificate or to select/quotient the flat freedom. The
latter would violate the stated no-selection and finite-authority
disciplines. This fresh attack independently kills the claimed J4 closure.

## 9. Geometry and rails

```text
SURFACE_GEOMETRY:
  the actual old-sector inclusions, test/current maps, support maps, and
  bundle pullbacks license the displayed compressions on their proved scopes;

RAILS:
  composition of those maps and packaging of exact finite shadows are valid
  categorical bookkeeping only after every required coordinate has the
  correct variance and one common arrow domain;

FAILURE_LOCATION:
  the artifact treats two rail constructions as physical certificates:
  (i) a family-presheaf as a J4-compatible action section, and
  (ii) an adjoint response compression as J12's forward response map.
```

No clash is proved among the already sealed finite values. The defect is the
claimed closure of missing physical faces, not a disagreement in Q-243 or
Q-279.

## 10. Final determination

```text
V1_FUNCTOR = KILL
V2_BOTTOM = KILL | Q243_SHADOW=PASS | Q279_SHADOW=PASS
V3_J4_J12_J15 = KILL
V4_CLASH_AUDIT = KILL
V5_REMAINDER = KILL
V6_FRESH_ATTACK = KILL

STAGE1_ASSEMBLY = DEFECTIVE (V1,V2,V3,V4,V5,V6)
STAGE2_REMAINDER = INCOMPLETE (all-arrow J4 + forward J12 + package J15 remain before the joint diamonds)

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
