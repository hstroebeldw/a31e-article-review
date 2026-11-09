# A31E study: shared context for all reviewers

Read this file first. It says what the study is, what has already been verified, which decisions the author has made, and which problems are known. Do not re-report a known problem unless you find that it is wrong or incomplete.

## 1. The study

Honours article (North-West University, author LH Stroebel, supervisor Sascha Roopa) on the A31E quaternary catchment, Marico area, North West Province, South Africa. Semi-arid. About 602 km². Mean annual precipitation about 597 mm (WR2012 rainfall zone A3B). Klein Maricopoort Dam (survey capacity 7.07 Mm³) stands on the upstream boundary of the catchment and supplies a canal (gauge A3H031) to irrigators below it. Kromellenboog Dam lies downstream. The Klein Marico River runs between them.

Aim: quantify (1) how reliably the canal supply from Klein Maricopoort Dam meets the registered scheme volume (2.34 Mm³/a, 442 ha), (2) how far groundwater inside A31E could offset the shortfall, (3) how both respond to climate change, plus flood risk in the modelled reach and contaminant pathways.

Total registered water use in A31E is 3.38 Mm³/a: 69% scheme (canal), 22% river abstraction, 8% boreholes. The national register (WARMS) records entitlements, not abstraction.

## 2. Methods in brief

- **Dam water balance.** Monthly, hydrological years 1936–2009 (888 months; hydrological year runs October to September and is named after the calendar year in which it begins). Inflow is not gauged: it is the remainder of the dam's own recorded balance (843 months), with 27 months rebuilt from station records and 18 from the WR2012 patched flow. Series 1 = inflow as recorded (the basis of every table and figure in the article). Series 2 = adjusted for a fixed release entry before February 1987 (reported as a check only).
- **Restriction rule.** No operating rule could be obtained. The share of the registered volume that the canal received, by storage zone (seven zones), was derived from the records (delivered volume divided by asked-for volume). Fitted on hydrological years 1966–1974 and 1981–1986, tested on 1987–2009, then refitted on both. The rule cannot separate an imposed restriction from irrigators asking for less water. The model gives two bounds: with the rule (lower bound) and without restriction (upper bound).
- **Reliability, resilience, vulnerability** after Hashimoto et al. (1982), formulas of Adeloye et al. (2016). A month fails when delivery is below 99% of the registered volume. Test criteria from Moriasi et al. (2007): NSE above 0.5, RSR at most 0.7, PBIAS within ±25%.
- **Climate cases** are sensitivity steps, not projections: Reference; M (inflow ×0.93, evaporation and demand ×1.064, recharge ×0.96); D (inflow ×0.80, evaporation and demand ×1.064, recharge ×0.89). Derived from IPCC AR6 ranges for eastern southern Africa 2041–2060.
- **Groundwater.** GMS 10.9.6, MODFLOW-NWT, steady state, one layer of 207.5 m, 200 m cells, recharge as in the final model, river and stream drains plus a ground drain. Two structures, always reported together as bounds: S (ground drain 1 m below land surface; PEST calibration on four static levels) and D (ground drain 15.27 m below surface; conductivities re-estimated and ending at their lower limits). Abstraction spread over the 45 cells under land mapped as irrigated. MODPATH particle tracking for pathways. Calibration data: four static water levels (262 other levels are not recorded as static).
- **Flood.** Design flood peaks at F2 (catchment about 1 357 km²) by the SANRAL (2013) Standard Design Flood (SDF) method, the Midgley and Pitman formula, and the Regional Maximum Flood (RMF, regions K3 and K4). Routed through the modelled reach with HEC-RAS 2D (30 m cells refined to 15 m, SRTM 30 m terrain; the 20 m DEM smoothed the valleys and is not used for the flood model).
- **Water quality.** Screening of monitoring data against the DWAF (1996) guidelines; concentration and exceedance statistics; mixing of upstream and local water.

## 3. Verified results (sw1 workbook; recomputed independently)

