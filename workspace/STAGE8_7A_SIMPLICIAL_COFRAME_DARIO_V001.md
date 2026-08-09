# STAGE 8 / 7A / STEP 8 — THE SIMPLICIAL COFRAME: FRAME DATA DERIVED, CLAUSE BARS IT BY EXACTLY 4!

Lane: DARIO (Builder B, independent verifier). Relay 753.
Governing: the booking 750 `57c55221…`; the frontier survey 751 `4d072e76…`.

## Lead determination

**The frame data derives cleanly. The clause will not take it, and the obstruction is a
single exact integer: `4! = 24`.**

**AE1 lands.** From `MAJ`'s sealed definition alone — the oriented order-simplex (Freudenthal)
subdivision of the unit 4-cube — the per-simplex frame is fully determined. One simplex per
permutation of `(0,1,2,3)`; edge-vector matrix = the staircase of partial sums;
**`det E = sgn(permutation)` for all 24**, verified exactly; `|det E| = 1` for every one;
four-volume `= |det E|/4! = 1/24` each; **sum `= 1`**. That reproduces `MAJ`'s sealed
`24 × 1/24` exactly. **Nothing is chosen** — every entry is computed from the sealed
coordinates.

**AE2 bars it, and the reason is structural, not a technicality.** `V011`'s general clause
encodes the cell's volume factor as **`|det e|`**. For a box that identification is exact —
the cell *is* the frame's parallelepiped. For a simplex it is false: the canonical frame gives
`|det E| = 1` while the cell's four-volume is `1/24`. **Off by exactly `4!`.**

**And no frame choice repairs it.** The discrepancy is the simplex-to-parallelepiped ratio,
which is combinatorial, not a frame normalization. Rescaling to force `|det ẽ| = 1/24` needs
`ẽ = E/λ` with `λ = 24^(1/4)` — **irrational**, in a construction the sealed sources carry in
exact rationals throughout (`MAJ`: *"re-derived exactly by iterated polynomial integration"*).
The repair would leave the arithmetic discipline the program works in.

**The sharpest form of the finding: this is a divergence between two sealed authorities, and
one of them already names the right answer.** `R33` — the executed STAGE7 packet result bound
to row A27 — rules that *"a subregion promoted to an elementary cell must be evaluated by that
child's intrinsic cell measure."* `MAJ` states that measure for an order-simplex: `|C|_4 =
1/24`. `V011`'s general-coframe clause computes `|det e| = 1` for the same child. **They agree
on boxes and diverge by `4!` on simplices.** The one-line statement needed is therefore not an
invention — it is a **reconciliation**, and `R33` already indicates which side it falls on. I
name it. I do not make it: that is a ruling.

```text
FRAME_DATA = derived (24 simplices, exact)
V011_CLAUSE = bars (one-line need named)
```

---

## 0. Preflight

### 0.1 Output name

Probed **before any write**, recursively over the archive: **absent**, artifact and sidecar
both. Nothing overwritten.

### 0.2 Sources verified before use

```text
MAJ    workspace/stage8_execution/work/MAJORANT_PHASE2_O3_O7_PROOF_DRAFT_V001.md   08b91543…
V011   workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/
         BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md                             aa7c6d49…
R33    workspace/R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md             e60aec3c…
750    workspace/STAGE8_7A_RESTRICTED_BOOKING_DARIO_V001.md                        57c55221…
751    workspace/STAGE8_7A_RA27_3_FRONTIER_DARIO_V001.md                           4d072e76…
738    workspace/STAGE8_7A_COUNTEREXAMPLE_CONTEST_DARIO_V001.md                    c854c8b2…
D012   workspace/STAGE8_TASK6_A25_A27_SCOPING_LANE2_V003.md                        74bbb7aa…
```

**Seal provenance stated precisely.** `V011` and `R33` carry **no adjacent sidecar**; both are
sealed by membership in `review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256`,
which lists `aa7c6d49…` and `e60aec3c…` respectively — I checked the manifest rather than
assuming a sidecar. All `V011` offsets are against `aa7c6d49…`, never the unsealed same-named
top-level file.

### 0.3 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
No member binding.  No fixed-point execution.  No end test.  No numeric evaluation of
PHYSICAL quantities — the exact-rational structural derivation of section 1 is the
commissioned task and touches no physical quantity.  No comparison to measured
constants.  No common cell formed.  No junction map evaluated.  No smooth data derived.
Nothing adopted.  No register, plan, tracker, or git action.
```

