# Methods (Section 5): the changes that follow from the new Results, Discussion and Introduction, version 1

Draft for approval. Not in the article. The order of Section 5 stays as it is (5.1 Data, 5.2 Data preparation, 5.3 Data processing within software, 5.4 Analysis, each in the order dam, groundwater, flood, water quality and climate). Only the paragraphs that must change are given below, each with its place in the current text (line numbers of `A31E_Sascha_Correction_text.txt`). A paragraph that is not listed stays as it is. The flood replacement text is in `Methods_flood_SDF_v4.md` and is only referred to here.

Where a sentence rests on something I could not verify, it is marked [unverified] in the text and listed in the notes.

---

## 5.1 Data

### 5.1.2 Groundwater (replaces the last paragraph, lines 838–843)

The mapped layers are the 1:250 000 geological maps (Michaluk & Keyser, 1991; Walraven, 1981), the 1:500 000 hydrogeological map with its borehole-yield classes (Barnard, 1999), the hydrological soil groups (Schulze & Schütte, 2023) and the national land cover of 2022 (DFFE, 2024). The regional transmissivity, storativity, thickness and recharge are those of the GRAII (DWS, s.a.a; Section 2.4), which gives a mean transmissivity of 22.81 m²/d [unverified: area of the mean], and the Reserve determination gives the recharge, use and baseflow of A31E (DWS, 2021). The vulnerability of the aquifer is taken from the national DRASTIC map (DWAF, cited by Esterhuyse, 2017).

### 5.1.3 Flood (replaces lines 847–852)

The terrain of the flood model is the 30 m Shuttle Radar Topography Mission (SRTM) elevation model of February 2000 (Farr et al., 2007), and the roughness follows the land-cover groups of the national land cover of 2022 (DFFE, 2024). The design rainfall of the station of the SDF basin, the runoff coefficients and the flood formulas are those of the drainage manual of the South African National Roads Agency (SANRAL, 2013), and the regions of the Regional Maximum Flood are those of Kovács (1988). The mean annual rainfall for the Midgley and Pitman formula is that of WR2012 for the quaternary catchments A31C, A31D and A31E (Bailey & Pitman, 2016) [unverified: the catchment table is a WR2012 file; confirm the citation].

### 5.1.4 Water quality and climate (replaces lines 856–873; the climate paragraph at 875–876 stays)

The water-quality records are the analyses of the Department at seven sites in A31E (DWS, s.a.e). The sites, in order along the Klein Marico River, with the period of each record and the number of samples with an electrical conductivity (EC), are: A3H030, the river at the weir below Klein Maricopoort Dam (1989–1993; 56 samples); A3H042Q01, the river below the dam (2012–2023; 81); 188257, the river at Kalkdam, Enzelsberg road (2005–2007; 3); 188038, the river at Nooitgedacht (2004–2005; 3); 188030, the river at Dammenbrug (2004; 1); A3R003Q01, Kromellenboog Dam near the wall (1966–2023; 248); and A3H016Q01, the Wilgeboomspruit (1971–1991; 54). Path 1 is sampled below Klein Maricopoort Dam and at the three sites along the reach, path 2 in the Wilgeboomspruit, and both paths in Kromellenboog Dam. The groundwater of A31E has no record of its own in these files, and its EC is the median of seven samples given in the Reserve determination (DWS, 2021:163). EC, which measures the dissolved salts, sulphate, chloride, sodium, the sodium adsorption ratio (SAR), inorganic nitrogen and phosphate are screened. The guideline values are the upper limits of the target range for irrigation and the boundaries of the trophic classes for aquatic ecosystems (DWAF, 1996a; DWAF, 1996b).

*Change: the sentence on the groundwater EC is new (the gazette page was opened and confirmed: A31E, seven samples, median 17.70 mS/m). "The reach" in the old text means the river between the dams here; the Results call it "the river between the dams", so the word "reach" is kept for the 15.7 km flood reach only. Replace "the three sites along the reach" by "the three sites along the river between the dams" in the paragraph above if you agree.*

---

## 5.2 Data preparation

### 5.2.1 Dam water balance (replaces the paragraph at lines 924–929 and adds one sentence to the paragraph at 882–888)

*Add at the end of the first paragraph (line 888):* The drought is the period from October 1983 to September 1995 defined in Section 1.1. The other spans in this study differ from it because they are counted on other series or measures, namely the inflow, the storage, the canal record and the rule.

