# Stage-8 T7 Superseded-Chain Disarm Disposition V001

Date: 2026-07-26 (autonomous window)

## Status

```text
APPEND_ONLY_DISPOSITION — DISARM PROPOSED, PENDING PRINCIPAL AUTHORIZATION
```

The v005 verification (return sealed alongside) found ONE blocking
residual: discipline rule 3 ("a superseded production chain may never
remain launchable on the canonical paths") is closed for every route
THROUGH launcher v005, but the superseded launchers v002-v004 remain on
canonical paths, operational, and able to launch their own chains onto
the SAME canonical output paths (verified statically; the v003 chain's
full pre-flight passes today; the v002 chain retains the live GPG
defect class). One stale invocation would permanently poison the
canonical comparison path (append-only workspace).

## Why not fixed autonomously

Every byte-preserving mechanical disarm touches sealed-era state:
- quarantine (move) breaks the sealed manifests' path+hash row
  verification that immutability sweeps perform;
- mode changes (chmod 000) break the same sweeps' read access;
- editing the files violates append-only.
Per the discipline's own rule 1 corollary, the inability to disarm
within the no-touch constraint is itself the finding: it is
DISPOSITIONED here and escalated, not silently absorbed.

## Interim state (recorded honestly)

Until the principal authorizes a disarm, non-launchability of the
superseded chains rests on OPERATOR DISCIPLINE ONLY — exactly what the
re-audit's B2 said must not be relied on. Mitigations in force that ARE
mechanical: the v005 launcher cannot reach any superseded component
(exact set-equality fence, live-probed); the v005 pre-flight blocks on
any pre-existing canonical artifact, so a poisoning event is DETECTED
before v005 consumes anything (it cannot be silently built upon); and
this disposition plus the corrections note scope the launcher v005
docstring's over-broad claim ("unlaunchable mechanically") to
v005-route-only until the disarm lands.

## Proposed disarm (for Brian's authorization on return)

```text
QUARANTINE: git-style move of the superseded production entry points
  (launch v002/v003/v004; run_..._pipeline v002/v003/v004;
  compare v002/v003/v004) to scripts/superseded_quarantine/ preserving
  bytes and names, PLUS a sealed quarantine manifest recording each
  file's pre-move path and hash, PLUS an amendment to the immutability-
  sweep expectation: rows of sealed manifests v001-v003 whose paths are
  quarantined verify at the quarantine path via the quarantine manifest.
  The derive lanes and their tests (shared, live) are NOT quarantined.
  Effect: no superseded chain resolvable at any canonical entry point;
  every sealed hash still verifiable; append-only narrative preserved.
```

Alternative if Brian prefers zero file motion: a sealed standing
runbook prohibition plus a pre-flight sentinel design (rejected
autonomously because both rest on discipline, not mechanism).

## Protected status

```text
superseded_chains_mechanically_disarmed = false
alpha_computed = false
proof_authorized = false
```
