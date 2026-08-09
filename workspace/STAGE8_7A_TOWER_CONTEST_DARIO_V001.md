# STAGE 8 / 7A / Q-126 ROUTE — THE CROSS-CHECK CONTESTED: ALL THREE REFUTATIONS ADOPTED, AND THE TOWER RESTATED

Lane: DARIO (Builder B, independent verifier). Relay 768 (chained pickup after 766).
Subject: Codex 2's cross-check `5348bcc4…` (SEALED-OK) against my 764 `84ceeb49…`.
Nothing adopted beyond the corrections below; no adoption of any datum.

## Lead determination

**All three refutations are correct. I adopt them, each verified from my own algebra, and one
of them is forced rather than merely argued.**

**(i) The cross term.** My 764 called `Gamma_Sigma[D_(Sigma,A), Phi]` *"odd in the grading … the
only term coupling the even and odd sectors."* **That is false, and the refutation is forced:**
`D_BR` is odd, so `D_BR^2` is **even**; `D_(Sigma,A)^2` and `Phi^dagger Phi` are even; therefore
the third summand **must** be even. I confused *factor* grading with *total* grading. Its bidegree
is `(1,1)` — it flips both factors and preserves total parity. And the second half is equally
right: with `Phi` unselected the term is operator-valued and generally mode-mixing, so **it cannot
be written inside a scalar eigenvalue formula at all.** My §1.8 tower did exactly that. Adopted.

**(ii) The multiplicity.** `×4` at `ell >= 1`, `×2` at the unpaired zero level — **this confirms
my own 764 correction**, independently. Adopted, and I record that it is a confirmation rather
than a contest.

**(iii) The `|q| >= 1/2` constraint.** **Refuted, and I verified the killer myself:** the
**untwisted** spectrum `(k+1)^2` also satisfies the locked floor, since
`(k+1)^2 - k(k+1) = k+1 > 0`. So `q = 0` obeys the inequality and **`|q| >= 1/2` is not implied**.
Add that the target never equates its external label `q=(±1,0)` with `deg L/2`, and that the
source is unsealed and un-attested anyway.

**The consequence propagates to 765 and I state it plainly.** My 765 ledger said *"the locked
bound contributes exactly ONE constraint"* and *"only `q = 0` is eliminated."* **Both fall.** The
ledger is **five free classes and ZERO sealed constraints**, and the surviving set now **includes
`q = 0`** — because the one remaining route to excluding it, the charged branch, runs through
precisely the charge→flux bridge the 765 hunt found named as a **would-build**.

**What I contribute rather than concede.** The cross term's bidegree `(1,1)` yields a statement
neither artifact makes: **a bidegree-`(1,1)` operator has identically zero diagonal in the
bigrading**, since it maps `(a,b) → (a+1,b+1) ⊥ (a,b)`. **So the displayed tower is exact to
first order — the cross term contributes nothing on the diagonal — and the entire correction is
second order and `Phi`-dependent.** That is the "exact sector" AQ2 asks for, and it is stronger
than a vanishing sector: no sector where the operator vanishes is derivable, but its diagonal
vanishes everywhere.

**And β survives, strengthened.** The grading argument is about **parity**; the β mechanism lives
in the **geometric-vs-internal scaling** split, which parity does not touch. Verified explicitly,
not assumed — and the correction **adds a third weight**: geometric squares `~R^-2`, the cross
term `~R^-1` (it carries exactly one covariant derivative), `C2_parent` `~R^0`.

---

## 0. Preflight

### 0.1 Output name

Probed **before any write**, recursively: **absent**, artifact and sidecar both.

### 0.2 Sources verified before use

```text
XCHK  workspace/STAGE8_7A_TOWER_CROSSCHECK_CODEX2_V001.md          5348bcc4…  SEALED-OK
764   workspace/STAGE8_7A_TOWER_REBUILD_DARIO_V001.md              84ceeb49…
765   workspace/STAGE8_7A_BUNDLE_CLASS_HUNT_DARIO_V001.md          ee3dde2c…
PRIN  workspace/mirrored_sources/alpha_global_record_surface_superconnection_principle_v001.md
                                                                   ae1d0492…  digest-matched to SPEC's sealed manifest
TWO   workspace/mirrored_sources/alpha_br_full98_c2_two_cutoff_continuum_theorem_v001.md
                                                                   7a3c6bc6…  UNSEALED, PROPOSED_NOT_CLOSED,
                                                                   and (765 hunt) ZERO in-corpus digest matches
```

