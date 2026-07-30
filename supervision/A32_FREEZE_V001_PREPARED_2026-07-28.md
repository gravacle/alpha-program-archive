# A32 HOLDOUT FREEZE — V001, PREPARED (2026-07-28T22:55Z) — NOT RATIFIED, NOT SEALED

STATUS: PREPARED IN ANTICIPATION and immediately RE-STATUSED: the principal directed
one-decision-at-a-time ratification before any seal act. The reviewer lane had read the
principal's "accepting the recommendation" as ruling all four decisions; that reading was
broader than the words and is withdrawn. NO sidecar was written, NO relay paste was sent,
NO flag was claimed, and CONTINUATION_STATE was not updated with any ratification claim.
This file now serves as the prepared template; each of the four decisions below becomes
RULED only upon the principal's explicit per-item ruling, and the seal act follows the
final ruling. This instrument supersedes A32_FREEZE_DRAFT_V000_2026-07-28.md (which remains on disk,
append-only history). Ladder-grade flag flips are NOT claimed (independent evaluator
unimplemented, RD-22 NOT AUTHORIZED); the five drafting flags remain false until the
construction lane writes the V011 freeze fields and the collector executes. SPEC-SEAL
becomes ATTAINABLE, not attained. alpha_computed = false; proof_authorized = false.

## Ratification provenance

- Ruled by: Brian Mulconrey (principal), 2026-07-28, session e268883f, upon the four-question
  ruling set. Ruling words, verbatim: "I'm good with accepting the recommendation. We
  obviously don't want to copy values just because we think they will fit. We want to
  derive them."
- Antecedent record, hashes pinned (all written BEFORE the ruling):
  13faf0bc9a455590bd99d1a40587d798bc558e87aa1d1bc6dcf6778731138123  A32_FREEZE_DRAFT_V000_2026-07-28.md
  5185ad0f5e7097fe0e0886e61771fc57e49f169f034cc52cc7c9bf11543c07ea  A32_SIX_ITEM_PROPOSALS_2026-07-28.md
  224faead2c9431b9d0a2c66c2de8e205c89ceb0a9840afb32d8e29d4b0b47eba  A32_RATIFICATION_DECISION_SHEET_2026-07-28.md
- The principal's challenges and their resolutions precede the ruling in the record: the
  correlation-ceiling refinement was WITHDRAWN on the principal's objection (proximity is
  not lineage; the theory's discriminating signal is expected on alpha's geometric surface);
  exclusion is DATA-LINEAGE ONLY, exactly as sealed (V011:1985-1990).

## The thirteen mechanical items

Ratified AS WRITTEN in A32_FREEZE_DRAFT_V000_2026-07-28.md (lines 21-58), incorporated here
by the pinned hash above. Count correction of record: THIRTEEN items, not twelve.

## The six principal items — RULED

1. REGISTRY / API SOURCE: the NIST CODATA recommended-values table, 2022 adjustment, as one
   fixed-vintage machine-readable artifact (canonical ASCII table at
   physics.nist.gov/cuu/Constants/Table/allascii.txt, or the equivalent versioned JSON if
   the collector verifies it as the canonical form), retrieved once by the collector, full
   raw bytes hashed, T_cutoff = the 2022 adjustment vintage. Exclusions are LINEAGE-ONLY
   per the sealed eligibility rule: the alpha datum and its deterministic re-expressions
   (values computed from the alpha measurement rather than independently measured). NO
   correlation ceiling; NO proximity exclusion — alpha-adjacent independently measured
   observables are eligible and are the expected home of structure-sensitive candidates.
   DISCLOSURE (rule-free): CODATA adjusted values presume standard-theory relations among
   constants; this leans conservative (against the theory) and is disclosed rather than
   patched.
2. EXTERNAL RANDOMNESS BEACON: drand (League of Entropy) mainnet PRIMARY — round number
   computed deterministically from the frozen genesis time and period, first round strictly
   after PREDICTION-MAP-SEAL; value = the round's randomness, hex, parsed verbatim.
   FALLBACK, predeclared, no discretion: NIST Randomness Beacon v2 pulse at the first whole
   UTC minute after the same seal instant if the drand round is unretrievable from all
   frozen mirrors for 24 hours; both unavailable 72 hours = FAIL CLOSED, no third source.
   Collector verifies and records exact chain hash, genesis, period, and mirror list at
   freeze execution, before PREDICTION-MAP-SEAL; later drift = fail closed.
3. SAME-ALPHA COMPARATOR CLASS: published standard-theory (QED/SM) expressions, citable
   BEFORE candidate-universe construction, evaluated with the identical alpha input under
   the frozen convention alpha(0) = 1/(4 pi kappa_Thomson), perturbative order FROZEN PER
   FORMULA at preregistration, no candidate-specific fitted parameter, refit, channel
   coefficient, or post-selection. No published expression = that candidate ineligible.
4. CALIBRATION RULE: as drafted, unchanged — identical alpha input and identical candidate
   metadata for BID and comparator; refit / channel-specific coefficient / post-selection
   renders the comparator ineligible FOR THAT CANDIDATE.
5. DISTINCTNESS THRESHOLD: D >= 5, with
   D = |mu_BID - mu_comp| / sqrt(sigma_BID^2 + sigma_comp^2 + sigma_meas^2) after unit
   conversion and covariance projection; singular covariance fails eligibility unless a
   projection rule was frozen beforehand. AN EMPTY ELIGIBLE SET FAILS CLOSED; D is never
   renegotiated after any set size, prediction, or value is seen.
6. OBSERVABLE FAMILY: ALL machine-enumerated registry candidates satisfying the five sealed
   eligibility conditions (V011:1983-1993) and computability under the frozen
   prediction-map interface. NO human subfamily may be carved out after registry
   collection.

## Ordering and third-party verifiability

This freeze precedes SPEC-SEAL, candidate-universe construction, prediction generation,
beacon evaluation, and any alpha evaluation (V011:1953-1968, :1995-1998; sealed restatement
in the Gate5 battery spec :55-61). At ratification, the five drafting flags
(holdout_registry_source_query_cutoff_frozen, holdout_randomness_beacon_frozen,
structure_sensitive_holdout_available, holdout_universe_sealed, prediction_map_sealed) are
ALL STILL FALSE — a third party can verify from these that the freeze preceded everything
downstream. RD-36 timing rule honored: COMMIT then EXECUTE.

## Remaining acts, assigned

- CONSTRUCTION LANE (relay paste 114): write these six rulings into the V011 specification
  bundle's freeze fields (V011:1953-1968 list) so H_spec can eventually bind them; index
  this ruling in STAGE8_LANE_STATUS.md in the same act, citing this file and its sidecar
  hash. The reviewer lane does not write to the workspace.
- COLLECTOR (fresh context, later): execute mechanical items 1-8 against the ruled registry;
  custodian commitments per item 9. The collector is the FIRST process to touch registry
  bytes.
- EVALUATOR (blocked, RD-22): ladder-grade flag computation remains unavailable and is not
  simulated.

Not sealed as ladder authority. Sealed as the principal's ruling of record, sidecar in the
same act. alpha_computed = false; proof_authorized = false.
