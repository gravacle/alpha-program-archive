RELAY 782 | LANE: DARIO | DONE   [PLAN:F1-ADVANCE / RATIO ROUTE]

INBOX   RELAY_PASTE_782_RL2B_RATIO_STATE_MAP_DARIO_V001.md
        c6c4e3b375c4dec7f9421e80be02fd709ba78dde044293f1e4c275d2fc59a47b  (seal verified BEFORE reading)
LANE GUARD: header names DARIO. PASS.
PICKED UP BY CHAINED PICKUP from 781.
STATE-BRIEF PINNING: relay pinned PROGRAM_STATE_BRIEF_V003.md (63549f639b75…) — digest MATCHES
  the relay's stated pin, seal OK, read before task work.

OUTPUT  workspace/STAGE8_RATIO_ROUTE_STATE_MAP_DARIO_V001.md
        fdc09c072c254e280ea0297a9ed6989ee70bece6c07e329450cf0d2f7b26e4da   (46,124 bytes)
SIDECAR workspace/STAGE8_RATIO_ROUTE_STATE_MAP_DARIO_V001.md.seal.sha256    shasum -c: OK

NAME PROBE: absent before write (recursive, artifact and sidecar).

SEARCHED SPACE: ./workspace/**/*.{md,json} + ./supervision/**/*.{md,json} = 3,003 files.
  evaluator_build_A/ and checks/ EXCLUDED BY LAW from every result. memory-bank NEVER searched.
  Sub-corpus bearing R-L2b or A-L0: 121 files, of which 86 carry a verifying sidecar.
  Controls (case-sensitive, all non-zero): R-L2b 111, A-L0 47, A32 169, cluster.summab 7,
  "ratio route" 23, S13 25.

=== FOUR CUSTODY FINDINGS, PRINCIPAL/REGISTRAR-FACING ===

(i) A SEAL GENUINELY FAILS.  supervision/EXECUTION_TRACKER.md
      sidecar : f42addcc9303d1f4785f4adef7412143321d7ab24d0628fb9b2dfae8ea403fae
      file    : ad0740f9ac9880d9b531fae408e727530831a2d7d0b234703f171ca98ea2c2f8
      shasum -c run FROM THE FILE'S OWN DIRECTORY: FAILED.  mtimes identical (08:52:28), so the
      tracker was written AFTER its own seal was computed.  Consistent with a live registrar
      file — but a sidecar that does not verify is a custody break whatever the cause.
      I do not touch trackers; reported only.

(ii) RELAY 781's FLATTENING CHECK IS NOW AGAINST A SUPERSEDED REGISTER.
      DECLINE_REGISTER_V002.md (957476c8c605a370…, sealed OK, 15,523 B) states "V002 supersedes
      V001 … FLATTENING CHECK runs against THIS table", S01–S37 from sweep 779.  At my 781
      preflight `find` returned V001 ONLY, so that check was correct when run and is not correct
      now.  781's FLATTENING_CHECK = clean SHOULD BE RE-RUN AGAINST V002 BY THE REGISTRAR.
      (My +1 decline is S01 there, sourced to the same 768 span I verified at 781.)
      THIS RELAY's flattening check WAS run against V002.

(iii) LIVE-FILE RACES WITHIN ONE RELAY.  PROGRAM_STATE_BRIEF moved V003 -> V005 and THE_PLAN
      moved V001 -> V003 while 782 ran; V005's own pointer names plan V002, already stale.
      I complied with the relay's explicit pin (V003) and ALSO read V005 and plan V003,
      disclosing both rather than silently substituting.  ALIGNMENT LAW 4's "current version"
      is not well-defined under a live registrar.

(iv) A STRATUM'S BUILT ARTIFACT LIVES OUTSIDE THE ARCHIVE.  Stratum S1/S2's product is pinned by
      path+hash into a parent tree, is ABSENT from the lawful glob, and the record itself states
      its hash "is pinned NOWHERE" with "No .seal.sha256 sidecars … in the parent tree for this
      family."  The most-executed stratum is the least custodied.

