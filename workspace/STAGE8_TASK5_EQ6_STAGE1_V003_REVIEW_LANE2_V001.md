# STAGE 8 TASK 5 / EQ6 — REVIEW OF RECORD: STAGE-1 V003 ON THE ADOPTED ROWS — LANE 2 V001

```text
ARTIFACT_TYPE = ADVERSARIAL_REVIEW_OF_RECORD
LANE = CODEX_LANE_2
ARTIFACT_UNDER_REVIEW = STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md
ARTIFACT_UNDER_REVIEW_SHA256 = a46beae26048a0d093de339363fb8597d362a0101d103cfc06305edabac53f4c
REGISTER_HEAD_STATED = Q-467
REGISTER_HEAD_VERIFIED = Q-468
Q468_EFFECT_ON_REVIEW = NONSUPERSEDING; relay 544 remains queued

STAGE1_V003 = DEFECTIVE (H1,H5,H6)
FC_SUPPLIED = FC2, FC4, FC13; FC1/FC7/FC8/FC9 carried; FC3 and FC5 not confirmed; FC10 partial; FC11 open; FC12 struck

MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The adopted A3 and A4 rows are not rejected here.  The A4 signed pushout and
the J15 contravariant mate recompute.  The defect is in V003's implementation
of the A3 family as one all-arrow functor: its arrow-local flat action is
promoted to a simultaneous family action with a missing target term, and its
relation composition proves closure but not the reverse factorization needed
for equality of relation arrows.  These are repairable rail/family-naturality
defects, not a new physical counterexample to either adopted row.

## 1. Preflight, custody, and authorities

### 1.1 Three-line preflight

```text
DOES_THE_OBJECT_EXIST = yes
  | the Lane-1 V003 artifact exists locally and in the archive mirror
IS_THE_VERSION_CURRENT = yes through Q-468
  | the relay stated Q-467; Q-468 is later parallel Hodge work and expressly
    leaves relay 544 queued, so it does not supersede this review
ARE_ITS_INPUTS_PRESENT = yes
  | A3, A4, the determination map, V002 review, and the reviewed artifact exist
NO_CLOBBER = pass
  | this review filename was absent locally and in the archive before writing
