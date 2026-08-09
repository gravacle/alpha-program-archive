RELAY 800 | LANE: DARIO | DONE   [PLAN:C1-PRE-2]

INBOX   RELAY_PASTE_800_E4B_PROOF_MOLLER_HUNT_DARIO_V001.md
        d0616df56ccf342326b4b408e57edcc76ffd81c2377addaad52c9a76217628dd  (seal verified BEFORE reading)
LANE GUARD: header names DARIO. PASS.
STATE-BRIEF PINNING: relay pinned PROGRAM_STATE_BRIEF_V005.md (e26f0d16055f…) — digest matches
  (e26f0d16055f3e83), seal OK, read before task work.  Drift check: V005 current.
LAW 8 on every seal — and MODE 3 (packet-manifest membership) was decisive for all Task-B
  survivors, none of which carries an adjacent sidecar in either spelling.

OUTPUT  workspace/STAGE8_C1_E4B_PROOF_AND_MOLLER_HUNT_DARIO_V001.md
        162c6d7ddcd280f567645eb863828d86c3d9a8cd06f49c0641a4361ff8a1a0f5   (22,446 bytes)
SIDECAR workspace/STAGE8_C1_E4B_PROOF_AND_MOLLER_HUNT_DARIO_V001.md.seal.sha256   shasum -c: OK

NAME PROBE: absent before write (recursive, artifact and sidecar).

SOURCES VERIFIED BEFORE USE
  3359960fb411eff8…  CAUSAL_DIRECT_LIMIT_REDUNDANT_RECORD_RESULT_V001.md            manifest OK
  9be3f55fd527b9a8…  CAUSAL_DIRECT_LIMIT_ARCHITECTURE_ADJUDICATION_RESULT_V001.md   manifest OK
  625b4ed9c91b28dd…  CAUSAL_DIRECT_LIMIT_RECORD_PRINCIPLE_V001.md                   manifest OK
  b760e1b91c931545…  workspace/STAGE8_C1_E4_VERIFICATION_DARIO_V001.md              .md.seal OK
  5f8e60629f2b0fc7…  R3_4_SHARED_SOURCE_OUTGOING_RANGE_ERRATUM_V001.md              manifest OK
  10909b5c21e73ecf…  R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md             manifest OK
  3240d935ef558948…  R3_4_DRESSED_OUTGOING_RECORD_RANGE_RESULT_V001.md              manifest OK
  781608f2fe4c8753…  R3_4_SHARED_SOURCE_CAUSAL_PARENT_RESULT_V001.md   seal NOT established by any
     of the three modes; cited only as SUPERSEDED historical phrasing, carried at that grade.
INTEGRITY CHECK RUN (the V011 hazard pattern): workspace and packet copies of ERR / GNS / RNG are
  BYTE-IDENTICAL, so all quotations are packet-sealed content.

