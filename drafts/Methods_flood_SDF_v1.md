# Methods, flood: the SDF calculation, version 1 (Section 5.2.3, with a new table)

Draft for approval. Not in the article. Your friend shows the steps and a table of the SDF inputs and results. I think A31E should do the same, for three reasons. The SDF is the main flood estimate, so a reader should be able to follow it. The article now gives only the basin, two runoff coefficients and the time of concentration (16.4 h), and the supervisor asked that the Methods show what was done and why. The manual itself gives the steps (SANRAL, 2013:3-45 to 3-47), so the table is short. Everything in the table is from your files, and the 1:100-year peak reproduces from the inputs with the manual's equations (see the notes).

---

## 5.2.3 Flood (replaces the second paragraph; the first paragraph and the others stay)

The peak of the SDF was calculated in the steps of the drainage manual (SANRAL, 2013:3-45 to 3-47), with the inputs in Table 5. The catchment at F2 lies in SDF basin 1. Its area, the length of its longest watercourse and the slope between 10% and 85% of that length were taken from the GIS. The time of concentration follows from the length and slope. The design rainfall is the point rainfall for the time of concentration, reduced by the area reduction factor, and the runoff coefficient for each return period follows from the calibrated coefficients of the basin for the 1:2-year and 1:100-year floods. The Midgley and Pitman formula was applied as a check with the MAP of 597 mm (SANRAL, 2013:3-61–3-62), and the RMF was applied as an upper limit for Kovács regions K3 and K4, on whose boundary the catchment lies (Kovács, 1988; SANRAL, 2013:3-65–3-67). Each peak was given the triangular hydrograph that the manual prescribes for the SDF, which rises over one time of concentration and falls over two (SANRAL, 2013:3-45, 3-47).

**Table 5 (new): Inputs and steps of the SDF method at F2 (SANRAL, 2013:3-45 to 3-47).**

| Step | Quantity | Value |
| --- | --- | --- |
| 1 | SDF basin | 1 |
| 2 | Catchment area, A | 1 357.26 km² |
| 3 | Longest watercourse, L | 94.12 km |
| 4 | Slope between 10% and 85% of L, S | 5.36 m/km (1 155 m and 1 533 m) |
| 5 | Time of concentration, Tc = (0.87 L² / (1000 S))^0.385 | 16.44 h |
| 6 | Point rainfall for Tc, 1:100-year | 161.8 mm |
| 7 | Area reduction factor, ARF | 84.4% |
| 8 | Runoff coefficient, C2 and C100 | 10% and 40% |
| 9 | Peak, Q = C I A / 3.6, with I = point rainfall × ARF / Tc | 1:50-year 974 m³/s; 1:100-year 1 252 m³/s |

---

## Notes for the author (not article text)

**Recomputed with code from the manual's equations** (SANRAL, 2013:3-46, in the text file in the repository)
- Tc from L = 94.12 km and S = 5.36 m/km: 16.43 h (the files give 16.44).
- ARF = (90 000 − 12 800 ln A + 9 830 ln(60 Tc))^0.4 = 84.4%.
- Q100 = 0.40 × (161.8 × 0.844 / 16.44) × 1 357.26 / 3.6 = 1 253 m³/s (the files give 1 252; the difference is rounding).
- Not recomputable: the point rainfall of 161.8 mm itself (it needs the station values of Tables 3B.1 and 3B.2 or the Hershfield equation, and interpolation between them for Tc between 6 and 24 hours); I took it from your results file.

**Gaps you must close** (I did not fill them)
1. The point rainfall for the 1:50-year flood is not in the files. The peak of 974 m³/s implies about 138 mm (C50 = 0.364). Add the value from your workings, or drop the 1:50-year peak from the table.
2. The Midgley and Pitman peak of 889 m³/s does not reproduce from the inputs in the files. With K_T = 1.00 (Bushveld, Table 3.17), P = 597 mm, A = 1 357.26 km² and the catchment parameter C = A S / (L Lc) (the equation printed in the text file is damaged), using S = 0.00536, L = 94.12 km and Lc = 27.38 km, the formula gives 527 m³/s. To give 889 m³/s the catchment parameter C would have to be about 0.039, against 0.0028 here. Please send the values of S, L and Lc that you used, and the equation as printed in the manual; until then I have not put a Midgley and Pitman row in Table 5, and the 889 m³/s remains unreproducible (a known problem in the project context).
3. The table numbers: this is Table 5, so every later table moves up by one, in addition to the two moves of Block 1 and the table above. The final numbering should be set once, when all blocks are in.

**Why the flood Methods need this**: Results 6.7 compares three methods that differ by 41%, and the Discussion says the choice of method decides the design flood. A reader can only judge that if the SDF steps are visible. The friend's report has the same table (basin, area, longest watercourse, slope, time of concentration, point rainfall, area reduction factor, runoff coefficient, peak), in a catchment of 515 km² with basin 2.
