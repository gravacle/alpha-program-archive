CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; the closure block is the first content)
CLOSURE_END_BYTE = XXXXXXXX   (computed on bytes as a fixed point at seal time)
VERDICT_BEARING_SET = exactly the 6 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
PATH_RULE = every member carries its FULL path from the alpha-program-archive root and is rehashed
  at that path before sealing (Q-913 standard).
ANCHOR_RULE = CLOSURE_MEMBER_CITATION_RULE_V001. No flag name is used as an anchor.
LANE = DARIO   ROLE_THIS_RELAY = CANDIDATE V006 — TWO LINES (relay 1069)
AUTHORITY = member 02, the ATTACH SUPPLY MANDATE, verified LIVE at seal time. It ratifies NO CONTENT
  and none is entered here.
SUPERSESSION = supersedes V005 (member 03) and, through it, V004, V003, V002, V001, APPEND-ONLY.
  ALL FIVE ARE BYTE-UNTOUCHED, verified before and after; the generator refuses if any moved.
SCOPE = EXACTLY TWO INSERTIONS of one line each, taken from sealed V003 by span. Everything else is
  byte-identical to V005 and is digested on both sides at section 4.0.4.
CLOSURE_SCOPE_NOTE = this artifact's verdict-bearing set is deliberately SMALL. The candidate's own
  27-member closure is carried inside the byte-identical body and is unaltered; the members declared
  here are exactly those this relay's two insertions and their verification depend on. Re-declaring
  the full body closure would imply a re-verification this relay did not perform.
ALL_RESULTS = CLAIMED until the opposite-lane check.
SELF_CITATION_BAR = DARIO's own prior outputs are not record witnesses. Members 03 and 05 are members
  ONLY as the superseded subject and the read-only byte source of the two inserted lines.
LIVE_MEMBERS = NONE.
```

| # | Closed member | SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_1069_CANDIDATE_V006_DARIO_V001.md` | `1a782a8d3e9716ba98e0232aedbf07cc7a8752fe75445e15f13b5b7a644b2a93` | assignment |
| 02 | `workspace/ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001.md` | `ad9fc14e1f07494f7527d95f2a94ee7a26da9d49cc784c409f31325f54572213` | **THE AUTHORITY — verified live** |
| 03 | `workspace/STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V005.md` | `96ec8bf4e2706eced5b17489d53f3844402331854ed4ea82d54c212dec3a22d7` | **V005 — superseded, byte-untouched; source of all carried bytes** |
| 04 | `workspace/STAGE8_ATTACH_CANDIDATE_V005_CHECK_CODEX2_V001.md` | `42fbe3930ee66805a4de7ba0d7bfb02e19d2b1e0dcb5db9cd6a68e1e6c2d3ba2` | **the V005 check — the misbounded-span finding** |
| 05 | `workspace/STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V003.md` | `82d5c5dd59d1d0d6981a2cde7244c1dad1a66352c4159b8543f0554777abea31` | **V003 — READ-ONLY BYTE SOURCE of the two inserted lines** |
| 06 | `supervision/PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | state pin |

```text
THE TWO INSERTIONS, taken from sealed V003 (member 05) by span:
  V003 line 255  ->  after V005 line 284   F14's CLOSING CODE FENCE
  V003 line 270  ->  after V005 line 300   F15's FINAL SENTENCE ("it in one pass.")

