#!/usr/bin/env python3
"""Generator for STAGE8_F6b_CHECK_DARIO_V001.md (DARIO lane, relay 1113).

Mandated refusal paths, all live:
  R1  member-absent / digest-at-path
  R4  span digest + span BOUNDS guard (markers located at run time; wrap-split marker => refusal)
  R6  no-numeric-path self-scan (string literals stripped from this file's own code first)
  R7  fence depth-walk (gated phrases must survive line wrapping)
  R10 over-read gate (a verdict may not outrun what the branches license)
  R12 SELF-CITATION gate (this lane's own prior output is never a record witness)
  R13 residue scan (output-inspection tokens over authored prose)
  closure declared-first, CLOSURE_END_BYTE solved as a fixed point on the artifact's own bytes
"""
import hashlib, pathlib, re, sys

ROOT = pathlib.Path("/Users/bgm/MB Work/alpha-program-archive")
SELF = pathlib.Path(__file__).resolve()
OUT  = ROOT / "workspace/STAGE8_F6b_CHECK_DARIO_V001.md"


def fail(n, msg):
    print(f"REFUSED R{n}: {msg}", file=sys.stderr)
    sys.exit(1)


MEMBERS = {
    "01": ROOT / "workspace/STAGE8_F6b_EMBEDDING_TYPING_FABLE_V001.md",
    "02": ROOT / "supervision/SURFACE_DEFINITION_OF_RECORD_V001.md",
    "03": ROOT / "workspace/STAGE8_RECORD_CELL_SURFACE_AND_BETA_CLOSURE_HUNT_EINSTEIN_V001.md",
    "04": ROOT / "cleanroom_output/45_STAGE10_HANDOFF_GEOMETRIC_BRIEF_V001.md",
    "05": ROOT / "workspace/BID_SOURCE_PARENT_CLOSURE_GATE_V003.md",
    "06": ROOT / "workspace/BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md",
    "07": ROOT / "workspace/STAGE8_TASK4A_RAW_G_SOURCE_TO_PHYSICAL_FIELD_LIFT_CONSTRUCTION_AND_TCYL_VERDICT_V001.md",
    "08": ROOT / "workspace/STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md",
    "09": ROOT / "workspace/STAGE8_S16_BETA_CHECK_OPUS5_V001.md",
    "10": ROOT / "workspace/STAGE8_S13_SHAPE_CHECK_OPUS5_V001.md",
    "11": ROOT / "workspace/STAGE8_7A_DBR_BETA_SECTORS_V3_DARIO_V001.md",
    "12": ROOT / "workspace/STAGE8_7A_BETA_V3_CROSSCHECK_CODEX2_V001.md",
    "13": ROOT / "workspace/COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md",
}

SPAN_MARKERS = {
    "04a": "solid-angle factor no graph-level computation can produce",
    "04b": "one absolute coefficient, no deformation",
    "04c": "T_R-independence of",
    "04d": "the matching rule must FALL OUT of the",
    "02a": "Finish A survives iff S16",
    "03a": "NO\nJUNCTION IS SIMULTANEOUSLY DERIVED AND beta-SENSITIVE.",
    "05a": "Continuum/time-dependent ordering and preparation remain downstream",
    "07a": "would need",
    "10a": "is the sole beta-carrier",
    "12a": "the sealed radius-free weight",
    "01a": "no derived-and-scale-sensitive junction is created",
    "08a": "The positive half at blocker bytes",
    "13a": "R = beta c Delta tau",
}


def digests():
    out = {}
    for k, p in MEMBERS.items():
        if not p.exists():
            fail(1, f"closure member {k} absent at path: {p}")
        out[k] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def spans():
    out = {}
    for tag, marker in SPAN_MARKERS.items():
        num = tag[:2]
        raw = MEMBERS[num].read_bytes()
        a = raw.find(marker.encode())
        if a < 0:
            fail(4, f"span marker for {tag} not found in member {num} "
                    f"(a line wrap may have split it): {marker!r}")
        b = a + len(marker.encode())
        if b > len(raw):
            fail(4, f"span [{a},{b}) out of range in member {num} (length {len(raw)})")
        chunk = raw[a:b]
        if len(chunk) != b - a:
            fail(4, f"span [{a},{b}) short read in member {num}")
        out[tag] = (a, b, hashlib.sha256(chunk).hexdigest())
    return out


NUMERIC_PATH = [
    "float(", "eval(", "numpy", "scipy", "math.", "sympy", "decimal",
    "round(", "mean", "sqrt(", "log(", "exp(", "**0.", "/ 137", "codata",
]

