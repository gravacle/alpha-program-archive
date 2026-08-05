# STAGE 8 TASK 5 / EQ6 - JOINT FINITE ASSEMBLY, STAGE 1 V003

## Lead result

```text
ARTIFACT_TYPE = CONDITIONAL_FINITE_ASSEMBLY_BUILD
LANE = CODEX_LANE_1
REGISTER_HEAD = Q-465
CONDITION_TAG = [EQ6]

J4_FACE = BUILT
J12_FACE = BUILT
J15_FACE = BUILT

J4_FORM = RELATIONAL_INCREMENT_GROUPOID
J12_FORM = STRICT_SIGNED_PUSHOUT_CONTACT_GLUE
J15_FORM = CONTRAVARIANT_BOTTOM_MATE

CONTACT_TWIST_SEEN = none
CLASH_FOUND = none

STAGE2_REMAINDER = physical_J2 + J7 + joint_equalizer_diamonds

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The three finite faces assemble on one structured tuple.  They do not form
three covariant maps of the same kind.  The action coordinate is a relation in
the adopted increment groupoid, the represented/contact response coordinate is
the unique map out of the adopted signed pushout, and the finite bottom is a
contravariant restriction mate.  Treating all three as ordinary forward maps
would reinstate the defects killed in V001 and V002.

No member of the flat action family, response family, orientation family,
frame family, filtration family, or rank family is selected.  The parameter
`nu` and all rank/ratio data remain symbolic.  Nothing in this artifact binds a
member, executes a fixed point, runs an end test, or evaluates a number.

## 1. Preflight and custody

### 1.1 Authorities checked before construction

| Authority | Role | Verification used here |
|---|---|---|
| `alpha_supervision/LOCKED_PROCESS.md` | process, gates, surface-geometry-versus-rails discipline | SHA-256 `1ee1c4188cf1ac1d37f40537a611407c0fd344387bd39421688f8b18478d8469` |
| `QUESTIONS_SETTLED_REGISTER_V001.md` | commission head Q-465; non-consuming drift check through Q-466 | SHA-256 `89864b4cae30a44cd334429a5d9d79dd94689e8298a5a3e406966907251f2d68`; sidecar verified |
| `DOR_020_A3_J4_RELATIONAL_INCREMENT_GROUPOID_2026-08-04.md` | adopted J4 law | SHA-256 `07e0e50145314fe5c30b7f7b5637d4c8add0834c631ad9c2e16209bf3b5a9d6f` |
| `DOR_020_A4_J12_CONTACT_GLUE_STRICT_PUSHOUT_2026-08-04.md` | adopted J12 law | SHA-256 `5fd95472bd6f0507a371779505fe91e2c3c4657ee3afc664ca563a3743d668a4` |
| `STAGE8_TASK5_EQ6_DETERMINATION_MAP_LANE1_V001.md` | mathematical source for the adopted rows and J15 mate | SHA-256 `76ee3c695b1c0c02986a13ff64d6db93f76e39c6861b40273bd31aed1c3a2eb0` |
| `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V002.md` | represented `Eta` geometry carried forward | SHA-256 `e5381e6687dbdd5aed792bdddd1050ea7f39d17e748d6c9e374746c4cee37731` |
| `STAGE8_TASK5_EQ6_STAGE1_V002_REVIEW_LANE1_V001.md` | V002 kill witnesses and scope audit | SHA-256 prefix `312dbe14` |
| DoR-020 and A1 | adopted continuum package and WHERE clauses | ratified premises, condition-tagged `[EQ6]` |

The commission's questions-settled head was Q-465.  Before sealing, the live
register also contained Q-466 from the parallel physical-J2 lane.  That later
row was checked only for drift: it confirms physical J2 remains absent and
does not change any J4/J12/J15 premise or construction below.  This artifact
therefore consumes through Q-465 and records Q-466 as non-consuming parallel
drift.  In particular, this
build consumes Q-313/Q-347 for the old-image descent discipline, Q-411/Q-421 for
the joint-fiber constraints, Q-459/Q-462 for the failed finite assemblies,
Q-463 for the determination map, and Q-464/Q-465 for the two adopted rows and
the present commission.

### 1.2 Output and custody checks

The requested output name and sidecar did not exist before construction.  This
is a Lane-1 build.  It does not review itself and performs no register, plan,
tracker, git, commit, or push action.

### 1.3 Standing notation

For an admitted finite arrow `f : N -> M`, write

```text
rho_f       : completed/finite fields at M -> fields at N
j_prof,f    : represented profiles at N -> represented profiles at M
r_f^Bot     : Bot_M^resp -> Bot_N^resp
R_N^rep     := im(Kernbar_N)
I_N^contact := adopted contact-incidence carrier
C_N         := R_N^rep intersect I_N^contact
```

The action representative at stage `N` is `I_N`.  Its admitted vertical
increment along `f` is `v_f`.  The represented response map carried from V002
is

```text
Eta_f^rep(Kernbar_N H) = Kernbar_M(j_prof,f H).
```

V002 proved this formula well-defined and compositional on represented
profiles.  That result is consumed unchanged; the present build extends its
codomain by the adopted contact pushout.

## 2. The one structured finite package

The finite package is valued in the mixed-variance category

```text
FinPkg_020 := ActRel x RespPush x BotStruct x Aux,
```

where:

1. `ActRel` has action objects and adopted relation spans as arrows;
2. `RespPush` has signed-pushout response carriers and linear covariant maps;
3. `BotStruct` is the independently sealed, multi-sorted finite-bottom
   category; each coordinate keeps its sealed variance, and its physical
   response coordinate uses the contravariant old-image restriction;
4. `Aux` contains the already ratified covariance, reality, units, Ward,
   support, subextensivity, restriction, and bundle data.

For each finite stage `N`, define

```text
F_003(N) = (Act_N, P_N, Bot_N, Aux_N),
```

and for each admitted `f : N -> M`, define

```text
F_003(f) = (Rel_f, Eta_f, BotStruct(f; r_f^Bot), Aux_f).
```

The next three sections construct these three nontrivial coordinates and prove
their composition laws.  The phrase "one functor" below always means this
typed mixed-variance functor.  It never means an invented upward bottom map.

The bottom object carried here is the V002 tagged tuple

```text
Bot_N = (Gate1-4_N, Q243_N, Q279_N, Q309_N, Q408_N,
         ActionBottom_N, WardBottom_N, ReaderBottom_N,
         WhereBottom_N, C1FaithBottom_N).                      (PKG-1)
