# LANE CHANGE CUSTODY NOTE — CLAUDE CONSTRUCTION, V002 (2026-07-28)

Supersedes nothing; extends LANE_CHANGE_CUSTODY_CLAUDE_CONSTRUCTION_V001 (seal fc585326…)
append-only. Decision recorded by the reviewer lane at the principal's direction, session
e268883f, 2026-07-28 night.

## The decision

The Einstein window (Claude construction lane) is running out of usage credit. The
principal directed the migration; configuration adopted on the reviewer lane's
recommendation:

1. The CONSTRUCTION role held by the Einstein window migrates to FRESH SESSIONS on the
   Bohm account, run from a SEPARATE WORKING DIRECTORY —
   /Users/bgm/MB Work/construction_lane/ — so the construction sessions and the reviewer
   sessions share NO auto-memory namespace and NO conversational context. Same account is
   billing only; independence is carried by context isolation plus role separation, exactly
   as it was when Einstein and Bohm were both Claude on separate accounts.
2. Codex RETAINS construction execution in the workspace and ADDS mechanical
   coordination-as-bookkeeping (queue tracking, seal verification, relay carriage).
   Coordination-as-DECISION does not move: decisions remain the principal's, per the
   declared division of labor (construction = Codex, verification/independence = reviewer
   lane, decisions = principal).
3. The principal continues to hold the blind wall. Relays remain numbered pastes through
   the principal. The reviewer session (this one) remains REVIEWER-ONLY: it does not
   construct, does not write to the workspace, and does not grade its own work.
4. EFFECTIVE: upon receipt of the Einstein handoff dump (requested by paste 115). Until
   receipt, Einstein remains the construction window of record for its in-flight items.
5. The corpus precedent that reviewer-and-constructor in ONE CONTEXT is non-independent
   (Codex self-reviews, labeled NON_INDEPENDENT) is the binding constraint this
   configuration is designed around.

## Verification hooks

- Einstein handoff file expected at: MB Work/alpha_supervision/EINSTEIN_HANDOFF_*.md
  (paste 115 requests it, with in-flight state, open constructions, resume pointers).
- First construction session on the Bohm account must begin by writing a session-open note
  citing THIS file and its sidecar hash, from the new working directory.
- Any future audit reading only V001 gets a stale custody picture; V001 + V002 together are
  the chain.

alpha_computed = false; proof_authorized = false. This note assigns roles; it derives
nothing and seals no physics.
