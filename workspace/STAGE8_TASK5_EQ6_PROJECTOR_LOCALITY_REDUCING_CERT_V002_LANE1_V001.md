# STAGE 8 TASK 5 / EQ6 - PROJECTOR LOCALITY, REDUCTION, AND CERT V002

Date: 2026-08-04

Custody: Codex Lane 1, determination and derivation lane

## Lead result

```text
REGISTER_HEAD = Q-468
CONDITION_TAG = [EQ6]

FIXED_STAGE_HODGE_LICENSE = DERIVED / PROVABLE
SECTOR_LOCALITY = PROVEN
WITHIN_CYCLE_GLOBALITY = LAWFUL / PROVABLE
WITHIN_CYCLE_LOCALITY_RATIFIED = false / PROVABLE

REDUCING = AUTHORABLE
REDUCING_DERIVABLE_FROM_A4 = false / PROVABLE
REDUCING_OBSTRUCTED = false / PROVABLE

NATURALITY = OPEN
NATURALITY_RANK_PRESERVING = DERIVED_ON_CHAIN_AND_ADJOINT_SCOPE
NATURALITY_ALL_ARROWS = TYPE-U

CERT_V002 = BLOCKED(contact_reducing + all_arrow_adjoint_intertwiner)
READER_REFERENCED = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The Q-466 locality specification was too strong.  The ratified support laws
require no spreading between certified disjoint sectors; they do not require
pointwise support preservation inside one connected cycle.  On a certified
Hilbert direct sum of chain sectors, the Hodge Laplacian and its zero spectral
projector are block diagonal.  Inside one cycle, however, the harmonic
projection is the basis-free Riesz representative of the cycle's flux or
holonomy pairing and is generally supported on the whole cycle.

That correction removes V001's false locality blocker.  It does not create
the two operator certificates V001 also lacked.  The strict A4 pushout does
not make the contact subspace reducing for the ratified Laplacian, and the
sealed arrow maps do not supply an adjoint intertwiner on every
cycle-creating refinement.  Consequently the maximal reader-free V002
subpackage is assembled below, but the conjunctive projector certificate
remains blocked.

## 0. Preflight, authorities, and symbols

### 0.1 Preflight

```text
DOES_THE_OBJECT_EXIST = yes | V001 attempt exists and hash verifies
IS_THE_VERSION_CURRENT = yes | through Q-468
ARE_INPUTS_PRESENT = yes
OUTPUT_PREEXISTED = false
PREFLIGHT = PASS
```

The requested output and sidecar did not exist locally or in the archive
before construction.  V001 was hash-verified before reading:

```text
STAGE8_TASK5_EQ6_MAXWELL_HODGE_PROJECTOR_CERT_LANE2_V001.md
SHA-256 f074ca24e8b96c576f5c64b856377f39ed8d4fc729c02cbf591326322558f816
sidecar verification = OK
```

The live questions-settled register was sealed at Q-468 at preflight.  Q-467
records the pending-review stage-1 J4/J12/J15 build; no unreviewed claim from
that row is needed here.  The J15 form used below is the independently derived
and ratified contravariant mate from Q-464/A4.

### 0.2 Authority ledger

| Authority | SHA-256 | Use |
|---|---:|---|
| questions-settled register at preflight | `6ecd91139c0e62c81053fff0b5fb03efb5f2424939943a17a7b0342a823ba502` | current through Q-468; no later row present at seal preparation |
| `LOCKED_PROCESS.md` | `1ee1c4188cf1ac1d37f40537a611407c0fd344387bd39421688f8b18478d8469` | gates, negative typing, geometry/rails rule |
| DoR-019 decision | `6ab72b0cb3a93e123eb1d3c5088fc83361d86c6dc739f0a886380dbd2d143f1f` | ratified positive metrics, Riesz maps, W3 precision, units |
| metric V005 | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | finite metric and adjoint restriction formulas |
| DoR-020-A1 decision | `c4dc5976d7e65fe8a6597870629e64cabe6a031b95de97f5572bb36379abb588` | path/current support and bundle-field law |
| adopted WHERE clauses | `19b2060392b6e04448c1c13416b87b67decf401246e3414a783b288fdb5d80ec` | exact OLD_FID/RNL/LR membership scopes |
| WHERE final check | `b4c901f512379251b55d31aae6914d1fce9af6280c8f65081afeabfd4e75f219` | Q-432 `P=id` and mixer regressions |
| DoR-020-A4 strict pushout | `5fd95472bd6f0507a371779505fe91e2c3c4657ee3afc664ca563a3743d668a4` | contact gluing and J13 laws |
| local orthogonal excision certificate | `d61a550a33bf1215c35f4d6f27cd2ec5d644b93a05e16d08fe3d43ded3416817` | support-indexed direct-sum/excision discipline |
| RNL correction | `99c34408b86f93a343b372595bb7f7b199501b1eaab4ef241d5aea2f853f9757` | relative no-leakage, not global orthogonality |
| J4/J12/J15 determination map | `76ee3c695b1c0c02986a13ff64d6db93f76e39c6861b40273bd31aed1c3a2eb0` | true J15 contravariant mate |
| physical J2 attempt | `3fd4b924ec1a70f3e730bcf99f406d697c53937b26467d2ae6d5aa8c1bb6822c` | certificate interface only; no reader imported |
| projector cert V001 | `f074ca24e8b96c576f5c64b856377f39ed8d4fc729c02cbf591326322558f816` | fixed-stage theorem and reciprocal-loop witness |

Every local authority sidecar available next to these artifacts was verified
before use.  No measured value, response target, threshold, or reader is an
authority for this construction.

### 0.3 Register and clause sweep

The ratified texts and register were searched for `within-cycle locality`,
`harmonic support`, `Hodge projector`, `contact reducing`, `Laplacian`,
`RNL`, `LR`, and `Ward`.  The result is exact:

1. DoR-019 fixes the metric and unit/Riesz structure, not a support-local
   Hodge law.
2. DoR-020-A1 fixes path/current support and local field transport.
3. RNL applies to physically disjoint or contact-exclusive sectors under its
   stated antecedent; Q-432 expressly rejects global orthogonality.
4. LR requires transported tests to remain in the mapped local range.
5. A4 requires contact gluing plus J13 support/Ward/restriction laws, but says
   nothing about the contact orthogonal projection commuting with a Riesz
   adjoint, Laplacian, or spectral projector.
6. No ratified clause requires a harmonic projection to preserve the support
   of an individual edge inside one connected cycle.

Therefore the L1 stop condition does not fire.

```text
WITHIN_CYCLE_LOCALITY_CLAUSE_FOUND = false / PROVABLE
```

### 0.4 Symbol-collision ledger

The following names are kept distinct throughout:

```text
Delta_N^Hdg    Hodge Laplacian, never an action/phase difference;
P_H,N          harmonic spectral projector, never the WHERE test map P_R;
E_C,N          orthogonal projector onto the contact subspace;
Riesz_N        metric Riesz map, never a refinement restriction;
rho_f^k        downward degree-k restriction;
I_contact,N    contact response/symbol subspace, not the A3 action I_N;
r_f^Bot        J15 bottom restriction, not rho_f^k.
```

## 1. L1 - Corrected locality law

### 1.1 Fixed-stage input

At one actual finite stage `N`, let

```text
... -> C_N^(k-1) --d_N^(k-1)--> C_N^k
    --d_N^k--> C_N^(k+1) -> ...,

