**SUPERSEDED on 9 November (21:40): the Midgley and Pitman run stays at 889 m³/s (597 mm); use `Results_plain_v3_climate_flood_pathways.md` for 6.6 to 6.8.**

# Results 6.6 to 6.8 (climate, flood, pathways and water quality), plain style, version 4

Draft for approval. Not in the article. Version 4 changes only the Midgley and Pitman figures of 6.7 (mean annual rainfall of 563 mm instead of 597 mm; see `Methods_flood_SDF_v4.md`); everything else is as in version 3. Version 3 replaced `Results_plain_v2_climate_flood_pathways.md` after the panel of 9 November (surface water, groundwater, flood, water quality, citations, editor). The tables, figures and maps are unchanged except where the notes say so. The text now gives the pattern and a few figures; the tables carry the rest. Causes and interpretations are left to the Discussion.

---

## 6.6 Climate change

The two climate cases of Table 5 were applied to the water balance of the dam and to the groundwater model, to test how sensitive the canal supply and the groundwater are to a drier climate. Case M is the median step and case D the dry end of the projections. The reliability of the canal supply is measured against the registered volume raised by the demand factor of the case (Section 5.4.4). Table 10 gives the results against the Reference run.

The reliability by time falls in each step, with and without the rule, and the mean shortfall and the longest event grow. With the rule, the reliability by time falls from 0.59 in the Reference run to 0.54 in case M and 0.48 in case D. In case M the dam delivers about as much water as in the Reference run (1.89 against 1.86 Mm³/a with the rule), so its lower reliability is against a larger demand. In case D it delivers less (1.79 Mm³/a). With the rule, the months with less than half of the registered volume increase from 156 in the Reference run to 214 in case D.

**Table 10: The climate cases against the Reference run.** Canal supply: with the restriction rule / without restriction, hydrological years 1936–2009, against the registered volume raised by the demand factor of the case. Groundwater: discharge to rivers and streams in the base case (Mm³/a) and its change under the recharge factor of the case.

| Case | Reliability by time | Yearly reliability | Mean shortfall (Mm³/a) | Longest event (months) | Groundwater to rivers, S | Groundwater to rivers, D |
| --- | --- | --- | --- | --- | --- | --- |
| Reference | 0.590 / 0.867 | 0.446 / 0.770 | 0.48 / 0.27 | 146 / 20 | 9.86 Mm³/a | 0.63 Mm³/a |
| M (median) | 0.541 / 0.829 | 0.405 / 0.703 | 0.60 / 0.36 | 148 / 35 | −3.8% | −5% |
| D (dry end) | 0.477 / 0.791 | 0.324 / 0.635 | 0.70 / 0.44 | 163 / 35 | −10.5% | −14% |

The simulated storage is never higher than in the Reference run, and it is lower at every level in Figure 14. With the rule, the dam holds at least half of its capacity in about 64% of the months in the Reference run, in about 59% in case M and in about 53% in case D.

**Figure 14** (unchanged): Share of months in which the simulated storage of Klein Maricopoort Dam is at or above each level, for the Reference run and cases M and D, hydrological years 1936–2009. Left panel: with the restriction rule; right panel: without restriction.

In the groundwater model, the discharge to the rivers and streams falls by about the same percentage as the recharge: by 3.8% and 10.5% in structure S and by 5% and 14% in structure D (Table 10). Map 7 shows how much lower the water table stands in case D than in the Reference run, from two runs that both include an abstraction of 0.5 Mm³/a under the irrigated land. In structure S the mean lowering is 1.00 m, and it is largest on the high ground between the valleys. Under the pumped cells it averages 0.23 m. In structure D the mean lowering is 0.38 m, and under the pumped cells it averages 3.78 m, which equals the increase in the drawdown of the abstraction there, from 20.6 to 24.3 m (from 2.30 to 2.42 m in structure S). These drawdowns are means of 200 m model cells. Under case M the lowering is about a third of that under case D.

---

## 6.7 Flood extent and depth in the modelled reach

The design flood at F2 was estimated with three methods (Section 5.4.3), and four model runs were routed through the 15.7 km reach, to find how large the floods are and how much of the cultivated land they cover.

At the 1:100-year return period the SDF gives a peak of 1 252 m³/s and the Midgley and Pitman formula 839 m³/s, which is 67% of the SDF peak, so the SDF peak is 49% higher. The SDF peak also exceeds the RMF of region K3 and is about half that of region K4 (Table 11).

