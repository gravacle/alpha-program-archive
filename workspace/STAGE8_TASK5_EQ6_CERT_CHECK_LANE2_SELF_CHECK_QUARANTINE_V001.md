# STAGE 8 TASK 5 / EQ6 - CERT CHECK AND ZERO-DEFECT SECTION - LANE 1 V001

Date: 2026-08-04
Lane: Codex Lane 1
Task: 5 / EQ6 / hostile certificate check and physical-section determination
Custody: adversarial reviewer and derivation lane

## Lead result

```text
CERT = CONFIRMED

SECTION = NEEDS(
  CONSTRUCTIBLE_WITH_ROUTE:
  NONEMPTY_COVARIANT_ZERO_DEFECT_SECTION_ON_THE_ACTUAL_FIXED
  DOR019_Q408_POSITIVE_SOURCE_FAMILY,
  INCLUDING_COMMON_REFINEMENT_COHERENCE)

SECTION_DERIVABLE_FROM_CURRENT_STACK = false / TYPE-R
SECTION_EXHIBITED = false / TYPE-U
DIRECT_SUM_MODEL_ADMITTED = true / TYPE-P
DIRECT_SUM_MODEL_IS_PHYSICAL_SECTION = false

ALL_RANK = PARTIAL / TYPE-U
JOINT_EQ6 = PARTIAL / TYPE-U

GEOMETRY_VS_RAILS =
  the certificate equations and decision procedure are rails;
  E_geom, the fixed Riesz form, Phi, local supports, and the existence of
  actual positive-source zero-defect members are surface geometry.
  The remaining stop is geometric inhabitance, not a missing rail.

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The Lane-2 certificate is a genuine, failure-capable proof object.  Its
four defects recover OLD_FID, local orthogonal excision, the corrected
disjoint/contact-exclusive RNL family, and LR without replacing the fixed
DoR-019 metric or the fixed Q-408 analysis map.  Both cycle-creating
diamonds pass conditionally when their actual legs carry coherent
zero-defect terms.  The direct-sum model is admitted and proves joint
consistency.

That is not yet an actual physical section.  The fixed stack admits both a
zero-defect compatibility model and fixed-data countermodels with nonzero
metric or support defects.  Covariance carries zeros to zeros but does not
create a zero.  Stagewise or orbitwise nonemptiness would also not prove a
single coherent all-rank section.  The exact remaining object is therefore
the nonempty common-refinement equalizer of the physical zero-defect loci.

---

## 0. Preflight and custody

### 0.1 Required checks

```text
LOCKED_PROCESS = READ
REGISTER_HEAD = Q-443
PREFLIGHT = PASS
```

The artifact under review was hash-verified before reading:

```text
STAGE8_TASK5_EQ6_LOCAL_ORTHOGONAL_EXCISION_CERT_LANE2_V001.md
SHA-256 = d61a550a33bf1215c35f4d6f27cd2ec5d644b93a05e16d08fe3d43ded3416817
SEAL = OK
```

The governing Lane-1 standard was also seal-verified:

```text
STAGE8_TASK5_EQ6_DIAMOND_CHECK_AND_JOINT_ADMISSION_TYPING_LANE1_V001.md
SHA-256 = 6cd40961b3fc7862e5f6e92904b49d595115ba612d74b97a7e27df096f18d445
```

The adopted where-clause artifact and its final check were checked at their
recorded hashes.  The register seal at Q-443 was valid.  No later entry was
consumed.

### 0.2 Register sweep

```text
Q-408  fixed finite current/kernel calculus, analysis maps, and supports;
Q-418  admitted rank-preserving subdivision with P=id;
Q-422  [EQ6] requires one joint witness, not separate marginal witnesses;
Q-427  surface geometry cannot be replaced by categorical rails;
Q-430  a fixed Riesz mixer can preserve algebra while leaking support;
Q-432  relative no-leakage replaces forbidden global orthogonality;
Q-438  W1/W4 are adopted possibly-empty membership laws;
Q-439  the zero-source first-cycle member exists;
Q-440  positive-source all-rank members remain the need;
Q-441  disjoint and contact cycle-creating diamonds stop on fixed defects;
Q-442  the tests are jointly consistent; contact retains OLD_FID,
       exclusive-region RNL, and LR;
