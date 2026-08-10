# STAGE 8 — CROSS-CHECK OF THE C3 COUPLING ATTACK
## DARIO LANE (Builder B, verifier) — RELAY 883 — [PLAN:AXN-BUILD-B11]

```text
alpha_computed         = false
proof_authorized       = false
kappa_record_computed  = false
```

All charter fences live. No member bound; no fixed-point execution; no end test; no smooth import; no
EM identification; no common cell formed; no junction map evaluated; no numeric evaluation of any
physical quantity; no comparison to measured constants. PE-1..PE-13 pointer-only, none opened or
consulted. Builder-A code not opened. `~/.codex` untouched; memory-bank never searched. No register,
plan, tracker, git action.

CLAIM STATUS: **all headline items CLAIMED.**

SUBJECT: `STAGE8_AXN_T10_C3_COUPLING_CARRIER_CODEX2_V001.md` = `0af5106f5a7bc2c0`, seal verified BEFORE
reading.

**DISCLOSED AT THE TOP.** I have written **all three colliding glyphs** into sealed artifacts myself.
At 857 I quoted `Gamma_2PI[Abar,G] = (i hbar/2) Tr_C log G^(-1) + Gamma_rest[Abar,G;
source,record,g,gauge,edge]` — carrying **both** `G` and `g` in one sentence — and separately quoted
the adjudication's `G` as the primitive source-geometry conversion. **I used all three roles without
ever asking whether the two `G` glyphs denote the same object.** Confirming the hazard convicts my own
prior work; dismissing it protects that work. **Both pulls were live and the check was built against
them.**

---

## 0. LEAD

| item | result |
|---|---|
| graph | **CONFIRMED** — digest recomputed exactly, and re-serialization reproduces it |
| identity hazard | **CONFIRMED-THREE-UNLINKED** — and the one probe that could have produced a false link resolves to substring artifacts |
| topologies | **CONFIRMED-TWO-LIVE** — both governing flags `NO_VERDICT` at source |
| termwise scope | **CONFIRMED** — no term demand reinstalled |
| conformance | **VERBATIM**, with one **strengthening** the subject discloses itself |

**The identity finding is real, and it matters beyond C3 exactly as the relay says.** If `G_2PI` and
`G_conversion` were silently one object, **any numerical agreement involving them would be an artifact
of notation rather than a result.** The program's coincidence-style scoring depends on this typing.

---

## 1. THE GRAPH — **CONFIRMED**

**Digest recomputed, not accepted.** Extracting the payload between the canonical markers and hashing
per the stated rules (UTF-8, keys sorted, separators `,`/`:`, no trailing newline):

```text
computed  22476fc4d42626d7ac5db205f52b2087cfbaecf57b3d0601538760ace7585c8e
pinned    22476fc4...                                              MATCH
```

**And a stronger check the pin alone would not give:** I parsed the payload and **re-serialized it
canonically from the parsed object** — `json.dumps(sort_keys=True, separators=(',',':'))` — which
reproduces **the same digest**. So the serialization is **genuinely canonical**, not merely a hash of
whatever text happened to sit between the markers. **A hand-edited payload would fail this second
check and pass the first.**

**Structure resolved: 14 nodes, 13 edges.** All three role nodes occur as **distinct** ids —
`g_metric`, `G_2PI`, `G_conversion` — alongside `action_carrier`, `source`, `record`, `gauge`, `edge`,
`gamma_rest`, `variation_receiver`, `boundary_receiver`, `layer_A_density`, `layer_B_operator`,
`gravity_sector`. **Every contract node occurs.**

**No edge asserts an underived map.** Edge-status census:

```text
ABSENT                                       5
PRESENT_SYNTAX_ONLY                          1     <- E01, formal_arguments_of: SYNTAX, not a map
REQUIRED_UNINSTANTIATED                      1
ABSENT_GENERIC_PACKET_PARENT_ONLY            1
REQUIRED_NOT_POSABLE_ON_UNBUILT_FUNCTIONAL   1
PRESENT_ROLE_VALUE_UNDERIVED                 1
PARTIAL_DECLARED_OUTER_ACTION                1
LIVE_NOT_EXHIBITED_NOT_EXCLUDED              1
PARTIAL_ROLE_COMPLETE_MAP_ABSENT             1
```

**Not one status is an unqualified `PRESENT` or `DERIVED`.** Both statuses containing the word
`PRESENT` are qualified in the same token — `SYNTAX_ONLY`, `ROLE_VALUE_UNDERIVED`. **That is the check
that matters**, because an underived map would have to enter as an unqualified present edge, and there
is none.

