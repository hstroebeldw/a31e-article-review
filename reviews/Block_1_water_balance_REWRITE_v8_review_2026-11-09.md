# Panel report: Block 1 water balance, version 8 (Sections 6.2, 6.3, 7.1)

Date: 9 November 2026. Reviewers: hydrologist-surface-water, literature-verifier, academic-editor (all independent). Consolidated by the main session. Nothing in the article, the workbooks or the block was edited.

Items marked **[main session]** were re-run by the main session after the panel returned. The main session also found that its own reverse test (Table 8) used the wrong years; see A1.

---

## A. Clear errors

| # | Where | Problem | Evidence | Fix |
|---|---|---|---|---|
| A1 | Table 8, reverse test; 6.3 "about 22% out … in both directions" | **The reverse test was run over the wrong years.** "Hydrological years 1966–1974 and 1981–1986" were run as October 1966–September 1974 and October 1981–September 1986, which omits hydrological years 1974 and 1986 (a year is named after the calendar year in which it starts). Corrected over the stated years [main session, confirmed independently by the surface-water reviewer]: monthly canal 178 months, NSE 0.56, RSR 0.66, PBIAS +18.9 (passes); yearly canal 14 years, NSE 0.49, RSR 0.72, PBIAS +19.4 (fails narrowly, on NSE and RSR). The series 2 values quoted in the notes (0.37, +24.6) were also from the short run; the corrected series 2 gives 0.51 and +21.7 for the yearly canal volume. | `A31E_test_replication_sim.py`, rerun with ranges 196610–197509 and 198110–198709; Rule!E7 defines the fit period. | Replace Table 8 reverse columns (178 months; 14 years; 0.56 / 0.66 / +18.9; 0.49 / 0.72 / +19.4). "About 22% out in both directions" no longer holds (22% forward, 19% reverse). |
| A2 | 7.1 "since its capacity covers less than two years of the registered volume"; 6.2 "about three years … about 1.8 years once evaporation and release are added" | The two sections give different quantities. 7.07 / 2.34 = 3.0 years of the registered volume; about 1.8 years only after evaporation and release are added (1.76 with the release table, 1.70 with the recorded 0.33). Editor and surface-water reviewer agree. | Params B4, B6; Run_Test mean storage 3.11. | Use one wording in both places: "less than two years of the registered volume together with the evaporation and release", or drop the number from 7.1. |
| A3 | 7.1 "the dry years of 1981 to 1986" | Zone A3B rainfall is 585 mm in 1981 (97% of the 605 mm mean) and 557 mm in 1986 (92%). The dry years are 1982–1985 (454, 378, 347, 386 mm). The 1981 inflow (7.75 Mm³/a) was above the median. Editor and surface-water reviewer agree. | Inputs, rainfall and series 1 by hydrological year [main session earlier output agrees]. | "the dry years of 1982 to 1985". The rainfall of those years must be reported in Results if the Discussion relies on it. |
| A4 | 7.1 "In some shortfall years the dam stood nearly full" | The five years are those with storage never below 75% (lowest start-of-month storage: 100.5%, 99.4%, 94.4%, 75.5%, 75.5%). Two of five are not "nearly full". | Inputs H and G; Q1. | "stood above three-quarters full" (as 6.2 says). |
| A5 | 7.1 and 6.3 Pyburn attributions | Per the citation check, Pyburn p. 113 (12 years of no or very little recharge, 1983–1995) and p. 109 (Rietpoort Spring ceased March 1984 through pumping) lie in Appendix A, which summarises earlier reports: p. 113 under 8.1.16 (Bogare, 2005, report 2005/0076-02), p. 109 under 8.1.13 (Botha, 1993, GH3815). So Pyburn did not "calculate" or "ascribe" either. The p. 113 passage does not name "the Zeerust dolomite" in the part read. **Unverified: this rests on a text extraction of the PDF, not on page images.** | Citation check ID 10a, 10b. | "reports that earlier work calculated …" and "earlier work (Botha, 1993, in Pyburn, 2015:109) ascribes …"; Bogare and Botha unread, so mark as cited in Pyburn. Drop "in the Zeerust dolomite" until p. 113 is checked. |
| A6 | Table 8 caption, "A positive PBIAS means that the model is too low (Moriasi et al., 2007:891)" | The sign convention is on p. 888 of Moriasi, not p. 891. The criteria values are on p. 891 and correct. | Citation check ID 6. | Cite "2007:888, 891". |
| A7 | 7.1 "(Peterson et al., 2021:745; Fowler et al., 2022)" | The sentence reads as if both support "groundwater processes were among the explanations rated plausible". Only Fowler rates them. Peterson is confirmed only at abstract level (Crossref, press release); the paper's own explanation is increased transpiration. Rule 2: the full text of Peterson was not opened. | Citation check ID 12a/12b. | Cite each for its own point, or cite Fowler alone; mark Peterson "abstract only". |
| A8 | 7.1 "the register records entitlements (DWS, s.a.f)" | The WARMS page describes the register of water use and authorisations. It does not use "entitlement" or say it is not abstraction. | Citation check ID 8. | "records registered and authorised use" (supported), or add a source for "not measured abstraction". |
| A9 | 6.2 "The longest run of shortfall years lasted ten years, from 1984 to 1993" | 1994 has 11 valid months carrying 0.28 Mm³. The missing month (a part-month, April 1995) would need about 2.0 Mm³ to make 1994 a non-shortfall year, against 0.971 as the largest monthly canal volume on record. 1995 and 1996 are shortfall years. The run is therefore at least 13 years (1984–1996) by inference, matching the modelled event of December 1983 to January 1996. | Inputs AM, O. | Decision B7. |
| A10 | 6.3 "one month fails at 0.37 Mm³/a"; Figure 11 | 0.37 is recomputed correctly, but the FirmYield sheet's rule columns do not reproduce: at 0.5 Mm³/a the sheet gives 77 failure months and reliability 0.913, the model gives 159 and 0.821 (= Sens row 9, which the text uses). If Figure 11 plots the FirmYield rule columns, it is wrong. | FirmYield F10:H17 against Sens L9. Already a known open item (project context). | Check what Figure 11 plots; replace the rule columns from Sens. |
| A11 | Table 9 column headers "(lower bound)", "(upper bound)" | Conflicts with 7.1 ("not a strict lower bound"). | Article line ~1432. | "with the rule" / "without restriction". |
| A12 | 6.2 "It is positive in every year" (net contribution) | True for the 21 years with a value in 1987–2009; 1991 (0.07) and 1997 (0.12) are close to zero. | Q2!P. | "positive in each of the 21 years with a value". |
| A13 | Header of the file; 6.3 "changes the reliability by time to 0.588 … 0.865" | A 0.002 difference reported to three decimals and called a change. Stale header ("version 4"). | Sens rows 21, 47. | "leaves it almost unchanged (0.59 and 0.86)". |
| A14 | Table 8 caption, reverse test | The capacities used are not stated (7.88 to September 1980, 8.07 for 1980–1981, 7.07 from 1982); the area curve is capped at 7.07 Mm³. | Inputs G; Curve K16:L16. | Name them in the caption. |
| A15 | Table 8 caption, Moriasi criteria | The criteria are for monthly streamflow; the transfer to storage and to yearly canal volumes (n = 20 and 14) is not stated. With 14 values the result is unstable: moving from 12 to 14 years moved the reverse yearly NSE from 0.34 to 0.49. | Params A54 (the workbook states "transferred"); the main session's two reverse runs. | Add "set for monthly streamflow; transferred here" and the small n. |

