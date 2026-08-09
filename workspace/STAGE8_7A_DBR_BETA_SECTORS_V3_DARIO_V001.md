# STAGE 8 / 7A / [PLAN:A1-CORRECTIVE-3] — THE BETA SECTORS WITH `w_Phi` SYMBOLIC

Lane: DARIO (Builder B, independent verifier). Relay 789.
State brief pinned by the relay: `PROGRAM_STATE_BRIEF_V005.md` = `e26f0d16055f3e83…` — digest matches
the pin, seal OK, read before task work. Drift check run: V005 and `DECLINE_REGISTER_V002` still
current.
Governing: 787 `STAGE8_7A_REBUILD_V2_CROSSCHECK_CODEX2_V001.md` = `513132c183f1e03e…` SEALED-OK.
**The refutation is ADOPTED.** Law 2a in force. All headline items **CLAIMED**.

## Lead determination — CLAIMED

**787 is right, and the defect is one relay older than the register records.**

Q-695 attributes the implicit `w_Phi = 0` to **784**. It originates at **768** — my own artifact —
and 768 states both halves of the contradiction **in the same paragraph**:

```text
768, final block, verified byte-exact this relay (file 03db8d3da273f42c…):

  "The correction adds a THIRD weight: geometric squares ~ beta^-2, the cross term
   ~ beta^-1 (it carries exactly ONE covariant derivative where the squares carry two),
   C2_parent ~ beta^0 ...
   Weight declined: TWO's normalisation is unsealed and Phi's own scaling unselected."
                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

**`beta^-1` fixes `w_Phi = 0`. The next sentence declares `w_Phi` unselected.** 781 inherited it
(placing `Phi^dagger Phi` in the `beta^0` sector — true only at `w_Phi = 0`), 784 inherited it
again and flagged the neighbouring entry as unselected while leaving the cross term fixed.
**Three relays carried a contradiction that was fully visible in the paragraph that created it.**
I record the corrected attribution for the registrar.

**The symbolic table:**

```text
geometric (three towers)          beta^-2              two covariant derivatives
cross  T = Gamma_Sigma c(grad_A Phi)   beta^(w_Phi - 1)     ONE derivative acting on Phi
C2_parent                         beta^0               internal Spin(10) invariant, radius-free
Phi^dagger Phi                    beta^(2 w_Phi)       zeroth order, two powers of Phi
```

**The core survives for every `w_Phi`, and that is the result worth banking.** The non-uniformity
is witnessed by a pair that contains no `Phi` at all — geometric `beta^-2` against `C2_parent`
`beta^0`. These can never coincide. **So `beta` is non-uniform for EVERY `w_Phi`, and "beta cannot
be absorbed by any overall normalisation" holds unconditionally.** What was `w_Phi`-dependent all
along was only the *count* of sectors — and every count I have written (768's "three", 784's
"four") was stated flatly and is conditional.

**And a temptation, named and declined.** `w_Phi = -1` is the **unique** value collapsing the cross
term, `Phi^dagger Phi` and the geometric towers onto a single weight `beta^-2` — the tidiest
possible grading. **Adopting it because it is tidiest is selection from a desired coefficient.**
It is displayed as one unselected member, exactly like `w_Phi = 0`.

---

## 0. Preflight

```text
OUTPUT NAME   probed recursively before any write: artifact and sidecar ABSENT.
STATE BRIEF   PROGRAM_STATE_BRIEF_V005.md  e26f0d16055f3e83…  seal OK, digest matches the pin.
787           STAGE8_7A_REBUILD_V2_CROSSCHECK_CODEX2_V001.md  513132c183f1e03e…  SEALED-OK
768           STAGE8_7A_TOWER_CONTEST_DARIO_V001.md           03db8d3da273f42c…  SEALED-OK
784           STAGE8_7A_DBR_LAYER_REBUILD_V2_DARIO_V001.md    dcc84e6a58a9fae4…  (subject)
DECLINES      DECLINE_REGISTER_V002.md  957476c8c605a370…  SEALED-OK
LAW 2a        LOCKED_PROCESS.md line 546, verbatim: "the SCALING WEIGHT of every carried
              operator freedom (e.g. w_Phi under beta rescaling) is itself a freedom and gets
              its own row in the freedoms-consumed block."
Q-695         QUESTIONS_SETTLED_REGISTER_V001.md line 15077 — the five confirmed verdicts,
              CITED here and NOT re-derived (AS4).

