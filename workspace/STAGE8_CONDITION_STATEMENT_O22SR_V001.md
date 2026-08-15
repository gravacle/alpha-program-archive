# STAGE 8 — CONDITION STATEMENT (READING REPORT)

COMMISSION: O22SR
DATE: 2026-08-15
TYPE: QUOTATION AND RESTATEMENT ONLY. No derivation, no evaluation, no computation.

SOURCES READ (both seal-verified by `shasum -a 256 -c` in
`/Users/bgm/MB Work/alpha-program-archive/workspace`):

```text
STAGE8_W1_SUBVOLUME_RATE_O5SR_AUDIT_V001.md: OK
STAGE8_CERTIFICATION_RULES_O8SR_V001.md: OK
```

---

## (a) PASSAGE FROM `STAGE8_W1_SUBVOLUME_RATE_O5SR_AUDIT_V001.md`

Quoted verbatim with line numbers. Nothing elided from inside any sentence.

```text
211	> **AUDIT FINDING A-1 [DERIVED, REFUTES].** The `q = 2` Chebyshev bound, taken
212	> together with the sealed rank cap `N_n <= 4n^3`, **is sufficient** for a certified
213	> sub-volume rate (at exponent `3 - delta'` for every `delta' < delta`). Hence:
214	>   - "the necessary condition T-2c is *never* sufficient" is **FALSE**;
215	>   - "a boundary case sitting exactly on the failure line" describes **no boundary**:
216	>     T-2c and T-2d are equivalent up to arbitrarily small exponent loss;
217	>   - "the topology carrier MUST deliver `q` STRICTLY BELOW 2" is **not derived**.
218	>     The correct obligation is `q = 2` with a sub-volume prefactor `n^{3-delta}` —
219	>     which is exactly what a sub-volume rate already says. T-2's headline is
220	>     therefore **circular where it is not false**: after the correction, T-2c+T-2d
221	>     restate the rate rather than quantify a new obligation on the carrier.
```

Immediately surrounding context, quoted the same way (the derivation the finding
rests on, and the paragraph that states what the finding does and does not
deliver):

```text
186	### §3.3 The correct sufficiency statement, re-derived exactly
187	
188	Split the layer-cake integral at `s_0 = n^{-delta/2}`, using the cap below and the
189	`q = 2` bound above:
190	
191	```text
192	  int_0^{s_0} 2 s N_n(s) ds  <=  int_0^{s_0} 2 s (4 n^3) ds  =  4 n^{3-delta}
193	                                                             [AUDIT-CAS X1, exact]
194	  int_{s_0}^{2} 2 s N_n(s) ds <= int_{s_0}^2 2 s (c n^{3-delta} s^-2) ds
195	                              =  2 c n^{3-delta} ( ln 2 + (delta/2) ln n )
196	                                                             [AUDIT-CAS X2, exact]
197	  ----------------------------------------------------------------------------
198	  ||A_n||_2^2  <=  n^{3-delta} ( 4 + 2c ln 2 + c delta ln n )  =  O(n^{3-delta} log n)
199	                                                             [AUDIT-CAS X3, exact]
200	```
201	
202	and `n^{3-delta} log n` is **still sub-volume**: for every `eps` with
203	`0 < eps < delta`,
204	
205	```text
206	        n^{3-delta} log n / n^{3-(delta-eps)}  ->  0        [AUDIT-CAS X4, exact]
207	```
208	
209	so the exponent `3 - (delta - eps)` holds, with `delta - eps > 0`.
```

```text
241	**Net effect on the target's verdict: NONE adverse.** The correction removes a
242	positive claim about what the carrier owes. `RATE_CERTIFIED = false` stands
243	untouched — indeed §3.3 exhibits no rate, only an implication whose antecedent
244	(a `q = 2` counting bound with sub-volume prefactor, uniform in `n`) **no artifact
245	in the swept stock supplies**. The carrier is still owed; it is owed something
246	different from what the target says.
```

The sealed upper bound the finding turns on is stated earlier in the same file:

```text
160	The target's own T-1 proof opens: *"`A` has exactly `r` singular values
161	`s_1 >= ... >= s_r >= 0`"*. Independently, at the boundary-closure's own bytes
162	(`80db260f` :302), the cap is sealed ground:
163	
164	```text
165	"conversion from operator grade requires the rank factor: rank <= 4n^3 on
166	 ran C_n (of record)"
167	```
168	
169	Therefore, for every `n` and every `s > 0`, **`N_n(s) <= r_n = 4n^3`** — trivially,
170	since `N_n` counts a subset of the `r_n` singular values. This is not an extra
171	premise: it is the same sealed fact T-1 is built from, and it is available at every
172	`s`.
```

