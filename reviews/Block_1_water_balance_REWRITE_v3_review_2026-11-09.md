# Review: Block 1 rewrite v3 (Sections 6.2, 6.3, 7.1)

Date: 9 November 2026. Block: `drafts/Block_1_water_balance_REWRITE_v3.md`. Panel: surface-water hydrologist (SW), groundwater hydrogeologist (GW), literature verifier (LV), academic editor (ED). Flood and water-quality reviewers were not used (no such claims in the block). Each reviewer worked independently from the same task. Nothing in the block or any other project file was edited.

Basis of checking: numbers recomputed from the sw1 workbook with `openpyxl` (`data_only=True`) by SW, GW and ED; SW also recalculated copies of sw1 and sw2 in LibreOffice. Sources: only Hashimoto (1982) could be read in full. DWAF (2004), Pyburn (2015), Peterson et al. (2021), Fowler et al. (2022), Kapangaziwiri et al. (2011) and Moriasi et al. (2007) could not be opened in this session (hosts not on the network allow-list). Their status below rests on the verification report of 8 November and is marked "unverified" where it is not first-hand.

Almost every printed number reproduces (see D). The problems lie in what the numbers are used to show, in four citations, and in terminology and density.

---

## A. Clear errors

Ranked by severity.

**A1. "Very low confidence" is not in DWAF (2004). Major.** 7.1, third paragraph: the Department "reports that the hydrological information of the Marico has not been updated since the agreement of 1988 and is of very low confidence (DWAF, 2004:83)". The verification report (8 November) says the phrase is not in the report and that p. 83 refers only to the agreement, with no year given. (LV C9, SW 7, ED 29.) Status: the author is still confirming p. 83 (context §5); DWAF could not be opened here. Until confirmed, keep only wording confirmed from p. 83, mark "1988" unverified, or attribute "very low confidence" to this study.

**A2. Fowler et al. (2022): the reason clause is not in any source read. Major.** 7.1: "...only as a possible contributor, since the dams are not numerous or large enough". The citation inventory records that Fowler was never opened. The verification report gives only the ratings (groundwater storage "plausible", farm dams "in-between"). "Among the plausible explanations" also implies several; the report names one. No page given. (LV C14, GW H13, SW 25, ED 33.) Fix: open the paper (HESS 26:6073–6120) and cite the section, or cut the clause.

**A3. Pyburn (2015) statements go beyond what is verified. Major.** (LV C10–C11, GW H14, SW 26, ED 31–32.)
- "Springs of the Zeerust dolomite declined to almost nil in 1986": the earlier check places this on p. 45 and ties it to the Paardenvallei springs. The general wording may over-generalise.
- "in a period of little recharge": Pyburn gives no cause for the decline (context §5). Whether "little recharge" is his wording or the article's reading, and whether p. 113 carries it, is unverified. "Until the rains of 1996" is also unverified.
- "since the Rietpoort Well Field was commissioned in 1974 and the Rietpoort Spring ceased flowing ten years later": "since" turns two dated facts into a cause. The approved text says Pyburn, reviewing earlier work, reports that the well field caused the spring to stop; v3 only sets the two side by side. The name "Rietpoort Well Field" is not in the approved text. 1974, "ten years later" and "low rainfall" (p. 5) are unverified.
Fix: the author reads pp. 5, 45 and 113 and the wording follows what Pyburn says.

**A4. "The drought" has five different spans, and 1995 sits on both sides of its end. Major.** (ED 1, SW 17.)
- 6.3: "1995 and 1996, the two years after the drought". Table 6 and its caption put hydrological year 1995 inside the drought column ("the hydrological year in which the dam recovered"). Hydrological year 1995 runs October 1995 to September 1996; the 146-month event ends in January 1996.
- Spans used: October 1983–September 1995 (Introduction), December 1983–January 1996 (6.3), 1987–1995 (Table 6), 1982–1994 (inflow below medians), "1983 to 1995" (7.1).
- Table 6 "drought" column includes the recovery (storage rose to 46–67% in 1996; change in storage +0.35). Without 1995, evaporation takes 64% of what entered the dam, not "about half" (SW 17).
Fix: define the drought once, label other spans by date, and state that "1995 and 1996" are hydrological years. The Table 6 column label is the author's decision (B14).

