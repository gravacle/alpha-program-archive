# STAGE8 TASK 4A MISSING PHYSICAL LAYER — CONSOLIDATED SPECIFICATION AND CONSTRAINT BATTERY V001

**Status:** `SEALED REPORT — CONSOLIDATION ONLY; NO PHYSICAL OBJECT IS PROMOTED OR ADOPTED HERE`

**Gates:**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Headline determination

The minimal shared package that can decide whether `p_ch` cancels or survives in
one chosen complete physical-response channel is **smaller than the full missing
physical layer**. It consists of eight top-level packages:

```text
M1  SOURCE_GERM_PHYS with one common-origin pointwise Z_inc[J,R]
M2  physical source topology and differential calculus
M3  complete U3 physical input package
M4  PhysicalLogGerm
M5  raw-G / inverse-Hessian / RetHess physical realization
M6  paired finite-to-physical and physical-to-finite comparison maps
M7  common-origin stationary-background package
M8  exactly one alpha-facing consumption package
```

Its shape is:

```text
AUTHORED-PHYSICS-SHAPED  1 package:  M1
THEOREM-SHAPED           2 packages: M2, M4
CONSTRUCTION-SHAPED      4 packages: M5, M6, M7, M8
MIXED COMPOSITE          1 package:  M3
```

`M3` is mixed because its quotient, measure, contour, and boundary realization
are construction-shaped, while its common-domain and common-origin-provenance
certificates are theorem-shaped. These labels identify the kind of work needed;
they do **not** assert existence or authorize adoption.

The single authored object shared by both the tail and background channels is
the complete common-origin scalar physical functional in `M1`. The ratified
finite law and amplitudes do not supply it. All later constructions consume it.
Thus the next commissioning decision is not the whole sixteen-row layer at
once: it is `M1`, followed by the theorem/construction chain for one selected
consumer.

The full consolidated layer contains eleven top-level packages and sixteen
canonical rows after expanding `U3`. The three packages omitted from the minimal
single-channel target are:

```text
P7  an object-side finite-core / separation / T5 theorem (optional when the
    chosen output instead proves its own Tail_R factorization),
P9  the local-projection consumer when another channel is chosen, and
P11 the complete Thomson/Q_spec consumer when another channel is chosen.
```

No claim in this report decides `p_ch`, constructs a response, or evaluates any
quantity.

## 1. Authority and scope

### 1.1 Current chain read end to end

| Register row | Artifact | Role in this consolidation |
|---|---|---|
| Q-239 | `STAGE8_CTP_PHYS_INPUT_PACKAGE_U3_DOR008_DOR009_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` | five open U3 fields and finite skeleton |
| Q-245 | `STAGE8_TASK4A_CORRELATOR_COMPLETION_ARROW_AND_RESTRICTION_PINNING_DETERMINATION_V001.md` | `SOURCE_GERM_PHYS`, physical restriction maps, separation preconditions |
| Q-249 | `STAGE8_TASK4A_PHYSICAL_RESPONSE_CLASS_SEALED_SIGNATURE_DETERMINATION_V001.md` | `PHYSICAL_RETHESS_CLASS_AND_RESTRICTION_PACKAGE` |
| Q-250 | `STAGE8_TASK4A_RESPONSE_CLASS_FORCING_AND_TAIL_OUTPUT_INERTNESS_DETERMINATION_V001.md` | exact modulo-tail theorem and two lawful discharge routes |
| Q-251 | `STAGE8_TASK4A_ALPHA_FACING_OUTPUT_TAIL_ANNIHILATION_THEOREM_DETERMINATION_V001.md` | six consumer rows, all consumption specifications absent |
| Q-252 | `STAGE8_TASK4A_BACKGROUND_CHANNEL_STATIONARY_EVALUATION_POINT_DETERMINATION_V001.md` | background pair, pullback map, complete Thomson functional |

The constraint battery also reads the two standing results it is expressly
required to preserve:

