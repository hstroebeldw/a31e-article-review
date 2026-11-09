# Number check: article (corrected) against the Excel workbooks

Scope: every number in `/home/claude/article/corrected.txt` that can be traced to the workbooks in `/home/claude/workbooks/extracted/A31E_Workbooks_latest/`.
Read-only: no article or workbook was modified. Cached values were read with `python3 -I` + openpyxl `data_only=True`. Where a figure needed a recalculation (demand changes, switch changes), a **copy** of the workbook was recalculated with LibreOffice (copies in `/home/claude/work/tmp/`, scripts in `/home/claude/scripts/`). Page numbers are the printed page numbers of the article PDF.

Abbreviations: **sw1** = `..._sw1.xlsx` (Params!B9 = 1, inflow as recorded); **sw2** = `..._sw2.xlsx` (Params!B9 = 2, adjusted inflow). "Rule" = with the restriction rule (Run_Ref, Run_A, Run_B ...); "N" = no restriction (Run_*_N). Case M sits in the sheets named Run_A / Run_A_N; case D in Run_B / Run_B_N.

## 0. Headline findings

1. **Every figure that depends on the inflow switch reproduces on sw1, none on sw2.** This covers Table 7, Table 10, the 21.9 Mm³ event total, the 0.48 / 0.27 mean shortfall, the 59% share in Figure 14's text, the 0.36 firm yield and the 8% failure at 1.5 Mm³/a. WHICH_FILE_IS_LATEST.txt says that sw2 is the one in the Block 3 results table 49a, but the article's numbers are the sw1 numbers (details in section 2). The article never states which inflow series Tables 7 and 10 use, and the result of the adjusted-series check (sw2) is not reported in Section 6.
2. The sw2 workbook is internally mixed: its sheets Sens, FirmYield and Graphs 4 hold **stored sw1 values** (the Sens reference row reads 0.5901 in the sw2 file while its own RRV reads 0.5878).
3. Table 6 and the surrounding text use three different inflow bases (see section 3, items T6-1 and T6-9).
4. A handful of text numbers do not reproduce as worded (section 4).

## 1. Main table

Status key: MATCH = reproduces to the precision printed (rounding only); MISMATCH = does not reproduce as worded; CANNOT REPRODUCE = source not in the workbooks; AMBIGUOUS-SERIES = reproduces on one series but the article does not say which / sentence mixes series.

### 1A. Table 6, water balance 1987–2009 (p. 33) and text of Section 6.2 (p. 32–33)

The inflow terms of 1987–2009 are identical in sw1 and sw2 (the adjusted series only differs before Feb 1987), so Table 6 is **switch-independent** (verified: Inputs!AT = Inputs!AZ for all months from hydrological year 1987). Values below are recomputed from sheet Inputs (monthly records), per hydrological year, means over the period.

| ID | Item | Article | Workbook (sheet/column; value) | Switch | Status | Note |
|---|---|---|---|---|---|---|
| T6-1 | Inflow 1987–2009 | 3.33 | Whole-period closure: dS + irrigation col + spill + A3H030 + evaporation + losses − rain = **3.3247**. Monthly inflow series (Inputs!AT, used by every run; Check!C35) = **3.3931**. Record inflow column (Inputs!AA) = 3.1913. WR2012 patched (Inputs!AC) = 3.8026 | none | MATCH within 0.005 on closure (3.32 vs 3.33); AMBIGUOUS-SERIES | Check!F35 says "Table 8 gives 3.33 from whole-year closure". 3.33 comes from Phase 3 Table 8; the workbook closure gives 3.32. The series the model runs use is 3.39 (1.8% higher). Table 6 does not say which basis it uses. |
| T6-2 | Inflow 1987–1995 | 1.23 | closure 1.2340; Inputs!AT 1.2347 | none | MATCH | both bases agree here |
| T6-3 | Inflow 1996–2009 | 4.67 | closure 4.6688; Inputs!AT 4.7807 | none | MATCH (closure) | monthly series would give 4.78 |
| T6-4 | Rain on surface 87–09 / 87–95 / 96–09 | 0.42 / 0.24 / 0.53 | Inputs!X (record): 0.4173 / 0.2390 / 0.5319 | none | MATCH | the model uses zone A3B × area (Inputs!BB): 0.459 / 0.234 / 0.604, not shown in the table |
| T6-5 | Evaporation | 1.23 / 0.74 / 1.55 | Inputs!V (record): 1.2300 / 0.7382 / 1.5461 | none | MATCH | model evaporation (Inputs!BA) 1.328 / 0.714 / 1.723 not shown |
| T6-6 | Canal | 1.20 / 0.30 / 1.78 | Inputs!L (irrigation column of the reservoir record): 1.1969 / 0.2953 / 1.7765 | none | MATCH | this is the reservoir-record column, not gauge A3H031 (Inputs!M: 1.229 / 0.296 / 1.829, 4 gap months). The table caption cites DWA 2012; DWS s.a.b, so fine, but the text calls it "the canal carried" |
| T6-7 | Spill | 0.87 / 0.00 / 1.43 | Inputs!P: 0.8685 / 0 / 1.4269 | none | MATCH | |
| T6-8 | Release to river | 0.33 / 0.07 / 0.49 | Inputs!S (A3H030; 4 blank months = 0): 0.3259 / 0.0702 / 0.4903 | none | MATCH | |
| T6-9 | Change in storage | +0.11 / +0.36 / −0.05 | Inputs!I(last) − H(first): +0.1115 / **+0.3549** / −0.0450 | none | MATCH, one cell off | +0.3549 rounds to +0.35, not +0.36 (0.0051 over the rounding boundary). −0.045 rounds to −0.05 only with round-half-away-from-zero. |
| T6-10 | Closure of the table | (not stated) | Rounded columns: 87–09 in 3.75 / out 3.74; 87–95 in 1.47 / out 1.47; 96–09 in 5.20 / out 5.20 | none | MATCH within 0.01 | The 87–09 column leaves 0.01 because the table has no "losses" row (losses 0.0092 Mm³/a, Inputs!Z) and because of T6-1. The record's own closure residual (Inputs!AG) is −0.074 Mm³/a for 87–09 (−0.122 for 96–09, +0.0006 for 87–95); the 96–09 residual is not discussed anywhere. |
| T6-11 | Evaporation = "a third" of water entering, 87–09; "about half" in 87–95 | one third / half | 1.23/(3.33+0.42) = 0.328; 0.74/(1.23+0.24) = 0.503 | none | MATCH | p. 32 |
| T6-12 | Canal 0.30 in 1987–95 | 0.30 | 0.2953 | none | MATCH | also p. 50 |