- Failure months with the rule / without restriction: 364 / 118. Reliability by time: 0.590 / 0.867. Yearly reliability: 0.446 / 0.770. Longest event: 146 / 20 months (146 under both inflow series). Mean shortfall: 0.48 / 0.27 Mm³/a. Resilience 0.044 / 0.093. Vulnerability 0.50 / 0.88.
- Historic firm yield without restriction: no failure at 0.36 Mm³/a, one failure month at 0.38. Department's yield for the dam: 1.4 Mm³/a (DWAF 2004:50), no stated method or assurance.
- Table 6 (1987–2009, Mm³/a): inflow remainder 3.32, rain 0.42, evaporation 1.23, canal 1.20, spill 0.87, release 0.33, losses 0.01, change in storage +0.11.
- Canal record 1966–2009: 38 years with a complete record, 24 shortfall years (63%), mean shortfall 58% of the registered volume, longest run ten years (1984–1993), five shortfall years in which storage never fell below 75%.
- Test 1987–2009: monthly storage NSE 0.86, RSR 0.37, PBIAS +7.4%; yearly canal NSE 0.60, RSR 0.64, PBIAS −22.4%; monthly canal does not pass (NSE 0.38). The balance finds a shortfall in 192 of 265 valid months against 216 recorded. The excess in yearly volumes is about half in 1995 and 1996.
- Groundwater (S / D): mean drawdown in the 45 pumped cells at 0.25, 0.5 and 2.34 Mm³/a: S 0.96, 2.30, 40.8 m; D 4.92, 20.6 m and cells cannot deliver above about 1.2 Mm³/a. Share of pumped water from less river and stream discharge: S 87–89% up to 1.0 Mm³/a, 78% at 2.34; D 0.3–1.5%. Base-case discharge to rivers and streams: S 9.86 Mm³/a, D 0.63 Mm³/a, against estimates of 2.00 (DWS 2021), 2.53 and 3.43 Mm³/a (WR2012-based). Recharge 17.336 Mm³/a (DWS 2021 Reserve), 17.53 in the model. Scaled-pair result: models with half or double the recharge and conductivities fit the four levels equally well but give 0.96 to 7.43 m in S at 0.5 Mm³/a.
- Flood: SDF 1:100 peak 1 252 m³/s; Midgley and Pitman 889; RMF 1 205 (K3) and 2 355 (K4); area deeper than 1 m for the four plans 6.10 to 7.01 km².
- A31E in WR2012: 602 km², zone A3B, MAP 597 mm, runoff 7.21 Mm³/a. DWS (2021) Reserve: 936 people, recharge 17.336 Mm³/a, baseflow 2.00 Mm³/a.

## 4. Decisions already made by the author (do not reopen without cause)

- Approved values stay: 8.04 km² of cultivated land in the flood area and 3.43 Mm³/a Hughes baseflow (the 8.04 could not be reproduced from the file; leave open, do not use it in new arguments).
- Flood methods are cited from SANRAL (2013) only.
- Access date for web sources: 20 October 2026.
- Reliability tables use inflow series 1.
- The author decides every interpretation. Reviewers report; they do not rewrite the author's conclusions.
- Cite only sources that have been read. No invented references, pages or quotes.

## 5. Known problems already found (status at 9 November 2026)

- A source that does not say what the article says: Saft et al. (direction reversed), Calow et al., Konikow and Leake (0.85 is the US-wide value, the mean over 34 systems is 0.61), De Wit and Stankiewicz (50% is drainage density, not flow), Fowler et al. 2022 (farm dams only "in-between"), Peterson et al. 2021 (context, cause open), IPCC chapters (no support for a later start of the rains), Howard and Washington 2020 (about half a month, end-of-century RCP8.5), MacDonald et al. 2021 (1.338 in the table, 1.388 in the text; continental regression).
- Pyburn (2015) pages: the useful pages are 5, 45 and 113; Pyburn never mentions the dam and gives no cause for the 1986 decline.
- DWAF (2004): page 83 wording being confirmed by the author (hydrological information not updated since the agreement of 1988; confidence "very low"). The claim that the yield is "described as a firm yield (p. 54)" is unconfirmed.
- Midgley and Pitman peak (889 m³/s): the article gives none of the inputs, so it cannot be reproduced.
- Rule fit and test shares differ strongly between the two periods; this needs a table in the methods.
- The inflow is a back-calculated residual and carries all errors of the reservoir record; this limitation is not yet stated in the Discussion.
- The author has asked that the Discussion contain no new results, no pointers back to other sections, and few numbers.

## 6. Where the files are (inside this package, folder `files/`)

- `files/article/` : `A31E_Sascha_Correction_current_74pp.pdf` and its text `A31E_Sascha_Correction_text.txt` (the article as it stands, 74 pages; the text file keeps the page numbers as lone numbers).
- `files/workbooks/` : `A31E_Dam_Water_Balance_v2_caseM_FirmYield_sw1.xlsx` (the truth workbook; sheets Params, Inputs, Run_*, RRV, FirmYield, Sens, Q1, Q2, Check), `..._sw2.xlsx` (adjusted inflow series), `49e_geology_dolomite_table.xlsx`, `49h_flood_profiles_Q100_SDF.xlsx`, `design_hydrographs_15min.xlsx`, `A31E_Gauge_data_quality_tables.xlsx`, `WHICH_FILE_IS_LATEST.txt` (its note that sw2 is the Block 3 series is wrong: the article uses sw1).
- `files/results/` : `49_Block3_results.txt`, `49b_Groundwater_results.txt`, `49d_water_quality_screening.csv`, `49_Block_3_results_Update24.txt`, the flood and pathway proposals, `35_Maps_tables_and_figures_plan.txt`, earlier checks (`number_check.md`, `flood_deeper_than_1m_recomputed.csv`, `wr2012_A31E_row.csv`, `sanral_checks.txt`).
- `files/approved_text/` : `APPROVED_Full_text_v2_Sections_1-9.md`, the author's approved text, the source of the values the author has approved.
- `files/gis/` : shapefiles and rasters for irrigated land, stations, pathways (Map10) and the flood plans (Map11; `cells_<plan>.shp` hold the mesh cells, with D_CLASS depth classes).
- `files/sources_papers/` : PDFs of Hashimoto 1982, Sankarasubramanian 2001, Canadell 1996 (scanned; text extraction fails), Xie 2024, Leake and Barlow 2013, MacDonald 2021, Knowling and Werner 2016, Howard and Washington 2020.
- `files/sources_reports/` : text of the SANRAL Drainage Manual (2013) with page numbers at the end of each page, and OCR text of the WR2012 executive summary (Bailey and Pitman 2016). Not included: Pyburn (2015) and DWAF (2004); the verifier must fetch them from the links in the article's reference list (and mark what it could not read).
- `files/notes/` : earlier panel report, citation inventory, repetition map and structure template.
- `context/A31E_Verification_Report.md` : the verification report (status 8 November 2026).
- `drafts/` : blocks to review. `reviews/` : where the reports are written.

