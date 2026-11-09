# Review of the Methods changes (version 1) and the flood Methods (version 4)

Report of 9 November 2026. Block: `drafts/Methods_changes_v1.md` with `drafts/Methods_flood_SDF_v4.md`. Panel: surface-water hydrologist, groundwater hydrogeologist, flood hydrologist, water-quality reviewer, literature verifier and academic editor, each working alone. Nothing in the article, the workbooks, the result files or the drafts was changed. Where I checked a reviewer's claim myself, it is marked "checked".

The citation check was interrupted by a usage limit and resumed at 20:55; it is included (A19 to A23 and Section E). Sources read in full text by the verifier: the SANRAL manual, the WR2012 executive summary, Knowling & Werner (2016), Leake & Barlow (2013) and Canadell et al. (1996, scanned, read by OCR). Pollock, Moriasi, Niswonger, Barnett, SKM, Woessner & Poeter and DWAF (1996b) were read only through a fetch tool that returns a summary, so their pages are marked "to confirm".

**Summary.** 23 clear errors (A), 17 decisions for you (B), 10 wording groups (C). The block is not ready to go into the article. Three problems stop it: (1) several sentences state something that the files do not support or that the Results contradict; (2) some Methods contain results, limits or interpretations that belong in the Results or the Discussion; (3) the Results report quantities for which no method is described. The SDF table is the best new part. The Midgley and Pitman rainfall of 563 mm is defensible and stays.

---

## A. Clear errors

Ranked by severity.

**A1. The Table 5 note was not changed, and it states a cause that the Results contradict (critical).** The "replacement" for the note under the climate table is word for word the current sentence: "Because the low inflow of 1982 to 1994 was not caused by low rainfall...". Results 6.2 says that the rainfall was well below the mean in 1982–1985 and in 1991, and Section 1.1 says only that the inflow stayed below its median although the rainfall of 1986–1995 averaged 99% of its mean. The sentence also gives a cause as settled. A further point is missing: the elasticity of 2.0–2.5 was estimated on the WR2012 patched inflow, which contains this period (Update 24, section 1), so the period may bias it. *Surface water M1, editor M26; checked against article lines 226–228 and 1019–1023.*

**A2. The reverse test is described wrongly, and neither test is independent for the demand pattern (major).** In 5.2.1 I wrote "the pattern of the months of the fit period in which the dam stood at 85% or more". In the reverse test the pattern comes from the full-dam months of 1966–1974 and 1981–1986, which are the years being tested, not from the fit period 1987–2009. The monthly pass of the reverse test depends on it: the reviewer reproduced Table 8 only with that pattern (monthly NSE 0.56), and with the Figure 3 pattern the NSE is 0.14. In the forward test, Figure 3 (1997–2014 without 2010) overlaps 13 of the 23 test years. The kept sentence in 5.4.1, "the test is independent only for the restriction rule and the demand", therefore holds for the rule only. The Table 8 caption ("the pattern comes from the canal record of the years tested") does not fit the forward test. *Surface water M2, M3; editor M21.*

**A3. The count of runs is from an old design (major).** "Twenty-seven of the 74 runs of the design" is the count of 11 October, before cases A, B, C and the stress test left the article (recharge ×0.72, ×0.80, ×1.20). The run list in the result file names 13 runs in S and 13 in D, which is 26, not 27 (checked: the list is in `49b_Groundwater_results.txt`, section 11). The runs behind the article now include the ×0.96 and ×0.89 runs with and without wells, which the count does not describe. The factors 0.72 and 1.20 appear nowhere else in the article. *Groundwater G1, editor M43.*

