# Stage 8 Task 4a Response-Class Forcing and Tail-Output Inertness Determination v001

Date: 2026-08-02
Lane: CODEX LANE 1
Task: 4a
Authority: DoR-011, proof and construction only
Register head at issue: Q-249

## 0. Lead determination

**THE FALSIFIER DOES NOT FORCE `RetHess_phys` INTO THE SEPARABLE CLASS. IT
FORCES, AT MOST, A RESPONSE COSET MODULO THE FINITE-RESTRICTION TAIL.**

The proof attempt fails at the physical source completion. The sealed finite
operations are norm/module preserving, but the physical chain then requires:

```text
source differentiation in topology_src/Diff_src;
source-inclusive continuum/projective completion;
convolution inversion on the completed quotient;
stationary 2PI-to-1PI reduction and Schur inversion;
contour/i-epsilon boundary values;
retarded extraction on completed domains;
and, downstream, a q^2 -> 0 Thomson limit.
```

No sealed source types any of those limit or derivative operations as norm
preserving. Q-245 has already refuted the obvious norm-continuous extension.

The counterexample succeeds against forcing from finite restrictions. Let

```text
Tail_B** = intersection_N ker((r_N^B)**) = z_tail B**
```

as proved in Q-247. For any complete candidate `H` in a class admitting this
tail and any `t in Tail_B**`, the family

```text
H_t := H + t
```

has exactly the same finite restrictions as `H`. Addition, adjoint,
composition, finite CTP block operations, and inversion where defined do not
restore detectability: every extended finite restriction annihilates `t`.
The weak-star moving-tail construction also shows how a completion operation
can exit the norm class while retaining all finite data.

This is a refutation of the **forcing inference**, not a determination that
the physical response is bidual. The physical response class, its restriction
maps, and the embedding of `z_tail B**` into a retarded physical kernel remain
unbuilt.

The output-side rescue also fails at present. No alpha-facing complete output
is proved to factor through finite restrictions or to annihilate the tail:

```text
p_loc / B_ind / C_EM / R_comp: complete-operator maps, unbuilt;
DeltaPhi[K;X_K]: response-to-phase map unbuilt, no ratio/homogeneity rule;
kappa_Q(q^2) / kappa_Thomson: complete-amplitude and q^2-limit maps,
                              no finite-restriction factorization.
```

The sharp remaining theorem is therefore:

```text
ALPHA_FACING_OUTPUT_TAIL_ANNIHILATION:
  O(H+t)=O(H)
  for every admitted complete response H,
  every t in Tail_R,
  and every alpha-facing output O.
```

Equivalently, every such `O` must factor through the complete family of
physical finite restrictions. That theorem is not sealed.

```text
DOR008_RESTRICTION_DISCIPLINE_FORCES_NORM_RETHESS_CLASS = false | TYPE-R |
  test: H and H+t, t in z_tail B**, have identical extended finite
        restrictions while belonging to distinct complete bidual classes

PHYSICAL_RETHESS_IS_BIDUAL = NO_VERDICT |
  prerequisite: RetHess_phys, physical rho_H,N, and a physical tail embedding
                are uninstantiated

PHYSICAL_RESPONSE_DETERMINED_MODULO_TAIL = true | TYPE-P |
  premises: an instantiated complete response class, linear physical
            restrictions, and closure under tail addition

ALPHA_FACING_OUTPUT_TAIL_INERTNESS_PROVED = false | TYPE-U |
  would-build: instantiate the physical response/restriction class and prove
               each output factors through the family of finite restrictions

P_CH_TAIL_ROUTE_DEAD = NO_VERDICT |
  prerequisite: either physical Tail_R={0} or output-tail annihilation

P_CH_TAIL_ROUTE_LIVE = NO_VERDICT |
  prerequisite: a physical p_ch-dependent tail and one complete output that
                detects it
```

## 1. Scope, current authority, and premises

### 1.1 Preflight and current head

