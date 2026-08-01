# Stage-8 Task 3d Plane-Coverage Theorem v001

Date: 2026-08-01  
Lane: CODEX LANE 2  
Task: **Task 3d — prove or refute plane coverage on the nullity-two stratum**  
Register head at issue: Q-204  
Road standing: **UNBLOCKS THE FINITE PLANE-FAMILY FORM OF STEP 3, CONDITIONAL ON THE DECLARED REDUCED CARRIER.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Lead theorem

**The plane-coverage conjecture is proved on the complete declared
sixteen-dimensional reduced odd/odd span.** For every weight triple `w`—not
merely for a bounded enumeration—if

```text
K(w) = ker(ad_(Z_w) restricted to V_odd/odd)
```

has real dimension two, then `K(w)` is exactly one of the four real
Hermitian sign-pair planes supported on `X_E/Y_E`. All four occur. Hence

```text
| image(w -> K(w)) on the nullity-two stratum | = 4.
```

The missing support lemma is derived rather than assumed. After complexifying
the declared Pauli span, the commutator splits into two invariant blocks:

```text
edge-diagonal block      Q_E in {I_E,Z_E}   zero relation contributes 4 real dimensions
edge-off-diagonal block  Q_E in {X_E,Y_E}   zero sign pair contributes 2 real dimensions
```

Therefore a two-dimensional kernel cannot contain any edge-diagonal
`I_E/Z_E` support. It must annihilate exactly one off-diagonal sign pair; two
annihilated pairs would already contribute at least four real dimensions.
There are exactly four sign pairs modulo Hermitian conjugation.

This repairs relay 286's coverage failure at the **plane-output** level:
the infinite law family quotiented by equality of its reduced kernel image has
exactly four instantiated classes. It does not identify the underlying grading
laws as complete physical laws and it does not transport the theorem to the
unbuilt complete carrier.

```text
reduced_plane_coverage_theorem_proved = true
reduced_plane_coverage_theorem_standing = TYPE-P |
  premise: the declared reduced carrier, odd/odd span, and Z_w grading ansatz

nullity_two_kernel_has_IE_or_ZE_support = false | TYPE-R
nullity_two_kernel_has_more_than_one_offdiagonal_sign_pair = false | TYPE-R
nullity_two_kernel_outside_four_sign_pair_planes_exists = false | TYPE-R

nullity_two_law_to_kernel_image_cardinality = 4
kernel_image_equivalence_derived = true | TYPE-P
reduced_plane_family_coverage_repaired = true | TYPE-P

complete_carrier_plane_coverage_derived = false | TYPE-U
complete_physical_grading_law_equivalence_derived = false | TYPE-U
forcing_protocol_step_3_executed = false | TYPE-C |
  constraint: this relay stops at the plane-coverage theorem
unique_full_carrier_coupling_ray_derived = false | TYPE-U
```

## 1. Preflight, premises, and standing

### 1.1 Object and version

The object exists in sealed text:

- `FULL_CARRIER_DILATION_SELECTOR_OBSTRUCTION_GATE_V001.md:15-33` declares
  `H_red = C^2_S tensor C^2_R tensor C^2_E` and expressly withholds promotion
  to a complete physical carrier.
- The same file at `:35-49` gives the complete real sixteen-dimensional
  odd/odd span.
- At `:51-68` it defines `Z_w` and the restricted commutator problem.
- Q-183's current adversarial recomputation derives the ladder action at
  `STAGE8_SEAM10_NARROWING_ADVERSARIAL_RECOMPUTATION_V001.md:74-84` and
  gives four bounded kernel images at `:88-97`.
- Q-204 records the infinite law family and makes the present universal
  plane-coverage claim explicitly conjectural.

No later numbered version of the governing carrier gate or Q-183 correction
was found. Relay 286 remains current through Q-204.

```text
object_exists = true
current_version_checked = true
inputs_present = true |
  scope: finite reduced carrier, exact full odd/odd span, symbolic weight triple
schema_substitution_used = false
```

### 1.2 Declared premises at the outset