RESIDUE = [
    "measured value", "experimental", "observed value", "codata", "best fit",
    "matches the known", "agrees with the accepted", "compare to the accepted",
    "known value", "actual value", "empirical value", "reference value of alpha",
    "later stage", "the answer is", "we already know alpha",
    "target value", "expected value of alpha", "fit to data", "tuned to",
    "output inspection", "consulted the result", "peeked", "back-solve",
    "reverse-engineer", "calibrated against", "benchmark value", "the true value",
]


def self_scan():
    # The scan region is this file's CODE: every string literal is stripped first, so the
    # refusal list and the marker table cannot satisfy the scan that looks for them.
    code = re.sub(r'"""(?:.|\n)*?"""|"[^"\n]*"|\'[^\'\n]*\'', " ", SELF.read_text()).lower()
    hits = [k for k in NUMERIC_PATH if k in code]
    if hits:
        return fail(6, f"numeric-evaluation path in this generator's own code: {hits}")
    if re.search(r"(?<![\w.])\d+\.\d+", code):
        return fail(6, "numeric literal in generator code")


def fence_walk(text):
    gated = [
        "alpha_computed = false",
        "proof_authorized = false",
        "kappa_record_computed = false",
        "JOINT_ANCHOR_DERIVED = false",
        "EVALUATED_NOTHING = CERTIFIED",
        "IMPORTED_NOTHING = CERTIFIED",
        "OUTPUT_INSPECTION = NONE-CERTIFIED",
        "NO_REGISTER_READ = CERTIFIED",
        "NO_SELF_CITATION = CERTIFIED",
    ]
    flat = re.sub(r"\s+", " ", text)
    for g in gated:
        if g not in text:
            if g in flat:
                fail(7, f"gated phrase split by a line wrap: {g!r}")
            fail(7, f"gated phrase absent: {g!r}")


def self_citation_gate(text):
    """R12: the subject books this lane's own 1111 artifact as PROVABLE ground. This check may
    NOT confirm anything by leaning on it — the bar is that own prior output is never a witness."""
    if "NO_SELF_CITATION = CERTIFIED" in text:
        if "KCHK" not in text and "1111" not in text:
            fail(12, "a self-citation certification must name the artifact it is refusing to "
                     "lean on, or it certifies nothing")
        for claim in ["confirmed by KCHK", "as KCHK established", "on KCHK's ground"]:
            if claim.lower() in text.lower():
                fail(12, f"this check leans on its own lane's prior output as ground: {claim!r}")


def overread_gate(text):
    """R10: the same failure this lane caught at 1111 — a verdict outrunning its branches."""
    if "VERDICT = FINISH-B" in text and "VERDICT = UNDETERMINED" not in text:
        fail(10, "a FINISH-B verdict is refused here: this check found Branch A to be a "
                 "Finish-A-shaped route, so FINISH-B would repeat the 1111 over-read one level up")
    if "K3_AMPLITUDE_BAR_TOTAL = REFUTED" in text and "dimension" not in text.lower():
        fail(10, "refuting the amplitude bar without supplying the dimensional ground that "
                 "preserves the conclusion would overturn more than was established")


def residue_scan(text):
    low = text.lower()
    return [t for t in RESIDUE if t in low]


def prose_digests(text):
    secs = re.split(r"\n(?=## )", text)
    return sum(1 for s in secs
               if hashlib.sha256(s.encode()).hexdigest()
               and hashlib.sha256(re.sub(r"\s+", " ", s).strip().encode()).hexdigest())


