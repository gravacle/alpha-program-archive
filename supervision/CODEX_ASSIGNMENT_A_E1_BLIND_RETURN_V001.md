# Codex Assignment A — E1 Blind Diagnosis and Replacement Routes (verbatim)
Received 2026-07-26 via Brian's relay. Recorded verbatim for citation by hash.
An INDEPENDENT-SYSTEM lane (Codex, not this construction lane's model family),
run BLIND to this lane's IR memo, E1 successor spec, and every E1
replacement-route artifact. Its blindness attestation and custody-hash
confirmation are part of the return.

---

Stage-8 T7 E1 Blind Diagnosis And Replacement Routes V001

Blindness note: I did not open /Users/bgm/MB Work/alpha_supervision/ROUTE_MEMO_2026-07-26_ir_sea_kernel_attack.md, STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V001.md, or any E1 replacement-route artifact. I skipped CONTINUATION_STATE.md sections 207-274 and 495-553 as potential IR/E1 framing. Custody hash remained confirmed: d8b587a1423dc48ef1b1a53b64260df1a12a3f97e90ca03dafefbdba660be5db.

Diagnosis

The divergence is primarily a bound-class failure at the n=1 single-cell coincidence limit, not yet a proven divergence of the completed theory. The old E1 bound defines K_sea as a positive trace-norm/action-density supremum over admitted cells, with the kernel localized by the sharp record localizer. In the Phase-1 draft, K_sea is exactly the per-cell, per-4-volume sea covariance trace functional; the draft records that the sealed corpus only gives a |x|^-3 decay class and that the naive positive kernel integral log-diverges at coincidence. See MAJORANT_LEMMA0_PROOF_DRAFT_V001.md line 525.

The sharp boundary is not my first diagnosis. A discontinuous localizer can worsen trace/Schatten certification and must be tested, but the fatal local integral is the volume diagonal x=y; smoothing only the boundary will not by itself remove a |x-y|^-3 positive majorant. The supremum over admitted cells is also not the root; it is the enforcement mechanism that prevents hiding the problem in a chosen carrier, truncation, or cell size. The actual root is: absolute trace-norm majorization was taken before using the CTP, determinant-ratio, oscillatory/PV, and completed-normalization cancellations that might make the object finite.

The completed-chain constraint is binding: there is no unitality anchor. The completed object is normalized by Z_hat_comp = Z_comp / Z_comp(0), with Z_comp(0) != 0 a named hypothesis, not a structural identity. See STAGE8_T7_CONNECTED_LINKED_CLUSTER_MAJORANT_DERIVATION_SPEC_V001.md line 109 and STAGE8_T7_COMPLETED_CONDITIONED_DUHAMEL_IDENTITY_AND_INTERCHANGE_SCHEMA_SPEC_V001.md line 177.

Replacement Routes

1. Cancellation-first CTP determinant route. Prove the majorant directly for the pair-holomorphic completed functional Ghat_K(z,w), bounding determinant/log differences after CTP subtraction and baseline normalization, not the raw sea trace norm. It must prove per-K zero-freeness, uniform intensive bounds, action-density cluster estimates, and M3 over the full D3 quantifier. It is refuted if the cancellation-preserving determinant difference still has a certified nonintegrable |x|^-3 lower obstruction. This does not initially exclude the sharp localizer as an object; it only tests whether the old positive bound threw away essential cancellation.

2. Renormalized single-cell anchor route. Isolate the n=1 activity as a separately certified completed single-cell factor, then prove the linked-cluster majorant for the residual connected activities. This must be an exact identity for -Log Z_hat_comp, not a subtraction by convention. It must prove the one-cell term is finite/certified and that all n>=2 activities satisfy the action-density KP bound uniformly. It is refuted if the single-cell term remains noncertifiable without changing the completed object. If refuted there, the sharp localizer becomes a candidate obstruction to the bound class.

3. Smooth-localizer sharp-limit classifier. Introduce a sealed smooth localizer family approaching Q 1_(|x|<=r(t)) Q, prove the completed-chain majorant with constants uniform in the smoothing parameter, then take the sharp limit in Ghat_K, logs, and Hessians. It is refuted if the constants necessarily grow like the coincidence logarithm or zeros accumulate in the sharp limit. This is the route that can honestly terminate in "sharp localizer obstruction," but only if the obstruction survives cancellation-first and completed-normalized formulations.

Frozen Predictions

Route 1 is the best survivor. Route 2 survives only if formulated as an exact completed-normalization identity, not as a counterterm choice. Route 3 is most valuable as a classifier; prediction: it will show the sharp projector is an obstruction to the old positive trace-norm bound, not yet to the completed object itself.

Protected status remains unchanged: alpha_computed=false, proof_authorized=false, no production verdict, no coupling, no alpha.