```text
DOES_THE_OBJECT_EXIST = true
  Q-249 poses the class-forcing question after the symmetric class audit.

IS_THE_VERSION_CURRENT = true_through_Q_249
  no later registered ruling existed at the start of this run.

ARE_THE_INPUTS_PRESENT = sufficient_for_the_logical_forcing_test
  Q-247 supplies both the norm separation theorem and exact bidual tail;
  the physical class and maps remain absent and are not fabricated.
```

### 1.2 Authorities

| Authority | SHA-256 | Load-bearing content |
|---|---|---|
| `STAGE8_TASK4A_PHYSICAL_RESPONSE_CLASS_SEALED_SIGNATURE_DETERMINATION_V001.md` | `8dc5e133c2cf857b1b6ea48c933717b29912b8a39bf192e946d2e36f0bef2e22` | Q-249: complete response chain class-untyped |
| `STAGE8_TASK4A_FINITE_RESTRICTION_SEPARATION_AND_BIDUAL_TAIL_DETERMINATION_V001.md` | `60b5b4c5788eca2be2d9f11d67983b2e7a5823066cdabf9a734f7a59aae0ecd1` | Q-247: norm separation and exact bidual tail |
| `STAGE8_TASK4A_CORRELATOR_COMPLETION_ARROW_AND_RESTRICTION_PINNING_DETERMINATION_V001.md` | `5b9a4a8b000c313049caa71aff4235cc9eb4b0f98bb2af9931fd8820930ed856` | Q-245: naive norm extension refuted; tail/background split |
| `STAGE8_TASK4A_FINITE_HESSIAN_TO_DELTAPHI_TRANSPORT_MAP_CONSTRUCTION_AND_P_CH_TRACE_V001.md` | `70185aa842bc500724719c65bd66b5f07005e2214b97be0d35e07fd029d5c68c` | Q-243: finite CTP operations and complete transport stop |
| `STAGE8_FINITE_P_CH_DEPENDENCE_AND_PHASE_RESIDUAL_TRANSPORT_DETERMINATION_V001.md` | `8a71b6cdeca839fb6e52dbac4c2d13f7b9d2dafc3531dc1cc8bdc9089b3410b0` | phase output has no sealed ratio/homogeneity rule |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_ITEM2_PHYSICAL_LOG0_GERM_SPEC_V001.md` | `14573a676a385dd4c814f3fd12d8fb53caa601598e96b35525c6372329d506b3` | physical source topology/calculus unbuilt |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U3_DOR008_DOR009_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` | `b0118d89e0b4b321fbf9caab5bfb811a0b5fd572e808d02615ee8503db2bc1ac` | physical contour, measure, boundary, and domains unbuilt |
| `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md` | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | complete physical operations and T5 restriction discipline |
| `primitive_record_cell_selection_principle_v004.md` | `13d227ceb2198d96b0e4e2fef57b874cea71cb755320508fbf4c6d64a00c507e` | live response, projection, background, and phase roles |
| `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `20a3a17d44e15841baded9eaed3fdbecfde0ecb14bdb8162ea41a8bcd21d1a48` | complete Thomson response and zero-momentum limit |

The cleanroom, parent program root, and supervision register were entered.
`a32_holdout/custodian_private/` was not entered. No value-bearing holdout
file was opened.

### 1.3 Imported mathematics

The following standard facts are used explicitly:

1. a bounded star-homomorphism extends normally to biduals;
2. the kernel of a homomorphism is preserved under addition, adjoint, and
   multiplication by admitted elements;
3. a homomorphism maps an inverse to the inverse whenever both are defined;
4. differentiation commutes with a continuous linear map in a calculus where
   both operations are defined; and
5. a map is constant on cosets of a linear subspace exactly when it factors
   through the corresponding quotient.

These are mathematical tools. They do not adopt a bidual physical response,
a source topology, or an output factorization.

## 2. Candidate forcing theorem

### 2.1 Exact candidate

The strongest candidate supported by the relay is:

> Any complete physical retarded response built from DoR-008's norm-class
> finite source maps by the operations sealed in the response chain, and
> reproducing every sealed finite response under physical restriction, lies
> in a class on which Q-247 separation holds.

Let the proposed input conditions be:

```text
F1  finite source maps s_J/s_R are bounded norm/module objects;
F2  the complete object is built using only sealed response-chain operations;
F3  physical restrictions reproduce every sealed finite result;
F4  every operation commutes with those restrictions where the chain requires;
F5  no post-output supplement is added.
```

The desired conclusion is:

```text
RetHess_phys subset L_B(E_F)
```

or another class with zero common finite-restriction kernel.

### 2.2 Operations actually named by the sealed chain

| Operation | Source | Class-preservation status |
|---|---|---|
| finite-support source insertion `s_J/s_R` | Q-249, U1_008 | norm/module preserving at finite level |
| finite linear combinations, products, adjoints | DoR-008 C-star/module grammar | norm/module preserving |
| finite Keldysh transform `T_CTP^T H T_CTP` | raw-map spec `:785-819`; Q-243 | finite bounded matrix operation; preserving |
| ordered mixed-block projection | same | finite bounded linear projection; preserving |
| pointwise `Z_inc`, `Log_0`, and source differentiation | item-2 source-germ spec `:237-316` | `topology_src` and `Diff_src` explicitly unbuilt |
| source-inclusive continuum/projective completion | Q-245 `:322-448`; raw-map spec `:420-466` | topology unbuilt; naive norm-continuous extension refuted |
| raw correlator to convolution operator | raw-map spec `:639-722` | measure, delta distribution, and operator topology unbuilt |
| two-sided convolution inversion | same | class preserving only after a common Banach/operator algebra and domain are fixed; absent |
| stationary reduction `G_*(Abar)` | raw-map spec `:724-755`; v004 `:172-180` | stationary class and block-inverse topology unbuilt |
| Schur complement | raw-map spec `:743-755` | requires an inverse in an untyped completed class |
| contour/i-epsilon boundary value and retarded support | U3 `:337-400`; raw-map spec `:821-828` | physical contour and limit topology unbuilt |
| induced response subtraction and local projection | v004 `:115-168` | common operator space and `p_loc` unbuilt |
| response-to-on-shell-phase map | Q-243 `:237-259`; phase audit `:447-511` | unbuilt |
| zero-momentum Thomson limit | V011 `:1613-1655` | limit required; topology not stated |

## 3. Proof attempt

### 3.1 What does preserve the separable class

Inside the ratified class

```text
B = A_F,+ tensor_min (A_F,-)^op,
E_F = B_B,
L_B(E_F)=L(B),
```

finite sums, products, adjoints, left multiplication, the finite CTP matrix
transform, and finite block extraction remain in the same norm class. Q-247
then gives:

```text
intersection_N ker(Pi_N) = {0}
```

on represented left multipliers.

If the complete construction were already proved to use only these
operations and norm limits in this class, the forcing theorem would close.
That premise is not present.

### 3.2 The circular step

The candidate proof says:

```text
finite restrictions determine H
because finite restrictions separate the admissible class.
```

But Q-247 separation applies only **after** the admissible class is placed in
`L_B(E_F)`. It cannot prove that placement. Using separation to select the
class on which separation holds is circular.

```text
FINITE_CORE_ARGUMENT_DERIVES_ITS_OWN_RESPONSE_CLASS = false | TYPE-R |
  test: the separation premise is class-relative and the desired class
        inclusion is an independent hypothesis of the proof
