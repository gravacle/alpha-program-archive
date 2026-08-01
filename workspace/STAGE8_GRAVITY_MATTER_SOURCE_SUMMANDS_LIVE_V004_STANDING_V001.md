# Stage 8 Gravity and Matter Source Summands, Live-v004 Standing v001

Date: 2026-08-01
Lane: CODEX LANE 1
Relay: PASTE 290, Task 3b
Register head checked: Q-205
Construction performed: none

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Lead verdict

**The historical four-summand remainder is not carried unchanged into the
active v004 zero-bare formulation.** The four terms can be enumerated exactly
from the 2026-07-20 source-action skeleton:

```text
Gamma_record,matter,gravity[X]
  corresponds there to

  1. S_EH[g]
  2. S_gravity,boundary[g]
  3. (1/2) sum_(m=+/-1/2) S_D[u_m;g,A,Phi_BR]
  4. Gamma_record[X].
```

The historical Maxwell term is not one of those four; it was the separate
first term in the v002 partition. The active v004 branch expressly removes
that microscopic Maxwell term and treats `K` only as a local surrogate for an
induced response
(`primitive_record_cell_selection_principle_v004.md:3-9`). Its exact active
functional is not a four-term action. Before a decomposition it states only a
normalized 2PI identity, and its prospective decomposition is

```text
Gamma_2PI[Abar,G]
  = (i hbar/2) Tr_C log G^(-1)
    + Gamma_rest[Abar,G; source,record,g,gauge,edge]
```

(`primitive_record_cell_selection_principle_v004.md:89-105`). Thus the four
historical names remain useful source vocabulary, while the live complete
zero-bare source-record-gravity CTP functional remains unbuilt.

The active authority independently retains explicit gravitational and Dirac
action forms through `alpha_complete_dimension_convention_ledger_v004.md`, but
it does not identify those two forms plus a complete record action with an
exact four-summand decomposition of `Gamma_rest`. The current authority JSON
lists that ledger and both v004 principles as active physics inputs
(`alpha_post_cleanroom_current_authority_spec_v001.json:2-12`) and leaves the
complete physical kernels and domains false (`:13-27`). Q-205 concerns seam
10's four-plane theorem and does not supersede this action standing.

```text
historical_v002_remainder_has_four_named_source_terms = true

historical_four_term_remainder_is_the_active_v004_exact_decomposition = false | TYPE-R |
  test: v004:3-9 removes the microscopic Maxwell partition and v004:89-105
        replaces the undecomposed active target by the 2PI/Gamma_rest form

active_zero_bare_source_record_gravity_CTP_functional_constructed = false | TYPE-U |
  would-build: one instantiated normalized source-record-field-gravity CTP
               functional on a certified physical carrier, quotient, measure,
               state/effect package, domains, boundary data, and action-family
               provenance
```

## 1. Source decomposition and currency

### 1.1 The historical partition

`primitive_record_cell_selection_principle_v002.md:30-46` writes

```text
Gamma_K[X]
  = (K/4) integral_Omega sqrt(|g|) F_(mu nu) F^(mu nu) d^4x
    + Gamma_record,matter,gravity[X].
```

`primitive_self_consistent_one_particle_source_principle_v001.md:52-67`
then expands the single-history stationary spine as

```text
Gamma_K[X]
  = S_EH[g] + S_gravity,boundary[g]
    - (K/4) integral_Omega sqrt(-g) F_(mu nu) F^(mu nu)
    + (1/2) sum_(m=+/-1/2) S_D[u_m;g,A,Phi_BR]
    + Gamma_record[X]
    + normalization and endpoint constraints.
```

Comparing the two displays fixes the four members of the second term. The
normalization and endpoint constraints are constraints appended to the
stationary problem, not named members of `Gamma_record,matter,gravity`. The
Maxwell term is likewise outside that remainder.

