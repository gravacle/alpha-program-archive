# STAGE 8 / PLAN F0 — K_* DEFINING-CHAIN PIN — CODEX 2 V001

Date: 2026-08-09  
Lane: CODEX 2  
Scope: sealed-stock hunt and citation pin only  
Status of every headline determination in this report: **CLAIMED**, pending independent cross-check  
Authority claimed: none

## 0. Result in plain language

**CLAIMED:** the corpus does define what `K_*` is at the abstract level. It is the
unique simple positive onset root of the scalar closure residual of the complete
on-shell `Gamma_K` / Boundary-Resolved stationary one-cell problem, conditional
on the induced-only/current-carrier branch and gated by the opening, mutation,
and admitted-family uniqueness conditions below.

**CLAIMED:** that definition is not executable today. The live-currency audit
says no unique executable `C_record(K)` formula is appointed; the producer and
mutation-family objects are incomplete; the local-shadow-to-physical-carrier
bridge is absent; and no sealed statement proves the required `K_*` to
`kappa_Thomson` identity. `K_*` is therefore **PARTIALLY DEFINED**, not
undefined and not computed.

Nothing in this report derives or evaluates a root, response, stiffness,
coupling, scale, or physical quantity.

## 1. Preflight, custody, and searched space

### 1.1 Pins

- `PROGRAM_STATE_BRIEF_V005.md` verified at
  `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`
  and read before task work.
- Governing plan `THE_PLAN_TO_ALPHA_AND_GRAVITY_V003.md` verified at
  `4ddebb1e8a7387a5fd49724c59ec55853ed457a70e242ae57a725ff9ae9d875f`.
- The current cleanroom copy of `QUESTIONS_SETTLED_REGISTER_V001.md` verified at
  `e99e22811a5bcddbd51c0e1fa57e4aa9262e890d13e6bb9e0c7565d387a48dbf`.
  Its sealed content ends at Q-685. It contains Q-34 and Q-62, but not Q-691.
- Every non-packet authority admitted below had its adjacent seal rechecked.
  The cited V011 copy is the packet copy, not an unsealed root; its bytes hash
  to the packet-pinned
  `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a`.
- PE-1 through PE-7 were not consulted and carry zero weight.

### 1.2 Glob and searched-space clause

The candidate corpus was generated with:

```text
rg --files -g '*.md' -g '*.json'
  -g '!relay_inbox/**' -g '!relay_outbox/**'
  -g '!evaluator_build_A/**' -g '!evaluator_build_B/**'
  -g '!checks/**' -g '!stage8_execution/**'
  -g '!review_packets/**/PE_*' -g '!rd22_run_*/**'
  -g '!**/__pycache__/**'
```

This returned **1,787 files** in the cleanroom. Relay text, lane returns,
generated evaluator/package copies, run roots, caches, and PE material were
excluded because they are not definition authorities. The sealed review-packet
stock otherwise remained in scope. Search hits were candidates only: a span
entered the authority table only after its carrier pin was verified.

### 1.3 Multiple-form search transcript

| Query family | Files hit |
|---|---:|
| `K_*` | 98 |
| `K_star` | 70 |
| `onset stiffness` | 3 |
| `stiffness selector` | 10 |
| `Thomson stiffness` | 11 |
| `kappa_Thomson` | 160 |
| content synonym `onset root` | 18 |
| content synonym `C_record(K` | 44 |
| content synonym `Gamma_K` | 119 |
| content synonym `threshold-conditioned` | 15 |
| content synonym `physical charged-sector Thomson` | 1 |
| content synonym `impedance(s) of` | 6 |
| content synonym `alpha_micro` | 15 |

M-2 covered exact/case-folded forms, symbol/ASCII forms, underscore/hyphen/
spacing variation, and content-synonym search. A hit that merely quoted a
listed authority, reported a status flag, fenced computation, or named the
symbol without adding a fixing predicate was classified **MERE MENTION**.
Exact repetitions do not become additional independent definition spans.

## 2. AS1 — the definition/type/constraint spans

The table is the complete set of independent fixing content recovered by the
search. “Span SHA” hashes exactly the displayed half-open byte span.

