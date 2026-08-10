# STAGE 8 — AXN — THE CHAIN INSTANCE AND THE RECEIVER BINDING
## DARIO LANE — RELAY 924 — `[PLAN:AXN-BUILD-D22]`

## 0. Preflight

Relay 924 verified before reading at
`ae409880d0b385fc87405abc5b0273829887b1f8d3ee48bf972188e318e63958`. Lane guard read DARIO; the
pickup ACK was written before content access. `PROGRAM_STATE_BRIEF_V005.md` verified and read before
task work at `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`. Both subjects
verified against their own sidecars before reading. The output name and its sidecar were clear.

---

## 1. Law-9b closure — declared first

```text
C_924 = {
 1  RELAY_PASTE_924_CHAIN_INSTANCE_DARIO_V001.md
      ae409880d0b385fc87405abc5b0273829887b1f8d3ee48bf972188e318e63958
 2  supervision/PROGRAM_STATE_BRIEF_V005.md
      e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c
 3  STAGE8_AXN_SPEC_ACTS_DARIO_V001.md                                  [my 916 — subject]
      241ccf880266a895f5955173c8c87e7d180d8c6ba6dffefd10f257267454eca1
 4  STAGE8_AXN_SPEC_SUPPLEMENT_CHECKS_CODEX2_V001.md                    [922 — governing]
      9000b4e994bac24857338026f98b06500d6b424dd8c79af25930ab27e6f79bb6
 5  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md            [PARENT / DESCEND]
      40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9
 6  STAGE8_T7_HERMITE_GALERKIN_BASELINE_SPEC_V001.md                    [the named Galerkin family]
      80aa4e1722c117e8195ce0fb2ae3fc37262bc8fc2ba5d79a6dd38cd1029bc26d
 7  STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md          [the governing correction]
      a1258dcf40732f0e3fce358a68ffdbd34bc347d70283550440582a1129bec510
 8  STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md [pins member 7's digest]
      seal verified against its own sidecar; carries `a1258dcf40732f0e…`
 9  STAGE8_AXN_SUPPLEMENTS_DARIO_V001.md                                [my 920 — corrected in §3.4]
      2a829a35eb5fb6cf0b8dc1ca8c4c07848684d1958a787cadb070f4dcc0df8ba9
}
```

| key | sealed bytes | span SHA-256 | content |
|---|---|---|---|
| `PARENT` | member 5 `[5711,6867)` | `eddc2e9ab66e1036e7defdc514b61214e0adef3b48fced3c3aa7a67b6df5f2c3` | `S_n`, `h_0[g,a]`, `h_K(t)`, the Galerkin permission, `H_K = dGamma_R(h_K)` |
| `DESCEND` | member 5 `[6867,7879)` | `827cf361f052d36c62e7fc6ea57e61c04cf8c18fc552dcde18bd7ee5e5ef8e3a` | `D_K`, `C_K(x)`, `D_K^2` |

Member 6 verified against its own sidecar. Member 7 carries no own sidecar; it is named as *"the
authority correction"* by member 6 and its digest is pinned inside member 8, whose own seal verified —
the same in-text-pin route used at 911 and 920.

**Name probe.** `STAGE8_AXN_CHAIN_INSTANCE_DARIO_V001.md` and its sidecar: clear at pickup.

---

## 2. Gates and standing

```text
alpha_computed         = false
proof_authorized       = false
kappa_record_computed  = false
JOINT_ANCHOR_DERIVED   = false
```

Every headline determination is **CLAIMED** pending the opposite-lane check. **Nothing here touches
the adopted anchor, the gauntlet, or any core-gated object**: no gauntlet clause was evaluated, no
anchor field was read for content, and no core-gated quantity was consulted. No member was bound; no
fixed point was executed; no end test was run; no physical quantity was numerically evaluated; no
measured constant was consulted. PE-1 through PE-13 remained pointer-only. Builder-A code paths were
not accessed.

**922 governs and I accept it without qualification.** At 916 I wrote `LINE6 = 2/3 booked` with the
source third BOOKED. 922 rules it **specified-conditional, not booked**: I supplied a schema and
took credit for an instance. My own 916 text shows the seam — `ACT_I = DERIVED (schema and
embeddings)` followed by `source BOOKED` — and I let the second claim inherit the first's credit.
Members 3 and 9 are mine and carry no confirming weight here.

