# STAGE 8 TASK 5 / EQ6 — REVIEW OF THE LOC BUILD + THE HOL PROVENANCE DETERMINATION — DARIO V001

Date: 2026-08-05
Lane: Dario (Claude Opus 5), cross-family reviewer and adjudicator of record
Task: PASTE 570 / Task 5 / EQ6
Under review: `STAGE8_TASK5_EQ6_THE_LOC_BUILD_LANE3_V001.md` (`b53d9e93…`, verified, 1,325 lines)
Prior of record: my seed adjudication (`e287b057…`), verified.

## Lead result

```text
REGISTER_HEAD = Q-496

LOC_BUILD = CONFIRMED (+3 items, none fatal)
  The specification, the negative derivability result, the candidate family, the
  no-selection discipline, and the false-anchor avoidance all hold. The build is
  honest about its own scope in its Lead and its board.

B5C_THEOREM = CONFIRMED (+family-wide over L_F2 exactly as claimed)
  BUT: the (C1) membership clause ENTAILS the negation of the seed condition (S28),
  so the theorem's hypothesis contains its conclusion; and its scope does NOT reach
  F^2-compatibility. The register headline "F^2 CANNOT THREAD THE LOOP" over-reads it.
  The build's own Lead does not -- it says "the minimal F^2-compatible branch".

HOL_PROVENANCE = A1_AMENDMENT_NEEDED
  +GAP 1 (decisive, and prior to every value question): (B6) demands a map OUT OF A
   KERNEL SPACE, D_N^Loc -> im(P_H,N). Holonomy is a function of (loop, connection)
   and carries no kernel argument. A1 supplies no correspondence D_N^Loc -> {cycles}.
  +GAP 2: units -- a U(1) holonomy is a dimensionless phase; im(P_H,N) carries the
   ratified DoR-019 unit classes; no conversion is licensed.
  +GAP 3: A1 is expressly "law-only" and its field-torsor horn permits the empty
   torsor, which "supplies no witness"; and members are retained whole, so the
   period's VALUE is family-valued.
  The structural half IS carried: A1 adopts the U(1) bundle WITH CONNECTION and
  states "transport derived from the declared members". So H2 was the right question
  and the derivation reaches transport -- one step short of any value, two steps
  short of a map out of D_N^Loc.

VERB_AUDIT_SELF = CLEAN (+1 disclosed correction of a prior framing of my own)

MEMBER_BOUND = false ; FIXED_POINT_EXECUTED = false ; END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = false (the build's own appeal stands; I add none)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

**The headline.** The build is good work and its central negative result is right. But the theorem it
returns is narrower than the record has taken it to be, and the enlargement route it names does not
close: the Wilson-line discovery **relocates** the program's open question rather than answering it.
Before, the question was whether the `F^2` source threads the loop. Now it is whether the adopted
connection's period on the record-visible loop is nonzero, and whether any map carries a source
kernel to that period at all. Both are open, and the second is open for a *type* reason that no
forcing theorem about periods would repair.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-496 | verified |
| Build `b53d9e93…`, 1,325 lines | verified before reading |
| Where-clauses V005 `19b20603…`; projector cert `0bef9a00…`; my seed adjudication `e287b057…` | verified |
| Output name absent before construction | verified — no clobber |

## 1. H1 — review of the build

### 1.1 (a) (B5c) — the algebra is right; the scope is not what the record took it to be

[PROVABLE] **The algebra, recomputed.** For harmonic `c` (so `d c = 0`) and `M := delta^(k+1) d^k`,

```text
<M v, c> = <delta d v, c> = <d v, d c> = <d v, 0> = 0,
```

degree-correct, by adjointness. Hence `ran(M) perp im(P_H)`, and with `P_H` self-adjoint and
`c in im(P_H)`, `<x,c> = <P_H x, c>`, giving `q_T,N(L) = 0` for every `L in L_F2`. **(B5c) is a
correct universal statement over `L_F2`. No member of `L_F2` evades it, and I could not construct one
— nor should one exist.**

[PROVABLE] **But the family is defined by the conclusion.** The final membership clause of (C1) reads

```text
iota_N^H Loc_N^phys(kappa_T,N)  in  closure(ran(M_N^(Hdg,k))).
```

Since `Loc_N^C = iota_N^H o Loc_N^phys`, and (see below) `ran(M) subset ker(P_H)`, this clause says
`P_H,N Loc_N^C(kappa_T,N) = 0` — which is **exactly the negation of (S28)**, the seed condition, stated
at build line 684 as `P_H,N Loc_N^C(kappa_T,N) != 0`. The theorem's hypothesis therefore contains its
conclusion.

[PROVABLE] **The clause is also strictly stronger than (B5c) needs, and the surplus is unexplained.**
I recomputed: on a finite carrier with `delta^(k+1) = (d^k)^*`,

```text
C^(k+1) = ran(d^k)  (+)perp  ker(delta^(k+1))
=> delta^(k+1)(C^(k+1)) = ran(delta^(k+1) d^k) + 0
=> ran(M^(Hdg,k)) = ran(delta^(k+1)).
```

Meanwhile `ker(P_H) = im(P_H)^perp = ran(d^(k-1)) (+) ran(delta^(k+1))` by the cert's own (1-9). So

```text
ran(M) = ran(delta^(k+1))  STRICTLY INSIDE  ker(P_H)   whenever ran(d^(k-1)) != 0,
```

which is generic. (B4)/(B5) use **only** orthogonality to `im(P_H)`, i.e. only membership in
`ker(P_H)`. The clause as written additionally deletes the entire **exact** sector `ran(d^(k-1))`,
for no stated reason. The minimal clause supporting (B5c) is literally `not-(S28)`.

[PROVABLE] **The range clause is not inherited from the specification — it is an extra cut at (C1).**
The build's own compatibility-fiber decomposition defines the Hodge fiber as

```text
Hdg := { (iotatilde_N^H, iota_N^H)_N satisfying (S14),(S19),(S21),(S25),(S25b),
         and every Hodge diamond equation },