```

### 3.3 The first genuine exit

The finite source interface ends before the physical source germ. The next
operation is differentiation of the completed scalar functional in an
independently derived `topology_src/Diff_src`. The source-germ specification
expressly refuses to select a Banach, locally convex, Frechet, Gateaux,
Bastiani, or other calculus.

Even before raw `G` exists, the norm-preservation proof therefore stops.
Downstream inversion, Schur reduction, contour limits, and the Thomson limit
add independent untyped exits.

The limit danger is realized, not hypothetical: Q-245 proves the finite
amplitude has no continuous extension through the ratified compact-spectrum
product topology, and Q-247 constructs a nonzero weak-star limit in `B**`.

```text
SEALED_OPERATIONS_PRESERVE_NORM_MODULE_CLASS_END_TO_END = false | TYPE-U |
  would-build: topology_src, Diff_src, a norm-closed physical source germ,
               class-preserving differentiation/inversion/stationarity/
               contour-limit theorems, and the q^2-limit topology

CANDIDATE_RESPONSE_CLASS_FORCING_THEOREM_PROVED = false | TYPE-R |
  test: the weak-star completion model H+f(s)t preserves every finite
        restriction and the named algebraic operation forms while lying
        outside the norm class; no current premise excludes that model
```

The second flag refutes the proposed derivation from the current premise set.
It does not refute the possibility that a future physical construction lands
in the norm class for independent reasons.

## 4. Countermodel to forcing

### 4.1 Tail extension

Q-247 proves:

```text
Tail_B**
  = intersection_N ker((r_N^B)**)
  = M_cyl(Y)^perp
  = z_tail B**
  != {0}.
