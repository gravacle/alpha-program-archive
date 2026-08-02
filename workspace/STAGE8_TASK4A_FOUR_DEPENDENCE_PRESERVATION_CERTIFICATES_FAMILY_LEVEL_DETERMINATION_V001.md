# Stage 8 Task 4a Four Dependence-Preservation Certificates at Family Level Determination V001

Date: 2026-08-02  
Task: PASTE 363 / Task 4a  
Lane: CODEX LANE 2  
Status: FOUR UNIVERSAL CERTIFICATES REFUTED; FINITE-SHADOW ACCOUNTING THEOREM PROVED; REPLACEMENT CERTIFICATE NAMED

Premise-dependent positives are marked:

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013, DoR-014
```

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Lead determination

**`Tail_R` evades all four proposed full-realization certificates, and the
universal “neither injects nor deletes `p`-dependence” requirement is itself too
strong. Item (a) is not discharged.**

The requested proof engine fails at its first premise. The standing constraint
battery does mention `p_ch` explicitly:

```text
B2  finite retarded block is zero and p_ch-independent;
B3  finite response restrictions stay p_ch-free, while completed p_ch
    dependence may enter through physical tail content or the stationary
    background.
```

These are `STAGE8_TASK4A_MISSING_PHYSICAL_LAYER_CONSOLIDATED_SPEC_AND_CONSTRAINT_BATTERY_V001.md:503-515`.
Thus “admissibility never mentions `p`” is false. More importantly, B3 expressly
leaves the response tail and background as lawful dependence channels.

Even a genuinely `p`-blind operation need not preserve dependence: a linear
map can have a kernel. Integration, boundary-value projection, quotient/null
removal, and domain restriction all have admissible kernels. Q-279's own exact
finite result exhibits the physically relevant version: the noise and
`J_delta/R` blocks carry `p`, while the ordered retarded block is zero because
the selected projection has no common-source leg. Deleting dependence from one
component is not automatically a defect; it can be the content of the physical
map.

The exact result is:

```text
MEASURE_UNIVERSAL_NO_INJECTION_NO_DELETION_THEOREM = false | TYPE-R
CONTOUR_UNIVERSAL_NO_INJECTION_NO_DELETION_THEOREM = false | TYPE-R
BOUNDARY_UNIVERSAL_NO_INJECTION_NO_DELETION_THEOREM = false | TYPE-R
DOMAIN_UNIVERSAL_NO_INJECTION_NO_DELETION_THEOREM = false | TYPE-R

FULL_CERTIFICATES_PROVED = 0
FULL_CERTIFICATES_REFUTED = 4

FINITE_SHADOW_PATTERN_PRESERVATION = true | TYPE-P |
  premises: DoR-008 finite-restriction reproduction plus Q-243/Q-279 exact
            finite reference tuple |
  condition: the completed chain supplies the B1-B3 commuting physical
             restriction square

ITEM_A_DISCHARGED = false | TYPE-U |
  would-build: arrow-by-arrow p-dependence ACCOUNTING certificates, not
               universal no-injection/no-deletion certificates
```

What is proved at family level is narrower and useful:

> Any completed chain admitted by B1-B3 must reproduce the whole Q-279 finite
> restriction pattern: the finite retarded block remains zero and `p`-free,
> while the finite noise and `J_delta/R` blocks retain their exact symbolic
> weights. A mismatch voids that completion.

This theorem governs the **finite shadows of the assembled chain**. It does not
prove that each unbuilt field is injective on every `p`-carrying component, and
it does not govern restriction-invisible response tails.

The correct replacement for Q-280 item (a) is a four-row **dependence-accounting
certificate**. For each field it must state its parameter action, kernel, image,
tail action, and commuting restriction square. It may lawfully certify a
specific deletion—such as noise-to-retarded projection—provided the deletion
is explicit and the full finite reference tuple is reproduced.

## 1. Preflight, scope, and authorities

### 1.1 Currency

This determination is current through Q-280. Q-279 supersedes the earlier
in-flight standing of relay 361 and is consumed here as the exact finite
nonzero-`R` reference.

### 1.2 Roots entered and exclusions

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha_supervision
```

Excluded or not performed:

```text
a32_holdout/custodian_private/                    NOT ENTERED
alpha/kappa/coupling/root/scale evaluation        NOT PERFORMED
physical response value evaluation                NOT PERFORMED
comparison to measured constants                  NOT PERFORMED
register/plan/tracker/git/commit/push              NOT TOUCHED
```

### 1.3 Authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `STAGE8_TASK4A_MINIMAL_CONSUMPTION_AUDIT_AND_CORE_REDUCTION_DETERMINATION_V001.md` | `9ede28633b49081e4c6b1461663d14653b2b1017900c6a8c3e0076cc53545144` | Q-280 certificate proposal and residual channels |
| `STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md` | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | Q-279 exact finite `p`-free retarded and `p`-carrying noise/probe blocks |
| `STAGE8_TASK4A_P2_PHYSICAL_SOURCE_TOPOLOGY_AND_DIFFERENTIAL_CALCULUS_CONSTRUCTION_V002.md` | `40b2af34443e051fffdc7bf2ec7025c811a98c501a82d19164596ee6f37f00c1` | source topology, dense core, restriction naturality, `Tail_src={0}` |
| `STAGE8_TASK4A_P4_PHYSICAL_LOG_GERM_ON_P2_CALCULUS_CONSTRUCTION_V001.md` | `b4c77ea948a02f3736fc824976f9ebd6381deff35f5c339a646739ea159725c5` | anchored physical log germ and exact derivatives |
| `STAGE8_TASK4A_P3_SECOND_ATTACK_LAW_SIDE_CONSTRUCTION_AND_NARROWED_STOP_V001.md` | `8e9a09c104f4b6352263591037b2e0bb9a82b659aa1b6276cdd48117f872acec` | four field interfaces, exact law-side subpackage, and evasion-capable operations |
| `STAGE8_TASK4A_RESPONSE_CLASS_FORCING_AND_TAIL_OUTPUT_INERTNESS_DETERMINATION_V001.md` | `fccd16a74269386a2fdb7bac122f907cd659c8eb09ae5f45eabf39e5e9180d79` | `H+f(p)t` tail countermodel and quotient determinacy |
| `STAGE8_TASK4A_ALPHA_FACING_OUTPUT_TAIL_ANNIHILATION_THEOREM_DETERMINATION_V001.md` | `a71d4e59fcde1a7df10e8051e46befb9b4b6653a0917bb03a0c0403179717fef` | output-tail scope split and six unspecified consumptions |
| `STAGE8_TASK4A_P7_FINITE_CORE_SEPARATION_T5_COMMUTING_SQUARE_CERTIFICATE_V001.md` | `07205bf5e1888bd39a97d4e86543852d5e9b88b103e5c0b429c76bd77290d6be` | conditional field/package preservation and extraction naturality |
| `STAGE8_TASK4A_MISSING_PHYSICAL_LAYER_CONSOLIDATED_SPEC_AND_CONSTRAINT_BATTERY_V001.md` | `241bf43f04aed7f215bad6ea80170a9c7733000896df839ac80974769d0a46c3` | P3 signatures and B1-B14 admissibility battery |

## 2. Exact definitions

### 2.1 Parameter channel

For every admitted ordered-rank class `[A]`, the only built entry path is:

```text
[A] -> d_state -> p_[A] -> Z_[A] -> Log_0 Z_[A] -> derivatives.
```

No rank pair or ratio is evaluated. Let `A_p` denote the algebra of symbolic
coefficient functions generated by the exact germ coefficients, including
`p`, the probe-dressed weight `omega_R`, and the noise coefficient
`kappa_R`. A source or response object can be written schematically as an
element of:

```text
A_p tensor E,
```

where `E` carries its source, Keldysh, boundary, or operator components.

### 2.2 What “exact dependence preservation” would require

For a family of field operations `F_p:E->Y`, define:

```text
NO-INJECTION:
  F_p is independent of p on every p-free input.

NO-DELETION on a declared p-submodule D_p subset A_p tensor E:
  ker(id_(A_p) tensor F) intersect D_p = {0}.

EXACT-PRESERVATION:
  NO-INJECTION plus NO-DELETION, including the admitted tail submodule.
```

For a fixed `p`-blind linear map `F=id_(A_p) tensor F_0`, no injection follows
formally. No deletion does **not** follow: it additionally requires `F_0` to be
injective on the coefficient-carrying vectors. None of the four field
signatures requires that global injectivity.

