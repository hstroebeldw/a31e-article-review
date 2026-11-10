# A31E article: hand-over for a new chat (10 November 2026)

Author: LH Stroebel (Heindrich), NWU Honours. Supervisor: Sascha Roopa. Meeting with Sascha 10 Nov 2026; article due 17 Nov 2026.
Start a new chat by attaching this zip and saying: "Read HANDOFF_FOR_NEW_CHAT.md and CLAUDE.md first."

## 1. Rules (from CLAUDE.md, still in force)
- The author decides every interpretation. State findings and options; never present a new interpretation as settled.
- Cite only sources that were opened and read. Mark anything unverified as "unverified". Never invent a reference, page, DOI or number.
- Recompute numbers with code (openpyxl, data_only=True).
- Do not edit the workbooks or result files in `files/`. Reports go to `reviews/`, drafts to `drafts/`.
- South African/British English, impersonal voice, plain declarative sentences. Results report; the Discussion interprets, has no new results, few numbers, no pointers back.
- The author is tired of questions. Ask as little as possible; put open decisions in one short yes/no list.

## 2. State of the article
- Latest PDF: `drafts/A31E_final_draft_v5.pdf` (v4 = layout and captions; v5 = group A fixes below). Text of v4: `drafts/A31E_final_draft_v4.txt`.
- Layout rules the author set: Arial text (Liberation Sans used, same metrics); each main heading starts a new page; otherwise no large blank gaps; all maps 14 cm wide, same size; charts redrawn in Excel style from workbook data (Figure 1 conceptual model kept as is; Figures 12 and 15 are still old pictures because the data is not in the folder); NWU cover page from the Word document; every figure, map and table sits in the subsection that cites it (checked by script); captions short, with the explanation in a paragraph before the float.
- Discussion: `drafts/Discussion_integrated_v11.md`. Recommendations/Conclusions: `drafts/Recommendations_Conclusions_v5.md` (flood-line recommendation removed; six recommendations).
- The flood line is shown on Map 9, so the text does not "determine" it. The reason the 1:50 and 1:100 lines look alike is for the author only, not for the article: `reviews/Why_1in50_and_1in100_floodlines_look_alike_2026-11-10.md`.

## 3. Earlier author decisions (keep)
Thirteen shortfall years 1984–1996; SDF only for floods; "irrigated land"; no Midgley/Pitman/RMF remarks; SAR 2.0 with its reason; Wilgeboomspruit sentence with Figure 8; Map 9 exported from RAS Mapper and drawn in ArcGIS; Map 5 is the corrected soils map; no mixing check; no 47.5 m; reverse-test rerun for Figure 9; short Discussion citing only Hashimoto et al. (1982), Leake & Barlow (2013), DWAF (2004); Kalkdam above the Doringrivier; Map 10 description stays, without the statement that contaminant transport is not modelled; headings "Pathways" and "The two waters" were revised on 10 Nov.

## 4. Group A fixes applied in v5 (each checked against workbook or result files)
1. Phosphate (6.8): 19% is station A3H042Q01 (74 samples, 2012–2023); A3H030 is 4% (56 samples, 1989–1993).
2. Section 4.3: most rain that does not run off evaporates; a small part recharges the groundwater.
3. Section 1: sentence "sustainable only at a rate balanced by recharge" removed (contradicts Section 3.2 and Leake & Barlow).
4. Section 6.1: 91% is the share of water that would drain if both zones were dewatered (storativity × thickness).
5. Cuthbert et al. (2019) and Xie et al. (2024) wording aligned with their abstracts; De Wit & Stankiewicz step to dam inflow marked as inference.
6. Sensitivity sentence: release test is x0.5 and x1.5 (Sens rows 17–18), not ±10%.
7. 0.166 Mm³: lowest since the survey of 1982. Canal 2022 and 2024: 1.89–2.16 Mm³/a (2023 has part months). Wilgeboomspruit 53 mm/a: six complete years. 296 Mm³ is the patched WR2012 flow.
8. Chloride, sodium, SAR: "none of the samples" (result file 49_Block3: no exceedance at any site).

## 5. Still open: group A items not applied (need a source or the author)
- Recharge 29.2 mm/a does not reproduce (17.53 Mm³/a over 15 142 cells of 0.04 km² gives 28.9 mm/a). The author must check the GMS grid.
- Bailey & Pitman (2016) is cited for 597 mm, 602 km², 1 901 mm and zone A3B; `files/results/wr2012_A31E_row.csv` takes them from the WR2012 quaternary spreadsheet. Cite the dataset.
- Konikow & Leake (2014) "34 systems, 0.61": opened on the publisher page earlier; the citation reviewer saw only abstracts. Re-check if in doubt.
- Table 15: percentages from 1–3 samples (188257, 188038, 188030) should show counts.
- Smithers (2012) wording of method groups and the "conservative" label; Hashimoto vulnerability definition; Moriasi ratings are for monthly steps; DWAF (2004:93) deficit at 1:50 assurance; DWAF 2.6 and 4.4 name different return-flow sources.
- AI declaration page: needs the author's facts and signature.
- Figures 12 and 15: need the GMS export (262 levels) and the DWS water-quality downloads.

## 6. Decisions the author still has to make (group B)
Full list with options and costs: `reviews/A31E_final_draft_v3_review_2026-11-10.md`, section B and F. Main ones:
1. Add the D bound (water from the ground drain, large drawdown, at most 1.2 Mm³/a deliverable) next to the S bound in the Abstract, Discussion, Conclusions and Recommendation 4?
2. Climate cases are measured against a target raised from 2.34 to 2.49 Mm³/a; report both targets?
3. "The water of A31E is fresher": one tributary and seven groundwater samples; name what was measured or drop?
4. Firm yield 0.36 Mm³/a rests on one month (October 1992); compared with DWAF's 1.4, which is not like with like.
5. Causes of the salinity below the dam (return flow, dolomite above the dam, evaporation): list as inference?
6. Statements that D's drawdowns follow from the PEST lower limits, that drains only remove water, and that results are steady state.
7. Travel time: report the spread (shares reaching a river within 1, 10, 50 years) and the porosity range?

## 7. Workflow for the next chat
1. Get the answers to section 6 in one short list.
2. Rewrite only the affected blocks in `drafts/`, keeping the author's tone (see the Introduction in `files/approved_text/`).
3. Run `/review-block` once on the changed sentences only.
4. Rebuild the PDF with the build scripts in `build/` (see `build/README.txt`).

## 8. Folder map
- `context/project_context.md`: facts, numbers, decisions. Read first.
- `files/`: read-only evidence (workbooks, results, GIS, source papers, approved text).
- `drafts/`: all drafts and the PDFs. `reviews/`: all reports (problems list, panel review, flood note).
- `.claude/agents/`: the reviewer agents. `build/`: PDF build scripts and Excel-style figure scripts.
- `transcript/`: full chat record (jsonl) for anything not summarised here.