```

Choose any nonzero `t in Tail_B**`. Let `H` be any candidate in a completed
class containing the canonical image of `B` and `Tail_B**`. Define:

```text
H_t := H + t.
```

Then, for every finite stage:

```text
(r_N^B)**(H_t)
  = (r_N^B)**(H) + (r_N^B)**(t)
  = (r_N^B)**(H).
```

Thus every test whose input is only the family of finite restrictions gives
the same verdict on `H` and `H_t`.

```text
TAIL_ADDITION_PRESERVES_ALL_FINITE_RESTRICTION_DATA = true | TYPE-P |
  premises: Q-247's exact Tail_B** characterization and linear extended
            restrictions

FINITE_RESTRICTION_COMPLIANCE_SELECTS_ONE_COMPLETE_ELEMENT = false | TYPE-R |
  test: H and H+t are distinct and have identical restrictions for every N
```

### 4.2 Compatibility with named algebraic operations

Because each `(r_N^B)**` is a star-homomorphism:

1. adjoints and finite linear combinations of tail terms remain invisible;
2. products containing a tail factor remain in the tail ideal;
3. finite CTP matrix transformations preserve invisibility componentwise;
4. a tail may be placed in an ordered block without changing any finite block;
5. whenever `H_t` is invertible, its finite inverse equals the inverse of the
   finite restriction of `H`; and
6. block algebra and Schur operations, where all inverses exist, cannot recover
   a term already annihilated by the homomorphism.

For source dependence, let `f` be any scalar germ in a future admitted
calculus and define:

```text
H_t(s) := H(s) + f(s)t.
```

Every finite source germ and every finite derivative is unchanged, while the
complete derivative can differ by a tail-valued term. This is a logical model
of the missing calculus, not an adopted physical germ.

Q-247's explicit moving-tail net supplies the relevant completion operation:

```text
v_U = weak-star-lim_(m->U) v_m in B**,
```

with every fixed finite restriction zero and `v_U != 0`.

### 4.3 What the countermodel does not establish

The physical codomain also demands retarded support, CTP reality, Ward
identities, covariance, measure, contacts, boundary data, and domains. Those
objects are uninstantiated. The countermodel proves that the **current
forcing data** do not exclude a tail. It does not prove that a nonzero element
of `z_tail B**` embeds into an admissible physical retarded kernel satisfying
all those conditions.

One conditional embedding shape is:

```text
t tensor V_R,
```

where `V_R` is a nonzero homogeneous direction in the future physical
`RetHess` codomain. All finite restrictions still vanish. Whether such a
`V_R` and tensor/module embedding exist is part of the unbuilt physical class,
so it remains `NO_VERDICT`.

```text
BIDUAL_TAIL_IS_ADMITTED_PHYSICAL_RETHESS_CONTENT = NO_VERDICT |
  prerequisite: a class-typed RetHess_phys, physical restrictions, and a
                support/reality/Ward/domain-preserving tail embedding