---

## 1. AE1 — THE FRAME DATA, DERIVED FROM THE SEALED COORDINATES

### 1.1 The sealed definition

[PROVABLE] `MAJ` `08b91543…[19632,19996)`:

```text
family-B member = the oriented order-simplex (Freudenthal) subdivision
(24 simplices, `|C|_4 = 1/24` each — re-derived exactly by iterated
polynomial integration).
```

That names the construction and fixes its two invariants: **24 cells**, each of four-volume
**`1/24`**.

### 1.2 The construction — nothing chosen

[YOURS] The order-simplex subdivision of the unit 4-cube assigns one simplex to each
permutation `p` of `(0,1,2,3)`. Its vertices are the monotone chain from `0` to `(1,1,1,1)`
that turns on coordinates in the order `p`:

```text
v_0 = (0,0,0,0)
v_k = e_(p(0)) + … + e_(p(k-1))          k = 1,2,3
v_4 = (1,1,1,1)
```

The **frame** is the edge-vector matrix `E_p` whose rows are `v_k − v_0`. Every entry is `0`
or `1`, read off the chain; **nothing is selected** — the permutation indexes the cell, and the
cell determines its frame.

### 1.3 The exact results

[YOURS, exact rational arithmetic] Computed over all 24 permutations:

| Quantity | Result |
|---|---|
| number of simplices | **24** |
| entries of `E_p` | `0`/`1`, staircase of partial sums |
| `det E_p` | **`= sgn(p)` for all 24** — verified, not asserted |
| `\|det E_p\|` | **`1`**, every one |
| four-volume `= \|det E_p\|/4!` | **`1/24`**, every one |
| sum of the 24 volumes | **`1`** |

Two frames displayed in full:

```text
p = (0,1,2,3)   det E = +1   vol = 1/24        p = (0,1,3,2)   det E = -1   vol = 1/24
   [1 0 0 0]                                      [1 0 0 0]
   [1 1 0 0]                                      [1 1 0 0]
   [1 1 1 0]                                      [1 1 0 1]
   [1 1 1 1]                                      [1 1 1 1]
```

[PROVABLE] **Check against the sealed source.** `MAJ` states 24 simplices at `1/24` each,
summing to 1. The derivation reproduces **all three** — count, per-cell volume, and total —
from the coordinates alone. **Orientation is canonical too:** `det E_p = sgn(p)` supplies a
consistent orientation on all 24 without a choice, which is what `MAJ`'s word *"oriented"*
requires.

```text
FRAME_DATA = derived (24 simplices, exact).
```

---

## 2. AE2 — DOES `V011`'s CLAUSE ACCEPT IT?

### 2.1 What the clause says

[PROVABLE] `V011` `aa7c6d49…[46074,46387)`:

```text
Therefore each cell contributes

    V_cell sum_(mu<nu) F_(mu nu)^2

in the local orthonormal frame. For a general coframe `theta^a=e^a_mu dx^mu`,
the same map is defined by pulling the bivector through
`wedge^2(e^(-1))` and multiplying by `|det e|`.
```

**The volume factor in the general map is `|det e|`.** That is the whole of AE2.

### 2.2 Why the identification is exact for boxes

[PROVABLE] `V011` `aa7c6d49…[45718,46068)`: *"For an orthogonal physical cell with edge lengths
`ell_mu`, volume `V_cell = product_mu ell_mu`."*

