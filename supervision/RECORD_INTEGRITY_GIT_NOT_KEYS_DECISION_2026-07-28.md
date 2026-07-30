# RECORD-INTEGRITY MECHANISM: PUBLIC GIT, NOT KEY CUSTODY — DECISION OF RECORD (2026-07-28)

RULED BY THE PRINCIPAL, 2026-07-28 night, session e268883f — AND THIS IS A RE-MADE
DECISION. The principal states it was made previously ("We discussed the fact that I did
not want to be wrestling with PGP keys and agreed... to use git to keep the project
recorded with git deploy information. We're deploying to a public git repository."). It is
documented THIS time, at his direction, precisely because the earlier making of it went
unrecorded and it came back for re-litigation. The reviewer lane had re-offered an
encryption option in ignorance of the prior ruling; that offer is WITHDRAWN.

## The ruling

1. The project's integrity/timestamping mechanism is PUBLIC GIT DEPLOYMENT: artifacts are
   committed with descriptive messages and pushed to the public repository
   https://github.com/gravacle/alpha-program-archive.git. The public commit history is the
   third-party-verifiable record of WHAT existed WHEN. No PGP/GPG key custody is required
   of the principal, ever.
2. Applied to the A32 custodian question (this resolves the open custodian-hardening item;
   no encryption layer): 
   - The PUBLIC A32 collection artifacts (candidates.jsonl, commitments.jsonl, flags.jsonl,
     duplicates/exclusions, collector_v001.py, transcript.md, and raw_allascii.txt or its
     recorded hash) are committed and pushed to the public repository. The pushed
     commitments.jsonl is the outcome-mask commitment of record: later payload tampering is
     detectable against it, with the push timestamp as the third-party clock.
   - custodian_private/custodian.jsonl STAYS OUT of the repository (untracked, never
     committed). Rationale: the values are world-public anyway (CODATA); what A32 protects
     is PROCESS blindness — no lane looks — enforced by discipline plus the pre-unmasking
     contamination audit (mechanical item 11), with the public commitments supplying
     tamper-evidence. Publishing the private file would add nothing and would blur the
     lane-access line the contamination audit checks.
3. This supersedes, for this program, any plan requiring detached signatures. Corroborating
   record: the SP14 content-addressed runtime gate lineage FAILED CLOSED at its required
   GPG detached signature ("GPG signing failed: Inappropriate ioctl for device", rerun
   prohibited, repair lineage never built). The program's working integrity layer has in
   practice been git push (Einstein's window: "sealed, mirrored, committed and pushed") —
   this ruling makes that the mechanism of record rather than an accident.

## Execution

Committing and pushing the a32_holdout public artifacts to the archive repository is
assigned to the construction/bookkeeping lane (Codex), queued for the next relay unless the
principal executes it sooner. .gitignore (or placement outside the repo tree) must exclude
custodian_private/.

alpha_computed = false; proof_authorized = false.

## ENFORCEMENT ADDENDUM (2026-07-29, principal's direction: "how do we make sure that there
## is a PUSH EVERY TIME THAT ONE IS NEEDED?")

The eleven paste-119 commits sat unpushed until caught by reviewer verification — proving
that "remember to push" is a permission, not a requirement, and permissions never force.
Three enforcement layers installed, structural first:

1. STRUCTURAL (cannot be forgotten): a `post-commit` hook in
   /Users/bgm/MB Work/alpha-program-archive/.git/hooks/post-commit auto-pushes on EVERY
   commit and, on failure, prints a loud banner naming the consequence ("COMMIT IS LOCAL
   ONLY, NO PUBLIC RECORD"). Installed and tested 2026-07-29 (fired on two test commits;
   verified push landed). NOTE: git hooks are LOCAL and NOT cloned — any new machine or
   fresh clone must reinstall it; a lane that commits from a different checkout is not
   covered.
2. CHECKABLE (one command, any lane, any time):
   `sh "/Users/bgm/MB Work/alpha-program-archive/deploy_status.sh"` — fetches and reports
   either "DEPLOYED — public record current at <hash>" or the exact number of unpushed
   commits / uncommitted changes. Committed to the repo (b1c857e) so it travels with the
   archive even though the hook does not.
3. PROCEDURAL (the backstop that caught it this time): reviewer verification of any
   construction return MUST check deploy state, not just working-tree cleanliness. "git
   status is clean" means the working tree is clean and says NOTHING about whether the
   public record exists. The check is `git status -sb` (ahead count) or the script above.

Standing instruction for every relay to a construction lane: the definition of done for any
artifact is SEALED, MIRRORED, COMMITTED, AND PUSHED — and the lane reports the deploy_status
output, not "git status is clean".