**A5. "Net contribution of the reach" is undefined, and "did not come from the upper dam" overstates. Major.** 6.2. (ED 2, GW H7, SW 13.)
- The block does not say what the net contribution is made of. "Inflow" also names four different things (WR2012 patched flow, Table 6 remainder, simulated series 1, inflow to Kromellenboog).
- The remainder of Kromellenboog's balance is net of river abstraction and includes return flow of canal water (Q2!A3: these cannot be separated). The canal carried 0.30 Mm³/a in 1987–1995 against 1.78 in 1996–2009, so part of the rise from 3.80 to 5.80 Mm³/a may be return flow of upper-dam water. The workbook's lower bound for A31E runoff is 3.79 Mm³/a (Q2!D57). The 98% for the drought stands, because the canal carried so little then.
Fix: define the term once; use "was not passed on by the upper dam as spill or release", or state the return-flow caveat.

**A6. Wilgeboomspruit: the two means are not labelled with their periods. Major.** 6.2: "Its mean to the end of the record in August 1992 was 0.69 Mm³/a, a third of the flow before 1984". The 0.69 is the mean from April 1988 (49 valid months), not from February 1984; 2.10 is the mean of 162 valid months before February 1984. Both reproduce (0.686 and 2.101; ratio 0.33). (ED 4, GW, SW 11.) Whether "a third" is the right comparison is an interpretation (B11).

**A7. "More than three times the canal volume" holds for 1995 and for the two years together, not for 1996. Minor.** Recomputed: 1995 is 4.1 times, 1996 is 2.9 times, the pair 3.3 times (1.70 + 2.10 against 0.41 + 0.73). (ED 12, SW 3.) Say "together". The two years carry 49% of the 5.40 Mm³ excess.

**A8. "Although the zone rainfall exceeded 100 mm in four of these months": one of the four months had flow. Minor.** January 1985 (121 mm) had flow; the other three (March 1984 106 mm, January 1988 111 mm, February 1988 211 mm) did not. Flow resumed in April 1988 after about 420 mm in January–March 1988. (GW H11, SW 29.) Reword without "although"; the response is that of a store with a deficit.

---

## B. Interpretations the author must decide

Ranked by severity. None of these is settled by the panel.

**B1. The "lower bound" is not a bound (critical).** 6.3 gives reliability by time "59% to 87%"; 7.1 says "The result is therefore a range". The value 0.590 is the rule fitted on both periods. Fitted on the test period alone it gives 0.393 and a longest event of 169 months; fitted on the fit period alone, 0.586 (Sens rows 32–33). So the rule side of the range depends on the rule chosen and is not bounded at 0.59. (SW 1, ED 20, 38.) The v3 note says the 6.3 paragraph on rule sensitivity ("0.59 to 0.39") is "unchanged"; it was in fact removed, and 7.1 ("the two periods of the record give different rules") now rests on a result the block does not show.
- Option 1: keep "bound", and report the test-period-only result (0.39) next to the range. Cost: the range widens to roughly 0.39–0.87 and the headline weakens.
- Option 2: drop "bound" for the rule run; call 0.59 "the rule fitted on both periods" and say the range is conditional on the rule. Cost: the lower/upper bound language used elsewhere in the article must change.
- Option 3: restore the deleted sentence with 0.586 and 0.393, and leave the framing. Cost: the reader meets two ranges.

