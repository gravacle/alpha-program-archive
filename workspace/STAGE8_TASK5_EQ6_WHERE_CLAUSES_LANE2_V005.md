# STAGE 8 TASK 5 / EQ6 — WHERE-CLAUSES — LANE 2 V005

Date: 2026-08-04  
Lane: Codex Lane 2  
Task: 5 / EQ6 / `B_Q408_REFINEMENT`  
Custody: clause-layer repair after Q-435; hostile check required

## Lead result

```text
CLAUSES = LAW_ONLY_BUNDLE_TYPED

PATH_CURRENT_WHERE_LAW =
  DRAFTED_AS_POSSIBLY_EMPTY_ADMISSIBLE_FAMILY;
  NO_INHABITANCE_ASSERTED

LOCAL_FIELD_WHERE_LAW =
  DRAFTED_AS_POSSIBLY_EMPTY_ADMISSIBLE_FAMILY;
  U1_BUNDLE_LIFT_OR_PULLBACK_BUNDLE_ISOMORPHISM_REQUIRED;
  SMOOTH_FULL_RANK_REQUIRED;
  CHARACTERISTIC_CLASS_COMPATIBILITY_REQUIRED;
  NO_INHABITANCE_ASSERTED

CANONICAL_TEST_TRANSPORT = CARRIED / PASS
RELATIVE_NO_LEAKAGE = CARRIED / PASS
BUNDLE_TYPED_FIELD_TRANSPORT = CONDITIONALLY_DERIVED

AMENDMENT_TEXT = DRAFTED |
  DOR020_AMENDMENT_POPULATING_EXISTING_P4_X4_FIELDS

FULL_Ext_cycle_MEMBER = OPEN / TYPE-U
JOINT_EQ6 = OPEN
MEMBER_BOUND = false
READY_FOR_CHECK = yes
```

V005 is a clause artifact, not an inhabitant.  It defines two admissibility
laws.  Each law may have no members.  DoR-020's certified joint `[EQ6]`
witness remains the only object authorized to prove joint inhabitance.

The field law is now typed at the carrier level.  A base refinement does not
by itself pull a target connection onto the source U(1) bundle.  The law
therefore requires a smooth equivariant bundle lift, equivalently a bundle
isomorphism from the source bundle to the pullback target bundle, and it
requires the corresponding first-Chern-class equation.  Only after that
datum is supplied does connection and curvature transport follow by
functorial pullback.

---

## 0. Preflight, authorities, and register sweep

### 0.1 Three-line preflight

```text
DOES THE OBJECT EXIST?  The law-only bundle-typed clauses and amendment
                        text are drafted below; no member is exhibited.
IS THE VERSION CURRENT? YES, through register head Q-435.
ARE ITS INPUTS PRESENT? YES: the sealed Q-435 check, V004, DoR-020, P4/X4,
                        V005 surface/bundle data, Q-408, and DoR-019.
PREFLIGHT = PASS
```

The Q-435 check was hash- and seal-verified before reading:

```text
STAGE8_TASK5_EQ6_V004_HOSTILE_CHECK_LANE1_V001.md
SHA-256 = f586e67ac4e97feec8003d06659fa82d83773ce6ef530ee9c3628a9d54a4c57a
SEAL = PASS
```

Verified authorities:

| Authority | SHA-256 | Use |
|---|---|---|
| locked process with Q-427 rule | `d537e294c03b3fc50fa49844f5b166bdcee1d64fe1513b9201047f602cd1518f` | custody and geometry/rails split |
| register at Q-435 | `6df0d424812f503bc7576368df4780c9b91f3f0447e60a21543ee45159dbfb3f` | current scope |
| V004 hostile check | `f586e67ac4e97feec8003d06659fa82d83773ce6ef530ee9c3628a9d54a4c57a` | governing law-only and bundle repair |
| V004 | `c5254f663a1e3a6d1079027184c6dea96a35ab7255a856aa39e584b3d7c32dc2` | two passing constructions and clause source |
| continuum package V005 | `09883a0d7a5d1329033a09c59ff8d7c843a0098cba569d2a2b97f64f45b2dd95` | exact P4/X4 fields and partial rule |
| DoR-020 | `bead32b7a12dd70b48a5ddd729395f23914dce06047783226a33d3ccb1eafa31` | amendment scope and EQ6 condition |
| field signature V005 / DoR-015 object | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | U(1)-bundle surface family, paths, currents, fields |
| Q-408 current/kernel realization | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | actual analysis, current, kernel, support maps |
| carrier metric V005 / DoR-019 object | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | fixed Riesz maps and units |
| derived `Ref_path` square | `fa73114214d7653d9a5d181a684b3bd65f0d6e9f91fd2256fb159ca97e56c4bf` | finite/rank-preserving boundary |

