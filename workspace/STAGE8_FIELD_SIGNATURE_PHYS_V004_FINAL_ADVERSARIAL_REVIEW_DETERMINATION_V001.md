# FINAL ADVERSARIAL REVIEW OF FIELD_SIGNATURE_PHYS V004

**Verdict:** `DEAD`

**DoR-015 package:** not issued.

**Register head at start and final pre-write check:** Q-296, current register
SHA-256 `b20597dc799280bc4654cb08bca67813dfc90cd211c3da1bd810b41f13277758`.

```text
alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 1. Lead finding

V004's frame-tangent determination is refuted. The endpoint-frame mutation
used as its record-visible witness changes a raw framed coordinate `H_N`, but
V003's own S3 seam already maps that mutation to the derived Gate-4 vertex
rephasing action. Gate 4 identifies the two edge assignments: tree phases are
removable and loop holonomy is the surviving physical datum.

The smallest counterexample is V004's own one-edge witness. On a single
oriented edge `e:s->t`, hold `A` fixed and set

```text
p_t(epsilon)=p_t exp(-i epsilon),
p_s(epsilon)=p_s.
```

Then

```text
h_e(epsilon)=exp(i epsilon)h_e(0).
```

V004 concludes that the change is record-visible because the raw coordinate
changes. Gate 4 applies the vertex rephasing

```text
g_t=exp(i epsilon),
g_s=1,
U_e -> g_t U_e g_s^(-1),
```

and puts the two edge assignments in the same differential equivalence class.
On the one-edge tree there is no loop holonomy for the mutation to change.
The proposed witness therefore distinguishes representatives, not physical
Gate-4 classes.

This is not the unbuilt smooth PRPS-to-Gate-4 exhaustion theorem. It is the
finite map already present inside the proposal:

```text
T_iota,p(U_e)=h_e(A,p),
T_iota,p(g_t U_e g_s^(-1))
  =g_t h_e(A,p) g_s^(-1).
```

That equation is V003 S3 (`STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V003.md:702-719`).
V004 inherits V003 S3 and the complete finite frame family. The missing
smooth functor cannot be used to erase a finite intertwiner the proposal
already supplies.

```text
V004_FRAME_TANGENT_DETERMINATION_HOLDS = false | TYPE-R |
  test: the one-edge fixed-A frame mutation changes H_e but is exactly a
        Gate-4 vertex rephasing on a tree, hence changes no physical holonomy

RAW_FRAMED_H_N_IS_GATE4_GAUGE_INVARIANT = false | TYPE-R |
  test: H_e -> g_t H_e g_s^(-1) under the inherited vertex action

V004_FINITE_ENDPOINT_FRAME_TO_GATE4_MAP_IS_UNBUILT = false | TYPE-R |
  test: V003 S3 explicitly defines the equivariant finite map T_iota,p on the
        same realized vertices and edges used by V004

FRAME_TANGENT_ROUTE_DERIVED_AS_RECORD_VISIBLE = false | TYPE-R |
  test: the derivation tests a gauge-covariant coordinate before taking the
        derived Gate-4 equivalence class
