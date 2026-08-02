# Stage 8 Task 4a P2 Physical Source Topology and Differential Calculus Construction V002 -- Supersedes V001 per Q-276

Date: 2026-08-02  
Task: 4a / P2  
Status: CERTIFIED CONSTRUCTION ON RATIFIED PREMISES

Marks on every premise-dependent positive:

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013, DoR-014
```

Gates: `alpha_computed=false`; `proof_authorized=false`;
`kappa_record_computed=false`.

## 0. Lead determination

**P2 builds without a residual topology choice.** DoR-014 ratified the V004
germ, including C-A's source carrier

```text
E_src = ell^1(N)_+ direct-sum ell^1(N)_-
        direct-sum S_1,sym(H_CTP),
```

its sum norm, and complex Fréchet calculus. P2 instantiates those fields,
proves the finite cylindrical subspace norm-dense, proves coordinate
restrictions continuous and convergent, and supplies continuous first,
second, mixed, and higher Fréchet derivatives on the exported germ.

The Q-245 moving-tail obstruction is not hidden. A source translated to a new
cell at each stage has fixed `ell^1` norm and does not converge to zero in
`topology_src`; its bilocal trace-class analogue likewise has fixed trace
norm. Hence it produces no completion point and no source-tail element. Every
actual member of `E_src`, by contrast, converges under finite truncation.

The resulting norm-class source and germ tails are zero. This does **not**
prove the future physical response tail `Tail_R` zero and does not type
`RetHess_phys`; those remain P5/P6 obligations.

```text
P2_TOPOLOGY_SRC_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P2_DIFF_SRC_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P2_FINITE_SOURCE_CORE_DENSE = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P2_RESIDUAL_INEQUIVALENT_TOPOLOGY_FREEDOM = false | TYPE-P |
  premises: DoR-014; test: C-A was ratified as part of SOURCE_GERM_PHYS V004
P2_STATUS = BUILT
```

P3 can immediately consume the source carrier, topology, truncations, and
calculus. P4 can consume the analytic source half of `PhysicalLogGerm`. P5 can
pose the source derivatives and finite Keldysh instances. None receives a
measure, contour, physical quotient, response class, or retarded extraction
from P2.

## 1. Scope, currency, and controlling signatures

### 1.1 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha_supervision
```

Exclusions:

```text
a32_holdout/custodian_private/                  NOT ENTERED
response/kernel/root/coupling evaluation        NOT PERFORMED
measured-constant comparison                    NOT PERFORMED
register, plan, tracker, git, commit, push       NOT TOUCHED
```

### 1.2 Authorities

| Authority | Controlling content |
|---|---|
| `DECISION_OF_RECORD_014_SOURCE_GERM_PHYS_RATIFIED_2026-08-02_V001.md:4-27` | V004 germ, ordered-rank family, C-A/C-B, and analytic interfaces ratified |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md` (`d4cdbb66...`) | exact germ and rank-family discipline |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V001.md:200-220,342-463` | explicit C-A topology, calculus, truncation, and germ class inherited through V004 |
| `STAGE8_TASK4A_MISSING_PHYSICAL_LAYER_CONSOLIDATED_SPEC_AND_CONSTRAINT_BATTERY_V001.md:206-228,453-485` | P2 contract and consumer order |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_ITEM2_PHYSICAL_LOG0_GERM_SPEC_V001.md:237-316` | P4 input and `PhysicalLogGerm` signatures |
| `STAGE8_TASK4A_CORRELATOR_COMPLETION_ARROW_AND_RESTRICTION_PINNING_DETERMINATION_V001.md:359-449,491-540` | Q-245 moving-tail attack and separation requirements |
| `STAGE8_TASK4A_FINITE_RESTRICTION_SEPARATION_AND_BIDUAL_TAIL_DETERMINATION_V001.md:295-379,460-574` | Q-247 norm separation and bidual-tail boundary |
| `STAGE8_TASK4A_PHYSICAL_RESPONSE_CLASS_SEALED_SIGNATURE_DETERMINATION_V001.md:270-324,451-501` | P5 source-class and response-class signatures |

DoR-014 is current through Q-272. Its rank discipline is binding: every
construction below is uniform in the ordered positive integer pair
`(r_0,r_ch)`. No pair is selected and no symbolic ratio is evaluated.

## 2. P2 contract and consumer signatures

### 2.1 P2 must provide

Q-254 defines P2 by the fields

```text
D_src, 0_src, topology_src, Diff_src, Reg_D1.
```

It requires first and second source derivatives and an independent
symmetric-`R` derivative domain. The topology must define open neighborhood,
continuity, convergence, density/core, and the class in which restriction and
differentiation occur.

P2's complete output signature is therefore

```text
P2_SOURCE_CALCULUS :=
  (D_src,0_src,E_src,topology_src,
   E_src^fin,{rho_src,N},{iota_src,N},
   Diff_src,Reg_D1,Reg_D2,
   source_core_certificate,
   restriction_derivative_naturality_certificate,
   source_tail_certificate).
