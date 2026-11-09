# Methods (Section 5): the fixes, version 3

Not in the article. Version 3 replaces `Methods_changes_v2.md`. It applies the author's answers of 9 November (22:55). Only what changed is given, in article order, each with its place. Plain paragraphs are article text. Lines beginning "Note:" are not.

The flood methods are the SDF only (answer 7). The Midgley and Pitman formula, the Regional Maximum Flood, the shallow-water check, the mixing check and the 47.5 m reference depth are out, and so are the sentences that only they needed.

---

## 5.1.1 Dam water balance (one sentence added to the data paragraph)

The national register of water use (DWS, s.a.f) records entitlements and not the actual abstraction.

## 5.1.2 Groundwater (last paragraph, lines 838–843; replaces the sentence "The regional transmissivity, storativity, thickness and recharge are those of the GRAII (DWS, s.a.a; Section 2.4), and …")

The mapped layers are the 1:250 000 geological maps (Michaluk & Keyser, 1991; Walraven, 1981), the 1:500 000 hydrogeological map with its borehole-yield classes (Barnard, 1999), the hydrological soil groups (Schulze & Schütte, 2023) and the national land cover of 2022 (DFFE, 2024), which is classified from satellite images. The Groundwater Resource Assessment II (GRAII) gives the following modelled regional values for A31E (DWS, s.a.a). Transmissivity, which is how easily the full thickness of an aquifer passes water, is 22.81 m²/d. Storativity, which is the water released per m² of aquifer when its level falls by 1 m, is 0.00998 in the weathered zone and 0.00014 in the fractured zone below it. The weathered zone is 25.36 m thick and the fractured zone 182.14 m, a total of 207.5 m. Recharge, which is the part of rainfall that reaches the groundwater, is 4.84% of rainfall, about 29 mm/a. The Reserve determination gives the recharge, use and baseflow of A31E (DWS, 2021). The vulnerability of the aquifer is taken from the national DRASTIC map (DWAF, cited by Esterhuyse, 2017).

Note: the GRAII paragraph is the old Section 2.4 text, unchanged (Study Area version 2 moved it here). "Section 2.4" no longer points to it, so Results 6.1 must say "Section 5.1.2" where it says "the modelled regional values of the GRAII (Section 2.4)".

## 5.1.3 Flood (last sentence, lines 851–852)

Delete the sentence "The regions of the Regional Maximum Flood are those of the drainage manual …". The Regional Maximum Flood is not used.

Note: Kovács (1988) is still cited in Section 3.4 (line 568), so it stays in the reference list.

## 5.1.4 Water quality and climate (replaces the sentences from "Path 1 is sampled" to the end of the paragraph, lines 868–873)

Path 1 is sampled below Klein Maricopoort Dam and at the three sites along the river between the dams, path 2 in the Wilgeboomspruit, and both paths in Kromellenboog Dam. The groundwater of A31E is represented by the median electrical conductivity of seven samples given in the Reserve determination (DWS, 2021:163). EC, which measures the dissolved salts, chloride, sodium, the sodium adsorption ratio (SAR), inorganic nitrogen and phosphate-P are screened against guideline values, and sulphate is reported as a median. The guideline values are the upper limits of the target range for irrigation, where the SAR of 2.0 is the value for the crop yield, and the boundaries of the trophic classes for aquatic ecosystems (DWAF, 1996a:134; DWAF, 1996b).

Note: "the river between the dams" replaces "the reach", so that "reach" means only the 15.7 km flood reach. The sentence on the SAR is the brief reason asked for in answer 20.

## 5.2.1 Dam water balance

*Replace the paragraph at lines 924–929:*