FINAL LINES (as sealed)
  STRATA = 5 located, NOT 4 (the relay's premise corrected, as AS1 directs).  S1/S2 BR induced
     coefficient functions (product ABSENT from the glob, pinned NOWHERE, no sidecars); S3
     coupled record-bundle modulus gate (SEALED-OK, alpha_tree conditional, saddle open); S4 BID
     minimal cell + Hamilton-Jacobi scale bridge (gate carries NO SIDECAR; sqrt(2) blocked,
     chained behind O1); S5 joint-handle character Hessian — the FIFTH, absent from every
     four-list; plus one ORPHAN expressly NOT ADOPTED.  Sole sealed enumeration:
     STAGE8_GRAVITY_EVIDENCE_ADMISSION_AND_FIVE_STRATA_BINDING_V001.md (bad9795072739e35…),
     "One Route Class, Five Strata", scope block routes_merged=false / routes_ranked=false.
     CLAIM-STATUS LAW APPLIED: NO stratum carries PROVED anywhere in the glob; strongest is
     CLOSED_BUT_INSUFFICIENT.  Same-name trap disclosed (the adjudication sweep's four-way
     "strata" is a ratio-PRECEDENT stratification, a different object).
  DISCONNECTS = 5 classified (FORCED_UNIQUE: 0 / FREE_MULTIPLE: 2 / UNDECIDABLE_FROM_STOCK: 3).
     ZERO boundaries are closed by constraints already in stock.  The record's own cross-citation
     map finds ZERO cross-citations; the sealed binding carries a NON-COLLAPSE LAW forbidding
     shortcuts.  Cross-referenced to DECLINE_REGISTER_V002 rows S04, S29, S30, S33, S34 (span
     digests recomputed and matching).
  MISSING_POWER = located, and it is NOT a shortfall in a bound.  Spans: phrase at
     C4_DISPOSITION_BRIEF [5130,5574) (UNSEALED); sealed restatement "short exactly one power of
     decay" at C4_REFUTED_CLAUSE_STRIKE_PRINCIPAL_DECISION [5574,5969) under "A LEAD,
     DELIBERATELY NOT RULED ON"; failing term at T7_E1_SUCCESSOR_SPEC_V002 §O.A0.2 [35505,36573)
     with shell arithmetic [36573,37641) labelled "EXACT ARITHMETIC OF THE TARGET" (conditional
     on an ASSUMED exponent); point of loss at IBP_SCALAR_WEIGHT_DETERMINATION [112,974),
     [1625,2467).  THE FINDING: IBP_performed_anywhere_in_corpus = FALSE — the integration by
     parts has NEVER been performed and its integrand is NEVER WRITTEN — and
     smooth_cell_profiles_referent = ABSENT (2 occurrences, no definition, three candidates all
     disqualified).  "It is not lost in a computation, it is never supplied; the convergent sum
     presupposes it."  OBJECT KIND (the record's own): a PROFILE / TRANSVERSALITY /
     PROJECTION-TAIL LEMMA with three uncertified components (U1 time-profile norms, U2 lightcone
     transversality over full D3, U3 projection tail) — explicitly NOT a sharper bound and NOT a
     different decomposition.  All three alternative suppliers DEAD (HS volume scaling DEAD; time
     integration DOES_NOT_REACH; Q-support DEGENERATE, "U3 wearing a different name").
     CLASSIFICATION = UNDECIDABLE_FROM_STOCK — not FREE_MULTIPLE, because there are not two
     inequivalent sketches, there is NO OBJECT for the lemma to act on.  Missing sealed answer,
     named: a definition of "the smooth cell profiles".
     S13 DISCHARGED, VERIFIED BYTE-EXACT BY ME (file eed30aec…, span [19029,19502), span sha
     f18ee4f9…): "arm 2 may consume R-L2b, never the reverse."  R-L2b SUPPLIES; arm 2 CONSUMES;
     the missing power is the CONSUMER's, so CLOSING R-L2b DOES NOT CLOSE IT — that entailment is
     the identification S13 declines, and it is the relay's own framing.
  OBLIGATIONS = 4 cited individually (EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001,
     SEALED-OK, "ONE CAMPAIGN, FOUR DISCHARGES"): O1 [4137,4192); O2 [4192,4298); O3
     [4298,4414); O4 [4414,4670).  THREE DISCREPANCIES DISPLAYED: R-L2b is TWO exponents (alpha
     AND beta, the second "routinely omitted"); a DIFFERENT four-set (transport charter
     O-D1/O-D2/O-D3 + O-D4 flagged-not-accepted) is confusable with these four; the supervision
     restatement "THE FOUR CONSUMERS" is UNSEALED.
     TEN CROSSINGS = ENUMERATION ABSENT — the count appears in exactly two files and NEITHER
     lists them; and the ten is itself a REFUTATION of a reviewer's "one finite-to-physical
     bridge" hypothesis on type signatures: a measure of distance, not of progress.
     ROUTE STANDING: commutator route REFUTED BY ITS OWN LANE (two independent grounds);
     uniformity REFUTED (blind inputs); principal ruled it SUPERSEDED / RE-POSED with the ground
     disclosed as the principal's and NOT a sealed physical principle; typed REFUTED AS WRITTEN /
     TYPE-R.  THE FOUR CONSUMERS SURVIVE THE SUPERSESSION.  Route (b) — a DIFFERENT object — is
     LIVE and unconsumed per two decisions of record dated 2026-08-08.
  A32 = scope stated.  Twice ratified (holdout freeze 2026-07-28; instrument "RATIFIED AS BOUND"
     2026-08-06), BOTH acts expressly attaining nothing.  M5a-V002: 23 conjuncts, 7 TRUE / 13
     FALSE-SUPPLIED-BY / 3 FALSE-LONG-POLE, with passed_A01_A29_and_A35 FALSE at the graph root
     so SPEC-SEAL is false at the root.  Gates proof_authorized via A34.  Enlarges the definition
     of done (a SECOND, NON-ALPHA prediction at D>=5).  Q-25 permanent carriage.
     SCOPE UNCHANGED BY AS1-AS3, and the relay's premise is unsupported: the literal phrase
     "A32-gated" is ABSENT, and NO record ties A32's scope to the strata (probes stated; 8
     intersecting files read at their A32 spans).  Three statuses for one row displayed
     unresolved (F1 unstarted / R-22 already written into V011 / lane audit DONE-SCAFFOLD).
     CUSTODY: the workspace V011 working copy is a DIFFERENT byte-version from the sealed mirror
     and the A32 line numbers differ; spans NOT interchangeable.  Sealed mirror used.
  PATH_REMAINDER = enumerated (14 items), governed by a typing the relay's question does not
     carry.  SEALED Q-34 (PRINCIPAL ACT): "ALPHA'S STIFFNESS IS K_*"; kappa_record is the
     record-side INTENSIVE Hessian; "the two Hessians are generically DIFFERENT physical
     quantities".  CURRENT PLAN V003: "The R-L2b/linked-cluster campaign is OFF alpha's value
     path.  The kappa-only chain is short but is NOT a shortcut to alpha."  kappa_record is
     reached by the forced stitching spine, NOT by the ratio route.
     THE 14: (1) the Q-34 typing; (2) four consumers undischarged; (3) the beta exponent; (4) ten
     crossings never enumerated; (5) five strata unconnected, 0/5 forced; (6) S1/S2's product
     outside the archive; (7) A32's 3 long poles + FALSE graph root; (8) SPEC-SEAL false; (9) THE
     COMPARISON BAN'S RELEASE CONDITION ABSENT — four files mention it and EVERY ONE ASSERTS ITS
     NONEXISTENCE; (10) kappa_record = kappa_Thomson NOT ASSUMED, must be DERIVED or the route
     fails; (11) A28 firewall BLOCKED; (12) C7 chain — S03 EXPLICIT INCOMPLETENESS, S04-S08
     inheriting; (13) five physics rows BLOCKED, common cell not formed so prereg 9f0d12b4 cannot
     run; (14) the forced spine's three B1 fields ALL FREE, plus Gate-5's six PENDING items.
     FOR THE PRINCIPAL, PLAINLY: the missing power is the SMALLEST of these — one undefined
     object inside one arm of one obligation of a campaign the current plan places OFF alpha's
     value path.  Items 9, 10, 13 and 14 are ON the path and are not estimates at all: they are
     absent objects and unwritten authorizations.
  FREEDOMS_CONSUMED = depth x, modulus rho, the sqrt(2) branch, and the exponents alpha/beta all
     CARRIED-AS-PARAMETER; "the smooth cell profiles" CARRIED-AS-ABSENT; K_* vs kappa_record
     CONDITIONED-ON the sealed Q-34 typing, quoted, not merged.  SUBSTITUTED: NONE.
  FLATTENING_CHECK = clean, RUN AGAINST DECLINE_REGISTER_V002 (S01-S37), not the superseded V001.
     37 rows walked; 11 live to this map (S04, S13, S16, S23-S26, S29, S30, S33, S34, S36, S37).
  CHAIN_INVOKED = false
  VERB_AUDIT_SELF = NOT CLEAN (+5): (1) the pinned brief went stale TWICE during the relay and I
     report that alignment law 4's "current version" is ill-defined under a live registrar;
     (2) my own 781 flattening check is now against a superseded register — correct when run, not
     correct now, flagged for re-running; (3) a seal GENUINELY FAILS (EXECUTION_TRACKER.md),
     confirmed in isolation from the file's own directory because at 742 I generated six false
     mismatches doing this wrong; (4) the FORCED/FREE/UNDECIDABLE typing is MINE, not the
     record's, and another lane could type the S4 sqrt(2) boundary differently; (5) I answered
     AS5 as asked AND displayed the Q-34 typing that undercuts its premise, in that order, and
     flag the ordering as a judgment.
  alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false

GATES HELD: NO ESTIMATE ATTEMPTED (map only); no member binding; no fixed-point execution; no end
  test; no numeric evaluation of physical quantities; no comparison to measured constants.
  PE-1..PE-6 recorded, NOT consulted, NOT opened.  Law 5(a) register grep run before task work.
  Builder-B independence held: no evaluator_build_A/ or checks/ file opened by me or by any
  commissioned hunter (one grep ENUMERATED a path under that tree; disclosed; nothing opened).
  ~/.codex untouched; memory-bank never searched.  No register, plan, tracker, git action.