```

### 2.2 P3 consumer

Q-254 `:229-244` requires P3 to construct the physical prequotient/quotient,
measure, contour, boundary/contact data, domains, and provenance. P3 consumes:

```text
(D_src,topology_src,finite source core,rho_src,N,Diff_src)
```

to state continuity, measurability, quotient descent, contour domains, and
closability. P2 supplies none of P3's measure or contour content.

### 2.3 P4 consumer

The Item-2 specification gives

```text
PhysicalLogGerm =
  [(N,Z_inc|N,Log_0,W_inc,Reg_req,provenance)]_0_src,
```

where `N` is open in `topology_src`, `Reg_req` is expressed in `Diff_src`, and
the first `J` and symmetric-`R` derivatives must exist
(`STAGE8_CTP_PHYS_INPUT_PACKAGE_ITEM2_PHYSICAL_LOG0_GERM_SPEC_V001.md:281-316`).

P2 supplies the topology/calculus and analytic regularity leg. P3 must still
supply the physical quotient, measure, contour, boundary domains, and their
provenance before the full physical P4 tuple closes.

### 2.4 P5 consumer

The class package requires

```text
(topology_src,Diff_src,RetHess_phys,topology_RetHess,
 physical rho_H,N,finite-core statement,
 contour/boundary completion class,
 inversion/extraction square,stationary-background class).
```

P2 supplies the first two entries and the source-side core theorem. It also
makes the raw `J`, symmetric-`R`, second, and Keldysh mixed derivatives
well-posed. It does not construct `RetHess_phys`, its topology, or the physical
restriction maps.

## 3. Construction of `topology_src`

### 3.1 Carrier and norm

For every rank class `[A]`, let

```text
H_cell := ell^2(N),
E_J    := ell^1(N)_+ direct-sum ell^1(N)_-,
E_R    := S_1,sym(H_CTP),
E_src  := E_J direct-sum E_R,

||(J_+,J_-,R)||_src
  := ||J_+||_1+||J_-||_1+||R||_1,trace.
```

`S_1,sym` is the closed trace-class subspace obeying the ratified branch and
source symmetry. The finite branch index and CTP tensor factors do not change
trace-class completeness.

Define

```text
D_src := {+1,-1} cross E_src,
0_src := (n,0,0,0) on each n component,

topology_src :=
  discrete topology on {+1,-1}
  times the Banach norm topology of E_src.
```

This is `TYPE-P | premises: DoR-008, DoR-009, DoR-013, DoR-014`.
The rank pair affects only the scalar coefficient inherited through the A0
gauge class; it does not change `E_src` or its topology.

### 3.2 Finite stages, restrictions, and zero extensions

Let `P_N` be the coordinate projection onto the first `N` cell labels. Define

```text
E_src,N :=
  P_N ell^1_+ direct-sum P_N ell^1_-
  direct-sum P_N S_1,sym(H_CTP) P_N,