### 0.2 Register sweep

```text
Q-297  physical scalar currents are the complete ker(B^T) family;
Q-408  finite physical current/kernel and support maps exist;
Q-418  Ref_path has actual path subdivision and P=id;
Q-422  DoR-020 adopts the six-generator package conditional on [EQ6];
Q-425  Ref_0 is the maximal built physical refinement category;
Q-427  actual surface geometry must be separated from rails;
Q-430  old-to-new Riesz leakage refutes algebra-only physicality;
Q-432  relative no-leakage replaces global orthogonality;
Q-434  V004's two constructions land; two where-laws remain;
Q-435  constructions pass; clause nonemptiness and bundle typing fail.
```

No settled entry supplies a certified joint witness, a bundle lift on a
cycle-creating primitive, or permission to bind a lift, field, path, or
refinement member.

### 0.3 Existing P4/X4 fields populated by this amendment

Package V005 defines

```text
x_R=(Gamma_R,P_R,S_R,Cof_R,Dens_R,
     eta_conn,R,eta_curv,R) in X4(R).            (0-1)
```

The repaired where-laws populate the existing slots as follows:

| P4/X4 field | Source in the repaired amendment |
|---|---|
| `Gamma_R` | path/current where-law: actual refined edge paths modulo admitted Q-408 line-integral equality |
| `S_R` | induced injective conserved-current map from the same actual path relation |
| `P_R` | V004 canonical construction `Phi_G'^{-1}S_RPhi_G`, admitted only after relative certificates |
| `Cof_R` | bundle-field where-law's smooth full-rank coframe relation |
| `Dens_R` | positive density relation dual to `Cof_R` with unit compatibility |
| `eta_conn,R` | derived pullback through the declared U(1) bundle lift/isomorphism |
| `eta_curv,R` | derived curvature pullback through the same lift/isomorphism |

The lift/isomorphism and characteristic-class rows are certificate data
attached to the existing X4 relation; they are not additional physical
field slots.  No new P-field, X-field, generator, or root is introduced.

---

## 1. B1 — law-only path/current and field clauses

### 1.1 Governance semantics

For every primitive rail arrow `r:G->G'`, the amendment defines admissible
sets

```text
PathRel_adm(r),
FieldExt_adm(R) for R in PathRel_adm(r).         (B1-1)
```

Either set may be empty.  The following implications are forbidden:

```text
law adopted => PathRel_adm(r) inhabited,
law adopted => FieldExt_adm(R) inhabited,
each marginal inhabited => joint EQ6 inhabited. (B1-2)
```

The laws specify membership only.  A certified witness must exhibit one
joint term satisfying all six generator conditions and J1--J15 before any
member can be bound or any post-witness computation can run.

```text
CLAUSE_ASSERTS_INHABITANCE = false
CLAUSE_ASSERTS_MARGINAL_NONEMPTINESS = false
CLAUSE_ASSERTS_JOINT_NONEMPTINESS = false
EQ6_WITNESS_BURDEN_UNCHANGED = true
```

### 1.2 Law W1 — admissible path/current support correspondence

#### Law text

`PathRel_adm(r)` is defined to contain exactly the tuples

```text
R=(f_R,F_R,s_R,S_R,Gamma_R)                     (B1-3)
```

satisfying all of the following.

1. **Smooth actual support map.**

   ```text
   f_R:M_G->M_G' is a proper smooth map whose restriction to the old
   physical image has full rank dim(M_G).         (B1-4)
   ```

   In the equal-dimensional DoR-015 surface family it is a local
   diffeomorphism on that image; the embedded horn requires a proper
   embedding.  The same-carrier attachment horn is `f_R=id` on the old
   image, not a separate law.

2. **Actual path refinement.**  `Gamma_R` assigns every refined edge an
   actual V005 physical path, and

   ```text
   f_R compose gamma_(G,e)
    =ordered target-child path chain specified by s_R. (B1-5)
   ```

