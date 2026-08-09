# STAGE 8 / 7A / [PLAN:A1-CORRECTIVE-4] — ROW 7 SPLIT: A COUNT PREDICATE AND AN ATTRIBUTION PREDICATE

Lane: DARIO (Builder B, independent verifier). Relay 801.
State brief pinned: `PROGRAM_STATE_BRIEF_V005.md` = `e26f0d16055f3e83…` — digest matches, seal OK,
read before task work. Drift check: V005 current.
Governing: **796** `STAGE8_7A_BETA_V3_CROSSCHECK_CODEX2_V001.md` = `f78c115aea4e78bd…`, `.md.seal`
**OK** (law 8: both spellings probed; `.seal.sha256` absent). **The refutation is ADOPTED.**
Headline **CLAIMED**. PE-1..7 pointer-only, not opened, not consulted.

## Lead determination — CLAIMED

**768's sentence binds a COUNT to an ATTRIBUTION, and my V3 row 7 carried the binding intact
while I was in the middle of correcting a different conjunction.**

```text
768, verbatim (file 03db8d3da273f42c…):
   "The correction adds a THIRD weight: geometric squares ~ beta^-2, THE CROSS TERM ~ beta^-1
    (it carries exactly ONE covariant derivative where the squares carry two), C2_parent ~ beta^0."
```

That is two predicates in one clause — *how many* sectors there are, and *which term supplies*
the third. They have different truth sets:

| | predicate | exact condition |
|---|---|---|
| **P7a** | the distinct-sector count is **three** | `w_Phi ∈ {0, 1}` |
| **P7b** | the **cross term** supplies the third weight (distinct from both geometric and `C2_parent`) | `w_Phi ∉ {−1, 1}` |
| **768's compound** | P7a **AND** P7b | **`w_Phi = 0` only** |

**At `w_Phi = 1` the count is still three, but the cross term has merged with `C2_parent` and it is
`Phi^dagger Phi` that supplies the third weight.** My V3 row 7 read *"true only at
`w_Phi ∈ {0,1}`"* — correct for P7a, **false for the compound**.

**Only row 7 conflates. The other three conditional rows and all six unconditional rows are single
predicates**, walked and verified below.

---

## 1. THE SPLIT, RE-DERIVED FROM THE SECTOR FORMULAS

The V3 table (789, unchanged here):

```text
geometric (three towers)   beta^-2            cross  T = Gamma_Sigma c(nabla_A Phi)   beta^(w_Phi - 1)
C2_parent                  beta^0             Phi^dagger Phi                          beta^(2 w_Phi)
```

### 1.1 The coincidence conditions that separate the predicates

```text
cross = geometric   <=>  w_Phi - 1 = -2  <=>  w_Phi = -1
cross = C2_parent   <=>  w_Phi - 1 =  0  <=>  w_Phi =  1
=> P7b (cross supplies a weight distinct from both) holds iff w_Phi NOT in {-1, 1}.

count of distinct weights:  2 at w_Phi = -1 ;  3 at w_Phi in {0, 1} ;  4 otherwise
=> P7a (count is three) holds iff w_Phi in {0, 1}.

P7a AND P7b  =  {0,1} \ {-1,1}  =  {0}.
```

### 1.2 Verified over `w_Phi ∈ {−2, −3/2, −1, −1/2, 0, 1/2, 1, 3/2, 2, 3}`

| `w_Phi` | weights | P7a | P7b | 768's compound |
|---:|---|:---:|:---:|:---:|
| −1 | `{−2, −2, 0, −2}` | F | F | F |
| **0** | `{−2, −1, 0, 0}` | **T** | **T** | **T** |
| **1** | `{−2, 0, 0, 2}` | **T** | **F** | **F** |
| generic | four distinct | F | T | F |

### 1.3 Who supplies the third weight at `w_Phi = 1`

```text
weights: geometric -2 ; cross 0 ; C2_parent 0 ; Phi^dagger Phi 2
distinct: {-2, 0, 2}    ->  cross COINCIDES with C2_parent at 0;
                            the third weight, 2, is supplied by Phi^dagger Phi.
```

**796's attribution confirmed by independent re-derivation.**

---

## 2. THE OTHER ROWS, WALKED