rho_src,N(J_+,J_-,R)
  :=(P_N J_+,P_N J_-,P_N R P_N),

iota_src,N:E_src,N -> E_src
  := zero extension,

rho_src,N iota_src,N = id_(E_src,N).
```

Both maps are linear contractions; `iota_src,N` is isometric. Sequentially,

```text
rho_src,N iota_src,M rho_src,M = rho_src,N      for N<=M,
iota_src,N = iota_src,M iota_(N->M)            for N<=M.
```

For `J in ell^1`, coordinate truncation converges in `ell^1`. For trace-class
`R`, finite-rank compressions converge in trace norm when `P_N` increases
strongly to the identity. Hence

```text
||iota_src,N rho_src,N(s)-s||_src -> 0
```

for every `s in E_src`.

Define

```text
E_src^fin := union_N iota_src,N(E_src,N).
```

Then `E_src^fin` is norm dense in `E_src`. This is the P2
`SOURCE_CORE_CERT` required by P7's later composition theorem.

### 3.3 Determination and choice table

| Candidate | Standing in P2 | Reason and void condition |
|---|---|---|
| C-A sum-norm topology | **RATIFIED / TYPE-P** | DoR-014 adopted V004 including C-A. Voids if a sealed finite restriction fails, finite sources cease to be dense/continuous, or P3 proves its lawful operations cannot act on this domain. |
| max norm on the same finite direct sum | **EQUIVALENT PRESENTATION** | Sum and max norms are equivalent on the three-factor finite direct sum and generate the same topology; no physical choice. |
| compact-spectrum product topology | **REFUTED FOR THE SCALAR GERM / TYPE-R** | Q-245 moving-tail sequence makes the scalar amplitude and accumulated-phase covector discontinuous. |
| strict finite-support inductive-limit topology | **NOT AN ADMITTED P2 COMPLETION / TYPE-P BOUNDARY** | DoR-014 adopted the completed C-A Banach source family; finite support is retained as its dense core, not substituted for it. |
| weighted `ell^1`, `ell^2`, Sobolev, distributional, weak-star, or bidual completion | **OUTSIDE RATIFIED P2 / TYPE-S** | these classes are absent from the DoR-014 P2 source family; admitting one would be a new premise with its own gate and tail theorem. |

Thus no inequivalent topology choice remains **within the ratified P2
construction**. This is premise-level determination, not a claim that abstract
mathematics admits only one topology on finite-support sequences.

```text
TOPOLOGY_SRC_DETERMINED_BY_DOR014 = true | TYPE-P |
  premises: DoR-014
TOPOLOGY_SRC_DERIVED_WITHOUT_AUTHORED_PREMISE = false | TYPE-R |
  test: C-A entered through ratification, not an upstream uniqueness theorem
P2_ADMITS_NEW_TOPOLOGY_CHOICE = false | TYPE-P |
  premises: DoR-014
```

## 4. Moving-tail and source-tail adjudication

### 4.1 Linear moving tail

Let `e_m` be the source direction supported on cell `m`. In the compact
product topology Q-245 has `e_m -> 0` coordinatewise while the accumulated
phase covector remains nonzero. In `topology_src`,

```text
||e_m||_1 = constant,
||e_m-e_n||_1 = constant for m!=n.
```

No value is needed: the norms are bounded away from zero. Thus `(e_m)` does
not converge to zero and is not Cauchy. The Q-245 countersequence has no
`E_src` completion point.

### 4.2 Bilocal moving tail

Let `R_m` be a fixed nonzero rank-one symmetric bilocal source translated to
cell `m`. Its trace norm is independent of `m`, and distinct orthogonal
translations remain separated in trace norm. Hence `(R_m)` likewise produces
no trace-class tail limit.

### 4.3 What the tail is in this topology

For vectors,

```text
intersection_N ker(rho_src,N) = {0}.
```

For continuous linear functionals and bounded multilinear forms, vanishing on
every `E_src,N` implies vanishing on dense `E_src^fin`, hence everywhere.
For norm-continuous or norm-holomorphic germs, a germ vanishing on every
finite-support neighborhood vanishes on the full neighborhood by continuity.

Define the source/germ restriction tail in this class by

```text
Tail_src := intersection_N ker(rho_src,N),

