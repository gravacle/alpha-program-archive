# STAGE 8 / 7A / Q-126 ROUTE — THE TOWER REBUILT: THE TWISTED FLOOR DERIVED, TWO OF MY OWN CLAIMS REFUTED

Lane: DARIO (Builder B, independent verifier). Relay 764.
Governing: my 762 corrections; the locked spectrum in the mirrored two-cutoff theorem;
`E_parent` = the completed `Spin(10)` chiral **16**; the route's own sealed falsifier.
Nothing adopted; nothing evaluated numerically.

## Lead determination

**The tower rebuilds exactly — and the rebuild refutes two claims I would have shipped.**

**The twisted floor is derived, and it is not what I first read it to be.** For the monopole-twisted
Dirac operator on the unit `S^2` with charge `q` (`2q ∈ Z`, `deg L = 2q`):

```text
lambda_S2^2 = l(l+1) - q^2 + 1/4 ,   l = |q|-1/2, |q|+1/2, ...
            = ell (ell + 2|q|) ,     ell := l - (|q| - 1/2) = 0, 1, 2, ...
```

The reparametrisation is an exact identity — `(l+1/2)^2 - q^2` — and at `ell = 0` it gives
**exactly zero**: the zero-mode level, of multiplicity `2|q| = |deg L|`, all one chirality,
**reproducing the index theorem**. That is why the locked spectrum needs its `+1`.

**But the locked bound does not say what I drafted.** I had written that the floor `ell(ell+1)`
*identifies* the flux at `|q| = 1/2` — an **equality at minimum flux** — and read the principle's
*"minimum closed orientable exterior source-flux comparison"* as corroboration. **Both halves are
wrong, and I withdraw them.**

- *"minimum closed orientable"* modifies a **surface** — `S^2` is the minimal-genus closed
  orientable surface. **Closed and orientable are manifold predicates a flux does not possess.**
  The phrase places **no constraint whatsoever on `|q|`**.
- The sealed statement is an **inequality**, and `ell(ell + 2|q|) >= ell(ell+1)` holds for **every**
  `|q| >= 1/2` — I verified this in exact arithmetic over `|q| = 1/2 … 4`. **The floor does not
  select the flux.** Its real content is `|q| >= 1/2`, i.e. **the flux is nonzero** — an index
  statement, not a magnitude.

**And my multiplicity bookkeeping was wrong by exactly a factor of four**, which a Weyl-law audit
of my own then confirmed: my draft's implied bundle rank was **16**, against the true
`rank(S_Sigma ⊗ E_parent) = 4 × 16 = **64**`. Two independent undercounts — I omitted
`rank(S_{T^2}) = 2` entirely, and I used the single-sign `S^2` degeneracy where the `±` pairing
requires double. **This is the same failure mode as 731: I computed a rank in one line and threw
it away in the next.**

**What survives:** the twisted spectrum itself (derived two independent ways by the checker, and
index-consistent), the reparametrisation identity, `C2(16) = 45/8` in the stated convention, and
the spinor-rank factorisation.

---

## 0. Preflight

### 0.1 Output name

Probed **before any write**, recursively: **absent**, artifact and sidecar both.

### 0.2 Sources verified before use

```text
PRIN  workspace/mirrored_sources/alpha_global_record_surface_superconnection_principle_v001.md
                                                                    ae1d0492…  digest-matched to SPEC's manifest
TWO   workspace/mirrored_sources/alpha_br_full98_c2_two_cutoff_continuum_theorem_v001.md
                                                                    7a3c6bc6…  UNSEALED, PROPOSED_NOT_CLOSED
762   workspace/STAGE8_7A_DBR_PUBLIC_LAYER_DARIO_V001.md            beff9f11…
760   workspace/STAGE8_7A_DBR_SPECTRUM_DARIO_V001.md                a2745310…
GAP   workspace/…BR_CLOSURE_OPERATOR_STRUCTURAL_SPECTRAL_GAP_DETERMINATION_V001.md  e2fc00d2…  SEALED-OK
```

`TWO`'s status is unchanged from 762: **unsealed, `PROPOSED_NOT_CLOSED`**. Its locked spectrum is
used here as a **target to rebuild against and a test of my own prior work**, never as a sealed
ground.