3. **Incidence and current.**

   ```text
   partial_G' s_R=s_R^0 partial_G,
   S_R=s_R|ker(B_G^T),
   ker(S_R)={0},
   J_G'(S_Rc)=f_(R*)J_G(c).                     (B1-6)
   ```

4. **Support.**  The induced `F_R` preserves inclusions, finite unions, and
   disjointness on the actual local support poset, and

   ```text
   Supp_G'(S_Rc) subset F_R(Supp_G(c)).          (B1-7)
   ```

5. **Family laws.**  The full admissible set is closed under admitted
   relabeling, frame-torsor action, orientation/reality, restriction, and
   batching.  Composition uses `f_S compose f_R` and `S_SS_R`.  Actual
   common-refinement diamonds require equality of the two path/current maps
   at their common target.

6. **Finite authority.**  Every restriction to a sealed finite stage
   reproduces the exact DoR-008 path/current result.  No formal overlay is
   treated as an actual target.

#### Law alternatives and void conditions

| Horn inside the one law | Admitted form | Void condition |
|---|---|---|
| embedded refinement horn | proper smooth full-rank embedding on the old image; old paths are ordered unions of target child paths | unrelated supports, failed full rank, deleted old cycle, failed current pushforward, or failed covariance |
| same-carrier attachment horn | `M_G=M_G'`, `f_R=id` on the old image; new target cells/paths attach with actual local support | nonlocal attachment, false incidence, or spill that violates `(B1-7)` |
| empty/reject horn | `PathRel_adm(r)` has no term for that rail arrow | any later use of the rejected arrow as a physical generator |

The horns are not selected.  They define the membership law's permitted
forms.  The source/target paths are anchored in V005 A2 and the currents in
Q-408.  The unrelated-path and cycle-deletion witnesses are standing
falsifiers.

```text
W1_PATH_CURRENT_LAW = LAW_ONLY / BUNDLE_READY_BASE_MAP
W1_ADMISSIBLE_SET_MAY_BE_EMPTY = true
W1_PROPOSED_NOT_ADOPTED = true
```

### 1.3 Law W4 — admissible bundle-typed local-field relation

The base objects carry the ratified principal U(1) bundles

```text
pi_G:P_G->M_G,
pi_G':P_G'->M_G'.                                (B1-8)
```

For `R in PathRel_adm(r)`, `FieldExt_adm(R)` is defined to contain exactly
the tuples

```text
E_R=(e_G',mu_G',A_G',F_G',tilde_f_R,iota_R)     (B1-9)
```

satisfying all of the following.

1. **Smooth full-rank bundle lift.**  `tilde_f_R` is smooth,
   U(1)-equivariant, covers `f_R`, and has full rank on the old bundle
   image:

   ```text
   tilde_f_R:P_G->P_G',
   pi_G' compose tilde_f_R=f_R compose pi_G,
   tilde_f_R(p z)=tilde_f_R(p) z,
   rank(d tilde_f_R)=dim(P_G) on the old image.  (B1-10)
   ```

   Equivalently it supplies an equivariant bundle isomorphism

   ```text
   iota_R:P_G isomorphic_to f_R^*P_G'             (B1-11)
   ```

   over `id_(M_G)`.  The law retains the full gauge-covariant family of such
   lifts/isomorphisms.  It never selects one.

2. **Characteristic-class discipline.**  Membership requires

   ```text
   c_1(P_G)=f_R^*c_1(P_G') in H^2(M_G;Z).        (B1-12)
   ```

   For identities this is equality.  Under composition the pullbacks obey

   ```text
   c_1(P_G)
    =f_R^*c_1(P_G')
    =f_R^*f_S^*c_1(P_G'')
    =(f_S compose f_R)^*c_1(P_G'').             (B1-13)
   ```

   On an actual common-refinement diamond the two pullback classes must
   agree at the common source.  Finite restriction uses ordinary naturality
   of `c_1`.  Under the ratified U(1) reality/conjugation action,
   `c_1(conj(P))=-c_1(P)` on both sides, so the equality is covariant rather
   than silently treated as invariant.  A class mismatch voids the member
   before a connection is pulled back.

