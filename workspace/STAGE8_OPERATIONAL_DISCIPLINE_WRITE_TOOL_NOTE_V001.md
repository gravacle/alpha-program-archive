# Stage-8 Operational Discipline — Artifact Authoring Instrument V001

Date: 2026-07-26

## Status

```text
STANDING_OPERATIONAL_DISCIPLINE_SEALED
```

Adopted on Brian's operational directive (binding this session and all
future ones), recorded alongside the real-component precondition rule.

```text
1. Every artifact (.md, .json, specs, records, transcripts) is CREATED
   with the Write tool and MODIFIED with the Edit tool.
2. Bash is reserved for what genuinely needs a shell: shasum, git,
   find, grep, running scripts.
3. Shell redirection (`cat >`, `cat >>`, `tee`, `>`) is NEVER used to
   author an artifact.
```

Rationale of record: (i) the Write/Edit instruments carry the session's
standing approval boundary, removing unattended-operation prompts
without loosening any permission; (ii) `cat >` silently truncates its
target — the wrong default instrument in an append-only workspace
holding sealed artifacts. This is an instrument change only; every
approval boundary stays exactly where it is.

## Protected status

```text
alpha_computed = false
proof_authorized = false
```