| Register row | Artifact | Binding result |
|---|---|---|
| Q-243 | `STAGE8_TASK4A_FINITE_HESSIAN_TO_DELTAPHI_TRANSPORT_MAP_CONSTRUCTION_AND_P_CH_TRACE_V001.md` (`70185aa8...`) | the exact finite retarded block is zero and `p_ch`-free (`:329-342`, `:479-495`) |
| Q-247 | `STAGE8_TASK4A_FINITE_RESTRICTION_SEPARATION_AND_BIDUAL_TAIL_DETERMINATION_V001.md` (`60b5b4c5...`) | separation on ratified norm/module/left-multiplier classes, failure on the bidual, physical transport withheld (`:409-453`, `:481-566`, `:608-625`) |

Direct supporting specifications were also read where the six artifacts route
to them:

```text
STAGE8_CTP_PHYS_INPUT_PACKAGE_ITEM2_PHYSICAL_LOG0_GERM_SPEC_V001.md
STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md
primitive_record_cell_selection_principle_v004.md
BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md
```

**Post-prompt currency check:** the register advanced once, to Q-253, while
this consolidation was in progress. Its artifact,
`STAGE8_TASK4A_BIND_INPUT_SIGNATURE_AND_DOMAIN_TAIL_BLINDNESS_DETERMINATION_V001.md`
(`790ae95b...`), was checked. It sharpens P9 by proving that the `B_ind` tail
question is exactly `p_loc` restricted to `Tail_ind` (`:51-72`, `:86-100`) and
that the tail and background channels remain distinct. It neither adds a new
physical-layer object nor changes the eight-package minimal subset.

### 1.2 Roots, exclusions, and queries

