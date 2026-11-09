# Methods, flood: the SDF calculation, version 2 (Section 5.2.3, with a new table)

Draft for approval. Not in the article. It replaces `Methods_flood_SDF_v1.md` after the flood-hydrologist review of 9 November. Each correction was recomputed first (see the notes). Your friend shows the steps and a table of the SDF inputs and results, and I recommend that A31E does the same: the SDF is the main flood estimate, and the supervisor asked that the Methods show what was done and why.

---

## 5.2.3 Flood (replaces the second paragraph; the first paragraph and the others stay)

The peak of the SDF was calculated in the steps of the drainage manual, with the inputs in Table 5 (SANRAL, 2013:3-44 to 3-47, 3B-2). The catchment at F2 lies in SDF basin 1. Its area, the length of its longest watercourse and the slope between 10% and 85% of that length were taken from the GIS. The time of concentration follows from the length and the slope. The design rainfall for the time of concentration was interpolated between the modified Hershfield value for 6 h and the daily value of the basin station, Struan (SAWS 546 204), and was reduced by the area reduction factor. The runoff coefficient for each return period follows from the coefficients of the basin for the 1:2-year and 1:100-year floods through the return-period factors (SANRAL, 2013:3-46). The Midgley and Pitman formula was applied as a check, with the inputs in Table 5 (SANRAL, 2013:3-61, 3-62), and the RMF was applied as an upper limit for Kovács regions K3 and K4, on whose boundary the catchment lies (Kovács, 1988; SANRAL, 2013:3-65–3-67). The SDF method prescribes a triangular hydrograph that rises over one time of concentration and falls over two (SANRAL, 2013:3-45, 3-47), and the same shape was used for the Midgley and Pitman peak. The hydrographs have values every 15 minutes, with a minimum of 5 m³/s.

**Table 5 (new): Inputs and steps of the SDF and the Midgley and Pitman formula at F2 (SANRAL, 2013:3-44 to 3-47, 3-61, 3-62, 3B-2).**

| Step | Quantity | Value |
| --- | --- | --- |
| 1 | SDF basin; station | 1; Struan (SAWS 546 204) |
| 2 | Catchment area, A | 1 357.26 km² |
| 3 | Longest watercourse, L | 94.12 km |
| 4 | Average slope between 10% and 85% of L, S | 0.00536 m/m (5.36 m/km; 1 155 m and 1 533 m) |
| 5 | Time of concentration, Tc = (0.87 L² / (1000 S))^0.385, L in km and S in m/m | 16.44 h |
| 6 | Point rainfall for Tc, 1:100-year | 161.8 mm |
| 7 | Area reduction factor, ARF | 84.4% |
| 8 | Runoff coefficient, C2 and C100; C50 | 10% and 40%; 36.4% |
| 9 | Peak, Q = C I A / 3.6, with I = point rainfall × ARF / Tc | 1:50-year 974 m³/s; 1:100-year 1 252 m³/s |
| 10 | Hydrograph: rise Tc, fall 2 Tc, 15-minute values, minimum 5 m³/s | Peaks sampled: 972, 1 250 m³/s |
| 11 | Midgley and Pitman, Q = 0.0377 K_T P A^0.6 C^0.2, with C = A √S / (L Lc) = 0.0386 (Lc = 27.38 km, measured along the main watercourse from the outlet to the point nearest the centroid of the catchment; K_T 0.79 and 1.00 for the Bushveld; P = 597 mm) | 1:50-year 703 m³/s; 1:100-year 889 m³/s |

---

## Notes for the author (not article text)

**Corrections made after the flood-hydrologist review (each one recomputed in code)**
- **Units in step 5.** In version 1 the formula was printed with S = 5.36 m/km. Putting 5.36 into the formula as printed gives 1.15 h. The manual takes S in m/m (SANRAL, 2013:3-46, Eq. 3.17), so the factor 1000 turns it into m/km. With S = 0.00536 the formula gives 16.43 h (16.44 h with the unrounded slope 5.355 m/km). Step 4 now gives S in m/m, and the units are in the row for step 5.
- **Midgley and Pitman reproduces. My note in version 1 was wrong.** I used C = A S / (L Lc), which gives 527 m³/s, and I also left out the exponents of the formula in my check. The printed equation in the text file has lost its radical (it prints "Α S" over "L LC"). With C = A √S / (L Lc) = 0.0386 and the formula Q = 0.0377 K_T P A^0.6 C^0.2, I recomputed 373.6, 507.0, 702.7 and 889.5 m³/s for the 1:10, 1:20, 1:50 and 1:100-year floods, against 374, 507, 703 and 889 in your results file. This closes the "889 m³/s cannot be reproduced" problem in the project context, **provided the printed equation has the root of S**. I could not confirm this from the printed page or an outside source (the Midgley 1972 report that the reviewer opened does not contain the equation). Please check Equation 3.35 on the printed page. If it has the root, step 11 stands. If not, delete step 11.
- **The hydrograph.** The peaks of 972.2, 1 249.7 and 887.4 m³/s in Update 24 are not "the design peak minus 5 m³/s". The series is the triangle, sampled every 15 minutes, with a floor of 5 m³/s. The grid misses the apex by 0.06 h (16.5 h against 16.44 h), so the sampled peak is about 0.2% below the design peak (974 × (1 − 0.06/32.88) = 972.2). The "base flow 5 m³/s" in Update 24 is a floor at the two ends and not a flow added on top. I read the workbook (`design_hydrographs_15min.xlsx`) to check the maxima.
- **Citations.** Version 1 dropped pages 3-44 (the basin map) and 3B-2 (Table 3B.1, the coefficients and the station). They are back. The station and its coefficients are in Table 3B.1: basin 1, Struan, SAWS 546 204, M 56 mm, R 30 days, C2 10%, C100 40% (text file, line 7554).
- **The hydrograph shape.** The manual prescribes the triangle for the SDF only. Using it for the Midgley and Pitman peak is your choice, so the paragraph now says so.
- **The runoff coefficient.** C50 = 0.10 + 2.05 × (0.40 − 0.10) / 2.33 = 0.364, with the return-period factors of Table 3.13 (2.05 for 1:50 and 2.33 for 1:100).