COMPLETE BLOCKS, verified after insertion (the check's own digests):
  F14  V003 lines 239-255  1,136 B  2aae31641f2802b83334f3e7f3dc1a53630fd36016e411ae55f5c038f75d8783
  F15  V003 lines 257-270    724 B  b9c0208e3d889e66ad6581b39e6f25af7b79f0bedf5fd578914bd00b0490e72e

BLIND HELD. EVERY SCALE SYMBOLIC. NO NUMERIC EVALUATION OF A PHYSICAL QUANTITY. NO MEMBER BOUND.
NO FIXED-POINT EXECUTION. NO END TEST. NO MEASURED-CONSTANT COMPARISON. NO FREEZE. NO SELECTOR FROZEN.
PE-1..17 POINTER-ONLY, LEDGER SHUT. omega_phys UNTOUCHED. CASCADE-TERRITORY STOP FORM LIVE.
alpha_computed = false   proof_authorized = false   kappa_record_computed = false
JOINT_ANCHOR_DERIVED = false
```

CLOSURE_DECLARATION_END

# PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL ENTRY (ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001, ad9fc14e1f07…)

# STAGE 8 — THE ATTACH CANDIDATE, V006 — TWO LINES
## RELAY 1069 — `[PLAN:DESC-33]` — DARIO LANE — TWO INSERTIONS — [CLAIMED]

Date: 2026-08-12
Status: **SUPERSEDES V005 APPEND-ONLY.** V005, V004, V003, V002, V001 all byte-untouched.

**WHAT THE CHECK FOUND, AND WHERE IT ORIGINATED.** The restoration in V005 was byte-exact against the
spans it was given — and **the spans it was given were short by one line each.** V003 lines 239–254
stop one line before F14's closing code fence; lines 257–269 stop one line before F15's final
sentence. So V005 carried an **unclosed code fence** (55 fence markers, odd) and a sentence ending
mid-clause at *"the machine audit found"*.

**The misbounded spans came from the 1064 order itself, and I executed them exactly.** I record that
placement of origin because it is true, and then decline to hide behind it: **a digest that verifies
proves the bytes match the span, and says nothing about whether the span was the right one.** V005's
generator checked extraction fidelity and never asked whether the extracted region was a complete
block — no fence-balance test, no "does this end where a block ends" test. That gap was mine, and this
version closes it with both.

---

## 0. THE TWO SETTLEMENTS, CARRIED

Cited from member 04, not re-argued.

1. **`A4_PHASE = SURVIVES`** (member 04 `:234`; grounds at member 10 `:210-239` and the receiver shape
   at member 03 `:511-515`). `D(z) = diag(1,z,1)` is **not** `λI` for `z ≠ 1`: the first and third
   diagonal entries force `λ = 1` while the second would force `λ = z`. Its projective class is
   nontrivial, so the phase is **relative** and is not the common central scalar the quotient removes.
   **This was the attack I named as sharpest against my own V002 and could not close. Another lane
   closed it. It is carried as settled and I claim no credit for it.**
2. **Circuit canonicity for `K_square` at `b_1 = 1`** (member 04 `:88-108`), from independently rebuilt
   incidence matrices. Carried.

---

## 1. REPAIR (1) — DOMAIN: **NARROWED TO `b_1 = 1`**

**The `b_1 >= 1` claim is WITHDRAWN, not defended.** The check found the inconsistency inside my own
text — member 03 used `b_1 >= 1` at `:192,508` and `b_1 = 1` at `:269`. Those are different domains,
and selector-free canonicity is proved only at the narrower one: a cell with `b_1 > 1` carries several
independent cycle classes, so choosing among them would be exactly the selector I am forbidden to
freeze.

```text
OPERATIVE DOMAIN OF THE CANDIDATE (V003):
  connected admitted cells with b_1 = 1 — the specified square sector, member 10 :1840-1852.
  There the cycle class is unique, so gamma_j is canonical up to the F08 orientation reversal and
  NO SELECTOR IS FROZEN, because there is nothing to select.

DISPOSITION OF b_1 = 0 (tree, incl. first opening): the candidate is INERT and returns U_N^0.
  Correct behaviour — member 11 :70-77 rules the emptiness a DETERMINATION made on purpose.

DISPOSITION OF b_1 > 1: OUT OF SCOPE. Not claimed, not covered, not silently included. Admitting it
  would require a lawful cycle selector, which this artifact does not supply and may not freeze.
```

### 1.1 The three residuals, carried unchanged

```text
R1  the loop-bearing class is SPECIFIED and MANDATED but NOT SEALED     member 10 :2321, :1790
R2  no proof that the restricted domain is THE physical causal-cell domain
                                                                        member 12 :103-111, :168
R3  admissibility is not universality                                   member 10 :296-304
```

Member 04 `:104-106` confirms all three as accurate. They are unchanged, and narrowing the domain does
not shrink them: a **mathematical** sector being record-typed is still not a **physical** domain being
derived.

---

## 2. REPAIR (2) — A5: THE TWO-LINE RECEIVER, AND A LAW THAT HOLDS FOR EVERY PHASE

### 2.1 What was false

V002's intertwining law read with the only type-complete default receiver — the scalar `zI` on
`L_s ⊕ L_t` — holds only at `z = 1`. **Reproduced here before repairing** (member 04 `:159-174`):

```text
on e_s:   E_j(z e_s) = z|r>      but  D(z) E_j(e_s) = |r>        <- disagree unless z = 1
on e_t:   E_j(z e_t) = z|p_Q>    and  D(z) E_j(e_t) = z|p_Q>     <- agree
```

Exact residual, computed over the polynomial ring in `z`: `E_j(zI) - D(z)E_j` has the single nonzero
entry `(z - 1)`. The law was false for every nontrivial phase, and V002 asserted it.

### 2.2 The receiver representation, supplied

`rho_joint` does **not** act on the comparator pair as a common scalar. It acts as the **two-line
direct-sum representation**, one line trivial and one line carrying the character:

```text
R_j(z) := 1_(L_s)  direct-sum  z . 1_(L_t)          [the two-line receiver]

with the transport rule that fixes z from the circuit:

  z := ( rho_joint o iota_rep )( Hol_(gamma_j)(A) )
```

**The corrected intertwining law, verified identically rather than asserted:**

```text
E_j o R_j(z)  =  D(z) o E_j          for EVERY z.

  on e_s:  E_j(R_j(z) e_s) = E_j(e_s)   = |r>     =  D(z)|r>      ✓  (root line: trivial character)
  on e_t:  E_j(R_j(z) e_t) = E_j(z e_t) = z|p_Q>  =  D(z)|p_Q>    ✓  (successor line: character z)

  exact residual E_j R_j(z) - D(z) E_j = 0 identically, checked over the polynomial ring in z and
  re-checked by the generator as a refusal path.
```

This is also *why* the A4 settlement holds, and the two facts are the same fact seen twice: a
representation that is `triv ⊕ χ` is **relative by construction**, and a relative phase is precisely
what the projective quotient does not remove. **I record that as coherence between the settlement and
the repair, not as a second argument for either** — the lesson of the `kappa_ch` correction two relays
ago is that one computation seen twice is one computation.

### 2.3 The forced change elsewhere, traced

The corrected law forces exactly one change upstream, and it is in A4:

```text
A4 AS WRITTEN IN V002:  rho_joint o iota_rep = chi_1  "on the cell comparator line"  (singular)
A4 AS CORRECTED IN V003: the composite must act on L_s (+) L_t as the TWO-LINE representation
                         1 (+) chi_1 — i.e. trivial on the root line, chi_1 on the successor line.
```

Nothing else moves: A1's `theta_j`, A2's circuit, A3's character, and A6–A8 are untouched by this
repair, and F01–F13 are untouched. The trace is one row deep and stops there.

---

## 3. REPAIR (3) — A6: THE SIGN, REPRODUCED THEN CORRECTED

### 3.1 Reproduced first, as instructed

V002 `:325-328` wrote `H_j^(2)(t) = w_j(t) theta_j Q_cell` with `∫w dt = 1`, and claimed
`T exp[-i ∫ H^(2)] = exp(+i theta_j Q_cell) = D_n`.

Since `Q_cell = |p_Q><p_Q|` is a projector (`Q^2 = Q`), the exponential is exact:
`exp(i c theta Q) = I + (e^{i c theta} - 1) Q`. Therefore the displayed Hamiltonian gives

```text
T exp[ -i INT w_j theta_j Q_cell dt ] = exp( -i theta_j Q_cell ) = diag(1, e^{-i theta_j}, 1)
```

which is `D_n` at `n = -1`, **not** at the adopted `n = +1`. **The check is right and V002 was not
executable as written.**

### 3.2 Corrected

```text
A6 STAGE 2, CORRECTED:

  H_j^(2)(t) := - w_j(t) theta_j(A) Q_cell ,     INT w_j dt = 1

  T exp[ -i INT H_j^(2) dt ] = exp( +i theta_j Q_cell ) = diag(1, e^{+i theta_j}, 1) = D_n[a_j]
                                                                                       at n = +1.
```

Verified by the generator as a refusal path, at both signs, using the projector identity rather than a
numerical exponential.

### 3.3 What does NOT change

A6 remains **AUTHORED** and **parent-conditional**, exactly as member 04 `:117-137` rules: no sealed
member supplies a phased one-stage parent, and none contradicts the two-stage proposal, so the
one-stage attack does not make A6 fall — but the parent stays underived (member 20 `:77-101`) and the
consequence V002 stated stands: **the candidate demands a two-stage front from an object that has not
been derived at all.** The sign repair makes A6 executable; it does not make it grounded.

Stage 1 is untouched: `H_j^(1)(t) = v_j(t) B_j` with `∫v dt = tau_R`, giving `S_j` (member 20 `:16-34`).
The stage order remains read off the ratified law (member 14 `:121-150`), not chosen by me.

---

## 4. THE REPAIR — `B_j`, `v_j`, `w_j`, AND THE END OF THE EXEMPTION MECHANISM

### 4.0 RESTORED FROM V003 — the two classification blocks, byte-identical

*The two blocks below are V003's own bytes, extracted from sealed member 05 by span and rehashed
before insertion. **Their internal headings are V003's numbering, carried unchanged** — I have not
renumbered them to fit this artifact's section 4, because renumbering would break the byte-identity
that is the entire point of restoring them. Where V003 says "4.1" and "4.2" inside these blocks, read
"the F14 block" and "the F15 block".*

```text
F14 BLOCK   V003 lines 239-254   1,132 B   749dfe4a7a68efa2c43c870bc8767fcf7ad57c25c6800a324c13e5381455cd33
F15 BLOCK   V003 lines 257-269     708 B   ed824a3b79b4691964f644e829b7376734dc007167a8707e2882eb31bc4a627e
```

#### 4.0.1 The F14 block, restored

### 4.1 `rho_joint` is FORCED — a new row, at its span

The check is right that `rho_joint` was in neither table: no F-row named it, and A4 authors `iota_rep`
while carrying `rho_joint` from member 10. **Putting a forced representation inside the prose of an
authored bridge does not classify it.** Classified now:

```text
F14 (FORCED)  rho_joint — the faithful character of the additive-action comparison group G_joint, and
   the associated Hermitian line bundle L = P x_(rho_joint) C in which U_e is parallel transport.
   SPAN: member 10 :210-239.
   QUOTIENT SCOPE, carried with the row because the row is worthless without it: the projective
   quotient removes only the component acting as ONE COMMON SCALAR on the complete state; rho_joint's
   relative phases on the associated vertex fibres are not automatically that component (member 10
   :224-239; member 12 :35-51 separately distinguishes active U(1)_rel from the common ray-lift phase).
   STATUS: an ADOPTED PREMISE carried at its span — the same standing the check already confirmed for
   F12 and F13. It is NOT derived, and this row does not claim it is.
```

#### 4.0.2 The F15 block, restored

### 4.2 A second escape, surfaced by the machine audit and closed

Running the symbol extraction **before** writing this section — which is the point of doing it by
machine — surfaced one further symbol in neither table: the connection `A` itself. V002 used it in
`theta_j(A)` while tabling only the holonomy *rule* (F05). Closed:

```text
F15 (FORCED)  the adopted auxiliary compact connection `a` on the smooth principal U(1)_rel bundle,
   Level-1 adopted field content.  SPAN: member 12 :47-51.
```

**I record how this was found rather than presenting it as foresight:** prose review had already
passed this artifact twice and missed it both times, exactly as it missed `rho_joint`. The audit found
it in one pass.

#### 4.0.3 CARRIAGE — everything else, byte-identical to V004 (Q-930)

The restoration is an **insertion**. No V004 line is edited, reordered, or removed; the two blocks are
placed here, ahead of V004's own section-4 material, which then follows unchanged.

```text
CARRIED REGION A  = V004 sections 0-3 and the section-4 heading
  V004 lines 85-242    7,172 B   eb3ed614743fba83e8699d522e07dd5d47d144c8c1dff85bb84177ae219c21af
  V005 same bytes      7,172 B   eb3ed614743fba83e8699d522e07dd5d47d144c8c1dff85bb84177ae219c21af

CARRIED REGION B  = V004 sections 4.1 through 8
                    (the escape account, the repair, THE 35/16/0 MAP, the four invariants,
                     V004's own carriage proof, the recount, the candidate, the audits)
  V004 lines 243-577  16,379 B   7b1e2e324c3e60a734fbbeaa01d1e09154fbd04f91d70f5f28972037c76c0880
  V005 same bytes     16,379 B   7b1e2e324c3e60a734fbbeaa01d1e09154fbd04f91d70f5f28972037c76c0880
```

**Region B contains the symbol map, the invariants and the construction block**, so the `35/16/0`
audit result carries by construction rather than by re-derivation — and the generator re-runs it
anyway over the same bytes.

Changed in this version: the closure block, the title/status lines, this section 4.0, and section 9's
final lines. **No claim, count, row, requirement, registry status, residual or invariant changes.**

**What this episode is worth, stated once.** V004's carriage proof was real and it passed — but it
proved that *the regions I chose to carry* were byte-identical, which is silent about a region I chose
to rewrite. A carriage claim scoped to the carried regions cannot detect a deletion in the rewritten
one. **The check that catches this is not a better digest; it is comparing the predecessor's ledger
rows against the successor's text and asking whether every row still has its justification present.**
I record that because it is the generalisable part, and because it is the third distinct way this
artifact's completeness has now failed: prose review, an aliased extractor, and a carriage proof with
a blind spot exactly where the editing happened.

**So I built that check, and it returned something worth knowing.** Refusal path R7 now takes every
row the symbol map names and asks where its classification text actually lives. Result:

```text
ROW_JUSTIFICATION = 16/16 justified
  4 in this artifact      A4, A6, F14, F15
  12 inherited from sealed predecessors
       A1 A2 A3 F01 F02 F03 F04 F05  <- V001
       A7 A8 F10                     <- V002
       A5                            <- V003
```

**Nothing is missing — but three quarters of the ledger's justification lives in superseded
documents.** That is a property of the whole V002→V005 chain, not something this version introduced,
and it is exactly the condition that let two blocks go missing without anything noticing: when most
rows are justified by inheritance, one more absence looks normal. **I am reporting it, not repairing
it.** Importing the tables would be a substantive change the assignment excludes, and the honest move
is to hand the check a measured fact rather than a tidied artifact. R7's first version demanded
in-artifact text for every row and would have refused this artifact outright; that would not have
been a completeness check but a demand that this relay exceed its scope, so it was corrected to
follow the declared predecessor chain and report where.

---

### 4.1 The escape, stated as the check found it

Member 04 `:108-140` ran an independent extraction: it isolated the bytes between
`CONSTRUCTION_BEGIN` and `CONSTRUCTION_END`, lexed the mathematical identifiers generically, and got
**25 construction symbols against a map of 22 — three unmapped**:

```text
B_j   the base-pulse generator, appearing in H_stage stage 1   -> belongs to the carried F10 row
v_j   the base-pulse profile,   appearing in H_stage stage 1   -> belongs to the carried F10 row
w_j   the second-stage profile, appearing in H_stage stage 2   -> belongs to AUTHORED A6
```

**Why my R11 did not catch them is the part that matters.** It did not extract generically. It
admitted only a hard-coded regular-expression inventory, and then placed `B_j`, `v_j` and `w_j` in an
`ALIASES` set described in a source comment as *"bound/local, not ingredients"*. That description was
false: `B_j` and `v_j` are source objects of the forced base-pulse law and `w_j` is load-bearing
authored data. **I wrote a completeness check and then wrote an exemption into it that removed three
real ingredients from its own scope.**

The two earlier failures were prose review missing a symbol. This one is worse in kind: the machine
check I introduced *because* prose had failed twice contained, in its own source, the mechanism that
let the third failure through. **That is not a bug in the check. It is the check inspecting a
narrowed copy of its own subject.**

### 4.2 The repair, exactly as specified

```text
(1) MAP        B_j -> F10 ,  v_j -> F10 ,  w_j -> A6      (the check's own assignment, adopted)
(2) EXTRACTOR  the ALIASES set and the hard-coded regular-expression inventory are DELETED.
               Extraction is now generic over every letter-initial identifier in the block.
(3) AUDIT      rerun, raw output reported below, whatever it computes.
(4) CARRIAGE   nothing else moves; §4.4 proves it by span digest.
```

### 4.3 The map, now total — and the invariants that make an exemption impossible

Deleting one alias list would leave the *mechanism* intact for a future version to misuse. So the
repair is structural rather than cosmetic: the extractor now runs with **no alias set at all**, and
the generator enforces four invariants that make hiding a construction symbol impossible **by
construction**, not by my care:

```text
INV-1  no vocabulary entry may contain "_"                 -> B_j, v_j, w_j could never be filtered
INV-2  no vocabulary entry may be a single character       -> A, J, g, n, r, z can never be filtered
INV-3  vocabulary and map must be DISJOINT                 -> a symbol cannot be in both
INV-4  every extracted token that contains "_" OR is one character MUST be in the map
```

**INV-1 and INV-4 alone would have caught this relay's escape**, because all three escaped symbols
carry an underscore. The remaining filter is a **stated closed vocabulary** of English and operator
words — published below, disjoint from the map, and structurally incapable of holding an ingredient.
That is the difference between a declared lexical class and an exemption list, and it is the whole of
the repair.

```text
SYMBOL_TABLE_MAP_BEGIN
U_N        F01
W_N        F01
D_n        F01
I_3N       F01
j          F01
Q_cell     F02
S_j        F03
r          F03
p_Q        F03
P_0        F04
P_ch       F04
Hol        F05
i          F05
B_j        F10
v_j        F10
rho_joint  F14
L_s        F14
L_t        F14
e_s        F14
e_t        F14
A          F15
theta_j    A1
gamma_j    A2
b_1        A2
n          A3
iota_rep   A4
E_j        A5
R_j        A5
z          A5
o          A5
H_stage    A6
w_j        A6
t          A6
J          A7
g          A8
SYMBOL_TABLE_MAP_END
```

```text
CLOSED_VOCABULARY_BEGIN
DOMAIN admitted cells class connected contour cycle dependence diag every exactly exp for from
holds integral intertwining law of order orientation over per ratified span stage tensor the
through unique verified with
CLOSED_VOCABULARY_END
```

A fifth token class appears in the block and is handled by rule rather than by list: **row labels**
matching `^[FA][0-9]+$` (here, `F08`), which must name a row declared in the ledger. That is a
structural rule with no discretion in it.

**INV-4 earned its place on the generator's first run, and against me.** The first draft of the block
extractor used a bare substring search, which matched the **prose mention** of
`CONSTRUCTION_BEGIN`/`CONSTRUCTION_END` in §4.1 above and returned five bytes of English instead of
the construction. INV-4 reported **zero structural tokens** — an impossible result for a block full of
subscripted symbols — and the run refused. The extractor now matches its delimiters line-anchored.
**I record this because it is the same failure mode one level up:** a checker inspecting the wrong
bytes and reporting a pass is exactly what V003's alias set did, and the only reason this one was
caught in a single run rather than by the opposite lane is that the invariant made a wrong answer
*visibly* wrong instead of silently plausible.

**The raw audit output is reported at §8.3 exactly as the generator computes it.** The check
predicted `25 symbols / 16 distinct rows / 0 unmapped` under its own conservative extraction; my
extraction is **stricter** — INV-4 forces `b_1`, `e_s`, `e_t`, `p_Q`, `r`, `z` and the single-letter
tokens into the map as well — so my symbol count is larger. **A larger count here means a wider net,
not a laxer one**, and the number reported is the number computed.

### 4.4 CARRIAGE — the untouched regions, proved by span digest (Q-930)

Sections 0–3 and 5–7 of V003 are carried into V004 **byte-identical**. Not described as unchanged —
digested on both sides:

```text
CARRIED REGION A  = V003 sections 0 through 3   (settlements; domain; A5; A6)
  V003 lines 81-236   7,090 B   1d14a748ce71a4ea32dc72566fefb978f24a61a3c5327596ad2e1be701413665
  V004 same bytes     7,090 B   1d14a748ce71a4ea32dc72566fefb978f24a61a3c5327596ad2e1be701413665

CARRIED REGION B  = V003 sections 5 through 7   (recount; carried-unchanged; the candidate,
                                                 INCLUDING THE CONSTRUCTION BLOCK ITSELF)
  V003 lines 318-429  5,593 B   e716d80672b25499fed2ef088614051cc7fa3a6abf47508beca443e33def64b0
  V004 same bytes     5,593 B   e716d80672b25499fed2ef088614051cc7fa3a6abf47508beca443e33def64b0
```

**Region B contains the construction block.** That matters: the audit below runs over the *same
bytes* V003's audit ran over, so the improved result is attributable to the extractor and the map
alone, and not to my having quietly rewritten the subject to suit the test. The generator recomputes
both region digests and refuses to seal if either differs.

Changed in this version: the closure block, the title/status lines, this section 4, section 8.3's
audit output, and section 9's final lines. **Nothing in sections 0–3 or 5–7 moves, and no claim,
count, row, requirement, registry status or residual changes.**

---

## 5. REPAIR (5) — THE RECOUNT

### 5.1 Registry, restated with the true statuses

```text
AC-1  carrier/trace                    PASSES        (unchanged)
AC-2  representation                   ** NOT CLOSED **
        The registry (member 07 :249-254) requires rejection of the stationary same-GNS overclaim AND
        a derived moving-front or sector-changing implementation.  A4 supplies a GROUP BRIDGE ONLY.
        The SR representation obstruction remains open — member 03 :443-446 says so itself, and
        member 04 :183-185 holds me to it.  V002 presented AC-2 as "addressed"; that is corrected to
        NOT CLOSED.
AC-3  causal parent / time-ordering    ** PARTIAL, NOT CLOSED **
        A6 names an authored sequence and correctly keeps the parent conditional, but supplies NO
        DERIVED PARENT, and its displayed Hamiltonian carried the sign error now fixed.  This is
        partial addressing.  Saying it plainly: the repair makes A6 executable, not grounded.
AC-4  write/tail analyticity           NOT-YET-TESTABLE  (awaits the parent-derived join and tail test)
AC-5  connected continuum preparation  NOT-YET-TESTABLE  (awaits connected preparation, continuum
                                       ordering, and the completed common-origin object)
AC-6  no-member / character            PASSES        (the origin family remains unbound; n=+1 is a
                                       character, not a family member)

REGISTRY = 2 PASS / 2 NOT-CLOSED (one partial) / 2 NOT-YET-TESTABLE.
```

**AC5 remains a predicate, not a discharged fact. AC6 remains an open, named gap** — `res_B` consumes
an `Omega_C0 in State(A_C0)` that no construction supplies (member 24 `:209-221`).

### 5.2 Typed requirements: **1/5 forced-met**

```text
orientation law          ** THE ONE FULLY FORCED-MET REQUIREMENT **   F08, F09
time-ordering            NOT met: inter-cell is forced (F10) but that is ONE HALF of a single
                         requirement; intra-cell is A6, authored and parent-conditional.  A forced
                         half cannot be counted as a second whole requirement.
representation           NOT met: incomplete; A4 is a group bridge only, AC-2 open.
carrier embeddings       NOT met as forced: E_j and R_j are exact maps but authored identifications.
common-origin cert       NOT met: shape only, AC5 a predicate, AC6 a named gap.

REQUIREMENTS = 1/5 FORCED-MET.
```

V002 claimed `2/5`; **that count is withdrawn.** V001 claimed `5/5`; that remains withdrawn.

### 5.3 The core count, restated per the post-repair tables

```text
FORCED    F01–F15   = 15 rows   (13 confirmed by member 04 :143-154, + F14 rho_joint, + F15 the
                                 connection A — both surfaced as ledger escapes and closed here)
AUTHORED  A1–A8     =  8 rows   (7 NEW; A3 is already adopted elsewhere and adds nothing new)

CORE = 8-AUTHORED (7 NEW).
```

The authored core is **unchanged in size** by these repairs — A5 grew in content but not in row count,
and no new authored ingredient was introduced. **What grew is the FORCED table, by two rows that were
always forced and were simply unclassified.** That is the honest description: the ledger got more
complete, not more generous.

---

## 6. WHAT IS CARRIED UNCHANGED

- The settled A4 phase-survival and circuit-canonicity rulings (§0), cited, not re-argued.
- **The withdrawals stay withdrawals:** V001's "exactly one new ingredient", "representation met" and
  "5/5"; V002's `b_1 >= 1` domain, its `2/5` count, and its false A5 intertwining law.
- The three domain residuals R1–R3 (§1.1).
- Three of the prior refusal's four grounds still stand (member 23 `:370-377`); no Lorentzian parent.
- Placement nonuniqueness: at least four classes, coverage unproved (member 23 `:336-365`).
- **AC6 open. The forcing slot unchanged:** `future_derivation_can_select_the_attach_map = NO_VERDICT`.
- All V002 content the check confirmed: F01–F13 with the F07/F10 receiver limits, the row census, the
  zero-source reduction, the ratified stage order, and the output-inspection firewall.

---

## 7. THE CANDIDATE, AS IT NOW STANDS

### 7.1 The operative construction

```text
CONSTRUCTION_BEGIN
DOMAIN: connected admitted cells with b_1 = 1; gamma_j the unique cycle class, orientation per F08.

  theta_j := contour-integral over gamma_j of A
  Hol     := exp( i theta_j )
  z       := rho_joint ( iota_rep ( Hol ) )
  R_j     := 1_(L_s)  (+)  z . 1_(L_t)
  E_j     : L_s (+) L_t -> span{ |r>, |p_Q> },  E_j(e_s) = |r>,  E_j(e_t) = |p_Q>
  intertwining:  E_j o R_j  =  D_n o E_j        (holds for every z; verified)
  Q_cell  := |p_Q><p_Q|
  D_n     := diag( 1, z^n, 1 ) = exp( i n theta_j Q_cell )
  H_stage : stage 1  = + v_j(t) B_j        -> S_j
            stage 2  = - w_j(t) theta_j Q_cell -> D_n        (order from the ratified law)
  W_N     := tensor over j of ( D_n S_j )
  U_N     := P_0 tensor I_3N  +  P_ch tensor W_N ,   n = +1
  J-dependence: exactly P_ch.   g-dependence: exactly through gamma_j.
CONSTRUCTION_END
```

### 7.2 Zero-source reduction — unchanged and exact

At `A = 0`: `theta_j = 0`, `Hol = 1`, `z = 1`, `R_j = 1 ⊕ 1`, `D_n = I`, so `U_N = U_N^0` (member 18
`:158-169`). Note the corrected receiver reduces correctly too — `R_j(1)` is the identity on both
lines — which the false scalar receiver also did, and is why the defect survived two prose reviews.

### 7.3 What is still not claimed

No Lorentzian parent; no derived cell; no uniqueness of Attach; no physical domain; no discharged
common-origin certificate; nothing entered.

---

## 8. FREEDOMS, FLATTENING, AUDITS, CUSTODY

### 8.1 FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT   = ADOPTED-AND-FROZEN (unchanged)
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  every V003 content the check confirmed — the two settlements, the b_1 = 1 domain and its three
  residuals, the corrected A5 receiver and intertwining law, the corrected A6 sign, the F14/F15
  classifications, the registry statuses, the 1/5 requirement count and the 8-authored core;
  member 04's escape finding and its specified repair; all charter fences.

DERIVED HERE:
  the four extractor invariants INV-1..INV-4 and the observation that INV-1 with INV-4 would have
  caught this relay's escape unaided;
  the two carriage region digests, computed on both sides.

AUTHORED HERE:
  NOTHING.  No ingredient, no scope, no claim.  The map gained three entries that name objects
  already present in the construction and already owned by existing rows; no row was created, no
  row was moved between tables, and the row census is unchanged.

SELECTED HERE:
  NOTHING.  No selector, no member of the origin family, no state, no scale.  NOTHING ADOPTED,
  RATIFIED, ENTERED, PROMOTED OR FROZEN.  No stop lifted.  No decline filled.

SCALING WEIGHTS: none consumed, fixed, formed, compared, or substituted.  Every scale symbolic.
```

### 8.2 Flattening check — S01–S37 walked

- A **bound local** was not flattened into a **non-ingredient**: that false equation, written in my
  own source comment, is exactly what produced the escape (§4.1).
- A **declared lexical class** was not flattened into an **exemption list**: INV-1..INV-4 are what
  make the distinction structural rather than a matter of my good intentions (§4.3).
- A **deleted alias list** was not flattened into a **fixed mechanism**: the mechanism is what was
  removed, not one instance of its misuse.
- A **stricter extraction** was not flattened into a **stronger candidate**: the count rose because
  the net widened; nothing about the candidate improved (§4.3).
- A **repair to a check** was not flattened into a **repair to the thing checked**: no claim, count,
  row or status moves in this version.
- **Carriage** was not flattened into **assertion**: both regions are digested on both sides (§4.4).
- A **prediction by the check** was not flattened into a **target for my output**: the raw computed
  numbers are reported, including where they differ from the check's expectation.

### 8.3 Audits — raw generator output

```text
MANDATE            = LIVE (generator refuses without it)
V003, V002, V001   = BYTE-UNTOUCHED (refusal paths; rechecked after sealing)
PROSE_DIGESTS      = 26/26, STRICT==STABLE (0 live members)
CARRIAGE           = REGION A and REGION B byte-identical to V003, digests recomputed on both sides
CLOSED_CLAIM AUDIT = generic extractor, NO ALIAS SET, invariants INV-1..INV-4 enforced.
                     RAW OUTPUT REPORTED IN THE FINAL LINES, AS COMPUTED.
RESIDUE            = 0 hits (27-token scan over authored prose)
CLOSURE            = declared-first, byte 0, fixed point
OUTPUT_INSPECTION  = NONE-CERTIFIED.  This relay touched a checker and a map; no downstream object
                     was opened, and the battery, kappa_record and alpha remain pointers only.
VERB_AUDIT_SELF    = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
JOINT_ANCHOR_DERIVED = false
```

### 8.4 Custody

- **BUILDER NEVER VERIFIES OWN WORK.** CLAIMED until the Codex 2 check.
- V003, V002 and V001 read-only, superseded append-only, all still sealed and on the books.
- **No register, plan, tracker, or git action of any kind, read-only included.**
- PE-1..17 pointer-only; omega_phys untouched; no member bound; no freeze.

---


#### 4.0.4 THE TWO INSERTIONS AND THE CARRIAGE (Q-930)

Both inserted lines are V003's own bytes, taken by span from sealed member 05:

```text
INSERTION 1   V003 line 255  ->  after V005 line 284
              content: F14's closing code fence
INSERTION 2   V003 line 270  ->  after V005 line 300
              content: F15's final sentence, "it in one pass."
```

Verified after insertion, by the generator, refusing on any mismatch:

```text
F14 COMPLETE BLOCK   V003 lines 239-255  1,136 B
    2aae31641f2802b83334f3e7f3dc1a53630fd36016e411ae55f5c038f75d8783   occurs EXACTLY ONCE
F15 COMPLETE BLOCK   V003 lines 257-270    724 B
    b9c0208e3d889e66ad6581b39e6f25af7b79f0bedf5fd578914bd00b0490e72e   occurs EXACTLY ONCE
FENCE BALANCE        62 markers over the whole artifact, FINAL DEPTH 0 -> BALANCED
                     (V005: 55 markers, FINAL DEPTH 1 -> a fence left open)
                     of the 62, the carried body contributes 50 (V005 L96-693's 49, plus the
                     inserted closing fence); the remainder are this version's own closure and
                     section blocks.
```

*The assignment anticipated `56, even`. The computed total is **62**, because this version's closure
block and its new sections carry their own fenced blocks — a different head and tail than the count
assumed. **The number reported is the number computed.** The property that matters is not the total
but the balance, and it is verified by walking the file and tracking depth rather than by testing
parity: an even count can still be mismatched, whereas a final depth of zero cannot.*

Everything else is byte-identical to V005, digested on both sides:

```text
REGION A   V005 lines  96-284   9,086 B  ea45e4a2417030d07ffac5b8f45c3d30bac6082b497fd23c82288efcb5fc2623
REGION B   V005 lines 285-300     745 B  5139f9be0376521f21aacc2e92aed86501124e232ba008d2d8874d37347ae271
REGION C   V005 lines 301-693  19,831 B  28df927ed3315ba5f0c5b1b60deb8634b3164da491f49e3bea9268754261147e
```

Region C contains the symbol map, the closed vocabulary, invariants INV-1..INV-4 and the construction
block, so the closed-claim audit carries by construction — and the generator re-runs it anyway over
those same bytes.

**The lesson, and it is not the one V005 recorded.** V005 said the generalisable finding was that a
carriage proof scoped to the carried regions is blind to the rewritten one. True, and insufficient.
**This version's finding is narrower and sharper: a span digest certifies fidelity, not completeness.**
Every digest in V005 verified. The bytes were exactly the bytes named. The named bytes were not a
whole block, and no digest can tell you that — only a structural test can. So V006's generator adds
two: **fence balance** (an unclosed fence is a completeness failure a digest cannot see) and
**exact-once occurrence of the complete block**. Those are the tests that would have caught this
without anyone reading the file.

**Four completeness failures now, each in a different layer**: prose review; an aliased extractor; a
carriage proof blind where the editing happened; and a span digest that certified the wrong span. The
common shape is that each check was sound about the thing it measured and silent about its own scope.

---

## 9. FINAL LINES

```text
CLOSURE = declared-first (byte 0; end byte XXXXXXXX computed as a fixed point on bytes; 6 members;
     0 live; residue scan 0 hits from its own run.  The candidate's own 27-member closure is carried
     unaltered inside the byte-identical body; this relay's declared set is deliberately confined to
     what its two insertions depend on.)

F14 = COMPLETE-BLOCK-VERIFIED (1,136 B digest)
     V003 lines 239-255, 2aae31641f2802b83334f3e7f3dc1a53630fd36016e411ae55f5c038f75d8783,
     present EXACTLY ONCE.  The line V005 lacked was its CLOSING CODE FENCE.

F15 = COMPLETE-BLOCK-VERIFIED (724 B digest)
     V003 lines 257-270, b9c0208e3d889e66ad6581b39e6f25af7b79f0bedf5fd578914bd00b0490e72e,
     present EXACTLY ONCE.  The line V005 lacked was its FINAL SENTENCE.

FENCES = BALANCED (62 markers, FINAL DEPTH 0).  V005: 55 markers, FINAL DEPTH 1 — F14's fence never
     closed.  The assignment anticipated 56; the computed total is 62 because this version's closure
     and new sections carry their own fenced blocks, and the number reported is the number computed.
     Balance is verified by walking the file and tracking depth, NOT by testing parity: an even count
     can still be mismatched, a final depth of zero cannot.  A fence check is the cheapest
     completeness test available and V005's generator did not run it.

MAP = 35 symbols / 16 distinct rows / 0 unmapped   (re-run over the carried bytes; unchanged, as
     computed rather than as assumed)

CARRIAGE = SPANNED (all else byte-identical to V005)
     REGION A  V005 L96-284,   9,086 B  ea45e4a2417030d07ffac5b8f45c3d30bac6082b497fd23c82288efcb5fc2623
     REGION B  V005 L285-300,    745 B  5139f9be0376521f21aacc2e92aed86501124e232ba008d2d8874d37347ae271
     REGION C  V005 L301-693, 19,831 B  28df927ed3315ba5f0c5b1b60deb8634b3164da491f49e3bea9268754261147e
     Digests recomputed from sealed V005 and each region required verbatim in V006.
     NO CLAIM, COUNT, ROW, REQUIREMENT, REGISTRY STATUS, RESIDUAL OR INVARIANT CHANGES.

     THE DEFECT'S ORIGIN, STATED PLAINLY: the misbounded spans were in the 1064 assignment and I
     executed them exactly.  That does not discharge it.  A SPAN DIGEST CERTIFIES FIDELITY, NOT
     COMPLETENESS — V005's generator verified that the bytes matched the span and never asked whether
     the span was a whole block.  Closing that gap is this version's only substantive addition to the
     machinery: fence balance, and exact-once occurrence of the complete block.

OUTPUT_INSPECTION = NONE-CERTIFIED
PROSE_DIGESTS = 6/6, STRICT==STABLE
CHAIN_INVOKED = CHAIN_PLACEHOLDER
VERB_AUDIT_SELF = CLEAN

alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
JOINT_ANCHOR_DERIVED = false
```

**THIS ARTIFACT IS PROPOSED_NOT_ADOPTED.** Until an ENTRY addendum names this artifact's digest and
its check's digest, **no construction may consume this candidate as premise.** Forcing slot unchanged:
`future_derivation_can_select_the_attach_map = NO_VERDICT`.

All findings **CLAIMED** until the opposite-lane check.

**Where the candidate stands.** Unchanged in substance since V003. The last four relays have repaired
bookkeeping — a symbol map, an extractor, two dropped blocks, two dropped lines — and **not one of
them touched the physics.** The three substantive exposures are exactly where they have been: A6
demands a two-stage front from a parent nobody has derived, AC-2 is open on the SR representation, and
the operative domain is a mathematical sector no result has shown to be the physical one.

**That pattern is itself worth a sentence.** Six versions and five checks have converged on an artifact
whose remaining defects are all in how it is recorded rather than in what it claims. If the next check
is clean, the question in front of the principal is unchanged from V003 and is not one more pass over
my text: whether a conditional object carrying those three open conditions is entry-eligible at all.