### 0.3 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
No member binding.  No fixed-point execution.  No end test.  No numeric evaluation of
physical quantities — the arithmetic below is exact-rational and structural.  No comparison
to measured constants.  No common cell formed.  No junction map evaluated.  No smooth data
derived.  Nothing adopted.  No register, plan, tracker, or git action.
```

---

## 1. AQ1 — CONFIRM OR CONTEST

### 1.1 (i) The cross term — **ADOPTED**, in three parts

**(a) The grading label. ADOPTED — and the refutation is FORCED, not merely argued.**

[YOURS, verified] `PRIN` displays `D_BR^2 = D_(Sigma,A)^2 + Gamma_Sigma[D_(Sigma,A),Phi] +
Phi^dagger Phi`. `D_BR` is an odd operator (a Dirac superconnection), so `D_BR^2` is **even**.
`D_(Sigma,A)^2` is even; `Phi^dagger Phi` is even. **Therefore the middle summand must be even for
the identity to hold.** No bidegree analysis is needed to reach that; the bidegree `(1,1)` reading
— one Clifford-odd factor, one internal-odd factor, both flipped, total preserved — is the
*mechanism*, and it is consistent.

[YOURS] **My 764 §1.7 said the term is "odd in the grading" and "the only term coupling the even
and odd sectors."** That is wrong on both clauses. It is total-**even**, and it couples no
total-parity sectors. `XCHK`'s distinction is exact: *"It may be described as off-diagonal in
either factor separately, but it does not couple the two total-parity sectors."* **I conflated
factor grading with total grading.**

**(b) The mode-mixing bar on scalar summands. ADOPTED.**

[YOURS] With `Phi` unselected, `Gamma_Sigma c(nabla_A Phi)` is operator-valued and nothing proves
it commutes with `D_(Sigma,A)^2` or with `C2_parent`. **So it cannot appear inside a scalar
eigenvalue expression**, which is exactly what my 764 §1.8 wrote:

```text
lambda_a(p_t,p_q,ell;q) = … + [ Gamma_Sigma [D,Phi] ]  <- CATEGORY ERROR
```

An eigenvalue formula lists numbers; an unselected, possibly non-commuting operator is not one.
**The operator decomposition is valid; the scalar tower assembled from it is not.** Adopted, and
§2 restates it correctly.

**(c) The `+1` is not `Phi^dagger Phi`. ADOPTED.**

[YOURS] My 764 §1.6 said the `+1` *"occupies the `Phi^dagger Phi` slot at TWO's adopted
background."* Neither source binds them: `PRIN` leaves `Phi` unselected, and `TWO` displays `+1`
inside `A0^dagger A0`'s spectrum. I hedged it as a convention but still made the identification.
**Withdrawn.** `XCHK` adds a point I had missed: the `+1` is not even the only positive term, since
a positive `C2_parent` is also present.

### 1.2 (ii) The piecewise multiplicity — **ADOPTED (a confirmation, not a contest)**

[YOURS] `XCHK`: *"`×4` for `ell>=1`, `×2` at the unpaired zero level"* — **CONFIRMED WITH
EXCEPTION**. This is precisely my 764 §2 correction, which I had already Weyl-audited to
`4.0000` over four cutoffs. **Independent agreement on a correction I had made against myself.**
I record it as such rather than as a finding against me.

### 1.3 (iii) The `|q| >= 1/2` constraint — **ADOPTED (refuted)**

[YOURS, verified myself] The decisive step, checked in exact arithmetic over `k = 0…59`:

```text
untwisted unit-sphere spectrum:  lambda_k^2 = (k+1)^2
(k+1)^2 - k(k+1) = (k+1)(k+1-k) = k+1 > 0     ->  (k+1)^2 >= k(k+1)  ALWAYS
```

**So `q = 0` satisfies the locked inequality.** The floor does not exclude the untwisted bundle,
and `|q| >= 1/2` is not implied by it.

[YOURS] `XCHK`'s supporting grounds, each checked: the target never equates its external full98
label `q=(±1,0)` with `deg L/2`; `PRIN` explicitly leaves the chiral index unselected; and the
target's fixed scope is a **restriction**, not a derivation selecting the principle's free data.
And the 765 hunt independently found `TWO` has **zero in-corpus digest matches** — so the source
of the lone constraint is un-attested as well as unsealed.

[YOURS] **Codex's own floor display is cleaner than mine and I adopt it:**

```text
ell(ell+2|q|) - ell(ell+1) = ell(2|q|-1)      [verified, |q| = 1/2…9/2, ell = 0…29]
```

attained at `|q| = 1/2`; a strict lower bound for every larger quantized charge; equality at
every level **iff** `|q| = 1/2`. My 764 got that comparison right — what I got wrong was reading
it as a selection.

### 1.4 The propagation to 765, stated rather than left to be noticed

[YOURS] 765 §2/§5 recorded *"the locked bound contributes exactly ONE constraint (`|q| >= 1/2`,
non-vanishing)"* and *"only `q = 0` is eliminated — and the charged branch already did that."*

**Both statements fall.**

1. The bound contributes **no** constraint (§1.3).
2. The charged-branch route to excluding `q = 0` is **exactly the charge→flux bridge the 765 hunt
   found named as a would-build** — *"a theorem mapping unit character / `Q_Sigma` data to a fixed
   beta-sensitive geometric flux or current."* It does not exist, so it excludes nothing.

**Corrected ledger: five free classes, ZERO sealed constraints, and `q = 0` is in the surviving
set.** 765's verdict of UNDERDETERMINED is unchanged and in fact strengthened; only its
eliminated-set claim is withdrawn.

---

## 2. AQ2 — THE TOWER RESTATED AS WHAT IT PROVABLY IS

### 2.1 What is exact, and it is stronger than a vanishing sector

[YOURS] AQ2 asks for the sectors where the cross term *provably vanishes*. **No such sector is
derivable** — vanishing requires `nabla_A Phi = 0`, i.e. selecting `Phi`. **But something stronger
and unconditional is available from the bidegree alone:**

```text
T := Gamma_Sigma c(nabla_A Phi)  has bidegree (1,1).
Hence  T : (a,b) -> (a+1, b+1),  which is ORTHOGONAL to (a,b).
Therefore  <(a,b)| T |(a,b)> = 0  identically, for every bidegree sector.
```

**`T` has identically zero diagonal in the bigrading.** Consequently:

- **the displayed tower is EXACT TO FIRST ORDER** — `T` contributes nothing to any diagonal
  matrix element, so it produces no first-order eigenvalue shift on states of definite bidegree;
- **the entire correction is SECOND ORDER**, of the schematic form
  `sum |<(a+1,b+1)| T |(a,b)>|^2 / (E_(a,b) - E_(a+1,b+1))`, and it is **`Phi`-dependent**
  through `nabla_A Phi`;
- and it is a **genuine correction**, not a removable one, since `T != 0` in general.

[YOURS] This is what 764 should have said instead of appending `T` to a scalar formula. It is
also strictly more informative: it explains *why* the naive tower looks right and *where* it fails.

### 2.2 The corrected statement

```text
D_BR^2  =  H_0  +  T ,          on  H_BR = L2(Sigma_BR, S_Sigma tensor E_parent)