Roots entered:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003/
/Users/bgm/MB Work/alpha-program-archive/workspace/
/Users/bgm/MB Work/alpha-program-archive/supervision/
/Users/bgm/MB Work/alpha_supervision/
```

Excluded without entry:

```text
a32_holdout/custodian_private/
.git/
seal sidecars except for custody verification
```

The work was a named-chain consolidation, not a corpus-wide existence sweep.
Queries were case-insensitive exact-identifier/phrase checks for:

```text
Q-239 | Q-245 | Q-249 | Q-250 | Q-251 | Q-252
SOURCE_GERM_PHYS | PHYSICAL_RETHESS_CLASS_AND_RESTRICTION_PACKAGE
U3_008 | PhysicalLogGerm | Tail_R | rho_H,N | p_loc | Pi_loc
B_ind | C_EM | R_comp | DeltaPhi | Thomson
stationary background | Abar_* | G_* | physical pullback
```

`rg` was unavailable in the execution environment; `grep -n -E` was used as
the next available line-addressed matcher. Identifier matches were checked at
source before use. No negative below claims more than the named-chain scope.

## 2. Deduplication rules

This specification uses three different operations and does not conflate them:

```text
IDENTITY       two names denote the same field or map; both source signatures agree
PACKAGING      distinct fields are dependency-coupled and placed in one package
SUCCESSION     a later theorem replaces an earlier open question but not its inputs
```

An item is deduplicated only by `IDENTITY`. `PACKAGING` never erases its member
fields.

## 3. Proven identifications and refused identifications

| Earlier vocabulary | Later vocabulary | Ruling | Proof from the named texts |
|---|---|---|---|
| Q-245 `topology_src`, `Diff_src` inside `SOURCE_GERM_PHYS` | Q-249 `topology_src`, `Diff_src` | **IDENTICAL FIELDS** | Q-245 `:51-77` defines the physical germ with these exact fields; Q-249 `:472-480` repeats the same source-side class inputs to `RetHess_phys`. |
| Q-239 physical contour, measure, complete boundary data, endpoint domains | Q-249 `contour_and_boundary_completion_class` | **PACKAGED, NOT IDENTICAL** | Q-239 `:31-36`, `:439-509`, and `:519-584` enumerate the physical objects; Q-249 `:472-498` asks for the class that realizes them in the response chain. The class is their response-facing completion, not a second contour. |
| Q-245 physical restriction maps | Q-249 `physical rho_H,N` | **IDENTICAL RESPONSE-SIDE MAP FAMILY** | Q-245 `:502-520` defines `Tail_R` by the response restrictions and states their preservation duties; Q-249 `:472-498` places those maps in the physical response package. |
| Q-252 physical pullback from finite holonomy data to completed sources | Q-245/Q-249 physical restrictions | **NOT IDENTICAL** | The pullback points finite-to-physical; `rho_H,N` points physical-to-finite. They form a comparison pair but have opposite domains and codomains. |
| Q-249 `stationary_background_class` | Q-252 `(Abar_*,G_*)` and `COMMON_ORIGIN_STATIONARY_BACKGROUND_MAP` | **ONE PACKAGE, DISTINCT FIELDS** | Q-249 names the admissible class; Q-252 supplies the missing class instance and the map that must produce it. A class is not its instance or producer. |
| Q-245/Q-249 finite-core separation question | Q-250 modulo-tail theorem | **SUCCESSION** | Q-250 `:392-436` proves exact determinacy only in `R_phys_class/Tail_R`. It resolves what restrictions determine, but it does not build the class, maps, or prove `Tail_R=0`. |
| Q-251 `p_loc`, `B_ind`, `C_EM`, `R_comp` | four separate consumer debts | **ONE LOCAL-PROJECTION PACKAGE WITH FOUR OUTPUT ROLES** | Q-251 `:177` onward defines `Pi_loc=iota_loc compose p_loc`; `B_ind`, `C_EM`, and `R_comp` are compositions of the same complete response with `p_loc`/`Pi_loc`. Their outputs remain distinct. |
| Q-251 Thomson row | Q-252 complete Thomson functional | **IDENTICAL CONSUMER SPECIFICATION** | Both cite the same V011 complete `Q_spec` amplitude-to-response and zero-momentum boundary-value construction. Q-252 does not introduce a second Thomson object. |
| common-origin `Z_inc[J,R]` | U3 common-origin provenance | **NOT IDENTICAL** | The former is the scalar physical functional/output-producing object; the latter is the no-supplementation certificate that U3 and the source/state/effect data descend together. A flag/certificate is not its discharger. |
| mathematical bidual tail | physical `Tail_R` | **NOT IDENTIFIED** | Q-251 `:159-161` expressly withholds the identity until a physical response class, embedding, and restrictions exist. |

These refused identifications are load-bearing. Removing either direction of the
comparison pair, replacing provenance with bundling, or transporting a
mathematical tail into the physical class would make the consolidation smaller
only by making it false.

## 4. Canonical object ledger

The eleven packages below contain sixteen canonical rows. Every negative is a
construction-status negative unless a cited theorem refutes an identity or
shortcut.

### P1 — `SOURCE_GERM_PHYS` and the pointwise common-origin functional

**Existing sealed name and signature:** Q-245 `:51-77`, `:352-356`,
`:740-761`; PhysicalLogGerm spec `:90-140`.

Required content:

```text
Z_inc[J,R]
state/effect/dynamics common origin
independent symmetric bilocal R source
source ports and zero-source point
target-independent provenance
```

The finite `s_J/s_R` maps are operator/module-class maps and do not supply this
scalar functional (Q-245 `:133`, `:761`). The ratified finite law also does not
create the complete continuum source object.

**Shape:** `AUTHORED-PHYSICS-SHAPED` — this is the physical law/content absent
from the corpus, analogous to the pre-law state before the finite source-coupled
transition law was commissioned. Ratified finite data constrain it but do not
derive it.

```text
P1_exists = false | TYPE-U
```

### P2 — physical source topology and differential calculus

Fields already named in Q-245 and Q-249:

```text
D_src, 0_src, topology_src, Diff_src, Reg_D1
```

They must make first and second source derivatives meaningful and supply the
independent symmetric-`R` derivative domain. Q-245 `:660-673` expressly does
not install a topology. The PhysicalLogGerm spec states that the topology and
calculus must be independently derived rather than selected.

**Shape:** `THEOREM-SHAPED` — candidate route: derive the weakest calculus in
which P1, U3 descent, the finite cylinder germs, and all required derivatives
are continuous/closable, then prove uniqueness up to the declared physical
equivalence. If that route leaves inequivalent calculi, a later adoption would
be needed; this report does not pre-promote one.

```text
P2_exists = false | TYPE-U
```

### P3 — complete `U3` physical input package

Q-239 `:99-135` gives the exact interface. Its six canonical rows are:

| Row | Missing physical object | Work shape | Declared inputs |
|---|---|---|---|
| P3a | completed physical prequotient, orbit/constraint map, gauge-fixed quotient and null/private removal | `CONSTRUCTION-SHAPED` | P1, ratified carrier, physical equivalence relation |
| P3b | descended branch-joint contour/spacetime measure and `delta_phys` | `CONSTRUCTION-SHAPED` | P3a, P1, source/history carrier |
| P3c | interacting contour/analytic/`i epsilon` prescription | `CONSTRUCTION-SHAPED` | P1, P3a-b, causality/reality data |
| P3d | complete preparation/gluing variation, boundary gauge orbit, edge variables, reductions, contacts and boundary functionals | `CONSTRUCTION-SHAPED` | P1, P3a-c, completed geometry |
| P3e | common invariant endpoint domains for later unbounded physical operators | `THEOREM-SHAPED` | the operators from P1/P3c-d; prove common dense invariance/closability |
| P3f | common-origin/no-post-output-supplementation provenance for the complete tuple | `THEOREM-SHAPED` | P1 and P3a-e; frozen construction trace |

Q-239 `:374-400`, `:439-509`, `:519-584`, and `:636-646` prove that the
finite branch grammar, sequential glue, bounded domains, and Haar measure do
not discharge these rows.

```text
P3_complete_instance_exists = false | TYPE-U
```

### P4 — `PhysicalLogGerm`

Required output of P1-P3:

```text
a nonzero neighborhood of the physical zero-source point;
a declared branch Log_0;
W=-i Log_0 Z_inc;
regularity sufficient for the admitted first and second derivatives;
provenance tying the germ to the same physical functional.
```

**Shape:** `THEOREM-SHAPED` — once P1-P3 exist, prove local nonvanishing,
branch consistency, differentiability, and common-origin descent. No new
physical term is licensed here.

```text
P4_exists = false | TYPE-U
```

### P5 — raw correlator, inverse Hessian, retarded Hessian and induced response

The raw-map specification's P3-P7 chain and Q-249 `:206-387` require:

```text
raw G from the bilocal R derivative of W;
its admitted inverse I_C on a named quotient/domain;
the stationary/2PI Hessian H_C or normalized equivalent;
the contour boundary-value and retarded extraction H_R;
RetHess_phys and topology_RetHess;
the exact induced response Pi_R,ind and its subtraction/contact conventions.
```

These are one realization chain, not one operator. Each arrow must preserve
state, measure, contour, contacts, boundary data, and domains.

**Shape:** `CONSTRUCTION-SHAPED` — inputs P1-P4 plus the declared physical
inversion/stationarity interface. If inversion or the 2PI reduction requires an
unsealed physical selection, that residual is authored and must be surfaced;
it is not assumed here.

```text
P5_exists = false | TYPE-U
```

### P6 — paired comparison maps

This package deliberately contains two arrows:

```text
physical-to-finite: rho_G,N, rho_H,N and related source restrictions;
finite-to-physical: the Q-252 pullback/embedding from finite holonomy-source
                    data to the completed physical source/connection.