```

The canonical `LOCKED_PROCESS.md` was read in full.  The questions-settled
register sidecar verified and the live register SHA-256 was
`6ecd91139c0e62c81053fff0b5fb03efb5f2424939943a17a7b0342a823ba502`.

### 1.2 Hash-verified load-bearing authorities

| Authority | SHA-256 | Use |
|---|---|---|
| artifact under review | `a46beae26048a0d093de339363fb8597d362a0101d103cfc06305edabac53f4c` | reviewed construction |
| DoR-020-A3 J4 relational increment groupoid | `07e0e50145314fe5c30b7f7b5637d4c8add0834c631ad9c2e16209bf3b5a9d6f` | adopted J4 row |
| DoR-020-A4 J12 strict signed pushout | `5fd95472bd6f0507a371779505fe91e2c3c4657ee3afc664ca563a3743d668a4` | adopted J12 row and five voids |
| determination map | `76ee3c695b1c0c02986a13ff64d6db93f76e39c6861b40273bd31aed1c3a2eb0` | A3/A4 derivation and J15 mate standard |
| V002 review of record | `312dbe14efebd167b5287ccde773d69e64eb17b9bcfe91137d1e4cea50b15e0e` | old killers and geometry/rails split |
| continuum constraint arm | `d7dcbc3ad7c470c8aaf0d8407db625d3e910cf180cd7b035fbc96bdfe58471b4` | prior J4/J12/J15 and joint-equalizer typing |

Both decision-file sidecars and the reviewed source's local/archive bytes
verified.  No register, plan, tracker, git, commit, or push action is performed.

### 1.3 Verdict table

| Item | Verdict | Reason |
|---|---|---|
| H1 A3 conformance and consumers | **KILL** | the arrow-local A3 equations and consumer tags pass, but V003's claimed simultaneous flat-family action omits `+psi_M`, and its relation-span proof gives only closure, not equality/factorization |
| H2 A4 strict pushout | **PASS** | the adopted overlap equality is imposed exactly on `C_N`; the quotient computation is well-defined; the five voids are live; no twist is absorbed |
| H3 J15 contravariant mate | **PASS** | the cycle-creating calculation uses only the downward old-image restriction; FC4 holds and no non-carrying coordinate inherits contravariance |
| H4 old killers | **PASS** | the incompatible/vertical pair is absorbed exactly when flat and admissible; the overlap-decomposition collision is killed by the signed pushout relation |
| H5 FC ledger | **KILL** | FC2/FC4 are supplied, but FC3 and full-family FC5 are overclaimed; consequently FC10 stays partial and the stated stage-2 remainder is incomplete by the bounded A3 repair |
| H6 fresh attack | **KILL** | a nonzero intermediate-stage flat change makes V003's displayed family action violate its own cocycle; explicit computation below |

## 2. H1 — A3 conformance and the consumer audit

### 2.1 What matches the adopted row

For an admitted arrow `f:N->M`, V003 correctly carries

```text
I_M = I_N o rho_f + v_f,
v_(gf) = v_f o rho_g + v_g,
v_id = 0,
D^2 I_M = rho_f^*(D^2 I_N) + D^2 v_f.              (H1-1)
```

Its arrow-local source move also matches A3 literally:

```text
I_N' = I_N + psi_N,
I_M' = I_M,
v_f' = v_f - psi_N o rho_f.                         (H1-2)
```

Indeed `I_N' o rho_f+v_f'=I_M`.  No member is selected and the
rank-preserving identity-extension case `v_f=0` recovers the old restriction
formula.  The Hessian equation is differentiated only after retaining `v_f`,
which is the correct order.

### 2.2 Four-consumer recomputation

Let `j_active^k psi_N=0` for every finite `k`, as required of the admitted
flat family on the sealed active section.

#### Invariant consumer 1 — Q-243/Q-279 retarded finite block

The finite ordered retarded block is a finite active derivative of the
restricted action/functional.  Under `I_N -> I_N+psi_N`,

```text
Ret_N(I_N+psi_N)-Ret_N(I_N)
 = RetExtract_N(j_active^2 psi_N)
 = 0.                                                 (H1-3)
```

The exact Q-279 probe-on value therefore remains the sealed zero retarded
block.  This does not say the noise/probe blocks vanish; it says the flat
action increment contributes no active finite jet to them.  The table's
finite-active invariance tag passes.

#### Invariant consumer 2 — Q-309 finite kernel and mixing blocks

Each of the kernel, kernel-complement, and kernel-`R` finite blocks is formed
from active finite first/second derivatives.  Therefore

```text
Delta Block_Q309 = linear combination of j_active^1 psi_N
                                      and j_active^2 psi_N
                  = 0.                               (H1-4)
```

The table's invariant tag passes on the exact sealed scope.

#### Member-sensitive consumer 1 — off-section action value

For an off-section point `y`, flatness on the active section does not imply
`psi_N(y)=0`.  Thus

```text
I_N'(y)-I_N(y)=psi_N(y),                              (H1-5)
```

which can be nonzero.  V003 correctly tags the action value/off-section germ
as member-sensitive.

#### Member-sensitive consumer 2 — off-section Hessian/stationary family

At an off-section point,

```text
D^2 I_N'(y)-D^2 I_N(y)=D^2 psi_N(y),                 (H1-6)
```

and the stationary equation changes by `D psi_N(y)`.  V003 correctly retains
the full family rather than declaring these consumers invariant.

The audit found no consumer labeled invariant whose value moves on the
consumer's declared finite-active scope.  In particular, V003 does not call
the completed response or the off-section action invariant.

### 2.3 First defect — the simultaneous family action is not the displayed action

V003 goes beyond the arrow-local calculation and says a compatible family
`{psi_N}` preserves composition.  If every stage member changes, however,
the relation on `f:N->M` must transform as

```text
I_N' = I_N + psi_N,
I_M' = I_M + psi_M,
v_f' = v_f + psi_M - psi_N o rho_f.                  (H1-7)
```

This is forced by the relation equation.  V003 instead retains (H1-2), which
sets the target change to zero.  For composable `f:N->M` and `g:M->L`, applying
the V003 rule at each source gives

```text
v_f'  = v_f  - psi_N o rho_f,
v_g'  = v_g  - psi_M o rho_g,
v_gf' = v_gf - psi_N o rho_gf.                       (H1-8)
```

Then

```text
v_f' o rho_g + v_g'
 = v_gf' - psi_M o rho_g,                            (H1-9)