### 0.3 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
No member binding.  No fixed-point execution.  No end test.  NO NUMERIC EVALUATION OF
PHYSICAL QUANTITIES — every number below is a dimensionless multiplicity, an exact
rational Casimir in a stated convention, or an eigenvalue LABEL; no radius, gap value,
scale or root is evaluated.  No comparison to measured constants.  No common cell formed.
No junction map evaluated.  No smooth data derived.  Nothing adopted.
No register, plan, tracker, or git action.
```

---

## 1. AN1 — THE TOWER, REBUILT

### 1.1 The flux-twisted `S^2` operator

[YOURS, verified] On the unit `S^2` with monopole charge `q` (`2q ∈ Z`, `deg L = 2q`):

```text
lambda_S2 = ± sqrt( (l+1/2)^2 - q^2 ),      l = |q|-1/2, |q|+1/2, |q|+3/2, …
```

Each of `+lambda_l` and `−lambda_l` has multiplicity `2l+1`.

[YOURS, exact] **Reparametrised to the locked form.** Put `ell := l − (|q| − 1/2)`. Then

```text
l(l+1) − q^2 + 1/4 = (l+1/2)^2 − q^2 = (ell + |q|)^2 − q^2 = ell (ell + 2|q|)
```

identically. I checked it in exact rationals over `|q| = 1/2 … 7/2` and `ell = 0 … 6`: **no
mismatch**. At `ell = 0` it is exactly `0`.

[YOURS] **A precision the checker required and I adopt.** *"`ell = 0,1,2,…`"* is a **spectral-range
assertion**, not an algebraic consequence: it holds for the spin-½ total-angular-momentum ladder
`l = |q|−1/2, |q|+1/2, …` with `2q ≠ 0`. On the scalar monopole-harmonic ladder the same
substitution gives half-integers, and at `q = 0` the ladder has no `ell = 0` rung at all. **Stated
with its hypothesis.**

### 1.2 Zero modes and the index

[YOURS, verified exactly for `|q| = 1/2 … 7/2`]

```text
ell = 0  ->  lambda_S2^2 = 0 ,  multiplicity 2l_0 + 1 = 2|q| = |deg L| ,
             all of a single chirality (the sign of q)