If the realization itself descends from common-origin state data, its map may
be a family `F_p`. Target independence and freezing before output do not imply
`F_p=F_q`; they forbid tuning to the desired answer, not lawful dependence on a
common input.

### 2.3 Admissible realization, faithfully extracted

For this audit an admissible realization of field `k` means:

1. it has the field-specific P3 signature;
2. it descends on the frozen common-origin trace;
3. it satisfies B1-B14;
4. its physical class, restrictions, and `Tail_R` action are explicitly typed;
5. no downstream output was used to select it.

This definition is not silently strengthened by injectivity or `p`-blindness.
Those would be new clauses.

## 3. Verification of the proposed engine

### 3.1 The battery does mention `p`

The claim that admissibility “never references `p`” is refuted directly:

| Clause | Exact role |
|---|---|
| B2 (`Q-254:503-508`) | requires the finite retarded block to be zero and `p_ch`-independent |
| B3 (`Q-254:510-515`) | requires finite restrictions to stay `p_ch`-free and identifies tail/background as the only remaining entry channels |
| B8 (`Q-254:543-547`) | says the visible `p_ch` quotients are finite-domain objects, not complete outputs |

```text
ADMISSIBILITY_BATTERY_NEVER_MENTIONS_P = false | TYPE-R |
  test: B2, B3, and B8 explicitly name p_ch
```

### 3.2 A parameter-free definition is not a parameter-blind member

The four field signatures are written without choosing a `p` value. That only
establishes family-wide syntax. It does not prove that a common-origin measure,
analytic family, boundary functional, or operator domain is constant over the
state-family parameter.

```text
FIELD_SIGNATURES_SELECT_A_P_VALUE = false | TYPE-S |
  scope: P3 field signatures

FIELD_REALIZATIONS_PROVED_P_INDEPENDENT = false | TYPE-U |
  would-build: a common-origin naturality theorem showing F_[A]=F_[A'] after
               the declared A0/rank change wherever their carriers compare
```

### 3.3 What B1-B3 do prove

Q-279 freezes the entire finite reference tuple, not only its retarded entry:

```text
retarded (delta,c):               0;
noise (delta,delta):              i hbar kappa_eta ell_N tensor ell_N;
mixed (delta,R) and (R,delta):    proportional to kappa_eta;
(R,R):                            proportional to kappa_eta;
equal-history sourced scalar:     1-p+p exp[-Q_N(R)/2].
```

B1 requires reproduction on the same states, histories, orderings, contacts,
boundary data, and domains. B2-B3 forbid a completed restriction from inserting
`p` into the finite retarded block. Therefore:

> **Finite-shadow pattern theorem.** For every completed chain satisfying
> B1-B3 and equipped with the required commuting physical restriction maps,
> its restriction equals Q-279's tuple. It neither inserts `p` into the finite
> retarded block nor removes the exact `p` coefficients from the finite noise,
> probe, and sourced-scalar entries.

Proof: B1 identifies the restricted tuple componentwise with Q-279. Q-279 gives
the component formulas. B2-B3 separately make a different retarded restriction
a battery failure. Componentwise equality gives the result.

```text
FINITE_SHADOW_PATTERN_THEOREM_PROVED = true | TYPE-P |
  premises: DoR-008, B1-B3, Q-279, and instantiated commuting restrictions

FINITE_SHADOW_PATTERN_THEOREM_EXECUTABLE_NOW = false | TYPE-U |
  would-build: P5/P6 physical class and commuting restrictions
```

This conditional theorem is family-level and pre-output. It is not a proof that
each field arrow separately preserves every component.

### 3.4 Why the tail extensions are inside the declared theorem envelope

The countermodels below are models of the **standing admissibility clauses**,
not claims that the missing physical fields have been constructed. Their common
battery account is:

| Battery rows | Countermodel behavior |
|---|---|
| B1-B3 | every added tail term is killed by every finite restriction, so the complete Q-279 finite tuple is unchanged |
| B4 | no naive continuity inference is used; the completion class and tail are declared independently |
| B5 | the countermodel uses a completion larger than the separated norm/left-multiplier class; B5 says class membership must be proved and does not exclude that larger class |
| B6-B7 | `Tail_R` and its action are explicit; finite data determine only the coset |
| B8 | the finite visible `p` quotient is untouched and is not identified with the completed response |
| B9 | no downstream consumer is declared tail-blind; its future factorization remains required |
| B10-B12 | no stationary point or zero-surface identity is introduced |
| B13-B14 | the tail rule is placed in the hypothetical common-origin realization and frozen before output; it is not inferred from finite silence or tuned after a result |

This shows that the present battery does not logically imply the four universal
certificates. It does **not** ratify a tail term: the countermodels remain
hypothetical members used to refute a universal theorem. A future physical
realization may still exclude them by landing in P7's separated class.

## 4. Certificate 1 — measure

### 4.1 Standing admissibility

The measure port requires a branch-joint complex history measure or equivalent
history-event functional, finite marginal consistency, variation control or a
declared extension class, covariance, contour/boundary transformation laws,
quotient descent, and common-origin provenance
(`P3 second attack:257-292`). B1 requires the assembled completed restriction
to reproduce Q-279.

No clause requires integration to be injective on every `p`-carrying germ
component.

### 4.2 Deletion counterexample

Let `(H,Sigma,nu)` be any nontrivial admitted finite measure space and let
`f` be a nonzero integrable function of zero mean. For the symbolic germ output

```text
X_p := p f,
```

the fixed, `p`-blind integration operation gives:

```text
I_nu(X_p)=p integral f dnu=0.
```

Thus a `p`-blind measure operation deletes `p`-dependence. This does not require
a chosen `p`, a target, or a response value. It is the kernel of integration.

Q-278 supplies a concrete related witness: provisional Haar integration
annihilates an appended nontrivial character while identity evaluation
preserves it (`P3 second attack:242-249`). Haar fails the required descended
provenance and is not adopted, but the algebraic witness proves that integration
is not injective. B1 can forbid deletion of the **named Q-279 finite entries**;
it cannot make the measure injective on every germ output.

### 4.3 Tail evasion

If the completed history/response class has a restriction-invisible summand
`T`, two extensions can share every finite marginal:

```text
I_0(x+t)=I_fin(x),
I_1(x+t)=I_fin(x)+L(t),
```

with every finite restriction killing `t`. Taking `t=p t_0` lets `I_0` delete
and `I_1` retain tail dependence. B6-B7 require the tail to be declared; they
do not select one action. B13 requires provenance for a tail-sensitive term;
it does not prove that no common-origin tail action can exist.

For the narrower class of bounded countably additive complex measures on a
sigma-algebra generated by the cylinder sets, equality of all finite cylinder
marginals can determine the measure. The standing interface permits “bounded
total variation **or another declared extension class**” and does not select
that narrower class. Even in the narrower class, integration remains
non-injective on integrands.

```text
MEASURE_UNIVERSAL_NO_INJECTION_NO_DELETION_THEOREM = false | TYPE-R |
  test: nonzero zero-mean p f lies in the kernel of p-blind integration

MEASURE_FINITE_REFERENCE_PATTERN_PRESERVED = true | TYPE-P |
  premises: B1 plus the instantiated measure/restriction square

MEASURE_TAIL_ACTION_FIXED = false | TYPE-U |
  would-build: selected measure class, tail module, and its integration pairing
```

## 5. Certificate 2 — interacting contour / `i epsilon`

### 5.1 Standing admissibility

The contour port requires an epsilon-indexed analytic operator family, its
domain and sign/insertion rule, analytic half-domain, boundary-value map,
common invariant domain, and a limit in a named topology
(`P3 second attack:333-368`). E_post supplies orientation only.

No clause makes a boundary-value or causal-component map injective on the full
Keldysh tensor.

### 5.2 Deletion and block-transfer counterexample

Let the completed Keldysh carrier split into declared components:

```text
E_K = E_(c,c) direct-sum E_(c,delta)
      direct-sum E_(delta,c) direct-sum E_(delta,delta).
```

The ordered retarded extraction is a component map to `E_(delta,c)`. Q-279
places its exact `p` dependence in `E_(delta,delta)` and the `J_delta/R`
components, while `E_(delta,c)=0`. The component projection therefore deletes
the noise-sector dependence from the retarded output. That deletion is the
sealed finite reference, not a defect.

