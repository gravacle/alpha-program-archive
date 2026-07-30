# A THIRD CANDIDATE FOR THE CONJUGATE ENERGY: THE DIAMOND'S MODULAR HAMILTONIAN

Reviewer lane, 2026-07-30. **PROPOSAL, NOT A DERIVATION.** Tagged PART-PROVABLE. No value computed, no
comparison to any measured constant, nothing adopted.

## 1. THE GAP, AND WHY THE EXISTING DICHOTOMY IS THE WRONG SHAPE

`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:52-79` weighs exactly two candidates for the energy
conjugate to the tip-to-tip proper interval, and rejects both **for the same reason**:

> "These are both standard, geometrically meaningful energies, but they are conjugate to different
> boundary/time choices. The present causal diamond is declared to be **the support of a CTP history
> difference, not a material timelike boundary.** Therefore neither finite-boundary Brown-York energy nor
> asymptotic ADM/Misner-Sharp energy is automatically the Hamiltonian conjugate to the local tip-to-tip
> proper interval."

Misner-Sharp and Brown-York are both **boundary** energies. The rejection is correct and it generalizes:
*no* quasilocal boundary energy can be the right object for a region that has no material boundary. The
`sqrt(2)` is not a fork between two candidates — it is the residue of asking a boundary construction to
do a job that is not about a boundary.

**THE CLASS OF OBJECT DEFINED FOR A REGION WITHOUT A BOUNDARY WAS NEVER CONSIDERED.**

**BOUNDED NEGATIVE.** Roots: `Documents/New project/gravity_emergence_evidence_program`,
`MB Work/alpha_supervision`. Types md/json/py. Exclusions `node_modules`, `external/`,
`custodian_private`. Case-insensitive. File counts:

```
modular Hamiltonian 0 · modular flow 0 · modular automorphism 0 · conformal Killing 0
double cone 0 · Hislop 0 · Casini 0 · Bisognano 0 · Wichmann 0 · entanglement Hamiltonian 0
Tomita 2 · Unruh 1
```

**Modular theory is absent from this program.** The two `Tomita` hits are incidental to GNS material.

## 2. THE CANDIDATE

**The energy conjugate to a causal diamond is the diamond's MODULAR HAMILTONIAN `K` — the generator of
the modular automorphism group of the diamond's local algebra in the given state (Tomita-Takesaki).**

Why it is the correctly typed object, point by point against the gate's own objection:
- It is constructed from **(region, state)**. It needs no material boundary, no boundary conditions, and
  no reference spacetime to subtract against. "The support of a CTP history difference" is precisely a
  (region, state) datum.
- It is **the** generator canonically associated with a region in algebraic QFT. There is no competing
  member of its class to choose between, which is what removes the `sqrt(2)`-type freedom rather than
  relocating it.

**AND IT IS NOT A FREE CHOICE — TWO THEOREMS DO THE WORK.**

**(a) GEOMETRIC MODULAR FLOW (Hislop-Longo).** For a free massless field, the modular automorphism of a
double cone is **geometric**: it is the flow of the conformal Killing vector that preserves the diamond,
with the two tips as fixed points. The flow is not chosen; it is determined by the region and the vacuum.
For a diamond of radius `R` the conformal Killing field has the standard form

```
xi = [ (R^2 - t^2 - r^2) / (2R) ] d/dt  -  (t r / R) d/dr
```

which vanishes on the null boundary and at both tips.

**(b) FIXED NORMALIZATION (KMS).** The modular flow satisfies the KMS condition with a fixed periodicity
in the modular parameter. The scale of `K` is therefore set by the modular condition, not by a subtraction
convention or a reference energy. **This is what a "no free normalization" energy looks like.**

**THE CONVERSION TO PROPER TIME IS EXACT, NOT ADOPTED.** On the diamond's central worldline, integrating
`xi` gives `tau(s) = R tanh(s/2)` for modular parameter `s`, mapping `s` over the whole real line onto the
central proper-time interval `(-R, +R)` — i.e. onto the tip-to-tip interval. **So modular time and proper
time are related by a derived function**, not by a factor someone picks.

## 3. THE GATE'S FIVE CONDITIONS, HONESTLY SCORED

The gate at `:33-48` requires all five. This candidate does not pass all five, and pretending otherwise
would be the failure mode this program is built to avoid.

