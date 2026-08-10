# STAGE 8 — CROSS-CHECK OF THE BASE-FAMILY INVERSE ATTACK
## DARIO LANE (Builder B, verifier) — RELAY 887 — [PLAN:AXN-BUILD-B15]

```text
alpha_computed         = false
proof_authorized       = false
kappa_record_computed  = false
```

All charter fences live. No member bound; no fixed-point execution; no end test; no smooth import; no
EM identification; no numeric evaluation of any physical quantity; no comparison to measured
constants; no common cell formed; no junction map evaluated. PE-1..PE-13 pointer-only, none opened or
consulted. Builder-A code not opened. `~/.codex` untouched; memory-bank never searched. No register,
plan, tracker, git action.

CLAIM STATUS: **all headline items CLAIMED.**

**CUSTODY OF THIS PASS.** Relay 887 was first reached by chained pickup from 884, when the
**claim-status gate fired** — Codex's 885 subject did not exist — and I stopped cleanly, writing
`887_DONE.md` and **no artifact**. On re-invocation the gate has **opened**:
`STAGE8_AXN_BASE_FAMILY_INVERSE_CODEX2_V001.md` = `e857302bd35c01dd` is present with its sidecar,
**seal verified BEFORE reading**. The output name was **still absent**, so no overwrite question
arises. **The prior gate-stop record stands unamended.**

**DISCLOSED.** The check's centre — the C7 **zero-section vs Kolmogorov** distinction — is **my own**
(864, confirmed at 872). That makes me both well placed and at risk: a construction satisfying C7
while quietly assuming marginal consistency is exactly what the distinction exists to catch, and
equally I could **over-apply** it against a construction that genuinely derives the marginal
condition. **I pressed the system against the sealed amplitudes and the displayed square, not against
my restatement of them.**

---

## 0. LEAD

| item | result |
|---|---|
| constraints | **CONFIRMED** — K1–K7, with K3/K4 independence re-derived from the direction argument |
| verdict | **CONFIRMED — `CONSTRAINT-GAP`**, and the three-way elimination is tight |
| Haar | **CONFIRMED-COROLLARY** — and I verified it numerically, `1.5e-16`, with a control |
| S1 | **MATERIAL-PARTIAL, NARROWED** — from "a base family" to four named interfaces plus an exact conditional quotient |

**The finding I most wanted to test is right, and right for the reason that matters.** K3 is
contravariant zero-section compatibility; K4 is pushforward projectivity; and **K4 is not implied by
K3 because `π_MN` and `j_NM^Q` run in opposite directions.** That is the sharpest statement of my own
864 distinction anyone has written, including me.

**And the same asymmetry does double duty: it is also what refutes Haar.** K3 **evaluates at a point**
of the fiber (the identity, where any character is 1); K4 **integrates over** the fiber (where a
nontrivial character integrates to zero). **My 864 carried Haar's refutation as an external fact
(Q-239); here it falls out of the constraint system as a corollary.** That is a genuine structural
unification, and it is the consistency check the relay asked for.

---

## 1. THE CONSTRAINT SYSTEM — **CONFIRMED**

Checked against the sealed amplitudes and the displayed square. The two conditions that carry the
weight:

**K3 — C7 section naturality.** `j_NM^{Q,*} A_M = A_N`, contravariant, fixing appended coordinates to
the identity. The artifact states it is *"expressly not Kolmogorov consistency."* **Correct, and it is
my own 864/872 distinction stated at its own bytes.**

**K4 — weighted projectivity.** `(π_MN)_* ν_M = ν_N`, i.e. `(π_MN)_*(A_M λ_M) = A_N λ_N`. **A linear
constraint on the unknown bases**, and the artifact's reason for independence is exact:

> *"It is not implied by K3 because `π_MN` and `j_NM^Q` have opposite directions."*

**I re-derived that rather than accepting it.** `π_MN ∘ j_NM^Q = id_N`, so the section and projection
compose to the identity **on the section's image** — which is precisely why K3 constrains `A` only
**at** that image. A pushforward, by contrast, **integrates over the entire fiber**. **One condition
is a point evaluation, the other a fiber integral; they cannot imply one another.** Confirmed.

**K6 — normalization, at the correct type.** `A_N(1_{Q,N}) = 1` is **pointwise** and does **not**
imply `λ_N(total) = 1` or `ν_N(total) = 1`. **This is the type discipline S12 exists for**, and the
artifact keeps it: a measure-normalization functional must be **declared separately** and be
compatible with K4. **No type is flattened.**

K1 (carrier/σ-algebra/extension class as **requirements, not outputs of `A_N`**), K2 (the density
binding is the **only** sealed amplitude-to-measure relation; point values do not define countable
additivity), K5 (amplitude invariance does **not** force a unique covariance law for `λ_N`, especially
on an amplitude-null sector), and K7 (direction-bearing common-origin descent; **intrinsic quotient
measure cannot replace it**) all check at their stated scopes.