`GRAPH = CONFIRMED (digest + resolutions).`

---

## 2. THE IDENTITY HAZARD — **CONFIRMED-THREE-UNLINKED**

**This is a positive absence — the claim that no sealed sentence links any pair — and it is the claim
type I have got wrong three times this session.** So it ran **closure-first, hunting for a link**.

**Closure declared before the word "missing" is used:**

```text
C3_ID_CLOSURE := { v004 standing 58208084 ; G adjudication 273f03dd ; AXN skeleton 5a51b940 ;
                   grading authority 2215f79c ; the R3_4 parent SPEC's 15 pinned authorities ;
                   my own 857's cited source set }
```

**The three roles at their own sealed sentences, resolved independently:**

| role | sealed typing |
|---|---|
| `g_metric` | the spacetime/gravity **carrier**, used through `sqrt(-g)`, `gamma^mu`, `D_mu` (skeleton V1 row), and a **peer argument after the semicolon** in `Gamma_rest[…; source,record,**g**,gauge,edge]` |
| `G_2PI` | the argument **before** the semicolon, in `Gamma_2PI[Abar,**G**]` with `Tr_C log G^(-1)`. The corpus's `propagator G` family types this role as a **propagator/two-point object** (`G_K` stationary propagator; one-particle propagator) |
| `G_conversion` | *"c, hbar, and **G** are the three primitive conversion constants of the ordinary branch"* — a **scalar conversion** whose unit-free value is expressly **not derived** |

**THE LINK HUNT, and its one dangerous result.** Probing for identification language, the pattern
`G\s*=\s*g` returned **five** occurrences. Resolved individually:

```text
1-2.  INSIDE 881 ITSELF — and both are its own NEGATIVE probe reports
      ("found zero G=g, g=G, G<->g, or equivalent typed-map sentences")
3.    "BINDIN[G = g]enerated"        <- SUBSTRING ARTIFACT
4.    "B_[G = g]raph incidence operator"  <- SUBSTRING ARTIFACT
5.    "s_G = g_A4(I_K ., I_K .)"     <- an unrelated bilinear form on a DIFFERENT carrier
```

**ZERO genuine identifications.** No equality, intertwiner, conversion map, or common carrier relates
any pair within the declared closure.

**Worth stating because it is the mirror of my own recent errors:** at 878 every `term` hit was a
substring and the artifacts pointed toward a **false absence**; here three of five hits are substrings
pointing toward a **false link**. **Substring artifacts are direction-neutral** — they manufacture
whichever finding the reader is looking for, and the only defence is resolving every hit in context,
which is what §2 does.

`IDENTITY_HAZARD = CONFIRMED-THREE-UNLINKED (closures displayed).`

**And it convicts my own prior work, which I state plainly.** My 857 and 878 both quoted the
`Gamma_2PI[Abar,G] … Gamma_rest[…; g, …]` sentence and the conversion-`G` sentence **without flagging
that two distinct roles share the glyph `G`**. Nothing I concluded there depended on conflating them —
my arguments used `g`'s **argument position**, not `G` — but **a reader of my artifacts could have
flattened the two `G`s and I gave no warning.** 881 found what I should have.

---

## 3. THE TWO TOPOLOGIES — **CONFIRMED-TWO-LIVE**

Both governing flags verified **at their source**, not via the subject:

```text
STAGE8_GRAVITY_MATTER_SOURCE_SUMMANDS_LIVE_V004_STANDING_V001.md
  line 395:  gravity_matter_record_interaction_is_only_via_stationarity = NO_VERDICT
  line 399:  hidden_cross_term_required_by_sealed_text                  = NO_VERDICT
```

**Two `NO_VERDICT`s, and they cut in opposite directions** — exclusivity is not established **and** a
cross-term is not required. That is precisely what leaves **both** completions live:

- `K_stationarity` — shared variational variables and joint stationarity only; explicit partial
  material, **exclusivity unproved**;
- `K_direct_mixed` — the same plus a direct mixed internal `Gamma_rest` dependency; **allowed by the
  typed arguments, neither exhibited nor excluded**.

**Non-equivalent**, and neither selected. `MULTIPLE` correctly fires at the topology-completion
receiver.

`TOPOLOGIES = CONFIRMED-TWO-LIVE.`

---

## 4. TERMWISE SCOPE — **CONFIRMED, no term demand reinstalled**

`TERMWISE_GAP` fires because choosing between the survivors needs a `Gamma_rest` decomposition or
separability theorem. **The subject explicitly refuses to let that reinstall a term demand:**