```

The arrows are not inverses by definition. Their commuting and compatibility
relations must be proved. Q-245 `:502-520` defines
`Tail_R=intersection_N kernel(rho_H,N)` only after the physical class and maps
exist.

**Shape:** `CONSTRUCTION-SHAPED` — build both directions from P1-P5 and the
sealed finite cylinder system, without copying finite outputs backward or
choosing a completion to obtain a desired result.

```text
P6_exists = false | TYPE-U
```

### P7 — finite-core/separation and T5 commuting-square certificate

Q-245 `:509-520` states the required core/density, continuity/closability,
restriction-preservation, and commuting-extraction conditions. Q-250 then
proves the exact replacement when separation is unavailable:

```text
finite restrictions determine [H] in R_phys_class/Tail_R,
not H itself.
```

P7 may discharge by either:

```text
OBJECT SIDE: prove Tail_R={0}; or
OUTPUT SIDE: prove the selected consumer factors through
             R_phys_class/Tail_R.
```

**Shape:** `THEOREM-SHAPED`. The object-side route is not mandatory for a
single channel if that channel supplies its own output-tail theorem. It remains
required for an elementwise physical-response identification.

```text
P7_object_side_certificate_exists = false | TYPE-U
Q250_modulo_tail_theorem_exists = true
```

### P8 — common-origin stationary-background package

Q-249's `stationary_background_class` and Q-252's map/instance are consolidated
without identifying them:

```text
COMMON_ORIGIN_STATIONARY_BACKGROUND_MAP:
  (completed Z_inc/Log_0, rho_pre, effects, dynamics, physical source domain)
    -> (Abar_*, G_*(Abar_*)) at J=R=0
    -> H_R[...] at A_delta=0.
