# Stage 8 — q_N Completeness Assembly v001
## BLIND STRUCTURAL BUILD — codename QN-COMPLETE-BUILD — [CLAIMED]

Date: 2026-08-13
Role: BEDROCK / TYPING ONLY. No numeric value of anything is computed, bounded,
estimated, or compared. n, kappa, alpha, 137, and every winding index are
SUBJECTS by type throughout; the character exponent is written symbolically
(`n`, `|n|`). No scale, ell_P, metric, KK object, or "faithfulness-as-premise"
is imported. No register/tracker/plan/road/ledger/lens file was read.

Gates: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false` ; `coupling_evaluation_authorized = false`

---

## 0. SEALS VERIFIED AT PATH (recomputed before reading)

| Source | SHA-256 (recomputed at path) | Status |
|---|---|---|
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U3_DOR008_DOR009_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` (U3) | `b0118d89e0b4b321fbf9caab5bfb811a0b5fd572e808d02615ee8503db2bc1ac` | matches its `.seal.sha256` sidecar |
| `PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md` (PRP) | `45f6015c74593fd25f7862aa7bf6407e124f449ff7635dcf2f9d4c2c2303f08f` | matches task-supplied digest |
| `STAGE8_BARE_SURFACE_ALPHA_DETERMINATION_FABLE_V001.md` (FABLE) | `82e81f6e659108c05872d30d4c5ad00bf66cad3c272c4aa8240aa89fc5a62010` | matches task-supplied digest |
| `STAGE1_PREMISE_DISPOSITION_V001.md` (S1) | `254128f73a44869839d670557368709c1bf2a98d6f86b48f026064c80e8d2585` | matches task-supplied digest |

All four seals verify. Byte spans below are (file, line-range, byte-range) with
byte offsets 0-based half-open, computed at path.

---

## 1. q_N AND THE GROUP ACTION — OF RECORD

**Group action (common vertex gauge).** U3 fixes the doubled finite history
carrier and the ONE admissible action.

```text
X_N := Hist_N^rat x Hist_N^rat = { (z_+,z_-) | z_+,z_- in U(1)^N }
G_N := U(1)^(N+1)                              open-chain vertex gauge group
(g . z_a)_j := g_j z_(a,j) g_(j-1)^dagger,     a in {+,-}, j=1..N   [COMMON action]
```

The action is the SAME element `g` on both CTP branches; independent per-branch
transformation is expressly refused.
Grounding: U3 lines 155-189, byte span `[7024, 7866)` region; the one-cell
sealed origin `z^g = t z s^dagger` is quoted from
`STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md:321-354`.

**Orbit invariant q_N.** The relative-holonomy map, of record:

```text
q_N : X_N -> U(1)^N,   q_N(z_+,z_-)_j = r_j := conjugate(z_(-,j)) z_(+,j).
```

Grounding: U3 lines 191-235, byte span `[7866, 8850)`. Invariance under the
common action is the exact cancellation
`conjugate(g_j z_(-,j) g_(j-1)^dagger)(g_j z_(+,j) g_(j-1)^dagger) = conjugate(z_(-,j)) z_(+,j)`
(U3 lines 200-208).

**The two configuration-level readings of "the group action."** The task's
completeness definition names one action two ways, and the two ways are NOT the
same map until one node is supplied. This artifact keeps them separate on
purpose:

- READING A — VERTEX-GAUGE action of `G_N = U(1)^(N+1)` on the U(1)-valued
  histories `z`. Physical-null = the constant/diagonal vertex subgroup. This is
  the action U3 instantiates directly; the `z`'s are group elements, not yet
  characters of anything.
- READING B — WINDING / CHARACTER structure. In the connection-only surface the
  history entries are themselves characters of an underlying holonomy,
  `z_(a,j) = chi_n(h_(a,j))`, so `r_j = chi_n(relative holonomy in cell j)`
  (FABLE lines 59-72). The transformations of interest are then elements of the
  underlying holonomy carrier, among them the character kernel `ker(chi_n)`.

Readings A and B coincide only when `chi_n` is injective, i.e. `|n| = 1`. That
condition is the whole hinge of Section 2-4.

---

## 2. COMPLETENESS — READING A (VERTEX-GAUGE ORBIT SEPARATION): SHOWN, TYPE-P