```

The central V004 repair therefore fails. This is load-bearing: A4, A5, A6,
S5, and the physical applications of Doors A through C use the resulting
over-fine source carrier. V004 cannot be ratified as written.

---

## 2. Authorities and scope

### 2.1 Frozen authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V004.md` | `5a8d5598716e26eabdc90a58e8e61acf7021a2a03129b60875d5bd265bd741e6` | object under review |
| `STAGE8_FIELD_SIGNATURE_PHYS_V003_FINAL_ADVERSARIAL_REVIEW_DETERMINATION_V001.md` | `6e191e562988180f4a7051ca3601d051cce7bcc7689d9f68cfd1afeffe3274f4` | Q-294 repair order and counterexample |
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V003.md` | `a5a8420da4878f735553b1cc7870d2e722b0bb039328621070bcb29fc066aaa2` | inherited framed carrier, S3, and endpoint intertwiner |
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V002.md` | `deaa86ee58edb9f841ae3f7bae8ccf9b1cf659328b99fb60cd290a348641e1ad` | six-field baseline and original Gate-4 seam |
| `STAGE8_FIELD_SIGNATURE_PHYS_V002_ADVERSARIAL_REVIEW_DETERMINATION_V001.md` | `d11c0ffd6b24876ce8da7821fd733c326b41095e8b4a7d3a1e831a19a906641b` | S3 type correction and repair boundary |
| `STAGE8_TASK4A_RECORD_SURFACE_TO_PHYSICAL_FIELD_SIGNATURE_DERIVATION_AND_BETA_GAP_ATTACK_V001.md` | `65e4dd6a6e2926c9c100edb162f57352311e73438f23dd19509dda0403e2e4f6` | derived-versus-authored split |
| `STAGE8_TASK4A_P5_MAXIMAL_TRANSPORT_CHAIN_AND_DEPENDENCE_ACCOUNTING_PACKAGE_V002.md` | `31a738ec17696ea01e1cb6a6ee7a37a29e6c0ca24d6fb8cc050d06aed32a583f` | Q-288 door schema |
| `32_GATE4_DIFFERENTIAL_UNIQUENESS_RESULT_V001.md` | `a0d8b3f71632bd56cc3646fa59e84a2c2776539fadf04be733c7a1eaa997bdbb` | derived vertex-gauge equivalence and loop-holonomy invariant |
| `STAGE8_PRPS_GATE4_LOCALIZATION_BRIDGE_ATTEMPT_V001.md` | `f651817ffbfd52caa57be7e63437e2e0682f421c911611151389df8f14579cf7` | scope of the missing smooth exhaustion theorem |
| `STAGE8_TARGET_INDEPENDENT_LOCALIZATION_THEOREM_BUILD_RESULT_V001.md` | `448840fbd74aab5df22a51aaecef1731372e96ce414eef8cc22f1a5b198d27bb` | independent confirmation that the smooth theorem is unbuilt |
| `STAGE8_CANONICAL_PATCH_COVER_TO_INCIDENCE_GRAPH_FUNCTOR_ATTEMPT_V001.md` | `f600362c64fe47ee3986b89765a1f631cc74d87873d9a29384377836c8eccad1` | failed smooth-cover realization route |
| `STAGE8_TASK4A_P3_LAW_SIDE_SUBPACKAGE_CROSS_VERIFICATION_DETERMINATION_V001.md` | `aaff995613e60fdf792473dcb8d3ffefcc2390428f4e6aa21ea9fef12ec97e27` | Q-295 later ruling, checked and non-bearing |

### 2.2 Roots and search

```text
ROOTS_ENTERED = (
  /Users/bgm/Documents/New project,
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
    alpha_fundamental_record_action_cleanroom_v003,
  /Users/bgm/MB Work/alpha-program-archive/cleanroom_output,
  /Users/bgm/MB Work/alpha-program-archive/workspace,
  /Users/bgm/MB Work/alpha_supervision
)

EXCLUSIONS = (
  a32_holdout/custodian_private,
  every response/value/root/rank-member/background-member evaluation,
  every measure/contour/boundary/domain construction,
  every register/plan/tracker/git/commit/push act
)

IDENTIFYING_FUNCTOR_QUERY = word-boundaried, case-insensitive search for (
  endpoint-frame-to-vertex-gauge,
  smooth relative-frame changes are exhausted,
  relative-frame changes ... exhausted,
  identifying functor,
  Gate-4 ... endpoint comparison frame
)
```

The search found three negative smooth-bridge artifacts and V004's repetition
of their negative. It found no later sealed theorem completing the smooth
PRPS/Gate-4 exhaustion. It also found the finite S3 map inside V003, which is
the map relevant to V004's actual finite `Fr_N` variables.

```text
FULL_SMOOTH_ENDPOINT_FRAME_EXHAUSTION_THEOREM_FOUND = false | TYPE-S |
  roots: all five roots listed above |
  exclusions: the fenced path and non-Markdown sidecars |
  fences: no response or value computation |
  query: IDENTIFYING_FUNCTOR_QUERY above

LATER_BEARING_RULING_FOUND = false | TYPE-S |
  roots: alpha_supervision register through Q-296 |
  exclusions: no unregistered draft |
  fences: no register edit |
  query: Q-297; DoR-015; supersession of Q-296 or Gate-4 gauge
```

Q-295 concerns the law-side subpackage and does not bear on the field-frame
equivalence. Q-296 is the registered V004 proposal under review.

### 2.3 Declared mathematics

This review uses only the following mathematics beyond the sealed equations:

1. the incidence coboundary on a finite directed graph;
2. differentiation of a U(1)-valued coordinate;
3. a differential form descends through a quotient only if it annihilates
   vertical tangent directions; and