```

which is `ind(D) = deg L = 2q`, the Atiyah–Singer index on `S^2`. **This is why the locked
spectrum carries `+1`:** a flux-twisted sphere factor contributes **zero** at its bottom level, so
without an additive constant `lambda_a` would not be bounded below by 1.

### 1.3 What the locked floor actually says — and my draft headline withdrawn

[PROVABLE] `TWO` states an **inequality**: `lambda_a >= 1 + p_t^2 + p_q^2 + ell(ell+1)`.

[YOURS, exact] `ell(ell + 2|q|) >= ell(ell+1)` **for every `|q| >= 1/2`** — verified over
`|q| = 1/2, 1, 3/2, 2, 5/2, 3, 7/2, 4` and `ell = 0 … 39`, no violation. Equality **for all `ell`**
holds iff `2|q| = 1`.

[YOURS] **So the floor's content is `|q| >= 1/2` — the flux is NONZERO — and nothing more.** It is
an **index statement on the `S^2` factor**, not a magnitude. My draft's *"the floor is not an
inequality but an equality at minimum flux"* is **withdrawn**: `|q| = 1/2` is *one* way to satisfy
the bound, not the way it is satisfied.

[YOURS] **And the corroboration I drafted from the principle is withdrawn too.** `PRIN`:
*"`S2_flux` carries the **minimum closed orientable** exterior source-flux comparison."*
**"Minimum closed orientable" governs the surface** — `S^2` is the minimal-genus closed orientable
surface, the natural Gauss surface for an exterior flux comparison. *Closed* and *orientable* are
predicates of a manifold; a flux magnitude has neither. **The phrase constrains the surface and
says nothing about `|q|`.** I read a topological minimality as a numerical one.

### 1.4 `C2_parent` on the fixed 16

[YOURS, verified] `E_parent` is the `Spin(10)` chiral **16**. In the convention
`C2(vector of SO(N)) = (N−1)/2`, the general result `C2(spinor of SO(N)) = N(N−1)/16` gives

```text
C2(16) of Spin(10) = 10·9/16 = 45/8         (cross-check n(2n−1)/8, n=5: 45/8)
```

[PROVABLE-BY-INDEPENDENT-CHECK] The commissioned check reproduced `45/8` by the `(λ, λ+2ρ)` weight
formula **and** by an explicit 32×32 Clifford construction, matching Slansky's tables.

[YOURS] **Two qualifications, both load-bearing.**

1. **The value is convention-dependent.** The same representation has `C2 = 45/4`, `45/64`, or
   `45/16` in other standard normalisations. Only ratios are invariant — `C2(16)/C2(10) = 5/4`,
   `C2(16)/C2(45) = 45/64`. **And `Sigma_BR` carries no `Spin(10)` directions, so the geometry
   fixes no normalisation.** `C2_parent`'s numerical value in the locked spectrum is therefore a
   **convention-carrying constant**, and §3 ledgers it as such.
2. **Because the 16 is irreducible, `C2` is a single scalar on it** — a uniform additive shift that
   separates nothing inside the 16.

[YOURS] **An inference I drafted and now withdraw: it was backwards.** I had written that this
"explains" the sealed witness *"the current parent inventory includes a sector not lifted by the
quadratic invariant"* by implying an extra `C2 = 0` sector. The check shows the opposite:
`{16}` alone gives `{45/8}` — **uniform, lifting nothing relative**; `{16, 1}` gives `{0, 45/8}` —
**which SPLITS**. Adding a `C2 = 0` singlet is the condition under which the Casimir *does* lift.
**I cannot reconstruct the witness's "sector" from sealed text and no longer claim to.**

### 1.5 The `T^2_TQ` towers

[PROVABLE] `PRIN`: `Sigma_BR = S1_T x S2_flux x S1_Q = **T2_TQ x S2_flux**`, and the proper-time
factor *"is shared by the gravity and matter reads; it is not duplicated."*

[YOURS] On `T^2_TQ` the Dirac square is `p_t^2 + p_q^2` over the momentum lattice, with the
spin-structure shifts on each circle (`0` or `1/2`) selecting the lattice offset. **The spinor
bundle `S_{T^2}` has rank 2**, and at fixed `(p_t, p_q)` it carries `D_{T^2}` eigenvalues `±|p|`,
**both giving the same `D^2`** — which is precisely the factor §2 shows I dropped.

### 1.6 The `+1`

[YOURS] In `TWO`'s locked spectrum the constant is `+1`, and `TWO`'s own convergence bar reads
*"For the background gap `lambda >= 1`"*. Given §1.2 — the twisted sphere contributes zero at its
bottom — **the `+1` is what holds the background gap**, and it occupies the `Phi^dagger Phi` slot
at `TWO`'s adopted background `u=0`.

[YOURS] **It is a convention within `TWO`'s fixed scope, not a derived value.** `TWO` declares
*"one fixed periodic spin structure and one fixed external full98 mode `L=2`, `M=0`,
`q=(±1,0)`"*, and `PRIN` leaves `Phi` unselected. **`+1` is a scope fixing, and §3 ledgers it as
one.**

### 1.7 The cross-grade term, carried unselected

[PROVABLE] `PRIN` displays three grades:

```text
D_BR^2 = D_(Sigma,A)^2 + Gamma_Sigma [D_(Sigma,A), Phi] + Phi^dagger Phi
```

[YOURS] **Carried, not assumed away.** The middle term is `Gamma_Sigma` times a commutator: it is
**odd in the grading**, so it is the **only term coupling the even and odd sectors**, and it
vanishes **iff `Phi` is covariantly constant** (`[D_(Sigma,A), Phi] = 0`). Since `Phi` is
unselected — and the sealed TYPE-R witness records that the corpus *"leaves `Phi` unselected and
permits a nontrivial kernel"* — **no bound is available**: bounding it requires selecting `Phi`,
which is the free datum. It is displayed as the **`Phi`-dependent slot**, and my 760 assertion
that it cancels is withdrawn (that withdrawal was already made at 762 §1.3; it stands).

### 1.8 The tower, assembled

```text
lambda_a( p_t, p_q, ell ; q )
   =  p_t^2 / R_T^2                      T^2_TQ, shift by spin structure
    + p_q^2 / R_Q^2                      T^2_TQ, shift by spin structure
    + ell(ell + 2|q|) / r_flux^2         S^2_flux, TWISTED   [ell = 0,1,2,…]
    + [ Phi^dagger Phi ]                 the +1 slot at TWO's background
    + [ Gamma_Sigma [D,Phi] ]            THE CROSS GRADE — carried, unbounded
    + C2_parent                          uniform scalar on the irreducible 16

   locked form recovered at unit radii, with C2_parent's normalisation as in §1.4