---

## (b) PASSAGE FROM `STAGE8_CERTIFICATION_RULES_O8SR_V001.md`

The passage classifying the first obstruction (FP-1) as unsupplied rather than
excluded, and referring back to the reasoning quoted in (a). Quoted verbatim with
line numbers, nothing elided from inside any sentence.

```text
505	### 4.2 FP-1 — **MIXED**, and the two halves are cleanly separable
506	
507	```text
508	THE DISPLAYED IMPOSSIBILITY (F1-b): re-derived here exactly.
509	  rank x op delivers 4n^3 . k against an n-FREE target; against any same-power
510	  carrier object (2n^3) the ratio is 2k — n-free, constant, never o(1)
511	  [CAS R4a/R4b].  THIS IS REAL AND EXACT.
512	ITS QUANTIFIER: **the rank x op ROUTE.**  It says that ONE conversion cannot
513	  close.  It says nothing about the existence of a sub-volume trace/HS rate.
514	IS AN OBJECT OF THE REQUIRED KIND EXCLUDED?  **NO — and the record positively
515	  derives the opposite.**  W1-AUDIT KILL 1, re-derived here exactly:
516	    with the SEALED rank cap N_n(s) <= 4n^3 reinstated and a q = 2 counting
517	    bound N_n(s) <= c n^{3-delta} s^{-2}, splitting the layer-cake integral
518	    at s_0 = n^{-delta/2} gives
519	       int_0^{s_0} 2s(4n^3) ds       = 4 n^{3-delta}                [CAS R4c]
520	       int_{s_0}^{2} 2s(c n^{3-delta} s^{-2}) ds
521	                                     = 2c n^{3-delta}(ln 2 + (delta/2) ln n)
522	                                                                    [CAS R4d]
523	       total / n^{3-(delta-eps)} -> 0  for every 0 < eps < delta    [CAS R4e]
524	    — SUB-VOLUME.  So a q = 2 counting bound with a sub-volume prefactor
525	    SUFFICES.  The threshold value q = 2 becomes sufficient up to a log
526	    precisely because a SEALED RANK CAP was reinstated.
527	AND A CLAIMED RULE AT THIS POINT WAS ITSELF REFUTED: W1-AUDIT KILL 2 struck
528	  the claimed admissibility gate "every admissible topology for W-1 must be
529	  generated by SYMMETRY-BREAKING seminorms" as a NON-SEQUITUR (hypothesis (a)
530	  inert in its own proof).  A constraint that had been carried as binding on
531	  the carrier turned out to constrain nothing.
532	CLASSIFICATION [DERIVED]:
533	  ON THE ROUTE           = MATHEMATICAL (impossibility displayed, exact).
534	  AT THE FAILURE POINT   = RULE-IMPOSED-BY-ABSENCE. No mathematics excludes
535	    the required object; a SUFFICIENT CONDITION for it is exhibited of record.
536	    What blocks is (a) that no member supplies it — an ABSENCE — and (b) the
537	    exclusivity word in F1-b (class (iii)) as hardened downstream.
538	  NET: **MIXED.**
539	```
```

The same classification appears in the file's front matter, quoted the same way:

```text
30	  FP-1 = MIXED — the rank x op ROUTE's failure is MATHEMATICAL and exact
31	    (4n^3 k / 2n^3 = 2k, n-free, never o(1); R4a/R4b).  The FAILURE POINT is
32	    RULE-IMPOSED-BY-ABSENCE: no mathematics excludes the sub-volume rate, and
33	    the W1-AUDIT positively DERIVED that a q = 2 counting bound TOGETHER WITH
34	    THE SEALED RANK CAP SUFFICES up to a log (re-derived here exactly, R4c-R4e).
35	    What blocks is that no member supplies it — plus the word "ONLY" in "the
36	    only SEALED conversion", which is an INVENTORY statement about the record's
37	    stock and is nowhere a nonexistence theorem.
```

And in the file's own check battery:

```text
1255	PASS R4e the total is SUB-VOLUME: total / n^{3-(delta-eps)} -> 0 for 0<eps<delta => a q=2 counting bound with a sub-volume prefactor SUFFICES. The FP-1 escape is therefore NOT excluded by mathematics — it is UNSUPPLIED
```

---

## (c) PLAIN RESTATEMENT OF THE CONDITION SAID TO BE ENOUGH

In my own words, reporting only what the two files say.