GATES: alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false.
No member binding; no fixed-point execution; no end test; no numeric evaluation of physical
quantities; no comparison to measured constants; no determinant evaluated; no member evaluated
alone; no bundle class adopted or eliminated.  ***NO w_Phi VALUE SELECTED.***
PE-1..PE-7: pointer-known, ZERO WEIGHT, not opened, not consulted.
```

---

## 1. AS1 — THE SECTOR TABLE, `w_Phi` SYMBOLIC

### 1.1 Re-derived from the sealed operator, not pattern-matched

From 768's sealed operator display (span `[10764,11705)`, span sha `d08cccc778b13b44…`,
re-derived this relay): `D_BR^2 = H_0 + T`, `H_0 = D_(Sigma,A)^2 + Phi^dagger Phi + C2_parent`,
`T = Gamma_Sigma c(nabla_A Phi)`.

Under the common radius rescaling `(R_T, R_Q, r_flux) -> beta·(R_T, R_Q, r_flux)` together with
`Phi -> beta^(w_Phi) Phi`:

| sector | weight | why |
|---|---|---|
| `p_t^2/R_T^2`, `p_q^2/R_Q^2`, `ell(ell+2\|q\|)/r_flux^2` | `beta^-2` | two covariant derivatives; no `Phi` |
| `T = Gamma_Sigma c(nabla_A Phi)` | **`beta^(w_Phi - 1)`** | exactly ONE covariant derivative (`beta^-1`) acting on `Phi` (`beta^(w_Phi)`) |
| `C2_parent` | `beta^0` | internal `Spin(10)` invariant; `Sigma_BR` carries no `Spin(10)` directions |
| `Phi^dagger Phi` | **`beta^(2 w_Phi)`** | zeroth order in derivatives; two powers of `Phi` |

`beta` is **defined** as the parameter of the common radius rescaling, so the radii's weight `1` is
definitional, not selected. Independent radius scalings are the two `beta`-invariant ratios, carried
separately (§2.3).

### 1.2 Specializations — displayed, none selected

```text
w_Phi = -1  : weights {-2, -2, 0, -2}   -> 2 distinct.  UNIQUE minimal grading: cross,
                                           Phi^dagger Phi and geometric all collapse to beta^-2.
w_Phi =  0  : weights {-2, -1, 0,  0}   -> 3 distinct.  Phi^dagger Phi coincides with C2_parent.
                                           *** This is the value 768/781/784 implicitly used. ***
w_Phi =  1  : weights {-2,  0, 0,  2}   -> 3 distinct.  Cross coincides with C2_parent.
generic     : 4 distinct.
```

Exact coincidence conditions:

```text
cross = geometric        <=>  w_Phi = -1        Phi^dagger Phi = geometric  <=>  w_Phi = -1
cross = C2_parent        <=>  w_Phi =  1        Phi^dagger Phi = C2_parent  <=>  w_Phi =  0
cross = Phi^dagger Phi   <=>  w_Phi = -1
```

**NONE IS SELECTED.** `w_Phi = 0` appears only as one unselected member — the one three relays
used without saying so. `w_Phi = -1` appears only as one unselected member — and is flagged
because it is the *attractive* one, which is precisely why it must not be adopted (VOID CONDITION).

---

## 2. AS2 — DOWNSTREAM STATEMENTS RE-EXAMINED FOR `w_Phi` SENSITIVITY

**Ten statements checked. Six hold for all `w_Phi`; four are `w_Phi`-conditional.**

### 2.1 Hold for ALL `w_Phi` — and why

| # | statement | why it is `w_Phi`-independent |
|---|---|---|
| 1 | geometric sector is `beta^-2` | derivative count only; no `Phi` |
| 2 | `C2_parent` is `beta^0` | sealed as radius-free; no `Phi` |
| 3 | **`beta` is NON-UNIFORM** — at least two distinct sectors, always | witnessed by (1) vs (2), a pair containing no `Phi`; `-2 = 0` is impossible |
| 4 | **"`beta` cannot be absorbed by any overall normalisation"** (768's substantive claim) | follows from 3 alone |
| 5 | the two `beta`-invariant ratios `R_T : R_Q : r_flux` (FC-e) | §2.3 — verified explicitly, not inherited |
| 6 | `beta`'s non-uniformity is **class-independent** (775's U8 clause) | `Phi` is a shared datum across members; `w_Phi` carries no bundle-class index |

### 2.2 `w_Phi`-CONDITIONAL — displayed with the condition

| # | statement | origin | condition |
|---|---|---|---|
| 7 | *"adds a THIRD weight … three sectors"* | **768** | true only at `w_Phi ∈ {0, 1}` |
| 8 | *"`Phi^dagger Phi` sits in the `beta^0` sector"* | **781** | true only at `w_Phi = 0` |
| 9 | *"FOUR SECTORS, not three"* (U8 sharpening) | **784** | true only for generic `w_Phi`; **false at `w_Phi ∈ {-1, 0, 1}`** |
| 10 | the sector **count** generally | 768/781/784 | `2` at `w_Phi = -1`; `3` at `w_Phi ∈ {0,1}`; `4` generically |

[YOURS] **My 784 "sharpening" was not a sharpening.** It replaced one flatly-stated count with
another flatly-stated count. The genuinely `w_Phi`-independent statement is #3 — *that* `beta` is
non-uniform, never *how many* sectors it has.

### 2.3 The ratios — `w_Phi`-independence VERIFIED, not inherited

787 confirmed the two ratios independently; AS2 requires me to verify their `w_Phi`-independence
rather than inherit it. Explicitly:

```text
Under beta:  (R_T, R_Q, r_flux) -> (beta R_T, beta R_Q, beta r_flux)
   =>  R_T : R_Q : r_flux is invariant, by cancellation of the common factor.
