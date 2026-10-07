# Codex Task — Chain Shot V0.2

Read first:

- `CHAIN_SHOT_DESIGN_V0.1.md`
- `CHAIN_SHOT_V0.2_PLAN.md`
- `prototype/chain-shot-v0.1.html`

## Mission

Upgrade the prototype without adding any gameplay rule.

The goal is to test whether node position + arrow direction alone can support 10 good levels.

## Part A — Build an Offline Solver

Create:

`tools/chain-shot-level-tool.html`

or a small dependency-free JS script if simpler.

It must:

1. Accept a level JSON.
2. Build all directed edges according to the exact ray-pass-through rule.
3. Simulate every possible Seed.
4. Report for each Seed:
   - reachable node count;
   - reach ratio;
   - activation generations;
   - max cascade depth;
   - branch-event count.
5. Report level-wide:
   - solution Seeds;
   - solution count;
   - near-miss count (60%–90%);
   - outcome distribution.

Keep solver logic deterministic and separate from animation.

## Part B — Add Candidate Generation

A simple brute-force/random candidate generator is enough.

Inputs:
- node count;
- number of candidates;
- optional RNG seed.

Generate unique grid positions and 8-direction arrows, solve them, then keep only candidates satisfying configurable thresholds.

Default filter:
- solutionCount = 1 or 2;
- nearMissCount >= 2 for nodeCount >= 8;
- successful Seed maxCascadeDepth >= 3;
- successful Seed branchEvents >= 1.

Export accepted candidates as JSON.

Do not build a polished level editor.

## Part C — Curate 10 Levels

Use the tool, then manually inspect.

The final game prototype should contain only 10 curated levels.

Target ladder:
- 2 learn;
- 3 near-miss;
- 3 prediction;
- 2 spectacle.

Do not blindly take the top metric scores. Visual readability matters.

## Part D — Improve Failure Readability

In `prototype/chain-shot-v0.1.html`:

- after failure, keep active nodes bright;
- softly pulse dormant nodes;
- show activated / total;
- Restart must be immediate;
- no modal dialog.

## Part E — Improve Causal Readability

Add a tiny activation anticipation:
- node flashes/pops;
- then emits its outgoing pulse;
- activation order should remain visually traceable.

Do not change the simulation graph.

## Part F — Development Debug Mode

Add a hidden debug flag:
`?debug=1`

When enabled, allow showing:
- node indices;
- solution Seed(s);
- current seed reach ratio;
- activation generation number.

Normal mode must remain clean.

## Constraints

Do NOT add:
- special arrows;
- blockers;
- enemies;
- numbers;
- powerups;
- scoring economy;
- lives;
- procedural runtime levels;
- meta progression;
- skins;
- tutorial pages.

## Deliverables

1. updated prototype HTML;
2. level analysis/generation tool;
3. JSON or JS data for the final 10 curated levels;
4. short `V0.2_RESULT.md` explaining:
   - what changed;
   - which metrics were used;
   - why the 10 levels were selected;
   - remaining risks that require human playtest.

Before finishing, verify every curated level has at least one valid solution under the production simulation.
