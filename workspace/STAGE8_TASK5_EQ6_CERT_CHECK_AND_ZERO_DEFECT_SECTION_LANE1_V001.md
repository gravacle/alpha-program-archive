# STAGE 8 TASK 5 / EQ6 - CERT CHECK AND ZERO-DEFECT SECTION - LANE 1 V001

Date: 2026-08-04
Lane: Codex Lane 1
Task: hostile certificate check and zero-defect-section determination

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
  E_geom, the fixed Riesz form, Phi, local supports, and actual
  positive-source zero-defect members are surface geometry.
  The remaining stop is geometric inhabitance, not a missing rail.

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The certificate is a genuine failure-capable proof object. Its four
defects recover OLD_FID, local orthogonal excision, the corrected
disjoint/contact-exclusive RNL family, and LR without replacing the fixed
DoR-019 metric or Q-408 analysis map. Both cycle-creating diamonds pass
conditionally when their actual legs carry coherent zero-defect terms.
The direct-sum model is admitted and proves joint consistency.

That model is not an actual physical section. The fixed stack permits a
zero-defect compatibility model and fixed-data countermodels with nonzero
metric or support defects. Covariance carries zeros to zeros but cannot
make an empty zero locus nonempty. Stagewise nonemptiness also would not
prove a coherent all-rank section. The exact stop is the nonempty
common-refinement equalizer of the physical zero-defect loci.

---

## 0. Preflight and register sweep

```text
LOCKED_PROCESS = READ
REGISTER_HEAD = Q-443
PREFLIGHT = PASS
```

The reviewed artifact was hash-verified before reading:

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

Register entries checked:

```text
Q-408  fixed finite current/kernel calculus, analysis maps, and supports;
Q-418  admitted rank-preserving subdivision with P=id;
Q-422  [EQ6] requires one joint witness, not marginal witnesses;
Q-427  surface geometry cannot be replaced by categorical rails;
Q-430  a fixed Riesz mixer may preserve algebra while leaking support;
Q-432  relative no-leakage replaces forbidden global orthogonality;
Q-438  W1/W4 are adopted possibly-empty membership laws;
Q-439  the zero-source first-cycle member exists;
Q-440  positive-source all-rank members remain the need;
Q-441  both cycle-creating diamonds stop on fixed-data defects;
Q-442  the tests are jointly consistent; contact retains OLD_FID,
       exclusive-region RNL, and LR;
Q-443  Cert_LOE is built; its physical section remains open.
```

No settled entry supplies positive-source zero-defect nonemptiness or
licenses binding a metric, support map, refinement member, or certificate
term.

---

## 1. Verdict table

| Item | Verdict | Reason |
|---|---|---|
| I1 certificate and diamonds | **PASS** | The four defects are correctly typed on fixed data; both cycle-creating diamonds pass exactly conditionally, with the corrected contact set. |
| I2 direct-sum consistency | **PASS** | The certificate admits the Q-442 direct-sum model without promoting it to physical geometry. |
| I3 zero-defect section | **NEEDS / CONSTRUCTIBLE-WITH-ROUTE** | Current authorities neither force nor exhibit a nonempty coherent physical zero locus. |
| I4 cascade | **PASS AS CONDITIONAL / NOT EXECUTED** | A section would close all-rank admission; no section is exhibited, so all-rank and joint EQ6 remain partial. |
| I5 discipline and attacks | **PASS WITH FRONTIER FINDING** | No tuning or selection appears; fresh attacks exclude definitional and marginal inhabitance. |

---

## 2. I1 - recomputation of the certificate

### 2.1 Geometry-first input

For an actual W1/W4 cycle-creating candidate `r:G->G'`, the surface data
first give

```text
S_r: K_G -> K_G'
```

and the actual old/new support relation. Only when that relation supplies
a basis-free old-current retraction is

```text
E_r^geom: K_G' -> K_G',
(E_r^geom)^2 = E_r^geom,
image(E_r^geom) = S_r K_G,
E_r^geom S_r = S_r
```