**Table 11: Design flood peaks at F2 and the floods routed through the modelled reach** (catchment about 1 357 km²; model area 24.3 km², with 8.04 km² of land mapped as cultivated; DFFE, 2024). RMF (no return period): 1 205 m³/s for region K3 and 2 355 m³/s for region K4.

| Run | Design peak (m³/s) | Peak in / out (m³/s) | Peak reduced | Flooded (km²) | Deeper than 1 m (km²) | Cultivated land flooded (km²) |
| --- | --- | --- | --- | --- | --- | --- |
| 1:50, SDF | 974 | 972 / 951 | 2.1% | 7.72 | 6.26 | 3.17 |
| 1:100, SDF | 1 252 | 1 250 / 1 236 | 1.1% | 7.97 | 6.66 | 3.24 |
| 1:100, Midgley and Pitman | 839 | [rerun] | [rerun] | [rerun] | [rerun] | [rerun] |
| 1:100, SDF, shallow-water equations | 1 252 | 1 250 / 1 234 | 1.3% | 8.34 | 7.01 | 3.33 |

Over the reach the peak decreases by 1% to 3% and arrives about two hours later. At the time of the peak the model area holds 14% to 16% of the flood volume. The flooded area changes much less than the peak. The 1:100-year SDF peak is 29% larger than the 1:50-year peak, but it floods 3% more land, and the Midgley and Pitman flood has a peak 33% lower than the SDF flood and covers [rerun: was 5%] less land. The outlines of the 1:50-year and 1:100-year SDF floods almost coincide on Map 9. The 1:100-year flood covers 0.25 km² more land, equal to a strip about 8 m wide along each side of the 15.7 km reach. The shallow-water solver, instead of the diffusion-wave solver, increases the flooded area by 5% and changes the outflow peak by 0.2%.

In every run 3.1 to 3.3 km² of land mapped as cultivated is flooded, and most of it lies under more than 1 m of water. About 44 ha (42 to 46 ha across the runs) of the 165 ha of land mapped as irrigated is flooded in the 1:100-year SDF flood, and 38 ha of it lies deeper than 1 m.

**Map 9** (unchanged): Maximum depth of the 1:100-year flood (SDF method) in the modelled reach of the Klein Marico River, from the HEC-RAS 2D model, with the outline of the 1:50-year flood. Hatching shows land mapped as irrigated; the inset shows the irrigated land in more detail. Depth classes 0.01–0.5, 0.5–1, 1–2, 2–4 and >4 m.

---

## 6.8 Pathways and the two waters

Two things were examined. Particles were released from the 45 model cells under the irrigated land in the runs without abstraction and tracked forward in both model structures (MODPATH; Pollock, 2016), to see where water that recharges under the fields goes. The records of the Department of Water and Sanitation (DWS) were screened against the guidelines of DWAF (1996a, 1996b) to compare the water of the river below Klein Maricopoort Dam with the water generated inside A31E.

In structure S, 387 of the 405 particles (96%) end in a cell where a river drain discharges (Map 10). The median time to reach the river is about 140 years at an effective porosity of 0.10, and it scales with the porosity. In structure D no particle reaches a river or stream, and 288 of the 405 do not leave the cell in which they started. The water table under the fields stands 15.3 m deep in this structure (Map 8).

**Map 10** (unchanged): Flow paths of 405 particles released in the 45 model cells under the irrigated land (MODPATH 7; Pollock, 2016), for (a) structure S and (b) structure D. Yellow dots mark the end of each path. In S, 387 of the 405 paths end at a river; in D none do. The paths show advective flow direction only; contaminant transport is not modelled, and travel times depend on an assumed porosity.

