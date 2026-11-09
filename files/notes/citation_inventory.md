# Citation inventory: A31E Honours article (read-only)

Files: `/home/claude/work/citation_inventory.csv` (81 rows, full table) and this report. The article was not edited. Nothing was browsed; all URLs and read-status notes come from the article and chats 1-6.

Conventions. Page numbers are the printed page numbers (PDF page minus 5; the Abstract and start of Section 1 are printed page 1). Chat evidence is given as `chatN:line`. "Paywalled" is judged from the publisher only.

## 1. Reference list (Step 1)

81 entries, parsed to one row each in the CSV (id, authors, year, title, outlet, type, DOI/URL). Types: 38 journal, 25 report (including IPCC chapters, manuals, proceedings), 9 dataset (including 3 maps), 5 web, 2 legislation (Government Gazette notices), 1 news, 1 thesis. No entry is itself a secondary source.

Reference-list observations:
- Truncated author lists ("..."): Barnett 2012 (6); Cuthbert 2019 (12); Farr 2007 (34); Fowler 2022 (35); Gutiérrez 2021 (36); Iturbide 2022 (40); Iturbide 2020 (41); MacDonald 2021 (54); Ranasinghe 2021 (64); Trisos 2022 (74); Xie 2024 (81).
- The two geological maps (Michaluk & Keyser 1991; Walraven 1981) have no URL and no date of access. Chat3:271 had given a catalogue link for Michaluk (https://gbank.gsj.jp/ld/resource/geolis/90000538.html) and the publisher "Geological Survey", whereas the article says Council for Geoscience.
- Five dates of access (Canadell 1 Oct, Knowling & Werner 2 Oct, Konikow & Leake 4 Oct, Seward 5 Oct, Pyburn 7 Oct) were proposed by the assistant "in alternating steps of 1 and 2 days" (chat6:3466-3478), with the caveat that they should be the real dates. Their provenance should be confirmed.

## 2. In-text citations matched to the list (Step 2)

I found 240 in-text citation instances (224 parenthetical, 16 narrative "Author (Year)") from the Abstract to Conclusions. The Abstract, Recommendations and Conclusions contain none. Each was matched to a list entry by author, year and letter suffix. Per-entry usage (sections and printed pages) is in the CSV column `cited_at_section_and_printed_page`.

Results:
- Citations with no matching reference entry: none, for author-year citations. The only unlisted names are primary sources of secondary citations (Section 3 below).
- Reference entries never cited: none. Eight entries are cited only in narrative form (Adeloye, Coerver, Cullis & Phillips, Ebrahim, Howard & Washington, Konikow & Leake, Moriasi, Sankarasubramanian), so a search for "(Author, Year)" misses them.
- Mismatched years, spellings or letter suffixes (1996a/b, s.a.a-s.a.f, Iturbide 2020/2022): none found. Iturbide et al. 2022 is cited only inside "Iturbide et al., 2020, 2022" (Section 5.1.4).
- 36 entries are cited only once. Those that bear on the Discussion include Peterson 2021, Fowler 2022, Xie 2024, Konikow & Leake 2014, Howard & Washington 2020, Rouault & Richard 2005 and Canadell 1996.
- Cited page numbers fall inside each source's page range, except that Bailey & Pitman 2016 is listed as the "executive summary" yet is cited at pages 14 and 30 (2.2 and 5.1.1). The helper chat said it had no copy of the report (chat5:4244).
- Four cited pages equal the first page of the paper: Calow 2010:246, Seward 2006:473, Troldborg 2007:843, Peterson 2021:745. These are the sources that the chats describe as abstract-only (Section 4).

## 3. Secondary citations (Step 3)

| Where | Form in text | Primary source (from chats, not in the list) |
|---|---|---|
| Section 1, p. 2 | DWAF, cited by Knüppe, 2011:69 (15% national groundwater share) | A DWAF report of 2002 (chat3:87); title not given anywhere |
| Section 3.4, p. 13 | Alexander, cited by Smithers, 2012:639 (SDF calibrated on 29 catchments) | Alexander's work on the Standard Design Flood; year and title not given in the files |
| Section 3.4, p. 13 | Midgley and Pitman, cited by SANRAL, 2013:3-61 to 3-62 | Midgley & Pitman empirical flood formula; year and title not given. Chat5:232 had "cited by Smithers" instead |
| Section 6.8, p. 48 (text and Map 11 caption) | DWAF, cited by Esterhuyse, 2017 (DRASTIC classes) | National DRASTIC map for DWAF, 2005, GEOSS (chat3:771, 784) |
| Section 7.4, p. 53 | section 144, quoted by SANRAL, 2013:11-4 | National Water Act 36 of 1998, s. 144 |

In four of the five, the primary author is given without a year, which may be incomplete under the NWU secondary-citation pattern. I have not checked the NWU guide, which is not in the files.

## 4. Flags (Step 4)

### 4a. Abstract-only or unverified (from chat history)

The article text and docx carry no "[Abstract]" tag, and the list has no Konikow & Bredehoeft 1992 (discussed in chat6 as abstract-only). The chats record the following:
- Rouault & Richard 2005: abstract only; article number L15702 unconfirmed (chat3:85, 175, 209). Cited in Section 1.
- Calow 2010, Peterson 2021, Seward 2006, Troldborg 2007: tagged [Abstract] (chat5:4189, chat6:3288). PDFs were later received and "first page" confirmed (chat6:3498, 3574, 3602). The chats do not show that the page-by-page check was done.
- Canadell 1996: "abstract only" (chat4:250); the 15.0 m figure was read from the abstract (chat1:3560). Cited in 5.2.2.
- Pyburn 2015: the user says he read it through the NWU Library (chat2:306), but the helper and project chats held only extracts (chat3:2199; chat4:2361). Cited at pp. 4, 28, 44.
- Could not be opened by the helper (Oct 8): Hashimoto 1982 (quote and p. 19), Aminzadeh 2024, Schulze & Schütte 2023, Howard & Washington 2020 (quoted words unchecked), Saft 2015 (chat2:135, 422, 768). No later chat shows them checked.
- Fowler 2022 was accepted as "real" from memory (chat4:1292), not opened.
- No chat mentions: Kapangaziwiri 2011, Xie 2024, Scheff & Frierson 2014, Sankarasubramanian 2001, Adeloye, Coerver, Dlamini, Ebrahim, Harbaugh, Moriasi, Klemeš and 34 others (45 in all; the CSV column `chat_read_status` shows "No mention in chats 1-6").

### 4b. Citations supporting a local explanation from another catchment or continent (flag only)

| Source | Sentence supported (quoted, shortened) | Section, page | Reasoning |
|---|---|---|---|
| Peterson 2021 (Australia) | "runoff...had likewise not recovered...in 37% of the watersheds studied" | 7.1, p. 49 | Offered as a parallel for the unexplained 1980s-90s low inflow. The text itself says the cause is not assigned. |
| Fowler 2022 (Australia) | "declining groundwater storage and the harvesting of runoff by small dams" | 7.1, p. 50 | Australian explanations are said to "match" the two local explanations. Analogy, not evidence for the dam. |
| Saft 2015 (Australia) | "runoff during a long drought falls below" the earlier relationship | 7.2, p. 50 (also 3.1, 7.3) | Used to say the modelled naturalised runoff "agrees" with the finding. The sentence reads as a contrast, not agreement. |
| Kapangaziwiri 2011 (South Africa, other catchments) | low flows "may also come from storage above the water table" | 7.1 and 7.2 | National, not A31E. Used to explain why groundwater is not shown as the store. |
| Pyburn 2015 (Zeerust dolomite) | springs "declined to almost nil in 1986" | 7.1, p. 49 | Upstream and outside A31E; the link to dam inflow is "inferred". |
| Calow 2010 (Africa-wide) | boreholes' water "lies mainly near the surface" and "first to fail" | 7.2, p. 51 | Continental paper used for a statement about A31E's aquifer and its limit as a backup. |
| Cuthbert 2019 (sub-Saharan Africa) | recharge "depends mainly on episodes of heavy rainfall" | 7.3, p. 52 (also 1) | Used to say a drier climate could cut recharge "by more than the factor used". |
| De Wit & Stankiewicz 2006 (Africa) | change in rainfall "magnified in river flow" where about 500 mm | 7.3, p. 51 (also 1, 3.3) | Continental perennial-drainage finding used to explain the −7% to −20% inflow change. Chat2:1087 notes the paper measures perennial rivers. |
| Troldborg 2007 (Denmark) | models "that differ little in their heads can differ greatly" | 7.2, p. 51 | A multi-aquifer study used to interpret structures S and D. Methodological. |
| Scheff & Frierson 2014 (global) | warming "raises the evaporative demand by a few per cent" | 7.3, p. 51 | Global scaling applied to A31E. |
| Hashimoto 1982 | "high system reliability was accompanied by high system vulnerability" | 7.1, p. 48 | A general criteria paper. The quotation and p. 19 were not opened (chat2:768). |
| Konikow & Leake 2014 | capture "supplied about 0.85 of long-term withdrawals" | 3.2, p. 11 | Review of other aquifers, then relied on in 7.2 ("balanced mostly by capture"). |
| Xie 2024 (global) | groundwater "sustains river flow as baseflow" | 1, p. 2 | Global baseflow finding stated for dry periods in semi-arid catchments. |
| MacDonald 2021 (Africa) | recharge increases "to a power of about 1.34 to 1.39" | 5.2.4, p. 24 | Africa-wide relation used to set A31E recharge factors, which feed the climate results. |
| Sankarasubramanian 2001 (USA) | elasticity "estimated at 2.0 to 2.5" | 5.2.4, p. 24 | US method; the text itself says the inflow elasticity is only an "approximate scaling". |

## 5. Chat notes per entry (Step 5)

The chats contain few links. Candidate URLs are mostly those printed in the list (the CSV column `candidate_urls`). Links found only in the chats:
- Rouault & Richard 2005 repository copy: https://africarxiv.ubuntunet.net/handle/1/8737 (chat6:3371).
- Pyburn 2015 handle: http://hdl.handle.net/10394/20507 (in the list; chat2:147).
- Michaluk & Keyser 1991 catalogue record (chat3:271): see Section 1.
- Konikow & Bredehoeft 1992 USGS record: https://pubs.usgs.gov/publication/70016167 (chat6:3508); not cited in the article.
- Operating-rule sources Swart et al. 2007 (miya-water PDF, chat6:204) and DWAF 2007 do not appear in the article.

Status summary: opened or checked in chats: Aller, Esterhuyse, Smithers (pages), Ranasinghe (pp. 1770-1771), Engelbrecht (p. 37), Kovács figure, Farr, Mbae ("real"). See the CSV for all rows.

## 6. Priority list for full-text check via library sign-in (Step 6)

Order is by how much each source carries the Discussion's "why" claims. DOIs resolve through the library proxy. P = likely paywalled, OA = open access.

Drought recovery (7.1, 7.2):
1. Peterson 2021, Science. P. https://doi.org/10.1126/science.abd5085. Check the "37%" claim and the cause explanation.
2. Fowler 2022, HESS. OA. https://doi.org/10.5194/hess-26-6073-2022. Never opened per the chats; check the two explanations.
3. Saft 2015, WRR (Wiley). P. https://doi.org/10.1002/2014WR015348. Cited three times (3.1, 7.2, 7.3); could not be opened by the helper.
4. Kapangaziwiri 2011, IAHS. OA. https://iahs.info/uploads/dms/16813.26-127-132-345-04-H01_109_KAPANGAZIWIRI.pdf. Check pp. 127-128.
5. Pyburn 2015, NWU repository. OA. http://hdl.handle.net/10394/20507. Check pp. 4, 28, 44 against the full text.

Groundwater capture and backup (7.2):
6. Calow 2010, Ground Water (Wiley). P. https://doi.org/10.1111/j.1745-6584.2009.00558.x. Check the "near the surface" and "first to fail" claim.
7. Konikow & Leake 2014, Groundwater (Wiley). P. https://pubs.usgs.gov/publication/70127476. Check the 0.85 figure.
8. Seward 2006, Water SA. OA. https://ajol.info/index.php/wsa/article/view/5287.
9. Leake & Barlow 2013, USGS Fact Sheet. OA. https://pubs.usgs.gov/publication/fs20133001.
10. Troldborg 2007, Hydrogeology Journal (Springer). P. https://doi.org/10.1007/s10040-007-0192-y.
11. Knowling & Werner 2016, J. Hydrol. (Elsevier). P. https://researchnow.flinders.edu.au/en/publications/estimability-of-recharge-through-groundwater-model-calibration-in/. Recharge estimability.

Recharge and climate-change response (5.2.4, 7.3):
12. Cuthbert 2019, Nature. P. https://doi.org/10.1038/s41586-019-1441-7.
13. De Wit & Stankiewicz 2006, Science. P. https://doi.org/10.1126/science.1119929. Only the repository record was read.
14. MacDonald 2021, ERL. OA. https://doi.org/10.1088/1748-9326/abd661. Check 1.34-1.39.
15. Scheff & Frierson 2014, J. Climate (AMS). P. https://doi.org/10.1175/JCLI-D-13-00233.1. Check "about 1.5-4%" and p. 1554.
16. Sankarasubramanian 2001, WRR (Wiley). P. https://doi.org/10.1029/2000WR900330. Check p. 1775.
17. Howard & Washington 2020, J. Climate (AMS). P. https://doi.org/10.1175/JCLI-D-19-0755.1. Quoted words never checked.
18. Ranasinghe 2021 and Trisos 2022 (IPCC, Cambridge). OA. https://doi.org/10.1017/9781009157896.014 and https://doi.org/10.1017/9781009325844.011.

Other Discussion and Introduction claims:
19. Xie 2024, Nature Geoscience. P. https://doi.org/10.1038/s41561-024-01483-5. Check the baseflow statement.
20. Hashimoto 1982, WRR (Wiley). P. https://doi.org/10.1029/WR018i001p00014. Check the quote on p. 19.
21. Rouault & Richard 2005, GRL (Wiley). P. https://doi.org/10.1029/2005GL022436 or https://africarxiv.ubuntunet.net/handle/1/8737. Check "six of the eight".
22. Canadell 1996, Oecologia (Springer). P. https://link.springer.com/article/10.1007/BF00329030. Check 15.0 m (abstract only).

Salinity (7.5; reports, free web): DWAF 2004:57 (https://www.dws.gov.za/Documents/Other/WMA/MaricoISPfeb04.pdf) for the sources of the canal water's salinity; DWS 2021:163 (https://www.gov.za/sites/default/files/gcis_document/202112/45568gon1559.pdf) for the groundwater EC of 17.7 mS/m; DWAF 1996a:155 for the 40 mS/m guideline (https://www.dws.gov.za/iwqs/wq_guide/Pol_saWQguideFRESHIrrigationvol4.pdf).

## 7. Points for the main session

- The user's saved rule is that a source not read in full is removed from the article rather than tagged. The sources in 4a are the ones that rule bears on (from memory notes).
- Nothing in the chats shows that the "[Abstract]" sources were read through after the PDFs were received.