admitted. A Hilbert-space projector is not substituted for absent surface
data.

For an RNL-relevant local pair define

```text
A_r(O) = S_r Phi_G(Tbar_G(O)),
N_r(W) = ker(E_r^geom) intersect K_G'(W),
H_r(O,W) = A_r(O) direct-sum N_r(W).
```

Positivity of the fixed DoR-019 form gives the unique local orthogonal
projector

```text
E_r;O,W^orth
  = j_A (j_A^* R_K,G' j_A)^(-1) j_A^* R_K,G' |_H.
```

This is diagnostic. Physical admission requires
`E_r;O,W^geom=E_r;O,W^orth`; nothing is rotated or rescaled after testing.

### 2.2 Defect calculus

The four operators are

```text
Def_fid(r) = S_r^* R_K,G' S_r - R_K,G;

Def_orth(r;O,W) = E_r;O,W^geom - E_r;O,W^orth;

Def_leak(r;O,W) = i_W^* R_K,G' S_r Phi_G i_O;

P_r = Phi_G'^(-1) S_r Phi_G;
Def_supp(r;O) = q_G',F_r(O) P_r i_O.
```

Their zeros mean OLD_FID, metric agreement with actual local excision,
RNL on every active disjoint/contact-exclusive pair, and LR. The overlap
between `Def_orth` and `Def_leak` is legitimate: the first checks actual
geometry, while the second checks the ratified source/current typing. The
support defect remains independent because metric locality does not force
`Phi` locality.

### 2.3 Disjoint and contact calculations

On the rank-two target with cycles `c_U,c_V`, write

```text
g = [[alpha, zeta], [conj(zeta), delta]].
```

For the U-old leg,

```text
E_U^geom(c_V) = 0,
E_U^orth(c_V) = (conj(zeta)/alpha)c_U.
```

Thus the local orthogonal-excision defect vanishes exactly when `zeta=0`.
The V leg gives the conjugate equation. OLD_FID independently requires
`alpha=alpha_0` and `delta=delta_0`; LR requires every relevant
`Def_supp` to vanish. This rejects the Q-430 mixer without changing the
actual current injection.

For the endpoint-contact diamond, remove only the recorded contact locus
when forming exclusive tests. Nonzero exclusive tests give

```text
Def_leak,U = theta_U zeta,
Def_leak,V = theta_V conj(zeta).
```

Contact silences RNL only where supports actually meet. It does not remove
exclusive pairs or OLD_FID. The corrected contact set is exactly

```text
OLD_FID + EXCLUSIVE_REGION_RNL + LR.
```

### 2.4 Composition and diamonds

For certificate terms `r:G->G'` and `s:G'->G''`,

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

and successive LR inclusions give

```text
P_sr(Tbar_G(O)) subset Tbar_G''(F_s(F_r(O))).
```

The first term, transported through the second OLD_FID isometry, handles
inherited new sectors; the second handles fresh sectors. This remains
local and support-indexed, not globally orthogonal.

On an actual common-refinement diamond, LOE6 separately requires the W1/W4
maps and local certificate terms to cohere. With that hypothesis, the
fixed local orthogonal projector is unique and the two composites agree.
The theorem does not infer geometry from a bare rail square.

| Diamond | Result |
|---|---|
| rank-preserving subdivision | `S=id`, no new local sector, `P=id`; **PASS / ADMITTED** |
| disjoint cycle creation | **CONDITIONAL PASS** on zero fidelity, orthogonal/leakage, support, and W4 defects |
| endpoint contact creation | **CONDITIONAL PASS** on OLD_FID, exclusive RNL, LR, and W4 |

```text
I1 = PASS
CERT = CONFIRMED
```

---

## 3. I2 - direct-sum model

Take

```text
K_G' = S_r K_G direct-sum N_r,
R_K,G' = S_(r,*) R_K,G direct-sum R_N,
Tbar_G' = P_r Tbar_G direct-sum Tbar_N,
Phi_G' = Phi_G direct-sum Phi_N,
E_r^geom(x,n) = (x,0).
```