d_N^k d_N^(k-1)=0.                                  (L1-1)
```

DoR-019 supplies a positive inner product in every relevant degree.  Let
`Riesz_N^k` be its Riesz isomorphism and define

```text
delta_N^k
 := (Riesz_N^(k-1))^(-1)
    (d_N^(k-1))^*
    Riesz_N^k,

Delta_N^Hdg
 := d_N^(k-1) delta_N^k
    + delta_N^(k+1) d_N^k.                         (L1-2)
```

V001 proves, and Q-468 confirms, that `(L1-2)` gives the finite orthogonal
Hodge decomposition and the basis-free projector

```text
H_N^k := ker Delta_N^Hdg,
P_H,N := 1_{0}(Delta_N^Hdg).                       (L1-3)
```

This fixed-stage result is `PROVABLE`.  It comes from the ratified metric and
actual differential, not from an isometry alone.

### 1.2 Disjoint-sector direct-sum theorem

Let `{S_a}` be a finite family of actual support sectors certified as a
Hilbert direct sum of subcomplexes:

```text
C_N^k = orthogonal_direct_sum_a C_(N,a)^k,

d_N^k = direct_sum_a d_(N,a)^k.                   (L1-4)
```

The first equation is a premise with physical content.  It is supplied only
on an actual pair or family for which the RNL/excision certificate proves the
zero cross-pairing and the support decomposition.  Mere disjoint labels do
not imply it; Q-432's admissible off-diagonal metric is the permanent
counterexample to that shortcut.

From `(L1-4)`, the Riesz map splits:

```text
Riesz_N^k = direct_sum_a Riesz_(N,a)^k.            (L1-5)
```

Taking the adjoint in `(L1-4)` with `(L1-5)` gives

```text
delta_N^k = direct_sum_a delta_(N,a)^k.            (L1-6)
```

Substitution into `(L1-2)` yields

```text
Delta_N^Hdg = direct_sum_a Delta_(N,a)^Hdg.        (L1-7)
```

Finite functional calculus preserves direct sums, hence

```text
P_H,N
 = 1_{0}(Delta_N^Hdg)
 = direct_sum_a 1_{0}(Delta_(N,a)^Hdg)
 = direct_sum_a P_H,(N,a).                        (L1-8)