### 1B. Table 7, reliability, resilience, vulnerability (p. 36), Reference run, 74 years

| ID | Item | Article rule / N | sw1 (RRV!B / C) | sw2 (RRV!B / C) | Matches | Status |
|---|---|---|---|---|---|---|
| T7-1 | Reliability by time | 0.590 / 0.867 | 0.5901 / 0.8671 (364 / 118 failure months) | 0.5878 / 0.8649 (366 / 120) | **sw1** | MATCH sw1 |
| T7-2 | Reliability by volume | 0.795 / 0.883 | 0.7951 / 0.8832 | 0.7901 / 0.8772 | **sw1** | MATCH sw1 |
| T7-3 | Yearly reliability | 0.446 / 0.770 | 0.4459 / 0.7703 | 0.4459 / 0.7703 | both | MATCH (41 / 17 failure years in both) |
| T7-4 | Shortfall events; longest | 16; 146 / 11; 20 | 16; 146 / 11; 20 | 16; 146 / 11; 20 | both | MATCH |
| T7-5 | Resilience | 0.044 / 0.093 | 0.0440 / 0.0932 | 0.0437 / 0.0917 | **sw1** (sw2 gives 0.044 / 0.092) | MATCH sw1 |
| T7-6 | Vulnerability | 0.50 / 0.88 | 0.496 / 0.879 | 0.506 / 0.911 | **sw1** (sw2 gives 0.51 / 0.91) | MATCH sw1 |
| T7-7 | Mean shortfall (Mm³/a) | 0.48 / 0.27 | 0.4794 / 0.2734 (= (1 − reliability by volume) × 2.34; also sum of Run_Ref!P / 74) | 0.4911 / 0.2874 (0.49 / 0.29) | **sw1** | MATCH sw1. The table has no formula cell for this; it is derived. |
| T7-8 | Check values | (text of the note) failure months 364/118 sw1, 366/120 sw2 | RRV!B7, C7 = 364, 118 | 366, 120 | n/a | MATCH (workbooks confirm the check values; article shows reliability only, not months) |
| T7-9 | Four-fold wording "fails three times as often" (p. 36) | 3× | 364 / 118 = 3.08 | 366 / 120 = 3.05 | both | MATCH |
| T7-10 | Longest event 146 months, Dec 1983 – Jan 1996 (p. 36) | 146; Dec 1983–Jan 1996 | RRV!B27:D27: 1983-12 to 1996-01, 146 months | same dates, 146 | both | MATCH |
| T7-11 | Total shortfall of that event "21.9 Mm³" (p. 36) | 21.9 | RRV!E27 = **21.8577** | **22.5908** (22.6) | **sw1** | MATCH sw1; sw2 would give 22.6 |
| T7-12 | "more than nine times the yearly volume" | >9× | 21.8577 / 2.34 = 9.34 | 9.65 | both | MATCH |
| T7-13 | "includes 40% of all failure months" | 40% | 146 / 364 = 40.1% | 146 / 366 = 39.9% | both | MATCH |
| T7-14 | "full registered volume in 59% to 87% of the months, year without shortfall in 45% to 77% of years" (p. 36; abstract; p. 55; p. 56) | 59–87%, 45–77% | 59.0 / 86.7; 44.6 / 77.0 | 58.8 / 86.5; same years | months: **sw1** (59 / 87); sw2 gives 59 / 86. Years: both | MATCH sw1 |
| T7-15 | "failure month still brings half of the registered volume" / "almost nothing" | 0.50 / 0.88 | vulnerability 0.496 / 0.879 | 0.506 / 0.911 | sw1 | MATCH |
| T7-16 | "Without restriction, the same drought breaks into separate events of 11 to 20 months" (p. 36) | 11 to 20 | RRV!D34:D38 (five longest): 20, 18, 18, 14, 11. Full event list of Run_Ref_N inside the drought: 7 (Aug 1985), 7 (May 1986), 11, 18, 14, 18, 20, 5 (Jul 1995) | same | both | **MISMATCH (minor)**: three further events of 5 to 7 months occur inside the same drought window; "11 to 20" is only the five longest events of the whole record |

### 1C. Table 10, climate cases (p. 43) and Section 6.6 text

Case M = Run_A / Run_A_N (inflow ×0.93, evaporation and demand ×1.064); case D = Run_B / Run_B_N (×0.80, ×1.064). Reliability is against the raised demand (2.34 × 1.064 = 2.490 Mm³/a), as Section 5.4.4 says.

