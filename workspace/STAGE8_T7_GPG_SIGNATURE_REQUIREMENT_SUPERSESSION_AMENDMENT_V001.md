# Stage-8 T7 GPG Signature Requirement Supersession Amendment V001

Date: 2026-07-25 (evening)

## Status

```text
APPEND_ONLY_AMENDMENT_BY_PRINCIPAL_DECISION
```

This amendment supersedes every GPG-signing requirement in the sealed
Phase-A execution binding (6fa8845a…) and sealed implementation repair
binding (dc7cdd15…). Neither sealed document is altered. This is a
genuine principal decision made by Brian and relayed for sealing; it is
not a lane decision.

## Grounds: the sealed requirement is impossible, not inconvenient

The pinned disclosure key

```text
18488605D44F65A9B57B610AA5F3A86512A04D61
```

cannot sign: its passphrase is unrecoverable (searched: all session
transcripts, macOS keychain, all Memory Bank repos, all memory files; no
record of key generation or passphrase). The key predates this program
(created 2026-05-05 for Memory Bank security disclosure). The secret key
is present but unusable. A supersession is therefore forced regardless
of any preference.

Timing fence: this impossibility was discovered PRE-PRODUCTION, with
zero production values, receipts, or outputs in existence (the archive
anchor commit 1ec83f3 and the absent-outputs verification in the round-2
review record both witness this). The change cannot be outcome-shaped.

## Superseding requirements

1. EXTERNAL ANCHORING PER ARTIFACT: after each production receipt or
   sealed output is written, its digest is committed and pushed to the
   archive repository github.com/gravacle/alpha-program-archive BEFORE
   the next lane runs. Third-party timestamping replaces self-signing.
2. RECORDED PRINCIPAL AUTHORIZATION: production launch is gated on an
   explicit typed authorization from Brian, recorded in an append-only
   artifact and pushed before the first lane runs.
3. APPEND-ONLY ANCHOR BY ENFORCEMENT: the archive repository is being
   made public with force-push protection on main, so anchor history is
   append-only by GitHub's enforcement rather than by convention.
4. PRE-FLIGHT RULE (audit lesson, generalized): every fail-closed
   precondition of a production run — push capability and remote
   reachability included — must be pre-flighted BEFORE any canonical
   output path is consumed. A controller that can fail a precondition
   only after sealing an immutable output is non-conforming.

## Recorded rationale

A signature from a key held by the audited party, on the same machine as
the workspace, adds little over a third-party timestamp. The guarantee
the program actually needs is ordering — the artifact existed before the
result was known — and only external anchoring provides that.

## Scope

No numerical, analytic, carrier, threshold, or verdict requirement is
touched. The receipts themselves, their adjacent seals, immutability,
lane ordering, and every comparator gate remain as sealed (subject to
the separately sealed repair-binding successor). Requirement rows
referencing GPG signing in the two sealed bindings are void as
superseded; all other rows stand.

## Protected status

```text
actual_parent_regulated_CAR_operator_response_derived = false
route1_special_case_reexecution_passed = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
