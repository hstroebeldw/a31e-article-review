# Methods (Section 5): the fixes, version 2

Not in the article. Version 2 replaces `Methods_changes_v1.md` and `Methods_flood_SDF_v4.md`. It applies your answers of 9 November (21:28). Only what changed is given, in article order, each with its place. Text in plain paragraphs is article text. Lines beginning "Note:" are not.

The Midgley and Pitman check stays at 597 mm (see the note at the end), so the peaks of Results 6.7 (889 m³/s, 71%, 41%) stand, and `Results_plain_v3` is the current Results 6.6 to 6.8 (version 4 is dropped).

---

## 5.1.2 Groundwater (last paragraph, lines 838–843)

The mapped layers are the 1:250 000 geological maps (Michaluk & Keyser, 1991; Walraven, 1981), the 1:500 000 hydrogeological map with its borehole-yield classes (Barnard, 1999), the hydrological soil groups (Schulze & Schütte, 2023) and the national land cover of 2022 (DFFE, 2024). The regional transmissivity, storativity, thickness and recharge are those of the GRAII (DWS, s.a.a; Section 2.4), and the Reserve determination gives the recharge, use and baseflow of A31E (DWS, 2021). The vulnerability of the aquifer is taken from the national DRASTIC map (DWAF, cited by Esterhuyse, 2017).

Note: new sentence on DRASTIC, because Results 6.8 uses it. The 22.81 m²/d is already in Section 2.4.

## 5.1.3 Flood (last sentence, lines 851–852)

The regions of the Regional Maximum Flood are those of the drainage manual (SANRAL, 2013:3-65 to 3-67).

Note: Kovács is no longer cited (your decision: SANRAL only). Also change "(Kovács, 1988; SANRAL, 2013:3-65–3-67)" in 5.2.3 to "(SANRAL, 2013:3-65–3-67)".

## 5.1.4 Water quality and climate (replaces the sentences from "Path 1 is sampled" to the end of the paragraph, lines 868–873)

Path 1 is sampled below Klein Maricopoort Dam and at the three sites along the river between the dams, path 2 in the Wilgeboomspruit, and both paths in Kromellenboog Dam. The groundwater of A31E is represented by the median electrical conductivity of seven samples given in the Reserve determination (DWS, 2021:163). EC, which measures the dissolved salts, chloride, sodium, the sodium adsorption ratio (SAR), inorganic nitrogen and phosphate-P are screened against guideline values, and sulphate is reported as a median. The guideline values are the upper limits of the target range for irrigation and the boundaries of the trophic classes for aquatic ecosystems (DWAF, 1996a; DWAF, 1996b).

Note: "the three sites along the reach" becomes "the river between the dams" (so "reach" means only the 15.7 km flood reach). Sulphate has no guideline in the screening (Table 12 caption), so it cannot be "screened". The groundwater sentence is new; gazette p.163 is confirmed.

## 5.2.1 Dam water balance

*Replace the paragraph at lines 924–929:*

The inflow of each month is the remainder of the dam's own recorded balance. This remainder is available for 843 months. A further 27 months were rebuilt from the station records and 18 from the WR2012 patched flow, which gives the 888 months from October 1936 to September 2010. This is inflow series 1, and all results are for series 1 unless stated. Before 1987 a fixed release entry probably overstates the release when the dam was low, and a second, adjusted inflow series (series 2) was prepared for this period and run as a check.

*Add after "(Figure 2, lower panel)", line 937:*

The seasonal pattern of the canal volume in the forward test is that of Figure 3, and in the reverse test it is that of the months with the dam at 85% or more of its capacity in 1966–1974 and 1981–1986.

Note: the drought is already defined in Section 1.1 and is not repeated. Series 2 differs from series 1 from October 1966 to January 1987. The Table 8 caption in Results 6.3 ("the pattern of each test comes from the canal record of the years tested") must change to match: forward = Figure 3, reverse = the years tested.