> *"That triggers `TERMWISE_GAP`, but it **does not** make an additive gravity term a T10 requirement.
> The theorem would decide **graph topology**, not authorize `S_grav,D`, EH/KK, or any selected
> coefficient."*

**This is exactly right and it is consistent with my own 878 ruling** (`T10 =
STRUCTURAL-ADMISSIBLE`): a decomposition theorem is a **topology-deciding** object, not a
term-mandating one. **The gap fires at the graph-topology receiver, which is where it belongs.**

**I checked the three `S_grav,D` mentions in the subject**: each appears only to say the theorem would
**not** authorize it. **No term demand is reinstalled anywhere.**

`TERMWISE_SCOPE = CONFIRMED.`

---

## 5. CONFORMANCE — **VERBATIM**, with one disclosed strengthening

**All six contract stops fired, in the contract's own names**, one-to-one with the subject's lead:

```text
MAP_GAP               <- no total action-side coupling map
U1_GAP                <- Layer-A/Layer-B joint absent
VARIABLE_IDENTITY_GAP <- three roles, no identity or typed map
TERMWISE_GAP          <- requires Gamma_rest decomposition or separability
INSTANCE_ONLY         <- only finite/packet-scoped material
MULTIPLE              <- two non-equivalent topology completions
```

**THE STRENGTHENING, and the subject discloses it itself.** The contract defines
`VARIABLE_IDENTITY_GAP` over **two** roles — *"g-carrier and G-conversion are conflated or
unlinked."* The execution found **three**, splitting the two uppercase-`G` roles, and says so: *"The
original C3 contract said the graph must distinguish `g` and `G`; the execution discovers that two
uppercase-`G` roles must themselves be split."* **That is a strengthening within the stop, not a
deviation from it** — the stop fires, with richer content, disclosed rather than smuggled.

**FORBIDDEN list, checked item by item:** no `g` argument promoted to a `g` summand (it stays a peer
argument); no `S_grav,D` or EH/KK installed (mentioned only to deny authorization); no coefficient or
graph selected by downstream fit (neither survivor chosen); no coupling graph reported as a complete
action (*"neither incomplete topology is called a total action map"*). **Untouched.**

**F1 carried structural** — consistent with my own 878 resolution that a coupled Hessian demands
`g`-dependence, not a `g`-summand.

`CONFORMANCE = VERBATIM.`

---

## 6. FREEDOMS-CONSUMED (law 2, law 2a)

```text
CARRIED UNCHANGED: the three roles as THREE, with no identity asserted or denied beyond what the
  closure shows; both topology survivors LIVE and NEITHER SELECTED; the two NO_VERDICT flags as
  refusals, not as gaps awaiting work; TERMWISE_GAP at the GRAPH-TOPOLOGY receiver only; the graph's
  edge statuses at their sealed qualifications; F1 as structural; my own 857/878 carried as
  producer-declared objects with NO protective weight.

DERIVED HERE: (a) the digest recomputation AND the stronger re-serialization check that a hand-edited
  payload would fail; (b) the edge-status census showing no unqualified PRESENT/DERIVED; (c) the
  per-pair link hunt over a declared closure, and the resolution of all five G=g hits to substring
  artifacts, 881's own negative reports, and one unrelated bilinear form; (d) the observation that
  substring artifacts are DIRECTION-NEUTRAL, mirroring my 878 case; (e) source-side verification of
  both topology flags; (f) the stop-by-stop conformance mapping and the strengthening typing.

SELECTED HERE: NOTHING.  No identity, map, topology, decomposition, coefficient, term, or graph is
  asserted, selected, or promoted.  NO FLAG MOVES.  C3 does not pass and I do not move it.

NOT DONE AND DISCLOSED: I resolved the graph structurally (node ids, edge statuses, all-contract-nodes
  check) and spot-resolved edges rather than re-deriving all 13 from their source refs individually.
  My link hunt is closure-first over the declared set plus a corpus-wide pattern probe; it is NOT a
  per-file semantic reading of every file containing both glyphs.  I did not independently re-derive
  S09's joint stationarity equation.
```

**FLATTENING CHECK — 37/37 walked, clean.**
**S03 and THE VOID CONDITION — live at §3 and §4.** The tidy move was to prefer `K_stationarity`
because it has *"explicit partial material"* while its rival is merely *"allowed"*. **Material
asymmetry is not exclusivity**, the flag says `NO_VERDICT`, and **neither survivor is selected.** The
second was to let `TERMWISE_GAP` slide back into a term demand; **it fires at the topology receiver
and nowhere else.**
**S12** — `NO_VERDICT` carried as a refusal; qualified edge statuses never shortened to `PRESENT`.
**S26 / S08 / S19 / S24** untouched.
**T1 / T5** untouched.
**BR-1 HELD IN BOTH DIRECTIONS.** 881 got no weight toward itself — the digest was recomputed, the
flags read at source, and the link hunt run against my own closure rather than its probe. **And my own
857/878 got no protective weight**, which is why §2 ends by convicting them rather than defending
them.