The metric projector then equals `E_r^geom`; OLD_FID is exact; cross
support pairings vanish; and the test map is support-local. Identity bundle
pullbacks satisfy W4. Every displayed defect is zero, including the
corrected contact-exclusive family.

This proves the certificate class jointly consistent and model-inhabited.
It does not prove the actual retained DoR-019/Q-408 family contains that
member. The reviewed artifact preserves this distinction.

```text
I2 = PASS
DIRECT_SUM_MODEL = ADMITTED_COMPATIBILITY_TERM
JOINT_UNSATISFIABLE = false / TYPE-R
```

---

## 4. I3 - zero-defect section

### 4.1 Exact object

For each actual positive-source primitive `r`, let `Z_r` be the set of
actual W1/W4 members for which all four defect families, bundle equations,
and LOE6 vanish. The required object is not isolated nonemptiness. It is

```text
Gamma_cov(Z) != empty,
```

with restriction, composition, and every actual common-refinement square
coherent and with no basis, orientation, frame, filtration, or member
selected.

### 4.2 Why current content does not derive it

On `K=span(c_U,c_V)`, choose the positive form

```text
g_epsilon = [[1, epsilon], [conj(epsilon), 1]],
0 < |epsilon| < 1,
```

with actual disjoint U/V support and unchanged W1/W4 geometry. Then

```text
Def_leak,U = theta_U epsilon != 0,
E_U^orth(c_V) = conj(epsilon)c_U != 0
               = E_U^geom(c_V),
```

and the V leg fails conjugately. Covariance, reality, positivity, units,
and raw geometry can all remain valid. Therefore those authorities do not
force zero metric defects.

Independently, with diagonal metric a support-nonlocal analysis isomorphism
may send an old local test to a current with a new-region component. Then

```text
Def_orth = Def_leak = 0,
Def_supp != 0.
```

Thus relative orthogonality cannot derive LR. Together with the passing
direct-sum model, these countermodels show the current stack permits both
zero- and nonzero-defect realizations. Physical section nonemptiness is not
derived.

Covariance proves only

```text
x in Z_r implies U.x in Z_Ur.
```

It cannot prove that an `x` exists.

### 4.3 Constructible route

The section is **CONSTRUCTIBLE-WITH-ROUTE**:

1. Populate actual positive-source W1/W4 primitive orbits from the adopted
   where-laws, carrying real path/current, bundle, and support data.
2. Derive `E_r^geom` from each actual new-cell relation; reject any datum
   requiring a cycle-basis choice or deletion of visible current.
3. Compute all fixed-data defects using the DoR-019 metric and Q-408 `Phi`.
4. Retain complete covariance orbits of zero-defect candidates, never an
   isolated member.
5. Prove nonemptiness and restriction/composition closure.
6. Exhibit a nonempty common-refinement equalizer across all required
   diamonds. Separate leg witnesses do not suffice.

Equivalently, the missing physical theorem says the actual positive-source
refinement preserves the old Riesz form, is relatively orthogonal on every
active old/new pair, carries `Phi` support-locally, and does so coherently.

This is surface geometry. A clause merely asserting nonemptiness would be
a new physical adoption and would not itself be the proof-carrying witness
required by the strict `[EQ6]` regressions. No clause is authored here.

```text
I3 = NEEDS(CONSTRUCTIBLE_WITH_ROUTE:
           PHYSICAL_ZERO_DEFECT_NONEMPTINESS_AND_COHERENT_SECTION_THEOREM)
SECTION_EXHIBITED = false
```

### 4.4 Geometry versus rails

| Layer | Geometry | Rails |
|---|---|---|
| primitive | actual path/current support, bundle, coframe, density, connection, curvature | W1/W4 diagrams |
| excision | actual old/new split | `E_geom` idempotent/image equations |
| metric | fixed DoR-019 pairing | fidelity/orthogonal/leakage defects |
| locality | fixed Q-408 `Phi` and support | support quotient defect |
| all-rank | actual positive-source family | covariance/composition/equalizer conditions |

