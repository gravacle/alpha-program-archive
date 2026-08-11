RELAY 971 | LANE: DARIO | DONE

INBOX   RELAY_PASTE_971_SUITE_INSTANCE_DARIO_V001.md
        cf44dc200fe583990ac6ff37fae7ffcd5674d2032b43e9aa1f4157cc6a10b1e1  (verified BEFORE reading)
SUBJECTS my 969  28bc43a0a8e841f1...  (SEAL-OK)
         the check STAGE8_AXN_FAMILIES_V004_CROSSCHECK_CODEX2_V001.md  3cb349ea0d945d21...  (SEAL-OK)
GOVERNING STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V004.md  a195edb03b36be44...
OUTPUT  workspace/STAGE8_AXN_SUITE_INSTANCE_DARIO_V001.md
        b384c473a338717eb6f351b6c48bcf6ab1ee6c2d76f9d9749e36fe859362bacd   20,537 B
SEAL    workspace/STAGE8_AXN_SUITE_INSTANCE_DARIO_V001.md.seal.sha256  shasum -c: OK
        Output name CLEAR.  Closure at byte 0, ends 2228 (BYTES), block and final line agreeing.
        Scan 0 hits.  PRE-SEAL REPLAY: both suite digests recomputed under the displayed convention,
        the replay-entry and both certificate digests re-derived -- all OK.

SCHEMA_DIFF = FIELD-EXACT (0 missing / 0 extra / 0 renamed) at all three levels: outer 9/9,
  BOUNDED_CLASS 8/8, for_class 8/8, with exactly one variant present.

MY 969 WRAPPER GOT THREE THINGS WRONG, ALL MINE: invented key names (fc_01.. instead of the schema's
  own), both receipt receivers collapsed to a ROOT instead of enumerated LISTS, and the two
  certificates placed INSIDE the suite as undeclared fields.  I had also pointed bounded_class_definition
  and explicit_reopening_trigger at the CANDIDATE GRAMMAR; V004's §5.1.1 template points them at the
  STAGE-RULE ground and the sealed reopening predicate -- a different object.  All corrected.

A NOTE ON THE DIFF ITSELF, because it nearly produced a false result.  My first extractor sliced the
  schema by ASSUMED indentation and reported 43 discrepancies.  Those were an artifact of the
  extractor, not the suite -- the schema sits inside a fence at a different base indent.  I re-derived
  the levels from the block and re-ran, getting 0/0/0.  A DIFF TOOL UNCHECKED AGAINST A KNOWN-GOOD CASE
  CAN MANUFACTURE DEFECTS AS EASILY AS IT CAN MISS THEM, and I did not ship the first number.

SUITE_SHA = COMPUTED-OVER-COMPLETE, convention DISPLAYED because the schema states none.  A field
  cannot contain the digest of bytes that include itself, so I supplied and showed the only
  non-circular reading: stage 0 is the canonical suite with both digest fields omitted (3074 B) giving
  suite_sha256 = dec168f2254712e8...; stage 1 inserts it (3156 B) giving the freeze receipt
  0aef54371edbe0dc...; the final object is 3258 B.  Each digest covers STRICTLY EARLIER bytes, so it is
  non-circular and exactly replayable -- and if the registrar reads the self-reference differently the
  object rebuilds mechanically from stage 0.  I verified both by recomputation before sealing.

FREEZE_RECEIPT = SEALED-PRE-OUTPUT, and gate 3 is satisfied THE ONLY LAWFUL WAY -- BY COMPLETING THE
  OBJECT FIRST.  At 969 I left this field absent precisely because the suite was incomplete; completing
  the suite is what makes filling it honest rather than manufactured.

LISTS = BOTH-ENUMERATED with the identity holding byte-wise; the seven receipt digests were RE-DERIVED
  here from their payloads rather than copied.  The outer receiver stays separately present rather than
  filled by category substitution -- the distinction my own 952 ruling turned on.
REPLAY_ENTRY = BOUND: no sealed entry point existed, so one was built as authorised -- a seven-step
  deterministic procedure, byte-exact and order-fixed, no clock, no randomness, no network.
CERTS = REBOUND to the final suite digest, OUTSIDE the suite, both parsing at 8 fields.

A RECURRENCE I RECORD RATHER THAN BURY.  My first draft again pinned a member by completing the relay's
  TRUNCATED digest with invented bytes -- the same slip I caught at 969, one relay earlier.  I caught it
  again in the same pre-seal check and replaced it with the computed value.  TWICE IS A PATTERN, NOT AN
  ACCIDENT: a truncated digest in a relay is a PREFIX TO VERIFY AGAINST, never a stem to complete.  I
  wrote that rule into the artifact's custody section so it travels rather than living in my habits.

GATES HELD: alpha_computed=false; proof_authorized=false; kappa_record_computed=false.  BLIND held --
  the A0 fiber is a digest copy and every rank-shaped object stays closed.  BASIS INDEPENDENCE
  PRESERVED.  JOINT_ANCHOR_DERIVED = false travels.  PE-1..15 pointer-only.  No numeric evaluation.
  Authored here and only this: the replay entry-point object and the displayed digest convention.
  Nothing adopted, nothing registered, no register/plan/tracker/git action.  All CLAIMED.  Solo.

CHAIN_INVOKED = false