Claim A: `q_N(config) = q_N(config')` IFF `config, config'` lie in the same
`G_N`-orbit, and the ONLY elements of `G_N` acting trivially on `q_N` are the
constant/diagonal vertex transformations `g_0 = ... = g_N` (the physical-null
subgroup U(1)_diag).

**A.1 same-orbit => same q_N.** The invariance computation above. TYPE-P.

**A.2 same q_N => same-orbit (the separating direction).** U3 gives the explicit
reconstruction: given equal relative holonomies, set `g_0 = 1` and recursively
`g_j := w_(-,j) g_(j-1) z_(-,j)^dagger`; then `g.z_- = w_-`, and equality of the
relative holonomies forces `g.z_+ = w_+`. Hence equal `q_N` values put the two
pairs in one common-gauge orbit.
Grounding: U3 lines 210-219, byte span `[8173, 8494)`.

**A.3 the trivially-acting subgroup is EXACTLY the diagonal — nothing more.**
Two independent record witnesses:

- U3: the stabilizer "consists of constant vertex transformations
  `g_0 = ... = g_N`. It acts trivially. After removing this constant null
  direction, the effective action is free," giving
  `Q_N = X_N / (G_N / U(1)_diag) ~= U(1)^N`, `[z_+,z_-] <-> r`.
  Grounding: U3 lines 220-235, byte span `[8494, 8850)`.
  "Effective action is free" is precisely the statement that NO non-diagonal
  element acts trivially — the enumerated trivially-acting subgroup is closed at
  the diagonal.
- PRP, independently, for the primitive two-endpoint carrier: the comparison map
  `(u_0,u_1) -> u_1 u_0^(-1)` "is onto and its kernel is exactly `U(1)_diag`, so
  the quotient contains one compact relative-phase handle and no second
  independent phase handle."
  Grounding: PRP lines 33-42, byte span `[844, 1101)`.

**A.4 the two structure-preserving refutations of "something more than the
diagonal acts trivially."** U3 Section 8.1 shows that enlarging the trivially-
acting set to INDEPENDENT per-branch transformations is inadmissible precisely
because it would erase `r` — i.e. any transformation beyond the common/diagonal
one acts NON-trivially on `q_N`.
Grounding: U3 lines 653-666 (`INDEPENDENT_BRANCH_QUOTIENT_ADMISSIBLE = false | TYPE-R`,
test: "it removes the sealed relative-history invariant product_j r_j").

**Reading-A verdict.** The trivially-acting subgroup is the constant/gauge-
diagonal subgroup and nothing more; `q_N` separates every pair of distinct
vertex-gauge orbits. This is exactly U3's `FINITE_ORBIT_INVARIANT_COMPLETE =
true | TYPE-P | premises: DoR-008, DoR-009` and `FINITE_CONSTANT_STABILIZER_
REMOVED = true | TYPE-P` (U3 lines 246-254, byte span `[9006, 9344)`).

```text
READING_A_TRIVIAL_SUBGROUP_IS_DIAGONAL_ONLY = SHOWN
  span: U3:210-235 [8173,8850) + PRP:33-42 [844,1101) + U3:653-666
  typing: TYPE-P | premises DoR-008, DoR-009 | no faithfulness, no machinery
```

No node in Reading A is left at premise-level-pending: every step is discharged
from U3 + PRP record content. Reading A is COMPLETE_OF_RECORD.

---

## 3. COMPLETENESS — READING B (WINDING-MAGNITUDE): ONE NODE, NAMED

The task's definition additionally demands the "Equivalently" clause: the
character kernel `ker(chi_n) = Z_|n|` for `|n| > 1` must act NON-trivially on
`q_N` (so winding MAGNITUDE is distinguished). This is a strictly stronger
claim than Reading A, and it is NOT automatically true. Here is the exact
enumeration.

**B.1 the kernel structure, of record.**

```text
chi_n(exp(i theta)) = exp(i n theta),  n in Z.
ker(chi_n) = U(1)          (n = 0)          [unfaithful: whole group trivialised]
           = Z_|n|         (|n| > 1)        [finite roots-of-unity subgroup]
           = { identity }  (|n| = 1)        [faithful]