*Replace the paragraph at lines 924–929:* The inflow of each month is the remainder of the dam's own recorded balance. This remainder is available for 843 months. A further 27 months were rebuilt from the station records and 18 from the WR2012 patched flow, which gives the 888 months from October 1936 to September 2010. This is inflow series 1, and it is used in all runs. Before 1987 a fixed release entry probably overstates the release when the dam was low, and a second, adjusted inflow series (series 2) was prepared for this period and run as a check.

*Add to the paragraph at lines 930–937 (after "(Figure 2, lower panel)"):* The test was made in both directions. In the forward test the rule was fitted on 1966–1974 and 1981–1986 and tested on 1987–2009. In the reverse test it was fitted on 1987–2009 and tested on the earlier years. The number of years is small in both directions. Before 1982 the capacity of the dam was larger than the present 7.07 Mm³, and the area curve was capped at the present capacity [unverified: the capacities of 7.88 and 8.07 Mm³ and the cap come from the notes of Block 1; check the workbook before they go in]. The canal volume of each direction is distributed over the year with its own pattern: the pattern of Figure 3 for the forward test, and the pattern of the months of the fit period in which the dam stood at 85% or more of its capacity for the reverse test.

*Not added here:* the statement that rainfall does not explain the low inflow of 1986–1990. Section 1.1 (lines 228–230) already says it, with its source, and the Methods need not repeat it. Say if you want it in 5.2.4 as well (Block 1, version 14).

### 5.2.2 Groundwater (replaces lines 945–954 and adds a sentence at 956)

The model removes water from every cell through a ground drain, which represents seepage, springs, evaporation and uptake by plants. Two depths of the ground drain are used, and they define the two structures of the model, S for the shallow and D for the deep ground drain. In structure S the ground drain lies 1 m below the land surface. In structure D it lies 15.27 m below the surface, which is the median depth to water of 112 archive levels in A31E and its neighbouring catchments (DWS, s.a.c). These 112 levels include the four calibration levels but none of the 262 levels that are later compared with the model. The depth of 15.27 m is also close to the mean maximum rooting depth of tropical grassland and savanna, 15.0 m (Canadell et al., 1996), although such uptake has not been shown in A31E. The base of the weathered zone is taken at 47.5 m below the surface.

*Change: "S" and "D" are given their meaning here, once. Nothing else in the paragraph changes.*

### 5.2.3 Flood (replaces lines 973–991)

See `Methods_flood_SDF_v4.md` (the SDF steps and the new table, with the mean annual rainfall of 563 mm for the Midgley and Pitman check). Two lines of the old text go: "its watercourse length and slope were taken from GIS" (now step 2 to 4 of the table) and the sentence on the hydrograph (now step 10).

*Keep, as in the current text:* The SRTM model is used for the flood model alone, because the 20 m DEM smoothed the valleys. Manning's n was set for each land-cover group within published ranges (USACE HEC, s.a.b).

### 5.2.4 Water quality and climate (replaces lines 997–1009 and the note under Table 5)

The climate cases are expressed as factors that multiply the value of the Reference run, which is the water balance and the groundwater model with the recorded inflow, evaporation and demand and the regional recharge. They are steps to test how sensitive the supply and the groundwater are to a drier and warmer climate, and they are not forecasts. Case M represents the median of the projections for ESAF for 2041–2060 under intermediate emissions (SSP2-4.5). Case D represents their dry end, with the 10th percentile of the rainfall and the median warming, because the projected warming is narrow in range while the rainfall is uncertain even in sign (Section 3.3). The factors are given in Table 5. A single factor for the whole year cannot show a later start of the rainy season, so the cases may understate the loss of reliability.

*Note under Table 5 (replaces the paragraph at lines 1019–1028 only in its second sentence):* "Because the low inflow of 1982 to 1994 was not caused by low rainfall, this elasticity is an approximate scaling rather than a property of the catchments above the dam." The rest of the paragraph stays.

*Change: "steps, not forecasts" and the sentence on the later start of the rains are the author's own reading in the results file (file 45: "a uniform factor cannot represent the later start of the rains"); I only moved them to the Methods. The factors and the sources are unchanged.*

---

## 5.3 Data processing within software

### 5.3.2 Groundwater (replaces the second and third paragraphs, lines 1071–1084)

The hydraulic conductivity has two zones, surface deposits (3 479 cells) and bedrock (11 663 cells). It was estimated for each structure with PEST (Doherty & Hunt, 2010) within the limits 0.03–3.0 m/d for the deposits and 0.0005–0.05 m/d for the bedrock, using the four static water levels with an interval of 10 m each. The recharge was held at its regional value, because recharge and conductivity cannot be separated in a calibration on heads alone (Knowling & Werner, 2016). The calibrated model without wells is the base case of each structure. The residual of a borehole is the measured water level minus the simulated one, so that a negative residual means that the measured water table is deeper than that of the model, and the fit is expressed as the root-mean-square error (RMS) of the residuals.