FINAL LINES (as sealed)
  E4B = PROVED (E4 reduces to E4c alone).  Step 1: RED's clause "Causally dependent writes retain
     their causal order" FORCES the write order to be a LINEAR EXTENSION of the causal order —
     derived, not assumed.  Step 2: every prefix of a linear extension is a DOWN-SET (verified:
     200 random extensions, all prefixes, ZERO violations), so exhaustion stages are causally
     down-closed BY DERIVATION — supplying the very ingredient 799 named as missing, from RED's own
     clause.  Step 3: on a finite poset any two linear extensions are connected by ADJACENT
     TRANSPOSITIONS OF INCOMPARABLE (= spacelike-disjoint) elements — verified on 120 random
     posets, n = 4,5,6, every one connected, up to 360 extensions; exactly RED's licensed moves, so
     RED's clause gives THE SAME CIRCUIT along the connecting path.  Step 4: cofinality + local
     finiteness put every finite down-set eventually inside both exhaustions; ARCH section 3's
     strong convergence carries stagewise agreement to the limit.
     SECOND INDEPENDENT SUPPORT (found in Task B, missed at 799): GNS proves omega_M(iota_NM(A)) =
     omega_N(A), "for the full matrix algebra and every finite M>N; not inferred from the
     three-cell regression."  E4b rests on two supports sharing no step.  CARRIED HYPOTHESES
     unchanged and unenlarged.
  MOLLER_HUNT = ./workspace/**/*.{md,json} + ./supervision/**/*.{md,json} (2,987 files;
     evaluator_build_A/ and checks/ excluded by law; memory-bank never searched).  Controls all
     non-zero: Moller 86, outgoing 232, "causal exhaustion" 19, "direct limit" 46.
     HITS_RAW = 18 probe forms; 'Moller' occurrences typed 41 status-FLAG / 39 DEMAND / 127
     NEITHER, the 127 read individually.
     SURVIVORS = 4: ERR (5f8e6062…, packet-sealed) — "stable dressed outgoing-record monomorphism",
     a unital injective star-homomorphism whose range is a source-dressed record algebra inside the
     full parent and NOT generally inside the bare record-only algebra,
     stable_dressed_record_monomorphism_derived = true ; GNS (10909b5c…, packet-sealed) — verdict
     OUTGOING_RECORD_GNS_AND_DRESSED_NET_DERIVED with compatible state, GNS representation,
     strongly continuous identity dynamics, source-dressed incoming net, recoverable central
     sequence, and the exact compatibility theorem ; RNG (3240d935…, packet-sealed) — the
     matrix-unit range audit behind ERR ; SCP (781608f2…) — SUPERSEDED phrasing, seal not
     established, carried at that grade.
     ARCH's bar does NOT apply to USING S1-S3: it bars SELECTING a channel decomposition, and these
     are DERIVED results.  No channel decomposition is selected here.
  E4C_BOUNDARY = NARROWED (precursor found, scope stated).  NOT CERTIFIED-REAL — the hunt did not
     return empty.  NOT DISSOLVED — the target is absent and the same sealed files say so
     unprompted: "This is not a construction of a global source-inclusive state limit or an
     infinite-future source Moller UNITARY."  THE GAP, TYPED: (i) MONOMORPHISM vs UNITARY — E4c
     needs an INTERTWINER between the dressings induced by two cofinal exhaustions, and a unital
     injective star-homomorphism whose range is not generally inside the bare record-only algebra
     supplies none, injectivity giving no inverse off the range; (ii) COMPLETED-RECORDS/FINITE vs
     INFINITE-FUTURE SOURCE-INCLUSIVE — GNS's compatibility is exact for every finite M > N, while
     E4c needs the infinite-future source-inclusive limit GNS declines to construct.  SOLE LAWFUL
     ROUTE unchanged (ARCH section 5): "from the same target-independent source-record-gravity-
     gauge action required by R3."
     C1: may now assume E4a AND E4b; must still carry the dressed-maps disjunct alone, as a
     NARROWED live falsifier — not "no Moller object exists" but "the derived object is a
     MONOMORPHISM on completed records, not a UNITARY on the infinite-future source-inclusive
     limit."  C1 may consume S1-S3 lawfully; it may not treat them as closing E4c, nor select a
     channel decomposition to bridge the difference.
  CHAIN_INVOKED = false
  VERB_AUDIT_SELF = NOT CLEAN (+3): (1) 799 NAMED E4c's MISSING OBJECT FROM FLAG-READING ALONE — I
     cited two "= false" flags and a prose bar and called it the exact failing step, while a
     derived packet-sealed precursor sat in files I never opened; the obstruction was real, my
     account of it was thin, and only a dedicated hunt showed how thin; (2) the same hunt found
     E4b's SECOND SUPPORT, which I also missed at 799 while calling E4b "SUPPLIED-MODULO";
     (3) LAW 8 MODE 3 WAS DECISIVE AGAIN AND MY FIRST PROBE STILL GOT IT WRONG — the per-file loop
     reported all four survivors "unsealed?" because it hashed the workspace copies; the packet
     copies are manifest-verified, and I then ran the byte-identity check between the two copies so
     the quotations are packet-sealed content.  All three run against my own prior relay.
  alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false

FREEDOMS_CONSUMED = the exhaustion {V_n} CARRIED-AS-PARAMETER (none selected) ; the write order /
  linear extension DERIVED FROM RED, not chosen, and the choice among them shown immaterial ;
  down-closure of stages DERIVED, not assumed ; the primitive controlled-write rule CARRIED AS
  ADOPTED ELSEWHERE ; the ready-state boundary condition CARRIED AS HYPOTHESIS ; the outgoing
  channel decomposition NOT SELECTED (ARCH's bar quoted and obeyed) ; the Moller unitary CARRIED AS
  ABSENT, the precursor consumed only as a derived result ; the root spectral measure rho_f NOT
  SELECTED ; the causal complex V CARRIED-AS-PARAMETER ; the F-assignment rule NOT SELECTED ;
  scaling weights NONE CONSUMED (law 2a).  SUBSTITUTED: NONE.
FLATTENING_CHECK = clean (37 rows walked; 3 live: S24 LIVE AND OBSERVED — E4c not rescued by
  reaching for a clustering or channel-decomposition axiom, the precursor consumed as a DERIVED
  result; S26 and S08 discharged).

GATES HELD: no channel decomposition selected (ARCH's bar); no smooth import (S26); no EM
  identification (S08); no common cell formed; no junction map evaluated; no member binding; no
  fixed-point execution; no end test; no numeric evaluation of physical quantities; no comparison
  to measured constants.  PE-1..PE-7 pointer-known, zero weight, not opened, not consulted.
  Builder-B independence held: no evaluator_build_A/ or checks/ file read.  ~/.codex untouched;
  memory-bank never searched.  No register, plan, tracker, git action.