At completion, a fixed `p`-blind analytic boundary map may also send a
`p`-carrying tail component into a retarded tail while every finite restriction
remains zero:

```text
bv(p n_tail)=p t_R,
rho_H,N(t_R)=0 for every N.
```

This transfers existing dependence rather than creating a new scalar
coefficient, but it injects dependence into the **retarded channel** relative
to the finite block. B3 expressly identifies physical tail content as an open
entry route. Conversely `bv(n_tail)=0` deletes it. Both share the same finite
reference until the physical class and tail action are fixed.

```text
CONTOUR_UNIVERSAL_NO_INJECTION_NO_DELETION_THEOREM = false | TYPE-R |
  test: retarded component projection lawfully annihilates the p-carrying
        finite noise component; tail boundary maps can retain or kill p t

CONTOUR_FINITE_REFERENCE_PATTERN_PRESERVED = true | TYPE-P |
  premises: B1-B3 plus an instantiated contour restriction square

CONTOUR_TAIL_BOUNDARY_VALUE_ACTION_FIXED = false | TYPE-U |
  would-build: analytic class, physical tail subspace, boundary-value map, and
               restriction/extraction naturality
```

## 6. Certificate 3 — joint boundary/contact package

### 6.1 Standing admissibility

The boundary port requires the joint completed carrier, preparation/gluing
variation, physical boundary gauge orbit, edge reductions and functionals,
microcausal support, global boundary-form certificate, contacts, and
intertwiners to the exact source and record limits
(`P3 second attack:417-443`).

The signature includes quotients, reductions, null/private removal, and
boundary forms. Such maps are not injective by definition unless a separate
theorem proves injectivity on the relevant submodule.

### 6.2 Evasion

Let `q_bd:E_bd->E_bd/N_bd` be an admitted boundary reduction. If a
restriction-invisible boundary component `t_bd` lies in `N_bd`, then:

```text
q_bd(p t_bd)=0.
```

The operation is fixed and `p`-blind, yet it deletes dependence. If instead an
admitted common-origin boundary/contact map contains

```text
C_bd,p(x)=C_bd,0(x)+p L_bd(x)t_R,
```

with `t_R` in the physical response tail, all finite boundary receipts remain
unchanged while the completed channel acquires dependence. This family is not
asserted physical. It is an evading construction allowed by the current
interface unless B13 provenance and a tail-action theorem exclude it. The
current corpus contains neither exclusion theorem nor physical realization.

B1 prevents either behavior from altering the named Q-279 finite tuple. It does
not determine boundary-null or contact content invisible to all restrictions.

```text
BOUNDARY_UNIVERSAL_NO_INJECTION_NO_DELETION_THEOREM = false | TYPE-R |
  test: p-blind boundary quotient annihilates p t_bd; an explicit common-origin
        tail contact can change only the completed channel

BOUNDARY_FINITE_REFERENCE_PATTERN_PRESERVED = true | TYPE-P |
  premises: B1 plus instantiated boundary/contact restriction squares

BOUNDARY_TAIL_AND_NULL_ACTION_FIXED = false | TYPE-U |
  would-build: physical null/private subspace, contact map, tail action, and
               injectivity/factorization result on the declared p-submodule
```

## 7. Certificate 4 — unbounded generators and domains

### 7.1 Standing admissibility

The domain port requires named unbounded operators on the completed physical
representation, a common dense invariant core, symmetry and closability,
self-adjoint or closed-extension certificates, gauge invariance, boundary form,
and glue preservation (`P3 second attack:445-501`). No unbounded operator is
currently instantiated.

Agreement on a dense core does not uniquely determine every closed extension
without essential self-adjointness or an equivalent uniqueness theorem.

### 7.2 Evasion

Let `D_0` be the finite/core domain and let a symmetric operator `A_0` admit
two closed extensions `A^(1)` and `A^(2)` with the same action on `D_0`. Let a
boundary coordinate of the extension domain carry the common-origin symbolic
weight `p`. Then the two extensions can have:

```text
rho_N(A^(1))=rho_N(A^(2)) for every N,

A^(1)(p t_dom)=0,
A^(2)(p t_dom)=p t_R,
```