---

## B. Interpretations the author must decide

**B1. Does the reverse test show that the rule does not carry over? (critical, found by the surface-water reviewer, verified by the main session)**
The corrected reverse test leaves the yearly canal volume 19% too low. But on the same 14 years the fit-period rule fitted on those very years leaves it 14.7% too low [main session], and no restriction at all leaves it 9.4% too low. The canal carried more than the registered 2.34 Mm³/a in 11 of the 15 complete years 1966–1982 (up to 4.05), and the model cannot deliver more than the registered volume. So most of the reverse bias comes from the demand cap, and the rule transfer accounts for about 5 percentage points. In the forward test the rule transfer accounts for about 15 of the 22 points (the rule fitted on the test period gives −7.2%). Separately, the fit-period shares are measured against a different asked-for volume (a mean canal volume of 3.06 Mm³/a in months with the dam at 85% or more) than the test-period shares (2.34 × the seasonal pattern), so the shares are not like with like (Rule!T19, N).
Options:
1. Keep "the rule did not carry over" and base it on the forward test and the rule shares only; report the reverse test with the demand-cap limit. Cost: Table 8 needs a note, and the reverse yearly fail is explained by demand, not rule.
2. Say that the operation or the demand changed, "either the operator restricted harder, or irrigators asked for less water, or the demand before 1987 was larger than the registered volume", and no more. Cost: weaker headline, but it is what the evidence supports.
3. Drop the reverse test and keep the forward test with a sentence that the rule describes the test period. Cost: loses the second direction the author wanted to keep.
Recommendation of the main session: option 2 with the reverse test kept in Table 8.