| # | Historical member | Type and explicit arguments | Standing now |
|---|---|---|---|
| 1 | `S_EH[g]` | Bulk gravitational action, functional of the metric | Explicit active convention survives, but its physical coefficient is declared rather than record-derived: `TYPE-P` |
| 2 | `S_gravity,boundary[g]` | Gravitational boundary completion, functional of the induced metric/boundary geometry | Active v004 combines this with the EH bulk and `S_ref` as `S_grav,D`; standard Dirichlet completion declared, complete mixed domain open: `TYPE-P` plus `TYPE-U` completion debt |
| 3 | `(1/2) sum_m S_D[u_m;g,A,Phi_BR]` | One-particle Dirac matter term, coupled to metric, compact connection, and paired-return block | Source ontology adopted; public spin quotient derived; complete operator/domain and `Phi_BR` unbuilt: `TYPE-P` plus `TYPE-U` debts |
| 4 | `Gamma_record[X]` | Record functional on the full joint variable tuple `X` | Symbol named in the source skeleton; one-cell fidelity candidate exists, but no complete Lorentzian/CTP record functional is identified with this slot: `TYPE-U` |

The source-action file is hash-bound in the
`primitive_self_consistent_one_particle_source_manifest_v001.json` with
`sealed_date = 2026-07-20`. Its status block says
`self_consistent_one_particle_source_principle_adopted=true`, while also saying
`complete_self_adjoint_CTP_domain_derived=false`,
`paired_return_mass_block_derived=false`, and
`stationary_record_cell_derived=false`
(`primitive_self_consistent_one_particle_source_principle_v001.md:129-143`).
The action display is therefore an adopted source-action requirement, not an
executed complete-cell construction.

### 1.2 What v004 changes

The v004 authority correction is direct:

> "Version 002 placed a local Maxwell term with coefficient `K` inside the
> microscopic action. The active branch instead has zero bare Maxwell
> stiffness. Here `K` labels a local surrogate for an exact induced connection
> response; it is not a microscopic input."

Source: `primitive_record_cell_selection_principle_v004.md:3-9`.

The prior KT4 version audit reached the same typed result and names the active
unknown as `COMPLETE_ZERO_BARE_SOURCE_RECORD_GRAVITY_CTP_FUNCTIONAL`
(`STAGE8_GAMMA_RECORD_MATTER_GRAVITY_BARREDNESS_KT4_DETERMINATION_V001.md:51-96`).

The active dimension ledger still writes a branch action
`S_branch=S_grav,D+S_D+S_M` (`alpha_complete_dimension_convention_ledger_v004.md:75-96`),
but later restricts `S_M` to the fixed-`K` local surrogate
(`:154-180`) and says the exact zero-bare functional does not inherit its
boundary displacement (`:188-199`). Hence `S_M` may not be reinserted as the
microscopic fifth term, and the ledger's branch display does not close the
active `Gamma_rest` decomposition.

```text
v002_microscopic_Maxwell_partition_live = false | TYPE-R |
  test: v004 authority correction and zero-bare functional

four_historical_remainder_names_retained_as_exact_active_Gamma_rest_members = NO_VERDICT |
  reason: v004 names source, record, g, gauge, and edge arguments jointly but
          supplies no decomposition theorem or termwise identification
```

## 2. Gravity summands, precisely

### 2.1 Exact active form

The active dimension ledger combines historical members 1 and 2 into the
Dirichlet-completed gravity functional

```text
S_grav,D
  = -hbar/(16 pi l_P^2)
      { integral_M sqrt(-g) R d^4x
        + 2 sum_B epsilon_B integral_B sqrt(|h|) K_ext d^3x
        + 2 sum_J integral_J sqrt(sigma) eta_J d^2x }
    + S_ref.
```

Source: `alpha_complete_dimension_convention_ledger_v004.md:75-106`.
Here `B` consists of the actual non-null initial, final, and asymptotic
regulator boundaries; `J` consists of their non-null joints; and `S_ref` is the
fixed asymptotic reference subtraction (`:98-106`). The active domain principle
repeats that this completion belongs to the global time slab boundary of `M`,
not to the null edge of the history-support diamond
(`primitive_causal_record_cell_domain_principle_v004.md:14-39`).

The Planck convention is

```text
l_P = sqrt(hbar G/c^3).
```

