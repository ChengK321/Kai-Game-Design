# Chain Shot / Arrow Cascade — Minimal Decompression Rule Review

> Date: 2026-10-09
> Status: RESEARCH / PROPOSED RULE LAB ONLY. Not V0.4, not an approved rewrite.
> Main conversation: Chain Shot design mainline
> Immutable baseline: Chain Shot V0.3.1 Classic + original Synth Hit + Direction-family palette, 10 curated levels + existing Solver
> Evidence types: [SOURCE FACT], [MODEL CALC], [INFERENCE], [HYPOTHESIS]

## 1. User framing and corrected target

User finds that limiting each arrow to one relay risks reverting to `箭域迷阵`; original unlimited static-chain + single all-clear has a structural unique-source shortcut. Wants a multi-tap partial-clear **decompression** experience with minimal rules, drawing from the prior ~50-game sample library and current public games.

Do not optimize for exactly one correct Seed. Instead ask:

> Can each tap clear a satisfying cluster, and does the board change so the next tap is meaningfully different, without adding digits, skills, timers, lives or special arrows?

The source Gamelab.zip from the earlier conversation was **not directly accessible as a complete 50-game attachment in this session**. This review reuses previously recorded Rule Mining findings, the accessible 11-image game sample summary, Kai-Game-Lab notes, plus freshly checked public examples. Do not claim a new item-by-item inspection of all 50.

## 2. Public mechanism evidence, with market boundaries

- **Boomshine (2007)**: one click creates an expanding circle; neighboring moving dots trigger further explosions. Useful: local reaction can itself be the spectacle. Source: https://www.kongregate.com/en/games/k2xl/boomshine
- **Arrow Out Puzzle**: arrow exit constraints and sequence; Google Play showed 500K+ downloads / 24K ratings as observed 2026-10-09; that is category evidence, not validation for a different fusion. Source: https://play.google.com/store/apps/details?id=arrow.out.puzzle.escape.logicpuzzle
- **SameGame**: tap connected-color group, remove, and remaining blocks fall/compress; useful: removal automatically changes future adjacency. Source: https://pysolfc.sourceforge.io/doc/rules/samegame.html
- **Drop7**: removal, gravity, new matches, chain; useful: state-dependent downstream changes. Source: https://drop7.dev/learn/rules
- **Arrows - Chain Escape**: Google Play description ALREADY specifies that releasing one unblocked arrow automatically releases arrows it was blocking. This is extremely close to the previously considered 'newly unlocked arrows auto leave' candidate. It should not be claimed as an original commercial differentiation; page showed unproven/low distribution rather than strong demand confirmation. Source: https://play.google.com/store/apps/details?id=team.liberty.arrows
- **Arrow Escape - Chain Reaction / Arrow Chain**: market listings already describe multi-tap arrow cascades and fewer-move goals. Descriptions do not establish significant uptake. Sources:
  - https://play.google.com/store/apps/details?id=com.shworan.arrowescape
  - https://play.google.com/store/apps/details?id=com.arrow.chain.escape.puzzle

Transferable pattern from user samples and Game Lab mechanism library:
`low input → local action/global payoff → board state alteration → another worthwhile choice`.
Do not conflate polished visual skins with a new rule.

## 3. Reject false solutions

### 3.1 'Only one hit per arrow' is bounded but may collapse to a single-file chain

If each node activates only one next node, the reaction has at most one live successor per event and loses branching spectacle. It becomes close to an '箭域迷阵' line puzzle. Merely renaming energy to one use does not fix the product pleasure loop.

### 3.2 Limited range without state reflow risks endgame cleanup

If a tapped arrow triggers only 1–3 neighbors in a forward cone and remaining nodes stay fixed, board density decreases monotonically. Late-game nodes get more isolated, producing repeated single-node taps.

### 3.3 Automatic unlock-on-removal is elegant, but sparse and already described in a shipped app

Under full-line-of-sight arrows, manual release of one free arrow triggers any arrow that becomes newly free solely due to its removal. It requires no energy. However a small toy simulation of 1,000 random 7×9 boards at 26 arrows averaged only ~1.48 removed arrows per legal first tap, and ~16% of boards had *any* initially legal tap releasing ≥5 arrows. These are **model experiments on uniform random arrow boards**, NOT human/market evidence or proof curated levels are weak. Market precedent above further downgrades originality.

## 4. Recommended rule candidate: Three-Neighbor Directional Cascade + Settle

Working name: `Arrow Cascade / 三邻接力`.

**Primary player action: TAP any remaining arrow**. There is no "blocked tap" in the first prototype.

### All arrows use the same rule

- Arrows retain existing 8 orientations.
- On activation, arrow removes itself, and a pulse reaches the **three immediately neighboring grid cells centered on its forward direction**.
- Any unremoved arrow in those 3 cells also activates and repeats the *same rule*.
- Each arrow may activate at most once in the entire tap/cascade; resolve simultaneously or via deterministic queue until no new arrow is reached.
- Once the entire cascade stops, remove activated arrows, and **remaining arrows fall vertically to fill column gaps**. Orientation is unchanged. Falling is a *settling step*, NOT another free activation in the first prototype.
- Player can then tap again. Clear the board, with visible manual taps used and optionally personal best. No tap limit or health penalty.

### Exact three neighbors for clarity

For `↑`, hit `↖ position / ↑ position / ↗ position` immediately one row above.

For `→`, hit `↗ position / → position / ↘ position` immediately one column to the right.

For `↗`, hit cells directly `up`, `up-right`, `right`.

Other directions rotate this three-cell mask. The directions of the *targets* do not affect whether they are hit; they affect how each target relays after being hit.

All outcomes use grid adjacency, not new energy values or arbitrary line-of-sight blockers.