```text
F1  H_red is the three-factor complex carrier declared by the governing gate.

F2  V_odd/odd is the full real Hermitian span
      {X_S,Y_S} tensor {X_R,Y_R} tensor {I_E,X_E,Y_E,Z_E}.

F3  Z_w = w_S Z_S + w_R Z_R + w_E Z_E and K(w) is the kernel of
    [.,Z_w] restricted to V_odd/odd.

F4  The source, record, and edge Pauli factors are independent tensor factors.

GK1 Equality and dimension are taken in the declared reduced operator space.

GK2 No bounded enumeration, desired channel, unsigned selector, physical
    grading weight, or complete-carrier structure is assumed.

GK3 The theorem classifies kernel images only. Any stronger identity of
    physical grading laws requires a separate complete-carrier theorem.
```

`F1-F3` are sealed declarations, not derivations of the physical carrier.
The theorem below is derived exactly from them. Its physical standing is
therefore `TYPE-P`, not an unconditional full-carrier result.

## 2. Scope and method

### 2.1 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output/
/Users/bgm/MB Work/alpha-program-archive/workspace/
/Users/bgm/MB Work/alpha_supervision/
```

Excluded from recursion and evidence: every `a32_holdout/` and
`custodian_private/` directory, `.git`, dependency/vendor trees, binaries,
media, sidecars as substantive claims, and archive mirrors as independent
authorities. The fenced private directory was not entered, listed, or read.

### 2.2 Method

The proof is a symbolic decomposition of the **entire** declared operator
space. Enumeration is used only as an adversarial cross-check. This distinction
is load-bearing: no finite weight bound occurs in the proof.

Symbol collisions checked:

```text
G  = reduced Hermitian generator, not a gravitational constant
E  = edge/witness tensor factor, not energy
R  = record tensor factor, not a radius
w  = grading coefficients, not a coupling ray
```

## 3. Exact complex ladder decomposition

Define on each binary factor

```text
sigma_+ = (X+iY)/2,
sigma_- = (X-iY)/2.
```

These form a basis of the complexification of `span_R{X,Y}` and satisfy,
up to one common nonzero commutator factor and sign convention,

```text
[sigma_s,Z] proportional to s sigma_s,   s in {+1,-1}.
```

Complexifying `V_odd/odd` yields the direct sum

```text
V_C = D_C direct-sum O_C,

D_C = span_C {
  sigma_(s_S)^S sigma_(s_R)^R tensor I_E,
  sigma_(s_S)^S sigma_(s_R)^R tensor Z_E
  : s_S,s_R in {+1,-1}
},

O_C = span_C {
  sigma_(s_S)^S sigma_(s_R)^R sigma_(s_E)^E
  : s_S,s_R,s_E in {+1,-1}
}.
```

`D_C` is the edge-diagonal sector; `O_C` is the edge-off-diagonal sector.
Together they contain every one of the sixteen declared real directions after
the Hermitian reality condition is imposed. Nothing is omitted.

The commutator is diagonal on this complex basis:

```text
ad_(Z_w) on D_C:
  lambda_D(s_S,s_R) proportional to s_S w_S + s_R w_R;

ad_(Z_w) on O_C:
  lambda_O(s_S,s_R,s_E)
    proportional to s_S w_S + s_R w_R + s_E w_E.