---

## 3. Item 1 — the chain instance

### 3.1 What the record actually supplies

Member 6 names a Galerkin family:

```text
Q_(n,ell) L2(R3) = span{ phi_a(x/ell) phi_b(y/ell) phi_c(z/ell) : 0 <= a,b,c < n },
spinor carrier = tensor with C4.
"The spaces are nested in n and their union is a core for the free Dirac operator."
```

Three of the requirements are visible in that sentence: **finite rank**, **nested**, and a **core**
for the free operator. The last is exactly what `GC-6` demands, and it is of record rather than
authored.

### 3.2 What the governing correction then says

Member 7 is the authority correction member 6 itself names. It withdraws the earlier family
outright — a nested finite-rank `Q_n` commuting with `h_0` *"does not exist for the free massless
Dirac multiplier"*, since a nonzero finite-dimensional reducing subspace would give `h_0` an `L2`
eigenvector while its spectrum is purely continuous — and then states the requirements a genuine
family must meet:

```text
Q_n is finite rank and nested;
Q_n -> I strongly;
Q_n h_0 Q_n converges to h_0 on a common core;
Q_n M_c(t) Q_n converges strongly to M_c(t);
and the finite propagators converge strongly, uniformly on compact times.
```

with the sealed statuses

```text
genuine_finite_rank_continuum_restriction_constructed = false
parent_state_regulator_restriction_derived            = false
```

and, under **Next executable target**: *"Construct a target-free nested Galerkin family on the
actual continuum one-particle space, compress `h_0`, `M_c(t)`, `h_K(t)`, `P_-` … A pass requires an
analytic strong-propagator approximation theorem and a Schatten/phase argument for the completed
modulus; numerical convergence alone cannot promote the result."*

### 3.3 The verdict on item 1

Sealing a chain instance would require constructing that family and proving four convergence
statements — **the record's own next executable target**, expressly requiring an analytic
approximation theorem. Member 6's own status line calls its baseline *"a convergence diagnostic. No
finite value is a coupling or a proof of the continuum limit."*

```text
INSTANCE = NOT-DERIVABLE.

AUTHORITY TABLE (law 9b), at the pinned members:
  member 7  genuine_finite_rank_continuum_restriction_constructed = false
  member 7  parent_state_regulator_restriction_derived            = false
  member 7  the five requirements a genuine family must satisfy, displayed
  member 7  "Next executable target: Construct a target-free nested Galerkin family…"
  member 6  self-typed "a convergence diagnostic", not a continuum-limit proof
```

### 3.4 Two corrections to my own 920, both mine to make

**(i) "The record names no Galerkin chain" — WRONG.** Member 6 names a candidate family, in a file
whose name contains `GALERKIN`, and that filename appeared in my own terminal output at relay 916. I
saw the name and did not open the file. That is the **fourth** instance of the query-shape failure
that produced 869, 860 and the 921 denominator miss — and this one needed no query at all, only
opening a file already in front of me.

**(ii) `SUPPLEMENT-916-1` typed as "a naming act, cheapest kind, selects no physical content" —
WRONG.** It is not a naming act. Per member 7 it is a **construction plus a convergence theorem**,
carrying an analytic strong-propagator approximation requirement, and it is the record's own named
next executable target. It is among the most expensive supplements on the list, not the cheapest. The
mis-pricing was mine and it is withdrawn.

### 3.5 What does stand: the schema-level embeddings, re-run fresh

These are properties of the **schema**, uniform over admissible chains, so they survive the instance
stop. Re-run in this relay rather than carried from 916:

```text
CAR(K_2) -> CAR(K_3):   generator embedding  0.000e+00   unital 0.000e+00
                        multiplicative 0.000e+00   *-preserving 0.000e+00   isometric 8.882e-16
CAR(K_3) -> CAR(K_4):   generator embedding  0.000e+00   unital 0.000e+00
                        multiplicative 0.000e+00   *-preserving 0.000e+00   isometric 0.000e+00

record-side inclusion:  || iota(c)^2 - iota(c^2) ||              = 0.000e+00
                        || iota(G)iota(c) + iota(c)iota(G) ||    = 0.000e+00
composition:            source-then-record vs record-then-source = 0.000e+00
```