**What is said to be enough.** A counting bound on the singular values at the
borderline exponent — the value `q = 2` — is said to be enough, provided its
prefactor is already below volume order. Concretely, the condition is a bound of
the shape `N_n(s) <= c n^{3-delta} s^{-2}`: the number of singular values above a
threshold `s` is bounded by `s^{-2}` times a factor `c n^{3-delta}` that grows
more slowly than `n^3`, with `delta > 0`.

Both files say the reason the borderline value is enough is that it is not used
alone. It is combined with an upper bound on the count that is already sealed in
the record — the rank cap, `N_n(s) <= 4n^3` for every `n` and every `s`. The
files describe the mechanism as splitting the layer-cake integral at
`s_0 = n^{-delta/2}`: the sealed cap is used below the split point, where the
power-law bound is said to be vacuous, and the `q = 2` bound is used above it.
The two pieces are said to total to a sub-volume quantity, `O(n^{3-delta} log n)`,
which the files say still counts as sub-volume at exponent `3 - (delta - eps)` for
every `eps` in `(0, delta)`. The logarithm is the "up to a log" loss both files
mention.

**What would have to be true for the condition to apply.** Per the two files, the
`q = 2` counting bound with the sub-volume prefactor `n^{3-delta}` would have to
actually hold — and hold *uniformly in `n`*. The first file states the uniformity
requirement explicitly when it names the antecedent: "a `q = 2` counting bound
with sub-volume prefactor, uniform in `n`" (line 244). Elsewhere the same file
records that the constant `c` must be `n`-free for the conclusion to stand
(line 1060: "the sufficiency conclusion is VOID unless c is declared n-FREE").

So the structure both files present is an implication, not a result: *if* such a
bound is in hand, uniformly in `n` and with an `n`-free constant, *then* a
certified sub-volume rate follows. Neither file asserts the antecedent. The second
file's classification turns on exactly this: because no mathematics excludes the
object, and a sufficient condition for it is on the record, the first obstruction
is classified as **unsupplied** (an absence of a member who provides the bound)
rather than **excluded** (a theorem forbidding it).

---

## (d) DOES EITHER FILE SAY ANYONE HAS TRIED TO SHOW THE CONDITION IS TRUE?

**No such statement located.**

Searching both files for any statement that an attempt was made to establish the
`q = 2` counting bound with a uniform sub-volume prefactor, I found no such
statement. What both files state instead is the negative supply fact — that no
artifact or member provides it — together with an explicit disclaimer in the first
file that establishing it was deliberately not undertaken. Those statements are
quoted below so the distinction is visible, but none of them says anyone tried.

From `STAGE8_W1_SUBVOLUME_RATE_O5SR_AUDIT_V001.md`:

```text
243	untouched — indeed §3.3 exhibits no rate, only an implication whose antecedent
244	(a `q = 2` counting bound with sub-volume prefactor, uniform in `n`) **no artifact
245	in the swept stock supplies**. The carrier is still owed; it is owed something
246	different from what the target says.
```

```text
916	WHAT IS EXPLICITLY NOT DONE, so that no toy is smuggled in:
917	  - NO rate is derived, offered, or hinted at.  §3.3 exhibits an IMPLICATION whose
918	    antecedent nothing in the swept stock supplies; it is not a rate and is not
919	    offered as one.  RATE_CERTIFIED stays false in this audit exactly as in the target.
```

From `STAGE8_CERTIFICATION_RULES_O8SR_V001.md`:

```text
35	    What blocks is that no member supplies it — plus the word "ONLY" in "the
36	    only SEALED conversion", which is an INVENTORY statement about the record's
37	    stock and is nowhere a nonexistence theorem.
```

```text
536	    What blocks is (a) that no member supplies it — an ABSENCE — and (b) the
537	    exclusivity word in F1-b (class (iii)) as hardened downstream.
```

```text
1255	PASS R4e ... The FP-1 escape is therefore NOT excluded by mathematics — it is UNSUPPLIED
```

Each of these says the condition is *not supplied*. None of them says that any
member, artifact, audit, or lane attempted to supply it, and neither file records
a partial result, a failed attempt, or an assignment to attempt it. The only
occurrences of attempt language in either file are at
`STAGE8_CERTIFICATION_RULES_O8SR_V001.md` lines 448-449, and they concern a clause
repair and W-3's two readings of a clause — a different matter entirely, not the
`q = 2` counting bound.

---

END OF REPORT. No computation was run. No derivation was attempted. No file other
than the two named sources and a directory listing was read.
