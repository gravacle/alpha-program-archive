COLD_CONFIRM_HEADER_BEGIN

```text
CODENAME              = OPUS-COLD-CONFIRM
MODE                  = BLIND, COLD independent re-derivation
TARGET_SEEN           = NO. The other party's answer was never shown and is not guessed.
QUESTION              = At the bare record (connection-only, phase-rich/amplitude-poor,
                        natively dimensionless, no scale), does the surface DETERMINE its own
                        native dimensionless interaction-strength invariant as a fixed pure
                        number, or leave it a FREE dimensionless parameter?
DERIVATION_BASIS      = BEDROCK ONLY.
TYPING_ONLY           = TRUE. No coupling/kappa/alpha value is computed. All statements are
                        structural/typing statements. |n|=1 below is a QUANTIZATION-UNIT typing
                        (the generator of a discrete character group), not a value of alpha.
SCALE_ASSUMED         = NONE. The coupling is NOT routed through any scale; per the question,
                        there is no scale at this level and none is invoked.
EXCLUDED_NAMES        = not read: any file with ALPHA_DETERMINATION / ETHER / COUPLING_ASSEMBLY
                        in the name (this artifact's own output name is assigned, not a source);
                        register / tracker / plan / road / ledger were not read as authorities.
MACHINERY_FENCE       = I did NOT invoke: Lambda^even(C^5), K_KK, the fiber radius, the metric,
                        ell_P, Thomson matching, the KK action, any scale-bearing coupling
                        formula, "alpha rides a scale," or the Finish-A/B frame.
BLIND_HELD            = every scale/interval/modulus/coupling is a SUBJECT; none is evaluated.
alpha_computed = false ; kappa_record_computed = false ; proof_authorized = false
```

COLD_CONFIRM_HEADER_END

# STAGE 8 — COLD RE-DERIVATION: DOES THE BARE RECORD FIX ITS OWN NATIVE COUPLING?

## 0. What "the surface's own interaction-strength invariant" must mean here

The question fixes the object precisely: the surface's **own measure of how strongly it
responds to a source**, expressed as a dimensionless invariant, at the bare record — where the
record is connection-only, phase-rich / amplitude-poor, natively dimensionless, and carries no
scale. I take that literally and refuse to import the continuum coupling of gauge theory
(`e^2/4pi hbar c`), which is a metric-and-amplitude object and is fenced off. I ask instead:
**inside the bare structure itself, is there a dimensionless number that measures response
strength, and does the structure fix it or leave a continuous freedom?**

## 1. Bedrock inputs actually used (paths, hashes where pinned)

```text
B1  workspace/STAGE8_SADDLE_FOUNDATION_PARENT_ACTION_DARIO_V001.md
    sha256 1d11f15040f8b85b7e081fccfeddb995c41941c55464d759a2fa91a8feffc775  (verified at path)
    -> the record's OWN interacting object is indexed by the CONNECTION ALONE; no metric
       argument anywhere; the influence action is minus-i-log of an object the record ratifies.

B2  workspace/STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md
    -> the exact record-native interacting object:
         z_j := chi_n(h_j[a]) ,  |z_j| = 1        (unit-modulus holonomy character)
         Z_N[a_+,a_-] := product_j conjugate(z_(-,j)) z_(+,j)
         F_N = P_0 + Z_N P_ch
       The record responds to a source ONLY through Z_N, and |Z_N| = 1 EXACTLY.
       n in {+1,-1} are the FAITHFUL character orientations.

B3  workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_U1_DOR008_ASSEMBLY_DETERMINATION_V001.md
    -> the characters are unit modulus with U_lambda^* = U_(-lambda); the label inverts under
       star; the response enters with a fixed 1/2 and NO free normalization ("no compensating
       normalization"; "no free normalization remains").

B4  workspace/STAGE8_LOAD_BEARING_HOLONOMY_DERIVABILITY_DETERMINATION_V001.md
    -> the comparison group U(1)_rel = Stab(P_0,P_1)/U(1)_diag is DERIVED, compact, one
       generator (quoting PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md:49-61);
    -> the primitive unit character fixes Hol_gamma(a) = exp(i integral_gamma a) and
       "No additional charge-normalization factor may be inserted later"
       (quoting FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md:47-68);
    -> "a faithful character has |n|=1, and unit winding follows from the derived stabilizer,
       continuity, one-dimensional action, faithfulness after the response-null quotient, and
       orientation" (quoting STAGE1_PREMISE_DISPOSITION_V001.md:29-47);
    -> HONEST BOUNDARY: the file flags that the PHYSICAL LOCALIZATION and the identification of
       this normalization with the electromagnetic coupling ("on which alpha directly depends")
       are ADOPTED/IMPORTED at the least-favorable head. See section 5 — that boundary is about
       the scale-riding PROMOTION, which the question fences off.

B5  supervision/DECISION_OF_RECORD_009_THE_TRANSITION_LAW_RATIFIED_E_POST_2026-08-02_V001.md
    -> ratifies the transition law whose finite influence functional B2 instantiates.
```