Tail_germ :=
  {f in the ratified norm-holomorphic germ class:
   f vanishes on every finite-support source neighborhood}.
```

Then

```text
Tail_src={0},
Tail_germ={0}.
```

These are `TYPE-P | premises: DoR-008, DoR-009, DoR-013, DoR-014`.

The result is deliberately not transported to P5/P6:

```text
TAIL_SRC_IDENTIFIED_WITH_PHYSICAL_TAIL_R = false | TYPE-R |
  test: Tail_src is a source-vector kernel; Tail_R is a future retarded-operator
        restriction kernel with different domain and codomain
PHYSICAL_TAIL_R_ZERO = NO_VERDICT |
  prerequisite: RetHess_phys and physical rho_H,N
```

The Q-247 bidual tail is excluded from P2's source class, not disproved. If P5
later admits bidual/distributional response content, its separate tail theorem
still applies.

## 5. Construction of `Diff_src`

### 5.1 Calculus

On each discrete character component of `D_src`, define `Diff_src` to be
complex Fréchet differentiation on the Banach space `E_src`. For
`f:U subset E_src -> F` and `s in U`,

```text
D f(s)=L
```

means `L` is bounded complex-linear and

```text
||f(s+h)-f(s)-Lh||_F / ||h||_src -> 0.
```

Higher derivatives are iterated continuous Fréchet derivatives,

```text
D^k f(s) in L_sym^k(E_src;F).
```

Admissible directions are all of `E_src`. The independent source subspaces are

```text
E_J^+,
E_J^-,
E_J,c,
E_J,delta,
E_R,sym.
```

The sealed Keldysh common/difference transform is a bounded linear
automorphism on the two `ell^1` branch factors and, by finite branch-index
congruence, on `S_1,sym`. Hence all common, difference, `J`, `R`, mixed, and
second derivatives are instances of one calculus.

### 5.2 Chain rules and regularity

`Diff_src` carries the standard Banach-space chain, product, inverse-on-open-
set, exponential, and holomorphic logarithm rules. In the ratified germ,

```text
Xi_n[J,R]=L_n^Theta(J)-(1/2)Q_delta^Theta(R)
```

is bounded linear; therefore `exp(Xi_n)` and `Z_inc` are entire on `E_src`.
On the ratified nonzero neighborhood, `Log_0 Z_inc` and
`W_inc=-i hbar Log_0 Z_inc` are holomorphic.

Freeze the profiles

```text
Reg_D1 :=
  first J derivative plus first independent symmetric-R derivative,

Reg_D2 :=
  all second J/J, J/R, and R/R Fréchet derivatives needed to pose raw
  correlator and Keldysh block extraction,

Reg_Dk :=
  bounded symmetric k-linear derivatives on norm-bounded subneighborhoods.
```

The calculus supplies these derivative types. It does not assert that every
formal derivative is already a physical correlator; P3/P4 provenance remains
load-bearing.

### 5.3 Exported formulas

Uniformly over the ordered-rank family, write the inherited symbolic
coefficient as `p_[A]`. Then

```text
D Z_inc[J,R](j,r)
  =p_[A] exp(Xi_n[J,R])
    [L_n^Theta(j)-(1/2)Q_delta^Theta(r)],

D_R Z_inc[J,R](r)
  =-(p_[A]/2)exp(Xi_n[J,R])Q_delta^Theta(r),

D Log_0 Z_inc
  =[p_[A]exp(Xi_n)/Z_inc]D Xi_n.
```

No rank pair is selected and no coefficient is evaluated.

### 5.4 Restriction/derivative naturality

For the finite-stage germ

```text
Z_inc,N:=Z_inc compose iota_src,N,
```

the Banach chain rule gives, for all finite directions `h_1,...,h_k`,

```text
D^k Z_inc,N(s_N)[h_1,...,h_k]
 =D^k Z_inc(iota_src,N s_N)
    [iota_src,N h_1,...,iota_src,N h_k].
