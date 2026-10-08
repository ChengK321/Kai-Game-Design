# Chain Unlock Research — Blocking × Numeric Energy × Cascade

> 2026-10-09 | RESEARCH / PROPOSED FOR AN INDEPENDENT RULE LAB, NOT V0.4
> Decision owner: Chain Shot master design conversation
> Current playable reference: `prototype/chain-shot-v0.3.1.html`
> Immutable baseline: Classic + Synth Hit + Direction-family, existing 10 levels & Solver
> Labels: MARKET SOURCE, USER OBSERVATION, LOGIC, INFERENCE, HYPOTHESIS

## 1. Question and decision

Can a *blocked arrow* + *visible energy number* interact to create a new high-density loop, instead of adding two independent difficulty systems?

**Provisional decision: TEST CONDITIONAL CHAIN UNLOCK in a separate 3-board Rule Lab; HOLD any main-game rule changes.**

One-line player promise:

**点可启动的箭头，用有限连锁清掉挡路的节点，解锁下一次更大的连锁，尽量少点几次清盘。**

The product hypothesis is not simply "arrows have numbers". It is:
`Read blockade → pick available ignition → limited cascade clears a region → new available ignitions → repeat`.

## 2. Evidence from user game library

The prior 50-game / 120-screenshot user-supplied Gamelab collection (reviewed in an earlier conversation; screenshots, NOT executable source) identified:
- 箭域迷阵: direction/ray cascade, original inspiration of Chain Shot.
- 多米诺效应: directional relay and chain payoff.
- 数字约束/路径类: small visible numeric constraint guiding actions.
- 旋转拼图/状态切换: local move alters available future moves.

This supports **mechanic extraction**, not claims that the precise new combination was in those screenshot games or is a proven commercial success.

## 3. Market evidence (as publicly observed on 2026-10-09)

- Google Play Arrow Escape: Maze Puzzle Out, 1M+ visible download tier. Players clear arrows in order; blocked arrows don't leave the board. https://play.google.com/store/apps/details?id=com.arrow.puzzle
- Google Play Arrow Out Puzzle, 500K+ visible download tier. Developer description emphasizes careful order and collisions. https://play.google.com/store/apps/details?id=arrow.out.puzzle.escape.logicpuzzle
- Google Play Arrow Maze / Arrow Out official descriptions: blocked move gives no escape and sometimes costs a life. This *category* is established; don't infer our mechanic has been validated.
- Open source ChainReaction: cells reach critical capacity, burst, distribute orbs to neighbours; cascades follow. https://github.com/jubich/ChainReaction
- Numeric chain logic: Drop7 rules and cascade (secondary detailed rules reference) https://drop7.dev/learn/rules
- **Primary interview / developer's own reported speech**: `一箭又一箭` developer He Yikun reports their attempt to add color-target / buffer mechanics reduced simplicity and pleasure; they reverted and used sparse low-frequency additions instead. Team-reported 30–40 levels/day average and AI level generator/solver work are self-reported, not independent estimates. https://news.yxrb.net/2026/0528/7007.html

Market conclusion: blocking-based arrow puzzles have visible distribution; numerical chain cascades are established; **their fusion is currently a hypothesis**, not a demonstrated market gap or bestseller.

## 4. Critical contradiction to resolve

In familiar Arrow Out logic: if another arrow blocks the entire forward exit path, the selected arrow cannot move.

In classic Chain Shot: a pulse intentionally passes through/activates encountered arrows.

If a single rule simultaneously means "any arrow ahead blocks the pulse" AND "the pulse must hit arrows to start a chain", the system contradicts itself.

**Do not implement that naively.**

Distinguish a physical *manual launch* from a transmitted *automatic energy burst*, with explicit visuals and instructions, or reject the merger if novice users cannot understand the distinction.

## 5. Smallest coherent integrated candidate (HYPOTHESIS)

Working name: `Chain Unlock / 连锁解锁`.

### Board

- 6×7 sparse grid, around 10–16 arrows for experimental boards.
- Each arrow has an 8-direction marker and an integer STARTING charge `n ∈ {1,2,3}`.
- No permanent stone walls, traps, special arrows, timers, lives, skills or currency.
- Direction colors inherit the preferred V0.3.1 family scheme; sound inherits synthesized Hit.

### Manual launch — dynamic obstruction

- A tap is valid **only if the one immediately adjacent cell in the displayed arrow's direction is empty or outside the board**.
- If it is occupied by another arrow: a short bump / blocked marker, **no effect on board and no health penalty**.
- This is intentionally a **one-cell launch clearance** variant, NOT a claim to copy Arrow Out's full exit-path clearance. It allows a launch then a wave to reach targets farther away.
- A successful manual launch consumes/removes its own arrow.

### Wave — first playable proposal