The inflow of each month is the remainder of the dam's own recorded balance. This remainder is available for 843 months. A further 27 months were rebuilt from the station records and 18 from the WR2012 patched flow, which gives the 888 months from October 1936 to September 2010. This is inflow series 1, and all results are for series 1 unless stated. Before 1987 the release entry of the dam record is a fixed value, and a second inflow series (series 2) that adjusts it was prepared for this period and run as a check. The inflow to Kromellenboog Dam was calculated in the same way, as the remainder of its recorded balance (A3R003, A3H033), and the net contribution of the river between the dams is this inflow less the spill and release of Klein Maricopoort Dam.

*Add after "(Figure 2, lower panel)", line 937:*

The seasonal pattern of the canal volume in the forward test is that of Figure 3, and in the reverse test it is that of the months with the dam at 85% or more of its capacity in 1966–1974 and 1981–1986.

Note: "probably overstates the release when the dam was low" is out (answer 5). The drought is defined in Section 1.1 and not repeated. Series 2 differs from series 1 from October 1966 to January 1987.

## 5.2.2 Groundwater (second paragraph, lines 945–954)

The model removes water from every cell through a ground drain, which represents seepage, springs, evaporation and uptake by plants. Two depths of the ground drain are used, and they define the two structures of the model: structure S, with a shallow ground drain, and structure D, with a deep one. In structure S the ground drain lies 1 m below the land surface. In structure D it lies 15.27 m below the surface, which is the median depth to water of 112 archive levels in A31E and its neighbouring catchments (DWS, s.a.c). These 112 levels include the four calibration levels but none of the 262 levels that are later compared with the model. The depth of 15.27 m is also close to the mean maximum rooting depth of tropical grassland and savanna, 15.0 m (Canadell et al., 1996).

Note: "although such uptake has not been shown in A31E" and the sentence on the base of the weathered zone at 47.5 m are out. From here on the text writes "structure D" and "case D" in full, never "D" alone. The recharge is the regional rate of 29.2 mm/a on every cell (line 957); no return flow of canal or irrigation water is added to it, and the result files say nothing about one.

## 5.2.3 Flood (first sentence and the second and third paragraphs, lines 973–987)

*First sentence:* Flood extent and depth were modelled for the reach of the Klein Marico River below the Doringrivier, because the irrigated land lies along it.

*Replace lines 979–987 with the text and table below.*

The peak of the SDF was calculated in the steps of the drainage manual (SANRAL, 2013:3-44 to 3-47, 3B-2, 3B-3), with the inputs in Table 5. The catchment at F2 lies in SDF basin 1. Its area, the length of its longest watercourse and the slope between 10% and 85% of that length were taken from the GIS. The design rainfall for the time of concentration was interpolated linearly between the modified Hershfield value for 6 h and the daily value of the basin station, Struan (SAWS 546 204), and reduced by the area reduction factor. The runoff coefficient for each return period follows from the coefficients of the basin for the 1:2-year and 1:100-year floods through the return-period factors. Each peak was given the triangular hydrograph that the manual prescribes for the SDF, which rises over one time of concentration and falls over two (SANRAL, 2013:3-45, 3-47).

**Table 5 (new): Inputs of the SDF at F2.**

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
| 9 | Peak, Q = C I A / 3.6, with I = point rainfall × ARF / Tc | Table 14 |

Note: the Midgley and Pitman step (old step 10), its rainfall of 597 mm and the Regional Maximum Flood are out. In the article these were the second and third paragraphs of 5.2.3 (lines 979–987); check that no sentence about them is left.

## 5.2.4 Water quality and climate (replaces lines 997–1009)

The climate cases are expressed as factors that multiply the value of the Reference run, which is the water balance and the groundwater model with inflow series 1, the evaporation and demand of the records and the regional recharge. They are sensitivity steps for about 2050 and not forecasts. Case M represents the median of the projections for ESAF for 2041–2060 under intermediate emissions (SSP2-4.5). Case D represents their dry end, with the 10th percentile of the rainfall and the median warming, because the projected warming is narrow in range while the rainfall is uncertain even in sign (Section 3.3). The factors are given in Table 6.