3. **Coframe and density.**  `f_R` has full rank on the old image, so
   pullback of the target coframe is nondegenerate there.  With the admitted
   frame-torsor intertwiner carried family-wide,

   ```text
   e_G = f_R^* e_G' on the old image,
   mu_G=f_R^*mu_G' on the old image,              (B1-14)
   ```

   and `mu_G'` is positive.  `Cof_R` and `Dens_R` are the induced operators
   in the already declared R4 unit classes.  Their duality square commutes;
   no scale or frame is selected.

4. **Connection through the bundle lift.**  The source-bundle connection is
   compared to the target connection only through `(B1-10)`/`(B1-11)`:

   ```text
   eta_conn,R(A_G')
    :=tilde_f_R^*A_G'
     =iota_R^*(f_R^*A_G'),
   A_G=eta_conn,R(A_G') on the old image.         (B1-15)
   ```

   A bare base-map symbol `f_R^*A_G'` without `iota_R` is not a typed
   connection on `P_G` and is forbidden.

5. **Curvature and characteristic form.**  With `F_G'=Curv(A_G')`, define

   ```text
   eta_curv,R(F_G'):=tilde_f_R^*F_G'.            (B1-16)
   ```

   Naturality gives

   ```text
   eta_curv,R(Curv(A_G'))
    =Curv(eta_conn,R(A_G')).                     (B1-17)
   ```

   At the de Rham level, the sealed U(1) Chern--Weil class of `F` represents
   the real image of `c_1`; `(B1-12)` and `(B1-17)` therefore carry the same
   topological class under restriction.  No coefficient or curvature
   normalization beyond the ratified U(1) convention is introduced.

6. **Support, units, and covariance.**  Coframe, density, connection, and
   curvature restrictions are supported on the mapped old region.  The
   U(1) action, gauge covariance, CTP reality, E_post orientation, and R4
   unit seams commute with the lift.  All lawful lifts remain as a covariant
   family modulo the ratified gauge action.

7. **Composition and common refinement.**  Under the canonical pullback
   associator, bundle isomorphisms obey

   ```text
   iota_(S compose R)
    =(f_R^*iota_S) compose iota_R.               (B1-18)
   ```

   The corresponding equivariant lifts compose.  At actual diamonds, the
   two composite bundle isomorphisms agree up to the admitted U(1) gauge
   action, and their connection/curvature pullbacks agree as covariant
   classes.

8. **Finite authority.**  Every restriction reproduces the sealed finite
   U(1) path, connection, current, coframe/density, reality, and kernel
   structures exactly.  A bundle, tangent, or class mismatch is not hidden
   by completion.

#### Law alternatives and void conditions

| Horn inside the one law | Admitted form | Void condition |
|---|---|---|
| bundle-lift horn | smooth full-rank equivariant `tilde_f_R` covering the base refinement | failure of equivariance, cover square, rank, gauge covariance, or old-image agreement |
| pullback-isomorphism horn | smooth equivariant `iota_R:P_G≈f_R^*P_G'`; all compatible isomorphisms retained | class mismatch, no isomorphism, selected gauge lift, or failed composition |
| compatible field-torsor horn | full torsor of connection extensions and all compatible coframe/density members on new cells | empty torsor is allowed as a set but supplies no witness; noncovariant stabilizer, curvature mismatch, or unit failure voids an alleged member |
| empty/reject horn | `FieldExt_adm(R)` has no term | any later use of `R` as a full P4 field generator |

The lift and pullback-isomorphism horns are equivalent presentations of the
same carrier requirement, not two separately selectable physics choices.

```text
W4_LOCAL_FIELD_LAW = LAW_ONLY / BUNDLE_TYPED
W4_ADMISSIBLE_SET_MAY_BE_EMPTY = true
W4_PROPOSED_NOT_ADOPTED = true
```

---

## 2. B2 — certificates, topological tests, and no-selection

### 2.1 Bundle-lift/pullback equivalence

Given `tilde_f_R`, define

```text
iota_R(p)=(pi_G(p),tilde_f_R(p)) in f_R^*P_G'.  (B2-1)
```

Equivariance and the cover square make `(B2-1)` a principal-bundle map over
`M_G`.  Full rank and fiberwise U(1) bijectivity make it an isomorphism onto
the pullback bundle on the old image.  Conversely, projecting the second
component of an `iota_R` member gives `tilde_f_R`.  Thus the two horns encode
one typed datum.