Source: `alpha_complete_dimension_convention_ledger_v004.md:32-42`. The same
ledger derives the dimensional identities but classifies the metric, action,
stress, Planck-energy, and charge conventions only as
`DECLARED CONSISTENT`, and the global non-null gravity completion as
`STANDARD DIRICHLET COMPLETION DECLARED; MIXED/STATE-DEPENDENT DOMAIN OPEN`
(`:501-524`). Its flags are
`global_nonnull_Dirichlet_gravity_completion_declared=true` and
`mixed_gravitational_boundary_domain_derived=false` (`:527-560`).

### 2.2 Standing and date

The gravitational term is active because the current authority JSON lists the
dimension ledger as an active physics input and hash-binds it
(`alpha_post_cleanroom_current_authority_spec_v001.json:2-12,111-129`). It is
not derived from the record incidence structure or the current source-record
operator. The precise standing is therefore:

```text
gravity_action_form_active = true
gravity_action_and_l_P_record_derived = false | TYPE-U |
  would-build: a same-source derivation of the gravitational carrier,
               normalization and global CTP variational domain

gravity_action_current_standing = TYPE-P |
  premise: declared four-dimensional Einstein-Hilbert plus non-null
           Dirichlet completion with l_P defined from G
```

Q-181's phrase "adopted Planck length" is accurate only at this premise level.
The source ontology/action skeleton was sealed on 2026-07-20. The active v004
authority file carries no sealed `effective_date` field, so sealed text does
not support a more precise later "since" date than its current post-clean-room
authority status. Nothing upgrades `l_P` to a record-derived output.

The source stationary equation is

```text
G_(mu nu) + boundary/record terms
  = 8 pi G [T^EM_(mu nu) + <T^Dirac_(mu nu)>_(rho_1)
            + T^record_(mu nu)].
```

Source: `primitive_self_consistent_one_particle_source_principle_v001.md:85-102`.
That file says the complete cell "must yield" these equations and then leaves
the stationary cell false. The equation is a required coupled target, not a
computed stationary solution.

### 2.3 Instantiated would-build

An instantiated gravity member would require all of the following, fixed
before use:

1. one actual metric/geometry carrier and its two Lorentzian CTP history
   copies, reached by the discrete-to-continuum construction rather than an
   adopted smooth `(M,g)` shortcut;
2. one concrete global time slab, its non-null boundary pieces and joints,
   their orientations, induced metrics, `K_ext`, `eta_J`, and one fixed
   `S_ref`;
3. the displayed `S_grav,D` as a functional on that carrier, with a certified
   variational domain and vanishing/cancelled boundary form;
4. a same-source status for the coefficient `l_P`, or an explicit premise
   disposition carrying its conditionality; and
5. for the sourced Einstein equation, represented EM, Dirac, and record stress
   functionals on the same domain.

The standalone gravity functional needs the **metric sector**. The complete
coupled gravity equation needs **both** that metric sector and the joined
source-record-connection field/CTP home because its right-hand side contains
all three stresses. The pending DoR 008 proposal concerns an algebraic compact-
connection field/CTP presentation and expressly does not import smooth `(M,g)`;
it cannot by itself instantiate the gravity carrier.

## 3. Matter summand, precisely

### 3.1 Exact source form and couplings

At source the matter member is

```text
(1/2) sum_(m=+/-1/2) S_D[u_m;g,A,Phi_BR],

D_mu u = (nabla_mu + i A_mu) u.
```

Source: `primitive_self_consistent_one_particle_source_principle_v001.md:59-77`.
The factor `1/2` is the rotationally unresolved one-particle density, not a
two-particle singlet (`:29-50`). The same density operator supplies both the
connection current and Dirac stress (`:12-27`). `Phi_BR` is required to be the
odd block of the complete Boundary-Resolved superconnection, normalized by the
same microscopic operator; if it is not derived, the source problem remains
massless rather than receiving a fitted mass (`:79-83`).

The active convention ledger writes the symmetrized local Dirac form

```text
S_D = hbar integral_M sqrt(-g)
      { (i/2)[psi_bar gamma^mu D_mu psi
               -(D_mu psi_bar) gamma^mu psi]
        - mu psi_bar psi } d^4x,

D_mu psi = (nabla_mu+i A_mu) psi.
```

Source: `alpha_complete_dimension_convention_ledger_v004.md:75-96`. It also
displays the global Dirac boundary form and says the complete CTP domain must
make it vanish (`:201-219`). Its status table calls the global Dirac CTP
prescription `TYPED; COMPLETE OPERATOR DOMAIN OPEN` (`:501-524`).

