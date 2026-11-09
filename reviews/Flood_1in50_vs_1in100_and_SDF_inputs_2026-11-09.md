# Flood: SDF inputs found in the manual, and why the 1:50 and 1:100 flood lines look alike

Report of 9 November 2026. Nothing in the article, the workbooks or the result files was changed. All numbers were recomputed in code from the files named below and from the printed Drainage Manual (SANRAL, 2013), which I opened in Chrome from the DWS site (468 pages; the page numbers below are the printed ones).

## 1. The SDF peaks are correct: all six reproduce from the printed manual

Inputs read from the printed manual:
- Table 3B.1 (p. 3B-2): basin 1, station 546204 Struan, M = 56 mm, R = 30 days, C2 = 10%, C100 = 40%.
- Table 3B.2 (p. 3B-3), Struan, 1-day maxima for T = 2, 5, 10, 20, 50, 100, 200 years: 56, 80, 99, 119, 150, 177, 206 mm. Struan is at 25°24′S, 26°07′E, with 48 years of record and a mean annual rainfall of 549 mm.
- Equation 3.18 as printed (p. 3-46): P(t,T) = 1.13 (0.41 + 0.64 ln T) (−0.11 + 0.27 ln t) (0.79 M^0.69 R^0.20), t in minutes. For Tc between 6 and 24 hours the manual says to interpolate linearly between this value at 6 hours and the 1-day TR102 value.
- Equation 3.17, 3.19, 3.20 and the factors Y_T of Table 3.13 (2, 5, 10, 20, 50, 100: 0, 0.84, 1.28, 1.64, 2.05, 2.33).

Recomputed (L = 94.12 km, S = 5.355 m/km, A = 1 357.26 km²): Tc = 16.44 h; ARF = 84.4%.

| T (years) | Hershfield at 6 h (mm) | TR102 1-day (mm) | Point rainfall at Tc (mm) | C_T | Peak (m³/s) | Update 24 |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 35.8 | 56 | 47.5 | 0.100 | 92 | 92 |
| 5 | 60.4 | 80 | 71.8 | 0.208 | 289 | 289 |
| 10 | 79.0 | 99 | 90.6 | 0.265 | 464 | 464 |
| 20 | 97.6 | 119 | 110.0 | 0.311 | 662 | 662 |
| 50 | 122.1 | 150 | 138.3 | 0.364 | 974 | 974 |
| 100 | 140.7 | 177 | 161.8 | 0.400 | 1 252 | 1 252 |

So the 1:50-year peak of 974 m³/s is right (point rainfall 138.3 mm), and the 1:100-year point rainfall of 161.8 mm is right. The gaps in `Methods_flood_SDF_v2.md` (the 1:50 rainfall, the interpolation, the station) are closed.

## 2. Midgley and Pitman: the equation is confirmed, the MAP is not

Printed on p. 3-61: Q_T = 0.0377 K_T P A^0.6 C^0.2, with C = A √S / (L Lc) (S in m/m; L the hydraulic length; Lc the distance between the outlet and the centroid), and P the mean annual rainfall over the catchment (see Figure 3.7). K_T for Bushveld (zone 8, Table 3.17, p. 3-62) is 0.42, 0.57, 0.79 and 1.00 for 10, 20, 50 and 100 years. With S = 0.00536, L = 94.12 km, Lc = 27.38 km and P = 597 mm I recomputed 374, 507, 703 and 889 m³/s, as in Update 24. The square root, which the text file had lost, is there in the printed equation.

The MAP is the weak input. 597 mm is the WR2012 MAP of A31E alone. The WR2012 table (file `wr.xls`, WMA 3) gives MAP 546 mm for A31C (486 km²), 566 mm for A31D (705 km²) and 597 mm for A31E (602 km²). The dam catchment (1 162 km²) is A31C and A31D, and F2 adds about 195 km² (Doringrivier and the land between), which is in A31E. The area-weighted MAP is about 563 mm (558 mm for the dam catchment alone). At 563 mm the Midgley and Pitman peaks are 662 m³/s (1:50) and 838 m³/s (1:100), 6% below the values in Update 24, and the 1:100 value is 33% below the SDF, not 29%. The split of F2 by quaternary is an estimate: please take the exact split from your GIS if you want a defensible figure.