The rails can decide a candidate. They do not populate the geometric
fiber.

---

## 5. I4 - conditional cascade

Because no section is exhibited, the cascade cannot be executed
unconditionally. The proved implication is

```text
nonempty coherent physical Cert_LOE section
  -> both cycle-creating diamonds pass
  -> W1/W4 positive-source members close under composition/refinement
  -> the Q-408 root becomes all-rank on that category
  -> B_R1, C1, faithfulness, C2, and C3 may consume admitted arrows in
     dependency order
  -> one joint J1-J15 equalizer term remains required for [EQ6].
```

| Layer | Standing |
|---|---|
| certificate class and checker | **BUILT / CONFIRMED** |
| compatibility model | **BUILT / CONFIRMED** |
| rank-preserving boundary | **ADMITTED** |
| positive-source physical section | **TYPE-U / CONSTRUCTIBLE-WITH-ROUTE** |
| all-rank Q-408 family | **PARTIAL** |
| joint `[EQ6]` | **PARTIAL** |

```text
I4 = PASS_AS_CONDITIONAL
ALL_RANK = PARTIAL / TYPE-U
JOINT_EQ6 = PARTIAL / TYPE-U
```

---

## 6. I5 - regressions and fresh attacks

### 6.1 Regression ledger

| Regression | Result |
|---|---|
| abstract-kernel substitution | **PASS** - defects use actual `S`, `E_geom`, fixed `R_K`, fixed `Phi`, and support quotients |
| circular map | **PASS** - geometry precedes projector and defect construction |
| false nonemptiness | **PASS** - model term is separated from physical section |
| current deletion | **PASS** - no target current is removed from the carrier |
| covariance overclaim | **PASS** - invariance does not imply nonemptiness |
| all-stage overclaim | **PASS** - all-rank remains conditional |
| sector mixer | **PASS / REJECTED** - nonzero `zeta` is detected |
| `P=id` overreach | **PASS / ADMITTED** - unrelated old sectors are unconstrained |
| clause nonemptiness | **PASS** - clauses remain membership laws |

### 6.2 Too-easy test

The genuine new content is the explicit finite defect calculus and its
conditional composition law. Physical inhabitance did not become easier
by definition. The zero-source base and rank-preserving `N=0` control do
not populate a positive-source cycle-creating leg. No degenerate member is
counted.

### 6.3 Fresh attack 1 - invariant empty zero locus

Let covariance act transitively on a candidate orbit `X` and let an
equivariant defect have constant nonzero norm:

```text
||Def(U.x)|| = ||U Def(x) U^(-1)|| = d > 0.
```

The zero locus is invariant and empty. Every covariance proof survives,
but no section exists. Hence covariance cannot discharge inhabitance.

```text
FRESH_ATTACK_1 = PASS /
  COVARIANCE_PRESERVES_ZERO_LOCI_BUT_DOES_NOT_POPULATE_THEM
```

### 6.4 Fresh attack 2 - marginals are not an equalizer

Two legs may each have a nonempty zero-defect fiber while their transported
terms have disjoint target images:

```text
image_s(Z_r) intersect image_v(Z_u) = empty.
```

Every stage then has a passing candidate, but no common-refinement section
exists. The construction route must exhibit the joint intersection, not a
list of marginal witnesses.

```text
FRESH_ATTACK_2 = PASS /
  STAGEWISE_NONEMPTINESS_DOES_NOT_IMPLY_COHERENT_SECTION_NONEMPTINESS
```

### 6.5 Anti-tuning ledger

```text
1  Freeze actual W1/W4 and fixed DoR-019/Q-408 inputs.
2  Recompute the certificate and three diamond controls.
3  Admit the direct-sum term only as a consistency model.
4  Construct fixed-data countermodels before section classification.
5  State the nonempty equalizer as the exact physical need.
6  Do not inspect a response, threshold, fixed point, end test, alpha
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
