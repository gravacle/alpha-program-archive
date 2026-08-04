# STAGE 8 TASK 5 / EQ6 — ZERO-DEFECT SECTION BUILD — LANE 2 V001

Date: 2026-08-04  
Lane: Codex Lane 2  
Task: build the physical zero-defect section on the actual fixed DoR-019/Q-408 positive-source family

## Lead result

```text
SCOPE_CLAIMS =
  SC-1 DEFECT_RECOVERY:
    PROVEN_SUPPORTED at candidatewise fixed-data scope;
    no nonemptiness consequence retained;
  SC-2 COMPOSITION_AND_DIAMONDS:
    PROVEN_SUPPORTED only under actual W1/W4 coherence, LOE6, and
    zero-defect terms on every participating leg;
    the unconditional inherited/fresh-sector sentence is REMOVED

SECTION = STOPPED_AT(
  NONEMPTY_COMMON_REFINEMENT_EQUALIZER_OF_THE_ACTUAL_FIXED
  DOR019_Q408_POSITIVE_SOURCE_ZERO_DEFECT_LOCI;
  TYPE = CONSTRUCTIBLE_DEEPER / TYPE-U)

SECTION_DERIVABLE_FROM_CURRENT_STACK = false / TYPE-R
SECTION_DECLARABLE_AS_A_SUBSTITUTE_WITNESS = false
STRUCTURAL_IMPOSSIBILITY = false / TYPE-R
DIRECT_SUM_MODEL_IS_PHYSICAL_SECTION = false

DIAMONDS =
  rank-preserving subdivision: PASS / ADMITTED;
  disjoint cycle creation: CONDITIONAL_PASS / PHYSICAL TERMS OPEN;
  endpoint-contact cycle creation: CONDITIONAL_PASS / PHYSICAL TERMS OPEN

ALL_RANK = PARTIAL / TYPE-U
JOINT_EQ6 = PARTIAL / TYPE-U

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The physical section is not built. The failure is exact and constructive:
the actual path/current and bundle members exist at the minimal
positive-source diamonds, but the fixed DoR-019 metric and fixed Q-408
analysis map do not prove that those members lie in the zero loci. The
first rank-one-to-rank-two leg already requires a fixed-data old-image
isometry, vanishing old/new Riesz cross term, and support-local analysis
transport. None is supplied family-wide. Covariance cannot create a zero,
and stagewise candidates would not by themselves inhabit the
common-refinement equalizer.

The direct-sum construction remains an admitted consistency model. It
proves that the certificate equations are jointly satisfiable, so there is
no structural no-go. It is not a member of the fixed physical family and is
not used as one here.

---

## 0. Preflight, custody, and register sweep

### 0.1 Required preflight

```text
LOCKED_PROCESS = READ_IN_FULL
REGISTER_HEAD = Q-444
REGISTER_SEAL = OK
PREFLIGHT = PASS
```

The review of record was seal-verified before reading and then read in
full:

```text
STAGE8_TASK5_EQ6_CERT_CHECK_AND_ZERO_DEFECT_SECTION_LANE1_V001.md
SHA-256 = 1fdd8823f046822ae1a23546cf486c5aad7b1c2a438682d5d9313e897de0c56b
SEAL = OK
```

The quarantined self-check was also seal-verified before reconciliation:

```text
STAGE8_TASK5_EQ6_CERT_CHECK_LANE2_SELF_CHECK_QUARANTINE_V001.md
SHA-256 = c6593af60217e94f31baab0d5a6a2d595849ea4b73f598992215f3c19a0dc7a8
SEAL = OK
```

Load-bearing local mirrors were checked at their sealed hashes:

| Authority | SHA-256 | Use |
|---|---|---|
| carrier metric V005 / DoR-019 candidate | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | fixed finite Riesz form, full carrier, completion |
| Q-408 kernel realization | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | actual currents, analysis map, finite kernel/support calculus |
| adopted where-clause artifact | `19b2060392b6e04448c1c13416b87b67decf401246e3414a783b288fdb5d80ec` | W1/W4 membership laws |
| positive-source/all-rank attempt | `dec994976774bf598e79cd496f6b424d777d2321df2b41c0393219a3247c3ad6` | actual minimal positive-source diamonds and obstruction equations |
| pass-2 hostile check | `166002e9178faefe4464f504810553a606ec6465a0e3739a70e50a5d29d8604e` | all-rank need; no generic batching shortcut |
| local orthogonal excision certificate | `d61a550a33bf1215c35f4d6f27cd2ec5d644b93a05e16d08fe3d43ded3416817` | four fixed-data defects and conditional diamonds |

### 0.2 Register sweep

```text
Q-408  finite current/kernel realization, analysis maps, and supports;
Q-418  rank-preserving physical path subdivision has S=id and P=id;
Q-422  [EQ6] requires one joint witness, not marginal witnesses;
Q-427  actual surface geometry cannot be replaced by categorical rails;
Q-430  a fixed Riesz mixer may commute algebraically while leaking support;
Q-432  relative no-leakage replaces forbidden global orthogonality;
Q-438  W1/W4 are possibly-empty membership laws;
Q-439  the zero-source first-cycle member exists;
Q-440  positive-source all-rank members and actual diamonds remain open;
Q-441  both cycle-creating diamonds stop at fixed-data defects;
Q-442  joint inconsistency is refuted by a direct-sum model;
Q-443  Cert_LOE is built; physical section remains open;
Q-444  Cert_LOE is confirmed; the exact stop is the nonempty
       common-refinement equalizer of the actual physical zero loci.
