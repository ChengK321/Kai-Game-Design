# Chain Shot — Master Design State & One-Rule Depth Gate

> Updated: 2026-10-09
> Status: ACTIVE PROTOTYPE / ONE-RULE DEPTH REVIEW
> Canonical design conversation: Chain Shot 主对话
> Code: `ChengK321/Kai-Game-Design` branch `design/chain-shot-v0.1`
> Current experiment: V0.3.1. Do not start V0.4 until a depth gate has been reviewed.
> Evidence discipline: DIRECT OBSERVATION / VERIFIED CODE / CALC / INFERENCE / UNKNOWN.

## 1. Master Decision (2026-10-09)

- **Keep and test** the exact current One Rule. No rule, Solver or level rewrite is approved by this note.
- **Design baseline**: Classic persistent activation + original synthesized Hit + Direction-family color scheme.
- **Hold**: Lukeo135 Pop, Breviceps Pop, other licensed Pop candidates, Balloon Blast. No further opacity/micro-tuning or wholesale effect systems without evidence of benefit. This is a HOLD, not a permanent ban.
- **Hold**: V0.4 development, new arrows, obstacles, skills, economy, procedural production pipeline.
- **Next discriminating evidence**: novice human behavior on a few existing boards, focused on first-seed reasoning, deductions after failure, desire for the next puzzle and enthusiasm for the cascade.
- **Backups remain** Bounce Merge and Breath Block; do not open parallel production.

Note: current V0.3.1 HTML/report still defaults to Lukeo135 Pop on launch. The agreed design baseline is Classic + Synth; for now launch with `?audio=synth&mode=classic`. No code change was performed to alter the persisted default.

## 2. Compact History (no reset)

### V0.1 — One rule; branching chain

Initial inspiration: `《最强大脑》箭域迷阵` / tiny arrow-chain puzzles.

Our transformation: player clicks one Seed; ray passes *through* all encountered nodes; each unactivated hit arrow fires its own direction; each node activates once; full board reachability wins.

Core promise: `Observe → Predict → Tap → Watch branching cascade → Understand → Retry`.

### V0.2 — Graph + presentation exploration

- Deterministic directed graph/Solver allows measuring seed reachability, solution count, near misses, depth, branching.
- Familiar heart/house/lightning shapes introduced as an optional **expression** and first-impression enhancement, not as a second gameplay rule.
- Avoid copying `Arrow Out`'s exit-order gameplay or any commercial assets.
- One core pitfall: shape prettiness and cascading spectacle can conceal weak solving depth.

### V0.3 — 10 levels + animation/audio A/B

- Classic persistent lit nodes; Blast faded/fractured nodes; synth audio; three themes.
- Codex report: 660 Seed×mode×theme cases matched Solver; runtime/mobile-viewport testing passed within documented scope.
- Human observation: direction-family palette helped; Classic more comfortable and more traceable than initial Blast; synth sound felt underwhelming *before* the licensed audio A/B experiment.
- Emerging mechanical issue: a failed cascade strongly shrinks the possible winning seed set.

### FX Lab → V0.3.1 — Reference-driven sound trial

- Separate, offline FX Lab tested licensed CC0 pop variants (Freesound HQ previews and Kenney samples) in single/12-hit and fixed L6/L10 replay.
- V0.3.1 integrates live hit events, mode/audio switching, same-seed replay and 10 existing levels, without changing Solver or V0.3.
- Codex report: 1,100 Seed×audio×visual combinations matched independent Solver; browser checks passed. These are correctness tests, **not evidence of a preferred sound**.
- Latest USER HUMAN PLAYTEST:
  - Synth Hit clearly preferred;
  - Lukeo135 Pop resembled a machine gun in cascades;
  - Breviceps was crisp but repetitive;
  - Classic clearer/more comfortable than Balloon Blast;
  - Blast sound and animation did not provide expected uplift;
  - Possible cross-modal mismatch remains unverified.
