# F-FL1 — WHAT COULD FIX THE SMALL-`s` END: THE CONDITION CLASS EXISTS, IS RANKED, AND IS BLOCKED BY THE STITCHING RULE

Reviewer lane, 2026-07-30. F-FL1 is Q-18's frozen repair condition. Every claim carries file:line.
No value computed. **VERDICT: NOT REFUTED AND NOT AVAILABLE.**

## 1. THE QUESTION, AND WHY THE PHYSICS NARROWS IT IMMEDIATELY

Q-18 established that the proper-time floor cuts the SMALL-`s` end of
`Gamma_BR,k = -(1/2) integral_(1/k_R^2)^(1/k^2) (ds/s) STr'_BR exp(-s L_BR)`, and that a
bottom-of-spectrum condition provably cannot reach it. F-FL1 asks what could.

**SMALL `s` IS CONTROLLED BY THE HIGH END OF THE SPECTRUM AND BY MODE COUNTING.** In
`STr' exp(-s L) = sum_n (+/-) exp(-s lambda_n)`, the `s -> 0` limit is where every mode contributes,
so only three things can act there: the spectrum being bounded ABOVE, cancellation in the graded
mode count, or the measure. That is the complete candidate list, and it is the class Q-18 named.

## 2. THE CANCELLATION CLASS IS DEAD, AND FOR A REASON ALREADY IN THE CORPUS

The tempting mechanism: if the primed supertrace cancels its leading terms — `STr' 1 = 0` and the
next graded coefficients vanishing — the small-`s` end could be finite with no cutoff, and the
surviving coefficient would be calculable. **It fails, and the failure is structural, not
contingent.**

**THE `F^2` DIVERGENCE IS LOGARITHMIC, AND A LOGARITHM CANNOT BE CANCELLED BY MODE COUNTING.** In
four dimensions the `F^2` coefficient comes from the `A_4` heat-kernel coefficient, whose
contribution to `integral ds/s` is precisely `log`. Vanishing lower coefficients remove the power
divergences; they leave the log untouched. And the log's coefficient is the beta function, which
this program has computed and which is NOT zero —
`alpha_step5_zero_bare_compositeness_boundary_v002.md:53`:

```
lim_(Q/m -> infinity) d K_1D/d ln Q = -1/(6 pi^2),
```

So a vanishing `F^2` part of `A_4` would BE superconvergence, and the slot-9 attack already recorded
the incompatibility: "superconvergence and a nonzero beta function are mutually exclusive statements
about the same spectrum." **The cancellation class collapses into E2, which is dead.** It is also
rank 2 of the landscape in §3, independently blocked there.

## 3. THE CONDITION CLASS THAT WOULD WORK EXISTS, IS ALREADY RANKED, AND IS BLOCKED

`alpha_spectral_ncg_absolute_stiffness_research_v001.md:349-366` carries a seven-row ranked
PASS/BLOCK table over exactly this question. **RANK 1 IS THE ANSWER TO F-FL1**, verbatim:

| Rank | Candidate | What passes | Blocking fact | Verdict |
|---|---|---|---|---|
| 1 | "Fully finite **total** record-cell triple plus exact normalized determinant/CTP trace" | "Finite matrix determinant gives an absolute cell Hessian once `D[A]`, state, measure, and unit character are fixed" | "Current carrier is only internally finite; spacetime spectral support, cell density, and CTP construction are missing" | **PASS-CONDITIONAL / BLOCK-CURRENT** |

**On a total finite triple there is no small-`s` divergence to cut. The determinant is absolute, and
no floor is needed at all.** That is the condition F-FL1 asked for, and it is a statement about
ADMISSIBLE MODE CONTENT — the class Q-18 predicted might work.

The other six rows close the space, and each fails differently:
- **Rank 2** — UV-soft nonlocal vertex / superconvergent spectrum: "No such operator, spectrum,
  positivity proof, or no-mutation theorem is currently derived." This is §2's class and E2.
- **Ranks 3 and 4** — zeta spectral action, exact cutoff action with `f(0)=1`: both "add a bare
  action" / "Fixes a bare low-derivative coefficient by axiom", and rank 4 explicitly "violates
  zero-bare route." **They buy the small-`s` end by reintroducing what `K_bare = 0` forbids.**
- **Rank 5** — heat-kernel spectral action plus finite internal triple: "`f(0)` or equivalent common
  normalization is independent" → PASS-RELATIVE / BLOCK-ABSOLUTE. Fixes ratios, not the scale.
- **Rank 6** — exact continuum determinant of the CURRENT carrier: "`A_4` logarithm and finite local
  `F^2` mutation require subtraction/matching" → PASS-RUNNING / BLOCK-ABSOLUTE.