**Independently re-derived, not inherited from 796's confirmations.**

| row | statement | shape | conflation? |
|---|---|---|---|
| **8** | `Phi^dagger Phi` sits in the `beta^0` sector | `2 w_Phi = 0` — one sector's weight | **NO.** Holds exactly at `w_Phi = 0` (verified) |
| **9** | FOUR SECTORS, not three | pure count `= 4` | **NO.** Holds iff `w_Phi ∉ {−1, 0, 1}` (verified) — matches 789 |
| **10** | count is 2 at `−1`, 3 at `{0,1}`, 4 generically | pure count | **NO.** Verified across all tested `w_Phi` |
| **U1–U6** (unconditional) | geometric `= beta^-2`; `C2_parent = beta^0`; `beta` non-uniform for every `w_Phi`; non-absorbable by an overall normalisation; the two `beta`-invariant ratios; class-independence | single-sector, single-inequality, or ratio statements | **NO.** None names a *supplier*; `U3` is the single inequality `−2 ≠ 0`, verified for all tested `w_Phi` |

```text
OTHER_ROWS = walked clean.  Row 7 was the only conflation.
```

**Nothing else is updated.** The symbolic table, the six unconditional statements, the ratios, the
census and the freedoms block stand as 796 confirmed them.

---

## 3. FREEDOMS CONSUMED, FLATTENING CHECK

### 3.1 `FREEDOMS_CONSUMED` (law 2a) — item by item against §1–§2

| datum | tag | where |
|---|---|---|
| **`w_Phi`** | **CARRIED-AS-PARAMETER** — no value selected; `w_Phi ∈ {−1, 0, 1}` appear only as points where predicates change truth value | §1.1–1.3 |
| odd profile `Phi` | **CARRIED-AS-PARAMETER** — no form, norm, or commutation supplied | §1 |
| `beta` | **CARRIED-AS-PARAMETER** | §1 |
| the common radius weight `1` | **DEFINITIONAL** — `beta` *is* the common rescaling | §1 |
| `R_T`, `R_Q`, `r_flux` | **CARRIED-AS-PARAMETER** — not re-derived here; untouched | — |
| numerical `C2_parent` | **CARRIED-AS-PARAMETER** — only its sealed `beta`-weight `0` is used | §1.1 |
| bundle class `n`, spin structure, `N_lattice`, `f`, the counting metric | **NOT CONSUMED** — no trace, bound, or member statement in this artifact | — |

**SUBSTITUTED: none.**

### 3.2 `FLATTENING_CHECK` — against `DECLINE_REGISTER_V002` (S01–S37)

```text
S28  the five free D_BR data remain unselected          LIVE, CLEAN — Phi and w_Phi carried as
     parameters; neither constrained; no boundary-closure argument invoked.
S01  (= seed D1) the +1 / Phi^dagger Phi identification CLEAN — no mu^2 appears; Phi^dagger Phi is
     carried as an operator with the symbolic weight beta^(2 w_Phi).
S27  flat x16 granted only under (F)                    CLEAN — no multiplicity claim here.
S02-S26, S29-S37: not touched.
FLATTENING_CHECK = clean (37 rows walked; 1 live, 2 adjacent and explicitly untouched).
```

---

## 4. VERB AUDIT

**VOID CONDITION.** No `w_Phi` value selected. `w_Phi = 0` appears only as the point where 768's
compound predicate happens to hold — *stated as its truth set, not adopted*. `w_Phi = −1` and
`w_Phi = 1` appear only as coincidence points.

**BR-1.** The relay authorises one bounded correction; it does not authorise its result. §1 runs
against my own V3.

### 4.1 Self verb audit — **NOT CLEAN: two disclosures**