```

The response entry of `(PKG-1)` is written `Bot_N^resp`; it is the entry used
by the J15 mate.  The other entries are not forced into that variance.

## 3. E1 - J4 relation-span functor

### 3.1 Adopted relation

For `f : N -> M`, let `Rel_f` consist of triples

```text
(I_N, I_M, v_f)
```

satisfying

```text
I_M = I_N o rho_f + v_f.                                      (J4-1)
```

The increment is flat in the adopted sense on the active finite section.  It
is retained as record-visible family data rather than set to zero.

For composable arrows `f : N -> M` and `g : M -> L`, define

```text
v_gf = v_f o rho_g + v_g.                                     (J4-2)
```

Then

```text
I_L
 = I_M o rho_g + v_g
 = (I_N o rho_f + v_f) o rho_g + v_g
 = I_N o (rho_f o rho_g) + v_f o rho_g + v_g
 = I_N o rho_gf + v_gf.
```

Thus relational composition closes.  Associativity follows directly:

```text
v_h(gf)
 = v_gf o rho_h + v_h
 = v_f o rho_g o rho_h + v_g o rho_h + v_h
 = v_f o rho_hg + v_hg
 = v_(hg)f.
```

For the identity arrow,

```text
rho_id = id,    v_id = 0,
```

so `(I_N,I_N,0)` is the identity relation.  This proves the relation-span
functor laws on every admitted arrow.

### 3.2 Hessian and stationary data

Differentiating only after retaining the increment gives

```text
D I_M = rho_f^*(D I_N) + D v_f,
D^2 I_M = rho_f^*(D^2 I_N) + D^2 v_f.                        (J4-3)
```

Here `rho_f^*` is the full pullback of a covector or bilinear form on the typed
tangent domains.  No Hessian is silently identified across unequal domains.

Consequently:

* the action coordinate is explicitly member-sensitive;
* stationary loci and Hessians are family-valued unless a later licensed
  consumer proves groupoid invariance;
* the finite active jets remain the sealed zero jets because every admitted
  `v_f` is flat there;
* completed off-section jets are not deleted and are not evaluated here.

### 3.3 Flat groupoid action

For an admitted flat increment `psi_N`, define

```text
I_N' = I_N + psi_N,
v_f' = v_f - psi_N o rho_f.                                  (J4-4)
```

Then

```text
I_N' o rho_f + v_f'
 = I_N o rho_f + psi_N o rho_f + v_f - psi_N o rho_f
 = I_M.
