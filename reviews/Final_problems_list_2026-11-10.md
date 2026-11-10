# Problems still occurring in the draft set, and what the final draft does about them

Written 10 November 2026, for the meeting with Sascha. The final draft is `drafts/A31E_final_draft_v1.pdf`. Where a source was opened in Chrome or in the folder, it is named. Anything that could not be checked is marked **unverified**.

## A. Fixed in the final draft

| # | Problem | Fix | How it was checked |
| --- | --- | --- | --- |
| 1 | Section 1.1 gave the canal mean of the drought window as 0.25 Mm³/a. It does not reproduce. | Now 0.36 Mm³/a. | Workbook, months without a gap code: 0.360 (0.369 with the gap months). 0.25 belongs to the 11 counted years of 1984–1995. |
| 2 | Section 6.1 gave 168 ha irrigated land, 162 ha in fifteen patches, 145 ha under pivots. Table 14 uses 164.9 ha. | 164.9 ha in 18 patches, 147 ha under centre pivots. | Recomputed from `A31E_Irrigated.shp`, reprojected to EPSG:32735. If you hold another version of the layer, say so. |
| 3 | Konikow & Leake (2014): the text said "about 0.85 in the aquifer systems reviewed". | Now: 0.85 across the United States and a mean of 0.61 in the 34 systems and areas reviewed. | Publisher page opened in Chrome (abstract and the section on real systems). |
| 4 | Baseflow range 2.00 to 3.43 Mm³/a: the 3.43 (Hughes) was cited to Bailey & Pitman (2016), which does not contain it. | 3.43 dropped. Only 2.00 (Reserve determination, DWS, 2021) is used. "Five to nine times" became "almost nine times" (17.34 ÷ 2.00 = 8.7). | No source for 3.43 or 2.53 could be opened. Restore them only with a source. |
| 5 | DWAF (2004:57, 86) were used for return flow in the wrong way. | Page 57: return flow from irrigation in A31D and from the mines around Zeerust; its nutrient and salt content has limited re-use. Page 86: return flow from the towns and from irrigation is "being discharged into the Klein Marico River". Section 4.4 no longer points back to Section 2.6. | Both pages read in the report (WebFetch). |
| 6 | Section 3.3 carried the "later start of the summer rains" (Howard & Washington, 2020). | Sentence and reference removed. | Cases no longer rest on it. |
| 7 | Section 3.4 still described checks against other flood methods. 29 basins and 152 stations. | SDF only; 152 gauging stations in 29 drainage basins (SANRAL, 2013:3-43, 3-44). | Manual text in `files/sources_reports/`. |
| 8 | "Weathered zone holds 91% of the stored groundwater". | "Accounts for about 91% of the water the aquifer releases for each metre of fall in the water level." | 0.00998 × 25.36 ÷ (0.00998 × 25.36 + 0.00014 × 182.14) = 90.8%. |
| 9 | Table numbers, map numbers, orphan figure. | Tables 1–15 and Maps 1–11 follow order of appearance; depth to water is Map 7 and additional lowering Map 8; Figure 8 is cited again; Map 5 is the corrected soils map; Figure 6 is redrawn from inflow series 1. | Lists regenerated from the captions; page numbers read from the PDF. |
| 10 | Reference list held entries cited nowhere. | Removed: Pyburn (2015), Kapangaziwiri et al. (2011), Fowler et al. (2022), Peterson et al. (2021), News24 (2011), Howard & Washington (2020), Kovács (1988). | Citation cross-check by script. |
| 11 | Table 15: "no sample exceeds" for chloride, sodium and SAR cannot be confirmed from percentages rounded to whole numbers. | "Fewer than 0.5% of the samples at every site." | `49d_water_quality_screening.csv`. |
| 12 | Section 6.8 water quality wording. | Sulphate sentence with the medians; stations and number of samples named; 0.025 mg/L called the boundary between the mesotrophic and eutrophic classes (DWAF, 1996b:97). | Medians from the result file; DWAF page read earlier. |
| 13 | Section 6.3 had lost the sensitivity paragraph. Section 6.6 had "to the two sensitivity cases". The longest-event sentence was wrong for the dry case. | Paragraph restored with the verified numbers; "in the two sensitivity cases"; longest event "grows from the Reference run to case M" and with the rule further in case D. | `number_check.md`; Table 13 values. |
| 14 | Map 3 and Map 4 captions. | Original wording restored. | Article text. |
| 15 | Two-panel maps split from their captions at a page break. | Map height reduced. | Visual check of the PDF. |