The joint stage map is `(CAR functorial inclusion) tensor (A |-> A tensor I)`, both of the form
`A |-> A tensor I` in the chain-compatible Jordan–Wigner presentation, and the two orders of
composition agree exactly.

---

## 4. Item 2 — the receiver binding

922 lists four deficiencies. §4.1 closes the first, §4.2 supplies the second and corrects my 916 in
doing so, and §4.3 shows the remaining two are **one** obstruction.

### 4.1 GC-3, narrowed — and what my 920 self-check missed

922's ruling: GC-3 *"broadens compression from the parent-authorized `M_c(t)` to arbitrary 'parent's
own named operators' `T`"* and so *"fails authority-neutrality"*. `PARENT` authorizes Galerkin
compression of **"this multiplication operator"** — `M_c(t)` — and nothing else. I adopt 922's
minimal repair verbatim:

```text
GC-3  COMPRESSION. Finite-stage operators are P_n M_c(t) P_n for the multiplication
      operator whose Galerkin compression the parent explicitly authorizes. Any other
      P_n T P_n requires its own sealed authority; this schema grants none.
```

**What my 920 check should have caught.** My content-free table asked two questions of each clause —
*does it select anything?* and *is it uniform over admissible chains?* GC-3 passes both: it selects
no value and is chain-uniform. **Neither question can see an authority expansion.** The criteria were
the wrong criteria, and a clause-by-clause check run with the wrong criteria is a clean bill of
health that means nothing. The missing third question is *does it enlarge what the record permits?*
I record that as the defect in my method, not merely in the clause.

### 4.2 The closed signature — and my 916 split was scope-mixed

922: *"A lawful componentwise split can use those two scopes, but it must name the map, domains,
embeddings, and recombination. 916 displays no such closed signature."* Supplying it exposes an error
in the split itself.

```text
CARRIERS
  one-particle   H_1   = K_Sigma tensor R(K),   K_Sigma = L2(Sigma, S tensor L^q)
  stage n        H_1^n = K_n tensor R(K),       Pi_n = P_n tensor I_R(K)
  field          F     = Fock(K_Sigma) tensor R(K)      F_n = Fock(K_n) tensor R(K)
  target         A_SR  = CAR(K_Sigma) tensor R(C)       A_SR^n = CAR(K_n) tensor R(C)

MAP    dGamma_R : fiber-preserving one-particle operators on H_1 -> operators on F,
       acting as dGamma on the K_Sigma factor, identity on R(K).
       SEALED SCOPE: argument h_K(t) only — one occurrence in member 5.

SUMMANDS (DESCEND: exactly two)
  A = i gamma^mu nabla_mu      one-particle UNBOUNDED
  B = i gamma^5 C_K            one-particle BOUNDED   (||M_c|| <= 1; gamma^5 bounded; v_c scalar)

THE SETTLED CRITERION, APPLIED AT A COMMON SCOPE — like against like:
  stage n, both compressed : Pi_n A Pi_n and Pi_n B Pi_n are FINITE RANK, hence trace-class,
                             hence BOTH lifts BOUNDED and BOTH members of A_SR^n.
  uncompressed, both       : NEITHER is trace-class — M_c is an infinite-rank multiplication
                             operator — hence BOTH lifts unbounded and BOTH affiliation-typed.

RECOMBINATION  dGamma is linear, so dGamma_R(D_K) = dGamma_R(A) + dGamma_R(B) at a COMMON scope:
  at stage n     a member of A_SR^n, being a sum of two members;
  uncompressed   affiliated, with domain fixed by dGamma_R(A) — the summand whose
                 ONE-PARTICLE operator is unbounded.

EMBEDDINGS     A_SR^n -> A_SR^m  =  (CAR functorial) tensor (A |-> A tensor I);  §3.5 residuals.
```

**The correction this forces.** My 916 wrote the split as *write term IN, differential term
affiliation-typed*, as though both were classified at one scope. They were not: it compared a
**compressed** write term against an **uncompressed** differential term. At a common scope the two
summands fall on the **same** side — both members at stage `n`, both affiliated uncompressed. The
genuine difference between them is at the **one-particle boundedness** line, not the
membership/affiliation line, and it surfaces in the **domain** of the affiliated operator rather than
in its membership. 922 called the binding incomplete; completing it shows the split was also
mis-scoped, and that is mine.