---

## 7. FINAL LINES

```text
GRAPH = CONFIRMED (digest + resolutions).  Canonical digest RECOMPUTED, NOT ACCEPTED:
  22476fc4d42626d7ac5db205f52b2087cfbaecf57b3d0601538760ace7585c8e = pinned.  AND A STRONGER CHECK THE
  PIN ALONE WOULD NOT GIVE: I parsed the payload and RE-SERIALIZED IT CANONICALLY FROM THE PARSED
  OBJECT, reproducing the same digest — so the serialization is GENUINELY CANONICAL, not merely a hash
  of whatever text sat between the markers.  A HAND-EDITED PAYLOAD WOULD FAIL THIS SECOND CHECK AND
  PASS THE FIRST.  14 nodes / 13 edges resolved; all three role nodes occur as DISTINCT ids
  (g_metric, G_2PI, G_conversion) and EVERY CONTRACT NODE OCCURS.  NO EDGE ASSERTS AN UNDERIVED MAP:
  the status census is ABSENT 5, PRESENT_SYNTAX_ONLY 1, REQUIRED_UNINSTANTIATED 1,
  ABSENT_GENERIC_PACKET_PARENT_ONLY 1, REQUIRED_NOT_POSABLE_ON_UNBUILT_FUNCTIONAL 1,
  PRESENT_ROLE_VALUE_UNDERIVED 1, PARTIAL_DECLARED_OUTER_ACTION 1, LIVE_NOT_EXHIBITED_NOT_EXCLUDED 1,
  PARTIAL_ROLE_COMPLETE_MAP_ABSENT 1 — NOT ONE UNQUALIFIED "PRESENT" OR "DERIVED", and both statuses
  containing "PRESENT" are qualified IN THE SAME TOKEN.
IDENTITY_HAZARD = CONFIRMED-THREE-UNLINKED (closures displayed).  Ran CLOSURE-FIRST AND AS A HUNT FOR
  A LINK, because "no sealed sentence links any pair" is a POSITIVE ABSENCE — the claim type I have got
  wrong three times this session.  C3_ID_CLOSURE declared before the word "missing" was used.  THE
  THREE ROLES AT THEIR OWN SENTENCES: g_metric the spacetime carrier via sqrt(-g)/gamma^mu/D_mu and a
  PEER ARGUMENT AFTER the semicolon; G_2PI the argument BEFORE the semicolon in Gamma_2PI[Abar,G] with
  Tr_C log G^(-1), typed by the corpus's propagator family as a propagator/two-point object;
  G_conversion the scalar "c, hbar, and G are the three primitive conversion constants of the ordinary
  branch", unit-free value EXPRESSLY NOT DERIVED.  THE LINK HUNT'S ONE DANGEROUS RESULT: the pattern
  G\s*=\s*g returned FIVE occurrences — TWO are 881's OWN NEGATIVE PROBE REPORTS, TWO are SUBSTRING
  ARTIFACTS ("BINDIN[G=g]enerated", "B_[G = g]raph incidence operator"), and ONE is an unrelated
  bilinear form on a DIFFERENT carrier ("s_G = g_A4(...)").  ZERO GENUINE IDENTIFICATIONS; no equality,
  intertwiner, conversion map or common carrier relates any pair.  WORTH STATING BECAUSE IT MIRRORS MY
  OWN RECENT ERRORS: at 878 every "term" hit was a substring pointing toward a FALSE ABSENCE; here
  three of five point toward a FALSE LINK — SUBSTRING ARTIFACTS ARE DIRECTION-NEUTRAL, manufacturing
  whichever finding the reader wants, and the only defence is resolving every hit in context.  AND IT
  CONVICTS MY OWN PRIOR WORK: my 857 and 878 both quoted the Gamma_2PI/Gamma_rest sentence AND the
  conversion-G sentence WITHOUT FLAGGING THAT TWO DISTINCT ROLES SHARE THE GLYPH G.  Nothing I
  concluded depended on conflating them — my arguments used g's ARGUMENT POSITION, not G — BUT A
  READER OF MY ARTIFACTS COULD HAVE FLATTENED THE TWO G's AND I GAVE NO WARNING.  881 FOUND WHAT I
  SHOULD HAVE.
TOPOLOGIES = CONFIRMED-TWO-LIVE.  Both governing flags verified AT SOURCE, not via the subject:
  gravity_matter_record_interaction_is_only_via_stationarity = NO_VERDICT (line 395) and
  hidden_cross_term_required_by_sealed_text = NO_VERDICT (line 399).  TWO NO_VERDICTs CUTTING IN
  OPPOSITE DIRECTIONS — exclusivity not established AND a cross-term not required — which is exactly
  what leaves both K_stationarity (explicit partial material, exclusivity unproved) and K_direct_mixed
  (allowed by the typed arguments, neither exhibited nor excluded) live and non-equivalent.  MULTIPLE
  correctly fires at the topology-completion receiver; NEITHER SURVIVOR IS SELECTED.
TERMWISE_SCOPE = CONFIRMED (no term demand reinstalled).  TERMWISE_GAP fires because choosing between
  the survivors needs a Gamma_rest decomposition or separability theorem, and the subject explicitly
  refuses to let that reinstall a term demand: the theorem "would decide GRAPH TOPOLOGY, not authorize
  S_grav,D, EH/KK, or any selected coefficient."  CONSISTENT WITH MY OWN 878 RULING — a decomposition
  theorem is a TOPOLOGY-DECIDING object, not a term-mandating one.  I checked all three S_grav,D
  mentions in the subject: each appears ONLY to deny authorization.
CONFORMANCE = VERBATIM.  All six contract stops fired IN THE CONTRACT'S OWN NAMES, one-to-one with the
  subject's lead: MAP_GAP, U1_GAP, VARIABLE_IDENTITY_GAP, TERMWISE_GAP, INSTANCE_ONLY, MULTIPLE.  ONE
  STRENGTHENING, DISCLOSED BY THE SUBJECT ITSELF: the contract defines VARIABLE_IDENTITY_GAP over TWO
  roles ("g-carrier and G-conversion are conflated or unlinked") and the execution found THREE,
  splitting the two uppercase-G roles — "the execution discovers that two uppercase-G roles must
  themselves be split."  THAT IS A STRENGTHENING WITHIN THE STOP, NOT A DEVIATION FROM IT: the stop
  fires with richer content, disclosed rather than smuggled.  FORBIDDEN LIST CHECKED ITEM BY ITEM AND
  UNTOUCHED: no g promoted to a g summand; no S_grav,D or EH/KK installed; no coefficient or graph
  selected by downstream fit; no coupling graph reported as a complete action.  F1 carried structural.
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+3):
  (1) THE FINDING I CONFIRM CONVICTS MY OWN SEALED WORK, AND I HAD BOTH PULLS.  I have written all
      three colliding glyphs into artifacts — the Gamma_2PI/Gamma_rest sentence at 857 and again at
      878 — without once asking whether the two uppercase G's denote the same object.  Confirming the
      hazard indicts my own prior artifacts; dismissing it would have protected them.  I state the
      indictment rather than noting the collision neutrally.
  (2) I CONFIRMED ON ALL FIVE AXES, WHICH IS THE OUTCOME A CROSS-CHECKER SHOULD DISTRUST MOST.  The
      guards were making each check independent of the subject: the digest RECOMPUTED and additionally
      RE-SERIALIZED; the topology flags read AT SOURCE; the link hunt run against MY OWN declared
      closure rather than against 881's probe — which is why my hunt returned five hits where 881
      reported zero, and why resolving those five was the actual work.
  (3) MY COVERAGE IS UNEVEN AND "CONFIRMED" SHOULD NOT IMPLY OTHERWISE.  I resolved the graph
      STRUCTURALLY — node ids, edge statuses, all-contract-nodes — and SPOT-RESOLVED edges rather than
      re-deriving all thirteen from their source refs; the link hunt is closure-first plus a
      corpus-wide pattern probe, NOT a per-file semantic reading of every file carrying both glyphs;
      and I did not re-derive S09's joint stationarity equation.  A LINK HIDING IN PROSE THAT USES
      NEITHER GLYPH PATTERN IS THE LIVE RESIDUAL RISK, and it is where the next check should press.
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

---

**GATES HELD.** All charter fences live; nothing selected; no smooth import; no EM identification; no
member binding; no fixed-point execution; no end test; no numeric evaluation of physical quantities;
no comparison to measured constants; no common cell formed; no junction map evaluated. PE-1..PE-13
pointer-only, none opened or consulted. Builder-B independence held. `~/.codex` untouched;
memory-bank never searched. No register, plan, tracker, or git action.