Phi -> beta^(w_Phi) Phi acts on a DIFFERENT datum and appears in NO radius ratio.
Formally:  d/dw_Phi [ R_T/r_flux ] = 0  and  d/dw_Phi [ R_Q/r_flux ] = 0  IDENTICALLY,
   since neither ratio is a function of w_Phi at all.
```

**FC-e's substance is therefore `w_Phi`-independent**: `beta` is one scalar, the radii are three
independent free data, and quantifying over `beta` does not quantify over the two ratios. That
argument never touches `Phi`.

**One addition FC-e does take, under law 2a:** `w_Phi` is itself an axis a discrimination rule
would have to quantify over. It attaches to FC-e's `Phi` axis rather than opening a new FC — a
bookkeeping choice, and I flag it as mine.

---

## 3. AS3 — `FREEDOMS_CONSUMED`, CORRECTED UNDER LAW 2a

Every row re-checked **against the formulas actually written above** — the enforcement standard,
and the one 781 and 784 both failed.

| datum | tag | where it appears in THIS artifact |
|---|---|---|
| **`w_Phi` — the scaling weight of `Phi`** (law 2a row) | **CARRIED-AS-PARAMETER** | symbolic in §1.1's cross and `Phi^dagger Phi` rows and throughout §1.2/§2. **No value selected.** `w_Phi = 0` and `w_Phi = -1` displayed only as unselected members |
| odd profile `Phi` | **CARRIED-AS-PARAMETER** | §1.1; never given a form |
| `beta` | **CARRIED-AS-PARAMETER** | the rescaling parameter itself; never fixed |
| radii weight under `beta` (= 1) | **DEFINITIONAL, not selected** | `beta` *is* the common radius rescaling; stated at §1.1 |
| `R_T`, `R_Q`, `r_flux` | **CARRIED-AS-PARAMETER** | §1.1 denominators, §2.3 ratios |
| `C2_parent` numerical value | **CARRIED-AS-PARAMETER** | §1.1 row 3; only its `beta`-weight (0) is used, which is sealed |
| bundle class / chiral index `n` | **NOT CONSUMED** | nothing class-dependent is claimed; §2.1 row 6 asserts only independence |
| spin structure / `p^2_min` | **NOT CONSUMED** | no bound stated this relay |
| `N_lattice` | **NOT CONSUMED** | no trace evaluated this relay |
| analytic input `f` | **NOT CONSUMED** | no trace evaluated this relay |
| the counting inner product | **NOT CONSUMED** | no min-norm object used here |

**SUBSTITUTED: none** — and this time the claim is checked line-by-line against §1.1, which is
where the previous two blocks were false.

### 3.1 `FLATTENING_CHECK` — against `DECLINE_REGISTER_V002` (S01–S37)

```text
S28  the five free D_BR data remain unselected, constrainable only by "boundary closure +
     the induced action, before any comparison"                                        LIVE, CLEAN
     Phi is one of the five; w_Phi is its scaling weight.  Both carried as parameters; neither
     constrained here; no boundary-closure argument invoked.
S01  (= seed D1) the +1 / Phi^dagger Phi identification                                 CLEAN
     Not touched: no mu^2 appears in this artifact, and Phi^dagger Phi is carried as an operator
     with a symbolic weight, never as a number.