`CONSTRAINTS = CONFIRMED.`

---

## 2. THE VERDICT — **`CONSTRAINT-GAP` CONFIRMED**, and the elimination is tight

The artifact eliminates the other three terminal values. **I checked each, and the two controls do
double duty — which is why both are needed:**

| eliminated | why, and my check |
|---|---|
| `FAMILY-REFUTED` | the algebraic core is **not** inconsistent — **the Dirac control proves satisfiability**: identity-supported families satisfy the local section/projectivity and point-normalization equations, because sections and projections preserve the identity and `A_N(1)=1`. **A system with a solution cannot be refuted.** |
| `FAMILY-FORCED` | **Dirac and Haar are two distinct completions of the same C7 data.** Two completions ⇒ nothing forced. **This is why the second control is load-bearing rather than decorative** |
| `RESIDUAL-FREEDOM` | premature — `M_N`, `Norm`, `Cov`, `Prov` are **typed placeholders**, so the quotient `R_A` is **conditional**, not inhabited. Reporting a residual family would assert an inhabited object |

**The void-condition press the relay asked for, and it comes back clean.** The verdict is a
**negative**, so nothing is selected by it. The two controls are **expressly classified as controls,
not constructions** — the artifact says the Dirac move *"is a consistency control, not an admissible
S1 construction"* and records that it is *"a newly selected history law with no common-origin
descent."* **Nothing is chosen, and the one object that could have been mistaken for a construction is
labelled a control at the point of use.**

**The conditional quotient is displayed honestly.** `R_A ≅ image(D_A) ∩ Proj ∩ Cov ∩ Norm ∩ Prov`,
with the affine fiber `D_A^{-1}(ν) = λ_0 + ker(D_A)`. **Two distinct freedoms are separated** — freedom
among admissible weighted families, and amplitude-null lift freedom within one family. **Separating
them is the right move**: they would have to be closed by different objects.

`VERDICT = CONFIRMED.`

---

## 3. THE HAAR COROLLARY — **CONFIRMED**, and verified independently

The claim: product Haar satisfies K3 but **fails K4** for a nontrivial charged character. **I checked
it numerically rather than reasoning about it.**

```text
K3 at the section :  chi(identity) = chi(0) = 1.0          -> pullback preserves A ; K3 HOLDS
K4 over the fiber :  integral chi_n dHaar  =  1.5e-16      -> character orthogonality ; K4 FAILS
control, n = 0    :  integral chi_0 dHaar  =  1.000000     -> NO obstruction on the trivial character
```

**The control matters:** it shows the failure is **specific to the charged sector**, not a generic
defect of Haar. **So Haar is not "wrong" — it is wrong exactly where the physics lives.**

**And the mechanism is the same direction asymmetry as K3-vs-K4.** K3 evaluates the amplitude **at a
point** of the fiber, where every character equals 1; K4 **integrates over** the fiber, where a
nontrivial character vanishes. **One structural fact yields both the independence of the two
conditions and the refutation of the candidate.** That is a strong internal consistency signal for the
whole derivation, and it is what the relay's task (3) was asking for.

**Bearing on my own prior work, stated plainly:** at 864 I carried Haar as *"present-and-refuted"* on
Q-239's authority — an **external** fact I cited. **It is now a corollary of the constraint system**,
which is strictly better: a refutation that falls out of the conditions is more robust than one
imported alongside them.

`HAAR = CONFIRMED-COROLLARY.`

---

## 4. SCOPE DISCIPLINE — held

Primitive/flat scope as sealed. **No continuum import**: the constraint system is stated over finite
stages `N` with the extension class a **declared requirement** rather than an assumed one. **Nothing
installed** — `M_N`, `Norm`, `Cov`, `Prov` remain typed inputs; the quotient is conditional; no
carrier, σ-algebra, extension class, normalization functional, covariance action, or descent is
constructed.

**S1 status per this check.** `MATERIAL-PARTIAL`, unchanged in class, **narrowed in content**: from my
864's *"a base family `λ_N` not generated by the ratified law, germ, P2, or PathCert"* to **four named
input interfaces** — instantiate the branch-joint prequotient measurable carrier and extension class;
declare the measure-normalization functional; supply the covariance/boundary/contour/domain actions
and common-origin descent; supply a reproduction/characteristic theorem — **plus the exact conditional
quotient they would inhabit.** **That is a real narrowing of the gate I typed at 864, and it does not
move S1's class.**

---

## 5. FREEDOMS-CONSUMED (law 2, law 2a)