```

---

## 2. MULTIPLICITIES — CORRECTED, AND THE UNDERCOUNT DISCLOSED

### 2.1 What I had, and what it was missing

[YOURS] My draft: `mult = [N_lattice] × [2(ell+|q|)] × 16`. **Two independent undercounts:**

1. **`rank(S_{T^2}) = 2` omitted entirely.** Eigenspaces are tensor products; at fixed `(p_t,p_q)`
   the 2-dimensional torus spinor space contributes twice to the same `D^2` value (§1.5).
2. **The `S^2` `±` pairing dropped.** `2l+1` is the multiplicity of **each** Dirac eigenvalue
   `±lambda_l`, so the **`D^2` eigenspace** at level `ell >= 1` has dimension `2(2l+1) =
   4(ell+|q|)`. Only the **bottom** level is unpaired, at `2|q|`.

[YOURS] **My own Weyl-law audit, run to settle it rather than take the correction on trust:**

```text
Lambda      mine        corrected     ratio
   200      63,708       253,566      3.9801
   800   1,008,148     4,027,550      3.9950
  3200  16,096,901    64,367,506      3.9988
 12800 257,430,105 1,029,640,042      3.9997      ->  4.0000
```

**Ratio → 4 exactly.** My count reproduced a **rank-16** bundle; the true rank is
`rank(S_Sigma ⊗ E_parent) = 4 × 16 = **64**`. **I computed `rank(S_Sigma) = 4` in one line and
discarded it in the next.**

### 2.2 The corrected multiplicity

```text
mult(lambda_a)  =  [ 2 · N_lattice(p_t, p_q) ]  ×  d_S2(ell)  ×  16

   d_S2(ell)  =  4(ell + |q|)   for ell >= 1        [± paired]
   d_S2(0)    =  2|q|           = |deg L|            [unpaired zero modes, one chirality]

   at |q| = 1/2 :  d_S2(ell) = 2(2ell+1) for ell >= 1 ;  d_S2(0) = 1
```

### 2.3 The `× 16` is conditional, and the condition is not sealed

[YOURS] **A flat `× 16` is legitimate only if the `S^2` flux acts as a scalar on `E_parent`** — and
that is **impossible for any nonzero generator of the simple algebra `so(10)`**. So the flat factor
requires the flux `U(1)` to be **external to `Spin(10)`**, with the parent connection **flat and of
trivial holonomy on both circles**. **Nothing sealed states that.** If instead the flux sits inside
`Spin(10)`, it **twists the parent factor and changes the spectrum itself**, not merely the count.

```text
MULTIPLICITIES = pinned by the 16 (bundle class free, named) — pinned to
   [2 N_lattice] × d_S2(ell) × 16, CONDITIONAL on the flux U(1) being external to
   Spin(10) with a flat parent connection.  That condition is the bundle class,
   and it is FREE.