### 4.3 The two remaining deficiencies are one

922's items 3 and 4 — that `dGamma_R` is applied only to `h_K`, and that the differential-to-`h_0`
slicing identity is unstated — are **the same obstruction**. `dGamma_R`'s domain is one-particle
operators on `K_Sigma`; `D_K` is a covariant spacetime kernel. **`D_K` is not on `dGamma_R`'s domain
carrier until it is sliced.** So extending the lift's argument is not a separate spec act: it is
gated on precisely the slicing datum my 920 stopped and priced as `SUPPLEMENT-916-2`.

```text
BINDING = INCOMPLETE.
  CLOSED here : the authority narrowing (§4.1); the full signature — map, carriers, domains,
                embeddings, recombination (§4.2); S_n's Hermiticity forcing, carried through
                as S_n = (-slash n)(i gamma^5) with the conversion fixed by self-adjointness.
  REMAINING   : exactly ONE obstruction — the slicing datum. 922's items 3 and 4 collapse to it.
```

---

## 5. Line 6

```text
LINE6_SOURCE = STILL-CONDITIONAL, on one named datum (the slicing), with:
  the chain instance    NOT-DERIVABLE (authority table, §3.3) — and re-priced from a naming
                        act to a construction plus convergence theorem;
  the receiver binding  INCOMPLETE with its signature now closed and its remaining
                        obstruction reduced from two items to one.
```

The record third stays booked at Q-820; the field third stays core-gated. **The source third does
not book here, and I decline to book it** — booking it loosely once is what 922 corrected, and doing
it again on a smaller margin would be the same error.

---

## 6. FREEDOMS-CONSUMED (law 2a)