- From the launched arrow's original position, emit a short forward-directed **90° cone** reaching up to **2 grid cells** (fixed range for all nodes).
- Every arrow hit by this wave is consumed/removed. It automatically emits another cone in *its own direction* if transmitted wave energy remains.
- The STARTING charge `n` printed on an arrow applies **only when that arrow is manually selected as a Seed**. A relay node *does not replenish* a wave based on its printed starting charge.
- For a Seed with n=3: it may propagate up to three directed waves; every relay lowers wave energy by one. A final node hit at zero is removed but does not emit another wave.
- Handle same-wave hits simultaneously; an arrow may only be removed once; no order-dependent duplicate relay. Ensure energy/branch decisions are deterministic (e.g. process max incoming energy on same-tick collision, document exact tie behavior).
- This asymmetry (manual launch blocked, incoming-triggered relay does not require clearance) is an explicit **cognitive-risk hypothesis**: start arrow physically launches; hit arrow auto-bursts at its current position. If testers find it arbitrary, stop.

### Game objective

- Clear the board in as few **successful manual taps** as possible.
- First experiments show click count, but no hard cap or punishment. Invalid taps counted separately only for diagnostics.
- If no arrow can manually launch while arrows remain, show clearly blocked/deadlocked state and allow instant retry. Solver must reject such boards for the test set.
- Never claim "more arrow count" automatically improves challenge.

### Why this combination might create strategy

- A high-charge arrow behind a blockage is initially inaccessible.
- Choosing an eligible lower-charge arrow can remove the blocker, changing which arrows can be tapped.
- An early choice therefore influences the availability of a later high-charge cascade.
- Numeric charge can guide ordering, not simply higher value always winning.
- Every valid tap changes the board, unlike original one-tap-full-board attempt.

## 6. Simplicity audit

This prototype still carries cognitive risks:

1. Clicking blocked source does nothing, yet an automatically hit blocked arrow can still burst. Does the player distinguish **manual launch** vs **automatic relay**?
2. Numbers are **starter fuel only** and do not refill upon auto-trigger. Is this obvious?
3. Players may simply pick highest available number every time.
4. Initial board can form complete block cycles (no legal launch).
5. Once most of the board is cleared, last 2–3 arrows may become dull mop-up.
6. Combined direction glyph + number + direction colors might hurt reading on a mobile screen.

Therefore do not preapprove ten levels, a polished UI, a runtime level generator or an FX upgrade.

## 7. Discriminating experiments (three variants, same layout principles)

**A — Block-only**: Arrow Out-like next-cell clearance; each legal tap removes one; no chain/no energy. Control for the unlocking pleasure alone.

**B — Block + Fixed Relay**: Manual next-cell clearance; each valid tap initiates a direction-cone relay with fixed 2–3 wave depth; no per-arrow numbers. Tests whether a combination of blocking + chained mass clearing is already enough.

**C — Block + Numeric Relay**: Same as B, but each arrow displays starting charge 1–3 determining manual-seed depth. Tests whether numbers add meaningful choice or just reading overhead.

Keep EXACT parameters fixed within each comparison (shape, target distribution, animation baseline, count objective) except the new rule under test; do not claim perfect equivalent difficulty across mechanically distinct arms.

### Gate

- Unprompted novice can explain blocked tap, hit relay, and ending of wave after 1–2 rounds.
- At least two legal seeds offer observably different downstream board states.
- At least once a move unblocks a previously unavailable high-value arrow.
- Some players choose a lower-energy seed for sequencing reasons, rather than always taking highest N.
- Player voluntarily tries a different sequence to improve tap count.
- The last quarter of the board does not become 3–5 repetitive singleton taps.

**Kill / Hold signals**:
- B is no better than A → cascade adds spectacle but not decision value; stop before C.
- C is no better than B → remove visible energy numbers.
- Users cannot understand manual vs auto activation distinction → simplify block rule, do not explain with lengthy tutorials.
- Every board is solved by "tap highest available number" → numeric mechanic has failed to create depth.
- No desire to optimize taps after three boards → consider relaxing to purely sensory toy or HOLD.

## 8. Engineering scope if later authorized

Separate `prototype/chain-unlock-rule-lab.html`, 3 small curated boards + tiny independent transition checker.

**Do not modify** original Chain Shot V0.3.1, the canonical 10 levels, Solver, FX Lab, or the Reverse Seed proposal. The new solver needs full board-state search with dynamic unlock/removal and minimum manual taps; old one-shot reachability cannot validate this game unchanged.

Prefer read-only initial design review, then one scoped Codex implementation brief after explicit approval.

## 9. Decision Log

- **Decision**: A/B/C staged experiment is worthy of a small fork; no mainline migration.
- **Evidence**: current market's obstruction/sequence examples; chain-reaction precedents; Chain Shot single-seed graph weakness; user's desire for a new local-clearing loop.
- **Strongest Counter**: adding starter numbers and automatic relay roles may recreate the very complexity that 《一箭又一箭》 developers reportedly discarded.
- **Unknowns**: comprehension, emergent strategy, distinct outcomes, tap-count motivation, audience fit, scope of manual-vs-auto asymmetry.
- **Falsification**: no more deliberate choices or voluntary replays compared with B; user primarily sees confusing arbitrary blocked clicks.
- **Next Evidence**: 3-board A/B/C rule-lab, short human sessions, no artwork investment.