```

Hence the target relation is unchanged.  For a compatible family
`{psi_N}`, the same calculation on two composable arrows preserves (J4-2), so
the action is a genuine groupoid action and not a stagewise equivalence only.

No orbit quotient is taken.  The groupoid records the relation among all
members; it does not identify them as gauge.  This distinction is necessary
because the representative-family theorem permits a flat member change to
alter completed response content.

This calculation absorbs the former V6 witness.  A replacement
`I_N -> I_N + psi_N` no longer falsifies naturality; it changes the source
representative and the increment coordinate together inside one groupoid
orbit.  Excluding that witness would be an illicit selection.  Retaining it is
the adopted law.

### 3.4 Consumer certificate

Every stage-1 consumer is assigned one of the two statuses required by A3.
"Equivariant family" means the maps commute with the groupoid action while
the resulting member values remain distinct; it does not mean orbit
identification.

| Consumer | J4 status | Reason |
|---|---|---|
| Gate-1 through Gate-4 finite shadows | groupoid-invariant | flat increments have zero finite active jet |
| Q-243/Q-279/Q-309 finite blocks | groupoid-invariant | exact finite restrictions are unchanged |
| `Kern_Q408^fin` and represented `Eta^rep` | equivariant family | the carrier/map law is structural, but its member-generated response arguments are not quotient-identified |
| contact pushout response | equivariant family | the strict overlap law is fixed while member-dependent physical response data remain tagged |
| `C1_core^fin` and `Faith_fin` | equivariant family | norms/separation transport all admitted members and select none |
| `C3_fin`, Ward, support, and subextensivity | equivariant family | the laws hold memberwise on the glued carrier |
| `R2_alg^fin` and reader bottoms | groupoid-invariant only on sealed algebraic finite shadows; otherwise family-valued | no physical reader is selected here |
| `Where_A1^fin` and bundle/path data | equivariant family | bundle covariance transports the complete family |
| package-bottom map | mixed: invariant on sealed finite active jets, family-valued on action/Hessian inputs | the response entry is compared by the J15 mate |
| action value and off-section action germ | member-sensitive | changes by the retained flat family |
| stationary locus and generated Hessian away from the finite active section | member-sensitive/family-valued | (J4-3) retains `D v_f` and `D^2 v_f` |
| later fixed-point and number consumers | not executed | their member-sensitivity must remain explicitly tagged |

No consumer is represented by an untagged action member.

### 3.5 J4 regressions

1. **Old vertical-increment witness:** absorbed by (J4-4), not excluded.
2. **V6 incompatible section:** accepted exactly when its mismatch is an
   admitted flat increment; otherwise rejected by the adopted flatness and
   cocycle conditions.
3. **Rank-preserving identity arrow:** `v_f=0` recovers the old on-the-nose
   formula on that subcategory.
4. **Cycle-creating arrow:** a nonzero admitted `v_f` is retained and tagged;
   no target action is forced from the source action alone.
5. **Selection attack:** replacing the relation by a chosen section is
   forbidden and would void the build.

Therefore

```text
J4_FACE = BUILT.
```

## 4. E2 - J12 strict-pushout response

### 4.1 Adopted overlap and signed pushout

At each stage let

```text
C_N = R_N^rep intersect I_N^contact.
```

The adopted A4 datum is the strict overlap equality, for every admitted arrow
`f : N -> M`,

```text
eta_f^boundary |_C_N = Eta_f^rep |_C_N.                       (J12-1)
```

Define the signed pushout carrier in the additive response category by

```text
R_N^phys = P_N
 := (R_N^rep direct_sum I_N^contact) / Delta_N,