```

For `x in C_(N,a)^k`, equation `(L1-8)` gives

```text
P_H,N x in C_(N,a)^k.                              (L1-9)
```

Thus the Hodge projector has zero cross-sector spreading on every certified
disjoint-sector Hilbert direct sum.  The result is basis-free and covariant
under permutations, sign changes, and reality maps that preserve the
certified decomposition.

```text
DISJOINT_HILBERT_COMPLEX_IMPLIES_BLOCK_HODGE = true / PROVABLE
SECTOR_LOCALITY = PROVEN
```

The all-stage assertion remains premise-marked: the excision certificate is
a failure-capable proof object, not a theorem that every alleged physical
member supplies `(L1-4)`.

```text
ALL_STAGE_DIRECT_SUM_INHABITANCE = TYPE-P([EQ6] + actual_LOE_terms)
```

### 1.3 FC6 and the exact locality boundary

FC6 consists of the actual support conditions

```text
OLD_FID + EXCLUSIVE_REGION_RNL + LR.               (L1-10)
```

On a certified disjoint pair, `(L1-8)` is compatible with all three:

* OLD_FID keeps the old sector and its metric unchanged;
* RNL forbids a source-supported component from entering a physically
  disjoint target sector;
* LR keeps transported tests in the mapped support range.

Nothing in `(L1-10)` says that an operator must preserve every proper subset
of one connected sector.  In particular, an edge of a connected cycle is
not a disjoint Hodge subcomplex merely because it is a smaller support set.
The differential and harmonic constraint couple the cycle's edges.

Therefore the corrected locality field is:

```text
LOCALITY_CORRECTED =
  sector_blockwise_on_certified_disjoint_Hilbert_subcomplexes
  + RNL/LR_compatible
  + within_connected_cycle_globality_allowed.                 (L1-11)