```

Grounding: S1 lines 29-34, byte span `[727, 1027)`; PRP lines 74-76, byte span
`[1667, 1887)` ("n=0 is unfaithful and |n|>1 repeats the primitive winding").

**B.2 the decisive fact — direction of the kernel's action.** Because `chi_n` is
a homomorphism, for any `k in ker(chi_n)` and any holonomy `h`,
`chi_n(h.k) = chi_n(h) chi_n(k) = chi_n(h)`. Therefore, when the history entries
are read as characters (`z = chi_n(h)`), the subgroup `ker(chi_n)` acts
**trivially** on `z`, hence on every `r_j`, hence on `q_N`. Restated:

```text
for |n| > 1:  Z_|n| = ker(chi_n) acts TRIVIALLY on q_N.
for |n| = 1:  ker(chi_n) = {identity};  no non-identity element acts trivially.
```

So the "Equivalently" clause of the completeness definition — "ker(chi_n) acts
NON-trivially, distinguishing winding magnitude" — is TRUE for `|n| = 1` and
FALSE for `|n| > 1`. Winding-magnitude completeness is therefore EQUIVALENT to
`|n| = 1` (faithfulness of the response character). It is not derivable from
Reading A: Reading A quotients the vertex gauge `G_N`, which never touches the
underlying holonomy carrier where `ker(chi_n)` lives.

**B.3 the node named.** The single node standing between Reading A and the task's
full (Reading-A-and-B) completeness is:

```text
NODE  FAITHFULNESS_|n|=1 : the record's charged-sector response character is
      faithful, equivalently ker(chi_n) = {identity}, equivalently |n| = 1.
```

**B.4 disposition of the node in the record (typing, not import).** The record
supplies an argument for the node; it does not supply it as a bare numeric
premise:

- FABLE §5a: "a non-faithful response is constant on kernel cosets — precisely
  those source histories the record would fail to record"; the trivial baseline
  "has zero variation under every external history" and is eliminated by the
  surface's own charge/flux-access requirement. Read as TYPING: "being a RECORD
  of the connection" means separating the source histories; a character constant
  on `ker(chi_n)` fails to separate the histories differing by `Z_|n|`, so it is
  not a record of them. Grounding: FABLE lines 161-172, byte span `[9065, 9924)`.
- S1 Disposition 1: `|n| = 1` "DERIVED from faithful U(1) character theory,"
  from "the derived relative U(1) stabilizer; continuity; one-dimensional
  unitary action; faithfulness after the response-null quotient; and an
  orientation convention." Grounding: S1 lines 15-47, byte span `[459, 1438)`.
- S1 Disposition 2, HOWEVER, classifies "the primitive faithful U(1)_rel
  character" as `DISCLOSED_ORDINARY_PRIMITIVE_BRANCH_INPUT` (S1 lines 50-67) —
  i.e. faithfulness itself enters as a DISCLOSED BRANCH INPUT, and `|n| = 1` is
  the derived CONSEQUENCE of that input.

**B.5 the circularity that blocks a bare-Reading-A discharge.** Reading-B
completeness ("q_N distinguishes every winding-distinct configuration") is, term
for term, the statement that the response character separates all relative-phase
histories, which is the statement that the character is faithful. So Reading-B
completeness and the node FAITHFULNESS_|n|=1 are the SAME proposition. It cannot
be manufactured out of Reading A; it can only be (i) taken as record-definitional
bedrock (FABLE §5a: "record" ⟹ "records" ⟹ faithful), or (ii) read off DoR-008's
ratified carrier if that carrier is stipulated faithful, or (iii) left as the
disclosed branch input S1 Disposition 2 records. Routes (i)-(iii) all consist of
USING faithfulness; the task fence bars importing faithfulness as a premise.
Honouring the fence, this artifact does NOT import it: it names it as the one
residual node and reports Reading-B as premise-level-pending on that node.

```text
READING_B_WINDING_MAGNITUDE_COMPLETE = CONDITIONAL(FAITHFULNESS_|n|=1)
  = SHOWN if and only if the node is granted (record-definitional bedrock,
    or ratified-carrier content of DoR-008, or the S1 disclosed branch input);
  the fence bars importing it as a free premise, so it is carried, not used.
```

---

## 4. TYPING OF THE COMPLETED ARGUMENT

```text
Reading A (orbit separation, diagonal-only trivial subgroup):
  TYPE-P | premises DoR-008, DoR-009 | discharged of record (U3 §2.2, PRP)
  residual TYPE-R/TYPE-U nodes: NONE