```

and **none** of those clauses mentions `d`, `delta`, `ran`, `M^(Hdg,k)`, or `P_H`. The correction set
at (D9) varies only `Loc^phys` and is forced to `A_N(kappa_T,N) = 0` by the symbol-side pin (S15a).
**So the symbol side is rigid at `kappa_T` and the Hodge side is free in exactly the direction an
evasion would need.** The build's own (D10)–(D11) concede the point: they contemplate a gate-satisfying
package with `P_H,N iota_N^H A_N(K) = a_N(K) c_N` and compute that it *shifts* the loop pairing.

[PROVABLE] **Consequence, stated exactly.** An `F^2`-compatible package can satisfy every other clause
of (C1) and fail the range clause; such a package is outside `L_F2` and unreached by (B5c). Therefore

- (B5c) establishes: *members defined to have no harmonic component have no harmonic pairing*;
- (B5c) does **not** establish: *`F^2`-compatibility implies no harmonic pairing*.

[PROVABLE] **The build is honest; the register is not.** The build's Lead says only "the minimal
`F^2`-compatible branch has no route to a harmonic flat-holonomy line", flags "The family may be
empty", and calls (C1) "an authorable full-gate candidate". The register row Q-496 states flatly
"**F² CANNOT THREAD THE LOOP — THE COUPLING ENTERS THROUGH HOLONOMY OR NOT AT ALL.**" That is stronger
than (B5c) supports. **Item 1 for the build: the range clause's status as `not-(S28)` should have been
displayed at (C1), and the exact-sector surplus explained or dropped.**

[PART-PROVABLE] I note this cuts *toward* the build's own conclusion in one respect: since the clause
is `not-(S28)` plus surplus, (B5c) is best read not as a discovery but as a **consistency check** —
confirming that the `F^2` branch, once you require it to have no harmonic component, indeed has none.
The genuinely informative content is elsewhere: in the specification, the negative derivability result,
and the (B6)/(B7) enlargement analysis.

### 1.2 (b) Void conditions and the no-selection discipline — PASS, with one item

[PROVABLE] Fourteen void conditions are present at §2.5, and they are of the falsifiable kind rather
than restatements of construction steps. Void 12 is the sharpest and I verified it verbatim: "Any
`L in L_F2` has `P_H,N iota_N^H Loc_N^phys(kappa_T,N) != 0`. Such a witness voids `L_F2`; a separately
declared and falsifiable `Hol_N` seam belongs to a different candidate family." That is directly
falsifiable by an exhibited member, and it is the correct dual of (B5c) — it means the theorem is not
protected by fiat: a single exhibited member with nonzero harmonic component voids the family rather
than being explained away.

[PROVABLE] **No-selection: PASS.** The build selects no route, no map member, no field/gauge/frame
representative, no scale, no slice, no cycle generator, and no coefficient. The principal symbol is
taken only where it exists; lower-order differences fall in `ker(sigma_2^op)` before the quotient. The
family is retained whole.

[PROVABLE] **False-anchor avoidance: PASS, and exemplary.** The build reproduces the physical-J2
equation of record and states at its Lead that it "is not used as a premise, definition, normalization
proof, or existence theorem below." I checked the construction order; it is not so used. My
FALSE-ANCHOR finding from the seed adjudication is honored correctly.

[PROVABLE] **Item 2 for the build:** the fourteen voids are stated for the candidate family; none of
them fires on the *scope* question raised in §1.1 (that the family may be narrower than
`F^2`-compatible). A fifteenth void — "an `F^2`-compatible package satisfying (S2b)–(S27) but failing
the range clause" — would have caught it.

### 1.3 (c) The A1 flat-holonomy fence — correctly invoked

[PROVABLE] The fence's content: two connections may have identical curvature and identical
characteristic class while differing by a closed non-exact 1-form, hence having inequivalent holonomy
around a non-bounding cycle. **Holonomy carries strictly more information than curvature.** The
record's reciprocal loop is such a cycle (`H_N_RL = span{c_RL}`, `c_RL != 0`).

[PROVABLE] The build invokes it in the licensed direction — "curvature/`F^2` data cannot be relabeled
as a Wilson period" — which is exactly "you cannot derive a period *from* curvature". It needs nothing
stronger. **PASS.**

[PROVABLE] **Item 3, and it matters for H2:** the fence cuts both ways and the build does not record
the second edge. If holonomy carries strictly more information than curvature, then `Hol_N` is not
merely an *additional* term — it carries information `F^2` data **provably cannot contain**. Hence
`Hol_N` can never be derived from `F^2`-side data, and the (B7) enlargement is not a refinement of
localization but a genuinely new physical input. The build's phrase "a hidden holonomy counterterm,
not localization" gestures at this; the fence proves it.

## 2. H2 — the HOL provenance determination

### 2.1 What A1 actually adopted

[PROVABLE] DoR-020-A1's ruling, verbatim on the second clause:

> **THE LOCAL FIELD MEMBERS — typed as a U(1) BUNDLE WITH CONNECTION over the record surface, with the
> bundle lift/pullback-bundle isomorphism, smooth full-rank, and characteristic-class compatibility;
> transport derived from the declared members. Law-only.**

[PROVABLE] Two halves, both load-bearing. **"Transport derived from the declared members"** — so
parallel transport, and hence the holonomy of a closed loop of actual paths, is a *derived* property
of an adopted member, not a new datum. I verified the mechanism: `eta_conn,R(A_G') := tilde_f_R^* A_G'`
with `tilde_f_R` a U(1)-equivariant connection-preserving bundle map, so horizontal lifts correspond
and transport is natural. **H2 was the right question and its structural premise is sound.**

[PROVABLE] **"Law-only"** — and both clauses carry it. The adopted where-clause text contains **zero**
occurrences of "holonomy" and **zero** of "Wilson"; it supplies connection, curvature, `c_1`, pullback
compatibility, and transport. Its field-torsor horn states: "empty torsor is allowed as a set but
**supplies no witness**", with an explicit "empty/reject horn". Q-438 records the clause layer as
complete with "everything left is construction and witness."

[PROVABLE] No topological forcing is present. The only integral-class condition is the *relative*
`c_1(P_G) = f_R^* c_1(P_G')`, satisfied by `c_1 = 0` on both sides and used "as a necessary membership
test, not as an existence theorem". And it is the **wrong degree**: `c_1 in H^2` constrains curvature
flux over 2-cycles, while the sector at issue is flat and the object needed is a period around a
non-bounding 1-cycle. No amount of strengthening `c_1` reaches it.

### 2.2 GAP 1 — the type gap, decisive and prior to every value question

[PROVABLE] (B6) demands

```text
Hol_N : D_N^Loc -> im(P_H,N),
```

and the build's own (S8) gives the domain explicitly:

```text
D_N^Loc = span{kappa_T,N} + iota_N^Q408(Kernbar_N^cyc(O_N^cyc)).
```

**That is a space of kernels.** A connection holonomy has signature `(loop, connection) -> U(1)`; it
takes no kernel argument. So no evaluation of an adopted connection is `Hol_N` without an intervening
correspondence `D_N^Loc -> {cycles}` (or `-> H^1`).

[PROVABLE] A1's path/current clause does not supply one. Its current condition is a *naturality law
for currents across arrows* — `partial_G' s_R = s_R^0 partial_G`, `ker(S_R) = {0}`,
`J_G'(S_R c) = f_(R*) J_G(c)` — relating currents already given, on both sides of an arrow. It is not a
construction of a loop from a Maxwell source kernel. And the clause is labelled "law-only".

[PROVABLE] **This obstruction is insensitive to every value question.** Even a sealed, pinned, nonzero
reciprocal-loop period would not constitute `Hol_N`, because nothing carries `kappa_T,N` to a loop.
Conversely, no forcing theorem about periods — of any degree — would settle it. **This is the exact
gap, and it is the same source-to-loop coupling the program has been missing since the seed.**

### 2.3 GAP 2 — units

[PROVABLE] A U(1) holonomy is a dimensionless phase valued in a circle group, not a linear space; its
logarithm is a period carrying connection units. The target `im(P_H,N) subset C_N^k` carries the
ratified DoR-019 unit classes. No conversion between them is licensed by the adopted text, and DoR-019
does not license the symbol-to-Hodge cross-sector conversion in any case. This gap rides on GAP 1 —
fixing the domain without fixing the codomain units would leave `Hol_N` ill-typed on the other side.

### 2.4 GAP 3 — witness and value

[PROVABLE] A1 is law-only and its field-torsor horn permits the empty torsor, which "supplies no
witness". So the adopted law establishes no inhabitant.

[PART-PROVABLE] And the value is not determined. Members are retained as whole covariant families with
no selection. One correction I make against a tempting argument, because it would put a false
prohibition into the record: **the no-selection discipline is *not* the bar here.** Closed-loop U(1)
holonomy is gauge-*invariant* — for `A -> A + d log g`, `∮ d log g in 2 pi i Z` — so retaining the full
gauge family leaves every closed-loop period untouched. Any indeterminacy must come from the
*connection torsor* (closed non-exact deformations), not from the gauge family. Whether the sealed
finite connection data pins the reciprocal-loop period on the sealed skeleton is **not settled by the
where-clauses either way**, and settling it is a lane audit against DoR-008, not a reading.

### 2.5 The determination

[PROVABLE] **`HOL_PROVENANCE = A1_AMENDMENT_NEEDED`.** The A1 member's holonomy exists with genuine
provenance — the connection is adopted and transport is derived from the declared members — but three
required properties of (B6) are not carried by the adopted text: the **domain correspondence**
(decisive), the **unit conversion**, and any **witness**. The amendment candidate for the principal is
therefore a where-clause amendment supplying a sealed correspondence

```text
Xi_N : D_N^Loc -> {record-visible cycles}  (or -> H^1),
```

with its own provenance, units, covariance, restriction, and falsifiers — after which `Hol_N` would be
the composite of `Xi_N` with the already-derived transport. **I do not draft that amendment here and
none is adopted**; its content is a new physical correspondence (which source kernel encircles which
loop), and that is a principal's ruling, not a lane's.

[PROVABLE] **What this does NOT change.** My seed typing stands: `SEED_TYPE = END_TEST_STRUCTURAL`.
The holonomy route does not close the nonvanishing question — it **relocates** it, from "does the
`F^2` source thread the loop" to "does the adopted connection have a nonzero period on the
record-visible loop, and does anything carry the source to it". Both remain conditions. Membership V002
remains DEFECTIVE on D1/D2/D3/D6, all independent of this. J2 and J7 gain no premise: the physical
`Loc` is still unbuilt, and (B7) without (B6) is, in the build's own correct words, "a hidden holonomy
counterterm, not localization."

## 3. H3 — the physical reading

[PART-PROVABLE] The record has now derived, from its own structure rather than by assumption, that a
pure field-strength action cannot produce the coupling at issue: the loop the coupling would have to
act on is a flat direction, carrying holonomy but no field strength, and an `F^2`-type kernel is blind
to exactly such directions. That is the Aharonov–Bohm structure arriving as a consequence rather than
an input, and it is a real result — with the caveat established above that it is proved for the branch
that was *defined* to have no harmonic component, not yet for every `F^2`-compatible localization. What
follows for what `alpha` *is* on this surface depends entirely on the determination. If a
source-to-cycle correspondence were derived from the adopted law, then `alpha` would be a statement
about a **Wilson period of the record's own connection** — the coupling would be topological in
character, living in how the record's paths encircle one another rather than in any local field
intensity, and the constant would be a property of the surface's connectivity. If instead the
correspondence has to be authored, then the program would be *declaring* the channel through which
charge couples to geometry, and `alpha` would inherit exactly the status of that declaration — derived
in its structure, posited in its channel. And if the period is pinned to zero by the sealed finite
data, the whole coefficient route closes and the coupling must enter somewhere the program has not yet
looked. The honest position today is the middle one is not yet available and the first is not yet
earned: the record has proved where the coupling *cannot* come from, and named — but not built — the
only place it can.

## 4. H4 — verb audit on my own board

| My board line | Strongest verb my sources carry | Honest? |
|---|---|---|
| `LOC_BUILD = CONFIRMED (+3 items)` | specification, negative result, voids, no-selection and false-anchor all verified by me | **CLEAN** — I report it as confirmed despite raising the scope item |
| `B5C_THEOREM = CONFIRMED` | algebra recomputed; no member of `L_F2` evades | **CLEAN** — and I attach the scope rider rather than letting "CONFIRMED" imply the headline |
| range clause entails `not-(S28)` | (S28) at build line 684; `ran(M) = ran(delta) subset ker(P_H)` recomputed by me | **CLEAN** |
| `HOL_PROVENANCE = A1_AMENDMENT_NEEDED` | A1's "transport derived from the declared members" + "Law-only"; (S8)'s kernel-space domain; zero occurrences of holonomy/Wilson in the adopted text | **CLEAN** |
| GAP 3 value question | corrected: gauge-invariance means no-selection is *not* the bar; left open rather than claimed | **CLEAN** — I declined an argument that would have supported my conclusion but was wrong |

[PROVABLE] **One disclosed correction of my own prior framing.** In my seed adjudication I recorded the
`delta d` orthogonality as a "structural headwind" and noted it was blocked by the symbol-vs-operator
type shift. This build converts that headwind into (B5c) by *adjoining the range clause as a membership
condition* — i.e. by assuming the very identification I flagged as missing. My original caveat was
therefore correct and remains the right reading; what I did not anticipate is that the gap would be
closed by definition rather than by construction. I record this so the register does not carry my
earlier headwind as though it had been independently upgraded to a theorem about `F^2`.

```text
VERB_AUDIT_SELF = CLEAN (+1 disclosed correction)
```

## 5. Fence and stopping board

```text
B5C = CORRECT OVER L_F2; hypothesis entails conclusion; scope does not reach F^2-compatibility
REGISTER_HEADLINE = OVER-READ relative to both (B5c) and the build's own Lead
HOL_N = NOT DERIVABLE FROM A1 AS ADOPTED (+domain correspondence; +units; +witness)
A1_AMENDMENT_CANDIDATE = named, NOT DRAFTED, NOT ADOPTED
SEED_TYPE = END_TEST_STRUCTURAL (unchanged; the open value is relocated, not closed)
PHYSICAL_LOC = still unbuilt
MEMBERSHIP_THEOREM = still DEFECTIVE (D1/D2/D3/D6 stand, independent of this)
MACHINERY_APPEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No register, plan, tracker, git, commit, push, member-binding, fixed-point, end-test, or evaluation
action was performed by this lane. No law was adopted and no amendment was drafted.

LOC_BUILD = CONFIRMED (+item 1: the (C1) range clause entails `not-(S28)` and carries an unexplained
surplus deleting the exact sector — its status should be displayed at (C1); +item 2: no void condition
fires on the scope question, and a fifteenth would have caught it; +item 3: the A1 fence cuts both ways
and the second edge — that `Hol_N` carries information `F^2` provably cannot contain, so it can never
be derived from `F^2`-side data — is not recorded)
B5C_THEOREM = CONFIRMED (+family-wide over `L_F2` exactly as claimed, and no member of `L_F2` evades
it; +but the membership clause is the negation of the seed condition, so the hypothesis contains the
conclusion, and an `F^2`-compatible package satisfying (S2b)–(S27) may fail the range clause and be
unreached — the register headline "F² cannot thread the loop" is not established, though the build's
own Lead is correctly scoped)
HOL_PROVENANCE = A1_AMENDMENT_NEEDED (+GAP 1, decisive and prior to all value questions: (B6) needs a
map out of the kernel space `D_N^Loc = span{kappa_T,N} + iota^Q408(Kernbar^cyc(O^cyc))`, while holonomy
is a function of (loop, connection) with no kernel argument, and A1's path/current clause is a
covariance law for currents across arrows, not a construction of a cycle from a source kernel; +GAP 2:
a dimensionless U(1) phase against the ratified DoR-019 unit classes on `im(P_H,N)`, no licensed
conversion; +GAP 3: A1 is "law-only" with an empty-torsor horn that "supplies no witness", and the
period's value is family-valued — though NOT for the no-selection reason, since closed-loop U(1)
holonomy is gauge-invariant; the candidate amendment is a sealed correspondence
`Xi_N : D_N^Loc -> {record-visible cycles}` with its own full gate, named here and neither drafted nor
adopted)
VERB_AUDIT_SELF = CLEAN (+1 disclosed correction of my own prior framing)