```

No settled entry supplies a physical positive-source zero-defect member,
let alone a coherent section. No entry licenses changing the DoR-019
metric, changing the Q-408 analysis map, selecting a favorable refinement,
or declaring the direct-sum model physical.

---

## 1. J1 — reconciliation of the two quarantined scope claims

The authoritative Q-444 reading confirms the certificate after narrowing
two statements to the scope actually proved. This section installs those
narrowings before attempting inhabitance.

### 1.1 SC-1 — what the four defects recover

For an actual candidate refinement `r:G->G'`, with fixed current injection
`S_r`, actual geometric old-current projector `E_r^geom`, fixed DoR-019
Riesz maps, fixed Q-408 analysis maps `Phi`, and actual support maps, the
certificate defines

```text
Def_fid(r) = S_r^* R_K,G' S_r - R_K,G;

Def_orth(r;O,W)
  = E_r;O,W^geom - E_r;O,W^orth;

Def_leak(r;O,W)
  = i_W^* R_K,G' S_r Phi_G i_O;

P_r = Phi_G'^(-1) S_r Phi_G;
Def_supp(r;O) = q_G',F_r(O) P_r i_O.           (J1-1)
```

Candidatewise, their zero equations recover exactly

```text
Def_fid=0  <=> OLD_FID;
Def_orth=0 <=> actual local excision agrees with fixed-metric
                 orthogonal excision on the active local subspace;
Def_leak=0 <=> RNL on every active disjoint/contact-exclusive pair;
Def_supp=0 <=> LR on every actual old local region.              (J1-2)
```

This is the record review's supported reading. The word `recover` is
diagnostic and failure-capable: it says the zero equations are the required
tests. It does **not** imply that an actual physical candidate satisfying
them exists.

```text
SC-1 = PROVEN_SUPPORTED_PER_CANDIDATE
SC-1_NONEMPTY_ZERO_LOCUS_CONSEQUENCE = REMOVED
```

### 1.2 SC-2 — composition and common-refinement scope

For composable actual terms `r:G->G'` and `s:G'->G''`, the identities

```text
P_s P_r = P_sr;

Def_fid(sr)
  = S_r^* Def_fid(s) S_r + Def_fid(r)           (J1-3)
```

are exact. Successive LR inclusions also give

```text
P_sr(Tbar_G(O))
  subset Tbar_G''(F_s(F_r(O))).                 (J1-4)
```

The orthogonal/no-leakage part composes only after the actual terms on both
legs satisfy their zero defects and the W1/W4/LOE6 common-refinement data
cohere. Under those hypotheses, the first zero-defect term transported
through the second OLD_FID isometry handles the inherited new sector, the
second zero-defect term handles the fresh new sector, and uniqueness of the
fixed local orthogonal projector identifies the two diamond composites.

The quarantined broader sentence—read as saying that composition itself
creates inherited/fresh-sector orthogonality—is not used. It is removed.
The record-supported conditional theorem is retained.

```text
SC-2 = PROVEN_SUPPORTED_UNDER(
  ACTUAL_W1_W4_COHERENCE + LOE6 + ZERO_DEFECTS_ON_EVERY_LEG)
SC-2_UNCONDITIONAL_ORTHOGONALITY_CLAIM = REMOVED
```

### 1.3 Reconciliation board