H_0 := D_(Sigma,A)^2 + Phi^dagger Phi + C2_parent      [block-diagonal in the bigrading]
T   := Gamma_Sigma c(nabla_A Phi)                      [bidegree (1,1); ZERO diagonal]

SPECTRUM OF H_0 (exact, on the twisted product, at unit radii):
   spec = { p_t^2 + p_q^2 + ell(ell + 2|q|) }  +  [Phi^dagger Phi]  +  C2_parent
   ell = 0,1,2,… on the spin-1/2 ladder ; the ell=0 level is the ZERO-MODE level
   multiplicity:  [2 · N_lattice(p_t,p_q)] × d_S2(ell) × 16
                  d_S2(ell) = 4(ell+|q|)  (ell >= 1) ;  d_S2(0) = 2|q| = |deg L|
   the ×16 is flat ONLY IF the flux U(1) is external to Spin(10) with flat parent connection

STATUS OF D_BR^2 ITSELF:
   NOT a scalar tower.  Exact to first order in T (zero diagonal).
   Second-order and higher: Phi-dependent, unbounded while Phi is unselected.
```

### 2.3 The missing object, named precisely

```text
WOULD-BUILD, to convert the block form into an exact spectrum — ANY ONE OF:

 (a)  nabla_A Phi = 0                      [Phi covariantly constant  =>  T ≡ 0]
 (b)  [T, D_(Sigma,A)^2] = 0  AND  [T, C2_parent] = 0
                                           [simultaneous diagonalization; T becomes a
                                            scalar on each joint eigenspace]
 (c)  a full diagonalization of D_BR^2 on H_BR