**Recomputed with code** (SANRAL, 2013:3-46, in the text file in the repository): Tc 16.43 h; ARF = 84.4%; Q100 = 0.40 × (161.8 × 0.844 / 16.44) × 1 357.26 / 3.6 = 1 253 m³/s (the files give 1 252; rounding). Not recomputable: the point rainfall of 161.8 mm itself, because the daily values of the station (Table 3B.2) are an image in the text file.

**Gaps you must close** (I did not fill them)
1. **The 1:50-year point rainfall.** It is not in the files. The 974 m³/s implies about 138 mm. Add the value from your workings, or drop "1:50-year" from step 9.
2. **The interpolation (new text in the paragraph; and where the rainfall values are).** The helper chats do not contain the point rainfall: chat 6 says the Design Rainfall program was not needed because Struan is representative, and the 161.8 mm and the 1:50-year value were computed in the helper's own workings, which were not saved in the files or the chats. So the 1:50-year rainfall remains open (gap 1). The manual says that for a time of concentration between 6 and 24 hours the point rainfall is interpolated between the modified Hershfield value and the daily value of the station (Step 6). The sentence now says so. Please confirm that this is what you did. The implied daily values at Struan that fit all six of your peaks are a smooth series (about 56, 80, 99, 119, 150 and 177 mm for 1:2 to 1:100), which suggests that they are the values of Table 3B.2, but I could not read that table.
3. **The MAP of 597 mm (checked in the helper chats and the WR2012 table).** The helper chat chose 597 mm; it asked you for the MAP of A31C and A31D and the chats do not show that you supplied it. 597 mm is the WR2012 MAP of A31E alone (602 km²). The same WR2012 table gives 546 mm for A31C (486 km²) and 566 mm for A31D (705 km²), and the manual's Table 3B.1 gives 550 mm for the SDF basin 1. The F2 catchment (1 357 km²) is mostly A31C and A31D, so 597 mm is high for it. Weighting the three quaternary MAPs by area (the 166 km² above 1 191 km² taken as A31E; an estimate, since the GIS split is not in the files) gives about 563 mm, and the Midgley and Pitman peaks fall in proportion: 1:50-year 662 m³/s (from 703) and 1:100-year 838 m³/s (from 889), 6% lower. The effect on Section 6.7 is small (the check method falls from about 29% to about 33% below the SDF), but the number changes. Decide which MAP is defensible and say where it comes from; until then step 11 keeps 597 mm, as in your results.
4. **The GIS inputs (answered in part by the helper chats).** The elevation model was the SRTM 30 m model (chat 6: "Work on the SRTM 30 m DEM in UTM 35S"), and Lc is the distance along the main watercourse from the outlet to the point nearest the centroid, not a straight line. The helper recomputed Lc from the watershed centroids and found 21.14, 27.38 and 13.30 km for P1, P2 and the Doringrivier, the same as yours, and the slopes 5.2 to 5.4 m/km. The helper also gave Struan as a TR102 station at 25°24′S, 26°07′E, next to Zeerust (stated in chat 6; I have not checked the coordinates). Still not in any file or chat: that F2 lies in Bushveld (veld zone 8) and well inside basin 1.
5. **Table numbers.** This is Table 5, so every later table moves up by one. The final numbering should be set once all blocks are in.
6. **Overlap with Table 11 (Results).** Step 9 and step 11 repeat the design peaks in Table 11. Either keep them here and drop the peak column from Table 11, or end Table 5 at the runoff coefficient. I kept them, since the reader then sees how each peak arises.

**Why the flood Methods need this**: Results 6.7 compares three methods that differ by 41%, and the Discussion says the choice of method decides the design flood. A reader can only judge that if the steps are visible. The dolomite share is 629.6 km² (46.4% of F2) from `49e_geology_dolomite_table.xlsx`, and it is the reason why the manual's warning (SANRAL, 2013:3-45) applies; it belongs in the Study Area and in the Discussion, not in Table 5.