### Why this stops naturally

The cascade stops at gaps / off-board; it does not need numeric energy. At high density a lucky seed may still clear most or all the board, which can be a rewarding occasional spectacle. The rules do not guarantee a fixed maximum chain size. The goal is natural *spatial* bounds rather than fixed budget.

### Why gravity is worth exactly one comparison

Removing arrows alone monotonically lowers density, weakening the next chain and ending with single-node mop-up. Settling to the bottom creates new neighbor contacts and may keep later cascades rewarding. This is one familiar automatic board-response rule, not a second player action.

## 5. Exploratory simulation (NOT game or playtest)

A simple JavaScript toy model with:
- 7×9 grid; 22 or 30 unique random arrow positions, eight orientations uniformly sampled.
- Three-forward-neighbor relay and full closure per tap.
- Random valid click policy, comparing static vs vertical settle after each cascade.
- Also a perfect-information greedy policy choosing currently largest removal on each settled board.
- 300 pseudo-random starting boards per node count/mode. No hand-curated shapes, no animation, no novice behavior, no production Solver.

| Board | Policy/physics | Mean taps to clear | Mean single-arrow cleanup taps | Mean largest chain during run |
|---|---|---:|---:|---:|
| 22 arrows | Random, static | 13.5 | 9.1 | 4.8 |
| 22 arrows | Random, settle | 7.1 | 3.4 | 10.1 |
| 22 arrows | Oracle greedy, settle | 5.3 | 1.8 | 9.9 |
| 30 arrows | Random, static | 14.4 | 8.6 | 7.6 |
| 30 arrows | Random, settle | 7.4 | 3.2 | 14.5 |
| 30 arrows | Oracle greedy, settle | 5.3 | 1.8 | 14.5 |

The **toy evidence is strongly supportive of testing settle** to counter the solitary-arrow cleanup pathology. It is not proof that a real player can predict the largest chain or enjoys the result.

Additional initial tap distribution under independent random 7×9 boards:
- 22 nodes: mean initial reach ~2.56 arrows for 1-cell 90° forward fan, versus ~8.68 for 2-cell fan.
- 30 nodes: mean ~4.02 for 1-cell fan, versus ~17.40 for 2-cell fan.

This suggests start with exactly one-cell range. Two cells may remove much of the board on the first tap and revive the one-click-only problem. All results are toy-model inferences, not validated design constants.

## 6. Contrast three minimal tests

A. `Local Cascade / Static`: current candidate three-cell propagation, no settling.
B. `Local Cascade / Gravity`: same initial board and tap logic + vertical settling after completed cascade.
C. `Original Classic`: stable V0.3.1, used only as a *different-product-frame benchmark* for feel. No Blast/Pop reactivation.

Start by comparing A vs B; only if B produces clear value should we develop curated stages.

Do not introduce blocking, energy digits, 90-degree menus, movable walls, health, timer, RPG growth, rewards, monetization or procedural shipping generator.

## 7. Explicit alternative frame and strongest counter-case

If the biggest pleasure is simply watching a chain, a modernized `Boomshine` / one-tap quota variant might be more direct than direction arrows. The arrows may add unnecessary cognition; test whether they genuinely change players' starting choices.

Strongest arguments AGAINST candidate:
- Even with gravity, tap-anything always clears board eventually; it may lack challenge.
- Remaining arrows eventually bottom-stack; visible arrow directions could become harder to mentally trace after movement.
- Greedy-best vs random difference exists in model but might be invisible to people.
- The product resembles existing SameGame / chain pop systems; mechanically novel enough for a prototype is NOT proof of distribution differentiation.
- Visual feedback already favors Classic + Synth; don't default to noisy bursting because objects disappear.
- Solo-founder hidden cost may become content curation if random boards have erratic cascade balance.

Kill / degrade if:
- 3 boards played without tutorial lead to mostly indiscriminate tapping with no sense of one choice being better;
- players consistently prefer watching demo to playing or no desire for another board;
- gravity confuses causal readability more than it helps continuation;
- after choosing B the majority of real taps still just remove one arrow and feel like cleanup.

## 8. Next evidence and scope

**Decision: TEST, not BUILD approved.**

If implementation is authorized, create ONLY `prototype/arrow-cascade-rule-lab.html`, no edits to canonical V0.3.1 or Solver.

Prototype:
- same 3 curated 7×9 boards with 22–30 arrows,
- selectable `Static / Gravity` with same start board,
- 8-direction glyphs + preferred colors + original Synth Hit,
- one-finger taps, animated cascading dots, gravity settle,
- simple taps counter and no failure punishment,
- debug trace (seeds, activation sets, remaining position hash), independent variant unit checks,
- no new audio/assets/skins/numbered arrows/obstacles/Meta.

Human observation:
- Does the player voluntarily search for a larger chain?
- Does gravity produce an enjoyable second decision?
- Are endgame singleton cleanups less frequent and less annoying?
- Would the player replay to use fewer taps?
- Does the arrow direction meaningfully change choices, compared with colorless/undirected bubble pops?

## 9. Decision Log

- Decision: preserve canonical Chain Shot; narrow new fork to three-forward-neighbor chain + one post-chain gravity response.
- Evidence: observed Classic simplicity shortcut; analogous sources; toy-model reduction in cleanup taps / improved largest chain.
- Counter: automatic clearing with no failure might be a toy; adjacent arrow direction and gravity may not be intuitive; existing market analogues.
- Unknowns: human comprehension, fun, replay, 30-second session rhythm, actual optimization decisions, demand/distribution.
- Falsification: identical blind tapping behavior with or without gravity and no desire for repeat.
- Next Evidence: smallest two-variant side-by-side HTML experiment before V0.4 or a new commercial game identity.
