---
description: Run the expert review panel on one block of the A31E article and write one consolidated report
argument-hint: <path to the block file> [domains: surface, groundwater, flood, quality]
allowed-tools: Read, Grep, Glob, Bash, Task, Write
---

Review the block in `$ARGUMENTS`. Do not edit the block or any other project file. The only file you may write is the report in `reviews/`.

1. Read `context/project_context.md` and the block. Decide which domain reviewers apply. If the user named domains, use those; otherwise choose from the content:
   - dam, inflow, canal, reliability, yield, drought, climate cases → `hydrologist-surface-water`
   - groundwater, MODFLOW, abstraction, drawdown, capture, recharge, MODPATH → `hydrogeologist-groundwater`
   - design flood, SDF, RMF, HEC-RAS, flooded area → `flood-hydrologist`
   - water quality, guidelines, EC, phosphate, DRASTIC, pathways → `water-quality-contaminants`
2. Always add `literature-verifier` and `academic-editor`.
3. Start all chosen agents in parallel, each with: the block path, the paths of the evidence files named in `context/project_context.md` section 6, and the instruction to follow its own output format. Give each agent only this task, no summary of other agents' views, so that their reviews stay independent.
4. When all have returned, consolidate:
   - Merge duplicate findings (same sentence, same problem) and keep the strongest evidence.
   - Where two agents disagree, show both positions and say what evidence would settle it; do not pick a side silently.
   - Group the result into: **A. Clear errors** (number does not reproduce, source does not say it, wrong term), **B. Interpretations the author must decide** (each with the options and the cost of each), **C. Wording and repetition**, **D. Checked and sound**, **E. Could not check**.
   - Rank within each group by severity.
5. Write the report to `reviews/<block name>_review_<date>.md` and print only a short summary: counts per group and the five findings that matter most.
6. Never rewrite the block. Rewriting happens afterwards, in a separate step, after the author has decided the questions in group B.
