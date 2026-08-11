CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; no text precedes it)
PREDECLARATION_OUTPUT_SCAN = 0 hits in authored prose (27-token sweep)
VERDICT_BEARING_SET = exactly the 6 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = DARIO (adjudicator)   SUBJECT_LANE = CODEX 2 (run and instrument)
RULING_SPACE = exactly one of DISCLOSED-CONTROL-EXPECTED / GENUINE-INCOMPATIBILITY / GENUINE-REJECTION
DIGEST_RULE = every pinned digest computed from its file; relay digests verified in full
```

| # | Closed member | SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_976_K4_ADJUDICATION_DARIO_V001.md` | `c59cecde76dcef197c74213b59f47c09b2ab4c239ac837ec700250444e1ecb7d` | assignment |
| 02 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V004.md` | `a195edb03b36be44bf8ce1b71dbf1a01a3a0956c4afc65ddf17382cdca4ed0ab` | the governing instrument carrying the G6/K4 clause |
| 03 | `STAGE8_AXN_GAUNTLET_RUN4_CODEX2_V001.md` | `24d795366005c13a634b1b0c42b27970acbffe13b4353352b569240355966e11` | run 4 — verified in full against the relay |
| 04 | `STAGE8_AXN_S1_MEMBER_ATTEMPT_CODEX2_V001.md`, K4 grounds `[12114,13268)` | `32725f12a119bbb456dbe80e2c304e9dfb839acc9a05fda3d9f64e7317158842`; span `fcf8d90eecb442ce114689d2c73bb546b32fe769a14de28c5e32dc8365ad8ce6` | the disclosed control behaviour, rehashed by me |
| 05 | `STAGE8_AXN_ENTRY_DECISION_INSTRUMENT_CODEX2_V002.md`; `ENTRY_ROUND_2_DECISION_OF_RECORD_V001.md` | `af26ab0354420f64718942b9bdcc61a4e6826a885b7ac0440988a25d7f0c95e1`; `bca010f10771ba7fcd81cbfc2e4a430c2add46486ac829a856d8546a71288cca` | the H-HAAR row and price; the principal's entry |
| 06 | `PROGRAM_STATE_BRIEF_V005.md`; `LOCKED_PROCESS.md`; `DECLINE_REGISTER_V002.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`; `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb`; `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | state pin, process law, S01-S37 |

```text
BLIND HELD.  NO BRANCH WEIGHT AND NO PHYSICAL VALUE IS EVALUATED HERE -- the ruling turns on
what the clause ACCEPTS against what the record DISCLOSED, which is a reading of bytes.
```

CLOSURE_DECLARATION_END

# STAGE 8 — AXN K4 ADJUDICATION — DARIO LANE — V001
## RELAY 976 — `[PLAN:AXN-BUILD-D75]` — THE RULING

Date: 2026-08-10
Status: **RULING (b): GENUINE-INCOMPATIBILITY. The clause names product-Haar K4 FAIL by name, the
removal run 4 observed is the disclosed and computed prediction, and the run applied the clause as
written. The failure is branch-specific, so it is not a rejection on the merits. The fork is the
principal's and is displayed unranked.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. The discrimination that decides this

A disclosure that a control **fails** a gate is not a gate that **accepts** the failure. Pricing a known
incompatibility at entry does not convert it into compliance. So ruling (a) requires the **K4 clause
itself** to carry an accepting branch — not the entry instrument, not the price, not the disclosure.
And ruling (c) requires the failure to hold **whatever branch** is chosen.

I read all three sources at their bytes before ruling.

## 2. What K4 accepts — the clause, quoted [PROVABLE]

The gate is **G6 — K4 fiber test on the generated member**, in the governing instrument. It requires,
for every `N<=M`, `(pi_MN)_*(A_M lambda_M) = A_N lambda_N`, integrating **over the full fiber**, and
states that K3 "evaluates only on the zero-section image and cannot stand in for K4." Then, verbatim:

```text
Identity-supported Dirac: algebraic K4 PASS, but no independent promotion or provenance credit.
Product Haar: K4 FAIL on a nontrivial charged character by full-fiber integration.
```

and

```text
If the entered pairing's induced history functional is certified product-Haar-equivalent, the
principal has that structural consequence before the one-shot act; the run still records the
receiver and cannot swap the pairing. If the generated history marginal is in the failing control
class, the run records `K4 FAIL` and stops. ...
In every case the anchor is not revised, narrowed, or swapped after seeing the result.
```

**The clause carries no disclosed-control acceptance branch.** It names product Haar as **FAIL by
name**, and its only instruction for that case is that the run **records `K4 FAIL` and stops**. The
sentence about certification is not an exemption — it says the principal *has that structural
consequence*, which is a warning, not a waiver.

**K4_CLAUSE = demands the charged term's survival under full-fiber integration; accepts no
disclosed-control branch; names product Haar FAIL explicitly.**

## 3. What was disclosed — the grounds, quoted [PROVABLE]

Member 04's span, rehashed by me to `fcf8d90eecb442ce…` (**MATCH**), states the control behaviour as a
computation, not a caveat:

```text
Product-Haar control.  For one appended coordinate and a nontrivial charged character,
integral_U(1) r_(N+1) dH(r_(N+1)) = 0.
The charged term is removed by the fiber integral and retained at stage `N`, so Haar fails K4
...
The controls split.  (control split displayed: Dirac PASS / Haar FAIL.)
```

So the answer to the relay's question is unambiguous: **yes — the charged character integrating to
zero, and the consequent removal of the charged term, was the predicted behaviour.** It was computed
in advance and recorded. The entry instrument's H-HAAR row priced exactly this — *"the K4
charged-character negative control is disclosed before output"* — and the principal's round-2 entry
carries that price.

**DISCLOSURE = predicted precisely the behaviour run 4 observed, including the vanishing integral.**

## 4. Whether the run applied the clause as written [PROVABLE — AS-WRITTEN]

The correspondence is exact:

| The clause says | Run 4 did |
|---|---|
| integrate over the **full fiber**, not the zero section | `K4 | full-fiber weighted projectivity | FAIL` |
| product Haar fails on a nontrivial charged character | charged term removed by fiber integration, retained at stage `N` |
| the run **records `K4 FAIL` and stops** | `REJECTED AT G6 / K4`; `K5`,`K6`,`K7` all `NOT_RUN — ordered stop at K4` |
| the anchor is not revised, narrowed or swapped after the result | no swap attempted; the receiver is recorded |

**RUN_EVAL = AS-WRITTEN.** Run 4 did not misapply the clause; it executed it. It also reached deeper
than any prior run — G0 PASS, G1 7/7, G2, G3 8/8, `res_B`, K1-K3, the blind fiber matched, ten
certificates produced — so the rejection is a genuine gate result, not an early collapse.

## 5. The ruling [PROVABLE — (b) GENUINE-INCOMPATIBILITY]

**Not (a).** The clause names product Haar `K4 FAIL` explicitly. There is no branch to misapply, and
the run applied what is written. A ruling of (a) would have to read an exemption into a clause that
states the opposite.

**Not (c).** The same clause records **`Identity-supported Dirac: algebraic K4 PASS`**. The failure is
therefore **branch-specific by the instrument's own text** — another admitted history branch is not
excluded by K4. A rejection "on the merits independent of the branch choice" is exactly what the
control split refutes.

**(b) GENUINE-INCOMPATIBILITY.** K4 demands what H-HAAR provably cannot supply, and the
impossibility was **known, computed, and disclosed at entry time** — by member 04's vanishing
integral, by the H-HAAR price, and by the clause's own advance warning that a product-Haar-equivalent
entry carries "that structural consequence before the one-shot act."

## 6. The fork, displayed unranked [no recommendation]