## 5.2.2 Groundwater (second paragraph, lines 945–954)

The model removes water from every cell through a ground drain, which represents seepage, springs, evaporation and uptake by plants. Two depths of the ground drain are used, and they define the two structures of the model: structure S, with a shallow ground drain, and structure D, with a deep one. In structure S the ground drain lies 1 m below the land surface. In structure D it lies 15.27 m below the surface, which is the median depth to water of 112 archive levels in A31E and its neighbouring catchments (DWS, s.a.c). These 112 levels include the four calibration levels but none of the 262 levels that are later compared with the model. The depth of 15.27 m is also close to the mean maximum rooting depth of tropical grassland and savanna, 15.0 m (Canadell et al., 1996), although such uptake has not been shown in A31E.

Note: the last sentence of the old paragraph ("The base of the weathered zone is taken at 47.5 m") is cut here, because the model has one layer. The 47.5 m is explained once, in 5.4.2. From here on the text writes "structure D" and "case D" in full, never "D" alone.

## 5.2.4 Water quality and climate (replaces lines 997–1009)

The climate cases are expressed as factors that multiply the value of the Reference run, which is the water balance and the groundwater model with inflow series 1, the evaporation and demand of the records and the regional recharge. They are sensitivity steps and not forecasts. Case M represents the median of the projections for ESAF for 2041–2060 under intermediate emissions (SSP2-4.5). Case D represents their dry end, with the 10th percentile of the rainfall and the median warming, because the projected warming is narrow in range while the rainfall is uncertain even in sign (Section 3.3). The factors are given in Table 5.

*Table 5 caption:* "against hydrological years 1936–2009" (was 1937–2009).

*Sentence after the table (lines 1021–1023):* "Because the inflow stayed below its median from 1982 to 1994 although the rainfall of 1986–1995 was near its mean, this elasticity is an approximate scaling rather than a property of the catchments above the dam."

Note: the old sentence said that the low inflow "was not caused by low rainfall", which Results 6.2 contradicts (the rainfall was well below the mean in 1982–1985 and 1991). The later start of the rains is removed, as you asked. The result file gives the change against 1937–2009; 1936–2009 is your decision.

## 5.3.2 Groundwater (replaces the last two paragraphs, lines 1079–1084)

A31E has no water-level series for a transient model. The model is therefore run at steady state, in which the water entering the aquifer equals the water leaving it, and the cases are compared with one another. The residual of a borehole is its measured water level minus the simulated one, and the fit is expressed as the root-mean-square error of the residuals.

Particle tracking used MODPATH 7 (Pollock, 2016) in the base case of each structure. Nine particles were released at the water table in each of the 45 cells under the irrigated land, 405 in all, and tracked forward. The effective porosity was entered as 1.0 in every cell, and the travel times are scaled to a porosity of 0.10 afterwards.

Note: "no measured aquifer properties for analytical solutions (Leake & Barlow, 2013)" is cut. The fact sheet does not say it. "Weak sink" and the identical end points are cut.

## 5.3.3 Flood (last two sentences, lines 1097–1099)

The upstream boundary at F2 is the inflow hydrograph, with an energy slope from the terrain, and the downstream boundary is normal depth. The default diffusion-wave equations were used, and the full shallow-water equations as a check. The hydrographs have values every 15 minutes, with a minimum of 5 m³/s.

## 5.4.1 Dam water balance (one sentence, lines 1118–1119)

The test is independent only for the restriction rule, because the area curve, the pan factors and the release table were derived from the test period itself and the seasonal pattern comes from the canal record, and passing a split test is in any case "a necessary, rather than a sufficient, condition" for a model to be adequate (Klemeš, 1986:13).

Note: the rest of 5.4.1, including "lower bound" and "upper bound" with their explanation, stays as it is (your answer to 13).

## 5.4.2 Groundwater (replaces lines 1176–1189 and 1209–1220)