Q-443  Cert_LOE is built; the physical zero-defect section remains open.
```

No settled entry supplies nonemptiness of the actual positive-source
zero-defect locus.  No settled entry authorizes binding a metric, support
map, refinement member, or certificate term.

---

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| I1 certificate and diamonds | **PASS** | The four defects are correctly typed on fixed data; disjoint and contact diamonds pass exactly conditionally, with the corrected contact set retained. |
| I2 direct-sum consistency | **PASS** | The certificate admits the Q-442 direct-sum model term without promoting it to a physical inhabitant. |
| I3 zero-defect section | **NEEDS / CONSTRUCTIBLE-WITH-ROUTE** | Current authorities neither force nor exhibit a nonempty coherent physical zero locus; the exact route and countermodels are given below. |
| I4 cascade | **PASS AS CONDITIONAL / NOT EXECUTED** | If the section exists, composition and diamond coherence yield all-rank admission; because no section is exhibited here, all-rank and joint EQ6 remain partial. |
| I5 discipline and fresh attacks | **PASS WITH FRONTIER FINDING** | No tuning or selection appears; two fresh attacks prove that definitional and marginal nonemptiness cannot discharge the physical equalizer. |

---

## 2. I1 - hostile recomputation of the certificate

### 2.1 Fixed-data input and geometry-first excision

For an actual W1/W4 cycle-creating candidate `r:G->G'`, the surface data
first give the conserved-current injection

```text
S_r: K_G -> K_G'
```

and the actual old/new support relation.  Only when that relation supplies
a basis-free old-current retraction is

```text
E_r^geom: K_G' -> K_G',
(E_r^geom)^2 = E_r^geom,
image(E_r^geom) = S_r K_G,
E_r^geom S_r = S_r
```

admitted.  This is the correct geometry-first order.  A Hilbert-space
orthogonal projector is not substituted for missing surface data.

For an RNL-relevant old/new local pair, define

```text
A_r(O) = S_r Phi_G(Tbar_G(O)),
N_r(W) = ker(E_r^geom) intersect K_G'(W),
H_r(O,W) = A_r(O) direct-sum N_r(W).
```

On the fixed DoR-019 Riesz form, positivity gives the unique local
orthogonal projector

```text
E_r;O,W^orth
  = j_A (j_A^* R_K,G' j_A)^(-1) j_A^* R_K,G' |_H.
```

It is diagnostic.  The physical requirement is the failure-capable
equality `E_r;O,W^geom = E_r;O,W^orth`; nothing is rotated, rescaled, or
repaired after the test.

### 2.2 Four defects

The four displayed operators recover the required tests exactly:

```text
Def_fid(r) = S_r^* R_K,G' S_r - R_K,G;

Def_orth(r;O,W) = E_r;O,W^geom - E_r;O,W^orth;

Def_leak(r;O,W) = i_W^* R_K,G' S_r Phi_G i_O;

P_r = Phi_G'^(-1) S_r Phi_G;
Def_supp(r;O) = q_G',F_r(O) P_r i_O.
```

Their zeros mean, respectively:

```text
OLD_FID;
agreement of actual excision with fixed-metric local orthogonality;
RNL on every active disjoint or contact-exclusive pair;
LR for every actual old local region.
```

The apparent overlap of `Def_orth` and `Def_leak` is harmless and useful:
the first checks the actual geometry projector, while the second checks the
same required vanishing in the ratified RNL source/current typing.  The
support defect is independent; a diagonal metric does not force `Phi` to
preserve support.

### 2.3 Minimal disjoint calculation

On the target rank-two current space with ordered cycle representatives
`c_U,c_V`, write the fixed Gram form