- Therefore the prior V0.3 `keep polishing Pop/Blast` hypothesis is downgraded, not rationalized by more parameter tweaking.

## 3. Core Invariants (freeze until evidence gate)

1. One manual Seed per attempt.
2. Ray passes through nodes to board edge.
3. An unactivated node hit by a ray fires its own direction.
4. Each node activates at most once.
5. All rays stop before result declared.
6. Result = all activated nodes.
7. Retry fully resets simulation.
8. Rendering/audio variants do not alter Solver reachability.

## 4. Strongest Counter-case Against the One Rule

### Proven properties of current deterministic propagation graph

Let `R(s)` be the nodes activated from start `s`.

- `R(s)` is closed under outgoing reachability.
- If a start fails, **no node within its activated set can be the full-clear winner**. All winning seeds must lie among the **unactivated** nodes.
- With exactly one winning seed, that seed must have zero incoming edges (if another node could trigger it, that predecessor would also clear everything).
- In *all current 10 levels*, the single winning Seed is also the single zero-in-degree node.

Thus a possible `find the untriggerable source` solution policy exists, potentially bypassing intended long-cascade reasoning.

### Quantifying a simple player policy (not actual player telemetry)

From `prototype/chain-shot-v0.3-levels.json`, compare:
- `Blind random`: test unused Seeds uniformly without using cascade feedback (expected attempts `(n+1)/2`).
- `Elimination-only`: choose uniformly from candidates not yet ruled out; after each failed trial remove *all nodes activated by that attempt* from candidate pool, retaining this information across attempts. No arrow-geometry reasoning.

| Level | Blind random expected | Elimination-only expected | Wrong seeds leaving ≤2 dormant |
|---|---:|---:|---:|
| 1 | 3.00 | 2.67 | 1 / 4 |
| 2 | 4.00 | 3.03 | 1 / 6 |
| 3 | 4.50 | 2.93 | 1 / 7 |
| 4 | 5.00 | 2.84 | 2 / 8 |
| 5 | 6.00 | 2.70 | 6 / 10 |
| 6 | 6.50 | 3.04 | 2 / 11 |
| 7 | 6.00 | 2.47 | 8 / 10 |
| 8 | 7.00 | 3.58 | 1 / 12 |
| 9 | 8.50 | 3.60 | 1 / 15 |
| 10 | 9.50 | 4.51 | 0 / 17 |

The expectations are **CALC from current level data and a toy policy**, not human performance or retention. Actual players do not necessarily choose random Seeds or preserve all eliminated sets.

### Why this may invalidate puzzle longevity

Even without skill in predicting long cascades, users can learn:
- fail once → focus on unactivated nodes;
- optionally look for the unique arrow no other arrow can reach;
- solve by a similar routine across boards.

Near-miss-rich boards might feel exciting but could accelerate collapse to 1–2 candidates. The most visually satisfying boards are not necessarily the best puzzles.

### Strongest argument for continuing

This simplification could itself be the learning loop: visible failure teaches an actionable insight; player feels clever; short levels emphasize expressive cascade and satisfying completion rather than difficult abstract graph solving. No external novice playtest has established whether the shortcut is boring or rewarding.

## 5. Skill Research Integration (from 游戏开发 Skills 调研)

Kai-Game-Lab PR #2:
https://github.com/ChengK321/Kai-Game-Lab/pull/2

Branch `feat/kai-game-skills-v0.1` is currently **OPEN / NOT MERGED**. Its evaluation is **PROPOSED / NOT YET RUN**.

Four original project Skills:

- `kai-mechanic-gate`: reframing, simple-policy counterexamples, competing product frames, explicit kill criteria. **Primary workflow for the next phase.**
- `kai-game-prototype`: smallest reversible playable slice. Not needed until a concrete change is approved.
- `kai-game-feel`: controls sound/visual A/B without mechanics changes. Use only if a specific user-observed perceptual defect becomes the next bottleneck.
- `kai-game-qa`: rule invariants → deterministic Solver → actual browser smoke → visible result → real human playtest. QA success is not fun or retention.