| ID | Item | Article (rule / N) | sw1 | sw2 | Matches | Status |
|---|---|---|---|---|---|---|
| T10-1 | Reliability by time M | 0.541 / 0.829 | 0.5405 / 0.8288 (RRV!D8, E8) | 0.5327 / 0.8243 | **sw1** | MATCH sw1 |
| T10-2 | Reliability by time D | 0.477 / 0.791 | 0.4775 / 0.7905 (RRV!F8, G8) | 0.4741 / 0.7872 | **sw1** | MATCH sw1 |
| T10-3 | Yearly reliability M | 0.405 / 0.703 | 0.4054 / 0.7027 | 0.3919 / 0.7027 | **sw1** | MATCH sw1 |
| T10-4 | Yearly reliability D | 0.324 / 0.635 | 0.3243 / 0.6351 | 0.3243 / 0.6351 | both | MATCH |
| T10-5 | Mean shortfall M | 0.60 / 0.36 | 0.6023 / 0.3626 (sum of Run_A!P / 74) | 0.6179 / 0.3761 | **sw1** | MATCH sw1 (measured against the raised demand) |
| T10-6 | Mean shortfall D | 0.70 / 0.44 | 0.6965 / 0.4411 | 0.7110 / 0.4525 | **sw1** | MATCH sw1 |
| T10-7 | Longest event M, D | 148 / 35; 163 / 35 | 148 / 35; 163 / 35 | same | both | MATCH |
| T10-8 | Reference row | 0.590 / 0.867; 0.446 / 0.770; 0.48 / 0.27; 146 / 20 | as T7 | | sw1 | MATCH sw1 |
| T10-9 | Groundwater columns (9.86, 0.63, −3.8%, −5%, −10.5%, −14%) | | not in these workbooks | | | CANNOT REPRODUCE (MODFLOW output) |
| T10-10 | Text p. 42: "decreases by 5 points with the rule and 4 without in M; 11 and 8 in D" | 5, 4, 11, 8 | 4.96, 3.83, 11.26, 7.66 | 5.5, 4.1, 11.4, 7.8 | both round the same | MATCH |
| T10-11 | "full yearly volume in about seven of ten years in M, fewer than two of three in D, three of four in Reference" (N run) | 0.70, 0.635, 0.77 | 0.703, 0.635, 0.770 | same | both | MATCH |
| T10-12 | "with the rule case D lies 6 points below M, more than M lies below the Reference run" | 6 vs 5 | 0.5405 − 0.4775 = 0.063; 0.5901 − 0.5405 = 0.050 | 0.059; 0.055 | both | MATCH |
| T10-13 | "mean shortfall increases by a quarter to a third in M and a half to two-thirds in D" | 25–33%; 50–67% | M: +25.6% / +32.6%. D: **+45.3% / +61.3%** | M +25.8 / +30.9; D +44.8 / +57.4 | sw1 | MATCH for M; **D wording is loose** (45% to 61% is "nearly a half to three-fifths") |
| T10-14 | "longest event grows from 146 to 163 months; months below half the registered volume 156 to 214 with the rule" | 146→163; 156→214 | RRV!B15, F15 = 146, 163; RRV!B13, F13 = 156, 214 | 146, 163; **159, 219** | **sw1** | MATCH sw1 |
| T10-15 | Figure 14 text p. 43: dam holds ≥ half capacity in ~64% (Ref), 59% (M), 53% (D) of months, with the rule | 64 / 59 / 53 | share of months with storage at start ≥ 0.5 × 7.07 Mm³: Run_Ref 64.3%, Run_A 58.9%, Run_B 53.0% (Graphs 5 interpolates to the same) | 64.0, **58.1**, 52.8 | **sw1** (sw2 gives 58% for M) | MATCH sw1 |
| T10-16 | Recommendations p. 55: "32% to 70% of years under 2050 conditions" | 32–70% | D rule 32.4%; M N 70.3% | same | both | MATCH |
| T10-17 | Table 5 factors (inflow 0.93 / 0.80; evaporation and demand 1.064; recharge 0.96 / 0.89) | | Params!B39:D40 = 0.93 / 1.064 / 1.064 and 0.80 / 1.064 / 1.064 | | | MATCH (inflow and evaporation/demand). Recharge factors and the rainfall/warming derivation are not in the workbooks: CANNOT REPRODUCE. |

### 1D. Firm yield, sensitivities, demand curve (p. 37, abstract, p. 56)