Reading B (winding-magnitude distinguishability, the "Equivalently" clause):
  carries exactly one node: FAITHFULNESS_|n|=1
  typing of that node:
    - TYPE-P    IF DoR-008's ratified carrier is stipulated the faithful record
                carrier (then it is ratified-premise content, and Reading B is
                TYPE-P on DoR-008/009) — but this USES faithfulness;
    - TYPE-R    under S1 Disposition 2, where it is DISCLOSED_ORDINARY_PRIMITIVE_
                BRANCH_INPUT, a disclosed input rather than one of the two
                ratified DoR premises;
    the record-definitional (bedrock) route (FABLE §5a) discharges it as a
    typing truth about "record," not a numeric import.
```

The honest global typing: the object U3 built and named `q_N` is COMPLETE_OF_
RECORD **as a vertex-gauge orbit invariant** (Reading A, TYPE-P, no faithfulness,
no machinery). The task's completeness DEFINITION additionally folds in the
winding-magnitude clause (Reading B), which is not a restatement of Reading A but
is exactly the faithfulness node; it is therefore STILL_PARTIAL on the single
node FAITHFULNESS_|n|=1, which the fence bars this build from importing. U3's own
`TYPE-P` typing of `FINITE_ORBIT_INVARIANT_COMPLETE` is thus precisely correct
and precisely bounded: it certifies Reading A and stands ON the ratified faithful
carrier for Reading B — the "premise-level" character is genuine and lives at
exactly this node.

---

## 5. THE FALSIFIER, AND WHETHER THE RECORD TRIPS IT

**Falsifier F.** q_N is INCOMPLETABLE if some NON-null transformation acts
trivially on q_N — i.e. a transformation outside the constant/gauge-diagonal
subgroup that nonetheless leaves every `r_j` fixed, so that winding magnitude
becomes indistinguishable.

**The unique candidate the record actually offers.** `ker(chi_n) = Z_|n|` for
`|n| > 1`. By B.2 it acts trivially on `q_N` (a homomorphism kills its kernel),
and it is NOT the vertex-gauge diagonal — it lives in the holonomy carrier, not
in `G_N`. So IF `|n| > 1` is admitted, F is tripped and `q_N` is INCOMPLETABLE
in the winding-magnitude sense.

**Does the record trip F?**

- Reading A: NO. Within `G_N`, the effective action after removing the diagonal
  is free (U3 lines 220-229); no non-diagonal `G_N` element acts trivially. F has
  no witness in the vertex-gauge action.
- Reading B: the ONLY witness would be `Z_|n|` with `|n| > 1`. The record does
  not admit it AS LONG AS the node FAITHFULNESS_|n|=1 holds: faithful ⟹
  `ker(chi_n) = {identity}` ⟹ no non-null trivially-acting transformation ⟹ F
  not tripped. The record's own charge/flux-access requirement (FABLE §5a) and
  S1's `|n| = 1` disposition disarm F — but they disarm it via, and ONLY via,
  the faithfulness node. Strip that node and F is tripped.

**Net.** The falsifier is not tripped by the constructed content; its entire
status is controlled by the single node FAITHFULNESS_|n|=1. The record supplies a
bedrock/disclosed argument that disarms it; the fence forbids this build from
banking that argument as a premise. So: F is DISARMED-CONDITIONAL-ON the one node,
NOT tripped, NOT unconditionally cleared.

---

## 6. NODES U3 LEFT AT PREMISE-LEVEL — DISCHARGE LEDGER (q_N-completeness scope only)

Scope note: U3's five UNINSTANTIATED fields (descended measure `dmu_C`, physical
contour/`i epsilon` prescription, complete boundary/edge/gluing package, unbounded
endpoint domains, common-origin provenance) are NOT inputs to q_N-completeness;
they are downstream consumers. They remain TYPE-U and are out of scope here. The
q_N-completeness-relevant nodes:

```text
NODE                                     DISPOSITION
orbit map q_N well-defined & invariant    DISCHARGED  U3:191-208  TYPE-P
same-q_N => same-orbit (separation)        DISCHARGED  U3:210-219  TYPE-P
stabilizer = constant diagonal, nothing    DISCHARGED  U3:220-235 + PRP:33-42
  more (Reading A trivial subgroup)                    TYPE-P