**A4. The porosity statements do not match the Results or the evidence (major).**
- My note says the Results use 0.10 for the deposits and 0.01 for the bedrock. They do not. Results 6.8 gives times at one porosity of 0.10 (1 404 years × 0.10 = 140 years). The zoned 0.10/0.01 appears only in Update 24, marked "source to be found".
- The rule "time at n = time at 1.0 × n" holds only when one porosity applies along the whole path.
- "A porosity of 0.01, within the range for fractured crystalline rock" has no source. The bedrock of A31E is mostly Pretoria Group quartzite, sandstone and shale, which is not crystalline (Section 2.4), and fracture porosities may be lower than 0.01, so 0.01 is not a lower end.
- The kept paragraph in 5.2.2 says "a porosity of 0.10 is used", and the new 5.3.2 says "1.0 was entered". Both cannot stand as written.
*Groundwater G3, G4; water quality MP-1, MP-2; editor M24, M45.*

**A5. The mixing check cites the wrong table and the note contradicts the text (major).** The 19% is not in Table 7. It comes from the sentence "5.01 of the 6.21 Mm³/a (81%) that reached Kromellenboog Dam did not come from the upper dam" (article lines 1380–1382, checked). The same wrong citation is in Results v4 6.8. My change note says that the result is "only reported in the Results", but the Methods paragraph prints "10.9 mS/m", and the Results print "about 11". With the unrounded share (1.20/6.21 = 0.193) the result is 10.7, so "10.9" claims more than the inputs carry. The stations and sample numbers are not named (A3H042Q01, 81 samples; Kromellenboog Dam, 87 samples, a count that is not in the screening file). *Water quality WQ-1, WQ-3, WQ-4; editor M53; surface water M13.*

**A6. Sulphate is not screened (major).** 5.1.4 says that sulphate is screened. The Table 12 caption says "sulphate has no guideline in this screening", and the screening file has no sulphate exceedance column (checked). Sulphate is reported as a median only. The inherited sentence also parses as "EC measures sulphate, chloride...". *Water quality WQ-5, editor M11.*

**A7. The series 2 figures in 5.4.1 are in the wrong place and one does not reproduce (major).** The bracket says that they are stated in Results 6.3. Results 6.3 does not report series 2. The reliability (0.588 and 0.865) reproduces from the sw2 workbook. The firm yield of 0.30 Mm³/a is in no workbook: the reviewer's recomputation on series 2 gives no failure at 0.31 and one at 0.32, so about 0.31. These are results; Methods should say only that series 2 was run as a check. *Surface water M5, editor M39.*

**A8. The base of the weathered zone: 47.5 m against 25.36 m (major, inherited).** The article gives the weathered zone as 25.36 m thick and the fractured zone as 182.14 m (lines 406–416, checked), but the model and the counts of cells "below 47.5 m" use 47.5 m. The difference of 22.14 m is not explained. This was raised by the panel of 8 November and is not addressed by the draft. *Groundwater G7.*

**A9. The weights for the 563 mm do not add up with the project's own areas (major).** 486 + 705 = 1 191 km² is larger than the dam catchment of 1 162.09 km² (Table 14a), and the project's own split puts 195 km² of F2 in A31E, not 166. The mean is not sensitive to this (562.6 mm with 166 km²; 563.5 mm with 195 km²; both give 563 mm and the same peaks), but a reader will see that the areas do not agree. *Flood F1; the sensitivity is checked in the reviewer's code, and 100–250 km² gives 561–565 mm.*

**A10. 5.4.3 describes a comparison that no Result reports (major).** I wrote that the outlines were compared by "the depth of the water surface in the cells that are wet in both floods". The 0.28 m was taken out of 6.7. The "width by which the outline moves" is the added area divided by twice the reach length (0.254 km² / 15.7 km / 2 = 8.1 m); along the stepped outline the mean shift is about 4.5 m. "Depth of the water surface" also confuses depth with elevation. *Flood F2, editor M50.*

**A11. Basin 1 and veld zone 8 are stated as fact (major).** "The catchment at F2 lies in SDF basin 1" and "K_T for the Bushveld" are map readings that no file or chat settles (gaps 1 and 4 of the flood notes). The result is sensitive: with the Grassland factor (zone 4, K_T100 = 1.20), the 1:100 Midgley and Pitman peak would be about 1 006 m³/s, not 839. *Flood F7, editor M33.*

