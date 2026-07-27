# Is the Post-IBP Scalar Weight Determined? — Determination V001

Date: 2026-07-27

## Status — the answer

```text
**NO. AND THE REASON IS SHARPER THAN "THE CHOICES ARE FREE":
THE INTEGRATION BY PARTS CANNOT BE PERFORMED, BECAUSE THE CORPUS NEVER WRITES THE INTEGRAND.**

The chartered move — perform a SEALED OPERATION on SEALED INPUTS and report what falls out — is
unavailable here. THE OPERATION IS SEALED (one clause). THE INPUTS ARE NOT. Zero of seven are.
    determined_status = INPUTS_THEMSELVES_UNSEALED
Step 1's own gate fires: "if any input is itself unsealed, that is the answer."

*** I DID NOT PICK A CONVENTION. I DID NOT WRITE AN INTEGRAND. I DID NOT BOUND THE WEIGHT. ***
Writing the post-IBP weight would be A SPEC ACT — seven constructions wearing one derivation's
name — and it is the principal's.
AND THE COLLAR IDENTIFICATION DOES NOT HOLD: two gaps, not one. §4.
PRODUCTION PROHIBITED. alpha_computed = false. proof_authorized = false.
```

## 1. THE OBJECT, NAMED — and that is all that is chartered

```text
U1's OBJECT IS: THE POST-INTEGRATION-BY-PARTS LIGHT-CONE SCALAR WEIGHT — the scalar function onto
which the delta' of the light-cone kernel is transferred, and whose W^{1,1}/BV norm controls the
resulting pairing.
THAT IS A NAME. THE CORPUS SUPPLIES NO FORMULA FOR IT, AND NEITHER DO I.

WHAT *IS* DETERMINED, and reporting it is derivation: for int delta'(u) f(u) du with vanishing
boundary terms, moving the derivative off the delta is the only available direction. So the
STRUCTURAL result is forced — THE FIRST DERIVATIVE OF THE PROFILE, EVALUATED ON THE LIGHT CONE.
That is the shape. It is not the object, because f is not named.
```

## 2. ZERO OF SEVEN INPUTS ARE SEALED

```text
(1) THE KERNEL. "~ gamma.partial [delta(t-r)/(4 pi r)]" is TILDE-APPROXIMATE, PARENTHETICAL, and
    occurs ONCE corpus-wide. "delta(t-r)" = 1 hit. "Pauli-Jordan" = 0. "Green" = 0. The one sealed
    propagator artifact is MOMENTUM-SPACE, ONE-MOMENTUM, MASSIVE, with no position-space kernel and
    no light cone — A DIFFERENT OBJECT.
(2) THE DIFFERENTIATION VARIABLE. "delta'" occurs EXACTLY ONCE, WITH NO ARGUMENT WRITTEN. "null
    variable" = 0, "null coordinate" = 0, "retarded time" = 0. t, r, and u = t - r give three
    different transfers, and on delta(t-r) the t- and r-derivatives are interchangeable up to sign.
(3) *** THE CRUX — "THE SMOOTH CELL PROFILES" HAS NO SEALED REFERENT. *** Two occurrences: the
    passage and one paraphrase. NO ARTIFACT DEFINES IT, and the word is PLURAL and never expanded.
    The corpus's cell-side objects are THREE AND DIFFERENT:
      b_D = exp(16 - 1/s)   SMOOTH (Gevrey) — but it is the SOURCE INSERTION, and raw b_D is OUT
      v(t) = (pi/sqrt2) 32 r(t)^3   the ONLY object the corpus calls a TIME PROFILE — U1's own
            word — but it is the ER envelope on the RECORD term, and it is OUT
      M(t) = Q 1_{|x|<=r(t)} Q   POSTULATED SHARP by D6', NOT A SMOOTH PROFILE AT ALL
    WITH v(t) AND RAW b_D BOTH OUT AND M(t) SHARP BY POSTULATE, THE IBP HAS NO NAMED INPUT TO LAND
    ON. THE WEIGHT CANNOT BE READ OFF.
(4) THE DOMAIN. "spatial collar" = 0, "collar integration" = 0, "collar width" = 0. The collar is
    realized ONLY as a BINARY SWITCH between two exact Chebyshev counts — "no third numerator and
    no integral over a profile anywhere". THERE IS NO DOMAIN OVER WHICH TO INTEGRATE BY PARTS.
(5) DYSON BACKGROUND FACTORS. "free propagation between cells" occurs twice and is NEVER GIVEN A
    KERNEL. Whether U_0^* ... U_0 sits inside the weight or outside it is a CHOICE, and the two give
    different W^{1,1} objects.
(6) Q-TYPING. (ii) DOES NOT INHERIT (i)'s SCOPING. "unprojected" occurs ONCE in this sense, in (i)
    only; (ii) says "The free Dirac propagator" and says nothing about projection. Meanwhile the
    sealed dynamics ARE Galerkin-projected — "even the FREE term is h_(0,n,ell), Galerkin-projected"
    — and the sealed target is the Q-carrying Dyson-dressed cross term. CHOOSING UNPROJECTED VERSUS
    Q-COMPRESSED IS ITSELF A FREE CHOICE, AND IT CHANGES THE WEIGHT.
(7) THE NORM. The corpus writes "W^{1,1} / BV" WITH A SLASH, three times, all three verbatim
    carries of the same clause, AND NEVER PICKS.

DECISIVE CORROBORATION: "integration by parts" = 1 HIT CORPUS-WIDE — the passage itself.
"integrate by parts" = 0. "post-IBP" = 0. IN CODE: Huygens, light-cone, collar, by parts,
"delta(t", W^{1,1}, BV norm ALL RETURN ZERO across every .py and .json.
*** THE INTEGRATION BY PARTS IS ASSERTED ONCE AND HAS NEVER BEEN PERFORMED, IN TEXT OR IN CODE,
ANYWHERE IN THIS CORPUS. ***
```