S27  flat x16 granted only under (F)                                                    CLEAN
     Not touched: no multiplicity claim is made here.
S02–S26, S29–S37: not touched.
FLATTENING_CHECK = clean (37 rows walked; 1 live, 2 adjacent and explicitly untouched).
```

---

## 4. AS4 — SALVAGE

The five confirmed verdicts are **CITED to Q-695, not re-derived**:

| v2 item | disposition |
|---|---|
| radius derivation whole (product-tower square, three denominators, zeroth-order `Phi^dagger Phi`, radius-free `C2_parent`, non-commutation flag) | **CONFIRMED (Q-695)** — stands |
| no implicit unit radius outside the five named `(U)` sites | **CONFIRMED (Q-695)** — stands |
| tier-2 drop (independent 1,911-file probe found no sealed scalar-`Phi` carrier) | **CONFIRMED (Q-695)** — stands |
| tier-3 conditions | **CONFIRMED (Q-695)** — stands |
| member bounds ((F) attached, unconditional in `Phi`, separation `1/r_flux^2`) | **CONFIRMED (Q-695)** — stands |
| the two `beta`-invariant ratios | **CONFIRMED (Q-695)**, and `w_Phi`-independence now **verified here** (§2.3) rather than inherited |
| the S27 multiplicity-only reading | **CONFIRMED (Q-695)** — stands |
| **the `beta`-sector table** | **REFUTED (Q-695); REPLACED by §1.1** |
| 784's U8 "four sectors" sharpening | **`w_Phi`-CONDITIONAL** (§2.2 #9); the surviving claim is #3 |
| `lambda >= C2_parent` | **PROVED (Q-690)** — untouched throughout, and `w_Phi`-independent (it uses only positive-semidefiniteness) |

---

## 5. JURISDICTION AND VERB AUDIT

**Jurisdiction.** *What was the rule written to protect?* Law 2a exists because a sector table can
fix a weight invisibly. The risk was live and realised three times. *Does the outcome space
distinguish a real correction from a restatement?* Yes — §2.1 separates six surviving statements
from four conditional ones, and the survivor set is non-empty and load-bearing. *Would evidence
look different if `w_Phi` were selected?* Yes: some sealed text would fix `Phi`'s scaling. 768's own
sentence says the opposite.

**VOID CONDITION.** `w_Phi = -1` is the maximally tidy value and is displayed **and declined** on
exactly that ground. Nothing is chosen from a desired coefficient.

**BR-1.** The relay authorises the restatement; it does not authorise its result. The
attribution correction in the lead runs against my own oldest artifact in this arc.

**Builder independence.** 787 is Codex 2's sealed cross-check artifact — lawful stock. No
`evaluator_build_A/` or `checks/` file read. `~/.codex` untouched; `memory-bank` never searched.

### 5.1 Self verb audit — **NOT CLEAN: three disclosures**

1. **The substitution is mine and it is one relay older than the register records.** 768 wrote
   `beta^-1` and *"Phi's own scaling unselected"* **in the same paragraph**. Q-695 attributes it to
   784. The corrected attribution is 768 → 781 → 784, three relays, with the contradiction fully
   visible in the paragraph that created it. I report this to the registrar rather than accept the
   gentler attribution.
2. **784's "sharpening" was not one.** It replaced 768's flat "three" with a flat "four". Both are
   `w_Phi`-conditional; the `w_Phi`-independent statement was available the whole time and is
   weaker and more useful — *that* `beta` is non-uniform, not *how many* sectors it has.
3. **The invisible-substitution class has now caught me at values and at weights** — 781 set three
   radii to 1, 784/781/768 set `w_Phi` to 0, and in each case a freedoms block asserted "carried"
   while the formula one line away consumed it. Both were caught by the other lane, one cycle
   after commitment. *The block only works if it is audited against the formulas rather than
   against intent* — which is what §3 does and what my previous two blocks did not.

---

```text
SECTORS = restated symbolic (table displayed; w_Phi unselected).
   geometric (three towers) beta^-2 ; cross T = Gamma_Sigma c(nabla_A Phi) beta^(w_Phi - 1) ;
   C2_parent beta^0 ; Phi^dagger Phi beta^(2 w_Phi).  Re-derived from 768's sealed operator span
   [10764,11705) (span sha d08cccc778b13b44…, re-derived this relay).  Coincidences, exact:
   cross = geometric and Phi^dagger Phi = geometric and cross = Phi^dagger Phi all at w_Phi = -1 ;
   cross = C2_parent at w_Phi = 1 ; Phi^dagger Phi = C2_parent at w_Phi = 0.  Distinct-sector
   count: 2 at w_Phi = -1, 3 at w_Phi in {0,1}, 4 generically.  NONE SELECTED — w_Phi = 0 shown
   only as the unselected member 768/781/784 implicitly used, and w_Phi = -1 shown only as the
   unselected member that is MAXIMALLY TIDY and therefore precisely what the VOID CONDITION
   forbids adopting.
   ATTRIBUTION CORRECTED FOR THE REGISTRAR: the implicit w_Phi = 0 originates at 768, not 784.
   768's final block writes the cross term "~ beta^-1" and, in the SAME PARAGRAPH, "Phi's own
   scaling unselected."  781 inherited it (placing Phi^dagger Phi in the beta^0 sector, true only
   at w_Phi = 0); 784 inherited it again.  Three relays, one paragraph.