The water-quality records are in Figure 15 and Table 12. Below Klein Maricopoort Dam the median electrical conductivity (EC) was 51.2 mS/m in 1989–1993 (station A3H030, 56 samples) and 62.3 mS/m in 2012–2023 (A3H042Q01, 81 samples), and 86% and 99% of the samples exceeded the upper limit of the target range for irrigation, 40 mS/m. Three sites along the river between the dams (188257, 188038 and 188030; three, three and one samples, 2004–2007) had medians of 76 to 83 mS/m. The Wilgeboomspruit, the one gauged stream inside A31E (1971–1991), had a median of 3.85 mS/m and no exceedance. The groundwater of A31E had a median of 17.7 mS/m in seven samples (DWS, 2021:163), and Kromellenboog Dam, which receives both waters, 21.7 mS/m (1966–2023, 248 samples). Sulphate follows the same order, with medians of 30 to 57 mg/L below Klein Maricopoort Dam and 102 to 145 mg/L along the river between the dams, against 17.7 mg/L in Kromellenboog Dam and 3.05 mg/L in the Wilgeboomspruit. No sample at any site exceeds the guidelines for chloride, sodium or SAR.

**Figure 15** (unchanged) and **Table 12** (unchanged), as in the current article.

Over the common period of 2012–2023 the river below Klein Maricopoort Dam had a median EC of 62.3 mS/m and Kromellenboog Dam 20.7 mS/m. Water from Klein Maricopoort Dam made up 19% of the inflow to Kromellenboog Dam in 1987–2009 (Table 7). If that share applied in 2012–2023, a simple mixing calculation leaves an EC of about 11 mS/m for the other 81% of the inflow, which is the water from the catchment between the dams. Phosphate-P exceeds 0.025 mg/L, the boundary of a trophic class, in 19% of the samples at A3H042Q01 (74 samples), 4% at A3H030, 29% in Kromellenboog Dam (230 samples) and 20% in the Wilgeboomspruit (41 samples), so the nutrients do not separate the two waters in the same way.

The DRASTIC index was taken from the national map to rate how vulnerable the aquifer is to contamination from the surface. It is low over 96.7% of A31E and moderate over 3.3% (Map 11; DWAF, cited by Esterhuyse, 2017).

---

## Notes for the author (not article text)

**Flood review (applied above)**
- Retitled "Flood extent and depth", because 6.7 reports depth and extent, not risk. The cause of the small attenuation ("because the floodplain holds") is out: the 14% to 16% reproduces (15.6, 13.7, 16.2 and 15.3% from the water in the model area at the peak and the hydrograph volumes), but the stored water includes the channel, and the main reason for the small attenuation is more likely the 16.5 h rise against a travel time of about 2 h; that is for the Discussion if you want it.
- The "8 m" is now "a strip about 8 m wide along each side" (0.254 km² / 15.7 km / 2 = 8.1 m). It is an average: 278 whole mesh cells switch to wet, and measured along the stepped outline the mean shift is about 4.5 m. The bracket "42 to 46 ha" is now next to the 44 ha (the >1 m area ranges over 34 to 40 ha).
- Correction to my notes of version 2: the 6.26 / 6.66 / 6.10 in Table 11 are exactly the areas with depth class 3 and 4 (6.262, 6.662, 6.103, 7.011 km²), not rounded differences. Table 11 stands.
- 1:50 outflow: 972 / 951 gives 2.2% from the rounded values, and the table says 2.1% (from Update 24). The outflow hydrographs are not in the package, so I could not confirm 951.8. Check in your outflow file, or print 2.2%.
- Not reproducible here (outside this block): the cultivated land flooded (3.13 to 3.33 km²) and its base of 8.04 km²; the outflow peaks and delays. The reviewer found that the model also touches its northern boundary (25 cells, up to 3.2 m deep), that Manning's n is uncalibrated, that there is no flood mark or rating, and that the terrain is SRTM 30 m (February 2000); none of this is in 6.7. Say where the limits go (Methods, or one sentence next to Table 11). **The project context says "20 m DEM" for the flood model, but the Methods, Update 24 and the helper chat say SRTM 30 m; the project context is out of date.**
- "A31E itself contains none" (dolomite): the files show no dolomite for the Doringrivier (F3), not for the rest of A31E. Section 2.4 (Pretoria Group) is the source; confirm there when the sentence moves to the Study Area.