**A12. "Flood risk was assessed" (major).** The kept first sentence of 5.2.3 says so. Results 6.7 was retitled "Flood extent and depth" because it reports no hazard (depth × velocity was not computed). *Flood F3.*

**A13. Two different tables are called Table 5 (major).** The flood table (5.2.3) and the climate table (5.2.4) both carry the number 5 in consecutive subsections, so 5.2.4, 5.3.3 and 5.3.4 are ambiguous. Tables 10 and 11 are also used twice across the Results drafts. *Editor M4, surface water M14, flood F13.*

**A14. The runs "not made" are described too strongly or wrongly (major/minor).**
- "Covered only by the scaled pair, structure D with the conductivities of S, and the two structures" reads as covered; the result file says "partly covered". The drain conductances (×0.1, ×10 and ×0.001) were never varied, so how the pumped water splits between the river drains and the ground drain is untested against them. "No result of the study rests on the runs that were not made" is a statement about robustness that belongs to the limits. *Groundwater G2, editor M43.*
- The scaled pair was not run. Its values are the unscaled runs at the other rate (halved at 0.5 Mm³/a equals 1.0; doubled equals 0.25). The Methods say "Two further runs". *Groundwater G5.*
- "Was read between the runs" suggests an interpolated value was reported; Block 2 reports none and gives the runs on either side. *Groundwater G15.*

**A15. The RMF as "an upper limit" is contradicted by the result (minor).** The SDF 1:100 peak (1 252 m³/s) exceeds the RMF of region K3 (1 205 m³/s). The manual calls the values the upper realistic limits of recorded floods and says that where a catchment falls in two regions the value is adjusted proportionately or the higher one is accepted (p. 3-66). *Flood F15, editor M32.*

**A16. The Midgley and Pitman hydrograph peak is 837.5, not 839 m³/s (minor).** The 15-minute grid misses the apex by 0.06 h, as for the SDF series. After the rerun the "Peak in" of Table 11 will be about 837–838. Step 10 of the table gives no sampled peak for Midgley and Pitman. *Flood F8; checked against the CSV (maximum 837.5).*

**A17. Smaller numbers and citations (minor).**
- Results v4 6.6: "3.78 m, which equals the increase in the drawdown from 20.6 to 24.3 m"; 24.32 − 20.57 = 3.75. Write "about equals". *Groundwater G19.*
- "Between 1982 and 1994 ... in the cases" aside, the flood note "differ by 41%" is stale; at 563 mm it is 49%. *Flood F18.*
- The Table 5 caption (flood) cites pages up to 3B-2; Table 3B.2 is on 3B-3. *Flood F16.*
- Kovács (1988) is cited directly; the author decided to cite flood methods from SANRAL (2013) only. *Flood F14.*
- 5.2.1: series 2 differs from series 1 only from October 1966 to January 1987 (223 months), not "before 1987"; "used in all runs" contradicts the check run on series 2. The capacities of 7.88 Mm³ (1965–1975) and 8.07 Mm³ (1976–1981) are verified in the workbook (Inputs column G), and spill and the storage zones use the capacity of the date while the area curve is capped at 7.07 Mm³. The numbers of complete years in the tests are 14 and 20. *Surface water M9, M11.*
- Canadell et al. (1996): the earlier doubt is settled. The verifier read the scanned PDF by OCR: "15.0 ± 5.4 m for tropical grassland/savanna" (n = 15; highest value 68 m). The sentence is supported; "mean of reported species maxima" would be more exact. *Literature M8.*

**A19. The WR2012 catchment rainfall is not in the source cited (major).** Bailey & Pitman (2016), the executive summary, gives no MAP for A31C, A31D or A31E (the verifier searched the full OCR text). The values (546, 566 and 597 mm) come from the WR2012 quaternary spreadsheet (WMA 3 file, `wr.xls`), which is not in the package. The same applies in 5.1.3, 5.2.3 and the table. Cite the spreadsheet as a dataset with the access date, and keep the executive summary only for the description of WR2012. *Literature M5, F11.*