A31E has no measured aquifer properties for analytical solutions (Leake & Barlow, 2013) and no water-level series for a transient model. The model is therefore run at steady state, in which the water entering the aquifer equals the water leaving it, and the cases are compared with one another. Particle tracking used MODPATH 7 (Pollock, 2016) in the base case of each structure, which is the model without abstraction. Nine particles were released at the water table in each of the 45 cells under the irrigated land, 405 in all, and tracked forward. The particles were run once with the option that lets a particle pass through a weak sink and once with the option that stops it there, and the two runs gave identical end points. The effective porosity was entered as 1.0, so that the travel times could be scaled to any porosity afterwards (time at porosity n = time at 1.0 × n).

*Change: the definition of residual and RMS; the base case "without abstraction" for MODPATH; the pass-through and stop runs (one sentence, as your results file asks); the porosity of 1.0 and the scaling. The porosity values used in the Results (0.10 for the surface deposits and 0.01 for the fractured bedrock) are in 5.2.2 and 5.4.2.*

### 5.3.3 Flood (replaces the last two sentences, lines 1097–1099, and adds one)

The upstream boundary at F2 is the inflow hydrograph, with an energy slope from the terrain, and the downstream boundary is normal depth. The default diffusion-wave equations were used, and the full shallow-water equations as a check. The hydrographs are the triangles of Table 5 in Section 5.2.3, with values every 15 minutes and a minimum of 5 m³/s.

*Change: only the last sentence is new, and it points to the flood table so that the hydrograph is described once.*

### 5.3.4 Water quality and climate

Stays as it is (lines 1103–1104).

---

## 5.4 Analysis

### 5.4.1 Dam water balance (replaces two sentences, lines 1110–1124)

The sentences that must change are these.
- Line 1124, "The second, adjusted inflow series was run as a check." becomes: "The second, adjusted inflow series (series 2) was run as a check, and its reliability by time (0.588 with the rule, 0.865 without) and its firm yield (0.30 Mm³/a) are reported with the results of series 1." [the figures are from the results file; they are stated in Results 6.3, so they can be left out here].
- Lines 1146–1151, "upper bound" and "lower bound" stay, but "lower bound" is changed to "the reliability with the rule", since the rule is an average of the record and not a bound: "The unrestricted run gives the highest reliability, because every restricted month counts as a failure and much of the water held back in the dam is lost to evaporation. The run with the rule gives the reliability for the scheme as it was operated on average over the record, and a rule that restricts more would lower it further (Section 6.3)." [decision for the author: Block 1 version 14 also says to change this wording; the Results and Discussion already use "with the rule" and "without restriction"].

### 5.4.2 Groundwater (replaces lines 1160–1189 and adds a paragraph before line 1209)

The shortfall was first compared with the groundwater balance of the Reserve determination (DWS, 2021). Such a balance treats recharge as water that is free to be taken, while pumped water is balanced mostly by capture (Section 3.2), and only a flow model can show which discharge is reduced by pumping. With four static water levels and a steady-state calibration, the model belongs to Class 1, the lowest class of confidence in the Australian groundwater modelling guidelines, whose uses include developing coarse relationships between abstraction and impact (Barnett et al., 2012:20–21). Both structures are needed because the records contradict each of them (Section 6.4) and cannot identify a single conceptual model (Section 3.2). The fit was compared with the benchmark, and the 262 other archive levels were compared with both structures afterwards. Neither comparison is a validation (SKM, 2013:18).

Abstraction was run at rates of 0.25 to 2.34 Mm³/a at placement P1. Placements P2 and P3 test whether spreading the abstraction changes the result. The recharge was also multiplied by the factors of cases M and D, 0.96 and 0.89, both without wells and with 0.5 Mm³/a at P1.

Four results are read from each case and compared with the base case at the same recharge. These are the rate actually pumped, because MODFLOW-NWT reduces the rate of a well when its cell nearly dries (Niswonger et al., 2011), the drawdown in the pumped cells, the number of pumped cells in which the water level falls below the base of the weathered zone at 47.5 m, and the change in the outflow of each group of drains as a share of the rate pumped. The drawdown is the fall of the water table caused by the abstraction, and the lowering is the fall caused by a lower recharge. Both are means of the 200 m model cells and not the levels in a single well. The lowering of the water table that a lower recharge causes in the presence of the abstraction is read from two runs that both include the abstraction, one at the base recharge and one at the reduced recharge (Map 7).