| ID | Item | Article | Workbook | Switch | Status | Note |
|---|---|---|---|---|---|---|
| FY-1 | Firm yield 0.36 Mm³/a; one month fails at 0.38 | 0.36; 0.38 | FirmYield!B12:B13: 1 failure month at 0.38, 0 at 0.36 (typed values). I recalculated copies: sw1 0.36 → 0, 0.37 → 1, 0.38 → 1 failure months | **sw1 only** | MATCH sw1 | On sw2 the same recalculation gives **2** failure months at 0.34 and 0.36, 3 at 0.37 and 0.38, so no firm yield of 0.36 exists on sw2. FirmYield!A7 says "about 0.37" (between 0.36 and 0.38); article says "about 0.36" (the largest tested value with no failure). Fine, but the sheet and article differ in wording. |
| FY-2 | 0.36 / 1.4 = "about a quarter"; 0.36 / 2.34 = "about 15%" (p. 37, p. 56) | quarter; 15% | 25.7%; 15.4% | n/a | MATCH | |
| FY-3 | "at 1.5 Mm³/a the unrestricted canal fails in 8% of months" | 8% | Sens!L39 (stored) = 0.9212 → 7.9% failure. Recalculated on sw2: 0.911 → 8.9% | **sw1** | MATCH sw1 | sw2 would read 9% |
| FY-4 | "Even at 0.5 Mm³/a, the rule leaves reliability by time 0.82 and an event of 128 months" | 0.82; 128 | Sens!L9, N9 (stored, Run_Sens live): 0.8209; 128 | sw1 (stored in both files) | MATCH | **Inconsistency inside the workbook**: FirmYield!H10 gives 0.9133 for the same case (rule, 0.50 Mm³/a, 77 failure months). Reason: changing Params!B6 also refits the rule (Params!H46:H52 are formulas on the Rule sheet that divide delivered by asked-for volume), so the FirmYield rule columns use a different, rescaled rule (0.058 / 0.217 / 0.668 / 1 ... instead of 0.036 / 0.116 / 0.298 / 0.666 ...). The article follows Sens, which keeps the rule at 2.34 Mm³/a. FirmYield's own statement "nothing else was changed" is therefore not true for its "Rule" columns. The article does not use those columns. |
| FY-5 | "0.28 difference between bounds at 2.34 is about as large as raising demand from 0.5 to 3.0" | 0.28 | 0.867 − 0.590 = 0.277. Rule: 0.8209 → 0.5304 (0.29); N: 0.9921 → 0.8041 (0.19) | sw1 | MATCH for the rule; looser for N | |
| SE-1 | Rule fitted on the test period alone: 0.59 → 0.39 | 0.39 | Sens!L33 = 0.3930 | sw1 | MATCH | |
| SE-2 | ±10% evaporation, release: "about 0.02" | 0.02 | Sens!L22 0.5687 (−0.021), L23 0.6092 (+0.019), L25 0.6115 (+0.021), L26 0.5676 (−0.0225) | sw1 | MATCH | |
| SE-3 | capacity −10%, seasonal pattern: "<0.01" | <0.01 | +0.0045; −0.0090 | sw1 | MATCH | |
| SE-4 | N: largest change 0.02 from higher lowest usable storage | 0.02 | Sens!L55 0.8468 vs 0.8671 = −0.0203 | sw1 | MATCH | |
| SE-5 | Doubtful years lower reliabilities "by at most 0.05" | 0.05 | RRV rows 8, all 74 years minus without 1975–1980: largest drop 0.0484 (case S rule); Ref rule 0.036 | both (sw2 largest 0.0486) | MATCH | |
| SE-6 | Figure 13 caption: mean shortfall "0.27–0.70" for Reference, M, D, both bounds; longest-event rate "1.80–2.05" | 0.27–0.70; 1.80–2.05 | 0.2734 … 0.6965; 21.8577 / (146/12) = 1.797 and 3.4249 / (20/12) = 2.055 | sw1 | MATCH | 2.055 rounds to 2.06 at two decimals (printed 2.05) |
| SE-7 | p. 42: "mean shortfall 0.27 to 0.48 = 1.6% to 2.8% of the modelled recharge; registered volume 13.5%" | 1.6–2.8%; 13.5% | 0.2734 / 17.336 = 1.58%; 0.4794 / 17.336 = 2.77%; 2.34 / 17.336 = 13.50% | sw1 | MATCH only against the **Reserve recharge 17.336**, not the "modelled recharge" 17.53 (Table 8): against 17.53 the figures are 1.6%, 2.7% and 13.3% | |
| SE-8 | p. 42: equals the yield of "29 to 51 boreholes at 0.3 L/s" | 29–51 | 0.2734 Mm³/a = 8.67 L/s → 28.9; 0.4794 → 15.2 L/s → 50.7 | sw1 | MATCH | |
| SE-9 | Figure 11 data (demand curve 0.5–3.0; vertical lines 2.34, 2.73) | | Sens rows 9–20 and 34–46 (stored), Graphs 4 | sw1 (stored) | MATCH (the 2.73 Mm³/a case exists as Sens 12 and 38) | graph itself cannot be checked |

### 1E. Test of the model (Section 5.4.1, 6.3; p. 35)

| ID | Item | Article | Workbook (Run_Test!AU11:AW13, AV/AW/AF/AG) | Switch | Status |
|---|---|---|---|---|---|
| TE-1 | NSE, RSR, PBIAS monthly storage | 0.86, 0.37, +7.4% | 0.8636, 0.3693, +7.42% (AU11:AU13) | none (Run_Test X3 = 1 in both files) | MATCH |
| TE-2 | Yearly canal | 0.60, 0.64, −22.4% | 0.5953, 0.6362, −22.36% (AW11:AW13) | none | MATCH |
| TE-3 | Monthly canal "does not meet" | does not | NSE 0.378, RSR 0.789, PBIAS −17.2% (AV11:AV13); Check!C54 "no" | none | MATCH |
| TE-4 | "balance finds shortfall in 192 of the 265 months against 216 in the record" | 192 / 265 / 216 | sums of Run_Test!AG, AD, AF: 192 / 265 / 216 | none | MATCH |
| TE-5 | "delivers 22% more water than the canal carried" | 22% | PBIAS of yearly canal −22.36% | none | MATCH |
| TE-6 | Rule shares "from 0.036 in the lowest zone to 1.00 above 57%" | 0.036; 1.00 | Params!H46 = 0.0360; H51 = 1 (57% zone) | none | MATCH |
| TE-7 | 843 / 27 / 18 months; 888 months | 843, 27, 18 | Check!C26:C28 | none | MATCH |
| TE-8 | 259 months without spill (Fig. 2 caption) | 259 | Check!C42 | none | MATCH |
| TE-9 | 0.166 Mm³ lowest storage on record | 0.166 | Params!B5; Data_25 Nov 1992 = 166 Ml | none | MATCH |
| TE-10 | Capacity 7.07 Mm³; start storage; "about three years of the registered volume, 1.9 years with evaporation and release" | 7.07; 3; 1.9 | Params!B4; 7.07 / 2.34 = 3.02; 7.07 / (2.34 + 1.07 + 0.33) = 1.89 | none | MATCH |

### 1F. Records, inflow and climate statistics (Sections 1.1, 5.1, 5.2, 6.1, 6.2, 7)