| ID | Class | Sealed carrier (file SHA-256) | Half-open span; span SHA-256 | What the span fixes |
|---|---|---|---|---|
| D01 | DEFINITION | `QUESTIONS_SETTLED_REGISTER_V001.md` (`e99e22811a5bcddbd51c0e1fa57e4aa9262e890d13e6bb9e0c7565d387a48dbf`) | `[90997,94540)`; `d139a80e8598c924e75118f94432d98b3f5ce5e546ac9c583e1aed0a62ae67f0` | Q-34 fixes alpha's source as `K_*`, types it as the onset root of the one-cell closure condition, and re-poses slot 16 as `K_* -> kappa_Thomson`. |
| D02 | CONSTRAINT | same register pin | `[169469,171149)`; `75e6b3441b9e247dfd4bdcfa0eb947844a41b1102f752edb543f2a0ad03071b8` | Q-62 keeps `K_*`, `kappa_record`, and `kappa_Thomson` separately typed and denies an existing identification. |
| D03 | DEFINITION / CONSTRAINT | `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md` (`2d63dfadbb741c467b812f21e14f9e0e66015f1d86e2aa8307d8ae77acfe3d69`) | `[1134,3816)`; `4db2fd84d713b9c4d9fa0e704f81f5662dc1e3e22c61e85c6678b43e88773fab` | Makes the result conditional on the induced-only/current-carrier branch and says a completed `Gamma_K` plus unique simple positive `C_record` root would determine `K_*`; `k_R` enters the equation. |
| D04 | DETERMINATION ROUTE | same Gamma spec pin | `[5312,11674)`; `1dd0ff7fa25b3086d19a8fcc83bd833a2ae179fad9a90955559dce04dbe6ec4c` | Specifies the `Gamma_K` functional, normalization, measure, physical domain, charge ensemble, and boundary-data schema that must feed the root problem. |
| D05 | DETERMINATION ROUTE | same Gamma spec pin | `[11674,15744)`; `689072eafd8a5b8855b48741a6ab6b1644ab66df8394034018343366fe0f7c86` | Specifies the same-branch stationary cell `X_K`, including the duration and conjugate-energy target. |
| D06 | DETERMINATION ROUTE / CONSTRAINT | same Gamma spec pin | `[15744,17597)`; `1fbf5f74be31e9e498c1717c8e5a82c9aa547c9b3ec9f324ca237950ade9bedd` | Requires a BR operator/domain/spectrum on the same `X_K`, no earlier public charged record, one first record, an isolated next mode, and no second root/modulus. |
| D07 | DEFINITION | same Gamma spec pin | `[17597,20485)`; `775e7191fd4e83ee5116dd4d0cb937f83679b902c983a313d6fd99a2bf7c19ae` | Defines `C_record(K)` as the complete on-shell scalar closure residual and fixes `C_record(K_*)=0`, nonzero derivative, positivity, exhaustive-family uniqueness, and full-operator rather than scalar-projection closure. |
| D08 | CONSTRAINT | same Gamma spec pin | `[20631,23878)`; `8037d1fc1d235f6c1a208199f5ee6f9c089df31aefc38627c4411fc7cc7af5e9` | Freezes order: derive before root solve; audit geometry/clock/measure/regulator/action partition; pass uniqueness; solve once and reproduce. |
| D09 | DEFINITION / CONSTRAINT | `STAGE8_C_RECORD_LIVE_DEFINITION_CURRENCY_AUDIT_V001.md` (`885265bbce9f2999a4369d25ba4fb9cf3be3a3e59d48d763d0e6238fefce3b51`) | `[220,1766)`; `5ee5835d293d56104cb084898644af44efeeffc52f1f96d6508f9e7a5577676d` | Preserves only the abstract `C_record` output type and rules that no unique executable formula is currently appointed; it also prevents revival of the retired mass selector or adoption of the phase form. |
| D10 | DEFINITION / CONSTRAINT | `STAGE8_KAPPA_RECORD_KSTAR_PAIR_TEST_UNDER_Q61_V001.md` (`5d86c9c1a6433db4ea279d31e9a0163fc9e542f490810fdd2cba0252cc27a0e2`) | `[3815,7246)`; `1ed96c16df0b504374176d16a3a8f1349866a85e3c3d3dcf7cad301e294332ca` | Types `kappa_record` as primitive intensive record Hessian, `K_*` as one-cell onset/root surrogate, and `kappa_Thomson` as physical charged low-momentum stiffness. |
| D11 | DEFINITION / CONSTRAINT | sealed packet copy `review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` (`aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a`) | `[52738,55648)`; `56af7534213b52c13567fd26daa54dd75c57e9ff2422a8dc6938fb785e43955b` | Defines complete `Q_spec`, `Gamma_Q`, `kappa_Q`, and the Thomson limit; says `kappa_record=kappa_Thomson` is not assumed and must follow from the complete amplitude or fail. |
| D12 | DETERMINATION ROUTE / CONSTRAINT | `STAGE8_7A_THOMSON_SCOPING_DARIO_V001.md` (`ebed567ba1062dab0a6707b4c38ee82ae5dcf58bb1dfdd4d9986f8975add4b13`) | `[4378,9464)`; `ccb9694380bfb0b2d90e8778097eb6648fce8bdb76b1c3748483ce2a9ab3e076` | Fixes C7's nine-slot order, records 0/18 content, types S13/S16 threshold conditioning, and enforces the primitive/full-charged firewall. |
| D13 | CONSTRAINT | `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md` (`76589e94bb4af318880c61c3d677dc2518add8480100a7afaf675e4dd3a394a8`) | `[29145,30285)`; `92f6a9d5e6bcbaeb652199f058ece7091d1c1a461990f86d29789d58b01091af` | Carries the re-posed `K_* -> kappa_Thomson` obligation, threshold condition, and missing `LOCAL-SHADOW` to physical-carrier bridge; explicitly calls transport undetermined. |
| D14 | CONSTRAINT | `STAGE8_GAMMA_K_ROOT_PREMISE_RECOVERABILITY_DETERMINATION_V001.md` (`28b088f5257539e7ef6e8dc80e35b24dff9150082aa5ebbbf5fcff1137bef12f`) | `[2997,3930)`; `5f62442f2ff68ae59d7f2b6c2b2c4052c0f65f34220f9b2949c51a63bd8a437d` | Rules that carrier/domain, quotient, measure, record-effect family, and state declarations do not constitute a complete executable root producer without a new adoption. |
| D15 | CONSTRAINT | `STAGE8_GAMMA_K_ROOT_PRODUCER_ATTEMPT_F_RP1_V001.md` (`81e2aa87deb410922f794085341eca3993a68aca986a46a5a60b1b7ad6b1993b`) | `[2770,3451)`; `b89a7924539fe4130fead8b160ed4fd943a3635b2bd634cf616bfef8e5d8ec0a` | Records F-RP1: no root producer was derived because definite carrier/state/quotient/measure/effect content would have to be chosen. |
| D16 | CONSTRAINT | same F-RP1 pin | `[8095,9403)`; `edea9819c021efb5cfa3541ce70ee46b293d455998b296537c338071dc1c7011` | Records that the five mutation classes are named but their executable member sets are not enumerated. |