Delta_N
 := { (c,-c) : c in C_N }.                                   (J12-2)
```

Write classes as `[r,b]_N`.  Equality (J12-1) is an authored gluing datum
adopted by DoR-020-A4.  It is not relabeled as a pre-existing theorem.
At a finite stage `Delta_N` is finite-dimensional and closed, so the algebraic
and completed finite pushouts agree.

### 4.2 Extension of the represented map

For `f : N -> M`, use the V002 represented map and the adopted boundary map:

```text
Eta_f([r,b]_N)
 := [Eta_f^rep(r), eta_f^boundary(b)]_M.                       (J12-3)
```

This is well-defined.  A relation generator `(c,-c)` maps to

```text
(Eta_f^rep(c), -eta_f^boundary(c)),
```

By overlap equality and restriction compatibility, the two displayed entries
are one common element

```text
c_f := Eta_f^rep(c) = eta_f^boundary(c) in C_M.
```

The image is therefore `(c_f,-c_f) in Delta_M`, hence zero in `P_M`.
Thus (J12-3) depends only on the pushout class.

It is unique: if a response map out of `P_N` agrees with `Eta_f^rep` and
`eta_f^boundary` on the two canonical injections, the universal property of
the quotient (J12-2) forces it to equal (J12-3).  No additional response member
is selected.

Identity and composition are inherited componentwise:

```text
Eta_id([r,b]) = [r,b],

Eta_g Eta_f([r,b])
 = [Eta_g^rep Eta_f^rep(r),
    eta_g^boundary eta_f^boundary(b)]
 = Eta_gf([r,b]).                                             (J12-4)