```text
g = [[alpha, zeta], [conj(zeta), delta]].
```

For the U-old leg,

```text
E_U^geom(c_V) = 0,
E_U^orth(c_V) = (conj(zeta)/alpha)c_U.
```

Thus `Def_orth,U=0` if and only if `zeta=0` on that local pair.  The V-old
leg gives the conjugate equation.  OLD_FID additionally requires

```text
alpha = alpha_0,
delta = delta_0,
```

and LR independently requires every appropriate `Def_supp` to vanish.
The certificate therefore rejects the Q-430 sector mixer without changing
the actual current injection.

### 2.4 Corrected contact calculation

Let the old and new cycle corridors meet only at the recorded endpoint
`q`, and remove the contact locus when forming exclusive local tests.  For
nonzero exclusive tests the two leakage defects have the form

```text
Def_leak,U = theta_U zeta,
Def_leak,V = theta_V conj(zeta).
```

Endpoint contact silences RNL only for pairs whose supports actually meet.
It does not silence the exclusive-region family, and it does not affect
OLD_FID.  The complete contact requirement is therefore exactly

```text
OLD_FID + EXCLUSIVE_REGION_RNL + LR.
```

This matches the Q-442 correction.  No LR-only remnant survives.

### 2.5 Composition and common refinement

For certificate terms `r:G->G'` and `s:G'->G''`, the composite test map is
forced:

```text
P_s P_r
 = Phi_G''^(-1) S_s Phi_G' Phi_G'^(-1) S_r Phi_G
 = Phi_G''^(-1) S_s S_r Phi_G
 = P_sr.
```

Fidelity composes as

```text
Def_fid(sr)
 = S_r^* Def_fid(s) S_r + Def_fid(r),
```

so zero defects remain zero.  Successive LR inclusions give

```text
P_sr(Tbar_G(O))
 subset Tbar_G''(F_s(F_r(O))).
```

The inherited new sector stays orthogonal to transported old analysis by
the first term and OLD_FID for the second; the fresh new sector is checked
by the second term.  This is local and support-indexed, not a global
orthogonal decomposition.

On an actual common-refinement diamond, the certificate still requires the
actual W1/W4 maps and the local certificate terms to agree.  It does not
infer a geometric split from a bare commuting rail square.  With that
LOE6 hypothesis, the fixed local orthogonal projector is unique and the
two composite terms agree.  Hence the conditional diamond theorem is
valid at its stated scope.

### 2.6 Diamond reruns

| Diamond | Geometry | Certificate result | Physical standing |
|---|---|---|---|
| rank-preserving subdivision | `S=id`, no new local cycle sector, `P=id` | all defects zero | **PASS / ADMITTED** |
| disjoint cycle creation | actual U/V corridors and bundle square | pass if both positive-source legs have zero `Def_fid`, `Def_orth`/`Def_leak`, and `Def_supp` | **CONDITIONAL PASS / TERM OPEN** |
| endpoint contact creation | actual corridors share only recorded contact | pass if OLD_FID, every exclusive RNL defect, LR, and W4 all vanish | **CONDITIONAL PASS / TERM OPEN** |

The conditions are genuine: the Q-430 mixer fails, while the Q-432
rank-preserving `P=id` witness passes without imposing orthogonality on
unrelated pre-existing cycles.

```text
I1 = PASS
CERT = CONFIRMED
```

---

## 3. I2 - direct-sum consistency model

Take the compatibility data

```text
K_G' = S_r K_G direct-sum N_r,
R_K,G' = S_(r,*) R_K,G direct-sum R_N,
Tbar_G' = P_r Tbar_G direct-sum Tbar_N,
Phi_G' = Phi_G direct-sum Phi_N,
E_r^geom(x,n) = (x,0).
```

Then the fixed-metric orthogonal projector equals `E_r^geom`, OLD_FID is
exact, the cross-support pairings vanish, and the direct-sum test map is
support-local.  Identity bundle pullbacks satisfy W4.  Consequently every
certificate defect is zero, including the corrected contact-exclusive
family.