All earlier decisions are in the text: thirteen shortfall years (1984–1996), two short answers in the Conclusions with no figures, "irrigated land", SDF only, 1:100 flood line only (Recommendation 6), no mixing check, no 47.5 m, reverse-test rerun, SAR 2.0 with its reason, Wilgeboomspruit sentence with Figure 8, Kalkdam above the Doringrivier, Map 9 exported from RAS Mapper and drawn in ArcGIS.

## B. Still open

**For you to decide or supply**

1. **AI declaration page.** The text is the old text. It needs your facts and your signature. I did not change it.
2. **Figures 12 and 15** are still the old pictures. The folder holds only their summary statistics, not the 262 levels or the water-quality samples, so they could not be redrawn in Excel style. Send the GMS export and the DWS downloads and they will be redrawn. (Update, draft v2: Figures 2–11, 13 and 14 are redrawn from the workbook and `49b_Groundwater_results.txt`. Figure 9 now shows both tests: forward storage in the upper panel, yearly canal of the reverse and forward tests in the lower panel; new caption. Checks in `drafts/figures_excel_style/scripts/checks*.txt`: reverse test 14 years, NSE 0.49, PBIAS +19.4%; forward 20 years, NSE 0.60.)
3. **Study Area, climate (2.2).** The paragraph is short and has no source for temperature.
4. **Section 1.1 and the Abstract** use "thirteen successive years from 1984"; the drought of Section 1.1 is October 1983 to September 1995. They are different periods, as the Abstract note says.
5. The firm yield (0.36 Mm³/a) is not in the Abstract. Say if you want it.

**Unverified**

6. Baseflow 3.43 and 2.53 Mm³/a: no source opened (the Eskom report, Sami 2016, was refused by the fetch tool and is not in the folder).
7. The registered 0.285 Mm³/a from boreholes and the comparison with 0.265 and 0.81 (DWS, 2021:156): the page is a scan.
8. Page numbers not re-opened: Pollock (2016) pp. 2 and 19; Niswonger et al. p. 14; Knowling & Werner (2016) p. 974; Moriasi et al. (2007) Table 4; Barnett et al. (2012); SKM (2013:18); Smithers (2012), including the 60% figure; Hashimoto et al. (1982:18–19), which sits at a page break.
9. DWAF (2004): "the report states no method" for the 1.4 Mm³/a rests on Table 5.1 and the text around it, not on a statement that no method exists.
10. Phosphate: the DWS download for the median of 0.044 to 0.010 mg/L is not in the folder.

**Process**

11. The panel (`/review-block`) has not been run on the assembled document. Run it on the final draft before it goes to Sascha; group A should then be empty or contain only the unverified items above.
12. These earlier deliverables predate your decisions and should not be used: the Docs artifact "A31E verification report", `out/A31E_Update_1_Final.zip`, `out/A31E_Review_Agents.zip`.

## C. Draft v2 (10 November, after the Word document)

- Text in Arial (embedded as Liberation Sans, which has the same metrics and shapes as Arial; Arial itself is not installed in the build workspace). Charts use the same font.
- Every main heading (Abstract, 1–9, References, AI declaration) starts on a new page. Elsewhere no page ends with more than about 3 cm open, apart from one before a heading that must stay with its text. To get this, some figures and tables sit a few paragraphs after their first mention, and at most one subsection later (two for the two-panel Maps 7, 8 and 10).
- All maps are 14 cm wide, at the same size, from the higher-resolution images in the Word document (Map 5 from the corrected map).
- Discussion v10 (`drafts/Discussion_integrated_v10.md`): same content, numbers and citations as v9, with paragraph openings and links that follow the Introduction. No new results.
- Figure 15 is printed slightly smaller (11.6 cm high) so that it shares a page with Table 15.
