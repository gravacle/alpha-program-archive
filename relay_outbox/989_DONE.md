RELAY 989 | LANE: DARIO | DONE

INBOX    RELAY_PASTE_989_DEMAND_V002_DARIO_V001.md
         7389e8319ac5ab461862915ee88e25e0f37a5eb3e7cfd869fac86950e9ce90df  (verified BEFORE reading)
SUBJECTS my 986  STAGE8_DESC_DEMAND_DARIO_V001.md         da32dc9dfff38a32...  VERIFIED
         check   STAGE8_DESC_DEMAND_CHECK_CODEX2_V001.md  f3704df1bc4d7b2f...  VERIFIED
OUTPUT   workspace/STAGE8_DESC_DEMAND_DARIO_V002.md
         c883d3732af61800f6ac2219e87406ccbbae60f7928172a80281e2e2cae951e3   34,770 B
SEAL     workspace/STAGE8_DESC_DEMAND_DARIO_V002.md.seal.sha256   shasum -c: OK
         Output name CLEAR.  Closure at byte 0, ends 5703 (BYTES, fixed point), re-verified AFTER the
         late numeral patch.  Pre-closure 27-token scan: 0 hits.  Zero residual placeholders.

COUNT = 35 conditions + 1 verdict-relative, each at bytes.  V001's 18+1 CARRIED WHOLE.

I STATED THE FAILURE IN MY OWN WORDS RATHER THAN THE CHECK'S KINDER ONES, at section 0, before any
  fold, so nothing below it reads as a defence.  V001's TITLE claimed the section; its CONTENT read
  the demand at the receiver I happened to have in hand and stopped there.  A CORRECT SUBASSEMBLY
  PRESENTED AS THE WHOLE IS AN UNDER-DEMAND -- and it is exactly the failure V001 was built to catch:
  its own section 8 named six under-demands on the ground that no single source carries the demand,
  and then missed six more because I ran right-closure on every SPAN and never on the SECTION.  The
  discipline was right; I applied it one level too low.

THE SIX GROUPS FOLDED AT THEIR CONSUMERS' BYTES, right-closure run BOTH WAYS at each -- and I state
  it as a checked result rather than an assumption, because it is the check I failed to run at
  section scope in V001.  ALL SIX SPANS OPEN EXACTLY ON A CLAUSE HEADING AND CLOSE EXACTLY ON THE
  NEXT: no truncation, no overrun.
    U7  B0 A01-A05 [7262,10112)   -> conditions 19-23 (inhabited candidate; frozen inventory;
        target-independent rule PLUS the frozen trace; a FILLED signature; provenance/domain cert)
    U8  A06-A09 [10112,12021)     -> conditions 24-26 (C0, U1, U3).  A08/U2 is ALREADY condition 13
        and is NOT double-counted.
    U9  A10-A13 [12021,13587)     -> conditions 27-29 (d_C0, d_U1, d_U3).  A12/d_U2 is ALREADY
        condition 5 and is NOT double-counted.
    U10 A14-A17 [13587,19040)     -> conditions 30-33
    U11 MD-3 [8794,11563)         -> condition 34
    U12 placement [16822,17244) + SM rows [36914,38169) -> condition 35
  I RE-VERIFIED EVERY SPAN THE CHECK ASKED ME TO FOLD BEFORE FOLDING IT -- 10 spans, 6 files, ALL
  MATCH.  Folding an unverified span would import a claim rather than check one.

THE THREE CORRECTIONS:
  (1) NO-INSPECTION SPLIT.  The two bars have DIFFERENT GROUNDS and only the first comes from the
      words: the temporal bar from "without output inspection"; the COMPOSITIONAL bar from
      common-origin provenance, regardless of timing -- and A15 states the conjunction outright:
      "A datum bagged independently before output may pass literal timing while still failing
      A03/A05 common derivational provenance; both predicates are required."  This is a PROSE-LABEL
      fix: conditions 15 and 16 keep their numbers, text and grounds.  It matters because a builder
      reading the compositional bar as a timing rule will think an early enough assembly passes it.
  (2) PATHCERT.  My V001 law-9b call -- "no member fixes the certificate's FORM" -- was TRUE OF MY
      TEN-MEMBER CLOSURE AND TOO STRONG OF THE CORPUS.  PathCert(Omega) is sealed at [19909,21513),
      specified and uninstantiated.  I folded it as the PARTIALLY-SPECIFIED form and re-invented
      nothing, naming the remaining open item: the exact Cert_P5 canonical serialization and digest
      convention.  Worth noting what the schema adds beyond P5's four maps -- d_C0, d_U1, {d_fin,N},
      {iota_NM}, d_out and TEN named certificates: corroboration from a second direction that the
      record's own path-level certificate already reaches past the U2/P5 tuple.
  (3) TWO QUOTE ATTRIBUTIONS.  Both verbatim, both bound to the wrong bytes: Q20 -> G6 [39637,39732);
      Q21 -> entry-instrument V002 [20579,20661), not the anchor instrument.  NEITHER MOVES K7's
      CONTENT, since K7's own row independently rejects a status flag or a record-only Q7.  The
      defect was in my citation discipline, not in the reading.