non-diagonal / independent-branch acts     DISCHARGED  U3:653-666  (attack refuted)
  non-trivially
ker(chi_n)=Z_|n| structure                 DISCHARGED  S1:29-34, PRP:74-76  TYPE-P
winding-magnitude distinguishability =     UNDISCHARGEABLE UNDER FENCE
  FAITHFULNESS_|n|=1                        reason: equivalent to faithfulness;
                                            fence bars importing faithfulness as
                                            a premise; record offers it only as
                                            bedrock-definitional / DoR-008 carrier
                                            / S1 disclosed branch input (all = USING
                                            faithfulness). Carried as residual node.
```

---

## 7. WHAT THIS ARTIFACT DOES NOT SAY

```text
IT DOES NOT compute or bound n, |n|, kappa, alpha, 137, or any value; the
   winding index is a symbolic subject throughout.
IT DOES NOT import faithfulness as a premise; it NAMES faithfulness as the single
   residual node and reports the winding-magnitude clause as pending on it.
IT DOES NOT import a scale, ell_P, metric, KK object, or "machinery"; Reading A is
   pure vertex-gauge group theory of record.
IT DOES NOT claim Reading B is derivable from Reading A; it shows the two coincide
   only on the faithful carrier and are otherwise distinct.
IT DOES NOT touch U3's measure/contour/boundary/domain/origin residuals, which are
   downstream of q_N and remain TYPE-U in U3.
IT DOES NOT register, commit, push, or ratify anything.
```

---

## 8. FINAL FLAG BLOCK

```text
Q_N_STATED = q_N(z_+,z_-)_j = conjugate(z_(-,j)) z_(+,j) = r_j : X_N=(U(1)^N)^2 -> U(1)^N, the relative-holonomy invariant of the common vertex-gauge action G_N=U(1)^(N+1), (g.z_a)_j=g_j z_(a,j) g_(j-1)^dagger  [U3:191-235, bytes [7866,8850)]

TRIVIAL_SUBGROUP_IS_DIAGONAL_ONLY = SHOWN(U3:210-235 [8173,8850) + PRP:33-42 [844,1101) + U3:653-666; Reading A, TYPE-P, no faithfulness) ; the winding-magnitude "Equivalently" clause (ker(chi_n)=Z_|n| acts non-trivially) is NOT_SHOWN(equivalent to FAITHFULNESS_|n|=1; fence bars importing it)

COMPLETENESS = COMPLETE_OF_RECORD for the vertex-gauge orbit invariant (Reading A, diagonal-only, TYPE-P) ; STILL_PARTIAL(FAITHFULNESS_|n|=1) for the winding-magnitude distinguishability the task definition additionally demands (Reading B)

TYPING = TYPE-P for Reading A (rests only on DoR-008, DoR-009) ; carries(FAITHFULNESS_|n|=1) for Reading B — TYPE-R under S1 Disposition 2 (DISCLOSED_ORDINARY_PRIMITIVE_BRANCH_INPUT), promotable to TYPE-P only by USING DoR-008's carrier-faithfulness

MACHINERY_OR_FAITHFULNESS_USED = no (Reading A uses neither) ; the Reading-B closure would require yes(faithfulness/|n|=1), which the fence bars — so it is carried as a residual node, NOT used

FALSIFIER = "a non-null transformation acts trivially on q_N (winding magnitude indistinguishable)"; unique record candidate = ker(chi_n)=Z_|n|, |n|>1; RECORD DOES NOT TRIP IT (Reading A action is free; Reading B disarmed by faithfulness) but disarmament is CONDITIONAL-ON the one node FAITHFULNESS_|n|=1

FENCE_RESPECTED = CERTIFIED. Bedrock/typing only; every quantity symbolic; no n/kappa/alpha/137/value evaluated; no scale/ell_P/metric/KK imported; faithfulness NOT imported as premise but named as the residual node; no register/tracker/plan/road/ledger/lens read; seals verified at path before reading; no register/commit/push.

alpha_computed = false [TERMINAL_FENCE_DECLARATION]
proof_authorized = false [TERMINAL_FENCE_DECLARATION]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION]
coupling_evaluation_authorized = false [TERMINAL_FENCE_DECLARATION]
ALL_RESULTS = CLAIMED until an external-lane check.
```