4. an inverse-limit family is determined by all of its coordinate projections.

Each applies because V004 itself declares the corresponding finite graph,
U(1) coordinates, quotient, and inverse limit.

---

## 3. Z1: exact gauge and non-gauge split

Let `G_N=(V_N,E_N)` be any admitted finite write graph. Orient every edge
`e:s->t` and define the incidence coboundary

```text
(B theta)_e=theta_t-theta_s.
```

Let `L` send a connection tangent `a` to its realized path integrals:

```text
(L a)_e=integral_(gamma_e) a.
```

V004's framed coordinate has differential

```text
dH_N(a,theta)=i diag(H_N)(L a+B theta).
```

Because every component of `H_N` lies in U(1), `diag(H_N)` is invertible.
Thus the raw-coordinate kernel is exactly

```text
ker(dH_N)=ker(L+B).
```

This proves V004's algebraic separation statement on its own raw-coordinate
quotient. It does not prove physical separation after Gate-4 gauge.

### 3.1 Pure frame directions

For `a=0`, every frame tangent gives `B theta`. V003 S3 sends the finite frame
change to the same vertex-rephasing action as Gate 4. Therefore:

* `B theta=0` means a componentwise constant frame change. It is already a
  stabilizer of every edge coordinate.
* `B theta!=0` changes individual edge representatives but remains a Gate-4
  gauge direction.
* around every directed cycle `c`,

```text
sum_(e in c) (B theta)_e=0,
```

so pure frame changes alter no loop holonomy.

The complete finite `Fr_N` family contains endpoint-fiber points only at the
realized vertices. Any two tuples are related, vertex by vertex, by unique
torsor elements `g_v`. Hence the finite frame family is exhausted by the
finite vertex action without any patch cover, smooth extension, or global
section. The unbuilt smooth theorem concerns a larger object and does not
block this finite conclusion.

```text
PURE_FINITE_FRAME_TANGENT_HAS_NON_GAUGE_GATE4_COMPONENT = false | TYPE-R |
  test: every finite frame pair differs by a vertex tuple (g_v), and all cycle
        sums of B theta vanish

V004_ONE_EDGE_FRAME_WITNESS_CHANGES_PHYSICAL_HOLONOMY = false | TYPE-R |
  test: the admitted graph is a tree and Gate 4 removes its sole edge phase
```

### 3.2 Connection and mixed directions

The Gate-4 physical tangent carried by the edge phases is the class of

```text
L a+B theta
```

modulo `im(B)`. Therefore its class is the class of `L a`; the frame term
drops. On a graph with cycles, non-gauge content is represented by cycle
holonomy variations. On a tree, the phase tangent has no non-gauge content.

Mixed pairs satisfying `L a=-B theta` are raw-`H` null and are also physical
null. Connection tangents with nonzero cycle class survive. The clean split is
therefore:

```text
finite endpoint-frame coboundaries  -> Gate-4 gauge;
connection cycle-holonomy class     -> Gate-4 physical;
full smooth PRPS/Ward exhaustion    -> still TYPE-U outside this finite claim.
```

V004 instead retains `B theta` in the physical source and quotients only by
`ker(L+B)`. That quotient is too fine: it identifies equal coordinates, not
gauge-equivalent coordinates.

```text
V004_VISIBILITY_QUOTIENT_MATCHES_GATE4_PHYSICAL_QUOTIENT = false | TYPE-R |
  test: the one-edge pair has unequal H_e values but equal Gate-4 class

V004_GAUGE_NON_GAUGE_SPLIT_IS_CLEAN = false | TYPE-R |
  test: all nonconstant B theta directions are retained although they lie in
        the inherited vertex-gauge orbit

RECORD_VISIBLE_CONNECTION_WITNESS_SURVIVES_GATE4 = true |
  condition: its cycle-holonomy class in coker(B) is nonzero
```

Z1 fails.

---

## 4. Z2: the augmented current does not descend

V004 defines

```text
u_e^aug(a,theta)=(L a)_e+(B theta)_e
                =-i h_e^(-1) d h_e.
```

The equality is correct on the full framed presentation. The problem is its
claimed physical domain.

A covector on a quotient must annihilate tangent vectors to the quotient
orbit. Take the Gate-4 vertical tangent `(a,theta)=(0,theta)`. Then

```text
u_e^aug(0,theta)=(B theta)_e,
```