CARRIED = VERBATIM.  Conditions 1-18 and the O1-O4 / U1-U6 tables travel byte-for-byte; where a
  ground column changed it is only because member numbering grew 10 -> 14, and every such change is
  hunk-accounted.  DIFF = 13 HUNKS, H1-H13, NOTHING DELETED.

CONDITION 13 SURVIVED ITS OWN FLAG.  V001 closed by naming it as the thing to press -- whether the B0
  U2 signature types a SLOT or constrains DELIVERY.  The check pressed it and it holds: d_U2 has the
  complete U2 role as codomain, so a total map must deliver the inclusive identity and the contact
  rules.  Flagging it was right and cost nothing.

ONE FINDING THAT STRENGTHENS AN OVER-DEMAND FROM NEW DIRECTIONS: FOUR sealed consumers now decline
  uniqueness in their own words -- P5 section 4's two TYPE-R kills, A01 ("acceptance does not demand a
  unique microscopic ontology"), A16 ("unique-origin reconstruction remains unnecessary"), and MD-3
  ("an acceptance condition over the tested family, not a global uniqueness theorem").  A lane
  demanding unique source determination now over-demands against the record four times over.  O1 is
  the over-demand a 35-row list most invites, which is why I recorded the reinforcement.

ONE DEFECT RETURNED TO THE CHECK, as a courtesy and not a challenge: its closure member 18 prints the
  entry-instrument digest as 62 HEX CHARACTERS, NOT 64, diverging from the true digest after 41.  The
  file it names is right and its Q21 correction is INDEPENDENTLY VERIFIED HERE at [20579,20661), so
  THE FINDING STANDS -- but a closure table's whole function is content-addressing and a 62-character
  string addresses nothing.  My member 07 carries the well-formed digest.

ONE SLIP OF MY OWN, SELF-CAUGHT, AND THE IRONY RECORDED: I wrote "26 unique intervals" in the byte
  audit BY EYE -- in the very artifact whose hunk H11 corrects V001 for counting spans by eye.  The
  scoped grep returned 23; patched, and closure re-verified after the patch.  A second checker slip
  rode along: my verification regex matched H11's row instead of the section-8 sentence and reported
  "13", which is H11's (correct) figure for V001, not V002's.  Both numbers are now right and refer
  to different things.  NUMERAL_GREP = SCOPED-RUN throughout, per my own 986 lesson: 14 closure
  members, conditions contiguous 1..36 with 35 package + 1 verdict-relative, hunks contiguous H1..H13.

GATES HELD: alpha_computed=false; proof_authorized=false; kappa_record_computed=false.  BLIND held;
  every scale symbolic.  JOINT_ANCHOR_DERIVED = false travels.  PE-1..15 pointer-only.  Builder-A code
  untouched.  V001 remains sealed and on the books; V002 supersedes it as the reading of record and
  DELETES NOTHING.  NO construction, no candidate, no supply call, no selector exercised, no
  feasibility verdict -- and none implied by the count.  Nothing adopted, nothing registered, no
  register/plan/tracker/git action.  ALL CLAIMED until the opposite-lane check; the step to press
  first is THE FOLD BOUNDARY ITSELF -- I folded exactly the six groups the check named, on the test
  "applicable because the section's B0 domain reaches it".  That same test, one notch wider, pulls in
  A17's T5A/T5B Boundary-Resolved generator legs and the item-1 realization leg.  I read those as ROWS
  OF CONDITION 33 because A17 carries them as legs of one ledger; if a lane reads them as independent
  consumers, the count grows again and V002 is a subassembly of a wider shape in exactly the way V001
  was of this one.

CHAIN_INVOKED = false