```

This completes, rather than replaces, V002's genuine represented geometry.

### 4.3 J13 laws on the glued carrier

Each J13 law is checked on the two summands and then descends because its two
restrictions agree on `C_N`.

| Law | Pushout verification |
|---|---|
| cocycle/composition | equation (J12-4) on both injections |
| restriction | represented and boundary restrictions preserve `Delta_N`, so they induce the quotient map |
| reality | conjugation sends `(c,-c)` to `(conj(c),-conj(c))`; the quotient is stable |
| units | both legs use the declared R4-only unit seam; no implicit cross-sector conversion occurs |
| Ward/contact | the Ward functional agrees on `C_N`, so its difference vanishes on `Delta_N` |
| support | support is the union of the represented and contact supports modulo their actual overlap |
| OLD_FID | old physical bulk classes remain represented; no `D_G^*`-visible class is killed |
| RNL | the quotient identifies only the actual common contact class, so no leakage relation is added |
| LR | locality is checked separately on the two legs and on their common overlap |
| subextensivity | the glued bound is inherited from the component bounds because the common contribution is counted once |

More explicitly, with `q_N` the quotient map and with all expressions on their
declared scopes, the induced data satisfy

```text
Eta_g Eta_f q_N = Eta_gf q_N,
beta_gf          = beta_g + Eta_g(beta_f),
Res_f Eta_f       = id on each licensed old-image scope,
Theta_M Eta_f    = Eta_f Theta_N,
Ward_M Eta_f     = Ward_N,
supp(Eta_f x)    subset f(supp x) union supp(beta_f).          (J13-1)
```

The first equality was proved in (J12-4).  For each remaining equality, both
sides agree after precomposition with the represented injection and with the
contact injection.  They also agree on `C_N` by (J12-1).  The pushout universal
property therefore makes the equality hold on all of `P_N`.

Here `Res_f` denotes only the independently sealed response restriction on
the scope where it exists.  It is not inferred from an adjoint compression
and is not an upward map.  Outside that licensed old-image scope, no inverse
claim is made.

For subextensivity, equip the finite pushout with its quotient norm.  If the
component bounds are `a_N` and `b_N`, then

```text
||beta_N([r,b])|| <= a_N ||r|| + b_N ||b||,
```

and taking the infimum over all representatives of `[r,b]` gives the induced
quotient bound.  The sealed `a_N/Vol_N -> 0` and `b_N/Vol_N -> 0` estimates
therefore imply the glued subextensive estimate.  The R4 unit maps commute on
both injections and on `C_N`, so this argument supplies no undeclared unit
conversion.

### 4.4 No-deletion theorem

Suppose `[r,0]_N = 0` in `P_N`.  By (J12-2), there is `c in C_N` with
`(r,0)=(c,-c)`, so `c=0` and `r=0`.  Thus the represented injection is
injective.  Similarly the contact injection is injective.  The pushout deletes
only the duplicate presentation of the common class, not either physical leg.

In particular, a `D_G^*`-visible bulk cycle cannot be deleted by contact gluing.
Deleting one would trigger A4 void condition 2.

### 4.5 Contact-twist detector and five permanent void regressions

Define the overlap defect for an admitted arrow

```text
Tw_f := eta_f^boundary |_C_N - Eta_f^rep |_C_N.               (J12-5)
```

The adopted member has `Tw_f=0`.  The present corpus sweep found no actual
contact datum exhibiting `Tw_f != 0`.  The sweep included the determination
map, both adoption decisions, the pass-2 contact/excision builds, and both
prior stage-1 assemblies/reviews; the only nontrivial twist present is the
declined countermodel, not an exhibited actual contact datum.  This is reported
as

```text
CONTACT_TWIST_SEEN = none,
```

not as a theorem that future physical contact data cannot produce one.

All five A4 void conditions are installed as permanent regressions:

| Void | Failure-capable test | Present result |
|---|---|---|
| 1 | compare the represented and boundary images on every actual overlap class | equal by the adopted datum |
| 2 | test injectivity on `D_G^*`-visible represented bulk classes | injective by Section 4.4 |
| 3 | rerun beta, restriction, reality, units, Ward, OLD_FID, RNL, LR, and subextensivity | pass on the pushout |
| 4 | inspect the provenance of every overlap automorphism | none selected; the strict equality is the adopted datum |
| 5 | evaluate (J12-5) on every newly supplied actual contact class | no nonzero witness in present stock; any future witness voids A4 immediately |

Therefore

```text
J12_FACE = BUILT.
```

## 5. E3 - J15 contravariant bottom mate

### 5.1 Correct variance

For every stage, let

```text
pi_N^resp : P_N -> Bot_N^resp
```

be the response entry of the finite bottom projection/restriction, and for
`f : N -> M` retain the
sealed contravariant map

```text
r_f^Bot : Bot_M^resp -> Bot_N^resp.
```

The J15 face is the mate square

```text
r_f^Bot o pi_M^resp o Eta_f = pi_N^resp.                     (J15-1)
```

There is no response-bottom lift `Bot_N^resp -> Bot_M^resp` in this
construction.  Other bottom coordinates keep whatever variance their own
sealed definitions already assign.

### 5.2 Proof on represented and contact generators

For a represented class `r=Kernbar_N H`, V002's well-defined geometry gives

```text
r_f^Bot pi_M^resp Eta_f([r,0])
 = r_f^Bot pi_M^resp[Eta_f^rep(r),0]
 = pi_N^resp[r,0],
```

by exact old-image restriction.

For a contact class `b`, the adopted A4 restriction law gives

```text
r_f^Bot pi_M^resp Eta_f([0,b])
 = r_f^Bot pi_M^resp[0,eta_f^boundary(b)]
 = pi_N^resp[0,b].
```

The two formulas agree on `C_N` by (J12-1), so they factor through the signed
pushout.  Linearity then proves (J15-1) for every `[r,b]_N`.

For composable `f,g`,

```text
r_f^Bot r_g^Bot pi_L^resp Eta_g Eta_f
 = r_f^Bot pi_M^resp Eta_f
 = pi_N^resp,