| Scope claim | Q-444 disposition | Live statement in this build |
|---|---|---|
| four defects recover the physical requirements | supported | candidatewise equivalences `(J1-2)` only |
| composition closes the certificate | supported after recoverable scope repair | conditional on actual coherent zero-defect terms; no existence inference |

The two quarantined objections therefore do not kill `Cert_LOE`; neither is
allowed to populate the physical section.

---

## 2. J2 — attempted construction of the physical section

### 2.1 Actual family and fixed data

Let `I_pos` be the actual positive-source refinement category permitted by
the adopted W1/W4 where-laws. Its objects and arrows carry actual
incidence paths, conserved currents, local support maps, U(1) bundle lifts,
coframes, positive densities, connections, and curvatures. The laws are
membership laws and may have empty fibers.

For each actual primitive `r:G->G'`, let `X_r^phys` be the full no-selection
family of W1/W4 candidates with all bundle, covariance, reality, units, and
finite-restriction certificates. The metric and analysis data are not
coordinates of `X_r^phys` that may be adjusted; they are fixed inputs:

```text
g_K,G(c,d) = g_A4,G(u_c,u_d),
R_K,G:K_G -> K_G^*,
Phi_G = R_K,G^(-1) Abar_G.                     (J2-1)
```

Define the actual zero locus

```text
Z_r^phys := {
  x in X_r^phys :
  Def_fid(x)=0,
  Def_orth(x;O,W)=0 for every relevant local pair,
  Def_leak(x;O,W)=0 for every active disjoint/exclusive pair,
  Def_supp(x;O)=0 for every old local region,
  W1, W4, and LOE6 hold
}.                                             (J2-2)
```

This definition builds the locus as a failure-capable subfamily. It does
not prove that it is inhabited.

### 2.2 The required common-refinement equalizer

For every common-refinement diamond `d` and its two routes, let
`tau_d^L,tau_d^R` be the induced transports on actual certificate terms.
For every admitted covariance `U`, let `U_*` be the transported term. The
requested physical section is an element of

```text
Eq_phys := {
  (x_r)_r in product_(r in I_pos) Z_r^phys :
  tau_d^L(x)=tau_d^R(x) for every actual diamond d,
  x_(U r)=U_*x_r for every admitted covariance U,
  restriction and composition agree for every admitted arrow
}.                                             (J2-3)
```

The build target is

```text
Eq_phys != empty.                              (J2-4)
```

This formulation exposes both burdens:

1. `Z_r^phys != empty` for every required primitive orbit;
2. the transported stagewise terms have a nonempty joint equalizer.

Neither burden follows from covariance. Even a proof of every marginal
nonemptiness would leave `(J2-4)` open.

### 2.3 Rank-preserving control

On an admitted physical path subdivision, the cycle rank does not change
and the fixed maps satisfy

```text
S=id,
P=id,
R_K preserved by W3.                           (J2-5)
```

The path/current, bundle, connection, curvature, support, and finite-kernel
maps agree on the common subdivision. Hence all four defects vanish and
the subdivision term belongs to the relevant zero locus.

```text
Z_subdivision^phys != empty / TYPE-P
D_SUBDIVISION = PASS / ADMITTED
```

This control cannot create a positive-source cycle-rank-increasing member.

### 2.4 First positive-source test: disjoint cycle creation

Use the actual surface diamond with disjoint corridors `U,V` and target
cycles `c_U,c_V`:

```text
K_GU = span{c_U},
K_GV = span{c_V},
K_GUV = span{c_U,c_V},
Supp(c_U) subset U,
Supp(c_V) subset V,
closure(U) intersect closure(V)=empty.          (J2-6)
```

The adopted laws supply actual W1 path/current candidates and W4 bundle
candidates on both positive-source legs. On the fixed metric write

```text
g_K,GU(c_U,c_U)=alpha_0 > 0,
g_K,GV(c_V,c_V)=delta_0 > 0,

[g_K,GUV]_(c_U,c_V)
  = [[alpha,zeta],[conj(zeta),delta]],
alpha>0,
delta>0,
alpha*delta-|zeta|^2>0.                        (J2-7)
```

For the two legs, zero fidelity requires

```text
alpha=alpha_0,
delta=delta_0.                                 (J2-8)
```

W3 does not prove `(J2-8)` because these legs increase cycle rank. On the
favorable fidelity slice, choose an actual source-local test with

```text
Phi_GU(a_U)=theta_U c_U,
theta_U != 0.                                  (J2-9)
```