Abstraction was run at placement P1 at 0.25, 0.5, 1.0 and 2.34 Mm³/a in structure S and at 0.25, 0.5, 1.0, 2.0 and 2.34 Mm³/a in structure D. Placement P2 was run at 0.5 Mm³/a in both structures and at 2.34 Mm³/a in structure S, and placement P3 at 0.5 Mm³/a in structure S, to test whether spreading the abstraction changes the result. The recharge was also multiplied by the factors of cases M and D, 0.96 and 0.89, both without wells and with 0.5 Mm³/a at P1.

Four results are read from each case and compared with the base case at the same recharge. These are the rate actually pumped, because MODFLOW-NWT reduces the rate of a well when its cell nearly dries (Niswonger et al., 2011), the drawdown in the pumped cells, the number of pumped cells in which the water level falls below 47.5 m, which is the depth that the GRAII gives for the base of the weathered zone and is used here as a reference depth only, and the change in the outflow of each group of drains as a share of the rate pumped. The drawdown is the fall of the water table caused by the abstraction, and the lowering is the difference in the water table between two runs with the same abstraction, one at the base recharge and one at the reduced recharge. Both are means of 200 m model cells.

A steady-state drawdown is the state reached if pumping continued indefinitely at the mean recharge. It exceeds the drawdown of a single season of pumping at the same recharge, but it is not an upper limit for a long drought, during which the recharge falls below its mean. The loss of streamflow would in reality arrive later and continue after pumping stops (Section 3.2). Two further comparisons show what the four water levels cannot decide. In one, the recharge, the conductivities and the drain conductances are all halved or all doubled, which gives the same water levels and so fits the four levels equally well. In the other, structure D is run with the conductivities of structure S.

The particle times are those of the moving water alone, without dispersion, retention or decay. They scale in proportion to the effective porosity, which was not measured, and a porosity of 0.01 would make them ten times shorter than at 0.10.

Note: the count of runs ("27 of 74") and the list of runs not made are cut; the rates above are what Results 6.5 shows. "A reduction in the river or stream drains is water that would otherwise have flowed to Kromellenboog Dam" is cut (Discussion only). Map 7 and its caption move to Results 6.6 (your answer to 17). "Both structures are needed because the records contradict each of them (Section 6.4)" becomes: "Both structures are needed because four static water levels cannot identify a single conceptual model (Section 3.2)." The 47.5 m: the Section 2.4 thickness of the weathered zone (25.36 m) and the 47.5 m "depth of its base" both come from the GRAII and do not agree with each other; I only cite 47.5 m as the GRAII figure. Check this in the GRAII file if an examiner could ask.

## 5.2.3 and 5.4.3 Flood

*5.2.3, first sentence (line 973):* Flood extent and depth were modelled for the reach of the Klein Marico River below the Doringrivier, because the irrigated land lies along it.

*5.2.3, second and third paragraphs (lines 979–987): replace with the text and table below.*

The peak of the SDF was calculated in the steps of the drainage manual (SANRAL, 2013:3-44 to 3-47, 3B-2, 3B-3), with the inputs in the flood table below. The catchment at F2 lies in SDF basin 1. Its area, the length of its longest watercourse and the slope between 10% and 85% of that length were taken from the GIS. The design rainfall for the time of concentration was interpolated linearly between the modified Hershfield value for 6 h and the daily value of the basin station, Struan (SAWS 546 204), and reduced by the area reduction factor. The runoff coefficient for each return period follows from the coefficients of the basin for the 1:2-year and 1:100-year floods through the return-period factors. The Midgley and Pitman formula was applied as a check with the mean annual precipitation (MAP) of 597 mm (SANRAL, 2013:3-61, 3-62), and the RMF of Kovács regions K3 and K4, on whose boundary the catchment lies, was compared with the results (SANRAL, 2013:3-65–3-67). Each peak was given the triangular hydrograph that the manual prescribes for the SDF, which rises over one time of concentration and falls over two (SANRAL, 2013:3-45, 3-47).

