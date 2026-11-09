# Panel review of the whole draft set, 9 November 2026

Block: `drafts/Whole_draft_set_manifest.md` (Abstract v2, Introduction 1.2 v1, Study Area v2, Methods fixes v2, Results 6.2–6.8 v6, Discussion v8, Recommendations and Conclusions v3, numbering and reference file). Six reviewers worked independently: surface water, groundwater, flood, water quality, literature (citations) and academic editor. Nothing in the project was edited. Every number below was recomputed by at least one reviewer, from the workbooks, the result files, the shapefiles or the SANRAL text, unless it is in group E.

Reading guide. **A** holds what is wrong and can be corrected without your judgement. **B** holds what you decide; each has the options and what each costs. **C** holds wording and repetition. **D** lists what was checked and holds. **E** lists what nobody could check. Reviewer codes in brackets: W surface water, G groundwater, F flood, WQ water quality, CIT citations, ED editor.

Your rule for this article is that a finding changes the text only if something already written is wrong, and that limits stay out of the text. Several findings in B conflict with that rule (a limit was cut and a sentence now rests on it). Those are marked **rests on a cut limit**, and for each the cheapest option is to soften the sentence and not to restore the limit.

---

## A. Clear errors (24)

Ranked by severity.

| # | Where | What is wrong | Fix |
|---|---|---|---|
| A1 | Methods 5.4.4: "the 19% found for 1987–2009 (5.01 of the 6.21 Mm³/a, Section 6.2)" | 5.01/6.21 is 81%, the share that did not come from the upper dam. The 19% is 1.19/6.21 (ED 4, WQ-01, W4) | "(1.19 of the 6.21 Mm³/a, Section 6.2)" |
| A2 | Results 6.4: "14.5 Mm³/a … unaccounted for, which is five to nine times the estimates of baseflow" | 14.5 ÷ (3.43, 2.53, 2.00) = 4.2, 5.7, 7.3. "Five to nine" is recharge ÷ baseflow (G7, ED 3) | "four to seven times", or compare the recharge and say so |
| A3 | Abstract, Results 6.2: "thirteen successive years from 1984" | The workbook (Q1) counts a run of ten shortfall years, 1984–1993. 1994 has only 11 canal months without a gap code and is left out, and the sentence that argued 1994 was short was cut. The sentence before it ("38 have a complete record … 24") leaves 1994 out too, so two adjacent sentences count years two ways (W1, ED 1, CIT A5) | Decision B1 |
| A4 | Study Area 2.6: return flows "from Zeerust and from irrigation … their nutrient and salt content limits their re-use (DWAF, 2004:57)" | p. 57 is about return flow from irrigation in A31D and mines around Zeerust, and says the content "has limited its re-use for domestic supplies". The p. 86 quote is about urban and irrigation return flow, a different flow. The draft joins them with "their" and drops "for domestic supplies" (CIT S9, S10, WQ-16) | "…limits its re-use for domestic supplies (DWAF, 2004:57)", with the two flows kept apart |
| A5 | Cross-references that now break | (a) Methods v2 5.1.2 still says "GRAII (DWS, s.a.a; Section 2.4)" while Study Area v2 moves the values out of 2.4. (b) Results 6.1 "(Section 2.4)" for the GRAII. (c) Article 4.4 "inferred to enter the river upstream of it (Section 2.6)" points to a sentence that Study Area v2 removed. (d) The number file covers tables only: Map 8 now comes before Map 7, Figure 8 is orphaned (B23), and some line numbers in it are wrong ("Table 10" at Results line 90 is missing, "line 193" is a note line) (ED 29–31, CIT C4, WQ-17) | Use the Study Area v2 wording as the 5.1.2 text; point 6.1 to Section 5.1.2; label 4.4 as an inference without the pointer; add a map and figure map to the numbering file |
| A6 | Results 6.7 v6, Discussion ¶5, Rec 6 | The dolomite sentence (46.4%, all above the dam) is in no Results file. The Discussion sentence "the dolomite above the dam may make the SDF too high" has no basis until it is put back (F16, ED 9). It holds only for the 32.5 km² of A31E inside the F2 catchment, which the workbook covers; the rest of "A31E contains none" rests on the hydrogeological map | Insert the original sentence into Results 6.7 at assembly |
| A7 | Results 6.4: baseflow "2.00 to 3.43 Mm³/a (DWS, 2021; Bailey & Pitman, 2016)" | The WR2012 summary has no A31E baseflow. `wr2012_A31E_row.csv` records 3.43 as "NOT IN THIS FILE, still unsourced". The value stays by your decision, but the citation does not hold (CIT A2) | Name the real source of 2.53 and 3.43, or cite DWS (2021) for 2.00 only |
| A8 | Methods 5.2.3 and flood table step 10: "with the mean annual precipitation (MAP) of 597 mm (SANRAL, 2013:3-61, 3-62)" | SANRAL defines P as the mean annual rainfall over the catchment. 597 mm is the WR2012 MAP of A31E alone, and F2 (1 357 km²) is mostly upstream. As worded, the text implies it is the catchment MAP and that SANRAL gives it (F2, CIT M12). Keeping 597 mm is your decision; the text must say what it is | "with the MAP of A31E, 597 mm" and move the SANRAL citation after "formula" |
| A9 | Results 6.8: "Sulphate follows the same order" | The sulphate medians are in no Results sentence or table after the cut, only in Figure 15. Within path 1 the highest sulphate (188257) has the lowest EC, so "the same order" holds only broadly (WQ-11) | One clause with the medians, or "sulphate is also higher on path 1" |
| A10 | Results 6.8: the three sites between the dams, "76 to 83 mS/m" | No station is named, the qualifier "one to three samples each from a different period" was cut, and the total is 7 samples (188257: 3, 188038: 3, 188030: 1). Other shares and medians have no n (A3H030 56, A3H016 54, Kromellenboog 87) (WQ-03, WQ-09) | Name the stations and give n; Table 12 shows counts (14/74), not only percentages |
| A11 | Results 6.8: "boundary of a trophic class"; "No sample at any site exceeds the guidelines for chloride, sodium or SAR" | 0.025 mg/L is the mesotrophic–eutrophic boundary. The chloride (100 mg/L) and sodium (70 mg/L) values are TWQRs for wetted foliage; for water applied to the soil chloride is below 140 mg/L. "No sample" cannot be confirmed from the rounded percentages in the CSV (WQ-05, WQ-12) | "the boundary between the mesotrophic and eutrophic classes"; "for sprinkler irrigation (wetted foliage)"; confirm zero counts from the raw records |
| A12 | Results 6.2 / Table 6 caption: "only about 1.8 years" | With net evaporation 7.07 / (2.34 + 1.23 − 0.42 + 0.33) = 2.0 years. 1.8 comes only with gross evaporation or the 1996–2009 column (W2) | State the period and gross or net, and give the matching number |
| A13 | Methods 5.2.1: remainder of the recorded balance "(A3R003, A3H033)" | The Kromellenboog remainder uses the irrigation column of the reservoir record, not gauge A3H033 (W18) | Cite the reservoir record (DWA, 2012) and A3R003 |
| A14 | Table 8, reverse test: PBIAS +18.9 and +19.4 | The reviewer's rerun of the workbook formulas (rule 2, pattern 2, series 1) gives monthly NSE 0.564, RSR 0.66, PBIAS +19.3 and yearly 0.489, 0.715, +19.6, with the same 178 months and 14 years. NSE and RSR match; PBIAS differs by 0.2–0.4. No sheet stores the reverse test. `project_context.md` section 7 holds a different run (154 months, 12 years, 0.53, 0.34) (W7, ED 5) | Decision B17 |
| A15 | Abstract, Discussion ¶2, Conclusions: the water "that the dam releases" is above the salinity target | The samples are of the river below the wall (A3H030, A3H042Q01). The canal (A3H031) is not sampled, and "release" is the Table 7 term for the release to the river (WQ-18, ED 11) | "the river below the dam" |
| A16 | Discussion ¶4, Conclusions ¶4: the groundwater weakens "in structure D" | Under case D, structure S loses 1.04 Mm³/a of river and stream discharge (9.87 → 8.83) against 0.09 in D, and S's mean lowering (1.00 m) is larger than D's (0.38 m). D is larger only under the pumped cells (3.78 against 0.23 m) (G9, W15, ED 13) | Say what is measured, or "in both structures" |
| A17 | Discussion ¶1, Conclusions ¶2: "although the rainfall recovered" | Rainfall was above the mean only in 1987–1990. 1991 had 314 mm, the lowest of 1967–2008, and 1992 had 486 mm. Section 1.1 says 1986–1995 averaged 99% of the mean (ED 15, W11) | Use the Section 1.1 wording |
| A18 | Results 6.6: "the mean shortfall and the longest event grow" in each step | Without restriction the longest event is 35 months in both M and D (W20) | "grow from the Reference run to case M" |
| A19 | Results 6.5: "87% to 89% of the pumped water comes from less discharge to the rivers and streams" | 87–89% is the river-drain share. Rivers and streams together are 87.6–89.2%, which is what Table 11 prints (G17) | "88% to 89%" |
| A20 | Methods flood: "Section 5.4.3" in Results 6.7, "Design peak" column for the Midgley and Pitman row | The methods are described in 5.2.3. "Design peak" for a check method goes against your decision that the SDF is the design flood (F11) | Point to 5.2.3; call the column "Peak at F2" |
| A21 | Article 3.4 (stays): runoff coefficients "calibrated on 29 catchments (… SANRAL, 2013:3-43)" | SANRAL p. 3-43 has 29 drainage basins, and p. 3-44 has 152 flow-gauging stations (F15) | "calibrated for 29 drainage basins from the records of 152 gauging stations (SANRAL, 2013:3-43, 3-44)" |
| A22 | Article 6.1 (stays): "the weathered zone holds about 91% of the stored groundwater" | 91% is storativity × thickness (0.00998 × 25.36 against 0.00014 × 182.14). That is the water released per metre of head decline, not the volume stored (G12) | "about 91% of the water released per metre of decline", or drop |
| A23 | Article 3.3 (stays): the "later start of the summer rains" | You decided on 9 November to remove this entirely. It is still in Section 3.3 (ED 47) | Remove at assembly |
| A24 | Methods 5.2.3 replacement range "lines 979–987" described as "second and third paragraphs" | Lines 979–987 are the second paragraph only. Lines 989–991 (SRTM reason, Manning's n, USACE HEC) must stay (F13) | Correct the heading of the replacement |

---

## B. Interpretations the author must decide (29)

Order: the ones that touch several sections come first.

**B1. How long was the run of shortfall years?** (W1, ED 1, CIT A5; A3)
- (a) "Ten successive years from 1984" (1984–1993, the workbook's rule). Cost: the run is shorter than the 1984–1996 span used elsewhere, and Introduction 1.1 (twelve, October 1983 to September 1995) needs a sentence that these are different measures.
- (b) Keep thirteen, state that 1994 is incomplete but short (0.279 Mm³ in 11 months against 2.34), and count it the same way in the next sentence. Cost: one more sentence in 6.2, and years are counted by judgement.
- Either way, the Abstract, 6.2 and 1.1 must give the same period, and "the drought" has at least four spans (Section 1.1 October 1983–September 1995, canal years 1984–1996, simulated event December 1983–January 1996, table column 1987–1995) (W23, ED 39). Name each span by what it is.

**B2. "The restriction rule matters more than the demand"** (Discussion ¶1, Recommendation 3, Conclusions ¶2) (W9, CIT D1, ED 7; also W8). **Rests on a Result that was cut.** Three reviewers agree on the facts.
- The claim holds for the reliability by time (0.590 with the rule against 0.867 without). By volume it reverses: the rule changes it by 0.09 (0.795 against 0.883) while raising the demand from 0.5 to 3.0 changes it by 0.17. Restricted months count as failures at any demand.
- Hashimoto (1982:19) shows that policies change reliability at one fixed target and that there is a trade-off with vulnerability; it never varies the demand, so it cannot carry the comparison.
- The records cannot separate restriction from a lower request, and the delivered share by storage zone fell after 1987 (zone 3: 0.52 to 0.20; zone 4: 0.81 to 0.53) (W8).
- Options: (a) drop the claim in all three places, and let Recommendation 3 ask only for the rule to be stated (cost: the main managerial point goes); (b) restore one Result sentence limited to reliability by time and cite Hashimoto only for the trade-off (cost: a number returns to Results 6.3 and the claim must say "by time"); (c) say "the rule and the demand both matter, and the records cannot separate restriction from lower demand" (cost: weaker, but true).

**B3. The Conclusions repeat the Discussion sentence by sentence and do not answer the two research questions** (ED 21–23, F17, WQ-20).
- Question 1 asks how reliable; the Conclusions say only that the volume "cannot be assured" and use "most of the years that could be counted", which is the record (63%) and not the simulated 45–77%.
- Question 2 asks how large the floods are and along which paths; the Conclusions give "depends on the method" and the particle result, and name no receptor. The salinity sentence concerns upstream water, not contaminants from the land.
- The first paragraph repeats the aim of Section 1.2 almost word for word.
- Options: (a) rewrite the Conclusions as two answers and a link to the Recommendations, with no figure (cost: question 1 is answered in direction only, and the Abstract carries the range); (b) allow one range in the answer to question 1 (cost: breaks "no numbers"); (c) narrow question 2 to match the Conclusions (cost: the screening objective loses its answer).

**B4. The headline sentence on structure D credits it with a result that comes from its conductivities** (Abstract, Discussion ¶3, Conclusions ¶3) (G1, G2).
- "In the other the pumped cells cannot deliver the larger rates" comes from the lower-limit conductivities that the four levels do not fix. With S's conductivities structure D gives 2.22 m at 0.5 Mm³/a and no cell below 47.5 m. The structure decides where the water comes from; the conductivity decides how far heads fall.
- D's own source result (about 99% from the ground drain, under 2% from rivers) is in Results 6.5 but not in the three texts. The two structures are described by different kinds of result.
- Recharge and conductivity are not separable on four levels (scaled pair: 0.96–7.43 m at 0.5 Mm³/a in S, a factor of about 8), so "the water table against the river bed" is one cause of the range, not the only one.
- Options: (a) state the source for both structures and say that deliverability in D follows from conductivities the levels do not fix (cost: two more clauses); (b) drop the deliverability clause from Abstract, Discussion and Conclusions (cost: a result of 6.5 is not carried forward).

**B5. Limits that were cut and that an existing sentence now rests on.** Your rule is that limits stay out of the text. For each item the choice is the same: (i) soften the sentence that rests on it, (ii) restore one clause, or (iii) leave as is. I recommend (i) unless noted.
- Flood: "the flooded extent is a screening and not a flood line" (Discussion, Conclusions) and "the flood lines need a finer terrain model" (Rec 6) have no stated reason after the cuts (F1). The reviewer suggests the sentence "…not calibrated". You declined that sentence, so (i): say "indicative extent" without the reason, or drop "finer terrain" from Rec 6.
- A MODFLOW drain only removes water, so D's river share is a minimum and induced river leakage is not represented (G3); the ground-drain share lumps seepage, springs and evapotranspiration, so part of it may be lost streamflow (G4).
- The drawdown is a mean of 200 m cells, so levels in a pumped borehole fall further; at 0.5 Mm³/a each cell carries 0.35 L/s against mapped yields of 0.1–0.5 L/s (G5).
- Part of the 262 archive levels may be pumping levels, which would favour D (G6); three of the four calibration levels date from the drought (G16); the rate for the longest shortfall event is compared with a steady state at mean recharge (G13).
- The climate scaling ignores the effect of warming on runoff and acts mainly on wet months, so it understates the loss; this sentence was removed from the Conclusions (W14).
- Detection limits, the inorganic N definition and phosphate-P as the measure of inorganic P are not stated in Methods 5.4.4 (WQ-06); the water-quality sites span different periods and are not flow-weighted (WQ-07).
- Five of the 24 shortfall years (1974, 1977, 1979, 2000, 2001) had the dam at 75% or more, so a shortfall is measured against an entitlement that was not always asked for (W19). One clause restores this: "against the registered volume, which was not always asked for".
- The inflow is a back-calculated remainder, least certain when the dam is low (zero-inflow months are 14% of months below 10% storage against 4% above 60%) (W11, ED 17). Discussion and Conclusions state the low inflow as fact. Option (ii) here is cheap: one clause.

**B6. "Part of the irrigated land lies on the floodplain"** (Discussion ¶5, Conclusions ¶5, Rec 6) (F4, ED 8). Results 6.7 reports cultivated land flooded (3.1–3.3 km²), not irrigated land. The irrigated-land result (about 44 ha) was cut.
- (a) Write "cultivated land" in all three places (cost: weaker link to the scheme, and the 8.04 km² and 3.1–3.3 km² are unverified, see E).
- (b) Restore one Results clause on irrigated land flooded, recomputed from the irrigated-land layer (cost: a number returns to Results).

**B7. "The size of the design flood depends on the method"** (Results 6.7, Discussion, Conclusions, Abstract) (F3). The SDF is the design flood; Midgley and Pitman is a check and the RMF is an envelope without a return period. The finding that matters to the floodplain users, that the flooded area changes little (7.60–7.97 km²) while the peak changes by up to 41%, is only in Results.
- Option: "The SDF peak was compared with the Midgley and Pitman formula and the RMF" in Results; "the peak differs widely between methods, but the flooded area differs little" in the Discussion, Conclusions and Abstract (cost: a result sentence moves forward; you decide that reading).

**B8. Spillways and flood lines (Rec 6, Discussion ¶5)** (F5, F19). The reason for the spillway and for a 1:50 line was cut with News24 and the 1:50 reason. Options: (a) one clause that gives the reason (spill capacity decides whether Klein Maricopoort attenuates and the safety of Kromellenboog), with DWAF (2004:170–171), whose pages nobody could open; (b) ask only for the 1:100 line and drop the spillway part (cost: loses the dam-safety point).

**B9. The mixing check, "about 11 mS/m for the water from the catchment"** (Results 6.8, Methods 5.4.4) (WQ-02, W4).
- The data contradict it: the three sites between the dams (76.3, 77.7, 82.6 mS/m) are saltier than both end members (62.3 and about 11), so salt is gained along the river or the periods differ.
- It is very sensitive to the share: 1.8% gives 19.9 mS/m, 19% gives 10.9, 24.9% gives 6.9, and 33% or more gives a negative value. The 19% is a 1987–2009 volume average, mostly spill, applied to 2012–2023 samples that are mostly low flow.
- The 81% that did not come from the upper dam includes canal return flow, so it is an upper limit; the workbook's lower bound is 3.79 Mm³/a (about 61% of 6.21) (W4).
- Options: (a) give a range (about 7 to 20 mS/m) and name the salt gain as the reason; (b) drop the number and keep the order (path 1, then Kromellenboog, then A3H016); (c) keep as is and say "up to 81%" in 6.2. Cost: (a) adds a sentence; (b) removes the "much fresher" evidence (still in the three sites and A3H016); (c) leaves a number a reader can contradict from Table 12.

**B10. The "two waters" wording** (Discussion ¶2, Conclusions ¶2, ¶5) (ED 10, WQ-08, WQ-19). "Could not replace the supply" is an inference (22% of registered use is river abstraction below the wall). "The runoff of A31E is fresher" rests on the Wilgeboomspruit (A3H016, 39 km², a quartzite headwater, record ending 1991) and on seven groundwater samples. "Generated between the dams" is an inference (the net contribution includes canal return flow). Options: keep "does not reach the canal" and drop "could not replace"; name the sites ("the Wilgeboomspruit and the seven groundwater samples"); "came from the river between the dams".

**B11. The net contribution compared with 1996–2009 "under almost the same rainfall"** (Results 6.2) (W3). Three record effects could produce the difference without any response of the catchment: canal return flow (0.30 Mm³/a in 1987–95 against 1.78 after), sixteen months of flagged Kromellenboog outflow stored as zero, and three flood years (16.9, 19.0, 8.6 Mm³) in the 1996–2009 mean. Options: name them in the caption, or drop the rainfall comparison.

**B12. Climate wording** (Abstract, Discussion ¶4, Conclusions ¶4, Results 6.6) (W12, W13).
- "Probably somewhat drier" and "falls further by about 2050" read as projections; the Methods say these are sensitivity steps and the rainfall change is uncertain even in sign. Option: "in the two sensitivity cases for about 2050".
- "In case M … its lower reliability is against a larger demand": measured against the unchanged 2.34 Mm³/a, case M still gives 0.555 with the rule and 0.843 without, so about 70% of the fall remains. Option: remove the "so …" clause.

**B13. Words for the pathway result** (Discussion ¶3, Conclusions ¶5, Map 10 caption, Abstract) (G10, WQ-13). In S every cell also has the ground drain, and in D 288 of 405 particles never leave their start cell, so the result follows from the drain construction. "End in a cell where a river drain discharges" (the Results wording) is not "reach a river", and nothing follows about contaminant arrival. Option: use the Results wording; "after decades to centuries" (median 143 years at 0.10; 14 at 0.01); "groundwater flow paths from the irrigated land" and not "contaminant paths".

**B14. "The records cannot show which structure is closer"** (Discussion ¶3, Conclusions ¶3) (ED 12, G6). The 262 levels favour D (62% against 31% within 10 m) but D is slightly worse than the benchmark, and some levels may be pumping levels. Options: keep the neutral wording and restore the pumping-level reason in 6.4; or say what the levels favour and what they do not.

**B15. Firm yield** (Discussion ¶1, Rec 2, Results 6.3) (W10, W22, CIT D2). "A quarter of 1.4" is more precise than the sensitivity allows (a sixth to a third: lowest usable storage 0 or 0.5 Mm³ gives 0.44 or 0.24; evaporation ±10% gives 0.46 or 0.28; series 2 gives 0.32). The 0.36 is net of the river release and set by one month (October 1992, 0.21 Mm³ storage), and the Department gives no method. The Department's 1.4 "rests on hydrology not updated since 1988" is an inference; DWAF (2004:83) says the Marico hydrology has not been updated. Options: "well below", or the range; "historic firm yield"; restore the one-month sentence; cite p. 83 in Rec 2.

**B16. Reverse test, which run is final** (W5–W7, ED 5; A14). Table 8 (178 months, 0.56/0.49), the rerun (same, PBIAS differs) and `project_context.md` section 7 (154 months, 0.53/0.34) disagree, and no sheet stores it. Methods 5.4.1 describes only the forward test, yet Results 6.3 leads with the reverse pass. Option: confirm one run, store it, and add two sentences to 5.4.1 (the rule, the start storage, the years). Also decide W6: the reverse monthly pass uses the test years' own seasonal pattern; with the Figure 3 pattern the reverse monthly NSE is 0.14. Methods v2 already says "independent only for the rule". Options: leave that, or also report the Figure 3 result.

**B17. Table 5 base years** (W16). You decided "1936–2009". The result file says the factors were computed against 1937–2009 (`49_Block3_results.txt` line 30). Options: keep 1937–2009 in the caption; or recompute against 1936–2009 (the factors may change in the third digit).

**B18. GRAII depth** (G11, CIT C4). Methods 5.4.2 gives 47.5 m as the base of the weathered zone; the moved GRAII text gives 25.36 m thick and 207.5 m in total. Possible reconciliation (unverified): 47.5 = 22.14 depth to water + 25.36. Needs the GRAII file. Options: state the reconciliation once; or drop 47.5 m and use a defined depth.

**B19. Registered borehole use and the 0.81** (G22). 49b gives 28 records inside A31E = 0.265 Mm³/a; the article uses 0.285 (8.4% of 3.38). The 0.81 Mm³/a groundwater use of the Reserve is not in the package. Needs DWS (2021:156). Which figure is final?

**B20. Guideline for SAR** (WQ-04). The 2.0 is the crop-yield (toxicity) TWQR (DWAF 1996a:134). p. 133 and Table 2 (p. 135) give 1.5 for soils prone to surface sealing. Options: recount against 1.5 from the raw records; or state why 2.0 applies.

**B21. DRASTIC** (WQ-15). A "low" class over 96.7% sits beside a water table within 5 m at 114 boreholes in S. It is not used in the Discussion, Conclusions or Recommendations, the layer is not in the package, and the source is secondary (DWAF 2005, via Esterhuyse 2017). Options: keep it with "relative intrinsic vulnerability on a national grid, not validated here"; or cut it from 6.8 and Methods 5.1.2.

**B22. Figure 8 and Section 1.1** (ED 28). The Wilgeboomspruit paragraph and its Figure 8 reference were cut from Results 6.2, yet Section 1.1 still states "dry in 42 of the 50 months … suggests that groundwater storage declined". Options: restore one Results sentence citing Figure 8; or remove Figure 8, renumber, and amend 1.1.

**B23. Whether the Discussion needs more literature** (ED 17). It now cites four sources, two used weakly. You asked for a short Discussion; the supervisor asked for a literature-supported one. Options: leave as is; or one comparison per paragraph from sources already read (each needs a verified page).

**B24. Number density in Results** (ED 43). Paragraphs 6.2 ¶1, 6.5, 6.6 ¶4 (twelve numbers), 6.7 ¶3 and the EC paragraph in 6.8 carry more than four numbers not already in a table. Option: remove every number a table carries (0.59/0.54/0.48, 1 252/889/71%/41%, 1–3%, 3.1–3.3 km²). Cost: a second editing pass on Results.

**B25. Names** (ED 40, 42). D means structure D, case D and the row of Table 13. M can read as Midgley and Pitman. Options: "median case" and "dry case" in tables and text; or write "structure" and "case" in full everywhere. "Reach" means the 15.7 km flood reach in Methods v2 but the river between the dams in 4.3.

**B26. Study Area map positions** (ED 34). The positions in 2.3–2.5 are my reading of the maps. Confirm them on your GIS before use. 2.3 says "to the dam"; it should name Kromellenboog Dam.

**B27. Discussion sentence on 1:50 and 1:100 outlines** (previous open item) is not added; no reviewer asked for it.

**B28. The one place two reviewers disagree with your rule.** ED 17 and W11 want the inflow-residual limit stated; F1 wants "not calibrated" back. Both go against decisions you made. They are in B5 as options, not as errors.

**B29. Questions from the reviewers that only you can answer**
1. GRAII depth to water of about 22 m? (G11)
2. Is the 0.285 or the 0.265 Mm³/a right, and which page gives 0.81? (G22)
3. Present D's conductivities as "at most" values, so that its drawdowns are minima? (G)
4. Is 188257 "Kalkdam at Enzelsberg road" on the main stem, and above or below the Doringrivier junction? (WQ)
5. Why did the A3H042Q01 PO4-P median fall from 0.044 to 0.010 mg/L between the first look and the corrected CSV: detection limit, site-code filter or the N definition? (WQ)
6. Does the MODPATH recharge include return flow of canal water on the irrigated cells? (WQ)
7. Does the 17.7 mS/m groundwater EC equal the A3R003Q01 sulphate median (17.7 mg/L) by coincidence? (WQ)
8. Is Map 9 drawn from the RAS Mapper sub-grid raster or from `cells_Q100_SDF`? The two readmes disagree. (F)
9. How was the K3/K4 boundary placed, and was the two-region rule of SANRAL p. 3-66 considered? (F)
10. Which SANLC classes gave 3.13–3.33 km² flooded, and were they the 8.04 km² classes? (F)
11. Is the 1.4 Mm³/a the total draft (canal plus river) and for which capacity? (W)

---

## C. Wording and repetition

**Repetition map** (ED). Each fact should stand where it is first needed.

| Fact | Where it now stands | Keep |
| --- | --- | --- |
| Water in the upper dam comes from outside A31E | 1.1, 2.1 (twice), 4.1, Discussion ¶2, Conclusions ¶2 | 2.1 once; a clause in 1.1; not in Discussion or Conclusions |
| 3.38 Mm³/a registered, 69% scheme | 1.1, 2.6 | 1.1; 2.6 keeps the split not given there |
| Seven quality sites, 1966–2023 | 2.6, 5.1.4 | 5.1.4 |
| Return flows limit re-use | 2.6, 4.4 | 2.6 |
| NGA holds the records | 2.4, 5.1.2 | 5.1.2, with the definition of NGA |
| Reliability 59/87% and 45/77% | Results 6.3, Abstract, Table 10 | Results; Abstract keeps the yearly range |
| Cause of the low inflow not settled | 1.1, Discussion ¶1, Rec 7(b), Conclusions ¶2 | Discussion once |
| Groundwater cannot yet be a backup | Abstract, Discussion ¶3 and ¶6, Rec 4, Conclusions ¶3 | Discussion ¶6 once; Conclusions as the answer to question 1 |
| Salinity above the target | Results 6.8, Abstract, Discussion ¶2, Rec 5, Conclusions ¶5 | Results; Discussion once |
| Dry end, not the median | Discussion ¶4, Rec 1, Conclusions ¶4, Abstract | Discussion once; Rec 1 as the action |
| The aim | 1.2, Conclusions ¶1 | 1.2 |
| Independence of the test | 5.4.1 (twice), Table 8 caption | 5.4.1 once |
| Guideline screening | 5.1.4, 5.4.4 | 5.4.4 |

**Wording**
- "The drought also shows that A31E carries two waters" overstates: the two waters are the premise of 4.1 and the data are consistent with it (ED 18).
- "For the catchment, this means that …" and "…and the recommendations follow from that" are stock closings; the last Discussion paragraph and Conclusions ¶6 repeat each other (ED 19).
- "Each range has a known cause" (Discussion ¶6, Conclusions ¶6): "range" is first used here and is not defined (ED 16).
- The introduction to the Recommendations ("Each recommendation follows from the Discussion (Section 7)") is filler and a pointer back; Rec 5 gives reasons that are not in the Discussion, Rec 7(e) names the western arm, which the Discussion does not (ED 46).
- Abstract: "Irrigation … depends on a canal" lost the hedge of Section 1.1 ("appears to"); "falls further" does not say further than what; "only 1% to 3%" is evaluative; no pathway result is given (ED 24–26).
- Abbreviations are defined late or not at all: MAP, RMF, SDF, EC, DWS, AGES (ED 38).
- Research question 1 holds three questions, and "drawn down" for the dam collides with "drawdown" of groundwater; use "emptied" or "low" (ED 27).
- The Map 10 and Table 12 captions, the "inflow" in three senses (remainder, series 1, WR2012 patched flow), and "inflow as recorded" for a calculated inflow (ED 6, 42).
- Recommendation 2 repeats "not updated since 1988" without a citation (CIT D2).
- DRASTIC cited "cited by Esterhuyse, 2017" without the year of the primary source (DWAF, 2005) (CIT M3).
- Discussion note 26 places Saft and Troldborg in "Section 3.4 and 3.2"; they are in 3.1 and 3.2 (CIT).
- Study Area 2.4 keeps a generic sentence ("Groundwater occurrence depends primarily on geology, weathering and effective rainfall") that could sit in any paper (ED 32). DWAF 2004:55–56 says local groundwater "has the potential" to meet domestic supplies; the draft's "can meet" is slightly stronger (CIT S5).
- Study Area 2.1 and Methods 5.3.1 do not say the dam capacity was 3.2 Mm³ until 1966 and 7.88–8.07 Mm³ from 1976 to 1982 (W21).
- Table 12 and Results 6.8: add counts, not only percentages; the percentages have wide intervals (14/74 is 12–29%) (WQ-09, WQ-10).
- Results 6.8: travel time as a range (14–140 years at 0.01–0.10) (G20); the DRASTIC caveat of the old text (G21).
- Methods 5.4.2: Niswonger et al. — "reduces the rate" holds as an option of the package; confirm the run used it or write "can reduce" (CIT M10).

---

## D. Checked and sound

**Surface water** (workbook formulas rebuilt in Python, reproducing the Run sheets to 1e-14 and the forward test exactly: NSE 0.864/0.378/0.595, PBIAS +7.4/−17.2/−22.4)
- Table 9 and Table 10 Reference: 364/118 failure months, reliability 0.590/0.867 by time, 0.446/0.770 by volume, longest events 146/20, resilience 0.044/0.093, vulnerability 0.50/0.88; case M 0.541/0.829 and 0.405/0.703, case D 0.477/0.791 and 0.324/0.635; series 2 0.588/0.865.
- The 146-month event (December 1983 to January 1996, 21.86 Mm³, 40% of failure months); "three times as often" (3.08); inflow classes 843/27/18; median inflow 3.708; 1982–1994 below the median; mean 1985–1994 0.84; 1991 rainfall 314 mm; 38 canal years, 24 shortfall years (63%), mean shortfall 58%.
- Firm yield: no failure at 0.36; one failure at 0.37 in October 1992 (storage 0.211 Mm³) by the reviewer's rerun, so the Results sentence reproduces, although the FirmYield sheet stores only 0.36 and 0.38 (ED could not trace it; the Abstract note and the context file still say 0.38). At 1.5 Mm³/a, 7.9% of months fail.
- Table 6 (three columns, including the 3.39 and 1.23 in the caption), Table 7 (6.21, 3.87, 7.71, 5.01), storage 99.3% (December 1982), 21.9% (March 1984), 2.3% (November 1992); rule fitted on one period (0.586 and 0.393 with 169 months); "the rule costs water" (canal −0.206, evaporation +0.146, spill +0.062).
- Climate: factors, demand 2.49, deliveries 1.86/1.89/1.79, groundwater −3.8%, −5%, −10.5%, −14%; the inflow elasticity of 2.48 by the non-parametric estimator.

**Groundwater** (49b, 49 and the Map10 shapefiles)
- Conductivities, transmissivities, RMS values (14.85/3.85, 8.53/5.03, 8.61/5.15), the 262-level statistics (24.3/16.9/14.9; 31/62/71%), lowest-ground residuals, 114/14 boreholes within 5 m; budgets (7.67/9.86; 16.90/0.63); P1 drawdowns, delivered rates (D maximum 1.23 Mm³/a); Table 11 shares; the 69%/20% river split; the scaled-pair factor of about 8; event rates 1.80 and 2.05.
- Particles: 405, 387 (95.6%), 45 (S) and 288 (D) in their start cell; median 143 years at 0.10. The recharge of 4.84% agrees with 17.336 Mm³/a over 602 km² (28.8 mm/a). Canadell et al. (1996) supports the 15.0 m in 5.2.2 (mean of species maxima, n = 15). Removing the Leake & Barlow "analytical solutions" sentence is justified.

**Flood** (SANRAL text, hydrograph workbook, cell shapefiles)
- Tc 16.44 h (16.43 h with S rounded); Hershfield 122.1 and 140.7 mm at 6 h; interpolation 138.3 and 161.8 mm; ARF 84.4%; C50 36.4%; SDF peaks 974.5 and 1 252.8; Midgley and Pitman 889.5 at 597 mm and 838.8 at 563 mm; RMF K3 1 205 and K4 2 355; hydrograph volumes and the 16.5 h sampling (972.2, 1 249.7, 887.4); flooded and deeper-than-1-m areas (7.716/6.27, 7.970/6.668, 7.603/6.110, 8.342/7.024 km²); derived percentages (+29%, +3%, −5%, +5%, 0.25 km² ≈ 8 m, 0.2%).
- SANRAL pages 3-4, 3-45, 3-47, 3-61/62, 3-65 to 3-67 and 3B-2 say what the text says. The dolomite share (629.59/1 357.26 = 46.4%) and "all above the dam" (F1 and F2 both 629.59 km²) reproduce.

**Water quality** (49d CSV, DBF files, DWAF volumes read through WebFetch)
- Shares as whole counts: EC above 40 mS/m at A3H030 48/56, A3H042Q01 80/81, A3R003Q01 42/248, A3H016Q01 0/54; PO4-P above 0.025 at 14/74, 2/56, 67/230, 8/41, 1/3, 1/1; inorganic N 9/73 and 3/73. EC medians and n. Mixing arithmetic (20.7 − 0.19 × 62.3)/0.81 = 10.9 mS/m. Guideline values and pages: EC 40 mS/m (1996a:155), inorganic N (1996b:84), inorganic P (1996b:97), average-summer basis (pp. 82, 96). The DWAF (2004:86) quote.

**Citations**
- Supported: Leake & Barlow (2013) for capture; SANRAL 3-45, 3-4, 3-47, 3-61/62, 3-65, 3B-2; Canadell (1996); Pollock (2016); Moriasi (2007) p. 888 and the NSE/RSR limits of p. 891 (the RSR sign to be confirmed once); NRCS p. 7-2; Esterhuyse for the DRASTIC classes; DWAF 1996b pp. 84 and 97.
- Every citation in the drafts has an entry in the reference list. The five proposed removals (Pyburn, Kapangaziwiri, Fowler, Peterson, News24) are cited in no kept text and in none of the drafts. No other entry becomes uncited. Kovács (1988) stays (line 568); Sankarasubramanian and MacDonald 2021 survive the 5.2.4 replacement if the range starts at "(2001:1775)." as the draft says.

**Editor**
- The voice is impersonal throughout, with no first person, no em dash and none of "robust", "crucial", "comprehensive", "significant" or "overall". The Results follow the Introduction's order (what was done, why, what was found). The Methods edits are careful and mostly match the Introduction. The Discussion and Conclusions have at most two numbers per paragraph.

---

## E. Could not check

- **Not in the package:** the raw water-quality records (medians, detection limits, SAR at 1.5, the Cl, Na and SAR counts, the 20.7 mS/m with n = 87); DWS (2021) pp. 156 and 163 (scanned gazette: 936 people, 17.336, 2.00, 0.81, 0.285, 17.7 mS/m from seven samples); the GRAII and NGA extracts (22.81, 0.00998, 0.00014, 25.36, 182.14, 47.5, the 112 levels and the median 15.27 m); the WR2012 source of the baseflows 2.53 and 3.43; the geological and hydrogeological maps; the DRASTIC layer (96.7%/3.3%); the SANLC layer and `landcover_flooded.csv` (8.04 km²; 3.13–3.33 km² flooded; irrigated land flooded); the reverse-test sheet; the hydrograph CSVs (outflow peaks, delay, floodplain storage); the `Map09_additional_lowering` files; the drain type of each endpoint (so the 387 river endpoints cannot be recomputed).
- **Sources not opened or read second-hand:** Klemeš (1986:13); DWAF (2004) pp. 54–57, 83, 86, 170–171 (the last quarter was not read; pages are as the fetch tool reported them); Schulze & Schütte (2023) (dataset readme only); DFFE (2024) "classified from satellite images" (not found); MacDonald et al. (2012) p. 2 (HTML has no page markers); Pollock (2016), Niswonger et al. (2011) and Moriasi (2007) were read through WebFetch summaries and need one check at the source; SANRAL Table 3B.2 (Struan 150 and 177 mm) is an image; Smithers (2012); Bredehoeft et al. (1982).
- **Not checkable from the files:** SDF basin 1 and veld zone 8 (map images); L, S and Lc from the GIS (no layers); the 563 mm; the HEC-RAS Manning's n ranges (bare 0.022 is 0.001 below the lowest value in Update24); the Figure 15 and Map 10 images; the convergence of the shallow-water run.
- **Outside the brief:** Sections 3 and 4 and the unchanged Methods text were read for context only.

---

## Where the reviewers disagree or differ

- **0.37 Mm³/a failure month.** ED could not trace it (the sheet stores 0.36 and 0.38). W reran the formulas and reproduces one failure at 0.37 in October 1992. The sentence stands; the run should be stored in the workbook, or the sentence changed to "about 0.37".
- **Flood limit.** F1 asks for the sentence "not calibrated" to return. You declined it on 9 November at 21:33. Both positions are in B5; the evidence that would settle it is whether Sascha asks.
- **Inflow-residual limit.** ED and W want it stated; your rule keeps limits out. Settled by your decision in B5.
- **"Thirteen" years.** W, ED and CIT agree on the facts (ten by the workbook rule, thirteen by bridging 1994). They differ only on the remedy; B1 gives both.