on an added response-tail direction. The notation records the only property
needed for the countermodel: identical core restrictions and different closure
action. It does not assert a physical operator or choose a self-adjoint
extension.

Alternatively, restricting the physical domain to a subspace that excludes
`p t_dom` deletes the dependence while remaining `p`-blind. Dense-core
agreement cannot distinguish these cases.

```text
DOMAIN_UNIVERSAL_NO_INJECTION_NO_DELETION_THEOREM = false | TYPE-R |
  test: distinct closures/extensions agree on the finite core but retain or
        annihilate a p-carrying tail/domain direction

DOMAIN_FINITE_REFERENCE_PATTERN_PRESERVED = true | TYPE-P |
  premises: B1 plus instantiated operator/domain restriction squares

DOMAIN_EXTENSION_AND_TAIL_ACTION_FIXED = false | TYPE-U |
  would-build: named operators, essential-self-adjointness/unique-closure
               theorem or complete extension family, and tail action
```

## 8. Family-level theorem that does survive

The four refutations share one boundary and leave one useful theorem.

Define the completed field chain:

```text
F_chain := F_domain compose F_boundary compose F_contour compose F_measure,
```

with the actual order adjusted to the future P3/P5 interfaces and every arrow
typed. Suppose:

1. B1-B3 hold;
2. each physical restriction square exists;
3. the restricted chain is exactly the Q-279 finite construction; and
4. the comparison preserves the whole finite tuple, not only the retarded
   component.

Then:

```text
rho_N(F_chain(X_p)) = FiniteNonzeroRRef_N(p)
```

componentwise. Therefore all four full realizations jointly preserve the exact
finite `p`-pattern. This is immediate from the commuting squares and Q-279.

```text
JOINT_END_TO_END_FINITE_PATTERN_CERTIFICATE_PROVED = true | TYPE-P |
  premises: B1-B3 and instantiated restriction squares

PER_FIELD_FULL_INJECTIVITY_FOLLOWS_FROM_JOINT_FINITE_PATTERN = false | TYPE-R |
  test: kernels can cancel or act only in Tail_R while the composite finite
        restriction remains fixed
```

This is exactly why the replacement certificate must record the kernel and
tail action of each arrow rather than demand universal preservation.

## 9. Correct replacement for item (a)

For each field `F_k`, the build must emit:

```text
DEP_ACCOUNT_k := (
  carrier and codomain,
  p-parameter action: fixed F or family F_[A],
  declared p-bearing input submodules,
  kernel on each such submodule,
  image and any sector transfer,
  physical tail domain and tail action,
  finite restriction maps,
  commuting restriction square,
  Q-279 full-tuple reproduction,
  common-origin provenance,
  target-independence certificate
).
```

The acceptance rule is not “kernel equals zero everywhere.” It is:

1. no undeclared `p` coefficient appears;
2. every deletion or sector transfer is explicit;
3. the Q-279 finite tuple is reproduced componentwise;
4. every tail action is typed and sourced;
5. the selected downstream consumer receives a declared `p`-dependence
   signature.

```text
CORRECT_ITEM_A_OBJECT = FOUR_ARROW_DEPENDENCE_ACCOUNTING_PACKAGE
CORRECT_ITEM_A_OBJECT_EXISTS = false | TYPE-U |
  would-build: the four DEP_ACCOUNT_k instances on P5/P6's physical class and
               restrictions
```

This replacement does not author any of the four fields. It fixes the theorem
that their future realizations must prove.

## 10. Tail and scope accounting

### 10.1 `Tail_src` versus `Tail_R`

P2 V002 proves `Tail_src=Tail_germ={0}` in the ratified norm source topology.
That prevents a source increment from hiding by moving to later cells. It does
not constrain a response-level completion after measure, inversion, contour,
boundary, and domain operations.

```text
TAIL_SRC_ZERO_IMPLIES_TAIL_R_ZERO = false | TYPE-R |
  test: distinct source and response carriers; P5/P6 class transport absent
```

### 10.2 Response tail is the common evasion

Q-250 proves only:

```text
completed response determined modulo Tail_R.
```

For every field above, the universal certificate fails on either an ordinary
kernel already present at finite level or an untyped action on `Tail_R`.