**B2. A third explanation for the non-transfer: data before 1987.** The release is not gauged before 1987 (series 2 exists for that reason), the inflow is back-calculated with a fixed release entry, and the capacity differs. Some of the non-transfer may sit in the data of the two periods. The editor and the surface-water reviewer both raise it. Add as a clause, or leave out.

**B3. The monthly canal result is in-sample for the seasonal pattern.** The pattern used in each direction comes from the canal record of the test years (forward pattern: A3H031 1997–2014, which overlaps 1987–2009; reverse pattern: fit-period months with the dam at 85% or more). Swapping the patterns drops the monthly canal NSE to 0.10 (reverse) and −0.27 (forward). The monthly pass in the reverse test is therefore not independent support. Option: say so in the Table 8 caption and in 7.1's test sentence.

**B4. "A quarter of 1.4 Mm³/a" (new result in the Discussion; recompute with assumptions).** The ratio appears only in 7.1. The surface-water reviewer: the historic firm yield rests on a lowest usable storage of 0.166 Mm³ (the recorded minimum of November 1992, next to the limiting month) and on taking the release first. It is 0.44 with no dead storage, 0.48 with no river release, 0.54 with neither. Whether the Department's 1.4 includes the release is unknown (unverified). "Well below 1.4" survives; "a quarter" depends on the assumptions. Options: move the comparison to 6.3 with these qualifiers and keep only the conclusion in 7.1; or keep "about a quarter" in 7.1 with the qualifier.

**B5. Inflow is a residual: how to say it in two sentences.** The drought signal survives (35 of 168 months in 1982–1995 have zero inflow, but the fall from about 3.7 to 0.84 Mm³/a is larger than a 30% evaporation error of about 0.2). The text states the limit only for the test. Option: one sentence in 6.2 and one in 7.1.

**B6. The cause paragraph (several separate decisions).**
a. The 1982–1985 window (A3) and whether Results should report the rainfall of those years.
b. Pyburn attributions (A5): present Bogare and Botha as cited in Pyburn, mark unverified.
c. Pyburn p. 5 attributes the Rietpoort cessation to "a period of low rainfall", p. 109 (Botha) to pumping. Present both, or drop the sentence. The well field's position relative to the dam's catchment is not known; the editor notes that one local spring is generalised to the inflow, which was about 0.84 against a median of 3.7 Mm³/a.
d. The Victorian analogue: argued for relevance, or cut.
e. Whether to state the consequence promised in the opening sentence ("so its cause matters for how the results are read"): the editor says the paragraph does not keep that promise. Options: one sentence (for example, if recharge stays low after a drought, dry years are followed by years of low inflow, which this record counts once), or cut the opening.

**B7. The run of shortfall years: ten (strict) or thirteen (by inference).** Option 1: keep ten and the reason. Option 2: give both. Cost of option 1: it understates the continuous shortfall that the modelled event shows.

**B8. Reach: net contribution (6.2).** The surface-water reviewer: the share (81 / 98 / 75%) is mechanical (the upper dam passed 0.07 against 1.92 Mm³/a); the informative contrast is the absolute net contribution (3.80 against 5.80 Mm³/a) against the modelled naturalised runoff (7.42 against 6.51). The Kromellenboog inflow is itself a residual, so the net contribution is a difference of two residuals, and 1992–1993 have no yearly value. Return flow alone cannot explain the rise (canal +1.48, contribution +2.0), so "part of" is right. The editor: the return-flow reading is not an approved interpretation and nothing in the block takes it up; the definition repeats 4.3. Options: lead with the absolute values and add the residual caveat in the Table 7 caption; move the return-flow sentence to the Discussion or drop it.