[YOURS] For a box the natural frame is `e = diag(ell_0,…,ell_3)`, so
`|det e| = product_mu ell_mu = V_cell`. The identification holds **because the cell is the
frame's parallelepiped** — a box is exactly the parallelepiped spanned by its edge vectors.
That is a fact about boxes, not about frames.

### 2.3 The simplex: the identification fails, by exactly `4!`

[YOURS, exact] For the derived simplicial frame:

```text
|det E_p| = 1          (section 1.3, all 24)
V_cell    = 1/24       (MAJ, sealed; reproduced in section 1.3)

|det E_p| / V_cell = 24 = 4!
```

**A simplex is not its edge-parallelepiped; it is `1/d!` of it.** So plugging the derived frame
into `V011`'s general clause supplies a volume factor **24 times too large** on every one of
`A2`'s children.

### 2.4 No frame repairs it — and the repair is irrational

[YOURS] One could ask for a rescaled frame `ẽ = E/λ` with `|det ẽ| = 1/24`. In four dimensions
`|det(E/λ)| = |det E|/λ^4 = 1/λ^4`, so `λ^4 = 24` and **`λ = 24^(1/4)`**.

Three reasons this is not a repair:

1. **It is irrational**, and the sealed constructions on this thread are exact-rational
   throughout — `MAJ` *"re-derived exactly by iterated polynomial integration"*, and my own 738
   reconstruction ran in exact `Fraction` arithmetic end to end. A `24^(1/4)` frame leaves that
   discipline.
2. **It is unlicensed.** No sealed text states any normalization of the simplicial frame.
   Choosing one is exactly the move the void condition names.
3. **It is the wrong shape of fix.** The discrepancy is **combinatorial** — the simplex-to-
   parallelepiped ratio `1/d!` — and it is identical for every simplex regardless of geometry.
   A frame rescale distorts frame data to absorb a constant that has nothing to do with the
   frame.

### 2.5 The divergence is between two sealed authorities

[PROVABLE] `R33` `e60aec3c…[551,740)` — verdict
`INHERITED_REFINEMENT_NATURALITY_FORCES_UNIFORM_MEASURE`, an **executed** result and a STAGE7
packet member bound to row A27:

```text
Therefore a subregion promoted to an elementary cell must be evaluated by
that child's intrinsic cell measure. It may not retain a weighting profile
defined by an arbitrarily chosen parent.
```

[PROVABLE] `MAJ` states that child's intrinsic cell measure for an order-simplex: `|C|_4 = 1/24`.

[YOURS] **So on `A2`'s children two sealed authorities give different volume factors:**

| Authority | Volume factor on an `A2` child | Status |
|---|---|---|
| `R33` + `MAJ` | `1/24` — the child's own four-volume | executed result; sealed construction |
| `V011`'s general-coframe clause | `\|det e\| = 1` | sealed clause, written for the orthogonal case |

They **agree exactly on boxes** (`|det diag(ell)| = product ell = V_cell`) and **diverge by
`4!` on simplices**. This is not a gap in the record; it is a **conflict inside it**, of the
same shape as the C_ref/D3 conflict, and it has the same resolution-holder.

### 2.6 The one-line need — named, not authored

[YOURS] What would close the coframe field's `A2` half is a single sealed statement, in one of
two equivalent forms:

```text
EITHER  the general map's volume factor is |det e| / d!  for a d-simplex cell
        (equivalently: |det e| is the parallelepiped volume, and the cell
         volume is that divided by the cell's combinatorial type factor);

OR      the general map is restated with V_cell as an INDEPENDENT sealed datum
        rather than as |det e|, with the box case recovered as the special
        case V_cell = |det e|.
```

**I do not author either.** Both are rulings — the second in particular changes what `V011`'s
clause *means*, and `R33` already indicates which way the ruling falls without making it. My
lane's charge is to display the conflict and the two forms, which is done.

```text
V011_CLAUSE = bars (one-line need named).
```

---