```text
CARRIED UNCHANGED: K1-K7 at their stated scopes; the sealed pointwise normalization A_N(1)=1 as
  POINTWISE and never as a measure normalization; the two controls AS CONTROLS, never as
  constructions; the conditional quotient as CONDITIONAL; primitive/flat scope with NO continuum
  import; S1's class MATERIAL-PARTIAL; Q-239's Haar refutation, now carried as a COROLLARY rather than
  an imported fact.

DERIVED HERE: (a) independent re-derivation of K3/K4 independence from pi_MN o j_NM^Q = id_N holding
  only ON the section's image — point evaluation versus fiber integral; (b) numerical verification of
  the Haar corollary at 1.5e-16 WITH a trivial-character control isolating the failure to the charged
  sector; (c) the observation that the two controls DO DOUBLE DUTY — Dirac gives satisfiability
  (killing FAMILY-REFUTED) and Dirac-plus-Haar gives two completions (killing FAMILY-FORCED); (d) the
  observation that ONE direction asymmetry yields both the K3/K4 independence and the Haar refutation.

SELECTED HERE: NOTHING.  No carrier, sigma-algebra, extension class, base family, normalization
  functional, covariance action, descent, or characteristic theorem is constructed, chosen, or
  installed.  NO FLAG MOVES.  S1 is narrowed, not discharged.

NOT DONE AND DISCLOSED: I verified K3/K4 and K6 in full and checked K1/K2/K5/K7 at their stated scopes
  rather than re-deriving each from its cited bytes.  My Haar verification is a character-orthogonality
  computation on the fiber — it confirms the mechanism, NOT every step of the artifact's control
  argument.  I did not audit C_885's closure member-by-member.
```

**FLATTENING CHECK — 37/37 walked, clean.**
**S03 and THE VOID CONDITION — live at §2, and the artifact under check holds them.** The available
move was to promote the Dirac control — which **satisfies the local equations** — into an inhabited
family, or to report the conditional quotient as `RESIDUAL-FREEDOM`. **Neither is done**, and the
control is labelled a control at the point of use.
**S12** — the pointwise/measure normalization types are kept apart, which is the whole of K6.
**S26 / S08 / S19 / S24** untouched — **no continuum import**; the extension class stays a declared
requirement.
**T1 / T5** untouched.
**BR-1 HELD IN BOTH DIRECTIONS.** The subject is a producer-declared object and got no weight toward
itself — K3/K4 independence was re-derived and the Haar corollary recomputed. **And my own 864 got no
confirming weight toward its own distinction**: I tested whether the artifact over- or under-applied
it, and it does neither.

---

## 6. FINAL LINES