**B9. The trade-off wording (7.1).** The rule also delivers less in total (1.86 against 2.07 Mm³/a; reliability by volume 0.795 against 0.883; 0.21 Mm³/a extra lost to evaporation and spill), so it is not a neutral trade-off like Hashimoto's optimised policies. Add one clause, or leave it as "a similar trade-off".

**B10. "Not a strict lower bound" and its direction (editor).** The "therefore" is a missing step. State the direction (the rule fitted on the test period alone gives a lower reliability: 0.39 against 0.59), or remove the sentence.

**B11. Where the test design lives.** The editor: test design (two directions, criteria, the reason storage is not compared) belongs in Methods (Analysis); Results give the outcome. The current Methods describe the forward test only and Figure 9 shows the forward test.

---

## C. Wording and repetition

Merged from the editor's 40 findings (editor IDs in brackets); the most important first.

1. **Number density in Results.** [1, 6, 7, 10, 13, 14, 16, 19, 21]
   - 6.2 para 1: about 14 numbers and dates (keep 0.84 and one median).
   - 6.2 para 3: about 9 numbers.
   - 6.2 Wilgeboomspruit: about 12 numbers; cut to the dry-spell result and one rainfall remark.
   - 6.3 reliability paragraph: about 25 numbers in 12 sentences; split into three paragraphs and keep only numbers not in Table 9.
   - 6.3 firm-yield paragraph: about 14 numbers; keep the series 1 yield and one sensitivity.
   - Repeated in tables: 22% (PBIAS row), 81 / 98 / 75% (Table 7), 1.86 and 2.07 (2.34 minus the mean shortfall).
   - The comparison "0.28 … about as large as … 0.29" is an orphan since the Discussion no longer uses it.
2. **Eight spans for "the drought".** [3] The Introduction defines October 1983–September 1995; 6.2 and 6.3 use 1982–1994, December 1982–March 1984, 1985–1994, 1984–1993, December 1983–January 1996, and 7.1 uses 1983–1995 and 1982–1985. Say once why the spans differ (series and measure); use the Introduction span where possible.
3. **7.1 paragraph structure.** [14/23, B1-14] Paragraph 1 holds five points, paragraph 2 four. The author's rule is one point per paragraph, point first. The structure, not the word count (about 500), is what makes it long.
4. **Repetition of the Department's yield.** [30] 1.4 Mm³/a, no method and very low confidence appear in the Introduction 1.1, in 3.1 and now in 7.1. 7.1 should hold only the comparison and why it is not like with like. Also say "Table 5.1 states no assurance" (supported only for Table 5.1).
5. **"The records cannot separate the two" used three times.** [26] Keep one.
6. **Explanation inside Results.** [20] "because the canal is restricted whenever the dam stands low" and "because it restricts delivery by storage whatever the demand" are consequences of how the rule is built; cut or move.
7. **Methods content in captions and results.** [5, 11, 17] Table 6 caption (two inflow means 3.32 and 3.39; two canal quantities 1.20 and 1.23; why 1987); the test design; series 1 and 2 not defined. Move to Data preparation; label the canal quantities differently.
8. **Terminology.** [12, 15, 18]
   - "test", "consistency" and "validation" are used for one procedure; use "consistency check" once in Methods and mark the storage column as the circular one.
   - A percentage and a fraction for the same reliability.
   - "Firm yield" is not defined in Results (the 0.36 is "the largest demand the dam could have met").
9. **Repeated claims.** [2, 22, 27, 29, 37, 39] Inflow below median despite rain (also in 1.1; use one window); "more failures but shallower" restates 6.3 (keep one clause tied to Hashimoto); "the register records entitlements" is in 2.6 and 3.1 (keep the consequence); "too small for a drought of this length" is close to trivial (cut or compare with something specific); "A single drought in 74 years" is a summarising closer and an interpretation (364 failure months, 146 in one event; Introduction 3 says multi-year droughts cluster); confirm that 7.2 covers the reach, net contribution and Wilgeboomspruit.
10. **Sentence rhythm.** [40] Nearly every 7.1 sentence runs 25–35 words; terms from the workflow ("rule run", "the two bounds", "fit period") are not in the Introduction; "not like with like" is colloquial.
11. **Kapangaziwiri.** [35] The source says "often affected by poorly defined upstream developments". The dam inflow is a calculated remainder, not a gauged low flow. Fit the wording.
12. **Wilgeboomspruit.** [B1-19] The record ends in August 1992, so "dry again from March 1992" runs to the end of the record; gaps fall at the onset (August–September 1982, October–December 1983); a 25% fall in rainfall against a 67% fall in flow fits the high runoff elasticity of semi-arid catchments, so the February 1988 month (211 mm, no flow) is the stronger evidence. Name the end of the record and the gaps.
13. **Sources to introduce.** [33] The upstream dolomite appears first in 7.1; Study Area 2.4 says karst is absent in A31E. Introduce the upstream geology in the Study Area.