```

### 1.4 Harmonic pairing is the global cycle charge

Restrict the metric Riesz map to the harmonic space:

```text
R_H,N : H_N^k -> (H_N^k)^*.
```

For any `x in C_N^k`, define its harmonic pairing

```text
lambda_x(h) := <x,h>_N for h in H_N^k.             (L1-12)
```

The orthogonal projection is exactly

```text
P_H,N x = R_H,N^(-1)(lambda_x).                    (L1-13)
```

Equation `(L1-13)` uses no cycle basis.  It says that the global harmonic
component is determined by all flux/holonomy pairings of `x` with the
record-visible harmonic cycles.  In a one-dimensional reciprocal loop with
harmonic cycle `c`, it reduces to

```text
P_H,N x = (<x,c>_N/<c,c>_N)c.                     (L1-14)
```

For an edge-supported `epsilon_e` with nonzero pairing, `(L1-14)` is
supported on the full loop.  This is not leakage into a disjoint physical
sector.  It is the cycle's global flux/holonomy charge.  Orientation reversal
changes the cycle and pairing together, leaving the family-covariant content
unchanged and selecting no orientation.

```text
WITHIN_CYCLE_GLOBALITY = LAWFUL_PHYSICS / PROVABLE
RECIPROCAL_LOOP_SPREADING = REQUIRED_BEHAVIOR / PROVABLE
```

## 2. L2 - Contact-reducing theorem

### 2.1 What reduction would require

Let `I_N^k` be the finite contact subspace at degree `k`, and let

```text
E_C,N^k : C_N^k -> I_N^k
```

be its orthogonal projection in the ratified metric.  Since
`Delta_N^Hdg` is self-adjoint and finite-dimensional, the following are
equivalent:

```text
Delta_N^Hdg(I_N^k) subset I_N^k;
(I_N^k)^perp is also invariant;
[E_C,N^k,Delta_N^Hdg]=0.                         (L2-1)
```

Any condition in `(L2-1)` makes `I_N^k` reducing.  Functional calculus then
gives

```text
[E_C,N^k,P_H,N]=0,
P_H,N(I_N^k) subset I_N^k.                       (L2-2)
```

Equation `(L2-2)` is exactly what is needed for the Hodge projector to
descend through the contact quotient/pushout.  The stronger graded
subcomplex condition

```text
d_N E_C,N = E_C,N d_N,
delta_N E_C,N = E_C,N delta_N                   (L2-3)
```

implies `(L2-1)`, but is not necessary for projector descent.

### 2.2 A4 does not imply reduction

A4 supplies:

```text
represented/contact overlap equality;
signed pushout;
Eta composition;
beta cocycle, restriction, reality, units, Ward, support,
OLD_FID, RNL, LR, and subextensivity.              (L2-4)
```

No clause in `(L2-4)` names `Riesz_N`, `delta_N`, `Delta_N^Hdg`, `E_C,N`,
or a commutator among them.  Ward annihilation alone does not supply an
adjoint-invariant contact subcomplex; Q-408 already admits Ward-transverse
objects with off-diagonal support.

The non-implication has a finite countermodel.  Let the degree-one carrier be

```text
C^1 = span{e_c,e_b},
I_contact^1 = span{e_c},
g = identity,
A_epsilon = [[1,epsilon],[epsilon,1]],
0 < |epsilon| < 1.                                (L2-5)
```

`A_epsilon` is positive.  Let a two-term finite complex have

```text
C^0 = R^2,
d^0 = positive_square_root(A_epsilon),
d^1 = 0.                                          (L2-6)
```

Then `d^1 d^0=0`, and the degree-one Hodge Laplacian is

```text
Delta_1^Hdg = d^0 (d^0)^* = A_epsilon.            (L2-7)
```

The contact vector is outgoing-closed because `d^1 e_c=0`, but

```text
Delta_1^Hdg e_c = e_c + epsilon e_b
notin I_contact^1.                                (L2-8)
```

Make the represented carrier `C^1`, the contact carrier `I_contact^1`, and
their overlap `I_contact^1`; take represented and boundary transports to be
the identity, `beta=0`, reality to be ordinary conjugation, and support to be
one connected region.  The strict pushout and every applicable law in
`(L2-4)` pass.  RNL has no disjoint-sector antecedent in this one-region
model.  Yet `(L2-1)` fails by `(L2-8)`.

This countermodel uses a genuine positive finite Hilbert complex.  It is not
an abstract-kernel substitution and does not alter any A4 overlap datum.

```text
A4_IMPLIES_CONTACT_REDUCING = false / PROVABLE
REDUCING_DERIVABLE = false / PROVABLE
```

### 2.3 Reduction is not obstructed

Set `epsilon=0` in the same construction, or use an actual orthogonal direct
sum in which the contact complex is one summand.  Then `(L2-1)` holds and all
A4 laws continue to hold.  Thus the existing stack admits both reducing and
nonreducing models.

```text
REDUCING_OBSTRUCTED = false / PROVABLE
REDUCING_STATUS = INDEPENDENT_OF_CURRENT_RATIFIED_CLAUSES
```

### 2.4 Full-gate authoring surface

The exact authored candidate needed by this certificate would be:

```text
CONTACT_LAPLACIAN_REDUCING_CANDIDATE (YOURS)

For every admitted finite stage and relevant degree, the actual contact
subspace I_contact,N is invariant under the ratified Hodge Laplacian:

  Delta_N^Hdg(I_contact,N) subset I_contact,N,