**A20. Leake & Barlow (2013) does not say that analytical solutions need measured properties (major).** The sentence "A31E has no measured aquifer properties for analytical solutions (Leake & Barlow, 2013)" (article line 1079, kept in my replacement) is not in the 4-page fact sheet; it says only that numerical modelling is the most robust approach (p. 3). Reword so the citation carries what it says ("numerical models are the most robust way to find the rate, place and timing of streamflow depletion", p. 3), and leave the statement about missing aquifer properties as the author's own. *Literature M10.*

**A21. Woessner & Poeter (2020) supports 0.10 only loosely and 0.01 not at all (major).** Table 2 of the web book gives effective porosity of 0.01–0.46 for fine sand, 0.01–0.39 for silt and 0.01–0.18 for clay, so 0.10 lies inside very wide ranges; for fractured crystalline rock it lists total porosity (0.00–0.10) only. The book has no printed pages: cite the section and table. See A4 for the 0.01. *Literature M15.*

**A22. DWAF (1996b:84) covers nitrogen only (minor).** Page 84 is the inorganic nitrogen table ("average summer effects") and says that average summer concentrations are the best basis and single measurements a poor one; phosphate is on p. 97. Write "(DWAF, 1996b:84, 97)" and give the guideline's own basis (the summer mean) instead of the author's judgement. *Literature M16, water quality WQ-7.*

**A23. The flood table's caption attributes more to SANRAL than the manual says (minor).** Rows 4 (GIS values), 11 (P = 563 mm from WR2012) and the method for Lc are not from pages 3-44 to 3-62. The manual defines Lc only as the "distance between outlet and the centroid of the catchment" (3-61) and P as the mean annual rainfall over the catchment (Figure 3.7); "along the main watercourse" is your choice (and the helper's recomputation), and the area-weighted WR2012 value is your substitution. State both as choices. Add page 3B-3 (Table 3B.2) to the caption. The "on whose boundary" location of K3/K4 is a map reading (Figure 3.37, an image). Step 4 of the manual gives S in m/km and Eq. 3.17 uses m/m; one note under the table settles it. *Literature F3, F4, F10, F12.*

**A18. Statements of fact that are not facts about the method (minor).** "A single factor for the whole year... so the cases may understate the loss of reliability" gives a direction of bias that no run has tested; see B6.

---

## B. Interpretations the author must decide

Each has the options and the cost.

1. **Which run design is the reference, and how the runs not made are stated (A3, A14).** Option (a): list the runs behind the article in a small table (rate, placement, structure, recharge) and give the runs not made against that list, without "of 74", 0.72 or 1.20; cost: one table and your confirmation of the count (26 by the file list). Option (b): state only the limits ("the drain conductances were not varied") and drop the count; cost: the reader cannot see what was run. Surface water and groundwater reviewers favour (a); the editor wants the count and the assurance sentence deleted in both options.

2. **Porosity: one value or two zones (A4).** (a) One value of 0.10 for all cells, times scaled to other values; this matches Results 6.8 and is simple; cost: the 0.01 alternative is then a sensitivity only, and needs a source or a different wording ("for comparison"). (b) Zoned 0.10/0.01 as in Update 24; cost: the times must be recomputed by path segment for the 4 bedrock start cells, and a source for 0.01 is still needed. In both options "fractured crystalline rock" should become "fractured bedrock", and the source must be one that has been opened.

3. **Where 47.5 m comes from (A8).** Either give the GRAII field that yields 47.5 m, or change the threshold to the 25.36 m of Section 2.4. Cost of changing: the counts "19 of the 45 cells" and the 91% storage share change or must be rerun; cost of keeping: an unexplained 22 m difference to an examiner.