**Flood table (new; numbering to be set at the end; it is not Table 5 of the climate cases): Inputs of the SDF and the Midgley and Pitman formula at F2.**

| Step | Quantity | Value |
| --- | --- | --- |
| 1 | SDF basin; station | 1; Struan (SAWS 546 204) |
| 2 | Catchment area, A | 1 357.26 km² |
| 3 | Longest watercourse, L | 94.12 km |
| 4 | Average slope between 10% and 85% of L, S | 0.00536 m/m |
| 5 | Time of concentration, Tc = (0.87 L² / (1000 S))^0.385, L in km | 16.44 h |
| 6 | Point rainfall for Tc, 1:50-year and 1:100-year (modified Hershfield at 6 h: 122.1 and 140.7 mm; daily value of Struan: 150 and 177 mm) | 138.3 and 161.8 mm |
| 7 | Area reduction factor | 84.4% |
| 8 | Runoff coefficient C2 and C100; C50 | 10% and 40%; 36.4% |
| 9 | Peak, Q = C I A / 3.6, with I = point rainfall × ARF / Tc | Table 11 |
| 10 | Midgley and Pitman, Q = 0.0377 K_T P A^0.6 C^0.2, with C = A √S / (L Lc); Lc = 27.38 km; K_T 0.79 and 1.00; P = 597 mm | Table 11 |

*5.4.3 (replaces lines 1228–1237):*

As the drainage manual requires, the SDF was used as the main estimate and compared with the other applicable methods (SANRAL, 2013:3-4). Because the manual warns that the flood of a dolomitic catchment may be less than half of the SDF (SANRAL, 2013:3-45), the SDF is treated as the conservative case. Four plans were run, namely the 1:50-year and 1:100-year SDF floods, the 1:100-year Midgley and Pitman flood, and the 1:100-year SDF flood with the full shallow-water equations as a check on the default diffusion-wave equations. Two simplifications act in opposite directions, since ignoring the attenuation in Klein Maricopoort Dam makes the flood larger, while leaving out the inflow of the Waterkloofspruit makes the flood below its junction smaller.

Note: the SDF stays the design flood (your answer 8c); Midgley and Pitman and the RMF are comparisons. The 1:50-year reason, the 0.28 m, the SRTM channel heights, the boundary contact and the land-cover classes are left out (your answers 8a, b, d, e). The sentence on calibration is also left out (your answer of 21:33). The peaks are not repeated in the flood table: Table 11 has them. "Kovács regions" in the flood text: the region names can stay, only the citation is SANRAL.

## 5.4.4 Water quality and climate (replaces lines 1245–1253)

Each water-quality quantity was compared with its guideline value, and the share of samples above the guideline was counted for each site. A value above a guideline shows that the water could affect its use or its ecosystem, but it does not show that the water is contaminated. The guideline defines the trophic classes for the average summer concentration, so the share of single samples above a boundary is a screening indication and not a trophic classification (DWAF, 1996b:84, 97).

The river below the upper dam (A3H042Q01) and Kromellenboog Dam were also compared over their common period, 2012–2023, with a simple mixing check. The check assumes that the water in Kromellenboog Dam is a mixture of the water from the upper dam, taken at the median EC of A3H042Q01, and of the water from the catchment between the dams, and that the share from the upper dam was the 19% found for 1987–2009 (5.01 of the 6.21 Mm³/a, Section 6.2). The EC of the water from the catchment between the dams then follows from the median EC of Kromellenboog Dam. The check treats the medians of single samples as flow-weighted values and ignores evaporation in Kromellenboog Dam, so it indicates an order of magnitude only.

In the climate cases, the dam was run with the inflow multiplied by 0.93 and 0.80 and evaporation and demand by 1.064. The canal is asked for the registered volume raised by the same factor, 2.49 Mm³/a, and the reliability is measured against this volume. The groundwater model was run with the recharge multiplied by 0.96 and 0.89 (Section 5.4.2).