**B2. How the cause of the low inflow is argued (7.1, last paragraph).** The paragraph presents two separate explanations outside A31E. Reviewers raise several points; the author decides which enter the text. (GW H1–H6, H14–H16, SW 9, 27, ED 35–37.)
- The two explanations act on the same aquifer and are not exclusive: the well field pumped from 1974, and a spring stops when heads fall below its outlet. "Natural decline" cannot be asserted while pumping is under way.
- Onset against persistence. Inflow was below the median from 1982 (patched 2.14, 0.59, 1.50, 0.97 Mm³ for 1982–1985) while zone rainfall was 454, 378, 347 and 386 mm against a mean of 597 to 599 mm (1981–1986 mean 451 mm, the longest below-mean run since 1920). The onset is consistent with rainfall. The 1986 spring decline can bear only on persistence through 1987–1990, when rainfall was 693, 660, 631 and 682 mm and inflow was 1.07, 0.45, 0.67 and 0.89 Mm³.
- "Little recharge" in 7.1 and "above the long-term mean" in 6.2 read as contradictory. They can be reconciled through episodic recharge or the refilling of a storage deficit; the block offers neither.
- The Wilgeboomspruit (no dolomite, no known well field) also stopped in February 1984, the same time as the Rietpoort Spring. Dry years alone can stop a perennial stream in the region. It resumed in April 1988 while the dam inflow stayed very low. This contrast is the strongest evidence in the study that persistence lies in the dam's own catchment, and 7.1 does not use it.
- The inflow recovered after 1996 (1996–2009 mean 4.67 Mm³/a, above the 3.94 median) while the well field presumably still operated. This constrains the upstream-use explanation. Peterson et al. concerns catchments that did not recover; this inflow did, as the approved text said and v3 dropped.
- The fall to be explained is roughly 3 Mm³/a (median 3.94 against a 1985–1994 mean of 1.01). The second explanation can be sized only if Pyburn gives abstraction rates.
- That the springs' water reaches the dam "is inferred from the position of the dolomite": position shows only that springs lie in the surface catchment; groundwater divides in dyke-bounded compartments need not follow surface divides. The dam's catchment is 54.2% dolomite (629.6 of 1 162 km²).
- Options: (a) keep two explanations as written, with the A3 corrections (cost: reads as exclusive, misses the onset/persistence split); (b) rewrite as onset (rainfall-consistent) and persistence (two non-exclusive explanations), and use the Wilgeboomspruit both ways (cost: longer, more interpretation in the Discussion); (c) state only that the cause is unknown and cite no explanation (cost: loses the author's hypotheses).

**B3. The inflow is a back-calculated residual; the limit is not stated in 7.1.** Known problem (context §5). (SW 10, ED 35.) Details: in 1983–1995 the dam stood at 2–20% of capacity; 33 zero-inflow months; 69 of 156 evaporation entries and 67 inflow entries carry flag "E" (meaning not checked by the panel); the release gauge has "minimum value" and "above rating" months. SW's check: in 1987–1995 all non-storage terms together come to about 1.1 Mm³/a, so plausible errors in them cannot produce a fall from 4.67 to 1.23 Mm³/a; the yearly drop is robust, the monthly detail is not.
- Option 1: one sentence on the residual, no robustness argument. Cost: leaves a doubt unaddressed.
- Option 2: sentence plus the robustness argument. Cost: a number-based argument in the Discussion, and the author must accept SW's check.

**B4. Which inflow series to quote in 6.2: the reviewers differ.**
- ED: the patched flow gives 1.013 Mm³/a for 1985–1994 and cures the earlier mismatch with 0.84 (series 1).
- SW 12: the WR2012 patched flow is calculated from the same reservoir balance (WR2012 summary p. 30), so it is not independent. It holds April 1995 = 1.68 Mm³ while storage fell from 0.986 to 0.947 Mm³; the study rebuilt that month as 0.001. That one value is 65% of the 1994 total and lifts the 1985–1994 mean from 0.84 (series 1, the one the model uses) to 1.01.
- What would settle it: the origin of the April 1995 patched value. The author decides whether the narrative uses series 1 (0.84, consistent with the model and the tables) or the patched flow (1.01, with the April 1995 problem stated). Both reproduce.

**B5. "Restriction ... makes it larger overall" (7.1, first paragraph).** The 1.86 against 2.07 Mm³/a is a result. Reading it as "restriction makes the shortfall larger" treats a model difference as a management effect, and the unrestricted run is only a bound. (ED 22; SW 19 notes the "so" accounting also has other terms: rain +0.049, release +0.025, storage about +0.02 Mm³/a.) The v3 note lists this as new interpretation. Options: keep; or "In the model, restriction leaves less water for the canal because the dam holds more and loses more" and "partly because" for the accounting. The cost of the first is an interpretation without approval.

**B6. "The water balance removes this effect by asking for the registered volume in every year" (7.1, second paragraph).** The rule is fitted on delivered divided by asked-for volume, and the records cannot separate a restriction from irrigators asking for less. The lower bound therefore carries the effect forward. The sentence holds only for the unrestricted bound. (ED 27, SW 21.) "For the same reason" does not follow; two of the five high-storage years had a lowest storage of only 75.5%, with shortfalls of 3–23% of the registered volume. Options: limit to the unrestricted run, and add that the bound also depends on what irrigators asked for; or keep (cost: an overstatement an examiner can find).

**B7. Consequence of the 22% bias.** The balance delivers 22% more than the canal carried; half the excess falls in 1995–1996, when storage was 46–67%, the rule allowed full delivery and the canal carried 0.41 and 0.73 Mm³. Either operators kept restricting during recovery or irrigators asked for less. The block drew no consequence; the current article's reason ("the canal took up water more slowly") is also gone. (ED 21, SW 3.) Options: add one sentence that the simulated reliabilities are, if anything, optimistic in recovery years; or leave out (cost: the limit is unstated).

**B8. Wilgeboomspruit comparison and basis (6.2).** (GW H9, H10, H12, SW 11.)
- Zone rainfall over the valid months was 660 mm/a before 1984 and 496 mm/a after April 1988 (25% lower). With the study's elasticity of 2.0–2.5, rainfall alone predicts about 0.4–0.5 of the former flow. The runoff ratio fell from 8.2% to 3.6%. Dry-season-only ratio 0.055/0.122 = 45%. The pre-1984 mean contains 6 "minimum value" months (code 91) and 55 gap months, mostly 1975–1980.
- Three bases for one stream appear in the article (2.1 here; 1.27 Mm³/a for 1966–1990 and 53 mm/a for 1966–1980 elsewhere).
- GW H12 (beyond this block): the pre-1984 late-dry-season flow is about 25 mm/a over 39 km², close to the GRAII recharge (29 mm/a) and about three times the S-model drain outflow (0.33 Mm³/a); D gives 0.016. It could be a spring source, a catchment-area problem or a record problem, and it is the only flux observation in A31E that could constrain the recharge–conductivity non-uniqueness.
- The approved text said the gauge covers 39 km² and "does not stand for the reach as a whole"; v3 dropped this.
- Options: give rainfall for both windows or compare runoff ratios; or keep "a third" with the A6 labels (cost: reader infers an anomaly the rainfall partly explains).

**B9. Firm yield: depends on the series and has no assurance.** (SW 5, 6.) On sw1: no failure at 0.36, one at 0.38 (reproduced). On a recalculated copy of sw2 (adjusted series): none at 0.30, 1 at 0.32, 2 at 0.34 and 0.36, 3 at 0.38, so about 0.30. In both, the critical month is October 1992, at the lowest usable storage (0.166 Mm³). Article uses series 1, so 0.36 stands; the dependence is a limit. South African practice states a yield at an assurance from stochastic flows; the block does not say none was generated and that the DWAF figure may be such a yield. "Meaningful only together with the share of months or years" has no source. Options: state the range 0.30–0.36, name the critical month and add the stochastic sentence; or leave as is (cost: an examiner asks).

**B10. What the test shows (6.3, Table 7).** Series 1 is closed from the recorded storage, so storage NSE 0.86 tests the modelled outflows, not the inflow. Only the rule (fitted on 1966–1986) is tested out of sample; the rule is then refitted on both periods. Moriasi's criteria are set for monthly streamflow and are applied to storage and canal volume. The yearly canal volume passes narrowly (PBIAS −22.4% against ±25%). (SW 2, ED 38.) Options: add one sentence each on circularity and scope; or leave (cost: "meets all three criteria" is read as independent validation). The statement "the test supports counts of years and volumes more than event length" is not backed in 6.3; the record and model both give 17 shortfall years of 20 but 4 differ; the unrestricted longest event moves from 20 to 34 months with +10% evaporation (Sens row 48).

**B11. Low-demand "failure" under the rule (6.3).** "At a demand of 0.5 Mm³/a ... 0.82 and an event of 128 months": the rule cuts delivery by storage zone whatever the demand, so a failure here means the dam stood in a restricted zone, not that water was short. The longest event is 128 months at 0.5 and 148 at 3.0, which makes event length a property of the rule. FirmYield!H10 holds a conflicting value for the same label (0.913, 77 failure months; the rule is refitted there). (SW 4.) Options: say what failure means at low demand; correct the FirmYield columns (the author's file, not edited here).

**B12. Recurrence statement (7.1).** "Because the rainfall alone does not explain the low inflow after 1986, the recurrence of the drought cannot be estimated." SW 8: non sequitur; one such drought in 74 years is the reason, even if rainfall explained it. GW H6: the two causes have opposite consequences for the reliabilities (storage memory ties recurrence to multi-year dry runs; non-stationary upstream use means the pre-1983 record overstates today's inflow). ED 36: loose link to cause. Two positions: give the single-record reason (SW), or state what each explanation implies for reading the reliabilities (GW). They are compatible; the author chooses the emphasis.

**B13. "The water of A31E behaved differently" (6.2).** The A31E stream was dry in 42 of 50 months and the reach fell to two-thirds, against the upper inflow falling to 26%. A31E differed in degree and duration. GW H8, SW 15. Option: "fell less and recovered sooner" (interpretation) or a neutral statement of the two figures.

**B14. Table 6 column label and the capacity sentence.** Label "1987–1995 (drought)" or "(drought and recovery)" (A4). Capacity: "about 1.8 years" uses evaporation 1.23 Mm³/a at mean storage; the current article says 1.9 (ED: uses 1.07); near-full-supply evaporation of about 2.0 gives about 1.5 years (SW 18). Value 1.81 reproduces. The author approves the basis and adds "at the mean storage of the period" if kept.

**B15. Hashimoto trade-off and "storage limit" (7.1).** "Found the same trade-off" claims too much: a simulated reservoir with optimised hedging policies, vulnerability as the mean of the maximum deficit per event (LV C7, ED 23, SW 24). "Capacity too small to carry the scheme" gives no contrast; ED suggests 1.8 years against a drought of ten or more years. The quote and page are correct.

---

## C. Wording and repetition

Ranked by severity.

1. **Number density.** 6.2 paragraphs carry about 5, 6, 7, 10 and 7 non-year numbers; 6.3 second paragraph about 18; 7.1 last paragraph about 8. The Introduction keeps to about three per paragraph. The ranges "59% to 87%" and "45% to 77%" restate Table 8 and the Abstract. Move the reach figures to a small table (the approved v2 had Table 15); keep one contrast per paragraph. (ED 5, 14, 37.) 0.30 and "almost nothing" restate Table 6.
2. **Results–Discussion boundary.** "Because the inflow of each rainy season is passed to the canal at once" and "the rule also costs volume" are mechanism and evaluation in Results (ED 15). "The answer depends more on the restriction rule than on the demand" is interpretation, has no antecedent, and the figures say "about as large" (0.28 against 0.29; SW 20: "as much as") (ED 17). "Firm yield cannot be defined, because..." is an explanation (ED 18). "Modelled naturalised runoff... about twice the net contribution" compares a model output (excluding abstraction and return flow) with a derived net quantity, higher in the drought (7.42) than after (6.51), and is not taken up in 7.1 (ED 7, SW 14).
3. **Repetition.** "One drought dominates" appears three times (6.3; two places in 7.1). Say it once, in 7.1. The 146 months appear in 6.3 and 7.1. The register-records-entitlements sentence repeats 2.6 and 6.1; keep one clause.
4. **AI-sounding closers and symmetrical phrases.** "The result is therefore a range and not a single reliability"; "show X but not Y"; "A yield... is meaningful only together with..."; "The low inflow is accepted as part of the recorded sequence". Three of the four 7.1 paragraphs end on a summarising sentence. The Introduction does not. Stacked hedges ("possible", "cannot be assumed", "common where"). (ED 24, 25, 30, 39.)
5. **Terms.** One name for each inflow series and for the net contribution; "reach" (panel report M13 flags it; the supervisor's text was not in the files, so the author must confirm); "historic firm yield" is used in 7.1 without a definition in 6.3 and "yield" alone is used for the Department's figure; "long-term mean" for rainfall against "median" for inflow, and two medians in one sentence.
6. **Draft marks.** "Table 7 (new)" and "Table 8 (was Table 7) ... Values unchanged from the current Table 7" must go before insertion. Figure 9 is no longer cited; 6.2 jumps from Figure 8 to Figure 10.
7. **Smaller points.** The ten-year run of shortfall years ends only because 1994 (11 valid months) is left out; 1995 and 1996 are also shortfall years (SW 16). "Stayed nearly full" for the five years: use "above three-quarters of capacity". Peterson: add that it is context and that "by 2017" fits p. 745 (unverified). The 7.1 Hashimoto sentence could say "in a reservoir example". The Table 6 caption mixes the dam-record canal term (1.20) with gauge A3H031 (1.23) — correct and clear.

---

## D. Checked and sound

Recomputed from sw1 (SW, GW, ED agree unless stated):
- **6.2 inflow and storage:** patched-flow medians 3.945 (prints as 3.94; rounding to 3.95 also possible) and 3.23 without 1975–1980; below both medians 1982–1994; 1985–1994 patched mean 1.013 (43% of 2.34); rainfall 1987–1990 above the mean (693, 660, 631, 682 mm against 599); storage 99.3% in December 1982 and 21.9% in March 1984 (start of month).
- **Table 6:** all cells close: inflow 3.3247 / 1.2340 / 4.6688; rain 0.417 / 0.239 / 0.532; evaporation 1.230 / 0.738 / 1.546; canal 1.197 / 0.295 / 1.777; spill 0.869 / 0 / 1.427; release 0.326 / 0.070 / 0.490; losses 0.009 / 0.014 / 0.006; change in storage +0.111 / +0.355 / −0.045. Series 1 mean 3.393 and A3H031 1.229 match the caption. Evaporation share 32.9% and 50.3%. Capacity 3.02 years and 1.81 years.
- **Canal record:** 38 years, 24 shortfall years (63%), mean shortfall 57.5%, run 1984–1993, five years at or above 75% storage (SW; LV against context).
- **Kromellenboog:** 6.209, 5.014 (80.7%), 98%, 3.80 against 5.80, no negative year in 21, rank correlation 0.762, naturalised runoff 7.42/3.80 = 1.95, rainfall 598 against 608 mm (GW, SW; LV did not rebuild these).
- **Wilgeboomspruit:** flow in all 67 valid May–September months before February 1984; dry in 42 of 50; four months above 100 mm, largest 211.3 mm (February 1988); flow from April 1988; zero from March 1992; means 2.10 and 0.69.
- **Table 7 and the test:** 0.864 / 0.369 / +7.42; 0.378 / 0.789 / −17.2; 0.595 / 0.636 / −22.36; n = 276, 265, 20; 192 against 216 of 265; the balance gives 1.224 times the canal volume.
- **Reliability:** 364 / 118 failure months, 0.590 / 0.867, 0.446 / 0.770, vulnerability 0.496 / 0.879 ("half", "an eighth"), event December 1983 to January 1996 of 146 months, shortfall 21.86 Mm³ (9.3 times 2.34), 40.1% of failure months, three times as many failure months (3.08), unrestricted events within the drought up to 20 months, canal 1.861 against 2.067, extra evaporation 0.146 and spill 0.062, adjusted series 0.588 / 0.865.
- **Sens and yield:** 0.821 and 128 months at 0.5 Mm³/a; 7.9% at 1.5 Mm³/a; 0.28 against 0.29; no failure at 0.36 and one at 0.38 on sw1; 0.36/1.4 = 0.26 ("about a quarter").
- **Citations:** Hashimoto et al. (1982:19), "high system reliability was accompanied by high system vulnerability", verbatim (LV, SW).
- **Logic:** "outside A31E" is correct for the dam's inflow explanations, because the dam stands on the upstream boundary. A31E has no dolomite (Pretoria Group, 99.6% by §2.4).
- The v3 note's claim that the pointers back to other sections are gone holds for the block text.

---

## E. Could not check

- **Sources not opened** (network allow-list; status rests on the verification report): DWAF (2004) pp. 50 and 83 (www.dws.gov.za); Pyburn (2015) pp. 5, 45, 113 (repository.nwu.ac.za, hdl.handle.net); Peterson et al. (2021:745), "by 2017" and "161"; Fowler et al. (2022); Kapangaziwiri et al. (2011:128) for "common where gauged flows are affected by poorly defined developments upstream" (the earlier support is for a different statement); Moriasi et al. (2007:891) (a search snippet shows the thresholds in the abstract, p. 885; page 891 unconfirmed; the approved text cites 887–888 for definitions); Theis (1940) and Cuthbert et al. (2019) as used by GW. Allowing the hosts above would let A1–A3 and the E list be settled.
- **Not rebuilt from raw gauge series:** the Kromellenboog figures were recomputed from sheet Q2 by SW and GW but not from the raw gauge data; LV did not rebuild them.
- **Not shown or not checked:** Table 8 (not in the draft, "values unchanged"); Figures 6, 7, 8, 10 and 11 as images; reservoir-record flags "E" and "&" (meaning unknown); quality code 91 ("minimum value") effect on the Wilgeboomspruit means; the supervisor's text on "reach". The recalculations used LibreOffice, not Excel; the baseline copy reproduced 364 / 118 and 366 / 120.
- **Dataset citations** (DWA 2012, DWS s.a.b, s.a.f): dataset, no page; the register-records-entitlements statement cannot be shown by the dataset itself (LV C6).

### Notes on project files (not on the block; for the author)

- `49e_geology_dolomite_table.xlsx`: column P3 totals 162.6 km², which is the Doringrivier catchment (F3), not A31E; `number_check.md` GE-2 presumes P3 is A31E. The geology shares in §2.4 support "no dolomite in A31E" independently.
- `WHICH_FILE_IS_LATEST.txt` already carries a known error (sw2). FirmYield!H10 conflicts with Sens for the same label (B11).
- Unchanged-claim note in v3: the 6.3 paragraph on rule sensitivity and the explanation of the 22% excess were removed, though the note says "unchanged apart from two references" (B1, B7).