```

The package must provide the admissible background class, the actual map, the
selected/unique solution or solution class, and the evaluation pullback. Q-252
establishes that the finite relative-phase stationary set is empty for the
interior state-weight domain, that C1 is not an evaluation rule, and that the
three zero notions are distinct. None may be substituted for this package.

**Shape:** `CONSTRUCTION-SHAPED` — given P1-P6, pose the common-origin physical
stationarity problem and construct its solution class. Uniqueness, if claimed,
is a separate theorem; selection by convention is not licensed.

```text
P8_exists = false | TYPE-U
```

### P9 — local-projection consumer package

This package contains the shared machinery for four Q-251 rows:

```text
p_loc, iota_loc, Pi_loc=iota_loc compose p_loc;
the physical domain, codomain, topology and normalization p_loc[L_T]=1;
B_ind from the complete induced response;
C_EM from the complete full response;
R_comp from the complementary projection.
```

The four outputs are not identical. They share one absent physical projection.
Q-251 `:177` onward shows that an induced tail changes `B_ind` by
`p_loc(t_ind)` unless annihilation is proved.

The post-prompt Q-253 currency result proves the exact fixed-background
equivalence:

```text
B_ind is tail-blind
  iff p_loc restricted to Tail_ind equals zero
  iff p_loc factors through the induced-response tail quotient.
```

This is a theorem about what P9 must prove, not a construction of `p_loc`.

**Shape:** `THEOREM-SHAPED` — candidate route: derive the unique covariant local
coefficient projection on P5's completed class, prove its continuity and Ward/
boundary compatibility, and prove or refute its factorization through the
tail quotient. If multiple inequivalent projections survive, that residual is
authored-physics territory.

```text
P9_exists = false | TYPE-U
```

### P10 — response/state/boundary-to-phase consumer

Q-245 `:596-609`, Q-249 `:142-160`, and Q-251's `DeltaPhi` row require the
complete map

```text
(H_R or Pi_R,ind, physical state, boundary data)
  -> X_K on the complete on-shell cell
  -> DeltaPhi[K;X_K].
```

This is not a direct Hessian argument and no ratio/homogeneity shortcut is
sealed. Its tail action must be explicit: it either factors through the Q-250
quotient or supplies a lawful witness that it sees a physical tail.

**Shape:** `CONSTRUCTION-SHAPED` — declare the complete carrier and build the
state/boundary transport from P3-P8. No target value may select the map.

```text
P10_exists = false | TYPE-U
```

### P11 — complete `Q_spec`/Thomson consumer

Q-251 and Q-252 refer to the same V011 object:

```text
complete charged transition amplitude;
complete response kappa_Q(q^2);
path-independent boundary-value/limit construction;
physical limit topology and restriction relation.
```

The finite record amplitude does not instantiate the complete charged carrier,
spectrum, regulator/matching data, or physical limit.

**Shape:** `AUTHORED-PHYSICS-SHAPED` — the corpus does not contain the complete
charged Q-spec physical content from which this consumer would be constructed.
The response and limit theorems are downstream of that content.

```text
P11_exists = false | TYPE-U
```

## 5. Dependency order

The strict shared spine is:

```text
P1 -> P2 -> P3 -> P4 -> P5 -> P6
```

The arrows mean “is an input to,” not “uniquely derives.” After P6 the tree
splits:

```text
                         -> P7  object-side separation/T5 theorem
P1-P6 -> P8 background  -> P9  local-response consumers
                         -> P10 phase consumer
                         -> P11 complete Thomson consumer