| # | Condition | Status under this candidate |
|---|---|---|
| 1 | the HJ energy is constant on the stationary record trajectory | **PLAUSIBLY YES, structurally.** `K` generates its own flow, so it is conserved along it. Needs the record trajectory identified with the modular flow. |
| 2 | the CTP branch-energy difference equals the complete gravitating cell energy after one fixed reference subtraction | **THE HARD ONE, AND THERE IS A CANDIDATE BRIDGE.** Jacobson's causal-diamond first law relates a diamond's area variation to `delta <K>`. That is a gravity-to-modular-energy bridge of exactly the required type. NOT verified here, and not in this corpus. |
| 3 | no spectator/vacuum/binding/edge/environment energy contributes without entering the record action difference | **PARTIALLY ADDRESSED BY CONSTRUCTION.** Using relative entropy (state vs vacuum) rather than bare `<K>` makes the vacuum subtraction intrinsic instead of chosen. Spectators still need an argument. |
| 4 | the time parameter conjugate to that energy is the tip-to-tip proper interval `T_R` | **NO, NOT NAIVELY.** The conjugate parameter is the MODULAR parameter `s`, not proper time. **But the relation `tau = R tanh(s/2)` is exact and derived**, so this is a known conversion rather than an ambiguity — strictly better than a `sqrt(2)` with no derivation. |
| 5 | the energy is the one used by the chosen gravitational closure condition | **UNKNOWN.** Requires the closure condition restated in modular terms. |

**SO: 1 plausible, 2 has a named candidate bridge, 3 partial, 4 fails naively but with an exact
conversion, 5 open.** That is not a discharge of slot 1. It is a differently-shaped and, I think, better
target than choosing between two boundary energies.

## 4. WHAT WOULD CHANGE IF IT HOLDS

**The corpus wants `|Delta S_record| = E_R T_R`.** Modular theory says the exact relation available for a
region is the **entanglement first law**, `delta S = delta <K>` — an identity, not an adopted product
rule. If the record's action difference is the modular object, then the relation the corpus is trying to
assert becomes a theorem rather than a premise, and `T_R` enters through the derived
modular-to-proper-time conversion rather than through a chosen energy.

That would also give slot 1 a route that does not pass through the `sqrt(2)`: the ambiguity disappears
because both of its horns are ruled out by type, not adjudicated between.

## 5. THE LIMITS, STATED BEFORE ANYONE GETS EXCITED

1. **GEOMETRIC MODULAR FLOW IS A FREE / CONFORMAL RESULT.** For interacting fields the modular flow is
   not geometric in general. The corpus's carrier is a unit-character massless charged Dirac line and its
   sealed in-state is stationary quasifree — which **may** put it exactly in the applicable class. **That
   must be checked against the sealed state, not assumed.** If the applicable stage is the interacting
   sector, this candidate does not reach it.
2. **THE GRAVITY BRIDGE IS NOT IN THIS CORPUS** and is cited here from outside it. Importing it is a
   principal-level act, not a lane act, and it must clear the same fences as any external premise.
3. **A CONFORMAL KILLING FLOW IS NOT A KILLING FLOW.** The diamond's flow is conformal; whether the
   record construction tolerates conformal rather than isometric time is an open question this proposal
   does not settle.
4. **FORBIDDEN AND DELIBERATELY NOT PURSUED:** the modular periodicity is `2 pi` and the corpus's action
   marker is `|Delta S_record| = pi hbar`. **I am not pursuing that coincidence and it must not be used
   as evidence for anything.** Selection by numerical resemblance is the numerology fence; if this
   candidate is right, the relation will come out of the construction or not at all.

## 6. WHAT I RECOMMEND, AND WHAT I DO NOT

**RECOMMEND:** treat this as a specified TARGET for Section 2.2 of the `Gamma_K` spec, which currently
says the required conjugate energy "does not exist yet" and declines to choose between two boundary
energies. It is better to name a candidate class with two theorems behind it than to leave the slot
empty — provided it is entered as a target with limits 1-4 attached, and provided limit 1 is checked
against the sealed in-state before any construction leans on it.

**DO NOT RECOMMEND:** adopting it, treating it as discharging slot 1, or importing the gravity bridge
without a principal act. And do not let it displace the `Gamma_K` construction — this bears on Section 2,
not on the eleven missing pieces of Section 1.

`alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`.