```

This follows factor by factor because operators on different tensor factors
commute. Since the displayed monomials are a basis, nonzero-weight components
cannot cancel one another inside the commutator kernel.

## 4. Support lemma

### Lemma

If `dim_R K(w)=2`, then every member of `K(w)` has edge support only in
`span_R{X_E,Y_E}`.

### Proof

Hermitian conjugation sends every sign tuple `s` to `-s`. Count sign tuples
modulo this simultaneous reversal.

In `D_C`, there are two source-record sign pairs:

```text
[(+,+)] and [(+,-)].
```

For either pair satisfying `s_S w_S+s_R w_R=0`, the `I_E` and `Z_E` copies are
independent. Each complex ladder line plus its conjugate produces a real
Hermitian two-plane, so the two edge-diagonal copies contribute

```text
2 + 2 = 4 real kernel dimensions.
```

Therefore any edge-diagonal zero relation makes `dim_R K(w) >= 4`. It cannot
occur when the nullity is two. Thus the `I_E/Z_E` kernel component vanishes and
the kernel lies wholly in `O_C`. QED.

This proves the support restriction before using the three-sign ladder rule.
It closes the hole left by applying the off-diagonal rule to triples whose
kernels could also have diagonal witness support.

```text
support_lemma_proved = true
support_lemma_assumed_from_bounded_enumeration = false | TYPE-R
IE_ZE_supported_nullity_two_counterexample_exists = false | TYPE-R
```

## 5. Plane-coverage theorem

### Theorem

On `V_odd/odd`, every nullity-two kernel `K(w)` is exactly one of the four
off-diagonal sign-pair planes

```text
P_(+--)  = Hermitian real plane generated by sigma_+^S sigma_-^R sigma_-^E,
P_(+-+)  = Hermitian real plane generated by sigma_+^S sigma_-^R sigma_+^E,
P_(++-)  = Hermitian real plane generated by sigma_+^S sigma_+^R sigma_-^E,
P_(+++)  = Hermitian real plane generated by sigma_+^S sigma_+^R sigma_+^E.
```

Here “Hermitian real plane” means the real span of the displayed monomial plus
its adjoint and of its independent phase partner.

### Proof

By the support lemma, a nullity-two kernel lies in `O_C`. Modulo simultaneous
sign reversal, the eight three-sign tuples form exactly the four pairs listed
above. For each pair satisfying

```text
s_S w_S+s_R w_R+s_E w_E=0,
```

the corresponding complex ladder line and its conjugate contribute exactly
one real Hermitian two-plane.

If no sign pair is annihilated, the kernel is zero. If two or more distinct
sign pairs are annihilated, their basis monomials are independent and the real
kernel dimension is at least four. Therefore nullity two is equivalent to
annihilating exactly one of the four sign pairs, and `K(w)` equals its plane.
No fifth off-diagonal sign-pair plane exists in the declared span. QED.

All four images occur; Q-183 supplies primitive representatives:

| Plane | One primitive representative | Zero relation |
|---|---:|---|
| `P_(+--)` | `(2,1,1)` | `w_S-w_R-w_E=0` |
| `P_(+-+)` | `(2,1,-1)` | `w_S-w_R+w_E=0` |
| `P_(++-)` | `(2,-1,1)` | `w_S+w_R-w_E=0` |
| `P_(+++)` | `(2,-1,-1)` | `w_S+w_R+w_E=0` |

Hence the image size is not merely at most four; it is exactly four.

An equivalent exact nullity formula is

```text
dim_R K(w) = 4 N_D(w) + 2 N_O(w),

N_D(w) = number of diagonal sign pairs with s_S w_S+s_R w_R=0,
N_O(w) = number of off-diagonal sign pairs with
         s_S w_S+s_R w_R+s_E w_E=0.
```

Thus `dim_R K(w)=2` if and only if `N_D(w)=0` and `N_O(w)=1`.

```text
plane_coverage_at_most_four_proved = true
all_four_planes_realized = true
plane_coverage_exactly_four_proved = true
off_four_plane_nullity_two_counterexample_exists = false | TYPE-R
```

## 6. Counterexample hunt and theorem attacks

The reviewer conjecture was attacked in five structurally distinct ways.

### A1 — diagonal-support counterexample

An `I_E/Z_E` kernel direction cannot occur alone: the independent `I_E` and
`Z_E` copies make every diagonal zero relation contribute four real dimensions.
This attack fails by the support lemma.

### A2 — cancellation between sign channels

The ladder monomials are a basis and `ad_(Z_w)` is diagonal on them. Components
with nonzero weights cannot cancel across independent basis vectors. This
attack fails.

### A3 — two relations but only one real plane

Distinct sign pairs use distinct ladder monomials. Two annihilated pairs give
two independent real planes and nullity at least four. This attack fails.

### A4 — zero components and diagonal degeneracies

Weights with `w_S=+/-w_R` activate a diagonal sign pair and therefore have
nullity at least four. Zero components can make sign relations coincide in
pairs, but then they increase rather than hide kernel dimension. They do not
produce an off-plane nullity-two kernel.

### A5 — exact matrix cross-check

The governing exact Gaussian-integer matrix implementation was run on
representatives of all four planes, large members of Q-204's infinite family,
diagonal-support cases, zero-component cases, multiple-relation cases, and a
generic no-relation case. Every result agreed with
`dim_R K=4N_D+2N_O`. This execution is an adversarial check, not the universal
proof.

```text
counterexample_hunt_completed = true
counterexample_found = false | TYPE-R |
  scope: the complete declared reduced odd/odd carrier and every weight triple
