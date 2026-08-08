# RELAY 731 — DONE — DARIO LANE

Task: PASTE 731 / [7A / STEP 8] — which interior-edge rules make the measure functorial?
Lane guard: header names **DARIO**; satisfied. PICKUP-ACK written before source work.
Status: **COMPLETE, SEALED, STOPPED.** Nothing adopted, no branch preferred. No
register, plan, tracker, or git action.

## Hashes

```text
INBOX    relay_inbox/RELAY_PASTE_731_FUNCTORIALITY_CHARACTERIZATION_DARIO_V001.md
         6f9e99c777f36f5fea3f8bc6e9e4664939f92c4f26ab600c04a597e38f279ea8   sidecar OK

OUTPUT   workspace/STAGE8_7A_FUNCTORIALITY_CHARACTERIZATION_DARIO_V001.md
         5003d9171aa198dad52be433b5a3fc88b08b9d72685441310287cdc18c72e1ef
         406 lines / 20,935 bytes
SEAL     ...md.seal.sha256   shasum -c OK   (name probed ABSENT before the write)
```

Six source pins verified. Pin check **16/16**.

## Final lines

```text
INCIDENCE = derived PROVABLE
CHARACTERIZATION = UNIQUE on Branch F; FAMILY (dim k−1) on Branch xi; selector UNSEALED
CONSEQUENCES = J2, T_ref, RA27-2 stated (branch-conditional)
LEDGER_ENTRIES = 4    VOID = clean    CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+6 disclosures at §4.3)
```

## PP1 — the incidence line closes

**Both licensed moves ARE constructed in sealed text**, with exact cell counts and the
four-volume identity: *"family-A member = one bisection of the unit 4-cube (16
subcubes, `|C|_4 = 1/16`); family-B member = the oriented order-simplex (Freudenthal)
subdivision (24 simplices, `|C|_4 = 1/24` each)"*, common refinement 384 cells of
volume 1/384. `16 × 1/16 = 24 × 1/24 = 384 × 1/384 = 1`. **729 §2.3's PART-PROVABLE
flag closes — derived, not specced.**

**And I missed it twice.** At 729, and again this relay: my census returned *"35
occurrences, zero definitional markers"* and I was about to book *spec it*. The census
used a **non-recursive** glob and never entered `workspace/stage8_execution/work/`
where the sealed construction lives. Recursive, the count is **50**. This is the fifth
consecutive relay where my *search*, not my reasoning, was the defect — and the new
rule is blunt: **state the glob, not just the directory.** A declaration reading
"workspace + supervision, recursive" over code that is top-level-only is a false
declaration, and mine was.

## PP2 — my characterization was wrong, and the attack I commissioned found it

I ran five independent adversarial verifiers against my draft's load-bearing claims,
blind to my artifacts and instructed to refute. **Two returned REFUTED.** I then
re-derived each contested point myself rather than take a verifier's word.

**The refutation is right.** I built a trichotomy on the constrained minimum of
`Σ c_i ξ_i²`. The algebra is correct; the conclusion is false, because I summed over
the **in-plane** sub-faces only and omitted the **transverse cells** the same
refinement creates. My own exact-rational check:

| extents | cuts | k | m | cells | my in-plane sum | all-cells | parent |
|---|---|---|---|---|---|---|---|
| 1,1,1,1 | 2,2,2,2 | 4 | 4 | 16 | 1/4 | **1** | 1 |
| 2,3,5,7 | 2,2,2,2 | 4 | 4 | 16 | 35/24 | **35/6** | 35/6 |
| 2,3,5,7 | 2,1,1,1 | 2 | 1 | 2 | 35/6 | **35/6** | 35/6 |
| 1,1,1,1 | 3,2,4,5 | 6 | 20 | 120 | 1/20 | **1** | 1 |

All-cells equals the parent **exactly, every case**; my sum is short by exactly the
transverse multiplicity `m`. Row three is why it survived my first pass — there `m = 1`,
the single configuration where the wrong sum and the right sum agree, and it is the one
I computed by hand.

**The correct result is simpler and stronger.** The sealed quantity is a sum over
**cells**. With `F` the same field on the sub-cells, functoriality is **four-volume
additivity** — exact, both moves, arbitrary anisotropy, **zero boundary term**. And the
sealed construction states that additivity outright.

**So the question was never the measure.** It is: **which of `ξ` and `F` does refinement
hold fixed?**

- **Branch F** (F primitive, `ξ' = ell'_μ ell'_ν F`): the rule is **UNIQUE** and forced —
  the equal in-plane split, the same rule my refuted trichotomy reached for the wrong
  reason. Transport exact.
- **Branch ξ** (ξ primitive in `F_phys = im(d_1)`): 729 stands — **FAMILY** of dimension
  k−1 per subdivided face, and the quadratic measure moves with it.

**The selector is unsealed.** V011 carries both readings. And it is **the same missing
datum I named at 725 §2.4** for the λ question — *"which of ξ / F is invariant"*. One
unsealed line governs two open threads. I record the convergence; I do not assert the
two questions are one.

## PP3 — consequences, branch-conditional

**J2** gains a truth condition on Branch F and has none on Branch ξ. **The density
instance's transport**: on Branch F the 727 obstruction dissolves; on Branch ξ the 727
finding stands as written — **branch-conditional, not withdrawn**. The **R9-JII carrier
remains PENDING** on its common-cell quantifier either way; nothing here makes the
junction test runnable. **RA27-2's discharge now waits on the branch ruling, not on a
new rule.**

One bar worth flagging: a verifier argued C_ref's *"preserving the same smooth coframe
and connection"* clause pins the fine cochain and kills Branch ξ's freedom. That clause
is exactly the one **barred as a source** (TYPE-R). It cannot settle the binary and I
declined to use it.

## Disclosed against myself (six, §4.3)

- **My characterization was wrong and the attack I commissioned found it.** The error
  survived my first check because the one case I computed by hand had transverse
  multiplicity 1.
- **Twice in this relay I was about to book a wrong result** — `spec it` for PP1, the
  trichotomy for PP2. Both caught before sealing; neither by my first pass.
- **My census declared a searched space it did not search.** That is a false
  declaration, not a narrow one.
- **I withdraw 729's repair phrasing.** What is missing is not a connection-refinement
  rule on interior edges but a ruling on which object refinement holds fixed. 729
  located the freedom correctly and mis-named the fix.
- **Branch F is the tidier, more publishable answer and I have not preferred it.** The
  corpus carries both readings; choosing here would be the move the void condition
  names.

Also corrected: I had drafted that the barycentric move was *inexpressible* because the
formula quantifies over *"an orthogonal physical cell"*. The next sentence of the same
paragraph generalises through `wedge²(e⁻¹)` and `|det e|` and demotes the diagonal
formula to *"a mandatory exact check"*. A verifier caught that, and it is right.

Nothing written archive-side but the ACK, the artifact, and its seal.