| ID | Item (page) | Article | Workbook / recomputation | Series | Status | Note |
|---|---|---|---|---|---|---|
| R-1 | Inflow median 3.94 (p. 32, Fig. 6 caption) | 3.94 Mm³/a, 1936–2009 | Median of yearly sums of WR2012 patched flow (Data_26 col C, = Inputs!AC) = **3.945** | patched | MATCH (3.945 prints as 3.94 or 3.95) | Series 1 (as recorded, rebuilt) median is 3.708 (Q1!C107, labelled "for comparison with the WR2012 patched flow (3.94)"). The text says the patched flow, so 3.94 is right. |
| R-2 | "inflows of 2.14 and 0.59 Mm³ in 1982 and 1983" (p. 33) | 2.14; 0.59 | Patched flow: 2.14, 0.59. Series 1: 2.121, 0.637 (Q1!B53, B54) | patched | MATCH (patched) | |
| R-3 | "stayed below this median from 1982 to 1994" | 1982–1994 | patched: 1982–1994 all below 3.945, 1981 and 1995 above; series 1 (median 3.708): same years (Q1!Q) | both | MATCH | |
| R-4 | "over the ten years 1985–1994 it averaged **0.84** Mm³/a, about a third of the registered volume" (p. 32) | 0.84 | Series 1 (recorded + rebuilt): Q1!P65 = **0.8406**. WR2012 patched flow (the series the sentence is about): **1.013** | series 1, not patched | **MISMATCH / AMBIGUOUS-SERIES** | The sentence begins "The inflow ... taken as the WR2012 patched observed flow" and then says "it averaged 0.84". Patched gives 1.01 (43% of the registered volume, not "a third"). 0.84 / 2.34 = 36%. |
| R-5 | Dam 99% in Dec 1982 → 22% Mar 1984 (p. 33) | 99%; 22% | Data_25 col V: 99.3% (Dec 1982), 21.9% (Mar 1984) | n/a | MATCH | |
| R-6 | "below 25% in 139 of 144 months, Oct 1983 – Sep 1995" (p. 3) | 139 / 144 | Data_25 col V: 139 of 144 | n/a | MATCH | |
| R-7 | "During these years the canal carried a mean of **0.25** Mm³/a" (p. 3), same Oct 1983 – Sep 1995 window | 0.25 | Oct 1983 – Sep 1995 (hydrological years 1983–1994): **0.360** (months without gap code) or 0.369 (all printed values). 0.25 = mean of the counted years among hydrological years 1984–1995 (11 years, 1994 not counted): Q1 G, J columns → 0.2537 | n/a | **MISMATCH of window; value reproduces for another window** | chat4/chat2 record that the canal window is Oct 1984 – Sep 1996 and the storage window Oct 1983 – Sep 1995; the sentence in 1.1 pairs the 0.25 with the storage window. |
| R-8 | "median of 2.02 Mm³/a over 72 years of record" (p. 3) | 2.02; 72 | Q1: 72 counted years (J = 1, 1936–2024), median of G = 2.022 | n/a | MATCH | 1997–2014 mean 1.97 over 13 counted years also reproduces (not in article) |
| R-9 | "rainfall of 1986–1995 averaged 99% of its long-term mean" (p. 3) | 99% | zone A3B, hydrological years 1986–1995: 593.9 mm vs 1920–2009 mean 599.0 = 99.2% | n/a | MATCH | |
| R-10 | "Every year 1981–1986 below the long-term mean, longest such run since 1920" (p. 31) | six years | zone A3B: all six below 599.0; longest run in 1920–2009 is 6 (ends 1986) | n/a | MATCH | |
| R-11 | Station rainfall "varied between 314 and 900 mm in 1967–2008"; 1975 left out (Fig. 4) | 314–900 | A3E003 complete hydrological years 1967–2008: 314 (2006) to 900 (1980); 1975 = 1619 mm because Aug 1976 = 669.9 mm | n/a | MATCH | |
| R-12 | "93% of the rain falls October–April" (p. 31) | 93% | station A3E003 1967–2014 excluding doubtful months: 92.9%; including them 90.6%; zone A3B 92.0% | n/a | MATCH (with doubtful months excluded) | |
| R-13 | "S-pan evaporation averages **2 005** mm/a" (p. 32) | 2 005 | Sum of the twelve Figure B means = **1 993.8** (Params!C34, Check!C20); without part-months 2 007.0 (Params note N23); mean of 43 complete years = 1 977 | n/a | **MISMATCH (small)** | 2 005 is an earlier figure from the chat history (chat2 line 1384); neither 1 993.8 nor 2 007 equals it. |
| R-14 | "exceeds the rainfall in every month" | yes | station pan > station rain in all 12 months (smallest margin 89 mm, Feb–Mar) | n/a | MATCH | |
| R-15 | Reservoir "loses a mean of **1.07** Mm³/a to evaporation over 1936–2010, and about 2.0 when nearly full" (p. 32) | 1.07; 2.0 | Inputs!V mean over 888 months 1.0673 (Data_25 1.0695). Hydrological years 2000 and 2001: 1.997 and 2.067 | n/a | MATCH | "nearly full" is two named years, not a defined storage threshold (months ≥ 95% full average 1.60 Mm³/a-equivalent) |
| R-16 | Pan factors "0.82 to 0.89", back-calculated | 0.82–0.89 | Params!E22:E33 = 0.82, 0.83, 0.84, 0.84, 0.88, 0.88, 0.89, 0.87, 0.85, 0.84, 0.82, 0.82; medians recomputed from PanFactor!N:Y reproduce them (0.8179 … 0.8851) | n/a | MATCH | |
| R-17 | Canal "1.89 to 2.19 Mm³/a in 2022–2024" (p. 31) | 1.89–2.19 | Hydrological years: 2022 = 1.888 (12 months, counted); 2023 = 2.186 using all printed values (2.019 over the 10 months without gap code; year NOT counted, Q1!J94 = 0); 2024 = 2.161 (counted) | n/a | MATCH, but under the study's own counting rule the range is **1.89–2.16** | 2.19 includes two part-months that carry gap codes, the rule Sections 5.1 and 5.2.1 state for everything else. |
| R-18 | Counted years: "38 countable years of the raised dam; shortfall in 24 (63%); mean shortfall 58%; longest run 10 years 1984–1993" (p. 33) | 38; 24; 63%; 58%; 10 | Q1!C111:C118: 38; 24; 0.6316; 1.3462 / 2.34 = 57.5%; 10 (runs M55:M64 = 1984–1993) | n/a | MATCH | |
| R-19 | "in five of the shortfall years the dam never fell below 75% of capacity" (p. 33, 49) | five | Q1!E for shortfall years 1966–2009: 1974 (75.5), 1977, 1979, 2000 (75.5), 2001 | n/a | MATCH | |
| R-20 | Calculated inflow of 1975–1980 "totals 296 Mm³ against 186 at Kromellenboog" (p. 20) | 296; 186 | WR2012 patched A3R002 1975–1980 = 296.28; patched A3R003 = 185.69. (Series 1 gives 300.5; Data_25 Kromellenboog inflow column 171.1) | patched | MATCH (patched series) | the sentence says "calculated inflow" but the figure is the WR2012 patched flow |
| R-21 | Hydrological year 1975 "includes an implausible 670 mm in August 1976" | 670 | Data_17: 669.9 mm | n/a | MATCH | |
| R-22 | MAP 597 mm; naturalised runoff 7.21 Mm³/a (Section 2) | 597; 7.21 | Data_09 MAP 596.7; Data_08 mean 1920–2009 = 7.213 | n/a | MATCH | |
| R-23 | About a third of the volume falls June–September (Fig. 3) | a third | Params!H30:H33 sum = 0.317 | n/a | MATCH | |
| R-24 | Wilgeboomspruit: 53 mm/a = 7.6% of rainfall 1966–1980; mean 1.27 Mm³/a 1966–1990; dry in 42 of 50 months from Feb 1984; flowed again from April 1988 (pp. 31, 34) | as stated | Data_34 complete gap-free years: 1966–1980 six years mean 2.074 Mm³/a / 39 km² = 53.2 mm, 7.59% of zone rainfall; 1966–1990 twelve years mean 1.267 (median 0.686); Feb 1984 – Mar 1988: 42 zero months of 50; first flow Apr 1988 | n/a | MATCH | These need the "complete gap-free years only" rule, which the article does not state for these figures (all-month means give 1.30 and 48 mm). |
| R-24b | "It flowed again from April 1988, but at **a third** of its former mean" (p. 34) | one third (about 0.42 Mm³/a) | Data_34: April 1988 – August 1992 annualised mean 0.68 Mm³/a (54% of 1.27); hydrological years 1988–1990 mean 0.78 (all values) | n/a | **MISMATCH / CANNOT REPRODUCE** | Only the 1986–1987 years (0.476 Mm³/a, 37% of 1.27) are near a third, and those precede April 1988. |
| R-25 | Kromellenboog / reach (Q2, p. 34): 5.01 of 6.21 Mm³/a (81%); 3.80 vs 5.80; reach supplied 98%; positive every year; rank correlation 0.76; naturalised runoff about twice the net contribution | as stated | Q2!D39:F46, D44:F44: 6.2088, 5.0143, 0.8076; 3.7979 / 5.7964; 0.9818; D55 = 0 negative years; D56 = 0.7623 (21 years, balance basis); naturalised 7.4156 vs 3.7979 = 1.95 | none | MATCH | The Check sheet quotes a different correlation, 0.85 (22 years, patched-flow basis, Q2!E56 = 0.8487). The article correctly uses the balance basis 0.76, but the basis is not named. |

