PASTE 121 — CODEX
TO: Codex (primary construction lane). FROM: reviewer lane via principal. 2026-07-29.

SUBJECT: Deploy the A32 public collection artifacts — the last act still owed under the
record-integrity ruling.

WHY: RECORD_INTEGRITY_GIT_NOT_KEYS_DECISION_2026-07-28.md rules that the PUBLIC PUSH is
this program's integrity/timestamp mechanism, and assigns the A32 public artifacts'
commit+push to you. R-23 indexed their hashes in the register, but the FILES THEMSELVES ARE
NOT IN THE REPOSITORY (verified: no a32_holdout/ in the archive). Until they are, the
outcome-mask commitments have no third-party timestamp — which is the one property the
whole holdout depends on.

YOUR ACT:
1. Copy into the archive repo (/Users/bgm/MB Work/alpha-program-archive) under a32_holdout/
   ONLY these PUBLIC files from /Users/bgm/MB Work/a32_holdout/:
     raw_allascii.txt, candidates.jsonl, commitments.jsonl, exclusions.jsonl,
     duplicates.jsonl, flags.jsonl, collector_v001.py, transcript.md
2. *** NEVER COPY, COMMIT, OR READ custodian_private/ OR ANY FILE IN IT. *** Add a
   .gitignore entry excluding a32_holdout/custodian_private/ as a belt-and-braces guard,
   and verify with `git status --porcelain` and `git ls-files` that no custodian path is
   staged or tracked. If any custodian content has entered the index, STOP and report —
   do not push.
3. Before committing, verify each copied file's SHA-256 against the hashes recorded in R-23
   and report any mismatch instead of proceeding.
4. Commit with a message naming this as the A32 public-record deploy, and confirm the push.

DEFINITION OF DONE: SEALED (where applicable), MIRRORED, COMMITTED, AND PUSHED. Report the
output of: sh "/Users/bgm/MB Work/alpha-program-archive/deploy_status.sh"
plus the `git ls-files a32_holdout | wc -l` count and explicit confirmation that
custodian_private/ is absent from the repository.

FENCES: do not open, parse, summarize, or quote the contents of any value-bearing file; the
public files are value-free by construction and must stay that way. No new construction in
this paste. alpha_computed = false; proof_authorized = false.