- **Rank 7** — finite triple/topology/unit charge alone: "No principle fixes the metric on gauge-field
  configuration space" → PASS-KINEMATICS / BLOCK-STIFFNESS.

**AND RANK 1'S BLOCKING FACT IS THE STITCHING GAP**, which is not merely open but a SEALED FAILURE
RULE. `ABSOLUTE_STIFFNESS_SELECTOR_ROUTE_LEDGER_V003.md:116-126` — the route fails if "a finite-cell
answer is called physical without a derived stitching or continuum rule." No such rule exists
anywhere in the corpus; that was established by three disjoint search methods on 2026-07-27, and four
sealed objects carrying limit mechanisms all fail by type.

NOT A RECOVERY: the NCG research artifact is cited by five `CURRENT_AUTHORITY_LEDGER` versions and by
six reviewer sweeps. This landscape was known. What was not recorded is that its rank 1 is the answer
to F-FL1 and that its blocking fact is the same object the stitching finding names.

## 4. THE REFRAMING, AND IT IS THE RESULT WORTH KEEPING

*** THE PROPER-TIME FLOOR IS THE PRICE OF AN INCOMPLETE CARRIER. ***

Q-18 established that the floor is the content of the adopted induced-only axiom. F-FL1 sharpens
that: **the axiom is standing in for a finiteness property the carrier does not have.** On a total
finite triple the determinant is absolute and the floor is unnecessary; on a carrier finite only
internally, something must cut the small-`s` end, and the axiom is what does it.

**SO THE FLOOR AND THE STITCHING GAP ARE ONE PROBLEM, NOT TWO.** They have been tracked separately —
the floor as an adopted premise in the induced-only principle, the stitching rule as a missing
continuum object with its own failure rule — and they are the same missing property seen from two
sides. That is the same shape as `beta`: "The free parameter and the missing metric rule are one gap
seen from two sides" (Q-10).

## 5. CONSEQUENCE FOR THE `Gamma_K` CHARTER — STATE THIS BEFORE CONSTRUCTION, NOT AFTER

**`Gamma_K` BUILT ON THE CURRENT CARRIER LANDS AT RANK 6, NOT RANK 1.** Rank 1 requires "spacetime
spectral support, cell density, and CTP construction"; `Gamma_K` supplies the CTP construction and
the measure, and it does NOT supply spacetime finiteness. Rank 6 is the current carrier's row and its
verdict is PASS-RUNNING / BLOCK-ABSOLUTE: "`A_4` logarithm and finite local `F^2` mutation require
subtraction/matching."

Therefore: a completed `Gamma_K` with a unique simple positive `C_record` root would determine `K_*`
**conditionally on the induced-only axiom, not absolutely.** The closure residual is built from an
action carrying the `A_4` log, so `k_R` — the floor — appears in the equation that fixes `K_*`.

This does not weaken the charter and it does not fire F-GK1. It localizes what success delivers, and
it is exactly what F-GK3 exists to force into the open: **the induced-only axiom is a declared
condition of the construction, stated at the outset.** Q-18 already established that alpha's
conditionality equals that axiom's status; §5 says where in the machinery the dependence enters.

**AND IT SAYS WHAT WOULD LIFT IT:** a derived stitching or continuum rule, which would move the
construction from rank 6 to rank 1 and make the coefficient absolute. Nothing else in the ranked
landscape does that without reintroducing a bare action.

## 6. VERDICT

**F-FL1: NOT REFUTED, NOT AVAILABLE.** A condition that fixes the small-`s` end exists in principle
and is identified — rank 1, a total finite triple. It is blocked by the absence of a derived
stitching or continuum rule, whose absence is a sealed failure rule. **It is therefore NOT a fifth
exit for S9-B today**, and it should not be counted as one.

WHAT WOULD CHANGE IT: a derived stitching/continuum rule. That is the single object, and it now has
two independent consumers — the floor (this result) and any finite-cell stiffness route (the 07-27
finding).

WHAT DOES NOT CHANGE IT: any amount of work on the cancellation class (§2 kills it structurally), any
spectral-action variant that reintroduces a bare coefficient (ranks 3-4 violate `K_bare = 0`), or a
better determinant of the current carrier (rank 6 is already PASS-RUNNING / BLOCK-ABSOLUTE).

## 7. SCOPE

- Discharges no slot. Zero of eighteen remain derived.
- Computes nothing: no `alpha`, `kappa`, coupling, radius, scale, root or eigenvalue.
- Refutes no route. Rank 1 is BLOCK-CURRENT, not refuted.
- Does NOT fire F-GK1. Lane 1's scoping returned MISSING SPECIFICATION and that stands.
- Adopts nothing. The reframing in §4 is a typing claim about two existing open objects.

`alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`.
