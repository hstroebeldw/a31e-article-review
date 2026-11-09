A31E REVIEW PANEL FOR CLAUDE CODE

What this is
Six reviewer agents, a shared project context, working rules and one command. You give the panel a block of the article (for example the rewritten Sections 6.2, 6.3 and 7.1). Each agent reads it independently, checks the numbers against your workbooks and result files, and reports what is wrong or weak. A final step merges the reports into one file. The agents report; they never edit your text.

The agents
  hydrologist-surface-water    dam balance, inflow, yield, reliability, drought, climate cases
  hydrogeologist-groundwater   MODFLOW structures S and D, recharge, capture, drawdown, MODPATH
  flood-hydrologist            SDF, Midgley and Pitman, RMF, HEC-RAS, flooded areas
  water-quality-contaminants   guideline screening, sources, DRASTIC, pathways
  literature-verifier          does each cited source say what the sentence says, on that page
  academic-editor              the supervisor's corrections: terminology, repetition, number density,
                               Results/Discussion boundary, tone, AI-sounding phrasing

How to set it up
1. Unzip this folder next to (or around) your article files. Keep the hidden folder ".claude" inside it.
2. Nothing else to copy: the article, workbooks, result files, GIS layers, papers, SANRAL text and notes are already
   in the folder "files". Two sources are not included (Pyburn 2015, DWAF 2004); the literature agent fetches them
   from the links in the reference list and says what it could not read. If you add files, list them in
   context/project_context.md section 6.
3. Open a terminal in this folder and start Claude Code:  claude
4. Check that the agents are loaded:  /agents

How to run a review
  /review-block path/to/Block_1_water_balance_REWRITE_v3.md
or name the domains:
  /review-block path/to/block.md surface
The report appears in reviews/. Read group B first: those are the interpretations you decide.

Then
Answer group B, have the block rewritten, and run /review-block again. Repeat until group A is empty. Do this block by block (dam, groundwater, climate, flood, water quality, Conclusions).

What the panel can and cannot do
It is the same underlying model with focused instructions, separate contexts and a checklist. That helps in three ways: each reviewer reads the block fresh, each recomputes numbers from your files, and each has a different set of objections to look for. It does not make the agents field experts, and it can still be wrong. Treat their findings as a strong checklist and a source of questions, not as a verdict. Anything that rests on a source that was not opened is marked "unverified". The final judgement on an interpretation is yours, and your supervisor's.

Settings you may change
Each agent file has "model:" in its header (opus for the domain experts, sonnet for the verifier and editor). Change it if you want cheaper or stronger runs. Web access is needed for the literature checks; the agents never edit project files.

Keep up to date
When a decision changes (a value, a series, a citation rule), edit context/project_context.md section 4 or 5 so every agent sees it.