theorem_depends_on_finite_weight_enumeration = false | TYPE-R
```

## 7. Derived equivalence and exact scope of the repair

Define the reduced selector equivalence

```text
w equivalent_K w'  iff  K(w)=K(w') as subspaces of V_odd/odd.
```

Equality makes this an equivalence relation without importing a physical
source-record swap or convention. By the theorem, its quotient on the
nullity-two stratum has exactly four classes, represented by the four planes.
The Q-204 infinite family is therefore descriptive multiplicity for the
specific output `K(w)`.

This is the step-2 equivalence needed when the selected object is the reduced
kernel plane. It is **not** a theorem that different `Z_w` are identical as
complete physical grading laws. A consumer sensitive to `Z_w` outside the
kernel map could still distinguish them, and the complete physical carrier is
unbuilt.

Consequently:

```text
reduced_nullity_two_kernel_image_family_finite = true
reduced_nullity_two_kernel_image_family_instantiated = true
reduced_nullity_two_kernel_image_family_Q200_compliant = true | TYPE-P
relay286_law_level_coverage_failure_repaired_at_plane_level = true | TYPE-P
forcing_protocol_may_resume_at_step_3_on_four_reduced_planes = true | TYPE-P

same_kernel_implies_same_complete_physical_grading_law = NO_VERDICT
complete_carrier_kernel_image_cardinality = NO_VERDICT
complete_carrier_step_2_equivalence_derived = false | TYPE-U
```

No plane constraint was applied and no survivor was selected in this relay.

## 8. Premise ledger

| Item | Standing | Evidence |
|---|---|---|
| Three-factor reduced carrier | adopted/declared, `TYPE-P` | Governing gate `:15-33`; expressly not complete |
| Full sixteen-dimensional reduced odd/odd span | derived within the declaration | Governing gate `:35-49`; exact audit implementation |
| Integer `Z_w` grading ansatz | adopted candidate law, `TYPE-P` | Governing gate `:51-68`; not the axial Ward identity |
| Ladder diagonalization | derived | tensor-factor commutator algebra; Q-183 `:74-84` |
| Support lemma | derived | full diagonal/off-diagonal decomposition in section 4 |
| Four-plane coverage | derived | theorem in section 5 |
| Kernel-image equivalence | derived on the reduced selector | equality of kernel subspaces |
| Complete-carrier transport | unbuilt, `TYPE-U` | governing gate `:31-33,127-155` |
| Physical-law identity beyond the kernel map | unbuilt, `TYPE-U` | no complete-carrier transformation theorem |

## 9. Final typed verdict block

```text
TASK3d_plane_coverage_object_exists = true
TASK3d_plane_coverage_current_version_checked = true
TASK3d_plane_coverage_inputs_present = true

support_lemma_proved = true
support_lemma_assumed = false | TYPE-R
nullity_two_kernel_has_IE_or_ZE_support = false | TYPE-R
nullity_two_kernel_has_multiple_offdiagonal_sign_pairs = false | TYPE-R

reduced_plane_coverage_theorem_proved = true
reduced_plane_coverage_theorem_standing = TYPE-P |
  premise: declared reduced carrier, complete odd/odd span, Z_w ansatz
nullity_two_law_to_kernel_image_cardinality = 4
off_four_plane_nullity_two_counterexample_exists = false | TYPE-R

kernel_image_equivalence_derived = true | TYPE-P
reduced_plane_family_coverage_repaired = true | TYPE-P
reduced_plane_family_Q200_compliant = true | TYPE-P
forcing_protocol_step_3_legally_reachable_on_reduced_planes = true | TYPE-P
forcing_protocol_step_3_executed = false | TYPE-C |
  constraint: relay scope stops at the theorem

same_kernel_implies_same_complete_physical_grading_law = NO_VERDICT
complete_carrier_plane_coverage_derived = false | TYPE-U
unique_full_carrier_coupling_ray_derived = false | TYPE-U
seam10_discharged = false | TYPE-U

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

