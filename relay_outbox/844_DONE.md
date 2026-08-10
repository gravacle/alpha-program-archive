RELAY 844 | LANE: DARIO | **STOPPED CLEANLY AT THE CLAIM-STATUS GATE**   [PLAN:AXN-BUILD-A11]

INBOX   RELAY_PASTE_844_EXITB_SCHEME_DARIO_V001.md
        0d33ba382eed2402fe8968a550aa1160a8e1408431596c5e778538438242a39f  (seal verified BEFORE reading)
LANE GUARD: header names DARIO. PASS.
STATE-BRIEF PINNING: PROGRAM_STATE_BRIEF_V005.md (e26f0d16055f3e83), seal OK, read before task work.

OUTPUT  **NONE.**  No EXIT-B scheme artifact was written; name probed and confirmed absent.
NO CONSTRUCTION OCCURRED: no variation scheme was defined, no class was parametrized, no pullback
        was built, no machinery of any kind was authored.

=====================================================================================
WHY: THE GATE FAILS ON TWO PROBES
=====================================================================================
Required: `STAGE8_AXN_BUILD_EXITA_HUNT_CODEX2_V001.md`, archive-side, with `CIRCULARITY = CONFIRMED`
(or corrections to apply).  Standard wait-once-then-stop.

  PROBE 1 (at pickup, in 844_ACK.md): ABSENT.  No EXITA / EXIT_A artifact; no relay-843 leg in
    inbox or outbox.
  PROBE 2 (widened): STILL ABSENT.  **No EXIT-named artifact of ANY kind exists in the archive**
    except this relay's own paste and sidecar.  The newest CODEX2 artifact by mtime is still
    `STAGE8_AXN_BUILD_ROUND1_CROSSCHECK_CODEX2_V001.md` — the one I already consumed at 842.

  REGISTRATION IS NOT CROSS-CHECK, AND HERE THE TRAP IS SHARPER THAN AT 842.
    EXECUTION_TRACKER line 674: "| 842 | Dario | [PLAN:AXN-BUILD-A9] H1 integrand | RETURNED (Q-746;
      UNDECIDABLE; U1<->H1 CIRCULAR; two exits) |"
    Register Q-746 records the circularity at length, in my own terms.
    **The register REPEATS MY CIRCULARITY CLAIM BACK TO ME.**  Reading "U1<->H1 CIRCULAR" in a
    registrar entry as though it were the opposite lane's CIRCULARITY = CONFIRMED is precisely the
    confusion the gate exists to prevent — and it is easier to fall into here than at 842, because
    the register's wording is the very verdict the gate asks for.  Charter law 3 requires the
    OPPOSITE LANE'S adversarial pass.  Registration is custody; confirmation is verification.

  GATE VERDICT: **FAILED.**  ACTION: STOP CLEANLY.

=====================================================================================
WHY THIS GATE IS SUBSTANTIVE, NOT PROCEDURAL — TWO REASONS, BOTH SPECIFIC TO THIS RELAY
=====================================================================================
**(1) EXIT-B EXISTS AS A ROUTE ONLY BECAUSE THE CIRCULARITY IS REAL, AND THE CIRCULARITY IS MINE.**
The relay's task is to build the class-wide variation scheme because U1 <-> H1 is mutually gated.
That finding is my own 842 result, CLAIMED and un-cross-checked. If the opposite lane refutes or
re-scopes it — for instance by showing the pullback is available per-candidate after all, or that
round 1's side of the loop was itself over-bound — **then the scheme is machinery built for a problem
that does not have that shape.** Building it first and testing the premise afterwards inverts the
cadence exactly as consuming an un-upgraded package would.