## 7. Updates of 9 November 2026 (afternoon), read after section 5

Sources now read by the main session (replace the matching lines in section 5):
- DWAF (2004): p. 50 Table 5.1 gives Klein Maricopoort 1.4 million m³/a ("Yield"; source: Crocodile (West) and Marico situation assessment report). P. 54 says the yield of the ISP was obtained from the firm yields of the dams in Table 5.1, so the "described as a firm yield (p. 54)" claim is supported. P. 83: "no update of the hydrological information of the Marico River catchment since the TSWASA agreement" (1988, pp. 50–51) and "The level of confidence on the hydrological information is very low."
- Pyburn (2015), printed pages: p. 45 is about the Paardenvallei eyes only (declined to almost nil in 1986; low flow for almost a decade until the rains of 1996). P. 113: a 12-year period of no or very little recharge was calculated between 1983 and 1995, corresponding with a decline in spring flow and water tables. P. 5: Rietpoort Well Field commissioned (1974); Rietpoort Spring ceased flowing ten years later "during a period of low rainfall". P. 109 ascribes that cessation (March 1984) to the intensive pumping of the well field. The article cites pp. 28, 44 and 4 (probably PDF page numbers); the printed pages are 45, 5 and 113. Pyburn never mentions the dam.
- Kapangaziwiri et al. (2011:128): gauged low flows "often affected by poorly defined upstream developments".
- Fowler et al. (2022): sustained hillslope drainage and delayed recharge rated plausible; farm dams in-between.
- Peterson et al. (2021): 161 catchments, 37%, by mid-2017, confirmed only through a press report (abstract not opened).

Analysis added in the main session (not in the workbook): script `files/notes/A31E_test_replication_sim.py` is not present here; the numbers are: forward test (rule 1, 1987–2009) storage NSE 0.86, monthly canal 0.38, yearly canal 0.60 (PBIAS −22.4%); reverse test (rule 2, pattern 2, years 1966–74 and 1981–86, series 1): monthly canal NSE 0.53, RSR 0.69, PBIAS +21.8% (154 months); yearly canal NSE 0.34, RSR 0.81, PBIAS +22.5% (12 years). A rule fitted on 1987–2009 itself gives yearly PBIAS −7.2% (NSE 0.68) forward. Recorded-canal run: storage NSE 0.996. The reviewers may re-run these from the workbook (the structure of Run_Test is described in its formulas); treat them as unverified until you have recomputed them.

Errors removed from earlier versions: the median yearly inflow of 1996–2009 is 3.22 Mm³/a, below the long-term median 3.71 (6 of 14 years above), so no argument may use a return of the inflow to above its median after 1996.

Rules for the Discussion (author, 9 November): short, one point per paragraph, the point first; few numbers; no new results; no pointers back to sections; plain words ("store", "memory", "onset", "persistence" are not used); the tone of the Introduction.

## 8. Structure decision of 9 November (author, 16:01): one integrated Discussion

- Results and Methods carry the detail and the reasons. The Discussion does not retell them. A reader should see what was decided without being drawn into how it was reached; the Results show how.
- The Discussion brings the results together, says how they link and what they mean for the catchment, and leads to the Recommendations. It is one section of a few paragraphs, the point first, without sub-headings.
- Do not go through every result and small part in a critical, sophisticated way. That is how an AI writes a discussion and not how a student does. Few numbers; those belong to Results.
- The Conclusions link the Introduction to the Recommendations and do not repeat results.
- Results should read easily: what was done, why, and what was found, in plain words, as in the example report of a previous year (VP Zandberg, First Draft). That report has no Discussion; its Risk assessment and Recommendations chapters did the interpreting.
- Draft: `drafts/Discussion_integrated_v1.md`. Block 1 v14 and Block 2 v2 stay as the saved Results drafts and as the source of the central ideas.