P_CH_HAS_NONZERO_COMPONENT_IN_PHYSICAL_TAIL = NO_VERDICT |
  prerequisite: the completed source germ, stationary map, and
                coherent-to-retarded construction
```

## 5. Exact surviving determinacy: a quotient, not a class

Let a future physical response class `R_phys_class` and restrictions

```text
rho_N:R_phys_class->R_N
```

be instantiated. Define:

```text
Tail_R := intersection_N ker(rho_N).
```

The family of all restrictions determines only the equivalence class

```text
[H] in R_phys_class / Tail_R,

H ~ H' iff H-H' in Tail_R.
```

Call this result **TAIL-QUOTIENT DETERMINACY**:

> Finite data determine the completed response exactly as a coset modulo
> restriction-invisible content. They determine an element only if the tail
> vanishes or every physical consumer is constant on tail cosets.

This is the lawful content of "forced up to a tail." It is neither norm-class
forcing nor a physical bidual adoption.

```text
TAIL_QUOTIENT_DETERMINACY = true | TYPE-P |
  premises: instantiated linear physical restrictions

ELEMENTWISE_COMPLETE_RESPONSE_DETERMINACY = NO_VERDICT |
  prerequisite: Tail_R={0} or output-tail annihilation, plus the physical T5
                restriction square
```

## 6. Output-side tail-inertness audit

### 6.1 Criterion

For an alpha-facing output `O`, the following are equivalent:

```text
O(H+t)=O(H) for every t in Tail_R;

O factors through R_phys_class/Tail_R;

O factors through the complete family of physical finite restrictions,
provided that family realizes the quotient.
```

Only such an output is proved tail-inert without first proving `Tail_R=0`.

### 6.2 Per-output results

| Output | Sealed input role | Finite-factorization status | Tail verdict |
|---|---|---|---|
| finite Q-243 mixed block | explicit finite Keldysh projection | already finite | tail-inert at finite stages only; not the complete output |
| normalized finite amplitude | finite scalar function and equal-history normalization | already finite | tail-inert at finite stages only |
| `p_loc` | linear coefficient functional on the complete inverse-kernel operator | unbuilt; no restriction factorization | `NO_VERDICT` |
| `B_ind(K)` / `C_EM(K)` | `p_loc` applied to complete induced/full residual operators | unbuilt; no restriction factorization | `NO_VERDICT` |
| `R_comp[G_K]` | complementary part of the complete operator residual | consumes full operator; no factorization | `NO_VERDICT` |
| `DeltaPhi[K;X_K]` | phase on complete on-shell cell | response-to-phase map unbuilt | `NO_VERDICT` |
| `C_record=DeltaPhi-pi` | additive scalar residual | no kernel ratio or homogeneity rule sealed | `NO_VERDICT` |
| `kappa_Q(q^2)` | coefficient of complete transverse quadratic response | complete-amplitude map; no finite factorization | `NO_VERDICT` |
| `kappa_Thomson` | path-independent `q^2->0` limit of `kappa_Q` | limit topology and restriction relation unstated | `NO_VERDICT` |

### 6.3 Why normalization does not prove inertness

The finite equal-history denominator is exactly one, and Q-237 proves it does
not remove the finite `p_ch` factors. The complete Thomson amplitude is also
normalized by `Z_Q[0]`, but a ratio is tail-inert only if numerator and
denominator carry the same tail dependence in a proved homogeneous way. No
such theorem is sealed.

The phase candidate is explicitly additive:

```text
C_record(K)=DeltaPhi[K;X_K]-pi.
```

Q-237 proves that no response-kernel denominator or homogeneity degree is
sealed. Therefore neither normalization nor the target phase annihilates a
tail by form alone.

### 6.4 Bounded negative

The output-factorization search used the cleanroom Markdown root, excluding
mirrors and `a32_holdout/custodian_private/`, with word-boundaried combinations
of:

```text
DeltaPhi | p_loc | B_ind | C_EM | R_comp | kappa_Q | kappa_Thomson

with