**(2) THE RELAY'S OWN SCOPING INSTRUCTION IS UNDETERMINED, BECAUSE 843 HAS NOT LANDED AT ALL.**
The paste says: *"If 843 lands EXIT-A INHABITED, note it: the scheme then serves as the TESTING
instrument for the candidate — build it anyway, scoped to that use."* **There is no 843 leg in the
inbox or outbox and no EXIT-A artifact anywhere.** So I do not know whether to build the scheme as a
**solving** instrument (EXIT-A empty: the scheme must generate the integrand) or a **testing**
instrument (EXIT-A inhabited: the scheme need only evaluate a supplied candidate against C2..C6).
**Those are materially different objects**, and the relay itself makes the scoping conditional on a
result that does not exist. Guessing which would be authorship of the scheme's purpose.

=====================================================================================
WHAT I DID NOT DO, AND WHY IT MATTERS THAT I DID NOT
=====================================================================================
This is the first relay in the build to commission CONSTRUCTION from me — *"build machinery, not an
action substitute; T5 untouched; STOP-ON-FREEDOM absolute within it."*  At 842 I declined to build
EXIT-B on my own initiative precisely because it was construction; the principal has now authorized
it, so the earlier objection is answered and would not have blocked me here.  **The blocker is the
gate alone, not reluctance.**  I record that distinction so the stop is not read as a lane declining
its first construction task.

FOR THE EXIT-A HUNT, WHEN IT COMES — what its verdict changes for this relay:
  CIRCULARITY = CONFIRMED + EXIT-A EMPTY      -> build the scheme as a SOLVING instrument; the
                                                 pullback must generate integrand constraints.
  CIRCULARITY = CONFIRMED + EXIT-A INHABITED  -> build it as a TESTING instrument, scoped to
                                                 evaluating the supplied candidate against C2..C6.
  CIRCULARITY REFUTED / RE-SCOPED             -> the relay's premise moves and the scheme's shape
                                                 must be re-posed before anything is built.
  The three branches produce three different artifacts.  That is the whole reason to wait.

FREEDOMS_CONSUMED = NONE.  No scheme, no class parametrization, no pullback, no map, no domain
  specification, no test battery, no machinery.  My own 842 circularity finding was READ FOR GATE
  STATUS ONLY and NOT built upon.  SCALING WEIGHTS (law 2a): NONE CONSUMED.  SUBSTITUTED: NONE.
FLATTENING_CHECK = not applicable to a task not executed; no decline row engaged because nothing was
  constructed or classified.  I note that S03 and the void condition WOULD have been the live rows —
  a variation scheme is machinery whose shape has many tidy candidates — and that T5 would have been
  the standing wall.  The live discipline here was charter law 3, and it is the reason for the stop.

GATES HELD: no construction; no consumption of an un-upgraded premise; T5 untouched; derive-never-
  select untouched because nothing was derived; no smooth import; no EM identification; no member
  bound.  PE-1..PE-11 pointer-only.  Builder-B independence held.  ~/.codex untouched; memory-bank
  never searched.  No register, plan, tracker, git action.

CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+3 disclosures): (1) THIRD GATE STOP IN SIX RELAYS (839, 842 first pickup,
  844), and all three protected MY OWN un-cross-checked work from being built upon.  A lane that
  keeps stopping on gates that shield its own claims should be watched for using the cadence as
  cover, so in each I tested the candidate artifacts against the gate rather than declaring absence
  on a filename — and here I additionally tested and REJECTED the registrar's Q-746 entry, which
  states my circularity verdict in the very words the gate asks for.  (2) THE PREMISE THIS RELAY
  WOULD BUILD ON IS THE SINGLE MOST CONSEQUENTIAL CLAIM I HAVE MADE IN THIS BUILD, and it has never
  been attacked; I would rather it were attacked before it becomes a foundation than after.
  (3) I FLAG THAT LEG A AND LEG B ARE NOW BOTH WAITING ON THE SAME MISSING VERIFIER PASS, and that
  842 ran only because its gate opened on a re-invocation — the throughput constraint is the
  verifier cadence, recorded as a state of the campaign and not as a complaint.