The clause constrains the option space before the principal chooses: **"the run still records the
receiver and cannot swap the pairing"** and **"in every case the anchor is not revised, narrowed, or
swapped after seeing the result."** So no post-hoc repair of the rejected entry is available; anything
that changes the branch must be a **fresh principal act**, not a mend.

| Option | What it is | Consequences, as the record states them |
|---|---|---|
| **A — a fresh history-branch entry** | a new principal entry act selecting `H-DIRAC` or `H-OTHER` | `H-DIRAC` has *algebraic K4 PASS* but **no independent promotion or provenance credit**, and K7 provenance must still pass; the entry instrument also makes `H-DIRAC` conditional on a separately sealed faithful joint-pairing construction. `H-OTHER` requires an exact nonclassification certificate. Either cascades: the pairing, its faithfulness certificate, the induced history functional, the equivalence certificate, the frozen-enum disposition and `entered_pairing_sha256` all regenerate |
| **B — a clause disposition** | amend K4/G6 through the supersession machinery | This is an amendment to the governing terms of an act already ADOPTED-AND-FROZEN. **I state and decline the governance question underneath it**, as at 952, 958 and 968: whether that is lawful post-adoption belongs to the principal or registrar |
| **C — record the rejection as final for this entry** | leave run 4's result standing | The anchor is not accepted at core; the record carries a rejection at a named gate with a branch-specific, pre-disclosed cause. Nothing already booked is disturbed — the suite, families, stage rule and entered objects stand as sealed |

**I recommend none of the three.** The choice is the principal's.

## 7. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the G6/K4 clause at the governing instrument's bytes;
  member 04's disclosed control computation at its rehashed span;
  the H-HAAR price and the principal's entry; run 4's ordered result.

SUBSTITUTED:
  NOTHING.  I adjudicated no branch, ranked no fork, and revised nothing.

DECLINED DELIBERATELY:
  option B's governance question -- whether amending the governing terms of an adopted act is
  lawful post-adoption -- declined here as at 952, 958 and 968;
  any recommendation between the three forks.

BLIND:
  no branch weight and no physical value was evaluated.  The ruling required none.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

## 8. Flattening, custody, byte audit

- **S01-S37 FLATTENING CHECK:** walked. A **disclosure that a control fails** was not identified with a
  **gate that accepts the failure** (§1) — the load-bearing distinction. A branch-specific failure was
  not identified with a rejection on the merits (§5). A pre-disclosed consequence was not identified
  with compliance. A displayed fork was not identified with a recommended one (§6). Run 4's depth was
  not identified with a pass, nor its rejection with an error.
- **F_PLDEC:** clause reading, span rehashing and correspondence only. No physical quantity evaluated.
- **BLIND:** held, as the run held it.
- **PE-1..PE-15:** pointer-only, zero verdict weight.
- **BR-1:** the run's own account located what to test; the ruling rests on the instrument's bytes and
  the disclosed grounds, not on the run's characterisation of them.
- **BUILDER-NEVER-VERIFIES:** the run and the instrument are both the opposite lane's; I built neither.
- **CHAIN:** no anchor act, member binding, fixed-point execution, end test, gauntlet run, numerical
  evaluation, or comparison with a measured constant was invoked.

```text
CLOSURE_BEGIN_BYTE = 0
CLOSURE_END_BYTE = 2304
PREDECLARATION_OUTPUT_SCAN = 0 hits
RULING = (b) GENUINE-INCOMPATIBILITY ; FORKS_DISPLAYED = 3 ; FORKS_RANKED = 0
CLAUSE_ACCEPTING_BRANCH = none ; CONTROL_SPLIT = Dirac PASS / Haar FAIL
```

Self verb audit: "quoted" applies to the clause and the disclosure, both reproduced from bytes.
"As-written" applies to the run on a displayed correspondence. "Genuine-incompatibility" is the single
ruling the relay's space allows for these facts, and I state why (a) and (c) are excluded rather than
only why (b) fits. "Declined" names the governance question and the ranking, both refused.
`VERB_AUDIT_SELF = CLEAN`.