## 3. AE3 — THE BOARD

The coframe field does **not** close. `751`'s board stands, with one entry sharpened:

| # | Field | Verdict over the working class | Change from 751 |
|---|---|---|---|
| 1 | incidence — four-volume half | **SUPPLIED** | — |
| 1b | incidence — cochain half | **GAP NAMED** | — |
| 2 | degree | **UNDERDETERMINED**, obstruction out of scope | — |
| 3 | **coframe** | **PARTIAL** — derived on `A1`; on `A2` the **frame data is now DERIVED and the clause bars it by `4!`** | **sharpened**: was "no sealed coframe on simplices", is now "the coframe is derived; the volume-factor convention conflicts" |
| 4 | connection | **UNDERDETERMINED** — free datum: refined edge assignment, dim 32 on `A2` | — |
| 5 | volume | **SUPPLIED** | — |
| 6 | support | **UNDERDETERMINED** | — |
| 7 | current density | **UNSUPPLIED** | — |

[YOURS] **What `R33` gives on `A2`, stated at its exact strength.** `R33`'s rule applies to
simplicial children without modification: each order-simplex is a subregion promoted to an
elementary cell, and must be evaluated by its own intrinsic measure — `1/24`, not a share of
the parent's. **`R33` is therefore not the obstacle on `A2`**; it is the authority that names
the correct factor and thereby *creates* the conflict with `V011`'s clause. Once the §2.6
statement exists, `R33` grounds the `A2` transport exactly as it grounds the `A1` transport at
751 §1.2, and the coframe field closes whole.

[YOURS] **Anisotropic parent extents**, per the commission: the derivation of §1 is on the
**unit** 4-cube, which is what `MAJ` seals. For a parent box with extents `ell_mu`, the
simplicial frames become `E_p · diag(ell)`, so `|det| = product_mu ell_mu` and the child
volume is `product ell / 4!`. **The `4!` discrepancy is unchanged and extent-independent** —
confirming §2.4's point that it is combinatorial. I state this as the natural extension and
**do not book it**: `MAJ` seals the unit cube, and the anisotropic case is one line beyond the
sealed coordinates.

---

## 4. GROUNDING, JURISDICTION, VERB AUDIT

### 4.1 Grounding

| # | Claim | Pin | Tag |
|---|---|---|---|
| 1 | 24 order-simplices at `1/24`, oriented, exactly re-derived | `08b91543…[19632,19996)` | PROVABLE |
| 2 | The general map's volume factor is `\|det e\|` | `aa7c6d49…[46074,46387)` | PROVABLE |
| 3 | The orthogonal cell's `V_cell = product ell_mu` | `aa7c6d49…[45718,46068)` | PROVABLE |
| 4 | `R33`'s child-intrinsic rule; executed; packet-sealed | `e60aec3c…[551,740)` | PROVABLE |
| 5 | The 24 frames; `det E = sgn(p)`; `\|det E\| = 1`; volumes `1/24`; sum `1` | §1.3 | YOURS, exact |
| 6 | `\|det E\|/V_cell = 4!` | §2.3 | YOURS, exact |
| 7 | The rescale is `24^(1/4)`, irrational | §2.4 | YOURS, exact |
| 8 | The two sealed authorities diverge on `A2`, agree on boxes | §2.5 | PART-PROVABLE |
| 9 | The anisotropic extension leaves `4!` unchanged | §3 | YOURS, **not booked** |

**Pin check: 9/9.** All spans re-read from bytes this relay; §1 and §2's arithmetic computed
in exact rationals and checked against `MAJ`'s three sealed invariants.

### 4.2 Jurisdiction check

**On deriving rather than reporting a gap.** At 751 I named the simplicial coframe a spec gap
and declined to author it. This relay's premise is the distinction that makes the difference:
**the sealed construction already determines the coordinates**, so computing the frame is
*verification of what is sealed*, not authorship of something new. §1 chooses nothing — the
test I applied is that every entry traces to `MAJ`'s definition, and the output reproduces
`MAJ`'s own invariants. Where authorship *would* have begun — §2.6's volume-factor statement —
I stopped.