equivalently [E_C,N,Delta_N^Hdg]=0.  The family is covariant under admitted
relabeling/reality, unit-correct, restriction-compatible on every licensed
old image, and no member, basis, complement, or scale is selected.
```

It is minimal for a Laplacian-reducing theorem: one commutator condition is
added, with no new coefficient.  It would require a principal amendment
because DoR-020-A1 declared the clause layer complete and A4 did not add this
operator law.  This lane does not adopt it.

| Alternative | Exact content | Consequence | Tag |
|---|---|---|---|
| harmonic-only preservation | `[E_C,N,P_H,N]=0` | enough for this projector, not for the Laplacian or full Hodge calculus | YOURS, weaker |
| Laplacian reducing | `(L2-1)` | canonical functional-calculus descent | YOURS, candidate |
| full Hilbert subcomplex | both equations `(L2-3)` | stronger d/delta descent | YOURS, stronger |
| partial/reject | retain fixed-stage Hodge but no contact quotient | certificate and J2 remain open | lawful rejection |

Failure-capable void conditions for any future reducing member are:

1. an actual contact vector with a noncontact component in
   `Delta_N^Hdg c`;
2. failure of the A4 overlap equality or any A4 void condition;
3. deletion of a `D_G^*`-visible bulk or harmonic cycle;
4. failure of reality, units, restriction, OLD_FID, RNL, or LR;
5. choosing a contact complement, commutator, or member from a reader,
   response, threshold, fixed point, end test, or numerical consequence;
6. failure of common-refinement coherence for the reducing family.

```text
REDUCING = AUTHORABLE
AUTHORED_HERE = false
```

## 3. L3 - Refinement naturality and the J15 mate

### 3.1 Exact projector comparison theorem

For an admitted arrow `f:N->M`, let

```text
rho_f^k : C_M^k -> C_N^k                         (L3-1)
```

be the sealed downward restriction.  The two typed intertwining equations
needed at degree `k` are

```text
rho_f^(k+1) d_M^k = d_N^k rho_f^k,
rho_f^(k-1) delta_M^k = delta_N^k rho_f^k.        (L3-2)
```

When `(L3-2)` holds, direct substitution gives

```text
rho_f^k Delta_M^Hdg = Delta_N^Hdg rho_f^k.        (L3-3)
```

Because both finite spectra are finite, choose a polynomial `p` on their
union with `p(0)=1` and `p(lambda)=0` at every nonzero spectral value.  Then

```text
P_H,M = p(Delta_M^Hdg),
P_H,N = p(Delta_N^Hdg).
```

Applying `(L3-3)` to the polynomial proves the contravariant naturality
square

```text
rho_f^k P_H,M = P_H,N rho_f^k.                    (L3-4)
```

This theorem is `PROVABLE`; its premises, not its algebra, are the live gap.

### 3.2 Proven scope

On a rank-preserving W3 arrow, the retained inclusion `j_f` is isometric and
the finite restriction is its adjoint:

```text
rho_f = j_f^*.                                    (L3-5)
```

Where the actual bundle/incidence transport is a chain map,

```text
d_M j_f = j_f d_N,                                (L3-6)
```

taking adjoints with `(L3-5)` gives the second mate in `(L3-2)`.  The sealed
pullback differential square gives the first.  Therefore `(L3-4)` is derived
on the rank-preserving identity/Ref_path and actual automorphism scopes where
both chain and adjoint equations are certified.

An isometry without `(L3-6)` is insufficient.  V001's permanent witness

```text
Delta_2^Hdg S(1) != S Delta_1^Hdg(1)              (L3-7)
```

still kills that inference.

```text
RANK_PRESERVING_PROJECTOR_NATURALITY = DERIVED_ON_INTERTWINING_SCOPE
HODGE_FROM_ISOMETRY_ALONE = REFUTED / TYPE-R
```

### 3.3 General cycle-creating arrows

On a cycle-creating arrow, the stack supplies a downward old-image
restriction but no representative-independent upward physical quotient.
W3 does not provide the isometric-inclusion/adjoint pair there.  A1 supplies
the geometric `d` pullback on its admitted support scope, but no sealed clause
supplies the second equation in `(L3-2)` for the new-cycle complement.

The exact missing object is

```text
CYCLE_CREATING_HODGE_ADJOINT_MATE_CERT:
  rho_f delta_M = delta_N rho_f
  on the actual contact/Maxwell symbol carrier,
  compatible with support, units, reality, and old-image restriction.
                                                               (L3-8)
```

It cannot be replaced by an upward map; doing so would violate FC4 and the
cycle-creating no-lift theorem.

### 3.4 Relation to J15

J15 supplies the independently derived bottom mate

```text
r_f^Bot pi_M Eta_f = pi_N.                         (L3-9)
```

Equation `(L3-9)` compares old finite bottoms after forward response
transport.  It does not mention `d`, `delta`, `Delta^Hdg`, or `P_H`, so it
does not imply `(L3-4)`.

If the local-symbol map `Loc` has its sealed restriction square and if
`(L3-4)` is independently proved, the projected mate is

```text
r_f^Bot pi_M P_H,M Loc_M Eta_f
 = pi_N P_H,N Loc_N.                              (L3-10)