1. **I carried a conjunction while correcting a conjunction.** 789 existed to fix an invisible
   substitution inside 768's `beta` paragraph. I split 768's claim from 781's and 784's, and I
   read each row's *condition* — but I never asked whether a single row held **two predicates**.
   768's sentence bound a count to an attribution and I copied the binding forward. **This is the
   third conjunction failure of the session** (742: a conjunctive clause read as one claim; 788:
   D11's two requirements read as one; here: a count and an attribution carried as one row) — and
   the first where I was actively auditing the very paragraph that contained it.
2. **The correction narrows a truth set I had reported as wider.** Row 7's compound holds at
   `w_Phi = 0` alone, not on `{0, 1}`. Nothing downstream consumed row 7 — 796 confirmed the six
   unconditional statements, the ratios and the block — so no further artifact needs amendment,
   and I state that rather than leave the scope of the fix implicit.

*Direction check:* both run against my own work; neither creates a result. The corrected row is
strictly weaker than the one it replaces.

---

```text
ROW7 = split (predicates + conditions displayed).
   768's clause — "The correction adds a THIRD weight: geometric squares ~ beta^-2, the cross term
   ~ beta^-1 ..., C2_parent ~ beta^0" — binds a COUNT to an ATTRIBUTION.  Split:
     P7a  "the distinct-sector count is THREE"                    holds iff w_Phi in {0, 1}
     P7b  "the CROSS TERM supplies the third weight, distinct
           from both geometric and C2_parent"                     holds iff w_Phi NOT in {-1, 1}
     768's COMPOUND = P7a AND P7b = {0,1} \ {-1,1} = {0}          holds ONLY at w_Phi = 0
   Derived from the coincidence conditions cross = geometric <=> w_Phi = -1 and
   cross = C2_parent <=> w_Phi = 1, re-derived from the sector formulas and verified over
   w_Phi in {-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2, 3}.
   AT w_Phi = 1 the count is still three, but cross (0) COINCIDES with C2_parent (0) and the third
   weight (2) is supplied by Phi^dagger Phi — 796's attribution confirmed by independent
   re-derivation.
   MY V3 ROW 7 SAID "true only at w_Phi in {0,1}": correct for P7a, FALSE for the compound.
OTHER_ROWS = walked clean.  Row 8 (Phi^dagger Phi in the beta^0 sector) is one sector's weight,
   2w_Phi = 0, holding exactly at w_Phi = 0 — no conflation.  Row 9 ("FOUR SECTORS, not three") is
   a pure count, holding iff w_Phi not in {-1,0,1} — no conflation, and matching 789.  Row 10 (the
   count schedule) is a pure count — no conflation.  The six unconditional rows are single-sector,
   single-inequality or ratio statements and none names a SUPPLIER; U3 is the single inequality
   geometric(-2) != C2_parent(0), verified for every tested w_Phi.  All re-derived independently
   rather than inherited from 796's confirmations.  Row 7 was the only conflation, and NOTHING ELSE
   IS UPDATED: the symbolic table, the six unconditional statements, the ratios, the census and the
   freedoms block stand as 796 confirmed them.
FREEDOMS_CONSUMED = w_Phi CARRIED-AS-PARAMETER (no value selected; -1, 0, 1 appear only as points
   where predicates change truth value) ; Phi CARRIED-AS-PARAMETER ; beta CARRIED-AS-PARAMETER ;
   the common radius weight 1 DEFINITIONAL ; R_T, R_Q, r_flux CARRIED-AS-PARAMETER (untouched) ;
   numerical C2_parent CARRIED-AS-PARAMETER (only its sealed beta-weight 0 used) ; bundle class n,
   spin structure, N_lattice, f and the counting metric NOT CONSUMED.  SUBSTITUTED: NONE.
FLATTENING_CHECK = clean (37 rows walked; S28 live and clean; S01 and S27 adjacent and explicitly
   untouched).
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+2): (1) I CARRIED A CONJUNCTION WHILE CORRECTING A CONJUNCTION —
   789 existed to fix an invisible substitution inside 768's beta paragraph; I split 768's claim
   from 781's and 784's and checked each row's CONDITION, but never asked whether a single row held
   TWO PREDICATES, and 768's sentence bound a count to an attribution.  THIRD conjunction failure
   of the session (742, 788, here), and the first while actively auditing the paragraph containing
   it; (2) the correction NARROWS a truth set I had reported as wider — row 7's compound holds at
   w_Phi = 0 alone, not on {0,1}; nothing downstream consumed row 7, so no further artifact needs
   amendment, and I state that rather than leave the fix's scope implicit.
   Both run against my own work; the corrected row is strictly weaker than the one it replaces.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
