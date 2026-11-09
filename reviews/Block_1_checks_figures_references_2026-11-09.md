# Checks of figures, references and workbook for Block 1 (9 November 2026)

Nothing in the article or the workbooks was edited. Each item says what was checked, what was found, and the exact change for the article.

## 1. Pyburn page numbers
- The article cites Pyburn (2015) once: the sentence in 7.1 (article lines 1877 and 1880: "2015:28, 44" and "2015:4").
- Version 10 of 7.1 replaces that sentence. It uses the printed pages 45 and 113 (page 5 is dropped with the Rietpoort sentence). Page 28 could not be checked against anything the article says; it disappears with the replacement.
- Source for the pages: the NWU repository PDF as read through a text extraction (printed page numbers). Pyburn pp. 109 and 113 are summaries of earlier reports (Botha 1993; Bogare 2005), as the citation check found.

## 2. Figure 6 (article PDF page 38)
- The figure plots the WR2012 patched observed flow, with a median of 3.94 Mm³/a and a rainfall mean of 599 mm. The text of version 10 uses series 1 and a median of 3.71 Mm³/a. They do not agree.
- Done: a replot on series 1 for hydrological years 1981–2009 (Figure_6_series1.png). Series 1 is the sum of the monthly inflow of the workbook (Inputs column AT). The median 3.71 is over the 74 years. The rainfall mean line (599 mm, 1920–2009) is taken from the current figure because the workbook holds only 1936–2009 (mean 604.7 mm). Years with months not taken from the dam record are grey (45 such months in the record).
- Check on the data: 1982 2.12 and 1983 0.64 Mm³/a on series 1, against 2.14 and 0.59 in the article's sentence (article line 1341), which uses the patched flow.
- New caption: "Yearly rainfall in WR2012 rainfall zone A3B (upper panel) and yearly inflow to Klein Maricopoort Dam as recorded in the dam's balance (series 1, lower panel), hydrological years 1981–2009, with the long-term mean rainfall (1920–2009) and the median inflow (1936–2009). Grey: years with months that are not taken from the dam record (Bailey & Pitman, 2016; DWA, 2012)."
- Article lines that still say "patched observed flow" and "3.94": lines 1329, 1330 and 1349 (all in 6.2). The 3.94 appears nowhere else.

## 3. Figure 7 (article PDF page 39)
- The caption has two panels: monthly storage (upper) and the yearly canal volume (lower), with years not counted in grey. 6.2 cites Figure 7 for the canal record, which is correct.
- Only the List of Figures title is incomplete: "Monthly storage in Klein Maricopoort Dam, June 1936 to November 2010". Change to "Monthly storage in Klein Maricopoort Dam, June 1936 to November 2010, and yearly volume in the canal, 1936–2024".

## 4. Figure 9 (article PDF page 40)
- The figure shows the simulated and recorded monthly storage 1987–2009 only, that is, the forward storage fit. It does not show the reverse test or the canal volume, so it cannot name both directions.
- Change the caption and the List of Figures title from "(test of the restriction rule)" to "(forward test)". The storage fit mainly tests the outflows, because the inflow is calculated from the recorded storage, so "test of the restriction rule" overstates it.
- Table 8 carries the reverse test; no new figure is needed.

## 5. Figure 11 and the FirmYield sheet
- Figure 11 (article PDF page 42): the with-rule curve starts near 0.82 at 0.5 Mm³/a and ends near 0.53 at 3.0 Mm³/a, and the unrestricted curve is near 0.87 at 2.34. These are the Sens values.
- Check: the rebuilt model (Rule 3, series 1, pattern 1, 888 months) reproduces all twelve with-rule values of Sens (failure months 159, 180, 204, 236, 265, 300, 325, 358, 381, 399, 417, 364 for 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0 and 2.34 Mm³/a; reliability by time 0.821 … 0.530, 0.590). Figure 11 and the text of 6.3 are therefore right.
- The FirmYield sheet is wrong only in its typed "Rule" columns (failure months 77, 67, 65, 62, 56, 53, 49, 24 for demands 0.5, 0.4, 0.38, 0.36, 0.34, 0.32, 0.3, 0.2). Those do not match any of the rules 1, 2 or 3 (rule 1 gives 160 failure months at 0.5; rule 2 gives 331; rule 3 gives 159). The no-restriction columns of that sheet reproduce (7, 2, 1, 0, … failure months) apart from not having a 0.37 row. Fix in the workbook: replace the Rule columns with the Sens values, and add a 0.37 row (one failure month on series 1; October 1992).
- Without restriction the yield is 0.36 Mm³/a with the lowest usable storage of 0.166 Mm³ and 0.44 Mm³/a with none (one failure month at 0.45); recomputed.

## 6. Other article items found during the checks
- Table 6 of the article: inflow 3.33 and change in storage +0.36 for 1987–2009 and 1987–1995; recomputed values are 3.32 and +0.35. Version 10 uses the recomputed values.
- Article line 1340: "about 1.9 years once evaporation and the release are included"; recomputed 1.8 (1.76 with the release table, 1.70 with the recorded release).
- Article line 1389: "mean of 1.27 Mm³/a in 1966–1990" for the Wilgeboomspruit; version 10 gives 2.1 Mm³/a for December 1965 to January 1984 (162 valid months), which is the period before the dry spell; the two figures cover different periods.
- Article line 1454–1455: "one month already fails at 0.38 Mm³/a"; version 10 says no failure at 0.36 and one at 0.37.
- Statements in the Abstract, Introduction and Conclusions that quote "ten years" for the shortfall run need the same change as 6.2 if the thirteen-year run is kept.