### 1G. Gauge data quality (Tables 1, 2, 3, p. 17–18)

Workbook: `A31E_Gauge_data_quality_tables.xlsx` (Table A = article Table 2; Table B = article Table 3). I also recounted the quality codes from Data_17 and they agree with Table A (e.g. canal 73.8 / 1.11 / 9.63 / 3.52 / 1.30%; H042 Data missing = 35.06 + 1.15 = 36.2%).

| ID | Item | Article | Workbook | Status |
|---|---|---|---|---|
| G-1 | Table 2, 126 cells (21 codes × 6 columns) | printed to 0.1% | Table A!B3:G23 × 100 | **MATCH for 122 cells; 4 cells differ by 0.05–0.1 in the last digit** (S-pan "Good monthly reading" 0.2 vs 0.145; S-pan "Negative" 0.2 vs 0.145; canal "Audited gauge plate readings" 0.7 vs 0.648; spill "Checked estimate – still unaudited" 0.7 vs 0.648). All four are single months (1/689, 1/689, 7/1080, 7/1081) rounded up. Column sums in the article: 100.1 / 100.0 / 100.0 / 100.0 / 100.1 / 100.2. |
| G-2 | Table 3, 68 cells | 0.1% | Table B!B3:E19 × 100 | **MATCH for 66 cells; 2 cells differ by 0.05** (A3H033 "Audited gauge plate readings" 1.1 vs 1.049; A3R003 "No info for stage/discharge" 0.4 vs 0.350). |
| G-3 | Months per record (1 081, 1 080, 292, 174, 690, 689, 321, 858, 858, 560) and Table 1 ranges | as stated | Table A row 24, Table B row 20; Data_17/34 first and last dates reproduce every range (e.g. A3H030 1987/02–2011/05, S-pan 1967/10–2025/02, Data_25 894 months to 2010/11, zone A3B 1 080 rows) | MATCH |
| G-4 | Text: "about 74% good continuous (spill, canal)", "S-pan 37.0% good continuous and 43.5% estimates", "A3H042 5.2% good continuous" | 74; 37.0; 43.5; 5.2 | 73.7 / 73.8; 37.0; 40.1 + 3.5 = 43.5 (exact 43.54); 5.2 | MATCH |