The fixed-data no-leakage defect is

```text
Def_leak(r_UV;U,V)
  = theta_U zeta.                              (J2-10)
```

The opposite leg gives the conjugate. Therefore the disjoint physical
zero locus requires

```text
zeta=0.                                       (J2-11)
```

DoR-019 positivity, units, covariance, and reality do not force
`(J2-11)`. The live positive form

```text
[[1,epsilon],[conj(epsilon),1]],
0<|epsilon|<1                                 (J2-12)
```

passes those carrier axioms while failing `(J2-11)`. This is a
non-derivability witness, not a choice for the physical metric.

Even if `(J2-8)` and `(J2-11)` are granted, the fixed Q-408 analysis map
must additionally satisfy

```text
Phi_GUV^(-1) S_UV Phi_GU(Tbar_GU(O))
  subset Tbar_GUV(F_UV(O))                     (J2-13)
```

and its symmetric counterpart. No adopted or ratified family theorem
proves `(J2-13)`. A diagonal Riesz form therefore would not by itself
inhabit the zero locus.

```text
Z_disjoint_positive^phys_NONEMPTY = UNPROVED / TYPE-U
D_DISJOINT = CONDITIONAL_PASS_ON(
  OLD_FID + LOCAL_ORTHOGONAL_EXCISION + RNL + LR + W4 + LOE6)
```

### 2.5 Second positive-source test: endpoint-contact creation

For the actual contact diamond, the old and new corridors meet only at the
recorded endpoint `q`. Removing that contact locus leaves the exclusive
old/new test pairs. The physical conditions are

```text
OLD_FID;
Def_leak=0 on every exclusive-region pair;
Def_supp=0 on every old local region;
W4 and LOE6.                                   (J2-14)
```

Contact can silence RNL only for supports that actually meet. It does not
remove the exclusive-region family, and it cannot prove LR on the
exclusive segment of the new path. Thus the contact locus remains open on
fixed physical data.

```text
Z_contact_positive^phys_NONEMPTY = UNPROVED / TYPE-U
D_CONTACT = CONDITIONAL_PASS_ON(
  OLD_FID + EXCLUSIVE_REGION_RNL + LR + W4 + LOE6)
```

### 2.6 Why the direct-sum model does not build `(J2-4)`

The admitted compatibility model takes

```text
K_G' = S_r K_G direct-sum N_r,
R_K,G' = S_(r,*) R_K,G direct-sum R_N,
Phi_G' = Phi_G direct-sum Phi_N,
E_r^geom(x,n)=(x,0).                           (J2-15)
```

It has zero defects and admits the corrected contact tests. But `(J2-15)`
authors a block decomposition of the target metric and analysis map. The
actual target already carries the fixed DoR-019 form and Q-408 analysis
map. Substituting `(J2-15)` would replace the tested physical data with a
rail-compliant stand-in, exactly the forbidden abstract-kernel/direct-sum
laundering.

```text
DIRECT_SUM_MODEL_ADMITTED = true / TYPE-P
DIRECT_SUM_MODEL_IN_Eq_phys = NOT_PROVEN
DIRECT_SUM_MODEL_USED_AS_SECTION = false
```

### 2.7 Exact stopping point and its type

The section construction stops before the first required positive-source
stage is inhabited. The exact missing object is

```text
PHYSICAL_ZERO_DEFECT_EQUALIZER_WITNESS :=
  a family (x_r)_r on the actual fixed DoR-019/Q-408 positive-source
  refinement category such that

  A. every required rank-one-to-rank-two primitive has an actual W1/W4
     member satisfying OLD_FID, local orthogonal excision, active RNL,
     LR, and all bundle certificates;
  B. the fixed, not modified, R_K and Phi are used;
  C. complete covariance orbits are retained without a member choice;
  D. restriction and composition close;
  E. every actual common-refinement equalizer is nonempty.             (J2-16)
```

Its earliest finite interface is a physical rank-one-to-rank-two member
proving, on the fixed data,

```text
S_r^* R_K,G' S_r = R_K,G,
i_W^* R_K,G' S_r Phi_G i_O = 0,
q_G',F_r(O) Phi_G'^(-1) S_r Phi_G i_O = 0       (J2-17)
```

for all active local pairs/regions, with the actual bundle term attached.
Its global interface is the nonempty equalizer `(J2-3)`.

The type is exact:

```text
TYPE = CONSTRUCTIBLE_DEEPER / TYPE-U
```