```text
JOINT_ANCHOR_INPUT   = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  922's rulings as governing; the parent spec's PARENT/DESCEND spans;
  member 6's named Hermite family and member 7's requirements and statuses;
  the settled trace-class criterion (922: CONFIRMED as theorem);
  my 916 and 920 as corrected subjects, with zero confirming weight.

CONDITIONED-ON:
  section 4.2's boundedness of B on ||M_c|| <= 1, which is what a spatial-section
    multiplication operator is; and on M_c being infinite-rank, which is what makes
    its compression necessary in member 7's own requirement list;
  section 4.3's collapse on dGamma_R's domain being one-particle operators on K_Sigma,
    which is how member 5 uses it.

SUBSTITUTED:
  NOTHING. No chain, subspace, projection, basis, ordering, slicing datum, lapse, shift,
  lift extension, or booking was authored or selected. GC-3's repair is 922's own text
  adopted verbatim, not a clause of mine. The instance is reported NOT-DERIVABLE rather
  than constructed.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

---

## 7. Flattening check, verb audit, byte audit

**FLATTENING CHECK — S01–S37 walked, clean.** A schema was not identified with an instance — that is
922's correction and §3 keeps it. A named candidate family was not identified with a constructed one:
member 6 names, member 7 records the construction as pending. Three visible requirements were not
identified with five. A diagnostic was not identified with a continuum-limit proof. Compressed and
uncompressed scopes were not compared as though equal — §4.2 exists because 916 did exactly that. A
classification was not identified with a binding. Two deficiencies were not left as two when they are
one. An honest `NOT-DERIVABLE` was not converted into a booking.

**BUILDER-B INDEPENDENCE:** derived from sealed sources and the opposite lane's ruling. Members 3 and
9 are mine and appear only as corrected subjects. A's code was not accessed.

**SELF VERB AUDIT.** "Not-derivable" is used once, for the instance, with its authority table
displayed. "Narrowed" is used for GC-3 and the narrowing is 922's text, adopted rather than
paraphrased. "Closed" is used for the signature and "incomplete" for the binding that contains it —
both in the same sentence so neither can be read as the other. "Wrong" is used twice, for my own 920
statements, without softening. No instance, booking, lift extension, or slicing datum is claimed.
`VERB_AUDIT_SELF = CLEAN`.

**BYTE-POSITION SELF-AUDIT.** §1's heading begins at byte **569**, its closure fence opens at byte
**618**, and the exact member list ends at byte **2043**. A scan of bytes `[0,618)` over `no `,
`not `, `none`, `never`, `absent`, `missing`, `without`, `lack`, `fail`, `gap`, ` open`,
`unresolved`, `underived`, `false`, `cannot`, `zero`, `stop`, `block`, `wrong`, `refus`, `unswept`,
`unsealed` returns **zero hits**.

---

## 8. Final lines

```text
CLOSURE = declared-first (sec-1 heading 569, closure fence 618, members end 2043; pre-closure scan over 22 forms = 0 hits)
INSTANCE = NOT-DERIVABLE. The record NAMES a candidate Galerkin family (Hermite Q_(n,ell), nested, union a core for the free Dirac operator — which is GC-6's obligation discharged of record), but its own authority correction records genuine_finite_rank_continuum_restriction_constructed = false and parent_state_regulator_restriction_derived = false, states the five requirements a genuine family must satisfy, and names constructing it as the NEXT EXECUTABLE TARGET requiring an analytic strong-propagator approximation theorem; the baseline self-types as a convergence diagnostic. TWO CORRECTIONS TO MY OWN 920, BOTH MINE: (i) "the record names no Galerkin chain" is WRONG — it names one, in a file whose name contains GALERKIN that appeared in my own terminal output at 916 and which I did not open; fourth instance of the query-shape failure, and this one needed no query, only opening a file in front of me. (ii) SUPPLEMENT-916-1 typed as "a naming act, cheapest kind" is WRONG — it is a CONSTRUCTION PLUS A CONVERGENCE THEOREM and the record's own next executable target, among the most expensive supplements rather than the cheapest. The mis-pricing is withdrawn.
RESIDUALS = shown, re-run fresh this relay: CAR(K_2)->CAR(K_3) and CAR(K_3)->CAR(K_4) generator embedding 0.000e+00, unital 0.000e+00, multiplicative 0.000e+00, *-preserving 0.000e+00, isometric 8.882e-16 and 0.000e+00; record-side inclusion ||iota(c)^2-iota(c^2)|| = 0.000e+00 and ||iota(G)iota(c)+iota(c)iota(G)|| = 0.000e+00; composition source-then-record against record-then-source 0.000e+00. These are SCHEMA-level and uniform over admissible chains, so they survive the instance stop.
BINDING = INCOMPLETE, with the signature now CLOSED. Supplied: carriers, the map with its sealed argument scope, both summands, the settled criterion applied AT A COMMON SCOPE, the recombination, and the embeddings. S_n's Hermiticity forcing carried through as S_n = (-slash n)(i gamma^5). THE COMPLETION EXPOSES AN ERROR IN MY 916 SPLIT: "write IN / differential AFFILIATED" compared a COMPRESSED write term against an UNCOMPRESSED differential term. At a common scope both summands fall on the SAME side — both members at stage n, both affiliated uncompressed, since M_c is an infinite-rank multiplication operator and so is not trace-class either. The genuine difference is at the ONE-PARTICLE BOUNDEDNESS line, not the membership line, and it surfaces in the DOMAIN of the affiliated operator. REMAINING: exactly ONE obstruction — 922's items 3 and 4 are the SAME thing, since dGamma_R's domain is one-particle operators on K_Sigma while D_K is a covariant spacetime kernel, so extending the lift's argument is gated on the slicing datum 920 already stopped and priced.
GC3 = NARROWED to the parent-authorized multiplication operator M_c(t) only, adopting 922's minimal repair verbatim; any other P_n T P_n requires its own sealed authority and this schema grants none. AND THE METHOD DEFECT NAMED: my 920 content-free table asked only "does it select anything?" and "is it uniform over admissible chains?" — GC-3 passes both, and NEITHER QUESTION CAN SEE AN AUTHORITY EXPANSION. The missing third question is "does it enlarge what the record permits?" A clause-by-clause check run with the wrong criteria is a clean bill of health that means nothing.
LINE6_SOURCE = STILL-CONDITIONAL on one named datum, the slicing. Record third booked at Q-820; field third core-gated. I DECLINE TO BOOK THE SOURCE THIRD — booking it loosely once is what 922 corrected, and doing it again on a smaller margin would be the same error.
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
```
