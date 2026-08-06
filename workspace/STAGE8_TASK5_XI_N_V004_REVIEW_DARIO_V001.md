# STAGE 8 TASK 5 — Ξ_N V004: FRESH CROSS-FAMILY REVIEW — DARIO V001

Lane: Dario (Claude Opus 5), cross-family review/adjudication lane
Task: PASTE 591 / Task 5
Authority to review: DoR-020-A8. **THIS ARTIFACT ADOPTS NOTHING AND REGISTERS NOTHING.**
Custody: I drafted V001–V003. The pen swapped to Lane 3 for V004. I review fresh.

```text
REGISTER_HEAD = Q-517
XI_N_V004 = CONFIRMED (+2 NOTES, neither adoption-blocking)
READY_FOR_RULING = yes
VERB_AUDIT_SELF = CLEAN
MEMBER_BOUND = false ; FIXED_POINT_EXECUTED = false ; END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MACHINERY_APPEAL = none raised by me (V004's own appeal is concurred in: G4-D +
  FULL-G4 + G5 + ExtSrc/Ker/transport/scalarization are genuinely unbuildable
  from current stock; stating them as gates is the honest move, not a dodge)
```

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-517 | verified |
| V004 `ac9335dc7a2e90ba088467ae0b6409d178c53950568be42af976469b5f917ede` | **verified before reading** |
| V003 re-review `b179f2e175ca4d136fa14cdef35ebe64931e651434ea11cf4fde58038e32f4e9` | verified |
| My V003 `d8f5112951c5378ce10126f91e8c89d0f31ebaae7ba6477677c9beb17b979e6c` | verified |
| Seams V002 `2525096ba06973b70064d6b9f9578470e0afca9c48e2cca6cf0f5c1194d12c52` | verified |
| My seams confirm `7150a768551e983d0bc262721f49f55cd61aea97cbf31458c6cca58f99a9831c` | verified |
| Output name collision (workspace + cleanroom) | none — clear to write |

---

## D1. THE THREE CLOSURES — **PASS ×3**

### D1.1 The anti-counterterm clause (Z13) — **PASS**

[PROVABLE] It is a real fence with a real falsifier, and it is honestly typed.

- The fence `supp_Λ,N(Ξ_N(x)) ⊆ cl_record,N(supp_D,N(x))` (Z13a) is a *support*
  containment, so it excludes exactly the hazard Loc (B6)-(B7) names: period
  content living where the record has no support — a holonomy counterterm hidden
  inside localization.
- The falsifier is one element: `(V3)` is one displayed `x_* ∈ CT_N` (Z13c), with
  `(Z13) at N ⟺ CT_N = ∅` (Z13b). One witness refutes. That is a genuine
  refutability condition, not a biconditional true of everything — which was
  precisely V002's (Z-A7) failure mode, and it is not repeated here.
- **The critical discipline is present verbatim:** *"Before FULL-G4 is formed,
  `CT_N` is UNFORMED, not empty; this is a gate gap, not passage of the clause."*
  This blocks the vacuous-gate exploit. I flag this specifically because
  **my own 574 modulus disjunction failed exactly here** — I offered arms that
  were not independent, and audit V002's Q-mode gate went vacuous as a result.
  V004 does not make that mistake: an unformed failure set is not a passed clause.
- Provenance is correctly separated: *"B7 does not derive the following clause.
  It motivates the failure mode; this draft states the support fence
  independently"*, and `Z13` is tagged AUTHORED, not inherited. That is the
  correct handling of the citation-drift failure mode.
- The self-limiting close is honest: *"It does not claim that every possible
  same-support counterterm is excluded."* The fence catches support-remote
  content only, and says so.

This closes the V003 re-review's sixth defect (Y9/full-G4 anti-counterterm law
omitted).

### D1.2 The typed constancy — sign-collapse rerun **by hand** — **PASS**

[PROVABLE] I reran my own collapse computation against the new clause and it
**does not go through**. V004 adopted REPAIR B. The rerun:

Let `s := q_D,N^addr(x)` for `x ≠ 0`, and take the D-side reversal `r_N^D`.