All other searched occurrences are **MERE MENTION**, duplicate quotation, status,
or historical/superseded route. They add no independent defining predicate.

## 3. AS2 — the defining chain

`EXISTS` below means a sealed schema/definition or already instantiated input
exists; it does not mean the physical calculation has been executed.
`PLAN-DELIVERABLE` means the governing plan assigns the construction but its
object is not present. `ABSENT` means the searched sealed stock contains no
appointed executable definition/object.

Plan pins used in the table:

- D2: `THE_PLAN_TO_ALPHA_AND_GRAVITY_V003.md[3304,3416)`, span SHA-256
  `46c3b926c1889be07d393ebb9a1a57608d14574f8751d455bfe6d3af5a047aaf`.
- F0–F4: same file `[3989,5331)`, span SHA-256
  `fccbd6acc2c8587695ce8400e59a6f41c10eab4b8f9a115b44508611d63de940`.

| Link | Object or predicate | State | Pin / owner |
|---:|---|---|---|
| 1 | induced-only/current-carrier conditional branch, with `k_R` floor | EXISTS | D03 |
| 2 | normalized `Gamma_K` functional/measure/domain schema | EXISTS | D04 |
| 3 | completed on-shell `Gamma_K` instance on the admitted branch | PLAN-DELIVERABLE | Plan F3b via the F0-pinned chain; D14/D15 show it is not an existing producer |
| 4 | stationary-cell `X_K` and conjugate-energy schema | EXISTS | D05 |
| 5 | completed same-branch stationary `X_K` instance | PLAN-DELIVERABLE | Plan F3b; D05 is schema only |
| 6 | BR operator/domain/spectrum/opening schema | EXISTS | D06 |
| 7 | completed BR operator, spectral map, opening and isolated-next-mode instance | PLAN-DELIVERABLE | Plan F3b; D06 states the required producer |
| 8 | abstract scalar residual and unique-simple-positive-root schema | EXISTS | D07 and D09 |
| 9 | one appointed executable `C_record(K)` formula derived from the complete on-shell problem | ABSENT | D09 expressly finds no current appointment |
| 10 | enumerated admitted members/equivalence test for all five mutation channels | ABSENT | D08 names the classes; D16 finds no executable member sets |
| 11 | mutation/uniqueness-gated solve and independent reproduction of `K_*` | PLAN-DELIVERABLE | Plan F3b; D08 fixes the order |
| 12 | `LOCAL-SHADOW` to physical-carrier bridge (LP-JII discharge) | ABSENT | D13 says S16 cannot be filled while it stands |
| 13 | complete downstream charged `Q_spec`, including C7's nine slots | PLAN-DELIVERABLE | Plan D2; D11/D12 define the demand; current content is 0/18 |
| 14 | `Gamma_Q`, transverse response, threshold matching, and Thomson-limit extraction | PLAN-DELIVERABLE | D2/S13/S16; D11 and D12 |
| 15 | derived statement/proof connecting `K_*` to `kappa_Thomson` | ABSENT | D13 preserves a transport obligation, but no sealed equality/identity theorem was found |
| 16 | alpha assembly only after the preceding source is lawfully transported | PLAN-DELIVERABLE | Plan F3c; no assembly executed here |