## 9. Final lines

```text
CLOSURE = declared-first (byte position 0, closure end 2304; scan 0 hits)
K4_CLAUSE = quoted. G6 requires (pi_MN)_*(A_M lambda_M) = A_N lambda_N integrated over the FULL FIBER, and states K3 cannot stand in for it. It carries NO disclosed-control acceptance branch: it names the two controls by name -- "Identity-supported Dirac: algebraic K4 PASS, but no independent promotion or provenance credit" and "Product Haar: K4 FAIL on a nontrivial charged character by full-fiber integration" -- and its only instruction for the failing class is that "the run records K4 FAIL and stops". The sentence about a certified product-Haar-equivalent entry is a WARNING, not a waiver: it says the principal "has that structural consequence before the one-shot act", and adds that the run "cannot swap the pairing" and that "in every case the anchor is not revised, narrowed, or swapped after seeing the result"
DISCLOSURE = quoted. Member 04's span, rehashed by me to fcf8d90eecb442ce... MATCH, states the behaviour as a COMPUTATION rather than a caveat: "For one appended coordinate and a nontrivial charged character, integral_U(1) r_(N+1) dH(r_(N+1)) = 0. The charged term is removed by the fiber integral and retained at stage N, so Haar fails K4", with the controls splitting Dirac PASS / Haar FAIL. THE REMOVAL RUN 4 OBSERVED WAS THE PREDICTED BEHAVIOUR, computed in advance; the entry instrument's H-HAAR row priced exactly it -- "the K4 charged-character negative control is disclosed before output" -- and the principal's round-2 entry carries that price
RUN_EVAL = AS-WRITTEN. The correspondence is exact at every line: full-fiber weighted projectivity tested rather than the zero section; the charged term removed by fiber integration and retained at stage N; K4 recorded FAIL with K5, K6 and K7 all NOT_RUN on an ordered stop; no swap attempted. Run 4 did not misapply the clause, it executed it -- and it reached deeper than any prior run (G0 PASS, G1 7/7, G2, G3 8/8, res_B, K1-K3, blind fiber matched, ten certificates), so the rejection is a genuine gate result rather than an early collapse
RULING = GENUINE-INCOMPATIBILITY (fork displayed). NOT (a): the clause names product Haar K4 FAIL explicitly, so there is no branch to misapply and a ruling of (a) would have to read an exemption into a clause stating the opposite. NOT (c): the same clause records identity-supported Dirac as algebraic K4 PASS, so the failure is BRANCH-SPECIFIC BY THE INSTRUMENT'S OWN TEXT and no universal rejection follows. THE DISCRIMINATION THAT DECIDES IT: a disclosure that a control FAILS a gate is not a gate that ACCEPTS the failure, and pricing a known incompatibility at entry does not convert it into compliance. K4 demands what H-HAAR provably cannot supply, and the impossibility was known, computed and disclosed at entry -- by the vanishing integral, by the H-HAAR price, and by the clause's own advance warning. THE FORK, DISPLAYED UNRANKED AND CONSTRAINED BY THE CLAUSE (no post-hoc repair; any branch change must be a FRESH principal act): (A) a fresh history-branch entry, where H-DIRAC has algebraic K4 PASS but no independent promotion or provenance credit and must still pass K7, and is conditional on a separately sealed faithful joint-pairing construction, while H-OTHER needs an exact nonclassification certificate -- either cascading through the pairing, faithfulness certificate, history functional, equivalence certificate, enum disposition and entered_pairing digest; (B) a clause disposition through the supersession machinery, which is an amendment to the governing terms of an ADOPTED-AND-FROZEN act and whose governance question I STATE AND DECLINE as at 952, 958 and 968; (C) record the rejection as final for this entry, leaving the suite, families, stage rule and entered objects standing as sealed. I RECOMMEND NONE
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