### 1H. Geology, dolomite and flood workbooks

| ID | Item | Article | Workbook | Status |
|---|---|---|---|---|
| GE-1 | "Catchment above the reach is underlain for 46.4% by dolomite of the Malmani Subgroup, all of which lies above Klein Maricopoort Dam" (p. 44; 7.4 "nearly half") | 46.4% | 49e, sheet "Dolomite formations": total dolomite 629.59 km², P2 share 46.4% (P2 = catchment at F2, 1 357 km²; 629.59 / 1357.1 = 46.4%). P1 (catchment of the dam) share 54.2%, same 629.59 km², so all dolomite lies above the dam. Sheet "Hydrogeological units": P1 sums to 1 162.0 km², P2 to 1 357.1 km². | MATCH. The article does not say that 46.4% refers to plan P2 and that 54.2% applies to the dam's own catchment. |
| GE-2 | A31E contains no dolomite | none | "Hydrogeological units" P3 karstic dolomite = 0 | MATCH (P3 is presumed to be A31E or the model area; the workbook does not label P3) |
| GE-3 | Peak inflows to the model, Table 11 "Peak in": 972, 1 250, 887 m³/s | 972 / 1 250 / 887 | design_hydrographs_15min.xlsx peaks: Q50_SDF 972.2, Q100_SDF 1 249.7, Q100_MP 887.4 | MATCH |
| GE-4 | Table 11 "Design peak": 974, 1 252, 889 m³/s | 974 / 1 252 / 889 | not in the hydrograph workbook; the hydrographs peak 1.6–2.3 m³/s lower (15-minute sampling puts the maximum at 16.5 h, the time of concentration is 16.4 h; base flow 5 m³/s) | CANNOT REPRODUCE directly; hydrographs consistent to 0.2% |
| GE-5 | Triangular hydrograph rises over one T_c (16.4 h) and falls over two | 16.4 h | rise 0 → 16.5 h, fall to base flow at 49.25 h (= 16.5 + 2 × 16.4 = 49.3) | MATCH |
| GE-6 | Percent arithmetic in the text: SDF exceeds Midgley and Pitman by 41%; M&P = 71% of SDF; M&P peak 29% lower; 0.25 km² more land; 3.3% reduced | 41%, 71%, 29% | 1 252 / 889 = 1.408; 889 / 1252 = 0.710; 887.4 / 1 249.7 = 0.710 → 29.0% lower; 7.97 − 7.72 = 0.25 | MATCH (arithmetic on the table's own values) |
| GE-7 | Reach length 15.7 km | 15.7 km | 49h River_Long: 525 stations at 30 m, last station 15 720 m | MATCH |
| GE-8 | Flood profile numbers | none in the article text | 49h River_Long (max depth 1.19 – 6.67 m, mean 3.53 m; water surface falls 52.6 m, no upward step; bed 1 115.3 → 1 061 m) and XS_1 to XS_3 (max depths 2.75, 4.50, 2.82 m) | The article quotes no number from these profiles; no check needed. |
| GE-9 | Peak out, peak reduced, flooded km², deeper than 1 m, cultivated land flooded, 14–16% volume held, 44 / 38 ha irrigated | | 49f, 49g, 49i, 49j are csv/txt and are not in the set | CANNOT REPRODUCE |

## 2. Which inflow series does each figure belong to?

| Quantity | sw1 | sw2 | Article uses |
|---|---|---|---|
| Table 7 (all cells that differ) | 0.590 / 0.867 / 0.795 / 0.883 / 0.093 / 0.50 / 0.88 / 0.48 / 0.27 | 0.588 / 0.865 / 0.790 / 0.877 / 0.092 / 0.51 / 0.91 / 0.49 / 0.29 | **sw1** |
| Event total, Reference rule | 21.86 | 22.59 | **sw1** (21.9) |
| Failure months | 364 / 118 | 366 / 120 | not printed; 40% consistent with both |
| Table 10 M and D | 0.541 / 0.829, 0.477 / 0.791, 0.405 / 0.703, 0.60 / 0.36, 0.70 / 0.44 | 0.533 / 0.824, 0.474 / 0.787, 0.392 / 0.703, 0.62 / 0.38, 0.71 / 0.45 | **sw1** |
| Share of months ≥ half capacity, M | 58.9% | 58.1% | **sw1** (59%) |
| Months below half the registered volume, rule: Ref, D | 156, 214 | 159, 219 | **sw1** |
| Firm yield 0.36 / failure at 0.38 | 0 / 1 | 2 / 3 | **sw1** |
| 1.5 Mm³/a, N fails in | 7.9% | 8.9% | **sw1** (8%) |
| Test (NSE, PBIAS), Table 6, Q1, Q2 | independent of the switch | | not applicable |
| Sens, FirmYield, Graphs 4 (demand curve) | stored, sw1 | stored, **still sw1** | sw1 |

Consequence for the author: if Table 49a (Block 3) was produced from the sw2 workbook, the article text does not follow it. Either the article is right (sw1 primary series, which is also what Sens, FirmYield and Fig. 11 hold) and the note in WHICH_FILE_IS_LATEST.txt is wrong, or the article should move to sw2 and about 25 numbers change (list above). The adjusted-series check promised in Section 5.4.1 ("run as a check") has no reported result in Section 6; Sens scenario 13 holds it (0.5878 / 0.7901 / 146 months / 22.6 Mm³).

## 3. Notes on Table 6 (not errors, but the author should decide)

- T6-1 / T6-9: "Inflow from the river (remainder)" is the whole-year closure of the record (3.33 in the article, 3.32 in the workbook). The monthly inflow series that drives every simulation averages 3.39 for the same years. Chat history (chat3 line 1590; chat4 line 1026) shows the author was told to name both and say why they differ; Section 6.2 and Table 6 name only 3.33.
- The table has no "losses" row (0.009 Mm³/a) and no residual row; the 1987–2009 column therefore closes to 0.01 and not exactly.
- The residual of the recorded balance in 1996–2009 (−0.122 Mm³/a, Inputs!AG) is larger than any displayed term except the change in storage; the table does not show it. The closure used for inflow absorbs it.

## 4. Mismatches and ambiguities, ranked by importance

1. **Switch (sw1 vs sw2).** All switch-dependent numbers reproduce on sw1 only (section 2). Conflicts with the note in WHICH_FILE_IS_LATEST.txt. The article does not say which inflow series Tables 7 and 10 use. Decision needed: keep sw1 and say so, and report the sw2 check in Section 6; or move to sw2.
2. **R-4: the 0.84 Mm³/a (1985–1994) is series 1, but the sentence is about the WR2012 patched flow.** Patched flow gives 1.01 Mm³/a (43% of the registered volume, not "about a third"). Also affects the same sentence's 3.94 and the 2.14 / 0.59 (patched) next to it.
3. **R-7: canal mean 0.25 Mm³/a is given for October 1983 – September 1995 (p. 3), but that window gives 0.36.** 0.25 is the mean of the 11 counted years among hydrological years 1984–1995.
4. **Table 6 inflow basis (T6-1, T6-9).** 3.33 / 1.23 / 4.67 are whole-year closures; the workbook closure is 3.32 (not 3.33) and the series used by the model is 3.39 / 1.23 / 4.78. The ΔS of the drought column is +0.35 in the workbook (+0.36 printed).
5. **R-13: S-pan 2 005 mm/a** is not in the workbook (1 993.8 in Figure B; 2 007 without part-months).
6. **R-17: canal range 1.89–2.19** uses a year (2023) that the study's own counting rule excludes; counted years 2022 and 2024 give 1.89–2.16.
7. **T7-16: "separate events of 11 to 20 months"** inside the drought; the unrestricted run has three more events of 5–7 months inside the same window.
8. **SE-7: "1.6% to 2.8% of the modelled recharge"** is computed against the Reserve recharge 17.336, not the model's 17.53 (which gives 1.6% and 2.7%; registered volume 13.3%).
9. **T10-13: "a half to two-thirds" for case D** is 45% to 61% on the workbook.
10. **R-24b: "a third of its former mean"** (Wilgeboomspruit after April 1988): April 1988 – August 1992 annualised 0.68 Mm³/a, hydrological years 1988–1990 0.78 Mm³/a, against 1.27, i.e. 54% to 61%, not a third (0.42). Computed from Data_34; the statement is not tied to a workbook cell.
11. **G-1 / G-2:** six gauge-table cells differ by 0.05–0.1 from the workbook in the last printed digit (single-month categories rounded up).
12. **FY-4: workbook inconsistency** between FirmYield "Rule" columns and Sens (rule refits when Params!B6 changes). The article uses Sens, so the article is unaffected; the FirmYield sheet text ("nothing else was changed") is wrong for those columns.
13. **GE-1:** 46.4% belongs to plan P2 (catchment at F2); the dam catchment (P1) is 54.2%. The article does not name the plan.

## 5. What could not be checked, and why

- Groundwater results (Tables 8, 9, 10 groundwater columns, Figure 13 curves, Map 7, Map 8, recharge factors, Table 4 borehole data, Section 5.2.2 and 5.4.2 numbers): MODFLOW / MODPATH outputs (49b, 49c) are csv/txt and not in the workbook set.
- Flood routing results (Table 11 peak out, flooded area, depth classes, cultivated land flooded, volume held, 44 and 38 ha): 49f, 49g, 49i, 49j are csv/txt and not provided. Only the inflow peaks (design hydrograph workbook) and the percent arithmetic could be checked. Design peaks 974 / 1 252 / 889, T_c, SDF region and RMF values come from the SANRAL calculation, not from a workbook.
- Water-quality screening (Table 12, Figure 15, EC / sulphate medians, 49d): csv, not provided.
- Land cover, soils, geology shares of A31E (31.8%, 24.4%, 20.9%, 22.5%; 59.8% / 40.2%; 91.6%; 83.2%; 168 ha; 145 ha; 442 ha; 0.285 and 3.38 Mm³/a registered; borehole counts and yields): GIS and WARMS data, not in the workbooks. Only Params!B6 = 2.34 (registered volume) is in the water-balance file.
- Evaporation zone 1 901 mm, Bailey & Pitman 2016 and DWAF 2004 values (1.4 Mm³/a yield), climate-model percentiles (Table 5 rainfall and warming, elasticity 2.0–2.5): external sources.
- Figures 4–11 and 14 as images: the series behind them are in sheets Graphs, Q1 and Q2 (checked where the article states a number from the figure), but the plotted images were not compared.
- Water-balance numbers rely on cached values; I recalculated copies of the workbooks in LibreOffice for the demand and switch variations (FY-1, FY-3, FY-4). A baseline recalculation reproduced the cached RRV exactly (364 / 118 / 408 / 152 ...), so the recalculation is trustworthy, but it is not Excel itself.
- Two items rest on chat history rather than a workbook cell: the origin of 2 005 mm/a (R-13) and the definition of the 0.25 window (R-7).