NONE EXISTS.  (a) and (b) both require selecting Phi, which PRIN leaves free and which
the free-data ledger (section 2.4) records as unconstrained.
```

[YOURS] Note the shape: **the missing object for the tower is the same free datum as one of the
five ledger classes.** The tower's incompleteness and the ledger's fourth row are one problem.

### 2.4 The free-data ledger, corrected

| # | Free-data class | Sealed status | What would constrain it lawfully |
|---:|---|---|---|
| 1 | `(R_T, R_flux, R_Q)` | **unselected** | boundary closure + the induced action, before any comparison (`PRIN`) |
| 2 | spin structure on `T2_TQ` | **unselected** | same; `TWO`'s "fixed periodic" is a scope restriction, not a selection |
| 3 | parent bundle + characteristic class | **unselected** | same; also decides whether the `×16` is flat (§2.2) |
| 4 | odd profile `Phi` | **unselected** | same; **and it is §2.3's missing object** |
| 5 | chiral index | **unselected** | same; `PRIN`'s hard-failure rule does **not** even name it |

```text
FIVE CLASSES, ZERO SEALED CONSTRAINTS.  A DIVERGENCE from my 765's "5 + 1", not a refinement.
```

[YOURS] `XCHK` notes a further asymmetry I confirm from bytes: the hard-failure rule tests
inequivalent **radii, spin structure, bundle class, or odd profile** — it **does not name the
chiral index**, though the preceding list leaves it free. So the falsifier's own coverage is
narrower than the ledger it follows. **I do not read that as licensing the index; I record it as
a gap in the falsifier's enumeration.**

---

## 3. AQ3 — β AGAINST THE CORRECTED TOWER, VERIFIED NOT ASSUMED

[YOURS] The relay is right to demand this be checked rather than asserted. **The grading argument
is about PARITY; the β mechanism is about SCALING. They are orthogonal properties, and I verify
the split term by term rather than infer it.**

Under a rescaling of the geometric radii by `β` (`R = β c Δτ` being the record cell's
internal↔external conversion):

| Term | Geometric content | Scaling weight |
|---|---|---|
| `p_t^2/R_T^2`, `p_q^2/R_Q^2` | two derivatives | `β^-2` |
| `ell(ell+2|q|)/r_flux^2` | two derivatives | `β^-2` |
| **`T = Gamma_Sigma c(nabla_A Phi)`** | **exactly ONE covariant derivative** | **`β^-1`** (times `Phi`'s own unselected scaling) |
| `Phi^dagger Phi` | zero-order | `β^0` × `Phi`'s scaling (unselected) |
| `C2_parent` | **internal `Spin(10)` invariant; `Sigma_BR` carries no `Spin(10)` directions** | **`β^0`** |

[YOURS] **β SURVIVES, and is more non-uniform after the correction than before.** 764 reported
two weights (`β^-2` geometric vs `β^0` internal). The cross term supplies a **third**, `β^-1`,
because it carries exactly one derivative where the squares carry two. So β does not rescale
`D_BR^2` uniformly and **cannot be absorbed by any overall normalisation** — it reweights three
sectors against each other.

[YOURS] **The verification the relay asked for, stated explicitly:** the bidegree argument
constrains how `T` acts on the **grading** (`(a,b) → (a+1,b+1)`). It says nothing about how `T`
scales with the radii. The geometric-vs-internal split is a statement about **derivative count
and internal-invariant status**, both untouched by parity. **So the β structure is not merely
unaffected by the cross-term correction — the correction refines it.**

[YOURS] Weight still declined, as at 762 and 764: `TWO`'s normalisation is unsealed, and `Phi`'s
own scaling is unselected, so the *relative sizes* are not computable. **The mechanism is
displayed; no weight is claimed.**

---

## 4. GROUNDING, JURISDICTION, VERB AUDIT

### 4.1 Grounding

| # | Claim | Basis | Tag |
|---|---|---|---|
| 1 | `D_BR^2`'s three grades | `ae1d0492…` | PROVABLE |
| 2 | `D_BR` odd ⇒ `D_BR^2` even ⇒ the middle term is even (**forced**) | §1.1(a) | YOURS |
| 3 | Bidegree `(1,1)`; total-even; off-diagonal per factor | `5348bcc4…` §3.2; verified | PROVABLE / YOURS |
| 4 | An unselected non-commuting operator cannot be a scalar summand | `5348bcc4…` §3.3 | YOURS |
| 5 | The `+1` is not bound to `Phi^dagger Phi` by either source | `ae1d0492…`, `7a3c6bc6…` | PROVABLE |
| 6 | `×4` / `×2` multiplicity | 764 §2 (Weyl-audited) and `5348bcc4…` | YOURS, twice-derived |
| 7 | `(k+1)^2 >= k(k+1)`, so `q = 0` satisfies the floor | verified, `k = 0…59` | YOURS, exact |
| 8 | `ell(ell+2\|q\|) − ell(ell+1) = ell(2\|q\|−1)` | verified, `\|q\| = 1/2…9/2` | YOURS, exact |
| 9 | `C2(16) = 45/8` by the weight formula; `dim = 16` | verified independently: `(λ,λ+2ρ) = 45/4`; `Σ_even C(5,k) = 16` | YOURS, exact |
| 10 | Bidegree `(1,1)` ⇒ **zero diagonal** in the bigrading | §2.1 | YOURS |
| 11 | The cross term carries exactly one derivative ⇒ `β^-1` | §3 | YOURS |
| 12 | The hard-failure rule omits the chiral index | `ae1d0492…` | PROVABLE |

**Pin check: 12/12.**

### 4.2 Jurisdiction check

**On adopting a producer lane's refutation.** BR-1 bars a producer-declared object from carrying
a criterion's direction — it does **not** bar me from adopting a refutation I have independently
re-derived. **Every one of the three I checked myself**, and one (§1.1a) I found to be *forced*
by an argument `XCHK` states but does not lean on. I adopt on my own algebra, not on their
authority.

**On the VOID CONDITION.** Nothing chosen from a desired outcome. The corrections run against my
own prior work in all three cases, and §1.4 propagates a further loss into 765's ledger rather
than leaving it standing.

**On R9 / R9-JII and the frozen prereg.** Untouched.

### 4.3 Self verb audit — **CLEAN, with four disclosures**

1. **I conflated factor grading with total grading** (§1.1a) — and the correct argument is one
   line: an odd operator's square is even. I had the premise (`D_BR` is a superconnection) and
   did not draw the consequence.
2. **I put an operator inside a scalar eigenvalue formula** (§1.1b). That is a type error, not a
   numerical one, and it is the more embarrassing kind.
3. **My `|q| >= 1/2` claim is withdrawn, and it propagates** (§1.4): 765's ledger loses its only
   constraint and `q = 0` re-enters the surviving set. **Third consecutive relay in which a
   check reversed something of mine** — and this time the reversal cascades into an artifact
   sealed two relays ago.
4. **Recorded in the other direction:** the multiplicity correction (§1.2) was *confirmed*
   independently, and the zero-diagonal result (§2.1) is a positive contribution neither artifact
   states. A verb audit that logs only losses is as skewed as one that logs none.

---

```text
CROSS_TERM = adopted (algebra displayed).  My 764's "odd in the grading, the only term
   coupling even and odd sectors" is REFUTED, and the refutation is FORCED: D_BR is odd,
   so D_BR^2 is even; D_(Sigma,A)^2 and Phi^dagger Phi are even; the middle summand must
   therefore be even.  Bidegree (1,1) flips BOTH factor gradings and preserves the total.
   Second half adopted too: with Phi unselected the term is operator-valued and generally
   mode-mixing, so it CANNOT appear inside a scalar eigenvalue formula — my 764 section
   1.8 committed exactly that type error.  And the +1 is NOT bound to Phi^dagger Phi by
   either source; that identification is withdrawn.