This is a conditional theorem about any admitted tuple.  It does not prove
that such a tuple exists.

### 2.2 Characteristic-class certificate

Naturality of the universal first Chern class gives

```text
c_1(f_R^*P_G')=f_R^*c_1(P_G').                  (B2-2)
```

An `iota_R` member implies

```text
c_1(P_G)=c_1(f_R^*P_G')=f_R^*c_1(P_G'),         (B2-3)
```

so `(B1-12)` is necessary.  It is installed as a pre-connection membership
test rather than asserted as an existence theorem.  Composition is `(B1-13)`;
restriction and common-refinement naturality follow from functoriality of
cohomological pullback.

```text
CHARACTERISTIC_CLASS_TEST = INSTALLED
CLASS_EQUALITY_ASSERTED_FOR_ALL_RAIL_ARROWS = false
CLASS_MISMATCH_VOIDS_MEMBER = true
```

### 2.3 Smooth full-rank certificate

For an alleged member, compute `df_R` and `d tilde_f_R` on the old image.
Membership requires the ranks in `(B1-4)` and `(B1-10)`.  Then target
coframes pull back to nondegenerate source coframes, positive densities
remain positive under the orientation-compatible map, and the bundle lift
does not collapse a horizontal or vertical field direction.

```text
SMOOTHNESS_TEST = INSTALLED
FULL_RANK_TEST = INSTALLED
DEGENERATE_PULLBACK_VOIDS_MEMBER = true
```

### 2.4 Gauge/no-selection certificate

If two lifts differ by a U(1) gauge transformation, both remain in the
admissible family.  Connections and curvature transform by the ratified
gauge law; no lift is privileged.  Simultaneous relabeling, frame changes,
orientation reversal, and reality carry the entire admissible set to the
corresponding set at the transformed arrow.

```text
BUNDLE_LIFT_SELECTED = false
GAUGE_REPRESENTATIVE_SELECTED = false
FRAME_SELECTED = false
PATH_MEMBER_SELECTED = false
```

---

## 3. B3 — draft DoR-020 amendment text and conditional transport

### 3.1 Amendment placement

```text
DRAFT DOR-020 AMENDMENT — WHERE-CONTENT FOR B_Q408_REFINEMENT

Status: PROPOSED AMENDMENT TEXT; NOT A RULING.

DoR-020's six generators, J1--J15 joint-equalizer condition, conditional
license, and pre-witness prohibitions remain unchanged.

For every primitive refinement arrow r:G->G', replace the uninstantiated
P4/X4 where-slots by the admissible subcarrier X4_where(r) subset X4(r)
defined below.  X4_where(r) may be empty.

(W1) Gamma_R and S_R belong to the law-only PathRel_adm(r) of Section 1.2:
     a proper smooth full-rank actual path/current refinement satisfying
     incidence, support, covariance, composition, common-refinement, and
     exact finite restriction laws.

(W2) P_R is not declared.  It is the canonical construction
     P_R=Phi_G'^(-1)S_RPhi_G and must pass old-image fidelity,
     relative no-leakage, and local supported-range certificates.

(W4) Cof_R,Dens_R,eta_conn,R,eta_curv,R belong to the law-only
     FieldExt_adm(R) of Section 1.3.  Membership includes a smooth full-rank
     U(1)-equivariant lift tilde_f_R, equivalently an isomorphism
     iota_R:P_G isomorphic_to f_R^*P_G'; characteristic-class equality;
     coframe/density duality; bundle-typed connection and curvature
     transport; covariance, composition, common-refinement, units, support,
     and exact finite restrictions.

The amendment defines admissibility only.  It binds no member and asserts
neither marginal nor joint inhabitance.  A certified [EQ6] witness must
exhibit one joint J1--J15 term before member binding, fixed-point execution,
or any end test.
```

This text populates exactly the existing P4/X4 fields in `(0-1)`.  It does
not add a seventh generator or a new theory stratum.

### 3.2 Re-verification of the two V004 constructions

Given an arbitrary alleged W1 member, the existing ratified maps construct

```text
P_R
 =Phi_G'^(-1)S_RPhi_G
 =Abar_G'^(-1)R_G'S_RR_G^(-1)Abar_G.           (B3-1)
```

The candidate is admitted only if