1. (Z4b) gives `q_D,N^addr(r_N^D x) = s^-`.
2. `S_D,N^addr` is a fixed-point-free ℤ₂-set, so `s^- ≠ s`.
3. Therefore `x` and `r_N^D x` lie in **different** addressed strata.
4. (Z4a) is a conditional on *equal* q-values, and V004 states explicitly:
   *"It says nothing when the two q-values are mate strata s and s^-."*
5. So no relation between `Ξ_N(x)` and `Ξ_N(r_N^D x)` is forced by constancy.

**The collapse is blocked.** V003's unsigned fixed-support constancy silently
forced sign-evenness (`Ξ(r x) = Ξ(x)`), which together with the G5-conditional
sign arm `Ξ(r x) = −Ξ(x)` gave `2Ξ = 0`, hence `Ξ ≡ 0` in a torsion-free
lattice. Orbit-addressing separates the mate strata and the contradiction
dissolves. That was the V003 re-review's R2 (Z3) KILL (+H12) and it is closed.

[PROVABLE] **The fixed-point-freeness is DERIVED, not asserted** — I checked
this, because an asserted freeness would be a look-alike repair. G4-D requires
`Prim_N(S) ≠ ∅` and a ℤ₂-equivariant bijection
`φ_(N,S) : forg_N^{-1}(S) ≅ ∏_{[a] ∈ Prim_N(S)} [a]` with
`φ(s^-) = (φ(s)_[a]^-)_[a]`. If `s^- = s`, then on any component `[a] = {b,b^-}`
we get `φ(s)_[a]^- = φ(s)_[a]`, contradicting the free involution on `[a]`.
The nonemptiness requirement is what makes "any component" available. Sound.

[PROVABLE] **The discipline note is also right and I confirm it independently:**
`R_or,[a]` must *not* be used as `q`'s value, because COMMON (O11) identifies
`(r, b^-)` with `(−r, b)` — which would re-merge exactly the mates the repair
separates. V004 uses an abstract fixed-point-free ℤ₂-set, not the orientation
line. That distinction is load-bearing and correctly drawn.

[PROVABLE — verb check on the closure] The block is a block on an *inference*,
at the clause level, **conditional on G4-D**, which is UNINHABITED. No member is
exhibited and no `Ξ_N` is shown to exist. V004 says this (`STATED BUT
UNRUNNABLE`); I restate it so my own PASS is not read as an existence claim.

### D1.3 The conditioned jump claim, and its dependents — **PASS**

[PROVABLE] The claim is now correct where V003's was false. I verified the
arithmetic directly: along the §5 displayed positive ray, `Θ(t) = exp(ip)` for
`t > 0` by stratum constancy, and `Θ(0) = 1` because `Ξ_N(0) = 0`. A jump at
zero therefore holds **iff `exp(ip) ≠ 1` iff `p ∉ 2πℤ`** — which is (D12).
The unconditional form is withdrawn in the lead. R3 KILL closed.

[PROVABLE] **The dependents are genuinely re-audited, not rubber-stamped.**
The decisive one is the permanent regression (D13): `p ∈ 2πℤ ⟹ Θ(t) = 1` for
all `t ≥ 0` — and then the honest consequence, which is the part that matters:

> *"D13 does not imply `Ξ_N(k) = 0`. If `Ξ_N(k) ≠ 0`, D8 still proves Ξ-space
> discontinuity while the U(1) character is blind."*

This is the correct separation. The character's blindness on `2πℤ` is a fact
about the *observable*, not about `Ξ_N`. V003 conflated the two; V004 does not.

[PROVABLE] The self-limiting rider is present and cuts against the candidate:
whenever the §5 ray is built from a satisfying `ε = 1` Z-A7 response, it lies in
D13, so *"the identity branch requires raw neutrality and forbids an assertion
of a character jump on that ray."* A draft that hands its own reader a case
where its headline claim may not be asserted is not optimising its verbs.

---

## D2. THE VERBATIM CARRY — **PASS, +1 NOTE (N1)**

Method: I did not take the carriage claim on trust. I extracted every
substantive line of my V003 (278 unique lines > 12 chars) and tested membership
in V004 mechanically. 55 lines do not survive byte-identically.

**Direction 1 — nothing my drafts had right was dropped in the swap.** Of the
55, the overwhelming majority are metadata that *must* change under a pen swap
(title, lane line, `REGISTER_HEAD = Q-512`, task number, supersession row,
provenance table rows, `CANDIDATE_V003 = DRAFTED (14 clauses …)`), plus
first-person prose recast as historical. I chased the two load-bearing
mathematical items by name and both survive in reworded form:

| V003 content | Status in V004 |
|---|---|
| The support-birth recurrence of the third horn | survives — lines 130, 134, 139, 147, 219, 914, 945 |
| The real logarithm gated by G2 = whole-image containment + (A4) charts | survives — lines 551, 563, 747, 788, 855, 893, 1001 |

[YOURS] **And V004 tightened one of mine rather than losing it.** V003 stated
the support-birth theorem unqualified. V004 marks it
`SUPPORT-BIRTH THEOREM [CONDITIONAL ON G4-D]`, which is *more* honest than my
draft: the disjointness it consumes comes from (Z2)(iii), which is itself
G4-D-gated. I record this as a correction to my own V003 that I did not catch
and the finder did.

[PROVABLE] The void suite — the V003 re-review's fourth item, *"the void suite
is not carried into the superseding clause set"* — is closed and extended:
`V3` (hidden counterterm), `V4a` (address erasure), `V4b` (selection),
`V4c` (support-birth overclaim). `V4b` is checked live and reported CLEAN by
inspection; `V4a`/`V4c` are correctly reported UNFORMED before their gate data
exist, not clean.

**Direction 2 — nothing confirmed in V003 was silently altered.** The three
marked deltas map exactly onto the three kills:

| Delta | Content | Kill closed |
|---|---|---|
| G1 (line 262) | restore Y9 as (Z13), type FULL-G4, restore V3 falsifier | sixth defect |
| G2 (lines 146, 222) | orbit-addressed oriented-support factor + collapse regression | R2 (Z3) + H12 |
| G3 (line 515) | condition character visibility by `p ∉ 2πℤ`, retain blind regression | R3 |

