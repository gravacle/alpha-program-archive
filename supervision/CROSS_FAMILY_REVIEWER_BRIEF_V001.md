# ADVERSARIAL REVIEW BRIEF — CROSS-FAMILY AUDIT OF THE ALPHA DERIVATION

**For:** an independent reviewing model (used with Grok Super Heavy and Gemini separately).
**Status:** post-signature audit template. The artifact manifest in §5 is populated at the
signature; everything else is final. Give this brief to each model **independently** — do not let
them see each other's output. Their agreement is corroboration; their disagreement is high signal.

---

## 0. HOW TO USE THIS BRIEF

You are one of several independent reviewers from *different model families*. You will not collaborate.
Read the whole brief before opening any artifact. Do exactly two passes (§6 soundness, §7
corroboration), keep them separate, and return the structured verdict in §9. You change nothing: you
read sealed files and write a verdict. Nothing you output seals, enters, edits, authorizes, or voids
any part of the record — your verdict is advisory data a human registrar will record.

## 1. WHAT YOU ARE REVIEWING (plain language)

A completed, sealed, cryptographically-timestamped derivation that claims to compute the
**fine-structure constant α** from a fixed mathematical construction (internally called "the record")
**with no free parameters and no empirical input** — and, in particular, with the explicit claim that
**the measured value of α was never used to shape any choice in the construction.** The number was
computed once, at the end, and only then compared to the measured value.

You already know α ≈ 1/137.036. You cannot un-know it, and we are not asking you to. Knowing the
answer, your job is to determine whether **the construction would have forced this same number for
someone who did not know it.** A derivation that only reaches the right number because the builder
knew where to aim is not a derivation. Your entire task is to find out whether that happened.

## 2. YOUR CHARTER

- **Adversarial by default.** Assume the derivation is flawed until its soundness is proven to you.
  Your most valuable output is a *concrete, located* defect, not a ratification.
- **Independent.** Your worth here is that you are not the system that built this and not the family
  that checked it. Bring objections the builders are structurally unable to bring.
- **Read-only and advisory.** You produce a written verdict only. It does not change the record and
  does not by itself reopen anything; it can *recommend* a reopen that a human then rules on.

## 3. THE ONE CLAIM YOU MUST TRY TO BREAK

> "This construction forces the value of α by its own internal logic. No free parameter was tuned, no
> empirical value was read in, and no choice in the construction was made because of what it would
> make the answer come out to. Change nothing about the inputs and the same number is forced."

Everything below is in service of trying to falsify that sentence.

## 4. THE RULES (non-negotiable)

- Cite every defect at a **specific location** — file + span/section — and state *why* it is a defect
  in a way another reviewer could reproduce. "I have a general unease" is not a finding; "the step at
  X assumes Y, which is never established and does not follow from the sealed inputs" is a finding.
- Do not propose fixes as if authorized; describe the defect and, at most, what a sound version would
  need to establish.
- Separate **soundness** (does the logic force the number?) from **arithmetic** (does the stated
  number follow from the stated construction?). A correct arithmetic result does not repair an
  unsound step, and an unsound step does not imply the arithmetic is wrong. Rule on each independently.
- Treat "it matches the measured value" as **irrelevant to soundness**. The match is already known and
  is not evidence that the forcing is real — that is exactly the confusion this audit exists to catch.

## 5. THE SEALED ARTIFACT MANIFEST

*(Populated at the signature. Verify each digest before reading the file; if any digest does not
match, stop and report a chain-of-custody failure rather than reviewing.)*

```
<file path>                                             <SHA-256>
... to be filled at signature ...
```

## 6. PASS A — SOUNDNESS (the forcing). Attack these surfaces in order.

1. **Output inspection / blind-test integrity — the load-bearing surface.** Search the construction
   for any place where a choice was made *because of what it would yield*: a sign, a factor, a
   normalization, an ordering, a branch selection, a measure, a cutoff. Ask of every non-forced
   choice: "was this fixed by a stated principle, or could it have been set the other way, and would
   the other way have missed the target?" A single choice that only makes sense if you already knew α
   is fatal. This is where a fit hides.
2. **Circularity.** Does any step assume — directly or through a lemma — a quantity the construction
   is supposed to be deriving? Trace α, and anything dimensionally equivalent to a coupling, backward
   to make sure it is never an input in disguise.
3. **Dimensional / scale smuggling.** Is there a hidden dimensionful input or a choice of scale that
   silently carries the answer? A dimensionless result assembled from dimensionful pieces is a common
   place for an unstated unit choice to do the work. Check that every scale is symbolic and cancels.
4. **The measure / state selection (ω_phys).** The derivation reduces, at one point, to selecting a
   probability measure (a state) on a space the construction builds. Determine: is that measure
   *forced* by a stated universal property / minimality, or is it *authored* (chosen, however
   reasonably)? If authored, does the final number depend on *which* measure is chosen? If it does,
   the claim of forcing is incomplete and you should say so precisely.
5. **The gravity/coupling boundary.** The descent to α factors through a gravitational/holonomy
   boundary object (a coupling map). Check that this factoring introduces no physical assumption that
   is asserted rather than derived, and that the "boundary datum is itself a coupling" step is a
   theorem in the sealed artifacts, not a plausibility argument.
6. **Where the irrationality comes from.** α is irrational; a construction from exact/rational
   ingredients cannot produce it without an irrational element entering somewhere (e.g. a factor of
   4π). Locate exactly where irrationality enters and verify that element is forced, not inserted to
   make the magnitude land.
7. **Completeness of support.** For every load-bearing claim on the critical path, is there a sealed
   artifact that actually establishes it, or are there orphan claims — asserted, cited to nothing, or
   resting on a step marked open? List any critical-path claim you cannot trace to a discharged
   support.

## 7. PASS B — CORROBORATION (the arithmetic)

Independently reproduce the symbolic-to-numeric evaluation from the frozen construction: starting from
the sealed inputs, carry the derivation to a number *yourself*, without copying the stated result, and
then compare. Report the value you obtain to full stated precision. A discrepancy is a finding; a
match corroborates arithmetic fidelity only — it says nothing about §6.

## 8. WHAT COUNTS AS A FINDING

- **Fatal:** a located step that is unjustified, circular, or fit-to-target such that the number is not
  actually forced.
- **Material:** an authored choice presented as forced, or a critical-path claim with no discharged
  support, even if the number happens to be unaffected.
- **Minor:** an arithmetic slip, an ambiguous citation, a presentation gap that does not touch the
  forcing.
- **Not a finding:** disagreement with the framing, aesthetic objection, or "I would have done it
  differently" absent a located defect.

## 9. REQUIRED OUTPUT FORMAT

```
OVERALL:  SOUND  |  FLAWED (defects below)  |  UNDETERMINED (state exactly what blocked you)
PASS A — per surface (1..7): RULING [pass / defect] + location + one-line reason
PASS B: value I independently obtained = <...>; matches stated? [yes/no]; deltas if any
STRONGEST ATTACK I MOUNTED: <describe the single best refutation you attempted and whether it succeeded>
DEFECT LIST: each = {severity, file, span, why, what a sound version would need}
CONFIDENCE: <your calibrated confidence that the forcing claim in §3 holds, with the one thing that
             would most change it>
```

## 10. CLOSING

The strongest thing you can do for this program is break it at a specific line. If you cannot, say so
plainly and name the surface you most expect a future reviewer to break. Do not soften either verdict
to be agreeable — a false "sound" and a false "flawed" are equally useless. You were chosen because
you are not us.