## 2. The derivation, from the bare structure

### 2.1 The response is a PURE PHASE, so no continuous coupling has a carrier

The record's entire response to a source is `Z_N = product_j conjugate(z_(-,j)) z_(+,j)`, a
product of unit-modulus characters, so `|Z_N| = 1` exactly (B2). This is the content of
"amplitude-poor": the surface carries no amplitude. A coupling constant in the ordinary sense
is precisely a modulator of an **amplitude** (a probability weight, a cross-section, a kinetic
normalization). At the bare record there is **no amplitude to modulate** — every response sits
on the unit circle. Therefore the usual continuous, dial-able dimensionless coupling has **no
carrier at all** at this level. It is not "free here"; it is **absent** here, and it is absent
because the object it would scale (an amplitude, equivalently `integral F wedge *F`, which needs
the Hodge star = a metric) is exactly the metric-bearing machinery the bare record does not
carry (B1: no metric argument anywhere).

So the only place a "how strongly it responds" invariant can live is **in the phase itself** —
in the exponent of the character.

### 2.2 The invariant is the holonomy-character winding / charge

Write the primitive holonomy as `Hol_gamma(a) = exp(i integral_gamma a)` and the record's
character as `chi_n(Hol) = Hol^n = exp(i n integral_gamma a)` (B4, B2). The rate at which the
record's phase advances per unit of source holonomy is the exponent coefficient `n`. That
coefficient IS "how strongly the surface responds to a source": it is the surface's own,
dimensionless, scale-free interaction-strength invariant. Call it the **winding / charge of the
faithful holonomy character**. Nothing else in `Z_N` measures response strength: `a` is the
source input (a subject), the branch pair is bookkeeping, and the `1/2`/orientation data carry
no free normalization (B3).

### 2.3 The winding is QUANTIZED — this removes all continuous freedom

The comparison group is `U(1)_rel`, and it is **derived** (record-native) as a compact group
with a single generator (B4, quoting the stabilizer quotient). The characters of a compact
abelian group are its Pontryagin dual, which is **discrete**: they are labeled by integers. A
character must be a single-valued unit-modulus homomorphism of the circle, so `n` must be an
integer — a non-integer exponent is not a function on `U(1)` at all. Hence:

```text
the interaction-strength invariant n is QUANTIZED: n in Z, not n in R.
```

This is the decisive structural fact. **Compactness of the record-derived comparison group
forbids a continuous coupling.** The existence of an integer tower of charge sectors is not a
"free continuous parameter"; it is the very signature of a fixed unit — the same way a tower of
integer quanta is the signature of quantization, i.e. of a fixed unit rather than a continuum.

### 2.4 Faithfulness / distinguishability pins the surface's OWN invariant to the generator

Among the integer tower, which is the surface's **own** invariant? A record is, constitutively,
a thing that **distinguishes** — it registers distinct source holonomies as distinct marks.
"Phase-rich" is exactly the statement that the distinctions live in the phases. A character
that failed to be faithful has a kernel and would collapse distinct holonomies to the same
record mark — it would not record. The response-null quotient (quotient out the directions that
produce no response) makes the operative character faithful by construction. A faithful
character of `U(1)_rel` is a **generator**: `|n| = 1` (B4, stated verbatim in the corpus). The
sign `+/-1` is orientation / charge-conjugation, not a strength. Higher `|n|` are non-primitive
— integer multiples of the generator, i.e. composite charges — not new couplings. The surface's
**own, primitive** interaction-strength invariant is therefore the generator, `|n| = 1`.

And the corpus rule is explicit that this leaves no residual freedom: once the primitive unit
character fixes `Hol = exp(i integral a)`, "**no additional charge-normalization factor may be
inserted later**" (B4). There is no slot for a free multiplier.

### 2.5 Nothing hidden rescales it

Could a rescaling `integral a -> c integral a`, `n -> n/c` smuggle a continuous coupling back in?
No: `U(1)_rel` is a genuine circle with a fixed `2 pi` period (it is a derived group, not a
choice of units), so single-valuedness fixes the normalization and only integer `n` survive.
The "identity-phase family" `chi` that the corpus leaves open (B4) shares the **same** record
projectors — it does not change response strength — so it is a gauge/reference-phase ambiguity,
not an interaction-strength coupling. No continuous strength freedom exists anywhere in the bare
object.

## 3. Steelman of FREE / UNDETERMINED, and why they lose at the bare level