```

---

## 3. AN2 — THE FREE-DATA LEDGER, AGAINST THE ROUTE'S OWN FALSIFIER

[PROVABLE] `PRIN`'s falsifier, verbatim:

```text
The route fails to compute alpha if two inequivalent choices of radii, spin
structure, bundle class, or odd profile satisfy all adopted record rules while
producing different weighted charged determinants. In that case a further
physical selection principle is required; the desired coupling may not select
the missing data retroactively.
```

| Free datum | What sealed text constrains it | What would select it lawfully | What the falsifier demands |
|---|---|---|---|
| **`R_T`, `R_flux`, `R_Q`** | Nothing. `TWO` writes the spectrum at **unit radii**, absorbing them (§4). `PRIN`: *"A value may not be called primitive merely because it is an integer or a compact radius."* | Derivation from *"boundary closure plus the induced action"* (`PRIN`'s own condition), **before** any comparison | Two radius sets satisfying all record rules must not give different weighted charged determinants — and the radii are exactly what §4 shows `beta` rescales |
| **Spin structure on `T^2_TQ`** | Four choices (`±` on each circle). `TWO` **fixes** *"one fixed periodic spin structure"* — a **scope fixing**, not a selection | Derivation, or principal adoption with the other three excluded on record | Periodic vs antiperiodic shift the lattice offsets and hence the whole `T^2` tower; they must not give different determinants |
| **Parent bundle + characteristic class** | **Rank fixed at 16** (`PRIN`); **class free**. §2.3: the class decides whether `×16` is flat or whether the flux twists the parent | Derivation of the class; or a sealed statement that the flux `U(1)` is external to `Spin(10)` with flat parent connection | This is the sharpest item: **different classes change the spectrum, not just the count** |
| **Odd profile `Phi`** | Unselected. Sealed TYPE-R witness: the corpus *"permits a nontrivial kernel"*. `TWO`'s `+1` is the `Phi`-slot **at its background**, within its fixed scope | Derivation of the vacuum profile; the `+1` is not it | `Phi` sets both the constant **and** the unbounded cross grade (§1.7). Two profiles satisfying the rules must not diverge |
| **Chiral index** | Unselected by `PRIN`. **But `TWO`'s floor does constrain the `S^2` factor: `|q| >= 1/2`, i.e. `deg L ≠ 0`** — a nonzero index on that factor (§1.3) | Derivation of the index; the floor gives only non-vanishing | The index fixes the zero-mode count `2|q|`, which enters `d_S2(0)` directly |

[YOURS] **The one thing the locked bound genuinely contributes to this ledger is a non-vanishing
statement**: `|q| >= 1/2`. That is real and it is small. Everything else in the table is free, and
`TWO`'s locked spectrum **fixes three of the five within its own scope** — spin structure, mode,
and the `+1` — which is a scope declaration and **not** progress against the falsifier.

[YOURS] **The ledger is the work plan and the kill condition in one table, as the commission says
— and read as a kill condition it is unflattering:** five free data, four of which change the
spectrum (not merely its labels), and the route fails if any two admissible settings survive to
different determinants. **Nothing in this relay reduces the free set.**

---

## 4. AN3 — `beta`, RE-DISPLAYED ON THE CORRECTED TOWER

[YOURS] 760's mechanism, carried onto §1.8: the three geometric towers carry the radii, and the
locked form is written with them **absorbed**. Restoring them:

```text
p_t^2/R_T^2 ,  p_q^2/R_Q^2 ,  ell(ell+2|q|)/r_flux^2      scale as  1/R^2
C2_parent                                                  an INTERNAL invariant
```

[YOURS] **And the corrected tower sharpens 760's statement into something stronger.** `beta` is the
record cell's internal↔external conversion (`R = beta c Delta tau`), so it rescales the **radii**.
But `C2_parent` is a `Spin(10)` invariant of the internal carrier and **carries no geometric
radius** — `Sigma_BR` has no `Spin(10)` directions (§1.4). **So `beta` does not rescale the
spectrum uniformly: it moves the geometric towers against the internal Casimir term.**

[YOURS] **Consequence, stated as structure and not as a value.** `beta` is therefore **not
removable by an overall normalisation** of `lambda_a`: it changes the **ratio** between the
geometric and internal sectors of the spectrum. Fixing that ratio is exactly what `GAP`'s
*"normalized transfer from `D_BR^2` to the `L_BR` **proper-time** consumer"* must do — which is why
that item, and not the raw tower, is where 762 located the `beta`-carrying step.

[YOURS] **A qualification I will not skip.** Whether `C2_parent` enters the locked convention as a
pure number or with an implicit scale is **not sealed**; `TWO` writes everything dimensionless. So
the non-uniformity above is a statement about the **restored** form, and its precise weight depends
on the normalisation `TWO` does not fix — which is §3's `C2_parent`-convention item. **I display
the mechanism and decline the weight.**

```text
BETA = re-displayed.  Geometric towers ~ 1/R^2 ; C2_parent internal and radius-free ;
   so beta acts NON-UNIFORMLY and is not removable by an overall normalisation.
   Weight declined: the normalisation TWO uses is not sealed.