which is nonzero for the Q-294/V004 endpoint mutation. Therefore `u_aug` is
not basic for the inherited Gate-4 quotient and cannot be the physical source
covector V004 claims.

The same observation applies to the local phase:

```text
phi_e=-i Log_0(h_e h_e,0^(-1)).
```

Its displayed differential is correct upstairs, but `phi_e` is a
frame-dependent edge coordinate. A cycle phase is invariant because all
endpoint terms telescope. V004 does not replace its edge phase by that
quotient-invariant object.

```text
U_AUG_DESCENDS_TO_INHERITED_GATE4_QUOTIENT = false | TYPE-R |
  test: u_e^aug(0,theta)=theta_t-theta_s is nonzero on a vertical vertex-gauge
        tangent

PHI_E_IS_A_PHYSICAL_GATE4_SCALAR = false | TYPE-R |
  test: phi_e shifts under endpoint vertex rephasing while cycle sums do not

A4_PHYSICAL_SEPARATION_RERUN_PASSES = false | TYPE-R |
  test: its domain retains gauge directions and its proposed covectors do not
        descend through the inherited physical equivalence

A5_PHYSICAL_DIFFERENTIAL_RERUN_PASSES = false | TYPE-R |
  test: d phi_e=u_e^aug holds only on the over-fine framed presentation

A6_PHYSICAL_SOURCE_DOMAIN_RERUN_PASSES = false | TYPE-R |
  test: A6 completes a source span containing the non-descending B theta sector
```

The algebraic identity and the physical quotient claim must not be conflated:

```text
D_PHI_EQUALS_U_AUG_UPSTAIRS = true | PROPOSAL-CONDITIONAL MATHEMATICS
U_AUG_IS_PHYSICAL_DOWNSTAIRS = false | TYPE-R |
  test: the vertical-tangent test above
```

Z2 fails.

---

## 5. Z3: Door F survives as a projective theorem

Door F is independently valid on the family V004 declares. It forms

```text
X_inf^fr={(x_N)_N:r_MN(x_M)=x_N}
```

as an equalizer inside the product and uses the product-subspace/projective
topology. If two compatible families have identical finite projections, they
are equal componentwise. In V004's stated separated-family sense,

```text
intersection_N ker(pi_N)={0}.
```

No weak-star, bidual, distributional, or nonseparating operation is hidden in
that construction. Given an A2 member and one finite frame tuple, retaining
the same global connection and choosing points in later nonempty principal
fibers gives a compatible extension. This establishes the stated conditional
projection surjectivity without selecting a distinguished section.

The Q-288 block is complete: it states the input and output classes,
topologies, restrictions, formation operation, every limit and its topology,
all four dangerous-operation flags, tail image, separation, restriction
square, Q-279 status, provenance, target independence, and verdict.

```text
DOOR_F_PROJECTIVE_EQUALIZER_WELL_DEFINED = true |
  PROPOSAL-CONDITIONAL MATHEMATICS
DOOR_F_COMMON_FINITE_PROJECTION_TAIL = {0} |
  PROPOSAL-CONDITIONAL MATHEMATICS
DOOR_F_Q288_ROW_COMPLETE = true | MECHANICAL_AUDIT
DOOR_F_INVOKES_FORBIDDEN_CLASS_FORMATION = false | TYPE-S |
  roots: V004 Door F fields and Q-288 mandatory schema |
  exclusions: TYPE-U future raw-G operations |
  fences: no physical image construction |
  query: weak-star; bidual; distributional; nonseparating; unnamed topology
```

Door F's theorem does not rescue V004's physical carrier. It faithfully
assembles the over-fine finite classes it is given.

```text
DOOR_F_ASSEMBLES_A_GATE4_PHYSICAL_CARRIER = false | TYPE-R |
  test: each finite X_N retains vertex-rephased representatives distinguished
        by raw H_N, so their inverse limit retains the same over-fine relation
```

Z3 passes mathematically and fails as a discharger of the physical proposal.

---

## 6. Z4: bounded reruns and doors

### 6.1 Rerun matrix

