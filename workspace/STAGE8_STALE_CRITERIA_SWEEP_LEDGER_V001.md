# CODEX 2 — Q-? Stale-criteria sweep

`alpha_computed = false; proof_authorized = false; kappa_record_computed = false.`

## Lead finding

One **STALE-BLOCKING** acceptance surface is confirmed: the cross-sector metric-rule admissibility spec
still requires overdetermination as its falsifier/minimal-pass criterion, despite Q-65 refuting that as the
only forcing route and Q-76 striking it. This would reject a correct beta candidate whose existence and
uniqueness are derived.

## Scope and verified counts

Current cleanroom plus historical program and supervision roots; excluded `.git`, dependencies,
`external`, `third_party`, `node_modules`, `.proof_deps`, and `a32_holdout` including `custodian_private`
(never accessed). Review packets were discovery-only. Case-insensitive word-boundaried queries covered
`falsifier`, `minimal-pass`, `acceptance`, `gate`, `release`, `overdetermin`, `derived ground`, `generative`,
`formation`, `disjoint critical`, `bare existence`, and `admitted family`.

The supplied approximate counts do not reproduce under this bounded cleanroom search: 179 files contain at
least one acceptance/gate keyword and 7 contain `overdetermin`; counts depend on whether historical and
review artifacts are included. These are discovery counts, not acceptance-surface counts.

## Acceptance-surface ledger

| Surface | Criterion as written | Classification | Effect |
|---|---|---|---|
| `STAGE8_CROSS_SECTOR_METRIC_RULE_ADMISSIBILITY_SPEC_V001.md:265-267,292` | F3/minimal-pass item 3 demand a second independent overdetermining requirement; success described as determination of beta | **STALE-BLOCKING** | Rejects a correct candidate forced by derived existence + uniqueness alone. Replacement: require derived existence and uniqueness (plus current closure/fence tests), without an overdetermination bar. |
| `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:530-581` | Five-channel mutation audit; no inequivalent admitted root; no narrowing after root | CURRENT | Preserves current anti-fitting rule; does not rely on “only overdetermination.” |
| `STAGE8_SECTION53_ADMITTED_FAMILY_CENSUS_REACHABILITY_AUDIT_V001.md` | Pre-root census and provenance required | CURRENT | Sequencing constraint, not a struck physical premise. |
| `STAGE8_OPEN_ACTION_FORM_ADMISSION_TO_SECTION53_AUDIT_V001.md` | Concrete action-form mutations admitted; open classes unresolved | CURRENT | Descriptive status; does not embed a struck rule. |
| Q-65/Q-76 references in supervision/register artifacts | Historical “only overdetermination” framing | STALE-INERT | These record the refutation/strike and do not operate as live gates. |
| “no chain reaches derived ground” statements | Legacy graph descriptions | STALE-INERT where present | Q-64/Q-75 refuted the universal claim; no live gate may reject on it. |
| “two disjoint critical paths” | Historical path census | STALE-INERT | Q-75 refuted independence; descriptive records do not enforce it. |
| generative/formation binary | Historical framing | STALE-INERT | Q-90 established generative provenance and formation order can coexist. |
| bare-existence shortcuts | Legacy flags/diagnostics | STALE-INERT | Q-94 requires structure, not bare existence; already superseded as a live standard. |
| admitted-family enumeration | Open-class census material | CURRENT sequencing requirement | Q-124 withdrawal is later than this snapshot only where explicitly registered; no blanket live gate was found in this scope. |

## Replacement criterion for the stale blocker

The current forcing test is: a candidate passes the relevant structural gate when its required object exists,
its existence and uniqueness are derived under the pre-root admissibility/mutation audit, and no struck
overdetermination requirement is imposed. This is named only; no spec was edited and no candidate was scored.

`stale_blocking_count = 1 | TYPE-R | test: cross-sector F3/minimal-pass text versus Q-65/Q-76 register rulings.`
`other_surface_exhaustiveness = NO_VERDICT | TYPE-C | deciding evidence: a signed inventory of every live gate
with authority/version provenance; discovery sweep found 179 keyword-bearing files, not 179 gates.`

No repair, git, commit, push, gate, or deploy action was performed.