**What changed from version 2, and why** (each point is from the panel; I checked the ones marked "checked" myself)
- **6.6 target and delivery (checked, the most important change).** In cases M and D the demand is raised by 6.4%, and the reliability is measured against the raised volume. Reliability by time with the rule is the same against 2.34 Mm³/a, but the yearly reliability and the mean shortfall are not: against 2.34 they would be 0.473 / 0.716 (M) and 0.419 / 0.649 (D) for the yearly reliability and 0.53 / 0.34 (M) and 0.62 / 0.41 (D) for the mean shortfall, against 0.405 / 0.703, 0.324 / 0.635, 0.60 / 0.36 and 0.70 / 0.44 in Table 10. The mean delivery is 1.861 (Reference), 1.887 (M) and 1.793 (D) Mm³/a with the rule, and 2.067, 2.127 and 2.049 without restriction. In case M the dam delivers slightly more water than in the Reference run; the reliability falls because the demand rises. Version 2 said that supply "would be lost", which was wrong for M. The text now says so, and the Table 10 caption says what the reliability is measured against. Decision for you: keep the raised demand as the target (as in the Methods) or add the against-2.34 values as a check.
- **6.6 "projections".** Version 2 read as a forecast. The cases are sensitivity steps (project context), so the text says "to test how sensitive". "Median step" and "dry end" keep your labels M and D; the surface-water reviewer suggests "central" and "dry step" instead. Your decision.
- **6.6 numbers cut.** The derived ratios ("a quarter to a third", "a half to two-thirds", the 6-point comparison), the "about three of every four years" sentence and all but three figures of the first paragraph are out, because Table 10 carries them. The "a half to two-thirds" did not reproduce exactly either (+45% and +62%).
- **6.6 lowering (checked, error of version 2).** I had written "so the lowering shown is that of the drier climate alone". That is wrong in structure D: the comparison without wells shows 0.03 m under the fields (Update 24), so the 3.78 m under the pumped cells is the increase in the drawdown of the abstraction at the lower recharge (24.32 − 20.57 = 3.75 m). The text says that. The S values (2.30 to 2.42 m) are added so both structures have a figure. "In the valleys the drains hold the water table" is out (a model construct; it belongs to the Discussion if you want it). "Drawdown" is the effect of the abstraction and "lowering" the effect of the climate; define both once in Section 5.4.2.
- **6.6 discharge.** "Falls by about as much as the recharge" is "about the same percentage", because by volume the lost recharge goes mostly to the ground drain in S (46%) and in D (95%).
- **6.7.** The dolomite sentence is out (to the Study Area; the Discussion keeps one clause). "Differ widely", "plan" and "full shallow-water equations" are replaced. The causal "because" before the floodplain storage is out. The sentence that the 8 m is "less than a third of one 30 m cell" is out of the Results, because it is a statement about resolution; see the option for the Discussion in version 2. The "about 40%" is out because it rests on the 8.04 km², which could not be reproduced (the 8.04 km² stays, with DFFE, 2024, in the Table 11 caption). The new "0.28 m" sentence is not in the text: the editor advises against it. It is in `reviews/Flood_1in50_vs_1in100_and_SDF_inputs_2026-11-09.md` if you want it back.
- **6.8 particles.** The 3.9 km, the 537 m, the 90th percentile and the "months beside the river" are out. "About 140 years" carries the porosity, and a clause says that the time scales with it. The "because" for D is out of the Results. The first sentence says that the runs are without abstraction (the particle runs use the base models). The travel times in D are left out on purpose: they are very spread out (median 7 years, up to tens of thousands of years), which only shows that the water hardly moves. Say if you want them.
- **6.8 water quality.** The sentence "the two paths carry different water" is out; the Discussion says it. "The reach" is now "the river between the dams", so it is not confused with the 15.7 km flood reach. Stations and sample numbers are named, because the 86% to 99% and the 19% each belong to a station. **Error corrected:** the 11 mS/m is for the 81% of the inflow that does not come from the dam, and not "for the water of the reach", where the sites have 76 to 83 mS/m (water-quality reviewer; checked: (20.7 − 0.19 × 62.3) / 0.81 = 10.94). The text now says "the water from the catchment between the dams", and that the share is for 1987–2009. The phosphate shares name the stations, and "phosphate-P" is used.