*Add before the paragraph at line 1209 ("A steady-state drawdown ..."):* Not every combination was run. Twenty-seven of the 74 runs of the design were made. The rate of 2.0 Mm³/a in structure S at P1 was read between the runs at 1.0 and 2.34 Mm³/a. Placement P2 at 2.34 Mm³/a and P3 at 0.5 Mm³/a were not run in structure D, and the recharge factors of 0.72 and 1.20 were not combined with abstraction. The sensitivity of the model to the conductivities, the conductances of the drains and the depth of the ground drain was covered only by the scaled pair below, by structure D run with the conductivities of S, and by the two structures themselves. No result of the study rests on the runs that were not made.

*Remove from the paragraph:* the sentence "A reduction in the river or stream drains is water that would otherwise have flowed to Kromellenboog Dam." It interprets a result and belongs to the Discussion only (Block 2, version 2, item on 5.4.2).

*Change in the scaled pair (line 1213–1216):* "In one, the recharge and conductivities are halved or doubled, which fits the levels equally well" becomes "In one, the recharge and the conductivities are both halved or both doubled, and the drain conductances are scaled in the same way, which fits the levels equally well".

*Particle times (replaces lines 1218–1220):* The particle times are those of the moving water alone, without dispersion, retention or decay. They scale in proportion to the effective porosity, which was not measured, and a porosity of 0.01, within the range for fractured crystalline rock, would make them ten times shorter than at 0.10. They also scale inversely with the conductivity, which the four water levels do not fix, so that in the scaled pair they would double or halve.

### 5.4.3 Flood (replaces the second sentence onwards, lines 1229–1237)

As the drainage manual requires, the SDF was used as the main estimate and compared with the other applicable methods (SANRAL, 2013:3-4). Because the manual warns that the flood of a dolomitic catchment may be less than half of the SDF (SANRAL, 2013:3-45), the SDF is treated as the conservative case. Four plans were run: the 1:50-year and 1:100-year SDF floods, the 1:100-year Midgley and Pitman flood, and the 1:100-year SDF flood with the full shallow-water equations as a check on the default diffusion-wave equations. The 1:50-year flood is included to compare its outline with that of the 1:100-year flood. The outlines of the floods were compared by their wet area, the depth of the water surface in the cells that are wet in both floods, and the width by which the outline moves. Two simplifications act in opposite directions, since ignoring the attenuation in Klein Maricopoort Dam makes the flood larger, while leaving out the inflow of the Waterkloofspruit makes the flood below its junction smaller. The model was not calibrated, because there is no flood mark or rating along the reach, and Manning's n is taken from published ranges.

*Change: the sentence on why the 1:50-year flood is included is new. The reason is yours (your message of 9 November: the two lines looked identical from the start); I worded it neutrally. Drop it if you prefer. The last sentence (no calibration) is a limit that the flood reviewer asked to be stated, and it can instead go to a limit sentence next to Table 11. The sentence on the comparison of outlines is what Section 6.7 reports (wet area, rise of the water surface, width of the strip).*

### 5.4.4 Water quality and climate (replaces lines 1245–1253)

Each water-quality quantity was compared with its guideline value, and the share of samples above the guideline was counted for each site. A value above a guideline shows that the water could affect its use or its ecosystem, but it does not show that the water is contaminated. The share of single samples above the boundary of a trophic class is a screening indication and not a trophic classification (DWAF, 1996b:84).

The river below the upper dam and Kromellenboog Dam were also compared over their common period, 2012–2023, with a simple mixing check. The check assumes that Kromellenboog Dam receives water from the upper dam and from the catchment between the dams, that the share from the upper dam was the 19% of the inflow found for 1987–2009 (Table 7), that this water has the median EC of the river below the upper dam (62.3 mS/m), and that the EC of the lower dam is the median of 2012–2023 (20.7 mS/m). The EC of the water from the catchment between the dams then follows as (20.7 − 0.19 × 62.3) / 0.81 = 10.9 mS/m. The result depends strongly on the share of 19%, and the other 81% also contains the return flow of canal water from irrigation, so that the check indicates an order of magnitude only.