```

which is the mate composition law.  The identity case is immediate.  This
proves J15 through the same structured functor as J4 and J12.

### 5.3 FC4 and new cycles

Equation (J15-1) compares only an existing target bottom shadow with its source
restriction.  It does not create a target bottom class from a source bottom
class.  On a cycle-creating refinement:

* the new target cycle remains present in `P_M`;
* `r_f^Bot` annihilates the target-only new-cycle coordinate when returning to
  the old image in `Bot_N^resp`;
* no upward extension is inferred;
* no source value is assigned to the new cycle.

This is FC4's contravariant-honesty clause exactly.  It is also compatible with
the descent/visibility theorem: visible target content survives at the target,
while old-image restriction remains exact.

### 5.4 Sealed finite consumers

The response mate is one coordinate of the multi-sorted bottom transformation.
Every sealed consumer has a typed leg:

| Bottom coordinate | Governing comparison |
|---|---|
| Gate 1-4 | independently sealed restriction/zero-extension equations |
| Q-243 and Q-279 | exact finite scalar and bilocal shadows |
| Q-309 | exact old kernel/mixing-zero restriction |
| Q-408 | `r_f^Bot` on the represented/contact response old image |
| action/Hessian | J4 relation, with invariant finite active jets and retained off-section member sensitivity |
| Ward/C3 | induced pushout Ward map and sealed restriction |
| reader | sealed algebraic reader only; physical J2 remains stage 2 |
| WHERE/bundle | adopted A1 restriction and bundle transport |
| C1/Faith | independently sealed finite norm, bound, and separation legs |

The response equality is on the nose:

```text
restricted target shadow = sealed source shadow.
```

There is no approximation, convergence claim, or replacement of a completed
object by a finite one.  Action/Hessian data are carried relationally by J4;
response/contact data are carried covariantly by J12; their finite observations
are compared only by (J15-1).

Therefore

```text
J15_FACE = BUILT.
```

## 6. E4 - Package coherence on one tuple

### 6.1 Functor laws

For an admitted arrow `f`, the single tuple is

```text
F_003(f)
 = (Rel_f,
    Eta_f^rep pushout eta_f^boundary,
    BotStruct(f; r_f^Bot),
    covariance/reality/unit/Ward/support data).