4. **The mixing check (A5).** Options: (a) keep the method with its assumptions in the Methods and the value (about 11 mS/m) only in the Results 6.8, and drop "If that share applied..." from the Results (water quality and the editor); (b) keep the calculation in the Results and only name it in the Methods (the current Results v4). Assumptions to name if kept: evaporation in Kromellenboog Dam raises its EC, so the local value would be lower; the medians of grab samples are not flow-weighted; the upper-dam water is taken at 62.3 mS/m although the sites between the dams have medians of 76–83 mS/m (with them the result would be about 6–8 mS/m, checked: 7.7 and 6.2); and the 81% is a net contribution. Cost of naming all: three more sentences; cost of naming none: the check looks more precise than it is.

5. **The reverse test and the demand pattern (A2).** Options: state that the reverse test is not independent for the monthly pattern and give the pattern-1 sensitivity (NSE 0.56 against 0.14); or state the independence limit without the numbers. The limits sentence in 5.4.1 must change in both cases.

6. **The "later start of the rains" sentence (A18).** Options: delete it from the Methods and keep it in Section 7 (the editor; it already appears at lines 1970–1974 and is a limit); reword neutrally in the Methods ("a single factor does not represent a change in the seasonal distribution, such as the projected decrease in September–November", surface water); or keep it as I wrote it (cost: an untested direction of bias). Nothing in the context supports a later start; Howard and Washington (2020) give about half a month at the end of the century under RCP8.5.

7. **Series 2 results (A7).** Put one sentence in Results 6.3 (0.588 and 0.865; firm yield about 0.31 if you accept the recomputation, or 0.30 if you can show the source) and write only "run as a check" in 5.4.1. Cost: one Results sentence; the alternative is that the check is reported nowhere.

8. **The flood choices.** (a) *The 1:50-year reason.* The reviewers (flood F11, editor M49) find "to compare its outline with that of the 1:100-year flood" circular, and the reason in my note is drawn from a result. Option: give a design reason (how sensitive the outline is to the return period), or drop the sentence. (b) *The 0.28 m.* Either bring it back into 6.7 or take its clause out of 5.4.3 (A10); it was taken out of 6.7 on the editor's advice. (c) *Selection of the design flood.* The manual (p. 3-4) says that where methods differ widely the selection must be motivated. The gap is now 49%. Option: say that no single design flood is selected and that the SDF and Midgley and Pitman runs are two cases; or say which is taken. (d) *The model limits* (no flood mark or rating, the 25 cells at the northern boundary, SRTM channel heights of February 2000): in 5.4.3, next to Table 11, or in the Discussion. (e) *Land-cover classes* that define "cultivated" (8.04 km²) and the irrigated layer must be named in 5.4.3 or 5.3.3, and the measure of attenuation and stored volume must be described (flood F10, editor M51).

9. **The split of F2 for the weights (A9).** Print the GIS split (A31E about 195 km², with A31C and A31D in proportion within 1 162 km²) or the subtraction (166 km²). The mean is 563 mm either way; the GIS split is the defensible one.

10. **The letter D (groundwater G11, editor M22).** "D" is both a model structure (deep ground drain) and a climate case (dry end). Options: always write "structure D" and "case D" in full; or rename one (climate cases "central" and "dry"; or structures "shallow" and "deep"). Cost: Results 6.6 and the tables change.

11. **The base years in the climate table (surface water, question 1).** Update 24 gives the change "against the mean of the water-balance record, hydrological years 1937–2009", the elasticity from 1936–2009, and the runs cover 1936–2009. Which period should the caption state?

12. **A limitation on the inflow itself (surface water M10).** The inflow is a remainder that carries the errors of the storage, area curve, evaporation and outflow records, with 14 minimum months and 6 negative remainders set to zero. Place it in 5.2.1, in the Discussion, or both. The "Reference run... recorded inflow, evaporation and demand" would then read "inflow series 1 and the registered volume".