```

not `v_gf'` unless `psi_M o rho_g=0`.  No adopted clause imposes that
vanishing.  By contrast, (H1-7) cancels the intermediate terms and obeys the
cocycle exactly.

This does not refute A3's local orbit move.  It refutes V003's claim that the
same two-term formula is already a simultaneous compatible-family action.

### 2.4 Second defect — relation closure is not relation equality

V003 defines `Rel_f` as all displayed triples satisfying the local relation.
For composable arrows it proves

```text
Rel_g o Rel_f subseteq Rel_gf.                       (H1-10)
```

That is closure: a composable pair produces a lawful composite increment.
A functor into a relation/span category requires the equality

```text
Rel_g o Rel_f = Rel_gf,                              (H1-11)
```

or an explicitly typed lax/pseudofunctor with a stated comparison cell.
V003 proves neither the reverse inclusion nor a comparison cell.  A direct
`gf`-increment must be shown to factor through an admissible intermediate
`I_M` with separately admissible `v_f` and `v_g`; the local equation alone
does not provide that support/certificate-preserving factorization.

The bounded repair is to define relation terms as restrictions of one actual
retained global R1 family member and prove that every `Rel_gf` term so defined
has its same-member intermediate term.  Alternatively the result must be
retagged as a lax relation construction.  V003 does neither.

```text
H1 = KILL
INVARIANT_CONSUMER_MOVEMENT_WITNESS = none
A3_LOCAL_RELATION = CONFIRMED
A3_ALL_STAGE_FAMILY_ACTION = DEFECTIVE
A3_RELATION_FUNCTOR_EQUALITY = UNPROVEN
```

## 3. H2 — A4 signed pushout and the nontrivial-overlap test

### 3.1 Adopted construction

V003 uses precisely

```text
C_N = R_N^rep intersect I_N^contact,
Delta_N = {(c,-c):c in C_N},
P_N = (R_N^rep direct_sum I_N^contact)/Delta_N,       (H2-1)

Eta_f[r,b]
 = [Eta_f^rep(r), eta_f^boundary(b)],
eta_f^boundary|C_N = Eta_f^rep|C_N.                  (H2-2)
```

The equality is imposed only on the actual common subspace `C_N`; no equality
is imposed on exclusive represented or exclusive contact directions.

### 3.2 Independent nontrivial-overlap computation

Take

```text
R_N^rep     = span{r,c},
I_N^contact = span{c,b},
C_N         = span{c} != {0}.
```

Let the two component transports send the common generator to the same
`c_f`, while sending `r` and `b` to arbitrary lawful exclusive images.  The
same pushout class has representatives

```text
[r+a c,b] = [r,b+a c].                               (H2-3)
```

Their images differ by

```text
(a c_f,-a c_f) in Delta_M,                           (H2-4)
```

so they are equal in `P_M`.  Hence response depends only on the pushout class.
If the boundary leg carried a twist `u(c_f)!=c_f`, (H2-4) would be replaced by
`(a c_f,-a u(c_f))`, which is not generally in `Delta_M`; the map would fail
to descend.  Thus V003 has not silently absorbed a contact twist.  Its
`Tw_f=0` detector is exactly failure-capable.

### 3.3 Five live voids

1. Unequal overlap images fail the calculation above.
2. Both canonical injections are injective: `[r,0]=0` forces `r=0`, and
   `[0,b]=0` forces `b=0`; no represented bulk cycle is deleted.
3. Composition, reality, units, Ward, restriction, support, OLD_FID, RNL, LR,
   and subextensivity descend only when their two legs agree on `C_N`; V003
   states and uses that premise rather than deriving it from the quotient.
4. The overlap identification is the adopted A4 member, not an automorphism
   selected from a later consumer.