```

The same identity holds for `Log_0` and `W_inc` wherever their common nonzero
neighborhood is admitted. Thus finite differentiation is the restriction of
the completed germ differentiation, not a fitted proxy.

## 6. Q-243 finite mixed-derivative embedding

At `R=0`, restrict to any finite stage and apply the bounded Keldysh transform.
Because the germ agrees with the sealed finite amplitude, its first and second
derivatives agree with the Q-243 finite derivatives by the naturality identity
above. The second derivative has rank-one branch-difference form

```text
D^2 Log_0 Z_inc|_0
  =-p_[A](1-p_[A]) ell_delta tensor ell_delta,
```
Correction: the leading minus sign is required by Q-276, `STAGE8_TASK4A_P2_FOUNDATION_CROSS_VERIFICATION_DETERMINATION_V001.md` (`78970c69...`).

where `ell_delta` is the finite accumulated difference-source covector. The
Keldysh transform therefore places the finite Hessian in the
difference/difference block; the ordered mixed retarded block remains the
sealed zero.

This is a structural embedding, not a response evaluation:

```text
Q243_FINITE_DERIVATIVES_EMBED_IN_DIFF_SRC = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
Q243_FINITE_RETHESS_IDENTIFIED_WITH_PHYSICAL_RETHESS = false | TYPE-R |
  test: P5 response class and extraction map are unbuilt
```

## 7. Battery certificates bearing on P2

| Battery item | Verdict | P2 certificate |
|---|---|---|
| B1 finite-restriction reproduction | **PASS / TYPE-P** | contractive `rho_src,N`, isometric zero extension, norm convergence, and derivative naturality reproduce all executable scalar finite restrictions uniformly over rank classes. |
| B2 finite retarded baseline | **PASS / TYPE-P** | Q-243 finite derivatives embed and retain the difference/difference block. |
| B3 finite restrictions `p_ch`-free in retarded block | **PASS / TYPE-P** | the source calculus carries the rank parameter symbolically; finite ordered retarded block remains zero. |
| B4 no naive continuous extension | **PASS / TYPE-P** | product topology is not used; moving-tail sequences do not converge in the C-A norm. |
| B5 named separation class | **PASS FOR SOURCE/Germ CLASS ONLY** | `E_src`, its continuous dual/multilinear classes, and norm-holomorphic germ class are named and separated. Physical `RetHess_phys` remains TYPE-U. |
| B6 explicit tail | **PASS FOR SOURCE/Germ CLASS ONLY** | `Tail_src=Tail_germ={0}`; no identity with physical `Tail_R`. |
| B13 finite authority | **PASS / TYPE-P** | finite sources form a dense core and every germ derivative is determined by its finite restrictions. |

```text
P2_BATTERY_CERTIFICATE = PASS_ON_P2_SCOPE
PHYSICAL_RESPONSE_SEPARATION_DISCHARGED_BY_P2 = false | TYPE-U |
  would-build: P5 RetHess_phys class and P6 physical restrictions
```

## 8. Consumer readiness and residual freedoms

### 8.1 P3

```text
P3_SOURCE_TOPOLOGY_INPUT_READY = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P3_MEASURE_CONTOUR_QUOTIENT_BOUNDARY_READY = false | TYPE-U |
  would-build: P3a-P3f physical package
```

P3 may now construct and test its quotient, measure, contour, boundary/contact,
and domain maps on a fixed source Banach carrier. P2 supplies no measure.

### 8.2 P4

```text
P4_ANALYTIC_SOURCE_HALF_READY = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_FULL_PHYSICAL_LOG_GERM_READY = false | TYPE-U |
  would-build: P3 quotient/measure/contour/boundary provenance
