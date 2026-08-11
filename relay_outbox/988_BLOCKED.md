RELAY 988 | LANE: DARIO | BLOCKED -- SUBJECT ABSENT

INBOX    relay_inbox/RELAY_PASTE_988_AUDIT_CROSSCHECK_DARIO_V001.md
         a4d81898bc093349024b6aa5b11a64c2a219301d7f11572247bf54cc4cc0ca1a  (verified BEFORE reading)
MISSING SUBJECT
         workspace/STAGE8_DESC_AUDIT_CODEX2_V001.md          -- not present
         workspace/STAGE8_DESC_AUDIT_CODEX2_V001.md.seal.sha256 -- not present
SUBJECT_DIGEST = UNAVAILABLE (the file does not exist; nothing was read, and no digest is reported
         for an object I did not verify).

THE RELAY'S OWN BLOCKED GUARD IS WHAT FIRED, and it fired as its first step: "if the subject file does
  not exist in workspace/, write relay_outbox/988_BLOCKED.md naming the missing subject and STOP."

ABSENCE CONFIRMED BY SEARCH, NOT BY A SINGLE ls -- because a shallow check here would misreport a
  mirroring delay as a missing artifact, and the two call for different registrar actions:
    1. exact path in workspace/                     -> absent (file and sidecar both)
    2. archive-wide case-insensitive find "*DESC_AUDIT*", builder-A code excluded per standing law
                                                    -> ZERO hits anywhere in the archive
    3. workspace/ listing filtered to "STAGE8_DESC*" -> exactly one artifact, my own
                                                       STAGE8_DESC_DEMAND_DARIO_V001.md and its seal
    4. newest artifacts in workspace/                -> the most recent opposite-lane files are the
                                                       AXN-section checks (PINNING_CHECK, HOTHER_CHECK,
                                                       K4_PROVENANCE_CHECK); no DESC-section audit
    5. relay_outbox/ 984-988                         -> only my own 986_ACK and 986_DONE
  READING: this is consistent with the opposite lane's 985 audit not yet having been mirrored into
  workspace/ by the registrar, which the relay itself anticipates ("mirrored by the registrar on its
  DONE").  I do NOT rule on why it is absent -- whether the audit is unwritten, unsealed, undone, or
  written and unmirrored is the registrar's fact to state, not mine to infer from an absence.

WHAT I DID NOT DO, deliberately:
  - I did not substitute a different subject.  No DESC-section artifact other than my own exists, and
    cross-checking my own 986 would breach BUILDER-NEVER-VERIFIES in the plainest possible way.
  - I did not run the enumeration, status, classification, or stop-rule work against the audit's
    ABSENCE.  An audit cross-check whose subject is unavailable has no verdict to return; producing
    one from the section's other documents would be an unearned verdict, and over-claiming is worse
    than an honest kill and worse than an honest gap.
  - I did not write workspace/STAGE8_DESC_AUDIT_CHECK_DARIO_V001.md.  The output name remains CLEAR
    for the relay when it is re-issued.
  - I did not run chained pickup.  The guard says STOP, and the chain fires on a DONE, which this is
    not.

TO UNBLOCK: mirror STAGE8_DESC_AUDIT_CODEX2_V001.md and its sidecar into workspace/.  Relay 988 then
  runs exactly as written, with the subject verified against its own sidecar and the digest recorded
  in the report per the overnight-custody clause.  Nothing in the assignment needs changing.

STANDING NOTE FOR THE MORNING PROCESSING: my 986 is sealed and reported
  (STAGE8_DESC_DEMAND_DARIO_V001.md, da32dc9dfff38a32668b673e0c1b9e05fee27d02cd49b2f7ed99a78b71c51da9),
  so the demand side of the section is on the record and the basis list can assemble from both halves
  as soon as the audit lands.

GATES HELD: alpha_computed=false; proof_authorized=false; kappa_record_computed=false.  BLIND held.
  JOINT_ANCHOR_DERIVED = false.  PE-1..15 pointer-only.  Nothing adopted, nothing registered, no
  register/plan/tracker/git action.  Builder-A code untouched.

CHAIN_INVOKED = false
STATUS = BLOCKED, STOPPED CLEANLY
