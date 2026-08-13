# Stage 8 — U(1)_rel Determinacy Check (Blind Independent Verification)
## OPUS-URELCHECK — bedrock/typing only — [CLAIMED until cross-lineage confirmation]

Date: 2026-08-13
Role: BLIND independent verifier. Confirm or refute ONE load-bearing structural
fact at the bytes, cross-lineage to the party that adjudicated it. No value of
n, kappa, alpha, or any constant is computed, bounded, or compared. Every
quantity is symbolic. Faithfulness is NOT used as a premise; it is tracked as a
derived-or-adopted object wherever it appears.

---

## 0. THE FACT UNDER TEST (the crux of the |n|-forced verdict)

A registrar adjudication concluded |n| is forced because: the record's
RESPONSE-NULL quotient removes ONLY the gauge diagonal `U(1)_diag` — NOT the
character kernel `ker(chi_n)` — so the record lands on the FULL determinate
relative-phase group `U(1)_rel = [U(1) x U(1)] / U(1)_diag`, on which
`ker(chi_n) = Z_|n|` is PHYSICAL structure that acts nontrivially on a complete
derived orbit invariant `q_N`, distinguishing |n|.

Three sub-questions, verified independently below at byte spans.

---

## 1. SEALS VERIFIED AT PATH (recomputed sha256)

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`.

| Source | sha256 recomputed at path | Expected | Match |
|---|---|---|---|
| `PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md` | `45f6015c74593fd25f7862aa7bf6407e124f449ff7635dcf2f9d4c2c2303f08f` | `45f6015c...03f08f` | YES |
| `STAGE1_PREMISE_DISPOSITION_V001.md` | `254128f73a44869839d670557368709c1bf2a98d6f86b48f026064c80e8d2585` | `254128f7...8e2585` | YES |
| `STAGE8_BARE_SURFACE_ALPHA_DETERMINATION_FABLE_V001.md` | `82e81f6e659108c05872d30d4c5ad00bf66cad3c272c4aa8240aa89fc5a62010` | `82e81f6e...a62010` | YES |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U3_DOR008_DOR009_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` (U3) | `b0118d89e0b4b321fbf9caab5bfb811a0b5fd572e808d02615ee8503db2bc1ac` | matches its own `.seal.sha256` sidecar | YES |

(STAGE1 recomputed exactly `254128f73a44869839d670557368709c1bf2a98d6f86b48f026064c80e8d2585`,
matching the expected digest byte-for-byte at verification time. U3's digest was
verified against its `.seal.sha256` sidecar because no digest was supplied inline.)

All four seals verify. Bedrock is intact.

---

## 2. QUESTION 1 — IS THE PHYSICAL-NULL QUOTIENT DIAGONAL-ONLY?

`PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md`:

- `:22-29` — `U(1)_diag = {(u,u)}` "changes no projective state or public record
  statistic and is removed by the physical null quotient."