Note: the value (about 11 mS/m), the two medians and the sample numbers are in Results 6.8 only (your answer 4). Results 6.8 and this paragraph must both say "Section 6.2", not "Table 7", for the 19%.

---

## What changed from version 1, in five lines

- Cut: the count of runs and the list of runs not made, the drought sentence, the "other spans" sentence, the later start of the rains, the 1:50 reason, the 0.28 m, the model limits (including calibration), the sentence on land-cover classes, the identical end points, the series 2 figures, the lost-water explanation in 5.4.1.
- Kept to fix an error in the existing text: the Table 5 sentence on the 1982–1994 inflow, "sulphate is screened", the independence sentence in 5.4.1, the Kovács citation, DWAF 1996b pages, the Leake & Barlow sentence.
- Added because the Results use it: DRASTIC and groundwater EC sources, the definition of structure S and D, drawdown and lowering, residual and RMS, the porosity of 1.0 and the scaling, the pattern of each test, the raised demand, the mixing check with its assumptions.

## About the Midgley and Pitman rainfall

You said the map is final and you will not rerun the Midgley and Pitman plan. The routed run used a hydrograph of 887 m³/s (the formula at 597 mm), and Table 11 shows its outputs. If I printed 839 m³/s (563 mm) in the same row, the table would show a peak in of 887 against a design peak of 839, which cannot be right, and I cannot correct the flooded areas without the run. So 597 mm and 889 m³/s stay, and the table stays as it is. The weakness is real and you accept it: 597 mm is the WR2012 rainfall of A31E alone, while the catchment at F2 is mostly A31C and A31D, where it is lower (about 563 mm over the whole catchment). If an examiner asks, the answer is that the Midgley and Pitman run is a check on the SDF, and that a lower rainfall would lower the check peak by about 6%. The flooded area would change very little, but that is my expectation from the other runs, not a result. The file `Q100_MP_hydrograph_MAP563.csv` is not used. If you want the 563 mm in the article after all, the only consistent way is to rerun that one plan.

---

## Added in the separate pass: the methods that the Results use (one sentence each)

These are only the sentences that the shortened Results 6.2–6.8 (version 6) still need. Methods that belonged to cut results (rank correlation, naturalised runoff, months below half the registered volume, volume held in the model area, irrigated land flooded, the Wilgeboomspruit) are not added.

**5.2.1 Dam water balance (after the paragraph on the inflow, line 929):**
The inflow to Kromellenboog Dam was calculated in the same way, as the remainder of its recorded balance (A3R003, A3H033), and the net contribution of the river between the dams is this inflow less the spill and release of Klein Maricopoort Dam.

**5.4.1 Dam water balance (after the sentence on the second inflow series, line 1124):**
The rule was also fitted on each period alone, to show how far the reliability depends on the period used.

**5.4.2 Groundwater (end of the paragraph at line 1189):**
The mean shortfall and the rate needed in the longest shortfall event were expressed as shares of the recharge of the Reserve determination and compared with the rates that the model could deliver.

**5.3.2 Groundwater (end of the particle paragraph):**
Each particle was classed by the drains of the cell in which it ended, and the time to the river is that of the particles that ended at a river drain.

**5.4.3 Flood (end of the paragraph):**
A cell of the mesh was counted as flooded where its maximum depth was at least 0.01 m. The peak reduction is the fall of the peak between the inflow at F2 and the outflow at the downstream boundary, and the delay is the time between the two peaks. The cultivated land flooded is the flooded area that lies on land mapped as cultivated in the national land cover (DFFE, 2024).

**5.4.4 Climate (end of the climate paragraph):**
The simulated storage of the cases was compared by the share of months in which it stood at or above each level.

Note: the sentences are from the way the Results and Table 11 are built, not from a method file. Please check three of them against what you did: that the particle times in 6.8 cover the 387 particles that ended at a river drain; that the flooded cells are those with a maximum depth of 0.01 m or more (the first depth class of Map 9); and that the delay is measured between the two peaks. The other four are plain statements of what the tables show.