DOWNSTREAM = 10 statements checked: 6 all-w_Phi / 4 conditional (displayed).
   ALL-w_Phi: geometric = beta^-2 ; C2_parent = beta^0 ; BETA IS NON-UNIFORM FOR EVERY w_Phi
   (witnessed by geometric -2 vs C2_parent 0, a pair containing no Phi, and -2 = 0 is impossible) ;
   "beta cannot be absorbed by any overall normalisation" ; the two beta-invariant ratios ;
   class-independence of the non-uniformity (Phi is a shared datum; w_Phi carries no class index).
   CONDITIONAL: 768's "adds a THIRD weight" (only w_Phi in {0,1}) ; 781's "Phi^dagger Phi sits in
   the beta^0 sector" (only w_Phi = 0) ; 784's "FOUR SECTORS, not three" (generic only — FALSE at
   w_Phi in {-1,0,1}) ; the sector count generally.
RATIOS = w_Phi-independence VERIFIED, not inherited.  Under beta the triple (R_T,R_Q,r_flux) scales
   by a common factor, so R_T : R_Q : r_flux is invariant by cancellation; Phi -> beta^(w_Phi) Phi
   acts on a DIFFERENT datum and appears in no radius ratio, so d/dw_Phi[R_T/r_flux] =
   d/dw_Phi[R_Q/r_flux] = 0 identically.  FC-e's substance (beta is ONE scalar; the radii are THREE
   independent free data) never touches Phi and is therefore w_Phi-independent.  Under law 2a,
   w_Phi is itself an axis a discrimination rule must quantify over; it attaches to FC-e's Phi axis
   rather than opening a new FC — a bookkeeping choice, flagged as mine.
FREEDOMS_CONSUMED = w_Phi CARRIED-AS-PARAMETER (its own row, law 2a; no value selected) ; Phi
   CARRIED-AS-PARAMETER ; beta CARRIED-AS-PARAMETER ; the radii's weight under beta DEFINITIONAL
   (beta IS the common radius rescaling), not selected ; R_T, R_Q, r_flux CARRIED-AS-PARAMETER ;
   C2_parent value CARRIED-AS-PARAMETER (only its sealed beta-weight 0 is used) ; bundle class n
   NOT CONSUMED ; spin structure / p^2_min NOT CONSUMED ; N_lattice NOT CONSUMED ; analytic input f
   NOT CONSUMED ; the counting inner product NOT CONSUMED.  SUBSTITUTED: NONE — and this time the
   claim is audited line-by-line against section 1.1, which is where the previous two blocks were
   false.
FLATTENING_CHECK = clean (37 rows walked; S28 live and clean — Phi and w_Phi carried, neither
   constrained, no boundary-closure argument invoked; S01 and S27 adjacent and explicitly
   untouched).
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+3): (1) the implicit w_Phi = 0 is MINE and originates at 768, one
   relay earlier than Q-695 records — 768 wrote "beta^-1" and "Phi's own scaling unselected" in the
   same paragraph, and I report the harsher attribution rather than accept the gentler one;
   (2) 784's "sharpening" was not one — it replaced a flat "three" with a flat "four", when the
   w_Phi-independent statement (THAT beta is non-uniform, not HOW MANY sectors) was available the
   whole time; (3) the invisible-substitution class has now caught me at values (781: radii to 1)
   and at weights (768/781/784: w_Phi to 0), each time with a freedoms block asserting "carried"
   while a formula one line away consumed it — the block only works when audited against the
   formulas rather than against intent.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