```text
FREE (continuous):   would require a non-compact charge group (dual = R) OR an amplitude for a
                     coupling to scale. The record DERIVES a compact U(1)_rel (dual = Z) and is
                     amplitude-poor (|Z_N|=1). Both carriers of a continuous coupling are absent.
                     -> REJECTED at the bare level.

FREE (discrete tower): "n could be any integer, so the sector is a free choice." But the tower
                     is integer multiples of ONE generator; the surface's OWN (primitive)
                     invariant is the generator, and faithfulness/distinguishability — which is
                     what "record" MEANS — selects it. A quantized tower is determination, not
                     freedom. -> REJECTED as the reading of the surface's own invariant.

UNDETERMINED:        the corpus flags "primitive_unit_winding_imported = true" and that
                     faithfulness/response-null and localization are not independently derived
                     AT THE LEAST-FAVORABLE HEAD. But every one of those flags is about the
                     PHYSICAL LOCALIZATION and the EM identification — the promotion of the bare
                     invariant to a localized, scale-bearing electromagnetic normalization "on
                     which alpha directly depends." That promotion is precisely the scale-riding
                     machinery the question fences off. It does not touch the bare-record
                     invariant, whose quantization (compact derived U(1)_rel) and generator
                     pinning (faithfulness = distinguishability) are available structurally.
                     -> the missing pieces are DOWNSTREAM of the asked object, not inside it.
```

Under no honest reading does the bare surface leave a **free continuous** dimensionless coupling.
The weakest defensible reading still yields a **quantized** invariant with the surface's own value
at the **generator**. That is determination, not freedom.

## 4. Result

The bare record supplies its own interaction-strength invariant intrinsically: it is the
**winding / charge of the faithful, unit-modulus holonomy character** — the coefficient `n` in
`exp(i n integral_gamma a)`, the rate of record-phase response per unit source holonomy. The
surface **fixes** it as a pure number by three facts it itself carries:

1. **Amplitude-poverty** (`|Z_N| = 1`) — there is no amplitude, hence no carrier for a
   continuous coupling; the invariant can only be a phase-winding.
2. **Compactness of the derived comparison group `U(1)_rel`** — quantizes the winding to
   integers; a continuous coupling is structurally forbidden.
3. **Faithfulness / distinguishability** (constitutive of "record"; "phase-rich") — pins the
   surface's own primitive winding to the generator; "no additional charge-normalization factor
   may be inserted later."

## 5. Honest boundary (what this does and does not claim)

```text
CLAIMED: at the BARE record, the surface's own dimensionless interaction-strength invariant is
         DETERMINED — a fixed pure number (the generator of the character group), fixed by
         amplitude-poverty + compact-quantization + faithfulness. No continuous free coupling
         exists at this level; the tower of integer charges is the signature of a fixed unit.

NOT CLAIMED: that the PHYSICAL, localized electromagnetic coupling (the scale-riding object on
         which a measured alpha would depend) is thereby derived. Promoting the bare invariant to
         a localized physical connection carries an adopted/imported unit-winding-normalization
         premise and an underived localization at the least-favorable head (B4). That promotion
         is the metric/scale machinery the question explicitly fences off, so it is OUT OF SCOPE
         for the asked object and does not weaken the bare-level verdict.

NOT DONE: no coupling, kappa, alpha, scale, root, eigenvalue, or measured value was computed or
         compared. |n|=1 is a quantization-unit typing, stated as the corpus states it, not a
         value of alpha.
```

## 6. Custody

```text
Bedrock read at path: B1-B5 above (workspace/ and supervision/). Parent-action hash re-verified.
Not read (kept cold): any ALPHA_DETERMINATION / ETHER / COUPLING_ASSEMBLY-named source; the
   register/tracker/plan/road/ledger as authorities; BID_UNIQUE_CHARGED_CONTROLLED_COUPLING
   content (only its sidecar hash was seen, never its body).
No register, git, commit, push, or registration action was performed.
BUILDER NEVER VERIFIES OWN WORK -> CLAIMED until an opposite-lane check.
```

---

NATIVE_INVARIANT_DERIVED = the winding/charge of the faithful unit-modulus holonomy character — the integer coefficient n in Hol=exp(i n integral_gamma a), i.e. the record's phase-response rate per unit source holonomy (the exponent of chi_n in the influence functional Z_N)
SURFACE_FIXES_IT = DETERMINED (fixed, a pure number: the generator |n|=1, fixed by three facts the surface itself carries — amplitude-poverty |Z_N|=1 leaves no amplitude for any continuous coupling; the record-derived COMPACT comparison group U(1)_rel quantizes the winding to integers, forbidding a continuous parameter; faithfulness/distinguishability, constitutive of "record", pins the primitive winding to the generator and "no additional charge-normalization factor may be inserted later")
MACHINERY_INVOKED = no