```

The identity law holds coordinatewise:

```text
(v_id, Eta_id, r_id^Bot) = (0, id, id).
```

For composable `f,g`, the composition law is

```text
v_gf       = v_f o rho_g + v_g,
Eta_gf     = Eta_g o Eta_f,
r_gf^Bot   = r_f^Bot o r_g^Bot.
```

The apparent reversal in the last line is exactly the response entry's
contravariant coordinate inside `BotStruct`.
Associativity was proved in Sections 3, 4, and 5.  The three coordinates share
the same stage objects and the same admitted arrows, so this is one structured
package rather than three unrelated constructions.

### 6.2 Joint compatibility

There is no clash among the three coordinates:

1. The flat action groupoid changes no sealed finite active jet, so it does not
   alter the pushout overlap or bottom shadows.
2. The pushout preserves both represented and contact injections, so it does
   not delete a groupoid-visible or bottom-visible class.
3. The bottom mate is evaluated after `Eta_f`; it respects the pushout relation
   and never assigns an upward action or response value.
4. Reality acts simultaneously by conjugation on action relations, pushout
   classes, and bottoms.
5. The R4-only unit seam is used once in each mixed-sector expression; no unit
   conversion is supplied implicitly by composition.

Thus

```text
CLASH_FOUND = none.
```

This statement is bounded to the built stage-1 faces.  It does not assert that
the still-open stage-2 diamonds commute.

### 6.3 Membership-guard board

| FC row | Stage-1 V003 status | Supply |
|---|---|---|
| FC1 actual physical objects | carried/conditioned | adopted finite objects and actual pushout carriers |
| FC2 one package-wide finite bottom | SUPPLIED | tagged tuple `(PKG-1)`, with the J15 response mate and each other sealed variance retained |
| FC3 one functor | SUPPLIED | `F_003 : I_F -> FinPkg_020` |
| FC4 contravariant honesty | SUPPLIED | no upward bottom map; Section 5.3 |
| FC5 covariance on full admitted families | SUPPLIED for stage-1 faces | groupoid, pushout, and mate covariance |
| FC6 OLD_FID/RNL/LR/local excision | SUPPLIED on adopted scopes | pushout law and permanent regressions |
| FC7 bundle | carried | DoR-020-A1 WHERE clauses |
| FC8 analytic core | carried | existing finite analytic package |
| FC9 finite-kernel honesty | carried and protected | represented injection is not deleted |
| FC10 joint compatibility | PARTIAL | J4/J12/J15 supplied; physical J2 and J7 remain |
| FC11 equalizer diamonds | OPEN | stage 2 |
| FC12 | struck | unchanged |
| FC13 target blindness | SUPPLIED | Section 8 |

### 6.4 Exact stage-2 remainder

Only the following finite-assembly work remains after this build:

```text
1. physical J2,
2. J7 as the surfaced joint face,
3. the joint equalizer diamonds on the actual live tower.
```

Neither the old J4 functionality claim nor a new J15 covariant lift is in the
remainder.  J4 has been replaced by the adopted relation groupoid; J15 is
closed by the contravariant mate.

## 7. DoR-008 finite-bottom checks

The finite-bottom condition is equality, not approximation.  Two independent
shadow checks are written explicitly.

### 7.1 Rank-preserving represented shadow

For `r=Kernbar_N H` and a cycle-rank-preserving identity extension,

```text
v_f = 0,
Eta_f([r,0]) = [Kernbar_M(j_prof,f H),0],
r_f^Bot pi_M^resp Eta_f([r,0]) = pi_N^resp[r,0].
```

This reproduces V002's represented shadow and the Q-243/Q-279 restrictions
exactly.

### 7.2 Cycle-creating contact shadow

For `[r,b]_N` under a cycle-creating arrow,

```text
r_f^Bot pi_M^resp[Eta_f^rep(r),eta_f^boundary(b)]
 = pi_N^resp[r,b].
```

The target may contain an additional cycle coordinate, but the old bottom sees
only its exact source restriction.  The new target coordinate is neither
deleted nor assigned an invented source value.  This reproduces the Q-309
zero/old-image discipline.

### 7.3 Finite active action shadow

Because every admitted action increment is flat on the active finite section,

```text
j^k(v_f)|active = 0 for every finite k,
```

and the sealed finite action, Hessian, retarded, and kernel shadows are
unchanged.  This is a conservativity statement only.  It does not set the
completed off-section action to zero.

## 8. E5 - Battery, geometry, and anti-tuning

### 8.1 Nine geometric regressions

| Regression | Required behavior | Result |
|---|---|---|
| 1. pure new-cycle profile | retained at target, zero old restriction | PASS by J15 variance |
| 2. covariance orbit | whole orbit retained, no representative chosen | PASS by J4 groupoid and J12 covariance |
| 3. all-stage skeleton | identity/composition on every admitted arrow | PASS coordinatewise |
| 4. rank-preserving `Ref_path` | old represented formula recovered | PASS with `v_f=0` |
| 5. no upward response quotient | no `Bot_N^resp -> Bot_M^resp` invented | PASS |
| 6. arbitrary represented profile | `Eta_f^rep` remains well-defined | PASS, carried from V002 |
| 7. sector mixer | rejected when it violates RNL/overlap preservation | PASS; it cannot descend through `Delta_N` |
| 8. `P=id` witness | admitted when it satisfies the actual relative no-leakage condition | PASS; no clause excludes it by form |
| 9. bundle/topology | WHERE bundle typing and restriction retained | PASS on adopted A1 scope |

The geometry checks behind the table are:

```text
new-cycle x_new:     r_f^Bot pi_M^resp(x_new)=0,
                     x_new != 0 in P_M;

rank-preserving f:   v_f=0,
                     Eta_f^rep Kernbar_N(H)=Kernbar_M(j_prof,f H),
                     Res_f Eta_f=id on the licensed old image;

arbitrary H:         Eta_f^rep is defined by the displayed Kernbar equation,
                     never by the adjoint compression;

