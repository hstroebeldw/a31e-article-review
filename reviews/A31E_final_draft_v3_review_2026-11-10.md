# Panel review of the assembled article (draft v3), 10 November 2026

Reviewers whose reports are consolidated here: hydrogeologist-groundwater (34 findings), water-quality-contaminants (21), literature-verifier (33 citation checks). Surface-water (24 findings) is merged in section F; the flood report is covered in `Flood_1in50_vs_1in100_and_SDF_inputs_2026-11-09.md`. The block was not rewritten. Every item in B needs the author's decision before any text changes.

## A. Clear errors (fix without interpretation)

| # | Where | Problem | Evidence | Fix |
| --- | --- | --- | --- | --- |
| A1 | Section 6.8, phosphate | "19% below the dam" is station A3H042Q01 only (14 of 74). A3H030 is 4% (2 of 56). Table 15 shows both. | `49d_water_quality_screening.csv` | Name both stations with n and period. |
| A2 | Section 4.3 | "Rain that does not run off recharges the groundwater": about 93% evaporates; recharge is about 29 mm of 597 mm. | Context §3; approved text had "a smaller part". | "Most of the rain that does not run off evaporates; a small part recharges the groundwater." |
| A3 | Section 1 | "Groundwater can be abstracted sustainably only at a rate balanced by recharge" contradicts Section 3.2 and Leake & Barlow (2013), Misconception 1. | Leake & Barlow 2013 | Delete or restate in capture terms. |
| A4 | Sections 5.2.2, 5.3.2 | Recharge 29.2 mm/a does not reproduce: 17.53 Mm³/a over 15 142 cells of 0.04 km² gives 28.9 mm/a. | `49b` §4 | Use 28.9 mm/a or state the cell area (author checks the GMS grid). |
| A5 | Section 6.1 | The 91% is storativity × thickness, i.e. water released if both zones were drained, not "per metre of fall". | Recomputed | Re-word. |
| A6 | Citation W1 | The values 597 mm, 602 km², 1 901 mm, A3B are not in Bailey & Pitman (2016) executive summary; `wr2012_A31E_row.csv` takes them from the WR2012 quaternary spreadsheet. | citation report | Cite the dataset; mark 99% and the median run "calculated from". |
| A7 | Citation W3 | De Wit & Stankiewicz (2006) refers to perennial drainage, not river flow or dam inflow. | Abstract | Use the source's term; drop the step to dam inflow or call it inference. |
| A8 | Citation W4 | Konikow & Leake (2014): "United States", "34 systems", "0.61" are not in the abstracts opened; the abstract gives 0.85 as the average for a sample of long-developed systems. This conflicts with problems-list item 3. | USGS, CA Water Library | Open the Wiley text, otherwise use the abstract wording. |
| A9 | Citation W5, W6 | Cuthbert et al. (2019) "mainly by heavy rainfall" and Xie et al. (2024) "during dry periods" are stronger than the abstracts (focused recharge; dry seasons). | abstracts | Re-word. |
| A10 | Citation W8 | MacDonald et al. (2021): β1 is 1.338 in Table 2 and 1.388 in the text; relation is spatial. | local PDF | "1.34 (Table 2)"; note spatial relation. |
| A11 | Citation W10, W11, W16, W17, W20, W21 | Smithers' method groups and the "conservative" label; Hashimoto's vulnerability is maximum severity; Moriasi ratings are for monthly steps; DWAF p. 93 shows deficit at 1:50 assurance; ISP excludes the 1990s drought rather than "does not mention" the dam. | citation report | Align each with its source. |
| A12 | Table 15, Section 6.8 | Percentages from 1–3 samples (188257, 188038, 188030) carry no information. | CSV | Show counts ("1 of 3"). |
| A13 | Section 4.4 / 2.6 | The two sections name different return-flow sources for DWAF (2004:57). | DWAF pp. 51, 57, 86 | Make them agree. |
| A14 | Section 6.8 | "Fewer than 0.5%" for Cl, Na, SAR: result file and CSV say none exceed. | `49_Block3_results.txt` | "in none of the samples". |

## B. Interpretations the author must decide