No sealed identity in these sources equates the ledger's local `mu` term with
the source skeleton's generated `Phi_BR`. The former is an active convention
form; the latter is a same-microscopic-operator requirement. Transporting one
into the other would be an unproved identity.

### 3.2 Standing

The one-particle source ontology is explicitly adopted
(`primitive_self_consistent_one_particle_source_principle_v001.md:3-10,129-143`).
The public spin quotient is derived inside that adopted sector, as confirmed by
`results/primitive_self_consistent_one_particle_source_v001.json`. The complete
matter operator is not constructed: the source principle leaves the
self-adjoint CTP domain and paired-return block false, while the active ledger
leaves the complete global CTP operator domain false.

```text
one_particle_source_ontology_standing = TYPE-P |
  premise: one normalized positive unit-character Dirac excitation

public_spin_quotient_derived_within_adopted_source_sector = true

complete_matter_summand_instantiated = false | TYPE-U |
  would-build: one represented Dirac operator/action on the completed joint
               source-record-field CTP carrier and common domain, with the
               generated Phi_BR block or a proved massless branch, its global
               boundary form, state, and common current/stress/response
               renormalization
```

### 3.3 Instantiated would-build and dependencies

The matter member requires:

1. the already constructed source CAR/GNS sector and one normalized public
   one-particle density;
2. an instantiated compact-connection field/CTP algebra, branch embeddings,
   joint representation, and common dense domain extending the source-record
   presentation;
3. the metric/spin structure needed for `gamma^mu`, `nabla_mu`, the invariant
   measure, and the boundary form;
4. the generated `Phi_BR` block from the same microscopic operator, or a
   theorem selecting the massless case; and
5. one target-independent common prescription for current, stress, and
   response, plus the endpoint/side-boundary domain.

It therefore requires **both** the pending field/CTP home and the metric
sector. The DoR 008 route remains pending and, at register head Q-205, its
intact proposal has failed the adversarial certificate and is unavailable for
use
(`STAGE8_FIELD_CTP_ADOPTION_PROPOSAL_ADVERSARIAL_KILL_DETERMINATION_V001.md:415-442`).
Even a repaired algebraic adoption would not supply the metric sector,
`Phi_BR`, state, dynamics, quotient/measure, contacts, Ward identities, or the
complete operator domain.

## 4. Record member and interaction audit

The record member is named only as `Gamma_record[X]` in the source skeleton.
The sealed one-cell candidate
`PRIMITIVE_ADDITIVE_RECORD_FIDELITY_ACTION_V002.md:50-96` adopts

```text
S_R,E(theta) = -hbar log[cos^2(theta/2)]
```

and gives a prospective cell sum. But that artifact expressly leaves the
causal ensemble, orientation measure, continuum limit, Lorentzian/CTP
continuation, and edge treatment unchosen (`:83-96`), says it is not yet the
complete electromagnetic action (`:98-108`), and leaves its completion flags
false (`:147-160`). No sealed map identifies this one-cell Euclidean candidate
with the full `Gamma_record[X]` slot.

### 4.1 Explicit coupling that is present

The written outer action is additive, but its summands share variables:

- the Dirac member depends explicitly on `g`, `A`, and `Phi_BR`;
- `Gamma_record` is a functional of the full tuple `X`, which includes
  `Omega`, `g`, `A`, `Phi_BR`, both source modes, interval, and record data;
- variation with respect to `g` produces the displayed Einstein equation with
  EM, Dirac, and record stresses; and
- v002 expressly permits the remainder to depend on `A` and the other fields
  (`primitive_record_cell_selection_principle_v002.md:43-46`).

Thus the sectors are coupled at least through shared variational variables and
the joint stationarity equations.

### 4.2 What cannot be certified

The source text does not define the internals of `Gamma_record[X]`. Active v004
makes the unresolved dependence more explicit by writing a single
`Gamma_rest[Abar,G; source,record,g,gauge,edge]`. Consequently the corpus does
not establish that gravity and matter meet the record member **only** through
the stationarity equations. A direct cross-term inside `Gamma_record` or
`Gamma_rest` is allowed by the declared arguments and neither exhibited nor
excluded.