13. **"Lower bound" in 5.4.1 (surface water M6).** My proposed wording ("the unrestricted run gives the highest reliability, because... much of the water held back is lost to evaporation") explains a result in the Methods and is incomplete (the Results give the loss to evaporation and spill). Option: "the run without restriction gives the higher reliability by time and by volume, because every restricted month counts as a failure; the run with the rule reproduces the average restriction found in the records", with the reasons left to the Results.

14. **The HEC-RAS rerun (flood Q7).** If the Q100_MP plan is not rerun, the Methods must return to 597 mm and say it is the rainfall of A31E only; I recommend the rerun, because the whole Midgley and Pitman row of Table 11 and the ranges that include it wait for it.

15. **Citation of Kovács (1988) (A17).** Cite "Kovács (1988, cited by SANRAL, 2013:3-65, 3-67)", or add the direct citation to the reference list after opening it.

16. **What the Methods must cover that the Results use (editor M42, M51).** The Results use methods that no Methods paragraph describes: the Kromellenboog balance and the "net contribution", the rank correlation, the count of complete years and the shortfall run, the rule refitted on one period alone, firm yield at the lowest usable storage (0.44), months below half the registered volume, the storage exceedance curve (Figure 14), the Reserve balance, the shortfall as a share of recharge, and the flood overlay, peak reduction, delay and stored volume. Options: add a short paragraph per method to 5.4.1–5.4.3, or cut the result that has no method. Cost: about six short paragraphs. This is the largest open item.

17. **Where Map 7 and the checks sit (editor M47, M37).** Map 7 shows a result and is in 5.4.2; the editor would move it to Results 6.6. The sentence "the two runs gave identical end points" is a result in 5.3.2; keep as one check sentence or move it to 6.8.

---

## C. Wording and repetition

1. **Notes inside article text (editor M1, M2).** The [unverified] and "[decision for the author...]" marks sit inside sentences, and the italic is used for both instructions and notes. Use one convention in both files: article text as plain paragraphs, every instruction or note in a labelled "Note" line, and no sentence offered for the article until its fact is checked. Reprint only the sentences that change, with an anchor (editor M3).
2. **Repetition (editor map).**
   - The fit and test years appear five times (the paragraph above, the Figure 2 caption, 5.2.1 addition, Results 6.3, the Table 8 caption). Describe the test design once. The editor puts it in 5.4.1 (Analysis); the surface-water reviewer wants the years of each pattern named in 5.2.1. Settle by putting the design in 5.4.1 and leaving only the data (capacities, patterns) in 5.2.1.
   - The hydrograph (15-minute values, 5 m³/s floor) appears three times; Manning's n and the shallow-water check twice each; the climate factors in the table, 5.3.4, 5.4.2 and 5.4.4; the Midgley and Pitman rainfall in 5.1.3, 5.2.3 and the table; the station list in 5.1.4 and 6.8.
   - 22.81 m²/d is already in Section 2.4 as "modelled regional value for A31E", and "mean" is not in the article. Delete the clause from 5.1.2.
   - The drought definition is in Section 1.1 and need not be repeated; my sentence on "other spans" names no span, explains nothing, and lists "the storage" as another measure although the drought itself is a storage measure. Delete it, or name the spans (1982–1994 inflow; December 1983 to January 1996 rule event; the canal run of 13 years).