I confirmed (Z4)'s rewrite from `SUPPORT-STRATUM` to `ORBIT-ADDRESSED
SUPPORT-STRATUM` sits inside §1.3 (154–259), which carries the G2 mark at 222 —
i.e. it is inside a *declared* region, not an unmarked edit.

### N1 — NOTE: the carriage claim's scope is slightly wider than the file

[PROVABLE] §0.1 declares base text retained verbatim except for **four** classes:
metadata, the new dependency audit, the consequence boards, and the three delta
regions. I found one substantive prose sentence altered outside all four. In
§2.2 (Z9), V003's

> **(Z9) names the actual future type and books it.**

became

> **(Z9) retains the actual future type and books it; its displayed clause is unchanged.**

§2.2 is not metadata, not the dependency audit, not a board, and not a G1/G2/G3
region. **No mathematics moves** — the displayed (Z9) clause block is genuinely
unchanged, so `(P0)` ("NO OTHER MATHEMATICAL CLAUSE IS CHANGED") holds, and the
new wording is *more* accurate than mine. The defect is confined to the scope of
the meta-claim: "retained verbatim outside four classes" is falsified by an
instance, where "clause blocks retained verbatim; prose may be re-voiced" would
be true. One-line repair to §0.1. **Not adoption-blocking.**

---

## D3. THE DEPENDENCY RE-AUDIT — **PASS** (two chains verified by hand)

The roots table (§6.1) is complete against the changed clauses and correctly
notes that `Z7/Z8`, `Z9/Z10`, `Z-A7` and `Z5` were *not rewritten* but are
rechecked "because the new clauses consume or constrain their arguments." That
is the right reason to recheck an unchanged clause.

**Chain 1 — G3 → Z3 visibility / Z6 chart gate (§6.4).** Verified above at D1.3:
(D12) and (D13) are both arithmetically correct, and the Ξ-vs-character
separation is correctly drawn. The chain closes with a genuine non-closure:
*"Conditioning W4 does not close G2. Whole-image containment, single-valued
logarithm, response independence, address covariance, and normalization remain
uninhabited. The class in ℝ/(2πℤ) remains exactly Z6."* A re-audit that ends by
re-asserting an open gate is doing its job.

**Chain 2 — G2 → Z-A7 (§6.3, line 750).** This is the sign-sensitive chain and
the one where my own G5-conditional sign arm lives, so I checked it directly.
The claim is orbit-stability: `p ∈ 2πℤ ⟺ −p ∈ 2πℤ` (D11). This is trivially
true — `2πℤ` is closed under negation — but it is the *right* thing to check,
because G2 introduced a reversal that sends `p ↦ −p`, and if Z-A7's condition
were not negation-invariant, addressing would have broken it. Two consequences
are drawn correctly: (i) a refuting `p` refutes together with its mate, so the
universal clause is refutable orbit-wise; (ii) **no address representative is
selected** — which is exactly what keeps the `V4b` selection void clean. I also
confirm (Z-A7)'s quantifier was actually rethreaded through the new structure
("EVERY *addressed* identity-branch response x"), so this is a real re-audit and
not a restatement.

---

## D4. THE ADOPTION-STRENGTH VERDICT — **CONFIRMED, +1 NOTE (N2)**

Walking the 15 clauses as a unit — `(Z1)–(Z13) + (Z-A7) + (Z-U)`; the count is
internally consistent and consistent with V003's 14:

**Internally coherent — yes.** I tested the clause set for the failure mode I
would most expect after a repair of this shape: an interaction between the new
addressing and the old homogeneity. With `r_N^D` the reversal and `t > 0`:
`r_N^D(tx) = t·(r_N^D x)`, so zero-homogeneity gives `Ξ(r_N^D(tx)) = Ξ(r_N^D x)`
while (Z4b) gives `−Ξ(tx) = −Ξ(x)`. Consistent. Applying (Z4b) twice returns
`Ξ(x)`, consistent with the involution. At `x = 0`, `r_N^D 0 = 0` forces
`2Ξ(0) = 0`, hence `Ξ(0) = 0` in the torsion-free lattice — consistent with
(Z2), not an extra constraint. And the collapse's last refuge, a *nonzero fixed
point* of `r_N^D`, is closed by the clause set itself: (Z4b) puts `x` and
`r_N^D x` in mate strata, `s^- ≠ s`, so `r_N^D x ≠ x`. Fixed-point-freeness of
the reversal on nonzero addressed sectors is derived, not assumed.

**Gate-complete — yes.** Every unrunnable clause names its gate (`G4-D`,
`FULL-G4`, `G5`, `G2`, `G2-N`, `G3`/ExtSrc), and `MACHINERY_APPEAL` is non-false
for the first time, which is the honest reading of a candidate this heavily
gated.

**Honest about inhabitance, licensed-not-inhabited in the lead — yes.**
`ADOPTION LICENSES THE INTERFACE; IT DOES NOT INHABIT IT.` is the second line of
the lead. `(Z-U)` closes `STATUS: RESIDUE -- carrier built, bare candidate
exhibited, no HOL member inhabited.` `(Z13)` closes *"It binds no Ξ member and
proves no holonomy route exists."* I find no status-verb optimism.

**Consistent with the R9 diagonal — yes, and correctly narrow.** R9 is cited at
Q-515 *"for the addressed orbit family and is not duplicated or consumed as an
Xi_N inhabitance claim"* (line 34), and line 838 adds *"no Xi inhabitance
inferred."* The candidate takes the orbit family from the sealed repair and
nothing else. That is the correct use.

**Consistent with the oddness falsifier — yes, and I must limit my own prior
finding here.** My 589 confirmation derived, from R9-V002 across an address
orbit, the oddness of the HOL **period**, `p_Hol(c^-) = −p_Hol(c)`. It is
tempting to read that as discharging `(Z-U)`'s outstanding
`Ξ_N(r_N^D x) = −Ξ_N(x)`. **It does not.** `Θ = Hol ∘ Ξ ∘ Ker`, so my corollary
constrains the *composite*; a parity failure in `Ξ` compensated by the log
branch would leave the composite odd. `(Z-U)`'s Ξ-side item is therefore
correctly still open, and V004 is right not to discharge it. I record this
against myself so the finding is not later over-credited.

I note in passing that `(Z-U)`'s Ξ-parity conjunct duplicates `(Z4b)`, which the
candidate already states. This is conservative double-booking — neither listing
discharges the other, so it cannot over-claim — and `(Z-U)`'s Ker-compatibility
requirement `r_N^D ∘ Ker_(a,K) = Ker_(a^-,K^-) ∘ r_(a,K)^O` is genuinely
additional. No defect.

### N2 — FRESH ATTACK: (Z4b) applies an involution that is not declared at `0_D`

[YOURS] `q_D,N^addr : D_N^Loc → {0_D} ⊔ S_D,N^addr`, and the ℤ₂-action `(-)^-`
is declared **on `S_D,N^addr`**, which is stipulated fixed-point-free. But
(Z4b) reads

```text
q_D,N^addr(r_N^D x) = q_D,N^addr(x)^-
```

for `x ∈ D_N^Loc` — and applies `(-)^-` to a value in the *disjoint union*.
At `x = 0` this requires `0_D^-`, which is nowhere defined.

The gap is isolated to exactly one point, because `q_D,N^addr^{-1}({0_D}) = {0}`
— the zero stratum is the single element `0`, not a larger set. And the repair
is forced rather than chosen: `r_N^D 0 = 0` gives `q^addr(r_N^D 0) = 0_D`, so
consistency **requires** `0_D^- = 0_D`. The involution on the disjoint union is
therefore fixed-point-free *away from the basepoint* — which is precisely what
the existing qualifier *"`s^- ≠ s` on every nonzero addressed sector"* is
already signalling. The text nearly says it; what is missing is the one line
extending `(-)^-` to `{0_D} ⊔ S_D,N^addr` by `0_D^- := 0_D` (or scoping (Z4b) to
`x ≠ 0`).

**Grading, honestly: this is a typing gap, not a kill.** Nothing downstream
breaks, no gate moves, no clause's content changes, and the collapse block of
D1.2 is untouched (it operates on nonzero `x`, where `s^- ≠ s` is stipulated).
I raise it because an undeclared operation at a basepoint is where a later
"look-alike" repair could quietly install a *different* extension, and the
candidate should own the one it needs. **Not adoption-blocking.**

---

## D5. VERB AUDIT ON MY OWN BOARD — **CLEAN**

| My verb | Check |
|---|---|
| "The collapse is blocked" (D1.2) | Blocked as an **inference**, at clause level, **conditional on uninhabited G4-D**. No member exhibited, no existence claimed. Stated inline. |
| "Fixed-point-freeness is derived" | Derived *within G4-D's own requirements*, which are uninhabited. It is a sound derivation from stipulated data, not an inhabited fact. |
| "PASS ×3" on D1 | PASS = the closure does what the V003 re-review demanded. It is not a claim that `Ξ_N` exists. |
| "V004 tightened one of mine" (D2) | A correction against my own V003, stated as such. |
| My 589 oddness corollary | Explicitly **limited** at D4: it constrains the composite, not `Ξ`'s parity, and discharges nothing in `(Z-U)`. |
| N1, N2 | Both graded NOTE and both marked not adoption-blocking. I did not inflate either to reach a defect count. |
| "CONFIRMED" | Confirms the candidate at **adoption strength as a licensed interface**. It is not a ruling, not an adoption, and not an inhabitance finding. |

No fence was blocked in a way that forced a structural result, so I raise no
MACHINERY-APPEAL of my own; I concur in V004's.

## Custody disclosure — an unrelated gap in my own record

[YOURS] `STAGE8_TASK5_AUDIT_V002_REVIEW_DARIO_V001.md` (PASTE 577) was **never
written, sealed, or mirrored**. The `Write` failed with a classifier-availability
error and the next relay arrived before I retried. **That relay's verdict is not
of record.** I flag it here because it is the only gap I know of in this lane's
custody chain, and it should not be discovered later as a silent absence.

---

```text
XI_N_V004 = CONFIRMED (+2 NOTES: N1 §0.1 carriage-claim scope wider than the
  file, one prose sentence altered at §2.2 outside the four declared exception
  classes, no mathematics moved; N2 (Z4b) applies (-)^- to a value in
  {0_D} ⊔ S_D,N^addr while the involution is declared only on S_D,N^addr,
  undefined at the single point 0_D, repair forced to 0_D^- := 0_D)
READY_FOR_RULING = yes
VERB_AUDIT_SELF = CLEAN
```

Both notes are one-line repairs that change no clause content, no gate status,
and no verdict. The three kills of the V003 re-review are closed, the void suite
is restored and extended, the carry is faithful in both directions, and the
dependency re-audit is genuine on the two chains I checked myself.