| Q-294 rerun | Independent result | Reason |
|---|---|---|
| A4 separation | `TYPE-R` physically | algebraically separates `T/(ker dH)` but includes Gate-4 vertical directions |
| A5 phase differential | algebraic pass, physical `TYPE-R` | exact upstairs; edge phase is not quotient-invariant |
| A6 source domain | `TYPE-R` physically | completes the non-descending augmented source span |
| S5 | `TYPE-R` physically | finite labels reach gauge-covariant edge currents, not the Gate-4 quotient source |
| S6 | conditional algebraic pass | zero-extension preserves old `B theta` and `L a` components; it does not cure the quotient error |
| Door B | zero-tail pass on declared span; physical input `TYPE-R` | norm completion is sound but starts from the wrong physical source class |
| Door C | zero-tail pass on declared span; physical input `TYPE-R` | trace-norm completion is sound but inherits Door B's carrier |
| Door A | `TYPE-R` as physical pullback | arbitrary `f(H_N)` need not be vertex-gauge invariant |
| choice table | mechanical pass | augmented-source choice is disclosed, but its derived justification is refuted |
| class-formation scan | pass | D0/F/V/A/B/C/D are all declared |

```text
S5_PHYSICAL_SOURCE_KERNEL_RERUN_PASSES = false | TYPE-R |
  test: u_aug is nonzero on the finite Gate-4 vertical tangent

DOOR_A_PHYSICAL_PULLBACK_DESCENDS = false | TYPE-R |
  test: choose a non-invariant cylinder f on a one-edge tree; f(H_e) changes
        between Gate-4-equivalent frame tuples

DOORS_B_C_ZERO_TAIL_PROOFS_HOLD_ON_DECLARED_CLASSES = true |
  PROPOSAL-CONDITIONAL MATHEMATICS

DOORS_B_C_DISCHARGE_PHYSICAL_SOURCE_APPLICATION = false | TYPE-R |
  test: both complete the A4/A6 class whose Gate-4 descent fails
```

### 6.2 Door V

Door V quotients by equality of every raw finite `H_N`. Gate-4 equivalence is
strictly coarser on any graph with a nontrivial vertex action. The one-edge
counterexample is again minimal:

```text
H_e(x)!=H_e(y),
[H_e(x)]_Gate4=[H_e(y)]_Gate4.
```

Thus Door V is separated relative to its own coordinates but is not the
inherited physical gauge quotient.

```text
DOOR_V_SET_QUOTIENT_IS_SEPARATED = true |
  PROPOSAL-CONDITIONAL MATHEMATICS

DOOR_V_EQUALS_DERIVED_GATE4_QUOTIENT = false | TYPE-R |
  test: one-edge vertex-rephasing pair above
```

### 6.3 Door D

V004 correctly leaves the physical raw-G image open. The final review does
not turn that open item into a failure and does not execute it.

```text
DOOR_D_PHYSICAL_IMAGE = NO_VERDICT |
  prerequisite: a lawful physical source quotient, scalar functional,
                derivatives, connected subtraction, raw-G lift,
                restrictions, and common-origin certificate
```

---

## 7. Z5: full regression

### 7.1 Seven seams

| Seam | Final V004 review |
|---|---|
| S1 orientation/causal path | conditional pass; unchanged |
| S2 incidence/support | conditional pass; unchanged |
| S3 framed transport | its equivariance equation is valid and supplies the killing finite identification |
| S4 CTP reality | conditional pass; unchanged |
| S5 source kernel | refuted physically by the vertical-tangent test |
| S6 zero-extension | conditional algebraic pass on the declared span |
| S7 `T_cyl` pullback | bounded family map exists; physical Gate-4 descent fails for non-invariant cylinders |

```text
SEVEN_SEAMS_V004_PASS_AS_PHYSICAL_AGGREGATE = false | TYPE-R |
  test: S5 and the physical application of S7 fail the inherited gauge quotient
```

### 7.2 Six-count and provenance

The six top-level authored structure count remains mechanically coherent.
The augmented-source clause can be housed inside A3/A4 rather than counted as
a separate top-level carrier. The defect is its standing: V004 calls finite
record observability a derived selection mechanism, but the test is performed
on a gauge-covariant representative.

If a future proposal keeps endpoint-frame coboundaries as physical sources,
it must disclose an authored breaking or replacement of the inherited Gate-4
equivalence. V004 does neither. This review does not author that replacement.

```text
V004_TOP_LEVEL_AUTHORED_STRUCTURE_COUNT = 6 | MECHANICAL_AUDIT
V004_FRAME_ROUTE_PROVENANCE_LINE_IS_VALID = false | TYPE-R |
  test: the claimed derived mechanism conflicts with Gate-4 and V003 S3

HIDDEN_SEVENTH_STRUCTURE_PROVED = NO_VERDICT |
  prerequisite: an independence test between a future gauge-breaking clause
                and the six A1-A6 authored fields
```