5. A future actual `Tw_f!=0` immediately voids the member.  The only nonzero
   twist in the checked stock is A4's declined countermodel, not actual data.

```text
H2 = PASS
SIGNED_PUSHOUT = CONFORMING
NONTRIVIAL_OVERLAP = WELL_DEFINED
CONTACT_TWIST_ABSORBED = false
```

## 4. H3 — J15 mate on a cycle-creating arrow

Let `f:N->M` be the one-edge-to-parallel-edge cycle-creating arrow.  The old
cycle quotient at `N` is zero and `M` has a nonzero new-cycle direction `z`.
The lawful bottom map is downward:

```text
r_f^Bot : Bot_M^resp -> Bot_N^resp,
r_f^Bot(z)=0.                                         (H3-1)
```

For a source response class `x=[r,b]_N`, V003's A4 map may have a target-only
component:

```text
Eta_f(x)=j_old(x)+a(x)z.                              (H3-2)
```

The mate computation is

```text
r_f^Bot pi_M^resp Eta_f(x)
 = r_f^Bot pi_M^resp(j_old(x)+a(x)z)
 = pi_N^resp(x),                                      (H3-3)
```

using exact old-image restriction.  The target class `z` remains nonzero in
`P_M`; only its restriction vanishes.  No map `Bot_N^resp->Bot_M^resp` is
constructed and no value is assigned to the new cycle.  This is FC4 exactly.

For `N->M->L`, the variance is

```text
r_gf^Bot = r_f^Bot o r_g^Bot,
Eta_gf = Eta_g o Eta_f,                              (H3-4)
```

and substitution into (H3-3) gives the composite mate.  The action coordinate
is carried by `Rel_f`, the response by `Eta_f`, and only the response-bottom
coordinate by `r_f^Bot`.  The Gate, action/Hessian, Ward, reader, WHERE, and
analytic entries retain their own sealed variances; V003 does not apply
`r_f^Bot` to them.

```text
H3 = PASS
J15_MATE = CONFIRMED_ON_CYCLE_CREATION
FC4 = HONORED
VARIANCE_LEAKAGE = none found
```

## 5. H4 — permanent old-killer regressions

### 5.1 V6 incompatible pair and vertical increment

For the prior pair

```text
I_N' = I_N+psi_N,
I_M' = I_M,
v_f' = v_f-psi_N o rho_f,                            (H4-1)
```

both triples satisfy the same target equation.  A3 retains them in the same
arrow-local groupoid orbit when `psi_N` and `v_f'` satisfy the adopted
flatness, support, covariance, and cocycle certificates.  If the mismatch is
not admitted/flat, it is excluded by `Rel_f`; it is not excluded by selecting
one member.  This is the adopted disposition.

### 5.2 Overlap-decomposition collision

For `c in C_N`, the formerly conflicting decompositions satisfy

```text
[c,0]_N=[0,c]_N,                                     (H4-2)
```

and their outputs agree by (H2-2).  A mismatch is exactly A4 void 1, not an
ambiguity hidden by notation.

```text
H4 = PASS
V6_PAIR = ABSORBED_IF_ADMITTED / EXCLUDED_IF_NONADMITTED
VERTICAL_INCREMENT = RETAINED
OVERLAP_COLLISION = ABSORBED_BY_SIGNED_PUSHOUT
```

## 6. H5 — FC ledger and exact remainder

| FC row | Independent review status | Reason |
|---|---|---|
| FC1 | carried/conditioned | actual finite carriers and adopted pushout are used; this build does not prove new inhabitance |
| FC2 | **SUPPLIED** | `Bot_N` is one multi-sorted bottom tuple; its response coordinate has the J15 mate and the other entries keep their sealed maps rather than inheriting response variance |
| FC3 | **NOT CONFIRMED** | the relation coordinate lacks (H1-11), so the asserted single `F_003` functor is not proved on all arrows |
| FC4 | **SUPPLIED** | only downward old-image response restriction on cycle creation |
| FC5 | **NOT CONFIRMED at full-family level** | the simultaneous flat-family action used in the covariance/family claim fails (H1-9) |
| FC6 | supplied only on adopted component scopes | A4 pushout regressions pass; this is not a stage-2 diamond theorem |
| FC7 | carried | A1 bundle law unchanged |
| FC8 | carried | finite analytic core unchanged |
| FC9 | carried/protected | both pushout injections are injective; no visible old class deleted |
| FC10 | **PARTIAL** | J12 and J15 pass; J4 needs the bounded family/factorization repair; physical J2 and J7 remain open |
| FC11 | **OPEN** | simultaneous equalizer diamonds are not built here |
| FC12 | struck | unchanged |
| FC13 | **SUPPLIED** | definitions follow A3/A4/bottom structure, with no downstream target used |