```text
S_R^*R_G'S_R=R_G,                               (B3-2)

g_(K,G')(S_RPhi_G(Tbar_G(O)),K_G'(V))=0
  whenever F_R(O) intersect V=empty,            (B3-3)

P_R(Tbar_G(O)) subset Tbar_G'(F_R(O)).          (B3-4)
```

The Q-432 `P=id` witness passes `(B3-2)`--`(B3-4)` even with an
off-diagonal pre-existing metric; the Q-430 old-to-new mixer fails
`(B3-3)` and `(B3-4)`.  The clause repair changes none of these results.

### 3.3 Bundle-typed conditional field transport

Given an arbitrary alleged W4 member, define the actual restriction maps

```text
eta_conn,R(A_G')=tilde_f_R^*A_G'
                 =iota_R^*(f_R^*A_G'),

eta_curv,R(F_G')=tilde_f_R^*F_G',

eta_cof,R(e_G')=f_R^*e_G',
eta_dens,R(mu_G')=f_R^*mu_G'.                  (B3-5)
```

Every expression is now typed.  Pullback functoriality and curvature
naturality give identity, composition, reality/gauge covariance, support,
and

```text
eta_curv,R compose Curv
 =Curv compose eta_conn,R.                      (B3-6)
```

The smooth full-rank condition makes the coframe pullback nondegenerate;
orientation compatibility preserves density positivity.  The class
condition ensures the source and pullback target bundles lie in the same
U(1) topological sector.  Common-refinement transport follows from
`(B1-18)` and the clause's diamond equality.

```text
BUNDLE_TYPED_TRANSPORT_DERIVATION = PASS_CONDITIONALLY / TYPE-P
BARE_BASE_PULLBACK_OF_CONNECTION_USED = false
```

### 3.4 Amendment consequence boundary

If the principal adopts the amendment, it changes only the law of
admissibility for the existing `B_Q408_REFINEMENT` coordinate.  It licenses
continued conditional theorem-building about any alleged member.  It does
not license:

```text
member binding;
claiming PathRel_adm or FieldExt_adm inhabited;
C1 resumption as an executed full-family build;
fixed-point execution;
the sealed-number end test.
```

Those remain behind a certified joint `[EQ6]` witness.

---

## 4. B4 — regressions, falsifiers, anti-tuning, and delta

### 4.1 Nine cumulative regressions

| Regression | V005 execution | Result |
|---|---|---|
| pure new-cycle profile | remains outside the old-image pullback | **PASS** |
| covariance orbit/moduli | full admissible families retained | **PASS** |
| all-stage skeleton | stagewise actual surfaces only | **PASS** |
| rank-preserving `Ref_path` | `f=id`, canonical bundle identity, `P=id` | **PASS** |
| cycle-creating upward quotient | none defined | **PASS** |
| arbitrary-profile restriction | old-image only; target new-cycle kernel retained | **PASS WITH SCOPE** |
| Q-430 old-to-new Riesz mixer | rejected by relative no-leakage/local range | **PASS** |
| Q-432 `P=id` overreach witness | admitted; global metric cross term tolerated | **PASS** |
| Q-435 bundle/topology attack | lift/isomorphism, rank, and `c_1` tests installed | **PASS — ILL-TYPED MEMBER REJECTED** |

### 4.2 Permanent regressions

| Regression | Result |
|---|---|
| abstract kernel | **PASS** — `P_R` uses actual Q-408 maps |
| circular `pi_Mx` | **PASS** — no reader defines a path, lift, or field |
| misstated nonemptiness | **PASS** — both laws explicitly permit empty admissible sets |
| Hodge from isometry | **PASS** — no Hodge or bundle existence inferred from the metric |
| objectwise minimum/selection | **PASS** — no path, field, bundle lift, or gauge representative selected |
| joint equalizer | **PASS** — marginal laws are never promoted to a joint witness |

### 4.3 Failure-capable falsifiers

1. **Bundle-lift ambiguity.**  Distinct gauge-related lifts remain as a full
   family.  Selecting one fails the no-selection certificate.
2. **Characteristic-class mismatch.**  If `(B1-12)` fails, no alleged W4
   member exists for that tuple; formal connection symbols cannot repair it.
3. **Rank defect.**  If `df_R` or `d tilde_f_R` loses required rank, the
   coframe/field pullback is degenerate and the tuple is rejected.
