# Chain Shot — V0.2 Depth Validation Plan

> Date: 2026-10-07
> State: ACTIVE PROTOTYPE V0.2
> Evidence: V0.1 received a positive internal playtest signal: core interaction was not perceived as obviously boring and is worth another minimal iteration.
> Constraint: Keep the exact same gameplay rule. Do not add special arrow types.

## 1. The Question V0.2 Must Answer

**Can positions + directions + node count alone create enough decision depth and replayability?**

If yes, Chain Shot remains a high-rule-density one-rule game.

If no, we must distinguish:
- weak core rule;
- weak level generation;
- weak visual explanation.

Do not hide a weak core behind new systems.

## 2. Model the Puzzle as Reachability

For every level, each arrow node is a vertex.

If node A fires and its ray passes through node B, create a directed edge:

`A → B`

Because rays pass through all collinear nodes, one node may have several outgoing edges.

Choosing a Seed means computing the transitive reachable set from that node.

The current puzzle is therefore:

> Find a Seed whose reachable closure contains every node.

This gives us a cheap offline solver and measurable level quality.

## 3. Required Level Metrics

For every candidate level calculate:

### solutionCount
How many Seeds reach 100% of nodes.

Target: usually 1; occasionally 2.

### reachRatio(seed)
`reachableNodes / totalNodes`

Use the distribution, not just the best Seed.

### nearMissCount
Number of wrong Seeds with reach ratio between 0.60 and 0.90.

Target: at least 2 on mid/late levels.

### maxCascadeDepth
Longest activation generation from Seed.

Target:
- tutorial: 2–3
- normal: 3–5
- spectacle: 5–7

### branchEvents
How many activated nodes cause 2+ new nodes to activate.

Target: at least 1 after tutorial.

### seedEntropy
How different are Seed outcomes?

Reject levels where almost every Seed produces the same result.

### visualDensity
Basic spacing/readability check.

Reject nodes that overlap or make arrow directions unreadable on mobile.

## 4. Generator Strategy

Do not begin with a sophisticated procedural generator.

Use a simple offline loop:

1. Randomly choose 6–16 unique grid positions.
2. Randomly assign 8-direction arrows.
3. Build the directed graph.
4. Solve every possible Seed.
5. Calculate metrics.
6. Reject poor levels.
7. Save interesting candidates as JSON.
8. Human-test the survivors.

Generation is a tool for finding hand-curated levels, not a runtime feature.

## 5. V0.2 Level Ladder

### 01–02 Learn
- 5–6 nodes
- clear branching
- easy to infer

### 03–05 Near Miss
- 7–10 nodes
- wrong Seeds often trigger 60–80%
- player gets “almost” feedback

### 06–08 Prediction
- 9–12 nodes
- direction geometry matters
- no obvious center heuristic

### 09–10 Spectacle
- 12–16 nodes
- 4+ activation generations
- multiple visible branches
- final cascade should be screen-record worthy

Do not ship 100 generated levels. Ten good ones are enough for this gate.

## 6. Feedback Improvements — No New Mechanics

### Failed Run
After cascade ends:
- keep activated nodes bright;
- pulse unactivated nodes softly;
- show `8 / 11 activated`;
- Restart remains one tap.

Goal: make failure informative.

### Cascade Readability
Each activation should have a very short anticipation flash before its outgoing pulse moves.

Goal: player can mentally follow:
`this node woke up → therefore that ray appeared`.

Do not slow the whole game excessively.

### Chain Rhythm
Prefer a visible rhythm:
`tap → 1 → 2 → 4 → 7 → complete`

rather than everything firing in one frame.

### Success
Keep success short.
No chest, coins, confetti economy, stars or progression screen yet.

## 7. Optional Debug Overlay

Only for development:

- node index;
- graph edges;
- chosen Seed reach ratio;
- activation generation/depth;
- solution Seeds.

Toggle via a small debug flag or URL query.

Never show this in normal play.

## 8. Playtest Questions

Observe behavior rather than asking “好玩吗”:

1. Does the player inspect directions before tapping?
2. On a fail, can they explain at least one missed connection?
3. Do they choose a different Seed on retry?
4. Do they develop a heuristic?
5. Does a 10–16 node cascade remain understandable?
6. After ten levels, do they want another level?

## 9. Kill / Continue

### Continue One Rule
If:
- 10 levels feel meaningfully different;
- Seed choice feels deliberate;
- near misses cause immediate retries;
- cascade remains readable.

### Degrade
If:
- generator can only make trivial or random-feeling boards;
- solution cannot be reasoned about visually;
- every level becomes brute-force Seed testing.

### Break
If:
- cascade spectacle is enjoyable but Seed choice is irrelevant;
- players prefer watching Demo to playing;
- a new system is required to create any decision.

## 10. Product Identity

Avoid building or marketing this as “最强大脑同款 / 箭域迷阵”.

Working identity remains **Chain Shot**.

The product value we are testing is:
**one deliberate trigger causing a readable branching chain reaction.**