### 3.1 D2 nine-slot cross-reference

| C7 slot | Defining-chain intersection |
|---|---|
| S03 dynamical U(1) action | Link 13, complete charged `Q_spec` |
| S04 gauge fixing, ghosts, gauge edge modes | Link 13 |
| S05 normalized interacting CTP amplitude | Links 13–14, source of `Gamma_Q` |
| S06 parent-derived regulator and finite renormalization | Links 13–14 |
| S07 transversality and photon-mass exclusion | Link 14 |
| S08 Lorentz- and packing-independent response | Link 14 |
| S13 interacting pole or infraparticle threshold | Link 14, fixes S16's condition without reverse selection |
| S16 threshold-conditioned Thomson matching | Links 14–15 |
| S17 interacting outgoing-sector descendant test | Post-match check after links 14–15 |

D12 records every one of these nine slots absent and the Q-spec at 0/18. No
later slot may select an earlier one.

### 3.2 Q-691 14-item remainder custody finding

The cleanroom register pin available to this lane ends at Q-685. Exact and
variant searches for `Q-691`, `14-item`, `fourteen-item`, and the purported
item-10 language returned no sealed Q-691 remainder artifact in the searched
stock. Therefore:

- a faithful line-by-line cross-reference of the fourteen items is
  **ABSENT OF CURRENT CUSTODY** and is not reconstructed;
- the relay's description of item 10 is treated as a hunt target, not sealed
  evidence;
- the hunted `K_*`/`kappa_Thomson` identity is link 15, and its sealed statement
  was not found;
- the unrelated older “14 steering objects” and other files' “item 10” strings
  were rejected as false positives.

This custody gap does not erase D2/C7 or the independently sealed transport
obligation. It prevents claiming that all fourteen Q-691 items were
cross-referenced.

## 4. AS3 — three stiffness types and the required relation

| Object | Sealed type | Role on the alpha path |
|---|---|---|
| `K_*` | unique simple positive **cell-level onset root** of the `Gamma_K`/BR stationary closure problem; a local induced-response surrogate under the named branch | Q-34 says this, not `kappa_record`, is alpha's upstream stiffness object |
| `kappa_record` | completed-chain primitive public-record **intensive Hessian/susceptibility** | a distinct record-side output; Q-62 places it off alpha's value path |
| `kappa_Thomson` | complete physical charged sector's finite path-independent **low-momentum transverse stiffness** | only this downstream object may enter the physical alpha expression in V011 |

**CLAIMED relation finding:**

1. D11 seals the older exact statement `kappa_record=kappa_Thomson` and says it
   may not be assumed: the complete amplitude must derive it or the route fails.
2. Q-34/D01 later re-poses the upstream source to `K_*`; D13 preserves
   `K_* -> kappa_Thomson` as a transport obligation and says it is neither
   discharged nor weakened.
3. No sealed authority in the searched stock states or proves
   `K_*=kappa_Thomson`. An arrow/transport obligation is not an equality proof.
   No producer mapping was promoted into one.

A valid derivation of the re-posed relation would consume: a completed and
uniquely gated `K_*` root (links 3–11), the missing local-shadow-to-physical
carrier bridge (link 12), the complete D2/C7 charged specification and its
derived spectrum/thresholds/decoupling/matching (links 13–14), and a theorem
comparing the transported source with the low-momentum coefficient. Those are
typed dependencies only; none was executed here.