In the climate cases, the dam was run with the inflow multiplied by 0.93 and 0.80 and evaporation and demand by 1.064. The canal is asked for the registered volume raised by the same factor, 2.34 × 1.064 = 2.49 Mm³/a, and the reliability is measured against this raised volume, so that the supply is judged against a demand that grows with the warming. The groundwater model was run with the recharge multiplied by 0.96 and 0.89 (Section 5.4.2).

*Change: the mixing check is described here with its assumptions and the result is only reported in the Results (6.8). In the current Results (version 3) the calculation is still in 6.8; if you keep it there, the third paragraph of this section can be shortened to its first sentence. The raised volume (2.49 Mm³/a) is my arithmetic: 2.34 × 1.064 = 2.4898.*

---

## Notes for the author (not article text)

**Verified in this session**
- Gazette 45568 (DWS, 2021), printed p.163 (PDF p.41 of gon1559): A31E, 7 samples, EC 17.70 mS/m. The sentence in 5.1.4 stands.
- The SDF steps, the six peaks and the Midgley and Pitman equation: `reviews/Flood_1in50_vs_1in100_and_SDF_inputs_2026-11-09.md`. The mean annual rainfall of 563 mm and the peaks of 663 and 839 m³/s are in `Methods_flood_SDF_v4.md`.
- 27 of 74 groundwater runs were made, and the list of runs not made is from `49b_Groundwater_results.txt`, section 10. The MODPATH settings (porosity entered as 1.0; pass-through and stop identical; no wells) are from `49_Block_3_results_Update24.txt`, section 4. The 0.10 and 0.01 porosities have the source note "to be found and verified"; the Methods cite Woessner & Poeter (2020) for 0.10 only.
- 2.34 × 1.064 = 2.49 Mm³/a, and the mixing check gives 10.94 mS/m.

**Things I could not verify, marked [unverified] above**
1. The GRAII mean transmissivity of 22.81 m²/d: the results file calls it "GRAII mean, file 3", and I do not know whether it is the mean of A31E or of a wider area.
2. The WR2012 citation for the catchment rainfall (Bailey & Pitman, 2016). The rainfall values themselves are from the WR2012 table (`wr.xls`), which I opened.
3. The pre-1982 capacities (7.88 and 8.07 Mm³) and the cap of the area curve at 7.07 Mm³ are from the notes of Block 1 and are not in the Methods text; check against the workbook. The notes of Block 1 also give 14 and 20 years for the two periods, which I could not match to 1966–1974 plus 1981–1986 (15 years) and 1987–2009 (23 years), so I left the numbers of years out.
4. The 20.7 mS/m (n = 87) of Kromellenboog Dam in 2012–2023: the raw extract is not in the package. The Methods now state it as an input of the check, which makes the gap visible.
5. The primary DRASTIC source (DWAF, 2005, cited by Esterhuyse, 2017) is not in the reference list. The sentence cites it as the Results do.
6. Citation pages: the literature check found that Pollock (2016) fits pages 2–6 and Aller et al. (1987) page 12 better than the pages cited elsewhere in the article (2–3 and 13). Neither citation appears in the Methods text I read (Pollock is cited without a page in 5.3.2), so check where the pages are given.

**Decisions for you**
1. Whether to keep the 1:50-year reason sentence in 5.4.3.
2. Whether the mixing check stays in the Results or only in the Methods (open point 1 of the Results notes).
3. "Lower bound" in 5.4.1: change to "the reliability with the rule", as proposed, or keep the word with the explanation.
4. Table 5 caption: "hydrological years 1937–2009" against the runs of 1936–2009. The results file says that the change of the Atlas was taken against the mean of the water-balance record 1937–2009 and the elasticity from 1936–2009. Which period do you want in the caption? I did not change it.
5. Limits of the flood model (no calibration, boundary contact on the north side in 25 cells, SRTM terrain error): in 5.4.3, next to Table 11, or only in the Discussion.
6. Table numbers: the new flood Table 5 shifts every later table by one. This is best done once, when all blocks are in.

**What I did not change**
- 5.1.1, the data tables (Tables 1 to 4), 5.3.1, 5.3.4 and the paragraph on sensitivity (lines 1154–1156). They agree with the Results as drafted.
- Section 5 intro (lines 683–689): it says "water balance uses monthly records" and needs no change.

**Not from Methods, but in the same files** (author or later step)
- Study Area 2.4: where the dolomite and the Paardenvallei eyes lie relative to the dam; the share of the dolomite in the catchment at F2 (629.6 km², 46.4%) goes there, as does the rainfall of 597 mm and the series mean of 599 mm.
- Conclusions: header note still says "five supporting questions".
- Abstract: rewrite after the Conclusions are approved.