**On the VOID CONDITION.** No coefficient was consulted, and nothing here is chosen from a
desired outcome. The derivation's result runs against closing the field: it would have been
easy, and wrong, to normalize the frame by `24^(1/4)` and report the coframe field closed.

**On the gates.** The arithmetic is exact-rational and structural — cell counts, determinants,
volumes. No physical quantity is evaluated, no response, no junction map, no smooth data.

**On R9 / R9-JII.** Untouched.

### 4.3 Self verb audit — **CLEAN, with three disclosures**

1. **The available shortcut, named because it was genuinely tempting.** Rescaling the frame by
   `24^(1/4)` makes `|det ẽ| = V_cell` and closes the coframe field in one line. It is
   unlicensed, irrational, and absorbs a combinatorial constant into frame data. **Refused**,
   and §2.4 states all three reasons rather than just asserting the refusal.
2. **I upgraded 751's finding rather than repeating it.** 751 said *"no sealed coframe on
   simplicial cells."* That was true and it was the weaker statement: the frame **is** derivable
   from sealed coordinates, and the real obstruction is one integer in a clause written for
   boxes. A gap that turns out to be a conflict is a different object, and the registrar should
   have the sharper one.
3. **§3's anisotropic extension is one line past the sealed coordinates** and I flag it as
   unbooked. `MAJ` seals the unit cube; a parent with general extents is the obvious next case
   and it is not what was sealed.

---

```text
FRAME_DATA = derived (24 simplices, exact).  One simplex per permutation of (0,1,2,3);
    edge-vector matrix = the staircase of partial sums, entries 0/1; det E_p = sgn(p)
    for ALL 24 (verified, not asserted); |det E_p| = 1 every one; four-volume =
    |det E_p|/4! = 1/24 every one; sum of the 24 volumes = 1.  Reproduces all three of
    MAJ's sealed invariants — count, per-cell volume, total — from the sealed
    coordinates alone, with nothing chosen and orientation canonical.
V011_CLAUSE = bars (one-line need named).  The general clause aa7c6d49...[46074,46387)
    encodes the cell's volume factor as |det e|.  That identification is EXACT for a
    box, because a box IS its edge-parallelepiped.  A simplex is 1/d! of its
    parallelepiped: |det E| = 1 against V_cell = 1/24, off by EXACTLY 4! = 24.  No
    frame repairs it — the required rescale is E/24^(1/4), IRRATIONAL, in a
    construction the sealed sources carry in exact rationals throughout, unlicensed by
    any sealed text, and the wrong shape besides, since the discrepancy is
    combinatorial and extent-independent (confirmed: for anisotropic parent extents the
    4! is unchanged).
    THE SHARP FORM: this is a CONFLICT between two sealed authorities, not a gap.
    R33 e60aec3c...[551,740) — executed, packet-sealed, bound to row A27 — rules that a
    promoted subregion is evaluated by THAT CHILD'S INTRINSIC CELL MEASURE, and MAJ
    states that measure is 1/24; V011's clause computes 1 for the same child.  They
    AGREE ON BOXES and DIVERGE BY 4! ON SIMPLICES.  The one-line statement needed is a
    RECONCILIATION, in either of two displayed forms, and R33 already indicates which
    way it falls.  Naming it is this lane's charge; making it is a ruling.
BOARD = updated.  Coframe stays PARTIAL, sharpened: was "no sealed coframe on
    simplices", is now "the coframe IS derived and the volume-factor convention
    conflicts".  R33 is NOT the obstacle on A2 — it is the authority naming the correct
    factor, and once the reconciliation exists it grounds A2 exactly as it grounds A1.
    All other fields unchanged from 751.
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+3 disclosures at section 4.3, including the one-line
    irrational normalization that would have closed the field and was refused)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
