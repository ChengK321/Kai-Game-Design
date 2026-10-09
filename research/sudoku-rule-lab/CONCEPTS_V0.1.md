# Sudoku DNA — 三个约束玩法假设 V0.1

Date: 2026-10-09
Repo branch: research/sudoku-rule-lab-v0.1
State: WATCH / HYPOTHESIS. No uniqueness proof, human test, or commercial evidence for any of the three.
Why now: don't build another generic sudoku. Borrow "few constraints -> forced inference -> visible progress", not the 9x9 skin. Keep three independent candidate kernels and cross-compare; no feature-stacking.

## Source mechanism (not a product specification)
Classic Sudoku: a static assignment puzzle; every assignment narrows the options of intersecting row, column, and 3x3 region constraints. Core pleasure: justified certainty and cascading forced moves. This is unlike a state-space survival loop such as 2048.

## SDK-01 — 变色密码 / Switch Count
- One-line rule: the clue at the end of each row and column equals how many times its sequence switches between dark and light. Fill the missing cells.
- Play: 5x5 for first probe; some initial dark/light hints, row/column switch-count clues; tap blank cell to assign one of two colors; no timer/power-ups. Example Dark Dark Light Light => exactly 1 transition; Dark Light Dark Light => 3.
- Pleasure: infer an entire line from 0 or max transition counts; each fixed cell constrains crossing lines. Fine-grained progress akin sudoku.
- Adjacent prior art: binary grids Takuzu/Binairo/Tango and Unruly. Not the same clue semantics, but adjacent cognitive loop. See https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/unruly.html and https://flipultimate.com/blog/games-like-tango
- Major counter-case: counting transitions is dull; row/col counts alone may be very underconstrained; a solvable unique answer need not permit pleasant human deductions.
- Earliest Gate: enumerate solutions under fixed clues; generate a handful of unique 4x4 and 5x5 seeds, then check how often human-readable local deductions suffice. Reject if uniqueness requires many fixed hints or trial-and-error.
- Status: WATCH, novelty UNVERIFIED.

## SDK-02 — 交点亮灯 / One Lamp Per Line
- One-line rule: each visibly marked line must contain exactly one lit node. Different lines can intersect or share nodes. Tap nodes to light them.
- Play: 8-12 nodes linked by 4-7 simple colored paths; some nodes may belong to 2 or 3 lines. Every line must have exactly one lamp. A single lit junction can satisfy several lines while excluding other nodes on those lines. Lines are sets of nodes, not dynamically moving objects. Unselected is not the same as forbidden; optional X-note is UI, not new game rule.
- Pleasure: overlapping exact-one constraints generate a multi-line aha moment. No numbers, basic arithmetic, 9x9 grid, or collision gimmicks.
- Adjacent prior art: Queens / Star Battle use exact-one on rows, columns and *disjoint* regions, with additional no-touch conditions. This idea explores arbitrary overlapping node groups; do not claim unique invention. See https://slowsquares.com/en/one-star/how-to-play
- Major counter-case: dense crossing lines visually confuse players; if 1 click instantly solves multiple constraints without meaningful reasoning, game trivializes. Check graph/line puzzles for close duplicates before any product claim.
- Earliest Gate: first render a 9-node 4-line design as a static diagram; see if three independent people can explain the rule without verbal instruction. Separately use exact-cover solver to verify uniqueness and forced-deduction steps. If layout needs more than 2-3 overlapping strokes per node, cut complexity, not add indicators.
- Status: WATCH, originality UNVERIFIED.

## SDK-03 — 四色修复 / Four-Color Repair
- One-line rule: swap two orthogonally adjacent color tiles; win once each row and column contains exactly one of each of 4 colors. Aim for minimal swaps.
- Play: fully populated 4x4, 4 colors, no empty squares. Generate from a valid Latin-square arrangement, then scramble with 2-5 adjacent swaps; swap remains the only action. Solved means *any* valid Latin-square arrangement, not a hidden preset cell-for-cell solution. Short move count can be rewarded but no extra tools.
- Pleasure: a single swap may repair one line while breaking another; make globally beneficial local corrections and improve toward a low-move finish.
- Adjacent prior art is STRONG: SudokuSwap and Swudoku already use tile swapping to repair sudoku with few moves: https://sudokuswap.com/ and https://swudoku.com/how-to-play/ . 4x4 colors + adjacent-only swaps is not sufficient evidence of novelty. This one is primarily a control experiment.
- Distinguish from existing Ring Shift: Ring Shift moves entire row or column with new balls and capacity pressure; SDK-03 moves exactly 2 neighboring tiles and has no random new content.
- Major counter-case: 2 moves trivial, 5 moves requires costly search, repeated 4x4 repairs all look the same; existing stronger competitors.
- Earliest Gate: use BFS on 4x4 colored board for scramble depths 2-5, quantify min-move ranges and whether simple greed is close to optimal; 5-user pilot only if solver finds an approachable difficulty band.
- Status: WATCH / PRIOR-ART-RISK.

## Comparative judgment
- SDK-01: deduction purity HIGH; visual hook LOW/MEDIUM; generator unknown; highest risk is tedious counting.
- SDK-02: potential insight moment HIGH; explanation minimal when diagram is legible; generator and visual clarity unknown; test visualization *before* feature design.
- SDK-03: touch/action immediacy HIGH; originality LOW/UNVERIFIED; depth and fast play unknown; deprioritize absent clear playtest advantage.
- Recommendation: first discuss/test SDK-02 because the user wants an abstracted new minimal logic loop, not another known sudoku wrapper. Keep SDK-01 as an independent counterfactual, SDK-03 as a negative-control against existing swap games. Priority is a study order, not evidence of success.

## Falsification / decision log
- Decision: preserve 3 candidates together only on research branch; do not create 3 design branches until the specific concept passes its early Gate. Keep core Chain Shot work separate.
- Supporting: players have established demand for fixed-rule logic puzzles; exact-one / binary / swap predecessors prove the mechanics are coherent, not that proposed variants will succeed.
- Counter: puzzle apps are crowded; distribution is not inherited; prior art for SDK-03; no mathematically checked puzzles or humans tested yet.
- Unknown: puzzle uniqueness, no-guess deductability, five-game fatigue, input clarity, visual differentiation, distribution.
- Kill: need extra sub-rules/items/story/complex animation for interest; most testers cannot explain rules quickly; human reasoning has no clear edge over blind random clicking; repeated games not different in thought process.
- Next evidence: single-page non-interactive picture for SDK-02 and a tiny solver for SDK-01/02; two-level HTML comparison only if these probes pass.
