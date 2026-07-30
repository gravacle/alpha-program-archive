# A32 MASKING DISPOSED: CUSTODIAN ACCEPTED WITH LIMITATION, COVARIANCE CLOSED BY EVIDENCE — PRINCIPAL DECISION, 2026-07-30

FINDABLE AS: **"A32 masking compliant"**, **"independent custodian"**, **"covariance not committed"**,
**"is the holdout sound"**, **"rule 9 deviations"**. Supersedes the open disposition in Q-24.

## THE RULING, IN TWO PARTS

**PART 1 — CUSTODIAN INDEPENDENCE: THE CURRENT ARRANGEMENT STANDS, WITH THE LIMITATION RECORDED.**

`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:2008-2011` rule 9 requires an "independent custodian" who
"attests that no payload was disclosed." `a32_holdout/collector_v001.py:301-326` does all of it in one
program and one run: salts from `/dev/urandom`, `custodian_private/custodian.jsonl` carrying payload AND
salt at mode 600, and the public `commitments.jsonl`. **Self-attestation cannot satisfy that clause.**

The commitments are NOT withdrawn and the holdout is NOT re-collected. **THE LIMITATION IS PERMANENT AND
MUST TRAVEL WITH EVERY A32 HEADLINE:** the concealment is cryptographically sound — `SHA256(salt ||
payload)` with 256-bit salts, fail-closed on short entropy reads — but **process independence between
collector and custodian was never established, and no independent attestation exists.** Any external
reading of rule 9 is entitled to that discount, and the program may not claim otherwise.

**PART 2 — COVARIANCE: CLOSED BY EVIDENCE. VACUOUS BY CONSTRUCTION.**

Rule 9 lists five payload fields; the collector commits four, omitting covariance. The concern was that
`D` is defined "after unit conversion and covariance projection" (`V011:2052-2058`), so an unbound
covariance could be supplied after a prediction exists — a post-hoc freedom inside the anti-post-hoc
mechanism.

**THE CHECK, RUN 2026-07-30 ON THE COLLECTOR SOURCE ONLY, NO CANDIDATE CONTENT READ:**

```
grep -i "covar|corr_matrix|correlation" collector_v001.py  ->  ZERO occurrences
parser fields (collector_v001.py:231-258):  name | value | uncertainty | units
```

**THE SOURCE FORMAT IS A FIXED-COLUMN TABLE CARRYING NAME, VALUE AND UNCERTAINTY. IT HAS NO COVARIANCE TO
COMMIT.** The payload omits covariance because none exists in the universe, not because the collector
dropped it. **The commitment binds everything the source supplies.** The spec over-specifies relative to
this universe; the collector does not under-bind it.

NO RE-COMMITMENT IS REQUIRED. Point (c) of Q-24 is closed with evidence rather than by assumption, which
was the condition of closing it.

## FORWARD CONDITION, AND IT IS BINDING

**THIS COLLECTOR CANNOT COMMIT A MULTI-COMPONENT OBSERVABLE.** It has no covariance field and no code path
for one. Therefore: **if the eligible universe is ever extended to vector or multi-component observables,
the collector must be revised and those candidates re-committed BEFORE any prediction exists.** Committing
a covariance-bearing candidate through the present collector would leave its covariance unbound, and that
would be the post-hoc freedom this check was run to exclude.

Recorded now because the eligible universe is not yet sealed — `provenance/bid_stage_subjects_v011.json:22-24`,
"No sealed HOLDOUT-UNIVERSE-SEAL immutable subject exists" — so extension is still possible and this
condition is live rather than hypothetical.

## WHY NOT RE-COLLECTION

Re-collection under a genuinely independent custodian was the only option producing a holdout that matches
its own spec, and it was available only in the present window, since a holdout committed late is VOID
rather than weaker. It was declined as disproportionate: the concealment mechanism is sound, the deviation
is one of process attestation rather than of cryptographic binding, and the covariance concern — the one
with teeth — dissolved on inspection. **The cost of the decision is that the independence limitation is
now permanent and inherited by FINAL-CLAIM.** That is stated here so it cannot later be discovered.

## SCOPE

- Discharges no slot. Zero of eighteen remain derived. Does NOT discharge or advance slot 18.
- Does NOT define "unused" — Q-23 remains open and is the next principal act.
- Does NOT seal the holdout universe, and does NOT convert A32 from ATTAINABLE to attained.
- Reads no candidate content and no custodian payload. `custodian_private/` was not read, listed, statted,
  hashed, or staged.
- Computes nothing; compares nothing to any measured value.

`alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`.