*Table 6 caption:* unchanged, "against hydrological years 1937–2009" (answer 17).

*Sentence after the table (lines 1021–1023):* "Because the inflow stayed below its median from 1982 to 1994 although the rainfall was above its mean from 1987 to 1990, this elasticity is an approximate scaling rather than a property of the catchments above the dam."

Note: the old sentence said that the low inflow "was not caused by low rainfall", which Results 6.2 contradicts. The later start of the rains is removed (also from article Section 3.3, lines 538 ff.; see the reference file).

## 5.3.2 Groundwater (replaces the last two paragraphs, lines 1079–1084)

A31E has no water-level series for a transient model, so the model is run at steady state, in which the water entering the aquifer equals the water leaving it, and the cases are compared with one another. The residual of a borehole is its measured water level minus the simulated one, and the fit is expressed as the root-mean-square error of the residuals.

Particle tracking used MODPATH 7 (Pollock, 2016) in the base case of each structure. Nine particles were released at the water table in each of the 45 cells under the irrigated land, 405 in all, and tracked forward. The effective porosity was entered as 1.0 in every cell, and the travel times are scaled to a porosity of 0.10 afterwards. Each particle was classed by the drains of the cell in which it ended.

## 5.3.3 Flood (last two sentences, lines 1097–1099)

The upstream boundary at F2 is the inflow hydrograph, with an energy slope from the terrain, and the downstream boundary is normal depth. The default diffusion-wave equations were used. The hydrographs have values every 15 minutes, with a minimum of 5 m³/s.

## 5.4.1 Dam water balance

*Replace the sentence at lines 1118–1121:*

The test is independent only for the restriction rule and the demand, because the area curve, the pan factors and the release table were derived from the test period itself, and passing a split test is in any case "a necessary, rather than a sufficient, condition" for a model to be adequate (Klemeš, 1986:13).

*Add after the sentence on the second inflow series (line 1124):*

The rule was also fitted on each period alone, to show how far the reliability depends on the period used. In the reverse test the rule was fitted on 1987–2009 and tested on 1966–1974 and 1981–1986, with the storage at the start of each period taken from the record, and the same three criteria were applied to the 178 months and the 14 years with a counted canal volume.

Note: the Klemeš sentence is the current article text, shortened by "and the demand" being kept as in the article. I did not open Klemeš (1986) myself, so the page 13 is unverified; if you prefer, the clause after "in any case" can go, and Klemeš (1986) then leaves the reference list (it is cited only here, line 1121). The rest of 5.4.1, including "lower bound" and "upper bound" with their explanation, stays as it is. The reverse-test numbers are the rerun of 9 November with the scripts in `drafts/rerun_scripts/` (rule 2, seasonal pattern 2, series 1); the earlier numbers in the project context (0.53, 0.34, 154 months, 12 years) came from a different selection of months and are not used.

## 5.4.2 Groundwater (replaces lines 1176–1189 and 1209–1220)

Abstraction was run at placement P1 at 0.25, 0.5, 1.0 and 2.34 Mm³/a in structure S and at 0.25, 0.5, 1.0, 2.0 and 2.34 Mm³/a in structure D. Placement P2 was run at 0.5 Mm³/a in both structures and at 2.34 Mm³/a in structure S, and placement P3 at 0.5 Mm³/a in structure S, to test whether spreading the abstraction changes the result. The recharge was also multiplied by the factors of cases M and D, 0.96 and 0.89, both without wells and with 0.5 Mm³/a at P1.

Three results are read from each case and compared with the base case at the same recharge. These are the rate actually pumped, because MODFLOW-NWT reduces the rate of a well when its cell nearly dries (Niswonger et al., 2011), the drawdown in the pumped cells, and the change in the outflow of each group of drains as a share of the rate pumped. The drawdown is the fall of the water table caused by the abstraction, and the lowering is the difference in the water table between two runs with the same abstraction, one at the base recharge and one at the reduced recharge. Both are means of 200 m model cells.