factor | finite restriction | cylindrical | tail | annihilate | quotient
```

The only bearing hits were Q-245/Q-247/Q-249 statements posing the tail
criterion and the C-record lineage statement that factors through the
stationary cell. No sealed alpha-facing output was found to factor through
the complete physical finite-restriction family.

```text
ALPHA_OUTPUT_FINITE_RESTRICTION_FACTORIZATION_FOUND = false | TYPE-S |
  roots: cleanroom Markdown root |
  excl: mirrors; sidecars; a32_holdout/custodian_private; measured data |
  fences: DoR-011 proof/construction only |
  query: the exact paired term families above, followed by line reading of
         every bearing hit

TAIL_SURVIVES_INTO_A_SEALED_ALPHA_OUTPUT = NO_VERDICT |
  prerequisite: a physical tail embedding and one instantiated complete
                output map that does not annihilate it
```

## 7. The sharp missing lemma

The remaining object is one theorem with a per-output certificate:

```text
ALPHA_FACING_OUTPUT_TAIL_ANNIHILATION_THEOREM

Inputs:
  RetHess_phys;
  physical rho_H,N;
  Tail_R=intersection_N ker(rho_H,N);
  the complete output maps p_loc, R_comp, DeltaPhi, kappa_Q, kappa_Thomson.

Claim:
  for every output O and every t in Tail_R,
  O(H+t)=O(H).

Equivalent certificate:
  O = O_tilde compose R,
  where R(H)=(rho_H,N(H))_N.
```

There are two lawful closure routes:

1. **object-side:** derive `RetHess_phys` in the Q-247 norm/left-multiplier
   class and prove the physical restrictions are the separating maps; or
2. **output-side:** permit a larger class but prove every alpha-facing output
   annihilates its tail.

Neither route is complete. The forcing theorem cannot choose route 1, and no
sealed output currently supplies route 2.

## 8. Kill-passes

### 8.1 No topology switch mid-proof

The norm proof, weak-star countermodel, and untyped physical class are kept as
three separate cases. The bidual witness is never called a norm element or a
physical kernel.

### 8.2 No natural-continuity argument

No appeal is made to what physical responses "normally" are. Q-245's failed
norm extension is carried as counterevidence.

### 8.3 No output inertness by hope

Every complete output is listed separately. Finite normalization and the
additive phase residual are not promoted to tail-annihilation theorems.

### 8.4 No p_ch identification with the tail

The scalar multiple `p_ch t` is a mathematical tail family. Q-243's coherent
one-point covector is not identified with it. Physical occupation remains
`NO_VERDICT`.

## 9. Final flag block

```text
RESPONSE_CLASS_FORCED_BY_DOR008_FALSIFIER = false | TYPE-R |
  test: the exact z_tail B** extension preserves every finite restriction

RESPONSE_CLASS_FORCING_PROOF_FAILS_AT_FIRST_PHYSICAL_DERIVATIVE = true |
  standing: source topology/calculus is TYPE-U before raw G exists

WEAK_STAR_LIMIT_CAN_EXIT_RATIFIED_NORM_CLASS_WITHOUT_FINITE_DISAGREEMENT =
  true | TYPE-P |
  premises: Q-247 moving-tail theorem

FORCED_UP_TO_TAIL = true | TYPE-P |
  premises: instantiated linear restriction family

PHYSICAL_TAIL_EXISTS = NO_VERDICT
PHYSICAL_TAIL_CONTAINS_P_CH = NO_VERDICT
PHYSICAL_TAIL_IS_OUTPUT_INERT = NO_VERDICT
P_CH_TAIL_ROUTE_DEAD = NO_VERDICT
P_CH_TAIL_ROUTE_LIVE = NO_VERDICT

SHARPEST_MISSING_OBJECT = ALPHA_FACING_OUTPUT_TAIL_ANNIHILATION_THEOREM

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

Finite restrictions determine exactly what they can see. Without a
class-preservation theorem they do not choose the response class; without an
output-factorization theorem they do not make the unseen tail physically
inert.