```text
explicit_outer_product_between_named_gravity_and_record_members_found = false | TYPE-S |
  roots: gravity_emergence_evidence_program, cleanroom workspace,
         archive workspace, alpha_supervision |
  exclusions: a32_holdout/custodian_private, .git, binary payloads,
              superseded versions as current authority |
  query: word-boundaried Gamma_record[X], Gamma_rest, S_EH,
         S_gravity,boundary, S_D[u_m;g,A,Phi_BR], Einstein-Hilbert,
         Dirac stress, record stress, summand

gravity_matter_record_interaction_is_only_via_stationarity = NO_VERDICT |
  reason: the complete record/Gamma_rest functional is unbuilt and its declared
          domain permits mixed source-record-metric-gauge-edge dependence

hidden_cross_term_required_by_sealed_text = NO_VERDICT |
  reason: no explicit mixed monomial is required, but no separability theorem
          excludes one
```

This is not evidence of a hidden imported cross-term. It is a specification
boundary: the active object has not been decomposed far enough to decide
whether one exists.

## 5. Source and seal checks

Roots entered:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/workspace
/Users/bgm/MB Work/alpha_supervision
```

Permanent exclusions:

```text
a32_holdout/custodian_private/ was not entered, listed, read, or searched
.git/ and binary payloads were excluded
superseded versions were not treated as current authority
```

Hash checks performed before this record was written:

```text
primitive_self_consistent_one_particle_source_principle_v001.md
  12feb7a6a4b1c3b5b91720c4dd7813cf3de8a2150d35bb2960ad521f0e36018a
  MATCH: sealed manifest

alpha_complete_dimension_convention_ledger_v004.md
  bbf2bdddfcefe851e985c4db03a62906082660af9a3c639d259afc93b4bbcc66
  MATCH: current authority JSON

primitive_record_cell_selection_principle_v004.md
  13d227ceb2198d96b0e4e2fef57b874cea71cb755320508fbf4c6d64a00c507e
  MATCH: current authority JSON

primitive_causal_record_cell_domain_principle_v004.md
  d7bdb60a971ae0ab00ca9e15e1f1928ebd2e2ca9c97c179c8eb53e85b13f2f96
  MATCH: current authority JSON

PRIMITIVE_ADDITIVE_RECORD_FIDELITY_ACTION_V002.md
  9da6fe80fd9ee3af7ae847b07d98884f8c0a0d86457d34684cb566b1d4adf013
  MATCH: local sidecar

STAGE8_C_RECORD_DEPENDENCY_MAP_AND_CRITICAL_PATH_EINSTEIN_V001.md
  59dcdcbabf2b2f79a1754ce16b18d64219489d13eefe57fe7d731dc0b7b4d754
  MATCH: sidecar and Q-181

STAGE8_GAMMA_RECORD_MATTER_GRAVITY_BARREDNESS_KT4_DETERMINATION_V001.md
  7993f0a4c5a475c8d470b0befc6ab2b7745f352266558c5334b1603eaf8a700f
  MATCH: sidecar and Q-182
```

## 6. Final status

```text
FOUR_HISTORICAL_REMAINDER_MEMBERS_ENUMERATED = true
ACTIVE_V004_DECOMPOSITION_IS_THE_SAME_FOUR = false | TYPE-R

GRAVITY_FORM_ACTIVE = true
GRAVITY_FORM_STANDING = TYPE-P
GRAVITY_NORMALIZATION_RECORD_DERIVED = false | TYPE-U
COMPLETE_GRAVITY_CTP_DOMAIN_DERIVED = false | TYPE-U

MATTER_SOURCE_ONTOLOGY_STANDING = TYPE-P
PUBLIC_SPIN_QUOTIENT_DERIVED = true
COMPLETE_MATTER_SUMMAND_INSTANTIATED = false | TYPE-U
PAIRED_RETURN_BLOCK_DERIVED = false | TYPE-U

COMPLETE_RECORD_SUMMAND_INSTANTIATED = false | TYPE-U
GRAVITY_MATTER_RECORD_ONLY_STATIONARITY_COUPLING = NO_VERDICT

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