A steady-state drawdown is the state reached if pumping continued indefinitely at the mean recharge. It exceeds the drawdown of a single season of pumping at the same recharge, and during a long drought, when the recharge falls below its mean, it would be larger. The loss of streamflow would in reality arrive later and continue after pumping stops (Section 3.2). Two further comparisons show what the four water levels cannot decide. In one, the recharge, the conductivities and the drain conductances are all halved or all doubled, which gives the same water levels and so fits the four levels equally well. In the other, structure D is run with the conductivities of structure S. The mean shortfall and the rate needed in the longest shortfall event were expressed as shares of the recharge of the Reserve determination and compared with the rates that the model could deliver.

The particle times are those of the moving water alone, without dispersion, retention or decay. They scale in proportion to the effective porosity, which was not measured, and a porosity of 0.01 would make them ten times shorter than at 0.10.

Note: the count of runs, the list of runs not made and the 47.5 m reference depth are out (answer 18). "Both structures are needed because the records contradict each of them (Section 6.4)" becomes "Both structures are needed because four static water levels cannot identify a single conceptual model (Section 3.2)." Map 7 and its caption move to Results 6.6 and are renumbered Map 8 (see the reference file).

## 5.4.3 Flood (replaces lines 1228–1237)

The design flood was estimated with the SDF method of the drainage manual (SANRAL, 2013). Two plans were run, the 1:50-year and the 1:100-year flood. Two simplifications act in opposite directions, since ignoring the attenuation in Klein Maricopoort Dam makes the flood larger, while leaving out the inflow of the Waterkloofspruit makes the flood below its junction smaller. A cell of the mesh was counted as flooded where its maximum depth was at least 0.01 m. The peak reduction is the fall of the peak between the inflow at F2 and the outflow at the downstream boundary, and the delay is the time between the two peaks. The irrigated land flooded is the area of land mapped as irrigated (DFFE, 2024) that lies in the flooded cells, calculated in a GIS.

Note: the depth of a cell is the maximum water surface minus the lowest elevation of the cell (README of the flood folder). The irrigated layer is in the Africa Albers projection and was reprojected to UTM 35S before the overlay. The dolomite warning of the manual, the comparison with the other methods and the shallow-water check are out.

## 5.4.4 Water quality and climate (replaces lines 1245–1253)

Each water-quality quantity was compared with its guideline value, and the share of samples above the guideline was counted for each site. A value above a guideline shows that the water could affect its use or its ecosystem, but it does not show that the water is contaminated. The guideline defines the trophic classes for the average summer concentration, so the share of single samples above a boundary is a screening indication and not a trophic classification (DWAF, 1996b:84, 97).

In the climate cases, the dam was run with the inflow multiplied by 0.93 and 0.80 and evaporation and demand by 1.064. The canal is asked for the registered volume raised by the same factor, 2.49 Mm³/a, and the reliability is measured against this volume. The groundwater model was run with the recharge multiplied by 0.96 and 0.89 (Section 5.4.2). The simulated storage of the cases was compared by the share of months in which it stood at or above each level.

Note: the mixing-check paragraph is out (answer 9).

---

## What changed from version 2, in six lines

- Out: Midgley and Pitman (formula, 597 mm, step 10), the Regional Maximum Flood, the shallow-water check, the dolomite warning, the mixing check and its assumptions, the 47.5 m reference depth, "such uptake has not been shown", "probably overstates the release".
- Changed: Table 5 is the SDF only (nine steps); 5.4.3 has two plans; Results 6.7 follows.
- Added: the register sentence (5.1.1), the GRAII values (5.1.2, moved from the Study Area), the SAR reason (5.1.4), the two reverse-test sentences (5.4.1), the irrigated land flooded (5.4.3).
- Climate-table caption stays at 1937–2009 (answer 17).
- Unverified and left to you: the page of Klemeš (1986), the pages of DWAF (2004) in the Discussion.