- `:31-42` — "The surviving comparison group is therefore `[U(1) x U(1)] /
  U(1)_diag` isomorphic to `U(1)_rel`, `(u_0,u_1) -> u_1 u_0^(-1)`. The displayed
  map is onto and its kernel is exactly `U(1)_diag`."
- `:54-56` — generator `Q = |1><1| = diag(0,1)`.
- `:68-72`, `:142-144` — characters `chi_n(theta) = exp(i n theta), n in Z`;
  `primitive_character_lattice = Z`.

Cross-lineage corroboration at the chain level, `U3 :221-235`: the trivially-
acting stabilizer is the constant-vertex subgroup `g_0 = ... = g_N`, and
`Q_N := X_N / (G_N / U(1)_diag)` is canonically `U(1)^N`. The removed null
direction is the diagonal only; the full carrier survives.

**FINDING Q1: CONFIRMED.** The physical/response-null (gauge) quotient removes
`U(1)_diag` only; the surviving carrier is the full `U(1)_rel = [U(1) x U(1)] /
U(1)_diag`; generator `Q = |1><1|`; character lattice `Z`. No sealed text in the
read set removes `ker(chi_n)` at the group/carrier level — the surviving group
retains every `Z_|n|` subgroup.

---

## 3. QUESTION 2 — q_N COMPLETE, STABILIZER = DIAGONAL, KERNEL PHYSICAL ON q_N?

`U3` (TYPE-P on premises DoR-008, DoR-009; PARTIAL assembly):

- `:190-219` — orbit map `q_N(z_+,z_-)_j = conjugate(z_(-,j)) z_(+,j)`; explicit
  proof "The invariant is complete."
- `:221-235` — "The stabilizer consists of constant vertex transformations
  `g_0 = ... = g_N`. It acts trivially. After removing this constant null
  direction, the effective action is free."
- `:246-254` — flags: `FINITE_ORBIT_INVARIANT_COMPLETE = true | TYPE-P`;
  `FINITE_CONSTANT_STABILIZER_REMOVED = true | TYPE-P`;
  `FINITE_GAUGE_FIXED_QUOTIENT_Q_N_INSTANTIATED = true | TYPE-P`.

**TYPE-P / PARTIAL status (noted exactly):** the whole U3 assembly is a finite
skeleton, not a full instance. `U3_008_INSTANCE_EXISTS = false | TYPE-U`
(`:43`); `PHYSICAL_VERDICT = NO_VERDICT`, `CONSTRUCTION_VERDICT =
FINITE_U3_SKELETON_ASSEMBLED__FULL_U3_HAS_FIVE_OPEN_FIELDS` (`:70-71`, `:852-853`);
the descended measure, physical contour prescription, complete boundary package,
unbounded endpoint domains, and common-origin trace are all `TYPE-U`.

**FINDING Q2, limb (i) — q_N COMPLETE and trivially-acting stabilizer =
constant-vertex (diagonal) only: CONFIRMED** at `U3 :210-254`, TYPE-P inside a
PARTIAL (TYPE-U at full-instance level) assembly.

**FINDING Q2, limb (ii) — "ker(chi_n) = Z_|n| is PHYSICAL structure acting
nontrivially on q_N, distinguishing |n|": UNVERIFIED at the bytes.** U3 contains
no `chi_n`, no `ker(chi_n)`, no `Z_|n|`, no winding index anywhere — its carrier
is `U(1)^N` with `z` already circle-valued, so no character reduction occurs in
U3. U3's stabilizer statement lives in the vertex GAUGE group `G_N = U(1)^(N+1)`;
`ker(chi_n)` lives in the RELATIVE-PHASE group `U(1)_rel` — a different object U3
never connects to `q_N`. The step "constant-vertex stabilizer is the only
trivial one, THEREFORE `ker(chi_n)` acts nontrivially on `q_N` and forces |n|"
is the crux's inference, not sealed byte-text. (Formally, `Z_|n|` translations do
move `U(1)^N` values — but that is true of any nontrivial subgroup and does not,
by itself, force |n| = 1.)

The only place the winding index is linked to |n| is `FABLE` and `STAGE1`, and
there the linkage is made by FAITHFULNESS, examined next.

---

## 4. QUESTION 3 — THE COUNTER-HYPOTHESIS, TESTED HARD

Counter-hypothesis: the response-null quotient removes `ker(chi_n)`, landing on
`U(1)_rel / Z_|n| ~= U(1)` where `chi_n` is faithful and |n| is INDISTINGUISHABLE
(verdict wrong).

At the GROUP/CARRIER level the counter-hypothesis is refuted: PRIMITIVE `:31-42`
and U3 `:221-235` keep the full `U(1)_rel` / `U(1)^N`; `ker(chi_n)` is not removed
from the carrier.

At the RESPONSE level the picture is different and load-bearing:

- `STAGE1_PREMISE_DISPOSITION_V001.md:35-43` — unit winding "follows from: the
  derived relative U(1) stabilizer; continuity; one-dimensional unitary action;
  **faithfulness after the response-null quotient**; and an orientation
  convention." Faithfulness is listed as an INPUT.
- `FABLE :161-172` — "Faithfulness forces unit winding ... a non-faithful
  response is constant on kernel cosets — precisely those source histories the
  record would fail to record." For |n| > 1 the RESPONSE `chi_n(holonomy)` is
  constant on `ker(chi_n)` cosets, i.e. the response factors through
  `U(1)_rel / ker(chi_n) ~= U(1)` and is faithful there.
- `FABLE :300-307` (flag) — "Faithfulness ... forces unit winding: the lattice
  GENERATOR."
- `PRIMITIVE :74-75` — "The primitive faithful character has |n| = 1 ... |n| > 1
  repeats the primitive winding." |n| = 1 is a faithful/primitive DESIGNATION;
  |n| > 1 is typed as a repeat, not as a physically-distinguished new structure
  the record retains.

So every sealed route to |n| = 1 runs through FAITHFULNESS: the physical
character is required to be injective, and |n| > 1 is rejected because its
response is UNRECORDED on kernel cosets. That is the counter-hypothesis's own
algebra (response faithful on `U(1)_rel / ker(chi_n)`), deployed as a SELECTION
of |n| = 1 — and it is the OPPOSITE of the crux's "the record lands on the full
`U(1)_rel` on which `ker(chi_n)` is PHYSICAL structure." Under the crux's stated
mechanism a |n| = 2 record would resolve `Z_2` cosets; FABLE `:165-168` states it
does not.

**FINDING Q3: COUNTER_HYPOTHESIS_SUPPORTED = NO** for its verdict-flipping
CONCLUSION — no sealed text concludes |n| is indistinguishable; all four files
conclude |n| is forced to unit winding. BUT the counter-hypothesis's response-
level ALGEBRA (`|n| > 1` response constant on `ker(chi_n)` cosets, factoring
through `U(1)_rel / ker(chi_n) ~= U(1)`) IS present in FABLE `:165-168`, and it is
exactly what makes the sealed forcing rest on FAITHFULNESS rather than on the
crux's "kernel physical acting on q_N."

---

## 5. WHY THE CRUX AS STATED CANNOT BE CONFIRMED AT THE BYTES

Two readings of the crux's third limb, both blocking confirmation:

- Strong reading (record itself lands on full `U(1)_rel`, `ker(chi_n)` recorded
  so a |n| > 1 record resolves `Z_|n|`): CONTRADICTED by FABLE `:165-168`
  ("constant on kernel cosets ... the record would fail to record").
- Reconciling reading (it is the CARRIER `q_N` that retains the kernel; a
  response is faithful iff |n| = 1): individually consistent with U3 + FABLE, but
  the step from "carrier retains the kernel" to "|n| = 1 is forced" is exactly
  FAITHFULNESS (select the response that matches the complete carrier). "Kernel
  physical on q_N" alone yields inequivalence of different |n|, not the value
  |n| = 1; a selection principle is still required, and in the bytes it is
  faithfulness.

My fence bars faithfulness as a premise unless derived from bedrock. FABLE's
attempt to derive it ("a record actually recording the connection"; the trivial
character eliminated by charge/flux access, `:165-172`) discharges `n = 0` and
the continuous slot, but its rejection of |n| > 1 is "constant on kernel cosets
= fails to record" — faithfulness restated, not reduced to something more
primitive. So faithfulness is adopted, not bedrock-derived, and it is the sole
sealed lever that reaches |n| = 1.

Consequently the |n|-forcing CONCLUSION is present in the corpus (via
faithfulness) and is NOT refuted; but the crux's stated MECHANISM — |n| forced
because `ker(chi_n)` is physical structure acting nontrivially on `q_N` with the
record on the full `U(1)_rel` — is not established at the bytes and is in tension
with FABLE's response-level typing.

---

## 6. WHAT WOULD CLOSE THE GAP

A bedrock derivation, independent of adopted faithfulness, that (a) the response
/ record itself (not merely the carrier `q_N`) retains `ker(chi_n)` as physical,
recorded structure, and (b) that this retention — not a faithfulness/injectivity
requirement — is what forces |n|. Absent that, U3 must additionally carry
`chi_n` / `ker(chi_n)` and connect the character kernel to `q_N` on one
construction trace. Neither is present in the read set.

---

## 7. FLAGS

```text
SEALS_VERIFIED_AT_PATH                = true (4/4)
QUOTIENT_DIAGONAL_ONLY_AT_CARRIER     = CONFIRMED  (PRIMITIVE:22-42; U3:221-235)
q_N_COMPLETE                          = CONFIRMED  (U3:210-254 | TYPE-P | PARTIAL:
                                        U3_008_INSTANCE_EXISTS=false TYPE-U;
                                        PHYSICAL_VERDICT=NO_VERDICT)