The stage-2 remainder in V003 is therefore underinclusive.  Before physical
J2, J7, and the joint diamonds can be the only remainder, the following
bounded stage-1 repair must land:

```text
1. install the all-stage flat-family transformation
     v_f' = v_f + psi_M - psi_N o rho_f;
2. define Rel_f by actual global-family provenance and prove
     Rel_g o Rel_f = Rel_gf,
   or retype the structure honestly as lax/pseudo with its comparison cell;
3. rerun the FC3/FC5 and J4 consumer-family certificates.
```

No A4 or J15 amendment is required by this review.

```text
H5 = KILL
NEWLY_GENUINE_FC_ROWS = FC2, FC4, FC13
FC3 = OPEN_BY_A3_FUNCTOR_REPAIR
FC5 = OPEN_BY_FULL_FAMILY_ACTION_REPAIR
FC10 = PARTIAL
FC11 = OPEN
```

## 7. H6 — fresh attack: the intermediate-stage flat change

Choose an admitted chain `N -f-> M -g-> L` and a nonzero admissible flat
`psi_M` with `psi_M o rho_g != 0`.  Set `psi_N=0` and leave `psi_L=0`.
V003's claimed family rule gives

```text
v_f'  = v_f,
v_g'  = v_g - psi_M o rho_g,
v_gf' = v_gf.                                        (H6-1)
```

Therefore

```text
v_f' o rho_g + v_g'
 = v_gf - psi_M o rho_g
 != v_gf'.                                           (H6-2)
```

All active finite jets can remain zero, so every finite-shadow regression can
still pass while the asserted family cocycle fails.  This is not the old V6
witness: V6 changes the source of one arrow while fixing its target.  The
fresh attack changes the intermediate object of a composable pair and tests
the simultaneous family structure V003 newly claimed.

The corrected rule (H1-7) admits the witness and restores the cocycle.  Thus
the defect is bounded and constructive, but it is real.

```text
H6 = KILL
FRESH_ATTACK = INTERMEDIATE_STAGE_FLAT_CHANGE
ATTACK_CLASS = RAIL/FAMILY_NATURALITY_DEFECT
PHYSICAL_CLASH = none established
```

## 8. Surface geometry versus rails

```text
SURFACE GEOMETRY:
  the actual vertical increments remain physical and unselected;
  the represented/contact overlap is glued by adopted A4;
  the target-only new cycle remains present while its old restriction is zero.

RAILS:
  V003's all-stage action formula and its relation-functor equality are
  bookkeeping/naturality claims.  They fail without changing the adopted
  surface content.  The repair must organize all retained members correctly;
  it must not delete an increment or select a section.

RAIL_ARTIFACT_FINDING:
  the defect is not a new-physics root and requires no principal choice;
  it is the missing target term plus the unproved relation factorization.
```

## 9. Final board

```text
H1 = KILL
H2 = PASS
H3 = PASS
H4 = PASS
H5 = KILL
H6 = KILL

STAGE1_V003 = DEFECTIVE (H1,H5,H6)
FC_SUPPLIED = FC2, FC4, FC13; FC1/FC7/FC8/FC9 carried; FC3 and FC5 not confirmed; FC10 partial; FC11 open; FC12 struck

CONTACT_TWIST_SEEN = none in actual checked stock
CLASH_FOUND = none at adopted surface geometry; rail/family-natural defects found
REPAIR_TYPE = BOUNDED_DERIVED_A3_IMPLEMENTATION_REPAIR

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