Reasons:

- **not derivable:** fixed-data mixer and support-spill countermodels obey
  the current ratified/adopted laws but have nonzero defects;
- **not structurally impossible:** the direct-sum model proves joint
  consistency;
- **not discharged by declaration:** the adopted where-laws are already
  law-only, and a new nonemptiness axiom would not itself be the actual
  proof-carrying member required by `[EQ6]`;
- **constructible deeper:** actual positive-source surface members can be
  tested by the complete certificate; what remains is to exhibit a member
  and prove its common-refinement coherence on the fixed data.

```text
SECTION = STOPPED_AT(PHYSICAL_ZERO_DEFECT_EQUALIZER_WITNESS)
SECTION_TYPE = CONSTRUCTIBLE_DEEPER / TYPE-U
MACHINERY_APPEAL = false
```

---

## 3. J3 — diamonds, all-rank family, cascade, and `[EQ6]`

Because `(J2-4)` is not inhabited, no unconditional cascade is executed.
The proved conditional chain is

```text
PHYSICAL_ZERO_DEFECT_EQUALIZER_WITNESS
  -> both cycle-creating diamonds pass unconditionally on its terms
  -> the W1/W4 positive-source family closes under composition and
     common refinement
  -> the Q-408 refinement root becomes all-rank on that category
  -> B_R1 naturality consumes the admitted arrows
  -> C1 completion and completed faithfulness consume the all-rank root
  -> B_C2 response-boundary naturality consumes the same arrows
  -> C3 may enter the joint J1-J15 equalizer
  -> one joint `[EQ6]` term must still be exhibited.                (J3-1)
```

The current board is

| Layer | State after this build |
|---|---|
| `Cert_LOE` and fixed-data checker | **BUILT / CONFIRMED / TYPE-P** |
| direct-sum compatibility model | **ADMITTED / TYPE-P / NOT PHYSICAL** |
| rank-preserving subdivision section | **INHABITED / TYPE-P** |
| positive-source physical zero locus | **NONEMPTY UNPROVED / TYPE-U** |
| common-refinement physical equalizer | **NOT INHABITED / TYPE-U** |
| disjoint cycle-creating diamond | **CONDITIONAL PASS** |
| endpoint-contact cycle-creating diamond | **CONDITIONAL PASS** |
| all-rank Q-408 physical family | **PARTIAL / TYPE-U** |
| joint `[EQ6]` | **PARTIAL / TYPE-U** |

The cascade does not use raw W1/W4 candidates as response-natural arrows.
It starts only after the physical section is exhibited.

---

## 4. J4 — falsifiers, regressions, and anti-tuning

### 4.1 The nine standing regressions

| Regression | Exercise on this build | Result |
|---|---|---|
| abstract-kernel substitution | all defects use actual `S`, actual `E_geom`, fixed `R_K`, fixed `Phi`, and actual support quotients | **PASS** |
| circular map | actual surface/bundle data precede `E_orth`, `P`, and the defects | **PASS** |
| false nonemptiness | defining `Z_r^phys` is not treated as proving `Z_r^phys!=empty` | **PASS** |
| cycle-current deletion | no target cycle/current is removed to make a defect vanish | **PASS** |
| covariance-orbit overclaim | covariance carries a zero if one exists; it is not used to produce one | **PASS** |
| all-stage overclaim | all-rank remains partial at the first positive-source rank increase | **PASS** |
| sector mixer | `(J2-12)` fails `Def_orth/Def_leak` and is rejected | **PASS** |
| `P=id` overreach | rank-preserving subdivision is admitted; `P=id` is not extended to cycle creation | **PASS** |
| clause nonemptiness | W1/W4 remain possibly-empty membership laws | **PASS** |

### 4.2 Cycle-creating and equalizer falsifiers

#### F1 — fixed-data Riesz mixer

For `0<|epsilon|<1`, `(J2-12)` preserves positivity, covariance class,
reality, and units but has

```text
Def_leak,U = theta_U epsilon != 0,
E_U^orth(c_V)=conj(epsilon)c_U != E_U^geom(c_V). (J4-1)
```

It is excluded from the zero locus. This proves the section is not forced
by carrier axioms.

#### F2 — support spill with diagonal metric

Let the metric be diagonal but let the fixed analysis isomorphism send an
old local test to a current with a component in the new exclusive region.
Then

```text
Def_orth=Def_leak=0,
Def_supp!=0.                                    (J4-2)
```