| # | Question | Options and cost |
| --- | --- | --- |
| B1 | Abstract, Discussion, Conclusions and Rec. 4 give only the S bound for groundwater and the river. Should the D bound (water from the ground drain, large drawdown, at most 1.2 Mm³/a deliverable) appear beside it? | (a) Add one clause in each place: complete, longer. (b) Leave: shorter, but breaks the rule that both bounds are reported together. |
| B2 | "The water of A31E is fresher" rests on one quartzite tributary (1971–1991) and seven groundwater samples of unknown position; the between-dam sites in A31E have the highest EC. | (a) Name what was measured and drop "the water of A31E". (b) Keep and qualify. (c) Keep: risk of challenge. |
| B3 | Cause of EC above 40 mS/m below the dam: return flow, natural dolomite above the dam (54.2% of the dam catchment), evaporation in the dam. Section 4.4 and the Discussion lean towards return flow. | (a) Present all three as inference. (b) Keep the lean and cite DWAF only. |
| B4 | D's conductivities lie at the PEST lower limits; its drawdowns and the 1.2 Mm³/a ceiling follow from the limits, not the data. The approved text said so; v3 does not. | Restore the sentence (short), or accept the risk of reading 1.2 as a finding. |
| B5 | Drains only remove water; the model cannot show a river losing water to the aquifer; "under 2% from rivers" in D partly follows from this. Approved sentence dropped in v3. | Restore in Section 5.3.2/6.5, or leave. |
| B6 | Steady state at mean recharge versus droughts of several years; Figure 13 places the shortfall band on a steady-state curve. | Add "at steady state" in Discussion/Conclusions and label the band as a scale comparison; or leave. |
| B7 | "None would reach a river" in D concerns water, not solutes; salts stay under the fields (evapotranspiration). | Say "in the model the water leaves through the ground drain" and that salts are not represented; or keep. |
| B8 | Travel time: only a median (about 140 years at n = 0.10). 11% of particles in S leave their start cell in under half a year; 90th percentile about 700 years. Porosity 0.01–0.10 not shown. | Report shares reaching a river within 1, 10 and 50 years and the porosity range; or keep the median alone. |
| B9 | Discussion names one cause that data could narrow (water-table position). Recharge and conductivity cannot be separated (S drawdown 0.96–7.43 m). | Name two causes and add flux gauging (low-flow gauging below the dam) to Rec. 6; or keep one. |
| B10 | Baseflow (2.00 Mm³/a) is the only flux information; matching it needs S scaled to about 0.2–0.35. | State that the estimates bracket the truth between S and D, or leave. |
| B11 | Drawdowns are 200 m cell means; P1 implies one borehole per cell, while Section 6.1 needs 150–740 boreholes. | Add the two clauses, or leave. |
| B12 | 47.5 m base of the weathered zone: 19 of 45 cells in S at 2.34 Mm³/a and 7 or 39 in D lie deeper. GRAII thicknesses inconsistent (25.36 + 182.14 = 207.5 against a base at 47.5 m). | Restore the count; author confirms thicknesses. |
| B13 | Section 3.2 states "access to groundwater appears to be the main limitation", which the Discussion replaces. | Remove or recast as a question. |
| B14 | The 262 levels may be pumping levels; three of four calibration levels were measured in 1990 and 1994 (drought). Caveat dropped in v3. | Restore in Results. |
| B15 | Evaporation in the upper dam and mixing: Kromellenboog "receives both waters" implies mixing; no mixing check was done (author decision). | Report the common-period comparison (2012–2023: 20.7 against 62.3 mS/m) as observation, or drop the clause. |
| B16 | Flow state of the sampling: 1989–1993 median storage 12.2%; medians 51.2 and 62.3 are different stations, periods and flow states. | One sentence saying they are not a trend. |
| B17 | Section 5.2.4 omits three steps (values at the detection limit; inorganic N definition; recalculation) and PO₄-P detection limits. | Add two sentences after the author confirms detection limits. |
| B18 | Population of 936 as evidence of no large urban source (DWS 2021:156 is a scan). | Label as inference. |
| B19 | DRASTIC 96.7% low: relative index, the irrigated cells' class is not stated, no layer in the folder. | State the class; or keep. |
| B20 | "Two waters" body wording, S/D labels, drought spans, 165 ha denominator, "floodplain", recommendation on flood absence (earlier items still open). | See problems list. |

## C. Wording and repetition

Cobbing, Calow and similar abstract-only sources are fine but should be re-opened if possible. Map 10 caption: "end at a river" means "in a cell whose river drain discharges"; name the river. Heading "Water quality and climate" (5.x.4) covers no water-quality run under the cases. Abstract: "salinity target" is not the guideline's term. Section 6.5 means over 474 against 45 cells (largest drawdown is the fairer comparison). "Case D" and "structure D" in one caption (Map 8) is confusing. Table 13 header should read "rivers and streams". The reference "Kromellenboog" is spelled "Krommellenboog" by DWAF.

## D. Checked and sound