**Open points for you**
1. **The 11 mS/m** is a rough check and very sensitive to the 19%: at 10%, 15%, 25% and 30% it would be 16.1, 13.4, 6.8 and 2.9 mS/m. The 81% also contains irrigation return flow of canal water (up to 1.23 Mm³/a, Table 15 of the approved text), which is dam water. Keep the check, or move it to the Methods and give only the result?
2. **The groundwater EC of 17.7 mS/m** and the "seven samples" (DWS, 2021:163): the Gazette PDF has no text layer, so neither the reviewer nor I could read page 163. It is **unverified**. I need a readable copy of the page, or your notes of the "file 15" source. The seven samples are not located, and the article says elsewhere that no groundwater quality record exists below the fields.
3. **The 20.7 mS/m (n = 87)** for Kromellenboog Dam in 2012–2023 is not in the screening file (only in Update 24); the raw extract ("file 12") is not in the package. Unverified.
4. **Sulphate along the river between the dams** (145 mg/L at 188257, 0.9 km below A3H042Q01, against 57 mg/L at the station) rises in a short distance; there are three samples and the periods differ. I did not explain it. Say if it should be reported as an open question.
5. **Citations (literature check, read through a summarising tool; confirm on the printed pages):** Pollock (2016) and Aller et al. (1987) support what they are cited for; the Methods cite Pollock at "2–3" and Aller at "13", and the pages that fit better are Pollock 2–6 and Aller 12 (and 20 for "relative"). DWAF (1996a:155, 48, 134, 144) and DWAF (1996b:84, 97) are supported, but check the printed footers (the contents list of the PDF has different page numbers). Michaluk & Keyser (1991) and Walraven (1981) could not be verified (maps; the catalogue spells "Mafekeng"); the 46.4% is your calculation from them and the geological workbook. The DRASTIC classes are in Esterhuyse (2017), but the 96.7% and 3.3% are your overlay, and the "1 km grid" of the Map 11 caption is not in Esterhuyse; the primary source is DWAF (2005, per Esterhuyse), which is not in the reference list.
6. **Particle travel times.** They scale with the porosity (unmeasured; 0.01 would make them ten times shorter) and with the conductivity (the four water levels do not fix it, so in the scaled pair they would double or halve). The text gives "about 140 years at 0.10, and it scales with the porosity"; a full range belongs in the Methods or the Discussion.
7. **The 15.3 m in D** is the depth of the ground drain in that structure (15.27 m) and so is built into the model, which is why particles stay in their cell. This is why the Discussion (version 6) no longer says the water table "stands below the river beds".
8. **Table 5** gives the base years as 1937–2009, while the runs and Table 10 use 1936–2009; align them.
9. **Workbook labels (not article text):** Run_A is titled "CASE A: +1 C, inflow −20%" but holds case M (0.93 / 1.064); Params labels A "+1 °C" and B "+2 °C", while Table 5 gives +1.9 °C for both; the RRV sheet's stored case A block is stale. The article uses the live values.
10. **"Longest event without restriction" (20 to 35 months in both M and D)** is a threshold effect: two Reference events (May 1988 to October 1989 and December 1989 to January 1991) merge into one when a month between them falls just below 99% of the volume. The figure is correct as defined; say so if a reader asks.

---

## Notes on version 4 (Midgley and Pitman at 563 mm)

- Changed in 6.7: the Midgley and Pitman peak (889 → 839 m³/s), its share of the SDF peak (71% → 67%), the SDF excess (41% → 49%) and the difference of the peaks in the paragraph after Table 11 (29% → 33% lower). All recomputed: 839 / 1 252 = 0.670; 1 252 / 839 = 1.492; 1 − 0.670 = 0.330.
- **Waiting for the HEC-RAS rerun** of the Q100_MP plan with `Q100_MP_hydrograph_MAP563.csv` (peak 839 m³/s, 15-minute values, 241 rows, floor 5 m³/s): the whole Midgley and Pitman row of Table 11 (peak in / out, reduction, flooded area, area deeper than 1 m, cultivated land), "covers [rerun] less land", and every range that includes this run: "decreases by 1% to 3%", "14% to 16%", "3.1 to 3.3 km²", "42 to 46 ha" and the 34 to 40 ha. Expect small changes only (the wet area moved by 0.37 km² for a 29% lower peak). Until the rerun the old Midgley and Pitman results (887 / 858 m³/s; 7.60 km²; 6.10 km² deeper than 1 m; 3.13 km² cultivated) belong to a peak of 889 m³/s and must not be printed against 839.
- If you prefer not to rerun, the alternative is to keep 889 m³/s (597 mm) and say that it is the rainfall of A31E alone; I do not recommend it, because the rainfall of the catchment at F2 is lower.
- The SDF rows, the RMF and the 1:50-year flood do not change. Map 9 shows the SDF floods and does not change either.