3. **Results in Methods (editor M29, M39, M40, M53).** Remove the design and sampled peaks from the end of the SDF table (it should end at the inputs; the peaks stay in Table 11; the flood reviewer asks to decide this, F5), the series 2 figures, the explanation of lost water in 5.4.1, and the value 10.9.
4. **Interpretation and defensive sentences.** "No result of the study rests on the runs that were not made", "the number of years is small in both directions", "the check indicates an order of magnitude only", "so that the supply is judged against a demand that grows with the warming".
5. **Terms.** "Reach" (the 15.7 km flood reach) against "the river between the dams" (also in article 4.3, line 643, and 6.x); "path 2" includes the groundwater; "phosphate-P"; "water table" (simulated) against "water level" (measured); "drawdown" and "lowering" defined twice in two sentences (use one: the lowering is the difference in the water table between two runs with the same abstraction, one at base and one at reduced recharge, which also fits structure D); "demand", "registered volume raised", "raised volume", "asked for" (one term); "mean annual rainfall" against "MAP" (the catchment at F2 is not the 597 mm of Section 2); "residual" with "water level" (use water-table elevation and state the sign once); "RMS" against "root mean square error".
6. **Plain language.** "An interval of 10 m each" and "weak sink" are undefined for the reader; "the three sites along the reach" must change if "reach" changes. The sentences "so that", "namely" and lists of three or four items should be shortened.
7. **The SDF prose and the table repeat each other (editor M28).** Keep the reason for each choice in one or two sentences and the values in the table. The instructions of the two files disagree about what is replaced in 5.2.3 (flood F4, editor M31): give the range once.
8. **Smaller wording points.** "S for the shallow and D for the deep ground drain" hides that the conductivities were also estimated separately; the groundwater reviewer suggests "whose conductivities were then estimated separately (Section 5.3.2)". "Both structures are needed because the records contradict each of them (Section 6.4)" is a result and a pointer; give the reason (four static levels cannot identify one conceptual model). P2 and P3 need their rates and "evenly". The step 6 interpolation should say "linear between 6 h and 24 h", and the elevation model and ARF equation should be named (flood F17). A statement of the limits of the residual: four points give no statistical power, and the share within 10 m and the mean residual are also used in the Results.
9. **Abbreviations.** EC and DWS are defined again in Results 6.8; "hydrological year" is used from Section 4 but defined in 5.2.1.
10. **Out of scope, noticed.** Results 6.2 gives a run of thirteen shortfall years (1984–1996) while the project context gives ten (1984–1993); the Abstract and Conclusions still say ten. The Params labels in the workbook still read "A: +1 C" and "Run_A... inflow −20%".

---

## D. Checked and sound

- Record of 888 months (843 + 27 + 18); drought as 139 of 144 months below 25% of capacity; rule shares from 0.036 to 1.00 above 57%; reference reliability 0.590/0.867; series 2 reliability 0.588/0.865; M and D reliability 0.541/0.829 and 0.477/0.791; the raised demand 2.34 × 1.064 = 2.490 (surface water, recomputed from the workbook).
- The forward test (NSE 0.864/0.378/0.595; PBIAS +7.42/−17.21/−22.36) reproduces exactly; the reverse test reproduces with rule 2, pattern 2, series 1 and the capacity of the date.
- Firm yield: no failure at 0.36; one failure at 0.37 and 0.38 (October 1992), so "0.37" in the Results is correct.
- Climate factors follow from Update 24 (−3.1% × 2.0–2.5 gives 0.92–0.94; recharge 0.96 and 0.88–0.89; 3.4% per °C).
- Residual sign and RMS (S 14.85, D 8.53, benchmark 8.61 m); depths 1 m and 15.27 m; transmissivities of S and D; the content of the scaled pair; MODPATH settings (no wells, 405 particles, porosity 1.0, pass-through and stop identical); 1 404 × 0.10 = 140 years.
- Site counts and periods in 5.1.4 match the screening file; Results 6.8 values reproduce; the mixing arithmetic gives 10.94 mS/m and the sensitivity to the share (10% → 16.1, 15% → 13.4, 25% → 6.8, 30% → 2.9).
- All six SDF peaks (92, 289, 464, 662, 974, 1 252 m³/s); S = 0.005355 m/m, Tc = 16.44 h, ARF 84.4%, C50 = 0.364; Midgley and Pitman 374/507/703/889 at 597 mm and 352/478/663/839 at 563 mm; 67% of the SDF peak, the SDF 49% higher, 33% lower; the workbook hydrographs; the flood areas from the cells files (7.716, 7.970, 7.603, 8.342 km²; 6.262, 6.662, 6.103, 7.011 km² deeper than 1 m; 278 cells, 0.254 km², 8.1 m). The SANRAL pages cited are correct.
- **563 mm is defensible.** The manual defines P as the mean annual rainfall over the catchment; A31E alone covers about 12–14% of F2; the result moves only between 561 and 565 mm for any A31E share from 100 to 250 km²; Struan's own value is 550 mm. The reason in the approved text for 597 mm (rainfall zone A3B) must not be carried over.
- Removing "would otherwise have flowed to Kromellenboog Dam" from 5.4.2 is correct (it is in Section 7.2). Knowling & Werner (2016) supports non-uniqueness from the correlation between recharge and conductivity.