This model therefore proves

```text
Cert_LOE is jointly consistent and its abstract/model fiber is nonempty.
```

It does not prove

```text
the actual retained DoR-019/Q-408 positive-source family contains such a
member.
```

The reviewed artifact keeps this distinction explicit, so the model is
admitted rather than laundered into physical geometry.

```text
I2 = PASS
DIRECT_SUM_MODEL = ADMITTED
JOINT_UNSATISFIABLE = false / TYPE-R
```

---

## 4. I3 - the zero-defect section

### 4.1 The exact section

Let `Prim_pos` be the actual positive-source W1/W4 primitive family, with
its covariance and common-refinement maps.  For each primitive `r`, let

```text
Z_r = {x in Prim_pos(r):
       Def_fid(x)=0,
       Def_orth(x;O,W)=0 for every relevant pair,
       Def_leak(x;O,W)=0 for every active disjoint/exclusive pair,
       Def_supp(x;O)=0 for every old local region,
       W1/W4 and LOE6 hold}.
```

The required object is not merely `Z_r != empty` for isolated `r`.  It is

```text
Gamma_cov(Z) != empty,
```

where a section is closed under covariance, restriction, composition, and
every actual common-refinement diamond, without selecting a basis,
orientation, frame, filtration, or isolated member.

### 4.2 Non-derivability from the current stack

The following fixed-data family separates the adopted membership laws from
section existence.  On `K=span(c_U,c_V)`, choose the positive Hermitian
form

```text
g_epsilon = [[1, epsilon], [conj(epsilon), 1]],
0 < |epsilon| < 1,
```

with actual disjoint U/V support and the unchanged W1/W4 geometry.  This is
the standing sector-mixer shape.  For the U-old leg,

```text
Def_leak,U = theta_U epsilon != 0,
E_U^orth(c_V) = conj(epsilon)c_U != 0
               = E_U^geom(c_V).
```

The V-old leg fails conjugately.  Covariance, reality, positivity, units,
and the raw geometric square can all remain valid.  Therefore those
authorities do not force zero metric defects.

Independently, even with a diagonal metric, a support-nonlocal analysis map
can satisfy the global carrier isomorphism while sending an old local test
to a current with a new-region component.  Then

```text
Def_orth = Def_leak = 0,
Def_supp != 0.
```

Thus metric locality cannot derive analysis locality.  The four zero
families are genuinely load-bearing.

These countermodels and the passing direct-sum model show:

```text
current ratified/adopted content permits both zero-defect and nonzero-defect
fixed-data realizations;
therefore physical zero-defect section nonemptiness is not derivable.
```

Covariance does not change that conclusion.  It proves only

```text
x in Z_r  implies  U.x in Z_Ur.
```

It does not prove that any `x` exists.

### 4.3 Exact constructive route

The remaining object is **CONSTRUCTIBLE-WITH-ROUTE**, not presently
derived and not satisfied by a declaration-only stand-in:

1. Populate the actual positive-source W1/W4 primitive orbits from the
   adopted where-laws, carrying the real path/current, bundle, and support
   data.
2. Derive `E_r^geom` from each actual new-cell support relation.  Reject a
   candidate when this requires a cycle-basis choice or deletes a visible
   current.
3. On the fixed DoR-019 metric and fixed Q-408 `Phi`, compute all four
   defect families without changing the input.
4. Retain the complete covariance orbit of every zero-defect candidate;
   do not select an isolated member.
5. Prove this orbit family nonempty on every required positive-source
   stage and prove restriction/composition closure.
6. Form the actual common-refinement equalizer and exhibit one nonempty
   covariant section through it.  Separate nonempty leg fibers do not
   suffice.

The physical theorem needed to make the route land may equivalently be
stated as a fixed-data surface-locality/excision theorem:

```text
the actual positive-source refinement generator preserves the old Riesz
form, is relatively orthogonal on every active local old/new pair, carries
the Q-408 analysis map support-locally, and does so coherently on actual
diamonds.
```

This is geometry.  A new clause simply asserting nonemptiness would be a
new physical adoption and would not count as the proof-carrying witness
required by the strict `[EQ6]` regressions.  No such clause is authored
here.

```text
I3 = NEEDS(CONSTRUCTIBLE_WITH_ROUTE:
           PHYSICAL_ZERO_DEFECT_NONEMPTINESS_AND_COHERENT_SECTION_THEOREM)
SECTION_EXHIBITED = false
```

### 4.4 Geometry versus rails

| Object | Surface geometry | Rail/proof machinery |
|---|---|---|
| primitive | actual path/current support, U(1) bundle, coframe, density, connection, curvature | W1/W4 commuting diagrams |
| excision | actual old/new current split from the new-cell relation | idempotent and image equations for `E_geom` |
| metric test | fixed DoR-019 Riesz pairing | `Def_fid`, `Def_orth`, `Def_leak` |
| analysis locality | fixed Q-408 `Phi` and actual support map | `Def_supp` and quotient square |
| all-rank section | actual positive-source members across refinements | covariance/composition/equalizer conditions |

The rails are now complete enough to test a member.  They do not populate
the geometric fiber.

---

## 5. I4 - conditional cascade

No physical section was exhibited in Section 4, so the requested
on-section cascade cannot be executed unconditionally.  The implication
itself is valid:

```text
nonempty coherent physical Cert_LOE section
  -> both cycle-creating diamonds pass unconditionally
  -> the actual W1/W4 positive-source family closes under composition and
     common refinement
  -> the Q-408 refinement root becomes all-rank on that category
  -> B_R1 naturality, C1 completion, faithfulness, C2 response boundary,
     and C3 may consume those admitted arrows in dependency order
  -> one joint J1-J15 equalizer term is still required for [EQ6].
```

The current ledger is therefore:

| Layer | Standing after this check |
|---|---|
| certificate class and decision procedure | **BUILT / CONFIRMED** |
| compatibility-model term | **BUILT / CONFIRMED** |
| rank-preserving physical boundary | **ADMITTED** |
| positive-source physical certificate section | **TYPE-U / CONSTRUCTIBLE-WITH-ROUTE** |
| all-rank Q-408 family | **PARTIAL** |
| joint `[EQ6]` | **PARTIAL** |

```text
I4 = PASS_AS_CONDITIONAL
ALL_RANK = PARTIAL / TYPE-U
JOINT_EQ6 = PARTIAL / TYPE-U
```

---

## 6. I5 - smuggling, the too-easy test, and fresh attacks

### 6.1 Inherited regressions

| Regression | Rerun | Result |
|---|---|---|
| abstract-kernel substitution | every defect uses actual `S`, `E_geom`, fixed `R_K`, fixed `Phi`, and actual support quotients | **PASS** |
| circular map | geometry precedes `E_orth`, `P`, and every defect | **PASS** |
| false nonemptiness | model term and certificate class are separated from physical section existence | **PASS** |
| cycle-current deletion | `E_geom` diagnoses old/new support; no target current is removed from the carrier | **PASS** |
| covariance-orbit overclaim | zero loci are invariant, but covariance is not claimed to populate them | **PASS** |
| all-stage overclaim | all-rank remains conditional on the coherent section | **PASS** |
| sector mixer | nonzero `zeta` fails `Def_orth` and `Def_leak` | **PASS / REJECTED** |
| `P=id` overreach | rank-preserving subdivision passes and unrelated old sectors remain unconstrained | **PASS / ADMITTED** |
| clause nonemptiness overreach | adopted clauses are used only as membership laws | **PASS** |

### 6.2 Too-easy question

What changed at Q-443 is a real construction insight: the missing phrase
was replaced by an explicit finite defect calculus and a composition law.
What did not change is physical inhabitance.  The reviewed artifact does
not use the definitional fact