Every Table 15 value against the CSV; sample numbers and periods; station positions; MODPATH counts (387/405, 288/405) and median 142.7 years; Table 11, Table 12 and Figure 13 values against `49b`; climate factors (S −3.8%/−10.5%, D −5%/−14%); 0.27–0.48 Mm³/a is 1.6–2.8% of recharge; 17.336 − 0.81 − 2.00 = 14.53 Mm³/a; DWAF (2004) pp. 50, 53, 55–57, 83, 86, 170–171; Hashimoto pp. 18–19; Leake & Barlow; Sankarasubramanian estimator; Scheff & Frierson; SANRAL 152 stations and 29 basins; Canadell 15.0 m; Knowling & Werner; Saft et al.; Rouault & Richard; Barnett et al. Table 2-1.

## E. Could not check

Konikow & Leake full text; Klemeš (1986) p. 13; Cobbing (2018); Lankford et al. (2023); Woessner & Poeter (2020); Pollock (2016); DWS (2021) pp. 130, 156, 163 (scan); DWAF (1996a, b); Climate Atlas values (Iturbide, Gutiérrez); DRASTIC layer; GMS model files; Figures 12 and 15 data; the DWS raw samples; the GIS folder `Map09_additional_lowering`.

## F. Surface-water findings (hydrologist-surface-water, 24 findings)

Clear errors: H4 the release test is x0.5 and x1.5, not +-10%; H14 the 296 against 186 Mm3 are WR2012 patched flows (series 1 totals 300.5); H15 0.166 Mm3 is the lowest since the 1982 survey, not "on record"; H16 2023 canal volume 2.19 includes two part months (complete years 1.89-2.16); H17 the 53 mm/a uses six complete years (all 15 years about 48 mm); H6 three places say the DWAF report states no method while the Discussion cites p. 54, which says the yield comes from the dams' firm yields; H19 Figure 11 does not show the firm yield; H20 "inflow as recorded" is a calculated remainder.

Interpretations for the author:
- H1 Climate cases are measured against a target raised from 2.34 to 2.49 Mm3/a; about half the rise in shortfall comes from the target (case M with the rule: 0.602 against 2.49, 0.536 against 2.34, Reference 0.479). Options: report both, split supply and demand, or keep and say so in the Abstract and Discussion.
- H2 With the rule, reliability by time (59%) equals the share of months with storage at or above 57% of capacity; it depends on zone 6 (1.003 set to 1.00) and the 99% threshold.
- H3 Without restriction the canal still fails in 88 of 120 months of 1986-1995; the "20 months" event becomes 34 months with evaporation +10%, and every year 1984-1995 fails in both bounds.
- H5 Firm yield 0.36 Mm3/a is set by one month (October 1992) in the least reliable part of the record, and depends on the release, evaporation and lowest storage; the comparison with DWAF's 1.4 is not like-with-like.
- H7 The reverse test passes (monthly NSE 0.564) only with the seasonal pattern of the tested years; with the Figure 3 pattern it is 0.143.
- H8 The canal carried a median 2.15 Mm3/a in years with storage above 75%; 5 of the 24 shortfall years had a full dam, so some shortfall reflects less demand.
- H9, H10 The non-recovery of inflow is stated as fact in 1.1 before the residual caveat; the 1986-1995 window includes 1995 (127%); 1987-1990 is the clean window; the reach between the dams gave 3.80 Mm3/a against 1.23 into the upper dam. Whether zone A3B represents the dam catchment is not shown.
- H11 Model evaporation is 6.5% below the Department's in 1984-1994 and 11% above after 1996.
- H12 The inflow factor ignores the temperature effect on runoff.
- H13 The rainfall range (+3% as 90th percentile) and "wettest tenth +0.5% to +3%" contradict each other; recheck against the Atlas.
- H18 1994 has 11 valid months, so the run of thirteen is broken in Q1; say so.
- H22 Abstract "delivers ... in 45% of the years" should read "would have delivered ... of the 74 years".
- H24 The fitting period moves reliability by time from 0.59 to 0.39, more than case D (0.48).

Checked and sound: Table 10, 13, 7, 8, 9 values; rule cost 0.21 Mm3/a; demand curve and firm yield arithmetic; record statistics (139 of 144 months below 25%; 24 of 38 years; zone rainfall 99.2%); climate factors from Table 6.

Not checked: DWAF (2004), Adeloye, Coerver, Saft, Moriasi, Atlas percentiles, Figure 2 construction, Tables 1-3.

Questions: does zone A3B cover the dam's catchment (area never stated); should the dry-season drop (2.6 to 0.9 Mm3/a) be reported; are the case labels "+1 C / +2 C" in Params stale (Table 6 gives +1.9 C).