Not confirmed: that F2 lies in veld zone 8 (Bushveld) on Figure 3.20, and that it lies well inside SDF basin 1 on Figure 3.30. Both are map readings; the map pages I opened did not settle them. Zeerust is in Bushveld, so I expect zone 8, but I did not verify it.

## 3. The 1:50 and 1:100 flood lines are close, and the reason is the valley, not an error

What the model gives (cells of the 30 m mesh, Update 24, `files/gis/Map11_flood`, areas recomputed from the polygons):

| | 1:50 (SDF) | 1:100 (SDF) | 1:100 (Midgley and Pitman) |
| --- | --- | --- | --- |
| Inflow peak (m³/s) | 972 | 1 250 | 887 |
| Wet area (km²) | 7.72 | 7.97 | 7.60 |
| Mean depth of wet cells (m) | 2.34 | 2.53 | 2.28 |
| Area deeper than 1 m (km²) | 6.27 | 6.67 | 6.11 |
| Area deeper than 2 m (km²) | 4.41 | 4.94 | 4.21 |
| Largest depth (m) | 7.4 | 7.6 | 7.3 |

Between 1:50 and 1:100 the peak is 29% larger, the wet area is 3.3% larger, and the water surface in the cells that are wet in both rises by 0.28 m (median and mean; the 10th to 90th percentiles are 0.21 to 0.35 m). The 278 cells that are wet only at 1:100 add 0.25 km² and are shallow (median 0.15 m).

The flood line moves very little sideways. The extra 0.25 km² is spread over the 15.7 km reach, which makes the flood about 16 m wider in total, or about 8 m on each side, against a mean flooded width of about 490 m. That is a quarter of one 30 m cell. A rise of 0.28 m that moves the edge by 8 m means that the valley sides have a slope of about 3.5% at the edge. So at the scale of a map the two lines lie on top of each other, and the lines cannot be told apart on a 30 m terrain model whose vertical error is several metres (Update 22: SRTM of February 2000).

Is the 0.28 m rise reasonable? In a confined section the discharge goes roughly with the depth to the power 5/3, so a 29% larger peak gives a depth about 16% larger at the channel. The cells are on average 2.3 to 2.6 m deep, and the model gives 8% to 11% (2.34 to 2.53 m, area-weighted over all wet cells, and 2.58 to 2.86 m on the cells wet in both), which is lower than 16%, as expected where the water spreads into storage on the floodplain and the peak is attenuated. The inflow peaks are as intended (972 and 1 250 m³/s, from the 15-minute hydrographs; Section 1 above shows that 974 and 1 252 are the design peaks).

My reading: the result is physical, because the valley confines the flood, and the 1:50 and 1:100 lines cannot be separated at this terrain resolution. It does not look like an input error (the peaks differ as they should, and the depth differs by 0.28 m). I did not check the HEC-RAS files themselves: that the Q50 plan really ran with the Q50 hydrograph is shown only by the inflow peak of 972 m³/s in Update 24.

## 4. Options for the flood map (you decide)

1. Keep the 1:50 outline and show the water-surface rise, or the depth difference, between 1:50 and 1:100 as a second panel (the data exist: both depth rasters are in `Map11_flood`). This makes the difference visible without re-running anything.
2. Show depth classes for both floods side by side, with the area deeper than 2 m in each (4.4 and 4.9 km²).
3. If you want lines that separate more clearly, the cause is the terrain and not the hydrology. A finer terrain model along the reach is the only fix, and that is already Recommendation 6.

If the MAP for Midgley and Pitman is changed (Section 2), the Q100_MP plan has to be re-run with a peak of about 836 m³/s, and the wet area would change very little (the Midgley and Pitman plan differs from the SDF by 0.37 km² for a 29% lower peak). The SDF plans do not change.