```

Equation `(L3-10)` is the exact lawful comparison: a downward bottom mate,
never an upward projector lift.  It is derived on the rank-preserving scope
of Section 3.2 and conditional elsewhere on `(L3-8)` plus contact reduction.

```text
J15_IMPLIES_HODGE_NATURALITY = false / PROVABLE
PROJECTED_J15_MATE = DERIVED_CONDITIONALLY / form_(L3-10)
NATURALITY = OPEN
NATURALITY_GAP = CYCLE_CREATING_HODGE_ADJOINT_MATE_CERT
```

## 4. L4 - Maximal Cert V002 assembly

### 4.1 Corrected field ledger

| Certificate field | Source or proof | Status | Tag |
|---|---|---|---|
| actual finite record complex and `d_N` | Q-408/A1 | built | PROVABLE premise |
| positive carrier metric/Riesz maps | DoR-019 | ratified | mixed derived/authored premise |
| `delta_N`, `Delta_N^Hdg`, finite closed ranges | `(L1-2)` and finite rank | derived | PROVABLE |
| fixed-stage Hodge decomposition/projector | V001/Q-468 and `(L1-3)` | derived | PROVABLE |
| corrected sector locality | `(L1-4)`-`(L1-9)` | derived on certified direct sums | PROVABLE / premise-marked |
| within-cycle global charge | harmonic pairing `(L1-12)`-`(L1-14)` | derived | PROVABLE |
| contact reduction | absent; countermodel `(L2-5)`-`(L2-8)` | open | AUTHORABLE |
| rank-preserving naturality | `(L3-2)`-`(L3-6)` | derived on certified scope | PROVABLE |
| all-arrow naturality | missing adjoint mate `(L3-8)` | open | TYPE-U |
| J15 projected mate | `(L3-10)` | conditional | PART-PROVABLE |
| normalized Maxwell coefficient line | V001, branch `m_T,N != 0` | carried without change | PROVABLE on branch |
| reader independence | dependency order below | pass | PROVABLE |
| DoR-008 finite shadows | no finite kernel/value changed | pass | PROVABLE |

The corrected locality field for V002 is therefore

```text
PROJECTOR_LOCALITY_V002 :=
  blockwise on every certified disjoint-sector Hilbert direct sum;
  RNL/LR compatible across those sectors;
  harmonic/flux globality allowed inside each connected cycle. (L4-1)
```

The false V001 field

```text
supp(P_H x) subset supp(x) for every within-cycle x
```

is deleted.  It is not weakened to make a preferred output pass; it is
removed because no ratified law owns it and the reciprocal-loop geometry
refutes it.

### 4.2 Conjunctive verdict

The named certificate requires all fields, not only fixed-stage Hodge.  Since
contact reduction is unratified and all-arrow naturality lacks `(L3-8)`, the
V002 certificate cannot be issued.

```text
FINITE_Q408_TO_LOCAL_MAXWELL_HODGE_PROJECTOR_CERT_V002
 = BLOCKED(
     CONTACT_LAPLACIAN_REDUCING_THEOREM,
     CYCLE_CREATING_HODGE_ADJOINT_MATE_CERT
   ).                                             (L4-2)
```

This is a typed construction boundary, not a fence stop and not a proof that
the two fields are physically impossible.

```text
CERT_V002 = BLOCKED(contact_reducing + all_arrow_adjoint_intertwiner)
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```

### 4.3 What the complete certificate would hand forward

If a principal ruling supplied a reducing member and a later construction
proved `(L3-8)`, the completed certificate would hand the next consumer a
reader-independent family

```text
Q408 finite profile
 -> actual local symbol/contact carrier
 -> P_H harmonic Maxwell component
 -> normalized coefficient on the nonzero m_T branch,             (L4-3)
```

with corrected sector locality, lawful within-cycle globality, contact
descent, and the contravariant naturality square `(L3-4)` on every arrow.
This statement does not pose J2, compare two readers, or assert its equality.

```text
J2_POSED = false
J2_EQUALITY_CLAIMED = false
READER_MEMBER_SELECTED = none
```

## 5. L5 - Battery and regressions

### 5.1 F_PLDEC circularity

Construction order is

```text
actual complex + ratified metric
 -> Riesz adjoint
 -> Hodge Laplacian
 -> spectral projector
 -> sector/contact/naturality tests
 -> only then the conditional Maxwell coefficient interface.       (L5-1)
