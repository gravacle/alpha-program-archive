#!/bin/sh
# One-command deploy check. Run from anywhere: sh "/Users/bgm/MB Work/alpha-program-archive/deploy_status.sh"
cd "/Users/bgm/MB Work/alpha-program-archive" || exit 1
git fetch -q origin 2>/dev/null
AHEAD=$(git rev-list --count origin/main..HEAD 2>/dev/null)
DIRTY=$(git status --porcelain | wc -l | tr -d ' ')
if [ "$AHEAD" = "0" ] && [ "$DIRTY" = "0" ]; then
  echo "DEPLOYED — public record current at $(git log -1 --format='%h %s')"
else
  [ "$AHEAD" != "0" ] && echo "*** $AHEAD COMMIT(S) NOT PUSHED — no public timestamp. Run: git push origin HEAD"
  [ "$DIRTY" != "0" ] && echo "*** $DIRTY uncommitted change(s) — not even committed yet."
fi
