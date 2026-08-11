RELAY 992 | LANE: DARIO | BLOCKED -- SUBJECT ABSENT

INBOX    relay_inbox/RELAY_PASTE_992_AUDIT_V002_CHECK_DARIO_V001.md
         572c82e0c05b757013db83f371971259b75e292807929db5cca94272ba5501ab  (verified BEFORE reading)
MISSING SUBJECT
         workspace/STAGE8_DESC_AUDIT_CODEX2_V002.md            -- not present
         workspace/STAGE8_DESC_AUDIT_CODEX2_V002.md.seal.sha256 -- not present
SUBJECT_DIGEST = UNAVAILABLE.  Nothing was read and no digest is reported for an object I did not
         verify.

THE RELAY'S OWN BLOCKED GUARD FIRED, as its first step: "if the subject is absent in workspace/,
  write relay_outbox/992_BLOCKED.md and STOP."

ABSENCE CONFIRMED BY SEARCH, NOT BY A SINGLE ls -- the same discipline as at 988, and for the same
  reason: a shallow check misreports a mirroring delay as a missing artifact, and the two call for
  different registrar actions.
    1. exact path in workspace/                       -> absent (file and sidecar both)
    2. archive-wide "*DESC_AUDIT*", builder-A excluded -> FOUR hits, and every one is V001-era:
                                                         STAGE8_DESC_AUDIT_CODEX2_V001.md + sidecar,
                                                         STAGE8_DESC_AUDIT_CHECK_DARIO_V001.md + sidecar
                                                         (the latter is MY 988).  NO V002 anywhere.
    3. workspace listing "STAGE8_DESC*"                -> five artifacts, all accounted for: the audit
                                                         V001, my 988 check of it, the demand check,
                                                         and my demand V001/V002
    4. newest workspace artifacts                      -> my 989 V002 is the most recent; the newest
                                                         opposite-lane file is the DEMAND check, not a
                                                         corrected supply map
    5. relay_outbox 990-992                            -> empty; no 990/991 traffic of mine
  READING: consistent with the opposite lane's corrected audit not yet being written or not yet
  mirrored.  I do NOT rule on which.  Whether V002 is unwritten, unsealed, or written-and-unmirrored
  is the registrar's fact to state, not mine to infer from an absence.

WHAT I DID NOT DO, deliberately:
  - I did not substitute STAGE8_DESC_AUDIT_CODEX2_V001.md as the subject.  The relay names V002 and
    asks for THE DELTA -- the fold of my own 988 findings.  Checking V001 again would answer a
    question nobody asked and would silently re-verify work already checked.
  - I did not reconstruct the expected delta from my own 988 and report on it.  That would be
    checking my own findings against themselves, which the relay expressly excludes ("you check the
    FOLD, not your own findings"), and it would be an unearned verdict on a document I have not seen.
  - I did not write workspace/STAGE8_DESC_AUDIT_V002_CHECK_DARIO_V001.md.  The output name remains
    CLEAR for the relay when it is re-issued.
  - I did not run chained pickup.  The guard says STOP, and the chain fires on a DONE, which this is
    not.

TO UNBLOCK: mirror STAGE8_DESC_AUDIT_CODEX2_V002.md and its sidecar into workspace/.  Relay 992 then
  runs exactly as written, with the subject verified against its own sidecar and its digest recorded
  per the chained-custody clause.  Nothing in the assignment needs changing.

STANDING NOTE FOR THE MORNING PROCESSING -- this lane's descent-section artifacts are all sealed and
  reported, so the section's demand half and the audit cross-check are both on the record:
    986  STAGE8_DESC_DEMAND_DARIO_V001.md        da32dc9dfff38a32...  (superseded by V002)
    988  STAGE8_DESC_AUDIT_CHECK_DARIO_V001.md   bf3d07ec1ea93339...  (CORRECTED; spine stands,
                                                 six moves -- the deltas 992 was to check)
    989  STAGE8_DESC_DEMAND_DARIO_V002.md        c883d3732af61800...  (35 conditions + 1
                                                 verdict-relative; reading of record)

GATES HELD: alpha_computed=false; proof_authorized=false; kappa_record_computed=false.  BLIND held.
  JOINT_ANCHOR_DERIVED = false.  PE-1..16 pointer-only.  Nothing read beyond seals, nothing adopted,
  nothing registered, no register/plan/tracker/git action.  Builder-A code untouched.

CHAIN_INVOKED = false
STATUS = BLOCKED, STOPPED CLEANLY
