RELAY 964 | LANE: DARIO | NO PASTE FOUND — NOTHING EXECUTED

A bare number 964 was issued.  Under the queue rule I must read the single file matching
relay_inbox/RELAY_PASTE_964_*.md, verify its seal BEFORE reading, and execute it.

THERE IS NO SUCH FILE.  Verified three independent ways, because an unquoted glob returning
"no matches found" is a known instrument failure in this lane and I do not trust it alone:

  1. ls -1 | grep -F '964'          -> no match
  2. find . -maxdepth 1 -name '*964*' -> no match
  3. numeric listing of every RELAY_PASTE_* in relay_inbox -> highest is 963

The inbox's newest entries are 963 (19:55), 961 (19:35) and 958 (19:13), all sealed, all with
matching sidecars.  Nothing is half-written, unsealed, or misnamed.

I HAVE EXECUTED NOTHING AND SEALED NOTHING.  In particular I did NOT:
  - re-run 963, whose work is already sealed at bda1dcf4e3c395a4... and reported;
  - guess which relay was intended, or infer a task from the surrounding numbers;
  - write a 964_DONE.md, which would assert a relay was performed when none exists.

This file is named NOT_FOUND rather than DONE so it cannot be mistaken downstream for a completed
relay.  No register, plan, tracker, or git action taken.  Gates unchanged: alpha_computed = false;
proof_authorized = false; kappa_record_computed = false.

STANDING BY.  If 964's paste is still to be written, issue the bare number again once it is sealed in
relay_inbox and I will pick it up under the normal rule.  If a different number was intended, say
which and I will run that one.

CHAIN_INVOKED = false