```

More precisely:

| Object built | What it enables | What it does not enable |
|---|---|---|
| P1 | posing P2-P4 and common-origin U3 | topology, contour, or response by itself |
| P2 | lawful source derivatives and class statements | nonzero logarithm or physical measure |
| P3 | physical quotient/measure/contour/boundary/domain/provenance | raw correlator without P4 |
| P4 | raw physical differentiated correlators | inversion or retarded extraction |
| P5 | a named physical response class and response chain | finite authority or background evaluation |
| P6 | `Tail_R`, finite comparison, and falsifier execution | `Tail_R=0` |
| P7 | elementwise response identity if object-side separation succeeds | output maps P9-P11 |
| P8 | evaluation at a lawful physical background | a consumer's tail action |
| P9 | local `B_ind/C_EM/R_comp` route | phase and Thomson routes |
| P10 | phase route | local projection and Thomson routes |
| P11 | Thomson route | local and phase routes |

`P7` becomes moot for one chosen output only when that output independently
proves factorization through `R_phys_class/Tail_R`. Q-250 supplies the quotient
theorem, not the factorization.

## 6. Constraint battery

Every future realization of P1-P11 must carry the following certificates.

### B1 — finite-restriction reproduction (DoR-008 falsifier)

The completed objects must reproduce all sealed finite restrictions on the
same states, histories, orderings, contacts, boundary data, and domains. Q-245
`:470`, `:509-520` states the preservation bar. Disagreement voids the claimed
completion or its TYPE-P use; it is not repairable by tuning the restriction
after the comparison.

### B2 — finite retarded block baseline (Q-243)

On the ratified finite class, the retarded two-point block at the finite zero
background is zero and independent of `p_ch`. A completed restriction that
produces a different finite block fails the battery. This is a finite
restriction statement, not a claim about the complete stationary evaluation.

### B3 — finite restrictions stay `p_ch`-free (Q-245)

Every forced finite restriction of the response must preserve the Q-243
independence. Any `p_ch` dependence may enter only through physical tail content
or through the completed stationary background. It cannot be inserted into a
finite core.

### B4 — no naive continuous extension (Q-245)

Continuity of the finite C*-module/source maps does not determine a complete
physical response. The source topology, calculus, physical restrictions,
common domain, and preservation certificates must be built independently.

### B5 — separation only on ratified classes (Q-247)

Q-247's norm-continuous left-multiplier separation theorem applies to the
ratified finite/module classes. A future `RetHess_phys` must be proved to belong
to the relevant class before the theorem is transported. No shared noun or
formal representation supplies that membership.

### B6 — tail structure must be explicit (Q-247, Q-250)

The physical class and restrictions must instantiate `Tail_R`. Q-250 proves
only coset determinacy. A claim of elementwise determination must prove
`Tail_R=0`; a claim about an output must prove tail factorization. A bidual tail
is not automatically the physical tail.

### B7 — modulo-tail determinacy (Q-250)

Any two physical candidates with identical finite restrictions are equivalent
only modulo `Tail_R`. This theorem is binding on every class, background, and
consumer claim. It forbids upgrading finite agreement to physical identity.

### B8 — visible quotients are finite-domain objects (Q-251)

The two existing visible `p_ch` quotients live in finite state domains. They
are not retarded-response outputs and do not prove tail cancellation or
survival. A future physical consumer must expose its own domain and quotient.

### B9 — consumer-specific tail certificate (Q-251)

For each of `p_loc`, `B_ind`, `C_EM`, `R_comp`, `DeltaPhi`, and the Thomson
functional, the implementation must prove either:

```text
O(H+t)=O(H) for every physical t in Tail_R,
```

or exhibit a lawful physical witness that the output sees the tail. Q-251
establishes that neither direction is currently proved for any of the six.
For `B_ind`, Q-253 reduces this certificate exactly to
`p_loc` restricted to `Tail_ind` being zero at fixed completed background; it
also proves that this certificate does not decide P8's background channel.

### B10 — no finite interior stationary point (Q-252)

For the ratified finite pure-phase amplitude and interior `p_ch` domain, the
finite relative-phase stationary set is empty. A completed background may not
claim descent from a nonexistent finite stationary point.

### B11 — C1 is not an evaluation rule (Q-252)

The exact `A=0` operator reduction certificate fixes a law limit. It does not
force response evaluation at zero background. A background prescription must
come from P8.

### B12 — the three zero surfaces remain distinct (Q-252)

The following may not be identified without a proved pullback:

```text
finite relative holonomy/phase zero;
physical J=R=0 source surface;
physical A_delta=0 retarded-evaluation surface.
```

P6 and P8 must state how they relate them.

### B13 — finite-authority principle

An authored consumer may not see non-finite/tail physics merely because the
finite theory leaves it unconstrained. Any tail-sensitive term needs its own
declared physical provenance and must survive B1-B12. Silence in the finite
theory is not authorization to add a completed contribution.

### B14 — target independence and no post-output supplementation

P1-P11, their candidate families, and all restriction/background/consumer maps
must be frozen before any downstream output is seen. Common-origin provenance
must be an executable descent certificate, not a bundle assembled after the
outputs are known.

## 7. Minimal deciding subsets by channel

### 7.1 Shared minimal core

Every lawful channel needs:

```text
P1 + P2 + P3 + P4 + P5 + P6 + P8.
```

This core is necessary to separate the two remaining routes of `p_ch`
re-entry:

```text
tail channel       instantiated by P5-P6 and adjudicated at the consumer;
background channel instantiated by P8.
```

Without P8, a finite zero-background result cannot decide the physical
evaluation point. Without P5-P6, finite agreement cannot decide the tail.

### 7.2 One selected route

Add exactly one:

```text
local B_ind/C_EM/R_comp route: P9
phase/DeltaPhi route:           P10
Thomson route:                  P11
```

This is the eight-package minimal deciding subset stated in Section 0. For the
phase route, for example, the commissioning target is
`P1-P6 + P8 + P10`; P7, P9, and P11 are not prerequisites if P10 itself proves
its tail action.

### 7.3 Universal all-output claim

A claim that `p_ch` cancels or survives in every alpha-facing output requires
all three consumers P9-P11 and either:

```text
P7 object-side Tail_R={0}; or
six consumer-specific output-tail certificates satisfying B9.
```

The full physical layer is therefore necessary for a universal claim, but not
for the first channel-specific decision.

## 8. Commissioning order

The smallest noncircular order is:

```text
1  commission P1 only: the common-origin pointwise physical functional;
2  attempt P2 and the theorem-shaped portions P3e/P3f;
3  construct P3a-P3d and prove P4;
4  construct P5 and the paired maps P6;
5  construct P8 without identifying the three zero surfaces;
6  choose one consumer by road relevance, not by desired output;
7  execute B1-B14 and decide its tail/background behavior;
8  only then decide whether P7 or the other consumers are worth building.
```

The commission must not start by authoring `RetHess_phys`, a background, or a
consumer. Those are downstream constructions and would silently choose the
source law, topology, contour, and domains that P1-P4 are required to expose.

## 9. Typed final determinations

```text
CONSOLIDATED_PHYSICAL_LAYER_SPEC_EXISTS = true