This proves that metric orthogonality alone cannot construct the section.

#### F3 — empty covariant zero locus

An equivariant defect may have constant positive norm on a transitive
actual candidate orbit:

```text
||Def(Ux)||=||U Def(x) U^(-1)||=d>0.            (J4-3)
```

The empty zero locus is covariant. Thus covariance does not prove
stagewise nonemptiness.

#### F4 — stagewise terms with empty equalizer

Even if two legs have nonempty zero loci, their images at a common
refinement may be disjoint:

```text
tau_d^L(Z_r^phys) intersect tau_d^R(Z_s^phys)
  = empty.                                      (J4-4)
```

This is why a list of stagewise witnesses would not satisfy `(J2-4)`.

#### F5 — outer-zero laundering

The outer composites from the rank-zero base both vanish. That equality
does not certify either positive-source side, whose defects are
`(J2-8)`–`(J2-13)`. The outer `0=0` is rejected as an inhabitance proof.

#### F6 — direct-sum laundering

Replacing the fixed target form/analysis map by `(J2-15)` would make the
tests pass by changing the object tested. The compatibility model remains
outside the physical equalizer unless actual fixed-data membership is
separately proved.

### 4.3 Fresh attack — zero-defect projection is not a lawful repair

One could attempt to project a physical candidate onto the kernel of all
four defects. This fails for three independent reasons:

1. the defect families have different codomains and no ratified common
   orthogonal projection;
2. projecting the metric or `Phi` changes the fixed DoR-019/Q-408 inputs;
3. projecting the member can delete record-visible cycle or support data.

Therefore `ker(Def)` is a membership test, not a repair operator.

```text
FRESH_ATTACK = PASS /
  NO_RATIFIED_ZERO_DEFECT_RETRACTION_ON_THE_ACTUAL_PHYSICAL_FAMILY
```

### 4.4 Anti-tuning ledger

```text
1  Freeze DoR-019 R_K and Q-408 Phi/support before constructing candidates.
2  Take actual W1/W4 path/current and bundle data from the adopted laws.
3  Define the four failure-capable defects without changing any input.
4  Run rank-preserving, disjoint, and contact minimal stages.
5  Attempt stagewise physical zero-locus inhabitance before the equalizer.
6  Refuse the direct-sum model as a physical substitute.
7  Type the exact equalizer witness only after the finite stops are found.
8  Inspect no response, fixed point, end test, alpha consequence, numeric
   value, or measured constant.
```

No member, rank, ratio, orientation, frame, cycle basis, gauge lift,
filtration, metric, analysis map, support map, reader, or completion was
selected. No response-facing consequence was used to define a candidate.

---

## 5. Final board

```text
SCOPE_CLAIMS =
  SC-1 candidatewise defect recovery: SUPPORTED;
  SC-1 nonemptiness inference: REMOVED;
  SC-2 composition under coherent zero-defect actual terms: SUPPORTED;
  SC-2 unconditional inherited/fresh orthogonality: REMOVED

CERT_LOE = CONFIRMED / TYPE-P
CERTIFICATE_IS_RAILS = true

SECTION = STOPPED_AT(
  PHYSICAL_ZERO_DEFECT_EQUALIZER_WITNESS_ON_THE_ACTUAL_FIXED
  DOR019_Q408_POSITIVE_SOURCE_FAMILY)
SECTION_TYPE = CONSTRUCTIBLE_DEEPER / TYPE-U
SECTION_DERIVABLE = false / TYPE-R
SECTION_DECLARED = false

DIRECT_SUM_MODEL = ADMITTED_COMPATIBILITY_TERM / TYPE-P
DIRECT_SUM_MODEL_IS_PHYSICAL = false
STRUCTURAL_IMPOSSIBILITY = false / TYPE-R

D_SUBDIVISION = PASS / ADMITTED
D_DISJOINT = CONDITIONAL_PASS / PHYSICAL_ZERO_TERMS_OPEN
D_CONTACT = CONDITIONAL_PASS / PHYSICAL_ZERO_TERMS_OPEN
D_CONTACT_REQUIREMENTS = OLD_FID + EXCLUSIVE_REGION_RNL + LR + W4 + LOE6

ALL_RANK = PARTIAL / TYPE-U
JOINT_EQ6 = PARTIAL / TYPE-U

MEMBER_BINDING = false
FIXED_POINT_EXECUTION = false
END_TEST = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = false
MACHINERY_APPEAL = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