## 3. THE PARTIAL-PINNING TABLE — 0 fully fixed, 2 partial, 6 open

```text
null variable                   OPEN
domain                          OPEN
spatial-collar integration      OPEN — absent as a NOTION, not merely unspecified
Dyson background factors        OPEN
Q-typing                        OPEN
the 1/(4 pi r) grouping         OPEN — the derivative is displayed on the WHOLE bracket, and the
                                text says only that "the delta' terms" integrate by parts. Whether
                                1/(4 pi r) travels with the profile or stays outside changes the
                                resulting scalar, and no sealed text fixes it.
the profile's identity          OPEN — §2(3), the crux
the boundary-term cutoff        PARTIAL — pinned by UNIQUE DESCRIPTION, never by citation. "all
                                orders" returns 3 hits, ALL b_D. Exactly one sealed object satisfies
                                the description — but ARM2 does not name it, writes it PLURAL, and
                                uses a different noun phrase one clause earlier. THE DESCRIPTION HAS
                                A UNIQUE SATISFIER; THE IDENTIFICATION IS UNMADE.
"the integration is temporal"   PARTIAL — and I record a correction against my own first reading:
                                the corpus fixes that the integration whose completion yields R^-1
                                is TEMPORAL; it never fixes the variable the delta' is
                                DIFFERENTIATED in. One notch weaker than "FIXED".
AN IBP WITH SIX FREE INPUTS IS NOT AN OPERATION. IT IS A DESIGN SPACE.
```

## 4. THE COLLAR IDENTIFICATION DOES NOT HOLD — two gaps, not one

```text
THE HYPOTHESIS WAS THAT ONE MISSING SPECIFICATION BLOCKS BOTH. IT IS NOT ESTABLISHED.
 - The collar needs an object whose SUPPORT reduces the shell count R^3 -> R^2.
 - U1 needs an object whose W^{1,1}/BV NORM controls the delta' pairing.
   A SUPPORT property and a NORM property are different properties. They MAY be properties of the
   same object — but the corpus never says so.
 - THE CORPUS NAMES ONE *SUPPLIER* FOR TWO FACTORS ("The free/Dyson propagation bridge must supply
   BOTH") AND NEVER ONE *OBJECT*. And that sentence is a REQUIREMENT — "must supply".
 - IT HAS THE VOCABULARY FOR SUCH AN IDENTIFICATION AND APPLIES IT ELSEWHERE — "A-L2 and A-L0's
   factor (i) are the same physics seen from two sides" — AND EVEN THERE FORBIDS CROSS-DISCHARGE.
   It never applies it between the collar's object and U1's.
 - AND THE COLLAR DETERMINATION ALREADY DECLARED ITS OWN TWO CANDIDATES DIFFERENT OBJECTS.
*** AN UNIDENTIFIED OBJECT CANNOT BE IDENTIFIED WITH AN UNDEFINED ONE. *** Status: UNDETERMINED.
The adjacency of factors (i) and (ii) in the same six-line passage is SUGGESTIVE AND IS NOT PROOF;
this lane has been corrected twice today for reading adjacency as identity, and does not do so here.
```

## 5. THE alpha-PATH CLAIM — the quote holds; the conclusion does not follow