Q-430 mixer zeta:    if zeta fails to preserve Delta_N it does not descend;
                     if adjusted to preserve the overlap, its old-to-new
                     support still violates RNL/local range;

Q-432 P=id:          on its rank-preserving admitted scope, Rel_f has v_f=0,
                     Eta_f=id, and r_f^Bot=id; no unrelated orthogonality
                     condition is added;

Q-435 bundle attack: the existing smooth U(1) lift, pullback-bundle
                     isomorphism, full-rank condition, unit class, and c_1
                     restriction must all commute before the tuple enters
                     Aux_f.
```

Thus a target-only cycle is retained even though its old bottom is zero; the
sector mixer is rejected by surface support rather than by categorical
bookkeeping; and `P=id` remains admitted as required.

### 8.2 Added permanent regressions

The following are also permanent:

1. old vertical-increment/V6 witness is absorbed as a groupoid orbit;
2. untagged action-member consumption is a failure;
3. all five A4 void tests in Section 4.5;
4. a covariant new-cycle bottom lift is forbidden;
5. a target cycle killed by the pushout is a failure;
6. a nonzero actual overlap defect `Tw_f` voids A4 immediately;
7. separate face nonemptiness cannot substitute for the stage-2 joint diamonds.

### 8.3 Surface geometry versus rails

```text
SURFACE GEOMETRY:
  action representatives plus real flat increments;
  represented and actual contact response carriers;
  their actual overlap C_N;
  signed pushout classes;
  target new-cycle content;
  exact finite bottom restrictions.

RAILS:
  the relation-span bookkeeping;
  the pushout universal-property presentation;
  the mixed-variance product category;
  sidecar/hash/custody procedures;
  member-sensitivity and condition tags.
```

No rail is used as evidence that a physical carrier is inhabited.  Conversely,
the geometry is not forced into a covariant square merely to simplify the
rails.

### 8.4 Anti-tuning ledger

Construction order was fixed entirely by adopted carrier structure:

```text
A3 relation law
 -> relation composition and flat groupoid action
A4 overlap equality
 -> signed pushout and unique Eta
sealed bottom restrictions
 -> contravariant mate
 -> mixed-variance package
 -> finite and geometric regressions.
```

No response value, contraction threshold, fixed point, end-test result,
measured constant, or desired verdict appears in a definition.  `nu`, `p`,
ranks, and ratios remain symbolic.  The order therefore supplies no route for
target-output tuning.

## 9. Delta against stage-1 V002

| V002 component | V003 treatment |
|---|---|
| represented `Eta_f^rep` formula and its profile-level well-definedness | carried unchanged |
| compression formula outside its left-inverse scope | still forbidden |
| action as an on-the-nose functional section | replaced by the adopted A3 relation-span groupoid |
| unresolved contact overlap equality | supplied by adopted A4 and used to build the signed pushout |
| represented-only response carrier | extended to `P_N` by the unique pushout map |
| attempted/implicit covariant bottom comparison | removed; replaced by the D3-4 contravariant mate |
| V6 and vertical-increment mismatch as kills | reclassified as absorbed groupoid regressions exactly when flat/admitted |
| J4/J12/J15 closure claims | now proved on the corrected typed objects |
| physical J2, J7, and joint diamonds | remain open for stage 2 |

No other V002 claim is upgraded.  In particular, this build does not claim an
unscoped compression, a selected action section, a contact-twist theorem, or an
upward cycle lift.

## 10. Honest stopping point

The adopted A3 and A4 rows are sufficient to build the three requested stage-1
faces.  They do not supply physical J2, J7, or the actual joint equalizer
diamonds.  Those remain the complete stage-2 frontier.  A future actual contact
class with `Tw_f != 0` would void A4 and therefore this J12/J15 branch; no such
witness is present in the current sealed stock.

No obstruction or clash was found inside the corrected stage-1 types.

```text
J4_FACE = BUILT
J12_FACE = BUILT
J15_FACE = BUILT
CONTACT_TWIST_SEEN = none
CLASH_FOUND = none

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