## 5. AS4 — exact-rationality typing only

**CLAIMED:** the defining form is **continuous-data**, not a ratio of counts or
integers by construction. It is a root of an as-yet-unappointed scalar residual
of a functional/boundary-value problem. Its admitted data include geometry,
clock, measure, regulator, action partition, state/domain, spectrum, duration,
and the matching floor. The defining predicates `C_record(K_*)=0`, positivity,
simplicity, and uniqueness do not impose rationality.

Consequently exact rationality itself remains undecidable until the missing
executable residual and inputs exist. That is a statement about the displayed
definition's type, not an evaluation of any value.

## 6. AS5 — F0 verdict, freedoms, and flattening

### 6.1 F0 verdict

**CLAIMED: PARTIAL.** The abstract computand is defined, but four load-bearing
links are absent: the appointed executable `C_record(K)` formula, enumerated
mutation-family members, the physical-carrier bridge, and the derived
`K_*`/`kappa_Thomson` relation. The Q-691 remainder artifact is additionally
absent from this lane's current custody and therefore cannot supply the last
item by implication.

### 6.2 Freedoms consumed

```text
new branch selected                         = false
executable C_record formula selected        = false
carrier/state/measure content authored      = false
mutation-family membership authored         = false
energy prescription selected                = false
K_* / kappa identity assumed                = false
root or physical quantity evaluated         = false
Q-691 remainder reconstructed               = false
```

The report consumed only the freedom to classify and cross-reference sealed
spans under the relay's evidence-hunt scope.

### 6.3 Flattening check against `DECLINE_REGISTER_V002.md`

The decline register verified at
`957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a`.
No route was flattened across these controlling entries:

- S21 `[8832,9218)`, span SHA-256
  `9115a21a564d328775b358f0e87836aaccf5091c4e1c785a5d5c330ceeb2a73a`:
  no Misner-Sharp/Brown-York energy was chosen; the conjugate energy remains a
  derivation demand.
- S23 `[9576,9927)`, span SHA-256
  `aa9450afbced119f3aceef3f5c724119e1190f28f90932f2fbe0fd85faedaa13`:
  flux quantization was not re-proposed as a stiffness selector.
- S28 `[11323,11716)`, span SHA-256
  `b9fd3b08d7865905f21bd36bd976ab8fab8c9c1a4a419a7a8854dd2255c935f6`:
  the five free `D_BR` data classes remain unselected and are not constrained
  after comparison.
- S30 `[12110,12591)`, span SHA-256
  `313f6fd764de0df90e7f550bf08bb70ba0694e408f69b75b6b0e818607368048`:
  the conditional Hessian-first route was not invoked or generalized.

The retired mass-ratio selector, phase candidate, scalar projection, and
declaration-as-producer routes likewise remain in their recorded dispositions.

## 7. Battery and self-audit

- `F_PLDEC`: **CLEAN**. No physical quantity was numerically evaluated; no
  comparison to a measured constant occurred.
- M-2: **CLEAN** under the four search modes stated in §1.3; the Q-691 false
  positives were rejected rather than merged.
- Jurisdiction: all headline determinations are marked **CLAIMED**. Quoted
  authorities retain their own status; this lane does not register or rule.
- Gates: `alpha_computed=false`; `proof_authorized=false`;
  `kappa_record_computed=false`; no member binding, fixed-point execution, end
  test, or chain invocation occurred.
- Verb audit: “defines,” “requires,” and “rules” report pinned text or the
  displayed classification. “Would consume” is dependency typing, not proof or
  execution. No authorization or physical success is claimed.

SEARCHED = `**/*.{md,json}` under the scoped cleanroom glob in §1.2 (1787 files)
DEFINITION_SPANS = 16 (cited)
CHAIN = 16 links: 5 EXIST / 7 PLAN / 4 ABSENT (executable C_record formula; mutation-family enumeration; physical-carrier bridge; derived K_*/kappa_Thomson relation)
KAPPA_RELATION = located (typed; K_*/kappa_Thomson equality statement absent)
RATIONALITY_TYPING = continuous-data (not ratio-by-construction; exact rationality undecidable before missing links are instantiated)
F0_VERDICT = PARTIAL (absent links: executable C_record formula; mutation-family enumeration; physical-carrier bridge; derived K_*/kappa_Thomson relation)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (all headline determinations CLAIMED; no physical value or proof claimed)
