# Stage-8 Real-Component and Precondition Discipline V001

Date: 2026-07-26 (early; adopted during the autonomous window)

## Status

```text
STANDING_DISCIPLINE_SEALED
```

Adopted on the external reviewer's root-cause finding (relayed by Brian
with the v004 re-audit NO-GO; recorded at /Users/bgm/MB Work/
alpha_supervision/EXTERNAL_REAUDIT_2026-07-26_fable_v004_return.md).
Four repetitions of ONE defect class occurred in one day: (1) GPG
signing capability checked after irreversible path consumption; (2)
comparator v003 bound manifest v002 while the frozen lanes stamp v001;
(3) launcher v003 could not launch the v004 comparator; (4) launcher
v004 cannot launch controller v004. In every case the repair logic was
correct and the plumbing failed identically: a precondition checked
after the irreversible step, or a rule enforced in a docstring while
the test drove a stub.

## The rule (binding on all successor work in this workspace)

```text
1. ANY change to an allowlist, manifest binding, executor row, or
   launch precondition MUST be covered by a test that drives the REAL
   component end to end. Never a fixture stub, never a monkeypatch,
   never a copied module. If the test cannot use the real component,
   that inability is itself a finding and must be dispositioned before
   sealing.
2. EVERY precondition of a production invocation must be verified
   BEFORE the first irreversible action (canonical path consumption,
   chmod-444 sealing, receipt writing). The preconditions must be
   ENUMERATED in the controlling artifact and the verification
   ordering PROVEN by the end-to-end test of rule 1.
3. A superseded production chain may never remain launchable on the
   canonical paths. Supersession of a pipeline component removes its
   launch route in the same change, mechanically — never by operator
   discipline or runbook.
```

Implementation instrument (this workspace): every production pipeline
controller carries a --preflight-only invocation mode that runs EVERY
enumerated precondition and exits before any canonical consumption; the
end-to-end startability test drives REAL launcher -> REAL controller
--preflight-only against the canonical workspace read-only, and its
recorded output is part of every verification artifact.

## Protected status

```text
alpha_computed = false
proof_authorized = false
```