### 7.3 Family discipline and derived premises

The full torsor family and endpoint-intertwiner family remain family-wide. No
frame member, global section, background member, rank member, or response
value is selected. `E_post` is not promoted to a physical frame. D0 and Door F
invoke no forbidden completion. The Q-290 unit-modulus no-go remains intact.

The derived Gate-4 premise is not consistent with V004's physical
interpretation of raw `H_N`. This is the failed regression.

```text
SELECTED_FRAME_MEMBER_FOUND = false | TYPE-S |
  roots: V004 A2-A6, endpoint intertwiners, seams, and doors |
  exclusions: local representatives used only for proofs |
  fences: family discipline |
  query: distinguished frame, selected section, evaluated family member

TARGET_AWARE_MEMBERSHIP_PREDICATE_FOUND = false | TYPE-S |
  roots: V004 A1-A6, choice table, seams, and all doors |
  exclusions: terminal fences and audit queries |
  fences: no response or value evaluation |
  query: word-boundaried p_ch, alpha, stiffness, residual value, measured target

UNFLAGGED_CLASS_FORMATION_STEP_FOUND = false | TYPE-S |
  roots: every V004 quotient, inverse limit, pullback, norm completion,
         trace completion, and bilinear class declaration |
  exclusions: operations stated only as TYPE-U |
  fences: Q-288 mandatory door schema |
  query: all class-forming arrows against Doors D0/F/V/A/B/C/D

FORBIDDEN_COMPLETION_INVOKED = false | TYPE-S |
  roots: V004 Doors D0/F/V/A/B/C/D |
  exclusions: unbuilt alternatives |
  fences: Q-288 door flags |
  query: weak-star, bidual, distributional, nonseparating, unnamed limit

DOR008_FULL_PHYSICAL_RESTRICTION_REPRODUCTION_COMPLETE = false | TYPE-U |
  would-build: a lawful Gate-4-compatible physical source quotient, physical
               raw-G image, and complete Q-279 restriction execution
```

---

## 8. Z6: DoR-015 gate

No DoR-015 package is emitted. Ratification would currently adopt a physical
source functional that is nonzero on a derived gauge orbit and a visibility
quotient that distinguishes gauge-equivalent representatives.

Door F, D0, the full torsor and intertwiner families, the no-selection
discipline, the six-count, the Q-288 door declarations, and the absence of
target tuning all survive this review. They are reusable results, but they do
not make V004 ratification-ready.

A successor would have to resolve, before another gate review, the exact
finite quotient actually consumed by A4-A6 and Doors A-C. The review does not
choose or build that successor. The live alternatives remain:

```text
1. quotient finite edge phases by the inherited Gate-4 vertex action and use
   cycle-holonomy/coker(B) source content;
2. restrict source differentiation to a fixed-frame fiber and prove every
   consumer is fiberwise; or
3. openly author a physical breaking/replacement of Gate-4 gauge and price it
   as new premise content.
```

```text
Z1_FRAME_DETERMINATION = KILLED
Z2_AUGMENTED_CURRENT = KILLED_AS_PHYSICAL_SOURCE
Z3_DOOR_F_ZERO_TAIL = SURVIVED_ON_DECLARED_PROJECTIVE_FAMILY
Z4_BOUNDED_RERUN_SET = SPLIT_ALGEBRAIC_PASS_PHYSICAL_FAIL
Z5_FULL_REGRESSION = FAILED_AT_GATE4_INCIDENCE_CONSISTENCY

OVERALL_VERDICT = DEAD

DOR_015_PACKAGE_PREPARED = false | TYPE-C |
  constraint: V004 failed the final independent Gate-4 quotient test |
  release: NONE FOR V004; any successor requires a new proposal and review

DOR_015_ISSUED = false | TYPE-C |
  constraint: principal ratification is unavailable for a killed proposal |
  release: NONE FOR V004
```

---

## 9. Custody

The review artifact is sealed and mirrored with its sidecar. No register,
plan, tracker, git, commit, push, gate, deploy, response evaluation, root, or
value computation is performed by this lane.

```text
REGISTER_HEAD_AT_SEND_TIME = Q-296
REGISTER_SHA256_AT_FINAL_CHECK =
  b20597dc799280bc4654cb08bca67813dfc90cd211c3da1bd810b41f13277758

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```