```text
VERIFIED VERBATIM AT SOURCE, seal recomputed and matching: "R-L2b serves the linked-cluster density.
THEREFORE R-L2b IS A Z_K-SIDE OBLIGATION, DOWNSTREAM OF THE A2 STATE EVALUATION."
*** BUT THAT SENTENCE IS ABOUT R-L2b, AND U1 IS A COMPONENT OF A-L0 ARM 2, NOT OF R-L2b. ***
The corpus holds them apart in terms: "A-L0 ARM 2 AND R-L2b ARE LARGELY INDEPENDENT ... R-L2b
controls scaling in CELL SIZE ... A-L0 ARM 2 controls decay in INTER-CELL SEPARATION ... DIFFERENT
VARIABLES: |C|_4 versus R. A bound in one does not supply a bound in the other."
A PARALLEL ROUTE TO THE SAME CONCLUSION EXISTS — arm 2 also serves the connected linked-cluster
density — AND NO SEALED ARTIFACT WALKS IT.
AND THE RATIFICATION EXPRESSLY FENCES THE MOVE: "THIS DECOUPLING IS A CONSEQUENCE OF THE RULING AND
IS EXPRESSLY NOT A GROUND FOR IT ... THIS DISCLOSURE EXISTS SO THAT NO LATER LANE CAN READ THE
CONVENIENCE AS THE REASON." USING IT NOW TO LIFT U1 OFF STAGE 8's BRANCH IS EXACTLY THE MISREAD THAT
SENTENCE WAS WRITTEN TO PREVENT. I DO NOT PERFORM IT. It is the principal's.

AND A SCHEDULING FACT, INDEPENDENT OF WHICH SIDE U1 LANDS ON: Stage 8 cannot return anything but
BLOCKED at present, because A4(5) requires an architecture-aware evaluator successor and authoring
it IS NOT AUTHORIZED. The "only startable item on the board" framing should be checked against that
gate before scheduling weight is placed on U1.
```

## 6. WHAT WOULD UNBLOCK IT — stated as a requirement, not a route

```text
A SEALED SPEC ACT FIXING ALL SEVEN INPUTS, authored as its own obligation with its own hostile
review, BEFORE U1 CAN EVEN BE POSED — let alone certified.
By the corpus's own sealed standard: "DERIVED means the principles REQUIRE it; anything they merely
ALLOW is a premise, however well-motivated." Anything produced by filling the open slots IS A
PREMISE. THAT IS WHY THIS IS THE PRINCIPAL'S AND NOT A LANE'S.
NOT ATTEMPTED. NOT SCOPED. NOT DESIGNED.
```

## 7. INVENTION CHECK

```text
NO INTEGRAND WAS WRITTEN. NO IBP WAS PERFORMED. NO VARIABLE, GROUPING, DOMAIN, PROFILE, DYSON
CONVENTION OR Q-TYPING WAS CHOSEN. NO NORM, CONSTANT, EXPONENT OR INEQUALITY IS ASSERTED OF THE
POST-IBP WEIGHT ANYWHERE IN THIS ARTIFACT.
THE THREE CANDIDATE PROFILES ARE REPORTED WITH THEIR DISQUALIFICATIONS AND NONE IS ADOPTED.
ONE CORRECTION TO A NEGATIVE, RECORDED BECAUSE IT CUTS AGAINST MY OWN PHRASING: a sealed
formula-bearing per-cell smooth profile DOES exist — "every Duhamel insertion therefore carries the
in-cell profile b_D^(c)" — so "no formula, ever" is true of the PHRASE searched and MISLEADING of
the OBJECT. It does not supply arm 2's referent: ARM2 never cites it, it lives on the |C|_4 variable
rather than R, and raw b_D is out. NAMED, NOT ADOPTED.
```

## Protected status

```text
determined_status = INPUTS_THEMSELVES_UNSEALED
inputs_sealed = 0 of 7 ; fully_fixed = 0 ; partial = 2 ; open = 6
IBP_performed_anywhere_in_corpus = FALSE ("integration by parts" = 1 hit, the assertion itself;
  zero in all .py and .json)
smooth_cell_profiles_referent = ABSENT (2 occurrences, no definition; three candidate objects, all
  disqualified: b_D out, v(t) out, M(t) sharp by postulate)
U1_object_named = the post-IBP light-cone scalar weight ; U1_object_written = FALSE
weight_bounded = FALSE ; certificate_attempted = FALSE
collar_identification = UNDETERMINED — a SUPPORT property and a NORM property; one SUPPLIER named
  for two factors, never one OBJECT; adjacency is not identity
alpha_path_claim = QUOTE HOLDS, CONCLUSION DOES NOT FOLLOW (it is about R-L2b; U1 is arm 2, and the
  corpus holds them independent on different variables). The transfer is the principal's.
ratification_decoupling_used_as_a_ground = FALSE — expressly fenced, and the fence honoured
stage8_can_return_non_BLOCKED = false (A4(5); successor unauthorized) — independent of U1
own_correction = "the integration is temporal" is one notch weaker than FIXED
constructed_anything = NONE ; convention_chosen = NONE ; spec_act_performed = NONE
production_authorized = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