```text
TAIL_R_EVASION_CLOSED_FOR_ANY_OF_FOUR_FIELDS = false | TYPE-U |
  would-build: P5/P6 plus DEP_ACCOUNT_measure/contour/boundary/domain
```

### 10.3 Background and output boundaries

This artifact does not touch Q-280 items (b) and (c):

```text
(b) common-origin stationary-background map;
(c) selected output-consumption/factorization signature.
```

Even a completed four-arrow accounting package would leave both necessary.

```text
BACKGROUND_MAP_DISCHARGED_HERE = false | TYPE-S |
  scope: four P3 operations only

OUTPUT_CONSUMPTION_SIGNATURE_DISCHARGED_HERE = false | TYPE-S |
  scope: four P3 operations only
```

## 11. Kill-passes

### 11.1 No dense-core overclaim

The finite theorem is explicitly a theorem about physical restrictions. It is
not promoted to a full-realization theorem. Every full certificate faces the
tail countermodel.

### 11.2 No unbuilt value used

No measure, contour, boundary functional, unbounded operator, domain, or tail
value is selected or evaluated. Countermodels use only structural kernels,
quotients, and extensions.

### 11.3 No “p-blind implies injective” fallacy

Parameter-blindness prevents coefficient creation only for a fixed map. It
does not make the map injective, prevent block transfer, or prove that a
common-origin family is constant over `[A]`.

### 11.4 No retarded/noise conflation

The exact finite retarded block and the `p`-carrying noise/`J_delta-R` blocks
remain distinct. The fact that the former omits dependence is not described as
deletion from the full generating functional.

### 11.5 No physical tail assertion

The evading `Tail_R` constructions refute derivability from the present
constraints. They do not prove that a physical response tail exists. That
existence remains `NO_VERDICT` until P5/P6 instantiate the class and maps.

## 12. Final typed ledger

```text
ADMISSIBILITY_BATTERY_NEVER_MENTIONS_P = false | TYPE-R
FIELD_SIGNATURES_SELECT_A_P_VALUE = false | TYPE-S
FIELD_REALIZATIONS_PROVED_P_INDEPENDENT = false | TYPE-U

MEASURE_UNIVERSAL_NO_INJECTION_NO_DELETION_THEOREM = false | TYPE-R
CONTOUR_UNIVERSAL_NO_INJECTION_NO_DELETION_THEOREM = false | TYPE-R
BOUNDARY_UNIVERSAL_NO_INJECTION_NO_DELETION_THEOREM = false | TYPE-R
DOMAIN_UNIVERSAL_NO_INJECTION_NO_DELETION_THEOREM = false | TYPE-R

FULL_CERTIFICATES_PROVED = 0
FULL_CERTIFICATES_REFUTED = 4

FINITE_SHADOW_PATTERN_THEOREM_PROVED = true | TYPE-P |
  premises: DoR-008, B1-B3, Q-279, instantiated commuting restrictions
FINITE_SHADOW_PATTERN_THEOREM_EXECUTABLE_NOW = false | TYPE-U

JOINT_END_TO_END_FINITE_PATTERN_CERTIFICATE_PROVED = true | TYPE-P |
  premises: B1-B3 and instantiated restriction squares
PER_FIELD_FULL_INJECTIVITY_FOLLOWS = false | TYPE-R

TAIL_SRC_ZERO = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
TAIL_R_EXISTS_AS_A_PHYSICAL_NONZERO_SPACE = NO_VERDICT
TAIL_R_EVASION_CLOSED = false | TYPE-U

CORRECT_ITEM_A_OBJECT = FOUR_ARROW_DEPENDENCE_ACCOUNTING_PACKAGE
CORRECT_ITEM_A_OBJECT_EXISTS = false | TYPE-U
ITEM_A_DISCHARGED = false | TYPE-U

BACKGROUND_MAP_DISCHARGED_HERE = false | TYPE-S
OUTPUT_CONSUMPTION_SIGNATURE_DISCHARGED_HERE = false | TYPE-S

FENCE_BLOCKED_STRUCTURAL_RESULT = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The verdict-chain boundary after this audit is exact: Q-279 supplies the full
finite pattern; future P3-P6 work must account for how each arrow moves or
annihilates that pattern and any response-tail component. A universal
preservation slogan cannot replace those arrow-level certificates.