4. **Curvature mismatch.**  Failure of `(B1-17)` rejects the field tuple even
   if support and units pass.
5. **Coframe/density mismatch.**  Failure of nondegeneracy, positivity, or
   duality rejects the tuple.
6. **Unrelated paths.**  A signed rail map between unrelated supports fails
   W1 before any bundle test.
7. **Common-refinement class mismatch.**  Different pulled-back `c_1`
   classes along two routes reject the diamond.
8. **Empty admissible family.**  This is not a clause failure.  It leaves
   `[EQ6]` open and forbids member binding.
9. **Finite restriction mismatch.**  Any failure to reproduce a sealed
   finite bundle/path/current/kernel result voids the alleged member.

### 4.4 Anti-tuning ledger

```text
1  Verify Q-435 and freeze its nonemptiness and bundle counterexamples.
2  Freeze DoR-020's conditional equalizer semantics.
3  Freeze existing P4/X4 field names before drafting amendment text.
4  Remove every inhabitance assertion from W1 and W4.
5  Type the base map's smooth full rank before coframe pullback.
6  Type the U(1) lift/isomorphism before connection pullback.
7  Install c_1 compatibility before curvature transport.
8  Derive transport only for an arbitrary alleged member, selecting none.
9  Re-run V004's passing constructions and all nine regressions.
10 Inspect no response, threshold, fixed point, end test, or measured datum.
```

### 4.5 Delta versus V004

| V004 clause content | V005 disposition |
|---|---|
| `declare a nonempty PathRel` | replaced by possibly empty law-defined `PathRel_adm` |
| `declare a nonempty FieldExt` | replaced by possibly empty law-defined `FieldExt_adm` |
| embedded and identity horns treated as separate | identity attachment scoped as same-carrier horn of the local-map law |
| proper local map | strengthened to smooth full rank on old image |
| bare `f_R^*A` | forbidden; replaced by bundle lift/pullback-bundle isomorphism |
| no topological bundle check | `c_1(P_G)=f_R^*c_1(P_G')` installed with composition/restriction diamonds |
| coframe/density clauses | full-rank, positivity, duality, and units made failure-capable |
| connection/curvature clauses | bundle-typed and conditionally derived |
| two V004 constructions | carried unchanged and reverified |
| amendment placement | drafted explicitly inside existing P4/X4 fields |
| member status | unchanged: no member bound; `[EQ6]` open |

## Final board

```text
CLAUSES = LAW_ONLY_BUNDLE_TYPED
AMENDMENT_TEXT = DRAFTED / PROPOSED_NOT_ADOPTED

PATH_CURRENT_WHERE_LAW = COMPLETE
LOCAL_FIELD_WHERE_LAW = COMPLETE
U1_BUNDLE_LIFT_CERTIFICATE = INSTALLED
PULLBACK_BUNDLE_ISOMORPHISM_CERTIFICATE = INSTALLED
SMOOTH_FULL_RANK_CERTIFICATE = INSTALLED
CHARACTERISTIC_CLASS_CERTIFICATE = INSTALLED

CANONICAL_TEST_TRANSPORT = PASS
RELATIVE_NO_LEAKAGE = PASS
BUNDLE_TYPED_FIELD_TRANSPORT = CONDITIONALLY_DERIVED

P4_X4_FIELDS_POPULATED_BY_DRAFT =
  Gamma_R + P_R + S_R + Cof_R + Dens_R + eta_conn_R + eta_curv_R

CLAUSE_ASSERTS_INHABITANCE = false
MEMBER_SELECTED = false
MEMBER_BOUND = false

FULL_Ext_cycle_MEMBER = OPEN / TYPE-U
B_Q408_REFINEMENT_FULL_ROOT = OPEN / TYPE-U
JOINT_EQ6 = OPEN
C1_RESUMPTION = N/A
READY_FOR_CHECK = yes

TARGET_TUNING_USED = false
ABSTRACT_STANDIN_USED = false
CIRCULAR_CERTIFICATE_USED = false
MACHINERY_APPEAL = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
fixed_point_executed = false
end_test_executed = false
numeric_evaluation = false
measured_constant_compared = false
```

Seal this artifact, mirror artifact and sidecar byte-identically to
`alpha-program-archive/workspace/`, report hashes, and stop.  No register,
plan, tracker, git, commit, or push action belongs to this lane.