---

## E. Could not check

- Pages still to be confirmed on the printed copies (the verifier read these through a summarising tool): Pollock (2016) pp. 2 and 19 (porosity in the velocity equation; pass-through or stop at weak sinks); Niswonger et al. (2011) p. 14 (well rate reduced as the head nears the cell bottom, PHIRAMP); Knowling & Werner (2016) p. 974 (read in full; "a unique solution for recharge and K cannot be obtained"); Moriasi et al. (2007:891) Table 4 (the extracted table was garbled); Barnett et al. (2012:20–21) Table 2-1; SKM (2013:18) (the passage lies between pages 17 and 19; the printed page is unconfirmed); DWS (2021:156) for the recharge, use and baseflow of A31E (an earlier check matched p. 156). Barnett's Class 1 wording says "extraction", so paraphrase it without quotation marks.
- Supported without change (verifier): the SANRAL pages 3-4, 3-44 to 3-47, 3-61, 3-62 and 3-65 to 3-67 for what they are cited for, including the warning on dolomite (3-45) and the requirement to compare with other methods (3-4); "conservative case" is your reading (the manual says the SDF produced satisfactorily conservative results in its calibration catchments).
- Possible sources, none opened: Barlow & Leake (2012), USGS Circular 1376 (named in the Leake & Barlow fact sheet); WR2012 User Guide TT 684/16.
- Esterhuyse (2017): the verifier could not open it (an unrelated Esterhuyse et al. 2017 paper does not describe the DRASTIC map). The page and the DWAF year (2005 per your notes) are needed.
- DWS (2021) gazette p. 163: confirmed by me in Chrome earlier today (A31E, seven samples, median 17.70 mS/m); the reviewers could not open it, and the Results v4 note still calls it unverified. The note should be updated.
- DWAF (1996a, 1996b) printed pages; Esterhuyse (2017) and the DRASTIC primary source (DWAF, 2005, not in the reference list); Canadell et al. (1996) (scanned); Barnett et al. (2012), SKM (2013), Niswonger et al. (2011), Pollock (2016), Woessner & Poeter (2020); Kovács (1988), Farr et al. (2007), USACE HEC (s.a.b); the IPCC Atlas values.
- The raw extract behind 20.7 mS/m (n = 87); the WR2012 values for A31C and A31D (the reviewer had only the A31E row; I have the full table in the scratchpad).
- GMS and MODPATH run files; HEC-RAS project files; the outflow hydrographs; the overlays behind the cultivated and irrigated areas; Lc, L and the elevations 1 155 m and 1 533 m (no catchment layer in the package); the map readings of Figures 3.20, 3.30 and 3.37.
- Whether the weak-sink option was set in both MODPATH simulation files: 45 particles in S and 288 in D never leave their start cell, which suggests strong sinks (groundwater, question 4). One check in GMS settles it.
- Whether the SRTM channel (February 2000) is a water surface (flood, question 8).

---

## Questions for you, shortest form

1. Run design and count (B1). 2. One porosity or two (B2). 3. The 47.5 m (B3). 4. Mixing check: place and assumptions (B4). 5. Reverse test: report the pattern sensitivity (B5). 6. Later-start sentence (B6). 7. Series 2 in Results 6.3 (B7). 8. The flood choices (B8). 9. GIS split of F2 (B9). 10. The letter D (B10). 11. Base years (B11). 12. Rerun HEC-RAS (B14).