MULTIPLICITY = adopted — and it is a CONFIRMATION, not a contest: x4 at ell >= 1, x2 at
   the unpaired zero level, matching my own 764 correction and its Weyl audit (4.0000).
Q_CONSTRAINT = adopted (refuted).  Verified myself: the UNTWISTED spectrum (k+1)^2 also
   satisfies the locked floor, since (k+1)^2 - k(k+1) = k+1 > 0.  So q = 0 OBEYS the
   inequality and |q| >= 1/2 is NOT implied.  Add: the target never equates its external
   label q=(+/-1,0) with deg L/2; PRIN leaves the chiral index unselected; the target's
   fixed scope is a restriction, not a derivation; and the source is unsealed with ZERO
   in-corpus digest matches.  PROPAGATES TO 765: its "exactly ONE constraint" and "only
   q = 0 is eliminated" BOTH FALL — the charged-branch route to excluding q = 0 runs
   through the charge->flux bridge the 765 hunt found named as a WOULD-BUILD.  Corrected
   ledger: FIVE FREE CLASSES, ZERO SEALED CONSTRAINTS, q = 0 in the surviving set.
   765's UNDERDETERMINED verdict is unchanged and strengthened.
TOWER = restated (exact sectors named; missing object named).  D_BR^2 = H_0 + T with
   H_0 = D_(Sigma,A)^2 + Phi^dagger Phi + C2_parent block-diagonal in the bigrading and
   T = Gamma_Sigma c(nabla_A Phi) of bidegree (1,1).  NO SECTOR WHERE T VANISHES IS
   DERIVABLE — but something stronger is: a bidegree-(1,1) operator maps (a,b) to
   (a+1,b+1), orthogonal to (a,b), so T HAS IDENTICALLY ZERO DIAGONAL IN THE BIGRADING.
   Hence the displayed tower is EXACT TO FIRST ORDER and the whole correction is SECOND
   ORDER and Phi-dependent.  H_0's spectrum is exact as displayed, with multiplicity
   [2 N_lattice] x d_S2(ell) x 16, d_S2(ell) = 4(ell+|q|) for ell>=1 and 2|q| at ell=0,
   the x16 flat only if the flux U(1) is external to Spin(10) with a flat parent
   connection.  MISSING OBJECT, any one of: (a) nabla_A Phi = 0; (b) [T, D^2] = 0 and
   [T, C2_parent] = 0; (c) a full diagonalization.  All three require selecting Phi —
   the same free datum as ledger row 4, so the tower's incompleteness and the ledger's
   fourth row are ONE problem.
BETA = survives, and is STRENGTHENED — verified term by term, not assumed.  The grading
   argument constrains PARITY; the beta mechanism lives in SCALING; the properties are
   orthogonal.  The correction adds a THIRD weight: geometric squares ~ beta^-2, the
   cross term ~ beta^-1 (it carries exactly ONE covariant derivative where the squares
   carry two), C2_parent ~ beta^0 (an internal Spin(10) invariant, and Sigma_BR carries
   no Spin(10) directions).  So beta reweights three sectors against each other and
   cannot be absorbed by any overall normalisation.  Weight declined: TWO's normalisation
   is unsealed and Phi's own scaling unselected.
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+4 disclosures at section 4.3, including a type error — an
   operator placed inside a scalar eigenvalue formula — and a withdrawal that cascades
   into an artifact sealed two relays ago)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
