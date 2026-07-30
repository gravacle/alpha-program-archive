# THE `D >= 5` TEST IS DEGENERATE ON THE ONE COMPARATOR THAT SURVIVES

Reviewer lane, 2026-07-30. Finding on lane 2's comparator preregistration
(`STAGE8_SLOT18_COMPARATOR_PREREGISTRATION_V001.md`, 478 lines). Lane 2's work is sound; this is a
consequence it did not draw. No value computed.

## 1. THE SITUATION

Lane 2 established, per family, that **five of six theory-output families have no published same-alpha
comparator payload at all**, and recorded `formula_available_families = 1`. The survivor is family 6, the
charged magnetic form factor — specifically **the electron zero-momentum magnetic anomaly**, with a
fixed-vintage CODATA formula payload, compatibility unresolved until BID derives that same observable.

The distinctness statistic, `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:2052-2058`:

```
D = |mu_BID - mu_comp| / sqrt(sigma_BID^2 + sigma_comp^2 + sigma_meas^2)
```

with "an empty eligible set fails closed."

## 2. THE FINDING

*** ON THE ELECTRON MAGNETIC ANOMALY, `D >= 5` IS PASSED BY A REFUTED THEORY AND FAILED BY A CORRECT
ONE. ***

The electron anomaly is the most precisely known quantity in physics: the QED prediction and the
measurement agree to roughly ten significant figures. So in the denominator, **`sigma_comp` and
`sigma_meas` are both extraordinarily small.**

Two consequences, and they point the same way:

**(a) `D >= 5` IS TRIVIAL TO ACHIEVE HERE AND THEREFORE DISCRIMINATES NOTHING.** With a denominator that
small, any BID prediction differing from the QED value by more than a whisker yields `D` enormously
greater than 5. The threshold was presumably chosen to mean "a substantial, hard-to-fake difference." On
this observable it means "differs at all."

**(b) ANY DIFFERENCE LARGE ENOUGH TO PASS IS ALREADY EXCLUDED BY MEASUREMENT.** Because QED's prediction
already matches experiment to ten digits, a BID prediction that differs from QED enough to give `D >= 5`
is, with near-certainty, in contradiction with the existing measurement. **Passing the test on this family
would be evidence that BID is wrong, not that it is distinctive.**

So the one family with an available comparator is the one where the test inverts: **a correct theory
fails it and an incorrect theory passes it.**

## 3. THE ESCAPE, AND WHY IT DOES NOT RESCUE THE SITUATION

`sigma_BID` is also in the denominator and is currently unknown. If BID's own prediction carried a large
honest theoretical uncertainty, `D` would be small and the spurious pass would not occur.

But that escape cuts the other way: **a theory whose prediction is too uncertain to conflict with QED is
also too uncertain to make the distinctive claim FINAL-CLAIM requires.** Either `sigma_BID` is small — and
then (a) and (b) bite — or it is large, and `D >= 5` cannot be reached at all. Neither branch produces the
intended result.

## 4. WHAT THIS IMPLIES FOR THE CANDIDATE UNIVERSE

**A32's discriminating power requires an observable where BID and standard theory can honestly differ
WITHOUT contradicting an existing measurement.** That means, roughly: structure-sensitive, and either not
yet precisely measured, or measured in a regime the comparator does not cover, or carrying a comparator
uncertainty large enough that a real difference is meaningful rather than fatal.

**AS FAR AS THE SEALED TEXT SHOWS, THAT CRITERION IS NOWHERE STATED.** The 355-candidate universe was
collected under a selection rule that — on the evidence recorded so far — does not include it. The
criterion is not "is a comparator available" (lane 2 has now answered that: once). It is "is a `D >= 5`
difference on this observable *both achievable and survivable*."

That is a third admissibility condition, alongside `structure-sensitive` (defined) and `unused`
(undefined, Q-23). **It is currently satisfied by zero of the six families**, and the one family with a
comparator is the clearest failure of it.

## 5. WHAT I AM NOT CLAIMING

- **Not** that A32 is broken. It is a well-built protocol; this is a property of the candidate SPACE, not
  of the machinery.
- **Not** that BID predicts anything about the electron anomaly. It does not yet, which is precisely why
  lane 2 recorded compatibility as unresolved.
- **Not** a numerical claim of any kind. I have computed nothing, and the argument uses only the
  well-known ORDER of the electron-anomaly agreement, not any value.
- **Not** that the eligible set is provably empty. It is empty of families satisfying all three
  conditions today, which is a different and weaker statement.

## 6. WHAT FOLLOWS

**FOR THE PRINCIPAL, and it belongs with Q-23's `unused` decision rather than after it:** the
admissibility conditions for slot 18 need a third clause. Defining `unused` while leaving this unstated
would produce a well-defined predicate over a candidate space in which the test cannot do its job.

**FOR THE LANE:** nothing until that is ruled. Freezing more comparator payloads for families that cannot
support a meaningful `D` would be work that reads as progress.

**AND ONE THING WORTH SAYING PLAINLY:** the terminal claim rests on finding an observable where this
theory differs measurably from standard physics and is not thereby refuted. That is a genuinely narrow
target, and the program has not yet stated the criterion that identifies it. Better to know now than
after a prediction is frozen.

`alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`.