```

No reader, `chi_K`, `T`, response value, threshold, fixed point, end test, or
number appears before the certificate fields are frozen.

```text
F_PLDEC_CIRCULARITY = EXCLUDED / PASS
READER_REFERENCED = no
```

### 5.2 Hodge license distinction

| Claim | Result |
|---|---|
| fixed-stage Hodge from ratified metric plus actual `d` | DERIVED |
| Hodge from isometry alone | REFUTED by `(L3-7)` |
| rank-preserving naturality with chain and adjoint intertwiners | DERIVED |
| all-arrow naturality from W3 alone | NOT DERIVED |
| within-cycle point locality | NOT RATIFIED and geometrically false |
| block locality on a certified Hilbert direct sum | DERIVED |

### 5.3 Reciprocal-loop lawful-behavior regression

Let `c` be the full reciprocal-loop harmonic cycle and let `epsilon_e` be an
edge-supported input with nonzero harmonic pairing.  The required result is

```text
P_H epsilon_e
 = (<epsilon_e,c>/<c,c>)c,
supp(P_H epsilon_e)=supp(c).                       (L5-2)
```

A candidate returning an edge-supported harmonic vector, or zero despite the
nonzero pairing, fails the Hodge theorem.  Spreading around this connected
cycle is now a passing regression, not a locality failure.

```text
RECIPROCAL_LOOP_MUST_SPREAD = PASS
NONSPREADING_PROJECTOR = REJECTED
```

### 5.4 Additional failure-capable checks

| Attack | Result |
|---|---|
| disjoint certified sectors | block formula `(L1-8)` gives zero cross-sector component |
| Q-430 metric mixer | disjoint labels without the LOE/RNL direct-sum premise are rejected, not promoted to `(L1-4)` |
| Q-432 `P=id` | remains admitted; no global orthogonality among unrelated pre-existing sectors is imposed |
| contact mixing | `(L2-8)` refutes automatic reduction while preserving A4 |
| direct-sum contact control | `epsilon=0` proves reduction is consistent and not obstructed |
| refinement mismatch | any failure of `(L3-3)` refutes the projector square |
| cycle-creating upward map | none introduced; only the downward mate `(L3-10)` is licensed |
| zero Maxwell normalization | `m_T,N=0` voids the coefficient branch; no denominator is inserted |
| hidden basis | spectral projection and harmonic Riesz pairing select no basis |
| hidden units | `Delta^Hdg` is an endomorphism in one unit class; all C/K passage stays on R4 |

### 5.5 Geometry versus rails

```text
SURFACE GEOMETRY:
  actual finite differential complex;
  certified disjoint support sectors;
  connected reciprocal cycles and their flux/holonomy pairing;
  actual contact subspace;
  old-image restrictions and target-only new cycles.

RAILS:
  direct-sum notation;
  spectral functional calculus;
  pushout presentation;
  mate-square bookkeeping;
  certificate and condition tags.
```

The sector theorem is geometric only when an actual LOE/RNL term supplies
the direct-sum premise.  The contact-reduction gap is geometric because the
ratified Laplacian may mix an actual contact vector with bulk content.  The
generality gap in `(L3-8)` is likewise operator geometry, not a missing
diagram label.

### 5.6 Anti-tuning ledger

```text
1  verify V001 and the register before reading;
2  freeze the ratified metric, differential, and A4 carrier;
3  derive the direct-sum Hodge theorem before considering J2;
4  sweep the ratified locality clauses;
5  retain reciprocal-loop spreading as lawful behavior;
6  construct both reducing and nonreducing contact models;
7  type the reducing choice surface without adopting it;
8  derive the exact Laplacian-intertwiner theorem;
9  compare its premises with W3/A1/J15;
10 stop the certificate at the two absent fields.
```

No consequence-facing datum influenced a definition or choice.

## Final board

```text
SECTOR_LOCALITY = PROVEN
REDUCING = AUTHORABLE
NATURALITY = OPEN
CERT_V002 = BLOCKED(contact_reducing + all_arrow_adjoint_intertwiner)
READER_REFERENCED = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