```

---

## 5. GROUNDING, JURISDICTION, VERB AUDIT

### 5.1 Grounding

| # | Claim | Basis | Tag |
|---|---|---|---|
| 1 | Twisted `S^2` spectrum, range, `2l+1` per Dirac eigenvalue | derived; independently reconstructed two ways in the commissioned check | YOURS, verified |
| 2 | `l(l+1) − q^2 + 1/4 = ell(ell+2|q|)`, exact; `0` at `ell=0` | exact rationals, `|q| = 1/2…7/2` | YOURS, exact |
| 3 | Zero modes `= 2|q| = |deg L|`, one chirality; index | exact, `|q| = 1/2…7/2` | YOURS, exact |
| 4 | The floor is satisfied by **every** `|q| >= 1/2`; equality iff `|q| = 1/2` | exact, `ell = 0…39` | YOURS, exact |
| 5 | *"minimum closed orientable"* modifies the **surface** | `ae1d0492…`, read grammatically | PROVABLE |
| 6 | `C2(16) = 45/8`; convention-dependent; uniform on an irrep | derived; independently reproduced two ways | YOURS, verified |
| 7 | Multiplicity undercount is exactly `×4`; true rank 64 | my own Weyl-law audit, four cutoffs → 4.0000 | YOURS, exact |
| 8 | `× 16` conditional on the flux being external to `Spin(10)` | structural: no nonzero `so(10)` generator acts as a scalar | YOURS |
| 9 | Three grades of `D_BR^2`; the cross term vanishes iff `Phi` covariantly constant | `ae1d0492…` + structure | PROVABLE / YOURS |
| 10 | `PRIN`'s falsifier; the unselected list | `ae1d0492…` | PROVABLE |
| 11 | `TWO`'s fixed scope (periodic spin structure, `L=2, M=0, q=(±1,0)`) and unit radii | `7a3c6bc6…` | PROVABLE (unsealed source) |
| 12 | `beta` acts non-uniformly on the restored tower | §4 | YOURS, weight declined |

**Pin check: 12/12.**

### 5.2 Jurisdiction check

**On deriving a spectrum as Builder B.** The geometry and operator are sealed/quoted; the twisted
spectrum is standard mathematics on that fixed object, and I commissioned five independent
adversarial checks **before** writing rather than after. Where selection would have begun —
`|q|`, the radii, the spin structure, `Phi`, the class — I stopped and ledgered.

**On the VOID CONDITION.** Nothing chosen from a desired coefficient. The one place a choice would
have produced a tidy result — reading the floor as *selecting* `|q| = 1/2` — is precisely what §1.3
withdraws. **The refutation runs against my own headline.**

**On `TWO`'s unsealed status.** Unchanged from 762: used as a rebuild target and as a test of my
own work, never as a ground. §1.6 and §3 record its scope fixings **as scope fixings**.

**On R9 / R9-JII and the frozen prereg.** Untouched.

### 5.3 Self verb audit — **CLEAN, with five disclosures**

1. **My draft headline is withdrawn twice over** (§1.3): the principle's phrase does not
   corroborate `|q| = 1/2`, and the sealed statement is an inequality that every `|q| >= 1/2`
   satisfies. I read a **topological** minimality as a **numerical** one — the same species of
   error as reading a bar as a deletion (742) and a bar as a non-existence (746).
2. **The multiplicity bookkeeping was wrong by exactly ×4** (§2), and the Weyl audit shows my
   count reproduced rank 16 against the true 64. **I computed `rank(S_Sigma) = 4` in §1 and threw
   it away in §2 of my own draft** — the 731 failure mode, third occurrence.
3. **An auxiliary inference about the sealed TYPE-R witness was backwards** (§1.4): a `C2 = 0`
   singlet is when the Casimir **does** lift, not when it fails to. I no longer claim to explain
   that witness.
4. **Three claims survived the checks** and I record that too, since a verb audit that only lists
   failures is as skewed as one that lists none: the twisted spectrum, the reparametrisation, and
   the Casimir value all held.
5. **The checks were commissioned by me and two came back against me.** That is now the standing
   pattern of this lane, and it is the reason to keep commissioning them.

---

```text
TOWER = rebuilt per the locked form (twisted floor derived; C2 on the 16; cross term
   carried).  lambda_S2^2 = ell(ell+2|q|), ell = 0,1,2,… on the spin-1/2 ladder — an
   exact reparametrisation of l(l+1) − q^2 + 1/4 = (l+1/2)^2 − q^2, checked in exact
   rationals.  ell = 0 gives EXACTLY ZERO with multiplicity 2|q| = |deg L|, one
   chirality: the Atiyah–Singer index, and the reason the locked spectrum needs its +1.
   THE FLOOR DOES NOT SELECT THE FLUX: ell(ell+2|q|) >= ell(ell+1) for EVERY |q| >= 1/2
   (verified |q| = 1/2…4, ell = 0…39); equality for all ell iff |q| = 1/2.  Its real
   content is |q| >= 1/2 — the flux is NONZERO, an index statement, not a magnitude.
   MY DRAFT HEADLINE IS WITHDRAWN, twice: the sealed phrase "minimum closed orientable"
   modifies a SURFACE (closed and orientable are manifold predicates; a flux has
   neither) and constrains |q| not at all; and the sealed statement is an INEQUALITY.
   C2_parent = 45/8 on the irreducible 16 in the convention C2(vector) = (N−1)/2 —
   independently reproduced by weight formula and explicit Clifford construction — but
   CONVENTION-DEPENDENT (45/4, 45/64, 45/16 elsewhere; only ratios invariant), and
   Sigma_BR carries no Spin(10) directions, so the geometry fixes no normalisation.
   The cross grade Gamma_Sigma[D,Phi] is CARRIED: odd, the only even–odd coupling,
   vanishing iff Phi is covariantly constant, and UNBOUNDABLE while Phi is unselected.