```text
the class of objects satisfying the zero equations exists as a class
```

as evidence that

```text
the fixed physical family contains an object in that class.
```

No vacuous or degenerate member is accepted.  In particular, the
zero-source base and the rank-preserving `N=0` control do not populate a
positive-source cycle-creating leg.

### 6.3 Fresh attack 1 - empty invariant zero locus

Let a covariance group act transitively on a physical candidate orbit
`X`, and let an equivariant defect have constant nonzero norm on `X`:

```text
||Def(U.x)|| = ||U Def(x) U^(-1)|| = d > 0.
```

Then the zero locus is invariant and empty.  Every covariance proof in the
certificate remains true, yet no section exists.  This refutes any attempt
to turn covariance of the defect equations into physical nonemptiness.

```text
FRESH_ATTACK_1 = PASS /
  COVARIANCE_PRESERVES_ZERO_LOCI_BUT_DOES_NOT_POPULATE_THEM
```

### 6.4 Fresh attack 2 - marginal nonemptiness is not a joint section

Suppose two legs of a common-refinement square each have nonempty
zero-defect fibers `Z_r` and `Z_u`.  Their transported composite terms may
land in disjoint subsets of the target certificate fiber:

```text
image_s(Z_r) intersect image_v(Z_u) = empty.
```

Both marginal checks pass, and every stage has a zero-defect candidate,
but no common-refinement section exists.  This is the equalizer regression
in its certificate form.  Therefore the constructive route must exhibit
the joint intersection, not merely list one member per stage.

```text
FRESH_ATTACK_2 = PASS /
  STAGEWISE_NONEMPTINESS_DOES_NOT_IMPLY_COHERENT_SECTION_NONEMPTINESS
```

### 6.5 Anti-tuning ledger

```text
1  Freeze the actual W1/W4 and fixed DoR-019/Q-408 inputs.
2  Recompute the certificate independently.
3  Run the disjoint, contact, and subdivision controls.
4  Admit the direct-sum term only as a consistency model.
5  Construct fixed-data countermodels before classifying section status.
6  State the nonempty equalizer as the exact physical need.
7  Do not inspect any response, threshold, fixed point, end test, alpha
   consequence, or measured constant.
```

No member, rank, ratio, orientation, frame, cycle basis, bundle gauge,
filtration, metric, reader, or completion was selected.

---

## 7. Final board

```text
CERT = CONFIRMED

SECTION = NEEDS(
  CONSTRUCTIBLE_WITH_ROUTE:
  NONEMPTY_COVARIANT_ZERO_DEFECT_SECTION_ON_ACTUAL_FIXED
  DOR019_Q408_POSITIVE_SOURCE_DATA,
  WITH_COMMON_REFINEMENT_EQUALIZER_NONEMPTY)

SECTION_DERIVABLE = false / TYPE-R
SECTION_EXHIBITED = false / TYPE-U
SECTION_DECLARED = false

D_SUBDIVISION = PASS / ADMITTED
D_DISJOINT = CONDITIONAL_PASS / PHYSICAL_TERM_OPEN
D_CONTACT = CONDITIONAL_PASS / PHYSICAL_TERM_OPEN
D_CONTACT_REQUIREMENTS = OLD_FID + EXCLUSIVE_REGION_RNL + LR

DIRECT_SUM_MODEL = ADMITTED_COMPATIBILITY_TERM
DIRECT_SUM_MODEL_IS_PHYSICAL = false

ALL_RANK = PARTIAL / TYPE-U
JOINT_EQ6 = PARTIAL / TYPE-U

GEOMETRY_VS_RAILS =
  rails complete enough to decide each candidate;
  geometry has not supplied a nonempty coherent positive-source zero locus

MEMBER_BINDING = false
FIXED_POINT_EXECUTION = false
END_TEST = false
NUMERIC_EVALUATION = false
MACHINERY_APPEAL = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
