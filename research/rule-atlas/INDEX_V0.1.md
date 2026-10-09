# Kai Game Lab — Rule Atlas V0.1

Date: 2026-10-09
Status: Lightweight research index; not a product roadmap
Source of truth: Kai-Game-Design GitHub. main keeps mature cross-project conclusions; raw hypotheses and candidates stay on research/concept branches.

## Goal
Preserve reusable mechanisms across genres without mixing one game's skin/theme, a rule, a pleasure loop, and product validation into one category. Prevent blind over-investment in a single game. Discover and kill cheaply. Cross-pollinate without assuming a combination improves the game.

## Classification: three independent axes
- Pleasure loop: deduction/forced discovery; space management/survival; chain feedback; trajectory prediction; state repair/optimization; reward-risk tradeoff.
- Action primitive: tap-to-fill/toggle; place/remove; slide/rotate; swap; draw/aim; select group.
- State/constraint engine: static intersecting constraints; finite deterministic state puzzle; dynamic state + capacity pressure; physics trajectory; simultaneous propagation.

One concept can have multiple tags across axes. Do NOT assign a single rigid game genre as its identity.

## Minimal record for each candidate
ID | One-line Rule | Pleasure Loop | Player Action | State Engine | Adjacent Prior Art | Novelty (Unverified/Partial) | Biggest Counter-Case | Status | Next Evidence | Kill Condition | Branch/URL

Status vocabulary: DISCOVERED -> WATCH -> RULE_PROBE -> HUMAN_PROBE -> PROTOTYPE -> VALIDATED / KILLED.
These states track evidence, not excitement, commercial potential, or originality. When research is only a sketch, keep it WATCH. The stages aren't mandatory bureaucratic gates.

## Existing and new entries
| ID | Mechanism / candidate | Loop | Action | Engine | Status | Primary record |
| --- | --- | --- | --- | --- | --- | --- |
| REF-2048 | 2048 (reference, not owned concept) | spatial capacity / growth | 4-direction swipe | dynamic state + new tile spawn | REFERENCE | research/gamelab-50/emergent-puzzle-v0.2.md on main |
| GL-PEEL | Endless Peel | capacity / trade-off | select exposed end color | dynamic spawn / removal | HUMAN_PROBE_PENDING | concept/peel-peel + research/gamelab-50/one-rule-validation-v0.3.md |
| GL-RING | Ring Shift | repair / tactical planning | shift whole row/column | dynamic spawn / color match | WATCH | concept/ring-shift |
| GL-SWALLOW | Swallow Slide | growth / spatial planning | slide | hypothesis | WATCH | concept/swallow-slide |
| GL-INK | Flip Ink | propagation / state change | toggle | synchronous propagation unverified | WATCH | concept/flip-ink |
| SDK-01 | Switch Count / 变色密码 | logical forced discovery | fill black/white | static row/col transition clues | WATCH | research/sudoku-rule-lab/CONCEPTS_V0.1.md |
| SDK-02 | One Lamp Per Line / 交点亮灯 | overlapping constraint deduction | tap node | static exact-one on overlapping subsets | WATCH | same |
| SDK-03 | Four-Color Repair / 四色修复 | spatial repair / move optimization | adjacent swap | scramble / constrained target state | WATCH / PRIOR-ART-RISK | same |

## Attention budget
- Across unrelated themes, compare underlying loops and playtest results, not surface theme.
- No formal production branch for WATCH proposals; create concept branch only when concrete validation warrants it.
- Keep no more than 3 active unvalidated Sudoku DNA proposals. If a new idea comes in, archive, replace, or promote an old one rather than snowball.
- Every research iteration ends with Decision + Counter Evidence + Unknown + Next Evidence/Kill.
- Neither mathematical solvability nor automated agent advantage implies players will have fun or return.