MULTIPLICITIES = pinned by the 16 (bundle class free, named):
   mult = [2 · N_lattice] × d_S2(ell) × 16, with d_S2(ell) = 4(ell+|q|) for ell >= 1
   and d_S2(0) = 2|q|.  MY DRAFT UNDERCOUNTED BY EXACTLY FOUR — rank(S_T2) = 2 omitted,
   and the S^2 ± pairing dropped — confirmed by my own Weyl-law audit converging to
   4.0000 over four cutoffs: my count reproduced rank 16 against the true
   rank(S_Sigma ⊗ E_parent) = 64.  The flat ×16 is CONDITIONAL: it requires the flux
   U(1) to be EXTERNAL to Spin(10) with a flat parent connection, since no nonzero
   so(10) generator acts as a scalar — and that condition is the bundle class, which
   is free.
FREE_DATA_LEDGER = displayed (per-item: constraint, lawful selector, falsifier demand).
   Five free data — radii, spin structure, bundle class, odd profile, chiral index.
   The locked bound contributes exactly ONE constraint: |q| >= 1/2, non-vanishing flux.
   TWO fixes three of the five WITHIN ITS OWN SCOPE (periodic spin structure, the L=2
   M=0 q=(±1,0) mode, the +1) — a scope declaration, NOT progress against the
   falsifier.  Four of the five change the SPECTRUM, not merely its labels.  Nothing in
   this relay reduces the free set.
BETA = re-displayed.  The three geometric towers scale as 1/R^2; C2_parent is an
   internal Spin(10) invariant carrying no geometric radius.  So beta acts
   NON-UNIFORMLY — it moves the geometric towers against the internal Casimir — and is
   therefore NOT removable by an overall normalisation of lambda_a.  Fixing that ratio
   is precisely GAP's "normalized transfer to the L_BR proper-time consumer".  Weight
   declined: TWO's normalisation is not sealed.
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+5 disclosures at section 5.3: headline withdrawn twice, a ×4
   multiplicity undercount that is the 731 failure mode's third occurrence, a backwards
   auxiliary inference, three surviving claims recorded, and the note that the checks
   which reversed me were ones I commissioned)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