```

The ratified nonzero neighborhood, anchored logarithm, and all required source
derivatives now have a certified topology/calculus.

### 8.3 P5

```text
P5_SOURCE_DERIVATIVE_CALCULUS_READY = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P5_RETHESS_CLASS_AND_EXTRACTION_READY = false | TYPE-U |
  would-build: P3/P4 physical package, raw G, inverse, RetHess_phys class,
               and retarded extraction/restriction square
```

### 8.4 Residual choice ledger

```text
P2_TOPOLOGY_CHOICE_REMAINS = false | TYPE-P |
  premises: DoR-014
P2_CALCULUS_CHOICE_REMAINS = false | TYPE-P |
  premises: DoR-014
P2_MEASURE_SELECTED = false | TYPE-S |
  scope: P2 output fields
P2_CONTOUR_SELECTED = false | TYPE-S |
  scope: P2 output fields
P2_SPECIFIC_RANK_PAIR_SELECTED = false | TYPE-S |
  scope: all definitions and proofs are family-wide
```

## 9. Mandatory kill passes

### 9.1 Rank selection

Every formula is indexed by `[A]` or is independent of the rank pair. No
ordered pair is instantiated. The topology and derivative bounds do not depend
on rank values.

### 9.2 Smuggled measure or contour

The trace norm and operator trace used to define the bilocal source functional
are Banach-operator data already ratified in C-A/C-B. They are not a spacetime,
contour, path-integral, or probabilistic measure. P3's measure and contour slots
remain explicitly unbuilt.

### 9.3 Verdict-tuned topology

The topology is used because DoR-014 ratified it before P2 construction. It is
not chosen here to make a stationary point, response, tail, or cancellation
verdict hold. The only tail theorem claimed is the direct density theorem in
the ratified norm class.

### 9.4 Bidual transport

No Q-247 norm separation statement is transported to bidual or distributional
classes. Conversely, Q-247's bidual counterexample is not imported as a source
tail because P2 admits no bidual completion.

```text
RANK_VALUE_SELECTION_FOUND = false | TYPE-S |
  scope: P2 construction
SMUGGLED_MEASURE_FOUND = false | TYPE-S |
  scope: P2 construction
SMUGGLED_CONTOUR_FOUND = false | TYPE-S |
  scope: P2 construction
DOWNSTREAM_VERDICT_TUNING_FOUND = false | TYPE-S |
  scope: P2 topology provenance precedes P3-P5 outputs
UNPROVED_NORM_TO_BIDUAL_TRANSPORT_FOUND = false | TYPE-S |
  scope: P2 class statements
P2_SURVIVES_MANDATORY_SELF_KILL = true
```

## 10. Final typed ledger

```text
P2_EXISTS = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

TOPOLOGY_SRC =
  discrete({+1,-1}) x norm(E_src)
DIFF_SRC = complex_Frechet(E_src)
REG_D1 = first_J plus first_symmetric_R
REG_D2 = second_JJ_JR_RR_and_Keldysh_instances

FINITE_SOURCE_CORE_DENSE = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
SOURCE_RESTRICTIONS_CONTINUOUS = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
DIFFERENTIATION_COMMUTES_WITH_FINITE_RESTRICTION = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

TAIL_SRC_ZERO = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
TAIL_GERM_ZERO = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
TAIL_R_ZERO = NO_VERDICT

P3_CAN_START = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_ANALYTIC_SOURCE_HALF_CAN_START = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P5_SOURCE_DERIVATIVE_SIDE_CAN_START = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

P2_MEASURE_BUILT = false | TYPE-S |
  scope: P2 contract; measure belongs to P3
P2_CONTOUR_BUILT = false | TYPE-S |
  scope: P2 contract; contour belongs to P3
P2_PHYSICAL_RETHESS_BUILT = false | TYPE-U |
  would-build: P5 response class and extraction package

alpha_computed = false [TERMINAL FENCE DECLARATION]
proof_authorized = false [TERMINAL FENCE DECLARATION]
kappa_record_computed = false [TERMINAL FENCE DECLARATION]
```