---

## D. Checked and sound (recomputed unless stated)

- Inflow, series 1: median 3.708 (3.224 without 1975–1980); 1996–2009 median 3.22 (equal to the other 3.22 by coincidence); 1985–1994 mean 0.841 (36% of 2.34); below both medians in every year 1982–1994; rainfall 1987–1990 (693, 660, 631, 682 mm) above the 605 mm mean.
- Storage 99.3% at the start of December 1982; 21.9% in March 1984 (end-of-month: 95.9% and 20.6%).
- Table 6: every cell; evaporation 33% and 50% of inflow.
- Canal record: 38 years, 24 shortfall years (63%), mean shortfall 57.5%, five shortfall years with storage never below 75%.
- Table 7: all cells (using end storages for 1992–1993); rank correlation 0.762 over 21 years; Wilgeboomspruit figures (2.10; 42 of 50; 3 of 4 months above 100 mm; 0.69; 660 and 496 mm/a).
- Forward test: every Table 8 forward value; 192 and 216 months; 49% of the yearly excess in 1995–1996 (ratio 3.3); the rule fitted on the test period gives −7.2% and NSE 0.68; recorded-canal storage NSE 0.996. The surface-water reviewer's rebuild of Run_Test and the main session's rebuild agree to rounding.
- Reliability and Table 9: 59–87% and 45–77%; 364 / 118 (3.1 times); vulnerability 0.50 / 0.88; the event December 1983–January 1996, 146 months, 40% of failure months, total 21.86 Mm³ (9.3 times the yearly volume); events no longer than 20 months; 1.86 / 2.07; +0.15 and +0.06; 0.59, 0.39 and 169; 0.588 / 0.865; 8% at 1.5; 0.82 and 128 at 0.5; 0.28 and 0.29.
- Firm yield: series 1 none at 0.36, one at 0.37; series 2 none at 0.30, one at 0.32; October 1992 first in both.
- Hashimoto et al. (1982:19): quotation verified in the PDF (the passage is the water-supply reservoir example; "similar" is an adequate hedge).
- DWAF (2004): p. 50 Table 5.1 (Klein Maricopoort 1.4 million m³/a, "Yield"); p. 54 (the ISP yield was obtained from firm yields of dams); p. 83 ("no update of the hydrological information … since the TSWASA agreement"; confidence "very low"). The tool reports a sharing agreement of 1987 on p. 55 and 1988 on pp. 50–51 and 83: the author decides which year to use.
- Kapangaziwiri et al. (2011:128): "often affected by poorly defined upstream developments … specifically during periods of low flow" (second half of the sentence supported; "cannot separate" is the author's inference).
- Fowler et al. (2022): hillslope drainage and delayed recharge rated plausible; farm dams in-between.
- Moriasi et al. (2007): values on p. 891 (NSE > 0.50, RSR < 0.70; ±25% for streamflow; "for a monthly time step", p. 893 says they need modifying for other time steps).
- No pointers back to sections in 7.1; no banned words; no em dashes or first person.

---

## E. Could not check

- Figures 6–11 (in particular whether Figure 6 is on series 1 and what Figure 11 plots).
- DWA (2012) and DWS (s.a.b) at source (checked against the workbook copy only).
- Peterson et al. (2021) full text; Bogare (2005) and Botha (1993); Pyburn page images (all page findings come from a text extraction); the whole of DWAF (2004).
- Whether the Rietpoort Well Field lies inside the dam's catchment; whether the Department's 1.4 Mm³/a includes the release.
- The sw2 workbook (series 2 values taken from reruns).
- Moriasi (2007:891) page numbers were checked through a web tool, not page images.

---

## Summary counts

A: 15 clear errors (one of them the main session's own: A1). B: 11 interpretations. C: 13 groups of wording and repetition findings. D: 11 groups of checked items. E: 7 items not checked.
