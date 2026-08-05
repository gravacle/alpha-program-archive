## PASTE 554 — CODEX LANE 1 (HIGH EFFORT) — [TASK 5 / EQ6] REVIEW OF RECORD: THE PARTIAL JOINT DIAMONDS

PREFLIGHT (verify before starting; report any failure and STOP):
- Register head: Q-478.
- Artifact under review (Lane 2's build): `alpha-program-archive/workspace/STAGE8_TASK5_EQ6_PARTIAL_JOINT_DIAMONDS_LANE2_V001.md`
  SHA-256 `5539b53ddeb208638af314f34e018591e1e6bd93403906e6a5edd46bc34e4766`. Verify before reading.
- Your standards: the confirmed V003/V004 assembly (`a46beae2…`, `9bf34e27…` — you built the faces), FC11's original statement (one finite fiber-product term including the contact cocycle), the scoped mate cert you just built (`088eccd9…` — its SCOPE_MATCHED square is what a J2 face would plug in).
- SPARK-VERDICT protocol: recompute; your verdict carries a Sol re-check obligation.

TASK — PASS/KILL per item:
U1. **The partial term:** verify the five-component fiber product genuinely commutes on at least two actual common-refinement diamonds — recompute the faces from YOUR OWN confirmed constructions (you built them; check the diamonds use them correctly, not look-alikes).
U2. **The contact cocycle:** verify its passage through the A4 pushout on one nontrivial overlap.
U3. **The J2/J7 contract (D2):** audit against the J2 statement AND against your scoped mate cert — is the contract satisfiable by the SCOPED J2 form (the projected old-image square), or does it silently demand the full square that is blocked/failing? If the contract over-demands, state the corrected contract exactly.
U4. **The completion theorem (D3):** verify the proof; hunt for a hidden coherence the gap audit missed (the historical trap: a simultaneity condition visible only when all six components are present).
U5. **One fresh attack.**
Final lines: `PARTIAL_DIAMONDS = CONFIRMED / DEFECTIVE (+items)`, `CONTRACT = COMPATIBLE_WITH_SCOPED_J2 / OVER-DEMANDS (+correction)`, `COMPLETION_THEOREM = CONFIRMED / GAP (+item)`.

OUTPUT: one artifact, lane-tagged filename
`STAGE8_TASK5_EQ6_DIAMONDS_REVIEW_LANE1_V001.md`
If the output filename already exists in the workspace, STOP and report — do not overwrite. Seal, mirror byte-identically to `alpha-program-archive/workspace/`, verify, report hashes, STOP. No register, plan, tracker, git, commit, or push action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants. If a fence blocks a structural result, flag MACHINERY-APPEAL and continue.