Do not claim Codex has automatically installed or executed these Skills in the game repo; this integration uses their **documented methods**. Do not merge PR #2 or add new heavyweight tool chains without separate evaluation/approval.

## 6. Proposed Smallest Discriminating Human Playtest

### No new features needed

Use current V0.3.1:
`prototype/chain-shot-v0.3.1.html?audio=synth&mode=classic`

Prefer Direction-family color setting. No hint mode, demo, time limit, skins, or new arrow type.

### Participants

Seek 4–6 fresh users with no Chain Shot design involvement. This is *screening evidence*, not a statistically powered retention study. Let them play without explaining the graph/incoming-degree shortcut.

### Session (about 10 minutes/person; flexible)

1. Give only one sentence: `点一个箭头，让所有箭头被触发。`
2. Observe L1–3 learning; do not prompt for a strategy during initial attempts.
3. Observe L5, L7, L10 (plus L6 if time permits), including first click and first fail.
4. After play, ask `你是怎么决定点哪个箭头的？` and `为什么下一次选择那个？`. Asking after play avoids tutoring them with leading language.
5. Finally ask if they want another level, and whether the most enjoyable part was planning or seeing propagation.

### Minimal worksheet

For each player/board record:
- first decision latency (rough seconds);
- first Seed + did it succeed;
- failed-run reach ratio / remaining nodes;
- number of attempts to clear;
- does next selection lie among previously unactivated nodes;
- did the player *spontaneously* articulate 'find one nobody hits' or another repeatable heuristic;
- voluntary retry / voluntary next level;
- an example of causal reasoning, or description of pure blind testing;
- clarity and comfort of Classic+Synth cascade after multiple repetitions.

Human observers should keep the first-run experience natural; avoid giving them a tutorial about residual sets or graph degrees.

### Decision Gate — predeclare interpretation, don't invent precision

**Continue as puzzle-first** when players often inspect direction relationships BEFORE first input, explain failures in terms of causal paths, and continue to find fresh distinctions between boards.

**Continue as chain-spectacle-first** when solving is easy but players voluntarily replay because the visual/audio propagation itself is rewarding. This is a possible alternative product frame with same rule, not permission to introduce systems.

**Degrade / consider Hold** when players primarily cycle candidate Seeds mechanically, rapidly converge on one trivial heuristic, cannot distinguish why later boards are different, and show no desire for another level despite clear feedback.

Do not choose the winning frame by tiny percentages from a 4–6-user sample. Consider whether the same qualitative pattern repeats independently.

## 7. No premature V0.4

Current next action is a **read-only Depth Review + human test**, not UI polish, new levels, more Pop recordings, new mechanics, or refactoring.

After observation, write:
`Decision / Evidence / Counter Evidence / Unknowns / Falsification / Next Evidence`

Only if observed player behavior supports it should we change the curated level selection / failure-presentation or reopen the One Rule itself. A flawed heuristic cannot be repaired merely by adding particles.

## 8. Project references

- `CHAIN_SHOT_V0.3.1_IN_GAME_FX_REPORT.md`
- `CHAIN_SHOT_V0.3_REPORT.md`
- `CHAIN_SHOT_FX_LAB_REPORT.md`
- `CHAIN_SHOT_V0.3_PLAYTEST_REVIEW_2026-10-08.md`
- `prototype/chain-shot-v0.3-levels.json`
- `tools/chain-shot-solver.py`
- `CHAIN_SHOT_V0.3.1_IN_GAME_FX_GATE_2026-10-08.md`
- `CHAIN_SHOT_GAME_FEEL_REFERENCE_BRIEF_2026-10-08.md`
- `Kai-Game-Lab` PR #2 for game Skills (not merged)