FULL_PHYSICAL_LAYER_INSTANCE_EXISTS = false | TYPE-U

MINIMAL_SINGLE_CHANNEL_DECIDING_SUBSET_IDENTIFIED = true

MINIMAL_SINGLE_CHANNEL_PACKAGE_COUNT = 8

MINIMAL_SUBSET_IS_SMALLER_THAN_FULL_LAYER = true

SHARED_AUTHORED_GATE_COUNT = 1

SHARED_AUTHORED_GATE = SOURCE_GERM_PHYS / common-origin pointwise Z_inc[J,R]

P_CH_TAIL_CHANNEL_DECIDED = false | TYPE-U
  prerequisite: P1-P6 plus the selected consumer's tail certificate

P_CH_BACKGROUND_CHANNEL_DECIDED = false | TYPE-U
  prerequisite: P1-P6 plus P8

P_CH_CANCELLATION_OR_SURVIVAL_DECIDED = false | TYPE-U
  prerequisite: the eight-package minimal subset and constraint battery

PHYSICAL_AND_MATHEMATICAL_TAIL_IDENTITY = false | TYPE-R
  scope: Q-251 expressly withholds transport without the physical class/maps

FINITE_ZERO_BACKGROUND_FORCES_PHYSICAL_EVALUATION_POINT = false | TYPE-R
  scope: Q-252 proves C1 is not an evaluation rule and the zero surfaces differ
```

`TYPE-U` denotes unbuilt, not physically refuted. The two `TYPE-R` rows refute
specific identity/forcing transports only; they do not refute the physical
layer or either `p_ch` outcome.

## 10. Fences and custody statement

No root, eigenvalue, coupling, scale, response value, phase value, or measured
constant was computed or compared. No Misner-Sharp/Brown-York choice was made.
No physical object was repaired, adopted, or promoted. This artifact is the
requested commissioning specification only.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