TRIVIAL_STABILIZER_IS_DIAGONAL_ONLY   = CONFIRMED  (U3:221-235)
KERNEL_PHYSICAL_ACTING_ON_q_N         = UNVERIFIED (U3 has no chi_n/ker(chi_n)/
                                        winding; linkage absent at bytes)
FORCING_MECHANISM_IN_SEALED_TEXT      = FAITHFULNESS (STAGE1:41; FABLE:161-172,
                                        300-307), not kernel-on-q_N
COUNTER_HYPOTHESIS_CONCLUSION         = NOT_SUPPORTED (all files force |n|=1)
COUNTER_HYPOTHESIS_ALGEBRA_PRESENT    = YES (FABLE:165-168, response factors
                                        through U(1)_rel/ker(chi_n) for |n|>1)
FAITHFULNESS_USED_BY_ME               = no (declined; it is the reason for
                                        UNVERIFIED)
MACHINERY_IMPORTED_BY_ME              = no (no scale/GR/carrier import)
alpha_computed = false ; kappa_record_computed = false ;
coupling_evaluation_authorized = false ; proof_authorized = false
ALL_RESULTS = CLAIMED until cross-lineage confirmation.
```

---

## 8. VERDICT LINES

QUOTIENT_IS_DIAGONAL_ONLY = CONFIRMED(PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md:22-42, "removed by the physical null quotient" + "[U(1) x U(1)] / U(1)_diag ... kernel is exactly U(1)_diag"; corroborated U3:221-235, Q_N = X_N/(G_N/U(1)_diag))

Q_N_COMPLETE_KERNEL_PHYSICAL = UNVERIFIED (q_N-COMPLETE and constant-vertex/diagonal-only trivial stabilizer are CONFIRMED at U3:210-254 as TYPE-P inside a PARTIAL assembly [U3_008_INSTANCE_EXISTS=false TYPE-U; PHYSICAL_VERDICT=NO_VERDICT]; but the load-bearing "ker(chi_n)=Z_|n| is PHYSICAL structure acting nontrivially on q_N, distinguishing |n|" limb is UNVERIFIED — U3 contains no chi_n/ker(chi_n)/winding and never links a character kernel to q_N; the only |n|-linkage, in FABLE/STAGE1, runs through FAITHFULNESS and types |n|>1 as "constant on kernel cosets ... the record would fail to record", which is the opposite of a recorded kernel)

COUNTER_HYPOTHESIS_SUPPORTED = NO (no sealed text concludes |n| indistinguishable; all four files force |n| to unit winding — note: the counter-hypothesis's response-level algebra, response constant on ker(chi_n) cosets for |n|>1 factoring through U(1)_rel/ker(chi_n) ~= U(1), IS present at FABLE:165-168 and is what makes the sealed forcing rest on faithfulness, not on kernel-on-q_N)

VERDICT = UNVERIFIED (the diagonal-only quotient and q_N-completeness are confirmed at the bytes, but the |n|-forcing CRUX AS STATED is not established: the sealed forcing of |n| runs through FAITHFULNESS — barred by fence as an undischarged premise and not bedrock-derived in the corpus — while the crux's own mechanism, ker(chi_n) physical and recorded on the full-U(1)_rel record acting on q_N, is absent from U3 and contradicted at the response level by FABLE:165-168; missing = a bedrock derivation, independent of adopted faithfulness, that the kernel is retained as recorded physical structure on the record and that this, not faithfulness, forces |n|)

MACHINERY_OR_FAITHFULNESS_USED = no
