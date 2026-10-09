# SDK-02 交点亮灯 / One Lamp Per Path — Deep Review V0.2

Date: 2026-10-09
Status: WATCH, mathematically viable in small cases, no product validation. Do not build code yet.
Branch: research/sudoku-rule-lab-v0.1
Relation: research/sudoku-rule-lab/CONCEPTS_V0.1.md

## 1. SHOULD WE DO THIS?
Current decision: NOT a production go. No proof that the gap between trivial boards and visually unreadable dense path diagrams is wide enough to support human fun, repeated plays, or distribution. Continue only as a small, evidence-seeking rules experiment.

## 2. Minimal rule (no growth in player-facing rules)
Tap an existing socket to toggle its light. On each fixed, visibly identifiable path, exactly one socket must be lit. A socket shared by multiple paths counts toward each of those paths. A bare geometric crossing without a socket is NOT a shared node. Paths may be bent and may contain 2 or 3+ sockets. No line-of-sight, transmission, adjacency exclusion, timer, random spawn, abilities, or connection-building.

## 3. Structural mathematical issue: all 2-socket paths cannot yield a unique board
Write x_v in {0,1}. Each 2-socket path (u,v) forces x_u + x_v = 1. If an assignment works, swapping 0 and 1 on every socket preserves every such constraint, so another distinct assignment works. If constraints are contradictory (e.g. a 3-edge odd cycle), there is no assignment. Consequently, with no preset on/off hints, all-2-socket path boards never have a unique solution. Some 3+-socket paths (or user-facing givens, undesirable at this stage) are necessary for unique solutions.

## 4. Example 1: four sockets, three paths
Sockets A B C D.
Paths AB, BC, ADC. Every path requires exactly one lit.
Unique verified solution: B,D lit; A,C off.
Human reasoning: if B off, then AB forces A on and BC forces C on; ADC would then have two lit sockets, contradiction. Therefore B on, A/C off, so D on.
Good: compact contradiction deduction with 1 rule and 2 actions. Bad: can be brute-forced very quickly, little replay by itself.

## 5. Example 2: seven sockets, six paths
Sockets A B C D E F G.
Paths BG; AF; ACG; AE; DG; BDE.
Exhaustive truth-assignment enumeration independently verifies exactly one solution: E,F,G lit, all others off.
Human deduction:
- BG and DG both exactly-one imply B and D have the same state (both complement G).
- BDE exactly-one means B and D cannot both be on; therefore B=D=off and E=on.
- BG => G=on.
- AE with E on => A off.
- AF with A off => F on.
- ACG with A off and G on => C off.
A different tactic appears: pair equality -> eliminate -> cascading definite assignments, not brute choice.
Note: A and G both participate in 3 paths, but A must be off while G must be on; largest-degree node is not a reliable click strategy.
Counter: showing these six intersecting paths on a phone may be a more difficult problem than solving the logic. This table is a mathematical proof of a reasonable deduction, NOT a polished visual puzzle.

## 6. Pleasure loop / limits
Look at shared line memberships -> identify equivalence or exclusion -> justify one forced light -> close one or several path constraints -> propagate. Possible 'aha' but fewer physical clicks than thought steps; rewarding UI may not solve poor readability.
Uniqueness is not the same as human deducibility. Two examples don't establish generator diversity or retention.

## 7. Adjacent competitors and evidence boundary
- LinkedIn Queens official: exactly one crown per row/column/colored region PLUS no neighboring crowns: https://www.linkedin.com/help/linkedin/answer/a6269510
- Star Battle: same exact-one or exact-N placement logic with no-touch, structured grid: https://www.starbattlepuzzles.com/how-to-play
- Akari/Light Up: place bulbs, line-of-sight illumination/no bulb mutual visibility/numeric wall clues; visual theme is closer, actual rules distinct: https://www.thepuzzlelabs.com/light-up-akari/rules
- Graph path/constraint exact-one is a known abstract combinatorial form, cannot claim originality based on searching without a directly identical app.

## 8. Strongest counter-case
The 'newness' is in unusual presentation of overlapping exact-one sets, while the exact-one inference core is not new. Queens' rows/columns/color regions are instantly legible, while arbitrary curved paths require players to trace crossings and distinguish which sockets count toward which path. Small boards risk obvious central click or brute-force; large boards risk visual clutter and a logic-exam feel. In that scenario this is a worse interface for a known mechanism.

## 9. Evidence gates without code
1. Prepare just two or three STATIC phone-size paper/slide diagrams (no runnable prototype), including the 4-node tutorial and a 7-node case. All paths individually traceable; no ambiguous crossings. Not a full art redesign.
2. Blind test 5-8 people: after a single one-line rule, do they understand shared-node credit, distinguish crossing with/from without node, and make a justified placement rather than guess? Record time-to-understand and expressed frustration. Do not coach while they play.
3. Before investing in a generator, require a handful of different human-deducible unique puzzles with different first deductions, no reliance on 'click the highest-degree junction' or forcing central universal intersections.
Kill if several people misunderstand the path membership, if meaningful puzzles are visually cluttered, if first clicks are mostly trial and error, or if five varied boards all boil down to the same trick.
4. Only after these tests, compare again vs Queens/Tango/0h h1; require experience superiority or a distinct audience, not a cosmetic difference.

## Decision Log
- Decision: WATCH; no production, no code, no elaborate UI or rule additions.
- FACT: official competitor rules.
- CALC: structural complement symmetry; examples above unique as enumerated.
- INFERENCE: potential human 'aha' loop; high visual interpretation cost.
- HYPOTHESIS: enough readable, varied, quick-logic boards exist to make a repeatable game.
- Strongest Counter: exact-one generalized graph is difficult to read; presentation cost destroys the simplicity gained by omitting numbers.
- Next Evidence: static phone-size diagrams + uncoached people, then logic generation only if legible.