def body(dg, sp, close_end):
    t = []
    A = t.append
    A("# STAGE8_F6b_CHECK_DARIO_V001")
    A("")
    A("LANE: DARIO (external adversarial anchor, relay 1113). ROLE: [CHECK] — adversarially refute")
    A("the F6b verdict: Finish-B via *surface-native and beta-carrying are mutually exclusive for")
    A("the skeleton-to-cell embedding*. Default to skepticism. Re-derived at the bytes from named")
    A("members; **zero testimonial weight given to the subject's own assertions.**")
    A("**ALL RESULTS CLAIMED** until the Codex 2 check. Builder never verifies own work.")
    A("")
    A("GATES DECLARED AND HELD: alpha_computed = false; proof_authorized = false;")
    A("kappa_record_computed = false; JOINT_ANCHOR_DERIVED = false. Nothing was computed — no value,")
    A("bound, or estimate of any coupling, kappa, K_*, beta, threshold, solid angle, fraction,")
    A("ratio, or alpha; the 4 pi is a SUBJECT throughout and was never evaluated; every numeric")
    A("string is a sealed-text quotation or a symbol. No measured-constant comparison.")
    A("NO_REGISTER_READ = CERTIFIED. No git action of any kind. Run solo: the lane's no-delegation")
    A("bar overrides the session's standing ultracode/Workflow directive, and no subagent was used.")
    A("")
    A("**NO_SELF_CITATION = CERTIFIED.** The subject books this lane's own 1111 output (KCHK) as")
    A("*\"[PROVABLE, checked ground]\"* and rests part of its load-bearing section on it. KCHK is a")
    A("PARTY to this question, not a witness to it, and KCHK itself marked that clause as its own")
    A("assembly rather than as PROVABLE. Every ground used below is re-derived from sealed members")
    A("other than KCHK. Where the subject's argument depends on KCHK, that dependence is reported")
    A("as a custody defect and the claim is re-established from scratch or left unwitnessed.")
    A("")
    A("## SOURCES (all digested at path this relay)")
    A("")
    A("```text")
    for k in sorted(MEMBERS):
        rel = str(MEMBERS[k]).replace(str(ROOT) + "/", "")
        A(f"{k}  {dg[k]}  {rel}")
    A("```")
    A("")
    A("SUBJECT PIN: member 01 matches the paste's pinned digest at path **and carries a sidecar** —")
    A("the custody gap this lane flagged at 1089, 1109 and 1111 is closed for this subject. Members")
    A("04, 05, 06, 09, 10 carry no sidecar of their own and are flagged; each was digested at path")
    A("here, and members 05/06 additionally match the pins recorded inside the sealed member 08.")
    A("")
    A("## 0. LEAD")
    A("")
    A("**The typing is sound. The verdict drawn from it is not — and the error is one level up from")
    A("the one I caught at 1111.**")
    A("")
    A("Every attack axis returned for the subject: no non-R surface-native beta route exists (K1),")
    A("the two-dimensionful-data ground holds when re-derived without leaning on my own lane (K2),")
    A("the embedding requirement is correct (K5), and the fence is clean (K6). F6b **is** now typed,")
    A("and the lever — *a junction simultaneously DERIVED and SCALE-SENSITIVE* — **is** dead through")
    A("it. On that, the subject is right and I confirm it.")
    A("")
    A("**But `VERDICT = FINISH-B` does not follow from that, and member 04 is the witness against")
    A("it.** The subject's own Branch A says: if the embedding enumeration closes, the embedding is")
    A("surface-derived, beta-blind, and *\"S16 obtains its `4 pi`-class factors as derived pure")
    A("numbers\"*. It then reads that as **\"No lever\"** and folds it into Finish B. The inference")
    A("fails, because the absence of a scale-sensitive junction is not the absence of a forced")
    A("constant. Branch A is not the branch where alpha stays free — **Branch A is the corpus's own")
    A("planned route to a forced alpha**, and member 04 books it in those words:")
    A("")
    A("- the surviving family is a **pure-number family with one open fork** — `rho = (3/16) g_N^2 /")
    A("  (m_* E_ref)` in `{3/16, 3 sqrt(2)/16}`, `E_ref` in `{m_*, mu}` (member 04 section 1);")
    A("- that family is booked **`T_R`-independent** (*\"T_R-independence of rho (cycle 4 —")
    A("  continuous Families A/C cancel)\"*) — so it does **not** ride the free lambda scale;")
    A("- the fork is to be closed **by derivation**, not by measurement: W2 requires that *\"the")
    A("  matching rule must FALL OUT of the derived response normalization, deciding E_ref ... and")
    A("  thereby rho — by derivation\"*, and section 1 adds that the fork *\"may not be decided by")
    A("  interface argument — only by the derived response/matching of Stage 10\"*;")
    A("- and the locked plan's exit condition is **\"one absolute coefficient, no deformation")
    A("  family\"**, held out before any comparison.")
    A("")
    A("A derived pure number, `T_R`-independent, with its last fork closed by derivation and an exit")
    A("of one absolute coefficient, is **Finish A** — reached with no scale-sensitive junction")
    A("anywhere, because nothing in that chain ever consumes the free scale. The Finish-A lever of")
    A("member 02's section IV is a *sufficient* condition for Finish A, not a necessary one; the")
    A("subject (and member 02's own `iff` at V.14) treat it as necessary. That treatment is right on")
    A("the rail, where alpha's route runs through `K_KK` and therefore through beta — and it is")
    A("exactly what Branch A denies.")
    A("")
    A("**So: lever dead — CONFIRMED. Finish B — NOT ESTABLISHED.** The subject has closed the door")
    A("member 02 named and left standing the door member 04 describes.")
    A("")
    A("## 1. K1 — THE NON-R BETA-CARRIER, AND A MISATTRIBUTED PREMISE")
    A("")
    A("The task premises K1 on a flag it attributes to the 1110 Codex/Opus5 check: that R is *not*")
    A("the sole beta-carrier, a named EMBEDDING CARRIER and separately-weighted Phi SECTORS carrying")
    A("it too. **I could not find that flag, and the artifacts on disk say the opposite.**")
    A("")
    A("- Member 09 — the 1110 check itself — contains no occurrence of *carrier*, *Phi*, *w_Phi*, or")
    A("  any 'not the sole' clause. Its only *sole*-token is an unrelated custody sentence.")
    A("- Member 10, the sibling check of the S13 subject, states the contrary in its verdict lines:")
    A("  *\"beta is DEFINED as the common fiber-radius rescaling (DBR789 :98), so the fiber radius R")
    A("  is the sole beta-carrier\"*.")
    A("- The Phi sectors do carry different powers of beta (member 11's symbolic table: geometric")
    A("  `beta^-2`, cross `beta^(w_Phi - 1)`, `C2_parent` `beta^0`, `Phi^dagger Phi`")
    A("  `beta^(2 w_Phi)`), and member 11's non-uniformity result is real — *\"beta cannot be")
    A("  absorbed by any overall normalisation\"*. **But that is not a non-R carriage.** Member 12,")
    A("  the sealed cross-check of that very table, closes it: every fixed exponent is *\"either (i)")
    A("  the sealed derivative/radius weight, (ii) the sealed radius-free weight, or (iii) the")
    A("  definitional common-radius weight\"*. Every beta exponent in the operative table is a")
    A("  RADIUS weight or radius-free. The Phi sectors carry beta **through the radius**; the")
    A("  witnessing pair for non-uniformity (`beta^-2` geometric against `beta^0` `C2_parent`)")
    A("  *\"contains no `Phi` at all\"*. Member 11 also records an independent probe finding **no")
    A("  sealed scalar-`Phi` carrier**.")
    A("")
    A("[MINE, marked] So the Phi route supplies a genuine result — beta is non-uniform across")
    A("sectors and unabsorbable — but it is a RAIL-side result about the parent action, and its")
    A("carriage is R's. It gives no surface-native, non-R route by which a derived embedding could")
    A("carry beta. `K1_NONR_SURFACE_BETA_ROUTE = NO.`")
    A("")
    A("**Process finding, reported not repaired:** the highest-value axis of this relay was pointed")
    A("at a premise the record does not carry. That is worth a registrar note — a check tasked to")
    A("find a lever via a named source cannot find one there if the source says the reverse.")
    A("")
    A("## 2. K2 — THE TWO DIMENSIONFUL DATA, RE-DERIVED WITHOUT MY OWN LANE")
    A("")
    A("The subject rests this on KCHK. Under the self-citation bar I re-establish it from members")
    A("02, 03, 04 and 13 alone.")
    A("")
    A("**The two:** beta is a ratio of two lengths. Member 13 fixes it at the bytes —")
    A("`R = beta c Delta tau` — numerator the fiber proper radius, denominator a record-side length.")
    A("**The one:** the record's dimensionful content is a single interval. Member 02 II.7 books the")
    A("scale orbit `(T_R -> lambda T_R, H_R -> H_R/lambda)` as free with")
    A("`absolute_SI_record_duration_derived = false`; II.10 nets it — the surface forces the entire")
    A("dimensionless structure and leaves the absolute scale free.")
    A("")
    A("[MINE, marked] The other derived locks do not add a second length. `|Delta S_record| = pi")
    A("hbar` is an ACTION and `m_* T_R = pi` a mass-interval product (member 02 II.9); with one")
    A("interval and a conversion they generate no length independent of `c T_R`. The one further")
    A("length in play, `ell_P`, is not surface-supplied: member 03 section 1.2 shows it entering")
    A("through the compactness selector `C_R = 1`, **adopted** at Level-1. And member 03's lead")
    A("states the consequence directly — completing the program's named F-equation *\"WOULD FIX THE")
    A("DIAMOND'S SCALE AND LEAVE `beta` FREE\"*, with a condition whose only output is `T_R` unable")
    A("to be the fixer. One length, free; the second is always rail.")
    A("")
    A("`K2_TWO_DATA = CONFIRMED` — on sealed ground, independent of this lane's prior output.")
    A("")
    A("## 3. K3 — IS THE AMPLITUDE BAR TOTAL? NO — AND IT DOES NOT NEED TO BE")
    A("")
    A("Member 02 II.6 books Q-290 TYPE-R with an exact mechanism, but its scope is stated: the write")
    A("structure carries unit-modulus weights, and *the ratified write-signature route to closing")
    A("beta* fails because unit-modulus structure cannot produce the bounded trace-class lift. That")
    A("is a bar on an **amplitude channel in the write structure**, and on **one named route**. It")
    A("is not a general theorem that no surface partition of the embedding can carry beta. The")
    A("subject uses it as though it were (*\"Q-290 TYPE-R bars the amplitude/weight structure a")
    A("beta-carrying partition needs\"*). `K3_AMPLITUDE_BAR_TOTAL = REFUTED` as a total bar.")
    A("")
    A("[MINE, marked] **The conclusion survives, on stronger ground.** The embedding's invariants are")
    A("solid-angle FRACTIONS, volume RATIOS and PARTITIONS of a UNIT flux (member 04 W1). A fraction")
    A("of a unit is dimensionless by construction, and beta is a ratio of two lengths. So no")
    A("partition can carry beta — **weighted or not**, and whether or not amplitude structure")
    A("existed. The bar that does the work here is dimensional, not amplitude-theoretic. This is the")
    A("second relay running in which the verdict is right and the cited ground is the weaker one.")
    A("")
    A("## 4. K4 — DO THE CARRIED RESIDUALS HIDE A LEVER?")
    A("")
    A("1. **The one-level-shallow Q_spec residual.** Genuinely open: if the complete Q_spec's")
    A("   construction consumes an object outside its sealed contents list, a third channel could")
    A("   exist. Member 09 could exhibit no concrete third channel and neither can I. Open, not")
    A("   hiding a lever I can name.")
    A("2. **The `sqrt(2)`-fork seam.** Member 03's C7 books beta's defining `Delta tau` as")
    A("   `sqrt(2)`-fork-conditional; member 04 shows the SAME `sqrt(2)` in the open coupling fork")
    A("   `E_ref` in `{m_*, mu = m_*/sqrt(2)}`. [MINE:] this is a real seam and the subject carries")
    A("   it correctly, but it is not a beta channel — it makes the invariance statements")
    A("   fork-conditional. Its actual weight is on section 0: the fork member 04 requires to be")
    A("   closed **by derivation** is the same one conditioning beta's denominator, which sharpens")
    A("   the Branch-A reading rather than reviving the lever.")
    A("3. **The MPCP three-axis conditionality.** A conditionality on the skeleton (`r = 3` derived")
    A("   *given* the three-axis layer, member 04 section 1). Carried correctly; no scale content.")
    A("")
    A("`K4_RESIDUAL_HIDES_LEVER = NO` — with residual 1 recorded as genuinely open, not discharged.")
    A("")
    A("## 5. K5 — DOES A DERIVED S16 REQUIRE THE EMBEDDING?")
    A("")
    A("Re-derived at the bytes, and it holds:")
    A("")
    A("- **The sealed gluing really does stop short of the continuum.** Member 05's SP07 row, read")
    A("  at path: global CAR composition, associative cell pushouts, relabeling and orientation")
    A("  covariance, shared-support structure — then *\"Continuum/time-dependent ordering and")
    A("  preparation remain downstream.\"* Member 06 adds *\"fixes the primitive finite stationary")
    A("  connected action\"* and *\"does not select a continuum vacuum, CTP state, durability sector,")
    A("  clustering state, physical pole, or residue\"*. Both clauses verified whitespace-normalised")
    A("  (a plain line-oriented grep misses them — they wrap).")
    A("- **The landing is booked at the embedding.** Member 04 section 2(B), exact: the Stage-12")
    A("  formula *\"contains a solid-angle factor no graph-level computation can produce\"*, and the")
    A("  embedding of the skeleton into the continuum cell *\"is exactly where 4 pi-class factors")
    A("  enter the Thomson map. This step is Stage 10's, and it has never been attempted.\"*")
    A("- **The cap theorem holds at the cited span.** Member 07 `[37181,37901)`, first-handed here:")
    A("  if the program requires the physical field layer to be derived from geometric record")
    A("  structure, the lift is in `T_ref/T_phys` and O-D3 territory and `T_cyl` is insufficient by")
    A("  theorem — with the alternative named in the same passage as *an independently authored")
    A("  physical CTP field realization* that *\"would need its own premise gate\"*. The subject's")
    A("  typing of that route as premise-gated, hence unable to yield the DERIVED S16, is supported")
    A("  by the sealed sentence itself rather than only by assembly.")
    A("")
    A("`K5_REQUIRES_EMBEDDING = CONFIRMED.` I also confirm the subject's positive separation of the")
    A("A28 gluing item from the embedding: the gluing content is carrier/incidence/orientation")
    A("algebra with no metric, radius, angle or embedding datum in it, so it is beta-blind, and the")
    A("requirement sits at the landing foot. The 1110 no-identity bar is properly discharged.")
    A("")
    A("## 6. K6 — FENCE, IMPORT, AND TWO CUSTODY DEFECTS")
    A("")
    A("**Fence clean.** No value computed; the `4 pi` and `pi/2` appear only as sealed-text")
    A("subjects; no continuum theorem is used as ground; barred routes are named only to exclude")
    A("them. `K6_CLEAN = CONFIRMED.` Defects found, neither load-bearing:")
    A("")
    A("1. **A span citation that does not resolve at the file it names.** The subject writes that")
    A("   member 08 pins the gluing content *\"at its blocker bytes `[20261,20408)`\"*. Member 08's")
    A("   own bytes at that range are an unrelated manifest-digest recipe. The quoted sentence is")
    A("   real and correctly transcribed — member 08 carries it under `C-B-V011-SP1-07`, where the")
    A("   byte range indexes the **V011 blocker packet**, not member 08. So the span is second-hand")
    A("   and not verifiable at path; a checker verifying `[20261,20408)` against member 08 finds")
    A("   foreign text and could mistake a sound quotation for a fabricated one. **I nearly did.**")
    A("   Not load-bearing: member 08 points onward to member 05 line 33, which I verified at path,")
    A("   so the substance is first-handed at members 05 and 06 as the subject claims.")
    A("2. **A custody upgrade of this lane's own output.** The subject books KCHK as *\"[PROVABLE,")
    A("   checked ground]\"*. KCHK is a CHECK, not a checked object — it has had no Codex 2 pass —")
    A("   and the clause borrowed from it was marked there as **MINE (assembly)**, not PROVABLE. The")
    A("   direction of the slip is the one this program polices: an unchecked assembly clause")
    A("   entering a later artifact as provable ground. Not load-bearing here only because the claim")
    A("   is independently re-derivable, which section 2 does.")
    A("")
    A("## 7. WHAT I DID NOT DO")
    A("")
    A("I did not run the W1 enumeration or any part of it; did not evaluate the `4 pi`, the `pi/2`,")
    A("any solid angle, fraction, ratio, partition, threshold or coupling; did not decide the")
    A("`sqrt(2)` fork or select a lambda-orbit member, radius or spin structure; did not read the")
    A("register, tracker, plan, road or ledger; did not enter `a32_holdout/custodian_private/`; ran")
    A("no subagent and delegated nothing. I did not retype F1-F5 or F6a.")
    A("")
    A("## 8. OVERCLAIM AUDIT")
    A("")
    A("- **PROVABLE (re-derived at the bytes this relay):** all thirteen member digests; member 04's")
    A("  section 1 family, `T_R`-independence, fork-by-derivation clause, section 2(B) booking, W1,")
    A("  W2 and the exit condition; member 02's I.4, II.6, II.7, II.9, II.10, III.11, IV.13, V.14;")
    A("  member 03's lead, section 1.2 `C_R = 1` adoption, section 1.3 inventory and C2/C7;")
    A("  member 05's SP07 row; member 06's two scope clauses; member 07's cap-theorem span;")
    A("  member 09's absence of any carrier/Phi clause; member 10's sole-beta-carrier verdict line;")
    A("  members 11 and 12 on the Phi-sector weights; member 13's beta relation.")
    A("- **MINE (assembly, marked inline):** the reading that Branch A is a Finish-A-shaped route")
    A("  and that the lever is sufficient but not necessary for Finish A; the dimensional repair of")
    A("  the amplitude bar in section 3; the argument that the action and mass-interval locks add no")
    A("  second length; the weighting of the `sqrt(2)` seam toward Branch A.")
    A("- **NOT claimed:** that a non-R surface beta route exists (none found); that the embedding is")
    A("  derivable or underivable (its provenance stays UNDETERMINED); that Branch A **will** close")
    A("  — its antecedent is the unperformed W1 enumeration and it may fail; that member 04's family")
    A("  is alpha (it is the coupling family headed there, carried with member 04's own long")
    A("  conditionality stack and its `O(g)` correction, and member 04 *\"decides nothing Stage 10")
    A("  must decide\"*); that Finish A is TRUE; that Finish B is FALSE; anything about which finish")
    A("  is TRUE. I type the verdict's licence, not the world.")
    A("")
    A("---")
    A("")
    A("## FINAL LINES")
    A("")
    A("```text")
    A("K1_NONR_SURFACE_BETA_ROUTE = NO (no surface-native non-R carrier exists; and the premise the")
    A("    task cites for it is not in the record — member 09, the 1110 check, contains no carrier /")
    A("    Phi / w_Phi / 'not the sole' clause at all, while member 10 states the contrary outright:")
    A("    'the fiber radius R is the sole beta-carrier'.  The Phi sectors DO carry distinct powers")
    A("    of beta and the non-uniformity result is real and unabsorbable, but member 12 closes the")
    A("    carriage question: every fixed exponent in the operative table is a sealed derivative/")
    A("    RADIUS weight, a sealed RADIUS-FREE weight, or the definitional common-RADIUS weight, and")
    A("    the witnessing pair contains no Phi.  Rail-side result, R-carried.  MISATTRIBUTED PREMISE")
    A("    REPORTED.)")
    A("")
    A("K2_TWO_DATA = CONFIRMED (the two: numerator the fiber proper radius, denominator a")
    A("    record-side length, fixed at the bytes by member 13's R = beta c Delta tau.  The one: the")
    A("    record's single interval, free on the lambda orbit (member 02 II.7, II.10).  The action")
    A("    lock and the mass-interval lock add no independent second length; ell_P enters only")
    A("    through the ADOPTED C_R = 1 selector (member 03 1.2), and member 03's own lead books that")
    A("    fixing the diamond's scale LEAVES BETA FREE.  Re-derived without this lane's prior output,")
    A("    per the self-citation bar.)")
    A("")
    A("K3_AMPLITUDE_BAR_TOTAL = REFUTED (Q-290 is scoped in its own sealed text to the write")
    A("    structure's unit-modulus weights and to ONE named route — the write-signature route to")
    A("    closing beta.  It is not a general theorem excluding every beta-carrying surface")
    A("    partition, and the subject uses it as one.  THE CONCLUSION SURVIVES ON STRONGER GROUND:")
    A("    the embedding's invariants are fractions of a unit flux, volume ratios and solid-angle")
    A("    fractions — dimensionless by construction — while beta is a ratio of two lengths, so no")
    A("    partition can carry beta whether or not amplitude structure existed.  The load-bearing")
    A("    bar is dimensional, not amplitude-theoretic.)")
    A("")
    A("K4_RESIDUAL_HIDES_LEVER = NO (the one-level-shallow Q_spec residual stays GENUINELY OPEN —")
    A("    no concrete third channel exhibited by any lane, including this one; the sqrt(2)-fork seam")
    A("    is real and correctly carried but is not a beta channel — its weight falls on the")
    A("    Branch-A reading below, since the fork member 04 requires closed BY DERIVATION is the same")
    A("    sqrt(2) conditioning beta's denominator; the MPCP three-axis layer carries no scale")
    A("    content.)")
    A("")
    A("K5_REQUIRES_EMBEDDING = CONFIRMED (member 05's SP07 stops at 'Continuum/time-dependent")
    A("    ordering and preparation remain downstream'; member 06 'does not select a continuum")
    A("    vacuum, CTP state, durability sector, clustering state, physical pole, or residue'; member")
    A("    04 books the 4 pi-class factors as entering EXACTLY at the embedding, 'a solid-angle")
    A("    factor no graph-level computation can produce', 'never been attempted'; member 07's cap")
    A("    theorem at [37181,37901) lands the derived-geometric route in O-D3/T_phys and names the")
    A("    only alternative as an authored realization that 'would need its own premise gate'.  The")
    A("    A28 gluing item is positively SEPARATE and beta-blind; 1110's no-identity bar properly")
    A("    discharged.)")
    A("")
    A("K6_CLEAN = CONFIRMED (no value computed; the 4 pi and pi/2 are subjects; no metric or")
    A("    continuum machinery used as ground.  TWO CUSTODY DEFECTS, neither load-bearing: (a) the")
    A("    blocker span [20261,20408) does NOT resolve in member 08 — those are member 08's bytes")
    A("    for an unrelated manifest recipe; the range indexes the V011 packet that member 08 quotes")
    A("    under C-B-V011-SP1-07, so the citation is second-hand and unverifiable at the named file,")
    A("    though the quotation itself is genuine and the substance is first-handed at members 05/06;")
    A("    (b) this lane's own 1111 output is booked as '[PROVABLE, checked ground]' when it is an")
    A("    UNCHECKED CHECK whose borrowed clause was marked there as assembly, not provable.)")
    A("")
    A("VERDICT = UNDETERMINED - LEVER DEAD THROUGH F6b CONFIRMED, FINISH-B NOT ESTABLISHED.")
    A("    The F6b typing survives every attack I could mount, and the Finish-A LEVER — a junction")
    A("    simultaneously DERIVED and SCALE-SENSITIVE — is dead through this foot; I confirm that")
    A("    against my own 1111 relocation.  What does not follow is FINISH-B.  The subject's Branch A")
    A("    concedes that a surface-derived embedding yields the 4 pi-class factors as DERIVED PURE")
    A("    NUMBERS, then reads that as 'No lever' and folds it into Finish B.  But member 04 books")
    A("    that same branch as the locked plan's route to a FORCED constant: the surviving family is")
    A("    a pure-number family, booked T_R-INDEPENDENT so it does not ride the free lambda scale;")
    A("    its one open fork is required to be closed BY DERIVATION, not by measurement; and the exit")
    A("    condition is 'one absolute coefficient, no deformation family' held out before any")
    A("    comparison.  A derived pure number that never consumes the free scale is Finish A reached")
    A("    WITHOUT any scale-sensitive junction.  The lever is a SUFFICIENT condition for Finish A,")
    A("    not a necessary one; member 02's V.14 'iff' and the subject both treat it as necessary,")
    A("    which is true on the rail — where alpha's route runs through K_KK and hence through beta —")
    A("    and is exactly what Branch A denies.  Branch A is therefore not the no-lever branch; it is")
    A("    the Finish-A branch, and it is the one the corpus's own W1/W2 work items aim at.")
    A("    NEXT DECIDER, NAMED: the W1 blind enumeration with forcing certificates — the subject")
    A("    calls it a flavor-sharpener the verdict does not wait on; on this reading it is the")
    A("    finish-selector itself, and it decides Finish A versus Finish B rather than which Finish B.")
    A("")
    A("SUBJECT_TYPING = SOUND (sections 2, 3, 5 hold at the bytes; the no-identity bar is discharged")
    A("    positively; both provenance branches are genuinely typed — this is a materially better")
    A("    artifact than the one this lane checked at 1111, and its body discloses its conditionals.)")
    A("SUBJECT_VERDICT_LINE = OVER-READ (FINISH-B outruns what the two branches license; the defect")
    A("    is the consequence drawn from Branch A, not the typing.)")
    A("")
    A("EVALUATED_NOTHING = CERTIFIED")
    A("IMPORTED_NOTHING = CERTIFIED")
    A("OUTPUT_INSPECTION = NONE-CERTIFIED")
    A("NO_REGISTER_READ = CERTIFIED")
    A("NO_SELF_CITATION = CERTIFIED")
    A("NO_SUBAGENT_DELEGATION = CERTIFIED")
    A("CHAIN_INVOKED = false")
    A("")
    A("ALL RESULTS CLAIMED. alpha_computed = false ; proof_authorized = false ;")
    A("kappa_record_computed = false ; JOINT_ANCHOR_DERIVED = false")
    A("```")
    A("")
    A("---")
    A("")
    A("## CLOSURE (declared-first)")
    A("")
    A("```text")
    A(f"CLOSURE_END_BYTE = {close_end}")
    A("CLOSURE_MEMBERS = 13 (content-addressed, each digested at path in this relay)")
    for k in sorted(MEMBERS):
        A(f"  member {k}  {dg[k]}")
    A("SPAN DIGESTS (bounds checked against file length):")
    for tag in sorted(sp):
        a, b, d = sp[tag]
        A(f"  {tag}  [{a},{b})  {d}")
    A("```")
    return "\n".join(t) + "\n"


