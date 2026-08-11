RELAY 995 | LANE: DARIO | DONE

INBOX    RELAY_PASTE_995_DEMAND_V004_DARIO_V001.md
         542e579f9ed98cfee3d03656c0d7e26f3594cdd9da83c4ea9aebd66f7700d1d7  (verified BEFORE reading)
SUBJECTS V003 fbf76d210bfc0981...  VERIFIED;  check ba67264055f9191e...  VERIFIED
OUTPUT   workspace/STAGE8_DESC_DEMAND_DARIO_V004.md
         bed63c314a779b499fe5c7aaae46221f32fa6255778d9a6a7bb0f597c48e880e   53,232 B
         workspace/build_v004.py  110006d42079cb705fefd4d9e1b9f07658920ad5b9e94656e076964e9ed17e93
SEAL     both sealed; shasum -c: OK.  Name CLEAR.  Closure byte 0, ends 7279 (fixed point).
         Scan 0 hits.  SCOPED grep: 16 members; conditions contiguous 1..36.  Zero placeholders.

ALL FOUR CUSTODY ITEMS FOLDED IN ONE PASS.  NOTHING LEFT FOR A FIFTH.

(1) DIFFS = REPLAYED-AND-CORRECT, and I found the cause rather than just adopting the numbers.
    V001->V002 = 2/372/347 ; V002->V003 = 10/158/38 ; V003->V004 = 7/183/16 (fixed point).
    ALL REPLAYED BY ME WITH GNU `diff -u` AGAINST THE SEALED BYTES immediately before sealing, and the
    first two reproduce the check's values INDEPENDENTLY.
    THE CAUSE: V003's certificate NAMED "GNU unified, 3 context lines" and COMPUTED with python
    difflib.unified_diff, which emits larger change blocks -- 457/422 and 160/39 on the same files.
    THE CONVENTION AND THE COMPUTATION DISAGREED.  That is precisely a certificate of memory rather
    than of the files, which is what this pass existed to remove, and I put the diagnosis in the
    artifact rather than silently swapping the digits.

(2) METHOD = REPRODUCIBLE.  V004 is built from sealed V003 by NAMED REPLACEMENT ONLY via
    build_v004.py, reproduced VERBATIM at section 6.6 and SEALED ALONGSIDE the artifact.  Replay:
        shasum -c STAGE8_DESC_DEMAND_DARIO_V003.md.seal.sha256 && python3 build_v004.py
    Each of the nine replacements ASSERTS ITS TARGET IS PRESENT EXACTLY ONCE before applying, so a
    drifted source ABORTS the build instead of silently producing a different file.  "Byte-carried" is
    now a property a third party can re-derive, not a claim I make.

(3) SET_CLAIM = EXACT.  V002->V003 = 13 RETAINED / 7 ADDED / 1 DROPPED by set comparison, and the drop
    is the 989 assignment REPLACED by the 993 assignment.  So V003's "nothing removed is TRUE at the
    set level" WAS FALSE A SECOND TIME and is WITHDRAWN.  Stated exactly: V002->V003 replaced one row
    and added seven.  V003->V004 = one row REPLACED (993 -> 995 assignment), two rows EXTENDED,
    nothing else dropped -- declared in advance this time rather than discovered afterward.
    THE PATTERN IS WORTH NAMING: I have now claimed "nothing removed" twice and been wrong twice, both
    times because I checked the CONDITION level and asserted at the SET level.  The fix is not more
    care, it is computing the set delta before writing the sentence, which is what V004 does.

(4) MEMBER01 = REHASHES.  The declared path resolved from the ARCHIVE ROOT while every other member
    resolves in workspace/, so the row addressed nothing for a reader anchored at the artifact.  Fixed
    by adding an explicit PATH_RULE to the closure -- unqualified names resolve in workspace/,
    root-anchored names at the archive root -- and root-anchoring member 01.  VERIFIED BY REHASHING:
    <archive-root>/relay_inbox/RELAY_PASTE_995_... -> 542e579f9ed98cfe..., matching the assignment.

SUBSTANCE = BYTE-CARRIED (invocation-verified).  The 36 rows, their grounds, the six folds and the U12
    full span carry byte-identical from V003.  U12 CONFIRMED and the register decline RULED RIGHT by
    the check; neither is reopened.

INTEGRITY SWEEP RUN AT PICKUP, unprompted, because several of my sealed artifacts were reported
    modified this turn: all nine (demand V001/V002/V003, the two DESC checks, 983, 981, 978, 977)
    still verify against their sidecars.  No custody event; recorded so the registrar does not have to
    re-run it.

GATES HELD: alpha_computed=false; proof_authorized=false; kappa_record_computed=false.  BLIND held;
    every scale symbolic.  JOINT_ANCHOR_DERIVED = false travels.  PE-1..16 pointer-only.  Builder-A
    code untouched.  NO construction, no candidate, no supply call, no selector exercised.  V001-V003
    remain sealed and on the books; V004 supersedes them as the demand reading of record.  Nothing
    adopted, nothing registered, no register/plan/tracker/git action.  ALL CLAIMED until the
    opposite-lane check; the step to press first is the BUILD SCRIPT ITSELF -- it is now part of the
    evidence, so it should be read as such: if any of its nine replacement targets is wrong, the build
    aborts rather than misbuilding, but a target that is right and a REPLACEMENT that is wrong would
    still pass.  The replacements, not the assertions, are the thing to check.

CHAIN_INVOKED = false
