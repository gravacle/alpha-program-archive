STANDING RULE — LANES DO NOT COMMIT. THE REVIEWER COMMITS.

DATE: 2026-07-31. PRINCIPAL DIRECTION. Applies to every lane, permanently.
alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
rule_status = STANDING; effective relay 188. Supersedes the overnight seal-only protocol by making it permanent.

---

## 1. THE RULE

*** NO LANE RUNS ANY GIT COMMAND. THE REVIEWER IS THE SOLE COMMITTER. ***

```text
LANE DOES        write the artifact in the cleanroom
                 compute its .seal.sha256 sidecar and VERIFY it matches
                 mirror artifact + sidecar to alpha-program-archive/workspace/
                 report hashes and paths, and STOP

LANE DOES NOT    git add / commit / push / pull / rebase / reset / stash / restore
                 touch corpus_check_baseline_v001.json
                 run deploy_status.sh, or treat any deploy state as its concern
                 ask for publication authorization -- the reviewer verifies and publishes
```

**A lane MAY run `corpus_check.py --report` on its own artifact.** *** `--gate` IS NOT A LANE'S CONCERN AND
A RED GATE IS NEVER A REASON TO STOP WORKING. ***

---

## 2. WHY — FOUR COLLISIONS, AND A COST NOBODY WAS COUNTING

**Four shared-index collisions on 2026-07-30 and 07-31.** Nothing was lost — every artifact was sealed and
every seal verified — **but attribution corrupted repeatedly**: one lane's commit swallowed another's
staged register update, a commit title was rewritten to a different relay, and one lane nearly swept
another's in-flight work.

*** AND THE LARGER COST WAS LANE TIME. *** Lanes have been blocked at the gate, unstaging their own files,
restoring the index, waiting on baseline bumps, and asking for publication authorization. **None of that is
a lane's job, and all of it was competing with the physics.**

**Per-lane git worktrees were the other candidate fix.** *** THEY SOLVE PARALLEL COMMITS. WE DO NOT NEED
PARALLEL COMMITS — WE NEED PARALLEL WORK. *** Single-committer custody achieves the same isolation with no
change to any lane's working paths.

---

## 3. WHAT THE REVIEWER OWES IN RETURN

**Every artifact is verified before it is committed:** *** SEAL AGAINST THE STATED HASH, FENCE SCAN FOR
COMPUTED VALUES, AND THE ARTIFACT READ RATHER THAN THE REPORT. *** That last is not optional — twice a
lane's summary omitted a finding its own flag block contained, and both were caught only by opening the
file.

**The reviewer also owns:** the baseline, resealing it, gate repair, push conflicts, and rebases. **A lane
that reports a sealed artifact has discharged its obligation completely.**

---

## 4. WHAT DOES NOT CHANGE

**Nothing about the physics discipline.** Q-52 testability, Q-54 typing, Q-69's flag/discharge prohibition,
Q-76's disclosure, Q-80's new-class rule, Q-83's road justification, every fence, and the `sqrt(2)`
derived-never-chosen rule all stand exactly as written.

*** AND SEALING IS STILL THE LANE'S OBLIGATION. A LANE THAT REPORTS AN UNSEALED ARTIFACT HAS NOT FINISHED.
The seal is what makes single-committer custody safe: the reviewer verifies what the lane sealed, not what
the reviewer hopes it wrote. ***

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