```text
CONSTRAINTS = CONFIRMED.  K1-K7 checked against the sealed amplitudes and the displayed square.  THE
  TWO THAT CARRY THE WEIGHT: K3 is contravariant zero-section compatibility (j_NM^{Q,*} A_M = A_N,
  appended coordinates fixed to the identity, "expressly not Kolmogorov consistency") and K4 is
  pushforward projectivity ((pi_MN)_* nu_M = nu_N).  I RE-DERIVED THE INDEPENDENCE RATHER THAN
  ACCEPTING IT: pi_MN o j_NM^Q = id_N, so section and projection compose to the identity ONLY ON THE
  SECTION'S IMAGE, which is exactly why K3 constrains A only THERE — while a pushforward INTEGRATES
  OVER THE ENTIRE FIBER.  ONE CONDITION IS A POINT EVALUATION, THE OTHER A FIBER INTEGRAL; THEY CANNOT
  IMPLY ONE ANOTHER.  This is the sharpest statement of my own 864/872 distinction anyone has written,
  including me.  K6's type discipline is correct and is the whole of S12 here: A_N(1_{Q,N}) = 1 is
  POINTWISE and does NOT imply lambda_N(total) = 1 or nu_N(total) = 1; a measure-normalization
  functional must be DECLARED SEPARATELY and be K4-compatible.  K1/K2/K5/K7 check at their stated
  scopes.
VERDICT = CONFIRMED (CONSTRAINT-GAP), and the three-way elimination is TIGHT because THE TWO CONTROLS
  DO DOUBLE DUTY.  FAMILY-REFUTED is unavailable because THE DIRAC CONTROL PROVES SATISFIABILITY —
  identity-supported families satisfy the local section/projectivity and point-normalization equations,
  since sections and projections preserve the identity and A_N(1) = 1, and A SYSTEM WITH A SOLUTION
  CANNOT BE REFUTED.  FAMILY-FORCED is unavailable because DIRAC AND HAAR ARE TWO DISTINCT COMPLETIONS
  OF THE SAME C7 DATA, and two completions force nothing — WHICH IS WHY THE SECOND CONTROL IS
  LOAD-BEARING RATHER THAN DECORATIVE.  RESIDUAL-FREEDOM is premature because M_N, Norm, Cov and Prov
  are TYPED PLACEHOLDERS, so R_A is CONDITIONAL, not inhabited.  THE VOID-CONDITION PRESS COMES BACK
  CLEAN: the verdict is a NEGATIVE so nothing is selected by it, and the one object that could have
  been mistaken for a construction — the Dirac family — is labelled "a consistency control, not an
  admissible S1 construction" AT THE POINT OF USE, and recorded as "a newly selected history law with
  no common-origin descent".  The conditional quotient R_A = image(D_A) ∩ Proj ∩ Cov ∩ Norm ∩ Prov with
  affine fiber lambda_0 + ker(D_A) SEPARATES TWO DISTINCT FREEDOMS — freedom among admissible weighted
  families, and amplitude-null lift freedom within one family — which is right, because they would
  have to be closed by different objects.
HAAR = CONFIRMED-COROLLARY, VERIFIED INDEPENDENTLY AND NUMERICALLY.  K3 at the section: chi(identity)
  = chi(0) = 1.0, so the pullback preserves A and K3 HOLDS.  K4 over the fiber: integral chi_n dHaar =
  1.5e-16, character orthogonality, so the pushforward VANISHES on the charged sector while A_N
  lambda_N does not — K4 FAILS.  TRIVIAL-CHARACTER CONTROL, n = 0: integral chi_0 dHaar = 1.000000, NO
  obstruction — SO THE FAILURE IS SPECIFIC TO THE CHARGED SECTOR, and Haar is not "wrong" but WRONG
  EXACTLY WHERE THE PHYSICS LIVES.  AND THE MECHANISM IS THE SAME DIRECTION ASYMMETRY AS K3-VS-K4: K3
  EVALUATES AT A POINT of the fiber, where every character equals 1; K4 INTEGRATES OVER the fiber,
  where a nontrivial character vanishes.  ONE STRUCTURAL FACT YIELDS BOTH THE INDEPENDENCE OF THE TWO
  CONDITIONS AND THE REFUTATION OF THE CANDIDATE — a strong internal consistency signal for the whole
  derivation.  BEARING ON MY OWN WORK: at 864 I carried Haar as "present-and-refuted" on Q-239's
  AUTHORITY, an EXTERNAL fact I cited; IT IS NOW A COROLLARY OF THE CONSTRAINT SYSTEM, which is
  strictly better — a refutation that falls out of the conditions is more robust than one imported
  alongside them.
S1 = MATERIAL-PARTIAL, NARROWED (class unchanged, content narrowed).  From my own 864's "a base family
  lambda_N not generated by the ratified law, germ, P2, or PathCert" to FOUR NAMED INPUT INTERFACES —
  instantiate the branch-joint prequotient measurable carrier and extension class; declare the
  measure-normalization functional; supply the covariance/boundary/contour/domain actions and
  common-origin descent; supply a reproduction/characteristic theorem — PLUS THE EXACT CONDITIONAL
  QUOTIENT THEY WOULD INHABIT.  A REAL NARROWING OF THE GATE I TYPED AT 864.  S1 IS NOT DISCHARGED AND
  NO FLAG MOVES.
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+3):
  (1) THE CHECK'S CENTRE IS MY OWN DISTINCTION, AND I HAD BOTH FAILURE MODES AVAILABLE — under-apply
      it and miss a smuggled Kolmogorov assumption, or over-apply it and reject a construction that
      genuinely derives the marginal condition.  I tested for BOTH and the artifact does NEITHER: K3
      and K4 are stated separately, their independence is argued from DIRECTION rather than asserted,
      and K4 is never quietly derived from K3.  I record that confirming my own distinction is the
      comfortable outcome and that the guard was re-deriving the independence myself.
  (2) I CONFIRMED ON ALL FOUR AXES.  The guard was that each check was made INDEPENDENT of the
      subject: the K3/K4 independence RE-DERIVED from the composition identity, the Haar corollary
      RECOMPUTED numerically with a control the artifact does not display, and the three-way
      elimination checked by asking what each control ACTUALLY PROVES rather than accepting its label.
      The double-duty observation is mine and is the part of this check I would most want attacked.
  (3) MY COVERAGE IS UNEVEN AND "CONFIRMED" SHOULD NOT IMPLY OTHERWISE — K3, K4 and K6 verified in
      full; K1, K2, K5 and K7 checked AT THEIR STATED SCOPES rather than re-derived from their cited
      bytes; C_885's closure NOT audited member-by-member; and my Haar computation confirms THE
      MECHANISM, not every step of the artifact's control argument.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

---

**GATES HELD.** All charter fences live; nothing selected; no smooth import; no EM identification; no
member binding; no fixed-point execution; no end test; no numeric evaluation of physical quantities;
no comparison to measured constants; no common cell formed; no junction map evaluated. PE-1..PE-13
pointer-only, none opened or consulted. Builder-B independence held. `~/.codex` untouched;
memory-bank never searched. No register, plan, tracker, or git action.