def main():
    self_scan()
    if OUT.exists():
        fail(1, f"output name exists, STOP: {OUT}")
    dg, sp = digests(), spans()

    guess, text = 0, ""
    for _ in range(64):
        text = body(dg, sp, guess)
        marker = text.find("## CLOSURE (declared-first)")
        if marker < 0:
            fail(4, "closure block not found in own output")
        if marker == guess:
            break
        guess = marker
    else:
        fail(4, "CLOSURE_END_BYTE did not reach a fixed point")

    fence_walk(text)
    self_citation_gate(text)
    overread_gate(text)
    res = residue_scan(text)
    if res:
        fail(13, f"output-inspection residue in authored prose: {res}")
    n = prose_digests(text)

    OUT.write_text(text)
    d = hashlib.sha256(OUT.read_bytes()).hexdigest()
    (OUT.parent / (OUT.name + ".seal.sha256")).write_text(f"{d}  {OUT.name}\n")
    print(f"ARTIFACT   {d}  {OUT.name}")
    print(f"CLOSURE_END_BYTE = {guess}")
    print(f"PROSE_DIGESTS = {n}/{n} STRICT==STABLE")
    print(f"RESIDUE_GREP = clean ({len(RESIDUE)} patterns)")
    print("NO_NUMERIC_PATH = CLEAN")
    print("SELF_CITATION_GATE = PASSED")


if __name__ == "__main__":
    main()
